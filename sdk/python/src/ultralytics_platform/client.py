# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from __future__ import annotations

import os

import httpx

from ._client import SyncAPIClient
from .resources import (
    Account,
    Billing,
    Datasets,
    Deployments,
    Explore,
    Exports,
    Images,
    Lifecycle,
    Models,
    Projects,
    StorageIntegrations,
    Training,
    Upload,
)


class Platform:
    """Client for the Ultralytics Platform API."""

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str = "https://platform.ultralytics.com",
        timeout: float | httpx.Timeout = 60.0,
        max_retries: int = 2,
        http_client: httpx.Client | None = None,
    ) -> None:
        """Initialize the client.

        Args:
            api_key (str, optional): API key. Defaults to ULTRALYTICS_API_KEY.
            base_url (str): API base URL.
            timeout (float | httpx.Timeout): Request timeout.
            max_retries (int): Retries for connection errors and retryable responses.
            http_client (httpx.Client, optional): Custom HTTP client.
        """
        resolved_api_key = api_key or os.environ.get("ULTRALYTICS_API_KEY")
        self._client = SyncAPIClient(
            api_key=resolved_api_key,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            http_client=http_client,
        )
        self.account = Account(self._client)
        self.billing = Billing(self._client)
        self.datasets = Datasets(self._client)
        self.deployments = Deployments(self._client)
        self.explore = Explore(self._client)
        self.images = Images(self._client)
        self.storage_integrations = StorageIntegrations(self._client)
        self.models = Models(self._client)
        self.exports = Exports(self._client)
        self.projects = Projects(self._client)
        self.training = Training(self._client)
        self.lifecycle = Lifecycle(self._client)
        self.upload = Upload(self._client)

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()

    def __enter__(self) -> Platform:  # noqa: PYI034
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: object,
    ) -> None:
        self.close()
