import type { AreaBounds, Position } from "./subsurface-model";

export type ResourceCell = { id: string; bounds: AreaBounds; coordinates: Position };
export type ResourceGroup = ResourceCell & { count: number; kind: "oilgas" | "minerals" };
export type LaidOutResourceGroup = ResourceGroup & { displayCoordinates: Position };
const KANSAS: AreaBounds = [-102.1, 36.95, -94.55, 40.05];

/** Fixed, nonoverlapping Kansas envelopes keep source count groups stable while panning.
 * A cell at the viewport edge retains its complete regional count. */
export function geologyResourceCells(viewport: AreaBounds): ResourceCell[] {
  const cells: ResourceCell[] = [];
  const broad = viewport[2] - viewport[0] > 3 || viewport[3] - viewport[1] > 1.5;
  const columns = broad ? 3 : 8, rows = broad ? 2 : 4;
  const width = broad ? (KANSAS[2] - KANSAS[0]) / 3 : 1;
  const height = broad ? (KANSAS[3] - KANSAS[1]) / 2 : 1;
  for (let x = 0; x < columns; x++) for (let y = 0; y < rows; y++) {
    const west = KANSAS[0] + x * width, south = KANSAS[1] + y * height;
    const east = Math.min(KANSAS[2], west + width), north = Math.min(KANSAS[3], south + height);
    if (east <= viewport[0] || west >= viewport[2] || north <= viewport[1] || south >= viewport[3]) continue;
    const visibleWest = Math.max(west, viewport[0]), visibleEast = Math.min(east, viewport[2]);
    const visibleSouth = Math.max(south, viewport[1]), visibleNorth = Math.min(north, viewport[3]);
    const bounds = [west, south, east, north].map(value => Number(value.toFixed(6))) as AreaBounds;
    cells.push({ id: `${broad ? "b" : "m"}:${x}:${y}`, bounds,
      coordinates: [(visibleWest + visibleEast) / 2, (visibleSouth + visibleNorth) / 2] });
  }
  return cells;
}

/** Match the map's circle radius interpolation, including the displayed 22px cap. */
export function resourceGroupRadius(count: number): number {
  if (count <= 1) return 10;
  if (count <= 100) return 10 + (count - 1) * 5 / 99;
  return Math.min(22, 15 + (count - 100) * 7 / 9900);
}

/** Place paired source groups using projected pixels, then turn the measured
 * positions back into map coordinates. The pair shifts together at map edges. */
export function layoutResourceGroups(
  groups: ResourceGroup[],
  width: number,
  project: (coordinates: Position) => { x: number; y: number },
  unproject: (point: { x: number; y: number }) => { lng: number; lat: number },
): LaidOutResourceGroup[] {
  const byCell = new Map<string, ResourceGroup[]>();
  for (const group of groups) byCell.set(group.id, [...(byCell.get(group.id) ?? []), group]);
  const placed = new Map<ResourceGroup, Position>();
  for (const pair of byCell.values()) {
    const anchor = project(pair[0].coordinates);
    const oilgas = pair.find(group => group.kind === "oilgas");
    const minerals = pair.find(group => group.kind === "minerals");
    const oilRadius = oilgas ? resourceGroupRadius(oilgas.count) : 0;
    const mineRadius = minerals ? resourceGroupRadius(minerals.count) : 0;
    const halfSpacing = oilgas && minerals ? (oilRadius + mineRadius + 10) / 2 : 0;
    let oilX = anchor.x - halfSpacing, mineX = anchor.x + halfSpacing;
    const left = Math.min(...[oilgas && oilX - oilRadius, minerals && mineX - mineRadius].filter((value): value is number => typeof value === "number"));
    const right = Math.max(...[oilgas && oilX + oilRadius, minerals && mineX + mineRadius].filter((value): value is number => typeof value === "number"));
    const shift = Math.max(0, 8 - left) - Math.max(0, right - (width - 8));
    oilX += shift; mineX += shift;
    for (const group of pair) {
      const sourcePoint = unproject({ x: group.kind === "oilgas" ? oilX : mineX, y: anchor.y });
      placed.set(group, [sourcePoint.lng, sourcePoint.lat]);
    }
  }
  return groups.map(group => ({ ...group, displayCoordinates: placed.get(group) ?? group.coordinates }));
}
