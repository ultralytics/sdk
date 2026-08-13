# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from __future__ import annotations

from typing import Any, Literal, NotRequired, TypedDict

AccountRetrieveSummaryResponseCounts = TypedDict(
    "AccountRetrieveSummaryResponseCounts", {"projects": int, "datasets": int, "models": int}
)


AccountRetrieveSummaryResponseTeamsItem = TypedDict(
    "AccountRetrieveSummaryResponseTeamsItem",
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


AccountRetrieveSummaryResponse = TypedDict(
    "AccountRetrieveSummaryResponse",
    {
        "username": str,
        "name": str,
        "accountType": Literal["personal", "team"],
        "plan": Literal["free", "pro", "enterprise"],
        "creditsCents": int,
        "counts": AccountRetrieveSummaryResponseCounts,
        "teams": list[AccountRetrieveSummaryResponseTeamsItem],
    },
)


AccountListApiKeysResponseKeysItem = TypedDict(
    "AccountListApiKeysResponseKeysItem",
    {
        "keyId": str,
        "name": str,
        "keyPrefix": str,
        "lastUsedAt": NotRequired[str],
        "usageCount": float,
        "createdAt": str,
    },
)


AccountListApiKeysResponse = TypedDict("AccountListApiKeysResponse", {"keys": list[AccountListApiKeysResponseKeysItem]})


AccountRetrieveStorageUsageResponseUsageProjects = TypedDict(
    "AccountRetrieveStorageUsageResponseUsageProjects", {"current": float, "limit": float, "percent": float}
)


AccountRetrieveStorageUsageResponseUsageDatasets = TypedDict(
    "AccountRetrieveStorageUsageResponseUsageDatasets", {"current": float, "limit": float, "percent": float}
)


AccountRetrieveStorageUsageResponseUsageModels = TypedDict(
    "AccountRetrieveStorageUsageResponseUsageModels", {"current": float, "limit": float, "percent": float}
)


AccountRetrieveStorageUsageResponseUsageImages = TypedDict(
    "AccountRetrieveStorageUsageResponseUsageImages", {"current": float, "limit": float, "percent": float}
)


AccountRetrieveStorageUsageResponseUsageAnnotations = TypedDict(
    "AccountRetrieveStorageUsageResponseUsageAnnotations", {"current": float}
)


AccountRetrieveStorageUsageResponseUsageDeployments = TypedDict(
    "AccountRetrieveStorageUsageResponseUsageDeployments", {"current": float, "limit": float, "percent": float}
)


AccountRetrieveStorageUsageResponseUsageStorage = TypedDict(
    "AccountRetrieveStorageUsageResponseUsageStorage", {"current": float, "limit": float, "percent": float}
)


AccountRetrieveStorageUsageResponseUsage = TypedDict(
    "AccountRetrieveStorageUsageResponseUsage",
    {
        "projects": NotRequired[AccountRetrieveStorageUsageResponseUsageProjects],
        "datasets": NotRequired[AccountRetrieveStorageUsageResponseUsageDatasets],
        "models": NotRequired[AccountRetrieveStorageUsageResponseUsageModels],
        "images": NotRequired[AccountRetrieveStorageUsageResponseUsageImages],
        "annotations": NotRequired[AccountRetrieveStorageUsageResponseUsageAnnotations],
        "deployments": NotRequired[AccountRetrieveStorageUsageResponseUsageDeployments],
        "storage": AccountRetrieveStorageUsageResponseUsageStorage,
    },
)


AccountRetrieveStorageUsageResponseBreakdownByCategoryDatasets = TypedDict(
    "AccountRetrieveStorageUsageResponseBreakdownByCategoryDatasets", {"bytes": float, "count": float}
)


AccountRetrieveStorageUsageResponseBreakdownByCategoryModels = TypedDict(
    "AccountRetrieveStorageUsageResponseBreakdownByCategoryModels", {"bytes": float, "count": float}
)


AccountRetrieveStorageUsageResponseBreakdownByCategoryExports = TypedDict(
    "AccountRetrieveStorageUsageResponseBreakdownByCategoryExports", {"bytes": float, "count": float}
)


AccountRetrieveStorageUsageResponseBreakdownByCategory = TypedDict(
    "AccountRetrieveStorageUsageResponseBreakdownByCategory",
    {
        "datasets": AccountRetrieveStorageUsageResponseBreakdownByCategoryDatasets,
        "models": AccountRetrieveStorageUsageResponseBreakdownByCategoryModels,
        "exports": AccountRetrieveStorageUsageResponseBreakdownByCategoryExports,
    },
)


AccountRetrieveStorageUsageResponseBreakdownTopItemsItem = TypedDict(
    "AccountRetrieveStorageUsageResponseBreakdownTopItemsItem",
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


AccountRetrieveStorageUsageResponseBreakdown = TypedDict(
    "AccountRetrieveStorageUsageResponseBreakdown",
    {
        "byCategory": AccountRetrieveStorageUsageResponseBreakdownByCategory,
        "topItems": list[AccountRetrieveStorageUsageResponseBreakdownTopItemsItem],
    },
)


AccountRetrieveStorageUsageResponse = TypedDict(
    "AccountRetrieveStorageUsageResponse",
    {
        "tier": Literal["free", "pro", "enterprise"],
        "usage": AccountRetrieveStorageUsageResponseUsage,
        "updatedAt": str | None,
        "breakdown": AccountRetrieveStorageUsageResponseBreakdown,
        "region": Literal["us", "eu", "ap"],
        "username": str,
    },
)


AccountRetrievePublicUserProfileResponseUserSocials = TypedDict(
    "AccountRetrievePublicUserProfileResponseUserSocials",
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


AccountRetrievePublicUserProfileResponseUser = TypedDict(
    "AccountRetrievePublicUserProfileResponseUser",
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
        "socials": NotRequired[AccountRetrievePublicUserProfileResponseUserSocials],
        "followerCount": int,
        "isFollowed": bool,
    },
)


AccountRetrievePublicUserProfileResponse = TypedDict(
    "AccountRetrievePublicUserProfileResponse", {"user": AccountRetrievePublicUserProfileResponseUser}
)


AccountFollowUserResponse = TypedDict("AccountFollowUserResponse", {"followed": bool, "followerCount": int})


BillingListTransactionsResponseTransactionsItemModel = TypedDict(
    "BillingListTransactionsResponseTransactionsItemModel",
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


BillingListTransactionsResponseTransactionsItem = TypedDict(
    "BillingListTransactionsResponseTransactionsItem",
    {
        "id": str,
        "type": Literal[
            "signup",
            "purchase",
            "subscription",
            "monthly_grant",
            "training",
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
        "model": NotRequired[BillingListTransactionsResponseTransactionsItemModel | None],
    },
)


BillingListTransactionsResponse = TypedDict(
    "BillingListTransactionsResponse", {"transactions": list[BillingListTransactionsResponseTransactionsItem]}
)


BillingListUsageSummaryResponsePlan = TypedDict(
    "BillingListUsageSummaryResponsePlan",
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


BillingListUsageSummaryResponseMetricsItem = TypedDict(
    "BillingListUsageSummaryResponseMetricsItem",
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


BillingListUsageSummaryResponseTrainingCredit = TypedDict(
    "BillingListUsageSummaryResponseTrainingCredit", {"monthlyGrant": float, "balanceAvailable": float}
)


BillingListUsageSummaryResponseFeatures = TypedDict(
    "BillingListUsageSummaryResponseFeatures", {"privateProjects": bool, "teams": bool, "enterpriseLicense": bool}
)


BillingListUsageSummaryResponse = TypedDict(
    "BillingListUsageSummaryResponse",
    {
        "plan": BillingListUsageSummaryResponsePlan,
        "metrics": list[BillingListUsageSummaryResponseMetricsItem],
        "trainingCredit": BillingListUsageSummaryResponseTrainingCredit,
        "features": BillingListUsageSummaryResponseFeatures,
        "creditsCents": float,
        "paidSeats": NotRequired[float],
        "currentSeats": NotRequired[float],
        "maxSeats": NotRequired[float],
        "nextInvoiceCents": NotRequired[float],
    },
)


DatasetsRetrieveClassStatsResponseClassesItem = TypedDict(
    "DatasetsRetrieveClassStatsResponseClassesItem", {"classId": float, "count": float, "imageCount": float}
)


DatasetsRetrieveClassStatsResponseImageStatsWidthHistogramItem = TypedDict(
    "DatasetsRetrieveClassStatsResponseImageStatsWidthHistogramItem",
    {"bin": float, "count": float, "size": NotRequired[float]},
)


DatasetsRetrieveClassStatsResponseImageStatsHeightHistogramItem = TypedDict(
    "DatasetsRetrieveClassStatsResponseImageStatsHeightHistogramItem",
    {"bin": float, "count": float, "size": NotRequired[float]},
)


DatasetsRetrieveClassStatsResponseImageStatsPointsHistogramItem = TypedDict(
    "DatasetsRetrieveClassStatsResponseImageStatsPointsHistogramItem",
    {"bin": float, "count": float, "size": NotRequired[float]},
)


DatasetsRetrieveClassStatsResponseImageStatsFileSizeHistogramItem = TypedDict(
    "DatasetsRetrieveClassStatsResponseImageStatsFileSizeHistogramItem",
    {"bin": float, "count": float, "size": NotRequired[float]},
)


DatasetsRetrieveClassStatsResponseImageStatsObjectsPerImageHistogramItem = TypedDict(
    "DatasetsRetrieveClassStatsResponseImageStatsObjectsPerImageHistogramItem",
    {"bin": float, "count": float, "size": NotRequired[float]},
)


DatasetsRetrieveClassStatsResponseImageStatsBboxWidthHistogramItem = TypedDict(
    "DatasetsRetrieveClassStatsResponseImageStatsBboxWidthHistogramItem",
    {"bin": float, "count": float, "size": NotRequired[float]},
)


DatasetsRetrieveClassStatsResponseImageStatsBboxHeightHistogramItem = TypedDict(
    "DatasetsRetrieveClassStatsResponseImageStatsBboxHeightHistogramItem",
    {"bin": float, "count": float, "size": NotRequired[float]},
)


DatasetsRetrieveClassStatsResponseImageStatsBboxWidthNormHistogramItem = TypedDict(
    "DatasetsRetrieveClassStatsResponseImageStatsBboxWidthNormHistogramItem",
    {"bin": float, "count": float, "size": NotRequired[float]},
)


DatasetsRetrieveClassStatsResponseImageStatsBboxHeightNormHistogramItem = TypedDict(
    "DatasetsRetrieveClassStatsResponseImageStatsBboxHeightNormHistogramItem",
    {"bin": float, "count": float, "size": NotRequired[float]},
)


DatasetsRetrieveClassStatsResponseImageStats = TypedDict(
    "DatasetsRetrieveClassStatsResponseImageStats",
    {
        "widthHistogram": list[DatasetsRetrieveClassStatsResponseImageStatsWidthHistogramItem],
        "heightHistogram": list[DatasetsRetrieveClassStatsResponseImageStatsHeightHistogramItem],
        "pointsHistogram": list[DatasetsRetrieveClassStatsResponseImageStatsPointsHistogramItem],
        "formatDistribution": dict[str, float],
        "fileSizeHistogram": list[DatasetsRetrieveClassStatsResponseImageStatsFileSizeHistogramItem],
        "objectsPerImageHistogram": list[DatasetsRetrieveClassStatsResponseImageStatsObjectsPerImageHistogramItem],
        "bboxWidthHistogram": list[DatasetsRetrieveClassStatsResponseImageStatsBboxWidthHistogramItem],
        "bboxHeightHistogram": list[DatasetsRetrieveClassStatsResponseImageStatsBboxHeightHistogramItem],
        "bboxWidthNormHistogram": list[DatasetsRetrieveClassStatsResponseImageStatsBboxWidthNormHistogramItem],
        "bboxHeightNormHistogram": list[DatasetsRetrieveClassStatsResponseImageStatsBboxHeightNormHistogramItem],
    },
)


DatasetsRetrieveClassStatsResponseLocationHeatmap = TypedDict(
    "DatasetsRetrieveClassStatsResponseLocationHeatmap", {"bins": list[list[float]], "maxCount": float}
)


DatasetsRetrieveClassStatsResponseDimensionHeatmap = TypedDict(
    "DatasetsRetrieveClassStatsResponseDimensionHeatmap",
    {
        "bins": list[list[float]],
        "maxCount": float,
        "minWidth": float,
        "maxWidth": float,
        "minHeight": float,
        "maxHeight": float,
    },
)


DatasetsRetrieveClassStatsResponse = TypedDict(
    "DatasetsRetrieveClassStatsResponse",
    {
        "classes": list[DatasetsRetrieveClassStatsResponseClassesItem],
        "imageStats": DatasetsRetrieveClassStatsResponseImageStats,
        "locationHeatmap": DatasetsRetrieveClassStatsResponseLocationHeatmap,
        "dimensionHeatmap": DatasetsRetrieveClassStatsResponseDimensionHeatmap,
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
    "DatasetsRetrieveResponseDatasetLastIngestSummary", {"added": int, "errors": int, "skippedCounts": dict[str, int]}
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
        "imageCount": int,
        "classCount": NotRequired[int],
        "classNames": NotRequired[list[str]],
        "format": NotRequired[Literal["yolo", "coco", "voc", "raw", "ndjson"]],
        "tags": NotRequired[list[str]],
        "license": NotRequired[
            Literal[
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


DatasetsRetrieveEmbeddingsResponseActiveJobProgress = TypedDict(
    "DatasetsRetrieveEmbeddingsResponseActiveJobProgress",
    {
        "stage": Literal["embedding", "umap"],
        "percent": float,
        "processed": NotRequired[float],
        "total": NotRequired[float],
        "failedDownloads": NotRequired[float],
        "failedInference": NotRequired[float],
    },
)


DatasetsRetrieveEmbeddingsResponseActiveJob = TypedDict(
    "DatasetsRetrieveEmbeddingsResponseActiveJob",
    {
        "id": str,
        "status": Literal["queued", "starting", "running"],
        "progress": DatasetsRetrieveEmbeddingsResponseActiveJobProgress | None,
        "createdAt": str,
    },
)


DatasetsRetrieveEmbeddingsResponse = TypedDict(
    "DatasetsRetrieveEmbeddingsResponse",
    {
        "analyzedAt": str | None,
        "embeddingsCount": int,
        "latestImageAt": str | None,
        "activeJob": DatasetsRetrieveEmbeddingsResponseActiveJob | None,
    },
)


DatasetsCreateEmbeddingsResponse = TypedDict("DatasetsCreateEmbeddingsResponse", {"jobId": str})


DatasetsDeleteEmbeddingsResponse = TypedDict("DatasetsDeleteEmbeddingsResponse", {"cancelled": str | None})


DatasetsRetrieveExportResponseVariant1 = TypedDict(
    "DatasetsRetrieveExportResponseVariant1", {"downloadUrl": str, "version": int}
)


DatasetsRetrieveExportResponseVariant2 = TypedDict(
    "DatasetsRetrieveExportResponseVariant2", {"downloadUrl": str, "cached": bool}
)


DatasetsRetrieveExportResponse = DatasetsRetrieveExportResponseVariant1 | DatasetsRetrieveExportResponseVariant2


DatasetsCreateExportResponse = TypedDict(
    "DatasetsCreateExportResponse", {"version": int, "downloadUrl": str, "reused": bool}
)


DatasetsUpdateExportResponse = TypedDict("DatasetsUpdateExportResponse", {"ok": Literal[True]})


DatasetsRetrieveImagesClusteringResponseImagesItem = TypedDict(
    "DatasetsRetrieveImagesClusteringResponseImagesItem",
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
        "missing": bool,
    },
)


DatasetsRetrieveImagesClusteringResponse = TypedDict(
    "DatasetsRetrieveImagesClusteringResponse",
    {
        "images": list[DatasetsRetrieveImagesClusteringResponseImagesItem],
        "total": int,
        "offset": int,
        "limit": int,
        "hasMore": bool,
        "nextOffset": int | None,
        "updatedAt": str,
    },
)


DatasetsListImagesResponseImagesItemLabelsItem = TypedDict(
    "DatasetsListImagesResponseImagesItemLabelsItem",
    {
        "classId": int,
        "bbox": NotRequired[list[Any]],
        "segments": NotRequired[list[float]],
        "keypoints": NotRequired[list[float]],
        "obb": NotRequired[list[Any]],
        "skeletonId": NotRequired[str],
    },
)


DatasetsListImagesResponseImagesItem = TypedDict(
    "DatasetsListImagesResponseImagesItem",
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
        "labels": NotRequired[list[DatasetsListImagesResponseImagesItemLabelsItem]],
        "labelsTruncated": NotRequired[Literal[True]],
    },
)


DatasetsListImagesResponse = TypedDict(
    "DatasetsListImagesResponse",
    {
        "images": list[DatasetsListImagesResponseImagesItem],
        "total": NotRequired[int],
        "hasMore": bool,
        "classes": list[str],
        "errorCount": int,
        "nextCursor": NotRequired[str],
    },
)


DatasetsRetrieveSelectedImagesResponseImagesItemLabelsItem = TypedDict(
    "DatasetsRetrieveSelectedImagesResponseImagesItemLabelsItem",
    {
        "classId": int,
        "bbox": NotRequired[list[Any]],
        "segments": NotRequired[list[float]],
        "keypoints": NotRequired[list[float]],
        "obb": NotRequired[list[Any]],
        "skeletonId": NotRequired[str],
    },
)


DatasetsRetrieveSelectedImagesResponseImagesItem = TypedDict(
    "DatasetsRetrieveSelectedImagesResponseImagesItem",
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
        "labels": NotRequired[list[DatasetsRetrieveSelectedImagesResponseImagesItemLabelsItem]],
        "labelsTruncated": NotRequired[Literal[True]],
    },
)


DatasetsRetrieveSelectedImagesResponse = TypedDict(
    "DatasetsRetrieveSelectedImagesResponse",
    {
        "images": list[DatasetsRetrieveSelectedImagesResponseImagesItem],
        "total": int,
        "hasMore": Literal[False],
        "classes": list[str],
        "errorCount": int,
        "nextCursor": NotRequired[Any],
    },
)


DatasetsIngestResponse = TypedDict("DatasetsIngestResponse", {"jobId": str, "status": Literal["queued"]})


DatasetsListModelsResponseModelsItemDatasetVersion = TypedDict(
    "DatasetsListModelsResponseModelsItemDatasetVersion", {"version": int, "contentHash": str}
)


DatasetsListModelsResponseModelsItem = TypedDict(
    "DatasetsListModelsResponseModelsItem",
    {
        "id": str,
        "owner": str,
        "project": str,
        "model": str,
        "name": str,
        "status": Literal["pending", "untrained", "starting", "running", "completed", "failed", "cancelled"],
        "task": NotRequired[Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"]],
        "datasetVersion": NotRequired[DatasetsListModelsResponseModelsItemDatasetVersion],
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


DatasetsListModelsResponse = TypedDict(
    "DatasetsListModelsResponse", {"models": list[DatasetsListModelsResponseModelsItem], "count": int}
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
    "DatasetsListResponseDatasetsItemLastIngestSummary", {"added": int, "errors": int, "skippedCounts": dict[str, int]}
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
        "imageCount": int,
        "classCount": NotRequired[int],
        "classNames": NotRequired[list[str]],
        "format": NotRequired[Literal["yolo", "coco", "voc", "raw", "ndjson"]],
        "tags": NotRequired[list[str]],
        "license": NotRequired[
            Literal[
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


DatasetsImportFromRoboflowResponseImportedItem = TypedDict(
    "DatasetsImportFromRoboflowResponseImportedItem",
    {"projectId": str, "projectName": str, "version": int, "datasetId": str, "slug": str},
)


DatasetsImportFromRoboflowResponseFailedItem = TypedDict(
    "DatasetsImportFromRoboflowResponseFailedItem", {"projectId": str, "projectName": str, "version": int, "error": str}
)


DatasetsImportFromRoboflowResponseSkippedItem = TypedDict(
    "DatasetsImportFromRoboflowResponseSkippedItem", {"projectId": str, "projectName": str, "version": int}
)


DatasetsImportFromRoboflowResponse = TypedDict(
    "DatasetsImportFromRoboflowResponse",
    {
        "imported": list[DatasetsImportFromRoboflowResponseImportedItem],
        "failed": list[DatasetsImportFromRoboflowResponseFailedItem],
        "skipped": list[DatasetsImportFromRoboflowResponseSkippedItem],
    },
)


DatasetsPreviewRoboflowImportResponseWorkspace = TypedDict(
    "DatasetsPreviewRoboflowImportResponseWorkspace", {"url": str, "name": str}
)


DatasetsPreviewRoboflowImportResponseNewDatasetsItem = TypedDict(
    "DatasetsPreviewRoboflowImportResponseNewDatasetsItem",
    {
        "workspace": str,
        "projectId": str,
        "projectName": str,
        "projectType": str,
        "latestVersion": int,
        "latestVersionName": NotRequired[str],
    },
)


DatasetsPreviewRoboflowImportResponseStorage = TypedDict(
    "DatasetsPreviewRoboflowImportResponseStorage", {"usedBytes": float, "limitBytes": float, "hasEnoughStorage": bool}
)


DatasetsPreviewRoboflowImportResponse = TypedDict(
    "DatasetsPreviewRoboflowImportResponse",
    {
        "workspace": DatasetsPreviewRoboflowImportResponseWorkspace,
        "newDatasets": list[DatasetsPreviewRoboflowImportResponseNewDatasetsItem],
        "skippedCount": int,
        "missingVersionCount": int,
        "unsupportedCount": int,
        "unresolvedCount": int,
        "bytesTotal": int,
        "storage": DatasetsPreviewRoboflowImportResponseStorage,
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
        "deployment": str,
        "name": str,
        "status": Literal["creating", "deploying", "ready", "stopping", "stopped", "failed"],
        "statusMessage": NotRequired[str],
        "region": str,
        "serviceUrl": NotRequired[str],
        "resources": DeploymentsRetrieveResponseDeploymentResources,
        "deployedAt": NotRequired[str],
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


DeploymentsRetrieveHealthResponse = TypedDict(
    "DeploymentsRetrieveHealthResponse",
    {"healthy": bool, "status": NotRequired[float], "latencyMs": float, "error": NotRequired[str]},
)


DeploymentsRetrieveLogsResponseEntriesItemHttpRequest = TypedDict(
    "DeploymentsRetrieveLogsResponseEntriesItemHttpRequest",
    {"method": str, "url": str, "status": float, "latencyMs": float, "userAgent": NotRequired[str]},
)


DeploymentsRetrieveLogsResponseEntriesItem = TypedDict(
    "DeploymentsRetrieveLogsResponseEntriesItem",
    {
        "timestamp": str,
        "severity": Literal["DEFAULT", "DEBUG", "INFO", "NOTICE", "WARNING", "ERROR", "CRITICAL", "ALERT", "EMERGENCY"],
        "message": str,
        "httpRequest": NotRequired[DeploymentsRetrieveLogsResponseEntriesItemHttpRequest],
    },
)


DeploymentsRetrieveLogsResponse = TypedDict(
    "DeploymentsRetrieveLogsResponse",
    {"entries": list[DeploymentsRetrieveLogsResponseEntriesItem], "nextPageToken": NotRequired[str]},
)


DeploymentsRetrieveMetricsResponseVariant1TimeRange = TypedDict(
    "DeploymentsRetrieveMetricsResponseVariant1TimeRange", {"start": str, "end": str}
)


DeploymentsRetrieveMetricsResponseVariant1Summary = TypedDict(
    "DeploymentsRetrieveMetricsResponseVariant1Summary",
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


DeploymentsRetrieveMetricsResponseVariant1TimeSeriesRequestsItem = TypedDict(
    "DeploymentsRetrieveMetricsResponseVariant1TimeSeriesRequestsItem", {"timestamp": str, "value": float}
)


DeploymentsRetrieveMetricsResponseVariant1TimeSeriesErrorsItem = TypedDict(
    "DeploymentsRetrieveMetricsResponseVariant1TimeSeriesErrorsItem", {"timestamp": str, "value": float}
)


DeploymentsRetrieveMetricsResponseVariant1TimeSeriesLatencyP50Item = TypedDict(
    "DeploymentsRetrieveMetricsResponseVariant1TimeSeriesLatencyP50Item", {"timestamp": str, "value": float}
)


DeploymentsRetrieveMetricsResponseVariant1TimeSeriesLatencyP95Item = TypedDict(
    "DeploymentsRetrieveMetricsResponseVariant1TimeSeriesLatencyP95Item", {"timestamp": str, "value": float}
)


DeploymentsRetrieveMetricsResponseVariant1TimeSeriesCpuUtilizationItem = TypedDict(
    "DeploymentsRetrieveMetricsResponseVariant1TimeSeriesCpuUtilizationItem", {"timestamp": str, "value": float}
)


DeploymentsRetrieveMetricsResponseVariant1TimeSeriesMemoryUtilizationItem = TypedDict(
    "DeploymentsRetrieveMetricsResponseVariant1TimeSeriesMemoryUtilizationItem", {"timestamp": str, "value": float}
)


DeploymentsRetrieveMetricsResponseVariant1TimeSeriesInstanceCountItem = TypedDict(
    "DeploymentsRetrieveMetricsResponseVariant1TimeSeriesInstanceCountItem", {"timestamp": str, "value": float}
)


DeploymentsRetrieveMetricsResponseVariant1TimeSeries = TypedDict(
    "DeploymentsRetrieveMetricsResponseVariant1TimeSeries",
    {
        "requests": list[DeploymentsRetrieveMetricsResponseVariant1TimeSeriesRequestsItem],
        "errors": list[DeploymentsRetrieveMetricsResponseVariant1TimeSeriesErrorsItem],
        "latencyP50": list[DeploymentsRetrieveMetricsResponseVariant1TimeSeriesLatencyP50Item],
        "latencyP95": list[DeploymentsRetrieveMetricsResponseVariant1TimeSeriesLatencyP95Item],
        "cpuUtilization": list[DeploymentsRetrieveMetricsResponseVariant1TimeSeriesCpuUtilizationItem],
        "memoryUtilization": list[DeploymentsRetrieveMetricsResponseVariant1TimeSeriesMemoryUtilizationItem],
        "instanceCount": list[DeploymentsRetrieveMetricsResponseVariant1TimeSeriesInstanceCountItem],
    },
)


DeploymentsRetrieveMetricsResponseVariant1 = TypedDict(
    "DeploymentsRetrieveMetricsResponseVariant1",
    {
        "deploymentId": str,
        "region": str,
        "timeRange": DeploymentsRetrieveMetricsResponseVariant1TimeRange,
        "summary": DeploymentsRetrieveMetricsResponseVariant1Summary,
        "timeSeries": DeploymentsRetrieveMetricsResponseVariant1TimeSeries,
    },
)


DeploymentsRetrieveMetricsResponseVariant2 = TypedDict(
    "DeploymentsRetrieveMetricsResponseVariant2",
    {"requests24h": list[float], "totalRequests": float, "errorRate": float, "avgLatencyMs": float},
)


DeploymentsRetrieveMetricsResponse = (
    DeploymentsRetrieveMetricsResponseVariant1 | DeploymentsRetrieveMetricsResponseVariant2
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
        "speed": dict[str, float],
        "results": list[Any],
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
        "task": str | None,
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


ExploreRetrieveSearchResponseProjectsItem = TypedDict(
    "ExploreRetrieveSearchResponseProjectsItem",
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


ExploreRetrieveSearchResponseDatasetsItemSplits = TypedDict(
    "ExploreRetrieveSearchResponseDatasetsItemSplits", {"train": int, "val": int, "test": int, "labeled": int}
)


ExploreRetrieveSearchResponseDatasetsItemSampleImagesItemLabelsItem = TypedDict(
    "ExploreRetrieveSearchResponseDatasetsItemSampleImagesItemLabelsItem",
    {
        "classId": int,
        "bbox": NotRequired[list[Any]],
        "segments": NotRequired[list[float]],
        "keypoints": NotRequired[list[float]],
        "obb": NotRequired[list[Any]],
        "skeletonId": NotRequired[str],
    },
)


ExploreRetrieveSearchResponseDatasetsItemSampleImagesItem = TypedDict(
    "ExploreRetrieveSearchResponseDatasetsItemSampleImagesItem",
    {
        "url": str,
        "imageUrl": NotRequired[str],
        "width": float,
        "height": float,
        "labels": NotRequired[list[ExploreRetrieveSearchResponseDatasetsItemSampleImagesItemLabelsItem]],
    },
)


ExploreRetrieveSearchResponseDatasetsItem = TypedDict(
    "ExploreRetrieveSearchResponseDatasetsItem",
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
        "splits": NotRequired[ExploreRetrieveSearchResponseDatasetsItemSplits],
        "kptShape": NotRequired[list[Any]],
        "starCount": int,
        "sampleImages": list[ExploreRetrieveSearchResponseDatasetsItemSampleImagesItem],
        "userImageUrl": NotRequired[str],
        "updatedAt": str,
    },
)


ExploreRetrieveSearchResponse = TypedDict(
    "ExploreRetrieveSearchResponse",
    {
        "projects": list[ExploreRetrieveSearchResponseProjectsItem],
        "datasets": list[ExploreRetrieveSearchResponseDatasetsItem],
        "hasMore": bool,
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


ImagesRetrieveSignedUrlsResponse = TypedDict(
    "ImagesRetrieveSignedUrlsResponse", {"urls": dict[str, str], "thumbnails": dict[str, str]}
)


StorageIntegrationsDisconnectCloudStorageResponse = TypedDict(
    "StorageIntegrationsDisconnectCloudStorageResponse", {"success": Literal[True]}
)


StorageIntegrationsBrowseCloudStorageObjectsResponseEntriesItem = TypedDict(
    "StorageIntegrationsBrowseCloudStorageObjectsResponseEntriesItem",
    {
        "kind": Literal["folder", "file"],
        "name": str,
        "key": str,
        "size": NotRequired[float],
        "updatedAt": NotRequired[str],
    },
)


StorageIntegrationsBrowseCloudStorageObjectsResponse = TypedDict(
    "StorageIntegrationsBrowseCloudStorageObjectsResponse",
    {"entries": list[StorageIntegrationsBrowseCloudStorageObjectsResponseEntriesItem], "cursor": NotRequired[str]},
)


StorageIntegrationsListCloudStorageIntegrationsResponseIntegrationsItem = TypedDict(
    "StorageIntegrationsListCloudStorageIntegrationsResponseIntegrationsItem",
    {
        "id": str,
        "provider": Literal["gcs", "s3", "azure"],
        "credentialIdentity": str,
        "targets": list[str],
        "createdAt": str,
    },
)


StorageIntegrationsListCloudStorageIntegrationsResponse = TypedDict(
    "StorageIntegrationsListCloudStorageIntegrationsResponse",
    {"integrations": list[StorageIntegrationsListCloudStorageIntegrationsResponseIntegrationsItem]},
)


StorageIntegrationsConnectCloudStorageResponse = TypedDict(
    "StorageIntegrationsConnectCloudStorageResponse",
    {
        "id": str,
        "provider": Literal["gcs", "s3", "azure"],
        "credentialIdentity": str,
        "targets": list[str],
        "createdAt": str,
    },
)


StorageIntegrationsDiscoverCloudStorageLocationsResponse = TypedDict(
    "StorageIntegrationsDiscoverCloudStorageLocationsResponse", {"targets": list[str]}
)


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


ModelsRetrieveResponseVariant1ModelTrainArgs = TypedDict(
    "ModelsRetrieveResponseVariant1ModelTrainArgs",
    {
        "model": NotRequired[str],
        "data": NotRequired[str],
        "classes": NotRequired[list[int] | None],
        "lr0": NotRequired[float],
        "lrf": NotRequired[float],
        "momentum": NotRequired[float],
        "weight_decay": NotRequired[float],
        "warmup_epochs": NotRequired[float],
        "warmup_momentum": NotRequired[float],
        "warmup_bias_lr": NotRequired[float],
        "optimizer": NotRequired[
            Literal["auto", "SGD", "MuSGD", "Adam", "AdamW", "NAdam", "RAdam", "RMSProp", "Adamax"]
        ],
        "box": NotRequired[float],
        "cls": NotRequired[float],
        "dfl": NotRequired[float],
        "pose": NotRequired[float],
        "kobj": NotRequired[float],
        "label_smoothing": NotRequired[float],
        "hsv_h": NotRequired[float],
        "hsv_s": NotRequired[float],
        "hsv_v": NotRequired[float],
        "degrees": NotRequired[float],
        "translate": NotRequired[float],
        "scale": NotRequired[float],
        "shear": NotRequired[float],
        "perspective": NotRequired[float],
        "flipud": NotRequired[float],
        "fliplr": NotRequired[float],
        "mosaic": NotRequired[float],
        "mixup": NotRequired[float],
        "copy_paste": NotRequired[float],
        "epochs": NotRequired[int],
        "batch": NotRequired[int],
        "imgsz": NotRequired[int],
        "pretrained": NotRequired[bool],
        "patience": NotRequired[int],
        "time": NotRequired[float | None],
        "seed": NotRequired[int],
        "deterministic": NotRequired[bool],
        "amp": NotRequired[bool],
        "cos_lr": NotRequired[bool],
        "compile": NotRequired[
            bool | Literal["default", "reduce-overhead", "max-autotune", "max-autotune-no-cudagraphs"]
        ],
        "close_mosaic": NotRequired[int],
        "save_period": NotRequired[int],
        "fraction": NotRequired[float],
        "freeze": NotRequired[int | None],
        "single_cls": NotRequired[bool],
        "rect": NotRequired[bool],
        "multi_scale": NotRequired[float],
        "val": NotRequired[bool],
        "resume": NotRequired[bool],
        "device": NotRequired[Literal["0", "auto", "cpu", "mps"]],
        "cache": NotRequired[Literal["ram", "disk", "false"]],
        "workers": NotRequired[int],
        "dropout": NotRequired[float],
        "iou": NotRequired[float],
        "max_det": NotRequired[int],
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


ModelsRetrieveResponseVariant1Model = TypedDict(
    "ModelsRetrieveResponseVariant1Model",
    {
        "id": str,
        "owner": str,
        "project": str,
        "projectName": str,
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
        "color": NotRequired[str],
        "datasetId": NotRequired[str],
        "datasetVersion": NotRequired[ModelsRetrieveResponseVariant1ModelDatasetVersion],
        "sourceModelId": NotRequired[str],
        "sourceModel": NotRequired[ModelsRetrieveResponseVariant1ModelSourceModel],
        "baseModel": NotRequired[str],
        "epochs": NotRequired[int],
        "bestEpoch": NotRequired[int | None],
        "bestFitness": NotRequired[float | None],
        "trainArgs": NotRequired[ModelsRetrieveResponseVariant1ModelTrainArgs],
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


ModelsRetrieveFilesResponseFilesItem = TypedDict(
    "ModelsRetrieveFilesResponseFilesItem", {"name": str, "size": float, "downloadUrl": str}
)


ModelsRetrieveFilesResponse = TypedDict(
    "ModelsRetrieveFilesResponse", {"files": list[ModelsRetrieveFilesResponseFilesItem]}
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
        "speed": dict[str, float],
        "results": list[Any],
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
        "task": str | None,
        "version": dict[str, str],
    },
)


ModelsPredictResponse = TypedDict(
    "ModelsPredictResponse",
    {"images": list[ModelsPredictResponseImagesItem], "metadata": ModelsPredictResponseMetadata},
)


ModelsRetrieveTrainingResponseJobProgress = TypedDict(
    "ModelsRetrieveTrainingResponseJobProgress",
    {
        "currentEpoch": float,
        "totalEpochs": float,
        "startedAt": NotRequired[str],
        "completedAt": NotRequired[str],
        "percentage": float,
    },
)


ModelsRetrieveTrainingResponseJobTiming = TypedDict(
    "ModelsRetrieveTrainingResponseJobTiming", {"elapsedMs": float, "timePerEpochMs": float, "etaMs": float}
)


ModelsRetrieveTrainingResponseJobCompute = TypedDict(
    "ModelsRetrieveTrainingResponseJobCompute", {"gpuType": str, "gpuDisplayName": str, "gpuMemoryGb": float}
)


ModelsRetrieveTrainingResponseJobTrainArgs = TypedDict(
    "ModelsRetrieveTrainingResponseJobTrainArgs",
    {
        "model": NotRequired[str],
        "epochs": NotRequired[float | str],
        "batch": NotRequired[float | str],
        "imgsz": NotRequired[float | str],
    },
)


ModelsRetrieveTrainingResponseJobError = TypedDict(
    "ModelsRetrieveTrainingResponseJobError", {"message": str, "code": NotRequired[str], "timestamp": str}
)


ModelsRetrieveTrainingResponseJob = TypedDict(
    "ModelsRetrieveTrainingResponseJob",
    {
        "id": str,
        "status": Literal["pending", "untrained", "starting", "running", "completed", "failed", "cancelled"],
        "progress": ModelsRetrieveTrainingResponseJobProgress,
        "timing": ModelsRetrieveTrainingResponseJobTiming,
        "compute": ModelsRetrieveTrainingResponseJobCompute | None,
        "trainArgs": ModelsRetrieveTrainingResponseJobTrainArgs | None,
        "epochMetrics": dict[str, Any] | None,
        "error": ModelsRetrieveTrainingResponseJobError | None,
        "createdAt": str,
        "updatedAt": str,
    },
)


ModelsRetrieveTrainingResponseInstanceStatus = TypedDict(
    "ModelsRetrieveTrainingResponseInstanceStatus", {"status": str}
)


ModelsRetrieveTrainingResponse = TypedDict(
    "ModelsRetrieveTrainingResponse",
    {
        "job": ModelsRetrieveTrainingResponseJob | None,
        "instanceStatus": NotRequired[ModelsRetrieveTrainingResponseInstanceStatus | None],
    },
)


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


ModelsListResponseModelsItemTrainArgs = TypedDict(
    "ModelsListResponseModelsItemTrainArgs",
    {
        "model": NotRequired[str],
        "data": NotRequired[str],
        "classes": NotRequired[list[int] | None],
        "lr0": NotRequired[float],
        "lrf": NotRequired[float],
        "momentum": NotRequired[float],
        "weight_decay": NotRequired[float],
        "warmup_epochs": NotRequired[float],
        "warmup_momentum": NotRequired[float],
        "warmup_bias_lr": NotRequired[float],
        "optimizer": NotRequired[
            Literal["auto", "SGD", "MuSGD", "Adam", "AdamW", "NAdam", "RAdam", "RMSProp", "Adamax"]
        ],
        "box": NotRequired[float],
        "cls": NotRequired[float],
        "dfl": NotRequired[float],
        "pose": NotRequired[float],
        "kobj": NotRequired[float],
        "label_smoothing": NotRequired[float],
        "hsv_h": NotRequired[float],
        "hsv_s": NotRequired[float],
        "hsv_v": NotRequired[float],
        "degrees": NotRequired[float],
        "translate": NotRequired[float],
        "scale": NotRequired[float],
        "shear": NotRequired[float],
        "perspective": NotRequired[float],
        "flipud": NotRequired[float],
        "fliplr": NotRequired[float],
        "mosaic": NotRequired[float],
        "mixup": NotRequired[float],
        "copy_paste": NotRequired[float],
        "epochs": NotRequired[int],
        "batch": NotRequired[int],
        "imgsz": NotRequired[int],
        "pretrained": NotRequired[bool],
        "patience": NotRequired[int],
        "time": NotRequired[float | None],
        "seed": NotRequired[int],
        "deterministic": NotRequired[bool],
        "amp": NotRequired[bool],
        "cos_lr": NotRequired[bool],
        "compile": NotRequired[
            bool | Literal["default", "reduce-overhead", "max-autotune", "max-autotune-no-cudagraphs"]
        ],
        "close_mosaic": NotRequired[int],
        "save_period": NotRequired[int],
        "fraction": NotRequired[float],
        "freeze": NotRequired[int | None],
        "single_cls": NotRequired[bool],
        "rect": NotRequired[bool],
        "multi_scale": NotRequired[float],
        "val": NotRequired[bool],
        "resume": NotRequired[bool],
        "device": NotRequired[Literal["0", "auto", "cpu", "mps"]],
        "cache": NotRequired[Literal["ram", "disk", "false"]],
        "workers": NotRequired[int],
        "dropout": NotRequired[float],
        "iou": NotRequired[float],
        "max_det": NotRequired[int],
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
        "color": NotRequired[str],
        "datasetId": NotRequired[str],
        "datasetVersion": NotRequired[ModelsListResponseModelsItemDatasetVersion],
        "sourceModelId": NotRequired[str],
        "sourceModel": NotRequired[ModelsListResponseModelsItemSourceModel],
        "baseModel": NotRequired[str],
        "epochs": NotRequired[int],
        "bestEpoch": NotRequired[int | None],
        "bestFitness": NotRequired[float | None],
        "trainArgs": NotRequired[ModelsListResponseModelsItemTrainArgs],
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


ExportsRetrieveStatusResponseExportFile = TypedDict(
    "ExportsRetrieveStatusResponseExportFile",
    {"size": NotRequired[float], "downloadUrl": NotRequired[str], "downloadFilename": NotRequired[str]},
)


ExportsRetrieveStatusResponseExportError = TypedDict(
    "ExportsRetrieveStatusResponseExportError", {"message": str, "timestamp": str}
)


ExportsRetrieveStatusResponseExport = TypedDict(
    "ExportsRetrieveStatusResponseExport",
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
        "file": NotRequired[ExportsRetrieveStatusResponseExportFile],
        "error": NotRequired[ExportsRetrieveStatusResponseExportError],
        "startedAt": NotRequired[str],
        "completedAt": NotRequired[str],
        "createdAt": str,
        "updatedAt": str,
    },
)


ExportsRetrieveStatusResponse = TypedDict(
    "ExportsRetrieveStatusResponse", {"export": ExportsRetrieveStatusResponseExport}
)


ExportsCancelOrDeleteResponse = TypedDict(
    "ExportsCancelOrDeleteResponse", {"success": Literal[True], "action": Literal["cancelled", "deleted"]}
)


ExportsListModelResponse = TypedDict(
    "ExportsListModelResponse",
    {"exports": list[ExportsRetrieveStatusResponseExport], "region": Literal["us", "eu", "ap"]},
)


ExportsExportModelResponse = TypedDict(
    "ExportsExportModelResponse",
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


ProjectsRetrieveResponseModelsItemTrainArgs = TypedDict(
    "ProjectsRetrieveResponseModelsItemTrainArgs",
    {
        "model": NotRequired[str],
        "data": NotRequired[str],
        "classes": NotRequired[list[int] | None],
        "lr0": NotRequired[float],
        "lrf": NotRequired[float],
        "momentum": NotRequired[float],
        "weight_decay": NotRequired[float],
        "warmup_epochs": NotRequired[float],
        "warmup_momentum": NotRequired[float],
        "warmup_bias_lr": NotRequired[float],
        "optimizer": NotRequired[
            Literal["auto", "SGD", "MuSGD", "Adam", "AdamW", "NAdam", "RAdam", "RMSProp", "Adamax"]
        ],
        "box": NotRequired[float],
        "cls": NotRequired[float],
        "dfl": NotRequired[float],
        "pose": NotRequired[float],
        "kobj": NotRequired[float],
        "label_smoothing": NotRequired[float],
        "hsv_h": NotRequired[float],
        "hsv_s": NotRequired[float],
        "hsv_v": NotRequired[float],
        "degrees": NotRequired[float],
        "translate": NotRequired[float],
        "scale": NotRequired[float],
        "shear": NotRequired[float],
        "perspective": NotRequired[float],
        "flipud": NotRequired[float],
        "fliplr": NotRequired[float],
        "mosaic": NotRequired[float],
        "mixup": NotRequired[float],
        "copy_paste": NotRequired[float],
        "epochs": NotRequired[int],
        "batch": NotRequired[int],
        "imgsz": NotRequired[int],
        "pretrained": NotRequired[bool],
        "patience": NotRequired[int],
        "time": NotRequired[float | None],
        "seed": NotRequired[int],
        "deterministic": NotRequired[bool],
        "amp": NotRequired[bool],
        "cos_lr": NotRequired[bool],
        "compile": NotRequired[
            bool | Literal["default", "reduce-overhead", "max-autotune", "max-autotune-no-cudagraphs"]
        ],
        "close_mosaic": NotRequired[int],
        "save_period": NotRequired[int],
        "fraction": NotRequired[float],
        "freeze": NotRequired[int | None],
        "single_cls": NotRequired[bool],
        "rect": NotRequired[bool],
        "multi_scale": NotRequired[float],
        "val": NotRequired[bool],
        "resume": NotRequired[bool],
        "device": NotRequired[Literal["0", "auto", "cpu", "mps"]],
        "cache": NotRequired[Literal["ram", "disk", "false"]],
        "workers": NotRequired[int],
        "dropout": NotRequired[float],
        "iou": NotRequired[float],
        "max_det": NotRequired[int],
    },
)


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
        "trainArgs": NotRequired[ProjectsRetrieveResponseModelsItemTrainArgs],
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


TrainingRetrieveGpuAvailabilityResponse = "TrainingRetrieveGpuAvailabilityResponse"


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


LifecycleRetrieveTrashResponseItemsItemParentProject = TypedDict(
    "LifecycleRetrieveTrashResponseItemsItemParentProject", {"_id": str, "name": str, "slug": str}
)


LifecycleRetrieveTrashResponseItemsItem = TypedDict(
    "LifecycleRetrieveTrashResponseItemsItem",
    {
        "_id": str,
        "type": Literal["project", "dataset", "model"],
        "name": str,
        "slug": str,
        "trashedAt": str,
        "daysRemaining": int,
        "cascadedCount": NotRequired[int],
        "parentProject": NotRequired[LifecycleRetrieveTrashResponseItemsItemParentProject],
        "sizeBytes": NotRequired[float],
    },
)


LifecycleRetrieveTrashResponseSummaryByTypeProjects = TypedDict(
    "LifecycleRetrieveTrashResponseSummaryByTypeProjects", {"count": int}
)


LifecycleRetrieveTrashResponseSummaryByTypeDatasets = TypedDict(
    "LifecycleRetrieveTrashResponseSummaryByTypeDatasets", {"count": int, "sizeBytes": float}
)


LifecycleRetrieveTrashResponseSummaryByTypeModels = TypedDict(
    "LifecycleRetrieveTrashResponseSummaryByTypeModels", {"count": int, "sizeBytes": float}
)


LifecycleRetrieveTrashResponseSummaryByTypeExports = TypedDict(
    "LifecycleRetrieveTrashResponseSummaryByTypeExports", {"count": int, "sizeBytes": float}
)


LifecycleRetrieveTrashResponseSummaryByType = TypedDict(
    "LifecycleRetrieveTrashResponseSummaryByType",
    {
        "projects": LifecycleRetrieveTrashResponseSummaryByTypeProjects,
        "datasets": LifecycleRetrieveTrashResponseSummaryByTypeDatasets,
        "models": LifecycleRetrieveTrashResponseSummaryByTypeModels,
        "exports": LifecycleRetrieveTrashResponseSummaryByTypeExports,
    },
)


LifecycleRetrieveTrashResponseSummary = TypedDict(
    "LifecycleRetrieveTrashResponseSummary",
    {"totalItems": int, "totalSizeBytes": float, "byType": LifecycleRetrieveTrashResponseSummaryByType},
)


LifecycleRetrieveTrashResponse = TypedDict(
    "LifecycleRetrieveTrashResponse",
    {
        "items": list[LifecycleRetrieveTrashResponseItemsItem],
        "total": int,
        "page": int,
        "limit": int,
        "totalPages": int,
        "summary": LifecycleRetrieveTrashResponseSummary,
        "region": Literal["us", "eu", "ap"],
    },
)


LifecycleRestoreTrashedItemResponse = TypedDict(
    "LifecycleRestoreTrashedItemResponse", {"success": Literal[True], "restoredModels": NotRequired[int]}
)


LifecyclePermanentlyDeleteTrashResponse = TypedDict(
    "LifecyclePermanentlyDeleteTrashResponse",
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


UploadRetrieveFileUrlResponse = TypedDict(
    "UploadRetrieveFileUrlResponse", {"sessionId": str, "uploadUrl": str, "expiresAt": str}
)
