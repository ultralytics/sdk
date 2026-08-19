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
    _form_data,
    _path_parameter,
    _query_parameter,
)
from ..types import (
    ModelsCloneResponse,
    ModelsCreateResponse,
    ModelsDeleteResponse,
    ModelsDeleteTrainingResponse,
    ModelsFilesResponse,
    ModelsListResponse,
    ModelsPredictResponse,
    ModelsRetrieveResponse,
    ModelsTrainingResponse,
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
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
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
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

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
                timeout=timeout,
                extra_headers=extra_headers,
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
        self,
        owner: str,
        project: str,
        model: str,
        *,
        analysis: Literal["1"] | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ModelsRetrieveResponse:
        """Get model details.

        Returns model details. Pass analysis=1 to return per-image validation analysis instead.

        Args:
            owner (str): Project owner
            project (str): Project name
            model (str): Model name
            analysis (Literal["1"], optional): Return per-image validation analysis instead of model details
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

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
                timeout=timeout,
                extra_headers=extra_headers,
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
        train_results: Sequence[dict[str, Any]] | NotGiven = NOT_GIVEN,
        epochs: float | NotGiven = NOT_GIVEN,
        best_epoch: float | NotGiven = NOT_GIVEN,
        best_fitness: float | NotGiven = NOT_GIVEN,
        version: str | NotGiven = NOT_GIVEN,
        training_error: dict[str, Any] | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
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
            train_results (Sequence[dict[str, Any]], optional): trainResults request value.
            epochs (float, optional): epochs request value.
            best_epoch (float, optional): bestEpoch request value.
            best_fitness (float, optional): bestFitness request value.
            version (str, optional): version request value.
            training_error (dict[str, Any], optional): trainingError request value.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

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
                timeout=timeout,
                extra_headers=extra_headers,
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

    def delete(
        self,
        owner: str,
        project: str,
        model: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ModelsDeleteResponse:
        """Delete a model.

        Moves the model to trash for 30 days.

        Args:
            owner (str): Project owner
            project (str): Project name
            model (str): Model name
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

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
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    def files(
        self,
        owner: str,
        project: str,
        model: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ModelsFilesResponse:
        """Download model files.

        Returns a short-lived download URL for model weights.

        Args:
            owner (str): Project owner
            project (str): Project name
            model (str): Model name
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (ModelsFilesResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsFilesResponse,
            self._client.request(
                "GET",
                f"/api/models/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}/{_path_parameter(model, explode=False, allow_reserved=False)}/files",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    def predict(
        self,
        owner: str,
        project: str,
        model: str,
        *,
        body: dict[str, Any],
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ModelsPredictResponse:
        """Run model inference.

        Runs inference on an image or video using a trained model. Depth models accept images only.

        Args:
            owner (str): Project owner
            project (str): Project name
            model (str): Model name
            body (dict[str, Any]): Request body.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

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
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                data=_form_data({key: value for key, value in body.items() if key not in ["file"]}, multipart=True),
                files={key: body[key] for key in ["file"] if key in body},
            ),
        )

    def training(
        self,
        owner: str,
        project: str,
        model: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ModelsTrainingResponse:
        """Check training progress.

        Returns live status, epoch progress, timing, compute, metrics, and safe error details.

        Args:
            owner (str): Project owner
            project (str): Project name
            model (str): Model name
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (ModelsTrainingResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsTrainingResponse,
            self._client.request(
                "GET",
                f"/api/models/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}/{_path_parameter(model, explode=False, allow_reserved=False)}/training",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    def delete_training(
        self,
        owner: str,
        project: str,
        model: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ModelsDeleteTrainingResponse:
        """Cancel training.

        Terminates active compute and marks the model as cancelled.

        Args:
            owner (str): Project owner
            project (str): Project name
            model (str): Model name
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

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
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    def list(
        self,
        owner: str,
        project: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ModelsListResponse:
        """List models in a project.

        Returns models by owner and project name.

        Args:
            owner (str): Project owner
            project (str): Project name
            limit (int, optional): Maximum models to return
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

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
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("limit", limit, style="form", explode=True)],
            ),
        )

    def create(
        self,
        *,
        body: dict[str, Any],
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ModelsCreateResponse:
        """Create a model.

        Creates a model in an existing project.

        Args:
            body (dict[str, Any]): API request for creating a new model
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

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
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json=body,
            ),
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
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
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
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

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
                timeout=timeout,
                extra_headers=extra_headers,
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
        self,
        owner: str,
        project: str,
        model: str,
        *,
        analysis: Literal["1"] | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ModelsRetrieveResponse:
        """Get model details.

        Returns model details. Pass analysis=1 to return per-image validation analysis instead.

        Args:
            owner (str): Project owner
            project (str): Project name
            model (str): Model name
            analysis (Literal["1"], optional): Return per-image validation analysis instead of model details
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

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
                timeout=timeout,
                extra_headers=extra_headers,
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
        train_results: Sequence[dict[str, Any]] | NotGiven = NOT_GIVEN,
        epochs: float | NotGiven = NOT_GIVEN,
        best_epoch: float | NotGiven = NOT_GIVEN,
        best_fitness: float | NotGiven = NOT_GIVEN,
        version: str | NotGiven = NOT_GIVEN,
        training_error: dict[str, Any] | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
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
            train_results (Sequence[dict[str, Any]], optional): trainResults request value.
            epochs (float, optional): epochs request value.
            best_epoch (float, optional): bestEpoch request value.
            best_fitness (float, optional): bestFitness request value.
            version (str, optional): version request value.
            training_error (dict[str, Any], optional): trainingError request value.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

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
                timeout=timeout,
                extra_headers=extra_headers,
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

    async def delete(
        self,
        owner: str,
        project: str,
        model: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ModelsDeleteResponse:
        """Delete a model.

        Moves the model to trash for 30 days.

        Args:
            owner (str): Project owner
            project (str): Project name
            model (str): Model name
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

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
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    async def files(
        self,
        owner: str,
        project: str,
        model: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ModelsFilesResponse:
        """Download model files.

        Returns a short-lived download URL for model weights.

        Args:
            owner (str): Project owner
            project (str): Project name
            model (str): Model name
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (ModelsFilesResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsFilesResponse,
            await self._client.request(
                "GET",
                f"/api/models/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}/{_path_parameter(model, explode=False, allow_reserved=False)}/files",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    async def predict(
        self,
        owner: str,
        project: str,
        model: str,
        *,
        body: dict[str, Any],
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ModelsPredictResponse:
        """Run model inference.

        Runs inference on an image or video using a trained model. Depth models accept images only.

        Args:
            owner (str): Project owner
            project (str): Project name
            model (str): Model name
            body (dict[str, Any]): Request body.
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

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
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                data=_form_data({key: value for key, value in body.items() if key not in ["file"]}, multipart=True),
                files={key: body[key] for key in ["file"] if key in body},
            ),
        )

    async def training(
        self,
        owner: str,
        project: str,
        model: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ModelsTrainingResponse:
        """Check training progress.

        Returns live status, epoch progress, timing, compute, metrics, and safe error details.

        Args:
            owner (str): Project owner
            project (str): Project name
            model (str): Model name
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

        Returns:
            (ModelsTrainingResponse): The API response.

        Raises:
            (APIError): If the API returns an unsuccessful response.
        """
        return cast(
            ModelsTrainingResponse,
            await self._client.request(
                "GET",
                f"/api/models/{_path_parameter(owner, explode=False, allow_reserved=False)}/{_path_parameter(project, explode=False, allow_reserved=False)}/{_path_parameter(model, explode=False, allow_reserved=False)}/training",
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    async def delete_training(
        self,
        owner: str,
        project: str,
        model: str,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ModelsDeleteTrainingResponse:
        """Cancel training.

        Terminates active compute and marks the model as cancelled.

        Args:
            owner (str): Project owner
            project (str): Project name
            model (str): Model name
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

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
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
            ),
        )

    async def list(
        self,
        owner: str,
        project: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ModelsListResponse:
        """List models in a project.

        Returns models by owner and project name.

        Args:
            owner (str): Project owner
            project (str): Project name
            limit (int, optional): Maximum models to return
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

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
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                params=[*_query_parameter("limit", limit, style="form", explode=True)],
            ),
        )

    async def create(
        self,
        *,
        body: dict[str, Any],
        timeout: float | httpx.Timeout | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> ModelsCreateResponse:
        """Create a model.

        Creates a model in an existing project.

        Args:
            body (dict[str, Any]): API request for creating a new model
            timeout (float | httpx.Timeout, optional): Request timeout override.
            extra_headers (dict[str, str], optional): Additional request headers.

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
                timeout=timeout,
                extra_headers=extra_headers,
                auth=("Authorization", "Bearer "),
                json=body,
            ),
        )
