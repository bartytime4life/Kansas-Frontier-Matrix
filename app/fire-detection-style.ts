import type { Feature, FeatureCollection, Polygon } from "geojson";
import type { ExpressionSpecification, GeoJSONSource, LayerSpecification, SymbolLayerSpecification, Map as MapLibreMap, StyleImageInterface, StyleImageWebGLData } from "./maplibre-seam";
import { browserRenderBudget, updateGeoJSON, rememberGeoJSON, setVisibleIfChanged, uploadedGeoJSON } from "./map-performance";
import { globeOverviewPaintSize } from "./globe-context";

/**
 * Display treatment for NASA GIBS NOAA-20 VIIRS thermal detections.
 *
 * Zoomed out, each detection is an animated flame glyph standing on its pixel
 * centre. Zoomed in, the glyph gives way to the detection's own ground
 * footprint: a provider scan × track rectangle (metres on the ground, so it
 * scales with zoom and pitch) filled with an ember texture and a soft heat
 * edge. The rectangle is the satellite detection pixel, not a fire perimeter,
 * flame front or burned area, and the motion is illustrative: no frame of it
 * encodes fire behaviour, spread or intensity.
 *
 * The selectable records stay on the provider point source. The footprints are
 * a display-only derivative on a site-local source, so hover and inspection
 * still resolve through the original `-halo`/`-circle` layer ids.
 */

export const FIRE_POINT_LAYER_IDS = Object.freeze({
  halo: "external-nasa-gibs-fire-points-halo",
  circle: "external-nasa-gibs-fire-points-circle",
  heat: "external-nasa-gibs-fire-points-footprint-heat",
  shimmer: "external-nasa-gibs-fire-points-footprint-shimmer",
  edge: "external-nasa-gibs-fire-points-footprint-edge",
  flame: "external-nasa-gibs-fire-points-flame",
});
export const FIRE_POINT_SOURCE_ID = "external-nasa-gibs-fire-points";
/** Site-local (kfm-) so the click/hover fallback never treats a derived
 * rectangle as a separate provider record. */
export const FIRE_FOOTPRINT_SOURCE_ID = "kfm-nasa-gibs-fire-footprints";

export type FireConfidence = "high" | "nominal" | "low";
const CONFIDENCES: readonly FireConfidence[] = ["high", "nominal", "low"];
/** Outer flame colours keep the previous point palette keyed to confidence. */
export const FIRE_CONFIDENCE_COLORS: Readonly<Record<FireConfidence, string>> = Object.freeze({ high: "#ff3757", nominal: "#ff713b", low: "#ffc46c" });
const FLAME_PALETTES: Readonly<Record<FireConfidence, { outer: string; deep: string; mid: string; core: string }>> = Object.freeze({
  high: { outer: "#ff3757", deep: "#a50f2b", mid: "#ff7a2e", core: "#ffe9a0" },
  nominal: { outer: "#ff713b", deep: "#b3300f", mid: "#ffa53a", core: "#fff1b8" },
  low: { outer: "#ffc46c", deep: "#cf7a22", mid: "#ffdc8f", core: "#fffbe8" },
});
export const flameImageId = (confidence: FireConfidence) => `kfm-fire-flame-${confidence}`;
export const FIRE_EMBER_PATTERN_ID = "kfm-fire-ember-texture";

const confidenceMatch = <T extends string>(values: Readonly<Record<FireConfidence, T>>): ExpressionSpecification =>
  ["match", ["get", "confidence"], "high", values.high, "low", values.low, values.nominal];

// ---------------------------------------------------------------------------
// Ground footprints
// ---------------------------------------------------------------------------

const NOAA20_INCLINATION_DEG = 98.74;
const EARTH_ROTATION_MPS = 465.1;
const GROUND_TRACK_SPEED_MPS = 6_800;
/**
 * Approximate azimuth of the NOAA-20 along-track (pixel "track") axis at a
 * latitude, in degrees clockwise from north. Daytime passes are ascending and
 * night passes descending for this 13:30 sun-synchronous orbit. The provider
 * does not supply per-pixel orientation; unknown passes stay north-aligned.
 */
export function noaa20TrackAzimuth(latitude: number, dayNight: unknown): number {
  const ascending = dayNight === "Day" || dayNight === "D";
  const descending = dayNight === "Night" || dayNight === "N";
  if (!ascending && !descending || !Number.isFinite(latitude) || Math.abs(latitude) > 80) return 0;
  const cosLat = Math.cos(latitude * Math.PI / 180);
  const sinHeading = Math.max(-1, Math.min(1, Math.cos(NOAA20_INCLINATION_DEG * Math.PI / 180) / cosLat));
  const north = Math.sqrt(1 - sinHeading ** 2) * GROUND_TRACK_SPEED_MPS * (ascending ? 1 : -1);
  const east = sinHeading * GROUND_TRACK_SPEED_MPS - EARTH_ROTATION_MPS * cosLat;
  const heading = Math.atan2(east, north) * 180 / Math.PI;
  // An axis, not a direction: fold into (-90, 90].
  return heading > 90 ? heading - 180 : heading <= -90 ? heading + 180 : heading;
}

