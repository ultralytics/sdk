# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from __future__ import annotations

from typing import Any, Literal, cast

from .._client import (
    AsyncAPIClient,
    SyncAPIClient,
    _query_parameter,
)
from ..types import (
    LifecyclePermanentlyDeleteTrashResponse,
    LifecycleRestoreTrashedItemResponse,
    LifecycleRetrieveTrashResponse,
)


class Lifecycle:
    """Lifecycle API operations."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def retrieve_trash(
        self,
        *,
        type: Literal["all", "project", "dataset", "model"] | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> LifecycleRetrieveTrashResponse:
        """View trash.

        Returns deleted items that can still be restored. Items are permanently deleted after 30 days.

        Args:
            type (Literal["all", "project", "dataset", "model"], optional): type query parameter.
            page (int, optional): page query parameter.
            limit (int, optional): limit query parameter.

        Returns:
            (LifecycleRetrieveTrashResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            LifecycleRetrieveTrashResponse,
            self._client.request(
                "GET",
                "/api/trash",
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("type", type, style="form", explode=True),
                    *_query_parameter("page", page, style="form", explode=True),
                    *_query_parameter("limit", limit, style="form", explode=True),
                ],
            ),
        )

    def restore_trashed_item(
        self, *, id: str, type: Literal["project", "dataset", "model"]
    ) -> LifecycleRestoreTrashedItemResponse:
        """Restore a trashed item.

        Restores a trashed project, dataset, or model before its retention period expires.

        Args:
            id (str): id request value.
            type (Literal["project", "dataset", "model"]): type request value.

        Returns:
            (LifecycleRestoreTrashedItemResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            LifecycleRestoreTrashedItemResponse,
            self._client.request(
                "POST", "/api/trash", auth=("Authorization", "Bearer "), json={"id": id, "type": type}
            ),
        )

    def permanently_delete_trash(self, *, body: dict[str, Any]) -> LifecyclePermanentlyDeleteTrashResponse:
        """Permanently delete trash.

        Permanently deletes one trashed resource or all workspace trash. This cannot be undone.

        Args:
            body (dict[str, Any]): Permanently delete one trashable resource or all workspace trash

        Returns:
            (LifecyclePermanentlyDeleteTrashResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            LifecyclePermanentlyDeleteTrashResponse,
            self._client.request("DELETE", "/api/trash", auth=("Authorization", "Bearer "), json=body),
        )


class AsyncLifecycle:
    """Asynchronous Lifecycle API operations."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def retrieve_trash(
        self,
        *,
        type: Literal["all", "project", "dataset", "model"] | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> LifecycleRetrieveTrashResponse:
        """View trash.

        Returns deleted items that can still be restored. Items are permanently deleted after 30 days.

        Args:
            type (Literal["all", "project", "dataset", "model"], optional): type query parameter.
            page (int, optional): page query parameter.
            limit (int, optional): limit query parameter.

        Returns:
            (LifecycleRetrieveTrashResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            LifecycleRetrieveTrashResponse,
            await self._client.request(
                "GET",
                "/api/trash",
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("type", type, style="form", explode=True),
                    *_query_parameter("page", page, style="form", explode=True),
                    *_query_parameter("limit", limit, style="form", explode=True),
                ],
            ),
        )

    async def restore_trashed_item(
        self, *, id: str, type: Literal["project", "dataset", "model"]
    ) -> LifecycleRestoreTrashedItemResponse:
        """Restore a trashed item.

        Restores a trashed project, dataset, or model before its retention period expires.

        Args:
            id (str): id request value.
            type (Literal["project", "dataset", "model"]): type request value.

        Returns:
            (LifecycleRestoreTrashedItemResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            LifecycleRestoreTrashedItemResponse,
            await self._client.request(
                "POST", "/api/trash", auth=("Authorization", "Bearer "), json={"id": id, "type": type}
            ),
        )

    async def permanently_delete_trash(self, *, body: dict[str, Any]) -> LifecyclePermanentlyDeleteTrashResponse:
        """Permanently delete trash.

        Permanently deletes one trashed resource or all workspace trash. This cannot be undone.

        Args:
            body (dict[str, Any]): Permanently delete one trashable resource or all workspace trash

        Returns:
            (LifecyclePermanentlyDeleteTrashResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            LifecyclePermanentlyDeleteTrashResponse,
            await self._client.request("DELETE", "/api/trash", auth=("Authorization", "Bearer "), json=body),
        )
