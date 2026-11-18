/** Raster basemap tile failures are evidence about one tile, not the whole map.
 * A tile that failed during camera movement is never re-requested once the
 * camera settles elsewhere, so a failure only matters while its tile could
 * still be part of the settled view. Failures without a tile identity are
 * source-level and stay until the basemap changes. */
export type RasterTile = { z: number; x: number; y: number };
export type RasterViewBounds = { west: number; east: number; south: number; north: number };

export const BASEMAP_TILE_GAP_MESSAGE =
  "Some basemap tiles are unavailable. Gaps are unknown; choose another basemap or retry. Map controls and records remain available.";

const MAX_TRACKED_TILES = 256;
const finite = (...values: number[]) => values.every(Number.isFinite);
const key = (sourceId: string, tile: RasterTile) => `${sourceId}/${tile.z}/${tile.x}/${tile.y}`;

/** True when `tile` could be drawn in the settled view. MapLibre draws a
 * 512 px raster at about the map zoom, a 256 px raster one level above it, and
 * coarser tiles toward a pitched horizon; past the source maxzoom it overzooms
 * the maxzoom tile. The window is deliberately wide, and any malformed input
 * counts as in view, so a real gap is never hidden. */
export const rasterTileInView = (tile: RasterTile, bounds: RasterViewBounds, zoom: number, maxzoom = 22): boolean => {
  if (!finite(tile.z, tile.x, tile.y, zoom, maxzoom, bounds.west, bounds.east, bounds.south, bounds.north)) return true;
  const drawn = Math.min(Math.floor(zoom), Math.floor(maxzoom));
  if (tile.z < Math.max(0, drawn - 3) || tile.z > Math.min(Math.floor(zoom) + 2, Math.floor(maxzoom))) return false;
  const n = 2 ** tile.z;
  if (tile.x < 0 || tile.x >= n || tile.y < 0 || tile.y >= n) return true;
  const latitude = (row: number) => Math.atan(Math.sinh(Math.PI * (1 - 2 * row / n))) * 180 / Math.PI;
  if (!(latitude(tile.y) > bounds.south && latitude(tile.y + 1) < bounds.north)) return false;
  const west = tile.x / n * 360 - 180;
  const east = (tile.x + 1) / n * 360 - 180;
  // Bounds can extend past ±180° when world copies are visible.
  for (const shift of [-360, 0, 360]) {
    if (west + shift < bounds.east && east + shift > bounds.west) return true;
  }
  return false;
};

/** Raster sources in a basemap style, mapped to their maxzoom (MapLibre's
 * default is 22). A style URL has no inline sources, so it has none here. */
export const rasterSourceMaxzooms = (style: string | { sources: Record<string, { type: string; maxzoom?: number }> }): Map<string, number> => {
  const sources = new Map<string, number>();
  if (typeof style === "string") return sources;
  for (const [id, source] of Object.entries(style.sources)) {
    if (source.type === "raster") sources.set(id, typeof source.maxzoom === "number" ? source.maxzoom : 22);
  }
  return sources;
};

export class BasemapRasterHealth {
  private failedTiles = new Map<string, { sourceId: string; tile: RasterTile }>();
  private failedSources = new Set<string>();

  reset(): void { this.failedTiles.clear(); this.failedSources.clear(); }

  markFailed(sourceId: string, tile?: RasterTile): void {
    if (!tile) { this.failedSources.add(sourceId); return; }
    const id = key(sourceId, tile);
    this.failedTiles.delete(id);
    this.failedTiles.set(id, { sourceId, tile });
    // Keep the newest failures; a dropped old entry was not drawn recently.
    while (this.failedTiles.size > MAX_TRACKED_TILES) this.failedTiles.delete(this.failedTiles.keys().next().value!);
  }

  markLoaded(sourceId: string, tile?: RasterTile): void {
    if (tile) this.failedTiles.delete(key(sourceId, tile));
  }

  /** `sources` maps each raster source in the current basemap to its maxzoom;
   * failures for sources no longer in the style never count. */
  hasFailureInView(sources: ReadonlyMap<string, number>, bounds: RasterViewBounds, zoom: number): boolean {
    for (const sourceId of this.failedSources) if (sources.has(sourceId)) return true;
    for (const { sourceId, tile } of this.failedTiles.values()) {
      const maxzoom = sources.get(sourceId);
      if (maxzoom !== undefined && rasterTileInView(tile, bounds, zoom, maxzoom)) return true;
    }
    return false;
  }
}
