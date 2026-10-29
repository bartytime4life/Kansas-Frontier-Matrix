import { boundedFetch } from "../event-atlas/upstream";
import { WELL_LEVELS_MAX_PAGES, isWellSite, nextPageUrl, pageFeatures, parseWellLevels, wellLevelsProviderUrl, type WellLevels } from "../../well-levels";

export const dynamic = "force-dynamic";
const MAX_BYTES = 4 * 1024 * 1024;
const FRESH_MS = 6 * 60 * 60 * 1000;
const KEPT_WELLS = 200;
const kept = new Map<string, { at: number; levels: WellLevels }>();

/**
 * One monitoring well's measured depth to water from the USGS Water Data
 * field-measurements collection, every page up to a bound, kept six hours
 * (new measurements arrive about once a year).
 */
export async function GET(request: Request) {
  const params = new URL(request.url).searchParams;
  const site = params.get("site");
  if (!isWellSite(site) || [...params.keys()].some(key => key !== "site" || params.getAll(key).length > 1))
    return Response.json({ message: "Give one well's 15-digit USGS site number." }, { status: 400, headers: { "Cache-Control": "no-store" } });
  const headers = { "Cache-Control": "public, max-age=3600, s-maxage=21600", "X-Content-Type-Options": "nosniff" };
  const hit = kept.get(site);
  if (hit && Date.now() - hit.at < FRESH_MS) return Response.json(hit.levels, { headers });
  try {
    const source = wellLevelsProviderUrl(site);
    const features: unknown[] = [];
    let url: string | null = source, pages = 0;
    while (url && pages < WELL_LEVELS_MAX_PAGES) {
      const page = JSON.parse((await boundedFetch(url, MAX_BYTES, { timeoutMs: 20_000 })).text()) as unknown;
      features.push(...pageFeatures(page));
      url = nextPageUrl(page);
      pages++;
    }
    const levels = parseWellLevels(features, site, new Date().toISOString(), source, url !== null);
    if (kept.size >= KEPT_WELLS) kept.delete(kept.keys().next().value!);
    kept.set(site, { at: Date.now(), levels });
    return Response.json(levels, { headers });
  } catch {
    return Response.json({ state: "unavailable", message: "USGS Water Data did not answer for this well. Try again, or open its KGS record." },
      { status: 502, headers: { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" } });
  }
}
