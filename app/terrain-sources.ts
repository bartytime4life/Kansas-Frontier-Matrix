export type TerrainSourceStatus = "ACTIVE_CONTEXT" | "CANDIDATE" | "IMPLEMENTATION_SPEC";

export type TerrainSourceRecord = Readonly<{
  id: string;
  title: string;
  organization: string;
  status: TerrainSourceStatus;
  role: string;
  resolution: string;
  format: string;
  coverage: string;
  sourceUrl: string;
  tileTemplate?: string;
  encoding?: "terrarium" | "mapbox";
  tileSize?: number;
  maxZoom?: number;
  attribution: string;
  boundary: string;
}>;

/**
 * Terrain sources stay explicit and role-separated:
 * - ACTIVE_CONTEXT may be requested by MapLibre for visual terrain only.
 * - CANDIDATE is authoritative source material that still needs a governed
 *   transform, versioned artifact, rights review, and admission receipt.
 * - IMPLEMENTATION_SPEC defines renderer compatibility, not data authority.
 */
export const TERRAIN_SOURCES: readonly TerrainSourceRecord[] = Object.freeze([
  Object.freeze({
    id: "terrain-aws-mapzen-terrarium",
    title: "Terrain Tiles · Terrarium",
    organization: "AWS Open Data / Mapzen",
    status: "ACTIVE_CONTEXT",
    role: "Key-free raster DEM display carrier",
    resolution: "Source-dependent global mosaic; visual context only",
    format: "256 px Terrarium PNG raster-dem tiles",
    coverage: "Global",
    sourceUrl: "https://registry.opendata.aws/terrain-tiles/",
    tileTemplate: "https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png",
    encoding: "terrarium",
    tileSize: 256,
    maxZoom: 15,
    attribution: "Terrain Tiles · Mapzen · AWS Open Data",
    boundary: "Active only when Terrain 3D is selected. It is external display context, not admitted KFM evidence or a source of reportable elevation values.",
  }),
  Object.freeze({
    id: "terrain-usgs-3dep-13arc",
    title: "USGS 3DEP 1/3 arc-second DEM",
    organization: "U.S. Geological Survey",
    status: "CANDIDATE",
    role: "Authoritative Kansas elevation candidate",
    resolution: "Approximately 10 m",
    format: "Cloud Optimized GeoTIFF and National Map services",
    coverage: "United States, including Kansas",
    sourceUrl: "https://data.usgs.gov/datacatalog/data/USGS%3A3a81321b-c153-416f-98b7-cc8e5f0e17c3",
    attribution: "U.S. Geological Survey 3D Elevation Program",
    boundary: "Not requested by the browser today. Admission requires a pinned product/version, a reproducible Terrain RGB or Terrarium derivative, lineage, performance proof, and evidence-parity fallback.",
  }),
  Object.freeze({
    id: "terrain-maplibre-raster-dem",
    title: "MapLibre raster-dem contract",
    organization: "MapLibre",
    status: "IMPLEMENTATION_SPEC",
    role: "Renderer compatibility specification",
    resolution: "Not a dataset",
    format: "Mapbox Terrain RGB, Mapzen Terrarium, or custom RGB encoding",
    coverage: "Renderer contract",
    sourceUrl: "https://maplibre.org/maplibre-style-spec/sources/#raster-dem",
    attribution: "MapLibre Style Specification",
    boundary: "Confirms how compatible DEM tiles are decoded and rendered. It does not establish source authority, rights, accuracy, freshness, admission, or release.",
  }),
]);

export const ACTIVE_TERRAIN_SOURCE = TERRAIN_SOURCES[0];

export const STRUCTURE_3D_SOURCE: TerrainSourceRecord = Object.freeze({
  id: "structures-openfreemap-liberty",
  title: "OpenFreeMap Liberty building extrusion",
  organization: "OpenFreeMap / OpenMapTiles / OpenStreetMap",
  status: "ACTIVE_CONTEXT",
  role: "Provider-height 3D structures display carrier",
  resolution: "Vector-tile building coverage; attributes vary by place",
  format: "MVT building source layer + MapLibre fill-extrusion",
  coverage: "Global display context, including Kansas where mapped",
  sourceUrl: "https://github.com/hyperknot/openfreemap",
  attribution: "OpenFreeMap · OpenMapTiles · OpenStreetMap contributors",
  boundary: "Visible only at city-scale zoom when the Liberty style supplies its building-3d layer. The Site neither fills missing heights nor treats building geometry as KFM evidence.",
});
