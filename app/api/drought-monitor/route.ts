import { boundedFetch } from "../event-atlas/upstream";
import { isUsdmDate, latestUsdmDate, parseUsdmMap, previousUsdmDate, usdmMapProviderUrl, type DroughtMap } from "../../drought-monitor";

export const dynamic = "force-dynamic";
// The national map, before it is cut to Kansas.
const MAX_BYTES = 40 * 1024 * 1024;
const LATEST_FRESH_MS = 60 * 60 * 1000;
const KEPT_WEEKS = 16;
const kept = new Map<string, { at: number; map: DroughtMap }>();
const remember = (map: DroughtMap) => {
  kept.delete(map.date);
  kept.set(map.date, { at: Date.now(), map });
  while (kept.size > KEPT_WEEKS) kept.delete(kept.keys().next().value!);
};

// Each national map is 9 to 15 MB to download and parse. Visitors who ask for the same week share one read,
// at most two weeks are read at once, and a short line waits behind them, so many requests for different
// weeks cannot each hold a national map in memory at the same moment.
const MAX_READS = 2, MAX_WAITING = 12;
const pending = new Map<string, Promise<DroughtMap>>();
const waiting: (() => void)[] = [];
let reading = 0;
class Busy extends Error {}
const turn = (): Promise<void> | void => {
  if (reading < MAX_READS) { reading++; return; }
  if (waiting.length >= MAX_WAITING) throw new Busy();
  return new Promise<void>(resolve => { waiting.push(resolve); });
};
// A finished read hands its place to the next in line, so the count never passes the limit in between.
const done = () => { const next = waiting.shift(); if (next) next(); else reading--; };
function readWeek(date: string, now: Date): Promise<DroughtMap> {
  let shared = pending.get(date);
  if (!shared) {
    shared = (async () => {
      await turn();
      try {
        const source = usdmMapProviderUrl(date);
        const response = await boundedFetch(source, MAX_BYTES, { timeoutMs: 30_000 });
        const map = parseUsdmMap(JSON.parse(response.text()) as unknown, date, now.toISOString(), source);
        remember(map);
        return map;
      } finally { done(); }
    })().finally(() => { pending.delete(date); });
    pending.set(date, shared);
  }
  return shared;
}

/**
 * One week's U.S. Drought Monitor map, cut to the region around Kansas: the
 * week asked for (a Tuesday, "YYYYMMDD"), or the newest released. A past week
 * is kept as published; the newest is read again hourly, and when its
 * Thursday release is late (a holiday) the week before is answered.
 */
export async function GET(request: Request) {
  const asked = new URL(request.url).searchParams.get("date");
  const now = new Date(), latest = latestUsdmDate(now);
  const noStore = { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" };
  if (asked !== null && (!isUsdmDate(asked) || asked > latest))
    return Response.json({ state: "error", message: "Choose a Drought Monitor week: a Tuesday from 2000-01-04 to the newest released map." }, { status: 400, headers: noStore });
  const candidates = asked ? [asked] : [latest, previousUsdmDate(latest)];
  for (const date of candidates) {
    const past = date !== latest;
    const headers = { "Cache-Control": past && asked ? "public, max-age=86400, s-maxage=604800" : "public, max-age=1800, s-maxage=3600", "X-Content-Type-Options": "nosniff" };
    const cached = kept.get(date);
    if (cached && (past || Date.now() - cached.at < LATEST_FRESH_MS)) return Response.json(cached.map, { headers });
    try {
      return Response.json(await readWeek(date, now), { headers });
    } catch (error) {
      if (error instanceof Busy)
        return Response.json({ state: "unavailable", message: "The Drought Monitor is reading other weeks. Try again in a moment." }, { status: 503, headers: { ...noStore, "Retry-After": "3" } });
      /* Not released yet, or unavailable: the week before is tried when the newest was asked for. */
    }
  }
  return Response.json({ state: "unavailable", message: "The Drought Monitor map is unavailable. Try again, or open it at droughtmonitor.unl.edu." }, { status: 502, headers: noStore });
}
