/**
 * A side view (vertical cross-section) along a line between two picked points:
 * which airspace volumes and TFRs the line passes through, over what distance,
 * and between which altitudes (feet MSL) above the ground at each sample. The
 * same limits the 3D and 2D views draw, laid out as distance against altitude.
 * Standalone on purpose (no imports), like the other aviation model modules.
 */
export type ProfilePoint = Readonly<{ lon: number; lat: number; distanceNm: number; groundFt: number }>;
export type ProfileVolume = Readonly<{
  key: string; label: string; color: string; kind: "airspace" | "tfr";
  bbox: readonly [number, number, number, number]; rings: readonly (readonly (readonly [number, number])[])[];
  /** Floor and ceiling in feet MSL over a given ground elevation. */
  lowFt: (groundFt: number) => number; highFt: (groundFt: number) => number;
}>;
export type ProfileSegment = Readonly<{ from: number; to: number; low: readonly number[]; high: readonly number[] }>;
export type ProfileBand = Readonly<{ key: string; label: string; color: string; kind: ProfileVolume["kind"]; segments: readonly ProfileSegment[] }>;

export const PROFILE_SAMPLES = 241;
export const PROFILE_MAX_NM = 320;
export const PROFILE_TOP_FT = 20000;
export const PROFILE_TRAFFIC_KM = 5;
const KM_PER_NM = 1.852;

const distanceKm = (lon1: number, lat1: number, lon2: number, lat2: number) => {
  const toRad = Math.PI / 180, p1 = lat1 * toRad, p2 = lat2 * toRad;
  const a = Math.sin((p2 - p1) / 2) ** 2 + Math.cos(p1) * Math.cos(p2) * Math.sin((lon2 - lon1) * toRad / 2) ** 2;
  return 6371.0088 * 2 * Math.asin(Math.min(1, Math.sqrt(a)));
};

/** Evenly spaced points from A to B (straight in lon/lat; under 0.1% off a great circle at this length and latitude). */
export function profilePath(a: Readonly<{ lon: number; lat: number }>, b: Readonly<{ lon: number; lat: number }>, samples = PROFILE_SAMPLES):
  readonly Readonly<{ lon: number; lat: number; distanceNm: number }>[] {
  const totalNm = distanceKm(a.lon, a.lat, b.lon, b.lat) / KM_PER_NM;
  if (!(totalNm > 0) || totalNm > PROFILE_MAX_NM) throw new Error("The side view needs two distinct points within 320 NM.");
  return Object.freeze(Array.from({ length: samples }, (_, index) => {
    const t = index / (samples - 1);
    return Object.freeze({ lon: a.lon + (b.lon - a.lon) * t, lat: a.lat + (b.lat - a.lat) * t, distanceNm: totalNm * t });
  }));
}

const insideRings = (lon: number, lat: number, rings: ProfileVolume["rings"]) => {
  let inside = false;
  for (const ring of rings) {
    for (let i = 0, j = ring.length - 1; i < ring.length; j = i++) {
      const [xi, yi] = ring[i], [xj, yj] = ring[j];
      if ((yi > lat) !== (yj > lat) && lon < (xj - xi) * (lat - yi) / (yj - yi) + xi) inside = !inside;
    }
  }
  return inside;
};

/** Each volume the line passes through, as runs of consecutive samples with the floor and ceiling at every sample. */
export function profileBands(points: readonly ProfilePoint[], volumes: readonly ProfileVolume[]): readonly ProfileBand[] {
  const lons = points.map(point => point.lon), lats = points.map(point => point.lat);
  const box = [Math.min(...lons), Math.min(...lats), Math.max(...lons), Math.max(...lats)];
  const bands: ProfileBand[] = [];
  for (const volume of volumes) {
    if (volume.bbox[2] < box[0] || volume.bbox[0] > box[2] || volume.bbox[3] < box[1] || volume.bbox[1] > box[3]) continue;
    const segments: ProfileSegment[] = [];
    let from = -1;
    const close = (to: number) => {
      const span = points.slice(from, to + 1);
      const low = span.map(point => Math.max(point.groundFt, volume.lowFt(point.groundFt)));
      const high = span.map((point, index) => Math.max(low[index], volume.highFt(point.groundFt)));
      segments.push(Object.freeze({ from, to, low: Object.freeze(low), high: Object.freeze(high) }));
      from = -1;
    };
    points.forEach((point, index) => {
      const inside = point.lon >= volume.bbox[0] && point.lon <= volume.bbox[2] && point.lat >= volume.bbox[1] && point.lat <= volume.bbox[3] && insideRings(point.lon, point.lat, volume.rings);
      if (inside && from < 0) from = index;
      if (!inside && from >= 0) close(index - 1);
    });
    if (from >= 0) close(points.length - 1);
    if (segments.length) bands.push(Object.freeze({ key: volume.key, label: volume.label, color: volume.color, kind: volume.kind, segments: Object.freeze(segments) }));
  }
  // Lower volumes first, so the chart and the text list read bottom-up like the airspace column.
  return Object.freeze(bands.sort((left, right) => Math.min(...left.segments.flatMap(segment => segment.low)) - Math.min(...right.segments.flatMap(segment => segment.low))
    || left.label.localeCompare(right.label)));
}

/** Along-track distance (NM) of a position within `maxKm` of the A–B line, or null; local equirectangular projection. */
export function alongTrackNm(a: Readonly<{ lon: number; lat: number }>, b: Readonly<{ lon: number; lat: number }>, lon: number, lat: number, maxKm = PROFILE_TRAFFIC_KM): number | null {
  const kx = 111.32 * Math.cos(((a.lat + b.lat) / 2) * Math.PI / 180), ky = 110.57;
  const bx = (b.lon - a.lon) * kx, by = (b.lat - a.lat) * ky, px = (lon - a.lon) * kx, py = (lat - a.lat) * ky;
  const length = Math.hypot(bx, by);
  if (!(length > 0)) return null;
  const along = (px * bx + py * by) / length, across = Math.abs(px * by - py * bx) / length;
  return along < 0 || along > length || across > maxKm ? null : along / KM_PER_NM;
}

/** One readable line per band run: "CLASS C · ICT · 2,700 MSL–5,300 MSL, 4.9 to 9.8 NM". */
export function profileSummary(points: readonly ProfilePoint[], bands: readonly ProfileBand[]): readonly string[] {
  const nm = (value: number) => value.toFixed(1);
  return Object.freeze(bands.flatMap(band => band.segments.map(segment =>
    `${band.label}, ${nm(points[segment.from].distanceNm)} to ${nm(points[segment.to].distanceNm)} NM`)));
}
