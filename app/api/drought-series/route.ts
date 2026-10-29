import { boundedFetch } from "../event-atlas/upstream";
import { parseUsdmSeries, usdmSeriesProviderUrl, type DroughtSeries } from "../../drought-monitor";

export const dynamic = "force-dynamic";
const MAX_BYTES = 2 * 1024 * 1024;
const FRESH_MS = 6 * 60 * 60 * 1000;
let kept: { at: number; series: DroughtSeries } | null = null;

/**
 * Kansas's weekly share of area in each Drought Monitor category, from the
 * first map in January 2000 to the newest, as the USDM data services compute
 * it. Read again every six hours; a new week arrives each Thursday.
 */
export async function GET() {
  const headers = { "Cache-Control": "public, max-age=3600, s-maxage=21600", "X-Content-Type-Options": "nosniff" };
  if (kept && Date.now() - kept.at < FRESH_MS) return Response.json(kept.series, { headers });
  const now = new Date(), source = usdmSeriesProviderUrl(now);
  try {
    const response = await boundedFetch(source, MAX_BYTES, { timeoutMs: 20_000 });
    const series = parseUsdmSeries(response.text(), now.toISOString(), source);
    kept = { at: now.getTime(), series };
    return Response.json(series, { headers });
  } catch {
    return Response.json({ state: "unavailable", message: "The Drought Monitor statistics are unavailable. The weekly map still shows its measured shares." },
      { status: 502, headers: { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" } });
  }
}
