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
        "description": NotRequired[str],
        "visibility": Literal["public", "private"],
        "task": Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"],
        "imageCount": float,
        "classCount": NotRequired[float],
        "classNames": NotRequired[list[str]],
        "format": NotRequired[Literal["yolo", "coco", "voc", "raw"]],
        "tags": NotRequired[list[str]],
        "license": NotRequired[
            Literal[
                "None",
                "CC0-1.0",
                "CC-BY-2.5",
                "CC-BY-4.0",
                "CC-BY-SA-4.0",
                "CC-BY-NC-4.0",
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
        "splits": NotRequired[DatasetsListResponseDatasetsItemSplits],
        "annotationCount": NotRequired[float],
        "totalBytes": NotRequired[float],
        "starCount": float,
        "isStarred": bool,
        "status": NotRequired[Literal["processing", "ready", "failed"]],
        "sampleImages": NotRequired[list[DatasetsListResponseDatasetsItemSampleImagesItem]],
        "storageProvider": NotRequired[Literal["gcs", "s3", "azure"]],
        "classColors": NotRequired[dict[str, str]],
        "kptShape": NotRequired[list[Any]],
        "flipIdx": NotRequired[list[int]],
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
        "description": NotRequired[str],
        "visibility": Literal["public", "private"],
        "task": Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"],
        "imageCount": float,
        "classCount": NotRequired[float],
        "classNames": NotRequired[list[str]],
        "format": NotRequired[Literal["yolo", "coco", "voc", "raw"]],
        "tags": NotRequired[list[str]],
        "license": NotRequired[
            Literal[
                "None",
                "CC0-1.0",
                "CC-BY-2.5",
                "CC-BY-4.0",
                "CC-BY-SA-4.0",
                "CC-BY-NC-4.0",
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
        "splits": NotRequired[DatasetsRetrieveResponseDatasetSplits],
        "annotationCount": NotRequired[float],
        "totalBytes": NotRequired[float],
        "starCount": float,
        "isStarred": bool,
        "status": NotRequired[Literal["processing", "ready", "failed"]],
        "sampleImages": NotRequired[list[DatasetsRetrieveResponseDatasetSampleImagesItem]],
        "storageProvider": NotRequired[Literal["gcs", "s3", "azure"]],
        "classColors": NotRequired[dict[str, str]],
        "kptShape": NotRequired[list[Any]],
        "flipIdx": NotRequired[list[int]],
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
        "sampleSize": NotRequired[float],
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


DatasetsRetrieveExportResponse = TypedDict(
    "DatasetsRetrieveExportResponse", {"downloadUrl": str, "version": NotRequired[int], "cached": NotRequired[bool]}
)


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
        "progress": DatasetsRetrieveEmbeddingsResponseActiveJobProgress,
        "createdAt": str,
    },
)


DatasetsRetrieveEmbeddingsResponse = TypedDict(
    "DatasetsRetrieveEmbeddingsResponse",
    {
        "analyzedAt": str | None,
        "embeddingsCount": int,
        "latestImageAt": str | None,
        "activeJob": DatasetsRetrieveEmbeddingsResponseActiveJob,
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


DatasetsCreateIconResponse = TypedDict("DatasetsCreateIconResponse", {"success": Literal[True], "downloadUrl": str})


DatasetsDeleteIconResponse = TypedDict("DatasetsDeleteIconResponse", {"success": Literal[True]})


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
        "modelCount": float,
        "modelNames": NotRequired[list[str]],
        "totalBytes": NotRequired[float],
        "starCount": float,
        "isStarred": bool,
        "archived": NotRequired[bool],
        "region": NotRequired[Literal["us", "eu", "ap"]],
        "task": NotRequired[Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"]],
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
        "starCount": float,
        "isStarred": bool,
        "archived": NotRequired[bool],
        "region": NotRequired[Literal["us", "eu", "ap"]],
        "task": NotRequired[Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"]],
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


ProjectsCreateIconResponse = TypedDict("ProjectsCreateIconResponse", {"success": Literal[True], "downloadUrl": str})


ProjectsDeleteIconResponse = TypedDict("ProjectsDeleteIconResponse", {"success": Literal[True]})


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
        "description": NotRequired[str],
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
        ],
        "datasetId": NotRequired[str],
        "datasetVersion": NotRequired[ModelsListResponseModelsItemDatasetVersion],
        "sourceModelId": NotRequired[str],
        "epochs": NotRequired[float],
        "bestEpoch": NotRequired[float],
        "bestFitness": NotRequired[float],
        "trainArgs": NotRequired[ModelsListResponseModelsItemTrainArgs],
        "version": NotRequired[str],
        "docs": NotRequired[str],
        "startedAt": NotRequired[str],
        "completedAt": NotRequired[str],
        "classNames": NotRequired[list[str]],
        "metrics": NotRequired[dict[str, float]],
        "trainResults": NotRequired[list[ModelsListResponseModelsItemTrainResultsItem]],
        "hasWeights": bool,
        "file": NotRequired[ModelsListResponseModelsItemFile],
        "plots": NotRequired[list[Any]],
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


ModelsListCompletedResponseModelsItem = TypedDict(
    "ModelsListCompletedResponseModelsItem",
    {
        "_id": str,
        "slug": str,
        "name": str,
        "task": Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"],
        "projectSlug": str,
        "projectName": str,
        "projectIconColor": NotRequired[str],
        "projectIconLetter": NotRequired[str],
        "bestFitness": NotRequired[float],
    },
)


ModelsListCompletedResponse = TypedDict(
    "ModelsListCompletedResponse", {"models": list[ModelsListCompletedResponseModelsItem]}
)


ModelsRetrieveResponseModelDatasetVersion = TypedDict(
    "ModelsRetrieveResponseModelDatasetVersion", {"version": float, "contentHash": str}
)


ModelsRetrieveResponseModelTrainArgs = TypedDict(
    "ModelsRetrieveResponseModelTrainArgs",
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


ModelsRetrieveResponseModelTrainResultsItem = TypedDict(
    "ModelsRetrieveResponseModelTrainResultsItem",
    {
        "epoch": NotRequired[float],
        "metrics": NotRequired[dict[str, float]],
        "fitness": NotRequired[float],
        "timestamp": NotRequired[str],
    },
)


ModelsRetrieveResponseModelFile = TypedDict("ModelsRetrieveResponseModelFile", {"size": float})


ModelsRetrieveResponseModelTrainingError = TypedDict(
    "ModelsRetrieveResponseModelTrainingError", {"message": str, "code": NotRequired[str], "timestamp": str}
)


ModelsRetrieveResponseModelSourceModel = TypedDict(
    "ModelsRetrieveResponseModelSourceModel",
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


ModelsRetrieveResponseModel = TypedDict(
    "ModelsRetrieveResponseModel",
    {
        "_id": str,
        "username": NotRequired[str],
        "projectId": NotRequired[str],
        "projectSlug": NotRequired[str],
        "slug": NotRequired[str],
        "name": str,
        "description": NotRequired[str],
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
        ],
        "datasetId": NotRequired[str],
        "datasetVersion": NotRequired[ModelsRetrieveResponseModelDatasetVersion],
        "sourceModelId": NotRequired[str],
        "epochs": NotRequired[float],
        "bestEpoch": NotRequired[float],
        "bestFitness": NotRequired[float],
        "trainArgs": NotRequired[ModelsRetrieveResponseModelTrainArgs],
        "version": NotRequired[str],
        "docs": NotRequired[str],
        "startedAt": NotRequired[str],
        "completedAt": NotRequired[str],
        "classNames": NotRequired[list[str]],
        "metrics": NotRequired[dict[str, float]],
        "trainResults": NotRequired[list[ModelsRetrieveResponseModelTrainResultsItem]],
        "hasWeights": bool,
        "file": NotRequired[ModelsRetrieveResponseModelFile],
        "plots": NotRequired[list[Any]],
        "trainingError": NotRequired[ModelsRetrieveResponseModelTrainingError],
        "starCount": float,
        "isStarred": bool,
        "clonedFrom": NotRequired[str],
        "downloadCount": NotRequired[float],
        "cloneCount": NotRequired[float],
        "createdAt": NotRequired[str],
        "updatedAt": NotRequired[str],
        "sourceModel": NotRequired[ModelsRetrieveResponseModelSourceModel],
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
        ],
    },
)


ModelsRetrieveResponseAnalysisCoverage = TypedDict(
    "ModelsRetrieveResponseAnalysisCoverage",
    {
        "mode": Literal["full", "sampled", "tails", "partial", "unavailable"],
        "omittedMiddle": int,
        "unmatchedExtremes": int,
    },
)


ModelsRetrieveResponseAnalysisScatterSample = TypedDict(
    "ModelsRetrieveResponseAnalysisScatterSample", {"eligible": int, "rows": list[list[Any]]}
)


ModelsRetrieveResponseAnalysisCohortsWorstMetricsF1 = TypedDict(
    "ModelsRetrieveResponseAnalysisCohortsWorstMetricsF1",
    {"count": int, "min": float, "p25": float, "median": float, "p75": float, "max": float, "mean": float},
)


ModelsRetrieveResponseAnalysisCohortsWorstMetrics = TypedDict(
    "ModelsRetrieveResponseAnalysisCohortsWorstMetrics",
    {"tp": int, "fp": int, "fn": int, "f1": ModelsRetrieveResponseAnalysisCohortsWorstMetricsF1},
)


ModelsRetrieveResponseAnalysisCohortsWorstExamplesItemLabelsItem = TypedDict(
    "ModelsRetrieveResponseAnalysisCohortsWorstExamplesItemLabelsItem",
    {
        "classId": int,
        "bbox": NotRequired[list[Any]],
        "segments": NotRequired[list[float]],
        "keypoints": NotRequired[list[float]],
        "obb": NotRequired[list[Any]],
        "skeletonId": NotRequired[str],
    },
)


ModelsRetrieveResponseAnalysisCohortsWorstExamplesItem = TypedDict(
    "ModelsRetrieveResponseAnalysisCohortsWorstExamplesItem",
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
        "labels": NotRequired[list[ModelsRetrieveResponseAnalysisCohortsWorstExamplesItemLabelsItem]],
    },
)


ModelsRetrieveResponseAnalysisCohortsWorst = TypedDict(
    "ModelsRetrieveResponseAnalysisCohortsWorst",
    {
        "count": int,
        "matched": int,
        "metrics": ModelsRetrieveResponseAnalysisCohortsWorstMetrics,
        "examples": list[ModelsRetrieveResponseAnalysisCohortsWorstExamplesItem],
    },
)


ModelsRetrieveResponseAnalysisCohortsBestMetricsF1 = TypedDict(
    "ModelsRetrieveResponseAnalysisCohortsBestMetricsF1",
    {"count": int, "min": float, "p25": float, "median": float, "p75": float, "max": float, "mean": float},
)


ModelsRetrieveResponseAnalysisCohortsBestMetrics = TypedDict(
    "ModelsRetrieveResponseAnalysisCohortsBestMetrics",
    {"tp": int, "fp": int, "fn": int, "f1": ModelsRetrieveResponseAnalysisCohortsBestMetricsF1},
)


ModelsRetrieveResponseAnalysisCohortsBestExamplesItemLabelsItem = TypedDict(
    "ModelsRetrieveResponseAnalysisCohortsBestExamplesItemLabelsItem",
    {
        "classId": int,
        "bbox": NotRequired[list[Any]],
        "segments": NotRequired[list[float]],
        "keypoints": NotRequired[list[float]],
        "obb": NotRequired[list[Any]],
        "skeletonId": NotRequired[str],
    },
)


ModelsRetrieveResponseAnalysisCohortsBestExamplesItem = TypedDict(
    "ModelsRetrieveResponseAnalysisCohortsBestExamplesItem",
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
        "labels": NotRequired[list[ModelsRetrieveResponseAnalysisCohortsBestExamplesItemLabelsItem]],
    },
)


ModelsRetrieveResponseAnalysisCohortsBest = TypedDict(
    "ModelsRetrieveResponseAnalysisCohortsBest",
    {
        "count": int,
        "matched": int,
        "metrics": ModelsRetrieveResponseAnalysisCohortsBestMetrics,
        "examples": list[ModelsRetrieveResponseAnalysisCohortsBestExamplesItem],
    },
)


ModelsRetrieveResponseAnalysisCohorts = TypedDict(
    "ModelsRetrieveResponseAnalysisCohorts",
    {"worst": ModelsRetrieveResponseAnalysisCohortsWorst, "best": ModelsRetrieveResponseAnalysisCohortsBest},
)


ModelsRetrieveResponseAnalysisComparisonsWidthWorst = TypedDict(
    "ModelsRetrieveResponseAnalysisComparisonsWidthWorst",
    {"count": int, "min": float, "p25": float, "median": float, "p75": float, "max": float, "mean": float},
)


ModelsRetrieveResponseAnalysisComparisonsWidthBest = TypedDict(
    "ModelsRetrieveResponseAnalysisComparisonsWidthBest",
    {"count": int, "min": float, "p25": float, "median": float, "p75": float, "max": float, "mean": float},
)


ModelsRetrieveResponseAnalysisComparisonsWidthRelationshipFit = TypedDict(
    "ModelsRetrieveResponseAnalysisComparisonsWidthRelationshipFit",
    {"slope": float, "intercept": float, "pearsonR": float, "rSquared": float},
)


ModelsRetrieveResponseAnalysisComparisonsWidthRelationshipCovariance = TypedDict(
    "ModelsRetrieveResponseAnalysisComparisonsWidthRelationshipCovariance",
    {"mean": list[Any], "eigenvalues": list[Any], "eigenvectors": list[Any]},
)


ModelsRetrieveResponseAnalysisComparisonsWidthRelationship = TypedDict(
    "ModelsRetrieveResponseAnalysisComparisonsWidthRelationship",
    {
        "count": int,
        "fit": ModelsRetrieveResponseAnalysisComparisonsWidthRelationshipFit,
        "covariance": ModelsRetrieveResponseAnalysisComparisonsWidthRelationshipCovariance,
    },
)


ModelsRetrieveResponseAnalysisComparisonsWidth = TypedDict(
    "ModelsRetrieveResponseAnalysisComparisonsWidth",
    {
        "worst": ModelsRetrieveResponseAnalysisComparisonsWidthWorst,
        "best": ModelsRetrieveResponseAnalysisComparisonsWidthBest,
        "relationship": ModelsRetrieveResponseAnalysisComparisonsWidthRelationship,
    },
)


ModelsRetrieveResponseAnalysisComparisonsHeightWorst = TypedDict(
    "ModelsRetrieveResponseAnalysisComparisonsHeightWorst",
    {"count": int, "min": float, "p25": float, "median": float, "p75": float, "max": float, "mean": float},
)


ModelsRetrieveResponseAnalysisComparisonsHeightBest = TypedDict(
    "ModelsRetrieveResponseAnalysisComparisonsHeightBest",
    {"count": int, "min": float, "p25": float, "median": float, "p75": float, "max": float, "mean": float},
)


ModelsRetrieveResponseAnalysisComparisonsHeightRelationshipFit = TypedDict(
    "ModelsRetrieveResponseAnalysisComparisonsHeightRelationshipFit",
    {"slope": float, "intercept": float, "pearsonR": float, "rSquared": float},
)


ModelsRetrieveResponseAnalysisComparisonsHeightRelationshipCovariance = TypedDict(
    "ModelsRetrieveResponseAnalysisComparisonsHeightRelationshipCovariance",
    {"mean": list[Any], "eigenvalues": list[Any], "eigenvectors": list[Any]},
)


ModelsRetrieveResponseAnalysisComparisonsHeightRelationship = TypedDict(
    "ModelsRetrieveResponseAnalysisComparisonsHeightRelationship",
    {
        "count": int,
        "fit": ModelsRetrieveResponseAnalysisComparisonsHeightRelationshipFit,
        "covariance": ModelsRetrieveResponseAnalysisComparisonsHeightRelationshipCovariance,
    },
)


ModelsRetrieveResponseAnalysisComparisonsHeight = TypedDict(
    "ModelsRetrieveResponseAnalysisComparisonsHeight",
    {
        "worst": ModelsRetrieveResponseAnalysisComparisonsHeightWorst,
        "best": ModelsRetrieveResponseAnalysisComparisonsHeightBest,
        "relationship": ModelsRetrieveResponseAnalysisComparisonsHeightRelationship,
    },
)


ModelsRetrieveResponseAnalysisComparisonsPixelsWorst = TypedDict(
    "ModelsRetrieveResponseAnalysisComparisonsPixelsWorst",
    {"count": int, "min": float, "p25": float, "median": float, "p75": float, "max": float, "mean": float},
)


ModelsRetrieveResponseAnalysisComparisonsPixelsBest = TypedDict(
    "ModelsRetrieveResponseAnalysisComparisonsPixelsBest",
    {"count": int, "min": float, "p25": float, "median": float, "p75": float, "max": float, "mean": float},
)


ModelsRetrieveResponseAnalysisComparisonsPixelsRelationshipFit = TypedDict(
    "ModelsRetrieveResponseAnalysisComparisonsPixelsRelationshipFit",
    {"slope": float, "intercept": float, "pearsonR": float, "rSquared": float},
)


ModelsRetrieveResponseAnalysisComparisonsPixelsRelationshipCovariance = TypedDict(
    "ModelsRetrieveResponseAnalysisComparisonsPixelsRelationshipCovariance",
    {"mean": list[Any], "eigenvalues": list[Any], "eigenvectors": list[Any]},
)


ModelsRetrieveResponseAnalysisComparisonsPixelsRelationship = TypedDict(
    "ModelsRetrieveResponseAnalysisComparisonsPixelsRelationship",
    {
        "count": int,
        "fit": ModelsRetrieveResponseAnalysisComparisonsPixelsRelationshipFit,
        "covariance": ModelsRetrieveResponseAnalysisComparisonsPixelsRelationshipCovariance,
    },
)


ModelsRetrieveResponseAnalysisComparisonsPixels = TypedDict(
    "ModelsRetrieveResponseAnalysisComparisonsPixels",
    {
        "worst": ModelsRetrieveResponseAnalysisComparisonsPixelsWorst,
        "best": ModelsRetrieveResponseAnalysisComparisonsPixelsBest,
        "relationship": ModelsRetrieveResponseAnalysisComparisonsPixelsRelationship,
    },
)


ModelsRetrieveResponseAnalysisComparisonsAspectRatioWorst = TypedDict(
    "ModelsRetrieveResponseAnalysisComparisonsAspectRatioWorst",
    {"count": int, "min": float, "p25": float, "median": float, "p75": float, "max": float, "mean": float},
)


ModelsRetrieveResponseAnalysisComparisonsAspectRatioBest = TypedDict(
    "ModelsRetrieveResponseAnalysisComparisonsAspectRatioBest",
    {"count": int, "min": float, "p25": float, "median": float, "p75": float, "max": float, "mean": float},
)


ModelsRetrieveResponseAnalysisComparisonsAspectRatioRelationshipFit = TypedDict(
    "ModelsRetrieveResponseAnalysisComparisonsAspectRatioRelationshipFit",
    {"slope": float, "intercept": float, "pearsonR": float, "rSquared": float},
)


ModelsRetrieveResponseAnalysisComparisonsAspectRatioRelationshipCovariance = TypedDict(
    "ModelsRetrieveResponseAnalysisComparisonsAspectRatioRelationshipCovariance",
    {"mean": list[Any], "eigenvalues": list[Any], "eigenvectors": list[Any]},
)


ModelsRetrieveResponseAnalysisComparisonsAspectRatioRelationship = TypedDict(
    "ModelsRetrieveResponseAnalysisComparisonsAspectRatioRelationship",
    {
        "count": int,
        "fit": ModelsRetrieveResponseAnalysisComparisonsAspectRatioRelationshipFit,
        "covariance": ModelsRetrieveResponseAnalysisComparisonsAspectRatioRelationshipCovariance,
    },
)


ModelsRetrieveResponseAnalysisComparisonsAspectRatio = TypedDict(
    "ModelsRetrieveResponseAnalysisComparisonsAspectRatio",
    {
        "worst": ModelsRetrieveResponseAnalysisComparisonsAspectRatioWorst,
        "best": ModelsRetrieveResponseAnalysisComparisonsAspectRatioBest,
        "relationship": ModelsRetrieveResponseAnalysisComparisonsAspectRatioRelationship,
    },
)


ModelsRetrieveResponseAnalysisComparisonsInstanceCountWorst = TypedDict(
    "ModelsRetrieveResponseAnalysisComparisonsInstanceCountWorst",
    {"count": int, "min": float, "p25": float, "median": float, "p75": float, "max": float, "mean": float},
)


ModelsRetrieveResponseAnalysisComparisonsInstanceCountBest = TypedDict(
    "ModelsRetrieveResponseAnalysisComparisonsInstanceCountBest",
    {"count": int, "min": float, "p25": float, "median": float, "p75": float, "max": float, "mean": float},
)


ModelsRetrieveResponseAnalysisComparisonsInstanceCountRelationshipFit = TypedDict(
    "ModelsRetrieveResponseAnalysisComparisonsInstanceCountRelationshipFit",
    {"slope": float, "intercept": float, "pearsonR": float, "rSquared": float},
)


ModelsRetrieveResponseAnalysisComparisonsInstanceCountRelationshipCovariance = TypedDict(
    "ModelsRetrieveResponseAnalysisComparisonsInstanceCountRelationshipCovariance",
    {"mean": list[Any], "eigenvalues": list[Any], "eigenvectors": list[Any]},
)


ModelsRetrieveResponseAnalysisComparisonsInstanceCountRelationship = TypedDict(
    "ModelsRetrieveResponseAnalysisComparisonsInstanceCountRelationship",
    {
        "count": int,
        "fit": ModelsRetrieveResponseAnalysisComparisonsInstanceCountRelationshipFit,
        "covariance": ModelsRetrieveResponseAnalysisComparisonsInstanceCountRelationshipCovariance,
    },
)


ModelsRetrieveResponseAnalysisComparisonsInstanceCount = TypedDict(
    "ModelsRetrieveResponseAnalysisComparisonsInstanceCount",
    {
        "worst": ModelsRetrieveResponseAnalysisComparisonsInstanceCountWorst,
        "best": ModelsRetrieveResponseAnalysisComparisonsInstanceCountBest,
        "relationship": ModelsRetrieveResponseAnalysisComparisonsInstanceCountRelationship,
    },
)


ModelsRetrieveResponseAnalysisComparisonsClassPresenceItemWorst = TypedDict(
    "ModelsRetrieveResponseAnalysisComparisonsClassPresenceItemWorst", {"count": int, "prevalence": float}
)


ModelsRetrieveResponseAnalysisComparisonsClassPresenceItemBest = TypedDict(
    "ModelsRetrieveResponseAnalysisComparisonsClassPresenceItemBest", {"count": int, "prevalence": float}
)


ModelsRetrieveResponseAnalysisComparisonsClassPresenceItem = TypedDict(
    "ModelsRetrieveResponseAnalysisComparisonsClassPresenceItem",
    {
        "classId": int,
        "name": str,
        "worst": ModelsRetrieveResponseAnalysisComparisonsClassPresenceItemWorst,
        "best": ModelsRetrieveResponseAnalysisComparisonsClassPresenceItemBest,
        "prevalenceDifference": float,
    },
)


ModelsRetrieveResponseAnalysisComparisons = TypedDict(
    "ModelsRetrieveResponseAnalysisComparisons",
    {
        "width": ModelsRetrieveResponseAnalysisComparisonsWidth,
        "height": ModelsRetrieveResponseAnalysisComparisonsHeight,
        "pixels": ModelsRetrieveResponseAnalysisComparisonsPixels,
        "aspectRatio": ModelsRetrieveResponseAnalysisComparisonsAspectRatio,
        "instanceCount": ModelsRetrieveResponseAnalysisComparisonsInstanceCount,
        "classPresence": list[ModelsRetrieveResponseAnalysisComparisonsClassPresenceItem],
        "classPresenceTruncated": bool,
    },
)


ModelsRetrieveResponseAnalysis = TypedDict(
    "ModelsRetrieveResponseAnalysis",
    {
        "population": int,
        "retained": int,
        "matched": int,
        "unmatched": int,
        "traitsAvailable": bool,
        "sourceSplit": Literal["train", "val"] | None,
        "coverage": ModelsRetrieveResponseAnalysisCoverage,
        "scatterSample": ModelsRetrieveResponseAnalysisScatterSample,
        "cohorts": ModelsRetrieveResponseAnalysisCohorts,
        "comparisons": ModelsRetrieveResponseAnalysisComparisons,
    },
)


ModelsRetrieveResponse = TypedDict(
    "ModelsRetrieveResponse",
    {
        "model": NotRequired[ModelsRetrieveResponseModel],
        "isOwner": NotRequired[bool],
        "analysis": NotRequired[ModelsRetrieveResponseAnalysis],
    },
)


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
    {"model": NotRequired[str], "epochs": NotRequired[float], "batch": NotRequired[float], "imgsz": NotRequired[float]},
)


ModelsRetrieveTrainingResponseJob = TypedDict(
    "ModelsRetrieveTrainingResponseJob",
    {
        "id": str,
        "status": Literal["pending", "untrained", "starting", "running", "completed", "failed", "cancelled"],
        "progress": ModelsRetrieveTrainingResponseJobProgress,
        "timing": ModelsRetrieveTrainingResponseJobTiming,
        "compute": ModelsRetrieveTrainingResponseJobCompute,
        "trainArgs": ModelsRetrieveTrainingResponseJobTrainArgs,
        "epochMetrics": dict[str, Any] | None,
        "error": Any | None,
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
        "job": ModelsRetrieveTrainingResponseJob,
        "instanceStatus": NotRequired[ModelsRetrieveTrainingResponseInstanceStatus],
    },
)


ModelsDeleteTrainingResponse = TypedDict(
    "ModelsDeleteTrainingResponse",
    {"success": Literal[True], "status": Literal["cancelled"], "warning": NotRequired[str]},
)


ModelsTrackDownloadResponse = TypedDict("ModelsTrackDownloadResponse", {"success": Literal[True]})


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


ExportsTrackDownloadResponse = TypedDict("ExportsTrackDownloadResponse", {"success": Literal[True]})


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
        "statusMessage": NotRequired[str],
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


DeploymentsRetrieveMetricsResponseTimeRange = TypedDict(
    "DeploymentsRetrieveMetricsResponseTimeRange", {"start": str, "end": str}
)


DeploymentsRetrieveMetricsResponseSummary = TypedDict(
    "DeploymentsRetrieveMetricsResponseSummary",
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


DeploymentsRetrieveMetricsResponseTimeSeriesRequestsItem = TypedDict(
    "DeploymentsRetrieveMetricsResponseTimeSeriesRequestsItem", {"timestamp": str, "value": float}
)


DeploymentsRetrieveMetricsResponseTimeSeriesErrorsItem = TypedDict(
    "DeploymentsRetrieveMetricsResponseTimeSeriesErrorsItem", {"timestamp": str, "value": float}
)


DeploymentsRetrieveMetricsResponseTimeSeriesLatencyP50Item = TypedDict(
    "DeploymentsRetrieveMetricsResponseTimeSeriesLatencyP50Item", {"timestamp": str, "value": float}
)


DeploymentsRetrieveMetricsResponseTimeSeriesLatencyP95Item = TypedDict(
    "DeploymentsRetrieveMetricsResponseTimeSeriesLatencyP95Item", {"timestamp": str, "value": float}
)


DeploymentsRetrieveMetricsResponseTimeSeriesCpuUtilizationItem = TypedDict(
    "DeploymentsRetrieveMetricsResponseTimeSeriesCpuUtilizationItem", {"timestamp": str, "value": float}
)


DeploymentsRetrieveMetricsResponseTimeSeriesMemoryUtilizationItem = TypedDict(
    "DeploymentsRetrieveMetricsResponseTimeSeriesMemoryUtilizationItem", {"timestamp": str, "value": float}
)


DeploymentsRetrieveMetricsResponseTimeSeriesInstanceCountItem = TypedDict(
    "DeploymentsRetrieveMetricsResponseTimeSeriesInstanceCountItem", {"timestamp": str, "value": float}
)


DeploymentsRetrieveMetricsResponseTimeSeries = TypedDict(
    "DeploymentsRetrieveMetricsResponseTimeSeries",
    {
        "requests": list[DeploymentsRetrieveMetricsResponseTimeSeriesRequestsItem],
        "errors": list[DeploymentsRetrieveMetricsResponseTimeSeriesErrorsItem],
        "latencyP50": list[DeploymentsRetrieveMetricsResponseTimeSeriesLatencyP50Item],
        "latencyP95": list[DeploymentsRetrieveMetricsResponseTimeSeriesLatencyP95Item],
        "cpuUtilization": list[DeploymentsRetrieveMetricsResponseTimeSeriesCpuUtilizationItem],
        "memoryUtilization": list[DeploymentsRetrieveMetricsResponseTimeSeriesMemoryUtilizationItem],
        "instanceCount": list[DeploymentsRetrieveMetricsResponseTimeSeriesInstanceCountItem],
    },
)


DeploymentsRetrieveMetricsResponse = TypedDict(
    "DeploymentsRetrieveMetricsResponse",
    {
        "deploymentId": NotRequired[str],
        "region": NotRequired[str],
        "timeRange": NotRequired[DeploymentsRetrieveMetricsResponseTimeRange],
        "summary": NotRequired[DeploymentsRetrieveMetricsResponseSummary],
        "timeSeries": NotRequired[DeploymentsRetrieveMetricsResponseTimeSeries],
        "requests24h": NotRequired[list[float]],
        "totalRequests": NotRequired[float],
        "errorRate": NotRequired[float],
        "avgLatencyMs": NotRequired[float],
    },
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


AccountRetrieveSummaryResponseCounts = TypedDict(
    "AccountRetrieveSummaryResponseCounts", {"projects": int, "datasets": int, "models": int}
)


AccountRetrieveSummaryResponseTeamsItem = TypedDict(
    "AccountRetrieveSummaryResponseTeamsItem", {"username": str, "fullName": NotRequired[str], "role": str}
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


AccountCreateApiKeyResponse = TypedDict(
    "AccountCreateApiKeyResponse", {"keyId": str, "key": str, "keyPrefix": str, "name": str, "createdAt": str}
)


AccountRevokeApiKeyResponse = TypedDict("AccountRevokeApiKeyResponse", {"deleted": Literal[True], "keyId": str})


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


AccountRetrieveProfileSettingsResponseSocials = TypedDict(
    "AccountRetrieveProfileSettingsResponseSocials",
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


AccountRetrieveProfileSettingsResponse = TypedDict(
    "AccountRetrieveProfileSettingsResponse",
    {
        "displayName": str,
        "company": str,
        "useCase": str,
        "bio": str,
        "socials": NotRequired[AccountRetrieveProfileSettingsResponseSocials],
        "plan": Literal["free", "pro", "enterprise"],
        "username": str,
        "email": str,
        "imageUrl": str,
        "accountType": Literal["personal", "team"],
        "iconColor": NotRequired[str],
        "iconLetter": NotRequired[str],
        "region": Literal["us", "eu", "ap"],
    },
)


AccountUpdateProfileSettingsResponse = TypedDict("AccountUpdateProfileSettingsResponse", {"success": Literal[True]})


AccountListCloudStorageIntegrationsResponseIntegrationsItem = TypedDict(
    "AccountListCloudStorageIntegrationsResponseIntegrationsItem",
    {
        "id": str,
        "provider": Literal["gcs", "s3", "azure"],
        "credentialIdentity": str,
        "targets": list[str],
        "createdAt": str,
    },
)


AccountListCloudStorageIntegrationsResponse = TypedDict(
    "AccountListCloudStorageIntegrationsResponse",
    {"integrations": list[AccountListCloudStorageIntegrationsResponseIntegrationsItem]},
)


AccountConnectCloudStorageResponse = TypedDict(
    "AccountConnectCloudStorageResponse",
    {
        "id": str,
        "provider": Literal["gcs", "s3", "azure"],
        "credentialIdentity": str,
        "targets": list[str],
        "createdAt": str,
    },
)


AccountDiscoverCloudStorageLocationsResponse = TypedDict(
    "AccountDiscoverCloudStorageLocationsResponse", {"targets": list[str]}
)


AccountBrowseCloudStorageObjectsResponseEntriesItem = TypedDict(
    "AccountBrowseCloudStorageObjectsResponseEntriesItem",
    {
        "kind": Literal["folder", "file"],
        "name": str,
        "key": str,
        "size": NotRequired[float],
        "updatedAt": NotRequired[str],
    },
)


AccountBrowseCloudStorageObjectsResponse = TypedDict(
    "AccountBrowseCloudStorageObjectsResponse",
    {"entries": list[AccountBrowseCloudStorageObjectsResponseEntriesItem], "cursor": NotRequired[str]},
)


AccountRetrieveTrashResponseItemsItemParentProject = TypedDict(
    "AccountRetrieveTrashResponseItemsItemParentProject", {"_id": str, "name": str, "slug": str}
)


AccountRetrieveTrashResponseItemsItem = TypedDict(
    "AccountRetrieveTrashResponseItemsItem",
    {
        "_id": str,
        "type": Literal["project", "dataset", "model"],
        "name": str,
        "slug": str,
        "trashedAt": str,
        "daysRemaining": int,
        "cascadedCount": NotRequired[int],
        "parentProject": NotRequired[AccountRetrieveTrashResponseItemsItemParentProject],
        "sizeBytes": NotRequired[float],
    },
)


AccountRetrieveTrashResponseSummaryByTypeProjects = TypedDict(
    "AccountRetrieveTrashResponseSummaryByTypeProjects", {"count": int}
)


AccountRetrieveTrashResponseSummaryByTypeDatasets = TypedDict(
    "AccountRetrieveTrashResponseSummaryByTypeDatasets", {"count": int, "sizeBytes": float}
)


AccountRetrieveTrashResponseSummaryByTypeModels = TypedDict(
    "AccountRetrieveTrashResponseSummaryByTypeModels", {"count": int, "sizeBytes": float}
)


AccountRetrieveTrashResponseSummaryByTypeExports = TypedDict(
    "AccountRetrieveTrashResponseSummaryByTypeExports", {"count": int, "sizeBytes": float}
)


AccountRetrieveTrashResponseSummaryByType = TypedDict(
    "AccountRetrieveTrashResponseSummaryByType",
    {
        "projects": AccountRetrieveTrashResponseSummaryByTypeProjects,
        "datasets": AccountRetrieveTrashResponseSummaryByTypeDatasets,
        "models": AccountRetrieveTrashResponseSummaryByTypeModels,
        "exports": AccountRetrieveTrashResponseSummaryByTypeExports,
    },
)


AccountRetrieveTrashResponseSummary = TypedDict(
    "AccountRetrieveTrashResponseSummary",
    {"totalItems": int, "totalSizeBytes": float, "byType": AccountRetrieveTrashResponseSummaryByType},
)


AccountRetrieveTrashResponse = TypedDict(
    "AccountRetrieveTrashResponse",
    {
        "items": list[AccountRetrieveTrashResponseItemsItem],
        "total": float,
        "page": int,
        "limit": int,
        "totalPages": int,
        "summary": AccountRetrieveTrashResponseSummary,
        "region": Literal["us", "eu", "ap"],
    },
)


AccountRestoreTrashedItemResponse = TypedDict(
    "AccountRestoreTrashedItemResponse", {"success": Literal[True], "restoredModels": NotRequired[int]}
)


AccountPermanentlyDeleteTrashedItemResponse = TypedDict(
    "AccountPermanentlyDeleteTrashedItemResponse",
    {"success": Literal[True], "deletedCount": int, "cascadedModels": NotRequired[int]},
)


AccountPermanentlyDeleteAllTrashedItemsResponseDeleted = TypedDict(
    "AccountPermanentlyDeleteAllTrashedItemsResponseDeleted",
    {"projects": int, "datasets": int, "models": int, "deployments": int},
)


AccountPermanentlyDeleteAllTrashedItemsResponse = TypedDict(
    "AccountPermanentlyDeleteAllTrashedItemsResponse",
    {"success": Literal[True], "deleted": AccountPermanentlyDeleteAllTrashedItemsResponseDeleted, "totalDeleted": int},
)


AccountRetrieveIfUsernameIsAvailableResponse = TypedDict(
    "AccountRetrieveIfUsernameIsAvailableResponse", {"available": bool, "username": str}
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


AccountFollowOrUnfollowUserResponse = TypedDict(
    "AccountFollowOrUnfollowUserResponse", {"followed": bool, "followerCount": int}
)


AccountUploadWorkspaceIconResponse = TypedDict(
    "AccountUploadWorkspaceIconResponse", {"success": Literal[True], "downloadUrl": str}
)


AccountDeleteWorkspaceIconResponse = TypedDict("AccountDeleteWorkspaceIconResponse", {"success": Literal[True]})


BillingRetrieveBalanceResponse = TypedDict(
    "BillingRetrieveBalanceResponse", {"creditsCents": float, "plan": Literal["free", "pro", "enterprise"]}
)


BillingListTransactionsResponseTransactionsItemModel = TypedDict(
    "BillingListTransactionsResponseTransactionsItemModel",
    {"name": str, "slug": str, "projectSlug": str, "username": str},
)


BillingListTransactionsResponseTransactionsItem = TypedDict(
    "BillingListTransactionsResponseTransactionsItem",
    {
        "type": str,
        "amountCents": float,
        "balanceAfter": float,
        "modelId": NotRequired[str],
        "period": NotRequired[str],
        "createdAt": str,
        "receiptUrl": NotRequired[str | None],
        "model": NotRequired[BillingListTransactionsResponseTransactionsItemModel],
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


ActivityListResponseEventsItem = TypedDict(
    "ActivityListResponseEventsItem",
    {
        "_id": str,
        "userId": str,
        "userEmail": str,
        "userName": str,
        "action": Literal[
            "created",
            "updated",
            "deleted",
            "trashed",
            "restored",
            "started",
            "completed",
            "failed",
            "cancelled",
            "uploaded",
            "shared",
            "unshared",
            "exported",
            "cloned",
            "analyzed",
        ],
        "resourceType": Literal[
            "project", "dataset", "model", "training", "export", "deployment", "settings", "onboarding", "api_key"
        ],
        "resourceId": NotRequired[str],
        "resourceName": NotRequired[str],
        "metadata": NotRequired[dict[str, Any]],
        "timestamp": str,
        "seen": bool,
        "archived": bool,
    },
)


ActivityListResponseFilters = TypedDict(
    "ActivityListResponseFilters",
    {"archived": bool, "search": NotRequired[str], "start": NotRequired[str], "end": NotRequired[str]},
)


ActivityListResponseActivityItem = TypedDict(
    "ActivityListResponseActivityItem",
    {
        "_id": str,
        "userId": str,
        "userEmail": str,
        "userName": str,
        "action": Literal[
            "created",
            "updated",
            "deleted",
            "trashed",
            "restored",
            "started",
            "completed",
            "failed",
            "cancelled",
            "uploaded",
            "shared",
            "unshared",
            "exported",
            "cloned",
            "analyzed",
        ],
        "resourceType": Literal[
            "project", "dataset", "model", "training", "export", "deployment", "settings", "onboarding", "api_key"
        ],
        "resourceId": NotRequired[str],
        "resourceName": NotRequired[str],
        "metadata": NotRequired[dict[str, Any]],
        "timestamp": str,
        "seen": bool,
        "archived": bool,
    },
)


ActivityListResponse = TypedDict(
    "ActivityListResponse",
    {
        "events": NotRequired[list[ActivityListResponseEventsItem]],
        "total": NotRequired[float],
        "unseenCount": NotRequired[float],
        "exportedAt": NotRequired[str],
        "app": NotRequired[Literal["alpha"]],
        "owner": NotRequired[str],
        "filters": NotRequired[ActivityListResponseFilters],
        "activity": NotRequired[list[ActivityListResponseActivityItem]],
    },
)


ActivityCreateMarkSeenResponse = TypedDict("ActivityCreateMarkSeenResponse", {"success": Literal[True]})


ActivityArchiveResponse = TypedDict("ActivityArchiveResponse", {"success": Literal[True]})


ExploreRetrieveSearchResponseProjectsItem = TypedDict(
    "ExploreRetrieveSearchResponseProjectsItem",
    {
        "_id": str,
        "slug": str,
        "name": str,
        "description": NotRequired[str],
        "username": str,
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
    "ExploreRetrieveSearchResponseDatasetsItemSplits", {"train": float, "val": float, "test": float, "labeled": float}
)


ExploreRetrieveSearchResponseDatasetsItemSampleImagesItemLabelsItem = TypedDict(
    "ExploreRetrieveSearchResponseDatasetsItemSampleImagesItemLabelsItem",
    {
        "classId": float,
        "bbox": NotRequired[list[float]],
        "segments": NotRequired[list[float]],
        "keypoints": NotRequired[list[float]],
        "obb": NotRequired[list[float]],
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
        "_id": str,
        "slug": str,
        "name": str,
        "description": NotRequired[str],
        "username": str,
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


ExploreRetrieveSidebarResponseProjectsItem = TypedDict(
    "ExploreRetrieveSidebarResponseProjectsItem",
    {
        "_id": str,
        "slug": str,
        "name": str,
        "modelCount": int,
        "iconColor": NotRequired[str],
        "iconLetter": NotRequired[str],
        "iconImage": NotRequired[str],
    },
)


ExploreRetrieveSidebarResponseDatasetsItem = TypedDict(
    "ExploreRetrieveSidebarResponseDatasetsItem",
    {"_id": str, "slug": str, "name": str, "imageCount": NotRequired[int], "thumbnail": NotRequired[str]},
)


ExploreRetrieveSidebarResponse = TypedDict(
    "ExploreRetrieveSidebarResponse",
    {
        "projects": list[ExploreRetrieveSidebarResponseProjectsItem],
        "datasets": list[ExploreRetrieveSidebarResponseDatasetsItem],
    },
)


UploadRetrieveFileUrlResponse = TypedDict(
    "UploadRetrieveFileUrlResponse", {"sessionId": str, "uploadUrl": str, "expiresAt": str}
)


UploadCompleteResponseFile = TypedDict("UploadCompleteResponseFile", {"size": float, "contentType": NotRequired[str]})


UploadCompleteResponse = TypedDict(
    "UploadCompleteResponse", {"success": Literal[True], "file": UploadCompleteResponseFile}
)


TeamsListResponseTeamsItem = TypedDict(
    "TeamsListResponseTeamsItem",
    {
        "userId": str,
        "username": str,
        "fullName": NotRequired[str],
        "imageUrl": NotRequired[str],
        "iconColor": NotRequired[str],
        "iconLetter": NotRequired[str],
        "plan": Literal["free", "pro", "enterprise"],
        "region": Literal["us", "eu", "ap"],
        "role": str,
        "deniedReason": NotRequired[str],
    },
)


TeamsListResponse = TypedDict("TeamsListResponse", {"teams": list[TeamsListResponseTeamsItem]})


TeamsCreateResponseTeam = TypedDict(
    "TeamsCreateResponseTeam",
    {
        "userId": str,
        "username": str,
        "fullName": str,
        "iconColor": str,
        "iconLetter": str,
        "plan": str,
        "region": str,
        "role": str,
    },
)


TeamsCreateResponse = TypedDict("TeamsCreateResponse", {"team": TeamsCreateResponseTeam})


TeamsListMembersResponseMembersItem = TypedDict(
    "TeamsListMembersResponseMembersItem",
    {
        "userId": NotRequired[str],
        "username": str,
        "email": str,
        "role": str,
        "status": Literal["pending", "active"],
        "joinedAt": str,
        "imageUrl": NotRequired[str],
        "invitedBy": NotRequired[str],
        "inviteId": NotRequired[str],
        "inviteCreatedAt": NotRequired[str],
    },
)


TeamsListMembersResponse = TypedDict(
    "TeamsListMembersResponse", {"members": list[TeamsListMembersResponseMembersItem], "maxSeats": float}
)


TeamsInviteResponse = TypedDict("TeamsInviteResponse", {"invited": Literal[True], "email": str})


TeamsChangeMemberRoleResponse = TypedDict("TeamsChangeMemberRoleResponse", {"success": Literal[True]})


TeamsRemoveMemberOrLeaveResponse = TypedDict("TeamsRemoveMemberOrLeaveResponse", {"success": Literal[True]})


TeamsTransferOwnershipResponse = TypedDict("TeamsTransferOwnershipResponse", {"success": Literal[True]})
