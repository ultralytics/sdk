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
    DatasetsBatchResponse,
    DatasetsClassStatsResponse,
    DatasetsCloneResponse,
    DatasetsClusteringResponse,
    DatasetsCreateBatchResponse,
    DatasetsCreateEmbeddingsResponse,
    DatasetsCreateExportResponse,
    DatasetsCreateResponse,
    DatasetsDeleteBatchResponse,
    DatasetsDeleteClassesResponse,
    DatasetsDeleteEmbeddingsResponse,
    DatasetsDeleteResponse,
    DatasetsEmbeddingsResponse,
    DatasetsExportResponse,
    DatasetsImagesResponse,
    DatasetsImportRoboflowResponse,
    DatasetsIngestResponse,
    DatasetsListResponse,
    DatasetsMergeClassesResponse,
    DatasetsModelsResponse,
    DatasetsPreviewRoboflowResponse,
    DatasetsRedistributeSplitsResponse,
    DatasetsRestoreResponse,
    DatasetsRetrieveResponse,
    DatasetsSelectedImagesResponse,
    DatasetsUpdateExportResponse,
    DatasetsUpdateResponse,
)


class Datasets:
    """Datasets API operations."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def class_stats(
        self,
        owner: str,
        dataset: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsClassStatsResponse:
        """Get dataset statistics.

        Returns class counts, image distributions, and annotation heatmaps.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsClassStatsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsClassStatsResponse,
            self._client.request(
                "GET",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/class-stats",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    def delete_classes(
        self,
        owner: str,
        dataset: str,
        *,
        class_ids: Sequence[int],
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsDeleteClassesResponse:
        """Delete dataset classes.

        Deletes annotations in the selected classes, removes the classes, and shifts remaining class IDs.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            class_ids (Sequence[int]): classIds request value.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsDeleteClassesResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsDeleteClassesResponse,
            self._client.request(
                "POST",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/classes/delete",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={"classIds": class_ids},
            ),
        )

    def merge_classes(
        self,
        owner: str,
        dataset: str,
        *,
        source_class_ids: Sequence[int],
        target_class_id: int,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsMergeClassesResponse:
        """Merge dataset classes.

        Reassigns annotations to one target class and removes the source classes.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            source_class_ids (Sequence[int]): sourceClassIds request value.
            target_class_id (int): targetClassId request value.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsMergeClassesResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsMergeClassesResponse,
            self._client.request(
                "POST",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/classes/merge",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={"sourceClassIds": source_class_ids, "targetClassId": target_class_id},
            ),
        )

    def clone(
        self,
        owner: str,
        dataset: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        dataset_body: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        visibility: Literal["public", "private"] | NotGiven = NOT_GIVEN,
        license: Literal[
            "None",
            "CC0-1.0",
            "PDM-1.0",
            "CC-BY-2.5",
            "CC-BY-3.0",
            "CC-BY-4.0",
            "CC-BY-NC-2.0",
            "CC-BY-NC-3.0",
            "CC-BY-NC-4.0",
            "CC-BY-SA-3.0",
            "CC-BY-SA-4.0",
            "CC-BY-NC-SA-3.0",
            "CC-BY-NC-SA-4.0",
            "CC-BY-ND-4.0",
            "CC-BY-NC-ND-2.0",
            "CC-BY-NC-ND-4.0",
            "Apache-2.0",
            "MIT",
            "BSD-3-Clause",
            "AGPL-3.0",
            "GPL-2.0",
            "GPL-3.0",
            "LGPL-3.0",
            "ODbL-1.0",
            "DbCL-1.0",
            "Research-Only",
            "Other",
        ]
        | NotGiven = NOT_GIVEN,
        owner_body: str | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsCloneResponse:
        """Clone a dataset.

        Copies an accessible dataset into your personal workspace or a team workspace.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            name (str, optional): name request value.
            dataset_body (str, optional): Name for the cloned dataset
            description (str, optional): description request value.
            visibility (Literal["public", "private"], optional): Resource visibility
            license (Literal["None", "CC0-1.0", "PDM-1.0", "CC-BY-2.5", "CC-BY-3.0", "CC-BY-4.0", "CC-BY-NC-2.0", "CC-BY-NC-3.0", "CC-BY-NC-4.0", "CC-BY-SA-3.0", "CC-BY-SA-4.0", "CC-BY-NC-SA-3.0", "CC-BY-NC-SA-4.0", "CC-BY-ND-4.0", "CC-BY-NC-ND-2.0", "CC-BY-NC-ND-4.0", "Apache-2.0", "MIT", "BSD-3-Clause", "AGPL-3.0", "GPL-2.0", "GPL-3.0", "LGPL-3.0", "ODbL-1.0", "DbCL-1.0", "Research-Only", "Other"], optional): Dataset license identifier
            owner_body (str, optional): Destination owner
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsCloneResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsCloneResponse,
            self._client.request(
                "POST",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/clone",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={
                    "name": name,
                    "dataset": dataset_body,
                    "description": description,
                    "visibility": visibility,
                    "license": license,
                    "owner": owner_body,
                },
            ),
        )

    def retrieve(
        self,
        owner: str,
        dataset: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsRetrieveResponse:
        """Get a dataset.

        Returns a dataset by owner and dataset name.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsRetrieveResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsRetrieveResponse,
            self._client.request(
                "GET",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    def update(
        self,
        owner: str,
        dataset: str,
        *,
        starred: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        metadata: dict[str, Any] | NotGiven = NOT_GIVEN,
        visibility: Literal["public", "private"] | NotGiven = NOT_GIVEN,
        tags: Sequence[str] | NotGiven = NOT_GIVEN,
        class_names: Sequence[str] | NotGiven = NOT_GIVEN,
        class_colors: dict[str, Any] | NotGiven = NOT_GIVEN,
        format: Literal["yolo", "coco", "raw", "ndjson"] | NotGiven = NOT_GIVEN,
        task: Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"] | NotGiven = NOT_GIVEN,
        license: Literal[
            "None",
            "CC0-1.0",
            "PDM-1.0",
            "CC-BY-2.5",
            "CC-BY-3.0",
            "CC-BY-4.0",
            "CC-BY-NC-2.0",
            "CC-BY-NC-3.0",
            "CC-BY-NC-4.0",
            "CC-BY-SA-3.0",
            "CC-BY-SA-4.0",
            "CC-BY-NC-SA-3.0",
            "CC-BY-NC-SA-4.0",
            "CC-BY-ND-4.0",
            "CC-BY-NC-ND-2.0",
            "CC-BY-NC-ND-4.0",
            "Apache-2.0",
            "MIT",
            "BSD-3-Clause",
            "AGPL-3.0",
            "GPL-2.0",
            "GPL-3.0",
            "LGPL-3.0",
            "ODbL-1.0",
            "DbCL-1.0",
            "Research-Only",
            "Other",
        ]
        | NotGiven = NOT_GIVEN,
        icon_color: str | NotGiven = NOT_GIVEN,
        icon_letter: str | Literal[""] | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsUpdateResponse:
        """Update a dataset.

        Updates dataset properties. Changing the display name also changes the dataset name used in URLs.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            starred (bool, optional): starred request value.
            name (str, optional): name request value.
            description (str, optional): description request value.
            metadata (dict[str, Any], optional): Custom JSON metadata with keys limited to 128 characters and at most 500,000 serialized characters.
            visibility (Literal["public", "private"], optional): Resource visibility
            tags (Sequence[str], optional): tags request value.
            class_names (Sequence[str], optional): classNames request value.
            class_colors (dict[str, Any], optional): classColors request value.
            format (Literal["yolo", "coco", "raw", "ndjson"], optional): Dataset annotation format
            task (Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"], optional): Dataset task type
            license (Literal["None", "CC0-1.0", "PDM-1.0", "CC-BY-2.5", "CC-BY-3.0", "CC-BY-4.0", "CC-BY-NC-2.0", "CC-BY-NC-3.0", "CC-BY-NC-4.0", "CC-BY-SA-3.0", "CC-BY-SA-4.0", "CC-BY-NC-SA-3.0", "CC-BY-NC-SA-4.0", "CC-BY-ND-4.0", "CC-BY-NC-ND-2.0", "CC-BY-NC-ND-4.0", "Apache-2.0", "MIT", "BSD-3-Clause", "AGPL-3.0", "GPL-2.0", "GPL-3.0", "LGPL-3.0", "ODbL-1.0", "DbCL-1.0", "Research-Only", "Other"], optional): Dataset license identifier
            icon_color (str, optional): iconColor request value.
            icon_letter (str | Literal[""], optional): iconLetter request value.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsUpdateResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsUpdateResponse,
            self._client.request(
                "PATCH",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}",
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
                    "classNames": class_names,
                    "classColors": class_colors,
                    "format": format,
                    "task": task,
                    "license": license,
                    "iconColor": icon_color,
                    "iconLetter": icon_letter,
                },
            ),
        )

    def delete(
        self,
        owner: str,
        dataset: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsDeleteResponse:
        """Delete a dataset.

        Moves a dataset to trash for 30 days.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsDeleteResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsDeleteResponse,
            self._client.request(
                "DELETE",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    def embeddings(
        self,
        owner: str,
        dataset: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsEmbeddingsResponse:
        """Get dataset analysis status.

        Returns embedding analysis status, progress, and freshness.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsEmbeddingsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsEmbeddingsResponse,
            self._client.request(
                "GET",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/embeddings",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    def create_embeddings(
        self,
        owner: str,
        dataset: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsCreateEmbeddingsResponse:
        """Analyze dataset embeddings.

        Starts embedding extraction and clustering.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsCreateEmbeddingsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsCreateEmbeddingsResponse,
            self._client.request(
                "POST",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/embeddings",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    def delete_embeddings(
        self,
        owner: str,
        dataset: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsDeleteEmbeddingsResponse:
        """Cancel dataset analysis.

        Cancels the active embedding analysis job, if present.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsDeleteEmbeddingsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsDeleteEmbeddingsResponse,
            self._client.request(
                "DELETE",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/embeddings",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    def export(
        self,
        owner: str,
        dataset: str,
        *,
        v: int | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsExportResponse:
        """Download a dataset export.

        Returns a signed URL for the current dataset or a saved version snapshot.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            v (int, optional): Saved version number
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsExportResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsExportResponse,
            self._client.request(
                "GET",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/export",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("v", v, style="form", explode=True)],
            ),
        )

    def create_export(
        self,
        owner: str,
        dataset: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsCreateExportResponse:
        """Create a dataset version.

        Creates an immutable numbered snapshot and returns its signed NDJSON download URL.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            description (str, optional): description request value.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsCreateExportResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsCreateExportResponse,
            self._client.request(
                "POST",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/export",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={"description": description},
            ),
        )

    def update_export(
        self,
        owner: str,
        dataset: str,
        *,
        version: int,
        description: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsUpdateExportResponse:
        """Update a dataset version description.

        Updates the description stored on an existing saved dataset version.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            version (int): version request value.
            description (str): description request value.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsUpdateExportResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsUpdateExportResponse,
            self._client.request(
                "PATCH",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/export",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={"version": version, "description": description},
            ),
        )

    def clustering(
        self,
        owner: str,
        dataset: str,
        *,
        offset: int | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsClusteringResponse:
        """Get dataset clustering layout.

        Returns paginated image coordinates from a completed dataset analysis.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            offset (int, optional): offset query parameter.
            limit (int, optional): limit query parameter.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsClusteringResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsClusteringResponse,
            self._client.request(
                "GET",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/images/clustering",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("offset", offset, style="form", explode=True),
                    *_query_parameter("limit", limit, style="form", explode=True),
                ],
            ),
        )

    def images(
        self,
        owner: str,
        dataset: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        include_total: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        split: Literal["train", "val", "test"] | NotGiven = NOT_GIVEN,
        has_error: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        has_label: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        class_ids: str | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        sort: Literal[
            "newest",
            "oldest",
            "name-asc",
            "name-desc",
            "height-asc",
            "height-desc",
            "width-asc",
            "width-desc",
            "size-asc",
            "size-desc",
            "labels-desc",
            "labels-asc",
        ]
        | NotGiven = NOT_GIVEN,
        include_thumbnails: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        include_image_urls: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        include_labels: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsImagesResponse:
        """List dataset images.

        Returns paginated images. Capped preview annotations are included only when requested.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            limit (int, optional): Maximum images to return
            offset (int, optional): Images to skip
            cursor (str, optional): Last image ID from the previous page
            include_total (Literal["true", "false"], optional): Include the total matching image count
            split (Literal["train", "val", "test"], optional): Dataset split
            has_error (Literal["true", "false"], optional): Filter by processing error state
            has_label (Literal["true", "false"], optional): Filter by annotation state
            class_ids (str, optional): Comma-separated class IDs; empty matches no images
            search (str, optional): Image name or metadata search
            sort (Literal["newest", "oldest", "name-asc", "name-desc", "height-asc", "height-desc", "width-asc", "width-desc", "size-asc", "size-desc", "labels-desc", "labels-asc"], optional): Sort order
            include_thumbnails (Literal["true", "false"], optional): Include signed thumbnail URLs
            include_image_urls (Literal["true", "false"], optional): Include signed full-size image URLs
            include_labels (Literal["true", "false"], optional): Include capped preview annotations
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsImagesResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsImagesResponse,
            self._client.request(
                "GET",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/images",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("limit", limit, style="form", explode=True),
                    *_query_parameter("offset", offset, style="form", explode=True),
                    *_query_parameter("cursor", cursor, style="form", explode=True),
                    *_query_parameter("includeTotal", include_total, style="form", explode=True),
                    *_query_parameter("split", split, style="form", explode=True),
                    *_query_parameter("hasError", has_error, style="form", explode=True),
                    *_query_parameter("hasLabel", has_label, style="form", explode=True),
                    *_query_parameter("classIds", class_ids, style="form", explode=True),
                    *_query_parameter("search", search, style="form", explode=True),
                    *_query_parameter("sort", sort, style="form", explode=True),
                    *_query_parameter("includeThumbnails", include_thumbnails, style="form", explode=True),
                    *_query_parameter("includeImageUrls", include_image_urls, style="form", explode=True),
                    *_query_parameter("includeLabels", include_labels, style="form", explode=True),
                ],
            ),
        )

    def selected_images(
        self,
        owner: str,
        dataset: str,
        *,
        image_ids: Sequence[str],
        split: Literal["train", "val", "test"] | NotGiven = NOT_GIVEN,
        has_error: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        has_label: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        class_ids: str | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        sort: Literal[
            "newest",
            "oldest",
            "name-asc",
            "name-desc",
            "height-asc",
            "height-desc",
            "width-asc",
            "width-desc",
            "size-asc",
            "size-desc",
            "labels-desc",
            "labels-asc",
        ]
        | NotGiven = NOT_GIVEN,
        include_thumbnails: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        include_image_urls: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        include_labels: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsSelectedImagesResponse:
        """Get selected dataset images.

        Returns the requested images with optional signed URLs and capped preview annotations.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            split (Literal["train", "val", "test"], optional): Dataset split
            has_error (Literal["true", "false"], optional): Filter by processing error state
            has_label (Literal["true", "false"], optional): Filter by annotation state
            class_ids (str, optional): Comma-separated class IDs; empty matches no images
            search (str, optional): Image name or metadata search
            sort (Literal["newest", "oldest", "name-asc", "name-desc", "height-asc", "height-desc", "width-asc", "width-desc", "size-asc", "size-desc", "labels-desc", "labels-asc"], optional): Sort order
            include_thumbnails (Literal["true", "false"], optional): Include signed thumbnail URLs
            include_image_urls (Literal["true", "false"], optional): Include signed full-size image URLs
            include_labels (Literal["true", "false"], optional): Include capped preview annotations
            image_ids (Sequence[str]): imageIds request value.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsSelectedImagesResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsSelectedImagesResponse,
            self._client.request(
                "POST",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/images",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("split", split, style="form", explode=True),
                    *_query_parameter("hasError", has_error, style="form", explode=True),
                    *_query_parameter("hasLabel", has_label, style="form", explode=True),
                    *_query_parameter("classIds", class_ids, style="form", explode=True),
                    *_query_parameter("search", search, style="form", explode=True),
                    *_query_parameter("sort", sort, style="form", explode=True),
                    *_query_parameter("includeThumbnails", include_thumbnails, style="form", explode=True),
                    *_query_parameter("includeImageUrls", include_image_urls, style="form", explode=True),
                    *_query_parameter("includeLabels", include_labels, style="form", explode=True),
                ],
                json={"imageIds": image_ids},
            ),
        )

    def ingest(
        self,
        owner: str,
        dataset: str,
        *,
        body: dict[str, Any],
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsIngestResponse:
        """Ingest dataset data.

        Processes a completed upload, remote archive, or connected data source into this dataset.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            body (dict[str, Any]): Input for dataset ingest job
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsIngestResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsIngestResponse,
            self._client.request(
                "POST",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/ingest",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json=body,
            ),
        )

    def models(
        self,
        owner: str,
        dataset: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsModelsResponse:
        """List models trained on a dataset.

        Returns accessible models whose training data references this dataset.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsModelsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsModelsResponse,
            self._client.request(
                "GET",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/models",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    def batch(
        self,
        owner: str,
        dataset: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsBatchResponse:
        """Get auto-annotation run status.

        Returns the dataset's in-flight auto-annotation run and its progress, or the last finished run awaiting dismissal.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsBatchResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsBatchResponse,
            self._client.request(
                "GET",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/predict/batch",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    def create_batch(
        self,
        owner: str,
        dataset: str,
        *,
        model_id: str,
        confidence: float | NotGiven = NOT_GIVEN,
        iou: float | NotGiven = NOT_GIVEN,
        class_mapping: Sequence[int | None] | NotGiven = NOT_GIVEN,
        include_annotated: bool | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsCreateBatchResponse:
        """Auto-annotate a dataset.

        Saves a dataset version, then queues a run that labels the dataset's unlabeled images with the given model, or every image when `includeAnnotated` is set. Existing labels are never changed, and the run is billed for the images it actually processes.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            model_id (str): Fully qualified model URI
            confidence (float, optional): Confidence threshold
            iou (float, optional): IoU threshold for non-maximum suppression
            class_mapping (Sequence[int | None], optional): Dataset class index for each model class, or null to drop it
            include_annotated (bool, optional): Also annotate images that already have labels, keeping the labels they have
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsCreateBatchResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsCreateBatchResponse,
            self._client.request(
                "POST",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/predict/batch",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={
                    "modelId": model_id,
                    "confidence": confidence,
                    "iou": iou,
                    "classMapping": class_mapping,
                    "includeAnnotated": include_annotated,
                },
            ),
        )

    def delete_batch(
        self,
        owner: str,
        dataset: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsDeleteBatchResponse:
        """Cancel or dismiss an auto-annotation run.

        Cancels an in-flight run, or settles billing and dismisses its terminal summary.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsDeleteBatchResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsDeleteBatchResponse,
            self._client.request(
                "DELETE",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/predict/batch",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    def restore(
        self,
        owner: str,
        dataset: str,
        *,
        version: int,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsRestoreResponse:
        """Restore a saved dataset version.

        Restores dataset files, labels, and metadata from a previously saved version.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            version (int): version request value.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsRestoreResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsRestoreResponse,
            self._client.request(
                "POST",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/restore",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={"version": version},
            ),
        )

    def redistribute_splits(
        self,
        owner: str,
        dataset: str,
        *,
        train: int,
        val: int,
        test: int,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsRedistributeSplitsResponse:
        """Redistribute dataset splits.

        Randomly reassigns images using train, validation, and test percentages that total 100.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            train (int): Train split percentage
            val (int): Validation split percentage
            test (int): Test split percentage
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsRedistributeSplitsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsRedistributeSplitsResponse,
            self._client.request(
                "POST",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/splits/redistribute",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={"train": train, "val": val, "test": test},
            ),
        )

    def list(
        self,
        owner: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        include_samples: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        include_image_urls: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsListResponse:
        """List datasets.

        Returns datasets owned by the named owner. Private datasets require workspace access.

        Args:
            owner (str): Dataset owner
            limit (int, optional): Maximum datasets to return
            include_samples (Literal["true", "false"], optional): Include sample image previews
            include_image_urls (Literal["true", "false"], optional): Include full-size sample image fallback URLs
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsListResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsListResponse,
            self._client.request(
                "GET",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("limit", limit, style="form", explode=True),
                    *_query_parameter("includeSamples", include_samples, style="form", explode=True),
                    *_query_parameter("includeImageUrls", include_image_urls, style="form", explode=True),
                ],
            ),
        )

    def create(
        self,
        *,
        dataset: str,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        metadata: dict[str, Any] | NotGiven = NOT_GIVEN,
        visibility: Literal["public", "private"] | NotGiven = NOT_GIVEN,
        task: Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"] | NotGiven = NOT_GIVEN,
        image_count: int | NotGiven = NOT_GIVEN,
        class_names: Sequence[str] | NotGiven = NOT_GIVEN,
        format: Literal["yolo", "coco", "raw", "ndjson"] | NotGiven = NOT_GIVEN,
        tags: Sequence[str] | NotGiven = NOT_GIVEN,
        license: Literal[
            "None",
            "CC0-1.0",
            "PDM-1.0",
            "CC-BY-2.5",
            "CC-BY-3.0",
            "CC-BY-4.0",
            "CC-BY-NC-2.0",
            "CC-BY-NC-3.0",
            "CC-BY-NC-4.0",
            "CC-BY-SA-3.0",
            "CC-BY-SA-4.0",
            "CC-BY-NC-SA-3.0",
            "CC-BY-NC-SA-4.0",
            "CC-BY-ND-4.0",
            "CC-BY-NC-ND-2.0",
            "CC-BY-NC-ND-4.0",
            "Apache-2.0",
            "MIT",
            "BSD-3-Clause",
            "AGPL-3.0",
            "GPL-2.0",
            "GPL-3.0",
            "LGPL-3.0",
            "ODbL-1.0",
            "DbCL-1.0",
            "Research-Only",
            "Other",
        ]
        | NotGiven = NOT_GIVEN,
        require_exact_slug: bool | NotGiven = NOT_GIVEN,
        owner: str | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsCreateResponse:
        """Create a dataset.

        Creates an empty dataset in your personal workspace or a team workspace.

        Args:
            dataset (str): Dataset name used in Platform URLs
            name (str): Display name
            description (str, optional): description request value.
            metadata (dict[str, Any], optional): Custom JSON metadata with keys limited to 128 characters and at most 500,000 serialized characters.
            visibility (Literal["public", "private"], optional): Resource visibility
            task (Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"], optional): Dataset task type
            image_count (int, optional): imageCount request value.
            class_names (Sequence[str], optional): classNames request value.
            format (Literal["yolo", "coco", "raw", "ndjson"], optional): Dataset annotation format
            tags (Sequence[str], optional): tags request value.
            license (Literal["None", "CC0-1.0", "PDM-1.0", "CC-BY-2.5", "CC-BY-3.0", "CC-BY-4.0", "CC-BY-NC-2.0", "CC-BY-NC-3.0", "CC-BY-NC-4.0", "CC-BY-SA-3.0", "CC-BY-SA-4.0", "CC-BY-NC-SA-3.0", "CC-BY-NC-SA-4.0", "CC-BY-ND-4.0", "CC-BY-NC-ND-2.0", "CC-BY-NC-ND-4.0", "Apache-2.0", "MIT", "BSD-3-Clause", "AGPL-3.0", "GPL-2.0", "GPL-3.0", "LGPL-3.0", "ODbL-1.0", "DbCL-1.0", "Research-Only", "Other"], optional): Dataset license identifier
            require_exact_slug (bool, optional): Reject a slug conflict instead of creating an automatically suffixed dataset
            owner (str, optional): Workspace owner
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsCreateResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsCreateResponse,
            self._client.request(
                "POST",
                "/api/datasets",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={
                    "dataset": dataset,
                    "name": name,
                    "description": description,
                    "metadata": metadata,
                    "visibility": visibility,
                    "task": task,
                    "imageCount": image_count,
                    "classNames": class_names,
                    "format": format,
                    "tags": tags,
                    "license": license,
                    "requireExactSlug": require_exact_slug,
                    "owner": owner,
                },
            ),
        )

    def import_roboflow(
        self,
        *,
        api_key: str,
        items: Sequence[dict[str, Any]],
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsImportRoboflowResponse:
        """Import datasets from Roboflow.

        Imports selected Roboflow dataset versions into the API key's workspace.

        Args:
            api_key (str): Roboflow API key
            items (Sequence[dict[str, Any]]): items request value.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsImportRoboflowResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsImportRoboflowResponse,
            self._client.request(
                "POST",
                "/api/integrations/roboflow/import",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={"apiKey": api_key, "items": items},
            ),
        )

    def preview_roboflow(
        self, *, api_key: str, timeout: float | httpx.Timeout | None = None, extra_headers: dict[str, str] | None = None
    ) -> DatasetsPreviewRoboflowResponse:
        """Preview a Roboflow import.

        Validates a Roboflow API key and lists datasets available for import.

        Args:
            api_key (str): Roboflow API key
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsPreviewRoboflowResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsPreviewRoboflowResponse,
            self._client.request(
                "POST",
                "/api/integrations/roboflow/preview",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={"apiKey": api_key},
            ),
        )


class AsyncDatasets:
    """Asynchronous Datasets API operations."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def class_stats(
        self,
        owner: str,
        dataset: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsClassStatsResponse:
        """Get dataset statistics.

        Returns class counts, image distributions, and annotation heatmaps.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsClassStatsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsClassStatsResponse,
            await self._client.request(
                "GET",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/class-stats",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    async def delete_classes(
        self,
        owner: str,
        dataset: str,
        *,
        class_ids: Sequence[int],
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsDeleteClassesResponse:
        """Delete dataset classes.

        Deletes annotations in the selected classes, removes the classes, and shifts remaining class IDs.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            class_ids (Sequence[int]): classIds request value.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsDeleteClassesResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsDeleteClassesResponse,
            await self._client.request(
                "POST",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/classes/delete",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={"classIds": class_ids},
            ),
        )

    async def merge_classes(
        self,
        owner: str,
        dataset: str,
        *,
        source_class_ids: Sequence[int],
        target_class_id: int,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsMergeClassesResponse:
        """Merge dataset classes.

        Reassigns annotations to one target class and removes the source classes.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            source_class_ids (Sequence[int]): sourceClassIds request value.
            target_class_id (int): targetClassId request value.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsMergeClassesResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsMergeClassesResponse,
            await self._client.request(
                "POST",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/classes/merge",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={"sourceClassIds": source_class_ids, "targetClassId": target_class_id},
            ),
        )

    async def clone(
        self,
        owner: str,
        dataset: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        dataset_body: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        visibility: Literal["public", "private"] | NotGiven = NOT_GIVEN,
        license: Literal[
            "None",
            "CC0-1.0",
            "PDM-1.0",
            "CC-BY-2.5",
            "CC-BY-3.0",
            "CC-BY-4.0",
            "CC-BY-NC-2.0",
            "CC-BY-NC-3.0",
            "CC-BY-NC-4.0",
            "CC-BY-SA-3.0",
            "CC-BY-SA-4.0",
            "CC-BY-NC-SA-3.0",
            "CC-BY-NC-SA-4.0",
            "CC-BY-ND-4.0",
            "CC-BY-NC-ND-2.0",
            "CC-BY-NC-ND-4.0",
            "Apache-2.0",
            "MIT",
            "BSD-3-Clause",
            "AGPL-3.0",
            "GPL-2.0",
            "GPL-3.0",
            "LGPL-3.0",
            "ODbL-1.0",
            "DbCL-1.0",
            "Research-Only",
            "Other",
        ]
        | NotGiven = NOT_GIVEN,
        owner_body: str | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsCloneResponse:
        """Clone a dataset.

        Copies an accessible dataset into your personal workspace or a team workspace.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            name (str, optional): name request value.
            dataset_body (str, optional): Name for the cloned dataset
            description (str, optional): description request value.
            visibility (Literal["public", "private"], optional): Resource visibility
            license (Literal["None", "CC0-1.0", "PDM-1.0", "CC-BY-2.5", "CC-BY-3.0", "CC-BY-4.0", "CC-BY-NC-2.0", "CC-BY-NC-3.0", "CC-BY-NC-4.0", "CC-BY-SA-3.0", "CC-BY-SA-4.0", "CC-BY-NC-SA-3.0", "CC-BY-NC-SA-4.0", "CC-BY-ND-4.0", "CC-BY-NC-ND-2.0", "CC-BY-NC-ND-4.0", "Apache-2.0", "MIT", "BSD-3-Clause", "AGPL-3.0", "GPL-2.0", "GPL-3.0", "LGPL-3.0", "ODbL-1.0", "DbCL-1.0", "Research-Only", "Other"], optional): Dataset license identifier
            owner_body (str, optional): Destination owner
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsCloneResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsCloneResponse,
            await self._client.request(
                "POST",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/clone",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={
                    "name": name,
                    "dataset": dataset_body,
                    "description": description,
                    "visibility": visibility,
                    "license": license,
                    "owner": owner_body,
                },
            ),
        )

    async def retrieve(
        self,
        owner: str,
        dataset: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsRetrieveResponse:
        """Get a dataset.

        Returns a dataset by owner and dataset name.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsRetrieveResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsRetrieveResponse,
            await self._client.request(
                "GET",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    async def update(
        self,
        owner: str,
        dataset: str,
        *,
        starred: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        metadata: dict[str, Any] | NotGiven = NOT_GIVEN,
        visibility: Literal["public", "private"] | NotGiven = NOT_GIVEN,
        tags: Sequence[str] | NotGiven = NOT_GIVEN,
        class_names: Sequence[str] | NotGiven = NOT_GIVEN,
        class_colors: dict[str, Any] | NotGiven = NOT_GIVEN,
        format: Literal["yolo", "coco", "raw", "ndjson"] | NotGiven = NOT_GIVEN,
        task: Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"] | NotGiven = NOT_GIVEN,
        license: Literal[
            "None",
            "CC0-1.0",
            "PDM-1.0",
            "CC-BY-2.5",
            "CC-BY-3.0",
            "CC-BY-4.0",
            "CC-BY-NC-2.0",
            "CC-BY-NC-3.0",
            "CC-BY-NC-4.0",
            "CC-BY-SA-3.0",
            "CC-BY-SA-4.0",
            "CC-BY-NC-SA-3.0",
            "CC-BY-NC-SA-4.0",
            "CC-BY-ND-4.0",
            "CC-BY-NC-ND-2.0",
            "CC-BY-NC-ND-4.0",
            "Apache-2.0",
            "MIT",
            "BSD-3-Clause",
            "AGPL-3.0",
            "GPL-2.0",
            "GPL-3.0",
            "LGPL-3.0",
            "ODbL-1.0",
            "DbCL-1.0",
            "Research-Only",
            "Other",
        ]
        | NotGiven = NOT_GIVEN,
        icon_color: str | NotGiven = NOT_GIVEN,
        icon_letter: str | Literal[""] | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsUpdateResponse:
        """Update a dataset.

        Updates dataset properties. Changing the display name also changes the dataset name used in URLs.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            starred (bool, optional): starred request value.
            name (str, optional): name request value.
            description (str, optional): description request value.
            metadata (dict[str, Any], optional): Custom JSON metadata with keys limited to 128 characters and at most 500,000 serialized characters.
            visibility (Literal["public", "private"], optional): Resource visibility
            tags (Sequence[str], optional): tags request value.
            class_names (Sequence[str], optional): classNames request value.
            class_colors (dict[str, Any], optional): classColors request value.
            format (Literal["yolo", "coco", "raw", "ndjson"], optional): Dataset annotation format
            task (Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"], optional): Dataset task type
            license (Literal["None", "CC0-1.0", "PDM-1.0", "CC-BY-2.5", "CC-BY-3.0", "CC-BY-4.0", "CC-BY-NC-2.0", "CC-BY-NC-3.0", "CC-BY-NC-4.0", "CC-BY-SA-3.0", "CC-BY-SA-4.0", "CC-BY-NC-SA-3.0", "CC-BY-NC-SA-4.0", "CC-BY-ND-4.0", "CC-BY-NC-ND-2.0", "CC-BY-NC-ND-4.0", "Apache-2.0", "MIT", "BSD-3-Clause", "AGPL-3.0", "GPL-2.0", "GPL-3.0", "LGPL-3.0", "ODbL-1.0", "DbCL-1.0", "Research-Only", "Other"], optional): Dataset license identifier
            icon_color (str, optional): iconColor request value.
            icon_letter (str | Literal[""], optional): iconLetter request value.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsUpdateResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsUpdateResponse,
            await self._client.request(
                "PATCH",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}",
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
                    "classNames": class_names,
                    "classColors": class_colors,
                    "format": format,
                    "task": task,
                    "license": license,
                    "iconColor": icon_color,
                    "iconLetter": icon_letter,
                },
            ),
        )

    async def delete(
        self,
        owner: str,
        dataset: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsDeleteResponse:
        """Delete a dataset.

        Moves a dataset to trash for 30 days.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsDeleteResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsDeleteResponse,
            await self._client.request(
                "DELETE",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    async def embeddings(
        self,
        owner: str,
        dataset: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsEmbeddingsResponse:
        """Get dataset analysis status.

        Returns embedding analysis status, progress, and freshness.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsEmbeddingsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsEmbeddingsResponse,
            await self._client.request(
                "GET",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/embeddings",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    async def create_embeddings(
        self,
        owner: str,
        dataset: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsCreateEmbeddingsResponse:
        """Analyze dataset embeddings.

        Starts embedding extraction and clustering.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsCreateEmbeddingsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsCreateEmbeddingsResponse,
            await self._client.request(
                "POST",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/embeddings",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    async def delete_embeddings(
        self,
        owner: str,
        dataset: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsDeleteEmbeddingsResponse:
        """Cancel dataset analysis.

        Cancels the active embedding analysis job, if present.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsDeleteEmbeddingsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsDeleteEmbeddingsResponse,
            await self._client.request(
                "DELETE",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/embeddings",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    async def export(
        self,
        owner: str,
        dataset: str,
        *,
        v: int | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsExportResponse:
        """Download a dataset export.

        Returns a signed URL for the current dataset or a saved version snapshot.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            v (int, optional): Saved version number
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsExportResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsExportResponse,
            await self._client.request(
                "GET",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/export",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("v", v, style="form", explode=True)],
            ),
        )

    async def create_export(
        self,
        owner: str,
        dataset: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsCreateExportResponse:
        """Create a dataset version.

        Creates an immutable numbered snapshot and returns its signed NDJSON download URL.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            description (str, optional): description request value.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsCreateExportResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsCreateExportResponse,
            await self._client.request(
                "POST",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/export",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={"description": description},
            ),
        )

    async def update_export(
        self,
        owner: str,
        dataset: str,
        *,
        version: int,
        description: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsUpdateExportResponse:
        """Update a dataset version description.

        Updates the description stored on an existing saved dataset version.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            version (int): version request value.
            description (str): description request value.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsUpdateExportResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsUpdateExportResponse,
            await self._client.request(
                "PATCH",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/export",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={"version": version, "description": description},
            ),
        )

    async def clustering(
        self,
        owner: str,
        dataset: str,
        *,
        offset: int | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsClusteringResponse:
        """Get dataset clustering layout.

        Returns paginated image coordinates from a completed dataset analysis.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            offset (int, optional): offset query parameter.
            limit (int, optional): limit query parameter.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsClusteringResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsClusteringResponse,
            await self._client.request(
                "GET",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/images/clustering",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("offset", offset, style="form", explode=True),
                    *_query_parameter("limit", limit, style="form", explode=True),
                ],
            ),
        )

    async def images(
        self,
        owner: str,
        dataset: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        include_total: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        split: Literal["train", "val", "test"] | NotGiven = NOT_GIVEN,
        has_error: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        has_label: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        class_ids: str | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        sort: Literal[
            "newest",
            "oldest",
            "name-asc",
            "name-desc",
            "height-asc",
            "height-desc",
            "width-asc",
            "width-desc",
            "size-asc",
            "size-desc",
            "labels-desc",
            "labels-asc",
        ]
        | NotGiven = NOT_GIVEN,
        include_thumbnails: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        include_image_urls: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        include_labels: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsImagesResponse:
        """List dataset images.

        Returns paginated images. Capped preview annotations are included only when requested.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            limit (int, optional): Maximum images to return
            offset (int, optional): Images to skip
            cursor (str, optional): Last image ID from the previous page
            include_total (Literal["true", "false"], optional): Include the total matching image count
            split (Literal["train", "val", "test"], optional): Dataset split
            has_error (Literal["true", "false"], optional): Filter by processing error state
            has_label (Literal["true", "false"], optional): Filter by annotation state
            class_ids (str, optional): Comma-separated class IDs; empty matches no images
            search (str, optional): Image name or metadata search
            sort (Literal["newest", "oldest", "name-asc", "name-desc", "height-asc", "height-desc", "width-asc", "width-desc", "size-asc", "size-desc", "labels-desc", "labels-asc"], optional): Sort order
            include_thumbnails (Literal["true", "false"], optional): Include signed thumbnail URLs
            include_image_urls (Literal["true", "false"], optional): Include signed full-size image URLs
            include_labels (Literal["true", "false"], optional): Include capped preview annotations
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsImagesResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsImagesResponse,
            await self._client.request(
                "GET",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/images",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("limit", limit, style="form", explode=True),
                    *_query_parameter("offset", offset, style="form", explode=True),
                    *_query_parameter("cursor", cursor, style="form", explode=True),
                    *_query_parameter("includeTotal", include_total, style="form", explode=True),
                    *_query_parameter("split", split, style="form", explode=True),
                    *_query_parameter("hasError", has_error, style="form", explode=True),
                    *_query_parameter("hasLabel", has_label, style="form", explode=True),
                    *_query_parameter("classIds", class_ids, style="form", explode=True),
                    *_query_parameter("search", search, style="form", explode=True),
                    *_query_parameter("sort", sort, style="form", explode=True),
                    *_query_parameter("includeThumbnails", include_thumbnails, style="form", explode=True),
                    *_query_parameter("includeImageUrls", include_image_urls, style="form", explode=True),
                    *_query_parameter("includeLabels", include_labels, style="form", explode=True),
                ],
            ),
        )

    async def selected_images(
        self,
        owner: str,
        dataset: str,
        *,
        image_ids: Sequence[str],
        split: Literal["train", "val", "test"] | NotGiven = NOT_GIVEN,
        has_error: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        has_label: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        class_ids: str | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        sort: Literal[
            "newest",
            "oldest",
            "name-asc",
            "name-desc",
            "height-asc",
            "height-desc",
            "width-asc",
            "width-desc",
            "size-asc",
            "size-desc",
            "labels-desc",
            "labels-asc",
        ]
        | NotGiven = NOT_GIVEN,
        include_thumbnails: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        include_image_urls: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        include_labels: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsSelectedImagesResponse:
        """Get selected dataset images.

        Returns the requested images with optional signed URLs and capped preview annotations.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            split (Literal["train", "val", "test"], optional): Dataset split
            has_error (Literal["true", "false"], optional): Filter by processing error state
            has_label (Literal["true", "false"], optional): Filter by annotation state
            class_ids (str, optional): Comma-separated class IDs; empty matches no images
            search (str, optional): Image name or metadata search
            sort (Literal["newest", "oldest", "name-asc", "name-desc", "height-asc", "height-desc", "width-asc", "width-desc", "size-asc", "size-desc", "labels-desc", "labels-asc"], optional): Sort order
            include_thumbnails (Literal["true", "false"], optional): Include signed thumbnail URLs
            include_image_urls (Literal["true", "false"], optional): Include signed full-size image URLs
            include_labels (Literal["true", "false"], optional): Include capped preview annotations
            image_ids (Sequence[str]): imageIds request value.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsSelectedImagesResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsSelectedImagesResponse,
            await self._client.request(
                "POST",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/images",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("split", split, style="form", explode=True),
                    *_query_parameter("hasError", has_error, style="form", explode=True),
                    *_query_parameter("hasLabel", has_label, style="form", explode=True),
                    *_query_parameter("classIds", class_ids, style="form", explode=True),
                    *_query_parameter("search", search, style="form", explode=True),
                    *_query_parameter("sort", sort, style="form", explode=True),
                    *_query_parameter("includeThumbnails", include_thumbnails, style="form", explode=True),
                    *_query_parameter("includeImageUrls", include_image_urls, style="form", explode=True),
                    *_query_parameter("includeLabels", include_labels, style="form", explode=True),
                ],
                json={"imageIds": image_ids},
            ),
        )

    async def ingest(
        self,
        owner: str,
        dataset: str,
        *,
        body: dict[str, Any],
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsIngestResponse:
        """Ingest dataset data.

        Processes a completed upload, remote archive, or connected data source into this dataset.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            body (dict[str, Any]): Input for dataset ingest job
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsIngestResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsIngestResponse,
            await self._client.request(
                "POST",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/ingest",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json=body,
            ),
        )

    async def models(
        self,
        owner: str,
        dataset: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsModelsResponse:
        """List models trained on a dataset.

        Returns accessible models whose training data references this dataset.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsModelsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsModelsResponse,
            await self._client.request(
                "GET",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/models",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    async def batch(
        self,
        owner: str,
        dataset: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsBatchResponse:
        """Get auto-annotation run status.

        Returns the dataset's in-flight auto-annotation run and its progress, or the last finished run awaiting dismissal.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsBatchResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsBatchResponse,
            await self._client.request(
                "GET",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/predict/batch",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    async def create_batch(
        self,
        owner: str,
        dataset: str,
        *,
        model_id: str,
        confidence: float | NotGiven = NOT_GIVEN,
        iou: float | NotGiven = NOT_GIVEN,
        class_mapping: Sequence[int | None] | NotGiven = NOT_GIVEN,
        include_annotated: bool | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsCreateBatchResponse:
        """Auto-annotate a dataset.

        Saves a dataset version, then queues a run that labels the dataset's unlabeled images with the given model, or every image when `includeAnnotated` is set. Existing labels are never changed, and the run is billed for the images it actually processes.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            model_id (str): Fully qualified model URI
            confidence (float, optional): Confidence threshold
            iou (float, optional): IoU threshold for non-maximum suppression
            class_mapping (Sequence[int | None], optional): Dataset class index for each model class, or null to drop it
            include_annotated (bool, optional): Also annotate images that already have labels, keeping the labels they have
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsCreateBatchResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsCreateBatchResponse,
            await self._client.request(
                "POST",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/predict/batch",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={
                    "modelId": model_id,
                    "confidence": confidence,
                    "iou": iou,
                    "classMapping": class_mapping,
                    "includeAnnotated": include_annotated,
                },
            ),
        )

    async def delete_batch(
        self,
        owner: str,
        dataset: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsDeleteBatchResponse:
        """Cancel or dismiss an auto-annotation run.

        Cancels an in-flight run, or settles billing and dismisses its terminal summary.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsDeleteBatchResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsDeleteBatchResponse,
            await self._client.request(
                "DELETE",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/predict/batch",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    async def restore(
        self,
        owner: str,
        dataset: str,
        *,
        version: int,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsRestoreResponse:
        """Restore a saved dataset version.

        Restores dataset files, labels, and metadata from a previously saved version.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            version (int): version request value.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsRestoreResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsRestoreResponse,
            await self._client.request(
                "POST",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/restore",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={"version": version},
            ),
        )

    async def redistribute_splits(
        self,
        owner: str,
        dataset: str,
        *,
        train: int,
        val: int,
        test: int,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsRedistributeSplitsResponse:
        """Redistribute dataset splits.

        Randomly reassigns images using train, validation, and test percentages that total 100.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            train (int): Train split percentage
            val (int): Validation split percentage
            test (int): Test split percentage
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsRedistributeSplitsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsRedistributeSplitsResponse,
            await self._client.request(
                "POST",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/splits/redistribute",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={"train": train, "val": val, "test": test},
            ),
        )

    async def list(
        self,
        owner: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        include_samples: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        include_image_urls: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsListResponse:
        """List datasets.

        Returns datasets owned by the named owner. Private datasets require workspace access.

        Args:
            owner (str): Dataset owner
            limit (int, optional): Maximum datasets to return
            include_samples (Literal["true", "false"], optional): Include sample image previews
            include_image_urls (Literal["true", "false"], optional): Include full-size sample image fallback URLs
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsListResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsListResponse,
            await self._client.request(
                "GET",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("limit", limit, style="form", explode=True),
                    *_query_parameter("includeSamples", include_samples, style="form", explode=True),
                    *_query_parameter("includeImageUrls", include_image_urls, style="form", explode=True),
                ],
            ),
        )

    async def create(
        self,
        *,
        dataset: str,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        metadata: dict[str, Any] | NotGiven = NOT_GIVEN,
        visibility: Literal["public", "private"] | NotGiven = NOT_GIVEN,
        task: Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"] | NotGiven = NOT_GIVEN,
        image_count: int | NotGiven = NOT_GIVEN,
        class_names: Sequence[str] | NotGiven = NOT_GIVEN,
        format: Literal["yolo", "coco", "raw", "ndjson"] | NotGiven = NOT_GIVEN,
        tags: Sequence[str] | NotGiven = NOT_GIVEN,
        license: Literal[
            "None",
            "CC0-1.0",
            "PDM-1.0",
            "CC-BY-2.5",
            "CC-BY-3.0",
            "CC-BY-4.0",
            "CC-BY-NC-2.0",
            "CC-BY-NC-3.0",
            "CC-BY-NC-4.0",
            "CC-BY-SA-3.0",
            "CC-BY-SA-4.0",
            "CC-BY-NC-SA-3.0",
            "CC-BY-NC-SA-4.0",
            "CC-BY-ND-4.0",
            "CC-BY-NC-ND-2.0",
            "CC-BY-NC-ND-4.0",
            "Apache-2.0",
            "MIT",
            "BSD-3-Clause",
            "AGPL-3.0",
            "GPL-2.0",
            "GPL-3.0",
            "LGPL-3.0",
            "ODbL-1.0",
            "DbCL-1.0",
            "Research-Only",
            "Other",
        ]
        | NotGiven = NOT_GIVEN,
        require_exact_slug: bool | NotGiven = NOT_GIVEN,
        owner: str | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsCreateResponse:
        """Create a dataset.

        Creates an empty dataset in your personal workspace or a team workspace.

        Args:
            dataset (str): Dataset name used in Platform URLs
            name (str): Display name
            description (str, optional): description request value.
            metadata (dict[str, Any], optional): Custom JSON metadata with keys limited to 128 characters and at most 500,000 serialized characters.
            visibility (Literal["public", "private"], optional): Resource visibility
            task (Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"], optional): Dataset task type
            image_count (int, optional): imageCount request value.
            class_names (Sequence[str], optional): classNames request value.
            format (Literal["yolo", "coco", "raw", "ndjson"], optional): Dataset annotation format
            tags (Sequence[str], optional): tags request value.
            license (Literal["None", "CC0-1.0", "PDM-1.0", "CC-BY-2.5", "CC-BY-3.0", "CC-BY-4.0", "CC-BY-NC-2.0", "CC-BY-NC-3.0", "CC-BY-NC-4.0", "CC-BY-SA-3.0", "CC-BY-SA-4.0", "CC-BY-NC-SA-3.0", "CC-BY-NC-SA-4.0", "CC-BY-ND-4.0", "CC-BY-NC-ND-2.0", "CC-BY-NC-ND-4.0", "Apache-2.0", "MIT", "BSD-3-Clause", "AGPL-3.0", "GPL-2.0", "GPL-3.0", "LGPL-3.0", "ODbL-1.0", "DbCL-1.0", "Research-Only", "Other"], optional): Dataset license identifier
            require_exact_slug (bool, optional): Reject a slug conflict instead of creating an automatically suffixed dataset
            owner (str, optional): Workspace owner
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsCreateResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsCreateResponse,
            await self._client.request(
                "POST",
                "/api/datasets",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={
                    "dataset": dataset,
                    "name": name,
                    "description": description,
                    "metadata": metadata,
                    "visibility": visibility,
                    "task": task,
                    "imageCount": image_count,
                    "classNames": class_names,
                    "format": format,
                    "tags": tags,
                    "license": license,
                    "requireExactSlug": require_exact_slug,
                    "owner": owner,
                },
            ),
        )

    async def import_roboflow(
        self,
        *,
        api_key: str,
        items: Sequence[dict[str, Any]],
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> DatasetsImportRoboflowResponse:
        """Import datasets from Roboflow.

        Imports selected Roboflow dataset versions into the API key's workspace.

        Args:
            api_key (str): Roboflow API key
            items (Sequence[dict[str, Any]]): items request value.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsImportRoboflowResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsImportRoboflowResponse,
            await self._client.request(
                "POST",
                "/api/integrations/roboflow/import",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={"apiKey": api_key, "items": items},
            ),
        )

    async def preview_roboflow(
        self, *, api_key: str, timeout: float | httpx.Timeout | None = None, extra_headers: dict[str, str] | None = None
    ) -> DatasetsPreviewRoboflowResponse:
        """Preview a Roboflow import.

        Validates a Roboflow API key and lists datasets available for import.

        Args:
            api_key (str): Roboflow API key
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (DatasetsPreviewRoboflowResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsPreviewRoboflowResponse,
            await self._client.request(
                "POST",
                "/api/integrations/roboflow/preview",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={"apiKey": api_key},
            ),
        )
