import type { FeatureCollection, MultiLineString } from "geojson";
import type { SceneLightPreset } from "./scene-effects";
import type { TerrainProvider } from "./terrain-sources";
import type { TerrainSurfaceMode } from "./terrain-surface";
export type { TerrainSurfaceMode, TerrainSurfaceProbe } from "./terrain-surface";

export type TerrainDrawingMode = "off" | "contours" | "grid" | "both";
export type TerrainDrawingConfig = Readonly<{
  mode: TerrainDrawingMode; enabled: boolean; provider: TerrainProvider;
  efficient: boolean; detail: boolean; light: SceneLightPreset; azimuth: number;
  surface?: TerrainSurfaceMode; surfaceOpacity?: number; probeEnabled?: boolean;
}>;
export type TerrainDrawingStatus = Readonly<{
  state: "off" | "unavailable" | "loading" | "ready";
  message: string; intervalMeters: number | null; spacingMeters: number | null;
  coverage: number; sampleCount?: number; validCellCount?: number; totalCellCount?: number;
}>;
export const TERRAIN_DRAWING_INITIAL_STATUS: TerrainDrawingStatus = Object.freeze({
  state: "off", message: "Loaded display DEM · gaps stay empty", intervalMeters: null, spacingMeters: null, coverage: 0,
});
export const TERRAIN_DRAWING_MIN_ZOOM = 8.5;
export const TERRAIN_DRAWING_MAX_SAMPLES = 65 * 65;
export const TERRAIN_DRAWING_MAX_SEGMENTS = 16_000;
export const TERRAIN_DRAWING_MAX_LEVELS = 48;
// This is the same Kansas focus box in which the terrain reader can safely
// distinguish MapLibre's missing-tile zero from a legitimate sea-level value.
export const TERRAIN_DRAWING_BOUNDS = [-102.1, 36.9, -94.5, 40.1] as const;
export type DrawingPoint = [number, number];
export type TerrainDrawingGrid = Readonly<{
  size: number; bounds: readonly [number, number, number, number];
  spacingMeters: number; heights: readonly (number | null)[];
}>;
export type TerrainDrawingProperties = { role: "contour" | "grid"; index: boolean; elevation?: number };
export type TerrainDrawingData = FeatureCollection<MultiLineString, TerrainDrawingProperties>;
export type TerrainDrawingGeometry = Readonly<{
  data: TerrainDrawingData; intervalMeters: number | null; coverage: number;
  sampleCount: number; segmentCount: number; clipped: boolean;
}>;

/** A bounded geographic footprint, independent of pitch and bearing. */
export function terrainDrawingFootprint(center: DrawingPoint, zoom: number, efficient: boolean, detail: boolean): Omit<TerrainDrawingGrid, "heights"> | null {
  const [lng, lat] = center;
  const [west, south, east, north] = TERRAIN_DRAWING_BOUNDS;
  if (![lng, lat, zoom].every(Number.isFinite) || zoom < TERRAIN_DRAWING_MIN_ZOOM || lng < west || lng > east || lat < south || lat > north) return null;
  const size = efficient ? 33 : detail ? 65 : 49;
  // Approx. 450 screen pixels at this latitude, never more than 24 km.
  const width = Math.max(120, Math.min(24_000, 156543.03392 * Math.cos(lat * Math.PI / 180) / 2 ** zoom * 450));
  const halfLat = width / 2 / 111_320;
  const halfLng = halfLat / Math.cos(lat * Math.PI / 180);
  const bounds = [Math.max(west, lng - halfLng), Math.max(south, lat - halfLat), Math.min(east, lng + halfLng), Math.min(north, lat + halfLat)] as const;
  // Clipping at the focus box can make a rectangle; report the larger spacing.
  const spacingMeters = Math.max((bounds[2] - bounds[0]) * 111_320 * Math.cos(lat * Math.PI / 180), (bounds[3] - bounds[1]) * 111_320) / (size - 1);
  return { size, bounds, spacingMeters };
}

export function terrainDrawingCoordinate(grid: Pick<TerrainDrawingGrid, "size" | "bounds">, index: number): DrawingPoint {
  const { size, bounds: [west, south, east, north] } = grid;
  return [west + (index % size) / (size - 1) * (east - west), north - Math.floor(index / size) / (size - 1) * (north - south)];
}

function niceInterval(minimum: number): number {
  const decade = 10 ** Math.floor(Math.log10(minimum));
  return ([1, 2, 5, 10].find(value => value * decade >= minimum) ?? 10) * decade;
}

/** Each segment belongs to one complete cell. Unknown corners create a hole. */
export function contourCell(points: readonly DrawingPoint[], heights: readonly number[], level: number): DrawingPoint[][] {
  if (heights.length !== 4 || points.length !== 4 || !Number.isFinite(level) || !heights.every(Number.isFinite)) return [];
  const edges: (DrawingPoint | null)[] = heights.map((height, index) => {
    const next = (index + 1) % 4;
    // Half-open ownership handles exact-level vertices without division by zero.
    if ((height > level) === (heights[next] > level)) return null;
    const t = (level - height) / (heights[next] - height);
    return [points[index][0] + t * (points[next][0] - points[index][0]), points[index][1] + t * (points[next][1] - points[index][1])];
  });
  const crossed = edges.flatMap((point, index) => point ? [index] : []);
  let pairs: number[][] = crossed.length === 2 ? [crossed] : [];
  if (crossed.length === 4) {
    // Bilinear asymptotic decider; the exactly symmetric saddle has a stable
    // tie rule. Never join through a different cell or a missing sample.
    const q = (heights[0] - level) * (heights[2] - level) - (heights[1] - level) * (heights[3] - level);
    pairs = q > 0 ? [[0, 1], [2, 3]] : [[0, 3], [1, 2]];
  }
  return pairs.flatMap(([a, b]) => {
    const first = edges[a]!, second = edges[b]!;
    return first[0] === second[0] && first[1] === second[1] ? [] : [[first, second]];
  });
}

