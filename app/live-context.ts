import type { FeatureCollection } from "geojson";
import type { GeoJSONSource, LayerSpecification, Map as MapLibreMap } from "maplibre-gl";

export type OfficialContextId = "census-counties" | "usgs-streamflow" | "usgs-3dep-hillshade" | "nws-alerts" | "nws-radar";
export type OfficialContextFeedId = "census-counties" | "usgs-streamflow" | "nws-alerts";
export type OfficialContextState = "idle" | "loading" | "ready" | "empty" | "partial" | "error";

export type OfficialContextPayload = Readonly<{
  feed: OfficialContextFeedId;
  state: "ready" | "empty" | "partial";
  retrievedAt: string;
  upstreamUpdatedAt: string | null;
  featureCount: number;
  data: FeatureCollection;
  source: string;
  limitation: string;
  truncated: boolean;
}>;

export type OfficialContextSource = Readonly<{
  id: OfficialContextId;
  title: string;
  shortTitle: string;
  organization: string;
  domain: string;
  kind: "SNAPSHOT_GEOJSON" | "OPERATIONAL_GEOJSON" | "OPERATIONAL_WMS";
  sourceId: string;
  layerIds: readonly string[];
  interactiveLayerIds: readonly string[];
  apiPath?: `/api/live-context?feed=${OfficialContextFeedId}`;
  mapUrl?: string;
  endpointLabel: string;
  sourceUrl: string;
  serviceUrl: string;
  cadence: string;
  freshness: string;
  defaultVisibility: boolean;
  defaultOpacity: number;
  color: string;
  attribution: string;
  evidenceRole: "EXTERNAL_CONTEXT_ONLY";
  boundary: string;
  fallback: string;
}>;

