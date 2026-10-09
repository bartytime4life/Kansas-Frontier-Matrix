import type { Map as MapLibreMap } from "./maplibre-seam";

const TOPO_RASTER_LAYER_ID = "usgs-topo-context-raster";
const TOPO_RASTER_DEPTH_PAINT = {
  "raster-brightness-max": 0.83,
  "raster-contrast": 0.18,
  "raster-saturation": -0.04,
} as const;

export type TerrainReliefLook = "general" | "topographic";
export type TerrainReliefLight = "night" | "dusk" | "clear";

/** Lighting is a display treatment of the active raster DEM, not a new
 * elevation surface or an inferred contour product. The stronger topo look
 * applies only while the topographic basemap is shown in Terrain 3D. */
export const terrainHillshadePaint = (look: TerrainReliefLook, light: TerrainReliefLight, azimuth: number) => ({
  "hillshade-shadow-color": look === "topographic" ? "#16343c" : "#102c3d",
  "hillshade-highlight-color": look === "topographic"
    ? light === "dusk" ? "#f0d5a9" : light === "night" ? "#c6d8d5" : "#f8ebcc"
    : light === "dusk" ? "#ecd6b5" : "#edf1df",
  "hillshade-accent-color": look === "topographic" ? "#9a8067" : "#729aa0",
  "hillshade-exaggeration": look === "topographic" ? 1 : 0.66,
  "hillshade-illumination-direction": ((Number.isFinite(azimuth) ? azimuth : 235) % 360 + 360) % 360,
});

// applyTerrainReliefStyle lives in scene-effects.ts so cinematic relief and
// sun-following light share one code path.

/** The USGS topo tile remains unchanged. Removing these three paint overrides
 * returns the 2D raster layer to the original style's exact defaults. */
export const applyTopographicRasterDepth = (map: MapLibreMap, active: boolean): void => {
  if (!map.getLayer(TOPO_RASTER_LAYER_ID)) return;
  for (const property of Object.keys(TOPO_RASTER_DEPTH_PAINT) as Array<keyof typeof TOPO_RASTER_DEPTH_PAINT>) {
    const current = map.getPaintProperty(TOPO_RASTER_LAYER_ID, property);
    if (active) {
      const value = TOPO_RASTER_DEPTH_PAINT[property];
      if (current !== value) map.setPaintProperty(TOPO_RASTER_LAYER_ID, property, value);
    } else if (current !== undefined) {
      map.setPaintProperty(TOPO_RASTER_LAYER_ID, property, undefined);
    }
  }
};
