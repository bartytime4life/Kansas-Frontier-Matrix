import { boundedFetch } from "../event-atlas/upstream";
import { parseTornadoCsv, tornadoCsvCandidates, type TornadoRecord } from "../../tornado-record";

export const dynamic = "force-dynamic";
const MAX_BYTES = 16 * 1024 * 1024;
const FRESH_MS = 24 * 60 * 60 * 1000;
let kept: { at: number; record: TornadoRecord } | null = null;

/**
 * Kansas's tornadoes since 1950 from the SPC severe weather database: the
 * newest yearly file that answers (released each spring for the year before),
 * cut to Kansas on the server and kept a day.
 */
export async function GET() {
  const headers = { "Cache-Control": "public, max-age=3600, s-maxage=86400", "X-Content-Type-Options": "nosniff" };
  if (kept && Date.now() - kept.at < FRESH_MS) return Response.json(kept.record, { headers });
  const now = new Date();
  for (const source of tornadoCsvCandidates(now)) {
    try {
      const response = await boundedFetch(source, MAX_BYTES, { timeoutMs: 30_000 });
      const record = parseTornadoCsv(response.text(), now.toISOString(), source);
      kept = { at: Date.now(), record };
      return Response.json(record, { headers });
    } catch { /* Not released under that name yet, or unavailable: the year before is tried. */ }
  }
  return Response.json({ state: "unavailable", message: "The SPC tornado database is unavailable. Try again, or see spc.noaa.gov/wcm." },
    { status: 502, headers: { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" } });
}
