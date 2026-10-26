import type { ExpressionSpecification, LayerSpecification, SourceSpecification, StyleSpecification } from "./maplibre-seam";
import { externalContextSource } from "./external-context-sources";
import { ORIENTATION_SOURCE_ID, orientationSource } from "./kansas-orientation";
import type { CategoryBasemapKey } from "./category-basemap-keys";

/**
 * Category base maps: purpose-made cartography built from the same OpenFreeMap
 * vector tiles and fonts as the standard style, plus the registered Terrarium
 * display DEM for relief. No new provider, key or request host is introduced.
 *
 * - Aviation chart: a sectional-chart reading. Banded elevation tint and
 *   hillshade, quiet water and roads, yellow built-up areas, and the
 *   OpenMapTiles aeroway and aerodrome layers drawn as runways, aprons and
 *   circled airport symbols with ICAO/IATA identifiers.
 * - Government & civic: a light reference map where state, county and city
 *   boundaries and their places are the subject, with land and roads receding.
 * - River network: a deep-water ground where rivers glow by size and streams,
 *   wetlands and river names carry the drainage.
 * - Relief model: a smooth hypsometric tint under strong hillshade, so the
 *   land surface is the subject; roads and labels stay quiet.
 * - Storm desk: a neutral charcoal ground that keeps radar and alert colours
 *   true, with towns and the state line to read where weather is hitting.
 * - Network map: a light base with the road hierarchy in colour, route
 *   numbers, classic dashed rail and bridges.
 * - Historic atlas: a parchment ground with sepia relief and a 1° graticule,
 *   where railroads are the subject in classic atlas style, modern roads
 *   recede and city names are letter-spaced capitals.
 *
 * County lines are drawn only where jurisdictions are the subject (civic), and
 * river lines only where drainage is (river network) or where a chart uses them
 * as landmarks (aviation). Every other style leaves them out, so a map opens on
 * its own subject; the census-counties and 3DHP layers add them on request.
 *
 * Layer ids avoid the `kfm-` and `external-` prefixes (except `kfm-background`)
 * so overlay placement keeps treating them as basemap. Every layer here is
 * display context, never evidence.
 */
export const OPENMAPTILES_SOURCE_ID = "openmaptiles";
export const BASEMAP_RELIEF_DEM_SOURCE_ID = "basemap-relief-dem";
export const BASEMAP_HILLSHADE_LAYER_ID = "basemap-relief-hillshade";

const openFreeMap = externalContextSource("openfreemap-liberty");
const terrarium = externalContextSource("aws-mapzen-terrarium");
const OPENFREEMAP_ORIGIN = new URL(openFreeMap.requestUrl).origin;
const TILEJSON_URL = `${OPENFREEMAP_ORIGIN}/planet`;
const GLYPHS_URL = `${OPENFREEMAP_ORIGIN}/fonts/{fontstack}/{range}.pbf`;
const REGULAR = ["Noto Sans Regular"];
const BOLD = ["Noto Sans Bold"];
const ITALIC = ["Noto Sans Italic"];

const FEET_PER_METER = 3.28084;
const ft = (feet: number) => Math.round(feet / FEET_PER_METER);
const zoomRamp = (...stops: number[]): ExpressionSpecification =>
  ["interpolate", ["linear"], ["zoom"], ...stops] as unknown as ExpressionSpecification;

/** Each category basemap carries one hillshade under this id; the scene's sun direction re-aims it. */
const hillshade = (exaggeration: number, shadow: string, highlight: string, accent: string): LayerSpecification => ({
  id: BASEMAP_HILLSHADE_LAYER_ID, type: "hillshade", source: BASEMAP_RELIEF_DEM_SOURCE_ID, paint: {
    "hillshade-exaggeration": exaggeration, "hillshade-shadow-color": shadow, "hillshade-highlight-color": highlight, "hillshade-accent-color": accent,
    "hillshade-illumination-direction": 315, "hillshade-illumination-anchor": "map",
  },
});

function vectorSources(): Record<string, SourceSpecification> {
  return {
    [OPENMAPTILES_SOURCE_ID]: { type: "vector", url: TILEJSON_URL, attribution: openFreeMap.attribution },
    // Capped at zoom 11 like the 3D terrain carrier; closer views overzoom it.
    [BASEMAP_RELIEF_DEM_SOURCE_ID]: { type: "raster-dem", tiles: [terrarium.requestUrl], tileSize: 256, maxzoom: 11, encoding: "terrarium", attribution: terrarium.attribution },
    [ORIENTATION_SOURCE_ID]: orientationSource(),
  };
}

/** Sectional-chart elevation bands, in metres, at 1,000 ft steps (Kansas spans about 680–4,040 ft). */
export const AVIATION_TINT_BANDS: readonly (readonly [number, string])[] = Object.freeze([
  [ft(0), "#bcd6a4"], [ft(1000), "#cfe0ae"], [ft(2000), "#e2e4b8"], [ft(3000), "#ead7ab"], [ft(4000), "#e1c597"], [ft(5000), "#d6b48a"],
]);

