import type { TopicId } from "./layer-workspaces";
import type { OfficialContextId } from "./live-context";
import type { BasemapKey } from "./map-runtime";
import type { SceneRecipe } from "./scene-studio";

/**
 * Category maps: the map look each start-page subject opens with. One entry per
 * topic names its basemap, renderer, camera and a few starter context layers,
 * so the welcome, the Layers panel and shared URLs agree on what "the aviation
 * map" or "the water map" is. Choosing one is presentation and navigation:
 * starters are existing provider-context switches, never admitted evidence.
 */
export type CategoryScene = "2d" | "terrain" | "globe";
export type CategoryCamera = Readonly<{ center: readonly [number, number]; zoom: number; pitch: number; bearing: number }>;
export type CategoryMap = Readonly<{
  topic: TopicId;
  /** Short name for the map look, shown on cards and in the scene dock. */
  name: string;
  /** What the visitor will see, in one sentence. */
  lede: string;
  basemap: BasemapKey;
  scene: CategoryScene;
  camera: CategoryCamera;
  starters: readonly OfficialContextId[];
  /** Specialty overlays this look switches on, such as the 3D airspace layer. */
  overlays?: readonly "aviation"[];
  /**
   * The light this look opens under, by scene recipe: only its atmosphere and
   * sun azimuth are applied, never its effect settings. Relief reads best under
   * a raking sun, weather on a dark sky.
   */
  light?: SceneRecipe;
  /** Three colours that sketch the basemap on the start card. */
  swatch: readonly [string, string, string];
}>;

const STATEWIDE = Object.freeze({ center: [-98.38, 38.48] as const, zoom: 5.9, pitch: 0, bearing: 0 });
const tilted = (pitch: number, bearing: number, zoom = 6.1, center: readonly [number, number] = STATEWIDE.center): CategoryCamera =>
  Object.freeze({ center, zoom, pitch, bearing });