const positiveKm = (value: unknown) => typeof value === "number" && Number.isFinite(value) && value > 0 && value < 10 ? value : null;

/** One detection pixel as a ground rectangle of scan × track kilometres. */
export function fireFootprintPolygon(longitude: number, latitude: number, scanKm: number, trackKm: number, trackAzimuthDeg = 0): Polygon {
  const azimuth = trackAzimuthDeg * Math.PI / 180;
  const track = [Math.sin(azimuth), Math.cos(azimuth)], scan = [Math.cos(azimuth), -Math.sin(azimuth)];
  const halfScan = scanKm * 500, halfTrack = trackKm * 500;
  const metresPerLon = 111_320 * Math.cos(latitude * Math.PI / 180), metresPerLat = 110_574;
  const corner = (s: number, t: number): [number, number] => {
    const east = s * halfScan * scan[0] + t * halfTrack * track[0];
    const north = s * halfScan * scan[1] + t * halfTrack * track[1];
    return [Number((longitude + east / metresPerLon).toFixed(6)), Number((latitude + north / metresPerLat).toFixed(6))];
  };
  const ring = [corner(-1, -1), corner(1, -1), corner(1, 1), corner(-1, 1)];
  return { type: "Polygon", coordinates: [[...ring, ring[0]]] };
}

export type FireFootprints = { collection: FeatureCollection; bounds: [number, number, number, number] | null };
const EMPTY_FOOTPRINTS: FireFootprints = Object.freeze({ collection: Object.freeze({ type: "FeatureCollection", features: [] }) as FeatureCollection, bounds: null });
const derived = new WeakMap<FeatureCollection, FireFootprints>();

/**
 * Derive display footprints from the provider points. A detection without
 * provider scan/track dimensions gets no rectangle; its flame stays instead.
 */
export function deriveFireFootprints(points: FeatureCollection | undefined): FireFootprints {
  if (!points?.features?.length) return EMPTY_FOOTPRINTS;
  const cached = derived.get(points);
  if (cached) return cached;
  const features: Feature<Polygon>[] = [];
  let west = Infinity, south = Infinity, east = -Infinity, north = -Infinity;
  for (const feature of points.features) {
    if (feature.geometry?.type !== "Point") continue;
    const [longitude, latitude] = feature.geometry.coordinates;
    if (!Number.isFinite(longitude) || !Number.isFinite(latitude)) continue;
    west = Math.min(west, longitude); east = Math.max(east, longitude); south = Math.min(south, latitude); north = Math.max(north, latitude);
    const properties = feature.properties ?? {};
    const scanKm = positiveKm(properties.scanKm), trackKm = positiveKm(properties.trackKm);
    if (scanKm === null || trackKm === null) continue;
    const confidence = CONFIDENCES.includes(properties.confidence) ? properties.confidence as FireConfidence : "nominal";
    features.push({ type: "Feature", geometry: fireFootprintPolygon(longitude, latitude, scanKm, trackKm, noaa20TrackAzimuth(latitude, properties.dayNight)),
      properties: { featureId: properties.featureId ?? feature.id ?? null, confidence, display: "satellite-detection-pixel" } });
  }
  const result: FireFootprints = { collection: { type: "FeatureCollection", features }, bounds: Number.isFinite(west) ? [west, south, east, north] : null };
  derived.set(points, result);
  return result;
}

// ---------------------------------------------------------------------------
// Paint and layout
// ---------------------------------------------------------------------------

/** Metres per CSS pixel at z0 for 512 px tiles at mid-Kansas latitude (38.5° N). */
const KANSAS_METRES_PER_PIXEL_Z0 = 40_075_016.686 * Math.cos(38.5 * Math.PI / 180) / 512;
const largestDimensionKm: ExpressionSpecification = ["max", ["to-number", ["get", "scanKm"], 0], ["to-number", ["get", "trackKm"], 0]];
const hasFootprint: ExpressionSpecification = ["all", [">", ["to-number", ["get", "scanKm"], 0], 0], [">", ["to-number", ["get", "trackKm"], 0], 0]];

/**
 * Hit target: covers the flame glyph zoomed out and the whole footprint
 * zoomed in. Linear integer-zoom stops (starting at z4) keep the globe
 * overview scaling in live-context valid.
 */
export const FIRE_HIT_RADIUS: ExpressionSpecification = ["interpolate", ["linear"], ["zoom"],
  4, 11, 9, 13,
  ...[10, 11, 12, 13, 14, 15, 16, 17, 18].flatMap((zoom) => [zoom, ["max", 14, ["*", largestDimensionKm, 0.62 * 1000 * 2 ** zoom / KANSAS_METRES_PER_PIXEL_Z0]]]),
] as ExpressionSpecification;
/** The flame body rises above its pixel centre, so the hit target follows it up while zoomed out. */
export const FIRE_HIT_TRANSLATE = ["interpolate", ["linear"], ["zoom"], 10, ["literal", [0, -9]], 12, ["literal", [0, 0]]] as unknown as [number, number];

