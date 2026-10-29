import { boundedFetch } from "../../event-atlas/upstream";
import { isQpfHours, isRainfallHours, parseRainfallLegend, QPF_LEGEND_PROVIDER_URL, rainfallLegendProviderUrl, type RainfallLegend, type RainfallView } from "../../../mrms-rainfall";

export const dynamic = "force-dynamic";
const MAX_BYTES = 1024 * 1024;
const FRESH_MS = 24 * 60 * 60 * 1000;
const kept = new Map<string, { at: number; legend: RainfallLegend }>();

/**
 * The NWS service's own legend for one rainfall view: an MRMS window (1–72
 * hours, observed) or a WPC forecast window (6 hours to 7 days). Kept a day:
 * the classes rarely change.
 */
export async function GET(request: Request) {
  const params = new URL(request.url).searchParams;
  const kind = params.get("kind") ?? "observed", hours = Number(params.get("hours"));
  const noStore = { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" };
  const view: RainfallView | null = kind === "observed" && isRainfallHours(hours) ? { kind, hours } : kind === "forecast" && isQpfHours(hours) ? { kind, hours } : null;
  if (!view) return Response.json({ state: "error", message: "Choose observed rain (1, 3, 6, 12, 24, 48 or 72 hours) or a forecast (6, 24, 48, 72, 120 or 168 hours)." }, { status: 400, headers: noStore });
  const headers = { "Cache-Control": "public, max-age=3600, s-maxage=86400", "X-Content-Type-Options": "nosniff" };
  const key = `${view.kind}:${view.hours}`;
  const cached = kept.get(key);
  if (cached && Date.now() - cached.at < FRESH_MS) return Response.json(cached.legend, { headers });
  try {
    const response = await boundedFetch(view.kind === "observed" ? rainfallLegendProviderUrl(view.hours) : QPF_LEGEND_PROVIDER_URL, MAX_BYTES, { timeoutMs: 15_000 });
    const legend = parseRainfallLegend(JSON.parse(response.text()) as unknown, view, new Date().toISOString());
    kept.set(key, { at: Date.now(), legend });
    return Response.json(legend, { headers });
  } catch {
    return Response.json({ state: "unavailable", message: "The rainfall legend is unavailable; the map may still draw." }, { status: 502, headers: noStore });
  }
}
