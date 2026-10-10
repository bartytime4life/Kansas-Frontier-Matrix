import type { Map as MapLibreMap } from "./maplibre-seam";
import { createAuroraCurtainLayer, CURTAIN_PALETTES } from "./aurora-curtain-layer";
import { solarPositionAt } from "./daylight-layer";
import { KANSAS_OUTLINE } from "./kansas-orientation";
import { terrainHillshadePaint } from "./terrain-relief-style";

/**
 * Cinematic MapLibre presentation across 2D, tilted, Terrain 3D and globe
 * views: relief lighting, sky, a Kansas border curtain and glow, 2D shaded
 * relief, 3D value columns, lit buildings, sun-following light, selection
 * glow and a camera flyover.
 *
 * Everything here is display treatment. No effect changes feature geometry,
 * evidence state, source values, reported elevations, time, or report
 * semantics, and every effect can be switched off to restore the plain map.
 */

export type SceneLightPreset = "night" | "dusk" | "clear";

export type SceneEffectSettings = Readonly<{
  /** Deeper relief shading, richer sky and fog. Off restores the legacy look. */
  cinematic: boolean;
  /** Glowing border walls around Kansas in tilted and globe views. */
  curtain: boolean;
  /** Light and sky follow the computed sun position over the map center. */
  sunSync: boolean;
  /** Soft Kansas outline glow over every basemap, and a beacon from orbit. */
  kansasGlow: boolean;
  /** DEM shaded relief under 2D maps. Requests display-DEM tiles. */
  relief2d: boolean;
  /** 3D columns for provider point values (earthquake magnitude, streamflow) when tilted. */
  columns: boolean;
  /** Height-shaded, light-matched styling for provider 3D buildings. */
  buildings: boolean;
  /** Real stars, the Milky Way and (from orbit) the Sun behind the globe and above a night horizon. */
  stars: boolean;
  /** Rivers animate downstream where USGS 3DHP maps a direction; gauges light their own reach. */
  waterFlow: boolean;
}>;

export type SceneEffectKey = keyof SceneEffectSettings;
export const SCENE_EFFECT_KEYS: readonly SceneEffectKey[] = ["cinematic", "curtain", "sunSync", "kansasGlow", "relief2d", "columns", "buildings", "stars", "waterFlow"];

/** Defaults make no new network requests (2D relief and flowing water off; the star catalog is bundled). */
export const DEFAULT_SCENE_EFFECTS: SceneEffectSettings = Object.freeze({
  cinematic: true, curtain: true, sunSync: false, kansasGlow: true, relief2d: false, columns: true, buildings: true, stars: true, waterFlow: false,
});
export const SCENE_EFFECTS_STORAGE_KEY = "kfm-scene-effects-v1";

export type SceneLookPreset = "cinematic" | "natural" | "plain";
export const SCENE_LOOK_PRESETS: Readonly<Record<SceneLookPreset, Readonly<{ label: string; detail: string; settings: SceneEffectSettings }>>> = Object.freeze({
  cinematic: { label: "Cinematic", detail: "Every effect, including 2D relief", settings: Object.freeze({ cinematic: true, curtain: true, sunSync: false, kansasGlow: true, relief2d: true, columns: true, buildings: true, stars: true, waterFlow: true }) },
  natural: { label: "Natural", detail: "Relief, sky and 3D data; no glow", settings: Object.freeze({ cinematic: true, curtain: false, sunSync: true, kansasGlow: false, relief2d: true, columns: true, buildings: true, stars: true, waterFlow: true }) },
  plain: { label: "Plain", detail: "The original flat look", settings: Object.freeze({ cinematic: false, curtain: false, sunSync: false, kansasGlow: false, relief2d: false, columns: false, buildings: false, stars: false, waterFlow: false }) },
});

export const matchingLookPreset = (settings: SceneEffectSettings): SceneLookPreset | null =>
  (Object.keys(SCENE_LOOK_PRESETS) as SceneLookPreset[]).find((id) => SCENE_EFFECT_KEYS.every((key) => SCENE_LOOK_PRESETS[id].settings[key] === settings[key])) ?? null;

