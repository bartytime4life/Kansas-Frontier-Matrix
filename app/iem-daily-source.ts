import { boundedFetch } from "./api/event-atlas/upstream";

/** IEM requests sequential access and a two-second gap. Shared by GDD and frost
 * routes in this process. Multiple processes still need an egress-wide limiter.
 * Equal in-flight requests share bytes; failed responses are never cached.
 */
export function createDailyReader(
  read: (url: string) => Promise<string>,
  now = Date.now,
  pause = (ms: number) => new Promise<void>(resolve => setTimeout(resolve, ms)),
) {
  let tail: Promise<unknown> = Promise.resolve(), finished = -Infinity;
  const pending = new Map<string, Promise<string>>();
  return (url: string): Promise<string> => {
    const existing = pending.get(url);
    if (existing) return existing;
    if (pending.size >= 4) return Promise.reject(new Error("Daily source queue is full."));
    const task = tail.then(async () => {
      const wait = Math.max(0, finished + 2100 - now());
      if (wait) await pause(wait);
      try { return await read(url); } finally { finished = now(); }
    });
    pending.set(url, task);
    tail = task.catch(() => undefined);
    void task.finally(() => pending.delete(url)).catch(() => undefined);
    return task;
  };
}

export const fetchDailySummary = createDailyReader(async url =>
  (await boundedFetch(url, 512 * 1024, { timeoutMs: 15_000, cache: "no-store" })).text());
