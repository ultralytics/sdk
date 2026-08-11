# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from __future__ import annotations

import asyncio
import json
import os
from pathlib import Path
from typing import Any
from urllib.parse import quote

import httpx
from jsonschema import Draft202012Validator, ValidationError
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012
from ultralytics_platform import AsyncPlatform, Platform

ROOT = Path(__file__).parents[1]
BASE_URL = "https://platform.ultralytics.com"


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


def get(client: httpx.Client, path: str, params: dict[str, Any] | None = None) -> Any:
    response = client.get(path, params=params)
    response.raise_for_status()
    return response.json()


def optional_get(client: httpx.Client, path: str, params: dict[str, Any] | None = None) -> Any:
    response = client.get(path, params=params)
    if response.status_code in {401, 403} or response.status_code >= 500:
        response.raise_for_status()
    return response.json() if response.is_success else {}


def fixtures(client: httpx.Client) -> dict[str, str]:
    summary = get(client, "/api/account/summary")
    datasets = get(client, "/api/datasets", {"limit": 1})
    projects = get(client, "/api/projects", {"limit": 1})
    project = first(projects, "projects")
    project_id = identifier(project)
    models = optional_get(client, "/api/models", {"projectId": project_id} if project_id else None)
    deployments = get(client, "/api/deployments", {"limit": 1})
    integrations = get(client, "/api/integrations/buckets")
    dataset = first(datasets, "datasets")
    model = first(models, "models") or (models.get("model") if isinstance(models, dict) else None)
    deployment = first(deployments, "deployments")
    integration = first(integrations, "integrations")
    result = {
        "username": str(summary.get("username", "ultralytics")),
        "datasetId": identifier(dataset) or "missing-live-smoke-dataset",
        "projectId": project_id or "missing-live-smoke-project",
        "modelId": identifier(model) or "missing-live-smoke-model",
        "deploymentId": identifier(deployment) or "missing-live-smoke-deployment",
        "id": identifier(integration) or "missing-live-smoke-integration",
    }
    images = optional_get(client, f"/api/datasets/{quote(result['datasetId'], safe='')}/images", {"limit": 1})
    exports = optional_get(client, "/api/exports", {"modelId": result["modelId"], "limit": 1})
    result["imageId"] = identifier(first(images, "images")) or "missing-live-smoke-image"
    result["exportId"] = identifier(first(exports, "exports")) or "missing-live-smoke-export"
    targets = integration.get("targets") if integration else None
    result["target"] = str(targets[0]) if isinstance(targets, list) and targets else "missing-live-smoke-target"
    return result


def validate_gets(document: dict[str, Any], client: httpx.Client) -> None:
    values = fixtures(client)
    registry = Registry().with_resource(
        "urn:openapi", Resource.from_contents(document, default_specification=DRAFT202012)
    )
    exercised = successful = 0
    failures: list[str] = []
    for path, path_item in document["paths"].items():
        operation = path_item.get("get")
        if not operation:
            continue
        request_path = path
        parameters = [*path_item.get("parameters", []), *operation.get("parameters", [])]
        query: dict[str, Any] = {}
        for parameter in parameters:
            name = parameter["name"]
            if parameter["in"] == "path":
                request_path = request_path.replace(f"{{{name}}}", quote(values.get(name, f"missing-{name}"), safe=""))
            elif parameter.get("required"):
                query[name] = values.get(name, f"live-smoke-{name}")
        if path == "/api/models":
            query["projectId"] = values["projectId"]
        response = client.get(request_path, params=query)
        exercised += 1
        print(f"GET {path}: {response.status_code}")
        if response.status_code in {401, 403} or response.status_code >= 500:
            raise RuntimeError(f"GET {path} returned {response.status_code}")
        if not response.is_success:
            continue
        successful += 1
        response_spec = operation["responses"].get(str(response.status_code)) or operation["responses"].get("default")
        if not response_spec:
            raise RuntimeError(f"GET {path} has no response schema for {response.status_code}")
        response_spec = resolve(document, response_spec)
        media = response_spec.get("content", {}).get("application/json")
        if media and media.get("schema"):
            try:
                Draft202012Validator(absolute_references(media["schema"]), registry=registry).validate(response.json())
            except ValidationError as error:
                failures.append(f"GET {path}: {error.json_path} failed {error.validator}")
    if exercised != 45:
        raise RuntimeError(f"Expected 45 GET operations, exercised {exercised}")
    if failures:
        raise RuntimeError("Response schema failures:\n" + "\n".join(failures))
    print(f"Validated {successful} successful responses across all {exercised} GET operations")


async def validate_async_sdk() -> None:
    async with AsyncPlatform() as client:
        await client.account.retrieve_summary()


def main() -> None:
    if not os.environ.get("ULTRALYTICS_API_KEY"):
        raise RuntimeError("ULTRALYTICS_API_KEY is required")
    with Platform() as sdk:
        sdk.account.retrieve_summary()
    asyncio.run(validate_async_sdk())
    document = json.loads((ROOT / "docs/openapi.json").read_text())
    headers = {"Authorization": f"Bearer {os.environ['ULTRALYTICS_API_KEY']}"}
    with httpx.Client(base_url=BASE_URL, headers=headers, follow_redirects=True, timeout=30) as client:
        validate_gets(document, client)


if __name__ == "__main__":
    main()
