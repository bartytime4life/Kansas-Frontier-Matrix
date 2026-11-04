import { NextResponse } from "next/server";

/**
 * The hosted Node server has no shared edge cache, so each aviation route keeps
 * its last successful response in process for a short, provider-respecting
 * window, and concurrent viewers share one upstream request. Failures are
 * never cached or replayed. The body keeps its own `retrievedAt`, so a replay
 * still reports the true upstream time.
 */
type Entry = Readonly<{ at: number; body: string; status: number; headers: readonly [string, string][] }>;
export const AVIATION_CACHE_MAX_ENTRIES = 8;
export const AVIATION_CACHE_MAX_BYTES = 8 * 1024 * 1024;
const entries = new Map<string, Entry>();
const inflight = new Map<string, Promise<Entry>>();

export async function cachedAviationRoute(key: string, ttlMs: number, build: () => Promise<NextResponse>, now: () => number = Date.now): Promise<NextResponse> {
  const hit = entries.get(key);
  let entry: Entry;
  if (hit && now() >= hit.at && now() - hit.at < ttlMs) entry = hit;
  else {
    let pending = inflight.get(key);
    if (!pending) {
      pending = (async () => {
        const response = await build();
        const fresh: Entry = { at: now(), body: await response.text(), status: response.status, headers: [...response.headers.entries()] };
        if (response.ok && new TextEncoder().encode(fresh.body).byteLength <= AVIATION_CACHE_MAX_BYTES) {
          entries.delete(key);
          while (entries.size >= AVIATION_CACHE_MAX_ENTRIES) entries.delete(entries.keys().next().value!);
          entries.set(key, fresh);
        }
        return fresh;
      })().finally(() => inflight.delete(key));
      inflight.set(key, pending);
    }
    entry = await pending;
  }
  return new NextResponse(entry.body, { status: entry.status, headers: entry.headers as [string, string][] });
}

/** Test seam: forget cached responses. */
export const clearAviationRouteCache = () => { entries.clear(); inflight.clear(); };
