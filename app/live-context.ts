import type { FeatureCollection } from "geojson";
import type { GeoJSONSource, LayerSpecification, Map as MapLibreMap, RasterTileSource } from "maplibre-gl";
import { noaaRadarTileUrl } from "./noaa-radar";

export type OfficialContextId = "census-counties" | "usgs-streamflow" | "noaa-nwps-gauges" | "usgs-3dhp-hydrography" | "usgs-wbd-watersheds" | "noaa-nwm-analysis" | "noaa-nwm-short-range" | "usgs-earthquakes" | "noaa-hms-smoke" | "raspberry-shake-stations" | "usgs-3dep-hillshade" | "usgs-3dep-slope" | "nws-alerts" | "nws-radar";
export type OfficialContextFeedId = "census-counties" | "usgs-streamflow" | "noaa-nwps-gauges" | "usgs-earthquakes" | "nws-alerts" | "noaa-hms-smoke" | "raspberry-shake-stations";
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
  managedAdapterPath?: string;
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
    title: "Census Kansas counties + population",
    shortTitle: "Counties + population",
    organization: "U.S. Census Bureau",
    domain: "Boundaries & places",
    kind: "SNAPSHOT_GEOJSON",
    sourceId: "external-census-counties",
    layerIds: Object.freeze(["external-census-counties-fill", "external-census-counties-line"]),
    interactiveLayerIds: Object.freeze(["external-census-counties-fill"]),
    apiPath: "/api/live-context?feed=census-counties",
    endpointLabel: "TIGERweb Census2020 counties · population, housing, land/water area",
    sourceUrl: "https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/tigerWMS_Census2020/MapServer/82",
    serviceUrl: "https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb",
    cadence: "2020 decennial Census county baseline; 2010 comparison in the archive",
    freshness: "2020 Census geography, population and housing counts",
    defaultVisibility: true,
    defaultOpacity: 0.72,
    color: "#8fd8d0",
    attribution: "U.S. Census Bureau TIGERweb",
    evidenceRole: "EXTERNAL_CONTEXT_ONLY",
    boundary: "Census baseline for all 105 Kansas counties. Geometry, population, housing, and land/water area retain their 2020 edition. It is not present-day population or a reconstruction of older boundaries.",
    fallback: "If the published Census service is unavailable, the overlay stays unavailable. No county or population count is inferred.",
  }),
  Object.freeze({
    id: "usgs-streamflow",
    title: "USGS River Pulse observations + history",
    shortTitle: "River Pulse",
    organization: "U.S. Geological Survey",
    domain: "Living waters",
    kind: "OPERATIONAL_GEOJSON",
    sourceId: "external-usgs-streamflow",
    layerIds: Object.freeze(["external-usgs-streamflow-glow", "external-usgs-streamflow-points", "external-usgs-streamflow-labels"]),
    interactiveLayerIds: Object.freeze(["external-usgs-streamflow-points"]),
    managedAdapterPath: "/api/hydrology/streamflow?mode=network&range=24h",
    endpointLabel: "api.waterdata.usgs.gov · OGC API v1 continuous + daily",
    sourceUrl: "https://api.waterdata.usgs.gov/ogcapi/v1/collections/continuous",
    serviceUrl: "https://api.waterdata.usgs.gov/ogcapi/v1/",
    cadence: "Instantaneous observations, commonly 15-minute; daily means for the one-year selected-station view",
    freshness: "Bounded 24-hour network window + on-demand selected-station history",
    defaultVisibility: true,
    defaultOpacity: 0.92,
    color: "#55d9ec",
    attribution: "U.S. Geological Survey Water Data APIs",
    evidenceRole: "EXTERNAL_CONTEXT_ONLY",
    boundary: "The map steps exact USGS samples without interpolation. Statewide playback is a deterministic, bounded gauge sample; longer histories are station-specific. Values may be provisional, delayed, revised, qualified, or incomplete. Discharge is not comparable across differently sized basins and is not painted onto ungauged reaches. This is not flood guidance, a certified statistic, an admitted KFM observation, or an all-stations inventory.",
    fallback: "A timeout, malformed response, missing sample, or upstream error becomes an explicit unavailable or gap state; the Site never converts it into zero flow, carries a future value backward, or declares a statewide all-clear.",
  }),
  Object.freeze({
    id: "noaa-nwps-gauges",
    title: "NOAA NWPS observations + forecasts",
    shortTitle: "NWPS gauges + forecast",
    organization: "NOAA National Water Prediction Service",
    domain: "Living waters",
    kind: "OPERATIONAL_GEOJSON",
    sourceId: "external-noaa-nwps-gauges",
    layerIds: Object.freeze(["external-noaa-nwps-gauges-halo", "external-noaa-nwps-gauges-points"]),
    interactiveLayerIds: Object.freeze(["external-noaa-nwps-gauges-points"]),
    managedAdapterPath: "/api/hydrology/noaa?mode=network",
    endpointLabel: "api.water.noaa.gov · NWPS v1 gauges + NWM reach series",
    sourceUrl: "https://api.water.noaa.gov/nwps/v1/gauges",
    serviceUrl: "https://water.noaa.gov/about/api",
    cadence: "Provider operational observations, forecasts, and model series",
    freshness: "Exact provider valid times; rolling availability discovered on request",
    defaultVisibility: false,
    defaultOpacity: 0.86,
    color: "#b995ff",
    attribution: "NOAA National Water Prediction Service",
    evidenceRole: "EXTERNAL_CONTEXT_ONLY",
    boundary: "Observed, forecast, and modeled series retain separate source-role labels and valid times. Flood categories appear only when NOAA supplies them. The NWPS API is operational and does not provide a durable general historical archive; this Site is not a warning service, inundation map, emergency guide, or KFM EvidenceBundle.",
    fallback: "Sentinel values, invalid dates, missing geometry, and failed requests are withheld. A missing or stale NOAA record is never shown as normal, safe, or zero flow.",
  }),
  Object.freeze({
    id: "usgs-3dhp-hydrography",
    title: "USGS 3D Hydrography Program network",
    shortTitle: "3DHP hydrography",
    organization: "U.S. Geological Survey",
    domain: "Living waters",
    kind: "OPERATIONAL_WMS",
    sourceId: "external-usgs-3dhp-hydrography",
    layerIds: Object.freeze(["external-usgs-3dhp-hydrography-raster"]),
    interactiveLayerIds: Object.freeze([]),
    mapUrl: "https://3dhp.nationalmap.gov/arcgis/rest/services/usgs_3dhp_all/MapServer/export?bbox={bbox-epsg-3857}&bboxSR=3857&imageSR=3857&size=256%2C256&format=png32&transparent=true&layers=show%3A50%2C60&f=image",
    endpointLabel: "3dhp.nationalmap.gov · usgs_3dhp_all flowlines + waterbodies",
    sourceUrl: "https://3dhp.nationalmap.gov/arcgis/rest/services/usgs_3dhp_all/MapServer",
    serviceUrl: "https://www.usgs.gov/3d-hydrography-program",
    cadence: "Provider-current transitional 3DHP/NHD service",
    freshness: "Current published service mosaic; feature vintages vary by collection area",
    defaultVisibility: true,
    defaultOpacity: 0.78,
    color: "#5bd6e7",
    attribution: "USGS The National Map · 3D Hydrography Program",
    evidenceRole: "EXTERNAL_CONTEXT_ONLY",
    boundary: "This image carrier renders provider flowlines and waterbodies. 3DHP is transitional and can include legacy NHD-sourced work units; current Kansas samples do not support a claim that displayed reaches carry meaningful elevation or 3D geometry. It is not a vector analysis surface, velocity measurement, complete topology proof, site-specific regulatory determination, or KFM release.",
    fallback: "Failed or slow map-service tiles stay transparent. The Site does not draw substitute streams, infer downstream direction, or extend gauge values along the network.",
  }),
  Object.freeze({
    id: "usgs-wbd-watersheds",
    title: "USGS/NRCS Watershed Boundary Dataset",
    shortTitle: "WBD watersheds",
    organization: "U.S. Geological Survey · USDA NRCS",
    domain: "Living waters",
    kind: "OPERATIONAL_WMS",
    sourceId: "external-usgs-wbd-watersheds",
    layerIds: Object.freeze(["external-usgs-wbd-watersheds-raster"]),
    interactiveLayerIds: Object.freeze([]),
    mapUrl: "https://hydro.nationalmap.gov/arcgis/rest/services/wbd/MapServer/export?bbox={bbox-epsg-3857}&bboxSR=3857&imageSR=3857&size=256%2C256&format=png32&transparent=true&layers=show%3A4%2C5%2C6&f=image",
    endpointLabel: "hydro.nationalmap.gov · WBD HUC8/HUC10/HUC12",
    sourceUrl: "https://hydro.nationalmap.gov/arcgis/rest/services/wbd/MapServer",
    serviceUrl: "https://www.usgs.gov/national-hydrography/watershed-boundary-dataset",
    cadence: "Published legacy national watershed service; WBD is no longer maintained as a current USGS product",
    freshness: "Current service availability does not establish a current boundary vintage",
    defaultVisibility: false,
    defaultOpacity: 0.58,
    color: "#74cdbd",
    attribution: "USGS Watershed Boundary Dataset · USDA NRCS",
    evidenceRole: "EXTERNAL_CONTEXT_ONLY",
    boundary: "Scale-dependent HUC8, HUC10, and HUC12 boundaries are rendered from the published legacy WBD service for watershed identity and orientation. USGS now classifies WBD as a legacy product no longer maintained. These images are not selected-vector geometry, a basin condition estimate, a site-specific regulatory boundary, or a KFM EvidenceBundle.",
    fallback: "Unavailable watershed tiles remain transparent. Gauge observations are never generalized into watershed-wide conditions when this carrier is visible.",
  }),
  Object.freeze({
    id: "noaa-nwm-analysis",
    title: "NOAA NWM high-flow analysis guidance",
    shortTitle: "NWM high-flow analysis",
    organization: "NOAA Office of Water Prediction",
    domain: "Living waters",
    kind: "OPERATIONAL_WMS",
    sourceId: "external-noaa-nwm-analysis",
    layerIds: Object.freeze(["external-noaa-nwm-analysis-raster"]),
    interactiveLayerIds: Object.freeze([]),
    mapUrl: "https://maps.water.noaa.gov/server/rest/services/nwm/ana_high_flow_magnitude/MapServer/export?bbox={bbox-epsg-3857}&bboxSR=3857&imageSR=3857&size=256%2C256&format=png32&transparent=true&f=image",
    endpointLabel: "NOAA HydroVIS · ana_high_flow_magnitude",
    sourceUrl: "https://maps.water.noaa.gov/server/rest/services/nwm/ana_high_flow_magnitude/MapServer",
    serviceUrl: "https://water.noaa.gov/about/nwm",
    cadence: "Provider-current hourly National Water Model analysis summary",
    freshness: "Current service snapshot; exact historic frames are not advertised by this map carrier",
    defaultVisibility: false,
    defaultOpacity: 0.7,
    color: "#62d7c6",
    attribution: "NOAA National Water Model · HydroVIS",
    evidenceRole: "EXTERNAL_CONTEXT_ONLY",
    boundary: "This provider-rendered layer is modeled high-flow analysis guidance, not a gauge observation, warning polygon, observed inundation extent, or KFM evidence. Its service metadata does not advertise a selectable time axis, so the Site does not animate or relabel it as historical.",
    fallback: "Unavailable tiles remain transparent and are never interpreted as no high flow. Consult official NWS products for decisions.",
  }),
  Object.freeze({
    id: "noaa-nwm-short-range",
    title: "NOAA NWM next-18-hour maximum high-flow guidance",
    shortTitle: "NWM 18-hour outlook",
    organization: "NOAA Office of Water Prediction",
    domain: "Living waters",
    kind: "OPERATIONAL_WMS",
    sourceId: "external-noaa-nwm-short-range",
    layerIds: Object.freeze(["external-noaa-nwm-short-range-raster"]),
    interactiveLayerIds: Object.freeze([]),
    mapUrl: "https://maps.water.noaa.gov/server/rest/services/nwm/srf_18hr_max_high_flow_magnitude/MapServer/export?bbox={bbox-epsg-3857}&bboxSR=3857&imageSR=3857&size=256%2C256&format=png32&transparent=true&f=image",
    endpointLabel: "NOAA HydroVIS · srf_18hr_max_high_flow_magnitude",
    sourceUrl: "https://maps.water.noaa.gov/server/rest/services/nwm/srf_18hr_max_high_flow_magnitude/MapServer",
    serviceUrl: "https://water.noaa.gov/about/nwm",
    cadence: "Provider-current hourly short-range National Water Model summary",
    freshness: "Maximum modeled guidance for the provider's current next-18-hour window",
    defaultVisibility: false,
    defaultOpacity: 0.72,
    color: "#bd9cff",
    attribution: "NOAA National Water Model · HydroVIS",
    evidenceRole: "EXTERNAL_CONTEXT_ONLY",
    boundary: "This is a modeled maximum over a forecast window—not an observation, official River Forecast Center forecast, warning, deterministic outcome, floodplain, or KFM evidence. The raster carrier exposes no selectable historic time axis in its current service metadata.",
    fallback: "Missing tiles or an empty-looking image are never labeled safe. The Site withholds failed imagery and does not synthesize forecast values.",
  }),
  Object.freeze({
    id: "usgs-earthquakes",
    title: "USGS recent earthquakes near Kansas",
    shortTitle: "Recent earthquakes",
    organization: "U.S. Geological Survey",
    domain: "Geology & hazards",
    kind: "OPERATIONAL_GEOJSON",
    sourceId: "external-usgs-earthquakes",
    layerIds: Object.freeze(["external-usgs-earthquakes-points"]),
    interactiveLayerIds: Object.freeze(["external-usgs-earthquakes-points"]),
    apiPath: "/api/live-context?feed=usgs-earthquakes",
    endpointLabel: "earthquake.usgs.gov · FDSN event query",
    sourceUrl: "https://earthquake.usgs.gov/fdsnws/event/1/",
    serviceUrl: "https://earthquake.usgs.gov/earthquakes/search/",
    cadence: "USGS event catalog; bounded rolling 30-day request",
    freshness: "Events reported or revised within the past 30 days",
    defaultVisibility: false,
    defaultOpacity: 0.92,
    color: "#f2a65a",
    attribution: "U.S. Geological Survey Earthquake Hazards Program",
    evidenceRole: "EXTERNAL_CONTEXT_ONLY",
    boundary: "Catalog locations, times, depths, and magnitudes may be preliminary, reviewed, revised, or deleted. This display is not an earthquake alert, felt-report service, hazard forecast, emergency guide, or admitted KFM observation.",
    fallback: "An unavailable or empty catalog is shown as such; it is never interpreted as proof that no earthquake occurred or that seismic risk is absent.",
  }),
  Object.freeze({
    id: "noaa-hms-smoke",
    title: "NOAA HMS satellite-analyzed smoke footprints",
    shortTitle: "HMS smoke footprints",
    organization: "NOAA Hazard Mapping System",
    domain: "Fire, smoke & hazards",
    kind: "OPERATIONAL_GEOJSON",
    sourceId: "external-noaa-hms-smoke",
    layerIds: Object.freeze(["external-noaa-hms-smoke-fill", "external-noaa-hms-smoke-line"]),
    interactiveLayerIds: Object.freeze(["external-noaa-hms-smoke-fill"]),
    apiPath: "/api/live-context?feed=noaa-hms-smoke",
    endpointLabel: "satepsanone.nesdis.noaa.gov · HMS Smoke_Polygons KML",
    sourceUrl: "https://satepsanone.nesdis.noaa.gov/pub/FIRE/web/HMS/Smoke_Polygons/KML/",
    serviceUrl: "https://www.ospo.noaa.gov/products/land/hms.html",
    cadence: "Daily analyst KML publications; bounded rolling 24-hour map window",
    freshness: "Provider Start/End intervals and density category from retrieved KML",
    defaultVisibility: false,
    defaultOpacity: 0.38,
    color: "#d67d62",
    attribution: "NOAA Hazard Mapping System smoke polygons",
    evidenceRole: "EXTERNAL_CONTEXT_ONLY",
    boundary: "The map draws only NOAA HMS polygons whose provider Start/End intervals intersect the bounded rolling 24-hour window and Kansas bounds. Density is qualitative provider metadata. A footprint is not a fire perimeter, plume altitude, surface PM2.5, exposure, measured transport, health guidance, warning, or all-clear; this layer remains outside KFM evidence and releases.",
    fallback: "A failed daily publication becomes PARTIAL or ERROR, and an empty intersection remains time-stamped. The Site never substitutes a forecast/model, carries a polygon forward, or treats missing smoke as clear air.",
  }),
  Object.freeze({
    id: "raspberry-shake-stations",
    title: "Raspberry Shake AM station network",
    shortTitle: "Raspberry Shake stations",
    organization: "Raspberry Shake · FDSN AM network",
    domain: "Geology & hazards",
    kind: "OPERATIONAL_GEOJSON",
    sourceId: "external-raspberry-shake-stations",
    layerIds: Object.freeze(["external-raspberry-shake-stations-halo", "external-raspberry-shake-stations-points", "external-raspberry-shake-stations-labels"]),
    interactiveLayerIds: Object.freeze(["external-raspberry-shake-stations-points"]),
    apiPath: "/api/live-context?feed=raspberry-shake-stations",
    endpointLabel: "data.raspberryshake.org · FDSN station/1 query",
    sourceUrl: "https://manual.raspberryshake.org/fdsn.html",
    serviceUrl: "https://stationview.raspberryshake.org/",
    cadence: "Station metadata on demand; archived waveforms are provider-delayed and realtime streaming is a separate service",
    freshness: "FDSN station inventory retrieved at request time",
    defaultVisibility: false,
    defaultOpacity: 0.9,
    color: "#c4a2ff",
    attribution: "Raspberry Shake · FDSN AM network",
    evidenceRole: "EXTERNAL_CONTEXT_ONLY",
    boundary: "The active map connection is a bounded FDSN station metadata snapshot: network, station, coordinates, elevation, site name, and provider time bounds. FDSN is not realtime, the provider documents a delay boundary and no fdsnws-event service, and waveform counts require response metadata and a separate bounded adapter. StationView is linked for provider realtime inspection. This layer is not an earthquake alert, waveform measurement, warning, or KFM evidence.",
    fallback: "Malformed, out-of-bounds, capped, or unavailable station rows remain explicit. No station is invented, no waveform is inferred from a marker, and no absence of stations is treated as absence of seismic activity.",
  }),
  Object.freeze({
    id: "usgs-3dep-hillshade",
    title: "USGS 3DEP LiDAR-derived multidirectional hillshade",
    shortTitle: "3DEP LiDAR hillshade",
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
    boundary: "The service renders a provider-current hillshade from the 3DEP elevation mosaic, whose source products include LiDAR point clouds and derived DEMs. It is not a native raster-dem terrain source, point-elevation answer, pinned work-unit tile, pulse-spacing or vertical-datum assertion, accuracy certificate, or admitted KFM elevation artifact.",
    fallback: "Slow or failed image-service tiles remain transparent. The existing 2D map and Terrarium display terrain remain available without substituting a numeric 3DEP claim.",
  }),
  Object.freeze({
    id: "usgs-3dep-slope",
    title: "USGS 3DEP LiDAR-derived slope context",
    shortTitle: "3DEP slope",
    organization: "U.S. Geological Survey",
    domain: "Terrain & landforms",
    kind: "OPERATIONAL_WMS",
    sourceId: "external-usgs-3dep-slope",
    layerIds: Object.freeze(["external-usgs-3dep-slope-raster"]),
    interactiveLayerIds: Object.freeze([]),
    mapUrl: "https://elevation.nationalmap.gov/arcgis/rest/services/3DEPElevation/ImageServer/exportImage?bbox={bbox-epsg-3857}&bboxSR=3857&imageSR=3857&size=256%2C256&format=png32&renderingRule=%7B%22rasterFunction%22%3A%22Slope%22%7D&f=image",
    endpointLabel: "elevation.nationalmap.gov · 3DEPElevation · Slope raster function",
    sourceUrl: "https://elevation.nationalmap.gov/arcgis/rest/services/3DEPElevation/ImageServer",
    serviceUrl: "https://www.usgs.gov/3d-elevation-program/about-3dep-products-services",
    cadence: "USGS dynamic 3DEP service; provider-controlled refresh",
    freshness: "Current published 3DEP service mosaic",
    defaultVisibility: false,
    defaultOpacity: 0.34,
    color: "#e0a56c",
    attribution: "USGS 3D Elevation Program",
    evidenceRole: "EXTERNAL_CONTEXT_ONLY",
    boundary: "This optional slope visualization is dynamically derived by the USGS 3DEP service. It provides terrain-form context and does not expose raw point clouds, establish a selected work-unit identity, prove a vertical datum or accuracy for a pixel, or create a KFM elevation or hazard claim.",
    fallback: "If the slope raster function is unavailable, the layer remains transparent and the attributed 2D/Terrarium display path remains available. No numeric slope or elevation value is inferred from image colors.",
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
    title: "NOAA nowCOAST CONUS radar reflectivity loop",
    shortTitle: "NOAA radar loop",
    organization: "NOAA nowCOAST · NWS/OAR MRMS",
    domain: "Weather & hazards",
    kind: "OPERATIONAL_WMS",
    sourceId: "external-nws-radar",
    layerIds: Object.freeze(["external-nws-radar-raster"]),
    interactiveLayerIds: Object.freeze([]),
    endpointLabel: "nowcoast.noaa.gov · conus_base_reflectivity_mosaic",
    sourceUrl: "https://nowcoast.noaa.gov/",
    serviceUrl: "https://nowcoast.noaa.gov/geoserver/weather_radar/wms",
    cadence: "Time-enabled MRMS mosaic; cadence is discovered from advertised observations (currently about four minutes)",
    freshness: "Exact available observation times loaded from the fixed NOAA WMS capabilities adapter",
    defaultVisibility: false,
    defaultOpacity: 0.68,
    color: "#f2c14e",
    attribution: "NOAA nowCOAST · NWS/OAR MRMS",
    evidenceRole: "EXTERNAL_CONTEXT_ONLY",
    boundary: "Observed 1 km CONUS base-reflectivity mosaics are shown at exact NOAA-advertised frame times. The Site does not infer values from rendered colors, interpolate frames, resolve beam blockage or quality flags, convert reflectivity to rainfall, predict motion, determine warning status, or create KFM evidence support.",
    fallback: "If the frame manifest or requested WMS tiles fail, the radar is frozen or withheld with a visible error; no prior frame is relabeled as current and no synthetic radar is substituted. Consult official NWS products for decisions.",
  }),
]);

