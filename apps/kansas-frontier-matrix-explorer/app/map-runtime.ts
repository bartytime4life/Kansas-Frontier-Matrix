export type BasemapKey = "midnight" | "prairie";
export type AtmospherePreset = "night" | "dusk" | "clear";

export type BasemapDescriptor = Readonly<{
  title: string;
  note: string;
}>;

export const BASEMAPS: Readonly<Record<BasemapKey, BasemapDescriptor>> = Object.freeze({
  midnight: Object.freeze({
    title: "Midnight navy",
    note: "Renderer-neutral high-contrast preference descriptor",
  }),
  prairie: Object.freeze({
    title: "Prairie dusk",
    note: "Renderer-neutral low-glare preference descriptor",
  }),
});

export const SCENE_ENVIRONMENTS = Object.freeze({
  night: Object.freeze({
    "sky-color": "#07171a",
    "horizon-color": "#173438",
    "fog-color": "#0d2427",
    "fog-ground-blend": 0.35,
    "horizon-fog-blend": 0.7,
    "sky-horizon-blend": 0.82,
    "atmosphere-blend": 0.68,
  }),
  dusk: Object.freeze({
    "sky-color": "#263744",
    "horizon-color": "#d49c78",
    "fog-color": "#5f6867",
    "fog-ground-blend": 0.28,
    "horizon-fog-blend": 0.62,
    "sky-horizon-blend": 0.9,
    "atmosphere-blend": 0.82,
  }),
  clear: Object.freeze({
    "sky-color": "#6d9dac",
    "horizon-color": "#d4e5df",
    "fog-color": "#afc9c3",
    "fog-ground-blend": 0.22,
    "horizon-fog-blend": 0.48,
    "sky-horizon-blend": 0.78,
    "atmosphere-blend": 0.88,
  }),
}) satisfies Readonly<Record<AtmospherePreset, Readonly<Record<string, string | number>>>>;

export type TileCoordinate = Readonly<{ z: number; x: number; y: number; label: string }>;
export type GeographicBounds = Readonly<{ west: number; south: number; east: number; north: number }>;
export type ScreenRect = Readonly<{ startX: number; startY: number; endX: number; endY: number }>;
export type ScreenViewport = Readonly<{ width: number; height: number }>;

const radians = (degrees: number) => degrees * (Math.PI / 180);

export const lngLatToTile = (longitude: number, latitude: number, zoom: number): TileCoordinate => {
  const z = Math.max(0, Math.min(22, Math.floor(Number.isFinite(zoom) ? zoom : 0)));
  const lng = Math.max(-180, Math.min(180, Number.isFinite(longitude) ? longitude : 0));
  const lat = Math.max(-85.051129, Math.min(85.051129, Number.isFinite(latitude) ? latitude : 0));
  const tileCount = 2 ** z;
  const x = Math.max(0, Math.min(tileCount - 1, Math.floor(((lng + 180) / 360) * tileCount)));
  const latitudeRadians = radians(lat);
  const y = Math.max(0, Math.min(tileCount - 1, Math.floor(
    ((1 - Math.log(Math.tan(latitudeRadians) + (1 / Math.cos(latitudeRadians))) / Math.PI) / 2) * tileCount,
  )));
  return Object.freeze({ z, x, y, label: `${z}/${x}/${y}` });
};

/**
 * Convert a north-up, unpitched screen rectangle into a renderer-neutral
 * geographic query envelope. The result is context for a governed catalog
 * query; it is not geometry evidence and does not expose a MapLibre object.
 */
export const screenRectToBounds = (
  rect: ScreenRect,
  viewport: ScreenViewport,
  visibleBounds: GeographicBounds,
  minimumPixels = 12,
): GeographicBounds | null => {
  if (![rect.startX, rect.startY, rect.endX, rect.endY, viewport.width, viewport.height, visibleBounds.west, visibleBounds.south, visibleBounds.east, visibleBounds.north, minimumPixels].every(Number.isFinite)) return null;
  if (viewport.width <= 0 || viewport.height <= 0 || visibleBounds.west >= visibleBounds.east || visibleBounds.south >= visibleBounds.north || minimumPixels < 0) return null;

  const clampPixel = (value: number, maximum: number) => Math.max(0, Math.min(maximum, value));
  const startX = clampPixel(rect.startX, viewport.width);
  const endX = clampPixel(rect.endX, viewport.width);
  const startY = clampPixel(rect.startY, viewport.height);
  const endY = clampPixel(rect.endY, viewport.height);
  const left = Math.min(startX, endX);
  const right = Math.max(startX, endX);
  const top = Math.min(startY, endY);
  const bottom = Math.max(startY, endY);
  if (right - left < minimumPixels || bottom - top < minimumPixels) return null;

  const longitudeSpan = visibleBounds.east - visibleBounds.west;
  const latitudeSpan = visibleBounds.north - visibleBounds.south;
  return Object.freeze({
    west: visibleBounds.west + (left / viewport.width) * longitudeSpan,
    south: visibleBounds.north - (bottom / viewport.height) * latitudeSpan,
    east: visibleBounds.west + (right / viewport.width) * longitudeSpan,
    north: visibleBounds.north - (top / viewport.height) * latitudeSpan,
  });
};
