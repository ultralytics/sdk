# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from __future__ import annotations

from typing import Any, cast

import httpx

from .._client import (
    NOT_GIVEN,
    AsyncAPIClient,
    NotGiven,
    SyncAPIClient,
    _query_parameter,
)
from ..types import (
    AgentsDeleteResponse,
    AgentsListResponse,
    AgentsSaveResponse,
)


class Agents:
    """Agents API operations."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(
        self,
        *,
        owner: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> AgentsListResponse:
        """List agents.

        Returns up to 100 saved agents, most recently updated first. Pass id to return that agent with its graph.

        Args:
            owner (str, optional): Workspace username; defaults to yours
            id (str, optional): Agent ID
            search (str, optional): search query parameter.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (AgentsListResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AgentsListResponse,
            self._client.request(
                "GET",
                "/api/workflows",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("owner", owner, style="form", explode=True),
                    *_query_parameter("id", id, style="form", explode=True),
                    *_query_parameter("search", search, style="form", explode=True),
                ],
            ),
        )

    def save(
        self,
        *,
        name: str,
        graph: dict[str, Any],
        version: int,
        owner: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> AgentsSaveResponse:
        """Save an agent.

        Creates an agent when id is omitted, or replaces the graph of the agent at version. Returns the block errors the Agents canvas shows; the agent is saved either way. Open it at /agents?workflow=<id>, where runs start.

        Args:
            owner (str, optional): Workspace username; defaults to yours
            id (str, optional): id request value.
            name (str): name request value.
            graph (dict[str, Any]): nodes[] are {id, type: "agent", position: {x, y}, data: {label, type, config}} with string or number config values; place each block 220 right of its input and branches 180 apart. edges[] are {id, source, target}; templateId is "". Dataset {dataset: slug or "official:coco8", split: train|val|test, maxInputs: up to 20 on free shared trials, 0 = all with a deployment} reads images; given an input, {dataset: slug} collects them. Image {dataset, image: image ID, name} is one dataset image; uploads happen on the canvas. YOLO {model: "ul://ultralytics/yolo26/yolo26n" (-seg, -pose, -obb, -cls suffixes) or ul://owner/project/model, task, conf?}; official models detect the 80 COCO classes. LLM {model: e.g. gemini-3.1-flash-lite-image, prompt} reads the image and upstream text. Gate {kind: "condition", path: "<YOLO or Deployment block id>.counts.<class>" or ".confidence.<class or *>", op: eq|ne|gt|gte|lt|lte|between, value, upper?} or {kind: "every", unit: frames|seconds, value}. Deployment {deployment: slug, conf?}. Export {model, format} stands alone. Output {}. Slack {message}. Webhook {url: HTTPS, body: JSON object as a string}. Messages and bodies insert the upstream result at "{output}". Each block has at most one input. Dataset and Image blocks start chains; Export, Output, Slack, and Webhook end them.
            version (int): Version being replaced; 0 creates the agent
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (AgentsSaveResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AgentsSaveResponse,
            self._client.request(
                "PUT",
                "/api/workflows",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
                json={"id": id, "name": name, "graph": graph, "version": version},
            ),
        )

    def delete(
        self,
        *,
        id: str,
        owner: str | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> AgentsDeleteResponse:
        """Delete an agent.

        Moves an agent to trash and cancels its active runs.

        Args:
            owner (str, optional): Workspace username; defaults to yours
            id (str): Agent ID
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (AgentsDeleteResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AgentsDeleteResponse,
            self._client.request(
                "DELETE",
                "/api/workflows",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("owner", owner, style="form", explode=True),
                    *_query_parameter("id", id, style="form", explode=True),
                ],
            ),
        )


class AsyncAgents:
    """Asynchronous Agents API operations."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(
        self,
        *,
        owner: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> AgentsListResponse:
        """List agents.

        Returns up to 100 saved agents, most recently updated first. Pass id to return that agent with its graph.

        Args:
            owner (str, optional): Workspace username; defaults to yours
            id (str, optional): Agent ID
            search (str, optional): search query parameter.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (AgentsListResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AgentsListResponse,
            await self._client.request(
                "GET",
                "/api/workflows",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("owner", owner, style="form", explode=True),
                    *_query_parameter("id", id, style="form", explode=True),
                    *_query_parameter("search", search, style="form", explode=True),
                ],
            ),
        )

    async def save(
        self,
        *,
        name: str,
        graph: dict[str, Any],
        version: int,
        owner: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> AgentsSaveResponse:
        """Save an agent.

        Creates an agent when id is omitted, or replaces the graph of the agent at version. Returns the block errors the Agents canvas shows; the agent is saved either way. Open it at /agents?workflow=<id>, where runs start.

        Args:
            owner (str, optional): Workspace username; defaults to yours
            id (str, optional): id request value.
            name (str): name request value.
            graph (dict[str, Any]): nodes[] are {id, type: "agent", position: {x, y}, data: {label, type, config}} with string or number config values; place each block 220 right of its input and branches 180 apart. edges[] are {id, source, target}; templateId is "". Dataset {dataset: slug or "official:coco8", split: train|val|test, maxInputs: up to 20 on free shared trials, 0 = all with a deployment} reads images; given an input, {dataset: slug} collects them. Image {dataset, image: image ID, name} is one dataset image; uploads happen on the canvas. YOLO {model: "ul://ultralytics/yolo26/yolo26n" (-seg, -pose, -obb, -cls suffixes) or ul://owner/project/model, task, conf?}; official models detect the 80 COCO classes. LLM {model: e.g. gemini-3.1-flash-lite-image, prompt} reads the image and upstream text. Gate {kind: "condition", path: "<YOLO or Deployment block id>.counts.<class>" or ".confidence.<class or *>", op: eq|ne|gt|gte|lt|lte|between, value, upper?} or {kind: "every", unit: frames|seconds, value}. Deployment {deployment: slug, conf?}. Export {model, format} stands alone. Output {}. Slack {message}. Webhook {url: HTTPS, body: JSON object as a string}. Messages and bodies insert the upstream result at "{output}". Each block has at most one input. Dataset and Image blocks start chains; Export, Output, Slack, and Webhook end them.
            version (int): Version being replaced; 0 creates the agent
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (AgentsSaveResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AgentsSaveResponse,
            await self._client.request(
                "PUT",
                "/api/workflows",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("owner", owner, style="form", explode=True)],
                json={"id": id, "name": name, "graph": graph, "version": version},
            ),
        )

    async def delete(
        self,
        *,
        id: str,
        owner: str | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> AgentsDeleteResponse:
        """Delete an agent.

        Moves an agent to trash and cancels its active runs.

        Args:
            owner (str, optional): Workspace username; defaults to yours
            id (str): Agent ID
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (AgentsDeleteResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            AgentsDeleteResponse,
            await self._client.request(
                "DELETE",
                "/api/workflows",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("owner", owner, style="form", explode=True),
                    *_query_parameter("id", id, style="form", explode=True),
                ],
            ),
        )