/**
 * Hard-edged bands like a printed chart. MapLibre builds the color-relief ramp
 * from `interpolate` stops, so each band edge is a pair of stops one metre apart.
 */
const aviationTint = (): ExpressionSpecification => {
  const stops = AVIATION_TINT_BANDS.flatMap(([metres, color], index) => {
    const next = AVIATION_TINT_BANDS[index + 1];
    return next ? [metres, color, next[0] - 1, color] : [metres, color, metres + 3000, color];
  });
  return ["interpolate", ["linear"], ["elevation"], ...stops] as unknown as ExpressionSpecification;
};

const airportIdent: ExpressionSpecification = ["coalesce", ["get", "icao"], ["get", "iata"], ""] as unknown as ExpressionSpecification;

function aviationLayers(): LayerSpecification[] {
  const omt = OPENMAPTILES_SOURCE_ID;
  return [
    { id: "kfm-background", type: "background", paint: { "background-color": "#e6dfc6" } },
    { id: "chart-elevation-tint", type: "color-relief", source: BASEMAP_RELIEF_DEM_SOURCE_ID, paint: { "color-relief-color": aviationTint(), "color-relief-opacity": 0.9 } } as LayerSpecification,
    { id: BASEMAP_HILLSHADE_LAYER_ID, type: "hillshade", source: BASEMAP_RELIEF_DEM_SOURCE_ID, paint: {
      "hillshade-exaggeration": 0.55, "hillshade-shadow-color": "#5d4a2c", "hillshade-highlight-color": "#fffbea", "hillshade-accent-color": "#7a6744",
      "hillshade-illumination-direction": 315, "hillshade-illumination-anchor": "map",
    } },
    { id: "chart-urban", type: "fill", source: omt, "source-layer": "landuse", filter: ["in", ["get", "class"], ["literal", ["residential", "commercial", "industrial", "retail"]]],
      paint: { "fill-color": "#f5d96a", "fill-opacity": zoomRamp(5, 0.85, 12, 0.55, 14, 0.25), "fill-outline-color": "#c9a92c" } },
    { id: "chart-water", type: "fill", source: omt, "source-layer": "water", paint: { "fill-color": "#a7cbe3", "fill-outline-color": "#3f7fb4" } },
    { id: "chart-waterway", type: "line", source: omt, "source-layer": "waterway", filter: ["in", ["get", "class"], ["literal", ["river", "canal", "stream"]]],
      layout: { "line-cap": "round", "line-join": "round" },
      paint: { "line-color": "#3f7fb4", "line-width": ["interpolate", ["linear"], ["zoom"], 6, ["match", ["get", "class"], "river", 0.9, 0.2], 12, ["match", ["get", "class"], "river", 2.4, 0.9]], "line-opacity": 0.85 } },
    { id: "chart-kansas-outline", type: "line", source: ORIENTATION_SOURCE_ID, filter: ["==", ["get", "role"], "outline"],
      paint: { "line-color": "#5a4f3c", "line-width": zoomRamp(4, 1, 10, 2), "line-opacity": 0.6 } },
    { id: "chart-graticule", type: "line", source: ORIENTATION_SOURCE_ID, filter: ["==", ["get", "role"], "graticule"], paint: { "line-color": "#4b6a92", "line-width": 0.7, "line-opacity": 0.5, "line-dasharray": [6, 3] } },
    { id: "chart-state-boundary", type: "line", source: omt, "source-layer": "boundary", filter: ["all", ["==", ["get", "admin_level"], 4], ["!=", ["get", "maritime"], 1]],
      paint: { "line-color": "#5a4f3c", "line-width": zoomRamp(4, 1, 10, 2.2), "line-dasharray": [5, 2, 1, 2] } },
    { id: "chart-rail", type: "line", source: omt, "source-layer": "transportation", filter: ["==", ["get", "class"], "rail"], minzoom: 7,
      paint: { "line-color": "#2f2f2f", "line-width": zoomRamp(7, 0.6, 13, 1.4), "line-dasharray": [3, 1.5] } },
    { id: "chart-roads-minor", type: "line", source: omt, "source-layer": "transportation", minzoom: 10, filter: ["in", ["get", "class"], ["literal", ["secondary", "tertiary", "minor"]]],
      layout: { "line-cap": "round" }, paint: { "line-color": "#b27a9a", "line-width": zoomRamp(10, 0.4, 15, 1.6), "line-opacity": 0.6 } },
    { id: "chart-roads-major", type: "line", source: omt, "source-layer": "transportation", filter: ["in", ["get", "class"], ["literal", ["motorway", "trunk", "primary"]]],
      layout: { "line-cap": "round", "line-join": "round" },
      paint: { "line-color": "#a8326e", "line-width": zoomRamp(5, 0.5, 9, 1.2, 14, 3), "line-opacity": 0.8 } },
    { id: "chart-aerodrome-area", type: "fill", source: omt, "source-layer": "aeroway", filter: ["==", ["get", "class"], "aerodrome"],
      paint: { "fill-color": "#c9cfe6", "fill-opacity": 0.45, "fill-outline-color": "#1d3d7a" } },
    { id: "chart-apron", type: "fill", source: omt, "source-layer": "aeroway", minzoom: 12, filter: ["all", ["==", ["geometry-type"], "Polygon"], ["==", ["get", "class"], "apron"]],
      paint: { "fill-color": "#b4bbd2", "fill-opacity": 0.85 } },
    { id: "chart-taxiway", type: "line", source: omt, "source-layer": "aeroway", minzoom: 11, filter: ["all", ["==", ["geometry-type"], "LineString"], ["==", ["get", "class"], "taxiway"]],
      layout: { "line-cap": "round" }, paint: { "line-color": "#4d6496", "line-width": zoomRamp(11, 0.6, 15, 4) } },
    { id: "chart-runway", type: "line", source: omt, "source-layer": "aeroway", minzoom: 8, filter: ["all", ["==", ["geometry-type"], "LineString"], ["==", ["get", "class"], "runway"]],
      layout: { "line-cap": "butt" }, paint: { "line-color": "#14306a", "line-width": zoomRamp(8, 1.6, 11, 4, 15, 26) } },
    { id: "chart-runway-area", type: "fill", source: omt, "source-layer": "aeroway", minzoom: 11, filter: ["all", ["==", ["geometry-type"], "Polygon"], ["==", ["get", "class"], "runway"]],
      paint: { "fill-color": "#14306a" } },
    { id: "chart-place-labels", type: "symbol", source: omt, "source-layer": "place", filter: ["in", ["get", "class"], ["literal", ["city", "town", "village"]]],
      layout: {
        "text-field": ["get", "name"], "text-font": ["match", ["get", "class"], "city", ["literal", BOLD], ["literal", REGULAR]],
        "text-size": ["interpolate", ["linear"], ["zoom"], 6, ["match", ["get", "class"], "city", 12, 9], 12, ["match", ["get", "class"], "city", 17, 13]],
        "text-letter-spacing": 0.04, "text-transform": "uppercase", "symbol-sort-key": ["get", "rank"], "text-max-width": 8,
      },
      paint: { "text-color": "#2b2a24", "text-halo-color": "rgba(246,240,214,0.9)", "text-halo-width": 1.4 } },
    { id: "chart-airport-ring", type: "circle", source: omt, "source-layer": "aerodrome_label", minzoom: 6,
      paint: {
        "circle-radius": zoomRamp(6, 3.5, 10, 7, 14, 9), "circle-color": "rgba(255,255,255,0.25)",
        "circle-stroke-width": zoomRamp(6, 1.4, 12, 2.4),
        "circle-stroke-color": ["match", ["get", "class"], "military", "#6a3d9a", "private", "#a8326e", "#14306a"],
      } },
    { id: "chart-airport-labels", type: "symbol", source: omt, "source-layer": "aerodrome_label", minzoom: 7,
      layout: {
        "text-field": ["step", ["zoom"], airportIdent, 10, ["format", airportIdent, { "font-scale": 1 }, "\n", {}, ["get", "name"], { "font-scale": 0.78, "text-font": ["literal", REGULAR] }]],
        "text-font": BOLD, "text-size": zoomRamp(7, 10, 12, 13), "text-offset": [0, 1.15], "text-anchor": "top", "text-max-width": 9,
      },
      paint: { "text-color": ["match", ["get", "class"], "military", "#5b2f88", "private", "#8f2a5e", "#14306a"], "text-halo-color": "rgba(246,240,214,0.95)", "text-halo-width": 1.6 } },
    { id: "chart-water-labels", type: "symbol", source: omt, "source-layer": "water_name", minzoom: 9,
      layout: { "text-field": ["get", "name"], "text-font": ITALIC, "text-size": 11 }, paint: { "text-color": "#2f6a9c", "text-halo-color": "rgba(220,235,245,0.8)", "text-halo-width": 1 } },
  ] as LayerSpecification[];
}

