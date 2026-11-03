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

/**
 * The slow camera drift while the welcome plays: tilted and globe views turn
 * about their center, flat maps ease gently in and back out. Each leg is one
 * eased move; the engine alternates legs until paused.
 */
export function welcomeDriftLeg(view: WelcomeView, leg: number): Readonly<{ bearing: number; zoom: number; duration: number }> {
  const out = leg % 2 === 0;
  if (view.scene === "2d") return { bearing: view.camera.bearing, zoom: view.camera.zoom + (out ? 0.35 : 0), duration: 24_000 };
  return { bearing: view.camera.bearing + (out ? 24 : 0), zoom: view.camera.zoom, duration: 30_000 };
}
