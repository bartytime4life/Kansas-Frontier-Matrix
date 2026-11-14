import type { OfficialContextSource } from "./live-context";

/**
 * November 2026 discovery layers. Every entry is a fixed, provider-rendered
 * public map service (never a user-supplied URL or query). Images remain
 * external display context; colors are provider symbology, not measurements.
 */
const NOAA_VECTOR = "https://mapservices.weather.noaa.gov/vector/rest/services";
const PADUS = "https://edits.nationalmap.gov/arcgis/rest/services/PAD-US/PAD_US/MapServer";
const SDM_WMS = "https://sdmdataaccess.sc.egov.usda.gov/Spatial/SDM.wms";

export type LegendStop = Readonly<{ label: string; color: string }>;
export type DiscoveryLayerId = "noaa-spc-fire-weather" | "noaa-cpc-drought-outlook" | "usgs-padus-lands" | "nrcs-ssurgo-soils";

const arcgisExport = (service: string, layers: readonly number[]) =>
  `${service}/export?bbox={bbox-epsg-3857}&bboxSR=3857&imageSR=3857&size=256%2C256&format=png32&transparent=true&layers=show%3A${layers.join("%2C")}&f=image`;

const operational = {
  kind: "OPERATIONAL_WMS", interactiveLayerIds: [], defaultVisibility: false, evidenceRole: "EXTERNAL_CONTEXT_ONLY",
} as const;

/** Compact provider legends for the discovery layers, drawn as chips beside each toggle. */
export const DISCOVERY_LEGENDS: Readonly<Record<DiscoveryLayerId, readonly LegendStop[]>> = Object.freeze({
  "noaa-spc-fire-weather": [
    { label: "Elevated", color: "#e69800" }, { label: "Critical", color: "#ff0000" }, { label: "Extreme", color: "#e600a9" },
  ],
  "noaa-cpc-drought-outlook": [
    { label: "Persists", color: "#9b634a" }, { label: "Improves", color: "#ded4bc" },
    { label: "Removal likely", color: "#b2ad69" }, { label: "Develops", color: "#ffde63" },
  ],
  "usgs-padus-lands": [
    { label: "Federal (USACE)", color: "#63ddff" }, { label: "Fish & Wildlife", color: "#ad5764" },
    { label: "State fish & wildlife", color: "#a392de" }, { label: "State park", color: "#9baade" },
    { label: "City / county", color: "#bbc458" }, { label: "Private conservation", color: "#e68d45" },
  ],
  "nrcs-ssurgo-soils": [
    { label: "Soil map-unit boundary", color: "#ff8c00" },
  ],
});

