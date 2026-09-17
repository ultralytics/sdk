# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license
"""Unified Ultralytics CLI: local YOLO commands and Platform SDK operations discovered from the SDK itself."""

from __future__ import annotations

import importlib.util
import inspect
import json
import os
import sys
import time
import types
import typing
import zipfile
from collections.abc import Sequence
from contextlib import ExitStack
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from tarfile import is_tarfile
from tempfile import TemporaryDirectory
from typing import Any, BinaryIO, Literal, get_args, get_origin, get_type_hints

from . import NOT_GIVEN, APIConnectionError, APIError, NotGiven, Platform
from ._cli_metadata import MULTIPART_FILES

JSON_TYPES = {type(None): "null", bool: "boolean", int: "integer", float: "number", str: "string", list: "array"}
JSON_TYPES |= {dict: "object", Sequence: "array"}
OFFICIAL_FAMILIES = ("yolo26", "yolo11", "yolov8", "yolov5")  # public ultralytics/<family> projects on Platform


def platform_url() -> str:
    """Platform origin, read per invocation so ULTRALYTICS_PLATFORM_URL applies after import."""
    return os.getenv("ULTRALYTICS_PLATFORM_URL", "https://platform.ultralytics.com").rstrip("/")


def kinds(annotation: Any) -> tuple[set[str], list | None]:
    """Map a generated SDK annotation to JSON kinds and literal choices; empty kinds accept any JSON value."""
    if annotation is Any:
        return set(), None
    if annotation is BinaryIO:
        return {"binary"}, None
    origin = get_origin(annotation)
    if origin is Literal:
        values = list(get_args(annotation))
        return {JSON_TYPES[type(value)] for value in values}, values
    if origin in {types.UnionType, typing.Union}:
        members = [member for member in get_args(annotation) if member is not NotGiven]
        parts = [kinds(member) for member in members]
        if any(not part[0] for part in parts):
            return set(), None
        literal = all(get_origin(member) is Literal or member is type(None) for member in members)
        return set().union(*(part[0] for part in parts)), [
            v for _, c in parts for v in c or [None]
        ] if literal else None
    return {JSON_TYPES[origin or annotation]}, None


def describe(method) -> dict[str, dict]:
    """Argument descriptors from the SDK signature: positional parameters are path parameters."""
    hints = get_type_hints(method)
    result = {}
    for parameter in inspect.signature(method).parameters.values():
        if parameter.name in {"timeout", "extra_headers"}:
            continue
        types_, choices = kinds(hints[parameter.name])
        result[parameter.name] = {
            "types": types_,
            "choices": choices,
            "required": parameter.default is parameter.empty,
            "path": parameter.kind is parameter.POSITIONAL_OR_KEYWORD,
        }
    return result


def assignments(tokens: list[str]) -> dict[str, str | None]:
    """Allow spaces before '=' while preserving empty values and subsequent shell arguments."""
    result = {}
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if i + 1 < len(tokens) and tokens[i + 1].startswith("=") and "=" not in token:
            i += 1
            token += tokens[i]
        key, separator, value = token.partition("=")
        i += 1
        if (key.startswith("-") and token not in {"--help", "-h"}) or not key:
            raise ValueError("Use key=value arguments, not --key value")
        if key in result:
            raise ValueError(f"duplicate argument: {key}")
        result[key] = value if separator else None
    return result


