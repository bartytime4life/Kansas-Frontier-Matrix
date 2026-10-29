import { readBoundedJson } from "../../bounded-json";
import { CIVIC_SERVICE, parseCivicDistricts } from "../../civic-districts";
import type { OfficialContextPayload } from "../../live-context";

// Pin edition, state and fields. No caller-provided coordinates, SQL or upstream URL.
export const CIVIC_QUERY_URL = `${CIVIC_SERVICE}/query?${new URLSearchParams({ where: "STATE='20'", outFields: "GEOID,STATE,CDSESSN", returnGeometry: "true", outSR: "4326", geometryPrecision: "6", resultRecordCount: "5", f: "geojson" })}`;
export const CIVIC_CACHE_MS = 24 * 60 * 60_000;
const UNAVAILABLE = "The Census 119th Congress district layer is unavailable. No substitute boundaries were loaded. Retry after one minute.";

export function createCivicDistrictReader(fetcher: typeof fetch = fetch, clock: () => number = Date.now) {
  let cached: { at: number; payload: OfficialContextPayload } | null = null;
  let inFlight: Promise<OfficialContextPayload> | null = null, retryAt = 0;
  return async function readCivicDistricts(): Promise<OfficialContextPayload> {
    const now = clock();
    if (cached && now >= cached.at && now - cached.at < CIVIC_CACHE_MS) return cached.payload;
    if (inFlight) return inFlight;
    if (now < retryAt) throw new Error(UNAVAILABLE);
    inFlight = (async () => {
      const controller = new AbortController(), timer = setTimeout(() => controller.abort(), 25_000);
      try {
        const response = await fetcher(CIVIC_QUERY_URL, { signal: controller.signal, redirect: "manual", cache: "no-store", headers: { Accept: "application/geo+json, application/json" } });
        if (!response.ok) { void response.body?.cancel().catch(() => undefined); throw new Error(UNAVAILABLE); }
        const payload = parseCivicDistricts(await readBoundedJson(response, 2 * 1024 * 1024, controller.signal), new Date(clock()));
        cached = { at: clock(), payload }; retryAt = 0; return payload;
      } catch { cached = null; retryAt = clock() + 60_000; throw new Error(UNAVAILABLE); }
      finally { clearTimeout(timer); }
    })();
    try { return await inFlight; } finally { inFlight = null; }
  };
}
export const readCivicDistricts = createCivicDistrictReader();
