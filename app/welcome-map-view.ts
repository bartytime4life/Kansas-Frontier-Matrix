import { BASEMAP_RELIEF_DEM_SOURCE_ID } from "./category-basemaps";
import { CATEGORY_MAPS, categorySceneLabel, type CategoryCamera, type CategoryScene } from "./category-maps";
import { externalContextSource } from "./external-context-sources";
import type { OfficialContextId } from "./live-context";
import type { TopicId } from "./layer-workspaces";
import type { BasemapKey } from "./map-runtime";
import type { StyleSpecification } from "./maplibre-seam";

/**
 * Real geography, using the Explorer's renderers and source adapters. Selected
 * topics visit a useful geographic scale instead of repeating the statewide
 * view. These preview cameras and layers do not change the working map.
 * Until a visitor points at a topic it shows the Explorer's
 * default vector map over the whole state, so opt-in providers (imagery,
 * aerials, topo, the Terrarium DEM) are requested only for a topic the
 * visitor chose to preview. A previewed topic also shows its starter data
 * layers and a few lightweight scientific tools, drawn as the Explorer draws
 * them. Preview-only additions do not change the working map's defaults.
 */
export type WelcomeScientificLayer = "land-cover" | "animal-records" | "cropland" | "daylight";
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
  /** Short map key, retained in the phone's compact preview. */
  key?: string;
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
// Animal records reuse the Observatory's coarse GBIF carrier. ALPR reports
// retain the adapter's generalized cells, never exact camera locations.
const PREVIEW_CONTEXT: Partial<Record<TopicId, readonly OfficialContextId[]>> = {
  water: ["usgs-wbd-watersheds"],
  evidence: ["census-counties"],
  land: ["blm-plss-sections"],
  "public-safety": ["deflock-alpr"],
};
const SCIENTIFIC_LAYERS: Partial<Record<TopicId, readonly WelcomeScientificLayer[]>> = {
  agriculture: ["cropland"],
  ecology: ["land-cover"],
  flora: ["land-cover"],
  fauna: ["animal-records"],
  sky: ["daylight"],
};
const PREVIEW_DETAIL: Partial<Record<TopicId, string>> = {
  water: "Published USGS/NRCS watershed boundaries over rivers and lakes; live gauge samples load in the opened map.",
  agriculture: "USDA NASS crop classes over Kansas aerial imagery; crop classification is separate from soil-moisture measurements.",
  ecology: "Tuttle Creek and the Big Blue River: NLCD 2021 classes and published watershed boundaries on real imagery and 1.5× terrain.",
  flora: "Flint Hills near Tallgrass Prairie: NLCD 2021 grassland, forest and water classes at 30 m over aerial imagery and 1.5× terrain. Cover is not a species inventory.",
  fauna: "GBIF Animalia occurrence records from 2025 in coarse hexagons over a labelled Kansas map. Includes observations and specimens; shading is not abundance, absence, tracks or habitat.",
  sky: "Calculated current daylight and twilight on the globe; solar geometry, not observed clouds or stars.",
  land: "BLM township and section survey lines over Kansas 2024 aerial imagery near the Sixth Principal Meridian; survey references, not ownership or access.",
  evidence: "Shawnee County's actual 2020 Census boundary and population record, highlighted on the map. Provider context, not released KFM evidence.",
  "public-safety": "Community-reported ALPR areas around Wichita, generalized to 0.05° cells. Counts are mapped reports, not verified devices or live activity; no crime, court or live emergency feed.",
};

// Named geographic views, not an invented surface or a second map renderer.
// Fine land-cover cells and survey sections need local-scale cameras; GBIF's
// coarse aggregate remains at regional scale and source zoom never exceeds six.
const GEOGRAPHIC_VIEWS: Partial<Record<TopicId, Partial<Pick<WelcomeView, "basemap" | "scene" | "camera" | "name" | "key">>>> = {
  flora: { basemap: "kansas-aerial", scene: "terrain", camera: { center: [-96.56, 38.43], zoom: 10.1, pitch: 52, bearing: -16 }, name: "Flint Hills vegetation", key: "NLCD 2021 · 30 m · grassland / forest / water" },
  fauna: { basemap: "standard", scene: "2d", camera: { center: [-98.38, 38.48], zoom: 6.5, pitch: 0, bearing: 0 }, name: "Kansas animal records", key: "GBIF · 2025 · coarse record density, not animal abundance" },
  ecology: { basemap: "imagery", scene: "terrain", camera: { center: [-96.64, 39.32], zoom: 9.1, pitch: 48, bearing: -24 }, name: "Big Blue River landscape", key: "NLCD 2021 · 30 m + USGS watershed boundaries" },
  land: { basemap: "kansas-aerial", scene: "2d", camera: { center: [-97.37, 39.62], zoom: 11.3, pitch: 0, bearing: 0 }, name: "Survey sections on the land", key: "BLM PLSS · townships + sections · not property lines" },
  history: { camera: { center: [-97.45, 38.86], zoom: 8.8, pitch: 0, bearing: 0 }, name: "Abilene–Salina routes", key: "KDOT · 1918 roads + abandoned rail reference" },
  evidence: { basemap: "civic", camera: { center: [-95.76, 39.04], zoom: 8.6, pitch: 0, bearing: 0 }, name: "Shawnee County source record", key: "Census 2020 · actual boundary + population record" },
  "public-safety": { basemap: "storm", camera: { center: [-97.34, 37.69], zoom: 9.1, pitch: 0, bearing: 0 }, name: "Wichita reported ALPR areas", key: "DeFlock / OSM · 0.05° report cells · not live activity" },
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
  const geography = GEOGRAPHIC_VIEWS[look.topic] ?? {};
  return { topic: look.topic, basemap: look.basemap, scene: look.scene, camera: look.camera, ...geography, starters, scientificLayers: SCIENTIFIC_LAYERS[look.topic] ?? [], prisms: Boolean(look.overlays?.includes("population")), name: geography.name ?? look.name, detail: `${categorySceneLabel(geography.scene ?? look.scene)} · ${PREVIEW_DETAIL[look.topic] ?? look.lede}` };
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