/** About 20–30% larger than the former 6.5–10 px dot; shrinks as the footprint takes over. */
export const FLAME_ICON_SIZE: ExpressionSpecification = ["interpolate", ["linear"], ["zoom"], 4, 0.76, 8, 0.93, 10, 1.03, 11, 0.86, 12, 0.62, 13, 0.46];
const flameOpacity = (opacity: number): ExpressionSpecification => ["interpolate", ["linear"], ["zoom"],
  10.5, opacity, 11.5, ["case", hasFootprint, opacity * 0.45, opacity], 12.3, ["case", hasFootprint, 0, opacity], 13.25, ["case", hasFootprint, 0, opacity]];
const haloOpacity = (opacity: number): ExpressionSpecification => ["interpolate", ["linear"], ["zoom"], 10, opacity * 0.3, 12, opacity * 0.14, 13, 0];
const heatOpacity = (opacity: number): ExpressionSpecification => ["interpolate", ["linear"], ["zoom"], 8, 0, 9.5, opacity * 0.82, 11, opacity * 0.94];
const shimmerOpacity = (opacity: number): ExpressionSpecification => ["interpolate", ["linear"], ["zoom"], 8.5, 0, 10, opacity * 0.55, 13, opacity * 0.7];
const edgeOpacity = (opacity: number): ExpressionSpecification => ["interpolate", ["linear"], ["zoom"], 10.5, 0, 12, opacity * 0.34, 15, opacity * 0.45];
/** Pixel widths that grow with the ground footprint (about 0.2 × a 500 m pixel). */
const groundWidth = (factor: number): ExpressionSpecification => ["interpolate", ["linear"], ["zoom"],
  ...[8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18].flatMap((zoom) => [zoom, Number((factor * 1000 * 2 ** zoom / KANSAS_METRES_PER_PIXEL_Z0).toFixed(2))])] as ExpressionSpecification;

const footprintLayers = (): LayerSpecification[] => [
  { id: FIRE_POINT_LAYER_IDS.heat, type: "fill", source: FIRE_FOOTPRINT_SOURCE_ID, minzoom: 8,
    paint: { "fill-pattern": FIRE_EMBER_PATTERN_ID, "fill-opacity": 0, "fill-antialias": true } },
  { id: FIRE_POINT_LAYER_IDS.shimmer, type: "line", source: FIRE_FOOTPRINT_SOURCE_ID, minzoom: 8.5,
    layout: { "line-join": "round" },
    paint: { "line-color": confidenceMatch(FIRE_CONFIDENCE_COLORS), "line-width": groundWidth(0.1), "line-blur": groundWidth(0.09), "line-opacity": 0 } },
  { id: FIRE_POINT_LAYER_IDS.edge, type: "line", source: FIRE_FOOTPRINT_SOURCE_ID, minzoom: 10,
    paint: { "line-color": "#ffc27a", "line-width": ["interpolate", ["linear"], ["zoom"], 10, 0.5, 14, 1, 18, 1.6], "line-opacity": 0 } },
];
const flameLayer = (globe: boolean): SymbolLayerSpecification => ({
  id: FIRE_POINT_LAYER_IDS.flame, type: "symbol", source: FIRE_POINT_SOURCE_ID, maxzoom: 13.5,
  layout: {
    "icon-image": confidenceMatch({ high: flameImageId("high"), nominal: flameImageId("nominal"), low: flameImageId("low") }),
    "icon-size": (globe ? globeOverviewPaintSize(FLAME_ICON_SIZE) : FLAME_ICON_SIZE) as ExpressionSpecification,
    "icon-anchor": "bottom", "icon-offset": [0, FLAME_BASE_PADDING],
    "icon-allow-overlap": true, "icon-ignore-placement": true, "icon-pitch-alignment": "viewport", "icon-rotation-alignment": "viewport",
    // Nearer flames draw in front when the map is tilted.
    "symbol-z-order": "viewport-y",
  },
  paint: { "icon-opacity": 0 },
});

export const FIRE_REPORT_FLAME_ID = "external-nifc-fire-reports-flame";
const REPORT_SOURCE = "external-nifc-fire-reports";
const REPORT_ICON_SIZE: ExpressionSpecification = ["interpolate", ["linear"], ["zoom"], 4, 0.76, 8, 0.93, 10, 1.03];
/** Incident reports retain their own IDs and type-specific palettes; the flame is illustrative. */
export function syncFireReportDisplay(map: MapLibreMap, visible: boolean, opacity: number): void {
  const points = uploadedGeoJSON(map.getSource(REPORT_SOURCE) as GeoJSONSource | undefined);
  const footprints = deriveFireFootprints(points);
  const hasData = Boolean(points?.features?.length);
  if (visible && hasData) ensureFireImages(map);
  if (map.getSource(REPORT_SOURCE) && !map.getLayer(FIRE_REPORT_FLAME_ID)) {
    const layer = flameLayer(false);
    const { maxzoom: _maxzoom, ...reportLayer } = layer;
    void _maxzoom;
    map.addLayer({ ...reportLayer, id: FIRE_REPORT_FLAME_ID, source: REPORT_SOURCE,
      layout: { ...layer.layout, "icon-image": ["match", ["get", "incidentType"],
        "Prescribed fire", flameImageId("low"), "Incident complex", flameImageId("nominal"), flameImageId("high")],
        "icon-size": REPORT_ICON_SIZE } });
  }
  setLayoutExpression(map, FIRE_REPORT_FLAME_ID, "icon-size", map.getProjection?.()?.type === "globe" ? globeOverviewPaintSize(REPORT_ICON_SIZE) : REPORT_ICON_SIZE);
  setVisibleIfChanged(map, FIRE_REPORT_FLAME_ID, visible);
  setPaintExpression(map, FIRE_REPORT_FLAME_ID, "icon-opacity", Math.max(0, Math.min(1, opacity)));
  for (const id of [REPORT_SOURCE + "-halo", REPORT_SOURCE + "-point"]) {
    setPaintExpression(map, id, "circle-opacity", 0);
    setPaintExpression(map, id, "circle-stroke-opacity", 0);
    setPaintExpression(map, id, "circle-translate", [0, -9]);
  }
  syncFireDisplayMotion(map, "reports", visible && opacity > 0 && hasData, footprints.bounds);
}