def parse(raw: dict[str, str | None], arguments: dict[str, dict]) -> dict:
    """Convert supplied arguments using the SDK signature; only supplied values reach the SDK."""
    result = {}
    stdin_used = False
    for name, text in raw.items():
        if name not in arguments:
            raise ValueError(f"unknown argument: {name}")
        arg = arguments[name]
        kinds_ = {"string"} if "binary" in arg["types"] else arg["types"]
        if text is None:
            if kinds_ - {"null"} != {"boolean"}:
                raise ValueError(f"{name} requires a value; only booleans may be bare")
            text = "True"
        if text.startswith("@") and (not kinds_ or kinds_ & {"object", "array"}):
            if text == "@-":
                if stdin_used:
                    raise ValueError("stdin can supply only one input")
                stdin_used = True
                text = sys.stdin.read()
            else:
                try:
                    text = Path(text[1:]).read_text(encoding="utf-8")
                except OSError as error:
                    raise ValueError(f"{name}: cannot read JSON input file") from error
        expected = "|".join(sorted(kinds_)) or "JSON"
        try:
            if text.lower() in {"null", "none"} and (not kinds_ or "null" in kinds_):
                value = None
            elif kinds_ - {"null"} == {"string"}:
                value = text
            elif "boolean" in kinds_ and text.lower() in {"true", "false"}:
                value = text.lower() == "true"
            elif kinds_ - {"null"} == {"integer"}:
                value = int(text)
            elif kinds_ - {"null"} == {"number"}:
                value = float(text)
            else:
                value = json.loads(text)
            json.dumps(value, allow_nan=False)  # Reject non-finite numbers at any depth.
        except ValueError as error:
            raise ValueError(f"{name}: expected {expected}; objects and arrays require valid JSON") from error
        actual = JSON_TYPES.get(type(value))
        if kinds_ and actual not in kinds_ and not (actual == "integer" and "number" in kinds_):
            raise ValueError(f"{name}: expected {expected}")
        if arg["choices"] is not None and value not in arg["choices"]:
            raise ValueError(f"{name}: choose one of {json.dumps(arg['choices'])}")
        result[name] = value
    missing = [
        n for n, a in arguments.items() if a["required"] and n not in result and not (a["path"] and n == "owner")
    ]
    if missing:
        raise ValueError(f"missing arguments: {', '.join(missing)}")
    return result


def open_inputs(values: dict, arguments: dict[str, dict], files: list[str], stack: ExitStack) -> dict:
    """Open binary arguments and the multipart body fields the generator identified as binary."""
    fields = [(values, name) for name, arg in arguments.items() if "binary" in arg["types"] and name in values]
    fields += [
        (values["body"], field) for field in files if isinstance(values.get("body"), dict) and field in values["body"]
    ]
    for container, key in fields:
        value = container[key]
        if not isinstance(value, str) or not value.startswith("@") or value == "@-":
            raise ValueError(f"{key}: binary inputs require @path (not stdin)")
        container[key] = stack.enter_context(open(value[1:], "rb"))  # noqa: SIM115 - caller owns the ExitStack
    return values


def output(value) -> None:
    """Write one complete SDK response to stdout; never fetch additional pages."""
    if isinstance(value, bytes):
        sys.stdout.buffer.write(value)
    elif isinstance(value, str):
        print(value)
    else:
        print(json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False))


def defaults(methods: dict[str, Any]) -> dict[str, list[str]]:
    """Implicit verbs: bare `list`, and `retrieve` when its extra path identifiers are supplied."""
    if "list" not in methods:
        return {}
    result = {"list": []}
    if "retrieve" in methods:
        parents = {name for name, arg in describe(methods["list"]).items() if arg["path"]}
        identifiers = [
            name for name, arg in describe(methods["retrieve"]).items() if arg["path"] and name not in parents
        ]
        if identifiers:
            result["retrieve"] = identifiers
    return result


def yolo_args(tokens: list[str]) -> dict:
    """Type key=value arguments the way `yolo` does; Alpha validates their values."""
    from ultralytics.cfg import DEFAULT_CFG_DICT, smart_value
    from ultralytics.utils import YAML
    from ultralytics.utils.checks import check_model_file_from_stem

    raw = assignments(tokens)
    args = YAML.load(Path(raw.pop("cfg")).expanduser()) if raw.get("cfg") else {}
    args.update({key: True if value is None else smart_value(value) for key, value in raw.items()})
    if unknown := set(args) - set(DEFAULT_CFG_DICT) - {"gpu_type", "save_dir"}:
        raise ValueError(f"Unknown YOLO arguments: {', '.join(sorted(unknown))}")
    for key in ("project", "name", "save_dir"):
        if args.get(key) is not None:
            args[key] = str(args[key])
    if args.get("model") is not None:
        args["model"] = str(check_model_file_from_stem(str(args["model"])))  # yolo26n -> yolo26n.pt, as YOLO does
    return args


