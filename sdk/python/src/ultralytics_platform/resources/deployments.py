# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from __future__ import annotations

from typing import Any, Literal, cast

import httpx

from .._client import (
    NOT_GIVEN,
    AsyncAPIClient,
    NotGiven,
    SyncAPIClient,
    _form_data,
    _path_parameter,
    _query_parameter,
)
from ..types import (
    DeploymentsCreateResponse,
    DeploymentsDeleteResponse,
    DeploymentsHealthResponse,
    DeploymentsListResponse,
    DeploymentsLogsResponse,
    DeploymentsMetricsResponse,
    DeploymentsPredictResponse,
    DeploymentsRetrieveResponse,
    DeploymentsUpdateResponse,
)


class Deployments:
    """Deployments API operations."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def retrieve(
        self,
        owner: str,
        deployment: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DeploymentsRetrieveResponse:
        """Get deployment details.

        Returns deployment configuration, status, and service URL.

        Args:
            owner (str): Deployment owner
            deployment (str): Deployment name
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

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
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    def update(
        self,
        owner: str,
        deployment: str,
        *,
        body: dict[str, Any],
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DeploymentsUpdateResponse:
        """Update a deployment.

        Starts, stops, or rolls out another model while preserving the endpoint URL.

        Args:
            owner (str): Deployment owner
            deployment (str): Deployment name
            body (dict[str, Any]): API request for updating a deployment
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

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
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json=body,
            ),
        )

    def delete(
        self,
        owner: str,
        deployment: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DeploymentsDeleteResponse:
        """Delete a deployment.

        Permanently removes the inference endpoint.

        Args:
            owner (str): Deployment owner
            deployment (str): Deployment name
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

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
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    def health(
        self,
        owner: str,
        deployment: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DeploymentsHealthResponse:
        """Check deployment health.

        Pings and warms the deployment endpoint.

        Args:
            owner (str): Deployment owner
            deployment (str): Deployment name
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DeploymentsHealthResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsHealthResponse,
            self._client.request(
                "GET",
                f"/api/deployments/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(deployment, explode=False, allow_reserved=False)}/health",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    def logs(
        self,
        owner: str,
        deployment: str,
        *,
        severity: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        page_token: str | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DeploymentsLogsResponse:
        """Get deployment logs.

        Returns recent deployment service logs.

        Args:
            owner (str): Deployment owner
            deployment (str): Deployment name
            severity (str, optional): Comma-separated log severity levels
            limit (int, optional): Maximum log entries to return
            page_token (str, optional): Pagination token
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DeploymentsLogsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsLogsResponse,
            self._client.request(
                "GET",
                f"/api/deployments/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(deployment, explode=False, allow_reserved=False)}/logs",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("severity", severity, style="form", explode=True),
                    *_query_parameter("limit", limit, style="form", explode=True),
                    *_query_parameter("pageToken", page_token, style="form", explode=True),
                ],
            ),
        )

    def metrics(
        self,
        owner: str,
        deployment: str,
        *,
        range: Literal["1h", "6h", "24h", "7d", "30d"] | NotGiven = NOT_GIVEN,
        sparkline: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DeploymentsMetricsResponse:
        """Get deployment metrics.

        Returns request volume, latency, errors, and resource utilization.

        Args:
            owner (str): Deployment owner
            deployment (str): Deployment name
            range (Literal["1h", "6h", "24h", "7d", "30d"], optional): Metrics time range
            sparkline (Literal["true", "false"], optional): Return the compact dashboard summary
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DeploymentsMetricsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsMetricsResponse,
            self._client.request(
                "GET",
                f"/api/deployments/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(deployment, explode=False, allow_reserved=False)}/metrics",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("range", range, style="form", explode=True),
                    *_query_parameter("sparkline", sparkline, style="form", explode=True),
                ],
            ),
        )

    def predict(
        self,
        owner: str,
        deployment: str,
        *,
        body: dict[str, Any],
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DeploymentsPredictResponse:
        """Run deployment inference.

        Runs inference through a dedicated deployment endpoint. Depth models accept images only.

        Args:
            owner (str): Deployment owner
            deployment (str): Deployment name
            body (dict[str, Any]): Request body.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

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
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                data=_form_data({key: value for key, value in body.items() if key not in ["file"]}, multipart=True),
                files={key: body[key] for key in ["file"] if key in body},
            ),
        )

    def list(
        self,
        owner: str,
        *,
        status: Literal["creating", "deploying", "ready", "stopping", "stopped", "failed"] | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DeploymentsListResponse:
        """List deployments.

        Returns workspace inference endpoints. Anonymous callers must filter by one public model; workspace-wide listing requires authentication.

        Args:
            owner (str): Deployment owner
            status (Literal["creating", "deploying", "ready", "stopping", "stopped", "failed"], optional): Deployment status filter
            model (str, optional): Project and model names separated by a slash
            limit (int, optional): Maximum deployments to return
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

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
                timeout=timeout,
                extra_headers=extra_headers,
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
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DeploymentsCreateResponse:
        """Deploy a model.

        Creates a dedicated auto-scaling inference endpoint for a model.

        Args:
            owner (str): Deployment owner
            project (str): Project name
            model (str): Model name
            deployment (str): Deployment name
            name (str): Display name
            region (Literal["asia-east1", "asia-northeast1", "asia-northeast2", "asia-south1", "asia-southeast3", "europe-north1", "europe-north2", "europe-southwest1", "europe-west1", "europe-west4", "europe-west8", "europe-west9", "me-west1", "northamerica-south1", "us-central1", "us-east1", "us-east4", "us-east5", "us-south1", "us-west1", "africa-south1", "asia-east2", "asia-northeast3", "asia-southeast1", "asia-southeast2", "asia-south2", "australia-southeast1", "australia-southeast2", "europe-central2", "europe-west10", "europe-west12", "europe-west2", "europe-west3", "europe-west6", "me-central1", "northamerica-northeast1", "northamerica-northeast2", "southamerica-east1", "southamerica-west1", "us-west2", "us-west3", "us-west4"]): region request value.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

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
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={"project": project, "model": model, "deployment": deployment, "name": name, "region": region},
            ),
        )


