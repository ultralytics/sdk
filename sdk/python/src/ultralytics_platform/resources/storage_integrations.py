# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from __future__ import annotations

from typing import Any, cast

from .._client import (
    AsyncAPIClient,
    SyncAPIClient,
    _path_parameter,
    _query_parameter,
)
from ..types import (
    StorageIntegrationsBrowseCloudStorageObjectsResponse,
    StorageIntegrationsConnectCloudStorageResponse,
    StorageIntegrationsDisconnectCloudStorageResponse,
    StorageIntegrationsDiscoverCloudStorageLocationsResponse,
    StorageIntegrationsListCloudStorageIntegrationsResponse,
)


class StorageIntegrations:
    """Storage Integrations API operations."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def disconnect_cloud_storage(self, id: str) -> StorageIntegrationsDisconnectCloudStorageResponse:
        """Disconnect cloud storage.

        Removes saved credentials without deleting provider data. Connected datasets remain visible but their files are unavailable until the same storage account is reconnected.

        Args:
            id (str): Cloud integration ID

        Returns:
            (StorageIntegrationsDisconnectCloudStorageResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            StorageIntegrationsDisconnectCloudStorageResponse,
            self._client.request(
                "DELETE",
                f"/api/integrations/buckets/{_path_parameter(id, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
            ),
        )

    def browse_cloud_storage_objects(
        self, id: str, *, target: str, prefix: str | None = None, cursor: str | None = None
    ) -> StorageIntegrationsBrowseCloudStorageObjectsResponse:
        """Browse cloud storage objects.

        Lists folders and objects beneath a prefix in a connected bucket or container.

        Args:
            id (str): Cloud integration ID
            target (str): Bucket or container name
            prefix (str, optional): Folder prefix
            cursor (str, optional): Provider pagination cursor

        Returns:
            (StorageIntegrationsBrowseCloudStorageObjectsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            StorageIntegrationsBrowseCloudStorageObjectsResponse,
            self._client.request(
                "GET",
                f"/api/integrations/buckets/{_path_parameter(id, explode=False, allow_reserved=False)}/objects",
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("target", target, style="form", explode=True),
                    *_query_parameter("prefix", prefix, style="form", explode=True),
                    *_query_parameter("cursor", cursor, style="form", explode=True),
                ],
            ),
        )

    def list_cloud_storage_integrations(self) -> StorageIntegrationsListCloudStorageIntegrationsResponse:
        """List cloud storage integrations.

        Returns the cloud storage integrations configured for the API key's workspace.

        Returns:
            (StorageIntegrationsListCloudStorageIntegrationsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            StorageIntegrationsListCloudStorageIntegrationsResponse,
            self._client.request("GET", "/api/integrations/buckets", auth=("Authorization", "Bearer ")),
        )

    def connect_cloud_storage(self, *, body: Any) -> StorageIntegrationsConnectCloudStorageResponse:
        """Connect cloud storage.

        Validates and saves a GCS, Amazon S3, or Azure Blob Storage integration.

        Args:
            body (Any): Request body.

        Returns:
            (StorageIntegrationsConnectCloudStorageResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            StorageIntegrationsConnectCloudStorageResponse,
            self._client.request("POST", "/api/integrations/buckets", auth=("Authorization", "Bearer "), json=body),
        )

    def discover_cloud_storage_locations(
        self, *, body: dict[str, Any]
    ) -> StorageIntegrationsDiscoverCloudStorageLocationsResponse:
        """Discover cloud storage locations.

        Lists accessible buckets or containers using the supplied provider credentials.

        Args:
            body (dict[str, Any]): Request body.

        Returns:
            (StorageIntegrationsDiscoverCloudStorageLocationsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            StorageIntegrationsDiscoverCloudStorageLocationsResponse,
            self._client.request(
                "POST", "/api/integrations/buckets/discover", auth=("Authorization", "Bearer "), json=body
            ),
        )


class AsyncStorageIntegrations:
    """Asynchronous Storage Integrations API operations."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def disconnect_cloud_storage(self, id: str) -> StorageIntegrationsDisconnectCloudStorageResponse:
        """Disconnect cloud storage.

        Removes saved credentials without deleting provider data. Connected datasets remain visible but their files are unavailable until the same storage account is reconnected.

        Args:
            id (str): Cloud integration ID

        Returns:
            (StorageIntegrationsDisconnectCloudStorageResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            StorageIntegrationsDisconnectCloudStorageResponse,
            await self._client.request(
                "DELETE",
                f"/api/integrations/buckets/{_path_parameter(id, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
            ),
        )

    async def browse_cloud_storage_objects(
        self, id: str, *, target: str, prefix: str | None = None, cursor: str | None = None
    ) -> StorageIntegrationsBrowseCloudStorageObjectsResponse:
        """Browse cloud storage objects.

        Lists folders and objects beneath a prefix in a connected bucket or container.

        Args:
            id (str): Cloud integration ID
            target (str): Bucket or container name
            prefix (str, optional): Folder prefix
            cursor (str, optional): Provider pagination cursor

        Returns:
            (StorageIntegrationsBrowseCloudStorageObjectsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            StorageIntegrationsBrowseCloudStorageObjectsResponse,
            await self._client.request(
                "GET",
                f"/api/integrations/buckets/{_path_parameter(id, explode=False, allow_reserved=False)}/objects",
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("target", target, style="form", explode=True),
                    *_query_parameter("prefix", prefix, style="form", explode=True),
                    *_query_parameter("cursor", cursor, style="form", explode=True),
                ],
            ),
        )

    async def list_cloud_storage_integrations(self) -> StorageIntegrationsListCloudStorageIntegrationsResponse:
        """List cloud storage integrations.

        Returns the cloud storage integrations configured for the API key's workspace.

        Returns:
            (StorageIntegrationsListCloudStorageIntegrationsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            StorageIntegrationsListCloudStorageIntegrationsResponse,
            await self._client.request("GET", "/api/integrations/buckets", auth=("Authorization", "Bearer ")),
        )

    async def connect_cloud_storage(self, *, body: Any) -> StorageIntegrationsConnectCloudStorageResponse:
        """Connect cloud storage.

        Validates and saves a GCS, Amazon S3, or Azure Blob Storage integration.

        Args:
            body (Any): Request body.

        Returns:
            (StorageIntegrationsConnectCloudStorageResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            StorageIntegrationsConnectCloudStorageResponse,
            await self._client.request(
                "POST", "/api/integrations/buckets", auth=("Authorization", "Bearer "), json=body
            ),
        )

    async def discover_cloud_storage_locations(
        self, *, body: dict[str, Any]
    ) -> StorageIntegrationsDiscoverCloudStorageLocationsResponse:
        """Discover cloud storage locations.

        Lists accessible buckets or containers using the supplied provider credentials.

        Args:
            body (dict[str, Any]): Request body.

        Returns:
            (StorageIntegrationsDiscoverCloudStorageLocationsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            StorageIntegrationsDiscoverCloudStorageLocationsResponse,
            await self._client.request(
                "POST", "/api/integrations/buckets/discover", auth=("Authorization", "Bearer "), json=body
            ),
        )
