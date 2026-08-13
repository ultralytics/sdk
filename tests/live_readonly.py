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
from ultralytics_platform import APIConnectionError, APIError, Platform

ROOT = Path(__file__).parents[1]
BASE_URL = "https://platform.ultralytics.com"
DATASET_URL = "https://github.com/ultralytics/assets/releases/download/v0.0.0/coco32.zip"
HTTP_METHODS = {"delete", "get", "patch", "post", "put"}
DATASET_IMAGE_COUNT = 32
EXPECTED_FORBIDDEN = {
    "post_api_datasets_owner_dataset_clone": "You cannot clone a dataset to the same workspace.",
    "post_api_models_owner_project_model_clone": "You cannot clone a model to the same workspace.",
    "post_api_projects_owner_project_clone": "You cannot clone a project to the same workspace.",
}


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


def response_validator(
    document: dict[str, Any], statuses: dict[str, set[int]], validation_errors: list[RuntimeError]
) -> Callable[[httpx.Response], None]:
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
            statuses.setdefault(operation_id, set()).add(response.status_code)
            print(f"{operation_id}: {response.status_code}")
            responses = operation.get("responses", {})
            response_spec = responses.get(str(response.status_code)) or responses.get("default")
            if response.status_code == 403:
                expected_error = EXPECTED_FORBIDDEN.get(operation_id)
                try:
                    actual_error = response.json().get("error")
                except (ValueError, AttributeError):
                    actual_error = None
                if actual_error != expected_error:
                    raise RuntimeError(f"{operation_id} returned unexpected 403")
            if response.status_code == 401 or response.status_code >= 500 or not response_spec:
                raise RuntimeError(f"{operation_id} returned unexpected {response.status_code}")
            response_spec = resolve(document, response_spec)
            media = response_spec.get("content", {}).get("application/json")
            if response.is_success and media and media.get("schema"):
                try:
                    Draft202012Validator(absolute_references(media["schema"]), registry=registry).validate(
                        response.json()
                    )
                except ValidationError as error:
                    validation_errors.append(
                        RuntimeError(f"{operation_id}: {error.json_path} failed {error.validator}")
                    )
            return
        raise RuntimeError(f"SDK requested undocumented operation: {request.method} {request.url.path}")

    return validate


def expected_error(call: Callable[[], Any], operation_id: str, reason: str, expected_errors: dict[str, str]) -> Any:
    """Classify an operation that cannot safely succeed in the production canary."""
    try:
        return call()
    except APIError as error:
        if error.status_code in {401, 429} or error.status_code >= 500:
            raise
        if error.status_code == 403 and operation_id not in EXPECTED_FORBIDDEN:
            raise
        expected_errors[operation_id] = reason
        return {}


def cleanup_resource(
    retrieve: Callable[[], dict[str, Any]],
    delete: Callable[[], Any],
    key: str,
    known_id: Callable[[], str | None],
    permanently_delete: Callable[[str], Any] | None = None,
) -> None:
    """Delete a canary resource discovered by its unique public path."""
    errors: list[Exception] = []
    resource_id = known_id()
    try:
        result = retrieve()
    except APIError as error:
        if error.status_code != 404:
            errors.append(error)
    except APIConnectionError as error:
        errors.append(error)
    else:
        resource = result.get(key) if isinstance(result, dict) else None
        if isinstance(resource, dict):
            value = resource.get("id") or resource.get("_id")
            resource_id = str(value) if value else resource_id
    try:
        delete()
    except APIError as error:
        if error.status_code != 404:
            errors.append(error)
    except APIConnectionError as error:
        errors.append(error)
    if permanently_delete and resource_id:
        try:
            permanently_delete(resource_id)
        except APIError as error:
            if error.status_code != 404:
                errors.append(error)
        except APIConnectionError as error:
            errors.append(error)
    if errors:
        raise RuntimeError(errors)


def ignore_missing(call: Callable[[], Any]) -> None:
    """Allow cleanup to be idempotent while surfacing every other API failure."""
    try:
        call()
    except APIError as error:
        if error.status_code != 404:
            raise


