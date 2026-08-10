# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from __future__ import annotations

from typing import Any, cast

from .._client import (
    NOT_GIVEN,
    AsyncAPIClient,
    NotGiven,
    SyncAPIClient,
    _path_parameter,
    _query_parameter,
)
from ..types import (
    ExportsCreateResponse,
    ExportsDeleteResponse,
    ExportsListResponse,
    ExportsRetrieveResponse,
    ExportsTrackDownloadResponse,
)


class Exports:
    """Exports API operations."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, *, model_id: str, status: str | None = None, limit: float | None = None) -> ExportsListResponse:
        """List model exports.

        Returns export jobs for a model, including status and download URLs for completed exports.

        Args:
            model_id (str): Model name or ID (required)
            status (str, optional): Filter by status: queued, running, completed, failed
            limit (float, optional): Number of results to return (default 20, max 100)

        Returns:
            (ExportsListResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ExportsListResponse,
            self._client.request(
                "GET",
                "/api/exports",
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("modelId", model_id, style="form", explode=True),
                    *_query_parameter("status", status, style="form", explode=True),
                    *_query_parameter("limit", limit, style="form", explode=True),
                ],
            ),
        )

    def create(
        self,
        *,
        model_id: str,
        format: str,
        gpu_type: str | NotGiven = NOT_GIVEN,
        args: dict[str, Any] | NotGiven = NOT_GIVEN,
    ) -> ExportsCreateResponse:
        """Export model to a new format.

        Converts a trained model to a different format for deployment (ONNX, TensorRT, CoreML, LiteRT, etc.).

        Args:
            model_id (str): Model to export (name or ID)
            format (str): Target format: onnx, engine, coreml, litert, openvino, torchscript, etc.
            gpu_type (str, optional): GPU type (required for TensorRT/engine exports)
            args (dict[str, Any], optional): Additional export options (e.g. imgsz, quantize, dynamic)

        Returns:
            (ExportsCreateResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ExportsCreateResponse,
            self._client.request(
                "POST",
                "/api/exports",
                auth=("Authorization", "Bearer "),
                json={"modelId": model_id, "format": format, "gpuType": gpu_type, "args": args},
            ),
        )

    def retrieve(self, export_id: str) -> ExportsRetrieveResponse:
        """Get export status.

        Returns one export job, including a signed download URL when complete.

        Args:
            export_id (str): exportId path parameter.

        Returns:
            (ExportsRetrieveResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ExportsRetrieveResponse,
            self._client.request(
                "GET",
                f"/api/exports/{_path_parameter(export_id, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
            ),
        )

    def delete(self, export_id: str) -> ExportsDeleteResponse:
        """Cancel or delete an export.

        Cancels an active export or deletes a finished export and its file.

        Args:
            export_id (str): exportId path parameter.

        Returns:
            (ExportsDeleteResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ExportsDeleteResponse,
            self._client.request(
                "DELETE",
                f"/api/exports/{_path_parameter(export_id, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
            ),
        )

    def track_download(self, export_id: str) -> ExportsTrackDownloadResponse:
        """Track an export download.

        Args:
            export_id (str): exportId path parameter.

        Returns:
            (ExportsTrackDownloadResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ExportsTrackDownloadResponse,
            self._client.request(
                "POST",
                f"/api/exports/{_path_parameter(export_id, explode=False, allow_reserved=False)}/track-download",
                auth=("Authorization", "Bearer "),
            ),
        )


class AsyncExports:
    """Asynchronous Exports API operations."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(
        self, *, model_id: str, status: str | None = None, limit: float | None = None
    ) -> ExportsListResponse:
        """List model exports.

        Returns export jobs for a model, including status and download URLs for completed exports.

        Args:
            model_id (str): Model name or ID (required)
            status (str, optional): Filter by status: queued, running, completed, failed
            limit (float, optional): Number of results to return (default 20, max 100)

        Returns:
            (ExportsListResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ExportsListResponse,
            await self._client.request(
                "GET",
                "/api/exports",
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("modelId", model_id, style="form", explode=True),
                    *_query_parameter("status", status, style="form", explode=True),
                    *_query_parameter("limit", limit, style="form", explode=True),
                ],
            ),
        )

    async def create(
        self,
        *,
        model_id: str,
        format: str,
        gpu_type: str | NotGiven = NOT_GIVEN,
        args: dict[str, Any] | NotGiven = NOT_GIVEN,
    ) -> ExportsCreateResponse:
        """Export model to a new format.

        Converts a trained model to a different format for deployment (ONNX, TensorRT, CoreML, LiteRT, etc.).

        Args:
            model_id (str): Model to export (name or ID)
            format (str): Target format: onnx, engine, coreml, litert, openvino, torchscript, etc.
            gpu_type (str, optional): GPU type (required for TensorRT/engine exports)
            args (dict[str, Any], optional): Additional export options (e.g. imgsz, quantize, dynamic)

        Returns:
            (ExportsCreateResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ExportsCreateResponse,
            await self._client.request(
                "POST",
                "/api/exports",
                auth=("Authorization", "Bearer "),
                json={"modelId": model_id, "format": format, "gpuType": gpu_type, "args": args},
            ),
        )

    async def retrieve(self, export_id: str) -> ExportsRetrieveResponse:
        """Get export status.

        Returns one export job, including a signed download URL when complete.

        Args:
            export_id (str): exportId path parameter.

        Returns:
            (ExportsRetrieveResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ExportsRetrieveResponse,
            await self._client.request(
                "GET",
                f"/api/exports/{_path_parameter(export_id, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
            ),
        )

    async def delete(self, export_id: str) -> ExportsDeleteResponse:
        """Cancel or delete an export.

        Cancels an active export or deletes a finished export and its file.

        Args:
            export_id (str): exportId path parameter.

        Returns:
            (ExportsDeleteResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ExportsDeleteResponse,
            await self._client.request(
                "DELETE",
                f"/api/exports/{_path_parameter(export_id, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
            ),
        )

    async def track_download(self, export_id: str) -> ExportsTrackDownloadResponse:
        """Track an export download.

        Args:
            export_id (str): exportId path parameter.

        Returns:
            (ExportsTrackDownloadResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ExportsTrackDownloadResponse,
            await self._client.request(
                "POST",
                f"/api/exports/{_path_parameter(export_id, explode=False, allow_reserved=False)}/track-download",
                auth=("Authorization", "Bearer "),
            ),
        )
