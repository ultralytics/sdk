# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from __future__ import annotations

from typing import Any, Literal, NotRequired, TypedDict

DatasetsListResponseDatasetsItemSplits = TypedDict(
    "DatasetsListResponseDatasetsItemSplits", {"train": float, "val": float, "test": float, "labeled": float}
)


DatasetsListResponseDatasetsItemSampleImagesItemLabelsItem = TypedDict(
    "DatasetsListResponseDatasetsItemSampleImagesItemLabelsItem",
    {
        "classId": float,
        "bbox": NotRequired[list[float]],
        "segments": NotRequired[list[float]],
        "keypoints": NotRequired[list[float]],
        "obb": NotRequired[list[float]],
        "skeletonId": NotRequired[str],
    },
)


DatasetsListResponseDatasetsItemSampleImagesItem = TypedDict(
    "DatasetsListResponseDatasetsItemSampleImagesItem",
    {
        "url": str,
        "imageUrl": NotRequired[str],
        "width": float,
        "height": float,
        "labels": NotRequired[list[DatasetsListResponseDatasetsItemSampleImagesItemLabelsItem]],
    },
)


DatasetsListResponseDatasetsItemProcessingError = TypedDict(
    "DatasetsListResponseDatasetsItemProcessingError", {"message": str, "timestamp": str}
)


DatasetsListResponseDatasetsItemVersionsItemSplits = TypedDict(
    "DatasetsListResponseDatasetsItemVersionsItemSplits",
    {"train": float, "val": float, "test": float, "labeled": float},
)


DatasetsListResponseDatasetsItemVersionsItem = TypedDict(
    "DatasetsListResponseDatasetsItemVersionsItem",
    {
        "version": float,
        "description": NotRequired[str],
        "sizeBytes": NotRequired[float],
        "contentHash": NotRequired[str],
        "imageCount": float,
        "classCount": float,
        "annotationCount": float,
        "splits": DatasetsListResponseDatasetsItemVersionsItemSplits,
        "createdAt": str,
    },
)


DatasetsListResponseDatasetsItem = TypedDict(
    "DatasetsListResponseDatasetsItem",
    {
        "_id": str,
        "username": str,
        "slug": str,
        "name": str,
        "description": NotRequired[str | None],
        "visibility": Literal["public", "private"],
        "task": Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"],
        "imageCount": float,
        "classCount": NotRequired[float | None],
        "classNames": NotRequired[list[str] | None],
        "format": NotRequired[Literal["yolo", "coco", "voc", "raw", "ndjson"]],
        "tags": NotRequired[list[str] | None],
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
            | None
        ],
        "splits": NotRequired[DatasetsListResponseDatasetsItemSplits],
        "annotationCount": NotRequired[float],
        "totalBytes": NotRequired[float],
        "starCount": float,
        "isStarred": bool,
        "status": NotRequired[Literal["processing", "ready", "failed"]],
        "sampleImages": NotRequired[list[DatasetsListResponseDatasetsItemSampleImagesItem]],
        "storageProvider": NotRequired[Literal["gcs", "s3", "azure"]],
        "classColors": NotRequired[dict[str, str]],
        "kptShape": NotRequired[list[Any] | None],
        "flipIdx": NotRequired[list[int] | None],
        "processingTimeMs": NotRequired[float],
        "processingError": NotRequired[DatasetsListResponseDatasetsItemProcessingError],
        "errorCount": NotRequired[float],
        "iconColor": NotRequired[str],
        "iconLetter": NotRequired[str],
        "iconImage": NotRequired[str],
        "clonedFrom": NotRequired[str],
        "cloneCount": NotRequired[float],
        "region": NotRequired[Literal["us", "eu", "ap"]],
        "versions": NotRequired[list[DatasetsListResponseDatasetsItemVersionsItem]],
        "createdAt": str,
        "updatedAt": str,
    },
)


DatasetsListResponse = TypedDict(
    "DatasetsListResponse",
    {"datasets": list[DatasetsListResponseDatasetsItem], "total": float, "region": Literal["us", "eu", "ap"]},
)


DatasetsCreateResponse = TypedDict(
    "DatasetsCreateResponse",
    {
        "projectId": NotRequired[str],
        "datasetId": NotRequired[str],
        "modelId": NotRequired[str],
        "slug": str,
        "region": Literal["us", "eu", "ap"],
    },
)


