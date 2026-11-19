import { readBoundedJson } from "../../bounded-json";
import { parseDeflock, DEFLOCK_MAX_RECORDS } from "../../deflock";
import type { OfficialContextPayload } from "../../live-context";

// Fixed statewide query: no client coordinates, arbitrary query, provider URL or OSM user data.
export const DEFLOCK_QUERY = `[out:json][timeout:20][maxsize:8388608];area["ISO3166-2"="US-KS"]["admin_level"="4"]->.ks;.ks out ids;node(area.ks)["man_made"="surveillance"]["surveillance:type"="ALPR"];out body ${DEFLOCK_MAX_RECORDS + 1};`;
const PROVIDER_URL = `https://overpass-api.de/api/interpreter?${new URLSearchParams({ data: DEFLOCK_QUERY })}`;
export const DEFLOCK_CACHE_MS = 60 * 60_000;
// Each consecutive provider failure doubles the wait before the next attempt,
// up to 15 minutes. Any success resets it.
const FAILURE_COOLDOWN_MS = 60_000;
const MAX_FAILURE_COOLDOWN_MS = 15 * 60_000;
export const deflockCooldownMs = (failures: number) => Math.min(MAX_FAILURE_COOLDOWN_MS, FAILURE_COOLDOWN_MS * 2 ** Math.max(0, failures - 1));
const errorMessage = (waitMs: number) => `DeFlock / OpenStreetMap reports are unavailable. No camera locations or absence claim can be inferred. Next provider check in about ${Math.max(1, Math.ceil(waitMs / 60_000))} minute${Math.ceil(waitMs / 60_000) > 1 ? "s" : ""}.`;
const recheckMessage = "DeFlock / OpenStreetMap reports are unavailable. No camera locations or absence claim can be inferred. Next provider check is running now; try again in about a minute.";

/** One bounded shared read per process; cache only the generalized public projection. */
export function createDeflockReader(fetcher: typeof fetch = fetch, clock: () => number = Date.now) {
  let cached: { at: number; payload: OfficialContextPayload } | null = null;
  let inFlight: Promise<OfficialContextPayload> | null = null;
  let retryAt = 0, failures = 0;
  return async function readDeflock(): Promise<OfficialContextPayload> {
    const now = clock();
    if (cached && now >= cached.at && now - cached.at < DEFLOCK_CACHE_MS) return cached.payload;
    // Cold and recovery checks have no prior successful snapshot to refresh.
    const background = cached === null;
    if (inFlight) {
      if (background) throw new Error(recheckMessage);
      return inFlight;
    }
    if (now < retryAt) throw new Error(errorMessage(retryAt - now));
    // Reserve the shared slot before calling a fetcher that could throw synchronously.
    const attempt = Promise.resolve().then(async () => {
      const controller = new AbortController(), timer = setTimeout(() => controller.abort(), 25_000);
      try {
        const response = await fetcher(PROVIDER_URL, { signal: controller.signal, redirect: "manual", cache: "no-store",
          headers: { Accept: "application/json", "User-Agent": "KansasFrontierMatrix/1.0 (https://kansasfrontiermatrix.com)" } });
        if (!response.ok) {
          void response.body?.cancel().catch(() => undefined);
          throw new Error("upstream status");
        }
        const raw = await readBoundedJson(response, 2 * 1024 * 1024, controller.signal);
        const payload = parseDeflock(raw, new Date(clock()));
        cached = { at: clock(), payload }; retryAt = 0; failures = 0;
        return payload;
      } catch {
        cached = null; failures++;
        const wait = deflockCooldownMs(failures); retryAt = clock() + wait;
        throw new Error(errorMessage(wait));
      } finally { clearTimeout(timer); inFlight = null; }
    });
    inFlight = attempt;
    if (background) {
      void attempt.catch(() => {});
      throw new Error(recheckMessage);
    }
    return attempt;
  };
}
export const readDeflock = createDeflockReader();
