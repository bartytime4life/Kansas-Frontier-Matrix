import { exactUtc } from "../../../event-atlas";
import {
  NEXRAD_EARLIEST_DAY,
  NEXRAD_SOURCE_PAGE,
  STORM_LIMITATION,
  STORM_LIST_BYTES,
  STORM_LOOKBACK_MS,
  STORM_PRODUCT_BYTES,
  STORM_RADARS,
  latestStormVolume,
  parseStormListing,
  parseStormProduct,
  stormFeatures,
  stormListUrl,
  stormObjectUrl,
  type StormAvailability,
  type StormFrame,
  type StormListingRow,
  type StormProduct,
  type StormProductResult,
  type StormRadarId,
  type StormRadarStatus,
} from "../../../nexrad-storms";
import { boundedFetch } from "../upstream";
export const dynamic = "force-dynamic";

// In-memory only. Nothing from the radar archive is written to storage.
const listings = new Map<string, { at: number; rows: StormListingRow[] }>();
const products = new Map<string, StormProductResult>();
const remember = <T,>(cache: Map<string, T>, key: string, value: T, limit: number) => {
  cache.delete(key); cache.set(key, value);
  while (cache.size > limit) cache.delete(cache.keys().next().value!);
};

async function listing(radar: StormRadarId, product: StormProduct, day: string) {
  const id = `${radar}:${product}:${day}`, cached = listings.get(id);
  // Recent days may still be filling in; older days are stable archive listings.
  const ttl = day >= new Date(Date.now() - 2 * 86_400_000).toISOString().slice(0, 10) ? 120_000 : 3_600_000;
  if (cached && Date.now() - cached.at < ttl) return cached.rows;
  const rows = parseStormListing((await boundedFetch(stormListUrl(radar, product, day), STORM_LIST_BYTES)).text(), radar, product, day);
  remember(listings, id, { at: Date.now(), rows }, 64);
  return rows;
}

async function product(key: string) {
  const cached = products.get(key);
  if (cached) return cached;
  const parsed = parseStormProduct((await boundedFetch(stormObjectUrl(key), STORM_PRODUCT_BYTES)).bytes, key);
  remember(products, key, parsed, 256);
  return parsed;
}

const daysBetween = (startMs: number, endMs: number) => {
  const days = new Set<string>();
  for (let t = Date.parse(new Date(startMs).toISOString().slice(0, 10) + "T00:00:00Z"); t <= endMs; t += 86_400_000) days.add(new Date(t).toISOString().slice(0, 10));
  return [...days];
};
const validTime = (value: string | null) => {
  const time = exactUtc(value ?? "");
  return time && time.slice(0, 10) >= NEXRAD_EARLIEST_DAY && Date.parse(time) <= Date.now() ? time : null;
};
const fail = (message: string, status = 400) => Response.json({ message }, { status, headers: { "Cache-Control": "no-store" } });

async function frame(time: string): Promise<StormFrame> {
  const at = Date.parse(time), days = daysBetween(at - STORM_LOOKBACK_MS, at);
  const results = await Promise.all(STORM_RADARS.map(async (radar): Promise<{ status: StormRadarStatus; parsed: StormProductResult[] }> => {
    const base = { id: radar.id, site: radar.site, name: radar.name };
    try {
      const nst = (await Promise.all(days.map((day) => listing(radar.id, "NST", day)))).flat();
      const volume = latestStormVolume(nst, time);
      if (!volume) return { status: { ...base, status: "no-scan", volumeTime: null, message: "No archived storm-tracking scan in the 12 minutes before this time." }, parsed: [] };
      const cells = await product(volume.key);
      // Rotation is optional: its failure degrades this radar to storm cells only.
      let rotation: StormProductResult | null = null, message = "Storm cells only; no rotation product for this scan";
      try {
        const nmd = (await Promise.all(days.map((day) => listing(radar.id, "NMD", day)))).flat().find((row) => row.time === volume.time);
        if (nmd) { rotation = await product(nmd.key); message = "Storm cells and rotation"; }
      } catch { message = "Storm cells only; rotation unavailable for this scan"; }
      return { status: { ...base, status: "ok", volumeTime: volume.time, message }, parsed: rotation ? [cells, rotation] : [cells] };
    } catch (error) {
      return { status: { ...base, status: "unavailable", volumeTime: null, message: error instanceof Error ? error.message : "Radar archive unavailable." }, parsed: [] };
    }
  }));
  if (results.every((result) => result.status.status === "unavailable")) throw new Error("The radar storm archive is unavailable for every Kansas radar.");
  const data = stormFeatures(results.flatMap((result) => result.parsed), time);
  const kinds = data.features.map((feature) => feature.properties ?? {});
  return {
    format: "kfm-nexrad-storms-v1", time, retrievedAt: new Date().toISOString(), radars: results.map((result) => result.status), data,
    counts: { cells: kinds.filter((p) => p.kind === "cell").length, rotations: kinds.filter((p) => p.kind === "rotation").length, tornadoSignatures: kinds.filter((p) => p.kind === "rotation" && p.tvs === true).length },
    source: NEXRAD_SOURCE_PAGE, limitation: STORM_LIMITATION, evidenceRole: "EXTERNAL_CONTEXT_ONLY",
  };
}

async function availability(start: string, end: string): Promise<StormAvailability> {
  const startMs = Date.parse(start), endMs = Date.parse(end), days = daysBetween(startMs, endMs - 1);
  const radars = await Promise.all(STORM_RADARS.map(async (radar) => {
    try {
      const rows = (await Promise.all(days.map((day) => listing(radar.id, "NST", day)))).flat();
      return { id: radar.id, status: "ok" as const, times: rows.filter((row) => Date.parse(row.time) >= startMs && Date.parse(row.time) < endMs).map((row) => row.time) };
    } catch { return { id: radar.id, status: "unavailable" as const, times: [] }; }
  }));
  if (radars.every((radar) => radar.status === "unavailable")) throw new Error("The radar storm archive is unavailable for every Kansas radar.");
  return { format: "kfm-nexrad-storm-availability-v1", start, end, radars };
}

export async function GET(request: Request) {
  const params = new URL(request.url).searchParams, keys = [...params.keys()];
  if (keys.some((key) => params.getAll(key).length !== 1)) return fail("Repeated parameters are not accepted.");
  try {
    if (keys.length === 1 && keys[0] === "time") {
      const time = validTime(params.get("time"));
      if (!time) return fail(`Choose an exact UTC time from ${NEXRAD_EARLIEST_DAY} to now.`);
      const body = await frame(time);
      const settled = Date.now() - Date.parse(time) > 86_400_000;
      return Response.json(body, { headers: { "Cache-Control": settled ? "public, max-age=3600" : "public, max-age=60", "X-Content-Type-Options": "nosniff" } });
    }
    if (keys.length === 2 && keys.includes("start") && keys.includes("end")) {
      const start = validTime(params.get("start")), end = exactUtc(params.get("end") ?? "");
      if (!start || !end || Date.parse(end) <= Date.parse(start) || Date.parse(end) - Date.parse(start) > 86_400_000) return fail("Choose an exact UTC interval of at most 24 hours.");
      return Response.json(await availability(start, end), { headers: { "Cache-Control": "public, max-age=120", "X-Content-Type-Options": "nosniff" } });
    }
    return fail("Use either ?time= or ?start=&end=.");
  } catch (error) {
    return fail(error instanceof Error ? error.message : "Radar storm archive unavailable.", 502);
  }
}