/** Bounded, resumable geometry work. The runtime yields between four-row batches. */
export function* terrainDrawingGeometryBatches(grid: TerrainDrawingGrid, options: { intervalMeters?: number; maxSegments?: number } = {}): Generator<void, TerrainDrawingGeometry> {
  const empty = (): TerrainDrawingGeometry => ({ data: { type: "FeatureCollection", features: [] }, intervalMeters: null, coverage: 0, sampleCount: 0, segmentCount: 0, clipped: false });
  if (!Number.isInteger(grid.size) || grid.size < 2 || grid.size > 65 || grid.heights.length !== grid.size ** 2 || !grid.bounds.every(Number.isFinite)) return empty();
  const valid = grid.heights.filter((height): height is number => typeof height === "number" && Number.isFinite(height));
  if (!valid.length) return { ...empty(), sampleCount: grid.heights.length };
  const min = Math.min(...valid), max = Math.max(...valid);
  const requestedInterval = Number.isFinite(options.intervalMeters) && options.intervalMeters! > 0 ? options.intervalMeters! : Math.max(5, grid.spacingMeters / 35, (max - min) / 32);
  const interval = niceInterval(Math.max(requestedInterval, (max - min) / (TERRAIN_DRAWING_MAX_LEVELS - 1)));
  const limit = Math.max(0, Math.min(TERRAIN_DRAWING_MAX_SEGMENTS, Number.isFinite(options.maxSegments) ? Math.floor(options.maxSegments!) : TERRAIN_DRAWING_MAX_SEGMENTS));
  const contourLines = new Map<number, DrawingPoint[][]>();
  const contourKeys = new Map<number, Set<string>>();
  const gridLines: DrawingPoint[][] = [];
  const levels: number[] = [];
  if (min !== max) for (let elevation = Math.ceil(min / interval) * interval; elevation <= max && levels.length < TERRAIN_DRAWING_MAX_LEVELS; elevation += interval) levels.push(elevation);
  let segmentCount = 0, clipped = false;
  const add = (lines: DrawingPoint[][], segment: DrawingPoint[]) => {
    if (segmentCount >= limit) { clipped = true; return; }
    lines.push(segment); segmentCount += 1;
  };
  const value = (index: number) => typeof grid.heights[index] === "number" && Number.isFinite(grid.heights[index]) ? grid.heights[index] as number : null;
  // Grid edges are adjacent loaded samples; absent points never get bridged.
  for (let row = 0; row < grid.size; row += 1) {
    for (let col = 0; col < grid.size; col += 1) {
      const index = row * grid.size + col;
      if (value(index) === null) continue;
      const point = terrainDrawingCoordinate(grid, index);
      if (col < grid.size - 1 && value(index + 1) !== null) add(gridLines, [point, terrainDrawingCoordinate(grid, index + 1)]);
      if (row < grid.size - 1 && value(index + grid.size) !== null) add(gridLines, [point, terrainDrawingCoordinate(grid, index + grid.size)]);
    }
    if (row % 4 === 3) yield;
  }
  for (let row = 0; row < grid.size - 1 && segmentCount < limit; row += 1) {
    for (let col = 0; col < grid.size - 1 && segmentCount < limit; col += 1) {
      const nw = row * grid.size + col;
      const indices = [nw, nw + 1, nw + grid.size + 1, nw + grid.size];
      const heights = indices.map(value);
      if (heights.some(height => height === null)) continue;
      const points = indices.map(index => terrainDrawingCoordinate(grid, index));
      const low = Math.min(...heights as number[]), high = Math.max(...heights as number[]);
      for (const level of levels) {
        if (level < low || level > high) continue;
        const lines = contourLines.get(level) ?? [];
        const seen = contourKeys.get(level) ?? new Set<string>();
        for (const segment of contourCell(points, heights as number[], level)) {
          // An exact-level edge can belong to both adjacent cells. Keep one
          // copy, without rounding the geometry itself or joining any gaps.
          const key = segment.map(point => point.map(value => value.toFixed(12)).join(",")).sort().join(";");
          if (!seen.has(key)) { add(lines, segment); seen.add(key); }
        }
        if (lines.length) contourLines.set(level, lines);
        contourKeys.set(level, seen);
      }
    }
    if (row % 4 === 3) yield;
  }
  if (segmentCount >= limit) clipped = true;
  const features: TerrainDrawingData["features"] = [...contourLines].map(([elevation, coordinates]) => ({
    type: "Feature", properties: { role: "contour", elevation, index: Math.round(elevation / interval) % 5 === 0 }, geometry: { type: "MultiLineString", coordinates },
  }));
  if (gridLines.length) features.unshift({ type: "Feature", properties: { role: "grid", index: false }, geometry: { type: "MultiLineString", coordinates: gridLines } });
  return { data: { type: "FeatureCollection", features }, intervalMeters: levels.length ? interval : null, coverage: valid.length / grid.heights.length, sampleCount: grid.heights.length, segmentCount, clipped };
}

export function buildTerrainDrawingGeometry(grid: TerrainDrawingGrid, options: { intervalMeters?: number; maxSegments?: number } = {}): TerrainDrawingGeometry {
  const batches = terrainDrawingGeometryBatches(grid, options);
  let next = batches.next();
  while (!next.done) next = batches.next();
  return next.value;
}
