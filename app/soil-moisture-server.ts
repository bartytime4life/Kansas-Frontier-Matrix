import { readBoundedText } from "./bounded-json";
import { commonSoilDays, parseSoilAvailability, SOIL_VIEWS, validSoilDay, type SoilView } from "./soil-moisture";

const CAPABILITIES = "https://gibs.earthdata.nasa.gov/wmts/epsg3857/best/1.0.0/WMTSCapabilities.xml";
const TTL_MS = 15 * 60_000;
const TIMEOUT_MS = 12_000;
const MAX_CAPABILITIES_BYTES = 8 * 1024 * 1024;
const MAX_TILE_BYTES = 1024 * 1024;
type Availability = { availableDays: string[]; daysByView: Record<SoilView, string[]>; latestCommonDay: string | null; checkedAt: string };
let cached: { value: Availability; expires: number } | null = null;
let pending: Promise<Availability> | null = null;

export class SoilSourceError extends Error {
  constructor(readonly code: string, readonly httpStatus = 502) { super(code); }
}

export async function boundedNasaFetch(url: string, accept: string, maxBytes: number): Promise<Response> {
  try {
    // The signal remains attached while callers read the body, not just until headers arrive.
    const response = await fetch(url, { cache: "no-store", redirect: "manual", signal: AbortSignal.timeout(TIMEOUT_MS), headers: { Accept: accept } });
    if (response.status >= 300 && response.status < 400) throw new SoilSourceError("NASA_REDIRECT_REJECTED");
    if (!response.ok) throw new SoilSourceError("NASA_HTTP_ERROR");
    const size = Number(response.headers.get("content-length"));
    if (Number.isFinite(size) && size > maxBytes) throw new SoilSourceError("NASA_RESPONSE_TOO_LARGE");
    return response;
  } catch (error) {
    if (error instanceof SoilSourceError) throw error;
    if (error instanceof Error && (error.name === "AbortError" || error.name === "TimeoutError")) throw new SoilSourceError("NASA_TIMEOUT", 504);
    throw new SoilSourceError("NASA_NETWORK_ERROR");
  }
}

export async function soilAvailability(force = false): Promise<{ value: Availability; cache: "hit" | "miss" }> {
  if (!force && cached && cached.expires > Date.now()) return { value: cached.value, cache: "hit" };
  if (!pending) pending = (async () => {
    const response = await boundedNasaFetch(CAPABILITIES, "application/xml", MAX_CAPABILITIES_BYTES);
    if (!/xml/i.test(response.headers.get("content-type") ?? "")) throw new SoilSourceError("NASA_UNEXPECTED_CONTENT");
    let xml: string;
    try { xml = await readBoundedText(response, MAX_CAPABILITIES_BYTES); }
    catch (error) { throw new SoilSourceError(error instanceof Error && (error.name === "AbortError" || error.name === "TimeoutError") ? "NASA_TIMEOUT" : "NASA_MALFORMED_OR_OVERSIZED", error instanceof Error && (error.name === "AbortError" || error.name === "TimeoutError") ? 504 : 502); }
    let daysByView: Record<SoilView, string[]>;
    try { daysByView = parseSoilAvailability(xml); }
    catch { throw new SoilSourceError("NASA_CAPABILITIES_MISMATCH"); }
    const availableDays = commonSoilDays(daysByView);
    return { daysByView, availableDays, latestCommonDay: availableDays[0] ?? null, checkedAt: new Date().toISOString() };
  })().finally(() => { pending = null; });
  const value = await pending;
  cached = { value, expires: Date.now() + TTL_MS };
  return { value, cache: "miss" };
}

export function parseTileRequest(url: string): { view: SoilView; day: string; z: number; x: number; y: number } {
  const p = new URL(url).searchParams;
  if ([...p.keys()].some(k => !["view", "day", "z", "x", "y"].includes(k) || p.getAll(k).length !== 1)) throw new SoilSourceError("INVALID_TILE_REQUEST", 400);
  if (["view", "day", "z", "x", "y"].some(k => !p.has(k))) throw new SoilSourceError("INVALID_TILE_REQUEST", 400);
  const view = p.get("view") as SoilView, day = p.get("day") ?? "";
  const coords = ["z", "x", "y"].map(k => p.get(k) ?? "");
  if (!(view in SOIL_VIEWS) || !validSoilDay(day) || coords.some(v => !/^\d+$/.test(v))) throw new SoilSourceError("INVALID_TILE_REQUEST", 400);
  const [z, x, y] = coords.map(Number), n = 2 ** z;
  if (![z, x, y].every(Number.isSafeInteger) || z < 0 || z > 6 || x >= n || y >= n) throw new SoilSourceError("INVALID_TILE_REQUEST", 400);
  return { view, day, z, x, y };
}

export async function soilTileBytes(view: SoilView, day: string, z: number, x: number, y: number): Promise<Uint8Array> {
  const layer = SOIL_VIEWS[view].layer;
  const url = `https://gibs.earthdata.nasa.gov/wmts/epsg3857/best/${layer}/default/${day}/GoogleMapsCompatible_Level6/${z}/${y}/${x}.png`;
  const response = await boundedNasaFetch(url, "image/png", MAX_TILE_BYTES);
  if (!/^image\/png(?:;|$)/i.test(response.headers.get("content-type") ?? "")) throw new SoilSourceError("NASA_UNEXPECTED_CONTENT");
  let bytes: Uint8Array;
  try {
    const reader = response.body?.getReader();
    if (!reader) throw new Error();
    const chunks: Uint8Array[] = []; let length = 0;
    while (true) { const { value, done } = await reader.read(); if (done) break; length += value.length; if (length > MAX_TILE_BYTES) { await reader.cancel(); throw new Error(); } chunks.push(value); }
    bytes = new Uint8Array(length); let offset = 0;
    for (const chunk of chunks) { bytes.set(chunk, offset); offset += chunk.length; }
  } catch (error) { throw new SoilSourceError(error instanceof Error && (error.name === "AbortError" || error.name === "TimeoutError") ? "NASA_TIMEOUT" : "NASA_MALFORMED_OR_OVERSIZED", error instanceof Error && (error.name === "AbortError" || error.name === "TimeoutError") ? 504 : 502); }
  // GIBS WMTS tiles are 256 px PNGs. Reject an image with a forged signature
  // or implausible dimensions before forwarding it to the map decoder.
  const header = new DataView(bytes.buffer, bytes.byteOffset, bytes.byteLength);
  if (bytes.length < 33 || ![137,80,78,71,13,10,26,10].every((n, i) => bytes[i] === n)
    || header.getUint32(8) !== 13 || String.fromCharCode(...bytes.slice(12, 16)) !== "IHDR"
    || header.getUint32(16) !== 256 || header.getUint32(20) !== 256) throw new SoilSourceError("NASA_INVALID_PNG");
  return bytes;
}