DatasetsRetrieveResponseDatasetSplits = TypedDict(
    "DatasetsRetrieveResponseDatasetSplits", {"train": float, "val": float, "test": float, "labeled": float}
)


DatasetsRetrieveResponseDatasetSampleImagesItemLabelsItem = TypedDict(
    "DatasetsRetrieveResponseDatasetSampleImagesItemLabelsItem",
    {
        "classId": float,
        "bbox": NotRequired[list[float]],
        "segments": NotRequired[list[float]],
        "keypoints": NotRequired[list[float]],
        "obb": NotRequired[list[float]],
        "skeletonId": NotRequired[str],
    },
)


DatasetsRetrieveResponseDatasetSampleImagesItem = TypedDict(
    "DatasetsRetrieveResponseDatasetSampleImagesItem",
    {
        "url": str,
        "imageUrl": NotRequired[str],
        "width": float,
        "height": float,
        "labels": NotRequired[list[DatasetsRetrieveResponseDatasetSampleImagesItemLabelsItem]],
    },
)


DatasetsRetrieveResponseDatasetProcessingError = TypedDict(
    "DatasetsRetrieveResponseDatasetProcessingError", {"message": str, "timestamp": str}
)


DatasetsRetrieveResponseDatasetVersionsItemSplits = TypedDict(
    "DatasetsRetrieveResponseDatasetVersionsItemSplits", {"train": float, "val": float, "test": float, "labeled": float}
)


DatasetsRetrieveResponseDatasetVersionsItem = TypedDict(
    "DatasetsRetrieveResponseDatasetVersionsItem",
    {
        "version": float,
        "description": NotRequired[str],
        "sizeBytes": NotRequired[float],
        "contentHash": NotRequired[str],
        "imageCount": float,
        "classCount": float,
        "annotationCount": float,
        "splits": DatasetsRetrieveResponseDatasetVersionsItemSplits,
        "createdAt": str,
    },
)


DatasetsRetrieveResponseDataset = TypedDict(
    "DatasetsRetrieveResponseDataset",
    {
        "_id": str,
        "username": str,
        "slug": str,
        "name": str,
        "description": NotRequired[str | None],
        "visibility": Literal["public", "private"],
        "task": Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"],
        "imageCount": float,
        "classCount": NotRequired[float | None],
        "classNames": NotRequired[list[str] | None],
        "format": NotRequired[Literal["yolo", "coco", "voc", "raw", "ndjson"]],
        "tags": NotRequired[list[str] | None],
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
            | None
        ],
        "splits": NotRequired[DatasetsRetrieveResponseDatasetSplits],
        "annotationCount": NotRequired[float],
        "totalBytes": NotRequired[float],
        "starCount": float,
        "isStarred": bool,
        "status": NotRequired[Literal["processing", "ready", "failed"]],
        "sampleImages": NotRequired[list[DatasetsRetrieveResponseDatasetSampleImagesItem]],
        "storageProvider": NotRequired[Literal["gcs", "s3", "azure"]],
        "classColors": NotRequired[dict[str, str]],
        "kptShape": NotRequired[list[Any] | None],
        "flipIdx": NotRequired[list[int] | None],
        "processingTimeMs": NotRequired[float],
        "processingError": NotRequired[DatasetsRetrieveResponseDatasetProcessingError],
        "errorCount": NotRequired[float],
        "iconColor": NotRequired[str],
        "iconLetter": NotRequired[str],
        "iconImage": NotRequired[str],
        "clonedFrom": NotRequired[str],
        "cloneCount": NotRequired[float],
        "region": NotRequired[Literal["us", "eu", "ap"]],
        "versions": NotRequired[list[DatasetsRetrieveResponseDatasetVersionsItem]],
        "createdAt": str,
        "updatedAt": str,
    },
)


DatasetsRetrieveResponse = TypedDict("DatasetsRetrieveResponse", {"dataset": DatasetsRetrieveResponseDataset})


DatasetsUpdateResponse = TypedDict("DatasetsUpdateResponse", {"success": Literal[True]})


DatasetsDeleteResponse = TypedDict("DatasetsDeleteResponse", {"success": Literal[True]})


