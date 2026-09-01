export const MAP_RUNTIME_TEMPORAL_PLAYBACK_PROFILE =
  "kfm.map-runtime-temporal-playback.v1" as const;

export const MAP_RUNTIME_TEMPORAL_PLAYBACK_STATES = [
  "PAUSED",
  "PLAYING",
  "ENDED",
  "DISPOSED",
] as const;

export type MapRuntimeTemporalPlaybackState =
  (typeof MAP_RUNTIME_TEMPORAL_PLAYBACK_STATES)[number];

export type MapRuntimeTemporalPlaybackReasonCode =
  | "MAP_RUNTIME_TEMPORAL_INVALID"
  | "MAP_RUNTIME_TEMPORAL_DISPOSED"
  | "MAP_RUNTIME_TEMPORAL_SCHEDULER_FAILED"
  | "MAP_RUNTIME_TEMPORAL_LISTENER_INVALID";

export class MapRuntimeTemporalPlaybackError extends Error {
  readonly code: MapRuntimeTemporalPlaybackReasonCode;

  constructor(code: MapRuntimeTemporalPlaybackReasonCode, message: string) {
    super(message);
    this.name = "MapRuntimeTemporalPlaybackError";
    this.code = code;
  }
}

export type MapRuntimeTemporalPlaybackOptions = Readonly<{
  startMs: number;
  endMs: number;
  stepMs: number;
  frameDelayMs?: number;
  loop?: boolean;
}>;

export type MapRuntimeTemporalPlaybackSnapshot = Readonly<{
  profile: typeof MAP_RUNTIME_TEMPORAL_PLAYBACK_PROFILE;
  state: MapRuntimeTemporalPlaybackState;
  startMs: number;
  endMs: number;
  stepMs: number;
  cursorMs: number;
  frameDelayMs: number;
  loop: boolean;
}>;

export type MapRuntimeTemporalPlaybackListener = (
  snapshot: MapRuntimeTemporalPlaybackSnapshot,
) => void;

/** Deterministic timer seam for browser playback and no-network tests. */
export type MapRuntimeTemporalScheduler = Readonly<{
  request(callback: () => void, delayMs: number): number;
  cancel(handle: number): void;
}>;

export type MapRuntimeTemporalPlayback = Readonly<{
  readonly profile: typeof MAP_RUNTIME_TEMPORAL_PLAYBACK_PROFILE;
  getSnapshot(): MapRuntimeTemporalPlaybackSnapshot;
  play(): MapRuntimeTemporalPlaybackSnapshot;
  pause(): MapRuntimeTemporalPlaybackSnapshot;
  seek(cursorMs: number): MapRuntimeTemporalPlaybackSnapshot;
  step(direction: -1 | 1): MapRuntimeTemporalPlaybackSnapshot;
  subscribe(listener: MapRuntimeTemporalPlaybackListener): () => void;
  dispose(): void;
}>;

const DEFAULT_FRAME_DELAY_MS = 250;
const MAX_FRAME_DELAY_MS = 60_000;
const MAX_TIMELINE_FRAMES = 100_000;

function temporalError(
  code: MapRuntimeTemporalPlaybackReasonCode,
  message: string,
): MapRuntimeTemporalPlaybackError {
  return new MapRuntimeTemporalPlaybackError(code, message);
}

function isSafeInteger(value: unknown): value is number {
  return typeof value === "number" && Number.isSafeInteger(value);
}

function createDefaultTemporalScheduler(): MapRuntimeTemporalScheduler {
  return Object.freeze({
    request: (callback: () => void, delayMs: number) =>
      globalThis.setTimeout(callback, delayMs) as unknown as number,
    cancel: (handle: number) => globalThis.clearTimeout(handle),
  });
}

