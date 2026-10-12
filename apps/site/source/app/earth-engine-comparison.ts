import { EARTH_ENGINE_CONTEXT_LAYERS, EARTH_ENGINE_SOURCE_YEARS, earthEngineSetYear, parseEarthEngineManifest, type EarthEngineContextLayer, type EarthEngineContextLayerId, type EarthEngineContextManifest } from "./earth-engine-context";
import type { Map as MapLibreMap } from "./maplibre-seam";

export type ComparisonSnapshot = { year: number; setId: string; layer: EarthEngineContextLayer };
export type ComparisonPair = { kind: "ready"; id: EarthEngineContextLayerId; key: string; a: ComparisonSnapshot; b: ComparisonSnapshot; minZoom: number; maxZoom: number; overviewZoom: number | null }
  | { kind: "unavailable"; reason: string };

export function comparisonCameraOptions(pair: Extract<ComparisonPair, { kind: "ready" }>) {
  const minZoom = pair.minZoom, maxZoom = Math.min(22, pair.maxZoom + 2);
  return { minZoom, maxZoom, zoom: Math.min(maxZoom, Math.max(5, minZoom)) };
}

/** Share position/scale while excluding terrain, bearing, and pitch from a flat comparison. */
export function synchronizeComparisonMaps(maps: Pick<MapLibreMap, "on" | "off" | "jumpTo" | "getCenter" | "getZoom">[]): () => void {
  let syncing = false, disposed = false;
  const listeners = maps.map(map => {
    const move = () => {
      if (syncing || disposed) return;
      syncing = true;
      try { for (const other of maps) if (other !== map) other.jumpTo({ center: map.getCenter(), zoom: map.getZoom(), bearing: 0, pitch: 0 }); }
      finally { syncing = false; }
    };
    map.on("move", move);
    return { map, move };
  });
  return () => { disposed = true; for (const { map, move } of listeners) map.off("move", move); };
}

export function comparisonYears(manifests: readonly EarthEngineContextManifest[], id: EarthEngineContextLayerId): number[] {
  if (!EARTH_ENGINE_SOURCE_YEARS[id]) return [];
  const counts = new Map<number, number>();
  for (const candidate of manifests) {
    const manifest = parseEarthEngineManifest(candidate), year = earthEngineSetYear(manifest);
    if (manifest && year !== null && manifest.layers.some(layer => layer.id === id && layer.status === "approved")) counts.set(year, (counts.get(year) ?? 0) + 1);
  }
  // Duplicate pointers are ambiguous, never selected by array order.
  return [...counts].filter(([, count]) => count === 1).map(([year]) => year).sort((a, b) => a - b);
}

export function comparisonPair(manifests: readonly EarthEngineContextManifest[], id: EarthEngineContextLayerId, yearA: number, yearB: number): ComparisonPair {
  const unavailable = (reason: string): ComparisonPair => ({ kind: "unavailable", reason });
  if (!EARTH_ENGINE_CONTEXT_LAYERS.some(layer => layer.id === id) || !EARTH_ENGINE_SOURCE_YEARS[id]) return unavailable("Choose one annual imagery product. Mixed-date elevation cannot be compared as annual imagery.");
  if (yearA === yearB) return unavailable("Choose two different installed years.");
  const years = comparisonYears(manifests, id);
  if (!years.includes(yearA) || !years.includes(yearB)) return unavailable("Two unambiguous, approved, installed years are required. Missing years remain unavailable.");
  const snapshot = (year: number): ComparisonSnapshot => {
    const manifest = manifests.find(item => parseEarthEngineManifest(item) && earthEngineSetYear(item) === year && item.layers.some(layer => layer.id === id && layer.status === "approved"))!;
    return { year, setId: manifest.setId, layer: manifest.layers.find(layer => layer.id === id)! };
  };
  const a = snapshot(yearA), b = snapshot(yearB);
  if (a.layer.source !== b.layer.source || a.layer.resolutionMeters !== b.layer.resolutionMeters || a.layer.legend !== b.layer.legend) return unavailable("The selected snapshots have different source, grid resolution, or legend metadata. Review their compatibility before comparing them.");
  const zooms = Object.keys(a.layer.tileIndexes).map(Number).filter(z => Boolean(b.layer.tileIndexes[String(z)])).sort((x, y) => x - y);
  if (!zooms.length) return unavailable("The selected snapshots have no common prepared tile zoom.");
  const overviewZoom = zooms.filter(z => {
    if (z > 8) return false;
    const x = a.layer.tileIndexes[String(z)], y = b.layer.tileIndexes[String(z)];
    return (Math.max(x.maxX, y.maxX) - Math.min(x.minX, y.minX) + 1) * (Math.max(x.maxY, y.maxY) - Math.min(x.minY, y.minY) + 1) <= 96;
  }).at(-1) ?? null;
  return { kind: "ready", id, a, b, minZoom: zooms[0], maxZoom: zooms.at(-1)!, overviewZoom,
    key: [id, a.setId, b.setId, a.layer.reviewSha256, b.layer.reviewSha256, a.layer.geotiffSha256, b.layer.geotiffSha256].join(":") };
}

