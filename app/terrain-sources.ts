import { externalContextSource } from "./external-context-sources";

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

const activeTerrainContext = externalContextSource("aws-mapzen-terrarium");

/**
 * The upstream Terrarium pyramid contains isolated, implausible high-zoom
 * samples around the prior Smoky Hills investigation camera (including a sharp
 * negative discontinuity near Ellsworth). MapLibre turns those samples into
 * vertical terrain walls. Zoom 11 is the highest inspected level that keeps
 * this investigation view continuous; deeper map zooms deliberately overzoom the clean z11 DEM.
 */
export const TERRARIUM_RENDER_MAX_ZOOM = 11;

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
    title: activeTerrainContext.title,
    organization: activeTerrainContext.organization,
    status: "ACTIVE_CONTEXT",
    role: "Key-free raster DEM display carrier",
    resolution: "Source-dependent global mosaic; renderer capped at zoom 11 for continuity; visual context only",
    format: "256 px Terrarium PNG raster-dem tiles",
    coverage: "Global",
    sourceUrl: activeTerrainContext.sourceUrl,
    tileTemplate: activeTerrainContext.requestUrl,
    encoding: "terrarium",
    tileSize: 256,
    maxZoom: TERRARIUM_RENDER_MAX_ZOOM,
    attribution: activeTerrainContext.attribution,
    boundary: `${activeTerrainContext.boundary} High-zoom upstream discontinuities are excluded by a renderer safety cap; closer views overzoom the inspected continuous DEM level instead.`,
  }),
  Object.freeze({
    id: "terrain-usgs-3dep-13arc",
    title: "USGS 3DEP LiDAR-derived DEM family",
    organization: "U.S. Geological Survey",
    status: "CANDIDATE",
    role: "Authoritative Kansas elevation / LiDAR-derived terrain candidate",
    resolution: "Work-unit dependent: 1 m project products through approximately 10 m seamless DEM",
    format: "LiDAR point clouds, Cloud Optimized GeoTIFF, XML/GeoPackage metadata, and National Map services",
    coverage: "United States, including Kansas",
    sourceUrl: "https://www.usgs.gov/3d-elevation-program/about-3dep-products-services",
    attribution: "U.S. Geological Survey 3D Elevation Program",
    boundary: "The map may show an attributed dynamic 3DEP hillshade or slope visualization, but it does not request raw point clouds or claim that a rendered pixel identifies one work unit, pulse spacing, vertical datum, acquisition interval, or accuracy. Admission requires a pinned product/version, preserved XML and spatial metadata, a reproducible Terrain RGB or Terrarium derivative, lineage, performance proof, and an evidence-parity fallback.",
  }),
  Object.freeze({
    id: "terrain-usgs-3dep-lidar-metadata",
    title: "USGS 3DEP LiDAR availability + work-unit metadata",
    organization: "U.S. Geological Survey",
    status: "CANDIDATE",
    role: "LiDAR coverage and provenance discovery",
    resolution: "Work-unit metadata; not a renderer surface",
    format: "Lidar Explorer, WESM GeoPackage, product XML, point-cloud/DEM download catalogs",
    coverage: "United States, including Kansas",
    sourceUrl: "https://apps.nationalmap.gov/lidar-explorer/",
    attribution: "U.S. Geological Survey 3D Elevation Program",
    boundary: "This record scaffolds the work-unit and provenance path for future Kansas LiDAR features. It is not itself an admitted dataset, raw point-cloud fetch, elevation answer, or release; exact work unit, product, CRS/datum, classification, quality level, and rights remain required before activation.",
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
