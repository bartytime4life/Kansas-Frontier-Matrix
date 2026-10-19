import { browserJsonRequest } from "./browser-json-request";

// Page-owned display reads only. Never use this for governed release/admin data.
type Result = Awaited<ReturnType<typeof browserJsonRequest>> & { cache: "network" | "memory" };
type Consumer = ((result: Result | undefined, error?: unknown) => void) & { progress?: (phase: "queued" | "fetching") => void };
type Job = { key: string; url: string; maxBytes: number; controller: AbortController; started: boolean;
  consumers: Set<Consumer>; cacheMs: number; validate: (body: unknown) => boolean };
export class LayerJsonReads {
  private active = 0;
  private jobs = new Map<string, Job>();
  private queue: Job[] = [];
  private cache = new Map<string, { result: Result; expires: number }>();
  constructor(private concurrency = 3, private now = () => Date.now()) {}
  read(url: string, options: { signal: AbortSignal; maxBytes: number; cacheMs?: number; validate: (body: unknown) => boolean; onProgress?: (phase: "queued" | "fetching") => void }): Promise<Result> {
    const { signal, maxBytes, validate, cacheMs = 0 } = options;
    signal.throwIfAborted();
    // Limits and identity are part of the key; current reads always bypass memory.
    const key = `${maxBytes}:${url}`;
    const cached = this.cache.get(key);
    if (cacheMs && cached && cached.expires > this.now() && validate(cached.result.body)) {
      this.cache.delete(key); this.cache.set(key, cached);
      return Promise.resolve({ ...cached.result, cache: "memory" });
    }
    this.cache.delete(key);
    let job = this.jobs.get(key);
    if (!job) {
      job = { key, url, maxBytes, validate, cacheMs, controller: new AbortController(), started: false, consumers: new Set() };
      this.jobs.set(key, job); this.queue.push(job);
    }
    const current = job;
    return new Promise((resolve, reject) => {
      const finish: Consumer = (result: Result | undefined, error?: unknown) => {
        signal.removeEventListener("abort", abort);
        current.consumers.delete(finish);
        if (error !== undefined) reject(error);
        else {
          try {
            if (result && validate(result.body)) resolve(result);
            else reject(new Error("Source response does not match the requested layer or date."));
          } catch (validationError) { reject(validationError); }
        }
      };
      const abort = () => {
        finish(undefined, signal.reason ?? new DOMException("Cancelled", "AbortError"));
        if (!current.consumers.size) {
          current.controller.abort();
          if (this.jobs.get(key) === current) this.jobs.delete(key);
          this.queue = this.queue.filter(item => item !== current);
        }
      };
      finish.progress = options.onProgress;
      current.consumers.add(finish);
      finish.progress?.(current.started ? "fetching" : "queued");
      signal.addEventListener("abort", abort, { once: true });
      if (signal.aborted) abort();
      this.pump();
    });
  }
  private pump() {
    while (this.active < this.concurrency && this.queue.length) {
      const job = this.queue.shift()!;
      if (!job.consumers.size || job.controller.signal.aborted) continue;
      this.active++; job.started = true;
      for (const finish of job.consumers) finish.progress?.("fetching");
      void browserJsonRequest(job.url, {
        signal: job.controller.signal, maxBytes: job.maxBytes, timeoutMs: 30_000,
        recovery: job.url === "/api/live-context?feed=census-counties" ? "census" : undefined,
        headers: { Accept: "application/json" },
      })
        .then(response => {
          const result: Result = { ...response, cache: "network" };
          job.controller.signal.throwIfAborted();
          if (!result.response.ok || !job.validate(result.body)) throw new Error(`Source adapter returned an unavailable or incompatible response (HTTP ${result.response.status}).`);
          // At most four 8 MiB responses, with original source/retrieval timestamps.
          if (job.cacheMs && job.maxBytes <= 8 * 1024 * 1024) {
            this.cache.set(job.key, { result, expires: this.now() + Math.min(job.cacheMs, 300_000) });
            while (this.cache.size > 4) this.cache.delete(this.cache.keys().next().value!);
          }
          // Retire before resolving consumers: an await continuation can start
          // another uncached read before finally runs. A settled job cannot
          // deliver a response to consumers attached in that interval.
          if (this.jobs.get(job.key) === job) this.jobs.delete(job.key);
          for (const finish of [...job.consumers]) finish(result);
        }).catch(error => {
          if (this.jobs.get(job.key) === job) this.jobs.delete(job.key);
          for (const finish of [...job.consumers]) finish(undefined, error);
        })
        .finally(() => { this.active--; if (this.jobs.get(job.key) === job) this.jobs.delete(job.key); this.pump(); });
    }
  }
}