export const KANSAS_DISCOVERY_SOURCES: readonly OfficialContextSource[] = Object.freeze([
  {
    ...operational, id: "noaa-spc-fire-weather", title: "NOAA SPC Day 1 fire-weather outlook", shortTitle: "Fire-weather outlook · Day 1",
    organization: "NOAA NWS Storm Prediction Center", domain: "Fire, smoke & hazards",
    sourceId: "external-noaa-spc-fire-weather", layerIds: ["external-noaa-spc-fire-weather-raster"],
    mapUrl: arcgisExport(`${NOAA_VECTOR}/fire_weather/SPC_firewx/MapServer`, [1, 2]), maxNativeZoom: 10,
    endpointLabel: "mapservices.weather.noaa.gov · SPC_firewx · Day 1 outlook + dry thunderstorms",
    sourceUrl: "https://www.spc.noaa.gov/products/fire_wx/", serviceUrl: `${NOAA_VECTOR}/fire_weather/SPC_firewx/MapServer`,
    legendUrl: `${NOAA_VECTOR}/fire_weather/SPC_firewx/MapServer/legend`,
    cadence: "SPC fire-weather outlooks are issued daily and updated; the service shows its current issuance",
    freshness: "Provider-current Day 1 forecast; issuance time is on the SPC product page",
    defaultOpacity: 0.7, color: "#e69800", attribution: "NOAA NWS Storm Prediction Center",
    legend: "Elevated, critical and extreme fire-weather areas plus dry-thunderstorm areas. Outlines are forecast areas.",
    boundary: "SPC fire-weather outlooks forecast meteorological conditions (wind, humidity, dry thunderstorms) that favor wildfire spread. They are not burn bans, red-flag warnings, active fire detections or fire perimeters. Combine with thermal detections and NIFC reports only as separate context. Not KFM evidence.",
    fallback: "An empty or failed image is not a no-risk finding. Local NWS red-flag warnings and county burn restrictions remain authoritative.",
  },
  {
    ...operational, id: "noaa-cpc-drought-outlook", title: "NOAA CPC seasonal drought outlook", shortTitle: "Drought outlook · seasonal",
    organization: "NOAA NWS Climate Prediction Center", domain: "Weather & hazards",
    sourceId: "external-noaa-cpc-drought-outlook", layerIds: ["external-noaa-cpc-drought-outlook-raster"],
    mapUrl: arcgisExport(`${NOAA_VECTOR}/outlooks/cpc_drought_outlk/MapServer`, [4]), maxNativeZoom: 9,
    endpointLabel: "mapservices.weather.noaa.gov · cpc_drought_outlk · seasonal outlook",
    sourceUrl: "https://www.cpc.ncep.noaa.gov/products/expert_assessment/sdo_summary.php", serviceUrl: `${NOAA_VECTOR}/outlooks/cpc_drought_outlk/MapServer`,
    legendUrl: `${NOAA_VECTOR}/outlooks/cpc_drought_outlk/MapServer/legend`,
    cadence: "CPC issues the seasonal drought outlook monthly",
    freshness: "Provider-current seasonal outlook; valid period on the CPC page",
    defaultOpacity: 0.58, color: "#ffde63", attribution: "NOAA NWS Climate Prediction Center",
    legend: "Expected drought tendency through the outlook season: persists, improves, removal likely or develops.",
    boundary: "The seasonal drought outlook forecasts the direction of drought change relative to the U.S. Drought Monitor. It is not current drought intensity, a disaster designation, an irrigation or crop-insurance determination, or KFM evidence.",
    fallback: "Missing imagery stays blank. Blank is not a no-drought finding; check the current U.S. Drought Monitor for present conditions.",
  },
  {
    ...operational, id: "usgs-padus-lands", title: "USGS PAD-US 4.0 public and protected lands", shortTitle: "Public & protected lands",
    organization: "U.S. Geological Survey Gap Analysis Project", domain: "Land cover & ecology",
    sourceId: "external-usgs-padus-lands", layerIds: ["external-usgs-padus-lands-raster"],
    mapUrl: arcgisExport(PADUS, [0]), minDisplayZoom: 6, maxNativeZoom: 15,
    endpointLabel: "edits.nationalmap.gov · PAD_US · fee managers",
    sourceUrl: "https://www.sciencebase.gov/catalog/item/652ef930d34edd15305a9b03", serviceUrl: PADUS,
    legendUrl: `${PADUS}/legend`,
    cadence: "Periodic PAD-US releases; this service shows version 4.0",
    freshness: "PAD-US 4.0 compilation; individual agency submissions have their own dates",
    defaultOpacity: 0.62, color: "#9baade", attribution: "USGS Gap Analysis Project · PAD-US 4.0",
    legend: "Colors identify the managing agency type for fee-owned public and protected lands.",
    boundary: "PAD-US compiles agency-reported fee ownership and management for protected areas. Boundaries can be generalized or out of date, and inclusion does not grant public access, hunting permission or legal title. Private land is not shown. External context only.",
    fallback: "Unavailable tiles stay transparent. No absence of public land, access or protection is inferred.",
  },
  {
    ...operational, id: "nrcs-ssurgo-soils", title: "USDA NRCS SSURGO soil survey map units", shortTitle: "Soil survey · map units",
    organization: "USDA Natural Resources Conservation Service", domain: "Land records & survey",
    sourceId: "external-nrcs-ssurgo-soils", layerIds: ["external-nrcs-ssurgo-soils-raster"],
    mapUrl: `${SDM_WMS}?SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&LAYERS=MapunitPoly&STYLES=&SRS=EPSG%3A3857&BBOX={bbox-epsg-3857}&WIDTH=256&HEIGHT=256&FORMAT=image%2Fpng&TRANSPARENT=TRUE`,
    minDisplayZoom: 12, maxNativeZoom: 16,
    endpointLabel: "sdmdataaccess.sc.egov.usda.gov · SDM WMS · MapunitPoly",
    sourceUrl: "https://websoilsurvey.nrcs.usda.gov/", serviceUrl: SDM_WMS,
    cadence: "NRCS refreshes SSURGO annually; the service shows the current Soil Data Mart edition",
    freshness: "Provider-current SSURGO map units; survey-area publication dates vary",
    defaultOpacity: 0.75, color: "#ff8c00", attribution: "USDA NRCS Soil Survey Geographic Database (SSURGO)",
    legend: "Orange outlines · SSURGO soil map-unit polygons. Open Web Soil Survey for map-unit names and properties.",
    boundary: "SSURGO map units delineate soil-survey polygons mapped at roughly 1:12,000–1:24,000. A map unit can contain several soil components and inclusions; the outline is not a site-specific soil test, engineering suitability, septic or building approval, or a KFM release. Visible only at close zoom because outlines are dense.",
    fallback: "At overview scale or on provider failure, outlines are absent; no soil class or property is inferred.",
  },
] satisfies OfficialContextSource[]).map(source => Object.freeze({ ...source, layerIds: Object.freeze(source.layerIds), interactiveLayerIds: Object.freeze(source.interactiveLayerIds) })) as readonly OfficialContextSource[];

export const DISCOVERY_LAYER_IDS: readonly DiscoveryLayerId[] = Object.freeze(KANSAS_DISCOVERY_SOURCES.map(source => source.id as DiscoveryLayerId));

/** Point-feed legends mirror the MapLibre paint expressions in live-context.ts. */
const FEED_LEGENDS: Readonly<Record<"nps-nrhp-places" | "nps-historic-trails" | "nps-trail-places", readonly LegendStop[]>> = Object.freeze({
  "nps-nrhp-places": [
    { label: "Building", color: "#e8c27a" }, { label: "District", color: "#d99a4e" }, { label: "Site", color: "#c7a46b" },
    { label: "Structure", color: "#e2b866" }, { label: "Object", color: "#f0d9a0" }, { label: "Landmark ring", color: "#fff0c2" },
  ],
  "nps-historic-trails": [
    { label: "Santa Fe", color: "#e07a3f" }, { label: "Oregon", color: "#5aa9e6" }, { label: "California", color: "#b48ee0" },
    { label: "Pony Express", color: "#e5c34b" }, { label: "Cattle trails (study)", color: "#c98b5a" },
  ],
  "nps-trail-places": [{ label: "Public trail site", color: "#f2c46d" }],
});

/** Layers added in the November 2026 refresh, shown with a NEW marker in layer lists. */
export const NEW_LAYER_IDS: ReadonlySet<string> = new Set<string>([...DISCOVERY_LAYER_IDS, "nps-nrhp-places", "nps-historic-trails", "nps-trail-places"]);
export const discoveryLegend = (id: string): readonly LegendStop[] | undefined =>
  DISCOVERY_LEGENDS[id as DiscoveryLayerId] ?? FEED_LEGENDS[id as keyof typeof FEED_LEGENDS];
