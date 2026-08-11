# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from __future__ import annotations

from typing import Any, Literal, cast

from .._client import (
    AsyncAPIClient,
    SyncAPIClient,
    _path_parameter,
    _query_parameter,
)
from ..types import (
    StorageIntegrationsBrowseCloudStorageObjectsResponse,
    StorageIntegrationsConnectCloudStorageResponse,
    StorageIntegrationsDiscoverCloudStorageLocationsResponse,
    StorageIntegrationsListCloudStorageIntegrationsResponse,
)


class StorageIntegrations:
    """Storage Integrations API operations."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list_cloud_storage_integrations(
        self, *, owner: str | None = None
    ) -> StorageIntegrationsListCloudStorageIntegrationsResponse:
        """List cloud storage integrations.

        Returns the cloud storage integrations configured for a workspace.

        Args:
            owner (str, optional): Workspace username

        Returns:
            (StorageIntegrationsListCloudStorageIntegrationsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            StorageIntegrationsListCloudStorageIntegrationsResponse,
            self._client.request(
                "GET",
                "/api/integrations/buckets",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
            ),
        )

    def connect_cloud_storage(
        self,
        *,
        provider: Literal["gcs", "s3", "azure"],
        credentials: dict[str, Any],
        targets: list[str],
        owner: str | None = None,
    ) -> StorageIntegrationsConnectCloudStorageResponse:
        """Connect cloud storage.

        Validates and saves a GCS, Amazon S3, or Azure Blob Storage integration.

        Args:
            owner (str, optional): Workspace username
            provider (Literal["gcs", "s3", "azure"]): Cloud storage provider
            credentials (dict[str, Any]): Provider credentials
            targets (list[str]): Storage buckets or containers

        Returns:
            (StorageIntegrationsConnectCloudStorageResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            StorageIntegrationsConnectCloudStorageResponse,
            self._client.request(
                "POST",
                "/api/integrations/buckets",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
                json={"provider": provider, "credentials": credentials, "targets": targets},
            ),
        )

    def discover_cloud_storage_locations(
        self, *, provider: Literal["gcs", "s3", "azure"], credentials: dict[str, Any], owner: str | None = None
    ) -> StorageIntegrationsDiscoverCloudStorageLocationsResponse:
        """Discover cloud storage locations.

        Lists accessible buckets or containers using the supplied provider credentials.

        Args:
            owner (str, optional): Workspace username
            provider (Literal["gcs", "s3", "azure"]): Cloud storage provider
            credentials (dict[str, Any]): Provider credentials

        Returns:
            (StorageIntegrationsDiscoverCloudStorageLocationsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            StorageIntegrationsDiscoverCloudStorageLocationsResponse,
            self._client.request(
                "POST",
                "/api/integrations/buckets/discover",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
                json={"provider": provider, "credentials": credentials},
            ),
        )

    def browse_cloud_storage_objects(
        self, id: str, *, target: str, prefix: str | None = None, cursor: str | None = None, owner: str | None = None
    ) -> StorageIntegrationsBrowseCloudStorageObjectsResponse:
        """Browse cloud storage objects.

        Lists folders and objects beneath a prefix in a connected bucket or container.

        Args:
            id (str): ID
            target (str): Bucket or container name
            prefix (str, optional): Folder prefix
            cursor (str, optional): Provider pagination cursor
            owner (str, optional): Workspace username

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
                    *_query_parameter("owner", owner, style="form", explode=True),
                ],
            ),
        )


class AsyncStorageIntegrations:
    """Asynchronous Storage Integrations API operations."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list_cloud_storage_integrations(
        self, *, owner: str | None = None
    ) -> StorageIntegrationsListCloudStorageIntegrationsResponse:
        """List cloud storage integrations.

        Returns the cloud storage integrations configured for a workspace.

        Args:
            owner (str, optional): Workspace username

        Returns:
            (StorageIntegrationsListCloudStorageIntegrationsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            StorageIntegrationsListCloudStorageIntegrationsResponse,
            await self._client.request(
                "GET",
                "/api/integrations/buckets",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
            ),
        )

    async def connect_cloud_storage(
        self,
        *,
        provider: Literal["gcs", "s3", "azure"],
        credentials: dict[str, Any],
        targets: list[str],
        owner: str | None = None,
    ) -> StorageIntegrationsConnectCloudStorageResponse:
        """Connect cloud storage.

        Validates and saves a GCS, Amazon S3, or Azure Blob Storage integration.

        Args:
            owner (str, optional): Workspace username
            provider (Literal["gcs", "s3", "azure"]): Cloud storage provider
            credentials (dict[str, Any]): Provider credentials
            targets (list[str]): Storage buckets or containers

        Returns:
            (StorageIntegrationsConnectCloudStorageResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            StorageIntegrationsConnectCloudStorageResponse,
            await self._client.request(
                "POST",
                "/api/integrations/buckets",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
                json={"provider": provider, "credentials": credentials, "targets": targets},
            ),
        )

    async def discover_cloud_storage_locations(
        self, *, provider: Literal["gcs", "s3", "azure"], credentials: dict[str, Any], owner: str | None = None
    ) -> StorageIntegrationsDiscoverCloudStorageLocationsResponse:
        """Discover cloud storage locations.

        Lists accessible buckets or containers using the supplied provider credentials.

        Args:
            owner (str, optional): Workspace username
            provider (Literal["gcs", "s3", "azure"]): Cloud storage provider
            credentials (dict[str, Any]): Provider credentials

        Returns:
            (StorageIntegrationsDiscoverCloudStorageLocationsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            StorageIntegrationsDiscoverCloudStorageLocationsResponse,
            await self._client.request(
                "POST",
                "/api/integrations/buckets/discover",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
                json={"provider": provider, "credentials": credentials},
            ),
        )

    async def browse_cloud_storage_objects(
        self, id: str, *, target: str, prefix: str | None = None, cursor: str | None = None, owner: str | None = None
    ) -> StorageIntegrationsBrowseCloudStorageObjectsResponse:
        """Browse cloud storage objects.

        Lists folders and objects beneath a prefix in a connected bucket or container.

        Args:
            id (str): ID
            target (str): Bucket or container name
            prefix (str, optional): Folder prefix
            cursor (str, optional): Provider pagination cursor
            owner (str, optional): Workspace username

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
                    *_query_parameter("owner", owner, style="form", explode=True),
                ],
            ),
        )