function civicLayers(): LayerSpecification[] {
  const omt = OPENMAPTILES_SOURCE_ID;
  return [
    { id: "kfm-background", type: "background", paint: { "background-color": "#f3f1ec" } },
    { id: BASEMAP_HILLSHADE_LAYER_ID, type: "hillshade", source: BASEMAP_RELIEF_DEM_SOURCE_ID, paint: {
      "hillshade-exaggeration": 0.28, "hillshade-shadow-color": "#8c8577", "hillshade-highlight-color": "#ffffff", "hillshade-accent-color": "#a59d8e",
      "hillshade-illumination-direction": 315, "hillshade-illumination-anchor": "map",
    } },
    { id: "civic-urban", type: "fill", source: omt, "source-layer": "landuse", filter: ["in", ["get", "class"], ["literal", ["residential", "commercial", "industrial", "retail"]]],
      paint: { "fill-color": "#e3dcef", "fill-opacity": zoomRamp(5, 0.9, 13, 0.55) } },
    { id: "civic-parks", type: "fill", source: omt, "source-layer": "park", paint: { "fill-color": "#dce8d2", "fill-opacity": 0.7 } },
    { id: "civic-water", type: "fill", source: omt, "source-layer": "water", paint: { "fill-color": "#c3d9e6" } },
    { id: "civic-roads-minor", type: "line", source: omt, "source-layer": "transportation", minzoom: 11, filter: ["in", ["get", "class"], ["literal", ["secondary", "tertiary", "minor"]]],
      paint: { "line-color": "#ffffff", "line-width": zoomRamp(11, 0.6, 16, 5) } },
    { id: "civic-roads-major", type: "line", source: omt, "source-layer": "transportation", filter: ["in", ["get", "class"], ["literal", ["motorway", "trunk", "primary"]]],
      layout: { "line-cap": "round", "line-join": "round" }, paint: { "line-color": "#d8cbb5", "line-width": zoomRamp(5, 0.5, 10, 1.6, 15, 5) } },
    { id: "civic-municipal-boundary", type: "line", source: omt, "source-layer": "boundary", minzoom: 9, filter: ["==", ["get", "admin_level"], 8],
      paint: { "line-color": "#8a6fb5", "line-width": zoomRamp(9, 0.6, 14, 1.6), "line-dasharray": [2, 2] } },
    { id: "civic-county-boundary", type: "line", source: omt, "source-layer": "boundary", filter: ["==", ["get", "admin_level"], 6],
      paint: { "line-color": "#6d559b", "line-width": zoomRamp(6, 0.6, 10, 1.4, 14, 2.4), "line-opacity": 0.85 } },
    { id: "civic-state-boundary-halo", type: "line", source: omt, "source-layer": "boundary", filter: ["all", ["==", ["get", "admin_level"], 4], ["!=", ["get", "maritime"], 1]],
      paint: { "line-color": "#cbbbe6", "line-width": zoomRamp(4, 4, 10, 9), "line-opacity": 0.7 } },
    { id: "civic-state-boundary", type: "line", source: omt, "source-layer": "boundary", filter: ["all", ["==", ["get", "admin_level"], 4], ["!=", ["get", "maritime"], 1]],
      paint: { "line-color": "#3f2a6b", "line-width": zoomRamp(4, 1.2, 10, 2.6) } },
    // The bundled outline frames the state at every zoom, even when vector tiles fail.
    { id: "civic-kansas-outline", type: "line", source: ORIENTATION_SOURCE_ID, filter: ["==", ["get", "role"], "outline"],
      paint: { "line-color": "#3f2a6b", "line-width": zoomRamp(4, 1.6, 10, 3), "line-opacity": 0.75 } },
    { id: "civic-place-labels", type: "symbol", source: omt, "source-layer": "place", filter: ["in", ["get", "class"], ["literal", ["city", "town", "village"]]],
      layout: {
        // State capitals (OpenMapTiles capital 2 or 4) carry a star.
        "text-field": ["case", ["in", ["get", "capital"], ["literal", [2, 4]]], ["concat", "★ ", ["get", "name"]], ["get", "name"]],
        "text-font": ["match", ["get", "class"], "city", ["literal", BOLD], ["literal", REGULAR]],
        "text-size": ["interpolate", ["linear"], ["zoom"], 6, ["match", ["get", "class"], "city", 13, 10], 12, ["match", ["get", "class"], "city", 18, 13]],
        "symbol-sort-key": ["get", "rank"], "text-max-width": 8,
      },
      paint: { "text-color": "#2c2240", "text-halo-color": "rgba(255,255,255,0.92)", "text-halo-width": 1.5 } },
    { id: "civic-water-labels", type: "symbol", source: omt, "source-layer": "water_name", minzoom: 10,
      layout: { "text-field": ["get", "name"], "text-font": ITALIC, "text-size": 11 }, paint: { "text-color": "#5b84a0", "text-halo-color": "#ffffff", "text-halo-width": 1 } },
  ] as LayerSpecification[];
}

