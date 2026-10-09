import type { FeatureCollection, Polygon } from "geojson";
import { terrainDrawingCoordinate, type DrawingPoint, type TerrainDrawingGrid } from "./terrain-drawing";

export type TerrainSurfaceMode = "off" | "slope" | "aspect";
export type TerrainAspectDirection = "N" | "NE" | "E" | "SE" | "S" | "SW" | "W" | "NW" | "Flat";
export type TerrainSurfaceProbe = Readonly<{
  slopeDegrees: number; aspectDegrees: number | null; elevationMeters: number;
  center: DrawingPoint; spacingMeters: number;
}>;
export const TERRAIN_SURFACE_FLAT_DEGREES = 0.5;
export const TERRAIN_SURFACE_MAX_CELLS = 63 * 63;
export const TERRAIN_SLOPE_LEGEND = Object.freeze([
  { key: "gentle", label: "<2°", color: "#356d86" },
  { key: "low", label: "2–5°", color: "#72aa9d" },
  { key: "moderate", label: "5–10°", color: "#d8bc65" },
  { key: "steep", label: "10–20°", color: "#e08b4e" },
  { key: "very-steep", label: "≥20°", color: "#c65043" },
] as const);
export const TERRAIN_ASPECT_LEGEND = Object.freeze([
  { key: "N", label: "N", color: "#497bb1" },
  { key: "NE", label: "NE", color: "#50a6ba" },
  { key: "E", label: "E", color: "#6a9d64" },
  { key: "SE", label: "SE", color: "#b8b755" },
  { key: "S", label: "S", color: "#dc9a45" },
  { key: "SW", label: "SW", color: "#d76b58" },
  { key: "W", label: "W", color: "#ae638d" },
  { key: "NW", label: "NW", color: "#8075b1" },
  { key: "Flat", label: "Flat", color: "#858d91" },
] as const);

export const terrainSlopeBand = (slope: number) => slope < 2 ? TERRAIN_SLOPE_LEGEND[0] : slope < 5 ? TERRAIN_SLOPE_LEGEND[1] : slope < 10 ? TERRAIN_SLOPE_LEGEND[2] : slope < 20 ? TERRAIN_SLOPE_LEGEND[3] : TERRAIN_SLOPE_LEGEND[4];
export function terrainAspectDirection(aspect: number | null): TerrainAspectDirection {
  if (aspect === null || !Number.isFinite(aspect)) return "Flat";
  return TERRAIN_ASPECT_LEGEND[Math.floor(((((aspect % 360) + 360) % 360) + 22.5) / 45) % 8].key;
}
export const terrainSurfaceOpacity = (value: number | undefined) => Number.isFinite(value) ? Math.max(0.2, Math.min(0.75, value!)) : 0.55;

export type TerrainSurfaceCell = TerrainSurfaceProbe & Readonly<{ id: number; row: number; column: number }>;
export type TerrainSurfaceProperties = Readonly<{
  role: "surface"; slopeDegrees: number; aspectDegrees: number | null;
  elevationMeters: number; slopeBand: string; aspectDirection: TerrainAspectDirection;
  slopeColor: string; aspectColor: string;
}>;
export type TerrainSurfaceGeometry = Readonly<{
  data: FeatureCollection<Polygon, TerrainSurfaceProperties>;
  cells: ReadonlyMap<number, TerrainSurfaceCell>;
  totalCellCount: number;
}>;

const validGrid = (grid: TerrainDrawingGrid) => Number.isInteger(grid.size) && grid.size >= 3 && grid.size <= 65
  && grid.heights.length === grid.size ** 2 && grid.bounds.length === 4 && grid.bounds.every(Number.isFinite)
  && grid.bounds[0] < grid.bounds[2] && grid.bounds[1] < grid.bounds[3]
  && grid.bounds[0] >= -180 && grid.bounds[2] <= 180 && grid.bounds[1] > -90 && grid.bounds[3] < 90
  && Number.isFinite(grid.spacingMeters) && grid.spacingMeters > 0;

/** Horn 3×3 derivatives over the loaded samples. Rows run north to south;
 * downhill aspect is clockwise from north. No neighbor may be missing.
 * Reference: https://gdal.org/en/stable/programs/gdaldem.html */
