# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from __future__ import annotations

from typing import Literal, cast

from .._client import (
    NOT_GIVEN,
    AsyncAPIClient,
    NotGiven,
    SyncAPIClient,
)
from ..types import (
    UploadCompleteResponse,
    UploadRetrieveFileUrlResponse,
)


class Upload:
    """Upload API operations."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def complete(self, *, session_id: str, checksum: str | NotGiven = NOT_GIVEN) -> UploadCompleteResponse:
        """Confirm file upload.

        Call this after uploading a file to the signed URL. Dataset uploads are verified here, then processed by the dataset ingest endpoint.

        Args:
            session_id (str): sessionId request value.
            checksum (str, optional): checksum request value.

        Returns:
            (UploadCompleteResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            UploadCompleteResponse,
            self._client.request(
                "POST",
                "/api/upload/complete",
                auth=("Authorization", "Bearer "),
                json={"sessionId": session_id, "checksum": checksum},
            ),
        )

    def retrieve_file_url(
        self,
        *,
        asset_id: str,
        content_type: str,
        total_bytes: float,
        asset_type: Literal["datasets", "models", "images", "videos"],
        filename: str,
    ) -> UploadRetrieveFileUrlResponse:
        """Get a file upload URL.

        Generates a pre-signed URL for uploading a file directly to cloud storage. Upload the file with a PUT request to the returned URL, complete the upload, then call the resource ingest endpoint with the returned sessionId. Dataset filenames must end in .zip, .tar, .tar.gz, .tgz, or .ndjson — package loose images into an archive.

        Args:
            asset_id (str): assetId request value.
            content_type (str): contentType request value.
            total_bytes (float): totalBytes request value.
            asset_type (Literal["datasets", "models", "images", "videos"]): assetType request value.
            filename (str): filename request value.

        Returns:
            (UploadRetrieveFileUrlResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            UploadRetrieveFileUrlResponse,
            self._client.request(
                "POST",
                "/api/upload/signed-url",
                auth=("Authorization", "Bearer "),
                json={
                    "assetId": asset_id,
                    "contentType": content_type,
                    "totalBytes": total_bytes,
                    "assetType": asset_type,
                    "filename": filename,
                },
            ),
        )


class AsyncUpload:
    """Asynchronous Upload API operations."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def complete(self, *, session_id: str, checksum: str | NotGiven = NOT_GIVEN) -> UploadCompleteResponse:
        """Confirm file upload.

        Call this after uploading a file to the signed URL. Dataset uploads are verified here, then processed by the dataset ingest endpoint.

        Args:
            session_id (str): sessionId request value.
            checksum (str, optional): checksum request value.

        Returns:
            (UploadCompleteResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            UploadCompleteResponse,
            await self._client.request(
                "POST",
                "/api/upload/complete",
                auth=("Authorization", "Bearer "),
                json={"sessionId": session_id, "checksum": checksum},
            ),
        )

    async def retrieve_file_url(
        self,
        *,
        asset_id: str,
        content_type: str,
        total_bytes: float,
        asset_type: Literal["datasets", "models", "images", "videos"],
        filename: str,
    ) -> UploadRetrieveFileUrlResponse:
        """Get a file upload URL.

        Generates a pre-signed URL for uploading a file directly to cloud storage. Upload the file with a PUT request to the returned URL, complete the upload, then call the resource ingest endpoint with the returned sessionId. Dataset filenames must end in .zip, .tar, .tar.gz, .tgz, or .ndjson — package loose images into an archive.

        Args:
            asset_id (str): assetId request value.
            content_type (str): contentType request value.
            total_bytes (float): totalBytes request value.
            asset_type (Literal["datasets", "models", "images", "videos"]): assetType request value.
            filename (str): filename request value.

        Returns:
            (UploadRetrieveFileUrlResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            UploadRetrieveFileUrlResponse,
            await self._client.request(
                "POST",
                "/api/upload/signed-url",
                auth=("Authorization", "Bearer "),
                json={
                    "assetId": asset_id,
                    "contentType": content_type,
                    "totalBytes": total_bytes,
                    "assetType": asset_type,
                    "filename": filename,
                },
            ),
        )
