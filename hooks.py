# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license
"""Response hooks for Platform and AsyncPlatform: wake a local On Premise worker after creating its job."""

from __future__ import annotations

from contextlib import suppress

import httpx


def wake_request(response: httpx.Response) -> dict | None:
    """Return the local wake request for a created ingest or training job; responses don't say where a job runs."""
    url = response.request.url
    if response.is_success and response.request.method == "POST" and url.path.endswith(("/ingest", "/training/start")):
        # Workers accept only their Platform's origin; reading headers only keeps a dripping listener from blocking
        origin = f"{url.scheme}://{url.netloc.decode()}"
        return {"method": "GET", "url": "http://127.0.0.1:8765/wake", "headers": {"Origin": origin}, "timeout": 0.5}
    return None


def response_hook(response: httpx.Response) -> None:
    """Wake the local worker; never raises."""
    if request := wake_request(response):
        with suppress(httpx.HTTPError), httpx.stream(**request, trust_env=False):
            pass


async def async_response_hook(response: httpx.Response) -> None:
    """Wake the local worker without blocking the event loop; never raises."""
    if request := wake_request(response):
        with suppress(httpx.HTTPError):
            async with httpx.AsyncClient(trust_env=False) as client, client.stream(**request):
                pass
