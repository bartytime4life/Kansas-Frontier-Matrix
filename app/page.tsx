"use client";
import { withCivicKey } from "./map-keys";
import { civicCongressForDay, civicCongressLabel, civicDayForFrame, civicFrameVisible, civicRecordMatchesDay, civicTermStart, civicSourceForRecord, CIVIC_HISTORY_LIMITATION } from "./civic-history";
import { CIVIC_ID, CIVIC_LIMITATION, CIVIC_SOURCE } from "./civic-districts";
import { DEFLOCK_LIMITATION } from "./deflock";
import { TransportHistoryControl } from "./transport-history-control";
import "./transport-history.css";
import { CompactTimeSweep, type CalendarSourceRow } from "./compact-time-sweep";
import { CALENDAR_ARCHIVE_BOUNDS, calendarArchiveFeeds, calendarFrameDay, calendarVisibility, readCalendarSweep, type CalendarArchiveFeed, type CalendarFrameOutcome, type CalendarSweepView } from "./calendar-sweep";
import { EarthEngineComparisonPanel } from "./earth-engine-comparison-panel";
import { installExplorerMenuDismissal } from "./explorer-menu-dismissal";
import { countySearchGeometry, countySearchResults, globalSearchStatus } from "./county-search";
import { atlasDiscoveryResults, type GlobalSearchItem } from "./atlas-discovery";
import { isolateModalBackground, modalReturnTarget } from "./modal-background";
import { decodeStreamflowTransport } from "./streamflow-transport";
import { browserJsonRequest } from "./browser-json-request";
import { explorerHistoryParams, restoreArchiveViewDays, saveExplorerHistoryView } from "./explorer-layer-history";
import { LayerJsonReads } from "./layer-json-reads";
import { layerHitStack } from "./layer-hit-stack";
import { createMapHoverSampler } from "./map-hover-sampler";
import { FrameCheck } from "./frame-check";
import { MapStartersControl } from "./map-starters-control";
import { contextSelectionChanges, preferredContextIds, readContextPreference, starterPlan, type StarterAccessMap } from "./map-starters";
import type { MapMouseEvent } from "./maplibre-seam";
import { BasemapCacheControls } from "./basemap-cache-controls";
import { categoryMap, categorySceneLabel, type CategoryScene } from "./category-maps";
import { densityGroupCounts, PRISM_METRES_PER_PERSON_PER_SQUARE_MILE, setPopulationPrisms } from "./population-prisms";
import { REVIEWED_REASONS, REVIEWED_SOURCE_BY_TOPIC, REVIEWED_SOURCE_LABEL, useReviewedSnapshots, reviewedFeatureList, reviewedFeatureSummary } from "./reviewed-snapshots";
import { chartElevationKey, mapKeysFor, reliefElevationKey, withElevationKey, withReviewedKey } from "./map-keys";
import { REVIEWED_FEATURE_ID, REVIEWED_SOURCE_ID, setReviewedSnapshot } from "./reviewed-snapshot-layers";
import { verificationReading, verifyOutlook } from "./outlook-verification";
import { STORM_REPORTS_PAGE, STORM_REPORTS_SOURCE_ID, kansasReportList, reportClock, reportMagnitude, REPORT_KINDS, stormReportsKey, stormReportsReading, syncStormReports, validStormReports, type ReportDay, type StormReport, type StormReports } from "./storm-reports";
import { changeCollection, droughtChangeStart, countyChangeList, countyChangeReading, countyDroughtChange, droughtChangeKey, droughtChangeReading, type DroughtChangeWeeks, DROUGHT_NEWEST_REFRESH_MS, droughtCountyAtClick, DROUGHT_PLAY_STEP_MS, DROUGHT_PLAY_WEEKS, DROUGHT_SERIES_REFRESH_MS, usdmWeeksBefore, DROUGHT_SOURCE_ID, USDM_CATEGORIES, countyDroughtList, countyDroughtReading, countyDroughtShares, countyDroughtSummary, rememberDroughtMap, USDM_FIRST_DATE, USDM_PAGE, droughtKey, droughtReading, isUsdmDate, nextUsdmDate, previousUsdmDate, syncDroughtMonitor, usdmDateLabel, validDroughtMap, validDroughtSeries, type DroughtMap, type DroughtSeries } from "./drought-monitor";
import { SPC_OUTLOOK_PAGE, SPC_OUTLOOK_SOURCE_ID, isOutlookProduct, outlookProductName, outlookProducts, spcOutlookKey, spcOutlookReading, syncSpcOutlook, validSpcOutlook, type OutlookDay, type OutlookProduct, type SpcOutlook } from "./spc-outlook";
import { hiDpiBasemapStyle } from "./hd-rasters";
import { FLOOD_GAUGE_REFRESH_MS, floodGaugeApiPath, floodGaugeList, floodGaugePage, floodGaugeSummaries, floodHydrograph, floodKey, floodNetworkSummary, floodReading, parseFloodGauge, syncFloodSelection, FLOOD_SELECTED_SOURCE_ID, type FloodGauge } from "./flood-forecast";
import { annualCounts, EARTHQUAKE_RECORD_SOURCE_ID, recordEventList, recordPlots, earthquakeEventUrl, earthquakeRecordKey, recordYearColor, syncEarthquakeRecord, validEarthquakeRecord, type EarthquakeRecord, type EarthquakeRecordEvent } from "./earthquake-record";
import { PHOTOREAL_LANDSCAPES } from "./photoreal-landscapes";
import { AVIATION_TINT_BANDS, CATEGORY_BASEMAPS, RELIEF_RAMP } from "./category-basemaps";
import { isCategoryBasemapKey } from "./category-basemap-keys";
import { CategoryMapDock, nextSunStep, SUN_PLAY_RESTART_STEP, SUN_TIME_STEPS, type AquiferView } from "./category-map-dock";
import { evidenceSummary } from "./evidence-summary";
import "./evidence-summary.css";
import { AviationLayerControl } from "./aviation-layer-control";
import { AVIATION_RESEARCH_SOURCE } from "./aviation-research";
import { ExplorerGuide, readExplorerGuideDismissed, writeExplorerGuideDismissed, type ExplorerGuideAction } from "./explorer-guide";
import { hasExplorerDestination } from "./explorer-startup";
import { WelcomeFeatureGuide } from "./living-welcome/FeatureGuide.jsx";
import "./living-welcome/welcome.css";
import type { WelcomeFeatureDestination } from "./living-welcome/features";
import { captureBasemapSourceIds } from "../scripts/welcome-demos/capture-metrics.mjs";
import { basemapCacheRequest } from "./basemap-cache";
import { GROUNDWATER_CLASS_LEGENDS, GROUNDWATER_MANIFEST, safeKgsWellUrl } from "./aquifer-layers";
import { DEFAULT_SOIL_MAP_STATE, hideSoilContext, restoreSoilMapState, serializeSoilMapState, SOIL_VIEWS, soilLegendUrl, visibleExternalContextCount, type SoilMapState } from "./soil-moisture";
import { GovernedWaterControl } from "./governed-water-control";
import { GovernedWeatherControl } from "./governed-weather-control";
import { LivingWatersControl } from "./living-waters-control";
import { LIVING_WATERS_SOURCE } from "./living-waters-fixture";
import { resizeMapAfterLayout } from "./cutaway-locator";

import { lazy, Suspense, useCallback, useEffect, useMemo, useRef, useState } from "react";
import { InspectionPanelSwitch, useInspectionPanel } from "./inspection-panel";
import "./inspection-panel.css";
import "./explorer-controls.css";
import "./category-map-dock.css";
import "./atlas-studio.css";
import Link from "next/link";
import { BridgeRecordInspector } from "./bridge-record-inspector";
import { isBridgeLayer } from "./kansas-bridge-records";
import { BlmPlssInspector } from "./blm-plss-inspector";
import { isBlmPlssLayer } from "./blm-plss-records";
import { HmsSmokePlayback } from "./hms-smoke-playback-control";
import { HmsFrameTransitions, hmsFade } from "./hms-smoke-playback";
import { resetHmsSmokeFade, setHmsSmokeFade } from "./live-context";
import { createSettledMapCommit, geoJSONHasData, waitForGeoJSON } from "./map-performance";
import { installStormDeskPerformanceProbe, recordStormDeskFrame } from "./storm-desk-performance";
import { readBoundedJson } from "./bounded-json";
import { buildAvailabilityBins, timelineLabelSteps } from "./timeline-availability";
import { deriveMapSignals } from "./map-signals";
import { parseRepositoryObservation, type RepositoryConnection } from "./repository-status";
import { replaceExplorerHistory } from "./embed-runtime";
import { parseSavedWorkspaceList, writeSavedWorkspaceList } from "./saved-workspaces";
import ResearchPanel from "./research-panel";
import { countyResearch, researchCounties } from "./research-county";
import AssistantWorkspace from "./assistant/workspace";
import {sampleAssistantSelection, type AssistantFocus, type AssistantContext} from "./assistant-context";
import UndergroundPanel, { SubsurfaceInspector, type SubsurfaceInspection } from "./underground-panel-loader";
import { persistableSubsurface, validSubsurfaceContext, type SubsurfaceContext } from "./subsurface-model";
import researchStyles from "./research.module.css";
import { chooseResearchAnchor, readResearchInventory, nearbyResearch, providerResearchPoints, persistableResearch, researchIdentity, researchSourceUrl, validResearchRecord, validResearchContext, type ResearchContext, type ResearchCoverage, type ResearchRecord, type ResearchRadius } from "./research-context";
import { catalogDisplayStatus, catalogFilterMatches, type CatalogFilter, type CatalogStatus } from "./layer-workspaces";
import { BASELINE_STACKS, currentUtcDay } from "./daily-baseline";
import { SourceQualityRow } from "./source-quality-row";
import { sourceDownloadHref } from "./source-downloads";
import { readFireDay } from "./map-context-cache";
import { planOfficialRefresh } from "./official-refresh-plan";
import { ArchiveDaySlider } from "./archive-day-slider";
import { SoilMoistureControl, type SoilMoistureEngineContext } from "./soil-moisture-control";
import { CropCasmaControl } from "./crop-casma-control";
import { HistoricalTopoControl } from "./historical-topo-control";
import { LayerSourceNotices, RenderQualityControl } from "./map-toolbar";
import { HostedSourceStatus } from "./hosted-source-status";
import { drawWindFlowCanvas, nearestWindFlowSample, resetWindFlowCanvas, windFlowToneForBasemap, windToCompass } from "./wind-arrow-canvas";
import type { WaterPathAnalysis } from "./water-path-analysis";
import { drawWaterMotionCanvas } from "./water-motion-canvas";
import { readProgressiveDownstreamGuide, waterReadingCue, type DownstreamGuide, type DownstreamPath } from "./water-flow-context";
import { applyTopographicRasterDepth } from "./terrain-relief-style";
import { TerrainRasterViewTracker, terrainRasterErrorTile, terrainRasterTileInView, type TerrainRasterId } from "./terrain-raster-status";
import type { WindArrowFrame, WindArrowSample } from "./wind-arrow-data";
import { loadWindFlowFrame } from "./wind-flow-client";
import { EarthEngineDisplayControls } from "./earth-engine-display";
import { EarthEngineRasterFallback, type EarthEngineDisplayState } from "./earth-engine-raster-fallback";
import { useEarthEngineContext } from "./earth-engine-context-client";
import { EARTH_ENGINE_CONTEXT_LAYERS } from "./earth-engine-context";
import { applyProjectionNavigationLimits, GLOBE_VIEWPOINTS, REGIONAL_NAVIGATION_BOUNDS } from "./globe-context";
import { browserRenderBudget, controlOwnsMapSourceErrors, mapRuntimeErrorCode, readRenderQuality, sampleMapRuntimeHealth, QUALITY_STORAGE_KEY, type MapRuntimeCheckFailure, type RenderQuality } from "./map-performance";
import { webgl2Available } from "./webgl-support";
import { sameRecord, sameValues } from "./state-equality";
import type { Feature, FeatureCollection, Geometry } from "geojson";
import { loadMapLibre, type GeoJSONSource, type Map as MapLibreMap, type MapSourceDataEvent, type ScaleControl } from "./maplibre-seam";
import {
  CATEGORY_ORDER,
  findFeature,
  findLayerByRenderer,
  LAYER_REGISTRY,
  SEARCH_INDEX,
  TIME_STEPS,
  type EvidenceState,
  type FeatureProperties,
  type LayerRecord,
} from "./explorer-data";
import {
  applyDynamicMapEffects,
  applyRegistryState,
  applyTemporalRegistryFilters,
  applySceneEnvironment,
  areaSquareMiles,
  BASEMAPS,
  buildMeasurementData,
  distanceMiles,
  reorderRegistryLayers,
  setStructureExtrusions,
  setTerrainHeightOverlay as applyTerrainHeightOverlay,
  setTerrainPresentation as applyTerrainPresentation,
  setElevationExaggeration,
  setDaylightMapLayer,
  shouldFallbackStandardBasemap,
  isBasemapKey,
  VECTOR_BASEMAPS,
  terrainSourceLoadState,
  unexaggeratedTerrainElevation,
  TERRAIN_HILLSHADE_LAYER_ID,
  TERRAIN_HILLSHADE_SOURCE_ID,
  TERRAIN_COLOR_SOURCE_ID,
  TERRAIN_SOURCE_ID,
  terrainPresentationSourceMatches,
  type Structures3DState,
  type TerrainPresentationState,
  updateAnalysisAreaSource,
  updateImportPreviewSource,
  updateMeasurementSource,
  updateSelectionSource,
  type AtmospherePreset,
  type BasemapKey,
  type RegistryEvidenceFilter,
} from "./map-runtime";
import {
  MAP_CAPABILITY_GATES,
  MAP_VIEW_PROFILES,
  MAPLIBRE_REPOSITORY_STATUS,
  type MapUtilityView,
  type MapViewProfile,
  type MeasureUnit,
} from "./map-interface";
import {
  LIVING_ATLAS_VIEWS,
  livingAtlasStatusLabel,
  type LivingAtlasView,
} from "./living-atlas";
import {
  LIFECYCLE_GATES,
  REPOSITORY_SNAPSHOT,
  REPOSITORY_UPDATES,
  TRANSITION_BOUNDARIES,
  type RepositoryUpdateState,
} from "./repository-updates";
import { SITE_IDENTITY } from "./site-identity";
import { PUBLIC_SITE_ORIGIN } from "./crawler-discovery";
import {
  FEATURE_AREAS,
  FEATURE_CATALOG,
  featureMaturityLabel,
  type FeatureArea,
  type FeatureMaturity,
} from "./feature-catalog";
import {
  CORPUS_SNAPSHOT,
  CORPUS_SOURCES,
  SOURCE_ADMISSION_BY_ID,
  SOURCE_ADMISSION_STATES,
  SOURCE_CANDIDATES,
  SOURCE_DOMAINS,
  SOURCE_GAPS,
  type SourceAdmissionState,
} from "./source-intelligence";
import {
  buildFocusActionProposals,
  buildFocusGateTrace,
  FOCUS_INTENTS,
  focusIntentNarrative,
  focusResultForState,
  type FocusActionProposal,
  type FocusIntentId,
  type FocusStage,
} from "./focus-mode";
import { buildPublicSafeExport } from "./export-center";
import {
  FUNCTION_REGISTRY,
  functionsForGroup,
  type FunctionGroup,
  type FunctionRecord,
} from "./function-registry";
import { runtimeSeamStepForSelection, type RuntimeSeamState } from "./runtime-seam";
import {
  PLANNING_SCENARIO_MODES,
  PLANNING_SCENARIO_REVIEWS,
  type ScenarioReviewMode,
} from "./planning-scenario";
import { buildTemporalComparison } from "./temporal-comparison";
import {
  buildTemporalFrameSummary,
  buildTemporalQuery,
  buildTemporalSequence,
  isFeatureAvailableForTemporalQuery,
  nextTemporalFrame,
  temporalRecordsForQuery,
  type TemporalLoopMode,
  type TemporalPlaybackDirection,
  type TemporalStepRule,
  type TemporalSweepMode,
  type TemporalSweepQuery,
} from "./temporal-sweep";
import {
  buildLocalImportPreview,
  IMPORT_PREVIEW_MAX_BYTES,
  importPreviewAudit,
  type LocalImportPreview,
} from "./import-preview";
import {
  MAX_PLACE_TRAIL_STOPS,
  nextPlaceStopIndex,
  normalizePlaceStopName,
  reorderPlaceStops,
} from "./places-trail";
import ReportStoryWorkspaces from "./report-story-workspaces";
import { KDOT_HISTORIC_STATE_MAPS_URL, KDOT_PAST_COUNTY_MAPS_URL, ROAD_MAP_EDITIONS } from "./road-map-editions";
import { applyRoadStudyLayers, inspectRoadStudyFile as inspectRoadStudyGeoJson, ROAD_STUDY_COLORS, ROAD_STUDY_MAX_LAYERS, type RoadStudyLayer } from "./road-year-study";
import { buildFireReportContext, nearbyFireContext, type FireReportContext } from "./fire-report-analysis";
import { readDraftSnapshot } from "./workspace-storage";
import {
  policyDecisionFromEvidenceState,
  trustStateFromEvidenceState,
  type EvidenceRecord,
  type MapSnapshot,
  type StoryScene,
  type TrustState,
} from "./workspace-model";
import { ACTIVE_TERRAIN_SOURCE, STRUCTURE_3D_SOURCE, TERRAIN_SOURCES, TERRARIUM_RENDER_MAX_ZOOM, terrainSourceFor, type TerrainProvider } from "./terrain-sources";
import { setWaterFlowMotion, subscribeWaterFlowStatus, syncWaterFlow, waterFlowIsAnimating, waterFlowReading, type WaterFlowStatus } from "./water-flow-sync";
import { nightSkyIsTwinkling, setNightSkyTwinkle, syncBuildingStyle, syncKansasGlow, syncNightSky, syncNightSkyVisibility, syncRelief2d } from "./scene-overlays";
import { CURTAIN_MIN_PITCH, DEFAULT_SCENE_EFFECTS, KANSAS_FLYOVER, SCENE_EFFECT_KEYS, SCENE_EFFECT_OPTIONS, SCENE_LOOK_PRESETS, matchingLookPreset, effectiveSceneLight, applySelectionPulse, applyTerrainReliefStyle, curtainIsVisible, sceneEffectsForTopic, readSceneEffects, setCurtainShimmer, registerSceneEffects, registerSunInstant, sunSceneLight, syncBorderCurtain, syncBorderCurtainVisibility, writeSceneEffects, type SceneEffectSettings, type SceneView } from "./scene-effects";
import { SceneEffectsControls, ScenePanel } from "./scene-effects-controls";
import { DEFAULT_TERRAIN_DEPTH, terrainDepth, compositionDefaults, applyGroundView, applySceneComposition, sceneRecipePresentation, SCENE_RECIPES, type SceneComposition, type ScenePresentation, type SceneRecipe } from "./scene-studio";
import { createTerrainDrawing } from "./terrain-drawing-runtime";
import { TERRAIN_DRAWING_INITIAL_STATUS, type TerrainDrawingConfig, type TerrainDrawingMode, type TerrainDrawingStatus, type TerrainSurfaceMode, type TerrainSurfaceProbe } from "./terrain-drawing";
import { EXTERNAL_CONTEXT_SOURCES } from "./external-context-sources";
import { ExplorerControlsNavigation } from "./explorer-controls-navigation";
import { officialSourceTopics, specialtyLayerTopics, registryLayerTopics, atlasViewTopics, featureTopics, functionTopics, topicDefinition, topicSearchText, restoreTopic, serializeTopicSelection, imageryTopics, layerEntryMatches, selectedCatalogCount, type LayerCatalogEntry, type LayerBrowseView } from "./layer-workspaces";
import { TopicSelect, TopicGuide } from "./topic-navigation";
import { DISASTER_COVERAGE_HOLDS, LAYER_WORKSPACES, filterOfficialSources, sourceMinimumZoom, sourceNeedsCloserView, type LayerWorkspace, type TopicId } from "./layer-workspaces";
import {
  applyOfficialContextState,
  clearOfficialContextFeed,
  clearNoaaSatelliteFrame,
  defaultOfficialContextOpacity,
  defaultOfficialContextVisibility,
  OFFICIAL_CONTEXT_BY_ID,
  OFFICIAL_CONTEXT_BY_SOURCE_ID,
  officialContextForMapSource,
  OFFICIAL_CONTEXT_INTERACTIVE_LAYER_IDS,
  OFFICIAL_CONTEXT_PRESENT_FRAME,
  OFFICIAL_CONTEXT_SOURCES,
  OFFICIAL_CONTEXT_TEMPORAL_SUPPORT,
  TERRAIN_DISPLAY_MIN_ZOOM,
  commitNoaaRadarObservationTime,
  discardNoaaRadarStagedFrame,
  noaaRadarObservationTimeIsApplied,
  officialContextVisibilityForFrame,
  setNoaaRadarObservationTime,
  stageNoaaRadarObservationTime,
  setNoaaLightningObservationTime,
  setNoaaLightningGlow,
  setNoaaSatelliteFrame,
  type OfficialContextFeedId,
  type OfficialContextId,
  type OfficialContextPayload,
  type OfficialContextState,
} from "./live-context";
import { canonicalLightningTime, NOAA_LIGHTNING_LEGEND_URL, type LightningManifest } from "./lightning-data";
import { LightningFlashLoop } from "./lightning-flash-loop";
import {
  isNoaaRadarManifest,
  nextNoaaRadarFrameIndex,
  noaaRadarFrameAgeMinutes,
  noaaRadarManifestIsFresh,
  NOAA_RADAR_FRAME_API_PATH,
  NOAA_RADAR_LEGEND_URL,
  NOAA_RADAR_MAX_LOOP_FRAMES,
  NOAA_RADAR_PRODUCT_TITLE,
  NOAA_RADAR_SOURCE_TITLE,
  selectNoaaRadarLoopFrames,
  type NoaaRadarLoopSpanMinutes,
  type NoaaRadarManifest,
  type NoaaRadarManifestState,
  type NoaaRadarPlaybackSpeed,
} from "./noaa-radar";
import { isNoaaSatelliteManifest, NOAA_SATELLITE_FRAMES_PATH, type NoaaSatelliteFrame, type NoaaSatelliteManifest } from "./noaa-satellite";
import {
  buildStreamflowFrame,
  streamflowContextPayload,
  savedStreamflowLocations,
  restoreStreamflowLocations,
  normalizeUsgsStationId,
  parseStreamflowBundle,
  validStreamflowArchiveDay,
  restoreStreamflowArchiveDay,
  streamflowDisplayFrames,
  streamflowExactFrames,
  streamflowBundleForUtcDay,
  stationObservations,
  type StreamflowBundle,
  type StreamflowFrame,
  type RiverMapDisplay,
} from "./streamflow";
import { riverDrawerObservation } from "./evidence-drawer-observation";
import { drawerArtifactAttributes, parseUsgsStageDetail, type DrawerAttribute, type UsgsStageDetail } from "./evidence-drawer-data";
import { HydrologyObservatory,
  type HydrologyObservatoryState,
  type HydrologyPlaybackSpeed,
  type HydrologyRange,
} from "./hydrology-observatory";
import { AviationControl } from "./aviation-control";
import { boundedUtcDay, datedSourceDisplayStatus, earthquakeEventTimes, earthquakesThroughEvent, smokeInitialFrameIndex, smokeValidityTimes, smokeValidAt } from "./source-time";
import {
  NOAA_HYDROLOGY_NETWORK_API_PATH,
  noaaGaugeNetworkGeoJson,
  parseNoaaGaugeNetwork,
  type NoaaGaugeFeatureProperties,
} from "./noaa-hydrology";
import {
  currentKansasCalendarDay,
  DAYLIGHT_LOOP_DURATION_MS,
  dateRangeLoopFractionAtInstant,
  intervalFractionAtInstant,
  daylightLoopFraction,
  daylightShouldAutoplay,
  formatKansasSolarTime,
  instantAtIntervalFraction,
  instantAtDateRangeLoopFraction,
  kansasCalendarDaysInclusive,
  kansasLocalDateRangeInterval,
  kansasLocalDayInterval,
  restoreDaylightView,
  solarReferenceElevation,
} from "./daylight-layer";
import { daylightPhaseReading } from "./daylight-shader-layer";
import { formatMeasuredArea } from "./measurement-format";

/** How long each quarter-hour step of Play the day holds: 5:00 AM to 11:45 PM plays in about 15 seconds. */
const SUN_PLAY_STEP_MS = 200;

const KNOWN_TEMPORAL_FRAMES = new Set<number>([
  ...TIME_STEPS,
  ...LAYER_REGISTRY.flatMap((layer) => layer.temporal?.years ?? []),
]);

type ViewState = { center: [number, number]; zoom: number; bearing: number; pitch: number };
type MapBoundsState = { west: number; south: number; east: number; north: number };
type RuntimeState = { kind: "loading" | "ready" | "degraded" | "error" | "unsupported"; message: string };
type MapLibreRuntimeProbe = {
  version: string | null;
  workerConfigured: boolean;
  runtimeAssetsReady: boolean;
  webgl2: boolean | null;
  mapConstructed: boolean;
  canvasReady: boolean;
  styleLoaded: boolean;
  idle: boolean;
  tilesLoaded: boolean;
  controlsReady: boolean;
  interactionsReady: boolean;
  sourcesReady: number;
  projection: "mercator" | "globe";
  error: string | null;
  failedChecks: readonly MapRuntimeCheckFailure[];
};
type DrawerView = "evidence" | "metadata" | "lineage" | "focus";
type LeftPanelMode = "views" | "layers" | "live" | "places" | "stories";
type MeasureMode = "point" | "distance" | "area" | null;
type PlaybackSpeed = 0.5 | 1 | 2;
type NoaaRadarFrameLoadState = "idle" | "loading" | "ready" | "error";
type BoxDragMode = "zoom" | "report-area";
type TerrainProfileSample = Readonly<{ distanceMiles: number; elevationMeters: number }>;
type TerrainElevationReading = Readonly<{ longitude: number; latitude: number; meters: number; feet: number; provider: TerrainProvider }>;
type WindArrowHover = Readonly<{ sample: WindArrowSample; screenX: number; screenY: number }>;
type RepositoryView = "updates" | "functions" | "scenario" | "runtime" | "transitions" | "readiness" | "sources";
type SourceObservatoryView = "candidates" | "corpus" | "gaps";
type GovernedRoute = "/bootstrap" | "/layers" | "/evidence" | "/focus";
type GovernedMethod = "GET" | "POST";
type PublicWorkspaceId = "explore" | "knowledge" | "features" | "trust";
type PrimaryWorkspace = "map" | "reports" | "stories";
type ReportScope = "VIEWPORT" | "ANALYSIS_AREA" | "VISIBLE_LAYERS" | "SELECTION";
type ReportDetail = "EXECUTIVE" | "STANDARD" | "TECHNICAL";
type ReportSection = "summary" | "findings" | "records" | "evidence" | "limitations";
type WorkspaceSnapshot = Readonly<{
  id: string;
  name: string;
  savedAt: string;
  view: ViewState;
  // Optional for device-local v1 compatibility; missing legacy markers fail closed on restore.
  locationCameraRedacted?: boolean;
  researchContext?: ResearchContext;
  subsurfaceContext?: SubsurfaceContext;
  visibility: Record<string, boolean>;
  opacity: Record<string, number>;
  layerOrder: string[];
  year: number;
  mapEvidenceFilter?: RegistryEvidenceFilter;
  basemap: BasemapKey;
  projection: "mercator" | "globe";
  scene?: {
    preset: ScenePresetId;
    verticalExaggeration: number;
    atmosphere: AtmospherePreset;
    lightAzimuth: number;
    fieldOfView: number;
  };
  measurement?: {
    mode: Exclude<MeasureMode, null>;
    unit: MeasureUnit;
    label: string;
    coordinates: [number, number][];
  } | null;
  analysisArea?: MapBoundsState | null;
  temporalComparison?: {
    timeA: number;
    timeB: number;
  };
  temporalSweep?: {
    mode: TemporalSweepMode;
    stepRule: TemporalStepRule;
    rangeStart: number;
    rangeEnd: number;
    windowFrames: number;
    direction: TemporalPlaybackDirection;
    loopMode: TemporalLoopMode;
  };
  report: {
    title: string;
    scope: ReportScope;
    detail: ReportDetail;
    layerIds: string[];
    sections: Record<ReportSection, boolean>;
    query: string;
    evidenceFilter: EvidenceState | "ALL";
  };
  selection: { layerId: string; featureId: string } | null;
}>;
type MapQueryCandidate = Readonly<{
  featureId: string;
  layerId: string;
  title: string;
  layerTitle: string;
  evidenceState: EvidenceState;
  sourceYear: number;
}>;
type ScenePresetId = "overview-2d" | "globe-overview" | "water-systems" | "smoke-context" | "elevation-3d" | "tile-grid";
type HoverSummary = Readonly<{
  id: string;
  title: string;
  subtitle: string;
  state: string;
}>;

type SelectedContext = {
  kind: "registry" | "basemap";
  featureId: string;
  layerId: string;
  layer: LayerRecord;
  properties: FeatureProperties;
  geometry: Feature<Geometry>;
  externalStationId?: string | null;
  externalFeatureId?: string | null;
  externalAttributes?: readonly DrawerAttribute[];
  civicRecord?: { sourceDay: string | null; congressNumber: number | null; termStart: string | null; termEndExclusive: string | null };
};

type StageDrawerLoad = { stationId: string; status: "loading" | "ready" | "error"; detail?: UsgsStageDetail };

const officialContextIdForSelection = (selection: SelectedContext | null): OfficialContextId | null => {
  if (!selection?.featureId.startsWith("official-context:")) return null;
  return OFFICIAL_CONTEXT_SOURCES.find((source) => selection.layerId === `official-context-${source.id}`)?.id ?? null;
};

const officialSelectionIsHeld = (selection: SelectedContext | null, frame: number, buildCurrent: boolean, civicDay: string | null) => Boolean(
  selection?.featureId.startsWith("official-context:")
  && (!buildCurrent || (officialContextIdForSelection(selection) === CIVIC_ID
    ? !civicRecordMatchesDay(selection?.civicRecord, civicDay)
    : frame !== OFFICIAL_CONTEXT_PRESENT_FRAME)),
);

const selectionCarrierIsVisible = (
  selection: SelectedContext | null,
  registryVisibility: Record<string, boolean>,
  effectiveOfficialVisibility: Record<OfficialContextId, boolean>,
) => {
  if (!selection) return false;
  if (selection.kind === "registry") return registryVisibility[selection.layerId] === true;
  const officialContextId = officialContextIdForSelection(selection);
  return officialContextId
    ? effectiveOfficialVisibility[officialContextId] === true
    : true;
};

const selectionPassesEvidenceFilter = (selection: SelectedContext | null, filter: RegistryEvidenceFilter) => (
  !selection
  || selection.kind !== "registry"
  || filter === "ALL"
  || selection.properties.evidenceState === filter
);

const BASEMAP_CONTEXT_LAYER: LayerRecord = {
  id: "basemap-context",
  title: "Standard vector basemap",
  description: "Open geographic context from the selected basemap style. It is a display carrier, not KFM evidence.",
  domain: "Basemap context",
  category: "Reference boundaries & locators",
  sourceType: "Vector tiles",
  sourceId: "openfreemap-vector-context",
  datasetName: "OpenFreeMap / OpenMapTiles / OpenStreetMap context",
  geometryType: "Mixed",
  minZoom: 0,
  maxZoom: 20,
  defaultVisibility: true,
  defaultOpacity: 1,
  legend: [{ label: "External geographic context", color: "#b9edf1", shape: "line" }],
  units: "display context",
  scaleNote: "Provider-rendered vector geometry; inspect source attribution before reuse",
  validTimeExtent: "Provider-defined",
  sourceTime: "Provider-defined",
  releaseTime: "External display service",
  freshnessState: "NOT_APPLICABLE",
  attribution: "OpenFreeMap · OpenMapTiles · OpenStreetMap",
  evidenceReference: "No KFM EvidenceBundle attached",
  publicStatus: "GENERALIZED",
  sensitivityNote: "Basemap geometry is context only. It is not a KFM release, source admission, or evidence resolution.",
  releaseState: "GENERALIZED",
  correctionNote: "Provider corrections and update cadence are external to this Site and are not asserted here.",
  relatedLayers: [],
  interactions: ["hover", "select", "zoom", "inspect"],
  filters: [],
  viewingModes: ["2D", "globe", "terrain"],
  bounds: [-104.8, 34.8, -92, 42.2],
  data: { type: "FeatureCollection", features: [] },
  renderers: [],
};

const DOMAIN_HOLDS = Object.freeze([
  { domain: "Soil", state: "HELD", detail: "No admitted public-safe soil adapter is connected in this Site." },
  { domain: "Weather", state: "PUBLIC-SAFE", detail: "NWS alert areas and a time-enabled NOAA radar loop are available as optional official operational context; they are not admitted evidence, forecasts, or an all-clear." },
  { domain: "Smoke", state: "PUBLIC-SAFE", detail: "NOAA HMS satellite-analyzed smoke footprints are available as bounded external context; synthetic smoke, model transport, surface PM2.5, fire perimeters, and advisories remain separate." },
  { domain: "Air Quality", state: "HELD", detail: "No governed air-quality source, freshness contract, or public-safe release is connected." },
  { domain: "Natural Resources", state: "HELD", detail: "No public-safe resource inventory or rights-cleared layer is connected." },
  { domain: "Roads", state: "PUBLIC-SAFE", detail: "Real road context is available through the external vector basemap; KFM road evidence remains generalized." },
  { domain: "Rail", state: "PUBLIC-SAFE", detail: "Real rail context is available through the external vector basemap; KFM rail evidence remains generalized." },
  { domain: "Trade Routes", state: "HELD", detail: "No admitted historical trade-route source is connected." },
  { domain: "Cities", state: "PUBLIC-SAFE", detail: "City labels are available from the external vector basemap; KFM place fixtures remain explicit." },
  { domain: "Infrastructure", state: "HELD", detail: "No governed asset inventory or rights-cleared infrastructure layer is connected." },
  { domain: "Archaeology", state: "RESTRICTED", detail: "No precise archaeology layer is exposed; generalized story seams remain the safe extension point." },
  { domain: "Historical Geography", state: "HELD", detail: "No admitted historical boundary or archival map layer is connected." },
  { domain: "People / Land", state: "RESTRICTED", detail: "The Site does not expose person-level, parcel-level, or sensitive land detail." },
  { domain: "Terrain / Elevation", state: "PUBLIC-SAFE", detail: "External DEM terrain plus optional USGS 3DEP mosaic hillshade and slope are display context only; raw point clouds and governed KFM elevation evidence remain held." },
  { domain: "Imagery", state: "PUBLIC-SAFE", detail: "Optional attributed imagery is display context only; it is never KFM evidence." },
] as const);

const officialContextStateLabel = (state: OfficialContextState) => ({
  idle: "NOT LOADED",
  loading: "LOADING",
  ready: "READY",
  empty: "NO RESULTS",
  partial: "PARTIAL",
  error: "UNAVAILABLE",
}[state]);

// Open on Kansas Overview: a paused, north-up 2D statewide orientation.
// Terrain, globe, and local investigation cameras remain explicit actions.
const KANSAS_VIEW: ViewState = { center: [-98.38, 38.48], zoom: 5.45, bearing: 0, pitch: 0 };
/** Glow, 2D relief and building light. Decorative: each step
 * fails on its own and never marks the map runtime degraded. */
const syncSceneOverlays = (map: MapLibreMap, light: AtmospherePreset, azimuth: number, efficient: boolean) => {
  for (const step of [
    () => syncKansasGlow(map, light, azimuth),
    () => syncRelief2d(map, ACTIVE_TERRAIN_SOURCE, light, azimuth),
    () => syncBuildingStyle(map, light, azimuth),
    () => syncNightSky(map, light, azimuth, efficient),
    () => syncWaterFlow(map, { light, azimuth, efficient, gaugeSourceId: OFFICIAL_CONTEXT_BY_ID["usgs-streamflow"].sourceId, gaugeLayerId: OFFICIAL_CONTEXT_BY_ID["usgs-streamflow"].layerIds[1] }),
  ]) {
    try { step(); } catch { /* one overlay failing never blocks the others */ }
  }
};
const STRUCTURE_FOCUS_PRESETS = Object.freeze([
  Object.freeze({ id: "wichita", label: "Focus Wichita", center: [-97.3375, 37.6872] as [number, number], bearing: -24 }),
  Object.freeze({ id: "topeka", label: "Focus Topeka", center: [-95.689, 39.0473] as [number, number], bearing: 28 }),
  Object.freeze({ id: "ellsworth", label: "Focus Ellsworth", center: [-98.2306, 38.7306] as [number, number], bearing: -18 }),
] as const);
const EXPECTED_MAPLIBRE_VERSION = "6.9.0";
const MAPLIBRE_WORKER_URL = "/maplibre/maplibre-gl-worker.mjs";
const MAPLIBRE_RUNTIME_ASSET_URLS = [MAPLIBRE_WORKER_URL, "/maplibre/maplibre-gl-shared.mjs"] as const;
const SUPPORTED_CONTEXT_BOUNDS = Object.freeze({ west: -104.8, south: 34.8, east: -92, north: 42.2 });
const DEFAULT_MAP_PROFILE = MAP_VIEW_PROFILES.find((profile) => profile.id === "overview")!;
const defaultVisibility = Object.fromEntries(LAYER_REGISTRY.map((layer) => [layer.id, DEFAULT_MAP_PROFILE.visibleLayerIds.includes(layer.id)]));
const defaultOpacity = Object.fromEntries(LAYER_REGISTRY.map((layer) => [layer.id, layer.defaultOpacity]));
const defaultReportLayerIds = LAYER_REGISTRY.filter((layer) => defaultVisibility[layer.id]).map((layer) => layer.id);
const defaultOfficialVisibility = defaultOfficialContextVisibility();
const defaultOfficialOpacity = defaultOfficialContextOpacity();
const defaultOfficialStates = Object.fromEntries(OFFICIAL_CONTEXT_SOURCES.map((source) => [source.id, "idle"])) as Record<OfficialContextId, OfficialContextState>;
const officialContextRuntimeVisibility = (
  visibility: Record<OfficialContextId, boolean>,
  frame: number,
  noaaRadarReady: boolean,
  noaaRadarFrameTime: string | null,
  buildYearCurrent = true,
  calendarDay: string | null = null,
  checkedDays: Partial<Record<OfficialContextId, string>> = {},
) => {
  const base = officialContextVisibilityForFrame(visibility, frame, buildYearCurrent);
  const currentOnly = OFFICIAL_CONTEXT_SOURCES.filter(source => {
    const frames = OFFICIAL_CONTEXT_TEMPORAL_SUPPORT[source.id].supportedFrames;
    return frames.length === 1 && frames[0] === OFFICIAL_CONTEXT_PRESENT_FRAME;
  }).map(source => source.id);
  const next = calendarVisibility(base, visibility, calendarDay, frame, currentUtcDay(), checkedDays, currentOnly, buildYearCurrent);
  next[CIVIC_ID] = civicFrameVisible(visibility[CIVIC_ID], frame, OFFICIAL_CONTEXT_PRESENT_FRAME, currentUtcDay(), calendarDay, checkedDays[CIVIC_ID], buildYearCurrent);
  next["nws-radar"] = next["nws-radar"] && noaaRadarReady && Boolean(noaaRadarFrameTime);
  return next;
};
const checkedCalendarDays = (days: Partial<Record<OfficialContextFeedId, string>>, payloads: Partial<Record<OfficialContextFeedId, OfficialContextPayload>>): Partial<Record<OfficialContextId, string>> =>
  Object.fromEntries((Object.keys(CALENDAR_ARCHIVE_BOUNDS) as CalendarArchiveFeed[]).flatMap(feed => {
    const payload = payloads[feed], day = days[feed];
    return day && payload?.feed === feed && (feed !== CIVIC_ID || payload.sourceDay === day) && ["ready", "partial", "empty"].includes(payload.state) ? [[feed, day]] : [];
  }));
const defaultOrder = LAYER_REGISTRY.map((layer) => layer.id);
const interactiveLayerIds = LAYER_REGISTRY.flatMap((layer) => layer.renderers.filter((renderer) => renderer.interactive).map((renderer) => renderer.id));
const layerDomains = ["ALL", ...Array.from(new Set([...LAYER_REGISTRY.map((layer) => layer.domain), ...DOMAIN_HOLDS.map((hold) => hold.domain)])).sort()] as const;
const DOMAIN_LIVE_CONTEXT: Readonly<Partial<Record<(typeof layerDomains)[number], readonly OfficialContextId[]>>> = Object.freeze({
  Fire: Object.freeze(["nasa-firms-active-fire", "noaa-hms-smoke"] as const),
  Hydrology: Object.freeze(["usgs-streamflow", "noaa-nwps-gauges", "usgs-3dhp-hydrography", "usgs-wbd-watersheds"] as const),
  Geology: Object.freeze(["usgs-earthquakes"] as const),
  Atmosphere: Object.freeze(["noaa-hms-smoke", "nws-forecast-wind"] as const),
});
const catalogCategorySlug = (category: string) => category.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
const FOCUSABLE_SELECTOR = "button:not([disabled]), input:not([disabled]), select:not([disabled]), textarea:not([disabled]), summary, a[href], [tabindex]:not([tabindex='-1'])";
const visibleFocusableElements = (container: HTMLElement) => Array.from(container.querySelectorAll<HTMLElement>(FOCUSABLE_SELECTOR)).filter((element) => {
  if (!(element.tabIndex >= 0 && !element.closest("[hidden], [inert]") && element.getClientRects().length > 0)) return false;
  for (let ancestor = element.parentElement; ancestor && container.contains(ancestor); ancestor = ancestor.parentElement) {
    if (ancestor instanceof HTMLDetailsElement && !ancestor.open && ancestor.querySelector(":scope > summary") !== element) return false;
  }
  return true;
});
const drawerViews = ["evidence", "metadata", "lineage", "focus"] as const satisfies readonly DrawerView[];
const drawerViewLabels: Record<DrawerView, string> = {
  evidence: "Data",
  metadata: "Metadata",
  lineage: "Trace",
  focus: "Focus",
};
const mapUtilityLabels: Record<MapUtilityView, string> = {
  report: "Report",
  navigate: "Appearance",
  inspect: "Inspect",
  scene: "Appearance",
  history: "Kansas historic maps",
  connections: "Sources",
  import: "Import",
  compare: "Compare",
  measure: "Measure",
  export: "Export",
  diagnostics: "Diagnostics",
};
const mapUtilityDescriptions: Record<MapUtilityView, string> = {
  report: "Build a report from the current map, time, layers, and selection.",
  inspect: "Find a feature and inspect its evidence context.",
  navigate: "Adjust the map appearance. Legacy navigation links open this panel.",
  scene: "Adjust the current terrain and 3D view.",
  history: "Find dated USGS sheet editions near this map view.",
  connections: "Check the sources behind the current map.",
  import: "Preview a local KML or GeoJSON file in this browser.",
  compare: "Compare selected layers and times.",
  measure: "Draw and measure on this map.",
  export: "Review what the map can safely export.",
  diagnostics: "Check map health and recovery options.",
};
const QUICK_LIVE_CONTEXT_IDS = [
  "usgs-streamflow",
  "usgs-earthquakes",
  "nasa-gibs-fire-points",
  "nifc-fire-reports",
  "noaa-goes-geocolor",
  "noaa-hms-smoke",
  "nws-radar",
] as const satisfies readonly OfficialContextId[];
const REPORT_SECTIONS: readonly Readonly<{ id: ReportSection; label: string; detail: string }>[] = Object.freeze([
  Object.freeze({ id: "summary", label: "Summary", detail: "Scope, time, record, and layer totals" }),
  Object.freeze({ id: "findings", label: "Findings", detail: "Deterministic observations from the filtered records" }),
  Object.freeze({ id: "records", label: "Record table", detail: "Feature-level data rows and evidence states" }),
  Object.freeze({ id: "evidence", label: "Evidence notes", detail: "Source roles, citations, freshness, and release posture" }),
  Object.freeze({ id: "limitations", label: "Limitations", detail: "Generalization, uncertainty, and use boundaries" }),
]);
const defaultReportSections: Record<ReportSection, boolean> = {
  summary: true,
  findings: true,
  records: true,
  evidence: true,
  limitations: true,
};
const escapeReportHtml = (value: unknown) => String(value)
  .replaceAll("&", "&amp;")
  .replaceAll("<", "&lt;")
  .replaceAll(">", "&gt;")
  .replaceAll('"', "&quot;")
  .replaceAll("'", "&#039;");

// Transient display projection only: never a ReportDraft, EvidenceRef or release.
type ProviderReportSelection = Readonly<{
  kind: "basemap";
  role: "EXTERNAL_CONTEXT_ONLY";
  evidenceBundle: null;
  status: "AVAILABLE" | "WITHHELD" | "INCOMPATIBLE";
  boundary: string;
  context: null | Readonly<{
    id: string; title: string; layer: string; summary: string;
    sourceOrganization: string; sourceUrl: string | null; sourceTime: string;
    observedAt: string | null; providerUpdatedAt: string | null; retrievedAt: string | null;
    sourceState: string; fieldBasis: string; attributes: readonly DrawerAttribute[];
    attribution: string; sourceBoundary: string; limitation: string;
  }>;
}>;
// Counts describe KFM records; provider context keeps its own bounded status.
const emptyReportFindings = (status: ProviderReportSelection["status"] | null, catalogEmpty: boolean): string[] => [
  "No KFM records match this report's scope and filters.",
  catalogEmpty
    ? "No KFM domain records are currently released in this application. Provider-backed map layers remain separate source context."
    : "Adjust the scope, time, or filters to inspect available KFM records.",
  status === "AVAILABLE"
    ? "One selected provider record is included as external source context, with its own source time, attribution, and use limits. It is not a released KFM record."
    : status === "WITHHELD"
      ? "Selected provider context is withheld; no source details are included."
      : status === "INCOMPATIBLE"
        ? "Selected provider context is excluded because it is incompatible with the active map time."
        : "Select a provider-backed map feature and choose Create report to preserve its source context.",
];
const buildProviderReportSelection = (input: {
  selected: SelectedContext | null; timeMismatch: boolean; locationPrivate: boolean;
  source?: (typeof OFFICIAL_CONTEXT_SOURCES)[number]; attributes: readonly DrawerAttribute[];
  attributesCurrent: boolean; sourceState?: string; sourceUrl?: string;
  observedAt?: string | null; providerUpdatedAt?: string | null; retrievedAt?: string | null;
  limitation?: string | null;
}): ProviderReportSelection | null => {
  const { selected } = input;
  if (!selected || selected.kind !== "basemap") return null;
  const boundary = "External source context only. No KFM EvidenceBundle attached; this report does not admit, review, release, or publish provider data.";
  const withheld = { kind: "basemap", role: "EXTERNAL_CONTEXT_ONLY", evidenceBundle: null, status: "WITHHELD", boundary, context: null } as const;
  // Check privacy before copying identifiers, labels, source URLs or attributes:
  // each can reconstruct a private/local selection even without its geometry.
  if (input.locationPrivate) return withheld;
  const { source } = input;
  if (!source || source.id !== officialContextIdForSelection(selected)
    || selected.properties.releaseState === "RESTRICTED"
    || ["DENIED_BY_POLICY", "RESTRICTED_ACCESS"].includes(selected.properties.evidenceState)) return withheld;
  if (input.timeMismatch) return { ...withheld, status: "INCOMPATIBLE" };
  const text = (value: unknown, maximum: number) => typeof value === "string" ? value.trim().slice(0, maximum) : "";
  const timestamp = (value: unknown) => typeof value === "string" && value.length <= 80 && Number.isFinite(Date.parse(value)) ? value : null;
  // Source use limits and any distinct selection note survive independently
  // of feed availability caveats. Prefer the allowlisted source when bounded.
  const sourceBoundary = [...new Set([text(source.boundary, 4000), text(selected.properties.generalizationNote, 4000)].filter(Boolean))].join(" ").slice(0, 4000);
  return {
    kind: "basemap", role: "EXTERNAL_CONTEXT_ONLY", evidenceBundle: null, status: "AVAILABLE", boundary,
    context: {
      id: text(selected.featureId, 180), title: text(selected.properties.title, 240), layer: text(selected.layer.title, 240),
      summary: text(selected.properties.summary, 2000), sourceOrganization: text(source.organization, 240),
      sourceUrl: researchSourceUrl(input.sourceUrl ?? source.sourceUrl),
      // Provider source time is separate from the report's active map time.
      sourceTime: text(selected.properties.temporalScope, 500),
      observedAt: timestamp(input.observedAt), providerUpdatedAt: timestamp(input.providerUpdatedAt), retrievedAt: timestamp(input.retrievedAt),
      sourceState: text(input.sourceState, 80) || "Not available",
      fieldBasis: input.attributesCurrent ? "Latest loaded matching provider fields; summary and source time retain the selected map snapshot." : "Selected map snapshot; reselect after a feed update to refresh its fields.",
      attributes: input.attributes.slice(0, 32).map((attribute) => ({ label: text(attribute.label, 100), value: text(attribute.value, 240) })).filter((attribute) => attribute.label && attribute.value),
      attribution: text(source.attribution, 1000), sourceBoundary, limitation: text(input.limitation ?? selected.properties.uncertainty, 4000),
    },
  };
};
const providerReportHtml = (selection: ProviderReportSelection | { kind: "registry" } | null) => {
  if (!selection || selection.kind !== "basemap") return "";
  const context = selection.context;
  const heading = `<section aria-label="Selected provider source context"><h2>Selected provider source context</h2><p class="boundary"><strong>EXTERNAL_CONTEXT_ONLY · No KFM EvidenceBundle attached</strong><br>${escapeReportHtml(selection.boundary)}</p>`;
  if (!context) return `${heading}<p>${selection.status === "INCOMPATIBLE" ? "Selection is incompatible with the active map time; source details are omitted." : "Selection details are withheld for privacy or unavailable public provenance."}</p></section>`;
  const facts = [
    ["Provider", context.sourceOrganization], ["Source time / edition", context.sourceTime],
    ["Observation time", context.observedAt ?? "Not available"], ["Provider update time", context.providerUpdatedAt ?? "Not available"],
    ["Retrieved", context.retrievedAt ?? "Not available"], ["Response state", context.sourceState], ["Field basis", context.fieldBasis],
    ...context.attributes.map((attribute) => [attribute.label, attribute.value]),
  ];
  return `${heading}<h3>${escapeReportHtml(context.title)}</h3><p>${escapeReportHtml(context.summary)}</p><p>${escapeReportHtml(context.layer)} · <code>${escapeReportHtml(context.id)}</code></p><dl>${facts.map(([label, value]) => `<dt>${escapeReportHtml(label)}</dt><dd>${escapeReportHtml(value)}</dd>`).join("")}</dl>${context.sourceUrl ? `<p><a href="${escapeReportHtml(context.sourceUrl)}" rel="noreferrer">Open provider source</a></p>` : ""}<p><strong>Source use boundary:</strong> ${escapeReportHtml(context.sourceBoundary)}</p><p><strong>Response / availability limitation:</strong> ${escapeReportHtml(context.limitation)}</p><p><strong>Attribution:</strong> ${escapeReportHtml(context.attribution)}</p></section>`;
};
const validLayerPayload = (value: unknown, feed: OfficialContextFeedId, day?: string): boolean => {
  if (!value || typeof value !== "object") return false;
  const payload = value as Partial<OfficialContextPayload>;
  return payload.feed === feed && (!day || (payload.sourceDay === undefined && feed !== "nasa-gibs-fire-points" && feed !== CIVIC_ID) || payload.sourceDay === day)
    && ["ready", "empty", "partial"].includes(payload.state ?? "")
    && payload.data?.type === "FeatureCollection" && Array.isArray(payload.data.features)
    && payload.featureCount === payload.data.features.length
    && typeof payload.retrievedAt === "string" && Number.isFinite(Date.parse(payload.retrievedAt));
};

const governedRoutes = new Set<GovernedRoute>(["/bootstrap", "/layers", "/evidence"]);

const loadConfiguredMapLibre = async () => {
  await Promise.all(MAPLIBRE_RUNTIME_ASSET_URLS.map(async (url) => {
    const response = await fetch(url, { method: "HEAD", cache: "force-cache" });
    if (!response.ok) throw new Error(`MapLibre runtime asset unavailable (${response.status})`);
    await response.body?.cancel();
  }));
  const mapLibre = await loadMapLibre();
  mapLibre.setWorkerUrl(MAPLIBRE_WORKER_URL);
  const renderBudget = browserRenderBudget();
  mapLibre.setMaxParallelImageRequests(renderBudget.imageRequests);
  mapLibre.setWorkerCount(Math.max(1, Math.min(renderBudget.workerCount, Math.floor((navigator.hardwareConcurrency || 4) / 2))));
  const version = mapLibre.getVersion();
  if (version !== EXPECTED_MAPLIBRE_VERSION) throw new Error(`Expected MapLibre ${EXPECTED_MAPLIBRE_VERSION}, received ${version}`);
  if (mapLibre.getWorkerUrl() !== MAPLIBRE_WORKER_URL) throw new Error("MapLibre worker configuration did not persist");
  return { mapLibre, version };
};
const WORKSPACE_STORAGE_KEY = "kfm-map-workspaces-v1";
const inspectGovernedRoute = (method: GovernedMethod, path: GovernedRoute) => {
  const registered = governedRoutes.has(path);
  const supported = registered && method === "GET";
  const status = supported ? 200 : registered ? 405 : 404;
  return {
    http_status: status,
    deployment_posture: "CODE_SHAPE_NOT_DEPLOYED",
    envelope: {
      id: `site-fixture:${method.toLowerCase()}:${path.slice(1) || "root"}`,
      spec_hash: "SITE_LOCAL_REPOSITORY_CHECKPOINT",
      version: "1",
      issued_at: "2026-08-22T16:36:51Z",
      outcome: supported ? "ABSTAIN" : "ERROR",
      reason_code: supported ? "NOT_IMPLEMENTED" : "SAFE_RUNTIME_ERROR",
      evidence_refs: [],
      policy_state: "NOT_EVALUATED",
      freshness: "PINNED_REPOSITORY_SNAPSHOT",
      correction_state: "NONE",
    },
  };
};

const evidenceLabels: Record<EvidenceState, { label: string; explanation: string }> = {
  ANSWER: { label: "Supported", explanation: "A matching demonstration evidence reference is present." },
  MISSING_EVIDENCE: { label: "Missing evidence", explanation: "No claim-bearing EvidenceBundle is attached for this scope." },
  SOURCE_STALE: { label: "Source stale", explanation: "The source time is older than the active support context." },
  GENERALIZED_GEOMETRY: { label: "Generalized geometry", explanation: "The geometry is deliberately simplified and non-authoritative." },
  RESTRICTED_ACCESS: { label: "Restricted access", explanation: "The public client is not authorized to resolve the protected source." },
  DENIED_BY_POLICY: { label: "Denied by policy", explanation: "Policy prevents precise disclosure or a claim-bearing answer." },
  CORRECTED: { label: "Corrected", explanation: "The current fixture supersedes an earlier version and keeps that correction visible." },
  SUPERSEDED: { label: "Superseded", explanation: "This record is retained for lineage but is not current support." },
  ERROR: { label: "Operational error", explanation: "Resolution failed; no unsupported fallback answer is permitted." },
};

const useDebounced = <T,>(value: T, delay: number) => {
  const [debounced, setDebounced] = useState(value);
  useEffect(() => {
    const timer = window.setTimeout(() => setDebounced(value), delay);
    return () => window.clearTimeout(timer);
  }, [value, delay]);
  return debounced;
};

const copyFeature = (layer: LayerRecord, featureId: string): SelectedContext | null => {
  const result = findFeature(featureId);
  if (!result || result.layer.id !== layer.id) return null;
  return {
    kind: "registry",
    featureId,
    layerId: layer.id,
    layer,
    properties: result.feature.properties,
    geometry: {
      type: "Feature",
      properties: {},
      geometry: JSON.parse(JSON.stringify(result.feature.geometry)) as Geometry,
    },
  };
};

type BasemapFeatureCandidate = {
  id?: string | number | null;
  source?: string;
  sourceLayer?: string;
  properties?: Record<string, unknown> | null;
  geometry?: Geometry | null;
};

const stringContextProperty = (properties: Record<string, unknown>, key: string) => {
  const value = properties[key];
  return typeof value === "string" && value.trim() !== "" ? value.trim() : null;
};

const numberContextProperty = (properties: Record<string, unknown>, key: string) => {
  const value = properties[key];
  return typeof value === "number" && Number.isFinite(value) ? value : null;
};

const officialContextSummary = (source: OfficialContextId, title: string, properties: Record<string, unknown>) => {
  if (source === CIVIC_ID) return `${title}. ${stringContextProperty(properties, "congress") ?? "Congress unknown"}. ${Number(properties.congressNumber) < 119 ? CIVIC_HISTORY_LIMITATION : CIVIC_LIMITATION}`;
  if (source === "deflock-alpr") return `${title}. ${DEFLOCK_LIMITATION}`;
  if (source.startsWith("kgs-")) return source === "kgs-monitoring-wells" ? `${title}: 2026 monitoring location. Open the KGS well record for dated observations; no water-level measurement is attached to this point.` : `${title} feet · regional 2022–2024 classified estimate. Unclassified areas are blank. This is not a present measurement or a groundwater-flow calculation.`;
  if (source === "nifc-fire-reports") {
    const type = stringContextProperty(properties, "incidentType") ?? "incident";
    const discoveryAt = stringContextProperty(properties, "discoveryAt");
    const reportState = stringContextProperty(properties, "reportState") ?? "Current activity unverified";
    return `${title} is a ${type.toLowerCase()} in the NIFC WFIGS/IRWIN working incident feed${discoveryAt ? `, discovered ${new Date(discoveryAt).toLocaleString()}` : ""}. ${reportState}. This confirms a provider incident record, not current activity, perimeter, exact point location, or independent satellite corroboration.`;
  }
  if (source === "census-counties") {
    const population = numberContextProperty(properties, "populationEstimate");
    const estimate = population === null
      ? "The Census population count was unavailable, so no value is inferred."
      : `The 2020 Census population count is ${Math.round(population).toLocaleString("en-US")}.`;
    return `${title} is shown from the 2020 Census county baseline. ${estimate} Population, housing, and land/water area remain dated source context. Open the daily archive to compare the 2010 and 2020 editions.`;
  }
  if (source === "usgs-streamflow") {
    const value = stringContextProperty(properties, "displayValue") ?? "not reported";
    const observedAt = stringContextProperty(properties, "observedAt");
    const trend = stringContextProperty(properties, "trend");
    return `${title} reported ${value}${observedAt ? ` at ${new Date(observedAt).toLocaleString()}` : ""}${trend ? ` · ${trend}` : ""}. USGS values may be provisional, revised, delayed, or incomplete; discharge magnitude and change are not flood guidance or KFM evidence.`;
  }
  if (source === "noaa-nwps-gauges") {
    const observedValue = numberContextProperty(properties, "observedValue");
    const observedUnit = stringContextProperty(properties, "observedUnit") ?? "unit not supplied";
    const observedAt = stringContextProperty(properties, "observedAt");
    const forecastValue = numberContextProperty(properties, "forecastValue");
    const forecastUnit = stringContextProperty(properties, "forecastUnit") ?? observedUnit;
    const forecastAt = stringContextProperty(properties, "forecastAt");
    const floodCategory = stringContextProperty(properties, "floodCategory");
    const observed = observedValue === null ? "No current primary observation was supplied" : `Observed ${observedValue.toLocaleString("en-US")} ${observedUnit}${observedAt ? ` at ${new Date(observedAt).toLocaleString()}` : ""}`;
    const forecast = forecastValue === null ? "no official forecast value was supplied" : `official forecast ${forecastValue.toLocaleString("en-US")} ${forecastUnit}${forecastAt ? ` at ${new Date(forecastAt).toLocaleString()}` : ""}`;
    return `${title}: ${observed}; ${forecast}${floodCategory ? ` · NOAA category ${floodCategory}` : ""}. Observation, forecast, and retrieval clocks remain separate. Missing values are not an all-clear, and this display is not a warning service or KFM evidence.`;
  }
  if (source === "usgs-earthquakes") {
    const magnitude = numberContextProperty(properties, "magnitude");
    const depth = numberContextProperty(properties, "depthKilometers");
    const observedAt = stringContextProperty(properties, "observedAt");
    return `${magnitude === null ? "Magnitude not reported" : `Magnitude ${magnitude.toFixed(1)}`}${depth === null ? "" : ` · ${depth.toFixed(1)} km depth`}${observedAt ? ` · ${new Date(observedAt).toLocaleString()}` : ""}. USGS catalog values can be revised; this is external situational context, not an alert, forecast, or KFM evidence.`;
  }
  if (source === "noaa-hms-smoke") {
    const density = stringContextProperty(properties, "density") ?? "density not supplied";
    const start = stringContextProperty(properties, "start");
    const end = stringContextProperty(properties, "end");
    const satellite = stringContextProperty(properties, "satellite");
    return `${title} · ${density}${satellite ? ` · ${satellite}` : ""}${start && end ? ` · ${new Date(start).toLocaleString()}–${new Date(end).toLocaleString()}` : ""}. NOAA HMS analyst context is not surface PM2.5, plume altitude, measured transport, a fire perimeter, warning, health advisory, or all-clear.`;
  }
  if (source === "nasa-gibs-fire-points") {
    const acquiredAt = stringContextProperty(properties, "acquiredAt");
    const frp = numberContextProperty(properties, "frpMw");
    const confidence = stringContextProperty(properties, "confidence");
    const hotSpotType = stringContextProperty(properties, "hotSpotType");
    return `${title}${acquiredAt ? ` · acquired ${new Date(acquiredAt).toLocaleString()}` : ""}${frp === null ? "" : ` · ${frp.toFixed(2)} MW radiative power`}${confidence ? ` · ${confidence} confidence` : ""}${hotSpotType && hotSpotType !== "Not supplied" ? ` · ${hotSpotType}` : ""}. This marker is the thermal-anomaly pixel center, not an ignition location. It is not a verified wildfire, perimeter, incident, or safety alert. Provider attributes are external context, not KFM evidence.`;
  }
  if (source === "raspberry-shake-stations") {
    const network = stringContextProperty(properties, "network") ?? "AM";
    const station = stringContextProperty(properties, "station") ?? "station";
    const elevation = numberContextProperty(properties, "elevationMeters");
    return `${title} · ${network}.${station}${elevation === null ? "" : ` · ${elevation.toFixed(0)} m`}. FDSN station metadata is a delayed/archive context connection; open StationView for provider realtime inspection. No waveform, alert, or KFM evidence is inferred from the marker.`;
  }
  if (source === "nws-alerts") {
    const severity = stringContextProperty(properties, "severity") ?? "severity not supplied";
    const area = stringContextProperty(properties, "zoneName") ?? stringContextProperty(properties, "areaDesc");
    const expires = stringContextProperty(properties, "expires");
    return `${title} · ${severity}${area ? ` · ${area}` : ""}${expires ? ` · expires ${new Date(expires).toLocaleString()}` : ""}. Consult the National Weather Service for decisions; this map is not a warning-delivery service or KFM evidence.`;
  }
  return `${title} was returned by an official external context connection. It is useful for orientation and situational awareness, but no KFM EvidenceBundle is attached.`;
};

const officialContextTime = (source: OfficialContextId, properties: Record<string, unknown>, fallback: string) => {
  if (source === CIVIC_ID) return `${stringContextProperty(properties, "congress") ?? "Congress unknown"} · applicable ${stringContextProperty(properties, "termStart") ?? "unknown"} to ${stringContextProperty(properties, "termEndExclusive") ?? "unknown"} (end exclusive; calendar-day resolution). ${Number(properties.congressNumber) === 119 ? "Census boundary vintage: January 1, 2025." : "Reconstructed historical plan; source revision is not its effective date."} Retrieval is separate.`;
  if (source === "deflock-alpr") return `OSM database snapshot: ${stringContextProperty(properties, "upstreamUpdatedAt") ?? "unknown"}; camera observation and installation dates unknown.`;
  if (source === "census-counties") return "2020 Census geography, population and housing baseline";
  if (source === "usgs-streamflow" || source === "usgs-earthquakes") return stringContextProperty(properties, "observedAt") ?? fallback;
  if (source === "noaa-nwps-gauges") {
    const observedAt = stringContextProperty(properties, "observedAt");
    const forecastAt = stringContextProperty(properties, "forecastAt");
    return observedAt && forecastAt ? `Observed ${observedAt} · forecast ${forecastAt}` : observedAt ?? forecastAt ?? fallback;
  }
  if (source === "nws-alerts") {
    const effective = stringContextProperty(properties, "effective");
    const expires = stringContextProperty(properties, "expires");
    return effective && expires ? `${effective} through ${expires}` : effective ?? expires ?? fallback;
  }
  if (source === "noaa-hms-smoke") {
    const start = stringContextProperty(properties, "start");
    const end = stringContextProperty(properties, "end");
    return start && end ? `${start} through ${end}` : fallback;
  }
  if (source === "nasa-gibs-fire-points") return stringContextProperty(properties, "acquiredAt") ?? fallback;
  if (source === "nifc-fire-reports") return stringContextProperty(properties, "discoveryAt") ?? fallback;
  if (source === "raspberry-shake-stations") return fallback;
  return fallback;
};

const drawerTimestamp = (value: string | null | undefined) => {
  if (!value || !Number.isFinite(Date.parse(value))) return "Not available";
  return new Intl.DateTimeFormat(undefined, {
    year: "numeric", month: "short", day: "numeric", hour: "numeric", minute: "2-digit", timeZoneName: "short",
  }).format(new Date(value));
};

const buildBasemapContext = (candidate: BasemapFeatureCandidate, longitude: number, latitude: number): SelectedContext | null => {
  if (!candidate.geometry) return null;
  const properties = candidate.properties ?? {};
  const registeredSource = typeof candidate.source === "string" ? OFFICIAL_CONTEXT_BY_SOURCE_ID[candidate.source] : undefined;
  const officialSource = registeredSource?.id === CIVIC_ID ? civicSourceForRecord(properties) : registeredSource;
  const sourceLayer = typeof candidate.sourceLayer === "string" && candidate.sourceLayer.trim() !== ""
    ? candidate.sourceLayer
    : officialSource?.shortTitle ?? "vector layer";
  const titleCandidate = [properties["name:en"], properties.name, properties.name_en, properties.event, properties.headline, properties.place, properties.monitoringLocationId, properties.ref, properties.class, properties.type]
    .find((value): value is string => typeof value === "string" && value.trim() !== "");
  const title = titleCandidate?.trim() ?? `${sourceLayer} feature`;
  const featureId = `${officialSource ? "official-context" : "basemap"}:${sourceLayer}:${String(candidate.id ?? `${title}:${longitude.toFixed(4)},${latitude.toFixed(4)}`)}`.slice(0, 180);
  const contextLayer: LayerRecord = officialSource ? {
    ...BASEMAP_CONTEXT_LAYER,
    id: `official-context-${officialSource.id}`,
    title: officialSource.title,
    description: officialSource.boundary,
    domain: officialSource.domain,
    category: officialSource.id === CIVIC_ID ? "Reference boundaries & locators" : officialSource.id === "deflock-alpr" ? "Roads, rail & movement" : officialSource.id === "census-counties" ? "Reference boundaries & locators"
      : ["kgs-monitoring-wells", "kgs-water-table", "kgs-depth-to-water", "kgs-saturated-thickness", "usgs-streamflow", "noaa-nwps-gauges", "usgs-3dhp-hydrography", "usgs-wbd-watersheds", "noaa-nwm-analysis", "noaa-nwm-short-range"].includes(officialSource.id) ? "Hydrology & water"
        : officialSource.id === "usgs-3dep-hillshade" || officialSource.id === "usgs-earthquakes" ? "Geology & landforms"
          : "Weather & hazards",
    sourceType: officialSource.kind === "OPERATIONAL_WMS" ? "Raster" : "GeoJSON",
    sourceId: officialSource.sourceId,
    datasetName: officialSource.title,
    attribution: officialSource.attribution,
    validTimeExtent: officialSource.freshness,
    sourceTime: officialSource.freshness,
    releaseTime: "External operational context",
    evidenceReference: "No KFM EvidenceBundle attached",
    sensitivityNote: officialSource.boundary,
    correctionNote: officialSource.fallback,
  } : BASEMAP_CONTEXT_LAYER;
  return {
    kind: "basemap",
    featureId,
    layerId: contextLayer.id,
    layer: contextLayer,
    externalStationId: officialSource?.id === "usgs-streamflow"
      ? normalizeUsgsStationId(String(properties.stationId ?? properties.monitoringLocationId ?? ""))
      : null,
    externalFeatureId: typeof properties.featureId === "string" ? properties.featureId : officialSource && candidate.id !== undefined ? String(candidate.id) : null,
    externalAttributes: drawerArtifactAttributes(officialSource?.id ?? "basemap", properties),
    ...(officialSource?.id === CIVIC_ID ? { civicRecord: {
      sourceDay: stringContextProperty(properties, "sourceDay"),
      congressNumber: typeof properties.congressNumber === "number" ? properties.congressNumber : null,
      termStart: stringContextProperty(properties, "termStart"),
      termEndExclusive: stringContextProperty(properties, "termEndExclusive"),
    } } : {}),
    properties: {
      fid: featureId,
      title,
      summary: officialSource ? officialContextSummary(officialSource.id, title, properties) : `A real geographic feature returned by the selected vector basemap (${sourceLayer}). It is useful for orientation and map interaction, but no KFM EvidenceBundle is attached.`,
      sourceRole: "external display context",
      sourceOrganization: officialSource?.organization ?? "OpenFreeMap / OpenMapTiles / OpenStreetMap",
      citation: "No KFM EvidenceBundle attached",
      spatialScope: "Provider-rendered map feature inside the Kansas context extent",
      temporalScope: officialSource ? officialContextTime(officialSource.id, properties, officialSource.freshness) : "Provider-defined; not resolved by KFM",
      lastUpdate: officialSource ? stringContextProperty(properties, "retrievedAt") ?? officialSource.freshness : "Provider-defined",
      freshnessState: "EXTERNAL_PROVIDER",
      evidenceState: "MISSING_EVIDENCE",
      reviewState: "NOT_KFM_REVIEWED",
      releaseState: "GENERALIZED",
      rights: `Use remains subject to ${officialSource?.organization ?? "the external provider"}'s attribution and terms.`,
      generalizationNote: officialSource?.boundary ?? "Geometry is rendered by an external basemap and is not a KFM released artifact.",
      uncertainty: officialSource?.fallback ?? "The Site does not resolve provider lineage, update time, completeness, or claim support for this feature.",
      correctionState: "EXTERNAL_PROVIDER_STATE_UNKNOWN",
      relatedLayers: "",
      year: officialSource?.id === CIVIC_ID ? Number(String(properties.sourceDay ?? properties.termStart ?? "2026").slice(0, 4)) : 2026,
      focusLng: longitude,
      focusLat: latitude,
      displayLabel: title,
    },
    geometry: {
      type: "Feature",
      properties: { displaySourceId: officialSource?.id ?? "basemap" },
      geometry: JSON.parse(JSON.stringify(candidate.geometry)) as Geometry,
    },
  };
};

const parseNumber = (value: string | null, fallback: number) => {
  if (value === null || value.trim() === "") return fallback;
  const parsed = Number(value);
  return Number.isFinite(parsed) ? parsed : fallback;
};

const clamp = (value: number, minimum: number, maximum: number) => Math.min(maximum, Math.max(minimum, value));

const formatCoordinate = (value: number, positive: string, negative: string) =>
  `${Math.abs(value).toFixed(4)}° ${value >= 0 ? positive : negative}`;

const formatTimelineStep = (value: number) => {
  if (value <= -1_000_000_000) return `${Number((Math.abs(value) / 1_000_000_000).toPrecision(3))} Ga BP`;
  if (value <= -1_000_000) return `${Number((Math.abs(value) / 1_000_000).toPrecision(3))} Ma BP`;
  if (value === -11_700) return "11.7 ka BP";
  if (value < 0) return `${Math.abs(value).toLocaleString("en-US")} BCE`;
  if (value < 1000) return `${value} CE`;
  if (value <= 9999) return String(value);
  return value.toLocaleString("en-US");
};

const formatNoaaRadarLocalTime = (value: string) => new Intl.DateTimeFormat(undefined, {
  month: "short",
  day: "numeric",
  hour: "numeric",
  minute: "2-digit",
  timeZoneName: "short",
}).format(new Date(value));

const formatNoaaRadarUtcTime = (value: string) => `${value.slice(0, 10)} · ${value.slice(11, 16)}Z`;

const timelineEraLabel = (value: number, buildYearCurrent = true) => {
  if (value <= -4_000_000_000) return "Hadean eon context";
  if (value <= -2_500_000_000) return "Archean eon context";
  if (value < -541_000_000) return "Proterozoic eon context";
  if (value < -252_000_000) return "Paleozoic era context";
  if (value < -66_000_000) return "Mesozoic era context";
  if (value < -2_580_000) return "Cenozoic era context";
  if (value < -11_700) return "Quaternary context";
  if (value < -8_000) return "Holocene context";
  if (value < 1) return "Archaeological time capacity";
  if (value < 1541) return "Early human record capacity";
  if (value < 1854) return "Early historical capacity";
  if (value < 2000) return "Historical record";
  if (value === OFFICIAL_CONTEXT_PRESENT_FRAME) return buildYearCurrent ? "Present operational window · source-specific clocks" : "Build-year mismatch · current sources held";
  return "Modern record";
};

const TIMELINE_MAJOR_STEPS = new Set<number>([-4_540_000_000, 1800, 1850, 1900, 1950, 2000, OFFICIAL_CONTEXT_PRESENT_FRAME]);
const TIMELINE_JUMPS = Object.freeze([
  Object.freeze({ label: "Earth", year: -4_540_000_000 }),
  Object.freeze({ label: "Paleozoic", year: -541_000_000 }),
  Object.freeze({ label: "Quaternary", year: -2_580_000 }),
  Object.freeze({ label: "Human time", year: -8_000 }),
  Object.freeze({ label: "Historical", year: 1541 }),
  Object.freeze({ label: "Modern", year: 2022 }),
]);

const motionDuration = (duration: number) => window.matchMedia("(prefers-reduced-motion: reduce)").matches ? 0 : duration;

const isFeatureInsideBounds = (properties: Pick<FeatureProperties, "focusLng" | "focusLat">, bounds: MapBoundsState) => (
  properties.focusLng >= bounds.west
  && properties.focusLng <= bounds.east
  && properties.focusLat >= bounds.south
  && properties.focusLat <= bounds.north
);

const cameraViewsEquivalent = (left: ViewState, right: ViewState) => (
  Math.abs(left.center[0] - right.center[0]) < 0.00001
  && Math.abs(left.center[1] - right.center[1]) < 0.00001
  && Math.abs(left.zoom - right.zoom) < 0.01
  && Math.abs(left.bearing - right.bearing) < 0.1
  && Math.abs(left.pitch - right.pitch) < 0.1
);

const trustStateForLayer = (layer: LayerRecord): TrustState => {
  if (layer.releaseState === "RESTRICTED") return "Restricted";
  if (layer.releaseState === "GENERALIZED") return "Generalized";
  if (layer.freshnessState === "STALE") return "Stale";
  if (layer.releaseState === "DEMONSTRATION") {
    return `${layer.datasetName} ${layer.attribution}`.toLowerCase().includes("synthetic") ? "Synthetic" : "Site-local demo";
  }
  return "Held";
};

const measurementLabelFor = (mode: Exclude<MeasureMode, null>, coordinates: [number, number][], unit: MeasureUnit) => {
  if (mode === "point") {
    if (coordinates.length === 0) return "Click the map to place a point";
    const [longitude, latitude] = coordinates[0];
    return `${latitude.toFixed(4)}, ${longitude.toFixed(4)} · browser-local point`;
  }
  if (mode === "distance") {
    if (coordinates.length < 2) return "Add another point";
    const miles = distanceMiles(coordinates);
    return unit === "metric" ? `${(miles * 1.609344).toFixed(1)} km approximate` : `${miles.toFixed(1)} mi approximate`;
  }
  if (coordinates.length < 3) return `Add ${3 - coordinates.length} more point${coordinates.length === 2 ? "" : "s"}`;
  return formatMeasuredArea(areaSquareMiles(coordinates), unit === "metric");
};

const LocalWelcomeRecorder = __KFM_WELCOME_RECORDER__ && import.meta.env.DEV
  ? lazy(() => import("./living-welcome/dev-recorder")) : null;

export default function Home() {
  const mapContainerRef = useRef<HTMLDivElement>(null);
  const windArrowCanvasRef = useRef<HTMLCanvasElement>(null);
  const riverPathFocusRef = useRef<string | null>(null);
  const waterMotionCanvasRef = useRef<HTMLCanvasElement>(null);
  const daylightDayInitial = currentKansasCalendarDay();
  const [daylightDay, setDaylightDay] = useState(daylightDayInitial);
  const [daylightThroughDay, setDaylightThroughDay] = useState(daylightDayInitial);
  const [daylightInstant, setDaylightInstant] = useState<number>(() => kansasLocalDayInterval(daylightDayInitial).startMs);
  const [daylightEnabled, setDaylightEnabled] = useState(false);
  const [daylightPlaying, setDaylightPlaying] = useState(false);
  const daylightDayRef = useRef(daylightDay);
  const daylightThroughDayRef = useRef(daylightThroughDay);
  const daylightInstantRef = useRef(daylightInstant);
  const daylightEnabledRef = useRef(false);
  const daylightPlayingRef = useRef(false);
  const mapRef = useRef<MapLibreMap | null>(null);
  const mapInformationHostRef = useRef<HTMLDivElement>(null);
  const localCapturePixelRatioRef = useRef<number | null>(null);
  const localCaptureWindFrameRef = useRef<WindArrowFrame | null>(null);
  const earthEngineContext = useEarthEngineContext();
  const [earthEngineDisplay, setEarthEngineDisplay] = useState<EarthEngineDisplayState>({ visible: {}, opacity: {}, years: {} });
  const styleGenerationReadyRef = useRef(false);
  // Set on each style.load and cleared by setStyle: overlays attach only after it.
  const styleDocumentLoadedRef = useRef(false);
  const mapMutationErrorRef = useRef<string | null>(null);
  const scaleControlRef = useRef<ScaleControl | null>(null);
  const hoveredRef = useRef<{ source: string; id: string | number } | null>(null);
  const hoverCandidateIdRef = useRef<string | null>(null);
  const hoverDrawerTimerRef = useRef<number | null>(null);
  const visibilityRef = useRef(defaultVisibility);
  const opacityRef = useRef(defaultOpacity);
  const officialVisibilityRef = useRef(defaultOfficialVisibility);
  const buildYearCurrentRef = useRef(true);
  const officialOpacityRef = useRef(defaultOfficialOpacity);
  const officialPayloadsRef = useRef<Partial<Record<OfficialContextFeedId, OfficialContextPayload>>>({});
  const explorerRestoredRef = useRef(false);
  const officialArchiveDaysRef = useRef<Partial<Record<OfficialContextFeedId, string>>>({});
  const officialArchivePayloadsRef = useRef<Partial<Record<OfficialContextFeedId, OfficialContextPayload>>>({});
  const smokeTransitionsRef = useRef(new HmsFrameTransitions());
  const [smokePlaybackSignal, setSmokePlaybackSignal] = useState(() => smokeTransitionsRef.current.signal);
  const cancelSmokePlayback = useCallback(() => {
    // Synchronous invalidation also reaches the child's independent cache read.
    setSmokePlaybackSignal(smokeTransitionsRef.current.cancel());
    const map = mapRef.current;
    if (map && styleGenerationReadyRef.current) {
      resetHmsSmokeFade(map);
      setHmsSmokeFade(map, 1, officialOpacityRef.current["noaa-hms-smoke"]);
    }
  }, []);
  const layerJsonReadsRef = useRef<LayerJsonReads | null>(null);
  layerJsonReadsRef.current ??= new LayerJsonReads();
  const officialRequestsRef = useRef(new Map<OfficialContextFeedId, AbortController>());
  const officialRasterFailuresRef = useRef(new Set<OfficialContextId>());
  const terrainRasterViewRef = useRef(new TerrainRasterViewTracker());
  const failedTerrainSourceRef = useRef<unknown>(null);
  const noaaRadarRequestRef = useRef<AbortController | null>(null);
  const noaaRadarLastRequestAtRef = useRef(0);
  const noaaRadarReadyRef = useRef(false);
  const noaaRadarManifestRef = useRef<NoaaRadarManifest | null>(null);
  const noaaRadarFrameTimeRef = useRef<string | null>(null);
  const noaaRadarPendingFrameTimeRef = useRef<string | null>(null);
  const noaaRadarRequestedTimeRef = useRef<string | null>(null);
  const noaaRadarFollowLatestRef = useRef(true);
  const lightningAutoStartRef = useRef(true);
  const noaaRadarFrameLoadCleanupRef = useRef<(() => void) | null>(null);
  const noaaRadarFrameFailureRef = useRef<((message: string) => void) | null>(null);
  const noaaSatelliteRequestRef = useRef<AbortController | null>(null);
  const noaaSatelliteManifestRef = useRef<NoaaSatelliteManifest | null>(null);
  const noaaSatelliteFrameRef = useRef<NoaaSatelliteFrame | null>(null);
  const noaaSatelliteFollowLatestRef = useRef(true);
  const streamflowRequestRef = useRef<AbortController | null>(null);
  const streamflowRequestPathRef = useRef<string | null>(null);
  const streamflowRequestStationRef = useRef<string | null>(null);
  const streamflowRequestGenerationRef = useRef(0);
  const streamflowBundleRef = useRef<StreamflowBundle | null>(null);
  const streamflowArchiveDayRef = useRef<string | null>(null);
  const streamflowRequestedTimeRef = useRef<string | null>(null);
  const noaaHydrologyRequestRef = useRef<AbortController | null>(null);
  const orderRef = useRef(defaultOrder);
  const yearRef = useRef<number>(OFFICIAL_CONTEXT_PRESENT_FRAME);
  const temporalQueryRef = useRef<TemporalSweepQuery>({
    mode: "snapshot",
    frame: OFFICIAL_CONTEXT_PRESENT_FRAME,
    rangeStart: TIME_STEPS[0],
    rangeEnd: TIME_STEPS.at(-1)!,
    windowStart: OFFICIAL_CONTEXT_PRESENT_FRAME,
  });
  const mapEvidenceFilterRef = useRef<RegistryEvidenceFilter>("ALL");
  const basemapRef = useRef<BasemapKey>("standard");
  const projectionRef = useRef<"mercator" | "globe">("mercator");
  const scenePresetRef = useRef<ScenePresetId>("overview-2d");
  const terrainProviderRef = useRef<TerrainProvider>("mapzen");
  // Close 3D views over Kansas move from the display DEM (capped at zoom 11) to the
  // USGS 3DEP mosaic. `auto` marks that switch, `failed` stops it after 3DEP fails
  // once, and `byHand` leaves a visitor's own choice of DEM alone.
  const terrainDetailRef = useRef({ auto: false, failed: false, byHand: false });
  const terrainDetailFallbackRef = useRef<(() => void) | null>(null);
  const attachedTerrainProviderRef = useRef<TerrainProvider | null>(null);
  const setTerrainPresentation = (map: MapLibreMap, enabled: boolean, scale: number) => {
    const provider = terrainProviderRef.current;
    const source = terrainSourceFor(provider);
    const state = applyTerrainPresentation(map, enabled, scale, source);
    const attachedMatches = enabled && terrainPresentationSourceMatches(map, source);
    if (enabled && state !== "ERROR") {
      applyTerrainReliefStyle(map, basemapRef.current === "topo" ? "topographic" : "general", atmospherePresetRef.current, lightAzimuthRef.current);
    }
    const topoDemReady = attachedMatches && state !== "ERROR" && basemapRef.current === "topo"
      && Boolean(map.getSource(TERRAIN_SOURCE_ID) && map.isSourceLoaded(TERRAIN_SOURCE_ID));
    applyTopographicRasterDepth(map, topoDemReady);
    attachedTerrainProviderRef.current = state === "LOADING" && attachedMatches ? provider : null;
    return state;
  };
  const setTerrainHeightOverlay = (map: MapLibreMap, enabled: boolean) => applyTerrainHeightOverlay(map, enabled, terrainSourceFor(terrainProviderRef.current));
  const verticalExaggerationRef = useRef(1);
  const topographicOverlayRef = useRef(false);
  const atmospherePresetRef = useRef<AtmospherePreset>("night");
  const lightAzimuthRef = useRef(210);
  const fieldOfViewRef = useRef(36);
  const structures3DRef = useRef(false);
  const gestureModeRef = useRef<"cooperative" | "direct">("cooperative");
  const sceneOrbitTimerRef = useRef<number | null>(null);
  const sceneOrbitCancelRef = useRef<(() => void) | null>(null);
  const sceneOrbitContextRef = useRef("");
  const terrainDrawingRef = useRef<ReturnType<typeof createTerrainDrawing> | null>(null);
  const terrainDrawingConfigRef = useRef<TerrainDrawingConfig>({ mode: "off", surface: "off", surfaceOpacity: 0.55, probeEnabled: true, enabled: false, provider: "mapzen", efficient: false, detail: false, light: "night", azimuth: 210 });
  const sceneEffectsRef = useRef<SceneEffectSettings>(DEFAULT_SCENE_EFFECTS);
  const flyoverCancelRef = useRef<(() => void) | null>(null);
  const renderEfficientRef = useRef(false);
  const placeTourTimerRef = useRef<number | null>(null);
  const selectedRef = useRef<SelectedContext | null>(null);
  const measureModeRef = useRef<MeasureMode>(null);
  const measurementGeometryModeRef = useRef<MeasureMode>(null);
  const measureUnitRef = useRef<MeasureUnit>("imperial");
  const measureCoordinatesRef = useRef<[number, number][]>([]);
  const analysisAreaRef = useRef<MapBoundsState | null>(null);
  const boxDragModeRef = useRef<BoxDragMode>("zoom");
  const importPreviewRef = useRef<LocalImportPreview | null>(null);
  const importPreviewVisibleRef = useRef(false);
  const roadStudyLayersRef = useRef<readonly RoadStudyLayer[]>([]);
  const roadStudyInputRef = useRef<HTMLInputElement>(null);
  const roadStudyImportGenerationRef = useRef(0);
  const importInspectionGenerationRef = useRef(0);
  const importInputRef = useRef<HTMLInputElement>(null);
  const cameraHistoryRef = useRef<ViewState[]>([KANSAS_VIEW]);
  const cameraHistoryIndexRef = useRef(0);
  const replayingCameraHistoryRef = useRef(false);
  const returnFocusRef = useRef<HTMLElement | null>(null);
  const leftPanelRef = useRef<HTMLElement>(null);
  const leftPanelReturnRef = useRef<HTMLElement | null>(null);
  const sourceSearchFocusPendingRef = useRef(false);
  const rightPanelRef = useRef<HTMLElement>(null);
  const timelineRef = useRef<HTMLElement>(null);
  const repositoryButtonRef = useRef<HTMLButtonElement>(null);
  const repositoryPanelRef = useRef<HTMLElement>(null);
  const workspaceDetailsRef = useRef<HTMLDetailsElement>(null);
  const globalSearchInputRef = useRef<HTMLTextAreaElement>(null);
  const assistantEvidenceReturnRef = useRef<HTMLElement | null>(null);
  const [assistantDraftRequest, setAssistantDraftRequest] = useState<{id:number;value:string;intent:"find"|"explore"|"evidence"}>();
  const mapUtilityPanelRef = useRef<HTMLElement>(null);
  const mapUtilityReturnRef = useRef<HTMLElement | null>(null);
  const sourceStatusPanelRef = useRef<HTMLElement>(null);
  const sourceStatusReturnRef = useRef<HTMLElement | null>(null);
  const qwenPanelRef = useRef<HTMLElement>(null);
  const [chatReadingView, setChatReadingView] = useState(false);
  const qwenReturnRef = useRef<HTMLElement | null>(null);
  const drawerTabRefs = useRef<Array<HTMLButtonElement | null>>([]);
  const pendingViewRef = useRef<ViewState | null>(null);
  const lastKnownGoodViewRef = useRef<ViewState>(KANSAS_VIEW);
  const locationDerivedViewRef = useRef(false);
  const compactRef = useRef(false);
  const openSelectionRef = useRef<(context: SelectedContext, returnElement?: HTMLElement | null) => void>(() => undefined);

  const [visibility, setVisibility] = useState<Record<string, boolean>>(defaultVisibility);
  const [opacity, setOpacity] = useState<Record<string, number>>(defaultOpacity);
  const [officialVisibility, setOfficialVisibility] = useState<Record<OfficialContextId, boolean>>(defaultOfficialVisibility);
  const [buildYearCurrent, setBuildYearCurrent] = useState(true);
  const [officialOpacity, setOfficialOpacity] = useState<Record<OfficialContextId, number>>(defaultOfficialOpacity);
  const [officialReadPhases, setOfficialReadPhases] = useState<Partial<Record<OfficialContextId, "queued" | "fetching">>>({});
  const [officialStates, setOfficialStates] = useState<Record<OfficialContextId, OfficialContextState>>(defaultOfficialStates);
  const [officialPayloads, setOfficialPayloads] = useState<Partial<Record<OfficialContextFeedId, OfficialContextPayload>>>({});
  const [officialArchiveDays, setOfficialArchiveDays] = useState<Partial<Record<OfficialContextFeedId, string>>>({});
  const [officialArchiveDraftDays, setOfficialArchiveDraftDays] = useState<Partial<Record<OfficialContextFeedId, string>>>(() => ({ "noaa-hms-smoke": currentUtcDay() }));
  const [earthquakeArchiveFrameIndex, setEarthquakeArchiveFrameIndex] = useState(-1);
  const [smokeArchiveFrameIndex, setSmokeArchiveFrameIndex] = useState(-1);
  const [officialErrors, setOfficialErrors] = useState<Partial<Record<OfficialContextId, string>>>({});
  const [noaaRadarManifestState, setNoaaRadarManifestState] = useState<NoaaRadarManifestState>("idle");
  const [noaaRadarManifest, setNoaaRadarManifest] = useState<NoaaRadarManifest | null>(null);
  const [noaaRadarManifestError, setNoaaRadarManifestError] = useState("");
  const [noaaRadarFrameTime, setNoaaRadarFrameTime] = useState<string | null>(null);
  const [noaaRadarPendingFrameTime, setNoaaRadarPendingFrameTime] = useState<string | null>(null);
  const [noaaRadarLoopSpan, setNoaaRadarLoopSpan] = useState<NoaaRadarLoopSpanMinutes>(60);
  const [noaaRadarPlaybackSpeed, setNoaaRadarPlaybackSpeed] = useState<NoaaRadarPlaybackSpeed>(1);
  const [noaaRadarPlaying, setNoaaRadarPlaying] = useState(false);
  const [noaaRadarSmooth, setNoaaRadarSmooth] = useState(false);
  const [fireVisualMode, setFireVisualMode] = useState<"exact" | "soft">("exact");
  const [noaaRadarFollowLatest, setNoaaRadarFollowLatest] = useState(true);
  const [noaaRadarFrameLoadState, setNoaaRadarFrameLoadState] = useState<NoaaRadarFrameLoadState>("idle");
  const [noaaRadarClock, setNoaaRadarClock] = useState(() => Date.now());
  const [lightningManifest, setLightningManifest] = useState<LightningManifest | null>(null);
  const [lightningManifestState, setLightningManifestState] = useState<"idle" | "loading" | "ready" | "error">("idle");
  const [lightningFrame, setLightningFrame] = useState<string | null>(null);
  const [lightningPlaying, setLightningPlaying] = useState(false);
  const [lightningPreview, setLightningPreview] = useState<"idle" | "loading" | "signal" | "none" | "error">("idle");
  const [lightningViewRevision, setLightningViewRevision] = useState(0);
  const [lightningReloadToken, setLightningReloadToken] = useState(0);
  const [glmFlashesEnabled, setGlmFlashesEnabled] = useState(false);
  const [noaaSatelliteManifest, setNoaaSatelliteManifest] = useState<NoaaSatelliteManifest | null>(null);
  const [noaaSatelliteFrame, setNoaaSatelliteSelectedFrame] = useState<NoaaSatelliteFrame | null>(null);
  const [radarArchiveDraftDay, setRadarArchiveDraftDay] = useState(currentUtcDay);
  const [streamflowBundle, setStreamflowBundle] = useState<StreamflowBundle | null>(null);
  const [stageDrawerLoad, setStageDrawerLoad] = useState<StageDrawerLoad | null>(null);
  const [streamflowState, setStreamflowState] = useState<HydrologyObservatoryState>("idle");
  const [streamflowError, setStreamflowError] = useState<string | null>(null);
  const [streamflowFrameIndex, setStreamflowFrameIndex] = useState(-1);
  const [streamflowPlaying, setStreamflowPlaying] = useState(false);
  const [riverMapDisplay, setRiverMapDisplay] = useState<RiverMapDisplay>("rivers");
  const [streamflowPlaybackSpeed, setStreamflowPlaybackSpeed] = useState<HydrologyPlaybackSpeed>(1);
  const [streamflowRange, setStreamflowRange] = useState<HydrologyRange>("24h");
  const [streamflowSelectedStationId, setStreamflowSelectedStationId] = useState<string | null>(null);
  const [loadedDownstreamAnalysis, setDownstreamAnalysis] = useState<WaterPathAnalysis | null>(null);
  const [loadedDownstreamPaths, setDownstreamPaths] = useState<readonly DownstreamPath[]>([]);
  const [downstreamStationId, setDownstreamStationId] = useState<string | null>(null);
  const directionGuideCacheRef = useRef(new Map<string, { guide: DownstreamGuide; expiresAt: number }>());
  const downstreamPaths = useMemo(() => downstreamStationId === streamflowSelectedStationId ? loadedDownstreamPaths : [], [downstreamStationId, streamflowSelectedStationId, loadedDownstreamPaths]);
  const downstreamAnalysis = downstreamStationId === streamflowSelectedStationId ? loadedDownstreamAnalysis : null;
  const [downstreamState, setDownstreamState] = useState<"idle" | "loading" | "ready" | "empty" | "error">("idle");
  const [streamflowArchiveDay, setStreamflowArchiveDay] = useState<string | null>(null);
  const [streamflowArchiveDraftDay, setStreamflowArchiveDraftDay] = useState(currentUtcDay);
  const [streamflowCoverage, setStreamflowCoverage] = useState<{ station: string; continuous: { start: string; end: string } | null; daily: { start: string; end: string } | null; partial: boolean } | null>(null);
  const [streamflowCoverageMessage, setStreamflowCoverageMessage] = useState("Choose a station to check its provider-declared record span.");
  const [liveInstrument, setLiveInstrument] = useState<"river" | "radar" | "lightning">("river");
  const [layerOrder, setLayerOrder] = useState<string[]>(defaultOrder);
  const [basemap, setBasemap] = useState<BasemapKey>("standard");
  const [view, setView] = useState<ViewState>(KANSAS_VIEW);
  const regionalViewRef = useRef<ViewState>(KANSAS_VIEW);
  const [scenePreset, setScenePreset] = useState<ScenePresetId>("overview-2d");
  const [terrainProvider, setTerrainProvider] = useState<TerrainProvider>("mapzen");
  const [terrainState, setTerrainState] = useState<TerrainPresentationState>("OFF");
  const [topographicOverlay, setTopographicOverlay] = useState(false);
  const [terrainElevationReading, setTerrainElevationReading] = useState<TerrainElevationReading | null>(null);
  const [terrainElevationUnavailable, setTerrainElevationUnavailable] = useState<{ longitude: number; latitude: number } | null>(null);
  const [lockedTerrainElevation, setLockedTerrainElevation] = useState<TerrainElevationReading | null>(null);
  const [verticalExaggeration, setVerticalExaggeration] = useState(1);
  const [atmospherePreset, setAtmospherePreset] = useState<AtmospherePreset>("night");
  const [lightAzimuth, setLightAzimuth] = useState(210);
  const [fieldOfView, setFieldOfView] = useState(36);
  const [structures3DEnabled, setStructures3DEnabled] = useState(false);
  const [structures3DState, setStructures3DState] = useState<Structures3DState>("OFF");
  const [gestureMode, setGestureMode] = useState<"cooperative" | "direct">("cooperative");
  const [sceneOrbiting, setSceneOrbiting] = useState(false);
  const [terrainDrawingMode, setTerrainDrawingMode] = useState<TerrainDrawingMode>("off");
  const [terrainDrawingDetail, setTerrainDrawingDetail] = useState(false);
  const [terrainSurfaceMode, setTerrainSurfaceMode] = useState<TerrainSurfaceMode>("off");
  const [terrainSurfaceOpacity, setTerrainSurfaceOpacity] = useState(0.55);
  const [terrainSurfaceProbe, setTerrainSurfaceProbe] = useState<TerrainSurfaceProbe | null>(null);
  const [scenePanelOpen, setScenePanelOpen] = useState(false);
  const [terrainDrawingStatus, setTerrainDrawingStatus] = useState<TerrainDrawingStatus>(TERRAIN_DRAWING_INITIAL_STATUS);
  const [sceneEffects, setSceneEffects] = useState<SceneEffectSettings>(DEFAULT_SCENE_EFFECTS);
  const [flyoverStopIndex, setFlyoverStopIndex] = useState<number | null>(null);
  const [sunClock, setSunClock] = useState(() => Date.now());
  // A time-of-day study for the computed sun; null follows the clock.
  const [sunStudyAt, setSunStudyAt] = useState<number | null>(null);
  const sunAt = sunStudyAt ?? sunClock;
  const [sunPlaying, setSunPlaying] = useState(false);
  const [dynamicEffects, setDynamicEffects] = useState(true);
  const [windArrowState, setWindArrowState] = useState<"OFF" | "LOADING" | "READY" | "ERROR">("OFF");
  const [windArrowFrame, setWindArrowFrame] = useState<WindArrowFrame | null>(null);
  const [windArrowDirect, setWindArrowDirect] = useState(false);
  const [windArrowHover, setWindArrowHover] = useState<WindArrowHover | null>(null);
  const [windArrowSampleIndex, setWindArrowSampleIndex] = useState(0);
  const [windArrowReloadToken, setWindArrowReloadToken] = useState(0);
  const windLayerSelected = officialVisibility["nws-forecast-wind"];
  const [reducedMotion, setReducedMotion] = useState(false);
  const [mapViewportBounds, setMapViewportBounds] = useState<MapBoundsState>(SUPPORTED_CONTEXT_BOUNDS);
  const [analysisArea, setAnalysisArea] = useState<MapBoundsState | null>(null);
  const [boxDragMode, setBoxDragMode] = useState<BoxDragMode>("zoom");
  const [importPreview, setImportPreview] = useState<LocalImportPreview | null>(null);
  const [importPreviewVisible, setImportPreviewVisible] = useState(false);
  const [importError, setImportError] = useState("");
  const [importBusy, setImportBusy] = useState(false);
  const [roadStudyLayers, setRoadStudyLayers] = useState<readonly RoadStudyLayer[]>([]);
  const [roadStudyEditionId, setRoadStudyEditionId] = useState(ROAD_MAP_EDITIONS[0].id);
  const [roadStudyError, setRoadStudyError] = useState("");
  const [roadStudyBusy, setRoadStudyBusy] = useState(false);
  const [cameraHistoryIndex, setCameraHistoryIndex] = useState(0);
  const [cameraHistoryLength, setCameraHistoryLength] = useState(1);
  const [runtime, setRuntime] = useState<RuntimeState>({ kind: "loading", message: "Starting the MapLibre renderer…" });
  const [maplibreProbe, setMaplibreProbe] = useState<MapLibreRuntimeProbe>({
    version: null,
    workerConfigured: false,
    runtimeAssetsReady: false,
    webgl2: null,
    mapConstructed: false,
    canvasReady: false,
    styleLoaded: false,
    idle: false,
    tilesLoaded: false,
    controlsReady: false,
    interactionsReady: false,
    sourcesReady: 0,
    projection: "mercator",
    error: null,
    failedChecks: [],
  });
  const runMapMutation = useCallback((operation: string, mutation: () => void): boolean => {
    try {
      mutation();
      return true;
    } catch {
      const code = `MAP_${operation.toUpperCase().replace(/[^A-Z0-9]+/g, "_")}_FAILED`;
      mapMutationErrorRef.current = code;
      setMaplibreProbe((current) => ({ ...current, error: mapMutationErrorRef.current }));
      setRuntime({ kind: "degraded", message: `${operation} failed (${code}); the Explorer shell and data controls remain available.` });
      return false;
    }
  }, []);
  const [frameCheckEnabled, setFrameCheckEnabled] = useState(false);
  useEffect(() => { setFrameCheckEnabled(new URLSearchParams(window.location.search).get("frameCheck") === "1"); }, []);
  const [styleReady, setStyleReady] = useState(false);
  const [renderQuality, setRenderQuality] = useState<RenderQuality>("auto");
  const [renderEfficient, setRenderEfficient] = useState(false);
  useEffect(() => { setRenderQuality(readRenderQuality()); }, []);
  useEffect(() => {
    const map = mapRef.current; if (!map) return;
    let disposed = false;
    const apply = () => {
      const budget = browserRenderBudget(renderQuality);
      // setPixelRatio always calls resize, even when its value is unchanged.
      const pixelRatio = __KFM_WELCOME_RECORDER__ && localCapturePixelRatioRef.current !== null ? localCapturePixelRatioRef.current : budget.pixelRatio;
      if (map.getPixelRatio() !== pixelRatio)
        runMapMutation("Rendering-quality update", () => map.setPixelRatio(pixelRatio));
      void loadMapLibre().then(gl => { if (!disposed) runMapMutation("Image-request budget update", () => gl.setMaxParallelImageRequests(budget.imageRequests)); }).catch((error: unknown) => {
        if (!disposed) runMapMutation("MapLibre runtime update", () => { throw error; });
      });
    };
    apply(); window.addEventListener("resize", apply);
    return () => { disposed = true; window.removeEventListener("resize", apply); };
  }, [renderQuality, runMapMutation, styleReady]);
  useEffect(() => {
    const efficient = browserRenderBudget(renderQuality).efficient;
    renderEfficientRef.current = efficient;
    setRenderEfficient(efficient);
  }, [renderQuality]);
  const chooseRenderQuality = (value: RenderQuality) => { setRenderQuality(value); try { localStorage.setItem(QUALITY_STORAGE_KEY, value); } catch { /* The current session still uses the selected quality. */ } };
  const [locationCameraRedacted, setLocationCameraRedacted] = useState(false);
  const [selected, setSelected] = useState<SelectedContext | null>(null);
  const [hoverSummary, setHoverSummary] = useState<HoverSummary | null>(null);
  const [hoverActive, setHoverActive] = useState(false);
  const [primaryWorkspace, setPrimaryWorkspace] = useState<PrimaryWorkspace>("map");
  const [workspaceSnapshot, setWorkspaceSnapshot] = useState<MapSnapshot | null>(null);
  const [fireReportContext, setFireReportContext] = useState<FireReportContext | null>(null);
  const [researchReportContext, setResearchReportContext] = useState<ResearchContext | null>(null);
  const [undergroundOpen, setUndergroundOpen] = useState(false);
  const [undergroundFocusRequest, setUndergroundFocusRequest] = useState(0);
  const undergroundOpenRef = useRef(false);
  undergroundOpenRef.current = undergroundOpen;
  const [subsurfaceContext, setSubsurfaceContext] = useState<SubsurfaceContext | null>(null);
  const [subsurfaceReportContext, setSubsurfaceReportContext] = useState<SubsurfaceContext | null>(null);
  const [subsurfaceInspection, setSubsurfaceInspection] = useState<SubsurfaceInspection | null>(null);
  const [subsurfacePrivate, setSubsurfacePrivate] = useState(false);
  const [undergroundRestoreKey, setUndergroundRestoreKey] = useState(0);
  useEffect(() => { if (undergroundOpen && locationCameraRedacted) setSubsurfacePrivate(true); }, [undergroundOpen, locationCameraRedacted]);
  const [researchCounty, setResearchCounty] = useState<NonNullable<ResearchContext["county"]> | null>(null);
  const [researchAnchor, setResearchAnchor] = useState<ResearchRecord | null>(null);
  const [researchLocationRedacted, setResearchLocationRedacted] = useState(false);
  const [researchOpen, setResearchOpen] = useState(false);
  const researchResultFocusRef = useRef<string | null>(null);
  const [researchSnapshotPoints, setResearchSnapshotPoints] = useState<FeatureCollection | null>(null);
  const [researchMissingSources, setResearchMissingSources] = useState<ResearchCoverage[]>([]);
  const [leftOpen, setLeftOpen] = useState(false);
  const [sourceStatusOpen, setSourceStatusOpen] = useState(false);
  const [sourceStatusScope, setSourceStatusScope] = useState<"selected" | "all">("selected");
  const [instrumentOpen, setInstrumentOpen] = useState(false);
  // On phones the radar dock opens on its reading and transport; loop, speed, opacity and the legend fold behind Settings.
  const [radarDetailsOpen, setRadarDetailsOpen] = useState(false);
  const [leftPanelMode, setLeftPanelMode] = useState<LeftPanelMode>("layers");
  const [layerCatalogView, setLayerCatalogView] = useState<LayerBrowseView>("official");
  const [starterPanelOpen, setStarterPanelOpen] = useState(true);
  const [layerPreferencesReady, setLayerPreferencesReady] = useState(false);
  const [officialSourceQuery, setOfficialSourceQuery] = useState("");
  const [officialCatalogFilter, setOfficialCatalogFilter] = useState<CatalogFilter>("all");
  const [officialWorkspace, setOfficialWorkspace] = useState<LayerWorkspace>("all");
  // The category whose map look was opened, and whether its dock was hidden.
  const [categoryDockTopic, setCategoryDockTopic] = useState<TopicId | null>(null);
  // County population prisms: on with the People map, toggled from its dock.
  const [populationPrisms, setPopulationPrismsShown] = useState(false);
  // The Kansas earthquake record since 1973 (Landform relief): shown or not, the
  // served record once read, whether the read failed, one year or all, and the
  // event a visitor selected. While it is shown the 30-day catalog is hidden.
  const [quakeRecordOn, setQuakeRecordOn] = useState(false);
  const [quakeRecord, setQuakeRecord] = useState<EarthquakeRecord | null>(null);
  const [quakeRecordFailed, setQuakeRecordFailed] = useState(false);
  const [quakeRecordYear, setQuakeRecordYear] = useState<number | null>(null);
  const [quakeRecordSelected, setQuakeRecordSelected] = useState<EarthquakeRecordEvent | null>(null);
  const quakeRecordEventsRef = useRef<ReadonlyMap<string, EarthquakeRecordEvent>>(new Map());
  const quakeLiveWasOnRef = useRef(false);
  // The SPC convective outlook (Storm desk): the day shown (null when off), the
  // product chosen (categorical, or a hazard's probabilities), the outlooks read
  // so far by "day-product", and the one whose read failed.
  const [outlookDay, setOutlookDay] = useState<OutlookDay | null>(null);
  // The U.S. Drought Monitor on the Field view: the week shown ("YYYYMMDD"), or null for the newest released.
  const [floodOn, setFloodOn] = useState(false);
  const [floodLid, setFloodLid] = useState<string | null>(null);
  const [floodGauge, setFloodGauge] = useState<FloodGauge | null>(null);
  const [floodFailed, setFloodFailed] = useState<string | null>(null);
  const [floodClock, setFloodClock] = useState(() => Date.now());
  const floodOnRef = useRef(false);
  const floodGaugesWereOnRef = useRef(false);
  const [droughtOn, setDroughtOn] = useState(false);
  const [droughtWeek, setDroughtWeek] = useState<string | null>(null);
  const [droughtMaps, setDroughtMaps] = useState<ReadonlyMap<string, DroughtMap>>(() => new Map());
  const [droughtFailed, setDroughtFailed] = useState<string | null>(null);
  const [droughtSeries, setDroughtSeries] = useState<DroughtSeries | null>(null);
  const [droughtSeriesFailed, setDroughtSeriesFailed] = useState(false);
  const lastDroughtRef = useRef<DroughtMap | null>(null);
  const lastDroughtChangeRef = useRef<Readonly<{ weeks: DroughtChangeWeeks; from: string; to: string; data: FeatureCollection }> | null>(null);
  const droughtReadAtRef = useRef(new Map<string, number>());
  const droughtSeriesReadAtRef = useRef(0);
  const [droughtTick, setDroughtTick] = useState(0);
  // The county picked in the Drought Monitor's county list, by GEOID.
  const [droughtCounty, setDroughtCounty] = useState<string | null>(null);
  const droughtCountiesAskedRef = useRef(false);
  const [droughtPlaying, setDroughtPlaying] = useState(false);
  // A change view: the week shown against 4 or 12 weeks before it, or 0 for the categories.
  const [droughtChange, setDroughtChange] = useState<DroughtChangeWeeks>(0);
  const [droughtSinceFailed, setDroughtSinceFailed] = useState<string | null>(null);
  const [outlookHazard, setOutlookHazard] = useState<OutlookProduct>("cat");
  const [outlooks, setOutlooks] = useState<Partial<Record<string, SpcOutlook>>>({});
  const [outlookFailed, setOutlookFailed] = useState<string | null>(null);
  // Bumped when a shown outlook reaches its quarter-hour, so the read below runs again.
  const [outlookTick, setOutlookTick] = useState(0);
  // When this browser last read each outlook, by its own clock: the provider's
  // retrievedAt can be older than the refresh (a cached answer, a skewed clock)
  // and must never make a fresh read look stale.
  const outlookReadAtRef = useRef(new Map<string, number>());
  // SPC's preliminary storm reports (Storm desk): the convective day shown (null
  // when off), the days read so far, the day whose read failed, and the report
  // selected on the map.
  const [reportsDay, setReportsDay] = useState<ReportDay | null>(null);
  const [stormReports, setStormReports] = useState<Partial<Record<ReportDay, StormReports>>>({});
  const [reportsFailed, setReportsFailed] = useState<ReportDay | null>(null);
  const [reportsTick, setReportsTick] = useState(0);
  const [reportSelected, setReportSelected] = useState<StormReport | null>(null);
  // The feature picked in a shown reviewed snapshot, by its release feature id; it lapses with the release.
  const [reviewedPick, setReviewedPick] = useState<string | null>(null);
  const stormReportsRef = useRef<ReadonlyMap<string, StormReport>>(new Map());
  // When this browser last read each day's reports, by its own clock (as for the outlook).
  const reportsReadAtRef = useRef(new Map<ReportDay, number>());
  // The landscape the photo-real 3D view last flew to.
  const [photorealPlace, setPhotorealPlace] = useState<string | null>(null);
  // The provider hillshade switched off on entering the photograph, restored on return.
  const photorealHidHillshadeRef = useRef(false);
  const [categoryDockHidden, setCategoryDockHidden] = useState(false);
  const aviationPickingRef = useRef(false);
  const setAviationPicking = useCallback((active: boolean) => {
    aviationPickingRef.current = active;
    if (active) {
      if (hoverDrawerTimerRef.current !== null) window.clearTimeout(hoverDrawerTimerRef.current);
      hoverDrawerTimerRef.current = null; hoverCandidateIdRef.current = null;
      setHoverActive(false); setHoverSummary(null);
    }
  }, []);
  const [aviationSelected, setAviationSelected] = useState(false);
  const [aviationShowRequest, setAviationShowRequest] = useState(0);
  const [aviationResearch, setAviationResearch] = useState<readonly ResearchRecord[] | null>(null);
  const [aviationInspect, setAviationInspect] = useState<Readonly<{ lon: number; lat: number; label: string; nonce: number }> | null>(null);
  const { inspectionPanel, rightOpen, qwenOpen, setRightOpen, setQwenOpen, previewEvidence } = useInspectionPanel();
  const [timelineOpen, setTimelineOpen] = useState(false);
  const [drawerView, setDrawerView] = useState<DrawerView>("evidence");
  const [focusStage, setFocusStage] = useState<FocusStage>("outcome");
  const [focusIntent, setFocusIntent] = useState<FocusIntentId>("explain");
  const [pendingFocusAction, setPendingFocusAction] = useState<FocusActionProposal | null>(null);
  const [layerQuery, setLayerQuery] = useState("");
  const [pendingCatalogTarget, setPendingCatalogTarget] = useState<string | null>(null);
  const [atlasViewQuery, setAtlasViewQuery] = useState("");
  const [atlasTopic, setAtlasTopic] = useState<LayerWorkspace>("all");
  const [layerDomain, setLayerDomain] = useState<(typeof layerDomains)[number]>("ALL");
  const [globalQuery, setGlobalQuery] = useState("");
  const [expandedLayers, setExpandedLayers] = useState<Set<string>>(new Set());
  const [year, setYear] = useState<number>(OFFICIAL_CONTEXT_PRESENT_FRAME);
  const [previewYear, setPreviewYear] = useState<number>(OFFICIAL_CONTEXT_PRESENT_FRAME);
  const [baselineDay, setBaselineDay] = useState(currentUtcDay);
  const [mapEvidenceFilter, setMapEvidenceFilter] = useState<RegistryEvidenceFilter>("ALL");
  const [playing, setPlaying] = useState(false);
  const [temporalMode, setTemporalMode] = useState<TemporalSweepMode>("snapshot");
  const [temporalStepRule, setTemporalStepRule] = useState<TemporalStepRule>("regular-calendar");
  const [playbackSpeed, setPlaybackSpeed] = useState<PlaybackSpeed>(1);
  const [playbackDirection, setPlaybackDirection] = useState<TemporalPlaybackDirection>("forward");
  const [playbackLoopMode, setPlaybackLoopMode] = useState<TemporalLoopMode>("stop");
  const [sweepRangeStart, setSweepRangeStart] = useState<number>(TIME_STEPS[0]);
  const [sweepRangeEnd, setSweepRangeEnd] = useState<number>(TIME_STEPS.at(-1)!);
  const [movingWindowFrames, setMovingWindowFrames] = useState(3);
  const [calendarSweep, setCalendarSweep] = useState<CalendarSweepView | null>(null);
  const calendarSweepRef = useRef<CalendarSweepView | null>(null);
  const calendarSeekGeneration = useRef(0);
  const calendarArchiveLoads = useRef(new Map<OfficialContextFeedId, { day: string; promise: Promise<void> }>());
  useEffect(() => { calendarSweepRef.current = calendarSweep; }, [calendarSweep]);
  const [measureMode, setMeasureMode] = useState<MeasureMode>(null);
  const [measurementGeometryMode, setMeasurementGeometryMode] = useState<MeasureMode>(null);
  const [measureCoordinateCount, setMeasureCoordinateCount] = useState(0);
  const [measureUnit, setMeasureUnit] = useState<MeasureUnit>("imperial");
  const [measurement, setMeasurement] = useState("Select a measurement tool");
  const [terrainProfile, setTerrainProfile] = useState<readonly TerrainProfileSample[]>([]);
  const [mapUtilityOpen, setMapUtilityOpen] = useState(false);
  const [mapUtilityFocusRequest, setMapUtilityFocusRequest] = useState(0);
  const [mapContextOpen, setMapContextOpen] = useState(false);
  const composerRef = useRef<HTMLElement>(null);
  const mapGuideRef = useRef<HTMLElement>(null);
  const composerTriggerRef = useRef<HTMLButtonElement>(null);
  const [mapUtilityView, setMapUtilityView] = useState<MapUtilityView>("scene");
  const [mapFeatureQuery, setMapFeatureQuery] = useState("");
  const [mapFeatureLayer, setMapFeatureLayer] = useState("ALL");
  const [connectionQuery, setConnectionQuery] = useState("");
  const [connectionFilter, setConnectionFilter] = useState<"ALL" | "VISIBLE" | "READY" | "ERROR">("ALL");
  const [sourceActivity, setSourceActivity] = useState<Record<string, "WAITING" | "UPDATING" | "SETTLED">>(
    Object.fromEntries(LAYER_REGISTRY.map((layer) => [layer.id, "WAITING"])),
  );
  const [sourceProbeCounts, setSourceProbeCounts] = useState<Record<string, number>>({});
  const [mapQueryCandidates, setMapQueryCandidates] = useState<readonly MapQueryCandidate[]>([]);
  const [inspectViewportOnly, setInspectViewportOnly] = useState(false);
  const [inspectVisibleLayersOnly, setInspectVisibleLayersOnly] = useState(false);
  const [nearbyRadiusMiles, setNearbyRadiusMiles] = useState<ResearchRadius>(25);
  const [compareTimeA, setCompareTimeA] = useState<number>(1910);
  const [compareTimeB, setCompareTimeB] = useState<number>(OFFICIAL_CONTEXT_PRESENT_FRAME);
  const [coordinateLatitude, setCoordinateLatitude] = useState(String(KANSAS_VIEW.center[1]));
  const [coordinateLongitude, setCoordinateLongitude] = useState(String(KANSAS_VIEW.center[0]));
  const [coordinateError, setCoordinateError] = useState("");
  const [projection, setProjection] = useState<"mercator" | "globe">("mercator");
  const [helpOpen, setHelpOpen] = useState(false);
  // Welcome is decided after hydration alongside URL/history restoration.
  // null owns the first server/client paint until URL and device preferences resolve.
  const [guideOpen, setGuideOpen] = useState<boolean | null>(null);
  // While the welcome covers the map, `?` reveals the map's source credits instead.
  const [welcomeSourcesOpen, setWelcomeSourcesOpen] = useState(false);
  const [repositoryOpen, setRepositoryOpen] = useState(false);
  const [currentWorkspace, setCurrentWorkspace] = useState<PublicWorkspaceId>("explore");
  const [repositoryView, setRepositoryView] = useState<RepositoryView>("updates");
  const [scenarioReviewMode, setScenarioReviewMode] = useState<ScenarioReviewMode>("held");
  const [functionGroup, setFunctionGroup] = useState<FunctionGroup>("PUBLIC_INTERFACE");
  const [activeFunctionId, setActiveFunctionId] = useState("export");
  const [functionQuery, setFunctionQuery] = useState("");
  const [featureQuery, setFeatureQuery] = useState("");
  const [featureTopic, setFeatureTopic] = useState<LayerWorkspace>("all");
  const [functionTopic, setFunctionTopic] = useState<LayerWorkspace>("all");
  const [featureArea, setFeatureArea] = useState<FeatureArea | "ALL">("ALL");
  const [featureMaturity, setFeatureMaturity] = useState<FeatureMaturity | "ALL">("ALL");
  const [repositoryQuery, setRepositoryQuery] = useState("");
  const [repositoryStateFilter, setRepositoryStateFilter] = useState<"ALL" | RepositoryUpdateState>("ALL");
  const [repositoryConnection, setRepositoryConnection] = useState<RepositoryConnection>({ state: "idle" });
  const [repositoryRefreshKey, setRepositoryRefreshKey] = useState(0);
  const [activeTransitionId, setActiveTransitionId] = useState(TRANSITION_BOUNDARIES[0].id);
  const [governedRoute, setGovernedRoute] = useState<GovernedRoute>("/bootstrap");
  const [governedMethod, setGovernedMethod] = useState<GovernedMethod>("GET");
  const [sourceObservatoryView, setSourceObservatoryView] = useState<SourceObservatoryView>("candidates");
  const [sourceQuery, setSourceQuery] = useState("");
  const [sourceDomain, setSourceDomain] = useState("ALL");
  const [sourceAdmissionState, setSourceAdmissionState] = useState<SourceAdmissionState | "ALL">("ALL");
  const [exportGeneratedAt, setExportGeneratedAt] = useState("PREVIEW_NOT_OPENED");
  const [reportGeneratedAt, setReportGeneratedAt] = useState("LIVE PREVIEW");
  const [reportTitle, setReportTitle] = useState("Kansas map data report");
  const [reportScope, setReportScope] = useState<ReportScope>("VIEWPORT");
  const [reportDetail, setReportDetail] = useState<ReportDetail>("STANDARD");
  const [reportLayerIds, setReportLayerIds] = useState<string[]>(defaultReportLayerIds);
  const [reportSections, setReportSections] = useState<Record<ReportSection, boolean>>(defaultReportSections);
  const [reportQuery, setReportQuery] = useState("");
  const [reportEvidenceFilter, setReportEvidenceFilter] = useState<EvidenceState | "ALL">("ALL");
  const [workspaceName, setWorkspaceName] = useState("");
  const [savedWorkspaces, setSavedWorkspaces] = useState<WorkspaceSnapshot[]>([]);
  const [activePlaceId, setActivePlaceId] = useState<string | null>(null);
  const [placeTourPlaying, setPlaceTourPlaying] = useState(false);
  const [runtimeSeamState, setRuntimeSeamState] = useState<RuntimeSeamState>("IDLE");
  const [runtimeSeamReason, setRuntimeSeamReason] = useState("Awaiting deterministic replay");
  const [cropSelected, setCropSelected] = useState(false);
  const [reviewedWaterSelected, setReviewedWaterSelected] = useState(false);
  const [reviewedWeatherSelected, setReviewedWeatherSelected] = useState(false);
  const [soilMapState, setSoilMapState] = useState<SoilMapState>(DEFAULT_SOIL_MAP_STATE);
  const changeSoilMapState = useCallback((next: Partial<SoilMapState>) => setSoilMapState(current => ({ ...current, ...next })), []);
  const [soilMoistureContext, setSoilMoistureContext] = useState<SoilMoistureEngineContext | null>(null);
  const [toast, setToast] = useState("");
  const [isCompact, setIsCompact] = useState(false);
  const [sourceStates, setSourceStates] = useState<Record<string, "loading" | "ready" | "error">>(
    Object.fromEntries(LAYER_REGISTRY.map((layer) => [layer.id, "loading"])),
  );

  const surfaceInspectionOpen = scenePanelOpen && terrainSurfaceMode !== "off" && !measureMode && !undergroundOpen && runtime.kind !== "unsupported";
  const surfaceInspectionOpenRef = useRef(surfaceInspectionOpen);
  surfaceInspectionOpenRef.current = surfaceInspectionOpen;
  const surfaceEvidencePendingRef = useRef(false);

  useEffect(() => {
    if (surfaceInspectionOpen || !surfaceEvidencePendingRef.current) return;
    surfaceEvidencePendingRef.current = false;
    // Reveal the sampled selection after Scene closes, unless another tool won focus.
    if (!qwenOpen && !leftOpen && !mapUtilityOpen && !timelineOpen && !sourceStatusOpen && !helpOpen && !repositoryOpen && !mapContextOpen) setRightOpen(true);
  }, [surfaceInspectionOpen, qwenOpen, leftOpen, mapUtilityOpen, timelineOpen, sourceStatusOpen, helpOpen, repositoryOpen, mapContextOpen, setRightOpen]);

  const debouncedGlobalQuery = useDebounced(globalQuery, 140);
  const debouncedLayerQuery = useDebounced(layerQuery, 140);

  useEffect(() => { visibilityRef.current = visibility; }, [visibility]);
  useEffect(() => { opacityRef.current = opacity; }, [opacity]);
  useEffect(() => { officialVisibilityRef.current = officialVisibility; }, [officialVisibility]);
  useEffect(() => {
    const check = () => {
      const current = new Date().getUTCFullYear() === OFFICIAL_CONTEXT_PRESENT_FRAME;
      if (!current && buildYearCurrentRef.current) {
        for (const controller of officialRequestsRef.current.values()) controller.abort();
        noaaRadarRequestRef.current?.abort();
        noaaSatelliteRequestRef.current?.abort();
        streamflowRequestRef.current?.abort();
        noaaHydrologyRequestRef.current?.abort();
      }
      buildYearCurrentRef.current = current;
      setBuildYearCurrent(current);
    };
    check();
    const timer = window.setInterval(check, 60_000);
    document.addEventListener("visibilitychange", check);
    return () => { window.clearInterval(timer); document.removeEventListener("visibilitychange", check); };
  }, []);
  const runtimeOfficialVisibility = useCallback((visibility: Record<OfficialContextId, boolean>, frame: number, radarReady: boolean, radarFrameTime: string | null) =>
    officialContextRuntimeVisibility(visibility, frame, radarReady, radarFrameTime, buildYearCurrentRef.current, calendarSweepRef.current ? calendarFrameDay(calendarSweepRef.current) : null, checkedCalendarDays(officialArchiveDaysRef.current, officialArchivePayloadsRef.current)), []);
  useEffect(() => { officialOpacityRef.current = officialOpacity; }, [officialOpacity]);
  useEffect(() => { officialPayloadsRef.current = officialPayloads; }, [officialPayloads]);
  useEffect(() => { noaaRadarManifestRef.current = noaaRadarManifest; }, [noaaRadarManifest]);
  useEffect(() => { noaaRadarFrameTimeRef.current = noaaRadarFrameTime; }, [noaaRadarFrameTime]);
  useEffect(() => { noaaRadarPendingFrameTimeRef.current = noaaRadarPendingFrameTime; }, [noaaRadarPendingFrameTime]);
  useEffect(() => { noaaRadarFollowLatestRef.current = noaaRadarFollowLatest; }, [noaaRadarFollowLatest]);
  useEffect(() => { streamflowBundleRef.current = streamflowBundle; }, [streamflowBundle]);
  useEffect(() => { orderRef.current = layerOrder; }, [layerOrder]);
  useEffect(() => { yearRef.current = year; }, [year]);
  useEffect(() => {
    setSweepRangeStart((current) => Math.min(current, year));
    setSweepRangeEnd((current) => Math.max(current, year));
  }, [year]);
  useEffect(() => { mapEvidenceFilterRef.current = mapEvidenceFilter; }, [mapEvidenceFilter]);
  useEffect(() => { basemapRef.current = basemap; }, [basemap]);
  useEffect(() => { projectionRef.current = projection; }, [projection]);
  useEffect(() => { scenePresetRef.current = scenePreset; }, [scenePreset]);
  useEffect(() => { verticalExaggerationRef.current = verticalExaggeration; }, [verticalExaggeration]);
  useEffect(() => { atmospherePresetRef.current = atmospherePreset; }, [atmospherePreset]);
  useEffect(() => { lightAzimuthRef.current = lightAzimuth; }, [lightAzimuth]);
  useEffect(() => { fieldOfViewRef.current = fieldOfView; }, [fieldOfView]);
  useEffect(() => { structures3DRef.current = structures3DEnabled; }, [structures3DEnabled]);
  useEffect(() => { gestureModeRef.current = gestureMode; }, [gestureMode]);
  useEffect(() => { boxDragModeRef.current = boxDragMode; }, [boxDragMode]);
  useEffect(() => { importPreviewRef.current = importPreview; }, [importPreview]);
  useEffect(() => { importPreviewVisibleRef.current = importPreviewVisible; }, [importPreviewVisible]);
  useEffect(() => {
    const preference = window.matchMedia("(prefers-reduced-motion: reduce)");
    const syncPreference = () => {
      setReducedMotion(preference.matches);
      if (preference.matches) {
        setPlaying(false);
        setNoaaRadarPlaying(false);
        daylightPlayingRef.current = false;
        setDaylightPlaying(false);
      }
    };
    syncPreference();
    preference.addEventListener("change", syncPreference);
    return () => preference.removeEventListener("change", syncPreference);
  }, []);

  useEffect(() => {
    if (!daylightPlaying || !daylightEnabled || reducedMotion || document.hidden) return;
    let animationFrame = 0;
    let lastMapUpdate = 0;
    let lastClockUpdate = 0;
    const loopDurationMs = kansasCalendarDaysInclusive(daylightDay, daylightThroughDay) * DAYLIGHT_LOOP_DURATION_MS;
    const startFraction = dateRangeLoopFractionAtInstant(daylightInstantRef.current, daylightDay, daylightThroughDay);
    const startedAt = performance.now();
    const tick = (now: number) => {
      if (!daylightPlayingRef.current || document.hidden) return;
      const fraction = daylightLoopFraction(startFraction, now - startedAt, loopDurationMs);
      const instant = instantAtDateRangeLoopFraction(daylightDay, daylightThroughDay, fraction);
      if (now - lastMapUpdate >= 33) {
        daylightInstantRef.current = instant;
        if (mapRef.current && styleGenerationReadyRef.current && daylightEnabledRef.current) {
          setDaylightMapLayer(mapRef.current, true, instant);
        }
        lastMapUpdate = now;
      }
      if (now - lastClockUpdate >= 100) {
        setDaylightInstant(instant);
        lastClockUpdate = now;
      }
      animationFrame = window.requestAnimationFrame(tick);
    };
    animationFrame = window.requestAnimationFrame(tick);
    return () => window.cancelAnimationFrame(animationFrame);
  }, [daylightDay, daylightEnabled, daylightPlaying, daylightThroughDay, reducedMotion]);

  useEffect(() => {
    const pauseWhenHidden = () => {
      if (!document.hidden) return;
      daylightPlayingRef.current = false;
      setDaylightPlaying(false);
    };
    document.addEventListener("visibilitychange", pauseWhenHidden);
    return () => document.removeEventListener("visibilitychange", pauseWhenHidden);
  }, []);
  useEffect(() => {
    const restoreSavedWorkspaces = window.setTimeout(() => {
      try {
        const result = parseSavedWorkspaceList(window.localStorage.getItem(WORKSPACE_STORAGE_KEY), MAX_PLACE_TRAIL_STOPS);
        const restored = result.records as unknown as WorkspaceSnapshot[];
        setSavedWorkspaces(restored);
        if (result.rejected) {
          if (restored.length) window.localStorage.setItem(WORKSPACE_STORAGE_KEY, JSON.stringify(restored));
          else window.localStorage.removeItem(WORKSPACE_STORAGE_KEY);
        }
      } catch { /* Device-local workspace storage is optional. */ }
    }, 0);
    return () => window.clearTimeout(restoreSavedWorkspaces);
  }, []);

  useEffect(() => () => {
    smokeTransitionsRef.current.cancel();
    if (placeTourTimerRef.current !== null) window.clearTimeout(placeTourTimerRef.current);
    for (const controller of officialRequestsRef.current.values()) controller.abort();
    officialRequestsRef.current.clear();
    noaaRadarRequestRef.current?.abort();
    noaaRadarFrameLoadCleanupRef.current?.();
    streamflowRequestRef.current?.abort();
    noaaHydrologyRequestRef.current?.abort();
  }, []);

  useEffect(() => { selectedRef.current = selected; }, [selected]);
  useEffect(() => { measureModeRef.current = measureMode; }, [measureMode]);
  useEffect(() => { measurementGeometryModeRef.current = measurementGeometryMode; }, [measurementGeometryMode]);
  useEffect(() => { measureUnitRef.current = measureUnit; }, [measureUnit]);

  const activeLayers = useMemo(() => LAYER_REGISTRY.filter((layer) => visibility[layer.id]), [visibility]);
  const visibleCount = activeLayers.length;
  const temporalSequence = useMemo(() => buildTemporalSequence(
    activeLayers,
    TIME_STEPS,
    sweepRangeStart,
    sweepRangeEnd,
    temporalStepRule,
  ), [activeLayers, sweepRangeEnd, sweepRangeStart, temporalStepRule]);
  const timelineSteps = useMemo(() => [...new Set([...TIME_STEPS, ...temporalSequence])].sort((left, right) => left - right), [temporalSequence]);
  const timelineLabels = useMemo(() => timelineLabelSteps(timelineSteps, TIMELINE_MAJOR_STEPS), [timelineSteps]);
  const temporalQuery = useMemo(() => buildTemporalQuery(
    temporalMode,
    temporalMode === "comparison" ? compareTimeB : year,
    sweepRangeStart,
    sweepRangeEnd,
    temporalSequence,
    movingWindowFrames,
  ), [compareTimeB, movingWindowFrames, sweepRangeEnd, sweepRangeStart, temporalMode, temporalSequence, year]);
  const temporalFrameIndex = temporalSequence.indexOf(temporalQuery.frame);
  const comparisonTemporalFrame = temporalMode === "comparison"
    ? compareTimeA
    : nextTemporalFrame(
      temporalSequence,
      temporalQuery.frame,
      playbackDirection === "forward" ? "reverse" : "forward",
      "stop",
    );
  const comparisonTemporalQuery = useMemo(() => comparisonTemporalFrame === null ? null : buildTemporalQuery(
    temporalMode,
    comparisonTemporalFrame,
    sweepRangeStart,
    sweepRangeEnd,
    temporalSequence,
    movingWindowFrames,
  ), [comparisonTemporalFrame, movingWindowFrames, sweepRangeEnd, sweepRangeStart, temporalMode, temporalSequence]);
  const temporalMetricLayers = useMemo(() => mapEvidenceFilter === "ALL"
    ? activeLayers
    : activeLayers.map((layer) => ({
      ...layer,
      data: {
        ...layer.data,
        features: layer.data.features.filter((feature) => feature.properties.evidenceState === mapEvidenceFilter),
      },
    })), [activeLayers, mapEvidenceFilter]);
  const temporalFrameSummary = useMemo(
    () => buildTemporalFrameSummary(temporalMetricLayers, temporalQuery, comparisonTemporalQuery),
    [comparisonTemporalQuery, temporalMetricLayers, temporalQuery],
  );
  const temporalScopeLabel = temporalMode === "moving-window"
    ? `${formatTimelineStep(temporalQuery.windowStart)} to ${formatTimelineStep(temporalQuery.frame)}`
    : temporalMode === "accumulation"
      ? `${formatTimelineStep(temporalQuery.rangeStart)} through ${formatTimelineStep(temporalQuery.frame)}`
      : temporalMode === "comparison"
        ? `${formatTimelineStep(compareTimeA)} ↔ ${formatTimelineStep(compareTimeB)}`
      : formatTimelineStep(temporalQuery.frame);
  const temporalFramePosition = temporalFrameIndex >= 0 ? temporalFrameIndex + 1 : null;
  const previousSweepFrame = nextTemporalFrame(temporalSequence, temporalQuery.frame, "reverse", "stop");
  const nextSweepFrame = nextTemporalFrame(temporalSequence, temporalQuery.frame, "forward", "stop");
  useEffect(() => { temporalQueryRef.current = temporalQuery; }, [temporalQuery]);
  const visibleOfficialSources = useMemo(() => OFFICIAL_CONTEXT_SOURCES.filter((source) => officialVisibility[source.id]), [officialVisibility]);
  const visibleOfficialCount = visibleExternalContextCount(visibleOfficialSources.length, soilMapState.visible);
  const selectedEarthEngineCount = Object.values(earthEngineDisplay.visible).filter(Boolean).length;
  const catalogEntries: LayerCatalogEntry[] = [
    ...OFFICIAL_CONTEXT_SOURCES.map(source => ({ id: source.id, title: source.title, keywords: `${source.shortTitle} ${source.organization} ${source.domain}`, selected: officialVisibility[source.id], topics: officialSourceTopics(source.id) })),
    { id: "daylight", title: "Daylight & twilight", keywords: "sun solar geometry calculated light", topics: specialtyLayerTopics("daylight"), selected: daylightEnabled },
    { id: "soil", title: "Soil moisture", keywords: "NASA SMAP modeled surface root water", topics: specialtyLayerTopics("soil"), selected: soilMapState.visible },
    { id: "crop", title: "Soil moisture 1 km hybrid", keywords: "USDA NASS Crop-CASMA direct provider preview reviewed numeric cells", topics: specialtyLayerTopics("crop"), selected: cropSelected },
    { id: "reviewed-water", title: "Reviewed water stations", keywords: "USGS governed snapshot evidence", topics: specialtyLayerTopics("reviewed-water"), selected: reviewedWaterSelected },
    { id: "reviewed-weather", title: "Reviewed daily weather", keywords: "NOAA GHCN-Daily precipitation temperature governed snapshot evidence", topics: specialtyLayerTopics("reviewed-weather"), selected: reviewedWeatherSelected },
    { id: "aviation", title: "Airspace, airports & aviation weather", keywords: "FAA NASR airspace class B C D E airports runways airways 3D drone UAS LAANC TFR METAR PIREP ADS-B traffic", topics: specialtyLayerTopics("aviation"), selected: aviationSelected },
    ...EARTH_ENGINE_CONTEXT_LAYERS.map(layer => ({ id: layer.id, title: layer.title, keywords: `${layer.source} ${layer.attribution}`, topics: imageryTopics(layer.id), selected: Boolean(earthEngineDisplay.visible[layer.id]), imagery: true })),
    ...LAYER_REGISTRY.map(layer => ({ id: layer.id, title: layer.title, keywords: `${layer.domain} ${layer.description}`, topics: registryLayerTopics(layer.domain), selected: Boolean(visibility[layer.id]) })),
  ];
  const selectedMapLayerCount = selectedCatalogCount(catalogEntries);
  const matchingCatalogEntries = catalogEntries.filter(entry => layerEntryMatches(entry, layerCatalogView, officialWorkspace, officialSourceQuery));
  const shownCatalogIds = new Set(matchingCatalogEntries.map(entry => entry.id));
  const noaaRadarManifestFresh = noaaRadarManifestIsFresh(noaaRadarManifest, noaaRadarClock);
  const noaaRadarRenderable = Boolean(noaaRadarFrameTime && noaaRadarManifestFresh);
  useEffect(() => {
    noaaRadarReadyRef.current = noaaRadarRenderable;
    if (!noaaRadarRenderable) setNoaaRadarPlaying(false);
  }, [noaaRadarRenderable]);
  const effectiveOfficialVisibility = useMemo(
    () => officialContextRuntimeVisibility(officialVisibility, temporalQuery.frame, noaaRadarRenderable, noaaRadarFrameTime, buildYearCurrent, calendarSweep ? calendarFrameDay(calendarSweep) : null, checkedCalendarDays(officialArchiveDays, officialPayloads)),
    [buildYearCurrent, calendarSweep, noaaRadarFrameTime, noaaRadarRenderable, officialArchiveDays, officialPayloads, officialVisibility, temporalQuery.frame],
  );
  const civicFrameDay = civicDayForFrame(temporalQuery.frame, OFFICIAL_CONTEXT_PRESENT_FRAME, currentUtcDay(), calendarSweep ? calendarFrameDay(calendarSweep) : null);
  const civicFrameCongress = civicCongressForDay(civicFrameDay ?? "");
  const lightningSelected = effectiveOfficialVisibility["noaa-lightning-density"] && projection !== "globe";
  const lightningFrameIndex = lightningManifest?.frames.indexOf(lightningFrame ?? "") ?? -1;
  const lightningPlaybackReady = (lightningPreview === "signal" || lightningPreview === "none")
    && (officialStates["noaa-lightning-density"] === "ready" || officialStates["noaa-lightning-density"] === "empty");
  const composedSurfaceCount = activeLayers.filter((layer) => layer.renderers.some((renderer) => renderer.spec.type === "fill")).length
    + visibleOfficialSources.filter((source) => effectiveOfficialVisibility[source.id] && (source.kind === "OPERATIONAL_WMS" || source.layerIds.some((id) => id.endsWith("-fill")))).length
    + selectedEarthEngineCount;
  const withheldOfficialCount = visibleOfficialSources.filter((source) => !effectiveOfficialVisibility[source.id]).length;
  const selectedOfficialContextId = officialContextIdForSelection(selected);
  const selectedIsHeldOfficialContext = officialSelectionIsHeld(selected, temporalQuery.frame, buildYearCurrent, civicFrameDay);
  const selectedTimeMismatch = Boolean(
    selected
    && (selectedIsHeldOfficialContext || !isFeatureAvailableForTemporalQuery(selected.layer, selected.properties.year, temporalQuery)),
  );
  const officialFeatureCount = visibleOfficialSources.reduce((total, source) => total + (effectiveOfficialVisibility[source.id] ? officialPayloads[source.id as OfficialContextFeedId]?.featureCount ?? (officialStates[source.id] === "ready" ? GROUNDWATER_MANIFEST.find(item => item.id === source.id)?.featureCount ?? 0 : 0) : 0), 0);
  const officialReadyCount = visibleOfficialSources.filter((source) => effectiveOfficialVisibility[source.id] && ["ready", "partial", "empty"].includes(officialStates[source.id])).length;
  const officialLoadingCount = visibleOfficialSources.filter((source) => effectiveOfficialVisibility[source.id] && officialStates[source.id] === "loading").length;
  const officialRefreshPlan = planOfficialRefresh(OFFICIAL_CONTEXT_SOURCES, officialVisibility, temporalQuery.frame, OFFICIAL_CONTEXT_PRESENT_FRAME, Boolean(streamflowArchiveDay), officialArchiveDays);
  const officialLatestRetrievedAt = visibleOfficialSources.filter((source) => effectiveOfficialVisibility[source.id])
    .map((source) => officialPayloads[source.id as OfficialContextFeedId]?.retrievedAt)
    .filter((value): value is string => Boolean(value))
    .concat(effectiveOfficialVisibility["nws-radar"] ? noaaRadarManifest?.retrievedAt ?? [] : [])
    .concat(effectiveOfficialVisibility["noaa-goes-geocolor"] ? noaaSatelliteManifest?.retrievedAt ?? [] : [])
    .concat(effectiveOfficialVisibility["nws-forecast-wind"] ? windArrowFrame?.retrievedAtUtc ?? [] : [])
    .sort()
    .at(-1) ?? null;
  const earthquakeArchiveFrames = useMemo(() => {
    const day = officialArchiveDays["usgs-earthquakes"];
    const payload = officialArchivePayloadsRef.current["usgs-earthquakes"];
    if (!day || !payload) return [];
    return earthquakeEventTimes(payload, day);
  }, [officialArchiveDays, officialPayloads]);
  const smokeArchiveFrames = useMemo(() => {
    const day = officialArchiveDays["noaa-hms-smoke"];
    const payload = officialArchivePayloadsRef.current["noaa-hms-smoke"];
    return day && payload ? smokeValidityTimes(payload, day) : [];
  }, [officialArchiveDays, officialPayloads]);
  const streamflowFrames = useMemo(() => streamflowBundle
    ? streamflowArchiveDay ? streamflowExactFrames(streamflowBundle) : streamflowDisplayFrames(streamflowBundle)
    : [], [streamflowArchiveDay, streamflowBundle]);
  const safeStreamflowFrameIndex = streamflowFrames.length === 0 ? -1 : clamp(streamflowFrameIndex, 0, streamflowFrames.length - 1);
  const streamflowFrameTime = safeStreamflowFrameIndex >= 0 ? streamflowFrames[safeStreamflowFrameIndex] : streamflowBundle?.query.end ?? null;
  const streamflowFrame = useMemo<StreamflowFrame | null>(() => {
    if (!streamflowBundle || !streamflowFrameTime) return null;
    const toleranceMinutes = streamflowRange === "1y" ? 36 * 60 : streamflowRange === "24h" ? 30 : 90;
    return buildStreamflowFrame(streamflowBundle, streamflowFrameTime, toleranceMinutes);
  }, [streamflowBundle, streamflowFrameTime, streamflowRange]);
  const streamflowSelectedStation = useMemo(() => streamflowBundle?.stations.find((station) => station.stationId === streamflowSelectedStationId) ?? null,
    [streamflowBundle, streamflowSelectedStationId]);
  const selectedWaterCue = useMemo(() => waterReadingCue(
    streamflowFrame?.features.find((feature) => feature.properties.stationId === streamflowSelectedStationId)?.properties ?? null,
    streamflowBundle && streamflowSelectedStationId ? stationObservations(streamflowBundle, streamflowSelectedStationId) : [],
  ), [streamflowBundle, streamflowFrame, streamflowSelectedStationId]);
  const streamflowLatestTime = streamflowFrames.at(-1) ?? null;
  const streamflowLatestAgeMinutes = streamflowLatestTime ? Math.max(0, Math.floor((Date.now() - Date.parse(streamflowLatestTime)) / 60_000)) : null;
  const streamflowDisplayState: HydrologyObservatoryState = streamflowState === "ready"
    && streamflowBundle?.query.mode === "recent-series"
    && streamflowLatestAgeMinutes !== null
    && streamflowLatestAgeMinutes > 60
    ? "stale"
    : streamflowState;
  const streamflowSelectedAtPresent = buildYearCurrent && officialVisibility["usgs-streamflow"] && temporalQuery.frame === OFFICIAL_CONTEXT_PRESENT_FRAME;
  const noaaHydrologySelectedAtPresent = buildYearCurrent && officialVisibility["noaa-nwps-gauges"] && temporalQuery.frame === OFFICIAL_CONTEXT_PRESENT_FRAME;
  const mapSignals = useMemo(() => deriveMapSignals({
    streamflow: streamflowSelectedAtPresent && (streamflowState === "ready" || streamflowState === "partial") ? streamflowFrame : null,
    gauges: noaaHydrologySelectedAtPresent && ["ready", "partial"].includes(officialStates["noaa-nwps-gauges"])
      ? officialPayloads["noaa-nwps-gauges"]?.data.features.map((feature) => feature.properties as NoaaGaugeFeatureProperties) : undefined,
    entered: temporalFrameSummary.entered.length,
    exited: temporalFrameSummary.exited.length,
  }), [noaaHydrologySelectedAtPresent, officialPayloads, officialStates, streamflowFrame, streamflowSelectedAtPresent, streamflowState, temporalFrameSummary]);
  const noaaRadarLoopFrames = useMemo(
    () => selectNoaaRadarLoopFrames(noaaRadarManifest?.frames ?? [], noaaRadarLoopSpan, NOAA_RADAR_MAX_LOOP_FRAMES),
    [noaaRadarLoopSpan, noaaRadarManifest?.frames],
  );
  const noaaRadarLatestFrame = noaaRadarLoopFrames.at(-1) ?? null;
  const noaaRadarFrameIndex = noaaRadarFrameTime ? noaaRadarLoopFrames.indexOf(noaaRadarFrameTime) : -1;
  const noaaRadarActiveFrame = noaaRadarFrameIndex >= 0 ? noaaRadarLoopFrames[noaaRadarFrameIndex] : null;
  const noaaRadarAgeMinutes = noaaRadarActiveFrame ? noaaRadarFrameAgeMinutes(noaaRadarActiveFrame, noaaRadarClock) : null;
  const noaaRadarLatestAgeMinutes = noaaRadarLatestFrame ? noaaRadarFrameAgeMinutes(noaaRadarLatestFrame, noaaRadarClock) : null;
  const noaaRadarSelectedAtPresent = buildYearCurrent && officialVisibility["nws-radar"] && temporalQuery.frame === OFFICIAL_CONTEXT_PRESENT_FRAME;
  const noaaSatelliteSelectedAtPresent = buildYearCurrent && officialVisibility["noaa-goes-geocolor"] && temporalQuery.frame === OFFICIAL_CONTEXT_PRESENT_FRAME;
  const lightningSelectedAtPresent = buildYearCurrent && officialVisibility["noaa-lightning-density"] && temporalQuery.frame === OFFICIAL_CONTEXT_PRESENT_FRAME;
  const glmFlashesAllowed = buildYearCurrent && temporalQuery.frame === OFFICIAL_CONTEXT_PRESENT_FRAME && projection !== "globe";
  useEffect(() => { if (!glmFlashesAllowed) setGlmFlashesEnabled(false); }, [glmFlashesAllowed]);
  const availableLiveInstruments = [
    ...(streamflowSelectedAtPresent ? ["river" as const] : []),
    ...(noaaRadarSelectedAtPresent ? ["radar" as const] : []),
    ...(lightningSelectedAtPresent ? ["lightning" as const] : []),
  ];
  const activeLiveInstrument = availableLiveInstruments.includes(liveInstrument) ? liveInstrument : availableLiveInstruments[0] ?? null;
  const liveDockVisible = instrumentOpen && activeLiveInstrument !== null;
  const showStreamflowDock = activeLiveInstrument === "river";
  const showRadarDock = activeLiveInstrument === "radar";
  const showLightningDock = activeLiveInstrument === "lightning";
  const noaaRadarSelectedIsLatest = Boolean(noaaRadarActiveFrame && noaaRadarLatestFrame && noaaRadarActiveFrame === noaaRadarLatestFrame);
  const noaaRadarFrameError = noaaRadarManifestError
    || (noaaRadarManifest && !noaaRadarManifestFresh ? "The newest advertised NOAA observation is more than 15 minutes old." : "")
    || (noaaRadarFrameLoadState === "error" ? officialErrors["nws-radar"] ?? "The requested NOAA radar image did not finish loading." : "");
  const noaaRadarDisplayState = noaaRadarManifestState === "loading"
    ? "LOADING FRAMES"
    : noaaRadarManifestState === "error" && noaaRadarRenderable
      ? "FROZEN"
      : noaaRadarManifestState === "error"
        ? "UNAVAILABLE"
        : noaaRadarManifest && !noaaRadarManifestFresh
          ? "UNAVAILABLE"
        : noaaRadarFrameLoadState === "error" && noaaRadarRenderable
          ? "FROZEN"
          : noaaRadarFrameLoadState === "error"
            ? "UNAVAILABLE"
        : noaaRadarFrameLoadState === "loading"
          ? "BUFFERING"
          : noaaRadarPlaying
            ? "PLAYING"
            : noaaRadarFollowLatest && noaaRadarSelectedIsLatest
              ? "LATEST"
              : "PAUSED";
  const noaaRadarFrameHeadline = noaaRadarPendingFrameTime && noaaRadarFrameLoadState === "loading"
    ? `Buffering ${formatNoaaRadarLocalTime(noaaRadarPendingFrameTime)}`
    : noaaRadarActiveFrame
      ? formatNoaaRadarLocalTime(noaaRadarActiveFrame)
      : noaaRadarManifestState === "loading"
        ? "Discovering exact frames…"
        : "No observation selected";
  const noaaRadarFrameDetail = noaaRadarPendingFrameTime && noaaRadarFrameLoadState === "loading"
    ? `${formatNoaaRadarUtcTime(noaaRadarPendingFrameTime)} requested · ${noaaRadarFrameTime ? `last confirmed ${formatNoaaRadarLocalTime(noaaRadarFrameTime)}` : "no confirmed image yet"}`
    : noaaRadarActiveFrame
      ? `${formatNoaaRadarUtcTime(noaaRadarActiveFrame)} · ${noaaRadarAgeMinutes ?? "?"} min ago`
      : "Radar remains hidden until NOAA supplies a valid frame list";
  const noaaRadarCrossDomainSources = [
    effectiveOfficialVisibility["nws-alerts"] && (officialPayloads["nws-alerts"]?.featureCount ?? 0) > 0 ? "active alert areas" : null,
    effectiveOfficialVisibility["usgs-streamflow"] && (officialPayloads["usgs-streamflow"]?.featureCount ?? 0) > 0 ? "streamflow observations" : null,
    effectiveOfficialVisibility["usgs-earthquakes"] && (officialPayloads["usgs-earthquakes"]?.featureCount ?? 0) > 0 ? "recent earthquake records" : null,
  ].filter((value): value is string => Boolean(value));
  const mapContextRecords = useMemo(() => activeLayers.flatMap((layer) => layer.data.features.filter((feature) => (
    isFeatureAvailableForTemporalQuery(layer, feature.properties.year, temporalQuery)
    && feature.properties.focusLng >= mapViewportBounds.west
    && feature.properties.focusLng <= mapViewportBounds.east
    && feature.properties.focusLat >= mapViewportBounds.south
    && feature.properties.focusLat <= mapViewportBounds.north
  ))), [activeLayers, mapViewportBounds, temporalQuery]);
  const supportedMapContextCount = useMemo(() => mapContextRecords.filter((feature) => (
    (feature.properties.evidenceState === "ANSWER" || feature.properties.evidenceState === "CORRECTED") && feature.properties.sourceRole === "source-backed-context"
  )).length, [mapContextRecords]);
  const allEvidenceRecords = useMemo<readonly EvidenceRecord[]>(() => LAYER_REGISTRY.flatMap((layer) => {
    const sourceCandidate = SOURCE_CANDIDATES.find((candidate) => candidate.layerId === layer.id);
    return layer.data.features.map((feature) => ({
      id: `evidence:${layer.id}:${feature.properties.fid}`,
      featureId: feature.properties.fid,
      layerId: layer.id,
      title: feature.properties.title,
      domain: layer.domain,
      sourceOrganization: feature.properties.sourceOrganization,
      sourceRole: feature.properties.sourceRole,
      citation: feature.properties.citation,
      officialUrl: sourceCandidate?.sourceUrl,
      spatialScope: feature.properties.spatialScope,
      displayFocus: [feature.properties.focusLng, feature.properties.focusLat] as const,
      temporalExtent: {
        start: feature.properties.year,
        end: feature.properties.year,
        label: feature.properties.temporalScope,
        mode: layer.temporal ? "instant" as const : "unknown" as const,
        uncertainty: feature.properties.uncertainty,
      },
      trustState: trustStateFromEvidenceState(feature.properties.evidenceState, feature.properties.sourceRole),
      evidenceState: feature.properties.evidenceState,
      supports: feature.properties.summary,
      cannotProve: feature.properties.generalizationNote,
      caveat: feature.properties.uncertainty,
      policyStatus: `${feature.properties.releaseState} · ${feature.properties.reviewState}`,
      includedByDefault: feature.properties.evidenceState === "ANSWER" || feature.properties.evidenceState === "CORRECTED",
    }));
  }), []);
  const selectedSourceCandidate = useMemo(() => selected
    ? SOURCE_CANDIDATES.find((candidate) => candidate.layerId === selected.layerId)
    : undefined, [selected]);
  const filteredAtlasViews = useMemo(() => {
    const terms = atlasViewQuery.trim().toLowerCase().split(/\s+/).filter(Boolean);
    return LIVING_ATLAS_VIEWS.filter(view => (atlasTopic === "all" || atlasViewTopics(view.id).includes(atlasTopic))
      && terms.every(term => [view.title, view.question, view.scope, view.time, view.sourcePosture, view.report, ...view.domains, topicSearchText(atlasViewTopics(view.id))].join(" ").toLowerCase().includes(term)));
  }, [atlasViewQuery, atlasTopic]);
  const activeViewProfileId = useMemo(() => MAP_VIEW_PROFILES.find((profile) => (
    profile.year === year
    && profile.basemap === basemap
    && profile.projection === projection
    && LAYER_REGISTRY.every((layer) => visibility[layer.id] === profile.visibleLayerIds.includes(layer.id))
  ))?.id ?? null, [basemap, projection, visibility, year]);
  const activeAtlasView = useMemo(
    () => LIVING_ATLAS_VIEWS.find((atlasView) => atlasView.profileId === activeViewProfileId)
      ?? LIVING_ATLAS_VIEWS.find((atlasView) => atlasView.id === "kansas-overview"),
    [activeViewProfileId],
  );
  const primaryRepresentationLabel = scenePreset === "elevation-3d"
    ? `Terrain 3D · ${terrainState === "READY" ? "DEM" : terrainState === "ERROR" ? "unavailable" : "loading"}`
    : projection === "globe"
      ? "Globe"
      : "2D";
  const mapRepresentationLabel = `${primaryRepresentationLabel}${structures3DEnabled ? ` · Structures 3D ${structures3DState === "READY" ? "ready" : structures3DState.toLowerCase()}` : ""}`;
  const assistantFocus = useMemo<AssistantFocus>(() => {
    const privateView = locationCameraRedacted || locationDerivedViewRef.current || Boolean(subsurfaceInspection && subsurfacePrivate);
    const base = {version: 1 as const, frame: temporalQuery.frame, view: primaryRepresentationLabel, surface: 'map', filters: {evidence: mapEvidenceFilter, temporalMode}, ...(temporalMode === 'comparison' ? {comparison: {frameA: compareTimeA, frameB: compareTimeB}} : {}), layers: [...activeLayers.map(layer => layer.id),...visibleOfficialSources.map(source => source.id)].slice(0,14)};
    if (privateView) return {context: {...base, layers: [], selection: null}, title: "Private context withheld", detail: "Location-derived selections stay in this browser."};
    if (subsurfaceInspection) {
      const {record, interval} = subsurfaceInspection;
      const selection = sampleAssistantSelection(subsurfaceInspection);
      return {context: {...base, selection}, title: selection ? record.name : "Sample context unavailable", detail: selection ? `${interval ? `${interval.top}–${interval.bottom} ${record.depthUnit} · ${interval.description.slice(0,160)}` : `${record.id} · ${record.intervals.length} source intervals`} · source context, not admitted evidence` : "Select this sample again in Underground to bind its source tile."};
    }
    if (selected && !selectedTimeMismatch) {
      const p=selected.properties;
      if (["RESTRICTED_ACCESS","DENIED_BY_POLICY","GENERALIZED_GEOMETRY"].includes(p.evidenceState)) return {context: {...base, layers: [], selection: null}, title: "Protected context withheld", detail: "This selection is not sent to AI."};
      const clean=(value: string, limit: number)=>String(value || "Not supplied").replace(/[\x00-\x1f\x7f]/g," ").slice(0,limit);
      const selection=selected.kind === "registry" ? {kind: "registry" as const, layerId: selected.layerId, featureId: selected.featureId} : {kind: "display" as const, title: clean(p.title,160), source: clean(p.sourceOrganization,100), description: clean(p.summary,300), time: clean(p.temporalScope,100)};
      return {context: {...base, selection}, title: p.title, detail: `${p.sourceOrganization} · ${p.temporalScope} · display context; evidence remains separately governed`};
    }
    return {context: {...base, selection: null}, title: selectedTimeMismatch ? "Selection outside active time" : "Current map view", detail: selectedTimeMismatch ? "The incompatible selection is withheld. Choose its supported time to ask about it." : "Select a feature or Underground sample to ask about its details."};
  }, [activeLayers, visibleOfficialSources, mapEvidenceFilter, temporalMode, compareTimeA, compareTimeB, locationCameraRedacted, primaryRepresentationLabel, selected, selectedTimeMismatch, subsurfaceInspection, subsurfacePrivate, temporalQuery.frame]);

  const temporalComparison = useMemo(
    () => buildTemporalComparison(activeLayers, compareTimeA, compareTimeB),
    [activeLayers, compareTimeA, compareTimeB],
  );
  const temporalComparisonRows = useMemo(
    () => temporalComparison.layers.filter((layer) => layer.timeARecordCount > 0 || layer.timeBRecordCount > 0),
    [temporalComparison],
  );
  const temporalNoData = useMemo(() => activeLayers.filter((layer) => layer.temporal && !layer.data.features.some((feature) => (
    isFeatureAvailableForTemporalQuery(layer, feature.properties.year, temporalQuery)
  ))), [activeLayers, temporalQuery]);
  const availabilityByStep = useMemo(() => Object.fromEntries(timelineSteps.map((step) => {
    if (step < Math.min(sweepRangeStart, sweepRangeEnd) || step > Math.max(sweepRangeStart, sweepRangeEnd)) return [step, 0];
    const query = buildTemporalQuery(temporalMode, step, sweepRangeStart, sweepRangeEnd, temporalSequence, movingWindowFrames);
    return [step, temporalRecordsForQuery(temporalMetricLayers, query, true).length];
  })), [movingWindowFrames, sweepRangeEnd, sweepRangeStart, temporalMetricLayers, temporalMode, temporalSequence, timelineSteps]);
  const availabilityBins = useMemo(() => buildAvailabilityBins(timelineSteps, availabilityByStep), [timelineSteps, availabilityByStep]);
  const hasTimelineRecords = availabilityBins.some((bin) => bin.peak > 0);
  const sourceStateCounts = useMemo(() => ({
    ready: Object.values(sourceStates).filter((state) => state === "ready").length,
    loading: Object.values(sourceStates).filter((state) => state === "loading").length,
    error: Object.values(sourceStates).filter((state) => state === "error").length,
  }), [sourceStates]);
  const sourceConnections = useMemo(() => LAYER_REGISTRY.map((layer) => {
    const compatibleFeatures = layer.data.features.filter((feature) => isFeatureAvailableForTemporalQuery(layer, feature.properties.year, temporalQuery));
    const viewportFeatures = compatibleFeatures.filter((feature) => (
      feature.properties.focusLng >= mapViewportBounds.west
      && feature.properties.focusLng <= mapViewportBounds.east
      && feature.properties.focusLat >= mapViewportBounds.south
      && feature.properties.focusLat <= mapViewportBounds.north
    ));
    return {
      layer,
      state: sourceStates[layer.id],
      activity: sourceActivity[layer.id] ?? "WAITING",
      visible: Boolean(visibility[layer.id]),
      compatibleCount: compatibleFeatures.length,
      viewportCount: viewportFeatures.length,
      probeCount: sourceProbeCounts[layer.id],
    };
  }), [mapViewportBounds, sourceActivity, sourceProbeCounts, sourceStates, temporalQuery, visibility]);
  const filteredSourceConnections = useMemo(() => {
    const query = connectionQuery.trim().toLowerCase();
    return sourceConnections.filter((connection) => {
      if (connectionFilter === "VISIBLE" && !connection.visible) return false;
      if (connectionFilter === "READY" && connection.state !== "ready") return false;
      if (connectionFilter === "ERROR" && connection.state !== "error") return false;
      return !query || `${connection.layer.title} ${connection.layer.id} ${connection.layer.sourceId} ${connection.layer.domain} ${connection.layer.sourceType}`.toLowerCase().includes(query);
    });
  }, [connectionFilter, connectionQuery, sourceConnections]);
  const officialContextConnections = useMemo(() => OFFICIAL_CONTEXT_SOURCES.map((source) => {
    const payload = source.apiPath || source.managedAdapterPath ? officialPayloads[source.id as OfficialContextFeedId] : undefined;
    const snapshot = GROUNDWATER_MANIFEST.find(item => item.id === source.id);
    return {
      source: source.id === CIVIC_ID ? civicSourceForRecord(payload?.data.features[0]?.properties) : source,
      visible: officialVisibility[source.id],
      activeAtFrame: effectiveOfficialVisibility[source.id],
      state: officialStates[source.id],
      featureCount: payload?.featureCount ?? (officialStates[source.id] === "ready" ? snapshot?.featureCount : undefined),
      retrievedAt: source.id === "noaa-goes-geocolor" ? noaaSatelliteManifest?.retrievedAt : source.id === "noaa-lightning-density" ? lightningManifest?.retrievedAt : source.id === "nws-forecast-wind" ? windArrowFrame?.retrievedAtUtc : payload?.retrievedAt ?? snapshot?.retrievedAt,
      limitation: source.id === "noaa-goes-geocolor" ? noaaSatelliteManifest?.limitation : payload?.limitation,
      temporalSupport: OFFICIAL_CONTEXT_TEMPORAL_SUPPORT[source.id],
    };
  }), [effectiveOfficialVisibility, lightningManifest?.retrievedAt, noaaSatelliteManifest, officialPayloads, officialStates, officialVisibility, windArrowFrame?.retrievedAtUtc]);
  const researchWellInventoryReady = styleReady && effectiveOfficialVisibility["kgs-monitoring-wells"] && officialStates["kgs-monitoring-wells"] === "ready";
  useEffect(() => {
    setResearchSnapshotPoints(null);
    if (!researchWellInventoryReady) return;
    const source = mapRef.current?.getSource(OFFICIAL_CONTEXT_BY_ID["kgs-monitoring-wells"].sourceId) as GeoJSONSource | undefined;
    if (!source?.getData) return;
    const abort = new AbortController();
    void readResearchInventory(() => source.getData(), abort.signal, data => {
      if (data.type === "FeatureCollection") setResearchSnapshotPoints(data);
    });
    return () => abort.abort();
  }, [basemap, researchWellInventoryReady]);

  const researchData = useMemo(() => {
    const records: ResearchRecord[] = [];
    const coverage: ResearchCoverage[] = [...researchMissingSources];
    for (const layer of LAYER_REGISTRY.filter(item => visibility[item.id])) {
      const features = layer.data.features.filter(feature => layer.publicStatus !== "RESTRICTED"
        && ["ANSWER", "CORRECTED", "GENERALIZED_GEOMETRY"].includes(feature.properties.evidenceState)
        && isFeatureAvailableForTemporalQuery(layer, feature.properties.year, temporalQuery)
        && (mapEvidenceFilter === "ALL" || feature.properties.evidenceState === mapEvidenceFilter));
      for (const feature of features) {
        const p = feature.properties;
        const record: ResearchRecord = { kind: "registry", sourceId: layer.sourceId, featureId: p.fid, title: p.title,
          coordinates: [p.focusLng, p.focusLat], sourceTitle: p.sourceOrganization, sourceUrl: researchSourceUrl(p.citation),
          sourceTime: p.temporalScope, retrievedAt: null, evidenceLabel: p.evidenceState,
          limitation: `${p.generalizationNote || layer.scaleNote} ${p.uncertainty || layer.sensitivityNote}`.trim() || "Registry display anchor, not a surveyed site." };
        if (validResearchRecord(record)) records.push(record);
      }
      coverage.push({ sourceId: layer.id, title: layer.title, state: features.length ? "ready" : "empty", retrievedAt: null,
        limitation: "Only eligible public-safe registry display anchors in the active time and evidence filter. No geometry-edge distance." });
    }
    for (const connection of officialContextConnections.filter(item => item.visible)) {
      const { source, state, activeAtFrame } = connection;
      const manifest = GROUNDWATER_MANIFEST.find(item => item.id === source.id);
      const payload = source.id === "kgs-monitoring-wells" && researchSnapshotPoints && manifest
        ? { feed: source.id, state: "ready", retrievedAt: manifest.retrievedAt, data: researchSnapshotPoints, truncated: false }
        : officialPayloads[source.id as OfficialContextFeedId];
      const eligible = activeAtFrame && (state === "ready" || state === "partial" || state === "empty");
      const points = providerResearchPoints({ id: source.id, title: source.title, url: source.sourceUrl, time: source.freshness, limitation: source.boundary }, payload,
        eligible, officialArchiveDays[source.id as OfficialContextFeedId], properties => officialContextTime(source.id, properties, source.freshness));
      records.push(...points);
      const coverageState: ResearchCoverage["state"] = !activeAtFrame ? "held" : state === "loading" ? "loading" : state === "error" ? "unavailable"
        : !payload ? "not-spatial" : !eligible ? "unavailable" : state === "partial" || payload.truncated ? "partial" : points.length ? "ready" : "empty";
      coverage.push({ sourceId: source.id, title: source.title, state: coverageState, retrievedAt: connection.retrievedAt ?? null,
        limitation: `${points.length} eligible loaded points before radius filtering. ${connection.limitation ?? source.boundary} ${!payload ? "No point inventory available here; raster pixels, polygons and streamed tiles are excluded." : "Invalid or missing point coordinates and identities are excluded. Provider response extent and limits apply; absence does not prove no records exist."}`.slice(0, 2000) });
    }
    if (aviationResearch) {
      // The aviation layer offers its point inventory while shown: public-use airports and METAR stations.
      const points = aviationResearch.filter(validResearchRecord);
      records.push(...points);
      coverage.push({ sourceId: "aviation-context", title: "Airspace, airports & aviation weather", state: points.length ? "ready" : "empty",
        retrievedAt: points.find(point => point.retrievedAt)?.retrievedAt ?? null,
        limitation: `${points.length} public-use airports and weather stations before radius filtering. Airspace volumes and TFR areas are polygons and are excluded, as are private-use facilities and live aircraft; open the aviation layer's point inspector for the airspace at a place.` });
    }
    return { records, coverage };
  }, [aviationResearch, mapEvidenceFilter, officialArchiveDays, officialContextConnections, officialPayloads, researchMissingSources, researchSnapshotPoints, temporalQuery, visibility]);
  const researchCountyOptions = useMemo(() => researchCounties(officialPayloads["census-counties"], officialStates["census-counties"]), [officialPayloads, officialStates]);
  const researchContext = useMemo<ResearchContext | null>(() => {
    if (!researchAnchor) return null;
    const scoped = countyResearch(researchCounty, researchData.records, officialPayloads["census-counties"], officialStates["census-counties"]);
    return { version: 1, anchor: researchAnchor, radiusMiles: nearbyRadiusMiles, mapTime: temporalScopeLabel,
      ...(scoped.county ? { county: scoped.county } : {}),
      capturedAt: new Date().toISOString(), ...nearbyResearch(researchAnchor, scoped.records, nearbyRadiusMiles), coverage: researchData.coverage };
  }, [nearbyRadiusMiles, researchAnchor, researchCounty, researchData, temporalScopeLabel, officialPayloads, officialStates]);
  const researchAnchorAvailable = Boolean(researchAnchor && researchData.records.some(record => researchIdentity(record) === researchIdentity(researchAnchor)));
  const selectedResearchRecord = selected ? researchData.records.find(record => record.kind === "registry"
    ? record.sourceId === selected.layer.sourceId && record.featureId === selected.featureId
    : record.sourceId === officialContextIdForSelection(selected) && (record.featureId === selected.externalFeatureId
      || selected.geometry.id !== undefined && record.featureId === String(selected.geometry.id))) ?? null : null;

  const officialCatalogStatuses = useMemo(() => Object.fromEntries(OFFICIAL_CONTEXT_SOURCES.map(source => {
    const held = officialVisibility[source.id] && (!effectiveOfficialVisibility[source.id]
      || projection === "globe" && (source.kind === "OPERATIONAL_WMS" || source.kind === "HISTORICAL_RASTER"));
    return [source.id, { selected: officialVisibility[source.id], held, state: officialStates[source.id],
      canDisplay: styleReady && !held && view.zoom >= sourceMinimumZoom(source) && officialOpacity[source.id] > 0 }];
  })) as Record<OfficialContextId, CatalogStatus>, [effectiveOfficialVisibility, officialOpacity, officialStates, officialVisibility, projection, styleReady, view.zoom]);
  const starterAccess = useMemo<StarterAccessMap>(() => {
    const requested = Object.fromEntries(OFFICIAL_CONTEXT_SOURCES.map(source => [source.id, true])) as Record<OfficialContextId, boolean>;
    const eligible = officialContextVisibilityForFrame(requested, temporalQuery.frame, buildYearCurrent);
    return Object.fromEntries(OFFICIAL_CONTEXT_SOURCES.map(source => {
      const needsFlatMap = projection === "globe" && (source.kind === "OPERATIONAL_WMS" || source.kind === "HISTORICAL_RASTER");
      return [source.id, { held: !eligible[source.id] || needsFlatMap, unavailable: officialStates[source.id] === "error",
        guidance: !eligible[source.id] ? "Held at this map time; use the timeline to choose a supported time"
          : needsFlatMap ? "Held in Globe; choose the flat map to use this source"
          : view.zoom < sourceMinimumZoom(source) ? `Appears at zoom ${sourceMinimumZoom(source)}+` : undefined }];
    }));
  }, [buildYearCurrent, officialStates, projection, temporalQuery.frame, view.zoom]);
  const filteredOfficialContextConnections = useMemo(() => {
    const query = connectionQuery.trim().toLowerCase();
    return officialContextConnections.filter((connection) => {
      if (connectionFilter === "VISIBLE" && !connection.visible) return false;
      if (connectionFilter === "READY" && connection.state !== "ready" && connection.state !== "partial" && connection.state !== "empty") return false;
      if (connectionFilter === "ERROR" && connection.state !== "error") return false;
      const searchable = `${connection.source.title} ${connection.source.id} ${connection.source.organization} ${connection.source.kind} ${connection.source.endpointLabel}`.toLowerCase();
      return !query || searchable.includes(query);
    });
  }, [connectionFilter, connectionQuery, officialContextConnections]);
  const externalContextConnections = useMemo(() => EXTERNAL_CONTEXT_SOURCES.map((source) => {
    const active = source.activatesWhen.some((activation) => (
      activation === "elevation-3d" ? scenePreset === "elevation-3d" : basemap === activation
    ));
    let state: "READY" | "REQUESTING" | "ERROR" | "NOT_SELECTED" = "NOT_SELECTED";
    if (source.id === "aws-mapzen-terrarium") {
      // Scene effects' 2D shaded relief requests the same display DEM on flat maps.
      const relief2dActive = sceneEffects.relief2d && scenePreset !== "elevation-3d" && projection !== "globe";
      if (relief2dActive && !(active && terrainProvider === "mapzen")) {
        return { source, active: true, state: styleReady && maplibreProbe.tilesLoaded ? "READY" as const : runtime.kind === "error" ? "ERROR" as const : "REQUESTING" as const };
      }
      const mapzenSelected = active && terrainProvider === "mapzen";
      if (mapzenSelected) state = terrainState === "READY" && attachedTerrainProviderRef.current === "mapzen" ? "READY" : terrainState === "ERROR" ? "ERROR" : "REQUESTING";
      return { source, active: mapzenSelected, state };
    } else if (active) {
      state = styleReady && maplibreProbe.tilesLoaded ? "READY" : runtime.kind === "error" ? "ERROR" : "REQUESTING";
    }
    return { source, active, state };
  }), [basemap, maplibreProbe.tilesLoaded, projection, runtime.kind, sceneEffects.relief2d, scenePreset, styleReady, terrainProvider, terrainState]);
  const filteredExternalContextConnections = useMemo(() => {
    const query = connectionQuery.trim().toLowerCase();
    return externalContextConnections.filter((connection) => {
      if (connectionFilter === "VISIBLE" && !connection.active) return false;
      if (connectionFilter === "READY" && connection.state !== "READY") return false;
      if (connectionFilter === "ERROR" && connection.state !== "ERROR") return false;
      const searchable = `${connection.source.title} ${connection.source.id} ${connection.source.organization} ${connection.source.kind} ${connection.source.endpointLabel} ${connection.source.capabilities.join(" ")}`.toLowerCase();
      return !query || searchable.includes(query);
    });
  }, [connectionFilter, connectionQuery, externalContextConnections]);
  const activeExternalContextCount = externalContextConnections.filter((connection) => connection.active).length;
  const maplibreCapabilityChecks = useMemo(() => {
    const state = (ready: boolean, failed = false): "READY" | "CHECKING" | "ERROR" => failed ? "ERROR" : ready ? "READY" : "CHECKING";
    const startupFailed = Boolean(maplibreProbe.error);
    const checkFailed = (...codes: MapRuntimeCheckFailure[]) => codes.some((code) => maplibreProbe.failedChecks.includes(code));
    return [
      {
        id: "module-worker",
        label: "ESM runtime + worker",
        detail: `${maplibreProbe.version ?? "Loading version"} · same-origin worker + shared module ${maplibreProbe.runtimeAssetsReady ? "verified" : "pending"}`,
        state: state(maplibreProbe.version === EXPECTED_MAPLIBRE_VERSION && maplibreProbe.workerConfigured && maplibreProbe.runtimeAssetsReady, startupFailed && !maplibreProbe.workerConfigured),
      },
      {
        id: "webgl2",
        label: "WebGL2 context",
        detail: "Required by MapLibre GL JS 6; catalog metadata remains readable if unavailable",
        state: state(maplibreProbe.webgl2 === true, maplibreProbe.webgl2 === false),
      },
      {
        id: "canvas",
        label: "Map + canvas",
        detail: maplibreProbe.canvasReady ? "Map constructed with a non-zero render surface" : "Waiting for the render surface",
        state: state(maplibreProbe.mapConstructed && maplibreProbe.canvasReady, checkFailed("CANVAS_CHECK_FAILED") || startupFailed && !maplibreProbe.mapConstructed),
      },
      {
        id: "style",
        label: "Style Specification v8",
        detail: `${BASEMAPS[basemap].title} · ${maplibreProbe.styleLoaded ? "style loaded" : "style pending"}`,
        state: state(maplibreProbe.styleLoaded, checkFailed("STYLE_CHECK_FAILED") || startupFailed),
      },
      {
        id: "sources",
        label: "Released map sources",
        detail: `${maplibreProbe.sourcesReady}/${LAYER_REGISTRY.length} GeoJSON sources · ${maplibreProbe.idle ? "idle" : "working"} · ${maplibreProbe.tilesLoaded ? "tiles settled" : "tiles pending"}`,
        state: state(maplibreProbe.sourcesReady === LAYER_REGISTRY.length && maplibreProbe.idle && maplibreProbe.tilesLoaded, checkFailed("SOURCE_CHECK_FAILED", "IDLE_CHECK_FAILED", "TILE_CHECK_FAILED") || startupFailed || sourceStateCounts.error > 0),
      },
      {
        id: "interaction",
        label: "Controls + interactions",
        detail: "Unified KFM dock, scale, pan, zoom, keyboard, hover, selection, cluster expansion, measurement, camera history, and analysis-area handlers",
        state: state(maplibreProbe.controlsReady && maplibreProbe.interactionsReady, checkFailed("INTERACTION_CHECK_FAILED") || startupFailed),
      },
      {
        id: "projection",
        label: "Projection + fallback",
        detail: maplibreProbe.mapConstructed ? `${maplibreProbe.projection} active · Mercator remains the explicit 2D fallback` : "Renderer unavailable · catalog and evidence interfaces remain active",
        state: state(maplibreProbe.mapConstructed, checkFailed("PROJECTION_CHECK_FAILED") || startupFailed),
      },
    ] as const;
  }, [basemap, maplibreProbe, sourceStateCounts.error]);
  const mapFeatureIndex = useMemo(() => {
    const query = mapFeatureQuery.trim().toLowerCase();
    return LAYER_REGISTRY
      .filter((layer) => mapFeatureLayer === "ALL" || layer.id === mapFeatureLayer)
      .filter((layer) => !inspectVisibleLayersOnly || visibility[layer.id])
      .flatMap((layer) => layer.data.features
        .filter((feature) => isFeatureAvailableForTemporalQuery(layer, feature.properties.year, temporalQuery))
        .filter((feature) => mapEvidenceFilter === "ALL" || feature.properties.evidenceState === mapEvidenceFilter)
        .map((feature) => ({ layer, feature })))
      .filter(({ feature }) => !inspectViewportOnly || (
        feature.properties.focusLng >= mapViewportBounds.west
        && feature.properties.focusLng <= mapViewportBounds.east
        && feature.properties.focusLat >= mapViewportBounds.south
        && feature.properties.focusLat <= mapViewportBounds.north
      ))
      .filter(({ layer, feature }) => !query || `${feature.properties.title} ${feature.properties.fid} ${feature.properties.evidenceState} ${layer.title}`.toLowerCase().includes(query));
  }, [inspectViewportOnly, inspectVisibleLayersOnly, mapEvidenceFilter, mapFeatureLayer, mapFeatureQuery, mapViewportBounds, temporalQuery, visibility]);
  const mapCompatibleFeatureCount = useMemo(() => LAYER_REGISTRY.reduce((count, layer) => count + layer.data.features.filter((feature) => (
    isFeatureAvailableForTemporalQuery(layer, feature.properties.year, temporalQuery)
    && (mapEvidenceFilter === "ALL" || feature.properties.evidenceState === mapEvidenceFilter)
  )).length, 0), [mapEvidenceFilter, temporalQuery]);
  const analysisAreaRecordCount = useMemo(() => analysisArea
    ? LAYER_REGISTRY.reduce((count, layer) => count + layer.data.features.filter((feature) => (
      isFeatureAvailableForTemporalQuery(layer, feature.properties.year, temporalQuery)
      && isFeatureInsideBounds(feature.properties, analysisArea)
    )).length, 0)
    : 0, [analysisArea, temporalQuery]);
  const matchesReportRecord = useCallback((layer: LayerRecord, properties: FeatureProperties) => {
    const query = reportQuery.trim().toLowerCase();
    if (!reportLayerIds.includes(layer.id)) return false;
    if (mapEvidenceFilter !== "ALL" && properties.evidenceState !== mapEvidenceFilter) return false;
    if (reportEvidenceFilter !== "ALL" && properties.evidenceState !== reportEvidenceFilter) return false;
    if (query && !`${properties.title} ${properties.fid} ${properties.summary} ${properties.sourceOrganization} ${properties.sourceRole} ${properties.evidenceState} ${layer.title} ${layer.domain}`.toLowerCase().includes(query)) return false;
    if (reportScope === "SELECTION") return selected?.layerId === layer.id && selected.featureId === properties.fid;
    if (reportScope === "VISIBLE_LAYERS" && !visibility[layer.id]) return false;
    if (reportScope === "VIEWPORT" && !(
      properties.focusLng >= mapViewportBounds.west
      && properties.focusLng <= mapViewportBounds.east
      && properties.focusLat >= mapViewportBounds.south
      && properties.focusLat <= mapViewportBounds.north
    )) return false;
    if (reportScope === "ANALYSIS_AREA" && (!analysisArea || !isFeatureInsideBounds(properties, analysisArea))) return false;
    return true;
  }, [analysisArea, mapEvidenceFilter, mapViewportBounds, reportEvidenceFilter, reportLayerIds, reportQuery, reportScope, selected, visibility]);
  const reportRecords = useMemo(() => {
    return LAYER_REGISTRY
      .filter((layer) => reportLayerIds.includes(layer.id))
      .flatMap((layer) => layer.data.features
        .filter((feature) => isFeatureAvailableForTemporalQuery(layer, feature.properties.year, temporalQuery))
        .filter((feature) => matchesReportRecord(layer, feature.properties))
        .map((feature) => ({ layer, properties: feature.properties })))
  }, [matchesReportRecord, reportLayerIds, temporalQuery]);
  const reportEvidenceCounts = useMemo(() => reportRecords.reduce<Record<string, number>>((counts, record) => {
    counts[record.properties.evidenceState] = (counts[record.properties.evidenceState] ?? 0) + 1;
    return counts;
  }, {}), [reportRecords]);
  const reportLayerSummary = useMemo(() => LAYER_REGISTRY
    .filter((layer) => reportLayerIds.includes(layer.id))
    .map((layer) => ({
      id: layer.id,
      title: layer.title,
      domain: layer.domain,
      releaseState: layer.releaseState,
      attribution: layer.attribution,
      recordCount: reportRecords.filter((record) => record.layer.id === layer.id).length,
    }))
    .filter((layer) => layer.recordCount > 0), [reportLayerIds, reportRecords]);
  const reportTemporalComparison = useMemo(() => buildTemporalComparison(
    LAYER_REGISTRY.filter((layer) => reportLayerIds.includes(layer.id)),
    compareTimeA,
    compareTimeB,
    (layer, feature) => matchesReportRecord(layer, feature.properties),
  ), [compareTimeA, compareTimeB, matchesReportRecord, reportLayerIds]);
  const filteredLayerIds = useMemo(() => {
    const query = debouncedLayerQuery.trim().toLowerCase();
    return new Set(LAYER_REGISTRY.filter((layer) => {
      const matchesQuery = !query || `${layer.title} ${layer.description} ${layer.category} ${layer.datasetName} ${layer.domain}`.toLowerCase().includes(query);
      return matchesQuery;
    }).map((layer) => layer.id));
  }, [debouncedLayerQuery]);
  const listedOfficialSources = filterOfficialSources(OFFICIAL_CONTEXT_SOURCES, officialWorkspace, "")
    .filter(source => shownCatalogIds.has(source.id) && catalogFilterMatches(officialCatalogFilter, officialCatalogStatuses[source.id]));
  const searchResults = useMemo(() => atlasDiscoveryResults(globalQuery, debouncedGlobalQuery, SEARCH_INDEX, OFFICIAL_CONTEXT_SOURCES, officialPayloads["census-counties"], officialStates["census-counties"]), [debouncedGlobalQuery, globalQuery, officialPayloads, officialStates]);
  const searchStatus = globalSearchStatus(globalQuery, debouncedGlobalQuery, officialStates["census-counties"], searchResults.length);
  const filteredRepositoryUpdates = useMemo(() => {
    const query = repositoryQuery.trim().toLowerCase();
    return REPOSITORY_UPDATES.filter((update) => {
      const stateMatches = repositoryStateFilter === "ALL" || update.state === repositoryStateFilter;
      const queryMatches = !query || `${update.area} ${update.title} ${update.summary} ${update.boundary} ${update.state}`.toLowerCase().includes(query);
      return stateMatches && queryMatches;
    });
  }, [repositoryQuery, repositoryStateFilter]);
  const filteredSourceCandidates = useMemo(() => {
    const query = sourceQuery.trim().toLowerCase();
    return SOURCE_CANDIDATES.filter((source) => {
      const matchesDomain = sourceDomain === "ALL" || source.domain === sourceDomain;
      const admissionState = SOURCE_ADMISSION_BY_ID[source.id] ?? "candidate";
      const matchesAdmission = sourceAdmissionState === "ALL" || admissionState === sourceAdmissionState;
      const matchesQuery = !query || `${source.title} ${source.organization} ${source.domain} ${source.sourceRole} ${source.value} ${source.nextGate} ${admissionState}`.toLowerCase().includes(query);
      return matchesDomain && matchesAdmission && matchesQuery;
    });
  }, [sourceAdmissionState, sourceDomain, sourceQuery]);
  const sourceAdmissionCounts = useMemo(() => Object.fromEntries(
    SOURCE_ADMISSION_STATES.filter((state) => state !== "ALL").map((state) => [state, SOURCE_CANDIDATES.filter((source) => (SOURCE_ADMISSION_BY_ID[source.id] ?? "candidate") === state).length]),
  ) as Record<SourceAdmissionState, number>, []);
  const filteredFunctions = useMemo(() => {
    const query = functionQuery.trim().toLowerCase();
    return functionsForGroup(functionGroup).filter((record) => (functionTopic === "all" || functionTopics(record.id).includes(functionTopic)) && (!query || `${record.title} ${record.summary} ${record.interface} ${record.boundary} ${record.authority} ${record.maturity} ${record.inventory} ${record.sourceLabel} ${topicSearchText(functionTopics(record.id))}`.toLowerCase().includes(query)));
  }, [functionGroup, functionQuery, functionTopic]);
  const activeFunction = FUNCTION_REGISTRY.find((record) => record.id === activeFunctionId && record.group === functionGroup) ?? filteredFunctions[0] ?? functionsForGroup(functionGroup)[0];
  const functionCounts = useMemo(() => Object.fromEntries(["ACTIVE", "BOUNDED", "DOCUMENTED", "GATED"].map((state) => [state, FUNCTION_REGISTRY.filter((record) => record.state === state).length])), []);
  const filteredFeatures = useMemo(() => {
    const query = featureQuery.trim().toLowerCase();
    return FEATURE_CATALOG.filter((feature) => {
      if (featureTopic !== "all" && !featureTopics(feature.id).includes(featureTopic)) return false;
      if (featureArea !== "ALL" && feature.area !== featureArea) return false;
      if (featureMaturity !== "ALL" && feature.maturity !== featureMaturity) return false;
      return !query || `${feature.name} ${feature.area} ${feature.maturity} ${feature.summary} ${feature.path} ${feature.keywords.join(" ")} ${topicSearchText(featureTopics(feature.id))}`.toLowerCase().includes(query);
    });
  }, [featureArea, featureMaturity, featureQuery, featureTopic]);
  const featureMaturityCounts = useMemo(() => Object.fromEntries(
    (["VERIFIED_SLICE", "FIXTURE_FIRST", "DOCUMENTED", "HOLD"] as const)
      .map((maturity) => [maturity, FEATURE_CATALOG.filter((feature) => feature.maturity === maturity).length]),
  ), []);
  const activeTransition = TRANSITION_BOUNDARIES.find((transition) => transition.id === activeTransitionId) ?? TRANSITION_BOUNDARIES[0];
  const governedRouteResult = useMemo(() => inspectGovernedRoute(governedMethod, governedRoute), [governedMethod, governedRoute]);
  const planningScenarioReview = PLANNING_SCENARIO_REVIEWS[scenarioReviewMode];

  const selectedOfficialConnection = officialContextConnections.find((connection) => connection.source.id === selectedOfficialContextId);
  const selectedOfficialPayload = selectedOfficialContextId ? officialPayloads[selectedOfficialContextId as OfficialContextFeedId] : undefined;
  const selectedRiverObservation = useMemo(() => selectedOfficialContextId === "usgs-streamflow"
    ? riverDrawerObservation(selected?.externalStationId ?? null, streamflowBundle, streamflowFrame, streamflowFrameTime, streamflowDisplayState)
    : null, [selectedOfficialContextId, selected?.externalStationId, streamflowBundle, streamflowFrame, streamflowFrameTime, streamflowDisplayState]);
  // The drawer asks the same three questions of every selection; this only restates its own fields.
  const selectedSummary = useMemo(() => selected ? evidenceSummary({ ...selected.properties, kind: selected.kind, officialId: selectedOfficialContextId,
    layerDomain: selected.layer.domain, observedAt: selectedRiverObservation?.observedAt ?? null }) : null, [selected, selectedOfficialContextId, selectedRiverObservation]);
  const selectedOfficialFeature = selected?.externalFeatureId && selectedOfficialPayload?.data.features.find((feature) =>
    feature.properties?.featureId === selected.externalFeatureId
    && (selectedOfficialContextId !== CIVIC_ID || (
      civicRecordMatchesDay(selected.civicRecord, civicFrameDay)
      && civicRecordMatchesDay(feature.properties, civicFrameDay)
      && (selectedOfficialPayload.sourceDay === civicFrameDay || selectedOfficialPayload.sourceDay === undefined && selected.civicRecord?.congressNumber === 119)
    )));
  const selectedFireComparisonId = selectedOfficialContextId === "nifc-fire-reports" ? "nasa-gibs-fire-points" : selectedOfficialContextId === "nasa-gibs-fire-points" ? "nifc-fire-reports" : null;
  const selectedFireComparisonPayload = selectedFireComparisonId ? officialPayloads[selectedFireComparisonId] : undefined;
  const selectedFireNeighbors = selectedFireComparisonId && selectedOfficialFeature && selectedFireComparisonPayload
    ? nearbyFireContext(selectedOfficialFeature, selectedFireComparisonPayload.data.features, selectedFireComparisonId === "nifc-fire-reports" ? "discoveryAt" : "acquiredAt") : [];
  const selectedArtifactAttributes = selected?.kind === "registry"
    ? drawerArtifactAttributes("registry", selected.properties)
    : selectedOfficialContextId && selectedOfficialFeature
      ? drawerArtifactAttributes(selectedOfficialContextId, selectedOfficialFeature.properties)
      : selected?.externalAttributes ?? [];
  const selectedAttributesCurrent = Boolean(selectedOfficialFeature);
  const selectedProviderReport = buildProviderReportSelection({
    selected, timeMismatch: selectedTimeMismatch,
    locationPrivate: locationCameraRedacted || locationDerivedViewRef.current || researchLocationRedacted || subsurfacePrivate,
    source: selectedOfficialConnection?.source, attributes: selectedArtifactAttributes, attributesCurrent: selectedAttributesCurrent,
    sourceState: selectedRiverObservation?.status ?? selectedOfficialConnection?.state, sourceUrl: selectedRiverObservation?.sourceUrl,
    observedAt: selectedRiverObservation?.observedAt, providerUpdatedAt: selectedOfficialPayload?.upstreamUpdatedAt,
    retrievedAt: selectedRiverObservation?.retrievedAt ?? selectedOfficialConnection?.retrievedAt,
    limitation: selectedOfficialPayload?.limitation ?? selectedOfficialConnection?.limitation,
  });
  const reportFindings = useMemo(() => {
    if (reportRecords.length === 0) return emptyReportFindings(selectedProviderReport?.status ?? null, LAYER_REGISTRY.length === 0);
    const supported = (reportEvidenceCounts.ANSWER ?? 0) + (reportEvidenceCounts.CORRECTED ?? 0);
    const bounded = reportRecords.length - supported;
    const mostRepresented = [...reportLayerSummary].sort((left, right) => right.recordCount - left.recordCount)[0];
    return [
      `${reportRecords.length} record${reportRecords.length === 1 ? "" : "s"} match the ${reportScope === "VIEWPORT" ? "current map extent" : reportScope === "ANALYSIS_AREA" ? "locked area-of-interest" : reportScope === "VISIBLE_LAYERS" ? "visible-layer" : "selected-feature"} scope for ${temporalScopeLabel}.`,
      `${supported} record${supported === 1 ? "" : "s"} carry supported or corrected evidence states; ${bounded} remain generalized, missing, stale, restricted, denied, superseded, or error states.`,
      mostRepresented
        ? `${mostRepresented.title} contributes the largest share of this report (${mostRepresented.recordCount} record${mostRepresented.recordCount === 1 ? "" : "s"}).`
        : "No records match the current report filters; widen the map, change time, or include another layer.",
      `${reportTemporalComparison.changedLayerCount} included layer${reportTemporalComparison.changedLayerCount === 1 ? " changes" : "s change"} catalog availability between ${formatTimelineStep(compareTimeA)} and ${formatTimelineStep(compareTimeB)}. This is fixture availability under declared temporal rules, not observed change or imagery analysis.`,
    ];
  }, [compareTimeA, compareTimeB, reportEvidenceCounts, reportLayerSummary, reportRecords.length, reportScope, reportTemporalComparison.changedLayerCount, temporalScopeLabel, selectedProviderReport?.status]);
  const providerReportTitle = selectedProviderReport?.status === "WITHHELD" ? "Withheld source-context report" : reportTitle;
  const selectedFireSourceDay = selectedOfficialContextId === "nasa-gibs-fire-points"
    ? selectedArtifactAttributes.find((attribute) => ["Detection source day · UTC", "NASA image day · UTC"].includes(attribute.label))?.value
    : undefined;
  const selectedDischargeHistory = useMemo(() => streamflowBundle && selectedOfficialContextId === "usgs-streamflow" && selected?.externalStationId
    ? streamflowBundle.observations.filter((item) => item.stationId === selected.externalStationId).slice(-8).reverse()
    : [], [selected?.externalStationId, selectedOfficialContextId, streamflowBundle]);
  const latestLoadedDischarge = useMemo(() => streamflowBundle && selectedOfficialContextId === "usgs-streamflow" && selected?.externalStationId
    ? streamflowBundle.observations.findLast((item) => item.stationId === selected.externalStationId && item.value !== null)
    : null, [selected?.externalStationId, selectedOfficialContextId, streamflowBundle]);
  const selectedStageDetail = stageDrawerLoad?.stationId === selected?.externalStationId ? stageDrawerLoad : null;
  useEffect(() => {
    const stationId = selectedOfficialContextId === "usgs-streamflow" && rightOpen ? selected?.externalStationId : null;
    if (!stationId) return;
    const controller = new AbortController();
    setStageDrawerLoad({ stationId, status: "loading" });
    const load = async () => {
      try {
        const path = `/api/hydrology/streamflow?mode=station&range=7d&station=${encodeURIComponent(stationId)}&parameter=00065&resolution=continuous`;
        const response = await fetch(path, { cache: "no-store", headers: { Accept: "application/json" }, signal: controller.signal });
        if (!response.ok) throw new Error(`USGS gauge-height request returned HTTP ${response.status}.`);
        const detail = parseUsgsStageDetail(await readBoundedJson(response, 8 * 1024 * 1024), stationId);
        if (!controller.signal.aborted) setStageDrawerLoad({ stationId, status: "ready", detail });
      } catch {
        if (!controller.signal.aborted) setStageDrawerLoad({ stationId, status: "error" });
      }
    };
    void load();
    return () => controller.abort();
  }, [rightOpen, selected?.externalStationId, selectedOfficialContextId]);
  const selectedLabel = selected?.properties.title ?? "Statewide Kansas";
  const selectedEvidence = selected ? evidenceLabels[selected.properties.evidenceState] : null;
  const selectedLayerHidden = Boolean(selected && !selectionCarrierIsVisible(selected, visibility, effectiveOfficialVisibility));
  const selectedEvidenceFiltered = Boolean(selected && !selectionPassesEvidenceFilter(selected, mapEvidenceFilter));
  const activeFocus = focusResultForState(selected?.properties.evidenceState ?? "MISSING_EVIDENCE", selectedTimeMismatch);
  const focusGates = useMemo(() => buildFocusGateTrace({
    state: selected?.properties.evidenceState ?? "MISSING_EVIDENCE",
    timeMismatch: selectedTimeMismatch,
    temporal: selected?.layer.temporal,
    featureYear: selected?.properties.year ?? year,
    activeYear: year,
    releaseState: selected?.properties.releaseState ?? "DEMONSTRATION",
    correctionState: selected?.properties.correctionState ?? "NONE",
  }), [selected, selectedTimeMismatch, year]);
  const focusProposals = useMemo(() => buildFocusActionProposals({
    state: selected?.properties.evidenceState ?? "MISSING_EVIDENCE",
    timeMismatch: selectedTimeMismatch,
    activeYear: year,
    featureYear: selected?.properties.year ?? year,
    currentCenter: view.center,
    focusCenter: selected ? [selected.properties.focusLng, selected.properties.focusLat] : view.center,
  }), [selected, selectedTimeMismatch, view.center, year]);
  const focusNarrative = useMemo(() => focusIntentNarrative({
    intent: focusIntent,
    result: activeFocus,
    state: selected?.properties.evidenceState ?? "MISSING_EVIDENCE",
    timeMismatch: selectedTimeMismatch,
    activeYear: year,
    featureYear: selected?.properties.year ?? year,
    citation: selected?.properties.citation ?? "no-evidence-ref",
  }), [activeFocus, focusIntent, selected, selectedTimeMismatch, year]);

  const buildExportReview = useCallback((exportedAt: string) => buildPublicSafeExport({
    exportedAt,
    locationCameraRedacted: locationCameraRedacted || locationDerivedViewRef.current,
    view,
    projection,
    basemap,
    layerOrder,
    temporalSweep: {
      mode: temporalMode,
      frame: temporalQuery.frame,
      rangeStart: temporalQuery.rangeStart,
      rangeEnd: temporalQuery.rangeEnd,
      windowStart: temporalQuery.windowStart,
      stepRule: temporalStepRule,
      interpolation: false,
    },
    workspace: currentWorkspace,
    layers: activeLayers.map((layer) => ({
      id: layer.id,
      title: layer.title,
      opacity: opacity[layer.id] ?? layer.defaultOpacity,
      attribution: layer.attribution,
      releaseState: layer.releaseState,
      generalization: layer.sensitivityNote,
      correction: layer.correctionNote,
    })),
    selection: selected && !selectedTimeMismatch ? {
      featureId: selected.featureId,
      title: selected.properties.title,
      layerId: selected.layerId,
      evidenceState: selected.properties.evidenceState,
      evidenceReference: selected.properties.citation,
      temporalScope: selected.properties.temporalScope,
      sourceYear: selected.properties.year,
      temporalMode: selected.layer.temporal?.mode ?? "untimed",
      sourceTime: selected.layer.sourceTime,
      releaseTime: selected.layer.releaseTime,
      lastUpdate: selected.properties.lastUpdate,
      reviewState: selected.properties.reviewState,
      releaseState: selected.properties.releaseState,
      correctionState: selected.properties.correctionState,
      geometry: selected.geometry.geometry,
      generalization: selected.properties.generalizationNote,
    } : null,
  }), [activeLayers, basemap, currentWorkspace, layerOrder, locationCameraRedacted, opacity, projection, selected, selectedTimeMismatch, temporalMode, temporalQuery, temporalStepRule, view]);
  const exportReview = useMemo(() => buildExportReview(exportGeneratedAt), [buildExportReview, exportGeneratedAt]);

  const buildExplorerParams = useCallback(() => {
    const params = new URLSearchParams();
    serializeTopicSelection(params, officialWorkspace, layerCatalogView);
    const redactLocationCamera = locationCameraRedacted || locationDerivedViewRef.current;
    const serializedView = redactLocationCamera ? KANSAS_VIEW : view;
    params.set("c", `${serializedView.center[0].toFixed(5)},${serializedView.center[1].toFixed(5)}`);
    params.set("z", serializedView.zoom.toFixed(2));
    if (Math.abs(serializedView.bearing) > 0.1) params.set("b", serializedView.bearing.toFixed(1));
    if (serializedView.pitch > 0.1) params.set("p", serializedView.pitch.toFixed(1));
    if (redactLocationCamera) params.set("privacy", "location-camera-redacted");
    params.set("l", activeLayers.map((layer) => layer.id).join(","));
    params.set("o", LAYER_REGISTRY.map((layer) => `${layer.id}:${(opacity[layer.id] ?? layer.defaultOpacity).toFixed(2)}`).join(","));
    params.set("ctx", visibleOfficialSources.map((source) => source.id).join(","));
    params.set("ctxd", Object.entries(officialArchiveDays).filter(([, day]) => day).map(([feed, day]) => `${feed}:${day}`).join(","));
    params.set("ctxo", OFFICIAL_CONTEXT_SOURCES.map((source) => `${source.id}:${(officialOpacity[source.id] ?? source.defaultOpacity).toFixed(2)}`).join(","));
    serializeSoilMapState(params, soilMapState);
    if (populationPrisms) params.set("prisms", "on");
    if (quakeRecordOn) params.set("quakes", "record");
    if (outlookDay) params.set("outlook", String(outlookDay));
    if (outlookDay && outlookHazard !== "cat") params.set("outlookHazard", outlookHazard);
    if (reportsDay) params.set("reports", reportsDay);
    if (droughtOn) params.set("drought", droughtWeek ?? "newest");
    params.set("sunDay", daylightDay);
    params.set("sunThrough", daylightThroughDay);
    params.set("sunAt", new Date(daylightInstant).toISOString());
    if (daylightEnabled) params.set("sun", "on");
    if (officialVisibility["nws-radar"] && noaaRadarFrameTime) {
      params.set("radarTime", noaaRadarFrameTime);
      params.set("radarSpan", String(noaaRadarLoopSpan));
      params.set("radarSpeed", String(noaaRadarPlaybackSpeed));
      params.set("radarFollow", noaaRadarFollowLatest ? "latest" : "selected");
    }
    params.set("hydroRange", streamflowRange);
    params.set("hydroSpeed", String(streamflowPlaybackSpeed));
    if (streamflowFrameTime) params.set("hydroTime", streamflowFrameTime);
    if (streamflowSelectedStationId) params.set("hydroStation", streamflowSelectedStationId);
    if (streamflowArchiveDay) params.set("hydroDay", streamflowArchiveDay);
    if (officialVisibility["usgs-streamflow"] || officialVisibility["nws-radar"] || officialVisibility["noaa-lightning-density"]) params.set("live", liveInstrument);
    if (calendarSweep) params.set("calendar", JSON.stringify(calendarSweep));
    params.set("t", String(year));
    params.set("tm", temporalMode);
    params.set("tstep", temporalStepRule);
    params.set("trange", `${sweepRangeStart},${sweepRangeEnd}`);
    params.set("twindow", String(movingWindowFrames));
    params.set("tdir", playbackDirection);
    params.set("tloop", playbackLoopMode);
    params.set("motion", dynamicEffects ? "on" : "off");
    if (mapEvidenceFilter !== "ALL") params.set("ef", mapEvidenceFilter);
    params.set("base", basemap);
    params.set("proj", projection);
    params.set("scene", scenePreset);
    params.set("zscale", verticalExaggeration.toFixed(1));
    params.set("sky", atmospherePreset);
    params.set("light", String(Math.round(lightAzimuth)));
    params.set("fov", fieldOfView.toFixed(1));
    params.set("gestures", gestureMode);
    params.set("order", layerOrder.join(","));
    params.set("units", measureUnit);
    params.set("ws", currentWorkspace);
    if (analysisArea && !redactLocationCamera) {
      params.set("aoi", [analysisArea.west, analysisArea.south, analysisArea.east, analysisArea.north].map((value) => value.toFixed(5)).join(","));
    }
    if (mapUtilityOpen) {
      params.set("mapui", "open");
      params.set("maptab", mapUtilityView);
    }
    if (sourceStatusOpen && leftOpen) params.set("layers", "sources");
    params.set("times", `${compareTimeA},${compareTimeB}`);
    if (selected) {
      params.set("f", selected.featureId);
      params.set("panel", drawerView);
      params.set("drawer", rightOpen ? "open" : "closed");
      params.set("focusStage", focusStage);
      params.set("focusIntent", focusIntent);
    }
    return params;
  }, [calendarSweep, officialWorkspace, layerCatalogView, soilMapState, populationPrisms, quakeRecordOn, outlookDay, outlookHazard, reportsDay, droughtOn, droughtWeek, activeLayers, analysisArea, atmospherePreset, basemap, compareTimeA, compareTimeB, currentWorkspace, daylightDay, daylightEnabled, daylightInstant, daylightThroughDay, drawerView, dynamicEffects, fieldOfView, focusIntent, focusStage, gestureMode, layerOrder, lightAzimuth, liveInstrument, locationCameraRedacted, mapEvidenceFilter, mapUtilityOpen, mapUtilityView, leftOpen, sourceStatusOpen, measureUnit, movingWindowFrames, noaaRadarFollowLatest, noaaRadarFrameTime, noaaRadarLoopSpan, noaaRadarPlaybackSpeed, officialArchiveDays, officialOpacity, officialVisibility, opacity, playbackDirection, playbackLoopMode, projection, rightOpen, scenePreset, selected, streamflowArchiveDay, streamflowFrameTime, streamflowPlaybackSpeed, streamflowRange, streamflowSelectedStationId, sweepRangeEnd, sweepRangeStart, temporalMode, temporalStepRule, verticalExaggeration, view, visibleOfficialSources, year]);

  const announce = useCallback((message: string) => {
    setToast(message);
    window.setTimeout(() => setToast(""), 3600);
  }, []);

  const setDaylightPlayback = useCallback((playing: boolean) => {
    daylightPlayingRef.current = playing;
    setDaylightPlaying(playing);
  }, []);

  const selectDaylightRange = useCallback((fromDay: string, throughDay: string) => {
    if (!fromDay || !throughDay) return;
    try {
      const today = currentKansasCalendarDay();
      if (fromDay > today || throughDay > today || throughDay < fromDay) throw new RangeError("Invalid Kansas date range.");
      const interval = kansasLocalDateRangeInterval(fromDay, throughDay);
      daylightDayRef.current = fromDay;
      daylightThroughDayRef.current = throughDay;
      daylightInstantRef.current = interval.startMs;
      daylightEnabledRef.current = true;
      setDaylightDay(fromDay);
      setDaylightThroughDay(throughDay);
      setDaylightInstant(interval.startMs);
      setDaylightEnabled(true);
      const shouldPlay = daylightShouldAutoplay(reducedMotion, document.hidden);
      setDaylightPlayback(shouldPlay);
      if (mapRef.current && styleGenerationReadyRef.current) setDaylightMapLayer(mapRef.current, true, interval.startMs);
    } catch {
      announce("Choose a valid Kansas Central date range through today");
    }
  }, [announce, reducedMotion, setDaylightPlayback]);

  const selectDaylightStart = useCallback((day: string) => {
    const throughDay = daylightThroughDayRef.current;
    selectDaylightRange(day, throughDay < day ? day : throughDay);
  }, [selectDaylightRange]);

  const selectDaylightThrough = useCallback((day: string) => {
    const fromDay = daylightDayRef.current;
    selectDaylightRange(day < fromDay ? day : fromDay, day);
  }, [selectDaylightRange]);

  const toggleDaylightVisibility = useCallback((enabled: boolean) => {
    daylightEnabledRef.current = enabled;
    setDaylightEnabled(enabled);
    if (!enabled || document.hidden) setDaylightPlayback(false);
    if (mapRef.current && styleGenerationReadyRef.current) {
      setDaylightMapLayer(mapRef.current, enabled, daylightInstantRef.current);
    }
  }, [setDaylightPlayback]);

  const seekDaylight = useCallback((fraction: number) => {
    const interval = kansasLocalDateRangeInterval(daylightDayRef.current, daylightThroughDayRef.current);
    const instant = instantAtIntervalFraction(interval, Math.min(fraction, 0.9999999));
    daylightInstantRef.current = instant;
    setDaylightPlayback(false);
    setDaylightInstant(instant);
    if (mapRef.current && styleGenerationReadyRef.current && daylightEnabledRef.current) {
      setDaylightMapLayer(mapRef.current, true, instant);
    }
  }, [setDaylightPlayback]);

  const commitTemporalFrame = useCallback((next: number, message?: string, keepCalendar = false) => {
    if (officialContextIdForSelection(selectedRef.current) === CIVIC_ID) {
      selectedRef.current = null; setSelected(null); setRightOpen(false);
      if (mapRef.current?.isStyleLoaded()) updateSelectionSource(mapRef.current, null);
    }
    if (!keepCalendar) {
      cancelSmokePlayback();
      calendarSeekGeneration.current++;
      calendarSweepRef.current = null;
      setCalendarSweep(null);
      // Annual controls leave dated-source mode, even when the year stays the
      // same. Retire hidden archives too, before Present can expose them.
      const retired = (Object.keys(CALENDAR_ARCHIVE_BOUNDS) as CalendarArchiveFeed[])
        .filter(feed => officialArchiveDaysRef.current[feed] || calendarArchiveLoads.current.has(feed));
      for (const feed of retired) {
        officialRequestsRef.current.get(feed)?.abort();
        officialRequestsRef.current.delete(feed);
        calendarArchiveLoads.current.delete(feed);
        officialArchiveDaysRef.current = { ...officialArchiveDaysRef.current, [feed]: undefined };
        officialArchivePayloadsRef.current = { ...officialArchivePayloadsRef.current, [feed]: undefined };
        officialPayloadsRef.current = { ...officialPayloadsRef.current, [feed]: undefined };
        setOfficialStates(current => ({ ...current, [feed]: "idle" }));
        setOfficialErrors(current => ({ ...current, [feed]: undefined }));
        setOfficialReadPhases(current => ({ ...current, [feed]: undefined }));
      }
      if (retired.length) {
        setOfficialArchiveDays(officialArchiveDaysRef.current);
        setOfficialPayloads(officialPayloadsRef.current);
        setEarthquakeArchiveFrameIndex(-1);
        setSmokeArchiveFrameIndex(-1);
        const selectedFeed = officialContextIdForSelection(selectedRef.current);
        const clearSelection = selectedFeed !== null && retired.includes(selectedFeed as CalendarArchiveFeed);
        if (clearSelection) { selectedRef.current = null; setSelected(null); setRightOpen(false); }
        const map = mapRef.current;
        if (map && styleGenerationReadyRef.current) runMapMutation("Leave dated calendar sources", () => {
          for (const feed of retired) clearOfficialContextFeed(map, feed);
          if (clearSelection) updateSelectionSource(map, null);
        });
      }
    }
    setSweepRangeStart((current) => Math.min(current, next));
    setSweepRangeEnd((current) => Math.max(current, next));
    yearRef.current = next;
    setYear(next);
    setPreviewYear(next);
    if (temporalMode === "comparison") setCompareTimeB(next);
    if (message) announce(message);
  }, [announce, cancelSmokePlayback, runMapMutation, setRightOpen, temporalMode]);

  const stepTemporalSweep = useCallback((direction: TemporalPlaybackDirection) => {
    const next = nextTemporalFrame(temporalSequence, year, direction, "stop");
    if (next === null) {
      setPlaying(false);
      announce(`Reached the ${direction === "forward" ? "end" : "start"} of the selected sweep range`);
      return;
    }
    setPlaying(false);
    commitTemporalFrame(next, `Committed ${formatTimelineStep(next)}; map, evidence, report, and story context moved together`);
  }, [announce, commitTemporalFrame, temporalSequence, year]);

  const toggleTemporalPlayback = useCallback(() => {
    if (playing) {
      setPlaying(false);
      announce("Time sweep paused");
      return;
    }
    if (reducedMotion) {
      announce("Automatic sweep is off for reduced motion; use previous and next frame controls");
      return;
    }
    if (temporalMode === "snapshot" || temporalMode === "comparison") return;
    const next = nextTemporalFrame(temporalSequence, year, playbackDirection, playbackLoopMode);
    if (next === null) {
      const restart = temporalSequence[playbackDirection === "forward" ? 0 : temporalSequence.length - 1];
      if (restart !== undefined) commitTemporalFrame(restart);
    }
    setPlaying(true);
    announce(`Time sweep started ${playbackDirection}; ${temporalSequence.length} bounded frame${temporalSequence.length === 1 ? "" : "s"}`);
  }, [announce, commitTemporalFrame, playbackDirection, playbackLoopMode, playing, reducedMotion, temporalMode, temporalSequence, year]);

  const applyNoaaRadarFrame = useCallback((observedAt: string, announceChange = false) => {
    const currentManifest = noaaRadarManifestRef.current;
    if (!currentManifest?.frames.includes(observedAt) || !noaaRadarManifestIsFresh(currentManifest, Date.now())) {
      noaaRadarReadyRef.current = false;
      noaaRadarPendingFrameTimeRef.current = null;
      setNoaaRadarPendingFrameTime(null);
      setNoaaRadarPlaying(false);
      setNoaaRadarFrameLoadState("error");
      setOfficialStates((current) => ({ ...current, "nws-radar": "error" }));
      setOfficialErrors((current) => ({ ...current, "nws-radar": "The requested observation is not in a fresh NOAA frame manifest; radar remains withheld." }));
      const map = mapRef.current;
      if (map && styleGenerationReadyRef.current) applyOfficialContextState(
        map,
        runtimeOfficialVisibility(officialVisibilityRef.current, temporalQueryRef.current.frame, false, null),
        officialOpacityRef.current,
        officialPayloadsRef.current,
      );
      return;
    }
    const previousConfirmedFrame = noaaRadarFrameTimeRef.current;
    const currentMap = mapRef.current;
    // An unchanged manifest must not restage the confirmed scan into the other
    // buffer. Style replacement still reloads it because the source is gone.
    if (previousConfirmedFrame === observedAt && noaaRadarReadyRef.current
      && !noaaRadarPendingFrameTimeRef.current && currentMap && styleGenerationReadyRef.current
      && noaaRadarObservationTimeIsApplied(currentMap, observedAt)) {
      setNoaaRadarFrameLoadState("ready");
      setOfficialStates(current => current["nws-radar"] === "ready" ? current : { ...current, "nws-radar": "ready" });
      setOfficialErrors(current => current["nws-radar"] ? { ...current, "nws-radar": undefined } : current);
      return;
    }
    noaaRadarPendingFrameTimeRef.current = observedAt;
    setNoaaRadarPendingFrameTime(observedAt);
    noaaRadarFrameLoadCleanupRef.current?.();
    noaaRadarFrameLoadCleanupRef.current = null;
    noaaRadarFrameFailureRef.current = null;
    const map = mapRef.current;
    if (!map || !styleGenerationReadyRef.current) {
      setNoaaRadarFrameLoadState("idle");
      return;
    }
    try {
      setNoaaRadarFrameLoadState("loading");
      setOfficialStates((current) => ({ ...current, "nws-radar": "loading" }));
      let settled = false;
      let timeout = 0;
      let stagedSourceId = "";
      const onSourceData = (event: MapSourceDataEvent) => {
        if (event.sourceId !== stagedSourceId || !event.isSourceLoaded || !map.isSourceLoaded(stagedSourceId)) return;
        if (!noaaRadarObservationTimeIsApplied(map, observedAt)) return;
        if (!noaaRadarManifestRef.current?.frames.includes(observedAt) || !noaaRadarManifestIsFresh(noaaRadarManifestRef.current, Date.now())) {
          finish("error", "The NOAA frame manifest became stale before the requested image settled.");
          return;
        }
        finish("ready");
      };
      const finish = (state: "ready" | "error", failureMessage = "The selected NOAA frame did not finish loading.") => {
        if (settled) return;
        settled = true;
        map.off("sourcedata", onSourceData);
        window.clearTimeout(timeout);
        noaaRadarFrameLoadCleanupRef.current = null;
        noaaRadarFrameFailureRef.current = null;
        if (noaaRadarPendingFrameTimeRef.current === observedAt) {
          noaaRadarPendingFrameTimeRef.current = null;
          setNoaaRadarPendingFrameTime(null);
        }
        setNoaaRadarFrameLoadState(state);
        recordStormDeskFrame(state === "ready" ? "confirmed" : "failed", observedAt);
        if (state === "ready") {
          commitNoaaRadarObservationTime(map, stagedSourceId, officialVisibilityRef.current["nws-radar"], officialOpacityRef.current["nws-radar"]);
          noaaRadarFrameTimeRef.current = observedAt;
          noaaRadarReadyRef.current = true;
          setNoaaRadarFrameTime(observedAt);
          setOfficialStates((current) => ({ ...current, "nws-radar": "ready" }));
          setOfficialErrors((current) => ({ ...current, "nws-radar": undefined }));
          applyOfficialContextState(
            map,
            runtimeOfficialVisibility(officialVisibilityRef.current, temporalQueryRef.current.frame, noaaRadarReadyRef.current, observedAt),
            officialOpacityRef.current,
            officialPayloadsRef.current,
          );
          if (announceChange) announce(`NOAA radar frame ${formatNoaaRadarLocalTime(observedAt)} selected; no interpolation`);
        } else {
          setNoaaRadarPlaying(false);
          noaaRadarReadyRef.current = Boolean(previousConfirmedFrame);
          discardNoaaRadarStagedFrame(map, stagedSourceId);
          applyOfficialContextState(
            map,
            runtimeOfficialVisibility(officialVisibilityRef.current, temporalQueryRef.current.frame, noaaRadarReadyRef.current, previousConfirmedFrame),
            officialOpacityRef.current,
            officialPayloadsRef.current,
          );
          setOfficialStates((current) => ({ ...current, "nws-radar": "error" }));
          setOfficialErrors((current) => ({ ...current, "nws-radar": `${failureMessage} Playback is paused${previousConfirmedFrame ? " on the last confirmed observation" : " and radar is withheld"}.` }));
        }
      };
      map.on("sourcedata", onSourceData);
      noaaRadarFrameFailureRef.current = (message) => finish("error", message);
      timeout = window.setTimeout(() => finish("error"), 12_000);
      noaaRadarFrameLoadCleanupRef.current = () => {
        if (settled) return;
        settled = true;
        map.off("sourcedata", onSourceData);
        window.clearTimeout(timeout);
        noaaRadarFrameFailureRef.current = null;
      };
      const sourceUpdate = previousConfirmedFrame ? "changed" : setNoaaRadarObservationTime(map, observedAt);
      stagedSourceId = previousConfirmedFrame ? stageNoaaRadarObservationTime(map, observedAt) : OFFICIAL_CONTEXT_BY_ID["nws-radar"].sourceId;
      recordStormDeskFrame("stage", observedAt);
      if (sourceUpdate === null) throw new Error("The fixed NOAA raster source could not be initialized.");
      if (previousConfirmedFrame || !officialVisibilityRef.current["nws-radar"] || temporalQueryRef.current.frame !== OFFICIAL_CONTEXT_PRESENT_FRAME) {
        applyOfficialContextState(
          map,
          runtimeOfficialVisibility(officialVisibilityRef.current, temporalQueryRef.current.frame, noaaRadarReadyRef.current, previousConfirmedFrame),
          officialOpacityRef.current,
          officialPayloadsRef.current,
        );
      }
      if ((sourceUpdate === "unchanged" && previousConfirmedFrame === observedAt) || map.isSourceLoaded(stagedSourceId)) window.requestAnimationFrame(() => finish("ready"));
    } catch (error) {
      noaaRadarFrameFailureRef.current?.(error instanceof Error ? error.message : "The NOAA radar frame could not be applied.");
    }
  }, [announce, runtimeOfficialVisibility]);

  const refreshNoaaRadarManifest = useCallback(async (quiet = false) => {
    if (document.hidden || !officialVisibilityRef.current["nws-radar"]) return;
    if (!buildYearCurrentRef.current) {
      noaaRadarReadyRef.current = false;
      setNoaaRadarPlaying(false);
      if (!quiet) announce("This site build does not match the UTC year; rebuild before refreshing current radar");
      return;
    }
    if (yearRef.current !== OFFICIAL_CONTEXT_PRESENT_FRAME) {
      noaaRadarReadyRef.current = false;
      setNoaaRadarPlaying(false);
      if (!quiet) announce(`NOAA radar remains held outside ${formatTimelineStep(OFFICIAL_CONTEXT_PRESENT_FRAME)}; switch to Present before refreshing frames`);
      return;
    }
    if (noaaRadarRequestRef.current) return;
    const requestStartedAt = Date.now();
    if (requestStartedAt - noaaRadarLastRequestAtRef.current < 60_000) {
      if (!quiet) announce("NOAA radar frames were checked less than a minute ago; the bounded retry window is still active");
      return;
    }
    noaaRadarLastRequestAtRef.current = requestStartedAt;
    const controller = new AbortController();
    noaaRadarRequestRef.current = controller;
    const firstLoad = !noaaRadarFrameTimeRef.current;
    if (firstLoad) {
      setNoaaRadarManifestState("loading");
      setOfficialStates((current) => ({ ...current, "nws-radar": "loading" }));
    }
    setNoaaRadarManifestError("");
    setOfficialErrors((current) => ({ ...current, "nws-radar": undefined }));
    try {
      const response = await fetch(NOAA_RADAR_FRAME_API_PATH, { cache: "no-store", signal: controller.signal, headers: { Accept: "application/json" } });
      const candidate = await readBoundedJson(response, 512 * 1024) as unknown;
      if (controller.signal.aborted) return;
      if (!response.ok || !isNoaaRadarManifest(candidate)) throw new Error("The fixed NOAA frame adapter returned an invalid or unavailable manifest.");
      const manifestCheckedAt = Date.now();
      if (candidate.freshness !== "current" || !noaaRadarManifestIsFresh(candidate, manifestCheckedAt)) throw new Error("The newest NOAA radar observation is more than 15 minutes old.");
      const latest = candidate.frames.at(-1)!;
      const requested = noaaRadarRequestedTimeRef.current;
      let current = noaaRadarFrameTimeRef.current;
      if (current && !candidate.frames.includes(current)) {
        current = null;
        noaaRadarFrameTimeRef.current = null;
        setNoaaRadarFrameTime(null);
      }
      noaaRadarManifestRef.current = candidate;
      setNoaaRadarManifest(candidate);
      setNoaaRadarManifestState("ready");
      setNoaaRadarClock(manifestCheckedAt);
      if (requested && !candidate.frames.includes(requested) && !noaaRadarFollowLatestRef.current) {
        const message = "The exact NOAA observation requested by this shared view is no longer available in the rolling manifest.";
        noaaRadarRequestedTimeRef.current = null;
        noaaRadarReadyRef.current = false;
        noaaRadarFrameTimeRef.current = null;
        setNoaaRadarFrameTime(null);
        setNoaaRadarFrameLoadState("error");
        setOfficialStates((currentStates) => ({ ...currentStates, "nws-radar": "error" }));
        setOfficialErrors((currentErrors) => ({ ...currentErrors, "nws-radar": message }));
        const map = mapRef.current;
        if (map && styleGenerationReadyRef.current) applyOfficialContextState(
          map,
          runtimeOfficialVisibility(officialVisibilityRef.current, temporalQueryRef.current.frame, false, null),
          officialOpacityRef.current,
          officialPayloadsRef.current,
        );
        if (!quiet) announce(`${message} Choose Latest to load a current frame.`);
        return;
      }
      const target = requested && candidate.frames.includes(requested)
        ? requested
        : noaaRadarFollowLatestRef.current || !current || !candidate.frames.includes(current)
          ? latest
          : current;
      noaaRadarRequestedTimeRef.current = null;
      noaaRadarReadyRef.current = Boolean(current);
      applyNoaaRadarFrame(target);
      if (!quiet) announce(`${candidate.frames.length} exact NOAA radar observations loaded; newest ${formatNoaaRadarLocalTime(latest)}`);
    } catch (error) {
      if (error instanceof Error && error.name === "AbortError") return;
      const message = error instanceof Error ? error.message : "NOAA radar frames are unavailable.";
      const lastManifest = noaaRadarManifestRef.current;
      noaaRadarReadyRef.current = Boolean(noaaRadarFrameTimeRef.current && noaaRadarManifestIsFresh(lastManifest, Date.now()));
      setNoaaRadarManifestState("error");
      setNoaaRadarManifestError(message);
      setNoaaRadarPlaying(false);
      setOfficialStates((current) => ({ ...current, "nws-radar": "error" }));
      setOfficialErrors((current) => ({ ...current, "nws-radar": message }));
      if (!quiet) announce("NOAA radar loop unavailable; no untimed or synthetic fallback was used");
    } finally {
      if (noaaRadarRequestRef.current === controller) noaaRadarRequestRef.current = null;
    }
  }, [announce, applyNoaaRadarFrame, runtimeOfficialVisibility]);

  const selectNoaaSatelliteFrame = useCallback((frame: NoaaSatelliteFrame) => {
    const manifest = noaaSatelliteManifestRef.current;
    if (!manifest?.frames.some((candidate) => candidate.kind === frame.kind && candidate.observedAt === frame.observedAt)) return;
    noaaSatelliteFollowLatestRef.current = frame.observedAt === manifest.frames.at(-1)?.observedAt;
    noaaSatelliteFrameRef.current = frame;
    setNoaaSatelliteSelectedFrame(frame);
    officialRasterFailuresRef.current.delete("noaa-goes-geocolor");
    setOfficialStates((current) => ({ ...current, "noaa-goes-geocolor": "loading" }));
    const map = mapRef.current;
    if (map?.isStyleLoaded()) {
      try {
        setNoaaSatelliteFrame(map, frame,
          buildYearCurrentRef.current && officialVisibilityRef.current["noaa-goes-geocolor"] && temporalQueryRef.current.frame === OFFICIAL_CONTEXT_PRESENT_FRAME,
          officialOpacityRef.current["noaa-goes-geocolor"]);
      } catch (error) {
        setOfficialStates((current) => ({ ...current, "noaa-goes-geocolor": "error" }));
        setOfficialErrors((current) => ({ ...current, "noaa-goes-geocolor": error instanceof Error ? error.message : "NOAA image could not be selected." }));
      }
    }
  }, []);

  const refreshNoaaSatelliteFrames = useCallback(async (quiet = false) => {
    if (document.hidden || !officialVisibilityRef.current["noaa-goes-geocolor"] || !buildYearCurrentRef.current || noaaSatelliteRequestRef.current || temporalQueryRef.current.frame !== OFFICIAL_CONTEXT_PRESENT_FRAME) return;
    const controller = new AbortController();
    noaaSatelliteRequestRef.current = controller;
    setOfficialStates((current) => ({ ...current, "noaa-goes-geocolor": "loading" }));
    setOfficialErrors((current) => ({ ...current, "noaa-goes-geocolor": undefined }));
    try {
      const response = await fetch(NOAA_SATELLITE_FRAMES_PATH, { cache: "no-store", signal: controller.signal, headers: { Accept: "application/json" } });
      const candidate = await readBoundedJson(response, 512 * 1024) as unknown;
      if (controller.signal.aborted) return;
      if (!response.ok || !isNoaaSatelliteManifest(candidate)) throw new Error("NOAA did not provide a valid dated satellite frame list.");
      noaaSatelliteManifestRef.current = candidate;
      setNoaaSatelliteManifest(candidate);
      const prior = noaaSatelliteFrameRef.current;
      const selectedFrame = noaaSatelliteFollowLatestRef.current
        ? candidate.frames.at(-1)!
        : candidate.frames.find((frame) => frame.kind === prior?.kind && frame.observedAt === prior.observedAt) ?? candidate.frames.at(-1)!;
      selectNoaaSatelliteFrame(selectedFrame);
      if (!quiet) announce(`${candidate.frameCount} dated NOAA ${candidate.product === "geocolor" ? "GeoColor" : "GOES visible fallback"} images checked; newest ${drawerTimestamp(candidate.frames.at(-1)!.observedAt)}`);
    } catch (error) {
      if (controller.signal.aborted) return;
      const message = error instanceof Error ? error.message : "NOAA satellite frames are unavailable.";
      noaaSatelliteManifestRef.current = null;
      noaaSatelliteFrameRef.current = null;
      setNoaaSatelliteManifest(null);
      setNoaaSatelliteSelectedFrame(null);
      const map = mapRef.current;
      if (map?.isStyleLoaded()) clearNoaaSatelliteFrame(map);
      setOfficialStates((current) => ({ ...current, "noaa-goes-geocolor": "error" }));
      setOfficialErrors((current) => ({ ...current, "noaa-goes-geocolor": message }));
      if (!quiet) announce("NOAA satellite imagery unavailable; no undated image was substituted");
    } finally {
      if (noaaSatelliteRequestRef.current === controller) noaaSatelliteRequestRef.current = null;
    }
  }, [announce, selectNoaaSatelliteFrame]);

  const stepNoaaRadar = useCallback((direction: "forward" | "reverse") => {
    if (!noaaRadarManifestFresh || noaaRadarLoopFrames.length < 2) return;
    const currentIndex = Math.max(0, noaaRadarFrameIndex);
    const nextIndex = nextNoaaRadarFrameIndex(noaaRadarLoopFrames.length, currentIndex, direction, false);
    if (nextIndex === null) {
      setNoaaRadarPlaying(false);
      announce(`Reached the ${direction === "forward" ? "newest" : "oldest"} NOAA radar observation in this loop`);
      return;
    }
    setNoaaRadarPlaying(false);
    setNoaaRadarFollowLatest(nextIndex === noaaRadarLoopFrames.length - 1);
    applyNoaaRadarFrame(noaaRadarLoopFrames[nextIndex], true);
  }, [announce, applyNoaaRadarFrame, noaaRadarFrameIndex, noaaRadarLoopFrames, noaaRadarManifestFresh]);

  const jumpNoaaRadarToLatest = useCallback(() => {
    if (!noaaRadarLatestFrame || !noaaRadarManifestFresh) {
      void refreshNoaaRadarManifest();
      return;
    }
    setNoaaRadarPlaying(false);
    setNoaaRadarFollowLatest(true);
    applyNoaaRadarFrame(noaaRadarLatestFrame, true);
  }, [applyNoaaRadarFrame, noaaRadarLatestFrame, noaaRadarManifestFresh, refreshNoaaRadarManifest]);

  const toggleNoaaRadarPlayback = useCallback(() => {
    if (noaaRadarPlaying) {
      setNoaaRadarPlaying(false);
      announce("NOAA radar loop paused");
      return;
    }
    if (reducedMotion) {
      announce("Automatic radar playback is off for reduced motion; previous and next observation controls remain available");
      return;
    }
    if (!noaaRadarRenderable || noaaRadarLoopFrames.length < 2 || noaaRadarFrameLoadState === "loading") return;
    const first = noaaRadarLoopFrames[0];
    if (noaaRadarFrameTime !== first) applyNoaaRadarFrame(first);
    setNoaaRadarFollowLatest(false);
    setNoaaRadarPlaying(true);
    announce(`NOAA radar loop restarted at the oldest of ${noaaRadarLoopFrames.length} exact observations`);
  }, [announce, applyNoaaRadarFrame, noaaRadarFrameLoadState, noaaRadarFrameTime, noaaRadarLoopFrames, noaaRadarPlaying, noaaRadarRenderable, reducedMotion]);

  const refreshStreamflow = useCallback(async (
    requestedRange: HydrologyRange,
    requestedStationId: string | null,
    quiet = false,
    archiveDay: string | null = null,
  ) => {
    if (!buildYearCurrentRef.current || temporalQueryRef.current.frame !== OFFICIAL_CONTEXT_PRESENT_FRAME) {
      if (!quiet) announce(buildYearCurrentRef.current ? "River Pulse remains held outside the operational-present atlas frame" : "This site build does not match the UTC year; rebuild before refreshing River Pulse");
      return;
    }
    if ((requestedRange !== "24h" || archiveDay) && !requestedStationId) {
      setStreamflowError("Select a USGS station before requesting a longer historical range.");
      if (!quiet) announce("A selected USGS station is required for longer streamflow history");
      return;
    }
    const stationId = requestedStationId ? normalizeUsgsStationId(requestedStationId) : null;
    if (requestedStationId && !stationId) {
      setStreamflowError("The selected USGS station identifier is invalid.");
      return;
    }
    const archiveEndMilliseconds = archiveDay ? Math.min(Date.now(), Date.parse(`${archiveDay}T00:00:00.000Z`) + 86_400_000) : null;
    if (archiveDay && (!validStreamflowArchiveDay(archiveDay, currentUtcDay())
      || !Number.isFinite(archiveEndMilliseconds)
      || new Date(Date.parse(`${archiveDay}T00:00:00.000Z`)).toISOString().slice(0, 10) !== archiveDay
      || archiveEndMilliseconds! > Date.now()
      || archiveEndMilliseconds! < Date.parse("1800-01-01T00:00:00.000Z"))) {
      setStreamflowError("Choose a valid past UTC calendar day.");
      return;
    }
    const path = archiveDay
      ? `/api/hydrology/streamflow?mode=station&range=24h&station=${encodeURIComponent(stationId!)}&parameter=00060&end=${encodeURIComponent(new Date(archiveEndMilliseconds!).toISOString().replace(".000Z", "Z"))}&resolution=continuous`
      : requestedRange === "24h"
      ? "/api/hydrology/streamflow?mode=network&range=24h&encoding=columns-v1"
      : `/api/hydrology/streamflow?mode=station&range=${requestedRange}&station=${encodeURIComponent(stationId!)}&parameter=00060`;
    // The statewide adapter answers a second concurrent network request with 429,
    // and aborting here does not stop its upstream work. Let an identical request
    // that is already in flight finish instead of replacing it. The network path
    // omits the station, so the newest caller's station still wins on completion.
    const inFlight = streamflowRequestRef.current;
    if (inFlight && !inFlight.signal.aborted && streamflowRequestPathRef.current === path) {
      streamflowRequestStationRef.current = stationId;
      return;
    }
    streamflowArchiveDayRef.current = archiveDay;
    setStreamflowArchiveDay(archiveDay);
    if (archiveDay) {
      streamflowBundleRef.current = null;
      setStreamflowBundle(null);
      officialPayloadsRef.current = { ...officialPayloadsRef.current, "usgs-streamflow": undefined };
      setOfficialPayloads(officialPayloadsRef.current);
    }
    streamflowRequestRef.current?.abort();
    const controller = new AbortController();
    streamflowRequestRef.current = controller;
    streamflowRequestPathRef.current = path;
    streamflowRequestStationRef.current = stationId;
    const generation = ++streamflowRequestGenerationRef.current;
    setStreamflowPlaying(false);
    setStreamflowState("loading");
    setStreamflowError(null);
    setOfficialStates((current) => ({ ...current, "usgs-streamflow": "loading" }));
    setOfficialErrors((current) => ({ ...current, "usgs-streamflow": undefined }));
    try {
      const { response, body: candidate } = await browserJsonRequest(path, {
        // The network adapter can spend 60 seconds acquiring data. Leave time
        // for its bounded response, and wait out a concurrent tab's acquisition.
        signal: controller.signal, maxBytes: 64 * 1024 * 1024,
        timeoutMs: !archiveDay && requestedRange === "24h" ? 75_000 : 60_000,
        recovery: !archiveDay && requestedRange === "24h" ? "river-network" : undefined,
        headers: { Accept: "application/json" },
      });
      if (!response.ok) {
        const message = candidate && typeof candidate === "object" && ("error" in candidate || "message" in candidate)
          ? String((candidate as { error?: unknown; message?: unknown }).error ?? (candidate as { message?: unknown }).message ?? `HTTP ${response.status}`)
          : `HTTP ${response.status}`;
        throw new Error(message);
      }
      const parsedBundle = parseStreamflowBundle(decodeStreamflowTransport(candidate));
      if (generation !== streamflowRequestGenerationRef.current) return;
      const bundle = archiveDay ? streamflowBundleForUtcDay(parsedBundle, archiveDay) : parsedBundle;
      const frames = archiveDay ? streamflowExactFrames(bundle) : streamflowDisplayFrames(bundle);
      const requestedTime = streamflowRequestedTimeRef.current;
      const restoredIndex = requestedTime
        ? frames.reduce((matched, frame, index) => Date.parse(frame) <= Date.parse(requestedTime) ? index : matched, -1)
        : -1;
      streamflowRequestedTimeRef.current = null;
      if (!archiveDay && requestedRange === "24h") {
        try { localStorage.setItem("kfm-river-station-locations-v1", savedStreamflowLocations(bundle)); } catch { /* Optional location cache. */ }
      }
      streamflowBundleRef.current = bundle;
      setStreamflowBundle(bundle);
      setStreamflowRange(requestedRange);
      setStreamflowSelectedStationId(streamflowRequestStationRef.current);
      setStreamflowFrameIndex(restoredIndex >= 0 ? restoredIndex : frames.length - 1);
      const nextState: HydrologyObservatoryState = bundle.state;
      setStreamflowState(nextState);
      setOfficialStates((current) => ({ ...current, "usgs-streamflow": bundle.state }));
      if (!quiet) announce(frames.length === 0
        ? "USGS returned no streamflow observations; no zero-flow value was inferred"
        : `${bundle.stations.length} USGS gauge${bundle.stations.length === 1 ? "" : "s"} and ${bundle.observations.length.toLocaleString("en-US")} exact observations loaded`);
    } catch (error) {
      if (controller.signal.aborted || generation !== streamflowRequestGenerationRef.current) return;
      const message = error instanceof Error ? error.message : "The USGS streamflow request failed.";
      setStreamflowPlaying(false);
      if (!streamflowBundleRef.current && !archiveDay && requestedRange === "24h") {
        try {
          const locations = restoreStreamflowLocations(localStorage.getItem("kfm-river-station-locations-v1"));
          if (locations) { streamflowBundleRef.current = locations; setStreamflowBundle(locations); setStreamflowFrameIndex(-1); }
        } catch { /* No saved locations are available. */ }
      }
      setStreamflowState(streamflowBundleRef.current ? "stale" : "error");
      setStreamflowError(message);
      setOfficialStates((current) => ({ ...current, "usgs-streamflow": "error" }));
      setOfficialErrors((current) => ({ ...current, "usgs-streamflow": message }));
      if (!quiet) announce(streamflowBundleRef.current
        ? "USGS refresh failed; River Pulse is frozen on its visibly dated last confirmed bundle"
        : "USGS streamflow is unavailable; no synthetic or stale fallback was used");
    } finally {
      if (streamflowRequestRef.current === controller) streamflowRequestRef.current = null;
    }
  }, [announce]);

  const refreshSelectedStreamflow = useCallback((quiet = false) => {
    const archiveDay = streamflowArchiveDayRef.current;
    return refreshStreamflow(archiveDay ? "24h" : streamflowRange, streamflowSelectedStationId, quiet, archiveDay);
  }, [refreshStreamflow, streamflowRange, streamflowSelectedStationId]);

  const refreshNoaaHydrologyNetwork = useCallback(async (quiet = false) => {
    if (!buildYearCurrentRef.current || temporalQueryRef.current.frame !== OFFICIAL_CONTEXT_PRESENT_FRAME) {
      if (!quiet) announce(buildYearCurrentRef.current ? "NOAA hydrology remains held outside the operational-present atlas frame" : "This site build does not match the UTC year; rebuild before refreshing NOAA hydrology");
      return;
    }
    if (noaaHydrologyRequestRef.current && !noaaHydrologyRequestRef.current.signal.aborted) return;
    const controller = new AbortController();
    noaaHydrologyRequestRef.current = controller;
    setOfficialStates((current) => ({ ...current, "noaa-nwps-gauges": "loading" }));
    setOfficialErrors((current) => ({ ...current, "noaa-nwps-gauges": undefined }));
    try {
      const { response, body: candidate } = await browserJsonRequest(NOAA_HYDROLOGY_NETWORK_API_PATH, {
        signal: controller.signal, maxBytes: 8 * 1024 * 1024, timeoutMs: 30_000, headers: { Accept: "application/json" },
      });
      if (!response.ok) throw new Error(`NOAA hydrology adapter returned HTTP ${response.status}.`);
      if (controller.signal.aborted || noaaHydrologyRequestRef.current !== controller) return;
      const network = parseNoaaGaugeNetwork(candidate);
      const data = noaaGaugeNetworkGeoJson(network);
      const payload: OfficialContextPayload = {
        feed: "noaa-nwps-gauges",
        state: network.state,
        retrievedAt: network.retrievedAt,
        upstreamUpdatedAt: network.records.flatMap((gauge) => [gauge.observed.validTime, gauge.forecast.validTime]).filter((value): value is string => Boolean(value)).sort().at(-1) ?? null,
        featureCount: data.features.length,
        data,
        source: network.sourceUrl,
        limitation: network.limitation,
        truncated: network.truncated,
      };
      officialPayloadsRef.current = { ...officialPayloadsRef.current, "noaa-nwps-gauges": payload };
      setOfficialPayloads(officialPayloadsRef.current);
      setOfficialStates((current) => ({ ...current, "noaa-nwps-gauges": payload.state }));
      if (!quiet) announce(`${payload.featureCount} NOAA NWPS Kansas gauges loaded with separate observed and forecast states`);
    } catch (error) {
      if (controller.signal.aborted) return;
      const message = error instanceof Error ? error.message : "The NOAA hydrology request failed.";
      setOfficialStates((current) => ({ ...current, "noaa-nwps-gauges": "error" }));
      setOfficialErrors((current) => ({ ...current, "noaa-nwps-gauges": message }));
      if (!quiet) announce("NOAA hydrology is unavailable; no warning, normal-flow, or all-clear state was inferred");
    } finally {
      if (noaaHydrologyRequestRef.current === controller) noaaHydrologyRequestRef.current = null;
    }
  }, [announce]);

  useEffect(() => {
    if (!streamflowBundle) return;
    const payload = streamflowContextPayload(streamflowBundle, streamflowFrame, streamflowFrameTime, streamflowSelectedStationId, riverMapDisplay);
    officialPayloadsRef.current = { ...officialPayloadsRef.current, "usgs-streamflow": payload };
    setOfficialPayloads(officialPayloadsRef.current);
  }, [streamflowBundle, streamflowFrame, streamflowFrameTime, streamflowSelectedStationId, riverMapDisplay]);

  const stepStreamflow = useCallback((direction: "reverse" | "forward") => {
    if (streamflowFrames.length === 0) return;
    const nextIndex = clamp(safeStreamflowFrameIndex + (direction === "forward" ? 1 : -1), 0, streamflowFrames.length - 1);
    if (nextIndex === safeStreamflowFrameIndex) {
      announce(`Reached the ${direction === "forward" ? "latest" : "oldest"} River Pulse observation frame`);
      return;
    }
    setStreamflowPlaying(false);
    setStreamflowFrameIndex(nextIndex);
    announce(`River Pulse stepped to ${new Date(streamflowFrames[nextIndex]).toLocaleString()}; no values were interpolated`);
  }, [announce, safeStreamflowFrameIndex, streamflowFrames]);

  const toggleStreamflowPlayback = useCallback(() => {
    if (streamflowPlaying) {
      setStreamflowPlaying(false);
      announce("River Pulse playback paused");
      return;
    }
    if (reducedMotion) {
      announce("Automatic River Pulse playback is off for reduced motion; exact-frame stepping remains available");
      return;
    }
    if (streamflowFrames.length < 2 || streamflowDisplayState === "error" || streamflowDisplayState === "empty" || streamflowDisplayState === "loading") return;
    setStreamflowPlaying(true);
    announce(`River Pulse started across ${streamflowFrames.length} exact USGS observation frames without interpolation`);
  }, [announce, reducedMotion, streamflowDisplayState, streamflowFrames.length, streamflowPlaying]);

  const seekStreamflow = useCallback((index: number) => {
    if (streamflowFrames.length === 0) return;
    setStreamflowPlaying(false);
    setStreamflowFrameIndex(clamp(Math.round(index), 0, streamflowFrames.length - 1));
  }, [streamflowFrames.length]);

  const jumpStreamflowToLatest = useCallback(() => {
    if (streamflowFrames.length === 0) return;
    setStreamflowPlaying(false);
    setStreamflowFrameIndex(streamflowFrames.length - 1);
    announce("River Pulse returned to the latest exact USGS observation frame");
  }, [announce, streamflowFrames.length]);

  const changeStreamflowRange = useCallback((range: HydrologyRange) => {
    const stationRequired = range !== "24h";
    if (stationRequired && !streamflowSelectedStationId) {
      announce("Select a USGS station before opening a longer history");
      return;
    }
    setStreamflowRange(range);
    void refreshStreamflow(range, streamflowSelectedStationId);
  }, [announce, refreshStreamflow, streamflowSelectedStationId]);

  const selectStreamflowStation = useCallback((stationId: string | null) => {
    const normalized = stationId ? normalizeUsgsStationId(stationId) : null;
    riverPathFocusRef.current = null;
    setStreamflowPlaying(false);
    setStreamflowSelectedStationId(normalized);
    setLiveInstrument("river");
    if (streamflowArchiveDayRef.current && normalized) {
      void refreshStreamflow("24h", normalized, false, streamflowArchiveDayRef.current);
      return;
    }
    if (streamflowArchiveDayRef.current && !normalized) {
      void refreshStreamflow("24h", null);
      return;
    }
    if (!normalized && streamflowRange !== "24h") {
      setStreamflowRange("24h");
      void refreshStreamflow("24h", null);
      return;
    }
    if (normalized && streamflowRange !== "24h") void refreshStreamflow(streamflowRange, normalized);
  }, [refreshStreamflow, streamflowRange]);

  const showStreamflowDirection = useCallback(() => {
    const map = mapRef.current;
    if (!map || !streamflowBundle || !streamflowSelectedAtPresent) return;
    const reporting = new Set(streamflowFrame?.features
      .filter((feature) => !feature.properties.missing && feature.properties.value !== null && feature.properties.value > 0)
      .map((feature) => feature.properties.stationId) ?? []);
    const candidates = streamflowBundle.stations.filter((station) => reporting.has(station.stationId));
    const center = map.getCenter();
    const station = streamflowSelectedStation ?? (candidates.length ? candidates : streamflowBundle.stations)
      .reduce<typeof streamflowBundle.stations[number] | null>((closest, candidate) => {
        if (!closest) return candidate;
        const distance = (candidate.longitude - center.lng) ** 2 + (candidate.latitude - center.lat) ** 2;
        const closestDistance = (closest.longitude - center.lng) ** 2 + (closest.latitude - center.lat) ** 2;
        return distance < closestDistance ? candidate : closest;
      }, null);
    if (!station) return;
    if (station.stationId !== streamflowSelectedStationId) selectStreamflowStation(station.stationId);
    const pathPoints = station.stationId === streamflowSelectedStationId ? downstreamPaths.flatMap(path => path.coordinates) : [];
    riverPathFocusRef.current = downstreamState === "ready" && pathPoints.length ? null : station.stationId;
    if (pathPoints.length) {
      const longitudes = pathPoints.map(point => point[0]), latitudes = pathPoints.map(point => point[1]);
      map.fitBounds([[Math.min(...longitudes), Math.min(...latitudes)], [Math.max(...longitudes), Math.max(...latitudes)]], {
        padding: { top: 50, left: 55, right: 55, bottom: Math.min(300, map.getCanvas().clientHeight * 0.4) }, maxZoom: 13, duration: reducedMotion ? 0 : 650,
      });
    } else map.easeTo({
      center: [station.longitude, station.latitude],
      zoom: Math.max(map.getZoom(), 11.5),
      offset: [0, -Math.min(150, map.getCanvas().clientHeight * 0.22)],
      duration: reducedMotion ? 0 : 650,
    });
    announce(`Showing mapped flow direction near ${station.name}; arrow pace is illustrative`);
  }, [announce, downstreamPaths, downstreamState, reducedMotion, selectStreamflowStation, streamflowBundle, streamflowFrame, streamflowSelectedAtPresent, streamflowSelectedStation, streamflowSelectedStationId]);

  const loadStreamflowArchiveDay = useCallback(() => {
    if (!streamflowArchiveDraftDay || !streamflowSelectedStationId) return;
    void refreshStreamflow("24h", streamflowSelectedStationId, false, streamflowArchiveDraftDay);
  }, [refreshStreamflow, streamflowArchiveDraftDay, streamflowSelectedStationId]);

  // Find a county reads the county payload, so it loads once even while the
  // county layer is hidden (it is off by default); hidden data is not drawn.
  const searchNeedsCounties = (id: OfficialContextId) => id === "census-counties" && !officialPayloadsRef.current["census-counties"];
  const refreshOfficialContext = useCallback(async (feed: OfficialContextFeedId) => {
    if (!buildYearCurrentRef.current || temporalQueryRef.current.frame !== OFFICIAL_CONTEXT_PRESENT_FRAME || officialArchiveDaysRef.current[feed]) return;
    if (officialRequestsRef.current.has(feed)) return;
    const source = OFFICIAL_CONTEXT_BY_ID[feed];
    const controller = new AbortController();
    officialRequestsRef.current.set(feed, controller);
    setOfficialStates((current) => ({ ...current, [feed]: "loading" }));
    setOfficialErrors((current) => ({ ...current, [feed]: undefined }));
    try {
      const { response, body } = await layerJsonReadsRef.current!.read(source.apiPath!, {
        signal: controller.signal, maxBytes: 8 * 1024 * 1024,
        validate: value => validLayerPayload(value, feed),
        onProgress: phase => { if (!controller.signal.aborted && officialRequestsRef.current.get(feed) === controller) setOfficialReadPhases(current => ({ ...current, [feed]: phase })); },
      });
      const candidate = body as Partial<OfficialContextPayload> & { error?: string };
      const validState = candidate.state === "ready" || candidate.state === "empty" || candidate.state === "partial";
      if (!response.ok || candidate.feed !== feed || !validState || typeof candidate.featureCount !== "number" || !candidate.data || candidate.data.type !== "FeatureCollection" || !Array.isArray(candidate.data.features)) {
        throw new Error(candidate.error ?? `Fixed source adapter returned HTTP ${response.status}.`);
      }
      if (controller.signal.aborted || officialRequestsRef.current.get(feed) !== controller) return;
      const payload = candidate as OfficialContextPayload;
      officialPayloadsRef.current = { ...officialPayloadsRef.current, [feed]: payload };
      setOfficialPayloads(officialPayloadsRef.current);
      setOfficialStates((current) => ({ ...current, [feed]: payload.state }));
      const map = mapRef.current;
      if (map && styleGenerationReadyRef.current) applyOfficialContextState(map, runtimeOfficialVisibility(officialVisibilityRef.current, temporalQueryRef.current.frame, noaaRadarReadyRef.current, noaaRadarFrameTimeRef.current), officialOpacityRef.current, officialPayloadsRef.current);
      announce(payload.featureCount === 0
        ? `${source.shortTitle}: zero mapped features at ${new Date(payload.retrievedAt).toLocaleTimeString()}—not an all-clear`
        : `${source.shortTitle}: ${payload.featureCount} ${feed === "deflock-alpr" ? "community report areas" : "official context features"} refreshed`);
    } catch (error) {
      if (controller.signal.aborted || officialRequestsRef.current.get(feed) !== controller) return;
      const message = error instanceof Error ? error.message : "Official context request failed.";
      // A failed current refresh cannot leave an earlier operational snapshot
      // mapped under an unavailable status. The payload change reapplies an
      // empty GeoJSON source through the official-source map effect.
      officialPayloadsRef.current = { ...officialPayloadsRef.current, [feed]: undefined };
      setOfficialPayloads(officialPayloadsRef.current);
      const selectedFeedFailed = officialContextIdForSelection(selectedRef.current) === feed;
      if (selectedFeedFailed) {
        selectedRef.current = null;
        setSelected(null);
        setRightOpen(false);
      }
      const map = mapRef.current;
      if (map && styleGenerationReadyRef.current) {
        runMapMutation("Clear failed official source", () => {
          clearOfficialContextFeed(map, feed);
          if (selectedFeedFailed) updateSelectionSource(map, null);
        });
      }
      setOfficialStates((current) => ({ ...current, [feed]: "error" }));
      setOfficialErrors((current) => ({ ...current, [feed]: message }));
      announce(`${source.shortTitle} unavailable; previous mapped features were cleared and no fallback inference was used`);
    } finally {
      if (officialRequestsRef.current.get(feed) === controller) officialRequestsRef.current.delete(feed);
    }
  }, [announce, runMapMutation, runtimeOfficialVisibility]);

  const reserveSmokePlayback = useCallback((day: string, signal: AbortSignal) => {
    signal.throwIfAborted();
    officialRequestsRef.current.get("noaa-hms-smoke")?.abort();
    officialRequestsRef.current.delete("noaa-hms-smoke");
    // A prior day's confirmed payload cannot certify this new reservation.
    if (officialArchiveDaysRef.current["noaa-hms-smoke"] !== day) {
      officialArchivePayloadsRef.current = { ...officialArchivePayloadsRef.current, "noaa-hms-smoke": undefined };
    }
    // Pin acquisition immediately, but label the map date only after commit.
    officialArchiveDaysRef.current = { ...officialArchiveDaysRef.current, "noaa-hms-smoke": day };
  }, []);
  const commitSmokePlayback = useCallback((day: string, payload: OfficialContextPayload, callerSignal: AbortSignal, smooth: boolean) => {
    const owner = smokeTransitionsRef.current.signal;
    return smokeTransitionsRef.current.run(callerSignal, async (signal) => {
      const map = mapRef.current;
      const sourceId = OFFICIAL_CONTEXT_BY_ID["noaa-hms-smoke"].sourceId;
      const source = map?.getSource(sourceId);
      if (!map || !styleGenerationReadyRef.current || source?.type !== "geojson") throw new Error("Smoke map is not ready.");
      const sameSource = () => mapRef.current === map && styleGenerationReadyRef.current && map.getSource(sourceId) === source;
      const checked = (uploaded = false) => {
        signal.throwIfAborted();
        if (!sameSource() || uploaded && !geoJSONHasData(source as GeoJSONSource, payload.data)) throw new Error("Smoke map changed during playback.");
      };
      const prior = officialPayloadsRef.current["noaa-hms-smoke"];
      const apply = (values = officialPayloadsRef.current) => { if (sameSource()) applyOfficialContextState(map, runtimeOfficialVisibility(officialVisibilityRef.current, temporalQueryRef.current.frame, noaaRadarReadyRef.current, noaaRadarFrameTimeRef.current), officialOpacityRef.current, values); };
      let presented = false;
      const paint = (factor: number) => { if (sameSource()) setHmsSmokeFade(map, factor, officialOpacityRef.current["noaa-hms-smoke"]); };
      try {
        checked();
        if (prior && smooth) await hmsFade(1, 0, signal, paint);
        checked();
        // Tentative renderer data is not yet confirmed source/evidence state.
        presented = true;
        apply({ ...officialPayloadsRef.current, "noaa-hms-smoke": payload });
        await waitForGeoJSON(source as GeoJSONSource, signal);
        checked(true);
        if (prior && smooth) await hmsFade(0, 1, signal, paint);
        checked(true);
        officialPayloadsRef.current = { ...officialPayloadsRef.current, "noaa-hms-smoke": payload };
        setOfficialPayloads(officialPayloadsRef.current);
        officialArchivePayloadsRef.current["noaa-hms-smoke"] = payload;
        setOfficialArchiveDays(current => ({ ...current, "noaa-hms-smoke": day }));
        setOfficialStates(current => ({ ...current, "noaa-hms-smoke": payload.state }));
        setOfficialErrors(current => ({ ...current, "noaa-hms-smoke": undefined }));
      } catch (error) {
        if (!owner.aborted && presented && officialPayloadsRef.current["noaa-hms-smoke"] === prior) {
          apply();
          // Restoration is bounded by the upload helper, but must finish before
          // a queued transition is allowed to adopt its own prior frame.
          if (sameSource()) await waitForGeoJSON(source as GeoJSONSource);
        }
        throw error;
      } finally {
        // Style replacement can remove this source while its map remains alive.
        // Do not leave that map's next style inheriting a zero opacity multiplier.
        if (!owner.aborted) {
          resetHmsSmokeFade(map);
          if (mapRef.current === map && styleGenerationReadyRef.current) setHmsSmokeFade(map, 1, officialOpacityRef.current["noaa-hms-smoke"]);
        }
      }
    });
  }, []);

  const loadOfficialArchiveDay = useCallback((feed: OfficialContextFeedId, day: string, force = false): Promise<void> => {
    const prior = calendarArchiveLoads.current.get(feed);
    if (!force && prior?.day === day) return prior.promise;
    const promise = (async () => {
    if (![CIVIC_ID, "usgs-earthquakes", "noaa-hms-smoke", "nasa-gibs-fire-points", "raspberry-shake-stations"].includes(feed)
      || !/^\d{4}-\d{2}-\d{2}$/.test(day)
      || !Number.isFinite(Date.parse(`${day}T00:00:00.000Z`))
      || new Date(`${day}T00:00:00.000Z`).toISOString().slice(0, 10) !== day
      || day > currentUtcDay()
      || (feed === "nasa-gibs-fire-points" && day < "2018-01-01")
      || (feed === "noaa-hms-smoke" && day < "2005-08-05")
      || (feed === CIVIC_ID && civicCongressForDay(day) === null)) return;
    if (feed === "noaa-hms-smoke") cancelSmokePlayback();
    if (officialArchiveDaysRef.current[feed] === day && !officialRequestsRef.current.get(feed)?.signal.aborted && officialRequestsRef.current.has(feed)) return;
    officialRequestsRef.current.get(feed)?.abort();
    const controller = new AbortController();
    officialRequestsRef.current.set(feed, controller);
    officialArchiveDaysRef.current = { ...officialArchiveDaysRef.current, [feed]: day };
    setOfficialArchiveDays(officialArchiveDaysRef.current);
    officialArchivePayloadsRef.current = { ...officialArchivePayloadsRef.current, [feed]: undefined };
    officialPayloadsRef.current = { ...officialPayloadsRef.current, [feed]: undefined };
    setOfficialPayloads(officialPayloadsRef.current);
    setOfficialStates((current) => ({ ...current, [feed]: "loading" }));
    setOfficialErrors((current) => ({ ...current, [feed]: undefined }));
    if (feed === "usgs-earthquakes") setEarthquakeArchiveFrameIndex(-1);
    if (feed === "noaa-hms-smoke") setSmokeArchiveFrameIndex(-1);
    try {
      const source = OFFICIAL_CONTEXT_BY_ID[feed];
      const cached = feed === "nasa-gibs-fire-points" ? await readFireDay(day) : null;
      controller.signal.throwIfAborted();
      const read = cached ? null : await layerJsonReadsRef.current!.read(`${source.apiPath!}&day=${encodeURIComponent(day)}`, {
        signal: controller.signal, maxBytes: 8 * 1024 * 1024, cacheMs: force ? 0 : 300_000,
        validate: value => validLayerPayload(value, feed, day),
        onProgress: phase => { if (!controller.signal.aborted && officialRequestsRef.current.get(feed) === controller) setOfficialReadPhases(current => ({ ...current, [feed]: phase })); },
      });
      const response = read?.response;
      const candidate = (cached ?? read?.body) as Partial<OfficialContextPayload> & { error?: string };
      const validState = candidate.state === "ready" || candidate.state === "empty" || candidate.state === "partial";
      if ((response && !response.ok) || candidate.feed !== feed || !validState || typeof candidate.featureCount !== "number"
        || !candidate.data || candidate.data.type !== "FeatureCollection" || !Array.isArray(candidate.data.features)) {
        throw new Error(candidate.error ?? `Dated source adapter returned HTTP ${response?.status ?? "invalid cached response"}.`);
      }
      if (controller.signal.aborted || officialRequestsRef.current.get(feed) !== controller) return;
      const payload = candidate as OfficialContextPayload;
      officialArchivePayloadsRef.current = { ...officialArchivePayloadsRef.current, [feed]: payload };
      const smokeTimes = feed === "noaa-hms-smoke" ? smokeValidityTimes(payload, day) : [];
      const smokeFrameIndex = feed === "noaa-hms-smoke" ? smokeInitialFrameIndex(payload, day) : -1;
      const visiblePayload = feed === "noaa-hms-smoke" && smokeFrameIndex >= 0 ? smokeValidAt(payload, day, smokeTimes[smokeFrameIndex]) : payload;
      officialPayloadsRef.current = { ...officialPayloadsRef.current, [feed]: visiblePayload };
      setOfficialPayloads(officialPayloadsRef.current);
      setOfficialStates((current) => ({ ...current, [feed]: payload.state }));
      if (feed === "noaa-hms-smoke") setSmokeArchiveFrameIndex(smokeFrameIndex);
      if (feed === "usgs-earthquakes") {
        const times = earthquakeEventTimes(payload, day);
        setEarthquakeArchiveFrameIndex(times.length - 1);
      }
      announce(payload.featureCount
        ? `${source.shortTitle}: ${payload.featureCount} dated source records loaded for ${day} UTC${cached ? " from this browser's map directory" : read?.cache === "memory" ? " from the dated snapshot kept on this page; original retrieval time retained" : ""}`
        : `${source.shortTitle}: no mapped records returned for ${day} UTC; no earlier day was carried forward`);
    } catch (error) {
      if (controller.signal.aborted || officialRequestsRef.current.get(feed) !== controller) return;
      const message = error instanceof Error ? error.message : "Dated source request failed.";
      setOfficialStates((current) => ({ ...current, [feed]: "error" }));
      setOfficialErrors((current) => ({ ...current, [feed]: message }));
      announce(`${OFFICIAL_CONTEXT_BY_ID[feed].shortTitle}: archive day unavailable; the map is empty for this source`);
    } finally {
      if (officialRequestsRef.current.get(feed) === controller) officialRequestsRef.current.delete(feed);
    }
    })();
    calendarArchiveLoads.current.set(feed, { day, promise });
    const settled = () => { if (calendarArchiveLoads.current.get(feed)?.promise === promise) calendarArchiveLoads.current.delete(feed); };
    void promise.then(settled, settled);
    return promise;
  }, [announce, cancelSmokePlayback]);

  const returnOfficialSourceToCurrent = useCallback((feed: OfficialContextFeedId) => {
    if (feed === "noaa-hms-smoke") cancelSmokePlayback();
    officialRequestsRef.current.get(feed)?.abort();
    officialRequestsRef.current.delete(feed);
    officialArchiveDaysRef.current = { ...officialArchiveDaysRef.current, [feed]: undefined };
    setOfficialArchiveDays(officialArchiveDaysRef.current);
    officialArchivePayloadsRef.current = { ...officialArchivePayloadsRef.current, [feed]: undefined };
    officialPayloadsRef.current = { ...officialPayloadsRef.current, [feed]: undefined };
    setOfficialPayloads(officialPayloadsRef.current);
    if (feed === "usgs-earthquakes") setEarthquakeArchiveFrameIndex(-1);
    if (feed === "noaa-hms-smoke") setSmokeArchiveFrameIndex(-1);
    void refreshOfficialContext(feed);
  }, [cancelSmokePlayback, refreshOfficialContext]);


  const seekCalendarFrame = useCallback(async (candidate: CalendarSweepView): Promise<CalendarFrameOutcome> => {
    const next = readCalendarSweep(JSON.stringify(candidate), currentUtcDay());
    if (!next) return { state: "error", message: "Choose a valid UTC calendar range." };
    cancelSmokePlayback();
    const generation = ++calendarSeekGeneration.current, day = calendarFrameDay(next);
    const nextYear = Number(day.slice(0, 4));
    calendarSweepRef.current = next; setCalendarSweep(next); setPlaying(false); setTemporalMode("snapshot");
    commitTemporalFrame(nextYear, undefined, true);
    // A feature selected on another day must not remain bound to the drawer/AI.
    if (selectedRef.current) { selectedRef.current = null; setSelected(null); setRightOpen(false); if (mapRef.current?.isStyleLoaded()) updateSelectionSource(mapRef.current, null); }
    const feeds = calendarArchiveFeeds(officialVisibilityRef.current, day);
    const reads = feeds.filter(feed => officialArchiveDaysRef.current[feed] !== day || !officialArchivePayloadsRef.current[feed]);
    for (const feed of Object.keys(CALENDAR_ARCHIVE_BOUNDS) as CalendarArchiveFeed[]) {
      if (!officialVisibilityRef.current[feed] || officialArchiveDaysRef.current[feed] === day) continue;
      officialRequestsRef.current.get(feed)?.abort(); officialRequestsRef.current.delete(feed);
      officialArchivePayloadsRef.current = { ...officialArchivePayloadsRef.current, [feed]: undefined };
      officialPayloadsRef.current = { ...officialPayloadsRef.current, [feed]: undefined };
    }
    setOfficialPayloads(officialPayloadsRef.current);
    // Independent bounded adapters; each already rejects stale/aborted replies.
    await Promise.all(reads.map(feed => loadOfficialArchiveDay(feed, day)));
    if (generation !== calendarSeekGeneration.current) return { state: "reference", message: "A newer date replaced this request." };
    const checked = feeds.map(feed => officialArchiveDaysRef.current[feed] === day ? officialArchivePayloadsRef.current[feed] : undefined);
    if (feeds.length && checked.every(payload => !payload)) return { state: "error", message: "Selected sources are unavailable for " + day + ". Previous dated features remain withheld." };
    const map = mapRef.current;
    if (map && styleGenerationReadyRef.current) {
      applyOfficialContextState(map, runtimeOfficialVisibility(officialVisibilityRef.current, nextYear, noaaRadarReadyRef.current, noaaRadarFrameTimeRef.current), officialOpacityRef.current, officialPayloadsRef.current);
      try {
        await Promise.all(feeds.map(async feed => {
          const source = map.getSource(OFFICIAL_CONTEXT_BY_ID[feed].sourceId);
          if (source?.type === "geojson") await waitForGeoJSON(source as GeoJSONSource, AbortSignal.timeout(15_000));
        }));
      } catch { return { state: "error", message: "The selected date did not finish rendering. Playback paused; retry this date." }; }
    } else if (feeds.length) return { state: "error", message: "Observations were checked; the map renderer is not ready. Playback paused." };
    if (generation !== calendarSeekGeneration.current) return { state: "reference", message: "A newer date replaced this request." };
    if (!feeds.length) {
      const annual = next.step === "years" && activeLayers.some(layer => Boolean(layer.temporal));
      return { state: annual ? "empty" : "reference", message: annual ? "Annual catalog frame selected. No daily source follows this date; catalog availability is not observed change." : "No selected source can follow this date. Open Layers to select earthquake, smoke, thermal-detection, station-inventory, or congressional history. Other source clocks remain separate." };
    }
    const partial = checked.some(payload => !payload || payload.state === "partial" || payload.truncated);
    const count = checked.reduce((sum, payload) => sum + (payload?.featureCount ?? 0), 0);
    return { state: partial ? "partial" : count ? "ready" : "empty", message: day + " UTC · " + count + " returned source records across " + feeds.length + " selected dated sources." + (partial ? " Coverage is partial or one source is unavailable." : count ? " Source dates and retrieval clocks remain separate." : " An empty response does not prove absence.") };
  }, [activeLayers, cancelSmokePlayback, commitTemporalFrame, loadOfficialArchiveDay, runtimeOfficialVisibility, setRightOpen]);

  // Turning on a supported layer inside an active calendar view checks that
  // same day. It never substitutes the provider's current snapshot.
  useEffect(() => {
    const current = calendarSweepRef.current;
    if (!current) return;
    const day = calendarFrameDay(current);
    for (const feed of calendarArchiveFeeds(officialVisibility, day)) {
      if (officialArchiveDaysRef.current[feed] !== day || !officialArchivePayloadsRef.current[feed] && !officialRequestsRef.current.has(feed)) void loadOfficialArchiveDay(feed, day);
    }
  }, [calendarSweep, loadOfficialArchiveDay, officialVisibility]);

  const returnCalendarToPresent = useCallback(() => {
    setPlaying(false); setTemporalMode("snapshot"); commitTemporalFrame(OFFICIAL_CONTEXT_PRESENT_FRAME);
  }, [commitTemporalFrame]);

  // Year-only frames resolve to January 1; exact Congress selections use the shared calendar.
  useEffect(() => {
    if (calendarSweep || !officialVisibility[CIVIC_ID] || !buildYearCurrent || temporalQuery.frame === OFFICIAL_CONTEXT_PRESENT_FRAME) return;
    const day = civicDayForFrame(temporalQuery.frame, OFFICIAL_CONTEXT_PRESENT_FRAME, currentUtcDay(), null);
    if (day && (officialArchiveDaysRef.current[CIVIC_ID] !== day || !officialArchivePayloadsRef.current[CIVIC_ID] && !officialRequestsRef.current.has(CIVIC_ID))) void loadOfficialArchiveDay(CIVIC_ID, day);
  }, [calendarSweep, officialVisibility, buildYearCurrent, temporalQuery.frame, loadOfficialArchiveDay]);

  const seekEarthquakeArchiveFrame = useCallback((index: number) => {
    const day = officialArchiveDaysRef.current["usgs-earthquakes"];
    const original = officialArchivePayloadsRef.current["usgs-earthquakes"];
    const time = earthquakeArchiveFrames[index];
    if (!day || !original || !time) return;
    const payload = earthquakesThroughEvent(original, day, time);
    officialPayloadsRef.current = { ...officialPayloadsRef.current, "usgs-earthquakes": payload };
    setOfficialPayloads(officialPayloadsRef.current);
    setEarthquakeArchiveFrameIndex(index);
  }, [earthquakeArchiveFrames]);

  const seekSmokeArchiveFrame = useCallback((index: number) => {
    const day = officialArchiveDaysRef.current["noaa-hms-smoke"];
    const original = officialArchivePayloadsRef.current["noaa-hms-smoke"];
    const cursor = smokeArchiveFrames[index];
    if (!day || !original || !cursor) return;
    officialPayloadsRef.current = { ...officialPayloadsRef.current, "noaa-hms-smoke": smokeValidAt(original, day, cursor) };
    setOfficialPayloads(officialPayloadsRef.current);
    setSmokeArchiveFrameIndex(index);
  }, [smokeArchiveFrames]);

  const setOfficialContextVisible = useCallback((id: OfficialContextId, visible: boolean) => {
    const terrainRaster = id === "usgs-3dep-hillshade" || id === "usgs-3dep-slope";
    if (id === "nws-radar" && visible) {
      noaaRadarReadyRef.current = Boolean(
        noaaRadarFrameTimeRef.current
        && noaaRadarManifestIsFresh(noaaRadarManifestRef.current, Date.now()),
      );
      setNoaaRadarClock(Date.now());
      setLiveInstrument("radar");
      setInstrumentOpen(true);
    }
    if (id === "usgs-streamflow" && visible) setLiveInstrument("river");
    const source = OFFICIAL_CONTEXT_BY_ID[id];
    if (visible && source.kind === "OPERATIONAL_WMS" && id !== "nws-radar" && !terrainRaster) {
      officialRasterFailuresRef.current.delete(id);
      setOfficialErrors(current => current[id] ? ({ ...current, [id]: undefined }) : current);
    }
    const next = { ...officialVisibilityRef.current, [id]: visible };
    officialVisibilityRef.current = next;
    setOfficialVisibility(next);
    if (!visible && source.apiPath) {
      const feed = id as OfficialContextFeedId;
      officialRequestsRef.current.get(feed)?.abort();
      officialRequestsRef.current.delete(feed);
      setOfficialStates(current => ({ ...current, [id]: officialPayloadsRef.current[feed]?.state ?? "idle" }));
    }
    if (source.apiPath && visible && !officialPayloadsRef.current[id as OfficialContextFeedId]) {
      const feed = id as OfficialContextFeedId, day = officialArchiveDaysRef.current[feed];
      if (day) void loadOfficialArchiveDay(feed, day);
      else void refreshOfficialContext(feed);
    }
    if (id === "usgs-streamflow" && visible && !streamflowBundleRef.current) void refreshSelectedStreamflow();
    if (id === "noaa-nwps-gauges" && visible && !officialPayloadsRef.current["noaa-nwps-gauges"]) void refreshNoaaHydrologyNetwork();
    if (id === "nws-radar" && visible && temporalQueryRef.current.frame === OFFICIAL_CONTEXT_PRESENT_FRAME) void refreshNoaaRadarManifest();
    if (id === "nws-radar" && !visible) setNoaaRadarPlaying(false);
    if (id === "noaa-lightning-density") {
      lightningAutoStartRef.current = visible;
      setLightningPlaying(false);
      if (visible) { setLiveInstrument("lightning"); setInstrumentOpen(true); }
    }
    if (id === "usgs-streamflow" && !visible) setStreamflowPlaying(false);
    const map = mapRef.current;
    const rasterPending = visible && source.kind === "OPERATIONAL_WMS" && id !== "nws-radar" && !officialRasterFailuresRef.current.has(id);
    if (rasterPending) setOfficialStates((current) => ({ ...current, [id]: "loading" }));
    // A failed global runtime proof must not leave a selected source at IDLE
    // when MapLibre's style is already loaded and can accept this layer.
    if (map?.isStyleLoaded()) {
      try {
        applyOfficialContextState(map, runtimeOfficialVisibility(next, temporalQueryRef.current.frame, noaaRadarReadyRef.current, noaaRadarFrameTimeRef.current), officialOpacityRef.current, officialPayloadsRef.current);
        if (terrainRaster) {
          const rendererSource = map.getSource(source.sourceId);
          terrainRasterViewRef.current.bindSource(id, rendererSource);
          if (visible && temporalQueryRef.current.frame === OFFICIAL_CONTEXT_PRESENT_FRAME) {
            const bounds = map.getBounds();
            const viewBounds = { west: bounds.getWest(), east: bounds.getEast(), south: bounds.getSouth(), north: bounds.getNorth() };
            const failed = terrainRasterViewRef.current.hasFailed(id, viewBounds, map.getZoom());
            if (failed) officialRasterFailuresRef.current.add(id);
            else officialRasterFailuresRef.current.delete(id);
            const state = terrainRasterViewRef.current.status(id, viewBounds, map.getZoom(), Boolean(rendererSource && map.isSourceLoaded(source.sourceId)));
            setOfficialStates(current => current[id] === state ? current : ({ ...current, [id]: state }));
            if (!failed) setOfficialErrors(current => current[id] ? ({ ...current, [id]: undefined }) : current);
          }
        }
      } catch (error) {
        setOfficialStates((current) => ({ ...current, [id]: "error" }));
        setOfficialErrors((current) => ({ ...current, [id]: error instanceof Error ? error.message : "Raster context could not be applied." }));
      }
    }
  }, [loadOfficialArchiveDay, refreshNoaaHydrologyNetwork, refreshNoaaRadarManifest, refreshOfficialContext, refreshSelectedStreamflow, runtimeOfficialVisibility]);

  const applyStarterContext = (ids: readonly OfficialContextId[], title: string) => {
    // Revalidate at the owning state boundary. No camera, time, opacity, release or specialist-owner writes.
    const plan = starterPlan(ids, OFFICIAL_CONTEXT_SOURCES, starterAccess);
    if (ids.length && !plan.selected.length) { announce("Starter sources are held or unavailable; current layers remain selected"); return; }
    const changes = contextSelectionChanges(plan.selected, OFFICIAL_CONTEXT_SOURCES, officialVisibilityRef.current);
    changes.forEach(change => setOfficialContextVisible(change.id, change.visible));
    setOfficialSourceQuery("");
    setOfficialWorkspace("all");
    setOfficialCatalogFilter("all");
    setLayerCatalogView("selected");
    announce(`${title}; ${plan.selected.length} public context layers selected. Camera and source dates retained.`);
  };

  const retryOfficialLayer = (id: OfficialContextId) => {
    const source = OFFICIAL_CONTEXT_BY_ID[id];
    if (id === "nws-forecast-wind") { setWindArrowReloadToken(value => value + 1); return; }
    if (source.apiPath) {
      const feed = id as OfficialContextFeedId;
      const archiveDay = officialArchiveDaysRef.current[feed];
      if (archiveDay) void loadOfficialArchiveDay(feed, archiveDay, true);
      else void refreshOfficialContext(feed);
      return;
    }
    if (id === "usgs-streamflow") { void refreshSelectedStreamflow(); return; }
    if (id === "noaa-nwps-gauges") { void refreshNoaaHydrologyNetwork(); return; }
    if (id === "nws-radar") { void refreshNoaaRadarManifest(); return; }
    if (id === "noaa-lightning-density") { setLightningPlaying(false); setLightningReloadToken((value) => value + 1); return; }
    if (id === "noaa-goes-geocolor") { void refreshNoaaSatelliteFrames(); return; }
    const map = mapRef.current;
    if (!map || !styleGenerationReadyRef.current) return;
    officialRasterFailuresRef.current.delete(id);
    if (id === "usgs-3dep-hillshade" || id === "usgs-3dep-slope") terrainRasterViewRef.current.reset(id);
    setOfficialErrors(current => ({ ...current, [id]: undefined }));
    setOfficialStates(current => ({ ...current, [id]: "loading" }));
    if (map.getSource(source.sourceId)) map.refreshTiles(source.sourceId);
    else setOfficialContextVisible(id, true);
    announce(`Retrying ${source.shortTitle}`);
  };

  const applyDomainLens = useCallback((domain: (typeof layerDomains)[number]) => {
    setLayerDomain(domain);
    if (domain === "ALL") {
      announce("Domain lens cleared; the current map layers remain unchanged");
      return;
    }
    const layerIds = LAYER_REGISTRY.filter((layer) => layer.domain === domain).map((layer) => layer.id);
    setVisibility((current) => {
      const next = { ...current };
      layerIds.forEach((id) => { next[id] = true; });
      visibilityRef.current = next;
      return next;
    });
    (DOMAIN_LIVE_CONTEXT[domain] ?? []).forEach((id) => setOfficialContextVisible(id, true));
    const liveDetail = (DOMAIN_LIVE_CONTEXT[domain] ?? []).length ? " and matched live context" : "";
    announce(`${domain} lens added ${layerIds.length} historical layer${layerIds.length === 1 ? "" : "s"}${liveDetail}; other map layers remain available`);
  }, [announce, setOfficialContextVisible]);

  const setOfficialContextOpacity = useCallback((id: OfficialContextId, value: number) => {
    const next = { ...officialOpacityRef.current, [id]: clamp(value, 0, 1) };
    officialOpacityRef.current = next;
    setOfficialOpacity(next);
    const map = mapRef.current;
    if (map && styleGenerationReadyRef.current) applyOfficialContextState(map, runtimeOfficialVisibility(officialVisibilityRef.current, temporalQueryRef.current.frame, noaaRadarReadyRef.current, noaaRadarFrameTimeRef.current), next, officialPayloadsRef.current);
  }, [runtimeOfficialVisibility]);
  // The context renderer draws the prisms on each pass while the map asks for them.
  useEffect(() => {
    const map = mapRef.current;
    if (!map) return;
    setPopulationPrisms(map, populationPrisms);
    if (styleReady && styleGenerationReadyRef.current) applyOfficialContextState(map, runtimeOfficialVisibility(officialVisibilityRef.current, temporalQueryRef.current.frame, noaaRadarReadyRef.current, noaaRadarFrameTimeRef.current), officialOpacityRef.current, officialPayloadsRef.current);
  }, [populationPrisms, styleReady, runtimeOfficialVisibility]);

  // The earthquake record replaces the 30-day catalog while it is shown, so one
  // colour scale is on the map at a time; hiding it brings the catalog back.
  const showQuakeRecord = useCallback((on: boolean) => {
    setQuakeRecordOn(on);
    setQuakeRecordYear(null);
    setQuakeRecordSelected(null);
    if (on) {
      setQuakeRecordFailed(false);
      quakeLiveWasOnRef.current = Boolean(officialVisibilityRef.current["usgs-earthquakes"]);
      if (quakeLiveWasOnRef.current) setOfficialContextVisible("usgs-earthquakes", false);
    } else if (quakeLiveWasOnRef.current) {
      quakeLiveWasOnRef.current = false;
      setOfficialContextVisible("usgs-earthquakes", true);
    }
  }, [setOfficialContextVisible]);
  useEffect(() => {
    if (!quakeRecordOn || quakeRecord || quakeRecordFailed) return;
    const controller = new AbortController();
    void fetch("/api/earthquake-record", { signal: controller.signal })
      .then(response => response.ok ? response.json() as Promise<unknown> : Promise.reject(new Error(`HTTP ${response.status}`)))
      .then(value => {
        if (controller.signal.aborted) return;
        if (!validEarthquakeRecord(value)) throw new Error("Invalid earthquake record.");
        quakeRecordEventsRef.current = new Map(value.events.map(event => [event.id, event]));
        setQuakeRecord(value);
        announce(`${value.events.length.toLocaleString("en-US")} Kansas earthquakes of magnitude ${value.minMagnitude} or more since ${value.startYear} are on the map, coloured by year`);
      })
      .catch(() => { if (!controller.signal.aborted) setQuakeRecordFailed(true); });
    return () => controller.abort();
  }, [quakeRecordOn, quakeRecord, quakeRecordFailed, announce]);
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !styleReady) return;
    const record = quakeRecordOn ? quakeRecord : null;
    const sync = () => {
      try { syncEarthquakeRecord(map, record, quakeRecordYear, quakeRecordSelected?.id ?? null); }
      catch { /* The style is reloading; its styledata event draws the record again. */ }
    };
    sync();
    if (!record) return;
    // A new style drops the record's source; put it back once the style has loaded.
    const restore = () => { if (map.isStyleLoaded() && !map.getSource(EARTHQUAKE_RECORD_SOURCE_ID)) sync(); };
    map.on("styledata", restore);
    return () => { map.off("styledata", restore); };
  }, [quakeRecordOn, quakeRecord, quakeRecordYear, quakeRecordSelected, styleReady]);
  // A day's outlook is read when it is first shown, and again each time it is a quarter-hour old.
  const OUTLOOK_REFRESH_MS = 15 * 60_000;
  const chooseOutlook = useCallback((day: OutlookDay | null) => { setOutlookDay(day); setOutlookFailed(null); }, []);
  const chooseOutlookHazard = useCallback((product: OutlookProduct) => { setOutlookHazard(product); setOutlookFailed(null); }, []);
  // Day 3 is categorical only; a hazard chosen there waits for day 1 or 2.
  const outlookProduct: OutlookProduct = outlookDay && outlookProducts(outlookDay).includes(outlookHazard) ? outlookHazard : "cat";
  const outlookId = outlookDay ? `${outlookDay}-${outlookProduct}` : null;
  useEffect(() => {
    if (!outlookDay || !outlookId || outlookFailed === outlookId) return;
    const current = outlooks[outlookId];
    const readAt = outlookReadAtRef.current.get(outlookId);
    const age = current && readAt !== undefined ? Date.now() - readAt : Infinity;
    if (age < OUTLOOK_REFRESH_MS) {
      // Fresh: come back when it is a quarter-hour old, while this day is still shown.
      const timer = setTimeout(() => setOutlookTick(tick => tick + 1), OUTLOOK_REFRESH_MS - age);
      return () => clearTimeout(timer);
    }
    const controller = new AbortController();
    void fetch(`/api/spc-outlook?day=${outlookDay}&product=${outlookProduct}`, { signal: controller.signal })
      .then(response => response.ok ? response.json() as Promise<unknown> : Promise.reject(new Error(`HTTP ${response.status}`)))
      .then(value => {
        if (controller.signal.aborted) return;
        if (!validSpcOutlook(value) || value.day !== outlookDay || value.product !== outlookProduct) throw new Error("Invalid SPC outlook.");
        outlookReadAtRef.current.set(outlookId, Date.now());
        setOutlooks(current => ({ ...current, [outlookId]: value }));
        announce(`SPC day ${value.day} ${value.product === "cat" ? "convective" : outlookProductName(value.product).toLowerCase()} outlook on the map: ${spcOutlookReading(value)}`);
      })
      .catch(() => { if (!controller.signal.aborted) setOutlookFailed(outlookId); });
    return () => controller.abort();
  }, [outlookDay, outlookProduct, outlookId, outlooks, outlookFailed, outlookTick, announce]);
  const shownOutlook = outlookId ? outlooks[outlookId] ?? null : null;
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !styleReady) return;
    const sync = () => {
      try { syncSpcOutlook(map, shownOutlook); }
      catch { /* The style is reloading; its styledata event draws the outlook again. */ }
    };
    sync();
    if (!shownOutlook) return;
    const restore = () => { if (map.isStyleLoaded() && !map.getSource(SPC_OUTLOOK_SOURCE_ID)) sync(); };
    map.on("styledata", restore);
    return () => { map.off("styledata", restore); };
  }, [shownOutlook, styleReady]);

  // Kansas's weekly drought shares since 2000: read when the Drought Monitor is shown, and again while it stays shown once they are six hours old.
  useEffect(() => {
    if (!droughtOn || droughtSeriesFailed) return;
    const age = droughtSeries ? Date.now() - droughtSeriesReadAtRef.current : Infinity;
    if (age < DROUGHT_SERIES_REFRESH_MS) {
      const timer = setTimeout(() => setDroughtTick(tick => tick + 1), DROUGHT_SERIES_REFRESH_MS - age);
      return () => clearTimeout(timer);
    }
    const controller = new AbortController();
    void fetch("/api/drought-series", { signal: controller.signal })
      .then(response => response.ok ? response.json() as Promise<unknown> : Promise.reject(new Error(`HTTP ${response.status}`)))
      .then(value => {
        if (controller.signal.aborted) return;
        if (!validDroughtSeries(value)) throw new Error("Invalid Drought Monitor statistics.");
        droughtSeriesReadAtRef.current = Date.now();
        setDroughtSeries(value);
      })
      .catch(() => {
        if (controller.signal.aborted) return;
        // A failed re-read keeps the series in hand and tries again after the same interval.
        if (droughtSeries) { droughtSeriesReadAtRef.current = Date.now(); setDroughtTick(tick => tick + 1); }
        else setDroughtSeriesFailed(true);
      });
    return () => controller.abort();
  }, [droughtOn, droughtSeries, droughtSeriesFailed, droughtTick]);
  const droughtId = droughtOn ? droughtWeek ?? "newest" : null;
  useEffect(() => {
    if (!droughtId || droughtFailed === droughtId) return;
    const current = droughtMaps.get(droughtId);
    if (current) {
      // A past week is kept as published; the newest is read again once it is an hour old, while it is shown.
      if (droughtId !== "newest") return;
      const age = Date.now() - (droughtReadAtRef.current.get(droughtId) ?? 0);
      if (age < DROUGHT_NEWEST_REFRESH_MS) {
        const timer = setTimeout(() => setDroughtTick(tick => tick + 1), DROUGHT_NEWEST_REFRESH_MS - age);
        return () => clearTimeout(timer);
      }
    }
    const controller = new AbortController();
    // A dragged week slider settles before its map is read.
    const timer = setTimeout(() => {
      void fetch(`/api/drought-monitor${droughtWeek ? `?date=${droughtWeek}` : ""}`, { signal: controller.signal })
        .then(response => response.ok ? response.json() as Promise<unknown> : Promise.reject(new Error(`HTTP ${response.status}`)))
        .then(value => {
          if (controller.signal.aborted) return;
          if (!validDroughtMap(value) || (droughtWeek !== null && value.date !== droughtWeek)) throw new Error("Invalid Drought Monitor map.");
          droughtReadAtRef.current.set(droughtId, Date.now());
          // A dozen weeks are kept for stepping back and forth; older ones are read again.
          setDroughtMaps(maps => rememberDroughtMap(maps, droughtId, value));
          if (droughtWeek === null && current?.date !== value.date) announce(`U.S. Drought Monitor on the map: ${droughtReading(value, null)}`);
        })
        .catch(() => {
          if (controller.signal.aborted) return;
          // A failed re-read of the newest keeps the map shown and tries again after the same interval.
          if (current) { droughtReadAtRef.current.set(droughtId, Date.now()); setDroughtTick(tick => tick + 1); }
          else setDroughtFailed(droughtId);
        });
    }, droughtWeek ? 350 : 0);
    return () => { clearTimeout(timer); controller.abort(); };
  }, [droughtId, droughtWeek, droughtMaps, droughtFailed, droughtTick, announce]);
  // While the next week loads, the last one drawn stays on the map, and its key with it.
  const droughtLoaded = droughtId ? droughtMaps.get(droughtId) ?? null : null;
  if (droughtLoaded) lastDroughtRef.current = droughtLoaded;
  else if (!droughtId || droughtFailed === droughtId) lastDroughtRef.current = null;
  const shownDrought = droughtId ? droughtLoaded ?? lastDroughtRef.current : null;
  // The Census counties the site already reads (for search and People) give the county lines and each county's shares.
  // They are asked for once each time the Drought Monitor is shown; a failed read leaves the map without county lines.
  useEffect(() => {
    if (!droughtOn || officialPayloads["census-counties"] || droughtCountiesAskedRef.current) return;
    droughtCountiesAskedRef.current = true;
    void refreshOfficialContext("census-counties");
  }, [droughtOn, officialPayloads, refreshOfficialContext]);
  const droughtCounties = droughtOn ? officialPayloads["census-counties"]?.data ?? null : null;
  const countyDrought = useMemo(() => droughtLoaded && droughtCounties ? countyDroughtShares(droughtLoaded.data, droughtCounties) : null, [droughtLoaded, droughtCounties]);
  const countyDroughtItems = useMemo(() => countyDrought ? countyDroughtList(countyDrought) : [], [countyDrought]);
  const pickedCountyDrought = droughtCounty ? countyDrought?.find(county => county.geoid === droughtCounty) ?? null : null;
  // A change view compares the week drawn with 4 or 12 weeks before it, as the USDM's change maps do; that week is read like any other.
  // A week too near the first map (2000-01-04) has no whole interval behind it, so no change is drawn for it.
  const droughtChangeFrom = droughtChange ? droughtChangeStart(droughtChange) : null;
  const droughtChangeTooEarly = Boolean(droughtChangeFrom && droughtLoaded && droughtLoaded.date < droughtChangeFrom);
  const droughtSinceDate = droughtChange && droughtLoaded && !droughtChangeTooEarly ? usdmWeeksBefore(droughtLoaded.date, droughtChange) : null;
  useEffect(() => {
    if (!droughtSinceDate || droughtMaps.has(droughtSinceDate) || droughtSinceFailed === droughtSinceDate) return;
    const controller = new AbortController();
    const timer = setTimeout(() => {
      void fetch(`/api/drought-monitor?date=${droughtSinceDate}`, { signal: controller.signal })
        .then(response => response.ok ? response.json() as Promise<unknown> : Promise.reject(new Error(`HTTP ${response.status}`)))
        .then(value => {
          if (controller.signal.aborted) return;
          if (!validDroughtMap(value) || value.date !== droughtSinceDate) throw new Error("Invalid Drought Monitor map.");
          setDroughtMaps(maps => rememberDroughtMap(maps, droughtSinceDate, value));
        })
        .catch(() => { if (!controller.signal.aborted) setDroughtSinceFailed(droughtSinceDate); });
    }, 350);
    return () => { clearTimeout(timer); controller.abort(); };
  }, [droughtSinceDate, droughtMaps, droughtSinceFailed]);
  const droughtSince = droughtSinceDate ? droughtMaps.get(droughtSinceDate) ?? null : null;
  const countyDroughtSince = useMemo(() => droughtSince && droughtCounties ? countyDroughtShares(droughtSince.data, droughtCounties) : null, [droughtSince, droughtCounties]);
  const countyChange = useMemo(() => countyDrought && countyDroughtSince ? countyDroughtChange(countyDrought, countyDroughtSince) : null, [countyDrought, countyDroughtSince]);
  const droughtChangeData = useMemo(() => countyChange && droughtCounties ? changeCollection(droughtCounties, countyChange) : null, [countyChange, droughtCounties]);
  // As with the categories, the change last drawn stays on the map while the next week and its earlier week load (each Play step),
  // and goes with a failed week, a week too near the first map, or another view.
  const freshDroughtChange = droughtChange && droughtChangeData && droughtSince && droughtLoaded ? { weeks: droughtChange, from: droughtSince.date, to: droughtLoaded.date, data: droughtChangeData } : null;
  if (freshDroughtChange) lastDroughtChangeRef.current = freshDroughtChange;
  else if (!droughtOn || droughtChange !== lastDroughtChangeRef.current?.weeks || droughtChangeTooEarly || (droughtId !== null && droughtFailed === droughtId)
    || (droughtSinceDate !== null && droughtSinceFailed === droughtSinceDate)) lastDroughtChangeRef.current = null;
  const shownDroughtChange = droughtChange ? freshDroughtChange ?? lastDroughtChangeRef.current : null;
  const pickedCountyChange = droughtCounty ? countyChange?.find(change => change.geoid === droughtCounty) ?? null : null;
  // Statewide, the USDM's own statistics are used for both weeks when they are in hand.
  const droughtSeriesShares = (date: string) => droughtSeries?.weeks.find(week => week.date === date)?.shares ?? null;
  const droughtChangeText = droughtChange && droughtLoaded && droughtSince ? droughtChangeReading(droughtSeriesShares(droughtLoaded.date) ?? droughtLoaded.kansas,
    droughtSeriesShares(droughtSince.date) ?? droughtSince.kansas, droughtChange, droughtSince.date, Boolean(droughtSeriesShares(droughtLoaded.date) && droughtSeriesShares(droughtSince.date))) : null;
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !styleReady) return;
    const sync = () => {
      try { syncDroughtMonitor(map, shownDrought, droughtCounties, droughtCounty, shownDroughtChange?.data ?? null); }
      catch { /* The style is reloading; its styledata event draws the map again. */ }
    };
    sync();
    if (!shownDrought) return;
    const restore = () => { if (map.isStyleLoaded() && !map.getSource(DROUGHT_SOURCE_ID)) sync(); };
    map.on("styledata", restore);
    return () => { map.off("styledata", restore); };
  }, [shownDrought, droughtCounties, droughtCounty, shownDroughtChange?.data, styleReady]);
  const pickDroughtCounty = (geoid: string) => {
    const feature = droughtCounties?.features.find(item => String(item.properties?.geoid ?? "") === geoid);
    const geometry = feature && countySearchGeometry(feature);
    if (!geometry) return;
    setDroughtCounty(geoid);
    mapRef.current?.fitBounds(geometry.bounds, { padding: 70, maxZoom: 9, duration: motionDuration(650) });
  };
  const droughtNewest = droughtMaps.get("newest")?.date ?? droughtSeries?.weeks.at(-1)?.date ?? null;
  const droughtDate = droughtWeek ?? droughtMaps.get("newest")?.date ?? null;
  const droughtChartWeeks = useMemo(() => droughtSeries?.weeks.map(week => ({ date: week.date, label: usdmDateLabel(week.date), shares: week.shares })) ?? null, [droughtSeries]);
  const chooseDroughtWeek = (date: string | null) => { setDroughtPlaying(false); setDroughtWeek(date && date !== droughtNewest ? date : null); setDroughtFailed(null); };
  // Play steps forward a week at a time, each week once it is drawn, and stops at the newest, on a failed week, or when the map closes.
  const droughtPlayStops = droughtPlaying && (!droughtOn || reducedMotion || droughtWeek === null || (droughtId !== null && droughtFailed === droughtId));
  if (droughtPlayStops) setDroughtPlaying(false);
  // In a change view, a step also waits for its earlier week (or that week's failure), so the change is drawn before Play moves on.
  const droughtSinceWaiting = droughtSinceDate !== null && !droughtSince && droughtSinceFailed !== droughtSinceDate;
  useEffect(() => {
    if (!droughtPlaying || droughtPlayStops || !droughtWeek || !droughtLoaded || droughtSinceWaiting) return;
    const timer = setTimeout(() => {
      const next = nextUsdmDate(droughtWeek);
      setDroughtWeek(droughtNewest && next >= droughtNewest ? null : next);
    }, DROUGHT_PLAY_STEP_MS);
    return () => clearTimeout(timer);
  }, [droughtPlaying, droughtPlayStops, droughtWeek, droughtLoaded, droughtSinceWaiting, droughtNewest]);
  const playDrought = (on: boolean) => {
    // From the newest, Play starts a year back.
    if (on && droughtWeek === null) {
      const from = droughtNewest ?? droughtDate;
      if (!from) return;
      setDroughtWeek(usdmWeeksBefore(from, DROUGHT_PLAY_WEEKS));
    }
    setDroughtFailed(null);
    setDroughtPlaying(on);
  };
  const showDrought = (on: boolean) => {
    setDroughtOn(on);
    setDroughtWeek(null);
    setDroughtFailed(null);
    setDroughtSeriesFailed(false);
    setDroughtCounty(null);
    setDroughtChange(0);
    setDroughtSinceFailed(null);
    droughtCountiesAskedRef.current = false;
    const map = mapRef.current;
    // The Drought Monitor is a statewide picture: a field-scale view pulls out to Kansas.
    if (on && map && map.getZoom() > 7.5) map.easeTo({ center: [-98.38, 38.5], zoom: 6.2, duration: motionDuration(1200), essential: false });
  };

  // NWS flood forecasts on the River network: the NWPS gauges by flood category, and one gauge's hydrograph,
  // read again every ten minutes while it is shown (observations every 15–60 minutes, forecasts a few times a day).
  floodOnRef.current = floodOn;
  const showFlood = (on: boolean) => {
    setFloodOn(on);
    setFloodLid(null);
    setFloodFailed(null);
    if (on) {
      floodGaugesWereOnRef.current = Boolean(officialVisibilityRef.current["noaa-nwps-gauges"]);
      if (!floodGaugesWereOnRef.current) setOfficialContextVisible("noaa-nwps-gauges", true);
    } else if (!floodGaugesWereOnRef.current) setOfficialContextVisible("noaa-nwps-gauges", false);
  };
  useEffect(() => {
    if (!floodOn || !floodLid) return;
    const controller = new AbortController();
    const read = () => {
      setFloodClock(Date.now());
      void fetch(floodGaugeApiPath(floodLid), { signal: controller.signal })
        .then(response => response.ok ? response.json() as Promise<unknown> : Promise.reject(new Error(`HTTP ${response.status}`)))
        .then(value => {
          if (controller.signal.aborted) return;
          setFloodGauge(parseFloodGauge(value, floodLid));
          setFloodFailed(null);
        })
        .catch(() => { if (!controller.signal.aborted) setFloodFailed(floodLid); });
    };
    read();
    const timer = setInterval(read, FLOOD_GAUGE_REFRESH_MS);
    return () => { clearInterval(timer); controller.abort(); };
  }, [floodOn, floodLid]);
  const floodGaugeFeatures = floodOn ? officialPayloads["noaa-nwps-gauges"]?.data.features ?? null : null;
  const floodSummaries = useMemo(() => floodGaugeFeatures ? floodGaugeSummaries(floodGaugeFeatures) : [], [floodGaugeFeatures]);
  const floodItems = useMemo(() => floodGaugeList(floodSummaries), [floodSummaries]);
  const shownFloodGauge = floodGauge && floodGauge.lid === floodLid ? floodGauge : null;
  const floodPlot = useMemo(() => shownFloodGauge ? floodHydrograph(shownFloodGauge, floodClock) : null, [shownFloodGauge, floodClock]);
  const floodPoint = useMemo(() => {
    const feature = floodLid ? floodGaugeFeatures?.find(item => item.properties?.lid === floodLid) : undefined;
    return feature?.geometry?.type === "Point" ? feature.geometry.coordinates as [number, number] : null;
  }, [floodGaugeFeatures, floodLid]);
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !styleReady) return;
    const point = floodOn ? floodPoint : null;
    const sync = () => { try { syncFloodSelection(map, point); } catch { /* The style is reloading; its styledata event draws the ring again. */ } };
    sync();
    if (!point) return;
    const restore = () => { if (map.isStyleLoaded() && !map.getSource(FLOOD_SELECTED_SOURCE_ID)) sync(); };
    map.on("styledata", restore);
    return () => { map.off("styledata", restore); };
  }, [floodOn, floodPoint, styleReady]);
  const pickFloodGauge = (lid: string) => {
    setFloodLid(lid);
    setFloodFailed(null);
    const feature = floodGaugeFeatures?.find(item => item.properties?.lid === lid);
    if (feature?.geometry?.type === "Point") easeToPicked(feature.geometry.coordinates as [number, number]);
  };

  // Today's reports are re-read every five minutes while shown; yesterday's every half hour.
  const chooseReports = useCallback((day: ReportDay | null) => { setReportsDay(day); setReportsFailed(null); setReportSelected(null); }, []);
  useEffect(() => {
    if (!reportsDay || reportsFailed === reportsDay) return;
    const current = stormReports[reportsDay];
    const refresh = reportsDay === "today" ? 5 * 60_000 : 30 * 60_000;
    const readAt = reportsReadAtRef.current.get(reportsDay);
    const age = current && readAt !== undefined ? Date.now() - readAt : Infinity;
    if (age < refresh) {
      const timer = setTimeout(() => setReportsTick(tick => tick + 1), refresh - age);
      return () => clearTimeout(timer);
    }
    const controller = new AbortController();
    void fetch(`/api/storm-reports?day=${reportsDay}`, { signal: controller.signal })
      .then(response => response.ok ? response.json() as Promise<unknown> : Promise.reject(new Error(`HTTP ${response.status}`)))
      .then(value => {
        if (controller.signal.aborted) return;
        if (!validStormReports(value) || value.day !== reportsDay) throw new Error("Invalid SPC storm reports.");
        reportsReadAtRef.current.set(value.day, Date.now());
        setStormReports(current => ({ ...current, [value.day]: value }));
        // A refresh carries the selected report's latest form, or drops it if SPC withdrew it.
        setReportSelected(selected => selected ? value.reports.find(report => report.id === selected.id) ?? null : null);
        announce(`SPC storm reports on the map: ${stormReportsReading(value)}`);
      })
      .catch(() => { if (!controller.signal.aborted) setReportsFailed(reportsDay); });
    return () => controller.abort();
  }, [reportsDay, stormReports, reportsFailed, reportsTick, announce]);
  const shownReports = reportsDay ? stormReports[reportsDay] ?? null : null;
  // Today's reports against the Day 1 outlook shown, as SPC verifies it; null when the two do not cover the same day.
  const outlookCheck = useMemo(() => {
    const check = shownOutlook && shownReports ? verifyOutlook(shownOutlook, shownReports) : null;
    return check && shownOutlook ? verificationReading(check, shownOutlook.product) : null;
  }, [shownOutlook, shownReports]);
  useEffect(() => { stormReportsRef.current = new Map((shownReports?.reports ?? []).map(report => [report.id, report])); }, [shownReports]);
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !styleReady) return;
    const sync = () => {
      try { syncStormReports(map, shownReports, reportSelected?.id ?? null); }
      catch { /* The style is reloading; its styledata event draws the reports again. */ }
    };
    sync();
    if (!shownReports) return;
    const restore = () => { if (map.isStyleLoaded() && !map.getSource(STORM_REPORTS_SOURCE_ID)) sync(); };
    map.on("styledata", restore);
    return () => { map.off("styledata", restore); };
  }, [shownReports, reportSelected, styleReady]);

  const refreshVisibleOfficialContext = useCallback(() => {
    if (!buildYearCurrentRef.current) {
      announce("This site build does not match the UTC year; rebuild before refreshing current sources");
      return;
    }
    const plan = planOfficialRefresh(OFFICIAL_CONTEXT_SOURCES, officialVisibilityRef.current, temporalQueryRef.current.frame, OFFICIAL_CONTEXT_PRESENT_FRAME, Boolean(streamflowArchiveDayRef.current), officialArchiveDaysRef.current);
    if (plan.reason === "historical") {
      announce(`Current sources are held at ${formatTimelineStep(temporalQueryRef.current.frame)}; switch to Present to refresh`);
      return;
    }
    if (plan.reason === "none") {
      announce("Select a refreshable current source before refreshing");
      return;
    }
    plan.feeds.forEach((feed) => { void refreshOfficialContext(feed as OfficialContextFeedId); });
    if (plan.radar) void refreshNoaaRadarManifest(true);
    if (plan.satellite) void refreshNoaaSatelliteFrames(true);
    if (plan.lightning) setLightningReloadToken((value) => value + 1);
    if (plan.streamflow) void refreshStreamflow(streamflowRange, streamflowSelectedStationId, true);
    if (plan.hydrology) void refreshNoaaHydrologyNetwork(true);
    announce(`Refreshing ${plan.count} selected official connection${plan.count === 1 ? "" : "s"}`);
  }, [announce, refreshNoaaHydrologyNetwork, refreshNoaaRadarManifest, refreshNoaaSatelliteFrames, refreshOfficialContext, refreshStreamflow, streamflowRange, streamflowSelectedStationId]);

  const hideAllOfficialContext = useCallback(() => {
    setSoilMapState(current => hideSoilContext(current));
    for (const [feed, controller] of officialRequestsRef.current) {
      controller.abort();
      setOfficialStates(current => ({ ...current, [feed]: officialPayloadsRef.current[feed]?.state ?? "idle" }));
    }
    officialRequestsRef.current.clear();
    const next = Object.fromEntries(OFFICIAL_CONTEXT_SOURCES.map((source) => [source.id, false])) as Record<OfficialContextId, boolean>;
    officialVisibilityRef.current = next;
    setOfficialVisibility(next);
    setNoaaRadarPlaying(false);
    setLightningPlaying(false);
    setStreamflowPlaying(false);
    const map = mapRef.current;
    if (map && styleGenerationReadyRef.current) applyOfficialContextState(map, runtimeOfficialVisibility(next, temporalQueryRef.current.frame, noaaRadarReadyRef.current, noaaRadarFrameTimeRef.current), officialOpacityRef.current, officialPayloadsRef.current);
    announce("Official context hidden; loaded snapshots remain available on this page");
  }, [announce, runtimeOfficialVisibility]);

  useEffect(() => {
    const refresh = () => {
      const day = currentUtcDay();
      setBaselineDay(day);
      if (!buildYearCurrentRef.current || document.hidden || temporalQueryRef.current.frame !== OFFICIAL_CONTEXT_PRESENT_FRAME) return;
      for (const source of OFFICIAL_CONTEXT_SOURCES) {
        if (source.apiPath && officialVisibilityRef.current[source.id]) void refreshOfficialContext(source.id as OfficialContextFeedId);
      }
    };
    const timer = window.setInterval(refresh, 300_000);
    const visible = () => { if (!document.hidden) refresh(); };
    const online = () => {
      if (buildYearCurrentRef.current && !document.hidden && officialVisibilityRef.current["census-counties"]
        && temporalQueryRef.current.frame === OFFICIAL_CONTEXT_PRESENT_FRAME) void refreshOfficialContext("census-counties");
    };
    document.addEventListener("visibilitychange", visible);
    window.addEventListener("online", online);
    return () => { clearInterval(timer); document.removeEventListener("visibilitychange", visible); window.removeEventListener("online", online); };
  }, [refreshOfficialContext]);

  useEffect(() => {
    // Fixed provider URLs otherwise stay in MapLibre's tile cache for the
    // whole visit. Revalidate only selected current rasters at their display
    // cadence; exact radar and GeoColor frames have separate dated schedulers.
    const cadence = {
      "noaa-nwm-analysis": 15 * 60_000,
      "noaa-nwm-short-range": 15 * 60_000,
      "nasa-firms-active-fire": 60 * 60_000,
      "usgs-3dhp-hydrography": 60 * 60_000,
      "usgs-3dep-hillshade": 6 * 60 * 60_000,
      "usgs-3dep-slope": 6 * 60 * 60_000,
    } satisfies Partial<Record<OfficialContextId, number>>;
    const last = new Map<OfficialContextId, number>();
    const refresh = () => {
      const map = mapRef.current;
      if (!buildYearCurrentRef.current || document.hidden || !map || !styleGenerationReadyRef.current || !map.isStyleLoaded()
        || projectionRef.current === "globe" || temporalQueryRef.current.frame !== OFFICIAL_CONTEXT_PRESENT_FRAME) return;
      const now = Date.now();
      for (const [id, milliseconds] of Object.entries(cadence) as [OfficialContextId, number][]) {
        const source = OFFICIAL_CONTEXT_BY_ID[id];
        if (!officialVisibilityRef.current[id] || !map.getSource(source.sourceId) || officialRasterFailuresRef.current.has(id)) {
          last.delete(id);
          continue;
        }
        const previous = last.get(id);
        if (previous === undefined) { last.set(id, now); continue; }
        if (now - previous < milliseconds) continue;
        last.set(id, now);
        if (id === "usgs-3dep-hillshade" || id === "usgs-3dep-slope") {
          terrainRasterViewRef.current.reset(id);
          setOfficialStates(current => ({ ...current, [id]: "loading" }));
        }
        map.refreshTiles(source.sourceId);
      }
    };
    const timer = window.setInterval(refresh, 60_000);
    document.addEventListener("visibilitychange", refresh);
    return () => { window.clearInterval(timer); document.removeEventListener("visibilitychange", refresh); };
  }, []);

  useEffect(() => {
    if (!buildYearCurrent || calendarSweep || temporalQuery.frame !== OFFICIAL_CONTEXT_PRESENT_FRAME) {
      for (const [feed, controller] of officialRequestsRef.current) {
        if (officialArchiveDaysRef.current[feed]) continue;
        controller.abort(); officialRequestsRef.current.delete(feed);
        setOfficialStates(current => ({ ...current, [feed]: officialPayloadsRef.current[feed]?.state ?? "idle" }));
      }
      return;
    }
    // Hydrate selected current sources on first entry and when returning from history.
    // Archived and historical frames never initiate a current-source request.
    const timer = window.setTimeout(() => {
      for (const source of OFFICIAL_CONTEXT_SOURCES) {
        if (source.apiPath && (officialVisibilityRef.current[source.id] || searchNeedsCounties(source.id))) void refreshOfficialContext(source.id as OfficialContextFeedId);
      }
    }, 40);
    return () => window.clearTimeout(timer);
  }, [buildYearCurrent, calendarSweep, officialArchiveDays, refreshOfficialContext, temporalQuery.frame]);

  const dismissMapUtilityWithoutFocus = useCallback(() => {
    mapUtilityReturnRef.current = null;
    setMapUtilityOpen(false);
    setMapQueryCandidates([]);
  }, []);

  const openQwenCompanion = useCallback((returnElement?: HTMLElement | null, focusTarget: "close" | "composer" = "close") => {
    qwenReturnRef.current = returnElement
      ?? (document.activeElement instanceof HTMLElement ? document.activeElement : null);
    setPrimaryWorkspace("map");
    setGuideOpen(false);
    setWelcomeSourcesOpen(false);
    setQwenOpen(true);
    setHelpOpen(false);
    dismissMapUtilityWithoutFocus();
    if (isCompact) {
      setLeftOpen(false);
      setRightOpen(false);
      setTimelineOpen(false);
    }
    window.setTimeout(() => {
      // One opening action owns one focus destination. Find must not compete
      // with a second delayed callback that sends its first keys to Close.
      const target = focusTarget === "composer" ? globalSearchInputRef.current
        : qwenPanelRef.current?.querySelector<HTMLButtonElement>(isCompact ? '.inspection-map' : '[aria-label="Close Qwen companion"]');
      target?.focus({ preventScroll: true });
    }, 0);
  }, [dismissMapUtilityWithoutFocus, isCompact, setQwenOpen, setRightOpen]);

  const openAtlasComposer = useCallback((intent: "find" | "explore", value?: string, returnElement?: HTMLElement | null) => {
    setPrimaryWorkspace("map");
    openQwenCompanion(returnElement, "composer");
    setAssistantDraftRequest(current => ({id:(current?.id ?? 0)+1, value:value ?? globalSearchInputRef.current?.value ?? "", intent}));
  }, [openQwenCompanion]);

  useEffect(() => {
    if (new URLSearchParams(window.location.search).get("kfm-chat") === "1") {
      const timer = window.setTimeout(() => { openQwenCompanion(null); }, 0);
      return () => window.clearTimeout(timer);
    }
  }, [openQwenCompanion]);

  const openEvidencePanel = useCallback(() => {
    dismissMapUtilityWithoutFocus();
    setRightOpen(true);
    if (isCompact) { setLeftOpen(false); setTimelineOpen(false); }
    window.setTimeout(() => rightPanelRef.current?.querySelector<HTMLButtonElement>('[aria-label="Close Evidence Drawer"]')?.focus({ preventScroll: true }), 0);
  }, [dismissMapUtilityWithoutFocus, isCompact, setRightOpen]);

  const inspectAssistantSources = (context: AssistantContext, returnElement?: HTMLElement) => {
    // The rich inspector owns the active selection. Never replace that selection
    // with a previous answer's scope; old answers retain their own source links.
    if (JSON.stringify(context) !== JSON.stringify(assistantFocus.context) || (!selected && !subsurfaceInspection)) return false;
    assistantEvidenceReturnRef.current = returnElement ?? globalSearchInputRef.current;
    setResearchOpen(false);
    openEvidencePanel();
    return true;
  };

  const closeQwenCompanion = useCallback((returnElement?: HTMLElement | null) => {
    const returnTarget = returnElement ?? qwenReturnRef.current;
    qwenReturnRef.current = null;
    setQwenOpen(false);
    window.setTimeout(() => {
      if (returnTarget?.isConnected && returnTarget.getClientRects().length > 0) returnTarget.focus({ preventScroll: true });
      else mapContainerRef.current?.focus({ preventScroll: true });
    }, 0);
  }, []);

  useEffect(() => {
    if (!qwenOpen || !isCompact) return;
    const panel = qwenPanelRef.current;
    if (!panel) return;
    const focusable = () => visibleFocusableElements(panel);
    const shell = panel.closest(".site-root");
    const background: HTMLElement[] = [];
    let activeBranch: Element = panel;
    let activeContainer = panel.parentElement;
    while (activeContainer) {
      for (const element of activeContainer.children) {
        if (element !== activeBranch
          && !element.classList.contains("qwen-modal-backdrop")
          && element instanceof HTMLElement && !element.inert
          && element.getAttribute("aria-hidden") !== "true") background.push(element);
      }
      if (activeContainer === shell) break;
      activeBranch = activeContainer;
      activeContainer = activeContainer.parentElement;
    }
    const priorBackgroundState = background.map((element) => ({
      element,
      inert: element.inert,
      ariaHidden: element.getAttribute("aria-hidden"),
    }));
    for (const element of background) {
      element.inert = true;
      element.setAttribute("aria-hidden", "true");
    }
    if (!panel.contains(document.activeElement)) focusable()[0]?.focus({ preventScroll: true });
    const handleFocusIn = (event: FocusEvent) => {
      if (event.target instanceof Node && !panel.contains(event.target)) {
        focusable()[0]?.focus({ preventScroll: true });
      }
    };
    const handleKey = (event: KeyboardEvent) => {
      if (event.key === "Escape") {
        event.preventDefault();
        event.stopPropagation();
        closeQwenCompanion();
        return;
      }
      if (event.key !== "Tab") return;
      const items = focusable();
      if (!items.length) {
        event.preventDefault();
        return;
      }
      const first = items[0];
      const last = items[items.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    };
    document.addEventListener("focusin", handleFocusIn, true);
    panel.addEventListener("keydown", handleKey);
    return () => {
      document.removeEventListener("focusin", handleFocusIn, true);
      panel.removeEventListener("keydown", handleKey);
      for (const { element, inert, ariaHidden } of priorBackgroundState) {
        element.inert = inert;
        if (ariaHidden === null) element.removeAttribute("aria-hidden");
        else element.setAttribute("aria-hidden", ariaHidden);
      }
    };
  }, [closeQwenCompanion, isCompact, qwenOpen]);

  const stopSceneOrbit = useCallback((notify = true) => {
    const cancel = sceneOrbitCancelRef.current;
    sceneOrbitCancelRef.current = null;
    cancel?.();
    if (sceneOrbitTimerRef.current !== null) {
      window.clearTimeout(sceneOrbitTimerRef.current);
      sceneOrbitTimerRef.current = null;
    }
    mapRef.current?.stop();
    setSceneOrbiting(false);
    if (notify) announce("3D orbit stopped at the current camera");
  }, [announce]);

  const stopFlyover = useCallback((notify = true) => {
    const cancel = flyoverCancelRef.current;
    flyoverCancelRef.current = null;
    cancel?.();
    setFlyoverStopIndex(null);
    if (notify && cancel) announce("Flyover stopped · you have the camera");
  }, [announce]);

  const applyComparisonTime = useCallback((nextYear: number, label: "A" | "B") => {
    setPlaying(false);
    setTemporalMode("snapshot");
    commitTemporalFrame(nextYear);
    announce(`Applied Time ${label}: ${formatTimelineStep(nextYear)} to the map`);
  }, [announce, commitTemporalFrame]);

  const copyTemporalComparison = useCallback(async () => {
    try {
      await navigator.clipboard.writeText(JSON.stringify(temporalComparison, null, 2));
      announce("Time A / Time B catalog comparison copied with no public effect");
    } catch {
      announce("Clipboard access was blocked; the temporal comparison stayed in the browser");
    }
  }, [announce, temporalComparison]);

  const activateDrawerView = useCallback((nextView: DrawerView, focusTab = false) => {
    setDrawerView(nextView);
    if (focusTab) {
      const nextIndex = drawerViews.indexOf(nextView);
      window.setTimeout(() => drawerTabRefs.current[nextIndex]?.focus(), 0);
    }
  }, []);

  const handleDrawerTabKeyDown = useCallback((event: React.KeyboardEvent<HTMLButtonElement>, index: number) => {
    let nextIndex: number | null = null;
    if (event.key === "ArrowRight" || event.key === "ArrowDown") nextIndex = (index + 1) % drawerViews.length;
    if (event.key === "ArrowLeft" || event.key === "ArrowUp") nextIndex = (index - 1 + drawerViews.length) % drawerViews.length;
    if (event.key === "Home") nextIndex = 0;
    if (event.key === "End") nextIndex = drawerViews.length - 1;
    if (nextIndex === null) return;
    event.preventDefault();
    activateDrawerView(drawerViews[nextIndex], true);
  }, [activateDrawerView]);

  const copyFocusReceipt = async () => {
    if (!selected) return;
    const issuedAt = new Date();
    const receipt = {
      format: "kfm-focus-session-receipt-v1",
      authority: "SITE_LOCAL_DEMONSTRATION",
      issued_at: issuedAt.toISOString(),
      expires_at: new Date(issuedAt.getTime() + 15 * 60 * 1000).toISOString(),
      context_is_evidence: false,
      context: {
        workspace: currentWorkspace,
        feature_id: selected.featureId,
        layer_id: selected.layerId,
        spatial_scope: selected.properties.spatialScope,
        active_time: year,
        source_time: selected.properties.year,
        temporal_mode: selected.layer.temporal?.mode ?? "untimed",
        camera: locationDerivedViewRef.current
          ? { center: "WITHHELD_BROWSER_LOCATION", zoom: "WITHHELD", bearing: "WITHHELD", pitch: "WITHHELD", projection }
          : { center: view.center, zoom: view.zoom, bearing: view.bearing, pitch: view.pitch, projection },
        visible_layer_ids: activeLayers.map((layer) => layer.id),
        evidence_refs: [selected.properties.citation],
        release_posture: selected.properties.releaseState,
        review_posture: selected.properties.reviewState,
        freshness: selected.properties.freshnessState,
        geometry: "OMITTED_FROM_RECEIPT",
      },
      request_profile: {
        profile: "site-local-map-selection-v1",
        request_id: `focus:${selected.featureId}:${year}`,
        claim_id: `site-fixture:${selected.featureId}`,
        question: FOCUS_INTENTS.find((intent) => intent.id === focusIntent)?.label ?? "Explain current context",
        allowed_evidence_refs: [selected.properties.citation],
      },
      transport: { free_text: false, browser_to_model_call: false },
      resolution: {
        evidence_state: selected.properties.evidenceState,
        finite_outcome: activeFocus.outcome,
        reason_code: activeFocus.code,
        closure_checks: focusGates.map((gate) => ({ id: gate.id, state: gate.state, detail: gate.detail })),
      },
      effects: { policy: "NONE", review: "NONE", release: "NONE", publication: "NONE" },
      limitations: [
        "Context is not proof or authority.",
        "This receipt describes a deterministic site-local fixture response, not an authenticated KFM runtime.",
        "No protected geometry, raw source record, credential, consent grant, or model output is included.",
      ],
    };
    try {
      await navigator.clipboard.writeText(JSON.stringify(receipt, null, 2));
      announce("Focus context receipt copied · expires in 15 minutes");
    } catch {
      announce("Clipboard access was blocked; no receipt left the browser");
    }
  };

  const applyFocusAction = useCallback((proposal: FocusActionProposal) => {
    if (!selected) return;
    setPendingFocusAction(null);
    if (proposal.kind === "SET_TIME") {
      if (proposal.targetYear === undefined || !TIME_STEPS.includes(proposal.targetYear as (typeof TIME_STEPS)[number])) {
        announce("The proposed source year is not an available Explorer time step");
        return;
      }
      setPlaying(false);
      commitTemporalFrame(proposal.targetYear);
      announce(`Applied view-only time change to ${formatTimelineStep(proposal.targetYear)}`);
      return;
    }
    if (proposal.kind === "CENTER_SELECTION") {
      mapRef.current?.easeTo({
        center: [selected.properties.focusLng, selected.properties.focusLat],
        zoom: Math.max(mapRef.current.getZoom(), 7),
        duration: motionDuration(650),
      });
      announce("Applied camera-only Focus action");
      return;
    }
    if (proposal.kind === "OPEN_SOURCES") {
      setSourceObservatoryView("gaps");
      setRepositoryView("sources");
      setRepositoryOpen(true);
      announce("Opened discovery gaps; no source was admitted");
      return;
    }
    const targetView: DrawerView = proposal.kind === "OPEN_METADATA" ? "metadata" : proposal.kind === "OPEN_LINEAGE" ? "lineage" : "evidence";
    activateDrawerView(targetView, true);
    announce("Applied review-navigation action only");
  }, [activateDrawerView, announce, commitTemporalFrame, selected]);

  const closeRepository = useCallback(() => {
    setRepositoryOpen(false);
    setCurrentWorkspace(rightOpen && selectedRef.current ? "trust" : "explore");
    window.setTimeout(() => (repositoryButtonRef.current?.closest("details")?.querySelector<HTMLElement>("summary") ?? repositoryButtonRef.current)?.focus(), 0);
  }, [rightOpen]);

  const closeMapGuide = useCallback(() => {
    setHelpOpen(false);
    if (mapGuideRef.current?.contains(document.activeElement)) {
      document.querySelector<HTMLButtonElement>(".guide-trigger")?.focus({ preventScroll: true });
    }
  }, []);

  useEffect(() => {
    if (!helpOpen) return;
    mapGuideRef.current?.querySelector<HTMLButtonElement>('[aria-label="Close map guide"]')?.focus({ preventScroll: true });
  }, [helpOpen]);

  const closeLiveInstrument = useCallback(() => {
    setInstrumentOpen(false);
    setStreamflowPlaying(false);
    setNoaaRadarPlaying(false);
    setLightningPlaying(false);
    window.requestAnimationFrame(() => mapContainerRef.current?.focus({ preventScroll: true }));
  }, []);

  const closeRightPanel = useCallback(() => {
    const assistantReturn = assistantEvidenceReturnRef.current;
    assistantEvidenceReturnRef.current = null;
    if (assistantReturn) {
      setQwenOpen(true);
      window.setTimeout(() => (assistantReturn.isConnected ? assistantReturn : globalSearchInputRef.current)?.focus({preventScroll:true}), 0);
      return;
    }
    setRightOpen(false);
    setCurrentWorkspace("explore");
    const returnTarget = returnFocusRef.current;
    returnFocusRef.current = null;
    window.setTimeout(() => {
      const targetIsUsable = returnTarget?.isConnected && !returnTarget.closest("[inert]");
      (targetIsUsable ? returnTarget : mapContainerRef.current)?.focus();
    }, 0);
  }, [setQwenOpen, setRightOpen]);

  const closeLeftPanel = useCallback(() => {
    setLeftOpen(false);
    setCurrentWorkspace("explore");
    const returnTarget = leftPanelReturnRef.current;
    leftPanelReturnRef.current = null;
    window.setTimeout(() => modalReturnTarget(returnTarget, mapContainerRef.current)?.focus({ preventScroll: true }), 0);
  }, []);

  const toggleTimelinePanel = useCallback(() => {
    setPrimaryWorkspace("map");
    setTimelineOpen((open) => primaryWorkspace !== "map" || !open);
  }, [primaryWorkspace]);

  const closeTimelinePanel = useCallback(() => {
    setTimelineOpen(false);
    setPlaying(false);
    window.setTimeout(() => mapContainerRef.current?.focus(), 0);
  }, []);

  const openSourceStatus = useCallback((returnElement?: HTMLElement | null) => {
    setPrimaryWorkspace("map");
    setGuideOpen(false);
    sourceStatusReturnRef.current = returnElement
      ?? (document.activeElement instanceof HTMLElement ? document.activeElement : mapContainerRef.current);
    if (!returnElement?.closest(".layer-panel")) leftPanelReturnRef.current = returnElement ?? null;
    setMapUtilityOpen(false);
    setRightOpen(false);
    setScenePanelOpen(false);
    setLeftPanelMode("layers");
    setSourceStatusOpen(true);
    setLeftOpen(true);
    window.requestAnimationFrame(() => {
      sourceStatusPanelRef.current?.querySelector<HTMLButtonElement>('[aria-label="Back to layers"]')?.focus({ preventScroll: true });
    });
  }, [setRightOpen]);

  const closeSourceStatus = useCallback((returnElement?: HTMLElement | null) => {
    setSourceStatusOpen(false);
    const returnTarget = returnElement ?? sourceStatusReturnRef.current;
    sourceStatusReturnRef.current = null;
    window.setTimeout(() => {
      const targetIsUsable = returnTarget?.isConnected
        && !returnTarget.closest("[inert]")
        && returnTarget.getClientRects().length > 0;
      (targetIsUsable ? returnTarget : returnTarget?.closest("details")?.querySelector<HTMLElement>("summary") ?? mapContainerRef.current)?.focus({ preventScroll: true });
    }, 0);
  }, []);

  const closeMapUtility = useCallback(() => {
    setMapUtilityOpen(false);
    setMapQueryCandidates([]);
    const returnTarget = mapUtilityReturnRef.current;
    mapUtilityReturnRef.current = null;
    window.setTimeout(() => {
      const targetIsUsable = returnTarget?.isConnected && !returnTarget.closest("[inert]");
      (targetIsUsable ? returnTarget : mapContainerRef.current)?.focus();
    }, 0);
  }, [setQwenOpen, setRightOpen]);

  const openMapUtility = useCallback((nextView: MapUtilityView, returnElement?: HTMLElement | null) => {
    setPrimaryWorkspace("map");
    mapUtilityReturnRef.current = returnElement ?? null;
    setScenePanelOpen(false);
    setMapUtilityView(nextView === "navigate" ? "scene" : nextView);
    setMapUtilityOpen(true);
    setMapUtilityFocusRequest((request) => request + 1);
    setCurrentWorkspace("explore");
    if (nextView === "export") setExportGeneratedAt(new Date().toISOString());
    if (nextView === "report") setReportGeneratedAt(new Date().toISOString());
    setHelpOpen(false);
    setSourceStatusOpen(false);
    setMapContextOpen(false);
    setLeftOpen(false);
    setRightOpen(false);
    if (isCompact) setTimelineOpen(false);
  }, [isCompact]);

  const openSelectedReport = (returnElement?: HTMLElement | null) => {
    if (selected?.kind === "basemap") {
      // The retained title must obey the same projection as exported context:
      // hiding it only during export would leak it after selection changes.
      const providerSelection = buildProviderReportSelection({
        selected, timeMismatch: selectedTimeMismatch,
        locationPrivate: locationCameraRedacted || locationDerivedViewRef.current || researchLocationRedacted || subsurfacePrivate,
        source: selectedOfficialConnection?.source, attributes: selectedArtifactAttributes, attributesCurrent: selectedAttributesCurrent,
        sourceState: selectedRiverObservation?.status ?? selectedOfficialConnection?.state, sourceUrl: selectedRiverObservation?.sourceUrl,
        observedAt: selectedRiverObservation?.observedAt, providerUpdatedAt: selectedOfficialPayload?.upstreamUpdatedAt,
        retrievedAt: selectedRiverObservation?.retrievedAt ?? selectedOfficialConnection?.retrievedAt,
        limitation: selectedOfficialPayload?.limitation ?? selectedOfficialConnection?.limitation,
      });
      setReportScope("SELECTION");
      setReportTitle(providerSelection?.status === "AVAILABLE" && providerSelection.context
        ? `${providerSelection.context.title.slice(0, 65)} · source context`
        : providerSelection?.status === "INCOMPATIBLE" ? "Incompatible source-context report" : "Withheld source-context report");
      setReportQuery("");
      setReportEvidenceFilter("ALL");
      openMapUtility("report", returnElement);
      return;
    }
    openPrimaryWorkspace("reports", true, null, researchContext);
  };

  useEffect(() => {
    if (primaryWorkspace !== "map" || !mapUtilityOpen) return;
    // Wait for the committed workspace and the panel's first opening paint.
    // A repeated request must also re-enter retained controls after a menu closes.
    let focusFrame: number | undefined;
    const commitFrame = window.requestAnimationFrame(() => {
      focusFrame = window.requestAnimationFrame(() => {
        const panel = mapUtilityPanelRef.current;
        if (panel) visibleFocusableElements(panel)[0]?.focus({ preventScroll: true });
      });
    });
    return () => {
      window.cancelAnimationFrame(commitFrame);
      if (focusFrame !== undefined) window.cancelAnimationFrame(focusFrame);
    };
  }, [primaryWorkspace, mapUtilityOpen, mapUtilityView, mapUtilityFocusRequest]);

  const openAtlasPanel = useCallback((mode: LeftPanelMode, returnElement?: HTMLElement | null) => {
    leftPanelReturnRef.current = returnElement ?? null;
    setPrimaryWorkspace("map");
    if (primaryWorkspace !== "map" && !sourceSearchFocusPendingRef.current) window.setTimeout(() => {
      const panel = leftPanelRef.current;
      if (panel) visibleFocusableElements(panel)[0]?.focus({ preventScroll: true });
    }, 0);
    setMapContextOpen(false);
    setCurrentWorkspace("knowledge");
    setLeftPanelMode(mode);
    setLeftOpen(true);
    setRightOpen(false);
    dismissMapUtilityWithoutFocus();
    if (isCompact) setTimelineOpen(false);
  }, [dismissMapUtilityWithoutFocus, isCompact, primaryWorkspace]);

  const openMapSettings = useCallback(() => {
    openMapUtility("scene");
  }, [openMapUtility]);

  useEffect(() => {
    if (!pendingCatalogTarget || debouncedLayerQuery.trim()) return;
    const frame = window.requestAnimationFrame(() => {
      if (pendingCatalogTarget === "earth-engine-context-controls") leftPanelRef.current?.querySelector<HTMLDetailsElement>(".reviewed-imagery-section")?.setAttribute("open", "");
      const target = document.getElementById(pendingCatalogTarget);
      target?.focus({ preventScroll: true });
      target?.scrollIntoView({ behavior: reducedMotion ? "auto" : "smooth", block: "start" });
      setPendingCatalogTarget(null);
    });
    return () => window.cancelAnimationFrame(frame);
  }, [debouncedLayerQuery, pendingCatalogTarget, reducedMotion]);

  const openEarthEngineLayers = useCallback(() => {
    setLayerQuery("");
    openAtlasPanel("layers");
    setStarterPanelOpen(false);
    setLayerCatalogView("local");
    setPendingCatalogTarget("earth-engine-context-controls");
    announce("Opened installed Earth Engine layers");
  }, [announce, openAtlasPanel]);

  useEffect(() => {
    const handleWorkspaceShortcut = (event: KeyboardEvent) => {
      if (event.defaultPrevented || event.metaKey || event.ctrlKey || event.altKey) return;
      const target = event.target as HTMLElement | null;
      const isEditing = target?.matches("input, textarea, select, [contenteditable='true']");
      if (event.key === "/" && !isEditing) {
        event.preventDefault();
        openAtlasComposer("find");
        return;
      }
      if (isEditing) return;
      if (event.key.toLowerCase() === "r") {
        event.preventDefault();
        openMapUtility("report");
      }
      if (event.key.toLowerCase() === "l") {
        event.preventDefault();
        setPrimaryWorkspace("map");
        dismissMapUtilityWithoutFocus();
        setLeftPanelMode("layers");
        setLeftOpen((current) => primaryWorkspace !== "map" || !current);
        if (isCompact) { setRightOpen(false); setTimelineOpen(false); }
      }
    };
    document.addEventListener("keydown", handleWorkspaceShortcut);
    return () => document.removeEventListener("keydown", handleWorkspaceShortcut);
  }, [dismissMapUtilityWithoutFocus, isCompact, openMapUtility, openAtlasComposer, primaryWorkspace]);

  const openLayerCatalogFromUtility = useCallback(() => {
    mapUtilityReturnRef.current = null;
    setMapUtilityOpen(false);
    setMapQueryCandidates([]);
    setLeftPanelMode("layers");
    setLeftOpen(true);
    setCurrentWorkspace("knowledge");
    setRightOpen(false);
    if (isCompact) setTimelineOpen(false);
    window.setTimeout(() => leftPanelRef.current?.querySelector<HTMLElement>("button:not([disabled]), input:not([disabled]), select:not([disabled])")?.focus(), 0);
  }, [isCompact]);

  const openSelection = useCallback((context: SelectedContext, returnElement?: HTMLElement | null) => {
    setSubsurfaceInspection(null);
    if (hoverDrawerTimerRef.current !== null) window.clearTimeout(hoverDrawerTimerRef.current);
    hoverDrawerTimerRef.current = null;
    hoverCandidateIdRef.current = null;
    setHoverSummary(null);
    setHoverActive(false);
    returnFocusRef.current = returnElement ?? null;
    mapUtilityReturnRef.current = null;
    setMapUtilityOpen(false);
    setMapQueryCandidates([]);
    setFocusStage("outcome");
    setFocusIntent("explain");
    setPendingFocusAction(null);
    selectedRef.current = context;
    setSelected(context);
    setResearchOpen(false);
    setDrawerView("evidence");
    // A real canvas resize invalidates the Scene sample. Retain the selection
    // now, but defer changing panel occupancy until active sampling finishes.
    const deferSurfaceEvidence = surfaceInspectionOpen && returnElement === mapContainerRef.current;
    surfaceEvidencePendingRef.current = deferSurfaceEvidence;
    if (!deferSurfaceEvidence) setRightOpen(true);
    setCurrentWorkspace("trust");
    if (isCompact && !deferSurfaceEvidence) {
      setLeftOpen(false);
      setTimelineOpen(false);
    }
  }, [isCompact, surfaceInspectionOpen, setRightOpen]);
  useEffect(() => { openSelectionRef.current = openSelection; }, [openSelection]);

  const selectStoredFeature = useCallback((layerId: string, featureId: string, returnElement?: HTMLElement | null) => {
    const layer = LAYER_REGISTRY.find((candidate) => candidate.id === layerId);
    if (!layer) return;
    const context = copyFeature(layer, featureId);
    if (!context) return;
    setVisibility((current) => ({ ...current, [layerId]: true }));
    openSelection(context, returnElement);
    const focus: [number, number] = [context.properties.focusLng, context.properties.focusLat];
    mapRef.current?.easeTo({ center: focus, zoom: Math.max(mapRef.current.getZoom(), 7), duration: window.matchMedia("(prefers-reduced-motion: reduce)").matches ? 0 : 700 });
    if (mapRef.current?.isStyleLoaded()) {
      const mismatch = !isFeatureAvailableForTemporalQuery(context.layer, context.properties.year, temporalQueryRef.current);
      const filtered = mapEvidenceFilterRef.current !== "ALL" && context.properties.evidenceState !== mapEvidenceFilterRef.current;
      updateSelectionSource(mapRef.current, mismatch || filtered ? null : context.geometry);
    }
  }, [openSelection]);

  const captureMapSnapshot = useCallback((): MapSnapshot => {
    const createdAt = new Date().toISOString();
    const representation: MapSnapshot["representation"] = mapUtilityOpen && mapUtilityView === "compare"
      ? "Compare"
      : scenePreset === "elevation-3d"
        ? "Terrain 3D"
        : projection === "globe"
          ? "Globe"
          : "2D";
    const redactCamera = locationCameraRedacted || locationDerivedViewRef.current;
    // Report snapshots persist only registry identities; external provider picks
    // travel in a separate, explicitly non-evidentiary context record.
    const capturedSelection = selected?.kind === "registry" && !selectedTimeMismatch ? selected : null;
    const evidenceRefs = Array.from(new Set([
      ...mapContextRecords.map((feature) => feature.properties.citation),
      ...(capturedSelection ? [capturedSelection.properties.citation] : []),
    ]));
    const selectedTrustState = capturedSelection ? trustStateFromEvidenceState(capturedSelection.properties.evidenceState, capturedSelection.properties.sourceRole) : undefined;
    const capturedSweepMode: TemporalSweepMode = representation === "Compare" ? "comparison" : temporalMode;
    const capturedSweepFrame = capturedSweepMode === "comparison" ? compareTimeB : temporalQuery.frame;
    const capturedRangeStart = capturedSweepMode === "comparison" ? Math.min(compareTimeA, compareTimeB) : temporalQuery.rangeStart;
    const capturedRangeEnd = capturedSweepMode === "comparison" ? Math.max(compareTimeA, compareTimeB) : temporalQuery.rangeEnd;
    return {
      id: `snapshot-${globalThis.crypto?.randomUUID?.() ?? Date.now()}`,
      createdAt,
      area: redactCamera && !capturedSelection
        ? { kind: "viewport", label: "Map extent withheld after browser location" }
        : capturedSelection
        ? { kind: "selection", label: `${capturedSelection.properties.title} · ${capturedSelection.properties.spatialScope}` }
        : analysisArea
          ? { kind: "aoi", label: "Locked browser-local area of interest", bounds: { ...analysisArea } }
          : { kind: "viewport", label: "Current Kansas map viewport", bounds: { ...mapViewportBounds } },
      camera: redactCamera
        ? { center: "WITHHELD_BROWSER_LOCATION", zoom: "WITHHELD", bearing: "WITHHELD", pitch: "WITHHELD" }
        : { center: [...view.center] as [number, number], zoom: view.zoom, bearing: view.bearing, pitch: view.pitch },
      representation,
      ...(representation === "Terrain 3D" ? { terrainProvider, terrainExaggeration: verticalExaggeration } : {}),
      projection,
      basemap,
      evidenceFilter: mapEvidenceFilter,
      temporalSweep: {
        mode: capturedSweepMode,
        frame: capturedSweepFrame,
        rangeStart: capturedRangeStart,
        rangeEnd: capturedRangeEnd,
        windowStart: capturedSweepMode === "moving-window" ? temporalQuery.windowStart : capturedRangeStart,
        windowFrames: movingWindowFrames,
        stepRule: temporalStepRule,
        interpolation: false,
      },
      committedTime: representation === "Compare"
        ? {
          start: Math.min(compareTimeA, compareTimeB),
          end: Math.max(compareTimeA, compareTimeB),
          label: `${formatTimelineStep(compareTimeA)} ↔ ${formatTimelineStep(compareTimeB)} · discrete comparison`,
          mode: "interval",
          uncertainty: "Catalog availability comparison only; no interpolation or observed-change claim.",
        }
        : temporalMode === "moving-window" || temporalMode === "accumulation"
          ? {
            start: temporalMode === "moving-window" ? temporalQuery.windowStart : temporalQuery.rangeStart,
            end: temporalQuery.frame,
            label: `${formatTimelineStep(temporalMode === "moving-window" ? temporalQuery.windowStart : temporalQuery.rangeStart)} ↔ ${formatTimelineStep(temporalQuery.frame)} · ${temporalMode.replace("-", " ")}`,
            mode: temporalMode === "accumulation" ? "cumulative" : "interval",
            uncertainty: "Feature-filtered site context only; no interpolation, resampling, causal inference, or source admission.",
          }
          : { start: temporalQuery.frame, end: temporalQuery.frame, label: `${formatTimelineStep(temporalQuery.frame)} · ${timelineEraLabel(temporalQuery.frame, buildYearCurrent)}`, mode: "instant" },
      visibleLayers: layerOrder
        .filter((layerId) => visibility[layerId])
        .flatMap((layerId, order) => {
          const layer = LAYER_REGISTRY.find((candidate) => candidate.id === layerId);
          return layer ? [{ id: layer.id, title: layer.title, domain: layer.domain, order, opacity: opacity[layer.id] ?? layer.defaultOpacity, trustState: trustStateForLayer(layer) }] : [];
        }),
      selection: capturedSelection && selectedTrustState ? {
        featureId: capturedSelection.featureId,
        layerId: capturedSelection.layerId,
        title: capturedSelection.properties.title,
        evidenceReference: capturedSelection.properties.citation,
        trustState: selectedTrustState,
      } : null,
      evidenceRefs,
      inspectableFeatureIds: mapContextRecords.map((feature) => feature.properties.fid),
      inspectableRecordCount: mapContextRecords.length,
      sourceBackedCount: supportedMapContextCount,
      boundedCount: Math.max(0, mapContextRecords.length - supportedMapContextCount),
      policy: policyDecisionFromEvidenceState(capturedSelection?.properties.evidenceState),
    };
  }, [analysisArea, basemap, buildYearCurrent, compareTimeA, compareTimeB, layerOrder, locationCameraRedacted, mapContextRecords, mapEvidenceFilter, mapUtilityOpen, mapUtilityView, mapViewportBounds, movingWindowFrames, opacity, projection, scenePreset, selected, selectedTimeMismatch, supportedMapContextCount, temporalMode, temporalQuery, temporalStepRule, terrainProvider, verticalExaggeration, view, visibility]);


  const openPrimaryWorkspace = useCallback((mode: Exclude<PrimaryWorkspace, "map">, freshFromMap = false, fireContext: FireReportContext | null = null, research: ResearchContext | null = null, subsurface: SubsurfaceContext | null = null) => {
    // A same-mode header action must not replace an unsaved editor with an
    // older stored snapshot. Explicit fresh composition remains intentional.
    if (!freshFromMap && primaryWorkspace === mode && workspaceSnapshot) return;
    // Each workspace owns its saved snapshot. Reusing the other mode's ID can
    // initialize a blank draft and overwrite an unrelated saved investigation.
    const savedSnapshot = freshFromMap ? null : readDraftSnapshot(mode);
    setWorkspaceSnapshot(savedSnapshot ?? captureMapSnapshot());
    setFireReportContext(mode === "reports" ? fireContext : null);
    setResearchReportContext(mode === "reports" ? persistableResearch(research && { ...research, capturedAt: new Date().toISOString() }, researchLocationRedacted || locationCameraRedacted || locationDerivedViewRef.current) ?? null : null);
    setSubsurfaceReportContext(mode === "reports" ? persistableSubsurface(subsurface && { ...subsurface, capturedAt: new Date().toISOString() }, subsurfacePrivate || locationCameraRedacted || locationDerivedViewRef.current) ?? null : null);
    setPrimaryWorkspace(mode);
    setMapContextOpen(false);
    setHelpOpen(false);
    setQwenOpen(false);
    setPlaying(false);
    setStreamflowPlaying(false);
    setNoaaRadarPlaying(false);
    setLightningPlaying(false);
    setDaylightPlayback(false);
    announce(savedSnapshot
      ? `${mode === "reports" ? "Report" : "Story"} draft resumed with its saved map snapshot`
      : `${mode === "reports" ? "Report" : "Story"} workspace opened from the current governed map state`);
  }, [announce, captureMapSnapshot, locationCameraRedacted, primaryWorkspace, researchLocationRedacted, setDaylightPlayback, subsurfacePrivate, workspaceSnapshot]);

  const returnToPrimaryMap = useCallback(() => {
    setPrimaryWorkspace("map");
    window.setTimeout(() => mapContainerRef.current?.focus(), 0);
  }, []);

  const closeHeaderOverflow = useCallback((action: HTMLElement, restoreTriggerFocus = true) => {
    const menu = action.closest("details");
    const summary = menu?.querySelector<HTMLElement>("summary");
    menu?.removeAttribute("open");
    if (!restoreTriggerFocus) return;
    window.setTimeout(() => {
      // A workspace or compact panel may already have taken focus after commit.
      // Restore the menu trigger only when its closing action left focus behind.
      if (document.activeElement === document.body || menu?.contains(document.activeElement)) summary?.focus({ preventScroll: true });
    }, 0);
  }, []);

  const inspectWorkspaceEvidence = useCallback((record: EvidenceRecord) => {
    setPrimaryWorkspace("map");
    selectStoredFeature(record.layerId, record.featureId);
  }, [selectStoredFeature]);

  const applyStoryScene = useCallback((scene: StoryScene) => {
    const snapshot = scene.snapshot;
    const snapshotSweep = snapshot.temporalSweep;
    const sceneFrame = snapshotSweep?.frame ?? snapshot.committedTime.end;
    const sceneSweepMode: TemporalSweepMode = snapshotSweep?.mode ?? (snapshot.representation === "Compare" ? "comparison" : "snapshot");
    const referencedRecord = allEvidenceRecords.find((record) => scene.evidenceRefs.includes(record.citation));
    const visibleIds = new Set(snapshot.visibleLayers.map((layer) => layer.id));
    if (referencedRecord) visibleIds.add(referencedRecord.layerId);
    const nextVisibility = Object.fromEntries(LAYER_REGISTRY.map((layer) => [layer.id, visibleIds.has(layer.id)]));
    const nextOpacity = { ...opacity };
    for (const layer of snapshot.visibleLayers) nextOpacity[layer.id] = layer.opacity;
    const nextOrder = [
      ...snapshot.visibleLayers.map((layer) => layer.id),
      ...layerOrder.filter((layerId) => !snapshot.visibleLayers.some((layer) => layer.id === layerId)),
    ];
    visibilityRef.current = nextVisibility;
    opacityRef.current = nextOpacity;
    orderRef.current = nextOrder;
    yearRef.current = sceneFrame;
    projectionRef.current = snapshot.projection;
    const snapshotBasemap = Object.prototype.hasOwnProperty.call(BASEMAPS, snapshot.basemap)
      ? snapshot.basemap as BasemapKey
      : "standard";
    basemapRef.current = snapshotBasemap;
    setVisibility(nextVisibility);
    setOpacity(nextOpacity);
    setLayerOrder(nextOrder);
    setYear(sceneFrame);
    setPreviewYear(sceneFrame);
    setPlaying(false);
    setTemporalMode(sceneSweepMode);
    setTemporalStepRule(snapshotSweep?.stepRule ?? "regular-calendar");
    setSweepRangeStart(snapshotSweep?.rangeStart ?? Math.min(snapshot.committedTime.start, sceneFrame));
    setSweepRangeEnd(snapshotSweep?.rangeEnd ?? Math.max(snapshot.committedTime.end, sceneFrame));
    setMovingWindowFrames(snapshotSweep?.windowFrames ?? 3);
    setProjection(snapshot.projection);
    setBasemap(snapshotBasemap);
    if (snapshot.representation === "Terrain 3D" && snapshot.terrainProvider && snapshot.terrainExaggeration !== undefined) {
      terrainProviderRef.current = snapshot.terrainProvider;
      verticalExaggerationRef.current = snapshot.terrainExaggeration;
      setTerrainProvider(snapshot.terrainProvider);
      setVerticalExaggeration(snapshot.terrainExaggeration);
    }
    setAnalysisArea(snapshot.area.kind === "aoi" && snapshot.area.bounds ? { ...snapshot.area.bounds } : null);
    setScenePreset(snapshot.representation === "Terrain 3D" ? "elevation-3d" : snapshot.projection === "globe" ? "globe-overview" : "overview-2d");
    setMapEvidenceFilter(snapshot.evidenceFilter ?? "ALL");
    mapEvidenceFilterRef.current = snapshot.evidenceFilter ?? "ALL";
    setCompareTimeA(snapshot.comparison?.timeA ?? snapshot.committedTime.start);
    setCompareTimeB(snapshot.comparison?.timeB ?? sceneFrame);
    setMapUtilityView(snapshot.representation === "Compare" ? "compare" : "scene");
    setMapUtilityOpen(snapshot.representation === "Compare");
    setPrimaryWorkspace("map");
    if (mapRef.current) applyProjectionNavigationLimits(mapRef.current, snapshot.projection);
    if (snapshot.camera.center !== "WITHHELD_BROWSER_LOCATION") {
      mapRef.current?.easeTo({
        center: [...snapshot.camera.center] as [number, number],
        zoom: snapshot.camera.zoom as number,
        bearing: snapshot.camera.bearing as number,
        pitch: snapshot.camera.pitch as number,
        duration: motionDuration(scene.motion === "none" ? 0 : 650),
      });
    }
    const sceneSelection = snapshot.selection;
    const sceneLayer = sceneSelection ? LAYER_REGISTRY.find((layer) => layer.id === sceneSelection.layerId) : undefined;
    const context = sceneLayer && sceneSelection ? copyFeature(sceneLayer, sceneSelection.featureId) : null;
    selectedRef.current = context;
    setSelected(context);
    setRightOpen(Boolean(context));
    if (mapRef.current?.isStyleLoaded()) updateSelectionSource(mapRef.current, context?.geometry ?? null);
    announce(`Opened story scene “${scene.title}” on the map; evidence and policy state remain unchanged`);
  }, [allEvidenceRecords, announce, layerOrder, opacity]);

  const clearSelectionState = useCallback(() => {
    setFocusStage("outcome");
    setFocusIntent("explain");
    setPendingFocusAction(null);
    selectedRef.current = null;
    returnFocusRef.current = null;
    setSelected(null);
    setRightOpen(false);
    if (mapRef.current?.isStyleLoaded()) updateSelectionSource(mapRef.current, null);
  }, []);

  const clearSelection = useCallback(() => {
    clearSelectionState();
    announce("Selection cleared");
  }, [announce, clearSelectionState]);

  useEffect(() => {
    const media = window.matchMedia("(max-width: 1100px)");
    const update = () => {
      setIsCompact(media.matches);
      if (media.matches && !compactRef.current) {
        setLeftOpen(false);
        setRightOpen(false);
        setTimelineOpen(false);
      }
      compactRef.current = media.matches;
    };
    update();
    media.addEventListener("change", update);
    return () => media.removeEventListener("change", update);
  }, []);

  const restoreExplorerFromUrl = useCallback(() => {
      cancelSmokePlayback();
      const params = explorerHistoryParams(window.location.search, window.history.state);
      const hasDestination = hasExplorerDestination(params, new URLSearchParams(window.location.search));
      if (!explorerRestoredRef.current) {
        // Decide from the same incoming URL/saved view that owns restoration,
        // before view serialization can add default camera parameters.
        setGuideOpen(!hasDestination && !readExplorerGuideDismissed());
        setWelcomeSourcesOpen(false);
      } else if (hasDestination) {
        // Back/Forward can restore a destination while manual help is open.
        // Do not strand keyboard focus in the removed guide or save an opt-out.
        if (document.activeElement?.closest(".explorer-guide")) {
          document.querySelector<HTMLButtonElement>(".guide-trigger")?.focus({ preventScroll: true });
        }
        setGuideOpen(false);
      }
      setStarterPanelOpen(!params.has("layerView") && !params.has("topic"));
      const restoredTopic = restoreTopic(params.get("topic"));
      setOfficialWorkspace(restoredTopic);
      setLayerCatalogView(params.get("layerView") === "imagery" ? "local" : params.get("layerView") === "selected" ? "selected" : "official");
      if (restoredTopic !== "all") { setLeftPanelMode("layers"); setLeftOpen(true); }
      const restoredSolar = restoreDaylightView(params.get("sunDay"), params.get("sunAt"), params.get("sun") === "on", currentKansasCalendarDay(), params.get("sunThrough"));
      daylightDayRef.current = restoredSolar.day;
      daylightThroughDayRef.current = restoredSolar.throughDay;
      daylightInstantRef.current = restoredSolar.instantMs;
      daylightEnabledRef.current = restoredSolar.enabled;
      daylightPlayingRef.current = false;
      setDaylightDay(restoredSolar.day);
      setDaylightThroughDay(restoredSolar.throughDay);
      setDaylightInstant(restoredSolar.instantMs);
      setDaylightEnabled(restoredSolar.enabled);
      setDaylightPlaying(restoredSolar.playing);
      if (mapRef.current && styleGenerationReadyRef.current) {
        setDaylightMapLayer(mapRef.current, restoredSolar.enabled, restoredSolar.instantMs);
      }
      const restoringGlobe = params.get("proj") === "globe";
      const centerParam = params.get("c")?.split(",").map((token) => token.trim() === "" ? Number.NaN : Number(token));
      const center: [number, number] = centerParam?.length === 2 && centerParam.every(Number.isFinite)
        ? [clamp(centerParam[0], restoringGlobe ? -180 : -104.8, restoringGlobe ? 180 : -92), clamp(centerParam[1], restoringGlobe ? -85 : 34.8, restoringGlobe ? 85 : 42.2)]
        : KANSAS_VIEW.center;
      const restoredView: ViewState = {
        center,
        zoom: clamp(parseNumber(params.get("z"), KANSAS_VIEW.zoom), restoringGlobe ? 0 : 4, 16),
        bearing: clamp(parseNumber(params.get("b"), KANSAS_VIEW.bearing), -180, 180),
        pitch: clamp(parseNumber(params.get("p"), KANSAS_VIEW.pitch), 0, 85),
      };
      const restoredCameraRedaction = params.get("privacy") === "location-camera-redacted";
      locationDerivedViewRef.current = restoredCameraRedaction;
      setLocationCameraRedacted(restoredCameraRedaction);
      pendingViewRef.current = restoredView;
      setView(restoredView);
      cameraHistoryRef.current = [restoredView];
      cameraHistoryIndexRef.current = 0;
      setCameraHistoryIndex(0);
      setCameraHistoryLength(1);
      if (mapRef.current) applyProjectionNavigationLimits(mapRef.current, restoringGlobe ? "globe" : "mercator");
      if (params.get("scene") === "elevation-3d") mapRef.current?.setMaxPitch(72);
      mapRef.current?.jumpTo(restoredView);
      const analysisTokens = params.get("aoi")?.split(",").map((token) => token.trim() === "" ? Number.NaN : Number(token));
      const restoredAnalysisArea = !restoredCameraRedaction && analysisTokens?.length === 4 && analysisTokens.every(Number.isFinite)
        ? {
          west: clamp(analysisTokens[0], SUPPORTED_CONTEXT_BOUNDS.west, SUPPORTED_CONTEXT_BOUNDS.east),
          south: clamp(analysisTokens[1], SUPPORTED_CONTEXT_BOUNDS.south, SUPPORTED_CONTEXT_BOUNDS.north),
          east: clamp(analysisTokens[2], SUPPORTED_CONTEXT_BOUNDS.west, SUPPORTED_CONTEXT_BOUNDS.east),
          north: clamp(analysisTokens[3], SUPPORTED_CONTEXT_BOUNDS.south, SUPPORTED_CONTEXT_BOUNDS.north),
        }
        : null;
      const nextAnalysisArea = restoredAnalysisArea && restoredAnalysisArea.west < restoredAnalysisArea.east && restoredAnalysisArea.south < restoredAnalysisArea.north
        ? restoredAnalysisArea
        : null;
      analysisAreaRef.current = nextAnalysisArea;
      setAnalysisArea(nextAnalysisArea);
      if (mapRef.current?.isStyleLoaded()) updateAnalysisAreaSource(mapRef.current, nextAnalysisArea);

      const knownLayerIds = new Set(LAYER_REGISTRY.map((layer) => layer.id));
      const visibleIds = params.get("l")?.split(",").filter((id) => knownLayerIds.has(id)) ?? [];
      const restoredVisibility = params.has("l")
        ? Object.fromEntries(LAYER_REGISTRY.map((layer) => [layer.id, visibleIds.includes(layer.id)]))
        : defaultVisibility;
      visibilityRef.current = restoredVisibility;
      setVisibility(restoredVisibility);
      const opacityPairs = params.get("o")?.split(",").map((pair) => pair.split(":")) ?? [];
      const restoredOpacity = Object.fromEntries(opacityPairs
        .filter(([id, value]) => knownLayerIds.has(id) && typeof value === "string" && value.trim() !== "" && Number.isFinite(Number(value)))
        .map(([id, value]) => [id, clamp(Number(value), 0, 1)]));
      const nextOpacity = { ...defaultOpacity, ...restoredOpacity };
      opacityRef.current = nextOpacity;
      setOpacity(nextOpacity);
      const knownOfficialIds = new Set<OfficialContextId>(OFFICIAL_CONTEXT_SOURCES.map((source) => source.id));
      const preferredIds = preferredContextIds(params, readContextPreference(OFFICIAL_CONTEXT_SOURCES));
      const restoredOfficialIds = preferredIds?.filter((id): id is OfficialContextId => knownOfficialIds.has(id as OfficialContextId)) ?? [];
      const nextOfficialVisibility = preferredIds !== null
        ? Object.fromEntries(OFFICIAL_CONTEXT_SOURCES.map((source) => [source.id, restoredOfficialIds.includes(source.id)])) as Record<OfficialContextId, boolean>
        : defaultOfficialVisibility;
      officialVisibilityRef.current = nextOfficialVisibility;
      setOfficialVisibility(nextOfficialVisibility);
      const restoredDays = restoreArchiveViewDays(params.get("ctxd"), currentUtcDay());
      for (const feed of new Set([...Object.keys(officialArchiveDaysRef.current), ...Object.keys(restoredDays)]) as Set<OfficialContextFeedId>) {
        if (officialArchiveDaysRef.current[feed] === restoredDays[feed as keyof typeof restoredDays]) continue;
        officialRequestsRef.current.get(feed)?.abort();
        officialRequestsRef.current.delete(feed);
        officialPayloadsRef.current = { ...officialPayloadsRef.current, [feed]: undefined };
        officialArchivePayloadsRef.current = { ...officialArchivePayloadsRef.current, [feed]: undefined };
      }
      officialArchiveDaysRef.current = restoredDays;
      setOfficialArchiveDays(restoredDays);
      setOfficialArchiveDraftDays({ "noaa-hms-smoke": currentUtcDay(), ...restoredDays });
      setOfficialPayloads(officialPayloadsRef.current);
      setSoilMapState(restoreSoilMapState(params));
      setPopulationPrismsShown(params.get("prisms") === "on");
      // A shared record view hid the 30-day catalog; leaving the record brings it back.
      quakeLiveWasOnRef.current = params.get("quakes") === "record" && restoredTopic !== "all" && Boolean(categoryMap(restoredTopic)?.tools?.includes("quakes"));
      setQuakeRecordOn(quakeLiveWasOnRef.current);
      const restoredOutlook = Number(params.get("outlook"));
      setOutlookDay((restoredOutlook === 1 || restoredOutlook === 2 || restoredOutlook === 3) && restoredTopic !== "all" && categoryMap(restoredTopic)?.tools?.includes("outlook") ? restoredOutlook : null);
      const restoredReports = params.get("reports");
      setReportsDay((restoredReports === "today" || restoredReports === "yesterday") && restoredTopic !== "all" && categoryMap(restoredTopic)?.tools?.includes("reports") ? restoredReports : null);
      const restoredDrought = params.get("drought");
      const droughtOffered = restoredTopic !== "all" && Boolean(categoryMap(restoredTopic)?.tools?.includes("drought"));
      setDroughtOn(droughtOffered && (restoredDrought === "newest" || isUsdmDate(restoredDrought)));
      setDroughtWeek(droughtOffered && isUsdmDate(restoredDrought) ? restoredDrought : null);
      const restoredHazard = params.get("outlookHazard");
      setOutlookHazard(isOutlookProduct(restoredHazard) ? restoredHazard : "cat");
      const officialOpacityPairs = params.get("ctxo")?.split(",").map((pair) => pair.split(":")) ?? [];
      const restoredOfficialOpacity = Object.fromEntries(officialOpacityPairs
        .filter(([id, value]) => knownOfficialIds.has(id as OfficialContextId) && typeof value === "string" && value.trim() !== "" && Number.isFinite(Number(value)))
        .map(([id, value]) => [id, clamp(Number(value), 0, 1)]));
      const nextOfficialOpacity = { ...defaultOfficialOpacity, ...restoredOfficialOpacity };
      officialOpacityRef.current = nextOfficialOpacity;
      setOfficialOpacity(nextOfficialOpacity);
      const restoredRadarSpan = params.get("radarSpan");
      setNoaaRadarLoopSpan(restoredRadarSpan === "all" ? "all" : restoredRadarSpan === "30" || restoredRadarSpan === "120" ? Number(restoredRadarSpan) as NoaaRadarLoopSpanMinutes : 60);
      const restoredRadarSpeed = Number(params.get("radarSpeed"));
      setNoaaRadarPlaybackSpeed(restoredRadarSpeed === 0.5 || restoredRadarSpeed === 2 ? restoredRadarSpeed : 1);
      const restoredRadarTime = params.get("radarTime");
      const normalizedRadarTime = restoredRadarTime && Number.isFinite(Date.parse(restoredRadarTime))
        ? new Date(Date.parse(restoredRadarTime)).toISOString()
        : null;
      noaaRadarRequestedTimeRef.current = normalizedRadarTime;
      const restoredRadarFollowLatest = params.get("radarFollow") !== "selected";
      noaaRadarFollowLatestRef.current = restoredRadarFollowLatest;
      setNoaaRadarFollowLatest(restoredRadarFollowLatest);
      setNoaaRadarPlaying(false);
      const restoredHydroStation = params.get("hydroStation");
      const normalizedHydroStation = restoredHydroStation ? normalizeUsgsStationId(restoredHydroStation) : null;
      const requestedHydroRange = params.get("hydroRange");
      const candidateHydroRange: HydrologyRange = requestedHydroRange === "7d" || requestedHydroRange === "30d" || requestedHydroRange === "1y" ? requestedHydroRange : "24h";
      const restoredHydroDay = restoreStreamflowArchiveDay(params.get("hydroDay"), normalizedHydroStation, currentUtcDay());
      const restoredHydroRange: HydrologyRange = restoredHydroDay || candidateHydroRange !== "24h" && !normalizedHydroStation ? "24h" : candidateHydroRange;
      streamflowArchiveDayRef.current = restoredHydroDay;
      setStreamflowArchiveDay(restoredHydroDay);
      setStreamflowArchiveDraftDay(restoredHydroDay ?? currentUtcDay());
      const restoredHydroSpeed = Number(params.get("hydroSpeed"));
      const normalizedHydroTime = params.get("hydroTime") && Number.isFinite(Date.parse(params.get("hydroTime")!))
        ? new Date(Date.parse(params.get("hydroTime")!)).toISOString()
        : null;
      streamflowRequestedTimeRef.current = normalizedHydroTime;
      setStreamflowRange(restoredHydroRange);
      setStreamflowSelectedStationId(normalizedHydroStation);
      setStreamflowPlaybackSpeed(restoredHydroSpeed === 0.5 || restoredHydroSpeed === 2 ? restoredHydroSpeed : 1);
      setStreamflowPlaying(false);
      const restoredLiveInstrument = params.get("live");
      setLiveInstrument(restoredLiveInstrument === "radar" || restoredLiveInstrument === "lightning" ? restoredLiveInstrument : "river");
      for (const source of OFFICIAL_CONTEXT_SOURCES) {
        if (!nextOfficialVisibility[source.id] || !source.apiPath) continue;
        const feed = source.id as OfficialContextFeedId, day = officialArchiveDaysRef.current[feed];
        if (day) void loadOfficialArchiveDay(feed, day);
        else if (!officialPayloadsRef.current[feed]) void refreshOfficialContext(feed);
      }
      const restoredCalendar = readCalendarSweep(params.get("calendar"), currentUtcDay());
      calendarSeekGeneration.current++; calendarSweepRef.current = restoredCalendar; setCalendarSweep(restoredCalendar);
      const restoredYear = Number(params.get("t"));
      const nextYear = restoredCalendar ? Number(calendarFrameDay(restoredCalendar).slice(0, 4)) : KNOWN_TEMPORAL_FRAMES.has(restoredYear) ? restoredYear : OFFICIAL_CONTEXT_PRESENT_FRAME;
      yearRef.current = nextYear;
      setYear(nextYear);
      setPreviewYear(nextYear);
      if (nextOfficialVisibility["nws-radar"] && nextYear === OFFICIAL_CONTEXT_PRESENT_FRAME) void refreshNoaaRadarManifest(true);
      if (nextOfficialVisibility["usgs-streamflow"] && nextYear === OFFICIAL_CONTEXT_PRESENT_FRAME) void refreshStreamflow(restoredHydroRange, normalizedHydroStation, true, restoredHydroDay);
      if (nextOfficialVisibility["noaa-nwps-gauges"] && nextYear === OFFICIAL_CONTEXT_PRESENT_FRAME) void refreshNoaaHydrologyNetwork(true);
      const restoredTemporalMode = params.get("tm");
      const nextTemporalMode: TemporalSweepMode = restoredTemporalMode === "moving-window" || restoredTemporalMode === "event-stepping" || restoredTemporalMode === "accumulation" || restoredTemporalMode === "comparison" ? restoredTemporalMode : "snapshot";
      setTemporalMode(restoredCalendar ? "snapshot" : nextTemporalMode);
      setTemporalStepRule(params.get("tstep") === "available-events" ? "available-events" : "regular-calendar");
      const restoredSweepRange = params.get("trange")?.split(",").map(Number) ?? [];
      const validSweepRange = restoredSweepRange.length === 2
        && restoredSweepRange.every((value) => TIME_STEPS.includes(value as (typeof TIME_STEPS)[number]))
        && restoredSweepRange[0] <= nextYear
        && restoredSweepRange[1] >= nextYear
        && restoredSweepRange[0] <= restoredSweepRange[1];
      setSweepRangeStart(validSweepRange ? restoredSweepRange[0] : TIME_STEPS[0]);
      setSweepRangeEnd(validSweepRange ? restoredSweepRange[1] : TIME_STEPS.at(-1)!);
      setMovingWindowFrames(clamp(Math.round(parseNumber(params.get("twindow"), 3)), 1, 8));
      setPlaybackDirection(params.get("tdir") === "reverse" ? "reverse" : "forward");
      setPlaybackLoopMode(params.get("tloop") === "loop" ? "loop" : "stop");
      setDynamicEffects(params.get("motion") !== "off");
      setPlaying(false);
      const restoredEvidenceFilter = params.get("ef");
      const nextEvidenceFilter: RegistryEvidenceFilter = restoredEvidenceFilter && restoredEvidenceFilter in evidenceLabels ? restoredEvidenceFilter as EvidenceState : "ALL";
      mapEvidenceFilterRef.current = nextEvidenceFilter;
      setMapEvidenceFilter(nextEvidenceFilter);
      const restoredBasemap = params.get("base");
      const nextBasemap: BasemapKey = isBasemapKey(restoredBasemap) ? restoredBasemap : "standard";
      basemapRef.current = nextBasemap;
      setBasemap(nextBasemap);
      const restoredProjection = params.get("proj");
      const nextProjection = restoredProjection === "globe" ? "globe" : "mercator";
      projectionRef.current = nextProjection;
      setProjection(nextProjection);
      const restoredScene = params.get("scene");
      const nextScenePreset: ScenePresetId = restoredScene === "overview-2d" || restoredScene === "globe-overview" || restoredScene === "water-systems" || restoredScene === "smoke-context" || restoredScene === "elevation-3d" || restoredScene === "tile-grid" ? restoredScene : "overview-2d";
      scenePresetRef.current = nextScenePreset;
      setScenePreset(nextScenePreset);
      const nextVerticalExaggeration = nextScenePreset === "elevation-3d" ? terrainDepth(parseNumber(params.get("zscale"), DEFAULT_TERRAIN_DEPTH)) : clamp(parseNumber(params.get("zscale"), 1), 0, 2);
      verticalExaggerationRef.current = nextVerticalExaggeration;
      setVerticalExaggeration(nextVerticalExaggeration);
      const restoredAtmosphere = params.get("sky");
      const nextAtmosphere: AtmospherePreset = restoredAtmosphere === "dusk" || restoredAtmosphere === "clear" || restoredAtmosphere === "night"
        ? restoredAtmosphere
        : nextScenePreset === "elevation-3d" ? "dusk" : "night";
      atmospherePresetRef.current = nextAtmosphere;
      setAtmospherePreset(nextAtmosphere);
      const nextLightAzimuth = clamp(parseNumber(params.get("light"), nextScenePreset === "elevation-3d" ? 235 : 210), 0, 359);
      lightAzimuthRef.current = nextLightAzimuth;
      setLightAzimuth(nextLightAzimuth);
      const nextFieldOfView = clamp(parseNumber(params.get("fov"), nextScenePreset === "elevation-3d" ? compositionDefaults("terrain").fieldOfView : 36), 20, 60);
      fieldOfViewRef.current = nextFieldOfView;
      setFieldOfView(nextFieldOfView);
      const nextGestureMode = params.get("gestures") === "direct" ? "direct" : "cooperative";
      gestureModeRef.current = nextGestureMode;
      setGestureMode(nextGestureMode);
      const restoredMeasureUnit: MeasureUnit = params.get("units") === "metric" ? "metric" : "imperial";
      measureUnitRef.current = restoredMeasureUnit;
      setMeasureUnit(restoredMeasureUnit);
      const restoredWorkspace = params.get("ws");
      setCurrentWorkspace(restoredWorkspace === "knowledge" || restoredWorkspace === "features" || restoredWorkspace === "trust" ? restoredWorkspace : "explore");
      const restoredMapUtilityView = params.get("maptab");
      const restoredSourceStatus = params.get("layers") === "sources" || restoredMapUtilityView === "localAtlas";
      if (restoredSourceStatus) { setLeftPanelMode("layers"); setLeftOpen(true); setSourceStatusOpen(true); }
      const nextMapUtilityView: MapUtilityView = nextTemporalMode === "comparison"
        ? "compare"
        : restoredMapUtilityView === "report" || restoredMapUtilityView === "inspect" || restoredMapUtilityView === "scene" || restoredMapUtilityView === "history" || restoredMapUtilityView === "connections" || restoredMapUtilityView === "import" || restoredMapUtilityView === "compare" || restoredMapUtilityView === "measure" || restoredMapUtilityView === "export" || restoredMapUtilityView === "diagnostics" ? restoredMapUtilityView : "scene";
      setMapUtilityView(nextMapUtilityView);
      const restoredComparisonTimes = params.get("times")?.split(",").map(Number) ?? [];
      if (restoredComparisonTimes.length === 2 && restoredComparisonTimes.every((value) => TIME_STEPS.includes(value as (typeof TIME_STEPS)[number]))) {
        setCompareTimeA(restoredComparisonTimes[0]);
        setCompareTimeB(restoredComparisonTimes[1]);
      } else {
        setCompareTimeA(1910);
        setCompareTimeB(OFFICIAL_CONTEXT_PRESENT_FRAME);
      }
      if (nextMapUtilityView === "export") setExportGeneratedAt(new Date().toISOString());
      if (nextMapUtilityView === "report") setReportGeneratedAt(new Date().toISOString());
      const restoredMapUtilityOpen = !restoredSourceStatus && (nextTemporalMode === "comparison" || params.get("mapui") === "open" && restoredMapUtilityView !== "display" && restoredMapUtilityView !== "places");
      setMapUtilityOpen(restoredMapUtilityOpen);
      if (params.get("mapui") === "open" && restoredMapUtilityView === "places") {
        setLeftPanelMode("places");
        setLeftOpen(true);
      }
      if (params.get("mapui") === "open" && restoredMapUtilityView === "display") {
        setLeftPanelMode("layers");
        setLeftOpen(true);
        window.setTimeout(() => { const settings = leftPanelRef.current?.querySelector<HTMLDetailsElement>("#map-settings"); if (settings) settings.open = true; }, 0);
      }
      if (restoredMapUtilityOpen && compactRef.current) {
        setLeftOpen(false);
        setRightOpen(false);
        setTimelineOpen(false);
      }
      const restoredOrder = params.get("order")?.split(",").filter(Boolean) ?? [];
      if (restoredOrder.length === knownLayerIds.size && new Set(restoredOrder).size === knownLayerIds.size && restoredOrder.every((id) => knownLayerIds.has(id))) {
        orderRef.current = restoredOrder;
        setLayerOrder(restoredOrder);
      } else {
        orderRef.current = defaultOrder;
        setLayerOrder(defaultOrder);
      }
      const featureId = params.get("f");
      let restoredSelection = false;
      if (featureId) {
        const match = findFeature(featureId);
        if (match) {
          const context = copyFeature(match.layer, featureId);
          if (context) {
            restoredSelection = true;
            setFocusStage("outcome");
            setFocusIntent("explain");
            setPendingFocusAction(null);
            selectedRef.current = context;
            setSelected(context);
            if (!params.has("l")) setVisibility((current) => {
              const next = { ...current, [context.layerId]: true };
              visibilityRef.current = next;
              return next;
            });
            const restoredDrawer = params.get("panel");
            setDrawerView(restoredDrawer === "metadata" || restoredDrawer === "lineage" || restoredDrawer === "focus" ? restoredDrawer : "evidence");
            const restoredFocusStage = params.get("focusStage");
            setFocusStage(restoredFocusStage === "checks" || restoredFocusStage === "actions" ? restoredFocusStage : "outcome");
            const restoredFocusIntent = params.get("focusIntent");
            setFocusIntent(restoredFocusIntent === "why" || restoredFocusIntent === "lineage" || restoredFocusIntent === "time" ? restoredFocusIntent : "explain");
            setRightOpen(params.get("drawer") !== "closed" && !(restoredMapUtilityOpen && compactRef.current));
          }
        }
      }
      if (!restoredSelection) {
        setFocusStage("outcome");
        setFocusIntent("explain");
        setPendingFocusAction(null);
        selectedRef.current = null;
        setSelected(null);
        setRightOpen(false);
      }
      explorerRestoredRef.current = true;
      setLayerPreferencesReady(true);
  }, [cancelSmokePlayback, loadOfficialArchiveDay, refreshNoaaHydrologyNetwork, refreshNoaaRadarManifest, refreshOfficialContext, refreshStreamflow]);

  useEffect(() => {
    if (explorerRestoredRef.current) saveExplorerHistoryView(buildExplorerParams(), window.history);
  }, [buildExplorerParams]);

  useEffect(() => {
    const restore = window.setTimeout(restoreExplorerFromUrl, 0);
    const handlePopState = () => restoreExplorerFromUrl();
    window.addEventListener("popstate", handlePopState);
    return () => {
      window.clearTimeout(restore);
      window.removeEventListener("popstate", handlePopState);
    };
  }, [restoreExplorerFromUrl]);

  useEffect(() => {
    let disposed = false;
    let resizeObserver: ResizeObserver | null = null;
    let mapResizeFrame: number | undefined;
    let cancelHoverSample = () => {};
    let cancelSettledViewCommit = () => {};
    let stopStormDeskProbe = () => {};
    const rasterRetryTimers = new Map<OfficialContextId, number>();
    const rasterRetryCounts = new Map<OfficialContextId, number>();
    let terrainRetryTimer: number | null = null;
    let terrainRetryCount = 0;
    const mapContainer = mapContainerRef.current;
    if (!mapContainer) return;

    loadConfiguredMapLibre().then(({ mapLibre, version }) => {
      if (disposed || !mapContainerRef.current) return;
      setMaplibreProbe((current) => ({ ...current, version, workerConfigured: true, runtimeAssetsReady: true, error: null }));
      try {
        const webgl2 = webgl2Available();
        setMaplibreProbe((current) => ({ ...current, webgl2 }));
        if (!webgl2) {
          setSourceStates(Object.fromEntries(LAYER_REGISTRY.map((layer) => [layer.id, "error"])));
          setMaplibreProbe((current) => ({ ...current, error: "WebGL2 is unavailable" }));
          setRuntime({ kind: "unsupported", message: "WebGL2 is unavailable in this browser. The Layer Catalog and trust metadata remain readable, but the interactive map cannot start." });
          return;
        }
        const initialView = pendingViewRef.current ?? KANSAS_VIEW;
        const renderBudget = browserRenderBudget();
        const map = new mapLibre.Map({ transformRequest: basemapCacheRequest,
          container: mapContainerRef.current,
          style: hiDpiBasemapStyle(BASEMAPS[basemapRef.current].style, renderBudget.pixelRatio),
          center: initialView.center,
          zoom: initialView.zoom,
          bearing: initialView.bearing,
          pitch: initialView.pitch,
          pixelRatio: renderBudget.pixelRatio,
          // The Explorer owns a frame-coalesced container observer below.
          // Avoid MapLibre's second observer doing the same canvas/camera work.
          trackResize: false,
          maxTileCacheSize: renderBudget.tileCache,
          maxPitch: scenePresetRef.current === "elevation-3d" ? 72 : 60,
          renderWorldCopies: false,
          minZoom: projectionRef.current === "globe" ? 0 : 4,
          maxZoom: 16,
          maxBounds: projectionRef.current === "globe" ? undefined : REGIONAL_NAVIGATION_BOUNDS,
          attributionControl: false,
          cooperativeGestures: gestureModeRef.current === "cooperative",
          boxZoom: {
            boxZoomEnd: (mapInstance, start, end) => {
              const cornerA = mapInstance.unproject([Math.min(start.x, end.x), Math.max(start.y, end.y)]);
              const cornerB = mapInstance.unproject([Math.max(start.x, end.x), Math.min(start.y, end.y)]);
              const bounds = {
                west: Math.min(cornerA.lng, cornerB.lng),
                south: Math.min(cornerA.lat, cornerB.lat),
                east: Math.max(cornerA.lng, cornerB.lng),
                north: Math.max(cornerA.lat, cornerB.lat),
              };
              if (boxDragModeRef.current === "report-area") {
                analysisAreaRef.current = bounds;
                setAnalysisArea(bounds);
                setReportScope("ANALYSIS_AREA");
                setReportGeneratedAt(new Date().toISOString());
                updateAnalysisAreaSource(mapInstance, bounds);
                announce("Shift-drag locked a browser-local MapLibre report area");
                return;
              }
              mapInstance.fitBounds([[bounds.west, bounds.south], [bounds.east, bounds.north]], { padding: 34, duration: motionDuration(450) });
            },
          },
        });
        mapRef.current = map;
        stopStormDeskProbe = installStormDeskPerformanceProbe(map);
        terrainDrawingRef.current = createTerrainDrawing(map, (status) => {
          if (!disposed && mapRef.current === map) setTerrainDrawingStatus(status);
        }, (probe) => {
          if (!disposed && mapRef.current === map) setTerrainSurfaceProbe(measureModeRef.current ? null : probe);
        });
        registerSceneEffects(map, sceneEffectsRef.current);
        const mapCanvas = map.getCanvas();
        mapCanvas.addEventListener("webglcontextlost", (event) => {
          event.preventDefault();
          setMaplibreProbe((current) => ({ ...current, canvasReady: false, error: "WebGL context lost" }));
          setRuntime({ kind: "degraded", message: "The browser paused the map renderer. Data controls remain available while MapLibre restores the canvas." });
        });
        mapCanvas.addEventListener("webglcontextrestored", () => {
          if (disposed) return;
          if (runMapMutation("Map canvas recovery", () => map.resize())) {
            setRuntime({ kind: "loading", message: "Map canvas restored · verifying sources and interactions…" });
          }
        });
        if (typeof ResizeObserver !== "undefined") {
          resizeObserver = new ResizeObserver((entries) => {
            if (disposed || !entries.some((entry) => entry.contentRect.width > 0 && entry.contentRect.height > 0)) return;
            if (mapResizeFrame !== undefined) return;
            mapResizeFrame = window.requestAnimationFrame(() => {
              mapResizeFrame = undefined;
              if (!disposed) runMapMutation("Map container resize", () => map.resize());
            });
          });
          resizeObserver.observe(mapContainer);
        }
        setMaplibreProbe((current) => ({ ...current, mapConstructed: true }));
        const scaleControl = new mapLibre.ScaleControl({ unit: measureUnitRef.current, maxWidth: 110 });
        scaleControlRef.current = scaleControl;
        map.addControl(scaleControl, "bottom-left");
        const navigationControl = new mapLibre.NavigationControl({ showCompass: true, showZoom: false, visualizePitch: true });
        const fullscreenControl = new mapLibre.FullscreenControl();
        const geolocateControl = new mapLibre.GeolocateControl({
          positionOptions: { enableHighAccuracy: false },
          trackUserLocation: false,
        });
        map.addControl(navigationControl, "top-right");
        map.addControl(fullscreenControl, "top-right");
        map.addControl(geolocateControl, "top-right");
        map.addControl(new mapLibre.AttributionControl({ compact: true }), "top-right");
        geolocateControl.on("geolocate", () => {
          locationDerivedViewRef.current = true;
          setLocationCameraRedacted(true);
          announce("Browser location is active; share and report outputs redact the location-derived camera");
        });
        const nativeControlsBound = true;
        let interactionHandlersBound = false;
        let runtimeError: string | null = null;
        let degradedReason: string | null = null;
        let styleFallbackAttempted = false;
        const failedSourceIds = new Set<string>();

        const refreshMaplibreProbe = () => {
          const health = sampleMapRuntimeHealth(
            map,
            LAYER_REGISTRY.map((layer) => layer.sourceId),
            interactionHandlersBound,
            nativeControlsBound && Boolean(scaleControlRef.current),
          );
          const nextSourceStates = Object.fromEntries(LAYER_REGISTRY.map((layer) => {
            const sourceReady = health.sourceReadyById[layer.sourceId];
            return [layer.id, sourceReady ? "ready" : failedSourceIds.has(layer.sourceId) ? "error" : "loading"];
          })) as Record<string, "loading" | "ready" | "error">;
          const sourcesReady = Object.values(nextSourceStates).filter((state) => state === "ready").length;
          const nextProbe = {
            styleLoaded: health.styleLoaded,
            canvasReady: health.canvasReady,
            idle: health.idle,
            tilesLoaded: health.tilesLoaded,
            controlsReady: health.controlsReady,
            interactionsReady: health.interactionsReady,
            sourcesReady,
            projection: health.projection,
            failedChecks: health.failedChecks,
            error: runtimeError ?? mapMutationErrorRef.current,
          } satisfies Partial<MapLibreRuntimeProbe>;
          setSourceStates((current) => sameRecord(current, nextSourceStates) ? current : nextSourceStates);
          setStyleReady(health.styleLoaded);
          setMaplibreProbe((current) => sameValues(current, nextProbe) ? current : { ...current, ...nextProbe });
          return nextProbe;
        };

        const syncStyle = (): boolean => {
          cancelHoverSample();
          styleDocumentLoadedRef.current = true;
          // A style that loads ends the outage that used the fallback, so a later
          // basemap that fails (a category map asking for the vector base again)
          // falls back too instead of failing the map.
          styleFallbackAttempted = false;
          styleGenerationReadyRef.current = false;
          mapMutationErrorRef.current = null;
          if (hoverDrawerTimerRef.current !== null) window.clearTimeout(hoverDrawerTimerRef.current);
          hoverDrawerTimerRef.current = null;
          hoverCandidateIdRef.current = null;
          setHoverSummary(null);
          setHoverActive(false);
          let styleStep = "LOCAL_REGISTRY";
          const synced = runMapMutation("Map style synchronization", () => {
            hoveredRef.current = null;
            map.getCanvas().style.cursor = "";
            applyRegistryState(map, visibilityRef.current, opacityRef.current, yearRef.current, orderRef.current, mapEvidenceFilterRef.current, temporalQueryRef.current);
            styleStep = "OFFICIAL_CONTEXT";
            noaaRadarReadyRef.current = Boolean(
              noaaRadarFrameTimeRef.current
              && noaaRadarManifestIsFresh(noaaRadarManifestRef.current, Date.now()),
            );
            applyOfficialContextState(map, runtimeOfficialVisibility(officialVisibilityRef.current, temporalQueryRef.current.frame, noaaRadarReadyRef.current, noaaRadarFrameTimeRef.current), officialOpacityRef.current, officialPayloadsRef.current);
            styleStep = "DAYLIGHT_CONTEXT";
            setDaylightMapLayer(map, daylightEnabledRef.current, daylightInstantRef.current);
            styleStep = "ELEVATION_SCALE";
            setElevationExaggeration(map, verticalExaggerationRef.current);
            styleStep = "PROJECTION";
            applyProjectionNavigationLimits(map, projectionRef.current);
            map.setProjection({ type: projectionRef.current });
            if (noaaSatelliteFrameRef.current) setNoaaSatelliteFrame(map, noaaSatelliteFrameRef.current,
              buildYearCurrentRef.current && officialVisibilityRef.current["noaa-goes-geocolor"] && temporalQueryRef.current.frame === OFFICIAL_CONTEXT_PRESENT_FRAME,
              officialOpacityRef.current["noaa-goes-geocolor"]);
            styleStep = "SCENE_ENVIRONMENT";
            applySceneEnvironment(map, atmospherePresetRef.current, lightAzimuthRef.current);
            styleStep = "FIELD_OF_VIEW";
            map.setVerticalFieldOfView(fieldOfViewRef.current);
            styleStep = "TERRAIN";
            setTerrainState(setTerrainPresentation(map, scenePresetRef.current === "elevation-3d", verticalExaggerationRef.current));
            setTerrainHeightOverlay(map, scenePresetRef.current === "elevation-3d" && topographicOverlayRef.current);
            setStructures3DState(setStructureExtrusions(map, structures3DRef.current));
            styleStep = "SCENE_EFFECTS";
            syncBorderCurtain(map, renderEfficientRef.current);
            syncSceneOverlays(map, atmospherePresetRef.current, lightAzimuthRef.current, renderEfficientRef.current);
            styleStep = "SELECTION";
            const currentSelection = selectedRef.current;
            if (currentSelection) {
              const mismatch = officialSelectionIsHeld(currentSelection, temporalQueryRef.current.frame, buildYearCurrentRef.current,
                civicDayForFrame(temporalQueryRef.current.frame, OFFICIAL_CONTEXT_PRESENT_FRAME, currentUtcDay(), calendarSweepRef.current ? calendarFrameDay(calendarSweepRef.current) : null))
                || !isFeatureAvailableForTemporalQuery(currentSelection.layer, currentSelection.properties.year, temporalQueryRef.current);
              const layerVisible = selectionCarrierIsVisible(currentSelection, visibilityRef.current,
                runtimeOfficialVisibility(officialVisibilityRef.current, temporalQueryRef.current.frame, noaaRadarReadyRef.current, noaaRadarFrameTimeRef.current));
              const filtered = !selectionPassesEvidenceFilter(currentSelection, mapEvidenceFilterRef.current);
              updateSelectionSource(map, mismatch || !layerVisible || filtered ? null : currentSelection.geometry);
            }
            styleStep = "MEASUREMENT";
            updateMeasurementSource(map, buildMeasurementData(measureCoordinatesRef.current, measurementGeometryModeRef.current));
            styleStep = "ANALYSIS_AREA";
            updateAnalysisAreaSource(map, analysisAreaRef.current);
            styleStep = "IMPORT_PREVIEW";
            updateImportPreviewSource(map, importPreviewVisibleRef.current ? importPreviewRef.current?.featureCollection : null);
            styleStep = "LOCAL_ROAD_STUDY";
            applyRoadStudyLayers(map, roadStudyLayersRef.current);
          });
          if (!synced) {
            const code = `MAP_STYLE_${styleStep}_FAILED`;
            mapMutationErrorRef.current = code;
            setMaplibreProbe((current) => ({ ...current, error: code }));
            setRuntime({ kind: "degraded", message: `${code}; the Explorer shell and data controls remain available.` });
            return false;
          }
          styleGenerationReadyRef.current = true;
          if (!runMapMutation("Map runtime proof refresh", () => { refreshMaplibreProbe(); })) {
            styleGenerationReadyRef.current = false;
            return false;
          }
          return true;
        };

        map.on("style.load", syncStyle);
        map.once("load", () => {
          // style.load already installed this generation. Reapplying every
          // source, terrain and overlay here queues another round of worker
          // updates just as the initial map settles. Retry only if setup failed
          // or did not run; later style.load events still rebuild every style.
          if (!styleGenerationReadyRef.current && !syncStyle()) return;
          if (!runMapMutation("Map load finalization", () => {
            map.setProjection({ type: projectionRef.current });
            map.resize();
          })) return;
          setRuntime({ kind: "loading", message: `MapLibre ${version} loaded · verifying catalog layers and interactions…` });
        });

        const clearHoverCandidate = () => {
          if (hoverDrawerTimerRef.current !== null) window.clearTimeout(hoverDrawerTimerRef.current);
          hoverDrawerTimerRef.current = null;
          hoverCandidateIdRef.current = null;
          setHoverActive(false);
        };
        const showHoverInDrawer = (summary: HoverSummary, autoOpen: boolean) => {
          if (hoverCandidateIdRef.current !== summary.id) {
            if (hoverDrawerTimerRef.current !== null) window.clearTimeout(hoverDrawerTimerRef.current);
            hoverCandidateIdRef.current = summary.id;
            // A deliberate desktop hover opens the dock once. Compact layouts keep click-to-open.
            if (autoOpen && !compactRef.current && rightPanelRef.current?.dataset.open !== "true") {
              hoverDrawerTimerRef.current = window.setTimeout(() => {
                hoverDrawerTimerRef.current = null;
                if (!aviationPickingRef.current && hoverCandidateIdRef.current === summary.id && !compactRef.current && !surfaceInspectionOpenRef.current) previewEvidence();
              }, 240);
            }
          }
          setHoverActive(true);
          setHoverSummary((current) => current?.id === summary.id && current.title === summary.title
            && current.subtitle === summary.subtitle && current.state === summary.state ? current : summary);
        };
        const hoverSampler = createMapHoverSampler<MapMouseEvent>((event) => {
          if (disposed || aviationPickingRef.current || !styleGenerationReadyRef.current || document.hidden) return;
          if (undergroundOpenRef.current && !measureModeRef.current) return;
          if (map.isMoving()) { clearHoverCandidate(); return; }
          if (scenePresetRef.current === "elevation-3d" && styleGenerationReadyRef.current
            && attachedTerrainProviderRef.current === terrainProviderRef.current
            && map.getTerrain()?.source === TERRAIN_SOURCE_ID
            && failedTerrainSourceRef.current !== map.getSource(TERRAIN_SOURCE_ID)) {
            const elevationMeters = unexaggeratedTerrainElevation(map, [event.lngLat.lng, event.lngLat.lat]);
            setTerrainElevationUnavailable(elevationMeters === null ? { longitude: event.lngLat.lng, latitude: event.lngLat.lat } : null);
            setTerrainElevationReading(elevationMeters !== null ? {
              longitude: event.lngLat.lng,
              latitude: event.lngLat.lat,
              meters: elevationMeters,
              feet: elevationMeters * 3.28084,
              provider: terrainProviderRef.current,
            } : null);
          } else {
            setTerrainElevationReading(null);
            setTerrainElevationUnavailable(null);
          }
          const renderedHits = map.queryRenderedFeatures(event.point).filter(feature => {
            const source = OFFICIAL_CONTEXT_BY_SOURCE_ID[feature.source];
            const record = findLayerByRenderer(feature.layer.id);
            return source ? officialOpacityRef.current[source.id] > 0 : record ? (opacityRef.current[record.id] ?? record.defaultOpacity) > 0 : true;
          });
          if (renderedHits[0]?.source === LIVING_WATERS_SOURCE || renderedHits[0]?.source === EARTHQUAKE_RECORD_SOURCE_ID || renderedHits[0]?.source === STORM_REPORTS_SOURCE_ID || renderedHits[0]?.source === REVIEWED_SOURCE_ID) {
            map.getCanvas().style.cursor = "pointer";
            if (hoveredRef.current) map.setFeatureState(hoveredRef.current, { hover: false });
            hoveredRef.current = null;
            clearHoverCandidate();
            return;
          }
          const availableLayers = interactiveLayerIds.filter((id) => map.getLayer(id));
          const availableOfficialLayers = OFFICIAL_CONTEXT_INTERACTIVE_LAYER_IDS.filter((id) => map.getLayer(id));
          const { candidate, officialCandidate } = layerHitStack(renderedHits, availableLayers, availableOfficialLayers);
          const externalCandidate = candidate ? null : officialCandidate ?? renderedHits.find((feature) => {
            const sourceId = typeof feature.source === "string" ? feature.source : "";
            const isSiteLocal = sourceId.startsWith("kfm-") || sourceId.startsWith("scene-") || LAYER_REGISTRY.some((layer) => layer.sourceId === sourceId);
            return !isSiteLocal && Boolean(feature.geometry) && Boolean(feature.properties && Object.keys(feature.properties).length);
          });
          if (!candidate && !externalCandidate) {
            map.getCanvas().style.cursor = "";
            if (hoveredRef.current) map.setFeatureState(hoveredRef.current, { hover: false });
            hoveredRef.current = null;
            clearHoverCandidate();
            return;
          }
          map.getCanvas().style.cursor = "pointer";
          if (!candidate) {
            if (hoveredRef.current) map.setFeatureState(hoveredRef.current, { hover: false });
            hoveredRef.current = null;
            const externalTitle = String(externalCandidate?.properties?.name ?? externalCandidate?.properties?.name_en ?? externalCandidate?.properties?.event ?? externalCandidate?.properties?.monitoringLocationId ?? externalCandidate?.properties?.class ?? "Basemap feature");
            const officialSource = externalCandidate?.source ? OFFICIAL_CONTEXT_BY_SOURCE_ID[externalCandidate.source] : undefined;
            showHoverInDrawer({
              id: `external:${externalCandidate?.source ?? "context"}:${externalTitle}`,
              title: externalTitle,
              subtitle: officialSource?.shortTitle ?? "External basemap context",
              state: "No KFM evidence attached",
            }, Boolean(officialSource));
            return;
          }
          const hoverLayer = findLayerByRenderer(candidate.layer.id);
          const hoverFeatureId = String(candidate.properties?.fid ?? candidate.id ?? "");
          const hoverRecord = hoverFeatureId ? findFeature(hoverFeatureId) : null;
          showHoverInDrawer({
            id: `${candidate.source}:${hoverFeatureId || candidate.properties?.cluster_id || candidate.layer.id}`,
            title: candidate.properties?.cluster
              ? `${candidate.properties.point_count ?? "Multiple"} nearby place records`
              : hoverRecord?.feature.properties.title ?? hoverLayer?.title ?? "Map feature",
            subtitle: candidate.properties?.cluster ? "Select to expand the cluster" : hoverLayer?.title ?? "Site-local map layer",
            state: candidate.properties?.cluster ? "Generalized cluster" : hoverRecord ? evidenceLabels[hoverRecord.feature.properties.evidenceState].label : "Inspect for details",
          }, true);
          if (candidate.id !== undefined) {
            const next = { source: candidate.source, id: candidate.id };
            if (hoveredRef.current?.source === next.source && hoveredRef.current.id === next.id) return;
            if (hoveredRef.current) map.setFeatureState(hoveredRef.current, { hover: false });
            hoveredRef.current = next;
            map.setFeatureState(hoveredRef.current, { hover: true });
          } else if (hoveredRef.current) {
            map.setFeatureState(hoveredRef.current, { hover: false });
            hoveredRef.current = null;
          }
        });
        cancelHoverSample = hoverSampler.cancel;
        map.on("mousemove", (event) => {
          if (aviationPickingRef.current || map.isMoving() || !styleGenerationReadyRef.current || document.hidden
            || undergroundOpenRef.current && !measureModeRef.current) {
            hoverSampler.cancel(); clearHoverCandidate(); return;
          }
          hoverSampler.push(event);
        });
        map.getCanvas().addEventListener("mouseleave", () => {
          hoverSampler.cancel();
          if (hoveredRef.current && map.getSource(hoveredRef.current.source)) {
            try { map.setFeatureState(hoveredRef.current, { hover: false }); } catch { /* Source teardown can race a pointer exit. */ }
          }
          hoveredRef.current = null;
          map.getCanvas().style.cursor = "";
          clearHoverCandidate();
          setTerrainElevationReading(null);
          setTerrainElevationUnavailable(null);
        });
        map.on("movestart", () => { hoverSampler.cancel(); clearHoverCandidate(); });

        map.on("click", (event) => {
          if (aviationPickingRef.current) return;
          if (undergroundOpenRef.current && !measureModeRef.current) return;
          if (measureModeRef.current) {
            measureCoordinatesRef.current = measureModeRef.current === "point"
              ? [[event.lngLat.lng, event.lngLat.lat]]
              : [...measureCoordinatesRef.current, [event.lngLat.lng, event.lngLat.lat]];
            setMeasureCoordinateCount(measureCoordinatesRef.current.length);
            const coordinates = measureCoordinatesRef.current;
            updateMeasurementSource(map, buildMeasurementData(coordinates, measureModeRef.current));
            setMeasurement(measurementLabelFor(measureModeRef.current, coordinates, measureUnitRef.current));
            if (measureModeRef.current === "point") {
              measureModeRef.current = null;
              setMeasureMode(null);
              map.doubleClickZoom.enable();
              setMeasurement(`Complete · ${measurementLabelFor("point", coordinates, measureUnitRef.current)}`);
              announce("Placed a browser-local point; it is not admitted evidence");
            }
            return;
          }

          const renderedHits = map.queryRenderedFeatures(event.point).filter(feature => {
            const source = OFFICIAL_CONTEXT_BY_SOURCE_ID[feature.source];
            const record = findLayerByRenderer(feature.layer.id);
            return source ? officialOpacityRef.current[source.id] > 0 : record ? (opacityRef.current[record.id] ?? record.defaultOpacity) > 0 : true;
          });
          // Local previews own their selection; never inspect official features beneath them.
          const availableLayers = interactiveLayerIds.filter((id) => map.getLayer(id));
          // The fixture control owns synthetic selection; never select provider
          // context underneath its schematic as evidence for that schematic.
          if (renderedHits[0]?.source === LIVING_WATERS_SOURCE) {
            setLeftPanelMode("views"); setAtlasViewQuery(""); setLeftOpen(true);
            return;
          }
          // These selections are shown only in the category dock, so picking one brings a closed dock back.
          // A reviewed-snapshot feature is a released record, not basemap context: the dock shows it with its release.
          if (renderedHits[0]?.source === REVIEWED_SOURCE_ID) {
            const id = renderedHits[0].properties?.[REVIEWED_FEATURE_ID];
            if (typeof id === "string" && id) { setReviewedPick(id); setCategoryDockHidden(false); }
            return;
          }
          // A storm report owns its selection: the dock shows the report; nothing beneath it is inspected.
          if (renderedHits[0]?.source === STORM_REPORTS_SOURCE_ID) {
            const id = renderedHits[0].properties?.id;
            const report = typeof id === "string" ? stormReportsRef.current.get(id) : undefined;
            if (report) { setReportSelected(report); setCategoryDockHidden(false); }
            return;
          }
          // With flood forecasts shown, an NWS gauge owns its selection: the dock draws its hydrograph.
          if (floodOnRef.current && renderedHits[0]?.source === OFFICIAL_CONTEXT_BY_ID["noaa-nwps-gauges"].sourceId) {
            const lid = renderedHits[0].properties?.lid;
            if (typeof lid === "string") { setFloodLid(lid); setFloodFailed(null); setCategoryDockHidden(false); }
            return;
          }
          // The earthquake record owns its selection: the dock shows the event; nothing beneath it is inspected.
          if (renderedHits[0]?.source === EARTHQUAKE_RECORD_SOURCE_ID) {
            const id = renderedHits[0].properties?.id;
            const event = typeof id === "string" ? quakeRecordEventsRef.current.get(id) : undefined;
            if (event) { setQuakeRecordSelected(event); setCategoryDockHidden(false); }
            return;
          }
          // With the Drought Monitor's counties on the map, a click picks the county under it; the dock gives its shares.
          // An interactive overlay or official feature drawn above the county keeps its own selection.
          const clickedCounty = droughtCountyAtClick(renderedHits, id => availableLayers.includes(id) || OFFICIAL_CONTEXT_INTERACTIVE_LAYER_IDS.includes(id));
          if (clickedCounty) {
            setDroughtCounty(clickedCounty);
            setCategoryDockHidden(false);
            return;
          }
          const availableOfficialLayers = OFFICIAL_CONTEXT_INTERACTIVE_LAYER_IDS.filter((id) => map.getLayer(id));
          const { candidate, officialCandidate, registryHits: renderedCandidates } = layerHitStack(renderedHits, availableLayers, availableOfficialLayers);
          if (!candidate) {
            setMapQueryCandidates([]);
            const externalCandidate = officialCandidate ?? renderedHits.find((feature) => {
              const sourceId = typeof feature.source === "string" ? feature.source : "";
              const isSiteLocal = sourceId.startsWith("kfm-") || sourceId.startsWith("scene-") || LAYER_REGISTRY.some((layer) => layer.sourceId === sourceId);
              return !isSiteLocal && Boolean(feature.geometry) && Boolean(feature.properties && Object.keys(feature.properties).length);
            });
            const context = externalCandidate
              ? buildBasemapContext(externalCandidate, event.lngLat.lng, event.lngLat.lat)
              : null;
            if (context) {
              const officialSource = externalCandidate?.source ? OFFICIAL_CONTEXT_BY_SOURCE_ID[externalCandidate.source] : undefined;
              if (officialSource?.id === "usgs-streamflow") {
                const stationCandidate = externalCandidate?.properties?.stationId ?? externalCandidate?.properties?.monitoringLocationId;
                const stationId = typeof stationCandidate === "string" ? normalizeUsgsStationId(stationCandidate) : null;
                if (stationId) {
                  setStreamflowPlaying(false);
                  setStreamflowSelectedStationId(stationId);
                  setLiveInstrument("river");
                }
              } else if (officialSource?.id === "noaa-nwps-gauges") {
                setLiveInstrument("river");
              }
              openSelectionRef.current(context, mapContainerRef.current);
              updateSelectionSource(map, context.geometry);
            }
            return;
          }

          if (candidate.properties?.cluster) {
            setMapQueryCandidates([]);
            const source = map.getSource(candidate.source) as GeoJSONSource;
            void source.getClusterExpansionZoom(Number(candidate.properties.cluster_id)).then((zoom) => {
              const coordinates = (candidate.geometry as GeoJSON.Point).coordinates as [number, number];
              map.easeTo({ center: coordinates, zoom, duration: window.matchMedia("(prefers-reduced-motion: reduce)").matches ? 0 : 500 });
            });
            return;
          }

          const stableCandidates = new Map<string, MapQueryCandidate>();
          for (const rendered of renderedCandidates) {
            if (rendered.properties?.cluster) continue;
            const layer = findLayerByRenderer(rendered.layer.id);
            const featureId = String(rendered.properties?.fid ?? rendered.id ?? "");
            const match = featureId ? findFeature(featureId) : null;
            if (!layer || !match || match.layer.id !== layer.id) continue;
            stableCandidates.set(`${layer.id}:${featureId}`, {
              featureId,
              layerId: layer.id,
              title: match.feature.properties.title,
              layerTitle: layer.title,
              evidenceState: match.feature.properties.evidenceState,
              sourceYear: match.feature.properties.year,
            });
          }
          const candidateStack = [...stableCandidates.values()];
          if (candidateStack.length > 1) {
            mapUtilityReturnRef.current = mapContainerRef.current;
            setMapQueryCandidates(candidateStack);
            setMapFeatureLayer("ALL");
            setMapUtilityView("inspect");
            setMapUtilityOpen(true);
            if (compactRef.current) {
              setLeftOpen(false);
              setRightOpen(false);
              setTimelineOpen(false);
            }
            window.setTimeout(() => mapUtilityPanelRef.current?.querySelector<HTMLElement>("button:not([disabled])")?.focus(), 0);
            return;
          }

          const stableCandidate = candidateStack[0];
          const layer = stableCandidate ? LAYER_REGISTRY.find((item) => item.id === stableCandidate.layerId) : undefined;
          const featureId = stableCandidate?.featureId ?? "";
          if (!layer || !featureId) {
            setRuntime({ kind: "degraded", message: "A rendered candidate could not be translated into a stable Explorer feature." });
            return;
          }
          const context = copyFeature(layer, featureId);
          if (!context) {
            setRuntime({ kind: "degraded", message: "The selected candidate has no stable application-level registry record." });
            return;
          }

          setMapQueryCandidates([]);
          openSelectionRef.current(context, mapContainerRef.current);
          updateSelectionSource(map, context.geometry);
        });
        interactionHandlersBound = true;

        const terrainRasterBounds = () => {
          const bounds = map.getBounds();
          return { west: bounds.getWest(), east: bounds.getEast(), south: bounds.getSouth(), north: bounds.getNorth() };
        };
        const syncTerrainRasterView = () => {
          const bounds = terrainRasterBounds();
          for (const id of ["usgs-3dep-hillshade", "usgs-3dep-slope"] as const) {
            if (!officialVisibilityRef.current[id] || temporalQueryRef.current.frame !== OFFICIAL_CONTEXT_PRESENT_FRAME) continue;
            const source = map.getSource(OFFICIAL_CONTEXT_BY_ID[id].sourceId);
            terrainRasterViewRef.current.bindSource(id, source);
            const failed = terrainRasterViewRef.current.hasFailed(id, bounds, map.getZoom());
            if (failed) officialRasterFailuresRef.current.add(id);
            else {
              officialRasterFailuresRef.current.delete(id);
              const pendingRetry = rasterRetryTimers.get(id);
              if (pendingRetry !== undefined) { window.clearTimeout(pendingRetry); rasterRetryTimers.delete(id); }
            }
            const next = terrainRasterViewRef.current.status(id, bounds, map.getZoom(), Boolean(source && map.isSourceLoaded(OFFICIAL_CONTEXT_BY_ID[id].sourceId)));
            setOfficialStates(current => current[id] === next ? current : ({ ...current, [id]: next }));
            if (!failed) setOfficialErrors(current => current[id] ? ({ ...current, [id]: undefined }) : current);
          }
        };
        // Cheap per-frame check; layout only changes when crossing the pitch threshold.
        map.on("pitch", () => {
          try {
            syncBorderCurtainVisibility(map, renderEfficientRef.current);
            syncNightSkyVisibility(map, renderEfficientRef.current);
          } catch { /* decorative only */ }
        });
        let settledViewWasReplay = false;
        const settledViewCommit = createSettledMapCommit(() => {
          syncTerrainRasterView();
          const center = map.getCenter();
          const nextView: ViewState = { center: [center.lng, center.lat], zoom: map.getZoom(), bearing: map.getBearing(), pitch: map.getPitch() };
          const bounds = map.getBounds();
          setMapViewportBounds({ west: bounds.getWest(), south: bounds.getSouth(), east: bounds.getEast(), north: bounds.getNorth() });
          setView(nextView);
          const cameraFov = map.getVerticalFieldOfView();
          fieldOfViewRef.current = cameraFov;
          setFieldOfView(cameraFov);
          if (!settledViewWasReplay && !locationDerivedViewRef.current) {
            const retained = cameraHistoryRef.current.slice(0, cameraHistoryIndexRef.current + 1);
            const previous = retained.at(-1);
            if (!previous || !cameraViewsEquivalent(previous, nextView)) {
              const nextHistory = [...retained, nextView].slice(-16);
              const nextIndex = nextHistory.length - 1;
              cameraHistoryRef.current = nextHistory;
              cameraHistoryIndexRef.current = nextIndex;
              setCameraHistoryIndex(nextIndex);
              setCameraHistoryLength(nextHistory.length);
            }
          }
        }, () => map.isMoving());
        cancelSettledViewCommit = settledViewCommit.cancel;
        map.on("movestart", () => {
          settledViewCommit.cancel();
          const center = map.getCenter();
          lastKnownGoodViewRef.current = { center: [center.lng, center.lat], zoom: map.getZoom(), bearing: map.getBearing(), pitch: map.getPitch() };
        });
        map.on("moveend", () => {
          // Consume the replay marker at its original event boundary. A manual
          // interruption must still record its eventual stopped view.
          settledViewWasReplay = replayingCameraHistoryRef.current;
          replayingCameraHistoryRef.current = false;
          settledViewCommit.schedule();
        });
        map.on("error", (event) => {
          const sourceId = (event as typeof event & { sourceId?: string }).sourceId;
          // Soil moisture, Crop-CASMA, Earth Engine, and device GeoPDF controls
          // report their own partial state; their tiles must not fail the map.
          if (controlOwnsMapSourceErrors(sourceId)) return;
          // MapLibre error text can contain a provider URL or a query token.
          // Only the finite class and already registered source title enter UI state.
          const message = mapRuntimeErrorCode("event", sourceId);
          const affectedLayer = sourceId ? LAYER_REGISTRY.find((layer) => layer.sourceId === sourceId) : undefined;
          const affectedOfficialContext = officialContextForMapSource(sourceId);
          if (VECTOR_BASEMAPS.has(basemapRef.current) && !styleFallbackAttempted && shouldFallbackStandardBasemap(sourceId, Boolean(affectedLayer), Boolean(affectedOfficialContext), styleDocumentLoadedRef.current)) {
            styleFallbackAttempted = true;
            runtimeError = null;
            degradedReason = `${BASEMAPS[basemapRef.current].title} basemap unavailable; switched to the local MapLibre style. ${message}`;
            basemapRef.current = "midnight";
            setBasemap("midnight");
            setRuntime({ kind: "degraded", message: degradedReason });
            return;
          }
          if (affectedOfficialContext?.id === "nws-radar") {
            setNoaaRadarPlaying(false);
            const failCurrentRadarFrame = noaaRadarFrameFailureRef.current;
            if (failCurrentRadarFrame) {
              failCurrentRadarFrame(message);
            } else {
              setNoaaRadarFrameLoadState("error");
              setOfficialStates((current) => ({ ...current, "nws-radar": "error" }));
              setOfficialErrors((current) => ({ ...current, "nws-radar": message }));
            }
            return;
          }
          if (affectedOfficialContext) {
            const id = affectedOfficialContext.id;
            const terrainRaster = id === "usgs-3dep-hillshade" || id === "usgs-3dep-slope";
            const erroredTile = terrainRasterErrorTile(event as typeof event & { tile?: { tileID?: { canonical?: { z: number; x: number; y: number } } }; coord?: { canonical?: { z: number; x: number; y: number } } });
            if (terrainRaster && erroredTile) {
              const bounds = map.getBounds();
              if (!terrainRasterTileInView(erroredTile,
                { west: bounds.getWest(), east: bounds.getEast(), south: bounds.getSouth(), north: bounds.getNorth() }, map.getZoom())) return;
            }
            officialRasterFailuresRef.current.add(id);
            if (id === "noaa-lightning-density") setLightningPlaying(false);
            if (terrainRaster) {
              terrainRasterViewRef.current.bindSource(id, map.getSource(affectedOfficialContext.sourceId));
              terrainRasterViewRef.current.markFailed(id, erroredTile);
            }
            const rasterBounds = terrainRaster ? terrainRasterBounds() : null;
            setOfficialStates(current => ({ ...current, [id]: terrainRaster
              ? terrainRasterViewRef.current.status(id, rasterBounds!, map.getZoom(), false)
              : current[id] === "ready" || current[id] === "partial" ? "partial" : "error" }));
            setOfficialErrors(current => ({ ...current, [id]: message }));
            // A single failed display tile does not invalidate the tiles already
            // on screen. Retry the selected current source twice, then leave its
            // explicit Retry control available if the upstream is still down.
            if (id !== "noaa-goes-geocolor" && !rasterRetryTimers.has(id) && (rasterRetryCounts.get(id) ?? 0) < 2) {
              const attempt = (rasterRetryCounts.get(id) ?? 0) + 1;
              rasterRetryCounts.set(id, attempt);
              const timer = window.setTimeout(() => {
                rasterRetryTimers.delete(id);
                if (disposed || document.hidden || mapRef.current !== map || !styleGenerationReadyRef.current
                  || !officialVisibilityRef.current[id] || temporalQueryRef.current.frame !== OFFICIAL_CONTEXT_PRESENT_FRAME
                  || !map.getSource(affectedOfficialContext.sourceId)) return;
                officialRasterFailuresRef.current.delete(id);
                if (terrainRaster) terrainRasterViewRef.current.reset(id);
                setOfficialStates(current => ({ ...current, [id]: terrainRaster ? "loading" : current[id] === "partial" ? "partial" : "loading" }));
                setOfficialErrors(current => ({ ...current, [id]: undefined }));
                map.refreshTiles(affectedOfficialContext.sourceId);
              }, attempt * 6000);
              rasterRetryTimers.set(id, timer);
            }
            return;
          }
          // A missing display basemap tile must not block cutaway navigation or records.
          // That covers raster carriers and, once the one local fallback has been used,
          // the category basemaps' own vector and relief tiles.
          const basemapStyle = BASEMAPS[basemapRef.current].style;
          if (sourceId && typeof basemapStyle !== "string" && (basemapStyle.sources[sourceId]?.type === "raster" || basemapStyle.sources[sourceId]?.type === "raster-dem" || VECTOR_BASEMAPS.has(basemapRef.current) && Object.hasOwn(basemapStyle.sources, sourceId))) {
            degradedReason = "Some basemap tiles are unavailable. Gaps are unknown; choose another basemap or retry. Map controls and records remain available.";
            setRuntime({ kind: "degraded", message: degradedReason });
            return;
          }
          // Handled before the error is recorded, so a fallback that loads leaves no failure behind.
          // MapLibre includes the originating source specification on the event.
          // The stable source ID may already belong to its replacement by now.
          const terrainEventSource = (event as typeof event & { source?: { tiles?: string[] } }).source;
          const terrainTiles = sourceId === TERRAIN_SOURCE_ID ? terrainEventSource?.tiles?.[0]
            ?? (map.getSource(TERRAIN_SOURCE_ID) as { serialize?: () => { tiles?: string[] } } | undefined)?.serialize?.().tiles?.[0] ?? "" : "";
          if (terrainTiles && terrainTiles !== terrainSourceFor(terrainProviderRef.current).tileTemplate) return;
          if (terrainTiles.includes("/api/3dep-dem-tile")) {
            // A 3DEP source already replaced by the display DEM can still report tiles in flight.
            if (terrainProviderRef.current !== "usgs-3dep") return;
            if (terrainDetailRef.current.auto && !terrainDetailRef.current.failed) {
              // The automatic 3DEP detail did not load here: back to the display DEM, once.
              terrainDetailRef.current = { ...terrainDetailRef.current, auto: false, failed: true };
              terrainDetailFallbackRef.current?.();
              return;
            }
          }
          runtimeError = message;
          if (sourceId) failedSourceIds.add(sourceId);
          if (sourceId === TERRAIN_SOURCE_ID) {
            failedTerrainSourceRef.current = map.getSource(TERRAIN_SOURCE_ID);
            setTerrainState("ERROR");
            setTerrainElevationReading(null);
            setTerrainElevationUnavailable(null);
            degradedReason = `Terrain DEM is unavailable; the 2D map remains usable. ${message}`;
            setRuntime({ kind: "degraded", message: degradedReason });
            // A slow live 3DEP mosaic can fail many distinct tiles at once.
            // Leave its explicit Retry control available instead of adding
            // another automatic burst while the provider is unavailable.
            if (terrainProviderRef.current !== "usgs-3dep" && terrainRetryTimer === null && terrainRetryCount < 2) {
              terrainRetryCount += 1;
              terrainRetryTimer = window.setTimeout(() => {
                terrainRetryTimer = null;
                if (disposed || document.hidden || mapRef.current !== map || !styleGenerationReadyRef.current
                  || scenePresetRef.current !== "elevation-3d" || !map.getSource(TERRAIN_SOURCE_ID)) return;
                failedTerrainSourceRef.current = null;
                failedSourceIds.delete(TERRAIN_SOURCE_ID);
                runtimeError = null;
                degradedReason = null;
                setTerrainState("LOADING");
                map.refreshTiles(TERRAIN_SOURCE_ID);
              }, terrainRetryCount * 6000);
            }
            return;
          }
          if (sourceId === TERRAIN_HILLSHADE_SOURCE_ID) {
            if (map.getLayer(TERRAIN_HILLSHADE_LAYER_ID)) map.setLayoutProperty(TERRAIN_HILLSHADE_LAYER_ID, "visibility", "none");
            announce("Terrain shadows are unavailable; the elevation surface remains active");
            return;
          }
          if (sourceId === TERRAIN_COLOR_SOURCE_ID) {
            topographicOverlayRef.current = false;
            setTopographicOverlay(false);
            setTerrainElevationReading(null);
            setTerrainElevationUnavailable(null);
            announce("Topographic height overlay is unavailable; Terrain 3D remains active");
            return;
          }
          if (sourceId === "usgs-topo-context") {
            setRuntime({ kind: "degraded", message: `USGS topographic basemap is unavailable; provider-backed source layers remain usable. ${message}` });
            return;
          }
          setMaplibreProbe((current) => ({ ...current, error: message }));
          if (affectedLayer) {
            setSourceStates((current) => ({ ...current, [affectedLayer.id]: "error" }));
            setRuntime({ kind: "degraded", message: `${affectedLayer.title} could not load; other map layers remain available. ${message}` });
          } else if (sourceId === "osm-context") {
            setRuntime({ kind: "degraded", message: `OpenStreetMap context is unavailable; provider-backed source layers remain available. ${message}` });
          } else {
            setRuntime({ kind: "error", message: `Map runtime error: ${message}` });
          }
        });
        map.on("sourcedata", (event) => {
          if (event.sourceId === TERRAIN_SOURCE_ID && event.isSourceLoaded
            && scenePresetRef.current === "elevation-3d" && map.getTerrain()?.source === TERRAIN_SOURCE_ID
            && map.getSource(TERRAIN_SOURCE_ID) && map.isSourceLoaded(TERRAIN_SOURCE_ID)
            && attachedTerrainProviderRef.current === terrainProviderRef.current
            && terrainPresentationSourceMatches(map, terrainSourceFor(terrainProviderRef.current))
            && failedTerrainSourceRef.current !== map.getSource(TERRAIN_SOURCE_ID)) {
            setTerrainState("READY");
            failedSourceIds.delete(TERRAIN_SOURCE_ID);
            if (terrainRetryTimer !== null) { window.clearTimeout(terrainRetryTimer); terrainRetryTimer = null; }
            if (degradedReason?.startsWith("Terrain DEM is unavailable")) { degradedReason = null; runtimeError = null; }
          }
          if (!event.sourceId) return;
          const officialSource = OFFICIAL_CONTEXT_BY_SOURCE_ID[event.sourceId];
          const terrainRaster = officialSource?.id === "usgs-3dep-hillshade" || officialSource?.id === "usgs-3dep-slope";
          if (terrainRaster) {
            const source = map.getSource(event.sourceId);
            terrainRasterViewRef.current.bindSource(officialSource.id, source);
            // A completion while hidden is still in this source's cache.
            if (source && event.tile?.state === "loaded") terrainRasterViewRef.current.markLoaded(officialSource.id, event.coord?.canonical);
          }
          const rasterBounds = terrainRaster ? terrainRasterBounds() : null;
          if (officialSource && officialSource.id !== "nws-radar" && !officialSource.apiPath && !officialSource.managedAdapterPath
            && (terrainRaster ? terrainRasterViewRef.current.hasLoaded(officialSource.id as TerrainRasterId, rasterBounds!, map.getZoom()) : event.isSourceLoaded)) {
            const pendingRetry = rasterRetryTimers.get(officialSource.id);
            if (pendingRetry !== undefined) { window.clearTimeout(pendingRetry); rasterRetryTimers.delete(officialSource.id); }
            const nextState = terrainRaster
              ? terrainRasterViewRef.current.status(officialSource.id as TerrainRasterId, rasterBounds!, map.getZoom(), event.isSourceLoaded)
              : officialRasterFailuresRef.current.has(officialSource.id)
                || officialSource.id === "noaa-goes-geocolor" && (noaaSatelliteManifestRef.current?.product === "visible" || noaaSatelliteManifestRef.current?.partial || noaaSatelliteManifestRef.current?.freshness === "delayed") ? "partial" : event.isSourceLoaded ? "ready" : "loading";
            setOfficialStates(current => current[officialSource.id] === nextState ? current : ({ ...current, [officialSource.id]: nextState }));
            if (nextState === "ready") setOfficialErrors(current => current[officialSource.id] ? ({ ...current, [officialSource.id]: undefined }) : current);
          }
          const layer = LAYER_REGISTRY.find((candidate) => candidate.sourceId === event.sourceId);
          if (!layer) return;
          setSourceActivity((current) => ({
            ...current,
            [layer.id]: event.isSourceLoaded ? "SETTLED" : "UPDATING",
          }));
        });
        map.on("idle", () => {
          runMapMutation("Map readiness check", () => {
            syncTerrainRasterView();
            if (scenePresetRef.current === "elevation-3d" && map.getTerrain()?.source === TERRAIN_SOURCE_ID
              && map.getSource(TERRAIN_SOURCE_ID) && map.isSourceLoaded(TERRAIN_SOURCE_ID)
              && attachedTerrainProviderRef.current === terrainProviderRef.current
              && terrainPresentationSourceMatches(map, terrainSourceFor(terrainProviderRef.current))
              && failedTerrainSourceRef.current !== map.getSource(TERRAIN_SOURCE_ID)) {
              setTerrainState("READY");
            }
            const probe = refreshMaplibreProbe();
            const mutationError = mapMutationErrorRef.current;
            const ready = probe.styleLoaded
              && probe.canvasReady
              && probe.tilesLoaded
              && probe.sourcesReady === LAYER_REGISTRY.length
              && probe.interactionsReady
              && probe.failedChecks.length === 0
              && !runtimeError
              && !degradedReason
              && !mutationError;
            if (!ready) {
              const failedCheckMessage = probe.failedChecks.length ? `Map health checks need attention: ${probe.failedChecks.join(", ")}.` : null;
              const next: RuntimeState = { kind: runtimeError || degradedReason || mutationError || failedCheckMessage ? "degraded" : "loading", message: failedCheckMessage ?? (runtimeError ? `MapLibre runtime proof is incomplete: ${runtimeError}` : degradedReason ?? mutationError ?? "MapLibre is waiting for all admitted local capabilities to settle…") };
              setRuntime((current) => sameValues(current, next) ? current : next);
              return;
            }
            const next: RuntimeState = { kind: "ready", message: `MapLibre ${version} ready · ${LAYER_REGISTRY.length} catalog layers · interactions proven` };
            setRuntime((current) => sameValues(current, next) ? current : next);
          });
        });
      } catch {
        const message = mapRuntimeErrorCode("start");
        setMaplibreProbe((current) => ({ ...current, error: message }));
        setRuntime({ kind: "error", message: `MapLibre could not start: ${message}` });
      }
    }).catch(() => {
      const message = mapRuntimeErrorCode("load");
      setMaplibreProbe((current) => ({ ...current, error: message }));
      setRuntime({ kind: "error", message: `MapLibre could not load: ${message}` });
    });

    return () => {
      disposed = true;
      for (const timer of rasterRetryTimers.values()) window.clearTimeout(timer);
      if (terrainRetryTimer !== null) window.clearTimeout(terrainRetryTimer);
      if (hoverDrawerTimerRef.current !== null) window.clearTimeout(hoverDrawerTimerRef.current);
      hoverDrawerTimerRef.current = null;
      hoverCandidateIdRef.current = null;
      cancelHoverSample();
      cancelSettledViewCommit();
      if (mapResizeFrame !== undefined) window.cancelAnimationFrame(mapResizeFrame);
      resizeObserver?.disconnect();
      styleDocumentLoadedRef.current = false;
      styleGenerationReadyRef.current = false;
      sceneOrbitCancelRef.current?.();
      sceneOrbitCancelRef.current = null;
      flyoverCancelRef.current?.();
      flyoverCancelRef.current = null;
      if (sceneOrbitTimerRef.current !== null) window.clearTimeout(sceneOrbitTimerRef.current);
      terrainDrawingRef.current?.destroy();
      terrainDrawingRef.current = null;
      stopStormDeskProbe();
      mapRef.current?.remove();
      mapRef.current = null;
    };
  }, [announce, runMapMutation, runtimeOfficialVisibility]);

  useEffect(() => {
    const map = mapRef.current;
    if (!map || !styleGenerationReadyRef.current) return;
    runMapMutation("Layer-state update", () => {
      applyRegistryState(map, visibility, opacity, yearRef.current, layerOrder, mapEvidenceFilter, temporalQueryRef.current);
      setElevationExaggeration(map, verticalExaggerationRef.current);
    });
  }, [layerOrder, mapEvidenceFilter, opacity, runMapMutation, visibility]);

  useEffect(() => {
    roadStudyLayersRef.current = roadStudyLayers;
    const map = mapRef.current;
    if (!map || !styleGenerationReadyRef.current) return;
    runMapMutation("Browser-local road study update", () => applyRoadStudyLayers(map, roadStudyLayers));
  }, [roadStudyLayers, runMapMutation, styleReady]);

  useEffect(() => {
    const map = mapRef.current;
    if (!map || !styleGenerationReadyRef.current) return;
    const hovered = hoveredRef.current;
    if (hovered && map.getSource(hovered.source)) {
      try { map.setFeatureState(hovered, { hover: false }); } catch { /* A filtered or replaced source has no hover state to clear. */ }
    }
    hoveredRef.current = null;
    setHoverSummary(null);
    map.getCanvas().style.cursor = "";
    runMapMutation("Timeline filter update", () => applyTemporalRegistryFilters(map, year, mapEvidenceFilter, temporalQuery));
  }, [mapEvidenceFilter, runMapMutation, temporalQuery, year]);

  useEffect(() => {
    const map = mapRef.current;
    if (!map || !styleGenerationReadyRef.current) return;
    runMapMutation("Official-source map update", () => {
      if (noaaRadarPendingFrameTime) {
        if (!noaaRadarSelectedAtPresent) applyOfficialContextState(map, effectiveOfficialVisibility, officialOpacity, officialPayloads);
        else if (noaaRadarFrameLoadState !== "loading") applyNoaaRadarFrame(noaaRadarPendingFrameTime);
        return;
      }
      if (noaaRadarRenderable && noaaRadarFrameTime && !noaaRadarObservationTimeIsApplied(map, noaaRadarFrameTime)) {
        applyNoaaRadarFrame(noaaRadarFrameTime);
        return;
      }
      applyOfficialContextState(map, effectiveOfficialVisibility, officialOpacity, officialPayloads);
    });
  }, [applyNoaaRadarFrame, effectiveOfficialVisibility, noaaRadarFrameLoadState, noaaRadarFrameTime, noaaRadarPendingFrameTime, noaaRadarRenderable, noaaRadarSelectedAtPresent, officialOpacity, officialPayloads, runMapMutation, styleReady]);

  const directionStationId = streamflowSelectedStation?.stationId ?? null;
  const directionLongitude = streamflowSelectedStation?.longitude ?? null;
  const directionLatitude = streamflowSelectedStation?.latitude ?? null;
  useEffect(() => {
    if (!streamflowSelectedAtPresent || !directionStationId || directionLongitude === null || directionLatitude === null) {
      setDownstreamPaths([]);
      setDownstreamAnalysis(null);
      setDownstreamStationId(null);
      setDownstreamState("idle");
      return;
    }
    const cacheKey = `${directionStationId}:${directionLongitude}:${directionLatitude}`;
    const cached = directionGuideCacheRef.current.get(cacheKey);
    if (cached && cached.expiresAt > Date.now()) {
      setDownstreamPaths(cached.guide.paths);
      setDownstreamAnalysis(cached.guide.analysis ?? null);
      setDownstreamStationId(directionStationId);
      setDownstreamState(cached.guide.state);
      return;
    }
    directionGuideCacheRef.current.delete(cacheKey);
    const controller = new AbortController();
    setDownstreamPaths([]);
    setDownstreamAnalysis(null);
    setDownstreamStationId(null);
    setDownstreamState("loading");
    const load = async () => {
      try {
        const params = new URLSearchParams({ lon: String(directionLongitude), lat: String(directionLatitude), stream: "1" });
        const response = await fetch(`/api/hydrology/direction?${params}`, { signal: controller.signal, headers: { Accept: "application/x-ndjson" } });
        if (!response.ok) throw new Error("Mapped direction unavailable.");
        const guide = await readProgressiveDownstreamGuide(response, nearby => {
          if (controller.signal.aborted) return;
          setDownstreamPaths(nearby.paths);
          setDownstreamAnalysis(nearby.analysis ?? null);
          setDownstreamStationId(directionStationId);
        }, controller.signal);
        if (controller.signal.aborted) return;
        if (directionGuideCacheRef.current.size >= 24) directionGuideCacheRef.current.delete(directionGuideCacheRef.current.keys().next().value!);
        directionGuideCacheRef.current.set(cacheKey, { guide, expiresAt: Date.now() + 15 * 60_000 });
        setDownstreamPaths(guide.paths);
        setDownstreamAnalysis(guide.analysis ?? null);
        setDownstreamStationId(directionStationId);
        setDownstreamState(guide.state);
      } catch {
        if (!controller.signal.aborted) {
          controller.abort();
          setDownstreamPaths([]);
          setDownstreamAnalysis(null);
          setDownstreamState("error");
        }
      }
    };
    void load();
    return () => controller.abort();
  }, [streamflowSelectedAtPresent, directionStationId, directionLongitude, directionLatitude]);

  useEffect(() => {
    if (!downstreamStationId || (downstreamState !== "ready" && downstreamAnalysis?.upstreamM === undefined) || riverPathFocusRef.current !== downstreamStationId || downstreamStationId !== streamflowSelectedStationId || !downstreamPaths.length) return;
    const map = mapRef.current;
    if (!map) return;
    if (downstreamState === "ready") riverPathFocusRef.current = null;
    const points = downstreamPaths.flatMap(path => path.coordinates);
    const longitudes = points.map(point => point[0]), latitudes = points.map(point => point[1]);
    map.fitBounds([[Math.min(...longitudes), Math.min(...latitudes)], [Math.max(...longitudes), Math.max(...latitudes)]], {
      padding: { top: 60, left: 55, right: 55, bottom: Math.min(450, map.getCanvas().clientHeight * .6) }, maxZoom: 13, duration: reducedMotion ? 0 : 1000,
    });
  }, [downstreamAnalysis, downstreamPaths, downstreamState, downstreamStationId, reducedMotion, streamflowSelectedStationId]);

  useEffect(() => {
    const map = mapRef.current;
    const canvas = waterMotionCanvasRef.current;
    if (primaryWorkspace !== "map" || !map || !canvas || !styleReady || !streamflowSelectedAtPresent || !streamflowFrame) {
      canvas?.getContext("2d")?.clearRect(0, 0, canvas.width, canvas.height);
      return;
    }
    const motionHealthy = streamflowDisplayState === "ready" || streamflowDisplayState === "partial";
    const animateDirection = motionHealthy && dynamicEffects && !reducedMotion && downstreamPaths.length > 0
      && selectedWaterCue.value !== null && selectedWaterCue.value > 0;
    const animate = animateDirection;
    let timer = 0;
    let lastDraw = 0;
    const render = () => {
      if (!document.hidden) drawWaterMotionCanvas(canvas, map, streamflowFrame, streamflowSelectedStationId,
        downstreamPaths, selectedWaterCue, performance.now(), false, animateDirection);
    };
    const tick = (now: number) => {
      timer = 0;
      if (now - lastDraw >= 1000 / 30) { render(); lastDraw = now; }
      if (animate && !document.hidden) timer = window.requestAnimationFrame(tick);
    };
    const visibility = () => {
      window.cancelAnimationFrame(timer);
      timer = 0;
      if (!document.hidden) { render(); if (animate) timer = window.requestAnimationFrame(tick); }
    };
    map.on("move", render);
    map.on("resize", render);
    document.addEventListener("visibilitychange", visibility);
    render();
    if (animate) timer = window.requestAnimationFrame(tick);
    return () => {
      map.off("move", render);
      map.off("resize", render);
      document.removeEventListener("visibilitychange", visibility);
      window.cancelAnimationFrame(timer);
      canvas.getContext("2d")?.clearRect(0, 0, canvas.width, canvas.height);
    };
  }, [primaryWorkspace, streamflowDisplayState, downstreamPaths, dynamicEffects, reducedMotion, selectedWaterCue, streamflowFrame, streamflowPlaying, streamflowSelectedAtPresent, streamflowSelectedStationId, styleReady]);

  useEffect(() => {
    const map = mapRef.current;
    const canvas = windArrowCanvasRef.current;
    const selected = primaryWorkspace === "map" && buildYearCurrent && windLayerSelected
      && temporalQuery.frame === OFFICIAL_CONTEXT_PRESENT_FRAME;
    if (!map || !canvas || !styleReady || !selected) {
      setWindArrowState("OFF");
      setWindArrowFrame(null);
      setWindArrowDirect(false);
      setWindArrowHover(null);
      canvas?.getContext("2d")?.clearRect(0, 0, canvas.width, canvas.height);
      return;
    }
    let disposed = false;
    let frame: WindArrowFrame | null = null;
    let controller: AbortController | null = null;
    let debounceTimer = 0;
    let drawTimer = 0;
    let lastDraw = -Infinity;
    const animated = dynamicEffects && !reducedMotion;
    // Streamlines live on the ground and are re-projected on every camera
    // move, so they stay glued to the map while it pans, rotates or pitches.
    // Idle motion is paced to ~30 fps; nothing runs while the tab is hidden.
    const render = () => {
      if (disposed || !frame || document.hidden) return;
      lastDraw = performance.now();
      // Line colours follow the active basemap (dark lines on light maps).
      drawWindFlowCanvas(canvas, map, frame, lastDraw, animated, windFlowToneForBasemap(basemapRef.current));
    };
    const tick = (now: number) => {
      drawTimer = 0;
      if (now - lastDraw >= 31) render();
      startMotion();
    };
    const startMotion = () => {
      if (animated && frame && !disposed && !document.hidden && !drawTimer) drawTimer = window.requestAnimationFrame(tick);
    };
    const onVisibilityChange = () => {
      if (document.hidden) { window.cancelAnimationFrame(drawTimer); drawTimer = 0; }
      else { render(); startMotion(); }
    };
    const onPointerMove = (event: { point: { x: number; y: number } }) => {
      const sample = frame && !map.isMoving() ? nearestWindFlowSample(map, frame, event.point.x, event.point.y) : null;
      setWindArrowHover(sample ? {
        sample,
        screenX: Math.max(12, Math.min(event.point.x + 18, map.getCanvas().clientWidth - 220)),
        screenY: event.point.y > map.getCanvas().clientHeight - 230
          ? Math.max(12, event.point.y - (scenePresetRef.current === "elevation-3d" ? 170 : 98))
          : event.point.y + (scenePresetRef.current === "elevation-3d" ? 106 : 20),
      } : null);
    };
    const onPointerLeave = () => setWindArrowHover(null);
    const onMapMove = () => render();
    const load = async () => {
      const bounds = map.getBounds();
      const center = map.getCenter();
      const west = Math.max(-102.1, Math.min(bounds.getWest(), center.lng - 0.08));
      const east = Math.min(-94.5, Math.max(bounds.getEast(), center.lng + 0.08));
      const south = Math.max(36.9, Math.min(bounds.getSouth(), center.lat - 0.06));
      const north = Math.min(40.1, Math.max(bounds.getNorth(), center.lat + 0.06));
      controller?.abort();
      frame = null;
      window.cancelAnimationFrame(drawTimer);
      drawTimer = 0;
      setWindArrowHover(null);
      canvas.getContext("2d")?.clearRect(0, 0, canvas.width, canvas.height);
      if (east - west < 0.02 || north - south < 0.02) {
        setWindArrowState("ERROR");
        setWindArrowFrame(null);
        return;
      }
      const requestController = new AbortController();
      controller = requestController;
      setWindArrowState("LOADING");
      setWindArrowFrame(null);
      setWindArrowDirect(false);
      try {
        const bbox = [west, south, east, north].map(value => value.toFixed(3)).join(",");
        const { frame: next, transport } = await loadWindFlowFrame(bbox, requestController.signal);
        if (disposed || requestController.signal.aborted) return;
        frame = next;
        setWindArrowFrame(next);
        setWindArrowDirect(transport === "direct-provider");
        setWindArrowState("READY");
        render();
        startMotion();
      } catch (error) {
        if (disposed || requestController.signal.aborted || (error instanceof DOMException && error.name === "AbortError")) return;
        frame = null;
        setWindArrowFrame(null);
        setWindArrowDirect(false);
        setWindArrowState("ERROR");
      }
    };
    const schedule = () => { window.clearTimeout(debounceTimer); debounceTimer = window.setTimeout(() => void load(), 350); };
    map.on("moveend", schedule);
    map.on("move", onMapMove);
    map.on("resize", render);
    map.on("mousemove", onPointerMove);
    map.getCanvas().addEventListener("mouseleave", onPointerLeave);
    document.addEventListener("visibilitychange", onVisibilityChange);
    const refreshTimer = window.setInterval(() => void load(), 10 * 60_000);
    void load();
    return () => {
      disposed = true;
      controller?.abort();
      map.off("moveend", schedule);
      map.off("move", onMapMove);
      map.off("resize", render);
      map.off("mousemove", onPointerMove);
      map.getCanvas().removeEventListener("mouseleave", onPointerLeave);
      document.removeEventListener("visibilitychange", onVisibilityChange);
      window.clearInterval(refreshTimer);
      window.clearTimeout(debounceTimer);
      window.cancelAnimationFrame(drawTimer);
      setWindArrowHover(null);
      resetWindFlowCanvas(canvas);
      canvas.getContext("2d")?.clearRect(0, 0, canvas.width, canvas.height);
    };
  }, [primaryWorkspace, buildYearCurrent, dynamicEffects, windLayerSelected, reducedMotion, styleReady, temporalQuery.frame, windArrowReloadToken]);

  useEffect(() => {
    const next: OfficialContextState = windArrowState === "READY" ? "ready" : windArrowState === "LOADING" ? "loading" : windArrowState === "ERROR" ? "error" : "idle";
    setOfficialStates(current => current["nws-forecast-wind"] === next ? current : ({ ...current, "nws-forecast-wind": next }));
    setOfficialErrors(current => {
      const message = windArrowState === "ERROR" ? "GFS wind forecast unavailable or outside the supported Kansas area." : undefined;
      return current["nws-forecast-wind"] === message ? current : ({ ...current, "nws-forecast-wind": message });
    });
  }, [windArrowState]);

  useEffect(() => {
    setTerrainElevationReading(null);
    setTerrainElevationUnavailable(null);
  }, [scenePreset, terrainProvider]);

  useEffect(() => {
    const map = mapRef.current;
    if (!map || !styleGenerationReadyRef.current) return;
    runMapMutation("Elevation-scale update", () => setElevationExaggeration(map, verticalExaggeration));
  }, [runMapMutation, verticalExaggeration]);

  useEffect(() => {
    const map = mapRef.current;
    if (!map || !styleGenerationReadyRef.current) {
      setTerrainState(scenePreset === "elevation-3d" ? "LOADING" : "OFF");
      return;
    }
    runMapMutation("Terrain presentation update", () => {
      const state = setTerrainPresentation(map, scenePreset === "elevation-3d", verticalExaggeration);
      setTerrainHeightOverlay(map, scenePreset === "elevation-3d" && topographicOverlayRef.current && state !== "ERROR");
      const source = map.getSource(TERRAIN_SOURCE_ID);
      setTerrainState(terrainSourceLoadState(state, Boolean(source && attachedTerrainProviderRef.current === terrainProvider && map.isSourceLoaded(TERRAIN_SOURCE_ID)),
        Boolean(source && failedTerrainSourceRef.current === source)));
    });
  }, [runMapMutation, scenePreset, styleReady, terrainProvider, verticalExaggeration]);

  useEffect(() => {
    const map = mapRef.current;
    if (!map || !styleGenerationReadyRef.current) {
      setStructures3DState(structures3DEnabled ? "UNAVAILABLE" : "OFF");
      return;
    }
    runMapMutation("Structure presentation update", () => setStructures3DState(setStructureExtrusions(map, structures3DEnabled)));
  }, [runMapMutation, structures3DEnabled, styleReady]);

  useEffect(() => {
    const map = mapRef.current;
    if (!map || !styleGenerationReadyRef.current) return;
    let animationFrame = 0;
    let lastFrame = 0;
    const budget = browserRenderBudget(renderQuality);
    const liveWaterSelected = buildYearCurrent && temporalQuery.frame === OFFICIAL_CONTEXT_PRESENT_FRAME
      && (officialVisibility["usgs-streamflow"] || officialVisibility["noaa-nwps-gauges"]);
    // Paint animation keeps MapLibre from becoming idle. Let the style and
    // source readiness check finish before starting ambient motion, including
    // after a basemap swap.
    const effectsActive = primaryWorkspace === "map" && runtime.kind === "ready" && projection !== "globe" && dynamicEffects && !reducedMotion && !budget.efficient
      && liveWaterSelected;

    // A soft marker halo is presentation only. The provider's observation,
    // forecast, trend, magnitude, and timestamp remain fixed between fetches.
    const emphasizeWaterStations = (timestamp: number, active: boolean) => {
      const pulse = active ? 0.76 + 0.24 * (Math.sin(timestamp / 760) + 1) / 2 : 1;
      for (const id of ["usgs-streamflow", "noaa-nwps-gauges"] as const) {
        const layerId = OFFICIAL_CONTEXT_BY_ID[id].layerIds[0];
        if (!map.getLayer(layerId)) continue;
        const target = (officialOpacityRef.current[id] ?? OFFICIAL_CONTEXT_BY_ID[id].defaultOpacity) * 0.3 * pulse;
        if (map.getPaintProperty(layerId, "circle-opacity") !== target) map.setPaintProperty(layerId, "circle-opacity", target);
      }
    };

    if (!effectsActive) {
      runMapMutation("Map-effect reset", () => { applyDynamicMapEffects(map, 0, opacity, false); emphasizeWaterStations(0, false); });
      return;
    }

    const renderEffects = (timestamp: number) => {
      if (!document.hidden && !map.isMoving() && timestamp - lastFrame >= 80 && styleGenerationReadyRef.current) {
        if (!runMapMutation("Dynamic map effect", () => { applyDynamicMapEffects(map, timestamp, opacity, true); emphasizeWaterStations(timestamp, liveWaterSelected); })) return;
        lastFrame = timestamp;
      }
      if (!document.hidden) animationFrame = window.requestAnimationFrame(renderEffects);
    };
    const resume = () => { window.cancelAnimationFrame(animationFrame); if (!document.hidden) animationFrame = window.requestAnimationFrame(renderEffects); };
    document.addEventListener("visibilitychange", resume); resume();
    return () => {
      window.cancelAnimationFrame(animationFrame);
      document.removeEventListener("visibilitychange", resume);
      if (styleGenerationReadyRef.current) runMapMutation("Map-effect cleanup", () => { applyDynamicMapEffects(map, 0, opacity, false); emphasizeWaterStations(0, false); });
    };
  }, [primaryWorkspace, buildYearCurrent, dynamicEffects, officialVisibility, opacity, projection, reducedMotion, renderQuality, runMapMutation, runtime.kind, styleReady, temporalQuery.frame, visibility]);

  useEffect(() => {
    const map = mapRef.current;
    if (!map) return;
    const pendingRadarFrame = noaaRadarPendingFrameTimeRef.current;
    noaaRadarFrameLoadCleanupRef.current?.();
    noaaRadarFrameLoadCleanupRef.current = null;
    noaaRadarFrameFailureRef.current = null;
    if (pendingRadarFrame) setNoaaRadarFrameLoadState("idle");
    if (!runMapMutation("Basemap style update", () => map.setStyle(hiDpiBasemapStyle(BASEMAPS[basemap].style, map.getPixelRatio()), { diff: false }))) return;
    styleDocumentLoadedRef.current = false;
    styleGenerationReadyRef.current = false;
    attachedTerrainProviderRef.current = null;
    officialRasterFailuresRef.current.clear();
    terrainRasterViewRef.current.resetAll();
    setOfficialStates(current => {
      const next = { ...current };
      for (const source of OFFICIAL_CONTEXT_SOURCES) {
        if (source.kind === "OPERATIONAL_WMS" && source.id !== "nws-radar" && officialVisibilityRef.current[source.id]) next[source.id] = "loading";
      }
      return next;
    });
    setTerrainElevationReading(null);
    setTerrainElevationUnavailable(null);
    setPlaying(false);
    setStyleReady(false);
    setTerrainState(scenePresetRef.current === "elevation-3d" ? "LOADING" : "OFF");
    setMaplibreProbe((current) => ({ ...current, styleLoaded: false, idle: false, tilesLoaded: false, sourcesReady: 0 }));
    setRuntime({ kind: "loading", message: `Applying ${BASEMAPS[basemap].title} style…` });
  }, [basemap, runMapMutation]);

  useEffect(() => {
    const selectionVisible = Boolean(selected && !selectedTimeMismatch && !selectedLayerHidden && !selectedEvidenceFiltered);
    const map = mapRef.current;
    if (!map || !styleGenerationReadyRef.current) return;
    runMapMutation("Selection update", () => updateSelectionSource(map, selectionVisible && selected ? selected.geometry : null));
  }, [runMapMutation, selected, selectedEvidenceFiltered, selectedLayerHidden, selectedTimeMismatch]);

  useEffect(() => {
    const map = mapRef.current;
    if (!map || !styleGenerationReadyRef.current) return;
    runMapMutation("Projection update", () => {
      applyProjectionNavigationLimits(map, projection);
      map.setProjection({ type: projection });
      // Current WMS overlays are regional Mercator tile carriers. Re-apply their
      // visibility after a projection change so globe mode cannot retain a
      // stretched or color-shifted raster from the prior 2D view.
      applyOfficialContextState(map, effectiveOfficialVisibility, officialOpacity, officialPayloads);
      setMaplibreProbe((current) => ({ ...current, projection }));
    });
  }, [effectiveOfficialVisibility, officialOpacity, officialPayloads, projection, runMapMutation]);

  useEffect(() => {
    const map = mapRef.current;
    if (!map || !styleReady || !styleGenerationReadyRef.current) return;
    const resampling = noaaRadarSmooth ? "linear" : "nearest";
    for (const id of ["external-nws-radar-raster", "external-nws-radar-raster-buffer"]) {
      if (map.getLayer(id) && map.getPaintProperty(id, "raster-resampling") !== resampling) map.setPaintProperty(id, "raster-resampling", resampling);
    }
    const halo = "external-nasa-gibs-fire-points-halo";
    if (map.getLayer(halo)) {
      const radius: ["interpolate", ["linear"], ["zoom"], number, number, number, number] = fireVisualMode === "soft"
        ? ["interpolate", ["linear"], ["zoom"], 4, 22, 10, 36]
        : ["interpolate", ["linear"], ["zoom"], 4, 14, 10, 20];
      map.setPaintProperty(halo, "circle-radius", radius);
      map.setPaintProperty(halo, "circle-blur", fireVisualMode === "soft" ? 0.9 : 0.55);
    }
  }, [fireVisualMode, noaaRadarSmooth, noaaRadarFrameTime, noaaRadarPendingFrameTime, officialPayloads, styleReady]);

  useEffect(() => {
    const map = mapRef.current;
    if (!map || !styleGenerationReadyRef.current) return;
    runMapMutation("Scene-light update", () => {
      applySceneEnvironment(map, atmospherePreset, lightAzimuth);
      if (scenePreset === "elevation-3d") {
        applyTerrainReliefStyle(map, basemap === "topo" ? "topographic" : "general", atmospherePreset, lightAzimuth);
      }
      applyTopographicRasterDepth(map, scenePreset === "elevation-3d" && basemap === "topo" && terrainState === "READY");
      map.setVerticalFieldOfView(fieldOfView);
    });
  }, [atmospherePreset, basemap, fieldOfView, lightAzimuth, runMapMutation, scenePreset, styleReady, terrainState]);

  useEffect(() => {
    const stored = sceneEffectsForTopic(readSceneEffects(), "all");
    sceneEffectsRef.current = stored;
    setSceneEffects(stored);
  }, []);

  useEffect(() => {
    const next = sceneEffectsForTopic(sceneEffectsRef.current, officialWorkspace);
    if (next === sceneEffectsRef.current) return;
    sceneEffectsRef.current = next;
    setSceneEffects(next);
    writeSceneEffects(next);
  }, [officialWorkspace]);

  useEffect(() => {
    if (!sceneEffects.sunSync) return;
    setSunClock(Date.now());
    const timer = window.setInterval(() => setSunClock(Date.now()), 60_000);
    return () => window.clearInterval(timer);
  }, [sceneEffects.sunSync]);

  // Scene effects are display treatment; re-apply them whenever the settings,
  // style generation, projection, render budget or (when following it) the sun changes.
  useEffect(() => {
    sceneEffectsRef.current = sceneEffects;
    const map = mapRef.current;
    if (!map) return;
    registerSceneEffects(map, sceneEffects);
    registerSunInstant(map, sunStudyAt);
    if (!styleGenerationReadyRef.current) return;
    runMapMutation("Scene-effect update", () => {
      applySceneEnvironment(map, atmospherePresetRef.current, lightAzimuthRef.current);
      if (scenePresetRef.current === "elevation-3d") {
        applyTerrainReliefStyle(map, basemapRef.current === "topo" ? "topographic" : "general", atmospherePresetRef.current, lightAzimuthRef.current);
      }
      syncBorderCurtain(map, renderEfficientRef.current);
      map.triggerRepaint();
    });
  }, [projection, renderQuality, runMapMutation, sceneEffects, styleReady, sunClock, sunStudyAt]);

  // Overlays follow the view, light, terrain state and the official point layers.
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !styleGenerationReadyRef.current) return;
    syncSceneOverlays(map, atmospherePresetRef.current, lightAzimuthRef.current, renderEfficientRef.current);
  }, [atmospherePreset, basemap, effectiveOfficialVisibility, lightAzimuth, officialOpacity, officialPayloads, projection, renderQuality, sceneEffects, scenePreset, structures3DState, styleReady, sunClock, sunStudyAt, terrainState]);

  // The renderer owns sampling, cancellation and source listeners. React only
  // supplies explicit presentation choices; changing a palette never remounts it.
  useEffect(() => {
    const map = mapRef.current;
    const light = map ? effectiveSceneLight(map, atmospherePreset, lightAzimuth, sunAt) : { preset: atmospherePreset, azimuth: lightAzimuth };
    const config: TerrainDrawingConfig = {
      mode: terrainDrawingMode, surface: terrainSurfaceMode, surfaceOpacity: terrainSurfaceOpacity, probeEnabled: !measureMode,
      enabled: styleReady && styleGenerationReadyRef.current && scenePreset === "elevation-3d" && projection === "mercator" && !undergroundOpen,
      provider: terrainProvider, efficient: browserRenderBudget(renderQuality).efficient,
      detail: terrainDrawingDetail, light: light.preset, azimuth: light.azimuth,
    };
    terrainDrawingConfigRef.current = config;
    terrainDrawingRef.current?.update(config);
    if (measureMode) setTerrainSurfaceProbe(null);
    if (!map && (terrainDrawingMode !== "off" || terrainSurfaceMode !== "off")) setTerrainDrawingStatus({ ...TERRAIN_DRAWING_INITIAL_STATUS, state: "unavailable", message: "Waiting for the map. Then choose Terrain 3D to draw its loaded elevations." });
  }, [atmospherePreset, lightAzimuth, measureMode, projection, renderQuality, sceneEffects.sunSync, scenePreset, styleReady, sunAt, terrainDrawingDetail, terrainDrawingMode, terrainProvider, terrainState, terrainSurfaceMode, terrainSurfaceOpacity, undergroundOpen]);

  const chooseTerrainDrawingMode = (mode: TerrainDrawingMode) => {
    const config = { ...terrainDrawingConfigRef.current, mode };
    terrainDrawingConfigRef.current = config;
    terrainDrawingRef.current?.update(config);
    setTerrainDrawingMode(mode);
  };
  const chooseTerrainSurfaceMode = (surface: TerrainSurfaceMode) => {
    const config = { ...terrainDrawingConfigRef.current, surface };
    terrainDrawingConfigRef.current = config;
    terrainDrawingRef.current?.update(config);
    if (surface === "off") setTerrainSurfaceProbe(null);
    setTerrainSurfaceMode(surface);
  };
  const chooseTerrainSurfaceOpacity = (value: number) => {
    const surfaceOpacity = Number.isFinite(value) ? clamp(value, 0.2, 0.75) : 0.55;
    const config = { ...terrainDrawingConfigRef.current, surfaceOpacity };
    terrainDrawingConfigRef.current = config;
    terrainDrawingRef.current?.update(config);
    setTerrainSurfaceOpacity(surfaceOpacity);
  };
  const sampleTerrainSurfaceCenter = () => {
    if (!measureModeRef.current) terrainDrawingRef.current?.probeCenter();
  };
  const chooseTerrainDrawingDetail = (detail: boolean) => {
    const config = { ...terrainDrawingConfigRef.current, detail };
    terrainDrawingConfigRef.current = config;
    terrainDrawingRef.current?.update(config);
    setTerrainDrawingDetail(detail);
  };

  useEffect(() => {
    if (sceneOrbitCancelRef.current && (reducedMotion || undergroundOpen || sceneOrbitContextRef.current !== `${projection}/${scenePreset}/${basemap}`)) stopSceneOrbit(false);
    if (flyoverCancelRef.current && (reducedMotion || undergroundOpen || projection !== "mercator" || scenePreset !== "elevation-3d")) stopFlyover(false);
  }, [basemap, projection, reducedMotion, scenePreset, stopFlyover, stopSceneOrbit, undergroundOpen]);

  // The curtain shimmer and star twinkle repaint at ~15 fps, and flowing
  // water at ~30 fps, only while they are on screen and ambient motion is
  // allowed; otherwise they hold still.
  useEffect(() => {
    const map = mapRef.current;
    const motionAllowed = runtime.kind === "ready" && dynamicEffects && !reducedMotion && !browserRenderBudget(renderQuality).efficient;
    const shimmer = motionAllowed && sceneEffects.curtain;
    const twinkle = motionAllowed && sceneEffects.stars;
    const flowing = motionAllowed && sceneEffects.waterFlow;
    setCurtainShimmer(shimmer);
    setNightSkyTwinkle(twinkle);
    setWaterFlowMotion(flowing);
    if (!map || !(shimmer || twinkle || flowing)) return;
    let frame = 0;
    let last = 0;
    const tick = (now: number) => {
      let water = false;
      try { water = flowing && waterFlowIsAnimating(map); } catch { /* style swap in progress */ }
      if (!document.hidden && now - last >= (water ? 33 : 66)) {
        last = now;
        try { if (water || (shimmer && curtainIsVisible(map)) || (twinkle && nightSkyIsTwinkling(map))) map.triggerRepaint(); } catch { /* style swap in progress */ }
      }
      frame = window.requestAnimationFrame(tick);
    };
    frame = window.requestAnimationFrame(tick);
    return () => { window.cancelAnimationFrame(frame); setCurtainShimmer(false); setNightSkyTwinkle(false); setWaterFlowMotion(false); };
  }, [dynamicEffects, reducedMotion, renderQuality, runtime.kind, sceneEffects.curtain, sceneEffects.stars, sceneEffects.waterFlow]);

  // The Scene panel reports what the flowing-water layer could draw.
  const [waterFlowState, setWaterFlowState] = useState<WaterFlowStatus | null>(null);
  useEffect(() => subscribeWaterFlowStatus(setWaterFlowState), []);
  const sceneReadings = useMemo(() => ({ waterFlow: waterFlowState ? waterFlowReading(waterFlowState) : null }), [waterFlowState]);

  // Terrain 3D may tilt further so the sky and horizon come into view.
  useEffect(() => {
    const map = mapRef.current;
    if (!map) return;
    runMapMutation("Camera pitch range update", () => map.setMaxPitch(scenePreset === "elevation-3d" ? 72 : 60));
  }, [runMapMutation, scenePreset, styleReady]);

  // A short ping marks a newly selected point. It stops by itself so the map
  // returns to idle, and is skipped for reduced motion or with ambient motion off.
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !styleGenerationReadyRef.current || !selected || selected.geometry.geometry.type !== "Point" || reducedMotion || !dynamicEffects) return;
    let frame = 0;
    const started = performance.now();
    const step = (now: number) => {
      let running = false;
      try { running = applySelectionPulse(map, now - started); } catch { return; }
      if (running) frame = window.requestAnimationFrame(step);
    };
    frame = window.requestAnimationFrame(step);
    return () => {
      window.cancelAnimationFrame(frame);
      try { applySelectionPulse(map, Number.POSITIVE_INFINITY); } catch { /* style may be gone */ }
    };
  }, [dynamicEffects, reducedMotion, selected, styleReady]);

  const sceneView: SceneView = projection === "globe" ? "globe" : scenePreset === "elevation-3d" ? "terrain" : view.pitch >= CURTAIN_MIN_PITCH ? "tilted" : "2d";

  const chooseSceneView = (mode: SceneView) => {
    if (mode === "terrain" || mode === "globe" || mode === "2d") {
      activateMapRepresentation(mode);
      return;
    }
    // Tilted 2D keeps the flat evidence map but shows curtain and buildings.
    if (projectionRef.current === "globe" || scenePresetRef.current === "elevation-3d") activateMapRepresentation("2d");
    replayingCameraHistoryRef.current = false;
    mapRef.current?.easeTo({ pitch: 56, bearing: Math.abs(view.bearing) < 1 ? -14 : view.bearing, duration: motionDuration(650) });
    announce("Tilted the 2D map · data, time and selection unchanged");
  };

  const updateSceneEffects = (next: SceneEffectSettings) => {
    // Turning the real sun on or off from any control ends a time-of-day study.
    if (next.sunSync !== sceneEffectsRef.current.sunSync) { setSunStudyAt(null); setSunPlaying(false); }
    sceneEffectsRef.current = next;
    setSceneEffects(next);
    writeSceneEffects(next);
    const changed = (Object.keys(next) as (keyof SceneEffectSettings)[]).find((key) => next[key] !== sceneEffects[key]);
    const label = SCENE_EFFECT_OPTIONS.find((option) => option.key === changed)?.label;
    const preset = matchingLookPreset(next);
    if (changed && label && SCENE_EFFECT_KEYS.filter((key) => next[key] !== sceneEffects[key]).length === 1) announce(`${label} ${next[changed] ? "on" : "off"} · display only`);
    else if (preset) announce(`${SCENE_LOOK_PRESETS[preset].label} look applied · display only`);
  };

  // Play the day starts from the shown time, or from 5:00 AM once the day has been played out.
  const playSunDay = (on: boolean) => {
    if (!on) { setSunPlaying(false); return; }
    const day = kansasLocalDayInterval(currentKansasCalendarDay(new Date(sunAt)));
    setSunStudyAt(nextSunStep(intervalFractionAtInstant(sunAt, day)) === null ? instantAtIntervalFraction(day, SUN_PLAY_RESTART_STEP / SUN_TIME_STEPS) : sunAt);
    setSunPlaying(true);
  };

  const chooseSceneRecipe = (recipe: SceneRecipe) => {
    const next = sceneRecipePresentation(recipe, sceneEffectsRef.current);
    atmospherePresetRef.current = next.atmosphere;
    lightAzimuthRef.current = next.azimuth;
    setAtmospherePreset(next.atmosphere);
    setLightAzimuth(next.azimuth);
    updateSceneEffects(next.settings);
    announce(`${SCENE_RECIPES[recipe].label} presentation light applied · camera, sources and dates preserved`);
  };

  const changeStudioLight = (next: Omit<ScenePresentation, "settings">) => {
    atmospherePresetRef.current = next.atmosphere;
    lightAzimuthRef.current = next.azimuth;
    setAtmospherePreset(next.atmosphere);
    setLightAzimuth(next.azimuth);
  };

  const changeTerrainDepth = (value: number) => {
    const next = terrainDepth(value);
    verticalExaggerationRef.current = next;
    setVerticalExaggeration(next);
  };

  const exploreGround = () => {
    const map = mapRef.current;
    if (!map || scenePresetRef.current !== "elevation-3d") return;
    runMapMutation("Ground view", () => {
      applyGroundView(map, { reducedMotion, interrupt: () => { stopFlyover(false); stopSceneOrbit(false); } });
      fieldOfViewRef.current = map.getVerticalFieldOfView();
      setFieldOfView(fieldOfViewRef.current);
    });
    announce("Closer ground view · current map center, source heights and selection preserved");
  };

  const composeSceneCamera = (patch: Partial<SceneComposition>, reset = false) => {
    const map = mapRef.current;
    if (!map) return;
    runMapMutation("Scene composition", () => {
      const next = applySceneComposition(map, patch, {
        view: sceneView, reducedMotion, reset,
        interrupt: () => { stopFlyover(false); stopSceneOrbit(false); },
      });
      fieldOfViewRef.current = next.fieldOfView;
      setFieldOfView(next.fieldOfView);
    });
    if (reset) announce("Composition reset · location, zoom and data preserved");
  };

  useEffect(() => {
    const map = mapRef.current;
    if (!map) return;
    runMapMutation("Gesture-mode update", () => {
      if (gestureMode === "cooperative") map.cooperativeGestures.enable();
      else map.cooperativeGestures.disable();
    });
  }, [gestureMode, runMapMutation]);

  useEffect(() => {
    const map = mapRef.current;
    if (!map) return;
    const resize = () => {
      const config = terrainDrawingConfigRef.current;
      // A provider drawer overlays this map. Avoid synthetic movement clearing
      // its tapped surface sample when the canvas dimensions did not change.
      runMapMutation("Map resize", () => { resizeMapAfterLayout(map, config.enabled && (config.surface ?? "off") !== "off"); });
    };
    const first = window.requestAnimationFrame(resize);
    const second = window.setTimeout(resize, 260);
    return () => { window.cancelAnimationFrame(first); window.clearTimeout(second); };
  }, [leftOpen, rightOpen, qwenOpen, runMapMutation, timelineOpen]);

  useEffect(() => {
    if (!playing || reducedMotion || temporalMode === "snapshot" || temporalMode === "comparison") return;
    const timer = window.setInterval(() => {
      const next = nextTemporalFrame(temporalSequence, yearRef.current, playbackDirection, playbackLoopMode);
      if (next === null) {
        setPlaying(false);
        return;
      }
      commitTemporalFrame(next);
    }, 1300 / playbackSpeed);
    return () => window.clearInterval(timer);
  }, [commitTemporalFrame, playbackDirection, playbackLoopMode, playbackSpeed, playing, reducedMotion, temporalMode, temporalSequence]);

  useEffect(() => {
    if (!noaaRadarManifest) return;
    setNoaaRadarClock(Date.now());
    const timer = window.setInterval(() => setNoaaRadarClock(Date.now()), 60_000);
    return () => window.clearInterval(timer);
  }, [noaaRadarManifest]);

  useEffect(() => {
    if (!lightningSelected) {
      setLightningPlaying(false);
      setLightningPreview("idle");
      return;
    }
    let disposed = false;
    const load = async () => {
      setLightningManifestState("loading");
      try {
        const response = await fetch("/api/lightning/frames", { cache: "no-store" });
        if (!response.ok) throw new Error("NOAA frame list unavailable");
        const candidate = await readBoundedJson(response, 64 * 1024) as LightningManifest;
        if (candidate.layer !== "ldn_lightning_strike_density" || candidate.evidenceRole !== "EXTERNAL_CONTEXT_ONLY" || !Array.isArray(candidate.frames) || candidate.frames.length < 1 || candidate.frames.length > 32 || candidate.frames.some((frame) => typeof frame !== "string" || canonicalLightningTime(frame) !== frame)) throw new Error("NOAA frame list invalid");
        if (disposed) return;
        setLightningManifest(candidate);
        if (lightningAutoStartRef.current) {
          lightningAutoStartRef.current = false;
          setLightningFrame(reducedMotion ? candidate.latest : candidate.frames[0]);
          if (!reducedMotion && candidate.frames.length > 1) setLightningPlaying(true);
        } else {
          setLightningFrame((current) => current && candidate.frames.includes(current) ? current : candidate.latest);
        }
        setLightningManifestState("ready");
      } catch {
        if (disposed) return;
        setLightningPlaying(false);
        setLightningManifestState("error");
        setOfficialStates((current) => ({ ...current, "noaa-lightning-density": "error" }));
        setOfficialErrors((current) => ({ ...current, "noaa-lightning-density": "NOAA advertised frames unavailable; no untimed image shown." }));
      }
    };
    void load();
    const timer = window.setInterval(() => { if (!document.hidden) void load(); }, 180_000);
    return () => { disposed = true; window.clearInterval(timer); };
  }, [lightningSelected, lightningReloadToken, reducedMotion]);

  useEffect(() => {
    if (!lightningSelected || !styleReady) return;
    const map = mapRef.current;
    if (!map) return;
    const moved = () => setLightningViewRevision((current) => current + 1);
    map.on("moveend", moved);
    return () => { map.off("moveend", moved); };
  }, [lightningSelected, styleReady]);

  useEffect(() => {
    const map = mapRef.current;
    const id = "noaa-lightning-density";
    // A playing radar loop keeps the *whole* style in a loading state. The
    // lightning source can still be attached and checked independently.
    if (!map || !styleReady) return;
    if (!lightningSelected || !lightningFrame || lightningManifestState !== "ready") {
      const source = OFFICIAL_CONTEXT_BY_ID[id];
      source.layerIds.forEach((layerId) => { if (map.getLayer(layerId)) map.setLayoutProperty(layerId, "visibility", "none"); });
      return;
    }
    let disposed = false;
    const abort = new AbortController();
    let sampledSignal: boolean | null = null;
    setLightningPreview("loading");
    setOfficialStates((current) => ({ ...current, [id]: "loading" }));
    setOfficialErrors((current) => ({ ...current, [id]: undefined }));
    officialRasterFailuresRef.current.delete(id);
    try { setNoaaLightningObservationTime(map, lightningFrame, officialOpacity[id], true); }
    catch { setLightningPlaying(false); setLightningPreview("error"); setOfficialStates((current) => ({ ...current, [id]: "error" })); return; }
    const settle = () => {
      if (disposed || sampledSignal === null || !map.getSource(OFFICIAL_CONTEXT_BY_ID[id].sourceId)) return;
      if (officialRasterFailuresRef.current.has(id)) {
        setLightningPlaying(false);
        setOfficialStates((current) => ({ ...current, [id]: sampledSignal ? "partial" : "error" }));
        return;
      }
      if (!map.isSourceLoaded(OFFICIAL_CONTEXT_BY_ID[id].sourceId)) return;
      setOfficialStates((current) => ({ ...current, [id]: sampledSignal ? "ready" : "empty" }));
    };
    map.on("sourcedata", settle);
    const bounds = map.getBounds();
    const center = map.getCenter();
    const width = Math.min(40, Math.max(0.25, bounds.getEast() - bounds.getWest()));
    const height = Math.min(25, Math.max(0.25, bounds.getNorth() - bounds.getSouth()));
    const bbox = [Math.max(-180, center.lng - width / 2), Math.max(-25, center.lat - height / 2), Math.min(180, center.lng + width / 2), Math.min(80, center.lat + height / 2)].map((value) => value.toFixed(5)).join(",");
    const inspect = async () => {
      try {
        const url = `/api/lightning/preview?time=${encodeURIComponent(lightningFrame)}&bbox=${encodeURIComponent(bbox)}`;
        const response = await fetch(url, { signal: abort.signal, cache: "no-store" });
        if (!response.ok) throw new Error("Preview unavailable");
        const bitmap = await createImageBitmap(await response.blob());
        const canvas = document.createElement("canvas");
        canvas.width = bitmap.width; canvas.height = bitmap.height;
        const context = canvas.getContext("2d", { willReadFrequently: true });
        if (!context) throw new Error("Preview pixels unavailable");
        context.drawImage(bitmap, 0, 0); bitmap.close();
        const pixels = context.getImageData(0, 0, canvas.width, canvas.height).data;
        let visiblePixels = 0;
        for (let index = 3; index < pixels.length; index += 4) if (pixels[index] > 8) visiblePixels++;
        if (disposed) return;
        sampledSignal = visiblePixels > 0;
        setLightningPreview(sampledSignal ? "signal" : "none");
        settle();
      } catch {
        if (disposed) return;
        setLightningPlaying(false);
        setLightningPreview("error");
        setOfficialStates((current) => ({ ...current, [id]: "partial" }));
        setOfficialErrors((current) => ({ ...current, [id]: "NOAA current-view image could not be inspected; signal presence is unconfirmed." }));
      }
    };
    void inspect();
    return () => { disposed = true; abort.abort(); map.off("sourcedata", settle); setNoaaLightningGlow(map, 0); };
  }, [lightningFrame, lightningManifestState, lightningSelected, lightningViewRevision, officialOpacity, styleReady]);

  useEffect(() => {
    if (!lightningSelected || lightningPreview !== "signal" || reducedMotion || !dynamicEffects || !styleReady || document.hidden) return;
    const map = mapRef.current;
    if (!map) return;
    let frame = 0;
    const started = performance.now();
    const animate = (now: number) => {
      const progress = Math.min(1, (now - started) / 1350);
      setNoaaLightningGlow(map, 0.23 * Math.sin(Math.PI * progress) ** 2 * (1 - progress * 0.35));
      if (progress < 1) frame = requestAnimationFrame(animate);
      else setNoaaLightningGlow(map, 0);
    };
    frame = requestAnimationFrame(animate);
    return () => { cancelAnimationFrame(frame); setNoaaLightningGlow(map, 0); };
  }, [lightningFrame, lightningPreview, lightningSelected, reducedMotion, dynamicEffects, styleReady]);

  useEffect(() => {
    if (!lightningPlaying || !lightningSelected || reducedMotion || lightningManifestState !== "ready" || lightningManifest?.frames.length === 1 || !lightningPlaybackReady) return;
    const timer = window.setTimeout(() => {
      const frames = lightningManifest?.frames ?? [];
      if (!frames.length) return;
      setLightningFrame(frames[(Math.max(0, frames.indexOf(lightningFrame ?? "")) + 1) % frames.length]);
    }, 1650);
    return () => window.clearTimeout(timer);
  }, [lightningFrame, lightningManifest, lightningManifestState, lightningPlaying, lightningPlaybackReady, lightningSelected, reducedMotion]);

  useEffect(() => {
    const pause = () => { if (document.hidden) setLightningPlaying(false); };
    document.addEventListener("visibilitychange", pause);
    return () => document.removeEventListener("visibilitychange", pause);
  }, []);

  useEffect(() => {
    if (!noaaRadarSelectedAtPresent) {
      noaaRadarRequestRef.current?.abort();
      noaaRadarRequestRef.current = null;
      setNoaaRadarPlaying(false);
      noaaRadarFrameLoadCleanupRef.current?.();
      noaaRadarFrameLoadCleanupRef.current = null;
      noaaRadarFrameFailureRef.current = null;
      noaaRadarPendingFrameTimeRef.current = null;
      setNoaaRadarPendingFrameTime(null);
      const map = mapRef.current;
      if (map && styleGenerationReadyRef.current) {
        if (noaaRadarFrameTimeRef.current) {
          try { setNoaaRadarObservationTime(map, noaaRadarFrameTimeRef.current); } catch { noaaRadarReadyRef.current = false; }
        }
        runMapMutation("Radar visibility update", () => applyOfficialContextState(
            map,
            runtimeOfficialVisibility(officialVisibilityRef.current, temporalQueryRef.current.frame, false, null),
            officialOpacityRef.current,
            officialPayloadsRef.current,
        ));
      }
      setNoaaRadarFrameLoadState(noaaRadarFrameTimeRef.current ? "ready" : "idle");
      return;
    }
    const refresh = () => {
      if (document.hidden) { noaaRadarRequestRef.current?.abort(); return; }
      void refreshNoaaRadarManifest(true);
    };
    refresh();
    const timer = window.setInterval(refresh, 240_000);
    document.addEventListener("visibilitychange", refresh);
    return () => { window.clearInterval(timer); document.removeEventListener("visibilitychange", refresh); };
  }, [noaaRadarSelectedAtPresent, refreshNoaaRadarManifest, runMapMutation, runtimeOfficialVisibility]);

  useEffect(() => {
    const abort = () => {
      noaaSatelliteRequestRef.current?.abort();
      noaaSatelliteRequestRef.current = null;
    };
    if (!noaaSatelliteSelectedAtPresent) { abort(); return; }
    const refresh = () => {
      if (document.hidden) { abort(); return; }
      void refreshNoaaSatelliteFrames(true);
    };
    refresh();
    const timer = window.setInterval(refresh, 300_000);
    document.addEventListener("visibilitychange", refresh);
    return () => {
      window.clearInterval(timer);
      document.removeEventListener("visibilitychange", refresh);
      abort();
    };
  }, [noaaSatelliteSelectedAtPresent, refreshNoaaSatelliteFrames]);

  useEffect(() => {
    if (buildYearCurrent) return;
    const map = mapRef.current;
    if (map?.isStyleLoaded()) runMapMutation("Hold satellite image for build-year mismatch", () => clearNoaaSatelliteFrame(map));
  }, [buildYearCurrent, runMapMutation]);

  useEffect(() => {
    if (!noaaRadarSelectedAtPresent || noaaRadarPendingFrameTime || noaaRadarFrameLoadState === "error" || noaaRadarLoopFrames.length === 0 || noaaRadarFrameIndex >= 0) return;
    const confirmedOutsideSelectedSpan = Boolean(noaaRadarFrameTime && noaaRadarManifest?.frames.includes(noaaRadarFrameTime));
    if (!noaaRadarFollowLatest && !confirmedOutsideSelectedSpan) return;
    const next = noaaRadarLoopFrames.at(-1)!;
    setNoaaRadarFollowLatest(true);
    applyNoaaRadarFrame(next);
  }, [applyNoaaRadarFrame, noaaRadarFollowLatest, noaaRadarFrameIndex, noaaRadarFrameLoadState, noaaRadarFrameTime, noaaRadarLoopFrames, noaaRadarManifest?.frames, noaaRadarPendingFrameTime, noaaRadarSelectedAtPresent]);


  useEffect(() => {
    if (!noaaRadarPlaying || !noaaRadarRenderable || reducedMotion || noaaRadarFrameLoadState === "loading" || noaaRadarLoopFrames.length < 2) return;
    const currentIndex = Math.max(0, noaaRadarFrameIndex);
    const nextIndex = nextNoaaRadarFrameIndex(noaaRadarLoopFrames.length, currentIndex, "forward", true);
    if (nextIndex === null) {
      setNoaaRadarPlaying(false);
      return;
    }
    const atNewestFrame = currentIndex === noaaRadarLoopFrames.length - 1;
    const delay = (atNewestFrame ? 1_500 : 700) / noaaRadarPlaybackSpeed;
    const timer = window.setTimeout(() => applyNoaaRadarFrame(noaaRadarLoopFrames[nextIndex]), delay);
    return () => window.clearTimeout(timer);
  }, [applyNoaaRadarFrame, noaaRadarFrameIndex, noaaRadarFrameLoadState, noaaRadarLoopFrames, noaaRadarPlaybackSpeed, noaaRadarPlaying, noaaRadarRenderable, reducedMotion]);

  useEffect(() => {
    if (!streamflowSelectedAtPresent) {
      setStreamflowPlaying(false);
      // A hidden or historical layer must not keep retrying current requests.
      streamflowRequestRef.current?.abort();
      streamflowRequestRef.current = null;
      return;
    }
    const refresh = () => {
      // URL/history restoration owns any initial station or archived day.
      if (explorerRestoredRef.current && !document.hidden && !streamflowRequestRef.current && !streamflowArchiveDayRef.current) void refreshStreamflow(streamflowRange, streamflowSelectedStationId, true);
    };
    refresh();
    const timer = window.setInterval(refresh, 300_000);
    document.addEventListener("visibilitychange", refresh);
    window.addEventListener("online", refresh);
    return () => {
      window.clearInterval(timer);
      document.removeEventListener("visibilitychange", refresh);
      window.removeEventListener("online", refresh);
    };
  }, [refreshStreamflow, streamflowRange, streamflowSelectedAtPresent, streamflowSelectedStationId]);

  useEffect(() => {
    const station = streamflowSelectedStationId;
    setStreamflowCoverage(null);
    if (!station) {
      setStreamflowCoverageMessage("Choose a station to check its provider-declared record span.");
      return;
    }
    const controller = new AbortController();
    setStreamflowCoverageMessage("Checking station record span…");
    const timer = window.setTimeout(async () => {
      try {
        const response = await fetch(`/api/hydrology/coverage?station=${encodeURIComponent(station)}`, { signal: controller.signal, headers: { Accept: "application/json" } });
        const candidate = await readBoundedJson(response, 1024 * 1024) as { station?: string; continuous?: { start?: string; end?: string } | null; daily?: { start?: string; end?: string } | null; partial?: boolean; message?: string };
        if (!response.ok || candidate.station !== station) throw new Error(candidate.message ?? "Station coverage unavailable.");
        const validSpan = (span: typeof candidate.continuous) => span && typeof span.start === "string" && typeof span.end === "string" && Number.isFinite(Date.parse(span.start)) && Number.isFinite(Date.parse(span.end)) && span.start <= span.end ? { start: span.start, end: span.end } : null;
        if (controller.signal.aborted) return;
        const continuous = validSpan(candidate.continuous);
        setStreamflowCoverage({ station, continuous, daily: validSpan(candidate.daily), partial: candidate.partial === true });
        if (continuous && candidate.partial !== true) {
          const minDay = continuous.start.slice(0, 10);
          const maxDay = [currentUtcDay(), continuous.end.slice(0, 10)].sort()[0];
          setStreamflowArchiveDraftDay((current) => boundedUtcDay(current, minDay, maxDay) ?? current);
        }
        setStreamflowCoverageMessage(candidate.message ?? "Provider-declared span; gaps may occur within it.");
      } catch (error) {
        if (controller.signal.aborted) return;
        setStreamflowCoverageMessage(error instanceof Error ? error.message : "Station coverage unavailable.");
      }
    }, 350);
    return () => { window.clearTimeout(timer); controller.abort(); };
  }, [streamflowSelectedStationId]);

  useEffect(() => {
    if (!noaaHydrologySelectedAtPresent) return;
    const refresh = () => {
      if (!document.hidden && !noaaHydrologyRequestRef.current) void refreshNoaaHydrologyNetwork(true);
    };
    refresh();
    const timer = window.setInterval(refresh, 300_000);
    return () => window.clearInterval(timer);
  }, [noaaHydrologySelectedAtPresent, refreshNoaaHydrologyNetwork]);

  useEffect(() => {
    if (!streamflowPlaying || !streamflowSelectedAtPresent || reducedMotion || streamflowFrames.length < 2 || safeStreamflowFrameIndex < 0) return;
    const atNewestFrame = safeStreamflowFrameIndex === streamflowFrames.length - 1;
    const nextIndex = atNewestFrame ? 0 : safeStreamflowFrameIndex + 1;
    const delay = (atNewestFrame ? 1_500 : 700) / streamflowPlaybackSpeed;
    const timer = window.setTimeout(() => setStreamflowFrameIndex(nextIndex), delay);
    return () => window.clearTimeout(timer);
  }, [reducedMotion, safeStreamflowFrameIndex, streamflowFrames.length, streamflowPlaybackSpeed, streamflowPlaying, streamflowSelectedAtPresent]);

  useEffect(() => {
    const pauseWhenHidden = () => {
      if (!document.hidden) return;
      setPlaying(false);
      setNoaaRadarPlaying(false);
      setStreamflowPlaying(false);
    };
    document.addEventListener("visibilitychange", pauseWhenHidden);
    return () => document.removeEventListener("visibilitychange", pauseWhenHidden);
  }, []);

  useEffect(() => {
    if (!mapContextOpen) return;
    const panel = composerRef.current;
    if (!panel) return;
    const controls = () => visibleFocusableElements(panel);
    controls()[0]?.focus();
    const onKey = (event: KeyboardEvent) => {
      if (event.key === "Escape") { event.preventDefault(); event.stopPropagation(); setMapContextOpen(false); composerTriggerRef.current?.focus(); }
      if (event.key !== "Tab") return;
      const items = controls();
      if (event.shiftKey && document.activeElement === items[0]) { event.preventDefault(); items.at(-1)?.focus(); }
      else if (!event.shiftKey && document.activeElement === items.at(-1)) { event.preventDefault(); items[0]?.focus(); }
    };
    panel.addEventListener("keydown", onKey);
    return () => panel.removeEventListener("keydown", onKey);
  }, [mapContextOpen]);

  useEffect(() => {
    if (!repositoryOpen) return;
    const controller = new AbortController();
    let expiryTimer: ReturnType<typeof setTimeout> | undefined;
    setRepositoryConnection({ state: "loading" });
    void fetch("/api/repository-status", { cache: "no-store", signal: controller.signal })
      .then(async (response) => {
        if (!response.ok) throw new Error("Repository status was unavailable");
        const observation = parseRepositoryObservation(await readBoundedJson(response, 8 * 1024));
        if (controller.signal.aborted) return;
        setRepositoryConnection(observation);
        if (observation.state === "ready") expiryTimer = setTimeout(() => {
          if (!controller.signal.aborted) setRepositoryConnection({ ...observation, state: "stale" });
        }, Math.max(0, observation.expiresAt! - Date.now()));
      })
      .catch((error) => {
        if (controller.signal.aborted || (error instanceof DOMException && error.name === "AbortError")) return;
        setRepositoryConnection({ state: "error" });
      });
    return () => { controller.abort(); clearTimeout(expiryTimer); };
  }, [repositoryOpen, repositoryRefreshKey]);

  useEffect(() => {
    if (!repositoryOpen) return;
    const panel = repositoryPanelRef.current;
    if (!panel) return;
    const focusable = () => visibleFocusableElements(panel);
    focusable()[0]?.focus();
    const handleKey = (event: KeyboardEvent) => {
      if (event.key === "Escape") {
        event.preventDefault();
        closeRepository();
        return;
      }
      if (event.key !== "Tab") return;
      const items = focusable();
      if (!items.length) return;
      const first = items[0];
      const last = items[items.length - 1];
      if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last.focus(); }
      if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first.focus(); }
    };
    panel.addEventListener("keydown", handleKey);
    return () => panel.removeEventListener("keydown", handleKey);
  }, [repositoryOpen, closeRepository]);

  useEffect(() => {
    if (primaryWorkspace !== "map" || !isCompact || !leftOpen || rightOpen || mapUtilityOpen || qwenOpen) return;
    const panel = leftPanelRef.current;
    if (!panel) return;
    const restoreBackground = isolateModalBackground(panel, panel.closest<HTMLElement>(".site-root"));
    const keepFocusInside = (event: FocusEvent) => {
      if (event.target instanceof Node && !panel.contains(event.target)) visibleFocusableElements(panel)[0]?.focus({ preventScroll: true });
    };
    document.addEventListener("focusin", keepFocusInside, true);
    return () => {
      document.removeEventListener("focusin", keepFocusInside, true);
      restoreBackground();
    };
  }, [primaryWorkspace, isCompact, leftOpen, rightOpen, mapUtilityOpen, qwenOpen]);

  useEffect(() => {
    if (primaryWorkspace !== "map" || !isCompact || (surfaceInspectionOpen && !mapUtilityOpen)) return;
    const openPanel = mapUtilityOpen ? mapUtilityPanelRef.current : rightOpen ? rightPanelRef.current : leftOpen ? leftPanelRef.current : null;
    if (!openPanel) return;
    const focusable = () => visibleFocusableElements(openPanel);
    const items = focusable();
    // A surface tap may open evidence behind Scene. Closing Scene with Escape
    // returns focus to its trigger; let Tab then enter the still-open drawer.
    const returningToScene = !mapUtilityOpen && rightOpen && terrainSurfaceMode !== "off" && document.activeElement instanceof Element && document.activeElement.closest(".scene-panel");
    if (!returningToScene) items[0]?.focus({ preventScroll: true });
    const handleKey = (event: KeyboardEvent) => {
      if (event.key === "Escape") {
        // This panel owns the transition; the same key must not close the
        // conversation that evidence returns to as it bubbles to document.
        event.preventDefault();
        event.stopPropagation();
        if (mapUtilityOpen) closeMapUtility(); else if (rightOpen) closeRightPanel(); else if (leftOpen) closeLeftPanel(); else closeTimelinePanel();
        return;
      }
      if (event.key !== "Tab") return;
      const currentItems = focusable();
      if (!currentItems.length) return;
      const first = currentItems[0];
      const last = currentItems[currentItems.length - 1];
      if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last.focus(); }
      if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first.focus(); }
    };
    openPanel.addEventListener("keydown", handleKey);
    return () => openPanel.removeEventListener("keydown", handleKey);
  }, [primaryWorkspace, isCompact, leftOpen, mapUtilityOpen, mapUtilityView, rightOpen, surfaceInspectionOpen, terrainSurfaceMode, timelineOpen, closeLeftPanel, closeMapUtility, closeRightPanel, closeTimelinePanel]);

  useEffect(() => {
    if (primaryWorkspace !== "map" || !sourceSearchFocusPendingRef.current || !leftOpen || leftPanelMode !== "layers") return;
    leftPanelRef.current?.querySelector<HTMLInputElement>('.catalog-search input[type="search"]')?.focus({ preventScroll: true });
    sourceSearchFocusPendingRef.current = false;
  }, [primaryWorkspace, globalQuery, leftOpen, leftPanelMode, officialSourceQuery]);

  useEffect(() => {
    const handleEscape = (event: KeyboardEvent) => {
      if (event.defaultPrevented || event.key !== "Escape" || repositoryOpen) return;
      // Header popovers own their Escape; keep the underlying Layers view open.
      if ((event.target as HTMLElement | null)?.closest?.(".map-dock-map-menu")) return;
      if (workspaceDetailsRef.current?.open) workspaceDetailsRef.current.open = false;
      else if (sourceStatusOpen) closeSourceStatus();
      else if (qwenOpen) closeQwenCompanion();
      else if (mapContextOpen) setMapContextOpen(false);
      else if (helpOpen) closeMapGuide();
      else if (mapUtilityOpen) closeMapUtility();
      else if (measureModeRef.current) {
        measureModeRef.current = null;
        measurementGeometryModeRef.current = null;
        measureCoordinatesRef.current = [];
        setMeasureCoordinateCount(0);
        setMeasureMode(null);
        setMeasurementGeometryMode(null);
        setMeasurement("Measurement cancelled");
        mapRef.current?.doubleClickZoom.enable();
        if (mapRef.current?.isStyleLoaded()) updateMeasurementSource(mapRef.current, buildMeasurementData([], null));
      }
      else if (liveDockVisible && !glmFlashesEnabled) closeLiveInstrument();
      else if (!isCompact && rightOpen) closeRightPanel();
    };
    document.addEventListener("keydown", handleEscape);
    return () => document.removeEventListener("keydown", handleEscape);
  }, [sourceStatusOpen, helpOpen, isCompact, mapContextOpen, mapUtilityOpen, qwenOpen, repositoryOpen, rightOpen, liveDockVisible, glmFlashesEnabled, closeLiveInstrument, closeMapUtility, closeQwenCompanion, closeRightPanel, closeSourceStatus, closeMapGuide]);

  const chooseSearchResult = (item: GlobalSearchItem) => {
    setPrimaryWorkspace("map");
    if (primaryWorkspace !== "map" && item.kind !== "source" && item.kind !== "county") window.setTimeout(() => mapContainerRef.current?.focus(), 0);
    setGlobalQuery("");
    if (item.kind === "county") {
      // Resolve again from the current successful payload; a stale search row
      // cannot reopen a failed/removed baseline or silently change map time.
      const payload = officialPayloads["census-counties"];
      const current = countySearchResults(payload, officialStates["census-counties"], item.title).find(row => row.id === item.id);
      const feature = current && payload?.data.features.find(row => row.properties?.featureId === current.featureId);
      const geometry = feature && countySearchGeometry(feature);
      if (!feature || !geometry) { announce("The county source is no longer available. Reopen Map layers to retry it."); return; }
      const source = OFFICIAL_CONTEXT_SOURCES.find(row => row.id === "census-counties");
      const context = buildBasemapContext({ ...feature, source: source?.sourceId }, ...geometry.focus);
      if (!context) return;
      setOfficialContextVisible("census-counties", true);
      assistantEvidenceReturnRef.current = globalSearchInputRef.current;
      openSelection(context, globalSearchInputRef.current);
      mapRef.current?.fitBounds(geometry.bounds, { padding: 70, maxZoom: 9, duration: motionDuration(650) });
      announce(`Opened ${current!.title} from the Census reference baseline. Map time is unchanged; source context is not KFM evidence.`);
      return;
    }
    if (item.kind === "source") {
      sourceSearchFocusPendingRef.current = true;
      openAtlasPanel("layers");
      setStarterPanelOpen(false);
      setLayerCatalogView("official");
      setOfficialWorkspace("all");
      setOfficialCatalogFilter("all");
      setOfficialSourceQuery(item.title);
      setOfficialContextVisible(item.officialContextId, true);
      announce(`Opened ${item.title} in Map layers`);
      return;
    }
    if (item.kind === "feature" && item.featureId) {
      selectStoredFeature(item.layerId, item.featureId);
      return;
    }
    const layer = LAYER_REGISTRY.find((candidate) => candidate.id === item.layerId);
    if (!layer) return;
    setVisibility((current) => ({ ...current, [layer.id]: true }));
    mapRef.current?.fitBounds([[layer.bounds[0], layer.bounds[1]], [layer.bounds[2], layer.bounds[3]]], { padding: 70, maxZoom: 9, duration: window.matchMedia("(prefers-reduced-motion: reduce)").matches ? 0 : 650 });
  };

  const activatePublicWorkspace = (workspaceId: PublicWorkspaceId) => {
    setCurrentWorkspace(workspaceId);
    if (workspaceDetailsRef.current) workspaceDetailsRef.current.open = false;
    setHelpOpen(false);
    setGlobalQuery("");

    if (workspaceId === "features") {
      setRepositoryView("readiness");
      setRepositoryOpen(true);
      announce("Opened the read-only repository feature and readiness workspace");
      return;
    }

    if (workspaceId === "trust" && !selected) {
      setRepositoryView("transitions");
      setRepositoryOpen(true);
      announce("Opened the trust workspace; select a map feature for its evidence record");
      return;
    }

    setRepositoryOpen(false);
    if (workspaceId === "knowledge") {
      dismissMapUtilityWithoutFocus();
      setRightOpen(false);
      setTimelineOpen(false);
      setLeftPanelMode("layers");
      setLeftOpen(true);
      window.setTimeout(() => leftPanelRef.current?.querySelector<HTMLElement>("input:not([disabled]), select:not([disabled]), button:not([disabled])")?.focus(), 0);
      announce("Opened the public-safe knowledge and layer workspace");
      return;
    }

    if (workspaceId === "trust") {
      dismissMapUtilityWithoutFocus();
      setLeftOpen(false);
      setTimelineOpen(false);
      setRightOpen(true);
      activateDrawerView("evidence", true);
      announce("Opened the selected feature's evidence workspace");
      return;
    }

    dismissMapUtilityWithoutFocus();
    if (isCompact) {
      setLeftOpen(false);
      setRightOpen(false);
      setTimelineOpen(false);
    }
    window.setTimeout(() => mapContainerRef.current?.focus(), 0);
    announce("Returned to the map workspace");
  };

  const zoomToLayer = (layer: LayerRecord) => {
    locationDerivedViewRef.current = false;
    setLocationCameraRedacted(false);
    setVisibility((current) => ({ ...current, [layer.id]: true }));
    mapRef.current?.fitBounds([[layer.bounds[0], layer.bounds[1]], [layer.bounds[2], layer.bounds[3]]], { padding: 70, maxZoom: 9, duration: window.matchMedia("(prefers-reduced-motion: reduce)").matches ? 0 : 650 });
  };

  const fitKansasView = () => {
    if (locationDerivedViewRef.current) {
      locationDerivedViewRef.current = false;
      setLocationCameraRedacted(false);
      mapRef.current?.jumpTo(KANSAS_VIEW);
      announce("Private location camera cleared and reset to the generalized Kansas extent");
      return;
    }
    mapRef.current?.fitBounds([[-102.1, 36.95], [-94.55, 40.05]], { padding: 48, duration: motionDuration(600) });
    announce("Fit the Kansas overview");
  };

  const captureAnalysisArea = () => {
    const map = mapRef.current;
    if (!map) {
      announce("The map is not ready to capture an analysis area");
      return;
    }
    if (locationDerivedViewRef.current) {
      announce("Clear the private location camera before capturing a shareable analysis area");
      return;
    }
    const bounds = map.getBounds();
    const nextArea: MapBoundsState = {
      west: clamp(bounds.getWest(), SUPPORTED_CONTEXT_BOUNDS.west, SUPPORTED_CONTEXT_BOUNDS.east),
      south: clamp(bounds.getSouth(), SUPPORTED_CONTEXT_BOUNDS.south, SUPPORTED_CONTEXT_BOUNDS.north),
      east: clamp(bounds.getEast(), SUPPORTED_CONTEXT_BOUNDS.west, SUPPORTED_CONTEXT_BOUNDS.east),
      north: clamp(bounds.getNorth(), SUPPORTED_CONTEXT_BOUNDS.south, SUPPORTED_CONTEXT_BOUNDS.north),
    };
    analysisAreaRef.current = nextArea;
    setAnalysisArea(nextArea);
    if (map.isStyleLoaded()) updateAnalysisAreaSource(map, nextArea);
    setReportScope("ANALYSIS_AREA");
    setReportGeneratedAt(new Date().toISOString());
    announce("Locked the current MapLibre viewport as the report area of interest");
  };

  const clearAnalysisArea = () => {
    analysisAreaRef.current = null;
    setAnalysisArea(null);
    if (mapRef.current?.isStyleLoaded()) updateAnalysisAreaSource(mapRef.current, null);
    if (reportScope === "ANALYSIS_AREA") setReportScope("VIEWPORT");
    announce("Cleared the locked analysis area");
  };

  const fitAnalysisArea = () => {
    if (!analysisArea) {
      announce("No analysis area is locked");
      return;
    }
    locationDerivedViewRef.current = false;
    setLocationCameraRedacted(false);
    mapRef.current?.fitBounds([[analysisArea.west, analysisArea.south], [analysisArea.east, analysisArea.north]], { padding: 64, maxZoom: 11, duration: motionDuration(600) });
    announce("Fit the locked analysis area");
  };

  const fitImportPreview = (preview = importPreview) => {
    if (!preview?.bounds || !preview.renderAllowed) {
      announce("The inspected file has no previewable geometry inside the supported Kansas context");
      return;
    }
    const [west, south, east, north] = preview.bounds;
    locationDerivedViewRef.current = true;
    setLocationCameraRedacted(true);
    mapRef.current?.fitBounds([
      [clamp(west, SUPPORTED_CONTEXT_BOUNDS.west, SUPPORTED_CONTEXT_BOUNDS.east), clamp(south, SUPPORTED_CONTEXT_BOUNDS.south, SUPPORTED_CONTEXT_BOUNDS.north)],
      [clamp(east, SUPPORTED_CONTEXT_BOUNDS.west, SUPPORTED_CONTEXT_BOUNDS.east), clamp(north, SUPPORTED_CONTEXT_BOUNDS.south, SUPPORTED_CONTEXT_BOUNDS.north)],
    ], { padding: 64, maxZoom: 12, duration: motionDuration(600) });
    announce("Fit the browser-local import preview; the derived camera remains private and redacted");
  };

  const inspectImportFile = async (file?: File | null) => {
    if (!file) return;
    const inspectionGeneration = ++importInspectionGenerationRef.current;
    setImportBusy(true);
    setImportError("");
    importPreviewRef.current = null;
    importPreviewVisibleRef.current = false;
    setImportPreview(null);
    setImportPreviewVisible(false);
    if (mapRef.current?.isStyleLoaded()) updateImportPreviewSource(mapRef.current, null);
    try {
      if (file.size > IMPORT_PREVIEW_MAX_BYTES) throw new Error("The preview is limited to files no larger than 2 MB.");
      const text = await file.text();
      if (inspectionGeneration !== importInspectionGenerationRef.current) return;
      const preview = buildLocalImportPreview({
        fileName: file.name,
        fileSizeBytes: file.size,
        text,
        inspectedAt: new Date().toISOString(),
        supportedBounds: SUPPORTED_CONTEXT_BOUNDS,
      });
      if (inspectionGeneration !== importInspectionGenerationRef.current) return;
      importPreviewRef.current = preview;
      setImportPreview(preview);
      const nextVisible = preview.renderAllowed;
      importPreviewVisibleRef.current = nextVisible;
      setImportPreviewVisible(nextVisible);
      if (mapRef.current?.isStyleLoaded()) updateImportPreviewSource(mapRef.current, nextVisible ? preview.featureCollection : null);
      if (nextVisible) fitImportPreview(preview);
      announce(nextVisible
        ? `Previewing ${preview.featureCount} browser-local ${preview.sourceFormat} feature${preview.featureCount === 1 ? "" : "s"}; exact bounds remain redacted from outward artifacts`
        : "File inspected, but map preview is blocked outside the supported Kansas context");
    } catch (error) {
      if (inspectionGeneration !== importInspectionGenerationRef.current) return;
      const message = error instanceof Error ? error.message : "The selected file could not be inspected.";
      setImportError(message);
      announce(message);
    } finally {
      if (inspectionGeneration === importInspectionGenerationRef.current) {
        setImportBusy(false);
        if (importInputRef.current) importInputRef.current.value = "";
      }
    }
  };

  const inspectRoadStudyFile = async (file?: File | null) => {
    if (!file) return;
    const generation = ++roadStudyImportGenerationRef.current;
    const editionId = roadStudyEditionId;
    setRoadStudyBusy(true);
    setRoadStudyError("");
    try {
      if (roadStudyLayers.length >= ROAD_STUDY_MAX_LAYERS && !roadStudyLayers.some((layer) => layer.editionId === editionId)) throw new Error(`Compare at most ${ROAD_STUDY_MAX_LAYERS} editions at once. Remove one to add another.`);
      if (file.size > IMPORT_PREVIEW_MAX_BYTES) throw new Error("Choose a road-line GeoJSON file no larger than 2 MB.");
      const text = await file.text();
      if (generation !== roadStudyImportGenerationRef.current) return;
      const existing = roadStudyLayers.find((layer) => layer.editionId === editionId);
      const next = inspectRoadStudyGeoJson({
        editionId,
        fileName: file.name,
        fileSizeBytes: file.size,
        text,
        color: existing?.color ?? ROAD_STUDY_COLORS[roadStudyLayers.length % ROAD_STUDY_COLORS.length],
        supportedBounds: SUPPORTED_CONTEXT_BOUNDS,
      });
      setRoadStudyLayers((current) => [...current.filter((layer) => layer.editionId !== editionId), existing ? { ...next, color: existing.color, opacity: existing.opacity } : next]);
      announce(`${next.editionLabel}: ${next.featureCount} candidate line${next.featureCount === 1 ? "" : "s"} added to the private visual comparison`);
    } catch (error) {
      if (generation !== roadStudyImportGenerationRef.current) return;
      setRoadStudyError(error instanceof Error ? error.message : "The road study file could not be opened.");
    } finally {
      if (generation === roadStudyImportGenerationRef.current) {
        setRoadStudyBusy(false);
        if (roadStudyInputRef.current) roadStudyInputRef.current.value = "";
      }
    }
  };

  const toggleImportPreview = () => {
    if (!importPreview?.renderAllowed) {
      announce("The inspected file has no previewable geometry inside the supported Kansas context");
      return;
    }
    const nextVisible = !importPreviewVisible;
    importPreviewVisibleRef.current = nextVisible;
    setImportPreviewVisible(nextVisible);
    if (mapRef.current?.isStyleLoaded()) updateImportPreviewSource(mapRef.current, nextVisible ? importPreview.featureCollection : null);
    announce(nextVisible ? "Displayed the browser-local import preview" : "Hid the browser-local import preview");
  };

  const clearImportPreview = () => {
    importInspectionGenerationRef.current += 1;
    importPreviewRef.current = null;
    importPreviewVisibleRef.current = false;
    setImportPreview(null);
    setImportPreviewVisible(false);
    setImportError("");
    setImportBusy(false);
    if (importInputRef.current) importInputRef.current.value = "";
    if (mapRef.current?.isStyleLoaded()) updateImportPreviewSource(mapRef.current, null);
    announce("Cleared the browser-local import preview");
  };

  const copyImportPreviewAudit = async () => {
    if (!importPreview) return;
    try {
      await navigator.clipboard.writeText(JSON.stringify(importPreviewAudit(importPreview), null, 2));
      announce("Copied the redacted no-effect import inspection record");
    } catch {
      announce("Clipboard access was blocked; no import inspection record left the browser");
    }
  };

  const travelCameraHistory = (direction: -1 | 1) => {
    const nextIndex = cameraHistoryIndexRef.current + direction;
    const nextView = cameraHistoryRef.current[nextIndex];
    if (!nextView) {
      announce(direction < 0 ? "No earlier camera view" : "No later camera view");
      return;
    }
    cameraHistoryIndexRef.current = nextIndex;
    setCameraHistoryIndex(nextIndex);
    replayingCameraHistoryRef.current = true;
    locationDerivedViewRef.current = false;
    setLocationCameraRedacted(false);
    mapRef.current?.easeTo({ ...nextView, center: [...nextView.center] as [number, number], duration: motionDuration(450) });
    announce(direction < 0 ? "Returned to the previous map view" : "Advanced to the next map view");
  };

  const inspectLayer = (layer: LayerRecord, returnElement: HTMLElement) => {
    const featureId = [...layer.data.features]
      .filter((feature) => isFeatureAvailableForTemporalQuery(layer, feature.properties.year, temporalQuery))
      .sort((left, right) => right.properties.year - left.properties.year)[0]?.properties.fid ?? null;
    if (!featureId) {
      announce(`${layer.title} has no feature compatible with ${temporalScopeLabel}`);
      return;
    }
    setMapFeatureQuery("");
    setMapFeatureLayer(layer.id);
    openMapUtility("inspect", returnElement);
  };

  const moveLayer = (layerId: string, direction: -1 | 1) => {
    setLayerOrder((current) => {
      const next = [...current];
      const index = next.indexOf(layerId);
      const target = index + direction;
      if (index < 0 || target < 0 || target >= next.length) return current;
      [next[index], next[target]] = [next[target], next[index]];
      if (mapRef.current?.isStyleLoaded()) reorderRegistryLayers(mapRef.current, next);
      return next;
    });
  };

  const selectIndexedFeature = (layerId: string, featureId: string) => {
    mapUtilityReturnRef.current = null;
    setMapUtilityOpen(false);
    setMapQueryCandidates([]);
    selectStoredFeature(layerId, featureId, mapContainerRef.current);
  };

  const centerIndexedFeature = (layerId: string, featureId: string) => {
    const match = findFeature(featureId);
    if (!match || match.layer.id !== layerId) return;
    locationDerivedViewRef.current = false;
    setLocationCameraRedacted(false);
    mapRef.current?.easeTo({ center: [match.feature.properties.focusLng, match.feature.properties.focusLat], zoom: Math.max(mapRef.current.getZoom(), 8), duration: motionDuration(550) });
    announce(`Centered ${match.feature.properties.title} · camera only`);
  };

  const goToCoordinates = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const latitude = Number(coordinateLatitude);
    const longitude = Number(coordinateLongitude);
    if (!Number.isFinite(latitude) || !Number.isFinite(longitude)) {
      setCoordinateError("Enter numeric latitude and longitude values.");
      return;
    }
    if (latitude < SUPPORTED_CONTEXT_BOUNDS.south || latitude > SUPPORTED_CONTEXT_BOUNDS.north || longitude < SUPPORTED_CONTEXT_BOUNDS.west || longitude > SUPPORTED_CONTEXT_BOUNDS.east) {
      setCoordinateError("Coordinates must be inside the Explorer's supported Kansas context extent.");
      return;
    }
    setCoordinateError("");
    setCoordinateLatitude(latitude.toFixed(5));
    setCoordinateLongitude(longitude.toFixed(5));
    locationDerivedViewRef.current = false;
    setLocationCameraRedacted(false);
    mapRef.current?.easeTo({ center: [longitude, latitude], zoom: Math.max(mapRef.current.getZoom(), 9), duration: motionDuration(600) });
    announce(`Centered ${latitude.toFixed(4)}°, ${longitude.toFixed(4)}° · camera only`);
  };

  const copyMapCenter = async () => {
    if (locationDerivedViewRef.current) {
      announce("The browser-location-derived center remains private and was not copied");
      return;
    }
    const coordinateText = `${view.center[1].toFixed(5)}, ${view.center[0].toFixed(5)}`;
    try {
      await navigator.clipboard.writeText(coordinateText);
      announce("Map center coordinates copied");
    } catch {
      announce("Map center coordinates could not be copied");
    }
  };

  const fitIndexedFeatures = () => {
    if (!mapFeatureIndex.length) {
      announce("No compatible indexed features to fit");
      return;
    }
    locationDerivedViewRef.current = false;
    setLocationCameraRedacted(false);
    const points = mapFeatureIndex.map(({ feature }) => [feature.properties.focusLng, feature.properties.focusLat] as [number, number]);
    if (points.length === 1) {
      mapRef.current?.easeTo({ center: points[0], zoom: Math.max(mapRef.current.getZoom(), 9), duration: motionDuration(550) });
    } else {
      const longitudes = points.map(([longitude]) => longitude);
      const latitudes = points.map(([, latitude]) => latitude);
      mapRef.current?.fitBounds([[Math.min(...longitudes), Math.min(...latitudes)], [Math.max(...longitudes), Math.max(...latitudes)]], { padding: 64, maxZoom: 10, duration: motionDuration(650) });
    }
    announce(`Fit ${mapFeatureIndex.length} compatible indexed feature${mapFeatureIndex.length === 1 ? "" : "s"}`);
  };

  const orientSceneCamera = (pitch: number, bearing = view.bearing) => {
    stopFlyover(false);
    stopSceneOrbit(false);
    mapRef.current?.easeTo({ pitch, bearing, duration: motionDuration(450) });
  };

  const toggleStructureExtrusions = () => {
    const next = !structures3DEnabled;
    structures3DRef.current = next;
    setStructures3DEnabled(next);
    if (next && basemapRef.current !== "standard") {
      basemapRef.current = "standard";
      setBasemap("standard");
      setStructures3DState("UNAVAILABLE");
    } else if (mapRef.current?.isStyleLoaded()) {
      setStructures3DState(setStructureExtrusions(mapRef.current, next));
    }
    announce(next ? "Height-backed Liberty structures enabled above zoom 13" : "3D structures hidden");
  };

  const focusStructureScene = (preset: (typeof STRUCTURE_FOCUS_PRESETS)[number]) => {
    stopSceneOrbit(false);
    structures3DRef.current = true;
    basemapRef.current = "standard";
    projectionRef.current = "mercator";
    scenePresetRef.current = "overview-2d";
    atmospherePresetRef.current = "dusk";
    fieldOfViewRef.current = 44;
    setStructures3DEnabled(true);
    setBasemap("standard");
    setProjection("mercator");
    setScenePreset("overview-2d");
    setAtmospherePreset("dusk");
    setFieldOfView(44);
    mapRef.current?.easeTo({ center: preset.center, zoom: 15.2, pitch: 60, bearing: preset.bearing, duration: motionDuration(700) });
    announce(`${preset.label} structure view applied · source height attributes only`);
  };

  const activateMapRepresentation = (mode: "2d" | "terrain" | "globe" | "compare") => {
    setPrimaryWorkspace("map");
    if (mode === "compare") {
      openMapUtility("compare");
      announce("Compare opened · choose two layers and dates without changing the active map time");
      return;
    }

    stopSceneOrbit(false);
    stopFlyover(false);
    const map = mapRef.current;
    // A second representation choice must cancel the first camera transition.
    // Otherwise MapLibre can finish an older ease after React has already
    // selected the newer mode, leaving the controls and canvas disagreeing.
    map?.stop();
    const currentBearing = map?.getBearing() ?? view.bearing;
    const currentPitch = map?.getPitch() ?? view.pitch;
    const wasGlobe = projectionRef.current === "globe";
    if (mode === "globe" && !wasGlobe) {
      const center = map?.getCenter();
      regionalViewRef.current = center ? { center: [center.lng, center.lat], zoom: map!.getZoom(), bearing: currentBearing, pitch: currentPitch } : view;
    }
    const nextProjection = mode === "globe" ? "globe" : "mercator";
    const nextScenePreset: ScenePresetId = mode === "terrain" ? "elevation-3d" : mode === "globe" ? "globe-overview" : "overview-2d";
    const nextAtmosphere: AtmospherePreset = mode === "terrain" || mode === "globe" ? "clear" : "night";
    const nextFieldOfView = compositionDefaults(mode === "terrain" ? "terrain" : mode === "globe" ? "globe" : "2d").fieldOfView;
    const nextPitch = mode === "terrain" ? Math.max(compositionDefaults("terrain").pitch, currentPitch) : 0;
    const nextBearing = mode === "2d" ? 0 : currentBearing;

    projectionRef.current = nextProjection;
    scenePresetRef.current = nextScenePreset;
    // Display emphasis is explicit; hover elevations and profile samples undo
    // this renderer scale before reporting DEM heights.
    verticalExaggerationRef.current = mode === "terrain" ? DEFAULT_TERRAIN_DEPTH : 1;
    atmospherePresetRef.current = nextAtmosphere;
    lightAzimuthRef.current = mode === "terrain" ? 235 : mode === "globe" ? 225 : 210;
    fieldOfViewRef.current = nextFieldOfView;
    if (map) { applyProjectionNavigationLimits(map, nextProjection); if (mode === "terrain") map.setMaxPitch(72); }

    // Commit renderer state as one transaction before scheduling React's
    // presentation updates. This makes repeated 2D ↔ terrain ↔ globe changes
    // idempotent and prevents a stale effect or style event from winning.
    if (map?.isStyleLoaded()) {
      if (mode !== "terrain") {
        setTerrainState(setTerrainPresentation(map, false, 1));
        setTerrainHeightOverlay(map, false);
      }
      map.setProjection({ type: nextProjection });
      applyOfficialContextState(map, effectiveOfficialVisibility, officialOpacityRef.current, officialPayloadsRef.current);
      if (mode === "terrain") {
        setTerrainState(setTerrainPresentation(map, true, verticalExaggerationRef.current));
        setTerrainHeightOverlay(map, topographicOverlayRef.current);
      }
      applySceneEnvironment(map, nextAtmosphere, lightAzimuthRef.current);
      map.setVerticalFieldOfView(nextFieldOfView);
      map.triggerRepaint();
    }

    setProjection(nextProjection);
    setScenePreset(nextScenePreset);
    setVerticalExaggeration(verticalExaggerationRef.current);
    setAtmospherePreset(nextAtmosphere);
    setLightAzimuth(lightAzimuthRef.current);
    setFieldOfView(nextFieldOfView);
    if (mode === "globe" && !VECTOR_BASEMAPS.has(basemapRef.current)) {
      // The alternate basemaps are regional raster carriers. The vector
      // basemaps remain visually stable as the globe zooms out.
      basemapRef.current = "standard";
      setBasemap("standard");
    }
    if (mode === "terrain") {
      setVisibility((current) => {
        const next = { ...current, "elevation-concept": false };
        visibilityRef.current = next;
        return next;
      });
    }
    const cameraTarget = mode === "globe" && !wasGlobe ? GLOBE_VIEWPOINTS.earth
      : mode !== "globe" && wasGlobe ? { ...regionalViewRef.current, pitch: nextPitch, bearing: nextBearing }
        : { pitch: nextPitch, bearing: nextBearing };
    if (!map && "center" in cameraTarget) pendingViewRef.current = cameraTarget;
    map?.easeTo({ ...cameraTarget, duration: motionDuration(420), essential: false });
    if (mode === "globe") { setLeftOpen(false); setRightOpen(false); setSourceStatusOpen(false); setMapUtilityOpen(false); }
    announce(`${mode === "terrain" ? "Terrain 3D display" : mode === "globe" ? "Globe display" : "2D evidence display"} applied · active time and selection preserved`);
  };

  const startTerrainInvestigation = () => {
    activateMapRepresentation("terrain");
    openMapUtility("scene");
    toggleMeasure("distance");
    announce(`Terrain investigation ready at ${verticalExaggerationRef.current.toFixed(1)}× display scale. Draw a line on the map, finish it, then preview unexaggerated DEM samples.`);
  };

  // The dock shows the calculated day and night at the current time when the
  // layer's date range holds it; another chosen day keeps its own clock.
  // Photo-real 3D: the 2024 one-foot aerial on the USGS 3DEP bare-earth DEM at
  // true vertical scale, under the real sun; a landscape id flies there, null
  // returns to the look's own map and the Mapzen relief at the default depth.
  const showPhotoreal = (landscapeId: string | null) => {
    const look = categoryMapOnScreen;
    if (!look) return;
    if (landscapeId === null) {
      basemapRef.current = look.basemap; setBasemap(look.basemap);
      if (photorealHidHillshadeRef.current) { photorealHidHillshadeRef.current = false; setOfficialContextVisible("usgs-3dep-hillshade", true); }
      if (terrainProviderRef.current !== "mapzen") chooseTerrainProvider("mapzen");
      changeTerrainDepth(DEFAULT_TERRAIN_DEPTH);
      announce(`${look.name} relief colours restored`);
      return;
    }
    const landscape = PHOTOREAL_LANDSCAPES.find(candidate => candidate.id === landscapeId);
    if (!landscape) return;
    if (categoryMode !== "terrain") activateMapRepresentation("terrain");
    if (basemapRef.current !== "photoreal") {
      basemapRef.current = "photoreal"; setBasemap("photoreal"); changeTerrainDepth(1);
      // The photograph carries the real light of its flight; painted relief stays off it.
      photorealHidHillshadeRef.current = Boolean(officialVisibilityRef.current["usgs-3dep-hillshade"]);
      if (photorealHidHillshadeRef.current) setOfficialContextVisible("usgs-3dep-hillshade", false);
    }
    if (terrainProviderRef.current !== "usgs-3dep") chooseTerrainProvider("usgs-3dep");
    if (!sceneEffectsRef.current.sunSync) updateSceneEffects({ ...sceneEffectsRef.current, sunSync: true });
    setPhotorealPlace(landscape.id);
    const { center, zoom, pitch, bearing } = landscape.camera;
    mapRef.current?.flyTo({ center: [center[0], center[1]], zoom, pitch, bearing, duration: motionDuration(2600), essential: false });
    announce(`${landscape.name} · photo-real 3D · USGS 3DEP at ${verticalExaggerationRef.current === 1 ? "true vertical scale" : `vertical ×${verticalExaggerationRef.current.toFixed(1)}`}`);
  };
  // NASA SMAP L4 cells are 9 km across: a field-scale view would show one cell as
  // a flat wash, so switching the soil tool on pulls out to the region they describe.
  const SOIL_REGIONAL_ZOOM = 7.2;
  const showCategorySoil = (on: boolean) => {
    changeSoilMapState({ visible: on });
    const map = mapRef.current;
    if (on && map && map.getZoom() > SOIL_REGIONAL_ZOOM + 0.5) map.easeTo({ zoom: SOIL_REGIONAL_ZOOM, duration: motionDuration(1200), essential: false });
    announce(on ? "NASA SMAP soil moisture shown · 9 km modelled cells over the region" : "Soil moisture hidden");
  };
  // The aquifer map shows one KGS view at a time; the dock switches between them.
  const AQUIFER_VIEW_IDS: readonly AquiferView[] = ["kgs-saturated-thickness", "kgs-depth-to-water", "kgs-aquifer-high-plains"];
  const aquiferView = AQUIFER_VIEW_IDS.find(id => officialVisibility[id]) ?? null;
  const showAquiferView = (view: AquiferView) => {
    for (const id of AQUIFER_VIEW_IDS) if (id === view || officialVisibilityRef.current[id]) setOfficialContextVisible(id, id === view);
  };
  const soilReading = !soilMapState.visible ? ""
    : soilMoistureContext?.renderedFrameTimeUtc ? `${SOIL_VIEWS[soilMapState.view].label} · ${soilMoistureContext.renderedFrameTimeUtc.slice(0, 16).replace("T", " ")} UTC · NASA SMAP L4, 9 km modelled cells`
    : soilMoistureContext?.availabilityState === "error" || soilMoistureContext?.mapState === "error" ? "NASA soil moisture is unavailable right now; nothing is drawn in its place"
    : "Finding NASA's latest soil moisture day…";
  const showCategoryDaylight = (on: boolean) => {
    toggleDaylightVisibility(on);
    if (!on) return;
    const interval = kansasLocalDateRangeInterval(daylightDayRef.current, daylightThroughDayRef.current);
    const now = Date.now();
    if (now >= interval.startMs && now < interval.endMs) seekDaylight(intervalFractionAtInstant(now, interval));
  };

  // From the category dock the investigation's steps sit in the Scene panel's collapsed
  // "Terrain tools" section, so open it and bring them into view.
  const startCategoryTransect = () => {
    startTerrainInvestigation();
    window.requestAnimationFrame(() => {
      const steps = document.querySelector<HTMLElement>(".map-utility-panel .terrain-investigation");
      steps?.closest("details")?.setAttribute("open", "");
      steps?.scrollIntoView({ behavior: reducedMotion ? "auto" : "smooth", block: "start" });
    });
  };

  const toggleTopographicHeightOverlay = () => {
    const next = !topographicOverlayRef.current;
    const map = mapRef.current;
    if (next && (!map?.isStyleLoaded() || terrainState === "ERROR")) {
      announce("Height overlay is waiting for the terrain DEM");
      return;
    }
    topographicOverlayRef.current = next;
    setTopographicOverlay(next);
    if (map) setTerrainHeightOverlay(map, next && scenePresetRef.current === "elevation-3d");
    if (!next) {
      setLockedTerrainElevation(null);
    }
    announce(next ? "Topographic height colors enabled · cursor DEM reading remains available" : "Topographic height colors disabled · cursor DEM reading remains available");
  };

  const previewTerrainProfile = () => {
    const map = mapRef.current;
    const line = measureCoordinatesRef.current;
    if (!map || terrainState !== "READY" || measurementGeometryModeRef.current !== "distance" || line.length < 2) {
      announce("Finish a two-point or longer line while Terrain 3D is ready before previewing a profile");
      return;
    }

    const samples: TerrainProfileSample[] = [];
    let cumulativeMiles = 0;
    for (let segmentIndex = 1; segmentIndex < line.length; segmentIndex += 1) {
      const start = line[segmentIndex - 1];
      const end = line[segmentIndex];
      const segmentMiles = distanceMiles([start, end]);
      const steps = 8;
      for (let step = segmentIndex === 1 ? 0 : 1; step <= steps; step += 1) {
        const fraction = step / steps;
        const coordinate: [number, number] = [
          start[0] + (end[0] - start[0]) * fraction,
          start[1] + (end[1] - start[1]) * fraction,
        ];
        const elevation = unexaggeratedTerrainElevation(map, coordinate);
        if (elevation !== null && Number.isFinite(elevation)) {
          samples.push({ distanceMiles: cumulativeMiles + segmentMiles * fraction, elevationMeters: elevation });
        }
      }
      cumulativeMiles += segmentMiles;
    }
    setTerrainProfile(samples);
    announce(samples.length ? "Display terrain profile previewed from unexaggerated renderer samples" : "No display elevation samples were available for this line");
  };

  const retryTerrain = () => {
    const map = mapRef.current;
    if (!map?.isStyleLoaded()) {
      setTerrainState("LOADING");
      setRuntime({ kind: "loading", message: "Waiting for the map style before retrying terrain…" });
      return;
    }
    // Retry uses the same complete teardown as a 3D → 2D transition so a
    // failed tile manager cannot be reused by the new terrain presentation.
    setTerrainPresentation(map, false, 1);
    setTerrainElevationReading(null);
    setTerrainElevationUnavailable(null);
    setTerrainState(setTerrainPresentation(map, true, verticalExaggerationRef.current));
    setTerrainHeightOverlay(map, topographicOverlayRef.current);
    setRuntime({ kind: "loading", message: `Retrying ${terrainProviderRef.current === "usgs-3dep" ? "USGS 3DEP" : "Mapzen"} elevation tiles…` });
    announce("Terrain source retry started; the 2D evidence path remains available");
  };

  const chooseTerrainProvider = (provider: TerrainProvider) => {
    terrainProviderRef.current = provider;
    attachedTerrainProviderRef.current = null;
    setTerrainElevationReading(null);
    setTerrainElevationUnavailable(null);
    setTerrainProvider(provider);
    setTerrainState("LOADING");
    announce(`Loading ${provider === "usgs-3dep" ? "USGS 3DEP" : "Mapzen"} display DEM`);
  };

  const chooseTerrainProviderByHand = (provider: TerrainProvider) => {
    terrainDetailRef.current = { ...terrainDetailRef.current, auto: false, byHand: true };
    chooseTerrainProvider(provider);
  };
  useEffect(() => {
    terrainDetailFallbackRef.current = () => {
      chooseTerrainProvider("mapzen");
      announce("USGS 3DEP elevation did not load here; the Mapzen display DEM is back, overzoomed beyond zoom 11");
    };
  });
  // Past zoom 11.5 in 3D over Kansas the display DEM is only overzoomed; the live
  // USGS 3DEP mosaic carries the finer relief.
  const wantsTerrainDetail = scenePreset === "elevation-3d" && terrainProvider === "mapzen" && view.zoom > TERRARIUM_RENDER_MAX_ZOOM + 0.5
    && view.center[0] >= -102.1 && view.center[0] <= -94.5 && view.center[1] >= 36.9 && view.center[1] <= 40.1;
  useEffect(() => {
    const detail = terrainDetailRef.current;
    if (!wantsTerrainDetail || detail.byHand || detail.failed) return;
    const timer = window.setTimeout(() => {
      terrainDetailRef.current = { ...terrainDetailRef.current, auto: true };
      chooseTerrainProvider("usgs-3dep");
      announce("Close view: loading USGS 3DEP elevation for finer relief");
    }, 0);
    return () => window.clearTimeout(timer);
  // chooseTerrainProvider only sets state and refs; announce is stable.
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [wantsTerrainDetail, announce]);

  const applyTerrainLook = (look: "natural" | "topographic" | "buildings") => {
    const nextBasemap: BasemapKey = look === "natural" ? "imagery" : look === "topographic" ? "topo" : "standard";
    topographicOverlayRef.current = false; setTopographicOverlay(false);
    if (mapRef.current) setTerrainHeightOverlay(mapRef.current, false);
    structures3DRef.current = look === "buildings"; setStructures3DEnabled(look === "buildings");
    basemapRef.current = nextBasemap; setBasemap(nextBasemap);
    activateMapRepresentation("terrain");
    atmospherePresetRef.current = "clear"; setAtmospherePreset("clear");
    announce(`${look === "natural" ? "Imagery with DEM relief" : look === "topographic" ? "Topographic map with DEM relief" : "Provider-height buildings; zoom in where mapped"} selected at ${verticalExaggerationRef.current.toFixed(1)}× display scale. Source elevations, data time, and camera center are preserved.`);
  };

  const chooseLandscape = (id: string) => {
    const stop = KANSAS_FLYOVER.find((candidate) => candidate.id === id && candidate.id !== "return");
    const map = mapRef.current;
    if (!map || !stop) return;
    stopFlyover(false);
    stopSceneOrbit(false);
    // A viewpoint changes only representation and camera. In particular, do
    // not use the general representation preset that resets light and scale.
    projectionRef.current = "mercator";
    scenePresetRef.current = "elevation-3d";
    setProjection("mercator");
    setScenePreset("elevation-3d");
    replayingCameraHistoryRef.current = false;
    runMapMutation("Landscape viewpoint", () => {
      applyProjectionNavigationLimits(map, "mercator");
      map.setMaxPitch(72);
      if (styleGenerationReadyRef.current) {
        map.setProjection({ type: "mercator" });
        setTerrainState(setTerrainPresentation(map, true, verticalExaggerationRef.current));
        setTerrainHeightOverlay(map, topographicOverlayRef.current);
      }
      map.easeTo({ center: [...stop.center] as [number, number], zoom: stop.zoom, pitch: stop.pitch, bearing: stop.bearing, duration: motionDuration(900), essential: false });
    });
    announce(`${stop.label} viewpoint · Terrain 3D; your light, lens, provider, scale and data are preserved`);
  };

  const startSceneOrbit = () => {
    const map = mapRef.current;
    if (!map) { announce("The MapLibre camera is not ready yet"); return; }
    if (projectionRef.current === "globe") { announce("Choose Tilted map or Terrain 3D before orbiting"); return; }
    if (document.hidden || window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      announce("Orbit is paused while hidden or reduced motion is enabled");
      return;
    }
    stopFlyover(false);
    stopSceneOrbit(false);
    const container = map.getContainer();
    const inputs = ["pointerdown", "wheel", "touchstart", "keydown"] as const;
    const interrupt = () => stopSceneOrbit();
    const hidden = () => { if (document.hidden) stopSceneOrbit(false); };
    const cleanup = () => {
      for (const type of inputs) container.removeEventListener(type, interrupt);
      document.removeEventListener("visibilitychange", hidden);
      map.off("moveend", finish);
      if (sceneOrbitTimerRef.current !== null) window.clearTimeout(sceneOrbitTimerRef.current);
      sceneOrbitTimerRef.current = null;
      if (sceneOrbitCancelRef.current === cleanup) sceneOrbitCancelRef.current = null;
    };
    const finish = () => { cleanup(); setSceneOrbiting(false); };
    sceneOrbitCancelRef.current = cleanup;
    sceneOrbitContextRef.current = `${projectionRef.current}/${scenePresetRef.current}/${basemapRef.current}`;
    for (const type of inputs) container.addEventListener(type, interrupt, { passive: true });
    document.addEventListener("visibilitychange", hidden);
    setSceneOrbiting(true);
    replayingCameraHistoryRef.current = true;
    map.easeTo({ bearing: map.getBearing() + 90, pitch: Math.max(46, map.getPitch()), duration: 12_000, easing: (progress) => progress, essential: false });
    // Register after easeTo, whose initial stop can emit an older moveend.
    map.once("moveend", finish);
    sceneOrbitTimerRef.current = window.setTimeout(finish, 12_050);
    announce("Orbit started · drag, scroll or press a key to take back the camera");
  };

  /** Camera-only tour of Kansas landscapes in Terrain 3D. Any direct map input
   * hands the camera back; nothing is selected, filtered or recorded. */
  const startFlyover = () => {
    const map = mapRef.current;
    if (!map) {
      announce("The MapLibre camera is not ready yet");
      return;
    }
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      announce("Flyover is unavailable because reduced motion is enabled");
      return;
    }
    stopFlyover(false);
    if (scenePresetRef.current !== "elevation-3d" || projectionRef.current === "globe") activateMapRepresentation("terrain");
    else stopSceneOrbit(false);
    const container = map.getContainer();
    const inputs = ["pointerdown", "wheel", "touchstart", "keydown"] as const;
    let cancelled = false;
    const interrupt = () => stopFlyover();
    const hidden = () => { if (document.hidden) stopFlyover(false); };
    const cleanup = () => {
      cancelled = true;
      for (const type of inputs) container.removeEventListener(type, interrupt);
      document.removeEventListener("visibilitychange", hidden);
      map.stop();
    };
    flyoverCancelRef.current = cleanup;
    document.addEventListener("visibilitychange", hidden);
    for (const type of inputs) container.addEventListener(type, interrupt, { passive: true });
    const visit = (index: number) => {
      if (cancelled) return;
      const stop = KANSAS_FLYOVER[index];
      if (!stop) {
        flyoverCancelRef.current = null;
        cleanup();
        setFlyoverStopIndex(null);
        announce("Flyover complete · Terrain 3D stays on");
        return;
      }
      setFlyoverStopIndex(index);
      replayingCameraHistoryRef.current = true;
      map.flyTo({ center: [...stop.center] as [number, number], zoom: stop.zoom, pitch: stop.pitch, bearing: stop.bearing, duration: stop.flightMs, curve: 1.5, essential: true });
      // Register after starting: flyTo stops any earlier animation synchronously.
      map.once("moveend", () => {
        if (cancelled) return;
        if (!stop.dwellMs) { visit(index + 1); return; }
        replayingCameraHistoryRef.current = true;
        map.easeTo({ bearing: stop.bearing + stop.drift, duration: stop.dwellMs, easing: (progress) => progress, essential: true });
        map.once("moveend", () => visit(index + 1));
      });
    };
    announce("Flyover started · drag, scroll or press any key to take back the camera");
    visit(0);
  };

  const setMapGestureMode = (mode: "cooperative" | "direct") => {
    gestureModeRef.current = mode;
    setGestureMode(mode);
    announce(mode === "cooperative" ? "Cooperative map gestures enabled" : "Direct map gestures enabled");
  };

  const probeSourceConnection = (layer: LayerRecord) => {
    const map = mapRef.current;
    if (!map?.isStyleLoaded() || map.getSource(layer.sourceId)?.loaded() !== true) {
      announce(`${layer.title} is not ready for a MapLibre source query`);
      return;
    }
    const uniqueFeatures = new Set(map.querySourceFeatures(layer.sourceId).map((feature) => String(feature.properties?.fid ?? feature.id ?? "anonymous")));
    setSourceProbeCounts((current) => ({ ...current, [layer.id]: uniqueFeatures.size }));
    announce(`${layer.title} source connection returned ${uniqueFeatures.size} stable feature${uniqueFeatures.size === 1 ? "" : "s"}`);
  };

  const inspectSourceConnection = (layer: LayerRecord) => {
    setMapFeatureQuery("");
    setMapFeatureLayer(layer.id);
    openMapUtility("inspect");
  };

  const applyViewProfile = (profile: MapViewProfile) => {
    const baselineSources = BASELINE_STACKS[profile.id];
    const nextVisibility = Object.fromEntries(LAYER_REGISTRY.map((layer) => [layer.id, baselineSources ? false : profile.visibleLayerIds.includes(layer.id)]));
    if (baselineSources) for (const source of OFFICIAL_CONTEXT_SOURCES) setOfficialContextVisible(source.id, baselineSources.includes(source.id));
    const nextScenePreset: ScenePresetId = profile.id === "smoke" ? "smoke-context" : profile.id === "elevation" ? "elevation-3d" : profile.projection === "globe" ? "globe-overview" : "overview-2d";
    const nextAtmosphere: AtmospherePreset = profile.id === "smoke" || profile.id === "hazards" || profile.id === "elevation" ? "dusk" : profile.projection === "globe" ? "clear" : "night";
    const nextLightAzimuth = profile.id === "elevation" ? 235 : profile.projection === "globe" ? 225 : 210;
    const nextFieldOfView = profile.id === "elevation" ? compositionDefaults("terrain").fieldOfView : profile.projection === "globe" ? 42 : 36;
    stopSceneOrbit(false);
    mapRef.current?.stop();
    visibilityRef.current = nextVisibility;
    mapEvidenceFilterRef.current = "ALL";
    const profileBasemap = profile.projection === "globe" ? "standard" : profile.basemap;
    basemapRef.current = profileBasemap;
    projectionRef.current = profile.projection;
    scenePresetRef.current = nextScenePreset;
    verticalExaggerationRef.current = profile.id === "elevation" ? DEFAULT_TERRAIN_DEPTH : 1;
    atmospherePresetRef.current = nextAtmosphere;
    lightAzimuthRef.current = nextLightAzimuth;
    fieldOfViewRef.current = nextFieldOfView;
    setVisibility(nextVisibility);
    commitTemporalFrame(baselineSources ? OFFICIAL_CONTEXT_PRESENT_FRAME : profile.year);
    setMapEvidenceFilter("ALL");
    setPlaying(false);
    setTemporalMode("snapshot");
    setBasemap(profileBasemap);
    setProjection(profile.projection);
    setScenePreset(nextScenePreset);
    setVerticalExaggeration(verticalExaggerationRef.current);
    setAtmospherePreset(nextAtmosphere);
    setLightAzimuth(nextLightAzimuth);
    setFieldOfView(nextFieldOfView);
    setMapQueryCandidates([]);
    locationDerivedViewRef.current = false;
    setLocationCameraRedacted(false);
    clearSelectionState();
    const map = mapRef.current;
    if (map) { applyProjectionNavigationLimits(map, profile.projection); if (profile.id === "elevation") map.setMaxPitch(72); }
    if (map?.isStyleLoaded()) {
      if (nextScenePreset !== "elevation-3d") {
        setTerrainState(setTerrainPresentation(map, false, 1));
        setTerrainHeightOverlay(map, false);
      } else {
        setTerrainState(setTerrainPresentation(map, true, verticalExaggerationRef.current));
        setTerrainHeightOverlay(map, topographicOverlayRef.current);
      }
      map.setProjection({ type: profile.projection });
      applyOfficialContextState(map, runtimeOfficialVisibility(officialVisibilityRef.current, temporalQueryRef.current.frame, noaaRadarReadyRef.current, noaaRadarFrameTimeRef.current), officialOpacityRef.current, officialPayloadsRef.current);
      applySceneEnvironment(map, nextAtmosphere, nextLightAzimuth);
      map.setVerticalFieldOfView(nextFieldOfView);
      map.triggerRepaint();
    }
    if (profile.id === "overview") {
      map?.easeTo({ center: [...KANSAS_VIEW.center] as [number, number], zoom: KANSAS_VIEW.zoom, bearing: KANSAS_VIEW.bearing, pitch: KANSAS_VIEW.pitch, duration: motionDuration(600) });
    } else {
      map?.fitBounds([[-102.1, 36.95], [-94.55, 40.05]], { padding: 54, duration: motionDuration(600), ...(profile.id === "elevation" ? { pitch: compositionDefaults("terrain").pitch } : {}) });
    }
    announce(`${profile.title} applied · view state only`);
  };

  const applyLivingAtlasView = (atlasView: LivingAtlasView) => {
    const profile = atlasView.profileId ? MAP_VIEW_PROFILES.find((candidate) => candidate.id === atlasView.profileId) : undefined;
    if (atlasView.profileId && !profile) {
      announce(`${atlasView.title} is not available in this Site build`);
      return;
    }
    setCurrentWorkspace("explore");
    setLeftPanelMode("views");
    if (profile) applyViewProfile(profile);
    // The profile sets its starting stack; a view adds the sources only it needs.
    for (const sourceId of atlasView.sources) setOfficialContextVisible(sourceId, true);
    if (atlasView.id === "living-waters") setLiveInstrument("river");
    if (atlasView.camera && !atlasView.story) {
      mapRef.current?.easeTo({
        center: [...atlasView.camera.center] as [number, number],
        zoom: atlasView.camera.zoom,
        bearing: atlasView.camera.bearing,
        pitch: atlasView.camera.pitch,
        duration: motionDuration(650),
      });
    }
    setLeftOpen(false);
    if (isCompact) {
      setRightOpen(false);
      setTimelineOpen(false);
    }
    announce(`${atlasView.title} opened · ${livingAtlasStatusLabel(atlasView.status)}`);
  };

  const persistSavedWorkspaces = (next: WorkspaceSnapshot[]) => {
    const bounded = next.slice(0, MAX_PLACE_TRAIL_STOPS);
    let saved = false;
    try { saved = writeSavedWorkspaceList(window.localStorage, WORKSPACE_STORAGE_KEY, bounded); } catch { /* Browser may deny the storage getter itself. */ }
    if (!saved) { announce("Investigation could not be saved on this device. Storage may be full or unavailable; your open map is unchanged."); return false; }
    setSavedWorkspaces(bounded);
    return true;
  };

  const saveCurrentWorkspace = () => {
    const savedAt = new Date().toISOString();
    const redactWorkspaceCamera = locationCameraRedacted || locationDerivedViewRef.current || researchLocationRedacted || subsurfacePrivate;
    const snapshot: WorkspaceSnapshot = {
      id: `workspace-${Date.now()}`,
      name: normalizePlaceStopName(workspaceName || (!redactWorkspaceCamera && researchOpen && researchAnchor ? `Near ${researchAnchor.title}` : ""), savedWorkspaces.length + 1),
      savedAt,
      view: redactWorkspaceCamera
        ? { center: [...KANSAS_VIEW.center] as [number, number], zoom: KANSAS_VIEW.zoom, bearing: KANSAS_VIEW.bearing, pitch: KANSAS_VIEW.pitch }
        : { center: [...view.center] as [number, number], zoom: view.zoom, bearing: view.bearing, pitch: view.pitch },
      locationCameraRedacted: redactWorkspaceCamera,
      researchContext: persistableResearch(researchContext && { ...researchContext, capturedAt: savedAt }, redactWorkspaceCamera, true),
      subsurfaceContext: persistableSubsurface(subsurfaceContext && { ...subsurfaceContext, capturedAt: savedAt }, redactWorkspaceCamera, true),
      visibility: { ...visibility },
      opacity: { ...opacity },
      layerOrder: [...layerOrder],
      year,
      mapEvidenceFilter,
      basemap,
      projection,
      scene: {
        preset: scenePreset,
        verticalExaggeration,
        atmosphere: atmospherePreset,
        lightAzimuth,
        fieldOfView,
      },
      measurement: redactWorkspaceCamera || !measurementGeometryMode
        ? null
        : { mode: measurementGeometryMode, unit: measureUnit, label: measurement, coordinates: measureCoordinatesRef.current.map(([longitude, latitude]) => [longitude, latitude] as [number, number]) },
      analysisArea: !redactWorkspaceCamera && analysisArea ? { ...analysisArea } : null,
      temporalComparison: { timeA: compareTimeA, timeB: compareTimeB },
      temporalSweep: {
        mode: temporalMode,
        stepRule: temporalStepRule,
        rangeStart: sweepRangeStart,
        rangeEnd: sweepRangeEnd,
        windowFrames: movingWindowFrames,
        direction: playbackDirection,
        loopMode: playbackLoopMode,
      },
      report: {
        title: reportTitle,
        scope: reportScope,
        detail: reportDetail,
        layerIds: [...reportLayerIds],
        sections: { ...reportSections },
        query: reportQuery,
        evidenceFilter: reportEvidenceFilter,
      },
      selection: selected ? { layerId: selected.layerId, featureId: selected.featureId } : null,
    };
    if (!persistSavedWorkspaces([snapshot, ...savedWorkspaces])) return;
    setActivePlaceId(snapshot.id);
    setWorkspaceName("");
    announce(`${snapshot.name} added to Places on this device`);
  };

  const loadSavedWorkspace = (snapshot: WorkspaceSnapshot) => {
    stopSceneOrbit(false);
    const knownLayerIds = new Set(LAYER_REGISTRY.map((layer) => layer.id));
    const nextVisibility = Object.fromEntries(LAYER_REGISTRY.map((layer) => [layer.id, snapshot.visibility?.[layer.id] === true]));
    const nextOpacity = Object.fromEntries(LAYER_REGISTRY.map((layer) => [layer.id, clamp(Number(snapshot.opacity?.[layer.id] ?? layer.defaultOpacity), 0, 1)]));
    const savedOrder = Array.isArray(snapshot.layerOrder) ? snapshot.layerOrder.filter((id) => knownLayerIds.has(id)) : [];
    const nextOrder = [...savedOrder, ...defaultOrder.filter((id) => !savedOrder.includes(id))];
    const nextYear = KNOWN_TEMPORAL_FRAMES.has(snapshot.year) ? snapshot.year : OFFICIAL_CONTEXT_PRESENT_FRAME;
    const nextBasemap: BasemapKey = isBasemapKey(snapshot.basemap) ? snapshot.basemap : "standard";
    const nextProjection = snapshot.projection === "globe" ? "globe" : "mercator";
    // Legacy snapshots predate the marker, so fail closed instead of exposing a possibly location-derived camera.
    const restoredLocationCameraRedaction = snapshot.locationCameraRedacted !== false;
    const savedScene = snapshot.scene;
    const nextScenePreset: ScenePresetId = savedScene?.preset === "globe-overview" || savedScene?.preset === "water-systems" || savedScene?.preset === "smoke-context" || savedScene?.preset === "elevation-3d" || savedScene?.preset === "tile-grid" ? savedScene.preset : "overview-2d";
    const nextVerticalExaggeration = nextScenePreset === "elevation-3d" ? terrainDepth(Number(savedScene?.verticalExaggeration ?? DEFAULT_TERRAIN_DEPTH)) : clamp(Number(savedScene?.verticalExaggeration ?? 1), 0, 2);
    const nextAtmosphere: AtmospherePreset = savedScene?.atmosphere === "dusk" || savedScene?.atmosphere === "clear" ? savedScene.atmosphere : "night";
    const nextLightAzimuth = clamp(Number(savedScene?.lightAzimuth ?? 210), 0, 359);
    const nextFieldOfView = clamp(Number(savedScene?.fieldOfView ?? 36), 20, 60);
    visibilityRef.current = nextVisibility;
    opacityRef.current = nextOpacity;
    orderRef.current = nextOrder;
    yearRef.current = nextYear;
    const savedMapEvidenceFilter = snapshot.mapEvidenceFilter;
    const nextMapEvidenceFilter: RegistryEvidenceFilter = savedMapEvidenceFilter && savedMapEvidenceFilter in evidenceLabels ? savedMapEvidenceFilter : "ALL";
    mapEvidenceFilterRef.current = nextMapEvidenceFilter;
    basemapRef.current = nextBasemap;
    projectionRef.current = nextProjection;
    verticalExaggerationRef.current = nextVerticalExaggeration;
    atmospherePresetRef.current = nextAtmosphere;
    lightAzimuthRef.current = nextLightAzimuth;
    fieldOfViewRef.current = nextFieldOfView;
    setVisibility(nextVisibility);
    setOpacity(nextOpacity);
    setLayerOrder(nextOrder);
    setYear(nextYear);
    setPreviewYear(nextYear);
    setMapEvidenceFilter(nextMapEvidenceFilter);
    setPlaying(false);
    const savedSweep = snapshot.temporalSweep;
    const savedSweepMode = savedSweep?.mode;
    const nextSavedSweepMode: TemporalSweepMode = savedSweepMode === "moving-window" || savedSweepMode === "event-stepping" || savedSweepMode === "accumulation" || savedSweepMode === "comparison" ? savedSweepMode : "snapshot";
    setTemporalMode(nextSavedSweepMode);
    setTemporalStepRule(savedSweep?.stepRule === "available-events" ? "available-events" : "regular-calendar");
    const savedSweepRangeValid = savedSweep
      && TIME_STEPS.includes(savedSweep.rangeStart as (typeof TIME_STEPS)[number])
      && TIME_STEPS.includes(savedSweep.rangeEnd as (typeof TIME_STEPS)[number])
      && savedSweep.rangeStart <= nextYear
      && savedSweep.rangeEnd >= nextYear
      && savedSweep.rangeStart <= savedSweep.rangeEnd;
    setSweepRangeStart(savedSweepRangeValid ? savedSweep.rangeStart : TIME_STEPS[0]);
    setSweepRangeEnd(savedSweepRangeValid ? savedSweep.rangeEnd : TIME_STEPS.at(-1)!);
    setMovingWindowFrames(clamp(Math.round(savedSweep?.windowFrames ?? 3), 1, 8));
    setPlaybackDirection(savedSweep?.direction === "reverse" ? "reverse" : "forward");
    setPlaybackLoopMode(savedSweep?.loopMode === "loop" ? "loop" : "stop");
    setBasemap(nextBasemap);
    setProjection(nextProjection);
    setScenePreset(nextScenePreset);
    setVerticalExaggeration(nextVerticalExaggeration);
    setAtmospherePreset(nextAtmosphere);
    setLightAzimuth(nextLightAzimuth);
    setFieldOfView(nextFieldOfView);
    const savedMeasurement = restoredLocationCameraRedaction ? null : snapshot.measurement;
    const restoredMeasurement = savedMeasurement
      && (savedMeasurement.mode === "distance" || savedMeasurement.mode === "area")
      && Array.isArray(savedMeasurement.coordinates)
      && savedMeasurement.coordinates.length > 0
      && savedMeasurement.coordinates.every((coordinate) => Array.isArray(coordinate) && coordinate.length === 2 && coordinate.every(Number.isFinite))
      ? savedMeasurement
      : null;
    measureModeRef.current = null;
    measurementGeometryModeRef.current = restoredMeasurement?.mode ?? null;
    measureCoordinatesRef.current = restoredMeasurement ? restoredMeasurement.coordinates.map(([longitude, latitude]) => [longitude, latitude] as [number, number]) : [];
    setMeasureCoordinateCount(measureCoordinatesRef.current.length);
    setMeasureMode(null);
    setMeasurementGeometryMode(restoredMeasurement?.mode ?? null);
    setMeasurement(restoredMeasurement?.label ?? "Select a measurement tool");
    if (mapRef.current?.isStyleLoaded()) updateMeasurementSource(mapRef.current, buildMeasurementData(measureCoordinatesRef.current, measurementGeometryModeRef.current));
    const savedAnalysisArea = snapshot.analysisArea;
    const nextAnalysisArea = savedAnalysisArea
      && Number.isFinite(savedAnalysisArea.west)
      && Number.isFinite(savedAnalysisArea.south)
      && Number.isFinite(savedAnalysisArea.east)
      && Number.isFinite(savedAnalysisArea.north)
      && savedAnalysisArea.west < savedAnalysisArea.east
      && savedAnalysisArea.south < savedAnalysisArea.north
      ? { ...savedAnalysisArea }
      : null;
    analysisAreaRef.current = nextAnalysisArea;
    setAnalysisArea(nextAnalysisArea);
    if (mapRef.current?.isStyleLoaded()) updateAnalysisAreaSource(mapRef.current, nextAnalysisArea);
    const savedComparison = snapshot.temporalComparison;
    setCompareTimeA(savedComparison && TIME_STEPS.includes(savedComparison.timeA as (typeof TIME_STEPS)[number]) ? savedComparison.timeA : 1910);
    setCompareTimeB(savedComparison && TIME_STEPS.includes(savedComparison.timeB as (typeof TIME_STEPS)[number]) ? savedComparison.timeB : OFFICIAL_CONTEXT_PRESENT_FRAME);
    setMapUtilityView(nextSavedSweepMode === "comparison" ? "compare" : "scene");
    setMapUtilityOpen(nextSavedSweepMode === "comparison");
    setReportTitle(snapshot.report?.title || "Kansas map data report");
    setReportScope(snapshot.report?.scope === "SELECTION" || snapshot.report?.scope === "VISIBLE_LAYERS" || (snapshot.report?.scope === "ANALYSIS_AREA" && nextAnalysisArea) ? snapshot.report.scope : "VIEWPORT");
    setReportDetail(snapshot.report?.detail === "EXECUTIVE" || snapshot.report?.detail === "TECHNICAL" ? snapshot.report.detail : "STANDARD");
    const savedReportLayerIds = (snapshot.report?.layerIds ?? []).filter((id) => knownLayerIds.has(id));
    setReportLayerIds(savedReportLayerIds.length ? savedReportLayerIds : LAYER_REGISTRY.filter((layer) => nextVisibility[layer.id]).map((layer) => layer.id));
    setReportSections({ ...defaultReportSections, ...(snapshot.report?.sections ?? {}) });
    setReportQuery(snapshot.report?.query ?? "");
    const savedEvidenceFilter = snapshot.report?.evidenceFilter;
    setReportEvidenceFilter(savedEvidenceFilter === "ALL" || (savedEvidenceFilter && savedEvidenceFilter in evidenceLabels) ? savedEvidenceFilter : "ALL");
    setReportGeneratedAt(new Date().toISOString());
    const savedView = snapshot.view;
    if (mapRef.current) applyProjectionNavigationLimits(mapRef.current, nextProjection);
    if (savedView && Array.isArray(savedView.center) && savedView.center.length === 2) {
      locationDerivedViewRef.current = restoredLocationCameraRedaction;
      setLocationCameraRedacted(restoredLocationCameraRedaction);
      mapRef.current?.easeTo({ center: [...savedView.center] as [number, number], zoom: savedView.zoom, bearing: savedView.bearing, pitch: savedView.pitch, duration: motionDuration(650) });
    }
    const restoredLayer = LAYER_REGISTRY.find((layer) => layer.id === snapshot.selection?.layerId);
    const restoredSelection = snapshot.selection && restoredLayer ? copyFeature(restoredLayer, snapshot.selection.featureId) : null;
    selectedRef.current = restoredSelection;
    setSelected(restoredSelection);
    setActivePlaceId(snapshot.id);
    const savedSubsurface = !restoredLocationCameraRedaction && validSubsurfaceContext(snapshot.subsurfaceContext) ? snapshot.subsurfaceContext : null;
    setSubsurfaceContext(savedSubsurface);
    setSubsurfacePrivate(false);
    setSubsurfaceInspection(null);
    setUndergroundOpen(Boolean(savedSubsurface));
    if (savedSubsurface) setPlaying(false);
    setUndergroundRestoreKey(v => v + 1);
    const savedResearch = !restoredLocationCameraRedaction && validResearchContext(snapshot.researchContext) ? snapshot.researchContext : null;
    setResearchAnchor(savedResearch?.anchor ?? null);
    setResearchCounty(savedResearch?.county ?? null);
    setResearchLocationRedacted(false);
    setNearbyRadiusMiles(savedResearch?.radiusMiles ?? 25);
    setResearchOpen(Boolean(savedResearch));
    setRightOpen(Boolean(savedResearch));
    if (savedResearch) {
      const sourceIds = new Set(savedResearch.coverage.map(item => item.sourceId));
      if (savedResearch.county) sourceIds.add("census-counties");
      for (const source of OFFICIAL_CONTEXT_SOURCES) {
        const visible = sourceIds.has(source.id);
        if (officialVisibilityRef.current[source.id] !== visible) setOfficialContextVisible(source.id, visible);
        // An explicit reopen refreshes existing eligible feeds as well as loading missing ones.
        if (visible && officialPayloadsRef.current[source.id as OfficialContextFeedId]) retryOfficialLayer(source.id);
      }
      setResearchMissingSources(savedResearch.coverage.filter(item => !OFFICIAL_CONTEXT_SOURCES.some(source => source.id === item.sourceId) && !knownLayerIds.has(item.sourceId))
        .map(item => ({ ...item, state: "unavailable", limitation: "This saved source is no longer available in this Site. Its old response is not restored." })));
      if (isCompact) { setLeftOpen(false); setTimelineOpen(false); }
    } else setResearchMissingSources([]);
    setMapQueryCandidates([]);
    announce(`${snapshot.name} restored from Places on this device${savedResearch ? "; dossier data reloads from eligible sources, saved rows are not reused" : ""}`);
  };

  const stopPlaceTour = (announceStop = true) => {
    if (placeTourTimerRef.current !== null) window.clearTimeout(placeTourTimerRef.current);
    placeTourTimerRef.current = null;
    setPlaceTourPlaying(false);
    if (announceStop) announce("Places trail stopped");
  };

  const stepPlaceTrail = (direction: -1 | 1) => {
    stopPlaceTour(false);
    const currentIndex = savedWorkspaces.findIndex((snapshot) => snapshot.id === activePlaceId);
    const nextIndex = nextPlaceStopIndex(savedWorkspaces.length, currentIndex, direction);
    if (nextIndex < 0) {
      announce("Save a place before stepping through a trail");
      return;
    }
    loadSavedWorkspace(savedWorkspaces[nextIndex]);
  };

  const playPlaceTrail = () => {
    if (savedWorkspaces.length < 2) {
      announce("Save at least two places to play a trail");
      return;
    }
    stopPlaceTour(false);
    setPlaceTourPlaying(true);
    const trail = [...savedWorkspaces];
    const visit = (index: number) => {
      const stop = trail[index];
      if (!stop) {
        placeTourTimerRef.current = null;
        setPlaceTourPlaying(false);
        announce("Places trail complete");
        return;
      }
      loadSavedWorkspace(stop);
      placeTourTimerRef.current = window.setTimeout(() => visit(index + 1), 3_600);
    };
    visit(0);
  };

  const reorderSavedWorkspace = (snapshot: WorkspaceSnapshot, direction: -1 | 1) => {
    stopPlaceTour(false);
    if (!persistSavedWorkspaces(reorderPlaceStops(savedWorkspaces, snapshot.id, direction))) return;
    announce(`${snapshot.name} moved ${direction < 0 ? "earlier" : "later"} in the Places trail`);
  };

  const deleteSavedWorkspace = (snapshot: WorkspaceSnapshot) => {
    stopPlaceTour(false);
    if (!persistSavedWorkspaces(savedWorkspaces.filter((candidate) => candidate.id !== snapshot.id))) return;
    if (activePlaceId === snapshot.id) setActivePlaceId(null);
    announce(`${snapshot.name} removed from this device`);
  };

  const updateMapEvidenceFilter = (nextFilter: RegistryEvidenceFilter) => {
    mapEvidenceFilterRef.current = nextFilter;
    setMapEvidenceFilter(nextFilter);
    announce(nextFilter === "ALL" ? "Showing every compatible evidence state" : `Map filtered to ${nextFilter.replaceAll("_", " ")}`);
  };

  const openResearchDossier = (replaceAnchor = false, returnElement?: HTMLElement) => {
    const anchor = chooseResearchAnchor(researchAnchor, selectedResearchRecord, replaceAnchor);
    if (!anchor) { announce("Select an eligible registry record or loaded provider point to start a dossier."); return; }
    if (replaceAnchor || !researchAnchor) {
      setResearchAnchor(anchor);
      setResearchLocationRedacted(locationCameraRedacted || locationDerivedViewRef.current);
      setResearchMissingSources([]);
      researchResultFocusRef.current = null;
    }
    if (returnElement) returnFocusRef.current = returnElement;
    setResearchOpen(true);
    setRightOpen(true);
    setMapUtilityOpen(false);
    setCurrentWorkspace("trust");
    if (isCompact) { setLeftOpen(false); setTimelineOpen(false); }
  };

  const centerResearchRecord = (record: ResearchRecord) => {
    mapRef.current?.easeTo({ center: [...record.coordinates], zoom: Math.max(view.zoom, 8), duration: motionDuration(500) });
    announce(`Centered ${record.title}; ${record.kind === "registry" ? "registry display anchor" : "provider point"}`);
  };

  const inspectResearchRecord = (record: ResearchRecord) => {
    if (!researchData.records.some(item => researchIdentity(item) === researchIdentity(record))) {
      announce("This record is no longer in the eligible loaded data. Its captured source details remain in the dossier."); return;
    }
    researchResultFocusRef.current = researchIdentity(record);
    if (record.kind === "provider" && (Object.values(AVIATION_RESEARCH_SOURCE) as string[]).includes(record.sourceId)) {
      // Aviation points open the aviation layer's own point inspector: airspace column, drone rule and weather there.
      const [lon, lat] = record.coordinates;
      setAviationInspect({ lon, lat, label: record.title, nonce: Date.now() });
      mapRef.current?.easeTo({ center: [lon, lat], zoom: Math.max(mapRef.current.getZoom(), 10), duration: window.matchMedia("(prefers-reduced-motion: reduce)").matches ? 0 : 600 });
      setResearchOpen(false);
      // The inspector lives in the Layers panel, which a compact dossier closed (and made inert).
      setSourceStatusOpen(false);
      setLeftPanelMode("layers");
      setLeftOpen(true);
      if (isCompact) { setRightOpen(false); setTimelineOpen(false); }
      announce(shownCatalogIds.has("aviation") ? "Opened in the airspace, airports and aviation weather point inspector."
        : "Opened in the aviation point inspector, which the current catalog search hides; clear the search to see it.");
      return;
    }
    if (record.kind === "registry") {
      const layer = LAYER_REGISTRY.find(item => visibility[item.id] && item.sourceId === record.sourceId && item.data.features.some(feature => feature.properties.fid === record.featureId));
      if (!layer) { announce("This registry source is no longer available."); return; }
      selectIndexedFeature(layer.id, record.featureId);
    }
    else {
      const source = OFFICIAL_CONTEXT_SOURCES.find(item => item.id === record.sourceId);
      const data = record.sourceId === "kgs-monitoring-wells" ? researchSnapshotPoints : officialPayloads[record.sourceId as OfficialContextFeedId]?.data;
      const feature = data?.features.find(item => String(item.properties?.featureId ?? item.id) === record.featureId);
      if (!source || !feature) { announce("The selected provider record is unavailable. Refresh its source."); return; }
      const context = buildBasemapContext({ ...feature, source: source.sourceId }, record.coordinates[0], record.coordinates[1]);
      if (!context) return;
      openSelection(context);
      if (mapRef.current?.isStyleLoaded()) updateSelectionSource(mapRef.current, context.geometry);
    }
    setResearchOpen(false);
    window.requestAnimationFrame(() => rightPanelRef.current?.querySelector<HTMLElement>("[data-selection-summary]")?.focus());
  };

  useEffect(() => {
    if (!researchOpen || !rightOpen) return;
    const frame = window.requestAnimationFrame(() => {
      const previous = Array.from(rightPanelRef.current?.querySelectorAll<HTMLElement>("[data-research-record]") ?? [])
        .find(element => element.dataset.researchRecord === researchResultFocusRef.current)?.querySelector<HTMLButtonElement>("button");
      (previous ?? rightPanelRef.current?.querySelector<HTMLElement>("[data-research-heading]"))?.focus();
    });
    return () => window.cancelAnimationFrame(frame);
  }, [researchOpen, rightOpen]);

  const isolateLayer = (layer: LayerRecord) => {
    const next = Object.fromEntries(LAYER_REGISTRY.map((candidate) => [candidate.id, candidate.id === layer.id]));
    visibilityRef.current = next;
    setVisibility(next);
    announce(`${layer.title} isolated on the map`);
  };

  const restoreLastKnownGoodView = () => {
    const lastView = lastKnownGoodViewRef.current;
    mapRef.current?.jumpTo({ ...lastView, center: [...lastView.center] as [number, number] });
    announce("Restored the last known local camera state");
  };

  const reapplyRendererState = () => {
    const map = mapRef.current;
    if (!map || !styleGenerationReadyRef.current) {
      announce("Style is not ready; renderer state was not changed");
      return;
    }
    try {
      applyRegistryState(map, visibilityRef.current, opacityRef.current, yearRef.current, orderRef.current, mapEvidenceFilterRef.current, temporalQueryRef.current);
      noaaRadarReadyRef.current = Boolean(
        noaaRadarFrameTimeRef.current
        && noaaRadarManifestIsFresh(noaaRadarManifestRef.current, Date.now()),
      );
      if (noaaRadarReadyRef.current && noaaRadarFrameTimeRef.current && !noaaRadarObservationTimeIsApplied(map, noaaRadarFrameTimeRef.current)) {
        applyNoaaRadarFrame(noaaRadarFrameTimeRef.current);
      }
      applyOfficialContextState(map, runtimeOfficialVisibility(officialVisibilityRef.current, temporalQueryRef.current.frame, noaaRadarReadyRef.current, noaaRadarFrameTimeRef.current), officialOpacityRef.current, officialPayloadsRef.current);
      setElevationExaggeration(map, verticalExaggerationRef.current);
      map.setProjection({ type: projectionRef.current });
      applySceneEnvironment(map, atmospherePresetRef.current, lightAzimuthRef.current);
      map.setVerticalFieldOfView(fieldOfViewRef.current);
      const currentSelection = selectedRef.current;
      const selectionAvailable = currentSelection
        && selectionCarrierIsVisible(currentSelection, visibilityRef.current,
          runtimeOfficialVisibility(officialVisibilityRef.current, temporalQueryRef.current.frame, noaaRadarReadyRef.current, noaaRadarFrameTimeRef.current))
        && !officialSelectionIsHeld(currentSelection, temporalQueryRef.current.frame, buildYearCurrentRef.current,
          civicDayForFrame(temporalQueryRef.current.frame, OFFICIAL_CONTEXT_PRESENT_FRAME, currentUtcDay(), calendarSweepRef.current ? calendarFrameDay(calendarSweepRef.current) : null))
        && isFeatureAvailableForTemporalQuery(currentSelection.layer, currentSelection.properties.year, temporalQueryRef.current)
        && selectionPassesEvidenceFilter(currentSelection, mapEvidenceFilterRef.current);
      updateSelectionSource(map, selectionAvailable ? currentSelection.geometry : null);
      updateMeasurementSource(map, buildMeasurementData(measureCoordinatesRef.current, measurementGeometryModeRef.current));
      updateAnalysisAreaSource(map, analysisAreaRef.current);
      setSourceStates((current) => Object.fromEntries(LAYER_REGISTRY.map((layer) => [
        layer.id,
        current[layer.id] === "error" ? "error" : map.getSource(layer.sourceId) ? "ready" : "loading",
      ])));
      const hasKnownSourceError = Object.values(sourceStates).includes("error");
      setRuntime(hasKnownSourceError
        ? { kind: "degraded", message: "Renderer state reapplied; known source errors remain visible for diagnosis" }
        : { kind: "ready", message: "MapLibre renderer state reapplied from the site registry" });
      announce(hasKnownSourceError ? "Reapplied renderer state without clearing known source errors" : "Reapplied local style, layers, time, selection, measurement, and analysis-area state");
    } catch {
      setRuntime({ kind: "degraded", message: `Registry reapply failed safely: ${mapRuntimeErrorCode("start")}` });
      announce("Renderer state could not be fully reapplied; diagnostics remain available");
    }
  };

  const resetExplorer = () => {
    const map = mapRef.current;
    visibilityRef.current = defaultVisibility;
    opacityRef.current = defaultOpacity;
    officialVisibilityRef.current = defaultOfficialVisibility;
    officialOpacityRef.current = defaultOfficialOpacity;
    orderRef.current = defaultOrder;
    yearRef.current = OFFICIAL_CONTEXT_PRESENT_FRAME;
    mapEvidenceFilterRef.current = "ALL";
    basemapRef.current = "standard";
    projectionRef.current = "mercator";
    scenePresetRef.current = "overview-2d";
    verticalExaggerationRef.current = 1;
    topographicOverlayRef.current = false;
    atmospherePresetRef.current = "night";
    lightAzimuthRef.current = 210;
    fieldOfViewRef.current = 36;
    structures3DRef.current = false;
    gestureModeRef.current = "cooperative";
    setVisibility(defaultVisibility);
    setOpacity(defaultOpacity);
    setOfficialVisibility(defaultOfficialVisibility);
    setOfficialOpacity(defaultOfficialOpacity);
    setOfficialErrors({});
    noaaRadarRequestRef.current?.abort();
    noaaRadarRequestRef.current = null;
    noaaRadarLastRequestAtRef.current = 0;
    noaaRadarReadyRef.current = false;
    noaaRadarManifestRef.current = null;
    noaaRadarFrameTimeRef.current = null;
    noaaRadarPendingFrameTimeRef.current = null;
    noaaRadarRequestedTimeRef.current = null;
    noaaRadarFollowLatestRef.current = true;
    noaaRadarFrameLoadCleanupRef.current?.();
    noaaRadarFrameLoadCleanupRef.current = null;
    noaaRadarFrameFailureRef.current = null;
    setNoaaRadarManifestState("idle");
    setNoaaRadarManifest(null);
    setNoaaRadarManifestError("");
    setNoaaRadarFrameTime(null);
    setNoaaRadarPendingFrameTime(null);
    setNoaaRadarLoopSpan(60);
    setNoaaRadarPlaybackSpeed(1);
    setNoaaRadarPlaying(false);
    setNoaaRadarFollowLatest(true);
    setNoaaRadarFrameLoadState("idle");
    for (const source of OFFICIAL_CONTEXT_SOURCES) {
      if ((source.defaultVisibility || searchNeedsCounties(source.id)) && source.apiPath && !officialPayloadsRef.current[source.id as OfficialContextFeedId]) void refreshOfficialContext(source.id as OfficialContextFeedId);
    }
    setLayerOrder(defaultOrder);
    setYear(OFFICIAL_CONTEXT_PRESENT_FRAME);
    setPreviewYear(OFFICIAL_CONTEXT_PRESENT_FRAME);
    setTemporalMode("snapshot");
    setTemporalStepRule("regular-calendar");
    setPlaybackSpeed(1);
    setPlaybackDirection("forward");
    setPlaybackLoopMode("stop");
    setSweepRangeStart(TIME_STEPS[0]);
    setSweepRangeEnd(TIME_STEPS.at(-1)!);
    setMovingWindowFrames(3);
    setPlaying(false);
    setDynamicEffects(true);
    setMapEvidenceFilter("ALL");
    setCompareTimeA(1910);
    setCompareTimeB(OFFICIAL_CONTEXT_PRESENT_FRAME);
    setBasemap("standard");
    setProjection("mercator");
    setScenePreset("overview-2d");
    setVerticalExaggeration(1);
    setTopographicOverlay(false);
    setTerrainState("OFF");
    setAtmospherePreset("night");
    setLightAzimuth(210);
    setFieldOfView(36);
    setStructures3DEnabled(false);
    setStructures3DState("OFF");
    setGestureMode("cooperative");
    stopSceneOrbit(false);
    setMeasureMode(null);
    setMeasurementGeometryMode(null);
    measureModeRef.current = null;
    measurementGeometryModeRef.current = null;
    measureCoordinatesRef.current = [];
    setMeasureCoordinateCount(0);
    setMeasurement("Select a measurement tool");
    mapRef.current?.doubleClickZoom.enable();
    locationDerivedViewRef.current = false;
    setLocationCameraRedacted(false);
    replayingCameraHistoryRef.current = true;
    cameraHistoryRef.current = [KANSAS_VIEW];
    cameraHistoryIndexRef.current = 0;
    setCameraHistoryIndex(0);
    setCameraHistoryLength(1);
    map?.stop();
    if (map?.isStyleLoaded()) {
      setTerrainState(setTerrainPresentation(map, false, 1));
      setTerrainHeightOverlay(map, false);
      setStructureExtrusions(map, false);
      map.setProjection({ type: "mercator" });
      applySceneEnvironment(map, "night", 210);
      map.setVerticalFieldOfView(36);
      map.triggerRepaint();
      updateMeasurementSource(map, buildMeasurementData([], null));
    }
    map?.jumpTo(KANSAS_VIEW);
    analysisAreaRef.current = null;
    setAnalysisArea(null);
    if (mapRef.current?.isStyleLoaded()) updateAnalysisAreaSource(mapRef.current, null);
    clearSelection();
    setMapQueryCandidates([]);
    setReportTitle("Kansas map data report");
    setReportScope("VIEWPORT");
    setReportDetail("STANDARD");
    setReportLayerIds([...defaultReportLayerIds]);
    setReportSections(defaultReportSections);
    setReportQuery("");
    setReportEvidenceFilter("ALL");
    announce("Explorer reset to the Kansas overview");
  };

  const toggleMeasure = (mode: Exclude<MeasureMode, null>) => {
    setTerrainProfile([]);
    if (measureMode === mode) {
      setMeasureMode(null);
      setMeasurementGeometryMode(null);
      measureModeRef.current = null;
      measurementGeometryModeRef.current = null;
      measureCoordinatesRef.current = [];
      setMeasureCoordinateCount(0);
      setMeasurement("Measurement cancelled");
      mapRef.current?.doubleClickZoom.enable();
      if (mapRef.current?.isStyleLoaded()) updateMeasurementSource(mapRef.current, buildMeasurementData([], null));
      return;
    }
    setMeasureMode(mode);
    setMeasurementGeometryMode(mode);
    measureModeRef.current = mode;
    measurementGeometryModeRef.current = mode;
    measureCoordinatesRef.current = [];
    setMeasureCoordinateCount(0);
    setMeasurement(`Click the map to start measuring ${mode}`);
    setMapQueryCandidates([]);
    const map = mapRef.current;
    if (map) {
      map.doubleClickZoom.disable();
      if (map.isStyleLoaded()) updateMeasurementSource(map, buildMeasurementData([], mode));
    }
  };

  const beginMapMeasurement = (mode: Exclude<MeasureMode, null>) => {
    toggleMeasure(mode);
    if (isCompact) {
      dismissMapUtilityWithoutFocus();
      window.requestAnimationFrame(() => mapContainerRef.current?.focus({ preventScroll: true }));
    }
  };

  const undoMeasurementPoint = () => {
    const mode = measurementGeometryModeRef.current;
    if (!mode || measureCoordinatesRef.current.length === 0) {
      announce("No measurement point to undo");
      return;
    }
    measureCoordinatesRef.current = measureCoordinatesRef.current.slice(0, -1);
    setMeasureCoordinateCount(measureCoordinatesRef.current.length);
    if (!measureModeRef.current) {
      measureModeRef.current = mode;
      setMeasureMode(mode);
      mapRef.current?.doubleClickZoom.disable();
    }
    if (mapRef.current?.isStyleLoaded()) updateMeasurementSource(mapRef.current, buildMeasurementData(measureCoordinatesRef.current, mode));
    setMeasurement(measureCoordinatesRef.current.length ? measurementLabelFor(mode, measureCoordinatesRef.current, measureUnitRef.current) : `Click the map to start measuring ${mode}`);
  };

  const finishMeasurement = () => {
    const mode = measurementGeometryModeRef.current;
    if (!mode) return;
    const minimum = mode === "point" ? 1 : mode === "distance" ? 2 : 3;
    if (measureCoordinatesRef.current.length < minimum) {
      announce(`Add ${minimum - measureCoordinatesRef.current.length} more point${minimum - measureCoordinatesRef.current.length === 1 ? "" : "s"} before finishing`);
      return;
    }
    measureModeRef.current = null;
    setMeasureMode(null);
    mapRef.current?.doubleClickZoom.enable();
    setMeasurement(`Complete · ${measurementLabelFor(mode, measureCoordinatesRef.current, measureUnitRef.current)}`);
    announce("Screen measurement finished locally; it is not survey or evidence");
  };

  const clearMeasurement = () => {
    measureModeRef.current = null;
    measurementGeometryModeRef.current = null;
    measureCoordinatesRef.current = [];
    setMeasureCoordinateCount(0);
    setMeasureMode(null);
    setMeasurementGeometryMode(null);
    setMeasurement("Select a measurement tool");
    setTerrainProfile([]);
    mapRef.current?.doubleClickZoom.enable();
    if (mapRef.current?.isStyleLoaded()) updateMeasurementSource(mapRef.current, buildMeasurementData([], null));
    announce("Screen measurement cleared");
  };

  const changeMeasureUnit = (unit: MeasureUnit) => {
    measureUnitRef.current = unit;
    setMeasureUnit(unit);
    scaleControlRef.current?.setUnit(unit);
    const mode = measurementGeometryModeRef.current;
    if (mode && measureCoordinatesRef.current.length) {
      const prefix = measureModeRef.current ? "" : "Complete · ";
      setMeasurement(`${prefix}${measurementLabelFor(mode, measureCoordinatesRef.current, unit)}`);
    }
  };

  const shareView = async () => {
    const params = buildExplorerParams();
    const sharePath = `${window.location.pathname}?${params.toString()}`;
    const shareUrl = `${window.location.origin}${sharePath}`;
    const historyUpdated = replaceExplorerHistory(sharePath);
    try {
      await navigator.clipboard.writeText(shareUrl);
      announce(locationDerivedViewRef.current
        ? "Share link copied with the location-derived camera redacted"
        : `Share link copied with camera, layer order, opacity, time, projection, evidence state${analysisArea ? ", and analysis area" : ""}`);
    } catch {
      announce(historyUpdated ? "Share state is in the address bar and ready to copy" : "Share link could not be copied; open the Site in a browser and try again");
    }
  };

  const copyMapContextReceipt = async () => {
    const issuedAt = new Date();
    const receipt = {
      format: "kfm-map-context-receipt-v1",
      authority: "SITE_LOCAL_DEMONSTRATION",
      issued_at: issuedAt.toISOString(),
      expires_at: new Date(issuedAt.getTime() + 15 * 60 * 1000).toISOString(),
      context_is_evidence: false,
      renderer: { family: "MapLibre GL JS", site_package: "6.9.0", repository_runtime_proven: false },
      camera: locationDerivedViewRef.current
        ? { center: "WITHHELD_BROWSER_LOCATION", zoom: "WITHHELD", bearing: "WITHHELD", pitch: "WITHHELD", projection }
        : { center: view.center, zoom: view.zoom, bearing: view.bearing, pitch: view.pitch, projection },
      display: { basemap, active_time: year, evidence_filter: mapEvidenceFilter, visible_layer_ids: activeLayers.map((layer) => layer.id), scene: scenePreset, atmosphere: atmospherePreset, light_azimuth: lightAzimuth, field_of_view: fieldOfView, gesture_mode: gestureMode },
      analysis_area: locationDerivedViewRef.current || !analysisArea
        ? null
        : { bounds: analysisArea, compatible_record_count: analysisAreaRecordCount, role: "SITE_LOCAL_CONTEXT_ONLY" },
      workspace: currentWorkspace,
      selection: selected ? {
        kind: selected.kind,
        feature_id: selected.featureId,
        layer_id: selected.layerId,
        layer_visible: !selectedLayerHidden,
        time_compatible: !selectedTimeMismatch,
        evidence_filter_compatible: !selectedEvidenceFiltered,
        evidence_ref: selected.properties.citation,
        evidence_state: selected.properties.evidenceState,
        geometry: "OMITTED_FROM_RECEIPT",
      } : null,
      effects: { evidence: "NONE", policy: "NONE", release: "NONE", publication: "NONE" },
      limitations: ["Hover previews are not claims.", "Attribution and basemap labels are context, not evidence.", "A browser-location-derived camera is redacted from URLs, receipts, shares, exports, and diagnostics."],
    };
    try {
      await navigator.clipboard.writeText(JSON.stringify(receipt, null, 2));
      announce("Map context receipt copied · expires in 15 minutes");
    } catch {
      announce("Clipboard access was blocked; map context stayed in the browser");
    }
  };

  const copyMapDiagnostics = async () => {
    const diagnostics = {
      format: "kfm-map-diagnostics-v1",
      authority: "SITE_LOCAL_REDACTED_DIAGNOSTIC",
      generated_at: new Date().toISOString(),
      site_renderer: { family: "MapLibre GL JS", package: maplibreProbe.version ?? EXPECTED_MAPLIBRE_VERSION, runtime_state: runtime.kind, message_class: runtime.kind.toUpperCase() },
      runtime_proof: {
        expected_version: EXPECTED_MAPLIBRE_VERSION,
        worker: maplibreProbe.workerConfigured ? "SAME_ORIGIN_CONFIGURED" : "NOT_CONFIRMED",
        runtime_assets: maplibreProbe.runtimeAssetsReady ? "WORKER_AND_SHARED_VERIFIED" : "NOT_CONFIRMED",
        webgl2: maplibreProbe.webgl2,
        map_constructed: maplibreProbe.mapConstructed,
        canvas_ready: maplibreProbe.canvasReady,
        style_loaded: maplibreProbe.styleLoaded,
        idle: maplibreProbe.idle,
        tiles_loaded: maplibreProbe.tilesLoaded,
        sources_ready: `${maplibreProbe.sourcesReady}/${LAYER_REGISTRY.length}`,
        controls_ready: maplibreProbe.controlsReady,
        interactions_ready: maplibreProbe.interactionsReady,
        projection: maplibreProbe.projection,
        error_class: maplibreProbe.error ? "FINITE_MAP_RUNTIME_ERROR" : null,
        failed_checks: maplibreProbe.failedChecks,
      },
      repository_boundary: {
        snapshot: REPOSITORY_SNAPSHOT.commit,
        architecture: "ACCEPTED",
        dependency: "EXACT_6.9.0",
        runtime: "BOUNDED_PACKAGE_OWNED_ADAPTER_SLICE",
        broader_production_activation: "HOLD",
      },
      camera: { zoom: Number(view.zoom.toFixed(2)), bearing: Math.round(view.bearing), pitch: Math.round(view.pitch), projection },
      style: { basemap, style_loaded: mapRef.current?.isStyleLoaded() ?? false, atmosphere: atmospherePreset, light_azimuth: lightAzimuth, field_of_view: fieldOfView },
      registry: { sources: LAYER_REGISTRY.length, renderers: interactiveLayerIds.length, visible_layers: visibleCount, source_states: sourceStates },
      source_connections: { activity: sourceActivity, probe_counts: sourceProbeCounts },
      active_time: year,
      workspace: currentWorkspace,
      selection: selected ? { kind: selected.kind, feature_id: selected.featureId, layer_id: selected.layerId, layer_visible: !selectedLayerHidden, time_compatible: !selectedTimeMismatch } : null,
      analysis_area: { active: Boolean(analysisArea), compatible_record_count: analysisAreaRecordCount, coordinates: "OMITTED_FROM_REDACTED_DIAGNOSTIC" },
      redaction: "No raw coordinates, source URLs, tokens, stacks, prompts, private payloads, or browser location included.",
      public_effect: "NONE",
    };
    try {
      await navigator.clipboard.writeText(JSON.stringify(diagnostics, null, 2));
      announce("Redacted MapLibre diagnostics copied with no public effect");
    } catch {
      announce("Clipboard access was blocked; diagnostics stayed in the browser");
    }
  };

  const copySourceIntakeDraft = async (source: (typeof SOURCE_CANDIDATES)[number]) => {
    const intakeDraft = {
      format: "kfm-source-intake-draft-v1",
      disposition: "PROPOSED_WORK_RECORD",
      publicEffect: "NONE",
      candidate: {
        id: source.id,
        title: source.title,
        organization: source.organization,
        domain: source.domain,
        cadence: source.cadence,
        sourceRole: source.sourceRole,
        admissionState: SOURCE_ADMISSION_BY_ID[source.id] ?? "candidate",
        dataModes: source.dataModes,
        officialPortal: source.sourceUrl,
        portalCheckedAt: source.checkedAt,
      },
      proposedValue: source.value,
      cannotProve: source.cannotProve,
      nextGate: source.nextGate,
      requiredBeforeAdmission: ["stable version identity", "rights and attribution", "sensitivity review", "fitness and materiality", "negative fixtures", "accountable disposition"],
      boundary: "Discovery, copying, or repository presence does not admit, release, activate, or publish this source.",
    };
    try {
      await navigator.clipboard.writeText(JSON.stringify(intakeDraft, null, 2));
      announce(`${source.title} intake draft copied with no public effect`);
    } catch {
      announce("Clipboard access was unavailable; the candidate remains visible in the observatory");
    }
  };

  const copyFunctionHandoff = async (record: FunctionRecord) => {
    const handoff = {
      format: "kfm-function-handoff-v1",
      disposition: "SITE_LOCAL_NO_EFFECT_HANDOFF",
      repository: `${REPOSITORY_SNAPSHOT.repository}@${REPOSITORY_SNAPSHOT.commit}`,
      function: { id: record.id, title: record.title, group: record.group, authority: record.authority, maturity: record.maturity, interface: record.interface },
      currentContext: { workspace: currentWorkspace, activeYear: year, selectedFeatureId: selected?.featureId ?? null, selectedLayerId: selected?.layerId ?? null },
      requiredClosure: record.requires,
      boundary: record.boundary,
      source: { label: record.sourceLabel, path: record.sourcePath ?? "DRIVE_WORKING_REFERENCE" },
      permittedNextStep: "Review this bounded handoff against the exact owning contract, authority, and current repository evidence.",
      effects: { sourceAdmission: "NONE", evidence: "NONE", policy: "NONE", review: "NONE", release: "NONE", deployment: "NONE", promotion: "NONE", publication: "NONE" },
    };
    try {
      await navigator.clipboard.writeText(JSON.stringify(handoff, null, 2));
      announce(`${record.title} handoff copied with no operational effect`);
    } catch {
      announce("Clipboard access was blocked; no operational action ran");
    }
  };

  const launchFunction = (record: FunctionRecord) => {
    if (record.action === "COPY_HANDOFF") {
      void copyFunctionHandoff(record);
      return;
    }
    if (record.action === "NONE") {
      announce(`${record.title} remains gated: ${record.requires.join(" · ")}`);
      return;
    }
    if (record.action === "OPEN_SOURCES") {
      setRepositoryView("sources");
      announce("Opened source discovery; no source was admitted");
      return;
    }
    setRepositoryOpen(false);
    if (record.action === "OPEN_MAP") {
      activatePublicWorkspace("explore");
      return;
    }
    if (record.action === "OPEN_LAYERS") {
      activatePublicWorkspace("knowledge");
      return;
    }
    if (record.action === "OPEN_TIMELINE") {
      setCurrentWorkspace("explore");
      setMapUtilityOpen(false);
      setLeftOpen(false);
      setRightOpen(false);
      setTimelineOpen(true);
      announce("Opened the bounded demonstration timeline");
      return;
    }
    if (record.action === "OPEN_EXPORT") {
      openMapUtility("export");
      announce("Opened trust-aware Export Review");
      return;
    }
    if (record.action === "OPEN_DIAGNOSTICS") {
      openMapUtility("diagnostics");
      announce("Opened redacted MapLibre and runtime-seam diagnostics");
      return;
    }
    if (!selected) {
      openMapUtility("inspect");
      announce(`Select a feature before opening ${record.title}`);
      return;
    }
    setMapUtilityOpen(false);
    setLeftOpen(false);
    setTimelineOpen(false);
    setRightOpen(true);
    setCurrentWorkspace("trust");
    activateDrawerView(record.action === "OPEN_FOCUS" ? "focus" : "evidence", true);
    announce(`Opened ${record.title} for ${selected.properties.title}`);
  };

  const buildCustomReportPayload = (generatedAt: string) => {
    // The ref is immediate: exports must be private even before the GPS state
    // update renders. Bounds and point labels can reconstruct a withheld center.
    const redactReportLocation = locationCameraRedacted || locationDerivedViewRef.current;
    const providerSelection = selected?.kind === "basemap" ? buildProviderReportSelection({
      selected, timeMismatch: selectedTimeMismatch,
      locationPrivate: redactReportLocation || researchLocationRedacted || subsurfacePrivate,
      source: selectedOfficialConnection?.source, attributes: selectedArtifactAttributes, attributesCurrent: selectedAttributesCurrent,
      sourceState: selectedRiverObservation?.status ?? selectedOfficialConnection?.state, sourceUrl: selectedRiverObservation?.sourceUrl,
      observedAt: selectedRiverObservation?.observedAt, providerUpdatedAt: selectedOfficialPayload?.upstreamUpdatedAt,
      retrievedAt: selectedRiverObservation?.retrievedAt ?? selectedOfficialConnection?.retrievedAt,
      limitation: selectedOfficialPayload?.limitation ?? selectedOfficialConnection?.limitation,
    }) : null;
    const recordLimit = reportDetail === "EXECUTIVE" ? 8 : reportDetail === "STANDARD" ? 30 : reportRecords.length;
    const heightOverlayRendered = scenePreset === "elevation-3d" && terrainState === "READY"
      && attachedTerrainProviderRef.current === terrainProvider && topographicOverlay;
    const records = reportRecords.slice(0, recordLimit).map(({ layer, properties }) => ({
      id: properties.fid,
      title: properties.title,
      layer: layer.title,
      domain: layer.domain,
      year: properties.year,
      summary: properties.summary,
      evidenceState: properties.evidenceState,
      evidenceReference: properties.citation,
      sourceRole: properties.sourceRole,
      sourceOrganization: properties.sourceOrganization,
      freshness: properties.freshnessState,
      reviewState: properties.reviewState,
      releaseState: properties.releaseState,
      uncertainty: properties.uncertainty,
      generalization: properties.generalizationNote,
    }));
    return {
      format: "kfm-custom-map-report-v1",
      title: providerSelection?.status === "WITHHELD" ? "Withheld source-context report" : reportTitle.trim() || "Kansas map data report",
      generatedAt,
      detail: reportDetail,
      scope: reportScope,
      filters: { query: providerSelection?.status === "WITHHELD" ? null : reportQuery || null, mapEvidenceState: mapEvidenceFilter, evidenceState: reportEvidenceFilter, layerIds: reportLayerIds },
      activeTime: {
        value: temporalQuery.frame,
        label: temporalScopeLabel,
        mode: temporalMode,
        start: temporalMode === "moving-window" ? temporalQuery.windowStart : temporalMode === "accumulation" ? temporalQuery.rangeStart : temporalQuery.frame,
        end: temporalQuery.frame,
        interpolation: "OFF",
      },
      temporalComparison: reportTemporalComparison,
      mapContext: {
        center: redactReportLocation ? "WITHHELD_BROWSER_LOCATION" : view.center,
        camera: redactReportLocation
          ? { zoom: "WITHHELD", bearing: "WITHHELD", pitch: "WITHHELD" }
          : { zoom: view.zoom, bearing: view.bearing, pitch: view.pitch },
        representation: mapRepresentationLabel,
        scene: scenePreset,
        terrain: {
          state: terrainState,
          exaggeration: verticalExaggeration,
          sourceRole: "external DEM display context · not evidence",
          heightOverlay: {
            enabled: heightOverlayRendered,
            method: "MapLibre color-relief from the active raster-dem; cursor and locked readings query unexaggerated terrain elevation.",
            colorRampMeters: [200, 300, 400, 500, 650, 800, 1000, 1250],
            lockedReading: lockedTerrainElevation ? {
              elevationMeters: lockedTerrainElevation.meters,
              elevationFeet: lockedTerrainElevation.feet,
              provider: lockedTerrainElevation.provider,
              coordinate: redactReportLocation ? "WITHHELD_BROWSER_LOCATION" : [lockedTerrainElevation.longitude, lockedTerrainElevation.latitude],
            } : null,
          },
        },
        projection,
        basemap,
        viewport: reportScope === "VIEWPORT" ? redactReportLocation ? "WITHHELD_BROWSER_LOCATION" : mapViewportBounds : null,
        analysisArea: reportScope === "ANALYSIS_AREA" ? redactReportLocation ? "WITHHELD_BROWSER_LOCATION" : analysisArea : null,
      },
      measurements: measurementGeometryMode ? {
        mode: measurementGeometryMode,
        unit: measureUnit,
        label: redactReportLocation ? "WITHHELD_BROWSER_LOCATION" : measurement,
        coordinates: redactReportLocation ? "WITHHELD_BROWSER_LOCATION" : measureCoordinatesRef.current.map(([longitude, latitude]) => [longitude, latitude] as [number, number]),
        approximation: "Browser-local screen measurement; not survey-grade or evidence.",
      } : null,
      selection: providerSelection ?? (selected?.kind === "registry" && !selectedTimeMismatch ? { id: selected.featureId, kind: selected.kind, title: selected.properties.title, layer: selected.layer.title, evidenceState: selected.properties.evidenceState, evidenceReference: selected.properties.citation, timeCompatible: true } : null),
      summary: reportSections.summary ? {
        matchedRecords: reportRecords.length,
        includedRecords: records.length,
        includedLayers: reportLayerSummary.length,
        evidenceStates: reportEvidenceCounts,
      } : null,
      findings: reportSections.findings ? reportRecords.length === 0
        ? emptyReportFindings(providerSelection?.status ?? null, LAYER_REGISTRY.length === 0)
        : reportFindings : null,
      layers: reportLayerSummary,
      records: reportSections.records ? records : null,
      evidenceNotes: reportSections.evidence ? records.map((record) => ({
        id: record.id,
        state: record.evidenceState,
        reference: record.evidenceReference,
        sourceRole: record.sourceRole,
        sourceOrganization: record.sourceOrganization,
        freshness: record.freshness,
        reviewState: record.reviewState,
        releaseState: record.releaseState,
      })) : null,
      limitations: reportSections.limitations ? [
        "No KFM domain records are released in this Site. Provider-backed map context retains its own source, time, and limitations.",
        "Map display, proximity, overlap, and screen measurement are not evidence or proof of a relationship.",
        "Any included measurement is a browser-local report input and remains approximate, not survey-grade.",
        "Basemap and terrain services are display context; their geometry and elevation values are not KFM evidence or source admission.",
        "Protected geometry is not reconstructed; location-derived camera coordinates remain withheld.",
        ...Array.from(new Set(records.map((record) => `${record.title}: ${record.generalization} ${record.uncertainty}`))),
      ] : null,
      attribution: [
        ...reportLayerSummary.map((layer) => ({ layer: layer.title, source: layer.attribution })),
        ...(heightOverlayRendered ? [{ layer: "Topographic height overlay", source: terrainSourceFor(terrainProvider).attribution }] : []),
      ],
    };
  };

  const copyCustomReport = async () => {
    const generatedAt = new Date().toISOString();
    const report = buildCustomReportPayload(generatedAt);
    setReportGeneratedAt(generatedAt);
    try {
      await navigator.clipboard.writeText(JSON.stringify(report, null, 2));
      announce(`Custom report copied with ${reportRecords.length} matching records`);
    } catch {
      announce("Clipboard access was blocked; the report preview stayed in the browser");
    }
  };

  const downloadCustomReport = (format: "html" | "json") => {
    const generatedAt = new Date().toISOString();
    const report = buildCustomReportPayload(generatedAt);
    setReportGeneratedAt(generatedAt);
    const safeName = (report.title || "kansas-map-report").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "").slice(0, 60) || "kansas-map-report";
    let content: string;
    let mime: string;
    if (format === "json") {
      content = JSON.stringify(report, null, 2);
      mime = "application/json";
    } else {
      const records = report.records ?? [];
      const findings = report.findings ?? [];
      const limitations = report.limitations ?? [];
      const heightOverlay = report.mapContext.terrain.heightOverlay;
      const lockedHeight = heightOverlay.lockedReading;
      const heightSection = heightOverlay.enabled
        ? `<section><h2>Terrain height overlay</h2><p><strong>Color relief:</strong> active, based on unexaggerated DEM elevation.</p>${lockedHeight ? `<p><strong>Locked reading:</strong> ${escapeReportHtml(lockedHeight.elevationFeet.toFixed(0))} ft / ${escapeReportHtml(lockedHeight.elevationMeters.toFixed(0))} m · ${lockedHeight.provider === "usgs-3dep" ? "USGS 3DEP" : "Mapzen"} display DEM</p>` : "<p>No cursor elevation was locked for this report.</p>"}<p class="boundary">External display DEM. Confirm vertical datum, product version, and survey requirements before using this value as authoritative evidence.</p></section>`
        : "";
      content = `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${escapeReportHtml(report.title)}</title><style>body{font:15px/1.55 Inter,system-ui,sans-serif;color:#17201d;max-width:1100px;margin:0 auto;padding:48px}header{border-bottom:3px solid #b88b38;padding-bottom:22px;margin-bottom:28px}h1{font-size:36px;letter-spacing:-.04em;margin:0 0 8px}h2{margin-top:34px}small,.muted{color:#607069}.metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}.metric{border:1px solid #ccd6d1;padding:15px}.metric strong{display:block;font-size:24px}table{width:100%;border-collapse:collapse;font-size:13px}th,td{border-bottom:1px solid #dce3df;padding:10px;text-align:left;vertical-align:top}th{background:#f1f5f2}code{font-size:11px}li{margin:8px 0}.boundary{border-left:4px solid #b88b38;background:#f7f3ea;padding:14px 18px}@media print{body{padding:0}.boundary{break-inside:avoid}}@media(max-width:700px){body{padding:24px}.metrics{grid-template-columns:1fr 1fr}table{display:block;overflow:auto}}</style></head><body><header><small>KANSAS FRONTIER MATRIX · CUSTOM MAP REPORT</small><h1>${escapeReportHtml(report.title)}</h1><p>${escapeReportHtml(report.scope.replaceAll("_", " "))} · active time ${escapeReportHtml(report.activeTime.label)} · generated ${escapeReportHtml(generatedAt)}</p></header>${report.summary ? `<section><h2>Report summary</h2><div class="metrics"><div class="metric"><small>MATCHED KFM RECORDS</small><strong>${report.summary.matchedRecords}</strong></div><div class="metric"><small>INCLUDED KFM RECORDS</small><strong>${report.summary.includedRecords}</strong></div><div class="metric"><small>KFM LAYERS</small><strong>${report.summary.includedLayers}</strong></div><div class="metric"><small>EVIDENCE STATES</small><strong>${Object.keys(report.summary.evidenceStates).length}</strong></div></div></section>` : ""}${findings.length ? `<section><h2>Findings</h2><ol>${findings.map((finding) => `<li>${escapeReportHtml(finding)}</li>`).join("")}</ol></section>` : ""}<section><h2>Time A / Time B catalog availability</h2><div class="metrics"><div class="metric"><small>TIME A</small><strong>${escapeReportHtml(formatTimelineStep(report.temporalComparison.timeA))}</strong><span>${report.temporalComparison.timeARecordCount} records</span></div><div class="metric"><small>TIME B</small><strong>${escapeReportHtml(formatTimelineStep(report.temporalComparison.timeB))}</strong><span>${report.temporalComparison.timeBRecordCount} records</span></div><div class="metric"><small>DELTA</small><strong>${report.temporalComparison.recordDelta >= 0 ? "+" : ""}${report.temporalComparison.recordDelta}</strong><span>catalog records</span></div><div class="metric"><small>CHANGED LAYERS</small><strong>${report.temporalComparison.changedLayerCount}</strong><span>under temporal rules</span></div></div><p class="boundary">Catalog availability only—not observed change, imagery analysis, causation, or proof of an event.</p></section>${records.length ? `<section><h2>Included records</h2><table><thead><tr><th>Record</th><th>Layer / time</th><th>Evidence</th><th>Summary</th></tr></thead><tbody>${records.map((record) => `<tr><td><strong>${escapeReportHtml(record.title)}</strong><br><code>${escapeReportHtml(record.id)}</code></td><td>${escapeReportHtml(record.layer)}<br>${escapeReportHtml(record.year)}</td><td>${escapeReportHtml(record.evidenceState)}<br><code>${escapeReportHtml(record.evidenceReference)}</code></td><td>${escapeReportHtml(record.summary)}</td></tr>`).join("")}</tbody></table></section>` : ""}${limitations.length ? `<section><h2>Limitations</h2><ul>${limitations.map((limitation) => `<li>${escapeReportHtml(limitation)}</li>`).join("")}</ul></section>` : ""}<section><h2>Attribution</h2><ul>${report.attribution.map((item) => `<li><strong>${escapeReportHtml(item.layer)}:</strong> ${escapeReportHtml(item.source)}</li>`).join("")}</ul></section><p class="boundary">This report is a browser-generated public-safe demonstration artifact. It does not release, publish, admit, or authorize KFM data.</p></body></html>`;
      if (heightSection) content = content.replace("<section><h2>Time A / Time B", `${heightSection}<section><h2>Time A / Time B`);
      content = content.replace("</header>", () => `</header>${providerReportHtml(report.selection)}`);
      mime = "text/html";
    }
    const url = URL.createObjectURL(new Blob([content], { type: mime }));
    const link = document.createElement("a");
    link.href = url;
    link.download = `${safeName}.${format}`;
    document.body.append(link);
    link.click();
    link.remove();
    window.setTimeout(() => URL.revokeObjectURL(url), 0);
    announce(`${format.toUpperCase()} report downloaded with ${reportRecords.length} matching records`);
  };

  const copyExportManifest = async () => {
    const review = buildExportReview(new Date().toISOString());
    setExportGeneratedAt(review.payload.exportedAt);
    try {
      await navigator.clipboard.writeText(JSON.stringify(review.payload, null, 2));
      announce("Public-safe export manifest copied after redaction review");
    } catch {
      announce("Clipboard access was blocked; export context stayed in the browser");
    }
  };

  const downloadPublicSafeExport = () => {
    const review = buildExportReview(new Date().toISOString());
    setExportGeneratedAt(review.payload.exportedAt);
    if (!review.downloadAllowed) {
      announce("Export is blocked until every visible layer carries attribution");
      return;
    }
    const url = URL.createObjectURL(new Blob([JSON.stringify(review.payload, null, 2)], { type: "application/json" }));
    const link = document.createElement("a");
    link.href = url;
    link.download = review.filename;
    document.body.append(link);
    link.click();
    link.remove();
    window.setTimeout(() => URL.revokeObjectURL(url), 0);
    announce(review.withheldFeatureCount
      ? "Public-safe export downloaded with protected geometry withheld"
      : "Public-safe export downloaded with attribution and trust metadata");
  };

  const initializeRuntimeSeam = () => {
    setRuntimeSeamState("READY");
    setRuntimeSeamReason("Deterministic NullMapRuntime initialized with no network or renderer dependency");
    announce("Renderer-neutral runtime seam initialized locally");
  };

  const bindRuntimeSeamSelection = () => {
    if (runtimeSeamState === "IDLE" || runtimeSeamState === "DISPOSED") {
      announce("Initialize the renderer-neutral seam before binding a selection");
      return;
    }
    const step = runtimeSeamStepForSelection(selected?.properties.evidenceState ?? null);
    setRuntimeSeamState(step.state);
    setRuntimeSeamReason(`${step.reason} · ${step.effect}`);
    announce(`Runtime seam resolved ${step.state}`);
  };

  const disposeRuntimeSeam = () => {
    setRuntimeSeamState("DISPOSED");
    setRuntimeSeamReason("Subscriptions cleared; repeated disposal remains a no-op");
    announce("Renderer-neutral runtime seam disposed locally");
  };

  const locateUser = () => {
    if (!navigator.geolocation) { announce("Geolocation is not available in this browser"); return; }
    navigator.geolocation.getCurrentPosition(
      ({ coords }) => {
        if (coords.longitude < SUPPORTED_CONTEXT_BOUNDS.west || coords.longitude > SUPPORTED_CONTEXT_BOUNDS.east || coords.latitude < SUPPORTED_CONTEXT_BOUNDS.south || coords.latitude > SUPPORTED_CONTEXT_BOUNDS.north) {
          announce("Browser location is outside the Explorer's supported Kansas context extent");
          return;
        }
        locationDerivedViewRef.current = true;
        setLocationCameraRedacted(true);
        mapRef.current?.easeTo({ center: [coords.longitude, coords.latitude], zoom: 10, duration: window.matchMedia("(prefers-reduced-motion: reduce)").matches ? 0 : 650 });
        announce("Map centered locally; the location-derived camera is redacted from URLs, shares, receipts, exports, and diagnostics");
      },
      () => announce("Location permission was unavailable or denied"),
      { enableHighAccuracy: false, timeout: 7000 },
    );
  };

  const toggleFullscreen = async () => {
    const shell = document.querySelector<HTMLElement>(".explorer-shell");
    if (!shell) return;
    try {
      if (document.fullscreenElement) await document.exitFullscreen(); else await shell.requestFullscreen();
    } catch {
      announce("Fullscreen is unavailable in this browser context");
    }
  };

  const calendarSourceRows: CalendarSourceRow[] = visibleOfficialSources.map(source => {
    const day = calendarSweep ? calendarFrameDay(calendarSweep) : null;
    const feed = source.id as CalendarArchiveFeed;
    const supported = Object.hasOwn(CALENDAR_ARCHIVE_BOUNDS, feed);
    const checkedDay = supported ? officialArchiveDays[feed] : undefined;
    const payload = supported ? officialArchivePayloadsRef.current[feed] : undefined;
    const matched = Boolean(day && checkedDay === day && payload);
    return { id: source.id, title: source.shortTitle,
      state: day && supported ? day < CALENDAR_ARCHIVE_BOUNDS[feed] ? "outside bounds" : checkedDay !== day ? "unchecked" : officialStates[source.id] : day && !effectiveOfficialVisibility[source.id] ? "held" : supported ? "independent" : "separate clock",
      detail: supported ? matched ? day + " UTC · " + payload!.featureCount + " source records · retrieved " + payload!.retrievedAt + (payload!.truncated ? " · truncated" : "") : "Exact day adapter · earliest query " + CALENDAR_ARCHIVE_BOUNDS[feed] + "; coverage is checked per request." : OFFICIAL_CONTEXT_TEMPORAL_SUPPORT[source.id].limitation,
    };
  });

  const fireImageDay = officialPayloads["nasa-gibs-fire-points"]?.sourceDay;
  const daylightDisplayTime = formatKansasSolarTime(daylightInstant);
  const daylightInterval = kansasLocalDateRangeInterval(daylightDay, daylightThroughDay);
  const daylightDurationHours = Math.round(daylightInterval.durationMs / 3_600_000);
  const daylightDayCount = kansasCalendarDaysInclusive(daylightDay, daylightThroughDay);
  const daylightToday = currentKansasCalendarDay();
  const daylightSliderValue = Math.round(intervalFractionAtInstant(daylightInstant, daylightInterval) * 10_000);
  const daylightRangeSummary = daylightDayCount === 1
    ? `Full local day · ${daylightDurationHours} hours · 60-second loop`
    : `${daylightDayCount.toLocaleString("en-US")} local days · 60-second loop per day`;
  const sourceIssues = OFFICIAL_CONTEXT_SOURCES.filter((source) =>
    officialVisibility[source.id] && (officialStates[source.id] === "error"
      || (officialStates[source.id] === "partial" && officialRasterFailuresRef.current.has(source.id))
      || (source.id === "nasa-gibs-fire-points" && officialStates[source.id] === "partial" && Boolean(fireImageDay && fireImageDay < currentUtcDay()))),
  ).map((source) => ({
    id: source.id,
    title: source.shortTitle,
    downloadHref: sourceDownloadHref(source.id, officialArchiveDays[source.id as OfficialContextFeedId]),
    detail: source.id === "nasa-gibs-fire-points" && officialStates[source.id] !== "error"
      ? `Showing NASA image day ${fireImageDay} UTC. Newer observations were unavailable at the last check; refresh to try again.`
      : officialStates[source.id] === "partial" && officialRasterFailuresRef.current.has(source.id)
        ? "Some display tiles did not load. The visible tiles remain source imagery; retry to check the missing area."
      : officialArchiveDays[source.id as OfficialContextFeedId]
        ? `Selected archive day ${officialArchiveDays[source.id as OfficialContextFeedId]} UTC could not load. Other layers remain available.`
        : undefined,
  }));

  const liveObservationSwitcher = availableLiveInstruments.length > 1 ? <nav className="live-observation-switcher" aria-label="Observation controls">
    {availableLiveInstruments.map((instrument) => <button key={instrument} type="button" aria-pressed={activeLiveInstrument === instrument} onClick={() => {
      setLiveInstrument(instrument);
      if (instrument !== "river") setStreamflowPlaying(false);
      if (instrument !== "radar") setNoaaRadarPlaying(false);
      if (instrument !== "lightning") setLightningPlaying(false);
    }}>{instrument === "river" ? "River Pulse" : instrument === "radar" ? "Radar Loop" : "Lightning"}</button>)}
  </nav> : null;

  // Radar on, then its live loop controls on the map.
  const watchRadarLoop = () => { setOfficialContextVisible("nws-radar", true); setLiveInstrument("radar"); setInstrumentOpen(true); };

  const toggleUnderground = () => { const open = primaryWorkspace !== "map" || !undergroundOpen; if (open) activateMapRepresentation("2d"); setUndergroundOpen(open); setPlaying(false); setSubsurfacePrivate(v => v || locationCameraRedacted || locationDerivedViewRef.current); setTimelineOpen(false); setLeftOpen(false); setRightOpen(false); setMapUtilityOpen(false); };
  const openMapGuideDiagnostics = () => {
    openMapUtility("diagnostics");
    // Re-enter retained controls, or let a newly opening panel paint past its
    // initial visibility transition before focusing after help has unmounted.
    window.requestAnimationFrame(() => window.requestAnimationFrame(() => {
      const panel = mapUtilityPanelRef.current;
      if (panel) visibleFocusableElements(panel)[0]?.focus({ preventScroll: true });
    }));
  };
  const welcomeShowing = guideOpen === true && primaryWorkspace === "map";
  const toggleExplorerGuide = () => {
    if (welcomeShowing) { setWelcomeSourcesOpen((open) => !open); return; }
    setWelcomeSourcesOpen(false); // every welcome opens with the sources hidden
    setPrimaryWorkspace("map");
    setGuideOpen(true);
  };
  // Keep the native provider-credit control in the visible ownership subtree:
  // the welcome strip, native fullscreen map, or ordinary map information host.
  useEffect(() => {
    const container = mapContainerRef.current, host = mapInformationHostRef.current;
    if (!container || !host || !styleReady) return;
    const owner = container.ownerDocument;
    const synchronize = () => {
      const attribution = host.querySelector<HTMLDetailsElement>(".maplibregl-ctrl-attrib")
        ?? container.querySelector<HTMLDetailsElement>(".maplibregl-ctrl-attrib");
      const fullscreen = owner.fullscreenElement
        ?? (owner as Document & { webkitFullscreenElement?: Element | null }).webkitFullscreenElement;
      const position = welcomeShowing ? ".maplibregl-ctrl-bottom-right" : ".maplibregl-ctrl-top-right";
      const destination = welcomeShowing || fullscreen === container || container.classList.contains("maplibregl-pseudo-fullscreen") ? container.querySelector(position) : host;
      if (!attribution || !destination) return;
      destination.appendChild(attribution);
      attribution.open = welcomeShowing;
      attribution.classList.toggle("maplibregl-compact-show", welcomeShowing);
    };
    owner.addEventListener("fullscreenchange", synchronize);
    owner.addEventListener("webkitfullscreenchange", synchronize);
    // The renderer's CSS fallback changes only the map class, without a
    // document fullscreen event. Observe that transition before the next paint.
    let pseudoFullscreen = container.classList.contains("maplibregl-pseudo-fullscreen");
    const pseudoObserver = new MutationObserver(() => {
      const next = container.classList.contains("maplibregl-pseudo-fullscreen");
      if (next === pseudoFullscreen) return;
      pseudoFullscreen = next;
      synchronize();
    });
    pseudoObserver.observe(container, { attributes: true, attributeFilter: ["class"] });
    synchronize();
    return () => {
      owner.removeEventListener("fullscreenchange", synchronize);
      owner.removeEventListener("webkitfullscreenchange", synchronize);
      pseudoObserver.disconnect();
    };
  }, [welcomeShowing, styleReady]);
  const closeExplorerGuide = (rememberDismissal: boolean) => {
    setGuideOpen(false);
    setWelcomeSourcesOpen(false);
    writeExplorerGuideDismissed(rememberDismissal);
    if (document.activeElement?.closest(".explorer-guide")) document.querySelector<HTMLButtonElement>(".guide-trigger")?.focus({ preventScroll: true });
  };
  // Opens Underground (or keeps it open) and moves focus into it.
  const enterUnderground = () => {
    if (primaryWorkspace !== "map" || !undergroundOpen) toggleUnderground();
    setUndergroundFocusRequest((request) => request + 1);
  };
  const runExplorerGuideAction = (action: ExplorerGuideAction) => {
    if (action === "layers") { setSourceStatusOpen(false); setStarterPanelOpen(true); openAtlasPanel("layers"); }
    else if (action === "time") { setPrimaryWorkspace("map"); setTimelineOpen(true); }
    else if (action === "underground") enterUnderground();
    else if (action === "qwen") openQwenCompanion(null);
    if (action === "layers" || action === "time") window.requestAnimationFrame(() => {
      // Guide dismissal restores its trigger synchronously. Enter the destination
      // after the requested panel has committed, including retained open panels.
      const panel = action === "layers" ? leftPanelRef.current : timelineRef.current;
      if (panel) visibleFocusableElements(panel)[0]?.focus({ preventScroll: true });
    });
  };
  const runWelcomeTopic = (topic: LayerWorkspace) => {
    runExplorerGuideAction("layers");
    setStarterPanelOpen(false);
    setLayerCatalogView("official");
    setOfficialWorkspace(topic);
  };
  // A category opens on its own map look: basemap, renderer, camera and a few
  // starter context layers. The Layers catalogue follows the same category, and
  // the category starter set replaces the previous category's official layers.
  // A look's light sets only atmosphere and sun azimuth; the visitor's effect settings stay as they are.
  // It is applied to the map now as well as to state: when state already holds these values (the
  // same look opened again), React skips the light effect after the representation transaction has
  // repainted its own default, so the map would keep that default while the controls showed the look.
  const applyCategoryLight = (recipe: SceneRecipe) => {
    const { atmosphere, azimuth } = SCENE_RECIPES[recipe];
    changeStudioLight({ atmosphere, azimuth });
    const map = mapRef.current;
    if (!map || !styleGenerationReadyRef.current) return;
    runMapMutation("Category light", () => {
      applySceneEnvironment(map, atmosphere, azimuth);
      if (scenePresetRef.current === "elevation-3d") applyTerrainReliefStyle(map, basemapRef.current === "topo" ? "topographic" : "general", atmosphere, azimuth);
      syncSceneOverlays(map, atmosphere, azimuth, renderEfficientRef.current);
    });
  };
  const openCategoryMap = (topic: TopicId) => {
    const look = categoryMap(topic);
    if (!look) { runWelcomeTopic(topic); return; }
    setUndergroundOpen(false);
    activateMapRepresentation(look.scene);
    basemapRef.current = look.basemap;
    setBasemap(look.basemap);
    if (look.light) applyCategoryLight(look.light);
    photorealHidHillshadeRef.current = false;
    if (look.starters.includes("nws-radar")) {
      setNoaaRadarPlaying(false);
      noaaRadarFollowLatestRef.current = true;
      setNoaaRadarFollowLatest(true);
      noaaRadarRequestedTimeRef.current = null;
      const latest = noaaRadarManifestRef.current?.frames.at(-1);
      if (latest) applyNoaaRadarFrame(latest);
    }
    // The earthquake record belongs to the map that offers it and closes with it; the
    // starters below decide whether the 30-day catalog is on.
    quakeLiveWasOnRef.current = false;
    setQuakeRecordOn(false);
    setQuakeRecordYear(null);
    setQuakeRecordSelected(null);
    setDroughtOn(false);
    setDroughtWeek(null);
    setDroughtCounty(null);
    setOutlookDay(null);
    setOutlookHazard("cat");
    setReportsDay(null);
    setReportSelected(null);
    // Each map opens on its own subject: only its starters are on, as a starter set does.
    for (const source of OFFICIAL_CONTEXT_SOURCES) {
      const on = look.starters.includes(source.id);
      if (on || officialVisibilityRef.current[source.id]) setOfficialContextVisible(source.id, on);
    }
    // Flood forecasts close with their map; the loop above has already set the NWS gauges to this map's starters.
    floodGaugesWereOnRef.current = false;
    setFloodOn(false);
    setFloodLid(null);
    if (look.overlays?.includes("aviation")) setAviationShowRequest(request => request + 1);
    setPopulationPrismsShown(Boolean(look.overlays?.includes("population")));
    // Soil moisture belongs to the maps that offer it; it does not follow into the others.
    if (!look.tools?.includes("soil")) setSoilMapState(current => current.visible ? hideSoilContext(current) : current);
    setStarterPanelOpen(false);
    setLayerCatalogView("official");
    setOfficialWorkspace(topic);
    setCategoryDockTopic(topic);
    setCategoryDockHidden(false);
    const camera: ViewState = { center: [look.camera.center[0], look.camera.center[1]], zoom: look.camera.zoom, bearing: look.camera.bearing, pitch: look.camera.pitch };
    const map = mapRef.current;
    if (map) map.flyTo({ ...camera, duration: motionDuration(1800), essential: false });
    else pendingViewRef.current = camera;
    announce(`${look.name} opened · ${categorySceneLabel(look.scene)} · display context, not evidence`);
  };
  const runWelcomeMap = (topic: TopicId) => openCategoryMap(topic);
  // The dock follows the catalogue's category while its map look is on screen,
  // including after a shared URL restores that basemap.
  const activeCategoryMap = officialWorkspace === "all" ? undefined : categoryMap(officialWorkspace);
  const categoryMode: CategoryScene = projection === "globe" ? "globe" : scenePreset === "elevation-3d" ? "terrain" : "2d";
  // The category map on screen: its look's basemap is on, or it was opened and not left since.
  const categoryMapOnScreen = activeCategoryMap && (activeCategoryMap.basemap === basemap || categoryDockTopic === activeCategoryMap.topic) ? activeCategoryMap : undefined;
  const showCategoryDock = Boolean(categoryMapOnScreen && !categoryDockHidden && guideOpen === false && primaryWorkspace === "map" && !undergroundOpen);
  // Reviewed snapshots from the site database, for the maps that offer them.
  const reviewedSource = categoryMapOnScreen?.tools?.includes("reviewed") ? REVIEWED_SOURCE_BY_TOPIC[categoryMapOnScreen.topic] ?? null : null;
  const reviewed = useReviewedSnapshots(reviewedSource, !reducedMotion);
  const reviewedData = reviewed.on && reviewed.product ? reviewed.product.data : null;
  // A pick that the shown release does not hold (another snapshot, or none) is no selection.
  const reviewedFeature = reviewedPick && reviewedData ? reviewedData.features.find(feature => String(feature.id ?? "") === reviewedPick) ?? null : null;
  const quakePlots = useMemo(() => quakeRecord ? recordPlots(quakeRecord, quakeRecordYear) : null, [quakeRecord, quakeRecordYear]);
  const quakeCounts = useMemo(() => quakeRecord ? annualCounts(quakeRecord).map(entry => ({ ...entry, color: recordYearColor(entry.year, quakeRecord.endYear) })) : null, [quakeRecord]);
  // Keyboard lists for the selections otherwise made only by clicking the map.
  const quakeEventList = useMemo(() => quakeRecord ? recordEventList(quakeRecord, quakeRecordYear) : [], [quakeRecord, quakeRecordYear]);
  const reviewedList = useMemo(() => reviewedData && reviewedSource ? reviewedFeatureList(reviewedSource, reviewedData) : [], [reviewedData, reviewedSource]);
  /** Moves the map to a picked feature without motion when reduced motion is asked for. */
  const easeToPicked = (center: [number, number]) => mapRef.current?.easeTo({ center, zoom: Math.max(mapRef.current.getZoom(), 8), duration: motionDuration(600) });
  useEffect(() => {
    const map = mapRef.current;
    if (!map) return;
    setReviewedSnapshot(map, reviewedData, reviewedFeature ? reviewedPick : null);
    if (styleReady && styleGenerationReadyRef.current) applyOfficialContextState(map, runtimeOfficialVisibility(officialVisibilityRef.current, temporalQueryRef.current.frame, noaaRadarReadyRef.current, noaaRadarFrameTimeRef.current), officialOpacityRef.current, officialPayloadsRef.current);
  }, [reviewedData, reviewedFeature, reviewedPick, styleReady, runtimeOfficialVisibility]);
  const reviewedTime = (value: string | undefined) => value ? new Date(value).toISOString().slice(0, 16).replace("T", " ") + " UTC" : null;
  // The light changes the map in 3D terrain and on category basemaps, whose shaded relief follows it.
  const categorySunAvailable = categoryMode === "terrain" || isCategoryBasemapKey(basemap);
  // Play the day runs only while its controls are on screen: the dock is shown with its sun controls, not on the globe.
  const sunControlsShown = showCategoryDock && categoryMode !== "globe" && categorySunAvailable;
  if (sunPlaying && !sunControlsShown) setSunPlaying(false);
  // Play the day: one quarter-hour step of the sun study at a time, until 11:45 PM.
  useEffect(() => {
    if (!sunPlaying || !sunControlsShown || !sceneEffects.sunSync || reducedMotion) return;
    const timer = window.setTimeout(() => {
      const day = kansasLocalDayInterval(currentKansasCalendarDay(new Date(sunAt)));
      const next = nextSunStep(intervalFractionAtInstant(sunAt, day));
      if (next === null) setSunPlaying(false);
      else setSunStudyAt(instantAtIntervalFraction(day, next));
    }, SUN_PLAY_STEP_MS);
    return () => window.clearTimeout(timer);
  }, [reducedMotion, sceneEffects.sunSync, sunAt, sunControlsShown, sunPlaying]);
  const chooseCategoryMode = (mode: CategoryScene) => {
    activateMapRepresentation(mode);
    // Vector category basemaps survive the globe; raster ones hand over to the standard style there.
    if (activeCategoryMap && (mode !== "globe" || VECTOR_BASEMAPS.has(activeCategoryMap.basemap))) { basemapRef.current = activeCategoryMap.basemap; setBasemap(activeCategoryMap.basemap); }
  };
  const resetCategoryView = () => {
    if (!activeCategoryMap) return;
    const { center, zoom, bearing, pitch } = activeCategoryMap.camera;
    if (activeCategoryMap.light) applyCategoryLight(activeCategoryMap.light);
    mapRef.current?.flyTo({ center: [center[0], center[1]], zoom: categoryMode === "globe" ? Math.min(zoom, 3.2) : zoom, bearing: categoryMode === "2d" ? 0 : bearing, pitch: categoryMode === "terrain" ? Math.max(pitch, 45) : 0, duration: motionDuration(1200), essential: false });
    announce(`${activeCategoryMap.name} view reset`);
  };
  const runWelcomeSearch = (query: string) => {
    setGlobalQuery(query);
    openAtlasComposer("find", query);
  };
  const runWelcomeFeature = (destination: WelcomeFeatureDestination) => {
    setGuideOpen(false);
    if (destination === "sources") openSourceStatus();
    else runWelcomeTopic(destination);
  };
  const chooseMapMenuRepresentation = (mode: "2d" | "terrain" | "globe") => {
    setUndergroundOpen(false);
    if (mapUtilityView === "compare") setMapUtilityOpen(false);
    activateMapRepresentation(mode);
  };
  const explorerHeaderRef = useRef<HTMLElement>(null);
  useEffect(() => {
    if (explorerHeaderRef.current) return installExplorerMenuDismissal(explorerHeaderRef.current);
  }, []);

  const mapRepresentationControls = () => <>
              <button type="button" data-map-panel="underground" aria-label="Underground Logs & sections" title="Underground Logs & sections" aria-pressed={undergroundOpen} data-active={undergroundOpen} onClick={toggleUnderground}><b>Underground</b><span className="sr-only">Logs &amp; sections</span></button>
              <button type="button" aria-pressed={!undergroundOpen && !(mapUtilityOpen && mapUtilityView === "compare") && projection === "mercator" && scenePreset !== "elevation-3d"} data-active={!undergroundOpen && !(mapUtilityOpen && mapUtilityView === "compare") && projection === "mercator" && scenePreset !== "elevation-3d"} onClick={() => chooseMapMenuRepresentation("2d")}><b>2D</b><span>Map</span></button>
              <button type="button" aria-pressed={!undergroundOpen && !(mapUtilityOpen && mapUtilityView === "compare") && scenePreset === "elevation-3d"} data-active={!undergroundOpen && !(mapUtilityOpen && mapUtilityView === "compare") && scenePreset === "elevation-3d"} onClick={() => chooseMapMenuRepresentation("terrain")}><b>Terrain 3D</b><span>{verticalExaggeration.toFixed(1)}×</span></button>
              {scenePreset === "elevation-3d" && <output className="terrain-mode-source" data-state={terrainState.toLowerCase()} aria-live="polite">{terrainProvider === "usgs-3dep" ? "USGS 3DEP" : "Mapzen"} · {terrainState === "READY" && attachedTerrainProviderRef.current === terrainProvider ? "DEM ready" : terrainState === "ERROR" ? "DEM unavailable" : "DEM loading"}{terrainProvider === "mapzen" && terrainState === "READY" && view.zoom > TERRARIUM_RENDER_MAX_ZOOM ? ` · coarse beyond z${TERRARIUM_RENDER_MAX_ZOOM}` : ""}</output>}
              {scenePreset === "elevation-3d" && terrainProvider === "usgs-3dep" && terrainState === "ERROR" && <button className="terrain-mode-action" type="button" onClick={() => chooseTerrainProviderByHand("mapzen")}>Use display DEM</button>}
              {scenePreset === "elevation-3d" && terrainState === "READY" && basemap === "topo" && view.pitch < 56 && <button className="terrain-mode-action" type="button" onClick={() => orientSceneCamera(58, view.bearing)}>Oblique view ↗</button>}
              <button type="button" aria-pressed={!undergroundOpen && !(mapUtilityOpen && mapUtilityView === "compare") && projection === "globe"} data-active={!undergroundOpen && !(mapUtilityOpen && mapUtilityView === "compare") && projection === "globe"} onClick={() => chooseMapMenuRepresentation("globe")}><b>Globe</b><span>◎</span></button>
              <button type="button" data-map-panel="compare" aria-pressed={mapUtilityOpen && mapUtilityView === "compare"} data-active={mapUtilityOpen && mapUtilityView === "compare"} onClick={() => { if (primaryWorkspace === "map" && mapUtilityOpen && mapUtilityView === "compare") closeMapUtility(); else { setUndergroundOpen(false); activateMapRepresentation("compare"); } }}><b>Compare</b><span>A/B</span></button>
  </>;

  return (
    <div className="site-root atlas-studio" data-startup={guideOpen === null ? "pending" : "ready"} data-welcome-sources={welcomeShowing && welcomeSourcesOpen ? "open" : undefined}>
      {guideOpen === null && <div className="explorer-startup-cover" role="status"><span>Opening the atlas…</span></div>}
      <a className="skip-link" href="#map-canvas" onClick={returnToPrimaryMap}>Skip to the map</a>
      <header ref={explorerHeaderRef} className="topbar">
        <div className="brand-lockup">
          <span className="mark" aria-hidden="true">KFM</span>
          <span><strong className="atlas-title">Kansas Frontier Matrix</strong><small className="atlas-subtitle">Atlas Studio · Prairie Field Desk</small></span>
        </div>
        <div className="atlas-scope-strip" aria-label="Current investigation">
          <button type="button" className="atlas-scope-control welcome-header-find" onClick={() => openAtlasComposer("find")} aria-label="Find a county or place" aria-controls="qwen-map-panel" title="Find places, layers and sources · shortcut /"><span className="welcome-find-icon" aria-hidden="true">⌕</span><span className="welcome-find-label">Find a county or place</span></button>
          <button type="button" className="welcome-ai-entry qwen-header-entry" aria-label="Chat with KFM about this map view" title="Chat with KFM · AI assistant" onClick={(event) => qwenOpen ? closeQwenCompanion(event.currentTarget) : openAtlasComposer("explore", undefined, event.currentTarget)} aria-expanded={qwenOpen} aria-controls="qwen-map-panel"><span className="qwen-launch-mark" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" strokeWidth="1.6"><path d="M20 11.5a8 8 0 0 1-8 8H5l-4 3 1.5-6A8 8 0 1 1 20 11.5Z"/><path d="M6.5 9h9M6.5 13h6"/></svg></span><span className="qwen-header-label">Chat<span className="qwen-header-name"> with KFM</span></span></button>
          <span className="welcome-header-context"><strong>{selectedLabel}</strong><br /><small>Map time {temporalScopeLabel} · {selectedMapLayerCount} layers</small></span>
        </div>
          <span className="sr-only" role="status">{sourceIssues.length ? `${sourceIssues.length} selected sources need attention. Open Layers, then Source status for recovery.` : ""}</span>
          <nav className="map-chrome-dock" aria-label="Map view and controls">
          <span className="map-dock-context sr-only" title={`Current area: ${selectedLabel} · ${temporalScopeLabel}`}><strong>{selectedLabel}</strong><small>{temporalScopeLabel}{buildYearCurrent ? "" : " · build out of date"}</small></span>
            <div className="map-dock-actions" role="group" aria-label="Quick map controls">
              <button className="map-dock-action" type="button" aria-pressed={timelineOpen} onClick={toggleTimelinePanel}><strong>Time</strong><b>{formatTimelineStep(year)}</b></button>
              <button className="map-dock-action" type="button" onClick={(event) => openAtlasPanel("layers", event.currentTarget)} aria-pressed={leftOpen && leftPanelMode === "layers"} title={sourceIssues.length ? `${sourceIssues.length} selected sources need attention · open Layers → Source status` : "Open map layers"} data-attention={sourceIssues.length > 0}><span aria-hidden="true">≡</span><strong>Layers</strong><b>{selectedMapLayerCount}</b></button>
        {runtime.kind !== "unsupported" && !undergroundOpen && <ScenePanel toolbar rendering={<><RenderQualityControl value={renderQuality} onChange={chooseRenderQuality} /><label className="effects-ambient"><input type="checkbox" checked={dynamicEffects && !reducedMotion} disabled={reducedMotion} onChange={event => setDynamicEffects(event.target.checked)} /> Ambient motion{reducedMotion ? " · reduced motion" : ""}</label></>} onOpenChange={setScenePanelOpen} readings={sceneReadings} view={sceneView} terrain={{ scale: verticalExaggeration, available: runtime.kind === "ready" && terrainState !== "ERROR", onScale: changeTerrainDepth, onGroundView: exploreGround }} drawing={{ mode: terrainDrawingMode, detail: terrainDrawingDetail, status: terrainDrawingStatus, source: terrainSourceFor(terrainProvider), onMode: chooseTerrainDrawingMode, onDetail: chooseTerrainDrawingDetail }} surface={{ mode: terrainSurfaceMode, opacity: terrainSurfaceOpacity, probe: terrainSurfaceProbe, probeEnabled: !measureMode, onMode: chooseTerrainSurfaceMode, onOpacity: chooseTerrainSurfaceOpacity, onProbeCenter: sampleTerrainSurfaceCenter }} exploration={{ orbiting: sceneOrbiting, onOrbit: () => sceneOrbiting ? stopSceneOrbit() : startSceneOrbit(), onLandscape: chooseLandscape }} presentation={{ atmosphere: atmospherePreset, azimuth: lightAzimuth }} camera={{ pitch: view.pitch, bearing: view.bearing, fieldOfView }} cameraReady={runtime.kind === "ready"} onRecipe={chooseSceneRecipe} onLight={changeStudioLight} onCamera={composeSceneCamera} settings={sceneEffects} light={sceneEffects.sunSync ? sunSceneLight(sunAt, view.center[0], view.center[1]) : null} efficient={renderEfficient} reducedMotion={reducedMotion} flyoverActive={flyoverStopIndex !== null} onChange={updateSceneEffects} onFlyover={() => flyoverStopIndex !== null ? stopFlyover() : startFlyover()} onRepresentation={chooseSceneView} />}
              <button className="map-dock-action" type="button" onClick={(event) => openAtlasPanel("places", event.currentTarget)} aria-pressed={leftOpen && leftPanelMode === "places"}><strong>Places</strong><b>{savedWorkspaces.length}</b></button>
              <details className="map-dock-menu map-dock-map-menu" name="map-dock-menu" onKeyDown={(event) => { if (event.key === "Escape") { event.stopPropagation(); event.currentTarget.open = false; event.currentTarget.querySelector<HTMLElement>("summary")?.focus(); } }}>
                <summary aria-label="Map views and controls">Map <small className="map-dock-current-view">{undergroundOpen ? "Underground" : mapUtilityOpen && mapUtilityView === "compare" ? "Compare A/B" : mapRepresentationLabel}</small><span aria-hidden="true">⌄</span></summary>
                <div className="map-dock-menu-panel">
                  <div className="map-dock-menu-representations" role="group" aria-label="Map representation" onClick={(event) => { const button = (event.target as HTMLElement).closest("button"); if (button) closeHeaderOverflow(event.currentTarget, !button.hasAttribute("data-map-panel")); }}>
                    {mapRepresentationControls()}
                  </div>
                  <div className="map-dock-menu-quick" role="group" aria-label="Quick map controls">
                    <button type="button" aria-pressed={timelineOpen} onClick={(event) => { closeHeaderOverflow(event.currentTarget, false); toggleTimelinePanel(); }}>Time · {formatTimelineStep(year)}</button>
                    <button type="button" aria-pressed={leftOpen && leftPanelMode === "layers"} onClick={(event) => { closeHeaderOverflow(event.currentTarget, false); openAtlasPanel("layers", event.currentTarget); }}>Layers · {selectedMapLayerCount}</button>
                    <button type="button" aria-pressed={leftOpen && leftPanelMode === "places"} onClick={(event) => { closeHeaderOverflow(event.currentTarget, false); openAtlasPanel("places", event.currentTarget); }}>Places · {savedWorkspaces.length}</button>
                  </div>
                  <button type="button" aria-label="Style and basemap" onClick={(event) => { event.currentTarget.closest("details")?.removeAttribute("open"); openMapSettings(); }}><strong>Style &amp; basemap</strong><small>Rendering quality, terrain, and background</small></button>
                  <button type="button" aria-label="Map controls: coordinates, camera, and navigation" onClick={(event) => { const summary = event.currentTarget.closest("details")?.querySelector<HTMLElement>("summary"); event.currentTarget.closest("details")?.removeAttribute("open"); openMapUtility("navigate", summary); }}><strong>Map controls</strong><small>Coordinates, camera, and navigation</small></button>
                </div>
              </details>
            </div>
          </nav>
        <div className="top-actions">
          <button className="guide-trigger" type="button" aria-label={welcomeShowing ? "Map sources" : "Open the quick start guide"} title={welcomeShowing ? "Map sources" : "Quick start guide"} aria-pressed={welcomeShowing ? welcomeSourcesOpen : undefined} aria-expanded={welcomeShowing ? undefined : false} onClick={toggleExplorerGuide}>?</button>
          <details className="header-overflow-menu" onKeyDown={(event) => { if (event.key === "Escape") { event.stopPropagation(); event.currentTarget.open = false; event.currentTarget.querySelector<HTMLElement>("summary")?.focus(); } }}>
            <summary aria-label="More site actions" title="More site actions">More <span aria-hidden="true">⌄</span></summary>
            <div className="header-overflow-panel">
              <div className="header-overflow-workspaces" role="group" aria-label="Primary Explorer actions">
                <button type="button" aria-current={primaryWorkspace === "map" ? "page" : undefined} onClick={(event) => { event.currentTarget.closest("details")?.removeAttribute("open"); returnToPrimaryMap(); }}>Map</button>
                <button type="button" aria-current={primaryWorkspace === "reports" ? "page" : undefined} onClick={(event) => { openPrimaryWorkspace("reports"); closeHeaderOverflow(event.currentTarget); }}>Reports</button>
                <button type="button" aria-current={primaryWorkspace === "stories" ? "page" : undefined} onClick={(event) => { openPrimaryWorkspace("stories"); closeHeaderOverflow(event.currentTarget); }}>Stories</button>
              </div>
          <div className="map-context-composer">
            <button ref={composerTriggerRef} className="new-from-map-action" type="button" aria-expanded={mapContextOpen} aria-controls="map-context-card" onClick={() => { setMapContextOpen((current) => !current); setHelpOpen(false); }} title="Create from the current map context"><span aria-hidden="true">＋</span><span className="new-from-map-label">Compose</span><span className="new-from-map-caret" aria-hidden="true">⌄</span></button>
            {mapContextOpen && <aside ref={composerRef} id="map-context-card" className="map-context-card" role="dialog" aria-modal="false" aria-labelledby="map-context-title">
              <header>
                <div><span>CONTEXT COMPOSER</span><h2 id="map-context-title">Map context ready</h2></div>
                <button type="button" onClick={() => setMapContextOpen(false)} aria-label="Close map context composer">×</button>
              </header>
              <p>The current camera, visible layers, time, and evidence posture will carry into the next workspace.</p>
              <dl>
                <div><dt>Area</dt><dd>{selected ? selected.properties.spatialScope : analysisArea ? "Locked analysis area" : "Current viewport"}</dd></div>
                <div><dt>Representation</dt><dd>{mapRepresentationLabel}</dd></div>
                <div><dt>Layers</dt><dd>{visibleCount} visible</dd></div>
                <div><dt>Time</dt><dd>{temporalScopeLabel}</dd></div>
                <div><dt>Inspectable</dt><dd>{mapContextRecords.length} records</dd></div>
                <div><dt>Evidence</dt><dd>{supportedMapContextCount} source-backed · {mapContextRecords.length - supportedMapContextCount} bounded</dd></div>
              </dl>
              <div className="map-context-actions">
                <button type="button" onClick={(event) => {
                  setReportScope(selected ? "SELECTION" : analysisArea ? "ANALYSIS_AREA" : "VIEWPORT");
                  setReportLayerIds(activeLayers.map((layer) => layer.id));
                  event.currentTarget.blur();
                  openPrimaryWorkspace("reports", true);
                }}><span aria-hidden="true">▤</span><strong>Create evidence report</strong><small>Editable findings, limits, attribution, Markdown + JSON</small></button>
                <button type="button" onClick={() => openPrimaryWorkspace("stories", true)}><span aria-hidden="true">◇</span><strong>Create guided story</strong><small>Build and preview ordered scenes from this exact map state</small></button>
                <button type="button" onClick={() => { setMapContextOpen(false); setSourceObservatoryView("candidates"); setRepositoryView("sources"); setRepositoryOpen(true); announce("Opened verified candidate portals; discovery has no public effect"); }}><span aria-hidden="true">↗</span><strong>Inspect connected sources</strong><small>Official portals, intake gates, and known limits</small></button>
              </div>
              <footer><span>DRAFT · NOT PUBLISHED</span><p>Provider-backed map context remains distinct from admitted KFM evidence.</p></footer>
            </aside>}
          </div>
          <button ref={repositoryButtonRef} className="status-header-action" type="button" onClick={() => { setRepositoryView("updates"); setRepositoryOpen(true); }} aria-expanded={repositoryOpen} aria-controls="repository-briefing" title="Check Site, data, and repository connections"><span aria-hidden="true">⌁</span><span>Status</span></button>
              <button className="share-action" type="button" onClick={(event) => { closeHeaderOverflow(event.currentTarget); void shareView(); }}>Share current view</button>
              <Link className="about-action" href="/about">About</Link>
              <Link className="about-action" href="/privacy">Privacy</Link>
            </div>
          </details>
        </div>

        {helpOpen && <aside ref={mapGuideRef} className="map-guide" role="dialog" aria-modal="false" aria-label="Map guide">
          <button className="icon-close" type="button" onClick={closeMapGuide} aria-label="Close map guide">×</button>
          <p className="panel-kicker">MAP GUIDE</p><h2>Explore a feature, then check what supports it.</h2>
          <p>Choose a real source layer or select a mapped feature to inspect its provider, time, and limits. External context is not admitted KFM evidence.</p>
          <ol><li>Search, choose an example, or enable a layer.</li><li>Select a feature.</li><li>Inspect what is supported, missing, corrected, or withheld.</li><li>Review time, lineage, and Focus Mode when you need more detail.</li></ol>
          <p><strong>Shift + drag</strong> uses MapLibre box zoom. Map controls support coordinate navigation and camera orientation; Inspect has a keyboard-accessible feature list. Terrain uses an external display DEM when available. The comparison tool accepts browser-local road-year linework; display context is not an admitted KFM source.</p>
          <button className="map-guide-start" type="button" onClick={openMapGuideDiagnostics}>Map diagnostics</button>
        </aside>}
        <WelcomeFeatureGuide onNavigate={runWelcomeFeature} paused={reducedMotion || !dynamicEffects} hint={categoryMapOnScreen && primaryWorkspace === "map" ? { title: categoryMapOnScreen.name, text: categoryMapOnScreen.tip } : null} />
      </header>

      {primaryWorkspace !== "map" && workspaceSnapshot && <ReportStoryWorkspaces
        key={`${primaryWorkspace}:${workspaceSnapshot.id}`}
        mode={primaryWorkspace}
        snapshot={workspaceSnapshot}
        fireContext={fireReportContext}
        researchContext={researchReportContext}
        subsurfaceContext={subsurfaceReportContext}
        evidenceRecords={allEvidenceRecords}
        onModeChange={(mode) => { if (mode !== primaryWorkspace) openPrimaryWorkspace(mode); }}
        onReturnToMap={returnToPrimaryMap}
        onInspectEvidence={inspectWorkspaceEvidence}
        onApplyScene={applyStoryScene}
        getCurrentSnapshot={captureMapSnapshot}
      />}

      <div className="repository-overlay" hidden={!repositoryOpen} onMouseDown={(event) => { if (event.target === event.currentTarget) closeRepository(); }}>
        <aside ref={repositoryPanelRef} id="repository-briefing" className="repository-briefing" role="dialog" aria-modal="true" aria-labelledby="repository-briefing-title">
          <header className="repository-heading">
            <div><p className="panel-kicker">CONNECTIONS + REPOSITORY + SOURCES</p><h2 id="repository-briefing-title">Inspect KFM boundaries</h2><p>A pinned implementation snapshot, live read-only GitHub currentness, and source ideas without collapsing discovery into release.</p></div>
            <button className="icon-close" type="button" onClick={closeRepository} aria-label="Close repository briefing">×</button>
          </header>

          <section className="repository-snapshot" aria-label="Repository snapshot">
            <div className="snapshot-identity"><span>SITE REFERENCE SNAPSHOT</span><strong>main@{REPOSITORY_SNAPSHOT.shortCommit}</strong><small>Inspected {REPOSITORY_SNAPSHOT.inspectedAt}</small></div>
            <dl>
              <div><dt>Domains</dt><dd>{REPOSITORY_SNAPSHOT.counts.knowledgeDomains}</dd></div>
              <div><dt>Feature families</dt><dd>{REPOSITORY_SNAPSHOT.counts.explorerFeatureFamilies}</dd></div>
              <div><dt>Map functions</dt><dd>{REPOSITORY_SNAPSHOT.counts.mapFunctions}</dd></div>
              <div><dt>Dated records</dt><dd>{REPOSITORY_SNAPSHOT.counts.repositoryUpdates}</dd></div>
            </dl>
            <section className="status-map-actions" aria-label="Map source and baseline controls">
              <header><div><span>MAP STATUS</span><strong>Sources, live playback, and baseline</strong></div><small>{baselineDay} UTC</small></header>
              <div className="status-live-toggles" aria-label="Quick live data layer toggles">
                {QUICK_LIVE_CONTEXT_IDS.map((sourceId) => {
                  const source = OFFICIAL_CONTEXT_BY_ID[sourceId];
                  const heldAtFrame = officialVisibility[sourceId] && !effectiveOfficialVisibility[sourceId];
                  return <button key={sourceId} type="button" aria-pressed={officialVisibility[sourceId]} data-active={officialVisibility[sourceId]} data-held={heldAtFrame} onClick={() => setOfficialContextVisible(sourceId, !officialVisibility[sourceId])} title={`${officialVisibility[sourceId] ? "Hide" : "Show"} ${source.title}`}><i style={{ "--swatch": source.color } as React.CSSProperties} aria-hidden="true" /><strong>{source.shortTitle}</strong></button>;
                })}
              </div>
              <div className="status-map-links">
                <button type="button" aria-expanded={sourceStatusOpen} aria-controls="map-source-status" onClick={() => { setRepositoryOpen(false); openSourceStatus(repositoryButtonRef.current?.closest("details")?.querySelector<HTMLElement>("summary")); }}><strong>Source status</strong><small>Freshness, limits, and recovery</small></button>
                <button type="button" aria-pressed={instrumentOpen} onClick={() => { setRepositoryOpen(false); if (instrumentOpen) closeLiveInstrument(); else setInstrumentOpen(true); setCurrentWorkspace("explore"); window.requestAnimationFrame(() => mapContainerRef.current?.focus({ preventScroll: true })); }}><strong>Live controls</strong><small>River, radar, and lightning playback</small></button>
                <button type="button" onClick={() => window.location.assign("/")} title={`Open a fresh baseline for ${baselineDay} UTC`}><strong>Today’s baseline</strong><small>Reset to the current daily view</small></button>
              </div>
            </section>
            <div className="site-identity-strip" aria-label="Public application and historical references">
              <div>
                <span>PUBLIC APPLICATION</span>
                <strong>GoDaddy Node Explorer</strong>
                <a href={`${PUBLIC_SITE_ORIGIN}/about#project`}>{PUBLIC_SITE_ORIGIN.replace("https://", "")}</a>
                <small>Configured public origin. About records this build’s source and input digest; data release remains separate.</small>
              </div>
              <div>
                <span>HISTORICAL SITES REFERENCE</span>
                <strong>{SITE_IDENTITY.provider}</strong>
                <small>{SITE_IDENTITY.slug} · {SITE_IDENTITY.projectId}</small>
                <a href={SITE_IDENTITY.canonicalUrl} target="_blank" rel="noreferrer">{SITE_IDENTITY.canonicalUrl.replace("https://", "")}</a>
                <small>Historical host and domain check: {SITE_IDENTITY.customDomainStatus.replaceAll("_", " ")} · {SITE_IDENTITY.checkedAt}. This is not the public application’s routing or deployment status.</small>
              </div>
              <div data-state="warning">
                <span>HISTORICAL REPOSITORY LINEAGE</span>
                <strong>{SITE_IDENTITY.sourceRelation.replaceAll("_", " ")}</strong>
                <small>{SITE_IDENTITY.repositoryManifestStatus.replaceAll("_", " ")} · {SITE_IDENTITY.repositoryManifestProjectId}; inspect each source and its storage bindings separately.</small>
              </div>
            </div>
            <div className="repository-connection" data-state={repositoryConnection.state} role="status" aria-live="polite">
              <div>
                <span>LIVE READ-ONLY GITHUB CHECK</span>
                <strong>{repositoryConnection.state === "ready" ? `main@${repositoryConnection.shortCommit}` : repositoryConnection.state === "stale" ? `Last checked main@${repositoryConnection.shortCommit} · refresh needed` : repositoryConnection.state === "loading" ? "Checking current main…" : repositoryConnection.state === "error" ? "Live check unavailable" : "Check available"}</strong>
                <p>{repositoryConnection.state === "ready"
                  ? repositoryConnection.liveCommit === REPOSITORY_SNAPSHOT.commit
                    ? "GitHub main matches the Site reference snapshot."
                    : `GitHub main differs from this Site’s reference snapshot main@${REPOSITORY_SNAPSHOT.shortCommit}.`
                  : repositoryConnection.state === "stale"
                    ? "This observation is over one minute old. Refresh before using it as current status."
                  : repositoryConnection.state === "error"
                    ? "The pinned snapshot remains available; no currentness claim is inferred."
                    : "Reads fixed public repository metadata only when this briefing opens."}</p>
              </div>
              <button type="button" onClick={() => setRepositoryRefreshKey((current) => current + 1)} disabled={repositoryConnection.state === "loading"}>Refresh</button>
              {(repositoryConnection.state === "ready" || repositoryConnection.state === "stale") && <small>{repositoryConnection.message ?? "Current main commit"}{repositoryConnection.observedAt ? ` · checked ${new Date(repositoryConnection.observedAt).toLocaleString()}` : ""}</small>}
              <footer>Read-only metadata · separate Site and GitHub source histories · no automatic code sync or mutation</footer>
            </div>
          </section>

          <div className="repository-scroll">
            <nav className="repository-tabs" role="tablist" aria-label="Repository briefing views" onKeyDown={(event) => {
              if (!["ArrowLeft", "ArrowRight", "Home", "End"].includes(event.key)) return;
              const tabs = Array.from(event.currentTarget.querySelectorAll<HTMLButtonElement>("[role='tab']"));
              const current = tabs.indexOf(document.activeElement as HTMLButtonElement);
              const target = event.key === "Home" ? 0 : event.key === "End" ? tabs.length - 1 : (current + (event.key === "ArrowRight" ? 1 : -1) + tabs.length) % tabs.length;
              event.preventDefault();
              tabs[target]?.focus();
              tabs[target]?.click();
            }}>
              <button id="repository-tab-updates" aria-controls="repository-updates-panel" tabIndex={repositoryView === "updates" ? 0 : -1} type="button" role="tab" aria-selected={repositoryView === "updates"} onClick={() => setRepositoryView("updates")}><span>Updates</span><b>{REPOSITORY_UPDATES.length}</b></button>
              <button id="repository-tab-functions" aria-controls="repository-functions-panel" tabIndex={repositoryView === "functions" ? 0 : -1} type="button" role="tab" aria-selected={repositoryView === "functions"} onClick={() => setRepositoryView("functions")}><span>Functions</span><b>{FUNCTION_REGISTRY.length}</b></button>
              <button id="repository-tab-scenario" aria-controls="repository-scenario-panel" tabIndex={repositoryView === "scenario" ? 0 : -1} type="button" role="tab" aria-selected={repositoryView === "scenario"} onClick={() => setRepositoryView("scenario")}><span>Scenario review</span><b>4</b></button>
              <button id="repository-tab-runtime" aria-controls="repository-runtime-panel" tabIndex={repositoryView === "runtime" ? 0 : -1} type="button" role="tab" aria-selected={repositoryView === "runtime"} onClick={() => setRepositoryView("runtime")}><span>Runtime lab</span><b>3</b></button>
              <button id="repository-tab-transitions" aria-controls="repository-transitions-panel" tabIndex={repositoryView === "transitions" ? 0 : -1} type="button" role="tab" aria-selected={repositoryView === "transitions"} onClick={() => setRepositoryView("transitions")}><span>Transition inspector</span><b>{TRANSITION_BOUNDARIES.length}</b></button>
              <button id="repository-tab-readiness" aria-controls="repository-readiness-panel" tabIndex={repositoryView === "readiness" ? 0 : -1} type="button" role="tab" aria-selected={repositoryView === "readiness"} onClick={() => setRepositoryView("readiness")}><span>Readiness gates</span><b>{LIFECYCLE_GATES.length}</b></button>
              <button id="repository-tab-sources" aria-controls="repository-sources-panel" tabIndex={repositoryView === "sources" ? 0 : -1} type="button" role="tab" aria-selected={repositoryView === "sources"} onClick={() => setRepositoryView("sources")}><span>Source observatory</span><b>{SOURCE_CANDIDATES.length}</b></button>
            </nav>

            {repositoryView === "updates" && <section id="repository-updates-panel" role="tabpanel" className="repository-update-section" aria-labelledby="repository-tab-updates">
              <div className="repository-section-heading"><div><span>FIELD UPDATES</span><h3 id="repository-updates-title">Grounded changes, not release claims</h3></div><a href={`https://github.com/${REPOSITORY_SNAPSHOT.repository}/tree/${REPOSITORY_SNAPSHOT.commit}`} target="_blank" rel="noreferrer">Open pinned tree ↗</a></div>
              <div className="repository-toolbar">
                <label><span className="sr-only">Search repository updates</span><i aria-hidden="true">⌕</i><input type="search" value={repositoryQuery} onChange={(event) => setRepositoryQuery(event.target.value)} placeholder="Search updates and boundaries" /></label>
                <label><span className="sr-only">Filter repository updates by state</span><select value={repositoryStateFilter} onChange={(event) => setRepositoryStateFilter(event.target.value as "ALL" | RepositoryUpdateState)}><option value="ALL">All states</option><option value="CORRECTED">Corrected</option><option value="ACCEPTED">Accepted</option><option value="BOUNDED PROOF">Bounded proof</option><option value="NEEDS VERIFICATION">Needs verification</option></select></label>
                <span>{filteredRepositoryUpdates.length} of {REPOSITORY_UPDATES.length} signals</span>
              </div>
              <div className="repository-update-grid">
                {filteredRepositoryUpdates.map((update) => <article key={update.id} className="repository-update-card" data-state={update.state}>
                  <div className="update-meta"><span>{update.area}</span><time>{update.date}</time></div>
                  <div className="update-assessment" aria-label={`Authority posture ${update.state}; capability maturity ${update.maturity}`}>
                    <span><small>Authority</small><strong className="update-state">{update.state}</strong></span>
                    <span><small>Maturity</small><strong className="update-maturity">{update.maturity}</strong></span>
                  </div>
                  <h4>{update.title}</h4>
                  <p>{update.summary}</p>
                  <div className="update-boundary"><span>Boundary</span><p>{update.boundary}</p></div>
                  <footer>
                    <a href={update.sourceUrl} target="_blank" rel="noreferrer">{update.sourceLabel} ↗</a>
                    {update.layerId && update.featureId && <button type="button" onClick={() => { setRepositoryOpen(false); selectStoredFeature(update.layerId!, update.featureId!); }}>Inspect local analogue</button>}
                  </footer>
                </article>)}
              </div>
              {filteredRepositoryUpdates.length === 0 && <div className="repository-empty"><strong>No matching repository signals</strong><p>Clear the search or choose another evidence state.</p></div>}
            </section>}

            {repositoryView === "functions" && <section id="repository-functions-panel" role="tabpanel" className="function-registry-section" aria-labelledby="repository-tab-functions">
              <div className="repository-section-heading"><div><span>AUTHORITY × MATURITY × INVENTORY</span><h3 id="function-registry-title">Function and interface navigator</h3></div><small>20 map functions · 9 Site workflows · 6 no-effect handoffs</small></div>
              <p className="function-registry-intro">The draft repository matrix supplies the full map-function inventory, while Site evidence decides what is implemented here. Higher-level workflows and operational handoffs stay visibly separate from atomic functions.</p>
              <div className="function-state-summary" aria-label="Function registry state counts">
                {(["ACTIVE", "BOUNDED", "DOCUMENTED", "GATED"] as const).map((state) => <article key={state} data-state={state}><span>{state}</span><strong>{functionCounts[state]}</strong></article>)}
              </div>
              <div className="function-registry-controls">
                <nav aria-label="Function registry groups">
                  {(["PUBLIC_INTERFACE", "OPERATIONAL_HANDOFF"] as FunctionGroup[]).map((group) => <button key={group} type="button" aria-pressed={functionGroup === group} onClick={() => { setFunctionGroup(group); setFunctionQuery(""); setActiveFunctionId(functionsForGroup(group)[0].id); }}>{group === "PUBLIC_INTERFACE" ? "Public interfaces" : "Operational handoffs"}<b>{functionsForGroup(group).length}</b></button>)}
                </nav>
                <label><span className="sr-only">Search functions and interface boundaries</span><i aria-hidden="true">⌕</i><input type="search" value={functionQuery} onChange={(event) => setFunctionQuery(event.target.value)} placeholder="Search function, interface, gate, or maturity" /></label>
              <TopicSelect label="Function topic" value={functionTopic} onChange={setFunctionTopic} />
              </div>
              <div className="function-workbench">
                <div className="function-selector" aria-label="Available function records">
                  {filteredFunctions.map((record) => <button key={record.id} type="button" data-active={record.id === activeFunction?.id} data-state={record.state} aria-pressed={record.id === activeFunction?.id} onClick={() => setActiveFunctionId(record.id)}><span>{record.state}</span><strong>{record.title}</strong><small>{record.inventory} · {record.interface}</small></button>)}
                  {filteredFunctions.length === 0 && <p>No function matches this search.</p>}
                </div>
                {activeFunction && <article className="function-detail" data-state={activeFunction.state}>
                  <header><span>{activeFunction.group.replaceAll("_", " ")}</span><strong>{activeFunction.state}</strong></header>
                  <h4>{activeFunction.title}</h4><p>{activeFunction.summary}</p>
                  <div className="function-axis-grid" aria-label={`Authority ${activeFunction.authority}; maturity ${activeFunction.maturity}; inventory ${activeFunction.inventory}`}>
                    <span><small>Authority posture</small><strong>{activeFunction.authority}</strong></span>
                    <span><small>Implementation maturity</small><strong>{activeFunction.maturity}</strong></span>
                    <span><small>Inventory source</small><strong>{activeFunction.inventory}</strong></span>
                  </div>
                  <dl><div><dt>Safe interface</dt><dd>{activeFunction.interface}</dd></div><div><dt>Boundary</dt><dd>{activeFunction.boundary}</dd></div></dl>
                  <section><span>Required closure</span><ul>{activeFunction.requires.map((requirement) => <li key={requirement}>{requirement}</li>)}</ul></section>
                  <footer><div><span>Evidence basis</span>{activeFunction.sourcePath ? <a href={`https://github.com/${REPOSITORY_SNAPSHOT.repository}/blob/${REPOSITORY_SNAPSHOT.commit}/${activeFunction.sourcePath}`} target="_blank" rel="noreferrer">{activeFunction.sourceLabel} ↗</a> : <p>{activeFunction.sourceLabel}</p>}</div><button type="button" disabled={activeFunction.action === "NONE"} onClick={() => launchFunction(activeFunction)}>{activeFunction.actionLabel}</button></footer>
                </article>}
              </div>
              <aside className="function-boundary-note"><strong>Operational handoff ≠ operational action</strong><p>Copied handoffs carry exact context, required closure, source path, and explicit non-effects. They cannot write a source, policy, review, lifecycle, release, deployment, promotion, or publication state.</p></aside>
            </section>}

            {repositoryView === "scenario" && <section id="repository-scenario-panel" role="tabpanel" className="planning-scenario-section" aria-labelledby="repository-tab-scenario">
              <div className="repository-section-heading"><div><span>FIXTURE-ONLY · TEXT-FIRST REVIEW</span><h3 id="planning-scenario-title">Planning scenario state lab</h3></div><a href={`https://github.com/${REPOSITORY_SNAPSHOT.repository}/blob/${REPOSITORY_SNAPSHOT.commit}/apps/explorer-web/src/features/planning_scenario_review/README.md`} target="_blank" rel="noreferrer">Open pinned feature ↗</a></div>
              <p className="planning-scenario-intro">Replay the four finite projections established by the current repository slice. Only the held synthetic fixture exposes review detail; missing, denied, and error states suppress scenario, evidence, participation, and limitation fields.</p>
              <nav className="planning-scenario-modes" aria-label="Planning scenario fixture states">
                {PLANNING_SCENARIO_MODES.map((mode) => <button key={mode.id} type="button" aria-pressed={scenarioReviewMode === mode.id} onClick={() => setScenarioReviewMode(mode.id)}>{mode.label}</button>)}
              </nav>
              <article className="planning-scenario-review" data-outcome={planningScenarioReview.outcome} role="status" aria-live={planningScenarioReview.outcome === "ABSTAIN" ? "polite" : "assertive"}>
                <header><div><span>{planningScenarioReview.outcome} / {planningScenarioReview.code}</span><h4>{planningScenarioReview.heading}</h4></div><strong>{planningScenarioReview.scenarioStatus ?? "NO DETAIL"}</strong></header>
                <p>{planningScenarioReview.message}</p>
                {planningScenarioReview.scenarioStatus === "HELD" && <>
                  <p className="planning-scenario-purpose">{planningScenarioReview.purpose}</p>
                  <dl className="planning-scenario-scope"><div><dt>Geography</dt><dd>{planningScenarioReview.geography}</dd></div><div><dt>Baseline as of</dt><dd>{planningScenarioReview.baselineAsOf}</dd></div><div><dt>Exploratory horizon</dt><dd>{planningScenarioReview.horizon}</dd></div></dl>
                  <div className="planning-scenario-table-wrap"><table><caption>Scenario inputs and uncertainty</caption><thead><tr><th scope="col">Input</th><th scope="col">Uncertainty</th><th scope="col">Evidence source</th></tr></thead><tbody>{planningScenarioReview.inputs.map((input) => <tr key={input.id}><th scope="row">{input.label}</th><td data-uncertainty={input.uncertainty}>{input.uncertainty}</td><td><code>{input.sourceRef}</code></td></tr>)}</tbody></table></div>
                  <div className="planning-scenario-review-grid">
                    <section><h5>Assumptions + uncertainty</h5><ol>{planningScenarioReview.assumptions.map((assumption) => <li key={assumption.id}><p>{assumption.statement}</p><strong>{assumption.uncertainty}</strong></li>)}</ol></section>
                    <section><h5>Equity questions + limits</h5><ul>{planningScenarioReview.equityQuestions.map((question) => <li key={question.id}><p>{question.description}</p><small>{question.limitation}</small></li>)}</ul></section>
                  </div>
                  <details className="planning-scenario-details"><summary>Inspect participation, evidence, and limitations</summary><div><section><h5>Participation references</h5>{planningScenarioReview.participationRefs.map((reference) => <code key={reference}>{reference}</code>)}</section><section><h5>Evidence references</h5>{planningScenarioReview.evidenceRefs.map((reference) => <code key={reference}>{reference}</code>)}</section><section><h5>Limitations</h5>{planningScenarioReview.limitations.map((limitation) => <p key={limitation}>{limitation}</p>)}</section></div></details>
                  <div className="planning-scenario-authority" aria-label="Planning scenario authority flags"><span>Evidence resolved <b>FALSE</b></span><span>Policy approved <b>FALSE</b></span><span>Review approved <b>FALSE</b></span><span>Recommendation authorized <b>FALSE</b></span><span>Publication authorized <b>FALSE</b></span></div>
                  <div className="planning-scenario-labels" aria-label="Non-authority labels">{planningScenarioReview.nonAuthorityLabels.map((label) => <span key={label}>{label.replaceAll("_", " ")}</span>)}</div>
                </>}
              </article>
              <aside className="function-boundary-note"><strong>Review context ≠ scenario authority</strong><p>This Site-local replay performs no transport, source retrieval, scenario computation, preference aggregation, policy evaluation, lifecycle write, release, deployment, or publication action. It does not mean the repository feature is mounted on a KFM production route.</p></aside>
            </section>}

            {repositoryView === "runtime" && <section id="repository-runtime-panel" role="tabpanel" className="runtime-lab-section" aria-labelledby="repository-tab-runtime">
              <div className="repository-section-heading"><div><span>STATIC CODE-SHAPE REPLAY</span><h3 id="runtime-lab-title">Governed API route lab</h3></div><a href={`https://github.com/${REPOSITORY_SNAPSHOT.repository}/blob/${REPOSITORY_SNAPSHOT.commit}/docs/atlas/master-api-surface.md`} target="_blank" rel="noreferrer">Open pinned checkpoint ↗</a></div>
              <p className="runtime-lab-intro">Exercise the exact bounded route matrix observed on GitHub. This lab makes no network request and does not imply that a KFM API is deployed.</p>
              <div className="runtime-lab-grid">
                <div className="runtime-route-controls">
                  <label><span>Method</span><select value={governedMethod} onChange={(event) => setGovernedMethod(event.target.value as GovernedMethod)}><option value="GET">GET</option><option value="POST">POST · unsupported</option></select></label>
                  <div><span>Path</span>{(["/bootstrap", "/layers", "/evidence", "/focus"] as GovernedRoute[]).map((path) => <button key={path} type="button" data-active={governedRoute === path} onClick={() => setGovernedRoute(path)}><code>{path}</code><small>{governedRoutes.has(path) ? "REGISTERED" : "UNKNOWN / 404"}</small></button>)}</div>
                  <aside><strong>Observed executable surface</strong><p>Three GET routes return finite negative envelopes. There is no current <code>/focus</code> route or substantive payload.</p></aside>
                </div>
                <article className="runtime-envelope" data-outcome={governedRouteResult.envelope.outcome}>
                  <header><div><span>HTTP {governedRouteResult.http_status}</span><strong>{governedRouteResult.envelope.outcome}</strong></div><b>CODE SHAPE · NOT DEPLOYED</b></header>
                  <div className="runtime-resolution"><code>{governedMethod} {governedRoute}</code><span>→</span><strong>{governedRouteResult.envelope.reason_code}</strong></div>
                  <pre aria-label="Static runtime response envelope">{JSON.stringify(governedRouteResult, null, 2)}</pre>
                  <footer><span>Four client outcomes only</span><b>ANSWER · ABSTAIN · DENY · ERROR</b><p>HOLD, PASS, FAIL, and APPROVE_READY are workflow or assessment states—not runtime outcomes.</p></footer>
                </article>
              </div>
              <div className="runtime-boundary-grid">
                <article><span>Shape proof</span><strong>Closed envelope</strong><p>Negative route behavior is deterministic and schema-shaped.</p></article>
                <article><span>Evidence</span><strong>Not resolved here</strong><p>An empty reference list cannot support ANSWER.</p></article>
                <article><span>Policy / release</span><strong>Not evaluated</strong><p>Code and merge state do not publish KFM data.</p></article>
                <article><span>Transport</span><strong>No request sent</strong><p>The Site replays repository evidence locally.</p></article>
              </div>
            </section>}

            {repositoryView === "transitions" && <section id="repository-transitions-panel" role="tabpanel" className="transition-section" aria-labelledby="repository-tab-transitions">
              <div className="repository-section-heading"><div><span>STATE BOUNDARIES</span><h3 id="transition-inspector-title">Inspect without collapsing state families</h3></div><small>Documentation view · no transition is applied</small></div>
              <div className="transition-workbench">
                <div className="transition-selector" aria-label="Documented transition boundaries">
                  {TRANSITION_BOUNDARIES.map((transition) => <button key={transition.id} type="button" data-active={transition.id === activeTransition.id} data-posture={transition.posture} onClick={() => setActiveTransitionId(transition.id)}>
                    <span>{transition.family} · {transition.posture}</span><strong><b>{transition.from}</b><i aria-hidden="true">→</i><b>{transition.to}</b></strong><small>{transition.title}</small>
                  </button>)}
                </div>
                <article className="transition-detail" data-posture={activeTransition.posture}>
                  <header><span>{activeTransition.family} BOUNDARY</span><strong>{activeTransition.posture}</strong></header>
                  <div className="transition-path"><b>{activeTransition.from}</b><i aria-hidden="true">→</i><b>{activeTransition.to}</b></div>
                  <h4>{activeTransition.title}</h4>
                  <p>{activeTransition.summary}</p>
                  <dl><div><dt>Guard</dt><dd>{activeTransition.guard}</dd></div><div><dt>Public projection</dt><dd>{activeTransition.projection}</dd></div></dl>
                  <div className="transition-proof"><span>Required proof</span><ul>{activeTransition.proof.map((item) => <li key={item}>{item}</li>)}</ul></div>
                  <footer><a href={activeTransition.sourceUrl} target="_blank" rel="noreferrer">Open pinned specification ↗</a>{activeTransition.layerId && activeTransition.featureId && <button type="button" onClick={() => { setRepositoryOpen(false); selectStoredFeature(activeTransition.layerId!, activeTransition.featureId!); }}>{activeTransition.analogueLabel}</button>}</footer>
                </article>
              </div>
            </section>}

            {repositoryView === "readiness" && <section id="repository-readiness-panel" role="tabpanel" className="readiness-section" aria-labelledby="repository-tab-readiness">
              <div className="repository-section-heading"><div><span>FIXTURE-ONLY ASSESSMENT</span><h3 id="readiness-title">Lifecycle gate closure map</h3></div><small>Assessment ≠ approval ≠ applied transition</small></div>
              <p className="readiness-intro">These seven repository-present gate shapes expose the required accountability roles and their fail-closed dispositions. They do not prove live evidence resolution, policy execution, signer authority, release, correction, rollback, or public serving.</p>
              <div className="lifecycle-gates">
                {LIFECYCLE_GATES.map((gate, index) => <article key={gate.id}><span>{String(index + 1).padStart(2, "0")}</span><div><strong>{gate.id}</strong><small>{gate.transition}</small><p>{gate.roles}</p></div><code>{gate.failClosed}</code></article>)}
              </div>
              <section className="feature-radar" aria-labelledby="feature-radar-title">
                <div className="repository-section-heading"><div><span>COMPLETE FEATURE CATALOG</span><h3 id="feature-radar-title">All 38 repository feature families</h3></div><small>Repository maturity labels · not Site implementation claims</small></div>
                <div className="function-state-summary feature-state-summary" aria-label="Feature maturity counts">
                  {(["VERIFIED_SLICE", "FIXTURE_FIRST", "DOCUMENTED", "HOLD"] as const).map((maturity) => <article key={maturity} data-state={maturity}><span>{featureMaturityLabel(maturity)}</span><strong>{featureMaturityCounts[maturity]}</strong></article>)}
                </div>
                <div className="feature-catalog-controls">
                  <label><span className="sr-only">Search the repository feature catalog</span><i aria-hidden="true">⌕</i><input type="search" value={featureQuery} onChange={(event) => setFeatureQuery(event.target.value)} placeholder="Search feature, area, maturity, or source path" /></label>
                  <TopicSelect label="Repository feature topic" value={featureTopic} onChange={setFeatureTopic} />
                  <label><span className="sr-only">Filter repository features by area</span><select value={featureArea} onChange={(event) => setFeatureArea(event.target.value as FeatureArea | "ALL")}><option value="ALL">All areas</option>{FEATURE_AREAS.map((area) => <option key={area} value={area}>{area}</option>)}</select></label>
                  <label><span className="sr-only">Filter repository features by maturity</span><select value={featureMaturity} onChange={(event) => setFeatureMaturity(event.target.value as FeatureMaturity | "ALL")}><option value="ALL">All maturity states</option><option value="VERIFIED_SLICE">Verified slice</option><option value="FIXTURE_FIRST">Fixture first</option><option value="DOCUMENTED">Documented</option><option value="HOLD">Hold</option></select></label>
                  <span>{filteredFeatures.length} of {FEATURE_CATALOG.length}</span>
                </div>
                <div className="feature-radar-grid">
                  {filteredFeatures.map((feature) => <article key={feature.id} data-state={feature.maturity}><span>{featureMaturityLabel(feature.maturity)}</span><small>{feature.area} · {featureTopics(feature.id).map(topic => topicDefinition(topic)?.title).join(" · ")}</small><strong>{feature.name}</strong><p>{feature.summary}</p><a href={`https://github.com/${REPOSITORY_SNAPSHOT.repository}/tree/${REPOSITORY_SNAPSHOT.commit}/${feature.path}`} target="_blank" rel="noreferrer">Open source ↗</a></article>)}
                </div>
                {filteredFeatures.length === 0 && <div className="repository-empty"><strong>No matching feature families</strong><p>Clear the search or choose another area or maturity state.</p></div>}
              </section>
            </section>}

            {repositoryView === "sources" && <section id="repository-sources-panel" role="tabpanel" className="source-observatory" aria-labelledby="repository-tab-sources">
              <div className="repository-section-heading"><div><span>DRIVE-BACKED DISCOVERY · NO PUBLIC EFFECT</span><h3 id="source-observatory-title">Source intelligence observatory</h3></div><small>{CORPUS_SNAPSHOT.rule}</small></div>
              <div className="source-observatory-summary">
                <article><span>Corpus references</span><strong>{CORPUS_SOURCES.length}</strong></article>
                <article><span>Candidate families</span><strong>{SOURCE_CANDIDATES.length}</strong></article>
                <article><span>Tracked gaps</span><strong>{SOURCE_GAPS.length}</strong></article>
                <p><b>Discovery ≠ admission.</b> These records preserve useful ideas and their limits without activating a source, changing a layer, or asserting runtime readiness.</p>
              </div>
              <nav className="source-tabs" role="tablist" aria-label="Source observatory views">
                <button type="button" role="tab" aria-selected={sourceObservatoryView === "candidates"} data-active={sourceObservatoryView === "candidates"} onClick={() => setSourceObservatoryView("candidates")}>Candidate sources <b>{SOURCE_CANDIDATES.length}</b></button>
                <button type="button" role="tab" aria-selected={sourceObservatoryView === "corpus"} data-active={sourceObservatoryView === "corpus"} onClick={() => setSourceObservatoryView("corpus")}>Corpus ledger <b>{CORPUS_SOURCES.length}</b></button>
                <button type="button" role="tab" aria-selected={sourceObservatoryView === "gaps"} data-active={sourceObservatoryView === "gaps"} onClick={() => setSourceObservatoryView("gaps")}>Gap register <b>{SOURCE_GAPS.length}</b></button>
              </nav>

              <div className="source-admission-legend" aria-label="Source admission states and record counts">
                {SOURCE_ADMISSION_STATES.filter((state): state is SourceAdmissionState => state !== "ALL").map((state) => <button key={state} type="button" data-active={sourceAdmissionState === state} onClick={() => setSourceAdmissionState((current) => current === state ? "ALL" : state)}><span>{state.replaceAll("-", " ")}</span><b>{sourceAdmissionCounts[state]}</b></button>)}
              </div>

              {sourceObservatoryView === "candidates" && <>
                <div className="repository-toolbar source-toolbar">
                  <label><span className="sr-only">Search source candidates</span><i aria-hidden="true">⌕</i><input type="search" value={sourceQuery} onChange={(event) => setSourceQuery(event.target.value)} placeholder="Search sources, organizations, roles, and gates" /></label>
                  <label><span className="sr-only">Filter source candidates by domain</span><select value={sourceDomain} onChange={(event) => setSourceDomain(event.target.value)}>{SOURCE_DOMAINS.map((domain) => <option key={domain} value={domain}>{domain === "ALL" ? "All domains" : domain}</option>)}</select></label>
                  <label><span className="sr-only">Filter source records by admission state</span><select value={sourceAdmissionState} onChange={(event) => setSourceAdmissionState(event.target.value as SourceAdmissionState | "ALL")}>{SOURCE_ADMISSION_STATES.map((state) => <option key={state} value={state}>{state === "ALL" ? "All admission states" : state.replaceAll("-", " ")}</option>)}</select></label>
                  <span>{filteredSourceCandidates.length} of {SOURCE_CANDIDATES.length} source records</span>
                </div>
                <div className="source-candidate-grid">
                  {filteredSourceCandidates.map((source) => <article key={source.id} className="source-candidate-card" data-admission={SOURCE_ADMISSION_BY_ID[source.id] ?? "candidate"}>
                    <header><span>{source.domain}</span><strong>{(SOURCE_ADMISSION_BY_ID[source.id] ?? "candidate").replaceAll("-", " ").toUpperCase()} · NO PUBLIC EFFECT</strong></header>
                    <h4>{source.title}</h4><p className="source-organization">{source.organization} · {source.cadence} · official portal checked <time dateTime={source.checkedAt}>{source.checkedAt}</time></p>
                    <dl><div><dt>Source role</dt><dd>{source.sourceRole}</dd></div><div><dt>Candidate value</dt><dd>{source.value}</dd></div><div><dt>Cannot prove</dt><dd>{source.cannotProve}</dd></div><div><dt>Next gate</dt><dd>{source.nextGate}</dd></div></dl>
                    <div className="source-modes">{source.dataModes.map((mode) => <span key={mode}>{mode}</span>)}</div>
                    <footer><a href={source.sourceUrl} target="_blank" rel="noreferrer">Open official source ↗</a>{source.discoveryPath && <Link href={source.discoveryPath}>Explore datasets & recipes</Link>}<button type="button" onClick={() => copySourceIntakeDraft(source)}>Copy bounded intake draft</button>{source.layerId && source.featureId && <button type="button" onClick={() => { setRepositoryOpen(false); selectStoredFeature(source.layerId!, source.featureId!); }}>Inspect local analogue</button>}</footer>
                  </article>)}
                </div>
                {filteredSourceCandidates.length === 0 && <div className="repository-empty"><strong>No matching source records</strong><p>Clear the search or choose another domain or admission state.</p></div>}
              </>}

              {sourceObservatoryView === "corpus" && <div className="corpus-ledger-grid">
                {CORPUS_SOURCES.map((source) => <article key={source.id} data-status={source.status}><header><span>{source.authority}</span><strong>{source.status}</strong></header><h4>{source.title}</h4><small>{source.version}</small><div>{source.supports.map((item) => <span key={item}>{item}</span>)}</div><p><b>Limit:</b> {source.limitation}</p></article>)}
              </div>}

              {sourceObservatoryView === "gaps" && <div className="source-gap-grid">
                {SOURCE_GAPS.map((gap) => <article key={gap.id} data-disposition={gap.disposition}><header><span>{gap.priority} · {gap.id}</span><strong>{gap.disposition}</strong></header><h4>{gap.title}</h4><p>{gap.reason}</p><div><span>Closure evidence</span><p>{gap.unlock}</p></div></article>)}
              </div>}
            </section>}

            <aside className="repository-boundary-note">
              <strong>Repository state ≠ site data state</strong>
              <p>This briefing reports inspected repository bytes. Map geometry uses separately labeled external source context. A merge, test, receipt, or renderer does not itself release or publish KFM data.</p>
            </aside>
          </div>
        </aside>
      </div>

      <main inert={primaryWorkspace !== "map"} className="explorer-shell" data-inspector={inspectionPanel ?? "closed"} data-left={leftOpen} data-right={rightOpen} data-timeline={timelineOpen}>
        <aside ref={leftPanelRef} className="layer-panel" data-panel-mode={leftPanelMode} aria-label={leftPanelMode === "layers" || leftPanelMode === "live" ? "Map layers" : "Living Atlas navigation"} aria-hidden={!leftOpen} inert={!leftOpen} aria-modal={isCompact && leftOpen || undefined} role={isCompact && leftOpen ? "dialog" : undefined}>
          <div className="panel-heading">
            <div><p className="panel-kicker">{leftPanelMode === "views" ? "LIVING ATLAS" : leftPanelMode === "live" || leftPanelMode === "layers" ? "KANSAS FRONTIER MATRIX" : leftPanelMode === "places" ? "PLACES" : "STORY ATLAS"}</p><h1>{leftPanelMode === "views" ? "Investigate Kansas" : leftPanelMode === "live" || leftPanelMode === "layers" ? <>Map layers <span className="layer-panel-count">{selectedMapLayerCount} selected</span></> : leftPanelMode === "places" ? "Places + trails" : "Guided stories"}</h1></div>
            <button className="icon-close" type="button" onClick={closeLeftPanel} aria-label="Close Explorer navigation">×</button>
          </div>
          {leftPanelMode !== "layers" && leftPanelMode !== "live" && <p className="panel-intro">{leftPanelMode === "views" ? "Start from a named question, then inspect the map, time, evidence, and report together." : leftPanelMode === "places" ? "Save complete, device-local investigations and revisit them as a trail." : "Pause on a site-local chapter, inspect its evidence state, and keep the boundary visible."}</p>}
          {leftPanelMode !== "layers" && leftPanelMode !== "live" && <nav className="left-panel-tabs" aria-label="Living Atlas sections">
            <button type="button" aria-current={leftPanelMode === "views" ? "page" : undefined} data-active={leftPanelMode === "views"} onClick={() => setLeftPanelMode("views")}>Views <b>{LIVING_ATLAS_VIEWS.length}</b></button>
            <button type="button" onClick={() => { setStarterPanelOpen(false); setLayerCatalogView("official"); setLeftPanelMode("layers"); }}>Map layers <b>{selectedMapLayerCount}</b></button>
            <button type="button" aria-current={leftPanelMode === "places" ? "page" : undefined} data-active={leftPanelMode === "places"} onClick={() => setLeftPanelMode("places")}>Places <b>{savedWorkspaces.length}</b></button>
          </nav>}

          <section className="atlas-view-library" hidden={leftPanelMode !== "views"} aria-labelledby="atlas-view-library-title">
            <div className="atlas-library-heading"><div><span className="panel-kicker">DEFAULT INVESTIGATIONS</span><h2 id="atlas-view-library-title">Choose a starting question</h2></div><small>{filteredAtlasViews.length} of {LIVING_ATLAS_VIEWS.length}</small></div>
            <label className="atlas-search-control"><span aria-hidden="true">⌕</span><span className="sr-only">Search Living Atlas views</span><input type="search" value={atlasViewQuery} onChange={(event) => setAtlasViewQuery(event.target.value)} placeholder="Search questions, domains, or time" /></label>
            <TopicSelect label="Investigation topic" value={atlasTopic} onChange={setAtlasTopic} />
            <TopicGuide value={atlasTopic} onTool={(view, element) => openMapUtility(view, element)} />
            <div className="atlas-view-list">
              {filteredAtlasViews.map((atlasView) => <article className="atlas-view-card" key={atlasView.id} data-status={atlasView.status} data-active={atlasView.profileId === activeViewProfileId}>
                <header><span>{livingAtlasStatusLabel(atlasView.status)}</span><small>{atlasView.display}</small></header>
                <h3>{atlasView.title}</h3>
                <p className="atlas-view-question">{atlasView.question}</p>
                <dl><div><dt>Scope</dt><dd>{atlasView.scope}</dd></div><div><dt>Time</dt><dd>{atlasView.time}</dd></div><div><dt>Source posture</dt><dd>{atlasView.sourcePosture}</dd></div></dl>
                <div className="atlas-view-domains" aria-label={`${atlasView.title} domains`}>{atlasViewTopics(atlasView.id).map(topic => <span key={topic}>{topicDefinition(topic)?.title}</span>)}</div>
                <p className="atlas-view-note">{atlasView.note}</p>
                <footer><span>{atlasView.report}</span><button type="button" onClick={() => applyLivingAtlasView(atlasView)}>Open on map</button></footer>
                {atlasView.syntheticProof && <LivingWatersControl mapRef={mapRef} styleReady={styleReady} flatMap={projection === "mercator" && scenePreset !== "elevation-3d"} onFlatMap={() => activateMapRepresentation("2d")} onInspect={() => { setLeftPanelMode("views"); setAtlasViewQuery(""); setLeftOpen(true); }} />}
              </article>)}
              {filteredAtlasViews.length === 0 && <div className="catalog-empty"><strong>No matching investigations</strong><p>Try a place, domain, time, or question.</p></div>}
            </div>
            <aside className="panel-boundary-note"><strong>Named view ≠ admitted data</strong><p>These views use provider-backed context. Open each source card to check its status, time, and limits.</p></aside>
          </section>

          <section className="panel-mode-placeholder places-trail-section" hidden={leftPanelMode !== "places"} aria-labelledby="places-panel-title">
            <div className="panel-mode-heading"><span className="panel-kicker">DEVICE-LOCAL WORKSPACES</span><h2 id="places-panel-title">Return to an investigation</h2></div>
            <p>Places stores camera, time, layers, comparison, report setup, and selected evidence on this device only.</p>
            <div className="panel-stat-grid"><article><span>SAVED PLACES</span><strong>{savedWorkspaces.length}</strong></article><article><span>ACTIVE PLACE</span><strong>{activePlaceId ? "YES" : "NONE"}</strong></article></div>
            <article className="place-capture-card">
                  <header><div><span>CURRENT MAP STATE</span><strong>{temporalScopeLabel} · {visibleCount} visible layers</strong></div><small>{selected ? `Selected: ${selected.properties.title}` : "No selected feature"}</small></header>
                  <div className="workspace-save-row"><input type="text" value={workspaceName} maxLength={50} onChange={(event) => setWorkspaceName(event.target.value)} placeholder="Place or investigation step name" /><button type="button" onClick={saveCurrentWorkspace}>Add place</button></div>
                </article>
                <div className="place-trail-controls" aria-label="Places trail controls">
                  <button type="button" onClick={() => stepPlaceTrail(-1)} disabled={savedWorkspaces.length === 0}>← Previous</button>
                  <button type="button" onClick={() => placeTourPlaying ? stopPlaceTour() : playPlaceTrail()} disabled={savedWorkspaces.length < 2}>{placeTourPlaying ? "Stop trail" : "▶ Play trail"}</button>
                  <button type="button" onClick={() => stepPlaceTrail(1)} disabled={savedWorkspaces.length === 0}>Next →</button>
                </div>
                <div className="place-trail-list" aria-label="Saved investigation places">
                  {savedWorkspaces.map((snapshot, index) => <article key={snapshot.id} data-active={activePlaceId === snapshot.id}>
                    <span className="place-stop-number">{String(index + 1).padStart(2, "0")}</span>
                    <button className="place-stop-main" type="button" onClick={() => { stopPlaceTour(false); loadSavedWorkspace(snapshot); }} aria-pressed={activePlaceId === snapshot.id}>
                      <strong>{snapshot.name}</strong><small>{formatTimelineStep(snapshot.year)} · {Object.values(snapshot.visibility ?? {}).filter(Boolean).length} layers · {snapshot.projection === "globe" ? "globe" : "2D"}</small><em>{snapshot.locationCameraRedacted !== false ? "Generalized camera" : snapshot.selection ? `Selection: ${snapshot.selection.featureId}` : "Map context"}</em>
                    </button>
                    <div className="place-stop-actions"><button type="button" onClick={() => reorderSavedWorkspace(snapshot, -1)} disabled={index === 0} aria-label={`Move ${snapshot.name} earlier`}>↑</button><button type="button" onClick={() => reorderSavedWorkspace(snapshot, 1)} disabled={index === savedWorkspaces.length - 1} aria-label={`Move ${snapshot.name} later`}>↓</button><button type="button" onClick={() => deleteSavedWorkspace(snapshot)} aria-label={`Delete ${snapshot.name}`}>×</button></div>
                  </article>)}
                  {savedWorkspaces.length === 0 && <div className="map-utility-empty"><strong>No saved places yet</strong><p>Frame a useful map view, name it, and add it as the first investigation stop.</p></div>}
                </div>
                <aside className="map-utility-boundary" data-tone="privacy"><strong>Google Earth–inspired, KFM-governed.</strong><p>Places are stored only in this browser. A browser-location-derived camera is replaced with the generalized Kansas view. Stops do not upload geometry, admit sources, create EvidenceBundles, or authorize release or publication.</p></aside>

          </section>

          <div className="layer-panel-controls" hidden={leftPanelMode !== "layers" && leftPanelMode !== "live"}>
            <nav className="layer-source-switch" aria-label="Layer views">
              <button type="button" aria-pressed={!sourceStatusOpen && starterPanelOpen} data-active={!sourceStatusOpen && starterPanelOpen} onClick={() => { setSourceStatusOpen(false); setStarterPanelOpen(true); }}>Start here</button>
              {([["official", "Browse"], ["selected", "On map"], ["local", "Imagery"]] as const).map(([id, label]) => <button key={id} type="button" aria-pressed={!sourceStatusOpen && !starterPanelOpen && layerCatalogView === id} data-active={!sourceStatusOpen && !starterPanelOpen && layerCatalogView === id} data-layer-view={id} onClick={() => { setSourceStatusOpen(false); setStarterPanelOpen(false); setLayerCatalogView(id); setOfficialCatalogFilter("all"); leftPanelRef.current?.querySelector<HTMLElement>(".layer-catalog-body:not([hidden])")?.scrollTo(0, 0); }}>{label}{id === "selected" && <span>{selectedMapLayerCount}</span>}</button>)}
              <button type="button" aria-pressed={sourceStatusOpen} data-active={sourceStatusOpen} onClick={event => openSourceStatus(event.currentTarget)}>Source status{sourceIssues.length > 0 && <span>{sourceIssues.length}</span>}</button>
            </nav>
            <label className="catalog-search" hidden={sourceStatusOpen || starterPanelOpen}><span aria-hidden="true">⌕</span><span className="sr-only">Search map layers</span><input type="search" aria-label="Search map layers" value={officialSourceQuery} onChange={event => setOfficialSourceQuery(event.target.value)} placeholder="Search layers, places, providers…" />{officialSourceQuery && <button type="button" aria-label="Clear layer search" onClick={() => setOfficialSourceQuery("")}>×</button>}</label>

          </div>

          {sourceStatusOpen && (leftPanelMode === "layers" || leftPanelMode === "live") && <aside ref={sourceStatusPanelRef} id="map-source-status" className="map-source-status layer-source-status" aria-label="Source status and data quality">
            <header><h2>Source status</h2><button type="button" onClick={() => closeSourceStatus()} aria-label="Back to layers">← Layers</button></header>
            <p>Today · {baselineDay} UTC. Live observations refresh as providers publish. County counts keep their Census edition, and historical gaps remain visible.</p>
            <nav className="source-status-scope" aria-label="Source status scope"><button type="button" aria-pressed={sourceStatusScope === "selected"} onClick={() => setSourceStatusScope("selected")}>On map · {visibleOfficialCount}</button><button type="button" aria-pressed={sourceStatusScope === "all"} onClick={() => setSourceStatusScope("all")}>All sources · {OFFICIAL_CONTEXT_SOURCES.length}</button></nav>
            <button type="button" onClick={(event) => openMapUtility("connections", event.currentTarget)}>Connection details</button>
            <div className="source-quality-actions"><Link href="/earth-engine">Earth Engine datasets & recipes</Link></div>
            <button type="button" onClick={refreshVisibleOfficialContext} disabled={!buildYearCurrent || officialRefreshPlan.count === 0 || officialLoadingCount > 0}>{!buildYearCurrent ? "Rebuild required for current sources" : officialRefreshPlan.reason === "historical" ? `Current sources held until ${formatTimelineStep(OFFICIAL_CONTEXT_PRESENT_FRAME)}` : officialLoadingCount > 0 ? "Refreshing selected sources…" : officialRefreshPlan.count === 0 ? "Select a current source to refresh" : `Refresh ${officialRefreshPlan.count} selected source${officialRefreshPlan.count === 1 ? "" : "s"}`}</button>
            <LayerSourceNotices issues={sourceIssues} onRetry={retryOfficialLayer} onHide={id => setOfficialContextVisible(id, false)} />
            <HostedSourceStatus />
            {OFFICIAL_CONTEXT_SOURCES.filter(source => sourceStatusScope === "all" || officialVisibility[source.id]).map((source) => <SourceQualityRow key={source.id} source={source} state={officialStates[source.id]} payload={officialPayloads[source.id as OfficialContextFeedId]} error={officialErrors[source.id]} selected={officialVisibility[source.id]} held={officialVisibility[source.id] && !effectiveOfficialVisibility[source.id]} viewZoom={view.zoom} archiveDay={officialArchiveDays[source.id as OfficialContextFeedId]} observedAt={source.id === "noaa-lightning-density" ? lightningFrame : null} checkedAt={source.id === "noaa-lightning-density" ? lightningManifest?.retrievedAt : null} onToggle={(selected) => setOfficialContextVisible(source.id, selected)} onRetry={() => retryOfficialLayer(source.id)} />)}
            <Link href="/observatory/sources">Historical coverage & sources ↗</Link>
          {sourceStatusOpen && scenePreset === "elevation-3d" && <aside className="terrain-scene-passport" data-state={terrainState.toLowerCase()} aria-label="Terrain scene passport">
            <header>
              <div><span>TERRAIN SCENE PASSPORT</span><strong>DEM relief</strong></div>
              <b>{terrainState === "READY" ? "DEM READY" : terrainState === "ERROR" ? "DEM UNAVAILABLE" : "LOADING DEM"}</b>
            </header>
            <dl>
              <div><dt>Vertical scale</dt><dd>{verticalExaggeration.toFixed(1)}× {verticalExaggeration === 1 ? "physical" : "display"}</dd></div>
              <div><dt>Camera</dt><dd>{Math.round(view.pitch)}° pitch · {Math.round((view.bearing + 360) % 360)}° bearing</dd></div>
              <div><dt>Carrier</dt><dd>{terrainState === "READY" && attachedTerrainProviderRef.current === terrainProvider ? "Attached: " : "Selected: "}{terrainProvider === "usgs-3dep" ? "USGS 3DEP DEM" : "Mapzen Terrarium DEM"}{terrainProvider === "mapzen" && view.zoom > TERRARIUM_RENDER_MAX_ZOOM ? ` · overzoomed from z${TERRARIUM_RENDER_MAX_ZOOM}` : ""}</dd></div>
              <div><dt>Evidence</dt><dd>Display context only</dd></div>
            </dl>
            <p>Relief is observed from the renderer. Vertical datum, analytical spacing, and KFM source admission are not asserted.</p>
            <div className="terrain-passport-actions">
              <button type="button" aria-pressed={topographicOverlay} onClick={toggleTopographicHeightOverlay}>{topographicOverlay ? "Hide height colors" : "Show height colors"}</button>
              <button type="button" onClick={startTerrainInvestigation}>Profile a transect</button>
              <button type="button" onClick={() => openMapUtility("scene")}>Inspect terrain method</button>
            </div>
            <output className="terrain-cursor-reading" aria-live="polite">{terrainElevationReading ? <><strong>{terrainElevationReading.feet.toFixed(0)} ft</strong><span>{terrainElevationReading.meters.toFixed(0)} m · unexaggerated {terrainElevationReading.provider === "usgs-3dep" ? "USGS 3DEP" : "Mapzen"} DEM</span></> : <span>{terrainElevationUnavailable ? "No DEM height available at pointer" : "Move over the map to read DEM elevation"}</span>}</output>
          </aside>}
          <aside hidden={!sourceStatusOpen} className="map-legend-dock" aria-label="Visible map legend">
            <header>
              <div><span>SELECTED LAYERS</span><strong>{visibleCount} domain · {visibleOfficialCount} sources · {selectedEarthEngineCount} snapshots</strong></div>
              <button type="button" onClick={(event) => openAtlasPanel("layers", event.currentTarget)}>Manage</button>
            </header>
            <div className="map-legend-list">
              {activeLayers.slice(0, 5).map((layer) => <div className="map-legend-row" key={layer.id}>
                <label className="visibility-switch quick-legend-toggle" title={`Hide ${layer.title}`}>
                  <input type="checkbox" checked={visibility[layer.id]} aria-label={`Hide ${layer.title}`} onChange={(event) => setVisibility((current) => ({ ...current, [layer.id]: event.target.checked }))} />
                  <span aria-hidden="true" />
                </label>
                <button type="button" onClick={(event) => inspectLayer(layer, event.currentTarget)} title={`Inspect ${layer.title}`}>
                  <i className={`legend-swatch ${layer.legend[0].shape}`} style={{ "--swatch": layer.legend[0].color } as React.CSSProperties} aria-hidden="true" />
                  <span><strong>{layer.title}</strong><small>{layer.releaseState} · {layer.releaseTime}</small></span>
                </button>
              </div>)}
              {activeLayers.length === 0 && <p>{visibleOfficialCount ? `${visibleOfficialCount} official context sources selected; connection states and record counts appear above.` : "No layers selected. Open Layer Catalog to choose a starting stack."}</p>}
            </div>
            {activeLayers.length > 5 && <footer>+{activeLayers.length - 5} more in Layer Catalog</footer>}
            <p className="map-legend-note">{isCategoryBasemapKey(basemap) ? CATEGORY_BASEMAPS[basemap].legend : basemap === "standard" ? "OpenFreeMap vector context · counties, places, roads, rail, water, and labels are display context; KFM overlays remain explicit." : basemap === "kansas-aerial" ? "Kansas NG911 aerial imagery · February–April 2024 · approximately 1 foot · display context, not KFM evidence. Local flight date unresolved; independent of map time." : basemap === "imagery" ? "Satellite imagery and provider-backed overlays are display context only." : basemap === "streets" ? "OpenStreetMap reference and provider-backed overlays are display context only." : basemap === "topo" ? "USGS The National Map topographic tiles are display context only · KFM evidence remains separate." : "Site-local display style and provider-backed overlays are display context only."}</p>
          </aside>
          </aside>}

          <div className="layer-catalog-body starter-panel-body" hidden={!starterPanelOpen || sourceStatusOpen || leftPanelMode !== "layers" && leftPanelMode !== "live"}>
            <MapStartersControl sources={OFFICIAL_CONTEXT_SOURCES} access={starterAccess} visibility={officialVisibility} selectionReady={layerPreferencesReady}
              sourceStatus={id => officialVisibility[id] ? catalogDisplayStatus(officialCatalogStatuses[id])
                : officialStates[id] === "idle" ? "Available to request · response not checked" : `Not selected · ${officialStates[id]}`}
              onApply={applyStarterContext}
              onRetry={retryOfficialLayer}
              onUse2D={() => chooseSceneView("2d")}
              onChooseTime={() => { setTimelineOpen(true); setLeftOpen(false); announce("Choose a supported map time; source dates stay separate"); }}
              onBrowse={() => { setStarterPanelOpen(false); setLayerCatalogView("selected"); window.requestAnimationFrame(() => leftPanelRef.current?.querySelector<HTMLButtonElement>('[data-layer-view="selected"]')?.focus()); }} />
          </div>
          <div className="layer-catalog-body" hidden={starterPanelOpen || sourceStatusOpen || leftPanelMode !== "layers" && leftPanelMode !== "live"}>
          <div className="layer-browse-context"><TopicSelect label="Layer topic" value={officialWorkspace} onChange={topic => { setOfficialWorkspace(topic); setOfficialCatalogFilter("all"); }} /><span role="status">{layerCatalogView === "selected" ? `${matchingCatalogEntries.length} of ${selectedMapLayerCount} selected` : `${matchingCatalogEntries.length} ${matchingCatalogEntries.length === 1 ? "layer" : "layers"}`}</span></div>
          <div className="layer-topic-index"><Link href="/topics">Explore subjects &amp; coverage ↗</Link>{officialWorkspace !== "all" && <button type="button" onClick={() => setOfficialWorkspace("all")}>Clear topic</button>}</div>
          <TopicGuide value={officialWorkspace} onTool={(view, element) => openMapUtility(view, element)}
            mapLook={activeCategoryMap ? { name: activeCategoryMap.name, lede: activeCategoryMap.lede, sceneLabel: categorySceneLabel(activeCategoryMap.scene), swatch: activeCategoryMap.swatch, active: activeCategoryMap.basemap === basemap } : null}
            onOpenMap={activeCategoryMap ? () => openCategoryMap(activeCategoryMap.topic) : undefined} />
          {officialWorkspace === "transport" && <TransportHistoryControl map={mapRef.current} mapReady={styleReady} date={calendarSweep ? calendarFrameDay(calendarSweep) : temporalQuery.frame >= 1000 && temporalQuery.frame <= 9999 ? `${temporalQuery.frame}-01-01` : null} reducedMotion={reducedMotion} animate={dynamicEffects} />}
          {layerCatalogView === "selected" && <p className="layer-selection-note">Availability is shown on each layer.</p>}
          {matchingCatalogEntries.length === 0 && <div className="catalog-empty" role="status"><strong>{layerCatalogView === "selected" && selectedMapLayerCount === 0 ? "Start with a layer" : "No matching layers"}</strong><p>{layerCatalogView === "selected" && selectedMapLayerCount === 0 ? "Browse topics and switch on a layer to build your map." : "Try another topic or search. Your map selections are unchanged."}</p><button type="button" onClick={() => { setOfficialSourceQuery(""); setOfficialWorkspace("all"); setOfficialCatalogFilter("all"); if (layerCatalogView === "selected" && selectedMapLayerCount === 0) setLayerCatalogView("official"); }}>{selectedMapLayerCount === 0 && layerCatalogView === "selected" ? "Browse layers" : "Reset filters"}</button></div>}

          <div className="layer-map-time" data-historical={!buildYearCurrent || year !== OFFICIAL_CONTEXT_PRESENT_FRAME}>
            <span><span aria-hidden="true">◷</span> Map time · <strong>{temporalScopeLabel}</strong>{!buildYearCurrent ? " · build year differs from UTC year" : ""}{withheldOfficialCount > 0 ? ` · ${withheldOfficialCount} current source${withheldOfficialCount === 1 ? "" : "s"} held` : ""}</span>
            <button type="button" onClick={() => { setTimelineOpen(true); setLeftOpen(false); setRightOpen(false); dismissMapUtilityWithoutFocus(); announce(`Opened the map timeline at ${temporalScopeLabel}`); }}>Change time</button>
          </div>




          <section className="official-context-catalog" id="official-context-catalog" tabIndex={-1} hidden={layerCatalogView === "local"} aria-labelledby="official-context-title">
            <h2 id="official-context-title" className="sr-only">Map layers</h2>

            <div className="official-context-list">{filterOfficialSources(OFFICIAL_CONTEXT_SOURCES, "all", "").map((source) => {
              const state = officialStates[source.id];
              const heldAtFrame = officialVisibility[source.id] && !effectiveOfficialVisibility[source.id];
              const minimumZoom = sourceMinimumZoom(source);
              const needsFlatMap = officialVisibility[source.id] && !heldAtFrame && projection === "globe" && (source.kind === "OPERATIONAL_WMS" || source.kind === "HISTORICAL_RASTER");
              const needsCloserView = !needsFlatMap && sourceNeedsCloserView(source, officialVisibility[source.id], heldAtFrame, state, view.zoom);
              const riverArchiveSpan = streamflowCoverage?.station === streamflowSelectedStationId && !streamflowCoverage.partial ? streamflowCoverage.continuous : null;
              const riverArchiveMinDay = riverArchiveSpan?.start.slice(0, 10);
              const riverArchiveMaxDay = riverArchiveSpan ? [currentUtcDay(), riverArchiveSpan.end.slice(0, 10)].sort()[0] : undefined;
              return <article key={source.id} hidden={!listedOfficialSources.some(item => item.id === source.id)} className="official-context-row" data-state={state} data-visible={officialVisibility[source.id]} data-held={heldAtFrame}>
                    <div className="official-context-primary"><label className="visibility-switch"><input type="checkbox" checked={officialVisibility[source.id]} aria-label={`${officialVisibility[source.id] ? "Hide" : "Show"} ${source.title}`} onChange={(event) => setOfficialContextVisible(source.id, event.target.checked)} /><span aria-hidden="true" /></label><i style={{ "--swatch": source.color } as React.CSSProperties} /><div><strong>{source.title}</strong><small>{source.organization}{source.kind === "HISTORICAL_RASTER" ? " · historical composite" : ""}{source.id === "noaa-goes-geocolor" && noaaSatelliteManifest ? ` · ${noaaSatelliteManifest.product === "visible" ? "GOES visible fallback" : "GeoColor"}` : ""} · {catalogDisplayStatus(officialCatalogStatuses[source.id])}</small></div></div>
                {officialVisibility[source.id] && state === "loading" && source.apiPath && <small role="status">{officialReadPhases[source.id] === "queued" ? "Waiting for a loading slot…" : "Receiving source data…"} You can hide this layer to cancel.</small>}
                {officialVisibility[source.id] && state === "error" && <div className="layer-request-recovery">
                  <p role="alert">{officialArchiveDays[source.id as OfficialContextFeedId] ? `Could not load ${officialArchiveDays[source.id as OfficialContextFeedId]} UTC.` : "Could not load source data."} {source.apiPath ? "This layer has no data on the map." : "Check Source quality for the failure and any retained observations."} Try again or hide it.</p>
                  <button type="button" disabled={heldAtFrame} onClick={(event) => {
                    // The recovery button disappears after retry; keep keyboard
                    // focus on this layer's stable control throughout acquisition.
                    event.currentTarget.closest("article")?.querySelector<HTMLInputElement>('input[type="checkbox"]')?.focus({ preventScroll: true });
                    retryOfficialLayer(source.id);
                  }}>Retry layer</button>
                </div>}
                <span hidden={!officialVisibility[source.id]} className={researchStyles.status}>Source time: {officialArchiveDays[source.id as OfficialContextFeedId] ? `${officialArchiveDays[source.id as OfficialContextFeedId]} UTC` : source.freshness}</span>
                {(needsCloserView || needsFlatMap || heldAtFrame) && <div className="reference-layer-guidance">
                  <small>{heldAtFrame ? "This source is held at the selected map year." : needsFlatMap ? "This regional image layer requires the flat map." : `Visible at zoom ${minimumZoom}+ · your view ${view.zoom.toFixed(1)}. Source dates vary.`}</small>
                  {heldAtFrame && buildYearCurrent && <button type="button" onClick={() => { setPlaying(false); commitTemporalFrame(OFFICIAL_CONTEXT_PRESENT_FRAME, "Returned to Present; each layer retains its own source dates"); }}>Use Present</button>}
                  {needsFlatMap && <button type="button" onClick={() => activateMapRepresentation("2d")}>Use flat map</button>}
                  {needsCloserView && <button type="button" onClick={() => { const map = mapRef.current; if (!map) return; const center = map.getCenter(); const inKansasView = center.lng >= -102.06 && center.lng <= -94.58 && center.lat >= 36.99 && center.lat <= 40.01; map.easeTo({ zoom: minimumZoom + 0.5, ...(inKansasView ? {} : { center: [-98.3, 38.5] as [number, number] }), duration: reducedMotion ? 0 : 600 }); announce(`Zooming to ${source.shortTitle}; provider coverage may still contain gaps`); }}>Zoom to layer</button>}
                </div>}
                {officialVisibility[source.id] && source.kind !== "MODEL_CANVAS" && <label className="opacity-control"><span>Opacity <b>{Math.round(officialOpacity[source.id] * 100)}%</b></span><input aria-label={`${source.shortTitle} opacity`} type="range" min="0" max="100" value={Math.round(officialOpacity[source.id] * 100)} onChange={(event) => setOfficialContextOpacity(source.id, Number(event.target.value) / 100)} /></label>}
                <details className="official-context-options"><summary>Details &amp; controls</summary><div className="official-context-option-body">                {source.id === "nws-radar" && <div className="noaa-radar-launch" aria-label="NOAA radar playback">
                  <strong>Watch radar over time</strong>
                  <p>Live nowCOAST scans use their exact observation times. Choose an older UTC day to watch NOAA/NWS-derived archive mosaics in Event Observatory.</p>
                  <div>
                    <button type="button" onClick={watchRadarLoop}>Watch live loop</button>
                    <label>Archive UTC day<input type="date" min="1995-01-01" max={currentUtcDay()} value={radarArchiveDraftDay} onInput={(event) => setRadarArchiveDraftDay(event.currentTarget.value)} onChange={(event) => setRadarArchiveDraftDay(event.target.value)} /></label>
                    <Link href={`/observatory?start=${encodeURIComponent(`${radarArchiveDraftDay || currentUtcDay()}T00:00`)}&hours=24&layers=radar,counties&replay=radar`}>Watch selected day ↗</Link>
                  </div>
                  <small>Archive coverage is checked after opening; unavailable dates and missing scans are shown as gaps, not clear weather.</small>
                  <label className="map-visual-control">Radar image display<select aria-label="Radar image display" value={noaaRadarSmooth ? "smooth" : "exact"} onChange={event => setNoaaRadarSmooth(event.target.value === "smooth")}><option value="exact">Exact pixels</option><option value="smooth">Smooth image</option></select></label>
                  <small>Spatial smoothing changes only drawn pixels; scan times and source data stay exact.</small>
                </div>}
                {(source.id === "nasa-firms-active-fire" || source.id === "nasa-gibs-fire-points") && <p className="thermal-context-note"><strong>NASA THERMAL CONTEXT · NOT KFM EVIDENCE</strong><span>{source.id === "nasa-firms-active-fire" ? "Provider-default daily raster; its exact UTC image date is unresolved." : "One checked UTC image day; each returned point keeps its own acquisition time."} Thermal anomalies do not confirm a wildfire incident, and blank coverage is not an all-clear.</span></p>}
                {source.id === "nasa-gibs-fire-points" && <label className="map-visual-control map-fire-visual-control">Detection display<select aria-label="Fire detection display" value={fireVisualMode} onChange={event => setFireVisualMode(event.target.value as "exact" | "soft")}><option value="exact">Exact point halos</option><option value="soft">Soft visual halos</option></select><small>Visual halos do not change selectable points, acquisition times, or report records. NASA display context · not KFM evidence.</small></label>}


                {source.legend && <p className="reference-layer-legend"><i style={{ backgroundColor: source.color }} aria-hidden="true" />{source.legend}</p>}
                {isBridgeLayer(source.id) && <BridgeRecordInspector layer={source.id} mapRef={mapRef} enabled={Boolean(effectiveOfficialVisibility[source.id]) && projection !== "globe" && styleReady} reducedMotion={reducedMotion} />}
                {isBlmPlssLayer(source.id) && <BlmPlssInspector layer={source.id} mapRef={mapRef} enabled={Boolean(effectiveOfficialVisibility[source.id]) && projection !== "globe" && styleReady} />}
                {GROUNDWATER_MANIFEST.find(item => item.id === source.id)?.legend.map(item => <p className="reference-layer-legend" key={item.value}><i style={{ backgroundColor: item.color }} aria-hidden="true" />{item.label} ft</p>)}
                {source.id.startsWith("kgs-") && <small>{source.freshness}. {source.cadence}.</small>}
                {source.legendUrl && <a href={source.legendUrl} target="_blank" rel="noreferrer">Provider legend ↗</a>}
                {source.id === "fema-flood-zones" && <a href="https://msc.fema.gov/portal/home" target="_blank" rel="noreferrer">Check effective FEMA map and amendments ↗</a>}
                {source.id === "usgs-3dep-slope" && <small className="terrain-layer-key">USGS slope colors: gray flatter · yellow shallow · red-brown steeper. This is visual context, not a slope measurement.</small>}
                <section className="source-time-control" aria-label={`${source.shortTitle} time controls`}>
                  <header><span>TIME · {source.id === "nasa-lightning-climatology" ? "HISTORICAL COMPOSITE" : source.id === "usgs-streamflow" || source.id === "nws-radar" || source.id === "noaa-goes-geocolor" || source.id === "noaa-lightning-density" ? "EXACT SOURCE FRAMES" : source.id === "census-counties" ? "2020 EDITION" : "SOURCE CLOCK"}</span><strong>{source.id === "nasa-lightning-climatology" ? "1995–2014" : source.id === "noaa-lightning-density" ? "15-MIN DENSITY" : source.id === "usgs-streamflow" && streamflowArchiveDay ? `${streamflowArchiveDay} UTC` : officialArchiveDays[source.id as OfficialContextFeedId] ? `${officialArchiveDays[source.id as OfficialContextFeedId]} UTC` : source.id === "nws-radar" ? "RECENT LOOP" : source.id === "noaa-goes-geocolor" ? "ROLLING 24 HOURS" : "CURRENT / PINNED"}</strong></header>
                  {source.id === "usgs-streamflow" ? <>
                    <p>{streamflowArchiveDay ? "Selected UTC day · every returned observation time" : "Loaded River Pulse window · bounded sample of exact times. Station points may use a prior sample within the declared 30-minute tolerance."}{streamflowBundle ? ` · ${streamflowBundle.observations.length.toLocaleString("en-US")} observations${streamflowBundle.truncated ? " · PARTIAL / TRUNCATED" : ""}` : streamflowState === "loading" ? " · checking source" : " · no loaded frame"}</p>
                    <input type="range" min="0" max={Math.max(0, streamflowFrames.length - 1)} value={Math.max(0, safeStreamflowFrameIndex)} disabled={streamflowFrames.length < 2 || streamflowState === "loading" || !officialVisibility[source.id] || heldAtFrame} onChange={(event) => seekStreamflow(Number(event.target.value))} aria-label="River Pulse exact observation time" aria-valuetext={streamflowFrameTime ? `${streamflowFrameTime} UTC observation cursor` : "No confirmed observation"} />
                    <output>{streamflowFrames.length > 0 && streamflowFrameTime ? `${streamflowFrameTime.slice(0, 19).replace("T", " ")} UTC · frame ${safeStreamflowFrameIndex + 1}/${streamflowFrames.length}` : streamflowState === "error" ? "Source unavailable · no archive point displayed" : "No observed frame loaded"}</output>
                    <small>{streamflowBundle ? `Loaded ${streamflowBundle.query.start.slice(0, 10)} → ${streamflowBundle.query.end.slice(0, 10)} UTC; this is the checked request window, not the station’s full record.` : "Choose a station to check an older day. Provider coverage differs by station."}</small>
                    <small>{streamflowCoverage?.continuous ? `Station continuous record: ${streamflowCoverage.continuous.start.slice(0, 10)} → ${streamflowCoverage.continuous.end.slice(0, 10)} UTC${streamflowCoverage.partial ? " · partial metadata" : ""}. Gaps may occur within this span.${streamflowCoverage.daily ? ` Daily means start ${streamflowCoverage.daily.start.slice(0, 10)}; inspect that older resolution in Observatory.` : ""}` : streamflowCoverage?.daily ? `No continuous span declared in this response. Daily mean record starts ${streamflowCoverage.daily.start.slice(0, 10)}; daily values are not intraday frames.` : streamflowCoverageMessage}</small>
                    <div className="source-time-actions"><label>Station<select value={streamflowSelectedStationId ?? ""} onChange={(event) => selectStreamflowStation(event.target.value || null)}><option value="">Choose a loaded station</option>{streamflowSelectedStationId && !(streamflowBundle?.stations ?? []).some((station) => station.stationId === streamflowSelectedStationId) && <option value={streamflowSelectedStationId}>{streamflowSelectedStationId} · selected</option>}{(streamflowBundle?.stations ?? []).map((station) => <option key={station.stationId} value={station.stationId}>{station.name} · {station.stationId}</option>)}</select></label><label>Older UTC day<input type="date" value={streamflowArchiveDraftDay} min={riverArchiveMinDay} max={riverArchiveMaxDay ?? currentUtcDay()} aria-invalid={Boolean(streamflowArchiveDraftDay && !validStreamflowArchiveDay(streamflowArchiveDraftDay, riverArchiveMaxDay ?? currentUtcDay()))} aria-describedby={streamflowArchiveDraftDay && !validStreamflowArchiveDay(streamflowArchiveDraftDay, riverArchiveMaxDay ?? currentUtcDay()) ? "river-archive-day-guidance" : undefined} onChange={(event) => setStreamflowArchiveDraftDay(event.target.value)} /></label><button type="button" disabled={!streamflowSelectedStationId || !validStreamflowArchiveDay(streamflowArchiveDraftDay, riverArchiveMaxDay ?? currentUtcDay()) || heldAtFrame || streamflowState === "loading" && streamflowArchiveDraftDay === streamflowArchiveDay} onClick={loadStreamflowArchiveDay}>Check day on map</button>{streamflowArchiveDay && <button type="button" onClick={() => void refreshStreamflow("24h", null)}>Recent network</button>}<Link href={`/observatory?start=${encodeURIComponent(`${streamflowArchiveDraftDay || streamflowArchiveDay || currentUtcDay()}T00:00`)}&hours=24&layers=river,counties${streamflowSelectedStationId ? `&station=${encodeURIComponent(streamflowSelectedStationId)}` : ""}`}>Full station archive ↗</Link></div>
                    {streamflowArchiveDraftDay && !validStreamflowArchiveDay(streamflowArchiveDraftDay, riverArchiveMaxDay ?? currentUtcDay()) && <small id="river-archive-day-guidance" role="status">Choose a valid UTC day from 1800 through {riverArchiveMaxDay ?? currentUtcDay()}; station coverage may be shorter.</small>}
                    {riverArchiveMinDay && riverArchiveMaxDay && <ArchiveDaySlider sourceLabel="River Pulse" minDay={riverArchiveMinDay} maxDay={riverArchiveMaxDay} day={streamflowArchiveDraftDay} onSelect={setStreamflowArchiveDraftDay} nextAction="Check day on map" />}
                  </> : source.id === "noaa-goes-geocolor" ? <>
                    <p>{noaaSatelliteManifest ? `${noaaSatelliteManifest.frameCount} dated ${noaaSatelliteManifest.product === "geocolor" ? "GOES GeoColor" : "GOES visible fallback"} images · latest ${drawerTimestamp(noaaSatelliteManifest.frames.at(-1)!.observedAt)}${noaaSatelliteManifest.freshness === "delayed" ? " · DELAYED" : ""}${noaaSatelliteManifest.partial ? " · PARTIAL CATALOG" : ""}` : state === "loading" ? "Checking NOAA image times…" : "No dated NOAA image catalog loaded."}</p>
                    <input type="range" min="0" max={Math.max(0, (noaaSatelliteManifest?.frameCount ?? 0) - 1)} value={Math.max(0, noaaSatelliteManifest?.frames.findIndex((frame) => frame.kind === noaaSatelliteFrame?.kind && frame.observedAt === noaaSatelliteFrame.observedAt) ?? 0)} disabled={!noaaSatelliteManifest || noaaSatelliteManifest.frameCount < 2 || state === "loading" || !officialVisibility[source.id] || heldAtFrame} onChange={(event) => { const frame = noaaSatelliteManifest?.frames[Number(event.target.value)]; if (frame) selectNoaaSatelliteFrame(frame); }} aria-label="NOAA satellite exact image frame" aria-valuetext={noaaSatelliteFrame ? `${noaaSatelliteFrame.observedAt} image time` : "No dated image selected"} />
                    <output>{noaaSatelliteFrame ? noaaSatelliteFrame.kind === "geocolor" ? `Selected GeoColor image: ${drawerTimestamp(noaaSatelliteFrame.observedAt)} → ${drawerTimestamp(noaaSatelliteFrame.validThrough)} · raster ${noaaSatelliteFrame.objectId} · ${state.toUpperCase()}` : `Selected GOES visible observation: ${drawerTimestamp(noaaSatelliteFrame.observedAt)} · ${state.toUpperCase()}` : "No image selected"}</output>
                    <small>{noaaSatelliteManifest ? `Catalog checked ${drawerTimestamp(noaaSatelliteManifest.retrievedAt)}. ${noaaSatelliteManifest.product === "visible" ? "GeoColor is unavailable; this is daylight-dependent GOES visible imagery from NOAA nowCOAST." : "GeoColor imagery is locked to the selected NOAA raster ID."} Older selected frames are not live. This is visual cloud context, not a fire or smoke finding.` : "A dated source image is required before any tile is shown. NOAA imagery is informational."}</small>
                    <div className="source-time-actions"><button type="button" disabled={!noaaSatelliteManifest || state === "loading"} onClick={() => { const latest = noaaSatelliteManifest?.frames.at(-1); if (latest) selectNoaaSatelliteFrame(latest); }}>Newest image</button><button type="button" disabled={state === "loading" || heldAtFrame} onClick={() => void refreshNoaaSatelliteFrames()}>Refresh frames</button><a href="https://www.nesdis.noaa.gov/imagery/satellite-maps/earth-real-time" target="_blank" rel="noreferrer">NOAA Earth in Real-Time ↗</a><a href="https://satellitemaps.nesdis.noaa.gov/arcgis/rest/services/MERGEDGC_Last_24hr/ImageServer" target="_blank" rel="noreferrer">GeoColor catalog ↗</a>{noaaSatelliteManifest?.product === "visible" && <a href="https://nowcoast.noaa.gov/" target="_blank" rel="noreferrer">NOAA nowCOAST ↗</a>}</div>
                  </> : source.id === "nws-radar" ? <>
                    <p>{noaaRadarManifest ? `${noaaRadarLoopFrames.length} exact scans in ${noaaRadarLoopSpan === "all" ? "the full NOAA live window" : `the selected ${noaaRadarLoopSpan}-minute loop`} · ${noaaRadarManifest.gapCount} detected gaps` : noaaRadarManifestState === "loading" ? "Checking NOAA frames" : "No verified radar manifest loaded"}</p>
                    <input type="range" min="0" max={Math.max(0, noaaRadarLoopFrames.length - 1)} value={Math.max(0, noaaRadarFrameIndex)} disabled={!noaaRadarRenderable || noaaRadarLoopFrames.length < 2 || noaaRadarFrameLoadState === "loading" || !officialVisibility[source.id] || heldAtFrame} onChange={(event) => { const index = Number(event.target.value); const frame = noaaRadarLoopFrames[index]; if (!frame) return; setNoaaRadarPlaying(false); setNoaaRadarFollowLatest(index === noaaRadarLoopFrames.length - 1); applyNoaaRadarFrame(frame); }} aria-label="NOAA radar exact scan time" aria-valuetext={noaaRadarActiveFrame ?? "No confirmed radar scan"} />
                    <output>{noaaRadarFrameTime ? `${noaaRadarFrameTime.slice(0, 19).replace("T", " ")} UTC · ${noaaRadarFrameLoadState === "loading" ? "loading" : noaaRadarDisplayState.toLowerCase()}` : "No confirmed scan rendered"}</output>
                    <small>Rolling confirmed scans only. Older radar days open in the separate Event Observatory map; they are not replayed on this map.</small>
                    <small>Choose an archive UTC day in the playback controls above. 1995 is the archive adapter’s earliest query bound, not proof that every day has radar imagery. Older days use a separate map and source.</small>
                  </> : source.id === "noaa-lightning-density" ? <div className="lightning-source-control" data-signal={lightningPreview}>
                    <p>Ground-network strike density in 8 × 8 km cells for each advertised 15-minute interval.</p>
                    <output>{lightningFrame ? `Selected frame ${lightningFrame.slice(0, 16).replace("T", " ")} UTC` : "No NOAA frame loaded"}</output>
                    <button type="button" onClick={() => { setLiveInstrument("lightning"); setInstrumentOpen(true); }} disabled={!officialVisibility[source.id] || heldAtFrame}>Open lightning controls on map</button>
                    <button type="button" onClick={() => { setGlmFlashesEnabled(true); setInstrumentOpen(false); }} disabled={!glmFlashesAllowed}>Open observed satellite flash loop</button>
                    <small>Exact time, playback, source status, and legend are in the map controls.</small>
                  </div> : source.id === "nasa-lightning-climatology" ? <div className="lightning-climate-control">
                    <p>NASA LIS/OTD combined flash-rate climatology from 1995–2014. This broad 0.5° climate field does not show fine local variation, this storm, or today’s lightning.</p>
                    <output>Fixed multi-year composite · no event playback</output>
                    <small>GIBS WMTS date 1995-05-04 is a tile carrier key, not a single observed lightning event.</small>
                    <button type="button" onClick={() => { setOfficialContextVisible("nasa-lightning-climatology", false); setOfficialContextVisible("noaa-lightning-density", false); setGlmFlashesEnabled(true); setInstrumentOpen(false); }} disabled={!glmFlashesAllowed}>Switch to timed lightning</button>
                    <small>Explore observed flashes in 15-minute, half-hour and hourly slices, or play individual pulses. Switching hides the climate average so it does not obscure the flashes. Use the year / month archive to select older dates and load a 15-minute, half-hour or hourly interval.</small>
                    {!glmFlashesAllowed && <small>Return to Present and use the flat map for observed flashes.</small>}
                    <a href={source.sourceUrl} target="_blank" rel="noreferrer">NASA GIBS collection metadata ↗</a>
                  </div> : source.id === "nifc-fire-reports" ? <>
                    <p>Interagency working incident reports discovered in Kansas during the last 30 days. A record confirms provider reporting; status, area, and cause can change. Satellite detections are compared only by proximity.</p>
                    <output>{!officialVisibility[source.id] ? "Report layer off." : heldAtFrame ? "Held by atlas year · Return to Present." : state === "loading" ? "Checking NIFC reports…" : state === "error" ? "NIFC reports unavailable · no substitute claims." : `${officialPayloads["nifc-fire-reports"]?.featureCount ?? 0} reports in the loaded response${state === "partial" ? " · partial" : ""}. No report is not an all-clear.`}</output>
                    <div className="source-time-actions"><button type="button" onClick={() => openPrimaryWorkspace("reports", true, buildFireReportContext("nifc-fire-reports", null, officialPayloads["nifc-fire-reports"]?.retrievedAt, officialPayloads["nifc-fire-reports"]?.state ?? "unavailable", officialPayloads["nasa-gibs-fire-points"]?.state ?? "unavailable", []))}>Build Kansas fire report</button><a href="https://inciweb.wildfire.gov/" target="_blank" rel="noreferrer">Browse InciWeb incident updates ↗</a><a href="https://www.nifc.gov/fire-information" target="_blank" rel="noreferrer">National fire news ↗</a></div>
                  </> : source.id === "noaa-hms-smoke" ? <HmsSmokePlayback sessionSignal={smokePlaybackSignal} enabled={Boolean(effectiveOfficialVisibility["noaa-hms-smoke"] && styleReady)} reducedMotion={reducedMotion} displayedDay={officialArchiveDays["noaa-hms-smoke"]} payload={officialPayloads["noaa-hms-smoke"]} onReserve={reserveSmokePlayback} onFrame={commitSmokePlayback} onCurrent={() => returnOfficialSourceToCurrent("noaa-hms-smoke")} /> : ["usgs-earthquakes", "nasa-gibs-fire-points", "raspberry-shake-stations"].includes(source.id) ? <>
                    <p>{source.id === "usgs-earthquakes" ? "Event timestamps; a checked day can be swept event by event." : source.id === "nasa-gibs-fire-points" ? "Selectable thermal detections for one exact UTC day; each point carries its own acquisition time. This is separate from the provider-default image layer." : "Station metadata valid for a checked date; no waveform time series on this map."}</p>
                    <div className="source-time-actions"><label>UTC archive day<input type="date" min={source.id === "nasa-gibs-fire-points" ? "2018-01-01" : undefined} max={currentUtcDay()} value={officialArchiveDraftDays[source.id as OfficialContextFeedId] ?? ""} onChange={(event) => setOfficialArchiveDraftDays((current) => ({ ...current, [source.id]: event.target.value }))} /></label><button type="button" disabled={!officialArchiveDraftDays[source.id as OfficialContextFeedId] || heldAtFrame || state === "loading" && officialArchiveDraftDays[source.id as OfficialContextFeedId] === officialArchiveDays[source.id as OfficialContextFeedId]} onClick={() => void loadOfficialArchiveDay(source.id as OfficialContextFeedId, officialArchiveDraftDays[source.id as OfficialContextFeedId]!)}>Check day on map</button>{officialArchiveDays[source.id as OfficialContextFeedId] && <button type="button" onClick={() => returnOfficialSourceToCurrent(source.id as OfficialContextFeedId)}>Current</button>}{source.id !== "nasa-gibs-fire-points" && <Link href={`/observatory?start=${encodeURIComponent(`${officialArchiveDraftDays[source.id as OfficialContextFeedId] || officialArchiveDays[source.id as OfficialContextFeedId] || currentUtcDay()}T00:00`)}&hours=24&layers=${source.id === "usgs-earthquakes" ? "earthquakes" : "shake"},counties`}>Open separate archive map ↗</Link>}</div>
                    <output>{officialArchiveDays[source.id as OfficialContextFeedId] ? state === "loading" ? "Checking day · old map features cleared" : state === "error" ? "Archive unavailable · map source empty" : !officialArchivePayloadsRef.current[source.id as OfficialContextFeedId] ? "Day not loaded · turn on layer to resume" : `${datedSourceDisplayStatus(officialArchivePayloadsRef.current[source.id as OfficialContextFeedId]?.featureCount ?? 0, officialPayloads[source.id as OfficialContextFeedId]?.featureCount ?? 0, officialArchiveDays[source.id as OfficialContextFeedId]!, officialVisibility[source.id], effectiveOfficialVisibility[source.id], styleReady)}${state === "partial" || officialPayloads[source.id as OfficialContextFeedId]?.truncated ? " · partial; missing coverage cannot be ruled out" : ""}` : !officialVisibility[source.id] ? "Current source off · Turn on layer to display." : heldAtFrame ? "Source held by atlas year · Return to Present to display." : source.id === "nasa-gibs-fire-points" ? `${officialPayloads["nasa-gibs-fire-points"]?.sourceDay ? `NASA image day ${officialPayloads["nasa-gibs-fire-points"]!.sourceDay} UTC` : "Current UTC day · check source"}${officialPayloads["nasa-gibs-fire-points"] ? ` · ${officialPayloads["nasa-gibs-fire-points"]!.featureCount} detections loaded${officialPayloads["nasa-gibs-fire-points"]!.state === "partial" ? " · partial" : ""}` : ""}; missing detections are not an all-clear.` : "Current source clock · earliest available day is checked per request."}</output>
                    {source.id === "usgs-earthquakes" && officialArchiveDays["usgs-earthquakes"] && <><input type="range" min="0" max={Math.max(0, earthquakeArchiveFrames.length - 1)} value={Math.max(0, earthquakeArchiveFrameIndex)} disabled={earthquakeArchiveFrames.length < 2 || state === "loading" || !officialVisibility[source.id] || heldAtFrame} onChange={(event) => seekEarthquakeArchiveFrame(Number(event.target.value))} aria-label="Earthquakes through exact event time on selected UTC day" aria-valuetext={earthquakeArchiveFrames[earthquakeArchiveFrameIndex] ?? "No event frame"} /><small>{earthquakeArchiveFrames.length ? `Events through ${earthquakeArchiveFrames[Math.max(0, earthquakeArchiveFrameIndex)].slice(11, 19)} UTC · ${Math.max(0, earthquakeArchiveFrameIndex + 1)}/${earthquakeArchiveFrames.length} returned event times. Empty intervals remain empty.` : officialArchivePayloadsRef.current["usgs-earthquakes"] ? "No returned event times for this checked day; no slider frame invented." : "Day not loaded; no event frame available."}</small></>}
                  </> : <p>{OFFICIAL_CONTEXT_TEMPORAL_SUPPORT[source.id].limitation} No selectable observation sweep is connected for this carrier.</p>}
                  {heldAtFrame && <small>Selected source is held by the global atlas year. Return that axis to Present to display its source clock.</small>}
                </section>
                {source.id === "nws-forecast-wind" && <div className="wind-arrow-source-card" data-state={windArrowState}>
                  <strong>Wind direction &amp; speed</strong>
                  <p>Open-Meteo NCEP GFS supplies the 10 m forecast speed and direction. Streamlines move toward the forecast direction; with motion off, arrows mark the model points. Wind-from bearings describe where wind comes from. Spacing and motion are illustrative, not measured particle paths.</p>
                  <output aria-live="polite">{!officialVisibility[source.id] ? "Turn on Wind direction & speed to show the forecast" : heldAtFrame ? "Held by atlas year" : windArrowState === "READY" && windArrowFrame ? `Valid ${windArrowFrame.validTimeUtc.replace("T", " ").slice(0, 16)} UTC · ${windArrowFrame.samples.length} model grid points · retrieved ${windArrowFrame.retrievedAtUtc.replace("T", " ").slice(0, 16)} UTC${windArrowDirect ? " · direct provider request" : " · Site adapter"} · ${reducedMotion ? "Direction arrows for reduced motion" : dynamicEffects ? "Streamlines moving with model direction" : "Direction arrows; ambient motion off"}` : windArrowState === "ERROR" ? "Model unavailable or outside Kansas · no wind flow drawn" : "Checking model direction and valid time…"}</output>
                  {windArrowState === "READY" && windArrowFrame && <details className="wind-arrow-samples">
                    <summary>Inspect model grid points</summary>
                    <label>Grid point<select value={windArrowSampleIndex} onChange={(event) => setWindArrowSampleIndex(Number(event.target.value))}>{windArrowFrame.samples.map((sample, index) => <option key={`${sample.latitude},${sample.longitude}`} value={index}>Point {index + 1} · {sample.latitude.toFixed(3)}° N, {Math.abs(sample.longitude).toFixed(3)}° W</option>)}</select></label>
                    {windArrowFrame.samples[windArrowSampleIndex] && <output aria-live="polite">{Math.round(windArrowFrame.samples[windArrowSampleIndex].speedMetersPerSecond * 2.23694)} mph toward {windToCompass(windArrowFrame.samples[windArrowSampleIndex].windToDegrees)} · from {windToCompass(windArrowFrame.samples[windArrowSampleIndex].windFromDegrees)}</output>}
                    <small>Forecast at the selected model grid point, valid {windArrowFrame.validTimeUtc.replace("T", " ").slice(0, 16)} UTC. Values between these points are not measured here.</small>
                  </details>}
                  <button type="button" onClick={() => setWindArrowReloadToken(value => value + 1)} disabled={!officialVisibility[source.id] || windArrowState === "LOADING" || heldAtFrame}>Refresh wind forecast</button>
                </div>}
                <div className="official-context-actions"><button type="button" onClick={event => openSourceStatus(event.currentTarget)}>Source details & quality</button>{needsCloserView && <button type="button" onClick={() => { mapRef.current?.easeTo({ zoom: minimumZoom + 0.25, duration: motionDuration(600) }); announce(`${source.shortTitle}: zoomed in to its display range`); }}>Zoom to view</button>}{["usgs-streamflow", "noaa-hms-smoke", "raspberry-shake-stations", "usgs-earthquakes", "nws-radar", "census-counties"].includes(source.id) && <Link href={`/observatory?layers=${({ "usgs-streamflow": "river", "noaa-hms-smoke": "smoke", "raspberry-shake-stations": "shake", "usgs-earthquakes": "earthquakes", "nws-radar": "radar", "census-counties": "counties" } as Record<string,string>)[source.id]},counties`}>Explore dated records ↗</Link>}</div>
                </div></details>
              </article>;
            })}</div>
            <section className="daylight-layer-card" hidden={!shownCatalogIds.has("daylight")} aria-label="Daylight and twilight controls">
              <header><div><strong>Daylight &amp; twilight</strong><small>Calculated solar geometry · {daylightEnabled ? styleReady ? "Selected" : "Selected · map loading" : "Off"}</small></div><label className="visibility-switch"><input type="checkbox" checked={daylightEnabled} aria-label={daylightEnabled ? "Hide Daylight and twilight" : "Show Daylight and twilight"} onChange={(event) => toggleDaylightVisibility(event.target.checked)} /><span aria-hidden="true" /></label></header>
              <details className="specialty-layer-details"><summary>Dates, playback &amp; details</summary><div className="official-context-option-body">
              <p>Estimated Sun position and twilight boundaries. This is not measured ground-level brightness.</p>
              <div className="daylight-date-range" aria-label="Kansas Central date range">
                <label>From<input type="date" aria-label="Daylight loop start date" value={daylightDay} max={daylightToday} onChange={(event) => selectDaylightStart(event.target.value)} /></label>
                <label>Through<input type="date" aria-label="Daylight loop end date" value={daylightThroughDay} min={daylightDay} max={daylightToday} onChange={(event) => selectDaylightThrough(event.target.value)} /></label>
              </div>
              <div className="daylight-clock-row"><button type="button" disabled={!daylightEnabled || reducedMotion} onClick={() => setDaylightPlayback(!daylightPlaying)}>{reducedMotion ? "Paused · reduced motion" : daylightPlaying ? "Pause" : "Resume"}</button><output aria-live="off" aria-label={`Kansas Central ${daylightDisplayTime.central}; ${daylightDisplayTime.utc}`}><strong>{daylightDisplayTime.central}</strong><small>{daylightDisplayTime.utc}</small></output></div>
              <label className="daylight-scrubber"><span className="sr-only">Solar time from {daylightDay} through {daylightThroughDay}, Kansas Central time</span><input type="range" min="0" max="10000" step="1" value={daylightSliderValue} disabled={!daylightEnabled} aria-valuetext={`${daylightDisplayTime.central}; ${daylightDisplayTime.utc}`} onChange={(event) => seekDaylight(Number(event.target.value) / 10_000)} /><span><span>{daylightDay} · midnight</span><span>{daylightRangeSummary}</span><span>{daylightThroughDay} · end</span></span></label>
              <small className="daylight-band-key"><i aria-hidden="true" /> Night <i aria-hidden="true" /> Astronomical twilight <i aria-hidden="true" /> Nautical twilight <i aria-hidden="true" /> Civil twilight · apparent sunrise/sunset</small>
              </div></details>
            </section>
            <div hidden={!shownCatalogIds.has("reviewed-water")}><GovernedWaterControl mapRef={mapRef} styleReady={styleReady} onSelectionChange={setReviewedWaterSelected} /></div>
            <div hidden={!shownCatalogIds.has("reviewed-weather")}><GovernedWeatherControl mapRef={mapRef} styleReady={styleReady} onSelectionChange={setReviewedWeatherSelected} /></div>
            <div hidden={!shownCatalogIds.has("soil")}><SoilMoistureControl mapRef={mapRef} styleReady={styleReady} state={soilMapState} onChange={changeSoilMapState} onEngineContextChange={setSoilMoistureContext} /></div>
            <div hidden={!shownCatalogIds.has("crop")}><CropCasmaControl mapRef={mapRef} styleReady={styleReady} projection={projection} onSelectionChange={setCropSelected} /></div>
            <div hidden={!shownCatalogIds.has("aviation")}><AviationLayerControl mapRef={mapRef} styleReady={styleReady} onSelectionChange={setAviationSelected} onResearchRecords={setAviationResearch} inspectRequest={aviationInspect} showRequest={aviationShowRequest} onPickingChange={setAviationPicking} /></div>
            {LAYER_REGISTRY.map(layer => <article key={layer.id} hidden={!shownCatalogIds.has(layer.id)} className="official-context-row" data-visible={visibility[layer.id]}><div className="official-context-primary"><label className="visibility-switch"><input type="checkbox" checked={visibility[layer.id]} aria-label={`${visibility[layer.id] ? "Hide" : "Show"} ${layer.title}`} onChange={event => setVisibility(current => ({ ...current, [layer.id]: event.target.checked }))} /><span aria-hidden="true" /></label><i style={{ "--swatch": layer.legend[0]?.color ?? "#8bbeb8" } as React.CSSProperties} /><div><strong>{layer.title}</strong><small>{layer.sourceId} · {visibility[layer.id] ? sourceStates[layer.id] : "Off"}</small></div></div><details className="specialty-layer-details"><summary>Source details</summary><div className="official-context-option-body"><p>{layer.description}</p><button type="button" onClick={() => zoomToLayer(layer)}>Fit layer</button><button type="button" onClick={() => inspectSourceConnection(layer)}>Inspect records</button></div></details></article>)}
            <details className="layer-source-diagnostics"><summary>Source status &amp; coverage</summary>
{composedSurfaceCount > 1 && <p className="layer-balance-note">Multiple surfaces are active. The map balances their opacity so boundaries and points stay readable; each slider keeps your selected value.</p>}
          {mapSignals.length > 0 && <section className="map-signal-panel" aria-label="Patterns supported by selected data"><strong>Signals in selected data</strong>{mapSignals.map((signal) => <article key={`${signal.kind}:${signal.title}`}><span>{signal.kind === "forecast" ? "PROVIDER FORECAST" : signal.kind === "observed" ? "OBSERVED" : "CATALOG TIME"}</span><b>{signal.title}</b><small>{signal.detail}</small></article>)}</section>}
            {officialWorkspace === "disaster" && <section className="official-workspace-ledger" aria-label="Disaster source coverage">
              <strong>Hazard source coverage</strong><p>Connected layers below keep independent visibility, opacity, source time, and quality settings. A missing feed is never an all-clear.</p>
              <details><summary>{DISASTER_COVERAGE_HOLDS.length} source families held for verification</summary>{DISASTER_COVERAGE_HOLDS.map(item => <p key={item.title}><b>{item.title} · HELD</b><br />{item.detail} <a href={item.sourceUrl} target="_blank" rel="noreferrer">Source ↗</a></p>)}</details>
            </section>}
            {officialWorkspace === "groundwater" && <section className="official-workspace-ledger" aria-label="Aquifers and groundwater guide"><h3>Beneath Kansas</h3><p>Start with an aquifer extent, then select one High Plains map to explore depth to water, saturated thickness, or water-table elevation. Each overlay has independent opacity. Click a region for its range, or a monitoring point for its KGS well record.</p><p>High Plains maps: <strong>2022–2024</strong>. Monitoring locations: <strong>2026</strong>. Snapshots checked October 4, 2026. Overlapping aquifers may occupy different depths. These maps do not calculate underground flow.</p><button type="button" onClick={() => { setOfficialContextVisible("kgs-aquifer-high-plains", true); mapRef.current?.fitBounds([[-102.06, 36.99], [-97.1, 40.01]], { padding: 70, duration: reducedMotion ? 0 : 700 }); }}>Explore the High Plains aquifer</button><a href="https://www.kgs.ku.edu/HighPlains/HPA_Atlas/index.html" target="_blank" rel="noreferrer">KGS High Plains Atlas ↗</a></section>}
            {officialWorkspace === "transport" && <p className="official-workspace-land-note">Kansas roads and active or abandoned railroad references from KDOT, plus optional DeFlock community-reported ALPR areas. Each overlay has its own visibility and opacity, over your chosen basemap. Source designations are not live traffic, train movement, public access, or historical reconstruction.</p>}
            {officialWorkspace === "land" && <p className="official-workspace-land-note">BLM PLSS images are provider-current Kansas survey reference; inspect identifiers at the map center from a layer’s Options. The separate MLRS oil-and-gas lease overlays show only authorized or closed Kansas cases with direct PLSS match scores 0–3. They omit generalized and unmapped cases and are not exact lease boundaries, ownership, drilling, or production. <a href="https://glorecords.blm.gov/" target="_blank" rel="noreferrer">Search official GLO patents, plats, and field notes ↗</a> Reviewed GLO overlays and KFM land releases remain pending.</p>}
            {officialWorkspace === "transport" && <p className="layer-journey-intro">Bridge age, historic designation, and recorded closure are separate filters. Historical roads are KDOT’s 1918 map, not proof of present abandonment. A verified statewide closed-road history and demolished-bridge inventory are not connected yet; no missing route is inferred closed.</p>}
            <p>{!buildYearCurrent ? `Current sources are held because this site was built for ${OFFICIAL_CONTEXT_PRESENT_FRAME}. NASA’s fixed lightning climatology remains available as historical context.` : year === OFFICIAL_CONTEXT_PRESENT_FRAME ? "Operational sources have their own observation clocks. NASA lightning climatology is a separate 1995–2014 historical composite. Both are map context only." : `Operational sources selected for the map are held at ${temporalScopeLabel}; choose Present to display them. NASA’s fixed climate field is independent of this atlas year.`}</p>
            <div className="official-context-pulse" aria-label="Live source connection status">
              <div><span><small>RETURNED FEATURES</small><strong>{officialFeatureCount.toLocaleString("en-US")}</strong></span><span><small>SELECTED SOURCES</small><strong>{officialReadyCount}/{visibleOfficialCount} settled</strong></span><span><small>LATEST RETRIEVAL</small><strong>{officialLatestRetrievedAt ? `${new Date(officialLatestRetrievedAt).toLocaleString("en-US", { timeZone: "UTC", year: "numeric", month: "short", day: "numeric", hour: "numeric", minute: "2-digit", hour12: false })} UTC` : "Not yet"}</strong></span></div>
              <nav aria-label="Official data actions"><button type="button" disabled={!buildYearCurrent || officialRefreshPlan.count === 0 || officialLoadingCount > 0} onClick={refreshVisibleOfficialContext}>{!buildYearCurrent ? "Rebuild required" : officialRefreshPlan.reason === "historical" ? `Held until ${formatTimelineStep(OFFICIAL_CONTEXT_PRESENT_FRAME)}` : officialLoadingCount > 0 ? "Refreshing…" : `Refresh ${officialRefreshPlan.count} selected`}</button><button type="button" disabled={visibleOfficialCount === 0} onClick={hideAllOfficialContext}>Hide all</button></nav>
            </div>
            </details>
            <footer><code>EXTERNAL SOURCE → FIXED ADAPTER → MAP DISPLAY</code><span>Evidence held at admission, release, and EvidenceBundle gates · <a href="https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3393" target="_blank" rel="noreferrer">governance issue #3393 ↗</a></span></footer>
          </section>

          <div className="local-layer-settings" hidden={!earthEngineContext.enabled || layerCatalogView === "official" || layerCatalogView === "selected" && !matchingCatalogEntries.some(entry => entry.imagery)}>
            <p className="layer-journey-intro">Reviewed Kansas imagery appears here when an approved display set is installed. Each layer has its own visibility, opacity, source period, and limits. <Link href="/earth-engine">Explore all source recipes ↗</Link></p>
            <section className="reviewed-imagery-section" aria-label="Earth Engine imagery layers">
              {earthEngineContext.enabled && <EarthEngineDisplayControls catalogView={layerCatalogView} catalogTopic={officialWorkspace} catalogQuery={officialSourceQuery} map={styleReady ? mapRef.current : null} mapYear={temporalMode === "snapshot" ? year : -1} manifests={earthEngineContext.manifests} loading={earthEngineContext.loading} error={earthEngineContext.error} rendererState={runtime.kind} onDisplayChange={setEarthEngineDisplay} onReload={earthEngineContext.reload} />}
            </section>
          </div>
            <nav className="layer-task-links" aria-label="Related map tools"><button type="button" onClick={event => openMapUtility("scene", event.currentTarget)}><span>Appearance</span><small>Basemap, terrain &amp; lighting</small><b aria-hidden="true">↗</b></button><button type="button" onClick={event => openSourceStatus(event.currentTarget)}><span>Source status</span><small>Connections &amp; coverage</small><b aria-hidden="true">↗</b></button></nav>

          </div>
          <details className="layer-panel-explore" hidden={sourceStatusOpen || leftPanelMode !== "layers" && leftPanelMode !== "live"}>
            <summary>Explore <span>Other map tools</span></summary>
            <nav aria-label="Other map tools">
              <button type="button" onClick={() => setLeftPanelMode("views")}>Views</button>
              <button type="button" onClick={() => setLeftPanelMode("places")}>Places</button>
              <Link href="/observatory">Event Observatory</Link>
              <button type="button" onClick={() => { setLeftOpen(false); openMapUtility("history"); }}>Kansas historic maps</button>
              <button type="button" onClick={() => { setLeftOpen(false); openMapUtility("navigate"); }}>Map controls</button>
            </nav>
            <AviationControl contextKey={JSON.stringify([year, calendarSweep, selected?.featureId ?? null, visibility, officialVisibility])} />
          </details>
        </aside>

        <section className="map-stage" data-underground={undergroundOpen ? "true" : undefined} data-live-dock={liveDockVisible || glmFlashesEnabled} data-radar-loop={showRadarDock} data-raster-fallback={runtime.kind === "unsupported" && earthEngineContext.manifests.length > 0} aria-label="Kansas MapLibre Explorer">

          <div ref={mapInformationHostRef} className="maplibregl-ctrl-top-right map-information-home" role="group" aria-label="Map information and source attribution" />

          {instrumentOpen && !glmFlashesEnabled && showStreamflowDock && <HydrologyObservatory
            bundle={streamflowBundle}
            state={streamflowDisplayState}
            error={streamflowError}
            frame={streamflowFrame}
            frameIndex={safeStreamflowFrameIndex}
            playing={streamflowPlaying}
            speed={streamflowPlaybackSpeed}
            range={streamflowRange}
            selectedStationId={streamflowSelectedStationId}
            mapDisplay={riverMapDisplay}
            onMapDisplay={setRiverMapDisplay}
            frameTimes={streamflowFrames}
            reducedMotion={reducedMotion}
            downstreamState={downstreamState}
            downstreamPathCount={downstreamPaths.length}
            downstreamAnalysis={downstreamAnalysis}
            sourceSwitcher={liveObservationSwitcher}
            onClose={closeLiveInstrument}
            onRefresh={() => { void refreshSelectedStreamflow(); }}
            onTogglePlay={toggleStreamflowPlayback}
            onStep={stepStreamflow}
            onSeek={seekStreamflow}
            onJumpLatest={jumpStreamflowToLatest}
            onSpeed={setStreamflowPlaybackSpeed}
            onRange={changeStreamflowRange}
            onSelectStation={selectStreamflowStation}
            onShowDirection={showStreamflowDirection}
          />}
          {instrumentOpen && !glmFlashesEnabled && showRadarDock && <aside
            className="noaa-radar-loop"
            data-state={noaaRadarDisplayState.toLowerCase().replaceAll(" ", "-")}
            data-details={radarDetailsOpen ? "open" : "closed"}
            tabIndex={0}
            aria-label="NOAA observed radar loop controls"
            onKeyDown={(event) => {
              if (event.target !== event.currentTarget) return;
              if (event.key === " ") { event.preventDefault(); toggleNoaaRadarPlayback(); }
              if (event.key === "ArrowLeft") { event.preventDefault(); stepNoaaRadar("reverse"); }
              if (event.key === "ArrowRight") { event.preventDefault(); stepNoaaRadar("forward"); }
              if (event.key === "Home") { event.preventDefault(); jumpNoaaRadarToLatest(); }
            }}
          >
            {liveObservationSwitcher}
            <header>
              <div><span>OBSERVED RADAR · EXTERNAL CONTEXT</span><strong>{NOAA_RADAR_PRODUCT_TITLE}</strong></div>
              <b>{noaaRadarDisplayState}</b>
              <button type="button" className="noaa-radar-details-toggle" aria-expanded={radarDetailsOpen} aria-controls="noaa-radar-details" onClick={() => setRadarDetailsOpen(open => !open)}>Settings</button>
              <button type="button" className="noaa-radar-close" onClick={closeLiveInstrument} aria-label="Close radar loop controls" title="Close the loop controls; the radar stays on the map"><span aria-hidden="true">×</span></button>
            </header>
            <div className="noaa-radar-frame" role="status" aria-live={noaaRadarPlaying ? "off" : "polite"} aria-busy={noaaRadarFrameLoadState === "loading"} aria-atomic="true">
              <div><strong>{noaaRadarFrameHeadline}</strong><small>{noaaRadarFrameDetail}</small></div>
              <span>{noaaRadarLoopFrames.length > 0 ? `${noaaRadarFrameIndex >= 0 ? noaaRadarFrameIndex + 1 : 0} / ${noaaRadarLoopFrames.length}` : "0 / 0"}</span>
            </div>
            {noaaRadarLoopSpan === "all" && noaaRadarLoopFrames.length > 1 && <p className="noaa-radar-motion-note">Available NOAA scans: {formatNoaaRadarLocalTime(noaaRadarLoopFrames[0])} to {formatNoaaRadarLocalTime(noaaRadarLoopFrames.at(-1)!)} · {noaaRadarLoopFrames.length} exact frames</p>}
            <div className="noaa-radar-transport" aria-label="Radar playback">
              <button type="button" onClick={() => stepNoaaRadar("reverse")} disabled={!noaaRadarRenderable || noaaRadarFrameIndex <= 0 || noaaRadarFrameLoadState === "loading"} aria-label="Previous NOAA radar observation">‹</button>
              <button className="noaa-radar-play" type="button" aria-pressed={noaaRadarPlaying} onClick={toggleNoaaRadarPlayback} disabled={reducedMotion || noaaRadarLoopFrames.length < 2 || noaaRadarManifestState === "loading" || !noaaRadarRenderable}>{noaaRadarPlaying ? "Ⅱ Pause" : "▶ Restart loop"}</button>
              <button type="button" onClick={() => stepNoaaRadar("forward")} disabled={!noaaRadarRenderable || noaaRadarFrameIndex < 0 || noaaRadarFrameIndex >= noaaRadarLoopFrames.length - 1 || noaaRadarFrameLoadState === "loading"} aria-label="Next NOAA radar observation">›</button>
              <input type="range" min="0" max={Math.max(0, noaaRadarLoopFrames.length - 1)} value={Math.max(0, noaaRadarFrameIndex)} disabled={!noaaRadarRenderable || noaaRadarLoopFrames.length < 2 || noaaRadarFrameLoadState === "loading"} onChange={(event) => {
                const nextIndex = Number(event.target.value);
                const nextFrame = noaaRadarLoopFrames[nextIndex];
                if (!nextFrame) return;
                setNoaaRadarPlaying(false);
                setNoaaRadarFollowLatest(nextIndex === noaaRadarLoopFrames.length - 1);
                applyNoaaRadarFrame(nextFrame);
              }} aria-label="Select an exact NOAA radar observation" aria-valuetext={noaaRadarActiveFrame ? `${formatNoaaRadarLocalTime(noaaRadarActiveFrame)}; ${formatNoaaRadarUtcTime(noaaRadarActiveFrame)}` : "No radar frame available"} />
              <button className="noaa-radar-live" type="button" aria-pressed={noaaRadarFollowLatest && noaaRadarSelectedIsLatest} onClick={jumpNoaaRadarToLatest}>Latest</button>
            </div>
            {noaaRadarFrameError && <div className="noaa-radar-error" role="alert"><strong>{noaaRadarRenderable ? "Frozen on the last confirmed observation" : "Radar withheld"}</strong><span>{noaaRadarFrameError} No untimed or synthetic fallback was used.</span></div>}
            <div id="noaa-radar-details" className="noaa-radar-details">
              <div className="noaa-radar-settings">
                <label><span>Loop</span><select value={noaaRadarLoopSpan} onChange={(event) => { setNoaaRadarPlaying(false); setNoaaRadarLoopSpan(event.target.value === "all" ? "all" : Number(event.target.value) as NoaaRadarLoopSpanMinutes); }}><option value={30}>30 min</option><option value={60}>1 hour</option><option value={120}>2 hours</option><option value="all">All available</option></select></label>
                <label><span>Speed</span><select value={noaaRadarPlaybackSpeed} onChange={(event) => setNoaaRadarPlaybackSpeed(Number(event.target.value) as NoaaRadarPlaybackSpeed)}><option value={0.5}>0.5×</option><option value={1}>1×</option><option value={2}>2×</option></select></label>
                <label><span>Opacity</span><input type="range" min="10" max="100" value={Math.round(officialOpacity["nws-radar"] * 100)} onChange={(event) => setOfficialContextOpacity("nws-radar", Number(event.target.value) / 100)} aria-valuetext={`${Math.round(officialOpacity["nws-radar"] * 100)} percent`} /></label>
                <button type="button" onClick={() => void refreshNoaaRadarManifest()} disabled={noaaRadarManifestState === "loading"}>Refresh</button>
              </div>
              <details className="noaa-radar-legend">
                <summary>Reflectivity legend + source</summary>
                <img src={NOAA_RADAR_LEGEND_URL} width="272" height="21" loading="lazy" alt="NOAA base-reflectivity color legend in dBZ" />
                <p>Playback starts with the oldest scan in the selected window, advances through exact observations to the newest scan, then repeats. Transparent pixels mean no displayed echo. Missing or unavailable imagery is not interpreted as clear weather. A settled request means MapLibre reported no source error; it does not prove complete radar coverage.</p>
                <dl><div><dt>Source</dt><dd>{NOAA_RADAR_SOURCE_TITLE}</dd></div><div><dt>Cadence</dt><dd>{noaaRadarManifest ? `${Math.round(noaaRadarManifest.nominalCadenceSeconds / 60)} min observed median` : "Discovered from NOAA"}</dd></div><div><dt>Latest age</dt><dd>{noaaRadarLatestAgeMinutes === null ? "Unknown" : `${noaaRadarLatestAgeMinutes} min`}</dd></div><div><dt>Gaps</dt><dd>{noaaRadarManifest ? noaaRadarManifest.gapCount : "Unknown"}</dd></div></dl>
                {noaaRadarCrossDomainSources.length > 0 && <p><strong>Co-visible operational context:</strong> {noaaRadarCrossDomainSources.join(" · ")}. Each source keeps its own observation or retrieval clock; visual overlap does not establish correlation, lag, direction, or causation.</p>}
                <a href={OFFICIAL_CONTEXT_BY_ID["nws-radar"].sourceUrl} target="_blank" rel="noreferrer">Open NOAA nowCOAST ↗</a>
              </details>
              {reducedMotion && <p className="noaa-radar-motion-note">Reduced motion is active. Automatic looping is off; exact-frame stepping remains available.</p>}
              <footer>Situational display only · not an emergency warning service · times remain separate from the atlas year</footer>
            </div>
          </aside>}
          {instrumentOpen && !glmFlashesEnabled && showLightningDock && <aside className="lightning-observatory" data-signal={lightningPreview} aria-label="NOAA lightning density controls">
            {liveObservationSwitcher}
            <header>
              <div><span>NOAA LIGHTNING · EXTERNAL CONTEXT</span><strong>15-minute strike density</strong></div>
              <button type="button" onClick={() => setLightningReloadToken((value) => value + 1)} disabled={lightningManifestState === "loading"}>Refresh</button>
            </header>
            <div className="lightning-clock"><strong>{lightningFrame ? `${lightningFrame.slice(0, 16).replace("T", " ")} UTC` : "No frame loaded"}</strong><span>{lightningManifest ? `${Math.max(0, lightningFrameIndex + 1)} / ${lightningManifest.frames.length} frames` : lightningManifestState === "loading" ? "Checking NOAA times" : "NOAA times unavailable"}</span></div>
            <output role="status" aria-live={lightningPlaying ? "off" : "polite"}>{!lightningSelected ? projection === "globe" ? "Lightning display is available on the flat map" : "Held by atlas time" : lightningPreview === "loading" ? "Loading and sampling the visible map area…" : lightningPreview === "signal" ? "NOAA density visible in the sampled map area for this frame" : lightningPreview === "none" ? "No NOAA density in the sampled map area for this frame · earlier frames may differ; not an all-clear" : lightningPreview === "error" || lightningManifestState === "error" ? "Visible-area signal unconfirmed or NOAA unavailable · no simulated flashes" : "Checking exact NOAA frames"}</output>
            <input type="range" min="0" max={Math.max(0, (lightningManifest?.frames.length ?? 1) - 1)} value={Math.max(0, lightningFrameIndex)} disabled={!lightningManifest || !lightningSelected} onChange={(event) => { setLightningPlaying(false); setLightningFrame(lightningManifest?.frames[Number(event.target.value)] ?? null); }} aria-label="NOAA lightning 15-minute density frame" aria-valuetext={lightningFrame ?? "No frame"} />
            <div className="lightning-transport" aria-label="Lightning playback"><button type="button" disabled={!lightningSelected || !lightningManifest || lightningFrameIndex <= 0} onClick={() => { setLightningPlaying(false); setLightningFrame(lightningManifest?.frames[lightningFrameIndex - 1] ?? null); }} aria-label="Previous lightning density frame">‹</button><button type="button" aria-pressed={lightningPlaying} disabled={!lightningPlaying && (reducedMotion || !lightningManifest || lightningManifest.frames.length < 2 || !lightningSelected || lightningManifestState !== "ready" || !lightningPlaybackReady)} onClick={() => { if (lightningPlaying) setLightningPlaying(false); else { setLightningFrame(lightningManifest?.frames[0] ?? null); setLightningPlaying(true); } }}>{lightningPlaying ? "Ⅱ Pause" : "▶ Replay frames"}</button><button type="button" disabled={!lightningSelected || !lightningManifest || lightningFrameIndex >= lightningManifest.frames.length - 1} onClick={() => { setLightningPlaying(false); setLightningFrame(lightningManifest?.frames[lightningFrameIndex + 1] ?? null); }} aria-label="Next lightning density frame">›</button><button type="button" disabled={!lightningManifest || !lightningSelected} onClick={() => { setLightningPlaying(false); setLightningFrame(lightningManifest?.latest ?? null); }}>Latest</button></div>
            <details className="lightning-details"><summary>Density legend + source</summary><div className="lightning-density-key"><img src="/api/lightning/legend" width="292" height="46" alt="NOAA nowCOAST lightning density legend with the provider's numeric bins and units" loading="lazy" /><a href={NOAA_LIGHTNING_LEGEND_URL} target="_blank" rel="noreferrer">NOAA density legend ↗</a></div><p>Ground-network strike density in 8 × 8 km cells. The glow follows returned image cells only. This 15-minute product does not supply exact interval boundaries here. Frame list checked {lightningManifest ? `${lightningManifest.retrievedAt.slice(11, 16)} UTC` : "not yet"}. Empty pixels do not establish safety.</p><a href={OFFICIAL_CONTEXT_BY_ID["noaa-lightning-density"].sourceUrl} target="_blank" rel="noreferrer">NOAA layer and time metadata ↗</a></details>
            {reducedMotion && <p className="lightning-motion-note">Reduced motion: autoplay and glow are off. Frame steps remain available.</p>}
            <footer>Situational display only · not an emergency warning service · time remains separate from the atlas year</footer>
          </aside>}
          <LightningFlashLoop key={glmFlashesEnabled && glmFlashesAllowed ? "enabled" : "disabled"} map={styleReady ? mapRef.current : null} enabled={glmFlashesEnabled && glmFlashesAllowed} reducedMotion={reducedMotion} onClose={() => setGlmFlashesEnabled(false)} />
          <ExplorerGuide open={guideOpen === true && primaryWorkspace === "map"} motionEnabled={dynamicEffects} onMotionChange={setDynamicEffects} onSearch={runWelcomeSearch} onTopic={runWelcomeTopic} onMap={runWelcomeMap} onClose={closeExplorerGuide} onAction={runExplorerGuideAction} onMore={() => setHelpOpen(true)} />

          {frameCheckEnabled && <FrameCheck selectedLayers={selectedMapLayerCount} map={runtime.kind === "ready" ? mapRef.current : null} />}
          <div id="map-canvas" ref={mapContainerRef} className="map-canvas" data-projection={projection} data-cinematic={sceneEffects.cinematic && scenePreset === "elevation-3d" ? "3d" : undefined} data-night-sky={sceneEffects.stars && !renderEfficient ? "on" : undefined} tabIndex={-1} role="application" aria-hidden={runtime.kind === "unsupported"} aria-label="Interactive map of real Kansas baselines and dated source layers. Use arrow keys to pan and plus or minus to zoom; use Inspect or Map layers for a keyboard feature alternative." onFocus={(event) => { if (event.target === event.currentTarget) mapRef.current?.getCanvas().focus({ preventScroll: true }); }} />
          {showCategoryDock && activeCategoryMap && <CategoryMapDock look={activeCategoryMap} mode={categoryMode} depth={verticalExaggeration} azimuth={lightAzimuth} sunAvailable={categorySunAvailable}
            terrainAvailable={runtime.kind !== "unsupported" && runtime.kind !== "error" && terrainState !== "ERROR"} onMode={chooseCategoryMode} onDepth={changeTerrainDepth}
            sun={sceneEffects.sunSync ? { light: sunSceneLight(sunAt, view.center[0], view.center[1]), at: sunAt, dayFraction: intervalFractionAtInstant(sunAt, kansasLocalDayInterval(currentKansasCalendarDay(new Date(sunAt)))), live: sunStudyAt === null } : null}
            onAzimuth={(azimuth) => changeStudioLight({ atmosphere: atmospherePreset, azimuth })} onRealSun={(sunSync) => updateSceneEffects({ ...sceneEffectsRef.current, sunSync })}
            onSunTime={(fraction) => { setSunPlaying(false); setSunStudyAt(fraction === null ? null : instantAtIntervalFraction(kansasLocalDayInterval(currentKansasCalendarDay(new Date(sunClock))), fraction)); }}
            sunPlaying={sunPlaying} motionAllowed={!reducedMotion} onSunPlay={playSunDay} onTransect={startCategoryTransect} onUnderground={enterUnderground}
            daylight={activeCategoryMap.tools?.includes("daylight") ? { on: daylightEnabled, playing: daylightPlaying, time: daylightDisplayTime.central,
              reading: `Kansas center: ${daylightPhaseReading(solarReferenceElevation(daylightInstant, activeCategoryMap.camera.center[1], activeCategoryMap.camera.center[0]))}` } : undefined}
            onDaylight={showCategoryDaylight} onDaylightPlay={setDaylightPlayback}
            measuringArea={measureMode === "area"} onMeasureArea={() => beginMapMeasurement("area")}
            radar={{ watching: liveDockVisible && showRadarDock, available: buildYearCurrent && temporalQuery.frame === OFFICIAL_CONTEXT_PRESENT_FRAME }}
            onRadar={(watch) => watch ? watchRadarLoop() : closeLiveInstrument()}
            layerVisibility={officialVisibility} onLayer={setOfficialContextVisible}
            civic={activeCategoryMap.topic === "government" ? { visible: Boolean(officialVisibility[CIVIC_ID]),
              state: officialStates[CIVIC_ID] === "error" ? "error" : effectiveOfficialVisibility[CIVIC_ID] ? officialStates[CIVIC_ID] : officialStates[CIVIC_ID] === "loading" ? "loading" : "held",
              day: civicFrameDay,
              congress: civicFrameCongress,
              options: Array.from({ length: 84 }, (_, index) => ({ value: index + 36, label: civicCongressLabel(index + 36) })),
              items: effectiveOfficialVisibility[CIVIC_ID] && officialStates[CIVIC_ID] === "ready" ? (officialPayloads[CIVIC_ID]?.data.features ?? []).map(feature => ({ id: String(feature.id), label: String(feature.properties?.name) })) : [] } : undefined}
            onCivicCongress={congress => {
              const day = civicTermStart(congress);
              setOfficialContextVisible(CIVIC_ID, true);
              void seekCalendarFrame({ day, start: "1861-01-29", end: currentUtcDay(), step: "years", before: null, showing: "B" });
            }}
            onCivicPresent={returnCalendarToPresent}
            onCivicRetry={() => retryOfficialLayer(CIVIC_ID)}
            onCivicPick={(id, returnElement) => {
              if (!effectiveOfficialVisibility[CIVIC_ID] || officialStates[CIVIC_ID] !== "ready") return;
              const feature = officialPayloads[CIVIC_ID]?.data.features.find(item => String(item.id) === id);
              const geometry = feature && countySearchGeometry(feature);
              if (!feature || !geometry) return;
              const context = buildBasemapContext({ ...feature, source: CIVIC_SOURCE.sourceId }, ...geometry.focus);
              if (!context) return;
              openSelection(context, returnElement);
              mapRef.current?.fitBounds(geometry.bounds, { padding: 70, maxZoom: 9, duration: motionDuration(650) });
            }}
            keys={withElevationKey([...(quakeRecordOn && quakeRecord ? [earthquakeRecordKey(quakeRecord.endYear)] : []), ...(shownOutlook ? [spcOutlookKey(shownOutlook.day, shownOutlook.product)] : []), ...(shownReports ? [stormReportsKey(shownReports.day)] : []), ...(floodOn && officialVisibility["noaa-nwps-gauges"] ? [floodKey()] : []), ...(shownDrought ? [shownDroughtChange ? droughtChangeKey(shownDroughtChange.weeks, shownDroughtChange.from, shownDroughtChange.to) : droughtKey(shownDrought.date)] : []), ...withReviewedKey(withCivicKey(mapKeysFor(activeCategoryMap.starters, id => Boolean(officialVisibility[id as OfficialContextId])), effectiveOfficialVisibility[CIVIC_ID] && officialStates[CIVIC_ID] === "ready" ? (officialPayloads[CIVIC_ID]?.data.features ?? []).map(feature => Number(feature.properties?.district)) : [], civicFrameCongress), reviewedData ? reviewedSource : null)],
              basemap === "relief" ? reliefElevationKey(RELIEF_RAMP) : basemap === "aviation-chart" ? chartElevationKey(AVIATION_TINT_BANDS) : null)}
            flow={{ on: sceneEffects.waterFlow, reading: sceneReadings.waterFlow, still: runtime.kind === "degraded" ? "the map is degraded" : runtime.kind !== "ready" ? "the map is still starting" : reducedMotion ? "reduced motion" : !dynamicEffects ? "ambient motion is off" : browserRenderBudget(renderQuality).efficient ? "efficient rendering" : null }}
            onFlow={(waterFlow) => updateSceneEffects({ ...sceneEffectsRef.current, waterFlow })} onReset={resetCategoryView}
            flood={activeCategoryMap.tools?.includes("flood") ? { on: floodOn,
              state: !buildYearCurrent || temporalQuery.frame !== OFFICIAL_CONTEXT_PRESENT_FRAME ? "held" : officialStates["noaa-nwps-gauges"] === "error" ? "failed" : floodGaugeFeatures ? "ready" : "loading",
              summary: floodGaugeFeatures ? floodNetworkSummary(floodSummaries) : null, list: floodItems, picked: floodLid, gauge: shownFloodGauge, plot: floodPlot,
              reading: shownFloodGauge ? floodReading(shownFloodGauge, floodClock) : null, gaugeLoading: Boolean(floodLid && !shownFloodGauge && floodFailed !== floodLid),
              gaugeFailed: floodLid !== null && floodFailed === floodLid && !shownFloodGauge, url: floodLid ? floodGaugePage(floodLid) : null } : undefined}
            onFlood={showFlood} onFloodPick={pickFloodGauge} onFloodClear={() => setFloodLid(null)}
            photoreal={activeCategoryMap.tools?.includes("photoreal") ? { on: basemap === "photoreal", landscapes: PHOTOREAL_LANDSCAPES, place: photorealPlace, depth: verticalExaggeration } : undefined}
            onPhotoreal={showPhotoreal}
            reviewed={reviewedSource ? { source: REVIEWED_SOURCE_LABEL[reviewedSource], on: reviewed.on, loading: reviewed.status === "loading",
              reason: reviewed.status === "withheld" && reviewed.reason ? REVIEWED_REASONS[reviewed.reason] ?? "No reviewed snapshot can be shown." : null,
              count: reviewed.history.length, index: reviewed.index, publishedAt: reviewedTime(reviewed.history[reviewed.index]?.publishedAt), capturedFor: reviewedTime(reviewed.product?.bucketAt),
              features: reviewed.product?.data.features.length ?? null, freshness: reviewed.product?.freshness ?? null, playing: reviewed.playing, motionAllowed: !reducedMotion,
              selected: reviewedFeature && reviewed.product ? { ...reviewedFeatureSummary(reviewedSource, reviewedFeature.properties), release: reviewed.product.releaseId,
                download: `/api/curated/${reviewedSource}?release=${reviewed.product.releaseId}&download=1` } : null, list: reviewedList, pick: reviewedFeature ? reviewedPick : null } : undefined}
            onReviewed={(on) => { setReviewedPick(null); reviewed.setOn(on); }} onReviewedIndex={reviewed.setIndex} onReviewedClear={() => setReviewedPick(null)}
            onReviewedPick={(id) => {
              // The same pick a map click makes; the map moves to the point, or to the middle of an alert area's extent.
              // A feature released without geometry is still selected, so its details and release show; the map stays put.
              const feature = reviewedData?.features.find(item => String(item.id ?? "") === id);
              if (!feature) return;
              setReviewedPick(id);
              if (!feature.geometry) return;
              const points = feature.geometry.type === "Point" ? [feature.geometry.coordinates] : feature.geometry.type === "Polygon" ? feature.geometry.coordinates.flat()
                : feature.geometry.type === "MultiPolygon" ? feature.geometry.coordinates.flat(2) : [];
              if (!points.length) return;
              const xs = points.map(point => point[0]), ys = points.map(point => point[1]);
              easeToPicked([(Math.min(...xs) + Math.max(...xs)) / 2, (Math.min(...ys) + Math.max(...ys)) / 2]);
            }}
            onReviewedPlay={(on) => { if (on && reviewed.index >= reviewed.history.length - 1) reviewed.setIndex(0); reviewed.setPlaying(on); }}
            aquifer={activeCategoryMap.tools?.includes("aquifer") ? { view: aquiferView, legend: aquiferView && aquiferView !== "kgs-aquifer-high-plains" ? GROUNDWATER_CLASS_LEGENDS[aquiferView] : null } : undefined}
            onAquiferView={showAquiferView}
            soil={activeCategoryMap.tools?.includes("soil") ? { on: soilMapState.visible, depth: soilMapState.view === "root" ? "root" : "surface", reading: soilReading, legendUrl: soilLegendUrl(soilMapState.view === "root" ? "root" : "surface") } : undefined}
            onSoil={showCategorySoil} onSoilDepth={(depth) => changeSoilMapState({ view: depth })}
            drought={activeCategoryMap.tools?.includes("drought") ? { on: droughtOn, loading: Boolean(droughtId && !droughtLoaded && droughtFailed !== droughtId),
              failed: droughtId !== null && droughtFailed === droughtId, reading: droughtLoaded ? droughtReading(droughtLoaded, droughtSeries) : null, url: USDM_PAGE,
              date: droughtDate, label: droughtDate ? usdmDateLabel(droughtDate) : null, newest: droughtWeek === null,
              previous: droughtDate && droughtDate > USDM_FIRST_DATE ? previousUsdmDate(droughtDate) : null,
              next: droughtWeek === null ? null : droughtNewest && nextUsdmDate(droughtWeek) >= droughtNewest ? droughtNewest : nextUsdmDate(droughtWeek),
              categories: USDM_CATEGORIES, weeks: droughtChartWeeks, seriesFailed: droughtSeriesFailed, playing: droughtPlaying, motionAllowed: !reducedMotion,
              counties: countyDrought && countyDrought.length ? { summary: countyDroughtSummary(countyDrought), list: countyChange ? countyChangeList(countyChange) : countyDroughtItems, picked: droughtCounty,
                reading: pickedCountyDrought && droughtLoaded ? [countyDroughtReading(pickedCountyDrought, droughtLoaded.date), pickedCountyChange && droughtChange ? countyChangeReading(pickedCountyChange, droughtChange) : null].filter(Boolean).join(" · ") : null } : null,
              change: { weeks: droughtChange, reading: droughtChangeText, start: droughtChangeTooEarly && droughtChangeFrom ? usdmDateLabel(droughtChangeFrom) : null, loading: Boolean(droughtSinceDate && !droughtSince && droughtSinceFailed !== droughtSinceDate),
                failed: droughtSinceDate !== null && droughtSinceFailed === droughtSinceDate } } : undefined}
            onDrought={showDrought} onDroughtWeek={chooseDroughtWeek} onDroughtPlay={playDrought} onDroughtChange={(weeks) => { setDroughtChange(weeks); setDroughtSinceFailed(null); }} onDroughtCounty={pickDroughtCounty} onDroughtCountyClear={() => setDroughtCounty(null)}
            population={activeCategoryMap.tools?.includes("population") ? { on: populationPrisms, ...densityGroupCounts(officialPayloads["census-counties"]?.data.features ?? []), metresPerPerson: PRISM_METRES_PER_PERSON_PER_SQUARE_MILE } : undefined}
            onPopulation={setPopulationPrismsShown}
            quakes={activeCategoryMap.tools?.includes("quakes") ? { on: quakeRecordOn, loading: quakeRecordOn && !quakeRecord && !quakeRecordFailed, failed: quakeRecordFailed,
              counts: quakeCounts, total: quakeRecord?.events.length ?? 0, startYear: quakeRecord?.startYear ?? 1973, endYear: quakeRecord?.endYear ?? new Date().getUTCFullYear(),
              minMagnitude: quakeRecord?.minMagnitude ?? 2.5, truncated: Boolean(quakeRecord?.truncated), year: quakeRecordYear,
              selected: quakeRecordSelected, selectedUrl: quakeRecordSelected ? earthquakeEventUrl(quakeRecordSelected.id) : null, list: quakeEventList, plots: quakePlots } : undefined}
            onQuakes={showQuakeRecord}
            outlook={activeCategoryMap.tools?.includes("outlook") ? { day: outlookDay, product: outlookProduct, products: outlookDay ? outlookProducts(outlookDay) : [], loading: Boolean(outlookId && !shownOutlook && outlookFailed !== outlookId),
              failed: outlookId !== null && outlookFailed === outlookId, reading: shownOutlook ? spcOutlookReading(shownOutlook) : null, url: SPC_OUTLOOK_PAGE } : undefined}
            onOutlook={chooseOutlook}
            onOutlookProduct={chooseOutlookHazard}
            reports={activeCategoryMap.tools?.includes("reports") ? { day: reportsDay, loading: Boolean(reportsDay && !shownReports && reportsFailed !== reportsDay),
              failed: reportsDay !== null && reportsFailed === reportsDay, reading: shownReports ? stormReportsReading(shownReports) : null, url: STORM_REPORTS_PAGE, verification: outlookCheck,
              selected: reportSelected ? { report: reportSelected, title: `${REPORT_KINDS.find(kind => kind.id === reportSelected.kind)?.name ?? "Report"} · ${reportMagnitude(reportSelected)}`,
                when: reportSelected.time ? reportClock(reportSelected.time) : null } : null, kansas: shownReports ? kansasReportList(shownReports) : [] } : undefined}
            onReports={chooseReports}
            onReportPick={(id) => {
              // The same selection a map click makes, then the map moves to it (no motion when reduced motion is asked for).
              const report = stormReportsRef.current.get(id);
              if (!report) return;
              setReportSelected(report);
              easeToPicked([report.longitude, report.latitude]);
            }}
            onReportClear={() => setReportSelected(null)}
            onQuakeYear={year => { setQuakeRecordYear(year); setQuakeRecordSelected(null); }}
            onQuakeClear={() => setQuakeRecordSelected(null)}
            onQuakePick={(id) => {
              const event = quakeRecordEventsRef.current.get(id);
              if (!event) return;
              setQuakeRecordSelected(event);
              easeToPicked([event.longitude, event.latitude]);
            }}
            onLayers={() => { setLayerCatalogView("official"); openAtlasPanel("layers"); }} onClose={() => setCategoryDockHidden(true)} />}
          {flyoverStopIndex !== null && KANSAS_FLYOVER[flyoverStopIndex] && <div className="flyover-caption" role="status" aria-live="polite">
            <span>FLYOVER · {flyoverStopIndex + 1}/{KANSAS_FLYOVER.length}</span>
            <strong>{KANSAS_FLYOVER[flyoverStopIndex].label}</strong>
            <small>{KANSAS_FLYOVER[flyoverStopIndex].region}</small>
            <button type="button" onClick={() => stopFlyover()}>Stop</button>
          </div>}
          {scenePreset === "elevation-3d" && flyoverStopIndex === null && !reducedMotion && runtime.kind === "ready" && !undergroundOpen
            && <button type="button" className="flyover-launch" onClick={startFlyover}><span aria-hidden="true">✈</span> Fly over Kansas</button>}
          <div className="map-effects" aria-hidden="true">
            <canvas ref={windArrowCanvasRef} className="wind-arrow-canvas" style={{ opacity: officialOpacity["nws-forecast-wind"] }} aria-hidden="true" />
            <canvas ref={waterMotionCanvasRef} className="water-motion-canvas" style={{ opacity: officialOpacity["usgs-streamflow"] }} aria-hidden="true" />
            {windArrowState === "READY" && windArrowFrame && windArrowHover && <output className="wind-arrow-hover" style={{ left: windArrowHover.screenX, top: windArrowHover.screenY }} aria-label="Nearest wind model grid point"><span>GFS MODEL GRID POINT · VALID {windArrowFrame.validTimeUtc.replace("T", " ").slice(0, 16)} UTC</span><strong>{Math.round(windArrowHover.sample.speedMetersPerSecond * 2.23694)} mph <b>→ {windToCompass(windArrowHover.sample.windToDegrees)}</b></strong><small>{windArrowHover.sample.latitude.toFixed(3)}°, {windArrowHover.sample.longitude.toFixed(3)}° · 10 m forecast</small></output>}
          </div>
          {buildYearCurrent && officialVisibility["nws-forecast-wind"] && temporalQuery.frame === OFFICIAL_CONTEXT_PRESENT_FRAME && <output className="wind-arrow-map-badge" data-state={windArrowState} aria-live="polite"><strong>OPEN-METEO · GFS WIND FLOW</strong><span>{windArrowState === "READY" && windArrowFrame ? `10 m forecast · valid ${windArrowFrame.validTimeUtc.replace("T", " ").slice(0, 16)} UTC · ${windArrowFrame.samples.length} grid points` : windArrowState === "ERROR" ? "Forecast unavailable · flow hidden" : "Loading forecast wind flow…"}</span></output>}
          {runtime.kind === "unsupported" && earthEngineContext.manifests.length > 0 && <EarthEngineRasterFallback manifests={earthEngineContext.manifests} display={earthEngineDisplay} onOpenLayers={openEarthEngineLayers} />}
          {(runtime.kind === "loading" || runtime.kind === "error" || (runtime.kind === "unsupported" && !earthEngineContext.manifests.length)) && <div className={`runtime-overlay ${runtime.kind}`} role="status" aria-live="assertive"><span className="runtime-spinner" aria-hidden="true" /><strong>{runtime.kind === "loading" ? "Preparing spatial explorer" : runtime.kind === "unsupported" ? "Map runtime unsupported" : "Map runtime unavailable"}</strong><p>{runtime.message}</p>{runtime.kind === "error" && <button type="button" onClick={() => window.location.reload()}>Reload map</button>}</div>}
          {runtime.kind === "degraded" && <div className="runtime-degraded-banner" role="status" aria-live="polite"><strong>Partial map degradation</strong><span>{runtime.message}</span></div>}
          {!buildYearCurrent && <div className="build-year-warning" role="status" aria-live="assertive"><strong>Current layers paused</strong><span>This site was built for {OFFICIAL_CONTEXT_PRESENT_FRAME}. Rebuild it for the current UTC year before displaying live sources.</span></div>}
          {temporalNoData.length > 0 && <div className="no-time-data" role="status"><strong>No compatible record for {temporalScopeLabel} in {temporalNoData.map((layer) => layer.title).join(", ")}</strong><span>Other active layers remain visible; choose an available frame or change the sweep semantics.</span></div>}

          <nav className="map-tool-rail" aria-label="Unified map controls">
            <div className="map-tool-group" aria-label="Map navigation">
              <button type="button" onClick={() => mapRef.current?.zoomIn({ duration: motionDuration(250) })} aria-label="Zoom in"><span className="map-tool-glyph" aria-hidden="true">＋</span></button>
              <button type="button" onClick={() => mapRef.current?.zoomOut({ duration: motionDuration(250) })} aria-label="Zoom out"><span className="map-tool-glyph" aria-hidden="true">−</span></button>
              <button type="button" onClick={fitKansasView} aria-label="Reset view to Kansas"><span className="map-tool-glyph" aria-hidden="true">KS</span></button>
            </div>
          </nav>

          <aside
            ref={mapUtilityPanelRef}
            id="map-utility-panel"
            className="map-utility-panel"
            data-open={mapUtilityOpen}
            data-view={mapUtilityView}
            aria-hidden={!mapUtilityOpen}
            inert={!mapUtilityOpen}
            aria-modal={isCompact && mapUtilityOpen || undefined}
            role={isCompact && mapUtilityOpen ? "dialog" : undefined}
            aria-labelledby="map-utility-title"
          >
            <header className="map-utility-heading">
              <div><p className="panel-kicker">MAP · {mapUtilityLabels[mapUtilityView].toUpperCase()}</p><h2 id="map-utility-title">{mapUtilityLabels[mapUtilityView]}</h2><span>{mapUtilityDescriptions[mapUtilityView]}</span></div>
              <button className="icon-close" type="button" onClick={closeMapUtility} aria-label={`Close ${mapUtilityLabels[mapUtilityView]}`}>×</button>
            </header>
            <ExplorerControlsNavigation value={mapUtilityView} onChange={viewId => { setMapUtilityView(viewId); if (viewId === "report") setReportGeneratedAt(new Date().toISOString()); if (viewId === "export") setExportGeneratedAt(new Date().toISOString()); }} />
            <div className="map-utility-scroll">
              {mapUtilityView === "report" && <section id="map-utility-view-report" role="region" aria-labelledby="map-utility-title" className="map-utility-section report-builder-section">
                <div className="map-utility-section-heading"><span>CUSTOM REPORT</span><h3>Build from the map you are using</h3><p>Filters apply immediately. The report uses current Explorer records and keeps evidence states, source roles, attribution, uncertainty, and time visible.</p></div>

                <div className="report-builder-grid">
                  <div className="report-controls">
                    <label className="report-title-field"><span>Report title</span><input type="text" value={providerReportTitle} maxLength={90} onChange={(event) => setReportTitle(event.target.value)} /></label>

                    <fieldset className="report-control-group"><legend>Record filters</legend><div className="report-filter-grid">
                      <label><span className="sr-only">Search records included in the report</span><i aria-hidden="true">⌕</i><input type="search" value={reportQuery} onChange={(event) => setReportQuery(event.target.value)} placeholder="Record, layer, source, or domain" /></label>
                      <label><span className="sr-only">Filter report by evidence state</span><select value={reportEvidenceFilter} onChange={(event) => setReportEvidenceFilter(event.target.value as EvidenceState | "ALL")}><option value="ALL">All evidence states</option>{(Object.keys(evidenceLabels) as EvidenceState[]).map((state) => <option key={state} value={state}>{state.replaceAll("_", " ")}</option>)}</select></label>
                    </div></fieldset>

                    <fieldset className="report-control-group"><legend>Geographic scope</legend><div className="report-scope-grid">
                      <button type="button" aria-pressed={reportScope === "VIEWPORT"} onClick={() => setReportScope("VIEWPORT")}><strong>Map extent</strong><small>Records inside the current viewport</small></button>
                      <button type="button" aria-pressed={reportScope === "ANALYSIS_AREA"} disabled={!analysisArea} onClick={() => setReportScope("ANALYSIS_AREA")}><strong>Locked area</strong><small>{analysisArea ? `${analysisAreaRecordCount} compatible records` : "Capture an area from Map controls"}</small></button>
                      <button type="button" aria-pressed={reportScope === "VISIBLE_LAYERS"} onClick={() => setReportScope("VISIBLE_LAYERS")}><strong>Visible layers</strong><small>Statewide records in active layers</small></button>
                      <button type="button" aria-pressed={reportScope === "SELECTION"} disabled={!selected} onClick={() => setReportScope("SELECTION")}><strong>Selection</strong><small>{selectedProviderReport?.status === "WITHHELD" ? "Selection details withheld" : selected?.properties.title ?? "Select a map feature first"}</small></button>
                    </div></fieldset>

                    <fieldset className="report-control-group"><legend>Detail level</legend><div className="report-detail-grid">
                      {(["EXECUTIVE", "STANDARD", "TECHNICAL"] as ReportDetail[]).map((detail) => <button key={detail} type="button" aria-pressed={reportDetail === detail} onClick={() => setReportDetail(detail)}>{detail === "EXECUTIVE" ? "Brief" : detail === "STANDARD" ? "Standard" : "Full detail"}</button>)}
                    </div></fieldset>

                    <fieldset className="report-control-group"><legend>Report sections</legend><div className="report-section-list">
                      {REPORT_SECTIONS.map((section) => <label key={section.id}><input type="checkbox" checked={reportSections[section.id]} onChange={(event) => setReportSections((current) => ({ ...current, [section.id]: event.target.checked }))} /><span><strong>{section.label}</strong><small>{section.detail}</small></span></label>)}
                    </div></fieldset>

                    <fieldset className="report-control-group"><legend>Included layers</legend>
                      <div className="report-layer-actions"><button type="button" onClick={() => setReportLayerIds(activeLayers.map((layer) => layer.id))}>Use visible</button><button type="button" onClick={() => setReportLayerIds(LAYER_REGISTRY.map((layer) => layer.id))}>Select all</button><button type="button" onClick={() => setReportLayerIds([])}>Clear</button></div>
                      <div className="report-layer-list">{LAYER_REGISTRY.map((layer) => {
                        const compatibleCount = layer.data.features.filter((feature) => isFeatureAvailableForTemporalQuery(layer, feature.properties.year, temporalQuery)).length;
                        return <label key={layer.id} data-visible={visibility[layer.id]}><input type="checkbox" checked={reportLayerIds.includes(layer.id)} onChange={(event) => setReportLayerIds((current) => event.target.checked ? [...new Set([...current, layer.id])] : current.filter((id) => id !== layer.id))} /><span><strong>{layer.title}</strong><small>{layer.domain} · {compatibleCount} time-compatible · {visibility[layer.id] ? "visible" : "hidden"}</small></span></label>;
                      })}</div>
                    </fieldset>

                    <fieldset className="report-control-group saved-workspace-control"><legend>Saved workspaces</legend>
                      <div className="workspace-save-row"><input type="text" value={workspaceName} maxLength={50} onChange={(event) => setWorkspaceName(event.target.value)} placeholder="Optional workspace name" /><button type="button" onClick={saveCurrentWorkspace}>Save current</button></div>
                      <p>Stores camera, active time, Time A/B comparison, layers, opacity, selection, and report settings only on this device.</p>
                      <div className="saved-workspace-list">{savedWorkspaces.map((snapshot) => <article key={snapshot.id}><button type="button" onClick={() => loadSavedWorkspace(snapshot)}><strong>{snapshot.name}</strong><small>{new Date(snapshot.savedAt).toLocaleString()} · {snapshot.report?.layerIds?.length ?? 0} report layers</small></button><button type="button" onClick={() => deleteSavedWorkspace(snapshot)} aria-label={`Delete ${snapshot.name}`}>×</button></article>)}{savedWorkspaces.length === 0 && <div><strong>No saved workspaces</strong><small>Save the current analysis setup to return to it later on this device.</small></div>}</div>
                    </fieldset>
                  </div>

                  <article className="report-preview" aria-live="polite">
                    <header><div><span>LIVE REPORT PREVIEW</span><h4>{providerReportTitle.trim() || "Kansas map data report"}</h4><p>{reportScope.replaceAll("_", " ")} · active map time {temporalScopeLabel} · {reportDetail}</p></div><strong>{reportRecords.length} KFM RECORD{reportRecords.length === 1 ? "" : "S"}</strong></header>
                    {selectedProviderReport && <section className="report-preview-section" aria-label="Selected provider source context">
                      <span>SELECTED PROVIDER SOURCE CONTEXT</span>
                      <aside className="report-boundary"><strong>EXTERNAL_CONTEXT_ONLY · No KFM EvidenceBundle attached</strong><p>{selectedProviderReport.boundary}</p></aside>
                      {selectedProviderReport.context ? <>
                        <h4>{selectedProviderReport.context.title}</h4><p>{selectedProviderReport.context.summary}</p>
                        <dl className="evidence-facts">
                          <div><dt>Provider</dt><dd>{selectedProviderReport.context.sourceOrganization}</dd></div>
                          <div><dt>Source time / edition</dt><dd>{selectedProviderReport.context.sourceTime}</dd></div>
                          <div><dt>Observation time</dt><dd>{selectedProviderReport.context.observedAt ?? "Not available"}</dd></div>
                          <div><dt>Provider update time</dt><dd>{selectedProviderReport.context.providerUpdatedAt ?? "Not available"}</dd></div>
                          <div><dt>Retrieved</dt><dd>{selectedProviderReport.context.retrievedAt ?? "Not available"}</dd></div>
                          <div><dt>Response state</dt><dd>{selectedProviderReport.context.sourceState}</dd></div>
                          {selectedProviderReport.context.attributes.map((attribute, index) => <div key={`${attribute.label}:${index}`}><dt>{attribute.label}</dt><dd>{attribute.value}</dd></div>)}
                        </dl>
                        <p>{selectedProviderReport.context.fieldBasis}</p>
                        {selectedProviderReport.context.sourceUrl && <a href={selectedProviderReport.context.sourceUrl} target="_blank" rel="noreferrer">Open provider source ↗</a>}
                        <p><strong>Source use boundary:</strong> {selectedProviderReport.context.sourceBoundary}</p><p><strong>Response / availability limitation:</strong> {selectedProviderReport.context.limitation}</p><p><strong>Attribution:</strong> {selectedProviderReport.context.attribution}</p>
                      </> : <p>{selectedProviderReport.status === "INCOMPATIBLE" ? "Selection is incompatible with the active map time; source details are omitted." : "Selection details are withheld for privacy or unavailable public provenance."}</p>}
                    </section>}
                    {(reportQuery || reportEvidenceFilter !== "ALL") && <div className="report-active-filters"><span>ACTIVE FILTERS</span>{reportQuery && <b>Search: {reportQuery}</b>}{reportEvidenceFilter !== "ALL" && <b>{reportEvidenceFilter.replaceAll("_", " ")}</b>}<button type="button" onClick={() => { setReportQuery(""); setReportEvidenceFilter("ALL"); }}>Clear</button></div>}
                    {reportSections.summary && <div className="report-metrics" aria-label="Report summary metrics"><article><span>KFM records</span><strong>{reportRecords.length}</strong></article><article><span>KFM layers</span><strong>{reportLayerSummary.length}</strong></article><article><span>Evidence states</span><strong>{Object.keys(reportEvidenceCounts).length}</strong></article><article><span>Selection</span><strong>{selected ? "1" : "0"}</strong></article></div>}
                    {measurementGeometryMode && <section className="report-preview-section"><span>MEASUREMENT INPUT</span><p>{measurement} · {measureUnit === "imperial" ? "miles / square miles" : "kilometers / square kilometers"}. Browser-local approximation is carried into JSON as a report input, not as evidence.</p></section>}
                    {reportSections.findings && <section className="report-preview-section"><span>FINDINGS</span><ol>{reportFindings.map((finding) => <li key={finding}>{finding}</li>)}</ol></section>}
                    <section className="report-preview-section report-temporal-comparison"><span>TIME A / TIME B CATALOG AVAILABILITY</span><div className="report-metrics"><article><span>{formatTimelineStep(compareTimeA)}</span><strong>{reportTemporalComparison.timeARecordCount}</strong><small>scoped records</small></article><article><span>{formatTimelineStep(compareTimeB)}</span><strong>{reportTemporalComparison.timeBRecordCount}</strong><small>scoped records</small></article><article><span>DELTA</span><strong>{reportTemporalComparison.recordDelta >= 0 ? "+" : ""}{reportTemporalComparison.recordDelta}</strong><small>catalog records</small></article><article><span>CHANGED</span><strong>{reportTemporalComparison.changedLayerCount}</strong><small>included layers</small></article></div><p>Applies this report’s layer, evidence, query, selection, visibility, viewport, or analysis-area scope to both times. Catalog availability is not observed change or imagery analysis.</p></section>
                    {reportSections.records && <section className="report-preview-section"><span>RECORDS</span><div className="report-record-table" role="table" aria-label="Included report records">
                      {reportRecords.slice(0, reportDetail === "EXECUTIVE" ? 8 : reportDetail === "STANDARD" ? 30 : reportRecords.length).map(({ layer, properties }) => <article key={`${layer.id}:${properties.fid}`} role="row"><div><strong>{properties.title}</strong><small>{layer.title} · {properties.year}</small></div><span data-state={properties.evidenceState}>{properties.evidenceState}</span><p>{properties.summary}</p></article>)}
                      {reportRecords.length === 0 && <div className="report-empty"><strong>{LAYER_REGISTRY.length === 0 ? "No released KFM records included" : "No KFM records included"}</strong><p>{emptyReportFindings(selectedProviderReport?.status ?? null, LAYER_REGISTRY.length === 0).slice(1).join(" ")}</p></div>}
                    </div></section>}
                    {reportSections.evidence && reportRecords.length > 0 && <section className="report-preview-section"><span>EVIDENCE DISTRIBUTION</span><div className="report-evidence-grid">{Object.entries(reportEvidenceCounts).sort((left, right) => right[1] - left[1]).map(([state, count]) => <article key={state}><strong>{count}</strong><span>{state}</span></article>)}</div></section>}
                    {reportSections.limitations && <aside className="report-boundary"><strong>Use boundary</strong><p>No KFM domain records are released in this Site. A generated report preserves limitations and cannot admit or release data.</p></aside>}
                    <footer><span role="status">Free report exports</span><div><button type="button" onClick={() => { void copyCustomReport(); }}>Copy report</button><button type="button" onClick={() => downloadCustomReport("json")}>Report data .json</button><button className="report-download-primary" type="button" onClick={() => downloadCustomReport("html")}>Download report .html</button></div></footer>
                  </article>
                </div>
              </section>}

              {mapUtilityView === "navigate" && <section id="map-utility-view-navigate" role="region" aria-labelledby="map-utility-title" className="map-utility-section">
                <div className="map-utility-section-heading"><span>EXPLORE KANSAS</span><h3>Find your next view</h3><p>Move around the map, return to a place, or try a different perspective.</p></div>
                <div className="map-utility-actions map-navigation-actions">
                  <button type="button" onClick={() => travelCameraHistory(-1)} disabled={cameraHistoryIndex === 0}>Previous view</button>
                  <button type="button" onClick={() => travelCameraHistory(1)} disabled={cameraHistoryIndex >= cameraHistoryLength - 1}>Next view</button>
                  <button type="button" onClick={() => mapRef.current?.zoomIn({ duration: motionDuration(250) })}>Zoom in</button>
                  <button type="button" onClick={() => mapRef.current?.zoomOut({ duration: motionDuration(250) })}>Zoom out</button>
                  <button type="button" onClick={() => mapRef.current?.resetNorthPitch({ duration: motionDuration(450) })}>Reset north</button>
                  <button type="button" onClick={fitKansasView}>Fit Kansas</button>
                  <button type="button" onClick={toggleFullscreen}>Fullscreen</button>
                  <button type="button" onClick={locateUser}>Use my location</button>
                  <button type="button" onClick={() => void copyMapCenter()} disabled={locationCameraRedacted}>Copy center</button>
                </div>
                <details className="explorer-secondary"><summary>Coordinates, gestures &amp; analysis area</summary><div className="explorer-secondary-body">
                <dl className="map-camera-facts">
                  <div><dt>Center</dt><dd>{locationCameraRedacted ? "Private camera · redacted" : `${formatCoordinate(view.center[1], "N", "S")} · ${formatCoordinate(view.center[0], "E", "W")}`}</dd></div>
                  <div><dt>Zoom</dt><dd>{view.zoom.toFixed(2)}</dd></div>
                  <div><dt>Bearing / pitch</dt><dd>{Math.round(view.bearing)}° / {Math.round(view.pitch)}°</dd></div>
                  <div><dt>Projection</dt><dd>{projection}</dd></div>
                </dl>
                <section className="analysis-area-card" data-active={Boolean(analysisArea)} aria-labelledby="analysis-area-title">
                  <header><div><span>MAPLIBRE VIEWPORT ANALYSIS</span><h4 id="analysis-area-title">Area of interest</h4></div><strong>{analysisArea ? "LOCKED" : "NOT SET"}</strong></header>
                  {analysisArea
                    ? <><dl><div><dt>West / east</dt><dd>{analysisArea.west.toFixed(4)}° / {analysisArea.east.toFixed(4)}°</dd></div><div><dt>South / north</dt><dd>{analysisArea.south.toFixed(4)}° / {analysisArea.north.toFixed(4)}°</dd></div><div><dt>Compatible records</dt><dd>{analysisAreaRecordCount}</dd></div><div><dt>Report scope</dt><dd>{reportScope === "ANALYSIS_AREA" ? "ACTIVE" : "AVAILABLE"}</dd></div></dl><div><button type="button" onClick={captureAnalysisArea}>Update from viewport</button><button type="button" onClick={fitAnalysisArea}>Fit area</button><button type="button" onClick={() => { setReportScope("ANALYSIS_AREA"); setReportGeneratedAt(new Date().toISOString()); openMapUtility("report"); }}>Build area report</button><button type="button" onClick={clearAnalysisArea}>Clear</button></div></>
                    : <><p>Lock the current viewport as a stable rectangular analysis area. You can pan elsewhere while reports continue using the locked extent.</p><button type="button" onClick={captureAnalysisArea} disabled={locationCameraRedacted}>Lock current viewport</button></>}
                  <footer>Released KFM domain registry is empty · viewport geometry is context, not evidence</footer>
                </section>
                <div className="map-control-group box-drag-control"><header><strong>Shift-drag action</strong><span>MapLibre box selection</span></header><div className="map-segmented-control"><button type="button" aria-pressed={boxDragMode === "zoom"} onClick={() => { boxDragModeRef.current = "zoom"; setBoxDragMode("zoom"); announce("Shift-drag now zooms to the drawn box"); }}>Zoom to box</button><button type="button" aria-pressed={boxDragMode === "report-area"} onClick={() => { boxDragModeRef.current = "report-area"; setBoxDragMode("report-area"); announce("Shift-drag now locks a browser-local report area"); }}>Capture report area</button></div><p className="map-control-note">Hold Shift and drag on the map. Capture mode converts the box to the locked report scope; it does not select evidence or edit source data.</p></div>
                <form className="map-coordinate-form" onSubmit={goToCoordinates}>
                  <header><strong>Go to coordinates</strong><span>Supported Kansas context extent</span></header>
                  <div>
                    <label><span>Latitude</span><input type="number" inputMode="decimal" min={SUPPORTED_CONTEXT_BOUNDS.south} max={SUPPORTED_CONTEXT_BOUNDS.north} step="0.00001" value={coordinateLatitude} onChange={(event) => { setCoordinateLatitude(event.target.value); setCoordinateError(""); }} aria-invalid={Boolean(coordinateError)} /></label>
                    <label><span>Longitude</span><input type="number" inputMode="decimal" min={SUPPORTED_CONTEXT_BOUNDS.west} max={SUPPORTED_CONTEXT_BOUNDS.east} step="0.00001" value={coordinateLongitude} onChange={(event) => { setCoordinateLongitude(event.target.value); setCoordinateError(""); }} aria-invalid={Boolean(coordinateError)} /></label>
                    <button type="submit">Go to point</button>
                  </div>
                  {coordinateError ? <p role="alert">{coordinateError}</p> : <small>Manual coordinates become ordinary shareable camera state. Browser location remains separately redacted.</small>}
                </form>
                <div className="map-orientation-controls">
                  <label><span><strong>Bearing</strong><output>{Math.round(view.bearing)}°</output></span><input type="range" min="-180" max="180" step="1" value={Math.round(view.bearing)} onChange={(event) => mapRef.current?.easeTo({ bearing: Number(event.target.value), duration: 0 })} /></label>
                  <label><span><strong>Pitch</strong><output>{Math.round(view.pitch)}°</output></span><input type="range" min="0" max="60" step="1" value={Math.round(view.pitch)} onChange={(event) => mapRef.current?.easeTo({ pitch: Number(event.target.value), duration: 0 })} /></label>
                </div>
                <div className="map-control-group"><header><strong>Gesture mode</strong><span>One unified map control system</span></header><div className="map-segmented-control"><button type="button" aria-pressed={gestureMode === "cooperative"} onClick={() => setMapGestureMode("cooperative")}>Cooperative</button><button type="button" aria-pressed={gestureMode === "direct"} onClick={() => setMapGestureMode("direct")}>Direct</button></div><p className="map-control-note">Cooperative mode requires a modifier key for wheel zoom and two fingers for touch pan, reducing accidental page trapping. Direct mode gives the map immediate gesture control.</p></div>
                <aside className="map-utility-boundary" data-tone="privacy"><strong>Location privacy</strong><p>Browser location is used only to move the local camera. While that camera remains location-derived, shared URLs use generalized Kansas defaults plus a redaction marker, receipts and exports use withheld markers, and diagnostics omit coordinates. Fit Kansas clears the private camera.</p></aside>
                <aside className="map-utility-boundary"><strong>Keyboard alternative</strong><p>Use Inspect for a searchable feature list, Layer Catalog for visibility and opacity, and these controls for camera actions without relying on pointer gestures.</p></aside>
                </div></details>
              </section>}

              {mapUtilityView === "history" && <HistoricalTopoControl map={mapRef.current} styleReady={styleReady} locationPrivate={locationCameraRedacted} />}

              {mapUtilityView === "inspect" && <section id="map-utility-view-inspect" role="region" aria-labelledby="map-utility-title" className="map-utility-section">
                <div className="map-utility-section-heading"><span>INSPECT</span><h3>Feature index + context receipt</h3><p>Map hover appears as a preview in the Evidence Drawer. A click or explicit Inspect action selects one feature for full details.</p></div>
                <article className="map-utility-card map-context-card">
                  <header><span>MAP CONTEXT</span><strong>{selected?.properties.title ?? "No committed selection"}</strong></header>
                  <dl><div><dt>Active time</dt><dd>{temporalScopeLabel}</dd></div><div><dt>Visible layers</dt><dd>{visibleCount}</dd></div><div><dt>Selection</dt><dd>{selected ? selected.properties.evidenceState : "NONE"}</dd></div><div><dt>Halo</dt><dd>{selectedLayerHidden ? "HIDDEN LAYER" : selectedTimeMismatch ? "OUTSIDE TIME" : selectedEvidenceFiltered ? "FILTERED" : selected ? "VISIBLE" : "NONE"}</dd></div></dl>
                  <div className="map-utility-actions">
                    <button type="button" onClick={() => void copyMapContextReceipt()}>Copy 15-minute map context receipt</button>
                    <button type="button" onClick={clearSelection} disabled={!selected}>Clear selection</button>
                  </div>
                </article>

                <section className="nearby-context-card" aria-labelledby="nearby-context-title">
                  <header><h4 id="nearby-context-title">Near here · place dossier</h4></header>
                  <p>Explore eligible registry anchors and loaded provider points from selected layers. Source dates and coverage limits stay with each result.</p>
                  <button type="button" disabled={!selectedResearchRecord && !researchAnchor} onClick={event => openResearchDossier(false, event.currentTarget)}>Open Near here</button>
                  {!selectedResearchRecord && !researchAnchor && <p>Select a loaded provider point or an eligible registry record first.</p>}
                </section>

                {mapQueryCandidates.length > 1 && <section className="map-overlap-chooser" aria-labelledby="overlap-title">
                  <div><span>OVERLAP CHOOSER</span><h4 id="overlap-title">{mapQueryCandidates.length} features share this map point</h4><p>Choose one explicitly; the renderer will not silently prefer draw order.</p></div>
                  {mapQueryCandidates.map((candidate) => <button key={`${candidate.layerId}:${candidate.featureId}`} type="button" onClick={() => selectIndexedFeature(candidate.layerId, candidate.featureId)}><span>{candidate.layerTitle} · {candidate.sourceYear}</span><strong>{candidate.title}</strong><small>{candidate.evidenceState}</small></button>)}
                </section>}

                <div className="map-feature-tools">
                  <label><span className="sr-only">Search available map features</span><i aria-hidden="true">⌕</i><input type="search" value={mapFeatureQuery} onChange={(event) => setMapFeatureQuery(event.target.value)} placeholder="Feature, ID, layer, or evidence state" /></label>
                  <label><span className="sr-only">Filter feature index by layer</span><select value={mapFeatureLayer} onChange={(event) => setMapFeatureLayer(event.target.value)}><option value="ALL">All available layers</option>{LAYER_REGISTRY.map((layer) => <option key={layer.id} value={layer.id}>{layer.title}</option>)}</select></label>
                </div>
                <div className="map-feature-scope" role="group" aria-label="Feature index spatial filters">
                  <label><input type="checkbox" checked={inspectViewportOnly} onChange={(event) => setInspectViewportOnly(event.target.checked)} /><span>Current viewport only</span></label>
                  <label><input type="checkbox" checked={inspectVisibleLayersOnly} onChange={(event) => setInspectVisibleLayersOnly(event.target.checked)} /><span>Visible layers only</span></label>
                  <button type="button" onClick={fitIndexedFeatures} disabled={!mapFeatureIndex.length}>Fit results</button>
                </div>
                <div className="map-feature-count"><span>{mapFeatureIndex.length} compatible feature{mapFeatureIndex.length === 1 ? "" : "s"}</span><small>Active time {temporalScopeLabel} · {temporalMode.replaceAll("-", " ")} semantics applied</small></div>
                <div className="map-feature-list">
                  {mapFeatureIndex.slice(0, 60).map(({ layer, feature }) => <article className="map-feature-row" key={`${layer.id}:${feature.properties.fid}`} data-visible={visibility[layer.id]}>
                    <header><span>{layer.title} · {feature.properties.year}</span><strong>{feature.properties.title}</strong><small>{feature.properties.evidenceState}</small></header>
                    <p><code>{feature.properties.fid}</code> · {visibility[layer.id] ? "Layer visible" : "Layer hidden"}</p>
                    <div><button type="button" onClick={() => centerIndexedFeature(layer.id, feature.properties.fid)}>Center</button><button type="button" onClick={() => selectIndexedFeature(layer.id, feature.properties.fid)}>Inspect</button></div>
                  </article>)}
                  {mapFeatureIndex.length === 0 && <div className="map-utility-empty"><strong>No compatible features</strong><p>Change the active time, clear a spatial filter or feature search, or choose another layer.</p></div>}
                </div>
              </section>}

              {mapUtilityView === "scene" && <section id="map-utility-view-scene" role="region" aria-labelledby="map-utility-title" className="map-utility-section scene-lab-section">
                <div className="map-utility-section-heading"><span>APPEARANCE</span><h3>Make the map your own</h3><p>Choose a map style, then shape its perspective and light.</p></div>
                <div className="appearance-basemap"><label><span>Basemap</span><select aria-label="Appearance basemap" value={basemap} onChange={event => setBasemap(event.target.value as BasemapKey)}>{(Object.keys(BASEMAPS) as BasemapKey[]).map(key => <option key={key} value={key}>{BASEMAPS[key].title}</option>)}</select></label></div>

                <div className="appearance-quick-looks" role="group" aria-label="Terrain starting looks"><button type="button" onClick={() => applyTerrainLook("natural")}>Natural terrain</button><button type="button" onClick={() => applyTerrainLook("topographic")}>Topographic relief</button><button type="button" onClick={() => applyTerrainLook("buildings")}>3D buildings</button></div>
                <section className="scene-preset-grid verified-representation-grid" aria-label="Verified map representations">
                  {([
                    ["2d", "2D map", "Mercator · terrain off"],
                    ["terrain", "Terrain 3D", terrainState === "READY" ? "DEM ready" : terrainState === "ERROR" ? "DEM unavailable" : "Loading DEM"],
                    ["globe", "Globe", "Globe projection"],
                  ] as const).map(([id, title, detail]) => <button key={id} type="button" aria-pressed={!undergroundOpen && (id === "terrain" ? scenePreset === "elevation-3d" : id === "globe" ? projection === "globe" : projection === "mercator" && scenePreset !== "elevation-3d")} onClick={() => chooseMapMenuRepresentation(id)}><span>{id === "terrain" ? "3D" : id === "globe" ? "◎" : "2D"}</span><strong>{title}</strong><small>{detail}</small></button>)}
                  <button type="button" aria-label="Underground recorded layers" aria-pressed={undergroundOpen} onClick={() => { toggleUnderground(); setUndergroundFocusRequest((request) => request + 1); }}><span>↓</span><strong>Underground</strong><small>Recorded logs, cores &amp; aquifers</small></button>
                </section>

                <SceneEffectsControls readings={sceneReadings} view={sceneView} terrain={{ scale: verticalExaggeration, available: runtime.kind === "ready" && terrainState !== "ERROR", onScale: changeTerrainDepth, onGroundView: exploreGround }} drawing={{ mode: terrainDrawingMode, detail: terrainDrawingDetail, status: terrainDrawingStatus, source: terrainSourceFor(terrainProvider), onMode: chooseTerrainDrawingMode, onDetail: chooseTerrainDrawingDetail }} surface={{ mode: terrainSurfaceMode, opacity: terrainSurfaceOpacity, probe: terrainSurfaceProbe, probeEnabled: !measureMode, onMode: chooseTerrainSurfaceMode, onOpacity: chooseTerrainSurfaceOpacity, onProbeCenter: sampleTerrainSurfaceCenter }} exploration={{ orbiting: sceneOrbiting, onOrbit: () => sceneOrbiting ? stopSceneOrbit() : startSceneOrbit(), onLandscape: chooseLandscape }} presentation={{ atmosphere: atmospherePreset, azimuth: lightAzimuth }} camera={{ pitch: view.pitch, bearing: view.bearing, fieldOfView }} cameraReady={runtime.kind === "ready"} onRecipe={chooseSceneRecipe} onLight={changeStudioLight} onCamera={composeSceneCamera} settings={sceneEffects} light={sceneEffects.sunSync ? sunSceneLight(sunAt, view.center[0], view.center[1]) : null} efficient={renderEfficient} reducedMotion={reducedMotion} flyoverActive={flyoverStopIndex !== null} onChange={updateSceneEffects} onFlyover={() => flyoverStopIndex !== null ? stopFlyover() : startFlyover()} />

                <details className="explorer-secondary"><summary>Terrain tools, sources &amp; rendering</summary><div className="explorer-secondary-body">
                <RenderQualityControl value={renderQuality} onChange={chooseRenderQuality} />
                <BasemapCacheControls />
                <label className="appearance-basemap">Terrain elevation source<select aria-label="Terrain elevation source" disabled={scenePreset !== "elevation-3d"} value={terrainProvider} onChange={event => chooseTerrainProviderByHand(event.target.value as "mapzen" | "usgs-3dep")}><option value="mapzen">Mapzen · display DEM</option><option value="usgs-3dep">USGS 3DEP · Kansas detail</option></select></label>
                <section className="renderer-capability-list" aria-label="Renderer capability status">
                  <article data-state="ready"><span>WORKS NOW</span><strong>2D, globe, camera, measurement</strong><small>Direct MapLibre state changes</small></article>
                  <article data-state={terrainState === "ERROR" ? "held" : "context"}><span>{terrainState === "READY" ? "DISPLAY ONLY" : terrainState}</span><strong>Terrain relief + profile preview</strong><small>External DEM; not KFM evidence</small></article>
                  <article data-state="context"><span>CONTEXT ONLY</span><strong>HMS smoke · Shake stations · hazard overlays</strong><small>Live-source controls stay in Layers; no model, alert, waveform, or evidence claim is implied</small></article>
                </section>

                <section className="terrain-height-instrument" aria-labelledby="terrain-height-title">
                  <header><div><span>TOPOGRAPHIC HEIGHT</span><h4 id="terrain-height-title">Elevation color overlay</h4></div><button type="button" role="switch" aria-checked={topographicOverlay} disabled={scenePreset !== "elevation-3d" || terrainState === "ERROR"} onClick={toggleTopographicHeightOverlay}>{topographicOverlay ? "ON" : "OFF"}</button></header>
                  <div className="terrain-height-ramp" aria-label="Elevation color scale from 200 to 1,250 meters"><i /><span>200 m</span><span>400 m</span><span>650 m</span><span>1,000 m</span><span>1,250 m</span></div>
                  <div className="terrain-height-readout">
                    <div><small>CURSOR ELEVATION</small><strong>{terrainElevationReading ? `${terrainElevationReading.feet.toFixed(0)} ft` : terrainElevationUnavailable ? "Unavailable here" : "Move over map"}</strong><span>{terrainElevationReading ? `${terrainElevationReading.meters.toFixed(0)} m · ${terrainElevationReading.latitude.toFixed(5)}, ${terrainElevationReading.longitude.toFixed(5)}` : terrainElevationUnavailable ? "No loaded DEM height at this point" : "Uses the active unexaggerated DEM"}</span></div>
                    <button type="button" disabled={!terrainElevationReading} onClick={() => { setLockedTerrainElevation(terrainElevationReading); announce("Elevation reading locked into the current report context"); }}>Lock for report</button>
                  </div>
                  {lockedTerrainElevation && <p><strong>Report reading:</strong> {lockedTerrainElevation.feet.toFixed(0)} ft / {lockedTerrainElevation.meters.toFixed(0)} m at {lockedTerrainElevation.latitude.toFixed(5)}, {lockedTerrainElevation.longitude.toFixed(5)} from the {lockedTerrainElevation.provider === "usgs-3dep" ? "USGS 3DEP" : "Mapzen"} display DEM. Verify against an admitted elevation source before making an authoritative claim.</p>}
                </section>

                <section className="terrain-investigation" aria-labelledby="terrain-investigation-title">
                  <header><div><span>TERRAIN INVESTIGATION</span><h4 id="terrain-investigation-title">Relief → transect → profile → evidence</h4></div><strong>{verticalExaggeration.toFixed(1)}× DISPLAY</strong></header>
                  <ol><li data-complete={scenePreset === "elevation-3d"}>Enable real display relief</li><li data-complete={measurementGeometryMode === "distance" && measureCoordinateCount >= 2}>Draw and finish a transect</li><li data-complete={terrainProfile.length > 0}>Preview unexaggerated samples</li><li data-complete={Boolean(selected)}>Select a feature for evidence</li></ol>
                  <div className="terrain-investigation-actions"><button type="button" onClick={startTerrainInvestigation}>Start terrain investigation</button><button type="button" onClick={previewTerrainProfile} disabled={terrainState !== "READY" || measurementGeometryMode !== "distance" || measureCoordinateCount < 2}>Preview display profile</button></div>
                  {terrainProfile.length > 0 ? <div className="terrain-profile-preview" aria-label="Display-only terrain profile">
                    <header><strong>{terrainProfile.length} samples</strong><span>{terrainProfile.at(-1)?.distanceMiles.toFixed(1)} mi transect · exaggeration ignored</span></header>
                    <div>{terrainProfile.map((sample, index) => {
                      const elevations = terrainProfile.map((item) => item.elevationMeters);
                      const minimum = Math.min(...elevations);
                      const maximum = Math.max(...elevations);
                      const height = maximum === minimum ? 50 : 18 + ((sample.elevationMeters - minimum) / (maximum - minimum)) * 72;
                      return <i key={`${sample.distanceMiles}-${index}`} style={{ height: `${height}%` }} title={`${sample.distanceMiles.toFixed(1)} mi · ${sample.elevationMeters.toFixed(0)} m`} />;
                    })}</div>
                    <footer><span>{Math.min(...terrainProfile.map((sample) => sample.elevationMeters)).toFixed(0)} m</span><span>Renderer preview only—not analytical elevation or report evidence</span><span>{Math.max(...terrainProfile.map((sample) => sample.elevationMeters)).toFixed(0)} m</span></footer>
                  </div> : <p>Draw a line with two or more points and finish it. The preview samples the active display DEM at unexaggerated scale; the governed analytical 3DEP profile remains held.</p>}
                </section>

                <div className="scene-control-grid">
                  <section className="scene-height-control" aria-labelledby="scene-height-title">
                    <header><div><strong id="scene-height-title">Terrain exaggeration</strong><small>{scenePreset === "elevation-3d" ? "External DEM display only" : "Enable Terrain 3D to adjust"}</small></div><output htmlFor="scene-height">{scenePreset === "elevation-3d" ? `${verticalExaggeration.toFixed(1)}×` : "OFF"}</output></header>
                    <input id="scene-height" type="range" min="0.1" max="3" step="0.1" value={verticalExaggeration} disabled={scenePreset !== "elevation-3d" || terrainState === "ERROR"} onChange={(event) => { const next = Number(event.target.value); verticalExaggerationRef.current = next; setVerticalExaggeration(next); }} />
                    <div><span>0.1×</span><span>1× physical</span><span>3×</span></div>
                    {scenePreset === "elevation-3d" && <div className="terrain-exaggeration-presets" role="group" aria-label="Terrain exaggeration presets">
                      {[1, 2, 2.5, 3].map((scale) => <button key={scale} type="button" aria-pressed={verticalExaggeration === scale} onClick={() => { verticalExaggerationRef.current = scale; setVerticalExaggeration(scale); }}>{scale.toFixed(scale === 1 ? 0 : 2).replace(/0$/, "")}×</button>)}
                    </div>}
                  </section>
                  <section className="scene-camera-controls" aria-label="3D camera orientation">
                    <header><strong>Camera</strong><small>{Math.round(view.pitch)}° pitch · {Math.round(view.bearing)}° bearing</small></header>
                    <div><button type="button" onClick={() => orientSceneCamera(48, -18)}>Oblique NW</button><button type="button" onClick={() => orientSceneCamera(54, 28)}>Oblique SE</button><button type="button" onClick={() => orientSceneCamera(0, view.bearing)}>Top down</button><button type="button" onClick={() => orientSceneCamera(view.pitch, 0)}>North up</button><button type="button" onClick={() => sceneOrbiting ? stopSceneOrbit() : startSceneOrbit()} aria-pressed={sceneOrbiting}>{sceneOrbiting ? "Stop orbit" : "Orbit 90°"}</button><button type="button" disabled={!selected} onClick={() => selected && mapRef.current?.easeTo({ center: [selected.properties.focusLng, selected.properties.focusLat], zoom: Math.max(view.zoom, 8.5), pitch: 58, bearing: -24, duration: motionDuration(650) })}>Focus selection</button></div>
                  </section>
                  <section className="scene-structures-control" data-state={structures3DState} aria-labelledby="scene-structures-title">
                    <header><div><span>STRUCTURES 3D</span><strong id="scene-structures-title">Provider heights only</strong><small>{STRUCTURE_3D_SOURCE.organization} · city-scale context</small></div><output>{structures3DState}</output></header>
                    <div className="scene-structures-body">
                      <button type="button" role="switch" aria-checked={structures3DEnabled} onClick={toggleStructureExtrusions}>{structures3DEnabled ? "Hide structures" : "Show structures"}</button>
                      <div role="group" aria-label="Structure focus presets">{STRUCTURE_FOCUS_PRESETS.map((preset) => <button key={preset.id} type="button" onClick={() => focusStructureScene(preset)}>{preset.label.replace("Focus ", "")}</button>)}</div>
                      <p>{structures3DState === "READY" ? "Building heights are supplied by the active Liberty style. Missing heights remain missing." : structures3DState === "UNAVAILABLE" ? "The current basemap does not expose a height-backed building layer." : structures3DEnabled ? "Requesting the provider building layer…" : "Off by default; this display carrier does not change evidence or report measurements."}</p>
                    </div>
                  </section>
                </div>

                <section className="terrain-source-ledger" aria-labelledby="terrain-source-ledger-title">
                  <header><div><span>3D SOURCE LEDGER</span><h4 id="terrain-source-ledger-title">Terrain, structures, authoritative candidate + renderer contract</h4></div><strong>{scenePreset === "elevation-3d" ? terrainState : "ROLE-SEPARATED"}</strong></header>
                  {scenePreset === "elevation-3d" && <div className="terrain-runtime-actions" role="status" aria-live="polite">
                    <p><strong>Live terrain:</strong> {terrainState === "READY" ? `${terrainProvider === "usgs-3dep" ? "USGS 3DEP" : "Mapzen"} DEM ready at ${verticalExaggeration.toFixed(2)}×` : terrainState === "ERROR" ? "DEM request failed; the 2D evidence path remains usable." : `Requesting ${terrainProvider === "usgs-3dep" ? "USGS 3DEP" : "Mapzen"} elevation tiles…`}</p>
                    {terrainState === "ERROR" && <button type="button" onClick={retryTerrain}>Retry terrain source</button>}
                  </div>}
                  <div>{[...TERRAIN_SOURCES, STRUCTURE_3D_SOURCE].map((source) => <article key={source.id} data-status={source.status}>
                    <header><span>{source.organization}</span><strong>{source.status.replaceAll("_", " ")}</strong></header>
                    <h5>{source.title}</h5>
                    <dl><div><dt>Role</dt><dd>{source.role}</dd></div><div><dt>Resolution</dt><dd>{source.resolution}</dd></div><div><dt>Format</dt><dd>{source.format}</dd></div><div><dt>Coverage</dt><dd>{source.coverage}</dd></div></dl>
                    <p>{source.boundary}</p>
                    <a href={source.sourceUrl} target="_blank" rel="noreferrer">Open primary source ↗</a>
                  </article>)}</div>
                  <p className="terrain-source-law">Rendered relief is visual context. Only a pinned, lineage-preserving, reviewed and released KFM artifact may support an elevation claim.</p>
                </section>

                <aside className="map-utility-boundary" data-tone="warning"><strong>3D preserves the 2D evidence path.</strong><p>Terrain 3D samples an external raster DEM for display and may exaggerate it; Structures 3D extrudes only provider-supplied building heights. Neither changes evidence, fills missing heights, or asserts a KFM release. No synthetic elevation extrusion layer is offered. Select any visible feature to inspect the same Evidence Drawer used in 2D.</p></aside>
                </div></details>
              </section>}

              {mapUtilityView === "connections" && <section id="map-utility-view-connections" role="region" aria-labelledby="map-utility-title" className="map-utility-section source-connections-section">
                <div className="map-utility-section-heading"><span>SOURCE CONNECTIONS</span><h3>Official feeds + network context + local registry</h3><p>Inspect bounded official adapters and raster services, external display carriers, and every site-local registry connection. Operational context remains separate from KFM evidence.</p></div>
                <div className="source-connection-summary" aria-label="Source connection summary">
                  <article><span>READY</span><strong>{sourceStateCounts.ready}/{LAYER_REGISTRY.length}</strong><small>MapLibre sources loaded</small></article>
                  <article><span>VISIBLE</span><strong>{visibleCount}</strong><small>Registry layers drawing now</small></article>
                  <article><span>RENDERERS</span><strong>{LAYER_REGISTRY.reduce((count, layer) => count + layer.renderers.length, 0)}</strong><small>Style layers connected</small></article>
                  <article><span>NETWORK</span><strong>{visibleOfficialCount + activeExternalContextCount}/{OFFICIAL_CONTEXT_SOURCES.length + EXTERNAL_CONTEXT_SOURCES.length}</strong><small>Official + external carriers selected</small></article>
                </div>
                <div className="source-connection-toolbar">
                  <label><i aria-hidden="true">⌕</i><span className="sr-only">Search source connections</span><input type="search" value={connectionQuery} onChange={(event) => setConnectionQuery(event.target.value)} placeholder="Layer, source ID, domain, or format" /></label>
                  <label><span className="sr-only">Filter source connections</span><select value={connectionFilter} onChange={(event) => setConnectionFilter(event.target.value as typeof connectionFilter)}><option value="ALL">All connections</option><option value="VISIBLE">Visible only</option><option value="READY">Ready only</option><option value="ERROR">Errors only</option></select></label>
                </div>
                <section className="official-connection-ledger" aria-labelledby="official-connection-ledger-title">
                  <header><div><span>OFFICIAL SOURCE PIPELINES</span><h4 id="official-connection-ledger-title">Fixed Kansas adapters + disclosed raster services</h4></div><strong>{officialFeatureCount} SELECTED FEATURES</strong></header>
                  <p>Only allowlisted endpoints are connected. Feed failures stay visible; zero features is time-stamped and never interpreted as statewide safety or completeness.</p>
                  <div className="official-connection-grid">{filteredOfficialContextConnections.map(({ source, visible, activeAtFrame, state, featureCount, retrievedAt, limitation, temporalSupport }) => <article className="official-connection-card" key={source.id} data-state={state} data-held={visible && !activeAtFrame}>
                    <header><div><span>{source.kind.replaceAll("_", " ")}</span><h5>{source.title}</h5><code>{source.endpointLabel}</code></div><strong>{visible && !activeAtFrame ? "HELD" : state.toUpperCase()}</strong></header>
                    <div className="official-connection-path"><span>OFFICIAL</span><i>→</i><span>{source.kind === "SNAPSHOT_GEOJSON" ? "DATED SNAPSHOT" : source.apiPath || source.managedAdapterPath ? "FIXED ADAPTER" : "WMS / TILES"}</span><i>→</i><span>MAP CONTEXT</span><i>⊣</i><span>EVIDENCE HELD</span></div>
                    <dl><div><dt>Mapped</dt><dd>{featureCount ?? (source.apiPath || source.managedAdapterPath || source.kind === "SNAPSHOT_GEOJSON" ? "NOT LOADED" : "RASTER TILES · NO FEATURES")}</dd></div><div><dt>Retrieved</dt><dd>{retrievedAt ? new Date(retrievedAt).toLocaleString() : "No tile retrieval clock"}</dd></div><div><dt>Cadence</dt><dd>{source.cadence}</dd></div><div><dt>Temporal support</dt><dd>{temporalSupport.axis.replaceAll("-", " ")} · {temporalSupport.supportedFrames.map(formatTimelineStep).join(", ")}</dd></div><div><dt>Evidence role</dt><dd>{source.evidenceRole.replaceAll("_", " ")}</dd></div></dl>
                    <p>{limitation ?? source.boundary}</p><aside><strong>Failure boundary</strong><span>{source.fallback}</span></aside>
                    <footer><button type="button" onClick={() => setOfficialContextVisible(source.id, !visible)}>{visible ? "Hide" : "Show"}</button>{source.apiPath && <button type="button" disabled={state === "loading"} onClick={() => void refreshOfficialContext(source.id as OfficialContextFeedId)}>Refresh</button>}{source.id === "usgs-streamflow" && <button type="button" disabled={state === "loading" || !activeAtFrame} onClick={() => void refreshSelectedStreamflow()}>Refresh observations</button>}{source.id === "noaa-nwps-gauges" && <button type="button" disabled={state === "loading" || !activeAtFrame} onClick={() => void refreshNoaaHydrologyNetwork()}>Refresh status</button>}<a href={source.sourceUrl} target="_blank" rel="noreferrer">Source ↗</a><a href={source.serviceUrl} target="_blank" rel="noreferrer">{source.id === "raspberry-shake-stations" ? "StationView ↗" : "Service ↗"}</a></footer>
                  </article>)}</div>
                  <footer className="official-pipeline-contract"><span>Governance: <a href="https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3393" target="_blank" rel="noreferrer">#3393 source-family decision</a></span><span>Hydrology: <a href="https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3372" target="_blank" rel="noreferrer">#3372 governed slice</a></span><span>Deployment: <a href="https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4418" target="_blank" rel="noreferrer">#4418 receipt hold</a></span></footer>
                </section>
                <section className="external-context-ledger" aria-labelledby="external-context-ledger-title">
                  <header><div><span>EXTERNAL NETWORK CONTEXT</span><h4 id="external-context-ledger-title">Browser-requested display carriers</h4></div><strong>{activeExternalContextCount} SELECTED</strong></header>
                  <p>Only the selected carriers make map requests. The local Midnight and Prairie styles make no basemap request. Rendering success proves display availability only—not source admission, fitness, accuracy, freshness, or evidence support.</p>
                  <div className="external-context-grid">
                    {filteredExternalContextConnections.map(({ source, active, state }) => <article className="external-context-card" key={source.id} data-state={state.toLowerCase()}>
                      <header><div><span>{source.kind.replaceAll("_", " ")} · {source.requestMode.replaceAll("_", " ")}</span><h5>{source.title}</h5><code>{source.endpointLabel}</code></div><strong>{state.replaceAll("_", " ")}</strong></header>
                      <dl><div><dt>Capability</dt><dd>{source.capabilities.join(" · ").replaceAll("_", " ")}</dd></div><div><dt>Evidence role</dt><dd>{source.evidenceRole.replaceAll("_", " ")}</dd></div><div><dt>Export effect</dt><dd>{source.exportEffect.replaceAll("_", " ")}</dd></div><div><dt>Attribution</dt><dd>{source.attribution}</dd></div></dl>
                      <p>{source.boundary}</p><aside><strong>Fallback</strong><span>{source.fallback}</span></aside>
                      <footer><span>{active ? "SELECTED BY CURRENT VIEW" : "NO REQUEST FROM CURRENT VIEW"}</span><a href={source.sourceUrl} target="_blank" rel="noreferrer">Open source record ↗</a></footer>
                    </article>)}
                  </div>
                </section>
                <div className="source-connection-subheading"><span>SITE-LOCAL REGISTRY</span><strong>{Object.keys(sourceProbeCounts).length} explicitly probed</strong></div>
                <div className="source-connection-list">
                  {filteredSourceConnections.map(({ layer, state, activity, visible, compatibleCount, viewportCount, probeCount }) => <article key={layer.id} className="source-connection-card" data-state={state} data-visible={visible}>
                    <header><div><span>{layer.domain} · {layer.sourceType}</span><h4>{layer.title}</h4><code>{layer.sourceId}</code></div><strong>{state.toUpperCase()}</strong></header>
                    <div className="source-connection-path" aria-label={`${layer.title} renderer connection`}><span>REGISTRY</span><i>→</i><span>{activity}</span><i>→</i><span>{layer.renderers.length} RENDERER{layer.renderers.length === 1 ? "" : "S"}</span><i>→</i><span>{visible ? "DRAWING" : "HIDDEN"}</span></div>
                    <dl><div><dt>Time-compatible</dt><dd>{compatibleCount}</dd></div><div><dt>In viewport</dt><dd>{viewportCount}</dd></div><div><dt>Source probe</dt><dd>{probeCount === undefined ? "NOT RUN" : `${probeCount} UNIQUE`}</dd></div><div><dt>Attribution</dt><dd>{layer.attribution}</dd></div></dl>
                    <footer><button type="button" onClick={() => setVisibility((current) => { const next = { ...current, [layer.id]: !current[layer.id] }; visibilityRef.current = next; return next; })}>{visible ? "Hide" : "Show"}</button><button type="button" onClick={() => zoomToLayer(layer)}>Fit</button><button type="button" onClick={() => probeSourceConnection(layer)} disabled={state !== "ready"}>Probe source</button><button type="button" onClick={() => inspectSourceConnection(layer)}>Records</button></footer>
                  </article>)}
                  {filteredSourceConnections.length === 0 && filteredExternalContextConnections.length === 0 && filteredOfficialContextConnections.length === 0 && <div className="map-utility-empty"><strong>No source connections match</strong><p>Clear the search or choose another connection state.</p></div>}
                </div>
                <aside className="map-utility-boundary" data-tone="warning"><strong>Connection status is renderer health, not source admission.</strong><p>The current view may contact the external carriers disclosed above; provider resources and availability remain external. A READY source or successful query does not prove rights, freshness, evidence, policy approval, release, or publication.</p></aside>
              </section>}

              {mapUtilityView === "import" && <section id="map-utility-view-import" role="region" aria-labelledby="map-utility-title" className="map-utility-section import-preview-section">
                <div className="map-utility-section-heading"><span>LOCAL IMPORT PREVIEW</span><h3>Inspect before any admission handoff</h3><p>Open a small KML or GeoJSON file in this browser. Supported points, lines, and polygons can appear as a temporary MapLibre overlay while structure, extent, temporal fields, attribution gaps, and sensitivity signals remain explicit.</p></div>
                <div className="import-path-grid" aria-label="Import preview boundary">
                  <article><span>01</span><strong>Parse locally</strong><small>No upload, network link, or external asset fetch.</small></article>
                  <article><span>02</span><strong>Inspect + preview</strong><small>MapLibre draws only supported local geometry.</small></article>
                  <article><span>03</span><strong>Stop at review</strong><small>No registry, report-data, evidence, or publication effect.</small></article>
                </div>
                <label className="import-dropzone" data-busy={importBusy} onDragOver={(event) => { event.preventDefault(); event.dataTransfer.dropEffect = "copy"; }} onDrop={(event) => { event.preventDefault(); void inspectImportFile(event.dataTransfer.files[0]); }}>
                  <input ref={importInputRef} type="file" accept=".kml,.geojson,.json,application/geo+json,application/vnd.google-earth.kml+xml" onChange={(event) => void inspectImportFile(event.target.files?.[0])} />
                  <span aria-hidden="true">⇧</span><strong>{importBusy ? "Inspecting file…" : "Choose or drop KML / GeoJSON"}</strong><small>Maximum 2 MB · browser memory only · raw file is never stored</small>
                </label>
                {importError && <div className="import-error" role="alert"><strong>Preview blocked</strong><p>{importError}</p></div>}
                {!importPreview && !importError && <div className="map-utility-empty import-empty"><strong>No local file inspected</strong><p>Use this surface for structure and map-fit review. It is intentionally not a source-ingestion or upload workflow.</p></div>}
                {importPreview && <>
                  <div className="import-preview-summary" aria-label="Local import preview summary">
                    <article><span>FORMAT</span><strong>{importPreview.sourceFormat}</strong><small>{(importPreview.fileSizeBytes / 1024).toFixed(1)} KB</small></article>
                    <article><span>FEATURES</span><strong>{importPreview.featureCount}</strong><small>{importPreview.invalidFeatureCount} invalid</small></article>
                    <article><span>GEOMETRIES</span><strong>{Object.values(importPreview.geometryCounts).reduce((sum, count) => sum + count, 0)}</strong><small>{Object.keys(importPreview.geometryCounts).length} types</small></article>
                    <article data-state={importPreview.renderAllowed ? "PASS" : "BLOCK"}><span>MAP PREVIEW</span><strong>{importPreview.renderAllowed ? importPreviewVisible ? "VISIBLE" : "HIDDEN" : "BLOCKED"}</strong><small>{importPreview.coverage.replaceAll("_", " ").toLowerCase()}</small></article>
                  </div>
                  <article className="import-file-card"><header><div><span>INSPECTED FILE</span><h4>{importPreview.fileName}</h4></div><strong>{importPreview.authority}</strong></header><dl>
                    <div><dt>Bounds</dt><dd>{importPreview.bounds ? importPreview.bounds.map((value) => value.toFixed(4)).join(" · ") : "NO GEOMETRY"}</dd></div>
                    <div><dt>Attribution</dt><dd>{importPreview.attribution ?? "NOT FOUND"}</dd></div>
                    <div><dt>Temporal fields</dt><dd>{importPreview.temporalFields.join(", ") || "NONE DETECTED"}</dd></div>
                    <div><dt>Potential sensitivity keys</dt><dd>{importPreview.sensitivitySignals.join(", ") || "NONE DETECTED"}</dd></div>
                  </dl></article>
                  <div className="import-geometry-grid">{Object.entries(importPreview.geometryCounts).map(([geometry, count]) => <article key={geometry}><span>{geometry}</span><strong>{count}</strong></article>)}</div>
                  <div className="import-check-list" aria-label="Import inspection checks">{importPreview.checks.map((check) => <article key={check.id} data-state={check.state}><span>{check.label}</span><p>{check.detail}</p><strong>{check.state}</strong></article>)}</div>
                  <div className="map-utility-actions import-preview-actions"><button type="button" disabled={!importPreview.renderAllowed} onClick={toggleImportPreview}>{importPreviewVisible ? "Hide preview" : "Show preview"}</button><button type="button" disabled={!importPreview.renderAllowed} onClick={() => fitImportPreview()}>Fit preview</button><button type="button" onClick={() => void copyImportPreviewAudit()}>Copy inspection</button><button type="button" onClick={clearImportPreview}>Clear</button></div>
                </>}
                <aside className="map-utility-boundary" data-tone="warning"><strong>Temporary Places, KFM-style: inspectable but unadmitted.</strong><p>The overlay never enters the Layer Catalog, Evidence Drawer, saved workspaces, reports, exports, registry, or repository. URL references, KML network links, overlays, models, tracks, and external resources are counted or warned about and are never fetched.</p></aside>
              </section>}

              {mapUtilityView === "compare" && <section id="map-utility-view-compare" role="region" aria-labelledby="map-utility-title" className="map-utility-section layer-compare-section">
                <div className="map-utility-section-heading"><span>COMPARE</span><h3>Time + layer investigation</h3><p>Compare catalog availability across two times, then inspect two registry layers without flattening source role, release posture, or sensitivity into a single score.</p></div>
                <section className="road-year-study" aria-labelledby="road-year-study-title">
                  <header><div><span>HISTORICAL ROAD STUDY · LOCAL PREVIEW</span><h4 id="road-year-study-title">Candidate road linework by map edition</h4></div><strong>{roadStudyLayers.length}/{ROAD_STUDY_MAX_LAYERS} loaded</strong></header>
                  <p>Choose local GeoJSON linework for each map edition, then compare up to four editions with separate colors and opacity. The available derived files trace colored marks printed on maps; they are incomplete and approximately positioned. This preview does not detect or verify road changes. Missing years remain unknown.</p>
                  <div className="road-study-import">
                    <label>Map edition<select value={roadStudyEditionId} onChange={(event) => setRoadStudyEditionId(event.target.value)}>{ROAD_MAP_EDITIONS.map((edition) => <option key={edition.id} value={edition.id} disabled={edition.localPdfState === "BLANK"}>{edition.label}{edition.localPdfState === "BLANK" ? " · blank local PDF" : ""}</option>)}</select></label>
                    <label>Candidate road-line GeoJSON<input ref={roadStudyInputRef} type="file" accept=".geojson,.json,application/geo+json" disabled={roadStudyBusy} onChange={(event) => void inspectRoadStudyFile(event.target.files?.[0])} /></label>
                  </div>
                  <small>Line geometry only · up to 2 MB and 2,500 lines per edition · browser memory only · no upload, saved workspace, report, or release effect.</small>
                  {roadStudyError && <p className="road-study-error" role="alert">{roadStudyError}</p>}
                  <div className="road-study-layers">{roadStudyLayers.map((layer) => <article key={layer.editionId}>
                    <div><strong>{layer.editionLabel}</strong><small>{layer.featureCount} candidate line{layer.featureCount === 1 ? "" : "s"} · {layer.fileName}</small></div>
                    <label className="road-study-color">Color<input type="color" value={layer.color} onChange={(event) => setRoadStudyLayers((current) => current.map((entry) => entry.editionId === layer.editionId ? { ...entry, color: event.target.value } : entry))} aria-label={`${layer.editionLabel} road color`} /></label>
                    <label className="road-study-opacity">Opacity <output>{Math.round(layer.opacity * 100)}%</output><input type="range" min="0" max="100" value={Math.round(layer.opacity * 100)} onChange={(event) => setRoadStudyLayers((current) => current.map((entry) => entry.editionId === layer.editionId ? { ...entry, opacity: Number(event.target.value) / 100 } : entry))} aria-label={`${layer.editionLabel} road opacity`} /></label>
                    <button type="button" onClick={() => setRoadStudyLayers((current) => current.map((entry) => entry.editionId === layer.editionId ? { ...entry, visible: !entry.visible } : entry))}>{layer.visible ? "Hide" : "Show"}</button>
                    <button type="button" onClick={() => setRoadStudyLayers((current) => current.filter((entry) => entry.editionId !== layer.editionId))}>Remove</button>
                  </article>)}{roadStudyLayers.length === 0 && <div className="map-utility-empty"><strong>No road linework loaded</strong><p>Choose local candidate GeoJSON files to compare printed map editions. The Site does not bundle or publish the quarantined road traces.</p></div>}</div>
                  <footer>Source leads: <a href={KDOT_HISTORIC_STATE_MAPS_URL} target="_blank" rel="noreferrer">KDOT historic state maps ↗</a> · <a href={KDOT_PAST_COUNTY_MAPS_URL} target="_blank" rel="noreferrer">KDOT county map archive ↗</a>. Written permission was reported by the project owner; its exact terms and each map-to-line transform still need review before repository admission or publication.</footer>
                </section>
                <div className="map-utility-empty"><strong>No released domain-layer pair is available</strong><p>Use the source-backed map layers for observed or dated context. A/B domain comparison will return when two governed layers are available; this view does not invent records to fill the gap.</p></div>
              </section>}

              {mapUtilityView === "measure" && <section id="map-utility-view-measure" role="region" aria-labelledby="map-utility-title" className="map-utility-section">
                <div className="map-utility-section-heading"><span>MEASURE</span><h3>Browser-local screen measurement</h3><p>Choose a geometry, then click the map to add points. Undo resumes a completed measurement for explicit editing.</p></div>
                <div className="map-control-group"><header><strong>Draw and measure</strong><span>{measureMode ? "ADDING POINTS" : measurementGeometryMode ? "COMPLETE / PAUSED" : analysisArea ? "RECTANGLE AOI SET" : "IDLE"}</span></header><div className="map-choice-grid map-draw-grid"><button type="button" aria-label="Point" aria-pressed={measurementGeometryMode === "point"} onClick={() => beginMapMeasurement("point")}><strong>Point</strong><small>One browser-local marker</small></button><button type="button" aria-label="Line" aria-pressed={measurementGeometryMode === "distance"} onClick={() => beginMapMeasurement("distance")}><strong>Line</strong><small>Distance approximation</small></button><button type="button" aria-label="Polygon" aria-pressed={measurementGeometryMode === "area"} onClick={() => beginMapMeasurement("area")}><strong>Polygon</strong><small>Area approximation</small></button><button type="button" aria-label="Rectangle" aria-pressed={Boolean(analysisArea)} onClick={captureAnalysisArea} disabled={locationCameraRedacted}><strong>Rectangle</strong><small>Capture current viewport AOI</small></button></div><p className="map-control-note">Point, line, and polygon geometry stays in this browser. Rectangle captures the current viewport or use Shift-drag in report-area mode for a custom box. None is admitted evidence.</p></div>
                <div className="map-control-group"><header><strong>Units</strong><span>Also updates the MapLibre scale bar</span></header><div className="map-segmented-control"><button type="button" aria-pressed={measureUnit === "imperial"} onClick={() => changeMeasureUnit("imperial")}>Miles / sq mi</button><button type="button" aria-pressed={measureUnit === "metric"} onClick={() => changeMeasureUnit("metric")}>Kilometers / km²</button></div></div>
                <article className="map-measure-status" aria-live="polite"><span>{measurementGeometryMode?.toUpperCase() ?? "NO MEASUREMENT"}</span><strong>{measurement}</strong><small>{measureMode ? "Click the map to add points." : measurementGeometryMode ? "Finished geometry remains on the map until cleared." : "Select distance or area to begin."}</small></article>
                <div className="map-utility-actions"><button type="button" onClick={undoMeasurementPoint} disabled={!measurementGeometryMode}>Undo point</button><button type="button" onClick={finishMeasurement} disabled={!measureMode}>Finish</button><button type="button" onClick={clearMeasurement} disabled={!measurementGeometryMode}>Clear</button></div>
                <aside className="map-utility-boundary" data-tone="warning"><strong>Screen measurement — not survey, cadastral, legal, or evidence.</strong><p>Results are approximate, browser-local, and excluded from context receipts and public-safe exports.</p></aside>
              </section>}

              {mapUtilityView === "export" && <section id="map-utility-view-export" role="region" aria-labelledby="map-utility-title" className="map-utility-section export-review-section">
                <div className="map-utility-section-heading"><span>EXPORT REVIEW</span><h3>Preview trust before download</h3><p>The outward artifact carries workspace, map context, separate temporal fields, visible layers, attribution, evidence posture, release/correction state, and redaction results.</p></div>
                <div className="export-review-summary" aria-label="Export review summary">
                  <article><span>FORMAT</span><strong>PUBLIC SAFE V2</strong><small>External context</small></article>
                  <article><span>LAYERS</span><strong>{activeLayers.length}</strong><small>Each keeps attribution</small></article>
                  <article><span>SELECTION</span><strong>{selected && !selectedTimeMismatch ? "1" : "0"}</strong><small>{selectedTimeMismatch ? "OUT-OF-TIME SELECTION HELD" : selected?.properties.evidenceState ?? "MAP CONTEXT ONLY"}</small></article>
                  <article data-state={exportReview.withheldFeatureCount ? "REDACTED" : "PASS"}><span>WITHHELD</span><strong>{exportReview.withheldFeatureCount}</strong><small>Protected geometry count</small></article>
                </div>
                <div className="export-preflight" aria-label="Export preflight checks">
                  {exportReview.checks.map((check) => <article key={check.id} data-state={check.state}><span>{check.label}</span><p>{check.detail}</p><strong>{check.state}</strong></article>)}
                </div>
                <div className="map-control-group temporal-axis-inspector"><header><strong>Temporal-axis inspector</strong><span>Axes stay separate</span></header><dl>
                  <div><dt>Active map time</dt><dd>{temporalScopeLabel}</dd></div>
                  <div><dt>Feature / source year</dt><dd>{selected?.properties.year ?? "NO SELECTION"}</dd></div>
                  <div><dt>Sweep query</dt><dd>{temporalMode.replaceAll("-", " ")} · {temporalStepRule.replaceAll("-", " ")} · interpolation off</dd></div>
                  <div><dt>Layer temporal rule</dt><dd>{selected?.layer.temporal?.mode ?? "layer-specific / untimed"}</dd></div>
                  <div><dt>Source time</dt><dd>{selected?.layer.sourceTime ?? "NO SELECTION"}</dd></div>
                  <div><dt>Last update</dt><dd>{selected?.properties.lastUpdate ?? "NO SELECTION"}</dd></div>
                  <div><dt>Release time</dt><dd>{selected?.layer.releaseTime ?? "NO SELECTION"}</dd></div>
                  <div><dt>Review posture</dt><dd>{selected?.properties.reviewState ?? "NO SELECTION"}</dd></div>
                  <div><dt>Correction time/state</dt><dd>{selected?.properties.correctionState ?? "NO SELECTION"} · time not modeled</dd></div>
                </dl><p>External sources have separate observation, publication, and retrieval times. Missing timestamps remain missing in exports.</p></div>
                <article className="export-manifest-preview"><header><span>MANIFEST PREVIEW</span><strong>{exportReview.downloadAllowed ? "READY TO DOWNLOAD" : "BLOCKED"}</strong></header><pre>{JSON.stringify({ format: exportReview.payload.format, authority: exportReview.payload.authority, workspace: currentWorkspace, exportedAt: exportGeneratedAt, publicEffect: exportReview.payload.publicEffect, redaction: exportReview.payload.trust, effects: "NONE" }, null, 2)}</pre></article>
                <div className="map-utility-actions export-actions"><button type="button" onClick={() => void copyExportManifest()}>Copy reviewed manifest</button><button type="button" disabled={!exportReview.downloadAllowed} onClick={downloadPublicSafeExport}>Download public-safe JSON</button></div>
                <aside className="map-utility-boundary" data-tone="privacy"><strong>Evidence-preserving export boundary</strong><p>The download is a browser-local demonstration artifact. It cannot admit a source, prove an EvidenceBundle, change policy or review state, release, deploy, promote, or publish KFM data.</p></aside>
              </section>}

              {mapUtilityView === "diagnostics" && <section id="map-utility-view-diagnostics" role="region" aria-labelledby="map-utility-title" className="map-utility-section">
                <div className="map-utility-section-heading"><span>DIAGNOSTICS</span><h3>Site runtime + repository boundary</h3><p>Local browser health is separate from KFM dependency admission, governed readiness, release, or publication.</p></div>
                <div className="map-runtime-summary">
                  <article data-state={runtime.kind}><span>SITE RUNTIME</span><strong>{runtime.kind.toUpperCase()}</strong><small>{runtime.message}</small></article>
                  <article><span>STYLE</span><strong>{styleReady ? "LOADED" : "WAITING"}</strong><small>{BASEMAPS[basemap].title} · {projection}</small></article>
                  <article><span>SOURCES</span><strong>{sourceStateCounts.ready} READY</strong><small>{sourceStateCounts.loading} loading · {sourceStateCounts.error} error</small></article>
                </div>
                <section className="map-control-group maplibre-runtime-proof" aria-labelledby="maplibre-runtime-proof-title">
                  <header><strong id="maplibre-runtime-proof-title">MapLibre {EXPECTED_MAPLIBRE_VERSION} runtime proof</strong><span>Live browser checks</span></header>
                  <div className="map-status-list" aria-label="MapLibre browser capability status">{maplibreCapabilityChecks.map((check) => <article className="map-status-row" key={check.id} data-state={check.state}><div><span>{check.label}</span><p>{check.detail}</p></div><strong>{check.state}</strong></article>)}</div>
                </section>
                <section className="runtime-seam-lab" aria-labelledby="runtime-seam-title">
                  <header><div><span>REPOSITORY-PROVEN PORT · SITE-LOCAL REPLAY</span><h4 id="runtime-seam-title">Renderer-neutral runtime seam</h4><p>Replay initialize → validated selection binding → dispose without importing the repository package, MapLibre, or a network source.</p></div><strong data-state={runtimeSeamState}>{runtimeSeamState}</strong></header>
                  <div className="runtime-seam-state"><span>Reason / effect</span><p>{runtimeSeamReason}</p><small>Current selection: {selected ? `${selected.featureId} · ${selected.properties.evidenceState}` : "NONE"}</small></div>
                  <div className="map-utility-actions"><button type="button" onClick={initializeRuntimeSeam}>Initialize Null seam</button><button type="button" onClick={bindRuntimeSeamSelection} disabled={runtimeSeamState === "IDLE" || runtimeSeamState === "DISPOSED"}>Bind current selection</button><button type="button" onClick={disposeRuntimeSeam} disabled={runtimeSeamState === "IDLE" || runtimeSeamState === "DISPOSED"}>Dispose</button><button type="button" onClick={() => { setRuntimeSeamState("IDLE"); setRuntimeSeamReason("Awaiting deterministic replay"); }}>Reset replay</button></div>
                  <footer>VERIFIED REPOSITORY SLICE: MapRuntimePort + NullMapRuntime + governed evidence binding · CONCRETE MAPLIBRE ADAPTER: HOLD</footer>
                </section>
                <div className="map-status-list" aria-label="MapLibre repository status">{MAPLIBRE_REPOSITORY_STATUS.map((status) => <article className="map-status-row" key={status.id} data-state={status.state}><div><span>{status.label}</span><p>{status.detail}</p></div><strong>{status.state}</strong></article>)}</div>
                <div className="map-utility-actions"><button type="button" onClick={reapplyRendererState}>Reapply local state</button><button type="button" onClick={restoreLastKnownGoodView}>Restore prior camera</button><button type="button" onClick={() => void copyMapDiagnostics()}>Copy redacted diagnostics</button></div>
                <div className="map-control-group"><header><strong>Capability gates</strong><span>Honest interfaces for unavailable work</span></header><div className="map-capability-grid">{MAP_CAPABILITY_GATES.map((gate) => <article className="map-capability-card" key={gate.id}><header><strong>{gate.title}</strong><span>{gate.state}</span></header><p>{gate.reason}</p><small>{gate.safeInterface}</small></article>)}</div></div>
                <aside className="map-utility-boundary"><strong>Renderer evidence boundary</strong><p>This Site runs MapLibre {EXPECTED_MAPLIBRE_VERSION} with same-origin worker assets, a selected external basemap or local style, optional external DEM terrain, and provider-backed source overlays. GitHub proves an exact dependency, a bounded concrete adapter, the renderer-neutral port, and deterministic Null runtime; broader authenticated, performance, governed-terrain, accessibility, and long-session readiness remain held.</p></aside>
              </section>}
            </div>
          </aside>

          {measurementGeometryMode && <div className="measurement-readout" role="region" aria-label="Active screen measurement"><span>{measurementGeometryMode.toUpperCase()} · {measureMode ? "ACTIVE" : "COMPLETE"}</span><strong aria-live="polite">{measurement}</strong><div><button type="button" onClick={undoMeasurementPoint}>Undo</button><button type="button" onClick={finishMeasurement} disabled={!measureMode}>Finish</button><button type="button" onClick={clearMeasurement}>Clear</button></div></div>}

          <nav className="map-mobile-actions" aria-label="Mobile map actions">
            <button type="button" onClick={(event) => openAtlasPanel("layers", event.currentTarget)}>Map layers <b>{selectedMapLayerCount}</b></button>
            <button type="button" onClick={(event) => openAtlasPanel("places", event.currentTarget)}>Places <b>{savedWorkspaces.length}</b></button>
            <button type="button" onClick={(event) => { openSourceStatus(event.currentTarget); setRightOpen(false); setTimelineOpen(false); }}>Sources</button>
            <button type="button" onClick={() => { setCurrentWorkspace("explore"); dismissMapUtilityWithoutFocus(); setTimelineOpen(true); setLeftOpen(false); setRightOpen(false); }}>Time <b>{temporalScopeLabel}</b></button>
            <button type="button" onClick={openMapSettings}>Style</button>
          </nav>

          {undergroundOpen && <UndergroundPanel entryFocusRequest={undergroundFocusRequest} basemap={basemap} onBasemap={setBasemap} onLayers={openLayerCatalogFromUtility} key={undergroundRestoreKey} map={mapRef.current} initialContext={subsurfaceContext} year={year} onPresent={() => { setPlaying(false); commitTemporalFrame(OFFICIAL_CONTEXT_PRESENT_FRAME, "Present map year applied; sample inventory dates remain separate from drilling dates"); }}
            redacted={subsurfacePrivate || locationCameraRedacted || locationDerivedViewRef.current}
            onTerrain={() => activateMapRepresentation("terrain")} onFlatMap={() => activateMapRepresentation("2d")} readElevation={point => mapRef.current && terrainState === "READY" ? unexaggeratedTerrainElevation(mapRef.current, point) : null}
            isDrawing={() => Boolean(measureModeRef.current)} onDraw={() => toggleMeasure("distance")}
            readTransect={() => measurementGeometryModeRef.current === "distance" && !measureModeRef.current ? measureCoordinatesRef.current.map(p => [...p] as [number, number]) : []}
            onContext={setSubsurfaceContext} onAsk={() => openQwenCompanion()}
            onInspect={inspection => { returnFocusRef.current = document.activeElement instanceof HTMLElement ? document.activeElement : null; setSubsurfaceInspection(inspection); setResearchOpen(false); setRightOpen(true); window.requestAnimationFrame(() => rightPanelRef.current?.querySelector<HTMLElement>("[data-subsurface-inspector]")?.focus()); }}
            onClose={() => { setUndergroundOpen(false); window.requestAnimationFrame(() => mapContainerRef.current?.focus({ preventScroll: true })); }} onSave={saveCurrentWorkspace}
            onReport={() => openPrimaryWorkspace("reports", true, null, null, subsurfaceContext)} />}
          <div className="screenreader-status sr-only" aria-live="polite">{runtime.message}. Map center {formatCoordinate(view.center[1], "N", "S")}, {formatCoordinate(view.center[0], "E", "W")}. {selectedMapLayerCount} map layers selected. Check Map layers for visibility and source status. {selected ? `Selected ${selected.properties.title}; evidence state ${selectedEvidence?.label}.` : "No feature selected."}</div>
        </section>

        {/* Share the shell stacking context with evidence, preserving map hit testing. */}


          {qwenOpen && isCompact && <div className="qwen-modal-backdrop" aria-hidden="true" onPointerDown={() => closeQwenCompanion()} />}
          <section hidden={!qwenOpen} inert={!qwenOpen} aria-hidden={!qwenOpen} ref={qwenPanelRef} id="qwen-map-panel" className="qwen-panel atlas-chat-dock" data-reading={chatReadingView} role="dialog" aria-modal={isCompact} aria-labelledby="qwen-panel-title">
            <InspectionPanelSwitch active="qwen" onEvidence={openEvidencePanel} onQwen={() => {}} onClose={() => closeQwenCompanion()} reading={chatReadingView} onReading={() => setChatReadingView(value => !value)} />
            <header className="qwen-panel-heading">
              <div><span className="qwen-eyebrow">YOUR INVESTIGATION</span><h2 id="qwen-panel-title">Chat with KFM</h2></div>
            </header>
            <AssistantWorkspace initialMode="explore" active={qwenOpen} focus={assistantFocus} place={selected ? String(selected.properties.title ?? "") : ""} inputRef={globalSearchInputRef} draftRequest={assistantDraftRequest}
              discovery={{query:globalQuery, items:searchResults, status:searchStatus.message, busy:searchStatus.busy, onQuery:setGlobalQuery, onChoose:id => { const item=searchResults.find(row => row.id===id); if (item) chooseSearchResult(item); }}}
              onInspectSources={inspectAssistantSources} />
          </section>

        <aside ref={rightPanelRef} className="evidence-drawer atlas-evidence-tray" data-open={rightOpen} data-state={selected?.properties.evidenceState ?? "EMPTY"} aria-label="Evidence Drawer" aria-hidden={!rightOpen} inert={!rightOpen} aria-modal={isCompact && rightOpen && !surfaceInspectionOpen || undefined} role={isCompact && rightOpen ? "dialog" : undefined}>
          <InspectionPanelSwitch active="evidence" onEvidence={() => {}} onQwen={() => openQwenCompanion()} onClose={closeRightPanel} />
          <div className="panel-heading drawer-heading">
            <div><p className="panel-kicker">EVIDENCE DRAWER</p><h2>{subsurfaceInspection ? subsurfaceInspection.record.name : researchOpen && researchAnchor ? `Near ${researchAnchor.title}` : selected?.properties.title ?? (hoverSummary ? "Map hover preview" : "Select a map feature")}</h2></div>
          </div>
          {subsurfaceInspection ? <SubsurfaceInspector inspection={subsurfaceInspection} onAsk={() => openQwenCompanion()}
            onCenter={() => mapRef.current?.easeTo({ center: subsurfaceInspection.record.coordinates, zoom: 13, duration: motionDuration(400) })}
            onSave={saveCurrentWorkspace} onReport={() => openPrimaryWorkspace("reports", true, null, null, subsurfaceContext)} /> : researchOpen && researchContext ? <div className="drawer-scroll">
            {selected && <button className="map-catalog-launch" type="button" onClick={() => { setResearchOpen(false); window.requestAnimationFrame(() => rightPanelRef.current?.querySelector<HTMLElement>("[data-selection-summary]")?.focus()); }}>Back to selected record</button>}
            <ResearchPanel key={researchIdentity(researchContext.anchor)} context={researchContext} counties={researchCountyOptions} onCounty={setResearchCounty} anchorAvailable={researchAnchorAvailable} onRadius={setNearbyRadiusMiles}
              onInspect={inspectResearchRecord} onCenter={centerResearchRecord} onSave={saveCurrentWorkspace}
              onReport={() => openPrimaryWorkspace("reports", true, null, researchContext)} redacted={researchLocationRedacted || locationCameraRedacted || locationDerivedViewRef.current} />
          </div> : <>
          {hoverSummary && !selected && <section className="drawer-hover-preview" aria-label="Map hover preview">
            <header><span>{hoverActive ? "MAP HOVER" : "LAST MAP HOVER"} · PREVIEW ONLY</span></header>
            <strong>{hoverSummary.title}</strong><span>{hoverSummary.subtitle}</span><p>{hoverSummary.state}</p>
            <small>Select the feature on the map for source details and evidence context.</small>
          </section>}
          {!selected ? !hoverSummary && <div className="drawer-empty"><span aria-hidden="true">⌖</span><h3>No feature selected</h3><p>Choose a map feature or use a Layer Catalog “Features” action. The map identifies a candidate; the registry supplies the stable context.</p></div> : <>
            <div className="drawer-scroll">
            <section className={researchStyles.summary} aria-label="Selection summary">
              {selectedSummary && selectedSummary.topics.length > 0 && (() => {
                const primary = selectedSummary.topics[0], look = categoryMap(primary);
                const lookOn = look && look.basemap === basemap && officialWorkspace === primary;
                return <div className="drawer-category" style={look ? { "--m0": look.swatch[0], "--m1": look.swatch[1], "--m2": look.swatch[2] } as React.CSSProperties : undefined}>
                  <span className="drawer-category-swatch" aria-hidden="true" />
                  <div><small>Category</small><strong>{selectedSummary.topics.slice(0, 3).map(topic => topicDefinition(topic)?.title ?? topic).join(" · ")}</strong></div>
                  {look && !lookOn && <button type="button" onClick={() => openCategoryMap(primary)}>Open the {look.name.toLowerCase()}</button>}
                </div>;
              })()}
              <h3 data-selection-summary tabIndex={-1}>Selected record</h3>
              {selectedSummary && <dl className="drawer-facts">
                <div><dt>What it is</dt><dd>{selectedSummary.what}</dd></div>
                <div><dt>Where &amp; when</dt><dd>{selectedSummary.where}<br />{selectedSummary.when}</dd></div>
                <div><dt>Source &amp; limits</dt><dd><strong>{selectedSummary.source}</strong> · {selectedSummary.status}<p>{selectedSummary.limits}</p></dd></div>
              </dl>}
              <div className={researchStyles.actions}>
                <button type="button" onClick={() => openQwenCompanion()}>Ask AI about this record</button>
                <button type="button" onClick={() => { activateDrawerView("evidence"); window.requestAnimationFrame(() => document.getElementById("drawer-tab-evidence")?.focus()); }}>Inspect</button>
                {selectedResearchRecord && <button type="button" onClick={() => centerResearchRecord(selectedResearchRecord)}>Center</button>}
                {researchSourceUrl(selectedOfficialConnection?.source.sourceUrl ?? selected.properties.citation) && <a href={researchSourceUrl(selectedOfficialConnection?.source.sourceUrl ?? selected.properties.citation)!} target="_blank" rel="noreferrer">Open source ↗</a>}
                <button type="button" disabled={!selectedResearchRecord && !researchAnchor} onClick={event => openResearchDossier(false, event.currentTarget)}>Near here</button>
                {researchAnchor && selectedResearchRecord && researchIdentity(researchAnchor) !== researchIdentity(selectedResearchRecord) && <button type="button" onClick={event => openResearchDossier(true, event.currentTarget)}>Start new dossier here</button>}
                <button type="button" onClick={saveCurrentWorkspace}>Save investigation</button>
                <button type="button" onClick={(event) => openSelectedReport(event.currentTarget)}>Create report</button>
              </div>
              {!selectedResearchRecord && !researchAnchor && <p>Near here requires an eligible registry record or loaded provider point. Raster pixels and polygon centroids are not used.</p>}
            </section>

            {selectedOfficialConnection && <section className="drawer-live-source" data-state={selectedRiverObservation?.status ?? selectedOfficialConnection.state} aria-label="Selected external source and telemetry">
              <header><span>SOURCE CONTEXT · {selectedOfficialConnection.source.shortTitle}</span><strong>{selectedRiverObservation?.status === "observation" ? "OBSERVATION LOADED" : selectedRiverObservation?.status === "gap" ? "NO SAMPLE AT FRAME" : selectedRiverObservation?.status === "stale" ? "LAST RESPONSE · CHECK SOURCE" : selectedRiverObservation?.status === "error" ? "SOURCE UNAVAILABLE" : selectedRiverObservation?.status === "loading" ? "REFRESHING" : selectedOfficialConnection.state.toUpperCase()}</strong></header>
              {selectedRiverObservation ? <>
                <div className="drawer-live-reading"><span>Discharge · USGS station {selectedRiverObservation.stationId.slice(5)}</span><strong>{selectedRiverObservation.displayValue ?? "No sample at this frame"}</strong><small>{selectedRiverObservation.observedAt ? `Observed ${drawerTimestamp(selectedRiverObservation.observedAt)}` : "The selected frame has no usable discharge observation."}</small></div>
                {!selectedRiverObservation.displayValue && latestLoadedDischarge && <p className="drawer-prior-reading">Latest loaded discharge: {latestLoadedDischarge.value?.toLocaleString("en-US")} {latestLoadedDischarge.unit} · {drawerTimestamp(latestLoadedDischarge.observedAt)}. This is not the selected frame.</p>}
                <p>Frame {drawerTimestamp(selectedRiverObservation.frameTime)} · Retrieved {drawerTimestamp(selectedRiverObservation.retrievedAt)}</p>
                <a href={selectedRiverObservation.sourceUrl} target="_blank" rel="noreferrer">Open this gauge at USGS ↗</a>
              </> : <>
                <p>{selectedOfficialConnection.source.organization} · {selectedOfficialConnection.featureCount ?? "Unknown"} features in response · Retrieved {drawerTimestamp(selectedOfficialConnection.retrievedAt)}</p>
                <a href={selectedOfficialConnection.source.sourceUrl} target="_blank" rel="noreferrer">Open source ↗</a>
              </>}
            </section>}
            {selected.kind === "basemap" ? <div className="drawer-claim-boundary"><span>CLAIM EVIDENCE</span><strong>No KFM EvidenceBundle attached</strong><p>{selectedOfficialConnection ? "Provider data is source context. KFM admission, review, and release have not occurred." : "This basemap feature is orientation context from an external display provider, not KFM evidence."}</p></div> : <><div className="drawer-state"><span className="state-icon" aria-hidden="true">{["ANSWER", "CORRECTED"].includes(selected.properties.evidenceState) ? "✓" : ["DENIED_BY_POLICY", "RESTRICTED_ACCESS", "ERROR"].includes(selected.properties.evidenceState) ? "!" : "○"}</span><span><small>{selected.properties.evidenceState}</small><strong>{selectedEvidence?.label}</strong></span></div><p className="state-explanation">{selectedEvidence?.explanation}</p></>}
            {selectedTimeMismatch && <div className="drawer-time-warning" role="status"><strong>Selection is outside active time</strong><span>{selectedOfficialContextId === CIVIC_ID ? `Selected congressional record: ${selected.civicRecord?.sourceDay ?? "date unknown"} · active day: ${civicFrameDay ?? "unsupported"}. Only records compatible with the active congressional view can be used` : selectedIsHeldOfficialContext ? `Current official context is held outside ${formatTimelineStep(OFFICIAL_CONTEXT_PRESENT_FRAME)}` : `Source ${formatTimelineStep(selected.properties.year)} · active ${temporalScopeLabel}`}. The normal map halo is hidden while the record stays available for inspection.</span></div>}
            {selectedOfficialContextId === "nasa-gibs-fire-points" && !selectedAttributesCurrent && <div className="drawer-time-warning" role="status"><strong>Detection is not on the active map</strong><span>This captured NASA detection is from {selectedFireSourceDay ?? "an earlier source day"} UTC. The map is checking {officialArchiveDays["nasa-gibs-fire-points"] ?? currentUtcDay()} UTC; this record remains available only for review.</span></div>}
            {selectedLayerHidden && <div className="drawer-time-warning" role="status"><strong>Selected layer is hidden</strong><span>{selected.layer.title} remains available for inspection, but its normal map halo is hidden until the layer is visible again.</span></div>}
            {selectedEvidenceFiltered && <div className="drawer-time-warning" role="status"><strong>Selection is outside the map evidence filter</strong><span>The record remains available for inspection, but its map geometry and halo stay hidden until the {mapEvidenceFilter.replaceAll("_", " ")} filter is cleared or changed.</span></div>}
            <div className="drawer-tabs" role="tablist" aria-label="Evidence Drawer views">
              {drawerViews.map((tab, index) => <button key={tab} ref={(node) => { drawerTabRefs.current[index] = node; }} id={`drawer-tab-${tab}`} type="button" role="tab" aria-selected={drawerView === tab} aria-controls={`drawer-panel-${tab}`} tabIndex={drawerView === tab ? 0 : -1} onClick={() => activateDrawerView(tab)} onKeyDown={(event) => handleDrawerTabKeyDown(event, index)}>{drawerViewLabels[tab]}</button>)}
            </div>
            <div>
              {drawerView === "evidence" && <section role="tabpanel" id="drawer-panel-evidence" aria-labelledby="drawer-tab-evidence" className="drawer-section">
                <p className="summary">{selectedRiverObservation ? `${selectedRiverObservation.stationName ?? selected.properties.title} is a USGS monitoring location. The observation follows the selected map frame; a missing frame remains a gap.` : selectedOfficialConnection ? `Selected map snapshot: ${selected.properties.summary} Re-select this feature after a feed update to refresh its mapped properties.` : selected.properties.summary}</p>
                {!selectedRiverObservation && <section className="drawer-data-block" aria-label="Selected artifact data"><header><h3>Selected artifact data</h3><small>{selected.kind === "registry" ? "Site-local record" : selectedAttributesCurrent ? "Current loaded provider response" : "Captured map properties"}</small></header>
                  {selectedOfficialContextId === "kgs-monitoring-wells" && safeKgsWellUrl(selectedArtifactAttributes.find(item => item.label === "KGS well record")?.value) && <a href={safeKgsWellUrl(selectedArtifactAttributes.find(item => item.label === "KGS well record")?.value)!} target="_blank" rel="noreferrer">Open this well’s KGS observations ↗</a>}
                  {selectedArtifactAttributes.length > 0 ? <dl className="drawer-attribute-list">{selectedArtifactAttributes.map((attribute) => <div key={attribute.label}><dt>{attribute.label}</dt><dd>{attribute.value}</dd></div>)}</dl> : <p>No measured feature attributes are available in this map carrier. Source and trust metadata are available below.</p>}
                </section>}
                {selectedFireComparisonId && <section className="drawer-data-block" aria-label="Fire report builder context"><header><h3>Fire report builder</h3><small>Source report and satellite signal kept separate</small></header>
                  <p><strong>{selectedOfficialContextId === "nifc-fire-reports" ? "NIFC incident record reported" : "NASA thermal signal observed"}.</strong> {selectedOfficialContextId === "nifc-fire-reports" ? "The incident identity and attributes come from the interagency working record; live activity is not independently established." : "A thermal anomaly is not by itself a wildfire incident report."}</p>
                  <p>{selectedFireComparisonPayload?.state === "ready" || selectedFireComparisonPayload?.state === "empty" || selectedFireComparisonPayload?.state === "partial"
                    ? selectedFireNeighbors.length ? `${selectedFireNeighbors.length} nearby ${selectedFireComparisonId === "nifc-fire-reports" ? "NIFC report" : "NASA detection"}${selectedFireNeighbors.length === 1 ? "" : "s"} within 10 km in the loaded ${selectedFireComparisonId === "nifc-fire-reports" ? "30-day report window" : "UTC image day"}. Proximity does not establish that these records describe the same event.` : `No ${selectedFireComparisonId === "nifc-fire-reports" ? "NIFC report" : "NASA detection"} within 10 km in the loaded response. This is not evidence of absence.`
                    : `Comparison source ${selectedFireComparisonId === "nifc-fire-reports" ? "NIFC reports" : "NASA detections"} is not loaded; no corroboration check is available.`}</p>
                  {selectedFireNeighbors.length > 0 && <ol className="drawer-sample-list">{selectedFireNeighbors.map((neighbor) => <li key={`${neighbor.name}-${neighbor.distanceKm}`}><strong>{neighbor.name}</strong><small>{neighbor.distanceKm.toFixed(1)} km from reported point · {neighbor.eventTime ? drawerTimestamp(neighbor.eventTime) : "time not supplied"}</small></li>)}</ol>}
                  {selectedFireComparisonPayload?.state === "partial" && <p>Comparison feed is partial; additional nearby records may be missing.</p>}
                  <a href="https://data-nifc.opendata.arcgis.com/pages/d6ef1367fadc4405b5f09c98e52ed972" target="_blank" rel="noreferrer">How NIFC distinguishes working and certified fire data ↗</a>
                  <p>Official incident updates and national fire news can add context, but no article is automatically matched to this record.</p>
                  <div className="source-time-actions"><a href="https://inciweb.wildfire.gov/" target="_blank" rel="noreferrer">Browse InciWeb ↗</a><a href="https://www.nifc.gov/fire-information" target="_blank" rel="noreferrer">NIFC fire news ↗</a></div>
                  <button type="button" onClick={() => openPrimaryWorkspace("reports", true, buildFireReportContext(selectedOfficialContextId === "nifc-fire-reports" ? "nifc-fire-reports" : "nasa-gibs-fire-points", selectedOfficialFeature || null, selectedOfficialPayload?.retrievedAt, selectedOfficialPayload?.state ?? "unavailable", selectedFireComparisonPayload?.state ?? "unavailable", selectedFireNeighbors))}>Build report from selected fire record</button>
                </section>}
                {selectedRiverObservation && <section className="drawer-data-block" aria-label="USGS gauge height data"><header><h3>Gauge height · USGS 00065</h3><small>Separate seven-day station request</small></header>
                  {selectedStageDetail?.status === "loading" && <p role="status">Loading station metadata and gauge-height observations…</p>}
                  {selectedStageDetail?.status === "error" && <p role="status">Gauge-height data are unavailable. The discharge frame and its history remain separate.</p>}
                  {selectedStageDetail?.status === "ready" && selectedStageDetail.detail && <>
                    <p>{selectedStageDetail.detail.latest ? `Latest returned value: ${selectedStageDetail.detail.latest.value?.toLocaleString("en-US")} ${selectedStageDetail.detail.latest.unit} · ${drawerTimestamp(selectedStageDetail.detail.latest.observedAt)}` : "No measured gauge-height value was returned in this seven-day request."} {selectedStageDetail.detail.partial ? "The response is partial." : ""}</p>
                    <p>Checked {drawerTimestamp(selectedStageDetail.detail.queryStart)} to {drawerTimestamp(selectedStageDetail.detail.queryEnd)} · {selectedStageDetail.detail.observationCount.toLocaleString("en-US")} returned samples · retrieved {drawerTimestamp(selectedStageDetail.detail.retrievedAt)}.</p>
                    {selectedStageDetail.detail.recent.length > 0 && <ol className="drawer-sample-list" aria-label="Recent gauge-height samples">{selectedStageDetail.detail.recent.map((item) => <li key={item.observedAt}><time dateTime={item.observedAt}>{drawerTimestamp(item.observedAt)}</time><strong>{item.value === null ? "No value" : `${item.value.toLocaleString("en-US")} ${item.unit}`}</strong><small>{item.approvalStatus ?? "Status unavailable"}{item.qualifiers.length ? ` · ${item.qualifiers.join(", ")}` : ""}</small></li>)}</ol>}
                  </>}
                  <a href={`https://waterdata.usgs.gov/monitoring-location/${selectedRiverObservation.stationId}/#dataTypeId=continuous-00065-0&period=P7D&showFieldMeasurements=true`} target="_blank" rel="noreferrer">Open gauge-height data at USGS ↗</a>
                </section>}
                {selectedRiverObservation && <><h3>Gauge and feed telemetry</h3><dl className="evidence-facts">
                  <div><dt>Feed state</dt><dd>{selectedRiverObservation.connectionState.toUpperCase()}{selectedRiverObservation.isPartial ? " · partial response" : ""}</dd></div>
                  <div><dt>Selected frame</dt><dd>{drawerTimestamp(selectedRiverObservation.frameTime)}</dd></div>
                  <div><dt>Observed</dt><dd>{drawerTimestamp(selectedRiverObservation.observedAt)}</dd></div>
                  <div><dt>Retrieved</dt><dd>{drawerTimestamp(selectedRiverObservation.retrievedAt)}</dd></div>
                  <div><dt>Station samples</dt><dd>{selectedRiverObservation.observationCount.toLocaleString("en-US")} in loaded response</dd></div>
                  <div><dt>USGS status</dt><dd>{selectedRiverObservation.approvalStatus ?? "Not available"}</dd></div>
                  <div><dt>Qualifiers</dt><dd>{selectedRiverObservation.qualifiers.length > 0 ? selectedRiverObservation.qualifiers.join(", ") : "None reported"}</dd></div>
                  <div><dt>Trend at frame</dt><dd>{selectedRiverObservation.trend && selectedRiverObservation.trend !== "unknown" ? selectedRiverObservation.trend : "Not available"}</dd></div>
                </dl></>}
                {selectedRiverObservation && <section className="drawer-data-block" aria-label="Loaded discharge data"><header><h3>Loaded discharge · USGS 00060</h3><small>{streamflowBundle?.query.mode === "historical-series" ? "Selected historical range" : "Bounded network window"}</small></header>
                  {selectedDischargeHistory.length > 0 ? <ol className="drawer-sample-list">{selectedDischargeHistory.map((item) => <li key={item.observedAt}><time dateTime={item.observedAt}>{drawerTimestamp(item.observedAt)}</time><strong>{item.value === null ? "No value" : `${item.value.toLocaleString("en-US")} ${item.unit}`}</strong><small>{item.approvalStatus ?? "Status unavailable"}{item.qualifiers.length ? ` · ${item.qualifiers.join(", ")}` : ""}</small></li>)}</ol> : <p>No discharge samples were returned for this station in the loaded request.</p>}
                  <p>The selected frame above is independent of this recent-sample list. No value is carried into a missing frame.</p>
                </section>}
                <details className="drawer-context-details"><summary>Context, provenance and claim fields</summary>
                <dl className="evidence-facts">
                  <div><dt>Layer / domain</dt><dd>{selected.layer.title} · {selected.layer.domain}</dd></div>
                  <div><dt>Source role</dt><dd>{selected.properties.sourceRole}</dd></div>
                  <div><dt>Source organization</dt><dd>{selected.properties.sourceOrganization}</dd></div>
                  <div><dt>Spatial scope</dt><dd>{selected.properties.spatialScope}</dd></div>
                  <div><dt>Temporal scope</dt><dd>{selectedRiverObservation ? drawerTimestamp(selectedRiverObservation.frameTime) : selected.properties.temporalScope}</dd></div>
                  <div><dt>Last update / freshness</dt><dd>{selectedOfficialConnection ? `${drawerTimestamp(selectedOfficialConnection.retrievedAt)} · ${selectedOfficialConnection.state.toUpperCase()}` : `${selected.properties.lastUpdate} · ${selected.properties.freshnessState}`}</dd></div>
                  <div><dt>Review / release</dt><dd>{selectedOfficialConnection ? "Not KFM reviewed · not KFM released" : `${selected.properties.reviewState} · ${selected.properties.releaseState}`}</dd></div>
                  <div><dt>Evidence reference</dt><dd><code>{selected.properties.citation}</code></dd></div>
                  <div><dt>Official source</dt><dd>{selectedOfficialConnection ? <a href={selectedRiverObservation?.sourceUrl ?? selectedOfficialConnection.source.sourceUrl} target="_blank" rel="noreferrer">{selectedOfficialConnection.source.organization} record ↗</a> : selectedSourceCandidate ? <a href={selectedSourceCandidate.sourceUrl} target="_blank" rel="noreferrer">{selectedSourceCandidate.organization} portal ↗</a> : "Not available for this site-local record"}</dd></div>
                  <div><dt>Source admission</dt><dd>{selectedOfficialConnection ? "External context · not KFM admitted" : selectedSourceCandidate ? `${(SOURCE_ADMISSION_BY_ID[selectedSourceCandidate.id] ?? "candidate").replaceAll("-", " ")} · checked ${selectedSourceCandidate.checkedAt}` : selected.kind === "basemap" ? "External display context" : "External context fixture"}</dd></div>
                </dl>
                </details>
                <div className="notice"><strong>Limitations</strong><p>{selectedRiverObservation?.status === "stale" ? "The source is stale or unavailable. A prior sample is shown only with its original time; no new observation is inferred. " : ""}{selectedOfficialPayload?.limitation ?? selected.properties.uncertainty}</p></div>
                <div className="notice"><strong>Generalization / rights</strong><p>{selected.properties.generalizationNote} {selected.properties.rights}</p></div>
                {selected.properties.correctionState !== "NONE" && <div className="notice correction"><strong>Correction state</strong><p>{selected.properties.correctionState}</p></div>}
                <div className="drawer-actions"><button type="button" onClick={() => activateDrawerView("focus", true)}>Open Focus Mode</button><button type="button" onClick={(event) => openSelectedReport(event.currentTarget)}>Add to report</button><button type="button" onClick={() => openPrimaryWorkspace("stories", true)}>Add to story</button><button type="button" onClick={(event) => openMapUtility("export", event.currentTarget)}>Review public-safe export</button></div>
              </section>}
              {drawerView === "metadata" && <section role="tabpanel" id="drawer-panel-metadata" aria-labelledby="drawer-tab-metadata" className="drawer-section">
                {selectedOfficialConnection ? <><h3>Official source details</h3><dl className="evidence-facts">
                  <div><dt>Provider</dt><dd>{selectedOfficialConnection.source.organization}</dd></div><div><dt>Feed</dt><dd>{selectedOfficialConnection.source.endpointLabel}</dd></div><div><dt>Cadence</dt><dd>{selectedOfficialConnection.source.cadence}</dd></div><div><dt>Response state</dt><dd>{selectedOfficialConnection.state.toUpperCase()}{selectedOfficialPayload?.truncated ? " · truncated" : ""}</dd></div>{selectedOfficialPayload?.sourceDay && <div><dt>NASA image day</dt><dd>{selectedOfficialPayload.sourceDay} UTC</dd></div>}<div><dt>Retrieved</dt><dd>{drawerTimestamp(selectedOfficialConnection.retrievedAt)}</dd></div><div><dt>Provider time</dt><dd>{drawerTimestamp(selectedOfficialPayload?.upstreamUpdatedAt)}</dd></div><div><dt>Evidence role</dt><dd>External context only</dd></div><div><dt>Attribution</dt><dd>{selectedOfficialConnection.source.attribution}</dd></div>
                </dl>{selectedRiverObservation && streamflowCoverage?.station === selectedRiverObservation.stationId && <div className="notice"><strong>Provider-declared discharge record span</strong><p>{streamflowCoverage.continuous ? `${drawerTimestamp(streamflowCoverage.continuous.start)} to ${drawerTimestamp(streamflowCoverage.continuous.end)} continuous` : "No continuous span declared"}{streamflowCoverage.daily ? ` · daily ${drawerTimestamp(streamflowCoverage.daily.start)} to ${drawerTimestamp(streamflowCoverage.daily.end)}` : ""}{streamflowCoverage.partial ? " · partial metadata" : ""}. Gaps may occur within these dates.</p></div>}{selectedRiverObservation && selectedStageDetail?.status === "ready" && selectedStageDetail.detail && <><h3>USGS monitoring location</h3><dl className="evidence-facts">
                  <div><dt>Station</dt><dd>{selectedStageDetail.detail.name} · {selectedStageDetail.detail.stationId}</dd></div>
                  <div><dt>Site type</dt><dd>{selectedStageDetail.detail.siteTypeCode ?? "Not reported"}</dd></div>
                  <div><dt>County</dt><dd>{selectedStageDetail.detail.county ?? "Not reported"}</dd></div>
                  <div><dt>Hydrologic unit</dt><dd>{selectedStageDetail.detail.huc ?? "Not reported"}</dd></div>
                  <div><dt>Drainage area</dt><dd>{selectedStageDetail.detail.drainageArea === null ? "Not reported" : `${selectedStageDetail.detail.drainageArea.toLocaleString("en-US")} sq mi`}</dd></div>
                  <div><dt>Contributing area</dt><dd>{selectedStageDetail.detail.contributingDrainageArea === null ? "Not reported" : `${selectedStageDetail.detail.contributingDrainageArea.toLocaleString("en-US")} sq mi`}</dd></div>
                  <div><dt>WGS84 point</dt><dd>{selectedStageDetail.detail.latitude.toFixed(5)}, {selectedStageDetail.detail.longitude.toFixed(5)} · provider coordinates, not survey precision</dd></div>
                  <div><dt>Stage response</dt><dd>{selectedStageDetail.detail.partial ? "Partial" : "Complete within request"}{selectedStageDetail.detail.truncated ? " · truncated" : ""}</dd></div>
                </dl></>}
                <div className="notice"><strong>Source boundary</strong><p>{selectedOfficialConnection.source.boundary}</p></div></> : selected.kind === "basemap" ? <><h3>External display metadata</h3><dl className="evidence-facts"><div><dt>Provider</dt><dd>{selected.properties.sourceOrganization}</dd></div><div><dt>Rendered layer</dt><dd>{selected.layer.title}</dd></div><div><dt>Feature ID</dt><dd>{selected.featureId}</dd></div><div><dt>Role</dt><dd>Orientation context only · no KFM source admission</dd></div></dl></> : <><h3>Registry-driven layer metadata</h3><dl className="evidence-facts">
                  <div><dt>Dataset</dt><dd>{selected.layer.datasetName}</dd></div><div><dt>Source / geometry</dt><dd>{selected.layer.sourceType} · {selected.layer.geometryType}</dd></div><div><dt>Zoom support</dt><dd>{selected.layer.minZoom}–{selected.layer.maxZoom}</dd></div><div><dt>Units</dt><dd>{selected.layer.units}</dd></div><div><dt>Valid time extent</dt><dd>{selected.layer.validTimeExtent}</dd></div><div><dt>Source time</dt><dd>{selected.layer.sourceTime}</dd></div><div><dt>Release time</dt><dd>{selected.layer.releaseTime}</dd></div><div><dt>Attribution</dt><dd>{selected.layer.attribution}</dd></div></dl><div className="legend-detail"><strong>Legend</strong>{selected.layer.legend.map((item) => <p key={item.label}><i className={`legend-swatch ${item.shape}`} style={{ "--swatch": item.color } as React.CSSProperties} />{item.label}</p>)}</div></>}
              </section>}
              {drawerView === "lineage" && <section role="tabpanel" id="drawer-panel-lineage" aria-labelledby="drawer-tab-lineage" className="drawer-section">
                {selectedOfficialConnection ? <><h3>Source-to-drawer trace</h3><ol className="lineage-list"><li><span>01</span><div><strong>{selectedOfficialConnection.source.organization}</strong><small>{selectedOfficialConnection.source.endpointLabel}</small></div></li><li><span>02</span><div><strong>Bounded Site connection</strong><small>{selectedOfficialConnection.source.managedAdapterPath ?? selectedOfficialConnection.source.apiPath ?? "Provider display layer"} · {selectedOfficialConnection.state.toUpperCase()}</small></div></li><li><span>03</span><div><strong>Retrieved response</strong><small>{drawerTimestamp(selectedOfficialConnection.retrievedAt)} · {selectedOfficialConnection.featureCount ?? "unknown"} displayed features</small></div></li><li><span>04</span><div><strong>Map selection</strong><small>{selected.featureId}</small></div></li><li><span>05</span><div><strong>KFM claim boundary</strong><small>No EvidenceBundle, source admission, review, or release established by this selection.</small></div></li></ol></> : <><h3>Selection-to-evidence trace</h3><ol className="lineage-list"><li><span>01</span><div><strong>MapLibre candidate</strong><small>queryRenderedFeatures identified a candidate only</small></div></li><li><span>02</span><div><strong>{selected.kind === "basemap" ? "External display context" : "Stable registry context"}</strong><small>{selected.featureId}</small></div></li><li><span>03</span><div><strong>{selected.kind === "basemap" ? "No KFM evidence resolution" : "Evidence resolution"}</strong><small>{selected.properties.citation}</small></div></li><li><span>04</span><div><strong>Policy / rights</strong><small>{selected.properties.evidenceState}</small></div></li><li><span>05</span><div><strong>Public-safe view</strong><small>{selected.kind === "basemap" ? "Context only · no claim support" : "Drawer + bounded Focus Mode"}</small></div></li></ol></>}
                <div className="boundary-law"><span>Renderer</span><b>≠</b><span>truth store</span><b>·</b><span>pixel</span><b>≠</b><span>proof</span></div>
              </section>}
              {drawerView === "focus" && <section role="tabpanel" id="drawer-panel-focus" aria-labelledby="drawer-tab-focus" className="drawer-section focus-mode">
                <div className="focus-heading"><span>FOCUS WORKBENCH · SITE-LOCAL DEMONSTRATION</span><strong>Deterministic · no live AI · no model endpoint</strong></div>
                <p>Focus Mode can inspect available map context, but no KFM domain records are admitted in this Site.</p>
                <nav className="focus-stage-nav" aria-label="Focus Workbench stages">
                  {(["outcome", "checks", "actions"] as FocusStage[]).map((stage) => <button key={stage} type="button" aria-pressed={focusStage === stage} onClick={() => { setFocusStage(stage); setPendingFocusAction(null); }}><span>{stage === "outcome" ? "01" : stage === "checks" ? "02" : "03"}</span>{stage === "checks" ? "Closure" : stage}</button>)}
                </nav>

                {focusStage === "outcome" && <div className="focus-stage">
                  <div className="focus-intents" aria-label="Safe Focus intents">
                    {FOCUS_INTENTS.map((intent) => <button key={intent.id} type="button" aria-pressed={focusIntent === intent.id} title={intent.label} onClick={() => setFocusIntent(intent.id)}>{intent.shortLabel}</button>)}
                  </div>
                  <div className="focus-context" aria-label="Focus context rail">
                    <span>Feature <code>{selected.featureId}</code></span>
                    <span>Layer <code>{selected.layerId}</code></span>
                    <span>Active / source time <code>{temporalScopeLabel} / {formatTimelineStep(selected.properties.year)}</code></span>
                    <span>Camera <code>z{view.zoom.toFixed(1)} · {projection}</code></span>
                    <span>Visible layers <code>{visibleCount} · bounded IDs</code></span>
                    <span>Release / review <code>{selected.properties.releaseState} · {selected.properties.reviewState}</code></span>
                  </div>
                  <div className="focus-context-law"><strong>MapContextEnvelope preview</strong><span>Strict local request: profile · request ID · claim ID · question · allowed EvidenceRefs</span><span>Context is not evidence or authority · no protected geometry included</span></div>
                  <div className="focus-resolution" aria-label={`Evidence state ${selected.properties.evidenceState} resolves to ${activeFocus.outcome}`}><span>Evidence state</span><strong>{selected.properties.evidenceState}</strong><b aria-hidden="true">→</b><span>Finite outcome</span><strong>{activeFocus.outcome}</strong></div>
                  <article className="focus-result" data-outcome={activeFocus.outcome} data-input-state={selected.properties.evidenceState} aria-live="polite"><div><span>{activeFocus.outcome}</span><code>{activeFocus.code}</code></div><h3>{activeFocus.title}</h3><p>{activeFocus.body}</p>{activeFocus.outcome === "ANSWER" && <small>Support: {selected.properties.citation}</small>}{activeFocus.outcome === "ABSTAIN" && <small>No unsupported answer generated.</small>}{activeFocus.outcome === "DENY" && <small>No protected attributes or exact geometry disclosed.</small>}{activeFocus.outcome === "ERROR" && <small>No fallback answer or provider output exposed.</small>}</article>
                  <div className="focus-intent-answer"><span>{FOCUS_INTENTS.find((intent) => intent.id === focusIntent)?.label}</span><p>{focusNarrative}</p></div>
                  <div className="focus-primary-actions"><button type="button" onClick={() => void copyFocusReceipt()}>Copy context receipt</button><button type="button" onClick={() => setFocusStage("checks")}>View closure checks</button></div>
                </div>}

                {focusStage === "checks" && <div className="focus-stage">
                  <div className="focus-section-heading"><span>DIAGNOSTIC ASSESSMENT</span><strong>Six visible closure checks</strong><p>These checks explain the local result. PASS is not publication, policy approval, or production readiness.</p></div>
                  <ol className="focus-gates">
                    {focusGates.map((gate, index) => <li key={gate.id} data-gate={gate.state}><span>{String(index + 1).padStart(2, "0")}</span><div><strong>{gate.label}</strong><p>{gate.detail}</p></div><b>{gate.state}</b></li>)}
                  </ol>
                  <div className="focus-negative-legend"><strong>Visible evidence states</strong><div>{Object.entries(evidenceLabels).map(([state, metadata]) => <span key={state} data-state={state} title={metadata.explanation}>{state}</span>)}</div></div>
                  <div className="focus-trust-law"><strong>Viewer display preference ≠ subject consent</strong><p>A local show/hide choice cannot grant consent, authority, rights, release, or a policy bypass.</p></div>
                  <button className="focus-copy" type="button" onClick={() => void copyFocusReceipt()}>Copy closure receipt</button>
                </div>}

                {focusStage === "actions" && <div className="focus-stage">
                  <div className="focus-section-heading"><span>MAP ACTION PROPOSALS</span><strong>Preview first · apply explicitly</strong><p>Actions can change only camera, timeline, or review navigation. They never mutate evidence, policy, consent, review, release, or publication state.</p></div>
                  <div className="focus-proposals">
                    {focusProposals.map((proposal) => <article key={proposal.id}><div><span>{proposal.kind.replaceAll("_", " ")}</span><strong>{proposal.title}</strong><p>{proposal.summary}</p></div><button type="button" onClick={() => setPendingFocusAction(proposal)}>Review</button></article>)}
                  </div>
                  {pendingFocusAction && <article className="focus-action-review" role="region" aria-live="polite" aria-labelledby="focus-action-title" aria-describedby="focus-action-description">
                    <span>LOCAL ACTION REVIEW · NO SILENT EXECUTION</span>
                    <h3 id="focus-action-title">{pendingFocusAction.title}</h3>
                    <p id="focus-action-description">{pendingFocusAction.summary}</p>
                    <dl><div><dt>Before</dt><dd>{pendingFocusAction.before}</dd></div><div><dt>After</dt><dd>{pendingFocusAction.after}</dd></div><div><dt>Governance effect</dt><dd>{pendingFocusAction.impact}</dd></div></dl>
                    <div><button type="button" onClick={() => applyFocusAction(pendingFocusAction)}>Apply explicit change</button><button type="button" onClick={() => setPendingFocusAction(null)}>Cancel</button></div>
                  </article>}
                  {!pendingFocusAction && <p className="focus-action-empty">Choose Review to inspect a before/after diff. Nothing runs until Apply is selected.</p>}
                </div>}
                <p className="focus-boundary">Outcomes cannot be manually overridden. Safe intents change the explanation only; action proposals change view state only.</p>
              </section>}
            </div>
            </div>
          </>}
          </>}
        </aside>

        <section ref={timelineRef} className="timeline-panel timeline-calendar" aria-label="Timeline and temporal controls">
          <CompactTimeSweep value={calendarSweep} year={year} years={timelineSteps} today={currentUtcDay()} reducedMotion={reducedMotion}
            open={timelineOpen} onOpenChange={setTimelineOpen} onSeek={seekCalendarFrame}
            onEra={next => { setPlaying(false); commitTemporalFrame(next); }} onPresent={returnCalendarToPresent}
            sources={calendarSourceRows} imageryComparison={<EarthEngineComparisonPanel manifests={earthEngineContext.manifests} loading={earthEngineContext.loading} error={earthEngineContext.error} />}>
          <div className="timeline-compact">
            <button className="timeline-toggle" type="button" aria-expanded={timelineOpen} onClick={() => { if (timelineOpen) { closeTimelinePanel(); return; } setTimelineOpen(true); if (isCompact) { dismissMapUtilityWithoutFocus(); setLeftOpen(false); setRightOpen(false); } }}>
              <span>TIME SWEEP</span>
              <strong>{temporalScopeLabel}</strong>
              <small>{previewYear === year ? `Atlas years · ${temporalMode.replaceAll("-", " ")} · ${timelineEraLabel(year, buildYearCurrent)}` : `Atlas year preview ${formatTimelineStep(previewYear)}`}</small>
            </button>
            <div className="timeline-controls">
              <button type="button" disabled={temporalMode === "comparison" || previousSweepFrame === null} onClick={() => stepTemporalSweep("reverse")} aria-label="Previous sweep frame">‹</button>
              <button type="button" aria-pressed={playing} disabled={reducedMotion || temporalMode === "snapshot" || temporalMode === "comparison" || temporalSequence.length < 2} onClick={toggleTemporalPlayback} aria-label={playing ? "Pause time sweep" : temporalMode === "snapshot" ? "Choose a sweep mode to play" : temporalMode === "comparison" ? "Comparison uses two frames; playback is unavailable" : reducedMotion ? "Playback is off for reduced motion; use frame steps" : temporalSequence.length < 2 ? "No sweep frames available to play" : "Play time sweep"} title={temporalMode === "snapshot" ? "Choose Moving window, Event stepping, or Accumulation to play" : temporalMode === "comparison" ? "Comparison shows two frames" : reducedMotion ? "Use previous and next for reduced motion" : undefined}>{playing ? "Ⅱ" : "▶"}</button>
              <button type="button" disabled={temporalMode === "comparison" || nextSweepFrame === null} onClick={() => stepTemporalSweep("forward")} aria-label="Next sweep frame">›</button>
              <label className="timeline-frame-picker">Year<select value={previewYear} onChange={(event) => { setPreviewYear(Number(event.target.value)); setPlaying(false); }} aria-label="Preview year or earlier era">{timelineSteps.map((step) => <option key={step} value={step}>{formatTimelineStep(step)}</option>)}</select></label>
            </div>
            <div className="timeline-track">
              <input type="range" min="0" max={timelineSteps.length - 1} value={Math.max(0, timelineSteps.indexOf(previewYear))} onChange={(event) => { setPreviewYear(timelineSteps[Number(event.target.value)]); setPlaying(false); }} aria-label="Preview time before committing; every year from 1800 is selectable" aria-valuetext={`Preview ${formatTimelineStep(previewYear)}; committed ${temporalScopeLabel}`} />
              <div className="timeline-ticks" style={{ "--timeline-columns": timelineSteps.length } as React.CSSProperties} aria-hidden="true">{timelineSteps.map((step) => <span key={step} className="timeline-tick" data-active={step === previewYear} data-committed={step === temporalQuery.frame} data-major={TIMELINE_MAJOR_STEPS.has(step)} data-in-range={step >= sweepRangeStart && step <= sweepRangeEnd} title={`${formatTimelineStep(step)} · ${timelineEraLabel(step, buildYearCurrent)}`}>{timelineLabels.has(step) ? <b>{formatTimelineStep(step)}</b> : <i />}</span>)}</div>
            </div>
            <div className="timeline-commit-actions">
              <button type="button" disabled={previewYear === temporalQuery.frame} onClick={() => { setPlaying(false); commitTemporalFrame(previewYear, `Committed ${formatTimelineStep(previewYear)} to the map, evidence, report, and story context`); }}>Commit</button>
              <button className="timeline-reset" type="button" disabled={!buildYearCurrent} onClick={() => { setPlaying(false); commitTemporalFrame(OFFICIAL_CONTEXT_PRESENT_FRAME, "Returned to the operational-present frame"); }}>{buildYearCurrent ? "Present" : "Rebuild for Present"}</button>
            </div>
          </div>
          <div className="timeline-detail">
            <section className="timeline-sweep-setup" aria-labelledby="timeline-sweep-title">
              <header><span>TIME SWEEP</span><strong id="timeline-sweep-title">Explore the map by year</strong><small>Preview a year, then Commit to update the map.</small></header>
              <div className="timeline-semantic-controls">
                <label>Mode<select value={temporalMode} onChange={(event) => { const nextMode = event.target.value as TemporalSweepMode; setPlaying(false); setTemporalMode(nextMode); if (nextMode === "comparison") { commitTemporalFrame(compareTimeB); setMapUtilityView("compare"); setMapUtilityOpen(true); setMapContextOpen(false); } }}><option value="snapshot">Snapshot</option><option value="moving-window">Moving window</option><option value="event-stepping">Event stepping</option><option value="accumulation">Accumulation</option><option value="comparison">A / B comparison</option></select></label>
              </div>
              <p className="timeline-mode-hint">{temporalMode === "snapshot" ? "Snapshot shows one year. Choose a sweep mode to enable Play." : temporalMode === "comparison" ? "Comparison holds two frames. Open the comparison view to inspect them." : reducedMotion ? "Automatic playback is off for reduced motion. Use previous and next to step through frames." : "Play advances through declared frames; gaps and source dates remain visible."}</p>
              <details className="timeline-advanced"><summary>Playback, range & interpretation</summary>
                <div className="timeline-semantic-controls">
                <label>Step<select value={temporalStepRule} onChange={(event) => { setPlaying(false); setTemporalStepRule(event.target.value as TemporalStepRule); }}><option value="regular-calendar">Every year</option><option value="available-events">Event dates + bounds</option></select></label>
              </div>
              <div className="timeline-range-controls" aria-label="Sweep range">
                <label><span>Start</span><select value={sweepRangeStart} onChange={(event) => { const next = Number(event.target.value); setPlaying(false); if (next <= year) setSweepRangeStart(next); }}>{TIME_STEPS.map((step) => <option key={`start:${step}`} value={step} disabled={step > year}>{formatTimelineStep(step)}</option>)}</select></label>
                <span aria-hidden="true">→</span>
                <label><span>End</span><select value={sweepRangeEnd} onChange={(event) => { const next = Number(event.target.value); setPlaying(false); if (next >= year) setSweepRangeEnd(next); }}>{TIME_STEPS.map((step) => <option key={`end:${step}`} value={step} disabled={step < year}>{formatTimelineStep(step)}</option>)}</select></label>
                <strong>{temporalSequence.length} frame{temporalSequence.length === 1 ? "" : "s"}</strong>
              </div>
                <div className="timeline-semantic-controls">
                <label>Frame cadence<select value={playbackSpeed} onChange={(event) => setPlaybackSpeed(Number(event.target.value) as PlaybackSpeed)}><option value={0.5}>Slow · 2.6 s</option><option value={1}>Normal · 1.3 s</option><option value={2}>Fast · 0.65 s</option></select></label>
                <label>Direction<select value={playbackDirection} onChange={(event) => { setPlaying(false); setPlaybackDirection(event.target.value as TemporalPlaybackDirection); }}><option value="forward">Forward</option><option value="reverse">Reverse</option></select></label>
                <label>At boundary<select value={playbackLoopMode} onChange={(event) => setPlaybackLoopMode(event.target.value as TemporalLoopMode)}><option value="stop">Stop</option><option value="loop">Loop</option></select></label>
                <label>Window<select value={movingWindowFrames} disabled={temporalMode !== "moving-window"} onChange={(event) => setMovingWindowFrames(Number(event.target.value))}><option value={2}>2 frames</option><option value={3}>3 frames</option><option value={5}>5 frames</option></select></label>
              </div>
              <p className="timeline-axis-note"><strong>YEAR BY YEAR · 1800 TO {TIME_STEPS.at(-1)}</strong> · Every calendar year is selectable; a year with no compatible records stays empty. Earlier eras are separate capacity markers, not claims of data. Frame spacing and cadence are ordinal, not proportional to elapsed time. The active query uses each layer’s declared feature-year axis; source, retrieval, release, review, and correction clocks remain separate metadata.</p>
              <div className="timeline-motion-controls">
                <label><input type="checkbox" checked={dynamicEffects && !reducedMotion} disabled={reducedMotion} onChange={(event) => setDynamicEffects(event.target.checked)} /> Ambient layer motion</label>
                <small>{reducedMotion ? "System reduced-motion is active: autoplay and ambient movement are off; stepping remains available." : "Local layer motion and live gauge halos are presentation only. HMS smoke stays tied to provider Start/End intervals; visual motion does not encode velocity, intensity, or measured change."}</small>
              </div>
              <div className="timeline-era-jumps" aria-label="Preview named time ranges">{TIMELINE_JUMPS.map((jump) => <button key={jump.label} type="button" data-active={jump.year === previewYear} onClick={() => { setPreviewYear(jump.year); setPlaying(false); }}>{jump.label}<small>{formatTimelineStep(jump.year)}</small></button>)}</div>
              </details>
              <div className="timeline-primary-actions"><Link href="/observatory">Provider history ↗</Link><button type="button" onClick={() => openPrimaryWorkspace("stories", true)}>Capture frame for story</button></div>
            </section>

            <section className="timeline-frame-readout" aria-labelledby="timeline-frame-title">
              <div className="timeline-frame-status" role="status" aria-live="polite" aria-atomic="true"><span>COMMITTED FRAME</span><strong id="timeline-frame-title">{temporalScopeLabel}</strong><small>{playing ? `Playing ${playbackDirection}; pauses when hidden` : "Paused"} · {temporalFramePosition ?? "off-sequence"}/{temporalSequence.length}</small></div>
              <div className="timeline-frame-metrics">
                <article><span>REGISTRY RECORDS</span><strong>{temporalFrameSummary.timedRecordCount}</strong></article>
                <article><span>DOMAINS</span><strong>{temporalFrameSummary.activeDomainCount}</strong></article>
                <article><span>ENTERED</span><strong>{temporalFrameSummary.entered.length}</strong></article>
                <article><span>EXITED</span><strong>{temporalFrameSummary.exited.length}</strong></article>
              </div>
              {(temporalFrameSummary.entered.length > 0 || temporalFrameSummary.exited.length > 0) && <div className="timeline-change-list">
                <div><span>{comparisonTemporalFrame === null ? "NO ADJACENT REFERENCE FRAME" : `ENTERED FROM ${formatTimelineStep(comparisonTemporalFrame)}`}</span>{temporalFrameSummary.entered.slice(0, 3).map((record) => <small key={`in:${record.id}`}>+ {record.title} · {record.domain}</small>)}{temporalFrameSummary.entered.length === 0 && <small>No entered records</small>}</div>
                <div><span>EXITED</span>{temporalFrameSummary.exited.slice(0, 3).map((record) => <small key={`out:${record.id}`}>− {record.title} · {record.domain}</small>)}{temporalFrameSummary.exited.length === 0 && <small>No exited records</small>}</div>
              </div>}
              {temporalFrameSummary.domainPairs.length > 0 && <div className="timeline-domain-links"><span>DOMAINS IN THIS FRAME</span>{temporalFrameSummary.domainPairs.slice(0, 4).map((pair) => <small key={pair.id}>{pair.leftDomain} ({pair.leftRecordCount}) ↔ {pair.rightDomain} ({pair.rightRecordCount})</small>)}<p>Co-presence is a catalog pattern, not spatial overlap or causation.</p></div>}
              {hasTimelineRecords ? <div className="availability-bars" aria-label="Peak compatible record count in each labeled range; missing years are not filled">{availabilityBins.map((bin) => <i key={bin.start} data-active={previewYear >= bin.start && previewYear <= bin.end} data-committed={temporalQuery.frame >= bin.start && temporalQuery.frame <= bin.end} title={`${formatTimelineStep(bin.start)}–${formatTimelineStep(bin.end)} · peak ${bin.peak} compatible records`} style={{ height: `${Math.min(52, 12 + bin.peak * 5)}px` }}><b>{bin.peak || ""}</b></i>)}</div> : <p className="timeline-empty">No compatible time-aware records in this range. The map keeps the year selectable without implying data.</p>}
            </section>

            <section className="timeline-live-context" data-held={withheldOfficialCount > 0} aria-labelledby="timeline-live-title">
              <header><span>LIVE SOURCE CONTEXT</span><strong id="timeline-live-title">{withheldOfficialCount > 0 ? `${withheldOfficialCount} current source${withheldOfficialCount === 1 ? "" : "s"} held` : `${visibleOfficialCount} selected · ${officialFeatureCount} loaded features`}</strong></header>
              {withheldOfficialCount > 0
                ? <p>Current-only sources are hidden at this year. They return at {formatTimelineStep(OFFICIAL_CONTEXT_PRESENT_FRAME)}; your choices are saved.</p>
                : <p>{officialReadyCount}/{visibleOfficialCount} selected sources settled · latest selected retrieval {officialLatestRetrievedAt ? `${officialLatestRetrievedAt.slice(0, 19).replace("T", " ")} UTC` : "pending"}.</p>}
              <details className="timeline-context-details"><summary>Source clocks and limits</summary>
              <dl>
                <div><dt>Phenomenon clock</dt><dd>{temporalScopeLabel}</dd></div>
                <div><dt>Live-source clock</dt><dd>{year === OFFICIAL_CONTEXT_PRESENT_FRAME ? "Operational present only" : "WITHHELD FROM HISTORICAL FRAME"}</dd></div>
                <div><dt>Interpolation</dt><dd>OFF</dd></div>
                <div><dt>Authority effect</dt><dd>NONE · context only</dd></div>
              </dl>
              <p className="timeline-reference-note">Untimed registry layers, the selected basemap, and interactive terrain remain present-day orientation context across frames; they are excluded from entered/exited metrics and cannot prove historical persistence. Choose Midnight or Prairie to avoid an external basemap request.</p>
              <p className="timeline-trust-note">A time sweep changes renderer filters and captured context. It cannot admit, correct, approve, release, deploy, or publish data.</p>
              </details>
            </section>
            <button className="icon-close timeline-close" type="button" onClick={closeTimelinePanel} aria-label="Close timeline">×</button>
          </div>
          </CompactTimeSweep>
        </section>

        <footer className="status-bar" data-terrain={scenePreset === "elevation-3d"} aria-label="Map status">
          <span><b>{categoryMapOnScreen?.name ?? activeAtlasView?.title ?? "Kansas Overview"}</b> · {selected?.properties.title ?? "Kansas statewide"}</span>
          {scenePreset === "elevation-3d" ? <output className="status-terrain-readout" data-state={terrainState === "ERROR" ? "error" : terrainState !== "READY" ? "loading" : terrainElevationUnavailable ? "unavailable" : terrainElevationReading ? "sample" : "idle"} aria-live="off">
            <em>DEM · {(terrainElevationReading?.provider ?? terrainProvider) === "usgs-3dep" ? "USGS 3DEP" : "MAPZEN"}</em>
            <strong>{terrainState === "ERROR" ? "Unavailable" : terrainState !== "READY" ? "Loading elevation" : terrainElevationReading ? `${terrainElevationReading.feet.toFixed(0)} ft` : terrainElevationUnavailable ? "No sample here" : "Hover for height"}</strong>
            <small>{terrainElevationReading ? `${terrainElevationReading.meters.toFixed(0)} m source height · ${verticalExaggeration.toFixed(1)}× display` : terrainElevationUnavailable ? "No loaded DEM tile at pointer" : "Source DEM height below pointer"}</small>
          </output> : <span>{mapRepresentationLabel}</span>}
          <span>MapLibre {EXPECTED_MAPLIBRE_VERSION} · terrain context only</span>
        </footer>
      </main>

      {LocalWelcomeRecorder && <Suspense fallback={null}><LocalWelcomeRecorder
        getMap={() => mapRef.current}
        prepareBenchmark={() => setGuideOpen(false)}
        freezeSourceFrame={scenario => { localCaptureWindFrameRef.current = scenario.sources.includes("nws-forecast-wind") ? windArrowFrame : null; }}
        releaseSourceFrame={() => { localCaptureWindFrameRef.current = null; }}
        setCapturePixelRatio={value => {
          localCapturePixelRatioRef.current = value;
          const map = mapRef.current, ratio = value ?? browserRenderBudget(renderQuality).pixelRatio;
          if (map && map.getPixelRatio() !== ratio) map.setPixelRatio(ratio);
        }}
        beforeFrame={(scenario, elapsedMs) => {
          // Public redraw renders with timestamp zero. Suppress only display
          // tile fades in the local export so real rasters are not held at 0.
          const map = mapRef.current;
          if (map) for (const layer of map.getStyle().layers) {
            if (layer.type === "raster" && map.getPaintProperty(layer.id, "raster-fade-duration") !== 0) map.setPaintProperty(layer.id, "raster-fade-duration", 0);
          }
          const frame = localCaptureWindFrameRef.current ?? windArrowFrame;
          if (scenario.sources.includes("nws-forecast-wind") && mapRef.current && windArrowCanvasRef.current && frame) {
            drawWindFlowCanvas(windArrowCanvasRef.current, mapRef.current, frame, elapsedMs, true, windFlowToneForBasemap(basemapRef.current));
          }
        }}
        extraCanvases={() => [windArrowCanvasRef.current, waterMotionCanvasRef.current]}
        prepare={scenario => {
          setGuideOpen(false); setLeftOpen(false); setRightOpen(false); setInstrumentOpen(false);
          setTimelineOpen(false); setMapUtilityOpen(false); setUndergroundOpen(false); setSelected(null);
          stopFlyover(false); stopSceneOrbit(false); setPlaying(false); setDaylightPlayback(false);
          setDaylightEnabled(false); hideAllOfficialContext(); chooseTerrainDrawingMode("off");
          setDynamicEffects(false);
          commitTemporalFrame(OFFICIAL_CONTEXT_PRESENT_FRAME, "Local recorded demo · source clocks retained");
          basemapRef.current = scenario.basemap as BasemapKey; setBasemap(scenario.basemap as BasemapKey);
          activateMapRepresentation(scenario.representation as "2d" | "terrain");
          if (scenario.representation === "terrain") { chooseTerrainProvider("mapzen"); changeTerrainDepth(1); }
          for (const id of scenario.sources) { setOfficialContextVisible(id as OfficialContextId, true); setOfficialContextOpacity(id as OfficialContextId, id === "kdot-roads-1918" ? 1 : id === "nasa-lightning-climatology" ? .85 : .75); }
        }}
        captureLayerStates={scenario => {
          const map = mapRef.current; if (!map) return [];
          const layers = map.getStyle().layers;
          return scenario.sources.flatMap((requestedId: string) => {
            const source = OFFICIAL_CONTEXT_BY_ID[requestedId as OfficialContextId];
            return source.layerIds.map(id => {
              const layer = map.getLayer(id), order = layers.findIndex(item => item.id === id);
              return { sourceId: source.sourceId, layerId: id, type: layer?.type ?? "missing", order,
                visibility: layer ? map.getLayoutProperty(id, "visibility") ?? "visible" : "missing",
                rasterOpacity: layer?.type === "raster" ? map.getPaintProperty(id, "raster-opacity") ?? 1 : null,
                rasterFadeDuration: layer?.type === "raster" ? map.getPaintProperty(id, "raster-fade-duration") : null,
                minzoom: layers[order]?.minzoom ?? null, maxzoom: layers[order]?.maxzoom ?? null,
                sourceLoaded: Boolean(map.getSource(source.sourceId) && map.isSourceLoaded(source.sourceId)) };
            });
          });
        }}
        evidence={scenario => {
          const map = mapRef.current;
          const attribution = [scenario.basemap === "imagery" ? "Tiles © Esri" : scenario.basemap === "kansas-aerial" ? "Kansas DASC / KGS · Kansas 911 · Surdex · 2024" : scenario.basemap === "topo" ? "USGS The National Map" : "OpenFreeMap · OpenMapTiles · © OpenStreetMap contributors"];
          const sourceTimes = [scenario.sourceTime];
          const answer = { ready: true, sourceTimes, attribution } as { ready: boolean; pending?: string; error?: string; sourceTimes: string[]; attribution: string[] };
          if (!map || !styleGenerationReadyRef.current || !map.getStyle()?.layers?.length) return { ...answer, ready: false, pending: `style document synchronization${mapMutationErrorRef.current ? ` (${mapMutationErrorRef.current})` : ""}` };
          if (basemapRef.current !== scenario.basemap) return { ...answer, ready: false, error: `Selected ${scenario.basemap} basemap unavailable; actual fallback is ${basemapRef.current}` };
          // isStyleLoaded/areTilesLoaded include unrelated previously selected
          // sources. Prove only this clip's actual basemap and requested layers.
          for (const id of captureBasemapSourceIds(map.getStyle())) {
            if (!map.isSourceLoaded(id)) { answer.ready = false; answer.pending = `${scenario.basemap} basemap source ${id}`; }
          }
          if (reducedMotion) return { ...answer, ready: false, error: "Reduced motion is enabled. Recording does not override this preference." };
          if (scenario.representation === "terrain") {
            attribution.push("Terrain Tiles · Mapzen · AWS Open Data");
            if (terrainState === "ERROR") return { ...answer, ready: false, error: "Terrain source is unavailable" };
            if (terrainState !== "READY") { answer.ready = false; answer.pending = "actual DEM tiles"; }
          }
          for (const requestedId of scenario.sources) {
            const id = requestedId as OfficialContextId, source = OFFICIAL_CONTEXT_BY_ID[id];
            attribution.push(source.attribution);
            if (officialStates[id] === "error" && !(id === "nws-forecast-wind" && localCaptureWindFrameRef.current)) return { ...answer, ready: false, error: `${source.shortTitle} unavailable: ${officialErrors[id] ?? "provider request failed"}` };
            if (id === "nws-forecast-wind") {
              const frame = localCaptureWindFrameRef.current ?? windArrowFrame;
              if (windArrowState === "ERROR" && !localCaptureWindFrameRef.current) return { ...answer, ready: false, error: "Actual GFS wind forecast unavailable" };
              if (!frame || (windArrowState !== "READY" && !localCaptureWindFrameRef.current)) { answer.ready = false; answer.pending = "the real GFS model grid"; }
              else { sourceTimes.splice(0, 1, `${frame.model} · valid ${frame.validTimeUtc}`); sourceTimes.push(`Retrieved ${frame.retrievedAtUtc}`); }
              continue;
            }
            const existingLayers = source.layerIds.filter(layerId => Boolean(map.getLayer(layerId)));
            if (existingLayers.length && existingLayers.every(layerId => map.getLayoutProperty(layerId, "visibility") === "none")) return { ...answer, ready: false, error: `${source.shortTitle} is hidden in the actual map style` };
            for (const layerId of existingLayers) {
              if (map.getLayer(layerId)?.type === "raster" && map.getPaintProperty(layerId, "raster-opacity") === 0) return { ...answer, ready: false, error: `${source.shortTitle} actual raster opacity is zero` };
            }
            const payload = officialPayloadsRef.current[id as OfficialContextFeedId];
            if (source.apiPath && (!payload || payload.featureCount === 0)) { answer.ready = false; answer.pending = `${source.shortTitle} source records`; }
            if (payload) sourceTimes.push(`${source.organization} · retrieved ${payload.retrievedAt}`);
            if (!map.getSource(source.sourceId) || !map.isSourceLoaded(source.sourceId) || !source.layerIds.some(layerId => Boolean(map.getLayer(layerId)))) { answer.ready = false; answer.pending = `${source.shortTitle} map tiles`; }
          }
          return answer;
        }}
        finish={() => { mapRef.current?.stop(); setDaylightPlayback(false); }}
      /></Suspense>}
      <div className="toast" role="status" aria-live="polite" data-visible={Boolean(toast)}>{toast}</div>
    </div>
  );
}
