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
    ModelsRetrieveResponse,
    ModelsRetrieveTrainingResponse,
    ModelsUpdateResponse,
)


class Models:
    """Models API operations."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def clone(
        self,
        owner: str,
        project: str,
        model: str,
        *,
        project_body: str,
        owner_body: str | NotGiven = NOT_GIVEN,
        model_body: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
    ) -> ModelsCloneResponse:
        """Clone a model.

        Copies an accessible model into an existing project.

        Args:
            owner (str): Project owner
            project (str): Project name
            model (str): Model name
            owner_body (str, optional): Destination owner
            project_body (str): Destination project
            model_body (str, optional): Destination model name
            name (str, optional): Destination display name
            description (str, optional): description request value.

        Returns:
            (ModelsCloneResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsCloneResponse,
            self._client.request(
                "POST",
                f"/api/models/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}/{_path_parameter(model, explode=False, allow_reserved=False)}/clone",
                auth=("Authorization", "Bearer "),
                json={
                    "owner": owner_body,
                    "project": project_body,
                    "model": model_body,
                    "name": name,
                    "description": description,
                },
            ),
        )

    def retrieve(
        self, owner: str, project: str, model: str, *, analysis: Literal["1"] | None = None
    ) -> ModelsRetrieveResponse:
        """Get model details.

        Returns model details. Pass analysis=1 to return per-image validation analysis instead.

        Args:
            owner (str): Project owner
            project (str): Project name
            model (str): Model name
            analysis (Literal["1"], optional): Return per-image validation analysis instead of model details

        Returns:
            (ModelsRetrieveResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsRetrieveResponse,
            self._client.request(
                "GET",
                f"/api/models/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}/{_path_parameter(model, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("analysis", analysis, style="form", explode=True)],
            ),
        )

    def update(
        self,
        owner: str,
        project: str,
        model: str,
        *,
        starred: bool | NotGiven = NOT_GIVEN,
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

        Updates model properties such as name, description, metadata, or training status.

        Args:
            owner (str): Project owner
            project (str): Project name
            model (str): Model name
            starred (bool, optional): starred request value.
            name (str, optional): name request value.
            color (str | None, optional): color request value.
            description (str, optional): description request value.
            metadata (dict[str, Any], optional): Custom JSON metadata with keys limited to 128 characters and at most 500,000 serialized characters.
            status (Literal["pending", "untrained", "starting", "running", "completed", "failed", "cancelled"], optional): Training/model status
            license (Literal["None", "Apache-2.0", "MIT", "BSD-3-Clause", "AGPL-3.0", "GPL-3.0", "LGPL-3.0", "MPL-2.0", "EUPL-1.1", "Unlicense", "CC0-1.0", "Ultralytics-Enterprise", "Other"], optional): Project/model license identifier
            dataset_slug (str | None, optional): datasetSlug request value.
            train_args (dict[str, Any], optional): Custom JSON metadata with keys limited to 128 characters and at most 500,000 serialized characters.
            train_results (list[dict[str, Any]], optional): trainResults request value.
            epochs (float, optional): epochs request value.
            best_epoch (float, optional): bestEpoch request value.
            best_fitness (float, optional): bestFitness request value.
            version (str, optional): version request value.
            training_error (dict[str, Any], optional): trainingError request value.

        Returns:
            (ModelsUpdateResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsUpdateResponse,
            self._client.request(
                "PATCH",
                f"/api/models/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}/{_path_parameter(model, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
                json={
                    "starred": starred,
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

    def delete(self, owner: str, project: str, model: str) -> ModelsDeleteResponse:
        """Delete a model.

        Moves the model to trash for 30 days.

        Args:
            owner (str): Project owner
            project (str): Project name
            model (str): Model name

        Returns:
            (ModelsDeleteResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsDeleteResponse,
            self._client.request(
                "DELETE",
                f"/api/models/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}/{_path_parameter(model, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
            ),
        )

    def retrieve_files(self, owner: str, project: str, model: str) -> ModelsRetrieveFilesResponse:
        """Download model files.

        Returns a short-lived download URL for model weights.

        Args:
            owner (str): Project owner
            project (str): Project name
            model (str): Model name

        Returns:
            (ModelsRetrieveFilesResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsRetrieveFilesResponse,
            self._client.request(
                "GET",
                f"/api/models/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}/{_path_parameter(model, explode=False, allow_reserved=False)}/files",
                auth=("Authorization", "Bearer "),
            ),
        )

    def predict(self, owner: str, project: str, model: str, *, body: dict[str, Any]) -> ModelsPredictResponse:
        """Run model inference.

        Runs inference on an image or video using a trained model.

        Args:
            owner (str): Project owner
            project (str): Project name
            model (str): Model name
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
                f"/api/models/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}/{_path_parameter(model, explode=False, allow_reserved=False)}/predict",
                auth=("Authorization", "Bearer "),
                data={key: value for key, value in body.items() if key not in ["file"]},
                files={key: body[key] for key in ["file"] if key in body},
            ),
        )

    def retrieve_training(self, owner: str, project: str, model: str) -> ModelsRetrieveTrainingResponse:
        """Check training progress.

        Returns live status, epoch progress, timing, compute, metrics, and safe error details.

        Args:
            owner (str): Project owner
            project (str): Project name
            model (str): Model name

        Returns:
            (ModelsRetrieveTrainingResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsRetrieveTrainingResponse,
            self._client.request(
                "GET",
                f"/api/models/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}/{_path_parameter(model, explode=False, allow_reserved=False)}/training",
                auth=("Authorization", "Bearer "),
            ),
        )

    def delete_training(self, owner: str, project: str, model: str) -> ModelsDeleteTrainingResponse:
        """Cancel training.

        Terminates active compute and marks the model as cancelled.

        Args:
            owner (str): Project owner
            project (str): Project name
            model (str): Model name

        Returns:
            (ModelsDeleteTrainingResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsDeleteTrainingResponse,
            self._client.request(
                "DELETE",
                f"/api/models/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}/{_path_parameter(model, explode=False, allow_reserved=False)}/training",
                auth=("Authorization", "Bearer "),
            ),
        )

    def list(self, owner: str, project: str, *, limit: int | None = None) -> ModelsListResponse:
        """List models in a project.

        Returns models by owner and project name.

        Args:
            owner (str): Project owner
            project (str): Project name
            limit (int, optional): Maximum models to return

        Returns:
            (ModelsListResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsListResponse,
            self._client.request(
                "GET",
                f"/api/models/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("limit", limit, style="form", explode=True)],
            ),
        )

    def create(self, *, body: dict[str, Any]) -> ModelsCreateResponse:
        """Create a model.

        Creates a model in an existing project.

        Args:
            body (dict[str, Any]): API request for creating a new model

        Returns:
            (ModelsCreateResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsCreateResponse,
            self._client.request("POST", "/api/models", auth=("Authorization", "Bearer "), json=body),
        )


