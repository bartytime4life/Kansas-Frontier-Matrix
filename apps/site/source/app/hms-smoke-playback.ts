import { readBoundedJson } from "./bounded-json";
import type { OfficialContextPayload } from "./live-context";
export const HMS_FIRST_DAY = "2005-08-05";
export const hmsToday = () => new Date().toISOString().slice(0, 10);
export const hmsDayNumber = (day: string) => Date.parse(`${day}T00:00:00Z`) / 86400000;
export const hmsAdvance = (day: string, step: number) => new Date((hmsDayNumber(day) + step) * 86400000).toISOString().slice(0, 10);
export function hmsValidDay(day: string, through = hmsToday()) {
  return /^\d{4}-\d{2}-\d{2}$/.test(day) && Number.isFinite(hmsDayNumber(day))
    && hmsAdvance(day, 0) === day && day >= HMS_FIRST_DAY && day <= through;
}
/** Three bounded daily payloads; no eager download of the twenty-year archive. */
export class HmsFrameCache {
  private frames = new Map<string, { payload: OfficialContextPayload; checked: number }>();
  constructor(private fetcher: typeof fetch = fetch) {}
  async get(day: string, signal: AbortSignal): Promise<OfficialContextPayload> {
    if (!hmsValidDay(day)) throw new Error("Choose a supported UTC archive day.");
    signal.throwIfAborted();
    const cached = this.frames.get(day);
    if (cached && Date.now() - cached.checked < 900_000) {
      this.frames.delete(day); this.frames.set(day, cached); return cached.payload;
    }
    const controller = new AbortController();
    const cancel = () => controller.abort(signal.reason);
    signal.addEventListener("abort", cancel, { once: true });
    const timer = setTimeout(() => controller.abort(new DOMException("Smoke publication timed out", "TimeoutError")), 30_000);
    try {
      const response = await this.fetcher(`/api/live-context?feed=noaa-hms-smoke&day=${day}`, { cache: "no-store", signal: controller.signal, credentials: "same-origin" });
      const payload = await readBoundedJson(response, 4 * 1024 * 1024, controller.signal) as OfficialContextPayload;
      signal.throwIfAborted(); controller.signal.throwIfAborted();
      if (!response.ok || payload.feed !== "noaa-hms-smoke" || !["ready", "empty", "partial"].includes(payload.state)
        || typeof payload.retrievedAt !== "string" || !Number.isFinite(Date.parse(payload.retrievedAt))
        || !Array.isArray(payload.smokeCoverage?.missingDays) || payload.smokeCoverage?.day !== day || !Array.isArray(payload.smokeCoverage.availableDays)
        || !payload.smokeCoverage.availableDays.includes(day)
        || payload.smokeCoverage.missingDays.some(missing => payload.smokeCoverage!.availableDays.includes(missing))
        || payload.data?.type !== "FeatureCollection" || !Array.isArray(payload.data.features)
        || payload.featureCount !== payload.data.features.length || payload.featureCount > 4000) {
        throw new Error("Requested NOAA publication unavailable or invalid. Last checked frame retained; no clear-air inference.");
      }
      this.frames.delete(day); this.frames.set(day, { payload, checked: Date.now() });
      while (this.frames.size > 3) this.frames.delete(this.frames.keys().next().value!);
      return payload;
    } finally { clearTimeout(timer); signal.removeEventListener("abort", cancel); }
  }
  get size() { return this.frames.size; }
}

/** Search a small explicit range; unavailable publications are never clear-air days. */
export async function findRecentSmoke(cache: HmsFrameCache, today: string, signal: AbortSignal, checking: (day: string) => void = () => {}) {
  const missingDays: string[] = [];
  for (let offset = 0; offset < 7; offset++) {
    const day = hmsAdvance(today, -offset);
    if (!hmsValidDay(day, today)) break;
    signal.throwIfAborted(); checking(day);
    let payload: OfficialContextPayload;
    try { payload = await cache.get(day, signal); }
    catch { signal.throwIfAborted(); missingDays.push(day); continue; }
    signal.throwIfAborted();
    if (payload.featureCount > 0) return { day, payload, missingDays };
  }
  return { day: null, payload: null, missingDays };
}

/** Serialize map mutations, including restoration of an interrupted upload.
 * A newer request cancels older work, but cannot read its tentative frame as
 * the last confirmed frame while that work is still cleaning up. */
export class HmsFrameTransitions {
  private pending: Promise<void> = Promise.resolve();
  private active: AbortController | null = null;
  run(signal: AbortSignal, transition: (signal: AbortSignal) => Promise<void>): Promise<void> {
    signal.throwIfAborted();
    this.active?.abort(new DOMException("Superseded smoke frame", "AbortError"));
    const controller = new AbortController();
    this.active = controller;
    const cancel = () => controller.abort(signal.reason);
    signal.addEventListener("abort", cancel, { once: true });
    const next = this.pending.then(async () => {
      controller.signal.throwIfAborted();
      await transition(controller.signal);
    }).finally(() => {
      signal.removeEventListener("abort", cancel);
      if (this.active === controller) this.active = null;
    });
    this.pending = next.catch(() => {});
    return next;
  }
}

/** Fade-through changes presentation only. Coordinates are never interpolated. */
export async function hmsFade(from: number, to: number, signal: AbortSignal, paint: (value: number) => void, duration = 180) {
  signal.throwIfAborted();
  if (!duration) { paint(to); return; }
  await new Promise<void>((resolve, reject) => {
    let frame = 0; const start = performance.now();
    const abort = () => { cancelAnimationFrame(frame); reject(new DOMException("Cancelled", "AbortError")); };
    const tick = (now: number) => {
      const fraction = Math.min(1, (now - start) / duration);
      try { paint(from + (to - from) * (fraction * fraction * (3 - 2 * fraction))); }
      catch (error) { signal.removeEventListener("abort", abort); reject(error); return; }
      if (fraction === 1) { signal.removeEventListener("abort", abort); resolve(); }
      else frame = requestAnimationFrame(tick);
    };
    signal.addEventListener("abort", abort, { once: true }); frame = requestAnimationFrame(tick);
  });
}
