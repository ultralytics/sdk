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
    DeploymentsCreateResponse,
    DeploymentsDeleteResponse,
    DeploymentsListResponse,
    DeploymentsPredictResponse,
    DeploymentsRetrieveHealthResponse,
    DeploymentsRetrieveLogsResponse,
    DeploymentsRetrieveMetricsResponse,
    DeploymentsRetrieveResponse,
    DeploymentsStartResponse,
    DeploymentsStopResponse,
    DeploymentsUpdateResponse,
)


class Deployments:
    """Deployments API operations."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(
        self,
        *,
        model_id: str | None = None,
        status: Literal["creating", "ready", "stopped", "failed"] | None = None,
        limit: float | None = None,
    ) -> DeploymentsListResponse:
        """List your deployments.

        Returns your deployed inference endpoints.

        Args:
            model_id (str, optional): Filter by model ID
            status (Literal["creating", "ready", "stopped", "failed"], optional): Deployment status filter
            limit (float, optional): Number of results to return (default 20, max 100)

        Returns:
            (DeploymentsListResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsListResponse,
            self._client.request(
                "GET",
                "/api/deployments",
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
        name: str,
        region: Literal[
            "asia-east1",
            "asia-northeast1",
            "asia-northeast2",
            "asia-south1",
            "asia-southeast3",
            "europe-north1",
            "europe-north2",
            "europe-southwest1",
            "europe-west1",
            "europe-west4",
            "europe-west8",
            "europe-west9",
            "me-west1",
            "northamerica-south1",
            "us-central1",
            "us-east1",
            "us-east4",
            "us-east5",
            "us-south1",
            "us-west1",
            "africa-south1",
            "asia-east2",
            "asia-northeast3",
            "asia-southeast1",
            "asia-southeast2",
            "asia-south2",
            "australia-southeast1",
            "australia-southeast2",
            "europe-central2",
            "europe-west10",
            "europe-west12",
            "europe-west2",
            "europe-west3",
            "europe-west6",
            "me-central1",
            "northamerica-northeast1",
            "northamerica-northeast2",
            "southamerica-east1",
            "southamerica-west1",
            "us-west2",
            "us-west3",
            "us-west4",
        ],
    ) -> DeploymentsCreateResponse:
        """Deploy a model.

        Creates a dedicated inference endpoint for a model. The endpoint runs on Google Cloud and scales automatically.

        Args:
            model_id (str): Model ID
            name (str): Resource name
            region (Literal["asia-east1", "asia-northeast1", "asia-northeast2", "asia-south1", "asia-southeast3", "europe-north1", "europe-north2", "europe-southwest1", "europe-west1", "europe-west4", "europe-west8", "europe-west9", "me-west1", "northamerica-south1", "us-central1", "us-east1", "us-east4", "us-east5", "us-south1", "us-west1", "africa-south1", "asia-east2", "asia-northeast3", "asia-southeast1", "asia-southeast2", "asia-south2", "australia-southeast1", "australia-southeast2", "europe-central2", "europe-west10", "europe-west12", "europe-west2", "europe-west3", "europe-west6", "me-central1", "northamerica-northeast1", "northamerica-northeast2", "southamerica-east1", "southamerica-west1", "us-west2", "us-west3", "us-west4"]): Cloud region

        Returns:
            (DeploymentsCreateResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsCreateResponse,
            self._client.request(
                "POST",
                "/api/deployments",
                auth=("Authorization", "Bearer "),
                json={"modelId": model_id, "name": name, "region": region},
            ),
        )

    def retrieve(self, deployment_id: str) -> DeploymentsRetrieveResponse:
        """Get deployment details.

        Returns deployment configuration, status, and service URL.

        Args:
            deployment_id (str): Deployment ID

        Returns:
            (DeploymentsRetrieveResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsRetrieveResponse,
            self._client.request(
                "GET",
                f"/api/deployments/{_path_parameter(deployment_id, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
            ),
        )

    def update(
        self, deployment_id: str, *, model_id: str, name: str | NotGiven = NOT_GIVEN
    ) -> DeploymentsUpdateResponse:
        """Replace a deployment model.

        Rolls out a new model revision while preserving the deployment ID, region, API key, and endpoint URL. An optional name is applied when the replacement becomes ready. The current revision continues serving until then.

        Args:
            deployment_id (str): Deployment ID
            model_id (str): Model ID
            name (str, optional): Optional new deployment display name

        Returns:
            (DeploymentsUpdateResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsUpdateResponse,
            self._client.request(
                "PATCH",
                f"/api/deployments/{_path_parameter(deployment_id, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
                json={"modelId": model_id, "name": name},
            ),
        )

    def delete(self, deployment_id: str) -> DeploymentsDeleteResponse:
        """Delete a deployment.

        Permanently stops and removes the inference endpoint. This cannot be undone.

        Args:
            deployment_id (str): Deployment ID

        Returns:
            (DeploymentsDeleteResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsDeleteResponse,
            self._client.request(
                "DELETE",
                f"/api/deployments/{_path_parameter(deployment_id, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
            ),
        )

    def predict(self, deployment_id: str, *, body: dict[str, Any]) -> DeploymentsPredictResponse:
        """Run inference on your endpoint.

        Send multipart/form-data with a file or source plus optional conf, iou, imgsz, normalize, and decimals fields to your dedicated deployment endpoint.

        Args:
            deployment_id (str): Deployment ID
            body (dict[str, Any]): Request body.

        Returns:
            (DeploymentsPredictResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsPredictResponse,
            self._client.request(
                "POST",
                f"/api/deployments/{_path_parameter(deployment_id, explode=False, allow_reserved=False)}/predict",
                auth=("Authorization", "Bearer "),
                data={key: value for key, value in body.items() if key not in ["file"]},
                files={key: body[key] for key in ["file"] if key in body},
            ),
        )

    def retrieve_health(self, deployment_id: str) -> DeploymentsRetrieveHealthResponse:
        """Check if endpoint is healthy.

        Pings the deployment endpoint and returns response time. Also warms up cold instances.

        Args:
            deployment_id (str): Deployment ID

        Returns:
            (DeploymentsRetrieveHealthResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsRetrieveHealthResponse,
            self._client.request(
                "GET",
                f"/api/deployments/{_path_parameter(deployment_id, explode=False, allow_reserved=False)}/health",
                auth=("Authorization", "Bearer "),
            ),
        )

    def retrieve_metrics(
        self,
        deployment_id: str,
        *,
        range: Literal["1h", "6h", "24h", "7d", "30d"] | None = None,
        sparkline: bool | None = None,
    ) -> DeploymentsRetrieveMetricsResponse:
        """Get endpoint performance metrics.

        Returns request volume, latency percentiles, error rates, and resource utilization over time.

        Args:
            deployment_id (str): Deployment ID
            range (Literal["1h", "6h", "24h", "7d", "30d"], optional): Time window (default: 24h)
            sparkline (bool, optional): Return the compact 24-hour dashboard summary

        Returns:
            (DeploymentsRetrieveMetricsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsRetrieveMetricsResponse,
            self._client.request(
                "GET",
                f"/api/deployments/{_path_parameter(deployment_id, explode=False, allow_reserved=False)}/metrics",
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("range", range, style="form", explode=True),
                    *_query_parameter("sparkline", sparkline, style="form", explode=True),
                ],
            ),
        )

    def retrieve_logs(
        self,
        deployment_id: str,
        *,
        severity: str | None = None,
        limit: float | None = None,
        page_token: str | None = None,
    ) -> DeploymentsRetrieveLogsResponse:
        """Get endpoint logs.

        Returns recent log entries from the deployment service for debugging.

        Args:
            deployment_id (str): Deployment ID
            severity (str, optional): Comma-separated levels: DEBUG, INFO, WARNING, ERROR, or CRITICAL
            limit (float, optional): Number of log entries (default 50, max 200)
            page_token (str, optional): Token for loading more entries

        Returns:
            (DeploymentsRetrieveLogsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsRetrieveLogsResponse,
            self._client.request(
                "GET",
                f"/api/deployments/{_path_parameter(deployment_id, explode=False, allow_reserved=False)}/logs",
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("severity", severity, style="form", explode=True),
                    *_query_parameter("limit", limit, style="form", explode=True),
                    *_query_parameter("pageToken", page_token, style="form", explode=True),
                ],
            ),
        )

    def start(self, deployment_id: str) -> DeploymentsStartResponse:
        """Start a stopped endpoint.

        Resumes a previously stopped deployment. Takes 1-2 minutes to become ready.

        Args:
            deployment_id (str): Deployment ID

        Returns:
            (DeploymentsStartResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsStartResponse,
            self._client.request(
                "POST",
                f"/api/deployments/{_path_parameter(deployment_id, explode=False, allow_reserved=False)}/start",
                auth=("Authorization", "Bearer "),
            ),
        )

    def stop(self, deployment_id: str) -> DeploymentsStopResponse:
        """Stop an endpoint.

        Stops the deployment to save costs. No charges while stopped. Can be restarted anytime.

        Args:
            deployment_id (str): Deployment ID

        Returns:
            (DeploymentsStopResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsStopResponse,
            self._client.request(
                "POST",
                f"/api/deployments/{_path_parameter(deployment_id, explode=False, allow_reserved=False)}/stop",
                auth=("Authorization", "Bearer "),
            ),
        )


