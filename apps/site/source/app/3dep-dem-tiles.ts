import Lerc from "lerc";
import { boundedFetch } from "./api/event-atlas/upstream";
import { TERRAIN_TILE_BOUNDS, TERRAIN_TILE_TTL } from "./terrain-tiles";

const ORIGIN = "https://elevation.nationalmap.gov/arcgis/rest/services/3DEPElevation/ImageServer/exportImage";
const MIN_ZOOM = 6;
const MAX_ZOOM = 15;
const TILE_SIZE = 256;
const MAX_LERC_BYTES = 1_048_576;
const PNG_SIGNATURE = Uint8Array.of(137, 80, 78, 71, 13, 10, 26, 10);

export function demTileRequest(url: URL) {
  const params = url.searchParams;
  if ([...params.keys()].some((key) => !["z", "x", "y"].includes(key) || params.getAll(key).length !== 1)) throw new Error("Unsupported elevation tile request.");
  const coordinates = ["z", "x", "y"].map((key) => {
    const value = params.get(key);
    if (!value || !/^\d{1,5}$/.test(value)) throw new Error("Invalid elevation tile coordinate.");
    return Number(value);
  });
  const [z, x, y] = coordinates;
  const n = 2 ** z;
  if (z < MIN_ZOOM || z > MAX_ZOOM || x >= n || y >= n) throw new Error("Elevation tile outside supported zoom range.");
  const latitude = (row: number) => Math.atan(Math.sinh(Math.PI * (1 - 2 * row / n))) * 180 / Math.PI;
  const west = x / n * 360 - 180;
  const east = (x + 1) / n * 360 - 180;
  if (east <= TERRAIN_TILE_BOUNDS[0] || west >= TERRAIN_TILE_BOUNDS[2] || latitude(y) <= TERRAIN_TILE_BOUNDS[1] || latitude(y + 1) >= TERRAIN_TILE_BOUNDS[3]) throw new Error("Elevation tile outside the Kansas map area.");
  const extent = 20037508.342789244;
  const step = 2 * extent / n;
  const bbox = [-extent + x * step, extent - (y + 1) * step, -extent + (x + 1) * step, extent - y * step].join(",");
  const upstream = new URL(ORIGIN);
  upstream.search = new URLSearchParams({ bbox, bboxSR: "3857", imageSR: "3857", size: `${TILE_SIZE},${TILE_SIZE}`, format: "lerc", pixelType: "F32", f: "image" }).toString();
  return { key: `${z}/${x}/${y}`, upstream: upstream.toString(), canonical: `${url.origin}/api/3dep-dem-tile?z=${z}&x=${x}&y=${y}` };
}

const crcTable = Uint32Array.from({ length: 256 }, (_, index) => {
  let value = index;
  for (let bit = 0; bit < 8; bit += 1) value = value & 1 ? 0xedb88320 ^ (value >>> 1) : value >>> 1;
  return value >>> 0;
});

function chunk(type: string, data: Uint8Array): Uint8Array {
  const output = new Uint8Array(12 + data.length);
  const view = new DataView(output.buffer);
  view.setUint32(0, data.length);
  for (let index = 0; index < 4; index += 1) output[4 + index] = type.charCodeAt(index);
  output.set(data, 8);
  let crc = 0xffffffff;
  for (let index = 4; index < output.length - 4; index += 1) crc = crcTable[(crc ^ output[index]) & 255] ^ (crc >>> 8);
  view.setUint32(output.length - 4, (crc ^ 0xffffffff) >>> 0);
  return output;
}

export async function lercToTerrarium(bytes: Uint8Array, decode = Lerc.decode): Promise<Uint8Array> {
  if (bytes.length < 32 || bytes.length > MAX_LERC_BYTES) throw new Error("Invalid USGS elevation response size.");
  const input = bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength) as ArrayBuffer;
  const raster = decode(input);
  if (raster.width !== TILE_SIZE || raster.height !== TILE_SIZE || raster.pixels.length !== 1 || raster.pixels[0].length !== TILE_SIZE * TILE_SIZE) throw new Error("Unexpected USGS elevation dimensions.");
  const scanline = new Uint8Array(TILE_SIZE * (1 + TILE_SIZE * 4));
  let valid = 0;
  for (let row = 0; row < TILE_SIZE; row += 1) {
    const rowStart = row * (1 + TILE_SIZE * 4);
    for (let column = 0; column < TILE_SIZE; column += 1) {
      const index = row * TILE_SIZE + column;
      const elevation = raster.pixels[0][index];
      const position = rowStart + 1 + column * 4;
      if (raster.mask && !raster.mask[index] || !Number.isFinite(elevation) || elevation < -12000 || elevation > 9000) continue;
      const encoded = Math.round((elevation + 32768) * 256);
      scanline[position] = (encoded >>> 16) & 255;
      scanline[position + 1] = (encoded >>> 8) & 255;
      scanline[position + 2] = encoded & 255;
      scanline[position + 3] = 255;
      valid += 1;
    }
  }
  if (valid === 0) throw new Error("USGS returned no usable elevation pixels.");
  const raw = scanline.buffer.slice(scanline.byteOffset, scanline.byteOffset + scanline.byteLength) as ArrayBuffer;
  const compressed = new Uint8Array(await new Response(new Blob([raw]).stream().pipeThrough(new CompressionStream("deflate"))).arrayBuffer());
  const header = new Uint8Array(13);
  const view = new DataView(header.buffer);
  view.setUint32(0, TILE_SIZE);
  view.setUint32(4, TILE_SIZE);
  header[8] = 8;
  header[9] = 6;
  const parts = [PNG_SIGNATURE, chunk("IHDR", header), chunk("IDAT", compressed), chunk("IEND", new Uint8Array())];
  const png = new Uint8Array(parts.reduce((length, part) => length + part.length, 0));
  let offset = 0;
  for (const part of parts) { png.set(part, offset); offset += part.length; }
  return png;
}

