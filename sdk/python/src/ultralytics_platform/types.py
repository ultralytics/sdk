# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from __future__ import annotations

from typing import Any, Literal, NotRequired, TypedDict


class DatasetsListResponseDatasetsItemSplits(TypedDict):
    train: float
    val: float
    test: float
    labeled: float


class DatasetsListResponseDatasetsItemSampleImagesItemLabelsItem(TypedDict):
    classId: float
    bbox: NotRequired[list[float]]
    segments: NotRequired[list[float]]
    keypoints: NotRequired[list[float]]
    obb: NotRequired[list[float]]
    skeletonId: NotRequired[str]


class DatasetsListResponseDatasetsItemSampleImagesItem(TypedDict):
    url: str
    imageUrl: NotRequired[str]
    width: float
    height: float
    labels: NotRequired[list[DatasetsListResponseDatasetsItemSampleImagesItemLabelsItem]]


class DatasetsListResponseDatasetsItemProcessingError(TypedDict):
    message: str
    timestamp: str


class DatasetsListResponseDatasetsItemVersionsItemSplits(TypedDict):
    train: float
    val: float
    test: float
    labeled: float


class DatasetsListResponseDatasetsItemVersionsItem(TypedDict):
    version: float
    description: NotRequired[str]
    sizeBytes: NotRequired[float]
    contentHash: NotRequired[str]
    imageCount: float
    classCount: float
    annotationCount: float
    splits: DatasetsListResponseDatasetsItemVersionsItemSplits
    createdAt: str


class DatasetsListResponseDatasetsItem(TypedDict):
    _id: str
    username: str
    slug: str
    name: str
    description: NotRequired[str]
    visibility: Literal["public", "private"]
    task: Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"]
    imageCount: float
    classCount: NotRequired[float]
    classNames: NotRequired[list[str]]
    format: NotRequired[Literal["yolo", "coco", "voc", "raw"]]
    tags: NotRequired[list[str]]
    license: NotRequired[
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
    ]
    splits: NotRequired[DatasetsListResponseDatasetsItemSplits]
    annotationCount: NotRequired[float]
    totalBytes: NotRequired[float]
    starCount: float
    isStarred: bool
    status: NotRequired[Literal["processing", "ready", "failed"]]
    sampleImages: NotRequired[list[DatasetsListResponseDatasetsItemSampleImagesItem]]
    storageProvider: NotRequired[Literal["gcs", "s3", "azure"]]
    classColors: NotRequired[dict[str, str]]
    kptShape: NotRequired[list[Any]]
    flipIdx: NotRequired[list[int]]
    processingTimeMs: NotRequired[float]
    processingError: NotRequired[DatasetsListResponseDatasetsItemProcessingError]
    errorCount: NotRequired[float]
    iconColor: NotRequired[str]
    iconLetter: NotRequired[str]
    iconImage: NotRequired[str]
    clonedFrom: NotRequired[str]
    cloneCount: NotRequired[float]
    region: NotRequired[Literal["us", "eu", "ap"]]
    versions: NotRequired[list[DatasetsListResponseDatasetsItemVersionsItem]]
    createdAt: str
    updatedAt: str


class DatasetsListResponse(TypedDict):
    datasets: list[DatasetsListResponseDatasetsItem]
    total: float
    region: Literal["us", "eu", "ap"]


class DatasetsCreateResponse(TypedDict):
    projectId: NotRequired[str]
    datasetId: NotRequired[str]
    modelId: NotRequired[str]
    slug: str
    region: Literal["us", "eu", "ap"]


class DatasetsRetrieveResponseDatasetSplits(TypedDict):
    train: float
    val: float
    test: float
    labeled: float


class DatasetsRetrieveResponseDatasetSampleImagesItemLabelsItem(TypedDict):
    classId: float
    bbox: NotRequired[list[float]]
    segments: NotRequired[list[float]]
    keypoints: NotRequired[list[float]]
    obb: NotRequired[list[float]]
    skeletonId: NotRequired[str]


class DatasetsRetrieveResponseDatasetSampleImagesItem(TypedDict):
    url: str
    imageUrl: NotRequired[str]
    width: float
    height: float
    labels: NotRequired[list[DatasetsRetrieveResponseDatasetSampleImagesItemLabelsItem]]


class DatasetsRetrieveResponseDatasetProcessingError(TypedDict):
    message: str
    timestamp: str


class DatasetsRetrieveResponseDatasetVersionsItemSplits(TypedDict):
    train: float
    val: float
    test: float
    labeled: float


class DatasetsRetrieveResponseDatasetVersionsItem(TypedDict):
    version: float
    description: NotRequired[str]
    sizeBytes: NotRequired[float]
    contentHash: NotRequired[str]
    imageCount: float
    classCount: float
    annotationCount: float
    splits: DatasetsRetrieveResponseDatasetVersionsItemSplits
    createdAt: str


class DatasetsRetrieveResponseDataset(TypedDict):
    _id: str
    username: str
    slug: str
    name: str
    description: NotRequired[str]
    visibility: Literal["public", "private"]
    task: Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"]
    imageCount: float
    classCount: NotRequired[float]
    classNames: NotRequired[list[str]]
    format: NotRequired[Literal["yolo", "coco", "voc", "raw"]]
    tags: NotRequired[list[str]]
    license: NotRequired[
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
    ]
    splits: NotRequired[DatasetsRetrieveResponseDatasetSplits]
    annotationCount: NotRequired[float]
    totalBytes: NotRequired[float]
    starCount: float
    isStarred: bool
    status: NotRequired[Literal["processing", "ready", "failed"]]
    sampleImages: NotRequired[list[DatasetsRetrieveResponseDatasetSampleImagesItem]]
    storageProvider: NotRequired[Literal["gcs", "s3", "azure"]]
    classColors: NotRequired[dict[str, str]]
    kptShape: NotRequired[list[Any]]
    flipIdx: NotRequired[list[int]]
    processingTimeMs: NotRequired[float]
    processingError: NotRequired[DatasetsRetrieveResponseDatasetProcessingError]
    errorCount: NotRequired[float]
    iconColor: NotRequired[str]
    iconLetter: NotRequired[str]
    iconImage: NotRequired[str]
    clonedFrom: NotRequired[str]
    cloneCount: NotRequired[float]
    region: NotRequired[Literal["us", "eu", "ap"]]
    versions: NotRequired[list[DatasetsRetrieveResponseDatasetVersionsItem]]
    createdAt: str
    updatedAt: str


class DatasetsRetrieveResponse(TypedDict):
    dataset: DatasetsRetrieveResponseDataset


class DatasetsUpdateResponse(TypedDict):
    success: Literal[True]


class DatasetsDeleteResponse(TypedDict):
    success: Literal[True]


class DatasetsRetrieveMetadataResponse(TypedDict):
    metadata: dict[str, Any]
    properties: list[list[Any]]


class DatasetsCloneResponse(TypedDict):
    datasetId: str
    slug: str
    name: str
    imageCount: float
    classCount: NotRequired[float]
    region: Literal["us", "eu", "ap"]


class DatasetsRetrieveClassStatsResponseClassesItem(TypedDict):
    classId: float
    count: float
    imageCount: float


class DatasetsRetrieveClassStatsResponseImageStatsWidthHistogramItem(TypedDict):
    bin: float
    count: float
    size: NotRequired[float]


class DatasetsRetrieveClassStatsResponseImageStatsHeightHistogramItem(TypedDict):
    bin: float
    count: float
    size: NotRequired[float]


class DatasetsRetrieveClassStatsResponseImageStatsPointsHistogramItem(TypedDict):
    bin: float
    count: float
    size: NotRequired[float]


class DatasetsRetrieveClassStatsResponseImageStatsFileSizeHistogramItem(TypedDict):
    bin: float
    count: float
    size: NotRequired[float]


class DatasetsRetrieveClassStatsResponseImageStatsObjectsPerImageHistogramItem(TypedDict):
    bin: float
    count: float
    size: NotRequired[float]


class DatasetsRetrieveClassStatsResponseImageStatsBboxWidthHistogramItem(TypedDict):
    bin: float
    count: float
    size: NotRequired[float]


class DatasetsRetrieveClassStatsResponseImageStatsBboxHeightHistogramItem(TypedDict):
    bin: float
    count: float
    size: NotRequired[float]


class DatasetsRetrieveClassStatsResponseImageStatsBboxWidthNormHistogramItem(TypedDict):
    bin: float
    count: float
    size: NotRequired[float]


class DatasetsRetrieveClassStatsResponseImageStatsBboxHeightNormHistogramItem(TypedDict):
    bin: float
    count: float
    size: NotRequired[float]


class DatasetsRetrieveClassStatsResponseImageStats(TypedDict):
    widthHistogram: list[DatasetsRetrieveClassStatsResponseImageStatsWidthHistogramItem]
    heightHistogram: list[DatasetsRetrieveClassStatsResponseImageStatsHeightHistogramItem]
    pointsHistogram: list[DatasetsRetrieveClassStatsResponseImageStatsPointsHistogramItem]
    formatDistribution: dict[str, float]
    fileSizeHistogram: list[DatasetsRetrieveClassStatsResponseImageStatsFileSizeHistogramItem]
    objectsPerImageHistogram: list[DatasetsRetrieveClassStatsResponseImageStatsObjectsPerImageHistogramItem]
    bboxWidthHistogram: list[DatasetsRetrieveClassStatsResponseImageStatsBboxWidthHistogramItem]
    bboxHeightHistogram: list[DatasetsRetrieveClassStatsResponseImageStatsBboxHeightHistogramItem]
    bboxWidthNormHistogram: list[DatasetsRetrieveClassStatsResponseImageStatsBboxWidthNormHistogramItem]
    bboxHeightNormHistogram: list[DatasetsRetrieveClassStatsResponseImageStatsBboxHeightNormHistogramItem]


class DatasetsRetrieveClassStatsResponseLocationHeatmap(TypedDict):
    bins: list[list[float]]
    maxCount: float


