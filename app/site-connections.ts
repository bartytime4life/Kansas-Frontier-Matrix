import type { OfficialContextFeedId, OfficialContextId } from "./live-context";
import { OFFICIAL_CONTEXT_SOURCES } from "./live-context";
import type { SiteActionId } from "./site-actions";

export type SiteConnectionKind = "GEOJSON_FEED" | "ADAPTER_FEED" | "WMS_RASTER";
export type SiteConnectionStatus = "ACTIVE_CONTEXT" | "DISPLAY_CONTEXT";

export type SiteConnectionRecord = Readonly<{
  id: OfficialContextId;
  title: string;
  organization: string;
  domain: string;
  kind: SiteConnectionKind;
  status: SiteConnectionStatus;
  role: "EXTERNAL_CONTEXT_ONLY";
  endpoint: string;
  feed: OfficialContextFeedId | null;
  sourceUrl: string;
  serviceUrl: string;
  freshness: string;
  codePaths: readonly string[];
  actionIds: readonly SiteActionId[];
  boundary: string;
}>;

/** Standard live-context feeds are implemented in these files. */
const STANDARD_FEED_CODE_PATHS: readonly string[] = ["app/live-context.ts", "app/api/live-context/route.ts", "app/page.tsx"];
/** Code paths for every source that is not a standard live-context feed. */
export const CONNECTION_CODE_PATHS: Partial<Record<OfficialContextId, readonly string[]>> = {
  "census-congress-119": ["app/civic-districts.ts", "app/civic-history.ts", "app/api/live-context/civic-districts.ts", "app/api/live-context/civic-history.ts", "app/api/live-context/route.ts", "app/live-context.ts", "app/page.tsx"],
  "deflock-alpr": ["app/deflock.ts", "app/api/live-context/deflock.ts", "app/api/live-context/route.ts", "app/live-context.ts", "app/page.tsx"],
"kgs-aquifer-alluvial": ["app/aquifer-layers.ts", "app/live-context.ts", "app/page.tsx"],
"kgs-aquifer-dakota": ["app/aquifer-layers.ts", "app/live-context.ts", "app/page.tsx"],
"kgs-aquifer-glacial-drift": ["app/aquifer-layers.ts", "app/live-context.ts", "app/page.tsx"],
"kgs-aquifer-high-plains": ["app/aquifer-layers.ts", "app/live-context.ts", "app/page.tsx"],
"kgs-aquifer-ozark": ["app/aquifer-layers.ts", "app/live-context.ts", "app/page.tsx"],
"kgs-aquifer-osage": ["app/aquifer-layers.ts", "app/live-context.ts", "app/page.tsx"],
"kgs-aquifer-flint-hills": ["app/aquifer-layers.ts", "app/live-context.ts", "app/page.tsx"],
"kgs-water-table": ["app/aquifer-layers.ts", "app/live-context.ts", "app/page.tsx"],
"kgs-saturated-thickness": ["app/aquifer-layers.ts", "app/live-context.ts", "app/page.tsx"],
"kgs-depth-to-water": ["app/aquifer-layers.ts", "app/live-context.ts", "app/page.tsx"],
"kgs-monitoring-wells": ["app/aquifer-layers.ts", "app/live-context.ts", "app/page.tsx"],

  "kdot-bridges-state": ["app/kansas-reference-layers.ts", "app/kdot-bridges.ts", "app/api/live-context/kdot-bridges.ts", "app/api/bridge-detail/route.ts", "app/live-context.ts", "app/page.tsx"],
  "kdot-bridges-local": ["app/kansas-reference-layers.ts", "app/kdot-bridges.ts", "app/api/live-context/kdot-bridges.ts", "app/api/bridge-detail/route.ts", "app/live-context.ts", "app/page.tsx"],
  "kdot-bridges-historic": ["app/kansas-reference-layers.ts", "app/kdot-bridges.ts", "app/api/live-context/kdot-bridges.ts", "app/api/bridge-detail/route.ts", "app/live-context.ts", "app/page.tsx"],
  "kdot-bridges-old": ["app/kansas-reference-layers.ts", "app/kdot-bridges.ts", "app/api/live-context/kdot-bridges.ts", "app/api/bridge-detail/route.ts", "app/live-context.ts", "app/page.tsx"],
  "kdot-bridges-closed": ["app/kansas-reference-layers.ts", "app/kdot-bridges.ts", "app/api/live-context/kdot-bridges.ts", "app/api/bridge-detail/route.ts", "app/live-context.ts", "app/page.tsx"],
  "kdot-roads-1918": ["app/kansas-reference-layers.ts", "app/live-context.ts", "app/page.tsx"],
  "kdot-roads": ["app/kansas-reference-layers.ts", "app/live-context.ts", "app/page.tsx"],
  "kdot-rail-active": ["app/kansas-reference-layers.ts", "app/live-context.ts", "app/page.tsx"],
  "kdot-rail-abandoned": ["app/kansas-reference-layers.ts", "app/live-context.ts", "app/page.tsx"],
  "fema-flood-zones": ["app/kansas-reference-layers.ts", "app/live-context.ts", "app/page.tsx"],

  "fema-disaster-declarations": ["app/fema-declarations.ts", "app/api/live-context/route.ts", "app/live-context.ts", "app/page.tsx"],
  "blm-plss-townships": ["app/live-context.ts", "app/blm-plss-records.ts", "app/api/blm-plss-records/route.ts", "app/blm-plss-inspector.tsx", "app/page.tsx"],
  "blm-plss-sections": ["app/live-context.ts", "app/blm-plss-records.ts", "app/api/blm-plss-records/route.ts", "app/blm-plss-inspector.tsx", "app/page.tsx"],
  "blm-plss-intersected": ["app/live-context.ts", "app/blm-plss-records.ts", "app/api/blm-plss-records/route.ts", "app/blm-plss-inspector.tsx", "app/page.tsx"],
  "blm-mlrs-leases-authorized": ["app/kansas-reference-layers.ts", "app/live-context.ts", "app/page.tsx"],
  "blm-mlrs-leases-closed": ["app/kansas-reference-layers.ts", "app/live-context.ts", "app/page.tsx"],
  "usgs-streamflow": ["app/live-context.ts", "app/streamflow.ts", "app/hydrology-observatory.tsx", "app/api/hydrology/streamflow/route.ts"],
  "noaa-nwps-gauges": ["app/live-context.ts", "app/noaa-hydrology.ts", "app/hydrology-observatory.tsx", "app/api/hydrology/noaa/route.ts"],
  "usgs-3dhp-hydrography": ["app/live-context.ts", "app/map-runtime.ts", "app/page.tsx"],
  "usgs-wbd-watersheds": ["app/live-context.ts", "app/map-runtime.ts", "app/page.tsx"],
  "noaa-nwm-analysis": ["app/live-context.ts", "app/noaa-hydrology.ts", "app/api/hydrology/noaa/route.ts"],
  "noaa-nwm-short-range": ["app/live-context.ts", "app/noaa-hydrology.ts", "app/api/hydrology/noaa/route.ts"],
  "noaa-hms-smoke": ["app/live-context.ts", "app/api/live-context/route.ts", "app/event-atlas.ts", "app/page.tsx"],
  "nasa-firms-active-fire": ["app/live-context.ts", "app/map-runtime.ts", "app/page.tsx"],
  "nasa-gibs-fire-points": ["app/live-context.ts", "app/api/live-context/route.ts", "app/evidence-drawer-data.ts", "app/page.tsx"],
  "nifc-fire-reports": ["app/live-context.ts", "app/api/live-context/route.ts", "app/fire-report-analysis.ts", "app/evidence-drawer-data.ts", "app/page.tsx"],
  "noaa-goes-geocolor": ["app/live-context.ts", "app/noaa-satellite.ts", "app/api/noaa-satellite/frames/route.ts", "app/page.tsx"],
  "usgs-3dep-hillshade": ["app/live-context.ts", "app/terrain-sources.ts", "app/map-runtime.ts", "app/page.tsx"],
  "usgs-3dep-slope": ["app/live-context.ts", "app/terrain-sources.ts", "app/map-runtime.ts", "app/page.tsx"],
  "nws-radar": ["app/live-context.ts", "app/noaa-radar.ts", "app/api/noaa-radar/frames/route.ts", "app/page.tsx"],
  "nws-forecast-wind": ["app/live-context.ts", "app/airflow-tiles.ts", "app/api/airflow-tile/route.ts", "app/wind-arrow-data.ts", "app/wind-flow-client.ts", "app/wind-arrow-canvas.ts", "app/api/wind-arrows/route.ts", "app/page.tsx"],
  "noaa-lightning-density": ["app/live-context.ts", "app/lightning-data.ts", "app/lightning-server.ts", "app/api/lightning/frames/route.ts", "app/api/lightning/tiles/[frame]/[z]/[x]/[y]/route.ts", "app/page.tsx"],
  "nasa-lightning-climatology": ["app/live-context.ts", "app/lightning-data.ts", "app/page.tsx"],
  "noaa-spc-fire-weather": ["app/kansas-discovery-layers.ts", "app/live-context.ts", "app/page.tsx"],
  "noaa-cpc-drought-outlook": ["app/kansas-discovery-layers.ts", "app/live-context.ts", "app/page.tsx"],
  "usgs-padus-lands": ["app/kansas-discovery-layers.ts", "app/live-context.ts", "app/page.tsx"],
  "nps-nrhp-places": ["app/live-context.ts", "app/api/live-context/route.ts", "app/evidence-drawer-data.ts", "app/page.tsx"],
  "nrcs-ssurgo-soils": ["app/kansas-discovery-layers.ts", "app/live-context.ts", "app/page.tsx"],
  "kdwp-wildlife-areas": ["app/live-context.ts", "app/api/live-context/route.ts", "app/evidence-drawer-data.ts", "app/page.tsx"],
  "kdwp-wiha-access": ["app/live-context.ts", "app/api/live-context/route.ts", "app/evidence-drawer-data.ts", "app/page.tsx"],
  "nps-historic-trails": ["app/live-context.ts", "app/api/live-context/route.ts", "app/evidence-drawer-data.ts", "app/page.tsx"],
  "nps-trail-places": ["app/live-context.ts", "app/api/live-context/route.ts", "app/evidence-drawer-data.ts", "app/page.tsx"],
};

