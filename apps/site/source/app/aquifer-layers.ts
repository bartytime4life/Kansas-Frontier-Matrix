import type { OfficialContextSource } from "./live-context";

const KGS_AQUIFERS = "https://services.kansasgis.org/arcgis8/rest/services/wwc5/wwc5_v2/MapServer";
export const KGS_ATLAS_URL = "https://www.kgs.ku.edu/HighPlains/HPA_Atlas/index.html";
export const GROUNDWATER_MANIFEST = [{"id": "kgs-water-table", "title": "Water-table elevation", "serviceUrl": "https://services2.arcgis.com/ZOdjAzAQ2B0f85zi/arcgis/rest/services/Kansas_HPA_water_table_elevation/FeatureServer/0", "retrievedAt": "2026-10-04T06:16:24.110758+00:00", "featureCount": 25, "generalizationDegrees": 0.0005, "field": "wte_2022_2024_MANUAL", "legend": [{"value": 1, "label": "1300 to 1500", "color": "#ffd3c9"}, {"value": 2, "label": "1500 to 1600", "color": "#f2bcb1"}, {"value": 3, "label": "1600 to 1700", "color": "#e8aa9e"}, {"value": 4, "label": "1700 to 1800", "color": "#e09f8d"}, {"value": 5, "label": "1800 to 1900", "color": "#d9997e"}, {"value": 6, "label": "1900 to 2000", "color": "#d49670"}, {"value": 7, "label": "2000 to 2100", "color": "#d99b6f"}, {"value": 8, "label": "2100 to 2200", "color": "#dea06a"}, {"value": 9, "label": "2200 to 2300", "color": "#e3a766"}, {"value": 10, "label": "2300 to 2400", "color": "#ebb26c"}, {"value": 11, "label": "2400 to 2500", "color": "#f2c074"}, {"value": 12, "label": "2500 to 2600", "color": "#facb7a"}, {"value": 13, "label": "2600 to 2700", "color": "#ffd782"}, {"value": 14, "label": "2700 to 2800", "color": "#ffe587"}, {"value": 15, "label": "2800 to 2900", "color": "#fff08f"}, {"value": 16, "label": "2900 to 3000", "color": "#fffa94"}, {"value": 17, "label": "3000 to 3100", "color": "#f6f78f"}, {"value": 18, "label": "3100 to 3200", "color": "#e1e683"}, {"value": 19, "label": "3200 to 3300", "color": "#cdd678"}, {"value": 20, "label": "3300 to 3400", "color": "#b9c76d"}, {"value": 21, "label": "3400 to 3500", "color": "#a8b863"}, {"value": 22, "label": "3500 to 3600", "color": "#95a858"}, {"value": 23, "label": "3600 to 3700", "color": "#82964d"}, {"value": 24, "label": "3700 to 3900", "color": "#718744"}], "bytes": 207331}, {"id": "kgs-saturated-thickness", "title": "Saturated thickness", "serviceUrl": "https://services2.arcgis.com/ZOdjAzAQ2B0f85zi/arcgis/rest/services/Kansas_HPA_thickness_2022_2024/FeatureServer/0", "retrievedAt": "2026-10-04T06:16:24.630206+00:00", "featureCount": 8, "generalizationDegrees": 0.0005, "field": "satthick_2022_2024_MANUAL", "legend": [{"value": 1, "label": "Under 50", "color": "#ffff73"}, {"value": 2, "label": "50 to 100", "color": "#95ff5e"}, {"value": 3, "label": "100 to 150", "color": "#00f240"}, {"value": 4, "label": "150 to 200", "color": "#00ab73"}, {"value": 5, "label": "200 to 250", "color": "#1d9eb9"}, {"value": 6, "label": "250 to 300", "color": "#225ea8"}, {"value": 7, "label": "Over 300", "color": "#0c2c84"}], "bytes": 468448}, {"id": "kgs-depth-to-water", "title": "Depth to water", "serviceUrl": "https://services2.arcgis.com/ZOdjAzAQ2B0f85zi/arcgis/rest/services/Kansas_HPA_Depth_to_Water/FeatureServer/0", "retrievedAt": "2026-10-04T06:16:24.148578+00:00", "featureCount": 10, "generalizationDegrees": 0.0005, "field": "dtw_2022_2024_MANUAL_RANGE", "legend": [{"value": "0.000000 - 25.000000", "label": "Under 25", "color": "#ffff80"}, {"value": "25.000001 - 50.000000", "label": "25 to 50", "color": "#fde86a"}, {"value": "50.000001 - 100.000000", "label": "50 to 100", "color": "#fbd255"}, {"value": "100.000001 - 150.000000", "label": "100 to 150", "color": "#f7bc41"}, {"value": "150.000001 - 200.000000", "label": "150 to 200", "color": "#f2a72e"}, {"value": "200.000001 - 250.000000", "label": "200 to 250", "color": "#ce7b20"}, {"value": "250.000001 - 300.000000", "label": "250 to 300", "color": "#ac5213"}, {"value": "300.000001 - 350.000000", "label": "300 to 350", "color": "#8b2e09"}, {"value": "350.000001 - 800.000000", "label": "Over 350", "color": "#6b0000"}], "bytes": 673788}, {"id": "kgs-monitoring-wells", "title": "Monitoring locations", "serviceUrl": "https://services2.arcgis.com/ZOdjAzAQ2B0f85zi/arcgis/rest/services/Annual_measurement_wells_2026/FeatureServer/0", "retrievedAt": "2026-10-04T06:16:24.364474+00:00", "featureCount": 1384, "generalizationDegrees": 0, "field": null, "legend": [], "bytes": 614393}] as const;

