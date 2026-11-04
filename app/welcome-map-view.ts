import { BASEMAP_RELIEF_DEM_SOURCE_ID } from "./category-basemaps";
import { CATEGORY_MAPS, categorySceneLabel, type CategoryCamera, type CategoryScene } from "./category-maps";
import { externalContextSource } from "./external-context-sources";
import type { OfficialContextId } from "./live-context";
import type { TopicId } from "./layer-workspaces";
import type { BasemapKey } from "./map-runtime";
import type { StyleSpecification } from "./maplibre-seam";

/**
 * What the welcome's background map shows: the real map each topic opens
 * with (its basemap, scene and camera from CATEGORY_MAPS), never an
 * illustration. Until a visitor points at a topic it shows the Explorer's
 * default vector map over the whole state, so opt-in providers (imagery,
 * aerials, topo, the Terrarium DEM) are requested only for a topic the
 * visitor chose to preview. A previewed topic also shows its starter data
 * layers and a few lightweight scientific tools, drawn as the Explorer draws
 * them. Preview-only additions do not change the working map's defaults.
 */
export type WelcomeScientificLayer = "land-cover" | "cropland" | "daylight";
export type WelcomeView = Readonly<{
  /** The topic, or null for the statewide default. */
  topic: string | null;
  basemap: BasemapKey;
  scene: CategoryScene;
  camera: CategoryCamera;
  /** Starter data layers the preview draws (provider-context ids). */
  starters: readonly string[];
  scientificLayers: readonly WelcomeScientificLayer[];
  /** Whether the county starter is drawn as population prisms, as the map draws it. */
  prisms: boolean;
  /** Caption: the map's name and what it shows. */
  name: string;
  detail: string;
}>;

/**
 * The full network gauge request belongs to River Pulse, not a pointer hover.
 * Radar and satellite previews use one newest current dated frame, not loops.
 */
export const WELCOME_PREVIEW_SKIPPED_STARTERS: ReadonlySet<string> = new Set(["usgs-streamflow"]);

export const WELCOME_DEM_SOURCE_ID = "welcome-terrain-dem";
export const WELCOME_TERRAIN_EXAGGERATION = 1.5;

// Fill the basemap-only previews with tools already available in the Explorer.
// Water uses published basin geography; a hover never starts River Pulse.
// Wildlife and safety stay at landscape/reference scale, without invented feeds.
const PREVIEW_CONTEXT: Partial<Record<TopicId, readonly OfficialContextId[]>> = {
  water: ["usgs-wbd-watersheds"],
  evidence: ["census-counties"],
  "public-safety": ["census-counties"],
};
const SCIENTIFIC_LAYERS: Partial<Record<TopicId, readonly WelcomeScientificLayer[]>> = {
  agriculture: ["cropland"],
  ecology: ["land-cover"],
  flora: ["land-cover"],
  fauna: ["land-cover"],
  sky: ["daylight"],
};
const PREVIEW_DETAIL: Partial<Record<TopicId, string>> = {
  water: "Published USGS/NRCS watershed boundaries over rivers and lakes; live gauge samples load in the opened map.",
  agriculture: "USDA NASS crop classes over Kansas aerial imagery; crop classification is separate from soil-moisture measurements.",
  ecology: "NLCD 2021 land-cover classes and published watershed boundaries; landscape context, not a habitat model.",
  flora: "NLCD 2021 vegetation and land-cover classes at 30 m; cover classes do not identify plant species.",
  fauna: "NLCD 2021 land-cover context at 30 m; no animal observations, tracks or habitat predictions.",
  sky: "Calculated current daylight and twilight on the globe; solar geometry, not observed clouds or stars.",
  evidence: "2020 Census county source geography; provider context, not released KFM evidence.",
  "public-safety": "2020 Census county reference geography; no crime, court or live emergency-incident feed.",
};

export const WELCOME_IDLE_VIEW: WelcomeView = Object.freeze({
  topic: null,
  basemap: "standard",
  scene: "2d",
  camera: Object.freeze({ center: [-98.38, 38.48] as const, zoom: 6.1, pitch: 0, bearing: 0 }),
  starters: Object.freeze([]),
  scientificLayers: Object.freeze([]),
  prisms: false,
  name: "Kansas",
  detail: "The Explorer's default vector map · choose a category to preview its map",
});

export function welcomeView(topic: string | null): WelcomeView {
  const look = topic && Object.hasOwn(CATEGORY_MAPS, topic) ? CATEGORY_MAPS[topic as keyof typeof CATEGORY_MAPS] : null;
  if (!look) return WELCOME_IDLE_VIEW;
  const starters = [...new Set([...look.starters, ...(PREVIEW_CONTEXT[look.topic] ?? [])])].filter(id => !WELCOME_PREVIEW_SKIPPED_STARTERS.has(id));
  return { topic: look.topic, basemap: look.basemap, scene: look.scene, camera: look.camera, starters, scientificLayers: SCIENTIFIC_LAYERS[look.topic] ?? [], prisms: Boolean(look.overlays?.includes("population")), name: look.name, detail: `${categorySceneLabel(look.scene)} · ${PREVIEW_DETAIL[look.topic] ?? look.lede}` };
}

