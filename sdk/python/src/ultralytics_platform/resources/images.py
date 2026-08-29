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
)
from ..types import (
    ImagesDeleteBulkResponse,
    ImagesDeleteResponse,
    ImagesPredictResponse,
    ImagesRetrieveResponse,
    ImagesUpdateBulkResponse,
    ImagesUpdateResponse,
    ImagesUrlsResponse,
)


class Images:
    """Images API operations."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def retrieve(
        self, image_id: str, timeout: float | httpx.Timeout | None = None, extra_headers: dict[str, str] | None = None
    ) -> ImagesRetrieveResponse:
        """Get an image.

        Returns the image fields, custom metadata, annotations, and dataset class names.

        Args:
            image_id (str): Image ID
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (ImagesRetrieveResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ImagesRetrieveResponse,
            self._client.request(
                "GET",
                f"/api/images/{_path_parameter(image_id, explode=False, allow_reserved=False)}",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    def update(
        self,
        image_id: str,
        *,
        body: dict[str, Any],
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ImagesUpdateResponse:
        """Update an image.

        Replaces either custom metadata, for example `{"metadata":{"location":"strasbourg"}}`, or annotations. Use one consistent flat keypoint shape: pairs `[x1, y1, x2, y2]` or triples `[x1, y1, visibility1, x2, y2, visibility2]`.

        Args:
            image_id (str): Image ID
            body (dict[str, Any]): Replace labels for an image Or Replace custom metadata for an image
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (ImagesUpdateResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ImagesUpdateResponse,
            self._client.request(
                "PATCH",
                f"/api/images/{_path_parameter(image_id, explode=False, allow_reserved=False)}",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json=body,
            ),
        )

    def delete(
        self, image_id: str, timeout: float | httpx.Timeout | None = None, extra_headers: dict[str, str] | None = None
    ) -> ImagesDeleteResponse:
        """Delete an image.

        Permanently deletes one image and its associated labels from a dataset.

        Args:
            image_id (str): Image ID
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (ImagesDeleteResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ImagesDeleteResponse,
            self._client.request(
                "DELETE",
                f"/api/images/{_path_parameter(image_id, explode=False, allow_reserved=False)}",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    def predict(
        self,
        image_id: str,
        *,
        model_id: str,
        confidence: float | NotGiven = NOT_GIVEN,
        iou: float | NotGiven = NOT_GIVEN,
        class_mapping: Sequence[int | None] | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ImagesPredictResponse:
        """Auto-annotate an image.

        Runs YOLO inference on an image to generate label predictions for auto-annotation. Supports custom models via ul:// URI. Depth datasets are rejected because dense maps cannot be converted to annotations.

        Args:
            image_id (str): Image ID
            model_id (str): Fully qualified model URI
            confidence (float, optional): Confidence threshold
            iou (float, optional): IoU threshold for non-maximum suppression
            class_mapping (Sequence[int | None], optional): Dataset class index for each model class, or null to drop it
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (ImagesPredictResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ImagesPredictResponse,
            self._client.request(
                "POST",
                f"/api/images/{_path_parameter(image_id, explode=False, allow_reserved=False)}/predict",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={"modelId": model_id, "confidence": confidence, "iou": iou, "classMapping": class_mapping},
            ),
        )

    def update_bulk(
        self,
        *,
        image_ids: Sequence[str],
        split: Literal["train", "val", "test"],
        conflict_policy: Literal["skip", "keep_both", "replace"] | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ImagesUpdateBulkResponse:
        """Move images to a different split.

        Moves images to a target split (train, val, or test). Filename and content conflicts require one basket-wide skip, keep-both, or replace policy. Maximum 1000 per batch.

        Args:
            image_ids (Sequence[str]): imageIds request value.
            split (Literal["train", "val", "test"]): Dataset split type
            conflict_policy (Literal["skip", "keep_both", "replace"], optional): How to handle filename or content conflicts
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (ImagesUpdateBulkResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ImagesUpdateBulkResponse,
            self._client.request(
                "PATCH",
                "/api/images/bulk",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={"imageIds": image_ids, "split": split, "conflictPolicy": conflict_policy},
            ),
        )

    def delete_bulk(
        self,
        *,
        image_ids: Sequence[str],
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ImagesDeleteBulkResponse:
        """Delete images from dataset.

        Deletes multiple images and their annotations from the dataset. Removes files from storage in the background. Maximum 1000 images per batch.

        Args:
            image_ids (Sequence[str]): imageIds request value.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (ImagesDeleteBulkResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ImagesDeleteBulkResponse,
            self._client.request(
                "DELETE",
                "/api/images/bulk",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={"imageIds": image_ids},
            ),
        )

    def urls(
        self,
        *,
        image_ids: Sequence[str],
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ImagesUrlsResponse:
        """Get signed image URLs.

        Returns temporary signed URLs for the requested image IDs.

        Args:
            image_ids (Sequence[str]): imageIds request value.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (ImagesUrlsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ImagesUrlsResponse,
            self._client.request(
                "POST",
                "/api/images/urls",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={"imageIds": image_ids},
            ),
        )


class AsyncImages:
    """Asynchronous Images API operations."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def retrieve(
        self, image_id: str, timeout: float | httpx.Timeout | None = None, extra_headers: dict[str, str] | None = None
    ) -> ImagesRetrieveResponse:
        """Get an image.

        Returns the image fields, custom metadata, annotations, and dataset class names.

        Args:
            image_id (str): Image ID
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (ImagesRetrieveResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ImagesRetrieveResponse,
            await self._client.request(
                "GET",
                f"/api/images/{_path_parameter(image_id, explode=False, allow_reserved=False)}",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    async def update(
        self,
        image_id: str,
        *,
        body: dict[str, Any],
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ImagesUpdateResponse:
        """Update an image.

        Replaces either custom metadata, for example `{"metadata":{"location":"strasbourg"}}`, or annotations. Use one consistent flat keypoint shape: pairs `[x1, y1, x2, y2]` or triples `[x1, y1, visibility1, x2, y2, visibility2]`.

        Args:
            image_id (str): Image ID
            body (dict[str, Any]): Replace labels for an image Or Replace custom metadata for an image
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (ImagesUpdateResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ImagesUpdateResponse,
            await self._client.request(
                "PATCH",
                f"/api/images/{_path_parameter(image_id, explode=False, allow_reserved=False)}",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json=body,
            ),
        )

    async def delete(
        self, image_id: str, timeout: float | httpx.Timeout | None = None, extra_headers: dict[str, str] | None = None
    ) -> ImagesDeleteResponse:
        """Delete an image.

        Permanently deletes one image and its associated labels from a dataset.

        Args:
            image_id (str): Image ID
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (ImagesDeleteResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ImagesDeleteResponse,
            await self._client.request(
                "DELETE",
                f"/api/images/{_path_parameter(image_id, explode=False, allow_reserved=False)}",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    async def predict(
        self,
        image_id: str,
        *,
        model_id: str,
        confidence: float | NotGiven = NOT_GIVEN,
        iou: float | NotGiven = NOT_GIVEN,
        class_mapping: Sequence[int | None] | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ImagesPredictResponse:
        """Auto-annotate an image.

        Runs YOLO inference on an image to generate label predictions for auto-annotation. Supports custom models via ul:// URI. Depth datasets are rejected because dense maps cannot be converted to annotations.

        Args:
            image_id (str): Image ID
            model_id (str): Fully qualified model URI
            confidence (float, optional): Confidence threshold
            iou (float, optional): IoU threshold for non-maximum suppression
            class_mapping (Sequence[int | None], optional): Dataset class index for each model class, or null to drop it
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (ImagesPredictResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ImagesPredictResponse,
            await self._client.request(
                "POST",
                f"/api/images/{_path_parameter(image_id, explode=False, allow_reserved=False)}/predict",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={"modelId": model_id, "confidence": confidence, "iou": iou, "classMapping": class_mapping},
            ),
        )

    async def update_bulk(
        self,
        *,
        image_ids: Sequence[str],
        split: Literal["train", "val", "test"],
        conflict_policy: Literal["skip", "keep_both", "replace"] | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ImagesUpdateBulkResponse:
        """Move images to a different split.

        Moves images to a target split (train, val, or test). Filename and content conflicts require one basket-wide skip, keep-both, or replace policy. Maximum 1000 per batch.

        Args:
            image_ids (Sequence[str]): imageIds request value.
            split (Literal["train", "val", "test"]): Dataset split type
            conflict_policy (Literal["skip", "keep_both", "replace"], optional): How to handle filename or content conflicts
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (ImagesUpdateBulkResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ImagesUpdateBulkResponse,
            await self._client.request(
                "PATCH",
                "/api/images/bulk",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={"imageIds": image_ids, "split": split, "conflictPolicy": conflict_policy},
            ),
        )

    async def delete_bulk(
        self,
        *,
        image_ids: Sequence[str],
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ImagesDeleteBulkResponse:
        """Delete images from dataset.

        Deletes multiple images and their annotations from the dataset. Removes files from storage in the background. Maximum 1000 images per batch.

        Args:
            image_ids (Sequence[str]): imageIds request value.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (ImagesDeleteBulkResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ImagesDeleteBulkResponse,
            await self._client.request(
                "DELETE",
                "/api/images/bulk",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={"imageIds": image_ids},
            ),
        )

    async def urls(
        self,
        *,
        image_ids: Sequence[str],
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ImagesUrlsResponse:
        """Get signed image URLs.

        Returns temporary signed URLs for the requested image IDs.

        Args:
            image_ids (Sequence[str]): imageIds request value.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (ImagesUrlsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ImagesUrlsResponse,
            await self._client.request(
                "POST",
                "/api/images/urls",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json={"imageIds": image_ids},
            ),
        )
