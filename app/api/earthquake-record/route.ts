import { boundedFetch } from "../event-atlas/upstream";
import { earthquakeRecordProviderUrl, parseEarthquakeRecord, type EarthquakeRecord } from "../../earthquake-record";

export const dynamic = "force-dynamic";
const MAX_BYTES = 10 * 1024 * 1024;
const FRESH_MS = 6 * 60 * 60 * 1000;
let kept: { at: number; record: EarthquakeRecord } | null = null;

/** The Kansas M2.5+ record since 1973 from the USGS catalog, kept for six hours: it changes by a handful of events a month. */
export async function GET() {
  const headers = { "Cache-Control": "public, max-age=3600, s-maxage=21600", "X-Content-Type-Options": "nosniff" };
  if (kept && Date.now() - kept.at < FRESH_MS) return Response.json(kept.record, { headers });
  const now = new Date();
  const source = earthquakeRecordProviderUrl(now);
  try {
    const response = await boundedFetch(source, MAX_BYTES, { timeoutMs: 25_000 });
    // FDSN answers 204 when nothing matches.
    const body = response.text();
    const record = parseEarthquakeRecord(body ? JSON.parse(body) as unknown : { features: [] }, now.toISOString(), source);
    kept = { at: now.getTime(), record };
    return Response.json(record, { headers });
  } catch {
    return Response.json({ state: "unavailable", message: "The USGS earthquake catalog is unavailable. Try again, or search it at earthquake.usgs.gov." },
      { status: 502, headers: { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" } });
  }
}
