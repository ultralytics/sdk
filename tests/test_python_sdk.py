from __future__ import annotations

import asyncio

import httpx
import pytest
from ultralytics_platform import APIError, AsyncPlatform, Platform


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


def test_api_error_details() -> None:
    def handle(request: httpx.Request) -> httpx.Response:
        return httpx.Response(422, json={"detail": "invalid"}, headers={"x-request-id": "request-1"}, request=request)

    http_client = httpx.Client(transport=httpx.MockTransport(handle))
    with Platform(api_key="ul_test", http_client=http_client) as client, pytest.raises(APIError) as raised:
        client.datasets.list()

    assert raised.value.status_code == 422
    assert raised.value.body == '{"detail":"invalid"}'
    assert raised.value.request_id == "request-1"