// A test requires an explicit entry for every non-feed source; the fallback only keeps the manifest renderable.
const connectionCodePaths = (source: (typeof OFFICIAL_CONTEXT_SOURCES)[number]): readonly string[] =>
  CONNECTION_CODE_PATHS[source.id] ?? (source.apiPath ? STANDARD_FEED_CODE_PATHS : ["app/live-context.ts"]);

/** Adapter-backed feeds; every other feed is read from the source's own apiPath. */
const ADAPTER_FEEDS: Partial<Record<OfficialContextId, OfficialContextFeedId>> = {
  "usgs-streamflow": "usgs-streamflow",
  "noaa-nwps-gauges": "noaa-nwps-gauges",
};

const connectionFeed = (source: (typeof OFFICIAL_CONTEXT_SOURCES)[number]): OfficialContextFeedId | null =>
  ADAPTER_FEEDS[source.id] ?? (source.apiPath?.match(/[?&]feed=([a-z0-9-]+)/)?.[1] as OfficialContextFeedId | undefined) ?? null;

const STANDARD_ACTIONS: readonly SiteActionId[] = ["toggle-context-connection", "set-context-opacity", "open-provider-source"];
const FEED_ACTIONS: readonly SiteActionId[] = ["toggle-context-connection", "refresh-visible-context", "set-context-opacity", "open-provider-source"];
/** Sources with tools beyond show, refresh (feeds only), opacity and provider link. */
const CONNECTION_ACTION_OVERRIDES: Partial<Record<OfficialContextId, readonly SiteActionId[]>> = {
  "blm-plss-townships": ["toggle-context-connection", "set-context-opacity", "inspect-plss-identifiers", "open-provider-source"],
  "blm-plss-sections": ["toggle-context-connection", "set-context-opacity", "inspect-plss-identifiers", "open-provider-source"],
  "blm-plss-intersected": ["toggle-context-connection", "set-context-opacity", "inspect-plss-identifiers", "open-provider-source"],
  "usgs-streamflow": ["toggle-context-connection", "refresh-visible-context", "refresh-streamflow", "change-hydrology-range", "step-exact-observation", "set-context-opacity", "open-provider-source"],
  "noaa-nwps-gauges": ["toggle-context-connection", "refresh-visible-context", "change-hydrology-range", "set-context-opacity", "open-provider-source"],
  "noaa-nwm-analysis": ["toggle-context-connection", "refresh-visible-context", "set-context-opacity", "open-provider-source"],
  "noaa-nwm-short-range": ["toggle-context-connection", "refresh-visible-context", "set-context-opacity", "open-provider-source"],
  "noaa-hms-smoke": ["toggle-context-connection", "refresh-visible-context", "step-exact-observation", "set-context-opacity", "open-provider-source"],
  "noaa-goes-geocolor": ["toggle-context-connection", "refresh-visible-context", "step-exact-observation", "set-context-opacity", "open-provider-source"],
  "nws-radar": ["toggle-context-connection", "refresh-radar-frames", "play-exact-radar-loop", "step-exact-observation", "set-context-opacity", "open-provider-source"],
  "noaa-lightning-density": ["toggle-context-connection", "refresh-visible-context", "step-exact-observation", "set-context-opacity", "open-provider-source"],
};