function normalizeOptions(
  options: MapRuntimeTemporalPlaybackOptions,
): Readonly<Required<MapRuntimeTemporalPlaybackOptions>> {
  const frameDelayMs = options.frameDelayMs ?? DEFAULT_FRAME_DELAY_MS;
  const loop = options.loop ?? false;

  if (
    !isSafeInteger(options.startMs) ||
    !isSafeInteger(options.endMs) ||
    !isSafeInteger(options.stepMs) ||
    !isSafeInteger(frameDelayMs) ||
    options.stepMs <= 0 ||
    frameDelayMs <= 0 ||
    frameDelayMs > MAX_FRAME_DELAY_MS ||
    options.endMs < options.startMs ||
    typeof loop !== "boolean"
  ) {
    throw temporalError(
      "MAP_RUNTIME_TEMPORAL_INVALID",
      "Temporal playback options are invalid.",
    );
  }

  const span = options.endMs - options.startMs;
  if (!Number.isSafeInteger(span) || span % options.stepMs !== 0) {
    throw temporalError(
      "MAP_RUNTIME_TEMPORAL_INVALID",
      "Temporal playback range must align exactly to stepMs.",
    );
  }

  const frameCount = span / options.stepMs + 1;
  if (!Number.isSafeInteger(frameCount) || frameCount > MAX_TIMELINE_FRAMES) {
    throw temporalError(
      "MAP_RUNTIME_TEMPORAL_INVALID",
      "Temporal playback exceeds the bounded frame count.",
    );
  }

  return Object.freeze({
    startMs: options.startMs,
    endMs: options.endMs,
    stepMs: options.stepMs,
    frameDelayMs,
    loop,
  });
}

/**
 * Bounded renderer-neutral temporal playback state machine.
 *
 * It owns only a finite numeric cursor and timer sequencing. Consumers decide
 * how a cursor maps to already-governed layer/runtime state; this helper does
 * not admit sources, inspect features, interpret domain time, or publish data.
 */