/**
 * The basemap style as the welcome draws it: the same style, with the globe
 * projection for globe looks, and a Terrarium DEM for 3D terrain looks (its own
 * source, so the style's hillshade source is not also driving the terrain mesh).
 */
export function welcomeStyle(style: StyleSpecification, view: WelcomeView): StyleSpecification {
  const projection = { type: view.scene === "globe" ? "globe" : "mercator" } as StyleSpecification["projection"];
  if (view.scene !== "terrain") {
    const { terrain: _terrain, ...rest } = style;
    return { ...rest, projection };
  }
  const terrarium = externalContextSource("aws-mapzen-terrarium");
  const relief = style.sources?.[BASEMAP_RELIEF_DEM_SOURCE_ID];
  const dem = relief?.type === "raster-dem" ? relief
    : { type: "raster-dem" as const, tiles: [terrarium.requestUrl], tileSize: 256, maxzoom: 11, encoding: "terrarium" as const, attribution: terrarium.attribution };
  return { ...style, projection, sources: { ...style.sources, [WELCOME_DEM_SOURCE_ID]: { ...dem } }, terrain: { source: WELCOME_DEM_SOURCE_ID, exaggeration: view.topic === "aviation" ? 1 : WELCOME_TERRAIN_EXAGGERATION } };
}

type MotionProfile = Readonly<{ east: number; north: number; turn: number; zoom: number; tilt?: number; seconds: number }>;
// Presentation-only camera choreography. Offsets are fractions of the current
// zoom's world span, so a field-scale preview cannot drift across the state.
const MOTION_PROFILES: Readonly<Record<string, MotionProfile>> = {
  transport: { east: .07, north: .035, turn: 0, zoom: .35, seconds: 24 },
  engineering: { east: .025, north: -.018, turn: 18, zoom: .12, tilt: 5, seconds: 28 },
  water: { east: .07, north: -.04, turn: -4, zoom: .15, seconds: 28 },
  groundwater: { east: -.045, north: .025, turn: 0, zoom: .22, seconds: 30 },
  ecology: { east: .03, north: -.035, turn: 5, zoom: .2, seconds: 30 },
  flora: { east: -.025, north: .025, turn: -5, zoom: .28, seconds: 28 },
  fauna: { east: .065, north: .01, turn: 3, zoom: .1, seconds: 32 },
  agriculture: { east: .035, north: -.025, turn: 7, zoom: .18, seconds: 30 },
  history: { east: .055, north: .012, turn: -6, zoom: .15, seconds: 32 },
  land: { east: .025, north: -.025, turn: 8, zoom: .2, seconds: 30 },
  people: { east: .015, north: 0, turn: 20, zoom: .08, tilt: -5, seconds: 32 },
  government: { east: .03, north: .012, turn: 0, zoom: .18, seconds: 30 },
  places: { east: -.04, north: .025, turn: -3, zoom: .24, seconds: 28 },
  science: { east: .035, north: -.015, turn: 0, zoom: -.16, seconds: 32 },
  sky: { east: .05, north: .012, turn: 8, zoom: 0, seconds: 36 },
  evidence: { east: .018, north: 0, turn: 0, zoom: .14, seconds: 30 },
  "public-safety": { east: -.025, north: .018, turn: 0, zoom: .2, seconds: 32 },
};

/** Four slow eased legs: a subject-specific pass, home, a reverse pass, home.
 * The source frame stays fixed; only the camera moves. Every pose is computed
 * from the category's original camera, avoiding cumulative drift. */
export function welcomeDriftLeg(view: WelcomeView, leg: number): Readonly<{ center: readonly [number, number]; pitch: number; bearing: number; zoom: number; duration: number }> {
  const { camera } = view;
  const profile = view.topic ? MOTION_PROFILES[view.topic] : undefined;
  const out = leg % 2 === 0;
  const direction = leg % 4 === 0 ? 1 : -1;
  if (profile) {
    const span = 360 / 2 ** camera.zoom;
    return {
      center: out ? [camera.center[0] + profile.east * span * direction, camera.center[1] + profile.north * span * direction] : camera.center,
      pitch: out ? Math.max(0, Math.min(68, camera.pitch + (profile.tilt ?? 0) * direction)) : camera.pitch,
      bearing: camera.bearing + (out ? profile.turn * direction : 0),
      zoom: camera.zoom + (out ? profile.zoom : 0), duration: profile.seconds * 1000,
    };
  }
  return { center: camera.center, pitch: camera.pitch,
    bearing: camera.bearing + (out && view.scene !== "2d" ? 24 * direction : 0),
    zoom: camera.zoom + (out && view.scene === "2d" ? .35 : 0), duration: view.scene === "2d" ? 24_000 : 30_000 };
}
