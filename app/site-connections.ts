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

const CONNECTION_CODE_PATHS: Record<OfficialContextId, readonly string[]> = {
  "census-counties": ["app/live-context.ts", "app/api/live-context/route.ts", "app/page.tsx"],
  "usgs-streamflow": ["app/live-context.ts", "app/streamflow.ts", "app/hydrology-observatory.tsx", "app/api/hydrology/streamflow/route.ts"],
  "noaa-nwps-gauges": ["app/live-context.ts", "app/noaa-hydrology.ts", "app/hydrology-observatory.tsx", "app/api/hydrology/noaa/route.ts"],
  "usgs-3dhp-hydrography": ["app/live-context.ts", "app/map-runtime.ts", "app/page.tsx"],
  "usgs-wbd-watersheds": ["app/live-context.ts", "app/map-runtime.ts", "app/page.tsx"],
  "noaa-nwm-analysis": ["app/live-context.ts", "app/noaa-hydrology.ts", "app/api/hydrology/noaa/route.ts"],
  "noaa-nwm-short-range": ["app/live-context.ts", "app/noaa-hydrology.ts", "app/api/hydrology/noaa/route.ts"],
  "usgs-earthquakes": ["app/live-context.ts", "app/api/live-context/route.ts", "app/page.tsx"],
  "noaa-hms-smoke": ["app/live-context.ts", "app/api/live-context/route.ts", "app/event-atlas.ts", "app/page.tsx"],
  "raspberry-shake-stations": ["app/live-context.ts", "app/api/live-context/route.ts", "app/page.tsx"],
  "usgs-3dep-hillshade": ["app/live-context.ts", "app/terrain-sources.ts", "app/map-runtime.ts", "app/page.tsx"],
  "usgs-3dep-slope": ["app/live-context.ts", "app/terrain-sources.ts", "app/map-runtime.ts", "app/page.tsx"],
  "nws-alerts": ["app/live-context.ts", "app/api/live-context/route.ts", "app/page.tsx"],
  "nws-radar": ["app/live-context.ts", "app/noaa-radar.ts", "app/api/noaa-radar/frames/route.ts", "app/page.tsx"],
};

const CONNECTION_FEEDS: Partial<Record<OfficialContextId, OfficialContextFeedId>> = {
  "census-counties": "census-counties",
  "usgs-streamflow": "usgs-streamflow",
  "noaa-nwps-gauges": "noaa-nwps-gauges",
  "usgs-earthquakes": "usgs-earthquakes",
  "noaa-hms-smoke": "noaa-hms-smoke",
  "raspberry-shake-stations": "raspberry-shake-stations",
  "nws-alerts": "nws-alerts",
};

const CONNECTION_ACTIONS: Record<OfficialContextId, readonly SiteActionId[]> = {
  "census-counties": ["toggle-context-connection", "refresh-visible-context", "set-context-opacity", "open-provider-source"],
  "usgs-streamflow": ["toggle-context-connection", "refresh-visible-context", "refresh-streamflow", "change-hydrology-range", "step-exact-observation", "set-context-opacity", "open-provider-source"],
  "noaa-nwps-gauges": ["toggle-context-connection", "refresh-visible-context", "change-hydrology-range", "set-context-opacity", "open-provider-source"],
  "usgs-3dhp-hydrography": ["toggle-context-connection", "set-context-opacity", "open-provider-source"],
  "usgs-wbd-watersheds": ["toggle-context-connection", "set-context-opacity", "open-provider-source"],
  "noaa-nwm-analysis": ["toggle-context-connection", "refresh-visible-context", "set-context-opacity", "open-provider-source"],
  "noaa-nwm-short-range": ["toggle-context-connection", "refresh-visible-context", "set-context-opacity", "open-provider-source"],
  "usgs-earthquakes": ["toggle-context-connection", "refresh-visible-context", "set-context-opacity", "open-provider-source"],
  "noaa-hms-smoke": ["toggle-context-connection", "refresh-visible-context", "step-exact-observation", "set-context-opacity", "open-provider-source"],
  "raspberry-shake-stations": ["toggle-context-connection", "refresh-visible-context", "set-context-opacity", "open-provider-source"],
  "usgs-3dep-hillshade": ["toggle-context-connection", "set-context-opacity", "open-provider-source"],
  "usgs-3dep-slope": ["toggle-context-connection", "set-context-opacity", "open-provider-source"],
  "nws-alerts": ["toggle-context-connection", "refresh-visible-context", "set-context-opacity", "open-provider-source"],
  "nws-radar": ["toggle-context-connection", "refresh-radar-frames", "play-exact-radar-loop", "step-exact-observation", "set-context-opacity", "open-provider-source"],
};

const connectionKind = (source: (typeof OFFICIAL_CONTEXT_SOURCES)[number]): SiteConnectionKind => {
  if (source.apiPath) return "GEOJSON_FEED";
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
    status: source.kind === "OPERATIONAL_WMS" ? "DISPLAY_CONTEXT" : "ACTIVE_CONTEXT",
    role: source.evidenceRole,
    endpoint: connectionEndpoint(source),
    feed: CONNECTION_FEEDS[source.id] ?? null,
    sourceUrl: source.sourceUrl,
    serviceUrl: source.serviceUrl,
    freshness: source.freshness,
    codePaths: CONNECTION_CODE_PATHS[source.id],
    actionIds: CONNECTION_ACTIONS[source.id],
    boundary: source.boundary,
  })),
) as readonly SiteConnectionRecord[];

export const SITE_CONNECTION_BY_ID = Object.freeze(
  Object.fromEntries(SITE_CONNECTIONS.map((connection) => [connection.id, connection])) as Record<OfficialContextId, SiteConnectionRecord>,
);