export const CATEGORY_MAPS: Readonly<Record<TopicId, CategoryMap>> = Object.freeze({
  engineering: { topic: "engineering", name: "Structures in relief", lede: "State bridges on a lit 3D landscape, so crossings read against the valleys they span.", basemap: "network", scene: "terrain", camera: tilted(58, -16, 7.2, [-97.3, 38.9]), starters: ["kdot-bridges-state"], light: "survey", swatch: ["#f2efe9", "#d6553a", "#3a3a3a"] },
  transport: { topic: "transport", name: "Network map", lede: "Highways by class, route numbers, active rail and bridges on a clean network base.", basemap: "network", scene: "2d", camera: STATEWIDE, starters: ["kdot-roads", "kdot-rail-active"], swatch: ["#f2efe9", "#e08a3c", "#3a3a3a"] },
  aviation: { topic: "aviation", name: "Aviation chart", lede: "A sectional-style chart with the FAA airspace above it as 3D volumes, airports, drone ceilings and live weather.", basemap: "aviation-chart", scene: "terrain", camera: tilted(58, -18, 7.9, [-97.4, 37.72]), starters: [], overlays: ["aviation"], light: "daylight", swatch: ["#cfe0ae", "#14306a", "#f5d96a"] },
  weather: { topic: "weather", name: "Storm desk", lede: "Radar and active alerts over towns and county lines, on a neutral dark base that keeps reflectivity colours true.", basemap: "storm", scene: "2d", camera: STATEWIDE, starters: ["nws-alerts", "nws-radar"], light: "blue", swatch: ["#12171d", "#3fae6a", "#e0c33a"] },
  disaster: { topic: "disaster", name: "Hazard watch", lede: "Alerts and fire detections over a dark base, each on its own clock.", basemap: "storm", scene: "2d", camera: STATEWIDE, starters: ["nws-alerts", "nasa-firms-active-fire"], light: "blue", swatch: ["#12171d", "#e8622c", "#f2c14e"] },
  water: { topic: "water", name: "River network", lede: "Stream gauges along glowing rivers, streams and lakes on a deep-water base.", basemap: "hydro", scene: "2d", camera: STATEWIDE, starters: ["usgs-streamflow"], light: "blue", swatch: ["#0b1d2c", "#1c6a99", "#7fd3f7"] },
  groundwater: { topic: "groundwater", name: "Aquifer map", lede: "The High Plains aquifer extent on an earthen base, ready for the Underground cutaway.", basemap: "prairie", scene: "2d", camera: STATEWIDE, starters: ["kgs-aquifer-high-plains"], light: "survey", swatch: ["#17231f", "#7fb3b0", "#c9a466"] },
  geology: { topic: "geology", name: "Landform relief", lede: "Recorded earthquakes over a coloured relief model in 3D.", basemap: "relief", scene: "terrain", camera: tilted(52, 20), starters: ["usgs-earthquakes"], light: "survey", swatch: ["#cdc884", "#a98965", "#c94c3c"] },
  terrain: { topic: "terrain", name: "Relief model", lede: "The land surface in 3D, coloured by elevation and lit by the sun; tilt and turn to read the slopes.", basemap: "relief", scene: "terrain", camera: tilted(62, -24, 7.4, [-99.6, 38.9]), starters: ["usgs-3dep-hillshade"], light: "golden", swatch: ["#86a866", "#dcc58f", "#a98965"] },
  ecology: { topic: "ecology", name: "Land cover view", lede: "Satellite imagery with watershed boundaries for landscape questions.", basemap: "imagery", scene: "2d", camera: STATEWIDE, starters: ["usgs-wbd-watersheds"], swatch: ["#3b4a2c", "#7d8f4e", "#a8c7d8"] },
  agriculture: { topic: "agriculture", name: "Field view", lede: "Kansas 2024 aerial imagery for reading fields and pivots up close.", basemap: "kansas-aerial", scene: "2d", camera: Object.freeze({ center: [-100.9, 37.98] as const, zoom: 10.5, pitch: 0, bearing: 0 }), starters: [], swatch: ["#5c6b3a", "#b7a36a", "#3f5d2e"] },
  history: { topic: "history", name: "Historic map", lede: "The 1918 road map on USGS topographic context.", basemap: "topo", scene: "2d", camera: STATEWIDE, starters: ["kdot-roads-1918"], swatch: ["#efe6cf", "#9c6b3c", "#4d4a3f"] },
  land: { topic: "land", name: "Survey grid", lede: "PLSS townships on topographic context: survey references, not ownership.", basemap: "topo", scene: "2d", camera: STATEWIDE, starters: ["blm-plss-townships"], swatch: ["#eae4d3", "#b08a52", "#6c7a5a"] },
  people: { topic: "people", name: "Community map", lede: "County outlines on the civic base, ready for aggregate Census context.", basemap: "civic", scene: "2d", camera: STATEWIDE, starters: ["census-counties"], swatch: ["#f3f1ec", "#e3dcef", "#6d559b"] },
  government: { topic: "government", name: "Civic map", lede: "Kansas by jurisdiction: state, county and city boundaries with their places, the capital starred.", basemap: "civic", scene: "2d", camera: STATEWIDE, starters: ["census-counties"], swatch: ["#f3f1ec", "#6d559b", "#3f2a6b"] },
  places: { topic: "places", name: "Reference map", lede: "Counties and watersheds on the civic base for orienting an investigation.", basemap: "civic", scene: "2d", camera: STATEWIDE, starters: ["census-counties", "usgs-wbd-watersheds"], swatch: ["#f3f1ec", "#9fc0d4", "#6d559b"] },
  science: { topic: "science", name: "Observation globe", lede: "Kansas on the globe with satellite context, then zoom in to the instruments.", basemap: "standard", scene: "globe", camera: Object.freeze({ center: [-98.38, 38.48] as const, zoom: 3.2, pitch: 0, bearing: 0 }), starters: ["noaa-goes-geocolor"], swatch: ["#0b1830", "#2c6fb0", "#e8eef5"] },
  sky: { topic: "sky", name: "Sky globe", lede: "The globe under calculated daylight and night-sky presentation.", basemap: "standard", scene: "globe", camera: Object.freeze({ center: [-98.38, 38.48] as const, zoom: 2.6, pitch: 0, bearing: 0 }), starters: [], swatch: ["#060c1c", "#3b4f8f", "#f2d27a"] },
  evidence: { topic: "evidence", name: "Reference base", lede: "The standard vector base with nothing extra switched on, for inspecting sources.", basemap: "standard", scene: "2d", camera: STATEWIDE, starters: [], swatch: ["#efece4", "#9fb7c9", "#4d4a3f"] },
} satisfies Record<TopicId, CategoryMap>);

export const categoryMap = (topic: string): CategoryMap | undefined =>
  Object.hasOwn(CATEGORY_MAPS, topic) ? CATEGORY_MAPS[topic as TopicId] : undefined;

/** Renderer-facing values for a category scene, matching activateMapRepresentation's modes. */
export const categorySceneLabel = (scene: CategoryScene): string =>
  scene === "terrain" ? "3D terrain" : scene === "globe" ? "Globe" : "2D map";
