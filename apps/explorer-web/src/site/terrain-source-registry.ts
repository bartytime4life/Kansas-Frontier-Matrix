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
 * - AUTHORITATIVE_CANDIDATE may be pinned but still needs admission and release decisions.
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
    id: "terrain-usgs-3dep-1m-x56y429",
    title: "USGS 3DEP 1 m · 14 x56y429 · KS Statewide 2018",
    organization: "U.S. Geological Survey",
    role: "AUTHORITATIVE_CANDIDATE",
    resolution: "1 m cells · 10,012 × 10,012 including border",
    format: "Float32 GeoTIFF · NAVD88 metres · nodata −999999",
    coverage: "One nominal 10 km tile intersecting the public-safe Ellsworth pilot area",
    sourceUrl:
      "https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/1m/Projects/KS_Statewide_2018_A18/metadata/USGS_1M_14_x56y429_KS_Statewide_2018_A18.xml",
    attribution: "U.S. Geological Survey 3D Elevation Program",
    boundary:
      "Fixture-only HOLD. Exact tile and metadata hashes are recorded, but delivered-tile geoid, applicable numeric vertical accuracy, human review, source admission, runtime loading, and release remain unresolved.",
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
    } else if (
      "tileTemplate" in source ||
      "encoding" in source ||
      "tileSize" in source ||
      "maxZoom" in source
    ) {
      issues.push(`non-display record must not expose runtime tile metadata: ${source.id}`);
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
