# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any
from urllib.parse import quote

import httpx
from jsonschema import Draft202012Validator, ValidationError
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012
from ultralytics_platform import Platform

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


def optional_get(
    document: dict[str, Any], client: httpx.Client, template: str, path: str, params: dict[str, Any] | None = None
) -> Any:
    response = client.get(path, params=params)
    if response.is_success:
        return response.json()
    if str(response.status_code) not in document["paths"][template]["get"]["responses"]:
        raise RuntimeError(f"GET {template} returned unexpected {response.status_code}")
    return {}


def fixtures(document: dict[str, Any], client: httpx.Client) -> dict[str, str]:
    account = get(client, "/api/account/summary")
    owner = str(account["username"])
    datasets = get(client, f"/api/datasets/{quote(owner, safe='')}", {"limit": 1})
    projects = get(client, f"/api/projects/{quote(owner, safe='')}", {"limit": 1})
    project = first(projects, "projects")
    project_name = str(project.get("project")) if project else "missing-live-smoke-project"
    models = optional_get(
        document,
        client,
        "/api/models/{owner}/{project}",
        f"/api/models/{quote(owner, safe='')}/{quote(project_name, safe='')}",
    )
    deployments = get(client, f"/api/deployments/{quote(owner, safe='')}", {"limit": 1})
    integrations = get(client, "/api/integrations/buckets")
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
    dataset_path = f"/api/datasets/{quote(owner, safe='')}/{quote(result['dataset'], safe='')}"
    model_path = "/api/models/{}/{}/{}".format(
        quote(owner, safe=""), quote(project_name, safe=""), quote(result["model"], safe="")
    )
    images = optional_get(
        document, client, "/api/datasets/{owner}/{dataset}/images", f"{dataset_path}/images", {"limit": 1}
    )
    exports = optional_get(
        document, client, "/api/models/{owner}/{project}/{model}/exports", f"{model_path}/exports", {"limit": 1}
    )
    result["imageId"] = identifier(first(images, "images")) or "missing-live-smoke-image"
    result["exportId"] = identifier(first(exports, "exports")) or "missing-live-smoke-export"
    targets = integration.get("targets") if integration else None
    result["target"] = str(targets[0]) if isinstance(targets, list) and targets else "missing-live-smoke-target"
    return result


def validate_gets(document: dict[str, Any], client: httpx.Client) -> dict[str, str]:
    values = fixtures(document, client)
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
        response = client.get(request_path, params=query)
        exercised += 1
        print(f"GET {path}: {response.status_code}")
        if response.status_code in {401, 403} or response.status_code >= 500:
            raise RuntimeError(f"GET {path} returned {response.status_code}")
        if not response.is_success:
            if str(response.status_code) not in operation.get("responses", {}):
                raise RuntimeError(f"GET {path} returned unexpected {response.status_code}")
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
    if exercised == 0 or successful == 0:
        raise RuntimeError("OpenAPI contract has no successful GET operations")
    if failures:
        raise RuntimeError("Response schema failures:\n" + "\n".join(failures))
    print(f"Validated {successful} successful responses across all {exercised} GET operations")
    return values


def validate_sdk(values: dict[str, str]) -> None:
    with Platform(base_url=BASE_URL) as client:
        client.account.retrieve_summary()
        client.datasets.list(values["owner"], limit=1)
        client.projects.list(values["owner"], limit=1)
        client.models.list(values["owner"], values["project"], limit=1)
        client.deployments.list(values["owner"], limit=1)
    print("Validated generated Python SDK against production")


def main() -> None:
    if not os.environ.get("ULTRALYTICS_API_KEY"):
        raise RuntimeError("ULTRALYTICS_API_KEY is required")
    document = json.loads((ROOT / "openapi.json").read_text())
    headers = {"Authorization": f"Bearer {os.environ['ULTRALYTICS_API_KEY']}"}
    with httpx.Client(base_url=BASE_URL, headers=headers, follow_redirects=True, timeout=30) as client:
        values = validate_gets(document, client)
    validate_sdk(values)


if __name__ == "__main__":
    main()