type Entry = { bytes: Uint8Array; retrievedAt: string; expires: number };
type Options = { fetchBytes?: (url: string) => Promise<Uint8Array>; now?: () => number; edgeCache?: () => Cache | undefined; convert?: typeof lercToTerrarium };
export function create3DepDemTileService(options: Options = {}) {
  const now = options.now ?? Date.now;
  const fetchBytes = options.fetchBytes ?? (async (url: string) => (await boundedFetch(url, MAX_LERC_BYTES, { timeoutMs: 12_000 })).bytes);
  const convert = options.convert ?? lercToTerrarium;
  const memory = new Map<string, Entry>();
  const pending = new Map<string, Promise<Entry>>();
  let memoryBytes = 0;
  const response = (entry: Entry, state: string) => new Response(new Uint8Array(entry.bytes), { headers: {
    "Content-Type": "image/png", "Cache-Control": `public, max-age=900, s-maxage=${Math.max(0, Math.floor((entry.expires - now()) / 1000))}`,
    "X-Content-Type-Options": "nosniff", "X-KFM-Tile-Cache": state,
    "X-KFM-Source": "USGS 3DEP bare-earth dynamic DEM; mixed source resolution", "X-KFM-Retrieved-At": entry.retrievedAt,
  } });
  return async (request: Request) => {
    let tile: ReturnType<typeof demTileRequest>;
    try { tile = demTileRequest(new URL(request.url)); }
    catch (error) { return Response.json({ error: (error as Error).message }, { status: 400, headers: { "Cache-Control": "no-store" } }); }
    const cached = memory.get(tile.key);
    if (cached && cached.expires > now()) { memory.delete(tile.key); memory.set(tile.key, cached); return response(cached, "MEMORY"); }
    if (cached) { memory.delete(tile.key); memoryBytes -= cached.bytes.byteLength; }
    const edge = options.edgeCache?.();
    const cacheKey = new Request(tile.canonical);
    try {
      const hit = await edge?.match(cacheKey);
      const expires = hit ? Date.parse(hit.headers.get("X-KFM-Retrieved-At") ?? "") + TERRAIN_TILE_TTL * 1000 : 0;
      if (hit?.ok && hit.headers.get("Content-Type") === "image/png" && expires > now()) {
        const result = new Response(hit.body, hit);
        result.headers.set("X-KFM-Tile-Cache", "EDGE");
        return result;
      }
    } catch { /* Memory cache is still available. */ }
    const coalesced = pending.has(tile.key);
    let work = pending.get(tile.key);
    if (!work) {
      if (pending.size >= 16) return Response.json({ error: "Elevation requests are busy. Please retry shortly." }, { status: 503, headers: { "Cache-Control": "no-store", "Retry-After": "5" } });
      work = (async () => {
        let bytes: Uint8Array;
        if (options.fetchBytes) bytes = await convert(await fetchBytes(tile.upstream));
        else {
          let lastError: unknown;
          let converted: Uint8Array | undefined;
          for (let attempt = 0; attempt < 2; attempt += 1) {
            try { converted = await convert(await fetchBytes(tile.upstream)); break; }
            catch (error) {
              lastError = error;
              if (attempt === 0) await new Promise((resolve) => setTimeout(resolve, 300));
            }
          }
          if (!converted) throw lastError;
          bytes = converted;
        }
        const entry = { bytes, retrievedAt: new Date(now()).toISOString(), expires: now() + TERRAIN_TILE_TTL * 1000 };
        while (memory.size >= 48 || memoryBytes + bytes.byteLength > 12 * 1024 * 1024) {
          const oldest = memory.keys().next().value;
          if (oldest === undefined) break;
          memoryBytes -= memory.get(oldest)!.bytes.byteLength;
          memory.delete(oldest);
        }
        memory.set(tile.key, entry);
        memoryBytes += bytes.byteLength;
        try { await edge?.put(cacheKey, response(entry, "ORIGIN")); } catch { /* The valid tile remains usable. */ }
        return entry;
      })();
      pending.set(tile.key, work);
      void work.finally(() => pending.delete(tile.key)).catch(() => undefined);
    }
    try { return response(await work, coalesced ? "COALESCED" : "ORIGIN"); }
    catch { return Response.json({ error: "USGS elevation is temporarily unavailable. Use fast display terrain or retry this source." }, { status: 502, headers: { "Cache-Control": "no-store", "Retry-After": "5" } }); }
  };
}