const setPaintExpression = (map: MapLibreMap, id: string, property: string, value: unknown) => {
  if (!map.getLayer(id)) return;
  const current = map.getPaintProperty(id, property as never);
  if (JSON.stringify(current) !== JSON.stringify(value)) map.setPaintProperty(id, property as never, value as never);
};
const setLayoutExpression = (map: MapLibreMap, id: string, property: string, value: unknown) => {
  if (!map.getLayer(id)) return;
  if (JSON.stringify(map.getLayoutProperty(id, property as never)) !== JSON.stringify(value)) map.setLayoutProperty(id, property as never, value as never);
};

/**
 * Add the derived footprint source and the flame/footprint layers, refresh the
 * derived rectangles, and apply visibility and opacity to every fire layer.
 * Called from applyOfficialContextState after the provider point source and
 * its `-halo`/`-circle` layers exist.
 */
export function syncFireDetectionDisplay(map: MapLibreMap, visible: boolean, opacity: number): void {
  const pointSource = map.getSource(FIRE_POINT_SOURCE_ID) as GeoJSONSource | undefined;
  const points = uploadedGeoJSON(pointSource);
  const footprints = refreshFireFootprints(map);
  const hasData = Boolean(points?.features?.length);
  if (visible && hasData) ensureFireImages(map);
  const globe = map.getProjection?.()?.type === "globe";
  if (map.getSource(FIRE_FOOTPRINT_SOURCE_ID)) for (const layer of footprintLayers()) if (!map.getLayer(layer.id)) map.addLayer(layer);
  if (pointSource && !map.getLayer(FIRE_POINT_LAYER_IDS.flame)) map.addLayer(flameLayer(globe));
  setLayoutExpression(map, FIRE_POINT_LAYER_IDS.flame, "icon-size", globe ? globeOverviewPaintSize(FLAME_ICON_SIZE) : FLAME_ICON_SIZE);

  const amount = Math.max(0, Math.min(1, opacity));
  for (const id of Object.values(FIRE_POINT_LAYER_IDS)) if (map.getLayer(id)) setVisibleIfChanged(map, id, visible);
  setPaintExpression(map, FIRE_POINT_LAYER_IDS.halo, "circle-opacity", haloOpacity(amount));
  // The former solid dot is now the transparent selection/hover target.
  setPaintExpression(map, FIRE_POINT_LAYER_IDS.circle, "circle-opacity", 0);
  setPaintExpression(map, FIRE_POINT_LAYER_IDS.circle, "circle-stroke-opacity", 0);
  setPaintExpression(map, FIRE_POINT_LAYER_IDS.circle, "circle-translate", FIRE_HIT_TRANSLATE);
  setPaintExpression(map, FIRE_POINT_LAYER_IDS.flame, "icon-opacity", flameOpacity(amount));
  setPaintExpression(map, FIRE_POINT_LAYER_IDS.heat, "fill-opacity", heatOpacity(amount));
  setPaintExpression(map, FIRE_POINT_LAYER_IDS.shimmer, "line-opacity", shimmerOpacity(amount));
  setPaintExpression(map, FIRE_POINT_LAYER_IDS.edge, "line-opacity", edgeOpacity(amount));
  syncFireDisplayMotion(map, "detections", visible && amount > 0 && hasData, footprints.bounds);
}

/**
 * Re-derive the footprint source from whatever collection the provider point
 * source last received, including a cleared (empty) one.
 */
export function refreshFireFootprints(map: MapLibreMap): FireFootprints {
  const pointSource = map.getSource(FIRE_POINT_SOURCE_ID) as GeoJSONSource | undefined;
  const footprints = deriveFireFootprints(uploadedGeoJSON(pointSource));
  const existing = map.getSource(FIRE_FOOTPRINT_SOURCE_ID) as GeoJSONSource | undefined;
  if (existing) updateGeoJSON(existing, footprints.collection);
  else if (pointSource) {
    map.addSource(FIRE_FOOTPRINT_SOURCE_ID, { type: "geojson", data: footprints.collection, attribution: "NASA GIBS · VIIRS NOAA-20 thermal anomalies" });
    rememberGeoJSON(map.getSource(FIRE_FOOTPRINT_SOURCE_ID) as GeoJSONSource, footprints.collection);
  }
  if (!footprints.collection.features.length && animators.has(map)) syncFireDisplayMotion(map, "detections", false, null);
  return footprints;
}

