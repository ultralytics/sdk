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
        offset: int | None = None,
        limit: int | None = None,
        task: str | None = None,
        author: str | None = None,
        starred: Literal["true", "false"] | None = None,
    ) -> ExploreRetrieveSearchResponse:
        """Search public projects and datasets.

        Browse public content. Authentication is only used for the caller's starred filter.

        Args:
            q (str, optional): Search term
            type (Literal["all", "projects", "datasets"], optional): Resource type filter
            sort (Literal["stars", "newest", "oldest", "name-asc", "name-desc", "count-desc", "count-asc"], optional): Sort order
            offset (int, optional): Results to skip
            limit (int, optional): Maximum results per resource type
            task (str, optional): Comma-separated YOLO task filters
            author (str, optional): Owner username filter
            starred (Literal["true", "false"], optional): Only content starred by the authenticated caller

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
                    *_query_parameter("limit", limit, style="form", explode=True),
                    *_query_parameter("task", task, style="form", explode=True),
                    *_query_parameter("author", author, style="form", explode=True),
                    *_query_parameter("starred", starred, style="form", explode=True),
                ],
            ),
        )


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
        offset: int | None = None,
        limit: int | None = None,
        task: str | None = None,
        author: str | None = None,
        starred: Literal["true", "false"] | None = None,
    ) -> ExploreRetrieveSearchResponse:
        """Search public projects and datasets.

        Browse public content. Authentication is only used for the caller's starred filter.

        Args:
            q (str, optional): Search term
            type (Literal["all", "projects", "datasets"], optional): Resource type filter
            sort (Literal["stars", "newest", "oldest", "name-asc", "name-desc", "count-desc", "count-asc"], optional): Sort order
            offset (int, optional): Results to skip
            limit (int, optional): Maximum results per resource type
            task (str, optional): Comma-separated YOLO task filters
            author (str, optional): Owner username filter
            starred (Literal["true", "false"], optional): Only content starred by the authenticated caller

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
                    *_query_parameter("limit", limit, style="form", explode=True),
                    *_query_parameter("task", task, style="form", explode=True),
                    *_query_parameter("author", author, style="form", explode=True),
                    *_query_parameter("starred", starred, style="form", explode=True),
                ],
            ),
        )
