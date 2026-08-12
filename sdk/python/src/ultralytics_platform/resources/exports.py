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
    ExportsCancelOrDeleteResponse,
    ExportsExportModelResponse,
    ExportsListModelResponse,
    ExportsRetrieveStatusResponse,
)


class Exports:
    """Exports API operations."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def retrieve_status(self, owner: str, project: str, model: str, export_id: str) -> ExportsRetrieveStatusResponse:
        """Get export status.

        Returns one export, including a download URL when complete.

        Args:
            owner (str): Project owner
            project (str): Project name
            model (str): Model name
            export_id (str): Export ID

        Returns:
            (ExportsRetrieveStatusResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ExportsRetrieveStatusResponse,
            self._client.request(
                "GET",
                f"/api/models/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}/{_path_parameter(model, explode=False, allow_reserved=False)}/exports/{_path_parameter(export_id, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
            ),
        )

    def cancel_or_delete(self, owner: str, project: str, model: str, export_id: str) -> ExportsCancelOrDeleteResponse:
        """Cancel or delete an export.

        Cancels an active export or deletes a finished export and its file.

        Args:
            owner (str): Project owner
            project (str): Project name
            model (str): Model name
            export_id (str): Export ID

        Returns:
            (ExportsCancelOrDeleteResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ExportsCancelOrDeleteResponse,
            self._client.request(
                "DELETE",
                f"/api/models/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}/{_path_parameter(model, explode=False, allow_reserved=False)}/exports/{_path_parameter(export_id, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
            ),
        )

    def list_model(
        self,
        owner: str,
        project: str,
        model: str,
        *,
        status: Literal["queued", "starting", "running", "completed", "failed", "cancelled"] | None = None,
        limit: int | None = None,
    ) -> ExportsListModelResponse:
        """List model exports.

        Returns export jobs for a model, including download URLs for completed exports.

        Args:
            owner (str): Project owner
            project (str): Project name
            model (str): Model name
            status (Literal["queued", "starting", "running", "completed", "failed", "cancelled"], optional): Export status filter
            limit (int, optional): Maximum exports to return

        Returns:
            (ExportsListModelResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ExportsListModelResponse,
            self._client.request(
                "GET",
                f"/api/models/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}/{_path_parameter(model, explode=False, allow_reserved=False)}/exports",
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("status", status, style="form", explode=True),
                    *_query_parameter("limit", limit, style="form", explode=True),
                ],
            ),
        )

    def export_model(
        self,
        owner: str,
        project: str,
        model: str,
        *,
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
    ) -> ExportsExportModelResponse:
        """Export a model.

        Converts a trained model to another deployment format.

        Args:
            owner (str): Project owner
            project (str): Project name
            model (str): Model name
            format (Literal["onnx", "torchscript", "openvino", "engine", "coreml", "litert", "pb", "saved_model", "paddle", "ncnn", "edgetpu", "mnn", "rknn", "qnn", "imx", "axelera", "executorch", "deepx", "hailo", "ascend"]): Target export format
            gpu_type (Literal["rtx-2000-ada", "rtx-a4500", "rtx-a5000", "rtx-4000-ada", "l4", "a40", "rtx-3090", "rtx-a6000", "rtx-pro-4000", "rtx-pro-4500", "rtx-4090", "rtx-6000-ada", "l40s", "rtx-pro-5000", "rtx-5090", "l40", "a100-80gb-pcie", "a100-80gb-sxm", "rtx-pro-6000", "h100-pcie", "h100-nvl", "h100-sxm", "h200-nvl", "h200-sxm", "b200", "b300", "jetson-thor-t5000", "jetson-thor-t4000", "jetson-agx-orin-64gb", "jetson-agx-orin-32gb", "jetson-orin-nx-16gb", "jetson-orin-nx-8gb", "jetson-orin-nano-8gb", "jetson-orin-nano-4gb"], optional): Target GPU type for TensorRT exports
            args (dict[str, Any] | None, optional): Additional export options

        Returns:
            (ExportsExportModelResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ExportsExportModelResponse,
            self._client.request(
                "POST",
                f"/api/models/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}/{_path_parameter(model, explode=False, allow_reserved=False)}/exports",
                auth=("Authorization", "Bearer "),
                json={"format": format, "gpuType": gpu_type, "args": args},
            ),
        )


class AsyncExports:
    """Asynchronous Exports API operations."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def retrieve_status(
        self, owner: str, project: str, model: str, export_id: str
    ) -> ExportsRetrieveStatusResponse:
        """Get export status.

        Returns one export, including a download URL when complete.

        Args:
            owner (str): Project owner
            project (str): Project name
            model (str): Model name
            export_id (str): Export ID

        Returns:
            (ExportsRetrieveStatusResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ExportsRetrieveStatusResponse,
            await self._client.request(
                "GET",
                f"/api/models/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}/{_path_parameter(model, explode=False, allow_reserved=False)}/exports/{_path_parameter(export_id, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
            ),
        )

    async def cancel_or_delete(
        self, owner: str, project: str, model: str, export_id: str
    ) -> ExportsCancelOrDeleteResponse:
        """Cancel or delete an export.

        Cancels an active export or deletes a finished export and its file.

        Args:
            owner (str): Project owner
            project (str): Project name
            model (str): Model name
            export_id (str): Export ID

        Returns:
            (ExportsCancelOrDeleteResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ExportsCancelOrDeleteResponse,
            await self._client.request(
                "DELETE",
                f"/api/models/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}/{_path_parameter(model, explode=False, allow_reserved=False)}/exports/{_path_parameter(export_id, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
            ),
        )

    async def list_model(
        self,
        owner: str,
        project: str,
        model: str,
        *,
        status: Literal["queued", "starting", "running", "completed", "failed", "cancelled"] | None = None,
        limit: int | None = None,
    ) -> ExportsListModelResponse:
        """List model exports.

        Returns export jobs for a model, including download URLs for completed exports.

        Args:
            owner (str): Project owner
            project (str): Project name
            model (str): Model name
            status (Literal["queued", "starting", "running", "completed", "failed", "cancelled"], optional): Export status filter
            limit (int, optional): Maximum exports to return

        Returns:
            (ExportsListModelResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ExportsListModelResponse,
            await self._client.request(
                "GET",
                f"/api/models/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}/{_path_parameter(model, explode=False, allow_reserved=False)}/exports",
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("status", status, style="form", explode=True),
                    *_query_parameter("limit", limit, style="form", explode=True),
                ],
            ),
        )

    async def export_model(
        self,
        owner: str,
        project: str,
        model: str,
        *,
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
    ) -> ExportsExportModelResponse:
        """Export a model.

        Converts a trained model to another deployment format.

        Args:
            owner (str): Project owner
            project (str): Project name
            model (str): Model name
            format (Literal["onnx", "torchscript", "openvino", "engine", "coreml", "litert", "pb", "saved_model", "paddle", "ncnn", "edgetpu", "mnn", "rknn", "qnn", "imx", "axelera", "executorch", "deepx", "hailo", "ascend"]): Target export format
            gpu_type (Literal["rtx-2000-ada", "rtx-a4500", "rtx-a5000", "rtx-4000-ada", "l4", "a40", "rtx-3090", "rtx-a6000", "rtx-pro-4000", "rtx-pro-4500", "rtx-4090", "rtx-6000-ada", "l40s", "rtx-pro-5000", "rtx-5090", "l40", "a100-80gb-pcie", "a100-80gb-sxm", "rtx-pro-6000", "h100-pcie", "h100-nvl", "h100-sxm", "h200-nvl", "h200-sxm", "b200", "b300", "jetson-thor-t5000", "jetson-thor-t4000", "jetson-agx-orin-64gb", "jetson-agx-orin-32gb", "jetson-orin-nx-16gb", "jetson-orin-nx-8gb", "jetson-orin-nano-8gb", "jetson-orin-nano-4gb"], optional): Target GPU type for TensorRT exports
            args (dict[str, Any] | None, optional): Additional export options

        Returns:
            (ExportsExportModelResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ExportsExportModelResponse,
            await self._client.request(
                "POST",
                f"/api/models/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}/{_path_parameter(model, explode=False, allow_reserved=False)}/exports",
                auth=("Authorization", "Bearer "),
                json={"format": format, "gpuType": gpu_type, "args": args},
            ),
        )