export function terrainSurfaceCell(grid: TerrainDrawingGrid, row: number, column: number): TerrainSurfaceCell | null {
  if (!validGrid(grid) || !Number.isInteger(row) || !Number.isInteger(column) || row < 1 || column < 1 || row >= grid.size - 1 || column >= grid.size - 1) return null;
  const id = row * grid.size + column;
  const values = [-grid.size - 1, -grid.size, -grid.size + 1, -1, 0, 1, grid.size - 1, grid.size, grid.size + 1].map(offset => grid.heights[id + offset]);
  if (values.some(value => typeof value !== "number" || !Number.isFinite(value))) return null;
  const [a, b, c, d, e, f, g, h, i] = values as number[];
  const center = terrainDrawingCoordinate(grid, id);
  const eastSpacing = (grid.bounds[2] - grid.bounds[0]) / (grid.size - 1) * 111_320 * Math.cos(center[1] * Math.PI / 180);
  const northSpacing = (grid.bounds[3] - grid.bounds[1]) / (grid.size - 1) * 111_320;
  if (!(eastSpacing > 0) || !(northSpacing > 0)) return null;
  const east = ((c + 2 * f + i) - (a + 2 * d + g)) / (8 * eastSpacing);
  const north = ((a + 2 * b + c) - (g + 2 * h + i)) / (8 * northSpacing);
  const slopeDegrees = Math.atan(Math.hypot(east, north)) * 180 / Math.PI;
  const aspectDegrees = slopeDegrees < TERRAIN_SURFACE_FLAT_DEGREES ? null : ((Math.atan2(-east, -north) * 180 / Math.PI) + 360) % 360;
  if (!Number.isFinite(slopeDegrees) || (aspectDegrees !== null && !Number.isFinite(aspectDegrees))) return null;
  return { id, row, column, slopeDegrees, aspectDegrees, elevationMeters: e, center, spacingMeters: Math.max(eastSpacing, northSpacing) };
}

/** Native fill polygons are centered on interior samples, not extrapolated to
 * the unsampled outer rim. At most 3969 cells, yielding every four rows. */
export function* terrainSurfaceGeometryBatches(grid: TerrainDrawingGrid): Generator<void, TerrainSurfaceGeometry> {
  const data: TerrainSurfaceGeometry["data"] = { type: "FeatureCollection", features: [] };
  const cells = new Map<number, TerrainSurfaceCell>();
  if (!validGrid(grid)) return { data, cells, totalCellCount: 0 };
  const halfLongitude = (grid.bounds[2] - grid.bounds[0]) / (grid.size - 1) / 2;
  const halfLatitude = (grid.bounds[3] - grid.bounds[1]) / (grid.size - 1) / 2;
  for (let row = 1; row < grid.size - 1; row += 1) {
    for (let column = 1; column < grid.size - 1; column += 1) {
      const cell = terrainSurfaceCell(grid, row, column);
      if (!cell) continue;
      cells.set(cell.id, cell);
      const [longitude, latitude] = cell.center;
      const west = longitude - halfLongitude, east = longitude + halfLongitude, south = latitude - halfLatitude, north = latitude + halfLatitude;
      const slope = terrainSlopeBand(cell.slopeDegrees), direction = terrainAspectDirection(cell.aspectDegrees);
      const aspect = TERRAIN_ASPECT_LEGEND.find(entry => entry.key === direction)!;
      data.features.push({
        type: "Feature", id: cell.id,
        properties: { role: "surface", slopeDegrees: cell.slopeDegrees, aspectDegrees: cell.aspectDegrees, elevationMeters: cell.elevationMeters, slopeBand: slope.key, aspectDirection: direction, slopeColor: slope.color, aspectColor: aspect.color },
        geometry: { type: "Polygon", coordinates: [[[west, north], [west, south], [east, south], [east, north], [west, north]]] },
      });
    }
    if (row % 4 === 0) yield;
  }
  return { data, cells, totalCellCount: (grid.size - 2) ** 2 };
}

export function buildTerrainSurfaceGeometry(grid: TerrainDrawingGrid): TerrainSurfaceGeometry {
  const batches = terrainSurfaceGeometryBatches(grid);
  let next = batches.next();
  while (!next.done) next = batches.next();
  return next.value;
}

/** Resolve only a valid cached cell; never query arbitrary map features or
 * interpolate into an unavailable neighbor or beyond the interior footprint. */
export function terrainSurfaceCellAt(grid: Pick<TerrainDrawingGrid, "size" | "bounds">, cells: ReadonlyMap<number, TerrainSurfaceCell>, coordinate: DrawingPoint): TerrainSurfaceCell | null {
  if (!coordinate.every(Number.isFinite) || grid.size < 3) return null;
  const longitudeStep = (grid.bounds[2] - grid.bounds[0]) / (grid.size - 1);
  const latitudeStep = (grid.bounds[3] - grid.bounds[1]) / (grid.size - 1);
  if (!(longitudeStep > 0) || !(latitudeStep > 0)) return null;
  const column = Math.floor((coordinate[0] - grid.bounds[0]) / longitudeStep + 0.5);
  const row = Math.floor((grid.bounds[3] - coordinate[1]) / latitudeStep + 0.5);
  if (column < 1 || row < 1 || column >= grid.size - 1 || row >= grid.size - 1) return null;
  return cells.get(row * grid.size + column) ?? null;
}
