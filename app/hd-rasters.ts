import type { SourceSpecification, StyleSpecification } from "./maplibre-seam";

/**
 * High-definition raster requests. Vector layers redraw at the screen's own
 * density, but a raster tile is a fixed grid of pixels: on a 2× screen a
 * 256-pixel tile is stretched and soft. From 1.5× up, the Site asks providers
 * for the pixels the screen will show.
 */
export const HIDPI_MIN_RATIO = 1.5;

/** Tiled imagery and topo with finer zoom levels than a 1× screen uses; OpenStreetMap's tile policy keeps it at 1×. */
const DENSER_TILES = new Set(["esri-imagery", "kansas-ng911-2024", "usgs-topo-context"]);

/**
 * A basemap style whose imagery tiles are declared at half their pixel size,
 * so MapLibre draws the next zoom level's tiles: two image pixels per CSS
 * pixel, the same ground at twice the detail.
 */
export function hiDpiBasemapStyle<T extends StyleSpecification | string>(style: T, pixelRatio: number): T {
  // A style URL (the standard vector base) is vector throughout.
  if (typeof style === "string" || !(pixelRatio >= HIDPI_MIN_RATIO)) return style;
  let changed = false;
  const sources = Object.fromEntries(Object.entries(style.sources).map(([id, source]): [string, SourceSpecification] => {
    if (!DENSER_TILES.has(id) || source.type !== "raster") return [id, source];
    changed = true;
    return [id, { ...source, tileSize: (source.tileSize ?? 512) / 2 }];
  }));
  return changed ? { ...(style as StyleSpecification), sources } as T : style;
}

/**
 * An ArcGIS MapServer export at twice the size and twice the dpi: symbols keep
 * their on-screen size (ArcGIS scales point sizes with dpi) and draw with twice
 * the pixels. Other requests are returned unchanged.
 */
export function hiDpiExportUrl(url: string, pixelRatio: number): string {
  if (!(pixelRatio >= HIDPI_MIN_RATIO) || !/\/MapServer\/export\?/.test(url) || !url.includes("size=256%2C256") || /[?&]dpi=/.test(url)) return url;
  return `${url.replace("size=256%2C256", "size=512%2C512")}&dpi=192`;
}
