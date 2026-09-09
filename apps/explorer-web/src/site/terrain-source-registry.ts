export type TerrainSourceRole =
  | "DISPLAY_CONTEXT"
  | "AUTHORITATIVE_CANDIDATE"
  | "IMPLEMENTATION_SPEC";

export type TerrainEncoding = "terrarium" | "mapbox";

export interface TerrainSourceRecord {
  readonly id: string;
  readonly title: string;
  readonly organization: string;
  readonly role: TerrainSourceRole;
  readonly resolution: string;
  readonly format: string;
  readonly coverage: string;
  readonly sourceUrl: string;
  readonly tileTemplate?: string;
  readonly encoding?: TerrainEncoding;
  readonly tileSize?: number;
  readonly maxZoom?: number;
  readonly attribution: string;
  readonly boundary: string;
}

/**
 * Source roles are intentionally separate:
 * - DISPLAY_CONTEXT can support reversible rendering, never an evidence claim.
 * - AUTHORITATIVE_CANDIDATE still needs a pinned product and admission receipt.
 * - IMPLEMENTATION_SPEC describes renderer compatibility, not data authority.
 */
export const TERRAIN_SOURCES = Object.freeze([
  Object.freeze({
    id: "terrain-aws-mapzen-terrarium",
    title: "Terrain Tiles · Terrarium",
    organization: "AWS Open Data / Mapzen",
    role: "DISPLAY_CONTEXT",
    resolution: "Source-dependent global mosaic; visual context only",
    format: "256 px Terrarium PNG raster-dem tiles",
    coverage: "Global",
    sourceUrl: "https://registry.opendata.aws/terrain-tiles/",
    tileTemplate:
      "https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png",
    encoding: "terrarium",
    tileSize: 256,
    maxZoom: 15,
    attribution: "Terrain Tiles · Mapzen · AWS Open Data",
    boundary:
      "A directly compatible, key-free display carrier. It must not become a KFM elevation measurement, evidence record, or release claim.",
  }),
  Object.freeze({
    id: "terrain-usgs-3dep-13arc",
    title: "USGS 3DEP 1/3 arc-second DEM",
    organization: "U.S. Geological Survey",
    role: "AUTHORITATIVE_CANDIDATE",
    resolution: "Approximately 10 m",
    format: "Cloud Optimized GeoTIFF and National Map services",
    coverage: "United States, including Kansas",
    sourceUrl:
      "https://data.usgs.gov/datacatalog/data/USGS%3A3a81321b-c153-416f-98b7-cc8e5f0e17c3",
    attribution: "U.S. Geological Survey 3D Elevation Program",
    boundary:
      "Admission requires a pinned product and datum, a reproducible MapLibre-compatible derivative, lineage, performance proof, 2D parity, and release review.",
  }),
  Object.freeze({
    id: "terrain-maplibre-raster-dem",
    title: "MapLibre raster-dem contract",
    organization: "MapLibre",
    role: "IMPLEMENTATION_SPEC",
    resolution: "Not a dataset",
    format: "Mapbox Terrain RGB, Mapzen Terrarium, or custom RGB encoding",
    coverage: "Renderer contract",
    sourceUrl:
      "https://maplibre.org/maplibre-style-spec/sources/#raster-dem",
    attribution: "MapLibre Style Specification",
    boundary:
      "Defines compatible raster-dem encodings. It does not establish source authority, accuracy, rights, freshness, admission, or release.",
  }),
] as const satisfies readonly TerrainSourceRecord[]);

export const getTerrainDisplaySource = (): TerrainSourceRecord => {
  const source = TERRAIN_SOURCES.find(
    (candidate) => candidate.role === "DISPLAY_CONTEXT",
  );
  if (source === undefined) {
    throw new Error("Terrain source registry has no display-context carrier.");
  }
  return source;
};

export const validateTerrainSourceRegistry = (): readonly string[] => {
  const issues: string[] = [];
  const ids = new Set<string>();

  for (const source of TERRAIN_SOURCES as readonly TerrainSourceRecord[]) {
    if (ids.has(source.id)) issues.push(`duplicate id: ${source.id}`);
    ids.add(source.id);
    if (!source.sourceUrl.startsWith("https://")) {
      issues.push(`source URL must use HTTPS: ${source.id}`);
    }
    if (source.role === "DISPLAY_CONTEXT") {
      if (!("tileTemplate" in source) || !("encoding" in source)) {
        issues.push(`display carrier is missing tile metadata: ${source.id}`);
      }
    }
  }

  if (
    TERRAIN_SOURCES.filter(
      (source) => source.role === "DISPLAY_CONTEXT",
    ).length !== 1
  ) {
    issues.push("exactly one display-context terrain carrier is required");
  }

  return Object.freeze(issues);
};
