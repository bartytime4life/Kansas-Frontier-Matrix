import type { DownstreamPath } from "./water-flow-context";

export type Coordinate = readonly [number, number];
export type WaterReach = DownstreamPath & { sequence: number | null; upstream?: number | null; downstream: number | null; levelpath: number | null; name: string | null; featureType?: number };
export type TerrainSample = { distanceM: number; coordinate: Coordinate; elevationM: number | null; datum: string | null; resolutionM: number | null };
export type WaterPathAnalysis = {
  upstreamM?: number; downstreamM?: number; upstreamStop?: string; downstreamStop?: string;
  lengthM: number; gaugeOffsetM: number; segments: number; connectors: number; name: string | null; stopReason: string;
  elevation: { state: "ready" | "partial" | "unavailable"; samples: TerrainSample[]; dropM: number | null; slopePercent: number | null; source: string; retrievedAt: string | null; notice: string };
};
export const ELEVATION_SOURCE = "https://elevation.nationalmap.gov/arcgis/rest/services/3DEPElevation/ImageServer/getSamples";
export const MAX_WATER_PATH_M = 40_000;
export const MAX_WATER_VERTICES = 5_000;
const radians = Math.PI / 180;
export function waterDistance(a: Coordinate, b: Coordinate) {
  const h = Math.sin((b[1] - a[1]) * radians / 2) ** 2 + Math.cos(a[1] * radians) * Math.cos(b[1] * radians) * Math.sin((b[0] - a[0]) * radians / 2) ** 2;
  return 6371008.8 * 2 * Math.asin(Math.sqrt(Math.min(1, h)));
}
export function waterPathLength(points: readonly Coordinate[]) {
  return points.slice(1).reduce((sum, p, i) => sum + waterDistance(points[i], p), 0);
}
const validCoordinate = (p: unknown): p is Coordinate => Array.isArray(p) && p.length === 2 && p.every(v => typeof v === "number" && Number.isFinite(v)) && p[0] >= -102.2 && p[0] <= -94.4 && p[1] >= 36.8 && p[1] <= 40.2;
const sequence = (v: unknown) => typeof v === "number" && Number.isSafeInteger(v) && v > 0 ? v : null;

export function parseWaterReaches(raw: unknown): WaterReach[] {
  const data = raw as { features?: unknown[]; error?: unknown } | null;
  if (!data || data.error || !Array.isArray(data.features) || data.features.length > 400) throw new Error("Invalid USGS flowline response.");
  let vertices = 0;
  const ids = new Set<string>();
  return data.features.flatMap(feature => {
    const f = feature as { properties?: Record<string, unknown>; geometry?: { type?: string; coordinates?: unknown[] } };
    const p = f?.properties, g = f?.geometry;
    if (p?.flowdirection !== 1 || ![1, 4, 5, 6].includes(p.featuretype as number) || g?.type !== "LineString" || !Array.isArray(g.coordinates)) return [];
    if (typeof p.id3dhp !== "string" || !/^[A-Za-z0-9]{1,16}$/.test(p.id3dhp) || ids.has(p.id3dhp)) throw new Error("Ambiguous USGS reach identity.");
    if (g.coordinates.length < 2 || g.coordinates.length > 10000 || !g.coordinates.every(validCoordinate)) return [];
    vertices += g.coordinates.length; if (vertices > 80000) throw new Error("USGS flowline geometry limit exceeded.");
    ids.add(p.id3dhp);
    return [{ id: p.id3dhp, coordinates: g.coordinates as Coordinate[], featureType: p.featuretype as number, sequence: sequence(p.hydrosequence), upstream: sequence(p.uphydrosequence), downstream: sequence(p.dnhydrosequence), levelpath: sequence(p.levelpath), name: typeof p.gnisidlabel === "string" ? p.gnisidlabel.slice(0, 160) : null }];
  });
}

