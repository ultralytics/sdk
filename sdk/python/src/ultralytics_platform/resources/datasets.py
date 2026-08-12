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
    DatasetsCloneResponse,
    DatasetsCreateEmbeddingsResponse,
    DatasetsCreateExportResponse,
    DatasetsCreateResponse,
    DatasetsDeleteClassesResponse,
    DatasetsDeleteEmbeddingsResponse,
    DatasetsDeleteResponse,
    DatasetsImportFromRoboflowResponse,
    DatasetsIngestResponse,
    DatasetsListImagesResponse,
    DatasetsListModelsResponse,
    DatasetsListResponse,
    DatasetsMergeClassesResponse,
    DatasetsPreviewRoboflowImportResponse,
    DatasetsRedistributeSplitsResponse,
    DatasetsRestoreResponse,
    DatasetsRetrieveClassStatsResponse,
    DatasetsRetrieveEmbeddingsResponse,
    DatasetsRetrieveExportResponse,
    DatasetsRetrieveImagesClusteringResponse,
    DatasetsRetrieveResponse,
    DatasetsRetrieveSelectedImagesResponse,
    DatasetsUpdateExportResponse,
    DatasetsUpdateResponse,
)


class Datasets:
    """Datasets API operations."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def retrieve_class_stats(self, owner: str, dataset: str) -> DatasetsRetrieveClassStatsResponse:
        """Get dataset statistics.

        Returns class counts, image distributions, and annotation heatmaps.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name

        Returns:
            (DatasetsRetrieveClassStatsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsRetrieveClassStatsResponse,
            self._client.request(
                "GET",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/class-stats",
                auth=("Authorization", "Bearer "),
            ),
        )

    def delete_classes(self, owner: str, dataset: str, *, class_ids: list[int]) -> DatasetsDeleteClassesResponse:
        """Delete dataset classes.

        Deletes annotations in the selected classes, removes the classes, and shifts remaining class IDs.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            class_ids (list[int]): classIds request value.

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
                auth=("Authorization", "Bearer "),
                json={"classIds": class_ids},
            ),
        )

    def merge_classes(
        self, owner: str, dataset: str, *, source_class_ids: list[int], target_class_id: int
    ) -> DatasetsMergeClassesResponse:
        """Merge dataset classes.

        Reassigns annotations to one target class and removes the source classes.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            source_class_ids (list[int]): sourceClassIds request value.
            target_class_id (int): targetClassId request value.

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
            "CC-BY-4.0",
            "CC-BY-NC-2.0",
            "CC-BY-SA-4.0",
            "CC-BY-NC-4.0",
            "CC-BY-NC-SA-3.0",
            "CC-BY-NC-SA-4.0",
            "CC-BY-ND-4.0",
            "CC-BY-NC-ND-4.0",
            "Apache-2.0",
            "MIT",
            "AGPL-3.0",
            "GPL-3.0",
            "Research-Only",
            "Other",
        ]
        | NotGiven = NOT_GIVEN,
        owner_body: str | NotGiven = NOT_GIVEN,
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
            license (Literal["None", "CC0-1.0", "PDM-1.0", "CC-BY-2.5", "CC-BY-4.0", "CC-BY-NC-2.0", "CC-BY-SA-4.0", "CC-BY-NC-4.0", "CC-BY-NC-SA-3.0", "CC-BY-NC-SA-4.0", "CC-BY-ND-4.0", "CC-BY-NC-ND-4.0", "Apache-2.0", "MIT", "AGPL-3.0", "GPL-3.0", "Research-Only", "Other"], optional): Dataset license identifier
            owner_body (str, optional): Destination owner

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

    def retrieve(self, owner: str, dataset: str) -> DatasetsRetrieveResponse:
        """Get a dataset.

        Returns a dataset by owner and dataset name.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name

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
        tags: list[str] | NotGiven = NOT_GIVEN,
        class_names: list[str] | NotGiven = NOT_GIVEN,
        class_colors: dict[str, Any] | NotGiven = NOT_GIVEN,
        format: Literal["yolo", "coco", "voc", "raw", "ndjson"] | NotGiven = NOT_GIVEN,
        task: Literal["detect", "segment", "semantic", "classify", "pose", "obb"] | NotGiven = NOT_GIVEN,
        license: Literal[
            "None",
            "CC0-1.0",
            "PDM-1.0",
            "CC-BY-2.5",
            "CC-BY-4.0",
            "CC-BY-NC-2.0",
            "CC-BY-SA-4.0",
            "CC-BY-NC-4.0",
            "CC-BY-NC-SA-3.0",
            "CC-BY-NC-SA-4.0",
            "CC-BY-ND-4.0",
            "CC-BY-NC-ND-4.0",
            "Apache-2.0",
            "MIT",
            "AGPL-3.0",
            "GPL-3.0",
            "Research-Only",
            "Other",
        ]
        | NotGiven = NOT_GIVEN,
        icon_color: str | NotGiven = NOT_GIVEN,
        icon_letter: str | Literal[""] | NotGiven = NOT_GIVEN,
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
            tags (list[str], optional): tags request value.
            class_names (list[str], optional): classNames request value.
            class_colors (dict[str, Any], optional): classColors request value.
            format (Literal["yolo", "coco", "voc", "raw", "ndjson"], optional): Dataset annotation format
            task (Literal["detect", "segment", "semantic", "classify", "pose", "obb"], optional): Dataset task type (depth coming soon)
            license (Literal["None", "CC0-1.0", "PDM-1.0", "CC-BY-2.5", "CC-BY-4.0", "CC-BY-NC-2.0", "CC-BY-SA-4.0", "CC-BY-NC-4.0", "CC-BY-NC-SA-3.0", "CC-BY-NC-SA-4.0", "CC-BY-ND-4.0", "CC-BY-NC-ND-4.0", "Apache-2.0", "MIT", "AGPL-3.0", "GPL-3.0", "Research-Only", "Other"], optional): Dataset license identifier
            icon_color (str, optional): iconColor request value.
            icon_letter (str | Literal[""], optional): iconLetter request value.

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

    def delete(self, owner: str, dataset: str) -> DatasetsDeleteResponse:
        """Delete a dataset.

        Moves a dataset to trash for 30 days.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name

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
                auth=("Authorization", "Bearer "),
            ),
        )

    def retrieve_embeddings(self, owner: str, dataset: str) -> DatasetsRetrieveEmbeddingsResponse:
        """Get dataset analysis status.

        Returns embedding analysis status, progress, and freshness.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name

        Returns:
            (DatasetsRetrieveEmbeddingsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsRetrieveEmbeddingsResponse,
            self._client.request(
                "GET",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/embeddings",
                auth=("Authorization", "Bearer "),
            ),
        )

    def create_embeddings(self, owner: str, dataset: str) -> DatasetsCreateEmbeddingsResponse:
        """Analyze dataset embeddings.

        Starts embedding extraction and clustering.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name

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
                auth=("Authorization", "Bearer "),
            ),
        )

    def delete_embeddings(self, owner: str, dataset: str) -> DatasetsDeleteEmbeddingsResponse:
        """Cancel dataset analysis.

        Cancels the active embedding analysis job, if present.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name

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
                auth=("Authorization", "Bearer "),
            ),
        )

    def retrieve_export(self, owner: str, dataset: str, *, v: int | None = None) -> DatasetsRetrieveExportResponse:
        """Download a dataset export.

        Returns a signed URL for the current dataset or a saved version snapshot.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            v (int, optional): Saved version number

        Returns:
            (DatasetsRetrieveExportResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsRetrieveExportResponse,
            self._client.request(
                "GET",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/export",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("v", v, style="form", explode=True)],
            ),
        )

    def create_export(
        self, owner: str, dataset: str, *, description: str | NotGiven = NOT_GIVEN
    ) -> DatasetsCreateExportResponse:
        """Create a dataset version.

        Creates an immutable numbered snapshot and returns its signed NDJSON download URL.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            description (str, optional): description request value.

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
                auth=("Authorization", "Bearer "),
                json={"description": description},
            ),
        )

    def update_export(
        self, owner: str, dataset: str, *, version: int, description: str
    ) -> DatasetsUpdateExportResponse:
        """Update a dataset version description.

        Updates the description stored on an existing saved dataset version.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            version (int): version request value.
            description (str): description request value.

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
                auth=("Authorization", "Bearer "),
                json={"version": version, "description": description},
            ),
        )

    def retrieve_images_clustering(
        self, owner: str, dataset: str, *, offset: int | None = None, limit: int | None = None
    ) -> DatasetsRetrieveImagesClusteringResponse:
        """Get dataset clustering layout.

        Returns paginated image coordinates from a completed dataset analysis.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            offset (int, optional): offset query parameter.
            limit (int, optional): limit query parameter.

        Returns:
            (DatasetsRetrieveImagesClusteringResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsRetrieveImagesClusteringResponse,
            self._client.request(
                "GET",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/images/clustering",
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("offset", offset, style="form", explode=True),
                    *_query_parameter("limit", limit, style="form", explode=True),
                ],
            ),
        )

    def list_images(
        self,
        owner: str,
        dataset: str,
        *,
        limit: int | None = None,
        offset: int | None = None,
        cursor: str | None = None,
        include_total: Literal["true", "false"] | None = None,
        split: Literal["train", "val", "test"] | None = None,
        has_error: Literal["true", "false"] | None = None,
        has_label: Literal["true", "false"] | None = None,
        class_ids: str | None = None,
        search: str | None = None,
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
        | None = None,
        include_thumbnails: Literal["true", "false"] | None = None,
        include_image_urls: Literal["true", "false"] | None = None,
        include_labels: Literal["true", "false"] | None = None,
    ) -> DatasetsListImagesResponse:
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

        Returns:
            (DatasetsListImagesResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsListImagesResponse,
            self._client.request(
                "GET",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/images",
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

    def retrieve_selected_images(
        self,
        owner: str,
        dataset: str,
        *,
        image_ids: list[str],
        split: Literal["train", "val", "test"] | None = None,
        has_error: Literal["true", "false"] | None = None,
        has_label: Literal["true", "false"] | None = None,
        class_ids: str | None = None,
        search: str | None = None,
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
        | None = None,
        include_thumbnails: Literal["true", "false"] | None = None,
        include_image_urls: Literal["true", "false"] | None = None,
        include_labels: Literal["true", "false"] | None = None,
    ) -> DatasetsRetrieveSelectedImagesResponse:
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
            image_ids (list[str]): imageIds request value.

        Returns:
            (DatasetsRetrieveSelectedImagesResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsRetrieveSelectedImagesResponse,
            self._client.request(
                "POST",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/images",
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
        target_split: Literal["train", "val", "test"] | NotGiven = NOT_GIVEN,
        conflict_policy: Literal["skip", "keep_both", "replace"] | NotGiven = NOT_GIVEN,
        session_id: Any | NotGiven = NOT_GIVEN,
        source_url: Any | NotGiven = NOT_GIVEN,
        reference: Any | NotGiven = NOT_GIVEN,
        class_mapping: Any | NotGiven = NOT_GIVEN,
        image_metadata: Any | NotGiven = NOT_GIVEN,
    ) -> DatasetsIngestResponse:
        """Ingest dataset data.

        Processes a completed upload, remote archive, or connected data source into this dataset.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            target_split (Literal["train", "val", "test"], optional): Target split for new images (overrides archive structure)
            conflict_policy (Literal["skip", "keep_both", "replace"], optional): How to handle filename or content conflicts
            session_id (Any, optional): Upload session ID from signed-url response
            source_url (Any, optional): Remote dataset archive or NDJSON URL
            reference (Any, optional): Connected cloud or On Premise source
            class_mapping (Any, optional): Mapping from incoming class names to this dataset
            image_metadata (Any, optional): Custom metadata keyed by each image's archive-relative path or NDJSON file value. Paths are limited to 1,024 characters, top-level metadata keys to 128 characters, and the map to 500,000 serialized characters.

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
                auth=("Authorization", "Bearer "),
                json={
                    "targetSplit": target_split,
                    "conflictPolicy": conflict_policy,
                    "sessionId": session_id,
                    "sourceUrl": source_url,
                    "reference": reference,
                    "classMapping": class_mapping,
                    "imageMetadata": image_metadata,
                },
            ),
        )

    def list_models(self, owner: str, dataset: str) -> DatasetsListModelsResponse:
        """List models trained on a dataset.

        Returns accessible models whose training data references this dataset.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name

        Returns:
            (DatasetsListModelsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsListModelsResponse,
            self._client.request(
                "GET",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/models",
                auth=("Authorization", "Bearer "),
            ),
        )

    def restore(self, owner: str, dataset: str, *, version: int) -> DatasetsRestoreResponse:
        """Restore a saved dataset version.

        Restores dataset files, labels, and metadata from a previously saved version.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            version (int): version request value.

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
                auth=("Authorization", "Bearer "),
                json={"version": version},
            ),
        )

    def redistribute_splits(
        self, owner: str, dataset: str, *, train: int, val: int, test: int
    ) -> DatasetsRedistributeSplitsResponse:
        """Redistribute dataset splits.

        Randomly reassigns images using train, validation, and test percentages that total 100.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            train (int): Train split percentage
            val (int): Validation split percentage
            test (int): Test split percentage

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
                auth=("Authorization", "Bearer "),
                json={"train": train, "val": val, "test": test},
            ),
        )

    def list(
        self,
        owner: str,
        *,
        limit: int | None = None,
        include_samples: Literal["true", "false"] | None = None,
        include_image_urls: Literal["true", "false"] | None = None,
    ) -> DatasetsListResponse:
        """List datasets.

        Returns datasets owned by the named owner. Private datasets require workspace access.

        Args:
            owner (str): Dataset owner
            limit (int, optional): Maximum datasets to return
            include_samples (Literal["true", "false"], optional): Include sample image previews
            include_image_urls (Literal["true", "false"], optional): Include full-size sample image fallback URLs

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
        task: Literal["detect", "segment", "semantic", "classify", "pose", "obb"] | NotGiven = NOT_GIVEN,
        image_count: int | NotGiven = NOT_GIVEN,
        class_names: list[str] | NotGiven = NOT_GIVEN,
        format: Literal["yolo", "coco", "voc", "raw", "ndjson"] | NotGiven = NOT_GIVEN,
        tags: list[str] | NotGiven = NOT_GIVEN,
        license: Literal[
            "None",
            "CC0-1.0",
            "PDM-1.0",
            "CC-BY-2.5",
            "CC-BY-4.0",
            "CC-BY-NC-2.0",
            "CC-BY-SA-4.0",
            "CC-BY-NC-4.0",
            "CC-BY-NC-SA-3.0",
            "CC-BY-NC-SA-4.0",
            "CC-BY-ND-4.0",
            "CC-BY-NC-ND-4.0",
            "Apache-2.0",
            "MIT",
            "AGPL-3.0",
            "GPL-3.0",
            "Research-Only",
            "Other",
        ]
        | NotGiven = NOT_GIVEN,
        owner: str | NotGiven = NOT_GIVEN,
    ) -> DatasetsCreateResponse:
        """Create a dataset.

        Creates an empty dataset in your personal workspace or a team workspace.

        Args:
            dataset (str): Dataset name used in Platform URLs
            name (str): name request value.
            description (str, optional): description request value.
            metadata (dict[str, Any], optional): Custom JSON metadata with keys limited to 128 characters and at most 500,000 serialized characters.
            visibility (Literal["public", "private"], optional): Resource visibility
            task (Literal["detect", "segment", "semantic", "classify", "pose", "obb"], optional): Dataset task type (depth coming soon)
            image_count (int, optional): imageCount request value.
            class_names (list[str], optional): classNames request value.
            format (Literal["yolo", "coco", "voc", "raw", "ndjson"], optional): Dataset annotation format
            tags (list[str], optional): tags request value.
            license (Literal["None", "CC0-1.0", "PDM-1.0", "CC-BY-2.5", "CC-BY-4.0", "CC-BY-NC-2.0", "CC-BY-SA-4.0", "CC-BY-NC-4.0", "CC-BY-NC-SA-3.0", "CC-BY-NC-SA-4.0", "CC-BY-ND-4.0", "CC-BY-NC-ND-4.0", "Apache-2.0", "MIT", "AGPL-3.0", "GPL-3.0", "Research-Only", "Other"], optional): Dataset license identifier
            owner (str, optional): Workspace owner

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
                    "owner": owner,
                },
            ),
        )

    def import_from_roboflow(self, *, api_key: str, items: list[dict[str, Any]]) -> DatasetsImportFromRoboflowResponse:
        """Import datasets from Roboflow.

        Imports selected Roboflow dataset versions into the API key's workspace.

        Args:
            api_key (str): apiKey request value.
            items (list[dict[str, Any]]): items request value.

        Returns:
            (DatasetsImportFromRoboflowResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsImportFromRoboflowResponse,
            self._client.request(
                "POST",
                "/api/integrations/roboflow/import",
                auth=("Authorization", "Bearer "),
                json={"apiKey": api_key, "items": items},
            ),
        )

    def preview_roboflow_import(self, *, api_key: str) -> DatasetsPreviewRoboflowImportResponse:
        """Preview a Roboflow import.

        Validates a Roboflow API key and lists datasets available for import.

        Args:
            api_key (str): apiKey request value.

        Returns:
            (DatasetsPreviewRoboflowImportResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsPreviewRoboflowImportResponse,
            self._client.request(
                "POST",
                "/api/integrations/roboflow/preview",
                auth=("Authorization", "Bearer "),
                json={"apiKey": api_key},
            ),
        )


class AsyncDatasets:
    """Asynchronous Datasets API operations."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def retrieve_class_stats(self, owner: str, dataset: str) -> DatasetsRetrieveClassStatsResponse:
        """Get dataset statistics.

        Returns class counts, image distributions, and annotation heatmaps.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name

        Returns:
            (DatasetsRetrieveClassStatsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsRetrieveClassStatsResponse,
            await self._client.request(
                "GET",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/class-stats",
                auth=("Authorization", "Bearer "),
            ),
        )

    async def delete_classes(self, owner: str, dataset: str, *, class_ids: list[int]) -> DatasetsDeleteClassesResponse:
        """Delete dataset classes.

        Deletes annotations in the selected classes, removes the classes, and shifts remaining class IDs.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            class_ids (list[int]): classIds request value.

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
                auth=("Authorization", "Bearer "),
                json={"classIds": class_ids},
            ),
        )

    async def merge_classes(
        self, owner: str, dataset: str, *, source_class_ids: list[int], target_class_id: int
    ) -> DatasetsMergeClassesResponse:
        """Merge dataset classes.

        Reassigns annotations to one target class and removes the source classes.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            source_class_ids (list[int]): sourceClassIds request value.
            target_class_id (int): targetClassId request value.

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
            "CC-BY-4.0",
            "CC-BY-NC-2.0",
            "CC-BY-SA-4.0",
            "CC-BY-NC-4.0",
            "CC-BY-NC-SA-3.0",
            "CC-BY-NC-SA-4.0",
            "CC-BY-ND-4.0",
            "CC-BY-NC-ND-4.0",
            "Apache-2.0",
            "MIT",
            "AGPL-3.0",
            "GPL-3.0",
            "Research-Only",
            "Other",
        ]
        | NotGiven = NOT_GIVEN,
        owner_body: str | NotGiven = NOT_GIVEN,
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
            license (Literal["None", "CC0-1.0", "PDM-1.0", "CC-BY-2.5", "CC-BY-4.0", "CC-BY-NC-2.0", "CC-BY-SA-4.0", "CC-BY-NC-4.0", "CC-BY-NC-SA-3.0", "CC-BY-NC-SA-4.0", "CC-BY-ND-4.0", "CC-BY-NC-ND-4.0", "Apache-2.0", "MIT", "AGPL-3.0", "GPL-3.0", "Research-Only", "Other"], optional): Dataset license identifier
            owner_body (str, optional): Destination owner

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

    async def retrieve(self, owner: str, dataset: str) -> DatasetsRetrieveResponse:
        """Get a dataset.

        Returns a dataset by owner and dataset name.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name

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
        tags: list[str] | NotGiven = NOT_GIVEN,
        class_names: list[str] | NotGiven = NOT_GIVEN,
        class_colors: dict[str, Any] | NotGiven = NOT_GIVEN,
        format: Literal["yolo", "coco", "voc", "raw", "ndjson"] | NotGiven = NOT_GIVEN,
        task: Literal["detect", "segment", "semantic", "classify", "pose", "obb"] | NotGiven = NOT_GIVEN,
        license: Literal[
            "None",
            "CC0-1.0",
            "PDM-1.0",
            "CC-BY-2.5",
            "CC-BY-4.0",
            "CC-BY-NC-2.0",
            "CC-BY-SA-4.0",
            "CC-BY-NC-4.0",
            "CC-BY-NC-SA-3.0",
            "CC-BY-NC-SA-4.0",
            "CC-BY-ND-4.0",
            "CC-BY-NC-ND-4.0",
            "Apache-2.0",
            "MIT",
            "AGPL-3.0",
            "GPL-3.0",
            "Research-Only",
            "Other",
        ]
        | NotGiven = NOT_GIVEN,
        icon_color: str | NotGiven = NOT_GIVEN,
        icon_letter: str | Literal[""] | NotGiven = NOT_GIVEN,
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
            tags (list[str], optional): tags request value.
            class_names (list[str], optional): classNames request value.
            class_colors (dict[str, Any], optional): classColors request value.
            format (Literal["yolo", "coco", "voc", "raw", "ndjson"], optional): Dataset annotation format
            task (Literal["detect", "segment", "semantic", "classify", "pose", "obb"], optional): Dataset task type (depth coming soon)
            license (Literal["None", "CC0-1.0", "PDM-1.0", "CC-BY-2.5", "CC-BY-4.0", "CC-BY-NC-2.0", "CC-BY-SA-4.0", "CC-BY-NC-4.0", "CC-BY-NC-SA-3.0", "CC-BY-NC-SA-4.0", "CC-BY-ND-4.0", "CC-BY-NC-ND-4.0", "Apache-2.0", "MIT", "AGPL-3.0", "GPL-3.0", "Research-Only", "Other"], optional): Dataset license identifier
            icon_color (str, optional): iconColor request value.
            icon_letter (str | Literal[""], optional): iconLetter request value.

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

    async def delete(self, owner: str, dataset: str) -> DatasetsDeleteResponse:
        """Delete a dataset.

        Moves a dataset to trash for 30 days.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name

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
                auth=("Authorization", "Bearer "),
            ),
        )

    async def retrieve_embeddings(self, owner: str, dataset: str) -> DatasetsRetrieveEmbeddingsResponse:
        """Get dataset analysis status.

        Returns embedding analysis status, progress, and freshness.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name

        Returns:
            (DatasetsRetrieveEmbeddingsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsRetrieveEmbeddingsResponse,
            await self._client.request(
                "GET",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/embeddings",
                auth=("Authorization", "Bearer "),
            ),
        )

    async def create_embeddings(self, owner: str, dataset: str) -> DatasetsCreateEmbeddingsResponse:
        """Analyze dataset embeddings.

        Starts embedding extraction and clustering.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name

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
                auth=("Authorization", "Bearer "),
            ),
        )

    async def delete_embeddings(self, owner: str, dataset: str) -> DatasetsDeleteEmbeddingsResponse:
        """Cancel dataset analysis.

        Cancels the active embedding analysis job, if present.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name

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
                auth=("Authorization", "Bearer "),
            ),
        )

    async def retrieve_export(
        self, owner: str, dataset: str, *, v: int | None = None
    ) -> DatasetsRetrieveExportResponse:
        """Download a dataset export.

        Returns a signed URL for the current dataset or a saved version snapshot.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            v (int, optional): Saved version number

        Returns:
            (DatasetsRetrieveExportResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsRetrieveExportResponse,
            await self._client.request(
                "GET",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/export",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("v", v, style="form", explode=True)],
            ),
        )

    async def create_export(
        self, owner: str, dataset: str, *, description: str | NotGiven = NOT_GIVEN
    ) -> DatasetsCreateExportResponse:
        """Create a dataset version.

        Creates an immutable numbered snapshot and returns its signed NDJSON download URL.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            description (str, optional): description request value.

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
                auth=("Authorization", "Bearer "),
                json={"description": description},
            ),
        )

    async def update_export(
        self, owner: str, dataset: str, *, version: int, description: str
    ) -> DatasetsUpdateExportResponse:
        """Update a dataset version description.

        Updates the description stored on an existing saved dataset version.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            version (int): version request value.
            description (str): description request value.

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
                auth=("Authorization", "Bearer "),
                json={"version": version, "description": description},
            ),
        )

    async def retrieve_images_clustering(
        self, owner: str, dataset: str, *, offset: int | None = None, limit: int | None = None
    ) -> DatasetsRetrieveImagesClusteringResponse:
        """Get dataset clustering layout.

        Returns paginated image coordinates from a completed dataset analysis.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            offset (int, optional): offset query parameter.
            limit (int, optional): limit query parameter.

        Returns:
            (DatasetsRetrieveImagesClusteringResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsRetrieveImagesClusteringResponse,
            await self._client.request(
                "GET",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/images/clustering",
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("offset", offset, style="form", explode=True),
                    *_query_parameter("limit", limit, style="form", explode=True),
                ],
            ),
        )

    async def list_images(
        self,
        owner: str,
        dataset: str,
        *,
        limit: int | None = None,
        offset: int | None = None,
        cursor: str | None = None,
        include_total: Literal["true", "false"] | None = None,
        split: Literal["train", "val", "test"] | None = None,
        has_error: Literal["true", "false"] | None = None,
        has_label: Literal["true", "false"] | None = None,
        class_ids: str | None = None,
        search: str | None = None,
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
        | None = None,
        include_thumbnails: Literal["true", "false"] | None = None,
        include_image_urls: Literal["true", "false"] | None = None,
        include_labels: Literal["true", "false"] | None = None,
    ) -> DatasetsListImagesResponse:
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

        Returns:
            (DatasetsListImagesResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsListImagesResponse,
            await self._client.request(
                "GET",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/images",
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

    async def retrieve_selected_images(
        self,
        owner: str,
        dataset: str,
        *,
        image_ids: list[str],
        split: Literal["train", "val", "test"] | None = None,
        has_error: Literal["true", "false"] | None = None,
        has_label: Literal["true", "false"] | None = None,
        class_ids: str | None = None,
        search: str | None = None,
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
        | None = None,
        include_thumbnails: Literal["true", "false"] | None = None,
        include_image_urls: Literal["true", "false"] | None = None,
        include_labels: Literal["true", "false"] | None = None,
    ) -> DatasetsRetrieveSelectedImagesResponse:
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
            image_ids (list[str]): imageIds request value.

        Returns:
            (DatasetsRetrieveSelectedImagesResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsRetrieveSelectedImagesResponse,
            await self._client.request(
                "POST",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/images",
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
        target_split: Literal["train", "val", "test"] | NotGiven = NOT_GIVEN,
        conflict_policy: Literal["skip", "keep_both", "replace"] | NotGiven = NOT_GIVEN,
        session_id: Any | NotGiven = NOT_GIVEN,
        source_url: Any | NotGiven = NOT_GIVEN,
        reference: Any | NotGiven = NOT_GIVEN,
        class_mapping: Any | NotGiven = NOT_GIVEN,
        image_metadata: Any | NotGiven = NOT_GIVEN,
    ) -> DatasetsIngestResponse:
        """Ingest dataset data.

        Processes a completed upload, remote archive, or connected data source into this dataset.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            target_split (Literal["train", "val", "test"], optional): Target split for new images (overrides archive structure)
            conflict_policy (Literal["skip", "keep_both", "replace"], optional): How to handle filename or content conflicts
            session_id (Any, optional): Upload session ID from signed-url response
            source_url (Any, optional): Remote dataset archive or NDJSON URL
            reference (Any, optional): Connected cloud or On Premise source
            class_mapping (Any, optional): Mapping from incoming class names to this dataset
            image_metadata (Any, optional): Custom metadata keyed by each image's archive-relative path or NDJSON file value. Paths are limited to 1,024 characters, top-level metadata keys to 128 characters, and the map to 500,000 serialized characters.

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
                auth=("Authorization", "Bearer "),
                json={
                    "targetSplit": target_split,
                    "conflictPolicy": conflict_policy,
                    "sessionId": session_id,
                    "sourceUrl": source_url,
                    "reference": reference,
                    "classMapping": class_mapping,
                    "imageMetadata": image_metadata,
                },
            ),
        )

    async def list_models(self, owner: str, dataset: str) -> DatasetsListModelsResponse:
        """List models trained on a dataset.

        Returns accessible models whose training data references this dataset.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name

        Returns:
            (DatasetsListModelsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsListModelsResponse,
            await self._client.request(
                "GET",
                f"/api/datasets/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(dataset, explode=False, allow_reserved=False)}/models",
                auth=("Authorization", "Bearer "),
            ),
        )

    async def restore(self, owner: str, dataset: str, *, version: int) -> DatasetsRestoreResponse:
        """Restore a saved dataset version.

        Restores dataset files, labels, and metadata from a previously saved version.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            version (int): version request value.

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
                auth=("Authorization", "Bearer "),
                json={"version": version},
            ),
        )

    async def redistribute_splits(
        self, owner: str, dataset: str, *, train: int, val: int, test: int
    ) -> DatasetsRedistributeSplitsResponse:
        """Redistribute dataset splits.

        Randomly reassigns images using train, validation, and test percentages that total 100.

        Args:
            owner (str): Dataset owner
            dataset (str): Dataset name
            train (int): Train split percentage
            val (int): Validation split percentage
            test (int): Test split percentage

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
                auth=("Authorization", "Bearer "),
                json={"train": train, "val": val, "test": test},
            ),
        )

    async def list(
        self,
        owner: str,
        *,
        limit: int | None = None,
        include_samples: Literal["true", "false"] | None = None,
        include_image_urls: Literal["true", "false"] | None = None,
    ) -> DatasetsListResponse:
        """List datasets.

        Returns datasets owned by the named owner. Private datasets require workspace access.

        Args:
            owner (str): Dataset owner
            limit (int, optional): Maximum datasets to return
            include_samples (Literal["true", "false"], optional): Include sample image previews
            include_image_urls (Literal["true", "false"], optional): Include full-size sample image fallback URLs

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
        task: Literal["detect", "segment", "semantic", "classify", "pose", "obb"] | NotGiven = NOT_GIVEN,
        image_count: int | NotGiven = NOT_GIVEN,
        class_names: list[str] | NotGiven = NOT_GIVEN,
        format: Literal["yolo", "coco", "voc", "raw", "ndjson"] | NotGiven = NOT_GIVEN,
        tags: list[str] | NotGiven = NOT_GIVEN,
        license: Literal[
            "None",
            "CC0-1.0",
            "PDM-1.0",
            "CC-BY-2.5",
            "CC-BY-4.0",
            "CC-BY-NC-2.0",
            "CC-BY-SA-4.0",
            "CC-BY-NC-4.0",
            "CC-BY-NC-SA-3.0",
            "CC-BY-NC-SA-4.0",
            "CC-BY-ND-4.0",
            "CC-BY-NC-ND-4.0",
            "Apache-2.0",
            "MIT",
            "AGPL-3.0",
            "GPL-3.0",
            "Research-Only",
            "Other",
        ]
        | NotGiven = NOT_GIVEN,
        owner: str | NotGiven = NOT_GIVEN,
    ) -> DatasetsCreateResponse:
        """Create a dataset.

        Creates an empty dataset in your personal workspace or a team workspace.

        Args:
            dataset (str): Dataset name used in Platform URLs
            name (str): name request value.
            description (str, optional): description request value.
            metadata (dict[str, Any], optional): Custom JSON metadata with keys limited to 128 characters and at most 500,000 serialized characters.
            visibility (Literal["public", "private"], optional): Resource visibility
            task (Literal["detect", "segment", "semantic", "classify", "pose", "obb"], optional): Dataset task type (depth coming soon)
            image_count (int, optional): imageCount request value.
            class_names (list[str], optional): classNames request value.
            format (Literal["yolo", "coco", "voc", "raw", "ndjson"], optional): Dataset annotation format
            tags (list[str], optional): tags request value.
            license (Literal["None", "CC0-1.0", "PDM-1.0", "CC-BY-2.5", "CC-BY-4.0", "CC-BY-NC-2.0", "CC-BY-SA-4.0", "CC-BY-NC-4.0", "CC-BY-NC-SA-3.0", "CC-BY-NC-SA-4.0", "CC-BY-ND-4.0", "CC-BY-NC-ND-4.0", "Apache-2.0", "MIT", "AGPL-3.0", "GPL-3.0", "Research-Only", "Other"], optional): Dataset license identifier
            owner (str, optional): Workspace owner

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
                    "owner": owner,
                },
            ),
        )

    async def import_from_roboflow(
        self, *, api_key: str, items: list[dict[str, Any]]
    ) -> DatasetsImportFromRoboflowResponse:
        """Import datasets from Roboflow.

        Imports selected Roboflow dataset versions into the API key's workspace.

        Args:
            api_key (str): apiKey request value.
            items (list[dict[str, Any]]): items request value.

        Returns:
            (DatasetsImportFromRoboflowResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsImportFromRoboflowResponse,
            await self._client.request(
                "POST",
                "/api/integrations/roboflow/import",
                auth=("Authorization", "Bearer "),
                json={"apiKey": api_key, "items": items},
            ),
        )

    async def preview_roboflow_import(self, *, api_key: str) -> DatasetsPreviewRoboflowImportResponse:
        """Preview a Roboflow import.

        Validates a Roboflow API key and lists datasets available for import.

        Args:
            api_key (str): apiKey request value.

        Returns:
            (DatasetsPreviewRoboflowImportResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            DatasetsPreviewRoboflowImportResponse,
            await self._client.request(
                "POST",
                "/api/integrations/roboflow/preview",
                auth=("Authorization", "Bearer "),
                json={"apiKey": api_key},
            ),
        )
