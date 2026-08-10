# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from __future__ import annotations

import time
from typing import Any
from urllib.parse import quote

import httpx

from ._exceptions import APIConnectionError, APIError


class NotGiven:
    """Sentinel for omitted request values."""


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
    if isinstance(value, (list, tuple)):
        return ",".join(encode(item) for item in value)
    return encode(value)


def _query_parameter(name: str, value: Any, *, style: str, explode: bool) -> list[tuple[str, Any]]:
    if value is None:
        return []
    if isinstance(value, dict):
        if style == "deepObject":
            return [(f"{name}[{key}]", item) for key, item in value.items()]
        if explode:
            return list(value.items())
        return [(name, ",".join(str(item) for pair in value.items() for item in pair))]
    if isinstance(value, (list, tuple)):
        if style == "form" and explode:
            return [(name, item) for item in value]
        separator = " " if style == "spaceDelimited" else "|" if style == "pipeDelimited" else ","
        return [(name, separator.join(str(item) for item in value))]
    return [(name, value)]


def _without_none(values: Any) -> Any:
    return {key: value for key, value in values.items() if value is not None} if isinstance(values, dict) else values


def _without_not_given(values: Any) -> Any:
    if isinstance(values, dict):
        return {key: value for key, value in values.items() if not isinstance(value, NotGiven)}
    return None if isinstance(values, NotGiven) else values


def _retry_delay(response: httpx.Response | None, attempt: int) -> float:
    if response is not None:
        try:
            return min(max(float(response.headers.get("retry-after", "")), 0), 60)
        except ValueError:
            pass
    return min(0.5 * (2**attempt), 8)


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
        self._client = http_client or httpx.Client(
            base_url=f"{base_url.rstrip('/')}/",
            timeout=timeout,
        )
        self._client.base_url = httpx.URL(f"{base_url.rstrip('/')}/")
        self._api_key = api_key
        self._max_retries = max_retries

    def request(self, method: str, path: str, **kwargs: Any) -> Any:
        retryable = method.upper() in {"GET", "HEAD", "OPTIONS"}
        headers = _without_none(kwargs.get("headers")) or {}
        if self._api_key and (auth := kwargs.get("auth")):
            headers.setdefault(auth[0], f"{auth[1]}{self._api_key}")
        request_path = (
            self._client.base_url.join(f"{kwargs['server'].rstrip('/')}/{path.lstrip('/')}")
            if kwargs.get("server")
            else path.lstrip("/")
        )
        for attempt in range(self._max_retries + 1):
            try:
                response = self._client.request(
                    method,
                    request_path,
                    params=_without_none(kwargs.get("params")),
                    headers=headers,
                    cookies=_without_none(kwargs.get("cookies")),
                    json=_without_not_given(kwargs.get("json")),
                    data=_without_not_given(kwargs.get("data")),
                    files=_without_not_given(kwargs.get("files")),
                    content=_without_not_given(kwargs.get("content")),
                )
            except httpx.HTTPError as error:
                if not retryable or attempt == self._max_retries:
                    raise APIConnectionError(str(error)) from error
                time.sleep(_retry_delay(None, attempt))
                continue
            if not retryable or (response.status_code not in {408, 409, 429} and response.status_code < 500):
                break
            if attempt == self._max_retries:
                break
            time.sleep(_retry_delay(response, attempt))
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
        self._client = http_client or httpx.AsyncClient(
            base_url=f"{base_url.rstrip('/')}/",
            timeout=timeout,
        )
        self._client.base_url = httpx.URL(f"{base_url.rstrip('/')}/")
        self._api_key = api_key
        self._max_retries = max_retries

    async def request(self, method: str, path: str, **kwargs: Any) -> Any:
        retryable = method.upper() in {"GET", "HEAD", "OPTIONS"}
        headers = _without_none(kwargs.get("headers")) or {}
        if self._api_key and (auth := kwargs.get("auth")):
            headers.setdefault(auth[0], f"{auth[1]}{self._api_key}")
        request_path = (
            self._client.base_url.join(f"{kwargs['server'].rstrip('/')}/{path.lstrip('/')}")
            if kwargs.get("server")
            else path.lstrip("/")
        )
        for attempt in range(self._max_retries + 1):
            try:
                response = await self._client.request(
                    method,
                    request_path,
                    params=_without_none(kwargs.get("params")),
                    headers=headers,
                    cookies=_without_none(kwargs.get("cookies")),
                    json=_without_not_given(kwargs.get("json")),
                    data=_without_not_given(kwargs.get("data")),
                    files=_without_not_given(kwargs.get("files")),
                    content=_without_not_given(kwargs.get("content")),
                )
            except httpx.HTTPError as error:
                if not retryable or attempt == self._max_retries:
                    raise APIConnectionError(str(error)) from error
                await __import__("asyncio").sleep(_retry_delay(None, attempt))
                continue
            if not retryable or (response.status_code not in {408, 409, 429} and response.status_code < 500):
                break
            if attempt == self._max_retries:
                break
            await __import__("asyncio").sleep(_retry_delay(response, attempt))
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

    async def close(self) -> None:
        await self._client.aclose()
