# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license
"""Response hooks that Platform and AsyncPlatform register on the HTTP clients they create; they must never raise."""

from __future__ import annotations

from contextlib import suppress

import httpx

WAKE_URL = "http://127.0.0.1:8765/wake"  # the On Premise worker's fixed local port


def job_origin(response: httpx.Response) -> str | None:
    """Return the Platform origin of a just-created ingest or training job, else None.

    Responses do not say where a job runs, so every one wakes; without a worker, or an old one, nothing changes.
    """
    request = response.request
    if response.is_success and request.method == "POST" and request.url.path.endswith(("/ingest", "/training/start")):
        return f"{request.url.scheme}://{request.url.netloc.decode()}"  # workers accept only their Platform's origin
    return None


def response_hook(response: httpx.Response) -> None:
    """Have an On Premise worker on this machine claim a just-created ingest or training job instead of polling."""
    if origin := job_origin(response):
        # stream returns after the headers, so a listener that drips a body can't hold the caller open
        with (
            suppress(httpx.HTTPError),
            httpx.stream("GET", WAKE_URL, headers={"Origin": origin}, timeout=0.5, trust_env=False),
        ):
            pass


async def async_response_hook(response: httpx.Response) -> None:
    """Wake the local On Premise worker like response_hook, without blocking the event loop."""
    if origin := job_origin(response):
        with suppress(httpx.HTTPError):
            async with (
                httpx.AsyncClient(trust_env=False) as client,
                client.stream("GET", WAKE_URL, headers={"Origin": origin}, timeout=0.5),
            ):
                pass
