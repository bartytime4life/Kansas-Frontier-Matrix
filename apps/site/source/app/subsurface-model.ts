import { atRecordYear } from "./subsurface-materials";
/** Display context from published sources; never an EvidenceBundle or geological interpolation. */
export type Position = [number, number];
export type DepthUnit = "ft" | "m";
export type DepthInterval = { top: number; bottom: number; description: string; interpreted?: string; category?: string };
export type Borehole = {
  id: string; sourceId: string; kind: "well" | "core"; name: string; coordinates: Position;
  coordinateReference: string; locationMethod: string; sourceUrl: string; sourceTime: string;
  depthUnit: DepthUnit; depthReference: "land-surface" | "drilled-depth" | "unknown";
  totalDepth: number | null; intervals: DepthInterval[]; photosUrl?: string;
};
export type DisplaySource = { id: string; title: string; url: string; retrievedAt: string; sourceTime: string; limitation: string; sha256: string };
export type SubsurfaceManifest = {
  version: 1; capturedAt: string; sources: DisplaySource[];
  tiles: { id: string; bounds: [number, number, number, number]; url: string; count: number; sha256: string }[];
  totals: Record<string, number>; counties: { name: string; coordinates: Position; count: number }[];
  locator?: { url: string; sha256: string };
};
export type SubsurfaceContext = {
  version: 1; capturedAt: string; anchor: Position; pinned: boolean; transect: Position[];
  depthRange: [number, number]; display: "section" | "3d" | "aquifer" | "surveys" | "soil";
  exaggeration: number; selectedSources: string[]; sourceVersions: DisplaySource[];
  recordIds: string[]; records: Borehole[]; coverage: string[];
  recordCutoff?: number | null;
  cursorDepth?: number; selectedRecordId?: string; descriptionFilter?: string;
};
export type SectionRecord = { record: Borehole; alongMeters: number; offsetMeters: number; distanceMeters: number };
export type GeophysicalProfile = { id: string; title: string; coordinates: Position; depthUnit: DepthUnit; depthReference: string; valueUnit: string; samples: { depth: number; value: number }[]; limitation?: string };
export type GeophysicalSurvey = { id: string; title: string; method: "electrical" | "gpr" | "electromagnetic" | "seismic"; sourceUrl: string; sourceTime: string; retrievedAt: string; status: "ready" | "reference-only" | "held"; limitation: string; profiles: GeophysicalProfile[] };

