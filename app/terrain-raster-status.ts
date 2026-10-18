/** The optional 3DEP imagery is tile context, separate from the geometry DEM.
 * A success in a former map view cannot establish coverage in the new view. */
export type TerrainRasterId = "usgs-3dep-hillshade" | "usgs-3dep-slope";
export type TerrainRasterBounds = { west: number; east: number; south: number; north: number };
export type TerrainRasterTile = { z: number; x: number; y: number };

export const terrainRasterErrorTile = (event: { tile?: { tileID?: { canonical?: TerrainRasterTile } }; coord?: { canonical?: TerrainRasterTile } }): TerrainRasterTile | undefined =>
  event.tile?.tileID?.canonical ?? event.coord?.canonical;

export const terrainRasterTileInView = (tile: TerrainRasterTile | undefined, bounds: TerrainRasterBounds, zoom: number): boolean => {
  // MapLibre's 256 px raster normally requests one zoom above the map zoom;
  // a pitched view can request another level. Bound both sides so old coarse
  // parents and distant fine children cannot attest the current view.
  const minTileZoom = Math.min(Math.floor(zoom), 14);
  const maxTileZoom = Math.min(Math.floor(zoom) + 2, 14);
  if (!tile || zoom < 7 || tile.z < minTileZoom || tile.z > maxTileZoom) return false;
  const n = 2 ** tile.z;
  if (tile.x < 0 || tile.x >= n || tile.y < 0 || tile.y >= n) return false;
  const latitude = (row: number) => Math.atan(Math.sinh(Math.PI * (1 - 2 * row / n))) * 180 / Math.PI;
  return (tile.x + 1) / n * 360 - 180 > bounds.west
    && tile.x / n * 360 - 180 < bounds.east
    && latitude(tile.y) > bounds.south
    && latitude(tile.y + 1) < bounds.north;
};

export const terrainRasterStatus = (loadedTile: boolean, failedTile: boolean, settled: boolean): "loading" | "ready" | "partial" | "error" =>
  failedTile ? loadedTile ? "partial" : "error" : loadedTile && settled ? "ready" : "loading";

export const terrainRasterNeedsCloserView = (selected: boolean, held: boolean, state: string, zoom: number): boolean =>
  selected && !held && state !== "error" && zoom < 7;

export class TerrainRasterViewTracker {
  private loaded = new Map<TerrainRasterId, Map<string, TerrainRasterTile>>();
  private failed = new Map<TerrainRasterId, Map<string, TerrainRasterTile>>();
  private sourceFailures = new Set<TerrainRasterId>();

  reset(id: TerrainRasterId): void { this.loaded.delete(id); this.failed.delete(id); this.sourceFailures.delete(id); }
  resetAll(): void { this.loaded.clear(); this.failed.clear(); this.sourceFailures.clear(); }
  markFailed(id: TerrainRasterId, tile?: TerrainRasterTile): void {
    if (!tile) { this.sourceFailures.add(id); return; }
    this.loaded.get(id)?.delete(`${tile.z}/${tile.x}/${tile.y}`);
    this.remember(this.failed, id, tile);
  }
  markLoaded(id: TerrainRasterId, tile: TerrainRasterTile | undefined): void {
    if (tile) {
      this.failed.get(id)?.delete(`${tile.z}/${tile.x}/${tile.y}`);
      this.remember(this.loaded, id, tile);
    }
  }
  hasLoaded(id: TerrainRasterId, bounds: TerrainRasterBounds, zoom: number): boolean {
    return Array.from(this.loaded.get(id)?.values() ?? []).some(tile => terrainRasterTileInView(tile, bounds, zoom));
  }
  hasFailed(id: TerrainRasterId, bounds: TerrainRasterBounds, zoom: number): boolean {
    return this.sourceFailures.has(id) || Array.from(this.failed.get(id)?.values() ?? []).some(tile => terrainRasterTileInView(tile, bounds, zoom));
  }
  status(id: TerrainRasterId, bounds: TerrainRasterBounds, zoom: number, settled: boolean): ReturnType<typeof terrainRasterStatus> {
    return terrainRasterStatus(this.hasLoaded(id, bounds, zoom), this.hasFailed(id, bounds, zoom), settled);
  }
  private remember(target: Map<TerrainRasterId, Map<string, TerrainRasterTile>>, id: TerrainRasterId, tile: TerrainRasterTile): void {
    const tiles = target.get(id) ?? new Map<string, TerrainRasterTile>();
    const key = `${tile.z}/${tile.x}/${tile.y}`;
    tiles.delete(key);
    tiles.set(key, tile);
    while (tiles.size > 128) tiles.delete(tiles.keys().next().value!);
    target.set(id, tiles);
  }
}
