# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from __future__ import annotations

from typing import Any, Literal, NotRequired, TypedDict

AccountSummaryResponseCounts = TypedDict(
    "AccountSummaryResponseCounts", {"projects": int, "datasets": int, "models": int}
)


AccountSummaryResponseTeamsItem = TypedDict(
    "AccountSummaryResponseTeamsItem",
    {
        "userId": str,
        "username": str,
        "fullName": NotRequired[str],
        "imageUrl": NotRequired[str],
        "iconColor": NotRequired[str],
        "iconLetter": NotRequired[str],
        "plan": str,
        "region": Literal["us", "eu", "ap"],
        "role": Literal["viewer", "editor", "admin", "owner"],
        "deniedReason": NotRequired[str],
    },
)


AccountSummaryResponse = TypedDict(
    "AccountSummaryResponse",
    {
        "username": str,
        "name": str,
        "accountType": Literal["personal", "team"],
        "plan": Literal["free", "pro", "enterprise"],
        "creditsCents": int,
        "counts": AccountSummaryResponseCounts,
        "teams": list[AccountSummaryResponseTeamsItem],
    },
)


AccountApiKeysResponseKeysItem = TypedDict(
    "AccountApiKeysResponseKeysItem", {"keyId": str, "name": str, "keyPrefix": str, "createdAt": str}
)


AccountApiKeysResponse = TypedDict("AccountApiKeysResponse", {"keys": list[AccountApiKeysResponseKeysItem]})


AccountStorageResponseUsageProjects = TypedDict(
    "AccountStorageResponseUsageProjects", {"current": float, "limit": float, "percent": float}
)


AccountStorageResponseUsageDatasets = TypedDict(
    "AccountStorageResponseUsageDatasets", {"current": float, "limit": float, "percent": float}
)


AccountStorageResponseUsageModels = TypedDict(
    "AccountStorageResponseUsageModels", {"current": float, "limit": float, "percent": float}
)


AccountStorageResponseUsageImages = TypedDict(
    "AccountStorageResponseUsageImages", {"current": float, "limit": float, "percent": float}
)


AccountStorageResponseUsageAnnotations = TypedDict("AccountStorageResponseUsageAnnotations", {"current": float})


AccountStorageResponseUsageDeployments = TypedDict(
    "AccountStorageResponseUsageDeployments", {"current": float, "limit": float, "percent": float}
)


AccountStorageResponseUsageStorage = TypedDict(
    "AccountStorageResponseUsageStorage", {"current": float, "limit": float, "percent": float}
)


AccountStorageResponseUsage = TypedDict(
    "AccountStorageResponseUsage",
    {
        "projects": NotRequired[AccountStorageResponseUsageProjects],
        "datasets": NotRequired[AccountStorageResponseUsageDatasets],
        "models": NotRequired[AccountStorageResponseUsageModels],
        "images": NotRequired[AccountStorageResponseUsageImages],
        "annotations": NotRequired[AccountStorageResponseUsageAnnotations],
        "deployments": NotRequired[AccountStorageResponseUsageDeployments],
        "storage": AccountStorageResponseUsageStorage,
    },
)


AccountStorageResponseBreakdownByCategoryDatasets = TypedDict(
    "AccountStorageResponseBreakdownByCategoryDatasets", {"bytes": float, "count": float}
)


AccountStorageResponseBreakdownByCategoryModels = TypedDict(
    "AccountStorageResponseBreakdownByCategoryModels", {"bytes": float, "count": float}
)


AccountStorageResponseBreakdownByCategoryExports = TypedDict(
    "AccountStorageResponseBreakdownByCategoryExports", {"bytes": float, "count": float}
)


AccountStorageResponseBreakdownByCategory = TypedDict(
    "AccountStorageResponseBreakdownByCategory",
    {
        "datasets": AccountStorageResponseBreakdownByCategoryDatasets,
        "models": AccountStorageResponseBreakdownByCategoryModels,
        "exports": AccountStorageResponseBreakdownByCategoryExports,
    },
)


AccountStorageResponseBreakdownTopItemsItem = TypedDict(
    "AccountStorageResponseBreakdownTopItemsItem",
    {
        "_id": str,
        "name": str,
        "slug": NotRequired[str],
        "sizeBytes": float,
        "type": Literal["project", "dataset", "model", "export"],
        "parentName": NotRequired[str],
        "parentSlug": NotRequired[str],
    },
)


AccountStorageResponseBreakdown = TypedDict(
    "AccountStorageResponseBreakdown",
    {
        "byCategory": AccountStorageResponseBreakdownByCategory,
        "topItems": list[AccountStorageResponseBreakdownTopItemsItem],
    },
)


AccountStorageResponse = TypedDict(
    "AccountStorageResponse",
    {
        "tier": Literal["free", "pro", "enterprise"],
        "usage": AccountStorageResponseUsage,
        "updatedAt": str | None,
        "breakdown": AccountStorageResponseBreakdown,
        "region": Literal["us", "eu", "ap"],
        "username": str,
    },
)


AccountProfileResponseUserSocials = TypedDict(
    "AccountProfileResponseUserSocials",
    {
        "github": NotRequired[str],
        "linkedin": NotRequired[str],
        "twitter": NotRequired[str],
        "discord": NotRequired[str],
        "youtube": NotRequired[str],
        "scholar": NotRequired[str],
        "website": NotRequired[str],
    },
)


AccountProfileResponseUser = TypedDict(
    "AccountProfileResponseUser",
    {
        "username": str,
        "fullName": NotRequired[str],
        "imageUrl": NotRequired[str],
        "accountType": Literal["personal", "team"],
        "iconColor": NotRequired[str],
        "iconLetter": NotRequired[str],
        "bio": NotRequired[str],
        "company": NotRequired[str],
        "useCase": NotRequired[str],
        "socials": NotRequired[AccountProfileResponseUserSocials],
        "followerCount": int,
        "isFollowed": bool,
    },
)


AccountProfileResponse = TypedDict("AccountProfileResponse", {"user": AccountProfileResponseUser})


AccountFollowResponse = TypedDict("AccountFollowResponse", {"followed": bool, "followerCount": int})


BillingTransactionsResponseTransactionsItemModel = TypedDict(
    "BillingTransactionsResponseTransactionsItemModel",
    {
        "name": str,
        "slug": str,
        "projectSlug": str,
        "username": str,
        "datasetId": NotRequired[str],
        "gpuType": NotRequired[str],
        "gpuDisplayName": NotRequired[str],
        "startedAt": NotRequired[str],
    },
)


BillingTransactionsResponseTransactionsItem = TypedDict(
    "BillingTransactionsResponseTransactionsItem",
    {
        "id": str,
        "type": Literal[
            "signup",
            "purchase",
            "subscription",
            "monthly_grant",
            "training",
            "annotation",
            "refund",
            "adjustment",
            "promo",
            "auto_topup",
            "auto_topup_failed",
            "pro_credit_expiry",
        ],
        "amountCents": float,
        "balanceAfter": float,
        "modelId": NotRequired[str],
        "datasetId": NotRequired[str],
        "apiKeyId": NotRequired[str],
        "runId": NotRequired[str],
        "gpuType": NotRequired[str],
        "gpuDisplayName": NotRequired[str],
        "period": NotRequired[str],
        "createdAt": str,
        "receiptUrl": NotRequired[str | None],
        "model": NotRequired[BillingTransactionsResponseTransactionsItemModel | None],
    },
)


BillingTransactionsResponse = TypedDict(
    "BillingTransactionsResponse", {"transactions": list[BillingTransactionsResponseTransactionsItem]}
)


BillingUsageSummaryResponsePlan = TypedDict(
    "BillingUsageSummaryResponsePlan",
    {
        "planId": Literal["free", "pro", "enterprise"],
        "name": str,
        "status": Literal["active", "past_due"],
        "cancelAtPeriodEnd": bool,
        "paymentFailedAt": NotRequired[str],
        "billingCycle": NotRequired[Literal["monthly", "yearly"]],
        "currentPeriodEnd": NotRequired[str],
        "enterpriseLicenseEnd": NotRequired[str],
        "licenseExpired": NotRequired[bool],
    },
)


BillingUsageSummaryResponseMetricsItem = TypedDict(
    "BillingUsageSummaryResponseMetricsItem",
    {
        "metricId": Literal["storage_bytes"],
        "kind": Literal["GAUGE"],
        "period": Literal["NONE"],
        "limit": float,
        "used": float,
        "remaining": float,
        "overageAllowed": bool,
    },
)


BillingUsageSummaryResponseTrainingCredit = TypedDict(
    "BillingUsageSummaryResponseTrainingCredit", {"monthlyGrant": float, "balanceAvailable": float}
)


BillingUsageSummaryResponseFeatures = TypedDict(
    "BillingUsageSummaryResponseFeatures", {"privateProjects": bool, "teams": bool, "enterpriseLicense": bool}
)


BillingUsageSummaryResponse = TypedDict(
    "BillingUsageSummaryResponse",
    {
        "plan": BillingUsageSummaryResponsePlan,
        "metrics": list[BillingUsageSummaryResponseMetricsItem],
        "trainingCredit": BillingUsageSummaryResponseTrainingCredit,
        "features": BillingUsageSummaryResponseFeatures,
        "creditsCents": float,
        "paidSeats": NotRequired[float],
        "currentSeats": NotRequired[float],
        "maxSeats": NotRequired[float],
        "nextInvoiceCents": NotRequired[float],
    },
)


DatasetsClassStatsResponseClassesItem = TypedDict(
    "DatasetsClassStatsResponseClassesItem", {"classId": float, "count": float, "imageCount": float}
)


DatasetsClassStatsResponseImageStatsWidthHistogramItem = TypedDict(
    "DatasetsClassStatsResponseImageStatsWidthHistogramItem", {"bin": float, "count": float, "size": NotRequired[float]}
)


DatasetsClassStatsResponseImageStatsHeightHistogramItem = TypedDict(
    "DatasetsClassStatsResponseImageStatsHeightHistogramItem",
    {"bin": float, "count": float, "size": NotRequired[float]},
)


DatasetsClassStatsResponseImageStatsPointsHistogramItem = TypedDict(
    "DatasetsClassStatsResponseImageStatsPointsHistogramItem",
    {"bin": float, "count": float, "size": NotRequired[float]},
)


DatasetsClassStatsResponseImageStatsFileSizeHistogramItem = TypedDict(
    "DatasetsClassStatsResponseImageStatsFileSizeHistogramItem",
    {"bin": float, "count": float, "size": NotRequired[float]},
)


DatasetsClassStatsResponseImageStatsObjectsPerImageHistogramItem = TypedDict(
    "DatasetsClassStatsResponseImageStatsObjectsPerImageHistogramItem",
    {"bin": float, "count": float, "size": NotRequired[float]},
)


DatasetsClassStatsResponseImageStatsBboxWidthHistogramItem = TypedDict(
    "DatasetsClassStatsResponseImageStatsBboxWidthHistogramItem",
    {"bin": float, "count": float, "size": NotRequired[float]},
)


DatasetsClassStatsResponseImageStatsBboxHeightHistogramItem = TypedDict(
    "DatasetsClassStatsResponseImageStatsBboxHeightHistogramItem",
    {"bin": float, "count": float, "size": NotRequired[float]},
)


DatasetsClassStatsResponseImageStatsBboxWidthNormHistogramItem = TypedDict(
    "DatasetsClassStatsResponseImageStatsBboxWidthNormHistogramItem",
    {"bin": float, "count": float, "size": NotRequired[float]},
)


DatasetsClassStatsResponseImageStatsBboxHeightNormHistogramItem = TypedDict(
    "DatasetsClassStatsResponseImageStatsBboxHeightNormHistogramItem",
    {"bin": float, "count": float, "size": NotRequired[float]},
)


DatasetsClassStatsResponseImageStats = TypedDict(
    "DatasetsClassStatsResponseImageStats",
    {
        "widthHistogram": list[DatasetsClassStatsResponseImageStatsWidthHistogramItem],
        "heightHistogram": list[DatasetsClassStatsResponseImageStatsHeightHistogramItem],
        "pointsHistogram": list[DatasetsClassStatsResponseImageStatsPointsHistogramItem],
        "formatDistribution": dict[str, float],
        "fileSizeHistogram": list[DatasetsClassStatsResponseImageStatsFileSizeHistogramItem],
        "objectsPerImageHistogram": list[DatasetsClassStatsResponseImageStatsObjectsPerImageHistogramItem],
        "bboxWidthHistogram": list[DatasetsClassStatsResponseImageStatsBboxWidthHistogramItem],
        "bboxHeightHistogram": list[DatasetsClassStatsResponseImageStatsBboxHeightHistogramItem],
        "bboxWidthNormHistogram": list[DatasetsClassStatsResponseImageStatsBboxWidthNormHistogramItem],
        "bboxHeightNormHistogram": list[DatasetsClassStatsResponseImageStatsBboxHeightNormHistogramItem],
    },
)


