# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from __future__ import annotations

from typing import Literal, cast

from .._client import (
    AsyncAPIClient,
    SyncAPIClient,
    _path_parameter,
    _query_parameter,
)
from ..types import (
    TeamsChangeMemberRoleResponse,
    TeamsCreateResponse,
    TeamsInviteResponse,
    TeamsListMembersResponse,
    TeamsListResponse,
    TeamsRemoveMemberOrLeaveResponse,
    TeamsTransferOwnershipResponse,
)


class Teams:
    """Teams API operations."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self) -> TeamsListResponse:
        """List your teams.

        Returns all teams you are a member of, along with your role in each.

        Returns:
            (TeamsListResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(TeamsListResponse, self._client.request("GET", "/api/teams", auth=("Authorization", "Bearer ")))

    def create(self, *, username: str, full_name: str) -> TeamsCreateResponse:
        """Create a new team.

        Creates a team workspace for collaboration. Limited to 5 teams per user. Teams start on the free plan.

        Args:
            username (str): Team username (globally unique across users and teams)
            full_name (str): Display name for the team

        Returns:
            (TeamsCreateResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            TeamsCreateResponse,
            self._client.request(
                "POST",
                "/api/teams/create",
                auth=("Authorization", "Bearer "),
                json={"username": username, "fullName": full_name},
            ),
        )

    def list_members(self, *, owner: str | None = None) -> TeamsListMembersResponse:
        """List team members.

        Returns active and pending members for a team workspace.

        Args:
            owner (str, optional): Team username

        Returns:
            (TeamsListMembersResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            TeamsListMembersResponse,
            self._client.request(
                "GET",
                "/api/members",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
            ),
        )

    def invite(
        self, *, email: str, role: Literal["admin", "editor", "viewer"], owner: str | None = None
    ) -> TeamsInviteResponse:
        """Invite someone to your team.

        Sends an email invitation to join your team workspace.

        Args:
            owner (str, optional): Team username
            email (str): email request value.
            role (Literal["admin", "editor", "viewer"]): Role to assign (owner cannot be invited)

        Returns:
            (TeamsInviteResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            TeamsInviteResponse,
            self._client.request(
                "POST",
                "/api/members",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
                json={"email": email, "role": role},
            ),
        )

    def change_member_role(
        self, user_id: str, *, role: Literal["admin", "editor", "viewer"], owner: str | None = None
    ) -> TeamsChangeMemberRoleResponse:
        """Change a member's role.

        Update a team member's role (viewer, editor, admin).

        Args:
            user_id (str): userId path parameter.
            owner (str, optional): Team username
            role (Literal["admin", "editor", "viewer"]): New role to assign

        Returns:
            (TeamsChangeMemberRoleResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            TeamsChangeMemberRoleResponse,
            self._client.request(
                "PATCH",
                f"/api/members/{_path_parameter(user_id, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
                json={"role": role},
            ),
        )

    def remove_member_or_leave(self, user_id: str, *, owner: str | None = None) -> TeamsRemoveMemberOrLeaveResponse:
        """Remove a member or leave a team.

        Removes a member from a team, or leaves the team when userId is your own user ID.

        Args:
            user_id (str): userId path parameter.
            owner (str, optional): Team username

        Returns:
            (TeamsRemoveMemberOrLeaveResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            TeamsRemoveMemberOrLeaveResponse,
            self._client.request(
                "DELETE",
                f"/api/members/{_path_parameter(user_id, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
            ),
        )

    def transfer_ownership(self, *, target_user_id: str, owner: str | None = None) -> TeamsTransferOwnershipResponse:
        """Transfer team ownership.

        Transfer ownership of a team workspace to another admin member.

        Args:
            owner (str, optional): Team username
            target_user_id (str): Clerk userId of the member to promote to owner

        Returns:
            (TeamsTransferOwnershipResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            TeamsTransferOwnershipResponse,
            self._client.request(
                "POST",
                "/api/members/transfer-ownership",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
                json={"targetUserId": target_user_id},
            ),
        )


class AsyncTeams:
    """Asynchronous Teams API operations."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self) -> TeamsListResponse:
        """List your teams.

        Returns all teams you are a member of, along with your role in each.

        Returns:
            (TeamsListResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            TeamsListResponse, await self._client.request("GET", "/api/teams", auth=("Authorization", "Bearer "))
        )

    async def create(self, *, username: str, full_name: str) -> TeamsCreateResponse:
        """Create a new team.

        Creates a team workspace for collaboration. Limited to 5 teams per user. Teams start on the free plan.

        Args:
            username (str): Team username (globally unique across users and teams)
            full_name (str): Display name for the team

        Returns:
            (TeamsCreateResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            TeamsCreateResponse,
            await self._client.request(
                "POST",
                "/api/teams/create",
                auth=("Authorization", "Bearer "),
                json={"username": username, "fullName": full_name},
            ),
        )

    async def list_members(self, *, owner: str | None = None) -> TeamsListMembersResponse:
        """List team members.

        Returns active and pending members for a team workspace.

        Args:
            owner (str, optional): Team username

        Returns:
            (TeamsListMembersResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            TeamsListMembersResponse,
            await self._client.request(
                "GET",
                "/api/members",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
            ),
        )

    async def invite(
        self, *, email: str, role: Literal["admin", "editor", "viewer"], owner: str | None = None
    ) -> TeamsInviteResponse:
        """Invite someone to your team.

        Sends an email invitation to join your team workspace.

        Args:
            owner (str, optional): Team username
            email (str): email request value.
            role (Literal["admin", "editor", "viewer"]): Role to assign (owner cannot be invited)

        Returns:
            (TeamsInviteResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            TeamsInviteResponse,
            await self._client.request(
                "POST",
                "/api/members",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
                json={"email": email, "role": role},
            ),
        )

    async def change_member_role(
        self, user_id: str, *, role: Literal["admin", "editor", "viewer"], owner: str | None = None
    ) -> TeamsChangeMemberRoleResponse:
        """Change a member's role.

        Update a team member's role (viewer, editor, admin).

        Args:
            user_id (str): userId path parameter.
            owner (str, optional): Team username
            role (Literal["admin", "editor", "viewer"]): New role to assign

        Returns:
            (TeamsChangeMemberRoleResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            TeamsChangeMemberRoleResponse,
            await self._client.request(
                "PATCH",
                f"/api/members/{_path_parameter(user_id, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
                json={"role": role},
            ),
        )

    async def remove_member_or_leave(
        self, user_id: str, *, owner: str | None = None
    ) -> TeamsRemoveMemberOrLeaveResponse:
        """Remove a member or leave a team.

        Removes a member from a team, or leaves the team when userId is your own user ID.

        Args:
            user_id (str): userId path parameter.
            owner (str, optional): Team username

        Returns:
            (TeamsRemoveMemberOrLeaveResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            TeamsRemoveMemberOrLeaveResponse,
            await self._client.request(
                "DELETE",
                f"/api/members/{_path_parameter(user_id, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
            ),
        )

    async def transfer_ownership(
        self, *, target_user_id: str, owner: str | None = None
    ) -> TeamsTransferOwnershipResponse:
        """Transfer team ownership.

        Transfer ownership of a team workspace to another admin member.

        Args:
            owner (str, optional): Team username
            target_user_id (str): Clerk userId of the member to promote to owner

        Returns:
            (TeamsTransferOwnershipResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            TeamsTransferOwnershipResponse,
            await self._client.request(
                "POST",
                "/api/members/transfer-ownership",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
                json={"targetUserId": target_user_id},
            ),
        )
