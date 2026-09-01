import {
  MapRuntimePortError,
  type MapRuntimePort,
  type MapRuntimeSnapshot,
} from "./map-runtime-port";

export const MAP_RUNTIME_RESIZE_COORDINATOR_PROFILE =
  "kfm.map-runtime-resize-coordinator.v1" as const;

/**
 * Minimal scheduling seam used to coalesce responsive layout bursts.
 *
 * The default implementation uses requestAnimationFrame in browsers and a
 * bounded timer fallback elsewhere. Tests may inject a deterministic scheduler
 * without DOM, network, renderer, worker, source, layer, or evidence access.
 */
export type MapRuntimeFrameScheduler = Readonly<{
  request(callback: () => void): number;
  cancel(handle: number): void;
}>;

export type MapRuntimeResizeCoordinator = Readonly<{
  readonly profile: typeof MAP_RUNTIME_RESIZE_COORDINATOR_PROFILE;
  schedule(): Promise<MapRuntimeSnapshot>;
  flush(): MapRuntimeSnapshot;
  hasPending(): boolean;
  dispose(): void;
}>;

type PendingResize = Readonly<{
  promise: Promise<MapRuntimeSnapshot>;
  resolve(snapshot: MapRuntimeSnapshot): void;
  reject(error: unknown): void;
}>;

function createDefaultFrameScheduler(): MapRuntimeFrameScheduler {
  if (
    typeof globalThis.requestAnimationFrame === "function" &&
    typeof globalThis.cancelAnimationFrame === "function"
  ) {
    return Object.freeze({
      request: (callback: () => void) =>
        globalThis.requestAnimationFrame(() => callback()),
      cancel: (handle: number) => globalThis.cancelAnimationFrame(handle),
    });
  }

  return Object.freeze({
    request: (callback: () => void) =>
      globalThis.setTimeout(callback, 16) as unknown as number,
    cancel: (handle: number) => globalThis.clearTimeout(handle),
  });
}

function disposedError(message = "Map runtime resize coordinator is disposed.") {
  return new MapRuntimePortError("MAP_RUNTIME_DISPOSED", message);
}

function normalizeResizeError(error: unknown): MapRuntimePortError {
  if (error instanceof MapRuntimePortError) return error;
  return new MapRuntimePortError(
    "MAP_RUNTIME_RESIZE_FAILED",
    "Map runtime resize scheduling failed.",
  );
}

/**
 * Frame-coalesced renderer-neutral resize helper.
 *
 * Repeated schedule() calls before the next frame share one promise and cause
 * at most one MapRuntimePort.resize() call. The coordinator never owns renderer
 * objects or source/layer/evidence authority; it only sequences an already
 * accepted MapRuntimePort operation.
 */
export class DefaultMapRuntimeResizeCoordinator
  implements MapRuntimeResizeCoordinator
{
  readonly profile = MAP_RUNTIME_RESIZE_COORDINATOR_PROFILE;

  private readonly runtime: MapRuntimePort;
  private readonly scheduler: MapRuntimeFrameScheduler;
  private frameHandle: number | null = null;
  private pending: PendingResize | null = null;
  private disposed = false;

  constructor(
    runtime: MapRuntimePort,
    scheduler: MapRuntimeFrameScheduler = createDefaultFrameScheduler(),
  ) {
    this.runtime = runtime;
    this.scheduler = scheduler;
  }

  schedule(): Promise<MapRuntimeSnapshot> {
    if (this.disposed) return Promise.reject(disposedError());
    if (this.pending !== null) return this.pending.promise;

    let resolvePending!: (snapshot: MapRuntimeSnapshot) => void;
    let rejectPending!: (error: unknown) => void;
    const promise = new Promise<MapRuntimeSnapshot>((resolve, reject) => {
      resolvePending = resolve;
      rejectPending = reject;
    });
    const pending: PendingResize = Object.freeze({
      promise,
      resolve: resolvePending,
      reject: rejectPending,
    });
    this.pending = pending;

    try {
      this.frameHandle = this.scheduler.request(() => this.runScheduled(pending));
    } catch (error) {
      this.frameHandle = null;
      this.pending = null;
      pending.reject(normalizeResizeError(error));
    }

    return promise;
  }

  flush(): MapRuntimeSnapshot {
    if (this.disposed) throw disposedError();

    const pending = this.pending;
    if (pending === null) return this.runtime.resize();

    this.clearScheduledFrame();
    this.pending = null;
    try {
      const snapshot = this.runtime.resize();
      pending.resolve(snapshot);
      return snapshot;
    } catch (error) {
      const normalized = normalizeResizeError(error);
      pending.reject(normalized);
      throw normalized;
    }
  }

  hasPending(): boolean {
    return this.pending !== null;
  }

  dispose(): void {
    if (this.disposed) return;
    this.disposed = true;
    this.clearScheduledFrame();
    const pending = this.pending;
    this.pending = null;
    pending?.reject(
      disposedError(
        "Map runtime resize coordinator was disposed before its scheduled resize.",
      ),
    );
  }

  private runScheduled(pending: PendingResize): void {
    if (this.pending !== pending) return;
    this.frameHandle = null;
    this.pending = null;

    if (this.disposed) {
      pending.reject(disposedError());
      return;
    }

    try {
      pending.resolve(this.runtime.resize());
    } catch (error) {
      pending.reject(normalizeResizeError(error));
    }
  }

  private clearScheduledFrame(): void {
    const handle = this.frameHandle;
    this.frameHandle = null;
    if (handle === null) return;
    try {
      this.scheduler.cancel(handle);
    } catch {
      // Scheduler cancellation is best-effort. A stale callback is harmless
      // because runScheduled() verifies the exact pending resize identity.
    }
  }
}

export function createMapRuntimeResizeCoordinator(
  runtime: MapRuntimePort,
  scheduler?: MapRuntimeFrameScheduler,
): MapRuntimeResizeCoordinator {
  return new DefaultMapRuntimeResizeCoordinator(runtime, scheduler);
}
