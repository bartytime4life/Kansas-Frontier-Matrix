Warning: truncated output (original token count: 71731)
Total output lines: 3959

"use client";

import { useCallback, useEffect, useMemo, useRef, useState, useSyncExternalStore } from "react";
import SiteLayerLibrary from "./site-layer-library";
import { createRequestedLayerStore } from "./site-requested-layer-state";
import { INSPECTED_DEMO_IDS } from "./site-layer-library-metadata";
import type { Feature, Geometry } from "geojson";
import {
  createNullMapRuntime,
  type MapRuntimeCamera,
  type MapRuntimePort,
} from "@kfm/maplibre";
import {
  CATEGORY_ORDER,
  findFeature,
  LAYER_REGISTRY,
  SEARCH_INDEX,
  TIME_STEPS,
  type EvidenceState,
  type FeatureProperties,
  type LayerRecord,
  type SearchItem,
} from "./explorer-data";
import {
  BASEMAPS,
  lngLatToTile,
  screenRectToBounds,
  type AtmospherePreset,
  type BasemapKey,
} from "./map-runtime";
import {
  inspectableFeatureId,
  isFeatureAvailableAtTime,
  isLayerAvailableAtTime,
  MAP_CAPABILITY_GATES,
  MAP_VIEW_PROFILES,
  MAPLIBRE_REPOSITORY_STATUS,
  type MapUtilityView,
  type MapViewProfile,
  type MeasureUnit,
} from "./map-interface";
import {
  LIFECYCLE_GATES,
  REPOSITORY_SNAPSHOT,
  REPOSITORY_UPDATES,
  TRANSITION_BOUNDARIES,
  type RepositoryUpdateState,
} from "./repository-updates";
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
  SOURCE_CANDIDATES,
  SOURCE_DOMAINS,
  SOURCE_GAPS,
} from "./source-intelligence";
import {
  buildFocusActionProposals,
  buildFocusGateTrace,
  FOCUS_INTENTS,
  focusIntentNarrative,
  focusResultForState,
  isFeatureTimeMismatch,
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
  buildLocalImportPreview,
  IMPORT_PREVIEW_MAX_BYTES,
  importPreviewAudit,
  type LocalImportPreview,
} from "./import-preview";
import { parseSavedWorkspaces } from "./workspace-storage";
import WaveformPreviewPanel from "./waveform-preview-panel";

