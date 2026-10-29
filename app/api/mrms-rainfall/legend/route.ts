import { boundedFetch } from "../../event-atlas/upstream";
import { isRainfallHours, parseRainfallLegend, rainfallLegendProviderUrl, type RainfallLegend } from "../../../mrms-rainfall";

export const dynamic = "force-dynamic";
const MAX_BYTES = 512 * 1024;
const FRESH_MS = 24 * 60 * 60 * 1000;
const kept = new Map<number, { at: number; legend: RainfallLegend }>();

/** The NWS MRMS service's own legend for one rainfall window (1–72 hours), kept a day: the classes rarely change. */
export async function GET(request: Request) {
  const hours = Number(new URL(request.url).searchParams.get("hours"));
  const noStore = { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" };
  if (!isRainfallHours(hours)) return Response.json({ state: "error", message: "Choose a rainfall window: 1, 3, 6, 12, 24, 48 or 72 hours." }, { status: 400, headers: noStore });
  const headers = { "Cache-Control": "public, max-age=3600, s-maxage=86400", "X-Content-Type-Options": "nosniff" };
  const cached = kept.get(hours);
  if (cached && Date.now() - cached.at < FRESH_MS) return Response.json(cached.legend, { headers });
  try {
    const response = await boundedFetch(rainfallLegendProviderUrl(hours), MAX_BYTES, { timeoutMs: 15_000 });
    const legend = parseRainfallLegend(JSON.parse(response.text()) as unknown, hours, new Date().toISOString());
    kept.set(hours, { at: Date.now(), legend });
    return Response.json(legend, { headers });
  } catch {
    return Response.json({ state: "unavailable", message: "The MRMS legend is unavailable; the rainfall map may still draw." }, { status: 502, headers: noStore });
  }
}