export function safeKgsWellUrl(value: unknown): string | null {
  if (typeof value !== "string") return null;
  try { const url = new URL(value); return url.protocol === "https:" && url.hostname === "geohydro.kgs.ku.edu" && url.pathname === "/geohydro/wizard/wizardwelldetail.cfm" && /^\d{14,15}$/.test(url.searchParams.get("usgs_id") ?? "") ? url.href : null; } catch { return null; }
}

const boundaries = [["alluvial", 4, "Alluvial", "#62d9e7"], ["dakota", 5, "Dakota", "#e9bd74"], ["glacial-drift", 6, "Glacial Drift", "#b5afea"], ["high-plains", 7, "High Plains", "#55c7a4"], ["ozark", 8, "Ozark", "#ed9aa9"], ["osage", 10, "Osage", "#b4d477"], ["flint-hills", 11, "Flint Hills", "#f5a869"]] as const;
export const AQUIFER_RASTER_SOURCES: readonly OfficialContextSource[] = boundaries.map(([slug, layer, name, color]) => {
  const id = `kgs-aquifer-${slug}` as OfficialContextSource["id"];
  const rgb = [1, 3, 5].map(offset => parseInt(color.slice(offset, offset + 2), 16));
  const dynamicLayers = [{ id: layer, source: { type: "mapLayer", mapLayerId: layer }, drawingInfo: { showLabels: false, renderer: { type: "simple", symbol: {
    type: "esriSFS", style: "esriSFSSolid", color: [...rgb, 150], outline: { type: "esriSLS", style: "esriSLSSolid", color: [...rgb, 255], width: 1.2 },
  } } } }];
  return {
    id, title: `KGS ${name} Aquifer reference extent`, shortTitle: `${name} aquifer`, organization: "Kansas Geological Survey", domain: "Aquifers & groundwater",
    kind: "OPERATIONAL_WMS", sourceId: `external-${id}`, layerIds: [`external-${id}-raster`], interactiveLayerIds: [],
    mapUrl: `${KGS_AQUIFERS}/export?bbox={bbox-epsg-3857}&bboxSR=3857&imageSR=3857&size=256%2C256&format=png32&transparent=true&layers=show%3A${layer}&dynamicLayers=${encodeURIComponent(JSON.stringify(dynamicLayers))}&f=image`,
    sourceUrl: `${KGS_AQUIFERS}/${layer}`, serviceUrl: KGS_AQUIFERS, endpointLabel: `KGS WWC5 map · aquifer layer ${layer}`,
    cadence: "Provider-served reference extent", freshness: "Reference boundary · source vintage not supplied",
    defaultVisibility: false, defaultOpacity: 0.65, color, minDisplayZoom: 5, maxNativeZoom: 14,
    attribution: "Kansas Geological Survey · aquifer reference boundaries", evidenceRole: "EXTERNAL_CONTEXT_ONLY",
    legend: `${name} aquifer mapped extent · translucent fill and outline`,
    boundary: "Regional aquifer reference extent, not a measured depth, present water supply, ownership, or parcel-scale delineation. Aquifers can overlap at different depths. Source vintage is not supplied.",
    fallback: "Provider image failure leaves this layer unavailable; no extent is inferred.",
  };
});

export const GROUNDWATER_SNAPSHOT_SOURCES: readonly OfficialContextSource[] = GROUNDWATER_MANIFEST.map(item => {
  const well = item.id === "kgs-monitoring-wells";
  return {
    id: item.id, title: `KGS ${item.title} · ${well ? "2026 locations" : "High Plains 2022–2024"}`, shortTitle: `${item.title} · ${well ? "2026" : "2022–2024"}`,
    organization: "Kansas Geological Survey", domain: "Aquifers & groundwater", kind: "SNAPSHOT_GEOJSON",
    sourceId: `external-${item.id}`, layerIds: [`external-${item.id}-${well ? "points" : "fill"}`], interactiveLayerIds: [`external-${item.id}-${well ? "points" : "fill"}`],
    mapUrl: `/data/groundwater/${item.id}.geojson`, sourceUrl: item.serviceUrl, serviceUrl: item.serviceUrl,
    endpointLabel: "KGS High Plains Atlas · checked snapshot", cadence: "Pinned snapshot retrieved 2026-10-04; not automatically refreshed",
    freshness: well ? "2026 monitoring locations · no water-level measurements attached" : "2022–2024 regional classified estimates",
    defaultVisibility: false, defaultOpacity: well ? 0.95 : 0.65, color: well ? "#f4d57d" : "#64c8bc",
    attribution: "Kansas Geological Survey · High Plains Aquifer Atlas", evidenceRole: "EXTERNAL_CONTEXT_ONLY",
    legend: well ? "Monitoring location · click for KGS well record" : "Provider classes in feet · click a mapped region to inspect its range",
    boundary: well ? "Monitoring locations from the 2026 network layer. Location membership does not establish a current measurement or a continuous record. Open the KGS well record to inspect observations."
      : "Regional 2022–2024 classified estimates; polygon class codes are not measurements. Geometry generalized to 0.0005 degrees for display. Not a parcel measurement, present condition, or precise hydraulic-head grid; no groundwater direction or velocity is inferred.",
    fallback: "Snapshot gaps and unclassified areas remain blank; missing coverage does not mean zero water.",
  };
});
