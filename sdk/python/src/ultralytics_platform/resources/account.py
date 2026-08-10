from __future__ import annotations

from typing import Any, BinaryIO, Literal, cast

from .._client import (
    NOT_GIVEN,
    AsyncAPIClient,
    NotGiven,
    SyncAPIClient,
    _path_parameter,
    _query_parameter,
)
from ..types import (
    AccountBrowseCloudStorageObjectsResponse,
    AccountConnectCloudStorageResponse,
    AccountCreateApiKeyResponse,
    AccountDeleteWorkspaceIconResponse,
    AccountDiscoverCloudStorageLocationsResponse,
    AccountFollowOrUnfollowUserResponse,
    AccountListApiKeysResponse,
    AccountListCloudStorageIntegrationsResponse,
    AccountPermanentlyDeleteAllTrashedItemsResponse,
    AccountPermanentlyDeleteTrashedItemResponse,
    AccountRestoreTrashedItemResponse,
    AccountRetrieveIfUsernameIsAvailableResponse,
    AccountRetrieveProfileSettingsResponse,
    AccountRetrievePublicUserProfileResponse,
    AccountRetrieveStorageUsageResponse,
    AccountRetrieveSummaryResponse,
    AccountRetrieveTrashResponse,
    AccountRevokeApiKeyResponse,
    AccountUpdateProfileSettingsResponse,
    AccountUploadWorkspaceIconResponse,
)


