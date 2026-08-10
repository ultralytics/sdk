# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from __future__ import annotations

from typing import Literal, cast

from .._client import (
    AsyncAPIClient,
    SyncAPIClient,
    _query_parameter,
)
from ..types import (
    ExploreRetrieveSearchResponse,
    ExploreRetrieveSidebarResponse,
)


class Explore:
    """Explore API operations."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def retrieve_search(
        self,
        *,
        q: str | None = None,
        type: Literal["all", "projects", "datasets"] | None = None,
        sort: Literal["stars", "newest", "oldest", "name-asc", "name-desc", "count-desc", "count-asc"] | None = None,
        offset: float | None = None,
        task: str | None = None,
        author: str | None = None,
        starred: bool | None = None,
    ) -> ExploreRetrieveSearchResponse:
        """Search public projects and datasets.

        Browse public content. Authentication is optional and used only for the caller's starred filter.

        Args:
            q (str, optional): Search term
            type (Literal["all", "projects", "datasets"], optional): Resource type filter
            sort (Literal["stars", "newest", "oldest", "name-asc", "name-desc", "count-desc", "count-asc"], optional): Sort order
            offset (float, optional): Skip this many results for pagination
            task (str, optional): Comma-separated YOLO task filters
            author (str, optional): Owner username filter
            starred (bool, optional): Return content starred by the authenticated caller

        Returns:
            (ExploreRetrieveSearchResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ExploreRetrieveSearchResponse,
            self._client.request(
                "GET",
                "/api/explore/search",
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("q", q, style="form", explode=True),
                    *_query_parameter("type", type, style="form", explode=True),
                    *_query_parameter("sort", sort, style="form", explode=True),
                    *_query_parameter("offset", offset, style="form", explode=True),
                    *_query_parameter("task", task, style="form", explode=True),
                    *_query_parameter("author", author, style="form", explode=True),
                    *_query_parameter("starred", starred, style="form", explode=True),
                ],
            ),
        )

    def retrieve_sidebar(self) -> ExploreRetrieveSidebarResponse:
        """Get curated public resources.

        Returns:
            (ExploreRetrieveSidebarResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(ExploreRetrieveSidebarResponse, self._client.request("GET", "/api/explore/sidebar"))


class AsyncExplore:
    """Asynchronous Explore API operations."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def retrieve_search(
        self,
        *,
        q: str | None = None,
        type: Literal["all", "projects", "datasets"] | None = None,
        sort: Literal["stars", "newest", "oldest", "name-asc", "name-desc", "count-desc", "count-asc"] | None = None,
        offset: float | None = None,
        task: str | None = None,
        author: str | None = None,
        starred: bool | None = None,
    ) -> ExploreRetrieveSearchResponse:
        """Search public projects and datasets.

        Browse public content. Authentication is optional and used only for the caller's starred filter.

        Args:
            q (str, optional): Search term
            type (Literal["all", "projects", "datasets"], optional): Resource type filter
            sort (Literal["stars", "newest", "oldest", "name-asc", "name-desc", "count-desc", "count-asc"], optional): Sort order
            offset (float, optional): Skip this many results for pagination
            task (str, optional): Comma-separated YOLO task filters
            author (str, optional): Owner username filter
            starred (bool, optional): Return content starred by the authenticated caller

        Returns:
            (ExploreRetrieveSearchResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ExploreRetrieveSearchResponse,
            await self._client.request(
                "GET",
                "/api/explore/search",
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("q", q, style="form", explode=True),
                    *_query_parameter("type", type, style="form", explode=True),
                    *_query_parameter("sort", sort, style="form", explode=True),
                    *_query_parameter("offset", offset, style="form", explode=True),
                    *_query_parameter("task", task, style="form", explode=True),
                    *_query_parameter("author", author, style="form", explode=True),
                    *_query_parameter("starred", starred, style="form", explode=True),
                ],
            ),
        )

    async def retrieve_sidebar(self) -> ExploreRetrieveSidebarResponse:
        """Get curated public resources.

        Returns:
            (ExploreRetrieveSidebarResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(ExploreRetrieveSidebarResponse, await self._client.request("GET", "/api/explore/sidebar"))
