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
    ExploreSearchResponse,
)


class Explore:
    """Explore API operations."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def search(
        self,
        *,
        q: str | NotGiven = NOT_GIVEN,
        type: Literal["all", "projects", "datasets"] | NotGiven = NOT_GIVEN,
        sort: Literal["stars", "newest", "oldest", "name-asc", "name-desc", "count-desc", "count-asc"]
        | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        task: str | NotGiven = NOT_GIVEN,
        author: str | NotGiven = NOT_GIVEN,
        starred: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ExploreSearchResponse:
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
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (ExploreSearchResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ExploreSearchResponse,
            self._client.request(
                "GET",
                "/api/explore/search",
                timeout=timeout,
                extra_headers=extra_headers,
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

    async def search(
        self,
        *,
        q: str | NotGiven = NOT_GIVEN,
        type: Literal["all", "projects", "datasets"] | NotGiven = NOT_GIVEN,
        sort: Literal["stars", "newest", "oldest", "name-asc", "name-desc", "count-desc", "count-asc"]
        | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        task: str | NotGiven = NOT_GIVEN,
        author: str | NotGiven = NOT_GIVEN,
        starred: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ExploreSearchResponse:
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
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (ExploreSearchResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ExploreSearchResponse,
            await self._client.request(
                "GET",
                "/api/explore/search",
                timeout=timeout,
                extra_headers=extra_headers,
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
