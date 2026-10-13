import type { Map as GLMap } from "./maplibre-seam";

export type GlobeViewpoint = "earth" | "continent" | "kansas";
export const GLOBE_VIEWPOINTS = {
  earth: { label: "Whole Earth", center: [-98.38, 25] as [number, number], zoom: 0.6, bearing: 0, pitch: 0 },
  continent: { label: "North America", center: [-100, 40] as [number, number], zoom: 2.2, bearing: 0, pitch: 0 },
  kansas: { label: "Kansas study area", center: [-98.38, 38.48] as [number, number], zoom: 5.45, bearing: 0, pitch: 0 },
} as const;

export const REGIONAL_NAVIGATION_BOUNDS: [[number, number], [number, number]] = [[-104.8, 34.8], [-92, 42.2]];

// Screen symbols are display cues, not geographic footprints. At a whole-Earth
// view Kansas spans only a few pixels, so fixed-size glows and borders would
// cover neighboring states. Keep the cues small until the study area grows.
export const GLOBE_OVERVIEW_SIZE_STOPS = [
  [0, 0], [2, 0.08], [4, 0.22], [7, 0.7], [10, 1],
] as const;

export function globeOverviewSizeScale(zoom: number): number {
  if (!Number.isFinite(zoom)) return 0;
  for (let index = 1; index < GLOBE_OVERVIEW_SIZE_STOPS.length; index += 1) {
    const [upperZoom, upperScale] = GLOBE_OVERVIEW_SIZE_STOPS[index];
    const [lowerZoom, lowerScale] = GLOBE_OVERVIEW_SIZE_STOPS[index - 1];
    if (zoom <= upperZoom) return lowerScale + (upperScale - lowerScale) * Math.max(0, (zoom - lowerZoom) / (upperZoom - lowerZoom));
  }
  return 1;
}

/** Canvas overlays do not receive MapLibre's globe horizon clipping. */
export function onVisibleGlobeHemisphere(center: { lng: number; lat: number }, [longitude, latitude]: readonly number[]): boolean {
  if (![center.lng, center.lat, longitude, latitude].every(Number.isFinite)) return false;
  const radians = Math.PI / 180;
  const cosAngle = Math.sin(center.lat * radians) * Math.sin(latitude * radians)
    + Math.cos(center.lat * radians) * Math.cos(latitude * radians) * Math.cos((longitude - center.lng) * radians);
  return cosAngle > 0;
}

/** Keep MapLibre's zoom expression outermost while sizing provider symbols on
 * the globe. Input data expressions remain intact, including magnitude cues. */
export function globeOverviewPaintSize(base: number | unknown[]): number | unknown[] {
  const multiply = (value: unknown, scale: number) => typeof value === "number" ? value * scale : ["*", scale, value];
  if (Array.isArray(base) && base[0] === "interpolate" && Array.isArray(base[2]) && base[2][0] === "zoom" && base[3] === 4) {
    const first = base[4];
    return ["interpolate", ["linear"], ["zoom"], 0, 0, 2, multiply(first, 0.08), 4, multiply(first, 0.22), ...base.slice(5)];
  }
  return ["interpolate", ["linear"], ["zoom"], ...GLOBE_OVERVIEW_SIZE_STOPS.flatMap(([zoom, scale]) => [zoom, multiply(base, scale)])];
}

// Projection is a display choice. This never expands a provider query or recipe AOI.
export function applyProjectionNavigationLimits(map: Pick<GLMap, "getMaxBounds" | "getMinZoom" | "setMaxBounds" | "setMinZoom">, projection: "globe" | "mercator") {
  const bounds = map.getMaxBounds();
  if (projection === "globe") {
    if (bounds) map.setMaxBounds(null);
    if (map.getMinZoom() !== 0) map.setMinZoom(0);
  } else {
    if (map.getMinZoom() !== 4) map.setMinZoom(4);
    if (!bounds || bounds.getWest() !== -104.8 || bounds.getSouth() !== 34.8 || bounds.getEast() !== -92 || bounds.getNorth() !== 42.2) map.setMaxBounds(REGIONAL_NAVIGATION_BOUNDS);
  }
}

export type GlobeCameraReading = {
  longitude: number; latitude: number; zoom: number; bearing: number; pitch: number;
  projection: "globe" | "mercator" | "unknown"; sampledAt: string;
  styleLoaded: boolean; tilesLoaded: boolean;
};

export function readGlobeCamera(map: Pick<GLMap, "getCenter" | "getZoom" | "getBearing" | "getPitch" | "getProjection" | "isStyleLoaded" | "areTilesLoaded">, now = new Date()): GlobeCameraReading | null {
  try {
    const center = map.getCenter();
    const zoom = map.getZoom(), bearing = map.getBearing(), pitch = map.getPitch();
    if (![center.lng, center.lat, zoom, bearing, pitch].every(Number.isFinite) || Math.abs(center.lat) > 90) return null;
    const projection = map.getProjection()?.type;
    return {
      longitude: ((center.lng + 180) % 360 + 360) % 360 - 180, latitude: center.lat,
      zoom, bearing, pitch, sampledAt: now.toISOString(),
      projection: projection === "globe" ? "globe" : projection === undefined || projection === "mercator" ? "mercator" : "unknown",
      styleLoaded: map.isStyleLoaded() === true, tilesLoaded: map.areTilesLoaded() === true,
    };
  } catch { return null; }
}
