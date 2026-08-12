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
    ModelsCloneResponse,
    ModelsCreateResponse,
    ModelsDeleteResponse,
    ModelsDeleteTrainingResponse,
    ModelsListResponse,
    ModelsPredictResponse,
    ModelsRetrieveFilesResponse,
    ModelsRetrieveMetadataResponse,
    ModelsRetrieveResponse,
    ModelsRetrieveTrainingResponse,
    ModelsUpdateResponse,
)


class Models:
    """Models API operations."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(
        self, *, project_id: str, limit: float | None = None, fields: str | None = None, ids: str | None = None
    ) -> ModelsListResponse:
        """List models in a project.

        Returns models for a project ID.

        Args:
            project_id (str): Project ID
            limit (float, optional): Number of results to return (default 20, max 100)
            fields (str, optional): Response detail level: 'summary' or 'charts'
            ids (str, optional): Comma-separated model IDs to return

        Returns:
            (ModelsListResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsListResponse,
            self._client.request(
                "GET",
                "/api/models",
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("projectId", project_id, style="form", explode=True),
                    *_query_parameter("limit", limit, style="form", explode=True),
                    *_query_parameter("fields", fields, style="form", explode=True),
                    *_query_parameter("ids", ids, style="form", explode=True),
                ],
            ),
        )

    def create(
        self,
        *,
        project_id: str,
        slug: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        metadata: dict[str, Any] | NotGiven = NOT_GIVEN,
        task: Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"] | NotGiven = NOT_GIVEN,
        train_args: dict[str, Any] | NotGiven = NOT_GIVEN,
        train_results: list[dict[str, Any]] | NotGiven = NOT_GIVEN,
        epochs: float | NotGiven = NOT_GIVEN,
        metrics: dict[str, Any] | NotGiven = NOT_GIVEN,
        version: str | NotGiven = NOT_GIVEN,
        docs: str | NotGiven = NOT_GIVEN,
        environment: dict[str, Any] | NotGiven = NOT_GIVEN,
        completed_at: str | NotGiven = NOT_GIVEN,
    ) -> ModelsCreateResponse:
        """Create a new model.

        Creates a model inside a project. The model can then be trained or have weights uploaded.

        Args:
            project_id (str): Project ID
            slug (str, optional): URL slug
            name (str, optional): Resource name
            description (str, optional): Resource description
            metadata (dict[str, Any], optional): Custom metadata object. Top-level keys are limited to 128 characters and the serialized object is limited to 500,000 characters.
            task (Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"], optional): YOLO task type
            train_args (dict[str, Any], optional): Custom metadata object. Top-level keys are limited to 128 characters and the serialized object is limited to 500,000 characters.
            train_results (list[dict[str, Any]], optional): Per-epoch training results
            epochs (float, optional): Epochs
            metrics (dict[str, Any], optional): Metrics
            version (str, optional): Version identifier
            docs (str, optional): Documentation URL from .pt file
            environment (dict[str, Any], optional): Custom metadata object. Top-level keys are limited to 128 characters and the serialized object is limited to 500,000 characters.
            completed_at (str, optional): Completed At

        Returns:
            (ModelsCreateResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsCreateResponse,
            self._client.request(
                "POST",
                "/api/models",
                auth=("Authorization", "Bearer "),
                json={
                    "projectId": project_id,
                    "slug": slug,
                    "name": name,
                    "description": description,
                    "metadata": metadata,
                    "task": task,
                    "trainArgs": train_args,
                    "trainResults": train_results,
                    "epochs": epochs,
                    "metrics": metrics,
                    "version": version,
                    "docs": docs,
                    "environment": environment,
                    "completedAt": completed_at,
                },
            ),
        )

    def retrieve(self, model_id: str, *, analysis: Literal["1"] | None = None) -> ModelsRetrieveResponse:
        """Get model details.

        Returns model details including training status, per-epoch metrics, validation plots, and file info. Pass `analysis=1` to instead return the per-image validation analysis: worst and best cohorts with up to 100 example images each, TP/FP/FN/F1 at IoU 0.50, image traits, and trait-vs-F1 comparisons.

        Args:
            model_id (str): Model ID
            analysis (Literal["1"], optional): Return the per-image validation analysis, not model details

        Returns:
            (ModelsRetrieveResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsRetrieveResponse,
            self._client.request(
                "GET",
                f"/api/models/{_path_parameter(model_id, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("analysis", analysis, style="form", explode=True)],
            ),
        )

    def update(
        self,
        model_id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        color: str | None | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        metadata: dict[str, Any] | NotGiven = NOT_GIVEN,
        status: Literal["pending", "untrained", "starting", "running", "completed", "failed", "cancelled"]
        | NotGiven = NOT_GIVEN,
        license: Literal[
            "None",
            "Apache-2.0",
            "MIT",
            "BSD-3-Clause",
            "AGPL-3.0",
            "GPL-3.0",
            "LGPL-3.0",
            "MPL-2.0",
            "EUPL-1.1",
            "Unlicense",
            "CC0-1.0",
            "Ultralytics-Enterprise",
            "Other",
        ]
        | NotGiven = NOT_GIVEN,
        dataset_slug: str | None | NotGiven = NOT_GIVEN,
        train_args: dict[str, Any] | NotGiven = NOT_GIVEN,
        train_results: list[dict[str, Any]] | NotGiven = NOT_GIVEN,
        epochs: float | NotGiven = NOT_GIVEN,
        best_epoch: float | NotGiven = NOT_GIVEN,
        best_fitness: float | NotGiven = NOT_GIVEN,
        version: str | NotGiven = NOT_GIVEN,
        training_error: dict[str, Any] | NotGiven = NOT_GIVEN,
    ) -> ModelsUpdateResponse:
        """Update a model.

        Update model properties like name, description, metadata, or training status.

        Args:
            model_id (str): Model ID
            name (str, optional): Resource name
            color (str | None, optional): Display color
            description (str, optional): Resource description
            metadata (dict[str, Any], optional): Custom metadata object. Top-level keys are limited to 128 characters and the serialized object is limited to 500,000 characters.
            status (Literal["pending", "untrained", "starting", "running", "completed", "failed", "cancelled"], optional): Training/model status
            license (Literal["None", "Apache-2.0", "MIT", "BSD-3-Clause", "AGPL-3.0", "GPL-3.0", "LGPL-3.0", "MPL-2.0", "EUPL-1.1", "Unlicense", "CC0-1.0", "Ultralytics-Enterprise", "Other"], optional): Project/model license identifier
            dataset_slug (str | None, optional): Dataset URL slug
            train_args (dict[str, Any], optional): Custom metadata object. Top-level keys are limited to 128 characters and the serialized object is limited to 500,000 characters.
            train_results (list[dict[str, Any]], optional): Per-epoch training results
            epochs (float, optional): Epochs
            best_epoch (float, optional): Best Epoch
            best_fitness (float, optional): Best Fitness
            version (str, optional): Version identifier
            training_error (dict[str, Any], optional): Training failure details

        Returns:
            (ModelsUpdateResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsUpdateResponse,
            self._client.request(
                "PATCH",
                f"/api/models/{_path_parameter(model_id, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
                json={
                    "name": name,
                    "color": color,
                    "description": description,
                    "metadata": metadata,
                    "status": status,
                    "license": license,
                    "datasetSlug": dataset_slug,
                    "trainArgs": train_args,
                    "trainResults": train_results,
                    "epochs": epochs,
                    "bestEpoch": best_epoch,
                    "bestFitness": best_fitness,
                    "version": version,
                    "trainingError": training_error,
                },
            ),
        )

    def delete(self, model_id: str) -> ModelsDeleteResponse:
        """Delete a model.

        Moves the model to trash. Can be restored within 30 days.

        Args:
            model_id (str): Model ID

        Returns:
            (ModelsDeleteResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsDeleteResponse,
            self._client.request(
                "DELETE",
                f"/api/models/{_path_parameter(model_id, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
            ),
        )

    def retrieve_metadata(self, model_id: str) -> ModelsRetrieveMetadataResponse:
        """Get model metadata.

        Returns custom metadata and Ultralytics-managed properties without adding them to normal payloads.

        Args:
            model_id (str): Model ID

        Returns:
            (ModelsRetrieveMetadataResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsRetrieveMetadataResponse,
            self._client.request(
                "GET",
                f"/api/models/{_path_parameter(model_id, explode=False, allow_reserved=False)}/metadata",
                auth=("Authorization", "Bearer "),
            ),
        )

    def clone(
        self,
        model_id: str,
        *,
        target_project_slug: str,
        model_name: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        owner: str | NotGiven = NOT_GIVEN,
    ) -> ModelsCloneResponse:
        """Clone an accessible model.

        Copies a public, owned, or shared model into an existing project.

        Args:
            model_id (str): Model ID
            target_project_slug (str): Target project URL slug
            model_name (str, optional): Model name
            description (str, optional): Resource description
            owner (str, optional): Workspace username

        Returns:
            (ModelsCloneResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsCloneResponse,
            self._client.request(
                "POST",
                f"/api/models/{_path_parameter(model_id, explode=False, allow_reserved=False)}/clone",
                auth=("Authorization", "Bearer "),
                json={
                    "targetProjectSlug": target_project_slug,
                    "modelName": model_name,
                    "description": description,
                    "owner": owner,
                },
            ),
        )

    def retrieve_files(self, model_id: str) -> ModelsRetrieveFilesResponse:
        """Download model files.

        Returns signed download URLs for model weights and exported files. URLs are valid for 1 hour.

        Args:
            model_id (str): Model ID

        Returns:
            (ModelsRetrieveFilesResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsRetrieveFilesResponse,
            self._client.request(
                "GET",
                f"/api/models/{_path_parameter(model_id, explode=False, allow_reserved=False)}/files",
                auth=("Authorization", "Bearer "),
            ),
        )

    def predict(self, model_id: str, *, body: dict[str, Any]) -> ModelsPredictResponse:
        """Run inference on a model.

        Send an image to run YOLO inference using shared GPU infrastructure. Supports all YOLO tasks (detect, segment, classify, pose, obb).

        Args:
            model_id (str): Model ID
            body (dict[str, Any]): Request body.

        Returns:
            (ModelsPredictResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsPredictResponse,
            self._client.request(
                "POST",
                f"/api/models/{_path_parameter(model_id, explode=False, allow_reserved=False)}/predict",
                auth=("Authorization", "Bearer "),
                data={key: value for key, value in body.items() if key not in ["file"]},
                files={key: body[key] for key in ["file"] if key in body},
            ),
        )

    def retrieve_training(self, model_id: str) -> ModelsRetrieveTrainingResponse:
        """Check training progress.

        Returns live status, epoch progress, timing, compute, metrics, and error details.

        Args:
            model_id (str): Model ID

        Returns:
            (ModelsRetrieveTrainingResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsRetrieveTrainingResponse,
            self._client.request(
                "GET",
                f"/api/models/{_path_parameter(model_id, explode=False, allow_reserved=False)}/training",
                auth=("Authorization", "Bearer "),
            ),
        )

    def delete_training(self, model_id: str) -> ModelsDeleteTrainingResponse:
        """Cancel training.

        Terminates the compute instance and marks the model as cancelled.

        Args:
            model_id (str): Model ID

        Returns:
            (ModelsDeleteTrainingResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsDeleteTrainingResponse,
            self._client.request(
                "DELETE",
                f"/api/models/{_path_parameter(model_id, explode=False, allow_reserved=False)}/training",
                auth=("Authorization", "Bearer "),
            ),
        )


