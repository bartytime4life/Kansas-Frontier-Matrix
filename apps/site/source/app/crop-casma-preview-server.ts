import { readBoundedText } from "./bounded-json";

const BASE = "https://cloud.csiss.gmu.edu/smap_server/cgi-bin/mapserv";
const LIMIT = 2 * 1024 * 1024;
const headers = { "Cache-Control": "private, max-age=300", "X-Content-Type-Options": "nosniff" };
let cached: { days: string[]; expires: number } | undefined;
let pending: Promise<string[]> | undefined;
export function previewDays(xml: string, year: number, today = new Date().toISOString().slice(0, 10)) {
  if (!xml.includes("<WMS_Capabilities")) throw new Error("Invalid capabilities");
  return [...new Set([...xml.matchAll(/<Name>SMAP-HYB-1KM-DAILY_(20\d{2})\.(\d{2})\.(\d{2})_PM<\/Name>/g)]
    .map(m => `${m[1]}-${m[2]}-${m[3]}`).filter(day => Number(day.slice(0, 4)) === year && day <= today && Number.isFinite(Date.parse(day)) && new Date(day).toISOString().slice(0, 10) === day))].sort().reverse();
}
function providerUrl(year: number, params: Record<string, string>) {
  return `${BASE}?${new URLSearchParams({ SERVICE: "WMS", VERSION: "1.3.0", MAP: `/WMS/SMAP-HYB-1KM-DAILY_${year}.map`, ...params })}`;
}
async function provider(url: string, media: string) {
  const response = await fetch(url, { redirect: "manual", signal: AbortSignal.timeout(12_000), headers: { Accept: media } });
  if (!response.ok || !response.headers.get("content-type")?.includes(media) || Number(response.headers.get("content-length")) > LIMIT) {
    void response.body?.cancel(); throw new Error("Provider unavailable");
  }
  return response;
}
async function advertisedDays() {
  if (cached && cached.expires > Date.now()) return cached.days;
  if (!pending) pending = (async () => {
    const year = new Date().getUTCFullYear();
    for (const candidate of [year, year - 1]) {
      const response = await provider(providerUrl(candidate, { REQUEST: "GetCapabilities" }), "xml");
      const days = previewDays(await readBoundedText(response, LIMIT), candidate);
      if (days.length) { cached = { days, expires: Date.now() + 900_000 }; return days; }
    }
    throw new Error("No advertised day");
  })().finally(() => { pending = undefined; });
  return pending;
}
export async function cropCasmaPreview(request: Request) {
  const params = new URL(request.url).searchParams;
  const day = params.get("day");
  if ([...params.keys()].some(key => key !== "day") || params.getAll("day").length > 1 || day !== null && !/^20\d{2}-\d{2}-\d{2}$/.test(day)) return Response.json({ state: "error", code: "INVALID_REQUEST" }, { status: 400 });
  try {
    const days = await advertisedDays();
    if (day === null) return Response.json({ state: "available", mode: "preview", day: days[0], availableDays: days, role: "EXTERNAL_CONTEXT_ONLY" }, { headers });
    if (!days.includes(day)) return Response.json({ state: "error", code: "DAY_NOT_ADVERTISED" }, { status: 404, headers });
    // WMS 1.3 EPSG:4326 uses latitude,longitude axis order. The browser
    // reprojects image rows into Mercator; the provider does not support 3857.
    const response = await provider(providerUrl(Number(day.slice(0, 4)), { REQUEST: "GetMap", LAYERS: `SMAP-HYB-1KM-DAILY_${day.replaceAll("-", ".")}_PM`, CRS: "EPSG:4326", FORMAT: "image/png", TRANSPARENT: "true", BBOX: "36.95,-102.1,40.05,-94.55", WIDTH: "1024", HEIGHT: "512" }), "image/png");
    const reader = response.body?.getReader(); if (!reader) throw new Error("Missing image");
    const chunks: Uint8Array[] = []; let length = 0;
    try { while (true) { const { done, value } = await reader.read(); if (done) break; length += value.length; if (length > LIMIT) throw new Error("Image too large"); chunks.push(value); } }
    catch (error) { void reader.cancel(); throw error; } finally { reader.releaseLock(); }
    const bytes = new Uint8Array(length); let offset = 0; for (const chunk of chunks) { bytes.set(chunk, offset); offset += chunk.length; }
    const view = new DataView(bytes.buffer);
    if (length < 33 || ![137,80,78,71,13,10,26,10].every((v, i) => bytes[i] === v) || view.getUint32(8) !== 13 || view.getUint32(12) !== 0x49484452 || view.getUint32(16) !== 1024 || view.getUint32(20) !== 512) throw new Error("Invalid image");
    return new Response(bytes, { headers: { ...headers, "Content-Type": "image/png" } });
  } catch (error) { console.info("crop_casma_preview", error instanceof Error ? error.message : "Provider error"); return Response.json({ state: "error", code: "PROVIDER_PREVIEW_UNAVAILABLE" }, { status: 502, headers: { "Cache-Control": "no-store" } }); }
}