DatasetsClassStatsResponseLocationHeatmap = TypedDict(
    "DatasetsClassStatsResponseLocationHeatmap", {"bins": list[list[float]], "maxCount": float}
)


DatasetsClassStatsResponseDimensionHeatmap = TypedDict(
    "DatasetsClassStatsResponseDimensionHeatmap",
    {
        "bins": list[list[float]],
        "maxCount": float,
        "minWidth": float,
        "maxWidth": float,
        "minHeight": float,
        "maxHeight": float,
    },
)


DatasetsClassStatsResponse = TypedDict(
    "DatasetsClassStatsResponse",
    {
        "classes": list[DatasetsClassStatsResponseClassesItem],
        "imageStats": DatasetsClassStatsResponseImageStats,
        "locationHeatmap": DatasetsClassStatsResponseLocationHeatmap,
        "dimensionHeatmap": DatasetsClassStatsResponseDimensionHeatmap,
        "classNames": list[str],
        "cached": bool,
        "sampleSize": NotRequired[float | None],
    },
)


DatasetsDeleteClassesResponse = TypedDict(
    "DatasetsDeleteClassesResponse",
    {
        "success": Literal[True],
        "classNames": list[str],
        "classColors": dict[str, str],
        "deletedClassIds": list[int],
        "deletedAnnotations": int,
    },
)


DatasetsMergeClassesResponse = TypedDict(
    "DatasetsMergeClassesResponse",
    {
        "success": Literal[True],
        "classNames": list[str],
        "classColors": dict[str, str],
        "mergedClassIds": list[int],
        "targetClassId": int,
    },
)


DatasetsCloneResponse = TypedDict(
    "DatasetsCloneResponse",
    {
        "id": str,
        "owner": str,
        "dataset": str,
        "name": str,
        "imageCount": int,
        "classCount": NotRequired[int],
        "region": Literal["us", "eu", "ap"],
    },
)


DatasetsRetrieveResponseDatasetSplits = TypedDict(
    "DatasetsRetrieveResponseDatasetSplits", {"train": int, "val": int, "test": int, "labeled": int}
)


DatasetsRetrieveResponseDatasetSampleImagesItemLabelsItem = TypedDict(
    "DatasetsRetrieveResponseDatasetSampleImagesItemLabelsItem",
    {
        "classId": int,
        "bbox": NotRequired[list[Any]],
        "segments": NotRequired[list[float]],
        "keypoints": NotRequired[list[float]],
        "obb": NotRequired[list[Any]],
        "skeletonId": NotRequired[str],
    },
)


DatasetsRetrieveResponseDatasetSampleImagesItem = TypedDict(
    "DatasetsRetrieveResponseDatasetSampleImagesItem",
    {
        "url": str,
        "imageUrl": NotRequired[str],
        "depthPreviewUrl": NotRequired[str],
        "width": int,
        "height": int,
        "labels": NotRequired[list[DatasetsRetrieveResponseDatasetSampleImagesItemLabelsItem]],
    },
)


DatasetsRetrieveResponseDatasetSourceVariant1 = TypedDict(
    "DatasetsRetrieveResponseDatasetSourceVariant1", {"provider": Literal["cloud"]}
)


DatasetsRetrieveResponseDatasetSourceVariant2 = TypedDict(
    "DatasetsRetrieveResponseDatasetSourceVariant2", {"provider": Literal["roboflow"]}
)


DatasetsRetrieveResponseDatasetSourceVariant3 = TypedDict(
    "DatasetsRetrieveResponseDatasetSourceVariant3", {"provider": Literal["local"], "keyId": NotRequired[str]}
)


DatasetsRetrieveResponseDatasetProcessingError = TypedDict(
    "DatasetsRetrieveResponseDatasetProcessingError", {"message": str, "timestamp": str}
)


DatasetsRetrieveResponseDatasetLastIngestSummary = TypedDict(
    "DatasetsRetrieveResponseDatasetLastIngestSummary",
    {"added": int, "paired": NotRequired[int], "errors": int, "skippedCounts": dict[str, int]},
)


DatasetsRetrieveResponseDatasetVersionsItemSplits = TypedDict(
    "DatasetsRetrieveResponseDatasetVersionsItemSplits", {"train": int, "val": int, "test": int, "labeled": int}
)


DatasetsRetrieveResponseDatasetVersionsItem = TypedDict(
    "DatasetsRetrieveResponseDatasetVersionsItem",
    {
        "version": int,
        "description": NotRequired[str],
        "sizeBytes": NotRequired[float],
        "contentHash": NotRequired[str],
        "sourceUpdatedAt": NotRequired[str],
        "imageCount": int,
        "classCount": int,
        "annotationCount": int,
        "splits": DatasetsRetrieveResponseDatasetVersionsItemSplits,
        "createdAt": str,
    },
)