// ---------------------------------------------------------------------------
// Animated images
// ---------------------------------------------------------------------------

export const FIRE_FRAME_COUNT = 12;
/** ~12 fps: enough for a flicker, a fraction of the display refresh. */
export const FIRE_FRAME_MS = 84;
/** A cheap clock check between frames, so a repaint lands soon after a frame falls due. */
const FIRE_CHECK_MS = 24;
/** A full, calm frame used when motion is off. */
const STILL_FRAME = 3;
const PIXEL_RATIO = 2;
const FLAME_W = 36, FLAME_H = 48, FLAME_BASE_Y = 40;
/** Logical pixels of glow below the flame base; the icon offset puts the base on the point. */
const FLAME_BASE_PADDING = FLAME_H - FLAME_BASE_Y;
const PATTERN_SIZE = 64;

/** Frame pixels by index; built on first use so only shown frames cost anything. */
type Frames = { width: number; height: number; frame: (index: number) => Uint8ClampedArray };
let flameFrames: Partial<Record<FireConfidence, Frames>> | null = null;
let emberFrames: Frames | null = null;

type Canvas2D = OffscreenCanvasRenderingContext2D | CanvasRenderingContext2D;
const createContext = (width: number, height: number): Canvas2D | null => {
  try {
    if (typeof OffscreenCanvas !== "undefined") return new OffscreenCanvas(width, height).getContext("2d", { willReadFrequently: true });
    if (typeof document !== "undefined") {
      const canvas = document.createElement("canvas");
      canvas.width = width; canvas.height = height;
      return canvas.getContext("2d", { willReadFrequently: true });
    }
  } catch { /* no 2D canvas: the layer draws nothing rather than failing the map */ }
  return null;
};

const rgba = (hex: string, alpha: number) => {
  const value = Number.parseInt(hex.slice(1), 16);
  return `rgba(${value >> 16 & 255},${value >> 8 & 255},${value & 255},${alpha})`;
};

/** A teardrop flame tongue from a base point, tip swaying sideways. */
function tonguePath(ctx: Canvas2D, cx: number, baseY: number, width: number, height: number, sway: number) {
  const tipX = cx + sway, tipY = baseY - height, half = width / 2;
  ctx.beginPath();
  ctx.moveTo(cx, baseY + 1.2);
  ctx.bezierCurveTo(cx - half * 1.05, baseY + 0.6, cx - half * 1.1, baseY - height * 0.32, cx - half * 0.62 + sway * 0.25, baseY - height * 0.52);
  ctx.bezierCurveTo(cx - half * 0.3 + sway * 0.6, baseY - height * 0.7, tipX - half * 0.12, tipY + height * 0.18, tipX, tipY);
  ctx.bezierCurveTo(tipX + half * 0.16, tipY + height * 0.2, cx + half * 0.36 + sway * 0.6, baseY - height * 0.68, cx + half * 0.64 + sway * 0.25, baseY - height * 0.5);
  ctx.bezierCurveTo(cx + half * 1.1, baseY - height * 0.3, cx + half * 1.05, baseY + 0.6, cx, baseY + 1.2);
  ctx.closePath();
}