export type SceneView = "2d" | "tilted" | "terrain" | "globe";
/** Which views each effect shows in, for the GUI. */
export const SCENE_EFFECT_OPTIONS: readonly Readonly<{ key: SceneEffectKey; label: string; detail: string; views: readonly SceneView[]; network?: boolean; motion?: boolean }>[] = Object.freeze([
  { key: "cinematic", label: "Cinematic relief & sky", detail: "Deeper relief shading, richer sky and distance haze", views: ["tilted", "terrain", "globe"] },
  { key: "kansasGlow", label: "Kansas glow", detail: "Soft outline glow on every basemap; a beacon from orbit", views: ["2d", "tilted", "terrain", "globe"] },
  { key: "relief2d", label: "Shaded relief in 2D", detail: "Display-DEM hillshade under flat maps", views: ["2d", "tilted"], network: true },
  { key: "curtain", label: "Kansas light curtain", detail: "Glowing border walls when tilted and on the globe", views: ["tilted", "terrain", "globe"], motion: true },
  { key: "columns", label: "3D data columns", detail: "Earthquake magnitude and streamflow as columns when tilted", views: ["tilted", "terrain", "globe"] },
  { key: "buildings", label: "Lit 3D buildings", detail: "Height-shaded provider buildings matched to the scene light", views: ["tilted", "terrain"] },
  { key: "sunSync", label: "Follow the real sun", detail: "Light and sky follow the sun over the map center", views: ["tilted", "terrain", "globe"] },
  { key: "stars", label: "Real night sky", detail: "Hipparcos stars where they are right now, the Milky Way and the Sun from orbit; above the horizon at night", views: ["tilted", "terrain", "globe"], motion: true },
  { key: "waterFlow", label: "Flowing water", detail: "Rivers flow downstream where USGS 3DHP maps a direction; a USGS gauge reading lights its own reach. Zoom 10 or closer", views: ["2d", "tilted", "terrain", "globe"], network: true, motion: true },
]);

export function parseSceneEffects(raw: unknown): SceneEffectSettings {
  if (!raw || typeof raw !== "object") return DEFAULT_SCENE_EFFECTS;
  const value = raw as Record<string, unknown>;
  return Object.freeze(Object.fromEntries(SCENE_EFFECT_KEYS.map((key) => [key, typeof value[key] === "boolean" ? value[key] : DEFAULT_SCENE_EFFECTS[key]])) as SceneEffectSettings);
}

/** Device-local preference. Blocked storage simply keeps the defaults. */
export function readSceneEffects(): SceneEffectSettings {
  try {
    const stored = window.localStorage.getItem(SCENE_EFFECTS_STORAGE_KEY);
    return stored ? parseSceneEffects(JSON.parse(stored)) : DEFAULT_SCENE_EFFECTS;
  } catch {
    return DEFAULT_SCENE_EFFECTS;
  }
}

export function writeSceneEffects(settings: SceneEffectSettings): void {
  try { window.localStorage.setItem(SCENE_EFFECTS_STORAGE_KEY, JSON.stringify(settings)); } catch { /* preference only */ }
}

// The renderer helpers in map-runtime and terrain-relief-style are called from
// many places with (map, preset, azimuth). Registering settings per map keeps
// those call sites unchanged.
const registered = new WeakMap<object, SceneEffectSettings>();
export const registerSceneEffects = (map: object, settings: SceneEffectSettings): void => { registered.set(map, settings); };
export const sceneEffectsFor = (map: object): SceneEffectSettings => registered.get(map) ?? DEFAULT_SCENE_EFFECTS;

const normalizeDegrees = (value: number, fallback: number) => ((Number.isFinite(value) ? value : fallback) % 360 + 360) % 360;
const clamp = (value: number, minimum: number, maximum: number) => Math.max(minimum, Math.min(maximum, value));

// ---------------------------------------------------------------------------
// Sun-following light
// ---------------------------------------------------------------------------

export type SceneLight = Readonly<{
  preset: SceneLightPreset;
  /** Direction the light comes from, degrees clockwise from north. */
  azimuth: number;
  /** Light height above the horizon in degrees. */
  altitude: number;
  source: "manual" | "sun" | "moon";
  /** Computed solar elevation when following the sun. */
  solarElevation?: number;
}>;

export const DEFAULT_LIGHT_ALTITUDE: Record<SceneLightPreset, number> = { night: 40, dusk: 22, clear: 38 };

/**
 * Converts the computed solar position into a scene light. Below the horizon
 * the scene uses a cool fill light opposite the sun so relief stays readable;
 * it is labelled "moon" because it is not the sun.
 */
export function sunSceneLight(instant: Date | number, longitude: number, latitude: number): SceneLight {
  const sun = solarPositionAt(instant, clamp(latitude, -89.9, 89.9), longitude);
  const elevation = sun.elevationDegrees;
  if (elevation <= 0) {
    return { preset: elevation > -6 ? "dusk" : "night", azimuth: normalizeDegrees(sun.azimuthDegrees + 180, 0), altitude: 35, source: "moon", solarElevation: elevation };
  }
  return { preset: elevation < 12 ? "dusk" : "clear", azimuth: normalizeDegrees(sun.azimuthDegrees, 0), altitude: clamp(elevation, 6, 75), source: "sun", solarElevation: elevation };
}

