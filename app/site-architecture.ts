export type SiteCodeSurfaceRecord = Readonly<{
  id: string;
  title: string;
  role: string;
  paths: readonly string[];
  handles: readonly string[];
  verification: readonly string[];
}>;

export type SiteRouteContract = Readonly<{
  id: string;
  route: string;
  owner: string;
  purpose: string;
  trustBoundary: string;
}>;

/** Coding surfaces are ownership and verification pointers, not a duplicate module graph. */
export const SITE_CODE_SURFACES = Object.freeze([
  { id: "data-commons", title: "Source downloads and steward intake", role: "Owns authenticated uploads, private file access, versioned review and source download links.", paths: ["app/data", "app/stewards", "app/api/data-submissions", "app/data-intake-server.ts", "app/source-downloads.ts", "db/schema.ts", "drizzle"], handles: ["D1 submission metadata", "R2 private files", "steward allowlist", "review audit history"], verification: ["tests/data-intake.test.mjs", "tests/intake-worker.test.mjs"] },
  {
    id: "map-shell",
    title: "Map shell and interaction surface",
    role: "Owns the first-screen investigation flow, catalog controls, map utilities, and context presentation.",
    paths: ["app/page.tsx", "app/globals.css"],
    handles: ["layer visibility/opacity/order", "official-context controls", "selection and evidence drawer", "report/story handoff"],
    verification: ["tests/rendered-html.test.mjs", "npm run build"],
  },
  {
    id: "feature-and-layer-model",
    title: "Feature, layer, and renderer model",
    role: "Defines site-local layer records, rendering contracts, terrain behavior, and temporal filters.",
    paths: ["app/explorer-data.ts", "app/map-runtime.ts", "app/temporal-sweep.ts", "app/terrain-sources.ts"],
    handles: ["registered layers", "MapLibre sources/layers", "time availability", "terrain and relief"],
    verification: ["tests/rendered-html.test.mjs", "tests/temporal-sweep.test.mjs", "tests/snapshot-workflows.test.mjs"],
  },
  {
    id: "official-context-adapters",
    title: "Official context allowlist and adapters",
    role: "Keeps source identity, provider URLs, feed bounds, caps, error states, and evidence exclusion together.",
    paths: ["app/live-context.ts", "app/api/live-context/route.ts", "app/external-context-sources.ts"],
    handles: ["Census", "USGS", "NOAA", "NWS", "Raspberry Shake"],
    verification: ["tests/rendered-html.test.mjs", "fixed route allowlists", "source-state readback"],
  },
  {
    id: "hydrology-adapters",
    title: "Hydrology adapters and River Pulse",
    role: "Owns separated USGS, NWPS, and NWM observation/forecast/model clocks and gap-aware display behavior.",
    paths: ["app/streamflow.ts", "app/noaa-hydrology.ts", "app/hydrology-observatory.tsx", "app/api/hydrology/streamflow/route.ts", "app/api/hydrology/noaa/route.ts"],
    handles: ["bounded station queries", "range controls", "exact observations", "no interpolation"],
    verification: ["tests/streamflow.test.mjs", "tests/rendered-html.test.mjs"],
  },
  {
    id: "event-observatory",
    title: "Historical event observatory",
    role: "Owns dated manifests, actual provider frames, interval boundaries, and historical replay separation.",
    paths: ["app/event-atlas.ts", "app/observatory/workspace.tsx", "app/api/event-atlas", "app/noaa-radar.ts", "app/api/noaa-radar/frames/route.ts"],
    handles: ["radar frame discovery", "smoke interval manifests", "source coverage", "replay links"],
    verification: ["tests/event-atlas.test.mjs", "tests/noaa-radar.test.mjs"],
  },
  {
    id: "evidence-and-workspaces",
    title: "Evidence, Focus, and workspace handoffs",
    role: "Keeps selection, evidence policy, bounded Focus results, reports, stories, and device-local drafts coherent.",
    paths: ["app/workspace-model.ts", "app/runtime-seam.ts", "app/focus-mode.ts", "app/report-story-workspaces.tsx", "app/export-center.ts", "app/workspace-storage.ts"],
    handles: ["trust posture", "abstention", "public-safe export", "local persistence"],
    verification: ["tests/snapshot-workflows.test.mjs", "tests/rendered-html.test.mjs"],
  },
  {
    id: "registry-and-alignment",
    title: "Feature, connection, action, and alignment registry",
    role: "Makes the Site's product surface and external boundaries machine-readable for UI, tests, and documentation alignment.",
    paths: ["app/site-features.ts", "app/site-connections.ts", "app/site-actions.ts", "app/site-architecture.ts", "app/site-registry.ts"],
    handles: ["feature ownership", "connection inventory", "action contracts", "code paths", "validation"],
    verification: ["tests/rendered-html.test.mjs", "site registry validation", "GitHub/Drive/Notion handoff"],
  },
  {
    id: "documentation-and-gaps",
    title: "Documentation, gaps, and source observatory",
    role: "Records what is implemented, held, external-only, or awaiting source/lineage/release review.",
    paths: ["README.md", "docs/SITE_FEATURE_CONNECTION_ACTION_MAP.md", "docs/KFM_SOURCE_GAP_REGISTER.md", "app/source-intelligence.ts", "app/observatory/sources/page.tsx"],
    handles: ["source roles", "next gates", "provider links", "alignment evidence"],
    verification: ["GitHub architecture docs", "Google Drive handoff", "Notion coordination page"],
  },
] as const satisfies readonly SiteCodeSurfaceRecord[]);