class DatasetsRetrieveClassStatsResponseDimensionHeatmap(TypedDict):
    bins: list[list[float]]
    maxCount: float
    minWidth: float
    maxWidth: float
    minHeight: float
    maxHeight: float


class DatasetsRetrieveClassStatsResponse(TypedDict):
    classes: list[DatasetsRetrieveClassStatsResponseClassesItem]
    imageStats: DatasetsRetrieveClassStatsResponseImageStats
    locationHeatmap: DatasetsRetrieveClassStatsResponseLocationHeatmap
    dimensionHeatmap: DatasetsRetrieveClassStatsResponseDimensionHeatmap
    classNames: list[str]
    cached: bool
    sampleSize: NotRequired[float]


class DatasetsMergeClassesResponse(TypedDict):
    success: Literal[True]
    classNames: list[str]
    classColors: dict[str, str]
    mergedClassIds: list[int]
    targetClassId: int


class DatasetsDeleteClassesResponse(TypedDict):
    success: Literal[True]
    classNames: list[str]
    classColors: dict[str, str]
    deletedClassIds: list[int]
    deletedAnnotations: int


class DatasetsRedistributeSplitsResponseSplits(TypedDict):
    train: int
    val: int
    test: int


class DatasetsRedistributeSplitsResponse(TypedDict):
    success: Literal[True]
    splits: DatasetsRedistributeSplitsResponseSplits
    modified: int


class DatasetsListImagesResponseImagesItemLabelsItem(TypedDict):
    classId: float
    bbox: NotRequired[list[float]]
    segments: NotRequired[list[float]]
    keypoints: NotRequired[list[float]]
    obb: NotRequired[list[float]]
    skeletonId: NotRequired[str]


class DatasetsListImagesResponseImagesItem(TypedDict):
    id: str
    hash: str
    ext: str
    thumbnailUrl: NotRequired[str]
    imageUrl: NotRequired[str]
    width: float
    height: float
    split: Literal["train", "val", "test"]
    labelCount: float
    name: str
    bytes: NotRequired[float]
    error: NotRequired[str | None]
    labels: NotRequired[list[DatasetsListImagesResponseImagesItemLabelsItem]]
    labelsTruncated: NotRequired[Literal[True]]


class DatasetsListImagesResponse(TypedDict):
    images: list[DatasetsListImagesResponseImagesItem]
    total: NotRequired[float]
    hasMore: bool
    classes: list[str]
    errorCount: float
    nextCursor: NotRequired[str]


class DatasetsRetrieveSelectedImagesResponseImagesItemLabelsItem(TypedDict):
    classId: float
    bbox: NotRequired[list[float]]
    segments: NotRequired[list[float]]
    keypoints: NotRequired[list[float]]
    obb: NotRequired[list[float]]
    skeletonId: NotRequired[str]


class DatasetsRetrieveSelectedImagesResponseImagesItem(TypedDict):
    id: str
    hash: str
    ext: str
    thumbnailUrl: NotRequired[str]
    imageUrl: NotRequired[str]
    width: float
    height: float
    split: Literal["train", "val", "test"]
    labelCount: float
    name: str
    bytes: NotRequired[float]
    error: NotRequired[str | None]
    labels: NotRequired[list[DatasetsRetrieveSelectedImagesResponseImagesItemLabelsItem]]
    labelsTruncated: NotRequired[Literal[True]]


class DatasetsRetrieveSelectedImagesResponse(TypedDict):
    images: list[DatasetsRetrieveSelectedImagesResponseImagesItem]
    total: int
    hasMore: Literal[False]
    classes: list[str]
    errorCount: int


class DatasetsRetrieveExportResponse(TypedDict):
    downloadUrl: str
    version: NotRequired[int]
    cached: NotRequired[bool]


class DatasetsCreateExportResponse(TypedDict):
    version: int
    downloadUrl: str
    reused: bool


class DatasetsUpdateExportResponse(TypedDict):
    ok: Literal[True]


class DatasetsIngestResponse(TypedDict):
    jobId: str
    datasetId: str
    status: Literal["queued"]


class DatasetsRetrieveEmbeddingsResponseActiveJobProgress(TypedDict):
    stage: Literal["embedding", "umap"]
    percent: float
    processed: NotRequired[float]
    total: NotRequired[float]
    failedDownloads: NotRequired[float]
    failedInference: NotRequired[float]


class DatasetsRetrieveEmbeddingsResponseActiveJob(TypedDict):
    id: str
    status: Literal["queued", "starting", "running"]
    progress: DatasetsRetrieveEmbeddingsResponseActiveJobProgress
    createdAt: str


class DatasetsRetrieveEmbeddingsResponse(TypedDict):
    analyzedAt: str | None
    embeddingsCount: int
    latestImageAt: str | None
    activeJob: DatasetsRetrieveEmbeddingsResponseActiveJob


class DatasetsCreateEmbeddingsResponse(TypedDict):
    jobId: str


class DatasetsDeleteEmbeddingsResponse(TypedDict):
    cancelled: str | None


class DatasetsRetrieveImagesClusteringResponseImagesItem(TypedDict):
    id: str
    umapX: float
    umapY: float
    split: Literal["train", "val", "test"] | None
    classIds: list[int]
    width: float
    height: float
    bytes: float | None
    labelCount: int
    missing: bool


class DatasetsRetrieveImagesClusteringResponse(TypedDict):
    images: list[DatasetsRetrieveImagesClusteringResponseImagesItem]
    total: int
    offset: int
    limit: int
    hasMore: bool
    nextOffset: int | None
    updatedAt: str


class DatasetsListModelsResponseModelsItemDatasetVersion(TypedDict):
    version: int
    contentHash: str