function drawFlame(ctx: Canvas2D, palette: (typeof FLAME_PALETTES)[FireConfidence], frame: number) {
  const theta = 2 * Math.PI * frame / FIRE_FRAME_COUNT;
  const cx = FLAME_W / 2, baseY = FLAME_BASE_Y;
  const sway = 1.7 * Math.sin(theta) + 0.8 * Math.sin(2 * theta + 1.1);
  const height = 27 * (1 + 0.07 * Math.sin(2 * theta + 0.4) + 0.04 * Math.sin(3 * theta + 2));
  ctx.setTransform(PIXEL_RATIO, 0, 0, PIXEL_RATIO, 0, 0);
  ctx.clearRect(0, 0, FLAME_W, FLAME_H);

  // Ground glow, flattened so it reads as light on the ground.
  ctx.save();
  ctx.translate(cx, baseY); ctx.scale(1, 0.5);
  const glowRadius = 15 * (1 + 0.06 * Math.sin(3 * theta));
  const glow = ctx.createRadialGradient(0, 0, 0, 0, 0, glowRadius);
  glow.addColorStop(0, rgba(palette.outer, 0.72)); glow.addColorStop(0.45, rgba(palette.outer, 0.3)); glow.addColorStop(1, rgba(palette.outer, 0));
  ctx.fillStyle = glow; ctx.beginPath(); ctx.arc(0, 0, glowRadius, 0, 2 * Math.PI); ctx.fill();
  ctx.restore();

  // Side tongues flicker out of phase with the main flame.
  const side = (offset: number, phase: number, scale: number) => {
    const local = 0.55 + 0.25 * Math.sin(2 * theta + phase);
    tonguePath(ctx, cx + offset, baseY, 9 * scale, height * local * scale, sway * 0.6 + offset * 0.18);
  };
  // A dark, soft rim keeps the flame legible on pale basemaps.
  ctx.save();
  ctx.shadowColor = "rgba(28,10,6,0.62)"; ctx.shadowBlur = 2.4 * PIXEL_RATIO;
  ctx.fillStyle = rgba(palette.deep, 0.94);
  tonguePath(ctx, cx, baseY, 19, height, sway); ctx.fill();
  side(-5.2, 0.9, 1); ctx.fill();
  side(5.4, 2.6, 0.95); ctx.fill();
  ctx.restore();

  const outer = ctx.createLinearGradient(0, baseY, 0, baseY - height);
  outer.addColorStop(0, rgba(palette.deep, 1)); outer.addColorStop(0.25, rgba(palette.outer, 1)); outer.addColorStop(0.8, rgba(palette.outer, 0.85)); outer.addColorStop(1, rgba(palette.outer, 0.35));
  ctx.fillStyle = outer;
  tonguePath(ctx, cx, baseY, 17.5, height * 0.97, sway); ctx.fill();
  side(-5, 0.9, 0.86); ctx.fill();
  side(5.2, 2.6, 0.82); ctx.fill();

  const middle = ctx.createLinearGradient(0, baseY, 0, baseY - height * 0.7);
  middle.addColorStop(0, rgba(palette.mid, 1)); middle.addColorStop(1, rgba(palette.mid, 0.55));
  ctx.fillStyle = middle;
  tonguePath(ctx, cx + 0.3 * Math.sin(theta + 1), baseY, 11.5, height * (0.66 + 0.05 * Math.sin(3 * theta + 0.7)), sway * 0.7); ctx.fill();

  const core = ctx.createLinearGradient(0, baseY, 0, baseY - height * 0.4);
  core.addColorStop(0, rgba(palette.core, 1)); core.addColorStop(1, rgba(palette.core, 0.7));
  ctx.fillStyle = core;
  tonguePath(ctx, cx, baseY, 6.5, height * (0.36 + 0.04 * Math.sin(4 * theta)), sway * 0.4); ctx.fill();

  // Two embers rising and fading on a loop.
  for (const [offset, phase] of [[0, 0.15], [0.5, 0.65]] as const) {
    const progress = (frame / FIRE_FRAME_COUNT + offset) % 1;
    const x = cx + 4.5 * Math.sin(2 * Math.PI * (progress + phase)) + (offset ? 3 : -3);
    const y = baseY - 9 - progress * 26;
    ctx.fillStyle = rgba(palette.core, 0.9 * (1 - progress));
    ctx.beginPath(); ctx.arc(x, y, 1.05 - progress * 0.45, 0, 2 * Math.PI); ctx.fill();
  }
}

const EMBER_RAMP: readonly (readonly [number, number, number, number])[] = [
  [0, 46, 6, 3], [0.32, 128, 18, 6], [0.55, 220, 60, 14], [0.75, 255, 138, 34], [0.9, 255, 206, 92], [1, 255, 246, 196],
];
function emberColor(heat: number, out: Uint8ClampedArray, offset: number) {
  let index = 1;
  while (index < EMBER_RAMP.length - 1 && EMBER_RAMP[index][0] < heat) index++;
  const [h0, r0, g0, b0] = EMBER_RAMP[index - 1], [h1, r1, g1, b1] = EMBER_RAMP[index];
  const t = Math.max(0, Math.min(1, (heat - h0) / (h1 - h0)));
  out[offset] = r0 + (r1 - r0) * t; out[offset + 1] = g0 + (g1 - g0) * t; out[offset + 2] = b0 + (b1 - b0) * t;
  out[offset + 3] = 255 * (0.8 + 0.2 * heat);
}

/** Seamless (integer-frequency) smouldering ember field, looping in time. */
export function renderEmberFrame(frame: number, size = PATTERN_SIZE * PIXEL_RATIO): Uint8ClampedArray {
  const data = new Uint8ClampedArray(size * size * 4);
  const theta = 2 * Math.PI * frame / FIRE_FRAME_COUNT, tau = 2 * Math.PI;
  for (let y = 0; y < size; y++) {
    const v = y / size;
    for (let x = 0; x < size; x++) {
      const u = x / size;
      // Domain-warped sums of integer-frequency waves: tiles seamlessly and
      // loops in time, with irregular hot cells instead of a visible lattice.
      const warpA = Math.sin(tau * (2 * u + v) + theta) + 0.6 * Math.sin(tau * (u - 4 * v) + 2.1);
      const warpB = Math.sin(tau * (-u + 3 * v) - theta + 1.3) + 0.6 * Math.sin(tau * (5 * u + 2 * v) + 0.4);
      const n = 0.5 * Math.sin(tau * (3 * u + 2 * v) + 1.9 * warpA + theta)
        + 0.36 * Math.sin(tau * (-2 * u + 5 * v) + 1.6 * warpB + 2 * theta + 0.5)
        + 0.26 * Math.sin(tau * (5 * u - 3 * v) - theta + 1.2 * warpA)
        + 0.18 * Math.sin(tau * (7 * u + 6 * v) + 3 * theta + warpB)
        + 0.12 * Math.sin(tau * (-9 * u + 4 * v) - 2 * theta + warpA - warpB);
      const flicker = 0.08 * Math.sin(tau * (4 * u + 7 * v) + 4 * theta + 2 * warpB);
      const heat = Math.max(0, Math.min(1, (n + flicker + 1.1) / 2.6)) ** 1.35;
      emberColor(heat, data, (y * size + x) * 4);
    }
  }
  return data;
}