export function comparisonTileUrl(snapshot: ComparisonSnapshot, z: number, x: number, y: number): string | null {
  const index = snapshot.layer.tileIndexes[String(z)];
  if (!index || ![z, x, y].every(Number.isInteger) || x < index.minX || x > index.maxX || y < index.minY || y > index.maxY) return null;
  // Rectangle membership is only a request envelope. The existing server checks exact hashed tile membership.
  return `/api/earth-engine-context/${encodeURIComponent(snapshot.setId)}/${snapshot.layer.id}/${z}/${x}/${y}.png`;
}

/** Whole-request deadline, cancellation, and a small PNG budget apply in both renderers. */
export async function readComparisonTile(url: string, caller: AbortSignal, timeoutMs = 15_000): Promise<ArrayBuffer> {
  const path = /^\/api\/earth-engine-context\/(ks-\d{4}-[a-z0-9-]{6,64})\/ee-[a-z0-9-]+\/\d{1,2}\/\d+\/\d+\.png$/.exec(url);
  if (!path || earthEngineSetYear({ setId: path[1] }) === null) throw new Error("Invalid comparison tile path.");
  const deadline = new AbortController(), signal = AbortSignal.any([caller, deadline.signal]);
  const timer = setTimeout(() => deadline.abort(new DOMException("Tile request timed out", "TimeoutError")), timeoutMs);
  const limit = 512 * 1024;
  try {
    signal.throwIfAborted();
    const response = await fetch(url, { signal, credentials: "same-origin", cache: "no-store", redirect: "error" });
    if (signal.aborted) { void response.body?.cancel().catch(() => undefined); signal.throwIfAborted(); }
    if (!response.ok || response.headers.get("content-type")?.split(";")[0].trim() !== "image/png" || Number(response.headers.get("content-length")) > limit || !response.body) {
      void response.body?.cancel().catch(() => undefined);
      throw new Error("Tile unavailable.");
    }
    const reader = response.body.getReader(), chunks: Uint8Array[] = [];
    let total = 0;
    const cancel = () => { void reader.cancel(signal.reason).catch(() => undefined); };
    signal.addEventListener("abort", cancel, { once: true });
    try {
      while (true) {
        signal.throwIfAborted();
        const chunk = await reader.read();
        signal.throwIfAborted();
        if (chunk.done) break;
        total += chunk.value.byteLength;
        if (total > limit) throw new Error("Tile byte limit exceeded.");
        chunks.push(chunk.value);
      }
    } catch (error) { void reader.cancel().catch(() => undefined); throw error; }
    finally { signal.removeEventListener("abort", cancel); reader.releaseLock(); }
    const bytes = new Uint8Array(total);
    let offset = 0;
    for (const chunk of chunks) { bytes.set(chunk, offset); offset += chunk.byteLength; }
    if (bytes.length < 24 || ![137,80,78,71,13,10,26,10].every((value, i) => bytes[i] === value)) throw new Error("Tile is not a PNG.");
    signal.throwIfAborted();
    return bytes.buffer;
  } finally { clearTimeout(timer); }
}