/** Snap only to a mapped line, never draw an invented gauge-to-river connector. */
export function nearestWaterReach(reaches: readonly WaterReach[], gauge: Coordinate) {
  let best: { reach: WaterReach; offsetM: number; head: Coordinate[]; tail: Coordinate[] } | null = null;
  const scale = Math.cos(gauge[1] * radians);
  for (const reach of reaches) for (let i = 1; i < reach.coordinates.length; i++) {
    const a = reach.coordinates[i - 1], b = reach.coordinates[i];
    const dx = (b[0] - a[0]) * scale, dy = b[1] - a[1];
    const denom = dx * dx + dy * dy;
    if (!denom) continue;
    const t = Math.max(0, Math.min(1, (((gauge[0] - a[0]) * scale * dx) + (gauge[1] - a[1]) * dy) / denom));
    const point: Coordinate = [a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1])];
    const offsetM = waterDistance(point, gauge);
    if (offsetM <= 1200 && (!best || offsetM < best.offsetM)) best = { reach, offsetM, head: [...reach.coordinates.slice(0, i), point], tail: [point, ...reach.coordinates.slice(i)] };
  }
  return best;
}

export function traceWaterPath(seed: NonNullable<ReturnType<typeof nearestWaterReach>>, reaches: readonly WaterReach[], maxDistance = MAX_WATER_PATH_M, maxReaches = 80) {
  const bySequence = new Map<number, WaterReach[]>();
  for (const reach of reaches) if (reach.sequence !== null) bySequence.set(reach.sequence, [...(bySequence.get(reach.sequence) ?? []), reach]);
  const points: Coordinate[] = [seed.tail[0]], visited = new Set<string>();
  let current = seed.reach, tail = seed.tail.slice(1), lengthM = 0, segments = 0, connectors = 0, stopReason = "End of returned downstream connections.";
  while (segments < maxReaches) {
    visited.add(current.id); segments++; if (current.featureType && current.featureType !== 1) connectors++;
    for (const point of tail) {
      const last = points.at(-1)!, distance = waterDistance(last, point);
      if (distance < 0.01) continue;
      if (points.length >= MAX_WATER_VERTICES) { stopReason = "Path vertex limit reached."; return finish(); }
      if (lengthM + distance >= maxDistance) {
        const fraction = (maxDistance - lengthM) / distance;
        points.push([last[0] + fraction * (point[0] - last[0]), last[1] + fraction * (point[1] - last[1])]);
        lengthM = maxDistance; stopReason = `${maxDistance / 1000} km exploration limit reached.`; return finish();
      }
      points.push(point); lengthM += distance;
    }
    if (!current.downstream) { stopReason = "No downstream network identifier supplied."; break; }
    const choices = bySequence.get(current.downstream) ?? [];
    if (choices.length !== 1) { stopReason = choices.length ? "Ambiguous downstream connection; path stopped." : "Downstream connection lies outside the returned river data."; break; }
    const next = choices[0];
    if (visited.has(next.id)) { stopReason = "Repeated downstream connection; path stopped."; break; }
    if (waterDistance(points.at(-1)!, next.coordinates[0]) > 10) { stopReason = "Mapped endpoints do not meet; path stopped at the gap."; break; }
    current = next; tail = [...next.coordinates];
    if (segments === maxReaches) stopReason = `${maxReaches}-reach exploration limit reached.`;
  }
  return finish();
  function finish() {
    return { path: { id: seed.reach.id, coordinates: points, hasConnectors: connectors > 0 } satisfies DownstreamPath, lengthM, segments, connectors, gaugeOffsetM: seed.offsetM, name: seed.reach.name, stopReason };
  }
}

/** Follow the supplied mainstem upstream, then restore downstream drawing order. */
export function traceWaterCorridor(seed: NonNullable<ReturnType<typeof nearestWaterReach>>, reaches: readonly WaterReach[]) {
  const reversed = reaches.map(reach => {
    const incoming = reach.sequence === null ? [] : reaches.filter(candidate => candidate.downstream === reach.sequence && candidate.sequence !== null);
    // Explicit mainstem wins only when reciprocal topology agrees. Without it,
    // multiple tributaries remain ambiguous; never choose by slope or proximity.
    const chosen = reach.upstream ? incoming.filter(candidate => candidate.sequence === reach.upstream) : incoming;
    return { ...reach, coordinates: [...reach.coordinates].reverse(), downstream: chosen.length === 1 ? chosen[0].sequence : null };
  });
  const reverseSeed = reversed.find(reach => reach.id === seed.reach.id)!;
  const up = traceWaterPath({ ...seed, reach: reverseSeed, tail: [...seed.head].reverse() }, reversed, 100_000, 200);
  const down = traceWaterPath(seed, reaches, 100_000, 200);
  const upstreamStop = up.stopReason.replaceAll("downstream", "upstream").replace("No upstream network identifier supplied.", "No unique reciprocal upstream connection in returned data (missing, inconsistent or ambiguous).");
  return { ...down,
    path: { ...down.path, coordinates: [...up.path.coordinates].reverse().concat(down.path.coordinates.slice(1)), hasConnectors: up.path.hasConnectors || down.path.hasConnectors },
    lengthM: up.lengthM + down.lengthM, upstreamM: up.lengthM, downstreamM: down.lengthM,
    upstreamStop, downstreamStop: down.stopReason,
    segments: up.segments + down.segments - 1,
    connectors: up.connectors + down.connectors - (seed.reach.featureType && seed.reach.featureType !== 1 ? 1 : 0),
    stopReason: `Upstream: ${upstreamStop} Downstream: ${down.stopReason}`,
  };
}