const connectionActions = (source: (typeof OFFICIAL_CONTEXT_SOURCES)[number]): readonly SiteActionId[] =>
  CONNECTION_ACTION_OVERRIDES[source.id] ?? (connectionFeed(source) ? FEED_ACTIONS : STANDARD_ACTIONS);

const connectionKind = (source: (typeof OFFICIAL_CONTEXT_SOURCES)[number]): SiteConnectionKind => {
  if (source.apiPath || source.kind === "SNAPSHOT_GEOJSON") return "GEOJSON_FEED";
  if (source.managedAdapterPath) return "ADAPTER_FEED";
  return "WMS_RASTER";
};

const connectionEndpoint = (source: (typeof OFFICIAL_CONTEXT_SOURCES)[number]): string => source.apiPath ?? source.managedAdapterPath ?? source.mapUrl ?? source.endpointLabel;

/** Normalized connection manifest derived from the existing official source allowlist. */
export const SITE_CONNECTIONS = Object.freeze(
  OFFICIAL_CONTEXT_SOURCES.map((source) => Object.freeze({
    id: source.id,
    title: source.title,
    organization: source.organization,
    domain: source.domain,
    kind: connectionKind(source),
    status: source.kind === "OPERATIONAL_WMS" || source.kind === "HISTORICAL_RASTER" ? "DISPLAY_CONTEXT" : "ACTIVE_CONTEXT",
    role: source.evidenceRole,
    endpoint: connectionEndpoint(source),
    feed: connectionFeed(source),
    sourceUrl: source.sourceUrl,
    serviceUrl: source.serviceUrl,
    freshness: source.freshness,
    codePaths: connectionCodePaths(source),
    actionIds: connectionActions(source),
    boundary: source.boundary,
  })),
) as readonly SiteConnectionRecord[];

export const SITE_CONNECTION_BY_ID = Object.freeze(
  Object.fromEntries(SITE_CONNECTIONS.map((connection) => [connection.id, connection])) as Record<OfficialContextId, SiteConnectionRecord>,
);
