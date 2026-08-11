# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from __future__ import annotations

import asyncio
import inspect
import json
import re
from io import BytesIO
from pathlib import Path
from typing import Any, BinaryIO, Literal, get_args, get_origin, get_type_hints

import httpx
import pytest
from ultralytics_platform import APIError, AsyncPlatform, Platform

ROOT = Path(__file__).parents[1]
HTTP_METHODS = {"delete", "get", "patch", "post", "put"}


def required_arguments(method: Any) -> dict[str, Any]:
    result: dict[str, Any] = {}
    hints = get_type_hints(method)
    for parameter in inspect.signature(method).parameters.values():
        if parameter.default is not inspect.Parameter.empty:
            continue
        annotation = hints[parameter.name]
        origin = get_origin(annotation)
        if origin is Literal:
            result[parameter.name] = get_args(annotation)[0]
        elif annotation is BinaryIO:
            result[parameter.name] = BytesIO(b"test")
        elif origin is list:
            result[parameter.name] = []
        elif origin is dict:
            result[parameter.name] = {}
        elif annotation is bool:
            result[parameter.name] = True
        elif annotation in {float, int}:
            result[parameter.name] = 1
        else:
            result[parameter.name] = "test"
    return result


def operations(client: Platform | AsyncPlatform) -> list[Any]:
    return [
        method
        for name, resource in vars(client).items()
        if not name.startswith("_")
        for method_name, method in inspect.getmembers(resource, inspect.ismethod)
        if not method_name.startswith("_")
    ]


def expected_requests() -> list[tuple[str, str]]:
    document = json.loads((ROOT / "openapi.json").read_text())
    return sorted(
        (method.upper(), re.sub(r"\{[^}]+\}", "test", path))
        for path, path_item in document["paths"].items()
        for method in path_item
        if method in HTTP_METHODS
    )


def response(request: httpx.Request) -> httpx.Response:
    return httpx.Response(200, json={"ok": True}, request=request)


def test_priority_resource_requests() -> None:
    requests: list[httpx.Request] = []

    def handle(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return response(request)

    http_client = httpx.Client(transport=httpx.MockTransport(handle))
    with Platform(api_key="ul_test", http_client=http_client) as client:
        datasets = client.datasets.list(limit=2)
        client.models.retrieve("model/id")
        client.deployments.create(model_id="model-id", name="production", region="us-central1")
        client.training.start(model_id="model-id", train_args={"epochs": 10})
        client.exports.create(model_id="model-id", format="onnx")

    assert [(request.method, request.url.raw_path) for request in requests] == [
        ("GET", b"/api/datasets?limit=2"),
        ("GET", b"/api/models/model%2Fid"),
        ("POST", b"/api/deployments"),
        ("POST", b"/api/training/start"),
        ("POST", b"/api/exports"),
    ]
    assert requests[0].url.params["limit"] == "2"
    assert datasets == {"ok": True}
    assert all(request.headers["Authorization"] == "Bearer ul_test" for request in requests)
    assert requests[2].content == b'{"modelId":"model-id","name":"production","region":"us-central1"}'


def test_async_resource_tree() -> None:
    async def run() -> None:
        requests: list[httpx.Request] = []

        async def handle(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            return response(request)

        http_client = httpx.AsyncClient(transport=httpx.MockTransport(handle))
        async with AsyncPlatform(api_key="ul_test", http_client=http_client) as client:
            datasets = await client.datasets.list(limit=1)

        assert requests[0].url == "https://platform.ultralytics.com/api/datasets?limit=1"
        assert datasets == {"ok": True}

    asyncio.run(run())


def test_all_operations_serialize() -> None:
    sync_requests: list[httpx.Request] = []

    def handle_sync(request: httpx.Request) -> httpx.Response:
        sync_requests.append(request)
        return response(request)

    sync_http = httpx.Client(transport=httpx.MockTransport(handle_sync))
    with Platform(api_key="ul_test", http_client=sync_http) as client:
        for method in operations(client):
            method(**required_arguments(method))

    async def run() -> list[httpx.Request]:
        async_requests: list[httpx.Request] = []

        async def handle(request: httpx.Request) -> httpx.Response:
            async_requests.append(request)
            return response(request)

        async_http = httpx.AsyncClient(transport=httpx.MockTransport(handle))
        async with AsyncPlatform(api_key="ul_test", http_client=async_http) as client:
            for method in operations(client):
                await method(**required_arguments(method))
        return async_requests

    expected = expected_requests()
    assert sorted((request.method, request.url.path) for request in sync_requests) == expected
    assert sorted((request.method, request.url.path) for request in asyncio.run(run())) == expected


def test_api_error_details() -> None:
    def handle(request: httpx.Request) -> httpx.Response:
        return httpx.Response(422, json={"detail": "invalid"}, headers={"x-request-id": "request-1"}, request=request)

    http_client = httpx.Client(transport=httpx.MockTransport(handle))
    with Platform(api_key="ul_test", http_client=http_client) as client, pytest.raises(APIError) as raised:
        client.datasets.list()

    assert raised.value.status_code == 422
    assert raised.value.body == '{"detail":"invalid"}'
    assert raised.value.request_id == "request-1"