/** The light the renderer should use for the requested manual preset. */
export function effectiveSceneLight(map: Pick<MapLibreMap, "getCenter">, preset: SceneLightPreset, azimuth: number, now: number = Date.now()): SceneLight {
  if (sceneEffectsFor(map).sunSync) {
    try {
      const center = map.getCenter();
      return sunSceneLight(now, center.lng, center.lat);
    } catch { /* fall back to the manual light */ }
  }
  return { preset, azimuth: normalizeDegrees(azimuth, 210), altitude: DEFAULT_LIGHT_ALTITUDE[preset], source: "manual" };
}

// ---------------------------------------------------------------------------
// Sky and atmosphere
// ---------------------------------------------------------------------------

/** Globe atmosphere fades out as the camera approaches the study area. */
// Kept below full strength so the planet surface and Kansas glow stay legible.
export const GLOBE_ATMOSPHERE_BLEND = ["interpolate", ["linear"], ["zoom"], 0, 0.62, 4, 0.55, 7, 0.2] as const;

/** Deeper zenith, warmer horizons and ground fog for aerial perspective. */
export const CINEMATIC_SKIES = Object.freeze({
  night: Object.freeze({
    "sky-color": "#030b1a",
    "horizon-color": "#1d4a63",
    "fog-color": "#0b2033",
    "fog-ground-blend": 0.55,
    "horizon-fog-blend": 0.82,
    "sky-horizon-blend": 0.62,
  }),
  dusk: Object.freeze({
    "sky-color": "#1a2550",
    "horizon-color": "#f2a46a",
    "fog-color": "#b4857a",
    "fog-ground-blend": 0.5,
    "horizon-fog-blend": 0.6,
    "sky-horizon-blend": 0.72,
  }),
  clear: Object.freeze({
    "sky-color": "#2f78bd",
    "horizon-color": "#d7ecf5",
    "fog-color": "#8fb3cc",
    "fog-ground-blend": 0.3,
    "horizon-fog-blend": 0.45,
    "sky-horizon-blend": 0.7,
  }),
});

export const CINEMATIC_LIGHT_COLOR: Record<SceneLightPreset, string> = { night: "#9fc3e6", dusk: "#ffc68f", clear: "#fff6dc" };
export const CINEMATIC_LIGHT_INTENSITY: Record<SceneLightPreset, number> = { night: 0.36, dusk: 0.62, clear: 0.55 };

// ---------------------------------------------------------------------------
// Relief lighting
// ---------------------------------------------------------------------------

type ReliefPalette = Readonly<{ highlight: string; shadow: string; accent: string }>;

// Chosen by side-by-side renders of the same DEM: MapLibre's multidirectional
// method averages its lights and washes Kansas relief out, while the standard
// method with a warm key highlight, deep shadow and full exaggeration keeps
// drainage networks crisp from statewide to local zoom.
const RELIEF_PALETTES: Record<SceneLightPreset, ReliefPalette> = {
  night: { highlight: "#bcd8ee", shadow: "#020818", accent: "#2c4a6e" },
  dusk: { highlight: "#ffcf94", shadow: "#060c24", accent: "#3f5f8a" },
  clear: { highlight: "#fff4dc", shadow: "#0b2136", accent: "#587d94" },
};

export type ReliefLook = "general" | "topographic";

export function cinematicHillshadePaint(look: ReliefLook, preset: SceneLightPreset, azimuth: number) {
  const palette = RELIEF_PALETTES[preset];
  return {
    "hillshade-method": "standard" as const,
    "hillshade-illumination-direction": normalizeDegrees(azimuth, 235),
    "hillshade-illumination-altitude": 45,
    "hillshade-highlight-color": palette.highlight,
    "hillshade-shadow-color": look === "topographic" ? "#16343c" : palette.shadow,
    "hillshade-accent-color": look === "topographic" ? "#9a8067" : palette.accent,
    "hillshade-exaggeration": 1,
  };
}

/** Hillshade paint for this map's settings. Effects off restores the legacy
 * palette exactly; following the sun replaces the manual light direction. */
export const reliefPaintFor = (
  map: Pick<MapLibreMap, "getCenter">,
  look: ReliefLook,
  light: SceneLightPreset,
  azimuth: number,
): Record<string, unknown> => {
  const scene = effectiveSceneLight(map, light, azimuth);
  if (sceneEffectsFor(map).cinematic) return cinematicHillshadePaint(look, scene.preset, scene.azimuth);
  return { ...terrainHillshadePaint(look, scene.preset, scene.azimuth), "hillshade-method": "standard", "hillshade-illumination-altitude": 45 };
};