function hydroLayers(): LayerSpecification[] {
  const omt = OPENMAPTILES_SOURCE_ID;
  const river = ["match", ["get", "class"], "river", 1, "canal", 0.55, 0.35];
  return [
    { id: "kfm-background", type: "background", paint: { "background-color": "#0b1d2c" } },
    hillshade(0.5, "#020b12", "#3f6f92", "#0a2a3f"),
    { id: "hydro-wetland", type: "fill", source: omt, "source-layer": "landcover", filter: ["==", ["get", "class"], "wetland"], paint: { "fill-color": "#11455a", "fill-opacity": 0.7 } },
    { id: "hydro-urban", type: "fill", source: omt, "source-layer": "landuse", filter: ["in", ["get", "class"], ["literal", ["residential", "commercial", "industrial"]]], paint: { "fill-color": "#13293a", "fill-opacity": 0.8 } },
    { id: "hydro-roads", type: "line", source: omt, "source-layer": "transportation", filter: ["in", ["get", "class"], ["literal", ["motorway", "trunk", "primary"]]], paint: { "line-color": "#21384b", "line-width": zoomRamp(5, 0.4, 12, 1.6) } },
    { id: "hydro-water", type: "fill", source: omt, "source-layer": "water", paint: { "fill-color": "#1c6a99", "fill-outline-color": "#55b8e6" } },
    // A soft glow under each river, then its bright course, both scaled by class.
    { id: "hydro-waterway-glow", type: "line", source: omt, "source-layer": "waterway", filter: ["in", ["get", "class"], ["literal", ["river", "canal", "stream"]]],
      layout: { "line-cap": "round", "line-join": "round" },
      paint: { "line-color": "#3fa9e0", "line-blur": 3, "line-opacity": 0.35, "line-width": ["interpolate", ["linear"], ["zoom"], 5, ["*", river, 3], 12, ["*", river, 10]] } },
    { id: "hydro-waterway", type: "line", source: omt, "source-layer": "waterway", filter: ["in", ["get", "class"], ["literal", ["river", "canal", "stream"]]],
      layout: { "line-cap": "round", "line-join": "round" },
      paint: { "line-color": ["match", ["get", "class"], "river", "#7fd3f7", "#4aa6d6"], "line-width": ["interpolate", ["linear"], ["zoom"], 5, ["*", river, 1.1], 12, ["*", river, 3.4]], "line-dasharray": ["match", ["get", "class"], "canal", ["literal", [3, 2]], ["literal", [1, 0]]] } },
    { id: "hydro-state-boundary", type: "line", source: omt, "source-layer": "boundary", filter: ["all", ["==", ["get", "admin_level"], 4], ["!=", ["get", "maritime"], 1]], paint: { "line-color": "#d9b45f", "line-width": 1.2, "line-dasharray": [4, 2], "line-opacity": 0.8 } },
    { id: "hydro-kansas-outline", type: "line", source: ORIENTATION_SOURCE_ID, filter: ["==", ["get", "role"], "outline"], paint: { "line-color": "#d9b45f", "line-width": zoomRamp(4, 1.2, 10, 2.2), "line-opacity": 0.7 } },
    { id: "hydro-waterway-labels", type: "symbol", source: omt, "source-layer": "waterway", minzoom: 7, filter: ["==", ["get", "class"], "river"],
      layout: { "symbol-placement": "line", "text-field": ["get", "name"], "text-font": ITALIC, "text-size": zoomRamp(7, 10, 12, 13), "text-letter-spacing": 0.08 },
      paint: { "text-color": "#9fdcf8", "text-halo-color": "#0b1d2c", "text-halo-width": 1.4 } },
    { id: "hydro-water-labels", type: "symbol", source: omt, "source-layer": "water_name", layout: { "text-field": ["get", "name"], "text-font": ITALIC, "text-size": 11 }, paint: { "text-color": "#9fdcf8", "text-halo-color": "#0b1d2c", "text-halo-width": 1.2 } },
    { id: "hydro-place-labels", type: "symbol", source: omt, "source-layer": "place", filter: ["in", ["get", "class"], ["literal", ["city", "town"]]],
      layout: { "text-field": ["get", "name"], "text-font": REGULAR, "text-size": ["match", ["get", "class"], "city", 12, 10], "symbol-sort-key": ["get", "rank"] },
      paint: { "text-color": "#b9d4e4", "text-halo-color": "#0b1d2c", "text-halo-width": 1.4 } },
  ] as LayerSpecification[];
}