/** Fixed allowlist of public, official context. These sources never enter KFM evidence, reports, exports, or admission state. */
export const OFFICIAL_CONTEXT_SOURCES: readonly OfficialContextSource[] = Object.freeze([
  Object.freeze({
    id: "census-counties",
    title: "Census 2026 Kansas county boundaries",
    shortTitle: "County boundaries",
    organization: "U.S. Census Bureau",
    domain: "Boundaries & places",
    kind: "SNAPSHOT_GEOJSON",
    sourceId: "external-census-counties",
    layerIds: Object.freeze(["external-census-counties-fill", "external-census-counties-line"]),
    interactiveLayerIds: Object.freeze(["external-census-counties-fill"]),
    apiPath: "/api/live-context?feed=census-counties",
    endpointLabel: "tigerweb.geo.census.gov · State_County (1)",
    sourceUrl: "https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/State_County/MapServer/1",
    serviceUrl: "https://tigerweb.geo.census.gov/tigerwebmain/TIGERweb_main.html",
    cadence: "Current TIGERweb service; pinned 2026 vintage in this adapter",
    freshness: "Jan. 1, 2026 vintage",
    defaultVisibility: true,
    defaultOpacity: 0.72,
    color: "#8fd8d0",
    attribution: "U.S. Census Bureau TIGERweb",
    evidenceRole: "EXTERNAL_CONTEXT_ONLY",
    boundary: "Official county geometry is fetched through a fixed, Kansas-only adapter. It is not a KFM release, historical boundary authority, parcel layer, or claim-bearing EvidenceBundle.",
    fallback: "If Census TIGERweb is unavailable, the overlay reports an error and remains empty; no substitute boundary is presented as equivalent.",
  }),
  Object.freeze({
    id: "usgs-streamflow",
    title: "USGS current Kansas streamflow observations",
    shortTitle: "Current streamflow",
    organization: "U.S. Geological Survey",
    domain: "Living waters",
    kind: "OPERATIONAL_GEOJSON",
    sourceId: "external-usgs-streamflow",
    layerIds: Object.freeze(["external-usgs-streamflow-points"]),
    interactiveLayerIds: Object.freeze(["external-usgs-streamflow-points"]),
    apiPath: "/api/live-context?feed=usgs-streamflow",
    endpointLabel: "api.waterdata.usgs.gov · latest-continuous",
    sourceUrl: "https://api.waterdata.usgs.gov/ogcapi/v0/collections/latest-continuous",
    serviceUrl: "https://api.waterdata.usgs.gov/ogcapi/v0/",
    cadence: "Upstream latest-value collection; refreshed on demand",
    freshness: "Most recent values in the past 24 hours",
    defaultVisibility: true,
    defaultOpacity: 0.92,
    color: "#55d9ec",
    attribution: "U.S. Geological Survey Water Data APIs",
    evidenceRole: "EXTERNAL_CONTEXT_ONLY",
    boundary: "Values are current-awareness context and may be provisional, delayed, revised, or incomplete. They are not flood warnings, certified statistics, admitted KFM observations, or an all-stations inventory.",
    fallback: "A timeout, malformed response, or upstream error becomes an explicit unavailable state; the Site never converts it into zero flow or a statewide all-clear.",
  }),
  Object.freeze({
    id: "usgs-3dep-hillshade",
    title: "USGS 3DEP multidirectional hillshade",
    shortTitle: "3DEP hillshade",
    organization: "U.S. Geological Survey",
    domain: "Terrain & landforms",
    kind: "OPERATIONAL_WMS",
    sourceId: "external-usgs-3dep-hillshade",
    layerIds: Object.freeze(["external-usgs-3dep-hillshade-raster"]),
    interactiveLayerIds: Object.freeze([]),
    mapUrl: "https://elevation.nationalmap.gov/arcgis/rest/services/3DEPElevation/ImageServer/exportImage?bbox={bbox-epsg-3857}&bboxSR=3857&imageSR=3857&size=256%2C256&format=png32&renderingRule=%7B%22rasterFunction%22%3A%22Hillshade%20Multidirectional%22%7D&f=image",
    endpointLabel: "elevation.nationalmap.gov · 3DEPElevation",
    sourceUrl: "https://elevation.nationalmap.gov/arcgis/rest/services/3DEPElevation/ImageServer",
    serviceUrl: "https://www.usgs.gov/3d-elevation-program",
    cadence: "USGS seamless service; provider-controlled refresh",
    freshness: "Current published 3DEP service mosaic",
    defaultVisibility: false,
    defaultOpacity: 0.46,
    color: "#d7c7a0",
    attribution: "USGS 3D Elevation Program",
    evidenceRole: "EXTERNAL_CONTEXT_ONLY",
    boundary: "The service renders a hillshade image from 3DEP. It is not a native raster-dem terrain source, point-elevation answer, pinned source tile, datum assertion, accuracy certificate, or admitted KFM elevation artifact.",
    fallback: "Slow or failed image-service tiles remain transparent. The existing 2D map and Terrarium display terrain remain available without substituting a numeric 3DEP claim.",
  }),
  Object.freeze({
    id: "nws-alerts",
    title: "NWS active Kansas alert areas",
    shortTitle: "Active alert areas",
    organization: "NOAA National Weather Service",
    domain: "Weather & hazards",
    kind: "OPERATIONAL_GEOJSON",
    sourceId: "external-nws-alerts",
    layerIds: Object.freeze(["external-nws-alerts-fill", "external-nws-alerts-line"]),
    interactiveLayerIds: Object.freeze(["external-nws-alerts-fill"]),
    apiPath: "/api/live-context?feed=nws-alerts",
    endpointLabel: "api.weather.gov · active?area=KS",
    sourceUrl: "https://www.weather.gov/documentation/services-web-api",
    serviceUrl: "https://api.weather.gov/alerts/active?area=KS",
    cadence: "Upstream active-alert collection; refreshed on demand",
    freshness: "Active alert snapshot at retrieval time",
    defaultVisibility: false,
    defaultOpacity: 0.34,
    color: "#ef7b61",
    attribution: "NOAA National Weather Service",
    evidenceRole: "EXTERNAL_CONTEXT_ONLY",
    boundary: "Alert polygons are assembled from the NWS affected-zone links returned with active Kansas alerts. This is situational context—not an emergency service, warning delivery guarantee, KFM release, or proof that no hazard exists.",
    fallback: "Any alert or zone lookup failure is shown as unavailable or partial. Zero returned features is time-stamped and never labeled safe or all-clear.",
  }),
  Object.freeze({
    id: "nws-radar",
    title: "NWS/NCEP current CONUS radar reflectivity",
    shortTitle: "Current radar",
    organization: "NOAA National Weather Service / NCEP",
    domain: "Weather & hazards",
    kind: "OPERATIONAL_WMS",
    sourceId: "external-nws-radar",
    layerIds: Object.freeze(["external-nws-radar-raster"]),
    interactiveLayerIds: Object.freeze([]),
    mapUrl: "https://opengeo.ncep.noaa.gov/geoserver/conus/conus_bref_qcd/ows?service=WMS&version=1.1.1&request=GetMap&layers=conus_bref_qcd&styles=&bbox={bbox-epsg-3857}&width=256&height=256&srs=EPSG:3857&format=image/png&transparent=true",
    endpointLabel: "opengeo.ncep.noaa.gov · conus_bref_qcd",
    sourceUrl: "https://www.weather.gov/gis/cloudgiswebservices",
    serviceUrl: "https://opengeo.ncep.noaa.gov/geoserver/conus/conus_bref_qcd/ows",
    cadence: "Operational WMS tiles; provider-controlled refresh",
    freshness: "Current mosaic as labeled by the upstream service",
    defaultVisibility: false,
    defaultOpacity: 0.68,
    color: "#f2c14e",
    attribution: "NOAA/NWS/NCEP OpenGeo",
    evidenceRole: "EXTERNAL_CONTEXT_ONLY",
    boundary: "Radar is a visual operational mosaic. The Site does not resolve sweep time, beam blockage, quality flags, precipitation rate, forecast, warning status, or KFM evidence support from these pixels.",
    fallback: "Failed WMS tiles remain transparent and the status stays provider-dependent; users should consult official NWS products for decisions.",
  }),
]);

