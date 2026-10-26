import type { Feature, FeatureCollection, Polygon } from "geojson";
import type { ExpressionSpecification, GeoJSONSource, LayerSpecification, Map as MapLibreMap } from "./maplibre-seam";
import { updateGeoJSON, rememberGeoJSON, setVisibleIfChanged, uploadedGeoJSON } from "./map-performance";
import { globeOverviewPaintSize } from "./globe-context";
import { FIRE_CONFIDENCE_COLORS, FIRE_REPORT_COLORS, FIRE_REPORT_OTHER_COLOR } from "./map-keys";

/**
 * Display for NASA GIBS NOAA-20 VIIRS thermal detections and NIFC incident
 * reports, as static scientific markers:
 *
 * - A detection is a dot at its pixel centre, coloured by the provider's
 *   detection confidence, at a fixed screen size. Close in, a dashed outline
 *   shows the provider scan × track pixel on the ground, approximately oriented
 *   to the satellite pass: the area the detection covers, not a fire perimeter,
 *   flame front or burned area.
 * - A reported incident is a ring at its reported location, coloured by
 *   incident type, so it never reads as a detection.
 *
 * Nothing is animated and marker size encodes nothing. The selectable records
 * stay on the provider point sources; the footprints are a display-only
 * derivative on a site-local source, so hover and inspection still resolve
 * through the original `-halo`/`-circle` layer ids.
 */

export const FIRE_POINT_LAYER_IDS = Object.freeze({
  halo: "external-nasa-gibs-fire-points-halo",
  circle: "external-nasa-gibs-fire-points-circle",
  shimmer: "external-nasa-gibs-fire-points-footprint-shimmer",
  edge: "external-nasa-gibs-fire-points-footprint-edge",
});
export const FIRE_POINT_SOURCE_ID = "external-nasa-gibs-fire-points";
/** Site-local (kfm-) so the click/hover fallback never treats a derived
 * rectangle as a separate provider record. */
export const FIRE_FOOTPRINT_SOURCE_ID = "kfm-nasa-gibs-fire-footprints";

export type FireConfidence = "high" | "nominal" | "low";
const CONFIDENCES: readonly FireConfidence[] = ["high", "nominal", "low"];
const confidenceColor: ExpressionSpecification = ["match", ["get", "confidence"], "high", FIRE_CONFIDENCE_COLORS.high, "low", FIRE_CONFIDENCE_COLORS.low, FIRE_CONFIDENCE_COLORS.nominal];
const reportColor: ExpressionSpecification = ["match", ["get", "incidentType"], ...FIRE_REPORT_COLORS.flat(), FIRE_REPORT_OTHER_COLOR] as unknown as ExpressionSpecification;

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
 * provider scan/track dimensions gets no rectangle; its marker stays instead.
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

/**
 * Hit target: covers the marker zoomed out and the whole footprint zoomed
 * in. Linear integer-zoom stops (starting at z4) keep the globe
 * overview scaling in live-context valid.
 */
export const FIRE_HIT_RADIUS: ExpressionSpecification = ["interpolate", ["linear"], ["zoom"],
  4, 11, 9, 13,
  ...[10, 11, 12, 13, 14, 15, 16, 17, 18].flatMap((zoom) => [zoom, ["max", 14, ["*", largestDimensionKm, 0.62 * 1000 * 2 ** zoom / KANSAS_METRES_PER_PIXEL_Z0]]]),
] as ExpressionSpecification;
/** Detection marker: a fixed screen size from the statewide view to the closest. */
export const FIRE_MARKER_RADIUS: ExpressionSpecification = ["interpolate", ["linear"], ["zoom"], 4, 3.5, 8, 4.5, 12, 5.5];
/** Report ring and its transparent hit target. */
const REPORT_RING_RADIUS: ExpressionSpecification = ["interpolate", ["linear"], ["zoom"], 4, 4.5, 10, 6.5];
const REPORT_HIT_RADIUS: ExpressionSpecification = ["interpolate", ["linear"], ["zoom"], 4, 10, 10, 14];
const edgeOpacity = (opacity: number): ExpressionSpecification => ["interpolate", ["linear"], ["zoom"], 10.5, 0, 12, opacity * 0.42, 15, opacity * 0.62];

