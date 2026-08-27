# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from __future__ import annotations

from typing import Any, cast

import httpx

from .._client import (
    NOT_GIVEN,
    AsyncAPIClient,
    NotGiven,
    SyncAPIClient,
)
from ..types import (
    UploadCompleteResponse,
    UploadSignedUrlResponse,
)


class Upload:
    """Upload API operations."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def complete(
        self,
        *,
        session_id: str,
        checksum: str | NotGiven = NOT_GIVEN,
        md5: str | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> UploadCompleteResponse:
        """Confirm file upload.

        Call this after uploading a file to the signed URL. Dataset uploads are verified here, then processed by the dataset ingest endpoint.

        Args:
            session_id (str): Upload session ID from signed-url response
            checksum (str, optional): checksum request value.
            md5 (str, optional): Expected uploaded object MD5 digest in hexadecimal
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

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
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={"sessionId": session_id, "checksum": checksum, "md5": md5},
            ),
        )

    def signed_url(
        self,
        *,
        body: dict[str, Any],
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> UploadSignedUrlResponse:
        """Get a file upload URL.

        Generates a pre-signed URL for uploading a file directly to cloud storage. Upload the file with a PUT request to the returned URL and headers, complete the upload, then call the resource ingest endpoint with the returned sessionId. Dataset upload URLs remain valid for 12 hours, are create-only, and filenames must end in .zip, .tar, .tar.gz, .tgz, or .ndjson — package loose images into an archive.

        Args:
            body (dict[str, Any]): Request body for generating a signed upload URL
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (UploadSignedUrlResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            UploadSignedUrlResponse,
            self._client.request(
                "POST",
                "/api/upload/signed-url",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json=body,
            ),
        )


class AsyncUpload:
    """Asynchronous Upload API operations."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def complete(
        self,
        *,
        session_id: str,
        checksum: str | NotGiven = NOT_GIVEN,
        md5: str | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> UploadCompleteResponse:
        """Confirm file upload.

        Call this after uploading a file to the signed URL. Dataset uploads are verified here, then processed by the dataset ingest endpoint.

        Args:
            session_id (str): Upload session ID from signed-url response
            checksum (str, optional): checksum request value.
            md5 (str, optional): Expected uploaded object MD5 digest in hexadecimal
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

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
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={"sessionId": session_id, "checksum": checksum, "md5": md5},
            ),
        )

    async def signed_url(
        self,
        *,
        body: dict[str, Any],
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> UploadSignedUrlResponse:
        """Get a file upload URL.

        Generates a pre-signed URL for uploading a file directly to cloud storage. Upload the file with a PUT request to the returned URL and headers, complete the upload, then call the resource ingest endpoint with the returned sessionId. Dataset upload URLs remain valid for 12 hours, are create-only, and filenames must end in .zip, .tar, .tar.gz, .tgz, or .ndjson — package loose images into an archive.

        Args:
            body (dict[str, Any]): Request body for generating a signed upload URL
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (UploadSignedUrlResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            UploadSignedUrlResponse,
            await self._client.request(
                "POST",
                "/api/upload/signed-url",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json=body,
            ),
        )
