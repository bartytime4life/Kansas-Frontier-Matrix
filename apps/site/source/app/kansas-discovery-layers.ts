import type { OfficialContextSource } from "./live-context";

/**
 * November 2026 discovery layers. Every entry is a fixed, provider-rendered
 * public map service (never a user-supplied URL or query). Images remain
 * external display context; colors are provider symbology, not measurements.
 */
const NOAA_VECTOR = "https://mapservices.weather.noaa.gov/vector/rest/services";
const NOAA_RASTER = "https://mapservices.weather.noaa.gov/raster/rest/services";
const MRLC_WMS = "https://www.mrlc.gov/geoserver/mrlc_display/wms";
const PADUS = "https://edits.nationalmap.gov/arcgis/rest/services/PAD-US/PAD_US/MapServer";
const SDM_WMS = "https://sdmdataaccess.sc.egov.usda.gov/Spatial/SDM.wms";

export type LegendStop = Readonly<{ label: string; color: string }>;
export type DiscoveryLayerId = "noaa-spc-convective-outlook" | "noaa-spc-fire-weather" | "noaa-mrms-qpe-24h"
  | "noaa-wpc-qpf-5day" | "noaa-cpc-drought-outlook" | "mrlc-nlcd-land-cover" | "usgs-padus-lands"
  | "nrcs-ssurgo-soils";

const arcgisExport = (service: string, layers: readonly number[]) =>
  `${service}/export?bbox={bbox-epsg-3857}&bboxSR=3857&imageSR=3857&size=256%2C256&format=png32&transparent=true&layers=show%3A${layers.join("%2C")}&f=image`;

const operational = {
  kind: "OPERATIONAL_WMS", interactiveLayerIds: [], defaultVisibility: false, evidenceRole: "EXTERNAL_CONTEXT_ONLY",
} as const;