export const OFFICIAL_CONTEXT_BY_ID = Object.freeze(Object.fromEntries(OFFICIAL_CONTEXT_SOURCES.map((source) => [source.id, source])) as Record<OfficialContextId, OfficialContextSource>);
export const OFFICIAL_CONTEXT_BY_SOURCE_ID = Object.freeze(Object.fromEntries(OFFICIAL_CONTEXT_SOURCES.map((source) => [source.sourceId, source])) as Record<string, OfficialContextSource>);
export const OFFICIAL_CONTEXT_INTERACTIVE_LAYER_IDS = Object.freeze(OFFICIAL_CONTEXT_SOURCES.flatMap((source) => source.interactiveLayerIds));

export const defaultOfficialContextVisibility = (): Record<OfficialContextId, boolean> => Object.fromEntries(OFFICIAL_CONTEXT_SOURCES.map((source) => [source.id, source.defaultVisibility])) as Record<OfficialContextId, boolean>;
export const defaultOfficialContextOpacity = (): Record<OfficialContextId, number> => Object.fromEntries(OFFICIAL_CONTEXT_SOURCES.map((source) => [source.id, source.defaultOpacity])) as Record<OfficialContextId, number>;

const emptyCollection = (): FeatureCollection => ({ type: "FeatureCollection", features: [] });
const firstRegistryLayer = (map: MapLibreMap) => map.getStyle().layers?.find((layer) => layer.id.startsWith("kfm-") && layer.id !== "kfm-background")?.id;
const ensureGeoJsonSource = (map: MapLibreMap, source: OfficialContextSource, data: FeatureCollection) => {
  const existing = map.getSource(source.sourceId) as GeoJSONSource | undefined;
  if (existing) existing.setData(data);
  else map.addSource(source.sourceId, { type: "geojson", data, promoteId: "featureId", attribution: source.attribution });
};
const ensureLayer = (map: MapLibreMap, specification: LayerSpecification, beforeId?: string) => {
  if (!map.getLayer(specification.id)) map.addLayer(specification, beforeId);
};

