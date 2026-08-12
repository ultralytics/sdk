# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from __future__ import annotations

from typing import Literal, cast

from .._client import (
    AsyncAPIClient,
    SyncAPIClient,
    _query_parameter,
)
from ..types import (
    AccountFollowUserResponse,
    AccountListApiKeysResponse,
    AccountRetrievePublicUserProfileResponse,
    AccountRetrieveStorageUsageResponse,
    AccountRetrieveSummaryResponse,
)


class Account:
    """Account API operations."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def retrieve_summary(self) -> AccountRetrieveSummaryResponse:
        """Summarize your Platform account.

        Returns your plan, credit balance, and resource counts. Browser sessions also include team workspaces.

        Returns:
            (AccountRetrieveSummaryResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountRetrieveSummaryResponse,
            self._client.request("GET", "/api/account/summary", auth=("Authorization", "Bearer ")),
        )

    def list_api_keys(self) -> AccountListApiKeysResponse:
        """List API keys.

        Returns active API key metadata for the API key's workspace.

        Returns:
            (AccountListApiKeysResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountListApiKeysResponse, self._client.request("GET", "/api/api-keys", auth=("Authorization", "Bearer "))
        )

    def retrieve_storage_usage(
        self, *, details: Literal["true", "false"] | None = None
    ) -> AccountRetrieveStorageUsageResponse:
        """Check storage usage.

        Returns storage breakdown by category and, when requested, the workspace's largest items.

        Args:
            details (Literal["true", "false"], optional): Include the ten largest storage consumers

        Returns:
            (AccountRetrieveStorageUsageResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountRetrieveStorageUsageResponse,
            self._client.request(
                "GET",
                "/api/storage",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("details", details, style="form", explode=True)],
            ),
        )

    def retrieve_public_user_profile(self, *, username: str) -> AccountRetrievePublicUserProfileResponse:
        """Get a public user profile.

        Returns a public user profile and its follow state for the authenticated caller.

        Args:
            username (str): username query parameter.

        Returns:
            (AccountRetrievePublicUserProfileResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountRetrievePublicUserProfileResponse,
            self._client.request(
                "GET",
                "/api/users",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("username", username, style="form", explode=True)],
            ),
        )

    def follow_user(self, *, username: str, followed: bool) -> AccountFollowUserResponse:
        """Follow a user.

        Follows or unfollows a Platform user.

        Args:
            username (str): username request value.
            followed (bool): followed request value.

        Returns:
            (AccountFollowUserResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountFollowUserResponse,
            self._client.request(
                "PATCH",
                "/api/users",
                auth=("Authorization", "Bearer "),
                json={"username": username, "followed": followed},
            ),
        )


class AsyncAccount:
    """Asynchronous Account API operations."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def retrieve_summary(self) -> AccountRetrieveSummaryResponse:
        """Summarize your Platform account.

        Returns your plan, credit balance, and resource counts. Browser sessions also include team workspaces.

        Returns:
            (AccountRetrieveSummaryResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountRetrieveSummaryResponse,
            await self._client.request("GET", "/api/account/summary", auth=("Authorization", "Bearer ")),
        )

    async def list_api_keys(self) -> AccountListApiKeysResponse:
        """List API keys.

        Returns active API key metadata for the API key's workspace.

        Returns:
            (AccountListApiKeysResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountListApiKeysResponse,
            await self._client.request("GET", "/api/api-keys", auth=("Authorization", "Bearer ")),
        )

    async def retrieve_storage_usage(
        self, *, details: Literal["true", "false"] | None = None
    ) -> AccountRetrieveStorageUsageResponse:
        """Check storage usage.

        Returns storage breakdown by category and, when requested, the workspace's largest items.

        Args:
            details (Literal["true", "false"], optional): Include the ten largest storage consumers

        Returns:
            (AccountRetrieveStorageUsageResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountRetrieveStorageUsageResponse,
            await self._client.request(
                "GET",
                "/api/storage",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("details", details, style="form", explode=True)],
            ),
        )

    async def retrieve_public_user_profile(self, *, username: str) -> AccountRetrievePublicUserProfileResponse:
        """Get a public user profile.

        Returns a public user profile and its follow state for the authenticated caller.

        Args:
            username (str): username query parameter.

        Returns:
            (AccountRetrievePublicUserProfileResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountRetrievePublicUserProfileResponse,
            await self._client.request(
                "GET",
                "/api/users",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("username", username, style="form", explode=True)],
            ),
        )

    async def follow_user(self, *, username: str, followed: bool) -> AccountFollowUserResponse:
        """Follow a user.

        Follows or unfollows a Platform user.

        Args:
            username (str): username request value.
            followed (bool): followed request value.

        Returns:
            (AccountFollowUserResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountFollowUserResponse,
            await self._client.request(
                "PATCH",
                "/api/users",
                auth=("Authorization", "Bearer "),
                json={"username": username, "followed": followed},
            ),
        )
