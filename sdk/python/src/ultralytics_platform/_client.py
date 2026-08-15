# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from __future__ import annotations

import asyncio
import json
import time
from collections.abc import Sequence
from typing import Any
from urllib.parse import quote

import httpx

from ._exceptions import APIConnectionError, APIError


class NotGiven:
    """Sentinel for omitted request values."""

    def __bool__(self) -> bool:
        return False

    def __repr__(self) -> str:
        return "NOT_GIVEN"


NOT_GIVEN = NotGiven()


def _path_parameter(value: Any, *, explode: bool, allow_reserved: bool) -> str:
    safe = ":/?#[]@!$&'()*+,;=" if allow_reserved else ""

    def encode(item: Any) -> str:
        return quote(str(item), safe=safe)

    if isinstance(value, dict):
        parts = (
            [f"{encode(key)}={encode(item)}" for key, item in value.items()]
            if explode
            else [encode(item) for pair in value.items() for item in pair]
        )
        return ",".join(parts)
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
        return ",".join(encode(item) for item in value)
    return encode(value)


def _query_parameter(name: str, value: Any, *, style: str, explode: bool) -> list[tuple[str, Any]]:
    if value is None or isinstance(value, NotGiven):
        return []
    if isinstance(value, dict):
        if style == "deepObject":
            return [(f"{name}[{key}]", item) for key, item in value.items()]
        if explode:
            return list(value.items())
        return [(name, ",".join(str(item) for pair in value.items() for item in pair))]
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
        if style == "form" and explode:
            return [(name, item) for item in value]
        separator = " " if style == "spaceDelimited" else "|" if style == "pipeDelimited" else ","
        return [(name, separator.join(str(item) for item in value))]
    return [(name, value)]


def _without_none(values: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in values.items() if value is not None and not isinstance(value, NotGiven)}


def _without_not_given(values: Any) -> Any:
    if isinstance(values, dict):
        return {key: value for key, value in values.items() if not isinstance(value, NotGiven)}
    return None if isinstance(values, NotGiven) else values


def _json_value(value: Any) -> Any:
    """Drop omitted values and turn any sequence into a list so the payload is JSON serializable."""
    if isinstance(value, dict):
        return {key: _json_value(item) for key, item in value.items() if not isinstance(item, NotGiven)}
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
        return [_json_value(item) for item in value]
    return None if isinstance(value, NotGiven) else value


def _form_data(values: dict[str, Any], *, multipart: bool) -> dict[str, Any]:
    """Encode object fields as JSON parts for multipart bodies and as exploded fields for URL-encoded bodies."""
    fields: dict[str, Any] = {}
    for name, value in _without_not_given(values).items():
        if isinstance(value, dict):
            if multipart:
                fields[name] = json.dumps(value)
            else:
                fields.update(value)
        else:
            fields[name] = value
    return fields


def _retry_delay(response: httpx.Response | None, attempt: int) -> float:
    if response is not None:
        try:
            return min(max(float(response.headers.get("retry-after", "")), 0.0), 60.0)
        except ValueError:
            pass
    return min(0.5 * 2.0**attempt, 8.0)