def resolve_project(client: Platform, project: str | None) -> tuple[str, str]:
    """Return the owner and slug of an existing project, creating the private cloud-training default."""
    from ultralytics.utils.callbacks.platform import slugify

    owner = client.account.summary()["username"]
    slug = slugify(Path(str(project)).resolve().name) if project else "cloud-training"
    try:
        if client.projects.retrieve(owner, slug)["project"]["visibility"] != "private" and project is None:
            raise ValueError("Project cloud-training is public; pass project= or make it private")
    except APIError as error:
        if error.status_code != 404:
            raise
        slug = client.projects.create(owner=owner, project=slug, name=slug, visibility="private")["project"]
    return owner, slug


def upload_file(client: Platform, path: Path, asset_type: str, asset_id: str) -> str:
    """Upload one dataset archive or checkpoint and return its completed upload session."""
    from ultralytics.utils.uploads import safe_upload

    signed = client.upload.signed_url(
        body={
            "assetType": asset_type,
            "assetId": asset_id,
            "filename": path.name,
            "contentType": "application/octet-stream",
            "totalBytes": path.stat().st_size,
        }
    )
    if not safe_upload(path, signed["uploadUrl"], headers=signed.get("headers"), progress=True):
        raise APIConnectionError(f"Upload failed: {path.name}")
    client.upload.complete(session_id=signed["sessionId"])
    return signed["sessionId"]


def platform_model(model: Any) -> str | None:
    """Return the ul:// URI of a Platform model or hosted official weights; None means a checkpoint to upload."""
    from ultralytics.utils.downloads import GITHUB_ASSETS_NAMES

    model = str(model)
    if model.startswith("ul://"):
        return model
    if Path(model).is_file():  # a local file wins over same-named official weights, as in local YOLO
        return None
    if model in GITHUB_ASSETS_NAMES and (family := next((f for f in OFFICIAL_FAMILIES if model.startswith(f)), None)):
        return f"ul://ultralytics/{family}/{Path(model).stem}"
    return None


def upload_model(client: Platform, model: Any, owner: str, project: str) -> str:
    """Upload a local .pt checkpoint as a new model of the project and return its ul:// URI."""
    from ultralytics import YOLO
    from ultralytics.utils.callbacks.platform import slugify

    path = Path(str(model)).expanduser()
    if not path.is_file() or path.suffix != ".pt":
        raise ValueError(
            f"model= must be a local .pt file, ul://owner/project/model, or {'/'.join(OFFICIAL_FAMILIES)} weights: {model}"
        )
    body = {"owner": owner, "project": project, "model": slugify(path.stem), "name": path.stem, "task": YOLO(path).task}
    created = client.models.create(body=body)
    upload_file(client, path, "models", created["id"])
    uri = f"ul://{created['owner']}/{created['project']}/{created['model']}"
    print(f"Model: {uri}")
    return uri


