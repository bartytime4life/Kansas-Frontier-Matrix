import type { Map as GLMap } from "maplibre-gl";

export type GlobeViewpoint = "earth" | "continent" | "kansas";
export const GLOBE_VIEWPOINTS = {
  earth: { label: "Whole Earth", center: [-98.38, 25] as [number, number], zoom: 0.6, bearing: 0, pitch: 0 },
  continent: { label: "North America", center: [-100, 40] as [number, number], zoom: 2.2, bearing: 0, pitch: 0 },
  kansas: { label: "Kansas study area", center: [-98.38, 38.48] as [number, number], zoom: 5.45, bearing: 0, pitch: 0 },
} as const;

export const REGIONAL_NAVIGATION_BOUNDS: [[number, number], [number, number]] = [[-104.8, 34.8], [-92, 42.2]];

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
