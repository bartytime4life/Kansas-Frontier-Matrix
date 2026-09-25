import { boundedFetch } from "./api/event-atlas/upstream";

export const TERRAIN_TILE_BOUNDS = [-104.8, 34.8, -92, 42.2] as const;
export const TERRAIN_TILE_MAX_ZOOM = 14;
export const TERRAIN_TILE_TTL = 6 * 60 * 60;
const FUNCTIONS = { hillshade: "Hillshade Multidirectional", slope: "Slope Map" } as const;
const ORIGIN = "https://elevation.nationalmap.gov/arcgis/rest/services/3DEPElevation/ImageServer/exportImage";
export function terrainTileRequest(url: URL) {
  const p = url.searchParams;
  if ([...p.keys()].some((k) => !["kind", "z", "x", "y"].includes(k) || p.getAll(k).length !== 1)) throw new Error("Unsupported tile request.");
  const kind = p.get("kind");
  if (kind !== "hillshade" && kind !== "slope") throw new Error("Unknown terrain layer.");
  const values = ["z", "x", "y"].map((k) => { const raw = p.get(k); if (!raw || !/^\d{1,5}$/.test(raw)) throw new Error("Invalid tile coordinate."); return Number(raw); });
  const [z, x, y] = values, n = 2 ** z;
  if (z < 3 || z > TERRAIN_TILE_MAX_ZOOM || x >= n || y >= n) throw new Error("Tile outside supported zoom range.");
  const latitude = (row: number) => Math.atan(Math.sinh(Math.PI * (1 - 2 * row / n))) * 180 / Math.PI;
  const west = x / n * 360 - 180, east = (x + 1) / n * 360 - 180;
  if (east <= TERRAIN_TILE_BOUNDS[0] || west >= TERRAIN_TILE_BOUNDS[2] || latitude(y) <= TERRAIN_TILE_BOUNDS[1] || latitude(y + 1) >= TERRAIN_TILE_BOUNDS[3]) throw new Error("Tile outside the Kansas map area.");
  const extent = 20037508.342789244, step = 2 * extent / n;
  const bbox = [-extent + x * step, extent - (y + 1) * step, -extent + (x + 1) * step, extent - y * step].join(",");
  const params = new URLSearchParams({ bbox, bboxSR: "3857", imageSR: "3857", size: "256,256", format: "png32", renderingRule: JSON.stringify({ rasterFunction: FUNCTIONS[kind] }), f: "image" });
  return { key: `${kind}/${z}/${x}/${y}`, upstream: `${ORIGIN}?${params}`, canonical: `${url.origin}/api/terrain-tile?kind=${kind}&z=${z}&x=${x}&y=${y}` };
}
export function validateTerrainPNG(bytes: Uint8Array) {
  const signature = [137, 80, 78, 71, 13, 10, 26, 10];
  if (bytes.length < 33 || bytes.length > 1_048_576 || signature.some((b, i) => bytes[i] !== b)) throw new Error("USGS did not return a PNG tile.");
  const view = new DataView(bytes.buffer, bytes.byteOffset, bytes.byteLength);
  if (view.getUint32(12) !== 0x49484452 || view.getUint32(16) !== 256 || view.getUint32(20) !== 256) throw new Error("Unexpected terrain tile dimensions.");
}
type Entry = { bytes: Uint8Array; retrievedAt: string; expires: number };
type Options = { fetchBytes?: (url: string) => Promise<Uint8Array>; now?: () => number; edgeCache?: () => Cache | undefined };
export function createTerrainTileService(options: Options = {}) {
  const now = options.now ?? Date.now;
  const fetchBytes = options.fetchBytes ?? (async (url) => (await boundedFetch(url, 1_048_576)).bytes);
  const memory = new Map<string, Entry>(), pending = new Map<string, Promise<Entry>>(); let memoryBytes = 0;
  const cacheControl = (expires: number) => { const remaining = Math.max(0, Math.floor((expires - now()) / 1000)); return `public, max-age=${Math.min(3600, remaining)}, s-maxage=${remaining}`; };
  const response = (entry: Entry, state: string) => new Response(new Uint8Array(entry.bytes), { headers: {
    "Content-Type": "image/png", "Cache-Control": cacheControl(entry.expires),
    "X-Content-Type-Options": "nosniff", "X-KFM-Tile-Cache": state,
    "X-KFM-Source": "USGS 3DEP display mosaic", "X-KFM-Retrieved-At": entry.retrievedAt,
  } });
  return async (request: Request) => {
    let tile; try { tile = terrainTileRequest(new URL(request.url)); } catch (error) { return Response.json({ error: (error as Error).message }, { status: 400, headers: { "Cache-Control": "no-store" } }); }
    const cached = memory.get(tile.key);
    if (cached && cached.expires > now()) { memory.delete(tile.key); memory.set(tile.key, cached); return response(cached, "MEMORY"); }
    if (cached) { memory.delete(tile.key); memoryBytes -= cached.bytes.byteLength; }
    const cache = options.edgeCache?.();
    const cacheKey = new Request(tile.canonical);
    try {
      const hit = await cache?.match(cacheKey);
      const expires = hit ? Date.parse(hit.headers.get("X-KFM-Retrieved-At") ?? "") + TERRAIN_TILE_TTL * 1000 : 0;
      if (hit?.ok && hit.headers.get("content-type") === "image/png" && expires > now()) { const result = new Response(hit.body, hit); result.headers.set("X-KFM-Tile-Cache", "EDGE"); result.headers.set("Cache-Control", cacheControl(expires)); return result; }
    } catch { /* The bounded memory cache remains usable if edge storage is unavailable. */ }
    const coalesced = pending.has(tile.key);
    let work = pending.get(tile.key);
    if (!work) {
      if (pending.size >= 32) return Response.json({ error: "Terrain requests are busy. Please retry the layer shortly." }, { status: 503, headers: { "Cache-Control": "no-store", "Retry-After": "5" } });
      work = (async () => {
        const bytes = await fetchBytes(tile.upstream); validateTerrainPNG(bytes);
        const entry = { bytes, retrievedAt: new Date(now()).toISOString(), expires: now() + TERRAIN_TILE_TTL * 1000 };
        while (memory.size >= 64 || memoryBytes + bytes.byteLength > 8 * 1024 * 1024) { const first = memory.keys().next().value; if (first === undefined) break; memoryBytes -= memory.get(first)!.bytes.byteLength; memory.delete(first); }
        memory.set(tile.key, entry); memoryBytes += bytes.byteLength;
        try { await cache?.put(cacheKey, response(entry, "ORIGIN")); } catch { /* Cache writes never make a valid source tile fail. */ }
        return entry;
      })(); pending.set(tile.key, work);
      void work.finally(() => pending.delete(tile.key)).catch(() => undefined);
    }
    try { return response(await work, coalesced ? "COALESCED" : "ORIGIN"); }
    catch { return Response.json({ error: "The USGS terrain tile is temporarily unavailable. Retry the layer or use display terrain; source data is available from the download notice." }, { status: 502, headers: { "Cache-Control": "no-store", "Retry-After": "5" } }); }
  };
}
