# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from __future__ import annotations

from typing import Any, Literal, cast

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
    ImagesRetrieveSignedUrlsResponse,
    ImagesUpdateBulkResponse,
    ImagesUpdateResponse,
)


class Images:
    """Images API operations."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def retrieve(self, image_id: str) -> ImagesRetrieveResponse:
        """Get an image.

        Returns the image fields, custom metadata, annotations, and dataset class names.

        Args:
            image_id (str): Image ID

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
                auth=("Authorization", "Bearer "),
            ),
        )

    def update(self, image_id: str, *, body: dict[str, Any]) -> ImagesUpdateResponse:
        """Update an image.

        Replaces the image annotations or custom metadata.

        Args:
            image_id (str): Image ID
            body (dict[str, Any]): Request body.

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
                auth=("Authorization", "Bearer "),
                json=body,
            ),
        )

    def delete(self, image_id: str) -> ImagesDeleteResponse:
        """Delete an image.

        Permanently deletes one image and its associated labels from a dataset.

        Args:
            image_id (str): Image ID

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
    ) -> ImagesPredictResponse:
        """Auto-annotate an image.

        Runs YOLO inference on an image to generate label predictions for auto-annotation. Supports custom models via ul:// URI.

        Args:
            image_id (str): Image ID
            model_id (str): Fully qualified model URI
            confidence (float, optional): Confidence threshold
            iou (float, optional): IoU threshold for non-maximum suppression

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
                auth=("Authorization", "Bearer "),
                json={"modelId": model_id, "confidence": confidence, "iou": iou},
            ),
        )

    def update_bulk(
        self,
        *,
        image_ids: list[str],
        split: Literal["train", "val", "test"],
        conflict_policy: Literal["skip", "keep_both", "replace"] | NotGiven = NOT_GIVEN,
    ) -> ImagesUpdateBulkResponse:
        """Move images to a different split.

        Moves images to a target split (train, val, or test). Filename and content conflicts require one basket-wide skip, keep-both, or replace policy. Maximum 1000 per batch.

        Args:
            image_ids (list[str]): imageIds request value.
            split (Literal["train", "val", "test"]): Dataset split type
            conflict_policy (Literal["skip", "keep_both", "replace"], optional): How to handle filename or content conflicts

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
                auth=("Authorization", "Bearer "),
                json={"imageIds": image_ids, "split": split, "conflictPolicy": conflict_policy},
            ),
        )

    def delete_bulk(self, *, image_ids: list[str]) -> ImagesDeleteBulkResponse:
        """Delete images from dataset.

        Deletes multiple images and their annotations from the dataset. Removes files from storage in the background. Maximum 1000 images per batch.

        Args:
            image_ids (list[str]): imageIds request value.

        Returns:
            (ImagesDeleteBulkResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ImagesDeleteBulkResponse,
            self._client.request(
                "DELETE", "/api/images/bulk", auth=("Authorization", "Bearer "), json={"imageIds": image_ids}
            ),
        )

    def retrieve_signed_urls(self, *, image_ids: list[str]) -> ImagesRetrieveSignedUrlsResponse:
        """Get signed image URLs.

        Returns temporary signed URLs for the requested image IDs.

        Args:
            image_ids (list[str]): imageIds request value.

        Returns:
            (ImagesRetrieveSignedUrlsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ImagesRetrieveSignedUrlsResponse,
            self._client.request(
                "POST", "/api/images/urls", auth=("Authorization", "Bearer "), json={"imageIds": image_ids}
            ),
        )


class AsyncImages:
    """Asynchronous Images API operations."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def retrieve(self, image_id: str) -> ImagesRetrieveResponse:
        """Get an image.

        Returns the image fields, custom metadata, annotations, and dataset class names.

        Args:
            image_id (str): Image ID

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
                auth=("Authorization", "Bearer "),
            ),
        )

    async def update(self, image_id: str, *, body: dict[str, Any]) -> ImagesUpdateResponse:
        """Update an image.

        Replaces the image annotations or custom metadata.

        Args:
            image_id (str): Image ID
            body (dict[str, Any]): Request body.

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
                auth=("Authorization", "Bearer "),
                json=body,
            ),
        )

    async def delete(self, image_id: str) -> ImagesDeleteResponse:
        """Delete an image.

        Permanently deletes one image and its associated labels from a dataset.

        Args:
            image_id (str): Image ID

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
    ) -> ImagesPredictResponse:
        """Auto-annotate an image.

        Runs YOLO inference on an image to generate label predictions for auto-annotation. Supports custom models via ul:// URI.

        Args:
            image_id (str): Image ID
            model_id (str): Fully qualified model URI
            confidence (float, optional): Confidence threshold
            iou (float, optional): IoU threshold for non-maximum suppression

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
                auth=("Authorization", "Bearer "),
                json={"modelId": model_id, "confidence": confidence, "iou": iou},
            ),
        )

    async def update_bulk(
        self,
        *,
        image_ids: list[str],
        split: Literal["train", "val", "test"],
        conflict_policy: Literal["skip", "keep_both", "replace"] | NotGiven = NOT_GIVEN,
    ) -> ImagesUpdateBulkResponse:
        """Move images to a different split.

        Moves images to a target split (train, val, or test). Filename and content conflicts require one basket-wide skip, keep-both, or replace policy. Maximum 1000 per batch.

        Args:
            image_ids (list[str]): imageIds request value.
            split (Literal["train", "val", "test"]): Dataset split type
            conflict_policy (Literal["skip", "keep_both", "replace"], optional): How to handle filename or content conflicts

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
                auth=("Authorization", "Bearer "),
                json={"imageIds": image_ids, "split": split, "conflictPolicy": conflict_policy},
            ),
        )

    async def delete_bulk(self, *, image_ids: list[str]) -> ImagesDeleteBulkResponse:
        """Delete images from dataset.

        Deletes multiple images and their annotations from the dataset. Removes files from storage in the background. Maximum 1000 images per batch.

        Args:
            image_ids (list[str]): imageIds request value.

        Returns:
            (ImagesDeleteBulkResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ImagesDeleteBulkResponse,
            await self._client.request(
                "DELETE", "/api/images/bulk", auth=("Authorization", "Bearer "), json={"imageIds": image_ids}
            ),
        )

    async def retrieve_signed_urls(self, *, image_ids: list[str]) -> ImagesRetrieveSignedUrlsResponse:
        """Get signed image URLs.

        Returns temporary signed URLs for the requested image IDs.

        Args:
            image_ids (list[str]): imageIds request value.

        Returns:
            (ImagesRetrieveSignedUrlsResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ImagesRetrieveSignedUrlsResponse,
            await self._client.request(
                "POST", "/api/images/urls", auth=("Authorization", "Bearer "), json={"imageIds": image_ids}
            ),
        )
