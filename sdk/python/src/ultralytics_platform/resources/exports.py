# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from __future__ import annotations

from typing import Any, Literal, cast

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
)


class Exports:
    """Exports API operations."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(
        self,
        *,
        model_id: str,
        status: Literal["queued", "starting", "running", "completed", "failed", "cancelled"] | None = None,
        limit: float | None = None,
    ) -> ExportsListResponse:
        """List model exports.

        Returns export jobs for a model, including status and download URLs for completed exports.

        Args:
            model_id (str): Model ID
            status (Literal["queued", "starting", "running", "completed", "failed", "cancelled"], optional): Export status filter
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
        format: Literal[
            "onnx",
            "torchscript",
            "openvino",
            "engine",
            "coreml",
            "litert",
            "pb",
            "saved_model",
            "paddle",
            "ncnn",
            "edgetpu",
            "mnn",
            "rknn",
            "qnn",
            "imx",
            "axelera",
            "executorch",
            "deepx",
            "hailo",
            "ascend",
        ],
        gpu_type: Literal[
            "rtx-2000-ada",
            "rtx-a4500",
            "rtx-a5000",
            "rtx-4000-ada",
            "l4",
            "a40",
            "rtx-3090",
            "rtx-a6000",
            "rtx-pro-4000",
            "rtx-pro-4500",
            "rtx-4090",
            "rtx-6000-ada",
            "l40s",
            "rtx-pro-5000",
            "rtx-5090",
            "l40",
            "a100-80gb-pcie",
            "a100-80gb-sxm",
            "rtx-pro-6000",
            "h100-pcie",
            "h100-nvl",
            "h100-sxm",
            "h200-nvl",
            "h200-sxm",
            "b200",
            "b300",
            "jetson-thor-t5000",
            "jetson-thor-t4000",
            "jetson-agx-orin-64gb",
            "jetson-agx-orin-32gb",
            "jetson-orin-nx-16gb",
            "jetson-orin-nx-8gb",
            "jetson-orin-nano-8gb",
            "jetson-orin-nano-4gb",
        ]
        | NotGiven = NOT_GIVEN,
        args: dict[str, Any] | None | NotGiven = NOT_GIVEN,
    ) -> ExportsCreateResponse:
        """Export model to a new format.

        Converts a trained model to a different format for deployment (ONNX, TensorRT, CoreML, LiteRT, etc.).

        Args:
            model_id (str): Model ID to export
            format (Literal["onnx", "torchscript", "openvino", "engine", "coreml", "litert", "pb", "saved_model", "paddle", "ncnn", "edgetpu", "mnn", "rknn", "qnn", "imx", "axelera", "executorch", "deepx", "hailo", "ascend"]): Target export format
            gpu_type (Literal["rtx-2000-ada", "rtx-a4500", "rtx-a5000", "rtx-4000-ada", "l4", "a40", "rtx-3090", "rtx-a6000", "rtx-pro-4000", "rtx-pro-4500", "rtx-4090", "rtx-6000-ada", "l40s", "rtx-pro-5000", "rtx-5090", "l40", "a100-80gb-pcie", "a100-80gb-sxm", "rtx-pro-6000", "h100-pcie", "h100-nvl", "h100-sxm", "h200-nvl", "h200-sxm", "b200", "b300", "jetson-thor-t5000", "jetson-thor-t4000", "jetson-agx-orin-64gb", "jetson-agx-orin-32gb", "jetson-orin-nx-16gb", "jetson-orin-nx-8gb", "jetson-orin-nano-8gb", "jetson-orin-nano-4gb"], optional): Target GPU type for TensorRT exports
            args (dict[str, Any] | None, optional): Additional export options

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
            export_id (str): Export ID

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
            export_id (str): Export ID

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


class AsyncExports:
    """Asynchronous Exports API operations."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(
        self,
        *,
        model_id: str,
        status: Literal["queued", "starting", "running", "completed", "failed", "cancelled"] | None = None,
        limit: float | None = None,
    ) -> ExportsListResponse:
        """List model exports.

        Returns export jobs for a model, including status and download URLs for completed exports.

        Args:
            model_id (str): Model ID
            status (Literal["queued", "starting", "running", "completed", "failed", "cancelled"], optional): Export status filter
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
        format: Literal[
            "onnx",
            "torchscript",
            "openvino",
            "engine",
            "coreml",
            "litert",
            "pb",
            "saved_model",
            "paddle",
            "ncnn",
            "edgetpu",
            "mnn",
            "rknn",
            "qnn",
            "imx",
            "axelera",
            "executorch",
            "deepx",
            "hailo",
            "ascend",
        ],
        gpu_type: Literal[
            "rtx-2000-ada",
            "rtx-a4500",
            "rtx-a5000",
            "rtx-4000-ada",
            "l4",
            "a40",
            "rtx-3090",
            "rtx-a6000",
            "rtx-pro-4000",
            "rtx-pro-4500",
            "rtx-4090",
            "rtx-6000-ada",
            "l40s",
            "rtx-pro-5000",
            "rtx-5090",
            "l40",
            "a100-80gb-pcie",
            "a100-80gb-sxm",
            "rtx-pro-6000",
            "h100-pcie",
            "h100-nvl",
            "h100-sxm",
            "h200-nvl",
            "h200-sxm",
            "b200",
            "b300",
            "jetson-thor-t5000",
            "jetson-thor-t4000",
            "jetson-agx-orin-64gb",
            "jetson-agx-orin-32gb",
            "jetson-orin-nx-16gb",
            "jetson-orin-nx-8gb",
            "jetson-orin-nano-8gb",
            "jetson-orin-nano-4gb",
        ]
        | NotGiven = NOT_GIVEN,
        args: dict[str, Any] | None | NotGiven = NOT_GIVEN,
    ) -> ExportsCreateResponse:
        """Export model to a new format.

        Converts a trained model to a different format for deployment (ONNX, TensorRT, CoreML, LiteRT, etc.).

        Args:
            model_id (str): Model ID to export
            format (Literal["onnx", "torchscript", "openvino", "engine", "coreml", "litert", "pb", "saved_model", "paddle", "ncnn", "edgetpu", "mnn", "rknn", "qnn", "imx", "axelera", "executorch", "deepx", "hailo", "ascend"]): Target export format
            gpu_type (Literal["rtx-2000-ada", "rtx-a4500", "rtx-a5000", "rtx-4000-ada", "l4", "a40", "rtx-3090", "rtx-a6000", "rtx-pro-4000", "rtx-pro-4500", "rtx-4090", "rtx-6000-ada", "l40s", "rtx-pro-5000", "rtx-5090", "l40", "a100-80gb-pcie", "a100-80gb-sxm", "rtx-pro-6000", "h100-pcie", "h100-nvl", "h100-sxm", "h200-nvl", "h200-sxm", "b200", "b300", "jetson-thor-t5000", "jetson-thor-t4000", "jetson-agx-orin-64gb", "jetson-agx-orin-32gb", "jetson-orin-nx-16gb", "jetson-orin-nx-8gb", "jetson-orin-nano-8gb", "jetson-orin-nano-4gb"], optional): Target GPU type for TensorRT exports
            args (dict[str, Any] | None, optional): Additional export options

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
            export_id (str): Export ID

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
            export_id (str): Export ID

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