class Account:
    """Account API operations."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def retrieve_summary(self) -> AccountRetrieveSummaryResponse:
        """Summarize your Platform account.

        Returns your plan, credit balance, resource counts, and team workspaces.

        Returns:
            (AccountRetrieveSummaryResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountRetrieveSummaryResponse,
            self._client.request("GET", "/api/account/summary", auth=("Authorization", "Bearer ")),
        )

    def list_api_keys(self, *, owner: str | None = None) -> AccountListApiKeysResponse:
        """List your API keys.

        Args:
            owner (str, optional): Workspace username

        Returns:
            (AccountListApiKeysResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountListApiKeysResponse,
            self._client.request(
                "GET",
                "/api/api-keys",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
            ),
        )

    def create_api_key(
        self, *, owner: str | None = None, name: str | NotGiven = NOT_GIVEN
    ) -> AccountCreateApiKeyResponse:
        """Create a new API key.

        Generates a new API key. Important: the full key is only shown once in the response — save it securely.

        Args:
            owner (str, optional): Workspace username
            name (str, optional): A label to identify this key (e.g. 'production', 'testing')

        Returns:
            (AccountCreateApiKeyResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountCreateApiKeyResponse,
            self._client.request(
                "POST",
                "/api/api-keys",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
                json={"name": name},
            ),
        )

    def revoke_api_key(self, *, key_id: str, owner: str | None = None) -> AccountRevokeApiKeyResponse:
        """Revoke an API key.

        Permanently deletes an API key. Any applications using this key will stop working immediately.

        Args:
            key_id (str): ID of the key to revoke
            owner (str, optional): Workspace username

        Returns:
            (AccountRevokeApiKeyResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountRevokeApiKeyResponse,
            self._client.request(
                "DELETE",
                "/api/api-keys",
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("keyId", key_id, style="form", explode=True),
                    *_query_parameter("owner", owner, style="form", explode=True),
                ],
            ),
        )

    def retrieve_storage_usage(
        self, *, owner: str | None = None, details: bool | None = None
    ) -> AccountRetrieveStorageUsageResponse:
        """Check storage usage.

        Returns storage breakdown by category (datasets, models, exports) and your largest items.

        Args:
            owner (str, optional): Team username (to check team storage)
            details (bool, optional): Include the ten largest storage consumers

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
                params=[
                    *_query_parameter("owner", owner, style="form", explode=True),
                    *_query_parameter("details", details, style="form", explode=True),
                ],
            ),
        )

    def retrieve_profile_settings(self, *, owner: str | None = None) -> AccountRetrieveProfileSettingsResponse:
        """Get your profile settings.

        Args:
            owner (str, optional): Workspace username

        Returns:
            (AccountRetrieveProfileSettingsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountRetrieveProfileSettingsResponse,
            self._client.request(
                "GET",
                "/api/settings",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
            ),
        )

    def update_profile_settings(
        self,
        *,
        owner: str | None = None,
        display_name: Any | NotGiven = NOT_GIVEN,
        company: str | NotGiven = NOT_GIVEN,
        use_case: str | NotGiven = NOT_GIVEN,
        bio: str | Literal[""] | NotGiven = NOT_GIVEN,
        github: str | NotGiven = NOT_GIVEN,
        linkedin: str | NotGiven = NOT_GIVEN,
        twitter: str | NotGiven = NOT_GIVEN,
        discord: str | NotGiven = NOT_GIVEN,
        youtube: str | NotGiven = NOT_GIVEN,
        scholar: str | NotGiven = NOT_GIVEN,
        website: str | NotGiven = NOT_GIVEN,
        icon_color: str | NotGiven = NOT_GIVEN,
        icon_letter: str | Literal[""] | NotGiven = NOT_GIVEN,
    ) -> AccountUpdateProfileSettingsResponse:
        """Update your profile settings.

        Update your display name, bio, company, social links, and other profile details.

        Args:
            owner (str, optional): Workspace username
            display_name (Any, optional): displayName request value.
            company (str, optional): company request value.
            use_case (str, optional): useCase request value.
            bio (str | Literal[""], optional): bio request value.
            github (str, optional): github request value.
            linkedin (str, optional): linkedin request value.
            twitter (str, optional): twitter request value.
            discord (str, optional): discord request value.
            youtube (str, optional): youtube request value.
            scholar (str, optional): scholar request value.
            website (str, optional): website request value.
            icon_color (str, optional): iconColor request value.
            icon_letter (str | Literal[""], optional): iconLetter request value.

        Returns:
            (AccountUpdateProfileSettingsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountUpdateProfileSettingsResponse,
            self._client.request(
                "POST",
                "/api/settings",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
                json={
                    "displayName": display_name,
                    "company": company,
                    "useCase": use_case,
                    "bio": bio,
                    "github": github,
                    "linkedin": linkedin,
                    "twitter": twitter,
                    "discord": discord,
                    "youtube": youtube,
                    "scholar": scholar,
                    "website": website,
                    "iconColor": icon_color,
                    "iconLetter": icon_letter,
                },
            ),
        )

    def list_cloud_storage_integrations(
        self, *, owner: str | None = None
    ) -> AccountListCloudStorageIntegrationsResponse:
        """List cloud storage integrations.

        Args:
            owner (str, optional): Workspace username

        Returns:
            (AccountListCloudStorageIntegrationsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountListCloudStorageIntegrationsResponse,
            self._client.request(
                "GET",
                "/api/integrations/buckets",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
            ),
        )

    def connect_cloud_storage(
        self,
        *,
        provider: Literal["gcs", "s3", "azure"],
        credentials: dict[str, Any],
        targets: list[str],
        owner: str | None = None,
    ) -> AccountConnectCloudStorageResponse:
        """Connect cloud storage.

        Args:
            owner (str, optional): Workspace username
            provider (Literal["gcs", "s3", "azure"]): provider request value.
            credentials (dict[str, Any]): credentials request value.
            targets (list[str]): targets request value.

        Returns:
            (AccountConnectCloudStorageResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountConnectCloudStorageResponse,
            self._client.request(
                "POST",
                "/api/integrations/buckets",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
                json={"provider": provider, "credentials": credentials, "targets": targets},
            ),
        )

    def discover_cloud_storage_locations(
        self, *, provider: Literal["gcs", "s3", "azure"], credentials: dict[str, Any], owner: str | None = None
    ) -> AccountDiscoverCloudStorageLocationsResponse:
        """Discover cloud storage locations.

        Args:
            owner (str, optional): Workspace username
            provider (Literal["gcs", "s3", "azure"]): provider request value.
            credentials (dict[str, Any]): credentials request value.

        Returns:
            (AccountDiscoverCloudStorageLocationsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountDiscoverCloudStorageLocationsResponse,
            self._client.request(
                "POST",
                "/api/integrations/buckets/discover",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
                json={"provider": provider, "credentials": credentials},
            ),
        )

    def browse_cloud_storage_objects(
        self, id: str, *, target: str, prefix: str | None = None, cursor: str | None = None, owner: str | None = None
    ) -> AccountBrowseCloudStorageObjectsResponse:
        """Browse cloud storage objects.

        Args:
            id (str): id path parameter.
            target (str): Bucket or container name
            prefix (str, optional): Folder prefix
            cursor (str, optional): Provider pagination cursor
            owner (str, optional): Workspace username

        Returns:
            (AccountBrowseCloudStorageObjectsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountBrowseCloudStorageObjectsResponse,
            self._client.request(
                "GET",
                f"/api/integrations/buckets/{_path_parameter(id, explode=False, allow_reserved=False)}/objects",
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("target", target, style="form", explode=True),
                    *_query_parameter("prefix", prefix, style="form", explode=True),
                    *_query_parameter("cursor", cursor, style="form", explode=True),
                    *_query_parameter("owner", owner, style="form", explode=True),
                ],
            ),
        )

    def retrieve_trash(
        self,
        *,
        type: Literal["all", "project", "dataset", "model"] | None = None,
        page: int | None = None,
        limit: int | None = None,
        owner: str | None = None,
    ) -> AccountRetrieveTrashResponse:
        """View trash.

        Returns deleted items that can still be restored. Items are permanently deleted after 30 days.

        Args:
            type (Literal["all", "project", "dataset", "model"], optional): Resource type filter
            page (int, optional): Page number (default 1)
            limit (int, optional): Items per page (default 50)
            owner (str, optional): Workspace username

        Returns:
            (AccountRetrieveTrashResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountRetrieveTrashResponse,
            self._client.request(
                "GET",
                "/api/trash",
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("type", type, style="form", explode=True),
                    *_query_parameter("page", page, style="form", explode=True),
                    *_query_parameter("limit", limit, style="form", explode=True),
                    *_query_parameter("owner", owner, style="form", explode=True),
                ],
            ),
        )

    def restore_trashed_item(
        self, *, id: str, type: Literal["project", "dataset", "model"]
    ) -> AccountRestoreTrashedItemResponse:
        """Restore a trashed item.

        Args:
            id (str): id request value.
            type (Literal["project", "dataset", "model"]): type request value.

        Returns:
            (AccountRestoreTrashedItemResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountRestoreTrashedItemResponse,
            self._client.request(
                "POST", "/api/trash", auth=("Authorization", "Bearer "), json={"id": id, "type": type}
            ),
        )

    def permanently_delete_trashed_item(
        self, *, id: str, type: Literal["project", "dataset", "model"]
    ) -> AccountPermanentlyDeleteTrashedItemResponse:
        """Permanently delete a trashed item.

        Permanently deletes one trashed resource. This cannot be undone.

        Args:
            id (str): id request value.
            type (Literal["project", "dataset", "model"]): type request value.

        Returns:
            (AccountPermanentlyDeleteTrashedItemResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountPermanentlyDeleteTrashedItemResponse,
            self._client.request(
                "DELETE", "/api/trash", auth=("Authorization", "Bearer "), json={"id": id, "type": type}
            ),
        )

    def permanently_delete_all_trashed_items(
        self, *, owner: str | None = None
    ) -> AccountPermanentlyDeleteAllTrashedItemsResponse:
        """Permanently delete all trashed items.

        Permanently deletes everything in your trash. This cannot be undone.

        Args:
            owner (str, optional): Workspace username

        Returns:
            (AccountPermanentlyDeleteAllTrashedItemsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountPermanentlyDeleteAllTrashedItemsResponse,
            self._client.request(
                "DELETE",
                "/api/trash/empty",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
            ),
        )

    def retrieve_if_username_is_available(
        self, *, username: str, suggest: bool | None = None
    ) -> AccountRetrieveIfUsernameIsAvailableResponse:
        """Check if a username is available.

        Args:
            username (str): Username to check
            suggest (bool, optional): Return a suggestion if unavailable

        Returns:
            (AccountRetrieveIfUsernameIsAvailableResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountRetrieveIfUsernameIsAvailableResponse,
            self._client.request(
                "GET",
                "/api/username/check",
                params=[
                    *_query_parameter("username", username, style="form", explode=True),
                    *_query_parameter("suggest", suggest, style="form", explode=True),
                ],
            ),
        )

    def retrieve_public_user_profile(self, *, username: str) -> AccountRetrievePublicUserProfileResponse:
        """Get a public user profile.

        Args:
            username (str): Username to look up

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

    def follow_or_unfollow_user(self, *, username: str, followed: bool) -> AccountFollowOrUnfollowUserResponse:
        """Follow or unfollow a user.

        Args:
            username (str): username request value.
            followed (bool): followed request value.

        Returns:
            (AccountFollowOrUnfollowUserResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountFollowOrUnfollowUserResponse,
            self._client.request(
                "PATCH",
                "/api/users",
                auth=("Authorization", "Bearer "),
                json={"username": username, "followed": followed},
            ),
        )

    def upload_workspace_icon(
        self,
        *,
        image: BinaryIO,
        owner: str | None = None,
        icon_color: str | NotGiven = NOT_GIVEN,
        icon_letter: str | NotGiven = NOT_GIVEN,
    ) -> AccountUploadWorkspaceIconResponse:
        """Upload a workspace icon.

        Args:
            owner (str, optional): Workspace username
            image (BinaryIO): WebP image, maximum 5 MB
            icon_color (str, optional): iconColor request value.
            icon_letter (str, optional): iconLetter request value.

        Returns:
            (AccountUploadWorkspaceIconResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountUploadWorkspaceIconResponse,
            self._client.request(
                "POST",
                "/api/settings/icon",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
                data={"iconColor": icon_color, "iconLetter": icon_letter},
                files={"image": image},
            ),
        )

    def delete_workspace_icon(self, *, owner: str | None = None) -> AccountDeleteWorkspaceIconResponse:
        """Delete a workspace icon.

        Args:
            owner (str, optional): Workspace username

        Returns:
            (AccountDeleteWorkspaceIconResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountDeleteWorkspaceIconResponse,
            self._client.request(
                "DELETE",
                "/api/settings/icon",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
            ),
        )


class AsyncAccount:
    """Asynchronous Account API operations."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def retrieve_summary(self) -> AccountRetrieveSummaryResponse:
        """Summarize your Platform account.

        Returns your plan, credit balance, resource counts, and team workspaces.

        Returns:
            (AccountRetrieveSummaryResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountRetrieveSummaryResponse,
            await self._client.request("GET", "/api/account/summary", auth=("Authorization", "Bearer ")),
        )

    async def list_api_keys(self, *, owner: str | None = None) -> AccountListApiKeysResponse:
        """List your API keys.

        Args:
            owner (str, optional): Workspace username

        Returns:
            (AccountListApiKeysResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountListApiKeysResponse,
            await self._client.request(
                "GET",
                "/api/api-keys",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
            ),
        )

    async def create_api_key(
        self, *, owner: str | None = None, name: str | NotGiven = NOT_GIVEN
    ) -> AccountCreateApiKeyResponse:
        """Create a new API key.

        Generates a new API key. Important: the full key is only shown once in the response — save it securely.

        Args:
            owner (str, optional): Workspace username
            name (str, optional): A label to identify this key (e.g. 'production', 'testing')

        Returns:
            (AccountCreateApiKeyResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountCreateApiKeyResponse,
            await self._client.request(
                "POST",
                "/api/api-keys",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
                json={"name": name},
            ),
        )

    async def revoke_api_key(self, *, key_id: str, owner: str | None = None) -> AccountRevokeApiKeyResponse:
        """Revoke an API key.

        Permanently deletes an API key. Any applications using this key will stop working immediately.

        Args:
            key_id (str): ID of the key to revoke
            owner (str, optional): Workspace username

        Returns:
            (AccountRevokeApiKeyResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountRevokeApiKeyResponse,
            await self._client.request(
                "DELETE",
                "/api/api-keys",
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("keyId", key_id, style="form", explode=True),
                    *_query_parameter("owner", owner, style="form", explode=True),
                ],
            ),
        )

    async def retrieve_storage_usage(
        self, *, owner: str | None = None, details: bool | None = None
    ) -> AccountRetrieveStorageUsageResponse:
        """Check storage usage.

        Returns storage breakdown by category (datasets, models, exports) and your largest items.

        Args:
            owner (str, optional): Team username (to check team storage)
            details (bool, optional): Include the ten largest storage consumers

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
                params=[
                    *_query_parameter("owner", owner, style="form", explode=True),
                    *_query_parameter("details", details, style="form", explode=True),
                ],
            ),
        )

    async def retrieve_profile_settings(self, *, owner: str | None = None) -> AccountRetrieveProfileSettingsResponse:
        """Get your profile settings.

        Args:
            owner (str, optional): Workspace username

        Returns:
            (AccountRetrieveProfileSettingsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountRetrieveProfileSettingsResponse,
            await self._client.request(
                "GET",
                "/api/settings",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
            ),
        )

    async def update_profile_settings(
        self,
        *,
        owner: str | None = None,
        display_name: Any | NotGiven = NOT_GIVEN,
        company: str | NotGiven = NOT_GIVEN,
        use_case: str | NotGiven = NOT_GIVEN,
        bio: str | Literal[""] | NotGiven = NOT_GIVEN,
        github: str | NotGiven = NOT_GIVEN,
        linkedin: str | NotGiven = NOT_GIVEN,
        twitter: str | NotGiven = NOT_GIVEN,
        discord: str | NotGiven = NOT_GIVEN,
        youtube: str | NotGiven = NOT_GIVEN,
        scholar: str | NotGiven = NOT_GIVEN,
        website: str | NotGiven = NOT_GIVEN,
        icon_color: str | NotGiven = NOT_GIVEN,
        icon_letter: str | Literal[""] | NotGiven = NOT_GIVEN,
    ) -> AccountUpdateProfileSettingsResponse:
        """Update your profile settings.

        Update your display name, bio, company, social links, and other profile details.

        Args:
            owner (str, optional): Workspace username
            display_name (Any, optional): displayName request value.
            company (str, optional): company request value.
            use_case (str, optional): useCase request value.
            bio (str | Literal[""], optional): bio request value.
            github (str, optional): github request value.
            linkedin (str, optional): linkedin request value.
            twitter (str, optional): twitter request value.
            discord (str, optional): discord request value.
            youtube (str, optional): youtube request value.
            scholar (str, optional): scholar request value.
            website (str, optional): website request value.
            icon_color (str, optional): iconColor request value.
            icon_letter (str | Literal[""], optional): iconLetter request value.

        Returns:
            (AccountUpdateProfileSettingsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountUpdateProfileSettingsResponse,
            await self._client.request(
                "POST",
                "/api/settings",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
                json={
                    "displayName": display_name,
                    "company": company,
                    "useCase": use_case,
                    "bio": bio,
                    "github": github,
                    "linkedin": linkedin,
                    "twitter": twitter,
                    "discord": discord,
                    "youtube": youtube,
                    "scholar": scholar,
                    "website": website,
                    "iconColor": icon_color,
                    "iconLetter": icon_letter,
                },
            ),
        )

    async def list_cloud_storage_integrations(
        self, *, owner: str | None = None
    ) -> AccountListCloudStorageIntegrationsResponse:
        """List cloud storage integrations.

        Args:
            owner (str, optional): Workspace username

        Returns:
            (AccountListCloudStorageIntegrationsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountListCloudStorageIntegrationsResponse,
            await self._client.request(
                "GET",
                "/api/integrations/buckets",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
            ),
        )

    async def connect_cloud_storage(
        self,
        *,
        provider: Literal["gcs", "s3", "azure"],
        credentials: dict[str, Any],
        targets: list[str],
        owner: str | None = None,
    ) -> AccountConnectCloudStorageResponse:
        """Connect cloud storage.

        Args:
            owner (str, optional): Workspace username
            provider (Literal["gcs", "s3", "azure"]): provider request value.
            credentials (dict[str, Any]): credentials request value.
            targets (list[str]): targets request value.

        Returns:
            (AccountConnectCloudStorageResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountConnectCloudStorageResponse,
            await self._client.request(
                "POST",
                "/api/integrations/buckets",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
                json={"provider": provider, "credentials": credentials, "targets": targets},
            ),
        )

    async def discover_cloud_storage_locations(
        self, *, provider: Literal["gcs", "s3", "azure"], credentials: dict[str, Any], owner: str | None = None
    ) -> AccountDiscoverCloudStorageLocationsResponse:
        """Discover cloud storage locations.

        Args:
            owner (str, optional): Workspace username
            provider (Literal["gcs", "s3", "azure"]): provider request value.
            credentials (dict[str, Any]): credentials request value.

        Returns:
            (AccountDiscoverCloudStorageLocationsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountDiscoverCloudStorageLocationsResponse,
            await self._client.request(
                "POST",
                "/api/integrations/buckets/discover",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
                json={"provider": provider, "credentials": credentials},
            ),
        )

    async def browse_cloud_storage_objects(
        self, id: str, *, target: str, prefix: str | None = None, cursor: str | None = None, owner: str | None = None
    ) -> AccountBrowseCloudStorageObjectsResponse:
        """Browse cloud storage objects.

        Args:
            id (str): id path parameter.
            target (str): Bucket or container name
            prefix (str, optional): Folder prefix
            cursor (str, optional): Provider pagination cursor
            owner (str, optional): Workspace username

        Returns:
            (AccountBrowseCloudStorageObjectsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountBrowseCloudStorageObjectsResponse,
            await self._client.request(
                "GET",
                f"/api/integrations/buckets/{_path_parameter(id, explode=False, allow_reserved=False)}/objects",
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("target", target, style="form", explode=True),
                    *_query_parameter("prefix", prefix, style="form", explode=True),
                    *_query_parameter("cursor", cursor, style="form", explode=True),
                    *_query_parameter("owner", owner, style="form", explode=True),
                ],
            ),
        )

    async def retrieve_trash(
        self,
        *,
        type: Literal["all", "project", "dataset", "model"] | None = None,
        page: int | None = None,
        limit: int | None = None,
        owner: str | None = None,
    ) -> AccountRetrieveTrashResponse:
        """View trash.

        Returns deleted items that can still be restored. Items are permanently deleted after 30 days.

        Args:
            type (Literal["all", "project", "dataset", "model"], optional): Resource type filter
            page (int, optional): Page number (default 1)
            limit (int, optional): Items per page (default 50)
            owner (str, optional): Workspace username

        Returns:
            (AccountRetrieveTrashResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountRetrieveTrashResponse,
            await self._client.request(
                "GET",
                "/api/trash",
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("type", type, style="form", explode=True),
                    *_query_parameter("page", page, style="form", explode=True),
                    *_query_parameter("limit", limit, style="form", explode=True),
                    *_query_parameter("owner", owner, style="form", explode=True),
                ],
            ),
        )

    async def restore_trashed_item(
        self, *, id: str, type: Literal["project", "dataset", "model"]
    ) -> AccountRestoreTrashedItemResponse:
        """Restore a trashed item.

        Args:
            id (str): id request value.
            type (Literal["project", "dataset", "model"]): type request value.

        Returns:
            (AccountRestoreTrashedItemResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountRestoreTrashedItemResponse,
            await self._client.request(
                "POST", "/api/trash", auth=("Authorization", "Bearer "), json={"id": id, "type": type}
            ),
        )

    async def permanently_delete_trashed_item(
        self, *, id: str, type: Literal["project", "dataset", "model"]
    ) -> AccountPermanentlyDeleteTrashedItemResponse:
        """Permanently delete a trashed item.

        Permanently deletes one trashed resource. This cannot be undone.

        Args:
            id (str): id request value.
            type (Literal["project", "dataset", "model"]): type request value.

        Returns:
            (AccountPermanentlyDeleteTrashedItemResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountPermanentlyDeleteTrashedItemResponse,
            await self._client.request(
                "DELETE", "/api/trash", auth=("Authorization", "Bearer "), json={"id": id, "type": type}
            ),
        )

    async def permanently_delete_all_trashed_items(
        self, *, owner: str | None = None
    ) -> AccountPermanentlyDeleteAllTrashedItemsResponse:
        """Permanently delete all trashed items.

        Permanently deletes everything in your trash. This cannot be undone.

        Args:
            owner (str, optional): Workspace username

        Returns:
            (AccountPermanentlyDeleteAllTrashedItemsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountPermanentlyDeleteAllTrashedItemsResponse,
            await self._client.request(
                "DELETE",
                "/api/trash/empty",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
            ),
        )

    async def retrieve_if_username_is_available(
        self, *, username: str, suggest: bool | None = None
    ) -> AccountRetrieveIfUsernameIsAvailableResponse:
        """Check if a username is available.

        Args:
            username (str): Username to check
            suggest (bool, optional): Return a suggestion if unavailable

        Returns:
            (AccountRetrieveIfUsernameIsAvailableResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountRetrieveIfUsernameIsAvailableResponse,
            await self._client.request(
                "GET",
                "/api/username/check",
                params=[
                    *_query_parameter("username", username, style="form", explode=True),
                    *_query_parameter("suggest", suggest, style="form", explode=True),
                ],
            ),
        )

    async def retrieve_public_user_profile(self, *, username: str) -> AccountRetrievePublicUserProfileResponse:
        """Get a public user profile.

        Args:
            username (str): Username to look up

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

    async def follow_or_unfollow_user(self, *, username: str, followed: bool) -> AccountFollowOrUnfollowUserResponse:
        """Follow or unfollow a user.

        Args:
            username (str): username request value.
            followed (bool): followed request value.

        Returns:
            (AccountFollowOrUnfollowUserResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountFollowOrUnfollowUserResponse,
            await self._client.request(
                "PATCH",
                "/api/users",
                auth=("Authorization", "Bearer "),
                json={"username": username, "followed": followed},
            ),
        )

    async def upload_workspace_icon(
        self,
        *,
        image: BinaryIO,
        owner: str | None = None,
        icon_color: str | NotGiven = NOT_GIVEN,
        icon_letter: str | NotGiven = NOT_GIVEN,
    ) -> AccountUploadWorkspaceIconResponse:
        """Upload a workspace icon.

        Args:
            owner (str, optional): Workspace username
            image (BinaryIO): WebP image, maximum 5 MB
            icon_color (str, optional): iconColor request value.
            icon_letter (str, optional): iconLetter request value.

        Returns:
            (AccountUploadWorkspaceIconResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountUploadWorkspaceIconResponse,
            await self._client.request(
                "POST",
                "/api/settings/icon",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
                data={"iconColor": icon_color, "iconLetter": icon_letter},
                files={"image": image},
            ),
        )

    async def delete_workspace_icon(self, *, owner: str | None = None) -> AccountDeleteWorkspaceIconResponse:
        """Delete a workspace icon.

        Args:
            owner (str, optional): Workspace username

        Returns:
            (AccountDeleteWorkspaceIconResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AccountDeleteWorkspaceIconResponse,
            await self._client.request(
                "DELETE",
                "/api/settings/icon",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
            ),
        )
