# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from __future__ import annotations

import os

import httpx

from ._client import AsyncAPIClient
from .resources import (
    AsyncAccount,
    AsyncBilling,
    AsyncDatasets,
    AsyncDeployments,
    AsyncExplore,
    AsyncExports,
    AsyncImages,
    AsyncLifecycle,
    AsyncModels,
    AsyncProjects,
    AsyncStorageIntegrations,
    AsyncTraining,
    AsyncUpload,
)


class AsyncPlatform:
    """Client for the Ultralytics Platform API."""

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str = "https://platform.ultralytics.com",
        timeout: float | httpx.Timeout = 60.0,
        max_retries: int = 2,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        """Initialize the client.

        Args:
            api_key (str, optional): API key. Defaults to ULTRALYTICS_API_KEY.
            base_url (str): API base URL.
            timeout (float | httpx.Timeout): Request timeout.
            max_retries (int): Retries for connection errors and retryable responses.
            http_client (httpx.AsyncClient, optional): Custom HTTP client.
        """
        resolved_api_key = api_key or os.environ.get("ULTRALYTICS_API_KEY")
        self._client = AsyncAPIClient(
            api_key=resolved_api_key,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            http_client=http_client,
        )
        self.account = AsyncAccount(self._client)
        self.billing = AsyncBilling(self._client)
        self.datasets = AsyncDatasets(self._client)
        self.deployments = AsyncDeployments(self._client)
        self.explore = AsyncExplore(self._client)
        self.images = AsyncImages(self._client)
        self.storage_integrations = AsyncStorageIntegrations(self._client)
        self.models = AsyncModels(self._client)
        self.exports = AsyncExports(self._client)
        self.projects = AsyncProjects(self._client)
        self.training = AsyncTraining(self._client)
        self.lifecycle = AsyncLifecycle(self._client)
        self.upload = AsyncUpload(self._client)

    async def close(self) -> None:
        """Close the underlying HTTP client."""
        await self._client.close()

    async def __aenter__(self) -> AsyncPlatform:  # noqa: PYI034
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: object,
    ) -> None:
        await self.close()