DatasetsRetrieveResponseDataset = TypedDict(
    "DatasetsRetrieveResponseDataset",
    {
        "id": str,
        "owner": str,
        "dataset": str,
        "name": str,
        "description": NotRequired[str],
        "visibility": Literal["public", "private"],
        "task": Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"],
        "channels": NotRequired[int],
        "depthScale": NotRequired[float],
        "imageCount": int,
        "classCount": NotRequired[int],
        "classNames": NotRequired[list[str]],
        "format": NotRequired[Literal["yolo", "coco", "raw", "ndjson"]],
        "tags": NotRequired[list[str]],
        "license": NotRequired[
            Literal[
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
        ],
        "splits": DatasetsRetrieveResponseDatasetSplits,
        "annotationCount": NotRequired[int],
        "totalBytes": NotRequired[float],
        "starCount": int,
        "isStarred": bool,
        "status": NotRequired[Literal["processing", "ready", "failed"]],
        "sampleImages": NotRequired[list[DatasetsRetrieveResponseDatasetSampleImagesItem]],
        "integrationProvider": NotRequired[Literal["gcs", "s3", "azure", "on-premise"]],
        "integrationStatus": NotRequired[Literal["online", "offline", "disconnected"]],
        "source": NotRequired[
            DatasetsRetrieveResponseDatasetSourceVariant1
            | DatasetsRetrieveResponseDatasetSourceVariant2
            | DatasetsRetrieveResponseDatasetSourceVariant3
        ],
        "classColors": NotRequired[dict[str, str]],
        "kptShape": NotRequired[list[Any]],
        "flipIdx": NotRequired[list[int]],
        "processingTimeMs": NotRequired[float],
        "lastIngestJobId": NotRequired[str],
        "processingError": NotRequired[DatasetsRetrieveResponseDatasetProcessingError],
        "lastIngestSummary": NotRequired[DatasetsRetrieveResponseDatasetLastIngestSummary],
        "errorCount": NotRequired[int],
        "iconColor": NotRequired[str],
        "iconLetter": NotRequired[str],
        "iconImage": NotRequired[str],
        "clonedFrom": NotRequired[str],
        "cloneCount": NotRequired[int],
        "region": NotRequired[Literal["us", "eu", "ap"]],
        "versions": NotRequired[list[DatasetsRetrieveResponseDatasetVersionsItem]],
        "createdAt": str,
        "updatedAt": str,
        "metadata": dict[str, Any],
    },
)


DatasetsRetrieveResponse = TypedDict("DatasetsRetrieveResponse", {"dataset": DatasetsRetrieveResponseDataset})


DatasetsUpdateResponse = TypedDict("DatasetsUpdateResponse", {"success": Literal[True], "dataset": str})


DatasetsDeleteResponse = TypedDict("DatasetsDeleteResponse", {"success": Literal[True]})


DatasetsEmbeddingsResponseActiveJobProgress = TypedDict(
    "DatasetsEmbeddingsResponseActiveJobProgress",
    {
        "stage": Literal["embedding", "umap"],
        "percent": float,
        "processed": NotRequired[float],
        "total": NotRequired[float],
        "failedDownloads": NotRequired[float],
        "failedInference": NotRequired[float],
    },
)


DatasetsEmbeddingsResponseActiveJob = TypedDict(
    "DatasetsEmbeddingsResponseActiveJob",
    {
        "id": str,
        "status": Literal["queued", "starting", "running"],
        "progress": DatasetsEmbeddingsResponseActiveJobProgress | None,
        "createdAt": str,
    },
)


DatasetsEmbeddingsResponse = TypedDict(
    "DatasetsEmbeddingsResponse",
    {
        "analyzedAt": str | None,
        "embeddingsCount": int,
        "latestImageAt": str | None,
        "activeJob": DatasetsEmbeddingsResponseActiveJob | None,
    },
)


DatasetsCreateEmbeddingsResponse = TypedDict("DatasetsCreateEmbeddingsResponse", {"jobId": str})


DatasetsDeleteEmbeddingsResponse = TypedDict("DatasetsDeleteEmbeddingsResponse", {"cancelled": str | None})


DatasetsExportResponseVariant1 = TypedDict("DatasetsExportResponseVariant1", {"downloadUrl": str, "version": int})


DatasetsExportResponseVariant2 = TypedDict("DatasetsExportResponseVariant2", {"downloadUrl": str, "cached": bool})


DatasetsExportResponse = DatasetsExportResponseVariant1 | DatasetsExportResponseVariant2


DatasetsCreateExportResponse = TypedDict(
    "DatasetsCreateExportResponse", {"version": int, "downloadUrl": str, "reused": bool}
)


DatasetsUpdateExportResponse = TypedDict("DatasetsUpdateExportResponse", {"ok": Literal[True]})


DatasetsClusteringResponseImagesItem = TypedDict(
    "DatasetsClusteringResponseImagesItem",
    {
        "id": str,
        "umapX": float,
        "umapY": float,
        "split": Literal["train", "val", "test"] | None,
        "classIds": list[int],
        "width": int,
        "height": int,
        "bytes": int | None,
        "labelCount": int,
        "labeled": bool,
        "missing": bool,
    },
)


DatasetsClusteringResponse = TypedDict(
    "DatasetsClusteringResponse",
    {
        "images": list[DatasetsClusteringResponseImagesItem],
        "total": int,
        "offset": int,
        "limit": int,
        "hasMore": bool,
        "nextOffset": int | None,
        "updatedAt": str,
    },
)


DatasetsImagesResponseImagesItemLabelsItem = TypedDict(
    "DatasetsImagesResponseImagesItemLabelsItem",
    {
        "classId": int,
        "bbox": NotRequired[list[Any]],
        "segments": NotRequired[list[float]],
        "keypoints": NotRequired[list[float]],
        "obb": NotRequired[list[Any]],
        "skeletonId": NotRequired[str],
    },
)


DatasetsImagesResponseImagesItemDepth = TypedDict(
    "DatasetsImagesResponseImagesItemDepth",
    {
        "hash": str,
        "bytes": int,
        "shape": list[int],
        "min": NotRequired[float],
        "max": NotRequired[float],
        "validFraction": NotRequired[float],
        "previewUrl": str,
    },
)


DatasetsImagesResponseImagesItem = TypedDict(
    "DatasetsImagesResponseImagesItem",
    {
        "id": str,
        "hash": str,
        "ext": str,
        "thumbnailUrl": NotRequired[str],
        "imageUrl": NotRequired[str],
        "width": int,
        "height": int,
        "split": Literal["train", "val", "test"],
        "labelCount": int,
        "name": str,
        "bytes": NotRequired[int],
        "error": NotRequired[str | None],
        "labels": NotRequired[list[DatasetsImagesResponseImagesItemLabelsItem]],
        "labelsTruncated": NotRequired[Literal[True]],
        "depth": NotRequired[DatasetsImagesResponseImagesItemDepth],
    },
)


DatasetsImagesResponse = TypedDict(
    "DatasetsImagesResponse",
    {
        "images": list[DatasetsImagesResponseImagesItem],
        "total": NotRequired[int],
        "hasMore": bool,
        "classes": list[str],
        "errorCount": int,
        "nextCursor": NotRequired[str],
    },
)


DatasetsSelectedImagesResponseImagesItemLabelsItem = TypedDict(
    "DatasetsSelectedImagesResponseImagesItemLabelsItem",
    {
        "classId": int,
        "bbox": NotRequired[list[Any]],
        "segments": NotRequired[list[float]],
        "keypoints": NotRequired[list[float]],
        "obb": NotRequired[list[Any]],
        "skeletonId": NotRequired[str],
    },
)


DatasetsSelectedImagesResponseImagesItemDepth = TypedDict(
    "DatasetsSelectedImagesResponseImagesItemDepth",
    {
        "hash": str,
        "bytes": int,
        "shape": list[int],
        "min": NotRequired[float],
        "max": NotRequired[float],
        "validFraction": NotRequired[float],
        "previewUrl": str,
    },
)


DatasetsSelectedImagesResponseImagesItem = TypedDict(
    "DatasetsSelectedImagesResponseImagesItem",
    {
        "id": str,
        "hash": str,
        "ext": str,
        "thumbnailUrl": NotRequired[str],
        "imageUrl": NotRequired[str],
        "width": int,
        "height": int,
        "split": Literal["train", "val", "test"],
        "labelCount": int,
        "name": str,
        "bytes": NotRequired[int],
        "error": NotRequired[str | None],
        "labels": NotRequired[list[DatasetsSelectedImagesResponseImagesItemLabelsItem]],
        "labelsTruncated": NotRequired[Literal[True]],
        "depth": NotRequired[DatasetsSelectedImagesResponseImagesItemDepth],
    },
)


DatasetsSelectedImagesResponse = TypedDict(
    "DatasetsSelectedImagesResponse",
    {
        "images": list[DatasetsSelectedImagesResponseImagesItem],
        "total": int,
        "hasMore": Literal[False],
        "classes": list[str],
        "errorCount": int,
        "nextCursor": NotRequired[Any],
    },
)


DatasetsIngestResponse = TypedDict("DatasetsIngestResponse", {"jobId": str, "status": Literal["queued"]})


DatasetsModelsResponseModelsItemDatasetVersion = TypedDict(
    "DatasetsModelsResponseModelsItemDatasetVersion", {"version": int, "contentHash": str}
)


DatasetsModelsResponseModelsItem = TypedDict(
    "DatasetsModelsResponseModelsItem",
    {
        "id": str,
        "owner": str,
        "project": str,
        "model": str,
        "name": str,
        "status": Literal["pending", "untrained", "starting", "running", "completed", "failed", "cancelled"],
        "task": NotRequired[Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"]],
        "datasetVersion": NotRequired[DatasetsModelsResponseModelsItemDatasetVersion],
        "epochs": NotRequired[int],
        "bestEpoch": NotRequired[int],
        "bestFitness": NotRequired[float],
        "metrics": dict[str, float],
        "startedAt": NotRequired[str],
        "completedAt": NotRequired[str],
        "createdAt": str,
        "projectIconColor": NotRequired[str],
        "projectIconLetter": NotRequired[str],
        "projectIconImage": NotRequired[str],
    },
)


DatasetsModelsResponse = TypedDict(
    "DatasetsModelsResponse", {"models": list[DatasetsModelsResponseModelsItem], "count": int}
)


DatasetsBatchResponseActiveJobProgress = TypedDict(
    "DatasetsBatchResponseActiveJobProgress", {"processed": float, "total": float}
)


DatasetsBatchResponseActiveJob = TypedDict(
    "DatasetsBatchResponseActiveJob",
    {"id": str, "stopping": bool, "progress": DatasetsBatchResponseActiveJobProgress, "startedAt": str},
)


DatasetsBatchResponseLastRunResults = TypedDict(
    "DatasetsBatchResponseLastRunResults", {"processed": int, "annotations": int, "classes": int}
)


DatasetsBatchResponseLastRun = TypedDict(
    "DatasetsBatchResponseLastRun",
    {"failed": bool, "stopped": bool, "error": str | None, "results": DatasetsBatchResponseLastRunResults | None},
)


DatasetsBatchResponse = TypedDict(
    "DatasetsBatchResponse",
    {"activeJob": DatasetsBatchResponseActiveJob | None, "lastRun": DatasetsBatchResponseLastRun | None},
)


DatasetsCreateBatchResponse = TypedDict("DatasetsCreateBatchResponse", {"jobId": str})


DatasetsDeleteBatchResponse = TypedDict(
    "DatasetsDeleteBatchResponse", {"action": Literal["cancelled", "dismissed", "none"], "jobId": str | None}
)


DatasetsRestoreResponse = TypedDict("DatasetsRestoreResponse", {"version": int, "imageCount": int})


DatasetsRedistributeSplitsResponseSplits = TypedDict(
    "DatasetsRedistributeSplitsResponseSplits", {"train": int, "val": int, "test": int}
)


DatasetsRedistributeSplitsResponse = TypedDict(
    "DatasetsRedistributeSplitsResponse",
    {"success": Literal[True], "splits": DatasetsRedistributeSplitsResponseSplits, "modified": int},
)


DatasetsListResponseDatasetsItemSplits = TypedDict(
    "DatasetsListResponseDatasetsItemSplits", {"train": int, "val": int, "test": int, "labeled": int}
)


DatasetsListResponseDatasetsItemSampleImagesItemLabelsItem = TypedDict(
    "DatasetsListResponseDatasetsItemSampleImagesItemLabelsItem",
    {
        "classId": int,
        "bbox": NotRequired[list[Any]],
        "segments": NotRequired[list[float]],
        "keypoints": NotRequired[list[float]],
        "obb": NotRequired[list[Any]],
        "skeletonId": NotRequired[str],
    },
)


DatasetsListResponseDatasetsItemSampleImagesItem = TypedDict(
    "DatasetsListResponseDatasetsItemSampleImagesItem",
    {
        "url": str,
        "imageUrl": NotRequired[str],
        "depthPreviewUrl": NotRequired[str],
        "width": int,
        "height": int,
        "labels": NotRequired[list[DatasetsListResponseDatasetsItemSampleImagesItemLabelsItem]],
    },
)


DatasetsListResponseDatasetsItemSourceVariant1 = TypedDict(
    "DatasetsListResponseDatasetsItemSourceVariant1", {"provider": Literal["cloud"]}
)


DatasetsListResponseDatasetsItemSourceVariant2 = TypedDict(
    "DatasetsListResponseDatasetsItemSourceVariant2", {"provider": Literal["roboflow"]}
)


DatasetsListResponseDatasetsItemSourceVariant3 = TypedDict(
    "DatasetsListResponseDatasetsItemSourceVariant3", {"provider": Literal["local"], "keyId": NotRequired[str]}
)


DatasetsListResponseDatasetsItemProcessingError = TypedDict(
    "DatasetsListResponseDatasetsItemProcessingError", {"message": str, "timestamp": str}
)


DatasetsListResponseDatasetsItemLastIngestSummary = TypedDict(
    "DatasetsListResponseDatasetsItemLastIngestSummary",
    {"added": int, "paired": NotRequired[int], "errors": int, "skippedCounts": dict[str, int]},
)


DatasetsListResponseDatasetsItemVersionsItemSplits = TypedDict(
    "DatasetsListResponseDatasetsItemVersionsItemSplits", {"train": int, "val": int, "test": int, "labeled": int}
)


DatasetsListResponseDatasetsItemVersionsItem = TypedDict(
    "DatasetsListResponseDatasetsItemVersionsItem",
    {
        "version": int,
        "description": NotRequired[str],
        "sizeBytes": NotRequired[float],
        "contentHash": NotRequired[str],
        "sourceUpdatedAt": NotRequired[str],
        "imageCount": int,
        "classCount": int,
        "annotationCount": int,
        "splits": DatasetsListResponseDatasetsItemVersionsItemSplits,
        "createdAt": str,
    },
)


DatasetsListResponseDatasetsItem = TypedDict(
    "DatasetsListResponseDatasetsItem",
    {
        "id": str,
        "owner": str,
        "dataset": str,
        "name": str,
        "description": NotRequired[str],
        "visibility": Literal["public", "private"],
        "task": Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"],
        "channels": NotRequired[int],
        "depthScale": NotRequired[float],
        "imageCount": int,
        "classCount": NotRequired[int],
        "classNames": NotRequired[list[str]],
        "format": NotRequired[Literal["yolo", "coco", "raw", "ndjson"]],
        "tags": NotRequired[list[str]],
        "license": NotRequired[
            Literal[
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
        ],
        "splits": DatasetsListResponseDatasetsItemSplits,
        "annotationCount": NotRequired[int],
        "totalBytes": NotRequired[float],
        "starCount": int,
        "isStarred": bool,
        "status": NotRequired[Literal["processing", "ready", "failed"]],
        "sampleImages": NotRequired[list[DatasetsListResponseDatasetsItemSampleImagesItem]],
        "integrationProvider": NotRequired[Literal["gcs", "s3", "azure", "on-premise"]],
        "integrationStatus": NotRequired[Literal["online", "offline", "disconnected"]],
        "source": NotRequired[
            DatasetsListResponseDatasetsItemSourceVariant1
            | DatasetsListResponseDatasetsItemSourceVariant2
            | DatasetsListResponseDatasetsItemSourceVariant3
        ],
        "classColors": NotRequired[dict[str, str]],
        "kptShape": NotRequired[list[Any]],
        "flipIdx": NotRequired[list[int]],
        "processingTimeMs": NotRequired[float],
        "lastIngestJobId": NotRequired[str],
        "processingError": NotRequired[DatasetsListResponseDatasetsItemProcessingError],
        "lastIngestSummary": NotRequired[DatasetsListResponseDatasetsItemLastIngestSummary],
        "errorCount": NotRequired[int],
        "iconColor": NotRequired[str],
        "iconLetter": NotRequired[str],
        "iconImage": NotRequired[str],
        "clonedFrom": NotRequired[str],
        "cloneCount": NotRequired[int],
        "region": NotRequired[Literal["us", "eu", "ap"]],
        "versions": NotRequired[list[DatasetsListResponseDatasetsItemVersionsItem]],
        "createdAt": str,
        "updatedAt": str,
    },
)


DatasetsListResponse = TypedDict(
    "DatasetsListResponse",
    {"datasets": list[DatasetsListResponseDatasetsItem], "total": int, "region": Literal["us", "eu", "ap"]},
)


DatasetsCreateResponse = TypedDict(
    "DatasetsCreateResponse", {"id": str, "owner": str, "dataset": str, "region": Literal["us", "eu", "ap"]}
)


DatasetsImportRoboflowResponseImportedItem = TypedDict(
    "DatasetsImportRoboflowResponseImportedItem",
    {"projectId": str, "projectName": str, "version": int, "datasetId": str, "slug": str},
)


DatasetsImportRoboflowResponseFailedItem = TypedDict(
    "DatasetsImportRoboflowResponseFailedItem", {"projectId": str, "projectName": str, "version": int, "error": str}
)


DatasetsImportRoboflowResponseSkippedItem = TypedDict(
    "DatasetsImportRoboflowResponseSkippedItem", {"projectId": str, "projectName": str, "version": int}
)


DatasetsImportRoboflowResponse = TypedDict(
    "DatasetsImportRoboflowResponse",
    {
        "imported": list[DatasetsImportRoboflowResponseImportedItem],
        "failed": list[DatasetsImportRoboflowResponseFailedItem],
        "skipped": list[DatasetsImportRoboflowResponseSkippedItem],
    },
)


DatasetsPreviewRoboflowResponseWorkspace = TypedDict(
    "DatasetsPreviewRoboflowResponseWorkspace", {"url": str, "name": str}
)


DatasetsPreviewRoboflowResponseNewDatasetsItem = TypedDict(
    "DatasetsPreviewRoboflowResponseNewDatasetsItem",
    {
        "workspace": str,
        "projectId": str,
        "projectName": str,
        "projectType": str,
        "latestVersion": int,
        "latestVersionName": NotRequired[str],
    },
)


DatasetsPreviewRoboflowResponseStorage = TypedDict(
    "DatasetsPreviewRoboflowResponseStorage", {"usedBytes": float, "limitBytes": float, "hasEnoughStorage": bool}
)


DatasetsPreviewRoboflowResponse = TypedDict(
    "DatasetsPreviewRoboflowResponse",
    {
        "workspace": DatasetsPreviewRoboflowResponseWorkspace,
        "newDatasets": list[DatasetsPreviewRoboflowResponseNewDatasetsItem],
        "skippedCount": int,
        "missingVersionCount": int,
        "unsupportedCount": int,
        "unresolvedCount": int,
        "bytesTotal": int,
        "storage": DatasetsPreviewRoboflowResponseStorage,
    },
)


DeploymentsRetrieveResponseDeploymentResources = TypedDict(
    "DeploymentsRetrieveResponseDeploymentResources",
    {"cpu": float, "memoryGi": float, "minInstances": float, "maxInstances": float},
)


DeploymentsRetrieveResponseDeployment = TypedDict(
    "DeploymentsRetrieveResponseDeployment",
    {
        "id": str,
        "owner": str,
        "project": NotRequired[str],
        "model": NotRequired[str],
        "task": NotRequired[Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"]],
        "deployment": str,
        "name": str,
        "status": Literal["creating", "deploying", "ready", "stopping", "stopped", "failed"],
        "statusMessage": NotRequired[str],
        "region": str,
        "serviceUrl": NotRequired[str],
        "resources": DeploymentsRetrieveResponseDeploymentResources,
        "deployedAt": NotRequired[str],
        "apiKeyId": NotRequired[str],
        "createdAt": str,
        "updatedAt": str,
    },
)


DeploymentsRetrieveResponse = TypedDict(
    "DeploymentsRetrieveResponse",
    {"deployment": DeploymentsRetrieveResponseDeployment, "region": Literal["us", "eu", "ap"]},
)


DeploymentsUpdateResponseVariant1 = TypedDict(
    "DeploymentsUpdateResponseVariant1",
    {"success": Literal[True], "status": Literal["ready", "stopped"], "message": str},
)


DeploymentsUpdateResponseVariant2 = TypedDict(
    "DeploymentsUpdateResponseVariant2",
    {"success": Literal[True], "status": Literal["deploying", "stopping"], "message": str},
)


DeploymentsUpdateResponse = DeploymentsUpdateResponseVariant1 | DeploymentsUpdateResponseVariant2


DeploymentsDeleteResponse = TypedDict("DeploymentsDeleteResponse", {"success": Literal[True]})


DeploymentsHealthResponse = TypedDict(
    "DeploymentsHealthResponse",
    {"healthy": bool, "status": NotRequired[float], "latencyMs": float, "error": NotRequired[str]},
)


DeploymentsLogsResponseEntriesItemHttpRequest = TypedDict(
    "DeploymentsLogsResponseEntriesItemHttpRequest",
    {"method": str, "url": str, "status": float, "latencyMs": float, "userAgent": NotRequired[str]},
)


DeploymentsLogsResponseEntriesItem = TypedDict(
    "DeploymentsLogsResponseEntriesItem",
    {
        "timestamp": str,
        "severity": Literal["DEFAULT", "DEBUG", "INFO", "NOTICE", "WARNING", "ERROR", "CRITICAL", "ALERT", "EMERGENCY"],
        "message": str,
        "httpRequest": NotRequired[DeploymentsLogsResponseEntriesItemHttpRequest],
    },
)


DeploymentsLogsResponse = TypedDict(
    "DeploymentsLogsResponse", {"entries": list[DeploymentsLogsResponseEntriesItem], "nextPageToken": NotRequired[str]}
)


DeploymentsMetricsResponseVariant1TimeRange = TypedDict(
    "DeploymentsMetricsResponseVariant1TimeRange", {"start": str, "end": str}
)


DeploymentsMetricsResponseVariant1Summary = TypedDict(
    "DeploymentsMetricsResponseVariant1Summary",
    {
        "totalRequests": float,
        "errorCount": float,
        "errorRate": float,
        "avgLatencyMs": float,
        "p50LatencyMs": float,
        "p95LatencyMs": float,
        "p99LatencyMs": float,
    },
)


DeploymentsMetricsResponseVariant1TimeSeriesRequestsItem = TypedDict(
    "DeploymentsMetricsResponseVariant1TimeSeriesRequestsItem", {"timestamp": str, "value": float}
)


DeploymentsMetricsResponseVariant1TimeSeriesErrorsItem = TypedDict(
    "DeploymentsMetricsResponseVariant1TimeSeriesErrorsItem", {"timestamp": str, "value": float}
)


DeploymentsMetricsResponseVariant1TimeSeriesLatencyP50Item = TypedDict(
    "DeploymentsMetricsResponseVariant1TimeSeriesLatencyP50Item", {"timestamp": str, "value": float}
)


DeploymentsMetricsResponseVariant1TimeSeriesLatencyP95Item = TypedDict(
    "DeploymentsMetricsResponseVariant1TimeSeriesLatencyP95Item", {"timestamp": str, "value": float}
)


DeploymentsMetricsResponseVariant1TimeSeriesCpuUtilizationItem = TypedDict(
    "DeploymentsMetricsResponseVariant1TimeSeriesCpuUtilizationItem", {"timestamp": str, "value": float}
)


DeploymentsMetricsResponseVariant1TimeSeriesMemoryUtilizationItem = TypedDict(
    "DeploymentsMetricsResponseVariant1TimeSeriesMemoryUtilizationItem", {"timestamp": str, "value": float}
)


DeploymentsMetricsResponseVariant1TimeSeriesInstanceCountItem = TypedDict(
    "DeploymentsMetricsResponseVariant1TimeSeriesInstanceCountItem", {"timestamp": str, "value": float}
)


DeploymentsMetricsResponseVariant1TimeSeries = TypedDict(
    "DeploymentsMetricsResponseVariant1TimeSeries",
    {
        "requests": list[DeploymentsMetricsResponseVariant1TimeSeriesRequestsItem],
        "errors": list[DeploymentsMetricsResponseVariant1TimeSeriesErrorsItem],
        "latencyP50": list[DeploymentsMetricsResponseVariant1TimeSeriesLatencyP50Item],
        "latencyP95": list[DeploymentsMetricsResponseVariant1TimeSeriesLatencyP95Item],
        "cpuUtilization": list[DeploymentsMetricsResponseVariant1TimeSeriesCpuUtilizationItem],
        "memoryUtilization": list[DeploymentsMetricsResponseVariant1TimeSeriesMemoryUtilizationItem],
        "instanceCount": list[DeploymentsMetricsResponseVariant1TimeSeriesInstanceCountItem],
    },
)


DeploymentsMetricsResponseVariant1 = TypedDict(
    "DeploymentsMetricsResponseVariant1",
    {
        "deploymentId": str,
        "region": str,
        "timeRange": DeploymentsMetricsResponseVariant1TimeRange,
        "summary": DeploymentsMetricsResponseVariant1Summary,
        "timeSeries": DeploymentsMetricsResponseVariant1TimeSeries,
    },
)


DeploymentsMetricsResponseVariant2 = TypedDict(
    "DeploymentsMetricsResponseVariant2",
    {"requests24h": list[float], "totalRequests": float, "errorRate": float, "avgLatencyMs": float},
)


DeploymentsMetricsResponse = DeploymentsMetricsResponseVariant1 | DeploymentsMetricsResponseVariant2


DeploymentsPredictResponseImagesItemSpeed = TypedDict(
    "DeploymentsPredictResponseImagesItemSpeed", {"preprocess": float, "inference": float, "postprocess": float}
)


DeploymentsPredictResponseImagesItemResultsItemBox = TypedDict(
    "DeploymentsPredictResponseImagesItemResultsItemBox",
    {
        "x1": float,
        "y1": float,
        "x2": float,
        "y2": float,
        "x3": NotRequired[float],
        "y3": NotRequired[float],
        "x4": NotRequired[float],
        "y4": NotRequired[float],
    },
)


DeploymentsPredictResponseImagesItemResultsItemSegments = TypedDict(
    "DeploymentsPredictResponseImagesItemResultsItemSegments", {"x": list[float], "y": list[float]}
)


DeploymentsPredictResponseImagesItemResultsItemKeypoints = TypedDict(
    "DeploymentsPredictResponseImagesItemResultsItemKeypoints",
    {"x": list[float], "y": list[float], "visible": NotRequired[list[float]]},
)


DeploymentsPredictResponseImagesItemResultsItem = TypedDict(
    "DeploymentsPredictResponseImagesItemResultsItem",
    {
        "name": str,
        "class": int,
        "confidence": NotRequired[float],
        "pixel_ratio": NotRequired[float],
        "box": NotRequired[DeploymentsPredictResponseImagesItemResultsItemBox],
        "segments": NotRequired[DeploymentsPredictResponseImagesItemResultsItemSegments],
        "keypoints": NotRequired[DeploymentsPredictResponseImagesItemResultsItemKeypoints],
    },
)


DeploymentsPredictResponseImagesItemSemanticMask = TypedDict(
    "DeploymentsPredictResponseImagesItemSemanticMask", {"shape": list[float], "encoding": Literal["png"], "data": str}
)


DeploymentsPredictResponseImagesItemDepth = TypedDict(
    "DeploymentsPredictResponseImagesItemDepth",
    {
        "shape": list[float],
        "encoding": Literal["png"],
        "data": str,
        "min": float,
        "max": float,
        "bits": Literal[8, 12, 16],
    },
)


DeploymentsPredictResponseImagesItem = TypedDict(
    "DeploymentsPredictResponseImagesItem",
    {
        "shape": list[float],
        "speed": DeploymentsPredictResponseImagesItemSpeed,
        "results": list[DeploymentsPredictResponseImagesItemResultsItem],
        "semantic_mask": NotRequired[DeploymentsPredictResponseImagesItemSemanticMask],
        "depth": NotRequired[DeploymentsPredictResponseImagesItemDepth],
    },
)


DeploymentsPredictResponseMetadata = TypedDict(
    "DeploymentsPredictResponseMetadata",
    {
        "imageCount": int,
        "functionTimeAlive": float,
        "functionTimeCall": float,
        "model": NotRequired[str],
        "task": NotRequired[Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"] | None],
        "version": dict[str, str],
    },
)


DeploymentsPredictResponse = TypedDict(
    "DeploymentsPredictResponse",
    {"images": list[DeploymentsPredictResponseImagesItem], "metadata": DeploymentsPredictResponseMetadata},
)


DeploymentsListResponse = TypedDict(
    "DeploymentsListResponse",
    {"deployments": list[DeploymentsRetrieveResponseDeployment], "total": float, "region": Literal["us", "eu", "ap"]},
)


DeploymentsCreateResponse = TypedDict(
    "DeploymentsCreateResponse",
    {"id": str, "deployment": str, "status": Literal["creating"], "message": str, "region": str},
)


ExploreSearchResponseProjectsItem = TypedDict(
    "ExploreSearchResponseProjectsItem",
    {
        "id": str,
        "project": str,
        "name": str,
        "description": NotRequired[str],
        "owner": str,
        "visibility": Literal["public", "private"],
        "iconColor": NotRequired[str],
        "iconLetter": NotRequired[str],
        "iconImage": NotRequired[str],
        "modelCount": int,
        "modelNames": list[str],
        "totalBytes": float,
        "starCount": int,
        "userImageUrl": NotRequired[str],
        "updatedAt": str,
    },
)


ExploreSearchResponseDatasetsItemSplits = TypedDict(
    "ExploreSearchResponseDatasetsItemSplits", {"train": int, "val": int, "test": int, "labeled": int}
)


ExploreSearchResponseDatasetsItemSampleImagesItemLabelsItem = TypedDict(
    "ExploreSearchResponseDatasetsItemSampleImagesItemLabelsItem",
    {
        "classId": int,
        "bbox": NotRequired[list[Any]],
        "segments": NotRequired[list[float]],
        "keypoints": NotRequired[list[float]],
        "obb": NotRequired[list[Any]],
        "skeletonId": NotRequired[str],
    },
)


ExploreSearchResponseDatasetsItemSampleImagesItem = TypedDict(
    "ExploreSearchResponseDatasetsItemSampleImagesItem",
    {
        "url": str,
        "imageUrl": NotRequired[str],
        "width": float,
        "height": float,
        "labels": NotRequired[list[ExploreSearchResponseDatasetsItemSampleImagesItemLabelsItem]],
    },
)


ExploreSearchResponseDatasetsItem = TypedDict(
    "ExploreSearchResponseDatasetsItem",
    {
        "id": str,
        "dataset": str,
        "name": str,
        "description": NotRequired[str],
        "owner": str,
        "visibility": Literal["public", "private"],
        "imageCount": int,
        "classCount": NotRequired[int],
        "classNames": NotRequired[list[str]],
        "classColors": NotRequired[dict[str, str]],
        "task": Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"],
        "totalBytes": NotRequired[float],
        "tags": NotRequired[list[str]],
        "splits": NotRequired[ExploreSearchResponseDatasetsItemSplits],
        "kptShape": NotRequired[list[Any]],
        "starCount": int,
        "sampleImages": list[ExploreSearchResponseDatasetsItemSampleImagesItem],
        "userImageUrl": NotRequired[str],
        "updatedAt": str,
    },
)


ExploreSearchResponse = TypedDict(
    "ExploreSearchResponse",
    {
        "projects": list[ExploreSearchResponseProjectsItem],
        "datasets": list[ExploreSearchResponseDatasetsItem],
        "hasMore": bool,
    },
)


ImagesRetrieveResponsePropertiesDepth = TypedDict(
    "ImagesRetrieveResponsePropertiesDepth",
    {
        "hash": str,
        "bytes": int,
        "shape": list[int],
        "min": NotRequired[float],
        "max": NotRequired[float],
        "validFraction": NotRequired[float],
    },
)


ImagesRetrieveResponseProperties = TypedDict(
    "ImagesRetrieveResponseProperties",
    {
        "id": str,
        "datasetId": str,
        "filename": str,
        "hash": str,
        "extension": str,
        "originalExtension": NotRequired[str],
        "originalPath": NotRequired[str],
        "width": int,
        "height": int,
        "split": Literal["train", "val", "test"],
        "annotationCount": int,
        "classIds": NotRequired[list[int]],
        "depth": NotRequired[ImagesRetrieveResponsePropertiesDepth],
        "bytes": NotRequired[int],
        "region": NotRequired[Literal["us", "eu", "ap"]],
        "externalKey": NotRequired[str],
        "externalRevision": NotRequired[str],
        "retainedByVersion": bool,
        "createdAt": str,
        "updatedAt": NotRequired[str],
        "error": NotRequired[str | None],
    },
)


ImagesRetrieveResponseLabelsItem = TypedDict(
    "ImagesRetrieveResponseLabelsItem",
    {
        "classId": int,
        "bbox": NotRequired[list[Any]],
        "segments": NotRequired[list[float]],
        "keypoints": NotRequired[list[float]],
        "obb": NotRequired[list[Any]],
        "skeletonId": NotRequired[str],
    },
)


ImagesRetrieveResponse = TypedDict(
    "ImagesRetrieveResponse",
    {
        "metadata": dict[str, Any],
        "properties": ImagesRetrieveResponseProperties,
        "labels": list[ImagesRetrieveResponseLabelsItem],
        "classNames": list[str],
        "labelsTruncated": NotRequired[Literal[True]],
    },
)


ImagesUpdateResponseVariant1LabelsItem = TypedDict(
    "ImagesUpdateResponseVariant1LabelsItem",
    {
        "classId": int,
        "bbox": NotRequired[list[Any]],
        "segments": NotRequired[list[float]],
        "keypoints": NotRequired[list[float]],
        "obb": NotRequired[list[Any]],
        "skeletonId": NotRequired[str],
    },
)


ImagesUpdateResponseVariant1 = TypedDict(
    "ImagesUpdateResponseVariant1",
    {"success": Literal[True], "labels": list[ImagesUpdateResponseVariant1LabelsItem], "labelCount": int},
)


ImagesUpdateResponseVariant2 = TypedDict("ImagesUpdateResponseVariant2", {"metadata": dict[str, Any], "updatedAt": str})


ImagesUpdateResponse = ImagesUpdateResponseVariant1 | ImagesUpdateResponseVariant2


ImagesDeleteResponse = TypedDict(
    "ImagesDeleteResponse", {"success": Literal[True], "deletedImageId": str, "deletedCount": int}
)


ImagesPredictResponsePredictionsItem = TypedDict(
    "ImagesPredictResponsePredictionsItem",
    {
        "classId": int,
        "bbox": NotRequired[list[Any]],
        "segments": NotRequired[list[float]],
        "keypoints": NotRequired[list[float]],
        "obb": NotRequired[list[Any]],
        "skeletonId": NotRequired[str],
    },
)


ImagesPredictResponse = TypedDict(
    "ImagesPredictResponse",
    {
        "success": Literal[True],
        "predictions": list[ImagesPredictResponsePredictionsItem],
        "confidences": NotRequired[list[float]],
        "modelUsed": str,
        "inferenceTime": NotRequired[float],
    },
)


ImagesUpdateBulkResponse = TypedDict(
    "ImagesUpdateBulkResponse",
    {
        "success": Literal[True],
        "modifiedCount": int,
        "skippedCount": int,
        "targetSplit": Literal["train", "val", "test"],
    },
)


ImagesDeleteBulkResponse = TypedDict(
    "ImagesDeleteBulkResponse", {"success": Literal[True], "deletedCount": int, "deletedImageIds": list[str]}
)


ImagesUrlsResponseDepthsValue = TypedDict("ImagesUrlsResponseDepthsValue", {"previewUrl": str})


ImagesUrlsResponse = TypedDict(
    "ImagesUrlsResponse",
    {"urls": dict[str, str], "thumbnails": dict[str, str], "depths": dict[str, ImagesUrlsResponseDepthsValue]},
)


StorageIntegrationsDeleteResponse = TypedDict("StorageIntegrationsDeleteResponse", {"success": Literal[True]})


StorageIntegrationsObjectsResponseEntriesItem = TypedDict(
    "StorageIntegrationsObjectsResponseEntriesItem",
    {
        "kind": Literal["folder", "file"],
        "name": str,
        "key": str,
        "size": NotRequired[float],
        "updatedAt": NotRequired[str],
    },
)


StorageIntegrationsObjectsResponse = TypedDict(
    "StorageIntegrationsObjectsResponse",
    {"entries": list[StorageIntegrationsObjectsResponseEntriesItem], "cursor": NotRequired[str]},
)


StorageIntegrationsListResponseIntegrationsItem = TypedDict(
    "StorageIntegrationsListResponseIntegrationsItem",
    {
        "id": str,
        "provider": Literal["gcs", "s3", "azure"],
        "credentialIdentity": str,
        "targets": list[str],
        "createdAt": str,
    },
)


StorageIntegrationsListResponse = TypedDict(
    "StorageIntegrationsListResponse", {"integrations": list[StorageIntegrationsListResponseIntegrationsItem]}
)


StorageIntegrationsCreateResponse = TypedDict(
    "StorageIntegrationsCreateResponse",
    {
        "id": str,
        "provider": Literal["gcs", "s3", "azure"],
        "credentialIdentity": str,
        "targets": list[str],
        "createdAt": str,
    },
)


StorageIntegrationsDiscoverResponse = TypedDict("StorageIntegrationsDiscoverResponse", {"targets": list[str]})


ModelsCloneResponse = TypedDict(
    "ModelsCloneResponse",
    {"id": str, "owner": str, "project": str, "model": str, "name": str, "region": Literal["us", "eu", "ap"]},
)


ModelsRetrieveResponseVariant1ModelDatasetVersion = TypedDict(
    "ModelsRetrieveResponseVariant1ModelDatasetVersion", {"version": int, "contentHash": str}
)


ModelsRetrieveResponseVariant1ModelSourceModel = TypedDict(
    "ModelsRetrieveResponseVariant1ModelSourceModel",
    {
        "owner": str,
        "project": str,
        "projectName": str,
        "projectIconColor": NotRequired[str],
        "projectIconLetter": NotRequired[str],
        "projectIconImage": NotRequired[str],
        "model": str,
        "modelName": str,
    },
)


ModelsRetrieveResponseVariant1ModelTrainResultsItem = TypedDict(
    "ModelsRetrieveResponseVariant1ModelTrainResultsItem",
    {
        "epoch": NotRequired[int],
        "metrics": NotRequired[dict[str, float]],
        "fitness": NotRequired[float],
        "timestamp": NotRequired[str],
    },
)


ModelsRetrieveResponseVariant1ModelFile = TypedDict("ModelsRetrieveResponseVariant1ModelFile", {"size": float})


ModelsRetrieveResponseVariant1ModelTrainingError = TypedDict(
    "ModelsRetrieveResponseVariant1ModelTrainingError", {"message": str, "code": NotRequired[str], "timestamp": str}
)


ModelsRetrieveResponseVariant1ModelComputeCost = TypedDict(
    "ModelsRetrieveResponseVariant1ModelComputeCost",
    {
        "gpuType": NotRequired[str],
        "gpuDisplayName": NotRequired[str],
        "pricePerHour": float,
        "totalCost": float,
        "durationMs": NotRequired[float],
    },
)


ModelsRetrieveResponseVariant1ModelCloudJob = TypedDict(
    "ModelsRetrieveResponseVariant1ModelCloudJob", {"gpuDisplayName": str}
)


ModelsRetrieveResponseVariant1ModelConsoleChunksItem = TypedDict(
    "ModelsRetrieveResponseVariant1ModelConsoleChunksItem",
    {"chunkId": float, "content": str, "lineCount": float, "timestamp": str},
)


ModelsRetrieveResponseVariant1ModelDataset = TypedDict(
    "ModelsRetrieveResponseVariant1ModelDataset", {"owner": str, "dataset": str}
)


ModelsRetrieveResponseVariant1Model = TypedDict(
    "ModelsRetrieveResponseVariant1Model",
    {
        "id": str,
        "owner": str,
        "project": str,
        "projectName": str,
        "projectIconColor": NotRequired[str],
        "projectIconLetter": NotRequired[str],
        "projectIconImage": NotRequired[str],
        "model": str,
        "visibility": Literal["public", "private"],
        "name": str,
        "description": NotRequired[str],
        "license": NotRequired[
            Literal[
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
        ],
        "status": NotRequired[
            Literal["pending", "untrained", "starting", "running", "completed", "failed", "cancelled"]
        ],
        "task": NotRequired[Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"]],
        "depthScaleVerified": NotRequired[bool],
        "color": NotRequired[str],
        "datasetId": NotRequired[str],
        "datasetVersion": NotRequired[ModelsRetrieveResponseVariant1ModelDatasetVersion],
        "sourceModelId": NotRequired[str],
        "sourceModel": NotRequired[ModelsRetrieveResponseVariant1ModelSourceModel],
        "baseModel": NotRequired[str],
        "epochs": NotRequired[int],
        "bestEpoch": NotRequired[int | None],
        "bestFitness": NotRequired[float | None],
        "trainArgs": NotRequired[dict[str, Any]],
        "metrics": NotRequired[dict[str, float]],
        "trainResults": NotRequired[list[ModelsRetrieveResponseVariant1ModelTrainResultsItem]],
        "hasWeights": bool,
        "file": NotRequired[ModelsRetrieveResponseVariant1ModelFile],
        "version": NotRequired[str],
        "docs": NotRequired[str],
        "startedAt": NotRequired[str],
        "completedAt": NotRequired[str],
        "classNames": NotRequired[list[str]],
        "plots": NotRequired[list[Any]],
        "trainingError": NotRequired[ModelsRetrieveResponseVariant1ModelTrainingError],
        "starCount": int,
        "isStarred": bool,
        "clonedFrom": NotRequired[str],
        "cloneCount": NotRequired[int],
        "environment": NotRequired[dict[str, Any]],
        "computeCost": NotRequired[ModelsRetrieveResponseVariant1ModelComputeCost],
        "cloudJob": NotRequired[ModelsRetrieveResponseVariant1ModelCloudJob],
        "consoleChunks": NotRequired[list[ModelsRetrieveResponseVariant1ModelConsoleChunksItem]],
        "createdAt": str,
        "updatedAt": str,
        "metadata": dict[str, Any],
        "dataset": NotRequired[ModelsRetrieveResponseVariant1ModelDataset],
    },
)


ModelsRetrieveResponseVariant1 = TypedDict(
    "ModelsRetrieveResponseVariant1", {"model": ModelsRetrieveResponseVariant1Model, "isOwner": bool}
)


ModelsRetrieveResponseVariant2AnalysisCoverage = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisCoverage",
    {
        "mode": Literal["full", "sampled", "tails", "partial", "unavailable"],
        "omittedMiddle": int,
        "unmatchedExtremes": int,
    },
)


ModelsRetrieveResponseVariant2AnalysisScatterSample = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisScatterSample", {"eligible": int, "rows": list[list[Any]]}
)


ModelsRetrieveResponseVariant2AnalysisCohortsWorstMetricsF1 = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisCohortsWorstMetricsF1",
    {"count": int, "min": float, "p25": float, "median": float, "p75": float, "max": float, "mean": float},
)


ModelsRetrieveResponseVariant2AnalysisCohortsWorstMetrics = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisCohortsWorstMetrics",
    {"tp": int, "fp": int, "fn": int, "f1": ModelsRetrieveResponseVariant2AnalysisCohortsWorstMetricsF1 | None},
)


ModelsRetrieveResponseVariant2AnalysisCohortsWorstExamplesItemLabelsItem = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisCohortsWorstExamplesItemLabelsItem",
    {
        "classId": int,
        "bbox": NotRequired[list[Any]],
        "segments": NotRequired[list[float]],
        "keypoints": NotRequired[list[float]],
        "obb": NotRequired[list[Any]],
        "skeletonId": NotRequired[str],
    },
)


ModelsRetrieveResponseVariant2AnalysisCohortsWorstExamplesItem = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisCohortsWorstExamplesItem",
    {
        "imageId": NotRequired[str],
        "hash": str,
        "tp": int,
        "fp": int,
        "fn": int,
        "f1": float,
        "isEmptyGroundTruth": bool,
        "width": NotRequired[float],
        "height": NotRequired[float],
        "pixels": NotRequired[float],
        "aspectRatio": NotRequired[float],
        "instanceCount": NotRequired[int],
        "labels": NotRequired[list[ModelsRetrieveResponseVariant2AnalysisCohortsWorstExamplesItemLabelsItem]],
    },
)


ModelsRetrieveResponseVariant2AnalysisCohortsWorst = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisCohortsWorst",
    {
        "count": int,
        "matched": int,
        "metrics": ModelsRetrieveResponseVariant2AnalysisCohortsWorstMetrics,
        "examples": list[ModelsRetrieveResponseVariant2AnalysisCohortsWorstExamplesItem],
    },
)


