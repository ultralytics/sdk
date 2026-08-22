# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal, cast

import httpx

from .._client import (
    NOT_GIVEN,
    AsyncAPIClient,
    NotGiven,
    SyncAPIClient,
    _path_parameter,
    _query_parameter,
)
from ..types import (
    ProjectsCloneResponse,
    ProjectsCreateResponse,
    ProjectsDeleteResponse,
    ProjectsListResponse,
    ProjectsRetrieveResponse,
    ProjectsUpdateResponse,
)


class Projects:
    """Projects API operations."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def clone(
        self,
        owner: str,
        project: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        visibility: Literal["public", "private"] | NotGiven = NOT_GIVEN,
        owner_body: str | NotGiven = NOT_GIVEN,
        project_body: str | NotGiven = NOT_GIVEN,
        license: Literal[
            "None",
            "Apache-2.0",
            "MIT",
            "BSD-3-Clause",
            "AGPL-3.0",
            "GPL-3.0",
            "LGPL-3.0",
            "MPL-2.0",
            "EUPL-1.1",
            "Unlicense",
            "CC0-1.0",
            "Ultralytics-Enterprise",
            "Other",
        ]
        | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ProjectsCloneResponse:
        """Clone a project.

        Copies an accessible project and its completed models into an account or editable workspace.

        Args:
            owner (str): Project owner
            project (str): Project name
            name (str, optional): name request value.
            description (str, optional): description request value.
            visibility (Literal["public", "private"], optional): Resource visibility
            owner_body (str, optional): Destination owner
            project_body (str, optional): Name for the cloned project
            license (Literal["None", "Apache-2.0", "MIT", "BSD-3-Clause", "AGPL-3.0", "GPL-3.0", "LGPL-3.0", "MPL-2.0", "EUPL-1.1", "Unlicense", "CC0-1.0", "Ultralytics-Enterprise", "Other"], optional): Project/model license identifier
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (ProjectsCloneResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ProjectsCloneResponse,
            self._client.request(
                "POST",
                f"/api/projects/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}/clone",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={
                    "name": name,
                    "description": description,
                    "visibility": visibility,
                    "owner": owner_body,
                    "project": project_body,
                    "license": license,
                },
            ),
        )

    def retrieve(
        self,
        owner: str,
        project: str,
        *,
        search: str | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ProjectsRetrieveResponse:
        """Get a project.

        Returns a project and its model summaries by owner and project name.

        Args:
            owner (str): Project owner
            project (str): Project name
            search (str, optional): Model name or metadata search
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (ProjectsRetrieveResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ProjectsRetrieveResponse,
            self._client.request(
                "GET",
                f"/api/projects/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("search", search, style="form", explode=True)],
            ),
        )

    def update(
        self,
        owner: str,
        project: str,
        *,
        starred: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        metadata: dict[str, Any] | NotGiven = NOT_GIVEN,
        visibility: Literal["public", "private"] | NotGiven = NOT_GIVEN,
        tags: Sequence[str] | NotGiven = NOT_GIVEN,
        license: Literal[
            "None",
            "Apache-2.0",
            "MIT",
            "BSD-3-Clause",
            "AGPL-3.0",
            "GPL-3.0",
            "LGPL-3.0",
            "MPL-2.0",
            "EUPL-1.1",
            "Unlicense",
            "CC0-1.0",
            "Ultralytics-Enterprise",
            "Other",
        ]
        | NotGiven = NOT_GIVEN,
        archived: bool | NotGiven = NOT_GIVEN,
        icon_color: str | NotGiven = NOT_GIVEN,
        icon_letter: str | Literal[""] | None | NotGiven = NOT_GIVEN,
        view_preferences: dict[str, Any] | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ProjectsUpdateResponse:
        """Update a project.

        Updates project properties. Changing the display name also changes the project name used in URLs.

        Args:
            owner (str): Project owner
            project (str): Project name
            starred (bool, optional): starred request value.
            name (str, optional): name request value.
            description (str, optional): description request value.
            metadata (dict[str, Any], optional): Custom JSON metadata with keys limited to 128 characters and at most 500,000 serialized characters.
            visibility (Literal["public", "private"], optional): Resource visibility
            tags (Sequence[str], optional): tags request value.
            license (Literal["None", "Apache-2.0", "MIT", "BSD-3-Clause", "AGPL-3.0", "GPL-3.0", "LGPL-3.0", "MPL-2.0", "EUPL-1.1", "Unlicense", "CC0-1.0", "Ultralytics-Enterprise", "Other"], optional): Project/model license identifier
            archived (bool, optional): archived request value.
            icon_color (str, optional): iconColor request value.
            icon_letter (str | Literal[""] | None, optional): iconLetter request value.
            view_preferences (dict[str, Any], optional): Shared project-level model view defaults
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (ProjectsUpdateResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ProjectsUpdateResponse,
            self._client.request(
                "PATCH",
                f"/api/projects/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={
                    "starred": starred,
                    "name": name,
                    "description": description,
                    "metadata": metadata,
                    "visibility": visibility,
                    "tags": tags,
                    "license": license,
                    "archived": archived,
                    "iconColor": icon_color,
                    "iconLetter": icon_letter,
                    "viewPreferences": view_preferences,
                },
            ),
        )

    def delete(
        self,
        owner: str,
        project: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ProjectsDeleteResponse:
        """Delete a project.

        Moves a project and its models to trash for 30 days.

        Args:
            owner (str): Project owner
            project (str): Project name
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (ProjectsDeleteResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ProjectsDeleteResponse,
            self._client.request(
                "DELETE",
                f"/api/projects/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    def list(
        self,
        owner: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ProjectsListResponse:
        """List an owner's projects.

        Returns public projects, plus private projects when the caller can view the owner's workspace.

        Args:
            owner (str): Project owner
            limit (int, optional): Maximum projects to return
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (ProjectsListResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ProjectsListResponse,
            self._client.request(
                "GET",
                f"/api/projects/{_path_parameter(owner, explode=False, allow_reserved=False)}",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("limit", limit, style="form", explode=True)],
            ),
        )

    def create(
        self,
        *,
        project: str,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        metadata: dict[str, Any] | NotGiven = NOT_GIVEN,
        visibility: Literal["public", "private"] | NotGiven = NOT_GIVEN,
        tags: Sequence[str] | NotGiven = NOT_GIVEN,
        license: Literal[
            "None",
            "Apache-2.0",
            "MIT",
            "BSD-3-Clause",
            "AGPL-3.0",
            "GPL-3.0",
            "LGPL-3.0",
            "MPL-2.0",
            "EUPL-1.1",
            "Unlicense",
            "CC0-1.0",
            "Ultralytics-Enterprise",
            "Other",
        ]
        | NotGiven = NOT_GIVEN,
        owner: str | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ProjectsCreateResponse:
        """Create a project.

        Creates a project for organizing models in an account or editable workspace.

        Args:
            project (str): Project name used in Platform URLs
            name (str): Display name
            description (str, optional): description request value.
            metadata (dict[str, Any], optional): Custom JSON metadata with keys limited to 128 characters and at most 500,000 serialized characters.
            visibility (Literal["public", "private"], optional): Resource visibility
            tags (Sequence[str], optional): tags request value.
            license (Literal["None", "Apache-2.0", "MIT", "BSD-3-Clause", "AGPL-3.0", "GPL-3.0", "LGPL-3.0", "MPL-2.0", "EUPL-1.1", "Unlicense", "CC0-1.0", "Ultralytics-Enterprise", "Other"], optional): Project/model license identifier
            owner (str, optional): Workspace owner
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (ProjectsCreateResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ProjectsCreateResponse,
            self._client.request(
                "POST",
                "/api/projects",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={
                    "project": project,
                    "name": name,
                    "description": description,
                    "metadata": metadata,
                    "visibility": visibility,
                    "tags": tags,
                    "license": license,
                    "owner": owner,
                },
            ),
        )


class AsyncProjects:
    """Asynchronous Projects API operations."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def clone(
        self,
        owner: str,
        project: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        visibility: Literal["public", "private"] | NotGiven = NOT_GIVEN,
        owner_body: str | NotGiven = NOT_GIVEN,
        project_body: str | NotGiven = NOT_GIVEN,
        license: Literal[
            "None",
            "Apache-2.0",
            "MIT",
            "BSD-3-Clause",
            "AGPL-3.0",
            "GPL-3.0",
            "LGPL-3.0",
            "MPL-2.0",
            "EUPL-1.1",
            "Unlicense",
            "CC0-1.0",
            "Ultralytics-Enterprise",
            "Other",
        ]
        | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ProjectsCloneResponse:
        """Clone a project.

        Copies an accessible project and its completed models into an account or editable workspace.

        Args:
            owner (str): Project owner
            project (str): Project name
            name (str, optional): name request value.
            description (str, optional): description request value.
            visibility (Literal["public", "private"], optional): Resource visibility
            owner_body (str, optional): Destination owner
            project_body (str, optional): Name for the cloned project
            license (Literal["None", "Apache-2.0", "MIT", "BSD-3-Clause", "AGPL-3.0", "GPL-3.0", "LGPL-3.0", "MPL-2.0", "EUPL-1.1", "Unlicense", "CC0-1.0", "Ultralytics-Enterprise", "Other"], optional): Project/model license identifier
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (ProjectsCloneResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ProjectsCloneResponse,
            await self._client.request(
                "POST",
                f"/api/projects/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}/clone",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={
                    "name": name,
                    "description": description,
                    "visibility": visibility,
                    "owner": owner_body,
                    "project": project_body,
                    "license": license,
                },
            ),
        )

    async def retrieve(
        self,
        owner: str,
        project: str,
        *,
        search: str | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ProjectsRetrieveResponse:
        """Get a project.

        Returns a project and its model summaries by owner and project name.

        Args:
            owner (str): Project owner
            project (str): Project name
            search (str, optional): Model name or metadata search
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (ProjectsRetrieveResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ProjectsRetrieveResponse,
            await self._client.request(
                "GET",
                f"/api/projects/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("search", search, style="form", explode=True)],
            ),
        )

    async def update(
        self,
        owner: str,
        project: str,
        *,
        starred: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        metadata: dict[str, Any] | NotGiven = NOT_GIVEN,
        visibility: Literal["public", "private"] | NotGiven = NOT_GIVEN,
        tags: Sequence[str] | NotGiven = NOT_GIVEN,
        license: Literal[
            "None",
            "Apache-2.0",
            "MIT",
            "BSD-3-Clause",
            "AGPL-3.0",
            "GPL-3.0",
            "LGPL-3.0",
            "MPL-2.0",
            "EUPL-1.1",
            "Unlicense",
            "CC0-1.0",
            "Ultralytics-Enterprise",
            "Other",
        ]
        | NotGiven = NOT_GIVEN,
        archived: bool | NotGiven = NOT_GIVEN,
        icon_color: str | NotGiven = NOT_GIVEN,
        icon_letter: str | Literal[""] | None | NotGiven = NOT_GIVEN,
        view_preferences: dict[str, Any] | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ProjectsUpdateResponse:
        """Update a project.

        Updates project properties. Changing the display name also changes the project name used in URLs.

        Args:
            owner (str): Project owner
            project (str): Project name
            starred (bool, optional): starred request value.
            name (str, optional): name request value.
            description (str, optional): description request value.
            metadata (dict[str, Any], optional): Custom JSON metadata with keys limited to 128 characters and at most 500,000 serialized characters.
            visibility (Literal["public", "private"], optional): Resource visibility
            tags (Sequence[str], optional): tags request value.
            license (Literal["None", "Apache-2.0", "MIT", "BSD-3-Clause", "AGPL-3.0", "GPL-3.0", "LGPL-3.0", "MPL-2.0", "EUPL-1.1", "Unlicense", "CC0-1.0", "Ultralytics-Enterprise", "Other"], optional): Project/model license identifier
            archived (bool, optional): archived request value.
            icon_color (str, optional): iconColor request value.
            icon_letter (str | Literal[""] | None, optional): iconLetter request value.
            view_preferences (dict[str, Any], optional): Shared project-level model view defaults
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (ProjectsUpdateResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ProjectsUpdateResponse,
            await self._client.request(
                "PATCH",
                f"/api/projects/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={
                    "starred": starred,
                    "name": name,
                    "description": description,
                    "metadata": metadata,
                    "visibility": visibility,
                    "tags": tags,
                    "license": license,
                    "archived": archived,
                    "iconColor": icon_color,
                    "iconLetter": icon_letter,
                    "viewPreferences": view_preferences,
                },
            ),
        )

    async def delete(
        self,
        owner: str,
        project: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ProjectsDeleteResponse:
        """Delete a project.

        Moves a project and its models to trash for 30 days.

        Args:
            owner (str): Project owner
            project (str): Project name
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (ProjectsDeleteResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ProjectsDeleteResponse,
            await self._client.request(
                "DELETE",
                f"/api/projects/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    async def list(
        self,
        owner: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ProjectsListResponse:
        """List an owner's projects.

        Returns public projects, plus private projects when the caller can view the owner's workspace.

        Args:
            owner (str): Project owner
            limit (int, optional): Maximum projects to return
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (ProjectsListResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ProjectsListResponse,
            await self._client.request(
                "GET",
                f"/api/projects/{_path_parameter(owner, explode=False, allow_reserved=False)}",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("limit", limit, style="form", explode=True)],
            ),
        )

    async def create(
        self,
        *,
        project: str,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        metadata: dict[str, Any] | NotGiven = NOT_GIVEN,
        visibility: Literal["public", "private"] | NotGiven = NOT_GIVEN,
        tags: Sequence[str] | NotGiven = NOT_GIVEN,
        license: Literal[
            "None",
            "Apache-2.0",
            "MIT",
            "BSD-3-Clause",
            "AGPL-3.0",
            "GPL-3.0",
            "LGPL-3.0",
            "MPL-2.0",
            "EUPL-1.1",
            "Unlicense",
            "CC0-1.0",
            "Ultralytics-Enterprise",
            "Other",
        ]
        | NotGiven = NOT_GIVEN,
        owner: str | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ProjectsCreateResponse:
        """Create a project.

        Creates a project for organizing models in an account or editable workspace.

        Args:
            project (str): Project name used in Platform URLs
            name (str): Display name
            description (str, optional): description request value.
            metadata (dict[str, Any], optional): Custom JSON metadata with keys limited to 128 characters and at most 500,000 serialized characters.
            visibility (Literal["public", "private"], optional): Resource visibility
            tags (Sequence[str], optional): tags request value.
            license (Literal["None", "Apache-2.0", "MIT", "BSD-3-Clause", "AGPL-3.0", "GPL-3.0", "LGPL-3.0", "MPL-2.0", "EUPL-1.1", "Unlicense", "CC0-1.0", "Ultralytics-Enterprise", "Other"], optional): Project/model license identifier
            owner (str, optional): Workspace owner
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (ProjectsCreateResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ProjectsCreateResponse,
            await self._client.request(
                "POST",
                "/api/projects",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={
                    "project": project,
                    "name": name,
                    "description": description,
                    "metadata": metadata,
                    "visibility": visibility,
                    "tags": tags,
                    "license": license,
                    "owner": owner,
                },
            ),
        )