/** Compact provider legends for the discovery layers, drawn as chips beside each toggle. */
export const DISCOVERY_LEGENDS: Readonly<Record<DiscoveryLayerId, readonly LegendStop[]>> = Object.freeze({
  "noaa-spc-convective-outlook": [
    { label: "Thunder", color: "#c1e9c1" }, { label: "Marginal", color: "#66a366" }, { label: "Slight", color: "#ffe066" },
    { label: "Enhanced", color: "#ffa366" }, { label: "Moderate", color: "#e06666" }, { label: "High", color: "#ee99ee" },
  ],
  "noaa-spc-fire-weather": [
    { label: "Elevated", color: "#e69800" }, { label: "Critical", color: "#ff0000" }, { label: "Extreme", color: "#e600a9" },
  ],
  "noaa-mrms-qpe-24h": [
    { label: "0.01 in", color: "#00ecec" }, { label: "0.25", color: "#003cff" }, { label: "0.5", color: "#00ff00" },
    { label: "1", color: "#00be00" }, { label: "2", color: "#ffff00" }, { label: "3", color: "#e7b400" },
    { label: "5", color: "#ffa0a0" }, { label: "7+", color: "#e60000" },
  ],
  "noaa-wpc-qpf-5day": [
    { label: "0.01 in", color: "#7fff00" }, { label: "0.25", color: "#088b00" }, { label: "0.5", color: "#104e8b" },
    { label: "1", color: "#00b2ee" }, { label: "1.5", color: "#8968cd" }, { label: "2", color: "#8b008b" },
    { label: "3", color: "#ff0000" }, { label: "5+", color: "#ff7f00" },
  ],
  "noaa-cpc-drought-outlook": [
    { label: "Persists", color: "#9b634a" }, { label: "Improves", color: "#ded4bc" },
    { label: "Removal likely", color: "#b2ad69" }, { label: "Develops", color: "#ffde63" },
  ],
  "mrlc-nlcd-land-cover": [
    { label: "Water", color: "#466b9f" }, { label: "Developed", color: "#d99282" }, { label: "Forest", color: "#68ab5f" },
    { label: "Shrub", color: "#ccb879" }, { label: "Grassland", color: "#dfdfc2" }, { label: "Pasture/hay", color: "#dcd939" },
    { label: "Crops", color: "#ab6c28" }, { label: "Wetlands", color: "#b8d9eb" },
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
    ...operational, id: "noaa-spc-convective-outlook", title: "NOAA SPC Day 1 severe-thunderstorm outlook", shortTitle: "Severe storm outlook · Day 1",
    organization: "NOAA NWS Storm Prediction Center", domain: "Weather & hazards",
    sourceId: "external-noaa-spc-convective-outlook", layerIds: ["external-noaa-spc-convective-outlook-raster"],
    mapUrl: arcgisExport(`${NOAA_VECTOR}/outlooks/SPC_wx_outlks/MapServer`, [1]), maxNativeZoom: 10,
    endpointLabel: "mapservices.weather.noaa.gov · SPC_wx_outlks · Day 1 categorical outlook",
    sourceUrl: "https://www.spc.noaa.gov/products/outlook/", serviceUrl: `${NOAA_VECTOR}/outlooks/SPC_wx_outlks/MapServer`,
    legendUrl: `${NOAA_VECTOR}/outlooks/SPC_wx_outlks/MapServer/legend`,
    cadence: "SPC issues Day 1 outlooks several times daily; the service shows its current issuance",
    freshness: "Provider-current Day 1 forecast; issuance and valid times are on the SPC product page",
    defaultOpacity: 0.55, color: "#ffa366", attribution: "NOAA NWS Storm Prediction Center",
    legend: "SPC categorical risk: thunder, marginal, slight, enhanced, moderate, high. Blank means no categorical risk drawn, not a guarantee of calm weather.",
    boundary: "This is the Storm Prediction Center's probabilistic forecast of organized severe-thunderstorm risk for the current outlook day. It is a forecast area, not an observed storm, a watch, a warning, or a local safety instruction. Categories describe forecast likelihood over a broad area. External context only; not a KFM release.",
    fallback: "If the outlook service is unavailable or returns no polygons, the layer stays blank. Blank never means no storms are possible; consult NWS watches and warnings for decisions.",
  },
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
    ...operational, id: "noaa-mrms-qpe-24h", title: "NOAA MRMS radar-estimated rainfall · past 24 hours", shortTitle: "Rainfall · past 24 h",
    organization: "NOAA NWS · NSSL Multi-Radar Multi-Sensor", domain: "Weather & hazards",
    sourceId: "external-noaa-mrms-qpe-24h", layerIds: ["external-noaa-mrms-qpe-24h-raster"],
    mapUrl: `${NOAA_RASTER}/obs/mrms_qpe/ImageServer/exportImage?bbox={bbox-epsg-3857}&bboxSR=3857&imageSR=3857&size=256%2C256&format=png32&transparent=true&renderingRule=${encodeURIComponent(JSON.stringify({ rasterFunction: "rft_24hr" }))}&f=image`,
    maxNativeZoom: 9,
    endpointLabel: "mapservices.weather.noaa.gov · mrms_qpe ImageServer · rft_24hr",
    sourceUrl: "https://mrms.ncep.noaa.gov/", serviceUrl: `${NOAA_RASTER}/obs/mrms_qpe/ImageServer`,
    legendUrl: `${NOAA_RASTER}/obs/mrms_qpe/ImageServer/legend`,
    cadence: "Hourly provider update, usually a few minutes after the hour",
    freshness: "Rolling 24-hour accumulation ending at the provider's latest hourly analysis",
    defaultOpacity: 0.62, color: "#00be00", attribution: "NOAA NWS · NSSL MRMS",
    legend: "Inches of radar-estimated precipitation, 1 km grid.",
    boundary: "MRMS radar-only quantitative precipitation estimates accumulate the past 24 hours at about 1 km. Radar estimates can miss shallow precipitation, overestimate hail cores, and degrade far from radars or under beam blockage. It is not a weather-station rainfall measurement, flood observation, or KFM evidence.",
    fallback: "Missing tiles stay transparent. A blank area can mean no estimated rain, no radar coverage or a service gap; the Site never labels it dry.",
  },
  {
    ...operational, id: "noaa-wpc-qpf-5day", title: "NOAA WPC 5-day precipitation forecast", shortTitle: "Rain forecast · 5 days",
    organization: "NOAA NWS Weather Prediction Center", domain: "Weather & hazards",
    sourceId: "external-noaa-wpc-qpf-5day", layerIds: ["external-noaa-wpc-qpf-5day-raster"],
    mapUrl: arcgisExport(`${NOAA_VECTOR}/precip/wpc_qpf/MapServer`, [10]), maxNativeZoom: 9,
    endpointLabel: "mapservices.weather.noaa.gov · wpc_qpf · 120-hour Day 1–5 total",
    sourceUrl: "https://www.wpc.ncep.noaa.gov/qpf/qpf2.shtml", serviceUrl: `${NOAA_VECTOR}/precip/wpc_qpf/MapServer`,
    legendUrl: `${NOAA_VECTOR}/precip/wpc_qpf/MapServer/legend`,
    cadence: "WPC updates quantitative precipitation forecasts several times daily",
    freshness: "Provider-current 120-hour forecast total; issuance time on the WPC page",
    defaultOpacity: 0.55, color: "#00b2ee", attribution: "NOAA NWS Weather Prediction Center",
    legend: "Forecast inches of total precipitation over the next five days.",
    boundary: "WPC quantitative precipitation forecasts are expert-blended forecast totals over broad areas. They are not observed rainfall, river forecasts, flood warnings or point guarantees. Compare with past-24-hour radar estimates only as different products on different clocks. Not KFM evidence.",
    fallback: "Unavailable forecast imagery remains blank. No rainfall value is inferred from colors or carried forward from an older issuance.",
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
    ...operational, id: "mrlc-nlcd-land-cover", title: "USGS/MRLC National Land Cover Database · 2021", shortTitle: "Land cover · NLCD 2021",
    organization: "Multi-Resolution Land Characteristics Consortium · USGS", domain: "Land cover & ecology",
    sourceId: "external-mrlc-nlcd-land-cover", layerIds: ["external-mrlc-nlcd-land-cover-raster"],
    mapUrl: `${MRLC_WMS}?SERVICE=WMS&REQUEST=GetMap&VERSION=1.1.1&LAYERS=NLCD_2021_Land_Cover_L48&STYLES=&FORMAT=image%2Fpng&TRANSPARENT=TRUE&HEIGHT=256&WIDTH=256&SRS=EPSG%3A3857&BBOX={bbox-epsg-3857}`,
    minDisplayZoom: 5, maxNativeZoom: 13,
    endpointLabel: "mrlc.gov GeoServer · NLCD_2021_Land_Cover_L48",
    sourceUrl: "https://www.mrlc.gov/data", serviceUrl: MRLC_WMS,
    legendUrl: `${MRLC_WMS}?REQUEST=GetLegendGraphic&VERSION=1.1.1&FORMAT=image%2Fpng&LAYER=NLCD_2021_Land_Cover_L48`,
    cadence: "Fixed 2021 edition; newer Annual NLCD products are published separately",
    freshness: "2021 land-cover classification from Landsat; not current conditions",
    defaultOpacity: 0.6, color: "#ab6c28", attribution: "MRLC · USGS National Land Cover Database",
    legend: "Sixteen NLCD classes at 30 m. Chips show the main Kansas groups.",
    boundary: "NLCD classifies 30 m Landsat pixels into land-cover classes for 2021. Classes have mapping error and do not establish ownership, current crops, habitat quality, species presence, zoning or present land use. External context only.",
    fallback: "Unavailable tiles stay transparent. No land-cover class is inferred for missing pixels.",
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
const FEED_LEGENDS: Readonly<Record<"nws-storm-reports" | "nps-nrhp-places", readonly LegendStop[]>> = Object.freeze({
  "nws-storm-reports": [
    { label: "Tornado", color: "#ff3b5c" }, { label: "Hail", color: "#5ec8ff" }, { label: "Wind", color: "#ffd166" },
    { label: "Flood", color: "#7ae582" }, { label: "Winter", color: "#c9b6ff" }, { label: "Other", color: "#e7e1d6" },
  ],
  "nps-nrhp-places": [
    { label: "Building", color: "#e8c27a" }, { label: "District", color: "#d99a4e" }, { label: "Site", color: "#c7a46b" },
    { label: "Structure", color: "#e2b866" }, { label: "Object", color: "#f0d9a0" }, { label: "Landmark ring", color: "#fff0c2" },
  ],
});

/** Layers added in the November 2026 refresh, shown with a NEW marker in layer lists. */
export const NEW_LAYER_IDS: ReadonlySet<string> = new Set<string>([...DISCOVERY_LAYER_IDS, "nws-storm-reports", "nps-nrhp-places"]);
export const discoveryLegend = (id: string): readonly LegendStop[] | undefined =>
  DISCOVERY_LEGENDS[id as DiscoveryLayerId] ?? FEED_LEGENDS[id as keyof typeof FEED_LEGENDS];
