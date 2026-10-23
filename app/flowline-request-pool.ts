/** Process/isolate-local protection for the fixed, public flowline endpoint only. */
export const FLOWLINE_REQUEST_LIMITS = Object.freeze({
  active: 9, waiters: 96, cacheEntries: 36, cacheBytes: 12 * 1024 * 1024,
  entryBytes: 6 * 1024 * 1024, freshMs: 3_600_000, failureMs: 1_000, timeoutMs: 30_000,
});

type Limits = { [K in keyof typeof FLOWLINE_REQUEST_LIMITS]: number };
type Result = { state: "ready"; body: string; expires: number }
  | { state: "unavailable" | "overloaded" | "cancelled" };
type Job = {
  controller: AbortController; subscribers: Set<(result: Result) => void>; value?: Result; finish: (result: Result) => void;
  waiters: number; done: boolean; timer: ReturnType<typeof setTimeout>;
};
type Cached = { result: Result; expires: number; bytes: number };

/**
 * Only the caller's validated, serialized payload may enter the success cache.
 * No queue or stale fallback. Aborted transports keep their slot until settled,
 * even if a transport ignores cancellation; a timeout must not open extra reads.
 * Options are an internal test seam, never sourced from request parameters.
 */
export function createFlowlineRequestPool(options: Partial<Limits> & { now?: () => number } = {}) {
  const limits = { ...FLOWLINE_REQUEST_LIMITS, ...options };
  const now = options.now ?? Date.now;
  const jobs = new Map<string, Job>();
  const cache = new Map<string, Cached>();
  let cacheBytes = 0, waiters = 0;
  const remove = (key: string) => {
    const entry = cache.get(key);
    if (entry) { cacheBytes -= entry.bytes; cache.delete(key); }
  };
  const prune = () => {
    for (const [key, entry] of cache) if (entry.expires <= now()) remove(key);
  };
  const remember = (key: string, result: Result, expires: number, bytes: number) => {
    prune();
    remove(key);
    if (bytes > limits.entryBytes || bytes > limits.cacheBytes) return;
    while (cache.size && (cache.size >= limits.cacheEntries || cacheBytes + bytes > limits.cacheBytes)) {
      remove(cache.keys().next().value!);
    }
    if (limits.cacheEntries > 0) { cache.set(key, { result, expires, bytes }); cacheBytes += bytes; }
  };
  const start = (key: string, load: (signal: AbortSignal) => Promise<string>) => {
    const controller = new AbortController();
    const job: Job = {
      controller, subscribers: new Set(), waiters: 0, done: false,
      finish: value => {
        if (job.done) return;
        job.done = true; job.value = value; clearTimeout(job.timer);
        for (const subscriber of job.subscribers) subscriber(value);
        job.subscribers.clear();
      },
      timer: setTimeout(() => {
        controller.abort();
        remember(key, { state: "unavailable" }, now() + limits.failureMs, 0);
        job.finish({ state: "unavailable" });
      }, limits.timeoutMs),
    };
    jobs.set(key, job);
    // Attach subscribers before dispatching the provider read.
    void Promise.resolve().then(() => {
      controller.signal.throwIfAborted();
      return load(controller.signal);
    }).then(body => {
      controller.signal.throwIfAborted();
      const value: Result = { state: "ready", body, expires: now() + limits.freshMs };
      remember(key, value, value.expires, new TextEncoder().encode(body).byteLength);
      job.finish(value);
    }).catch(() => {
      controller.abort();
      if (!job.done) {
        remember(key, { state: "unavailable" }, now() + limits.failureMs, 0);
        job.finish({ state: "unavailable" });
      }
    }).finally(() => { clearTimeout(job.timer); jobs.delete(key); });
    return job;
  };
  return {
    async get(key: string, signal: AbortSignal, load: (signal: AbortSignal) => Promise<string>): Promise<Result> {
      if (signal.aborted) return { state: "cancelled" };
      prune();
      const cached = cache.get(key);
      if (cached) {
        cache.delete(key); cache.set(key, cached); // bounded LRU, with absolute expiry
        return cached.result;
      }
      let job = jobs.get(key);
      if (waiters >= limits.waiters || job?.controller.signal.aborted || (!job && jobs.size >= limits.active)) return { state: "overloaded" };
      if (job?.done) return job.value!;
      job ??= start(key, load);
      const subscribedJob = job;
      waiters++; subscribedJob.waiters++;
      return new Promise<Result>(resolve => {
        let finished = false;
        const finish = (value: Result) => {
          if (finished) return;
          finished = true;
          signal.removeEventListener("abort", cancel);
          subscribedJob.subscribers.delete(finish);
          waiters--; subscribedJob.waiters--;
          resolve(value);
          if (!subscribedJob.waiters && !subscribedJob.done) {
            subscribedJob.controller.abort();
            subscribedJob.finish({ state: "cancelled" });
          }
        };
        const cancel = () => finish({ state: "cancelled" });
        subscribedJob.subscribers.add(finish);
        signal.addEventListener("abort", cancel, { once: true });
        if (signal.aborted) cancel();
      });
    },
  };
}