export function sampleWaterPath(points: readonly Coordinate[], count = 25): TerrainSample[] {
  const total = waterPathLength(points), samples: TerrainSample[] = [];
  let segment = 1, consumed = 0;
  for (let i = 0; i < count; i++) {
    const distanceM = total * i / (count - 1);
    while (segment < points.length - 1 && consumed + waterDistance(points[segment - 1], points[segment]) < distanceM) {
      consumed += waterDistance(points[segment - 1], points[segment]); segment++;
    }
    const a = points[segment - 1], b = points[segment], length = waterDistance(a, b);
    const f = length ? Math.max(0, Math.min(1, (distanceM - consumed) / length)) : 0;
    samples.push({ distanceM, coordinate: [a[0] + f * (b[0] - a[0]), a[1] + f * (b[1] - a[1])], elevationM: null, datum: null, resolutionM: null });
  }
  return samples;
}

export function parseWaterElevations(raw: unknown, requested: TerrainSample[]): WaterPathAnalysis["elevation"] {
  const data = raw as { samples?: Record<string, unknown>[]; error?: unknown } | null;
  if (!data || data.error || !Array.isArray(data.samples) || data.samples.length > requested.length) throw new Error("Elevation samples unavailable.");
  const samples = requested.map(p => ({ ...p })), seen = new Set<number>();
  for (const item of data.samples) {
    const index = item.locationId;
    if (typeof index !== "number" || !Number.isInteger(index) || index < 0 || index >= samples.length || seen.has(index)) throw new Error("Elevation sample identity is invalid.");
    seen.add(index);
    const location = item.location as { x?: unknown; y?: unknown; spatialReference?: { wkid?: number; latestWkid?: number } };
    if (!location || typeof location.x !== "number" || typeof location.y !== "number" || (location.spatialReference?.latestWkid ?? location.spatialReference?.wkid) !== 4326
      || !Number.isFinite(location.x) || !Number.isFinite(location.y) || waterDistance(samples[index].coordinate, [location.x, location.y]) > 2) throw new Error("Elevation sample location is invalid.");
    const value = typeof item.value === "string" && item.value.trim() !== "" ? Number(item.value) : typeof item.value === "number" ? item.value : NaN;
    if (!Number.isFinite(value) || value < -100 || value > 2000) continue;
    const attributes = item.attributes as Record<string, unknown> | undefined;
    samples[index].elevationM = value;
    samples[index].datum = typeof attributes?.VerticalDatum === "string" && attributes.VerticalDatum.trim() && !/unknown|unspecified|not available|^none$|^null$/i.test(attributes.VerticalDatum) ? attributes.VerticalDatum.slice(0, 180) : null;
    samples[index].resolutionM = typeof item.resolution === "number" && Number.isFinite(item.resolution) && item.resolution > 0 ? item.resolution : null;
  }
  const first = samples[0], last = samples.at(-1)!, count = samples.filter(s => s.elevationM !== null).length;
  const compatible = first.datum !== null && first.datum === last.datum;
  const dropM = compatible && first.elevationM !== null && last.elevationM !== null ? first.elevationM - last.elevationM : null;
  return { state: count === samples.length ? "ready" : count ? "partial" : "unavailable", samples, dropM, slopePercent: dropM !== null && last.distanceM > 0 ? dropM / last.distanceM * 100 : null,
    source: ELEVATION_SOURCE, retrievedAt: new Date().toISOString(), notice: "USGS 3DEP sampled terrain in meters, not river depth or water-surface elevation. Endpoint drop and mean slope require matching reported vertical datums. Terrain artifacts, dams and mixed source vintages can produce local rises; provider flow direction is retained." };
}
