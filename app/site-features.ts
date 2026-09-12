import type { OfficialContextId } from "./live-context";
import type { SiteActionId } from "./site-actions";

export type SiteFeatureStatus = "LIVE_UI" | "ACTIVE_CONTEXT" | "BOUNDED_PROOF" | "HELD";

export type SiteFeatureRecord = Readonly<{
  id: string;
  title: string;
  domain: "map" | "connections" | "earthquakes" | "hydrology" | "smoke" | "terrain" | "temporal" | "evidence" | "workspaces" | "focus" | "sources" | "alignment";
  status: SiteFeatureStatus;
  surface: string;
  userOutcome: string;
  sourceIds: readonly OfficialContextId[];
  actionIds: readonly SiteActionId[];
  codePaths: readonly string[];
  boundary: string;
}>;

/** Product features are intentionally separate from provider connections and handlers. */
export const SITE_FEATURES = Object.freeze([
  { id: "terrain-performance-controls", title: "3D appearance and efficient map loading", domain: "map", status: "ACTIVE_CONTEXT", surface: "Map mode strip and top-bar Data & downloads", userOutcome: "Choose imagery, topographic terrain or mapped buildings; adjust lighting and scale; recover individual layers and reach original downloads.", sourceIds: ["usgs-3dep-hillshade", "usgs-3dep-slope"], actionIds: ["download-source-data"], codePaths: ["app/map-toolbar.tsx", "app/map-performance.ts", "app/terrain-tiles.ts", "app/map-runtime.ts"], boundary: "Display terrain remains separate from USGS analytical elevation. Cached tiles retain retrieval timestamps. Quality modes change rendering budgets, not source values. No browser FPS claim or dependency upgrade." },
  { id: "daily-real-baseline", title: "Daily real-data baseline", domain: "map", status: "ACTIVE_CONTEXT", surface: "Explorer start and Event Observatory", userOutcome: "Open on real county/water sources and today's latest available frame; refresh while following today.", sourceIds: ["census-counties", "usgs-streamflow", "usgs-3dhp-hydrography"], actionIds: ["download-source-data"], codePaths: ["app/daily-baseline.ts", "app/page.tsx", "app/observatory/workspace.tsx"], boundary: "No synthetic layer starts enabled. Explicit historical selections stop automatic following; provider editions, daily summaries and missing hours keep their own meaning." },
  { id: "data-contribution-review", title: "Data commons and steward desk", domain: "sources", status: "LIVE_UI", surface: "/data and /stewards", userOutcome: "Propose data, download source files, follow submission status and review a durable queue.", sourceIds: [], actionIds: ["submit-source-data", "review-source-data", "download-source-data"], codePaths: ["app/data/workspace.tsx", "app/data-intake-server.ts", "db/schema.ts", "app/api/data-submissions/route.ts"], boundary: "Files remain private to their contributor and assigned stewards. Accepted proposals are not automatically admitted or rendered." },
  {
    id: "map-investigation-shell",
    title: "Map investigation shell",
    domain: "map",
    status: "LIVE_UI",
    surface: "Map command bar, MapLibre canvas, utility controls, and navigation",
    userOutcome: "Start an investigation with place, time, layers, representation, and trust posture visible together.",
    sourceIds: [],
    actionIds: ["toggle-layer-visibility", "set-layer-opacity", "save-device-workspace"],
    codePaths: ["app/page.tsx", "app/map-runtime.ts", "app/map-interface.ts"],
    boundary: "The shell coordinates registered local and external-context surfaces; it does not create a released KFM dataset.",
  },
  {
    id: "layer-catalog-controls",
    title: "Layer Catalog control surface",
    domain: "map",
    status: "LIVE_UI",
    surface: "Layer Catalog rows and expanded Controls affordance",
    userOutcome: "Find a layer, change visibility/opacity/order, zoom, inspect features, or solo the layer without hunting for hidden controls.",
    sourceIds: [],
    actionIds: ["toggle-layer-visibility", "set-layer-opacity", "inspect-layer-features", "solo-layer", "reorder-layer"],
    codePaths: ["app/page.tsx", "app/explorer-data.ts", "app/globals.css"],
    boundary: "Presentation controls do not change source authority, evidence state, or release status.",
  },
  {
    id: "priority-context-deck",
    title: "Priority context deck",
    domain: "connections",
    status: "LIVE_UI",
    surface: "Layer Catalog > Priority Connections",
    userOutcome: "Directly toggle earthquake, hydrology, and smoke/weather connections and see selected counts plus settled source states.",
    sourceIds: ["usgs-earthquakes", "raspberry-shake-stations", "usgs-streamflow", "noaa-nwps-gauges", "usgs-3dhp-hydrography", "usgs-wbd-watersheds", "noaa-nwm-analysis", "noaa-nwm-short-range", "noaa-hms-smoke", "nws-alerts", "nws-radar"],
    actionIds: ["toggle-context-connection", "toggle-context-group", "refresh-visible-context", "set-context-opacity", "open-provider-source"],
    codePaths: ["app/page.tsx", "app/live-context.ts", "app/globals.css"],
    boundary: "The deck only orchestrates the fixed official allowlist and never turns live context into a hazard answer.",
  },
  {
    id: "earthquake-seismic-context",
    title: "Earthquake and seismic context",
    domain: "earthquakes",
    status: "ACTIVE_CONTEXT",
    surface: "USGS earthquakes + Raspberry Shake station metadata",
    userOutcome: "Inspect bounded Kansas-area events alongside nearby station identities and provider handoffs.",
    sourceIds: ["usgs-earthquakes", "raspberry-shake-stations"],
    actionIds: ["toggle-context-connection", "refresh-visible-context", "set-context-opacity", "open-provider-source"],
    codePaths: ["app/api/live-context/route.ts", "app/live-context.ts", "app/page.tsx"],
    boundary: "This is catalog/station context, not an alert, warning, waveform claim, response-corrected amplitude, or seismic forecast.",
  },
  {
    id: "hydrology-river-pulse",
    title: "Hydrology and River Pulse",
    domain: "hydrology",
    status: "ACTIVE_CONTEXT",
    surface: "USGS River Pulse, NOAA NWPS, 3DHP, WBD, and NWM controls",
    userOutcome: "Compare observed, forecast, modeled, network, and watershed context while retaining each clock and source role.",
    sourceIds: ["usgs-streamflow", "noaa-nwps-gauges", "usgs-3dhp-hydrography", "usgs-wbd-watersheds", "noaa-nwm-analysis", "noaa-nwm-short-range"],
    actionIds: ["toggle-context-connection", "refresh-streamflow", "change-hydrology-range", "step-exact-observation", "refresh-visible-context", "set-context-opacity", "open-provider-source"],
    codePaths: ["app/hydrology-observatory.tsx", "app/streamflow.ts", "app/noaa-hydrology.ts", "app/api/hydrology/streamflow/route.ts", "app/api/hydrology/noaa/route.ts"],
    boundary: "Observed discharge is not interpolated or generalized across basins/reaches; NWPS/NWM products are not silently relabeled as gauge observations, warnings, or KFM evidence.",
  },
  {
    id: "smoke-weather-context",
    title: "Smoke and weather context",
    domain: "smoke",
    status: "ACTIVE_CONTEXT",
    surface: "NOAA HMS smoke footprints, NWS alerts, and NOAA radar",
    userOutcome: "See dated smoke footprints and exact radar observations beside weather context, with freshness and gap states exposed.",
    sourceIds: ["noaa-hms-smoke", "nws-alerts", "nws-radar"],
    actionIds: ["toggle-context-connection", "refresh-visible-context", "refresh-radar-frames", "play-exact-radar-loop", "step-exact-observation", "set-context-opacity", "open-provider-source"],
    codePaths: ["app/api/live-context/route.ts", "app/api/noaa-radar/frames/route.ts", "app/noaa-radar.ts", "app/event-atlas.ts", "app/page.tsx"],
    boundary: "Footprints and pixels are not surface PM2.5, plume altitude/transport, fire perimeter, warning, forecast, or all-clear products.",
  },
  {
    id: "lidar-terrain-context",
    title: "3DEP LiDAR-derived terrain context",
    domain: "terrain",
    status: "ACTIVE_CONTEXT",
    surface: "Dynamic USGS 3DEP hillshade and slope carriers",
    userOutcome: "Use relief and slope visuals for orientation while keeping derivative and acquisition limits visible.",
    sourceIds: ["usgs-3dep-hillshade", "usgs-3dep-slope"],
    actionIds: ["toggle-context-connection", "set-context-opacity", "open-provider-source"],
    codePaths: ["app/live-context.ts", "app/terrain-sources.ts", "app/map-runtime.ts", "app/page.tsx"],
    boundary: "Rendered relief is not raw point-cloud evidence, a sampled numeric elevation, a work-unit accuracy claim, or a released derivative lineage receipt.",
  },
  {
    id: "date-bound-observatory",
    title: "Date-bound event observatory",
    domain: "temporal",
    status: "BOUNDED_PROOF",
    surface: "/observatory and /observatory/sources",
    userOutcome: "Replay exact provider artifacts and source coverage without leaking current operational context into historical atlas time.",
    sourceIds: ["nws-radar", "noaa-hms-smoke", "usgs-streamflow"],
    actionIds: ["step-exact-observation", "refresh-radar-frames", "play-exact-radar-loop"],
    codePaths: ["app/observatory/workspace.tsx", "app/event-atlas.ts", "app/temporal-sweep.ts", "app/api/event-atlas"],
    boundary: "Replay links do not freeze provider revisions and do not become KFM EvidenceBundles or current-only safety guidance.",
  },
  {
    id: "evidence-drawer-and-trust",
    title: "Evidence drawer and trust membrane",
    domain: "evidence",
    status: "LIVE_UI",
    surface: "Selected-feature drawer, source role, evidence, policy, and Focus gates",
    userOutcome: "Understand what a selected record can support before composing a report or answer.",
    sourceIds: [],
    actionIds: ["inspect-layer-features", "open-focus-mode", "copy-source-intake-draft"],
    codePaths: ["app/page.tsx", "app/workspace-model.ts", "app/runtime-seam.ts", "app/focus-mode.ts"],
    boundary: "Context, candidate, model, and synthetic records cannot be promoted by UI convenience into released evidence.",
  },
  {
    id: "report-story-workspaces",
    title: "Report and guided-story workspaces",
    domain: "workspaces",
    status: "LIVE_UI",
    surface: "Device-local report, story, export, and workspace drafts",
    userOutcome: "Carry current map state into a readable draft while preserving time, layer, and evidence posture.",
    sourceIds: [],
    actionIds: ["save-device-workspace", "build-map-report"],
    codePaths: ["app/report-story-workspaces.tsx", "app/export-center.ts", "app/workspace-storage.ts", "app/workspace-model.ts"],
    boundary: "Draft creation is not publication, release, synchronization, or an authorization to expose protected geometry.",
  },
  {
    id: "bounded-focus-mode",
    title: "Bounded Focus Mode",
    domain: "focus",
    status: "BOUNDED_PROOF",
    surface: "Focus gate trace and Qwen handoff",
    userOutcome: "Receive an evidence-bounded answer, abstention, or next action with the gate reason visible.",
    sourceIds: [],
    actionIds: ["open-focus-mode"],
    codePaths: ["app/focus-mode.ts", "app/qwen-context.ts", "app/api/qwen/route.ts", "app/page.tsx"],
    boundary: "The model is downstream of source/evidence/policy checks and cannot issue life-safety, regulatory, health, or engineering instructions.",
  },
  {
    id: "source-observatory-and-intake",
    title: "Source observatory and intake",
    domain: "sources",
    status: "LIVE_UI",
    surface: "Sources workbench, provider links, gap register, and intake draft",
    userOutcome: "See candidate source identity, readiness, coverage, limits, and the next review gate before activation.",
    sourceIds: [],
    actionIds: ["open-provider-source", "copy-source-intake-draft"],
    codePaths: ["app/source-intelligence.ts", "app/observatory/sources/page.tsx", "docs/KFM_SOURCE_GAP_REGISTER.md"],
    boundary: "Discovery, access, activation, admission, release, and publication remain separate lifecycle decisions.",
  },
  {
    id: "held-raspberry-waveform-bridge",
    title: "Raspberry Shake waveform bridge scaffold",
    domain: "earthquakes",
    status: "HELD",
    surface: "Architecture registry and next-gate documentation",
    userOutcome: "Make the missing waveform work explicit without implying it is integrated.",
    sourceIds: ["raspberry-shake-stations"],
    actionIds: ["open-provider-source", "copy-source-intake-draft"],
    codePaths: ["app/site-connections.ts", "app/site-features.ts", "docs/SITE_FEATURE_CONNECTION_ACTION_MAP.md"],
    boundary: "Waveform retrieval, StationXML response handling, miniSEED validation, bounded windows, caching, evidence identity, and correction/rollback review remain future work.",
  },
  {
    id: "held-lidar-lineage",
    title: "LiDAR lineage receipt scaffold",
    domain: "terrain",
    status: "HELD",
    surface: "Architecture registry and alignment documentation",
    userOutcome: "Keep exact work-unit, CRS/datum, units, spacing, accuracy, nodata, processing, and derivative lineage gaps visible.",
    sourceIds: ["usgs-3dep-hillshade", "usgs-3dep-slope"],
    actionIds: ["open-provider-source", "copy-source-intake-draft"],
    codePaths: ["app/site-connections.ts", "app/site-features.ts", "docs/SITE_FEATURE_CONNECTION_ACTION_MAP.md"],
    boundary: "The repository's fixture-only LiDAR contract remains inactive until its source, policy, validation, release, and operational evidence gates are satisfied.",
  },
] as const satisfies readonly SiteFeatureRecord[]);

export type SiteFeatureId = (typeof SITE_FEATURES)[number]["id"];

export const SITE_FEATURE_BY_ID = Object.freeze(
  Object.fromEntries(SITE_FEATURES.map((feature) => [feature.id, feature])) as unknown as Record<SiteFeatureId, SiteFeatureRecord>,
);
