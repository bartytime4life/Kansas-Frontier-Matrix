import type { Map as MapLibreMap } from "./maplibre-seam";
import type { SceneEffectSettings, SceneLightPreset, SceneView } from "./scene-effects";

/** Presentation recipes use the existing light and effect state. No saved theme,
 * camera, basemap, source, time, or terrain-provider state is introduced. */
export const SCENE_RECIPES = {
  daylight: { label: "Daylight", detail: "Crisp light · open skies", atmosphere: "clear", azimuth: 210, cinematic: true },
  golden: { label: "Golden hour", detail: "Copper light · warm horizon", atmosphere: "dusk", azimuth: 265, cinematic: true },
  blue: { label: "Blue hour", detail: "Ice blue · deep horizons", atmosphere: "night", azimuth: 225, cinematic: true },
  survey: { label: "Survey", detail: "Quiet light · readable relief", atmosphere: "clear", azimuth: 315, cinematic: false },
} as const;
export type SceneRecipe = keyof typeof SCENE_RECIPES;
export type ScenePresentation = Readonly<{ atmosphere: SceneLightPreset; azimuth: number; settings: SceneEffectSettings }>;

export function sceneRecipePresentation(id: SceneRecipe, settings: SceneEffectSettings): ScenePresentation {
  const recipe = SCENE_RECIPES[id];
  return {
    atmosphere: recipe.atmosphere,
    azimuth: recipe.azimuth,
    // Preserve opted-out effects and, critically, the current 2D DEM choice.
    settings: { ...settings, cinematic: recipe.cinematic, sunSync: false,
      ...(id === "survey" ? { curtain: false, kansasGlow: false } : {}) },
  };
}

export function matchingSceneRecipe({ atmosphere, azimuth, settings }: ScenePresentation): SceneRecipe | null {
  if (settings.sunSync || !Number.isFinite(azimuth)) return null;
  return (Object.keys(SCENE_RECIPES) as SceneRecipe[]).find((id) => {
    const recipe = SCENE_RECIPES[id];
    return atmosphere === recipe.atmosphere && ((azimuth % 360) + 360) % 360 === recipe.azimuth
      && settings.cinematic === recipe.cinematic
      && (id !== "survey" || (!settings.curtain && !settings.kansasGlow));
  }) ?? null;
}

export type SceneComposition = Readonly<{ pitch: number; bearing: number; fieldOfView: number }>;
const bounded = (value: number, low: number, high: number, fallback: number) => Number.isFinite(value) ? Math.max(low, Math.min(high, value)) : fallback;
export const normalizedBearing = (value: number): number => Number.isFinite(value) ? ((value + 180) % 360 + 360) % 360 - 180 : 0;
export const compositionDefaults = (view: SceneView): SceneComposition => ({
  pitch: view === "terrain" ? 62 : view === "tilted" ? 56 : 0,
  bearing: 0,
  fieldOfView: view === "terrain" ? 50 : view === "globe" ? 42 : 36,
});

type CameraMap = Pick<MapLibreMap, "getPitch" | "getBearing" | "getVerticalFieldOfView" | "getMaxPitch" | "setVerticalFieldOfView" | "stop" | "easeTo">;
export const readSceneComposition = (map: Pick<CameraMap, "getPitch" | "getBearing" | "getVerticalFieldOfView">): SceneComposition => ({
  pitch: map.getPitch(), bearing: normalizedBearing(map.getBearing()), fieldOfView: map.getVerticalFieldOfView(),
});

/** Direct controls own the camera immediately. No center/zoom/data mutation.
 * Only reset animates; direct slider movement is immediate under every motion setting. */
export function applySceneComposition(map: CameraMap, patch: Partial<SceneComposition>, options: {
  view: SceneView; reducedMotion: boolean; reset?: boolean; interrupt: () => void;
}): SceneComposition {
  options.interrupt();
  map.stop();
  const current = readSceneComposition(map);
  const next = {
    pitch: options.view === "globe" ? 0 : bounded(patch.pitch ?? current.pitch, 0, Math.min(72, map.getMaxPitch()), current.pitch),
    bearing: normalizedBearing(patch.bearing ?? current.bearing),
    fieldOfView: bounded(patch.fieldOfView ?? current.fieldOfView, 20, 60, current.fieldOfView),
  };
  if (patch.fieldOfView !== undefined) map.setVerticalFieldOfView(next.fieldOfView);
  if (patch.pitch !== undefined || patch.bearing !== undefined) {
    map.easeTo({ pitch: next.pitch, bearing: next.bearing, duration: options.reset && !options.reducedMotion ? 300 : 0, essential: false });
  }
  return readSceneComposition(map);
}

/** Emphasize Kansas relief without altering the source elevation readouts. */
export const DEFAULT_TERRAIN_DEPTH = 2.5;
export const terrainDepth = (value: number, fallback = DEFAULT_TERRAIN_DEPTH): number =>
  Number.isFinite(value) ? Math.max(0.1, Math.min(3, value)) : fallback;

/** An explicit closer view of the current ground; never moves its center,
 * bearing, source, selection or date, and never zooms a closer view back out. */
export function applyGroundView(map: CameraMap & Pick<MapLibreMap, "getZoom">, options: {
  reducedMotion: boolean; interrupt: () => void;
}): void {
  options.interrupt();
  map.stop();
  map.setVerticalFieldOfView(50);
  map.easeTo({ zoom: Math.max(10.5, map.getZoom()), pitch: Math.min(66, map.getMaxPitch()), duration: options.reducedMotion ? 0 : 650, essential: false });
}
