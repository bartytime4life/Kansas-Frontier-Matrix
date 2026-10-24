import { NextResponse } from "next/server";
import { fetchJson, UpstreamError } from "./aviation-weather-server";
import { TFR_HOME, TFR_LIST_URL, UASFM_MAX_CELLS, UASFM_MAX_PAGES, UASFM_SERVICE, parseTfrList, parseUasfmPage, uasfmPageUrl, type UasCell } from "./aviation-drone-data";

const HEADERS = { "X-Content-Type-Options": "nosniff" } as const;

const failure = (code: string, error: unknown, message: string) => {
  const timeout = error instanceof UpstreamError && error.timeout;
  return NextResponse.json({ state: "error", code: `${code}_${timeout ? "TIMEOUT" : "UNAVAILABLE"}`, message, evidenceRole: "EXTERNAL_CONTEXT_ONLY" },
    { status: timeout ? 504 : 502, headers: { ...HEADERS, "Cache-Control": "no-store" } });
};

/** All Kansas-region UAS Facility Map cells, paged. Any bad page fails the whole set rather than drawing a partial grid as complete. */
export async function uasGridResponse(): Promise<NextResponse> {
  try {
    const cells: UasCell[] = [];
    let complete = false;
    for (let page = 0; page < UASFM_MAX_PAGES; page++) {
      const parsed = parseUasfmPage(await fetchJson(uasfmPageUrl(page), 8 * 1024 * 1024, 15_000));
      cells.push(...parsed.cells);
      if (cells.length > UASFM_MAX_CELLS) throw new Error("UASFM cell budget exceeded.");
      if (!parsed.more) { complete = true; break; }
    }
    if (!complete) throw new Error("UASFM paging did not finish within its page budget.");
    return NextResponse.json({ retrievedAt: new Date().toISOString(), sourceTitle: "FAA UAS Facility Maps", sourceUrl: UASFM_SERVICE, evidenceRole: "EXTERNAL_CONTEXT_ONLY",
      cells, limitation: "Maximum altitudes (ft AGL) LAANC can authorize per grid cell. A ceiling is not an authorization; outside these cells controlled airspace still needs a DroneZone request. Updated by the FAA every 56 days." },
    // The FAA republishes these grids on a 56-day cycle; a day of shared caching is ample.
    { status: 200, headers: { ...HEADERS, "Cache-Control": "public, max-age=3600, s-maxage=86400, stale-while-revalidate=3600" } });
  } catch (error) {
    return failure("AVIATION_UASFM", error, "FAA UAS Facility Map ceilings are unavailable. No partial grid was drawn.");
  }
}

export async function tfrResponse(): Promise<NextResponse> {
  try {
    const parsed = parseTfrList(await fetchJson(TFR_LIST_URL, 4 * 1024 * 1024, 12_000));
    return NextResponse.json({ retrievedAt: new Date().toISOString(), sourceTitle: "FAA Temporary Flight Restrictions", sourceUrl: TFR_HOME, evidenceRole: "EXTERNAL_CONTEXT_ONLY",
      kansas: parsed.kansas, total: parsed.total,
      limitation: "Kansas entries from the FAA's national TFR list, matched by state or text. Boundaries and times are in each NOTAM at tfr.faa.gov; a missing entry is not clearance to fly." },
    { status: 200, headers: { ...HEADERS, "Cache-Control": "public, max-age=300, stale-while-revalidate=120" } });
  } catch (error) {
    return failure("AVIATION_TFR", error, "The FAA TFR list is unavailable. Check tfr.faa.gov before flying.");
  }
}