/** Smooth hypsometric ramp in metres for the Kansas plains to the Front Range. */
export const RELIEF_RAMP: readonly (readonly [number, string])[] = Object.freeze([
  [150, "#5f8f5a"], [300, "#86a866"], [450, "#a9bb72"], [650, "#cdc884"], [850, "#dcc58f"], [1100, "#c9a77a"], [1500, "#a98965"], [2500, "#e9e2d6"],
]);

function reliefLayers(): LayerSpecification[] {
  const omt = OPENMAPTILES_SOURCE_ID;
  return [
    { id: "kfm-background", type: "background", paint: { "background-color": "#d9d2bf" } },
    { id: "relief-tint", type: "color-relief", source: BASEMAP_RELIEF_DEM_SOURCE_ID,
      paint: { "color-relief-color": ["interpolate", ["linear"], ["elevation"], ...RELIEF_RAMP.flat()], "color-relief-opacity": 0.92 } } as LayerSpecification,
    hillshade(0.85, "#3b2f22", "#fffaf0", "#6b5536"),
    { id: "relief-water", type: "fill", source: omt, "source-layer": "water", paint: { "fill-color": "#7aa6c2" } },
    { id: "relief-roads", type: "line", source: omt, "source-layer": "transportation", minzoom: 7, filter: ["in", ["get", "class"], ["literal", ["motorway", "trunk", "primary"]]], paint: { "line-color": "#f6f1e4", "line-width": zoomRamp(7, 0.5, 13, 2), "line-opacity": 0.75 } },
    { id: "relief-state-boundary", type: "line", source: omt, "source-layer": "boundary", filter: ["all", ["==", ["get", "admin_level"], 4], ["!=", ["get", "maritime"], 1]], paint: { "line-color": "#4a3d2c", "line-width": 1.2, "line-dasharray": [5, 2] } },
    { id: "relief-kansas-outline", type: "line", source: ORIENTATION_SOURCE_ID, filter: ["==", ["get", "role"], "outline"], paint: { "line-color": "#4a3d2c", "line-width": zoomRamp(4, 1, 10, 2), "line-opacity": 0.6 } },
    { id: "relief-peaks", type: "symbol", source: omt, "source-layer": "mountain_peak", minzoom: 9,
      layout: { "text-field": ["concat", "▲ ", ["get", "name"]], "text-font": ITALIC, "text-size": 11 }, paint: { "text-color": "#3b2f22", "text-halo-color": "#f6f1e4", "text-halo-width": 1.2 } },
    { id: "relief-place-labels", type: "symbol", source: omt, "source-layer": "place", filter: ["in", ["get", "class"], ["literal", ["city", "town"]]],
      layout: { "text-field": ["get", "name"], "text-font": REGULAR, "text-size": ["match", ["get", "class"], "city", 12, 10], "symbol-sort-key": ["get", "rank"] },
      paint: { "text-color": "#2f2618", "text-halo-color": "rgba(246,241,228,0.85)", "text-halo-width": 1.3 } },
  ] as LayerSpecification[];
}

