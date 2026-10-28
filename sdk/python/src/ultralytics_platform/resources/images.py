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
    ImagesDeleteBulkResponse,
    ImagesDeleteResponse,
    ImagesFindSimilarImagesResponse,
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
                Valid body objects (? marks an optional key): {labels} or {metadata}
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
        """Permanently delete an image.

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
        model_id: str
        | Literal[
            "qwen",
            "gemma",
            "nemotron",
            "moondream",
            "florence2",
            "owlv2",
            "yoloe26x",
            "sam3",
            "sam3.1",
            "groundingdino",
            "gpt-6-astra",
            "gpt-6.1-sol",
            "gpt-6.1-terra",
            "claude-fable-5-1",
            "claude-opus-5-5",
            "claude-sonnet-5-5",
            "gemini-4-argon",
            "grok-4.7",
            "kimi-k3",
            "kimi-k3.1-pro",
            "muse-wonder-1.0",
            "muse-spark-1.3",
            "mimo-v2.6-pro",
            "qwen3.8-max",
            "gpt-6-luna",
            "claude-haiku-5-5",
            "gemini-3.8-flash",
            "gemini-3.5-flash-lite",
            "glm-5.3-flash",
            "deepseek-flash",
            "mimo-v2.6-flash",
            "minimax-m3.1-flash",
        ],
        visual_prompts: Sequence[dict[str, Any]] | NotGiven = NOT_GIVEN,
        confidence: float | NotGiven = NOT_GIVEN,
        iou: float | NotGiven = NOT_GIVEN,
        class_mapping: Sequence[int | None] | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ImagesPredictResponse:
        """Auto-annotate an image.

        Generates label predictions using a YOLO model (ul:// URI), qwen, gemma, nemotron, moondream, florence2, owlv2, yoloe26x, sam3, sam3.1, or groundingdino. Without visualPrompts, hosted models detect the dataset classes (1–200) using model-specific thresholds and return no confidence scores. With visualPrompts, yoloe26x uses up to 200 labels on this image (bbox, segments, or obb) as seeds for detection, segmentation or mask-derived oriented boxes, preserves polygon shape as a visual mask, uses confidence and applies class-aware IoU suppression to the capped model output, and returns scores with the seed dataset class IDs. Visual prompts are not supported by batch annotation. Reaching the detection cap returns partial=true; more objects may exist. Truncated generative output returns only complete boxes with partial=true; objects or classes may be missing. Depth datasets are rejected because dense maps cannot be converted to annotations.

        Args:
            image_id (str): Image ID
            model_id (str | Literal["qwen", "gemma", "nemotron", "moondream", "florence2", "owlv2", "yoloe26x", "sam3", "sam3.1", "groundingdino", "gpt-6-astra", "gpt-6.1-sol", "gpt-6.1-terra", "claude-fable-5-1", "claude-opus-5-5", "claude-sonnet-5-5", "gemini-4-argon", "grok-4.7", "kimi-k3", "kimi-k3.1-pro", "muse-wonder-1.0", "muse-spark-1.3", "mimo-v2.6-pro", "qwen3.8-max", "gpt-6-luna", "claude-haiku-5-5", "gemini-3.8-flash", "gemini-3.5-flash-lite", "glm-5.3-flash", "deepseek-flash", "mimo-v2.6-flash", "minimax-m3.1-flash"]): modelId request value.
            visual_prompts (Sequence[dict[str, Any]], optional): Same-image seed labels (bbox, segments, or obb) for yoloe26x detection, segmentation or mask-derived OBB; classId is the dataset class index
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
                json={
                    "modelId": model_id,
                    "visualPrompts": visual_prompts,
                    "confidence": confidence,
                    "iou": iou,
                    "classMapping": class_mapping,
                },
            ),
        )

    def find_similar_images(
        self,
        image_id: str,
        *,
        include_source_dataset: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ImagesFindSimilarImagesResponse:
        """Find similar images.

        Returns visually similar images from public datasets and your own and team datasets, with their similarity score, source dataset, and license, automatically embedding the query image when needed. By default, excludes the source dataset and datasets containing copies of the query image. Set includeSourceDataset=true to include those datasets. Copies of the query image remain excluded.

        Args:
            image_id (str): Image ID
            include_source_dataset (Literal["true", "false"], optional): Include the source dataset and datasets containing copies of the query image; query copies remain excluded
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (ImagesFindSimilarImagesResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ImagesFindSimilarImagesResponse,
            self._client.request(
                "GET",
                f"/api/images/{_path_parameter(image_id, explode=False, allow_reserved=False)}/similar",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("includeSourceDataset", include_source_dataset, style="form", explode=True)],
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
        """Permanently delete dataset images.

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
                Valid body objects (? marks an optional key): {labels} or {metadata}
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
        """Permanently delete an image.

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
        model_id: str
        | Literal[
            "qwen",
            "gemma",
            "nemotron",
            "moondream",
            "florence2",
            "owlv2",
            "yoloe26x",
            "sam3",
            "sam3.1",
            "groundingdino",
            "gpt-6-astra",
            "gpt-6.1-sol",
            "gpt-6.1-terra",
            "claude-fable-5-1",
            "claude-opus-5-5",
            "claude-sonnet-5-5",
            "gemini-4-argon",
            "grok-4.7",
            "kimi-k3",
            "kimi-k3.1-pro",
            "muse-wonder-1.0",
            "muse-spark-1.3",
            "mimo-v2.6-pro",
            "qwen3.8-max",
            "gpt-6-luna",
            "claude-haiku-5-5",
            "gemini-3.8-flash",
            "gemini-3.5-flash-lite",
            "glm-5.3-flash",
            "deepseek-flash",
            "mimo-v2.6-flash",
            "minimax-m3.1-flash",
        ],
        visual_prompts: Sequence[dict[str, Any]] | NotGiven = NOT_GIVEN,
        confidence: float | NotGiven = NOT_GIVEN,
        iou: float | NotGiven = NOT_GIVEN,
        class_mapping: Sequence[int | None] | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ImagesPredictResponse:
        """Auto-annotate an image.

        Generates label predictions using a YOLO model (ul:// URI), qwen, gemma, nemotron, moondream, florence2, owlv2, yoloe26x, sam3, sam3.1, or groundingdino. Without visualPrompts, hosted models detect the dataset classes (1–200) using model-specific thresholds and return no confidence scores. With visualPrompts, yoloe26x uses up to 200 labels on this image (bbox, segments, or obb) as seeds for detection, segmentation or mask-derived oriented boxes, preserves polygon shape as a visual mask, uses confidence and applies class-aware IoU suppression to the capped model output, and returns scores with the seed dataset class IDs. Visual prompts are not supported by batch annotation. Reaching the detection cap returns partial=true; more objects may exist. Truncated generative output returns only complete boxes with partial=true; objects or classes may be missing. Depth datasets are rejected because dense maps cannot be converted to annotations.

        Args:
            image_id (str): Image ID
            model_id (str | Literal["qwen", "gemma", "nemotron", "moondream", "florence2", "owlv2", "yoloe26x", "sam3", "sam3.1", "groundingdino", "gpt-6-astra", "gpt-6.1-sol", "gpt-6.1-terra", "claude-fable-5-1", "claude-opus-5-5", "claude-sonnet-5-5", "gemini-4-argon", "grok-4.7", "kimi-k3", "kimi-k3.1-pro", "muse-wonder-1.0", "muse-spark-1.3", "mimo-v2.6-pro", "qwen3.8-max", "gpt-6-luna", "claude-haiku-5-5", "gemini-3.8-flash", "gemini-3.5-flash-lite", "glm-5.3-flash", "deepseek-flash", "mimo-v2.6-flash", "minimax-m3.1-flash"]): modelId request value.
            visual_prompts (Sequence[dict[str, Any]], optional): Same-image seed labels (bbox, segments, or obb) for yoloe26x detection, segmentation or mask-derived OBB; classId is the dataset class index
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
                json={
                    "modelId": model_id,
                    "visualPrompts": visual_prompts,
                    "confidence": confidence,
                    "iou": iou,
                    "classMapping": class_mapping,
                },
            ),
        )

    async def find_similar_images(
        self,
        image_id: str,
        *,
        include_source_dataset: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ImagesFindSimilarImagesResponse:
        """Find similar images.

        Returns visually similar images from public datasets and your own and team datasets, with their similarity score, source dataset, and license, automatically embedding the query image when needed. By default, excludes the source dataset and datasets containing copies of the query image. Set includeSourceDataset=true to include those datasets. Copies of the query image remain excluded.

        Args:
            image_id (str): Image ID
            include_source_dataset (Literal["true", "false"], optional): Include the source dataset and datasets containing copies of the query image; query copies remain excluded
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (ImagesFindSimilarImagesResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ImagesFindSimilarImagesResponse,
            await self._client.request(
                "GET",
                f"/api/images/{_path_parameter(image_id, explode=False, allow_reserved=False)}/similar",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("includeSourceDataset", include_source_dataset, style="form", explode=True)],
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
        """Permanently delete dataset images.

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