const TERRAIN_HILLSHADE_LAYER = "kfm-terrain-hillshade";
type PaintProperty = Parameters<MapLibreMap["setPaintProperty"]>[1];
type PaintValue = Parameters<MapLibreMap["setPaintProperty"]>[2];

/** Lighting is a display treatment of the active raster DEM, not a new
 * elevation surface. Only changed properties are written so tiles do not
 * repaint for an unchanged view. */
export const applyTerrainReliefStyle = (map: MapLibreMap, look: ReliefLook, light: SceneLightPreset, azimuth: number): void => {
  if (!map.getLayer(TERRAIN_HILLSHADE_LAYER)) return;
  for (const [key, value] of Object.entries(reliefPaintFor(map, look, light, azimuth))) {
    const property = key as PaintProperty;
    if (JSON.stringify(map.getPaintProperty(TERRAIN_HILLSHADE_LAYER, property)) !== JSON.stringify(value)) {
      map.setPaintProperty(TERRAIN_HILLSHADE_LAYER, property, value as PaintValue);
    }
  }
};

// ---------------------------------------------------------------------------
// Kansas border curtain
// ---------------------------------------------------------------------------

export const CURTAIN_LAYER_ID = "scene-kansas-aurora";
// Updated with the same effective light used by the sky and buildings. This
// registry is sampled by the existing layer, never by an extra repaint loop.
const curtainLights = new WeakMap<object, SceneLightPreset>();
export const registerCurtainLight = (map: object, preset: SceneLightPreset): void => { curtainLights.set(map, preset); };
/** Hidden near top-down, where a wall reads as a doubled outline. */
export const CURTAIN_MIN_PITCH = 12;

// One shimmer clock for the page; null holds the curtain still (reduced
// motion, ambient motion off, Battery saver or a hidden tab).
let shimmerStartedAt: number | null = null;
export const setCurtainShimmer = (active: boolean): void => {
  shimmerStartedAt = active ? (shimmerStartedAt ?? performance.now()) : null;
};
const shimmerClock = (): number | null => shimmerStartedAt === null ? null : (performance.now() - shimmerStartedAt) / 1000;

/** On the globe the wall is seen against the planet's limb at any tilt;
 * on flat maps it needs a tilt to read as a wall rather than a doubled line. */
export const curtainShouldShow = (settings: SceneEffectSettings, pitch: number, efficient: boolean, projection: string | undefined): boolean =>
  settings.curtain && !efficient && (projection === "globe" || (Number.isFinite(pitch) && pitch >= CURTAIN_MIN_PITCH));

/**
 * Adds (or removes) the curtain beneath every data overlay and sets its
 * visibility for the current camera. Safe to call on every style load.
 */
export function syncBorderCurtain(map: MapLibreMap, efficient: boolean): boolean {
  if (!sceneEffectsFor(map).curtain) {
    if (map.getLayer(CURTAIN_LAYER_ID)) map.removeLayer(CURTAIN_LAYER_ID);
    return true;
  }
  // Decorative: a GPU or shader failure removes the curtain and never
  // degrades the map, its sources or the style synchronization.
  try {
    if (!map.getLayer(CURTAIN_LAYER_ID)) {
      const beforeId = map.getStyle().layers?.find((layer) => layer.type === "symbol"
        || (layer.id.startsWith("kfm-") && layer.id !== "kfm-background") || layer.id.startsWith("external-"))?.id;
      map.addLayer(createAuroraCurtainLayer({ id: CURTAIN_LAYER_ID, ring: KANSAS_OUTLINE, clock: shimmerClock,
        palette: () => CURTAIN_PALETTES[curtainLights.get(map) ?? "night"],
      }), beforeId);
      map.setLayoutProperty(CURTAIN_LAYER_ID, "visibility", "none");
    }
    syncBorderCurtainVisibility(map, efficient);
    return true;
  } catch {
    try { if (map.getLayer(CURTAIN_LAYER_ID)) map.removeLayer(CURTAIN_LAYER_ID); } catch { /* already gone */ }
    return false;
  }
}

