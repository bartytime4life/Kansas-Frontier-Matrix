import { readBoundedJson } from "../../bounded-json";
import { parseDeflock, DEFLOCK_MAX_RECORDS } from "../../deflock";
import type { OfficialContextPayload } from "../../live-context";

// Fixed statewide query: no client coordinates, arbitrary query, provider URL or OSM user data.
export const DEFLOCK_QUERY = `[out:json][timeout:20][maxsize:8388608];area["ISO3166-2"="US-KS"]["admin_level"="4"]->.ks;.ks out ids;node(area.ks)["man_made"="surveillance"]["surveillance:type"="ALPR"];out body ${DEFLOCK_MAX_RECORDS + 1};`;
const PROVIDER_URL = `https://overpass-api.de/api/interpreter?${new URLSearchParams({ data: DEFLOCK_QUERY })}`;
export const DEFLOCK_CACHE_MS = 60 * 60_000;
const FAILURE_COOLDOWN_MS = 60_000;
const ERROR_MESSAGE = "DeFlock / OpenStreetMap reports are unavailable. No camera locations or absence claim can be inferred. Retry after one minute.";

/** One bounded shared read per process; cache only the generalized public projection. */
export function createDeflockReader(fetcher: typeof fetch = fetch, clock: () => number = Date.now) {
  let cached: { at: number; payload: OfficialContextPayload } | null = null;
  let inFlight: Promise<OfficialContextPayload> | null = null;
  let retryAt = 0;
  return async function readDeflock(): Promise<OfficialContextPayload> {
    const now = clock();
    if (cached && now >= cached.at && now - cached.at < DEFLOCK_CACHE_MS) return cached.payload;
    if (inFlight) return inFlight;
    if (now < retryAt) throw new Error(ERROR_MESSAGE);
    inFlight = (async () => {
      const controller = new AbortController(), timer = setTimeout(() => controller.abort(), 25_000);
      try {
        const response = await fetcher(PROVIDER_URL, { signal: controller.signal, redirect: "manual", cache: "no-store",
          headers: { Accept: "application/json", "User-Agent": "KansasFrontierMatrix/1.0 (https://kansasfrontiermatrix.com)" } });
        if (!response.ok) { void response.body?.cancel(); throw new Error(ERROR_MESSAGE); }
        const raw = await readBoundedJson(response, 2 * 1024 * 1024, controller.signal);
        const payload = parseDeflock(raw, new Date(clock()));
        cached = { at: clock(), payload }; retryAt = 0;
        return payload;
      } catch {
        cached = null; retryAt = clock() + FAILURE_COOLDOWN_MS;
        throw new Error(ERROR_MESSAGE);
      } finally { clearTimeout(timer); }
    })();
    try { return await inFlight; } finally { inFlight = null; }
  };
}
export const readDeflock = createDeflockReader();