ModelsRetrieveResponseVariant2AnalysisCohortsBestMetricsF1 = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisCohortsBestMetricsF1",
    {"count": int, "min": float, "p25": float, "median": float, "p75": float, "max": float, "mean": float},
)


ModelsRetrieveResponseVariant2AnalysisCohortsBestMetrics = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisCohortsBestMetrics",
    {"tp": int, "fp": int, "fn": int, "f1": ModelsRetrieveResponseVariant2AnalysisCohortsBestMetricsF1 | None},
)


ModelsRetrieveResponseVariant2AnalysisCohortsBestExamplesItemLabelsItem = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisCohortsBestExamplesItemLabelsItem",
    {
        "classId": int,
        "bbox": NotRequired[list[Any]],
        "segments": NotRequired[list[float]],
        "keypoints": NotRequired[list[float]],
        "obb": NotRequired[list[Any]],
        "skeletonId": NotRequired[str],
    },
)


ModelsRetrieveResponseVariant2AnalysisCohortsBestExamplesItem = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisCohortsBestExamplesItem",
    {
        "imageId": NotRequired[str],
        "hash": str,
        "tp": int,
        "fp": int,
        "fn": int,
        "f1": float,
        "isEmptyGroundTruth": bool,
        "width": NotRequired[float],
        "height": NotRequired[float],
        "pixels": NotRequired[float],
        "aspectRatio": NotRequired[float],
        "instanceCount": NotRequired[int],
        "labels": NotRequired[list[ModelsRetrieveResponseVariant2AnalysisCohortsBestExamplesItemLabelsItem]],
    },
)


