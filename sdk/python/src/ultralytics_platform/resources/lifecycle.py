# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from __future__ import annotations

from typing import Any, Literal, cast

import httpx

from .._client import (
    NOT_GIVEN,
    AsyncAPIClient,
    NotGiven,
    SyncAPIClient,
    _query_parameter,
)
from ..types import (
    LifecycleDeleteTrashResponse,
    LifecycleRestoreResponse,
    LifecycleTrashResponse,
)


class Lifecycle:
    """Lifecycle API operations."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def trash(
        self,
        *,
        type: Literal["all", "project", "dataset", "model"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> LifecycleTrashResponse:
        """View trash.

        Returns deleted items that can still be restored. Items are permanently deleted after 30 days.

        Args:
            type (Literal["all", "project", "dataset", "model"], optional): type query parameter.
            page (int, optional): page query parameter.
            limit (int, optional): limit query parameter.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (LifecycleTrashResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            LifecycleTrashResponse,
            self._client.request(
                "GET",
                "/api/trash",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("type", type, style="form", explode=True),
                    *_query_parameter("page", page, style="form", explode=True),
                    *_query_parameter("limit", limit, style="form", explode=True),
                ],
            ),
        )

    def restore(
        self,
        *,
        id: str,
        type: Literal["project", "dataset", "model"],
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> LifecycleRestoreResponse:
        """Restore a trashed item.

        Restores a trashed project, dataset, or model before its retention period expires.

        Args:
            id (str): Trashed resource ID
            type (Literal["project", "dataset", "model"]): type request value.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (LifecycleRestoreResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            LifecycleRestoreResponse,
            self._client.request(
                "POST",
                "/api/trash",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={"id": id, "type": type},
            ),
        )

    def delete_trash(
        self,
        *,
        body: dict[str, Any],
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> LifecycleDeleteTrashResponse:
        """Permanently delete trash.

        Permanently deletes one trashed resource or all workspace trash. This cannot be undone.

        Args:
            body (dict[str, Any]): Permanently delete one trashable resource or all workspace trash
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (LifecycleDeleteTrashResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            LifecycleDeleteTrashResponse,
            self._client.request(
                "DELETE",
                "/api/trash",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json=body,
            ),
        )


class AsyncLifecycle:
    """Asynchronous Lifecycle API operations."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def trash(
        self,
        *,
        type: Literal["all", "project", "dataset", "model"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> LifecycleTrashResponse:
        """View trash.

        Returns deleted items that can still be restored. Items are permanently deleted after 30 days.

        Args:
            type (Literal["all", "project", "dataset", "model"], optional): type query parameter.
            page (int, optional): page query parameter.
            limit (int, optional): limit query parameter.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (LifecycleTrashResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            LifecycleTrashResponse,
            await self._client.request(
                "GET",
                "/api/trash",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("type", type, style="form", explode=True),
                    *_query_parameter("page", page, style="form", explode=True),
                    *_query_parameter("limit", limit, style="form", explode=True),
                ],
            ),
        )

    async def restore(
        self,
        *,
        id: str,
        type: Literal["project", "dataset", "model"],
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> LifecycleRestoreResponse:
        """Restore a trashed item.

        Restores a trashed project, dataset, or model before its retention period expires.

        Args:
            id (str): Trashed resource ID
            type (Literal["project", "dataset", "model"]): type request value.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (LifecycleRestoreResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            LifecycleRestoreResponse,
            await self._client.request(
                "POST",
                "/api/trash",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={"id": id, "type": type},
            ),
        )

    async def delete_trash(
        self,
        *,
        body: dict[str, Any],
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> LifecycleDeleteTrashResponse:
        """Permanently delete trash.

        Permanently deletes one trashed resource or all workspace trash. This cannot be undone.

        Args:
            body (dict[str, Any]): Permanently delete one trashable resource or all workspace trash
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (LifecycleDeleteTrashResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            LifecycleDeleteTrashResponse,
            await self._client.request(
                "DELETE",
                "/api/trash",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json=body,
            ),
        )
