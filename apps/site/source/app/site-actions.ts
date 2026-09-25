/**
 * The action contract for the Site's visible controls and handoff affordances.
 *
 * This is an inventory, not a second event bus. Existing handlers remain in
 * their owning components; this registry makes the user-facing action surface
 * explicit for documentation, validation, and connector alignment.
 */

export type SiteActionMode = "LOCAL_UI" | "READ_ONLY_CONNECTOR" | "EXTERNAL_NAVIGATION" | "DEVICE_LOCAL" | "AUTHENTICATED_WRITE";

export type SiteActionCategory = "layers" | "connections" | "hydrology" | "temporal" | "reports" | "workspaces" | "focus" | "sources";

export type SiteActionRecord = Readonly<{
  id: string;
  label: string;
  category: SiteActionCategory;
  mode: SiteActionMode;
  handlerPath: string;
  connectorIds: readonly string[];
  inputs: readonly string[];
  outcomes: readonly string[];
  boundary: string;
}>;

export const SITE_ACTIONS = Object.freeze([
  { id: "submit-source-data", label: "Upload / propose source data", category: "sources", mode: "AUTHENTICATED_WRITE", handlerPath: "app/api/data-submissions/route.ts:POST", connectorIds: [], inputs: ["file up to 10 MB", "authenticated contributor", "source, dates, reuse terms, sensitivity"], outcomes: ["durable private submission", "recoverable validation/storage error"], boundary: "R2 quarantine and D1 metadata only. Submission never publishes or changes a map layer." },
  { id: "review-source-data", label: "Record steward review", category: "sources", mode: "AUTHENTICATED_WRITE", handlerPath: "app/api/data-submissions/[id]/route.ts:PATCH", connectorIds: [], inputs: ["assigned steward", "submission version", "decision and note"], outcomes: ["versioned review history", "unauthorized/conflict rejection"], boundary: "Server allowlist and optimistic concurrency; acceptance is a preparation candidate, not source admission or map publication." },
  { id: "download-source-data", label: "Download source data", category: "sources", mode: "READ_ONLY_CONNECTOR", handlerPath: "app/api/source-download/route.ts:GET", connectorIds: [], inputs: ["allowlisted source id"], outcomes: ["dated provider data with provenance", "explicit upstream error"], boundary: "No arbitrary URL proxy. Uploaded files use a separate authenticated ownership/steward download route." },
  {
    id: "toggle-layer-visibility",
    label: "Show or hide a layer",
    category: "layers",
    mode: "LOCAL_UI",
    handlerPath: "app/page.tsx:setVisibility",
    connectorIds: [],
    inputs: ["layer id", "desired visibility"],
    outcomes: ["MapLibre visibility changes", "visibility is carried into view/report state"],
    boundary: "Only registered Site layers can be changed; this does not admit an upstream source or alter evidence state.",
  },
  {
    id: "set-layer-opacity",
    label: "Adjust layer opacity",
    category: "layers",
    mode: "LOCAL_UI",
    handlerPath: "app/page.tsx:setOpacity",
    connectorIds: [],
    inputs: ["layer id", "opacity 0.10–1.00"],
    outcomes: ["Renderer opacity changes", "the chosen value remains inspectable in the layer controls"],
    boundary: "A visual adjustment is never a confidence, severity, or data-quality score.",
  },
  {
    id: "inspect-layer-features",
    label: "Inspect layer features",
    category: "layers",
    mode: "LOCAL_UI",
    handlerPath: "app/page.tsx:inspectLayer",
    connectorIds: [],
    inputs: ["layer id", "current temporal query"],
    outcomes: ["Feature list opens", "selected record can enter the evidence drawer"],
    boundary: "The map identifies a candidate; the registry and evidence posture determine what can be stated.",
  },
  {
    id: "solo-layer",
    label: "Solo a layer",
    category: "layers",
    mode: "LOCAL_UI",
    handlerPath: "app/page.tsx:isolateLayer",
    connectorIds: [],
    inputs: ["layer id"],
    outcomes: ["Other registered layers are hidden", "the selected layer remains visible"],
    boundary: "Solo mode changes display state only and never removes source-role limitations.",
  },
  {
    id: "reorder-layer",
    label: "Change draw order",
    category: "layers",
    mode: "LOCAL_UI",
    handlerPath: "app/page.tsx:moveLayer",
    connectorIds: [],
    inputs: ["layer id", "direction"],
    outcomes: ["MapLibre draw order changes", "the ordering is retained in the current view"],
    boundary: "Ordering is presentation state; it cannot make a context layer an evidence layer.",
  },
  {
    id: "toggle-context-connection",
    label: "Show or hide an official context connection",
    category: "connections",
    mode: "LOCAL_UI",
    handlerPath: "app/page.tsx:setOfficialContextVisible",
    connectorIds: ["official-context"],
    inputs: ["official context id", "desired visibility"],
    outcomes: ["Source-specific context is selected or withheld", "the source state remains visible"],
    boundary: "The fixed source allowlist is the boundary; the control cannot accept an arbitrary URL.",
  },
  {
    id: "toggle-context-group",
    label: "Show or hide a priority context group",
    category: "connections",
    mode: "LOCAL_UI",
    handlerPath: "app/page.tsx:setPriorityContextGroupVisible",
    connectorIds: ["official-context"],
    inputs: ["priority group", "desired visibility"],
    outcomes: ["Earthquake, hydrology, or smoke source selections update together", "group counts refresh"],
    boundary: "Group actions are convenience controls over already-registered sources, not a source discovery path.",
  },
  {
    id: "refresh-visible-context",
    label: "Refresh visible official context",
    category: "connections",
    mode: "READ_ONLY_CONNECTOR",
    handlerPath: "app/page.tsx:refreshVisibleOfficialContext",
    connectorIds: ["official-context"],
    inputs: ["visible source ids", "current frame"],
    outcomes: ["bounded adapter request", "ready, partial, empty, or error state"],
    boundary: "Read-only, allowlisted requests have bounded time/feature limits and never fall back silently to synthetic data.",
  },
  {
    id: "set-context-opacity",
    label: "Adjust context opacity",
    category: "connections",
    mode: "LOCAL_UI",
    handlerPath: "app/page.tsx:setOfficialContextOpacity",
    connectorIds: ["official-context"],
    inputs: ["official context id", "opacity 0.10–1.00"],
    outcomes: ["context renderer opacity changes"],
    boundary: "Opacity is a visual control and must not be interpreted as evidence strength or hazard severity.",
  },
  {
    id: "open-provider-source",
    label: "Open the provider source",
    category: "sources",
    mode: "EXTERNAL_NAVIGATION",
    handlerPath: "app/page.tsx:official-context-actions",
    connectorIds: ["official-context"],
    inputs: ["registered source id", "provider link"],
    outcomes: ["provider portal opens in a new tab"],
    boundary: "Navigation is read-only and does not imply provider approval, source admission, or an official warning handoff.",
  },
  {
    id: "refresh-streamflow",
    label: "Refresh River Pulse observations",
    category: "hydrology",
    mode: "READ_ONLY_CONNECTOR",
    handlerPath: "app/page.tsx:refreshStreamflow",
    connectorIds: ["usgs-streamflow"],
    inputs: ["range", "optional station id", "current frame"],
    outcomes: ["bounded USGS observations", "gap-aware station state", "provisional/qualified labels retained"],
    boundary: "No interpolation, basin-wide generalization, flood warning, or permanent archive is created by this action.",
  },
  {
    id: "change-hydrology-range",
    label: "Change hydrology time range",
    category: "hydrology",
    mode: "LOCAL_UI",
    handlerPath: "app/hydrology-observatory.tsx:range control",
    connectorIds: ["usgs-streamflow", "noaa-nwps-gauges"],
    inputs: ["24h, 7d, 30d, or 1y range", "optional station id"],
    outcomes: ["bounded adapter query changes", "observation/forecast/model clocks remain distinct"],
    boundary: "A longer display range does not backfill missing samples or turn operational context into a KFM release.",
  },
  {
    id: "step-exact-observation",
    label: "Step an exact observation frame",
    category: "temporal",
    mode: "LOCAL_UI",
    handlerPath: "app/temporal-sweep.ts:nextTemporalFrame",
    connectorIds: ["usgs-streamflow", "nws-radar", "noaa-hms-smoke"],
    inputs: ["direction", "declared temporal query"],
    outcomes: ["Map and observatory move to an actual returned frame", "gaps remain explicit"],
    boundary: "No synthetic timestamps, interpolation, nearest-time substitution, or carry-forward across tolerance is permitted.",
  },
  {
    id: "refresh-radar-frames",
    label: "Refresh exact radar frames",
    category: "temporal",
    mode: "READ_ONLY_CONNECTOR",
    handlerPath: "app/page.tsx:refreshNoaaRadarManifest",
    connectorIds: ["nws-radar"],
    inputs: ["requested loop span"],
    outcomes: ["NOAA-advertised observation manifest", "cadence and gaps become visible"],
    boundary: "The action never requests an untimed latest image or converts reflectivity into a warning, rainfall rate, or all-clear.",
  },
  {
    id: "play-exact-radar-loop",
    label: "Play an exact radar loop",
    category: "temporal",
    mode: "LOCAL_UI",
    handlerPath: "app/page.tsx:radar playback controls",
    connectorIds: ["nws-radar"],
    inputs: ["exact frame manifest", "playback speed", "loop state"],
    outcomes: ["only discovered frames are played", "stale/failed sequences pause visibly"],
    boundary: "Playback is observation context, not forecasting, warning delivery, or emergency communication.",
  },
  {
    id: "save-device-workspace",
    label: "Save a device-local workspace",
    category: "workspaces",
    mode: "DEVICE_LOCAL",
    handlerPath: "app/workspace-storage.ts:readDraftSnapshot",
    connectorIds: [],
    inputs: ["current view", "visible layers", "time", "selection", "trust posture"],
    outcomes: ["device-local draft persists", "restored state preserves evidence boundary"],
    boundary: "No server-side record, public release, or cross-device synchronization is implied.",
  },
  {
    id: "build-map-report",
    label: "Build a map report",
    category: "reports",
    mode: "DEVICE_LOCAL",
    handlerPath: "app/report-story-workspaces.tsx:report workspace",
    connectorIds: [],
    inputs: ["visible registry layers", "selected context", "time", "evidence state"],
    outcomes: ["report draft carries map context", "public-safe export preserves limitations"],
    boundary: "External context remains labeled and excluded from KFM admission, release, and EvidenceBundle claims.",
  },
  {
    id: "open-focus-mode",
    label: "Open bounded Focus Mode",
    category: "focus",
    mode: "LOCAL_UI",
    handlerPath: "app/focus-mode.ts:focusResultForState",
    connectorIds: [],
    inputs: ["selected feature", "evidence state", "declared intent"],
    outcomes: ["focus gate trace", "answer, abstention, or bounded action proposal"],
    boundary: "Focus Mode cannot promote external context, incomplete evidence, or model output into a released answer.",
  },
  {
    id: "copy-source-intake-draft",
    label: "Copy a source intake draft",
    category: "sources",
    mode: "DEVICE_LOCAL",
    handlerPath: "app/page.tsx:source intake workflow",
    connectorIds: [],
    inputs: ["provider source record", "access posture", "known gaps"],
    outcomes: ["reviewable intake text", "gaps and approval state remain visible"],
    boundary: "A candidate source is not activated, admitted, released, or treated as an upstream answer merely because an intake draft exists.",
  },
] as const satisfies readonly SiteActionRecord[]);

export type SiteActionId = (typeof SITE_ACTIONS)[number]["id"];

export const SITE_ACTION_BY_ID = Object.freeze(
  Object.fromEntries(SITE_ACTIONS.map((action) => [action.id, action])) as unknown as Record<SiteActionId, SiteActionRecord>,
);