class AsyncModels:
    """Asynchronous Models API operations."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def clone(
        self,
        owner: str,
        project: str,
        model: str,
        *,
        project_body: str,
        owner_body: str | NotGiven = NOT_GIVEN,
        model_body: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
    ) -> ModelsCloneResponse:
        """Clone a model.

        Copies an accessible model into an existing project.

        Args:
            owner (str): Project owner
            project (str): Project name
            model (str): Model name
            owner_body (str, optional): Destination owner
            project_body (str): Destination project
            model_body (str, optional): Destination model name
            name (str, optional): Destination display name
            description (str, optional): description request value.

        Returns:
            (ModelsCloneResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsCloneResponse,
            await self._client.request(
                "POST",
                f"/api/models/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}/{_path_parameter(model, explode=False, allow_reserved=False)}/clone",
                auth=("Authorization", "Bearer "),
                json={
                    "owner": owner_body,
                    "project": project_body,
                    "model": model_body,
                    "name": name,
                    "description": description,
                },
            ),
        )

    async def retrieve(
        self, owner: str, project: str, model: str, *, analysis: Literal["1"] | None = None
    ) -> ModelsRetrieveResponse:
        """Get model details.

        Returns model details. Pass analysis=1 to return per-image validation analysis instead.

        Args:
            owner (str): Project owner
            project (str): Project name
            model (str): Model name
            analysis (Literal["1"], optional): Return per-image validation analysis instead of model details

        Returns:
            (ModelsRetrieveResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsRetrieveResponse,
            await self._client.request(
                "GET",
                f"/api/models/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}/{_path_parameter(model, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("analysis", analysis, style="form", explode=True)],
            ),
        )

    async def update(
        self,
        owner: str,
        project: str,
        model: str,
        *,
        starred: bool | NotGiven = NOT_GIVEN,
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

        Updates model properties such as name, description, metadata, or training status.

        Args:
            owner (str): Project owner
            project (str): Project name
            model (str): Model name
            starred (bool, optional): starred request value.
            name (str, optional): name request value.
            color (str | None, optional): color request value.
            description (str, optional): description request value.
            metadata (dict[str, Any], optional): Custom JSON metadata with keys limited to 128 characters and at most 500,000 serialized characters.
            status (Literal["pending", "untrained", "starting", "running", "completed", "failed", "cancelled"], optional): Training/model status
            license (Literal["None", "Apache-2.0", "MIT", "BSD-3-Clause", "AGPL-3.0", "GPL-3.0", "LGPL-3.0", "MPL-2.0", "EUPL-1.1", "Unlicense", "CC0-1.0", "Ultralytics-Enterprise", "Other"], optional): Project/model license identifier
            dataset_slug (str | None, optional): datasetSlug request value.
            train_args (dict[str, Any], optional): Custom JSON metadata with keys limited to 128 characters and at most 500,000 serialized characters.
            train_results (list[dict[str, Any]], optional): trainResults request value.
            epochs (float, optional): epochs request value.
            best_epoch (float, optional): bestEpoch request value.
            best_fitness (float, optional): bestFitness request value.
            version (str, optional): version request value.
            training_error (dict[str, Any], optional): trainingError request value.

        Returns:
            (ModelsUpdateResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsUpdateResponse,
            await self._client.request(
                "PATCH",
                f"/api/models/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}/{_path_parameter(model, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
                json={
                    "starred": starred,
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

    async def delete(self, owner: str, project: str, model: str) -> ModelsDeleteResponse:
        """Delete a model.

        Moves the model to trash for 30 days.

        Args:
            owner (str): Project owner
            project (str): Project name
            model (str): Model name

        Returns:
            (ModelsDeleteResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsDeleteResponse,
            await self._client.request(
                "DELETE",
                f"/api/models/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}/{_path_parameter(model, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
            ),
        )

    async def retrieve_files(self, owner: str, project: str, model: str) -> ModelsRetrieveFilesResponse:
        """Download model files.

        Returns a short-lived download URL for model weights.

        Args:
            owner (str): Project owner
            project (str): Project name
            model (str): Model name

        Returns:
            (ModelsRetrieveFilesResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsRetrieveFilesResponse,
            await self._client.request(
                "GET",
                f"/api/models/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}/{_path_parameter(model, explode=False, allow_reserved=False)}/files",
                auth=("Authorization", "Bearer "),
            ),
        )

    async def predict(self, owner: str, project: str, model: str, *, body: dict[str, Any]) -> ModelsPredictResponse:
        """Run model inference.

        Runs inference on an image or video using a trained model.

        Args:
            owner (str): Project owner
            project (str): Project name
            model (str): Model name
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
                f"/api/models/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}/{_path_parameter(model, explode=False, allow_reserved=False)}/predict",
                auth=("Authorization", "Bearer "),
                data={key: value for key, value in body.items() if key not in ["file"]},
                files={key: body[key] for key in ["file"] if key in body},
            ),
        )

    async def retrieve_training(self, owner: str, project: str, model: str) -> ModelsRetrieveTrainingResponse:
        """Check training progress.

        Returns live status, epoch progress, timing, compute, metrics, and safe error details.

        Args:
            owner (str): Project owner
            project (str): Project name
            model (str): Model name

        Returns:
            (ModelsRetrieveTrainingResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsRetrieveTrainingResponse,
            await self._client.request(
                "GET",
                f"/api/models/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}/{_path_parameter(model, explode=False, allow_reserved=False)}/training",
                auth=("Authorization", "Bearer "),
            ),
        )

    async def delete_training(self, owner: str, project: str, model: str) -> ModelsDeleteTrainingResponse:
        """Cancel training.

        Terminates active compute and marks the model as cancelled.

        Args:
            owner (str): Project owner
            project (str): Project name
            model (str): Model name

        Returns:
            (ModelsDeleteTrainingResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsDeleteTrainingResponse,
            await self._client.request(
                "DELETE",
                f"/api/models/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}/{_path_parameter(model, explode=False, allow_reserved=False)}/training",
                auth=("Authorization", "Bearer "),
            ),
        )

    async def list(self, owner: str, project: str, *, limit: int | None = None) -> ModelsListResponse:
        """List models in a project.

        Returns models by owner and project name.

        Args:
            owner (str): Project owner
            project (str): Project name
            limit (int, optional): Maximum models to return

        Returns:
            (ModelsListResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsListResponse,
            await self._client.request(
                "GET",
                f"/api/models/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}",
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("limit", limit, style="form", explode=True)],
            ),
        )

    async def create(self, *, body: dict[str, Any]) -> ModelsCreateResponse:
        """Create a model.

        Creates a model in an existing project.

        Args:
            body (dict[str, Any]): API request for creating a new model

        Returns:
            (ModelsCreateResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsCreateResponse,
            await self._client.request("POST", "/api/models", auth=("Authorization", "Bearer "), json=body),
        )