const obj = (v: unknown): v is Record<string, unknown> => !!v && typeof v === "object" && !Array.isArray(v);
const str = (v: unknown, n = 1000): v is string => typeof v === "string" && v.length <= n;
const num = (v: unknown): v is number => typeof v === "number" && Number.isFinite(v);
export const validPosition = (v: unknown): v is Position => Array.isArray(v) && v.length === 2 && v.every(num) && v[0] >= -180 && v[0] <= 180 && v[1] >= -90 && v[1] <= 90;
export const inKansas = (p: Position) => p[0] >= -102.1 && p[0] <= -94.5 && p[1] >= 36.9 && p[1] <= 40.1;
export const sourceLink = (v: unknown): string | null => {
  if (!str(v, 2000)) return null;
  try { const u = new URL(v); return u.protocol === "https:" && !u.username && !u.password ? u.href : null; } catch { return null; }
};
export function validBorehole(v: unknown): v is Borehole {
  return obj(v) && str(v.id, 160) && !!v.id && str(v.sourceId, 80) && ["well", "core"].includes(String(v.kind)) && str(v.name, 240)
    && validPosition(v.coordinates) && inKansas(v.coordinates) && str(v.coordinateReference) && str(v.locationMethod)
    && !!sourceLink(v.sourceUrl) && str(v.sourceTime) && ["ft", "m"].includes(String(v.depthUnit))
    && ["land-surface", "drilled-depth", "unknown"].includes(String(v.depthReference))
    && (v.totalDepth === null || (num(v.totalDepth) && v.totalDepth >= 0 && v.totalDepth <= 40000))
    && (v.photosUrl === undefined || !!sourceLink(v.photosUrl)) && Array.isArray(v.intervals) && v.intervals.length <= 2000
    && v.intervals.every(i => obj(i) && num(i.top) && num(i.bottom) && i.top >= 0 && i.bottom > i.top && i.bottom <= 40000
      && str(i.description, 10000) && (i.interpreted === undefined || str(i.interpreted, 10000)) && (i.category === undefined || str(i.category, 1000)));
}
export function validGeophysicalSurvey(v: unknown): v is GeophysicalSurvey {
  if (!obj(v) || !str(v.id, 120) || !str(v.title) || !["electrical", "gpr", "electromagnetic", "seismic"].includes(String(v.method))
    || !sourceLink(v.sourceUrl) || !str(v.sourceTime) || !str(v.retrievedAt) || !Number.isFinite(Date.parse(v.retrievedAt))
    || !["ready", "reference-only", "held"].includes(String(v.status)) || !str(v.limitation, 10000) || !Array.isArray(v.profiles) || v.profiles.length > 100) return false;
  if (v.status !== "ready") return v.profiles.length === 0;
  // No qualified radar velocity model is currently available. A new time-axis adapter is required before GPR activation.
  if (v.method === "gpr") return false;
  return v.profiles.every(p => obj(p) && str(p.id, 120) && str(p.title) && validPosition(p.coordinates) && inKansas(p.coordinates)
    && ["ft", "m"].includes(String(p.depthUnit)) && ["land-surface", "unknown"].includes(String(p.depthReference)) && str(p.valueUnit, 30)
    && Array.isArray(p.samples) && p.samples.length <= 10000 && p.samples.every((s, i, samples) => obj(s) && num(s.depth) && num(s.value) && s.depth >= 0
      && (i === 0 || s.depth > (samples[i - 1] as { depth: number }).depth)));
}
const strings = (v: unknown, count: number, length: number) => Array.isArray(v) && v.length <= count && v.every(s => str(s, length));
export function validSubsurfaceContext(v: unknown): v is SubsurfaceContext {
  return obj(v) && v.version === 1 && str(v.capturedAt) && Number.isFinite(Date.parse(v.capturedAt)) && validPosition(v.anchor) && inKansas(v.anchor)
    && typeof v.pinned === "boolean" && Array.isArray(v.transect) && v.transect.length <= 100 && v.transect.every(p => validPosition(p) && inKansas(p))
    && Array.isArray(v.depthRange) && v.depthRange.length === 2 && v.depthRange.every(num) && v.depthRange[0] >= 0 && v.depthRange[1] > v.depthRange[0] && v.depthRange[1] <= 12000
    && ["section", "3d", "aquifer", "surveys", "soil"].includes(String(v.display)) && num(v.exaggeration) && v.exaggeration >= 1 && v.exaggeration <= 100
    && (v.recordCutoff === undefined || v.recordCutoff === null || (Number.isInteger(v.recordCutoff) && num(v.recordCutoff) && v.recordCutoff >= 1800 && v.recordCutoff <= 2200))
    && (v.cursorDepth === undefined || (num(v.cursorDepth) && v.cursorDepth >= v.depthRange[0] && v.cursorDepth <= v.depthRange[1]))
    && (v.selectedRecordId === undefined || str(v.selectedRecordId, 160)) && (v.descriptionFilter === undefined || str(v.descriptionFilter, 10000))
    && strings(v.selectedSources, 20, 80) && strings(v.recordIds, 50, 160) && strings(v.coverage, 30, 3000)
    && Array.isArray(v.records) && v.records.length <= 50 && v.records.every(r => validBorehole(r) && atRecordYear(r, (v.recordCutoff as number | null | undefined) ?? null))
    && new Set(v.records.map(r => r.id)).size === v.records.length && v.records.every(r => (v.recordIds as string[]).includes(r.id))
    && Array.isArray(v.sourceVersions) && v.sourceVersions.length <= 20 && v.sourceVersions.every(s => obj(s) && str(s.id, 80) && str(s.title) && !!sourceLink(s.url)
      && str(s.retrievedAt) && Number.isFinite(Date.parse(s.retrievedAt)) && str(s.sourceTime) && str(s.limitation, 10000) && str(s.sha256, 64) && /^[a-f0-9]{64}$/.test(s.sha256));
}
export function persistableSubsurface(v: SubsurfaceContext | null, redacted: boolean, settingsOnly = false): SubsurfaceContext | undefined {
  if (redacted || !validSubsurfaceContext(v)) return undefined;
  // A restored workspace fetches current eligible assets, never reuses captured rows as live data.
  return JSON.parse(JSON.stringify({ ...v, records: settingsOnly ? [] : v.records }));
}
export const meters = (depth: number, unit: DepthUnit) => depth * (unit === "ft" ? 0.3048 : 1);
export const radarDepth = (twoWayNanoseconds: number, metersPerNanosecond?: number) =>
  num(metersPerNanosecond) && metersPerNanosecond > 0 && metersPerNanosecond <= 0.3 && twoWayNanoseconds >= 0 ? twoWayNanoseconds * metersPerNanosecond / 2 : null;
