"use client";

import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import Link from "next/link";
import { BASELINE_STACKS, currentUtcDay } from "./daily-baseline";
import { SourceQualityRow } from "./source-quality-row";
import { DataNotices, RenderQualityControl, TerrainQuickControls } from "./map-toolbar";
import { browserRenderBudget, readRenderQuality, QUALITY_STORAGE_KEY, type RenderQuality } from "./map-performance";
import type { Feature, Geometry } from "geojson";
import type { GeoJSONSource, Map as MapLibreMap, MapSourceDataEvent, Popup, ScaleControl } from "maplibre-gl";
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
  type SearchItem,
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
  setTerrainHeightOverlay,
  setTerrainPresentation,
  setElevationExaggeration,
  TERRAIN_HILLSHADE_LAYER_ID,
  TERRAIN_COLOR_SOURCE_ID,
  TERRAIN_SOURCE_ID,
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
import { ANALYSIS_RECIPES, type AnalysisRecipe } from "./analysis-recipes";
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
import { COUNTY_STARTER_LAYER } from "./county-starter-slice";
import { buildQwenPrompt, type QwenMapContext } from "./qwen-context";
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
import { SynchronizedComparison } from "./snapshot-map";
import { readDraftSnapshot } from "./workspace-storage";
import {
  policyDecisionFromEvidenceState,
  trustStateFromEvidenceState,
  type EvidenceRecord,
  type MapSnapshot,
  type StoryScene,
  type TrustState,
} from "./workspace-model";
import { STRUCTURE_3D_SOURCE, TERRAIN_SOURCES } from "./terrain-sources";
import { EXTERNAL_CONTEXT_SOURCES } from "./external-context-sources";
import {
  applyOfficialContextState,
  defaultOfficialContextOpacity,
  defaultOfficialContextVisibility,
  OFFICIAL_CONTEXT_BY_ID,
  OFFICIAL_CONTEXT_BY_SOURCE_ID,
  OFFICIAL_CONTEXT_INTERACTIVE_LAYER_IDS,
  OFFICIAL_CONTEXT_PRESENT_FRAME,
  OFFICIAL_CONTEXT_SOURCES,
  OFFICIAL_CONTEXT_TEMPORAL_SUPPORT,
  noaaRadarObservationTimeIsApplied,
  officialContextVisibilityForFrame,
  setNoaaRadarObservationTime,
  type OfficialContextFeedId,
  type OfficialContextId,
  type OfficialContextPayload,
  type OfficialContextState,
} from "./live-context";
import { SITE_REGISTRY_COUNTS } from "./site-registry";
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
import {
  buildStreamflowFrame,
  normalizeUsgsStationId,
  parseStreamflowBundle,
  streamflowDisplayFrames,
  type StreamflowBundle,
  type StreamflowFrame,
} from "./streamflow";
import { HydrologyObservatory,
  type HydrologyObservatoryState,
  type HydrologyPlaybackSpeed,
  type HydrologyRange,
} from "./hydrology-observatory";
import {
  NOAA_HYDROLOGY_NETWORK_API_PATH,
  noaaGaugeNetworkGeoJson,
  parseNoaaGaugeNetwork,
} from "./noaa-hydrology";

if (!LAYER_REGISTRY.some((layer) => layer.id === COUNTY_STARTER_LAYER.id)) {
  const extentIndex = LAYER_REGISTRY.findIndex((layer) => layer.id === "kansas-extent");
  LAYER_REGISTRY.splice(extentIndex >= 0 ? extentIndex + 1 : 0, 0, COUNTY_STARTER_LAYER);
}
if (!SEARCH_INDEX.some((item) => item.id === `layer:${COUNTY_STARTER_LAYER.id}`)) {
  SEARCH_INDEX.push({
    id: `layer:${COUNTY_STARTER_LAYER.id}`,
    kind: "layer",
    title: COUNTY_STARTER_LAYER.title,
    subtitle: `${COUNTY_STARTER_LAYER.category} · ${COUNTY_STARTER_LAYER.datasetName}`,
    layerId: COUNTY_STARTER_LAYER.id,
  });
  SEARCH_INDEX.push(...COUNTY_STARTER_LAYER.data.features.map((item) => ({
    id: `feature:${item.properties.fid}`,
    kind: "feature" as const,
    title: item.properties.title,
    subtitle: `${COUNTY_STARTER_LAYER.title} · ${item.properties.fid}`,
    layerId: COUNTY_STARTER_LAYER.id,
    featureId: item.properties.fid,
    focus: [item.properties.focusLng, item.properties.focusLat] as [number, number],
  })));
}

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
};
type DrawerView = "evidence" | "metadata" | "lineage" | "focus";
type LeftPanelMode = "views" | "layers" | "places" | "stories";
type MeasureMode = "point" | "distance" | "area" | null;
type PlaybackSpeed = 0.5 | 1 | 2;
type NoaaRadarFrameLoadState = "idle" | "loading" | "ready" | "error";
type BoxDragMode = "zoom" | "report-area";
type TerrainProfileSample = Readonly<{ distanceMiles: number; elevationMeters: number }>;
type TerrainElevationReading = Readonly<{ longitude: number; latitude: number; meters: number; feet: number }>;
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
type QwenMessage = Readonly<{ role: "user" | "assistant"; content: string }>;
type QwenBridgeState = "ready" | "not-configured" | "error";
type RepositoryConnection = Readonly<{
  state: "idle" | "loading" | "ready" | "error";
  liveCommit?: string;
  shortCommit?: string;
  commitDate?: string | null;
  message?: string | null;
  observedAt?: string;
}>;
type HoverSummary = Readonly<{
  id: string;
  title: string;
  subtitle: string;
  state: string;
  x: number;
  y: number;
}>;
type OfficialSourceSearchItem = Readonly<{
  id: string;
  kind: "source";
  title: string;
  subtitle: string;
  officialContextId: OfficialContextId;
}>;
type GlobalSearchItem = SearchItem | OfficialSourceSearchItem;

type SelectedContext = {
  kind: "registry" | "basemap";
  featureId: string;
  layerId: string;
  layer: LayerRecord;
  properties: FeatureProperties;
  geometry: Feature<Geometry>;
};

const officialContextIdForSelection = (selection: SelectedContext | null): OfficialContextId | null => {
  if (!selection?.featureId.startsWith("official-context:")) return null;
  return OFFICIAL_CONTEXT_SOURCES.find((source) => selection.layerId === `official-context-${source.id}`)?.id ?? null;
};

const selectionCarrierIsVisible = (
  selection: SelectedContext | null,
  registryVisibility: Record<string, boolean>,
  officialVisibility: Record<OfficialContextId, boolean>,
  frame: number,
) => {
  if (!selection) return false;
  if (selection.kind === "registry") return registryVisibility[selection.layerId] === true;
  const officialContextId = officialContextIdForSelection(selection);
  return officialContextId
    ? officialContextVisibilityForFrame(officialVisibility, frame)[officialContextId] === true
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
  category: "Boundaries & places",
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
  { domain: "Terrain / Elevation", state: "PUBLIC-SAFE", detail: "External DEM terrain plus optional USGS 3DEP LiDAR-derived hillshade and slope are display context only; raw point clouds and governed KFM elevation evidence remain held." },
  { domain: "Imagery", state: "PUBLIC-SAFE", detail: "Optional attributed imagery is display context only; it is never KFM evidence." },
] as const);

type PriorityContextGroup = Readonly<{
  id: "seismic" | "hydrology" | "smoke";
  title: string;
  description: string;
  sourceIds: readonly OfficialContextId[];
}>;

const PRIORITY_CONTEXT_GROUPS: readonly PriorityContextGroup[] = Object.freeze([
  Object.freeze({
    id: "seismic",
    title: "Earthquakes + seismic context",
    description: "USGS recent catalog events and Raspberry Shake station locations. Neither connection is an alert or warning.",
    sourceIds: Object.freeze(["usgs-earthquakes", "raspberry-shake-stations"] as const),
  }),
  Object.freeze({
    id: "hydrology",
    title: "Hydrology + water systems",
    description: "Gauge observations, NOAA NWPS status, hydrography, watershed boundaries, and clearly labeled NWM model context.",
    sourceIds: Object.freeze(["usgs-streamflow", "noaa-nwps-gauges", "usgs-3dhp-hydrography", "usgs-wbd-watersheds", "noaa-nwm-analysis", "noaa-nwm-short-range"] as const),
  }),
  Object.freeze({
    id: "smoke",
    title: "Smoke + weather context",
    description: "NOAA HMS smoke footprints with NWS alerts and the exact-time NOAA radar loop kept as separate source roles.",
    sourceIds: Object.freeze(["noaa-hms-smoke", "nws-alerts", "nws-radar"] as const),
  }),
]);

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
const STRUCTURE_FOCUS_PRESETS = Object.freeze([
  Object.freeze({ id: "wichita", label: "Focus Wichita", center: [-97.3375, 37.6872] as [number, number], bearing: -24 }),
  Object.freeze({ id: "topeka", label: "Focus Topeka", center: [-95.689, 39.0473] as [number, number], bearing: 28 }),
  Object.freeze({ id: "ellsworth", label: "Focus Ellsworth", center: [-98.2306, 38.7306] as [number, number], bearing: -18 }),
] as const);
const EXPECTED_MAPLIBRE_VERSION = "6.6.0";
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
) => {
  const next = officialContextVisibilityForFrame(visibility, frame);
  next["nws-radar"] = next["nws-radar"] && noaaRadarReady && Boolean(noaaRadarFrameTime);
  return next;
};
const defaultOrder = LAYER_REGISTRY.map((layer) => layer.id);
const interactiveLayerIds = LAYER_REGISTRY.flatMap((layer) => layer.renderers.filter((renderer) => renderer.interactive).map((renderer) => renderer.id));
const layerDomains = ["ALL", ...Array.from(new Set([...LAYER_REGISTRY.map((layer) => layer.domain), ...DOMAIN_HOLDS.map((hold) => hold.domain)])).sort()] as const;
const catalogCategorySlug = (category: string) => category.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
const drawerViews = ["evidence", "metadata", "lineage", "focus"] as const satisfies readonly DrawerView[];
const drawerViewLabels: Record<DrawerView, string> = {
  evidence: "Evidence",
  metadata: "Summary",
  lineage: "Methods",
  focus: "Focus",
};
const mapUtilityViews = ["report", "inspect", "navigate", "places", "scene", "connections", "import", "compare", "display", "measure", "export", "diagnostics"] as const satisfies readonly MapUtilityView[];
const mapUtilityLabels: Record<MapUtilityView, string> = {
  report: "Report",
  navigate: "Navigate",
  inspect: "Inspect",
  places: "Places",
  scene: "Scene",
  connections: "Sources",
  import: "Import",
  compare: "Compare",
  display: "Display",
  measure: "Measure",
  export: "Export",
  diagnostics: "Diagnostics",
};
const QUICK_LIVE_CONTEXT_IDS = [
  "usgs-streamflow",
  "usgs-earthquakes",
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
const governedRoutes = new Set<GovernedRoute>(["/bootstrap", "/layers", "/evidence"]);

const loadConfiguredMapLibre = async () => {
  await Promise.all(MAPLIBRE_RUNTIME_ASSET_URLS.map(async (url) => {
    const response = await fetch(url, { method: "HEAD", cache: "force-cache" });
    if (!response.ok) throw new Error(`MapLibre runtime asset unavailable (${response.status})`);
    await response.body?.cancel();
  }));
  const maplibregl = await import("maplibre-gl");
  maplibregl.setWorkerUrl(MAPLIBRE_WORKER_URL);
  maplibregl.setMaxParallelImageRequests(browserRenderBudget().imageRequests);
  maplibregl.setWorkerCount(Math.max(1, Math.min(4, Math.floor((navigator.hardwareConcurrency || 4) / 2))));
  const version = maplibregl.getVersion();
  if (version !== EXPECTED_MAPLIBRE_VERSION) throw new Error(`Expected MapLibre ${EXPECTED_MAPLIBRE_VERSION}, received ${version}`);
  if (maplibregl.getWorkerUrl() !== MAPLIBRE_WORKER_URL) throw new Error("MapLibre worker configuration did not persist");
  return { maplibregl, version };
};
const GUIDED_EXAMPLES = Object.freeze([
  Object.freeze({
    id: "supported",
    state: "SUPPORTED",
    title: "Topeka · 2026",
    summary: "See a synthetic observation with a matching demonstration evidence reference.",
    layerId: "atmosphere-observations",
    featureId: "atmo-topeka-2026",
    year: 2026,
  }),
  Object.freeze({
    id: "corrected",
    state: "CORRECTED",
    title: "Hays · 2024",
    summary: "See how a visible correction stays attached to the selected record.",
    layerId: "atmosphere-observations",
    featureId: "atmo-hays-2024",
    year: 2024,
  }),
  Object.freeze({
    id: "withheld",
    state: "WITHHELD",
    title: "Protected context",
    summary: "See why precise detail remains unavailable instead of being inferred.",
    layerId: "public-safe-planning",
    featureId: "planning-generalized-envelope",
    year: 2026,
  }),
] as const);

const KFM_STORY_TRAIL = Object.freeze([
  Object.freeze({
    id: "supported",
    eyebrow: "SUPPORTED",
    title: "A claim with a visible evidence reference",
    narrative: "Start in Topeka with a synthetic observation whose evidence reference matches the selected fixture. The map identifies a candidate; the Evidence Drawer carries the bounded support record.",
    layerId: "atmosphere-observations",
    featureId: "atmo-topeka-2026",
    year: 2026,
  }),
  Object.freeze({
    id: "corrected",
    eyebrow: "CORRECTED",
    title: "A correction stays attached to the record",
    narrative: "Move west to Hays and back to 2024. The earlier value is not silently replaced: the correction state remains visible beside its current demonstration evidence reference.",
    layerId: "atmosphere-observations",
    featureId: "atmo-hays-2024",
    year: 2024,
  }),
  Object.freeze({
    id: "superseded",
    eyebrow: "SUPERSEDED",
    title: "History remains inspectable without becoming current",
    narrative: "Jump to 1910. This illustrative historical-vintage line is retained for lineage, but its superseded state prevents it from supporting a current answer.",
    layerId: "historical-context",
    featureId: "history-route-1910",
    year: 1910,
  }),
  Object.freeze({
    id: "withheld",
    eyebrow: "DENY",
    title: "Protected detail fails closed",
    narrative: "Finish at a deliberately coarse protected-context envelope. Policy denies precise disclosure, so the interface explains the boundary instead of inviting inference from the map.",
    layerId: "public-safe-planning",
    featureId: "planning-generalized-envelope",
    year: 2026,
  }),
] as const);

const GUIDED_START_STORAGE_KEY = "kfm-guided-start-dismissed-v1";
const WORKSPACE_STORAGE_KEY = "kfm-map-workspaces-v1";
const QWEN_QUICK_PROMPTS = Object.freeze([
  "What is visible in this map view?",
  "What changes when I move the time slider?",
  "Which visible layers need verification?",
]);

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
  if (source === "raspberry-shake-stations") return fallback;
  return fallback;
};

const buildBasemapContext = (candidate: BasemapFeatureCandidate, longitude: number, latitude: number): SelectedContext | null => {
  if (!candidate.geometry) return null;
  const properties = candidate.properties ?? {};
  const officialSource = typeof candidate.source === "string" ? OFFICIAL_CONTEXT_BY_SOURCE_ID[candidate.source] : undefined;
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
    category: officialSource.id === "census-counties" ? "Boundaries & places"
      : ["usgs-streamflow", "noaa-nwps-gauges", "usgs-3dhp-hydrography", "usgs-wbd-watersheds", "noaa-nwm-analysis", "noaa-nwm-short-range"].includes(officialSource.id) ? "Hydrology & water"
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
      year: 2026,
      focusLng: longitude,
      focusLat: latitude,
      displayLabel: title,
    },
    geometry: {
      type: "Feature",
      properties: {},
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

const timelineEraLabel = (value: number) => {
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
  if (value === 2026) return "Present operational window · 9 Sep 2026";
  return "Modern record";
};

const TIMELINE_MAJOR_STEPS = new Set<number>([-4_540_000_000, -541_000_000, -2_580_000, -11_700, 1885, 2026]);
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
  const squareMiles = areaSquareMiles(coordinates);
  return unit === "metric" ? `${(squareMiles * 2.58999).toFixed(1)} km² approximate` : `${squareMiles.toFixed(1)} sq mi approximate`;
};

const anchorDistanceMiles = (left: Pick<FeatureProperties, "focusLng" | "focusLat">, right: Pick<FeatureProperties, "focusLng" | "focusLat">) => {
  const earthRadiusMiles = 3958.8;
  const toRadians = (degrees: number) => degrees * (Math.PI / 180);
  const latitudeDelta = toRadians(right.focusLat - left.focusLat);
  const longitudeDelta = toRadians(right.focusLng - left.focusLng);
  const leftLatitude = toRadians(left.focusLat);
  const rightLatitude = toRadians(right.focusLat);
  const haversine = Math.sin(latitudeDelta / 2) ** 2
    + Math.cos(leftLatitude) * Math.cos(rightLatitude) * Math.sin(longitudeDelta / 2) ** 2;
  return earthRadiusMiles * 2 * Math.atan2(Math.sqrt(haversine), Math.sqrt(1 - haversine));
};

