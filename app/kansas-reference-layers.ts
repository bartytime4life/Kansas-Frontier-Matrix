import type { OfficialContextSource } from "./live-context";
import { BRIDGE_FILTERS, type BridgeLayerId } from "./kansas-bridge-records";

const KDOT = "https://kanplan.ksdot.gov/arcgis_web_adaptor/rest/services/Transportation";
const NFHL = "https://hazards.fema.gov/arcgis/rest/services/public/NFHL/MapServer";
const BLM_MLRS_LEASES = "https://gis.blm.gov/nlsdb/rest/services/Fluid_Minerals/Oil_Gas_Leases_Case_Disp/MapServer";
export const KANSAS_REFERENCE_BOUNDS = [-102.06, 36.99, -94.58, 40.01] as const;

// BLM says scores 0-3 are direct PLSS matches. Calculated, section-level,
// incomplete and county-level geocodes stay out of this first map carrier.
export const BLM_MLRS_DIRECT_KANSAS_WHERE = "GEO_STATE='KS' AND (QLTY LIKE '0:%' OR QLTY LIKE '1:%' OR QLTY LIKE '2:%' OR QLTY LIKE '3:%')";
function blmMlrsLeaseLayer(layer: 0 | 3, id: "blm-mlrs-leases-authorized" | "blm-mlrs-leases-closed", disposition: string): OfficialContextSource {
  return {
    id, title: `BLM Kansas oil and gas leases · ${disposition}`, shortTitle: `BLM leases · ${disposition.toLowerCase()}`,
    organization: "Bureau of Land Management", domain: "Land records & survey", kind: "OPERATIONAL_WMS",
    sourceId: `external-${id}`, layerIds: [`external-${id}-raster`], interactiveLayerIds: [],
    mapUrl: `${BLM_MLRS_LEASES}/export?bbox={bbox-epsg-3857}&bboxSR=3857&imageSR=3857&size=256%2C256&format=png32&transparent=true&layers=show%3A${layer}&layerDefs=${encodeURIComponent(JSON.stringify({ [layer]: BLM_MLRS_DIRECT_KANSAS_WHERE }))}&f=image`,
    sourceUrl: `${BLM_MLRS_LEASES}/${layer}`, serviceUrl: BLM_MLRS_LEASES, legendUrl: `${BLM_MLRS_LEASES}/legend`,
    endpointLabel: `BLM MLRS oil and gas lease case disposition · ${disposition} · Kansas direct PLSS matches`,
    cadence: "Provider-current disposition image; checked when visible tiles load",
    freshness: "Case disposition in current MLRS service, not live operations or a historical time series",
    defaultVisibility: false, defaultOpacity: 0.6, color: layer === 0 ? "#78cdb5" : "#dba77b",
    minDisplayZoom: 9, maxNativeZoom: 16, attribution: "U.S. Department of the Interior · Bureau of Land Management",
    evidenceRole: "EXTERNAL_CONTEXT_ONLY",
    legend: "BLM provider symbols. Only Kansas cases with direct PLSS match scores 0–3 are displayed; this swatch identifies the toggle, not a lease classification.",
    boundary: `BLM MLRS ${disposition.toLowerCase()} lease cases are geocoded from legal land descriptions. Even a direct PLSS match is not an exact lease or mineral-rights footprint. Other quality groups, ungeocoded cases and other dispositions are withheld. This is not current drilling, production, title, access, or a KFM land release.`,
    fallback: "Missing tiles or withheld geocoding quality leave gaps; no absence-of-lease or ownership claim is inferred.",
  };
}

// Fixed provider layers, never a user-supplied URL or query. Geometry is rendered
// by the provider in Web Mercator; styles change visibility, not measurements.
function kdotLine(service: "LRS_County" | "Railroads" | "Historical_Roads", layer: number, color: number[], dashed = false): string {
  const dynamic = [{ id: layer, source: { type: "mapLayer", mapLayerId: layer },
    drawingInfo: { showLabels: false, renderer: { type: "simple", symbol: {
      type: "esriSLS", style: dashed ? "esriSLSDash" : "esriSLSSolid", color, width: 1.5,
    } } } }];
  return `${KDOT}/${service}/MapServer/export?bbox={bbox-epsg-3857}&bboxSR=3857&imageSR=3857&size=256%2C256&format=png32&transparent=true&layers=show%3A${layer}&dynamicLayers=${encodeURIComponent(JSON.stringify(dynamic))}&f=image`;
}