const footprintLayers = (): LayerSpecification[] => [
  { id: FIRE_POINT_LAYER_IDS.shimmer, type: "line", source: FIRE_FOOTPRINT_SOURCE_ID, minzoom: 8.5,
    layout: { "line-join": "round" },
    // Neutral casing keeps the measurement footprint legible on light maps.
    // Dash lengths match the narrow pale line above (dash units × width).
    paint: { "line-color": "#253e46", "line-width": 2.6, "line-dasharray": [1.5, 2], "line-blur": 0, "line-opacity": 0 } },
  { id: FIRE_POINT_LAYER_IDS.edge, type: "line", source: FIRE_FOOTPRINT_SOURCE_ID, minzoom: 10,
    paint: { "line-color": "#fff1d1", "line-width": 1.3, "line-dasharray": [3, 4], "line-opacity": 0 } },
];

const setPaintExpression = (map: MapLibreMap, id: string, property: string, value: unknown) => {
  if (!map.getLayer(id)) return;
  const current = map.getPaintProperty(id, property as never);
  if (JSON.stringify(current) !== JSON.stringify(value)) map.setPaintProperty(id, property as never, value as never);
};
const sized = (map: MapLibreMap, radius: ExpressionSpecification) => map.getProjection?.()?.type === "globe" ? globeOverviewPaintSize(radius) : radius;

export const FIRE_REPORT_SOURCE_ID = "external-nifc-fire-reports";
/** Reports keep their own record ids: a transparent hit target and a ring coloured by incident type. */
export function syncFireReportDisplay(map: MapLibreMap, visible: boolean, opacity: number): void {
  const amount = Math.max(0, Math.min(1, opacity));
  const [halo, point] = [FIRE_REPORT_SOURCE_ID + "-halo", FIRE_REPORT_SOURCE_ID + "-point"];
  for (const id of [halo, point]) if (map.getLayer(id)) setVisibleIfChanged(map, id, visible);
  setPaintExpression(map, halo, "circle-radius", sized(map, REPORT_HIT_RADIUS));
  setPaintExpression(map, halo, "circle-opacity", 0);
  setPaintExpression(map, halo, "circle-stroke-opacity", 0);
  setPaintExpression(map, point, "circle-radius", sized(map, REPORT_RING_RADIUS));
  setPaintExpression(map, point, "circle-color", "#11161b");
  setPaintExpression(map, point, "circle-opacity", amount * 0.85);
  setPaintExpression(map, point, "circle-stroke-color", reportColor);
  setPaintExpression(map, point, "circle-stroke-width", 2.5);
  setPaintExpression(map, point, "circle-stroke-opacity", amount);
}

/**
 * Add the derived footprint source and layers, refresh the derived
 * rectangles, and apply visibility and opacity to every detection layer.
 * Called from applyOfficialContextState after the provider point source and
 * its `-halo`/`-circle` layers exist.
 */
export function syncFireDetectionDisplay(map: MapLibreMap, visible: boolean, opacity: number): void {
  refreshFireFootprints(map);
  if (map.getSource(FIRE_FOOTPRINT_SOURCE_ID)) for (const layer of footprintLayers()) if (!map.getLayer(layer.id)) map.addLayer(layer);
  const amount = Math.max(0, Math.min(1, opacity));
  for (const id of Object.values(FIRE_POINT_LAYER_IDS)) if (map.getLayer(id)) setVisibleIfChanged(map, id, visible);
  // The halo is the transparent hit target: the marker zoomed out, the whole footprint zoomed in.
  setPaintExpression(map, FIRE_POINT_LAYER_IDS.halo, "circle-radius", sized(map, FIRE_HIT_RADIUS));
  setPaintExpression(map, FIRE_POINT_LAYER_IDS.halo, "circle-opacity", 0);
  setPaintExpression(map, FIRE_POINT_LAYER_IDS.halo, "circle-stroke-opacity", 0);
  setPaintExpression(map, FIRE_POINT_LAYER_IDS.circle, "circle-radius", sized(map, FIRE_MARKER_RADIUS));
  setPaintExpression(map, FIRE_POINT_LAYER_IDS.circle, "circle-color", confidenceColor);
  setPaintExpression(map, FIRE_POINT_LAYER_IDS.circle, "circle-opacity", amount);
  setPaintExpression(map, FIRE_POINT_LAYER_IDS.circle, "circle-stroke-color", "#1a1310");
  setPaintExpression(map, FIRE_POINT_LAYER_IDS.circle, "circle-stroke-width", 1);
  setPaintExpression(map, FIRE_POINT_LAYER_IDS.circle, "circle-stroke-opacity", amount);
  setPaintExpression(map, FIRE_POINT_LAYER_IDS.shimmer, "line-opacity", edgeOpacity(amount));
  setPaintExpression(map, FIRE_POINT_LAYER_IDS.edge, "line-opacity", edgeOpacity(amount));
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
  return footprints;
}
