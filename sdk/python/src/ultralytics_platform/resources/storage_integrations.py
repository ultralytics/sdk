# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from __future__ import annotations

from typing import Any, cast

import httpx

from .._client import (
    NOT_GIVEN,
    AsyncAPIClient,
    NotGiven,
    SyncAPIClient,
    _path_parameter,
    _query_parameter,
)
from ..types import (
    StorageIntegrationsCreateResponse,
    StorageIntegrationsDeleteResponse,
    StorageIntegrationsDiscoverResponse,
    StorageIntegrationsListResponse,
    StorageIntegrationsObjectsResponse,
)


class StorageIntegrations:
    """Storage Integrations API operations."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def delete(
        self, id: str, timeout: float | httpx.Timeout | None = None, extra_headers: dict[str, str] | None = None
    ) -> StorageIntegrationsDeleteResponse:
        """Disconnect cloud storage.

        Removes saved credentials without deleting provider data. Connected datasets remain visible but their files are unavailable until the same storage account is reconnected.

        Args:
            id (str): Cloud integration ID
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (StorageIntegrationsDeleteResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            StorageIntegrationsDeleteResponse,
            self._client.request(
                "DELETE",
                f"/api/integrations/buckets/{_path_parameter(id, explode=False, allow_reserved=False)}",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    def objects(
        self,
        id: str,
        *,
        target: str,
        prefix: str | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> StorageIntegrationsObjectsResponse:
        """Browse cloud storage objects.

        Lists folders and objects beneath a prefix in a connected bucket or container.

        Args:
            id (str): Cloud integration ID
            target (str): Bucket or container name
            prefix (str, optional): Folder prefix
            cursor (str, optional): Provider pagination cursor
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (StorageIntegrationsObjectsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            StorageIntegrationsObjectsResponse,
            self._client.request(
                "GET",
                f"/api/integrations/buckets/{_path_parameter(id, explode=False, allow_reserved=False)}/objects",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("target", target, style="form", explode=True),
                    *_query_parameter("prefix", prefix, style="form", explode=True),
                    *_query_parameter("cursor", cursor, style="form", explode=True),
                ],
            ),
        )

    def list(
        self, timeout: float | httpx.Timeout | None = None, extra_headers: dict[str, str] | None = None
    ) -> StorageIntegrationsListResponse:
        """List cloud storage integrations.

        Returns the cloud storage integrations configured for the API key's workspace.

        Args:
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (StorageIntegrationsListResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            StorageIntegrationsListResponse,
            self._client.request(
                "GET",
                "/api/integrations/buckets",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    def create(
        self,
        *,
        body: dict[str, Any],
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> StorageIntegrationsCreateResponse:
        """Connect cloud storage.

        Validates and saves a GCS, Amazon S3, or Azure Blob Storage integration.

        Args:
            body (dict[str, Any]): Request body.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (StorageIntegrationsCreateResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            StorageIntegrationsCreateResponse,
            self._client.request(
                "POST",
                "/api/integrations/buckets",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json=body,
            ),
        )

    def discover(
        self,
        *,
        body: dict[str, Any],
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> StorageIntegrationsDiscoverResponse:
        """Discover cloud storage locations.

        Lists accessible buckets or containers using the supplied provider credentials.

        Args:
            body (dict[str, Any]): Request body.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (StorageIntegrationsDiscoverResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            StorageIntegrationsDiscoverResponse,
            self._client.request(
                "POST",
                "/api/integrations/buckets/discover",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json=body,
            ),
        )


class AsyncStorageIntegrations:
    """Asynchronous Storage Integrations API operations."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def delete(
        self, id: str, timeout: float | httpx.Timeout | None = None, extra_headers: dict[str, str] | None = None
    ) -> StorageIntegrationsDeleteResponse:
        """Disconnect cloud storage.

        Removes saved credentials without deleting provider data. Connected datasets remain visible but their files are unavailable until the same storage account is reconnected.

        Args:
            id (str): Cloud integration ID
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (StorageIntegrationsDeleteResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            StorageIntegrationsDeleteResponse,
            await self._client.request(
                "DELETE",
                f"/api/integrations/buckets/{_path_parameter(id, explode=False, allow_reserved=False)}",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    async def objects(
        self,
        id: str,
        *,
        target: str,
        prefix: str | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> StorageIntegrationsObjectsResponse:
        """Browse cloud storage objects.

        Lists folders and objects beneath a prefix in a connected bucket or container.

        Args:
            id (str): Cloud integration ID
            target (str): Bucket or container name
            prefix (str, optional): Folder prefix
            cursor (str, optional): Provider pagination cursor
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (StorageIntegrationsObjectsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            StorageIntegrationsObjectsResponse,
            await self._client.request(
                "GET",
                f"/api/integrations/buckets/{_path_parameter(id, explode=False, allow_reserved=False)}/objects",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("target", target, style="form", explode=True),
                    *_query_parameter("prefix", prefix, style="form", explode=True),
                    *_query_parameter("cursor", cursor, style="form", explode=True),
                ],
            ),
        )

    async def list(
        self, timeout: float | httpx.Timeout | None = None, extra_headers: dict[str, str] | None = None
    ) -> StorageIntegrationsListResponse:
        """List cloud storage integrations.

        Returns the cloud storage integrations configured for the API key's workspace.

        Args:
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (StorageIntegrationsListResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            StorageIntegrationsListResponse,
            await self._client.request(
                "GET",
                "/api/integrations/buckets",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    async def create(
        self,
        *,
        body: dict[str, Any],
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> StorageIntegrationsCreateResponse:
        """Connect cloud storage.

        Validates and saves a GCS, Amazon S3, or Azure Blob Storage integration.

        Args:
            body (dict[str, Any]): Request body.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (StorageIntegrationsCreateResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            StorageIntegrationsCreateResponse,
            await self._client.request(
                "POST",
                "/api/integrations/buckets",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json=body,
            ),
        )

    async def discover(
        self,
        *,
        body: dict[str, Any],
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> StorageIntegrationsDiscoverResponse:
        """Discover cloud storage locations.

        Lists accessible buckets or containers using the supplied provider credentials.

        Args:
            body (dict[str, Any]): Request body.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (StorageIntegrationsDiscoverResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            StorageIntegrationsDiscoverResponse,
            await self._client.request(
                "POST",
                "/api/integrations/buckets/discover",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json=body,
            ),
        )