export const applyOfficialContextState = (
  map: MapLibreMap,
  visibility: Record<OfficialContextId, boolean>,
  opacity: Record<OfficialContextId, number>,
  payloads: Partial<Record<OfficialContextFeedId, OfficialContextPayload>>,
) => {
  const county = OFFICIAL_CONTEXT_BY_ID["census-counties"];
  ensureGeoJsonSource(map, county, payloads["census-counties"]?.data ?? emptyCollection());
  ensureLayer(map, { id: county.layerIds[0], type: "fill", source: county.sourceId, paint: { "fill-color": county.color, "fill-opacity": 0.05 } });
  ensureLayer(map, { id: county.layerIds[1], type: "line", source: county.sourceId, paint: { "line-color": county.color, "line-width": ["interpolate", ["linear"], ["zoom"], 4, 0.7, 10, 2.1], "line-opacity": 0.72 } });

  const streamflow = OFFICIAL_CONTEXT_BY_ID["usgs-streamflow"];
  ensureGeoJsonSource(map, streamflow, payloads["usgs-streamflow"]?.data ?? emptyCollection());
  ensureLayer(map, { id: streamflow.layerIds[0], type: "circle", source: streamflow.sourceId, paint: {
    "circle-color": ["case", ["==", ["get", "approvalStatus"], "Approved"], "#5fe1b0", streamflow.color],
    "circle-radius": ["interpolate", ["linear"], ["zoom"], 4, 3.5, 10, 7.5, 14, 11],
    "circle-opacity": 0.92, "circle-stroke-color": "#07171a", "circle-stroke-width": 1.6,
  } });

  const alerts = OFFICIAL_CONTEXT_BY_ID["nws-alerts"];
  ensureGeoJsonSource(map, alerts, payloads["nws-alerts"]?.data ?? emptyCollection());
  const severityColor = ["match", ["get", "severity"], "Extreme", "#d9364f", "Severe", "#ef6b45", "Moderate", "#f2c14e", "Minor", "#78c6d0", "#b78ad7"] as unknown as string;
  ensureLayer(map, { id: alerts.layerIds[0], type: "fill", source: alerts.sourceId, paint: { "fill-color": severityColor, "fill-opacity": 0.34 } });
  ensureLayer(map, { id: alerts.layerIds[1], type: "line", source: alerts.sourceId, paint: { "line-color": severityColor, "line-width": 2.4, "line-opacity": 0.94 } });

  for (const raster of [OFFICIAL_CONTEXT_BY_ID["usgs-3dep-hillshade"], OFFICIAL_CONTEXT_BY_ID["nws-radar"]]) {
    if (!map.getSource(raster.sourceId)) map.addSource(raster.sourceId, { type: "raster", tiles: [raster.mapUrl!], tileSize: 256, attribution: raster.attribution, minzoom: 3, maxzoom: raster.id === "nws-radar" ? 12 : 16 });
    ensureLayer(map, { id: raster.layerIds[0], type: "raster", source: raster.sourceId, paint: { "raster-opacity": raster.defaultOpacity, "raster-fade-duration": raster.id === "nws-radar" ? 0 : 120 } }, firstRegistryLayer(map));
  }

  for (const source of OFFICIAL_CONTEXT_SOURCES) {
    const visible = visibility[source.id] ? "visible" : "none";
    for (const layerId of source.layerIds) {
      if (!map.getLayer(layerId)) continue;
      map.setLayoutProperty(layerId, "visibility", visible);
      const safeOpacity = Math.max(0.1, Math.min(1, opacity[source.id] ?? source.defaultOpacity));
      const layer = map.getLayer(layerId);
      if (layer?.type === "circle") map.setPaintProperty(layerId, "circle-opacity", safeOpacity);
      if (layer?.type === "fill") map.setPaintProperty(layerId, "fill-opacity", source.id === "census-counties" ? safeOpacity * 0.08 : safeOpacity);
      if (layer?.type === "line") map.setPaintProperty(layerId, "line-opacity", safeOpacity);
      if (layer?.type === "raster") map.setPaintProperty(layerId, "raster-opacity", safeOpacity);
    }
  }
};
