"use client";

import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import type { Feature, Geometry } from "geojson";
import type { GeoJSONSource, Map as MapLibreMap, Popup, ScaleControl } from "maplibre-gl";
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
  applyRegistryState,
  areaSquareMiles,
  BASEMAPS,
  buildMeasurementData,
  distanceMiles,
  reorderRegistryLayers,
  updateMeasurementSource,
  updateSelectionSource,
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

type ViewState = { center: [number, number]; zoom: number; bearing: number; pitch: number };
type MapBoundsState = { west: number; south: number; east: number; north: number };
type RuntimeState = { kind: "loading" | "ready" | "degraded" | "error"; message: string };
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
type MeasureMode = "distance" | "area" | null;
type RepositoryView = "updates" | "functions" | "runtime" | "transitions" | "readiness" | "sources";
type SourceObservatoryView = "candidates" | "corpus" | "gaps";
type GovernedRoute = "/bootstrap" | "/layers" | "/evidence" | "/focus";
type GovernedMethod = "GET" | "POST";
type PublicWorkspaceId = "explore" | "knowledge" | "features" | "trust";
type MapQueryCandidate = Readonly<{
  featureId: string;
  layerId: string;
  title: string;
  layerTitle: string;
  evidenceState: EvidenceState;
  sourceYear: number;
}>;

type SelectedContext = {
  featureId: string;
  layerId: string;
  layer: LayerRecord;
  properties: FeatureProperties;
  geometry: Feature<Geometry>;
};

const KANSAS_VIEW: ViewState = { center: [-98.38, 38.48], zoom: 5.45, bearing: 0, pitch: 0 };
const EXPECTED_MAPLIBRE_VERSION = "6.6.0";
const MAPLIBRE_WORKER_URL = "/maplibre/maplibre-gl-worker.mjs";
const MAPLIBRE_RUNTIME_ASSET_URLS = [MAPLIBRE_WORKER_URL, "/maplibre/maplibre-gl-shared.mjs"] as const;
const SUPPORTED_CONTEXT_BOUNDS = Object.freeze({ west: -104.8, south: 34.8, east: -92, north: 42.2 });
const defaultVisibility = Object.fromEntries(LAYER_REGISTRY.map((layer) => [layer.id, layer.defaultVisibility]));
const defaultOpacity = Object.fromEntries(LAYER_REGISTRY.map((layer) => [layer.id, layer.defaultOpacity]));
const defaultOrder = LAYER_REGISTRY.map((layer) => layer.id);
const interactiveLayerIds = LAYER_REGISTRY.flatMap((layer) => layer.renderers.filter((renderer) => renderer.interactive).map((renderer) => renderer.id));
const layerDomains = ["ALL", ...Array.from(new Set(LAYER_REGISTRY.map((layer) => layer.domain))).sort()] as const;
const drawerViews = ["evidence", "metadata", "lineage", "focus"] as const satisfies readonly DrawerView[];
const mapUtilityViews = ["navigate", "inspect", "compare", "display", "measure", "export", "diagnostics"] as const satisfies readonly MapUtilityView[];
const mapUtilityLabels: Record<MapUtilityView, string> = {
  navigate: "Navigate",
  inspect: "Inspect",
  compare: "Compare",
  display: "Display",
  measure: "Measure",
  export: "Export",
  diagnostics: "Diagnostics",
};
const governedRoutes = new Set<GovernedRoute>(["/bootstrap", "/layers", "/evidence"]);

const loadConfiguredMapLibre = async () => {
  await Promise.all(MAPLIBRE_RUNTIME_ASSET_URLS.map(async (url) => {
    const response = await fetch(url, { cache: "no-store" });
    if (!response.ok) throw new Error(`MapLibre runtime asset unavailable (${response.status})`);
    await response.body?.cancel();
  }));
  const maplibregl = await import("maplibre-gl");
  maplibregl.setWorkerUrl(MAPLIBRE_WORKER_URL);
  const version = maplibregl.getVersion();
  if (version !== EXPECTED_MAPLIBRE_VERSION) throw new Error(`Expected MapLibre ${EXPECTED_MAPLIBRE_VERSION}, received ${version}`);
  if (maplibregl.getWorkerUrl() !== MAPLIBRE_WORKER_URL) throw new Error("MapLibre worker configuration did not persist");
  return { maplibregl, version };
};
const publicWorkspaces: readonly Readonly<{
  id: PublicWorkspaceId;
  label: string;
  shortLabel: string;
  summary: string;
  capability: string;
}>[] = Object.freeze([
  Object.freeze({ id: "explore", label: "Explore", shortLabel: "Map", summary: "Map, time, layers, selection, and bounded Focus context.", capability: "PUBLIC · ACTIVE" }),
  Object.freeze({ id: "knowledge", label: "Knowledge", shortLabel: "Layers", summary: "Browse the public-safe Kansas knowledge domains and catalog.", capability: "PUBLIC · ACTIVE" }),
  Object.freeze({ id: "features", label: "Features", shortLabel: "Inventory", summary: "Inspect repository-grounded feature maturity and lifecycle gates.", capability: "PUBLIC · READ ONLY" }),
  Object.freeze({ id: "trust", label: "Trust", shortLabel: "Evidence", summary: "Inspect evidence, limitations, denials, corrections, and transitions.", capability: "PUBLIC · READ ONLY" }),
]);

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

const motionDuration = (duration: number) => window.matchMedia("(prefers-reduced-motion: reduce)").matches ? 0 : duration;