const transport = {
  organization: "Kansas Department of Transportation", domain: "Roads, rail & movement",
  kind: "OPERATIONAL_WMS", defaultVisibility: false, defaultOpacity: 0.85,
  cadence: "Provider-current reference service; checked as visible tiles load",
  freshness: "Feature dates vary; current service access is not live traffic or a historical edition",
  attribution: "Kansas Department of Transportation (KDOT)", evidenceRole: "EXTERNAL_CONTEXT_ONLY",
  fallback: "Unavailable tiles leave a gap. No routes, traffic, closure status, or missing geometry are inferred.",
  maxNativeZoom: 17,
} as const;

const STRUCTURES = "https://kanplan.ksdot.gov/arcgis_web_adaptor/rest/services/Structures";
function bridgeLayer(id: BridgeLayerId, title: string, boundary: string): OfficialContextSource {
  const { service, where } = BRIDGE_FILTERS[id];
  const base = `${STRUCTURES}/${service}/MapServer`;
  return { ...transport, id, title: `KDOT Kansas ${title}`, shortTitle: title,
    sourceId: `external-${id}`, layerIds: [`external-${id}-raster`], interactiveLayerIds: [],
    mapUrl: `${base}/export?bbox={bbox-epsg-3857}&bboxSR=3857&imageSR=3857&size=256%2C256&format=png32&transparent=true&layers=show%3A0&layerDefs=${encodeURIComponent(JSON.stringify({ 0: where }))}&f=image`,
    minDisplayZoom: 8, color: "#e2aaf1", endpointLabel: `KDOT ${service.replaceAll("_", " ")} · inventory point locations`,
    sourceUrl: `${base}/0`, serviceUrl: base, legendUrl: `${base}/legend`,
    legend: "Provider bridge symbols · point locations, not deck footprints. Open the provider legend for symbols.",
    boundary: `${boundary} Inventory observations may lag changes; not navigation, structural safety, public access, or evidence that a bridge has been demolished. External context only.`,
  };
}

