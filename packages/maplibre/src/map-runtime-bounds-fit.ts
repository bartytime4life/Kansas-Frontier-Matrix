import {
  MapRuntimePortError,
  freezeMapRuntimeCamera,
  type MapRuntimeCamera,
} from "./map-runtime-port";

export const MAP_RUNTIME_BOUNDS_FIT_PROFILE =
  "kfm.map-runtime-bounds-fit.v1" as const;

export type MapRuntimeBounds = Readonly<{
  west: number;
  south: number;
  east: number;
  north: number;
}>;

export type MapRuntimeViewport = Readonly<{
  widthPx: number;
  heightPx: number;
  paddingPx?: number;
}>;

export type MapRuntimeBoundsFitOptions = Readonly<{
  minZoom?: number;
  maxZoom?: number;
}>;

const MAX_MERCATOR_LATITUDE = 85.051129;
const MIN_ZOOM = 0;
const MAX_ZOOM = 24;
const TILE_SIZE_PX = 512;
const MAX_VIEWPORT_PX = 32_768;
const MAX_PADDING_PX = 16_384;

function failInvalidState(message: string): never {
  throw new MapRuntimePortError("MAP_RUNTIME_STATE_INVALID", message);
}

function finite(value: unknown): value is number {
  return typeof value === "number" && Number.isFinite(value);
}

function validateBounds(bounds: MapRuntimeBounds): void {
  if (
    typeof bounds !== "object" ||
    bounds === null ||
    !finite(bounds.west) ||
    !finite(bounds.south) ||
    !finite(bounds.east) ||
    !finite(bounds.north) ||
    bounds.west < -180 ||
    bounds.west > 180 ||
    bounds.east < -180 ||
    bounds.east > 180 ||
    bounds.south < -MAX_MERCATOR_LATITUDE ||
    bounds.south > MAX_MERCATOR_LATITUDE ||
    bounds.north < -MAX_MERCATOR_LATITUDE ||
    bounds.north > MAX_MERCATOR_LATITUDE ||
    bounds.south > bounds.north
  ) {
    failInvalidState("Map runtime bounds are invalid.");
  }
}

function validateViewport(viewport: MapRuntimeViewport): number {
  if (
    typeof viewport !== "object" ||
    viewport === null ||
    !Number.isSafeInteger(viewport.widthPx) ||
    !Number.isSafeInteger(viewport.heightPx) ||
    viewport.widthPx < 1 ||
    viewport.heightPx < 1 ||
    viewport.widthPx > MAX_VIEWPORT_PX ||
    viewport.heightPx > MAX_VIEWPORT_PX
  ) {
    failInvalidState("Map runtime viewport is invalid.");
  }

  const paddingPx = viewport.paddingPx ?? 0;
  if (
    !Number.isSafeInteger(paddingPx) ||
    paddingPx < 0 ||
    paddingPx > MAX_PADDING_PX ||
    viewport.widthPx - 2 * paddingPx < 1 ||
    viewport.heightPx - 2 * paddingPx < 1
  ) {
    failInvalidState("Map runtime viewport padding is invalid.");
  }
  return paddingPx;
}

function validateZoomRange(options: MapRuntimeBoundsFitOptions): {
  minZoom: number;
  maxZoom: number;
} {
  const minZoom = options.minZoom ?? MIN_ZOOM;
  const maxZoom = options.maxZoom ?? MAX_ZOOM;
  if (
    !finite(minZoom) ||
    !finite(maxZoom) ||
    minZoom < MIN_ZOOM ||
    maxZoom > MAX_ZOOM ||
    minZoom > maxZoom
  ) {
    failInvalidState("Map runtime bounds-fit zoom range is invalid.");
  }
  return { minZoom, maxZoom };
}

function longitudeSpanDegrees(bounds: MapRuntimeBounds): number {
  return bounds.east >= bounds.west
    ? bounds.east - bounds.west
    : bounds.east + 360 - bounds.west;
}

function centerLongitude(bounds: MapRuntimeBounds, spanDegrees: number): number {
  let longitude = bounds.west + spanDegrees / 2;
  if (longitude > 180) longitude -= 360;
  return Object.is(longitude, -0) ? 0 : longitude;
}

function mercatorY(latitude: number): number {
  const radians = (latitude * Math.PI) / 180;
  return (
    0.5 -
    Math.log(Math.tan(Math.PI / 4 + radians / 2)) / (2 * Math.PI)
  );
}

function latitudeFromMercatorY(y: number): number {
  return (
    (Math.atan(Math.sinh(Math.PI * (1 - 2 * y))) * 180) / Math.PI
  );
}

function fitZoom(availablePx: number, worldSpan: number, maxZoom: number): number {
  if (worldSpan === 0) return maxZoom;
  return Math.log2(availablePx / (TILE_SIZE_PX * worldSpan));
}

/**
 * Derives a deterministic zero-bearing/zero-pitch camera that contains a
 * caller-supplied geographic bounds inside a finite viewport.
 *
 * The helper owns only renderer-neutral navigation math. It does not inspect
 * features, admit sources/layers, decide evidence or sensitivity, fetch data,
 * or authorize publication. Bounds that cross the antimeridian are supported.
 */
export function fitMapRuntimeCameraToBounds(
  bounds: MapRuntimeBounds,
  viewport: MapRuntimeViewport,
  options: MapRuntimeBoundsFitOptions = {},
): MapRuntimeCamera {
  validateBounds(bounds);
  const paddingPx = validateViewport(viewport);
  const { minZoom, maxZoom } = validateZoomRange(options);

  const availableWidth = viewport.widthPx - 2 * paddingPx;
  const availableHeight = viewport.heightPx - 2 * paddingPx;
  const longitudeSpan = longitudeSpanDegrees(bounds);
  const xSpan = longitudeSpan / 360;
  const northY = mercatorY(bounds.north);
  const southY = mercatorY(bounds.south);
  const ySpan = Math.abs(southY - northY);

  const horizontalZoom = fitZoom(availableWidth, xSpan, maxZoom);
  const verticalZoom = fitZoom(availableHeight, ySpan, maxZoom);
  const zoom = Math.min(
    maxZoom,
    Math.max(minZoom, Math.min(horizontalZoom, verticalZoom)),
  );

  const centerY = (northY + southY) / 2;
  return freezeMapRuntimeCamera({
    longitude: centerLongitude(bounds, longitudeSpan),
    latitude: latitudeFromMercatorY(centerY),
    zoom,
    bearing: 0,
    pitch: 0,
  });
}
