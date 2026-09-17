<a href="https://www.ultralytics.com"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320" alt="Ultralytics logo"></a>

# 🔌 Ultralytics Platform API Python SDK

[![Ultralytics Discord](https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue)](https://discord.com/invite/ultralytics) [![Ultralytics Forums](https://img.shields.io/discourse/users?server=https%3A%2F%2Fcommunity.ultralytics.com&logo=discourse&label=Forums&color=blue)](https://community.ultralytics.com) [![Ultralytics Reddit](https://img.shields.io/reddit/subreddit-subscribers/ultralytics?style=flat&logo=reddit&logoColor=white&label=Reddit&color=blue)](https://www.reddit.com/r/Ultralytics/)

Typed synchronous and asynchronous Python clients generated from the [Ultralytics Platform API](https://platform.ultralytics.com) contract with [Ultralytics OpenAPI](https://github.com/ultralytics/openapi). The [interactive API reference](https://platform.ultralytics.com/api/docs) documents every resource and includes Python examples.

## 🐍 Python

[![PyPI - Version](https://img.shields.io/pypi/v/ultralytics-platform?logo=pypi&logoColor=white)](https://pypi.org/project/ultralytics-platform/) [![Ultralytics Downloads](https://static.pepy.tech/badge/ultralytics-platform)](https://clickpy.clickhouse.com/dashboard/ultralytics-platform) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ultralytics-platform?logo=python&logoColor=gold)](https://pypi.org/project/ultralytics-platform/)

Install the standalone [`ultralytics-platform`](https://pypi.org/project/ultralytics-platform/) package from PyPI in a [**Python >=3.11**](https://www.python.org/) environment. It has one lightweight runtime dependency (`httpx`) and does not install the larger `ultralytics` package:

```bash
uv pip install ultralytics-platform
```

Pass your [API key](https://platform.ultralytics.com/settings?tab=api-keys) directly as shown below. Alternatively, omit `api_key` to use `ULTRALYTICS_API_KEY` or the Platform key saved by `yolo login`. Both clients use explicit credentials first, then the environment, then saved settings. Pass `api_key=""` to disable authentication. `yolo logout` removes the saved key; it does not unset an environment variable. The SDK reads the existing Ultralytics settings directory, including `YOLO_CONFIG_DIR` and Linux `XDG_CONFIG_HOME`, without importing or installing `ultralytics`.

```python
from ultralytics_platform import Platform

with Platform(api_key="YOUR_API_KEY") as client:
    response = client.datasets.list("your_username")
```

The asynchronous client exposes the same resource tree:

```python
import asyncio

from ultralytics_platform import AsyncPlatform


async def main():
    async with AsyncPlatform(api_key="YOUR_API_KEY") as client:
        response = await client.datasets.list("your_username")


asyncio.run(main())
```

The package includes typed responses, multipart uploads, retries for temporary failures, structured API errors, custom HTTP clients, and context-manager cleanup.

## Unified `ul` CLI

This package installs `ul`. API resource commands work without the ML package. Local commands and `ul cloud train/predict/export` require `ultralytics` in the same environment. Existing `yolo` behavior, including local training with `ul://` inputs, is unchanged.

```bash
ul login API_KEY                # validate and save a Platform API key
ul logout                       # clear the saved key
ul train model=yolo26n.pt data=coco8.yaml epochs=100
ul cloud train model=yolo26n.pt data=ul://you/datasets/animals epochs=100
ul cloud train model=./best.pt data=./dataset/data.yaml epochs=100
ul cloud predict model=ul://you/project/model source=image.jpg conf=0.25
ul cloud export model=./best.pt format=onnx imgsz=640
ul cloud --help
ul cloud datasets images --help
ul cloud datasets               # list your datasets
ul cloud datasets dataset=coco8 # retrieve one dataset
ul cloud datasets images dataset=coco8 limit=20
ul cloud models project=p model=m
ul cloud training start model_id=MODEL_ID gpu_type=rtx-4090 train_args=@train.json
ul cloud models predict project=p model=m body='{"file":"@image.jpg","conf":0.25}'
ul cloud exports create project=p model=m format=onnx
```

`ul cloud train`, `ul cloud predict`, and `ul cloud export` accept YOLO `key=value` arguments and `cfg=path.yaml`; command-line values override the config. `gpu_type=` selects cloud compute for training and export. `model=` accepts official YOLO weights (yolo26, yolo11, yolov8, and yolov5 resolve to their public `ul://ultralytics/...` models; other official names are passed to training unchanged), a local `.pt` checkpoint uploaded as its own model, or a `ul://owner/project/model` URI. The commands use the installed `ultralytics` package for local file preparation and output saving; inference and training execute on Platform.

- **Train:** uploads local dataset YAMLs/folders or ZIP/TAR archives (other `data=` values such as the built-in `coco8.yaml` are passed to Platform unchanged), waits for ingestion and training, then downloads `weights/best.pt` and writes `args.yaml`, `results.csv` (when present in the checkpoint), and `results.json`. Platform currently exposes the promoted checkpoint, not a separate `last.pt` or the worker's complete output directory. Local datasets must have split directories under one root. Classification class folders are supported; Platform infers the dataset task from the labels during ingest. Uploaded datasets print a reusable URI. A new output model is created per invocation.
- **Predict:** submits one local image or video, then uses YOLO's writers for annotated images/videos, `save_txt`, `save_conf`, `save_crop`, `save_frames`, and display options. `save=False` disables annotated output. Saved runs also include the API response as `results.json`. `conf`, `iou`, and `imgsz` run on Platform; `classes` and `max_det` are applied locally to the returned detections; other inference execution settings are accepted but ignored because Platform controls remote execution. This lets you reuse local YOLO arguments when switching to cloud prediction. Responses contain rounded detections, polygon masks, top-five classification scores, and quantized depth, so cloud artifacts need not be byte-identical to local inference.
- **Export:** clones official weights into your project first (exports require an owned model), waits for completion and downloads the same artifact exposed in Portal. `save_dir=` selects the download directory; otherwise `project=` does, then the local checkpoint's directory or the current directory for hosted weights. Archives remain archives. Existing files are replaced only after a successful download. `name=` keeps YOLO's hardware-target meaning (for example, RKNN); it is not a download filename.

Train and predict reuse YOLO's `save_dir`, `project`, `name`, and `exist_ok` output-directory rules. For uploaded models and training runs, `project=` also selects or creates a private Platform project using the local directory's final component as its slug; the default is `cloud-training`. Explicit existing projects retain their visibility. The training worker assigns its own GPU, so `device=` is not sent. Boolean cache settings map to the API’s `ram`/`false` values. `name=` also names the output model on Platform, suffixed `-2`, `-3` on conflict the way YOLO increments local run directories; `save_dir=`, `exist_ok=`, and `device=` stay local. This also permits local paths that are longer or contain characters the API does not accept. Export consumes local output/device options before sending format arguments. It ignores `save`, `plots`, `workers`, and `cache` with one warning; artifact settings such as `quantize`, `imgsz`, and `dynamic` remain validated by Platform. Local commands (`ul train`, `ul predict`, `ul export`) remain unchanged.

These workflow commands return success only after completion and local output handling. Ctrl-C stops waiting (exit 130) but does not cancel the remote job. Failed or interrupted operations retain created resources; use the generated resource commands to inspect or cancel them before retrying. Training/export failures exit nonzero. Saved outputs from a previous run remain until a new artifact has downloaded successfully.

For API resource commands, arguments use `key=value` with values attached to `=`, command names use hyphens (`storage-integrations`), and argument names match Python keywords (`train_args`, `from_`). A separate `help`, `--help`, or `-h` token shows help without making a request; literal help values use `name=--help`. Bare booleans mean true. Omitted values, `False`, `0`, nullable `None`/`null`, and strings such as `license=None` remain distinct. Objects, arrays, and whole union bodies use JSON; `@request.json` reads JSON from a file and `@-` from stdin (one argument only). Binary fields require `@path`, including inside multipart body JSON.

A missing path `owner` defaults to the logged-in username through one account lookup, including for project operations; explicit owners win. For API resource commands, project identifiers (`project`) and destination owners are never inferred. Collection commands default to GET `list`, or matching GET `retrieve` when an item identifier is supplied; missing retrieval arguments fail instead of listing. Other resources show help. Writes require an explicit operation. Each API resource command invokes one SDK operation, plus any owner lookup, and prints the complete JSON, text, or binary response. Pagination is explicit; the SDK owns serialization, credentials, transport, and retries. Types and required arguments come from SDK signatures; the API validates nested JSON.

Cloud jobs may incur charges. API resource commands submit, inspect, or cancel one operation and exit, without polling or downloading artifacts. Success means the API call succeeded, not that a job finished. Exit codes: 0 success, 1 API/network errors (including nested validation), 2 local input errors, 130 interruption. Interrupting the CLI does not cancel a submitted job; use its cancellation operation.

Credentials prefer `ULTRALYTICS_API_KEY`, then shared YOLO settings. Login validates before saving; logout leaves environment variables unchanged. `ULTRALYTICS_PLATFORM_URL` selects another API origin. On systems with an existing Unix `ul` command, activate your Python environment or use `python -m ultralytics_platform.cli`.

## 🧩 One Contract, Typed Python

The [Ultralytics Platform API](https://platform.ultralytics.com) contract is the single source of truth for the generated client:

```text
OpenAPI contract
    └── Python SDK # ultralytics-platform
```

The [source repository](https://github.com/ultralytics/sdk) pins the consumed contract and generated output so API changes remain deterministic and reviewable. Generated SDK files should never be edited manually; update the contract, consumer configuration, [package README source](https://github.com/ultralytics/sdk/blob/main/README.python.md), or [generator](https://github.com/ultralytics/openapi) and regenerate.

## 🛠️ Validation

[CI](https://github.com/ultralytics/sdk/actions) regenerates the Python SDK to detect contract mismatch or generated drift. It also formats and lints Python, compiles the package, builds its wheel, installs it through the package boundary, and exercises representative synchronous and asynchronous requests.

## 💡 Contribute

[Ultralytics](https://www.ultralytics.com) thrives on community collaboration, and we deeply value your contributions! Please see our [Contributing Guide](https://docs.ultralytics.com/help/contributing) for details on how you can get involved. We also encourage you to share your feedback through our [Survey](https://www.ultralytics.com/survey?utm_source=github&utm_medium=social&utm_campaign=Survey). A huge thank you 🙏 to all our contributors!

API shape changes belong in the service OpenAPI contract; generated files should not be edited directly.

[![Ultralytics open-source contributors](https://raw.githubusercontent.com/ultralytics/assets/main/im/image-contributors.png)](https://github.com/ultralytics/sdk/graphs/contributors)

## 📄 License

- **AGPL-3.0 License**: The generated SDK is licensed under the [AGPL-3.0 License](https://spdx.org/licenses/AGPL-3.0-only.html).
- **Enterprise License**: Commercial licensing is available separately through [Ultralytics Licensing](https://www.ultralytics.com/license).

## 📫 Contact

For bug reports or feature suggestions related to this SDK, please submit an issue via [GitHub Issues](https://github.com/ultralytics/sdk/issues). Join our [Discord](https://discord.com/invite/ultralytics), [Reddit](https://www.reddit.com/r/Ultralytics/), or [Community Forums](https://community.ultralytics.com) for discussions and support!

<br>
<div align="center">
  <a href="https://github.com/ultralytics"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/social/logo-social-github.png" width="3%" alt="Ultralytics GitHub"></a>
  <img src="https://raw.githubusercontent.com/ultralytics/assets/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.linkedin.com/company/ultralytics/"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/social/logo-social-linkedin.png" width="3%" alt="Ultralytics LinkedIn"></a>
  <img src="https://raw.githubusercontent.com/ultralytics/assets/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://twitter.com/ultralytics"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/social/logo-social-twitter.png" width="3%" alt="Ultralytics Twitter"></a>
  <img src="https://raw.githubusercontent.com/ultralytics/assets/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.youtube.com/ultralytics"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/social/logo-social-youtube.png" width="3%" alt="Ultralytics YouTube"></a>
  <img src="https://raw.githubusercontent.com/ultralytics/assets/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.tiktok.com/@ultralytics"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/social/logo-social-tiktok.png" width="3%" alt="Ultralytics TikTok"></a>
  <img src="https://raw.githubusercontent.com/ultralytics/assets/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://ultralytics.com/bilibili"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/social/logo-social-bilibili.png" width="3%" alt="Ultralytics BiliBili"></a>
  <img src="https://raw.githubusercontent.com/ultralytics/assets/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://discord.com/invite/ultralytics"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/social/logo-social-discord.png" width="3%" alt="Ultralytics Discord"></a>
</div>
