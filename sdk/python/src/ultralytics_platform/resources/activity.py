from __future__ import annotations

from typing import cast

from .._client import (
    NOT_GIVEN,
    AsyncAPIClient,
    NotGiven,
    SyncAPIClient,
    _query_parameter,
)
from ..types import (
    ActivityArchiveResponse,
    ActivityCreateMarkSeenResponse,
    ActivityListResponse,
)


class Activity:
    """Activity API operations."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(
        self,
        *,
        limit: float | None = None,
        page: float | None = None,
        archived: bool | None = None,
        search: str | None = None,
        start: str | None = None,
        end: str | None = None,
        export: bool | None = None,
        owner: str | None = None,
    ) -> ActivityListResponse:
        """View recent activity.

        Returns a feed of recent actions on your account — model training, dataset uploads, etc.

        Args:
            limit (float, optional): Number of events to return (default 20, max 100)
            page (float, optional): Page number (starts at 1)
            archived (bool, optional): Return archived instead of active events
            search (str, optional): Search by resource name or type
            start (str, optional): Earliest event timestamp
            end (str, optional): Latest event timestamp
            export (bool, optional): Download all matching events as JSON
            owner (str, optional): Workspace username

        Returns:
            (ActivityListResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ActivityListResponse,
            self._client.request(
                "GET",
                "/api/activity",
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("limit", limit, style="form", explode=True),
                    *_query_parameter("page", page, style="form", explode=True),
                    *_query_parameter("archived", archived, style="form", explode=True),
                    *_query_parameter("search", search, style="form", explode=True),
                    *_query_parameter("start", start, style="form", explode=True),
                    *_query_parameter("end", end, style="form", explode=True),
                    *_query_parameter("export", export, style="form", explode=True),
                    *_query_parameter("owner", owner, style="form", explode=True),
                ],
            ),
        )

    def create_mark_seen(
        self, *, owner: str | None = None, event_ids: list[str] | NotGiven = NOT_GIVEN, all: bool | NotGiven = NOT_GIVEN
    ) -> ActivityCreateMarkSeenResponse:
        """Mark notifications as read.

        Args:
            owner (str, optional): Workspace username
            event_ids (list[str], optional): eventIds request value.
            all (bool, optional): all request value.

        Returns:
            (ActivityCreateMarkSeenResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ActivityCreateMarkSeenResponse,
            self._client.request(
                "POST",
                "/api/activity/mark-seen",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
                json={"eventIds": event_ids, "all": all},
            ),
        )

    def archive(
        self,
        *,
        owner: str | None = None,
        event_ids: list[str] | NotGiven = NOT_GIVEN,
        archive: bool | NotGiven = NOT_GIVEN,
        all: bool | NotGiven = NOT_GIVEN,
    ) -> ActivityArchiveResponse:
        """Archive an activity event.

        Args:
            owner (str, optional): Workspace username
            event_ids (list[str], optional): eventIds request value.
            archive (bool, optional): archive request value.
            all (bool, optional): all request value.

        Returns:
            (ActivityArchiveResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ActivityArchiveResponse,
            self._client.request(
                "POST",
                "/api/activity/archive",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
                json={"eventIds": event_ids, "archive": archive, "all": all},
            ),
        )


class AsyncActivity:
    """Asynchronous Activity API operations."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(
        self,
        *,
        limit: float | None = None,
        page: float | None = None,
        archived: bool | None = None,
        search: str | None = None,
        start: str | None = None,
        end: str | None = None,
        export: bool | None = None,
        owner: str | None = None,
    ) -> ActivityListResponse:
        """View recent activity.

        Returns a feed of recent actions on your account — model training, dataset uploads, etc.

        Args:
            limit (float, optional): Number of events to return (default 20, max 100)
            page (float, optional): Page number (starts at 1)
            archived (bool, optional): Return archived instead of active events
            search (str, optional): Search by resource name or type
            start (str, optional): Earliest event timestamp
            end (str, optional): Latest event timestamp
            export (bool, optional): Download all matching events as JSON
            owner (str, optional): Workspace username

        Returns:
            (ActivityListResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ActivityListResponse,
            await self._client.request(
                "GET",
                "/api/activity",
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("limit", limit, style="form", explode=True),
                    *_query_parameter("page", page, style="form", explode=True),
                    *_query_parameter("archived", archived, style="form", explode=True),
                    *_query_parameter("search", search, style="form", explode=True),
                    *_query_parameter("start", start, style="form", explode=True),
                    *_query_parameter("end", end, style="form", explode=True),
                    *_query_parameter("export", export, style="form", explode=True),
                    *_query_parameter("owner", owner, style="form", explode=True),
                ],
            ),
        )

    async def create_mark_seen(
        self, *, owner: str | None = None, event_ids: list[str] | NotGiven = NOT_GIVEN, all: bool | NotGiven = NOT_GIVEN
    ) -> ActivityCreateMarkSeenResponse:
        """Mark notifications as read.

        Args:
            owner (str, optional): Workspace username
            event_ids (list[str], optional): eventIds request value.
            all (bool, optional): all request value.

        Returns:
            (ActivityCreateMarkSeenResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ActivityCreateMarkSeenResponse,
            await self._client.request(
                "POST",
                "/api/activity/mark-seen",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
                json={"eventIds": event_ids, "all": all},
            ),
        )

    async def archive(
        self,
        *,
        owner: str | None = None,
        event_ids: list[str] | NotGiven = NOT_GIVEN,
        archive: bool | NotGiven = NOT_GIVEN,
        all: bool | NotGiven = NOT_GIVEN,
    ) -> ActivityArchiveResponse:
        """Archive an activity event.

        Args:
            owner (str, optional): Workspace username
            event_ids (list[str], optional): eventIds request value.
            archive (bool, optional): archive request value.
            all (bool, optional): all request value.

        Returns:
            (ActivityArchiveResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ActivityArchiveResponse,
            await self._client.request(
                "POST",
                "/api/activity/archive",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
                json={"eventIds": event_ids, "archive": archive, "all": all},
            ),
        )
