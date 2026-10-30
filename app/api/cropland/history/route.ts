import { boundedFetch } from "../../event-atlas/upstream";
import { CDL_YEARS, cdlValueProviderUrl, inCdlRegion, parseCdlValue, type CdlValue } from "../../../cropland";

export const dynamic = "force-dynamic";
const MAX_BYTES = 64 * 1024;
const CONCURRENCY = 4;
const FRESH_MS = 24 * 60 * 60 * 1000;
const KEPT_POINTS = 200;
const kept = new Map<string, { at: number; body: unknown }>();
const headers = { "Cache-Control": "public, max-age=86400, s-maxage=604800", "X-Content-Type-Options": "nosniff" };
const noStore = { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" };

/**
 * A point's Cropland Data Layer class in every year since 2008, read from
 * CropScape a few at a time. A year CropScape does not answer for is marked
 * failed, not empty. The whole answer is kept a day for each point.
 */
export async function GET(request: Request) {
  const params = new URL(request.url).searchParams;
  const lon = Number(params.get("lon")), lat = Number(params.get("lat"));
  if ([...params.keys()].some(key => key !== "lon" && key !== "lat") || params.get("lon") === null || params.get("lat") === null || !inCdlRegion(lon, lat))
    return Response.json({ state: "error", message: "Choose a point in or near Kansas." }, { status: 400, headers: noStore });
  // The key is the precision the answer echoes, so two clicks a metre apart never share a body that names the other's coordinates.
  const key = `${lon.toFixed(5)},${lat.toFixed(5)}`;
  const hit = kept.get(key);
  if (hit && Date.now() - hit.at < FRESH_MS) return Response.json(hit.body, { headers });
  const years: { year: number; state: "ready" | "none" | "failed"; crop: CdlValue | null }[] = [];
  const queue = [...CDL_YEARS].reverse();
  const worker = async () => {
    for (let year = queue.pop(); year !== undefined; year = queue.pop()) {
      try {
        const response = await boundedFetch(cdlValueProviderUrl(year, lon, lat), MAX_BYTES, { timeoutMs: 15_000 });
        const crop = parseCdlValue(response.text());
        years.push({ year, state: crop ? "ready" : "none", crop });
      } catch {
        years.push({ year, state: "failed", crop: null });
      }
    }
  };
  await Promise.all(Array.from({ length: CONCURRENCY }, worker));
  years.sort((a, b) => a.year - b.year);
  const body = { lon, lat, retrievedAt: new Date().toISOString(), years };
  if (kept.size >= KEPT_POINTS) kept.delete(kept.keys().next().value!);
  // Only a complete answer is kept: a partly failed history is retried on the next click rather than held for a day.
  if (years.every(y => y.state !== "failed")) kept.set(key, { at: Date.now(), body });
  return Response.json(body, { headers: years.some(y => y.state === "failed") ? noStore : headers });
}
