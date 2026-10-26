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
  /** One thing to try on this map, shown in the tip strip while the map is open. */
  tip: string;
  basemap: BasemapKey;
  scene: CategoryScene;
  camera: CategoryCamera;
  starters: readonly OfficialContextId[];
  /** Specialty overlays this look switches on, such as the 3D airspace layer. */
  overlays?: readonly ("aviation" | "population")[];
  /**
   * Explorer tools the dock offers for this look. `transect` starts the
   * existing terrain investigation: draw a line, then preview its
   * unexaggerated display-DEM profile. `flow` switches the Scene studio's
   * flowing-water effect on or off. `underground` opens the Underground view
   * of recorded well logs, cores and aquifer sections. `daylight` shows the
   * calculated night side and twilight bands at the current time. `area`
   * starts the existing polygon measurement for outlining a field or parcel.
   * `radar` opens the live NOAA radar loop on the map. `population` shows or
   * hides the county population prisms and their Kansas density-group legend.
   * `soil` shows NASA SMAP L4 modelled soil moisture (9 km cells) at a chosen
   * depth, pulling a field-scale view out to the region the cells describe.
   * `aquifer` switches the High Plains map between KGS saturated thickness,
   * depth to water and the aquifer extent, with the KGS classes as its legend.
   * `reviewed` steps through the reviewed hourly snapshots the site's own
   * database holds for the look's source (gauges or alerts). `photoreal`
   * drapes the 2024 one-foot Kansas aerial on the USGS 3DEP DEM at true
   * vertical scale, with OSM building heights, and flies to real landscapes.
   */
  tools?: readonly ("transect" | "flow" | "underground" | "daylight" | "area" | "radar" | "population" | "soil" | "aquifer" | "reviewed" | "photoreal" | "quakes" | "outlook")[];
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
  engineering: { topic: "engineering", name: "Structures in relief", lede: "State bridges on a lit 3D landscape where the Big Blue meets the Kansas River, so crossings read against the valleys they span.", tip: "Inspect bridge records near the view from Layers for this map, or draw a cross-section across a valley.", basemap: "network", scene: "terrain", camera: tilted(56, -16, 8.6, [-96.6, 39.17]), starters: ["kdot-bridges-state"], tools: ["transect"], light: "survey", swatch: ["#f2efe9", "#d6553a", "#3a3a3a"] },
  transport: { topic: "transport", name: "Network map", lede: "KDOT highways and active rail around Wichita on a clean network base; zoom out for the statewide road classes.", tip: "KDOT roads and rail draw from city scale; zoom out for the statewide road classes on the base.", basemap: "network", scene: "2d", camera: Object.freeze({ center: [-97.34, 37.69] as const, zoom: 9, pitch: 0, bearing: 0 }), starters: ["kdot-roads", "kdot-rail-active"], swatch: ["#f2efe9", "#e08a3c", "#3a3a3a"] },
  aviation: { topic: "aviation", name: "Aviation chart", lede: "A sectional-style chart with the FAA airspace above it as 3D volumes, airports, drone ceilings and live weather.", tip: "FAA airspace drawn in 3D over the chart, with airports and drone ceilings. Display only; not for navigation.", basemap: "aviation-chart", scene: "terrain", camera: tilted(58, -18, 7.9, [-97.4, 37.72]), starters: [], overlays: ["aviation"], light: "daylight", swatch: ["#cfe0ae", "#14306a", "#f5d96a"] },
  weather: { topic: "weather", name: "Storm desk", lede: "Radar and active alerts over towns, on a neutral dark base that keeps reflectivity colours true.", tip: "Each radar frame keeps its NOAA scan time. Select an alert area for its NWS event, severity and expiry.", basemap: "storm", scene: "2d", camera: STATEWIDE, starters: ["nws-alerts", "nws-radar"], tools: ["radar", "outlook", "reviewed"], light: "blue", swatch: ["#12171d", "#3fae6a", "#e0c33a"] },
  disaster: { topic: "disaster", name: "Hazard watch", lede: "Alerts, satellite fire detections and fire reports over a dark base, each on its own clock.", tip: "Select a fire detection to compare it with nearby fire reports; each record keeps its own time.", basemap: "storm", scene: "2d", camera: STATEWIDE, starters: ["nws-alerts", "nasa-gibs-fire-points", "nifc-fire-reports"], tools: ["reviewed"], light: "blue", swatch: ["#12171d", "#e8622c", "#f2c14e"] },
  water: { topic: "water", name: "River network", lede: "Stream gauges along glowing rivers, streams and lakes on a deep-water base.", tip: "Select a gauge for its USGS discharge and history; Show river flow moves the water downstream.", basemap: "hydro", scene: "2d", camera: STATEWIDE, starters: ["usgs-streamflow"], tools: ["flow", "reviewed"], light: "blue", swatch: ["#0b1d2c", "#1c6a99", "#7fd3f7"] },
  groundwater: { topic: "groundwater", name: "Aquifer map", lede: "How much water-bearing High Plains aquifer is left: KGS 2022–2024 saturated thickness in feet, beside depth to water.", tip: "Switch to depth to water; select an area for its KGS class, or explore underground for well logs and cores.", basemap: "prairie", scene: "2d", camera: Object.freeze({ center: [-100.0, 38.45] as const, zoom: 6.2, pitch: 0, bearing: 0 }), starters: ["kgs-saturated-thickness"], tools: ["aquifer", "underground"], light: "survey", swatch: ["#17231f", "#7fb3b0", "#c9a466"] },
  geology: { topic: "geology", name: "Landform relief", lede: "USGS earthquakes over a coloured relief model in 3D: the past 30 days, or every M2.5+ event in Kansas since 1973, coloured by year.", tip: "Select an earthquake for its USGS magnitude, depth and time; draw a cross-section across the land.", basemap: "relief", scene: "terrain", camera: tilted(52, 20), starters: ["usgs-earthquakes"], tools: ["quakes", "transect", "underground"], light: "survey", swatch: ["#cdc884", "#a98965", "#c94c3c"] },
  terrain: { topic: "terrain", name: "Relief model", lede: "The land surface in 3D, coloured by elevation and lit by the sun; tilt and turn to read the slopes.", tip: "Tilt and turn to read the slopes; a cross-section gives the unexaggerated elevation profile.", basemap: "relief", scene: "terrain", camera: tilted(62, -24, 7.4, [-99.6, 38.9]), starters: [], tools: ["transect", "photoreal"], light: "golden", swatch: ["#86a866", "#dcc58f", "#a98965"] },
  ecology: { topic: "ecology", name: "Landscape imagery", lede: "Satellite imagery with watershed boundaries: read vegetation, cropland and water by eye. It is not a classified land-cover map.", tip: "Watershed lines are USGS hydrologic units; the imagery shows the landscape, not land-cover classes.", basemap: "imagery", scene: "2d", camera: STATEWIDE, starters: ["usgs-wbd-watersheds"], swatch: ["#3b4a2c", "#7d8f4e", "#a8c7d8"] },
  agriculture: { topic: "agriculture", name: "Field view", lede: "Kansas 2024 aerial imagery for reading fields and pivots up close, with NASA's modelled soil moisture over the region.", tip: "Show soil moisture for NASA's 9 km model of the region; Measure an area outlines a field or pivot.", basemap: "kansas-aerial", scene: "2d", camera: Object.freeze({ center: [-100.9, 37.98] as const, zoom: 10.5, pitch: 0, bearing: 0 }), starters: [], tools: ["area", "soil"], swatch: ["#5c6b3a", "#b7a36a", "#3f5d2e"] },
  history: { topic: "history", name: "Historic atlas", lede: "The 1918 road map and abandoned railroads along the Abilene–Salina corridor, on a parchment atlas of today's rails and towns.", tip: "The 1918 roads and abandoned rail are dated KDOT references over today's geography.", basemap: "historic", scene: "2d", camera: Object.freeze({ center: [-97.45, 38.86] as const, zoom: 8.2, pitch: 0, bearing: 0 }), starters: ["kdot-roads-1918", "kdot-rail-abandoned"], swatch: ["#efe4c8", "#4a3523", "#8c6d47"] },
  land: { topic: "land", name: "Survey grid", lede: "PLSS townships counted from the Sixth Principal Meridian and the 40th-parallel baseline: survey references, not ownership.", tip: "Townships count south from the 40th parallel; ranges count east and west of the Sixth Principal Meridian.", basemap: "topo", scene: "2d", camera: Object.freeze({ center: [-97.37, 39.62] as const, zoom: 8.4, pitch: 0, bearing: 0 }), starters: ["blm-plss-townships"], tools: ["area"], swatch: ["#eae4d3", "#b08a52", "#6c7a5a"] },
  people: { topic: "people", name: "Population in 3D", lede: "Every county as a column: its height and colour show 2020 Census people per square mile of land, by Kansas's density groups.", tip: "Columns rise 100 m per person per square mile of land; select one for its 2020 Census counts.", basemap: "civic", scene: "terrain", camera: tilted(54, -14, 6.3, [-97.3, 38.15]), starters: ["census-counties"], overlays: ["population"], tools: ["population"], swatch: ["#f3f1ec", "#e3dcef", "#6d559b"] },
  government: { topic: "government", name: "Civic map", lede: "Kansas by jurisdiction: state, county and city boundaries with their places, the capital starred.", tip: "Select a county for its Census record, or find a county or place from the search box.", basemap: "civic", scene: "2d", camera: STATEWIDE, starters: ["census-counties"], swatch: ["#f3f1ec", "#6d559b", "#3f2a6b"] },
  places: { topic: "places", name: "Reference map", lede: "Counties and watersheds on the civic base for orienting an investigation.", tip: "Select a county to start an investigation there; watershed lines show the drainage it sits in.", basemap: "civic", scene: "2d", camera: STATEWIDE, starters: ["census-counties", "usgs-wbd-watersheds"], swatch: ["#f3f1ec", "#9fc0d4", "#6d559b"] },
  science: { topic: "science", name: "Satellite view", lede: "The latest NOAA GOES satellite image over Kansas and its neighbours, at its own scan time, with the calculated day–night line.", tip: "Each satellite image keeps its NOAA scan time; show day and night for the calculated terminator.", basemap: "standard", scene: "2d", camera: Object.freeze({ center: [-98.38, 38.5] as const, zoom: 5.4, pitch: 0, bearing: 0 }), starters: ["noaa-goes-geocolor"], tools: ["daylight"], swatch: ["#0b1830", "#2c6fb0", "#e8eef5"] },
  sky: { topic: "sky", name: "Sky globe", lede: "The globe under calculated daylight and night-sky presentation.", tip: "Show day and night for the calculated terminator and twilight bands; cloud cover is not shown.", basemap: "standard", scene: "globe", camera: Object.freeze({ center: [-98.38, 38.48] as const, zoom: 2.6, pitch: 0, bearing: 0 }), starters: [], tools: ["daylight"], swatch: ["#060c1c", "#3b4f8f", "#f2d27a"] },
  evidence: { topic: "evidence", name: "Reference base", lede: "The standard vector base with nothing extra switched on, for inspecting sources.", tip: "Select any mapped feature to open its source, time and limits in the Evidence Drawer.", basemap: "standard", scene: "2d", camera: STATEWIDE, starters: [], swatch: ["#efece4", "#9fb7c9", "#4d4a3f"] },
} satisfies Record<TopicId, CategoryMap>);

export const categoryMap = (topic: string): CategoryMap | undefined =>
  Object.hasOwn(CATEGORY_MAPS, topic) ? CATEGORY_MAPS[topic as TopicId] : undefined;

/** Renderer-facing values for a category scene, matching activateMapRepresentation's modes. */
export const categorySceneLabel = (scene: CategoryScene): string =>
  scene === "terrain" ? "3D terrain" : scene === "globe" ? "Globe" : "2D map";
