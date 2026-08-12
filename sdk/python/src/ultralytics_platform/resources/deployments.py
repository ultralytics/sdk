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
    DeploymentsCreateResponse,
    DeploymentsDeleteResponse,
    DeploymentsListResponse,
    DeploymentsPredictResponse,
    DeploymentsRetrieveHealthResponse,
    DeploymentsRetrieveLogsResponse,
    DeploymentsRetrieveMetricsResponse,
    DeploymentsRetrieveResponse,
    DeploymentsUpdateResponse,
)


class Deployments:
    """Deployments API operations."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def retrieve(self, owner: str, deployment: str) -> DeploymentsRetrieveResponse:
        """Get deployment details.

        Returns deployment configuration, status, and service URL.

        Args:
            owner (str): Deployment owner
            deployment (str): Deployment name

        Returns:
            (DeploymentsRetrieveResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsRetrieveResponse,
            self._client.request(
                "GET",
                f"/api/deployments/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(deployment, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
            ),
        )

    def update(self, owner: str, deployment: str, *, body: dict[str, Any]) -> DeploymentsUpdateResponse:
        """Update a deployment.

        Starts, stops, or rolls out another model while preserving the endpoint URL.

        Args:
            owner (str): Deployment owner
            deployment (str): Deployment name
            body (dict[str, Any]): API request for updating a deployment

        Returns:
            (DeploymentsUpdateResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsUpdateResponse,
            self._client.request(
                "PATCH",
                f"/api/deployments/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(deployment, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
                json=body,
            ),
        )

    def delete(self, owner: str, deployment: str) -> DeploymentsDeleteResponse:
        """Delete a deployment.

        Permanently removes the inference endpoint.

        Args:
            owner (str): Deployment owner
            deployment (str): Deployment name

        Returns:
            (DeploymentsDeleteResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsDeleteResponse,
            self._client.request(
                "DELETE",
                f"/api/deployments/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(deployment, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
            ),
        )

    def retrieve_health(self, owner: str, deployment: str) -> DeploymentsRetrieveHealthResponse:
        """Check deployment health.

        Pings and warms the deployment endpoint.

        Args:
            owner (str): Deployment owner
            deployment (str): Deployment name

        Returns:
            (DeploymentsRetrieveHealthResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsRetrieveHealthResponse,
            self._client.request(
                "GET",
                f"/api/deployments/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(deployment, explode=False, allow_reserved=False)}/health",
                auth=("Authorization", "Bearer "),
            ),
        )

    def retrieve_logs(
        self,
        owner: str,
        deployment: str,
        *,
        severity: str | None = None,
        limit: int | None = None,
        page_token: str | None = None,
    ) -> DeploymentsRetrieveLogsResponse:
        """Get deployment logs.

        Returns recent deployment service logs.

        Args:
            owner (str): Deployment owner
            deployment (str): Deployment name
            severity (str, optional): Comma-separated log severity levels
            limit (int, optional): Maximum log entries to return
            page_token (str, optional): Pagination token

        Returns:
            (DeploymentsRetrieveLogsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsRetrieveLogsResponse,
            self._client.request(
                "GET",
                f"/api/deployments/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(deployment, explode=False, allow_reserved=False)}/logs",
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("severity", severity, style="form", explode=True),
                    *_query_parameter("limit", limit, style="form", explode=True),
                    *_query_parameter("pageToken", page_token, style="form", explode=True),
                ],
            ),
        )

    def retrieve_metrics(
        self,
        owner: str,
        deployment: str,
        *,
        range: Literal["1h", "6h", "24h", "7d", "30d"] | None = None,
        sparkline: Literal["true", "false"] | None = None,
    ) -> DeploymentsRetrieveMetricsResponse:
        """Get deployment metrics.

        Returns request volume, latency, errors, and resource utilization.

        Args:
            owner (str): Deployment owner
            deployment (str): Deployment name
            range (Literal["1h", "6h", "24h", "7d", "30d"], optional): Metrics time range
            sparkline (Literal["true", "false"], optional): Return the compact dashboard summary

        Returns:
            (DeploymentsRetrieveMetricsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsRetrieveMetricsResponse,
            self._client.request(
                "GET",
                f"/api/deployments/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(deployment, explode=False, allow_reserved=False)}/metrics",
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("range", range, style="form", explode=True),
                    *_query_parameter("sparkline", sparkline, style="form", explode=True),
                ],
            ),
        )

    def predict(self, owner: str, deployment: str, *, body: dict[str, Any]) -> DeploymentsPredictResponse:
        """Run deployment inference.

        Runs inference through a dedicated deployment endpoint.

        Args:
            owner (str): Deployment owner
            deployment (str): Deployment name
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
                f"/api/deployments/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(deployment, explode=False, allow_reserved=False)}/predict",
                auth=("Authorization", "Bearer "),
                data={key: value for key, value in body.items() if key not in ["file"]},
                files={key: body[key] for key in ["file"] if key in body},
            ),
        )

    def list(
        self,
        owner: str,
        *,
        status: Literal["creating", "deploying", "ready", "stopping", "stopped", "failed"] | None = None,
        model: str | None = None,
        limit: int | None = None,
    ) -> DeploymentsListResponse:
        """List deployments.

        Returns workspace inference endpoints. Anonymous callers must filter by one public model; workspace-wide listing requires authentication.

        Args:
            owner (str): Deployment owner
            status (Literal["creating", "deploying", "ready", "stopping", "stopped", "failed"], optional): Deployment status filter
            model (str, optional): Project and model names separated by a slash
            limit (int, optional): Maximum deployments to return

        Returns:
            (DeploymentsListResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsListResponse,
            self._client.request(
                "GET",
                f"/api/deployments/{_path_parameter(owner, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("status", status, style="form", explode=True),
                    *_query_parameter("model", model, style="form", explode=True),
                    *_query_parameter("limit", limit, style="form", explode=True),
                ],
            ),
        )

    def create(
        self,
        owner: str,
        *,
        project: str,
        model: str,
        deployment: str,
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

        Creates a dedicated auto-scaling inference endpoint for a model.

        Args:
            owner (str): Deployment owner
            project (str): Project name
            model (str): Model name
            deployment (str): Deployment name
            name (str): name request value.
            region (Literal["asia-east1", "asia-northeast1", "asia-northeast2", "asia-south1", "asia-southeast3", "europe-north1", "europe-north2", "europe-southwest1", "europe-west1", "europe-west4", "europe-west8", "europe-west9", "me-west1", "northamerica-south1", "us-central1", "us-east1", "us-east4", "us-east5", "us-south1", "us-west1", "africa-south1", "asia-east2", "asia-northeast3", "asia-southeast1", "asia-southeast2", "asia-south2", "australia-southeast1", "australia-southeast2", "europe-central2", "europe-west10", "europe-west12", "europe-west2", "europe-west3", "europe-west6", "me-central1", "northamerica-northeast1", "northamerica-northeast2", "southamerica-east1", "southamerica-west1", "us-west2", "us-west3", "us-west4"]): region request value.

        Returns:
            (DeploymentsCreateResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsCreateResponse,
            self._client.request(
                "POST",
                f"/api/deployments/{_path_parameter(owner, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
                json={"project": project, "model": model, "deployment": deployment, "name": name, "region": region},
            ),
        )


class AsyncDeployments:
    """Asynchronous Deployments API operations."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def retrieve(self, owner: str, deployment: str) -> DeploymentsRetrieveResponse:
        """Get deployment details.

        Returns deployment configuration, status, and service URL.

        Args:
            owner (str): Deployment owner
            deployment (str): Deployment name

        Returns:
            (DeploymentsRetrieveResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsRetrieveResponse,
            await self._client.request(
                "GET",
                f"/api/deployments/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(deployment, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
            ),
        )

    async def update(self, owner: str, deployment: str, *, body: dict[str, Any]) -> DeploymentsUpdateResponse:
        """Update a deployment.

        Starts, stops, or rolls out another model while preserving the endpoint URL.

        Args:
            owner (str): Deployment owner
            deployment (str): Deployment name
            body (dict[str, Any]): API request for updating a deployment

        Returns:
            (DeploymentsUpdateResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsUpdateResponse,
            await self._client.request(
                "PATCH",
                f"/api/deployments/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(deployment, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
                json=body,
            ),
        )

    async def delete(self, owner: str, deployment: str) -> DeploymentsDeleteResponse:
        """Delete a deployment.

        Permanently removes the inference endpoint.

        Args:
            owner (str): Deployment owner
            deployment (str): Deployment name

        Returns:
            (DeploymentsDeleteResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsDeleteResponse,
            await self._client.request(
                "DELETE",
                f"/api/deployments/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(deployment, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
            ),
        )

    async def retrieve_health(self, owner: str, deployment: str) -> DeploymentsRetrieveHealthResponse:
        """Check deployment health.

        Pings and warms the deployment endpoint.

        Args:
            owner (str): Deployment owner
            deployment (str): Deployment name

        Returns:
            (DeploymentsRetrieveHealthResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsRetrieveHealthResponse,
            await self._client.request(
                "GET",
                f"/api/deployments/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(deployment, explode=False, allow_reserved=False)}/health",
                auth=("Authorization", "Bearer "),
            ),
        )

    async def retrieve_logs(
        self,
        owner: str,
        deployment: str,
        *,
        severity: str | None = None,
        limit: int | None = None,
        page_token: str | None = None,
    ) -> DeploymentsRetrieveLogsResponse:
        """Get deployment logs.

        Returns recent deployment service logs.

        Args:
            owner (str): Deployment owner
            deployment (str): Deployment name
            severity (str, optional): Comma-separated log severity levels
            limit (int, optional): Maximum log entries to return
            page_token (str, optional): Pagination token

        Returns:
            (DeploymentsRetrieveLogsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsRetrieveLogsResponse,
            await self._client.request(
                "GET",
                f"/api/deployments/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(deployment, explode=False, allow_reserved=False)}/logs",
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("severity", severity, style="form", explode=True),
                    *_query_parameter("limit", limit, style="form", explode=True),
                    *_query_parameter("pageToken", page_token, style="form", explode=True),
                ],
            ),
        )

    async def retrieve_metrics(
        self,
        owner: str,
        deployment: str,
        *,
        range: Literal["1h", "6h", "24h", "7d", "30d"] | None = None,
        sparkline: Literal["true", "false"] | None = None,
    ) -> DeploymentsRetrieveMetricsResponse:
        """Get deployment metrics.

        Returns request volume, latency, errors, and resource utilization.

        Args:
            owner (str): Deployment owner
            deployment (str): Deployment name
            range (Literal["1h", "6h", "24h", "7d", "30d"], optional): Metrics time range
            sparkline (Literal["true", "false"], optional): Return the compact dashboard summary

        Returns:
            (DeploymentsRetrieveMetricsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsRetrieveMetricsResponse,
            await self._client.request(
                "GET",
                f"/api/deployments/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(deployment, explode=False, allow_reserved=False)}/metrics",
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("range", range, style="form", explode=True),
                    *_query_parameter("sparkline", sparkline, style="form", explode=True),
                ],
            ),
        )

    async def predict(self, owner: str, deployment: str, *, body: dict[str, Any]) -> DeploymentsPredictResponse:
        """Run deployment inference.

        Runs inference through a dedicated deployment endpoint.

        Args:
            owner (str): Deployment owner
            deployment (str): Deployment name
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
                f"/api/deployments/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(deployment, explode=False, allow_reserved=False)}/predict",
                auth=("Authorization", "Bearer "),
                data={key: value for key, value in body.items() if key not in ["file"]},
                files={key: body[key] for key in ["file"] if key in body},
            ),
        )

    async def list(
        self,
        owner: str,
        *,
        status: Literal["creating", "deploying", "ready", "stopping", "stopped", "failed"] | None = None,
        model: str | None = None,
        limit: int | None = None,
    ) -> DeploymentsListResponse:
        """List deployments.

        Returns workspace inference endpoints. Anonymous callers must filter by one public model; workspace-wide listing requires authentication.

        Args:
            owner (str): Deployment owner
            status (Literal["creating", "deploying", "ready", "stopping", "stopped", "failed"], optional): Deployment status filter
            model (str, optional): Project and model names separated by a slash
            limit (int, optional): Maximum deployments to return

        Returns:
            (DeploymentsListResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsListResponse,
            await self._client.request(
                "GET",
                f"/api/deployments/{_path_parameter(owner, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("status", status, style="form", explode=True),
                    *_query_parameter("model", model, style="form", explode=True),
                    *_query_parameter("limit", limit, style="form", explode=True),
                ],
            ),
        )

    async def create(
        self,
        owner: str,
        *,
        project: str,
        model: str,
        deployment: str,
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

        Creates a dedicated auto-scaling inference endpoint for a model.

        Args:
            owner (str): Deployment owner
            project (str): Project name
            model (str): Model name
            deployment (str): Deployment name
            name (str): name request value.
            region (Literal["asia-east1", "asia-northeast1", "asia-northeast2", "asia-south1", "asia-southeast3", "europe-north1", "europe-north2", "europe-southwest1", "europe-west1", "europe-west4", "europe-west8", "europe-west9", "me-west1", "northamerica-south1", "us-central1", "us-east1", "us-east4", "us-east5", "us-south1", "us-west1", "africa-south1", "asia-east2", "asia-northeast3", "asia-southeast1", "asia-southeast2", "asia-south2", "australia-southeast1", "australia-southeast2", "europe-central2", "europe-west10", "europe-west12", "europe-west2", "europe-west3", "europe-west6", "me-central1", "northamerica-northeast1", "northamerica-northeast2", "southamerica-east1", "southamerica-west1", "us-west2", "us-west3", "us-west4"]): region request value.

        Returns:
            (DeploymentsCreateResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsCreateResponse,
            await self._client.request(
                "POST",
                f"/api/deployments/{_path_parameter(owner, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
                json={"project": project, "model": model, "deployment": deployment, "name": name, "region": region},
            ),
        )
