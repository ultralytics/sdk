# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from __future__ import annotations

import json
import os
import re
import time
from collections.abc import Callable
from pathlib import Path
from typing import Any

import httpx
from jsonschema import Draft202012Validator, ValidationError
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012
from ultralytics_platform import APIError, Platform

ROOT = Path(__file__).parents[1]
BASE_URL = "https://platform.ultralytics.com"
DATASET_URL = "https://github.com/ultralytics/assets/releases/download/v0.0.0/coco32.zip"
HTTP_METHODS = {"delete", "get", "patch", "post", "put"}


def resolve(document: dict[str, Any], value: dict[str, Any]) -> dict[str, Any]:
    reference = value.get("$ref")
    if not isinstance(reference, str) or not reference.startswith("#/"):
        return value
    result: Any = document
    for part in reference[2:].split("/"):
        result = result[part.replace("~1", "/").replace("~0", "~")]
    return result


def absolute_references(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            key: f"urn:openapi{item}"
            if key == "$ref" and isinstance(item, str) and item.startswith("#/")
            else absolute_references(item)
            for key, item in value.items()
        }
    if isinstance(value, list):
        return [absolute_references(item) for item in value]
    return value


def operation_coverage(document: dict[str, Any]) -> set[str]:
    """Return every unique contract operation required by the live SDK suite."""
    declarations = [
        operation["operationId"]
        for path_item in document["paths"].values()
        for method, operation in path_item.items()
        if method in HTTP_METHODS
    ]
    if len(declarations) != len(set(declarations)):
        raise RuntimeError("The OpenAPI contract contains duplicate operation IDs")
    return set(declarations)


def response_validator(document: dict[str, Any], observed: set[str]) -> Callable[[httpx.Response], None]:
    """Reject undocumented responses and validate every successful JSON body."""
    registry = Registry().with_resource(
        "urn:openapi", Resource.from_contents(document, default_specification=DRAFT202012)
    )

    def validate(response: httpx.Response) -> None:
        response.read()
        request = response.request
        for template, path_item in sorted(document["paths"].items(), key=lambda item: item[0].count("{")):
            if not re.fullmatch(re.sub(r"\{[^/]+\}", "[^/]+", template), request.url.path):
                continue
            operation = path_item.get(request.method.lower())
            if not operation:
                continue
            operation_id = operation["operationId"]
            observed.add(operation_id)
            print(f"{operation_id}: {response.status_code}")
            responses = operation.get("responses", {})
            response_spec = responses.get(str(response.status_code)) or responses.get("default")
            if response.status_code == 429 or response.status_code >= 500 or not response_spec:
                raise RuntimeError(f"{operation_id} returned unexpected {response.status_code}")
            response_spec = resolve(document, response_spec)
            media = response_spec.get("content", {}).get("application/json")
            if response.is_success and media and media.get("schema"):
                try:
                    Draft202012Validator(absolute_references(media["schema"]), registry=registry).validate(
                        response.json()
                    )
                except ValidationError as error:
                    raise RuntimeError(f"{operation_id}: {error.json_path} failed {error.validator}") from error
            return
        raise RuntimeError(f"SDK requested undocumented operation: {request.method} {request.url.path}")

    return validate


def documented(call: Callable[[], Any]) -> Any:
    """Return an SDK result or accept a documented non-success response."""
    try:
        return call()
    except APIError:
        return {}


def wait_for_images(client: Platform, owner: str, dataset: str) -> list[dict[str, Any]]:
    """Wait for the owned canary upload to finish ingesting."""
    for _ in range(12):
        images = client.datasets.list_images(owner, dataset, limit=10, include_labels="true").get("images", [])
        if images:
            return images
        time.sleep(5)
    raise RuntimeError("Canary dataset ingest produced no images")


def download_dataset() -> bytes:
    """Download the shared canary fixture with bounded retries for transient asset failures."""
    for attempt in range(6):
        try:
            response = httpx.get(DATASET_URL, follow_redirects=True, timeout=60)
            response.raise_for_status()
            return response.content
        except httpx.HTTPError:
            if attempt == 5:
                raise
            time.sleep(5)
    raise RuntimeError("Canary dataset download failed")


