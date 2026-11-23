import { boundedFetch } from "../event-atlas/upstream";
import {
  DROUGHT_SERIES_REFRESH_MS, DROUGHT_SERIES_RETRY_MS, latestUsdmDate, nextUsdmDate, parseUsdmSeries,
  previousUsdmDate, usdmSeriesProviderUrl, USDM_FIRST_DATE, USDM_SERIES_AREAS,
  type DroughtSeries, type DroughtSeriesFailure,
} from "../../drought-monitor";

export const dynamic = "force-dynamic";
const MAX_BYTES = 2 * 1024 * 1024;
type SeriesRead = Readonly<{ series: DroughtSeries } | { reason: DroughtSeriesFailure }>;
let kept: { at: number; series: DroughtSeries } | null = null;
let failed: { at: number; reason: DroughtSeriesFailure } | null = null;
let pending: Promise<SeriesRead> | null = null;

function completeHistory(series: DroughtSeries, minimumLastDate: string) {
  const weeks = series.weeks, last = weeks.at(-1);
  return weeks[0]?.date === USDM_FIRST_DATE && last !== undefined && last.date >= minimumLastDate
    && weeks.every((week, index) => index === 0 || week.date === nextUsdmDate(weeks[index - 1].date));
}

/**
 * The source should cover every Tuesday from the first map to the newest.
 * Allow one week of publication delay, while guarding against regression
 * beyond the last verified archive. Dates establish coverage, so values may
 * still change when the provider corrects an existing week.
 */
async function readSeries(): Promise<SeriesRead> {
  const now = new Date(Date.now());
  const expected = previousUsdmDate(latestUsdmDate(now));
  const previouslyCovered = kept?.series.weeks.at(-1)?.date;
  const minimumLastDate = previouslyCovered && previouslyCovered > expected ? previouslyCovered : expected;
  let reason: DroughtSeriesFailure = "unavailable";
  for (const area of USDM_SERIES_AREAS) {
    const source = usdmSeriesProviderUrl(now, area);
    let response;
    try { response = await boundedFetch(source, MAX_BYTES, { timeoutMs: 20_000 }); }
    catch { return { reason }; } // A provider that does not answer is not asked twice.
    let series;
    try { series = parseUsdmSeries(response.text(), now.toISOString(), source); }
    catch { continue; }
    if (completeHistory(series, minimumLastDate)) return { series };
    reason = "incomplete";
  }
  return { reason };
}

export async function GET() {
  const headers = { "Cache-Control": "public, max-age=3600, s-maxage=21600", "X-Content-Type-Options": "nosniff" };
  if (kept && Date.now() - kept.at < DROUGHT_SERIES_REFRESH_MS) return Response.json(kept.series, { headers });
  if (!failed || Date.now() - failed.at >= DROUGHT_SERIES_RETRY_MS) {
    pending ??= readSeries().finally(() => { pending = null; });
    const result = await pending;
    if ("series" in result) {
      kept = { at: Date.now(), series: result.series };
      failed = null;
      return Response.json(result.series, { headers });
    }
    failed = { at: Date.now(), reason: result.reason };
  }
  const { reason } = failed;
  if (kept) return Response.json({ ...kept.series, retained: reason }, { headers: { ...headers, "Cache-Control": "public, max-age=300" } });
  // The site's host replaces the body of a 502 with its own page; 503 keeps this message.
  return Response.json({ state: "unavailable", reason, message: reason === "incomplete"
    ? "The Drought Monitor returned an incomplete Kansas history. The weekly map still shows its measured shares."
    : "The Drought Monitor statistics are unavailable. The weekly map still shows its measured shares." },
    { status: 503, headers: { ...headers, "Cache-Control": "no-store" } });
}