def wait_for_images(client: Platform, owner: str, dataset: str) -> list[dict[str, Any]]:
    """Wait for the owned canary upload to finish ingesting."""
    for _ in range(12):
        result = client.datasets.retrieve(owner, dataset)
        if result["dataset"].get("imageCount") == DATASET_IMAGE_COUNT:
            images = client.datasets.list_images(owner, dataset, limit=DATASET_IMAGE_COUNT, include_labels="true").get(
                "images", []
            )
            if len(images) == DATASET_IMAGE_COUNT:
                return images
        time.sleep(5)
    raise RuntimeError(f"Canary dataset ingest did not produce all {DATASET_IMAGE_COUNT} images")


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


def exercise_api(client: Platform, cleanup: list[Callable[[], Any]], expected_errors: dict[str, str]) -> None:
    """Invoke every generated operation and require successful owned-resource CRUD."""
    account = client.account.retrieve_summary()
    owner = str(account["username"])
    suffix = str(time.time_ns())[-12:]
    slug = f"sdk-ci-{suffix}"
    missing = f"missing-{suffix}"
    created_ids: dict[str, str] = {}

    client.account.list_api_keys()
    client.account.retrieve_storage_usage(details="true")
    client.account.retrieve_public_user_profile(username=owner)
    expected_error(
        lambda: client.account.follow_user(username=owner, followed=True),
        "patch_api_users",
        "The canary cannot follow its own account and has no second test account",
        expected_errors,
    )
    client.billing.list_transactions()
    client.billing.list_usage_summary()
    client.explore.retrieve_search(limit=1)
    client.training.retrieve_gpu_availability()
    client.lifecycle.retrieve_trash(limit=1)

    project = slug
    cleanup.append(
        lambda: cleanup_resource(
            lambda: client.projects.retrieve(owner, project),
            lambda: client.projects.delete(owner, project),
            "project",
            lambda: created_ids.get("project"),
            lambda resource_id: client.lifecycle.permanently_delete_trash(body={"id": resource_id, "type": "project"}),
        )
    )
    project_result = client.projects.create(project=project, name="SDK CI project", visibility="private")
    if project_result.get("id"):
        created_ids["project"] = str(project_result["id"])
    client.projects.retrieve(owner, project)
    client.projects.update(owner, project, description="Full API lifecycle canary", tags=["sdk-ci"])
    if client.projects.retrieve(owner, project)["project"].get("description") != "Full API lifecycle canary":
        raise RuntimeError("Project update did not persist")
    client.projects.list(owner, limit=1)
    clone_project = f"{slug}-clone"
    cleanup.append(
        lambda: cleanup_resource(
            lambda: client.projects.retrieve(owner, clone_project),
            lambda: client.projects.delete(owner, clone_project),
            "project",
            lambda: created_ids.get("project-clone"),
            lambda resource_id: client.lifecycle.permanently_delete_trash(body={"id": resource_id, "type": "project"}),
        )
    )
    project_clone = expected_error(
        lambda: client.projects.clone(owner, project, project_body=f"{slug}-clone", name="SDK CI project clone"),
        "post_api_projects_owner_project_clone",
        "Cloning into the source workspace is prohibited and the canary has no second workspace",
        expected_errors,
    )
    if project_clone.get("id"):
        created_ids["project-clone"] = str(project_clone["id"])

    dataset = slug
    cleanup.append(
        lambda: cleanup_resource(
            lambda: client.datasets.retrieve(owner, dataset),
            lambda: client.datasets.delete(owner, dataset),
            "dataset",
            lambda: created_ids.get("dataset"),
            lambda resource_id: client.lifecycle.permanently_delete_trash(body={"id": resource_id, "type": "dataset"}),
        )
    )
    dataset_result = client.datasets.create(dataset=dataset, name="SDK CI dataset", task="detect", visibility="private")
    dataset_id = str(dataset_result["id"])
    created_ids["dataset"] = dataset_id
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
    expected_error(
        lambda: client.datasets.delete_classes(owner, dataset, class_ids=[9999]),
        "post_api_datasets_owner_dataset_classes_delete",
        "A nonexistent class ID safely validates the destructive endpoint",
        expected_errors,
    )
    expected_error(
        lambda: client.datasets.merge_classes(owner, dataset, source_class_ids=[9999], target_class_id=0),
        "post_api_datasets_owner_dataset_classes_merge",
        "A nonexistent source class safely validates the destructive endpoint",
        expected_errors,
    )
    client.datasets.redistribute_splits(owner, dataset, train=80, val=10, test=10)

    detail = client.images.retrieve(image_ids[0])
    metadata = detail.get("metadata", {})
    metadata_response = client.images.update(image_ids[0], body={"metadata": {**metadata, "location": "strasbourg"}})
    if metadata_response.get("metadata", {}).get("location") != "strasbourg":
        raise RuntimeError("Image metadata update was missing from the response")
    if client.images.retrieve(image_ids[0]).get("metadata", {}).get("location") != "strasbourg":
        raise RuntimeError("Image metadata update did not persist")
    client.images.update(image_ids[0], body={"metadata": metadata})

    labels = detail.get("labels", [])
    if not labels:
        raise RuntimeError("Canary dataset did not contain labels")
    keypoint_labels = [{**labels[0], "keypoints": [0.1, 0.2, 0.3, 0.4]}, *labels[1:]]
    keypoint_response = client.images.update(image_ids[0], body={"labels": keypoint_labels})
    if keypoint_response["labels"][0].get("keypoints") != [0.1, 0.2, 0.3, 0.4]:
        raise RuntimeError("Multiple image keypoints were missing from the response")
    saved_keypoints = client.images.retrieve(image_ids[0])["labels"][0].get("keypoints", [])
    if len(saved_keypoints) != 4 or any(
        abs(actual - expected) > 0.00005 for actual, expected in zip(saved_keypoints, [0.1, 0.2, 0.3, 0.4], strict=True)
    ):
        raise RuntimeError("Multiple image keypoints did not persist")
    client.images.update(image_ids[0], body={"labels": labels})
    client.images.update(image_ids[0], body={"labels": labels[:-1]})
    if len(client.images.retrieve(image_ids[0]).get("labels", [])) != len(labels) - 1:
        raise RuntimeError("Image label update did not persist")
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
    for _ in range(24):
        if client.datasets.retrieve_embeddings(owner, dataset).get("analyzedAt"):
            break
        time.sleep(5)
    else:
        raise RuntimeError("Canary dataset embedding analysis did not finish")
    client.datasets.retrieve_images_clustering(owner, dataset, limit=1)
    client.datasets.delete_embeddings(owner, dataset)

    clone_dataset = f"{slug}-clone"
    cleanup.append(
        lambda: cleanup_resource(
            lambda: client.datasets.retrieve(owner, clone_dataset),
            lambda: client.datasets.delete(owner, clone_dataset),
            "dataset",
            lambda: created_ids.get("dataset-clone"),
            lambda resource_id: client.lifecycle.permanently_delete_trash(body={"id": resource_id, "type": "dataset"}),
        )
    )
    dataset_clone = expected_error(
        lambda: client.datasets.clone(owner, dataset, dataset_body=f"{slug}-clone", name="SDK CI dataset clone"),
        "post_api_datasets_owner_dataset_clone",
        "Cloning into the source workspace is prohibited and the canary has no second workspace",
        expected_errors,
    )
    if dataset_clone.get("id"):
        created_ids["dataset-clone"] = str(dataset_clone["id"])

    model = slug
    cleanup.append(
        lambda: cleanup_resource(
            lambda: client.models.retrieve(owner, project, model),
            lambda: client.models.delete(owner, project, model),
            "model",
            lambda: created_ids.get("model"),
            lambda resource_id: client.lifecycle.permanently_delete_trash(body={"id": resource_id, "type": "model"}),
        )
    )
    model_result = client.models.create(
        body={"owner": owner, "project": project, "model": slug, "name": "SDK CI model", "task": "detect"}
    )
    model_id = str(model_result["id"])
    created_ids["model"] = model_id
    client.models.retrieve(owner, project, model)
    client.models.update(owner, project, model, description="Full API lifecycle canary", metadata={"source": "sdk-ci"})
    if client.models.retrieve(owner, project, model)["model"].get("description") != "Full API lifecycle canary":
        raise RuntimeError("Model update did not persist")
    client.models.list(owner, project, limit=1)
    client.models.retrieve_files(owner, project, model)
    client.models.retrieve_training(owner, project, model)
    expected_error(
        lambda: client.models.delete_training(owner, project, model),
        "delete_api_models_owner_project_model_training",
        "The canary model has no training session to delete",
        expected_errors,
    )
    client.exports.list_model(owner, project, model, limit=1)
    export = expected_error(
        lambda: client.exports.export_model(owner, project, missing, format="onnx"),
        "post_api_models_owner_project_model_exports",
        "The canary does not upload proprietary model weights",
        expected_errors,
    )
    export_id = str(export.get("id", missing))
    expected_error(
        lambda: client.exports.retrieve_status(owner, project, model, export_id),
        "get_api_models_owner_project_model_exports_exportId",
        "No export exists after the intentionally rejected export request",
        expected_errors,
    )
    expected_error(
        lambda: client.exports.cancel_or_delete(owner, project, model, export_id),
        "delete_api_models_owner_project_model_exports_exportId",
        "No export exists after the intentionally rejected export request",
        expected_errors,
    )
    expected_error(
        lambda: client.models.predict(owner, project, model, body={}),
        "post_api_models_owner_project_model_predict",
        "The canary model has no inference weights",
        expected_errors,
    )
    expected_error(
        lambda: client.images.predict(image_ids[0], model_id=model_id),
        "post_api_images_imageId_predict",
        "The canary model has no inference weights",
        expected_errors,
    )
    expected_error(
        lambda: client.training.start(model_id=missing, train_args={"epochs": 1}),
        "post_api_training_start",
        "A missing model avoids starting paid compute",
        expected_errors,
    )

    clone_model = f"{slug}-clone"
    cleanup.append(
        lambda: cleanup_resource(
            lambda: client.models.retrieve(owner, project, clone_model),
            lambda: client.models.delete(owner, project, clone_model),
            "model",
            lambda: created_ids.get("model-clone"),
            lambda resource_id: client.lifecycle.permanently_delete_trash(body={"id": resource_id, "type": "model"}),
        )
    )
    model_clone = expected_error(
        lambda: client.models.clone(owner, project, model, project_body=project, model_body=f"{slug}-clone"),
        "post_api_models_owner_project_model_clone",
        "Cloning into the source workspace is prohibited and the canary has no second workspace",
        expected_errors,
    )
    if model_clone.get("id"):
        created_ids["model-clone"] = str(model_clone["id"])

    client.deployments.list(owner, limit=1)
    cleanup.append(lambda: ignore_missing(lambda: client.deployments.delete(owner, slug)))
    deployment_result = expected_error(
        lambda: client.deployments.create(
            owner, project=missing, model=missing, deployment=slug, name="SDK CI deployment", region="us-central1"
        ),
        "post_api_deployments_owner",
        "A missing model avoids creating paid compute",
        expected_errors,
    )
    deployment = str(deployment_result.get("deployment", missing))
    deployment_reason = "No deployment exists after the intentionally rejected create request"
    expected_error(
        lambda: client.deployments.retrieve(owner, deployment),
        "get_api_deployments_owner_deployment",
        deployment_reason,
        expected_errors,
    )
    expected_error(
        lambda: client.deployments.update(owner, deployment, body={"action": "stop"}),
        "patch_api_deployments_owner_deployment",
        deployment_reason,
        expected_errors,
    )
    expected_error(
        lambda: client.deployments.retrieve_health(owner, deployment),
        "get_api_deployments_owner_deployment_health",
        deployment_reason,
        expected_errors,
    )
    expected_error(
        lambda: client.deployments.retrieve_logs(owner, deployment, limit=1),
        "get_api_deployments_owner_deployment_logs",
        deployment_reason,
        expected_errors,
    )
    expected_error(
        lambda: client.deployments.retrieve_metrics(owner, deployment),
        "get_api_deployments_owner_deployment_metrics",
        deployment_reason,
        expected_errors,
    )
    expected_error(
        lambda: client.deployments.predict(owner, deployment, body={}),
        "post_api_deployments_owner_deployment_predict",
        deployment_reason,
        expected_errors,
    )
    expected_error(
        lambda: client.deployments.delete(owner, deployment),
        "delete_api_deployments_owner_deployment",
        deployment_reason,
        expected_errors,
    )

    integrations = client.storage_integrations.list_cloud_storage_integrations()
    integration = (integrations.get("integrations") or [{}])[0]
    integration_id = str(integration.get("id") or integration.get("_id") or missing)
    targets = integration.get("targets") or ["missing"]
    expected_error(
        lambda: client.storage_integrations.browse_cloud_storage_objects(integration_id, target=str(targets[0])),
        "get_api_integrations_buckets_id_objects",
        "The canary has no configured cloud storage integration",
        expected_errors,
    )
    expected_error(
        lambda: client.storage_integrations.discover_cloud_storage_locations(provider="gcs", credentials={}),
        "post_api_integrations_buckets_discover",
        "Invalid empty credentials avoid connecting external storage",
        expected_errors,
    )
    expected_error(
        lambda: client.storage_integrations.connect_cloud_storage(provider="gcs", credentials={}, targets=["missing"]),
        "post_api_integrations_buckets",
        "Invalid empty credentials avoid connecting external storage",
        expected_errors,
    )
    expected_error(
        lambda: client.datasets.preview_roboflow_import(api_key="invalid"),
        "post_api_integrations_roboflow_preview",
        "Invalid credentials avoid importing external data",
        expected_errors,
    )
    expected_error(
        lambda: client.datasets.import_from_roboflow(api_key="invalid", items=[]),
        "post_api_integrations_roboflow_import",
        "Invalid credentials avoid importing external data",
        expected_errors,
    )

    client.datasets.delete(owner, dataset)
    client.lifecycle.restore_trashed_item(id=dataset_id, type="dataset")
    client.datasets.delete(owner, dataset)