def package_dataset(dataset: Path, destination: str, task: str | None) -> Path:
    """Zip the declared splits of a local dataset with their labels, masks, or depth maps.

    Existing archives pass through. A directory without a YAML is a classification dataset of class folders.
    """
    from ultralytics.data.utils import IMG_FORMATS, check_det_dataset, find_dataset_yaml
    from ultralytics.utils import YAML

    source = dataset.resolve()
    task = task or ("classify" if source.is_dir() and not any(source.rglob("*.yaml")) else "detect")
    if source.is_file() and (zipfile.is_zipfile(source) or is_tarfile(source)):
        return source
    yaml_file, declared = None, {}
    if task == "classify":
        root, directories = source, [source / split for split in ("train", "val", "test")]
        if not (source / "train").is_dir() or not any((source / split).is_dir() for split in ("val", "test")):
            raise ValueError("Classification data requires train/ and val/ or test/ class directories")
    else:
        yaml_file = find_dataset_yaml(source) if source.is_dir() else source
        if yaml_file.suffix.lower() not in {".yaml", ".yml"}:
            raise ValueError("Local data must be a dataset YAML, directory, ZIP, or TAR archive")
        data = check_det_dataset(str(yaml_file), autodownload=False)
        root, declared = Path(data["path"]), YAML.load(yaml_file)  # declared paths keep symlinked splits under root
        values = [declared[split] for split in ("train", "val", "test") if declared.get(split)]
        splits = [root / value for item in values for value in (item if isinstance(item, list) else [item])]
        if not all(split.is_dir() and Path(os.path.abspath(split)).is_relative_to(root) for split in splits):
            raise ValueError("Cloud uploads require split directories under the dataset root, not image lists")
        siblings = ("labels", data.get("masks_dir") or "masks", "depth")  # YOLO mirrors images/ per split
        directories = splits + [Path(*(n if p == "images" else p for p in s.parts)) for s in splits for n in siblings]
    archive = Path(destination) / f"{root.name}.zip"
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as output:
        if yaml_file:  # splits are relative to the archive root; a local path: key would point outside it
            YAML.save(archive.with_name("data.yaml"), {key: value for key, value in declared.items() if key != "path"})
            output.write(archive.with_name("data.yaml"), "data.yaml")
        for file in sorted({file for directory in directories for file in directory.rglob("*")}):
            if (
                file.is_file()
                and not any(part.startswith(".") for part in file.relative_to(root).parts)
                and file.suffix[1:].lower() in IMG_FORMATS | {"txt", "npy"}
            ):
                output.write(file, file.relative_to(root))
    return archive


def wait_job(fetch) -> dict:
    """Wait for a submitted cloud job and fail if it does not complete successfully."""
    last = None
    while True:
        job = fetch()
        if job is None:
            raise ValueError("Cloud job is no longer available")
        if job["status"] not in {"pending", "untrained", "queued", "starting", "running"}:
            break
        if (line := f"{job['status']}: {job.get('progress', '')}") != last:
            print(line, flush=True)
            last = line
        time.sleep(5)
    if job["status"] != "completed":
        raise ValueError(f"Cloud job {job['status']}: {(job.get('error') or {}).get('message', '')}")
    return job


def download_file(url: str, target: Path) -> Path:
    """Download a fresh artifact before replacing an existing output file."""
    from ultralytics.utils.downloads import safe_download

    target.parent.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(dir=target.parent) as temporary:
        downloaded = safe_download(url, file=target.name, dir=temporary, unzip=False)
        Path(downloaded).replace(target)
    print(f"Saved: {target}")
    return target


