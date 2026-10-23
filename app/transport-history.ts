/** Browser-local construction study. Source assertions remain unverified input;
 * this module cannot admit, publish or turn a study into KFM evidence. */
export type RoutePoint = readonly [number, number];
export type ProgressSample = Readonly<{ date: string; chainageM: number; sourceUrl: string }>;
export type TransportMilestone = Readonly<{ date: string; kind: "planned" | "activity-reported" | "completion-reported"; title: string; sourceUrl: string }>;
export type TransportWork = Readonly<{
  id: string; title: string; mode: "road" | "rail"; action: "build" | "reconstruct" | "remove";
  coordinates: readonly RoutePoint[]; widthM: number; positionAccuracyM: number;
  start: string; end: string; closedFrom?: string; reopenedAt?: string;
  progress: readonly ProgressSample[]; interpolate: boolean;
  progressMode?: "front" | "milestones"; milestones?: readonly TransportMilestone[];
  sourceUrl: string; geometrySourceUrl: string; limitation: string; synthetic: boolean;
}>;
export const TRANSPORT_STUDY_MAX_BYTES = 2_000_000;
export const TRANSPORT_STUDY_MAX_ROUTES = 12;
const DAY = 86_400_000;
export function transportDay(value: unknown): number | null {
  if (typeof value !== "string" || !/^\d{4}-\d{2}-\d{2}$/.test(value)) return null;
  const n = Date.parse(`${value}T00:00:00Z`);
  return Number.isFinite(n) && new Date(n).toISOString().slice(0, 10) === value ? n : null;
}
const url = (value: unknown) => {
  if (typeof value !== "string" || value.length > 800) return false;
  try { const u = new URL(value); return u.protocol === "https:" && !u.username && !u.password; } catch { return false; }
};
export const routeDistanceM = (a: RoutePoint, b: RoutePoint): number => {
  const r = Math.PI / 180;
  const h = Math.sin((b[1] - a[1]) * r / 2) ** 2 + Math.cos(a[1] * r) * Math.cos(b[1] * r) * Math.sin((b[0] - a[0]) * r / 2) ** 2;
  return 12_742_000 * Math.asin(Math.min(1, Math.sqrt(h)));
};
export const routeLengthM = (coordinates: readonly RoutePoint[]): number => coordinates.slice(1).reduce((sum, p, i) => sum + routeDistanceM(coordinates[i], p), 0);
export function routePose(coordinates: readonly RoutePoint[], chainageM: number): { coordinate: RoutePoint; heading: number } {
  let remaining = Math.max(0, chainageM);
  for (let i = 1; i < coordinates.length; i++) {
    const a = coordinates[i - 1], b = coordinates[i], length = routeDistanceM(a, b);
    if (remaining <= length || i === coordinates.length - 1) {
      const f = length ? Math.min(1, remaining / length) : 0;
      return { coordinate: [a[0] + (b[0] - a[0]) * f, a[1] + (b[1] - a[1]) * f],
        heading: Math.atan2((b[0] - a[0]) * Math.cos(a[1] * Math.PI / 180), b[1] - a[1]) };
    }
    remaining -= length;
  }
  return { coordinate: coordinates[0], heading: 0 };
}
export function routeSlice(coordinates: readonly RoutePoint[], startM: number, endM: number): RoutePoint[] {
  const points: RoutePoint[] = [routePose(coordinates, startM).coordinate];
  let at = 0;
  for (let i = 1; i < coordinates.length; i++) {
    at += routeDistanceM(coordinates[i - 1], coordinates[i]);
    if (at > startM && at < endM) points.push(coordinates[i]);
  }
  points.push(routePose(coordinates, endM).coordinate);
  return points;
}
export function inspectTransportStudy(text: string): readonly TransportWork[] {
  if (new TextEncoder().encode(text).length > TRANSPORT_STUDY_MAX_BYTES) throw new Error("Choose a study smaller than 2 MB.");
  let input;
  try { input = JSON.parse(text); } catch { throw new Error("Choose a valid construction-study JSON file."); }
  if (input?.version !== 1 || !Array.isArray(input.routes) || input.routes.length < 1 || input.routes.length > TRANSPORT_STUDY_MAX_ROUTES) throw new Error("A version 1 study must contain 1–12 routes.");
  const ids = new Set<string>(); let vertexCount = 0;
  return input.routes.map((record: Record<string, unknown>, index: number) => {
    if (!record || typeof record !== "object") throw new Error(`Route ${index + 1} is invalid.`);
    const fail = (message: string): never => { throw new Error(`Route ${index + 1}: ${message}`); };
    const { id, title, mode, action, coordinates, widthM, positionAccuracyM, start, end, sourceUrl, geometrySourceUrl, limitation } = record;
    if (typeof id !== "string" || !/^[a-z0-9-]{1,64}$/.test(id) || ids.has(id)) fail("use a unique simple ID.");
    ids.add(id as string);
    if (typeof title !== "string" || !title.trim() || title.length > 160 || typeof limitation !== "string" || !limitation.trim() || limitation.length > 800) fail("provide a title and a bounded limitation.");
    if (mode !== "road" && mode !== "rail" || !["build", "reconstruct", "remove"].includes(action as string)) fail("choose road/rail and build/reconstruct/remove.");
    if (!Array.isArray(coordinates) || coordinates.length < 2 || coordinates.length > 5_000) fail("provide 2–5,000 route vertices.");
    vertexCount += (coordinates as unknown[]).length;
    if (vertexCount > 10_000) fail("the study exceeds 10,000 vertices.");
    for (const p of coordinates as unknown[]) {
      if (!Array.isArray(p) || p.length !== 2 || !p.every(Number.isFinite) || p[0] < -102.1 || p[0] > -94.5 || p[1] < 36.9 || p[1] > 40.1) fail("use 2D longitude/latitude vertices inside Kansas.");
    }
    const points = coordinates as RoutePoint[];
    const length = routeLengthM(points);
    if (length < 80 || length > 500_000 || points.slice(1).some((p, i) => routeDistanceM(points[i], p) < .1)) fail("route length must be 80 m–500 km with no repeated vertices.");
    if (record.progressMode !== undefined && record.progressMode !== "front" && record.progressMode !== "milestones") fail("choose front or milestones progressMode.");
    if (record.progressMode === "milestones") {
      // Dates bound reports, not a fabricated actual work interval. No physical
      // width, front, closure interval or interpolation may be inferred here.
      const from = transportDay(start), to = transportDay(end);
      if (from === null || to === null || to <= from || !url(sourceUrl) || !url(geometrySourceUrl)) fail("provide ordered report-window dates and HTTPS source links.");
      if (record.interpolate !== false || !Array.isArray(record.progress) || record.progress.length || widthM !== undefined || positionAccuracyM !== undefined || record.closedFrom !== undefined || record.reopenedAt !== undefined) fail("milestone studies cannot assert a front, physical width/accuracy, interpolation or whole-route closure.");
      if (!Array.isArray(record.milestones) || record.milestones.length < 1 || record.milestones.length > 400) fail("provide 1–400 sourced milestones.");
      let previous = -Infinity;
      const milestones = (record.milestones as Record<string, unknown>[]).map(m => {
        if (!m || typeof m !== "object") return fail("invalid milestone.");
        const day = transportDay(m.date);
        if (day === null || day <= previous || day < (from as number) || day > (to as number) || !["planned", "activity-reported", "completion-reported"].includes(m.kind as string) || typeof m.title !== "string" || !m.title.trim() || m.title.length > 500 || !url(m.sourceUrl)) return fail("milestones require ordered report dates, a bounded title, kind and HTTPS source.");
        previous = day;
        return { date: m.date as string, kind: m.kind as TransportMilestone["kind"], title: m.title, sourceUrl: m.sourceUrl as string };
      });
      return { id, title, mode, action, coordinates: points, start, end, sourceUrl, geometrySourceUrl, limitation,
        progressMode: "milestones", milestones, progress: [], interpolate: false,
        // Internal sentinels only; milestone lines use a fixed cartographic width.
        widthM: 0, positionAccuracyM: 10_000, synthetic: input.synthetic === true } as TransportWork;
    }
    if (typeof widthM !== "number" || !Number.isFinite(widthM) || widthM < 2 || widthM > 40 || typeof positionAccuracyM !== "number" || !Number.isFinite(positionAccuracyM) || positionAccuracyM < .1 || positionAccuracyM > 10_000) fail("provide width (2–40 m) and positional uncertainty (0.1–10,000 m).");
    const startMs = transportDay(start), endMs = transportDay(end);
    if (startMs === null || endMs === null || endMs <= startMs || !url(sourceUrl) || !url(geometrySourceUrl)) fail("provide ordered actual work dates and HTTPS date/geometry source links.");
    if (record.interpolate !== undefined && typeof record.interpolate !== "boolean") fail("interpolate must be true or false.");
    const progress = record.progress;
    if (!Array.isArray(progress) || progress.length < 2 || progress.length > 400) fail("provide 2–400 dated chainage observations; calendar endpoints alone are insufficient.");
    let previousDate = -Infinity, previousM = -1;
    const samples = (progress as Record<string, unknown>[]).map(p => {
      if (!p || typeof p !== "object") return fail("invalid progress observation.");
      const date = transportDay(p.date), chainageM = p.chainageM;
      if (date === null || date <= previousDate || date < (startMs as number) || date > (endMs as number) || typeof chainageM !== "number" || !Number.isFinite(chainageM) || chainageM < previousM || chainageM < 0 || chainageM > length || !url(p.sourceUrl)) return fail("progress must be chronological, monotonic, within the work dates and route length, and individually sourced.");
      previousDate = date; previousM = chainageM;
      return { date: p.date as string, chainageM, sourceUrl: p.sourceUrl as string };
    });
    if (samples[0].chainageM !== 0 || samples[0].date !== start || samples.at(-1)!.date !== end || Math.abs(samples.at(-1)!.chainageM - length) > .5) fail("progress must begin at 0 m on the actual start and end at the route length on actual completion.");
    const closed = record.closedFrom === undefined ? undefined : transportDay(record.closedFrom);
    const reopened = record.reopenedAt === undefined ? undefined : transportDay(record.reopenedAt);
    if (closed === null || reopened === null || reopened !== undefined && (closed === undefined || reopened <= closed) || action === "remove" && reopened !== undefined) fail("closure/reopening dates must be valid, ordered, and consistent with removal.");
    // Return an explicit allowlist: never retain arbitrary metadata, linked assets or scripts.
    return { id, title, mode, action, coordinates: points, widthM, positionAccuracyM, start, end,
      closedFrom: record.closedFrom, reopenedAt: record.reopenedAt, progress: samples, interpolate: record.interpolate === true,
      sourceUrl, geometrySourceUrl, limitation, synthetic: input.synthetic === true } as TransportWork;
  });
}
export type TransportFrame = Readonly<{ state: "planned" | "working" | "complete" | "removed" | "unknown"; closed: boolean; chainageM: number; basis: "observed" | "interpolated" | "unknown"; sourceDate: string | null; rateMPerDay: number | null }>;
export function transportFrame(work: TransportWork, date: string): TransportFrame {
  const time = transportDay(date);
  if (time === null) return { state: "planned", closed: false, chainageM: 0, basis: "unknown", sourceDate: null, rateMPerDay: null };
  if (work.progressMode === "milestones") {
    const last = [...(work.milestones ?? [])].reverse().find(m => transportDay(m.date)! <= time);
    return { state: "unknown", closed: false, chainageM: 0, basis: "unknown", sourceDate: last?.date ?? null, rateMPerDay: null };
  }
  const start = transportDay(work.start)!, end = transportDay(work.end)!;
  const closed = Boolean(work.closedFrom && time >= transportDay(work.closedFrom)! && (!work.reopenedAt || time < transportDay(work.reopenedAt)!));
  if (time < start) return { state: "planned", closed, chainageM: 0, basis: "unknown", sourceDate: null, rateMPerDay: null };
  const earlier = [...work.progress].reverse().find(p => transportDay(p.date)! <= time)!;
  const later = work.progress.find(p => transportDay(p.date)! > time);
  const state = time >= end ? work.action === "remove" ? "removed" : "complete" : "working";
  const between = work.interpolate && later && transportDay(earlier.date)! < time;
  const fraction = between ? (time - transportDay(earlier.date)!) / (transportDay(later.date)! - transportDay(earlier.date)!) : 0;
  return { state, closed, chainageM: earlier.chainageM + (between ? (later.chainageM - earlier.chainageM) * fraction : 0),
    basis: between ? "interpolated" : "observed", sourceDate: earlier.date,
    rateMPerDay: later ? (later.chainageM - earlier.chainageM) / ((transportDay(later.date)! - transportDay(earlier.date)!) / DAY) : null };
}
/** Display LOD never enlarges a physical model to meet a minimum pixel size. */
export function transportWorkSectionFits(work: TransportWork, chainageM: number): boolean {
  if (work.widthM < 6 || chainageM < 45) return false;
  const front = routePose(work.coordinates, chainageM);
  const radians = Math.PI / 180;
  const allowance = Math.min(.35, Math.max(.1, (work.widthM - 6) / 2));
  for (let offset = 4; offset <= 40; offset += 4) {
    const point = routePose(work.coordinates, chainageM - offset);
    const east = (point.coordinate[0] - front.coordinate[0]) * 111_195 * Math.cos(front.coordinate[1] * radians);
    const north = (point.coordinate[1] - front.coordinate[1]) * 111_195;
    const across = east * Math.cos(front.heading) - north * Math.sin(front.heading);
    const angle = Math.atan2(Math.sin(point.heading - front.heading), Math.cos(point.heading - front.heading));
    if (Math.abs(across) > allowance || Math.abs(angle) > .08) return false;
  }
  return true;
}
export function transportDetail(zoom: number, latitude: number, accuracyM: number): "overview" | "equipment" | "crew" {
  const pixelsPerM = 512 * 2 ** zoom / (40_075_016.686 * Math.cos(latitude * Math.PI / 180));
  if (accuracyM > 4 || pixelsPerM * 8 < 7) return "overview";
  return pixelsPerM * .55 >= 2 ? "crew" : "equipment";
}
