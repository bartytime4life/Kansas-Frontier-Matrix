type HoverClock = {
  now: () => number;
  setTimer: (callback: () => void, delay: number) => number;
  clearTimer: (timer: number) => void;
};

/** Bound hit testing while always sampling the final pointer position. */
export function createMapHoverSampler<T>(sample: (event: T) => void, intervalMs = 80,
  clock: HoverClock = {
    now: () => performance.now(),
    setTimer: (callback, delay) => window.setTimeout(callback, delay),
    clearTimer: timer => window.clearTimeout(timer),
  }) {
  let last = -Infinity;
  let pending: { event: T } | undefined;
  let timer: number | undefined;
  const flush = () => {
    timer = undefined;
    const next = pending;
    pending = undefined;
    if (!next) return;
    last = clock.now();
    sample(next.event);
  };
  return {
    push(event: T) {
      pending = { event };
      if (timer !== undefined) return;
      const delay = Math.max(0, intervalMs - (clock.now() - last));
      if (delay === 0) flush();
      else timer = clock.setTimer(flush, delay);
    },
    cancel() {
      if (timer !== undefined) clock.clearTimer(timer);
      timer = undefined;
      pending = undefined;
      last = -Infinity;
    },
  };
}
