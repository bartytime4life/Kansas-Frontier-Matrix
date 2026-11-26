import type { RequestParameters } from "./maplibre-seam";

const PREFIX = "kfm-dem://";
const MAX_BYTES = 512 * 1024;
const CACHE_BYTES = 2 * 1024 * 1024;
const abortError = () => new DOMException("Aborted", "AbortError");

/** Only this origin's fixed public DEM endpoint enters the transport queue.
 * Source specifications and attribution retain the real provider URL. */
export function queuedDemUrl(raw: string, origin: string): string | null {
  try {
    const url = new URL(raw, origin);
    if (url.origin !== origin || url.pathname !== "/api/3dep-dem-tile" || url.hash || url.username || url.password) return null;
    if (url.searchParams.get("v") !== "2" || [...url.searchParams.keys()].length !== 4
      || ["v", "z", "x", "y"].some(key => url.searchParams.getAll(key).length !== 1)) return null;
    const values = ["z", "x", "y"].map(key => url.searchParams.get(key)!);
    if (values.some(v => !/^\d{1,5}$/.test(v))) return null;
    const [z,x,y] = values.map(Number);
    if (z < 6 || z > 17 || x >= 2 ** z || y >= 2 ** z) return null;
    return `${origin}/api/3dep-dem-tile?v=2&z=${z}&x=${x}&y=${y}`;
  } catch { return null; }
}

export const demTileRequest = (url: string): RequestParameters => {
  const current = typeof location === "undefined" ? null : queuedDemUrl(url, location.origin);
  return { url: current ? PREFIX + encodeURIComponent(current) : url };
};

type Result = { data: ArrayBuffer; cacheControl?: string; expires?: string };
type Waiter = { resolve: (result: Result) => void; reject: (error: unknown) => void; signal: AbortSignal; abort: () => void };
type Job = { url: string; waiters: Set<Waiter>; running: boolean };

/** Two distinct network reads shared by mesh, tint and shadow sources. Aborted
 * queued requests never reach the host. Started reads finish in their slot so
 * rapid zooms cannot leave an unbounded trail of uncancellable server work.
 * This is a 2 MiB volatile cache, not persistent visitor storage. */
export function createDemRequestPool(fetcher: typeof fetch = fetch, clock = Date.now) {
  const jobs = new Map<string, Job>(), cache = new Map<string, { data: ArrayBuffer; until: number; validUntil: number; cacheControl?: string; expires?: string }>();
  let running = 0, used = 0;
  function pump() {
    for (const job of jobs.values()) {
      if (running >= 2) break;
      if (job.running || !job.waiters.size) continue;
      running++; job.running = true;
      void (async () => {
        const response = await fetcher(job.url, { credentials: "same-origin", signal: AbortSignal.timeout(45_000) });
        if (!response.ok) throw Object.assign(new Error(`DEM tile unavailable (${response.status})`), { status: response.status });
        if (response.headers.get("content-type")?.split(";")[0] !== "image/png" || Number(response.headers.get("content-length")) > MAX_BYTES || !response.body) throw new Error("Invalid DEM tile response");
        const reader = response.body.getReader(), chunks: Uint8Array[] = []; let size = 0;
        while (true) {
          const part = await reader.read(); if (part.done) break;
          size += part.value.byteLength;
          if (size > MAX_BYTES) { await reader.cancel(); throw new Error("DEM tile exceeded display budget"); }
          chunks.push(part.value);
        }
        const bytes = new Uint8Array(size); let offset = 0;
        for (const chunk of chunks) { bytes.set(chunk, offset); offset += chunk.byteLength; }
        if (bytes.length < 8 || [137,80,78,71,13,10,26,10].some((value,index) => bytes[index] !== value)) throw new Error("Invalid DEM tile encoding");
        const data = bytes.buffer, cacheControl = response.headers.get("cache-control") ?? undefined, expires = response.headers.get("expires") ?? undefined;
        // Never renew source freshness. Retain only explicitly cacheable public
        // bytes, at most two minutes and no longer than the server's TTL.
        const date = Date.parse(response.headers.get("date") ?? "");
        const age = Math.max(0, Number(response.headers.get("age")) || 0, Number.isFinite(date) ? (clock() - date) / 1000 : 0);
        const seconds = /(?:^|,)\s*max-age=(\d+)/i.exec(cacheControl ?? "")?.[1];
        const cacheable = !/(?:no-store|no-cache|private)/i.test(cacheControl ?? "") && /(?:^|,)\s*public(?:,|$)/i.test(cacheControl ?? "") && seconds !== undefined;
        const remaining = cacheable ? Math.max(0, Number(seconds) - age) : 0;
        const effectiveCacheControl = cacheable ? `public, max-age=${Math.floor(remaining)}` : cacheControl;
        const ttl = Math.min(120, remaining);
        if (ttl > 0) {
          while (cache.size >= 12 || used + data.byteLength > CACHE_BYTES) { const key = cache.keys().next().value; if (!key) break; used -= cache.get(key)!.data.byteLength; cache.delete(key); }
          cache.set(job.url, { data, until: clock() + ttl * 1000, validUntil: clock() + remaining * 1000, cacheControl, expires }); used += data.byteLength;
        }
        return { data, cacheControl: effectiveCacheControl, expires };
      })().then(result => {
        jobs.delete(job.url); running--;
        for (const waiter of job.waiters) { waiter.signal.removeEventListener("abort", waiter.abort); waiter.resolve({ ...result, data: result.data.slice(0) }); }
        pump();
      }, error => {
        jobs.delete(job.url); running--;
        for (const waiter of job.waiters) { waiter.signal.removeEventListener("abort", waiter.abort); waiter.reject(error); }
        pump();
      });
    }
  }
  return (url: string, signal: AbortSignal): Promise<Result> => {
    if (signal.aborted) return Promise.reject(abortError());
    const cached = cache.get(url);
    if (cached && cached.until > clock()) { cache.delete(url); cache.set(url,cached); return Promise.resolve({ data: cached.data.slice(0), cacheControl: `public, max-age=${Math.max(0, Math.floor((cached.validUntil - clock()) / 1000))}`, expires: cached.expires }); }
    if (cached) { used -= cached.data.byteLength; cache.delete(url); }
    let job = jobs.get(url);
    if (!job) {
      if (jobs.size >= 64) return Promise.reject(new Error("DEM display queue is full; move closer or retry"));
      job = { url, waiters: new Set(), running: false }; jobs.set(url,job);
    }
    const captured = job;
    const result = new Promise<Result>((resolve,reject) => {
      const waiter: Waiter = { resolve,reject,signal,abort: () => {
        captured.waiters.delete(waiter); reject(abortError());
        if (!captured.running && !captured.waiters.size) jobs.delete(url);
      } };
      captured.waiters.add(waiter); signal.addEventListener("abort", waiter.abort, { once: true });
    });
    pump(); return result;
  };
}
const pool = createDemRequestPool();
export function demTileProtocol(request: RequestParameters, controller: AbortController): Promise<Result> {
  const url = request.url.startsWith(PREFIX) ? decodeURIComponent(request.url.slice(PREFIX.length)) : "";
  if (typeof location === "undefined" || queuedDemUrl(url,location.origin) !== url) return Promise.reject(new Error("Unsupported DEM resource"));
  return pool(url,controller.signal);
}