ModelsRetrieveResponseVariant2AnalysisCohortsBest = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisCohortsBest",
    {
        "count": int,
        "matched": int,
        "metrics": ModelsRetrieveResponseVariant2AnalysisCohortsBestMetrics,
        "examples": list[ModelsRetrieveResponseVariant2AnalysisCohortsBestExamplesItem],
    },
)


ModelsRetrieveResponseVariant2AnalysisCohorts = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisCohorts",
    {
        "worst": ModelsRetrieveResponseVariant2AnalysisCohortsWorst,
        "best": ModelsRetrieveResponseVariant2AnalysisCohortsBest,
    },
)


ModelsRetrieveResponseVariant2AnalysisComparisonsWidthWorst = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisComparisonsWidthWorst",
    {"count": int, "min": float, "p25": float, "median": float, "p75": float, "max": float, "mean": float},
)


ModelsRetrieveResponseVariant2AnalysisComparisonsWidthBest = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisComparisonsWidthBest",
    {"count": int, "min": float, "p25": float, "median": float, "p75": float, "max": float, "mean": float},
)


ModelsRetrieveResponseVariant2AnalysisComparisonsWidthRelationshipFit = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisComparisonsWidthRelationshipFit",
    {"slope": float, "intercept": float, "pearsonR": float, "rSquared": float},
)


