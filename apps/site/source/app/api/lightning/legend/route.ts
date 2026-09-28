import { fetchLightningPng } from "../../../lightning-server";
import { NOAA_LIGHTNING_LEGEND_URL } from "../../../lightning-data";

export const dynamic = "force-dynamic";

export async function GET() {
  try {
    const bytes = await fetchLightningPng(NOAA_LIGHTNING_LEGEND_URL);
    return new Response(new Uint8Array(bytes).buffer, { headers: {
      "Content-Type": "image/png", "Cache-Control": "public, max-age=3600", "X-Content-Type-Options": "nosniff",
    } });
  } catch (error) {
    console.error("NOAA lightning legend request failed", error);
    return new Response("NOAA lightning legend unavailable", { status: 502, headers: { "Cache-Control": "no-store" } });
  }
}