function stormLayers(): LayerSpecification[] {
  const omt = OPENMAPTILES_SOURCE_ID;
  return [
    { id: "kfm-background", type: "background", paint: { "background-color": "#12171d" } },
    hillshade(0.18, "#05080b", "#2a333d", "#0c1116"),
    { id: "storm-urban", type: "fill", source: omt, "source-layer": "landuse", filter: ["in", ["get", "class"], ["literal", ["residential", "commercial", "industrial"]]], paint: { "fill-color": "#1d252e", "fill-opacity": 0.85 } },
    { id: "storm-water", type: "fill", source: omt, "source-layer": "water", paint: { "fill-color": "#0f2a3b" } },
    { id: "storm-roads", type: "line", source: omt, "source-layer": "transportation", filter: ["in", ["get", "class"], ["literal", ["motorway", "trunk", "primary"]]], paint: { "line-color": "#2b343f", "line-width": zoomRamp(5, 0.5, 12, 2) } },
    { id: "storm-state-boundary", type: "line", source: omt, "source-layer": "boundary", filter: ["all", ["==", ["get", "admin_level"], 4], ["!=", ["get", "maritime"], 1]], paint: { "line-color": "#8b97a4", "line-width": zoomRamp(4, 1, 10, 2) } },
    { id: "storm-kansas-outline", type: "line", source: ORIENTATION_SOURCE_ID, filter: ["==", ["get", "role"], "outline"], paint: { "line-color": "#8b97a4", "line-width": zoomRamp(4, 1.2, 10, 2.2), "line-opacity": 0.8 } },
    { id: "storm-place-labels", type: "symbol", source: omt, "source-layer": "place", filter: ["in", ["get", "class"], ["literal", ["city", "town", "village"]]],
      layout: { "text-field": ["get", "name"], "text-font": ["match", ["get", "class"], "city", ["literal", BOLD], ["literal", REGULAR]], "text-size": ["interpolate", ["linear"], ["zoom"], 6, ["match", ["get", "class"], "city", 12, 9], 12, ["match", ["get", "class"], "city", 16, 12]], "symbol-sort-key": ["get", "rank"] },
      paint: { "text-color": "#d4dde6", "text-halo-color": "#0a0e12", "text-halo-width": 1.6 } },
  ] as LayerSpecification[];
}