class DatasetsListModelsResponseModelsItem(TypedDict):
    _id: str
    name: str
    slug: str
    status: Literal["pending", "untrained", "starting", "running", "completed", "failed", "cancelled"]
    task: NotRequired[Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"]]
    datasetVersion: NotRequired[DatasetsListModelsResponseModelsItemDatasetVersion]
    epochs: NotRequired[float]
    bestEpoch: NotRequired[float]
    bestFitness: NotRequired[float]
    metrics: dict[str, float]
    startedAt: NotRequired[str]
    completedAt: NotRequired[str]
    createdAt: str
    projectId: str
    projectSlug: NotRequired[str]
    projectIconColor: NotRequired[str]
    projectIconLetter: NotRequired[str]
    projectIconImage: NotRequired[str]
    username: str


class DatasetsListModelsResponse(TypedDict):
    models: list[DatasetsListModelsResponseModelsItem]
    count: int


class DatasetsRestoreResponse(TypedDict):
    version: int
    imageCount: int


class DatasetsPreviewRoboflowImportResponseWorkspace(TypedDict):
    url: str
    name: str


class DatasetsPreviewRoboflowImportResponseNewDatasetsItem(TypedDict):
    workspace: str
    projectId: str
    projectName: str
    projectType: str
    latestVersion: int
    latestVersionName: NotRequired[str]


class DatasetsPreviewRoboflowImportResponseStorage(TypedDict):
    usedBytes: float
    limitBytes: float
    hasEnoughStorage: bool


class DatasetsPreviewRoboflowImportResponse(TypedDict):
    workspace: DatasetsPreviewRoboflowImportResponseWorkspace
    newDatasets: list[DatasetsPreviewRoboflowImportResponseNewDatasetsItem]
    skippedCount: int
    missingVersionCount: int
    unsupportedCount: int
    unresolvedCount: int
    bytesTotal: int
    storage: DatasetsPreviewRoboflowImportResponseStorage


class DatasetsImportFromRoboflowResponseImportedItem(TypedDict):
    projectId: str
    projectName: str
    version: int
    datasetId: str
    slug: str


class DatasetsImportFromRoboflowResponseFailedItem(TypedDict):
    projectId: str
    projectName: str
    version: int
    error: str


class DatasetsImportFromRoboflowResponseSkippedItem(TypedDict):
    projectId: str
    projectName: str
    version: int


class DatasetsImportFromRoboflowResponse(TypedDict):
    imported: list[DatasetsImportFromRoboflowResponseImportedItem]
    failed: list[DatasetsImportFromRoboflowResponseFailedItem]
    skipped: list[DatasetsImportFromRoboflowResponseSkippedItem]


class DatasetsCreateIconResponse(TypedDict):
    success: Literal[True]
    downloadUrl: str


class DatasetsDeleteIconResponse(TypedDict):
    success: Literal[True]


class ImagesRetrieveLabelsResponseLabelsItem(TypedDict):
    classId: float
    bbox: NotRequired[list[float]]
    segments: NotRequired[list[float]]
    keypoints: NotRequired[list[float]]
    obb: NotRequired[list[float]]
    skeletonId: NotRequired[str]


class ImagesRetrieveLabelsResponse(TypedDict):
    labels: list[ImagesRetrieveLabelsResponseLabelsItem]
    classNames: list[str]
    labelsTruncated: NotRequired[Literal[True]]


class ImagesUpdateLabelsResponseLabelsItem(TypedDict):
    classId: float
    bbox: NotRequired[list[float]]
    segments: NotRequired[list[float]]
    keypoints: NotRequired[list[float]]
    obb: NotRequired[list[float]]
    skeletonId: NotRequired[str]


class ImagesUpdateLabelsResponse(TypedDict):
    success: Literal[True]
    labels: list[ImagesUpdateLabelsResponseLabelsItem]
    labelCount: float


class ImagesRetrieveMetadataResponseProperties(TypedDict):
    id: str
    datasetId: str
    filename: str
    hash: str
    extension: str
    originalExtension: NotRequired[str]
    originalPath: NotRequired[str]
    width: int
    height: int
    split: Literal["train", "val", "test"]
    annotationCount: int
    classIds: NotRequired[list[int]]
    bytes: NotRequired[int]
    region: NotRequired[Literal["us", "eu", "ap"]]
    externalKey: NotRequired[str]
    externalRevision: NotRequired[str]
    retainedByVersion: bool
    createdAt: str
    updatedAt: NotRequired[str]
    error: NotRequired[str | None]


class ImagesRetrieveMetadataResponse(TypedDict):
    metadata: dict[str, Any]
    properties: ImagesRetrieveMetadataResponseProperties


class ImagesUpdateMetadataResponse(TypedDict):
    metadata: dict[str, Any]
    updatedAt: str


class ImagesUpdateBulkResponse(TypedDict):
    success: Literal[True]
    modifiedCount: float
    skippedCount: float
    targetSplit: str


class ImagesDeleteBulkResponse(TypedDict):
    success: Literal[True]
    deletedCount: float
    deletedImageIds: list[str]


class ImagesPredictResponsePredictionsItem(TypedDict):
    classId: float
    bbox: NotRequired[list[float]]
    segments: NotRequired[list[float]]
    keypoints: NotRequired[list[float]]
    obb: NotRequired[list[float]]


class ImagesPredictResponse(TypedDict):
    success: Literal[True]
    predictions: list[ImagesPredictResponsePredictionsItem]
    modelUsed: str
    inferenceTime: NotRequired[float]


class ImagesRetrieveSignedUrlsResponse(TypedDict):
    urls: dict[str, str]
    thumbnails: dict[str, str]


class ImagesDeleteResponse(TypedDict):
    success: Literal[True]
    deletedImageId: str
    deletedCount: int


class ProjectsListResponseProjectsItemViewPreferences(TypedDict):
    sortBy: NotRequired[Literal["newest", "oldest", "name-asc", "name-desc", "size-asc", "size-desc"]]
    groupBy: NotRequired[Literal["none", "task"]]
    statusFilter: NotRequired[Literal["all", "completed", "running", "starting", "failed"]]


class ProjectsListResponseProjectsItem(TypedDict):
    _id: str
    username: str
    slug: str
    name: str
    description: NotRequired[str]
    visibility: Literal["public", "private"]
    tags: NotRequired[list[str]]
    license: NotRequired[
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
    ]
    iconColor: NotRequired[str]
    iconLetter: NotRequired[str]
    iconImage: NotRequired[str]
    modelCount: float
    modelNames: NotRequired[list[str]]
    totalBytes: NotRequired[float]
    starCount: float
    isStarred: bool
    archived: NotRequired[bool]
    region: NotRequired[Literal["us", "eu", "ap"]]
    task: NotRequired[Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"]]
    clonedFrom: NotRequired[str]
    cloneCount: NotRequired[float]
    totalModelDownloadCount: NotRequired[float]
    totalExportDownloadCount: NotRequired[float]
    viewPreferences: NotRequired[ProjectsListResponseProjectsItemViewPreferences]
    createdAt: str
    updatedAt: str


class ProjectsListResponse(TypedDict):
    projects: list[ProjectsListResponseProjectsItem]
    total: float
    region: Literal["us", "eu", "ap"]


class ProjectsCreateResponse(TypedDict):
    projectId: NotRequired[str]
    datasetId: NotRequired[str]
    modelId: NotRequired[str]
    slug: str
    region: Literal["us", "eu", "ap"]


class ProjectsRetrieveResponseProjectViewPreferences(TypedDict):
    sortBy: NotRequired[Literal["newest", "oldest", "name-asc", "name-desc", "size-asc", "size-desc"]]
    groupBy: NotRequired[Literal["none", "task"]]
    statusFilter: NotRequired[Literal["all", "completed", "running", "starting", "failed"]]


class ProjectsRetrieveResponseProject(TypedDict):
    _id: str
    username: str
    slug: str
    name: str
    description: NotRequired[str]
    visibility: Literal["public", "private"]
    tags: NotRequired[list[str]]
    license: NotRequired[
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
    ]
    iconColor: NotRequired[str]
    iconLetter: NotRequired[str]
    iconImage: NotRequired[str]
    starCount: float
    isStarred: bool
    archived: NotRequired[bool]
    region: NotRequired[Literal["us", "eu", "ap"]]
    task: NotRequired[Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"]]
    clonedFrom: NotRequired[str]
    cloneCount: NotRequired[float]
    totalModelDownloadCount: NotRequired[float]
    totalExportDownloadCount: NotRequired[float]
    viewPreferences: NotRequired[ProjectsRetrieveResponseProjectViewPreferences]
    createdAt: str
    updatedAt: str


class ProjectsRetrieveResponse(TypedDict):
    project: ProjectsRetrieveResponseProject
    isOwner: bool


class ProjectsUpdateResponse(TypedDict):
    success: Literal[True]


class ProjectsDeleteResponse(TypedDict):
    success: Literal[True]


class ProjectsRetrieveMetadataResponse(TypedDict):
    metadata: dict[str, Any]
    properties: list[list[Any]]


class ProjectsCloneResponse(TypedDict):
    projectId: str
    slug: str
    name: str
    modelCount: float
    region: Literal["us", "eu", "ap"]


class ProjectsCreateIconResponse(TypedDict):
    success: Literal[True]
    downloadUrl: str


class ProjectsDeleteIconResponse(TypedDict):
    success: Literal[True]


class ModelsListResponseModelsItemDatasetVersion(TypedDict):
    version: float
    contentHash: str


class ModelsListResponseModelsItemTrainArgs(TypedDict):
    model: NotRequired[str]
    classes: NotRequired[list[int] | None]
    lr0: NotRequired[float]
    lrf: NotRequired[float]
    momentum: NotRequired[float]
    weight_decay: NotRequired[float]
    warmup_epochs: NotRequired[float]
    warmup_momentum: NotRequired[float]
    warmup_bias_lr: NotRequired[float]
    optimizer: NotRequired[Literal["auto", "SGD", "MuSGD", "Adam", "AdamW", "NAdam", "RAdam", "RMSProp", "Adamax"]]
    box: NotRequired[float]
    cls: NotRequired[float]
    dfl: NotRequired[float]
    pose: NotRequired[float]
    kobj: NotRequired[float]
    label_smoothing: NotRequired[float]
    hsv_h: NotRequired[float]
    hsv_s: NotRequired[float]
    hsv_v: NotRequired[float]
    degrees: NotRequired[float]
    translate: NotRequired[float]
    scale: NotRequired[float]
    shear: NotRequired[float]
    perspective: NotRequired[float]
    flipud: NotRequired[float]
    fliplr: NotRequired[float]
    mosaic: NotRequired[float]
    mixup: NotRequired[float]
    copy_paste: NotRequired[float]
    epochs: NotRequired[int]
    batch: NotRequired[int]
    imgsz: NotRequired[int]
    pretrained: NotRequired[bool]
    patience: NotRequired[int]
    time: NotRequired[float | None]
    seed: NotRequired[int]
    deterministic: NotRequired[bool]
    amp: NotRequired[bool]
    cos_lr: NotRequired[bool]
    compile: NotRequired[bool | Literal["default", "reduce-overhead", "max-autotune", "max-autotune-no-cudagraphs"]]
    close_mosaic: NotRequired[int]
    save_period: NotRequired[int]
    fraction: NotRequired[float]
    freeze: NotRequired[int | None]
    single_cls: NotRequired[bool]
    rect: NotRequired[bool]
    multi_scale: NotRequired[float]
    val: NotRequired[bool]
    resume: NotRequired[bool]
    device: NotRequired[Literal["0", "auto", "cpu", "mps"]]
    cache: NotRequired[Literal["ram", "disk", "false"]]
    workers: NotRequired[int]
    dropout: NotRequired[float]
    iou: NotRequired[float]
    max_det: NotRequired[int]


class ModelsListResponseModelsItemTrainResultsItem(TypedDict):
    epoch: NotRequired[float]
    metrics: NotRequired[dict[str, float]]
    fitness: NotRequired[float]
    timestamp: NotRequired[str]


class ModelsListResponseModelsItemFile(TypedDict):
    size: float


class ModelsListResponseModelsItemTrainingError(TypedDict):
    message: str
    code: NotRequired[str]
    timestamp: str


class ModelsListResponseModelsItem(TypedDict):
    _id: str
    username: NotRequired[str]
    projectId: NotRequired[str]
    projectSlug: NotRequired[str]
    slug: NotRequired[str]
    name: str
    description: NotRequired[str]
    status: NotRequired[Literal["pending", "untrained", "starting", "running", "completed", "failed", "cancelled"]]
    task: NotRequired[Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"]]
    color: NotRequired[str]
    license: NotRequired[
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
    ]
    datasetId: NotRequired[str]
    datasetVersion: NotRequired[ModelsListResponseModelsItemDatasetVersion]
    sourceModelId: NotRequired[str]
    epochs: NotRequired[float]
    bestEpoch: NotRequired[float]
    bestFitness: NotRequired[float]
    trainArgs: NotRequired[ModelsListResponseModelsItemTrainArgs]
    version: NotRequired[str]
    docs: NotRequired[str]
    startedAt: NotRequired[str]
    completedAt: NotRequired[str]
    classNames: NotRequired[list[str]]
    metrics: NotRequired[dict[str, float]]
    trainResults: NotRequired[list[ModelsListResponseModelsItemTrainResultsItem]]
    hasWeights: bool
    file: NotRequired[ModelsListResponseModelsItemFile]
    plots: NotRequired[list[Any]]
    trainingError: NotRequired[ModelsListResponseModelsItemTrainingError]
    starCount: float
    isStarred: bool
    clonedFrom: NotRequired[str]
    downloadCount: NotRequired[float]
    cloneCount: NotRequired[float]
    createdAt: NotRequired[str]
    updatedAt: NotRequired[str]


class ModelsListResponse(TypedDict):
    models: list[ModelsListResponseModelsItem]
    region: Literal["us", "eu", "ap"]


class ModelsCreateResponse(TypedDict):
    projectId: NotRequired[str]
    datasetId: NotRequired[str]
    modelId: NotRequired[str]
    slug: str
    region: Literal["us", "eu", "ap"]


class ModelsListCompletedResponseModelsItem(TypedDict):
    _id: str
    slug: str
    name: str
    task: Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"]
    projectSlug: str
    projectName: str
    projectIconColor: NotRequired[str]
    projectIconLetter: NotRequired[str]
    bestFitness: NotRequired[float]


class ModelsListCompletedResponse(TypedDict):
    models: list[ModelsListCompletedResponseModelsItem]


class ModelsRetrieveResponseModelDatasetVersion(TypedDict):
    version: float
    contentHash: str


class ModelsRetrieveResponseModelTrainArgs(TypedDict):
    model: NotRequired[str]
    classes: NotRequired[list[int] | None]
    lr0: NotRequired[float]
    lrf: NotRequired[float]
    momentum: NotRequired[float]
    weight_decay: NotRequired[float]
    warmup_epochs: NotRequired[float]
    warmup_momentum: NotRequired[float]
    warmup_bias_lr: NotRequired[float]
    optimizer: NotRequired[Literal["auto", "SGD", "MuSGD", "Adam", "AdamW", "NAdam", "RAdam", "RMSProp", "Adamax"]]
    box: NotRequired[float]
    cls: NotRequired[float]
    dfl: NotRequired[float]
    pose: NotRequired[float]
    kobj: NotRequired[float]
    label_smoothing: NotRequired[float]
    hsv_h: NotRequired[float]
    hsv_s: NotRequired[float]
    hsv_v: NotRequired[float]
    degrees: NotRequired[float]
    translate: NotRequired[float]
    scale: NotRequired[float]
    shear: NotRequired[float]
    perspective: NotRequired[float]
    flipud: NotRequired[float]
    fliplr: NotRequired[float]
    mosaic: NotRequired[float]
    mixup: NotRequired[float]
    copy_paste: NotRequired[float]
    epochs: NotRequired[int]
    batch: NotRequired[int]
    imgsz: NotRequired[int]
    pretrained: NotRequired[bool]
    patience: NotRequired[int]
    time: NotRequired[float | None]
    seed: NotRequired[int]
    deterministic: NotRequired[bool]
    amp: NotRequired[bool]
    cos_lr: NotRequired[bool]
    compile: NotRequired[bool | Literal["default", "reduce-overhead", "max-autotune", "max-autotune-no-cudagraphs"]]
    close_mosaic: NotRequired[int]
    save_period: NotRequired[int]
    fraction: NotRequired[float]
    freeze: NotRequired[int | None]
    single_cls: NotRequired[bool]
    rect: NotRequired[bool]
    multi_scale: NotRequired[float]
    val: NotRequired[bool]
    resume: NotRequired[bool]
    device: NotRequired[Literal["0", "auto", "cpu", "mps"]]
    cache: NotRequired[Literal["ram", "disk", "false"]]
    workers: NotRequired[int]
    dropout: NotRequired[float]
    iou: NotRequired[float]
    max_det: NotRequired[int]


class ModelsRetrieveResponseModelTrainResultsItem(TypedDict):
    epoch: NotRequired[float]
    metrics: NotRequired[dict[str, float]]
    fitness: NotRequired[float]
    timestamp: NotRequired[str]


class ModelsRetrieveResponseModelFile(TypedDict):
    size: float


class ModelsRetrieveResponseModelTrainingError(TypedDict):
    message: str
    code: NotRequired[str]
    timestamp: str


class ModelsRetrieveResponseModelSourceModel(TypedDict):
    username: str
    projectSlug: str
    projectName: str
    projectIconColor: NotRequired[str]
    projectIconLetter: NotRequired[str]
    projectIconImage: NotRequired[str]
    modelSlug: str
    modelName: str


class ModelsRetrieveResponseModel(TypedDict):
    _id: str
    username: NotRequired[str]
    projectId: NotRequired[str]
    projectSlug: NotRequired[str]
    slug: NotRequired[str]
    name: str
    description: NotRequired[str]
    status: NotRequired[Literal["pending", "untrained", "starting", "running", "completed", "failed", "cancelled"]]
    task: NotRequired[Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"]]
    color: NotRequired[str]
    license: NotRequired[
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
    ]
    datasetId: NotRequired[str]
    datasetVersion: NotRequired[ModelsRetrieveResponseModelDatasetVersion]
    sourceModelId: NotRequired[str]
    epochs: NotRequired[float]
    bestEpoch: NotRequired[float]
    bestFitness: NotRequired[float]
    trainArgs: NotRequired[ModelsRetrieveResponseModelTrainArgs]
    version: NotRequired[str]
    docs: NotRequired[str]
    startedAt: NotRequired[str]
    completedAt: NotRequired[str]
    classNames: NotRequired[list[str]]
    metrics: NotRequired[dict[str, float]]
    trainResults: NotRequired[list[ModelsRetrieveResponseModelTrainResultsItem]]
    hasWeights: bool
    file: NotRequired[ModelsRetrieveResponseModelFile]
    plots: NotRequired[list[Any]]
    trainingError: NotRequired[ModelsRetrieveResponseModelTrainingError]
    starCount: float
    isStarred: bool
    clonedFrom: NotRequired[str]
    downloadCount: NotRequired[float]
    cloneCount: NotRequired[float]
    createdAt: NotRequired[str]
    updatedAt: NotRequired[str]
    sourceModel: NotRequired[ModelsRetrieveResponseModelSourceModel]
    baseModel: NotRequired[str]
    projectLicense: NotRequired[
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
    ]


class ModelsRetrieveResponseAnalysisCoverage(TypedDict):
    mode: Literal["full", "sampled", "tails", "partial", "unavailable"]
    omittedMiddle: int
    unmatchedExtremes: int


class ModelsRetrieveResponseAnalysisScatterSample(TypedDict):
    eligible: int
    rows: list[list[Any]]


class ModelsRetrieveResponseAnalysisCohortsWorstMetricsF1(TypedDict):
    count: int
    min: float
    p25: float
    median: float
    p75: float
    max: float
    mean: float


class ModelsRetrieveResponseAnalysisCohortsWorstMetrics(TypedDict):
    tp: int
    fp: int
    fn: int
    f1: ModelsRetrieveResponseAnalysisCohortsWorstMetricsF1


class ModelsRetrieveResponseAnalysisCohortsWorstExamplesItemLabelsItem(TypedDict):
    classId: int
    bbox: NotRequired[list[Any]]
    segments: NotRequired[list[float]]
    keypoints: NotRequired[list[float]]
    obb: NotRequired[list[Any]]
    skeletonId: NotRequired[str]


class ModelsRetrieveResponseAnalysisCohortsWorstExamplesItem(TypedDict):
    imageId: NotRequired[str]
    hash: str
    tp: int
    fp: int
    fn: int
    f1: float
    isEmptyGroundTruth: bool
    width: NotRequired[float]
    height: NotRequired[float]
    pixels: NotRequired[float]
    aspectRatio: NotRequired[float]
    instanceCount: NotRequired[int]
    labels: NotRequired[list[ModelsRetrieveResponseAnalysisCohortsWorstExamplesItemLabelsItem]]


class ModelsRetrieveResponseAnalysisCohortsWorst(TypedDict):
    count: int
    matched: int
    metrics: ModelsRetrieveResponseAnalysisCohortsWorstMetrics
    examples: list[ModelsRetrieveResponseAnalysisCohortsWorstExamplesItem]


class ModelsRetrieveResponseAnalysisCohortsBestMetricsF1(TypedDict):
    count: int
    min: float
    p25: float
    median: float
    p75: float
    max: float
    mean: float


class ModelsRetrieveResponseAnalysisCohortsBestMetrics(TypedDict):
    tp: int
    fp: int
    fn: int
    f1: ModelsRetrieveResponseAnalysisCohortsBestMetricsF1


class ModelsRetrieveResponseAnalysisCohortsBestExamplesItemLabelsItem(TypedDict):
    classId: int
    bbox: NotRequired[list[Any]]
    segments: NotRequired[list[float]]
    keypoints: NotRequired[list[float]]
    obb: NotRequired[list[Any]]
    skeletonId: NotRequired[str]


class ModelsRetrieveResponseAnalysisCohortsBestExamplesItem(TypedDict):
    imageId: NotRequired[str]
    hash: str
    tp: int
    fp: int
    fn: int
    f1: float
    isEmptyGroundTruth: bool
    width: NotRequired[float]
    height: NotRequired[float]
    pixels: NotRequired[float]
    aspectRatio: NotRequired[float]
    instanceCount: NotRequired[int]
    labels: NotRequired[list[ModelsRetrieveResponseAnalysisCohortsBestExamplesItemLabelsItem]]


class ModelsRetrieveResponseAnalysisCohortsBest(TypedDict):
    count: int
    matched: int
    metrics: ModelsRetrieveResponseAnalysisCohortsBestMetrics
    examples: list[ModelsRetrieveResponseAnalysisCohortsBestExamplesItem]


class ModelsRetrieveResponseAnalysisCohorts(TypedDict):
    worst: ModelsRetrieveResponseAnalysisCohortsWorst
    best: ModelsRetrieveResponseAnalysisCohortsBest


class ModelsRetrieveResponseAnalysisComparisonsWidthWorst(TypedDict):
    count: int
    min: float
    p25: float
    median: float
    p75: float
    max: float
    mean: float


class ModelsRetrieveResponseAnalysisComparisonsWidthBest(TypedDict):
    count: int
    min: float
    p25: float
    median: float
    p75: float
    max: float
    mean: float


class ModelsRetrieveResponseAnalysisComparisonsWidthRelationshipFit(TypedDict):
    slope: float
    intercept: float
    pearsonR: float
    rSquared: float


class ModelsRetrieveResponseAnalysisComparisonsWidthRelationshipCovariance(TypedDict):
    mean: list[Any]
    eigenvalues: list[Any]
    eigenvectors: list[Any]


class ModelsRetrieveResponseAnalysisComparisonsWidthRelationship(TypedDict):
    count: int
    fit: ModelsRetrieveResponseAnalysisComparisonsWidthRelationshipFit
    covariance: ModelsRetrieveResponseAnalysisComparisonsWidthRelationshipCovariance


class ModelsRetrieveResponseAnalysisComparisonsWidth(TypedDict):
    worst: ModelsRetrieveResponseAnalysisComparisonsWidthWorst
    best: ModelsRetrieveResponseAnalysisComparisonsWidthBest
    relationship: ModelsRetrieveResponseAnalysisComparisonsWidthRelationship


class ModelsRetrieveResponseAnalysisComparisonsHeightWorst(TypedDict):
    count: int
    min: float
    p25: float
    median: float
    p75: float
    max: float
    mean: float


class ModelsRetrieveResponseAnalysisComparisonsHeightBest(TypedDict):
    count: int
    min: float
    p25: float
    median: float
    p75: float
    max: float
    mean: float


class ModelsRetrieveResponseAnalysisComparisonsHeightRelationshipFit(TypedDict):
    slope: float
    intercept: float
    pearsonR: float
    rSquared: float


class ModelsRetrieveResponseAnalysisComparisonsHeightRelationshipCovariance(TypedDict):
    mean: list[Any]
    eigenvalues: list[Any]
    eigenvectors: list[Any]


class ModelsRetrieveResponseAnalysisComparisonsHeightRelationship(TypedDict):
    count: int
    fit: ModelsRetrieveResponseAnalysisComparisonsHeightRelationshipFit
    covariance: ModelsRetrieveResponseAnalysisComparisonsHeightRelationshipCovariance


class ModelsRetrieveResponseAnalysisComparisonsHeight(TypedDict):
    worst: ModelsRetrieveResponseAnalysisComparisonsHeightWorst
    best: ModelsRetrieveResponseAnalysisComparisonsHeightBest
    relationship: ModelsRetrieveResponseAnalysisComparisonsHeightRelationship


class ModelsRetrieveResponseAnalysisComparisonsPixelsWorst(TypedDict):
    count: int
    min: float
    p25: float
    median: float
    p75: float
    max: float
    mean: float


class ModelsRetrieveResponseAnalysisComparisonsPixelsBest(TypedDict):
    count: int
    min: float
    p25: float
    median: float
    p75: float
    max: float
    mean: float


class ModelsRetrieveResponseAnalysisComparisonsPixelsRelationshipFit(TypedDict):
    slope: float
    intercept: float
    pearsonR: float
    rSquared: float


class ModelsRetrieveResponseAnalysisComparisonsPixelsRelationshipCovariance(TypedDict):
    mean: list[Any]
    eigenvalues: list[Any]
    eigenvectors: list[Any]


class ModelsRetrieveResponseAnalysisComparisonsPixelsRelationship(TypedDict):
    count: int
    fit: ModelsRetrieveResponseAnalysisComparisonsPixelsRelationshipFit
    covariance: ModelsRetrieveResponseAnalysisComparisonsPixelsRelationshipCovariance


class ModelsRetrieveResponseAnalysisComparisonsPixels(TypedDict):
    worst: ModelsRetrieveResponseAnalysisComparisonsPixelsWorst
    best: ModelsRetrieveResponseAnalysisComparisonsPixelsBest
    relationship: ModelsRetrieveResponseAnalysisComparisonsPixelsRelationship


class ModelsRetrieveResponseAnalysisComparisonsAspectRatioWorst(TypedDict):
    count: int
    min: float
    p25: float
    median: float
    p75: float
    max: float
    mean: float


class ModelsRetrieveResponseAnalysisComparisonsAspectRatioBest(TypedDict):
    count: int
    min: float
    p25: float
    median: float
    p75: float
    max: float
    mean: float


class ModelsRetrieveResponseAnalysisComparisonsAspectRatioRelationshipFit(TypedDict):
    slope: float
    intercept: float
    pearsonR: float
    rSquared: float


class ModelsRetrieveResponseAnalysisComparisonsAspectRatioRelationshipCovariance(TypedDict):
    mean: list[Any]
    eigenvalues: list[Any]
    eigenvectors: list[Any]


class ModelsRetrieveResponseAnalysisComparisonsAspectRatioRelationship(TypedDict):
    count: int
    fit: ModelsRetrieveResponseAnalysisComparisonsAspectRatioRelationshipFit
    covariance: ModelsRetrieveResponseAnalysisComparisonsAspectRatioRelationshipCovariance


class ModelsRetrieveResponseAnalysisComparisonsAspectRatio(TypedDict):
    worst: ModelsRetrieveResponseAnalysisComparisonsAspectRatioWorst
    best: ModelsRetrieveResponseAnalysisComparisonsAspectRatioBest
    relationship: ModelsRetrieveResponseAnalysisComparisonsAspectRatioRelationship


class ModelsRetrieveResponseAnalysisComparisonsInstanceCountWorst(TypedDict):
    count: int
    min: float
    p25: float
    median: float
    p75: float
    max: float
    mean: float


class ModelsRetrieveResponseAnalysisComparisonsInstanceCountBest(TypedDict):
    count: int
    min: float
    p25: float
    median: float
    p75: float
    max: float
    mean: float


class ModelsRetrieveResponseAnalysisComparisonsInstanceCountRelationshipFit(TypedDict):
    slope: float
    intercept: float
    pearsonR: float
    rSquared: float


class ModelsRetrieveResponseAnalysisComparisonsInstanceCountRelationshipCovariance(TypedDict):
    mean: list[Any]
    eigenvalues: list[Any]
    eigenvectors: list[Any]


class ModelsRetrieveResponseAnalysisComparisonsInstanceCountRelationship(TypedDict):
    count: int
    fit: ModelsRetrieveResponseAnalysisComparisonsInstanceCountRelationshipFit
    covariance: ModelsRetrieveResponseAnalysisComparisonsInstanceCountRelationshipCovariance


class ModelsRetrieveResponseAnalysisComparisonsInstanceCount(TypedDict):
    worst: ModelsRetrieveResponseAnalysisComparisonsInstanceCountWorst
    best: ModelsRetrieveResponseAnalysisComparisonsInstanceCountBest
    relationship: ModelsRetrieveResponseAnalysisComparisonsInstanceCountRelationship


class ModelsRetrieveResponseAnalysisComparisonsClassPresenceItemWorst(TypedDict):
    count: int
    prevalence: float


class ModelsRetrieveResponseAnalysisComparisonsClassPresenceItemBest(TypedDict):
    count: int
    prevalence: float


class ModelsRetrieveResponseAnalysisComparisonsClassPresenceItem(TypedDict):
    classId: int
    name: str
    worst: ModelsRetrieveResponseAnalysisComparisonsClassPresenceItemWorst
    best: ModelsRetrieveResponseAnalysisComparisonsClassPresenceItemBest
    prevalenceDifference: float


class ModelsRetrieveResponseAnalysisComparisons(TypedDict):
    width: ModelsRetrieveResponseAnalysisComparisonsWidth
    height: ModelsRetrieveResponseAnalysisComparisonsHeight
    pixels: ModelsRetrieveResponseAnalysisComparisonsPixels
    aspectRatio: ModelsRetrieveResponseAnalysisComparisonsAspectRatio
    instanceCount: ModelsRetrieveResponseAnalysisComparisonsInstanceCount
    classPresence: list[ModelsRetrieveResponseAnalysisComparisonsClassPresenceItem]
    classPresenceTruncated: bool


class ModelsRetrieveResponseAnalysis(TypedDict):
    population: int
    retained: int
    matched: int
    unmatched: int
    traitsAvailable: bool
    sourceSplit: Literal["train", "val"] | None
    coverage: ModelsRetrieveResponseAnalysisCoverage
    scatterSample: ModelsRetrieveResponseAnalysisScatterSample
    cohorts: ModelsRetrieveResponseAnalysisCohorts
    comparisons: ModelsRetrieveResponseAnalysisComparisons


class ModelsRetrieveResponse(TypedDict):
    model: NotRequired[ModelsRetrieveResponseModel]
    isOwner: NotRequired[bool]
    analysis: NotRequired[ModelsRetrieveResponseAnalysis]


class ModelsUpdateResponse(TypedDict):
    success: Literal[True]


class ModelsDeleteResponse(TypedDict):
    success: Literal[True]


class ModelsRetrieveMetadataResponse(TypedDict):
    metadata: dict[str, Any]
    properties: list[list[Any]]


class ModelsCloneResponse(TypedDict):
    modelId: str
    modelSlug: str
    modelName: str
    projectId: str
    projectSlug: str
    projectName: str
    region: Literal["us", "eu", "ap"]


class ModelsRetrieveFilesResponseFilesItem(TypedDict):
    name: str
    size: NotRequired[float]
    downloadUrl: str


class ModelsRetrieveFilesResponse(TypedDict):
    files: list[ModelsRetrieveFilesResponseFilesItem]


class ModelsPredictResponseImagesItemSemanticMask(TypedDict):
    shape: list[float]
    encoding: Literal["png"]
    data: str


class ModelsPredictResponseImagesItemDepth(TypedDict):
    shape: list[float]
    encoding: Literal["png"]
    data: str
    min: float
    max: float
    bits: Literal[8, 12, 16]


class ModelsPredictResponseImagesItem(TypedDict):
    shape: list[float]
    speed: dict[str, float]
    results: list[Any]
    semantic_mask: NotRequired[ModelsPredictResponseImagesItemSemanticMask]
    depth: NotRequired[ModelsPredictResponseImagesItemDepth]


class ModelsPredictResponseMetadata(TypedDict):
    imageCount: int
    functionTimeAlive: float
    functionTimeCall: float
    task: str | None
    version: dict[str, str]


class ModelsPredictResponse(TypedDict):
    images: list[ModelsPredictResponseImagesItem]
    metadata: ModelsPredictResponseMetadata


class ModelsRetrieveTrainingResponseJobProgress(TypedDict):
    currentEpoch: float
    totalEpochs: float
    startedAt: NotRequired[str]
    completedAt: NotRequired[str]
    percentage: float


class ModelsRetrieveTrainingResponseJobTiming(TypedDict):
    elapsedMs: float
    timePerEpochMs: float
    etaMs: float


class ModelsRetrieveTrainingResponseJobCompute(TypedDict):
    gpuType: str
    gpuDisplayName: str
    gpuMemoryGb: float


class ModelsRetrieveTrainingResponseJobTrainArgs(TypedDict):
    model: NotRequired[str]
    epochs: NotRequired[float]
    batch: NotRequired[float]
    imgsz: NotRequired[float]


class ModelsRetrieveTrainingResponseJob(TypedDict):
    id: str
    status: Literal["pending", "untrained", "starting", "running", "completed", "failed", "cancelled"]
    progress: ModelsRetrieveTrainingResponseJobProgress
    timing: ModelsRetrieveTrainingResponseJobTiming
    compute: ModelsRetrieveTrainingResponseJobCompute
    trainArgs: ModelsRetrieveTrainingResponseJobTrainArgs
    epochMetrics: dict[str, Any] | None
    error: Any | None
    createdAt: str
    updatedAt: str


class ModelsRetrieveTrainingResponseInstanceStatus(TypedDict):
    status: str


class ModelsRetrieveTrainingResponse(TypedDict):
    job: ModelsRetrieveTrainingResponseJob
    instanceStatus: NotRequired[ModelsRetrieveTrainingResponseInstanceStatus]


class ModelsDeleteTrainingResponse(TypedDict):
    success: Literal[True]
    status: Literal["cancelled"]
    warning: NotRequired[str]


class ModelsTrackDownloadResponse(TypedDict):
    success: Literal[True]


class TrainingStartResponseEstimatedCost(TypedDict):
    pricePerHour: float
    gpuMemoryGb: float


class TrainingStartResponseBilling(TypedDict):
    estimatedCostCents: float
    estimatedCostDisplay: str
    balanceCents: float


class TrainingStartResponse(TypedDict):
    modelId: str
    status: Literal["starting"]
    gpuType: str
    estimatedCost: TrainingStartResponseEstimatedCost
    billing: TrainingStartResponseBilling


TrainingRetrieveGpuAvailabilityResponse = dict[str, Literal["High", "Medium", "Low"] | None]


class ExportsListResponseExportsItemFile(TypedDict):
    size: NotRequired[float]
    downloadUrl: NotRequired[str]
    downloadFilename: NotRequired[str]


class ExportsListResponseExportsItemError(TypedDict):
    message: str
    timestamp: str


class ExportsListResponseExportsItem(TypedDict):
    _id: str
    modelId: str
    projectId: str
    status: Literal["queued", "starting", "running", "completed", "failed", "cancelled"]
    format: Literal[
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
    ]
    args: NotRequired[dict[str, Any]]
    gpuType: NotRequired[str]
    file: NotRequired[ExportsListResponseExportsItemFile]
    error: NotRequired[ExportsListResponseExportsItemError]
    startedAt: NotRequired[str]
    completedAt: NotRequired[str]
    createdAt: str
    updatedAt: str


class ExportsListResponse(TypedDict):
    exports: list[ExportsListResponseExportsItem]
    region: Literal["us", "eu", "ap"]


class ExportsCreateResponse(TypedDict):
    exportId: str
    format: Literal[
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
    ]
    status: Literal["queued", "running"]
    gpuType: NotRequired[str]
    region: Literal["us", "eu", "ap"]


class ExportsRetrieveResponseExportFile(TypedDict):
    size: NotRequired[float]
    downloadUrl: NotRequired[str]
    downloadFilename: NotRequired[str]


class ExportsRetrieveResponseExportError(TypedDict):
    message: str
    timestamp: str


class ExportsRetrieveResponseExport(TypedDict):
    _id: str
    modelId: str
    projectId: str
    status: Literal["queued", "starting", "running", "completed", "failed", "cancelled"]
    format: Literal[
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
    ]
    args: NotRequired[dict[str, Any]]
    gpuType: NotRequired[str]
    file: NotRequired[ExportsRetrieveResponseExportFile]
    error: NotRequired[ExportsRetrieveResponseExportError]
    startedAt: NotRequired[str]
    completedAt: NotRequired[str]
    createdAt: str
    updatedAt: str


class ExportsRetrieveResponse(TypedDict):
    export: ExportsRetrieveResponseExport


class ExportsDeleteResponse(TypedDict):
    success: Literal[True]
    action: Literal["cancelled", "deleted"]


class ExportsTrackDownloadResponse(TypedDict):
    success: Literal[True]


class DeploymentsListResponseDeploymentsItemResources(TypedDict):
    cpu: float
    memoryGi: float
    minInstances: float
    maxInstances: float


class DeploymentsListResponseDeploymentsItem(TypedDict):
    _id: str
    username: str
    modelId: str
    projectId: str
    name: str
    slug: str
    status: Literal["creating", "deploying", "ready", "stopping", "stopped", "failed"]
    statusMessage: NotRequired[str]
    region: str
    serviceUrl: NotRequired[str]
    resources: DeploymentsListResponseDeploymentsItemResources
    deployedAt: NotRequired[str]
    createdAt: str
    updatedAt: str


class DeploymentsListResponse(TypedDict):
    deployments: list[DeploymentsListResponseDeploymentsItem]
    total: float
    region: Literal["us", "eu", "ap"]


class DeploymentsCreateResponse(TypedDict):
    deploymentId: str
    status: Literal["creating"]
    message: str
    region: str


class DeploymentsRetrieveResponseDeploymentResources(TypedDict):
    cpu: float
    memoryGi: float
    minInstances: float
    maxInstances: float


class DeploymentsRetrieveResponseDeployment(TypedDict):
    _id: str
    username: str
    modelId: str
    projectId: str
    name: str
    slug: str
    status: Literal["creating", "deploying", "ready", "stopping", "stopped", "failed"]
    statusMessage: NotRequired[str]
    region: str
    serviceUrl: NotRequired[str]
    resources: DeploymentsRetrieveResponseDeploymentResources
    deployedAt: NotRequired[str]
    createdAt: str
    updatedAt: str


class DeploymentsRetrieveResponse(TypedDict):
    deployment: DeploymentsRetrieveResponseDeployment
    region: Literal["us", "eu", "ap"]


class DeploymentsUpdateResponse(TypedDict):
    success: Literal[True]
    status: Literal["ready"]
    message: str


class DeploymentsDeleteResponse(TypedDict):
    success: Literal[True]


class DeploymentsPredictResponseImagesItemSemanticMask(TypedDict):
    shape: list[float]
    encoding: Literal["png"]
    data: str


class DeploymentsPredictResponseImagesItemDepth(TypedDict):
    shape: list[float]
    encoding: Literal["png"]
    data: str
    min: float
    max: float
    bits: Literal[8, 12, 16]


class DeploymentsPredictResponseImagesItem(TypedDict):
    shape: list[float]
    speed: dict[str, float]
    results: list[Any]
    semantic_mask: NotRequired[DeploymentsPredictResponseImagesItemSemanticMask]
    depth: NotRequired[DeploymentsPredictResponseImagesItemDepth]


class DeploymentsPredictResponseMetadata(TypedDict):
    imageCount: int
    functionTimeAlive: float
    functionTimeCall: float
    task: str | None
    version: dict[str, str]


class DeploymentsPredictResponse(TypedDict):
    images: list[DeploymentsPredictResponseImagesItem]
    metadata: DeploymentsPredictResponseMetadata


class DeploymentsRetrieveHealthResponse(TypedDict):
    healthy: bool
    status: NotRequired[float]
    latencyMs: float
    error: NotRequired[str]


class DeploymentsRetrieveMetricsResponseTimeRange(TypedDict):
    start: str
    end: str


class DeploymentsRetrieveMetricsResponseSummary(TypedDict):
    totalRequests: float
    errorCount: float
    errorRate: float
    avgLatencyMs: float
    p50LatencyMs: float
    p95LatencyMs: float
    p99LatencyMs: float


class DeploymentsRetrieveMetricsResponseTimeSeriesRequestsItem(TypedDict):
    timestamp: str
    value: float


class DeploymentsRetrieveMetricsResponseTimeSeriesErrorsItem(TypedDict):
    timestamp: str
    value: float


class DeploymentsRetrieveMetricsResponseTimeSeriesLatencyP50Item(TypedDict):
    timestamp: str
    value: float


class DeploymentsRetrieveMetricsResponseTimeSeriesLatencyP95Item(TypedDict):
    timestamp: str
    value: float


class DeploymentsRetrieveMetricsResponseTimeSeriesCpuUtilizationItem(TypedDict):
    timestamp: str
    value: float


class DeploymentsRetrieveMetricsResponseTimeSeriesMemoryUtilizationItem(TypedDict):
    timestamp: str
    value: float


class DeploymentsRetrieveMetricsResponseTimeSeriesInstanceCountItem(TypedDict):
    timestamp: str
    value: float


class DeploymentsRetrieveMetricsResponseTimeSeries(TypedDict):
    requests: list[DeploymentsRetrieveMetricsResponseTimeSeriesRequestsItem]
    errors: list[DeploymentsRetrieveMetricsResponseTimeSeriesErrorsItem]
    latencyP50: list[DeploymentsRetrieveMetricsResponseTimeSeriesLatencyP50Item]
    latencyP95: list[DeploymentsRetrieveMetricsResponseTimeSeriesLatencyP95Item]
    cpuUtilization: list[DeploymentsRetrieveMetricsResponseTimeSeriesCpuUtilizationItem]
    memoryUtilization: list[DeploymentsRetrieveMetricsResponseTimeSeriesMemoryUtilizationItem]
    instanceCount: list[DeploymentsRetrieveMetricsResponseTimeSeriesInstanceCountItem]


class DeploymentsRetrieveMetricsResponse(TypedDict):
    deploymentId: NotRequired[str]
    region: NotRequired[str]
    timeRange: NotRequired[DeploymentsRetrieveMetricsResponseTimeRange]
    summary: NotRequired[DeploymentsRetrieveMetricsResponseSummary]
    timeSeries: NotRequired[DeploymentsRetrieveMetricsResponseTimeSeries]
    requests24h: NotRequired[list[float]]
    totalRequests: NotRequired[float]
    errorRate: NotRequired[float]
    avgLatencyMs: NotRequired[float]


class DeploymentsRetrieveLogsResponseEntriesItemHttpRequest(TypedDict):
    method: str
    url: str
    status: float
    latencyMs: float
    userAgent: NotRequired[str]


class DeploymentsRetrieveLogsResponseEntriesItem(TypedDict):
    timestamp: str
    severity: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL", "DEFAULT"]
    message: str
    httpRequest: NotRequired[DeploymentsRetrieveLogsResponseEntriesItemHttpRequest]


class DeploymentsRetrieveLogsResponse(TypedDict):
    entries: list[DeploymentsRetrieveLogsResponseEntriesItem]
    nextPageToken: NotRequired[str]


class DeploymentsStartResponse(TypedDict):
    success: Literal[True]
    status: Literal["ready", "stopped"]
    message: str


class DeploymentsStopResponse(TypedDict):
    success: Literal[True]
    status: Literal["ready", "stopped"]
    message: str


class AccountRetrieveSummaryResponseCounts(TypedDict):
    projects: int
    datasets: int
    models: int


class AccountRetrieveSummaryResponseTeamsItem(TypedDict):
    username: str
    fullName: NotRequired[str]
    role: str


class AccountRetrieveSummaryResponse(TypedDict):
    username: str
    name: str
    accountType: Literal["personal", "team"]
    plan: Literal["free", "pro", "enterprise"]
    creditsCents: int
    counts: AccountRetrieveSummaryResponseCounts
    teams: list[AccountRetrieveSummaryResponseTeamsItem]


class AccountListApiKeysResponseKeysItem(TypedDict):
    keyId: str
    name: str
    keyPrefix: str
    lastUsedAt: NotRequired[str]
    usageCount: float
    createdAt: str


class AccountListApiKeysResponse(TypedDict):
    keys: list[AccountListApiKeysResponseKeysItem]


class AccountCreateApiKeyResponse(TypedDict):
    keyId: str
    key: str
    keyPrefix: str
    name: str
    createdAt: str


class AccountRevokeApiKeyResponse(TypedDict):
    deleted: Literal[True]
    keyId: str


class AccountRetrieveStorageUsageResponseUsageProjects(TypedDict):
    current: float
    limit: float
    percent: float


class AccountRetrieveStorageUsageResponseUsageDatasets(TypedDict):
    current: float
    limit: float
    percent: float


class AccountRetrieveStorageUsageResponseUsageModels(TypedDict):
    current: float
    limit: float
    percent: float


class AccountRetrieveStorageUsageResponseUsageImages(TypedDict):
    current: float
    limit: float
    percent: float


class AccountRetrieveStorageUsageResponseUsageAnnotations(TypedDict):
    current: float


class AccountRetrieveStorageUsageResponseUsageDeployments(TypedDict):
    current: float
    limit: float
    percent: float


class AccountRetrieveStorageUsageResponseUsageStorage(TypedDict):
    current: float
    limit: float
    percent: float


class AccountRetrieveStorageUsageResponseUsage(TypedDict):
    projects: NotRequired[AccountRetrieveStorageUsageResponseUsageProjects]
    datasets: NotRequired[AccountRetrieveStorageUsageResponseUsageDatasets]
    models: NotRequired[AccountRetrieveStorageUsageResponseUsageModels]
    images: NotRequired[AccountRetrieveStorageUsageResponseUsageImages]
    annotations: NotRequired[AccountRetrieveStorageUsageResponseUsageAnnotations]
    deployments: NotRequired[AccountRetrieveStorageUsageResponseUsageDeployments]
    storage: AccountRetrieveStorageUsageResponseUsageStorage


class AccountRetrieveStorageUsageResponseBreakdownByCategoryDatasets(TypedDict):
    bytes: float
    count: float


class AccountRetrieveStorageUsageResponseBreakdownByCategoryModels(TypedDict):
    bytes: float
    count: float


class AccountRetrieveStorageUsageResponseBreakdownByCategoryExports(TypedDict):
    bytes: float
    count: float


class AccountRetrieveStorageUsageResponseBreakdownByCategory(TypedDict):
    datasets: AccountRetrieveStorageUsageResponseBreakdownByCategoryDatasets
    models: AccountRetrieveStorageUsageResponseBreakdownByCategoryModels
    exports: AccountRetrieveStorageUsageResponseBreakdownByCategoryExports


class AccountRetrieveStorageUsageResponseBreakdownTopItemsItem(TypedDict):
    _id: str
    name: str
    slug: NotRequired[str]
    sizeBytes: float
    type: Literal["project", "dataset", "model", "export"]
    parentName: NotRequired[str]
    parentSlug: NotRequired[str]


class AccountRetrieveStorageUsageResponseBreakdown(TypedDict):
    byCategory: AccountRetrieveStorageUsageResponseBreakdownByCategory
    topItems: list[AccountRetrieveStorageUsageResponseBreakdownTopItemsItem]


class AccountRetrieveStorageUsageResponse(TypedDict):
    tier: Literal["free", "pro", "enterprise"]
    usage: AccountRetrieveStorageUsageResponseUsage
    updatedAt: str | None
    breakdown: AccountRetrieveStorageUsageResponseBreakdown
    region: Literal["us", "eu", "ap"]
    username: str


class AccountRetrieveProfileSettingsResponseSocials(TypedDict):
    github: NotRequired[str]
    linkedin: NotRequired[str]
    twitter: NotRequired[str]
    discord: NotRequired[str]
    youtube: NotRequired[str]
    scholar: NotRequired[str]
    website: NotRequired[str]


class AccountRetrieveProfileSettingsResponse(TypedDict):
    displayName: str
    company: str
    useCase: str
    bio: str
    socials: NotRequired[AccountRetrieveProfileSettingsResponseSocials]
    plan: Literal["free", "pro", "enterprise"]
    username: str
    email: str
    imageUrl: str
    accountType: Literal["personal", "team"]
    iconColor: NotRequired[str]
    iconLetter: NotRequired[str]
    region: Literal["us", "eu", "ap"]


class AccountUpdateProfileSettingsResponse(TypedDict):
    success: Literal[True]


class AccountListCloudStorageIntegrationsResponseIntegrationsItem(TypedDict):
    id: str
    provider: Literal["gcs", "s3", "azure"]
    credentialIdentity: str
    targets: list[str]
    createdAt: str


class AccountListCloudStorageIntegrationsResponse(TypedDict):
    integrations: list[AccountListCloudStorageIntegrationsResponseIntegrationsItem]


class AccountConnectCloudStorageResponse(TypedDict):
    id: str
    provider: Literal["gcs", "s3", "azure"]
    credentialIdentity: str
    targets: list[str]
    createdAt: str


class AccountDiscoverCloudStorageLocationsResponse(TypedDict):
    targets: list[str]


class AccountBrowseCloudStorageObjectsResponseEntriesItem(TypedDict):
    kind: Literal["folder", "file"]
    name: str
    key: str
    size: NotRequired[float]
    updatedAt: NotRequired[str]


class AccountBrowseCloudStorageObjectsResponse(TypedDict):
    entries: list[AccountBrowseCloudStorageObjectsResponseEntriesItem]
    cursor: NotRequired[str]


class AccountRetrieveTrashResponseItemsItemParentProject(TypedDict):
    _id: str
    name: str
    slug: str


class AccountRetrieveTrashResponseItemsItem(TypedDict):
    _id: str
    type: Literal["project", "dataset", "model"]
    name: str
    slug: str
    trashedAt: str
    daysRemaining: int
    cascadedCount: NotRequired[int]
    parentProject: NotRequired[AccountRetrieveTrashResponseItemsItemParentProject]
    sizeBytes: NotRequired[float]


class AccountRetrieveTrashResponseSummaryByTypeProjects(TypedDict):
    count: int


class AccountRetrieveTrashResponseSummaryByTypeDatasets(TypedDict):
    count: int
    sizeBytes: float


class AccountRetrieveTrashResponseSummaryByTypeModels(TypedDict):
    count: int
    sizeBytes: float


class AccountRetrieveTrashResponseSummaryByTypeExports(TypedDict):
    count: int
    sizeBytes: float


class AccountRetrieveTrashResponseSummaryByType(TypedDict):
    projects: AccountRetrieveTrashResponseSummaryByTypeProjects
    datasets: AccountRetrieveTrashResponseSummaryByTypeDatasets
    models: AccountRetrieveTrashResponseSummaryByTypeModels
    exports: AccountRetrieveTrashResponseSummaryByTypeExports


class AccountRetrieveTrashResponseSummary(TypedDict):
    totalItems: int
    totalSizeBytes: float
    byType: AccountRetrieveTrashResponseSummaryByType


class AccountRetrieveTrashResponse(TypedDict):
    items: list[AccountRetrieveTrashResponseItemsItem]
    total: float
    page: int
    limit: int
    totalPages: int
    summary: AccountRetrieveTrashResponseSummary
    region: Literal["us", "eu", "ap"]


class AccountRestoreTrashedItemResponse(TypedDict):
    success: Literal[True]
    restoredModels: NotRequired[int]


class AccountPermanentlyDeleteTrashedItemResponse(TypedDict):
    success: Literal[True]
    deletedCount: int
    cascadedModels: NotRequired[int]


class AccountPermanentlyDeleteAllTrashedItemsResponseDeleted(TypedDict):
    projects: int
    datasets: int
    models: int
    deployments: int


class AccountPermanentlyDeleteAllTrashedItemsResponse(TypedDict):
    success: Literal[True]
    deleted: AccountPermanentlyDeleteAllTrashedItemsResponseDeleted
    totalDeleted: int


class AccountRetrieveIfUsernameIsAvailableResponse(TypedDict):
    available: bool
    username: str


class AccountRetrievePublicUserProfileResponseUserSocials(TypedDict):
    github: NotRequired[str]
    linkedin: NotRequired[str]
    twitter: NotRequired[str]
    discord: NotRequired[str]
    youtube: NotRequired[str]
    scholar: NotRequired[str]
    website: NotRequired[str]


class AccountRetrievePublicUserProfileResponseUser(TypedDict):
    username: str
    fullName: NotRequired[str]
    imageUrl: NotRequired[str]
    accountType: Literal["personal", "team"]
    iconColor: NotRequired[str]
    iconLetter: NotRequired[str]
    bio: NotRequired[str]
    company: NotRequired[str]
    useCase: NotRequired[str]
    socials: NotRequired[AccountRetrievePublicUserProfileResponseUserSocials]
    followerCount: int
    isFollowed: bool


class AccountRetrievePublicUserProfileResponse(TypedDict):
    user: AccountRetrievePublicUserProfileResponseUser


class AccountFollowOrUnfollowUserResponse(TypedDict):
    followed: bool
    followerCount: int


class AccountUploadWorkspaceIconResponse(TypedDict):
    success: Literal[True]
    downloadUrl: str


class AccountDeleteWorkspaceIconResponse(TypedDict):
    success: Literal[True]


class BillingRetrieveBalanceResponse(TypedDict):
    creditsCents: float
    plan: Literal["free", "pro", "enterprise"]


class BillingListTransactionsResponseTransactionsItemModel(TypedDict):
    name: str
    slug: str
    projectSlug: str
    username: str


class BillingListTransactionsResponseTransactionsItem(TypedDict):
    type: str
    amountCents: float
    balanceAfter: float
    modelId: NotRequired[str]
    period: NotRequired[str]
    createdAt: str
    receiptUrl: NotRequired[str | None]
    model: NotRequired[BillingListTransactionsResponseTransactionsItemModel]


class BillingListTransactionsResponse(TypedDict):
    transactions: list[BillingListTransactionsResponseTransactionsItem]


class BillingListUsageSummaryResponsePlan(TypedDict):
    planId: Literal["free", "pro", "enterprise"]
    name: str
    status: Literal["active", "past_due"]
    cancelAtPeriodEnd: bool
    paymentFailedAt: NotRequired[str]
    billingCycle: NotRequired[Literal["monthly", "yearly"]]
    currentPeriodEnd: NotRequired[str]
    enterpriseLicenseEnd: NotRequired[str]
    licenseExpired: NotRequired[bool]


class BillingListUsageSummaryResponseMetricsItem(TypedDict):
    metricId: Literal["storage_bytes"]
    kind: Literal["GAUGE"]
    period: Literal["NONE"]
    limit: float
    used: float
    remaining: float
    overageAllowed: bool


class BillingListUsageSummaryResponseTrainingCredit(TypedDict):
    monthlyGrant: float
    balanceAvailable: float


class BillingListUsageSummaryResponseFeatures(TypedDict):
    privateProjects: bool
    teams: bool
    enterpriseLicense: bool


class BillingListUsageSummaryResponse(TypedDict):
    plan: BillingListUsageSummaryResponsePlan
    metrics: list[BillingListUsageSummaryResponseMetricsItem]
    trainingCredit: BillingListUsageSummaryResponseTrainingCredit
    features: BillingListUsageSummaryResponseFeatures
    creditsCents: float
    paidSeats: NotRequired[float]
    currentSeats: NotRequired[float]
    maxSeats: NotRequired[float]
    nextInvoiceCents: NotRequired[float]


class ActivityListResponseEventsItem(TypedDict):
    _id: str
    userId: str
    userEmail: str
    userName: str
    action: Literal[
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
    ]
    resourceType: Literal[
        "project", "dataset", "model", "training", "export", "deployment", "settings", "onboarding", "api_key"
    ]
    resourceId: NotRequired[str]
    resourceName: NotRequired[str]
    metadata: NotRequired[dict[str, Any]]
    timestamp: str
    seen: bool
    archived: bool


class ActivityListResponseFilters(TypedDict):
    archived: bool
    search: NotRequired[str]
    start: NotRequired[str]
    end: NotRequired[str]


class ActivityListResponseActivityItem(TypedDict):
    _id: str
    userId: str
    userEmail: str
    userName: str
    action: Literal[
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
    ]
    resourceType: Literal[
        "project", "dataset", "model", "training", "export", "deployment", "settings", "onboarding", "api_key"
    ]
    resourceId: NotRequired[str]
    resourceName: NotRequired[str]
    metadata: NotRequired[dict[str, Any]]
    timestamp: str
    seen: bool
    archived: bool


class ActivityListResponse(TypedDict):
    events: NotRequired[list[ActivityListResponseEventsItem]]
    total: NotRequired[float]
    unseenCount: NotRequired[float]
    exportedAt: NotRequired[str]
    app: NotRequired[Literal["alpha"]]
    owner: NotRequired[str]
    filters: NotRequired[ActivityListResponseFilters]
    activity: NotRequired[list[ActivityListResponseActivityItem]]


class ActivityCreateMarkSeenResponse(TypedDict):
    success: Literal[True]


class ActivityArchiveResponse(TypedDict):
    success: Literal[True]


class ExploreRetrieveSearchResponseProjectsItem(TypedDict):
    _id: str
    slug: str
    name: str
    description: NotRequired[str]
    username: str
    visibility: Literal["public", "private"]
    iconColor: NotRequired[str]
    iconLetter: NotRequired[str]
    iconImage: NotRequired[str]
    modelCount: int
    modelNames: list[str]
    totalBytes: float
    starCount: int
    userImageUrl: NotRequired[str]
    updatedAt: str


class ExploreRetrieveSearchResponseDatasetsItemSplits(TypedDict):
    train: float
    val: float
    test: float
    labeled: float


class ExploreRetrieveSearchResponseDatasetsItemSampleImagesItemLabelsItem(TypedDict):
    classId: float
    bbox: NotRequired[list[float]]
    segments: NotRequired[list[float]]
    keypoints: NotRequired[list[float]]
    obb: NotRequired[list[float]]
    skeletonId: NotRequired[str]


class ExploreRetrieveSearchResponseDatasetsItemSampleImagesItem(TypedDict):
    url: str
    imageUrl: NotRequired[str]
    width: float
    height: float
    labels: NotRequired[list[ExploreRetrieveSearchResponseDatasetsItemSampleImagesItemLabelsItem]]


class ExploreRetrieveSearchResponseDatasetsItem(TypedDict):
    _id: str
    slug: str
    name: str
    description: NotRequired[str]
    username: str
    visibility: Literal["public", "private"]
    imageCount: int
    classCount: NotRequired[int]
    classNames: NotRequired[list[str]]
    classColors: NotRequired[dict[str, str]]
    task: Literal["detect", "segment", "semantic", "depth", "classify", "pose", "obb"]
    totalBytes: NotRequired[float]
    tags: NotRequired[list[str]]
    splits: NotRequired[ExploreRetrieveSearchResponseDatasetsItemSplits]
    kptShape: NotRequired[list[Any]]
    starCount: int
    sampleImages: list[ExploreRetrieveSearchResponseDatasetsItemSampleImagesItem]
    userImageUrl: NotRequired[str]
    updatedAt: str


class ExploreRetrieveSearchResponse(TypedDict):
    projects: list[ExploreRetrieveSearchResponseProjectsItem]
    datasets: list[ExploreRetrieveSearchResponseDatasetsItem]
    hasMore: bool


class ExploreRetrieveSidebarResponseProjectsItem(TypedDict):
    _id: str
    slug: str
    name: str
    modelCount: int
    iconColor: NotRequired[str]
    iconLetter: NotRequired[str]
    iconImage: NotRequired[str]


class ExploreRetrieveSidebarResponseDatasetsItem(TypedDict):
    _id: str
    slug: str
    name: str
    imageCount: NotRequired[int]
    thumbnail: NotRequired[str]


class ExploreRetrieveSidebarResponse(TypedDict):
    projects: list[ExploreRetrieveSidebarResponseProjectsItem]
    datasets: list[ExploreRetrieveSidebarResponseDatasetsItem]


class UploadRetrieveFileUrlResponse(TypedDict):
    sessionId: str
    uploadUrl: str
    expiresAt: str


class UploadCompleteResponseFile(TypedDict):
    size: float
    contentType: NotRequired[str]


class UploadCompleteResponse(TypedDict):
    success: Literal[True]
    file: UploadCompleteResponseFile


class TeamsListResponseTeamsItem(TypedDict):
    userId: str
    username: str
    fullName: NotRequired[str]
    imageUrl: NotRequired[str]
    iconColor: NotRequired[str]
    iconLetter: NotRequired[str]
    plan: Literal["free", "pro", "enterprise"]
    region: Literal["us", "eu", "ap"]
    role: str
    deniedReason: NotRequired[str]


class TeamsListResponse(TypedDict):
    teams: list[TeamsListResponseTeamsItem]


class TeamsCreateResponseTeam(TypedDict):
    userId: str
    username: str
    fullName: str
    iconColor: str
    iconLetter: str
    plan: str
    region: str
    role: str


class TeamsCreateResponse(TypedDict):
    team: TeamsCreateResponseTeam


class TeamsListMembersResponseMembersItem(TypedDict):
    userId: NotRequired[str]
    username: str
    email: str
    role: str
    status: Literal["pending", "active"]
    joinedAt: str
    imageUrl: NotRequired[str]
    invitedBy: NotRequired[str]
    inviteId: NotRequired[str]
    inviteCreatedAt: NotRequired[str]


class TeamsListMembersResponse(TypedDict):
    members: list[TeamsListMembersResponseMembersItem]
    maxSeats: float


class TeamsInviteResponse(TypedDict):
    invited: Literal[True]
    email: str


class TeamsChangeMemberRoleResponse(TypedDict):
    success: Literal[True]


class TeamsRemoveMemberOrLeaveResponse(TypedDict):
    success: Literal[True]


class TeamsTransferOwnershipResponse(TypedDict):
    success: Literal[True]
