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
    ProjectsCloneResponse,
    ProjectsCreateResponse,
    ProjectsDeleteResponse,
    ProjectsListResponse,
    ProjectsRetrieveMetadataResponse,
    ProjectsRetrieveResponse,
    ProjectsUpdateResponse,
)


class Projects:
    """Projects API operations."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(
        self, *, limit: float | None = None, owner: str | None = None, region: Literal["us", "eu", "ap"] | None = None
    ) -> ProjectsListResponse:
        """List your projects.

        Returns your projects with pagination.

        Args:
            limit (float, optional): Number of results to return (default 20, max 500)
            owner (str, optional): Team workspace to browse
            region (Literal["us", "eu", "ap"], optional): Data region: us, eu, or ap

        Returns:
            (ProjectsListResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ProjectsListResponse,
            self._client.request(
                "GET",
                "/api/projects",
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("limit", limit, style="form", explode=True),
                    *_query_parameter("owner", owner, style="form", explode=True),
                    *_query_parameter("region", region, style="form", explode=True),
                ],
            ),
        )

    def create(
        self,
        *,
        slug: str,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        metadata: dict[str, Any] | NotGiven = NOT_GIVEN,
        visibility: Literal["public", "private"] | NotGiven = NOT_GIVEN,
        tags: list[str] | NotGiven = NOT_GIVEN,
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
    ) -> ProjectsCreateResponse:
        """Create a new project.

        Projects organize your models. Each model belongs to exactly one project.

        Args:
            slug (str): URL slug
            name (str): Resource name
            description (str, optional): Resource description
            metadata (dict[str, Any], optional): Custom metadata object. Top-level keys are limited to 128 characters and the serialized object is limited to 500,000 characters.
            visibility (Literal["public", "private"], optional): Resource visibility
            tags (list[str], optional): Resource tags
            license (Literal["None", "Apache-2.0", "MIT", "BSD-3-Clause", "AGPL-3.0", "GPL-3.0", "LGPL-3.0", "MPL-2.0", "EUPL-1.1", "Unlicense", "CC0-1.0", "Ultralytics-Enterprise", "Other"], optional): Project/model license identifier
            owner (str, optional): Team owner username (creates resource in their workspace)

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
                auth=("Authorization", "Bearer "),
                json={
                    "slug": slug,
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

    def retrieve(self, project_id: str) -> ProjectsRetrieveResponse:
        """Get project details.

        Returns one project and its model summary by project ID.

        Args:
            project_id (str): Project ID

        Returns:
            (ProjectsRetrieveResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ProjectsRetrieveResponse,
            self._client.request(
                "GET",
                f"/api/projects/{_path_parameter(project_id, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
            ),
        )

    def update(
        self,
        project_id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        metadata: dict[str, Any] | NotGiven = NOT_GIVEN,
        visibility: Literal["public", "private"] | NotGiven = NOT_GIVEN,
        tags: list[str] | NotGiven = NOT_GIVEN,
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
    ) -> ProjectsUpdateResponse:
        """Update a project.

        Update project properties like name, description, metadata, visibility, or tags.

        Args:
            project_id (str): Project ID
            name (str, optional): Resource name
            description (str, optional): Resource description
            metadata (dict[str, Any], optional): Custom metadata object. Top-level keys are limited to 128 characters and the serialized object is limited to 500,000 characters.
            visibility (Literal["public", "private"], optional): Resource visibility
            tags (list[str], optional): Resource tags
            license (Literal["None", "Apache-2.0", "MIT", "BSD-3-Clause", "AGPL-3.0", "GPL-3.0", "LGPL-3.0", "MPL-2.0", "EUPL-1.1", "Unlicense", "CC0-1.0", "Ultralytics-Enterprise", "Other"], optional): Project/model license identifier
            archived (bool, optional): Whether the resource is archived
            icon_color (str, optional): Icon color
            icon_letter (str | Literal[""] | None, optional): Icon letter
            view_preferences (dict[str, Any], optional): Shared project-level model view defaults

        Returns:
            (ProjectsUpdateResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ProjectsUpdateResponse,
            self._client.request(
                "PATCH",
                f"/api/projects/{_path_parameter(project_id, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
                json={
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

    def delete(self, project_id: str) -> ProjectsDeleteResponse:
        """Delete a project.

        Moves the project and all its models to trash. Can be restored within 30 days.

        Args:
            project_id (str): Project ID

        Returns:
            (ProjectsDeleteResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ProjectsDeleteResponse,
            self._client.request(
                "DELETE",
                f"/api/projects/{_path_parameter(project_id, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
            ),
        )

    def retrieve_metadata(self, project_id: str) -> ProjectsRetrieveMetadataResponse:
        """Get project metadata.

        Returns custom metadata and Ultralytics-managed properties without adding them to normal payloads.

        Args:
            project_id (str): Project ID

        Returns:
            (ProjectsRetrieveMetadataResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ProjectsRetrieveMetadataResponse,
            self._client.request(
                "GET",
                f"/api/projects/{_path_parameter(project_id, explode=False, allow_reserved=False)}/metadata",
                auth=("Authorization", "Bearer "),
            ),
        )

    def clone(
        self,
        project_id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        slug: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        visibility: Literal["public", "private"] | NotGiven = NOT_GIVEN,
        license: str | NotGiven = NOT_GIVEN,
        owner: str | NotGiven = NOT_GIVEN,
    ) -> ProjectsCloneResponse:
        """Clone an accessible project.

        Copies a public, owned, or shared project and its models into your account or a workspace.

        Args:
            project_id (str): Project ID
            name (str, optional): Resource name
            slug (str, optional): URL slug
            description (str, optional): Resource description
            visibility (Literal["public", "private"], optional): Resource visibility
            license (str, optional): License identifier
            owner (str, optional): Workspace username

        Returns:
            (ProjectsCloneResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ProjectsCloneResponse,
            self._client.request(
                "POST",
                f"/api/projects/{_path_parameter(project_id, explode=False, allow_reserved=False)}/clone",
                auth=("Authorization", "Bearer "),
                json={
                    "name": name,
                    "slug": slug,
                    "description": description,
                    "visibility": visibility,
                    "license": license,
                    "owner": owner,
                },
            ),
        )


