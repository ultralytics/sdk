# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from __future__ import annotations

from typing import Literal, cast

import httpx

from .._client import (
    NOT_GIVEN,
    AsyncAPIClient,
    NotGiven,
    SyncAPIClient,
    _query_parameter,
)
from ..types import (
    AccountApiKeysResponse,
    AccountFollowResponse,
    AccountProfileResponse,
    AccountStorageResponse,
    AccountSummaryResponse,
)


class Account:
    """Account API operations."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def summary(
        self, timeout: float | httpx.Timeout | None = None, extra_headers: dict[str, str] | None = None
    ) -> AccountSummaryResponse:
        """Summarize your Platform account.

        Returns your plan, credit balance, and resource counts. Browser sessions also include team workspaces.

        Args:
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (AccountSummaryResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountSummaryResponse,
            self._client.request(
                "GET",
                "/api/account/summary",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    def api_keys(
        self, timeout: float | httpx.Timeout | None = None, extra_headers: dict[str, str] | None = None
    ) -> AccountApiKeysResponse:
        """List API keys.

        Returns active API key metadata for the API key's workspace.

        Args:
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (AccountApiKeysResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountApiKeysResponse,
            self._client.request(
                "GET", "/api/api-keys", timeout=timeout, extra_headers=extra_headers, auth=("Authorization", "Bearer ")
            ),
        )

    def storage(
        self,
        *,
        details: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> AccountStorageResponse:
        """Check storage usage.

        Returns storage breakdown by category and, when requested, the workspace's largest items.

        Args:
            details (Literal["true", "false"], optional): Include the ten largest storage consumers
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (AccountStorageResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountStorageResponse,
            self._client.request(
                "GET",
                "/api/storage",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("details", details, style="form", explode=True)],
            ),
        )

    def profile(
        self,
        *,
        username: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> AccountProfileResponse:
        """Get a public user profile.

        Returns a public user profile and its follow state for the authenticated caller.

        Args:
            username (str): username query parameter.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (AccountProfileResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountProfileResponse,
            self._client.request(
                "GET",
                "/api/users",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("username", username, style="form", explode=True)],
            ),
        )

    def follow(
        self,
        *,
        username: str,
        followed: bool,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> AccountFollowResponse:
        """Follow a user.

        Follows or unfollows a Platform user.

        Args:
            username (str): username request value.
            followed (bool): followed request value.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (AccountFollowResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountFollowResponse,
            self._client.request(
                "PATCH",
                "/api/users",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={"username": username, "followed": followed},
            ),
        )


class AsyncAccount:
    """Asynchronous Account API operations."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def summary(
        self, timeout: float | httpx.Timeout | None = None, extra_headers: dict[str, str] | None = None
    ) -> AccountSummaryResponse:
        """Summarize your Platform account.

        Returns your plan, credit balance, and resource counts. Browser sessions also include team workspaces.

        Args:
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (AccountSummaryResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountSummaryResponse,
            await self._client.request(
                "GET",
                "/api/account/summary",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    async def api_keys(
        self, timeout: float | httpx.Timeout | None = None, extra_headers: dict[str, str] | None = None
    ) -> AccountApiKeysResponse:
        """List API keys.

        Returns active API key metadata for the API key's workspace.

        Args:
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (AccountApiKeysResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountApiKeysResponse,
            await self._client.request(
                "GET", "/api/api-keys", timeout=timeout, extra_headers=extra_headers, auth=("Authorization", "Bearer ")
            ),
        )

    async def storage(
        self,
        *,
        details: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> AccountStorageResponse:
        """Check storage usage.

        Returns storage breakdown by category and, when requested, the workspace's largest items.

        Args:
            details (Literal["true", "false"], optional): Include the ten largest storage consumers
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (AccountStorageResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountStorageResponse,
            await self._client.request(
                "GET",
                "/api/storage",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("details", details, style="form", explode=True)],
            ),
        )

    async def profile(
        self,
        *,
        username: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> AccountProfileResponse:
        """Get a public user profile.

        Returns a public user profile and its follow state for the authenticated caller.

        Args:
            username (str): username query parameter.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (AccountProfileResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountProfileResponse,
            await self._client.request(
                "GET",
                "/api/users",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("username", username, style="form", explode=True)],
            ),
        )

    async def follow(
        self,
        *,
        username: str,
        followed: bool,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> AccountFollowResponse:
        """Follow a user.

        Follows or unfollows a Platform user.

        Args:
            username (str): username request value.
            followed (bool): followed request value.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (AccountFollowResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountFollowResponse,
            await self._client.request(
                "PATCH",
                "/api/users",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={"username": username, "followed": followed},
            ),
        )