function networkLayers(): LayerSpecification[] {
  const omt = OPENMAPTILES_SOURCE_ID;
  const roadColor = ["match", ["get", "class"], "motorway", "#d6553a", "trunk", "#e08a3c", "primary", "#e3b04b", "secondary", "#c9bfa9", "#d8d2c4"];
  const roadWidth = ["interpolate", ["linear"], ["zoom"], 5, ["match", ["get", "class"], "motorway", 1.4, "trunk", 1.1, "primary", 0.8, 0.3], 14, ["match", ["get", "class"], "motorway", 7, "trunk", 6, "primary", 5, "secondary", 3.5, 2]];
  const roads = ["in", ["get", "class"], ["literal", ["motorway", "trunk", "primary", "secondary", "tertiary", "minor"]]];
  return [
    { id: "kfm-background", type: "background", paint: { "background-color": "#f2efe9" } },
    hillshade(0.2, "#9c9483", "#ffffff", "#b9b1a0"),
    { id: "network-urban", type: "fill", source: omt, "source-layer": "landuse", filter: ["in", ["get", "class"], ["literal", ["residential", "commercial", "industrial", "retail"]]], paint: { "fill-color": "#e6e0d4" } },
    { id: "network-water", type: "fill", source: omt, "source-layer": "water", paint: { "fill-color": "#c6dbe8" } },
    { id: "network-runway", type: "line", source: omt, "source-layer": "aeroway", minzoom: 10, filter: ["==", ["get", "class"], "runway"], paint: { "line-color": "#b9b4aa", "line-width": zoomRamp(10, 2, 15, 18) } },
    { id: "network-state-boundary", type: "line", source: omt, "source-layer": "boundary", filter: ["all", ["==", ["get", "admin_level"], 4], ["!=", ["get", "maritime"], 1]], paint: { "line-color": "#8c8270", "line-width": 1.4, "line-dasharray": [5, 2] } },
    { id: "network-kansas-outline", type: "line", source: ORIENTATION_SOURCE_ID, filter: ["==", ["get", "role"], "outline"], paint: { "line-color": "#8c8270", "line-width": zoomRamp(4, 1, 10, 2), "line-opacity": 0.6 } },
    { id: "network-road-casing", type: "line", source: omt, "source-layer": "transportation", minzoom: 9, filter: roads, layout: { "line-cap": "round", "line-join": "round" },
      paint: { "line-color": ["case", ["==", ["get", "brunnel"], "bridge"], "#5a5246", "#ffffff"], "line-gap-width": roadWidth, "line-width": ["case", ["==", ["get", "brunnel"], "bridge"], 1.6, 0.8] } },
    { id: "network-roads", type: "line", source: omt, "source-layer": "transportation", filter: roads, layout: { "line-cap": "round", "line-join": "round" }, paint: { "line-color": roadColor, "line-width": roadWidth } },
    // Classic rail: a dark line with white ties.
    { id: "network-rail", type: "line", source: omt, "source-layer": "transportation", filter: ["==", ["get", "class"], "rail"], paint: { "line-color": "#3a3a3a", "line-width": zoomRamp(6, 0.8, 14, 3) } },
    { id: "network-rail-ties", type: "line", source: omt, "source-layer": "transportation", minzoom: 8, filter: ["==", ["get", "class"], "rail"], paint: { "line-color": "#f2efe9", "line-width": zoomRamp(8, 0.5, 14, 1.8), "line-dasharray": [2, 3] } },
    { id: "network-route-numbers", type: "symbol", source: omt, "source-layer": "transportation_name", minzoom: 7, filter: ["all", ["has", "ref"], ["in", ["get", "class"], ["literal", ["motorway", "trunk", "primary"]]]],
      layout: { "symbol-placement": "line", "symbol-spacing": 320, "text-field": ["get", "ref"], "text-font": BOLD, "text-size": 10, "text-rotation-alignment": "viewport" },
      paint: { "text-color": "#ffffff", "text-halo-color": ["match", ["get", "class"], "motorway", "#b8432b", "#9a6a1f"], "text-halo-width": 3 } },
    { id: "network-place-labels", type: "symbol", source: omt, "source-layer": "place", filter: ["in", ["get", "class"], ["literal", ["city", "town", "village"]]],
      layout: { "text-field": ["get", "name"], "text-font": ["match", ["get", "class"], "city", ["literal", BOLD], ["literal", REGULAR]], "text-size": ["match", ["get", "class"], "city", 13, 10], "symbol-sort-key": ["get", "rank"] },
      paint: { "text-color": "#3a3329", "text-halo-color": "rgba(255,255,255,0.9)", "text-halo-width": 1.4 } },
  ] as LayerSpecification[];
}

function historicLayers(): LayerSpecification[] {
  const omt = OPENMAPTILES_SOURCE_ID;
  const ink = "#4a3523", sepia = "#8c6d47";
  return [
    { id: "kfm-background", type: "background", paint: { "background-color": "#efe4c8" } },
    hillshade(0.32, "#7a5c38", "#fbf3dd", "#9c7a4c"),
    { id: "historic-graticule", type: "line", source: ORIENTATION_SOURCE_ID, filter: ["==", ["get", "role"], "graticule"], paint: { "line-color": "#b79f74", "line-width": 0.6, "line-opacity": 0.6 } },
    { id: "historic-urban", type: "fill", source: omt, "source-layer": "landuse", filter: ["in", ["get", "class"], ["literal", ["residential", "commercial", "industrial"]]], paint: { "fill-color": "#e2cfa6", "fill-opacity": 0.7 } },
    { id: "historic-water", type: "fill", source: omt, "source-layer": "water", paint: { "fill-color": "#b9c9c0", "fill-outline-color": "#6f8f8a" } },
    // Modern roads recede so the historical overlays and the railroads lead.
    { id: "historic-roads", type: "line", source: omt, "source-layer": "transportation", minzoom: 6, filter: ["in", ["get", "class"], ["literal", ["motorway", "trunk", "primary"]]],
      paint: { "line-color": "#cdb88f", "line-width": zoomRamp(6, 0.4, 13, 1.6) } },
    { id: "historic-state-boundary", type: "line", source: omt, "source-layer": "boundary", filter: ["all", ["==", ["get", "admin_level"], 4], ["!=", ["get", "maritime"], 1]],
      paint: { "line-color": ink, "line-width": zoomRamp(4, 1.2, 10, 2.4), "line-dasharray": [6, 2, 1, 2] } },
    { id: "historic-kansas-outline", type: "line", source: ORIENTATION_SOURCE_ID, filter: ["==", ["get", "role"], "outline"], paint: { "line-color": ink, "line-width": zoomRamp(4, 1.2, 10, 2.4), "line-opacity": 0.55 } },
    // Atlas railroad: an ink line crossed by ties.
    { id: "historic-rail", type: "line", source: omt, "source-layer": "transportation", filter: ["==", ["get", "class"], "rail"], paint: { "line-color": ink, "line-width": zoomRamp(5, 0.8, 14, 2.2) } },
    { id: "historic-rail-ties", type: "line", source: omt, "source-layer": "transportation", minzoom: 7, filter: ["==", ["get", "class"], "rail"], paint: { "line-color": ink, "line-width": zoomRamp(7, 3, 14, 7), "line-dasharray": [0.3, 3] } },
    { id: "historic-place-labels", type: "symbol", source: omt, "source-layer": "place", filter: ["in", ["get", "class"], ["literal", ["city", "town", "village"]]],
      layout: {
        "text-field": ["case", ["==", ["get", "class"], "city"], ["upcase", ["get", "name"]], ["get", "name"]],
        "text-font": ["match", ["get", "class"], "city", ["literal", BOLD], ["literal", REGULAR]],
        "text-size": ["interpolate", ["linear"], ["zoom"], 6, ["match", ["get", "class"], "city", 11, 9], 12, ["match", ["get", "class"], "city", 15, 12]],
        "text-letter-spacing": ["match", ["get", "class"], "city", 0.18, 0.04], "symbol-sort-key": ["get", "rank"], "text-max-width": 9,
      },
      paint: { "text-color": "#3b2a18", "text-halo-color": "rgba(239,228,200,0.92)", "text-halo-width": 1.4 } },
  ] as LayerSpecification[];
}

