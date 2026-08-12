# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from __future__ import annotations

import json
import os
import re
from collections import Counter
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
HTTP_METHODS = {"delete", "get", "patch", "post", "put"}


def first(data: Any, key: str) -> dict[str, Any] | None:
    values = data.get(key) if isinstance(data, dict) else None
    return values[0] if isinstance(values, list) and values and isinstance(values[0], dict) else None


def identifier(value: dict[str, Any] | None) -> str | None:
    if not value:
        return None
    result = value.get("_id") or value.get("id")
    return str(result) if result else None


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


def operation_coverage(document: dict[str, Any]) -> dict[str, set[str]]:
    """Load the coverage ledger and require one classification per contract operation."""
    ledger = json.loads((ROOT / "operation-coverage.json").read_text())
    groups = {
        "sdkLive": ledger["sdkLive"],
        "portalCanary": ledger["portalCanary"]["operations"],
        **{f"excluded: {reason}": values for reason, values in ledger["excluded"].items()},
    }
    declarations = [operation for values in groups.values() for operation in values]
    duplicates = {operation for operation, count in Counter(declarations).items() if count > 1}
    coverage = {
        "sdkLive": set(ledger["sdkLive"]),
        "portalCanary": set(ledger["portalCanary"]["operations"]),
        "excluded": {operation for operations in ledger["excluded"].values() for operation in operations},
    }
    classified = set().union(*coverage.values())
    operations = {
        operation["operationId"]
        for path_item in document["paths"].values()
        for method, operation in path_item.items()
        if method in HTTP_METHODS
    }
    if duplicates:
        raise RuntimeError(f"Operations have multiple coverage owners: {sorted(duplicates)}")
    if classified != operations:
        raise RuntimeError(
            f"Operation coverage drift: missing={sorted(operations - classified)}, stale={sorted(classified - operations)}"
        )
    if any(not reason.strip() or not values for reason, values in ledger["excluded"].items()):
        raise RuntimeError("Every exclusion requires a reason and at least one operation")
    return coverage


def optional(call: Callable[[], Any]) -> Any:
    try:
        return call()
    except APIError:
        return {}


def fixtures(client: Platform) -> dict[str, str]:
    account = client.account.retrieve_summary()
    owner = str(account["username"])
    datasets = client.datasets.list(owner, limit=1)
    projects = client.projects.list(owner, limit=1)
    project = first(projects, "projects")
    project_name = str(project.get("project")) if project else "missing-live-smoke-project"
    models = optional(lambda: client.models.list(owner, project_name, limit=1))
    deployments = client.deployments.list(owner, limit=1)
    integrations = client.storage_integrations.list_cloud_storage_integrations()
    dataset = first(datasets, "datasets")
    model = first(models, "models") or (models.get("model") if isinstance(models, dict) else None)
    deployment = first(deployments, "deployments")
    integration = first(integrations, "integrations")
    result = {
        "owner": owner,
        "dataset": str(dataset.get("dataset")) if dataset else "missing-live-smoke-dataset",
        "project": project_name,
        "model": str(model.get("model")) if model else "missing-live-smoke-model",
        "deployment": str(deployment.get("deployment")) if deployment else "missing-live-smoke-deployment",
        "id": identifier(integration) or "missing-live-smoke-integration",
    }
    images = optional(lambda: client.datasets.list_images(owner, result["dataset"], limit=1))
    exports = optional(lambda: client.exports.list_model(owner, project_name, result["model"], limit=1))
    result["imageId"] = identifier(first(images, "images")) or "missing-live-smoke-image"
    result["exportId"] = identifier(first(exports, "exports")) or "missing-live-smoke-export"
    targets = integration.get("targets") if integration else None
    result["target"] = str(targets[0]) if isinstance(targets, list) and targets else "missing-live-smoke-target"
    return result


def response_validator(document: dict[str, Any], observed: set[str]) -> Callable[[httpx.Response], None]:
    """Validate every live SDK response against its documented status and success schema."""
    registry = Registry().with_resource(
        "urn:openapi", Resource.from_contents(document, default_specification=DRAFT202012)
    )

    def validate(response: httpx.Response) -> None:
        response.read()
        request = response.request
        for template, path_item in document["paths"].items():
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
            if response.status_code in {401, 403} or response.status_code >= 500 or not response_spec:
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


