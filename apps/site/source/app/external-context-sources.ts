export type ExternalContextSourceId =
  | "openfreemap-liberty"
  | "esri-world-imagery"
  | "openstreetmap-standard"
  | "usgs-national-map-topo"
  | "aws-mapzen-terrarium";

export type ExternalContextActivation = "standard" | "imagery" | "streets" | "topo" | "elevation-3d";

export type ExternalContextSource = Readonly<{
  id: ExternalContextSourceId;
  title: string;
  organization: string;
  kind: "VECTOR_STYLE" | "RASTER_BASEMAP" | "RASTER_DEM";
  capabilities: readonly ("BASEMAP" | "STRUCTURES_3D" | "TERRAIN_3D" | "HILLSHADE")[];
  activatesWhen: readonly ExternalContextActivation[];
  requestMode: "DEFAULT_NETWORK" | "OPT_IN_NETWORK";
  requestUrl: string;
  endpointLabel: string;
  sourceUrl: string;
  attribution: string;
  evidenceRole: "DISPLAY_CONTEXT_ONLY";
  exportEffect: "ATTRIBUTION_ONLY";
  fallback: string;
  boundary: string;
}>;

/**
 * Complete top-level browser-requested map-carrier inventory for the current Site.
 *
 * These records drive both renderer configuration and the visible network
 * disclosure. Keeping the URLs and trust posture in one registry prevents a
 * basemap or terrain endpoint from becoming an undocumented evidence path.
 */
export const EXTERNAL_CONTEXT_SOURCES: readonly ExternalContextSource[] = Object.freeze([
  Object.freeze({
    id: "openfreemap-liberty",
    title: "OpenFreeMap Liberty vector context",
    organization: "OpenFreeMap / OpenMapTiles / OpenStreetMap",
    kind: "VECTOR_STYLE",
    capabilities: Object.freeze(["BASEMAP", "STRUCTURES_3D"] as const),
    activatesWhen: Object.freeze(["standard"] as const),
    requestMode: "DEFAULT_NETWORK",
    requestUrl: "https://tiles.openfreemap.org/styles/liberty",
    endpointLabel: "tiles.openfreemap.org",
    sourceUrl: "https://openfreemap.org/",
    attribution: "OpenFreeMap · OpenMapTiles · OpenStreetMap contributors",
    evidenceRole: "DISPLAY_CONTEXT_ONLY",
    exportEffect: "ATTRIBUTION_ONLY",
    fallback: "The Site switches to its local MapLibre style and keeps site-local layers, evidence text, and reports available.",
    boundary: "Vector geography and provider-supplied building heights are visual context. They are not KFM-admitted records, EvidenceBundles, or reportable claims.",
  }),
  Object.freeze({
    id: "esri-world-imagery",
    title: "Esri World Imagery",
    organization: "Esri",
    kind: "RASTER_BASEMAP",
    capabilities: Object.freeze(["BASEMAP"] as const),
    activatesWhen: Object.freeze(["imagery"] as const),
    requestMode: "OPT_IN_NETWORK",
    requestUrl: "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    endpointLabel: "server.arcgisonline.com",
    sourceUrl: "https://www.arcgis.com/home/item.html?id=10df2279f9684e4a9f6a7f08febac2a9",
    attribution: "Tiles © Esri",
    evidenceRole: "DISPLAY_CONTEXT_ONLY",
    exportEffect: "ATTRIBUTION_ONLY",
    fallback: "A failed imagery request leaves the Site's local evidence layers and non-imagery styles available.",
    boundary: "Imagery is a visual reference only. Acquisition dates, sensor lineage, change claims, and KFM release state are not resolved by this Site.",
  }),
  Object.freeze({
    id: "openstreetmap-standard",
    title: "OpenStreetMap raster context",
    organization: "OpenStreetMap contributors",
    kind: "RASTER_BASEMAP",
    capabilities: Object.freeze(["BASEMAP"] as const),
    activatesWhen: Object.freeze(["streets"] as const),
    requestMode: "OPT_IN_NETWORK",
    requestUrl: "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
    endpointLabel: "tile.openstreetmap.org",
    sourceUrl: "https://operations.osmfoundation.org/policies/tiles/",
    attribution: "© OpenStreetMap contributors",
    evidenceRole: "DISPLAY_CONTEXT_ONLY",
    exportEffect: "ATTRIBUTION_ONLY",
    fallback: "A failed tile request leaves the local styles and site-local evidence layers available.",
    boundary: "Raster tiles provide normal interactive navigation context only; the Site does not prefetch or offer offline use. Completeness, update time, legal status, routing, and KFM evidence support are not asserted.",
  }),
  Object.freeze({
    id: "usgs-national-map-topo",
    title: "USGS The National Map topographic context",
    organization: "U.S. Geological Survey",
    kind: "RASTER_BASEMAP",
    capabilities: Object.freeze(["BASEMAP"] as const),
    activatesWhen: Object.freeze(["topo"] as const),
    requestMode: "OPT_IN_NETWORK",
    requestUrl: "https://basemap.nationalmap.gov/arcgis/rest/services/USGSTopo/MapServer/tile/{z}/{y}/{x}",
    endpointLabel: "basemap.nationalmap.gov · USGSTopo",
    sourceUrl: "https://basemap.nationalmap.gov/arcgis/rest/services/USGSTopo/MapServer",
    attribution: "USGS The National Map",
    evidenceRole: "DISPLAY_CONTEXT_ONLY",
    exportEffect: "ATTRIBUTION_ONLY",
    fallback: "A failed USGS topographic tile request leaves local styles and site-local evidence layers available.",
    boundary: "The National Map tiles are cartographic display context. Contours, names, symbology, currency, scale fitness, and KFM evidence support are not asserted by this Site.",
  }),
  Object.freeze({
    id: "aws-mapzen-terrarium",
    title: "Terrain Tiles · Terrarium",
    organization: "AWS Open Data / Mapzen",
    kind: "RASTER_DEM",
    capabilities: Object.freeze(["TERRAIN_3D", "HILLSHADE"] as const),
    activatesWhen: Object.freeze(["elevation-3d"] as const),
    requestMode: "OPT_IN_NETWORK",
    requestUrl: "https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png",
    endpointLabel: "s3.amazonaws.com/elevation-tiles-prod",
    sourceUrl: "https://registry.opendata.aws/terrain-tiles/",
    attribution: "Terrain Tiles · Mapzen · AWS Open Data",
    evidenceRole: "DISPLAY_CONTEXT_ONLY",
    exportEffect: "ATTRIBUTION_ONLY",
    fallback: "A failed DEM request removes terrain and preserves the 2D map, selection, evidence, and reporting path.",
    boundary: "Rendered relief is contextual. The Site does not sample or export elevations as KFM evidence, accuracy claims, survey results, or an admitted 3DEP product.",
  }),
]);

export const externalContextSource = (id: ExternalContextSourceId): ExternalContextSource => {
  const source = EXTERNAL_CONTEXT_SOURCES.find((candidate) => candidate.id === id);
  if (!source) throw new Error(`Unknown external context source: ${id}`);
  return source;
};