/** No geodetic registration or deviated-well placement without independent datum/trajectory qualification. */
export const canPlaceInGeologicalModel = (reference: string, trajectoryVerified: boolean, datumVerified: boolean) => reference === "land-surface" && trajectoryVerified && datumVerified;
const radians = (n: number) => n * Math.PI / 180;
export function distanceMeters(a: Position, b: Position): number {
  const dLat = radians(b[1] - a[1]), dLon = radians(b[0] - a[0]);
  const h = Math.sin(dLat / 2) ** 2 + Math.cos(radians(a[1])) * Math.cos(radians(b[1])) * Math.sin(dLon / 2) ** 2;
  return 6371008.8 * 2 * Math.atan2(Math.sqrt(h), Math.sqrt(Math.max(0, 1 - h)));
}
const bearing = (a: Position, b: Position) => Math.atan2(Math.sin(radians(b[0] - a[0])) * Math.cos(radians(b[1])), Math.cos(radians(a[1])) * Math.sin(radians(b[1])) - Math.sin(radians(a[1])) * Math.cos(radians(b[1])) * Math.cos(radians(b[0] - a[0])));
/** Great-circle segment projection; endpoint clamping keeps section offsets honest. */
export function sectionOffset(p: Position, route: Position[]): { alongMeters: number; offsetMeters: number } {
  let traveled = 0, best = { alongMeters: 0, offsetMeters: Infinity };
  for (let i = 1; i < route.length; i++) {
    const a = route[i - 1], b = route[i], length = distanceMeters(a, b);
    if (!length) continue;
    const angle = distanceMeters(a, p) / 6371008.8, delta = bearing(a, p) - bearing(a, b);
    const along = Math.atan2(Math.sin(angle) * Math.cos(delta), Math.cos(angle)) * 6371008.8;
    const offset = along < 0 ? distanceMeters(a, p) : along > length ? distanceMeters(b, p) : Math.abs(Math.asin(Math.max(-1, Math.min(1, Math.sin(angle) * Math.sin(delta))))) * 6371008.8;
    if (offset < best.offsetMeters) best = { alongMeters: traveled + Math.max(0, Math.min(length, along)), offsetMeters: offset };
    traveled += length;
  }
  return best;
}
export function nearbyColumns(records: Borehole[], anchor: Position, route: Position[] = [], radius = 25000): SectionRecord[] {
  const seen = new Set<string>();
  return records.filter(r => { const key = `${r.sourceId}:${r.id}`; if (seen.has(key)) return false; seen.add(key); return true; })
    .map(record => ({ record, distanceMeters: distanceMeters(anchor, record.coordinates), ...(route.length > 1 ? sectionOffset(record.coordinates, route) : { alongMeters: 0, offsetMeters: 0 }) }))
    .filter(r => (route.length > 1 ? r.offsetMeters : r.distanceMeters) <= radius)
    .sort((a, b) => (route.length > 1 ? a.offsetMeters - b.offsetMeters : a.distanceMeters - b.distanceMeters) || a.record.id.localeCompare(b.record.id, "en"));
}
export function intervalIssues(intervals: DepthInterval[]): { gaps: [number, number][]; overlaps: [number, number][] } {
  const result = { gaps: [] as [number, number][], overlaps: [] as [number, number][] }; let end = 0;
  for (const i of [...intervals].sort((a, b) => a.top - b.top || a.bottom - b.bottom)) {
    if (i.top > end) result.gaps.push([end, i.top]);
    if (i.top < end) result.overlaps.push([i.top, Math.min(end, i.bottom)]);
    end = Math.max(end, i.bottom);
  }
  return result;
}
export function intervalColor(i: DepthInterval): string {
  // Visual encoding of the supplied description only; these colors do not infer geology between wells.
  const s = `${i.interpreted ?? ""} ${i.description}`.toLowerCase();
  return /limestone/.test(s) ? "#c6c5ad" : /sandstone/.test(s) ? "#c99961" : /shale/.test(s) ? "#7f8586" : /clay/.test(s) ? "#ba8466" : /gravel/.test(s) ? "#9d9c83" : /sand/.test(s) ? "#dfc184" : /silt/.test(s) ? "#b6a186" : /soil/.test(s) ? "#76644f" : "#a6a5a0";
}
export const SUBSURFACE_LIMIT = "Source-backed display context, separate from included evidence. Columns use each record's own depth reference; gaps are unknown. No continuous seams, verified trajectories, or common elevation datum are supplied. Surface-map time does not reconstruct historical underground conditions.";
const xml = (s: string) => s.replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&apos;" })[c]!);
export function sectionSvg(context: SubsurfaceContext | null, redacted = false): string | null {
  const c = persistableSubsurface(context, redacted); if (!c) return null;
  const rows = nearbyColumns(c.records, c.anchor, c.transect, 1000000).slice(0, 12);
  const width = 960, height = 470, top = 80, plot = 300, range = c.depthRange[1] - c.depthRange[0];
  const blocks = rows.map((r, index) => {
    const x = 80 + index * (800 / Math.max(1, rows.length));
    return `<text x="${x}" y="58" font-size="10">${xml(r.record.id)}</text><rect x="${x}" y="${top}" width="32" height="${plot}" fill="#e6e2d8" stroke="#6c6d64" stroke-dasharray="2 4"/>` + r.record.intervals.map(i => {
      const a = Math.max(c.depthRange[0], meters(i.top, r.record.depthUnit)), b = Math.min(c.depthRange[1], meters(i.bottom, r.record.depthUnit));
      return b > a ? `<rect x="${x}" y="${top + (a - c.depthRange[0]) / range * plot}" width="32" height="${(b - a) / range * plot}" fill="${intervalColor(i)}"><title>${xml(`${i.top}–${i.bottom} ${r.record.depthUnit}: ${i.description}`)}</title></rect>` : "";
    }).join("") + `<text x="${x}" y="402" font-size="9">${xml(r.record.depthReference)}</text><text x="${x}" y="417" font-size="9">${(r.offsetMeters / 1000).toFixed(2)} km offset</text>`;
  }).join("");
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${width} ${height}"><rect width="100%" height="100%" fill="#f6f1e6"/><g font-family="sans-serif" fill="#253530"><text x="24" y="25" font-size="16">KFM recorded-depth columns · ${xml(c.capturedAt)}</text><text x="24" y="45" font-size="11">${c.depthRange[0]}–${c.depthRange[1]} m · individual reference depths · diagram; horizontal spacing is not scale</text>${blocks}<text x="24" y="446" font-size="11">Unknown between observations. Provider context, not included evidence. Sources and limitations accompany this image.</text><text x="24" y="464" font-size="9">The source of this material is the Kansas Geological Survey website at http://www.kgs.ku.edu/. All Rights Reserved.</text></g></svg>`;
}
const csvCell = (v: unknown) => { const s = String(v ?? ""); return `"${(/^[=+@\-\t\r]/.test(s) ? "'" : "") + s.replaceAll('"', '""')}"`; };
export function intervalCsv(context: SubsurfaceContext | null, redacted = false): string | null {
  const c = persistableSubsurface(context, redacted); if (!c) return null;
  return [["capture_time", "source", "record", "longitude", "latitude", "top", "bottom", "unit", "depth_reference", "original_description", "kgs_interpretation", "source_url", "archive_sha256", "source_edition", "retrieved_at", "coverage_limit", "attribution"],
    ...c.records.flatMap(r => { const source = c.sourceVersions.find(s => s.id === r.sourceId); return r.intervals.map(i => [c.capturedAt, r.sourceId, r.id, ...r.coordinates, i.top, i.bottom, r.depthUnit, r.depthReference, i.description, i.interpreted ?? "", r.sourceUrl, source?.sha256, source?.sourceTime, source?.retrievedAt, c.coverage.join("; "), "The source of this material is the Kansas Geological Survey website at http://www.kgs.ku.edu/. All Rights Reserved."]); })].map(row => row.map(csvCell).join(",")).join("\r\n");
}
export function subsurfaceMarkdown(context: SubsurfaceContext): string {
  if (!validSubsurfaceContext(context)) return "Underground context unavailable.";
  return ["## Underground source context", `Captured ${context.capturedAt}; ${context.records.length} loaded records. Depth ${context.depthRange.join("–")} m.`, SUBSURFACE_LIMIT,
    ...context.sourceVersions.map(s => `- ${s.title}: ${s.url} · retrieved ${s.retrievedAt} · source time ${s.sourceTime} · SHA256 ${s.sha256}. ${s.limitation}`),
    ...context.coverage.map(s => `- ${s}`), ...context.records.map(r => `- ${r.id}: ${r.sourceUrl} · ${r.depthReference}, ${r.depthUnit}; ${r.intervals.length} intervals.`)].join("\n\n");
}