function buildFrames(): boolean {
  if (flameFrames && emberFrames) return true;
  const width = FLAME_W * PIXEL_RATIO, height = FLAME_H * PIXEL_RATIO;
  const ctx = createContext(width, height);
  if (!ctx) return false;
  const flames: Partial<Record<FireConfidence, Frames>> = {};
  for (const confidence of CONFIDENCES) {
    const cache: Uint8ClampedArray[] = [];
    flames[confidence] = { width, height, frame: (index) => cache[index] ??= (() => {
      drawFlame(ctx, FLAME_PALETTES[confidence], index);
      return new Uint8ClampedArray(ctx.getImageData(0, 0, width, height).data);
    })() };
  }
  const size = PATTERN_SIZE * PIXEL_RATIO;
  const embers: Uint8ClampedArray[] = [];
  // About 4 ms per frame; the pattern is only drawn from z8, so most views never build it.
  emberFrames = { width: size, height: size, frame: (index) => embers[index] ??= renderEmberFrame(index, size) };
  flameFrames = flames;
  return true;
}

let motionOverride: boolean | null = null;
let motionStartedAt: number | null = null;
const now = () => typeof performance !== "undefined" ? performance.now() : Date.now();
/** The frame every fire image shows right now: animated while motion runs, otherwise still. */
export const currentFireFrame = (): number => motionStartedAt === null ? STILL_FRAME
  : (STILL_FRAME + Math.floor((now() - motionStartedAt) / FIRE_FRAME_MS)) % FIRE_FRAME_COUNT;

const premultiplied = new WeakMap<Uint8ClampedArray, Uint8Array>();
/** Premultiply a frame once; MapLibre would otherwise redo it in JS for every tile on every frame. */
const premultiply = (straight: Uint8ClampedArray): Uint8Array => {
  let out = premultiplied.get(straight);
  if (out) return out;
  out = new Uint8Array(straight.length);
  for (let index = 0; index < straight.length; index += 4) {
    const alpha = straight[index + 3];
    out[index] = Math.round(straight[index] * alpha / 255);
    out[index + 1] = Math.round(straight[index + 1] * alpha / 255);
    out[index + 2] = Math.round(straight[index + 2] * alpha / 255);
    out[index + 3] = alpha;
  }
  premultiplied.set(straight, out);
  return out;
};

const wrapped = new WeakMap<Uint8Array, Uint8Array>();
/**
 * A pattern frame with MapLibre's 1 px wrap border (bottom row above, top row
 * below, and so on). The atlas slot's border belongs to this image; without it
 * linear sampling shows a faint seam at every pattern repeat.
 */
const withWrapBorder = (pixels: Uint8Array, width: number, height: number): Uint8Array => {
  let out = wrapped.get(pixels);
  if (out) return out;
  const outWidth = width + 2;
  out = new Uint8Array(outWidth * (height + 2) * 4);
  for (let row = -1; row <= height; row++) {
    const source = (row + height) % height;
    for (let column = -1; column <= width; column++) {
      const from = (source * width + (column + width) % width) * 4, to = ((row + 1) * outWidth + column + 1) * 4;
      out[to] = pixels[from]; out[to + 1] = pixels[from + 1]; out[to + 2] = pixels[from + 2]; out[to + 3] = pixels[from + 3];
    }
  }
  wrapped.set(pixels, out);
  return out;
};

/**
 * Animated style image. Frames are uploaded straight into each icon atlas
 * slot as premultiplied pixels (MapLibre's WebGL image path), so an animation
 * step costs one texSubImage2D per atlas rather than a per-pixel JS pass.
 */
class FireImage implements StyleImageInterface {
  width: number; height: number; data: StyleImageWebGLData;
  private shown: number;
  constructor(private readonly source: Frames, pattern = false) {
    this.width = source.width; this.height = source.height;
    this.shown = currentFireFrame();
    this.data = { renderWithWebGL: ({ gl, texture, x, y, width, height }) => {
      gl.bindTexture(gl.TEXTURE_2D, texture);
      const pixels = premultiply(this.source.frame(this.shown));
      if (pattern) gl.texSubImage2D(gl.TEXTURE_2D, 0, x - 1, y - 1, width + 2, height + 2, gl.RGBA, gl.UNSIGNED_BYTE, withWrapBorder(pixels, width, height));
      else gl.texSubImage2D(gl.TEXTURE_2D, 0, x, y, width, height, gl.RGBA, gl.UNSIGNED_BYTE, pixels);
    } };
  }
  render(): boolean {
    const frame = currentFireFrame();
    if (frame === this.shown) return false;
    this.shown = frame;
    return true;
  }
}

function ensureFireImages(map: MapLibreMap) {
  if (typeof map.addImage !== "function" || typeof map.hasImage !== "function" || !buildFrames()) return;
  for (const confidence of CONFIDENCES) {
    const id = flameImageId(confidence);
    if (!map.hasImage(id)) map.addImage(id, new FireImage(flameFrames![confidence]!), { pixelRatio: PIXEL_RATIO });
  }
  if (!map.hasImage(FIRE_EMBER_PATTERN_ID)) map.addImage(FIRE_EMBER_PATTERN_ID, new FireImage(emberFrames!, true), { pixelRatio: PIXEL_RATIO });
}

