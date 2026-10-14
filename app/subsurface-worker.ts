import { inKansas, nearbyColumns, areaColumns, displayColumns, validAreaBounds, validBorehole, validPosition, type AreaBounds, type Borehole, type Position, type SubsurfaceManifest } from "./subsurface-model";

type Query = { id: number; kind: "probe" | "search" | "area" | "prepare"; bounds?: AreaBounds; anchor: Position; route: Position[]; sources: string[]; year: number; search?: string };
const scope = self as unknown as { onmessage: ((event: MessageEvent<Query>) => void) | null; postMessage: (message: unknown) => void };
let controller: AbortController | null = null;
let manifest: SubsurfaceManifest | null = null;
let locator: [string, string, Position, string][] | null = null;
const cache = new Map<string, Borehole[]>();
const safeAsset = (url: string) => /^\/data\/subsurface\/[a-zA-Z0-9._-]+$/.test(url);
const hexDigest = (value: string) => /^[a-f0-9]{64}$/.test(value);
async function boundedBytes(stream: ReadableStream<Uint8Array> | null, limit: number, signal: AbortSignal): Promise<Uint8Array<ArrayBuffer>> {
  if (!stream) return new Uint8Array();
  const reader=stream.getReader(), chunks: Uint8Array[]=[]; let size=0;
  try {
    while (true) {
      if (signal.aborted) throw new Error("Source request canceled");
      const {done,value}=await reader.read(); if (done) break;
      size+=value.byteLength;
      if (size>limit) { await reader.cancel(); throw new Error("Source response exceeds display limit"); }
      chunks.push(value);
    }
  } finally { reader.releaseLock(); }
  const bytes=new Uint8Array(size);let offset=0;
  for (const chunk of chunks) { bytes.set(chunk,offset);offset+=chunk.byteLength; }
  return bytes;
}
const digestBytes = async (bytes: Uint8Array<ArrayBuffer>) => Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256",bytes)), b=>b.toString(16).padStart(2,"0")).join("");
async function readAsset(url: string, signal: AbortSignal, sha256?: string, decodedSha256?: string, maxBytes = 5_000_000): Promise<unknown> {
  if (!safeAsset(url)) throw new Error("Invalid source asset path");
  if ((sha256&&!hexDigest(sha256))||(decodedSha256&&!hexDigest(decodedSha256))) throw new Error("Invalid source digest");
  // Stable content identity avoids an older deployment's cached missing file.
  const response = await fetch(sha256 ? url+"?sha256="+sha256 : url, { signal, cache: "no-cache" });
  if (!response.ok) throw new Error("Source unavailable ("+response.status+")");
  const bytes=await boundedBytes(response.body,decodedSha256?25_000_000:maxBytes,signal);
  const gzip=bytes[0]===0x1f&&bytes[1]===0x8b;
  if (gzip&&bytes.length>maxBytes) throw new Error("Source response exceeds display limit");
  if (sha256) {
    const digest=await digestBytes(bytes);
    // A host may transparently decode gzip. Only separately pinned exact
    // decoded bytes qualify; parseable JSON alone never clears integrity.
    if (digest!==sha256&&(gzip||!decodedSha256||digest!==decodedSha256)) throw new Error("Source integrity mismatch; display held");
  }
  const stream=new Blob([bytes]).stream();
  const decoded=gzip?stream.pipeThrough(new DecompressionStream("gzip")):stream;
  const entity=await boundedBytes(decoded,25_000_000,signal);
  return JSON.parse(new TextDecoder("utf-8",{fatal:true}).decode(entity));
}
function failureCode(error: unknown) {
  const message=error instanceof Error?error.message:"";
  const status=/^Source unavailable \((\d{3})\)$/.exec(message);
  return status?"SOURCE_HTTP_"+status[1]:message.includes("integrity mismatch")?"SOURCE_DIGEST_MISMATCH":message.includes("display limit")?"SOURCE_SIZE_LIMIT":"SOURCE_DECODE_FAILED";
}
async function run(q: Query, signal: AbortSignal) {
  if (!manifest) {
    const m = await readAsset("/data/subsurface/manifest.json", signal) as SubsurfaceManifest;
    if (m.version !== 1 || !Array.isArray(m.tiles) || !Array.isArray(m.sources) || m.tiles.some(t => !safeAsset(t.url))) throw new Error("Unsupported source manifest");
    manifest = m;
  }
  // Opening this tool warms only its bounded local manifest, never source tiles.
  if (q.kind === "prepare") return { manifest, prepared: true };
  if (q.kind === "search") {
    const term = q.search?.trim().toLowerCase() ?? "";
    if (term.length < 2 || term.length > 100) return { matches: [], manifest };
    if (!locator && manifest.locator) locator = await readAsset(manifest.locator.url, signal, manifest.locator.sha256, manifest.locator.decodedSha256) as typeof locator;
    return { manifest, matches: (locator ?? []).filter(r => validPosition(r[2]) && inKansas(r[2]) && q.sources.includes(r[0].startsWith("core-") ? "kgs-core" : "kgs-wwc5") && (r[0].toLowerCase().includes(term) || r[1].toLowerCase().includes(term))).slice(0, 30) };
  }
  const area = q.kind === "area";
  if (area && !validAreaBounds(q.bounds)) throw new Error("Choose a Kansas area no wider than one degree, then show that area.");
  if (!area && (!validPosition(q.anchor) || !inKansas(q.anchor) || !Array.isArray(q.route) || q.route.some(p => !validPosition(p) || !inKansas(p)))) throw new Error("Choose a location inside Kansas");
  const points = !area && q.route.length > 1 ? q.route : [q.anchor];
  const bounds = area ? q.bounds! : [Math.min(...points.map(p => p[0])) - .31, Math.min(...points.map(p => p[1])) - .23, Math.max(...points.map(p => p[0])) + .31, Math.max(...points.map(p => p[1])) + .23];
  const rankAnchor: Position = area ? [(bounds[0]+bounds[2])/2,(bounds[1]+bounds[3])/2] : q.anchor;
  const eligible = manifest.tiles.filter(t => t.bounds[2] >= bounds[0] && t.bounds[0] <= bounds[2] && t.bounds[3] >= bounds[1] && t.bounds[1] <= bounds[3]);
  const selected = eligible.sort((a, b) => {
    const distance = (t: typeof a) => Math.hypot((t.bounds[0] + t.bounds[2]) / 2 - rankAnchor[0], (t.bounds[1] + t.bounds[3]) / 2 - rankAnchor[1]);
    return distance(a) - distance(b) || a.id.localeCompare(b.id);
  }).slice(0, 8);
  const failures: string[] = [], failureCodes: string[] = []; let rejected = 0, timeHeld = 0;
  const arrays = await Promise.all(selected.map(async tile => {
    if (cache.has(tile.id)) return cache.get(tile.id)!;
    try {
      const raw = await readAsset(tile.url, signal, tile.sha256, tile.decodedSha256);
      if (!Array.isArray(raw)) throw new Error("Invalid source rows");
      const records = raw.filter(validBorehole); rejected += raw.length - records.length;
      if (!signal.aborted) { cache.set(tile.id, records); if (cache.size > 12) cache.delete(cache.keys().next().value!); }
      return records;
    } catch (error) { if (signal.aborted) throw error; failures.push(tile.id); failureCodes.push(failureCode(error)); return []; }
  }));
  const records = arrays.flat().filter(r => {
    if (!q.sources.includes(r.sourceId)) return false;
    if (area && (r.coordinates[0]<bounds[0]||r.coordinates[0]>bounds[2]||r.coordinates[1]<bounds[1]||r.coordinates[1]>bounds[3])) return false;
    // Archive dates are not historical reconstructions. In historical views, dated records from later years are held.
    if (q.year < new Date().getUTCFullYear()) {
      const recordYear = /^\d{4}-/.test(r.sourceTime) ? Number(r.sourceTime.slice(0, 4)) : NaN;
      if (!Number.isFinite(recordYear) || recordYear > q.year) { timeHeld++; return false; }
    }
    return true;
  });
  const ranked = area ? areaColumns(records, q.bounds!) : nearbyColumns(records, q.anchor, q.route);
  return { manifest, ...(area ? {bounds:q.bounds} : {}), columns: displayColumns(ranked), total: ranked.length, failures, failureCodes, rejected, timeHeld,
    ...(selected.length > 0 && failures.length === selected.length ? {error:"Requested well/core files could not be loaded. This is a source-delivery failure, not evidence that no records exist. "+[...new Set(failureCodes)].join(", ")} : {}),
    partial: eligible.length > selected.length || failures.length > 0 || (area && ranked.length > 50),
    coverage: `${selected.length - failures.length}/${selected.length} requested tiles loaded; ${eligible.length} intersect ${area ? "the selected map area" : "the 25 km search corridor"}. ${ranked.length} eligible records ${area ? "inside the area in loaded tiles" : "in loaded data"}; showing ${Math.min(50,ranked.length)} of up to 50.${area && ranked.length>50 ? " Record limit reached; closest wells and cores are represented separately. Zoom to a smaller area or choose one source for more detail." : ""} ${timeHeld} date-incompatible/undated records held. ${rejected} invalid records rejected.` };
}
scope.onmessage = event => {
  const expectedOrigin = self.location.origin;
  if (event.origin && event.origin !== expectedOrigin) return;
  controller?.abort(); controller = new AbortController(); const current = controller; const q = event.data;
  void run(q, current.signal).then(result => { if (!current.signal.aborted) scope.postMessage({ id: q.id, ...result }); })
    .catch(error => { if (!current.signal.aborted) scope.postMessage({ id: q.id, error: error instanceof Error ? error.message : "Underground source unavailable" }); });
};
