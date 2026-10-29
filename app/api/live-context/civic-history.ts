import { readBoundedText } from "../../bounded-json";
import { civicCongressForDay, civicHistoryPlan, civicHistoryRawUrl, parseCivicHistory } from "../../civic-history";
import { readCivicDistricts } from "./civic-districts";
import type { OfficialContextPayload } from "../../live-context";

const CACHE_MS = 24 * 60 * 60_000;
const UNAVAILABLE = "This congressional plan is unavailable. No other Congress was substituted. Retry after one minute.";
export function createCivicHistoryReader(fetcher: typeof fetch = fetch, clock: () => number = Date.now, census: () => Promise<OfficialContextPayload> = readCivicDistricts) {
  const cache = new Map<string, { raw: unknown; at: number }>();
  const pending = new Map<string, Promise<{ raw: unknown; at: number }>>(), retry = new Map<string, number>();
  return async function read(day: string): Promise<OfficialContextPayload> {
    const congress = civicCongressForDay(day);
    if (!congress || day > new Date(clock()).toISOString().slice(0, 10)) throw new Error("Choose a supported historical date.");
    if (congress === 119) return { ...await census(), sourceDay: day };
    const plan = civicHistoryPlan(congress);
    if (!plan) throw new Error(UNAVAILABLE);
    const key = plan.file, now = clock();
    let entry = cache.get(key);
    if (entry && (now < entry.at || now - entry.at >= CACHE_MS)) { cache.delete(key); entry = undefined; }
    if (!entry) {
      if (now < (retry.get(key) ?? 0)) throw new Error(UNAVAILABLE);
      let work = pending.get(key);
      if (!work) {
        work = (async () => {
          const controller = new AbortController(), timer = setTimeout(() => controller.abort(), 25_000);
          try {
            const response = await fetcher(civicHistoryRawUrl(plan), { signal: controller.signal, redirect: "manual", cache: "no-store", headers: { Accept: "application/json" } });
            if (!response.ok) { void response.body?.cancel().catch(() => undefined); throw new Error(UNAVAILABLE); }
            const text = await readBoundedText(response, 2 * 1024 * 1024, controller.signal);
            const hash = Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256", new TextEncoder().encode(text))), b => b.toString(16).padStart(2, "0")).join("");
            controller.signal.throwIfAborted();
            if (hash !== plan.sha256) throw new Error("Source integrity mismatch.");
            const raw: unknown = JSON.parse(text), at = clock();
            parseCivicHistory(raw, day, new Date(at));
            const result = { raw, at };
            while (cache.size >= 4) cache.delete(cache.keys().next().value!);
            cache.set(key, result); retry.delete(key); return result;
          } catch { cache.delete(key); retry.set(key, clock() + 60_000); throw new Error(UNAVAILABLE); }
          finally { clearTimeout(timer); }
        })();
        pending.set(key, work);
        const settled = () => { if (pending.get(key) === work) pending.delete(key); };
        void work.then(settled, settled);
      }
      entry = await work;
    } else { cache.delete(key); cache.set(key, entry); }
    return parseCivicHistory(entry.raw, day, new Date(entry.at));
  };
}
export const readCivicHistory = createCivicHistoryReader();