class AsyncModels:
    """Asynchronous Models API operations."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(
        self, *, project_id: str, limit: float | None = None, fields: str | None = None, ids: str | None = None
    ) -> ModelsListResponse:
        """List models in a project.

        Returns models for a project ID.

        Args:
            project_id (str): Project ID
            limit (float, optional): Number of results to return (default 20, max 100)
            fields (str, optional): Response detail level: 'summary' or 'charts'
            ids (str, optional): Comma-separated model IDs to return

        Returns:
            (ModelsListResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsListResponse,
            await self._client.request(
                "GET",
                "/api/models",
                auth=("Authorization", "Bearer "),
                params=[
                    *_query_parameter("projectId", project_id, style="form", explode=True),
                    *_query_parameter("limit", limit, style="form", explode=True),
                    *_query_parameter("fields", fields, style="form", explode=True),
                    *_query_parameter("ids", ids, style="form", explode=True),
                ],
            ),
        )

    async def create(
        self,
        *,
        project_id: str,
        slug: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        metadata: dict[str, Any] | NotGiven = NOT_GIVEN,
        task: Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"] | NotGiven = NOT_GIVEN,
        train_args: dict[str, Any] | NotGiven = NOT_GIVEN,
        train_results: list[dict[str, Any]] | NotGiven = NOT_GIVEN,
        epochs: float | NotGiven = NOT_GIVEN,
        metrics: dict[str, Any] | NotGiven = NOT_GIVEN,
        version: str | NotGiven = NOT_GIVEN,
        docs: str | NotGiven = NOT_GIVEN,
        environment: dict[str, Any] | NotGiven = NOT_GIVEN,
        completed_at: str | NotGiven = NOT_GIVEN,
    ) -> ModelsCreateResponse:
        """Create a new model.

        Creates a model inside a project. The model can then be trained or have weights uploaded.

        Args:
            project_id (str): Project ID
            slug (str, optional): URL slug
            name (str, optional): Resource name
            description (str, optional): Resource description
            metadata (dict[str, Any], optional): Custom metadata object. Top-level keys are limited to 128 characters and the serialized object is limited to 500,000 characters.
            task (Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"], optional): YOLO task type
            train_args (dict[str, Any], optional): Custom metadata object. Top-level keys are limited to 128 characters and the serialized object is limited to 500,000 characters.
            train_results (list[dict[str, Any]], optional): Per-epoch training results
            epochs (float, optional): Epochs
            metrics (dict[str, Any], optional): Metrics
            version (str, optional): Version identifier
            docs (str, optional): Documentation URL from .pt file
            environment (dict[str, Any], optional): Custom metadata object. Top-level keys are limited to 128 characters and the serialized object is limited to 500,000 characters.
            completed_at (str, optional): Completed At

        Returns:
            (ModelsCreateResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsCreateResponse,
            await self._client.request(
                "POST",
                "/api/models",
                auth=("Authorization", "Bearer "),
                json={
                    "projectId": project_id,
                    "slug": slug,
                    "name": name,
                    "description": description,
                    "metadata": metadata,
                    "task": task,
                    "trainArgs": train_args,
                    "trainResults": train_results,
                    "epochs": epochs,
                    "metrics": metrics,
                    "version": version,
                    "docs": docs,
                    "environment": environment,
                    "completedAt": completed_at,
                },
            ),
        )

    async def retrieve(self, model_id: str, *, analysis: Literal["1"] | None = None) -> ModelsRetrieveResponse:
        """Get model details.

        Returns model details including training status, per-epoch metrics, validation plots, and file info. Pass `analysis=1` to instead return the per-image validation analysis: worst and best cohorts with up to 100 example images each, TP/FP/FN/F1 at IoU 0.50, image traits, and trait-vs-F1 comparisons.

        Args:
            model_id (str): Model ID
            analysis (Literal["1"], optional): Return the per-image validation analysis, not model details

        Returns:
            (ModelsRetrieveResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsRetrieveResponse,
            await self._client.request(
                "GET",
                f"/api/models/{_path_parameter(model_id, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("analysis", analysis, style="form", explode=True)],
            ),
        )

    async def update(
        self,
        model_id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        color: str | None | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        metadata: dict[str, Any] | NotGiven = NOT_GIVEN,
        status: Literal["pending", "untrained", "starting", "running", "completed", "failed", "cancelled"]
        | NotGiven = NOT_GIVEN,
        license: Literal[
            "None",
            "Apache-2.0",
            "MIT",
            "BSD-3-Clause",
            "AGPL-3.0",
            "GPL-3.0",
            "LGPL-3.0",
            "MPL-2.0",
            "EUPL-1.1",
            "Unlicense",
            "CC0-1.0",
            "Ultralytics-Enterprise",
            "Other",
        ]
        | NotGiven = NOT_GIVEN,
        dataset_slug: str | None | NotGiven = NOT_GIVEN,
        train_args: dict[str, Any] | NotGiven = NOT_GIVEN,
        train_results: list[dict[str, Any]] | NotGiven = NOT_GIVEN,
        epochs: float | NotGiven = NOT_GIVEN,
        best_epoch: float | NotGiven = NOT_GIVEN,
        best_fitness: float | NotGiven = NOT_GIVEN,
        version: str | NotGiven = NOT_GIVEN,
        training_error: dict[str, Any] | NotGiven = NOT_GIVEN,
    ) -> ModelsUpdateResponse:
        """Update a model.

        Update model properties like name, description, metadata, or training status.

        Args:
            model_id (str): Model ID
            name (str, optional): Resource name
            color (str | None, optional): Display color
            description (str, optional): Resource description
            metadata (dict[str, Any], optional): Custom metadata object. Top-level keys are limited to 128 characters and the serialized object is limited to 500,000 characters.
            status (Literal["pending", "untrained", "starting", "running", "completed", "failed", "cancelled"], optional): Training/model status
            license (Literal["None", "Apache-2.0", "MIT", "BSD-3-Clause", "AGPL-3.0", "GPL-3.0", "LGPL-3.0", "MPL-2.0", "EUPL-1.1", "Unlicense", "CC0-1.0", "Ultralytics-Enterprise", "Other"], optional): Project/model license identifier
            dataset_slug (str | None, optional): Dataset URL slug
            train_args (dict[str, Any], optional): Custom metadata object. Top-level keys are limited to 128 characters and the serialized object is limited to 500,000 characters.
            train_results (list[dict[str, Any]], optional): Per-epoch training results
            epochs (float, optional): Epochs
            best_epoch (float, optional): Best Epoch
            best_fitness (float, optional): Best Fitness
            version (str, optional): Version identifier
            training_error (dict[str, Any], optional): Training failure details

        Returns:
            (ModelsUpdateResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsUpdateResponse,
            await self._client.request(
                "PATCH",
                f"/api/models/{_path_parameter(model_id, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
                json={
                    "name": name,
                    "color": color,
                    "description": description,
                    "metadata": metadata,
                    "status": status,
                    "license": license,
                    "datasetSlug": dataset_slug,
                    "trainArgs": train_args,
                    "trainResults": train_results,
                    "epochs": epochs,
                    "bestEpoch": best_epoch,
                    "bestFitness": best_fitness,
                    "version": version,
                    "trainingError": training_error,
                },
            ),
        )

    async def delete(self, model_id: str) -> ModelsDeleteResponse:
        """Delete a model.

        Moves the model to trash. Can be restored within 30 days.

        Args:
            model_id (str): Model ID

        Returns:
            (ModelsDeleteResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsDeleteResponse,
            await self._client.request(
                "DELETE",
                f"/api/models/{_path_parameter(model_id, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
            ),
        )

    async def retrieve_metadata(self, model_id: str) -> ModelsRetrieveMetadataResponse:
        """Get model metadata.

        Returns custom metadata and Ultralytics-managed properties without adding them to normal payloads.

        Args:
            model_id (str): Model ID

        Returns:
            (ModelsRetrieveMetadataResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsRetrieveMetadataResponse,
            await self._client.request(
                "GET",
                f"/api/models/{_path_parameter(model_id, explode=False, allow_reserved=False)}/metadata",
                auth=("Authorization", "Bearer "),
            ),
        )

    async def clone(
        self,
        model_id: str,
        *,
        target_project_slug: str,
        model_name: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        owner: str | NotGiven = NOT_GIVEN,
    ) -> ModelsCloneResponse:
        """Clone an accessible model.

        Copies a public, owned, or shared model into an existing project.

        Args:
            model_id (str): Model ID
            target_project_slug (str): Target project URL slug
            model_name (str, optional): Model name
            description (str, optional): Resource description
            owner (str, optional): Workspace username

        Returns:
            (ModelsCloneResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsCloneResponse,
            await self._client.request(
                "POST",
                f"/api/models/{_path_parameter(model_id, explode=False, allow_reserved=False)}/clone",
                auth=("Authorization", "Bearer "),
                json={
                    "targetProjectSlug": target_project_slug,
                    "modelName": model_name,
                    "description": description,
                    "owner": owner,
                },
            ),
        )

    async def retrieve_files(self, model_id: str) -> ModelsRetrieveFilesResponse:
        """Download model files.

        Returns signed download URLs for model weights and exported files. URLs are valid for 1 hour.

        Args:
            model_id (str): Model ID

        Returns:
            (ModelsRetrieveFilesResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsRetrieveFilesResponse,
            await self._client.request(
                "GET",
                f"/api/models/{_path_parameter(model_id, explode=False, allow_reserved=False)}/files",
                auth=("Authorization", "Bearer "),
            ),
        )

    async def predict(self, model_id: str, *, body: dict[str, Any]) -> ModelsPredictResponse:
        """Run inference on a model.

        Send an image to run YOLO inference using shared GPU infrastructure. Supports all YOLO tasks (detect, segment, classify, pose, obb).

        Args:
            model_id (str): Model ID
            body (dict[str, Any]): Request body.

        Returns:
            (ModelsPredictResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsPredictResponse,
            await self._client.request(
                "POST",
                f"/api/models/{_path_parameter(model_id, explode=False, allow_reserved=False)}/predict",
                auth=("Authorization", "Bearer "),
                data={key: value for key, value in body.items() if key not in ["file"]},
                files={key: body[key] for key in ["file"] if key in body},
            ),
        )

    async def retrieve_training(self, model_id: str) -> ModelsRetrieveTrainingResponse:
        """Check training progress.

        Returns live status, epoch progress, timing, compute, metrics, and error details.

        Args:
            model_id (str): Model ID

        Returns:
            (ModelsRetrieveTrainingResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsRetrieveTrainingResponse,
            await self._client.request(
                "GET",
                f"/api/models/{_path_parameter(model_id, explode=False, allow_reserved=False)}/training",
                auth=("Authorization", "Bearer "),
            ),
        )

    async def delete_training(self, model_id: str) -> ModelsDeleteTrainingResponse:
        """Cancel training.

        Terminates the compute instance and marks the model as cancelled.

        Args:
            model_id (str): Model ID

        Returns:
            (ModelsDeleteTrainingResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsDeleteTrainingResponse,
            await self._client.request(
                "DELETE",
                f"/api/models/{_path_parameter(model_id, explode=False, allow_reserved=False)}/training",
                auth=("Authorization", "Bearer "),
            ),
        )