export type SiteCodeSurfaceId = (typeof SITE_CODE_SURFACES)[number]["id"];

export const SITE_ROUTE_CONTRACTS = Object.freeze([
  { id: "data-intake-route", route: "/api/data-submissions", owner: "app/api/data-submissions/route.ts", purpose: "Authenticated bounded uploads and scoped submission lists.", trustBoundary: "No anonymous intake or public candidate reads. Source/rights/sensitivity metadata accompanies immutable uploaded bytes." },
  { id: "data-review-route", route: "/api/data-submissions/:id", owner: "app/api/data-submissions/[id]/route.ts", purpose: "Private download, detail, and version-checked steward decisions.", trustBoundary: "Contributor ownership or server-authorized steward for reads; steward and matching version for writes. Review never activates a layer." },
  { id: "source-download-route", route: "/api/source-download", owner: "app/api/source-download/route.ts", purpose: "Download bounded real source snapshots with dates and provenance.", trustBoundary: "Fixed source allowlist, no arbitrary URL and no candidate-data access." },
  {
    id: "explorer-route",
    route: "/",
    owner: "app/page.tsx",
    purpose: "Map-first investigation, visible layer and official-context controls, evidence drawer, and workbench handoffs.",
    trustBoundary: "Site-local demonstration layers and external operational context stay distinct from released KFM evidence.",
  },
  {
    id: "event-observatory-route",
    route: "/observatory",
    owner: "app/observatory/workspace.tsx",
    purpose: "Date-bound replay of exact provider artifacts and coverage states.",
    trustBoundary: "Historical replay does not freeze provider revisions or become an emergency/warning surface.",
  },
  {
    id: "source-observatory-route",
    route: "/observatory/sources",
    owner: "app/observatory/sources/page.tsx",
    purpose: "Source research, provider identity, implementation readiness, and gap disclosure.",
    trustBoundary: "Discovery and documented access are not activation, admission, release, or publication.",
  },
  {
    id: "live-context-route",
    route: "/api/live-context",
    owner: "app/api/live-context/route.ts",
    purpose: "Allowlisted bounded GeoJSON context feeds for selected official sources.",
    trustBoundary: "Unknown feeds and arbitrary upstream URLs are rejected; response failures remain explicit.",
  },
  {
    id: "hydrology-routes",
    route: "/api/hydrology/*",
    owner: "app/api/hydrology/",
    purpose: "Bounded USGS/NWPS/NWM adapter surfaces for network, station, gauge, and reach context.",
    trustBoundary: "Observation, forecast, and model roles remain separate, and no values are interpolated or generalized.",
  },
] as const satisfies readonly SiteRouteContract[]);

export type SiteRouteContractId = (typeof SITE_ROUTE_CONTRACTS)[number]["id"];