export class DefaultMapRuntimeTemporalPlayback
  implements MapRuntimeTemporalPlayback
{
  readonly profile = MAP_RUNTIME_TEMPORAL_PLAYBACK_PROFILE;

  private readonly options: Readonly<Required<MapRuntimeTemporalPlaybackOptions>>;
  private readonly scheduler: MapRuntimeTemporalScheduler;
  private readonly listeners = new Set<MapRuntimeTemporalPlaybackListener>();
  private state: MapRuntimeTemporalPlaybackState = "PAUSED";
  private cursorMs: number;
  private scheduledHandle: number | null = null;
  private scheduledToken: object | null = null;

  constructor(
    options: MapRuntimeTemporalPlaybackOptions,
    scheduler: MapRuntimeTemporalScheduler = createDefaultTemporalScheduler(),
  ) {
    this.options = normalizeOptions(options);
    this.scheduler = scheduler;
    this.cursorMs = this.options.startMs;
  }

  getSnapshot(): MapRuntimeTemporalPlaybackSnapshot {
    return Object.freeze({
      profile: this.profile,
      state: this.state,
      startMs: this.options.startMs,
      endMs: this.options.endMs,
      stepMs: this.options.stepMs,
      cursorMs: this.cursorMs,
      frameDelayMs: this.options.frameDelayMs,
      loop: this.options.loop,
    });
  }

  play(): MapRuntimeTemporalPlaybackSnapshot {
    this.assertActive();
    if (this.state === "PLAYING") return this.getSnapshot();
    if (!this.options.loop && this.cursorMs === this.options.endMs) {
      this.state = "ENDED";
      return this.publish();
    }

    this.state = "PLAYING";
    const snapshot = this.publish();
    this.scheduleNextTick();
    return snapshot;
  }

  pause(): MapRuntimeTemporalPlaybackSnapshot {
    this.assertActive();
    if (this.state === "PAUSED") return this.getSnapshot();
    this.clearScheduledTick();
    this.state = this.cursorMs === this.options.endMs && !this.options.loop
      ? "ENDED"
      : "PAUSED";
    return this.publish();
  }

  seek(cursorMs: number): MapRuntimeTemporalPlaybackSnapshot {
    this.assertActive();
    this.assertCursor(cursorMs);
    this.cursorMs = cursorMs;

    if (!this.options.loop && cursorMs === this.options.endMs) {
      this.clearScheduledTick();
      this.state = "ENDED";
    } else if (this.state === "ENDED") {
      this.state = "PAUSED";
    }

    return this.publish();
  }

  step(direction: -1 | 1): MapRuntimeTemporalPlaybackSnapshot {
    this.assertActive();
    if (direction !== -1 && direction !== 1) {
      throw temporalError(
        "MAP_RUNTIME_TEMPORAL_INVALID",
        "Temporal playback step direction must be -1 or 1.",
      );
    }

    this.clearScheduledTick();
    const next = this.cursorMs + direction * this.options.stepMs;
    if (next < this.options.startMs || next > this.options.endMs) {
      if (this.options.loop) {
        this.cursorMs = direction === 1
          ? this.options.startMs
          : this.options.endMs;
        this.state = "PAUSED";
      } else {
        this.cursorMs = direction === 1
          ? this.options.endMs
          : this.options.startMs;
        this.state = direction === 1 && this.cursorMs === this.options.endMs
          ? "ENDED"
          : "PAUSED";
      }
    } else {
      this.cursorMs = next;
      this.state = !this.options.loop && next === this.options.endMs
        ? "ENDED"
        : "PAUSED";
    }
    return this.publish();
  }

  subscribe(listener: MapRuntimeTemporalPlaybackListener): () => void {
    this.assertActive();
    if (typeof listener !== "function") {
      throw temporalError(
        "MAP_RUNTIME_TEMPORAL_LISTENER_INVALID",
        "Temporal playback listener must be a function.",
      );
    }
    this.listeners.add(listener);
    let active = true;
    return () => {
      if (!active) return;
      active = false;
      this.listeners.delete(listener);
    };
  }

  dispose(): void {
    if (this.state === "DISPOSED") return;
    this.clearScheduledTick();
    this.state = "DISPOSED";
    this.publish();
    this.listeners.clear();
  }

  private assertActive(): void {
    if (this.state === "DISPOSED") {
      throw temporalError(
        "MAP_RUNTIME_TEMPORAL_DISPOSED",
        "Temporal playback is disposed.",
      );
    }
  }

  private assertCursor(cursorMs: number): void {
    if (
      !isSafeInteger(cursorMs) ||
      cursorMs < this.options.startMs ||
      cursorMs > this.options.endMs ||
      (cursorMs - this.options.startMs) % this.options.stepMs !== 0
    ) {
      throw temporalError(
        "MAP_RUNTIME_TEMPORAL_INVALID",
        "Temporal playback cursor is outside the aligned timeline.",
      );
    }
  }

  private scheduleNextTick(): void {
    const token = {};
    this.scheduledToken = token;
    try {
      this.scheduledHandle = this.scheduler.request(
        () => this.runScheduledTick(token),
        this.options.frameDelayMs,
      );
    } catch {
      this.scheduledHandle = null;
      this.scheduledToken = null;
      this.state = "PAUSED";
      this.publish();
      throw temporalError(
        "MAP_RUNTIME_TEMPORAL_SCHEDULER_FAILED",
        "Temporal playback scheduler failed.",
      );
    }
  }

  private runScheduledTick(token: object): void {
    if (this.scheduledToken !== token || this.state !== "PLAYING") return;
    this.scheduledHandle = null;
    this.scheduledToken = null;

    const next = this.cursorMs + this.options.stepMs;
    if (next > this.options.endMs) {
      if (this.options.loop) {
        this.cursorMs = this.options.startMs;
      } else {
        this.cursorMs = this.options.endMs;
        this.state = "ENDED";
        this.publish();
        return;
      }
    } else {
      this.cursorMs = next;
      if (!this.options.loop && next === this.options.endMs) {
        this.state = "ENDED";
        this.publish();
        return;
      }
    }

    this.publish();
    this.scheduleNextTick();
  }

  private clearScheduledTick(): void {
    const handle = this.scheduledHandle;
    this.scheduledHandle = null;
    this.scheduledToken = null;
    if (handle === null) return;
    try {
      this.scheduler.cancel(handle);
    } catch {
      // Cancellation is best-effort; stale callbacks are token-guarded.
    }
  }

  private publish(): MapRuntimeTemporalPlaybackSnapshot {
    const snapshot = this.getSnapshot();
    for (const listener of this.listeners) {
      try {
        listener(snapshot);
      } catch {
        // Consumer observer faults cannot poison playback progression.
      }
    }
    return snapshot;
  }
}

export function createMapRuntimeTemporalPlayback(
  options: MapRuntimeTemporalPlaybackOptions,
  scheduler?: MapRuntimeTemporalScheduler,
): MapRuntimeTemporalPlayback {
  return new DefaultMapRuntimeTemporalPlayback(options, scheduler);
}