def validate_sdk(document: dict[str, Any]) -> None:
    expected = operation_coverage(document)
    statuses: dict[str, set[int]] = {}
    expected_errors: dict[str, str] = {}
    validation_errors: list[RuntimeError] = []
    cleanup: list[Callable[[], Any]] = []
    http_client = httpx.Client(
        timeout=60, event_hooks={"response": [response_validator(document, statuses, validation_errors)]}
    )
    exercise_error: Exception | None = None
    cleanup_errors: list[Exception] = []
    with Platform(base_url=BASE_URL, http_client=http_client) as client:
        try:
            exercise_api(client, cleanup, expected_errors)
        except (APIConnectionError, APIError, httpx.HTTPError, RuntimeError) as error:
            exercise_error = error
        finally:
            for action in reversed(cleanup):
                try:
                    action()
                except (APIConnectionError, APIError, httpx.HTTPError, RuntimeError) as error:
                    cleanup_errors.append(error)
    if exercise_error:
        raise exercise_error
    if cleanup_errors:
        raise RuntimeError(f"Canary cleanup failed: {cleanup_errors}")
    if validation_errors:
        raise RuntimeError(f"Live response schema validation failed: {validation_errors}")
    observed = set(statuses)
    if observed != expected:
        raise RuntimeError(
            f"Live SDK operation drift: missing={sorted(expected - observed)}, extra={sorted(observed - expected)}"
        )
    error_only = {operation_id for operation_id, codes in statuses.items() if not any(code < 400 for code in codes)}
    if error_only != set(expected_errors):
        raise RuntimeError(
            f"Live SDK error classification drift: unclassified={sorted(error_only - set(expected_errors))}, "
            f"unexpectedly successful={sorted(set(expected_errors) - error_only)}"
        )
    for operation_id, reason in sorted(expected_errors.items()):
        print(f"{operation_id}: expected non-success ({reason})")
    print(f"Validated all {len(observed)} generated Python SDK operations against production")


def main() -> None:
    if not os.environ.get("ULTRALYTICS_API_KEY"):
        raise RuntimeError("ULTRALYTICS_API_KEY is required")
    validate_sdk(json.loads((ROOT / "openapi.json").read_text()))


if __name__ == "__main__":
    main()