type ViewState = { center: [number, number]; zoom: number; bearing: number; pitch: number };
type MapBoundsState = { west: number; south: number; east: number; north: number };
type MapAreaDrawBox = { left: number; top: number; width: number; height: number };
type RuntimeState = { kind: "loading" | "ready" | "degraded" | "error"; message: string };
type DrawerView = "evidence" | "metadata" | "lineage" | "focus";
type MeasureMode = "distance" | "area" | null;
type RepositoryView = "updates" | "functions" | "scenario" | "runtime" | "transitions" | "readiness" | "sources";
type SourceObservatoryView = "candidates" | "corpus" | "gaps";
type GovernedRoute = "/bootstrap" | "/layers" | "/evidence" | "/focus";
type GovernedMethod = "GET" | "POST";
type PublicWorkspaceId = "explore" | "knowledge" | "features" | "trust";
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
  basemap: BasemapKey;
  projection: "mercator" | "globe";
  scene?: {
    preset: ScenePresetId;
    verticalExaggeration: number;
    atmosphere: AtmospherePreset;
    lightAzimuth: number;
    fieldOfView: number;
  };
  analysisArea?: MapBoundsState | null;
  temporalComparison?: {
    timeA: number;
    timeB: number;
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

type SelectedContext = {
  featureId: string;
  layerId: string;
  layer: LayerRecord;
  properties: FeatureProperties;
  geometry: Feature<Geometry>;
};

const KANSAS_VIEW: ViewState = { center: [-98.38, 38.48], zoom: 5.45, bearing: 0, pitch: 0 };
const EXPECTED_MAPLIBRE_VERSION = "6.6.0";
const MAP_RUNTIME_CONSUMER_HOLD = "DIRECT_CONSUMER_MIGRATION_HOLD";
const SUPPORTED_CONTEXT_BOUNDS = Object.freeze({ west: -104.8, south: 34.8, east: -92, north: 42.2 });
const defaultVisibility = Object.fromEntries(LAYER_REGISTRY.map((layer) => [layer.id, layer.defaultVisibility]));
const defaultOpacity = Object.fromEntries(LAYER_REGISTRY.map((layer) => [layer.id, layer.defaultOpacity]));
const defaultOrder = LAYER_REGISTRY.map((layer) => layer.id);
const interactiveLayerIds = LAYER_REGISTRY.flatMap((layer) => layer.renderers.filter((renderer) => renderer.interactive).map((renderer) => renderer.id));
const layerDomains = ["ALL", ...Array.from(new Set(LAYER_REGISTRY.map((layer) => layer.domain))).sort()] as const;
const drawerViews = ["evidence", "metadata", "lineage", "focus"] as const satisfies readonly DrawerView[];
const mapUtilityViews = ["report", "inspect", "navigate", "scene", "connections", "import", "compare", "display", "measure", "export", "diagnostics"] as const satisfies readonly MapUtilityView[];
const mapUtilityLabels: Record<MapUtilityView, string> = {
  report: "Report",
  navigate: "Navigate",
  inspect: "Inspect",
  scene: "Scene",
  connections: "Sources",
  import: "Import",
  compare: "Compare",
  display: "Display",
  measure: "Measure",
  export: "Export",
  diagnostics: "Diagnostics",
};
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

const timelineEraLabel = (value: number) => {
  if (value <= -541_000_000) return "Deep geologic time";
  if (value <= -2_580_000) return "Phanerozoic geologic time";
  if (value <= -11_700) return "Quaternary deep time";
  if (value < 1) return "Archaeological time capacity";
  if (value < 1541) return "Early human record capacity";
  if (value < 1854) return "Early historical capacity";
  if (value < 2000) return "Historical record";
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

const scaleAtView = (view: ViewState) => {
  const metersPerPixel = (156543.03 * Math.cos((view.center[1] * Math.PI) / 180)) / 2 ** view.zoom;
  return metersPerPixel >= 1000 ? `≈ ${(metersPerPixel / 1000).toFixed(1)} km/px` : `≈ ${Math.round(metersPerPixel)} m/px`;
};

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

export default function Home() {
  const mapContainerRef = useRef<HTMLDivElement>(null);
  const mapRuntimeRef = useRef<MapRuntimePort | null>(null);
  const yearRef = useRef<number>(2026);
  const basemapRef = useRef<BasemapKey>("midnight");
  const projectionRef = useRef<"mercator" | "globe">("mercator");
  const verticalExaggerationRef = useRef(1);
  const atmospherePresetRef = useRef<AtmospherePreset>("night");
  const lightAzimuthRef = useRef(210);
  const fieldOfViewRef = useRef(36);
  const gestureModeRef = useRef<"cooperative" | "direct">("cooperative");
  const sceneOrbitTimerRef = useRef<number | null>(null);
  const selectedRef = useRef<SelectedContext | null>(null);
  const measureModeRef = useRef<MeasureMode>(null);
  const measurementGeometryModeRef = useRef<MeasureMode>(null);
  const measureUnitRef = useRef<MeasureUnit>("imperial");
  const measureCoordinatesRef = useRef<[number, number][]>([]);
  const analysisAreaRef = useRef<MapBoundsState | null>(null);
  const areaDrawRef = useRef<{ pointerId: number; startX: number; startY: number; width: number; height: number } | null>(null);
  const importInputRef = useRef<HTMLInputElement>(null);
  const importInspectionGenerationRef = useRef(0);
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

  // A single synchronous owner serves both imperative Library transactions and
  // all legacy app writers. React renders its immutable subscribed snapshot.
  const [requestedLayers] = useState(() => createRequestedLayerStore({
    visibility: defaultVisibility, opacity: defaultOpacity, layerOrder: defaultOrder,
  }, INSPECTED_DEMO_IDS));
  const { visibility, opacity, layerOrder, membershipEpoch } = useSyncExternalStore(
    requestedLayers.subscribe, requestedLayers.getSnapshot, requestedLayers.getServerSnapshot,
  );
  const { setVisibility, setOpacity, setLayerOrder } = requestedLayers;
  const [basemap, setBasemap] = useState<BasemapKey>("midnight");
  const [view, setView] = useState<ViewState>(KANSAS_VIEW);
  const [scenePreset, setScenePreset] = useState<ScenePresetId>("overview-2d");
  const [verticalExaggeration, setVerticalExaggeration] = useState(1);
  const [atmospherePreset, setAtmospherePreset] = useState<AtmospherePreset>("night");
  const [lightAzimuth, setLightAzimuth] = useState(210);
  const [fieldOfView, setFieldOfView] = useState(36);
  const [gestureMode, setGestureMode] = useState<"cooperative" | "direct">("cooperative");
  const [sceneOrbiting, setSceneOrbiting] = useState(false);
  const [pointer, setPointer] = useState<[number, number]>(KANSAS_VIEW.center);
  const [mapViewportBounds, setMapViewportBounds] = useState<MapBoundsState>(SUPPORTED_CONTEXT_BOUNDS);
  const [analysisArea, setAnalysisArea] = useState<MapBoundsState | null>(null);
  const [areaDrawMode, setAreaDrawMode] = useState(false);
  const [areaDrawBox, setAreaDrawBox] = useState<MapAreaDrawBox | null>(null);
  const [importPreview, setImportPreview] = useState<LocalImportPreview | null>(null);
  const [importError, setImportError] = useState("");
  const [importBusy, setImportBusy] = useState(false);
  const [cameraHistoryIndex, setCameraHistoryIndex] = useState(0);
  const [cameraHistoryLength, setCameraHistoryLength] = useState(1);
  const [runtime, setRuntime] = useState<RuntimeState>({ kind: "loading", message: "Starting the renderer-neutral map boundary…" });
  const [locationCameraRedacted, setLocationCameraRedacted] = useState(false);
  const [selected, setSelected] = useState<SelectedContext | null>(null);
  const [leftOpen, setLeftOpen] = useState(false);
  const [rightOpen, setRightOpen] = useState(false);
  const [timelineOpen, setTimelineOpen] = useState(true);
  const [drawerView, setDrawerView] = useState<DrawerView>("evidence");
  const [focusStage, setFocusStage] = useState<FocusStage>("outcome");
  const [focusIntent, setFocusIntent] = useState<FocusIntentId>("explain");
  const [pendingFocusAction, setPendingFocusAction] = useState<FocusActionProposal | null>(null);
  const [layerQuery, setLayerQuery] = useState("");
  const [layerDomain, setLayerDomain] = useState<(typeof layerDomains)[number]>("ALL");
  const [globalQuery, setGlobalQuery] = useState("");
  const [expandedLayers, setExpandedLayers] = useState<Set<string>>(new Set());
  const [year, setYear] = useState<number>(2026);
  const [playing, setPlaying] = useState(false);
  const [toolsExpanded, setToolsExpanded] = useState(false);
  const [measureMode, setMeasureMode] = useState<MeasureMode>(null);
  const [measurementGeometryMode, setMeasurementGeometryMode] = useState<MeasureMode>(null);
  const [measureUnit, setMeasureUnit] = useState<MeasureUnit>("imperial");
  const [measurement, setMeasurement] = useState("Select a measurement tool");
  const [mapUtilityOpen, setMapUtilityOpen] = useState(false);
  const [mapUtilityView, setMapUtilityView] = useState<MapUtilityView>("navigate");
  const [mapFeatureQuery, setMapFeatureQuery] = useState("");
  const [mapFeatureLayer, setMapFeatureLayer] = useState("ALL");
  const [connectionQuery, setConnectionQuery] = useState("");
  const [connectionFilter, setConnectionFilter] = useState<"ALL" | "VISIBLE" | "HELD">("ALL");
  const [sourceActivity, setSourceActivity] = useState<Record<string, "WAITING" | "UPDATING" | "SETTLED">>(
    Object.fromEntries(LAYER_REGISTRY.map((layer) => [layer.id, "WAITING"])),
  );
  const [sourceProbeCounts, setSourceProbeCounts] = useState<Record<string, number>>({});
  const [mapQueryCandidates, setMapQueryCandidates] = useState<readonly MapQueryCandidate[]>([]);
  const [inspectViewportOnly, setInspectViewportOnly] = useState(false);
  const [inspectVisibleLayersOnly, setInspectVisibleLayersOnly] = useState(false);
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
  const [activeTransitionId, setActiveTransitionId] = useState(TRANSITION_BOUNDARIES[0].id);
  const [governedRoute, setGovernedRoute] = useState<GovernedRoute>("/bootstrap");
  const [governedMethod, setGovernedMethod] = useState<GovernedMethod>("GET");
  const [sourceObservatoryView, setSourceObservatoryView] = useState<SourceObservatoryView>("candidates");
  const [sourceQuery, setSourceQuery] = useState("");
  const [sourceDomain, setSourceDomain] = useState("ALL");
  const [exportGeneratedAt, setExportGeneratedAt] = useState("PREVIEW_NOT_OPENED");
  const [reportGeneratedAt, setReportGeneratedAt] = useState("LIVE PREVIEW");
  const [reportTitle, setReportTitle] = useState("Kansas map data report");
  const [reportScope, setReportScope] = useState<ReportScope>("VIEWPORT");
  const [reportDetail, setReportDetail] = useState<ReportDetail>("STANDARD");
  const [reportLayerIds, setReportLayerIds] = useState<string[]>(() => LAYER_REGISTRY.filter((layer) => layer.defaultVisibility).map((layer) => layer.id));
  const [reportSections, setReportSections] = useState<Record<ReportSection, boolean>>(defaultReportSections);
  const [reportQuery, setReportQuery] = useState("");
  const [reportEvidenceFilter, setReportEvidenceFilter] = useState<EvidenceState | "ALL">("ALL");
  const [workspaceName, setWorkspaceName] = useState("");
  const [savedWorkspaces, setSavedWorkspaces] = useState<WorkspaceSnapshot[]>([]);
  const [runtimeSeamState, setRuntimeSeamState] = useState<RuntimeSeamState>("IDLE");
  const [runtimeSeamReason, setRuntimeSeamReason] = useState("Awaiting deterministic replay");
  const [toast, setToast] = useState("");
  const [isCompact, setIsCompact] = useState(false);
  const [sourceStates] = useState<Record<string, "held">>(
    Object.fromEntries(LAYER_REGISTRY.map((layer) => [layer.id, "held"])),
  );

  const debouncedGlobalQuery = useDebounced(globalQuery, 140);
  const debouncedLayerQuery = useDebounced(layerQuery, 140);

  useEffect(() => { yearRef.current = year; }, [year]);
  useEffect(() => { basemapRef.current = basemap; }, [basemap]);
  useEffect(() => { projectionRef.current = projection; }, [projection]);
  useEffect(() => { verticalExaggerationRef.current = verticalExaggeration; }, [verticalExaggeration]);
  useEffect(() => { atmospherePresetRef.current = atmospherePreset; }, [atmospherePreset]);
  useEffect(() => { lightAzimuthRef.current = lightAzimuth; }, [lightAzimuth]);
  useEffect(() => { fieldOfViewRef.current = fieldOfView; }, [fieldOfView]);
  useEffect(() => { gestureModeRef.current = gestureMode; }, [gestureMode]);
  useEffect(() => {
    const restoreSavedWorkspaces = window.setTimeout(() => {
      try {
        const restored = parseSavedWorkspaces(window.localStorage.getItem(WORKSPACE_STORAGE_KEY));
        setSavedWorkspaces(restored as WorkspaceSnapshot[]);

      } catch { /* Device-local workspace storage is optional. */ }
    }, 0);
    return () => window.clearTimeout(restoreSavedWorkspaces);
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
  const temporalComparison = useMemo(
    () => buildTemporalComparison(activeLayers, compareTimeA, compareTimeB),
    [activeLayers, compareTimeA, compareTimeB],
  );
  const temporalComparisonRows = useMemo(
    () => temporalComparison.layers.filter((layer) => layer.timeARecordCount > 0 || layer.timeBRecordCount > 0),
    [temporalComparison],
  );
  const temporalNoData = useMemo(() => activeLayers.filter((layer) => layer.temporal?.mode === "exact" && !layer.temporal.years.includes(year)), [activeLayers, year]);
  const availabilityByStep = useMemo(() => Object.fromEntries(TIME_STEPS.map((step) => [step, activeLayers.filter((layer) => isLayerAvailableAtTime(layer, step)).length])), [activeLayers]);
  const sourceStateCounts = useMemo(() => ({
    held: Object.values(sourceStates).filter((state) => state === "held").length,
  }), [sourceStates]);
  const sourceConnections = useMemo(() => LAYER_REGISTRY.map((layer) => {
    const compatibleFeatures = layer.data.features.filter((feature) => isFeatureAvailableAtTime(layer, feature.properties.year, year));
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
  }), [mapViewportBounds, sourceActivity, sourceProbeCounts, sourceStates, visibility, year]);
  const filteredSourceConnections = useMemo(() => {
    const query = connectionQuery.trim().toLowerCase();
    return sourceConnections.filter((connection) => {
      if (connectionFilter === "VISIBLE" && !connection.visible) return false;
      if (connectionFilter === "HELD" && connection.state !== "held") return false;
      return !query || `${connection.layer.title} ${connection.layer.id} ${connection.layer.sourceId} ${connection.layer.domain} ${connection.layer.sourceType}`.toLowerCase().includes(query);
    });
  }, [connectionFilter, connectionQuery, sourceConnections]);
  const centerTile = useMemo(() => lngLatToTile(view.center[0], view.center[1], view.zoom), [view.center, view.zoom]);
  const maplibreCapabilityChecks = useMemo(() => {
    return [
      {
        id: "package-seam",
        label: "Package-owned candidate",
        detail: `@kfm/maplibre owns exact ${EXPECTED_MAPLIBRE_VERSION}; this Site imports only the renderer-neutral package surface`,
        state: "READY",
      },
      {
        id: "consumer-runtime",
        label: "Sites consumer runtime",
        detail: `${MAP_RUNTIME_CONSUMER_HOLD} · NullMapRuntime performs no renderer, worker, WebGL, source, tile, or network work`,
        state: "HOLD",
      },
      {
        id: "module-worker",
        label: "Renderer module + worker",
        detail: "NOT RUN in this Site; package-owned Vite fixture evidence does not activate this consumer",
        state: "HOLD",
      },
      {
        id: "style",
        label: "Style + projection",
        detail: `${BASEMAPS[basemap].title} and ${projection} are view-state choices only; no renderer style is loaded`,
        state: "HOLD",
      },
      {
        id: "sources",
        label: "Site-local layer descriptors",
        detail: `${sourceStateCounts.held}/${LAYER_REGISTRY.length} held from renderer loading; catalog and evidence metadata remain readable`,
        state: "HOLD",
      },
      {
        id: "interaction",
        label: "Renderer interactions",
        detail: "Renderer-neutral camera history, north-up box queries, and report-area filtering are available; hit testing, hover, cluster expansion, popups, and screen measurement remain held",
        state: "HOLD",
      },
      {
        id: "readiness",
        label: "Broader browser readiness",
        detail: "The governed twelve-probe packet remains pending; this fail-closed repair creates no readiness result",
        state: "HOLD",
      },
    ] as const;
  }, [basemap, projection, sourceStateCounts.held]);
  const mapFeatureIndex = useMemo(() => {
    const query = mapFeatureQuery.trim().toLowerCase();
    return LAYER_REGISTRY
      .filter((layer) => mapFeatureLayer === "ALL" || layer.id === mapFeatureLayer)
      .filter((layer) => !inspectVisibleLayersOnly || visibility[layer.id])
      .flatMap((layer) => layer.data.features
        .filter((feature) => isFeatureAvailableAtTime(layer, feature.properties.year, year))
        .map((feature) => ({ layer, feature })))
      .filter(({ feature }) => !inspectViewportOnly || (
        feature.properties.focusLng >= mapViewportBounds.west
        && feature.properties.focusLng <= mapViewportBounds.east
        && feature.properties.focusLat >= mapViewportBounds.south
        && feature.properties.focusLat <= mapViewportBounds.north
      ))
      .filter(({ layer, feature }) => !query || `${feature.properties.title} ${feature.properties.fid} ${feature.properties.evidenceState} ${layer.title}`.toLowerCase().includes(query));
  }, [inspectViewportOnly, inspectVisibleLayersOnly, mapFeatureLayer, mapFeatureQuery, mapViewportBounds, visibility, year]);
  const analysisAreaRecordCount = useMemo(() => analysisArea
    ? LAYER_REGISTRY.reduce((count, layer) => count + layer.data.features.filter((feature) => (
      isFeatureAvailableAtTime(layer, feature.properties.year, year)
      && isFeatureInsideBounds(feature.properties, analysisArea)
    )).length, 0)
    : 0, [analysisArea, year]);
  const analysisAreaOverlay = useMemo(() => {
    if (!analysisArea) return null;
    const longitudeSpan = mapViewportBounds.east - mapViewportBounds.west;
    const latitudeSpan = mapViewportBounds.north - mapViewportBounds.south;
    if (longitudeSpan <= 0 || latitudeSpan <= 0) return null;
    const left = clamp(((analysisArea.west - mapViewportBounds.west) / longitudeSpan) * 100, 0, 100);
    const right = clamp(((analysisArea.east - mapViewportBounds.west) / longitudeSpan) * 100, 0, 100);
    const top = clamp(((mapViewportBounds.north - analysisArea.north) / latitudeSpan) * 100, 0, 100);
    const bottom = clamp(((mapViewportBounds.north - analysisArea.south) / latitudeSpan) * 100, 0, 100);
    if (right <= left || bottom <= top) return null;
    return { left, top, width: right - left, height: bottom - top };
  }, [analysisArea, mapViewportBounds]);
  const matchesReportRecord = useCallback((layer: LayerRecord, properties: FeatureProperties) => {
    if (!reportLayerIds.includes(layer.id)) return false;
    if (reportEvidenceFilter !== "ALL" && properties.evidenceState !== reportEvidenceFilter) return false;
    const query = reportQuery.trim().toLowerCase();
    if (query && !`${properties.title} ${properties.fid} ${properties.summary} ${properties.sourceOrganization} ${properties.sourceRole} ${properties.evidenceState} ${layer.title} ${layer.domain}`.toLowerCase().includes(query)) return false;
    if (reportScope === "SELECTION") {
      return Boolean(selected && selected.layerId === layer.id && selected.featureId === properties.fid);
    }
    if (reportScope === "VISIBLE_LAYERS" && !visibility[layer.id]) return false;
    if (reportScope === "VIEWPORT") {
      return properties.focusLng >= mapViewportBounds.west
        && properties.focusLng <= mapViewportBounds.east
        && properties.focusLat >= mapViewportBounds.south
        && properties.focusLat <= mapViewportBounds.north;
    }
    if (reportScope === "ANALYSIS_AREA") {
      return Boolean(analysisArea && isFeatureInsideBounds(properties, analysisArea));
    }
    return true;
  }, [analysisArea, mapViewportBounds, reportEvidenceFilter, reportLayerIds, reportQuery, reportScope, selected, visibility]);
  const reportRecords = useMemo(() => LAYER_REGISTRY
    .filter((layer) => reportLayerIds.includes(layer.id))
    .flatMap((layer) => layer.data.features
      .filter((feature) => reportScope === "SELECTION"
        || isFeatureAvailableAtTime(layer, feature.properties.year, year))
      .filter((feature) => matchesReportRecord(layer, feature.properties))
      .map((feature) => ({
        layer,
        properties: feature.properties,
        outsideActiveTime: !isFeatureAvailableAtTime(layer, feature.properties.year, year),
      }))), [matchesReportRecord, reportLayerIds, reportScope, year]);
  const reportActiveTimeRecordCount = useMemo(
    () => reportRecords.filter((record) => !record.outsideActiveTime).length,
    [reportRecords],
  );
  const reportRetainedSelectionCount = reportRecords.length - reportActiveTimeRecordCount;
  const reportRecordLimit = reportDetail === "EXECUTIVE" ? 8 : reportDetail === "STANDARD" ? 30 : reportRecords.length;
  const reportIncludedRecordCount = Math.min(reportRecords.length, reportRecordLimit);
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
  const reportTemporalComparison = useMemo(
    () => buildTemporalComparison(
      LAYER_REGISTRY.filter((layer) => reportLayerIds.includes(layer.id)),
      compareTimeA,
      compareTimeB,
      (layer, feature) => matchesReportRecord(layer, feature.properties),
    ),
    [compareTimeA, compareTimeB, matchesReportRecord, reportLayerIds],
  );
  const reportFindings = useMemo(() => {
    const supported = (reportEvidenceCounts.ANSWER ?? 0) + (reportEvidenceCounts.CORRECTED ?? 0);
    const bounded = reportRecords.length - supported;
    const mostRepresented = [...reportLayerSummary].sort((left, right) => right.recordCount - left.recordCount)[0];
    return [
      `${reportActiveTimeRecordCount} record${reportActiveTimeRecordCount === 1 ? "" : "s"} match the ${reportScope === "VIEWPORT" ? "current map extent" : reportScope === "ANALYSIS_AREA" ? "locked area-of-interest" : reportScope === "VISIBLE_LAYERS" ? "visible-layer" : "selected-feature"} scope at ${formatTimelineStep(year)}.${reportRetainedSelectionCount ? ` ${reportRetainedSelectionCount} selected record${reportRetainedSelectionCount === 1 ? " is" : "s are"} retained for inspection outside the active time and excluded from the active-time match count.` : ""}`,
      `${supported} record${supported === 1 ? "" : "s"} carry supported or corrected evidence states; ${bounded} remain generalized, missing, stale, restricted, denied, superseded, or error states.`,
      mostRepresented
        ? `${mostRepresented.title} contributes the largest share of this report (${mostRepresented.recordCount} record${mostRepresented.recordCount === 1 ? "" : "s"}).`
        : "No records match the current report filters; widen the map, change time, or include another layer.",
      `${reportTemporalComparison.changedLayerCount} included layer${reportTemporalComparison.changedLayerCount === 1 ? "" : "s"} change catalog availability between Time A ${formatTimelineStep(compareTimeA)} and Time B ${formatTimelineStep(compareTimeB)}; this is not an observed-change or imagery claim.`,
    ];
  }, [compareTimeA, compareTimeB, reportActiveTimeRecordCount, reportEvidenceCounts, reportLayerSummary, reportRecords.length, reportRetainedSelectionCount, reportScope, reportTemporalComparison.changedLayerCount, year]);
  const filteredLayerIds = useMemo(() => {
    const query = debouncedLayerQuery.trim().toLowerCase();
    return new Set(LAYER_REGISTRY.filter((layer) => {
      const matchesDomain = layerDomain === "ALL" || layer.domain === layerDomain;
      const matchesQuery = !query || `${layer.title} ${layer.description} ${layer.category} ${layer.datasetName} ${layer.domain}`.toLowerCase().includes(query);
      return matchesDomain && matchesQuery;
    }).map((layer) => layer.id));
  }, [debouncedLayerQuery, layerDomain]);
  const searchResults = useMemo(() => {
    const query = debouncedGlobalQuery.trim().toLowerCase();
    if (!query) return [];
    return SEARCH_INDEX.filter((item) => `${item.title} ${item.subtitle}`.toLowerCase().includes(query)).slice(0, 7);
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
      const matchesQuery = !query || `${source.title} ${source.organization} ${source.domain} ${source.sourceRole} ${source.value} ${source.nextGate}`.toLowerCase().includes(query);
      return matchesDomain && matchesQuery;
    });
  }, [sourceDomain, sourceQuery]);
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
  const selectedLayerHidden = Boolean(selected && !visibility[selected.layerId]);
  const selectedTimeMismatch = Boolean(selected && isFeatureTimeMismatch(selected.layer.temporal, selected.properties.year, year));
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
    activeYear: year,
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
    selection: selected ? {
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
      layerReleaseState: selected.layer.releaseState,
      correctionState: selected.properties.correctionState,
      geometry: selected.geometry.geometry,
      generalization: selected.properties.generalizationNote,
    } : null,
  }), [activeLayers, basemap, currentWorkspace, layerOrder, locationCameraRedacted, opacity, projection, selected, view, year]);
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
    params.set("t", String(year));
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
    if (mapUtilityView === "compare") {
      params.set("compare", `${compareLeft.id},${compareRight.id}`);
    }
    params.set("times", `${compareTimeA},${compareTimeB}`);
    if (selected) {
      params.set("f", selected.featureId);
      params.set("panel", drawerView);
      params.set("drawer", rightOpen ? "open" : "closed");
      params.set("focusStage", focusStage);
      params.set("focusIntent", focusIntent);
    }
    return params;
  }, [activeLayers, analysisArea, atmospherePreset, basemap, compareLeft.id, compareRight.id, compareTimeA, compareTimeB, currentWorkspace, drawerView, fieldOfView, focusIntent, focusStage, gestureMode, layerOrder, lightAzimuth, locationCameraRedacted, mapUtilityOpen, mapUtilityView, measureUnit, opacity, projection, rightOpen, scenePreset, selected, verticalExaggeration, view, year]);

  const announce = useCallback((message: string) => {
    setToast(message);
    window.setTimeout(() => setToast(""), 3600);
  }, []);

  const applyRendererNeutralView = useCallback((nextView: ViewState) => {
    const camera: MapRuntimeCamera = {
      longitude: nextView.center[0],
      latitude: nextView.center[1],
      zoom: nextView.zoom,
      bearing: nextView.bearing,
      pitch: nextView.pitch,
    };
    try {
      mapRuntimeRef.current?.setCamera(camera);
    } catch {
      // The serializable view remains usable even if the null port is not ready yet.
    }
    setView((current) => {
      lastKnownGoodViewRef.current = current;
      return nextView;
    });
    setPointer([...nextView.center] as [number, number]);
  }, []);

  const updateRendererNeutralView = useCallback((update: Partial<Omit<ViewState, "center">> & { center?: [number, number] }) => {
    setView((current) => {
      const nextView: ViewState = {
        center: update.center ?? current.center,
        zoom: update.zoom ?? current.zoom,
        bearing: update.bearing ?? current.bearing,
        pitch: update.pitch ?? current.pitch,
      };
      const camera: MapRuntimeCamera = {
        longitude: nextView.center[0],
        latitude: nextView.center[1],
        zoom: nextView.zoom,
        bearing: nextView.bearing,
        pitch: nextView.pitch,
      };
      try {
        mapRuntimeRef.current?.setCamera(camera);
      } catch {
        // URL and catalog state remain deterministic while runtime setup is pending.
      }
      lastKnownGoodViewRef.current = current;
      setPointer([...nextView.center] as [number, number]);
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
      return nextView;
    });
  }, []);

  const stopSceneOrbit = useCallback((notify = true) => {
    if (sceneOrbitTimerRef.current !== null) {
      window.clearTimeout(sceneOrbitTimerRef.current);
      sceneOrbitTimerRef.current = null;
    }
    setSceneOrbiting(false);
    if (notify) announce("Renderer-neutral camera turn stopped at the current view");
  }, [announce]);

  const fitRendererNeutralBounds = useCallback((bounds: [number, number, number, number], maxZoom = 9) => {
    const [west, south, east, north] = bounds;
    const span = Math.max(east - west, north - south, 0.01);
    const zoom = Math.min(maxZoom, Math.max(4, Math.log2(360 / span) - 1));
    setMapViewportBounds({ west, south, east, north });
    updateRendererNeutralView({ center: [(west + east) / 2, (south + north) / 2], zoom });
  }, [updateRendererNeutralView]);

  const showComparedLayers = useCallback(() => {
    setVisibility((current) => ({ ...current, [compareLeft.id]: true, [compareRight.id]: true }));
    announce(`Showing ${compareLeft.title} and ${compareRight.title}; other visible layers were preserved`);
  }, [announce, compareLeft, compareRight, setVisibility]);

  const fitComparedLayers = useCallback(() => {
    const bounds: [number, number, number, number] = [
      Math.min(compareLeft.bounds[0], compareRight.bounds[0]),
      Math.min(compareLeft.bounds[1], compareRight.bounds[1]),
      Math.max(compareLeft.bounds[2], compareRight.bounds[2]),
      Math.max(compareLeft.bounds[3], compareRight.bounds[3]),
    ];
    setVisibility((current) => ({ ...current, [compareLeft.id]: true, [compareRight.id]: true }));
    fitRendererNeutralBounds(bounds);
    announce("Framed both comparison layers in renderer-neutral camera state; visibility changed only in this browser");
  }, [announce, compareLeft, compareRight, fitRendererNeutralBounds, setVisibility]);

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
    yearRef.current = nextYear;
    setYear(nextYear);
    setPlaying(false);
    announce(`Applied Time ${label} · ${formatTimelineStep(nextYear)} to the active map`);
  }, [announce]);

  const copyTemporalComparison = useCallback(async () => {
    try {
      await navigator.clipboard.writeText(JSON.stringify({
        ...temporalComparison,
        generatedAt: new Date().toISOString(),
        visibleLayerIds: activeLayers.map((layer) => layer.id),
        effects: { evidence: "NONE", policy: "NONE", review: "NONE", release: "NONE", publication: "NONE" },
      }, null, 2));
      announce(`Time A / Time B comparison copied for ${activeLayers.length} visible layers`);
    } catch {
      announce("Clipboard access was blocked; temporal comparison stayed in the browser");
    }
  }, [activeLayers, announce, temporalComparison]);

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
   …41731 tokens truncated…ctive time {formatTimelineStep(year)} · untimed, exact, and through-time semantics applied</small></div>
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
                <div className="map-utility-section-heading"><span>SCENE + 3D LAB</span><h3>Globe, extrusion, atmosphere + camera intent</h3><p>Compose reversible renderer-neutral scene state for globe projection, fill-extrusion descriptors, atmosphere, light, field of view, and camera turns. MapLibre execution, real terrain, and operational sources stay held.</p></div>

                <section className="scene-preset-grid" aria-label="Map scene presets">
                  {([
                    ["overview-2d", "2D overview", "Default evidence-first camera"],
                    ["globe-overview", "Globe overview", "Projection + atmosphere"],
                    ["water-systems", "Water systems", "Basins + directional corridors"],
                    ["smoke-context", "Smoke timeline", "Synthetic plume context"],
                    ["elevation-3d", "Elevation 3D", "Relative-height extrusions"],
                    ["tile-grid", "Tile grid", "Viewport diagnostics"],
                  ] as const).map(([id, title, detail]) => <button key={id} type="button" aria-pressed={scenePreset === id} onClick={() => applyScenePreset(id)}><span>{id === "elevation-3d" ? "3D" : id === "globe-overview" ? "◎" : id === "tile-grid" ? "XYZ" : id === "smoke-context" ? "AIR" : id === "water-systems" ? "H₂O" : "2D"}</span><strong>{title}</strong><small>{detail}</small></button>)}
                </section>

                <div className="scene-layer-toggles" role="group" aria-label="Advanced layer visibility">
                  {([
                    ["watershed-context", "Watersheds"],
                    ["smoke-context", "Smoke"],
                    ["elevation-concept", "Elevation"],
                    ["tile-matrix-grid", "Tile matrix"],
                  ] as const).map(([id, label]) => <button key={id} type="button" aria-pressed={visibility[id]} onClick={() => toggleSceneLayer(id)}><i aria-hidden="true" />{label}</button>)}
                </div>

                <div className="scene-control-grid">
                  <section className="scene-height-control" aria-labelledby="scene-height-title">
                    <header><div><strong id="scene-height-title">Relative vertical scale</strong><small>Synthetic extrusion only</small></div><output htmlFor="scene-height">{verticalExaggeration.toFixed(1)}×</output></header>
                    <input id="scene-height" type="range" min="0" max="2" step="0.1" value={verticalExaggeration} onChange={(event) => { const next = Number(event.target.value); verticalExaggerationRef.current = next; setVerticalExaggeration(next); }} />
                    <div><span>Flat</span><span>1× fixture</span><span>2× concept</span></div>
                  </section>
                  <section className="scene-camera-controls" aria-label="3D camera orientation">
                    <header><strong>Camera</strong><small>{Math.round(view.pitch)}° pitch · {Math.round(view.bearing)}° bearing</small></header>
                    <div><button type="button" onClick={() => orientSceneCamera(48, -18)}>Oblique NW</button><button type="button" onClick={() => orientSceneCamera(54, 28)}>Oblique SE</button><button type="button" onClick={() => orientSceneCamera(0, view.bearing)}>Top down</button><button type="button" onClick={() => orientSceneCamera(view.pitch, 0)}>North up</button><button type="button" onClick={() => sceneOrbiting ? stopSceneOrbit() : startSceneOrbit()} aria-pressed={sceneOrbiting}>{sceneOrbiting ? "Stop turn" : "Turn 90°"}</button><button type="button" disabled={!selected} onClick={() => selected && updateRendererNeutralView({ center: [selected.properties.focusLng, selected.properties.focusLat], zoom: Math.max(view.zoom, 8.5), pitch: 58, bearing: -24 })}>Focus selection</button></div>
                  </section>
                </div>

                <div className="scene-environment-grid">
                  <section className="scene-atmosphere-control" aria-labelledby="scene-atmosphere-title">
                    <header><div><strong id="scene-atmosphere-title">Sky + atmosphere</strong><small>Inert style-environment descriptor</small></div><output>{atmospherePreset.toUpperCase()}</output></header>
                    <div>{(["night", "dusk", "clear"] as const).map((preset) => <button key={preset} type="button" aria-pressed={atmospherePreset === preset} onClick={() => { atmospherePresetRef.current = preset; setAtmospherePreset(preset); }}>{preset}</button>)}</div>
                  </section>
                  <section className="scene-optics-control" aria-labelledby="scene-optics-title">
                    <header><div><strong id="scene-optics-title">Light + optics</strong><small>Extrusion illumination and vertical FOV</small></div></header>
                    <label><span>Light azimuth <output>{Math.round(lightAzimuth)}°</output></span><input type="range" min="0" max="359" step="1" value={lightAzimuth} onChange={(event) => { const next = Number(event.target.value); lightAzimuthRef.current = next; setLightAzimuth(next); }} /></label>
                    <label><span>Field of view <output>{fieldOfView.toFixed(0)}°</output></span><input type="range" min="20" max="60" step="1" value={fieldOfView} onChange={(event) => { const next = Number(event.target.value); fieldOfViewRef.current = next; setFieldOfView(next); }} /></label>
                  </section>
                </div>

                <section className="scene-time-strip" aria-labelledby="scene-time-title">
                  <header><strong id="scene-time-title">Smoke context time</strong><small>Exact fixture years · not current conditions</small></header>
                  <div>{([2022, 2024, 2026] as const).map((step) => <button key={step} type="button" aria-pressed={year === step} onClick={() => { yearRef.current = step; setYear(step); setPlaying(false); }}>{step}</button>)}</div>
                </section>

                <section className="scene-tile-ledger" aria-labelledby="tile-ledger-title">
                  <header><div><span>VIEWPORT DIAGNOSTICS</span><h4 id="tile-ledger-title">Tile matrix reader</h4></div><strong>HELD</strong></header>
                  <div className="scene-metrics">
                    <article><span>CENTER XYZ</span><strong>{centerTile.label}</strong><small>Web Mercator address at floor zoom</small></article>
                    <article><span>SOURCES</span><strong>{sourceStateCounts.held} HELD</strong><small>Catalog metadata readable</small></article>
                    <article><span>RENDER MODE</span><strong>{projection.toUpperCase()}</strong><small>{Math.round(view.pitch)}° pitch · {atmospherePreset} sky</small></article>
                    <article><span>CARRIER</span><strong>LOCAL GEOJSON</strong><small>No PMTiles, MVT, COG, or DEM fetch</small></article>
                  </div>
                  <p>The optional grid is a labeled GeoJSON simulation for viewport, selection, and matrix-orientation testing. It is not proof of a tile request, cache hit, archive range response, or KFM source admission.</p>
                </section>

                <aside className="map-utility-boundary" data-tone="warning"><strong>3D preserves the 2D evidence path.</strong><p>The elevation scene extrudes invented relative-height bands; it does not sample a DEM or assert elevation. Smoke is not an advisory or exposure surface. Water is not flow, storage, quality, flood, or legal-water authority. Select any visible feature to inspect the same Evidence Drawer used in 2D.</p></aside>
              </section>}

              {mapUtilityView === "connections" && <section id="map-utility-view-connections" role="tabpanel" aria-labelledby="map-utility-tab-connections" className="map-utility-section source-connections-section">
                <div className="map-utility-section-heading"><span>SOURCE CONNECTIONS</span><h3>Registry → held renderer → records</h3><p>Inspect each site-local fixture carrier, fit its declared bounds, or route to its compatible record index while renderer acquisition remains held.</p></div>
                <div className="source-connection-summary" aria-label="Source connection summary">
                  <article><span>HELD</span><strong>{sourceStateCounts.held}/{LAYER_REGISTRY.length}</strong><small>Renderer sources not acquired</small></article>
                  <article><span>VISIBLE</span><strong>{visibleCount}</strong><small>Registry visibility intent</small></article>
                  <article><span>DESCRIPTORS</span><strong>{LAYER_REGISTRY.reduce((count, layer) => count + layer.renderers.length, 0)}</strong><small>Inert style-layer metadata</small></article>
                  <article><span>INSPECTED</span><strong>{Object.keys(sourceProbeCounts).length}</strong><small>Site-local fixture queries</small></article>
                </div>
                <div className="source-connection-toolbar">
                  <label><i aria-hidden="true">⌕</i><span className="sr-only">Search source connections</span><input type="search" value={connectionQuery} onChange={(event) => setConnectionQuery(event.target.value)} placeholder="Layer, source ID, domain, or format" /></label>
                  <label><span className="sr-only">Filter source connections</span><select value={connectionFilter} onChange={(event) => setConnectionFilter(event.target.value as typeof connectionFilter)}><option value="ALL">All carriers</option><option value="VISIBLE">Visible intent only</option><option value="HELD">Renderer held</option></select></label>
                </div>
                <div className="source-connection-list">
                  {filteredSourceConnections.map(({ layer, state, activity, visible, compatibleCount, viewportCount, probeCount }) => <article key={layer.id} className="source-connection-card" data-state={state} data-visible={visible}>
                    <header><div><span>{layer.domain} · {layer.sourceType}</span><h4>{layer.title}</h4><code>{layer.sourceId}</code></div><strong>{state.toUpperCase()}</strong></header>
                    <div className="source-connection-path" aria-label={`${layer.title} renderer connection`}><span>REGISTRY</span><i>→</i><span>{activity}</span><i>→</i><span>{layer.renderers.length} DESCRIPTOR{layer.renderers.length === 1 ? "" : "S"}</span><i>→</i><span>RUNTIME HELD</span></div>
                    <dl><div><dt>Time-compatible</dt><dd>{compatibleCount}</dd></div><div><dt>In viewport</dt><dd>{viewportCount}</dd></div><div><dt>Source probe</dt><dd>{probeCount === undefined ? "NOT RUN" : `${probeCount} UNIQUE`}</dd></div><div><dt>Attribution</dt><dd>{layer.attribution}</dd></div></dl>
                    <footer><button type="button" onClick={() => setVisibility((current) => { const next = { ...current, [layer.id]: !current[layer.id] }; return next; })}>{visible ? "Hide intent" : "Show intent"}</button><button type="button" onClick={() => zoomToLayer(layer)}>Fit</button><button type="button" onClick={() => probeSourceConnection(layer)}>Inspect fixture</button><button type="button" onClick={() => inspectSourceConnection(layer)}>Records</button></footer>
                  </article>)}
                  {filteredSourceConnections.length === 0 && <div className="map-utility-empty"><strong>No source connections match</strong><p>Clear the search or choose another connection state.</p></div>}
                </div>
                <aside className="map-utility-boundary" data-tone="warning"><strong>Connection status is held renderer context, not source admission.</strong><p>These carriers expose only site-local fixtures already in the Explorer registry. A fixture inspection does not acquire MapLibre or prove rights, freshness, evidence, policy approval, release, deployment, or publication.</p></aside>
              </section>}

              {mapUtilityView === "import" && <section id="map-utility-view-import" role="tabpanel" aria-labelledby="map-utility-tab-import" className="map-utility-section import-preview-section">
                <div className="map-utility-section-heading"><span>LOCAL IMPORT PREVIEW</span><h3>Inspect before any admission handoff</h3><p>Open a small KML or GeoJSON file in this browser. Supported geometry, extent, temporal fields, attribution gaps, and sensitivity signals remain explicit while renderer acquisition stays held.</p></div>
                <div className="import-path-grid" aria-label="Import preview boundary">
                  <article><span>01</span><strong>Parse locally</strong><small>No upload, network link, or external asset fetch.</small></article>
                  <article><span>02</span><strong>Inspect structure</strong><small>Geometry and bounds remain browser-local context.</small></article>
                  <article><span>03</span><strong>Stop at review</strong><small>No catalog, report-data, evidence, or publication effect.</small></article>
                </div>
                <label className="import-dropzone" data-busy={importBusy} onDragOver={(event) => { event.preventDefault(); event.dataTransfer.dropEffect = "copy"; }} onDrop={(event) => { event.preventDefault(); void inspectImportFile(event.dataTransfer.files[0]); }}>
                  <input ref={importInputRef} type="file" accept=".kml,.geojson,.json,application/geo+json,application/vnd.google-earth.kml+xml" onChange={(event) => void inspectImportFile(event.target.files?.[0])} />
                  <span aria-hidden="true">⇧</span><strong>{importBusy ? "Inspecting file…" : "Choose or drop KML / GeoJSON"}</strong><small>Maximum 2 MB · browser memory only · raw file is never stored</small>
                </label>
                 <WaveformPreviewPanel />
                {importError && <div className="import-error" role="alert"><strong>Preview blocked</strong><p>{importError}</p></div>}
                {!importPreview && !importError && <div className="map-utility-empty import-empty"><strong>No local file inspected</strong><p>This is a structure-review surface, not a source-ingestion or upload workflow.</p></div>}
                {importPreview && <>
                  <div className="import-preview-summary" aria-label="Local import preview summary">
                    <article><span>FORMAT</span><strong>{importPreview.sourceFormat}</strong><small>{(importPreview.fileSizeBytes / 1024).toFixed(1)} KB</small></article>
                    <article><span>FEATURES</span><strong>{importPreview.featureCount}</strong><small>{importPreview.invalidFeatureCount} invalid</small></article>
                    <article><span>GEOMETRIES</span><strong>{Object.values(importPreview.geometryCounts).reduce((sum, count) => sum + count, 0)}</strong><small>{Object.keys(importPreview.geometryCounts).length} types</small></article>
                    <article data-state={importPreview.renderAllowed ? "PASS" : "BLOCK"}><span>BOUNDS CONTEXT</span><strong>{importPreview.renderAllowed ? "AVAILABLE" : "BLOCKED"}</strong><small>{importPreview.coverage.replaceAll("_", " ").toLowerCase()}</small></article>
                  </div>
                  <article className="import-file-card"><header><div><span>INSPECTED FILE</span><h4>{importPreview.fileName}</h4></div><strong>{importPreview.authority}</strong></header><dl>
                    <div><dt>Bounds</dt><dd>{importPreview.bounds ? "WITHHELD · browser-local geometry" : "NO GEOMETRY"}</dd></div>
                    <div><dt>Attribution</dt><dd>{importPreview.attribution ?? "NOT FOUND"}</dd></div>
                    <div><dt>Temporal fields</dt><dd>{importPreview.temporalFields.join(", ") || "NONE DETECTED"}</dd></div>
                    <div><dt>Potential sensitivity keys</dt><dd>{importPreview.sensitivitySignals.join(", ") || "NONE DETECTED"}</dd></div>
                  </dl></article>
                  {importPreview.renderAllowed && <div className="import-preview-notice" role="status"><strong>Bounds inspection available</strong><p>No geometry overlay is rendered. Exact bounds remain in browser memory; fitted camera state is privacy-marked and redacted from shares, saved workspace coordinates, receipts, reports, exports, and diagnostics.</p></div>}
                  <div className="import-geometry-grid">{Object.entries(importPreview.geometryCounts).map(([geometry, count]) => <article key={geometry}><span>{geometry}</span><strong>{count}</strong></article>)}</div>
                  <div className="import-check-list" aria-label="Import inspection checks">{importPreview.checks.map((check) => <article key={check.id} data-state={check.state}><span>{check.label}</span><p>{check.detail}</p><strong>{check.state}</strong></article>)}</div>
                  <div className="map-utility-actions import-preview-actions"><button type="button" disabled={!importPreview.renderAllowed} onClick={() => fitImportPreview()}>Fit bounds</button><button type="button" onClick={() => void copyImportPreviewAudit()}>Copy inspection</button><button type="button" onClick={clearImportPreview}>Clear</button></div>
                </>}
                <aside className="map-utility-boundary" data-tone="warning"><strong>Temporary Places, KFM-style: inspectable but unadmitted.</strong><p>Exact file geometry and bounds never enter the Layer Catalog, Evidence Drawer, saved workspaces, reports, exports, registry, repository, or renderer. A fitted camera is privacy-marked and generalized at those boundaries. URL references, KML network links, overlays, models, tracks, and external resources are counted or warned about and never fetched.</p></aside>
              </section>}

              {mapUtilityView === "compare" && <section id="map-utility-view-compare" role="tabpanel" aria-labelledby="map-utility-tab-compare" className="map-utility-section layer-compare-section">
                <div className="map-utility-section-heading"><span>COMPARE</span><h3>Time + layer investigation</h3><p>Compare two times across the visible catalog, then inspect two layers without flattening time, source role, release posture, or sensitivity.</p></div>
                <section className="temporal-compare-lab" aria-labelledby="temporal-compare-title">
                  <header><div><span>TIME A / TIME B</span><h4 id="temporal-compare-title">Catalog availability comparison</h4></div><strong>CONTEXT ONLY</strong></header>
                  <div className="temporal-compare-selectors">
                    <label><span>Time A</span><select value={compareTimeA} onChange={(event) => setCompareTimeA(Number(event.target.value))}>{TIME_STEPS.map((step) => <option key={`time-a-${step}`} value={step}>{formatTimelineStep(step)}</option>)}</select></label>
                    <button type="button" onClick={() => { setCompareTimeA(compareTimeB); setCompareTimeB(compareTimeA); }} aria-label="Swap comparison times">⇄<span>Swap</span></button>
                    <label><span>Time B</span><select value={compareTimeB} onChange={(event) => setCompareTimeB(Number(event.target.value))}>{TIME_STEPS.map((step) => <option key={`time-b-${step}`} value={step}>{formatTimelineStep(step)}</option>)}</select></label>
                  </div>
                  <div className="temporal-compare-metrics" aria-label="Temporal comparison summary">
                    <article><span>TIME A RECORDS</span><strong>{temporalComparison.timeARecordCount}</strong><small>{temporalComparison.timeALayerCount} visible layers represented</small></article>
                    <article><span>TIME B RECORDS</span><strong>{temporalComparison.timeBRecordCount}</strong><small>{temporalComparison.timeBLayerCount} visible layers represented</small></article>
                    <article><span>CATALOG DELTA</span><strong>{temporalComparison.recordDelta > 0 ? "+" : ""}{temporalComparison.recordDelta}</strong><small>Record availability only</small></article>
                    <article><span>CHANGED LAYERS</span><strong>{temporalComparison.changedLayerCount}</strong><small>Entered or exited fixture IDs</small></article>
                  </div>
                  <div className="temporal-compare-table" role="table" aria-label={`Visible-layer availability at ${formatTimelineStep(compareTimeA)} and ${formatTimelineStep(compareTimeB)}`}>
                    <header role="row"><span role="columnheader">Visible layer</span><span role="columnheader">Time A</span><span role="columnheader">Time B</span><span role="columnheader">Delta</span></header>
                    {temporalComparisonRows.map((row) => <article key={row.layerId} role="row"><div role="cell"><strong>{row.title}</strong><small>{row.domain} · {row.temporalMode}</small></div><span role="cell">{row.timeARecordCount}</span><span role="cell">{row.timeBRecordCount}</span><span role="cell" data-delta={row.timeBRecordCount - row.timeARecordCount}>{row.timeBRecordCount - row.timeARecordCount > 0 ? "+" : ""}{row.timeBRecordCount - row.timeARecordCount}<small>{row.enteredRecordIds.length} in · {row.exitedRecordIds.length} out</small></span></article>)}
                    {temporalComparisonRows.length === 0 && <div className="map-utility-empty"><strong>No visible records at either time</strong><p>Show another layer or choose different comparison times.</p></div>}
                  </div>
                  <div className="temporal-compare-actions"><button type="button" onClick={() => applyComparisonTime(compareTimeA, "A")}>Apply Time A</button><button type="button" onClick={() => applyComparisonTime(compareTimeB, "B")}>Apply Time B</button><button type="button" onClick={() => void copyTemporalComparison()}>Copy comparison</button></div>
                  <aside><strong>Not historical imagery or observed change</strong><p>The table reports fixture availability under each layer&apos;s declared temporal rule. Untimed context, entered IDs, exited IDs, and count deltas are not evidence that the world changed.</p></aside>
                </section>
                <div className="compare-section-divider"><span>LAYER A / LAYER B</span><p>Inspect metadata, release posture, and sensitivity for two catalog layers.</p></div>
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
                <div className="map-control-group"><header><strong>Projection</strong><span>Preference descriptor only</span></header><div className="map-choice-grid"><button type="button" aria-pressed={projection === "mercator"} onClick={() => setProjection("mercator")}><strong>Mercator</strong><small>Stored 2D preference</small></button><button type="button" aria-pressed={projection === "globe"} onClick={() => setProjection("globe")}><strong>Globe</strong><small>Stored globe preference · renderer held</small></button></div></div>
                <div className="map-control-group"><header><strong>View profiles</strong><span>View state only · reversible</span></header><div className="map-profile-list">{MAP_VIEW_PROFILES.map((profile) => <article key={profile.id}><div><strong>{profile.title}</strong><p>{profile.summary}</p><small>{profile.year} · {profile.basemap} · {profile.visibleLayerIds.length} layers</small></div><button type="button" onClick={() => applyViewProfile(profile)}>Apply profile</button></article>)}</div></div>
                <button className="map-catalog-launch" type="button" onClick={openLayerCatalogFromUtility}>Open full Layer Catalog for visibility, opacity, order, legends, time, and trust metadata</button>
              </section>}

              {mapUtilityView === "measure" && <section id="map-utility-view-measure" role="tabpanel" aria-labelledby="map-utility-tab-measure" className="map-utility-section">
                <div className="map-utility-section-heading"><span>MEASURE</span><h3>Browser-local screen measurement</h3><p>Choose a geometry, then click the map to add points. Undo resumes a completed measurement for explicit editing.</p></div>
                <div className="map-control-group"><header><strong>Geometry</strong><span>RENDERER HOLD</span></header><div className="map-choice-grid"><button type="button" aria-pressed={false} onClick={() => toggleMeasure("distance")}><strong>Distance</strong><small>Requires conforming renderer interaction</small></button><button type="button" aria-pressed={false} onClick={() => toggleMeasure("area")}><strong>Area</strong><small>Requires conforming renderer interaction</small></button></div></div>
                <div className="map-control-group"><header><strong>Units</strong><span>Stored preference only</span></header><div className="map-segmented-control"><button type="button" aria-pressed={measureUnit === "imperial"} onClick={() => changeMeasureUnit("imperial")}>Miles / sq mi</button><button type="button" aria-pressed={measureUnit === "metric"} onClick={() => changeMeasureUnit("metric")}>Kilometers / km²</button></div></div>
                <article className="map-measure-status" aria-live="polite"><span>NO MEASUREMENT</span><strong>{measurement}</strong><small>Distance and area measurement remain held until renderer interactions cross MapRuntimePort.</small></article>
                <div className="map-utility-actions"><button type="button" onClick={undoMeasurementPoint} disabled={!measurementGeometryMode}>Undo point</button><button type="button" onClick={finishMeasurement} disabled={!measureMode}>Finish</button><button type="button" onClick={clearMeasurement} disabled={!measurementGeometryMode}>Clear</button></div>
                <aside className="map-utility-boundary" data-tone="warning"><strong>Screen measurement — not survey, cadastral, legal, or evidence.</strong><p>Results are approximate, browser-local, and excluded from context receipts and public-safe exports.</p></aside>
              </section>}

              {mapUtilityView === "export" && <section id="map-utility-view-export" role="tabpanel" aria-labelledby="map-utility-tab-export" className="map-utility-section export-review-section">
                <div className="map-utility-section-heading"><span>EXPORT REVIEW</span><h3>Preview trust before download</h3><p>The outward artifact carries workspace, map context, separate temporal fields, visible layers, attribution, evidence posture, release/correction state, and redaction results.</p></div>
                <div className="export-review-summary" aria-label="Export review summary">
                  <article><span>FORMAT</span><strong>PUBLIC SAFE V2</strong><small>Site-local demonstration</small></article>
                  <article><span>LAYERS</span><strong>{activeLayers.length}</strong><small>Each keeps attribution</small></article>
                  <article><span>SELECTION</span><strong>{selected ? "1" : "0"}</strong><small>{selected?.properties.evidenceState ?? "MAP CONTEXT ONLY"}</small></article>
                  <article data-state={exportReview.withheldFeatureCount ? "REDACTED" : "PASS"}><span>WITHHELD</span><strong>{exportReview.withheldFeatureCount}</strong><small>Protected geometry count</small></article>
                </div>
                <div className="export-preflight" aria-label="Export preflight checks">
                  {exportReview.checks.map((check) => <article key={check.id} data-state={check.state}><span>{check.label}</span><p>{check.detail}</p><strong>{check.state}</strong></article>)}
                </div>
                <div className="map-control-group temporal-axis-inspector"><header><strong>Temporal-axis inspector</strong><span>Axes stay separate</span></header><dl>
                  <div><dt>Active map time</dt><dd>{formatTimelineStep(year)}</dd></div>
                  <div><dt>Feature / source year</dt><dd>{selected?.properties.year ?? "NO SELECTION"}</dd></div>
                  <div><dt>Temporal query mode</dt><dd>{selected?.layer.temporal?.mode ?? "layer-specific / untimed"}</dd></div>
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
                  <article><span>STYLE</span><strong>HELD</strong><small>{BASEMAPS[basemap].title} descriptor · {projection}</small></article>
                  <article><span>SOURCES</span><strong>{sourceStateCounts.held} HELD</strong><small>Catalog metadata remains readable</small></article>
                </div>
                <section className="map-control-group maplibre-runtime-proof" aria-labelledby="maplibre-runtime-proof-title">
                  <header><strong id="maplibre-runtime-proof-title">MapLibre {EXPECTED_MAPLIBRE_VERSION} acquisition boundary</strong><span>Runtime probes held</span></header>
                  <div className="map-status-list" aria-label="MapLibre browser capability status">{maplibreCapabilityChecks.map((check) => <article className="map-status-row" key={check.id} data-state={check.state}><div><span>{check.label}</span><p>{check.detail}</p></div><strong>{check.state}</strong></article>)}</div>
                </section>
                <section className="runtime-seam-lab" aria-labelledby="runtime-seam-title">
                  <header><div><span>REPOSITORY-PROVEN PORT · SITE-LOCAL REPLAY</span><h4 id="runtime-seam-title">Renderer-neutral runtime seam</h4><p>Replay initialize → validated selection binding → dispose through the repository package without acquiring MapLibre or a network source.</p></div><strong data-state={runtimeSeamState}>{runtimeSeamState}</strong></header>
                  <div className="runtime-seam-state"><span>Reason / effect</span><p>{runtimeSeamReason}</p><small>Current selection: {selected ? `${selected.featureId} · ${selected.properties.evidenceState}` : "NONE"}</small></div>
                  <div className="map-utility-actions"><button type="button" onClick={initializeRuntimeSeam}>Initialize Null seam</button><button type="button" onClick={bindRuntimeSeamSelection} disabled={runtimeSeamState === "IDLE" || runtimeSeamState === "DISPOSED"}>Bind current selection</button><button type="button" onClick={disposeRuntimeSeam} disabled={runtimeSeamState === "IDLE" || runtimeSeamState === "DISPOSED"}>Dispose</button><button type="button" onClick={() => { setRuntimeSeamState("IDLE"); setRuntimeSeamReason("Awaiting deterministic replay"); }}>Reset replay</button></div>
                  <footer>VERIFIED REPOSITORY SLICE: MapRuntimePort + NullMapRuntime + governed evidence binding · CONCRETE MAPLIBRE ADAPTER: HOLD</footer>
                </section>
                <div className="map-status-list" aria-label="MapLibre repository status">{MAPLIBRE_REPOSITORY_STATUS.map((status) => <article className="map-status-row" key={status.id} data-state={status.state}><div><span>{status.label}</span><p>{status.detail}</p></div><strong>{status.state}</strong></article>)}</div>
                <div className="map-utility-actions"><button type="button" onClick={reapplyRendererState}>Reapply local state</button><button type="button" onClick={restoreLastKnownGoodView}>Restore prior camera</button><button type="button" onClick={() => void copyMapDiagnostics()}>Copy redacted diagnostics</button></div>
                <div className="map-control-group"><header><strong>Capability gates</strong><span>Honest interfaces for unavailable work</span></header><div className="map-capability-grid">{MAP_CAPABILITY_GATES.map((gate) => <article className="map-capability-card" key={gate.id}><header><strong>{gate.title}</strong><span>{gate.state}</span></header><p>{gate.reason}</p><small>{gate.safeInterface}</small></article>)}</div></div>
                <aside className="map-utility-boundary"><strong>Renderer evidence boundary</strong><p>This Site runs the package-owned NullMapRuntime and does not acquire MapLibre. GitHub proves the exact package dependency, bounded adapter, renderer-neutral port, and deterministic Null runtime; full consumer migration and all renderer runtime probes remain held.</p></aside>
              </section>}
            </div>
          </aside>

          {measurementGeometryMode && <div className="measurement-readout" role="region" aria-label="Active screen measurement"><span>{measurementGeometryMode.toUpperCase()} · {measureMode ? "ACTIVE" : "COMPLETE"}</span><strong aria-live="polite">{measurement}</strong><div><button type="button" onClick={undoMeasurementPoint}>Undo</button><button type="button" onClick={finishMeasurement} disabled={!measureMode}>Finish</button><button type="button" onClick={clearMeasurement}>Clear</button></div></div>}

          <div className="map-mobile-actions">
            <button type="button" onClick={() => { setCurrentWorkspace("knowledge"); dismissMapUtilityWithoutFocus(); setLeftOpen(true); setRightOpen(false); setTimelineOpen(false); }}>Layers <b>{visibleCount}</b></button>
            <button type="button" onClick={() => { if (selected) { setCurrentWorkspace("trust"); dismissMapUtilityWithoutFocus(); setRightOpen(true); setLeftOpen(false); setTimelineOpen(false); } }} disabled={!selected}>Evidence</button>
            <button type="button" onClick={(event) => openMapUtility("report", event.currentTarget)}>Report</button>
            <button type="button" onClick={() => { setCurrentWorkspace("explore"); dismissMapUtilityWithoutFocus(); setTimelineOpen(true); setLeftOpen(false); setRightOpen(false); }}>Time <b>{formatTimelineStep(year)}</b></button>
            <a href="/about">About</a>
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
            {selectedTimeMismatch && <div className="drawer-time-warning" role="status"><strong>Selection is outside active time</strong><span>Source {formatTimelineStep(selected.properties.year)} · active {formatTimelineStep(year)}. The normal map halo is hidden while the record stays available for inspection.</span></div>}
            {selectedLayerHidden && <div className="drawer-time-warning" role="status"><strong>Selected layer is hidden</strong><span>{selected.layer.title} remains available for inspection, but its normal map halo is hidden until the layer is visible again.</span></div>}
            <div className="drawer-tabs" role="tablist" aria-label="Evidence Drawer views">
              {drawerViews.map((tab, index) => <button key={tab} ref={(node) => { drawerTabRefs.current[index] = node; }} id={`drawer-tab-${tab}`} type="button" role="tab" aria-selected={drawerView === tab} aria-controls={`drawer-panel-${tab}`} tabIndex={drawerView === tab ? 0 : -1} onClick={() => activateDrawerView(tab)} onKeyDown={(event) => handleDrawerTabKeyDown(event, index)}>{tab}</button>)}
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
                </dl>
                <div className="notice"><strong>Limitations</strong><p>{selected.properties.uncertainty}</p></div>
                <div className="notice"><strong>Generalization / rights</strong><p>{selected.properties.generalizationNote} {selected.properties.rights}</p></div>
                {selected.properties.correctionState !== "NONE" && <div className="notice correction"><strong>Correction state</strong><p>{selected.properties.correctionState}</p></div>}
                <div className="drawer-actions"><button type="button" onClick={() => activateDrawerView("focus", true)}>Open Focus Mode</button><button type="button" onClick={(event) => openMapUtility("export", event.currentTarget)}>Review public-safe export</button></div>
              </section>}
              {drawerView === "metadata" && <section role="tabpanel" id="drawer-panel-metadata" aria-labelledby="drawer-tab-metadata" className="drawer-section">
                <h3>Registry-driven layer metadata</h3><dl className="evidence-facts">
                  <div><dt>Dataset</dt><dd>{selected.layer.datasetName}</dd></div><div><dt>Source / geometry</dt><dd>{selected.layer.sourceType} · {selected.layer.geometryType}</dd></div><div><dt>Zoom support</dt><dd>{selected.layer.minZoom}–{selected.layer.maxZoom}</dd></div><div><dt>Units</dt><dd>{selected.layer.units}</dd></div><div><dt>Valid time extent</dt><dd>{selected.layer.validTimeExtent}</dd></div><div><dt>Source time</dt><dd>{selected.layer.sourceTime}</dd></div><div><dt>Release time</dt><dd>{selected.layer.releaseTime}</dd></div><div><dt>Attribution</dt><dd>{selected.layer.attribution}</dd></div></dl>
                <div className="legend-detail"><strong>Legend</strong>{selected.layer.legend.map((item) => <p key={item.label}><i className={`legend-swatch ${item.shape}`} style={{ "--swatch": item.color } as React.CSSProperties} />{item.label}</p>)}</div>
              </section>}
              {drawerView === "lineage" && <section role="tabpanel" id="drawer-panel-lineage" aria-labelledby="drawer-tab-lineage" className="drawer-section">
                <h3>Selection-to-evidence trace</h3><ol className="lineage-list"><li><span>01</span><div><strong>Catalog selection</strong><small>Stable registry lookup selected a fixture; renderer hit testing remains held</small></div></li><li><span>02</span><div><strong>Stable registry context</strong><small>{selected.featureId}</small></div></li><li><span>03</span><div><strong>Evidence resolution</strong><small>{selected.properties.citation}</small></div></li><li><span>04</span><div><strong>Policy / rights</strong><small>{selected.properties.evidenceState}</small></div></li><li><span>05</span><div><strong>Public-safe view</strong><small>Drawer + bounded Focus Mode</small></div></li></ol>
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
                    <span>Active / source time <code>{formatTimelineStep(year)} / {formatTimelineStep(selected.properties.year)}</code></span>
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
            <button className="timeline-toggle" type="button" aria-expanded={timelineOpen} onClick={() => { if (timelineOpen) { closeTimelinePanel(); return; } setTimelineOpen(true); if (isCompact) { dismissMapUtilityWithoutFocus(); setLeftOpen(false); setRightOpen(false); } }}><span>TIME</span><strong>{formatTimelineStep(year)}</strong><small>{timelineEraLabel(year)}</small></button>
            <div className="timeline-controls"><button type="button" disabled={TIME_STEPS.indexOf(year as (typeof TIME_STEPS)[number]) === 0} onClick={() => setYear(TIME_STEPS[Math.max(0, TIME_STEPS.indexOf(year as (typeof TIME_STEPS)[number]) - 1)])} aria-label="Previous available time">‹</button><button type="button" aria-pressed={playing} onClick={() => setPlaying((current) => !current)} aria-label={playing ? "Pause timeline" : "Play timeline"}>{playing ? "Ⅱ" : "▶"}</button><button type="button" disabled={TIME_STEPS.indexOf(year as (typeof TIME_STEPS)[number]) === TIME_STEPS.length - 1} onClick={() => setYear(TIME_STEPS[Math.min(TIME_STEPS.length - 1, TIME_STEPS.indexOf(year as (typeof TIME_STEPS)[number]) + 1)])} aria-label="Next available time">›</button></div>
            <div className="timeline-track"><input type="range" min="0" max={TIME_STEPS.length - 1} value={TIME_STEPS.indexOf(year as (typeof TIME_STEPS)[number])} onChange={(event) => setYear(TIME_STEPS[Number(event.target.value)])} aria-label="Active demonstration time" aria-valuetext={formatTimelineStep(year)} /><div className="timeline-ticks" style={{ "--timeline-columns": TIME_STEPS.length } as React.CSSProperties}>{TIME_STEPS.map((step) => <button key={step} type="button" data-active={step === year} data-major={TIMELINE_MAJOR_STEPS.has(step)} onClick={() => setYear(step)} aria-label={`Set timeline to ${formatTimelineStep(step)}`} title={`${formatTimelineStep(step)} · ${timelineEraLabel(step)}`}>{TIMELINE_MAJOR_STEPS.has(step) ? <span>{formatTimelineStep(step)}</span> : <i aria-hidden="true" />}</button>)}</div></div>
            <button className="timeline-reset" type="button" onClick={() => { setYear(2026); setPlaying(false); }}>Reset</button>
          </div>
          {timelineOpen && <div className="timeline-detail"><div><span>FULL TEMPORAL CAPACITY · 4.54 GA BP TO 2026</span><strong>{timelineEraLabel(year)} · active {formatTimelineStep(year)}</strong><p>This non-linear axis spans Earth history, archaeological time, historical records, and modern observations. Deep-time and intermediate ticks are capacity markers, not claims that current fixtures contain data. Exact layers appear only at declared years; through-time layers begin at their earliest valid vintage; untimed context remains available.</p><div className="timeline-era-jumps" aria-label="Jump between major time ranges">{TIMELINE_JUMPS.map((jump) => <button key={jump.label} type="button" data-active={jump.year === year} onClick={() => { setYear(jump.year); setPlaying(false); }}>{jump.label}<small>{formatTimelineStep(jump.year)}</small></button>)}</div></div><div><span>ACTIVE LAYERS AVAILABLE</span><div className="availability-bars" aria-label="Available layer count by timeline step">{TIME_STEPS.map((step) => <i key={step} data-active={step === year} title={`${formatTimelineStep(step)} · ${availabilityByStep[step]} available layer${availabilityByStep[step] === 1 ? "" : "s"}`} style={{ height: `${Math.min(44, 14 + availabilityByStep[step] * 5)}px` }}><b>{availabilityByStep[step]}</b></i>)}</div></div><button className="icon-close timeline-close" type="button" onClick={closeTimelinePanel} aria-label="Close timeline">×</button></div>}
        </section>

        <footer className="status-bar" aria-label="Map status">
          <span data-runtime={runtime.kind}><i />{runtime.kind.toUpperCase()}</span><span>{formatCoordinate(pointer[1], "N", "S")} · {formatCoordinate(pointer[0], "E", "W")}</span><span>{scaleAtView(view)}</span><span>Zoom {view.zoom.toFixed(2)}</span><span>Bearing {Math.round(view.bearing)}° · Pitch {Math.round(view.pitch)}°</span><span>{formatTimelineStep(year)} active time</span><span>{visibleCount} catalog layers visible</span><span>Renderer HOLD · MapLibre candidate {EXPECTED_MAPLIBRE_VERSION}</span><span>Repo main@{REPOSITORY_SNAPSHOT.shortCommit}</span>
        </footer>
      </main>

      <div className="toast" role="status" aria-live="polite" data-visible={Boolean(toast)}>{toast}</div>
    </div>
  );
}