export const OFFICIAL_CONTEXT_BY_ID = Object.freeze(Object.fromEntries(OFFICIAL_CONTEXT_SOURCES.map((source) => [source.id, source])) as Record<OfficialContextId, OfficialContextSource>);
export const OFFICIAL_CONTEXT_BY_SOURCE_ID = Object.freeze(Object.fromEntries(OFFICIAL_CONTEXT_SOURCES.map((source) => [source.sourceId, source])) as Record<string, OfficialContextSource>);
export const OFFICIAL_CONTEXT_INTERACTIVE_LAYER_IDS = Object.freeze(OFFICIAL_CONTEXT_SOURCES.flatMap((source) => source.interactiveLayerIds));
export const OFFICIAL_CONTEXT_PRESENT_FRAME = new Date().getUTCFullYear();

export type OfficialContextTemporalSupport = Readonly<{
  axis: "joined-source-snapshot" | "rolling-retrieval-window" | "provider-current-mosaic" | "provider-observation-loop" | "provider-observation-history" | "provider-forecast-series";
  supportedFrames: readonly number[];
  limitation: string;
}>;

/** Source-specific support declarations. A shared 2026 atlas tick represents
 * the operational-present UI frame; it is not asserted as every source's
 * observation, publication, or acquisition year. */
export const OFFICIAL_CONTEXT_TEMPORAL_SUPPORT: Readonly<Record<OfficialContextId, OfficialContextTemporalSupport>> = Object.freeze({
  "census-counties": Object.freeze({
    axis: "joined-source-snapshot",
    supportedFrames: Object.freeze([OFFICIAL_CONTEXT_PRESENT_FRAME]),
    limitation: "Pinned 2020 Census geography and counts. Older event dates do not change this independent baseline edition.",
  }),
  "usgs-streamflow": Object.freeze({
    axis: "provider-observation-history",
    supportedFrames: Object.freeze([OFFICIAL_CONTEXT_PRESENT_FRAME]),
    limitation: "A separate ISO-time River Pulse clock provides exact recent instantaneous observations plus selected-station instantaneous and daily history. It remains subordinate to the operational-present atlas frame and is not a pinned KFM release.",
  }),
  "noaa-nwps-gauges": Object.freeze({
    axis: "provider-forecast-series",
    supportedFrames: Object.freeze([OFFICIAL_CONTEXT_PRESENT_FRAME]),
    limitation: "Operational observations, forecasts, and NWM model series retain provider valid times and separate roles. NWPS is not a durable historical archive; this carrier is held outside the operational-present atlas frame.",
  }),
  "usgs-3dhp-hydrography": Object.freeze({
    axis: "provider-current-mosaic",
    supportedFrames: Object.freeze([OFFICIAL_CONTEXT_PRESENT_FRAME]),
    limitation: "Provider-current transitional 3DHP/NHD image service; collection-area vintages are not exposed as selectable historical slices.",
  }),
  "usgs-wbd-watersheds": Object.freeze({
    axis: "provider-current-mosaic",
    supportedFrames: Object.freeze([OFFICIAL_CONTEXT_PRESENT_FRAME]),
    limitation: "Published legacy HUC boundary image service; USGS no longer maintains WBD as a current product, and boundary vintages are not exposed as historical watershed snapshots in this Site.",
  }),
  "noaa-nwm-analysis": Object.freeze({
    axis: "provider-current-mosaic",
    supportedFrames: Object.freeze([OFFICIAL_CONTEXT_PRESENT_FRAME]),
    limitation: "Provider-current NWM analysis summary with no time-enabled map-service axis; never replayed as a historic observation.",
  }),
  "noaa-nwm-short-range": Object.freeze({
    axis: "provider-current-mosaic",
    supportedFrames: Object.freeze([OFFICIAL_CONTEXT_PRESENT_FRAME]),
    limitation: "Provider-current next-18-hour maximum modeled guidance with no time-enabled map-service axis; never replayed as an observation.",
  }),
  "usgs-earthquakes": Object.freeze({
    axis: "rolling-retrieval-window",
    supportedFrames: Object.freeze([OFFICIAL_CONTEXT_PRESENT_FRAME]),
    limitation: "The Explorer shows a rolling 30-day catalog; select a day in the Event Observatory for the connected historical catalog. Events may be revised.",
  }),
  "noaa-hms-smoke": Object.freeze({
    axis: "rolling-retrieval-window",
    supportedFrames: Object.freeze([OFFICIAL_CONTEXT_PRESENT_FRAME]),
    limitation: "Daily NOAA HMS publications are intersected with a rolling 24-hour window; provider Start/End intervals are retained, but no historical smoke archive or model/transport series is connected.",
  }),
  "raspberry-shake-stations": Object.freeze({
    axis: "rolling-retrieval-window",
    supportedFrames: Object.freeze([OFFICIAL_CONTEXT_PRESENT_FRAME]),
    limitation: "FDSN station metadata is retrieved on demand. Archived waveforms have provider latency and realtime inspection belongs to StationView/separate services; the atlas clock is not a seismic waveform history.",
  }),
  "usgs-3dep-hillshade": Object.freeze({
    axis: "provider-current-mosaic",
    supportedFrames: Object.freeze([OFFICIAL_CONTEXT_PRESENT_FRAME]),
    limitation: "Provider-current mosaic with no pinned acquisition-time slice in this Site.",
  }),
  "usgs-3dep-slope": Object.freeze({
    axis: "provider-current-mosaic",
    supportedFrames: Object.freeze([OFFICIAL_CONTEXT_PRESENT_FRAME]),
    limitation: "Provider-current dynamically derived slope visualization with no pinned work-unit or acquisition-time slice in this Site.",
  }),
  "nws-alerts": Object.freeze({
    axis: "rolling-retrieval-window",
    supportedFrames: Object.freeze([OFFICIAL_CONTEXT_PRESENT_FRAME]),
    limitation: "Active-alert snapshot at retrieval time; expired historical alerts are not requested.",
  }),
  "nws-radar": Object.freeze({
    axis: "provider-observation-loop",
    supportedFrames: Object.freeze([OFFICIAL_CONTEXT_PRESENT_FRAME]),
    limitation: "A bounded recent observation-time loop is available only inside the operational-present atlas frame. It is not a historical archive or a released KFM time series.",
  }),
});