ModelsRetrieveResponseVariant2AnalysisComparisonsWidthRelationshipCovariance = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisComparisonsWidthRelationshipCovariance",
    {"mean": list[Any], "eigenvalues": list[Any], "eigenvectors": list[Any]},
)


ModelsRetrieveResponseVariant2AnalysisComparisonsWidthRelationship = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisComparisonsWidthRelationship",
    {
        "count": int,
        "fit": ModelsRetrieveResponseVariant2AnalysisComparisonsWidthRelationshipFit | None,
        "covariance": ModelsRetrieveResponseVariant2AnalysisComparisonsWidthRelationshipCovariance | None,
    },
)


ModelsRetrieveResponseVariant2AnalysisComparisonsWidth = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisComparisonsWidth",
    {
        "worst": ModelsRetrieveResponseVariant2AnalysisComparisonsWidthWorst | None,
        "best": ModelsRetrieveResponseVariant2AnalysisComparisonsWidthBest | None,
        "relationship": ModelsRetrieveResponseVariant2AnalysisComparisonsWidthRelationship,
    },
)


ModelsRetrieveResponseVariant2AnalysisComparisonsHeightWorst = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisComparisonsHeightWorst",
    {"count": int, "min": float, "p25": float, "median": float, "p75": float, "max": float, "mean": float},
)


ModelsRetrieveResponseVariant2AnalysisComparisonsHeightBest = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisComparisonsHeightBest",
    {"count": int, "min": float, "p25": float, "median": float, "p75": float, "max": float, "mean": float},
)


ModelsRetrieveResponseVariant2AnalysisComparisonsHeightRelationshipFit = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisComparisonsHeightRelationshipFit",
    {"slope": float, "intercept": float, "pearsonR": float, "rSquared": float},
)


ModelsRetrieveResponseVariant2AnalysisComparisonsHeightRelationshipCovariance = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisComparisonsHeightRelationshipCovariance",
    {"mean": list[Any], "eigenvalues": list[Any], "eigenvectors": list[Any]},
)


ModelsRetrieveResponseVariant2AnalysisComparisonsHeightRelationship = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisComparisonsHeightRelationship",
    {
        "count": int,
        "fit": ModelsRetrieveResponseVariant2AnalysisComparisonsHeightRelationshipFit | None,
        "covariance": ModelsRetrieveResponseVariant2AnalysisComparisonsHeightRelationshipCovariance | None,
    },
)


ModelsRetrieveResponseVariant2AnalysisComparisonsHeight = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisComparisonsHeight",
    {
        "worst": ModelsRetrieveResponseVariant2AnalysisComparisonsHeightWorst | None,
        "best": ModelsRetrieveResponseVariant2AnalysisComparisonsHeightBest | None,
        "relationship": ModelsRetrieveResponseVariant2AnalysisComparisonsHeightRelationship,
    },
)


ModelsRetrieveResponseVariant2AnalysisComparisonsPixelsWorst = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisComparisonsPixelsWorst",
    {"count": int, "min": float, "p25": float, "median": float, "p75": float, "max": float, "mean": float},
)


ModelsRetrieveResponseVariant2AnalysisComparisonsPixelsBest = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisComparisonsPixelsBest",
    {"count": int, "min": float, "p25": float, "median": float, "p75": float, "max": float, "mean": float},
)


ModelsRetrieveResponseVariant2AnalysisComparisonsPixelsRelationshipFit = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisComparisonsPixelsRelationshipFit",
    {"slope": float, "intercept": float, "pearsonR": float, "rSquared": float},
)


ModelsRetrieveResponseVariant2AnalysisComparisonsPixelsRelationshipCovariance = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisComparisonsPixelsRelationshipCovariance",
    {"mean": list[Any], "eigenvalues": list[Any], "eigenvectors": list[Any]},
)


ModelsRetrieveResponseVariant2AnalysisComparisonsPixelsRelationship = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisComparisonsPixelsRelationship",
    {
        "count": int,
        "fit": ModelsRetrieveResponseVariant2AnalysisComparisonsPixelsRelationshipFit | None,
        "covariance": ModelsRetrieveResponseVariant2AnalysisComparisonsPixelsRelationshipCovariance | None,
    },
)


ModelsRetrieveResponseVariant2AnalysisComparisonsPixels = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisComparisonsPixels",
    {
        "worst": ModelsRetrieveResponseVariant2AnalysisComparisonsPixelsWorst | None,
        "best": ModelsRetrieveResponseVariant2AnalysisComparisonsPixelsBest | None,
        "relationship": ModelsRetrieveResponseVariant2AnalysisComparisonsPixelsRelationship,
    },
)


ModelsRetrieveResponseVariant2AnalysisComparisonsAspectRatioWorst = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisComparisonsAspectRatioWorst",
    {"count": int, "min": float, "p25": float, "median": float, "p75": float, "max": float, "mean": float},
)


ModelsRetrieveResponseVariant2AnalysisComparisonsAspectRatioBest = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisComparisonsAspectRatioBest",
    {"count": int, "min": float, "p25": float, "median": float, "p75": float, "max": float, "mean": float},
)


ModelsRetrieveResponseVariant2AnalysisComparisonsAspectRatioRelationshipFit = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisComparisonsAspectRatioRelationshipFit",
    {"slope": float, "intercept": float, "pearsonR": float, "rSquared": float},
)


ModelsRetrieveResponseVariant2AnalysisComparisonsAspectRatioRelationshipCovariance = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisComparisonsAspectRatioRelationshipCovariance",
    {"mean": list[Any], "eigenvalues": list[Any], "eigenvectors": list[Any]},
)


ModelsRetrieveResponseVariant2AnalysisComparisonsAspectRatioRelationship = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisComparisonsAspectRatioRelationship",
    {
        "count": int,
        "fit": ModelsRetrieveResponseVariant2AnalysisComparisonsAspectRatioRelationshipFit | None,
        "covariance": ModelsRetrieveResponseVariant2AnalysisComparisonsAspectRatioRelationshipCovariance | None,
    },
)


ModelsRetrieveResponseVariant2AnalysisComparisonsAspectRatio = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisComparisonsAspectRatio",
    {
        "worst": ModelsRetrieveResponseVariant2AnalysisComparisonsAspectRatioWorst | None,
        "best": ModelsRetrieveResponseVariant2AnalysisComparisonsAspectRatioBest | None,
        "relationship": ModelsRetrieveResponseVariant2AnalysisComparisonsAspectRatioRelationship,
    },
)


ModelsRetrieveResponseVariant2AnalysisComparisonsInstanceCountWorst = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisComparisonsInstanceCountWorst",
    {"count": int, "min": float, "p25": float, "median": float, "p75": float, "max": float, "mean": float},
)


ModelsRetrieveResponseVariant2AnalysisComparisonsInstanceCountBest = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisComparisonsInstanceCountBest",
    {"count": int, "min": float, "p25": float, "median": float, "p75": float, "max": float, "mean": float},
)


ModelsRetrieveResponseVariant2AnalysisComparisonsInstanceCountRelationshipFit = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisComparisonsInstanceCountRelationshipFit",
    {"slope": float, "intercept": float, "pearsonR": float, "rSquared": float},
)


ModelsRetrieveResponseVariant2AnalysisComparisonsInstanceCountRelationshipCovariance = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisComparisonsInstanceCountRelationshipCovariance",
    {"mean": list[Any], "eigenvalues": list[Any], "eigenvectors": list[Any]},
)


ModelsRetrieveResponseVariant2AnalysisComparisonsInstanceCountRelationship = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisComparisonsInstanceCountRelationship",
    {
        "count": int,
        "fit": ModelsRetrieveResponseVariant2AnalysisComparisonsInstanceCountRelationshipFit | None,
        "covariance": ModelsRetrieveResponseVariant2AnalysisComparisonsInstanceCountRelationshipCovariance | None,
    },
)