class AsyncProjects:
    """Asynchronous Projects API operations."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(
        self, *, limit: float | None = None, owner: str | None = None, region: Literal["us", "eu", "ap"] | None = None
    ) -> ProjectsListResponse:
        """List your projects.

        Returns your projects with pagination.

        Args:
            limit (float, optional): Number of results to return (default 20, max 500)
            owner (str, optional): Team workspace to browse
            region (Literal["us", "eu", "ap"], optional): Data region: us, eu, or ap

        Returns:
            (ProjectsListResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ProjectsListResponse,
            await self._client.request(
                "GET",
                "/api/projects",
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("limit", limit, style="form", explode=True),
                    *_query_parameter("owner", owner, style="form", explode=True),
                    *_query_parameter("region", region, style="form", explode=True),
                ],
            ),
        )

    async def create(
        self,
        *,
        slug: str,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        metadata: dict[str, Any] | NotGiven = NOT_GIVEN,
        visibility: Literal["public", "private"] | NotGiven = NOT_GIVEN,
        tags: list[str] | NotGiven = NOT_GIVEN,
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
    ) -> ProjectsCreateResponse:
        """Create a new project.

        Projects organize your models. Each model belongs to exactly one project.

        Args:
            slug (str): URL slug
            name (str): Resource name
            description (str, optional): Resource description
            metadata (dict[str, Any], optional): Custom metadata object. Top-level keys are limited to 128 characters and the serialized object is limited to 500,000 characters.
            visibility (Literal["public", "private"], optional): Resource visibility
            tags (list[str], optional): Resource tags
            license (Literal["None", "Apache-2.0", "MIT", "BSD-3-Clause", "AGPL-3.0", "GPL-3.0", "LGPL-3.0", "MPL-2.0", "EUPL-1.1", "Unlicense", "CC0-1.0", "Ultralytics-Enterprise", "Other"], optional): Project/model license identifier
            owner (str, optional): Team owner username (creates resource in their workspace)

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
                auth=("Authorization", "Bearer "),
                json={
                    "slug": slug,
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

    async def retrieve(self, project_id: str) -> ProjectsRetrieveResponse:
        """Get project details.

        Returns one project and its model summary by project ID.

        Args:
            project_id (str): Project ID

        Returns:
            (ProjectsRetrieveResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ProjectsRetrieveResponse,
            await self._client.request(
                "GET",
                f"/api/projects/{_path_parameter(project_id, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
            ),
        )

    async def update(
        self,
        project_id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        metadata: dict[str, Any] | NotGiven = NOT_GIVEN,
        visibility: Literal["public", "private"] | NotGiven = NOT_GIVEN,
        tags: list[str] | NotGiven = NOT_GIVEN,
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
    ) -> ProjectsUpdateResponse:
        """Update a project.

        Update project properties like name, description, metadata, visibility, or tags.

        Args:
            project_id (str): Project ID
            name (str, optional): Resource name
            description (str, optional): Resource description
            metadata (dict[str, Any], optional): Custom metadata object. Top-level keys are limited to 128 characters and the serialized object is limited to 500,000 characters.
            visibility (Literal["public", "private"], optional): Resource visibility
            tags (list[str], optional): Resource tags
            license (Literal["None", "Apache-2.0", "MIT", "BSD-3-Clause", "AGPL-3.0", "GPL-3.0", "LGPL-3.0", "MPL-2.0", "EUPL-1.1", "Unlicense", "CC0-1.0", "Ultralytics-Enterprise", "Other"], optional): Project/model license identifier
            archived (bool, optional): Whether the resource is archived
            icon_color (str, optional): Icon color
            icon_letter (str | Literal[""] | None, optional): Icon letter
            view_preferences (dict[str, Any], optional): Shared project-level model view defaults

        Returns:
            (ProjectsUpdateResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ProjectsUpdateResponse,
            await self._client.request(
                "PATCH",
                f"/api/projects/{_path_parameter(project_id, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
                json={
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

    async def delete(self, project_id: str) -> ProjectsDeleteResponse:
        """Delete a project.

        Moves the project and all its models to trash. Can be restored within 30 days.

        Args:
            project_id (str): Project ID

        Returns:
            (ProjectsDeleteResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ProjectsDeleteResponse,
            await self._client.request(
                "DELETE",
                f"/api/projects/{_path_parameter(project_id, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
            ),
        )

    async def retrieve_metadata(self, project_id: str) -> ProjectsRetrieveMetadataResponse:
        """Get project metadata.

        Returns custom metadata and Ultralytics-managed properties without adding them to normal payloads.

        Args:
            project_id (str): Project ID

        Returns:
            (ProjectsRetrieveMetadataResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ProjectsRetrieveMetadataResponse,
            await self._client.request(
                "GET",
                f"/api/projects/{_path_parameter(project_id, explode=False, allow_reserved=False)}/metadata",
                auth=("Authorization", "Bearer "),
            ),
        )

    async def clone(
        self,
        project_id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        slug: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        visibility: Literal["public", "private"] | NotGiven = NOT_GIVEN,
        license: str | NotGiven = NOT_GIVEN,
        owner: str | NotGiven = NOT_GIVEN,
    ) -> ProjectsCloneResponse:
        """Clone an accessible project.

        Copies a public, owned, or shared project and its models into your account or a workspace.

        Args:
            project_id (str): Project ID
            name (str, optional): Resource name
            slug (str, optional): URL slug
            description (str, optional): Resource description
            visibility (Literal["public", "private"], optional): Resource visibility
            license (str, optional): License identifier
            owner (str, optional): Workspace username

        Returns:
            (ProjectsCloneResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ProjectsCloneResponse,
            await self._client.request(
                "POST",
                f"/api/projects/{_path_parameter(project_id, explode=False, allow_reserved=False)}/clone",
                auth=("Authorization", "Bearer "),
                json={
                    "name": name,
                    "slug": slug,
                    "description": description,
                    "visibility": visibility,
                    "license": license,
                    "owner": owner,
                },
            ),
        )
