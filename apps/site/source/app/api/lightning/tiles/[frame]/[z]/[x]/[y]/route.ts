import { getLightningManifest, fetchLightningPng } from "../../../../../../../lightning-server";
import { lightningWmsUrl } from "../../../../../../../lightning-data";

export const dynamic = "force-dynamic";
type Params = { params: Promise<{ frame: string; z: string; x: string; y: string }> };

export async function GET(_request: Request, context: Params) {
  try {
    const { frame, z, x, y } = await context.params;
    const manifest = await getLightningManifest();
    if (!manifest.frames.includes(frame)) return new Response("Frame not advertised by NOAA", { status: 400 });
    let url: string;
    try { url = lightningWmsUrl(frame, Number(z), Number(x), Number(y)); }
    catch { return new Response("Invalid lightning tile coordinates", { status: 400 }); }
    const bytes = await fetchLightningPng(url);
    return new Response(new Uint8Array(bytes).buffer, { headers: { "Content-Type": "image/png", "Cache-Control": "public, max-age=120", "X-Content-Type-Options": "nosniff" } });
  } catch (error) {
    console.error("NOAA lightning tile request failed", error);
    return new Response("Lightning tile unavailable", { status: 502, headers: { "Cache-Control": "no-store" } });
  }
}
