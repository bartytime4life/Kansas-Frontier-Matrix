import { BASEMAP_RELIEF_DEM_SOURCE_ID } from "./category-basemaps";
import { CATEGORY_MAPS, categorySceneLabel, type CategoryCamera, type CategoryScene } from "./category-maps";
import { externalContextSource } from "./external-context-sources";
import type { BasemapKey } from "./map-runtime";
import type { StyleSpecification } from "./maplibre-seam";

/**
 * What the welcome's background map shows: the real map each topic opens
 * with (its basemap, scene and camera from CATEGORY_MAPS), never an
 * illustration. Until a visitor points at a topic it shows the Explorer's
 * default vector map over the whole state, so opt-in providers (imagery,
 * aerials, topo, the Terrarium DEM) are requested only for a topic the
 * visitor chose to preview. A previewed topic also shows its starter data
 * layers, drawn as the Explorer draws them.
 */
export type WelcomeView = Readonly<{
  /** The topic, or null for the statewide default. */
  topic: string | null;
  basemap: BasemapKey;
  scene: CategoryScene;
  camera: CategoryCamera;
  /** Starter data layers the preview draws (provider-context ids). */
  starters: readonly string[];
  /** Whether the county starter is drawn as population prisms, as the map draws it. */
  prisms: boolean;
  /** Caption: the map's name and what it shows. */
  name: string;
  detail: string;
}>;

/**
 * Starters a preview leaves out: each needs live machinery the welcome does
 * not run (GOES imagery its satellite frame list, river gauges the River Pulse
 * adapter). They appear when the map is opened. Radar is previewed as its
 * newest current scan.
 */
export const WELCOME_PREVIEW_SKIPPED_STARTERS: ReadonlySet<string> = new Set(["noaa-goes-geocolor", "usgs-streamflow"]);

export const WELCOME_DEM_SOURCE_ID = "welcome-terrain-dem";
export const WELCOME_TERRAIN_EXAGGERATION = 1.5;

export const WELCOME_IDLE_VIEW: WelcomeView = Object.freeze({
  topic: null,
  basemap: "standard",
  scene: "2d",
  camera: Object.freeze({ center: [-98.38, 38.48] as const, zoom: 6.1, pitch: 0, bearing: 0 }),
  starters: Object.freeze([]),
  prisms: false,
  name: "Kansas",
  detail: "The Explorer's default vector map · choose a category to preview its map",
});

export function welcomeView(topic: string | null): WelcomeView {
  const look = topic && Object.hasOwn(CATEGORY_MAPS, topic) ? CATEGORY_MAPS[topic as keyof typeof CATEGORY_MAPS] : null;
  if (!look) return WELCOME_IDLE_VIEW;
  const starters = look.starters.filter(id => !WELCOME_PREVIEW_SKIPPED_STARTERS.has(id));
  return { topic: look.topic, basemap: look.basemap, scene: look.scene, camera: look.camera, starters, prisms: Boolean(look.overlays?.includes("population")), name: look.name, detail: `${categorySceneLabel(look.scene)} · ${look.lede}` };
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
  return { ...style, projection, sources: { ...style.sources, [WELCOME_DEM_SOURCE_ID]: { ...dem } }, terrain: { source: WELCOME_DEM_SOURCE_ID, exaggeration: WELCOME_TERRAIN_EXAGGERATION } };
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