/**
 * Official adapters in this Site expose one current snapshot or rolling window,
 * not a historical archive. Preserve each user's visibility intent while
 * withholding those carriers whenever the committed atlas frame is not the
 * operational-present frame.
 */
export const officialContextVisibilityForFrame = (
  visibility: Record<OfficialContextId, boolean>,
  frame: number,
): Record<OfficialContextId, boolean> => Object.fromEntries(OFFICIAL_CONTEXT_SOURCES.map((source) => [
  source.id,
  OFFICIAL_CONTEXT_TEMPORAL_SUPPORT[source.id].supportedFrames.includes(frame) && visibility[source.id] === true,
])) as Record<OfficialContextId, boolean>;

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
  ensureLayer(map, { id: streamflow.layerIds[0], type: "circle", source: streamflow.sourceId, filter: ["!=", ["get", "missing"], true], paint: {
    "circle-color": ["case", ["==", ["get", "trend"], "rising"], "#67e8f9", ["==", ["get", "trend"], "falling"], "#f3c969", ["==", ["get", "trend"], "steady"], "#72d5a7", streamflow.color],
    "circle-radius": ["interpolate", ["linear"], ["zoom"], 4, ["interpolate", ["linear"], ["coalesce", ["get", "visualMagnitude"], 0], 0, 7, 4, 20], 10, ["interpolate", ["linear"], ["coalesce", ["get", "visualMagnitude"], 0], 0, 12, 4, 34]],
    "circle-blur": 0.72, "circle-opacity": 0.3,
  } });
  ensureLayer(map, { id: streamflow.layerIds[1], type: "circle", source: streamflow.sourceId, paint: {
    "circle-color": ["case", ["==", ["get", "missing"], true], "#17343b", ["==", ["get", "trend"], "rising"], "#55e6ff", ["==", ["get", "trend"], "falling"], "#f0c56c", ["==", ["get", "trend"], "steady"], "#73cfa8", streamflow.color],
    "circle-radius": ["interpolate", ["linear"], ["zoom"], 4, ["interpolate", ["linear"], ["coalesce", ["get", "visualMagnitude"], 0], 0, 3.5, 4, 8.5], 10, ["interpolate", ["linear"], ["coalesce", ["get", "visualMagnitude"], 0], 0, 6, 4, 13]],
    "circle-opacity": ["case", ["==", ["get", "missing"], true], 0.38, 0.96],
    "circle-stroke-color": ["case", ["==", ["get", "selected"], true], "#ffe5a4", ["==", ["get", "missing"], true], "#a4bdc2", ["==", ["get", "approvalStatus"], "Approved"], "#d5fff0", "#f3c969"],
    "circle-stroke-width": ["case", ["==", ["get", "selected"], true], 3.4, ["==", ["get", "missing"], true], 2.2, 1.4],
  } });
  ensureLayer(map, { id: streamflow.layerIds[2], type: "symbol", source: streamflow.sourceId, minzoom: 8.5, layout: {
    "text-field": ["coalesce", ["get", "stationName"], ["get", "name"], ["get", "monitoringLocationId"]], "text-size": 10.5, "text-offset": [0, 1.25], "text-anchor": "top", "text-optional": true,
  }, paint: { "text-color": "#d8f7f7", "text-halo-color": "#04171b", "text-halo-width": 1.5, "text-opacity": 0.86 } });

  const nwps = OFFICIAL_CONTEXT_BY_ID["noaa-nwps-gauges"];
  ensureGeoJsonSource(map, nwps, payloads["noaa-nwps-gauges"]?.data ?? emptyCollection());
  ensureLayer(map, { id: nwps.layerIds[0], type: "circle", source: nwps.sourceId, paint: {
    "circle-color": nwps.color, "circle-radius": ["interpolate", ["linear"], ["zoom"], 4, 8, 10, 18], "circle-blur": 0.82, "circle-opacity": 0.24,
  } });
  ensureLayer(map, { id: nwps.layerIds[1], type: "circle", source: nwps.sourceId, paint: {
    "circle-color": ["match", ["downcase", ["coalesce", ["get", "floodCategory"], ""]], "major", "#d9364f", "moderate", "#ef6b45", "minor", "#f2a65a", "action", "#f2c14e", nwps.color],
    "circle-radius": ["interpolate", ["linear"], ["zoom"], 4, 3.4, 10, 7.5, 14, 10], "circle-opacity": 0.9, "circle-stroke-color": ["case", ["==", ["get", "hasForecast"], true], "#e7d9ff", "#172e36"], "circle-stroke-width": ["case", ["==", ["get", "hasForecast"], true], 2.2, 1.2],
  } });

  const earthquakes = OFFICIAL_CONTEXT_BY_ID["usgs-earthquakes"];
  ensureGeoJsonSource(map, earthquakes, payloads["usgs-earthquakes"]?.data ?? emptyCollection());
  ensureLayer(map, { id: earthquakes.layerIds[0], type: "circle", source: earthquakes.sourceId, paint: {
    "circle-color": ["interpolate", ["linear"], ["coalesce", ["get", "magnitude"], 0], 0, "#ffd7a8", 2, earthquakes.color, 4, "#ef6b45", 6, "#d9364f"],
    "circle-radius": ["interpolate", ["linear"], ["zoom"], 4, ["interpolate", ["linear"], ["coalesce", ["get", "magnitude"], 0], 0, 3, 3, 7, 6, 12], 10, ["interpolate", ["linear"], ["coalesce", ["get", "magnitude"], 0], 0, 5, 3, 11, 6, 18]],
    "circle-opacity": 0.92, "circle-stroke-color": "#27130a", "circle-stroke-width": 1.5,
  } });

  const smoke = OFFICIAL_CONTEXT_BY_ID["noaa-hms-smoke"];
  ensureGeoJsonSource(map, smoke, payloads["noaa-hms-smoke"]?.data ?? emptyCollection());
  const smokeColor = ["match", ["get", "density"], "Heavy", "#df6b51", "Medium", "#d79862", "Light", "#b9c47b", "#8b9aa0"] as unknown as string;
  ensureLayer(map, { id: smoke.layerIds[0], type: "fill", source: smoke.sourceId, paint: { "fill-color": smokeColor, "fill-opacity": 0.32 } });
  ensureLayer(map, { id: smoke.layerIds[1], type: "line", source: smoke.sourceId, paint: { "line-color": smokeColor, "line-width": ["interpolate", ["linear"], ["zoom"], 4, 0.7, 9, 1.8], "line-opacity": 0.74 } });

  const raspberryShake = OFFICIAL_CONTEXT_BY_ID["raspberry-shake-stations"];
  ensureGeoJsonSource(map, raspberryShake, payloads["raspberry-shake-stations"]?.data ?? emptyCollection());
  ensureLayer(map, { id: raspberryShake.layerIds[0], type: "circle", source: raspberryShake.sourceId, paint: {
    "circle-color": raspberryShake.color, "circle-radius": ["interpolate", ["linear"], ["zoom"], 4, 9, 10, 20], "circle-blur": 0.8, "circle-opacity": 0.24,
  } });
  ensureLayer(map, { id: raspberryShake.layerIds[1], type: "circle", source: raspberryShake.sourceId, paint: {
    "circle-color": raspberryShake.color, "circle-radius": ["interpolate", ["linear"], ["zoom"], 4, 3.8, 10, 7.2, 14, 9], "circle-opacity": 0.94, "circle-stroke-color": "#271d3f", "circle-stroke-width": 1.4,
  } });
  ensureLayer(map, { id: raspberryShake.layerIds[2], type: "symbol", source: raspberryShake.sourceId, minzoom: 8.5, layout: {
    "text-field": ["coalesce", ["get", "name"], ["get", "station"]], "text-size": 10.5, "text-offset": [0, 1.25], "text-anchor": "top", "text-optional": true,
  }, paint: { "text-color": "#eadfff", "text-halo-color": "#100d1d", "text-halo-width": 1.5, "text-opacity": 0.86 } });

  const alerts = OFFICIAL_CONTEXT_BY_ID["nws-alerts"];
  ensureGeoJsonSource(map, alerts, payloads["nws-alerts"]?.data ?? emptyCollection());
  const severityColor = ["match", ["get", "severity"], "Extreme", "#d9364f", "Severe", "#ef6b45", "Moderate", "#f2c14e", "Minor", "#78c6d0", "#b78ad7"] as unknown as string;
  ensureLayer(map, { id: alerts.layerIds[0], type: "fill", source: alerts.sourceId, paint: { "fill-color": severityColor, "fill-opacity": 0.34 } });
  ensureLayer(map, { id: alerts.layerIds[1], type: "line", source: alerts.sourceId, paint: { "line-color": severityColor, "line-width": 2.4, "line-opacity": 0.94 } });

  for (const raster of [OFFICIAL_CONTEXT_BY_ID["usgs-3dhp-hydrography"], OFFICIAL_CONTEXT_BY_ID["usgs-wbd-watersheds"], OFFICIAL_CONTEXT_BY_ID["noaa-nwm-analysis"], OFFICIAL_CONTEXT_BY_ID["noaa-nwm-short-range"], OFFICIAL_CONTEXT_BY_ID["usgs-3dep-hillshade"], OFFICIAL_CONTEXT_BY_ID["usgs-3dep-slope"]]) {
    if (!map.getSource(raster.sourceId)) map.addSource(raster.sourceId, { type: "raster", tiles: [raster.mapUrl!], tileSize: 256, attribution: raster.attribution, minzoom: 3, maxzoom: 16 });
    ensureLayer(map, { id: raster.layerIds[0], type: "raster", source: raster.sourceId, paint: { "raster-opacity": raster.defaultOpacity, "raster-fade-duration": 120 } }, firstRegistryLayer(map));
  }

  for (const source of OFFICIAL_CONTEXT_SOURCES) {
    const visible = visibility[source.id] ? "visible" : "none";
    for (const layerId of source.layerIds) {
      if (!map.getLayer(layerId)) continue;
      map.setLayoutProperty(layerId, "visibility", visible);
      const safeOpacity = Math.max(0, Math.min(1, opacity[source.id] ?? source.defaultOpacity));
      const layer = map.getLayer(layerId);
      if (layer?.type === "circle") map.setPaintProperty(layerId, "circle-opacity", layerId.endsWith("-glow") || layerId.endsWith("-halo") ? safeOpacity * 0.3 : safeOpacity);
      if (layer?.type === "circle") map.setPaintProperty(layerId, "circle-stroke-opacity", safeOpacity);
      if (layer?.type === "fill") map.setPaintProperty(layerId, "fill-opacity", source.id === "census-counties" ? safeOpacity * 0.08 : safeOpacity);
      if (layer?.type === "line") map.setPaintProperty(layerId, "line-opacity", safeOpacity);
      if (layer?.type === "raster") map.setPaintProperty(layerId, "raster-opacity", safeOpacity);
      if (layer?.type === "symbol") map.setPaintProperty(layerId, "text-opacity", safeOpacity);
    }
  }
};