export const KANSAS_REFERENCE_SOURCES: readonly OfficialContextSource[] = Object.freeze([
  blmMlrsLeaseLayer(0, "blm-mlrs-leases-authorized", "authorized"),
  blmMlrsLeaseLayer(3, "blm-mlrs-leases-closed", "closed"),
  bridgeLayer("kdot-bridges-state", "Bridges · state highways", "KDOT state highway structures over 20 feet; inventory dates vary."),
  bridgeLayer("kdot-bridges-local", "Bridges · local roads", "KDOT non-state highway bridge inventory; structures over 20 feet."),
  bridgeLayer("kdot-bridges-historic", "Bridges · historic designation", "Non-state bridges recorded as National Register listed or eligible. Possible or undetermined significance is excluded. Historic designation does not mean closed."),
  bridgeLayer("kdot-bridges-old", "Bridges · built before 1950", "Non-state bridges with a recorded construction year before 1950; unknown years are excluded. An age filter is not historic designation; later reconstruction may have changed the structure."),
  bridgeLayer("kdot-bridges-closed", "Bridges · recorded closed", "Non-state bridges explicitly recorded closed to all traffic. A posted load restriction is not treated as a closure; this is not a live closure feed."),
  {
    ...transport, id: "kdot-roads-1918", title: "KDOT Kansas historical roads · 1918", shortTitle: "Historical roads · 1918",
    sourceId: "external-kdot-roads-1918", layerIds: ["external-kdot-roads-1918-raster"], interactiveLayerIds: [],
    mapUrl: kdotLine("Historical_Roads", 0, [245, 173, 116, 255], true), minDisplayZoom: 7, maxNativeZoom: 15,
    endpointLabel: "KDOT georeferenced and digitized 1918 State Highway Commission map", color: "#f5ad74",
    sourceUrl: `${KDOT}/Historical_Roads/MapServer/0`, serviceUrl: `${KDOT}/Historical_Roads/MapServer`,
    cadence: "Fixed 1918 source map; provider may revise digitization", freshness: "Historical 1918 edition, not current road status",
    legend: "Orange dashed lines · digitized 1918 named routes; approximate at source-map scale.",
    boundary: "KDOT digitized the 1918 map and cross-referenced contemporary AAA maps. Named routes can split or conflict. This layer does not establish present closure, abandonment, exact road width, or the date a road was built or removed. Compare with current roads without interpreting every difference as a closure. External historical context only.",
  },
  {
    ...transport, id: "kdot-roads", title: "KDOT Kansas roads and highways", shortTitle: "Roads & highways",
    sourceId: "external-kdot-roads", layerIds: ["external-kdot-roads-raster"], interactiveLayerIds: [],
    mapUrl: kdotLine("LRS_County", 4, [247, 216, 145, 255]), minDisplayZoom: 9,
    endpointLabel: "KDOT LRS County · public road route reference", color: "#f7d891",
    sourceUrl: `${KDOT}/LRS_County/MapServer/4`, serviceUrl: `${KDOT}/LRS_County/MapServer`,
    legend: "Gold lines · public road route reference; line width does not represent road width or capacity.",
    boundary: "KDOT's Kansas reference network includes state highways and non-state public roads. Uniform display lines do not imply functional class, road width, navigability, current traffic, closures, ownership, or historical existence. This is external map context, not a released KFM network.",
  },
  {
    ...transport, id: "kdot-rail-active", title: "KDOT Kansas active railroads", shortTitle: "Railroads · active",
    sourceId: "external-kdot-rail-active", layerIds: ["external-kdot-rail-active-raster"], interactiveLayerIds: [],
    mapUrl: kdotLine("Railroads", 0, [131, 231, 220, 255]), minDisplayZoom: 8,
    endpointLabel: "KDOT Railroads · provider-designated active lines", color: "#83e7dc",
    sourceUrl: `${KDOT}/Railroads/MapServer/0`, serviceUrl: `${KDOT}/Railroads/MapServer`,
    legend: "Cyan solid lines · KDOT active designation, not real-time train movement.",
    boundary: "Active is KDOT's source designation. It does not confirm today's operations, schedules, train locations, ownership, legal access, or route safety. Survey dates and changes are not a selectable historical timeline. External context only.",
  },
  {
    ...transport, id: "kdot-rail-abandoned", title: "KDOT Kansas abandoned railroads", shortTitle: "Railroads · abandoned",
    sourceId: "external-kdot-rail-abandoned", layerIds: ["external-kdot-rail-abandoned-raster"], interactiveLayerIds: [],
    mapUrl: kdotLine("Railroads", 1, [246, 164, 111, 255], true), minDisplayZoom: 8,
    endpointLabel: "KDOT Railroads · provider-designated abandoned lines", color: "#f6a46f",
    sourceUrl: `${KDOT}/Railroads/MapServer/1`, serviceUrl: `${KDOT}/Railroads/MapServer`,
    legend: "Orange dashed lines · KDOT abandoned designation; not a dated reconstruction.",
    boundary: "Abandoned is a provider designation, not proof of track removal, abandonment date, railbanking, title, trail availability, or public access. This layer is a current reference to former routes, not a reconstruction at the selected historical year. External context only.",
  },
  {
    id: "fema-flood-zones", title: "FEMA Kansas mapped flood hazard zones", shortTitle: "FEMA flood zones",
    organization: "Federal Emergency Management Agency", domain: "Weather & hazards", kind: "OPERATIONAL_WMS",
    sourceId: "external-fema-flood-zones", layerIds: ["external-fema-flood-zones-raster"], interactiveLayerIds: [],
    mapUrl: `${NFHL}/export?bbox={bbox-epsg-3857}&bboxSR=3857&imageSR=3857&size=256%2C256&format=png32&transparent=true&layers=show%3A28&layerDefs=${encodeURIComponent(JSON.stringify({ 28: "DFIRM_ID LIKE '20%'" }))}&f=image`,
    endpointLabel: "FEMA NFHL · Kansas Flood Hazard Zones (28)", sourceUrl: `${NFHL}/28`, serviceUrl: NFHL,
    cadence: "Provider-current published NFHL map; panel effective dates vary",
    freshness: "Mapped hazard reference, not a current flood observation or warning",
    defaultVisibility: false, defaultOpacity: 0.65, color: "#66bed8", minDisplayZoom: 14, maxNativeZoom: 18,
    attribution: "FEMA National Flood Hazard Layer", evidenceRole: "EXTERNAL_CONTEXT_ONLY",
    legend: "Provider flood-zone colors and hatching. Open FEMA's legend for zone categories; blank areas are not a no-risk finding.",
    legendUrl: `${NFHL}/legend`,
    boundary: "Kansas NFHL zone imagery is a reference view with varying panel dates and incomplete national coverage. It is not current inundation, an alert, a property-specific regulatory determination, or a KFM release. Confirm the effective map and amendments at FEMA's Map Service Center before a property decision.",
    fallback: "Missing imagery or unmapped areas remain blank; no flood boundary, safety claim, or zone classification is inferred.",
  },
]);
