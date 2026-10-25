/**
 * The same aviation data as a 2D chart: sectional-style ceiling/floor labels
 * and an altitude slice that keeps only what exists at one height. Heights are
 * recovered from each feature's drawn base/top (feet above its ground
 * reference) plus that ground, so 2D and 3D never disagree about a volume.
 */
// Standalone on purpose (no imports), like the other aviation model modules.
const FEET_TO_METERS = 0.3048;

export type AviationView = "3d" | "2d";
export type AltitudeSlice = Readonly<{ kind: "all" }> | Readonly<{ kind: "drone" }> | Readonly<{ kind: "msl"; ft: number }>;
export const ALL_ALTITUDES: AltitudeSlice = Object.freeze({ kind: "all" });
// Kansas ground is ~700–4,000 ft MSL, so slices start just above it and reach the airway structure.
export const SLICE_MSL_FEET: readonly number[] = Object.freeze([1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 6000, 7000, 8000, 10000, 12000, 14500, 18000, 25000]);
// Point reports (aircraft, PIREPs) are kept within this band of a slice; volumes must contain it.
export const SLICE_POINT_TOLERANCE_FT = 1000;
const DRONE_CEILING_FT = 400;

const firstPosition = (geometry: GeoJSON.Geometry): [number, number] | null => {
  const walk = (value: unknown): [number, number] | null => Array.isArray(value)
    ? typeof value[0] === "number" && typeof value[1] === "number" ? [value[0], value[1]] : walk(value[0]) : null;
  return "coordinates" in geometry ? walk(geometry.coordinates) : null;
};

/** A feature's vertical span: feet above its ground and feet MSL. Null when it carries no drawn heights. */
export function featureSpan(feature: GeoJSON.Feature, exaggeration: number, groundAt: (lon: number, lat: number) => number):
  Readonly<{ lowAgl: number; highAgl: number; lowMsl: number; highMsl: number }> | null {
  const properties = feature.properties ?? {};
  const base = Number(properties.base), top = Number(properties.top), scale = FEET_TO_METERS * exaggeration;
  if (!Number.isFinite(base) || !Number.isFinite(top) || !(scale > 0)) return null;
  const at = firstPosition(feature.geometry);
  const ground = Number.isFinite(Number(properties.groundFt)) ? Number(properties.groundFt) : at ? groundAt(at[0], at[1]) : 0;
  const lowAgl = base / scale, highAgl = top / scale;
  return Object.freeze({ lowAgl, highAgl, lowMsl: ground + lowAgl, highMsl: ground + highAgl });
}

/**
 * Keep only features present in the slice. Volumes must contain the slice
 * altitude; `toleranceFt` widens that for point reports drawn as thin markers.
 * The drone slice keeps anything that starts below 400 ft above its ground.
 */
export function sliceCollection(collection: GeoJSON.FeatureCollection, slice: AltitudeSlice, exaggeration: number,
  groundAt: (lon: number, lat: number) => number, toleranceFt = 0): GeoJSON.FeatureCollection {
  if (slice.kind === "all") return collection;
  return { type: "FeatureCollection", features: collection.features.filter(feature => {
    const span = featureSpan(feature, exaggeration, groundAt);
    if (!span) return false;
    if (slice.kind === "drone") return span.lowAgl < DRONE_CEILING_FT;
    return span.lowMsl - toleranceFt <= slice.ft && slice.ft < span.highMsl + toleranceFt;
  }) };
}

export const sliceTitle = (slice: AltitudeSlice): string => slice.kind === "all" ? "All altitudes"
  : slice.kind === "drone" ? "Drone altitudes (SFC–400 ft AGL)" : `${slice.ft.toLocaleString("en-US")} ft MSL`;
