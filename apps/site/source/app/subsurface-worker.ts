import { inKansas, nearbyColumns, validBorehole, validPosition, type Borehole, type Position, type SubsurfaceManifest } from "./subsurface-model";

type Query = { id: number; kind: "probe" | "search"; anchor: Position; route: Position[]; sources: string[]; year: number; search?: string };
const scope = self as unknown as { onmessage: ((event: MessageEvent<Query>) => void) | null; postMessage: (message: unknown) => void };
let controller: AbortController | null = null;
let manifest: SubsurfaceManifest | null = null;
let locator: [string, string, Position, string][] | null = null;
const cache = new Map<string, Borehole[]>();
const safeAsset = (url: string) => /^\/data\/subsurface\/[a-zA-Z0-9._-]+$/.test(url);
async function readAsset(url: string, signal: AbortSignal, sha256?: string, maxBytes = 5_000_000): Promise<unknown> {
  if (!safeAsset(url)) throw new Error("Invalid source asset path");
  const response = await fetch(url, { signal });
  if (!response.ok) throw new Error(`Source unavailable (${response.status})`);
  const bytes = new Uint8Array(await response.arrayBuffer());
  if (bytes.length > maxBytes) throw new Error("Source response exceeds display limit");
  if (sha256) {
    const digest = Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256", bytes)), b => b.toString(16).padStart(2, "0")).join("");
    if (digest !== sha256) throw new Error("Source integrity mismatch; display held");
  }
  const stream = new Blob([bytes]).stream();
  const decoded = bytes[0] === 0x1f && bytes[1] === 0x8b ? stream.pipeThrough(new DecompressionStream("gzip")) : stream;
  const text = await new Response(decoded).text();
  if (text.length > 25_000_000) throw new Error("Expanded source exceeds display limit");
  return JSON.parse(text);
}
async function run(q: Query, signal: AbortSignal) {
  if (!manifest) {
    const m = await readAsset("/data/subsurface/manifest.json", signal) as SubsurfaceManifest;
    if (m.version !== 1 || !Array.isArray(m.tiles) || !Array.isArray(m.sources) || m.tiles.some(t => !safeAsset(t.url))) throw new Error("Unsupported source manifest");
    manifest = m;
  }
  if (q.kind === "search") {
    const term = q.search?.trim().toLowerCase() ?? "";
    if (term.length < 2 || term.length > 100) return { matches: [], manifest };
    if (!locator && manifest.locator) locator = await readAsset(manifest.locator.url, signal, manifest.locator.sha256) as typeof locator;
    return { manifest, matches: (locator ?? []).filter(r => r[0].toLowerCase().includes(term) || r[1].toLowerCase().includes(term)).slice(0, 30) };
  }
  if (!validPosition(q.anchor) || !inKansas(q.anchor) || !Array.isArray(q.route) || q.route.some(p => !validPosition(p) || !inKansas(p))) throw new Error("Choose a location inside Kansas");
  const points = q.route.length > 1 ? q.route : [q.anchor];
  const bounds = [Math.min(...points.map(p => p[0])) - .31, Math.min(...points.map(p => p[1])) - .23, Math.max(...points.map(p => p[0])) + .31, Math.max(...points.map(p => p[1])) + .23];
  const eligible = manifest.tiles.filter(t => t.bounds[2] >= bounds[0] && t.bounds[0] <= bounds[2] && t.bounds[3] >= bounds[1] && t.bounds[1] <= bounds[3]);
  const selected = eligible.sort((a, b) => {
    const distance = (t: typeof a) => Math.hypot((t.bounds[0] + t.bounds[2]) / 2 - q.anchor[0], (t.bounds[1] + t.bounds[3]) / 2 - q.anchor[1]);
    return distance(a) - distance(b) || a.id.localeCompare(b.id);
  }).slice(0, 8);
  const failures: string[] = []; let rejected = 0, timeHeld = 0;
  const arrays = await Promise.all(selected.map(async tile => {
    if (cache.has(tile.id)) return cache.get(tile.id)!;
    try {
      const raw = await readAsset(tile.url, signal, tile.sha256);
      if (!Array.isArray(raw)) throw new Error("Invalid source rows");
      const records = raw.filter(validBorehole); rejected += raw.length - records.length;
      if (!signal.aborted) { cache.set(tile.id, records); if (cache.size > 12) cache.delete(cache.keys().next().value!); }
      return records;
    } catch (error) { if (signal.aborted) throw error; failures.push(tile.id); return []; }
  }));
  const records = arrays.flat().filter(r => {
    if (!q.sources.includes(r.sourceId)) return false;
    // Archive dates are not historical reconstructions. In historical views, dated records from later years are held.
    if (q.year < new Date().getUTCFullYear()) {
      const recordYear = /^\d{4}-/.test(r.sourceTime) ? Number(r.sourceTime.slice(0, 4)) : NaN;
      if (!Number.isFinite(recordYear) || recordYear > q.year) { timeHeld++; return false; }
    }
    return true;
  });
  const ranked = nearbyColumns(records, q.anchor, q.route);
  return { manifest, columns: ranked.slice(0, 50), total: ranked.length, failures, rejected, timeHeld,
    partial: eligible.length > selected.length || failures.length > 0,
    coverage: `${selected.length - failures.length}/${selected.length} requested tiles loaded; ${eligible.length} intersect the 25 km search corridor. ${ranked.length} eligible records in loaded data; showing up to 50. ${timeHeld} date-incompatible/undated records held. ${rejected} invalid records rejected.` };
}
scope.onmessage = event => {
  const expectedOrigin = self.location.origin;
  if (event.origin && event.origin !== expectedOrigin) return;
  controller?.abort(); controller = new AbortController(); const current = controller; const q = event.data;
  void run(q, current.signal).then(result => { if (!current.signal.aborted) scope.postMessage({ id: q.id, ...result }); })
    .catch(error => { if (!current.signal.aborted) scope.postMessage({ id: q.id, error: error instanceof Error ? error.message : "Underground source unavailable" }); });
};