class AsyncDeployments:
    """Asynchronous Deployments API operations."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def retrieve(
        self,
        owner: str,
        deployment: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DeploymentsRetrieveResponse:
        """Get deployment details.

        Returns deployment configuration, status, and service URL.

        Args:
            owner (str): Deployment owner
            deployment (str): Deployment name
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

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
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    async def update(
        self,
        owner: str,
        deployment: str,
        *,
        body: dict[str, Any],
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DeploymentsUpdateResponse:
        """Update a deployment.

        Starts, stops, or rolls out another model while preserving the endpoint URL.

        Args:
            owner (str): Deployment owner
            deployment (str): Deployment name
            body (dict[str, Any]): API request for updating a deployment
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

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
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json=body,
            ),
        )

    async def delete(
        self,
        owner: str,
        deployment: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DeploymentsDeleteResponse:
        """Delete a deployment.

        Permanently removes the inference endpoint.

        Args:
            owner (str): Deployment owner
            deployment (str): Deployment name
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

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
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    async def health(
        self,
        owner: str,
        deployment: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DeploymentsHealthResponse:
        """Check deployment health.

        Pings and warms the deployment endpoint.

        Args:
            owner (str): Deployment owner
            deployment (str): Deployment name
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DeploymentsHealthResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsHealthResponse,
            await self._client.request(
                "GET",
                f"/api/deployments/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(deployment, explode=False, allow_reserved=False)}/health",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    async def logs(
        self,
        owner: str,
        deployment: str,
        *,
        severity: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        page_token: str | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DeploymentsLogsResponse:
        """Get deployment logs.

        Returns recent deployment service logs.

        Args:
            owner (str): Deployment owner
            deployment (str): Deployment name
            severity (str, optional): Comma-separated log severity levels
            limit (int, optional): Maximum log entries to return
            page_token (str, optional): Pagination token
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DeploymentsLogsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsLogsResponse,
            await self._client.request(
                "GET",
                f"/api/deployments/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(deployment, explode=False, allow_reserved=False)}/logs",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("severity", severity, style="form", explode=True),
                    *_query_parameter("limit", limit, style="form", explode=True),
                    *_query_parameter("pageToken", page_token, style="form", explode=True),
                ],
            ),
        )

    async def metrics(
        self,
        owner: str,
        deployment: str,
        *,
        range: Literal["1h", "6h", "24h", "7d", "30d"] | NotGiven = NOT_GIVEN,
        sparkline: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DeploymentsMetricsResponse:
        """Get deployment metrics.

        Returns request volume, latency, errors, and resource utilization.

        Args:
            owner (str): Deployment owner
            deployment (str): Deployment name
            range (Literal["1h", "6h", "24h", "7d", "30d"], optional): Metrics time range
            sparkline (Literal["true", "false"], optional): Return the compact dashboard summary
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DeploymentsMetricsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DeploymentsMetricsResponse,
            await self._client.request(
                "GET",
                f"/api/deployments/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(deployment, explode=False, allow_reserved=False)}/metrics",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("range", range, style="form", explode=True),
                    *_query_parameter("sparkline", sparkline, style="form", explode=True),
                ],
            ),
        )

    async def predict(
        self,
        owner: str,
        deployment: str,
        *,
        body: dict[str, Any],
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DeploymentsPredictResponse:
        """Run deployment inference.

        Runs inference through a dedicated deployment endpoint. Depth models accept images only.

        Args:
            owner (str): Deployment owner
            deployment (str): Deployment name
            body (dict[str, Any]): Request body.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

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
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                data=_form_data({key: value for key, value in body.items() if key not in ["file"]}, multipart=True),
                files={key: body[key] for key in ["file"] if key in body},
            ),
        )

    async def list(
        self,
        owner: str,
        *,
        status: Literal["creating", "deploying", "ready", "stopping", "stopped", "failed"] | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DeploymentsListResponse:
        """List deployments.

        Returns workspace inference endpoints. Anonymous callers must filter by one public model; workspace-wide listing requires authentication.

        Args:
            owner (str): Deployment owner
            status (Literal["creating", "deploying", "ready", "stopping", "stopped", "failed"], optional): Deployment status filter
            model (str, optional): Project and model names separated by a slash
            limit (int, optional): Maximum deployments to return
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

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
                timeout=timeout,
                extra_headers=extra_headers,
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
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DeploymentsCreateResponse:
        """Deploy a model.

        Creates a dedicated auto-scaling inference endpoint for a model.

        Args:
            owner (str): Deployment owner
            project (str): Project name
            model (str): Model name
            deployment (str): Deployment name
            name (str): Display name
            region (Literal["asia-east1", "asia-northeast1", "asia-northeast2", "asia-south1", "asia-southeast3", "europe-north1", "europe-north2", "europe-southwest1", "europe-west1", "europe-west4", "europe-west8", "europe-west9", "me-west1", "northamerica-south1", "us-central1", "us-east1", "us-east4", "us-east5", "us-south1", "us-west1", "africa-south1", "asia-east2", "asia-northeast3", "asia-southeast1", "asia-southeast2", "asia-south2", "australia-southeast1", "australia-southeast2", "europe-central2", "europe-west10", "europe-west12", "europe-west2", "europe-west3", "europe-west6", "me-central1", "northamerica-northeast1", "northamerica-northeast2", "southamerica-east1", "southamerica-west1", "us-west2", "us-west3", "us-west4"]): region request value.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

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
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={"project": project, "model": model, "deployment": deployment, "name": name, "region": region},
            ),
        )