class AsyncDeployments:
    """Asynchronous Deployments API operations."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(
        self,
        *,
        model_id: str | None = None,
        status: Literal["creating", "ready", "stopped", "failed"] | None = None,
        limit: float | None = None,
    ) -> DeploymentsListResponse:
        """List your deployments.

        Returns your deployed inference endpoints.

        Args:
            model_id (str, optional): Filter by model ID
            status (Literal["creating", "ready", "stopped", "failed"], optional): Deployment status filter
            limit (float, optional): Number of results to return (default 20, max 100)

        Returns:
            (DeploymentsListResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsListResponse,
            await self._client.request(
                "GET",
                "/api/deployments",
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
        name: str,
        region: Literal[
            "asia-east1",
            "asia-northeast1",
            "asia-northeast2",
            "asia-south1",
            "asia-southeast3",
            "europe-north1",
            "europe-north2",
            "europe-southwest1",
            "europe-west1",
            "europe-west4",
            "europe-west8",
            "europe-west9",
            "me-west1",
            "northamerica-south1",
            "us-central1",
            "us-east1",
            "us-east4",
            "us-east5",
            "us-south1",
            "us-west1",
            "africa-south1",
            "asia-east2",
            "asia-northeast3",
            "asia-southeast1",
            "asia-southeast2",
            "asia-south2",
            "australia-southeast1",
            "australia-southeast2",
            "europe-central2",
            "europe-west10",
            "europe-west12",
            "europe-west2",
            "europe-west3",
            "europe-west6",
            "me-central1",
            "northamerica-northeast1",
            "northamerica-northeast2",
            "southamerica-east1",
            "southamerica-west1",
            "us-west2",
            "us-west3",
            "us-west4",
        ],
    ) -> DeploymentsCreateResponse:
        """Deploy a model.

        Creates a dedicated inference endpoint for a model. The endpoint runs on Google Cloud and scales automatically.

        Args:
            model_id (str): Model ID
            name (str): Resource name
            region (Literal["asia-east1", "asia-northeast1", "asia-northeast2", "asia-south1", "asia-southeast3", "europe-north1", "europe-north2", "europe-southwest1", "europe-west1", "europe-west4", "europe-west8", "europe-west9", "me-west1", "northamerica-south1", "us-central1", "us-east1", "us-east4", "us-east5", "us-south1", "us-west1", "africa-south1", "asia-east2", "asia-northeast3", "asia-southeast1", "asia-southeast2", "asia-south2", "australia-southeast1", "australia-southeast2", "europe-central2", "europe-west10", "europe-west12", "europe-west2", "europe-west3", "europe-west6", "me-central1", "northamerica-northeast1", "northamerica-northeast2", "southamerica-east1", "southamerica-west1", "us-west2", "us-west3", "us-west4"]): Cloud region

        Returns:
            (DeploymentsCreateResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsCreateResponse,
            await self._client.request(
                "POST",
                "/api/deployments",
                auth=("Authorization", "Bearer "),
                json={"modelId": model_id, "name": name, "region": region},
            ),
        )

    async def retrieve(self, deployment_id: str) -> DeploymentsRetrieveResponse:
        """Get deployment details.

        Returns deployment configuration, status, and service URL.

        Args:
            deployment_id (str): Deployment ID

        Returns:
            (DeploymentsRetrieveResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsRetrieveResponse,
            await self._client.request(
                "GET",
                f"/api/deployments/{_path_parameter(deployment_id, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
            ),
        )

    async def update(
        self, deployment_id: str, *, model_id: str, name: str | NotGiven = NOT_GIVEN
    ) -> DeploymentsUpdateResponse:
        """Replace a deployment model.

        Rolls out a new model revision while preserving the deployment ID, region, API key, and endpoint URL. An optional name is applied when the replacement becomes ready. The current revision continues serving until then.

        Args:
            deployment_id (str): Deployment ID
            model_id (str): Model ID
            name (str, optional): Optional new deployment display name

        Returns:
            (DeploymentsUpdateResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsUpdateResponse,
            await self._client.request(
                "PATCH",
                f"/api/deployments/{_path_parameter(deployment_id, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
                json={"modelId": model_id, "name": name},
            ),
        )

    async def delete(self, deployment_id: str) -> DeploymentsDeleteResponse:
        """Delete a deployment.

        Permanently stops and removes the inference endpoint. This cannot be undone.

        Args:
            deployment_id (str): Deployment ID

        Returns:
            (DeploymentsDeleteResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsDeleteResponse,
            await self._client.request(
                "DELETE",
                f"/api/deployments/{_path_parameter(deployment_id, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
            ),
        )

    async def predict(self, deployment_id: str, *, body: dict[str, Any]) -> DeploymentsPredictResponse:
        """Run inference on your endpoint.

        Send multipart/form-data with a file or source plus optional conf, iou, imgsz, normalize, and decimals fields to your dedicated deployment endpoint.

        Args:
            deployment_id (str): Deployment ID
            body (dict[str, Any]): Request body.

        Returns:
            (DeploymentsPredictResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsPredictResponse,
            await self._client.request(
                "POST",
                f"/api/deployments/{_path_parameter(deployment_id, explode=False, allow_reserved=False)}/predict",
                auth=("Authorization", "Bearer "),
                data={key: value for key, value in body.items() if key not in ["file"]},
                files={key: body[key] for key in ["file"] if key in body},
            ),
        )

    async def retrieve_health(self, deployment_id: str) -> DeploymentsRetrieveHealthResponse:
        """Check if endpoint is healthy.

        Pings the deployment endpoint and returns response time. Also warms up cold instances.

        Args:
            deployment_id (str): Deployment ID

        Returns:
            (DeploymentsRetrieveHealthResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsRetrieveHealthResponse,
            await self._client.request(
                "GET",
                f"/api/deployments/{_path_parameter(deployment_id, explode=False, allow_reserved=False)}/health",
                auth=("Authorization", "Bearer "),
            ),
        )

    async def retrieve_metrics(
        self,
        deployment_id: str,
        *,
        range: Literal["1h", "6h", "24h", "7d", "30d"] | None = None,
        sparkline: bool | None = None,
    ) -> DeploymentsRetrieveMetricsResponse:
        """Get endpoint performance metrics.

        Returns request volume, latency percentiles, error rates, and resource utilization over time.

        Args:
            deployment_id (str): Deployment ID
            range (Literal["1h", "6h", "24h", "7d", "30d"], optional): Time window (default: 24h)
            sparkline (bool, optional): Return the compact 24-hour dashboard summary

        Returns:
            (DeploymentsRetrieveMetricsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsRetrieveMetricsResponse,
            await self._client.request(
                "GET",
                f"/api/deployments/{_path_parameter(deployment_id, explode=False, allow_reserved=False)}/metrics",
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("range", range, style="form", explode=True),
                    *_query_parameter("sparkline", sparkline, style="form", explode=True),
                ],
            ),
        )

    async def retrieve_logs(
        self,
        deployment_id: str,
        *,
        severity: str | None = None,
        limit: float | None = None,
        page_token: str | None = None,
    ) -> DeploymentsRetrieveLogsResponse:
        """Get endpoint logs.

        Returns recent log entries from the deployment service for debugging.

        Args:
            deployment_id (str): Deployment ID
            severity (str, optional): Comma-separated levels: DEBUG, INFO, WARNING, ERROR, or CRITICAL
            limit (float, optional): Number of log entries (default 50, max 200)
            page_token (str, optional): Token for loading more entries

        Returns:
            (DeploymentsRetrieveLogsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsRetrieveLogsResponse,
            await self._client.request(
                "GET",
                f"/api/deployments/{_path_parameter(deployment_id, explode=False, allow_reserved=False)}/logs",
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("severity", severity, style="form", explode=True),
                    *_query_parameter("limit", limit, style="form", explode=True),
                    *_query_parameter("pageToken", page_token, style="form", explode=True),
                ],
            ),
        )

    async def start(self, deployment_id: str) -> DeploymentsStartResponse:
        """Start a stopped endpoint.

        Resumes a previously stopped deployment. Takes 1-2 minutes to become ready.

        Args:
            deployment_id (str): Deployment ID

        Returns:
            (DeploymentsStartResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsStartResponse,
            await self._client.request(
                "POST",
                f"/api/deployments/{_path_parameter(deployment_id, explode=False, allow_reserved=False)}/start",
                auth=("Authorization", "Bearer "),
            ),
        )

    async def stop(self, deployment_id: str) -> DeploymentsStopResponse:
        """Stop an endpoint.

        Stops the deployment to save costs. No charges while stopped. Can be restarted anytime.

        Args:
            deployment_id (str): Deployment ID

        Returns:
            (DeploymentsStopResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsStopResponse,
            await self._client.request(
                "POST",
                f"/api/deployments/{_path_parameter(deployment_id, explode=False, allow_reserved=False)}/stop",
                auth=("Authorization", "Bearer "),
            ),
        )