ModelsRetrieveResponseVariant2AnalysisComparisonsInstanceCount = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisComparisonsInstanceCount",
    {
        "worst": ModelsRetrieveResponseVariant2AnalysisComparisonsInstanceCountWorst | None,
        "best": ModelsRetrieveResponseVariant2AnalysisComparisonsInstanceCountBest | None,
        "relationship": ModelsRetrieveResponseVariant2AnalysisComparisonsInstanceCountRelationship,
    },
)


ModelsRetrieveResponseVariant2AnalysisComparisonsClassPresenceItemWorst = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisComparisonsClassPresenceItemWorst", {"count": int, "prevalence": float}
)


ModelsRetrieveResponseVariant2AnalysisComparisonsClassPresenceItemBest = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisComparisonsClassPresenceItemBest", {"count": int, "prevalence": float}
)


ModelsRetrieveResponseVariant2AnalysisComparisonsClassPresenceItem = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisComparisonsClassPresenceItem",
    {
        "classId": int,
        "name": str,
        "worst": ModelsRetrieveResponseVariant2AnalysisComparisonsClassPresenceItemWorst,
        "best": ModelsRetrieveResponseVariant2AnalysisComparisonsClassPresenceItemBest,
        "prevalenceDifference": float,
    },
)


ModelsRetrieveResponseVariant2AnalysisComparisons = TypedDict(
    "ModelsRetrieveResponseVariant2AnalysisComparisons",
    {
        "width": ModelsRetrieveResponseVariant2AnalysisComparisonsWidth,
        "height": ModelsRetrieveResponseVariant2AnalysisComparisonsHeight,
        "pixels": ModelsRetrieveResponseVariant2AnalysisComparisonsPixels,
        "aspectRatio": ModelsRetrieveResponseVariant2AnalysisComparisonsAspectRatio,
        "instanceCount": ModelsRetrieveResponseVariant2AnalysisComparisonsInstanceCount,
        "classPresence": list[ModelsRetrieveResponseVariant2AnalysisComparisonsClassPresenceItem],
        "classPresenceTruncated": bool,
    },
)


ModelsRetrieveResponseVariant2Analysis = TypedDict(
    "ModelsRetrieveResponseVariant2Analysis",
    {
        "population": int,
        "retained": int,
        "matched": int,
        "unmatched": int,
        "traitsAvailable": bool,
        "sourceSplit": Literal["train", "val"] | None,
        "coverage": ModelsRetrieveResponseVariant2AnalysisCoverage,
        "scatterSample": ModelsRetrieveResponseVariant2AnalysisScatterSample,
        "cohorts": ModelsRetrieveResponseVariant2AnalysisCohorts,
        "comparisons": ModelsRetrieveResponseVariant2AnalysisComparisons | None,
    },
)


ModelsRetrieveResponseVariant2 = TypedDict(
    "ModelsRetrieveResponseVariant2", {"analysis": ModelsRetrieveResponseVariant2Analysis | None}
)


ModelsRetrieveResponse = ModelsRetrieveResponseVariant1 | ModelsRetrieveResponseVariant2


ModelsUpdateResponseVariant1 = TypedDict(
    "ModelsUpdateResponseVariant1", {"success": Literal[True], "model": str, "datasetLinked": NotRequired[bool]}
)


ModelsUpdateResponseVariant2 = TypedDict("ModelsUpdateResponseVariant2", {"starred": bool, "starCount": int})


ModelsUpdateResponse = ModelsUpdateResponseVariant1 | ModelsUpdateResponseVariant2


ModelsDeleteResponse = TypedDict("ModelsDeleteResponse", {"success": Literal[True]})


ModelsFilesResponseFilesItem = TypedDict(
    "ModelsFilesResponseFilesItem", {"name": str, "size": float, "downloadUrl": str}
)


ModelsFilesResponse = TypedDict("ModelsFilesResponse", {"files": list[ModelsFilesResponseFilesItem]})


ModelsPredictResponseImagesItemSpeed = TypedDict(
    "ModelsPredictResponseImagesItemSpeed", {"preprocess": float, "inference": float, "postprocess": float}
)


ModelsPredictResponseImagesItemResultsItemBox = TypedDict(
    "ModelsPredictResponseImagesItemResultsItemBox",
    {
        "x1": float,
        "y1": float,
        "x2": float,
        "y2": float,
        "x3": NotRequired[float],
        "y3": NotRequired[float],
        "x4": NotRequired[float],
        "y4": NotRequired[float],
    },
)


ModelsPredictResponseImagesItemResultsItemSegments = TypedDict(
    "ModelsPredictResponseImagesItemResultsItemSegments", {"x": list[float], "y": list[float]}
)


ModelsPredictResponseImagesItemResultsItemKeypoints = TypedDict(
    "ModelsPredictResponseImagesItemResultsItemKeypoints",
    {"x": list[float], "y": list[float], "visible": NotRequired[list[float]]},
)


ModelsPredictResponseImagesItemResultsItem = TypedDict(
    "ModelsPredictResponseImagesItemResultsItem",
    {
        "name": str,
        "class": int,
        "confidence": NotRequired[float],
        "pixel_ratio": NotRequired[float],
        "box": NotRequired[ModelsPredictResponseImagesItemResultsItemBox],
        "segments": NotRequired[ModelsPredictResponseImagesItemResultsItemSegments],
        "keypoints": NotRequired[ModelsPredictResponseImagesItemResultsItemKeypoints],
    },
)


ModelsPredictResponseImagesItemSemanticMask = TypedDict(
    "ModelsPredictResponseImagesItemSemanticMask", {"shape": list[float], "encoding": Literal["png"], "data": str}
)


ModelsPredictResponseImagesItemDepth = TypedDict(
    "ModelsPredictResponseImagesItemDepth",
    {
        "shape": list[float],
        "encoding": Literal["png"],
        "data": str,
        "min": float,
        "max": float,
        "bits": Literal[8, 12, 16],
    },
)


ModelsPredictResponseImagesItem = TypedDict(
    "ModelsPredictResponseImagesItem",
    {
        "shape": list[float],
        "speed": ModelsPredictResponseImagesItemSpeed,
        "results": list[ModelsPredictResponseImagesItemResultsItem],
        "semantic_mask": NotRequired[ModelsPredictResponseImagesItemSemanticMask],
        "depth": NotRequired[ModelsPredictResponseImagesItemDepth],
    },
)