def live_sdk_calls(client: Platform, values: dict[str, str]) -> dict[str, Callable[[], Any]]:
    owner, dataset, project, model = (values[key] for key in ("owner", "dataset", "project", "model"))
    deployment, image_id, export_id = (values[key] for key in ("deployment", "imageId", "exportId"))
    return {
        "get_api_account_summary": client.account.retrieve_summary,
        "get_api_api_keys": client.account.list_api_keys,
        "get_api_billing_transactions": client.billing.list_transactions,
        "get_api_billing_usage_summary": client.billing.list_usage_summary,
        "get_api_datasets_owner": lambda: client.datasets.list(owner, limit=1),
        "get_api_datasets_owner_dataset": lambda: client.datasets.retrieve(owner, dataset),
        "get_api_datasets_owner_dataset_class_stats": lambda: client.datasets.retrieve_class_stats(owner, dataset),
        "get_api_datasets_owner_dataset_embeddings": lambda: client.datasets.retrieve_embeddings(owner, dataset),
        "get_api_datasets_owner_dataset_export": lambda: client.datasets.retrieve_export(owner, dataset),
        "get_api_datasets_owner_dataset_images": lambda: client.datasets.list_images(owner, dataset, limit=1),
        "get_api_datasets_owner_dataset_images_clustering": lambda: client.datasets.retrieve_images_clustering(
            owner, dataset, limit=1
        ),
        "get_api_datasets_owner_dataset_models": lambda: client.datasets.list_models(owner, dataset),
        "get_api_deployments_owner": lambda: client.deployments.list(owner, limit=1),
        "get_api_deployments_owner_deployment": lambda: client.deployments.retrieve(owner, deployment),
        "get_api_deployments_owner_deployment_health": lambda: client.deployments.retrieve_health(owner, deployment),
        "get_api_deployments_owner_deployment_logs": lambda: client.deployments.retrieve_logs(
            owner, deployment, limit=1
        ),
        "get_api_deployments_owner_deployment_metrics": lambda: client.deployments.retrieve_metrics(owner, deployment),
        "get_api_explore_search": lambda: client.explore.retrieve_search(limit=1),
        "get_api_images_imageId": lambda: client.images.retrieve(image_id),
        "get_api_integrations_buckets": client.storage_integrations.list_cloud_storage_integrations,
        "get_api_integrations_buckets_id_objects": lambda: client.storage_integrations.browse_cloud_storage_objects(
            values["id"], target=values["target"]
        ),
        "get_api_models_owner_project": lambda: client.models.list(owner, project, limit=1),
        "get_api_models_owner_project_model": lambda: client.models.retrieve(owner, project, model),
        "get_api_models_owner_project_model_exports": lambda: client.exports.list_model(owner, project, model, limit=1),
        "get_api_models_owner_project_model_exports_exportId": lambda: client.exports.retrieve_status(
            owner, project, model, export_id
        ),
        "get_api_models_owner_project_model_files": lambda: client.models.retrieve_files(owner, project, model),
        "get_api_models_owner_project_model_training": lambda: client.models.retrieve_training(owner, project, model),
        "get_api_projects_owner": lambda: client.projects.list(owner, limit=1),
        "get_api_projects_owner_project": lambda: client.projects.retrieve(owner, project),
        "get_api_storage": client.account.retrieve_storage_usage,
        "get_api_training_gpu_availability": client.training.retrieve_gpu_availability,
        "get_api_trash": lambda: client.lifecycle.retrieve_trash(limit=1),
        "get_api_users": lambda: client.account.retrieve_public_user_profile(username=owner),
        "post_api_datasets_owner_dataset_images": lambda: client.datasets.retrieve_selected_images(
            owner, dataset, image_ids=[image_id]
        ),
        "post_api_images_urls": lambda: client.images.retrieve_signed_urls(image_ids=[image_id]),
    }


def validate_sdk(document: dict[str, Any]) -> None:
    coverage = operation_coverage(document)
    observed: set[str] = set()
    http_client = httpx.Client(timeout=60, event_hooks={"response": [response_validator(document, observed)]})
    with Platform(base_url=BASE_URL, http_client=http_client) as client:
        values = fixtures(client)
        calls = live_sdk_calls(client, values)
        if set(calls) != coverage["sdkLive"]:
            raise RuntimeError(
                f"Live SDK call drift: missing={sorted(coverage['sdkLive'] - set(calls))}, "
                f"stale={sorted(set(calls) - coverage['sdkLive'])}"
            )
        for operation_id, call in calls.items():
            try:
                call()
            except APIError:
                pass
            if operation_id not in observed:
                raise RuntimeError(f"SDK method did not request {operation_id}")
    if observed != coverage["sdkLive"]:
        raise RuntimeError(f"Unexpected live SDK operations: {sorted(observed - coverage['sdkLive'])}")
    print(f"Validated {len(observed)} generated Python SDK operations against production")


def main() -> None:
    if not os.environ.get("ULTRALYTICS_API_KEY"):
        raise RuntimeError("ULTRALYTICS_API_KEY is required")
    document = json.loads((ROOT / "openapi.json").read_text())
    validate_sdk(document)


if __name__ == "__main__":
    main()