export function syncBorderCurtainVisibility(map: MapLibreMap, efficient: boolean): void {
  if (!map.getLayer(CURTAIN_LAYER_ID)) return;
  const projection = map.getProjection()?.type;
  const visibility = curtainShouldShow(sceneEffectsFor(map), map.getPitch(), efficient, typeof projection === "string" ? projection : undefined) ? "visible" : "none";
  if (map.getLayoutProperty(CURTAIN_LAYER_ID, "visibility") !== visibility) map.setLayoutProperty(CURTAIN_LAYER_ID, "visibility", visibility);
}

export const curtainIsVisible = (map: MapLibreMap): boolean =>
  Boolean(map.getLayer(CURTAIN_LAYER_ID)) && map.getLayoutProperty(CURTAIN_LAYER_ID, "visibility") === "visible";

// ---------------------------------------------------------------------------
// Selection pulse
// ---------------------------------------------------------------------------

export const SELECTION_PULSE_LAYER_ID = "kfm-selection-pulse";
export const SELECTION_PULSE_PERIOD_MS = 1100;
export const SELECTION_PULSE_DURATION_MS = SELECTION_PULSE_PERIOD_MS * 2;

/** One expanding ring per period. Returns false once the ping has finished. */
export function selectionPulseFrame(elapsedMs: number): { radius: number; opacity: number; running: boolean } {
  if (!(elapsedMs >= 0) || elapsedMs >= SELECTION_PULSE_DURATION_MS) return { radius: 12, opacity: 0, running: false };
  const progress = (elapsedMs % SELECTION_PULSE_PERIOD_MS) / SELECTION_PULSE_PERIOD_MS;
  const eased = 1 - (1 - progress) ** 3;
  return { radius: 12 + eased * 30, opacity: 0.9 * (1 - progress), running: true };
}

export function applySelectionPulse(map: MapLibreMap, elapsedMs: number): boolean {
  if (!map.getLayer(SELECTION_PULSE_LAYER_ID)) return false;
  const frame = selectionPulseFrame(elapsedMs);
  map.setPaintProperty(SELECTION_PULSE_LAYER_ID, "circle-radius", frame.radius);
  map.setPaintProperty(SELECTION_PULSE_LAYER_ID, "circle-stroke-opacity", frame.opacity);
  return frame.running;
}

// ---------------------------------------------------------------------------
// Flyover
// ---------------------------------------------------------------------------

export type FlyoverStop = Readonly<{
  id: string;
  label: string;
  region: string;
  center: readonly [number, number];
  zoom: number;
  pitch: number;
  bearing: number;
  /** Degrees of slow drift while lingering. */
  drift: number;
  flightMs: number;
  dwellMs: number;
}>;

/**
 * Camera targets for a terrain tour. Centers are approximate viewpoints over
 * well-known Kansas landscapes, not surveyed locations or mapped boundaries.
 */
export const KANSAS_FLYOVER: readonly FlyoverStop[] = Object.freeze([
  { id: "statewide", label: "Kansas", region: "Statewide view from the south-west", center: [-98.3, 38.35], zoom: 6.15, pitch: 55, bearing: -14, drift: 10, flightMs: 3200, dwellMs: 4200 },
  { id: "arikaree", label: "Arikaree Breaks", region: "Cheyenne County · north-west Kansas", center: [-101.78, 39.93], zoom: 10.4, pitch: 64, bearing: 32, drift: 22, flightMs: 7000, dwellMs: 6000 },
  { id: "smoky-hill", label: "Smoky Hill chalk country", region: "Gove and Logan counties · western Kansas", center: [-100.6, 38.82], zoom: 10.1, pitch: 62, bearing: -38, drift: 20, flightMs: 6000, dwellMs: 6000 },
  { id: "red-hills", label: "Red Hills", region: "Barber and Comanche counties · south-central Kansas", center: [-98.86, 37.2], zoom: 10.5, pitch: 66, bearing: 128, drift: 24, flightMs: 6500, dwellMs: 6500 },
  { id: "flint-hills", label: "Flint Hills", region: "Chase County · tallgrass prairie uplands", center: [-96.57, 38.44], zoom: 10.6, pitch: 64, bearing: -62, drift: 22, flightMs: 6500, dwellMs: 6500 },
  { id: "kansas-river", label: "Kansas River valley", region: "Douglas County · north-east Kansas", center: [-95.42, 39.02], zoom: 10.2, pitch: 60, bearing: 74, drift: 18, flightMs: 5500, dwellMs: 6000 },
  { id: "return", label: "Kansas", region: "Back to the statewide view", center: [-98.38, 38.48], zoom: 6, pitch: 48, bearing: 0, drift: 0, flightMs: 6500, dwellMs: 0 },
].map((stop) => Object.freeze({ ...stop, center: Object.freeze([...stop.center]) as unknown as readonly [number, number] })));