ModelsPredictResponseMetadata = TypedDict(
    "ModelsPredictResponseMetadata",
    {
        "imageCount": int,
        "functionTimeAlive": float,
        "functionTimeCall": float,
        "model": NotRequired[str],
        "task": NotRequired[Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"] | None],
        "version": dict[str, str],
    },
)


ModelsPredictResponse = TypedDict(
    "ModelsPredictResponse",
    {"images": list[ModelsPredictResponseImagesItem], "metadata": ModelsPredictResponseMetadata},
)


ModelsTrainingResponseJobProgress = TypedDict(
    "ModelsTrainingResponseJobProgress",
    {
        "currentEpoch": float,
        "totalEpochs": float,
        "startedAt": NotRequired[str],
        "completedAt": NotRequired[str],
        "percentage": float,
    },
)


ModelsTrainingResponseJobTiming = TypedDict(
    "ModelsTrainingResponseJobTiming", {"elapsedMs": float, "timePerEpochMs": float, "etaMs": float}
)


ModelsTrainingResponseJobCompute = TypedDict(
    "ModelsTrainingResponseJobCompute", {"gpuType": str, "gpuDisplayName": str, "gpuMemoryGb": float}
)


ModelsTrainingResponseJobTrainArgs = TypedDict(
    "ModelsTrainingResponseJobTrainArgs",
    {"model": NotRequired[str], "epochs": NotRequired[float], "batch": NotRequired[float], "imgsz": NotRequired[float]},
)


ModelsTrainingResponseJobError = TypedDict(
    "ModelsTrainingResponseJobError", {"message": str, "code": NotRequired[str], "timestamp": str}
)


ModelsTrainingResponseJob = TypedDict(
    "ModelsTrainingResponseJob",
    {
        "id": str,
        "status": Literal["pending", "untrained", "starting", "running", "completed", "failed", "cancelled"],
        "progress": ModelsTrainingResponseJobProgress,
        "timing": ModelsTrainingResponseJobTiming,
        "compute": ModelsTrainingResponseJobCompute | None,
        "trainArgs": ModelsTrainingResponseJobTrainArgs | None,
        "epochMetrics": dict[str, Any] | None,
        "error": ModelsTrainingResponseJobError | None,
        "createdAt": str,
        "updatedAt": str,
    },
)


ModelsTrainingResponse = TypedDict("ModelsTrainingResponse", {"job": ModelsTrainingResponseJob | None})


ModelsDeleteTrainingResponse = TypedDict(
    "ModelsDeleteTrainingResponse",
    {"success": Literal[True], "status": Literal["cancelled"], "warning": NotRequired[str]},
)


ModelsListResponseModelsItemDatasetVersion = TypedDict(
    "ModelsListResponseModelsItemDatasetVersion", {"version": int, "contentHash": str}
)


ModelsListResponseModelsItemSourceModel = TypedDict(
    "ModelsListResponseModelsItemSourceModel",
    {
        "owner": str,
        "project": str,
        "projectName": str,
        "projectIconColor": NotRequired[str],
        "projectIconLetter": NotRequired[str],
        "projectIconImage": NotRequired[str],
        "model": str,
        "modelName": str,
    },
)


ModelsListResponseModelsItemTrainResultsItem = TypedDict(
    "ModelsListResponseModelsItemTrainResultsItem",
    {
        "epoch": NotRequired[int],
        "metrics": NotRequired[dict[str, float]],
        "fitness": NotRequired[float],
        "timestamp": NotRequired[str],
    },
)


ModelsListResponseModelsItemFile = TypedDict("ModelsListResponseModelsItemFile", {"size": float})


ModelsListResponseModelsItemTrainingError = TypedDict(
    "ModelsListResponseModelsItemTrainingError", {"message": str, "code": NotRequired[str], "timestamp": str}
)


ModelsListResponseModelsItemComputeCost = TypedDict(
    "ModelsListResponseModelsItemComputeCost",
    {
        "gpuType": NotRequired[str],
        "gpuDisplayName": NotRequired[str],
        "pricePerHour": float,
        "totalCost": float,
        "durationMs": NotRequired[float],
    },
)


ModelsListResponseModelsItemCloudJob = TypedDict("ModelsListResponseModelsItemCloudJob", {"gpuDisplayName": str})


ModelsListResponseModelsItemConsoleChunksItem = TypedDict(
    "ModelsListResponseModelsItemConsoleChunksItem",
    {"chunkId": float, "content": str, "lineCount": float, "timestamp": str},
)


ModelsListResponseModelsItem = TypedDict(
    "ModelsListResponseModelsItem",
    {
        "id": str,
        "owner": str,
        "project": str,
        "projectName": str,
        "projectIconColor": NotRequired[str],
        "projectIconLetter": NotRequired[str],
        "projectIconImage": NotRequired[str],
        "model": str,
        "visibility": Literal["public", "private"],
        "name": str,
        "description": NotRequired[str],
        "license": NotRequired[
            Literal[
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
        ],
        "status": NotRequired[
            Literal["pending", "untrained", "starting", "running", "completed", "failed", "cancelled"]
        ],
        "task": NotRequired[Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"]],
        "depthScaleVerified": NotRequired[bool],
        "color": NotRequired[str],
        "datasetId": NotRequired[str],
        "datasetVersion": NotRequired[ModelsListResponseModelsItemDatasetVersion],
        "sourceModelId": NotRequired[str],
        "sourceModel": NotRequired[ModelsListResponseModelsItemSourceModel],
        "baseModel": NotRequired[str],
        "epochs": NotRequired[int],
        "bestEpoch": NotRequired[int | None],
        "bestFitness": NotRequired[float | None],
        "trainArgs": NotRequired[dict[str, Any]],
        "metrics": NotRequired[dict[str, float]],
        "trainResults": NotRequired[list[ModelsListResponseModelsItemTrainResultsItem]],
        "hasWeights": bool,
        "file": NotRequired[ModelsListResponseModelsItemFile],
        "version": NotRequired[str],
        "docs": NotRequired[str],
        "startedAt": NotRequired[str],
        "completedAt": NotRequired[str],
        "classNames": NotRequired[list[str]],
        "plots": NotRequired[list[Any]],
        "trainingError": NotRequired[ModelsListResponseModelsItemTrainingError],
        "starCount": int,
        "isStarred": bool,
        "clonedFrom": NotRequired[str],
        "cloneCount": NotRequired[int],
        "environment": NotRequired[dict[str, Any]],
        "computeCost": NotRequired[ModelsListResponseModelsItemComputeCost],
        "cloudJob": NotRequired[ModelsListResponseModelsItemCloudJob],
        "consoleChunks": NotRequired[list[ModelsListResponseModelsItemConsoleChunksItem]],
        "createdAt": str,
        "updatedAt": str,
    },
)


ModelsListResponse = TypedDict(
    "ModelsListResponse", {"models": list[ModelsListResponseModelsItem], "region": Literal["us", "eu", "ap"]}
)


ModelsCreateResponse = TypedDict(
    "ModelsCreateResponse", {"id": str, "owner": str, "project": str, "model": str, "region": Literal["us", "eu", "ap"]}
)


ExportsRetrieveResponseExportFile = TypedDict(
    "ExportsRetrieveResponseExportFile",
    {"size": NotRequired[float], "downloadUrl": NotRequired[str], "downloadFilename": NotRequired[str]},
)


ExportsRetrieveResponseExportError = TypedDict("ExportsRetrieveResponseExportError", {"message": str, "timestamp": str})


ExportsRetrieveResponseExport = TypedDict(
    "ExportsRetrieveResponseExport",
    {
        "id": str,
        "status": Literal["queued", "starting", "running", "completed", "failed", "cancelled"],
        "format": Literal[
            "onnx",
            "torchscript",
            "openvino",
            "engine",
            "coreml",
            "litert",
            "pb",
            "saved_model",
            "paddle",
            "ncnn",
            "edgetpu",
            "mnn",
            "rknn",
            "qnn",
            "imx",
            "axelera",
            "executorch",
            "deepx",
            "hailo",
            "ascend",
        ],
        "args": NotRequired[dict[str, Any]],
        "gpuType": NotRequired[str],
        "file": NotRequired[ExportsRetrieveResponseExportFile],
        "error": NotRequired[ExportsRetrieveResponseExportError],
        "startedAt": NotRequired[str],
        "completedAt": NotRequired[str],
        "createdAt": str,
        "updatedAt": str,
    },
)


ExportsRetrieveResponse = TypedDict("ExportsRetrieveResponse", {"export": ExportsRetrieveResponseExport})


ExportsDeleteResponse = TypedDict(
    "ExportsDeleteResponse", {"success": Literal[True], "action": Literal["cancelled", "deleted"]}
)


ExportsListResponse = TypedDict(
    "ExportsListResponse", {"exports": list[ExportsRetrieveResponseExport], "region": Literal["us", "eu", "ap"]}
)


ExportsCreateResponse = TypedDict(
    "ExportsCreateResponse",
    {
        "id": str,
        "format": Literal[
            "onnx",
            "torchscript",
            "openvino",
            "engine",
            "coreml",
            "litert",
            "pb",
            "saved_model",
            "paddle",
            "ncnn",
            "edgetpu",
            "mnn",
            "rknn",
            "qnn",
            "imx",
            "axelera",
            "executorch",
            "deepx",
            "hailo",
            "ascend",
        ],
        "status": Literal["queued", "running"],
        "gpuType": NotRequired[str],
        "region": Literal["us", "eu", "ap"],
    },
)


ProjectsCloneResponse = TypedDict(
    "ProjectsCloneResponse",
    {"id": str, "owner": str, "project": str, "name": str, "modelCount": int, "region": Literal["us", "eu", "ap"]},
)


ProjectsRetrieveResponseProjectViewPreferences = TypedDict(
    "ProjectsRetrieveResponseProjectViewPreferences",
    {
        "sortBy": NotRequired[Literal["newest", "oldest", "name-asc", "name-desc", "size-asc", "size-desc"]],
        "groupBy": NotRequired[Literal["none", "task"]],
        "statusFilter": NotRequired[Literal["all", "completed", "untrained", "running", "starting", "failed"]],
    },
)


ProjectsRetrieveResponseProject = TypedDict(
    "ProjectsRetrieveResponseProject",
    {
        "id": str,
        "owner": str,
        "project": str,
        "name": str,
        "description": NotRequired[str],
        "visibility": Literal["public", "private"],
        "tags": NotRequired[list[str]],
        "license": NotRequired[
            Literal[
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
        ],
        "iconColor": NotRequired[str],
        "iconLetter": NotRequired[str],
        "iconImage": NotRequired[str],
        "modelCount": int,
        "modelNames": NotRequired[list[str]],
        "totalBytes": NotRequired[float],
        "starCount": int,
        "isStarred": bool,
        "archived": NotRequired[bool],
        "region": NotRequired[Literal["us", "eu", "ap"]],
        "task": NotRequired[Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"]],
        "clonedFrom": NotRequired[str],
        "cloneCount": NotRequired[int],
        "viewPreferences": NotRequired[ProjectsRetrieveResponseProjectViewPreferences],
        "createdAt": str,
        "updatedAt": str,
        "metadata": dict[str, Any],
    },
)


ProjectsRetrieveResponseModelsItemFile = TypedDict("ProjectsRetrieveResponseModelsItemFile", {"size": float})


ProjectsRetrieveResponseModelsItem = TypedDict(
    "ProjectsRetrieveResponseModelsItem",
    {
        "id": str,
        "model": str,
        "name": str,
        "color": NotRequired[str],
        "task": NotRequired[Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"]],
        "status": NotRequired[
            Literal["pending", "untrained", "starting", "running", "completed", "failed", "cancelled"]
        ],
        "epochs": NotRequired[int],
        "bestEpoch": NotRequired[int | None],
        "bestFitness": NotRequired[float | None],
        "metrics": NotRequired[dict[str, float]],
        "epochCount": int,
        "startedAt": NotRequired[str],
        "file": NotRequired[ProjectsRetrieveResponseModelsItemFile],
        "hasWeights": bool,
        "trainArgs": NotRequired[dict[str, Any]],
        "createdAt": str,
        "updatedAt": str,
    },
)


ProjectsRetrieveResponse = TypedDict(
    "ProjectsRetrieveResponse",
    {"project": ProjectsRetrieveResponseProject, "models": list[ProjectsRetrieveResponseModelsItem], "isOwner": bool},
)


ProjectsUpdateResponseVariant1 = TypedDict("ProjectsUpdateResponseVariant1", {"success": Literal[True], "project": str})


ProjectsUpdateResponseVariant2 = TypedDict("ProjectsUpdateResponseVariant2", {"starred": bool, "starCount": int})


ProjectsUpdateResponse = ProjectsUpdateResponseVariant1 | ProjectsUpdateResponseVariant2


ProjectsDeleteResponse = TypedDict("ProjectsDeleteResponse", {"success": Literal[True], "cascadedModels": int})


ProjectsListResponseProjectsItemViewPreferences = TypedDict(
    "ProjectsListResponseProjectsItemViewPreferences",
    {
        "sortBy": NotRequired[Literal["newest", "oldest", "name-asc", "name-desc", "size-asc", "size-desc"]],
        "groupBy": NotRequired[Literal["none", "task"]],
        "statusFilter": NotRequired[Literal["all", "completed", "untrained", "running", "starting", "failed"]],
    },
)


ProjectsListResponseProjectsItem = TypedDict(
    "ProjectsListResponseProjectsItem",
    {
        "id": str,
        "owner": str,
        "project": str,
        "name": str,
        "description": NotRequired[str],
        "visibility": Literal["public", "private"],
        "tags": NotRequired[list[str]],
        "license": NotRequired[
            Literal[
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
        ],
        "iconColor": NotRequired[str],
        "iconLetter": NotRequired[str],
        "iconImage": NotRequired[str],
        "modelCount": int,
        "modelNames": NotRequired[list[str]],
        "totalBytes": NotRequired[float],
        "starCount": int,
        "isStarred": bool,
        "archived": NotRequired[bool],
        "region": NotRequired[Literal["us", "eu", "ap"]],
        "task": NotRequired[Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"]],
        "clonedFrom": NotRequired[str],
        "cloneCount": NotRequired[int],
        "viewPreferences": NotRequired[ProjectsListResponseProjectsItemViewPreferences],
        "createdAt": str,
        "updatedAt": str,
    },
)


ProjectsListResponse = TypedDict(
    "ProjectsListResponse",
    {"projects": list[ProjectsListResponseProjectsItem], "total": int, "region": Literal["us", "eu", "ap"]},
)


ProjectsCreateResponse = TypedDict(
    "ProjectsCreateResponse", {"id": str, "owner": str, "project": str, "region": Literal["us", "eu", "ap"]}
)


TrainingGpuAvailabilityResponse = dict[str, Literal["High", "Medium", "Low"] | None]


TrainingStartResponseEstimatedCost = TypedDict(
    "TrainingStartResponseEstimatedCost", {"pricePerHour": float, "gpuMemoryGb": float}
)


TrainingStartResponseBilling = TypedDict(
    "TrainingStartResponseBilling", {"estimatedCostCents": float, "estimatedCostDisplay": str, "balanceCents": float}
)


TrainingStartResponse = TypedDict(
    "TrainingStartResponse",
    {
        "modelId": str,
        "status": Literal["starting"],
        "gpuType": str,
        "estimatedCost": TrainingStartResponseEstimatedCost,
        "billing": TrainingStartResponseBilling,
    },
)


LifecycleTrashResponseItemsItemParentProject = TypedDict(
    "LifecycleTrashResponseItemsItemParentProject", {"_id": str, "name": str, "slug": str}
)


LifecycleTrashResponseItemsItem = TypedDict(
    "LifecycleTrashResponseItemsItem",
    {
        "_id": str,
        "type": Literal["project", "dataset", "model"],
        "name": str,
        "slug": str,
        "trashedAt": str,
        "daysRemaining": int,
        "cascadedCount": NotRequired[int],
        "parentProject": NotRequired[LifecycleTrashResponseItemsItemParentProject],
        "sizeBytes": NotRequired[float],
    },
)


LifecycleTrashResponseSummaryByTypeProjects = TypedDict("LifecycleTrashResponseSummaryByTypeProjects", {"count": int})


LifecycleTrashResponseSummaryByTypeDatasets = TypedDict(
    "LifecycleTrashResponseSummaryByTypeDatasets", {"count": int, "sizeBytes": float}
)


LifecycleTrashResponseSummaryByTypeModels = TypedDict(
    "LifecycleTrashResponseSummaryByTypeModels", {"count": int, "sizeBytes": float}
)


LifecycleTrashResponseSummaryByTypeExports = TypedDict(
    "LifecycleTrashResponseSummaryByTypeExports", {"count": int, "sizeBytes": float}
)


LifecycleTrashResponseSummaryByType = TypedDict(
    "LifecycleTrashResponseSummaryByType",
    {
        "projects": LifecycleTrashResponseSummaryByTypeProjects,
        "datasets": LifecycleTrashResponseSummaryByTypeDatasets,
        "models": LifecycleTrashResponseSummaryByTypeModels,
        "exports": LifecycleTrashResponseSummaryByTypeExports,
    },
)


LifecycleTrashResponseSummary = TypedDict(
    "LifecycleTrashResponseSummary",
    {"totalItems": int, "totalSizeBytes": float, "byType": LifecycleTrashResponseSummaryByType},
)


LifecycleTrashResponse = TypedDict(
    "LifecycleTrashResponse",
    {
        "items": list[LifecycleTrashResponseItemsItem],
        "total": int,
        "page": int,
        "limit": int,
        "totalPages": int,
        "summary": LifecycleTrashResponseSummary,
        "region": Literal["us", "eu", "ap"],
    },
)


LifecycleRestoreResponse = TypedDict(
    "LifecycleRestoreResponse", {"success": Literal[True], "restoredModels": NotRequired[int]}
)


LifecycleDeleteTrashResponse = TypedDict(
    "LifecycleDeleteTrashResponse",
    {
        "success": Literal[True],
        "deletedCount": int,
        "cascadedModels": NotRequired[int],
        "survivingDeployments": NotRequired[int],
    },
)


UploadCompleteResponseFile = TypedDict("UploadCompleteResponseFile", {"size": float, "contentType": NotRequired[str]})


UploadCompleteResponse = TypedDict(
    "UploadCompleteResponse", {"success": Literal[True], "file": UploadCompleteResponseFile}
)


UploadSignedUrlResponse = TypedDict(
    "UploadSignedUrlResponse",
    {"sessionId": str, "uploadUrl": str, "expiresAt": str, "headers": NotRequired[dict[str, str]]},
)
