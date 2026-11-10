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
    ExploreSearchByImageResponse,
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
        type: Literal["all", "projects", "datasets", "images"] | NotGiven = NOT_GIVEN,
        sort: Literal["relevance", "stars", "newest", "oldest", "name-asc", "name-desc", "count-desc", "count-asc"]
        | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        task: str | NotGiven = NOT_GIVEN,
        license: str | NotGiven = NOT_GIVEN,
        author: str | NotGiven = NOT_GIVEN,
        starred: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        min_images: int | NotGiven = NOT_GIVEN,
        max_images: int | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ExploreSearchResponse:
        """Search public projects, datasets and images.

        Browse public content. `type=images` searches images by what they show, across public datasets plus the caller's own and team datasets. Without `q` or a photo, it lists one image from each of the newest public datasets, each scored 1. Authentication is used for the caller's starred filter and their own and team images.

        Args:
            q (str, optional): Search term
            type (Literal["all", "projects", "datasets", "images"], optional): Resource type filter; `images` searches image content (public, own and team datasets)
            sort (Literal["relevance", "stars", "newest", "oldest", "name-asc", "name-desc", "count-desc", "count-asc"], optional): Sort order; `relevance` ranks dataset matches for `q` by search score, otherwise lists the newest first
            offset (int, optional): Results to skip
            limit (int, optional): Maximum results per resource type
            task (str, optional): Comma-separated YOLO task filters
            license (str, optional): Comma-separated license filters for projects and datasets
            author (str, optional): Owner username filter
            starred (Literal["true", "false"], optional): Only content starred by the authenticated caller
            min_images (int, optional): Minimum dataset image count
            max_images (int, optional): Maximum dataset image count
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
                    *_query_parameter("license", license, style="form", explode=True),
                    *_query_parameter("author", author, style="form", explode=True),
                    *_query_parameter("starred", starred, style="form", explode=True),
                    *_query_parameter("minImages", min_images, style="form", explode=True),
                    *_query_parameter("maxImages", max_images, style="form", explode=True),
                ],
            ),
        )

    def search_by_image(
        self,
        *,
        sort: Literal["relevance", "stars", "newest", "oldest", "name-asc", "name-desc", "count-desc", "count-asc"]
        | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        task: str | NotGiven = NOT_GIVEN,
        license: str | NotGiven = NOT_GIVEN,
        author: str | NotGiven = NOT_GIVEN,
        starred: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        min_images: int | NotGiven = NOT_GIVEN,
        max_images: int | NotGiven = NOT_GIVEN,
        type: Literal["images", "datasets"] | NotGiven = NOT_GIVEN,
        image: str | NotGiven = NOT_GIVEN,
        vector: str | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ExploreSearchByImageResponse:
        """Search by image.

        Send a photo as `image` (never stored), then reuse its returned `vector` for pages, filters or switching `type` between images and public datasets. Dataset cards show matching images.

        Args:
            sort (Literal["relevance", "stars", "newest", "oldest", "name-asc", "name-desc", "count-desc", "count-asc"], optional): Sort order; `relevance` ranks dataset matches for `q` by search score, otherwise lists the newest first
            offset (int, optional): Results to skip
            limit (int, optional): Maximum results per resource type
            task (str, optional): Comma-separated YOLO task filters
            license (str, optional): Comma-separated license filters for projects and datasets
            author (str, optional): Owner username filter
            starred (Literal["true", "false"], optional): Only content starred by the authenticated caller
            min_images (int, optional): Minimum dataset image count
            max_images (int, optional): Maximum dataset image count
            type (Literal["images", "datasets"], optional): Return matching images or public datasets
            image (str, optional): Base64-encoded photo file, at most 3 MiB
            vector (str, optional): The first page's `vector`, in place of `image`
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (ExploreSearchByImageResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ExploreSearchByImageResponse,
            self._client.request(
                "POST",
                "/api/explore/search",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={
                    "sort": sort,
                    "offset": offset,
                    "limit": limit,
                    "task": task,
                    "license": license,
                    "author": author,
                    "starred": starred,
                    "minImages": min_images,
                    "maxImages": max_images,
                    "type": type,
                    "image": image,
                    "vector": vector,
                },
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
        type: Literal["all", "projects", "datasets", "images"] | NotGiven = NOT_GIVEN,
        sort: Literal["relevance", "stars", "newest", "oldest", "name-asc", "name-desc", "count-desc", "count-asc"]
        | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        task: str | NotGiven = NOT_GIVEN,
        license: str | NotGiven = NOT_GIVEN,
        author: str | NotGiven = NOT_GIVEN,
        starred: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        min_images: int | NotGiven = NOT_GIVEN,
        max_images: int | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ExploreSearchResponse:
        """Search public projects, datasets and images.

        Browse public content. `type=images` searches images by what they show, across public datasets plus the caller's own and team datasets. Without `q` or a photo, it lists one image from each of the newest public datasets, each scored 1. Authentication is used for the caller's starred filter and their own and team images.

        Args:
            q (str, optional): Search term
            type (Literal["all", "projects", "datasets", "images"], optional): Resource type filter; `images` searches image content (public, own and team datasets)
            sort (Literal["relevance", "stars", "newest", "oldest", "name-asc", "name-desc", "count-desc", "count-asc"], optional): Sort order; `relevance` ranks dataset matches for `q` by search score, otherwise lists the newest first
            offset (int, optional): Results to skip
            limit (int, optional): Maximum results per resource type
            task (str, optional): Comma-separated YOLO task filters
            license (str, optional): Comma-separated license filters for projects and datasets
            author (str, optional): Owner username filter
            starred (Literal["true", "false"], optional): Only content starred by the authenticated caller
            min_images (int, optional): Minimum dataset image count
            max_images (int, optional): Maximum dataset image count
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
                    *_query_parameter("license", license, style="form", explode=True),
                    *_query_parameter("author", author, style="form", explode=True),
                    *_query_parameter("starred", starred, style="form", explode=True),
                    *_query_parameter("minImages", min_images, style="form", explode=True),
                    *_query_parameter("maxImages", max_images, style="form", explode=True),
                ],
            ),
        )

    async def search_by_image(
        self,
        *,
        sort: Literal["relevance", "stars", "newest", "oldest", "name-asc", "name-desc", "count-desc", "count-asc"]
        | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        task: str | NotGiven = NOT_GIVEN,
        license: str | NotGiven = NOT_GIVEN,
        author: str | NotGiven = NOT_GIVEN,
        starred: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        min_images: int | NotGiven = NOT_GIVEN,
        max_images: int | NotGiven = NOT_GIVEN,
        type: Literal["images", "datasets"] | NotGiven = NOT_GIVEN,
        image: str | NotGiven = NOT_GIVEN,
        vector: str | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ExploreSearchByImageResponse:
        """Search by image.

        Send a photo as `image` (never stored), then reuse its returned `vector` for pages, filters or switching `type` between images and public datasets. Dataset cards show matching images.

        Args:
            sort (Literal["relevance", "stars", "newest", "oldest", "name-asc", "name-desc", "count-desc", "count-asc"], optional): Sort order; `relevance` ranks dataset matches for `q` by search score, otherwise lists the newest first
            offset (int, optional): Results to skip
            limit (int, optional): Maximum results per resource type
            task (str, optional): Comma-separated YOLO task filters
            license (str, optional): Comma-separated license filters for projects and datasets
            author (str, optional): Owner username filter
            starred (Literal["true", "false"], optional): Only content starred by the authenticated caller
            min_images (int, optional): Minimum dataset image count
            max_images (int, optional): Maximum dataset image count
            type (Literal["images", "datasets"], optional): Return matching images or public datasets
            image (str, optional): Base64-encoded photo file, at most 3 MiB
            vector (str, optional): The first page's `vector`, in place of `image`
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (ExploreSearchByImageResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ExploreSearchByImageResponse,
            await self._client.request(
                "POST",
                "/api/explore/search",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={
                    "sort": sort,
                    "offset": offset,
                    "limit": limit,
                    "task": task,
                    "license": license,
                    "author": author,
                    "starred": starred,
                    "minImages": min_images,
                    "maxImages": max_images,
                    "type": type,
                    "image": image,
                    "vector": vector,
                },
            ),
        )
