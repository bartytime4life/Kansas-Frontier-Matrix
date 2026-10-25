import type { ExpressionSpecification, LayerSpecification, SourceSpecification, StyleSpecification } from "./maplibre-seam";
import { externalContextSource } from "./external-context-sources";
import { ORIENTATION_SOURCE_ID, orientationSource } from "./kansas-orientation";

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
    { id: "civic-waterway", type: "line", source: omt, "source-layer": "waterway", filter: ["==", ["get", "class"], "river"], paint: { "line-color": "#9fc0d4", "line-width": zoomRamp(6, 0.5, 12, 1.8) } },
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

export function aviationChartStyle(): StyleSpecification {
  return { version: 8, name: "KFM Aviation Chart", glyphs: GLYPHS_URL, sources: vectorSources(), layers: aviationLayers() };
}

export function civicStyle(): StyleSpecification {
  return { version: 8, name: "KFM Government & Civic", glyphs: GLYPHS_URL, sources: vectorSources(), layers: civicLayers() };
}
