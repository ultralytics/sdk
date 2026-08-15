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
    TrainingGpuAvailabilityResponse,
    TrainingStartResponse,
)


class Training:
    """Training API operations."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def gpu_availability(
        self,
        *,
        managed: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> TrainingGpuAvailabilityResponse:
        """Get GPU availability.

        Returns current cloud training capacity for each supported GPU type. Basic queries are public; `managed=true` additionally probes Ultralytics managed capacity and requires authentication.

        Args:
            managed (Literal["true", "false"], optional): Include managed training capacity
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (TrainingGpuAvailabilityResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            TrainingGpuAvailabilityResponse,
            self._client.request(
                "GET",
                "/api/training/gpu-availability",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("managed", managed, style="form", explode=True)],
            ),
        )

    def start(
        self,
        *,
        model_id: str,
        train_args: dict[str, Any],
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
        ]
        | NotGiven = NOT_GIVEN,
        capture_dataset_version: bool | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> TrainingStartResponse:
        """Start cloud training.

        Launches YOLO training on a cloud GPU. Training costs are deducted from your credit balance based on GPU type and duration.

        Args:
            model_id (str): Model ID to train
            gpu_type (Literal["rtx-2000-ada", "rtx-a4500", "rtx-a5000", "rtx-4000-ada", "l4", "a40", "rtx-3090", "rtx-a6000", "rtx-pro-4000", "rtx-pro-4500", "rtx-4090", "rtx-6000-ada", "l40s", "rtx-pro-5000", "rtx-5090", "l40", "a100-80gb-pcie", "a100-80gb-sxm", "rtx-pro-6000", "h100-pcie", "h100-nvl", "h100-sxm", "h200-nvl", "h200-sxm", "b200", "b300"], optional): Cloud GPU to use
            capture_dataset_version (bool, optional): Save an immutable dataset version for this run
            train_args (dict[str, Any]): YOLO training arguments
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (TrainingStartResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            TrainingStartResponse,
            self._client.request(
                "POST",
                "/api/training/start",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={
                    "modelId": model_id,
                    "gpuType": gpu_type,
                    "captureDatasetVersion": capture_dataset_version,
                    "trainArgs": train_args,
                },
            ),
        )


class AsyncTraining:
    """Asynchronous Training API operations."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def gpu_availability(
        self,
        *,
        managed: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> TrainingGpuAvailabilityResponse:
        """Get GPU availability.

        Returns current cloud training capacity for each supported GPU type. Basic queries are public; `managed=true` additionally probes Ultralytics managed capacity and requires authentication.

        Args:
            managed (Literal["true", "false"], optional): Include managed training capacity
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (TrainingGpuAvailabilityResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            TrainingGpuAvailabilityResponse,
            await self._client.request(
                "GET",
                "/api/training/gpu-availability",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("managed", managed, style="form", explode=True)],
            ),
        )

    async def start(
        self,
        *,
        model_id: str,
        train_args: dict[str, Any],
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
        ]
        | NotGiven = NOT_GIVEN,
        capture_dataset_version: bool | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> TrainingStartResponse:
        """Start cloud training.

        Launches YOLO training on a cloud GPU. Training costs are deducted from your credit balance based on GPU type and duration.

        Args:
            model_id (str): Model ID to train
            gpu_type (Literal["rtx-2000-ada", "rtx-a4500", "rtx-a5000", "rtx-4000-ada", "l4", "a40", "rtx-3090", "rtx-a6000", "rtx-pro-4000", "rtx-pro-4500", "rtx-4090", "rtx-6000-ada", "l40s", "rtx-pro-5000", "rtx-5090", "l40", "a100-80gb-pcie", "a100-80gb-sxm", "rtx-pro-6000", "h100-pcie", "h100-nvl", "h100-sxm", "h200-nvl", "h200-sxm", "b200", "b300"], optional): Cloud GPU to use
            capture_dataset_version (bool, optional): Save an immutable dataset version for this run
            train_args (dict[str, Any]): YOLO training arguments
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (TrainingStartResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            TrainingStartResponse,
            await self._client.request(
                "POST",
                "/api/training/start",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={
                    "modelId": model_id,
                    "gpuType": gpu_type,
                    "captureDatasetVersion": capture_dataset_version,
                    "trainArgs": train_args,
                },
            ),
        )
