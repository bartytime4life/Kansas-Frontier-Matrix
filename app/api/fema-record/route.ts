import { boundedFetch } from "../event-atlas/upstream";
import { FEMA_RECORD_MAX_PAGES, FEMA_RECORD_PAGE_SIZE, FEMA_RECORD_SOURCE, femaRecordPageUrl, parseFemaRecord, type FemaRecord } from "../../fema-record";

export const dynamic = "force-dynamic";
const PAGE_BYTES = 4 * 1024 * 1024;
const FRESH_MS = 12 * 60 * 60 * 1000;
let kept: { at: number; record: FemaRecord } | null = null;

/**
 * Every Kansas FEMA declaration since 1953, read from OpenFEMA a page at a
 * time and gathered by disaster number. Kept for twelve hours: declarations
 * arrive a few times a year.
 */
export async function GET() {
  const headers = { "Cache-Control": "public, max-age=3600, s-maxage=43200", "X-Content-Type-Options": "nosniff" };
  if (kept && Date.now() - kept.at < FRESH_MS) return Response.json(kept.record, { headers });
  const now = new Date();
  try {
    const rows: unknown[] = [];
    let truncated = true;
    for (let page = 0; page < FEMA_RECORD_MAX_PAGES; page++) {
      const response = await boundedFetch(femaRecordPageUrl(page), PAGE_BYTES, { timeoutMs: 20_000 });
      const body = JSON.parse(response.text()) as { DisasterDeclarationsSummaries?: unknown };
      if (!Array.isArray(body.DisasterDeclarationsSummaries)) throw new Error("OpenFEMA answered without declaration rows.");
      rows.push(...body.DisasterDeclarationsSummaries);
      if (body.DisasterDeclarationsSummaries.length < FEMA_RECORD_PAGE_SIZE) { truncated = false; break; }
    }
    const record = parseFemaRecord(rows, now.toISOString(), FEMA_RECORD_SOURCE, truncated);
    if (!record.disasters.length) throw new Error("OpenFEMA answered no Kansas declarations.");
    kept = { at: now.getTime(), record };
    return Response.json(record, { headers });
  } catch {
    return Response.json({ state: "unavailable", message: "OpenFEMA is unavailable. Try again, or search declarations at fema.gov/disaster/declarations." },
      { status: 502, headers: { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" } });
  }
}