const measurementLabelFor = (mode: Exclude<MeasureMode, null>, coordinates: [number, number][], unit: MeasureUnit) => {
  if (mode === "distance") {
    if (coordinates.length < 2) return "Add another point";
    const miles = distanceMiles(coordinates);
    return unit === "metric" ? `${(miles * 1.609344).toFixed(1)} km approximate` : `${miles.toFixed(1)} mi approximate`;
  }
  if (coordinates.length < 3) return `Add ${3 - coordinates.length} more point${coordinates.length === 2 ? "" : "s"}`;
  const squareMiles = areaSquareMiles(coordinates);
  return unit === "metric" ? `${(squareMiles * 2.58999).toFixed(1)} km² approximate` : `${squareMiles.toFixed(1)} sq mi approximate`;
};

export default function Home() {
  const mapContainerRef = useRef<HTMLDivElement>(null);
  const mapRef = useRef<MapLibreMap | null>(null);
  const popupRef = useRef<Popup | null>(null);
  const scaleControlRef = useRef<ScaleControl | null>(null);
  const hoveredRef = useRef<{ source: string; id: string | number } | null>(null);
  const pointerFrameRef = useRef<number | null>(null);
  const pendingPointerRef = useRef<[number, number]>(KANSAS_VIEW.center);
  const visibilityRef = useRef(defaultVisibility);
  const opacityRef = useRef(defaultOpacity);
  const orderRef = useRef(defaultOrder);
  const yearRef = useRef<number>(2026);
  const basemapRef = useRef<BasemapKey>("midnight");
  const projectionRef = useRef<"mercator" | "globe">("mercator");
  const selectedRef = useRef<SelectedContext | null>(null);
  const measureModeRef = useRef<MeasureMode>(null);
  const measurementGeometryModeRef = useRef<MeasureMode>(null);
  const measureUnitRef = useRef<MeasureUnit>("imperial");
  const measureCoordinatesRef = useRef<[number, number][]>([]);
  const returnFocusRef = useRef<HTMLElement | null>(null);
  const leftPanelRef = useRef<HTMLElement>(null);
  const rightPanelRef = useRef<HTMLElement>(null);
  const timelineRef = useRef<HTMLElement>(null);
  const repositoryButtonRef = useRef<HTMLButtonElement>(null);
  const repositoryPanelRef = useRef<HTMLElement>(null);
  const workspaceDetailsRef = useRef<HTMLDetailsElement>(null);
  const mapUtilityButtonRef = useRef<HTMLButtonElement>(null);
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
  const [layerOrder, setLayerOrder] = useState<string[]>(defaultOrder);
  const [basemap, setBasemap] = useState<BasemapKey>("midnight");
  const [view, setView] = useState<ViewState>(KANSAS_VIEW);
  const [pointer, setPointer] = useState<[number, number]>(KANSAS_VIEW.center);
  const [mapViewportBounds, setMapViewportBounds] = useState<MapBoundsState>(SUPPORTED_CONTEXT_BOUNDS);
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
  const [locationCameraRedacted, setLocationCameraRedacted] = useState(false);
  const [selected, setSelected] = useState<SelectedContext | null>(null);
  const [leftOpen, setLeftOpen] = useState(true);
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
  const [mapQueryCandidates, setMapQueryCandidates] = useState<readonly MapQueryCandidate[]>([]);
  const [inspectViewportOnly, setInspectViewportOnly] = useState(false);
  const [inspectVisibleLayersOnly, setInspectVisibleLayersOnly] = useState(false);
  const [compareLeftId, setCompareLeftId] = useState("water-context");
  const [compareRightId, setCompareRightId] = useState("atmosphere-observations");
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
  const [runtimeSeamState, setRuntimeSeamState] = useState<RuntimeSeamState>("IDLE");
  const [runtimeSeamReason, setRuntimeSeamReason] = useState("Awaiting deterministic replay");
  const [toast, setToast] = useState("");
  const [isCompact, setIsCompact] = useState(false);
  const [sourceStates, setSourceStates] = useState<Record<string, "loading" | "ready" | "error">>(
    Object.fromEntries(LAYER_REGISTRY.map((layer) => [layer.id, "loading"])),
  );

  const debouncedGlobalQuery = useDebounced(globalQuery, 140);
  const debouncedLayerQuery = useDebounced(layerQuery, 140);

  useEffect(() => { visibilityRef.current = visibility; }, [visibility]);
  useEffect(() => { opacityRef.current = opacity; }, [opacity]);
  useEffect(() => { orderRef.current = layerOrder; }, [layerOrder]);
  useEffect(() => { yearRef.current = year; }, [year]);
  useEffect(() => { basemapRef.current = basemap; }, [basemap]);
  useEffect(() => { projectionRef.current = projection; }, [projection]);

  const dismissGuidedStart = useCallback(() => {
    setGuidedStartOpen(false);
    try { window.localStorage.setItem(GUIDED_START_STORAGE_KEY, "1"); } catch { /* Device storage is optional. */ }
  }, []);

  const showGuidedStart = useCallback(() => {
    setHelpOpen(false);
    setGuidedStartOpen(true);
    try { window.localStorage.removeItem(GUIDED_START_STORAGE_KEY); } catch { /* Device storage is optional. */ }
  }, []);

  useEffect(() => {
    const hasSharedFeature = new URLSearchParams(window.location.search).has("f");
    let dismissed = false;
    try { dismissed = window.localStorage.getItem(GUIDED_START_STORAGE_KEY) === "1"; } catch { /* Device storage is optional. */ }
    const openGuide = window.setTimeout(() => setGuidedStartOpen(!hasSharedFeature && !dismissed), 0);
    return () => window.clearTimeout(openGuide);
  }, []);
  useEffect(() => { selectedRef.current = selected; }, [selected]);
  useEffect(() => { measureModeRef.current = measureMode; }, [measureMode]);
  useEffect(() => { measurementGeometryModeRef.current = measurementGeometryMode; }, [measurementGeometryMode]);
  useEffect(() => { measureUnitRef.current = measureUnit; }, [measureUnit]);

  const activeLayers = useMemo(() => LAYER_REGISTRY.filter((layer) => visibility[layer.id]), [visibility]);
  const visibleCount = activeLayers.length;
  const temporalNoData = useMemo(() => activeLayers.filter((layer) => layer.temporal?.mode === "exact" && !layer.temporal.years.includes(year)), [activeLayers, year]);
  const availabilityByStep = useMemo(() => Object.fromEntries(TIME_STEPS.map((step) => [step, activeLayers.filter((layer) => isLayerAvailableAtTime(layer, step)).length])), [activeLayers]);
  const sourceStateCounts = useMemo(() => ({
    ready: Object.values(sourceStates).filter((state) => state === "ready").length,
    loading: Object.values(sourceStates).filter((state) => state === "loading").length,
    error: Object.values(sourceStates).filter((state) => state === "error").length,
  }), [sourceStates]);
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
        label: "Admitted local sources",
        detail: `${maplibreProbe.sourcesReady}/${LAYER_REGISTRY.length} GeoJSON sources · ${maplibreProbe.idle ? "idle" : "working"} · ${maplibreProbe.tilesLoaded ? "tiles settled" : "tiles pending"}`,
        state: state(maplibreProbe.sourcesReady === LAYER_REGISTRY.length && maplibreProbe.idle && maplibreProbe.tilesLoaded, startupFailed || sourceStateCounts.error > 0),
      },
      {
        id: "interaction",
        label: "Controls + interactions",
        detail: "Scale, pan, zoom, keyboard, hover, selection, cluster expansion, and measurement handlers",
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
    params.set("order", layerOrder.join(","));
    params.set("units", measureUnit);
    params.set("ws", currentWorkspace);
    if (mapUtilityOpen) {
      params.set("mapui", "open");
      params.set("maptab", mapUtilityView);
    }
    if (mapUtilityView === "compare") params.set("compare", `${compareLeft.id},${compareRight.id}`);
    if (selected) {
      params.set("f", selected.featureId);
      params.set("panel", drawerView);
      params.set("drawer", rightOpen ? "open" : "closed");
      params.set("focusStage", focusStage);
      params.set("focusIntent", focusIntent);
    }
    return params;
  }, [activeLayers, basemap, compareLeft.id, compareRight.id, currentWorkspace, drawerView, focusIntent, focusStage, layerOrder, locationCameraRedacted, mapUtilityOpen, mapUtilityView, measureUnit, opacity, projection, rightOpen, selected, view, year]);

  const announce = useCallback((message: string) => {
    setToast(message);
    window.setTimeout(() => setToast(""), 3600);
  }, []);

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
  }, [activateDrawerView, announce, selected]);

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
    mapRef.current?.easeTo({ center: focus, zoom: Math.max(mapRef.current.getZoom(), 7), duration: window.matchMedia("(prefers-reduced-motion: reduce)").matches ? 0 : 700 });
    if (mapRef.current?.isStyleLoaded()) {
      const mismatch = isFeatureTimeMismatch(context.layer.temporal, context.properties.year, yearRef.current);
      updateSelectionSource(mapRef.current, mismatch ? null : context.geometry);
    }
  }, [openSelection]);

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
      mapRef.current?.jumpTo(restoredView);

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
        .map(([id, value]) => [id, clamp(Number(value), 0.1, 1)]));
      const nextOpacity = { ...defaultOpacity, ...restoredOpacity };
      opacityRef.current = nextOpacity;
      setOpacity(nextOpacity);
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
      const restoredMeasureUnit: MeasureUnit = params.get("units") === "metric" ? "metric" : "imperial";
      measureUnitRef.current = restoredMeasureUnit;
      setMeasureUnit(restoredMeasureUnit);
      const restoredWorkspace = params.get("ws");
      setCurrentWorkspace(restoredWorkspace === "knowledge" || restoredWorkspace === "features" || restoredWorkspace === "trust" ? restoredWorkspace : "explore");
      const restoredMapUtilityView = params.get("maptab");
      const nextMapUtilityView: MapUtilityView = restoredMapUtilityView === "inspect" || restoredMapUtilityView === "compare" || restoredMapUtilityView === "display" || restoredMapUtilityView === "measure" || restoredMapUtilityView === "export" || restoredMapUtilityView === "diagnostics" ? restoredMapUtilityView : "navigate";
      setMapUtilityView(nextMapUtilityView);
      const restoredCompareIds = params.get("compare")?.split(",") ?? [];
      if (restoredCompareIds.length === 2 && restoredCompareIds.every((id) => knownLayerIds.has(id)) && restoredCompareIds[0] !== restoredCompareIds[1]) {
        setCompareLeftId(restoredCompareIds[0]);
        setCompareRightId(restoredCompareIds[1]);
      }
      if (nextMapUtilityView === "export") setExportGeneratedAt(new Date().toISOString());
      const restoredMapUtilityOpen = params.get("mapui") === "open";
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
  }, []);

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
          setRuntime({ kind: "error", message: "WebGL2 is unavailable in this browser. The Layer Catalog and trust metadata remain readable, but the interactive map cannot start." });
          return;
        }
        const initialView = pendingViewRef.current ?? KANSAS_VIEW;
        const map = new maplibregl.Map({
          container: mapContainerRef.current,
          style: BASEMAPS[basemapRef.current].style,
          center: initialView.center,
          zoom: initialView.zoom,
          bearing: initialView.bearing,
          pitch: initialView.pitch,
          minZoom: 4,
          maxZoom: 16,
          maxBounds: [[-104.8, 34.8], [-92.0, 42.2]],
          attributionControl: { compact: true },
          cooperativeGestures: true,
        });
        mapRef.current = map;
        setMaplibreProbe((current) => ({ ...current, mapConstructed: true }));
        const scaleControl = new maplibregl.ScaleControl({ unit: measureUnitRef.current, maxWidth: 110 });
        scaleControlRef.current = scaleControl;
        map.addControl(scaleControl, "bottom-left");
        let interactionHandlersBound = false;
        let runtimeError: string | null = null;
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
            controlsReady: Boolean(scaleControlRef.current),
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
          hoveredRef.current = null;
          map.getCanvas().style.cursor = "";
          applyRegistryState(map, visibilityRef.current, opacityRef.current, yearRef.current, orderRef.current);
          map.setProjection({ type: projectionRef.current });
          const currentSelection = selectedRef.current;
          if (currentSelection) {
            const mismatch = isFeatureTimeMismatch(currentSelection.layer.temporal, currentSelection.properties.year, yearRef.current);
            const layerVisible = visibilityRef.current[currentSelection.layerId];
            updateSelectionSource(map, mismatch || !layerVisible ? null : currentSelection.geometry);
          }
          updateMeasurementSource(map, buildMeasurementData(measureCoordinatesRef.current, measurementGeometryModeRef.current));
          refreshMaplibreProbe();
        };

        map.on("style.load", syncStyle);
        map.once("load", () => {
          syncStyle();
          map.setProjection({ type: projectionRef.current });
          setRuntime({ kind: "loading", message: `MapLibre ${version} loaded · verifying local sources and interactions…` });
          map.resize();
        });

        map.on("mousemove", (event) => {
          pendingPointerRef.current = [event.lngLat.lng, event.lngLat.lat];
          if (pointerFrameRef.current === null) {
            pointerFrameRef.current = window.requestAnimationFrame(() => {
              setPointer(pendingPointerRef.current);
              pointerFrameRef.current = null;
            });
          }
          const availableLayers = interactiveLayerIds.filter((id) => map.getLayer(id));
          const candidate = map.queryRenderedFeatures(event.point, { layers: availableLayers })[0];
          if (!candidate) {
            map.getCanvas().style.cursor = "";
            if (hoveredRef.current) map.setFeatureState(hoveredRef.current, { hover: false });
            hoveredRef.current = null;
            return;
          }
          map.getCanvas().style.cursor = "pointer";
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

        map.on("click", (event) => {
          if (measureModeRef.current) {
            measureCoordinatesRef.current = [...measureCoordinatesRef.current, [event.lngLat.lng, event.lngLat.lat]];
            const coordinates = measureCoordinatesRef.current;
            updateMeasurementSource(map, buildMeasurementData(coordinates, measureModeRef.current));
            setMeasurement(measurementLabelFor(measureModeRef.current, coordinates, measureUnitRef.current));
            return;
          }

          const availableLayers = interactiveLayerIds.filter((id) => map.getLayer(id));
          const renderedCandidates = map.queryRenderedFeatures(event.point, { layers: availableLayers });
          const candidate = renderedCandidates[0];
          if (!candidate) {
            setMapQueryCandidates([]);
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
        });
        map.on("error", (event) => {
          const message = event.error?.message || "The map reported an unknown rendering error.";
          const sourceId = (event as typeof event & { sourceId?: string }).sourceId;
          const affectedLayer = sourceId ? LAYER_REGISTRY.find((layer) => layer.sourceId === sourceId) : undefined;
          runtimeError = message;
          if (sourceId) failedSourceIds.add(sourceId);
          setMaplibreProbe((current) => ({ ...current, error: message }));
          if (affectedLayer) {
            setSourceStates((current) => ({ ...current, [affectedLayer.id]: "error" }));
            setRuntime({ kind: "degraded", message: `${affectedLayer.title} could not load; other map layers remain available. ${message}` });
          } else {
            setRuntime({ kind: "error", message: `Map runtime error: ${message}` });
          }
        });
        map.on("idle", () => {
          const probe = refreshMaplibreProbe();
          const ready = probe.styleLoaded
            && probe.canvasReady
            && probe.tilesLoaded
            && probe.sourcesReady === LAYER_REGISTRY.length
            && probe.interactionsReady
            && !runtimeError;
          if (!ready) {
            setRuntime({ kind: runtimeError ? "degraded" : "loading", message: runtimeError ? `MapLibre runtime proof is incomplete: ${runtimeError}` : "MapLibre is waiting for all admitted local capabilities to settle…" });
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
      if (pointerFrameRef.current !== null) window.cancelAnimationFrame(pointerFrameRef.current);
      mapRef.current?.remove();
      mapRef.current = null;
    };
  }, []);

  useEffect(() => {
    const map = mapRef.current;
    if (!map || !map.isStyleLoaded()) return;
    applyRegistryState(map, visibility, opacity, year, layerOrder);
  }, [visibility, opacity, year, layerOrder]);

  useEffect(() => {
    const map = mapRef.current;
    if (!map || !map.isStyleLoaded()) return;
    map.setStyle(BASEMAPS[basemap].style);
    setStyleReady(false);
    setMaplibreProbe((current) => ({ ...current, styleLoaded: false, idle: false, tilesLoaded: false, sourcesReady: 0 }));
    setRuntime({ kind: "loading", message: `Applying ${BASEMAPS[basemap].title} style…` });
  }, [basemap]);

  useEffect(() => {
    const map = mapRef.current;
    if (!map?.isStyleLoaded()) return;
    updateSelectionSource(map, selected && !selectedTimeMismatch && !selectedLayerHidden ? selected.geometry : null);
  }, [selected, selectedLayerHidden, selectedTimeMismatch]);

  useEffect(() => {
    const map = mapRef.current;
    if (!map?.isStyleLoaded()) return;
    map.setProjection({ type: projection });
    setMaplibreProbe((current) => ({ ...current, projection }));
  }, [projection]);

  useEffect(() => {
    const map = mapRef.current;
    if (!map) return;
    const first = window.requestAnimationFrame(() => map.resize());
    const second = window.setTimeout(() => map.resize(), 260);
    return () => { window.cancelAnimationFrame(first); window.clearTimeout(second); };
  }, [leftOpen, rightOpen, timelineOpen]);

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
        mapRef.current?.doubleClickZoom.enable();
        if (mapRef.current?.isStyleLoaded()) updateMeasurementSource(mapRef.current, buildMeasurementData([], null));
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

  const applyViewProfile = (profile: MapViewProfile) => {
    const nextVisibility = Object.fromEntries(LAYER_REGISTRY.map((layer) => [layer.id, profile.visibleLayerIds.includes(layer.id)]));
    visibilityRef.current = nextVisibility;
    yearRef.current = profile.year;
    basemapRef.current = profile.basemap;
    projectionRef.current = profile.projection;
    setVisibility(nextVisibility);
    setYear(profile.year);
    setPlaying(false);
    setBasemap(profile.basemap);
    setProjection(profile.projection);
    setMapQueryCandidates([]);
    locationDerivedViewRef.current = false;
    setLocationCameraRedacted(false);
    clearSelectionState();
    mapRef.current?.fitBounds([[-102.1, 36.95], [-94.55, 40.05]], { padding: 54, duration: motionDuration(600) });
    announce(`${profile.title} applied · view state only`);
  };

  const restoreLastKnownGoodView = () => {
    const lastView = lastKnownGoodViewRef.current;
    mapRef.current?.jumpTo({ ...lastView, center: [...lastView.center] as [number, number] });
    announce("Restored the last known local camera state");
  };

  const reapplyRendererState = () => {
    const map = mapRef.current;
    if (!map?.isStyleLoaded()) {
      announce("Style is not ready; renderer state was not changed");
      return;
    }
    try {
      applyRegistryState(map, visibilityRef.current, opacityRef.current, yearRef.current, orderRef.current);
      map.setProjection({ type: projectionRef.current });
      const currentSelection = selectedRef.current;
      const selectionAvailable = currentSelection && visibilityRef.current[currentSelection.layerId] && !isFeatureTimeMismatch(currentSelection.layer.temporal, currentSelection.properties.year, yearRef.current);
      updateSelectionSource(map, selectionAvailable ? currentSelection.geometry : null);
      updateMeasurementSource(map, buildMeasurementData(measureCoordinatesRef.current, measurementGeometryModeRef.current));
      setSourceStates((current) => Object.fromEntries(LAYER_REGISTRY.map((layer) => [
        layer.id,
        current[layer.id] === "error" ? "error" : map.getSource(layer.sourceId) ? "ready" : "loading",
      ])));
      const hasKnownSourceError = Object.values(sourceStates).includes("error");
      setRuntime(hasKnownSourceError
        ? { kind: "degraded", message: "Renderer state reapplied; known source errors remain visible for diagnosis" }
        : { kind: "ready", message: "MapLibre renderer state reapplied from the site registry" });
      announce(hasKnownSourceError ? "Reapplied renderer state without clearing known source errors" : "Reapplied local style, layers, time, selection, and measurement state");
    } catch (error) {
      setRuntime({ kind: "degraded", message: `Registry reapply failed safely: ${error instanceof Error ? error.message : "unknown failure"}` });
      announce("Renderer state could not be fully reapplied; diagnostics remain available");
    }
  };

  const resetExplorer = () => {
    visibilityRef.current = defaultVisibility;
    opacityRef.current = defaultOpacity;
    orderRef.current = defaultOrder;
    yearRef.current = 2026;
    basemapRef.current = "midnight";
    projectionRef.current = "mercator";
    setVisibility(defaultVisibility);
    setOpacity(defaultOpacity);
    setLayerOrder(defaultOrder);
    setYear(2026);
    setBasemap("midnight");
    setProjection("mercator");
    setMeasureMode(null);
    setMeasurementGeometryMode(null);
    measureModeRef.current = null;
    measurementGeometryModeRef.current = null;
    measureCoordinatesRef.current = [];
    setMeasurement("Select a measurement tool");
    mapRef.current?.doubleClickZoom.enable();
    locationDerivedViewRef.current = false;
    setLocationCameraRedacted(false);
    mapRef.current?.jumpTo(KANSAS_VIEW);
    if (mapRef.current?.isStyleLoaded()) updateMeasurementSource(mapRef.current, buildMeasurementData([], null));
    clearSelection();
    setMapQueryCandidates([]);
    showGuidedStart();
    announce("Explorer reset to the Kansas demonstration view");
  };

  const toggleMeasure = (mode: Exclude<MeasureMode, null>) => {
    if (measureMode === mode) {
      setMeasureMode(null);
      setMeasurementGeometryMode(null);
      measureModeRef.current = null;
      measurementGeometryModeRef.current = null;
      measureCoordinatesRef.current = [];
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
    const minimum = mode === "distance" ? 2 : 3;
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
    setMeasureMode(null);
    setMeasurementGeometryMode(null);
    setMeasurement("Select a measurement tool");
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
        : "Share link copied with camera, layer order, opacity, time, projection, and evidence state");
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
      display: { basemap, active_time: year, visible_layer_ids: activeLayers.map((layer) => layer.id) },
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
        dependency: "HOLD",
        runtime: "HOLD",
        governed_probes: "0/12 NOT_RUN",
      },
      camera: { zoom: Number(view.zoom.toFixed(2)), bearing: Math.round(view.bearing), pitch: Math.round(view.pitch), projection },
      style: { basemap, style_loaded: mapRef.current?.isStyleLoaded() ?? false },
      registry: { sources: LAYER_REGISTRY.length, renderers: interactiveLayerIds.length, visible_layers: visibleCount, source_states: sourceStates },
      active_time: year,
      workspace: currentWorkspace,
      selection: selected ? { feature_id: selected.featureId, layer_id: selected.layerId, layer_visible: !selectedLayerHidden, time_compatible: !selectedTimeMismatch } : null,
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
        <details ref={workspaceDetailsRef} className="workspace-switcher">
          <summary aria-label={`Current workspace: ${publicWorkspaces.find((workspace) => workspace.id === currentWorkspace)?.label}. Open workspace switcher.`}>
            <span>Workspace</span><strong>{publicWorkspaces.find((workspace) => workspace.id === currentWorkspace)?.shortLabel}</strong><b aria-hidden="true">⌄</b>
          </summary>
          <div className="workspace-menu" aria-label="Public Explorer workspaces">
            <header><span>PUBLIC WORKSPACE REGISTRY</span><strong>Move context, not authority</strong><p>These destinations expose public-safe views only.</p></header>
            {publicWorkspaces.map((workspace, index) => <button key={workspace.id} type="button" data-active={currentWorkspace === workspace.id} aria-current={currentWorkspace === workspace.id ? "page" : undefined} onClick={() => activatePublicWorkspace(workspace.id)}>
              <span>{String(index + 1).padStart(2, "0")}</span><div><strong>{workspace.label}</strong><p>{workspace.summary}</p><small>{workspace.capability}</small></div>
            </button>)}
            <footer>Review, operations, source admission, release, and publication remain separate authorized surfaces.</footer>
          </div>
        </details>
        <div className="global-search">
          <label>
            <span className="sr-only">Search current layers and demonstration features</span>
            <span aria-hidden="true">⌕</span>
            <input value={globalQuery} onChange={(event) => setGlobalQuery(event.target.value)} type="search" placeholder="Search places, layers, feature IDs…" aria-describedby="global-search-help" />
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
          <button ref={repositoryButtonRef} className="repository-trigger" type="button" onClick={() => { setCurrentWorkspace("features"); setRepositoryOpen(true); setHelpOpen(false); setToolsExpanded(false); }} aria-expanded={repositoryOpen} aria-controls="repository-briefing" aria-label="Open repository and function briefing" title="Repository and function briefing"><span aria-hidden="true">R</span><i aria-hidden="true">{REPOSITORY_SNAPSHOT.counts.repositoryUpdates}</i></button>
          <button className="story-trigger" type="button" onClick={startStoryTrail} aria-expanded={storyOpen} aria-controls="kfm-story-trail" aria-label="Start guided Kansas trust story" title="Guided Kansas trust story">S</button>
          <button className="share-action" type="button" onClick={shareView} aria-label="Share current map view" title="Share current view">↗</button>
          <button type="button" onClick={() => setHelpOpen((current) => !current)} aria-expanded={helpOpen} aria-label="Open map guide" title="Map guide">?</button>
          <button className="panel-toggle" type="button" onClick={() => { setLeftOpen((current) => { const next = !current; setCurrentWorkspace(next ? "knowledge" : "explore"); return next; }); if (isCompact) { dismissMapUtilityWithoutFocus(); setRightOpen(false); setTimelineOpen(false); } }} aria-expanded={leftOpen} aria-label="Toggle Layer Catalog">☰</button>
        </div>
        {helpOpen && <aside className="map-guide" role="dialog" aria-modal="false" aria-label="Map guide">
          <button className="icon-close" type="button" onClick={() => setHelpOpen(false)} aria-label="Close map guide">×</button>
          <p className="panel-kicker">MAP GUIDE</p><h2>Explore a feature, then check what supports it.</h2>
          <p>Every layer in this build uses site-local synthetic or generalized demonstration data—not released operational data. Choose an example or select any feature to inspect its evidence state.</p>
          <div className="map-guide-actions"><button className="map-guide-start" type="button" onClick={showGuidedStart}>Try quick examples</button><button className="map-guide-start" type="button" onClick={startStoryTrail}>Start four-step story</button></div>
          <ol><li>Search, choose an example, or enable a layer.</li><li>Select a feature.</li><li>Inspect what is supported, missing, corrected, or withheld.</li><li>Review time, lineage, and Focus Mode when you need more detail.</li></ol>
          <p><strong>Shift + drag</strong> uses MapLibre box zoom. The Map Workbench also supports coordinate navigation, camera orientation, and viewport-scoped feature discovery. Terrain and swipe comparison remain unavailable because this build has no audited DEM or compatible comparison source.</p>
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
          <p className="panel-intro">Browse clearly labeled synthetic and generalized demonstration layers. Nothing in this build is a released operational dataset.</p>
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
                    <label className="opacity-control"><span>Opacity <b>{Math.round((opacity[layer.id] ?? layer.defaultOpacity) * 100)}%</b></span><input type="range" min="10" max="100" value={Math.round((opacity[layer.id] ?? layer.defaultOpacity) * 100)} onChange={(event) => setOpacity((current) => ({ ...current, [layer.id]: Number(event.target.value) / 100 }))} /></label>
                    <div className="layer-actions"><button type="button" onClick={() => zoomToLayer(layer)}>Zoom</button><button type="button" onClick={(event) => inspectLayer(layer, event.currentTarget)}>Features</button><button type="button" onClick={() => moveLayer(layer.id, -1)} aria-label={`Move ${layer.title} down in draw order`}>↓</button><button type="button" onClick={() => moveLayer(layer.id, 1)} aria-label={`Move ${layer.title} up in draw order`}>↑</button></div>
                    <p className="layer-note">{layer.sensitivityNote}</p>
                  </div>}
                </article>;
              })}</section>;
            })}
            {filteredLayerIds.size === 0 && <div className="catalog-empty"><strong>No layers found</strong><p>Try a domain, dataset, or geometry term.</p></div>}
          </div>

          <div className="panel-footer-actions"><button type="button" onClick={resetExplorer}>Reset Explorer</button><button type="button" onClick={(event) => openMapUtility("export", event.currentTarget)}>Review public-safe export</button></div>
        </aside>

        <section className="map-stage" aria-label="Kansas MapLibre Explorer">
          <div className="mission-band"><span data-runtime={runtime.kind}><i /> {runtime.kind === "ready" ? `MAPLIBRE ${maplibreProbe.version ?? EXPECTED_MAPLIBRE_VERSION} READY` : runtime.kind === "loading" ? "MAPLIBRE STARTING" : "EXPLORER FALLBACK"}</span><p>Synthetic and generalized data only · Select a feature to inspect what is supported, missing, corrected, or withheld.</p></div>
          <div id="map-canvas" ref={mapContainerRef} className="map-canvas" tabIndex={0} role="application" aria-label="Interactive MapLibre map of Kansas demonstration layers. Use arrow keys to pan and plus or minus to zoom; use Map Workbench Inspect or the Layer Catalog for a keyboard feature alternative." />

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

          <nav className="map-tool-rail" aria-label="Map tools">
            <button type="button" onClick={() => mapRef.current?.zoomIn({ duration: motionDuration(250) })} aria-label="Zoom in" data-tooltip="Zoom in">+</button>
            <button type="button" onClick={() => mapRef.current?.zoomOut({ duration: motionDuration(250) })} aria-label="Zoom out" data-tooltip="Zoom out">−</button>
            <button className="mobile-hidden-control" type="button" onClick={() => mapRef.current?.resetNorthPitch({ duration: motionDuration(450) })} aria-label="Reset compass and pitch" data-tooltip="Reset north">N</button>
            <button type="button" onClick={fitKansasView} aria-label="Reset view to Kansas" data-tooltip="Kansas extent">KS</button>
            <button ref={mapUtilityButtonRef} type="button" onClick={(event) => mapUtilityOpen ? closeMapUtility() : openMapUtility("navigate", event.currentTarget)} aria-expanded={mapUtilityOpen} aria-controls="map-utility-panel" aria-label="Open Map Workbench" data-tooltip="Map Workbench">UI</button>
            <button className="mobile-hidden-control" type="button" onClick={locateUser} aria-label="Use my location" data-tooltip="My location">⌾</button>
            <button type="button" onClick={() => setToolsExpanded((current) => !current)} aria-expanded={toolsExpanded} aria-controls="more-map-tools" aria-label="More map tools" data-tooltip="More tools">•••</button>
            {toolsExpanded && <div className="secondary-tools" id="more-map-tools">
              <button type="button" onClick={(event) => openMapUtility("navigate", event.currentTarget)}><span>UI</span>Map Workbench</button>
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
            aria-hidden={!mapUtilityOpen}
            inert={!mapUtilityOpen}
            aria-modal={isCompact && mapUtilityOpen || undefined}
            role={isCompact && mapUtilityOpen ? "dialog" : undefined}
            aria-labelledby="map-utility-title"
          >
            <header className="map-utility-heading">
              <div><p className="panel-kicker">MAP OPERATIONS</p><h2 id="map-utility-title">Map Workbench</h2><span>One interface for renderer controls, inspection, display, measurement, trust-aware export, and recovery.</span></div>
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
              {mapUtilityView === "navigate" && <section id="map-utility-view-navigate" role="tabpanel" aria-labelledby="map-utility-tab-navigate" className="map-utility-section">
                <div className="map-utility-section-heading"><span>NAVIGATE</span><h3>Camera, coordinates + private location</h3><p>MapLibre camera actions change only this browser view. They never change evidence, policy, review, release, or publication state.</p></div>
                <dl className="map-camera-facts">
                  <div><dt>Center</dt><dd>{locationCameraRedacted ? "Private camera · redacted" : `${formatCoordinate(view.center[1], "N", "S")} · ${formatCoordinate(view.center[0], "E", "W")}`}</dd></div>
                  <div><dt>Zoom</dt><dd>{view.zoom.toFixed(2)}</dd></div>
                  <div><dt>Bearing / pitch</dt><dd>{Math.round(view.bearing)}° / {Math.round(view.pitch)}°</dd></div>
                  <div><dt>Projection</dt><dd>{projection}</dd></div>
                </dl>
                <div className="map-utility-actions map-navigation-actions">
                  <button type="button" onClick={() => mapRef.current?.zoomIn({ duration: motionDuration(250) })}>Zoom in</button>
                  <button type="button" onClick={() => mapRef.current?.zoomOut({ duration: motionDuration(250) })}>Zoom out</button>
                  <button type="button" onClick={() => mapRef.current?.resetNorthPitch({ duration: motionDuration(450) })}>Reset north</button>
                  <button type="button" onClick={fitKansasView}>Fit Kansas</button>
                  <button type="button" onClick={toggleFullscreen}>Fullscreen</button>
                  <button type="button" onClick={locateUser}>Use my location</button>
                  <button type="button" onClick={() => void copyMapCenter()} disabled={locationCameraRedacted}>Copy center</button>
                </div>
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

              {mapUtilityView === "compare" && <section id="map-utility-view-compare" role="tabpanel" aria-labelledby="map-utility-tab-compare" className="map-utility-section layer-compare-section">
                <div className="map-utility-section-heading"><span>COMPARE</span><h3>Layer truth + capability matrix</h3><p>Compare two registry layers without flattening their time, source role, release posture, or sensitivity into a single score.</p></div>
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
                <div className="map-control-group"><header><strong>Geometry</strong><span>{measureMode ? "ADDING POINTS" : measurementGeometryMode ? "COMPLETE / PAUSED" : "IDLE"}</span></header><div className="map-choice-grid"><button type="button" aria-pressed={measurementGeometryMode === "distance"} onClick={() => toggleMeasure("distance")}><strong>Distance</strong><small>Polyline approximation</small></button><button type="button" aria-pressed={measurementGeometryMode === "area"} onClick={() => toggleMeasure("area")}><strong>Area</strong><small>Polygon approximation</small></button></div></div>
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
                <aside className="map-utility-boundary"><strong>Renderer evidence boundary</strong><p>This Site runs MapLibre {EXPECTED_MAPLIBRE_VERSION} against site-local GeoJSON fixtures. GitHub proves an exact dependency, a bounded concrete adapter, the renderer-neutral port, and deterministic Null runtime; broader authenticated, performance, terrain, accessibility, and long-session readiness remain held.</p></aside>
              </section>}
            </div>
          </aside>

          {measurementGeometryMode && <div className="measurement-readout" role="region" aria-label="Active screen measurement"><span>{measurementGeometryMode.toUpperCase()} · {measureMode ? "ACTIVE" : "COMPLETE"}</span><strong aria-live="polite">{measurement}</strong><div><button type="button" onClick={undoMeasurementPoint}>Undo</button><button type="button" onClick={finishMeasurement} disabled={!measureMode}>Finish</button><button type="button" onClick={clearMeasurement}>Clear</button></div></div>}

          <div className="map-mobile-actions">
            <button type="button" onClick={() => { setCurrentWorkspace("knowledge"); dismissMapUtilityWithoutFocus(); setLeftOpen(true); setRightOpen(false); setTimelineOpen(false); }}>Layers <b>{visibleCount}</b></button>
            <button type="button" onClick={() => { if (selected) { setCurrentWorkspace("trust"); dismissMapUtilityWithoutFocus(); setRightOpen(true); setLeftOpen(false); setTimelineOpen(false); } }} disabled={!selected}>Evidence</button>
            <button type="button" onClick={() => openMapUtility("navigate")}>Map</button>
            <button type="button" onClick={() => { setCurrentWorkspace("explore"); dismissMapUtilityWithoutFocus(); setTimelineOpen(true); setLeftOpen(false); setRightOpen(false); }}>Time <b>{formatTimelineStep(year)}</b></button>
            <button type="button" onClick={() => { setCurrentWorkspace("features"); setRepositoryView("functions"); setRepositoryOpen(true); }}>Functions</button>
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
                <h3>Selection-to-evidence trace</h3><ol className="lineage-list"><li><span>01</span><div><strong>MapLibre candidate</strong><small>queryRenderedFeatures identified a candidate only</small></div></li><li><span>02</span><div><strong>Stable registry context</strong><small>{selected.featureId}</small></div></li><li><span>03</span><div><strong>Evidence resolution</strong><small>{selected.properties.citation}</small></div></li><li><span>04</span><div><strong>Policy / rights</strong><small>{selected.properties.evidenceState}</small></div></li><li><span>05</span><div><strong>Public-safe view</strong><small>Drawer + bounded Focus Mode</small></div></li></ol>
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
          <span data-runtime={runtime.kind}><i />{runtime.kind.toUpperCase()}</span><span>{formatCoordinate(pointer[1], "N", "S")} · {formatCoordinate(pointer[0], "E", "W")}</span><span>{scaleAtView(view)}</span><span>Zoom {view.zoom.toFixed(2)}</span><span>Bearing {Math.round(view.bearing)}° · Pitch {Math.round(view.pitch)}°</span><span>{formatTimelineStep(year)} active time</span><span>{visibleCount} layers visible</span><span>GeoJSON fixtures · MapLibre {maplibreProbe.version ?? EXPECTED_MAPLIBRE_VERSION}</span><span>Repo main@{REPOSITORY_SNAPSHOT.shortCommit}</span>
        </footer>
      </main>

      <div className="toast" role="status" aria-live="polite" data-visible={Boolean(toast)}>{toast}</div>
    </div>
  );
}