export default function Home() {
  const mapContainerRef = useRef<HTMLDivElement>(null);
  const mapRef = useRef<MapLibreMap | null>(null);
  const styleGenerationReadyRef = useRef(false);
  const popupRef = useRef<Popup | null>(null);
  const scaleControlRef = useRef<ScaleControl | null>(null);
  const hoveredRef = useRef<{ source: string; id: string | number } | null>(null);
  const visibilityRef = useRef(defaultVisibility);
  const opacityRef = useRef(defaultOpacity);
  const officialVisibilityRef = useRef(defaultOfficialVisibility);
  const officialOpacityRef = useRef(defaultOfficialOpacity);
  const officialPayloadsRef = useRef<Partial<Record<OfficialContextFeedId, OfficialContextPayload>>>({});
  const officialRequestsRef = useRef(new Set<OfficialContextFeedId>());
  const officialRasterFailuresRef = useRef(new Set<OfficialContextId>());
  const failedTerrainSourceRef = useRef<unknown>(null);
  const noaaRadarRequestRef = useRef<AbortController | null>(null);
  const noaaRadarLastRequestAtRef = useRef(0);
  const noaaRadarReadyRef = useRef(false);
  const noaaRadarManifestRef = useRef<NoaaRadarManifest | null>(null);
  const noaaRadarFrameTimeRef = useRef<string | null>(null);
  const noaaRadarPendingFrameTimeRef = useRef<string | null>(null);
  const noaaRadarRequestedTimeRef = useRef<string | null>(null);
  const noaaRadarFollowLatestRef = useRef(true);
  const noaaRadarFrameLoadCleanupRef = useRef<(() => void) | null>(null);
  const noaaRadarFrameFailureRef = useRef<((message: string) => void) | null>(null);
  const streamflowRequestRef = useRef<AbortController | null>(null);
  const streamflowRequestGenerationRef = useRef(0);
  const streamflowBundleRef = useRef<StreamflowBundle | null>(null);
  const streamflowRequestedTimeRef = useRef<string | null>(null);
  const noaaHydrologyRequestRef = useRef<AbortController | null>(null);
  const orderRef = useRef(defaultOrder);
  const yearRef = useRef<number>(2026);
  const temporalQueryRef = useRef<TemporalSweepQuery>({
    mode: "snapshot",
    frame: 2026,
    rangeStart: TIME_STEPS[0],
    rangeEnd: TIME_STEPS.at(-1)!,
    windowStart: 2026,
  });
  const mapEvidenceFilterRef = useRef<RegistryEvidenceFilter>("ALL");
  const basemapRef = useRef<BasemapKey>("standard");
  const projectionRef = useRef<"mercator" | "globe">("mercator");
  const scenePresetRef = useRef<ScenePresetId>("overview-2d");
  const verticalExaggerationRef = useRef(1);
  const topographicOverlayRef = useRef(false);
  const atmospherePresetRef = useRef<AtmospherePreset>("night");
  const lightAzimuthRef = useRef(210);
  const fieldOfViewRef = useRef(36);
  const structures3DRef = useRef(false);
  const gestureModeRef = useRef<"cooperative" | "direct">("cooperative");
  const sceneOrbitTimerRef = useRef<number | null>(null);
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
  const importInspectionGenerationRef = useRef(0);
  const importInputRef = useRef<HTMLInputElement>(null);
  const cameraHistoryRef = useRef<ViewState[]>([KANSAS_VIEW]);
  const cameraHistoryIndexRef = useRef(0);
  const replayingCameraHistoryRef = useRef(false);
  const returnFocusRef = useRef<HTMLElement | null>(null);
  const leftPanelRef = useRef<HTMLElement>(null);
  const rightPanelRef = useRef<HTMLElement>(null);
  const timelineRef = useRef<HTMLElement>(null);
  const repositoryButtonRef = useRef<HTMLButtonElement>(null);
  const repositoryPanelRef = useRef<HTMLElement>(null);
  const workspaceDetailsRef = useRef<HTMLDetailsElement>(null);
  const mapUtilityButtonRef = useRef<HTMLButtonElement>(null);
  const globalSearchInputRef = useRef<HTMLInputElement>(null);
  const mapUtilityPanelRef = useRef<HTMLElement>(null);
  const mapUtilityReturnRef = useRef<HTMLElement | null>(null);
  const mapUtilityTabRefs = useRef<Array<HTMLButtonElement | null>>([]);
  const drawerTabRefs = useRef<Array<HTMLButtonElement | null>>([]);
  const pendingViewRef = useRef<ViewState | null>(null);
  const lastKnownGoodViewRef = useRef<ViewState>(KANSAS_VIEW);
  const locationDerivedViewRef = useRef(false);
  const compactRef = useRef(false);
  const openSelectionRef = useRef<(context: SelectedContext, returnElement?: HTMLElement | null) => void>(() => undefined);

  const [visibility, setVisibility] = useState<Record<string, boolean>>(defaultVisibility);
  const [opacity, setOpacity] = useState<Record<string, number>>(defaultOpacity);
  const [officialVisibility, setOfficialVisibility] = useState<Record<OfficialContextId, boolean>>(defaultOfficialVisibility);
  const [officialOpacity, setOfficialOpacity] = useState<Record<OfficialContextId, number>>(defaultOfficialOpacity);
  const [officialStates, setOfficialStates] = useState<Record<OfficialContextId, OfficialContextState>>(defaultOfficialStates);
  const [officialPayloads, setOfficialPayloads] = useState<Partial<Record<OfficialContextFeedId, OfficialContextPayload>>>({});
  const [officialErrors, setOfficialErrors] = useState<Partial<Record<OfficialContextId, string>>>({});
  const [noaaRadarManifestState, setNoaaRadarManifestState] = useState<NoaaRadarManifestState>("idle");
  const [noaaRadarManifest, setNoaaRadarManifest] = useState<NoaaRadarManifest | null>(null);
  const [noaaRadarManifestError, setNoaaRadarManifestError] = useState("");
  const [noaaRadarFrameTime, setNoaaRadarFrameTime] = useState<string | null>(null);
  const [noaaRadarPendingFrameTime, setNoaaRadarPendingFrameTime] = useState<string | null>(null);
  const [noaaRadarLoopSpan, setNoaaRadarLoopSpan] = useState<NoaaRadarLoopSpanMinutes>(60);
  const [noaaRadarPlaybackSpeed, setNoaaRadarPlaybackSpeed] = useState<NoaaRadarPlaybackSpeed>(1);
  const [noaaRadarPlaying, setNoaaRadarPlaying] = useState(false);
  const [noaaRadarFollowLatest, setNoaaRadarFollowLatest] = useState(true);
  const [noaaRadarFrameLoadState, setNoaaRadarFrameLoadState] = useState<NoaaRadarFrameLoadState>("idle");
  const [noaaRadarClock, setNoaaRadarClock] = useState(() => Date.now());
  const [streamflowBundle, setStreamflowBundle] = useState<StreamflowBundle | null>(null);
  const [streamflowState, setStreamflowState] = useState<HydrologyObservatoryState>("idle");
  const [streamflowError, setStreamflowError] = useState<string | null>(null);
  const [streamflowFrameIndex, setStreamflowFrameIndex] = useState(-1);
  const [streamflowPlaying, setStreamflowPlaying] = useState(false);
  const [streamflowPlaybackSpeed, setStreamflowPlaybackSpeed] = useState<HydrologyPlaybackSpeed>(1);
  const [streamflowRange, setStreamflowRange] = useState<HydrologyRange>("24h");
  const [streamflowSelectedStationId, setStreamflowSelectedStationId] = useState<string | null>(null);
  const [liveInstrument, setLiveInstrument] = useState<"river" | "radar">("river");
  const [layerOrder, setLayerOrder] = useState<string[]>(defaultOrder);
  const [basemap, setBasemap] = useState<BasemapKey>("standard");
  const [view, setView] = useState<ViewState>(KANSAS_VIEW);
  const [scenePreset, setScenePreset] = useState<ScenePresetId>("overview-2d");
  const [terrainState, setTerrainState] = useState<TerrainPresentationState>("OFF");
  const [topographicOverlay, setTopographicOverlay] = useState(false);
  const [terrainElevationReading, setTerrainElevationReading] = useState<TerrainElevationReading | null>(null);
  const [lockedTerrainElevation, setLockedTerrainElevation] = useState<TerrainElevationReading | null>(null);
  const [verticalExaggeration, setVerticalExaggeration] = useState(1);
  const [atmospherePreset, setAtmospherePreset] = useState<AtmospherePreset>("night");
  const [lightAzimuth, setLightAzimuth] = useState(210);
  const [fieldOfView, setFieldOfView] = useState(36);
  const [structures3DEnabled, setStructures3DEnabled] = useState(false);
  const [structures3DState, setStructures3DState] = useState<Structures3DState>("OFF");
  const [gestureMode, setGestureMode] = useState<"cooperative" | "direct">("cooperative");
  const [sceneOrbiting, setSceneOrbiting] = useState(false);
  const [dynamicEffects, setDynamicEffects] = useState(true);
  const [reducedMotion, setReducedMotion] = useState(false);
  const [mapViewportBounds, setMapViewportBounds] = useState<MapBoundsState>(SUPPORTED_CONTEXT_BOUNDS);
  const [analysisArea, setAnalysisArea] = useState<MapBoundsState | null>(null);
  const [boxDragMode, setBoxDragMode] = useState<BoxDragMode>("zoom");
  const [importPreview, setImportPreview] = useState<LocalImportPreview | null>(null);
  const [importPreviewVisible, setImportPreviewVisible] = useState(false);
  const [importError, setImportError] = useState("");
  const [importBusy, setImportBusy] = useState(false);
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
  });
  const [styleReady, setStyleReady] = useState(false);
  const [renderQuality, setRenderQuality] = useState<RenderQuality>("auto");
  useEffect(() => { setRenderQuality(readRenderQuality()); }, []);
  useEffect(() => {
    const map = mapRef.current; if (!map) return;
    let disposed = false;
    const apply = () => { const budget = browserRenderBudget(renderQuality); map.setPixelRatio(budget.pixelRatio); void import("maplibre-gl").then(gl => { if (!disposed) gl.setMaxParallelImageRequests(budget.imageRequests); }); };
    apply(); window.addEventListener("resize", apply);
    return () => { disposed = true; window.removeEventListener("resize", apply); };
  }, [renderQuality, styleReady]);
  const chooseRenderQuality = (value: RenderQuality) => { setRenderQuality(value); try { localStorage.setItem(QUALITY_STORAGE_KEY, value); } catch { /* The current session still uses the selected quality. */ } };
  const [locationCameraRedacted, setLocationCameraRedacted] = useState(false);
  const [selected, setSelected] = useState<SelectedContext | null>(null);
  const [hoverSummary, setHoverSummary] = useState<HoverSummary | null>(null);
  const [primaryWorkspace, setPrimaryWorkspace] = useState<PrimaryWorkspace>("map");
  const [workspaceSnapshot, setWorkspaceSnapshot] = useState<MapSnapshot | null>(null);
  const [leftOpen, setLeftOpen] = useState(false);
  const [sourceStatusOpen, setSourceStatusOpen] = useState(false);
  const [instrumentOpen, setInstrumentOpen] = useState(false);
  const [leftPanelMode, setLeftPanelMode] = useState<LeftPanelMode>("layers");
  const [rightOpen, setRightOpen] = useState(false);
  const [timelineOpen, setTimelineOpen] = useState(false);
  const [drawerView, setDrawerView] = useState<DrawerView>("evidence");
  const [focusStage, setFocusStage] = useState<FocusStage>("outcome");
  const [focusIntent, setFocusIntent] = useState<FocusIntentId>("explain");
  const [pendingFocusAction, setPendingFocusAction] = useState<FocusActionProposal | null>(null);
  const [layerQuery, setLayerQuery] = useState("");
  const [atlasViewQuery, setAtlasViewQuery] = useState("");
  const [layerDomain, setLayerDomain] = useState<(typeof layerDomains)[number]>("ALL");
  const [globalQuery, setGlobalQuery] = useState("");
  const [expandedLayers, setExpandedLayers] = useState<Set<string>>(new Set());
  const [year, setYear] = useState<number>(OFFICIAL_CONTEXT_PRESENT_FRAME);
  const [previewYear, setPreviewYear] = useState<number>(OFFICIAL_CONTEXT_PRESENT_FRAME);
  const [baselineDay, setBaselineDay] = useState(currentUtcDay);
  const [mapEvidenceFilter, setMapEvidenceFilter] = useState<RegistryEvidenceFilter>("ALL");
  const [playing, setPlaying] = useState(false);
  const [temporalMode, setTemporalMode] = useState<TemporalSweepMode>("snapshot");
  const [temporalStepRule, setTemporalStepRule] = useState<TemporalStepRule>("available-events");
  const [playbackSpeed, setPlaybackSpeed] = useState<PlaybackSpeed>(1);
  const [playbackDirection, setPlaybackDirection] = useState<TemporalPlaybackDirection>("forward");
  const [playbackLoopMode, setPlaybackLoopMode] = useState<TemporalLoopMode>("stop");
  const [sweepRangeStart, setSweepRangeStart] = useState<number>(TIME_STEPS[0]);
  const [sweepRangeEnd, setSweepRangeEnd] = useState<number>(TIME_STEPS.at(-1)!);
  const [movingWindowFrames, setMovingWindowFrames] = useState(3);
  const [toolsExpanded, setToolsExpanded] = useState(false);
  const [measureMode, setMeasureMode] = useState<MeasureMode>(null);
  const [measurementGeometryMode, setMeasurementGeometryMode] = useState<MeasureMode>(null);
  const [measureCoordinateCount, setMeasureCoordinateCount] = useState(0);
  const [measureUnit, setMeasureUnit] = useState<MeasureUnit>("imperial");
  const [measurement, setMeasurement] = useState("Select a measurement tool");
  const [terrainProfile, setTerrainProfile] = useState<readonly TerrainProfileSample[]>([]);
  const [mapUtilityOpen, setMapUtilityOpen] = useState(false);
  const [mapContextOpen, setMapContextOpen] = useState(false);
  const composerRef = useRef<HTMLElement>(null);
  const composerTriggerRef = useRef<HTMLButtonElement>(null);
  const [mapUtilityView, setMapUtilityView] = useState<MapUtilityView>("navigate");
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
  const [nearbyRadiusMiles, setNearbyRadiusMiles] = useState(100);
  const [nearbyVisibleLayersOnly, setNearbyVisibleLayersOnly] = useState(false);
  const [compareLeftId, setCompareLeftId] = useState("water-context");
  const [compareRightId, setCompareRightId] = useState("atmosphere-observations");
  const [compareTimeA, setCompareTimeA] = useState<number>(1910);
  const [compareTimeB, setCompareTimeB] = useState<number>(2026);
  const [coordinateLatitude, setCoordinateLatitude] = useState(String(KANSAS_VIEW.center[1]));
  const [coordinateLongitude, setCoordinateLongitude] = useState(String(KANSAS_VIEW.center[0]));
  const [coordinateError, setCoordinateError] = useState("");
  const [projection, setProjection] = useState<"mercator" | "globe">("mercator");
  const [helpOpen, setHelpOpen] = useState(false);
  const [repositoryOpen, setRepositoryOpen] = useState(false);
  const [guidedStartOpen, setGuidedStartOpen] = useState(false);
  const [storyOpen, setStoryOpen] = useState(false);
  const [storyStepIndex, setStoryStepIndex] = useState(0);
  const [currentWorkspace, setCurrentWorkspace] = useState<PublicWorkspaceId>("explore");
  const [repositoryView, setRepositoryView] = useState<RepositoryView>("updates");
  const [scenarioReviewMode, setScenarioReviewMode] = useState<ScenarioReviewMode>("held");
  const [functionGroup, setFunctionGroup] = useState<FunctionGroup>("PUBLIC_INTERFACE");
  const [activeFunctionId, setActiveFunctionId] = useState("export");
  const [functionQuery, setFunctionQuery] = useState("");
  const [featureQuery, setFeatureQuery] = useState("");
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
  const [qwenOpen, setQwenOpen] = useState(false);
  const [qwenQuestion, setQwenQuestion] = useState("");
  const [qwenBusy, setQwenBusy] = useState(false);
  const [qwenBridgeState, setQwenBridgeState] = useState<QwenBridgeState>("not-configured");
  const [qwenMessages, setQwenMessages] = useState<readonly QwenMessage[]>([
    {
      role: "assistant",
      content: "Ask Qwen about the current map view. The bridge sends only the selected map context; no inference endpoint is connected to this Site yet, so you can copy a grounded prompt for local Qwen/Ollama.",
    },
  ]);
  const [toast, setToast] = useState("");
  const [isCompact, setIsCompact] = useState(false);
  const [sourceStates, setSourceStates] = useState<Record<string, "loading" | "ready" | "error">>(
    Object.fromEntries(LAYER_REGISTRY.map((layer) => [layer.id, "loading"])),
  );

  const debouncedGlobalQuery = useDebounced(globalQuery, 140);
  const debouncedLayerQuery = useDebounced(layerQuery, 140);

  useEffect(() => { visibilityRef.current = visibility; }, [visibility]);
  useEffect(() => { opacityRef.current = opacity; }, [opacity]);
  useEffect(() => { officialVisibilityRef.current = officialVisibility; }, [officialVisibility]);
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
      }
    };
    syncPreference();
    preference.addEventListener("change", syncPreference);
    return () => preference.removeEventListener("change", syncPreference);
  }, []);
  useEffect(() => {
    const restoreSavedWorkspaces = window.setTimeout(() => {
      try {
        const stored = JSON.parse(window.localStorage.getItem(WORKSPACE_STORAGE_KEY) ?? "[]");
        if (Array.isArray(stored)) setSavedWorkspaces(stored.slice(0, MAX_PLACE_TRAIL_STOPS));
      } catch { /* Device-local workspace storage is optional. */ }
    }, 0);
    return () => window.clearTimeout(restoreSavedWorkspaces);
  }, []);

  useEffect(() => () => {
    if (placeTourTimerRef.current !== null) window.clearTimeout(placeTourTimerRef.current);
    noaaRadarRequestRef.current?.abort();
    noaaRadarFrameLoadCleanupRef.current?.();
    streamflowRequestRef.current?.abort();
    noaaHydrologyRequestRef.current?.abort();
  }, []);

  const dismissGuidedStart = useCallback(() => {
    setGuidedStartOpen(false);
    try { window.localStorage.setItem(GUIDED_START_STORAGE_KEY, "1"); } catch { /* Device storage is optional. */ }
  }, []);

  const showGuidedStart = useCallback(() => {
    setHelpOpen(false);
    setGuidedStartOpen(true);
    try { window.localStorage.removeItem(GUIDED_START_STORAGE_KEY); } catch { /* Device storage is optional. */ }
  }, []);

  // The map opens as a working surface. Guided material remains available from About.
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
  const visibleOfficialCount = visibleOfficialSources.length;
  const noaaRadarManifestFresh = noaaRadarManifestIsFresh(noaaRadarManifest, noaaRadarClock);
  const noaaRadarRenderable = Boolean(noaaRadarFrameTime && noaaRadarManifestFresh);
  useEffect(() => {
    noaaRadarReadyRef.current = noaaRadarRenderable;
    if (!noaaRadarRenderable) setNoaaRadarPlaying(false);
  }, [noaaRadarRenderable]);
  const effectiveOfficialVisibility = useMemo(
    () => officialContextRuntimeVisibility(officialVisibility, temporalQuery.frame, noaaRadarRenderable, noaaRadarFrameTime),
    [noaaRadarFrameTime, noaaRadarRenderable, officialVisibility, temporalQuery.frame],
  );
  const withheldOfficialCount = temporalQuery.frame === OFFICIAL_CONTEXT_PRESENT_FRAME ? 0 : visibleOfficialCount;
  const selectedIsHeldOfficialContext = Boolean(
    selected
    && selected.featureId.startsWith("official-context:")
    && temporalQuery.frame !== OFFICIAL_CONTEXT_PRESENT_FRAME,
  );
  const selectedTimeMismatch = Boolean(
    selected
    && (selectedIsHeldOfficialContext || !isFeatureAvailableForTemporalQuery(selected.layer, selected.properties.year, temporalQuery)),
  );
  const officialFeatureCount = useMemo(() => Object.values(officialPayloads).reduce((total, payload) => total + (payload?.featureCount ?? 0), 0), [officialPayloads]);
  const visibleRefreshableOfficialCount = useMemo(() => visibleOfficialSources.filter((source) => source.apiPath || source.managedAdapterPath || source.id === "nws-radar").length, [visibleOfficialSources]);
  const officialReadyCount = useMemo(() => Object.values(officialStates).filter((state) => state === "ready" || state === "partial" || state === "empty").length, [officialStates]);
  const officialLoadingCount = useMemo(() => Object.values(officialStates).filter((state) => state === "loading").length, [officialStates]);
  const officialLatestRetrievedAt = useMemo(() => Object.values(officialPayloads)
    .map((payload) => payload?.retrievedAt)
    .filter((value): value is string => Boolean(value))
    .concat(noaaRadarManifest?.retrievedAt ?? [])
    .sort()
    .at(-1) ?? null, [noaaRadarManifest?.retrievedAt, officialPayloads]);
  const streamflowFrames = useMemo(() => streamflowBundle ? streamflowDisplayFrames(streamflowBundle) : [], [streamflowBundle]);
  const safeStreamflowFrameIndex = streamflowFrames.length === 0 ? -1 : clamp(streamflowFrameIndex, 0, streamflowFrames.length - 1);
  const streamflowFrameTime = safeStreamflowFrameIndex >= 0 ? streamflowFrames[safeStreamflowFrameIndex] : null;
  const streamflowFrame = useMemo<StreamflowFrame | null>(() => {
    if (!streamflowBundle || !streamflowFrameTime) return null;
    const toleranceMinutes = streamflowRange === "1y" ? 36 * 60 : streamflowRange === "24h" ? 30 : 90;
    return buildStreamflowFrame(streamflowBundle, streamflowFrameTime, toleranceMinutes);
  }, [streamflowBundle, streamflowFrameTime, streamflowRange]);
  const streamflowLatestTime = streamflowFrames.at(-1) ?? null;
  const streamflowLatestAgeMinutes = streamflowLatestTime ? Math.max(0, Math.floor((Date.now() - Date.parse(streamflowLatestTime)) / 60_000)) : null;
  const streamflowDisplayState: HydrologyObservatoryState = streamflowState === "ready"
    && streamflowBundle?.query.mode === "recent-series"
    && streamflowLatestAgeMinutes !== null
    && streamflowLatestAgeMinutes > 60
    ? "stale"
    : streamflowState;
  const streamflowSelectedAtPresent = officialVisibility["usgs-streamflow"] && temporalQuery.frame === OFFICIAL_CONTEXT_PRESENT_FRAME;
  const noaaRadarLoopFrames = useMemo(
    () => selectNoaaRadarLoopFrames(noaaRadarManifest?.frames ?? [], noaaRadarLoopSpan, NOAA_RADAR_MAX_LOOP_FRAMES),
    [noaaRadarLoopSpan, noaaRadarManifest?.frames],
  );
  const noaaRadarLatestFrame = noaaRadarLoopFrames.at(-1) ?? null;
  const noaaRadarFrameIndex = noaaRadarFrameTime ? noaaRadarLoopFrames.indexOf(noaaRadarFrameTime) : -1;
  const noaaRadarActiveFrame = noaaRadarFrameIndex >= 0 ? noaaRadarLoopFrames[noaaRadarFrameIndex] : null;
  const noaaRadarAgeMinutes = noaaRadarActiveFrame ? noaaRadarFrameAgeMinutes(noaaRadarActiveFrame, noaaRadarClock) : null;
  const noaaRadarLatestAgeMinutes = noaaRadarLatestFrame ? noaaRadarFrameAgeMinutes(noaaRadarLatestFrame, noaaRadarClock) : null;
  const noaaRadarSelectedAtPresent = officialVisibility["nws-radar"] && temporalQuery.frame === OFFICIAL_CONTEXT_PRESENT_FRAME;
  const liveDockVisible = instrumentOpen && (streamflowSelectedAtPresent || noaaRadarSelectedAtPresent);
  const showStreamflowDock = streamflowSelectedAtPresent && (liveInstrument === "river" || !noaaRadarSelectedAtPresent);
  const showRadarDock = noaaRadarSelectedAtPresent && (liveInstrument === "radar" || !streamflowSelectedAtPresent);
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
    const query = atlasViewQuery.trim().toLowerCase();
    if (!query) return LIVING_ATLAS_VIEWS;
    return LIVING_ATLAS_VIEWS.filter((view) => (
      [view.title, view.question, view.scope, view.time, view.sourcePosture, view.report, ...view.domains]
        .join(" ")
        .toLowerCase()
        .includes(query)
    ));
  }, [atlasViewQuery]);
  const activeViewProfileId = useMemo(() => MAP_VIEW_PROFILES.find((profile) => (
    profile.year === year
    && profile.basemap === basemap
    && profile.projection === projection
    && LAYER_REGISTRY.every((layer) => visibility[layer.id] === profile.visibleLayerIds.includes(layer.id))
  ))?.id ?? null, [basemap, projection, visibility, year]);
  const activeViewProfile = useMemo(
    () => MAP_VIEW_PROFILES.find((profile) => profile.id === activeViewProfileId) ?? null,
    [activeViewProfileId],
  );
  const activeAtlasView = useMemo(
    () => LIVING_ATLAS_VIEWS.find((atlasView) => atlasView.profileId === activeViewProfileId && atlasView.status === "SITE_DEMO")
      ?? LIVING_ATLAS_VIEWS.find((atlasView) => atlasView.id === "kansas-overview"),
    [activeViewProfileId],
  );
  const primaryRepresentationLabel = scenePreset === "elevation-3d"
    ? `Terrain 3D · ${terrainState === "READY" ? "DEM" : terrainState === "ERROR" ? "unavailable" : "loading"}`
    : projection === "globe"
      ? "Globe"
      : "2D";
  const mapRepresentationLabel = `${primaryRepresentationLabel}${structures3DEnabled ? ` · Structures 3D ${structures3DState === "READY" ? "ready" : structures3DState.toLowerCase()}` : ""}`;
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
    return {
      source,
      visible: officialVisibility[source.id],
      activeAtFrame: effectiveOfficialVisibility[source.id],
      state: officialStates[source.id],
      featureCount: payload?.featureCount,
      retrievedAt: payload?.retrievedAt,
      limitation: payload?.limitation,
      temporalSupport: OFFICIAL_CONTEXT_TEMPORAL_SUPPORT[source.id],
    };
  }), [effectiveOfficialVisibility, officialPayloads, officialStates, officialVisibility]);
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
    if (active && source.id === "aws-mapzen-terrarium") {
      state = terrainState === "READY" ? "READY" : terrainState === "ERROR" ? "ERROR" : "REQUESTING";
    } else if (active) {
      state = styleReady && maplibreProbe.tilesLoaded ? "READY" : runtime.kind === "error" ? "ERROR" : "REQUESTING";
    }
    return { source, active, state };
  }), [basemap, maplibreProbe.tilesLoaded, runtime.kind, scenePreset, styleReady, terrainState]);
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
        state: state(maplibreProbe.mapConstructed && maplibreProbe.canvasReady, startupFailed && !maplibreProbe.mapConstructed),
      },
      {
        id: "style",
        label: "Style Specification v8",
        detail: `${BASEMAPS[basemap].title} · ${maplibreProbe.styleLoaded ? "style loaded" : "style pending"}`,
        state: state(maplibreProbe.styleLoaded, startupFailed),
      },
      {
        id: "sources",
        label: "Bounded local sources",
        detail: `${maplibreProbe.sourcesReady}/${LAYER_REGISTRY.length} GeoJSON sources · ${maplibreProbe.idle ? "idle" : "working"} · ${maplibreProbe.tilesLoaded ? "tiles settled" : "tiles pending"}`,
        state: state(maplibreProbe.sourcesReady === LAYER_REGISTRY.length && maplibreProbe.idle && maplibreProbe.tilesLoaded, startupFailed || sourceStateCounts.error > 0),
      },
      {
        id: "interaction",
        label: "Controls + interactions",
        detail: "Unified KFM dock, scale, pan, zoom, keyboard, hover, selection, cluster expansion, measurement, camera history, and analysis-area handlers",
        state: state(maplibreProbe.controlsReady && maplibreProbe.interactionsReady, startupFailed),
      },
      {
        id: "projection",
        label: "Projection + fallback",
        detail: maplibreProbe.mapConstructed ? `${maplibreProbe.projection} active · Mercator remains the explicit 2D fallback` : "Renderer unavailable · catalog and evidence interfaces remain active",
        state: state(maplibreProbe.mapConstructed, startupFailed),
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
  const nearbyContext = useMemo(() => {
    if (!selected || selectedTimeMismatch) return [];
    const perLayerCount = new Map<string, number>();
    return LAYER_REGISTRY
      .filter((layer) => !nearbyVisibleLayersOnly || visibility[layer.id])
      .flatMap((layer) => layer.data.features
        .filter((feature) => feature.properties.fid !== selected.featureId)
        .filter((feature) => isFeatureAvailableForTemporalQuery(layer, feature.properties.year, temporalQuery))
        .filter((feature) => mapEvidenceFilter === "ALL" || feature.properties.evidenceState === mapEvidenceFilter)
        .map((feature) => ({ layer, feature, distanceMiles: anchorDistanceMiles(selected.properties, feature.properties) })))
      .filter((row) => row.distanceMiles <= nearbyRadiusMiles)
      .sort((left, right) => left.distanceMiles - right.distanceMiles)
      .filter((row) => {
        const currentCount = perLayerCount.get(row.layer.id) ?? 0;
        if (currentCount >= 2) return false;
        perLayerCount.set(row.layer.id, currentCount + 1);
        return true;
      })
      .slice(0, 16);
  }, [mapEvidenceFilter, nearbyRadiusMiles, nearbyVisibleLayersOnly, selected, selectedTimeMismatch, temporalQuery, visibility]);
  const qwenContext = useMemo<QwenMapContext>(() => ({
    camera: {
      center: [Number(view.center[0].toFixed(5)), Number(view.center[1].toFixed(5))],
      zoom: Number(view.zoom.toFixed(2)),
      bearing: Number(view.bearing.toFixed(1)),
      pitch: Number(view.pitch.toFixed(1)),
      projection,
      representation: mapRepresentationLabel,
    },
    basemap: { key: basemap, title: BASEMAPS[basemap].title, note: BASEMAPS[basemap].note },
    time: { value: temporalQuery.frame, label: temporalScopeLabel, era: `${timelineEraLabel(temporalQuery.frame)} · ${temporalMode.replaceAll("-", " ")}` },
    visibleLayers: activeLayers.slice(0, 14).map((layer) => ({
      id: layer.id,
      title: layer.title,
      domain: layer.domain,
      sourceType: layer.sourceType,
      releaseState: layer.releaseState,
      publicStatus: layer.publicStatus,
      freshnessState: layer.freshnessState,
    })),
    selection: selected && !selectedTimeMismatch ? {
      featureId: selected.featureId,
      title: selected.properties.title,
      layerId: selected.layerId,
      layerTitle: selected.layer.title,
      domain: selected.layer.domain,
      evidenceState: selected.properties.evidenceState,
      evidenceReference: selected.properties.citation,
      sourceYear: selected.properties.year,
      spatialScope: selected.properties.spatialScope,
      summary: selected.properties.summary,
    } : null,
    nearbyContext: nearbyContext.slice(0, 8).map((row) => ({
      title: row.feature.properties.title,
      layerTitle: row.layer.title,
      distanceMiles: Number(row.distanceMiles.toFixed(1)),
      evidenceState: row.feature.properties.evidenceState,
    })),
  }), [activeLayers, basemap, mapRepresentationLabel, nearbyContext, projection, selected, selectedTimeMismatch, temporalMode, temporalQuery.frame, temporalScopeLabel, view]);
  const qwenPrompt = useMemo(() => buildQwenPrompt(qwenQuestion, qwenContext), [qwenContext, qwenQuestion]);
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
  const reportFindings = useMemo(() => {
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
  }, [compareTimeA, compareTimeB, reportEvidenceCounts, reportLayerSummary, reportRecords.length, reportScope, reportTemporalComparison.changedLayerCount, temporalScopeLabel]);
  const filteredLayerIds = useMemo(() => {
    const query = debouncedLayerQuery.trim().toLowerCase();
    return new Set(LAYER_REGISTRY.filter((layer) => {
      const matchesDomain = layerDomain === "ALL" || layer.domain === layerDomain;
      const matchesQuery = !query || `${layer.title} ${layer.description} ${layer.category} ${layer.datasetName} ${layer.domain}`.toLowerCase().includes(query);
      return matchesDomain && matchesQuery;
    }).map((layer) => layer.id));
  }, [debouncedLayerQuery, layerDomain]);
  const searchResults = useMemo<GlobalSearchItem[]>(() => {
    const query = debouncedGlobalQuery.trim().toLowerCase();
    if (!query) return [];
    const mapResults: GlobalSearchItem[] = SEARCH_INDEX.filter((item) => `${item.title} ${item.subtitle}`.toLowerCase().includes(query));
    const sourceResults: GlobalSearchItem[] = OFFICIAL_CONTEXT_SOURCES
      .filter((source) => `${source.title} ${source.shortTitle} ${source.organization} ${source.domain} ${source.endpointLabel}`.toLowerCase().includes(query))
      .map((source) => ({ id: `source:${source.id}`, kind: "source", title: source.shortTitle, subtitle: `${source.organization} · ${source.domain}`, officialContextId: source.id }));
    return [...sourceResults, ...mapResults].slice(0, 7);
  }, [debouncedGlobalQuery]);
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
    return functionsForGroup(functionGroup).filter((record) => !query || `${record.title} ${record.summary} ${record.interface} ${record.boundary} ${record.authority} ${record.maturity} ${record.inventory} ${record.sourceLabel}`.toLowerCase().includes(query));
  }, [functionGroup, functionQuery]);
  const activeFunction = FUNCTION_REGISTRY.find((record) => record.id === activeFunctionId && record.group === functionGroup) ?? filteredFunctions[0] ?? functionsForGroup(functionGroup)[0];
  const functionCounts = useMemo(() => Object.fromEntries(["ACTIVE", "BOUNDED", "DOCUMENTED", "GATED"].map((state) => [state, FUNCTION_REGISTRY.filter((record) => record.state === state).length])), []);
  const filteredFeatures = useMemo(() => {
    const query = featureQuery.trim().toLowerCase();
    return FEATURE_CATALOG.filter((feature) => {
      if (featureArea !== "ALL" && feature.area !== featureArea) return false;
      if (featureMaturity !== "ALL" && feature.maturity !== featureMaturity) return false;
      return !query || `${feature.name} ${feature.area} ${feature.maturity} ${feature.summary} ${feature.path} ${feature.keywords.join(" ")}`.toLowerCase().includes(query);
    });
  }, [featureArea, featureMaturity, featureQuery]);
  const featureMaturityCounts = useMemo(() => Object.fromEntries(
    (["VERIFIED_SLICE", "FIXTURE_FIRST", "DOCUMENTED", "HOLD"] as const)
      .map((maturity) => [maturity, FEATURE_CATALOG.filter((feature) => feature.maturity === maturity).length]),
  ), []);
  const activeTransition = TRANSITION_BOUNDARIES.find((transition) => transition.id === activeTransitionId) ?? TRANSITION_BOUNDARIES[0];
  const governedRouteResult = useMemo(() => inspectGovernedRoute(governedMethod, governedRoute), [governedMethod, governedRoute]);
  const compareLeft = LAYER_REGISTRY.find((layer) => layer.id === compareLeftId) ?? LAYER_REGISTRY[0];
  const compareRight = LAYER_REGISTRY.find((layer) => layer.id === compareRightId) ?? LAYER_REGISTRY[1];
  const planningScenarioReview = PLANNING_SCENARIO_REVIEWS[scenarioReviewMode];
  const activeStoryStep = KFM_STORY_TRAIL[storyStepIndex] ?? KFM_STORY_TRAIL[0];

  const selectedLabel = selected?.properties.title ?? "Statewide Kansas";
  const selectedEvidence = selected ? evidenceLabels[selected.properties.evidenceState] : null;
  const selectedLayerHidden = Boolean(selected && !selectionCarrierIsVisible(selected, visibility, officialVisibility, temporalQuery.frame));
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
    locationCameraRedacted,
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
    params.set("ctxo", OFFICIAL_CONTEXT_SOURCES.map((source) => `${source.id}:${(officialOpacity[source.id] ?? source.defaultOpacity).toFixed(2)}`).join(","));
    if (officialVisibility["nws-radar"] && noaaRadarFrameTime) {
      params.set("radarTime", noaaRadarFrameTime);
      params.set("radarSpan", String(noaaRadarLoopSpan));
      params.set("radarSpeed", String(noaaRadarPlaybackSpeed));
      params.set("radarFollow", noaaRadarFollowLatest ? "latest" : "selected");
    }
    if (officialVisibility["usgs-streamflow"]) {
      params.set("hydroRange", streamflowRange);
      params.set("hydroSpeed", String(streamflowPlaybackSpeed));
      if (streamflowFrameTime) params.set("hydroTime", streamflowFrameTime);
      if (streamflowSelectedStationId) params.set("hydroStation", streamflowSelectedStationId);
    }
    if (officialVisibility["usgs-streamflow"] || officialVisibility["nws-radar"]) params.set("live", liveInstrument);
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
    if (mapUtilityView === "compare") params.set("compare", `${compareLeft.id},${compareRight.id}`);
    params.set("times", `${compareTimeA},${compareTimeB}`);
    if (selected) {
      params.set("f", selected.featureId);
      params.set("panel", drawerView);
      params.set("drawer", rightOpen ? "open" : "closed");
      params.set("focusStage", focusStage);
      params.set("focusIntent", focusIntent);
    }
    return params;
  }, [activeLayers, analysisArea, atmospherePreset, basemap, compareLeft.id, compareRight.id, compareTimeA, compareTimeB, currentWorkspace, drawerView, dynamicEffects, fieldOfView, focusIntent, focusStage, gestureMode, layerOrder, lightAzimuth, liveInstrument, locationCameraRedacted, mapEvidenceFilter, mapUtilityOpen, mapUtilityView, measureUnit, movingWindowFrames, noaaRadarFollowLatest, noaaRadarFrameTime, noaaRadarLoopSpan, noaaRadarPlaybackSpeed, officialOpacity, officialVisibility, opacity, playbackDirection, playbackLoopMode, projection, rightOpen, scenePreset, selected, streamflowFrameTime, streamflowPlaybackSpeed, streamflowRange, streamflowSelectedStationId, sweepRangeEnd, sweepRangeStart, temporalMode, temporalStepRule, verticalExaggeration, view, visibleOfficialSources, year]);

  const announce = useCallback((message: string) => {
    setToast(message);
    window.setTimeout(() => setToast(""), 3600);
  }, []);

  const commitTemporalFrame = useCallback((next: number, message?: string) => {
    setSweepRangeStart((current) => Math.min(current, next));
    setSweepRangeEnd((current) => Math.max(current, next));
    yearRef.current = next;
    setYear(next);
    setPreviewYear(next);
    if (temporalMode === "comparison") setCompareTimeB(next);
    if (message) announce(message);
  }, [announce, temporalMode]);

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

  const loadTemporalEventStack = useCallback(() => {
    const eventLayerIds = new Set([
      "historical-context",
      "atmosphere-observations",
      "smoke-context",
      "fire-context",
      "hazards-context",
      "watershed-context",
      "water-context",
      "communities",
    ]);
    const nextVisibility = Object.fromEntries(LAYER_REGISTRY.map((layer) => [
      layer.id,
      visibilityRef.current[layer.id] || eventLayerIds.has(layer.id),
    ]));
    visibilityRef.current = nextVisibility;
    setVisibility(nextVisibility);
    setTemporalMode("event-stepping");
    setTemporalStepRule("available-events");
    setSweepRangeStart(1885);
    setSweepRangeEnd(OFFICIAL_CONTEXT_PRESENT_FRAME);
    setPlaybackDirection("forward");
    setPlaybackLoopMode("stop");
    commitTemporalFrame(1885);
    setPlaying(false);
    announce("Loaded a cross-domain event stack from 1885 to the operational-present frame; all claims remain source-specific");
  }, [announce, commitTemporalFrame]);

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
        officialContextRuntimeVisibility(officialVisibilityRef.current, temporalQueryRef.current.frame, false, null),
        officialOpacityRef.current,
        officialPayloadsRef.current,
      );
      return;
    }
    const previousConfirmedFrame = noaaRadarFrameTimeRef.current;
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
      const onSourceData = (event: MapSourceDataEvent) => {
        if (event.sourceId !== OFFICIAL_CONTEXT_BY_ID["nws-radar"].sourceId || !event.tile || !event.isSourceLoaded) return;
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
        if (state === "ready") {
          noaaRadarFrameTimeRef.current = observedAt;
          noaaRadarReadyRef.current = true;
          setNoaaRadarFrameTime(observedAt);
          setOfficialStates((current) => ({ ...current, "nws-radar": "ready" }));
          setOfficialErrors((current) => ({ ...current, "nws-radar": undefined }));
          applyOfficialContextState(
            map,
            officialContextRuntimeVisibility(officialVisibilityRef.current, temporalQueryRef.current.frame, noaaRadarReadyRef.current, observedAt),
            officialOpacityRef.current,
            officialPayloadsRef.current,
          );
          if (announceChange) announce(`NOAA radar frame ${formatNoaaRadarLocalTime(observedAt)} selected; no interpolation`);
        } else {
          setNoaaRadarPlaying(false);
          noaaRadarReadyRef.current = Boolean(previousConfirmedFrame);
          if (previousConfirmedFrame) {
            try { setNoaaRadarObservationTime(map, previousConfirmedFrame); } catch { noaaRadarReadyRef.current = false; }
          }
          applyOfficialContextState(
            map,
            officialContextRuntimeVisibility(officialVisibilityRef.current, temporalQueryRef.current.frame, noaaRadarReadyRef.current, previousConfirmedFrame),
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
      const sourceUpdate = setNoaaRadarObservationTime(map, observedAt);
      if (sourceUpdate === null) throw new Error("The fixed NOAA raster source could not be initialized.");
      if (previousConfirmedFrame || !officialVisibilityRef.current["nws-radar"] || temporalQueryRef.current.frame !== OFFICIAL_CONTEXT_PRESENT_FRAME) {
        applyOfficialContextState(
          map,
          officialContextRuntimeVisibility(officialVisibilityRef.current, temporalQueryRef.current.frame, noaaRadarReadyRef.current, previousConfirmedFrame),
          officialOpacityRef.current,
          officialPayloadsRef.current,
        );
      }
      if (sourceUpdate === "unchanged" && previousConfirmedFrame === observedAt) window.requestAnimationFrame(() => finish("ready"));
    } catch (error) {
      noaaRadarFrameFailureRef.current?.(error instanceof Error ? error.message : "The NOAA radar frame could not be applied.");
    }
  }, [announce]);

  const refreshNoaaRadarManifest = useCallback(async (quiet = false) => {
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
      const candidate = await response.json() as unknown;
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
          officialContextRuntimeVisibility(officialVisibilityRef.current, temporalQueryRef.current.frame, false, null),
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
  }, [announce, applyNoaaRadarFrame]);

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
    setNoaaRadarFollowLatest(false);
    setNoaaRadarPlaying(true);
    announce(`NOAA radar loop started with ${noaaRadarLoopFrames.length} exact observations and no interpolation`);
  }, [announce, noaaRadarFrameLoadState, noaaRadarLoopFrames.length, noaaRadarPlaying, noaaRadarRenderable, reducedMotion]);

  const refreshStreamflow = useCallback(async (
    requestedRange: HydrologyRange,
    requestedStationId: string | null,
    quiet = false,
  ) => {
    if (temporalQueryRef.current.frame !== OFFICIAL_CONTEXT_PRESENT_FRAME) {
      if (!quiet) announce("River Pulse remains held outside the operational-present atlas frame");
      return;
    }
    if (requestedRange !== "24h" && !requestedStationId) {
      setStreamflowError("Select a USGS station before requesting a longer historical range.");
      if (!quiet) announce("A selected USGS station is required for longer streamflow history");
      return;
    }
    const stationId = requestedStationId ? normalizeUsgsStationId(requestedStationId) : null;
    if (requestedStationId && !stationId) {
      setStreamflowError("The selected USGS station identifier is invalid.");
      return;
    }
    streamflowRequestRef.current?.abort();
    const controller = new AbortController();
    streamflowRequestRef.current = controller;
    const generation = ++streamflowRequestGenerationRef.current;
    setStreamflowPlaying(false);
    setStreamflowState("loading");
    setStreamflowError(null);
    setOfficialStates((current) => ({ ...current, "usgs-streamflow": "loading" }));
    setOfficialErrors((current) => ({ ...current, "usgs-streamflow": undefined }));
    const path = requestedRange === "24h"
      ? "/api/hydrology/streamflow?mode=network&range=24h"
      : `/api/hydrology/streamflow?mode=station&range=${requestedRange}&station=${encodeURIComponent(stationId!)}&parameter=00060`;
    try {
      const response = await fetch(path, { cache: "no-store", headers: { Accept: "application/json" }, signal: controller.signal });
      const candidate = await response.json() as unknown;
      if (!response.ok) {
        const message = candidate && typeof candidate === "object" && ("error" in candidate || "message" in candidate)
          ? String((candidate as { error?: unknown; message?: unknown }).error ?? (candidate as { message?: unknown }).message ?? `HTTP ${response.status}`)
          : `HTTP ${response.status}`;
        throw new Error(message);
      }
      const bundle = parseStreamflowBundle(candidate);
      if (generation !== streamflowRequestGenerationRef.current) return;
      const frames = streamflowDisplayFrames(bundle);
      const requestedTime = streamflowRequestedTimeRef.current;
      const restoredIndex = requestedTime
        ? frames.reduce((matched, frame, index) => Date.parse(frame) <= Date.parse(requestedTime) ? index : matched, -1)
        : -1;
      streamflowRequestedTimeRef.current = null;
      streamflowBundleRef.current = bundle;
      setStreamflowBundle(bundle);
      setStreamflowRange(requestedRange);
      setStreamflowSelectedStationId(stationId);
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

  const refreshNoaaHydrologyNetwork = useCallback(async (quiet = false) => {
    if (temporalQueryRef.current.frame !== OFFICIAL_CONTEXT_PRESENT_FRAME) {
      if (!quiet) announce("NOAA hydrology remains held outside the operational-present atlas frame");
      return;
    }
    noaaHydrologyRequestRef.current?.abort();
    const controller = new AbortController();
    noaaHydrologyRequestRef.current = controller;
    setOfficialStates((current) => ({ ...current, "noaa-nwps-gauges": "loading" }));
    setOfficialErrors((current) => ({ ...current, "noaa-nwps-gauges": undefined }));
    try {
      const response = await fetch(NOAA_HYDROLOGY_NETWORK_API_PATH, { cache: "no-store", headers: { Accept: "application/json" }, signal: controller.signal });
      const candidate = await response.json() as unknown;
      if (!response.ok) throw new Error(`NOAA hydrology adapter returned HTTP ${response.status}.`);
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
    if (!streamflowBundle || !streamflowFrame || !streamflowFrameTime) return;
    const data = {
      type: "FeatureCollection" as const,
      features: streamflowFrame.features.map((feature) => ({
        ...feature,
        properties: {
          ...feature.properties,
          selected: feature.properties.stationId === streamflowSelectedStationId,
          retrievedAt: streamflowBundle.retrievedAt,
        },
      })),
    };
    const payload: OfficialContextPayload = {
      feed: "usgs-streamflow",
      state: streamflowBundle.state,
      retrievedAt: streamflowBundle.retrievedAt,
      upstreamUpdatedAt: streamflowFrameTime,
      featureCount: data.features.length,
      data,
      source: streamflowBundle.source,
      limitation: streamflowBundle.limitation,
      truncated: streamflowBundle.truncated,
    };
    officialPayloadsRef.current = { ...officialPayloadsRef.current, "usgs-streamflow": payload };
    setOfficialPayloads(officialPayloadsRef.current);
  }, [streamflowBundle, streamflowFrame, streamflowFrameTime, streamflowSelectedStationId]);

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
    setStreamflowPlaying(false);
    setStreamflowSelectedStationId(normalized);
    setLiveInstrument("river");
    if (!normalized && streamflowRange !== "24h") {
      setStreamflowRange("24h");
      void refreshStreamflow("24h", null);
      return;
    }
    if (normalized && streamflowRange !== "24h") void refreshStreamflow(streamflowRange, normalized);
  }, [refreshStreamflow, streamflowRange]);

  const refreshOfficialContext = useCallback(async (feed: OfficialContextFeedId) => {
    if (officialRequestsRef.current.has(feed)) return;
    const source = OFFICIAL_CONTEXT_BY_ID[feed];
    officialRequestsRef.current.add(feed);
    setOfficialStates((current) => ({ ...current, [feed]: "loading" }));
    setOfficialErrors((current) => ({ ...current, [feed]: undefined }));
    try {
      const response = await fetch(source.apiPath!, { cache: "no-store", headers: { Accept: "application/json" } });
      const candidate = await response.json() as Partial<OfficialContextPayload> & { error?: string };
      const validState = candidate.state === "ready" || candidate.state === "empty" || candidate.state === "partial";
      if (!response.ok || candidate.feed !== feed || !validState || typeof candidate.featureCount !== "number" || !candidate.data || candidate.data.type !== "FeatureCollection" || !Array.isArray(candidate.data.features)) {
        throw new Error(candidate.error ?? `Fixed source adapter returned HTTP ${response.status}.`);
      }
      const payload = candidate as OfficialContextPayload;
      officialPayloadsRef.current = { ...officialPayloadsRef.current, [feed]: payload };
      setOfficialPayloads(officialPayloadsRef.current);
      setOfficialStates((current) => ({ ...current, [feed]: payload.state }));
      const map = mapRef.current;
      if (map && styleGenerationReadyRef.current) applyOfficialContextState(map, officialContextRuntimeVisibility(officialVisibilityRef.current, temporalQueryRef.current.frame, noaaRadarReadyRef.current, noaaRadarFrameTimeRef.current), officialOpacityRef.current, officialPayloadsRef.current);
      announce(payload.featureCount === 0
        ? `${source.shortTitle}: zero mapped features at ${new Date(payload.retrievedAt).toLocaleTimeString()}—not an all-clear`
        : `${source.shortTitle}: ${payload.featureCount} official context features refreshed`);
    } catch (error) {
      const message = error instanceof Error ? error.message : "Official context request failed.";
      setOfficialStates((current) => ({ ...current, [feed]: "error" }));
      setOfficialErrors((current) => ({ ...current, [feed]: message }));
      announce(`${source.shortTitle} unavailable; no fallback inference was used`);
    } finally {
      officialRequestsRef.current.delete(feed);
    }
  }, [announce]);

  const setOfficialContextVisible = useCallback((id: OfficialContextId, visible: boolean) => {
    if (id === "nws-radar" && visible) {
      noaaRadarReadyRef.current = Boolean(
        noaaRadarFrameTimeRef.current
        && noaaRadarManifestIsFresh(noaaRadarManifestRef.current, Date.now()),
      );
      setNoaaRadarClock(Date.now());
      setLiveInstrument("radar");
    }
    if (id === "usgs-streamflow" && visible) setLiveInstrument("river");
    const next = { ...officialVisibilityRef.current, [id]: visible };
    officialVisibilityRef.current = next;
    setOfficialVisibility(next);
    const source = OFFICIAL_CONTEXT_BY_ID[id];
    if (source.apiPath && visible && !officialPayloadsRef.current[id as OfficialContextFeedId]) void refreshOfficialContext(id as OfficialContextFeedId);
    if (id === "usgs-streamflow" && visible && !streamflowBundleRef.current) void refreshStreamflow(streamflowRange, streamflowSelectedStationId);
    if (id === "noaa-nwps-gauges" && visible && !officialPayloadsRef.current["noaa-nwps-gauges"]) void refreshNoaaHydrologyNetwork();
    if (id === "nws-radar" && visible && temporalQueryRef.current.frame === OFFICIAL_CONTEXT_PRESENT_FRAME) void refreshNoaaRadarManifest();
    if (id === "nws-radar" && !visible) setNoaaRadarPlaying(false);
    if (id === "usgs-streamflow" && !visible) setStreamflowPlaying(false);
    const map = mapRef.current;
    if (map && styleGenerationReadyRef.current) {
      try {
        applyOfficialContextState(map, officialContextRuntimeVisibility(next, temporalQueryRef.current.frame, noaaRadarReadyRef.current, noaaRadarFrameTimeRef.current), officialOpacityRef.current, officialPayloadsRef.current);
        if (visible && !source.apiPath && !source.managedAdapterPath && id !== "nws-radar" && !officialRasterFailuresRef.current.has(id)) setOfficialStates((current) => ({ ...current, [id]: "loading" }));
      } catch (error) {
        setOfficialStates((current) => ({ ...current, [id]: "error" }));
        setOfficialErrors((current) => ({ ...current, [id]: error instanceof Error ? error.message : "Raster context could not be applied." }));
      }
    }
  }, [refreshNoaaHydrologyNetwork, refreshNoaaRadarManifest, refreshOfficialContext, refreshStreamflow, streamflowRange, streamflowSelectedStationId]);

  const retryOfficialLayer = (id: OfficialContextId) => {
    const source = OFFICIAL_CONTEXT_BY_ID[id];
    if (source.apiPath) { void refreshOfficialContext(id as OfficialContextFeedId); return; }
    if (id === "usgs-streamflow") { void refreshStreamflow(streamflowRange, streamflowSelectedStationId); return; }
    if (id === "noaa-nwps-gauges") { void refreshNoaaHydrologyNetwork(); return; }
    if (id === "nws-radar") { void refreshNoaaRadarManifest(); return; }
    const map = mapRef.current;
    if (!map || !styleGenerationReadyRef.current) return;
    officialRasterFailuresRef.current.delete(id);
    setOfficialErrors(current => ({ ...current, [id]: undefined }));
    setOfficialStates(current => ({ ...current, [id]: "loading" }));
    if (map.getSource(source.sourceId)) map.refreshTiles(source.sourceId);
    else setOfficialContextVisible(id, true);
    announce(`Retrying ${source.shortTitle}`);
  };

  const setPriorityContextGroupVisible = useCallback((sourceIds: readonly OfficialContextId[], visible: boolean) => {
    sourceIds.forEach((sourceId) => setOfficialContextVisible(sourceId, visible));
    announce(`${visible ? "Showing" : "Hiding"} ${sourceIds.length} connected context layers`);
  }, [announce, setOfficialContextVisible]);

  const setOfficialContextOpacity = useCallback((id: OfficialContextId, value: number) => {
    const next = { ...officialOpacityRef.current, [id]: clamp(value, 0, 1) };
    officialOpacityRef.current = next;
    setOfficialOpacity(next);
    const map = mapRef.current;
    if (map && styleGenerationReadyRef.current) applyOfficialContextState(map, officialContextRuntimeVisibility(officialVisibilityRef.current, temporalQueryRef.current.frame, noaaRadarReadyRef.current, noaaRadarFrameTimeRef.current), next, officialPayloadsRef.current);
  }, []);

  const refreshVisibleOfficialContext = useCallback(() => {
    const feeds = OFFICIAL_CONTEXT_SOURCES.filter((source) => source.apiPath && officialVisibilityRef.current[source.id]);
    const radarSelected = officialVisibilityRef.current["nws-radar"];
    const radarRefreshable = radarSelected && temporalQueryRef.current.frame === OFFICIAL_CONTEXT_PRESENT_FRAME;
    const streamflowRefreshable = officialVisibilityRef.current["usgs-streamflow"] && temporalQueryRef.current.frame === OFFICIAL_CONTEXT_PRESENT_FRAME;
    const noaaHydrologyRefreshable = officialVisibilityRef.current["noaa-nwps-gauges"] && temporalQueryRef.current.frame === OFFICIAL_CONTEXT_PRESENT_FRAME;
    if (feeds.length === 0 && !radarSelected && !streamflowRefreshable && !noaaHydrologyRefreshable) {
      announce("Turn on an official data layer before refreshing");
      return;
    }
    feeds.forEach((source) => { void refreshOfficialContext(source.id as OfficialContextFeedId); });
    if (radarRefreshable) void refreshNoaaRadarManifest(true);
    if (streamflowRefreshable) void refreshStreamflow(streamflowRange, streamflowSelectedStationId, true);
    if (noaaHydrologyRefreshable) void refreshNoaaHydrologyNetwork(true);
    const connectionCount = feeds.length + (radarRefreshable ? 1 : 0) + (streamflowRefreshable ? 1 : 0) + (noaaHydrologyRefreshable ? 1 : 0);
    if (connectionCount === 0) {
      announce("NOAA radar remains held outside Present; no visible official connection was refreshed");
      return;
    }
    announce(`Refreshing ${connectionCount} visible official connection${connectionCount === 1 ? "" : "s"}`);
  }, [announce, refreshNoaaHydrologyNetwork, refreshNoaaRadarManifest, refreshOfficialContext, refreshStreamflow, streamflowRange, streamflowSelectedStationId]);

  const hideAllOfficialContext = useCallback(() => {
    const next = Object.fromEntries(OFFICIAL_CONTEXT_SOURCES.map((source) => [source.id, false])) as Record<OfficialContextId, boolean>;
    officialVisibilityRef.current = next;
    setOfficialVisibility(next);
    setNoaaRadarPlaying(false);
    setStreamflowPlaying(false);
    const map = mapRef.current;
    if (map && styleGenerationReadyRef.current) applyOfficialContextState(map, officialContextRuntimeVisibility(next, temporalQueryRef.current.frame, noaaRadarReadyRef.current, noaaRadarFrameTimeRef.current), officialOpacityRef.current, officialPayloadsRef.current);
    announce("Official context hidden; loaded snapshots remain available on this page");
  }, [announce]);

  useEffect(() => {
    const refresh = () => {
      const day = currentUtcDay();
      setBaselineDay(day);
      if (document.hidden || temporalQueryRef.current.frame !== OFFICIAL_CONTEXT_PRESENT_FRAME) return;
      for (const source of OFFICIAL_CONTEXT_SOURCES) {
        if (source.apiPath && officialVisibilityRef.current[source.id]) void refreshOfficialContext(source.id as OfficialContextFeedId);
      }
    };
    const timer = window.setInterval(refresh, 300_000);
    const visible = () => { if (!document.hidden) refresh(); };
    document.addEventListener("visibilitychange", visible);
    return () => { clearInterval(timer); document.removeEventListener("visibilitychange", visible); };
  }, [refreshOfficialContext]);

  useEffect(() => {
    const timer = window.setTimeout(() => {
      for (const source of OFFICIAL_CONTEXT_SOURCES) {
        if (source.apiPath && officialVisibilityRef.current[source.id]) void refreshOfficialContext(source.id as OfficialContextFeedId);
      }
      if (officialVisibilityRef.current["usgs-streamflow"] && !streamflowRequestRef.current && !streamflowBundleRef.current) void refreshStreamflow("24h", null, true);
      if (officialVisibilityRef.current["noaa-nwps-gauges"]) void refreshNoaaHydrologyNetwork(true);
    }, 40);
    return () => window.clearTimeout(timer);
  }, [refreshNoaaHydrologyNetwork, refreshOfficialContext, refreshStreamflow]);

  const dismissMapUtilityWithoutFocus = useCallback(() => {
    mapUtilityReturnRef.current = null;
    setMapUtilityOpen(false);
    setMapQueryCandidates([]);
  }, []);

  const openQwenCompanion = useCallback(() => {
    setQwenOpen(true);
    setHelpOpen(false);
    setGuidedStartOpen(false);
    setToolsExpanded(false);
    dismissMapUtilityWithoutFocus();
    if (isCompact) {
      setLeftOpen(false);
      setRightOpen(false);
      setTimelineOpen(false);
    }
  }, [dismissMapUtilityWithoutFocus, isCompact]);

  const closeQwenCompanion = useCallback(() => {
    setQwenOpen(false);
    window.setTimeout(() => mapContainerRef.current?.focus(), 0);
  }, []);

  const copyQwenPrompt = useCallback(async () => {
    try {
      await navigator.clipboard.writeText(qwenPrompt);
      announce("Map-grounded Qwen prompt copied with no public effect");
    } catch {
      announce("Clipboard access was blocked; the Qwen prompt stayed in the browser");
    }
  }, [announce, qwenPrompt]);

  const askQwen = useCallback(async () => {
    const question = qwenQuestion.trim().slice(0, 1200);
    if (!question || qwenBusy) return;
    setQwenBusy(true);
    setQwenMessages((current) => [...current, { role: "user" as const, content: question }].slice(-8));
    setQwenQuestion("");
    try {
      const response = await fetch("/api/qwen", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({ question, context: qwenContext }),
      });
      const payload = await response.json().catch(() => null) as { status?: string; answer?: string; message?: string } | null;
      if (!response.ok || payload?.status !== "ok" || !payload.answer) {
        const notConfigured = payload?.status === "not_configured";
        setQwenBridgeState(notConfigured ? "not-configured" : "error");
        setQwenMessages((current) => [...current, {
          role: "assistant" as const,
          content: notConfigured
            ? "No Qwen inference endpoint is connected to this Site. Copy the grounded prompt below into your local Qwen/Ollama session; the map, time, layers, and evidence boundary are already included."
            : payload?.message ?? "Qwen could not answer from the current map context.",
        }].slice(-8));
        return;
      }
      setQwenBridgeState("ready");
      setQwenMessages((current) => [...current, { role: "assistant" as const, content: payload.answer! }].slice(-8));
    } catch {
      setQwenBridgeState("error");
      setQwenMessages((current) => [...current, {
        role: "assistant" as const,
        content: "The Qwen bridge could not be reached. The map remains fully usable, and the grounded prompt can still be copied for local inference.",
      }].slice(-8));
    } finally {
      setQwenBusy(false);
    }
  }, [qwenBusy, qwenContext, qwenQuestion]);

  const stopSceneOrbit = useCallback((notify = true) => {
    if (sceneOrbitTimerRef.current !== null) {
      window.clearTimeout(sceneOrbitTimerRef.current);
      sceneOrbitTimerRef.current = null;
    }
    mapRef.current?.stop();
    setSceneOrbiting(false);
    if (notify) announce("3D orbit stopped at the current camera");
  }, [announce]);

  const showComparedLayers = useCallback(() => {
    setVisibility((current) => ({ ...current, [compareLeft.id]: true, [compareRight.id]: true }));
    announce(`Showing ${compareLeft.title} and ${compareRight.title}; other visible layers were preserved`);
  }, [announce, compareLeft, compareRight]);

  const fitComparedLayers = useCallback(() => {
    const bounds: [number, number, number, number] = [
      Math.min(compareLeft.bounds[0], compareRight.bounds[0]),
      Math.min(compareLeft.bounds[1], compareRight.bounds[1]),
      Math.max(compareLeft.bounds[2], compareRight.bounds[2]),
      Math.max(compareLeft.bounds[3], compareRight.bounds[3]),
    ];
    setVisibility((current) => ({ ...current, [compareLeft.id]: true, [compareRight.id]: true }));
    mapRef.current?.fitBounds([[bounds[0], bounds[1]], [bounds[2], bounds[3]]], { padding: 70, maxZoom: 9, duration: motionDuration(650) });
    announce("Fitted both comparison layers; camera and visibility changed only in this browser");
  }, [announce, compareLeft, compareRight]);

  const copyLayerComparison = useCallback(async () => {
    const summarize = (layer: LayerRecord) => ({
      id: layer.id,
      title: layer.title,
      domain: layer.domain,
      geometry: layer.geometryType,
      valid_time: layer.validTimeExtent,
      source_time: layer.sourceTime,
      release_time: layer.releaseTime,
      freshness: layer.freshnessState,
      release_state: layer.releaseState,
      public_status: layer.publicStatus,
      evidence_reference: layer.evidenceReference,
      visible: Boolean(visibility[layer.id]),
    });
    const comparison = {
      format: "kfm-site-layer-comparison-v1",
      authority: "SITE_LOCAL_READ_ONLY_PROJECTION",
      active_time: year,
      layers: [summarize(compareLeft), summarize(compareRight)],
      effects: { evidence: "NONE", policy: "NONE", review: "NONE", release: "NONE", publication: "NONE" },
      limitation: "Metadata comparison does not prove equivalence, compatibility, source admission, or publication readiness.",
    };
    try {
      await navigator.clipboard.writeText(JSON.stringify(comparison, null, 2));
      announce("Read-only layer comparison copied with no public effect");
    } catch {
      announce("Clipboard access was blocked; comparison stayed in the browser");
    }
  }, [announce, compareLeft, compareRight, visibility, year]);

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
    window.setTimeout(() => repositoryButtonRef.current?.focus(), 0);
  }, [rightOpen]);

  const closeRightPanel = useCallback(() => {
    setRightOpen(false);
    setCurrentWorkspace("explore");
    popupRef.current?.remove();
    const returnTarget = returnFocusRef.current;
    returnFocusRef.current = null;
    window.setTimeout(() => {
      const targetIsUsable = returnTarget?.isConnected && !returnTarget.closest("[inert]");
      (targetIsUsable ? returnTarget : mapContainerRef.current)?.focus();
    }, 0);
  }, []);

  const closeLeftPanel = useCallback(() => {
    setLeftOpen(false);
    setCurrentWorkspace("explore");
    window.setTimeout(() => mapContainerRef.current?.focus(), 0);
  }, []);

  const closeTimelinePanel = useCallback(() => {
    setTimelineOpen(false);
    setPlaying(false);
    window.setTimeout(() => mapContainerRef.current?.focus(), 0);
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
  }, []);

  const openMapUtility = useCallback((nextView: MapUtilityView, returnElement?: HTMLElement | null) => {
    mapUtilityReturnRef.current = returnElement ?? null;
    setMapUtilityView(nextView);
    setMapUtilityOpen(true);
    setCurrentWorkspace("explore");
    if (nextView === "export") setExportGeneratedAt(new Date().toISOString());
    if (nextView === "report") setReportGeneratedAt(new Date().toISOString());
    setToolsExpanded(false);
    setHelpOpen(false);
    setMapContextOpen(false);
    if (isCompact) {
      setLeftOpen(false);
      setRightOpen(false);
      setTimelineOpen(false);
    }
    window.setTimeout(() => mapUtilityPanelRef.current?.querySelector<HTMLElement>("button:not([disabled])")?.focus(), 0);
  }, [isCompact]);

  const openAtlasPanel = useCallback((mode: LeftPanelMode) => {
    setMapContextOpen(false);
    setCurrentWorkspace("knowledge");
    setLeftPanelMode(mode);
    setLeftOpen(true);
    setRightOpen(false);
    dismissMapUtilityWithoutFocus();
    if (isCompact) setTimelineOpen(false);
  }, [dismissMapUtilityWithoutFocus, isCompact]);

  const openLiveContextCatalog = useCallback(() => {
    openAtlasPanel("layers");
    announce("Opened live operational context controls");
    window.setTimeout(() => {
      document.getElementById("official-context-catalog")?.scrollIntoView({
        behavior: reducedMotion ? "auto" : "smooth",
        block: "start",
      });
    }, 0);
  }, [announce, openAtlasPanel, reducedMotion]);

  const activateMapUtilityView = useCallback((nextView: MapUtilityView, focusTab = false) => {
    setMapUtilityView(nextView);
    if (nextView === "export") setExportGeneratedAt(new Date().toISOString());
    if (nextView === "report") setReportGeneratedAt(new Date().toISOString());
    if (focusTab) {
      const nextIndex = mapUtilityViews.indexOf(nextView);
      window.setTimeout(() => mapUtilityTabRefs.current[nextIndex]?.focus(), 0);
    }
  }, []);

  const handleMapUtilityTabKeyDown = useCallback((event: React.KeyboardEvent<HTMLButtonElement>, index: number) => {
    let nextIndex: number | null = null;
    if (event.key === "ArrowRight" || event.key === "ArrowDown") nextIndex = (index + 1) % mapUtilityViews.length;
    if (event.key === "ArrowLeft" || event.key === "ArrowUp") nextIndex = (index - 1 + mapUtilityViews.length) % mapUtilityViews.length;
    if (event.key === "Home") nextIndex = 0;
    if (event.key === "End") nextIndex = mapUtilityViews.length - 1;
    if (nextIndex === null) return;
    event.preventDefault();
    activateMapUtilityView(mapUtilityViews[nextIndex], true);
  }, [activateMapUtilityView]);

  useEffect(() => {
    const handleWorkspaceShortcut = (event: KeyboardEvent) => {
      if (event.defaultPrevented || event.metaKey || event.ctrlKey || event.altKey) return;
      const target = event.target as HTMLElement | null;
      const isEditing = target?.matches("input, textarea, select, [contenteditable='true']");
      if (event.key === "/" && !isEditing) {
        event.preventDefault();
        globalSearchInputRef.current?.focus();
        return;
      }
      if (isEditing) return;
      if (event.key.toLowerCase() === "r") {
        event.preventDefault();
        openMapUtility("report");
      }
      if (event.key.toLowerCase() === "l") {
        event.preventDefault();
        dismissMapUtilityWithoutFocus();
        setLeftPanelMode("layers");
        setLeftOpen((current) => !current);
        if (isCompact) { setRightOpen(false); setTimelineOpen(false); }
      }
    };
    document.addEventListener("keydown", handleWorkspaceShortcut);
    return () => document.removeEventListener("keydown", handleWorkspaceShortcut);
  }, [dismissMapUtilityWithoutFocus, isCompact, openMapUtility]);

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
    returnFocusRef.current = returnElement ?? null;
    mapUtilityReturnRef.current = null;
    setMapUtilityOpen(false);
    setMapQueryCandidates([]);
    setFocusStage("outcome");
    setFocusIntent("explain");
    setPendingFocusAction(null);
    selectedRef.current = context;
    setSelected(context);
    setDrawerView("evidence");
    setRightOpen(true);
    setCurrentWorkspace("trust");
    if (isCompact) {
      setLeftOpen(false);
      setTimelineOpen(false);
    }
  }, [isCompact]);
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

  const openGuidedExample = useCallback((example: (typeof GUIDED_EXAMPLES)[number]) => {
    setTemporalMode("snapshot");
    commitTemporalFrame(example.year);
    setPlaying(false);
    setLeftOpen(false);
    setTimelineOpen(false);
    dismissGuidedStart();
    selectStoredFeature(example.layerId, example.featureId);
    announce(`Opened ${example.title} guided example at ${example.year}`);
  }, [announce, commitTemporalFrame, dismissGuidedStart, selectStoredFeature]);

  const openStoryStep = useCallback((requestedIndex: number) => {
    const nextIndex = Math.max(0, Math.min(KFM_STORY_TRAIL.length - 1, requestedIndex));
    const step = KFM_STORY_TRAIL[nextIndex];
    setStoryStepIndex(nextIndex);
    setStoryOpen(true);
    setGuidedStartOpen(false);
    setHelpOpen(false);
    setPlaying(false);
    setTemporalMode("snapshot");
    commitTemporalFrame(step.year);
    setLeftOpen(false);
    setTimelineOpen(false);
    selectStoredFeature(step.layerId, step.featureId);
    announce(`Story step ${nextIndex + 1} of ${KFM_STORY_TRAIL.length}: ${step.eyebrow}`);
  }, [announce, commitTemporalFrame, selectStoredFeature]);

  const startStoryTrail = useCallback(() => {
    setMapContextOpen(false);
    openStoryStep(0);
  }, [openStoryStep]);

  const closeStoryTrail = useCallback(() => {
    setStoryOpen(false);
    announce("Guided story closed; the current map selection was preserved");
  }, [announce]);

  const captureMapSnapshot = useCallback((): MapSnapshot => {
    const createdAt = new Date().toISOString();
    const representation: MapSnapshot["representation"] = mapUtilityOpen && mapUtilityView === "compare"
      ? "Compare"
      : scenePreset === "elevation-3d"
        ? "Terrain 3D"
        : projection === "globe"
          ? "Globe"
          : "2D";
    const redactCamera = locationCameraRedacted;
    const capturedSelection = selected && !selectedTimeMismatch ? selected : null;
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
      projection,
      basemap,
      evidenceFilter: mapEvidenceFilter,
      comparison: representation === "Compare" ? { layerA: compareLeftId, layerB: compareRightId, timeA: compareTimeA, timeB: compareTimeB } : undefined,
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
          : { start: temporalQuery.frame, end: temporalQuery.frame, label: `${formatTimelineStep(temporalQuery.frame)} · ${timelineEraLabel(temporalQuery.frame)}`, mode: "instant" },
      visibleLayers: layerOrder
        .filter((layerId) => visibility[layerId])
        .map((layerId, order) => {
          const layer = LAYER_REGISTRY.find((candidate) => candidate.id === layerId)!;
          return { id: layer.id, title: layer.title, domain: layer.domain, order, opacity: opacity[layer.id] ?? layer.defaultOpacity, trustState: trustStateForLayer(layer) };
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
      policy: policyDecisionFromEvidenceState(selected?.properties.evidenceState),
    };
  }, [analysisArea, basemap, compareTimeA, compareTimeB, layerOrder, locationCameraRedacted, mapContextRecords, mapEvidenceFilter, compareLeftId, compareRightId, mapUtilityOpen, mapUtilityView, mapViewportBounds, movingWindowFrames, opacity, projection, scenePreset, selected, selectedTimeMismatch, supportedMapContextCount, temporalMode, temporalQuery, temporalStepRule, view, visibility]);

  const comparisonSnapshot = useMemo(() => captureMapSnapshot(), [captureMapSnapshot]);

  const openPrimaryWorkspace = useCallback((mode: Exclude<PrimaryWorkspace, "map">, freshFromMap = false) => {
    if (freshFromMap || !workspaceSnapshot) setWorkspaceSnapshot(freshFromMap ? captureMapSnapshot() : readDraftSnapshot(mode) ?? captureMapSnapshot());
    setPrimaryWorkspace(mode);
    setMapContextOpen(false);
    setHelpOpen(false);
    setQwenOpen(false);
    setToolsExpanded(false);
    announce(`${mode === "reports" ? "Report" : "Story"} workspace opened from the current governed map state`);
  }, [announce, captureMapSnapshot, workspaceSnapshot]);

  const returnToPrimaryMap = useCallback(() => {
    setPrimaryWorkspace("map");
    window.setTimeout(() => mapContainerRef.current?.focus(), 0);
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
    setTemporalStepRule(snapshotSweep?.stepRule ?? "available-events");
    setSweepRangeStart(snapshotSweep?.rangeStart ?? Math.min(snapshot.committedTime.start, sceneFrame));
    setSweepRangeEnd(snapshotSweep?.rangeEnd ?? Math.max(snapshot.committedTime.end, sceneFrame));
    setMovingWindowFrames(snapshotSweep?.windowFrames ?? 3);
    setProjection(snapshot.projection);
    setBasemap(snapshotBasemap);
    setAnalysisArea(snapshot.area.kind === "aoi" && snapshot.area.bounds ? { ...snapshot.area.bounds } : null);
    setScenePreset(snapshot.representation === "Terrain 3D" ? "elevation-3d" : snapshot.projection === "globe" ? "globe-overview" : "overview-2d");
    setMapEvidenceFilter(snapshot.evidenceFilter ?? "ALL");
    mapEvidenceFilterRef.current = snapshot.evidenceFilter ?? "ALL";
    setCompareTimeA(snapshot.comparison?.timeA ?? snapshot.committedTime.start);
    setCompareTimeB(snapshot.comparison?.timeB ?? sceneFrame);
    if (snapshot.comparison) { setCompareLeftId(snapshot.comparison.layerA); setCompareRightId(snapshot.comparison.layerB); }
    setMapUtilityView(snapshot.representation === "Compare" ? "compare" : "navigate");
    setMapUtilityOpen(snapshot.representation === "Compare");
    setPrimaryWorkspace("map");
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
    const context = sceneSelection ? copyFeature(LAYER_REGISTRY.find((layer) => layer.id === sceneSelection.layerId)!, sceneSelection.featureId) : null;
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
    popupRef.current?.remove();
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
      const params = new URLSearchParams(window.location.search);
      const centerParam = params.get("c")?.split(",").map((token) => token.trim() === "" ? Number.NaN : Number(token));
      const center: [number, number] = centerParam?.length === 2 && centerParam.every(Number.isFinite)
        ? [clamp(centerParam[0], -104.8, -92), clamp(centerParam[1], 34.8, 42.2)]
        : KANSAS_VIEW.center;
      const restoredView: ViewState = {
        center,
        zoom: clamp(parseNumber(params.get("z"), KANSAS_VIEW.zoom), 4, 16),
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
      const restoredOfficialIds = params.get("ctx")?.split(",").filter((id): id is OfficialContextId => knownOfficialIds.has(id as OfficialContextId)) ?? [];
      const nextOfficialVisibility = params.has("ctx")
        ? Object.fromEntries(OFFICIAL_CONTEXT_SOURCES.map((source) => [source.id, restoredOfficialIds.includes(source.id)])) as Record<OfficialContextId, boolean>
        : defaultOfficialVisibility;
      officialVisibilityRef.current = nextOfficialVisibility;
      setOfficialVisibility(nextOfficialVisibility);
      const officialOpacityPairs = params.get("ctxo")?.split(",").map((pair) => pair.split(":")) ?? [];
      const restoredOfficialOpacity = Object.fromEntries(officialOpacityPairs
        .filter(([id, value]) => knownOfficialIds.has(id as OfficialContextId) && typeof value === "string" && value.trim() !== "" && Number.isFinite(Number(value)))
        .map(([id, value]) => [id, clamp(Number(value), 0, 1)]));
      const nextOfficialOpacity = { ...defaultOfficialOpacity, ...restoredOfficialOpacity };
      officialOpacityRef.current = nextOfficialOpacity;
      setOfficialOpacity(nextOfficialOpacity);
      const restoredRadarSpan = Number(params.get("radarSpan"));
      setNoaaRadarLoopSpan(restoredRadarSpan === 30 || restoredRadarSpan === 120 ? restoredRadarSpan : 60);
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
      const restoredHydroRange: HydrologyRange = candidateHydroRange !== "24h" && !normalizedHydroStation ? "24h" : candidateHydroRange;
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
      setLiveInstrument(restoredLiveInstrument === "radar" ? "radar" : "river");
      for (const source of OFFICIAL_CONTEXT_SOURCES) {
        if (nextOfficialVisibility[source.id] && source.apiPath && !officialPayloadsRef.current[source.id as OfficialContextFeedId]) void refreshOfficialContext(source.id as OfficialContextFeedId);
      }
      const restoredYear = Number(params.get("t"));
      const nextYear = KNOWN_TEMPORAL_FRAMES.has(restoredYear) ? restoredYear : 2026;
      yearRef.current = nextYear;
      setYear(nextYear);
      setPreviewYear(nextYear);
      if (nextOfficialVisibility["nws-radar"] && nextYear === OFFICIAL_CONTEXT_PRESENT_FRAME) void refreshNoaaRadarManifest(true);
      if (nextOfficialVisibility["usgs-streamflow"] && nextYear === OFFICIAL_CONTEXT_PRESENT_FRAME) void refreshStreamflow(restoredHydroRange, normalizedHydroStation, true);
      if (nextOfficialVisibility["noaa-nwps-gauges"] && nextYear === OFFICIAL_CONTEXT_PRESENT_FRAME) void refreshNoaaHydrologyNetwork(true);
      const restoredTemporalMode = params.get("tm");
      const nextTemporalMode: TemporalSweepMode = restoredTemporalMode === "moving-window" || restoredTemporalMode === "event-stepping" || restoredTemporalMode === "accumulation" || restoredTemporalMode === "comparison" ? restoredTemporalMode : "snapshot";
      setTemporalMode(nextTemporalMode);
      setTemporalStepRule(params.get("tstep") === "regular-calendar" ? "regular-calendar" : "available-events");
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
      const nextBasemap: BasemapKey = restoredBasemap === "standard" || restoredBasemap === "imagery" || restoredBasemap === "midnight" || restoredBasemap === "prairie" || restoredBasemap === "streets" || restoredBasemap === "topo" ? restoredBasemap : "standard";
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
      const nextVerticalExaggeration = clamp(parseNumber(params.get("zscale"), 1), 0, 2);
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
      const nextFieldOfView = clamp(parseNumber(params.get("fov"), nextScenePreset === "elevation-3d" ? 44 : 36), 20, 60);
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
      const nextMapUtilityView: MapUtilityView = nextTemporalMode === "comparison"
        ? "compare"
        : restoredMapUtilityView === "report" || restoredMapUtilityView === "inspect" || restoredMapUtilityView === "places" || restoredMapUtilityView === "scene" || restoredMapUtilityView === "connections" || restoredMapUtilityView === "import" || restoredMapUtilityView === "compare" || restoredMapUtilityView === "display" || restoredMapUtilityView === "measure" || restoredMapUtilityView === "export" || restoredMapUtilityView === "diagnostics" ? restoredMapUtilityView : "navigate";
      setMapUtilityView(nextMapUtilityView);
      const restoredCompareIds = params.get("compare")?.split(",") ?? [];
      if (restoredCompareIds.length === 2 && restoredCompareIds.every((id) => knownLayerIds.has(id)) && restoredCompareIds[0] !== restoredCompareIds[1]) {
        setCompareLeftId(restoredCompareIds[0]);
        setCompareRightId(restoredCompareIds[1]);
      }
      const restoredComparisonTimes = params.get("times")?.split(",").map(Number) ?? [];
      if (restoredComparisonTimes.length === 2 && restoredComparisonTimes.every((value) => TIME_STEPS.includes(value as (typeof TIME_STEPS)[number]))) {
        setCompareTimeA(restoredComparisonTimes[0]);
        setCompareTimeB(restoredComparisonTimes[1]);
      } else {
        setCompareTimeA(1910);
        setCompareTimeB(2026);
      }
      if (nextMapUtilityView === "export") setExportGeneratedAt(new Date().toISOString());
      if (nextMapUtilityView === "report") setReportGeneratedAt(new Date().toISOString());
      const restoredMapUtilityOpen = nextTemporalMode === "comparison" || params.get("mapui") === "open";
      setMapUtilityOpen(restoredMapUtilityOpen);
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
  }, [refreshNoaaHydrologyNetwork, refreshNoaaRadarManifest, refreshOfficialContext, refreshStreamflow]);

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
    const mapContainer = mapContainerRef.current;
    if (!mapContainer) return;

    loadConfiguredMapLibre().then(({ maplibregl, version }) => {
      if (disposed || !mapContainerRef.current) return;
      setMaplibreProbe((current) => ({ ...current, version, workerConfigured: true, runtimeAssetsReady: true, error: null }));
      try {
        const webgl2 = document.createElement("canvas").getContext("webgl2");
        setMaplibreProbe((current) => ({ ...current, webgl2: Boolean(webgl2) }));
        if (!webgl2) {
          setSourceStates(Object.fromEntries(LAYER_REGISTRY.map((layer) => [layer.id, "error"])));
          setMaplibreProbe((current) => ({ ...current, error: "WebGL2 is unavailable" }));
          setRuntime({ kind: "unsupported", message: "WebGL2 is unavailable in this browser. The Layer Catalog and trust metadata remain readable, but the interactive map cannot start." });
          return;
        }
        webgl2.getExtension("WEBGL_lose_context")?.loseContext();
        const initialView = pendingViewRef.current ?? KANSAS_VIEW;
        const renderBudget = browserRenderBudget();
        const map = new maplibregl.Map({
          container: mapContainerRef.current,
          style: BASEMAPS[basemapRef.current].style,
          center: initialView.center,
          zoom: initialView.zoom,
          bearing: initialView.bearing,
          pitch: initialView.pitch,
          pixelRatio: renderBudget.pixelRatio,
          maxTileCacheSize: renderBudget.tileCache,
          maxPitch: 60,
          renderWorldCopies: false,
          minZoom: 4,
          maxZoom: 16,
          maxBounds: [[-104.8, 34.8], [-92.0, 42.2]],
          attributionControl: { compact: true },
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
        setMaplibreProbe((current) => ({ ...current, mapConstructed: true }));
        const scaleControl = new maplibregl.ScaleControl({ unit: measureUnitRef.current, maxWidth: 110 });
        scaleControlRef.current = scaleControl;
        map.addControl(scaleControl, "bottom-left");
        const navigationControl = new maplibregl.NavigationControl({ showCompass: true, showZoom: true, visualizePitch: true });
        const fullscreenControl = new maplibregl.FullscreenControl();
        const geolocateControl = new maplibregl.GeolocateControl({
          positionOptions: { enableHighAccuracy: false },
          trackUserLocation: false,
        });
        map.addControl(navigationControl, "top-right");
        map.addControl(fullscreenControl, "top-right");
        map.addControl(geolocateControl, "top-right");
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
          const nextSourceStates = Object.fromEntries(LAYER_REGISTRY.map((layer) => {
            const sourceReady = Boolean(map.getSource(layer.sourceId)) && map.isSourceLoaded(layer.sourceId);
            return [layer.id, sourceReady ? "ready" : failedSourceIds.has(layer.sourceId) ? "error" : "loading"];
          })) as Record<string, "loading" | "ready" | "error">;
          const sourcesReady = Object.values(nextSourceStates).filter((state) => state === "ready").length;
          const styleLoaded = Boolean(map.isStyleLoaded());
          const canvasBounds = map.getCanvas().getBoundingClientRect();
          const canvasReady = canvasBounds.width > 0 && canvasBounds.height > 0 && map.getCanvas().width > 0 && map.getCanvas().height > 0;
          const projectionType = map.getProjection().type === "globe" ? "globe" : "mercator";
          const interactionsReady = interactionHandlersBound
            && map.dragPan.isEnabled()
            && map.scrollZoom.isEnabled()
            && map.keyboard.isEnabled()
            && map.touchZoomRotate.isEnabled();
          const nextProbe = {
            styleLoaded,
            canvasReady,
            idle: map.loaded(),
            tilesLoaded: map.areTilesLoaded(),
            controlsReady: nativeControlsBound && Boolean(scaleControlRef.current),
            interactionsReady,
            sourcesReady,
            projection: projectionType,
            error: runtimeError,
          } satisfies Partial<MapLibreRuntimeProbe>;
          setSourceStates(nextSourceStates);
          setStyleReady(styleLoaded);
          setMaplibreProbe((current) => ({ ...current, ...nextProbe }));
          return nextProbe;
        };

        const syncStyle = () => {
          styleGenerationReadyRef.current = true;
          hoveredRef.current = null;
          map.getCanvas().style.cursor = "";
          applyRegistryState(map, visibilityRef.current, opacityRef.current, yearRef.current, orderRef.current, mapEvidenceFilterRef.current, temporalQueryRef.current);
          noaaRadarReadyRef.current = Boolean(
            noaaRadarFrameTimeRef.current
            && noaaRadarManifestIsFresh(noaaRadarManifestRef.current, Date.now()),
          );
          applyOfficialContextState(map, officialContextRuntimeVisibility(officialVisibilityRef.current, temporalQueryRef.current.frame, noaaRadarReadyRef.current, noaaRadarFrameTimeRef.current), officialOpacityRef.current, officialPayloadsRef.current);
          setElevationExaggeration(map, verticalExaggerationRef.current);
          map.setProjection({ type: projectionRef.current });
          applySceneEnvironment(map, atmospherePresetRef.current, lightAzimuthRef.current);
          map.setVerticalFieldOfView(fieldOfViewRef.current);
          setTerrainState(setTerrainPresentation(map, scenePresetRef.current === "elevation-3d", verticalExaggerationRef.current));
          setTerrainHeightOverlay(map, scenePresetRef.current === "elevation-3d" && topographicOverlayRef.current);
          setStructures3DState(setStructureExtrusions(map, structures3DRef.current));
          const currentSelection = selectedRef.current;
          if (currentSelection) {
            const mismatch = (currentSelection.featureId.startsWith("official-context:") && temporalQueryRef.current.frame !== OFFICIAL_CONTEXT_PRESENT_FRAME)
              || !isFeatureAvailableForTemporalQuery(currentSelection.layer, currentSelection.properties.year, temporalQueryRef.current);
            const layerVisible = selectionCarrierIsVisible(currentSelection, visibilityRef.current, officialVisibilityRef.current, temporalQueryRef.current.frame);
            const filtered = !selectionPassesEvidenceFilter(currentSelection, mapEvidenceFilterRef.current);
            updateSelectionSource(map, mismatch || !layerVisible || filtered ? null : currentSelection.geometry);
          }
          updateMeasurementSource(map, buildMeasurementData(measureCoordinatesRef.current, measurementGeometryModeRef.current));
          updateAnalysisAreaSource(map, analysisAreaRef.current);
          updateImportPreviewSource(map, importPreviewVisibleRef.current ? importPreviewRef.current?.featureCollection : null);
          refreshMaplibreProbe();
        };

        map.on("style.load", syncStyle);
        map.once("load", () => {
          syncStyle();
          map.setProjection({ type: projectionRef.current });
          setRuntime({ kind: "loading", message: `MapLibre ${version} loaded · verifying local sources and interactions…` });
          map.resize();
        });

        let lastHoverSample = -Infinity;
        map.on("mousemove", (event) => {
          const now = performance.now();
          if (map.isMoving() || now - lastHoverSample < 80) return;
          lastHoverSample = now;
          if (scenePresetRef.current === "elevation-3d" && topographicOverlayRef.current) {
            // @ts-expect-error MapLibre runtime accepts the unexaggerated query option; bundled types currently omit it.
            const elevationMeters = map.queryTerrainElevation([event.lngLat.lng, event.lngLat.lat], { exaggerated: false });
            setTerrainElevationReading(elevationMeters !== null && Number.isFinite(elevationMeters) ? {
              longitude: event.lngLat.lng,
              latitude: event.lngLat.lat,
              meters: elevationMeters,
              feet: elevationMeters * 3.28084,
            } : null);
          }
          const availableLayers = interactiveLayerIds.filter((id) => map.getLayer(id));
          const candidate = (availableLayers.length ? map.queryRenderedFeatures(event.point, { layers: availableLayers }) : [])[0];
          const availableOfficialLayers = OFFICIAL_CONTEXT_INTERACTIVE_LAYER_IDS.filter((id) => map.getLayer(id));
          const officialCandidate = candidate || !availableOfficialLayers.length ? null : map.queryRenderedFeatures(event.point, { layers: availableOfficialLayers })[0];
          const externalCandidate = candidate ? null : officialCandidate ?? map.queryRenderedFeatures(event.point).find((feature) => {
            const sourceId = typeof feature.source === "string" ? feature.source : "";
            const isSiteLocal = sourceId.startsWith("kfm-") || LAYER_REGISTRY.some((layer) => layer.sourceId === sourceId);
            return !isSiteLocal && Boolean(feature.geometry) && Boolean(feature.properties && Object.keys(feature.properties).length);
          });
          if (!candidate && !externalCandidate) {
            map.getCanvas().style.cursor = "";
            if (hoveredRef.current) map.setFeatureState(hoveredRef.current, { hover: false });
            hoveredRef.current = null;
            setHoverSummary(null);
            return;
          }
          map.getCanvas().style.cursor = "pointer";
          if (!candidate) {
            if (hoveredRef.current) map.setFeatureState(hoveredRef.current, { hover: false });
            hoveredRef.current = null;
            const externalTitle = String(externalCandidate?.properties?.name ?? externalCandidate?.properties?.name_en ?? externalCandidate?.properties?.event ?? externalCandidate?.properties?.monitoringLocationId ?? externalCandidate?.properties?.class ?? "Basemap feature");
            const officialSource = externalCandidate?.source ? OFFICIAL_CONTEXT_BY_SOURCE_ID[externalCandidate.source] : undefined;
            setHoverSummary({
              id: `external:${externalCandidate?.source ?? "context"}:${externalTitle}`,
              title: externalTitle,
              subtitle: officialSource?.shortTitle ?? "External basemap context",
              state: "No KFM evidence attached",
              x: Math.max(8, Math.min(event.point.x + 18, map.getCanvas().clientWidth - 270)),
              y: Math.max(8, Math.min(event.point.y + 18, map.getCanvas().clientHeight - 112)),
            });
            return;
          }
          const hoverLayer = findLayerByRenderer(candidate.layer.id);
          const hoverFeatureId = String(candidate.properties?.fid ?? candidate.id ?? "");
          const hoverRecord = hoverFeatureId ? findFeature(hoverFeatureId) : null;
          setHoverSummary({
            id: `${candidate.source}:${hoverFeatureId || candidate.properties?.cluster_id || candidate.layer.id}`,
            title: candidate.properties?.cluster
              ? `${candidate.properties.point_count ?? "Multiple"} nearby place records`
              : hoverRecord?.feature.properties.title ?? hoverLayer?.title ?? "Map feature",
            subtitle: candidate.properties?.cluster ? "Select to expand the cluster" : hoverLayer?.title ?? "Site-local map layer",
            state: candidate.properties?.cluster ? "Generalized cluster" : hoverRecord ? evidenceLabels[hoverRecord.feature.properties.evidenceState].label : "Inspect for details",
            x: Math.max(8, Math.min(event.point.x + 18, map.getCanvas().clientWidth - 270)),
            y: Math.max(8, Math.min(event.point.y + 18, map.getCanvas().clientHeight - 112)),
          });
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
        map.getCanvas().addEventListener("mouseleave", () => {
          if (hoveredRef.current && map.getSource(hoveredRef.current.source)) {
            try { map.setFeatureState(hoveredRef.current, { hover: false }); } catch { /* Source teardown can race a pointer exit. */ }
          }
          hoveredRef.current = null;
          map.getCanvas().style.cursor = "";
          setHoverSummary(null);
          setTerrainElevationReading(null);
        });

        map.on("click", (event) => {
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

          const availableLayers = interactiveLayerIds.filter((id) => map.getLayer(id));
          const renderedCandidates = availableLayers.length ? map.queryRenderedFeatures(event.point, { layers: availableLayers }) : [];
          const candidate = renderedCandidates[0];
          if (!candidate) {
            setMapQueryCandidates([]);
            const availableOfficialLayers = OFFICIAL_CONTEXT_INTERACTIVE_LAYER_IDS.filter((id) => map.getLayer(id));
            const officialCandidate = availableOfficialLayers.length ? map.queryRenderedFeatures(event.point, { layers: availableOfficialLayers })[0] : undefined;
            const externalCandidate = officialCandidate ?? map.queryRenderedFeatures(event.point).find((feature) => {
              const sourceId = typeof feature.source === "string" ? feature.source : "";
              const isSiteLocal = sourceId.startsWith("kfm-") || LAYER_REGISTRY.some((layer) => layer.sourceId === sourceId);
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
              popupRef.current?.remove();
              const popupNode = document.createElement("div");
              popupNode.className = "map-popup-content";
              const title = document.createElement("strong");
              title.textContent = context.properties.title;
              const state = document.createElement("span");
              state.textContent = `${OFFICIAL_CONTEXT_BY_SOURCE_ID[externalCandidate?.source ?? ""]?.shortTitle ?? "Basemap context"} · no KFM evidence`;
              popupNode.append(title, state);
              popupRef.current = new maplibregl.Popup({ closeButton: true, closeOnClick: false, maxWidth: "280px" })
                .setLngLat(event.lngLat)
                .setDOMContent(popupNode)
                .addTo(map);
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
          let candidateStack = [...stableCandidates.values()];
          if (candidateStack.some((item) => item.layerId !== "kansas-extent")) candidateStack = candidateStack.filter((item) => item.layerId !== "kansas-extent");
          if (candidateStack.length > 1) {
            popupRef.current?.remove();
            mapUtilityReturnRef.current = mapContainerRef.current;
            setMapQueryCandidates(candidateStack);
            setMapFeatureLayer("ALL");
            setMapUtilityView("inspect");
            setMapUtilityOpen(true);
            setToolsExpanded(false);
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
          popupRef.current?.remove();
          const popupNode = document.createElement("div");
          popupNode.className = "map-popup-content";
          const title = document.createElement("strong");
          title.textContent = context.properties.title;
          const state = document.createElement("span");
          state.textContent = evidenceLabels[context.properties.evidenceState].label;
          popupNode.append(title, state);
          popupRef.current = new maplibregl.Popup({ closeButton: true, closeOnClick: false, maxWidth: "260px" })
            .setLngLat(event.lngLat)
            .setDOMContent(popupNode)
            .addTo(map);
        });
        interactionHandlersBound = true;

        map.on("movestart", () => {
          const center = map.getCenter();
          lastKnownGoodViewRef.current = { center: [center.lng, center.lat], zoom: map.getZoom(), bearing: map.getBearing(), pitch: map.getPitch() };
        });
        map.on("moveend", () => {
          const center = map.getCenter();
          const nextView: ViewState = { center: [center.lng, center.lat], zoom: map.getZoom(), bearing: map.getBearing(), pitch: map.getPitch() };
          const bounds = map.getBounds();
          setMapViewportBounds({ west: bounds.getWest(), south: bounds.getSouth(), east: bounds.getEast(), north: bounds.getNorth() });
          setView(nextView);
          if (replayingCameraHistoryRef.current) {
            replayingCameraHistoryRef.current = false;
          } else if (!locationDerivedViewRef.current) {
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
        });
        map.on("error", (event) => {
          const message = event.error?.message || "The map reported an unknown rendering error.";
          const sourceId = (event as typeof event & { sourceId?: string }).sourceId;
          const affectedLayer = sourceId ? LAYER_REGISTRY.find((layer) => layer.sourceId === sourceId) : undefined;
          const affectedOfficialContext = sourceId ? OFFICIAL_CONTEXT_BY_SOURCE_ID[sourceId] : undefined;
          if (basemapRef.current === "standard" && !styleFallbackAttempted && (!sourceId || (!affectedLayer && !affectedOfficialContext && sourceId !== TERRAIN_SOURCE_ID && sourceId !== TERRAIN_COLOR_SOURCE_ID))) {
            styleFallbackAttempted = true;
            runtimeError = null;
            degradedReason = `Standard vector basemap unavailable; switched to the local MapLibre style. ${message}`;
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
            officialRasterFailuresRef.current.add(affectedOfficialContext.id);
            setOfficialStates(current => current[affectedOfficialContext.id] === "error" ? current : ({ ...current, [affectedOfficialContext.id]: "error" }));
            setOfficialErrors(current => current[affectedOfficialContext.id] ? current : ({ ...current, [affectedOfficialContext.id]: message }));
            return;
          }
          runtimeError = message;
          if (sourceId) failedSourceIds.add(sourceId);
          if (sourceId === TERRAIN_SOURCE_ID) {
            failedTerrainSourceRef.current = map.getSource(TERRAIN_SOURCE_ID);
            setTerrainState("ERROR");
            degradedReason = `Terrain DEM is unavailable; the 2D map remains usable. ${message}`;
            setRuntime({ kind: "degraded", message: degradedReason });
            return;
          }
          if (sourceId === TERRAIN_COLOR_SOURCE_ID) {
            topographicOverlayRef.current = false;
            setTopographicOverlay(false);
            setTerrainElevationReading(null);
            announce("Topographic height overlay is unavailable; Terrain 3D remains active");
            return;
          }
          if (sourceId === "usgs-topo-context") {
            setRuntime({ kind: "degraded", message: `USGS topographic basemap is unavailable; site-local evidence layers remain usable. ${message}` });
            return;
          }
          setMaplibreProbe((current) => ({ ...current, error: message }));
          if (affectedLayer) {
            setSourceStates((current) => ({ ...current, [affectedLayer.id]: "error" }));
            setRuntime({ kind: "degraded", message: `${affectedLayer.title} could not load; other map layers remain available. ${message}` });
          } else if (sourceId === "osm-context") {
            setRuntime({ kind: "degraded", message: `OpenStreetMap context is unavailable; site-local evidence layers remain available. ${message}` });
          } else {
            setRuntime({ kind: "error", message: `Map runtime error: ${message}` });
          }
        });
        map.on("sourcedata", (event) => {
          if (event.sourceId === TERRAIN_SOURCE_ID && event.isSourceLoaded && failedTerrainSourceRef.current !== map.getSource(TERRAIN_SOURCE_ID)) {
            setTerrainState("READY");
            failedSourceIds.delete(TERRAIN_SOURCE_ID);
            if (degradedReason?.startsWith("Terrain DEM is unavailable")) { degradedReason = null; runtimeError = null; }
          }
          if (!event.sourceId) return;
          const officialSource = OFFICIAL_CONTEXT_BY_SOURCE_ID[event.sourceId];
          if (officialSource && officialSource.id !== "nws-radar" && !officialSource.apiPath && !officialSource.managedAdapterPath && event.isSourceLoaded && !officialRasterFailuresRef.current.has(officialSource.id)) {
            setOfficialStates(current => current[officialSource.id] === "ready" ? current : ({ ...current, [officialSource.id]: "ready" }));
          }
          const layer = LAYER_REGISTRY.find((candidate) => candidate.sourceId === event.sourceId);
          if (!layer) return;
          setSourceActivity((current) => ({
            ...current,
            [layer.id]: event.isSourceLoaded ? "SETTLED" : "UPDATING",
          }));
        });
        map.on("idle", () => {
          const probe = refreshMaplibreProbe();
          const ready = probe.styleLoaded
            && probe.canvasReady
            && probe.tilesLoaded
            && probe.sourcesReady === LAYER_REGISTRY.length
            && probe.interactionsReady
            && !runtimeError
            && !degradedReason;
          if (!ready) {
            setRuntime({ kind: runtimeError || degradedReason ? "degraded" : "loading", message: runtimeError ? `MapLibre runtime proof is incomplete: ${runtimeError}` : degradedReason ?? "MapLibre is waiting for all admitted local capabilities to settle…" });
            return;
          }
          setRuntime({ kind: "ready", message: `MapLibre ${version} ready · ${LAYER_REGISTRY.length} local sources · interactions proven` });
        });
      } catch (error) {
        const message = error instanceof Error ? error.message : "unknown failure";
        setMaplibreProbe((current) => ({ ...current, error: message }));
        setRuntime({ kind: "error", message: `MapLibre could not start: ${message}` });
      }
    }).catch((error: unknown) => {
      const message = error instanceof Error ? error.message : "unknown failure";
      setMaplibreProbe((current) => ({ ...current, error: message }));
      setRuntime({ kind: "error", message: `MapLibre could not load: ${message}` });
    });

    return () => {
      disposed = true;
      popupRef.current?.remove();
      styleGenerationReadyRef.current = false;
      if (sceneOrbitTimerRef.current !== null) window.clearTimeout(sceneOrbitTimerRef.current);
      mapRef.current?.remove();
      mapRef.current = null;
    };
  }, [announce]);

  useEffect(() => {
    const map = mapRef.current;
    if (!map || !styleGenerationReadyRef.current) return;
    applyRegistryState(map, visibility, opacity, yearRef.current, layerOrder, mapEvidenceFilter, temporalQueryRef.current);
    setElevationExaggeration(map, verticalExaggerationRef.current);
  }, [layerOrder, mapEvidenceFilter, opacity, visibility]);

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
    applyTemporalRegistryFilters(map, year, mapEvidenceFilter, temporalQuery);
  }, [mapEvidenceFilter, temporalQuery, year]);

  useEffect(() => {
    const map = mapRef.current;
    if (!map || !styleGenerationReadyRef.current) return;
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
  }, [applyNoaaRadarFrame, effectiveOfficialVisibility, noaaRadarFrameLoadState, noaaRadarFrameTime, noaaRadarPendingFrameTime, noaaRadarRenderable, noaaRadarSelectedAtPresent, officialOpacity, officialPayloads, styleReady]);

  useEffect(() => {
    const map = mapRef.current;
    if (!map || !styleGenerationReadyRef.current) return;
    setElevationExaggeration(map, verticalExaggeration);
  }, [verticalExaggeration]);

  useEffect(() => {
    const map = mapRef.current;
    if (!map || !styleGenerationReadyRef.current) {
      setTerrainState(scenePreset === "elevation-3d" ? "LOADING" : "OFF");
      return;
    }
    setTerrainState(setTerrainPresentation(map, scenePreset === "elevation-3d", verticalExaggeration));
  }, [scenePreset, styleReady, verticalExaggeration]);

  useEffect(() => {
    const map = mapRef.current;
    if (!map || !styleGenerationReadyRef.current) {
      setStructures3DState(structures3DEnabled ? "UNAVAILABLE" : "OFF");
      return;
    }
    setStructures3DState(setStructureExtrusions(map, structures3DEnabled));
  }, [structures3DEnabled, styleReady]);

  useEffect(() => {
    const map = mapRef.current;
    if (!map || !styleGenerationReadyRef.current) return;
    let animationFrame = 0;
    let lastFrame = 0;
    const effectsActive = dynamicEffects && !reducedMotion && renderQuality !== "efficient" && ["water-context", "smoke-context", "fire-context", "hazards-context", "habitat-connectivity", "transport-context", "communities"].some(id => visibility[id]);

    if (!effectsActive) {
      applyDynamicMapEffects(map, 0, opacity, false);
      return;
    }

    const renderEffects = (timestamp: number) => {
      if (!document.hidden && !map.isMoving() && timestamp - lastFrame >= 80 && styleGenerationReadyRef.current) {
        applyDynamicMapEffects(map, timestamp, opacity, true);
        lastFrame = timestamp;
      }
      if (!document.hidden) animationFrame = window.requestAnimationFrame(renderEffects);
    };
    const resume = () => { window.cancelAnimationFrame(animationFrame); if (!document.hidden) animationFrame = window.requestAnimationFrame(renderEffects); };
    document.addEventListener("visibilitychange", resume); resume();
    return () => {
      window.cancelAnimationFrame(animationFrame);
      document.removeEventListener("visibilitychange", resume);
      if (styleGenerationReadyRef.current) applyDynamicMapEffects(map, 0, opacity, false);
    };
  }, [dynamicEffects, opacity, reducedMotion, renderQuality, styleReady, visibility]);

  useEffect(() => {
    const map = mapRef.current;
    if (!map) return;
    const pendingRadarFrame = noaaRadarPendingFrameTimeRef.current;
    noaaRadarFrameLoadCleanupRef.current?.();
    noaaRadarFrameLoadCleanupRef.current = null;
    noaaRadarFrameFailureRef.current = null;
    if (pendingRadarFrame) setNoaaRadarFrameLoadState("idle");
    styleGenerationReadyRef.current = false;
    setPlaying(false);
    map.setStyle(BASEMAPS[basemap].style);
    setStyleReady(false);
    setTerrainState(scenePresetRef.current === "elevation-3d" ? "LOADING" : "OFF");
    setMaplibreProbe((current) => ({ ...current, styleLoaded: false, idle: false, tilesLoaded: false, sourcesReady: 0 }));
    setRuntime({ kind: "loading", message: `Applying ${BASEMAPS[basemap].title} style…` });
  }, [basemap]);

  useEffect(() => {
    const selectionVisible = Boolean(selected && !selectedTimeMismatch && !selectedLayerHidden && !selectedEvidenceFiltered);
    if (!selectionVisible) {
      popupRef.current?.remove();
      popupRef.current = null;
    }
    const map = mapRef.current;
    if (!map || !styleGenerationReadyRef.current) return;
    updateSelectionSource(map, selectionVisible && selected ? selected.geometry : null);
  }, [selected, selectedEvidenceFiltered, selectedLayerHidden, selectedTimeMismatch]);

  useEffect(() => {
    const map = mapRef.current;
    if (!map || !styleGenerationReadyRef.current) return;
    map.setProjection({ type: projection });
    setMaplibreProbe((current) => ({ ...current, projection }));
  }, [projection]);

  useEffect(() => {
    const map = mapRef.current;
    if (!map || !styleGenerationReadyRef.current) return;
    applySceneEnvironment(map, atmospherePreset, lightAzimuth);
    map.setVerticalFieldOfView(fieldOfView);
  }, [atmospherePreset, fieldOfView, lightAzimuth]);

  useEffect(() => {
    const map = mapRef.current;
    if (!map) return;
    if (gestureMode === "cooperative") map.cooperativeGestures.enable();
    else map.cooperativeGestures.disable();
  }, [gestureMode]);

  useEffect(() => {
    const map = mapRef.current;
    if (!map) return;
    const first = window.requestAnimationFrame(() => map.resize());
    const second = window.setTimeout(() => map.resize(), 260);
    return () => { window.cancelAnimationFrame(first); window.clearTimeout(second); };
  }, [leftOpen, rightOpen, timelineOpen]);

  useEffect(() => {
    if (!playing || reducedMotion || temporalMode === "snapshot" || temporalMode === "comparison") return;
    const timer = window.setInterval(() => {
      const next = nextTemporalFrame(temporalSequence, yearRef.current, playbackDirection, playbackLoopMode);
      if (next === null) {
        setPlaying(false);
        return;
      }
      yearRef.current = next;
      setYear(next);
      setPreviewYear(next);
    }, 1300 / playbackSpeed);
    return () => window.clearInterval(timer);
  }, [playbackDirection, playbackLoopMode, playbackSpeed, playing, reducedMotion, temporalMode, temporalSequence]);

  useEffect(() => {
    if (!noaaRadarManifest) return;
    setNoaaRadarClock(Date.now());
    const timer = window.setInterval(() => setNoaaRadarClock(Date.now()), 60_000);
    return () => window.clearInterval(timer);
  }, [noaaRadarManifest]);

  useEffect(() => {
    if (!noaaRadarSelectedAtPresent) {
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
        applyOfficialContextState(
          map,
          officialContextRuntimeVisibility(officialVisibilityRef.current, temporalQueryRef.current.frame, false, null),
          officialOpacityRef.current,
          officialPayloadsRef.current,
        );
      }
      setNoaaRadarFrameLoadState(noaaRadarFrameTimeRef.current ? "ready" : "idle");
      return;
    }
    void refreshNoaaRadarManifest(true);
    const timer = window.setInterval(() => { void refreshNoaaRadarManifest(true); }, 240_000);
    return () => window.clearInterval(timer);
  }, [noaaRadarSelectedAtPresent, refreshNoaaRadarManifest]);

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
      return;
    }
    const timer = window.setInterval(() => {
      void refreshStreamflow(streamflowRange, streamflowSelectedStationId, true);
    }, 300_000);
    return () => window.clearInterval(timer);
  }, [refreshStreamflow, streamflowRange, streamflowSelectedAtPresent, streamflowSelectedStationId]);

  useEffect(() => {
    if (!officialVisibility["noaa-nwps-gauges"] || temporalQuery.frame !== OFFICIAL_CONTEXT_PRESENT_FRAME) return;
    const timer = window.setInterval(() => { void refreshNoaaHydrologyNetwork(true); }, 300_000);
    return () => window.clearInterval(timer);
  }, [officialVisibility, refreshNoaaHydrologyNetwork, temporalQuery.frame]);

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
    const timer = window.setTimeout(() => {
      const params = buildExplorerParams();
      window.history.replaceState(null, "", `${window.location.pathname}?${params.toString()}`);
    }, 280);
    return () => window.clearTimeout(timer);
  }, [buildExplorerParams]);

  useEffect(() => {
    if (!mapContextOpen) return;
    const panel = composerRef.current;
    if (!panel) return;
    const controls = () => Array.from(panel.querySelectorAll<HTMLElement>("button:not([disabled]), a[href], input, select"));
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
    setRepositoryConnection({ state: "loading" });
    void fetch("/api/repository-status", { cache: "no-store", signal: controller.signal })
      .then(async (response) => {
        const payload = await response.json().catch(() => null) as Record<string, unknown> | null;
        if (!response.ok || payload?.state !== "ready" || typeof payload.commit !== "string" || !/^[0-9a-f]{40}$/i.test(payload.commit)) {
          throw new Error("Repository status was unavailable");
        }
        setRepositoryConnection({
          state: "ready",
          liveCommit: payload.commit.toLowerCase(),
          shortCommit: typeof payload.shortCommit === "string" ? payload.shortCommit : payload.commit.slice(0, 7),
          commitDate: typeof payload.commitDate === "string" ? payload.commitDate : null,
          message: typeof payload.message === "string" ? payload.message : null,
          observedAt: typeof payload.observedAt === "string" ? payload.observedAt : undefined,
        });
      })
      .catch((error) => {
        if (error instanceof DOMException && error.name === "AbortError") return;
        setRepositoryConnection({ state: "error" });
      });
    return () => controller.abort();
  }, [repositoryOpen, repositoryRefreshKey]);

  useEffect(() => {
    if (!repositoryOpen) return;
    const panel = repositoryPanelRef.current;
    if (!panel) return;
    const focusable = () => Array.from(panel.querySelectorAll<HTMLElement>("button:not([disabled]), input:not([disabled]), select:not([disabled]), a[href], [tabindex='0']"));
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
    if (!isCompact) return;
    const openPanel = mapUtilityOpen ? mapUtilityPanelRef.current : rightOpen ? rightPanelRef.current : leftOpen ? leftPanelRef.current : timelineOpen ? timelineRef.current : null;
    if (!openPanel) return;
    const focusable = () => Array.from(openPanel.querySelectorAll<HTMLElement>("button:not([disabled]), input:not([disabled]), select:not([disabled]), a[href], [tabindex='0']")).filter((element) => !element.hasAttribute("hidden"));
    const items = focusable();
    items[0]?.focus();
    const handleKey = (event: KeyboardEvent) => {
      if (event.key === "Escape") {
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
  }, [isCompact, leftOpen, mapUtilityOpen, rightOpen, timelineOpen, closeLeftPanel, closeMapUtility, closeRightPanel, closeTimelinePanel]);

  useEffect(() => {
    const handleEscape = (event: KeyboardEvent) => {
      if (event.key !== "Escape" || repositoryOpen) return;
      if (workspaceDetailsRef.current?.open) workspaceDetailsRef.current.open = false;
      else if (sourceStatusOpen) { setSourceStatusOpen(false); document.querySelector<HTMLButtonElement>('[aria-controls="map-source-status"]')?.focus(); }
      else if (mapContextOpen) setMapContextOpen(false);
      else if (helpOpen) setHelpOpen(false);
      else if (guidedStartOpen) dismissGuidedStart();
      else if (storyOpen) closeStoryTrail();
      else if (toolsExpanded) setToolsExpanded(false);
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
      else if (!isCompact && rightOpen) closeRightPanel();
    };
    document.addEventListener("keydown", handleEscape);
    return () => document.removeEventListener("keydown", handleEscape);
  }, [sourceStatusOpen, guidedStartOpen, helpOpen, isCompact, mapContextOpen, mapUtilityOpen, repositoryOpen, rightOpen, storyOpen, toolsExpanded, closeMapUtility, closeRightPanel, closeStoryTrail, dismissGuidedStart]);

  const chooseSearchResult = (item: GlobalSearchItem) => {
    setGlobalQuery("");
    if (item.kind === "source") {
      setLeftPanelMode("layers");
      setOfficialContextVisible(item.officialContextId, true);
      announce(`Opened ${item.title} in official data connections`);
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
    setToolsExpanded(false);
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
    announce("Fit the generalized Kansas demonstration extent");
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
    if (mode === "compare") {
      openMapUtility("compare");
      announce("Compare opened · choose two layers and dates without changing the active map time");
      return;
    }

    stopSceneOrbit(false);
    const map = mapRef.current;
    // A second representation choice must cancel the first camera transition.
    // Otherwise MapLibre can finish an older ease after React has already
    // selected the newer mode, leaving the controls and canvas disagreeing.
    map?.stop();
    const currentBearing = map?.getBearing() ?? view.bearing;
    const currentPitch = map?.getPitch() ?? view.pitch;
    const nextProjection = mode === "globe" ? "globe" : "mercator";
    const nextScenePreset: ScenePresetId = mode === "terrain" ? "elevation-3d" : mode === "globe" ? "globe-overview" : "overview-2d";
    const nextAtmosphere: AtmospherePreset = mode === "terrain" ? "dusk" : mode === "globe" ? "clear" : "night";
    const nextFieldOfView = mode === "terrain" ? 44 : mode === "globe" ? 42 : 36;
    const nextPitch = mode === "terrain" ? Math.max(48, currentPitch) : mode === "globe" ? Math.max(22, currentPitch) : 0;
    const nextBearing = mode === "2d" ? 0 : currentBearing;

    projectionRef.current = nextProjection;
    scenePresetRef.current = nextScenePreset;
    verticalExaggerationRef.current = 1;
    atmospherePresetRef.current = nextAtmosphere;
    lightAzimuthRef.current = mode === "terrain" ? 235 : mode === "globe" ? 225 : 210;
    fieldOfViewRef.current = nextFieldOfView;

    // Commit renderer state as one transaction before scheduling React's
    // presentation updates. This makes repeated 2D ↔ terrain ↔ globe changes
    // idempotent and prevents a stale effect or style event from winning.
    if (map?.isStyleLoaded()) {
      if (mode !== "terrain") {
        setTerrainState(setTerrainPresentation(map, false, 1));
        setTerrainHeightOverlay(map, false);
      }
      map.setProjection({ type: nextProjection });
      if (mode === "terrain") {
        setTerrainState(setTerrainPresentation(map, true, 1));
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
    if (mode === "terrain") {
      setVisibility((current) => {
        const next = { ...current, "elevation-concept": false };
        visibilityRef.current = next;
        return next;
      });
    }
    map?.easeTo({ pitch: nextPitch, bearing: nextBearing, duration: motionDuration(420), essential: false });
    announce(`${mode === "terrain" ? "Terrain 3D display" : mode === "globe" ? "Globe display" : "2D evidence display"} applied · active time and selection preserved`);
  };

  const startTerrainInvestigation = () => {
    activateMapRepresentation("terrain");
    openMapUtility("scene");
    toggleMeasure("distance");
    announce("Terrain investigation ready at physical 1× scale. Draw a line on the map, finish it, then preview the display profile.");
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
      setTerrainElevationReading(null);
      setLockedTerrainElevation(null);
    }
    announce(next ? "Topographic height colors enabled · move over the map to read unexaggerated elevation" : "Topographic height colors disabled");
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
        // @ts-expect-error MapLibre runtime accepts the unexaggerated query option; bundled types currently omit it.
        const elevation = map.queryTerrainElevation(coordinate, { exaggerated: false });
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
    if (map.getLayer(TERRAIN_HILLSHADE_LAYER_ID)) map.removeLayer(TERRAIN_HILLSHADE_LAYER_ID);
    map.setTerrain(null);
    if (map.getSource(TERRAIN_SOURCE_ID)) map.removeSource(TERRAIN_SOURCE_ID);
    setTerrainState(setTerrainPresentation(map, true, verticalExaggerationRef.current));
    setRuntime({ kind: "loading", message: "Retrying the attributed AWS Terrain Tiles DEM…" });
    announce("Terrain source retry started; the 2D evidence path remains available");
  };

  const applyTerrainLook = (look: "natural" | "topographic" | "buildings") => {
    const nextBasemap: BasemapKey = look === "natural" ? "imagery" : look === "topographic" ? "topo" : "standard";
    topographicOverlayRef.current = false; setTopographicOverlay(false);
    if (mapRef.current) setTerrainHeightOverlay(mapRef.current, false);
    structures3DRef.current = look === "buildings"; setStructures3DEnabled(look === "buildings");
    basemapRef.current = nextBasemap; setBasemap(nextBasemap);
    activateMapRepresentation("terrain");
    atmospherePresetRef.current = "clear"; setAtmospherePreset("clear");
    announce(`${look === "natural" ? "Imagery with physical relief" : look === "topographic" ? "Topographic terrain" : "Provider-height buildings; zoom in where mapped"} selected. Data time and camera center are preserved.`);
  };

  const startSceneOrbit = () => {
    const map = mapRef.current;
    if (!map) {
      announce("The MapLibre camera is not ready yet");
      return;
    }
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      announce("Orbit is paused because reduced motion is enabled");
      return;
    }
    stopSceneOrbit(false);
    setSceneOrbiting(true);
    replayingCameraHistoryRef.current = true;
    map.easeTo({
      bearing: map.getBearing() + 90,
      pitch: Math.max(46, map.getPitch()),
      duration: 12_000,
      easing: (progress) => progress,
    });
    sceneOrbitTimerRef.current = window.setTimeout(() => {
      sceneOrbitTimerRef.current = null;
      setSceneOrbiting(false);
    }, 12_050);
    announce("Started a reversible 90° MapLibre camera orbit");
  };

  const setMapGestureMode = (mode: "cooperative" | "direct") => {
    gestureModeRef.current = mode;
    setGestureMode(mode);
    announce(mode === "cooperative" ? "Cooperative map gestures enabled" : "Direct map gestures enabled");
  };

  const probeSourceConnection = (layer: LayerRecord) => {
    const map = mapRef.current;
    if (!map?.isStyleLoaded() || !map.getSource(layer.sourceId) || !map.isSourceLoaded(layer.sourceId)) {
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
    activateMapUtilityView("inspect");
  };

  const applyViewProfile = (profile: MapViewProfile) => {
    const baselineSources = BASELINE_STACKS[profile.id];
    const nextVisibility = Object.fromEntries(LAYER_REGISTRY.map((layer) => [layer.id, baselineSources ? false : profile.visibleLayerIds.includes(layer.id)]));
    if (baselineSources) for (const source of OFFICIAL_CONTEXT_SOURCES) setOfficialContextVisible(source.id, baselineSources.includes(source.id));
    const nextScenePreset: ScenePresetId = profile.id === "smoke" ? "smoke-context" : profile.id === "elevation" ? "elevation-3d" : profile.projection === "globe" ? "globe-overview" : "overview-2d";
    const nextAtmosphere: AtmospherePreset = profile.id === "smoke" || profile.id === "hazards" || profile.id === "elevation" ? "dusk" : profile.projection === "globe" ? "clear" : "night";
    const nextLightAzimuth = profile.id === "elevation" ? 235 : profile.projection === "globe" ? 225 : 210;
    const nextFieldOfView = profile.id === "elevation" ? 44 : profile.projection === "globe" ? 42 : 36;
    stopSceneOrbit(false);
    mapRef.current?.stop();
    visibilityRef.current = nextVisibility;
    mapEvidenceFilterRef.current = "ALL";
    basemapRef.current = profile.basemap;
    projectionRef.current = profile.projection;
    scenePresetRef.current = nextScenePreset;
    verticalExaggerationRef.current = 1;
    atmospherePresetRef.current = nextAtmosphere;
    lightAzimuthRef.current = nextLightAzimuth;
    fieldOfViewRef.current = nextFieldOfView;
    setVisibility(nextVisibility);
    commitTemporalFrame(baselineSources ? OFFICIAL_CONTEXT_PRESENT_FRAME : profile.year);
    setMapEvidenceFilter("ALL");
    setPlaying(false);
    setTemporalMode("snapshot");
    setBasemap(profile.basemap);
    setProjection(profile.projection);
    setScenePreset(nextScenePreset);
    setVerticalExaggeration(1);
    setAtmospherePreset(nextAtmosphere);
    setLightAzimuth(nextLightAzimuth);
    setFieldOfView(nextFieldOfView);
    setMapQueryCandidates([]);
    locationDerivedViewRef.current = false;
    setLocationCameraRedacted(false);
    clearSelectionState();
    const map = mapRef.current;
    if (map?.isStyleLoaded()) {
      if (nextScenePreset !== "elevation-3d") {
        setTerrainState(setTerrainPresentation(map, false, 1));
        setTerrainHeightOverlay(map, false);
      } else {
        setTerrainState(setTerrainPresentation(map, true, 1));
        setTerrainHeightOverlay(map, topographicOverlayRef.current);
      }
      map.setProjection({ type: profile.projection });
      applySceneEnvironment(map, nextAtmosphere, nextLightAzimuth);
      map.setVerticalFieldOfView(nextFieldOfView);
      map.triggerRepaint();
    }
    if (profile.id === "overview") {
      map?.easeTo({ center: [...KANSAS_VIEW.center] as [number, number], zoom: KANSAS_VIEW.zoom, bearing: KANSAS_VIEW.bearing, pitch: KANSAS_VIEW.pitch, duration: motionDuration(600) });
    } else {
      map?.fitBounds([[-102.1, 36.95], [-94.55, 40.05]], { padding: 54, duration: motionDuration(600) });
    }
    announce(`${profile.title} applied · view state only`);
  };

  const applyLivingAtlasView = (atlasView: LivingAtlasView) => {
    if (atlasView.status === "DESIGN_HOLD") {
      announce(`${atlasView.title} is visible as a design hold; its governed data package is not admitted`);
      return;
    }
    const profile = atlasView.profileId ? MAP_VIEW_PROFILES.find((candidate) => candidate.id === atlasView.profileId) : undefined;
    if (atlasView.profileId && !profile) {
      announce(`${atlasView.title} is not available in this Site build`);
      return;
    }
    setCurrentWorkspace("explore");
    setLeftPanelMode("views");
    if (profile) applyViewProfile(profile);
    if (atlasView.id === "living-waters") {
      (["usgs-3dhp-hydrography", "usgs-wbd-watersheds", "noaa-nwps-gauges", "usgs-streamflow"] as const)
        .forEach((sourceId) => setOfficialContextVisible(sourceId, true));
      setLiveInstrument("river");
    }
    if (atlasView.camera && !atlasView.story) {
      mapRef.current?.easeTo({
        center: [...atlasView.camera.center] as [number, number],
        zoom: atlasView.camera.zoom,
        bearing: atlasView.camera.bearing,
        pitch: atlasView.camera.pitch,
        duration: motionDuration(650),
      });
    }
    if (atlasView.story) {
      startStoryTrail();
      return;
    }
    setLeftOpen(false);
    if (isCompact) {
      setRightOpen(false);
      setTimelineOpen(false);
    }
    announce(`${atlasView.title} opened · ${livingAtlasStatusLabel(atlasView.status)}`);
  };

  const applyAnalysisRecipe = (recipe: AnalysisRecipe) => {
    const nextVisibility = Object.fromEntries(LAYER_REGISTRY.map((layer) => [layer.id, recipe.layerIds.includes(layer.id)]));
    stopSceneOrbit(false);
    visibilityRef.current = nextVisibility;
    mapEvidenceFilterRef.current = "ALL";
    basemapRef.current = recipe.basemap;
    projectionRef.current = "mercator";
    atmospherePresetRef.current = "night";
    lightAzimuthRef.current = 210;
    fieldOfViewRef.current = 36;
    setVisibility(nextVisibility);
    commitTemporalFrame(recipe.year);
    setMapEvidenceFilter("ALL");
    setPlaying(false);
    setTemporalMode("snapshot");
    setBasemap(recipe.basemap);
    setProjection("mercator");
    setScenePreset("overview-2d");
    setAtmospherePreset("night");
    setLightAzimuth(210);
    setFieldOfView(36);
    setReportTitle(recipe.title);
    setReportScope(recipe.scope);
    setReportDetail(recipe.detail);
    setReportLayerIds([...recipe.layerIds]);
    setReportQuery("");
    setReportEvidenceFilter("ALL");
    setReportGeneratedAt(new Date().toISOString());
    setMapQueryCandidates([]);
    locationDerivedViewRef.current = false;
    setLocationCameraRedacted(false);
    clearSelectionState();
    mapRef.current?.easeTo({ center: [...recipe.center] as [number, number], zoom: recipe.zoom, bearing: 0, pitch: 0, duration: motionDuration(650) });
    announce(`${recipe.title} recipe applied · map, time, layers, and report updated`);
  };

  const persistSavedWorkspaces = (next: WorkspaceSnapshot[]) => {
    const bounded = next.slice(0, MAX_PLACE_TRAIL_STOPS);
    setSavedWorkspaces(bounded);
    try { window.localStorage.setItem(WORKSPACE_STORAGE_KEY, JSON.stringify(bounded)); } catch { /* Device-local workspace storage is optional. */ }
  };

  const saveCurrentWorkspace = () => {
    const savedAt = new Date().toISOString();
    const redactWorkspaceCamera = locationCameraRedacted || locationDerivedViewRef.current;
    const snapshot: WorkspaceSnapshot = {
      id: `workspace-${Date.now()}`,
      name: normalizePlaceStopName(workspaceName, savedWorkspaces.length + 1),
      savedAt,
      view: redactWorkspaceCamera
        ? { center: [...KANSAS_VIEW.center] as [number, number], zoom: KANSAS_VIEW.zoom, bearing: KANSAS_VIEW.bearing, pitch: KANSAS_VIEW.pitch }
        : { center: [...view.center] as [number, number], zoom: view.zoom, bearing: view.bearing, pitch: view.pitch },
      locationCameraRedacted: redactWorkspaceCamera,
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
      analysisArea: analysisArea ? { ...analysisArea } : null,
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
    persistSavedWorkspaces([snapshot, ...savedWorkspaces]);
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
    const nextYear = KNOWN_TEMPORAL_FRAMES.has(snapshot.year) ? snapshot.year : 2026;
    const nextBasemap: BasemapKey = snapshot.basemap === "standard" || snapshot.basemap === "imagery" || snapshot.basemap === "midnight" || snapshot.basemap === "prairie" || snapshot.basemap === "streets" || snapshot.basemap === "topo" ? snapshot.basemap : "standard";
    const nextProjection = snapshot.projection === "globe" ? "globe" : "mercator";
    // Legacy snapshots predate the marker, so fail closed instead of exposing a possibly location-derived camera.
    const restoredLocationCameraRedaction = snapshot.locationCameraRedacted !== false;
    const savedScene = snapshot.scene;
    const nextScenePreset: ScenePresetId = savedScene?.preset === "globe-overview" || savedScene?.preset === "water-systems" || savedScene?.preset === "smoke-context" || savedScene?.preset === "elevation-3d" || savedScene?.preset === "tile-grid" ? savedScene.preset : "overview-2d";
    const nextVerticalExaggeration = clamp(Number(savedScene?.verticalExaggeration ?? 1), 0, 2);
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
    setTemporalStepRule(savedSweep?.stepRule === "regular-calendar" ? "regular-calendar" : "available-events");
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
    setCompareTimeB(savedComparison && TIME_STEPS.includes(savedComparison.timeB as (typeof TIME_STEPS)[number]) ? savedComparison.timeB : 2026);
    setMapUtilityView(nextSavedSweepMode === "comparison" ? "compare" : "navigate");
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
    if (savedView && Array.isArray(savedView.center) && savedView.center.length === 2) {
      locationDerivedViewRef.current = restoredLocationCameraRedaction;
      setLocationCameraRedacted(restoredLocationCameraRedaction);
      mapRef.current?.easeTo({ center: [...savedView.center] as [number, number], zoom: savedView.zoom, bearing: savedView.bearing, pitch: savedView.pitch, duration: motionDuration(650) });
    }
    const restoredSelection = snapshot.selection ? copyFeature(LAYER_REGISTRY.find((layer) => layer.id === snapshot.selection?.layerId) ?? LAYER_REGISTRY[0], snapshot.selection.featureId) : null;
    selectedRef.current = restoredSelection;
    setSelected(restoredSelection);
    setActivePlaceId(snapshot.id);
    setRightOpen(false);
    setMapQueryCandidates([]);
    announce(`${snapshot.name} restored from Places on this device`);
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
    persistSavedWorkspaces(reorderPlaceStops(savedWorkspaces, snapshot.id, direction));
    announce(`${snapshot.name} moved ${direction < 0 ? "earlier" : "later"} in the Places trail`);
  };

  const deleteSavedWorkspace = (snapshot: WorkspaceSnapshot) => {
    stopPlaceTour(false);
    persistSavedWorkspaces(savedWorkspaces.filter((candidate) => candidate.id !== snapshot.id));
    if (activePlaceId === snapshot.id) setActivePlaceId(null);
    announce(`${snapshot.name} removed from this device`);
  };

  const setLayerGroupVisibility = (layerIds: readonly string[], nextVisible: boolean) => {
    setVisibility((current) => {
      const next = { ...current };
      layerIds.forEach((id) => { next[id] = nextVisible; });
      visibilityRef.current = next;
      return next;
    });
    announce(`${nextVisible ? "Shown" : "Hidden"} ${layerIds.length} catalog layer${layerIds.length === 1 ? "" : "s"}`);
  };

  const updateMapEvidenceFilter = (nextFilter: RegistryEvidenceFilter) => {
    mapEvidenceFilterRef.current = nextFilter;
    setMapEvidenceFilter(nextFilter);
    announce(nextFilter === "ALL" ? "Showing every compatible evidence state" : `Map filtered to ${nextFilter.replaceAll("_", " ")}`);
  };

  const showNearbyContextLayers = () => {
    if (!selected || nearbyContext.length === 0) return;
    const nearbyLayerIds = new Set([selected.layerId, ...nearbyContext.map((row) => row.layer.id)]);
    setVisibility((current) => {
      const next = { ...current };
      nearbyLayerIds.forEach((id) => { next[id] = true; });
      visibilityRef.current = next;
      return next;
    });
    announce(`Shown ${nearbyLayerIds.size} layers represented near ${selected.properties.title}`);
  };

  const fitNearbyContext = () => {
    if (!selected) return;
    const anchors = [selected.properties, ...nearbyContext.map((row) => row.feature.properties)];
    if (anchors.length === 1) {
      mapRef.current?.easeTo({ center: [selected.properties.focusLng, selected.properties.focusLat], zoom: 9, duration: motionDuration(500) });
      return;
    }
    const bounds = anchors.reduce((current, properties) => ({
      west: Math.min(current.west, properties.focusLng),
      south: Math.min(current.south, properties.focusLat),
      east: Math.max(current.east, properties.focusLng),
      north: Math.max(current.north, properties.focusLat),
    }), { west: anchors[0].focusLng, south: anchors[0].focusLat, east: anchors[0].focusLng, north: anchors[0].focusLat });
    mapRef.current?.fitBounds([[bounds.west, bounds.south], [bounds.east, bounds.north]], { padding: 70, maxZoom: 10, duration: motionDuration(600) });
    announce(`Fit ${nearbyContext.length} nearby context records using generalized feature anchors`);
  };

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
      applyOfficialContextState(map, officialContextRuntimeVisibility(officialVisibilityRef.current, temporalQueryRef.current.frame, noaaRadarReadyRef.current, noaaRadarFrameTimeRef.current), officialOpacityRef.current, officialPayloadsRef.current);
      setElevationExaggeration(map, verticalExaggerationRef.current);
      map.setProjection({ type: projectionRef.current });
      applySceneEnvironment(map, atmospherePresetRef.current, lightAzimuthRef.current);
      map.setVerticalFieldOfView(fieldOfViewRef.current);
      const currentSelection = selectedRef.current;
      const selectionAvailable = currentSelection
        && selectionCarrierIsVisible(currentSelection, visibilityRef.current, officialVisibilityRef.current, temporalQueryRef.current.frame)
        && !(currentSelection.featureId.startsWith("official-context:") && temporalQueryRef.current.frame !== OFFICIAL_CONTEXT_PRESENT_FRAME)
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
    } catch (error) {
      setRuntime({ kind: "degraded", message: `Registry reapply failed safely: ${error instanceof Error ? error.message : "unknown failure"}` });
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
    yearRef.current = 2026;
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
      if (source.defaultVisibility && source.apiPath && !officialPayloadsRef.current[source.id as OfficialContextFeedId]) void refreshOfficialContext(source.id as OfficialContextFeedId);
    }
    setLayerOrder(defaultOrder);
    setYear(2026);
    setPreviewYear(2026);
    setTemporalMode("snapshot");
    setTemporalStepRule("available-events");
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
    setCompareTimeB(2026);
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
    setGuidedStartOpen(false);
    setReportTitle("Kansas map data report");
    setReportScope("VIEWPORT");
    setReportDetail("STANDARD");
    setReportLayerIds([...defaultReportLayerIds]);
    setReportSections(defaultReportSections);
    setReportQuery("");
    setReportEvidenceFilter("ALL");
    announce("Explorer reset to the Kansas demonstration view");
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
    setToolsExpanded(false);
    setMapQueryCandidates([]);
    const map = mapRef.current;
    if (map) {
      map.doubleClickZoom.disable();
      if (map.isStyleLoaded()) updateMeasurementSource(map, buildMeasurementData([], mode));
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
    window.history.replaceState(null, "", sharePath);
    try {
      await navigator.clipboard.writeText(shareUrl);
      announce(locationDerivedViewRef.current
        ? "Share link copied with the location-derived camera redacted"
        : `Share link copied with camera, layer order, opacity, time, projection, evidence state${analysisArea ? ", and analysis area" : ""}`);
    } catch {
      announce("Share state is in the address bar and ready to copy");
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
      renderer: { family: "MapLibre GL JS", site_package: "6.6.0", repository_runtime_proven: false },
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
      },
      repository_boundary: {
        snapshot: REPOSITORY_SNAPSHOT.commit,
        architecture: "ACCEPTED",
        dependency: "EXACT_6.6.0",
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
    const recordLimit = reportDetail === "EXECUTIVE" ? 8 : reportDetail === "STANDARD" ? 30 : reportRecords.length;
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
      title: reportTitle.trim() || "Kansas map data report",
      generatedAt,
      detail: reportDetail,
      scope: reportScope,
      filters: { query: reportQuery || null, mapEvidenceState: mapEvidenceFilter, evidenceState: reportEvidenceFilter, layerIds: reportLayerIds },
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
        center: locationCameraRedacted ? "WITHHELD_BROWSER_LOCATION" : view.center,
        camera: locationCameraRedacted
          ? { zoom: "WITHHELD", bearing: "WITHHELD", pitch: "WITHHELD" }
          : { zoom: view.zoom, bearing: view.bearing, pitch: view.pitch },
        representation: mapRepresentationLabel,
        scene: scenePreset,
        terrain: {
          state: terrainState,
          exaggeration: verticalExaggeration,
          sourceRole: "external DEM display context · not evidence",
          heightOverlay: {
            enabled: topographicOverlay,
            method: "MapLibre color-relief from the active raster-dem; cursor and locked readings query unexaggerated terrain elevation.",
            colorRampMeters: [200, 300, 400, 500, 650, 800, 1000, 1250],
            lockedReading: lockedTerrainElevation ? {
              elevationMeters: lockedTerrainElevation.meters,
              elevationFeet: lockedTerrainElevation.feet,
              coordinate: locationCameraRedacted ? "WITHHELD_BROWSER_LOCATION" : [lockedTerrainElevation.longitude, lockedTerrainElevation.latitude],
            } : null,
          },
        },
        projection,
        basemap,
        viewport: reportScope === "VIEWPORT" ? mapViewportBounds : null,
        analysisArea: reportScope === "ANALYSIS_AREA" ? analysisArea : null,
      },
      measurements: measurementGeometryMode ? {
        mode: measurementGeometryMode,
        unit: measureUnit,
        label: measurement,
        coordinates: locationCameraRedacted ? "WITHHELD_BROWSER_LOCATION" : measureCoordinatesRef.current.map(([longitude, latitude]) => [longitude, latitude] as [number, number]),
        approximation: "Browser-local screen measurement; not survey-grade or evidence.",
      } : null,
      selection: selected && !selectedTimeMismatch ? { id: selected.featureId, kind: selected.kind, title: selected.properties.title, layer: selected.layer.title, evidenceState: selected.properties.evidenceState, evidenceReference: selected.properties.citation, timeCompatible: true } : null,
      summary: reportSections.summary ? {
        matchedRecords: reportRecords.length,
        includedRecords: records.length,
        includedLayers: reportLayerSummary.length,
        evidenceStates: reportEvidenceCounts,
      } : null,
      findings: reportSections.findings ? reportFindings : null,
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
        "Current records are site-local synthetic or generalized demonstration data, not released operational KFM data.",
        "Map display, proximity, overlap, and screen measurement are not evidence or proof of a relationship.",
        "Any included measurement is a browser-local report input and remains approximate, not survey-grade.",
        "Basemap and terrain services are display context; their geometry and elevation values are not KFM evidence or source admission.",
        "Protected geometry is not reconstructed; location-derived camera coordinates remain withheld.",
        ...Array.from(new Set(records.map((record) => `${record.title}: ${record.generalization} ${record.uncertainty}`))),
      ] : null,
      attribution: [
        ...reportLayerSummary.map((layer) => ({ layer: layer.title, source: layer.attribution })),
        ...(topographicOverlay ? [{ layer: "Topographic height overlay", source: TERRAIN_SOURCES[0].attribution }] : []),
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
        ? `<section><h2>Terrain height overlay</h2><p><strong>Color relief:</strong> active, based on unexaggerated DEM elevation.</p>${lockedHeight ? `<p><strong>Locked reading:</strong> ${escapeReportHtml(lockedHeight.elevationFeet.toFixed(0))} ft / ${escapeReportHtml(lockedHeight.elevationMeters.toFixed(0))} m</p>` : "<p>No cursor elevation was locked for this report.</p>"}<p class="boundary">External display DEM. Confirm vertical datum, product version, and survey requirements before using this value as authoritative evidence.</p></section>`
        : "";
      content = `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${escapeReportHtml(report.title)}</title><style>body{font:15px/1.55 Inter,system-ui,sans-serif;color:#17201d;max-width:1100px;margin:0 auto;padding:48px}header{border-bottom:3px solid #b88b38;padding-bottom:22px;margin-bottom:28px}h1{font-size:36px;letter-spacing:-.04em;margin:0 0 8px}h2{margin-top:34px}small,.muted{color:#607069}.metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}.metric{border:1px solid #ccd6d1;padding:15px}.metric strong{display:block;font-size:24px}table{width:100%;border-collapse:collapse;font-size:13px}th,td{border-bottom:1px solid #dce3df;padding:10px;text-align:left;vertical-align:top}th{background:#f1f5f2}code{font-size:11px}li{margin:8px 0}.boundary{border-left:4px solid #b88b38;background:#f7f3ea;padding:14px 18px}@media print{body{padding:0}.boundary{break-inside:avoid}}@media(max-width:700px){body{padding:24px}.metrics{grid-template-columns:1fr 1fr}table{display:block;overflow:auto}}</style></head><body><header><small>KANSAS FRONTIER MATRIX · CUSTOM MAP REPORT</small><h1>${escapeReportHtml(report.title)}</h1><p>${escapeReportHtml(report.scope.replaceAll("_", " "))} · active time ${escapeReportHtml(report.activeTime.label)} · generated ${escapeReportHtml(generatedAt)}</p></header>${report.summary ? `<section><h2>Report summary</h2><div class="metrics"><div class="metric"><small>MATCHED RECORDS</small><strong>${report.summary.matchedRecords}</strong></div><div class="metric"><small>INCLUDED RECORDS</small><strong>${report.summary.includedRecords}</strong></div><div class="metric"><small>LAYERS</small><strong>${report.summary.includedLayers}</strong></div><div class="metric"><small>EVIDENCE STATES</small><strong>${Object.keys(report.summary.evidenceStates).length}</strong></div></div></section>` : ""}${findings.length ? `<section><h2>Findings</h2><ol>${findings.map((finding) => `<li>${escapeReportHtml(finding)}</li>`).join("")}</ol></section>` : ""}<section><h2>Time A / Time B catalog availability</h2><div class="metrics"><div class="metric"><small>TIME A</small><strong>${escapeReportHtml(formatTimelineStep(report.temporalComparison.timeA))}</strong><span>${report.temporalComparison.timeARecordCount} records</span></div><div class="metric"><small>TIME B</small><strong>${escapeReportHtml(formatTimelineStep(report.temporalComparison.timeB))}</strong><span>${report.temporalComparison.timeBRecordCount} records</span></div><div class="metric"><small>DELTA</small><strong>${report.temporalComparison.recordDelta >= 0 ? "+" : ""}${report.temporalComparison.recordDelta}</strong><span>catalog records</span></div><div class="metric"><small>CHANGED LAYERS</small><strong>${report.temporalComparison.changedLayerCount}</strong><span>under temporal rules</span></div></div><p class="boundary">Catalog availability only—not observed change, imagery analysis, causation, or proof of an event.</p></section>${records.length ? `<section><h2>Included records</h2><table><thead><tr><th>Record</th><th>Layer / time</th><th>Evidence</th><th>Summary</th></tr></thead><tbody>${records.map((record) => `<tr><td><strong>${escapeReportHtml(record.title)}</strong><br><code>${escapeReportHtml(record.id)}</code></td><td>${escapeReportHtml(record.layer)}<br>${escapeReportHtml(record.year)}</td><td>${escapeReportHtml(record.evidenceState)}<br><code>${escapeReportHtml(record.evidenceReference)}</code></td><td>${escapeReportHtml(record.summary)}</td></tr>`).join("")}</tbody></table></section>` : ""}${limitations.length ? `<section><h2>Limitations</h2><ul>${limitations.map((limitation) => `<li>${escapeReportHtml(limitation)}</li>`).join("")}</ul></section>` : ""}<section><h2>Attribution</h2><ul>${report.attribution.map((item) => `<li><strong>${escapeReportHtml(item.layer)}:</strong> ${escapeReportHtml(item.source)}</li>`).join("")}</ul></section><p class="boundary">This report is a browser-generated public-safe demonstration artifact. It does not release, publish, admit, or authorize KFM data.</p></body></html>`;
      if (heightSection) content = content.replace("<section><h2>Time A / Time B", `${heightSection}<section><h2>Time A / Time B`);
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

  return (
    <div className="site-root">
      <a className="skip-link" href="#map-canvas">Skip to the map</a>
      <header className="topbar">
        <div className="brand-lockup" aria-label="Kansas Frontier Matrix">
          <span className="mark" aria-hidden="true">KFM</span>
          <span><strong>Kansas Frontier Matrix</strong><small>Spatial evidence explorer</small></span>
        </div>
        <nav className="header-workflows" aria-label="Primary Explorer actions">
          <button type="button" title="Return focus to the map" aria-current={primaryWorkspace === "map" ? "page" : undefined} onClick={returnToPrimaryMap}><span aria-hidden="true">⌖</span>Map</button>
          <button type="button" title="Open the report workspace · shortcut R opens the map workbench report" aria-current={primaryWorkspace === "reports" ? "page" : undefined} onClick={() => openPrimaryWorkspace("reports")}>Reports</button>
          <button type="button" title="Open guided stories" aria-current={primaryWorkspace === "stories" ? "page" : undefined} onClick={() => openPrimaryWorkspace("stories")}>Stories</button>
        </nav>
        <div className="global-search">
          <label>
            <span className="sr-only">Search current places, layers, features, and official data sources</span>
            <span aria-hidden="true">⌕</span>
            <input ref={globalSearchInputRef} value={globalQuery} onChange={(event) => setGlobalQuery(event.target.value)} type="search" placeholder="Search places, layers, official data…" aria-describedby="global-search-help" title="Search · shortcut /" />
          </label>
          <span id="global-search-help" className="sr-only">Search results appear as keyboard-focusable buttons.</span>
          {globalQuery && <div className="search-results" id="global-search-results" aria-label="Search results">
            {searchResults.map((item) => <button type="button" key={item.id} onClick={() => chooseSearchResult(item)}><span>{item.kind}</span><strong>{item.title}</strong><small>{item.subtitle}</small></button>)}
            {searchResults.length === 0 && <p>No current place, layer, feature, or official source matches.</p>}
          </div>}
        </div>
        <div className="top-context" aria-label="Current map context">
          <span><small>AREA</small><strong>{selectedLabel}</strong></span>
          <span><small>TIME</small><strong>{temporalScopeLabel}</strong></span>
          <span className="release-indicator" data-selection-state={selected?.properties.evidenceState ?? "SOURCE_DATA"} title="Visible selection posture; not release or publication authority"><i /> {selected ? selectedEvidence?.label.toUpperCase() : visibleCount > 0 ? "EXAMPLES ACTIVE" : `DAILY BASELINE · ${baselineDay}`}</span>
        </div>
        <div className="top-actions">
          <DataNotices issues={OFFICIAL_CONTEXT_SOURCES.filter(source => officialVisibility[source.id] && officialStates[source.id] === "error").map(source => ({ id: source.id, title: source.shortTitle }))} onRetry={retryOfficialLayer} onHide={id => setOfficialContextVisible(id, false)} />
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
              <footer><span>DRAFT · NOT PUBLISHED</span><p>Site-local synthetic or generalized geometry remains distinct from official source candidates.</p></footer>
            </aside>}
          </div>
          <button ref={repositoryButtonRef} className="status-header-action" type="button" onClick={() => { setRepositoryView("updates"); setRepositoryOpen(true); }} aria-expanded={repositoryOpen} aria-controls="repository-briefing" title="Check Site, data, and repository connections"><span aria-hidden="true">⌁</span><span>Status</span></button>
          <button className="qwen-header-action" type="button" onClick={openQwenCompanion} aria-pressed={qwenOpen} title="Ask Qwen about the current map view"><span className="qwen-glyph" aria-hidden="true">Q</span><span>Qwen</span></button>
          <button className="share-action" type="button" onClick={shareView} aria-label="Share current map view" title="Share current view">↗</button>
          <Link className="about-action" href="/about">About</Link>
        </div>
        <nav className="mobile-primary-tabs" aria-label="Primary Explorer workspaces">
          <button type="button" aria-current={primaryWorkspace === "map" ? "page" : undefined} onClick={returnToPrimaryMap}>Map</button>
          <button type="button" aria-current={primaryWorkspace === "reports" ? "page" : undefined} onClick={() => openPrimaryWorkspace("reports")}>Reports</button>
          <button type="button" aria-current={primaryWorkspace === "stories" ? "page" : undefined} onClick={() => openPrimaryWorkspace("stories")}>Stories</button>
        </nav>
        {helpOpen && <aside className="map-guide" role="dialog" aria-modal="false" aria-label="Map guide">
          <button className="icon-close" type="button" onClick={() => setHelpOpen(false)} aria-label="Close map guide">×</button>
          <p className="panel-kicker">MAP GUIDE</p><h2>Explore a feature, then check what supports it.</h2>
          <p>Every layer in this build uses site-local synthetic or generalized demonstration data—not released operational data. Choose an example or select any feature to inspect its evidence state.</p>
          <div className="map-guide-actions"><button className="map-guide-start" type="button" onClick={showGuidedStart}>Try quick examples</button><button className="map-guide-start" type="button" onClick={startStoryTrail}>Start four-step story</button></div>
          <ol><li>Search, choose an example, or enable a layer.</li><li>Select a feature.</li><li>Inspect what is supported, missing, corrected, or withheld.</li><li>Review time, lineage, and Focus Mode when you need more detail.</li></ol>
          <p><strong>Shift + drag</strong> uses MapLibre box zoom. The Map Workbench also supports coordinate navigation, camera orientation, and viewport-scoped feature discovery. Terrain uses an external display DEM when available. Synchronized comparison shows bounded layer fixtures; neither display is an admitted KFM source.</p>
        </aside>}
      </header>

      {primaryWorkspace !== "map" && workspaceSnapshot && <ReportStoryWorkspaces
        key={workspaceSnapshot.id}
        mode={primaryWorkspace}
        snapshot={workspaceSnapshot}
        evidenceRecords={allEvidenceRecords}
        onModeChange={(mode) => setPrimaryWorkspace(mode)}
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
              <div><dt>Current signals</dt><dd>{REPOSITORY_SNAPSHOT.counts.repositoryUpdates}</dd></div>
            </dl>
            <div className="site-identity-strip" aria-label="Site identity and domain status">
              <div>
                <span>SITES BINDING</span>
                <strong>{SITE_IDENTITY.provider}</strong>
                <small>{SITE_IDENTITY.slug} · {SITE_IDENTITY.projectId}</small>
              </div>
              <div>
                <span>CANONICAL HOST</span>
                <a href={SITE_IDENTITY.canonicalUrl} target="_blank" rel="noreferrer">{SITE_IDENTITY.canonicalUrl.replace("https://", "")}</a>
                <small>{SITE_IDENTITY.customDomainStatus.replaceAll("_", " ")} · checked {SITE_IDENTITY.checkedAt}</small>
              </div>
              <div data-state="warning">
                <span>REPOSITORY IDENTITY</span>
                <strong>{SITE_IDENTITY.sourceRelation.replaceAll("_", " ")}</strong>
                <small>GitHub child manifest still names {SITE_IDENTITY.repositoryManifestProjectId}; this Site binding is authoritative.</small>
              </div>
            </div>
            <div className="repository-connection" data-state={repositoryConnection.state} role="status" aria-live="polite">
              <div>
                <span>LIVE READ-ONLY GITHUB CHECK</span>
                <strong>{repositoryConnection.state === "ready" ? `main@${repositoryConnection.shortCommit}` : repositoryConnection.state === "loading" ? "Checking current main…" : repositoryConnection.state === "error" ? "Live check unavailable" : "Check available"}</strong>
                <p>{repositoryConnection.state === "ready"
                  ? repositoryConnection.liveCommit === REPOSITORY_SNAPSHOT.commit
                    ? "GitHub main matches the Site reference snapshot."
                    : `GitHub main has advanced; this Site remains referenced to main@${REPOSITORY_SNAPSHOT.shortCommit}.`
                  : repositoryConnection.state === "error"
                    ? "The pinned snapshot remains available; no currentness claim is inferred."
                    : "Reads fixed public repository metadata only when this briefing opens."}</p>
              </div>
              <button type="button" onClick={() => setRepositoryRefreshKey((current) => current + 1)} disabled={repositoryConnection.state === "loading"}>Refresh</button>
              {repositoryConnection.state === "ready" && <small>{repositoryConnection.message ?? "Current main commit"}{repositoryConnection.observedAt ? ` · checked ${new Date(repositoryConnection.observedAt).toLocaleString()}` : ""}</small>}
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
                  <label><span className="sr-only">Filter repository features by area</span><select value={featureArea} onChange={(event) => setFeatureArea(event.target.value as FeatureArea | "ALL")}><option value="ALL">All areas</option>{FEATURE_AREAS.map((area) => <option key={area} value={area}>{area}</option>)}</select></label>
                  <label><span className="sr-only">Filter repository features by maturity</span><select value={featureMaturity} onChange={(event) => setFeatureMaturity(event.target.value as FeatureMaturity | "ALL")}><option value="ALL">All maturity states</option><option value="VERIFIED_SLICE">Verified slice</option><option value="FIXTURE_FIRST">Fixture first</option><option value="DOCUMENTED">Documented</option><option value="HOLD">Hold</option></select></label>
                  <span>{filteredFeatures.length} of {FEATURE_CATALOG.length}</span>
                </div>
                <div className="feature-radar-grid">
                  {filteredFeatures.map((feature) => <article key={feature.id} data-state={feature.maturity}><span>{featureMaturityLabel(feature.maturity)}</span><small>{feature.area}</small><strong>{feature.name}</strong><p>{feature.summary}</p><a href={`https://github.com/${REPOSITORY_SNAPSHOT.repository}/tree/${REPOSITORY_SNAPSHOT.commit}/${feature.path}`} target="_blank" rel="noreferrer">Open source ↗</a></article>)}
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
                    <h4>{source.title}</h4><p className="source-organization">{source.organization} · {source.cadence} · official portal checked <time dateTime={source.checkedAt}>8 Sep 2026</time></p>
                    <dl><div><dt>Source role</dt><dd>{source.sourceRole}</dd></div><div><dt>Candidate value</dt><dd>{source.value}</dd></div><div><dt>Cannot prove</dt><dd>{source.cannotProve}</dd></div><div><dt>Next gate</dt><dd>{source.nextGate}</dd></div></dl>
                    <div className="source-modes">{source.dataModes.map((mode) => <span key={mode}>{mode}</span>)}</div>
                    <footer><a href={source.sourceUrl} target="_blank" rel="noreferrer">Open official source ↗</a><button type="button" onClick={() => copySourceIntakeDraft(source)}>Copy bounded intake draft</button>{source.layerId && source.featureId && <button type="button" onClick={() => { setRepositoryOpen(false); selectStoredFeature(source.layerId!, source.featureId!); }}>Inspect local analogue</button>}</footer>
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
              <p>This briefing reports inspected repository bytes. Map geometry remains clearly labeled site-local demonstration content unless a layer record says otherwise. A merge, test, receipt, or renderer does not itself release or publish KFM data.</p>
            </aside>
          </div>
        </aside>
      </div>

      <main inert={primaryWorkspace !== "map"} className="explorer-shell" data-left={leftOpen} data-right={rightOpen} data-timeline={timelineOpen}>
        <aside ref={leftPanelRef} className="layer-panel" data-panel-mode={leftPanelMode} aria-label="Living Atlas navigation" aria-hidden={!leftOpen} inert={!leftOpen} aria-modal={isCompact && leftOpen || undefined} role={isCompact && leftOpen ? "dialog" : undefined}>
          <div className="panel-heading">
            <div><p className="panel-kicker">{leftPanelMode === "views" ? "LIVING ATLAS" : leftPanelMode === "layers" ? "LAYER CATALOG" : leftPanelMode === "places" ? "PLACES" : "STORY ATLAS"}</p><h1>{leftPanelMode === "views" ? "Investigate Kansas" : leftPanelMode === "layers" ? "Layer Catalog" : leftPanelMode === "places" ? "Places + trails" : "Guided stories"}</h1></div>
            <button className="icon-close" type="button" onClick={closeLeftPanel} aria-label="Close Explorer navigation">×</button>
          </div>
          <p className="panel-intro">{leftPanelMode === "views" ? "Start from a named question, then inspect the map, time, evidence, and report together." : leftPanelMode === "layers" ? "Start with real Kansas sources. Adjust each layer here, download its data, or propose an update for review." : leftPanelMode === "places" ? "Save complete, device-local investigations and revisit them as a trail." : "Pause on a site-local chapter, inspect its evidence state, and keep the boundary visible."}</p>
          <Link className="event-sidebar-link" href="/observatory">Event Observatory · 24-hour archive calendar, radar, smoke & rivers ↗</Link>
          <nav className="left-panel-tabs" aria-label="Living Atlas sections">
            <button type="button" aria-current={leftPanelMode === "views" ? "page" : undefined} data-active={leftPanelMode === "views"} onClick={() => setLeftPanelMode("views")}>Views <b>{LIVING_ATLAS_VIEWS.length}</b></button>
            <button type="button" aria-current={leftPanelMode === "layers" ? "page" : undefined} data-active={leftPanelMode === "layers"} onClick={() => setLeftPanelMode("layers")}>Layers <b>{visibleOfficialCount}/{OFFICIAL_CONTEXT_SOURCES.length}</b></button>
            <button type="button" aria-current={leftPanelMode === "places" ? "page" : undefined} data-active={leftPanelMode === "places"} onClick={() => setLeftPanelMode("places")}>Places <b>{savedWorkspaces.length}</b></button>
            <button type="button" aria-current={leftPanelMode === "stories" ? "page" : undefined} data-active={leftPanelMode === "stories"} onClick={() => setLeftPanelMode("stories")}>Stories <b>1</b></button>
          </nav>

          <section className="atlas-view-library" hidden={leftPanelMode !== "views"} aria-labelledby="atlas-view-library-title">
            <div className="atlas-library-heading"><div><span className="panel-kicker">DEFAULT INVESTIGATIONS</span><h2 id="atlas-view-library-title">Choose a starting question</h2></div><small>{filteredAtlasViews.length} of {LIVING_ATLAS_VIEWS.length}</small></div>
            <label className="atlas-search-control"><span aria-hidden="true">⌕</span><span className="sr-only">Search Living Atlas views</span><input type="search" value={atlasViewQuery} onChange={(event) => setAtlasViewQuery(event.target.value)} placeholder="Search questions, domains, or time" /></label>
            <div className="atlas-view-list">
              {filteredAtlasViews.map((atlasView) => <article className="atlas-view-card" key={atlasView.id} data-status={atlasView.status} data-active={atlasView.profileId === activeViewProfileId}>
                <header><span>{livingAtlasStatusLabel(atlasView.status)}</span><small>{atlasView.display}</small></header>
                <h3>{atlasView.title}</h3>
                <p className="atlas-view-question">{atlasView.question}</p>
                <dl><div><dt>Scope</dt><dd>{atlasView.scope}</dd></div><div><dt>Time</dt><dd>{atlasView.time}</dd></div><div><dt>Source posture</dt><dd>{atlasView.sourcePosture}</dd></div></dl>
                <div className="atlas-view-domains" aria-label={`${atlasView.title} domains`}>{atlasView.domains.map((domain) => <span key={domain}>{domain}</span>)}</div>
                <p className="atlas-view-note">{atlasView.note}</p>
                <footer><span>{atlasView.report}</span><button type="button" disabled={atlasView.status === "DESIGN_HOLD"} onClick={() => applyLivingAtlasView(atlasView)}>{atlasView.status !== "DESIGN_HOLD" ? atlasView.story ? "Start story" : "Open on map" : "Data binding held"}</button></footer>
              </article>)}
              {filteredAtlasViews.length === 0 && <div className="catalog-empty"><strong>No matching investigations</strong><p>Try a place, domain, time, or question.</p></div>}
            </div>
            <aside className="panel-boundary-note"><strong>Named view ≠ admitted data</strong><p>These cards make the proposed Living Atlas inventory useful without claiming that a held source, live service, or production geography is loaded.</p></aside>
          </section>

          <section className="panel-mode-placeholder" hidden={leftPanelMode !== "places"} aria-labelledby="places-panel-title">
            <div className="panel-mode-heading"><span className="panel-kicker">DEVICE-LOCAL WORKSPACES</span><h2 id="places-panel-title">Return to an investigation</h2></div>
            <p>Places stores camera, time, layers, comparison, report setup, and selected evidence on this device only.</p>
            <div className="panel-stat-grid"><article><span>SAVED PLACES</span><strong>{savedWorkspaces.length}</strong></article><article><span>ACTIVE PLACE</span><strong>{activePlaceId ? "YES" : "NONE"}</strong></article></div>
            <button className="panel-mode-primary" type="button" onClick={(event) => openMapUtility("places", event.currentTarget)}>Open Places + trails</button>
            <p className="panel-mode-note">A saved workspace is a reproducible map state, not a source release or public publication.</p>
          </section>

          <section className="panel-mode-placeholder" hidden={leftPanelMode !== "stories"} aria-labelledby="stories-panel-title">
            <div className="panel-mode-heading"><span className="panel-kicker">PAUSED CHAPTERS</span><h2 id="stories-panel-title">Story Atlas</h2></div>
            <p>A four-step site-local trust story connects a place, a declared time, a feature, and its evidence state. It never upgrades fixture data into a release.</p>
            <button className="panel-mode-primary" type="button" onClick={startStoryTrail}>Start four-step story</button>
            <div className="story-mode-steps"><span>01 · County locator</span><span>02 · Water context</span><span>03 · Time boundary</span><span>04 · Evidence outcome</span></div>
          </section>

          <div className="layer-catalog-body" hidden={leftPanelMode !== "layers"}>
          <label className="catalog-search"><span aria-hidden="true">⌕</span><span className="sr-only">Search Layer Catalog</span><input type="search" value={layerQuery} onChange={(event) => setLayerQuery(event.target.value)} placeholder="Filter layers and datasets" /></label>

          <details className="legacy-layer-index"><summary>Legacy examples & diagnostics</summary><p>These older interaction examples are separate from today’s real source baseline.</p>
          <section className="active-layers" aria-labelledby="active-title">
            <div className="section-row"><h2 id="active-title">Active local layers <span>{visibleCount}/{LAYER_REGISTRY.length}</span></h2><div className="active-layer-actions"><button type="button" onClick={() => { setVisibility(defaultVisibility); setOpacity(defaultOpacity); }}>Reset defaults</button><button type="button" onClick={() => setVisibility(Object.fromEntries(LAYER_REGISTRY.map((layer) => [layer.id, false])))}>Hide all</button></div></div>
            <div className="active-chips">{activeLayers.map((layer) => <button key={layer.id} type="button" onClick={() => zoomToLayer(layer)}>{layer.title}<span>↗</span></button>)}</div>
          </section>

          <nav className="catalog-section-jump" aria-label="Layer Catalog shortcuts">
            <a href="#catalog-layer-stack"><span>Legacy examples</span><b>Optional controls</b></a>
            <a href="#official-context-catalog"><span>Real data layers</span><b>{OFFICIAL_CONTEXT_SOURCES.length} connections</b></a>
            <a href="#catalog-domain-index-title"><span>All domains</span><b>{CATEGORY_ORDER.length} layer groups</b></a>
            <a href="#priority-context-title"><span>Priority context</span><b>Earthquake · water · smoke</b></a>
            <a href="#official-context-catalog"><span>All source controls</span><b>{OFFICIAL_CONTEXT_SOURCES.length} connections</b></a>
          </nav>

          <section className="catalog-domain-index" aria-labelledby="catalog-domain-index-title">
            <div className="section-row"><h2 id="catalog-domain-index-title">All layer domains <span>{LAYER_REGISTRY.length} layers</span></h2><small>Jump to a complete group</small></div>
            <div className="catalog-domain-grid">
              {CATEGORY_ORDER.map((category) => {
                const categoryLayers = LAYER_REGISTRY.filter((layer) => layer.category === category);
                const activeCategoryCount = categoryLayers.filter((layer) => visibility[layer.id]).length;
                return <button key={category} type="button" data-active={activeCategoryCount > 0} onClick={() => {
                  setLayerDomain("ALL");
                  setLayerQuery("");
                  window.requestAnimationFrame(() => document.getElementById(`catalog-category-${catalogCategorySlug(category)}`)?.scrollIntoView({ behavior: reducedMotion ? "auto" : "smooth", block: "start" }));
                }} aria-label={`Show ${category}: ${activeCategoryCount} of ${categoryLayers.length} active`}>
                  <strong>{category}</strong><small>{activeCategoryCount}/{categoryLayers.length} active</small>
                </button>;
              })}
            </div>
            <p>These are the site-local demonstration layers. Official live context—earthquakes, gauges, smoke, radar, watersheds, and terrain—is kept in the separate source-controls section below.</p>
          </section>

          </details>
          <section className="official-context-catalog" id="official-context-catalog" aria-labelledby="official-context-title">
            <header><div><span>OFFICIAL OPERATIONAL CONTEXT</span><h2 id="official-context-title">Real Kansas source connections</h2><small className="official-context-registry-summary">{SITE_REGISTRY_COUNTS.features} features · {SITE_REGISTRY_COUNTS.connections} connections · {SITE_REGISTRY_COUNTS.actions} actions</small></div><strong>{withheldOfficialCount > 0 ? `${visibleOfficialCount} SELECTED · HELD` : `${visibleOfficialCount}/${OFFICIAL_CONTEXT_SOURCES.length} ON`}</strong></header>
            <p>Live and current official sources may be drawn for orientation. They stay outside KFM admission, reports, exports, and EvidenceBundles.</p>
            <div className="official-context-pulse" aria-label="Official data connection status">
              <div><span><small>LOADED FEATURES</small><strong>{officialFeatureCount.toLocaleString("en-US")}</strong></span><span><small>CONNECTIONS</small><strong>{officialReadyCount}/{OFFICIAL_CONTEXT_SOURCES.length} checked</strong></span><span><small>LAST RETRIEVAL</small><strong>{officialLatestRetrievedAt ? new Date(officialLatestRetrievedAt).toLocaleTimeString([], { hour: "numeric", minute: "2-digit" }) : "Not yet"}</strong></span></div>
              <nav aria-label="Official data actions"><button type="button" disabled={visibleRefreshableOfficialCount === 0 || officialLoadingCount > 0} onClick={refreshVisibleOfficialContext}>{officialLoadingCount > 0 ? "Refreshing…" : "Refresh visible"}</button><button type="button" disabled={visibleOfficialCount === 0} onClick={hideAllOfficialContext}>Hide all</button></nav>
            </div>
            <details className="source-layer-groups"><summary>Layer groups · earthquakes, water & smoke</summary><section className="priority-context-deck" aria-labelledby="priority-context-title">
              <header>
                <div><span>PRIORITY CONNECTIONS</span><h3 id="priority-context-title">Earthquakes, water + smoke</h3></div>
                <small>Toggle a source directly</small>
              </header>
              <p className="priority-context-intro">The controls below keep the most actionable map connections visible. Open a source row for opacity, freshness, limits, and provider links.</p>
              <div className="priority-context-groups">
                {PRIORITY_CONTEXT_GROUPS.map((group) => {
                  const visibleSources = group.sourceIds.filter((sourceId) => officialVisibility[sourceId]);
                  const featureCount = group.sourceIds.reduce((total, sourceId) => total + (officialPayloads[sourceId as OfficialContextFeedId]?.featureCount ?? 0), 0);
                  const allVisible = visibleSources.length === group.sourceIds.length;
                  return <article className="priority-context-group" key={group.id} data-active={visibleSources.length > 0}>
                    <header>
                      <div><strong>{group.title}</strong><small>{visibleSources.length}/{group.sourceIds.length} selected{featureCount > 0 ? ` · ${featureCount.toLocaleString("en-US")} loaded` : ""}</small></div>
                      <span>{allVisible ? "FULL" : visibleSources.length ? "PARTIAL" : "OFF"}</span>
                    </header>
                    <p>{group.description}</p>
                    <div className="priority-context-source-list">
                      {group.sourceIds.map((sourceId) => {
                        const source = OFFICIAL_CONTEXT_BY_ID[sourceId];
                        const state = officialStates[sourceId];
                        const heldAtFrame = officialVisibility[sourceId] && !effectiveOfficialVisibility[sourceId];
                        return <button
                          className="priority-context-source"
                          key={sourceId}
                          type="button"
                          aria-pressed={officialVisibility[sourceId]}
                          data-active={officialVisibility[sourceId]}
                          data-state={state}
                          onClick={() => setOfficialContextVisible(sourceId, !officialVisibility[sourceId])}
                          title={`${officialVisibility[sourceId] ? "Hide" : "Show"} ${source.title}`}
                        >
                          <i aria-hidden="true" />
                          <span><strong>{source.shortTitle}</strong><small>{heldAtFrame ? "HELD" : officialContextStateLabel(state)}</small></span>
                        </button>;
                      })}
                    </div>
                    <footer>
                      <button type="button" onClick={() => setPriorityContextGroupVisible(group.sourceIds, true)} disabled={allVisible}>Show all</button>
                      <button type="button" onClick={() => setPriorityContextGroupVisible(group.sourceIds, false)} disabled={visibleSources.length === 0}>Hide all</button>
                    </footer>
                  </article>;
                })}
              </div>
            </section></details>
            <div className="official-context-list">{OFFICIAL_CONTEXT_SOURCES.map((source) => {
              const payload = source.apiPath || source.managedAdapterPath ? officialPayloads[source.id as OfficialContextFeedId] : undefined;
              const state = officialStates[source.id];
              const heldAtFrame = officialVisibility[source.id] && !effectiveOfficialVisibility[source.id];
              return <article key={source.id} className="official-context-row" data-state={state} data-visible={officialVisibility[source.id]} data-held={heldAtFrame}>
                <div className="official-context-primary"><label className="visibility-switch"><input type="checkbox" checked={officialVisibility[source.id]} aria-label={`${officialVisibility[source.id] ? "Hide" : "Show"} ${source.title}`} onChange={(event) => setOfficialContextVisible(source.id, event.target.checked)} /><span aria-hidden="true" /></label><i style={{ "--swatch": source.color } as React.CSSProperties} /><div><strong>{source.shortTitle}</strong><small>{source.organization}{heldAtFrame ? ` · held until ${formatTimelineStep(OFFICIAL_CONTEXT_PRESENT_FRAME)}` : ""}</small></div><b>{heldAtFrame ? "HELD" : state.toUpperCase()}</b></div>
                <label className="opacity-control"><span>Opacity <b>{Math.round(officialOpacity[source.id] * 100)}%</b></span><input aria-label={`${source.shortTitle} opacity`} type="range" min="0" max="100" value={Math.round(officialOpacity[source.id] * 100)} onChange={(event) => setOfficialContextOpacity(source.id, Number(event.target.value) / 100)} /></label>
                <div className="official-context-actions"><button type="button" onClick={() => { setSourceStatusOpen(true); setLeftOpen(false); }}>Source details & quality</button>{["usgs-streamflow", "noaa-hms-smoke", "raspberry-shake-stations", "usgs-earthquakes", "nws-radar", "census-counties"].includes(source.id) && <Link href={`/observatory?layers=${({ "usgs-streamflow": "river", "noaa-hms-smoke": "smoke", "raspberry-shake-stations": "shake", "usgs-earthquakes": "earthquakes", "nws-radar": "radar", "census-counties": "counties" } as Record<string,string>)[source.id]},counties`}>Explore dated records ↗</Link>}</div>
              </article>;
            })}</div>
            <footer><code>OFFICIAL SOURCE → FIXED ADAPTER / WMS → MAPLIBRE</code><span>Evidence held at admission, release, and EvidenceBundle gates · <a href="https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3393" target="_blank" rel="noreferrer">governance issue #3393 ↗</a></span></footer>
          </section>

          <section className="catalog-quick-lenses" aria-labelledby="quick-lenses-title">
            <div className="section-row"><h2 id="quick-lenses-title">Quick lenses</h2><span>Layers + time + style</span></div>
            <div>{MAP_VIEW_PROFILES.map((profile) => <button key={profile.id} type="button" aria-pressed={activeViewProfileId === profile.id} onClick={() => applyViewProfile(profile)}><strong>{profile.title}</strong><small>{profile.visibleLayerIds.length} layers · {profile.year}</small></button>)}</div>
          </section>

          <div className="basemap-control">
            <div className="catalog-filter-grid"><label><span>Basemap style</span><select value={basemap} onChange={(event) => setBasemap(event.target.value as BasemapKey)}>{(Object.keys(BASEMAPS) as BasemapKey[]).map((key) => <option key={key} value={key}>{BASEMAPS[key].title} · {BASEMAPS[key].note}</option>)}</select></label><label><span>Domain filter</span><select value={layerDomain} onChange={(event) => setLayerDomain(event.target.value as (typeof layerDomains)[number])}>{layerDomains.map((domain) => <option key={domain} value={domain}>{domain === "ALL" ? "All domains" : domain}</option>)}</select></label></div>
            <div className="catalog-evidence-filter"><label><span>Map evidence filter</span><select value={mapEvidenceFilter} onChange={(event) => updateMapEvidenceFilter(event.target.value as RegistryEvidenceFilter)}><option value="ALL">All evidence states</option>{(Object.keys(evidenceLabels) as EvidenceState[]).map((state) => <option key={state} value={state}>{state.replaceAll("_", " ")}</option>)}</select></label><output>{mapCompatibleFeatureCount} compatible records</output>{mapEvidenceFilter !== "ALL" && <button type="button" onClick={() => updateMapEvidenceFilter("ALL")}>Clear filter</button>}</div>
            <div className="catalog-filter-actions"><span>{layerQuery.trim() || layerDomain !== "ALL" || mapEvidenceFilter !== "ALL" ? "Catalog filters are active" : "Showing every local domain"}</span><button type="button" disabled={!layerQuery.trim() && layerDomain === "ALL" && mapEvidenceFilter === "ALL"} onClick={() => { setLayerQuery(""); setLayerDomain("ALL"); updateMapEvidenceFilter("ALL"); }}>Clear filters</button></div>
          </div>

          <details className="legacy-layer-index"><summary>Legacy example layer controls · {visibleCount} on</summary>
          <section className="catalog-layer-stack" id="catalog-layer-stack" aria-labelledby="catalog-layer-stack-title">
            <div className="section-row"><h2 id="catalog-layer-stack-title">Registered layers <span>{filteredLayerIds.size}/{LAYER_REGISTRY.length}</span></h2><div className="catalog-layer-stack-actions"><button type="button" disabled={filteredLayerIds.size === 0} onClick={() => setLayerGroupVisibility(Array.from(filteredLayerIds), true)}>Show all</button><button type="button" disabled={filteredLayerIds.size === 0} onClick={() => setLayerGroupVisibility(Array.from(filteredLayerIds), false)}>Hide all</button></div></div>
            <p>Every site-local layer remains available below. Toggle visibility directly or open a row for opacity, features, zoom, and draw order.</p>
          </section>

          <div className="catalog-groups">
            {CATEGORY_ORDER.map((category) => {
              const categoryLayers = LAYER_REGISTRY.filter((layer) => layer.category === category);
              const layers = layerOrder.map((id) => LAYER_REGISTRY.find((layer) => layer.id === id)).filter((layer): layer is LayerRecord => Boolean(layer && layer.category === category && filteredLayerIds.has(layer.id)));
              if (!layers.length) return null;
              return <section className="catalog-group" key={category} id={`catalog-category-${catalogCategorySlug(category)}`} aria-labelledby={`catalog-category-${catalogCategorySlug(category)}-title`}><header className="catalog-group-heading"><h2 id={`catalog-category-${catalogCategorySlug(category)}-title`}>{category} <span>{layers.length}/{categoryLayers.length}</span></h2><div><button type="button" onClick={() => setLayerGroupVisibility(layers.map((layer) => layer.id), true)}>Show all</button><button type="button" onClick={() => setLayerGroupVisibility(layers.map((layer) => layer.id), false)}>Hide all</button></div></header>{layers.map((layer) => {
                const noData = Boolean(layer.temporal && !layer.data.features.some((feature) => isFeatureAvailableForTemporalQuery(layer, feature.properties.year, temporalQuery)));
                const expanded = expandedLayers.has(layer.id);
                return <article className="layer-row" key={layer.id} data-active={visibility[layer.id]} data-state={sourceStates[layer.id]}>
                  <div className="layer-primary">
                    <label className="visibility-switch"><input type="checkbox" aria-label={`${visibility[layer.id] ? "Hide" : "Show"} ${layer.title}`} checked={visibility[layer.id]} onChange={(event) => setVisibility((current) => ({ ...current, [layer.id]: event.target.checked }))} /><span aria-hidden="true" /></label>
                    <i className={`legend-swatch ${layer.legend[0].shape}`} style={{ "--swatch": layer.legend[0].color } as React.CSSProperties} aria-hidden="true" />
                    <button className="layer-title" type="button" onClick={() => setExpandedLayers((current) => { const next = new Set(current); if (next.has(layer.id)) next.delete(layer.id); else next.add(layer.id); return next; })} aria-expanded={expanded} title={`${expanded ? "Hide" : "Show"} controls for ${layer.title}`}><strong>{layer.title}</strong><small>{noData ? `No ${layer.temporal?.label.toLowerCase()} data for ${temporalScopeLabel}` : `${layer.releaseState} · ${layer.releaseTime}`}</small><em>{expanded ? "Hide controls" : "Controls"} <span aria-hidden="true">{expanded ? "⌃" : "⌄"}</span></em></button>
                    <span className={`trust-badge state-${layer.releaseState.toLowerCase()}`}>{layer.releaseState}</span>
                  </div>
                  <label className="opacity-control layer-direct-opacity"><span>Opacity <b>{Math.round((opacity[layer.id] ?? layer.defaultOpacity) * 100)}%</b></span><input type="range" min="0" max="100" value={Math.round((opacity[layer.id] ?? layer.defaultOpacity) * 100)} aria-label={`${layer.title} opacity`} onChange={(event) => setOpacity((current) => ({ ...current, [layer.id]: Number(event.target.value) / 100 }))} /></label>
                  {expanded && <div className="layer-detail">
                    <p>{layer.description}</p>
                    <dl><div><dt>Format</dt><dd>{layer.sourceType}</dd></div><div><dt>Scale</dt><dd>{layer.scaleNote}</dd></div><div><dt>Time</dt><dd>{layer.validTimeExtent}</dd></div><div><dt>Freshness</dt><dd>{layer.freshnessState}</dd></div></dl>
                    <label className="opacity-control"><span>Opacity <b>{Math.round((opacity[layer.id] ?? layer.defaultOpacity) * 100)}%</b></span><input type="range" min="10" max="100" value={Math.round((opacity[layer.id] ?? layer.defaultOpacity) * 100)} onChange={(event) => setOpacity((current) => ({ ...current, [layer.id]: Number(event.target.value) / 100 }))} /></label>
                    <div className="layer-actions"><button type="button" onClick={() => zoomToLayer(layer)}>Zoom</button><button type="button" onClick={(event) => inspectLayer(layer, event.currentTarget)}>Features</button><button type="button" onClick={() => isolateLayer(layer)}>Solo</button><button type="button" onClick={() => moveLayer(layer.id, -1)} aria-label={`Move ${layer.title} down in draw order`}>↓</button><button type="button" onClick={() => moveLayer(layer.id, 1)} aria-label={`Move ${layer.title} up in draw order`}>↑</button></div>
                    <p className="layer-note">{layer.sensitivityNote}</p>
                  </div>}
                </article>;
              })}</section>;
            })}
            {layerDomain !== "ALL" && DOMAIN_HOLDS.some((hold) => hold.domain === layerDomain) && <section className="catalog-domain-hold" aria-label={`${layerDomain} readiness`}><header><span>{layerDomain}</span><strong>{DOMAIN_HOLDS.find((hold) => hold.domain === layerDomain)?.state}</strong></header><p>{DOMAIN_HOLDS.find((hold) => hold.domain === layerDomain)?.detail}</p><small>Map context, if visible from a basemap, is not an admitted KFM layer. Use the Sources and About surfaces for the current boundary.</small></section>}
            {filteredLayerIds.size === 0 && <div className="catalog-empty"><strong>No layers found</strong><p>Try a domain, dataset, or geometry term.</p></div>}
          </div>

          </details>
          <div className="panel-footer-actions"><button type="button" onClick={resetExplorer}>Reset map</button><Link href="/data">Propose a dataset</Link></div>
          </div>
        </aside>

        <section className="map-stage" data-live-dock={liveDockVisible} data-radar-loop={showRadarDock} aria-label="Kansas MapLibre Explorer">
          <div className="mission-band map-command-bar">
            <div className="map-command-identity">
              <span className="map-command-eyebrow">ACTIVE INVESTIGATION</span>
              <strong>{activeAtlasView?.title ?? activeViewProfile?.title ?? "Custom map view"}</strong>
              <small>{activeAtlasView?.question ?? activeViewProfile?.summary ?? "Inspect the current map state."}</small>
            </div>
            <div className="map-command-facts" aria-label="Current investigation context">
              <span><small>SCOPE</small><b>{selected?.properties.title ?? activeAtlasView?.scope ?? "Kansas statewide"}</b></span>
              <span><small>TIME</small><b>{temporalScopeLabel}</b></span>
              <span><small>LAYERS</small><b>{visibleCount} registry · {visibleOfficialCount} context</b></span>
            </div>
            <div className="map-command-status">
              <span data-runtime={runtime.kind}><i /> {runtime.kind === "ready" ? "MAP READY" : runtime.kind === "loading" ? "MAP STARTING" : runtime.kind === "degraded" ? "MAP DEGRADED" : runtime.kind === "unsupported" ? "MAP UNSUPPORTED" : "MAP UNAVAILABLE"}</span>
              <small>{BASEMAPS[basemap].title} · {mapRepresentationLabel}</small>
            </div>
            <div className="map-command-actions"><Link className="event-entry-link" href="/observatory">24-hour archive ↗</Link><button type="button" onClick={() => openAtlasPanel("layers")}>Layers</button><button type="button" onClick={openLiveContextCatalog}>Live data</button><button type="button" onClick={() => openMapUtility("navigate")}>Map controls</button><button type="button" onClick={saveCurrentWorkspace}>Save view</button><button type="button" onClick={() => openPrimaryWorkspace("reports", true)}>Build report</button></div>
          </div>
          <nav className="map-view-mode-strip" aria-label="Map representation">
            <span className="map-view-mode-heading">MAP REPRESENTATION <small>{mapRepresentationLabel}</small></span>
            <button type="button" aria-pressed={projection === "mercator" && scenePreset !== "elevation-3d"} data-active={projection === "mercator" && scenePreset !== "elevation-3d"} onClick={() => activateMapRepresentation("2d")}><b>2D</b><span>Map</span></button>
            <button type="button" aria-pressed={scenePreset === "elevation-3d"} data-active={scenePreset === "elevation-3d"} onClick={() => activateMapRepresentation("terrain")}><b>Terrain 3D</b><span>{verticalExaggeration.toFixed(1)}×</span></button>
            <button type="button" aria-pressed={projection === "globe"} data-active={projection === "globe"} onClick={() => activateMapRepresentation("globe")}><b>Globe</b><span>◎</span></button>
            <button type="button" aria-pressed={mapUtilityOpen && mapUtilityView === "compare"} data-active={mapUtilityOpen && mapUtilityView === "compare"} onClick={() => mapUtilityOpen && mapUtilityView === "compare" ? closeMapUtility() : activateMapRepresentation("compare")}><b>Compare</b><span>A/B</span></button>
            <TerrainQuickControls active={scenePreset === "elevation-3d"} state={terrainState} exaggeration={verticalExaggeration} lighting={atmospherePreset} azimuth={lightAzimuth} heightOverlay={topographicOverlay} onPreset={applyTerrainLook} onExaggeration={value => { verticalExaggerationRef.current = value; setVerticalExaggeration(value); }} onLighting={value => { atmospherePresetRef.current = value; setAtmospherePreset(value); }} onAzimuth={value => { lightAzimuthRef.current = value; setLightAzimuth(value); }} onHeight={toggleTopographicHeightOverlay} onRetry={retryTerrain} />
          </nav>
          <nav className="map-control-strip" aria-label="Quick map controls">
            <RenderQualityControl value={renderQuality} onChange={chooseRenderQuality} />
            <button className="map-control-launch" type="button" aria-pressed={timelineOpen} onClick={() => setTimelineOpen((open) => !open)}><strong>Time</strong><b>{formatTimelineStep(year)}</b></button>
            <Link className="map-control-launch" href="/observatory">Daily archive ↗</Link>
            <button className="map-control-launch" type="button" onClick={() => openAtlasPanel("layers")} aria-pressed={leftOpen && leftPanelMode === "layers"}>
              <span aria-hidden="true">≡</span><strong>Layers</strong><b>{visibleCount}</b>
            </button>
            <button className="map-control-launch map-control-launch-live" type="button" onClick={openLiveContextCatalog} aria-pressed={visibleOfficialCount > 0}>
              <span aria-hidden="true">⌁</span><strong>Live data</strong><b>{visibleOfficialCount}</b>
            </button>
            <div className="quick-live-toggle-list" aria-label="Quick live data layer toggles">
              {QUICK_LIVE_CONTEXT_IDS.map((sourceId) => {
                const source = OFFICIAL_CONTEXT_BY_ID[sourceId];
                const heldAtFrame = officialVisibility[sourceId] && !effectiveOfficialVisibility[sourceId];
                return <button
                  key={sourceId}
                  type="button"
                  aria-pressed={officialVisibility[sourceId]}
                  data-active={officialVisibility[sourceId]}
                  data-held={heldAtFrame}
                  onClick={() => setOfficialContextVisible(sourceId, !officialVisibility[sourceId])}
                  title={`${officialVisibility[sourceId] ? "Hide" : "Show"} ${source.title}`}
                >
                  <i style={{ "--swatch": source.color } as React.CSSProperties} aria-hidden="true" />
                  <span>{source.shortTitle}</span>
                </button>;
              })}
            </div>
            <label className="map-basemap-select"><span>Basemap</span><select value={basemap} onChange={(event) => setBasemap(event.target.value as BasemapKey)} aria-label="Choose basemap style">{(Object.keys(BASEMAPS) as BasemapKey[]).map((key) => <option key={key} value={key}>{BASEMAPS[key].title}</option>)}</select></label>
            <button className="map-control-launch" type="button" onClick={() => openMapUtility("navigate")}><span aria-hidden="true">⌖</span><strong>Controls</strong></button>
            <button className="map-control-launch" type="button" onClick={() => { setSourceStatusOpen((open) => !open); setLeftOpen(false); }} aria-expanded={sourceStatusOpen} aria-controls="map-source-status"><strong>Source status</strong></button>
            <button className="map-control-launch" type="button" onClick={() => setInstrumentOpen((open) => !open)} aria-pressed={instrumentOpen}><strong>Charts</strong></button>
            <a className="map-control-launch" href="/" title={`Open a fresh baseline for ${baselineDay} UTC`}><strong>Today’s baseline</strong></a>
            <Link className="map-control-launch" href="/data"><strong>Contribute data</strong></Link>
          </nav>
          {sourceStatusOpen && <aside id="map-source-status" className="map-source-status" aria-label="Source status and data quality">
            <header><h2>Sources & data quality</h2><button type="button" onClick={() => setSourceStatusOpen(false)} aria-label="Close source status">×</button></header>
            <p>Today · {baselineDay} UTC. Live observations refresh as providers publish. County counts keep their Census edition, and historical gaps remain visible.</p>
            <div className="source-quality-actions"><Link href="/data">Propose data for KFM</Link><Link href="/stewards">Steward review desk</Link></div>
            <button type="button" onClick={refreshVisibleOfficialContext} disabled={officialLoadingCount > 0}>Refresh selected sources</button>
            {OFFICIAL_CONTEXT_SOURCES.map((source) => <SourceQualityRow key={source.id} source={source} state={officialStates[source.id]} payload={officialPayloads[source.id as OfficialContextFeedId]} error={officialErrors[source.id]} selected={officialVisibility[source.id]} held={officialVisibility[source.id] && !effectiveOfficialVisibility[source.id]} onToggle={(selected) => setOfficialContextVisible(source.id, selected)} onRetry={() => retryOfficialLayer(source.id)} />)}
            <Link href="/observatory/sources">Historical coverage & sources ↗</Link>
          {sourceStatusOpen && scenePreset === "elevation-3d" && <aside className="terrain-scene-passport" data-state={terrainState.toLowerCase()} aria-label="Terrain scene passport">
            <header>
              <div><span>TERRAIN SCENE PASSPORT</span><strong>Smoky Hills relief</strong></div>
              <b>{terrainState === "READY" ? "DEM READY" : terrainState === "ERROR" ? "DEM UNAVAILABLE" : "LOADING DEM"}</b>
            </header>
            <dl>
              <div><dt>Vertical scale</dt><dd>{verticalExaggeration.toFixed(1)}× {verticalExaggeration === 1 ? "physical" : "display"}</dd></div>
              <div><dt>Camera</dt><dd>{Math.round(view.pitch)}° pitch · {Math.round((view.bearing + 360) % 360)}° bearing</dd></div>
              <div><dt>Carrier</dt><dd>External Terrarium DEM</dd></div>
              <div><dt>Evidence</dt><dd>Display context only</dd></div>
            </dl>
            <p>Relief is observed from the renderer. Vertical datum, analytical spacing, and KFM source admission are not asserted.</p>
            <div className="terrain-passport-actions">
              <button type="button" aria-pressed={topographicOverlay} onClick={toggleTopographicHeightOverlay}>{topographicOverlay ? "Hide height colors" : "Show height colors"}</button>
              <button type="button" onClick={startTerrainInvestigation}>Profile a transect</button>
              <button type="button" onClick={() => openMapUtility("scene")}>Inspect terrain method</button>
            </div>
            {topographicOverlay && <output className="terrain-cursor-reading" aria-live="polite">{terrainElevationReading ? <><strong>{terrainElevationReading.feet.toFixed(0)} ft</strong><span>{terrainElevationReading.meters.toFixed(0)} m · unexaggerated DEM</span></> : <span>Move over the map to read elevation</span>}</output>}
          </aside>}
          <aside hidden={!sourceStatusOpen} className="map-legend-dock" aria-label="Visible map legend">
            <header>
              <div><span>VISIBLE LAYERS</span><strong>{visibleCount} active</strong></div>
              <button type="button" onClick={() => openAtlasPanel("layers")}>Manage</button>
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
              {activeLayers.length === 0 && <p>No layers are visible. Open Layer Catalog to choose a starting stack.</p>}
            </div>
            {activeLayers.length > 5 && <footer>+{activeLayers.length - 5} more in Layer Catalog</footer>}
            <p className="map-legend-note">{basemap === "standard" ? "OpenFreeMap vector context · counties, places, roads, rail, water, and labels are display context; KFM overlays remain explicit." : basemap === "imagery" ? "Satellite imagery is display context only · overlays are synthetic or generalized." : basemap === "streets" ? "OpenStreetMap reference only · overlays are synthetic or generalized." : basemap === "topo" ? "USGS The National Map topographic tiles are display context only · KFM evidence remains separate." : "Site-local display style · overlays are synthetic or generalized."}</p>
          </aside>
          </aside>}
          {instrumentOpen && streamflowSelectedAtPresent && noaaRadarSelectedAtPresent && <nav className="live-observation-switcher" aria-label="Live observation display">
            <button type="button" aria-pressed={liveInstrument === "river"} onClick={() => { setLiveInstrument("river"); setNoaaRadarPlaying(false); }}>River Pulse</button>
            <button type="button" aria-pressed={liveInstrument === "radar"} onClick={() => { setLiveInstrument("radar"); setStreamflowPlaying(false); }}>Radar Loop</button>
          </nav>}
          {instrumentOpen && showStreamflowDock && <HydrologyObservatory
            bundle={streamflowBundle}
            state={streamflowDisplayState}
            error={streamflowError}
            frame={streamflowFrame}
            frameIndex={safeStreamflowFrameIndex}
            playing={streamflowPlaying}
            speed={streamflowPlaybackSpeed}
            range={streamflowRange}
            selectedStationId={streamflowSelectedStationId}
            reducedMotion={reducedMotion}
            onRefresh={() => { void refreshStreamflow(streamflowRange, streamflowSelectedStationId); }}
            onTogglePlay={toggleStreamflowPlayback}
            onStep={stepStreamflow}
            onSeek={seekStreamflow}
            onJumpLatest={jumpStreamflowToLatest}
            onSpeed={setStreamflowPlaybackSpeed}
            onRange={changeStreamflowRange}
            onSelectStation={selectStreamflowStation}
          />}
          {instrumentOpen && showRadarDock && <aside
            className="noaa-radar-loop"
            data-state={noaaRadarDisplayState.toLowerCase().replaceAll(" ", "-")}
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
            <header>
              <div><span>OBSERVED RADAR · EXTERNAL CONTEXT</span><strong>{NOAA_RADAR_PRODUCT_TITLE}</strong></div>
              <b>{noaaRadarDisplayState}</b>
            </header>
            <div className="noaa-radar-frame" role="status" aria-live={noaaRadarPlaying ? "off" : "polite"} aria-busy={noaaRadarFrameLoadState === "loading"} aria-atomic="true">
              <div><strong>{noaaRadarFrameHeadline}</strong><small>{noaaRadarFrameDetail}</small></div>
              <span>{noaaRadarLoopFrames.length > 0 ? `${noaaRadarFrameIndex >= 0 ? noaaRadarFrameIndex + 1 : 0} / ${noaaRadarLoopFrames.length}` : "0 / 0"}</span>
            </div>
            <div className="noaa-radar-transport" aria-label="Radar playback">
              <button type="button" onClick={() => stepNoaaRadar("reverse")} disabled={!noaaRadarRenderable || noaaRadarFrameIndex <= 0 || noaaRadarFrameLoadState === "loading"} aria-label="Previous NOAA radar observation">‹</button>
              <button className="noaa-radar-play" type="button" aria-pressed={noaaRadarPlaying} onClick={toggleNoaaRadarPlayback} disabled={reducedMotion || noaaRadarLoopFrames.length < 2 || noaaRadarManifestState === "loading" || !noaaRadarRenderable}>{noaaRadarPlaying ? "Ⅱ Pause" : "▶ Play"}</button>
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
            <div className="noaa-radar-settings">
              <label><span>Loop</span><select value={noaaRadarLoopSpan} onChange={(event) => { setNoaaRadarPlaying(false); setNoaaRadarLoopSpan(Number(event.target.value) as NoaaRadarLoopSpanMinutes); }}><option value={30}>30 min</option><option value={60}>1 hour</option><option value={120}>2 hours</option></select></label>
              <label><span>Speed</span><select value={noaaRadarPlaybackSpeed} onChange={(event) => setNoaaRadarPlaybackSpeed(Number(event.target.value) as NoaaRadarPlaybackSpeed)}><option value={0.5}>0.5×</option><option value={1}>1×</option><option value={2}>2×</option></select></label>
              <label><span>Opacity</span><input type="range" min="10" max="100" value={Math.round(officialOpacity["nws-radar"] * 100)} onChange={(event) => setOfficialContextOpacity("nws-radar", Number(event.target.value) / 100)} aria-valuetext={`${Math.round(officialOpacity["nws-radar"] * 100)} percent`} /></label>
              <button type="button" onClick={() => void refreshNoaaRadarManifest()} disabled={noaaRadarManifestState === "loading"}>Refresh</button>
            </div>
            <details className="noaa-radar-legend">
              <summary>Reflectivity legend + source</summary>
              <img src={NOAA_RADAR_LEGEND_URL} width="272" height="21" loading="lazy" alt="NOAA base-reflectivity color legend in dBZ" />
              <p>Transparent pixels mean no displayed echo. Missing or unavailable imagery is not interpreted as clear weather. Exact observations are stepped without interpolation. A settled request means MapLibre reported no source error; it does not prove complete radar coverage.</p>
              <dl><div><dt>Source</dt><dd>{NOAA_RADAR_SOURCE_TITLE}</dd></div><div><dt>Cadence</dt><dd>{noaaRadarManifest ? `${Math.round(noaaRadarManifest.nominalCadenceSeconds / 60)} min observed median` : "Discovered from NOAA"}</dd></div><div><dt>Latest age</dt><dd>{noaaRadarLatestAgeMinutes === null ? "Unknown" : `${noaaRadarLatestAgeMinutes} min`}</dd></div><div><dt>Gaps</dt><dd>{noaaRadarManifest ? noaaRadarManifest.gapCount : "Unknown"}</dd></div></dl>
              {noaaRadarCrossDomainSources.length > 0 && <p><strong>Co-visible operational context:</strong> {noaaRadarCrossDomainSources.join(" · ")}. Each source keeps its own observation or retrieval clock; visual overlap does not establish correlation, lag, direction, or causation.</p>}
              <a href={OFFICIAL_CONTEXT_BY_ID["nws-radar"].sourceUrl} target="_blank" rel="noreferrer">Open NOAA nowCOAST ↗</a>
            </details>
            {noaaRadarFrameError && <div className="noaa-radar-error" role="alert"><strong>{noaaRadarRenderable ? "Frozen on the last confirmed observation" : "Radar withheld"}</strong><span>{noaaRadarFrameError} No untimed or synthetic fallback was used.</span></div>}
            {reducedMotion && <p className="noaa-radar-motion-note">Reduced motion is active. Automatic looping is off; exact-frame stepping remains available.</p>}
            <footer>Situational display only · not an emergency warning service · times remain separate from the atlas year</footer>
          </aside>}
          <button className="qwen-map-launch" type="button" onClick={qwenOpen ? closeQwenCompanion : openQwenCompanion} aria-expanded={qwenOpen} aria-controls="qwen-map-panel" data-open={qwenOpen}>
            <span className="qwen-launch-mark" aria-hidden="true">Q</span>
            <span><strong>Ask Qwen</strong><small>About this map view</small></span>
            <b aria-hidden="true">{qwenOpen ? "×" : "↗"}</b>
          </button>
          {qwenOpen && <aside id="qwen-map-panel" className="qwen-panel" role="dialog" aria-modal="false" aria-labelledby="qwen-panel-title">
            <header className="qwen-panel-heading">
              <div><span className="qwen-eyebrow">QWEN · MAP CONTEXT</span><h2 id="qwen-panel-title">Ask about what you see</h2><p>MapLibre supplies the view. Qwen helps interpret the supplied context.</p></div>
              <button className="icon-close" type="button" onClick={closeQwenCompanion} aria-label="Close Qwen companion">×</button>
            </header>
            <div className="qwen-context-strip" aria-label="Qwen context scope">
              <span><small>VIEW</small><strong>{mapRepresentationLabel}</strong></span>
              <span><small>TIME</small><strong>{temporalScopeLabel}</strong></span>
              <span><small>LAYERS</small><strong>{visibleCount}</strong></span>
              <span><small>SELECTION</small><strong>{selected ? "1" : "0"}</strong></span>
            </div>
            <div className="qwen-messages" aria-live="polite">
              {qwenMessages.map((message, index) => <article key={`${message.role}-${index}`} data-role={message.role}><span>{message.role === "assistant" ? "QWEN" : "YOU"}</span><p>{message.content}</p></article>)}
              {qwenBusy && <article data-role="assistant" className="qwen-thinking"><span>QWEN</span><p>Reading the current map context…</p></article>}
            </div>
            <div className="qwen-quick-prompts" aria-label="Suggested Qwen questions">
              {QWEN_QUICK_PROMPTS.map((prompt) => <button type="button" key={prompt} onClick={() => setQwenQuestion(prompt)}>{prompt}</button>)}
            </div>
            <form className="qwen-form" onSubmit={(event) => { event.preventDefault(); void askQwen(); }}>
              <label><span className="sr-only">Ask Qwen about the map</span><textarea value={qwenQuestion} onChange={(event) => setQwenQuestion(event.target.value)} placeholder="Ask about this place, time, or layer context…" rows={3} maxLength={1200} /></label>
              <div><span data-bridge-state={qwenBridgeState}>{qwenBridgeState === "ready" ? "BRIDGE CONNECTED" : qwenBridgeState === "error" ? "BRIDGE UNAVAILABLE" : "LOCAL BRIDGE NOT CONFIGURED"}</span><button type="submit" disabled={!qwenQuestion.trim() || qwenBusy}>{qwenBusy ? "Thinking…" : "Ask Qwen"}</button></div>
            </form>
            <footer className="qwen-panel-footer"><p>Qwen is interpretive only. It cannot establish evidence, policy, release, or publication authority.</p><button type="button" onClick={() => void copyQwenPrompt()}>Copy grounded prompt</button></footer>
          </aside>}
          <div id="map-canvas" ref={mapContainerRef} className="map-canvas" tabIndex={0} role="application" aria-label="Interactive map of real Kansas baselines and dated source layers. Use arrow keys to pan and plus or minus to zoom; use Map Workbench Inspect or the Layer Catalog for a keyboard feature alternative." />
          {hoverSummary && <aside className="map-hover-summary" style={{ left: hoverSummary.x, top: hoverSummary.y }} aria-hidden="true">
            <span>{hoverSummary.subtitle}</span><strong>{hoverSummary.title}</strong><small>{hoverSummary.state}</small>
          </aside>}

          {(runtime.kind === "loading" || runtime.kind === "error" || runtime.kind === "unsupported") && <div className={`runtime-overlay ${runtime.kind}`} role="status" aria-live="assertive"><span className="runtime-spinner" aria-hidden="true" /><strong>{runtime.kind === "loading" ? "Preparing spatial explorer" : runtime.kind === "unsupported" ? "Map runtime unsupported" : "Map runtime unavailable"}</strong><p>{runtime.message}</p>{runtime.kind === "error" && <button type="button" onClick={() => window.location.reload()}>Reload map</button>}</div>}
          {runtime.kind === "degraded" && <div className="runtime-degraded-banner" role="status" aria-live="polite"><strong>Partial map degradation</strong><span>{runtime.message}</span></div>}
          {temporalNoData.length > 0 && <div className="no-time-data" role="status"><strong>No compatible record for {temporalScopeLabel} in {temporalNoData.map((layer) => layer.title).join(", ")}</strong><span>Other active layers remain visible; choose an available frame or change the sweep semantics.</span></div>}

          {runtime.kind === "ready" && guidedStartOpen && <aside className="guided-start" aria-labelledby="guided-start-title">
            <header>
              <div><span>START HERE · DEMONSTRATION ONLY</span><h2 id="guided-start-title">Explore one feature in under a minute.</h2></div>
              <button className="icon-close" type="button" onClick={dismissGuidedStart} aria-label="Dismiss guided examples">×</button>
            </header>
            <p>Every current map layer is synthetic or generalized. These examples show how the Explorer distinguishes supported, corrected, and protected contexts without pretending to be a live data source.</p>
            <div className="guided-example-list">
              {GUIDED_EXAMPLES.map((example) => <button key={example.id} type="button" data-tone={example.id} onClick={() => openGuidedExample(example)}>
                <span>{example.state}</span><strong>{example.title}</strong><small>{example.summary}</small><b aria-hidden="true">→</b>
              </button>)}
            </div>
            <footer>Or search a place above, choose any map feature, or browse the Layer Catalog.</footer>
          </aside>}

          {runtime.kind === "ready" && storyOpen && <aside id="kfm-story-trail" className="story-trail" role="region" aria-labelledby="story-trail-title" aria-live="polite">
            <header>
              <div><span>GUIDED KANSAS TRUST STORY · SITE-LOCAL</span><small>Step {storyStepIndex + 1} of {KFM_STORY_TRAIL.length}</small></div>
              <button className="icon-close" type="button" onClick={closeStoryTrail} aria-label="Close guided story">×</button>
            </header>
            <div className="story-progress" aria-label={`Story progress: step ${storyStepIndex + 1} of ${KFM_STORY_TRAIL.length}`}>
              {KFM_STORY_TRAIL.map((step, index) => <button key={step.id} type="button" data-active={index === storyStepIndex} aria-label={`Open story step ${index + 1}: ${step.title}`} onClick={() => openStoryStep(index)}><span>{String(index + 1).padStart(2, "0")}</span></button>)}
            </div>
            <article data-state={activeStoryStep.id}>
              <span>{activeStoryStep.eyebrow} · {formatTimelineStep(activeStoryStep.year)}</span>
              <h2 id="story-trail-title">{activeStoryStep.title}</h2>
              <p>{activeStoryStep.narrative}</p>
            </article>
            <div className="story-actions">
              <button type="button" disabled={storyStepIndex === 0} onClick={() => openStoryStep(storyStepIndex - 1)}>Previous</button>
              <button type="button" onClick={() => { setDrawerView("lineage"); setRightOpen(true); }}>Inspect lineage</button>
              {storyStepIndex < KFM_STORY_TRAIL.length - 1
                ? <button type="button" onClick={() => openStoryStep(storyStepIndex + 1)}>Next step</button>
                : <button type="button" onClick={closeStoryTrail}>Finish story</button>}
            </div>
            <footer>Fixture-first 2D guidance only · no live StoryManifest playback · no evidence, policy, review, release, or publication effect.</footer>
          </aside>}

          <nav className="map-tool-rail" aria-label="Unified map controls">
            <div className="map-tool-group" aria-label="Map navigation">
              <span className="map-tool-group-label">MAP</span>
              <button type="button" onClick={() => mapRef.current?.zoomIn({ duration: motionDuration(250) })} aria-label="Zoom in" data-tooltip="Zoom in"><span className="map-tool-glyph" aria-hidden="true">＋</span><span className="map-tool-label">Zoom in</span></button>
              <button type="button" onClick={() => mapRef.current?.zoomOut({ duration: motionDuration(250) })} aria-label="Zoom out" data-tooltip="Zoom out"><span className="map-tool-glyph" aria-hidden="true">−</span><span className="map-tool-label">Zoom out</span></button>
              <button className="mobile-hidden-control" type="button" onClick={() => mapRef.current?.resetNorthPitch({ duration: motionDuration(450) })} aria-label="Reset compass and pitch" data-tooltip="Reset north"><span className="map-tool-glyph" aria-hidden="true">N</span><span className="map-tool-label">Reset north</span></button>
              <button type="button" onClick={fitKansasView} aria-label="Reset view to Kansas" data-tooltip="Kansas extent"><span className="map-tool-glyph" aria-hidden="true">KS</span><span className="map-tool-label">Kansas extent</span></button>
            </div>
            <div className="map-tool-group map-tool-group-workbench" aria-label="KFM workbench shortcuts">
              <span className="map-tool-group-label">WORKBENCH</span>
              <button type="button" onClick={() => openAtlasPanel("views")} aria-pressed={leftOpen && leftPanelMode === "views"} aria-label="Open Living Atlas views" data-tooltip="Views"><span className="map-tool-glyph" aria-hidden="true">▦</span><span className="map-tool-label">Views</span></button>
              <button type="button" onClick={() => openAtlasPanel("layers")} aria-pressed={leftOpen && leftPanelMode === "layers"} aria-label="Open Layer Catalog" data-tooltip="Layers"><span className="map-tool-glyph" aria-hidden="true">≡</span><span className="map-tool-label">Layers</span></button>
              <button type="button" onClick={openLiveContextCatalog} aria-pressed={visibleOfficialCount > 0} aria-label="Open live data controls" data-tooltip="Live data"><span className="map-tool-glyph" aria-hidden="true">⌁</span><span className="map-tool-label">Live data</span></button>
              <button type="button" onClick={(event) => mapUtilityOpen && mapUtilityView === "inspect" ? closeMapUtility() : openMapUtility("inspect", event.currentTarget)} aria-expanded={mapUtilityOpen && mapUtilityView === "inspect"} aria-controls="map-utility-panel" aria-label="Open feature inspection" data-tooltip="Inspect"><span className="map-tool-glyph" aria-hidden="true">⌖</span><span className="map-tool-label">Inspect</span></button>
              <button type="button" onClick={(event) => mapUtilityOpen && mapUtilityView === "scene" ? closeMapUtility() : openMapUtility("scene", event.currentTarget)} aria-expanded={mapUtilityOpen && mapUtilityView === "scene"} aria-controls="map-utility-panel" aria-label="Open scene and tile lab" data-tooltip="Scene"><span className="map-tool-glyph" aria-hidden="true">3D</span><span className="map-tool-label">Scene</span></button>
              <button type="button" onClick={(event) => mapUtilityOpen && mapUtilityView === "measure" ? closeMapUtility() : openMapUtility("measure", event.currentTarget)} aria-expanded={mapUtilityOpen && mapUtilityView === "measure"} aria-controls="map-utility-panel" aria-label="Open measurement tools" data-tooltip="Measure"><span className="map-tool-glyph" aria-hidden="true">⌗</span><span className="map-tool-label">Measure</span></button>
              <button ref={mapUtilityButtonRef} className="map-report-tool" type="button" onClick={(event) => mapUtilityOpen && mapUtilityView === "report" ? closeMapUtility() : openMapUtility("report", event.currentTarget)} aria-expanded={mapUtilityOpen && mapUtilityView === "report"} aria-controls="map-utility-panel" aria-label="Build a custom report" data-tooltip="Report"><span className="map-tool-glyph" aria-hidden="true">＋</span><span className="map-tool-label">Report</span></button>
              <button type="button" onClick={() => setToolsExpanded((current) => !current)} aria-expanded={toolsExpanded} aria-controls="more-map-tools" aria-label="More map tools" data-tooltip="More tools"><span className="map-tool-glyph" aria-hidden="true">•••</span><span className="map-tool-label">More</span></button>
            </div>
            {toolsExpanded && <div className="secondary-tools" id="more-map-tools">
              <button type="button" onClick={(event) => openMapUtility("navigate", event.currentTarget)}><span>⌖</span>Map controls</button>
              <button type="button" onClick={(event) => openMapUtility("places", event.currentTarget)}><span>⌖</span>Places + trails</button>
              <button type="button" onClick={(event) => openMapUtility("display", event.currentTarget)}><span>◐</span>Display + basemap</button>
              <button type="button" onClick={(event) => openMapUtility("connections", event.currentTarget)}><span>⛓</span>Source connections</button>
              <button type="button" onClick={(event) => openMapUtility("import", event.currentTarget)}><span>⇧</span>Import preview</button>
              <button type="button" onClick={captureAnalysisArea} disabled={locationCameraRedacted}><span>▣</span>{analysisArea ? "Update report area" : "Lock report area"}</button>
              <button type="button" onClick={locateUser}><span>⌾</span>My location</button>
              <button type="button" onClick={toggleFullscreen} aria-label="Toggle fullscreen"><span>⛶</span>Fullscreen</button>
              <button type="button" aria-pressed={projection === "globe"} onClick={() => setProjection((current) => current === "globe" ? "mercator" : "globe")}><span>◎</span>{projection === "globe" ? "2D view" : "Globe"}</button>
              <button type="button" aria-pressed={measureMode === "point"} onClick={() => toggleMeasure("point")}><span>·</span>Draw point</button>
              <button type="button" aria-pressed={measureMode === "distance"} onClick={() => toggleMeasure("distance")}><span>↔</span>Draw line</button>
              <button type="button" aria-pressed={measureMode === "area"} onClick={() => toggleMeasure("area")}><span>◇</span>Draw polygon</button>
              <button type="button" onClick={captureAnalysisArea} disabled={locationCameraRedacted}><span>▣</span>Draw viewport rectangle</button>
              <button type="button" onClick={clearSelection} disabled={!selected}><span>×</span>Clear selection</button>
              <button type="button" onClick={shareView}><span>↗</span>Share view</button>
              <button type="button" onClick={(event) => openMapUtility("export", event.currentTarget)}><span>⇩</span>Review export</button>
            </div>}
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
              <div><p className="panel-kicker">MAP WORKBENCH</p><h2 id="map-utility-title">{mapUtilityView === "report" ? "Custom report builder" : mapUtilityView === "places" ? "Places + investigation trails" : mapUtilityView === "scene" ? "Map display" : mapUtilityView === "connections" ? "Source connections" : mapUtilityView === "import" ? "Local import preview" : "Map tools"}</h2><span>{mapUtilityView === "report" ? "Turn the current map, time, layers, and selected data into a usable report." : mapUtilityView === "places" ? "Capture complete map states as ordered, device-local investigation stops and move through them without changing KFM authority." : mapUtilityView === "scene" ? "Use verified renderer controls and see which 3D capabilities are display-only or held." : mapUtilityView === "connections" ? "Inspect the live relationship between the layer registry, MapLibre sources, renderers, and visible records." : mapUtilityView === "import" ? "Inspect KML or GeoJSON locally, preview supported geometry, and keep admission and publication effects at none." : "Inspect, navigate, query sources, compare, display, measure, export, and diagnose the active map."}</span></div>
              <button className="icon-close" type="button" onClick={closeMapUtility} aria-label="Close Map Workbench">×</button>
            </header>
            <nav className="map-utility-tabs" role="tablist" aria-label="Map Workbench views">
              {mapUtilityViews.map((utilityView, index) => <button
                key={utilityView}
                ref={(node) => { mapUtilityTabRefs.current[index] = node; }}
                id={`map-utility-tab-${utilityView}`}
                type="button"
                role="tab"
                aria-selected={mapUtilityView === utilityView}
                aria-controls={`map-utility-view-${utilityView}`}
                tabIndex={mapUtilityView === utilityView ? 0 : -1}
                onClick={() => activateMapUtilityView(utilityView)}
                onKeyDown={(event) => handleMapUtilityTabKeyDown(event, index)}
              >{mapUtilityLabels[utilityView]}</button>)}
            </nav>
            <div className="map-utility-scroll">
              {mapUtilityView === "report" && <section id="map-utility-view-report" role="tabpanel" aria-labelledby="map-utility-tab-report" className="map-utility-section report-builder-section">
                <div className="map-utility-section-heading"><span>CUSTOM REPORT</span><h3>Build from the map you are using</h3><p>Filters apply immediately. The report uses current Explorer records and keeps evidence states, source roles, attribution, uncertainty, and time visible.</p></div>

                <section className="analysis-recipes" aria-labelledby="analysis-recipes-title">
                  <header><div><span>ANALYSIS RECIPES</span><h4 id="analysis-recipes-title">Configure map + report together</h4></div><small>Reversible view state</small></header>
                  <div>{ANALYSIS_RECIPES.map((recipe) => <button key={recipe.id} type="button" onClick={() => applyAnalysisRecipe(recipe)}><span>{recipe.eyebrow}</span><strong>{recipe.title}</strong><p>{recipe.summary}</p><small>{recipe.year} · {recipe.layerIds.length} layers · {recipe.detail.toLowerCase()}</small></button>)}</div>
                </section>

                <div className="report-builder-grid">
                  <div className="report-controls">
                    <label className="report-title-field"><span>Report title</span><input type="text" value={reportTitle} maxLength={90} onChange={(event) => setReportTitle(event.target.value)} /></label>

                    <fieldset className="report-control-group"><legend>Record filters</legend><div className="report-filter-grid">
                      <label><span className="sr-only">Search records included in the report</span><i aria-hidden="true">⌕</i><input type="search" value={reportQuery} onChange={(event) => setReportQuery(event.target.value)} placeholder="Record, layer, source, or domain" /></label>
                      <label><span className="sr-only">Filter report by evidence state</span><select value={reportEvidenceFilter} onChange={(event) => setReportEvidenceFilter(event.target.value as EvidenceState | "ALL")}><option value="ALL">All evidence states</option>{(Object.keys(evidenceLabels) as EvidenceState[]).map((state) => <option key={state} value={state}>{state.replaceAll("_", " ")}</option>)}</select></label>
                    </div></fieldset>

                    <fieldset className="report-control-group"><legend>Geographic scope</legend><div className="report-scope-grid">
                      <button type="button" aria-pressed={reportScope === "VIEWPORT"} onClick={() => setReportScope("VIEWPORT")}><strong>Map extent</strong><small>Records inside the current viewport</small></button>
                      <button type="button" aria-pressed={reportScope === "ANALYSIS_AREA"} disabled={!analysisArea} onClick={() => setReportScope("ANALYSIS_AREA")}><strong>Locked area</strong><small>{analysisArea ? `${analysisAreaRecordCount} compatible records` : "Capture an area from Map controls"}</small></button>
                      <button type="button" aria-pressed={reportScope === "VISIBLE_LAYERS"} onClick={() => setReportScope("VISIBLE_LAYERS")}><strong>Visible layers</strong><small>Statewide records in active layers</small></button>
                      <button type="button" aria-pressed={reportScope === "SELECTION"} disabled={!selected} onClick={() => setReportScope("SELECTION")}><strong>Selection</strong><small>{selected?.properties.title ?? "Select a map feature first"}</small></button>
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
                    <header><div><span>LIVE REPORT PREVIEW</span><h4>{reportTitle.trim() || "Kansas map data report"}</h4><p>{reportScope.replaceAll("_", " ")} · {temporalScopeLabel} · {reportDetail}</p></div><strong>{reportRecords.length} RECORD{reportRecords.length === 1 ? "" : "S"}</strong></header>
                    {(reportQuery || reportEvidenceFilter !== "ALL") && <div className="report-active-filters"><span>ACTIVE FILTERS</span>{reportQuery && <b>Search: {reportQuery}</b>}{reportEvidenceFilter !== "ALL" && <b>{reportEvidenceFilter.replaceAll("_", " ")}</b>}<button type="button" onClick={() => { setReportQuery(""); setReportEvidenceFilter("ALL"); }}>Clear</button></div>}
                    {reportSections.summary && <div className="report-metrics" aria-label="Report summary metrics"><article><span>Records</span><strong>{reportRecords.length}</strong></article><article><span>Layers</span><strong>{reportLayerSummary.length}</strong></article><article><span>States</span><strong>{Object.keys(reportEvidenceCounts).length}</strong></article><article><span>Selection</span><strong>{selected ? "1" : "0"}</strong></article></div>}
                    {measurementGeometryMode && <section className="report-preview-section"><span>MEASUREMENT INPUT</span><p>{measurement} · {measureUnit === "imperial" ? "miles / square miles" : "kilometers / square kilometers"}. Browser-local approximation is carried into JSON as a report input, not as evidence.</p></section>}
                    {reportSections.findings && <section className="report-preview-section"><span>FINDINGS</span><ol>{reportFindings.map((finding) => <li key={finding}>{finding}</li>)}</ol></section>}
                    <section className="report-preview-section report-temporal-comparison"><span>TIME A / TIME B CATALOG AVAILABILITY</span><div className="report-metrics"><article><span>{formatTimelineStep(compareTimeA)}</span><strong>{reportTemporalComparison.timeARecordCount}</strong><small>scoped records</small></article><article><span>{formatTimelineStep(compareTimeB)}</span><strong>{reportTemporalComparison.timeBRecordCount}</strong><small>scoped records</small></article><article><span>DELTA</span><strong>{reportTemporalComparison.recordDelta >= 0 ? "+" : ""}{reportTemporalComparison.recordDelta}</strong><small>catalog records</small></article><article><span>CHANGED</span><strong>{reportTemporalComparison.changedLayerCount}</strong><small>included layers</small></article></div><p>Applies this report’s layer, evidence, query, selection, visibility, viewport, or analysis-area scope to both times. Catalog availability is not observed change or imagery analysis.</p></section>
                    {reportSections.records && <section className="report-preview-section"><span>RECORDS</span><div className="report-record-table" role="table" aria-label="Included report records">
                      {reportRecords.slice(0, reportDetail === "EXECUTIVE" ? 8 : reportDetail === "STANDARD" ? 30 : reportRecords.length).map(({ layer, properties }) => <article key={`${layer.id}:${properties.fid}`} role="row"><div><strong>{properties.title}</strong><small>{layer.title} · {properties.year}</small></div><span data-state={properties.evidenceState}>{properties.evidenceState}</span><p>{properties.summary}</p></article>)}
                      {reportRecords.length === 0 && <div className="report-empty"><strong>No records match</strong><p>Move or widen the map, change time, choose another scope, or include more layers.</p></div>}
                    </div></section>}
                    {reportSections.evidence && reportRecords.length > 0 && <section className="report-preview-section"><span>EVIDENCE DISTRIBUTION</span><div className="report-evidence-grid">{Object.entries(reportEvidenceCounts).sort((left, right) => right[1] - left[1]).map(([state, count]) => <article key={state}><strong>{count}</strong><span>{state}</span></article>)}</div></section>}
                    {reportSections.limitations && <aside className="report-boundary"><strong>Use boundary</strong><p>Site-local synthetic and generalized demonstration data only. The generated report preserves limitations and cannot release, publish, admit, or authorize KFM data.</p></aside>}
                    <footer><span>Updated {reportGeneratedAt}</span><div><button type="button" onClick={() => void copyCustomReport()} disabled={!reportLayerIds.length}>Copy</button><button type="button" onClick={() => downloadCustomReport("json")} disabled={!reportLayerIds.length}>Data .json</button><button className="report-download-primary" type="button" onClick={() => downloadCustomReport("html")} disabled={!reportLayerIds.length}>Report .html</button></div></footer>
                  </article>
                </div>
              </section>}

              {mapUtilityView === "navigate" && <section id="map-utility-view-navigate" role="tabpanel" aria-labelledby="map-utility-tab-navigate" className="map-utility-section">
                <div className="map-utility-section-heading"><span>NAVIGATE</span><h3>Camera, coordinates + private location</h3><p>MapLibre camera actions change only this browser view. They never change evidence, policy, review, release, or publication state.</p></div>
                <dl className="map-camera-facts">
                  <div><dt>Center</dt><dd>{locationCameraRedacted ? "Private camera · redacted" : `${formatCoordinate(view.center[1], "N", "S")} · ${formatCoordinate(view.center[0], "E", "W")}`}</dd></div>
                  <div><dt>Zoom</dt><dd>{view.zoom.toFixed(2)}</dd></div>
                  <div><dt>Bearing / pitch</dt><dd>{Math.round(view.bearing)}° / {Math.round(view.pitch)}°</dd></div>
                  <div><dt>Projection</dt><dd>{projection}</dd></div>
                </dl>
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
                <section className="analysis-area-card" data-active={Boolean(analysisArea)} aria-labelledby="analysis-area-title">
                  <header><div><span>MAPLIBRE VIEWPORT ANALYSIS</span><h4 id="analysis-area-title">Area of interest</h4></div><strong>{analysisArea ? "LOCKED" : "NOT SET"}</strong></header>
                  {analysisArea
                    ? <><dl><div><dt>West / east</dt><dd>{analysisArea.west.toFixed(4)}° / {analysisArea.east.toFixed(4)}°</dd></div><div><dt>South / north</dt><dd>{analysisArea.south.toFixed(4)}° / {analysisArea.north.toFixed(4)}°</dd></div><div><dt>Compatible records</dt><dd>{analysisAreaRecordCount}</dd></div><div><dt>Report scope</dt><dd>{reportScope === "ANALYSIS_AREA" ? "ACTIVE" : "AVAILABLE"}</dd></div></dl><div><button type="button" onClick={captureAnalysisArea}>Update from viewport</button><button type="button" onClick={fitAnalysisArea}>Fit area</button><button type="button" onClick={() => { setReportScope("ANALYSIS_AREA"); setReportGeneratedAt(new Date().toISOString()); openMapUtility("report"); }}>Build area report</button><button type="button" onClick={clearAnalysisArea}>Clear</button></div></>
                    : <><p>Lock the current viewport as a stable rectangular analysis area. You can pan elsewhere while reports continue using the locked extent.</p><button type="button" onClick={captureAnalysisArea} disabled={locationCameraRedacted}>Lock current viewport</button></>}
                  <footer>Site-local fixture query only · viewport geometry is context, not evidence</footer>
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
              </section>}

              {mapUtilityView === "places" && <section id="map-utility-view-places" role="tabpanel" aria-labelledby="map-utility-tab-places" className="map-utility-section places-trail-section">
                <div className="map-utility-section-heading"><span>PLACES + TRAILS</span><h3>Build a reusable spatial investigation</h3><p>Save the current camera, time, layer order, opacity, scene, report area, comparison, report setup, and selection as one ordered stop. Revisit a stop or play the sequence as a guided trail.</p></div>
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
              </section>}

              {mapUtilityView === "inspect" && <section id="map-utility-view-inspect" role="tabpanel" aria-labelledby="map-utility-tab-inspect" className="map-utility-section">
                <div className="map-utility-section-heading"><span>INSPECT</span><h3>Feature index + context receipt</h3><p>Hover is a preview only. A click or explicit Inspect action commits one stable registry feature before the Evidence Drawer opens.</p></div>
                <article className="map-utility-card map-context-card">
                  <header><span>MAP CONTEXT</span><strong>{selected?.properties.title ?? "No committed selection"}</strong></header>
                  <dl><div><dt>Active time</dt><dd>{temporalScopeLabel}</dd></div><div><dt>Visible layers</dt><dd>{visibleCount}</dd></div><div><dt>Selection</dt><dd>{selected ? selected.properties.evidenceState : "NONE"}</dd></div><div><dt>Halo</dt><dd>{selectedLayerHidden ? "HIDDEN LAYER" : selectedTimeMismatch ? "OUTSIDE TIME" : selectedEvidenceFiltered ? "FILTERED" : selected ? "VISIBLE" : "NONE"}</dd></div></dl>
                  <button type="button" onClick={() => void copyMapContextReceipt()}>Copy 15-minute map context receipt</button>
                </article>

                <section className="nearby-context-card" aria-labelledby="nearby-context-title" data-active={Boolean(selected)}>
                  <header><div><span>CROSS-DOMAIN DISCOVERY</span><h4 id="nearby-context-title">Nearby context</h4></div><strong>{selected ? `${nearbyContext.length} FOUND` : "SELECT A FEATURE"}</strong></header>
                  <div className="nearby-context-controls"><label><span>Anchor radius</span><select value={nearbyRadiusMiles} onChange={(event) => setNearbyRadiusMiles(Number(event.target.value))}>{[25, 50, 100, 200].map((radius) => <option key={radius} value={radius}>{radius} miles</option>)}</select></label><label><input type="checkbox" checked={nearbyVisibleLayersOnly} onChange={(event) => setNearbyVisibleLayersOnly(event.target.checked)} /><span>Visible layers only</span></label><button type="button" onClick={showNearbyContextLayers} disabled={!selected || nearbyContext.length === 0}>Show layers</button><button type="button" onClick={fitNearbyContext} disabled={!selected || nearbyContext.length === 0}>Fit context</button></div>
                  {!selected && <p>Commit a feature selection to discover nearby public-safe records across domains.</p>}
                  {selected && <div className="nearby-context-list">{nearbyContext.map(({ layer, feature, distanceMiles }) => <article key={`${layer.id}:${feature.properties.fid}`}><button type="button" onClick={() => selectIndexedFeature(layer.id, feature.properties.fid)}><span>{layer.title} · {distanceMiles < 1 ? "<1" : Math.round(distanceMiles)} mi</span><strong>{feature.properties.title}</strong><small>{feature.properties.evidenceState}</small></button></article>)}{nearbyContext.length === 0 && <p>No compatible anchors fall within this radius. Widen the radius or clear the evidence filter.</p>}</div>}
                  <footer>Distances use generalized feature anchors—not geometry edges, route distance, survey measurement, causal connection, or evidence of a relationship.</footer>
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

              {mapUtilityView === "scene" && <section id="map-utility-view-scene" role="tabpanel" aria-labelledby="map-utility-tab-scene" className="map-utility-section scene-lab-section">
                <div className="map-utility-section-heading"><span>MAP REPRESENTATION</span><h3>Verified renderer controls</h3><p>Change the live MapLibre canvas. Controls shown here either alter the renderer now or clearly report why a capability is unavailable.</p></div>

                <section className="scene-preset-grid verified-representation-grid" aria-label="Verified map representations">
                  {([
                    ["2d", "2D map", "Mercator · terrain off"],
                    ["terrain", "Terrain 3D", terrainState === "READY" ? "DEM ready" : terrainState === "ERROR" ? "DEM unavailable" : "Loading DEM"],
                    ["globe", "Globe", "Globe projection"],
                  ] as const).map(([id, title, detail]) => <button key={id} type="button" aria-pressed={id === "terrain" ? scenePreset === "elevation-3d" : id === "globe" ? projection === "globe" : projection === "mercator" && scenePreset !== "elevation-3d"} onClick={() => activateMapRepresentation(id)}><span>{id === "terrain" ? "3D" : id === "globe" ? "◎" : "2D"}</span><strong>{title}</strong><small>{detail}</small></button>)}
                </section>

                <section className="renderer-capability-list" aria-label="Renderer capability status">
                  <article data-state="ready"><span>WORKS NOW</span><strong>2D, globe, camera, measurement</strong><small>Direct MapLibre state changes</small></article>
                  <article data-state={terrainState === "ERROR" ? "held" : "context"}><span>{terrainState === "READY" ? "DISPLAY ONLY" : terrainState}</span><strong>Terrain relief + profile preview</strong><small>External DEM; not KFM evidence</small></article>
                  <article data-state="context"><span>CONTEXT ONLY</span><strong>HMS smoke · Shake stations · hazard overlays</strong><small>Live-source controls stay in Layers; no model, alert, waveform, or evidence claim is implied</small></article>
                </section>

                <section className="terrain-height-instrument" aria-labelledby="terrain-height-title">
                  <header><div><span>TOPOGRAPHIC HEIGHT</span><h4 id="terrain-height-title">Elevation color overlay</h4></div><button type="button" role="switch" aria-checked={topographicOverlay} disabled={scenePreset !== "elevation-3d" || terrainState === "ERROR"} onClick={toggleTopographicHeightOverlay}>{topographicOverlay ? "ON" : "OFF"}</button></header>
                  <div className="terrain-height-ramp" aria-label="Elevation color scale from 200 to 1,250 meters"><i /><span>200 m</span><span>400 m</span><span>650 m</span><span>1,000 m</span><span>1,250 m</span></div>
                  <div className="terrain-height-readout">
                    <div><small>CURSOR ELEVATION</small><strong>{terrainElevationReading ? `${terrainElevationReading.feet.toFixed(0)} ft` : "Move over map"}</strong><span>{terrainElevationReading ? `${terrainElevationReading.meters.toFixed(0)} m · ${terrainElevationReading.latitude.toFixed(5)}, ${terrainElevationReading.longitude.toFixed(5)}` : "Uses the active unexaggerated DEM"}</span></div>
                    <button type="button" disabled={!terrainElevationReading} onClick={() => { setLockedTerrainElevation(terrainElevationReading); announce("Elevation reading locked into the current report context"); }}>Lock for report</button>
                  </div>
                  {lockedTerrainElevation && <p><strong>Report reading:</strong> {lockedTerrainElevation.feet.toFixed(0)} ft / {lockedTerrainElevation.meters.toFixed(0)} m at {lockedTerrainElevation.latitude.toFixed(5)}, {lockedTerrainElevation.longitude.toFixed(5)}. External display DEM; verify against an admitted elevation source before making an authoritative claim.</p>}
                </section>

                <section className="terrain-investigation" aria-labelledby="terrain-investigation-title">
                  <header><div><span>TERRAIN INVESTIGATION</span><h4 id="terrain-investigation-title">Relief → transect → profile → evidence</h4></div><strong>1× PHYSICAL DEFAULT</strong></header>
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
                    <input id="scene-height" type="range" min="0.1" max="2" step="0.1" value={verticalExaggeration} disabled={scenePreset !== "elevation-3d" || terrainState === "ERROR"} onChange={(event) => { const next = Number(event.target.value); verticalExaggerationRef.current = next; setVerticalExaggeration(next); }} />
                    <div><span>0.1×</span><span>1× physical</span><span>2×</span></div>
                    {scenePreset === "elevation-3d" && <div className="terrain-exaggeration-presets" role="group" aria-label="Terrain exaggeration presets">
                      {[1, 1.35, 1.75, 2].map((scale) => <button key={scale} type="button" aria-pressed={verticalExaggeration === scale} onClick={() => { verticalExaggerationRef.current = scale; setVerticalExaggeration(scale); }}>{scale.toFixed(scale === 1 ? 0 : 2).replace(/0$/, "")}×</button>)}
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
                    <p><strong>Live terrain:</strong> {terrainState === "READY" ? `DEM ready at ${verticalExaggeration.toFixed(2)}×` : terrainState === "ERROR" ? "DEM request failed; the 2D evidence path remains usable." : "Requesting attributed Terrarium elevation tiles…"}</p>
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

                <aside className="map-utility-boundary" data-tone="warning"><strong>3D preserves the 2D evidence path.</strong><p>Terrain 3D samples an external raster DEM for display and may exaggerate it; Structures 3D extrudes only provider-supplied building heights. Neither changes evidence, fills missing heights, or asserts a KFM release. The optional “Elevation extrusion concept” layer remains a separate synthetic fixture. Select any visible feature to inspect the same Evidence Drawer used in 2D.</p></aside>
              </section>}

              {mapUtilityView === "connections" && <section id="map-utility-view-connections" role="tabpanel" aria-labelledby="map-utility-tab-connections" className="map-utility-section source-connections-section">
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
                  <header><div><span>OFFICIAL SOURCE PIPELINES</span><h4 id="official-connection-ledger-title">Fixed Kansas adapters + disclosed raster services</h4></div><strong>{officialFeatureCount} FEATURES</strong></header>
                  <p>Only allowlisted endpoints are connected. Feed failures stay visible; zero features is time-stamped and never interpreted as statewide safety or completeness.</p>
                  <div className="official-connection-grid">{filteredOfficialContextConnections.map(({ source, visible, activeAtFrame, state, featureCount, retrievedAt, limitation, temporalSupport }) => <article className="official-connection-card" key={source.id} data-state={state} data-held={visible && !activeAtFrame}>
                    <header><div><span>{source.kind.replaceAll("_", " ")}</span><h5>{source.title}</h5><code>{source.endpointLabel}</code></div><strong>{visible && !activeAtFrame ? "HELD" : state.toUpperCase()}</strong></header>
                    <div className="official-connection-path"><span>OFFICIAL</span><i>→</i><span>{source.apiPath || source.managedAdapterPath ? "FIXED ADAPTER" : "WMS / TILES"}</span><i>→</i><span>MAP CONTEXT</span><i>⊣</i><span>EVIDENCE HELD</span></div>
                    <dl><div><dt>Mapped</dt><dd>{featureCount ?? (source.apiPath || source.managedAdapterPath ? "NOT LOADED" : "RASTER")}</dd></div><div><dt>Retrieved</dt><dd>{retrievedAt ? new Date(retrievedAt).toLocaleString() : source.freshness}</dd></div><div><dt>Cadence</dt><dd>{source.cadence}</dd></div><div><dt>Temporal support</dt><dd>{temporalSupport.axis.replaceAll("-", " ")} · {temporalSupport.supportedFrames.map(formatTimelineStep).join(", ")}</dd></div><div><dt>Evidence role</dt><dd>{source.evidenceRole.replaceAll("_", " ")}</dd></div></dl>
                    <p>{limitation ?? source.boundary}</p><aside><strong>Failure boundary</strong><span>{source.fallback}</span></aside>
                    <footer><button type="button" onClick={() => setOfficialContextVisible(source.id, !visible)}>{visible ? "Hide" : "Show"}</button>{source.apiPath && <button type="button" disabled={state === "loading"} onClick={() => void refreshOfficialContext(source.id as OfficialContextFeedId)}>Refresh</button>}{source.id === "usgs-streamflow" && <button type="button" disabled={state === "loading" || !activeAtFrame} onClick={() => void refreshStreamflow(streamflowRange, streamflowSelectedStationId)}>Refresh observations</button>}{source.id === "noaa-nwps-gauges" && <button type="button" disabled={state === "loading" || !activeAtFrame} onClick={() => void refreshNoaaHydrologyNetwork()}>Refresh status</button>}<a href={source.sourceUrl} target="_blank" rel="noreferrer">Source ↗</a><a href={source.serviceUrl} target="_blank" rel="noreferrer">{source.id === "raspberry-shake-stations" ? "StationView ↗" : "Service ↗"}</a></footer>
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
                <aside className="map-utility-boundary" data-tone="warning"><strong>Connection status is renderer health, not source admission.</strong><p>Registry cards expose site-local fixtures. The current view may contact only the external carriers disclosed above; provider resources and availability remain external. A READY source or successful query does not prove rights, freshness, evidence, policy approval, release, or publication.</p></aside>
              </section>}

              {mapUtilityView === "import" && <section id="map-utility-view-import" role="tabpanel" aria-labelledby="map-utility-tab-import" className="map-utility-section import-preview-section">
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

              {mapUtilityView === "compare" && <section id="map-utility-view-compare" role="tabpanel" aria-labelledby="map-utility-tab-compare" className="map-utility-section layer-compare-section">
                <div className="map-utility-section-heading"><span>COMPARE</span><h3>Time + layer investigation</h3><p>Compare catalog availability across two times, then inspect two registry layers without flattening source role, release posture, or sensitivity into a single score.</p></div>
                <SynchronizedComparison snapshot={comparisonSnapshot} layerA={compareLeft.id} layerB={compareRight.id} timeA={compareTimeA} timeB={compareTimeB} />
                <section className="temporal-compare-lab" aria-labelledby="temporal-compare-title">
                  <header><div><span>TIME A / TIME B</span><h4 id="temporal-compare-title">Catalog availability comparison</h4></div><strong>{temporalComparison.changedLayerCount} CHANGED</strong></header>
                  <div className="temporal-compare-selectors">
                    <label><span>Time A</span><select value={compareTimeA} onChange={(event) => setCompareTimeA(Number(event.target.value))}>{TIME_STEPS.map((step) => <option key={`a:${step}`} value={step}>{formatTimelineStep(step)}</option>)}</select></label>
                    <span aria-hidden="true">→</span>
                    <label><span>Time B</span><select value={compareTimeB} onChange={(event) => { const next = Number(event.target.value); setCompareTimeB(next); if (temporalMode === "comparison") { yearRef.current = next; setYear(next); setPreviewYear(next); } }}>{TIME_STEPS.map((step) => <option key={`b:${step}`} value={step}>{formatTimelineStep(step)}</option>)}</select></label>
                  </div>
                  <div className="temporal-compare-metrics" aria-label="Temporal catalog comparison summary">
                    <article><span>TIME A RECORDS</span><strong>{temporalComparison.timeARecordCount}</strong><small>{temporalComparison.timeALayerCount} layers</small></article>
                    <article><span>TIME B RECORDS</span><strong>{temporalComparison.timeBRecordCount}</strong><small>{temporalComparison.timeBLayerCount} layers</small></article>
                    <article><span>DELTA</span><strong>{temporalComparison.recordDelta >= 0 ? "+" : ""}{temporalComparison.recordDelta}</strong><small>catalog records</small></article>
                    <article><span>CHANGED</span><strong>{temporalComparison.changedLayerCount}</strong><small>layer catalogs</small></article>
                  </div>
                  <div className="temporal-compare-rows">
                    {temporalComparisonRows.map((row) => <article key={row.layerId}><header><strong>{row.title}</strong><span>{row.temporalMode.toUpperCase()}</span></header><div><span><b>{row.timeARecordCount}</b> at A</span><i aria-hidden="true">→</i><span><b>{row.timeBRecordCount}</b> at B</span><em>{row.enteredRecordIds.length} entered · {row.exitedRecordIds.length} exited</em></div></article>)}
                    {temporalComparisonRows.length === 0 && <div className="map-utility-empty"><strong>No visible catalog records at either time</strong><p>Show more layers or choose another comparison pair.</p></div>}
                  </div>
                  <div className="temporal-compare-actions"><button type="button" onClick={() => applyComparisonTime(compareTimeA, "A")}>Apply Time A</button><button type="button" onClick={() => applyComparisonTime(compareTimeB, "B")}>Apply Time B</button><button type="button" onClick={() => void copyTemporalComparison()}>Copy comparison</button></div>
                  <aside><strong>Interpretation boundary</strong><p>Entered and exited IDs report site-local fixture availability under each layer’s declared temporal rule. They are not observed change, imagery analysis, causation, or evidence of an event. Untimed context can appear at both times without proving persistence.</p></aside>
                </section>
                <div className="compare-section-divider"><span>LAYER A / LAYER B</span></div>
                <div className="layer-compare-selectors">
                  <label><span>Layer A</span><select value={compareLeft.id} onChange={(event) => { const next = event.target.value; setCompareLeftId(next); if (next === compareRight.id) setCompareRightId(compareLeft.id); }}>{LAYER_REGISTRY.map((layer) => <option key={layer.id} value={layer.id}>{layer.title}</option>)}</select></label>
                  <button type="button" onClick={() => { setCompareLeftId(compareRight.id); setCompareRightId(compareLeft.id); }} aria-label="Swap compared layers">⇄<span>Swap</span></button>
                  <label><span>Layer B</span><select value={compareRight.id} onChange={(event) => { const next = event.target.value; setCompareRightId(next); if (next === compareLeft.id) setCompareLeftId(compareRight.id); }}>{LAYER_REGISTRY.map((layer) => <option key={layer.id} value={layer.id}>{layer.title}</option>)}</select></label>
                </div>
                <div className="layer-compare-grid">
                  {[compareLeft, compareRight].map((layer, index) => <article key={`${index}:${layer.id}`} data-visible={visibility[layer.id]}>
                    <header><span>LAYER {index === 0 ? "A" : "B"} · {layer.domain}</span><strong>{layer.releaseState}</strong></header>
                    <h4>{layer.title}</h4><p>{layer.description}</p>
                    <dl>
                      <div><dt>Geometry / format</dt><dd>{layer.geometryType} · {layer.sourceType}</dd></div>
                      <div><dt>Temporal basis</dt><dd>{layer.validTimeExtent}</dd></div>
                      <div><dt>Source / release time</dt><dd>{layer.sourceTime} · {layer.releaseTime}</dd></div>
                      <div><dt>Freshness</dt><dd>{layer.freshnessState}</dd></div>
                      <div><dt>Public posture</dt><dd>{layer.publicStatus}</dd></div>
                      <div><dt>Evidence reference</dt><dd><code>{layer.evidenceReference}</code></dd></div>
                    </dl>
                    <aside><strong>Sensitivity boundary</strong><p>{layer.sensitivityNote}</p></aside>
                    <footer><span>{visibility[layer.id] ? "VISIBLE NOW" : "HIDDEN NOW"}</span><button type="button" onClick={() => zoomToLayer(layer)}>Show + zoom</button></footer>
                  </article>)}
                </div>
                <div className="layer-compare-actions"><button type="button" onClick={showComparedLayers}>Show both</button><button type="button" onClick={fitComparedLayers}>Fit both extents</button><button type="button" onClick={() => void copyLayerComparison()}>Copy comparison</button></div>
                <aside className="map-utility-boundary"><strong>Comparison is a read-only projection</strong><p>Side-by-side metadata helps reveal differences; it does not prove layer compatibility, equivalent authority, current source admission, policy approval, release readiness, or publication.</p></aside>
              </section>}

              {mapUtilityView === "display" && <section id="map-utility-view-display" role="tabpanel" aria-labelledby="map-utility-tab-display" className="map-utility-section">
                <div className="map-utility-section-heading"><span>DISPLAY</span><h3>Styles, projections + view profiles</h3><p>Style changes preserve registry layers, time, selection eligibility, measurement geometry, camera, and attribution.</p></div>
                <div className="map-control-group"><header><strong>Basemap style</strong><span>Display context · not evidence</span></header><div className="map-choice-grid">{(Object.keys(BASEMAPS) as BasemapKey[]).map((key) => <button key={key} type="button" aria-pressed={basemap === key} onClick={() => setBasemap(key)}><strong>{BASEMAPS[key].title}</strong><small>{BASEMAPS[key].note}</small></button>)}</div></div>
                <div className="map-control-group"><header><strong>Projection</strong><span>Camera display only</span></header><div className="map-choice-grid"><button type="button" aria-pressed={projection === "mercator"} onClick={() => setProjection("mercator")}><strong>Mercator</strong><small>Stable 2D inspection</small></button><button type="button" aria-pressed={projection === "globe"} onClick={() => setProjection("globe")}><strong>Globe</strong><small>MapLibre globe display</small></button></div></div>
                <div className="map-control-group"><header><strong>View profiles</strong><span>View state only · reversible</span></header><div className="map-profile-list">{MAP_VIEW_PROFILES.map((profile) => <article key={profile.id}><div><strong>{profile.title}</strong><p>{profile.summary}</p><small>{profile.year} · {profile.basemap} · {profile.visibleLayerIds.length} layers</small></div><button type="button" onClick={() => applyViewProfile(profile)}>Apply profile</button></article>)}</div></div>
                <button className="map-catalog-launch" type="button" onClick={openLayerCatalogFromUtility}>Open full Layer Catalog for visibility, opacity, order, legends, time, and trust metadata</button>
              </section>}

              {mapUtilityView === "measure" && <section id="map-utility-view-measure" role="tabpanel" aria-labelledby="map-utility-tab-measure" className="map-utility-section">
                <div className="map-utility-section-heading"><span>MEASURE</span><h3>Browser-local screen measurement</h3><p>Choose a geometry, then click the map to add points. Undo resumes a completed measurement for explicit editing.</p></div>
                <div className="map-control-group"><header><strong>Draw and measure</strong><span>{measureMode ? "ADDING POINTS" : measurementGeometryMode ? "COMPLETE / PAUSED" : analysisArea ? "RECTANGLE AOI SET" : "IDLE"}</span></header><div className="map-choice-grid map-draw-grid"><button type="button" aria-pressed={measurementGeometryMode === "point"} onClick={() => toggleMeasure("point")}><strong>Point</strong><small>One browser-local marker</small></button><button type="button" aria-pressed={measurementGeometryMode === "distance"} onClick={() => toggleMeasure("distance")}><strong>Line</strong><small>Distance approximation</small></button><button type="button" aria-pressed={measurementGeometryMode === "area"} onClick={() => toggleMeasure("area")}><strong>Polygon</strong><small>Area approximation</small></button><button type="button" aria-pressed={Boolean(analysisArea)} onClick={captureAnalysisArea} disabled={locationCameraRedacted}><strong>Rectangle</strong><small>Capture current viewport AOI</small></button></div><p className="map-control-note">Point, line, and polygon geometry stays in this browser. Rectangle captures the current viewport or use Shift-drag in report-area mode for a custom box. None is admitted evidence.</p></div>
                <div className="map-control-group"><header><strong>Units</strong><span>Also updates the MapLibre scale bar</span></header><div className="map-segmented-control"><button type="button" aria-pressed={measureUnit === "imperial"} onClick={() => changeMeasureUnit("imperial")}>Miles / sq mi</button><button type="button" aria-pressed={measureUnit === "metric"} onClick={() => changeMeasureUnit("metric")}>Kilometers / km²</button></div></div>
                <article className="map-measure-status" aria-live="polite"><span>{measurementGeometryMode?.toUpperCase() ?? "NO MEASUREMENT"}</span><strong>{measurement}</strong><small>{measureMode ? "Click the map to add points." : measurementGeometryMode ? "Finished geometry remains on the map until cleared." : "Select distance or area to begin."}</small></article>
                <div className="map-utility-actions"><button type="button" onClick={undoMeasurementPoint} disabled={!measurementGeometryMode}>Undo point</button><button type="button" onClick={finishMeasurement} disabled={!measureMode}>Finish</button><button type="button" onClick={clearMeasurement} disabled={!measurementGeometryMode}>Clear</button></div>
                <aside className="map-utility-boundary" data-tone="warning"><strong>Screen measurement — not survey, cadastral, legal, or evidence.</strong><p>Results are approximate, browser-local, and excluded from context receipts and public-safe exports.</p></aside>
              </section>}

              {mapUtilityView === "export" && <section id="map-utility-view-export" role="tabpanel" aria-labelledby="map-utility-tab-export" className="map-utility-section export-review-section">
                <div className="map-utility-section-heading"><span>EXPORT REVIEW</span><h3>Preview trust before download</h3><p>The outward artifact carries workspace, map context, separate temporal fields, visible layers, attribution, evidence posture, release/correction state, and redaction results.</p></div>
                <div className="export-review-summary" aria-label="Export review summary">
                  <article><span>FORMAT</span><strong>PUBLIC SAFE V2</strong><small>Site-local demonstration</small></article>
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
                </dl><p>Observation, ingestion, review, and correction transaction timestamps are not modeled as distinct fields in these site fixtures; the export says so instead of inventing them.</p></div>
                <article className="export-manifest-preview"><header><span>MANIFEST PREVIEW</span><strong>{exportReview.downloadAllowed ? "READY TO DOWNLOAD" : "BLOCKED"}</strong></header><pre>{JSON.stringify({ format: exportReview.payload.format, authority: exportReview.payload.authority, workspace: currentWorkspace, exportedAt: exportGeneratedAt, publicEffect: exportReview.payload.publicEffect, redaction: exportReview.payload.trust, effects: "NONE" }, null, 2)}</pre></article>
                <div className="map-utility-actions export-actions"><button type="button" onClick={() => void copyExportManifest()}>Copy reviewed manifest</button><button type="button" disabled={!exportReview.downloadAllowed} onClick={downloadPublicSafeExport}>Download public-safe JSON</button></div>
                <aside className="map-utility-boundary" data-tone="privacy"><strong>Evidence-preserving export boundary</strong><p>The download is a browser-local demonstration artifact. It cannot admit a source, prove an EvidenceBundle, change policy or review state, release, deploy, promote, or publish KFM data.</p></aside>
              </section>}

              {mapUtilityView === "diagnostics" && <section id="map-utility-view-diagnostics" role="tabpanel" aria-labelledby="map-utility-tab-diagnostics" className="map-utility-section">
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
                <aside className="map-utility-boundary"><strong>Renderer evidence boundary</strong><p>This Site runs MapLibre {EXPECTED_MAPLIBRE_VERSION} with same-origin worker assets, a selected external basemap or local style, optional external DEM terrain, and site-local GeoJSON fixtures. GitHub proves an exact dependency, a bounded concrete adapter, the renderer-neutral port, and deterministic Null runtime; broader authenticated, performance, governed-terrain, accessibility, and long-session readiness remain held.</p></aside>
              </section>}
            </div>
          </aside>

          {measurementGeometryMode && <div className="measurement-readout" role="region" aria-label="Active screen measurement"><span>{measurementGeometryMode.toUpperCase()} · {measureMode ? "ACTIVE" : "COMPLETE"}</span><strong aria-live="polite">{measurement}</strong><div><button type="button" onClick={undoMeasurementPoint}>Undo</button><button type="button" onClick={finishMeasurement} disabled={!measureMode}>Finish</button><button type="button" onClick={clearMeasurement}>Clear</button></div></div>}

          <div className="map-mobile-actions">
            <button type="button" onClick={() => openAtlasPanel("views")}>Views <b>{LIVING_ATLAS_VIEWS.length}</b></button>
            <button type="button" onClick={() => openAtlasPanel("layers")}>Layers <b>{visibleCount}</b></button>
            <button type="button" onClick={() => { if (selected) { setCurrentWorkspace("trust"); dismissMapUtilityWithoutFocus(); setRightOpen(true); setLeftOpen(false); setTimelineOpen(false); } }} disabled={!selected}>Evidence</button>
            <button type="button" onClick={() => { setCurrentWorkspace("explore"); dismissMapUtilityWithoutFocus(); setTimelineOpen(true); setLeftOpen(false); setRightOpen(false); }}>Time <b>{temporalScopeLabel}</b></button>
            <button type="button" onClick={() => openPrimaryWorkspace("reports", true)}>Report</button>
          </div>

          <div className="screenreader-status sr-only" aria-live="polite">{runtime.message}. Map center {formatCoordinate(view.center[1], "N", "S")}, {formatCoordinate(view.center[0], "E", "W")}. {visibleCount} layers visible. {selected ? `Selected ${selected.properties.title}; evidence state ${selectedEvidence?.label}.` : "No feature selected."}</div>
        </section>

        <aside ref={rightPanelRef} className="evidence-drawer" data-open={rightOpen} data-state={selected?.properties.evidenceState ?? "EMPTY"} aria-label="Evidence Drawer" aria-hidden={!rightOpen} inert={!rightOpen} aria-modal={isCompact && rightOpen || undefined} role={isCompact && rightOpen ? "dialog" : undefined}>
          <div className="panel-heading drawer-heading">
            <div><p className="panel-kicker">EVIDENCE DRAWER</p><h2>{selected?.properties.title ?? "Select a map feature"}</h2></div>
            <button className="icon-close" type="button" onClick={closeRightPanel} aria-label="Close Evidence Drawer">×</button>
          </div>
          {!selected ? <div className="drawer-empty"><span aria-hidden="true">⌖</span><h3>No feature selected</h3><p>Choose a map feature or use a Layer Catalog “Features” action. The map identifies a candidate; the registry supplies the stable context.</p></div> : <>
            <div className="drawer-state"><span className="state-icon" aria-hidden="true">{["ANSWER", "CORRECTED"].includes(selected.properties.evidenceState) ? "✓" : ["DENIED_BY_POLICY", "RESTRICTED_ACCESS", "ERROR"].includes(selected.properties.evidenceState) ? "!" : "○"}</span><span><small>{selected.properties.evidenceState}</small><strong>{selectedEvidence?.label}</strong></span></div>
            <p className="state-explanation">{selectedEvidence?.explanation}</p>
            {selected.kind === "basemap" && <div className="notice external-context-notice"><strong>Basemap context only</strong><p>This is real geographic context from the selected external display provider. It is not a KFM EvidenceBundle, released layer, source admission, scientific validation, or citation for a claim.</p></div>}
            {selectedTimeMismatch && <div className="drawer-time-warning" role="status"><strong>Selection is outside active time</strong><span>{selectedIsHeldOfficialContext ? `Current official context is held outside ${formatTimelineStep(OFFICIAL_CONTEXT_PRESENT_FRAME)}` : `Source ${formatTimelineStep(selected.properties.year)} · active ${temporalScopeLabel}`}. The normal map halo is hidden while the record stays available for inspection.</span></div>}
            {selectedLayerHidden && <div className="drawer-time-warning" role="status"><strong>Selected layer is hidden</strong><span>{selected.layer.title} remains available for inspection, but its normal map halo is hidden until the layer is visible again.</span></div>}
            {selectedEvidenceFiltered && <div className="drawer-time-warning" role="status"><strong>Selection is outside the map evidence filter</strong><span>The record remains available for inspection, but its map geometry and halo stay hidden until the {mapEvidenceFilter.replaceAll("_", " ")} filter is cleared or changed.</span></div>}
            <div className="drawer-tabs" role="tablist" aria-label="Evidence Drawer views">
              {drawerViews.map((tab, index) => <button key={tab} ref={(node) => { drawerTabRefs.current[index] = node; }} id={`drawer-tab-${tab}`} type="button" role="tab" aria-selected={drawerView === tab} aria-controls={`drawer-panel-${tab}`} tabIndex={drawerView === tab ? 0 : -1} onClick={() => activateDrawerView(tab)} onKeyDown={(event) => handleDrawerTabKeyDown(event, index)}>{drawerViewLabels[tab]}</button>)}
            </div>
            <div className="drawer-scroll">
              {drawerView === "evidence" && <section role="tabpanel" id="drawer-panel-evidence" aria-labelledby="drawer-tab-evidence" className="drawer-section">
                <p className="summary">{selected.properties.summary}</p>
                <dl className="evidence-facts">
                  <div><dt>Layer / domain</dt><dd>{selected.layer.title} · {selected.layer.domain}</dd></div>
                  <div><dt>Source role</dt><dd>{selected.properties.sourceRole}</dd></div>
                  <div><dt>Source organization</dt><dd>{selected.properties.sourceOrganization}</dd></div>
                  <div><dt>Spatial scope</dt><dd>{selected.properties.spatialScope}</dd></div>
                  <div><dt>Temporal scope</dt><dd>{selected.properties.temporalScope}</dd></div>
                  <div><dt>Last update / freshness</dt><dd>{selected.properties.lastUpdate} · {selected.properties.freshnessState}</dd></div>
                  <div><dt>Review / release</dt><dd>{selected.properties.reviewState} · {selected.properties.releaseState}</dd></div>
                  <div><dt>Evidence reference</dt><dd><code>{selected.properties.citation}</code></dd></div>
                  <div><dt>Official source</dt><dd>{selectedSourceCandidate ? <a href={selectedSourceCandidate.sourceUrl} target="_blank" rel="noreferrer">{selectedSourceCandidate.organization} portal ↗</a> : "Not available for this site-local record"}</dd></div>
                  <div><dt>Source admission</dt><dd>{selectedSourceCandidate ? `${(SOURCE_ADMISSION_BY_ID[selectedSourceCandidate.id] ?? "candidate").replaceAll("-", " ")} · checked ${selectedSourceCandidate.checkedAt}` : selected.kind === "basemap" ? "External display context" : "Site-local demonstration fixture"}</dd></div>
                </dl>
                <div className="notice"><strong>Limitations</strong><p>{selected.properties.uncertainty}</p></div>
                <div className="notice"><strong>Generalization / rights</strong><p>{selected.properties.generalizationNote} {selected.properties.rights}</p></div>
                {selected.properties.correctionState !== "NONE" && <div className="notice correction"><strong>Correction state</strong><p>{selected.properties.correctionState}</p></div>}
                <div className="drawer-actions"><button type="button" onClick={() => activateDrawerView("focus", true)}>Open Focus Mode</button><button type="button" onClick={() => openPrimaryWorkspace("reports", true)}>Add to report</button><button type="button" onClick={() => openPrimaryWorkspace("stories", true)}>Add to story</button><button type="button" onClick={(event) => openMapUtility("export", event.currentTarget)}>Review public-safe export</button></div>
              </section>}
              {drawerView === "metadata" && <section role="tabpanel" id="drawer-panel-metadata" aria-labelledby="drawer-tab-metadata" className="drawer-section">
                <h3>Registry-driven layer metadata</h3><dl className="evidence-facts">
                  <div><dt>Dataset</dt><dd>{selected.layer.datasetName}</dd></div><div><dt>Source / geometry</dt><dd>{selected.layer.sourceType} · {selected.layer.geometryType}</dd></div><div><dt>Zoom support</dt><dd>{selected.layer.minZoom}–{selected.layer.maxZoom}</dd></div><div><dt>Units</dt><dd>{selected.layer.units}</dd></div><div><dt>Valid time extent</dt><dd>{selected.layer.validTimeExtent}</dd></div><div><dt>Source time</dt><dd>{selected.layer.sourceTime}</dd></div><div><dt>Release time</dt><dd>{selected.layer.releaseTime}</dd></div><div><dt>Attribution</dt><dd>{selected.layer.attribution}</dd></div></dl>
                <div className="legend-detail"><strong>Legend</strong>{selected.layer.legend.map((item) => <p key={item.label}><i className={`legend-swatch ${item.shape}`} style={{ "--swatch": item.color } as React.CSSProperties} />{item.label}</p>)}</div>
              </section>}
              {drawerView === "lineage" && <section role="tabpanel" id="drawer-panel-lineage" aria-labelledby="drawer-tab-lineage" className="drawer-section">
                <h3>Selection-to-evidence trace</h3><ol className="lineage-list"><li><span>01</span><div><strong>MapLibre candidate</strong><small>queryRenderedFeatures identified a candidate only</small></div></li><li><span>02</span><div><strong>{selected.kind === "basemap" ? "External display context" : "Stable registry context"}</strong><small>{selected.featureId}</small></div></li><li><span>03</span><div><strong>{selected.kind === "basemap" ? "No KFM evidence resolution" : "Evidence resolution"}</strong><small>{selected.properties.citation}</small></div></li><li><span>04</span><div><strong>Policy / rights</strong><small>{selected.properties.evidenceState}</small></div></li><li><span>05</span><div><strong>Public-safe view</strong><small>{selected.kind === "basemap" ? "Context only · no claim support" : "Drawer + bounded Focus Mode"}</small></div></li></ol>
                <div className="boundary-law"><span>Renderer</span><b>≠</b><span>truth store</span><b>·</b><span>pixel</span><b>≠</b><span>proof</span></div>
              </section>}
              {drawerView === "focus" && <section role="tabpanel" id="drawer-panel-focus" aria-labelledby="drawer-tab-focus" className="drawer-section focus-mode">
                <div className="focus-heading"><span>FOCUS WORKBENCH · SITE-LOCAL DEMONSTRATION</span><strong>Deterministic · no live AI · no model endpoint</strong></div>
                <p>Focus Mode binds the current map context to admitted site fixtures, runs diagnostic closure checks, and returns exactly one finite outcome.</p>
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
          </>}
        </aside>

        <section ref={timelineRef} className="timeline-panel" aria-label="Timeline and temporal controls" aria-hidden={isCompact && !timelineOpen || undefined} inert={isCompact && !timelineOpen} aria-modal={isCompact && timelineOpen || undefined} role={isCompact && timelineOpen ? "dialog" : undefined}>
          <div className="timeline-compact">
            <button className="timeline-toggle" type="button" aria-expanded={timelineOpen} onClick={() => { if (timelineOpen) { closeTimelinePanel(); return; } setTimelineOpen(true); if (isCompact) { dismissMapUtilityWithoutFocus(); setLeftOpen(false); setRightOpen(false); } }}>
              <span>TIME SWEEP</span>
              <strong>{temporalScopeLabel}</strong>
              <small>{previewYear === year ? `${temporalMode.replaceAll("-", " ")} · ${timelineEraLabel(year)}` : `Previewing ${formatTimelineStep(previewYear)}`}</small>
            </button>
            <div className="timeline-controls">
              <button type="button" disabled={temporalMode === "comparison" || previousSweepFrame === null} onClick={() => stepTemporalSweep("reverse")} aria-label="Previous sweep frame">‹</button>
              <button type="button" aria-pressed={playing} disabled={reducedMotion || temporalMode === "snapshot" || temporalMode === "comparison" || temporalSequence.length < 2} onClick={toggleTemporalPlayback} aria-label={playing ? "Pause time sweep" : "Play time sweep"}>{playing ? "Ⅱ" : "▶"}</button>
              <button type="button" disabled={temporalMode === "comparison" || nextSweepFrame === null} onClick={() => stepTemporalSweep("forward")} aria-label="Next sweep frame">›</button>
            </div>
            <div className="timeline-track">
              <input type="range" min="0" max={timelineSteps.length - 1} value={Math.max(0, timelineSteps.indexOf(previewYear))} onChange={(event) => { setPreviewYear(timelineSteps[Number(event.target.value)]); setPlaying(false); }} aria-label="Preview demonstration time before committing" aria-valuetext={`Preview ${formatTimelineStep(previewYear)}; committed ${temporalScopeLabel}`} />
              <div className="timeline-ticks" style={{ "--timeline-columns": timelineSteps.length } as React.CSSProperties}>{timelineSteps.map((step) => <button key={step} type="button" aria-current={step === temporalQuery.frame ? "step" : undefined} aria-pressed={step === previewYear} data-active={step === previewYear} data-committed={step === temporalQuery.frame} data-major={TIMELINE_MAJOR_STEPS.has(step as (typeof TIME_STEPS)[number])} data-in-range={step >= sweepRangeStart && step <= sweepRangeEnd} onClick={() => { setPreviewYear(step); setPlaying(false); }} aria-label={`Preview ${formatTimelineStep(step)}; ${timelineEraLabel(step)}${step === temporalQuery.frame ? "; committed frame" : ""}${step < sweepRangeStart || step > sweepRangeEnd ? "; outside sweep range and will expand it if committed" : ""}`} title={`${formatTimelineStep(step)} · ${timelineEraLabel(step)}`}>{TIMELINE_MAJOR_STEPS.has(step as (typeof TIME_STEPS)[number]) ? <span>{formatTimelineStep(step)}</span> : <i aria-hidden="true" />}</button>)}</div>
            </div>
            <div className="timeline-commit-actions">
              <button type="button" disabled={previewYear === temporalQuery.frame} onClick={() => { setPlaying(false); commitTemporalFrame(previewYear, `Committed ${formatTimelineStep(previewYear)} to the map, evidence, report, and story context`); }}>Commit</button>
              <button className="timeline-reset" type="button" onClick={() => { setPlaying(false); commitTemporalFrame(OFFICIAL_CONTEXT_PRESENT_FRAME, "Returned to the operational-present frame"); }}>Present</button>
            </div>
          </div>

          {timelineOpen && <div className="timeline-detail">
            <section className="timeline-sweep-setup" aria-labelledby="timeline-sweep-title">
              <header><span>SEMANTIC TIME SWEEP</span><strong id="timeline-sweep-title">Sweep declared temporal context without inventing continuity</strong></header>
              <p>Preview is harmless; Commit changes the shared map clock. Exact features are filtered atomically and are never interpolated or carried forward; “through” layers retain their declared persistence rule. Gaps remain gaps.</p>
              <div className="timeline-semantic-controls">
                <label>Mode<select value={temporalMode} onChange={(event) => { const nextMode = event.target.value as TemporalSweepMode; setPlaying(false); setTemporalMode(nextMode); if (nextMode === "comparison") { commitTemporalFrame(compareTimeB); setMapUtilityView("compare"); setMapUtilityOpen(true); setMapContextOpen(false); } }}><option value="snapshot">Snapshot</option><option value="moving-window">Moving window</option><option value="event-stepping">Event stepping</option><option value="accumulation">Accumulation</option><option value="comparison">A / B comparison</option></select></label>
                <label>Step<select value={temporalStepRule} onChange={(event) => { setPlaying(false); setTemporalStepRule(event.target.value as TemporalStepRule); }}><option value="available-events">Event dates + bounds</option><option value="regular-calendar">All atlas ticks</option></select></label>
                <label>Frame cadence<select value={playbackSpeed} onChange={(event) => setPlaybackSpeed(Number(event.target.value) as PlaybackSpeed)}><option value={0.5}>Slow · 2.6 s</option><option value={1}>Normal · 1.3 s</option><option value={2}>Fast · 0.65 s</option></select></label>
                <label>Direction<select value={playbackDirection} onChange={(event) => { setPlaying(false); setPlaybackDirection(event.target.value as TemporalPlaybackDirection); }}><option value="forward">Forward</option><option value="reverse">Reverse</option></select></label>
                <label>At boundary<select value={playbackLoopMode} onChange={(event) => setPlaybackLoopMode(event.target.value as TemporalLoopMode)}><option value="stop">Stop</option><option value="loop">Loop</option></select></label>
                <label>Window<select value={movingWindowFrames} disabled={temporalMode !== "moving-window"} onChange={(event) => setMovingWindowFrames(Number(event.target.value))}><option value={2}>2 frames</option><option value={3}>3 frames</option><option value={5}>5 frames</option></select></label>
              </div>
              <div className="timeline-range-controls" aria-label="Sweep range">
                <label><span>Start</span><select value={sweepRangeStart} onChange={(event) => { const next = Number(event.target.value); setPlaying(false); if (next <= year) setSweepRangeStart(next); }}>{TIME_STEPS.map((step) => <option key={`start:${step}`} value={step} disabled={step > year}>{formatTimelineStep(step)}</option>)}</select></label>
                <span aria-hidden="true">→</span>
                <label><span>End</span><select value={sweepRangeEnd} onChange={(event) => { const next = Number(event.target.value); setPlaying(false); if (next >= year) setSweepRangeEnd(next); }}>{TIME_STEPS.map((step) => <option key={`end:${step}`} value={step} disabled={step < year}>{formatTimelineStep(step)}</option>)}</select></label>
                <strong>{temporalSequence.length} frame{temporalSequence.length === 1 ? "" : "s"}</strong>
              </div>
              <p className="timeline-axis-note"><strong>FULL TEMPORAL CAPACITY · 4.54 GA BP TO 2026</strong> · Deep-time and intermediate ticks are capacity markers, not claims. Frame spacing and cadence are ordinal, not proportional to elapsed time. The active query uses each layer’s declared feature-year axis; source, retrieval, release, review, and correction clocks remain separate metadata.</p>
              <div className="timeline-motion-controls">
                <label><input type="checkbox" checked={dynamicEffects && !reducedMotion} disabled={reducedMotion} onChange={(event) => setDynamicEffects(event.target.checked)} /> Ambient layer motion</label>
                <small>{reducedMotion ? "System reduced-motion is active: autoplay and ambient movement are off; stepping remains available." : "Synthetic water, smoke, fire, rail, and place motion is presentation only. Live HMS smoke remains tied to provider Start/End intervals; no visual motion encodes velocity, intensity, or measured change."}</small>
              </div>
              <div className="timeline-era-jumps" aria-label="Preview named time ranges">{TIMELINE_JUMPS.map((jump) => <button key={jump.label} type="button" data-active={jump.year === previewYear} onClick={() => { setPreviewYear(jump.year); setPlaying(false); }}>{jump.label}<small>{formatTimelineStep(jump.year)}</small></button>)}</div>
              <div className="timeline-primary-actions"><button type="button" onClick={loadTemporalEventStack}>Load event stack</button><button type="button" onClick={() => openPrimaryWorkspace("stories", true)}>Capture frame for story</button></div>
            </section>

            <section className="timeline-frame-readout" aria-labelledby="timeline-frame-title">
              <header role="status" aria-live="polite" aria-atomic="true"><span>COMMITTED FRAME</span><strong id="timeline-frame-title">{temporalScopeLabel}</strong><small>{playing ? `Playing ${playbackDirection}; pauses when hidden` : "Paused"} · {temporalFramePosition ?? "off-sequence"}/{temporalSequence.length}</small></header>
              <div className="timeline-frame-metrics">
                <article><span>REGISTRY RECORDS</span><strong>{temporalFrameSummary.timedRecordCount}</strong></article>
                <article><span>DOMAINS</span><strong>{temporalFrameSummary.activeDomainCount}</strong></article>
                <article><span>ENTERED</span><strong>{temporalFrameSummary.entered.length}</strong></article>
                <article><span>EXITED</span><strong>{temporalFrameSummary.exited.length}</strong></article>
              </div>
              <div className="timeline-change-list">
                <div><span>{comparisonTemporalFrame === null ? "NO ADJACENT REFERENCE FRAME" : `ENTERED FROM ${formatTimelineStep(comparisonTemporalFrame)}`}</span>{temporalFrameSummary.entered.slice(0, 3).map((record) => <small key={`in:${record.id}`}>+ {record.title} · {record.domain}</small>)}{temporalFrameSummary.entered.length === 0 && <small>No entered records</small>}</div>
                <div><span>EXITED</span>{temporalFrameSummary.exited.slice(0, 3).map((record) => <small key={`out:${record.id}`}>− {record.title} · {record.domain}</small>)}{temporalFrameSummary.exited.length === 0 && <small>No exited records</small>}</div>
              </div>
              <div className="timeline-domain-links"><span>VISIBLE REGISTRY CO-PRESENCE</span>{temporalFrameSummary.domainPairs.slice(0, 4).map((pair) => <small key={pair.id}>{pair.leftDomain} ({pair.leftRecordCount}) ↔ {pair.rightDomain} ({pair.rightRecordCount})</small>)}{temporalFrameSummary.domainPairs.length === 0 && <small>Show time-aware layers from at least two domains to form a shared-frame link.</small>}<p>Counts use visible registry layers and the evidence filter, not viewport or zoom. Shared frame is not spatial overlap, correlation, direction, lag, or causation.</p></div>
              <div className="availability-bars" aria-label="Time-aware record count by ordinal timeline frame; gold is preview and an outline marks committed time">{timelineSteps.map((step) => <i key={step} data-active={step === previewYear} data-committed={step === temporalQuery.frame} data-in-range={step >= sweepRangeStart && step <= sweepRangeEnd} title={`${formatTimelineStep(step)} · ${availabilityByStep[step]} compatible time-aware record${availabilityByStep[step] === 1 ? "" : "s"}`} style={{ height: `${Math.min(52, 12 + availabilityByStep[step] * 5)}px` }}><b>{availabilityByStep[step]}</b></i>)}</div>
            </section>

            <section className="timeline-live-context" data-held={withheldOfficialCount > 0} aria-labelledby="timeline-live-title">
              <header><span>REAL OFFICIAL CONTEXT</span><strong id="timeline-live-title">{withheldOfficialCount > 0 ? `${withheldOfficialCount} current source${withheldOfficialCount === 1 ? "" : "s"} held` : `${visibleOfficialCount} selected · ${officialFeatureCount} loaded features`}</strong></header>
              {withheldOfficialCount > 0
                ? <p>Selected current-only official overlays do not rewind. They are temporarily hidden from this historical frame and will return at {formatTimelineStep(OFFICIAL_CONTEXT_PRESENT_FRAME)} without changing your source choices.</p>
                : <p>{officialReadyCount}/{OFFICIAL_CONTEXT_SOURCES.length} official adapters have a settled state. Latest Site retrieval: {officialLatestRetrievedAt ? `${officialLatestRetrievedAt.slice(0, 19).replace("T", " ")} UTC` : "not yet retrieved"}.</p>}
              <dl>
                <div><dt>Phenomenon clock</dt><dd>{temporalScopeLabel}</dd></div>
                <div><dt>Live-source clock</dt><dd>{year === OFFICIAL_CONTEXT_PRESENT_FRAME ? "Operational present only" : "WITHHELD FROM HISTORICAL FRAME"}</dd></div>
                <div><dt>Interpolation</dt><dd>OFF</dd></div>
                <div><dt>Authority effect</dt><dd>NONE · context only</dd></div>
              </dl>
              <p className="timeline-reference-note">Untimed registry layers, the selected basemap, and interactive terrain remain present-day orientation context across frames; they are excluded from entered/exited metrics and cannot prove historical persistence. Choose Midnight or Prairie to avoid an external basemap request.</p>
              <p className="timeline-trust-note">A time sweep changes renderer filters and captured context. It cannot admit, correct, approve, release, deploy, or publish data.</p>
            </section>
            <button className="icon-close timeline-close" type="button" onClick={closeTimelinePanel} aria-label="Close timeline">×</button>
          </div>}
        </section>

        <footer className="status-bar" aria-label="Map status">
          <span><b>{activeAtlasView?.title ?? "Kansas Overview"}</b> · {selected?.properties.title ?? "Kansas statewide"}</span>
          <span>{mapRepresentationLabel}</span>
          <span>MapLibre {EXPECTED_MAPLIBRE_VERSION} · terrain context only</span>
        </footer>
      </main>

      <div className="toast" role="status" aria-live="polite" data-visible={Boolean(toast)}>{toast}</div>
    </div>
  );
}