class SyncAPIClient:
    def __init__(
        self,
        *,
        api_key: str | None,
        base_url: str,
        timeout: float | httpx.Timeout,
        max_retries: int,
        http_client: httpx.Client | None,
    ) -> None:
        self._client = http_client or httpx.Client(timeout=timeout)
        self._base_url = httpx.URL(f"{base_url.rstrip('/')}/")
        self._api_key = api_key
        self._max_retries = max_retries

    def request(self, method: str, path: str, **kwargs: Any) -> Any:
        retryable = method.upper() in {"GET", "HEAD", "OPTIONS"}
        headers = {**_without_none(kwargs.get("headers") or {}), **(kwargs.get("extra_headers") or {})}
        if self._api_key and (auth := kwargs.get("auth")):
            headers.setdefault(auth[0], f"{auth[1]}{self._api_key}")
        server = kwargs.get("server")
        url = self._base_url.join(f"{server.rstrip('/')}/{path.lstrip('/')}" if server else path.lstrip("/"))
        for attempt in range(self._max_retries + 1):
            try:
                response = self._client.request(
                    method,
                    url,
                    params=kwargs.get("params"),
                    headers=headers,
                    cookies=_without_none(kwargs.get("cookies") or {}) or None,
                    json=_json_value(kwargs.get("json")),
                    data=kwargs.get("data"),
                    files=_without_not_given(kwargs.get("files")),
                    content=_without_not_given(kwargs.get("content")),
                    **({"timeout": timeout} if (timeout := kwargs.get("timeout")) is not None else {}),
                )
            except httpx.HTTPError as error:
                if not retryable or attempt == self._max_retries:
                    raise APIConnectionError(str(error)) from error
                time.sleep(_retry_delay(None, attempt))
                continue
            if (
                retryable
                and attempt < self._max_retries
                and (response.status_code in {408, 409, 429} or response.status_code >= 500)
            ):
                time.sleep(_retry_delay(response, attempt))
                continue
            if response.is_error:
                raise APIError(response.status_code, response.text, response.headers.get("x-request-id"))
            if response.status_code == 204 or not response.content:
                return None
            media_type = response.headers.get("content-type", "").split(";", 1)[0].lower()
            if media_type == "application/json" or media_type.endswith("+json"):
                return response.json()
            if kwargs.get("text") or media_type.startswith("text/"):
                return response.text
            return response.content
        raise APIConnectionError("Request was not attempted")

    def close(self) -> None:
        self._client.close()


class AsyncAPIClient:
    def __init__(
        self,
        *,
        api_key: str | None,
        base_url: str,
        timeout: float | httpx.Timeout,
        max_retries: int,
        http_client: httpx.AsyncClient | None,
    ) -> None:
        self._client = http_client or httpx.AsyncClient(timeout=timeout)
        self._base_url = httpx.URL(f"{base_url.rstrip('/')}/")
        self._api_key = api_key
        self._max_retries = max_retries

    async def request(self, method: str, path: str, **kwargs: Any) -> Any:
        retryable = method.upper() in {"GET", "HEAD", "OPTIONS"}
        headers = {**_without_none(kwargs.get("headers") or {}), **(kwargs.get("extra_headers") or {})}
        if self._api_key and (auth := kwargs.get("auth")):
            headers.setdefault(auth[0], f"{auth[1]}{self._api_key}")
        server = kwargs.get("server")
        url = self._base_url.join(f"{server.rstrip('/')}/{path.lstrip('/')}" if server else path.lstrip("/"))
        for attempt in range(self._max_retries + 1):
            try:
                response = await self._client.request(
                    method,
                    url,
                    params=kwargs.get("params"),
                    headers=headers,
                    cookies=_without_none(kwargs.get("cookies") or {}) or None,
                    json=_json_value(kwargs.get("json")),
                    data=kwargs.get("data"),
                    files=_without_not_given(kwargs.get("files")),
                    content=_without_not_given(kwargs.get("content")),
                    **({"timeout": timeout} if (timeout := kwargs.get("timeout")) is not None else {}),
                )
            except httpx.HTTPError as error:
                if not retryable or attempt == self._max_retries:
                    raise APIConnectionError(str(error)) from error
                await asyncio.sleep(_retry_delay(None, attempt))
                continue
            if (
                retryable
                and attempt < self._max_retries
                and (response.status_code in {408, 409, 429} or response.status_code >= 500)
            ):
                await asyncio.sleep(_retry_delay(response, attempt))
                continue
            if response.is_error:
                raise APIError(response.status_code, response.text, response.headers.get("x-request-id"))
            if response.status_code == 204 or not response.content:
                return None
            media_type = response.headers.get("content-type", "").split(";", 1)[0].lower()
            if media_type == "application/json" or media_type.endswith("+json"):
                return response.json()
            if kwargs.get("text") or media_type.startswith("text/"):
                return response.text
            return response.content
        raise APIConnectionError("Request was not attempted")

    async def close(self) -> None:
        await self._client.aclose()