DatasetsRetrieveMetadataResponse = TypedDict(
    "DatasetsRetrieveMetadataResponse", {"metadata": dict[str, Any], "properties": list[list[Any]]}
)


DatasetsCloneResponse = TypedDict(
    "DatasetsCloneResponse",
    {
        "datasetId": str,
        "slug": str,
        "name": str,
        "imageCount": float,
        "classCount": NotRequired[float],
        "region": Literal["us", "eu", "ap"],
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


DatasetsRedistributeSplitsResponseSplits = TypedDict(
    "DatasetsRedistributeSplitsResponseSplits", {"train": int, "val": int, "test": int}
)


DatasetsRedistributeSplitsResponse = TypedDict(
    "DatasetsRedistributeSplitsResponse",
    {"success": Literal[True], "splits": DatasetsRedistributeSplitsResponseSplits, "modified": int},
)


DatasetsListImagesResponseImagesItemLabelsItem = TypedDict(
    "DatasetsListImagesResponseImagesItemLabelsItem",
    {
        "classId": float,
        "bbox": NotRequired[list[float]],
        "segments": NotRequired[list[float]],
        "keypoints": NotRequired[list[float]],
        "obb": NotRequired[list[float]],
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
        "width": float,
        "height": float,
        "split": Literal["train", "val", "test"],
        "labelCount": float,
        "name": str,
        "bytes": NotRequired[float],
        "error": NotRequired[str | None],
        "labels": NotRequired[list[DatasetsListImagesResponseImagesItemLabelsItem]],
        "labelsTruncated": NotRequired[Literal[True]],
    },
)


DatasetsListImagesResponse = TypedDict(
    "DatasetsListImagesResponse",
    {
        "images": list[DatasetsListImagesResponseImagesItem],
        "total": NotRequired[float],
        "hasMore": bool,
        "classes": list[str],
        "errorCount": float,
        "nextCursor": NotRequired[str],
    },
)


DatasetsRetrieveSelectedImagesResponseImagesItemLabelsItem = TypedDict(
    "DatasetsRetrieveSelectedImagesResponseImagesItemLabelsItem",
    {
        "classId": float,
        "bbox": NotRequired[list[float]],
        "segments": NotRequired[list[float]],
        "keypoints": NotRequired[list[float]],
        "obb": NotRequired[list[float]],
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
        "width": float,
        "height": float,
        "split": Literal["train", "val", "test"],
        "labelCount": float,
        "name": str,
        "bytes": NotRequired[float],
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
    },
)


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


DatasetsIngestResponse = TypedDict(
    "DatasetsIngestResponse", {"jobId": str, "datasetId": str, "status": Literal["queued"]}
)


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


DatasetsRetrieveImagesClusteringResponseImagesItem = TypedDict(
    "DatasetsRetrieveImagesClusteringResponseImagesItem",
    {
        "id": str,
        "umapX": float,
        "umapY": float,
        "split": Literal["train", "val", "test"] | None,
        "classIds": list[int],
        "width": float,
        "height": float,
        "bytes": float | None,
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


DatasetsListModelsResponseModelsItemDatasetVersion = TypedDict(
    "DatasetsListModelsResponseModelsItemDatasetVersion", {"version": int, "contentHash": str}
)


DatasetsListModelsResponseModelsItem = TypedDict(
    "DatasetsListModelsResponseModelsItem",
    {
        "_id": str,
        "name": str,
        "slug": str,
        "status": Literal["pending", "untrained", "starting", "running", "completed", "failed", "cancelled"],
        "task": NotRequired[Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"]],
        "datasetVersion": NotRequired[DatasetsListModelsResponseModelsItemDatasetVersion],
        "epochs": NotRequired[float],
        "bestEpoch": NotRequired[float],
        "bestFitness": NotRequired[float],
        "metrics": dict[str, float],
        "startedAt": NotRequired[str],
        "completedAt": NotRequired[str],
        "createdAt": str,
        "projectId": str,
        "projectSlug": NotRequired[str],
        "projectIconColor": NotRequired[str],
        "projectIconLetter": NotRequired[str],
        "projectIconImage": NotRequired[str],
        "username": str,
    },
)


DatasetsListModelsResponse = TypedDict(
    "DatasetsListModelsResponse", {"models": list[DatasetsListModelsResponseModelsItem], "count": int}
)


DatasetsRestoreResponse = TypedDict("DatasetsRestoreResponse", {"version": int, "imageCount": int})


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


ImagesRetrieveLabelsResponseLabelsItem = TypedDict(
    "ImagesRetrieveLabelsResponseLabelsItem",
    {
        "classId": float,
        "bbox": NotRequired[list[float]],
        "segments": NotRequired[list[float]],
        "keypoints": NotRequired[list[float]],
        "obb": NotRequired[list[float]],
        "skeletonId": NotRequired[str],
    },
)


ImagesRetrieveLabelsResponse = TypedDict(
    "ImagesRetrieveLabelsResponse",
    {
        "labels": list[ImagesRetrieveLabelsResponseLabelsItem],
        "classNames": list[str],
        "labelsTruncated": NotRequired[Literal[True]],
    },
)


ImagesUpdateLabelsResponseLabelsItem = TypedDict(
    "ImagesUpdateLabelsResponseLabelsItem",
    {
        "classId": float,
        "bbox": NotRequired[list[float]],
        "segments": NotRequired[list[float]],
        "keypoints": NotRequired[list[float]],
        "obb": NotRequired[list[float]],
        "skeletonId": NotRequired[str],
    },
)


ImagesUpdateLabelsResponse = TypedDict(
    "ImagesUpdateLabelsResponse",
    {"success": Literal[True], "labels": list[ImagesUpdateLabelsResponseLabelsItem], "labelCount": float},
)


ImagesRetrieveMetadataResponseProperties = TypedDict(
    "ImagesRetrieveMetadataResponseProperties",
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


ImagesRetrieveMetadataResponse = TypedDict(
    "ImagesRetrieveMetadataResponse",
    {"metadata": dict[str, Any], "properties": ImagesRetrieveMetadataResponseProperties},
)


ImagesUpdateMetadataResponse = TypedDict("ImagesUpdateMetadataResponse", {"metadata": dict[str, Any], "updatedAt": str})


ImagesUpdateBulkResponse = TypedDict(
    "ImagesUpdateBulkResponse",
    {"success": Literal[True], "modifiedCount": float, "skippedCount": float, "targetSplit": str},
)


ImagesDeleteBulkResponse = TypedDict(
    "ImagesDeleteBulkResponse", {"success": Literal[True], "deletedCount": float, "deletedImageIds": list[str]}
)


ImagesPredictResponsePredictionsItem = TypedDict(
    "ImagesPredictResponsePredictionsItem",
    {
        "classId": float,
        "bbox": NotRequired[list[float]],
        "segments": NotRequired[list[float]],
        "keypoints": NotRequired[list[float]],
        "obb": NotRequired[list[float]],
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


ImagesRetrieveSignedUrlsResponse = TypedDict(
    "ImagesRetrieveSignedUrlsResponse", {"urls": dict[str, str], "thumbnails": dict[str, str]}
)


ImagesDeleteResponse = TypedDict(
    "ImagesDeleteResponse", {"success": Literal[True], "deletedImageId": str, "deletedCount": int}
)


ProjectsListResponseProjectsItemViewPreferences = TypedDict(
    "ProjectsListResponseProjectsItemViewPreferences",
    {
        "sortBy": NotRequired[Literal["newest", "oldest", "name-asc", "name-desc", "size-asc", "size-desc"]],
        "groupBy": NotRequired[Literal["none", "task"]],
        "statusFilter": NotRequired[Literal["all", "completed", "running", "starting", "failed"]],
    },
)


ProjectsListResponseProjectsItem = TypedDict(
    "ProjectsListResponseProjectsItem",
    {
        "_id": str,
        "username": str,
        "slug": str,
        "name": str,
        "description": NotRequired[str | None],
        "visibility": Literal["public", "private"],
        "tags": NotRequired[list[str] | None],
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
            | None
        ],
        "iconColor": NotRequired[str],
        "iconLetter": NotRequired[str | None],
        "iconImage": NotRequired[str],
        "modelCount": float,
        "modelNames": NotRequired[list[str]],
        "totalBytes": NotRequired[float],
        "starCount": float,
        "isStarred": bool,
        "archived": NotRequired[bool],
        "region": NotRequired[Literal["us", "eu", "ap"]],
        "task": NotRequired[Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"] | None],
        "clonedFrom": NotRequired[str],
        "cloneCount": NotRequired[float],
        "totalModelDownloadCount": NotRequired[float],
        "totalExportDownloadCount": NotRequired[float],
        "viewPreferences": NotRequired[ProjectsListResponseProjectsItemViewPreferences],
        "createdAt": str,
        "updatedAt": str,
    },
)


ProjectsListResponse = TypedDict(
    "ProjectsListResponse",
    {"projects": list[ProjectsListResponseProjectsItem], "total": float, "region": Literal["us", "eu", "ap"]},
)


ProjectsCreateResponse = TypedDict(
    "ProjectsCreateResponse",
    {
        "projectId": NotRequired[str],
        "datasetId": NotRequired[str],
        "modelId": NotRequired[str],
        "slug": str,
        "region": Literal["us", "eu", "ap"],
    },
)


ProjectsRetrieveResponseProjectViewPreferences = TypedDict(
    "ProjectsRetrieveResponseProjectViewPreferences",
    {
        "sortBy": NotRequired[Literal["newest", "oldest", "name-asc", "name-desc", "size-asc", "size-desc"]],
        "groupBy": NotRequired[Literal["none", "task"]],
        "statusFilter": NotRequired[Literal["all", "completed", "running", "starting", "failed"]],
    },
)


ProjectsRetrieveResponseProject = TypedDict(
    "ProjectsRetrieveResponseProject",
    {
        "_id": str,
        "username": str,
        "slug": str,
        "name": str,
        "description": NotRequired[str | None],
        "visibility": Literal["public", "private"],
        "tags": NotRequired[list[str] | None],
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
            | None
        ],
        "iconColor": NotRequired[str],
        "iconLetter": NotRequired[str | None],
        "iconImage": NotRequired[str],
        "modelCount": float,
        "starCount": float,
        "isStarred": bool,
        "archived": NotRequired[bool],
        "region": NotRequired[Literal["us", "eu", "ap"]],
        "task": NotRequired[Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"] | None],
        "clonedFrom": NotRequired[str],
        "cloneCount": NotRequired[float],
        "totalModelDownloadCount": NotRequired[float],
        "totalExportDownloadCount": NotRequired[float],
        "viewPreferences": NotRequired[ProjectsRetrieveResponseProjectViewPreferences],
        "createdAt": str,
        "updatedAt": str,
    },
)


ProjectsRetrieveResponse = TypedDict(
    "ProjectsRetrieveResponse", {"project": ProjectsRetrieveResponseProject, "isOwner": bool}
)


ProjectsUpdateResponse = TypedDict("ProjectsUpdateResponse", {"success": Literal[True]})


ProjectsDeleteResponse = TypedDict("ProjectsDeleteResponse", {"success": Literal[True]})


ProjectsRetrieveMetadataResponse = TypedDict(
    "ProjectsRetrieveMetadataResponse", {"metadata": dict[str, Any], "properties": list[list[Any]]}
)


ProjectsCloneResponse = TypedDict(
    "ProjectsCloneResponse",
    {"projectId": str, "slug": str, "name": str, "modelCount": float, "region": Literal["us", "eu", "ap"]},
)


ModelsListResponseModelsItemDatasetVersion = TypedDict(
    "ModelsListResponseModelsItemDatasetVersion", {"version": float, "contentHash": str}
)


ModelsListResponseModelsItemTrainArgs = TypedDict(
    "ModelsListResponseModelsItemTrainArgs",
    {
        "model": NotRequired[str],
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
        "epoch": NotRequired[float],
        "metrics": NotRequired[dict[str, float]],
        "fitness": NotRequired[float],
        "timestamp": NotRequired[str],
    },
)


ModelsListResponseModelsItemFile = TypedDict("ModelsListResponseModelsItemFile", {"size": float})


ModelsListResponseModelsItemTrainingError = TypedDict(
    "ModelsListResponseModelsItemTrainingError", {"message": str, "code": NotRequired[str], "timestamp": str}
)


ModelsListResponseModelsItem = TypedDict(
    "ModelsListResponseModelsItem",
    {
        "_id": str,
        "username": NotRequired[str],
        "projectId": NotRequired[str],
        "projectSlug": NotRequired[str],
        "slug": NotRequired[str],
        "name": str,
        "description": NotRequired[str | None],
        "status": NotRequired[
            Literal["pending", "untrained", "starting", "running", "completed", "failed", "cancelled"]
        ],
        "task": NotRequired[Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"]],
        "color": NotRequired[str],
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
            | None
        ],
        "datasetId": NotRequired[str],
        "datasetVersion": NotRequired[ModelsListResponseModelsItemDatasetVersion],
        "sourceModelId": NotRequired[str],
        "epochs": NotRequired[float],
        "bestEpoch": NotRequired[float | None],
        "bestFitness": NotRequired[float | None],
        "trainArgs": NotRequired[ModelsListResponseModelsItemTrainArgs],
        "version": NotRequired[str | None],
        "docs": NotRequired[str | None],
        "startedAt": NotRequired[str],
        "completedAt": NotRequired[str],
        "classNames": NotRequired[list[str] | None],
        "metrics": NotRequired[dict[str, float]],
        "trainResults": NotRequired[list[ModelsListResponseModelsItemTrainResultsItem]],
        "hasWeights": bool,
        "file": NotRequired[ModelsListResponseModelsItemFile],
        "plots": NotRequired[list[Any] | None],
        "trainingError": NotRequired[ModelsListResponseModelsItemTrainingError],
        "starCount": float,
        "isStarred": bool,
        "clonedFrom": NotRequired[str],
        "downloadCount": NotRequired[float],
        "cloneCount": NotRequired[float],
        "createdAt": NotRequired[str],
        "updatedAt": NotRequired[str],
    },
)


ModelsListResponse = TypedDict(
    "ModelsListResponse", {"models": list[ModelsListResponseModelsItem], "region": Literal["us", "eu", "ap"]}
)


ModelsCreateResponse = TypedDict(
    "ModelsCreateResponse",
    {
        "projectId": NotRequired[str],
        "datasetId": NotRequired[str],
        "modelId": NotRequired[str],
        "slug": str,
        "region": Literal["us", "eu", "ap"],
    },
)


ModelsRetrieveResponseVariant1ModelDatasetVersion = TypedDict(
    "ModelsRetrieveResponseVariant1ModelDatasetVersion", {"version": float, "contentHash": str}
)


ModelsRetrieveResponseVariant1ModelTrainArgs = TypedDict(
    "ModelsRetrieveResponseVariant1ModelTrainArgs",
    {
        "model": NotRequired[str],
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
        "epoch": NotRequired[float],
        "metrics": NotRequired[dict[str, float]],
        "fitness": NotRequired[float],
        "timestamp": NotRequired[str],
    },
)


ModelsRetrieveResponseVariant1ModelFile = TypedDict("ModelsRetrieveResponseVariant1ModelFile", {"size": float})


ModelsRetrieveResponseVariant1ModelTrainingError = TypedDict(
    "ModelsRetrieveResponseVariant1ModelTrainingError", {"message": str, "code": NotRequired[str], "timestamp": str}
)


ModelsRetrieveResponseVariant1ModelSourceModel = TypedDict(
    "ModelsRetrieveResponseVariant1ModelSourceModel",
    {
        "username": str,
        "projectSlug": str,
        "projectName": str,
        "projectIconColor": NotRequired[str],
        "projectIconLetter": NotRequired[str],
        "projectIconImage": NotRequired[str],
        "modelSlug": str,
        "modelName": str,
    },
)


ModelsRetrieveResponseVariant1Model = TypedDict(
    "ModelsRetrieveResponseVariant1Model",
    {
        "_id": str,
        "username": NotRequired[str],
        "projectId": NotRequired[str],
        "projectSlug": NotRequired[str],
        "slug": NotRequired[str],
        "name": str,
        "description": NotRequired[str | None],
        "status": NotRequired[
            Literal["pending", "untrained", "starting", "running", "completed", "failed", "cancelled"]
        ],
        "task": NotRequired[Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"]],
        "color": NotRequired[str],
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
            | None
        ],
        "datasetId": NotRequired[str],
        "datasetVersion": NotRequired[ModelsRetrieveResponseVariant1ModelDatasetVersion],
        "sourceModelId": NotRequired[str],
        "epochs": NotRequired[float],
        "bestEpoch": NotRequired[float | None],
        "bestFitness": NotRequired[float | None],
        "trainArgs": NotRequired[ModelsRetrieveResponseVariant1ModelTrainArgs],
        "version": NotRequired[str | None],
        "docs": NotRequired[str | None],
        "startedAt": NotRequired[str],
        "completedAt": NotRequired[str],
        "classNames": NotRequired[list[str] | None],
        "metrics": NotRequired[dict[str, float]],
        "trainResults": NotRequired[list[ModelsRetrieveResponseVariant1ModelTrainResultsItem]],
        "hasWeights": bool,
        "file": NotRequired[ModelsRetrieveResponseVariant1ModelFile],
        "plots": NotRequired[list[Any] | None],
        "trainingError": NotRequired[ModelsRetrieveResponseVariant1ModelTrainingError],
        "starCount": float,
        "isStarred": bool,
        "clonedFrom": NotRequired[str],
        "downloadCount": NotRequired[float],
        "cloneCount": NotRequired[float],
        "createdAt": NotRequired[str],
        "updatedAt": NotRequired[str],
        "sourceModel": NotRequired[ModelsRetrieveResponseVariant1ModelSourceModel],
        "baseModel": NotRequired[str],
        "projectLicense": NotRequired[
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
            | None
        ],
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


ModelsUpdateResponse = TypedDict("ModelsUpdateResponse", {"success": Literal[True]})


ModelsDeleteResponse = TypedDict("ModelsDeleteResponse", {"success": Literal[True]})


ModelsRetrieveMetadataResponse = TypedDict(
    "ModelsRetrieveMetadataResponse", {"metadata": dict[str, Any], "properties": list[list[Any]]}
)


ModelsCloneResponse = TypedDict(
    "ModelsCloneResponse",
    {
        "modelId": str,
        "modelSlug": str,
        "modelName": str,
        "projectId": str,
        "projectSlug": str,
        "projectName": str,
        "region": Literal["us", "eu", "ap"],
    },
)


ModelsRetrieveFilesResponseFilesItem = TypedDict(
    "ModelsRetrieveFilesResponseFilesItem", {"name": str, "size": NotRequired[float], "downloadUrl": str}
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
        "error": Any,
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


TrainingRetrieveGpuAvailabilityResponse = dict[str, Literal["High", "Medium", "Low"] | None]


ExportsListResponseExportsItemFile = TypedDict(
    "ExportsListResponseExportsItemFile",
    {"size": NotRequired[float], "downloadUrl": NotRequired[str], "downloadFilename": NotRequired[str]},
)


ExportsListResponseExportsItemError = TypedDict(
    "ExportsListResponseExportsItemError", {"message": str, "timestamp": str}
)


ExportsListResponseExportsItem = TypedDict(
    "ExportsListResponseExportsItem",
    {
        "_id": str,
        "modelId": str,
        "projectId": str,
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
        "file": NotRequired[ExportsListResponseExportsItemFile],
        "error": NotRequired[ExportsListResponseExportsItemError],
        "startedAt": NotRequired[str],
        "completedAt": NotRequired[str],
        "createdAt": str,
        "updatedAt": str,
    },
)


ExportsListResponse = TypedDict(
    "ExportsListResponse", {"exports": list[ExportsListResponseExportsItem], "region": Literal["us", "eu", "ap"]}
)


ExportsCreateResponse = TypedDict(
    "ExportsCreateResponse",
    {
        "exportId": str,
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


ExportsRetrieveResponseExportFile = TypedDict(
    "ExportsRetrieveResponseExportFile",
    {"size": NotRequired[float], "downloadUrl": NotRequired[str], "downloadFilename": NotRequired[str]},
)


ExportsRetrieveResponseExportError = TypedDict("ExportsRetrieveResponseExportError", {"message": str, "timestamp": str})


ExportsRetrieveResponseExport = TypedDict(
    "ExportsRetrieveResponseExport",
    {
        "_id": str,
        "modelId": str,
        "projectId": str,
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


DeploymentsListResponseDeploymentsItemResources = TypedDict(
    "DeploymentsListResponseDeploymentsItemResources",
    {"cpu": float, "memoryGi": float, "minInstances": float, "maxInstances": float},
)


DeploymentsListResponseDeploymentsItem = TypedDict(
    "DeploymentsListResponseDeploymentsItem",
    {
        "_id": str,
        "username": str,
        "modelId": str,
        "projectId": str,
        "name": str,
        "slug": str,
        "status": Literal["creating", "deploying", "ready", "stopping", "stopped", "failed"],
        "statusMessage": NotRequired[str | None],
        "region": str,
        "serviceUrl": NotRequired[str],
        "resources": DeploymentsListResponseDeploymentsItemResources,
        "deployedAt": NotRequired[str],
        "createdAt": str,
        "updatedAt": str,
    },
)


DeploymentsListResponse = TypedDict(
    "DeploymentsListResponse",
    {"deployments": list[DeploymentsListResponseDeploymentsItem], "total": float, "region": Literal["us", "eu", "ap"]},
)


DeploymentsCreateResponse = TypedDict(
    "DeploymentsCreateResponse", {"deploymentId": str, "status": Literal["creating"], "message": str, "region": str}
)


DeploymentsRetrieveResponseDeploymentResources = TypedDict(
    "DeploymentsRetrieveResponseDeploymentResources",
    {"cpu": float, "memoryGi": float, "minInstances": float, "maxInstances": float},
)


DeploymentsRetrieveResponseDeployment = TypedDict(
    "DeploymentsRetrieveResponseDeployment",
    {
        "_id": str,
        "username": str,
        "modelId": str,
        "projectId": str,
        "name": str,
        "slug": str,
        "status": Literal["creating", "deploying", "ready", "stopping", "stopped", "failed"],
        "statusMessage": NotRequired[str | None],
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


DeploymentsUpdateResponse = TypedDict(
    "DeploymentsUpdateResponse", {"success": Literal[True], "status": Literal["ready"], "message": str}
)


DeploymentsDeleteResponse = TypedDict("DeploymentsDeleteResponse", {"success": Literal[True]})


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


DeploymentsRetrieveHealthResponse = TypedDict(
    "DeploymentsRetrieveHealthResponse",
    {"healthy": bool, "status": NotRequired[float], "latencyMs": float, "error": NotRequired[str]},
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


DeploymentsRetrieveLogsResponseEntriesItemHttpRequest = TypedDict(
    "DeploymentsRetrieveLogsResponseEntriesItemHttpRequest",
    {"method": str, "url": str, "status": float, "latencyMs": float, "userAgent": NotRequired[str]},
)


DeploymentsRetrieveLogsResponseEntriesItem = TypedDict(
    "DeploymentsRetrieveLogsResponseEntriesItem",
    {
        "timestamp": str,
        "severity": Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL", "DEFAULT"],
        "message": str,
        "httpRequest": NotRequired[DeploymentsRetrieveLogsResponseEntriesItemHttpRequest],
    },
)


DeploymentsRetrieveLogsResponse = TypedDict(
    "DeploymentsRetrieveLogsResponse",
    {"entries": list[DeploymentsRetrieveLogsResponseEntriesItem], "nextPageToken": NotRequired[str]},
)


DeploymentsStartResponse = TypedDict(
    "DeploymentsStartResponse", {"success": Literal[True], "status": Literal["ready", "stopped"], "message": str}
)


DeploymentsStopResponse = TypedDict(
    "DeploymentsStopResponse", {"success": Literal[True], "status": Literal["ready", "stopped"], "message": str}
)


UploadRetrieveFileUrlResponse = TypedDict(
    "UploadRetrieveFileUrlResponse", {"sessionId": str, "uploadUrl": str, "expiresAt": str}
)


UploadCompleteResponseFile = TypedDict("UploadCompleteResponseFile", {"size": float, "contentType": NotRequired[str]})


UploadCompleteResponse = TypedDict(
    "UploadCompleteResponse", {"success": Literal[True], "file": UploadCompleteResponseFile}
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
        "total": float,
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


LifecyclePermanentlyDeleteTrashedItemResponse = TypedDict(
    "LifecyclePermanentlyDeleteTrashedItemResponse",
    {"success": Literal[True], "deletedCount": int, "cascadedModels": NotRequired[int]},
)