def cloud_train(client: Platform, tokens: list[str]) -> int:
    """ul cloud train model=yolo26n.pt data=ul://owner/datasets/slug epochs=100 [gpu_type=rtx-4090]

    Local .pt weights and dataset YAMLs, directories, ZIPs, or TARs are uploaded automatically.
    project= selects the output project; default: private cloud-training.
    Waits for completion and saves weights/best.pt, args.yaml, results.csv, and job details locally.
    """
    import csv

    from ultralytics import YOLO
    from ultralytics.cfg import DEFAULT_CFG_DICT, TASK2MODEL, get_cfg, get_save_dir
    from ultralytics.utils import YAML
    from ultralytics.utils.callbacks.platform import slugify
    from ultralytics.utils.downloads import GITHUB_ASSETS_NAMES

    args = yolo_args(tokens)
    if not isinstance(args.get("data"), str) or not args["data"]:
        raise ValueError("data= is required: use a Platform dataset URI or local dataset")
    args.setdefault("model", TASK2MODEL.get(args.get("task"), "yolo26n.pt"))
    args.setdefault("epochs", DEFAULT_CFG_DICT["epochs"])
    local_args = args.copy()
    gpu_type, project, name = args.pop("gpu_type", NOT_GIVEN), args.pop("project", None), args.pop("name", None)
    for key in ("device", "exist_ok", "save_dir"):  # local-only arguments; the worker assigns its own GPU
        args.pop(key, None)
    if "cache" in args and not isinstance(args["cache"], str):
        args["cache"] = "ram" if args["cache"] else "false"
    local_data = Path(args["data"]).expanduser()
    if not local_data.exists():  # ul:// URIs and built-in names such as coco8.yaml are resolved by Platform
        local_data = None
    with TemporaryDirectory(prefix="ul-cloud-train-") as temporary:
        archive = package_dataset(local_data, temporary, args.get("task")) if local_data else None
        owner, project_slug = resolve_project(client, project)
        model = args["model"]
        if Path(model).is_file() or not (model.startswith("ul://") or model in GITHUB_ASSETS_NAMES):
            args["model"] = upload_model(client, model, owner, project_slug)
        else:  # hosted official weights map to their public model; other official names stay bare for the worker
            args["model"] = platform_model(model) or model
        if archive:
            dataset = client.datasets.create(  # Platform infers the task from the labels during ingest
                owner=owner, dataset=slugify(archive.stem) or "dataset", name=archive.stem, visibility="private"
            )
            args["data"] = f"ul://{dataset['owner']}/datasets/{dataset['dataset']}"
            print(f"Dataset: {args['data']} (reuse this URI to skip uploading next time)")
            session = upload_file(client, archive, "datasets", dataset["id"])
            client.datasets.ingest(dataset["owner"], dataset["dataset"], body={"sessionId": session})
            state = {"status": "processing"}
            while state["status"] == "processing":
                time.sleep(2)
                state = client.datasets.retrieve(dataset["owner"], dataset["dataset"])["dataset"]
            if state["status"] == "failed":
                raise ValueError(f"Dataset ingestion failed; inspect {args['data']}: {state.get('processingError')}")
        body = {"owner": owner, "project": project_slug}
        if name:
            body |= {"model": slugify(name), "name": name}
        target = client.models.create(body=body)
        print(
            f"Run: {platform_url()}/{target['owner']}/{target['project']}/{target['model']} (model_id={target['id']})"
        )
        output(client.training.start(model_id=target["id"], train_args=args, gpu_type=gpu_type))
        model_path = (target["owner"], target["project"], target["model"])
        job = wait_job(lambda: client.models.training(*model_path)["job"])
        model = client.models.retrieve(*model_path)["model"]
        directory = get_save_dir(
            get_cfg(DEFAULT_CFG_DICT | local_args | {"mode": "train", "task": model.get("task") or "detect"})
        )
        files = client.models.files(*model_path)["files"]
        if not files:
            raise ValueError("Training completed without a downloadable checkpoint")
        checkpoint = YOLO(download_file(files[0]["downloadUrl"], directory / "weights" / "best.pt")).ckpt
        YAML.save(directory / "args.yaml", checkpoint["train_args"])
        if results := checkpoint.get("train_results"):
            with directory.joinpath("results.csv").open("w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(results)
                writer.writerows(zip(*results.values()))
        directory.joinpath("results.json").write_text(json.dumps(job, indent=2))
        output(job)
    return 0


def prediction_result(image, path: str, prediction: dict, names: dict, task: str, args):
    """Adapt Platform summaries to YOLO Results so its plotting and saving stay the single owner."""
    import base64

    import cv2
    import numpy as np
    from ultralytics.data.utils import polygons2masks
    from ultralytics.engine.results import Results
    from ultralytics.utils.ops import xyxyxyxy2xywhr

    rows, values = prediction["results"], {}
    if task == "classify":
        values["probs"] = np.zeros(len(names), dtype=np.float32)
        for row in rows:
            values["probs"][row["class"]] = row["confidence"]
    elif task not in {"semantic", "depth"}:
        if args.classes is not None:  # Platform predicts every class; apply YOLO's class filter and detection cap here
            classes = {args.classes} if isinstance(args.classes, int) else set(args.classes)
            rows = [row for row in rows if row["class"] in classes]
        rows = rows[: args.max_det]
        boxes = np.array([list(row["box"].values()) for row in rows], dtype=np.float32).reshape(
            -1, 8 if task == "obb" else 4
        )
        if task == "obb":
            boxes = xyxyxyxy2xywhr(boxes)
        scores = np.array([[r["confidence"], r["class"]] for r in rows], dtype=np.float32).reshape(-1, 2)
        values["obb" if task == "obb" else "boxes"] = np.concatenate((boxes, scores), axis=1)
        if rows and "segments" in rows[0]:
            polygons = [np.array(list(zip(r["segments"]["x"], r["segments"]["y"]))).ravel() for r in rows]
            values["masks"] = polygons2masks(image.shape[:2], polygons, color=1)
        if rows and "keypoints" in rows[0]:
            values["keypoints"] = np.array(
                [
                    np.stack([r["keypoints"][k] for k in ("x", "y", "visible") if k in r["keypoints"]], axis=-1)
                    for r in rows
                ],
                dtype=np.float32,
            )
    for key in ("semantic_mask", "depth"):
        if key in prediction:
            encoded = prediction[key]
            pixels = cv2.imdecode(np.frombuffer(base64.b64decode(encoded["data"]), np.uint8), cv2.IMREAD_UNCHANGED)
            if key == "depth":
                pixels = pixels.astype(np.float32) * encoded["max"] / (255 if encoded["bits"] == 8 else 65535)
                pixels = cv2.resize(pixels, (image.shape[1], image.shape[0]))
            values[key] = pixels
    return Results(image, path, names, speed=prediction["speed"], **values)


def save_predictions(source: Path, response: dict, args: dict) -> None:
    """Reuse YOLO's image/video, label, crop, and display writers without running local inference."""
    import numpy as np
    from ultralytics.cfg import DEFAULT_CFG_DICT
    from ultralytics.data.build import load_inference_source
    from ultralytics.engine.predictor import BasePredictor
    from ultralytics.nn.autobackend import default_class_names

    metadata = response["metadata"]  # classNames and task are optional in the contract
    names = dict(enumerate(metadata["classNames"])) if metadata.get("classNames") else default_class_names()
    if (task := metadata.get("task")) is None:
        raise ValueError("Platform did not report the model task, so predictions cannot be converted")
    writer = BasePredictor(cfg=DEFAULT_CFG_DICT | args | {"task": task, "mode": "predict"})
    directory = writer.save_dir
    writer.dataset = load_inference_source(str(source), batch=1)
    writer.source_type = writer.dataset.source_type
    if writer.args.save or writer.args.save_txt or writer.args.save_crop:
        directory.mkdir(parents=True, exist_ok=True)
        directory.joinpath("results.json").write_text(json.dumps(response, indent=2))
    try:
        for (paths, images, descriptions), prediction in zip(writer.dataset, response["images"], strict=True):
            result = prediction_result(images[0], paths[0], prediction, names, task, writer.args)
            writer.results = [result]
            writer.write_results(0, Path(paths[0]), np.moveaxis(images[0], -1, 0), descriptions)
    finally:
        for video in writer.vid_writer.values():
            video.release()
        if getattr(writer.dataset, "cap", None) is not None:
            writer.dataset.cap.release()
    if directory.exists():
        print(f"Results saved to {directory}")


def cloud_predict(client: Platform, tokens: list[str]) -> int:
    """ul cloud predict model=ul://owner/project/model source=image.jpg [conf=0.25 iou=0.7 imgsz=640]

    source= is one local image or video; conf/iou/imgsz run on Platform, classes/max_det apply locally.
    Saves annotated output, with optional save_txt/save_crop/save_frames.
    project=, name=, save_dir=, and exist_ok= control local outputs as in YOLO.
    """
    args = yolo_args(tokens)
    source = Path(str(args.pop("source", ""))).expanduser()
    if not source.is_file():
        raise ValueError("source= must be a local image or video file")
    model, project = args.pop("model", "yolo26n.pt"), args.pop("project", None)
    local_args = args | {"model": model, "project": project}
    uri = platform_model(model) or upload_model(client, model, *resolve_project(client, project))
    owner, project, model = uri[5:].split("/")
    options = {key: args[key] for key in ("conf", "iou", "imgsz") if key in args}  # YOLO options the endpoint accepts
    with source.open("rb") as file:
        response = client.models.predict(owner, project, model, body={"file": file, **options, "normalize": False})
    output(response)
    save_predictions(source, response, local_args)
    return 0


def cloud_export(client: Platform, tokens: list[str]) -> int:
    """ul cloud export model=ul://owner/project/model format=onnx [imgsz=640 quantize=16 gpu_type=rtx-4090]

    Waits for the export and downloads its artifact to save_dir= or project=, otherwise beside local weights or in cwd.
    Replaces an existing artifact only after a successful download; name= retains its export-target meaning.
    """
    args = yolo_args(tokens)
    local_args = args.copy()
    model, project = args.pop("model", "yolo26n.pt"), args.pop("project", None)
    uri = platform_model(model) or upload_model(client, model, *resolve_project(client, project))
    if uri.startswith("ul://ultralytics/"):  # exports require your own copy of official weights
        owner, slug = resolve_project(client, project)
        clone = client.models.clone(*uri[5:].split("/"), owner_body=owner, project_body=slug)
        uri = f"ul://{clone['owner']}/{clone['project']}/{clone['model']}"
        print(f"Model: {uri}")
    owner, project, model = uri[5:].split("/")
    gpu_type, fmt = args.pop("gpu_type", NOT_GIVEN), args.pop("format", "torchscript")
    ignored = args.keys() & {"save", "plots", "workers", "cache"}
    if ignored:
        print(f"Warning: cloud export ignores local options: {', '.join(sorted(ignored))}.", file=sys.stderr)
    for key in ("save_dir", "device", "exist_ok", "mode", "task", *ignored):
        args.pop(key, None)
    job = client.exports.create(owner, project, model, format=fmt, gpu_type=gpu_type, args=args)
    print(f"Export: {job['id']} ({job['status']})")
    job = wait_job(lambda: client.exports.retrieve(owner, project, model, job["id"])["export"])
    output(job)
    file = job.get("file") or {}
    if not file.get("downloadUrl") or not file.get("downloadFilename"):
        raise ValueError("Export completed without a download URL or filename")
    directory = Path(
        local_args.get("save_dir")
        or local_args.get("project")
        or (Path(str(local_args.get("model"))).parent if not platform_model(local_args.get("model")) else ".")
    )
    download_file(file["downloadUrl"], directory.expanduser() / Path(file["downloadFilename"]).name)
    return 0


CLOUD_COMMANDS = {"train": cloud_train, "predict": cloud_predict, "export": cloud_export}


def dispatch(tokens: list[str]) -> int:
    """Execute one SDK operation, inferring only a missing resource-path owner."""
    tokens = list(tokens)
    with ExitStack() as stack:
        client = stack.enter_context(Platform(base_url=platform_url()))
        if tokens and tokens[0] in CLOUD_COMMANDS:
            if len(tokens) == 1 or any(token in {"help", "--help", "-h"} for token in tokens):
                print(inspect.getdoc(CLOUD_COMMANDS[tokens[0]]))
                return 0
            try:
                return CLOUD_COMMANDS[tokens[0]](client, tokens[1:])
            except (AssertionError, SyntaxError, TypeError) as error:  # ultralytics reports invalid inputs this way
                raise ValueError(error) from error
        resources = {
            name.replace("_", "-"): {
                method.replace("_", "-"): member
                for method, member in inspect.getmembers(resource, inspect.ismethod)
                if not method.startswith("_")
            }
            for name, resource in vars(client).items()
            if not name.startswith("_")
        }
        resource = tokens.pop(0) if tokens and tokens[0] not in {"help", "--help", "-h"} else None
        if resource is not None and resource not in resources:
            raise ValueError("Unknown command; use --help to list API operations")
        methods = resources[resource] if resource is not None else {}
        implicit = defaults(methods)
        method = tokens.pop(0) if tokens and tokens[0] in methods else None
        raw = assignments(tokens)
        help_requested = any(key in {"help", "--help", "-h"} and value is None for key, value in raw.items())
        if resource is not None and method is None and not help_requested:
            method = next((name for name, keys in implicit.items() if keys and any(key in raw for key in keys)), None)
            method = method or ("list" if "list" in implicit else None)
        if method is None and tokens and not help_requested:
            raise ValueError("Choose a resource operation before supplying arguments")
        if method is None or help_requested:
            print("ul cloud train|predict|export key=value ... — YOLO workflows on Platform")
            print("<resource> [operation] key=value ... (path owner defaults to the logged-in username)")
            listing = {resource: {method: methods[method]} if method else methods} if resource else resources
            for resource_name, members in listing.items():
                for method_name, member in members.items():
                    doc = inspect.getdoc(member) or ""
                    print(f"  {resource_name} {method_name}: {doc.partition(chr(10))[0].rstrip('.')}")
                    if method is not None:
                        for line in doc.splitlines()[1:]:
                            if not line.startswith(("    timeout (", "    extra_headers (")):
                                print(line)
            return 0
        arguments = describe(methods[method])
        values = parse(raw, arguments)
        key = f"{resource.replace('-', '_')}.{method.replace('-', '_')}"
        open_inputs(values, arguments, MULTIPART_FILES.get(key, []), stack)
        if "owner" not in values and arguments.get("owner", {}).get("path"):
            username = client.account.summary().get("username")
            if not isinstance(username, str) or not username:
                raise ValueError("Could not infer owner; supply owner= explicitly")
            values["owner"] = username
        output(methods[method](**values))
    return 0


def main(argv: list[str] | None = None) -> int:
    """Run the unified CLI and translate SDK errors into process exit codes."""
    args = list(sys.argv[1:] if argv is None else argv)
    try:
        if not args or args in (["help"], ["--help"], ["-h"]):
            print(
                "ul login API_KEY | logout | version\n"
                "ul train|val|predict|export|track|benchmark key=value ...\n"
                "ul settings|checks|cfg|copy-cfg|solutions ...\n"
                "ul cloud train|predict|export key=value ...\n"
                "ul cloud <resource> [operation] key=value ...\n"
                "Login/logout and local commands require ultralytics. Use ul cloud --help to list API commands.\n"
                "Omitted path owners default to the logged-in username. No --key value options."
            )
            return 0
        if args in (["version"], ["--version"]):
            print(f"ultralytics-platform {version('ultralytics-platform')}")
            try:
                print(f"ultralytics {version('ultralytics')}")
            except PackageNotFoundError:
                print("ultralytics not installed")
            return 0
        workflow = args[0] == "cloud" and len(args) > 1 and args[1] in CLOUD_COMMANDS
        if (args[0] != "cloud" or workflow) and importlib.util.find_spec("ultralytics") is None:
            raise ValueError(
                "This command requires ultralytics. Install it in this environment: pip install ultralytics"
            )
        if args[0] == "cloud":
            return dispatch(args[1:])
        original = sys.argv[:]
        try:
            # YOLO aliases sys.argv as ARGV and recognizes its executable name in prediction paths.
            sys.argv[:] = ["yolo", *args]
            from ultralytics.cfg import entrypoint

            entrypoint()
        finally:
            sys.argv[:] = original
        return 0
    except APIError as error:
        body = error.json
        detail = body.get("error") if isinstance(body, dict) else None
        print(
            f"API request failed (HTTP {error.status_code}){f': {detail}' if isinstance(detail, str) else '.'}",
            file=sys.stderr,
        )
        return 1
    except APIConnectionError:
        print("Could not connect to API.", file=sys.stderr)
        return 1
    except (ValueError, OSError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        print("Interrupted.", file=sys.stderr)
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