/** Checks the renderer source without mutating or reloading it. */
export const noaaRadarObservationTimeIsApplied = (map: MapLibreMap, observedAt: string): boolean => {
  const radar = OFFICIAL_CONTEXT_BY_ID["nws-radar"];
  const source = map.getSource(radar.sourceId) as RasterTileSource | undefined;
  return Boolean(source && map.getLayer(radar.layerIds[0]) && source.serialize().tiles?.[0] === noaaRadarTileUrl(observedAt));
};

/** Switches the fixed NOAA raster source to one advertised observation time.
 * Invalid timestamps are rejected, and the tile URL never omits TIME. */
export const setNoaaRadarObservationTime = (map: MapLibreMap, observedAt: string): "changed" | "unchanged" | null => {
  const radar = OFFICIAL_CONTEXT_BY_ID["nws-radar"];
  const tileUrl = noaaRadarTileUrl(observedAt);
  let source = map.getSource(radar.sourceId) as RasterTileSource | undefined;
  let changed = false;
  if (!source) {
    map.addSource(radar.sourceId, { type: "raster", tiles: [tileUrl], tileSize: 256, attribution: radar.attribution, minzoom: 3, maxzoom: 12 });
    source = map.getSource(radar.sourceId) as RasterTileSource | undefined;
    changed = true;
  } else if (typeof source.setTiles === "function" && source.serialize().tiles?.[0] !== tileUrl) {
    source.setTiles([tileUrl]);
    changed = true;
  }
  ensureLayer(map, { id: radar.layerIds[0], type: "raster", source: radar.sourceId, paint: { "raster-opacity": radar.defaultOpacity, "raster-fade-duration": 0 } }, firstRegistryLayer(map));
  if (!source) return null;
  return changed ? "changed" : "unchanged";
};
