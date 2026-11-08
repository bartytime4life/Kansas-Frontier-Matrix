import { inKansas, validPosition, type AreaBounds, type Position } from "./subsurface-model";

export type LocatorEntry = [string, string, Position, string];
export type LocatorPoint = { id: string; county: string; coordinates: Position; tileId: string; kind: "well" | "core" };
export type LocatorCluster = { coordinates: Position; bounds: AreaBounds; count: number; wells: number; cores: number };

/** A full Kansas viewport is valid here; Underground's one-degree frame remains separate. */
export function validGeologyBounds(value: unknown): value is AreaBounds {
  return Array.isArray(value) && value.length === 4 && value.every(Number.isFinite)
    && value[0] >= -102.2 && value[2] <= -94.4 && value[1] >= 36.8 && value[3] <= 40.2
    && value[2] > value[0] && value[3] > value[1];
}

/** Every matching locator is counted in a fixed geographic grid at each scale.
 * The grid origin never follows the viewport, so modest pans do not reshuffle marks. */
export function mapLocator(entries: unknown, bounds: AreaBounds, maxPoints = 2500, columns = 32, rows = 20) {
  if (!validGeologyBounds(bounds) || !Array.isArray(entries) || !Number.isSafeInteger(maxPoints) || maxPoints < 1 || maxPoints > 5000)
    throw new Error("Invalid geology point request");
  const cols = Math.max(1, Math.min(64, Math.floor(columns)));
  const lines = Math.max(1, Math.min(48, Math.floor(rows)));
  const step = (span: number, divisions: number) => 2 ** Math.ceil(Math.log2(span / divisions));
  const width = step(bounds[2] - bounds[0], cols), height = step(bounds[3] - bounds[1], lines);
  const points: LocatorPoint[] = [];
  const cells = new Map<string, { count: number; wells: number; cores: number; lon: number; lat: number; bounds: AreaBounds; points: LocatorPoint[] }>();
  let total = 0, wells = 0, cores = 0;
  for (const entry of entries) {
    if (!Array.isArray(entry) || entry.length !== 4 || typeof entry[0] !== "string" || typeof entry[1] !== "string"
      || !validPosition(entry[2]) || !inKansas(entry[2]) || typeof entry[3] !== "string") continue;
    const kind = entry[0].startsWith("wwc5-") ? "well" : entry[0].startsWith("core-") ? "core" : null;
    if (!kind) continue;
    const [lon, lat] = entry[2];
    if (lon < bounds[0] || lon > bounds[2] || lat < bounds[1] || lat > bounds[3]) continue;
    total++; if (kind === "well") wells++; else cores++;
    const x = Math.floor((lon + 180) / width);
    const y = Math.floor((lat + 90) / height);
    const index = `${x}:${y}`;
    let cell = cells.get(index);
    if (!cell) {
      const west = x * width - 180, south = y * height - 90;
      cell = { count: 0, wells: 0, cores: 0, lon: 0, lat: 0, bounds: [west, south, west + width, south + height], points: [] };
      cells.set(index, cell);
    }
    cell.count++; cell.lon += lon; cell.lat += lat;
    if (points.length < maxPoints || cell.points.length < 9) {
      const point: LocatorPoint = { id: entry[0], county: entry[1].slice(0, 100), coordinates: [lon, lat], tileId: entry[3], kind };
      if (points.length < maxPoints) points.push(point);
      if (cell.points.length < 9) cell.points.push(point);
    }
    if (kind === "well") cell.wells++; else cell.cores++;
  }
  const sparse = [...cells.values()].filter(cell => cell.count <= 8);
  const showSparse = sparse.reduce((sum, cell) => sum + cell.count, 0) <= maxPoints;
  return { total, wells, cores, points: total <= maxPoints ? points : showSparse ? sparse.flatMap(cell => cell.points) : [],
    clusters: total > maxPoints ? [...cells.values()].filter(cell => !showSparse || cell.count > 8).map((cell): LocatorCluster => ({
      coordinates: [cell.lon / cell.count, cell.lat / cell.count], bounds: cell.bounds,
      count: cell.count, wells: cell.wells, cores: cell.cores,
    })) : [] };
}