export function aviationChartStyle(): StyleSpecification {
  return { version: 8, name: "KFM Aviation Chart", glyphs: GLYPHS_URL, sources: vectorSources(), layers: aviationLayers() };
}

export function civicStyle(): StyleSpecification {
  return { version: 8, name: "KFM Government & Civic", glyphs: GLYPHS_URL, sources: vectorSources(), layers: civicLayers() };
}

const style = (name: string, layers: () => LayerSpecification[]) => (): StyleSpecification => ({ version: 8, name, glyphs: GLYPHS_URL, sources: vectorSources(), layers: layers() });

/** Every category basemap: its picker title, network note, map legend and style. */
export const CATEGORY_BASEMAPS: Readonly<Record<CategoryBasemapKey, Readonly<{ title: string; note: string; legend: string; style: () => StyleSpecification }>>> = Object.freeze({
  "aviation-chart": { title: "Aviation chart", style: aviationChartStyle,
    note: "Sectional-style relief, runways and airport identifiers · OpenFreeMap · OpenMapTiles · OpenStreetMap · Terrarium relief · display context · not for navigation",
    legend: "Aviation chart · sectional-style elevation bands at 1,000 ft, hillshade, runways and airport identifiers from OpenMapTiles · display context, not for navigation." },
  civic: { title: "Government & civic", style: civicStyle,
    note: "State, county and city boundaries with their places · OpenFreeMap · OpenMapTiles · OpenStreetMap · display context · not legal boundaries",
    legend: "Government & civic · state, county and city boundaries and places from OpenMapTiles · display context, not legal boundaries." },
  hydro: { title: "River network", style: style("KFM River Network", hydroLayers),
    note: "Rivers, streams, lakes and wetlands on a deep-water ground · OpenFreeMap · OpenMapTiles · OpenStreetMap · Terrarium relief · display context",
    legend: "River network · mapped rivers, streams, lakes and wetlands from OpenMapTiles, scaled by class · display geography, not measured flow or watershed boundaries." },
  relief: { title: "Relief model", style: style("KFM Relief Model", reliefLayers),
    note: "Hypsometric elevation tint and strong hillshade · Terrarium DEM · OpenFreeMap · OpenMapTiles · display context",
    legend: "Relief model · display DEM coloured by elevation with hillshade · mixed-source display elevation, not survey measurement." },
  storm: { title: "Storm desk", style: style("KFM Storm Desk", stormLayers),
    note: "Neutral dark ground with towns and the state line so weather colours stay true · OpenFreeMap · OpenMapTiles · display context",
    legend: "Storm desk · towns and the state line from OpenMapTiles on a neutral dark ground · display context; weather layers keep their own clocks." },
  network: { title: "Network map", style: style("KFM Network Map", networkLayers),
    note: "Road hierarchy, route numbers, rail and bridges · OpenFreeMap · OpenMapTiles · OpenStreetMap · display context",
    legend: "Network map · road classes, route numbers, rail and bridges from OpenMapTiles · display context, not traffic, condition or access." },
  historic: { title: "Historic atlas", style: style("KFM Historic Atlas", historicLayers),
    note: "Parchment atlas ground with railroads and towns · OpenFreeMap · OpenMapTiles · OpenStreetMap · Terrarium relief · display context · present-day geography",
    legend: "Historic atlas · present-day railroads, lakes and towns from OpenMapTiles drawn in an atlas style · display context; historical layers keep their own source dates." },
});
