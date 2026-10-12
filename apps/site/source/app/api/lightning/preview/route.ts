import { getLightningManifest, fetchLightningPng } from "../../../lightning-server";
import { NOAA_LIGHTNING_LAYER, NOAA_LIGHTNING_STYLE, NOAA_LIGHTNING_WMS_URL } from "../../../lightning-data";

export const dynamic = "force-dynamic";

export async function GET(request: Request) {
  try {
    const search = new URL(request.url).searchParams;
    const frame = search.get("time") ?? "";
    const manifest = await getLightningManifest();
    if (!manifest.frames.includes(frame)) return new Response("Frame not advertised", { status: 400 });
    const bbox = (search.get("bbox") ?? "").split(",").map(Number);
    if (bbox.length !== 4 || bbox.some((value) => !Number.isFinite(value))) return new Response("Invalid view bounds", { status: 400 });
    const [west, south, east, north] = bbox;
    if (west < -180 || east > 180 || south < -25 || north > 80 || east <= west || north <= south || east - west > 40 || north - south > 25) return new Response("View outside bounded preview", { status: 400 });
    const params = new URLSearchParams({ SERVICE: "WMS", VERSION: "1.1.1", REQUEST: "GetMap", LAYERS: NOAA_LIGHTNING_LAYER, STYLES: NOAA_LIGHTNING_STYLE, FORMAT: "image/png", TRANSPARENT: "TRUE", SRS: "EPSG:4326", BBOX: bbox.join(","), WIDTH: "256", HEIGHT: "256", TIME: frame });
    const bytes = await fetchLightningPng(`${NOAA_LIGHTNING_WMS_URL}?${params}`);
    return new Response(new Uint8Array(bytes).buffer, { headers: { "Content-Type": "image/png", "Cache-Control": "public, max-age=120", "X-Content-Type-Options": "nosniff" } });
  } catch (error) {
    console.error("NOAA lightning preview request failed", error);
    return new Response("Lightning preview unavailable", { status: 502, headers: { "Cache-Control": "no-store" } });
  }
}