// ---------------------------------------------------------------------------
// Motion pacing
// ---------------------------------------------------------------------------

type Animator = { visible: boolean; bounds: [number, number, number, number] | null; timer: ReturnType<typeof setTimeout> | null; renderedAt: number };
const animators = new Map<MapLibreMap, Animator>();
let listenersInstalled = false;

const reducedMotionQuery = () => typeof window !== "undefined" && typeof window.matchMedia === "function" ? window.matchMedia("(prefers-reduced-motion: reduce)") : null;

/**
 * The page's own gate (reduced motion, Ambient motion, Battery saver) is
 * authoritative when it calls setFireDetectionMotion. Until then this module
 * applies the same rules it can observe: tab visibility, the reduced-motion
 * preference, the Battery-saver render budget and a `motion=off` view link.
 */
export function fireMotionAllowed(): boolean {
  if (typeof document === "undefined" || document.hidden) return false;
  if (reducedMotionQuery()?.matches) return false;
  if (motionOverride !== null) return motionOverride;
  try { if (new URLSearchParams(window.location.search).get("motion") === "off") return false; } catch { /* no location */ }
  return !browserRenderBudget().efficient;
}

/** Page-level hook: pass the same `motionAllowed` used for the curtain shimmer and water flow. */
export function setFireDetectionMotion(allowed: boolean): void {
  motionOverride = allowed;
  for (const map of animators.keys()) syncFireAnimation(map);
}

function installListeners() {
  if (listenersInstalled || typeof document === "undefined") return;
  listenersInstalled = true;
  const resync = () => { for (const map of animators.keys()) syncFireAnimation(map); };
  document.addEventListener("visibilitychange", resync);
  reducedMotionQuery()?.addEventListener?.("change", resync);
}

const inView = (map: MapLibreMap, bounds: Animator["bounds"]) => {
  if (!bounds) return true;
  try {
    const view = map.getBounds();
    return !(bounds[0] > view.getEast() || bounds[2] < view.getWest() || bounds[1] > view.getNorth() || bounds[3] < view.getSouth());
  } catch { return true; }
};

// One ticker per map, shared by independently toggled incident and detection layers.
const fireDisplays = new WeakMap<MapLibreMap, Map<string, { visible: boolean; bounds: Animator["bounds"] }>>();
function syncFireDisplayMotion(map: MapLibreMap, source: string, visible: boolean, bounds: Animator["bounds"]) {
  let displays = fireDisplays.get(map);
  if (!displays) { displays = new Map(); fireDisplays.set(map, displays); }
  displays.set(source, { visible, bounds });
  const active = [...displays.values()].filter(display => display.visible);
  const extents = active.flatMap(display => display.bounds ? [display.bounds] : []);
  const union: Animator["bounds"] = extents.length ? [Math.min(...extents.map(b => b[0])), Math.min(...extents.map(b => b[1])), Math.max(...extents.map(b => b[2])), Math.max(...extents.map(b => b[3]))] : null;
  syncFireAnimation(map, { visible: active.length > 0, bounds: union });
}

function syncFireAnimation(map: MapLibreMap, update?: Partial<Pick<Animator, "visible" | "bounds">>) {
  let animator = animators.get(map);
  if (!animator) {
    if (!update?.visible) return;
    if (typeof map.triggerRepaint !== "function") return;
    const entry: Animator = animator = { visible: false, bounds: null, timer: null, renderedAt: 0 };
    animators.set(map, entry);
    installListeners();
    // Another loop (curtain shimmer, water flow, camera motion) already
    // repainting advances the fire frames too; the ticker only fills gaps.
    const rendered = () => { entry.renderedAt = now(); };
    map.on?.("render", rendered);
    map.once?.("remove", () => { if (entry.timer) clearTimeout(entry.timer); map.off?.("render", rendered); animators.delete(map); });
  }
  if (update) Object.assign(animator, update);
  const run = animator.visible && fireMotionAllowed();
  if (run && !animator.timer) {
    motionStartedAt ??= now();
    const tick = () => {
      const entry = animators.get(map);
      if (!entry) return;
      if (!entry.visible || !fireMotionAllowed()) { entry.timer = null; settle(); return; }
      try { if (now() - entry.renderedAt >= FIRE_FRAME_MS - 10 && inView(map, entry.bounds)) map.triggerRepaint(); } catch { /* style swap in progress */ }
      entry.timer = setTimeout(tick, FIRE_CHECK_MS);
    };
    animator.timer = setTimeout(tick, FIRE_CHECK_MS);
  } else if (!run && animator.timer) {
    clearTimeout(animator.timer);
    animator.timer = null;
  }
  if (!run) settle();
}

/** With no map animating, hold every image on the still frame. */
function settle() {
  if ([...animators.values()].some((entry) => entry.timer)) return;
  if (motionStartedAt === null) return;
  motionStartedAt = null;
  for (const map of animators.keys()) try { map.triggerRepaint(); } catch { /* style swap in progress */ }
}