def exercise_api(client: Platform, cleanup: list[Callable[[], Any]]) -> None:
    """Invoke every generated operation and require successful owned-resource CRUD."""
    account = client.account.retrieve_summary()
    owner = str(account["username"])
    suffix = str(time.time_ns())[-12:]
    slug = f"sdk-ci-{suffix}"
    missing = f"missing-{suffix}"

    client.account.list_api_keys()
    client.account.retrieve_storage_usage(details="true")
    client.account.retrieve_public_user_profile(username=owner)
    documented(lambda: client.account.follow_user(username=owner, followed=True))
    client.billing.list_transactions()
    client.billing.list_usage_summary()
    client.explore.retrieve_search(limit=1)
    client.training.retrieve_gpu_availability()
    client.lifecycle.retrieve_trash(limit=1)

    project_result = client.projects.create(project=slug, name="SDK CI project", visibility="private")
    project_id, project = str(project_result["id"]), str(project_result["project"])
    cleanup.append(lambda: client.lifecycle.permanently_delete_trash(body={"id": project_id, "type": "project"}))
    cleanup.append(lambda: client.projects.delete(owner, project))
    client.projects.retrieve(owner, project)
    client.projects.update(owner, project, description="Full API lifecycle canary", tags=["sdk-ci"])
    if client.projects.retrieve(owner, project)["project"].get("description") != "Full API lifecycle canary":
        raise RuntimeError("Project update did not persist")
    client.projects.list(owner, limit=1)
    project_clone = documented(
        lambda: client.projects.clone(owner, project, project_body=f"{slug}-clone", name="SDK CI project clone")
    )
    if project_clone:
        clone_project_id, clone_project = str(project_clone["id"]), str(project_clone["project"])
        cleanup.append(
            lambda: client.lifecycle.permanently_delete_trash(body={"id": clone_project_id, "type": "project"})
        )
        cleanup.append(lambda: client.projects.delete(owner, clone_project))

    dataset_result = client.datasets.create(dataset=slug, name="SDK CI dataset", task="detect", visibility="private")
    dataset_id, dataset = str(dataset_result["id"]), str(dataset_result["dataset"])
    cleanup.append(lambda: client.lifecycle.permanently_delete_trash(body={"id": dataset_id, "type": "dataset"}))
    cleanup.append(lambda: client.datasets.delete(owner, dataset))
    archive = download_dataset()
    upload = client.upload.retrieve_file_url(
        asset_id=dataset_id,
        asset_type="datasets",
        filename="coco32.zip",
        content_type="application/zip",
        total_bytes=len(archive),
    )
    response = httpx.put(upload["uploadUrl"], content=archive, headers={"Content-Type": "application/zip"}, timeout=60)
    response.raise_for_status()
    client.upload.complete(session_id=upload["sessionId"])
    client.datasets.ingest(owner, dataset, session_id=upload["sessionId"])
    images = wait_for_images(client, owner, dataset)
    image_ids = [str(image.get("id") or image.get("_id")) for image in images]
    if len(image_ids) < 3:
        raise RuntimeError("Canary dataset needs at least three images for mutation isolation")

    client.datasets.retrieve(owner, dataset)
    client.datasets.update(owner, dataset, description="Full API lifecycle canary", tags=["sdk-ci"])
    if client.datasets.retrieve(owner, dataset)["dataset"].get("description") != "Full API lifecycle canary":
        raise RuntimeError("Dataset update did not persist")
    client.datasets.list(owner, limit=1)
    client.datasets.retrieve_class_stats(owner, dataset)
    client.datasets.list_images(owner, dataset, limit=1)
    client.datasets.retrieve_selected_images(owner, dataset, image_ids=image_ids[:1])
    client.datasets.list_models(owner, dataset)
    documented(lambda: client.datasets.retrieve_images_clustering(owner, dataset, limit=1))
    documented(lambda: client.datasets.delete_classes(owner, dataset, class_ids=[9999]))
    documented(lambda: client.datasets.merge_classes(owner, dataset, source_class_ids=[9999], target_class_id=0))
    client.datasets.redistribute_splits(owner, dataset, train=80, val=10, test=10)

    detail = client.images.retrieve(image_ids[0])
    labels = detail.get("labels", [])
    if labels:
        client.images.update(image_ids[0], body={"labels": labels[:-1]})
        if len(client.images.retrieve(image_ids[0]).get("labels", [])) != len(labels) - 1:
            raise RuntimeError("Image label update did not persist")
        client.images.update(image_ids[0], body={"labels": labels})
    else:
        client.images.update(image_ids[0], body={"labels": labels})
    client.images.update_bulk(image_ids=[image_ids[1]], split="val")
    client.images.retrieve_signed_urls(image_ids=image_ids[:1])
    client.images.delete_bulk(image_ids=[image_ids[1]])
    client.images.delete(image_ids[2])

    version_result = client.datasets.create_export(owner, dataset, description="SDK CI version")
    version = int(version_result["version"])
    client.datasets.retrieve_export(owner, dataset, v=version)
    client.datasets.update_export(owner, dataset, version=version, description="SDK CI version updated")
    client.datasets.restore(owner, dataset, version=version)
    client.datasets.create_embeddings(owner, dataset)
    client.datasets.retrieve_embeddings(owner, dataset)
    documented(lambda: client.datasets.delete_embeddings(owner, dataset))

    dataset_clone = documented(
        lambda: client.datasets.clone(owner, dataset, dataset_body=f"{slug}-clone", name="SDK CI dataset clone")
    )
    if dataset_clone:
        clone_dataset_id, clone_dataset = str(dataset_clone["id"]), str(dataset_clone["dataset"])
        cleanup.append(
            lambda: client.lifecycle.permanently_delete_trash(body={"id": clone_dataset_id, "type": "dataset"})
        )
        cleanup.append(lambda: client.datasets.delete(owner, clone_dataset))

    model_result = client.models.create(
        body={"owner": owner, "project": project, "model": slug, "name": "SDK CI model", "task": "detect"}
    )
    model_id, model = str(model_result["id"]), str(model_result["model"])
    cleanup.append(lambda: client.lifecycle.permanently_delete_trash(body={"id": model_id, "type": "model"}))
    cleanup.append(lambda: client.models.delete(owner, project, model))
    client.models.retrieve(owner, project, model)
    client.models.update(owner, project, model, description="Full API lifecycle canary", metadata={"source": "sdk-ci"})
    if client.models.retrieve(owner, project, model)["model"].get("description") != "Full API lifecycle canary":
        raise RuntimeError("Model update did not persist")
    client.models.list(owner, project, limit=1)
    client.models.retrieve_files(owner, project, model)
    client.models.retrieve_training(owner, project, model)
    documented(lambda: client.models.delete_training(owner, project, model))
    client.exports.list_model(owner, project, model, limit=1)
    export = documented(lambda: client.exports.export_model(owner, project, model, format="onnx"))
    export_id = str(export.get("id", missing))
    documented(lambda: client.exports.retrieve_status(owner, project, model, export_id))
    documented(lambda: client.exports.cancel_or_delete(owner, project, model, export_id))
    documented(lambda: client.models.predict(owner, project, model, body={}))
    documented(lambda: client.images.predict(image_ids[0], model_id=model_id))
    documented(lambda: client.training.start(model_id=missing, train_args={"epochs": 1}))

    model_clone = documented(
        lambda: client.models.clone(owner, project, model, project_body=project, model_body=f"{slug}-clone")
    )
    if model_clone:
        clone_model_id, clone_model = str(model_clone["id"]), str(model_clone["model"])
        cleanup.append(lambda: client.lifecycle.permanently_delete_trash(body={"id": clone_model_id, "type": "model"}))
        cleanup.append(lambda: client.models.delete(owner, project, clone_model))

    client.deployments.list(owner, limit=1)
    deployment_result = documented(
        lambda: client.deployments.create(
            owner, project=project, model=model, deployment=slug, name="SDK CI deployment", region="us-central1"
        )
    )
    deployment = str(deployment_result.get("deployment", missing))
    if deployment_result:
        cleanup.append(lambda: client.deployments.delete(owner, deployment))
    documented(lambda: client.deployments.retrieve(owner, deployment))
    documented(lambda: client.deployments.update(owner, deployment, body={"action": "stop"}))
    documented(lambda: client.deployments.retrieve_health(owner, deployment))
    documented(lambda: client.deployments.retrieve_logs(owner, deployment, limit=1))
    documented(lambda: client.deployments.retrieve_metrics(owner, deployment))
    documented(lambda: client.deployments.predict(owner, deployment, body={}))
    documented(lambda: client.deployments.delete(owner, deployment))

    integrations = client.storage_integrations.list_cloud_storage_integrations()
    integration = (integrations.get("integrations") or [{}])[0]
    integration_id = str(integration.get("id") or integration.get("_id") or missing)
    targets = integration.get("targets") or ["missing"]
    documented(lambda: client.storage_integrations.browse_cloud_storage_objects(integration_id, target=str(targets[0])))
    documented(lambda: client.storage_integrations.discover_cloud_storage_locations(provider="gcs", credentials={}))
    documented(
        lambda: client.storage_integrations.connect_cloud_storage(provider="gcs", credentials={}, targets=["missing"])
    )
    documented(lambda: client.datasets.preview_roboflow_import(api_key="invalid"))
    documented(lambda: client.datasets.import_from_roboflow(api_key="invalid", items=[]))
    documented(lambda: client.upload.complete(session_id=missing))

    client.datasets.delete(owner, dataset)
    client.lifecycle.restore_trashed_item(id=dataset_id, type="dataset")


def validate_sdk(document: dict[str, Any]) -> None:
    expected = operation_coverage(document)
    observed: set[str] = set()
    cleanup: list[Callable[[], Any]] = []
    http_client = httpx.Client(timeout=60, event_hooks={"response": [response_validator(document, observed)]})
    with Platform(base_url=BASE_URL, http_client=http_client) as client:
        try:
            exercise_api(client, cleanup)
        finally:
            for action in reversed(cleanup):
                try:
                    documented(action)
                except (RuntimeError, httpx.HTTPError) as error:
                    print(f"Cleanup warning: {error}")
    if observed != expected:
        raise RuntimeError(
            f"Live SDK operation drift: missing={sorted(expected - observed)}, extra={sorted(observed - expected)}"
        )
    print(f"Validated all {len(observed)} generated Python SDK operations against production")


def main() -> None:
    if not os.environ.get("ULTRALYTICS_API_KEY"):
        raise RuntimeError("ULTRALYTICS_API_KEY is required")
    validate_sdk(json.loads((ROOT / "openapi.json").read_text()))


if __name__ == "__main__":
    main()
