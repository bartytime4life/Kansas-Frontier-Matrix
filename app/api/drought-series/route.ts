import { boundedFetch } from "../event-atlas/upstream";
import { parseUsdmSeries, usdmSeriesProviderUrl, USDM_SERIES_AREAS, type DroughtSeries } from "../../drought-monitor";

export const dynamic = "force-dynamic";
const MAX_BYTES = 2 * 1024 * 1024;
const FRESH_MS = 6 * 60 * 60 * 1000;
const RETRY_MS = 5 * 60 * 1000;
let kept: { at: number; series: DroughtSeries } | null = null;
let failedAt = 0;
let pending: Promise<DroughtSeries> | null = null;

/**
 * One read of the provider. An answer that arrives but holds no Kansas weeks is asked again under the
 * state's other name; a provider that does not answer at all is not asked twice.
 */
async function readSeries(): Promise<DroughtSeries> {
  const now = new Date();
  let empty: unknown;
  for (const area of USDM_SERIES_AREAS) {
    const source = usdmSeriesProviderUrl(now, area);
    const response = await boundedFetch(source, MAX_BYTES, { timeoutMs: 20_000 });
    try { return parseUsdmSeries(response.text(), now.toISOString(), source); } catch (error) { empty = error; }
  }
  throw empty;
}

/**
 * Kansas's weekly share of area in each Drought Monitor category, from the
 * first map in January 2000 to the newest, as the USDM data services compute
 * it. Read again every six hours; a new week arrives each Thursday. When a
 * later read fails, the series already in hand is served with its own
 * retrieval time, and the provider is asked again after five minutes.
 */
export async function GET() {
  const headers = { "Cache-Control": "public, max-age=3600, s-maxage=21600", "X-Content-Type-Options": "nosniff" };
  if (kept && Date.now() - kept.at < FRESH_MS) return Response.json(kept.series, { headers });
  if (Date.now() - failedAt >= RETRY_MS) {
    pending ??= readSeries().finally(() => { pending = null; });
    try {
      const series = await pending;
      kept = { at: Date.now(), series };
      failedAt = 0;
      return Response.json(series, { headers });
    } catch { failedAt = Date.now(); }
  }
  if (kept) return Response.json(kept.series, { headers: { "Cache-Control": "public, max-age=300", "X-Content-Type-Options": "nosniff" } });
  // The site's host replaces the body of a 502 with its own page; 503 keeps this message.
  return Response.json({ state: "unavailable", message: "The Drought Monitor statistics are unavailable. The weekly map still shows its measured shares." },
    { status: 503, headers: { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" } });
}
