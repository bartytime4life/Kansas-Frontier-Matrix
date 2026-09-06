"use client";

import { useCallback, useEffect, useMemo, useRef, useState, useSyncExternalStore } from "react";
import Link from "next/link";
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
        const stored = JSON.parse(window.localStorage.getItem(WORKSPACE_STORAGE_KEY) ?? "[]");
        if (Array.isArray(stored)) setSavedWorkspaces(stored.slice(0, 8));
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
  }, [announce, compareLeft, compareRight]);

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
  }, [announce, compareLeft, compareRight, fitRendererNeutralBounds]);

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
      setYear(proposal.targetYear);
      announce(`Applied view-only time change to ${formatTimelineStep(proposal.targetYear)}`);
      return;
    }
    if (proposal.kind === "CENTER_SELECTION") {
      updateRendererNeutralView({
        center: [selected.properties.focusLng, selected.properties.focusLat],
        zoom: Math.max(mapRuntimeRef.current?.getSnapshot().camera.zoom ?? KANSAS_VIEW.zoom, 7),
      });
      announce("Applied renderer-neutral camera-only Focus action");
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
  }, [activateDrawerView, announce, selected, updateRendererNeutralView]);

  const closeRepository = useCallback(() => {
    setRepositoryOpen(false);
    setCurrentWorkspace(rightOpen && selectedRef.current ? "trust" : "explore");
    window.setTimeout(() => repositoryButtonRef.current?.focus(), 0);
  }, [rightOpen]);

  const closeRightPanel = useCallback(() => {
    setRightOpen(false);
    setCurrentWorkspace("explore");
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

  const dismissMapUtilityWithoutFocus = useCallback(() => {
    mapUtilityReturnRef.current = null;
    setMapUtilityOpen(false);
    setMapQueryCandidates([]);
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
    if (isCompact) {
      setLeftOpen(false);
      setRightOpen(false);
      setTimelineOpen(false);
    }
    window.setTimeout(() => mapUtilityPanelRef.current?.querySelector<HTMLElement>("button:not([disabled])")?.focus(), 0);
  }, [isCompact]);

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
    updateRendererNeutralView({
      center: focus,
      zoom: Math.max(mapRuntimeRef.current?.getSnapshot().camera.zoom ?? KANSAS_VIEW.zoom, 7),
    });
  }, [openSelection, updateRendererNeutralView]);

  const openGuidedExample = useCallback((example: (typeof GUIDED_EXAMPLES)[number]) => {
    yearRef.current = example.year;
    setYear(example.year);
    setPlaying(false);
    setLeftOpen(false);
    setTimelineOpen(false);
    dismissGuidedStart();
    selectStoredFeature(example.layerId, example.featureId);
    announce(`Opened ${example.title} guided example at ${example.year}`);
  }, [announce, dismissGuidedStart, selectStoredFeature]);

  const openStoryStep = useCallback((requestedIndex: number) => {
    const nextIndex = Math.max(0, Math.min(KFM_STORY_TRAIL.length - 1, requestedIndex));
    const step = KFM_STORY_TRAIL[nextIndex];
    setStoryStepIndex(nextIndex);
    setStoryOpen(true);
    setGuidedStartOpen(false);
    setHelpOpen(false);
    setPlaying(false);
    yearRef.current = step.year;
    setYear(step.year);
    setLeftOpen(false);
    setTimelineOpen(false);
    selectStoredFeature(step.layerId, step.featureId);
    announce(`Story step ${nextIndex + 1} of ${KFM_STORY_TRAIL.length}: ${step.eyebrow}`);
  }, [announce, selectStoredFeature]);

  const startStoryTrail = useCallback(() => openStoryStep(0), [openStoryStep]);

  const closeStoryTrail = useCallback(() => {
    setStoryOpen(false);
    announce("Guided story closed; the current map selection was preserved");
  }, [announce]);

  const clearSelectionState = useCallback(() => {
    setFocusStage("outcome");
    setFocusIntent("explain");
    setPendingFocusAction(null);
    selectedRef.current = null;
    returnFocusRef.current = null;
    setSelected(null);
    setRightOpen(false);
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
      replayingCameraHistoryRef.current = true;
      applyRendererNeutralView(restoredView);
      cameraHistoryRef.current = [restoredView];
      cameraHistoryIndexRef.current = 0;
      setCameraHistoryIndex(0);
      setCameraHistoryLength(1);
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

      const knownLayerIds = new Set(LAYER_REGISTRY.map((layer) => layer.id));
      const visibleIds = params.get("l")?.split(",").filter((id) => knownLayerIds.has(id)) ?? [];
      const restoredVisibility = params.has("l")
        ? Object.fromEntries(LAYER_REGISTRY.map((layer) => [layer.id, visibleIds.includes(layer.id)]))
        : defaultVisibility;
      const opacityPairs = params.get("o")?.split(",").map((pair) => pair.split(":")) ?? [];
      const restoredOpacity = Object.fromEntries(opacityPairs
        .filter(([id, value]) => knownLayerIds.has(id) && typeof value === "string" && value.trim() !== "" && Number.isFinite(Number(value)))
        .map(([id, value]) => [id, clamp(Number(value), 0, 1)]));
      const nextOpacity = { ...defaultOpacity, ...restoredOpacity };
      const restoredYear = Number(params.get("t"));
      const nextYear = TIME_STEPS.includes(restoredYear as (typeof TIME_STEPS)[number]) ? restoredYear : 2026;
      yearRef.current = nextYear;
      setYear(nextYear);
      const restoredBasemap = params.get("base");
      const nextBasemap: BasemapKey = restoredBasemap === "prairie" ? "prairie" : "midnight";
      basemapRef.current = nextBasemap;
      setBasemap(nextBasemap);
      const restoredProjection = params.get("proj");
      const nextProjection = restoredProjection === "globe" ? "globe" : "mercator";
      projectionRef.current = nextProjection;
      setProjection(nextProjection);
      const restoredScene = params.get("scene");
      const nextScenePreset: ScenePresetId = restoredScene === "globe-overview" || restoredScene === "water-systems" || restoredScene === "smoke-context" || restoredScene === "elevation-3d" || restoredScene === "tile-grid" ? restoredScene : "overview-2d";
      setScenePreset(nextScenePreset);
      const nextVerticalExaggeration = clamp(parseNumber(params.get("zscale"), 1), 0, 2);
      verticalExaggerationRef.current = nextVerticalExaggeration;
      setVerticalExaggeration(nextVerticalExaggeration);
      const restoredAtmosphere = params.get("sky");
      const nextAtmosphere: AtmospherePreset = restoredAtmosphere === "dusk" || restoredAtmosphere === "clear" ? restoredAtmosphere : "night";
      atmospherePresetRef.current = nextAtmosphere;
      setAtmospherePreset(nextAtmosphere);
      const nextLightAzimuth = clamp(parseNumber(params.get("light"), 210), 0, 359);
      lightAzimuthRef.current = nextLightAzimuth;
      setLightAzimuth(nextLightAzimuth);
      const nextFieldOfView = clamp(parseNumber(params.get("fov"), 36), 20, 60);
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
      const nextMapUtilityView: MapUtilityView = restoredMapUtilityView === "report" || restoredMapUtilityView === "inspect" || restoredMapUtilityView === "scene" || restoredMapUtilityView === "connections" || restoredMapUtilityView === "import" || restoredMapUtilityView === "compare" || restoredMapUtilityView === "display" || restoredMapUtilityView === "measure" || restoredMapUtilityView === "export" || restoredMapUtilityView === "diagnostics" ? restoredMapUtilityView : "navigate";
      setMapUtilityView(nextMapUtilityView);
      const restoredCompareIds = params.get("compare")?.split(",") ?? [];
      if (restoredCompareIds.length === 2 && restoredCompareIds.every((id) => knownLayerIds.has(id)) && restoredCompareIds[0] !== restoredCompareIds[1]) {
        setCompareLeftId(restoredCompareIds[0]);
        setCompareRightId(restoredCompareIds[1]);
      }
      const restoredTimes = params.get("times")?.split(",").map(Number) ?? [];
      if (restoredTimes.length === 2 && restoredTimes.every((candidate) => TIME_STEPS.includes(candidate as (typeof TIME_STEPS)[number]))) {
        setCompareTimeA(restoredTimes[0]);
        setCompareTimeB(restoredTimes[1]);
      }
      if (nextMapUtilityView === "export") setExportGeneratedAt(new Date().toISOString());
      if (nextMapUtilityView === "report") setReportGeneratedAt(new Date().toISOString());
      const restoredMapUtilityOpen = params.get("mapui") === "open";
      setMapUtilityOpen(restoredMapUtilityOpen);
      if (restoredMapUtilityOpen && compactRef.current) {
        setLeftOpen(false);
        setRightOpen(false);
        setTimelineOpen(false);
      }
      const restoredOrder = params.get("order")?.split(",").filter(Boolean) ?? [];
      const nextOrder = restoredOrder.length === knownLayerIds.size
        && new Set(restoredOrder).size === knownLayerIds.size
        && restoredOrder.every((id) => knownLayerIds.has(id)) ? restoredOrder : defaultOrder;
      requestedLayers.replace({ visibility: restoredVisibility, opacity: nextOpacity, layerOrder: nextOrder });
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
  }, [applyRendererNeutralView]);

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
    const initialView = pendingViewRef.current ?? KANSAS_VIEW;
    const runtimePort = createNullMapRuntime({
      longitude: initialView.center[0],
      latitude: initialView.center[1],
      zoom: initialView.zoom,
      bearing: initialView.bearing,
      pitch: initialView.pitch,
    });
    mapRuntimeRef.current = runtimePort;
    const unsubscribe = runtimePort.subscribeSnapshot((snapshot) => {
      if (disposed || snapshot.state === "DISPOSED") return;
      const nextView: ViewState = {
        center: [snapshot.camera.longitude, snapshot.camera.latitude],
        zoom: snapshot.camera.zoom,
        bearing: snapshot.camera.bearing,
        pitch: snapshot.camera.pitch,
      };
      setView(nextView);
      setPointer([...nextView.center] as [number, number]);
    });

    void runtimePort.initialize().then(() => {
      if (disposed) return;
      setRuntime({
        kind: "degraded",
        message: "Renderer acquisition is held. NullMapRuntime preserves serializable camera and catalog state without MapLibre, WebGL, workers, sources, tiles, or network access.",
      });
    }).catch(() => {
      if (disposed) return;
      setRuntime({
        kind: "error",
        message: "The renderer-neutral fallback could not initialize; catalog and evidence metadata remain readable.",
      });
    });

    return () => {
      disposed = true;
      unsubscribe();
      runtimePort.dispose();
      if (mapRuntimeRef.current === runtimePort) mapRuntimeRef.current = null;
    };
  }, []);

  useEffect(() => {
    if (!playing) return;
    const timer = window.setInterval(() => {
      setYear((current) => TIME_STEPS[(TIME_STEPS.indexOf(current as (typeof TIME_STEPS)[number]) + 1) % TIME_STEPS.length]);
    }, 1300);
    return () => window.clearInterval(timer);
  }, [playing]);

  useEffect(() => {
    const timer = window.setTimeout(() => {
      const params = buildExplorerParams();
      window.history.replaceState(null, "", `${window.location.pathname}?${params.toString()}`);
    }, 280);
    return () => window.clearTimeout(timer);
  }, [buildExplorerParams]);

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
      else if (helpOpen) setHelpOpen(false);
      else if (guidedStartOpen) dismissGuidedStart();
      else if (storyOpen) closeStoryTrail();
      else if (toolsExpanded) setToolsExpanded(false);
      else if (mapUtilityOpen) closeMapUtility();
      else if (measureModeRef.current) {
        measureModeRef.current = null;
        measurementGeometryModeRef.current = null;
        measureCoordinatesRef.current = [];
        setMeasureMode(null);
        setMeasurementGeometryMode(null);
        setMeasurement("Measurement cancelled");
      }
      else if (!isCompact && rightOpen) closeRightPanel();
    };
    document.addEventListener("keydown", handleEscape);
    return () => document.removeEventListener("keydown", handleEscape);
  }, [guidedStartOpen, helpOpen, isCompact, mapUtilityOpen, repositoryOpen, rightOpen, storyOpen, toolsExpanded, closeMapUtility, closeRightPanel, closeStoryTrail, dismissGuidedStart]);

  const chooseSearchResult = (item: SearchItem) => {
    setGlobalQuery("");
    if (item.kind === "feature" && item.featureId) {
      selectStoredFeature(item.layerId, item.featureId);
      return;
    }
    const layer = LAYER_REGISTRY.find((candidate) => candidate.id === item.layerId);
    if (!layer) return;
    setVisibility((current) => ({ ...current, [layer.id]: true }));
    fitRendererNeutralBounds(layer.bounds);
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
    fitRendererNeutralBounds(layer.bounds);
  };

  const fitKansasView = () => {
    if (locationDerivedViewRef.current) {
      locationDerivedViewRef.current = false;
      setLocationCameraRedacted(false);
      applyRendererNeutralView(KANSAS_VIEW);
      announce("Private location camera cleared and reset to the generalized Kansas extent");
      return;
    }
    fitRendererNeutralBounds([-102.1, 36.95, -94.55, 40.05]);
    announce("Framed the generalized Kansas demonstration extent in renderer-neutral camera state");
  };

  const startAreaDraw = () => {
    if (locationDerivedViewRef.current || locationCameraRedacted) {
      announce("Clear the private location camera before drawing a shareable report area");
      return;
    }
    stopSceneOrbit(false);
    projectionRef.current = "mercator";
    setProjection("mercator");
    updateRendererNeutralView({ bearing: 0, pitch: 0 });
    areaDrawRef.current = null;
    setAreaDrawBox(null);
    setAreaDrawMode(true);
    setToolsExpanded(false);
    dismissMapUtilityWithoutFocus();
    window.setTimeout(() => document.querySelector<HTMLElement>(".map-query-surface")?.focus(), 0);
    announce("Box query ready · drag on the north-up map to define a report area, or press Escape to cancel");
  };

  const cancelAreaDraw = (notify = true) => {
    areaDrawRef.current = null;
    setAreaDrawBox(null);
    setAreaDrawMode(false);
    if (notify) announce("Box query cancelled; the previous report area was preserved");
  };

  const mapPointFromPointer = (event: React.PointerEvent<HTMLDivElement>) => {
    const bounds = event.currentTarget.getBoundingClientRect();
    const x = clamp(event.clientX - bounds.left, 0, bounds.width);
    const y = clamp(event.clientY - bounds.top, 0, bounds.height);
    const longitude = mapViewportBounds.west + (x / Math.max(bounds.width, 1)) * (mapViewportBounds.east - mapViewportBounds.west);
    const latitude = mapViewportBounds.north - (y / Math.max(bounds.height, 1)) * (mapViewportBounds.north - mapViewportBounds.south);
    setPointer([longitude, latitude]);
    return { x, y, width: bounds.width, height: bounds.height };
  };

  const handleMapAreaPointerDown = (event: React.PointerEvent<HTMLDivElement>) => {
    const point = mapPointFromPointer(event);
    if (!areaDrawMode || event.button !== 0) return;
    event.preventDefault();
    event.currentTarget.setPointerCapture(event.pointerId);
    areaDrawRef.current = { pointerId: event.pointerId, startX: point.x, startY: point.y, width: point.width, height: point.height };
    setAreaDrawBox({ left: point.x, top: point.y, width: 0, height: 0 });
  };

  const handleMapAreaPointerMove = (event: React.PointerEvent<HTMLDivElement>) => {
    const point = mapPointFromPointer(event);
    const drawing = areaDrawRef.current;
    if (!areaDrawMode || !drawing || drawing.pointerId !== event.pointerId) return;
    event.preventDefault();
    setAreaDrawBox({
      left: Math.min(drawing.startX, point.x),
      top: Math.min(drawing.startY, point.y),
      width: Math.abs(point.x - drawing.startX),
      height: Math.abs(point.y - drawing.startY),
    });
  };

  const handleMapAreaPointerUp = (event: React.PointerEvent<HTMLDivElement>) => {
    const point = mapPointFromPointer(event);
    const drawing = areaDrawRef.current;
    if (!areaDrawMode || !drawing || drawing.pointerId !== event.pointerId) return;
    event.preventDefault();
    if (event.currentTarget.hasPointerCapture(event.pointerId)) event.currentTarget.releasePointerCapture(event.pointerId);
    const nextArea = screenRectToBounds(
      { startX: drawing.startX, startY: drawing.startY, endX: point.x, endY: point.y },
      { width: drawing.width, height: drawing.height },
      mapViewportBounds,
    );
    areaDrawRef.current = null;
    setAreaDrawBox(null);
    if (!nextArea) {
      announce("Draw a larger report area; the previous area was preserved");
      return;
    }
    analysisAreaRef.current = { ...nextArea };
    setAnalysisArea({ ...nextArea });
    setReportScope("ANALYSIS_AREA");
    setReportGeneratedAt(new Date().toISOString());
    setAreaDrawMode(false);
    openMapUtility("report");
    announce("Box query committed to the custom report; map pixels remain context, not evidence");
  };

  const captureAnalysisArea = () => {
    if (locationDerivedViewRef.current) {
      announce("Clear the private location camera before capturing a shareable analysis area");
      return;
    }
    const nextArea: MapBoundsState = {
      west: clamp(mapViewportBounds.west, SUPPORTED_CONTEXT_BOUNDS.west, SUPPORTED_CONTEXT_BOUNDS.east),
      south: clamp(mapViewportBounds.south, SUPPORTED_CONTEXT_BOUNDS.south, SUPPORTED_CONTEXT_BOUNDS.north),
      east: clamp(mapViewportBounds.east, SUPPORTED_CONTEXT_BOUNDS.west, SUPPORTED_CONTEXT_BOUNDS.east),
      north: clamp(mapViewportBounds.north, SUPPORTED_CONTEXT_BOUNDS.south, SUPPORTED_CONTEXT_BOUNDS.north),
    };
    analysisAreaRef.current = nextArea;
    setAnalysisArea(nextArea);
    setReportScope("ANALYSIS_AREA");
    setReportGeneratedAt(new Date().toISOString());
    announce("Locked the current renderer-neutral view bounds as the report area of interest");
  };

  const clearAnalysisArea = () => {
    analysisAreaRef.current = null;
    setAnalysisArea(null);
    areaDrawRef.current = null;
    setAreaDrawBox(null);
    setAreaDrawMode(false);
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
    fitRendererNeutralBounds([analysisArea.west, analysisArea.south, analysisArea.east, analysisArea.north], 11);
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
    fitRendererNeutralBounds([
      clamp(west, SUPPORTED_CONTEXT_BOUNDS.west, SUPPORTED_CONTEXT_BOUNDS.east),
      clamp(south, SUPPORTED_CONTEXT_BOUNDS.south, SUPPORTED_CONTEXT_BOUNDS.north),
      clamp(east, SUPPORTED_CONTEXT_BOUNDS.west, SUPPORTED_CONTEXT_BOUNDS.east),
      clamp(north, SUPPORTED_CONTEXT_BOUNDS.south, SUPPORTED_CONTEXT_BOUNDS.north),
    ], 12);
    announce("Fit the browser-local import inspection bounds; the derived camera remains private and redacted");
  };

  const inspectImportFile = async (file?: File | null) => {
    if (!file) return;
    const inspectionGeneration = ++importInspectionGenerationRef.current;
    setImportBusy(true);
    setImportError("");
    setImportPreview(null);
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
      setImportPreview(preview);
      if (preview.renderAllowed) fitImportPreview(preview);
      announce(preview.renderAllowed
        ? `Inspected ${preview.featureCount} browser-local ${preview.sourceFormat} feature${preview.featureCount === 1 ? "" : "s"}; renderer acquisition remains held`
        : "File inspected, but the preview is blocked outside the supported Kansas context");
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

  const clearImportPreview = () => {
    importInspectionGenerationRef.current += 1;
    setImportPreview(null);
    setImportError("");
    setImportBusy(false);
    if (importInputRef.current) importInputRef.current.value = "";
    announce("Cleared the browser-local import inspection");
  };

  const copyImportPreviewAudit = async () => {
    if (!importPreview) return;
    try {
      await navigator.clipboard.writeText(JSON.stringify(importPreviewAudit(importPreview), null, 2));
      announce("Copied the redacted import inspection record");
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
    updateRendererNeutralView({ ...nextView, center: [...nextView.center] as [number, number] });
    announce(direction < 0 ? "Returned to the previous map view" : "Advanced to the next map view");
  };

  const inspectLayer = (layer: LayerRecord, returnElement: HTMLElement) => {
    const featureId = inspectableFeatureId(layer, year);
    if (!featureId) {
      announce(`${layer.title} has no feature compatible with ${formatTimelineStep(year)}`);
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
    updateRendererNeutralView({
      center: [match.feature.properties.focusLng, match.feature.properties.focusLat],
      zoom: Math.max(mapRuntimeRef.current?.getSnapshot().camera.zoom ?? KANSAS_VIEW.zoom, 8),
    });
    announce(`Centered ${match.feature.properties.title} in renderer-neutral camera state`);
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
    updateRendererNeutralView({
      center: [longitude, latitude],
      zoom: Math.max(mapRuntimeRef.current?.getSnapshot().camera.zoom ?? KANSAS_VIEW.zoom, 9),
    });
    announce(`Centered ${latitude.toFixed(4)}°, ${longitude.toFixed(4)}° in renderer-neutral camera state`);
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
      updateRendererNeutralView({
        center: points[0],
        zoom: Math.max(mapRuntimeRef.current?.getSnapshot().camera.zoom ?? KANSAS_VIEW.zoom, 9),
      });
    } else {
      const longitudes = points.map(([longitude]) => longitude);
      const latitudes = points.map(([, latitude]) => latitude);
      fitRendererNeutralBounds([
        Math.min(...longitudes),
        Math.min(...latitudes),
        Math.max(...longitudes),
        Math.max(...latitudes),
      ], 10);
    }
    announce(`Fit ${mapFeatureIndex.length} compatible indexed feature${mapFeatureIndex.length === 1 ? "" : "s"}`);
  };

  const applyScenePreset = (preset: ScenePresetId) => {
    const scene = {
      "overview-2d": {
        layers: ["kansas-extent", "watershed-context", "water-context", "prairie-context", "atmosphere-observations", "communities"],
        basemap: "midnight" as BasemapKey,
        projection: "mercator" as const,
        camera: { ...KANSAS_VIEW },
        scale: 1,
        atmosphere: "night" as AtmospherePreset,
        lightAzimuth: 210,
        fieldOfView: 36,
        label: "2D Kansas overview",
      },
      "globe-overview": {
        layers: ["kansas-extent", "watershed-context", "water-context", "prairie-context", "atmosphere-observations", "communities"],
        basemap: "midnight" as BasemapKey,
        projection: "globe" as const,
        camera: { center: [-98.38, 38.48] as [number, number], zoom: 4.8, bearing: -16, pitch: 22 },
        scale: 1,
        atmosphere: "clear" as AtmospherePreset,
        lightAzimuth: 225,
        fieldOfView: 42,
        label: "Renderer-neutral globe overview",
      },
      "water-systems": {
        layers: ["kansas-extent", "watershed-context", "water-context", "communities"],
        basemap: "midnight" as BasemapKey,
        projection: "mercator" as const,
        camera: { center: [-98.25, 38.55] as [number, number], zoom: 6.05, bearing: 0, pitch: 18 },
        scale: 1,
        atmosphere: "clear" as AtmospherePreset,
        lightAzimuth: 195,
        fieldOfView: 38,
        label: "Water systems scene",
      },
      "smoke-context": {
        layers: ["kansas-extent", "watershed-context", "smoke-context", "atmosphere-observations", "communities"],
        basemap: "midnight" as BasemapKey,
        projection: "mercator" as const,
        camera: { center: [-97.05, 38.65] as [number, number], zoom: 6.0, bearing: -8, pitch: 28 },
        scale: 1,
        atmosphere: "dusk" as AtmospherePreset,
        lightAzimuth: 248,
        fieldOfView: 40,
        label: "Synthetic smoke context scene",
      },
      "elevation-3d": {
        layers: ["kansas-extent", "watershed-context", "water-context", "elevation-concept", "communities"],
        basemap: "prairie" as BasemapKey,
        projection: "mercator" as const,
        camera: { center: [-98.38, 38.48] as [number, number], zoom: 5.8, bearing: -18, pitch: 52 },
        scale: 1.2,
        atmosphere: "dusk" as AtmospherePreset,
        lightAzimuth: 235,
        fieldOfView: 44,
        label: "Synthetic elevation extrusion scene",
      },
      "tile-grid": {
        layers: ["kansas-extent", "tile-matrix-grid", "water-context", "communities"],
        basemap: "midnight" as BasemapKey,
        projection: "mercator" as const,
        camera: { center: [-98.38, 38.48] as [number, number], zoom: 6.2, bearing: 0, pitch: 0 },
        scale: 1,
        atmosphere: "night" as AtmospherePreset,
        lightAzimuth: 210,
        fieldOfView: 36,
        label: "Tile diagnostic grid scene",
      },
    }[preset];
    stopSceneOrbit(false);
    const nextVisibility = Object.fromEntries(LAYER_REGISTRY.map((layer) => [layer.id, scene.layers.includes(layer.id)]));
    yearRef.current = 2026;
    basemapRef.current = scene.basemap;
    projectionRef.current = scene.projection;
    verticalExaggerationRef.current = scene.scale;
    atmospherePresetRef.current = scene.atmosphere;
    lightAzimuthRef.current = scene.lightAzimuth;
    fieldOfViewRef.current = scene.fieldOfView;
    setVisibility(nextVisibility);
    setYear(2026);
    setPlaying(false);
    setBasemap(scene.basemap);
    setProjection(scene.projection);
    setScenePreset(preset);
    setVerticalExaggeration(scene.scale);
    setAtmospherePreset(scene.atmosphere);
    setLightAzimuth(scene.lightAzimuth);
    setFieldOfView(scene.fieldOfView);
    setMapQueryCandidates([]);
    locationDerivedViewRef.current = false;
    setLocationCameraRedacted(false);
    clearSelectionState();
    updateRendererNeutralView(scene.camera);
    announce(`${scene.label} applied · reversible browser-only view state`);
  };

  const toggleSceneLayer = (layerId: "watershed-context" | "smoke-context" | "elevation-concept" | "tile-matrix-grid") => {
    setVisibility((current) => {
      const next = { ...current, [layerId]: !current[layerId] };
      return next;
    });
  };

  const orientSceneCamera = (pitch: number, bearing = view.bearing) => {
    updateRendererNeutralView({ pitch, bearing });
  };

  const startSceneOrbit = () => {
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      announce("Orbit is paused because reduced motion is enabled");
      return;
    }
    stopSceneOrbit(false);
    setSceneOrbiting(true);
    replayingCameraHistoryRef.current = true;
    updateRendererNeutralView({ bearing: view.bearing + 90, pitch: Math.max(46, view.pitch) });
    sceneOrbitTimerRef.current = window.setTimeout(() => {
      sceneOrbitTimerRef.current = null;
      setSceneOrbiting(false);
    }, 900);
    announce("Applied a reversible 90° renderer-neutral camera turn; MapLibre animation remains held");
  };

  const setMapGestureMode = (mode: "cooperative" | "direct") => {
    gestureModeRef.current = mode;
    setGestureMode(mode);
    announce(mode === "cooperative" ? "Cooperative map gestures enabled" : "Direct map gestures enabled");
  };

  const probeSourceConnection = (layer: LayerRecord) => {
    const uniqueFeatures = new Set(layer.data.features
      .filter((feature) => isFeatureAvailableAtTime(layer, feature.properties.year, year))
      .map((feature) => feature.properties.fid));
    setSourceActivity((current) => ({ ...current, [layer.id]: "SETTLED" }));
    setSourceProbeCounts((current) => ({ ...current, [layer.id]: uniqueFeatures.size }));
    announce(`${layer.title} site-local fixture inspection returned ${uniqueFeatures.size} stable feature${uniqueFeatures.size === 1 ? "" : "s"}; renderer source queries remain held`);
  };

  const inspectSourceConnection = (layer: LayerRecord) => {
    setMapFeatureQuery("");
    setMapFeatureLayer(layer.id);
    activateMapUtilityView("inspect");
  };

  const applyViewProfile = (profile: MapViewProfile) => {
    const nextVisibility = Object.fromEntries(LAYER_REGISTRY.map((layer) => [layer.id, profile.visibleLayerIds.includes(layer.id)]));
    const nextScenePreset: ScenePresetId = profile.id === "smoke" ? "smoke-context" : profile.id === "elevation" ? "elevation-3d" : profile.projection === "globe" ? "globe-overview" : "overview-2d";
    const nextAtmosphere: AtmospherePreset = profile.id === "smoke" || profile.id === "elevation" ? "dusk" : profile.projection === "globe" ? "clear" : "night";
    const nextFieldOfView = profile.id === "elevation" ? 44 : profile.projection === "globe" ? 42 : 36;
    stopSceneOrbit(false);
    yearRef.current = profile.year;
    basemapRef.current = profile.basemap;
    projectionRef.current = profile.projection;
    atmospherePresetRef.current = nextAtmosphere;
    fieldOfViewRef.current = nextFieldOfView;
    setVisibility(nextVisibility);
    setYear(profile.year);
    setPlaying(false);
    setBasemap(profile.basemap);
    setProjection(profile.projection);
    setScenePreset(nextScenePreset);
    setAtmospherePreset(nextAtmosphere);
    setFieldOfView(nextFieldOfView);
    setMapQueryCandidates([]);
    locationDerivedViewRef.current = false;
    setLocationCameraRedacted(false);
    clearSelectionState();
    fitRendererNeutralBounds([-102.1, 36.95, -94.55, 40.05]);
    announce(`${profile.title} applied · view state only`);
  };

  const applyAnalysisRecipe = (recipe: AnalysisRecipe) => {
    const nextVisibility = Object.fromEntries(LAYER_REGISTRY.map((layer) => [layer.id, recipe.layerIds.includes(layer.id)]));
    stopSceneOrbit(false);
    yearRef.current = recipe.year;
    basemapRef.current = recipe.basemap;
    projectionRef.current = "mercator";
    atmospherePresetRef.current = "night";
    lightAzimuthRef.current = 210;
    fieldOfViewRef.current = 36;
    setVisibility(nextVisibility);
    setYear(recipe.year);
    setPlaying(false);
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
    updateRendererNeutralView({ center: [...recipe.center] as [number, number], zoom: recipe.zoom, bearing: 0, pitch: 0 });
    announce(`${recipe.title} recipe applied · map, time, layers, and report updated`);
  };

  const persistSavedWorkspaces = (next: WorkspaceSnapshot[]) => {
    const bounded = next.slice(0, 8);
    setSavedWorkspaces(bounded);
    try { window.localStorage.setItem(WORKSPACE_STORAGE_KEY, JSON.stringify(bounded)); } catch { /* Device-local workspace storage is optional. */ }
  };

  const saveCurrentWorkspace = () => {
    const savedAt = new Date().toISOString();
    const redactWorkspaceCamera = locationCameraRedacted || locationDerivedViewRef.current;
    const currentLayers = requestedLayers.getSnapshot();
    const snapshot: WorkspaceSnapshot = {
      id: `workspace-${Date.now()}`,
      name: workspaceName.trim() || `Kansas workspace ${savedWorkspaces.length + 1}`,
      savedAt,
      view: redactWorkspaceCamera
        ? { center: [...KANSAS_VIEW.center] as [number, number], zoom: KANSAS_VIEW.zoom, bearing: KANSAS_VIEW.bearing, pitch: KANSAS_VIEW.pitch }
        : { center: [...view.center] as [number, number], zoom: view.zoom, bearing: view.bearing, pitch: view.pitch },
      locationCameraRedacted: redactWorkspaceCamera,
      visibility: { ...currentLayers.visibility },
      opacity: { ...currentLayers.opacity },
      layerOrder: [...currentLayers.layerOrder],
      year,
      basemap,
      projection,
      scene: {
        preset: scenePreset,
        verticalExaggeration,
        atmosphere: atmospherePreset,
        lightAzimuth,
        fieldOfView,
      },
      analysisArea: analysisArea ? { ...analysisArea } : null,
      temporalComparison: { timeA: compareTimeA, timeB: compareTimeB },
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
    setWorkspaceName("");
    announce(`${snapshot.name} saved on this device`);
  };

  const loadSavedWorkspace = (snapshot: WorkspaceSnapshot) => {
    stopSceneOrbit(false);
    const knownLayerIds = new Set(LAYER_REGISTRY.map((layer) => layer.id));
    const nextVisibility = Object.fromEntries(LAYER_REGISTRY.map((layer) => [layer.id, snapshot.visibility?.[layer.id] === true]));
    const nextOpacity = Object.fromEntries(LAYER_REGISTRY.map((layer) => [layer.id, clamp(parseNumber(String(snapshot.opacity?.[layer.id] ?? layer.defaultOpacity), layer.defaultOpacity), 0, 1)]));
    const savedOrder = Array.isArray(snapshot.layerOrder) ? [...new Set(snapshot.layerOrder.filter((id) => knownLayerIds.has(id)))] : [];
    const nextOrder = [...savedOrder, ...defaultOrder.filter((id) => !savedOrder.includes(id))];
    const nextYear = TIME_STEPS.includes(snapshot.year as (typeof TIME_STEPS)[number]) ? snapshot.year : 2026;
    const nextBasemap: BasemapKey = snapshot.basemap === "prairie" ? "prairie" : "midnight";
    const nextProjection = snapshot.projection === "globe" ? "globe" : "mercator";
    // Legacy snapshots predate the marker, so fail closed instead of exposing a possibly location-derived camera.
    const restoredLocationCameraRedaction = snapshot.locationCameraRedacted !== false;
    const savedScene = snapshot.scene;
    const nextScenePreset: ScenePresetId = savedScene?.preset === "globe-overview" || savedScene?.preset === "water-systems" || savedScene?.preset === "smoke-context" || savedScene?.preset === "elevation-3d" || savedScene?.preset === "tile-grid" ? savedScene.preset : "overview-2d";
    const nextVerticalExaggeration = clamp(Number(savedScene?.verticalExaggeration ?? 1), 0, 2);
    const nextAtmosphere: AtmospherePreset = savedScene?.atmosphere === "dusk" || savedScene?.atmosphere === "clear" ? savedScene.atmosphere : "night";
    const nextLightAzimuth = clamp(Number(savedScene?.lightAzimuth ?? 210), 0, 359);
    const nextFieldOfView = clamp(Number(savedScene?.fieldOfView ?? 36), 20, 60);
    yearRef.current = nextYear;
    basemapRef.current = nextBasemap;
    projectionRef.current = nextProjection;
    verticalExaggerationRef.current = nextVerticalExaggeration;
    atmospherePresetRef.current = nextAtmosphere;
    lightAzimuthRef.current = nextLightAzimuth;
    fieldOfViewRef.current = nextFieldOfView;
    requestedLayers.replace({ visibility: nextVisibility, opacity: nextOpacity, layerOrder: nextOrder });
    setYear(nextYear);
    setPlaying(false);
    setBasemap(nextBasemap);
    setProjection(nextProjection);
    setScenePreset(nextScenePreset);
    setVerticalExaggeration(nextVerticalExaggeration);
    setAtmospherePreset(nextAtmosphere);
    setLightAzimuth(nextLightAzimuth);
    setFieldOfView(nextFieldOfView);
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
    const savedComparison = snapshot.temporalComparison;
    setCompareTimeA(TIME_STEPS.includes(savedComparison?.timeA as (typeof TIME_STEPS)[number]) ? savedComparison!.timeA : 1910);
    setCompareTimeB(TIME_STEPS.includes(savedComparison?.timeB as (typeof TIME_STEPS)[number]) ? savedComparison!.timeB : 2026);
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
      updateRendererNeutralView({ center: [...savedView.center] as [number, number], zoom: savedView.zoom, bearing: savedView.bearing, pitch: savedView.pitch });
    }
    const restoredSelection = snapshot.selection ? copyFeature(LAYER_REGISTRY.find((layer) => layer.id === snapshot.selection?.layerId) ?? LAYER_REGISTRY[0], snapshot.selection.featureId) : null;
    selectedRef.current = restoredSelection;
    setSelected(restoredSelection);
    setRightOpen(false);
    setMapQueryCandidates([]);
    announce(`${snapshot.name} restored from this device`);
  };

  const deleteSavedWorkspace = (snapshot: WorkspaceSnapshot) => {
    persistSavedWorkspaces(savedWorkspaces.filter((candidate) => candidate.id !== snapshot.id));
    announce(`${snapshot.name} removed from this device`);
  };

  const restoreLastKnownGoodView = () => {
    const lastView = lastKnownGoodViewRef.current;
    applyRendererNeutralView({ ...lastView, center: [...lastView.center] as [number, number] });
    announce("Restored the last known local camera state");
  };

  const reapplyRendererState = () => {
    const runtimePort = mapRuntimeRef.current;
    if (!runtimePort) {
      announce("Renderer-neutral runtime is unavailable; no state was changed");
      return;
    }
    try {
      const snapshot = runtimePort.getSnapshot();
      applyRendererNeutralView({
        center: [snapshot.camera.longitude, snapshot.camera.latitude],
        zoom: snapshot.camera.zoom,
        bearing: snapshot.camera.bearing,
        pitch: snapshot.camera.pitch,
      });
      setRuntime({ kind: "degraded", message: "Renderer acquisition remains held; serializable NullMapRuntime camera state was reasserted without loading styles, sources, tiles, or workers." });
      announce("Reasserted renderer-neutral camera state; renderer capabilities remain held");
    } catch {
      setRuntime({ kind: "error", message: "Renderer-neutral state could not be reasserted; catalog and evidence metadata remain readable." });
      announce("Renderer-neutral state could not be reasserted; no renderer was acquired");
    }
  };

  const resetExplorer = () => {
    yearRef.current = 2026;
    basemapRef.current = "midnight";
    projectionRef.current = "mercator";
    verticalExaggerationRef.current = 1;
    atmospherePresetRef.current = "night";
    lightAzimuthRef.current = 210;
    fieldOfViewRef.current = 36;
    gestureModeRef.current = "cooperative";
    requestedLayers.replace({ visibility: defaultVisibility, opacity: defaultOpacity, layerOrder: defaultOrder });
    setYear(2026);
    setBasemap("midnight");
    setProjection("mercator");
    setScenePreset("overview-2d");
    setVerticalExaggeration(1);
    setAtmospherePreset("night");
    setLightAzimuth(210);
    setFieldOfView(36);
    setGestureMode("cooperative");
    stopSceneOrbit(false);
    setMeasureMode(null);
    setMeasurementGeometryMode(null);
    measureModeRef.current = null;
    measurementGeometryModeRef.current = null;
    measureCoordinatesRef.current = [];
    setMeasurement("Select a measurement tool");
    locationDerivedViewRef.current = false;
    setLocationCameraRedacted(false);
    replayingCameraHistoryRef.current = true;
    cameraHistoryRef.current = [KANSAS_VIEW];
    cameraHistoryIndexRef.current = 0;
    setCameraHistoryIndex(0);
    setCameraHistoryLength(1);
    analysisAreaRef.current = null;
    setAnalysisArea(null);
    areaDrawRef.current = null;
    setAreaDrawBox(null);
    setAreaDrawMode(false);
    applyRendererNeutralView(KANSAS_VIEW);
    clearSelection();
    setMapQueryCandidates([]);
    setGuidedStartOpen(false);
    setReportTitle("Kansas map data report");
    setReportScope("VIEWPORT");
    setReportDetail("STANDARD");
    setReportLayerIds(LAYER_REGISTRY.filter((layer) => layer.defaultVisibility).map((layer) => layer.id));
    setReportSections(defaultReportSections);
    setReportQuery("");
    setReportEvidenceFilter("ALL");
    setCompareTimeA(1910);
    setCompareTimeB(2026);
    announce("Explorer reset to the Kansas demonstration view");
  };

  const toggleMeasure = (mode: Exclude<MeasureMode, null>) => {
    setMeasureMode(null);
    setMeasurementGeometryMode(null);
    measureModeRef.current = null;
    measurementGeometryModeRef.current = null;
    measureCoordinatesRef.current = [];
    setMeasurement(`HOLD · ${mode} measurement requires the conforming renderer consumer migration`);
    setToolsExpanded(false);
    setMapQueryCandidates([]);
    announce(`Screen ${mode} measurement remains held until renderer interactions cross MapRuntimePort`);
  };

  const undoMeasurementPoint = () => {
    announce("No renderer-backed measurement points are available while the consumer migration is held");
  };

  const finishMeasurement = () => {
    announce("Screen measurement remains held until renderer interactions cross MapRuntimePort");
  };

  const clearMeasurement = () => {
    measureModeRef.current = null;
    measurementGeometryModeRef.current = null;
    measureCoordinatesRef.current = [];
    setMeasureMode(null);
    setMeasurementGeometryMode(null);
    setMeasurement("Select a measurement tool");
    announce("Screen measurement cleared");
  };

  const changeMeasureUnit = (unit: MeasureUnit) => {
    measureUnitRef.current = unit;
    setMeasureUnit(unit);
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
      renderer: { family: "NullMapRuntime", package_candidate: "6.6.0", consumer_state: MAP_RUNTIME_CONSUMER_HOLD, repository_runtime_proven: false },
      camera: locationDerivedViewRef.current
        ? { center: "WITHHELD_BROWSER_LOCATION", zoom: "WITHHELD", bearing: "WITHHELD", pitch: "WITHHELD", projection }
        : { center: view.center, zoom: view.zoom, bearing: view.bearing, pitch: view.pitch, projection },
      display: { basemap, active_time: year, visible_layer_ids: activeLayers.map((layer) => layer.id), scene: scenePreset, atmosphere: atmospherePreset, light_azimuth: lightAzimuth, field_of_view: fieldOfView, gesture_mode: gestureMode },
      analysis_area: locationDerivedViewRef.current || !analysisArea
        ? null
        : { bounds: analysisArea, compatible_record_count: analysisAreaRecordCount, role: "SITE_LOCAL_CONTEXT_ONLY" },
      workspace: currentWorkspace,
      selection: selected ? {
        feature_id: selected.featureId,
        layer_id: selected.layerId,
        layer_visible: !selectedLayerHidden,
        time_compatible: !selectedTimeMismatch,
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
      site_renderer: { family: "NullMapRuntime", package_candidate: EXPECTED_MAPLIBRE_VERSION, consumer_state: MAP_RUNTIME_CONSUMER_HOLD, runtime_state: runtime.kind },
      runtime_proof: {
        expected_version: EXPECTED_MAPLIBRE_VERSION,
        worker: "NOT_RUN",
        runtime_assets: "NOT_RUN",
        webgl2: "NOT_RUN",
        map_constructed: false,
        canvas_ready: false,
        style_loaded: false,
        idle: false,
        tiles_loaded: false,
        sources_ready: `0/${LAYER_REGISTRY.length} · HELD`,
        controls_ready: false,
        interactions_ready: false,
        projection,
        reason: MAP_RUNTIME_CONSUMER_HOLD,
      },
      repository_boundary: {
        snapshot: REPOSITORY_SNAPSHOT.commit,
        architecture: "ACCEPTED",
        dependency: "EXACT_6.6.0",
        runtime: "BOUNDED_PACKAGE_OWNED_ADAPTER_SLICE",
        broader_production_activation: "HOLD",
      },
      camera: { zoom: Number(view.zoom.toFixed(2)), bearing: Math.round(view.bearing), pitch: Math.round(view.pitch), projection },
      style: { basemap_descriptor: basemap, style_loaded: false, state: "HOLD" },
      registry: { sources: LAYER_REGISTRY.length, renderers: interactiveLayerIds.length, visible_layers: visibleCount, source_states: sourceStates },
      source_connections: { activity: sourceActivity, probe_counts: sourceProbeCounts },
      active_time: year,
      workspace: currentWorkspace,
      selection: selected ? { feature_id: selected.featureId, layer_id: selected.layerId, layer_visible: !selectedLayerHidden, time_compatible: !selectedTimeMismatch } : null,
      analysis_area: { active: Boolean(analysisArea), compatible_record_count: analysisAreaRecordCount, coordinates: "OMITTED_FROM_REDACTED_DIAGNOSTIC" },
      redaction: "No raw coordinates, source URLs, tokens, stacks, prompts, private payloads, or browser location included.",
      public_effect: "NONE",
    };
    try {
      await navigator.clipboard.writeText(JSON.stringify(diagnostics, null, 2));
      announce("Redacted renderer-neutral diagnostics copied with no public effect");
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
        dataModes: source.dataModes,
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
      announce("Opened redacted renderer-neutral and runtime-seam diagnostics");
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
    const records = reportRecords.slice(0, reportRecordLimit).map(({ layer, properties, outsideActiveTime }) => ({
      id: properties.fid,
      title: properties.title,
      layer: layer.title,
      domain: layer.domain,
      year: properties.year,
      activeTimeCompatibility: outsideActiveTime ? "RETAINED_OUTSIDE_ACTIVE_TIME" : "COMPATIBLE_WITH_ACTIVE_TIME",
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
    const redactReportCamera = locationCameraRedacted || locationDerivedViewRef.current;
    return {
      format: "kfm-custom-map-report-v1",
      title: reportTitle.trim() || "Kansas map data report",
      generatedAt,
      detail: reportDetail,
      scope: reportScope,
      filters: { query: reportQuery || null, evidenceState: reportEvidenceFilter, layerIds: reportLayerIds },
      activeTime: { value: year, label: formatTimelineStep(year) },
      temporalComparison: reportTemporalComparison,
      mapContext: {
        center: redactReportCamera ? "WITHHELD_BROWSER_LOCATION" : view.center,
        zoom: redactReportCamera ? "WITHHELD_BROWSER_LOCATION" : view.zoom,
        projection,
        basemap,
        viewport: !redactReportCamera && reportScope === "VIEWPORT" ? mapViewportBounds : null,
        analysisArea: !redactReportCamera && reportScope === "ANALYSIS_AREA" ? analysisArea : null,
      },
      spatialQuery: !redactReportCamera && reportScope === "ANALYSIS_AREA" && analysisArea ? {
        profile: "kfm-site-spatial-query-plan-v1",
        relation: "FOCUS_POINT_INSIDE_BOUNDS",
        bounds: analysisArea,
        candidateCount: reportRecords.length,
        authority: "CONTEXT_ONLY",
        rendererHitsAreEvidence: false,
      } : null,
      selection: selected ? { id: selected.featureId, title: selected.properties.title, layer: selected.layer.title, evidenceState: selected.properties.evidenceState } : null,
      summary: reportSections.summary ? {
        matchedRecords: reportActiveTimeRecordCount,
        retainedSelectionRecords: reportRetainedSelectionCount,
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
        "Protected geometry is not reconstructed; location-derived camera coordinates remain withheld.",
        ...Array.from(new Set(records.map((record) => `${record.title}: ${record.generalization} ${record.uncertainty}`))),
      ] : null,
      attribution: reportLayerSummary.map((layer) => ({ layer: layer.title, source: layer.attribution })),
    };
  };

  const copyCustomReport = async () => {
    const generatedAt = new Date().toISOString();
    const report = buildCustomReportPayload(generatedAt);
    setReportGeneratedAt(generatedAt);
    try {
      await navigator.clipboard.writeText(JSON.stringify(report, null, 2));
      announce(`Custom report copied with ${reportIncludedRecordCount} included records`);
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
      content = `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${escapeReportHtml(report.title)}</title><style>body{font:15px/1.55 Inter,system-ui,sans-serif;color:#17201d;max-width:1100px;margin:0 auto;padding:48px}header{border-bottom:3px solid #b88b38;padding-bottom:22px;margin-bottom:28px}h1{font-size:36px;letter-spacing:-.04em;margin:0 0 8px}h2{margin-top:34px}small,.muted{color:#607069}.metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}.metric{border:1px solid #ccd6d1;padding:15px}.metric strong{display:block;font-size:24px}table{width:100%;border-collapse:collapse;font-size:13px}th,td{border-bottom:1px solid #dce3df;padding:10px;text-align:left;vertical-align:top}th{background:#f1f5f2}code{font-size:11px}li{margin:8px 0}.boundary{border-left:4px solid #b88b38;background:#f7f3ea;padding:14px 18px}@media print{body{padding:0}.boundary{break-inside:avoid}}@media(max-width:700px){body{padding:24px}.metrics{grid-template-columns:1fr 1fr}table{display:block;overflow:auto}}</style></head><body><header><small>KANSAS FRONTIER MATRIX · CUSTOM MAP REPORT</small><h1>${escapeReportHtml(report.title)}</h1><p>${escapeReportHtml(report.scope.replaceAll("_", " "))} · active time ${escapeReportHtml(report.activeTime.label)} · generated ${escapeReportHtml(generatedAt)}</p></header>${report.summary ? `<section><h2>Report summary</h2><div class="metrics"><div class="metric"><small>ACTIVE-TIME MATCHES</small><strong>${report.summary.matchedRecords}</strong></div><div class="metric"><small>INCLUDED RECORDS</small><strong>${report.summary.includedRecords}</strong></div><div class="metric"><small>RETAINED SELECTIONS</small><strong>${report.summary.retainedSelectionRecords}</strong></div><div class="metric"><small>LAYERS</small><strong>${report.summary.includedLayers}</strong></div></div></section>` : ""}${findings.length ? `<section><h2>Findings</h2><ol>${findings.map((finding) => `<li>${escapeReportHtml(finding)}</li>`).join("")}</ol></section>` : ""}<section><h2>Time A / Time B catalog availability</h2><div class="metrics"><div class="metric"><small>TIME A</small><strong>${escapeReportHtml(formatTimelineStep(report.temporalComparison.timeA))}</strong><span>${report.temporalComparison.timeARecordCount} records</span></div><div class="metric"><small>TIME B</small><strong>${escapeReportHtml(formatTimelineStep(report.temporalComparison.timeB))}</strong><span>${report.temporalComparison.timeBRecordCount} records</span></div><div class="metric"><small>CATALOG DELTA</small><strong>${report.temporalComparison.recordDelta > 0 ? "+" : ""}${report.temporalComparison.recordDelta}</strong><span>availability only</span></div><div class="metric"><small>CHANGED LAYERS</small><strong>${report.temporalComparison.changedLayerCount}</strong><span>entered / exited IDs</span></div></div><p class="boundary">This comparison reports time-compatible fixture records. It is not historical imagery, observed change, or evidence of causation.</p></section>${records.length ? `<section><h2>Included records</h2><table><thead><tr><th>Record</th><th>Layer / time</th><th>Evidence</th><th>Summary</th></tr></thead><tbody>${records.map((record) => `<tr><td><strong>${escapeReportHtml(record.title)}</strong><br><code>${escapeReportHtml(record.id)}</code></td><td>${escapeReportHtml(record.layer)}<br>${escapeReportHtml(record.year)}${record.activeTimeCompatibility === "RETAINED_OUTSIDE_ACTIVE_TIME" ? "<br><strong>RETAINED OUTSIDE ACTIVE TIME</strong>" : ""}</td><td>${escapeReportHtml(record.evidenceState)}<br><code>${escapeReportHtml(record.evidenceReference)}</code></td><td>${escapeReportHtml(record.summary)}</td></tr>`).join("")}</tbody></table></section>` : ""}${limitations.length ? `<section><h2>Limitations</h2><ul>${limitations.map((limitation) => `<li>${escapeReportHtml(limitation)}</li>`).join("")}</ul></section>` : ""}<section><h2>Attribution</h2><ul>${report.attribution.map((item) => `<li><strong>${escapeReportHtml(item.layer)}:</strong> ${escapeReportHtml(item.source)}</li>`).join("")}</ul></section><p class="boundary">This report is a browser-generated public-safe demonstration artifact. It does not release, publish, admit, or authorize KFM data.</p></body></html>`;
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
    announce(`${format.toUpperCase()} report downloaded with ${reportIncludedRecordCount} included records`);
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
        updateRendererNeutralView({ center: [coords.longitude, coords.latitude], zoom: 10 });
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
          <button type="button" title="Layers · shortcut L" aria-pressed={leftOpen} onClick={() => { setLeftOpen((current) => !current); setCurrentWorkspace("knowledge"); if (isCompact) { dismissMapUtilityWithoutFocus(); setRightOpen(false); setTimelineOpen(false); } }}><span aria-hidden="true">▦</span>Layers</button>
          <button className="header-report-action" type="button" title="Build report · shortcut R" aria-pressed={mapUtilityOpen && mapUtilityView === "report"} onClick={(event) => openMapUtility("report", event.currentTarget)}><span aria-hidden="true">＋</span>Build report</button>
        </nav>
        <div className="global-search">
          <label>
            <span className="sr-only">Search current layers and demonstration features</span>
            <span aria-hidden="true">⌕</span>
            <input ref={globalSearchInputRef} value={globalQuery} onChange={(event) => setGlobalQuery(event.target.value)} type="search" placeholder="Search places, layers, feature IDs…" aria-describedby="global-search-help" title="Search · shortcut /" />
          </label>
          <span id="global-search-help" className="sr-only">Search results appear as keyboard-focusable buttons.</span>
          {globalQuery && <div className="search-results" id="global-search-results" aria-label="Search results">
            {searchResults.map((item) => <button type="button" key={item.id} onClick={() => chooseSearchResult(item)}><span>{item.kind}</span><strong>{item.title}</strong><small>{item.subtitle}</small></button>)}
            {searchResults.length === 0 && <p>No current layer, place, dataset, or feature ID matches.</p>}
          </div>}
        </div>
        <div className="top-context" aria-label="Current map context">
          <span><small>AREA</small><strong>{selectedLabel}</strong></span>
          <span><small>TIME</small><strong>{formatTimelineStep(year)}</strong></span>
          <span className="release-indicator" data-selection-state={selected?.properties.evidenceState ?? "DEMONSTRATION"} title="Visible selection posture; not release or publication authority"><i /> {selected ? selectedEvidence?.label.toUpperCase() : "DEMONSTRATION"}</span>
        </div>
        <div className="top-actions">
          <button className="share-action" type="button" onClick={shareView} aria-label="Share current map view" title="Share current view">↗</button>
          <Link className="about-action" href="/about">About</Link>
        </div>
        {helpOpen && <aside className="map-guide" role="dialog" aria-modal="false" aria-label="Map guide">
          <button className="icon-close" type="button" onClick={() => setHelpOpen(false)} aria-label="Close map guide">×</button>
          <p className="panel-kicker">MAP GUIDE</p><h2>Explore a feature, then check what supports it.</h2>
          <p>Nothing in this build is a released operational dataset. Every layer uses site-local synthetic or generalized demonstration data. Choose an example or select any feature to inspect its evidence state.</p>
          <div className="map-guide-actions"><button className="map-guide-start" type="button" onClick={showGuidedStart}>Try quick examples</button><button className="map-guide-start" type="button" onClick={startStoryTrail}>Start four-step story</button></div>
          <ol><li>Search, choose an example, or enable a layer.</li><li>Select a feature.</li><li>Inspect what is supported, missing, corrected, or withheld.</li><li>Review time, lineage, and Focus Mode when you need more detail.</li></ol>
          <p><strong>Renderer interactions are held.</strong> The Map Workbench retains renderer-neutral coordinate navigation, camera state, and catalog-scoped feature discovery. Box zoom, terrain, and swipe comparison remain unavailable pending a conforming consumer and admitted sources.</p>
        </aside>}
      </header>

      <div className="repository-overlay" hidden={!repositoryOpen} onMouseDown={(event) => { if (event.target === event.currentTarget) closeRepository(); }}>
        <aside ref={repositoryPanelRef} id="repository-briefing" className="repository-briefing" role="dialog" aria-modal="true" aria-labelledby="repository-briefing-title">
          <header className="repository-heading">
            <div><p className="panel-kicker">REPOSITORY + SOURCE BRIEFING</p><h2 id="repository-briefing-title">Inspect KFM boundaries</h2><p>Current GitHub evidence and Drive-backed source ideas, translated without collapsing discovery into release.</p></div>
            <button className="icon-close" type="button" onClick={closeRepository} aria-label="Close repository briefing">×</button>
          </header>

          <section className="repository-snapshot" aria-label="Repository snapshot">
            <div className="snapshot-identity"><span>PINNED SNAPSHOT</span><strong>main@{REPOSITORY_SNAPSHOT.shortCommit}</strong><small>Inspected {REPOSITORY_SNAPSHOT.inspectedAt}</small></div>
            <dl>
              <div><dt>Domains</dt><dd>{REPOSITORY_SNAPSHOT.counts.knowledgeDomains}</dd></div>
              <div><dt>Feature families</dt><dd>{REPOSITORY_SNAPSHOT.counts.explorerFeatureFamilies}</dd></div>
              <div><dt>Map functions</dt><dd>{REPOSITORY_SNAPSHOT.counts.mapFunctions}</dd></div>
              <div><dt>Current signals</dt><dd>{REPOSITORY_SNAPSHOT.counts.repositoryUpdates}</dd></div>
            </dl>
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

              {sourceObservatoryView === "candidates" && <>
                <div className="repository-toolbar source-toolbar">
                  <label><span className="sr-only">Search source candidates</span><i aria-hidden="true">⌕</i><input type="search" value={sourceQuery} onChange={(event) => setSourceQuery(event.target.value)} placeholder="Search sources, organizations, roles, and gates" /></label>
                  <label><span className="sr-only">Filter source candidates by domain</span><select value={sourceDomain} onChange={(event) => setSourceDomain(event.target.value)}>{SOURCE_DOMAINS.map((domain) => <option key={domain} value={domain}>{domain === "ALL" ? "All domains" : domain}</option>)}</select></label>
                  <span>{filteredSourceCandidates.length} of {SOURCE_CANDIDATES.length} candidates</span>
                </div>
                <div className="source-candidate-grid">
                  {filteredSourceCandidates.map((source) => <article key={source.id} className="source-candidate-card">
                    <header><span>{source.domain}</span><strong>DISCOVERED · NO PUBLIC EFFECT</strong></header>
                    <h4>{source.title}</h4><p className="source-organization">{source.organization} · {source.cadence}</p>
                    <dl><div><dt>Source role</dt><dd>{source.sourceRole}</dd></div><div><dt>Candidate value</dt><dd>{source.value}</dd></div><div><dt>Cannot prove</dt><dd>{source.cannotProve}</dd></div><div><dt>Next gate</dt><dd>{source.nextGate}</dd></div></dl>
                    <div className="source-modes">{source.dataModes.map((mode) => <span key={mode}>{mode}</span>)}</div>
                    <footer><button type="button" onClick={() => copySourceIntakeDraft(source)}>Copy bounded intake draft</button>{source.layerId && source.featureId && <button type="button" onClick={() => { setRepositoryOpen(false); selectStoredFeature(source.layerId!, source.featureId!); }}>Inspect local analogue</button>}</footer>
                  </article>)}
                </div>
                {filteredSourceCandidates.length === 0 && <div className="repository-empty"><strong>No matching source candidates</strong><p>Clear the search or choose another domain.</p></div>}
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

      <main className="explorer-shell" data-left={leftOpen} data-right={rightOpen} data-timeline={timelineOpen}>
        <aside ref={leftPanelRef} className="layer-panel" aria-label="Explorer and Layer Catalog" aria-hidden={!leftOpen} inert={!leftOpen} aria-modal={isCompact && leftOpen || undefined} role={isCompact && leftOpen ? "dialog" : undefined}>
          <div className="panel-heading">
            <div><p className="panel-kicker">LAYER CATALOG</p><h1>Explore Kansas</h1></div>
            <button className="icon-close" type="button" onClick={closeLeftPanel} aria-label="Close Layer Catalog">×</button>
          </div>
          <p className="panel-intro">Choose synthetic and generalized demonstration layers for the map and your next report.</p>
          <label className="catalog-search"><span aria-hidden="true">⌕</span><span className="sr-only">Search Layer Catalog</span><input type="search" value={layerQuery} onChange={(event) => setLayerQuery(event.target.value)} placeholder="Filter layers and datasets" /></label>

          <section className="active-layers" aria-labelledby="active-title">
            <div className="section-row"><h2 id="active-title">Active layers <span>{visibleCount}</span></h2><button type="button" onClick={() => setVisibility(Object.fromEntries(LAYER_REGISTRY.map((layer) => [layer.id, layer.id === "kansas-extent"])))}>Clear</button></div>
            <div className="active-chips">{activeLayers.map((layer) => <button key={layer.id} type="button" onClick={() => zoomToLayer(layer)}>{layer.title}<span>↗</span></button>)}</div>
          </section>

          <div className="basemap-control">
            <div className="catalog-filter-grid"><label><span>Basemap style</span><select value={basemap} onChange={(event) => setBasemap(event.target.value as BasemapKey)}>{(Object.keys(BASEMAPS) as BasemapKey[]).map((key) => <option key={key} value={key}>{BASEMAPS[key].title} · {BASEMAPS[key].note}</option>)}</select></label><label><span>Domain filter</span><select value={layerDomain} onChange={(event) => setLayerDomain(event.target.value as (typeof layerDomains)[number])}>{layerDomains.map((domain) => <option key={domain} value={domain}>{domain === "ALL" ? "All domains" : domain}</option>)}</select></label></div>
          </div>

          <div className="catalog-groups">
            {CATEGORY_ORDER.map((category) => {
              const layers = layerOrder.map((id) => LAYER_REGISTRY.find((layer) => layer.id === id)).filter((layer): layer is LayerRecord => Boolean(layer && layer.category === category && filteredLayerIds.has(layer.id)));
              if (!layers.length) return null;
              return <section className="catalog-group" key={category}><h2>{category}</h2>{layers.map((layer) => {
                const noData = layer.temporal?.mode === "exact" && !layer.temporal.years.includes(year);
                const expanded = expandedLayers.has(layer.id);
                return <article className="layer-row" key={layer.id} data-active={visibility[layer.id]} data-state={sourceStates[layer.id]}>
                  <div className="layer-primary">
                    <label className="visibility-switch"><input type="checkbox" aria-label={`${visibility[layer.id] ? "Hide" : "Show"} ${layer.title}`} checked={visibility[layer.id]} onChange={(event) => setVisibility((current) => ({ ...current, [layer.id]: event.target.checked }))} /><span aria-hidden="true" /></label>
                    <i className={`legend-swatch ${layer.legend[0].shape}`} style={{ "--swatch": layer.legend[0].color } as React.CSSProperties} aria-hidden="true" />
                    <button className="layer-title" type="button" onClick={() => setExpandedLayers((current) => { const next = new Set(current); if (next.has(layer.id)) next.delete(layer.id); else next.add(layer.id); return next; })} aria-expanded={expanded}><strong>{layer.title}</strong><small>{noData ? `No ${layer.temporal?.label.toLowerCase()} data for ${formatTimelineStep(year)}` : `${layer.releaseState} · ${layer.releaseTime}`}</small></button>
                    <span className={`trust-badge state-${layer.releaseState.toLowerCase()}`}>{layer.releaseState}</span>
                  </div>
                  {expanded && <div className="layer-detail">
                    <p>{layer.description}</p>
                    <dl><div><dt>Format</dt><dd>{layer.sourceType}</dd></div><div><dt>Scale</dt><dd>{layer.scaleNote}</dd></div><div><dt>Time</dt><dd>{layer.validTimeExtent}</dd></div><div><dt>Freshness</dt><dd>{layer.freshnessState}</dd></div></dl>
                    <label className="opacity-control"><span>Opacity <b>{Math.round((opacity[layer.id] ?? layer.defaultOpacity) * 100)}%</b></span><input type="range" min="0" max="100" value={Math.round((opacity[layer.id] ?? layer.defaultOpacity) * 100)} onChange={(event) => setOpacity((current) => ({ ...current, [layer.id]: Number(event.target.value) / 100 }))} /></label>
                    <div className="layer-actions"><button type="button" onClick={() => zoomToLayer(layer)}>Zoom</button><button type="button" onClick={(event) => inspectLayer(layer, event.currentTarget)}>Features</button><button type="button" onClick={() => moveLayer(layer.id, -1)} aria-label={`Move ${layer.title} down in draw order`}>↓</button><button type="button" onClick={() => moveLayer(layer.id, 1)} aria-label={`Move ${layer.title} up in draw order`}>↑</button></div>
                    <p className="layer-note">{layer.sensitivityNote}</p>
                  </div>}
                </article>;
              })}</section>;
            })}
            {filteredLayerIds.size === 0 && <div className="catalog-empty"><strong>No layers found</strong><p>Try a domain, dataset, or geometry term.</p></div>}
          </div>

          <div className="panel-footer-actions"><button type="button" onClick={resetExplorer}>Reset map</button><button type="button" onClick={(event) => { setReportLayerIds(activeLayers.map((layer) => layer.id)); openMapUtility("report", event.currentTarget); }}>Report visible layers</button></div>
        </aside>

        <section className="map-stage" aria-label="Kansas renderer-neutral Explorer">
          <div className="mission-band map-command-bar">
            <span data-runtime={runtime.kind}><i /> RENDERER HOLD · NULL RUNTIME</span>
            <p>Synthetic and generalized catalog data only · <b>{visibleCount}</b> layers · <b>{formatTimelineStep(year)}</b> · <b>{selected ? selected.properties.title : "No selection"}</b></p>
            <div><SiteLayerLibrary
              layers={LAYER_REGISTRY} visibility={visibility} opacity={opacity} layerOrder={layerOrder}
              area={analysisArea} year={year} membershipEpoch={membershipEpoch}
              readState={requestedLayers.getSnapshot} onChange={requestedLayers.compareAndSet}
              onInspect={(id) => {
                const layer = LAYER_REGISTRY.find((candidate) => candidate.id === id);
                const returnElement = document.activeElement instanceof HTMLElement ? document.activeElement : mapContainerRef.current;
                if (layer && returnElement) inspectLayer(layer, returnElement);
              }}
            /><button type="button" onClick={saveCurrentWorkspace}>Save view</button><button type="button" onClick={(event) => openMapUtility("report", event.currentTarget)}>Build report</button></div>
          </div>
          <div id="map-canvas" ref={mapContainerRef} className="map-canvas" tabIndex={areaDrawMode ? -1 : 0} role="application" aria-label="Renderer-neutral Kansas Explorer shell. Use Map Workbench Inspect or the Layer Catalog to inspect catalog and evidence metadata; renderer interactions remain held." />
          {analysisAreaOverlay && !areaDrawMode && <div className="map-analysis-overlay" style={{ left: `${analysisAreaOverlay.left}%`, top: `${analysisAreaOverlay.top}%`, width: `${analysisAreaOverlay.width}%`, height: `${analysisAreaOverlay.height}%` }} aria-hidden="true"><span>REPORT AREA · {analysisAreaRecordCount}</span></div>}
          {areaDrawMode && <div
            className="map-query-surface"
            tabIndex={0}
            role="application"
            aria-label="Draw a rectangular report area. Drag across the map, or press Escape to cancel."
            onPointerDown={handleMapAreaPointerDown}
            onPointerMove={handleMapAreaPointerMove}
            onPointerUp={handleMapAreaPointerUp}
            onPointerCancel={() => cancelAreaDraw(false)}
            onKeyDown={(event) => { if (event.key === "Escape") { event.preventDefault(); event.stopPropagation(); cancelAreaDraw(); } }}
          >
            {areaDrawBox && <div className="map-area-draw-box" style={{ left: areaDrawBox.left, top: areaDrawBox.top, width: areaDrawBox.width, height: areaDrawBox.height }} aria-hidden="true" />}
          </div>}
          {areaDrawMode && <aside className="map-area-draw-hint" role="status"><div><span>SPATIAL QUERY</span><strong>Drag a report area</strong><small>North-up Mercator context · pixels are candidate scope, not evidence</small></div><button type="button" onClick={() => cancelAreaDraw()}>Cancel</button></aside>}

          {(runtime.kind === "loading" || runtime.kind === "error") && <div className={`runtime-overlay ${runtime.kind}`} role="status" aria-live="assertive"><span className="runtime-spinner" aria-hidden="true" /><strong>{runtime.kind === "loading" ? "Preparing spatial explorer" : "Map runtime unavailable"}</strong><p>{runtime.message}</p>{runtime.kind === "error" && <button type="button" onClick={() => window.location.reload()}>Reload map</button>}</div>}
          {runtime.kind === "degraded" && <div className="runtime-degraded-banner" role="status" aria-live="polite"><strong>Partial map degradation</strong><span>{runtime.message}</span></div>}
          {temporalNoData.length > 0 && <div className="no-time-data" role="status"><strong>No {formatTimelineStep(year)} observation in {temporalNoData.map((layer) => layer.title).join(", ")}</strong><span>Other active layers remain visible; choose an available tick in the timeline.</span></div>}

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
            <button type="button" onClick={() => updateRendererNeutralView({ zoom: Math.min(16, view.zoom + 1) })} aria-label="Zoom in" data-tooltip="Zoom in">+</button>
            <button type="button" onClick={() => updateRendererNeutralView({ zoom: Math.max(4, view.zoom - 1) })} aria-label="Zoom out" data-tooltip="Zoom out">−</button>
            <button className="mobile-hidden-control" type="button" onClick={() => updateRendererNeutralView({ bearing: 0, pitch: 0 })} aria-label="Reset compass and pitch" data-tooltip="Reset north">N</button>
            <button type="button" onClick={fitKansasView} aria-label="Reset view to Kansas" data-tooltip="Kansas extent">KS</button>
            <button className="map-rail-divider" type="button" onClick={(event) => mapUtilityOpen && mapUtilityView === "scene" ? closeMapUtility() : openMapUtility("scene", event.currentTarget)} aria-expanded={mapUtilityOpen && mapUtilityView === "scene"} aria-controls="map-utility-panel" aria-label="Open scene and tile lab" data-tooltip="Scene + tiles">3D</button>
            <button ref={mapUtilityButtonRef} className="map-report-tool" type="button" onClick={(event) => mapUtilityOpen && mapUtilityView === "report" ? closeMapUtility() : openMapUtility("report", event.currentTarget)} aria-expanded={mapUtilityOpen && mapUtilityView === "report"} aria-controls="map-utility-panel" aria-label="Build a custom report" data-tooltip="Build report">R</button>
            <button type="button" onClick={() => setToolsExpanded((current) => !current)} aria-expanded={toolsExpanded} aria-controls="more-map-tools" aria-label="More map tools" data-tooltip="More tools">•••</button>
            {toolsExpanded && <div className="secondary-tools" id="more-map-tools">
              <button type="button" onClick={(event) => openMapUtility("navigate", event.currentTarget)}><span>⌖</span>Map controls</button>
              <button type="button" onClick={(event) => openMapUtility("connections", event.currentTarget)}><span>⛓</span>Source connections</button>
              <button type="button" onClick={(event) => openMapUtility("import", event.currentTarget)}><span>⇧</span>Import preview</button>
              <button type="button" onClick={startAreaDraw} disabled={locationCameraRedacted}><span>▣</span>{analysisArea ? "Redraw report area" : "Draw report area"}</button>
              <button type="button" onClick={locateUser}><span>⌾</span>My location</button>
              <button type="button" onClick={toggleFullscreen} aria-label="Toggle fullscreen"><span>⛶</span>Fullscreen</button>
              <button type="button" aria-pressed={projection === "globe"} onClick={() => setProjection((current) => current === "globe" ? "mercator" : "globe")}><span>◎</span>{projection === "globe" ? "2D view" : "Globe"}</button>
              <button type="button" aria-pressed={measureMode === "distance"} onClick={() => toggleMeasure("distance")}><span>↔</span>Distance</button>
              <button type="button" aria-pressed={measureMode === "area"} onClick={() => toggleMeasure("area")}><span>◇</span>Area</button>
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
              <div><p className="panel-kicker">MAP WORKBENCH</p><h2 id="map-utility-title">{mapUtilityView === "report" ? "Custom report builder" : mapUtilityView === "scene" ? "Scene + 3D lab" : mapUtilityView === "connections" ? "Source connections" : mapUtilityView === "import" ? "Local import preview" : "Map tools"}</h2><span>{mapUtilityView === "report" ? "Turn the current map, time, layers, and selected data into a usable report." : mapUtilityView === "connections" ? "Inspect the held relationship between the layer registry, renderer descriptors, and site-local records." : mapUtilityView === "import" ? "Inspect KML or GeoJSON locally while admission, renderer, report, export, and publication effects remain at none." : "Inspect, navigate, explore scene intent, compare, display, measure, export, and diagnose the renderer-neutral map state."}</span></div>
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

                    <section className="report-map-query" data-active={Boolean(analysisArea)} aria-labelledby="report-map-query-title">
                      <header><div><span>QUERY FROM MAP</span><strong id="report-map-query-title">Spatial report area</strong></div><b>{analysisArea ? "READY" : "NOT SET"}</b></header>
                      <p>Draw a rectangle on the map to turn a visual extent into a bounded catalog query. Candidate records still pass time, layer, evidence-state, and text filters before entering the report.</p>
                      {analysisArea && <dl><div><dt>West / east</dt><dd>{analysisArea.west.toFixed(4)}° / {analysisArea.east.toFixed(4)}°</dd></div><div><dt>South / north</dt><dd>{analysisArea.south.toFixed(4)}° / {analysisArea.north.toFixed(4)}°</dd></div><div><dt>Catalog candidates</dt><dd>{analysisAreaRecordCount}</dd></div><div><dt>Filtered report</dt><dd>{reportScope === "ANALYSIS_AREA" ? `${reportRecords.length} records` : "Scope available"}</dd></div></dl>}
                      <div><button type="button" onClick={startAreaDraw} disabled={locationCameraRedacted}>{analysisArea ? "Redraw on map" : "Draw on map"}</button><button type="button" onClick={captureAnalysisArea} disabled={locationCameraRedacted}>Use viewport</button><button type="button" onClick={fitAnalysisArea} disabled={!analysisArea}>Fit area</button>{analysisArea && <button type="button" onClick={clearAnalysisArea}>Clear</button>}</div>
                      <footer><span>FOCUS_POINT_INSIDE_BOUNDS</span><small>Context only · renderer hits are not evidence</small></footer>
                    </section>

                    <fieldset className="report-control-group"><legend>Detail level</legend><div className="report-detail-grid">
                      {(["EXECUTIVE", "STANDARD", "TECHNICAL"] as ReportDetail[]).map((detail) => <button key={detail} type="button" aria-pressed={reportDetail === detail} onClick={() => setReportDetail(detail)}>{detail === "EXECUTIVE" ? "Brief" : detail === "STANDARD" ? "Standard" : "Full detail"}</button>)}
                    </div></fieldset>

                    <fieldset className="report-control-group"><legend>Report sections</legend><div className="report-section-list">
                      {REPORT_SECTIONS.map((section) => <label key={section.id}><input type="checkbox" checked={reportSections[section.id]} onChange={(event) => setReportSections((current) => ({ ...current, [section.id]: event.target.checked }))} /><span><strong>{section.label}</strong><small>{section.detail}</small></span></label>)}
                    </div></fieldset>

                    <fieldset className="report-control-group"><legend>Included layers</legend>
                      <div className="report-layer-actions"><button type="button" onClick={() => setReportLayerIds(activeLayers.map((layer) => layer.id))}>Use visible</button><button type="button" onClick={() => setReportLayerIds(LAYER_REGISTRY.map((layer) => layer.id))}>Select all</button><button type="button" onClick={() => setReportLayerIds([])}>Clear</button></div>
                      <div className="report-layer-list">{LAYER_REGISTRY.map((layer) => {
                        const compatibleCount = layer.data.features.filter((feature) => isFeatureAvailableAtTime(layer, feature.properties.year, year)).length;
                        return <label key={layer.id} data-visible={visibility[layer.id]}><input type="checkbox" checked={reportLayerIds.includes(layer.id)} onChange={(event) => setReportLayerIds((current) => event.target.checked ? [...new Set([...current, layer.id])] : current.filter((id) => id !== layer.id))} /><span><strong>{layer.title}</strong><small>{layer.domain} · {compatibleCount} time-compatible · {visibility[layer.id] ? "visible" : "hidden"}</small></span></label>;
                      })}</div>
                    </fieldset>

                    <fieldset className="report-control-group saved-workspace-control"><legend>Saved workspaces</legend>
                      <div className="workspace-save-row"><input type="text" value={workspaceName} maxLength={50} onChange={(event) => setWorkspaceName(event.target.value)} placeholder="Optional workspace name" /><button type="button" onClick={saveCurrentWorkspace}>Save current</button></div>
                      <p>Stores camera, active time, Time A / Time B comparison, layers, opacity, selection, and report settings only on this device.</p>
                      <div className="saved-workspace-list">{savedWorkspaces.map((snapshot) => <article key={snapshot.id}><button type="button" onClick={() => loadSavedWorkspace(snapshot)}><strong>{snapshot.name}</strong><small>{new Date(snapshot.savedAt).toLocaleString()} · {snapshot.report?.layerIds?.length ?? 0} report layers</small></button><button type="button" onClick={() => deleteSavedWorkspace(snapshot)} aria-label={`Delete ${snapshot.name}`}>×</button></article>)}{savedWorkspaces.length === 0 && <div><strong>No saved workspaces</strong><small>Save the current analysis setup to return to it later on this device.</small></div>}</div>
                    </fieldset>
                  </div>

                  <article className="report-preview" aria-live="polite">
                    <header><div><span>LIVE REPORT PREVIEW</span><h4>{reportTitle.trim() || "Kansas map data report"}</h4><p>{reportScope.replaceAll("_", " ")} · {formatTimelineStep(year)} · {reportDetail}</p></div><strong>{reportIncludedRecordCount} INCLUDED RECORD{reportIncludedRecordCount === 1 ? "" : "S"}</strong></header>
                    {(reportQuery || reportEvidenceFilter !== "ALL") && <div className="report-active-filters"><span>ACTIVE FILTERS</span>{reportQuery && <b>Search: {reportQuery}</b>}{reportEvidenceFilter !== "ALL" && <b>{reportEvidenceFilter.replaceAll("_", " ")}</b>}<button type="button" onClick={() => { setReportQuery(""); setReportEvidenceFilter("ALL"); }}>Clear</button></div>}
                    {reportSections.summary && <div className="report-metrics" aria-label="Report summary metrics"><article><span>Active-time matches</span><strong>{reportActiveTimeRecordCount}</strong></article><article><span>Layers</span><strong>{reportLayerSummary.length}</strong></article><article><span>States</span><strong>{Object.keys(reportEvidenceCounts).length}</strong></article><article><span>Retained selections</span><strong>{reportRetainedSelectionCount}</strong></article></div>}
                    {reportSections.findings && <section className="report-preview-section"><span>FINDINGS</span><ol>{reportFindings.map((finding) => <li key={finding}>{finding}</li>)}</ol></section>}
                    {reportSections.findings && <section className="report-preview-section report-temporal-comparison"><span>TIME A / TIME B</span><div><article><strong>{formatTimelineStep(compareTimeA)}</strong><small>{reportTemporalComparison.timeARecordCount} compatible records</small></article><i aria-hidden="true">→</i><article><strong>{formatTimelineStep(compareTimeB)}</strong><small>{reportTemporalComparison.timeBRecordCount} compatible records</small></article><b>{reportTemporalComparison.recordDelta > 0 ? "+" : ""}{reportTemporalComparison.recordDelta} catalog delta</b></div><p>{reportTemporalComparison.changedLayerCount} included layer{reportTemporalComparison.changedLayerCount === 1 ? "" : "s"} have entered or exited fixture IDs. This is catalog availability, not an observed-change claim.</p></section>}
                    {reportSections.records && <section className="report-preview-section"><span>RECORDS</span><div className="report-record-table" role="table" aria-label="Included report records">
                      {reportRecords.slice(0, reportRecordLimit).map(({ layer, properties, outsideActiveTime }) => <article key={`${layer.id}:${properties.fid}`} role="row"><div><strong>{properties.title}</strong><small>{layer.title} · {properties.year}{outsideActiveTime ? ` · RETAINED OUTSIDE ${formatTimelineStep(year)}` : ""}</small></div><span data-state={properties.evidenceState}>{properties.evidenceState}</span><p>{properties.summary}</p></article>)}
                      {reportRecords.length === 0 && <div className="report-empty"><strong>No records match</strong><p>Move or widen the map, change time, choose another scope, or include more layers.</p></div>}
                    </div></section>}
                    {reportSections.evidence && reportRecords.length > 0 && <section className="report-preview-section"><span>EVIDENCE DISTRIBUTION</span><div className="report-evidence-grid">{Object.entries(reportEvidenceCounts).sort((left, right) => right[1] - left[1]).map(([state, count]) => <article key={state}><strong>{count}</strong><span>{state}</span></article>)}</div></section>}
                    {reportSections.limitations && <aside className="report-boundary"><strong>Use boundary</strong><p>Site-local synthetic and generalized demonstration data only. The generated report preserves limitations and cannot release, publish, admit, or authorize KFM data.</p></aside>}
                    <footer><span>Updated {reportGeneratedAt}</span><div><button type="button" onClick={() => void copyCustomReport()} disabled={!reportLayerIds.length}>Copy</button><button type="button" onClick={() => downloadCustomReport("json")} disabled={!reportLayerIds.length}>Data .json</button><button className="report-download-primary" type="button" onClick={() => downloadCustomReport("html")} disabled={!reportLayerIds.length}>Report .html</button></div></footer>
                  </article>
                </div>
              </section>}

              {mapUtilityView === "navigate" && <section id="map-utility-view-navigate" role="tabpanel" aria-labelledby="map-utility-tab-navigate" className="map-utility-section">
                <div className="map-utility-section-heading"><span>NAVIGATE</span><h3>Camera, coordinates + private location</h3><p>Renderer-neutral camera state changes only this browser shell. It never acquires a renderer or changes evidence, policy, review, release, or publication state.</p></div>
                <dl className="map-camera-facts">
                  <div><dt>Center</dt><dd>{locationCameraRedacted ? "Private camera · redacted" : `${formatCoordinate(view.center[1], "N", "S")} · ${formatCoordinate(view.center[0], "E", "W")}`}</dd></div>
                  <div><dt>Zoom</dt><dd>{view.zoom.toFixed(2)}</dd></div>
                  <div><dt>Bearing / pitch</dt><dd>{Math.round(view.bearing)}° / {Math.round(view.pitch)}°</dd></div>
                  <div><dt>Projection</dt><dd>{projection}</dd></div>
                </dl>
                <div className="map-utility-actions map-navigation-actions">
                  <button type="button" onClick={() => travelCameraHistory(-1)} disabled={cameraHistoryIndex === 0}>Previous view</button>
                  <button type="button" onClick={() => travelCameraHistory(1)} disabled={cameraHistoryIndex >= cameraHistoryLength - 1}>Next view</button>
                  <button type="button" onClick={() => updateRendererNeutralView({ zoom: Math.min(16, view.zoom + 1) })}>Zoom in</button>
                  <button type="button" onClick={() => updateRendererNeutralView({ zoom: Math.max(4, view.zoom - 1) })}>Zoom out</button>
                  <button type="button" onClick={() => updateRendererNeutralView({ bearing: 0, pitch: 0 })}>Reset north</button>
                  <button type="button" onClick={fitKansasView}>Fit Kansas</button>
                  <button type="button" onClick={toggleFullscreen}>Fullscreen</button>
                  <button type="button" onClick={locateUser}>Use my location</button>
                  <button type="button" onClick={() => void copyMapCenter()} disabled={locationCameraRedacted}>Copy center</button>
                </div>
                <section className="analysis-area-card" data-active={Boolean(analysisArea)} aria-labelledby="analysis-area-title">
                  <header><div><span>RENDERER-NEUTRAL VIEW ANALYSIS</span><h4 id="analysis-area-title">Area of interest</h4></div><strong>{analysisArea ? "LOCKED" : "NOT SET"}</strong></header>
                  {analysisArea
                    ? <><dl><div><dt>West / east</dt><dd>{analysisArea.west.toFixed(4)}° / {analysisArea.east.toFixed(4)}°</dd></div><div><dt>South / north</dt><dd>{analysisArea.south.toFixed(4)}° / {analysisArea.north.toFixed(4)}°</dd></div><div><dt>Compatible records</dt><dd>{analysisAreaRecordCount}</dd></div><div><dt>Report scope</dt><dd>{reportScope === "ANALYSIS_AREA" ? "ACTIVE" : "AVAILABLE"}</dd></div></dl><div><button type="button" onClick={captureAnalysisArea}>Update from viewport</button><button type="button" onClick={fitAnalysisArea}>Fit area</button><button type="button" onClick={() => { setReportScope("ANALYSIS_AREA"); setReportGeneratedAt(new Date().toISOString()); openMapUtility("report"); }}>Build area report</button><button type="button" onClick={clearAnalysisArea}>Clear</button></div></>
                    : <><p>Lock the current viewport as a stable rectangular analysis area. You can pan elsewhere while reports continue using the locked extent.</p><button type="button" onClick={captureAnalysisArea} disabled={locationCameraRedacted}>Lock current viewport</button></>}
                  <footer>Site-local fixture query only · viewport geometry is context, not evidence</footer>
                </section>
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
                  <label><span><strong>Bearing</strong><output>{Math.round(view.bearing)}°</output></span><input type="range" min="-180" max="180" step="1" value={Math.round(view.bearing)} onChange={(event) => updateRendererNeutralView({ bearing: Number(event.target.value) })} /></label>
                  <label><span><strong>Pitch</strong><output>{Math.round(view.pitch)}°</output></span><input type="range" min="0" max="60" step="1" value={Math.round(view.pitch)} onChange={(event) => updateRendererNeutralView({ pitch: Number(event.target.value) })} /></label>
                </div>
                <div className="map-control-group"><header><strong>Gesture mode</strong><span>One unified map control system</span></header><div className="map-segmented-control"><button type="button" aria-pressed={gestureMode === "cooperative"} onClick={() => setMapGestureMode("cooperative")}>Cooperative</button><button type="button" aria-pressed={gestureMode === "direct"} onClick={() => setMapGestureMode("direct")}>Direct</button></div><p className="map-control-note">Cooperative mode requires a modifier key for wheel zoom and two fingers for touch pan, reducing accidental page trapping. Direct mode gives the map immediate gesture control.</p></div>
                <aside className="map-utility-boundary" data-tone="privacy"><strong>Location privacy</strong><p>Browser location is used only to move the local camera. While that camera remains location-derived, shared URLs use generalized Kansas defaults plus a redaction marker, receipts and exports use withheld markers, and diagnostics omit coordinates. Fit Kansas clears the private camera.</p></aside>
                <aside className="map-utility-boundary"><strong>Keyboard alternative</strong><p>Use Inspect for a searchable feature list, Layer Catalog for visibility and opacity, and these controls for camera actions without relying on pointer gestures.</p></aside>
              </section>}

              {mapUtilityView === "inspect" && <section id="map-utility-view-inspect" role="tabpanel" aria-labelledby="map-utility-tab-inspect" className="map-utility-section">
                <div className="map-utility-section-heading"><span>INSPECT</span><h3>Feature index + context receipt</h3><p>Hover is a preview only. A click or explicit Inspect action commits one stable registry feature before the Evidence Drawer opens.</p></div>
                <article className="map-utility-card map-context-card">
                  <header><span>MAP CONTEXT</span><strong>{selected?.properties.title ?? "No committed selection"}</strong></header>
                  <dl><div><dt>Active time</dt><dd>{formatTimelineStep(year)}</dd></div><div><dt>Visible layers</dt><dd>{visibleCount}</dd></div><div><dt>Selection</dt><dd>{selected ? selected.properties.evidenceState : "NONE"}</dd></div><div><dt>Halo</dt><dd>{selectedLayerHidden ? "HIDDEN LAYER" : selectedTimeMismatch ? "OUTSIDE TIME" : selected ? "VISIBLE" : "NONE"}</dd></div></dl>
                  <button type="button" onClick={() => void copyMapContextReceipt()}>Copy 15-minute map context receipt</button>
                </article>

                {mapQueryCandidates.length > 1 && <section className="map-overlap-chooser" aria-labelledby="overlap-title">
                  <div><span>OVERLAP CHOOSER</span><h4 id="overlap-title">{mapQueryCandidates.length} catalog features share this context</h4><p>Choose one explicitly; the shell will not silently prefer descriptor order.</p></div>
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
                <div className="map-feature-count"><span>{mapFeatureIndex.length} compatible feature{mapFeatureIndex.length === 1 ? "" : "s"}</span><small>Active time {formatTimelineStep(year)} · untimed, exact, and through-time semantics applied</small></div>
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
            <Link href="/about">About</Link>
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
