import {
  MapRuntimePortError,
  freezeMapRuntimeCamera,
  type MapRuntimeCamera,
  type MapRuntimePort,
  type MapRuntimeSnapshot,
} from "./map-runtime-port";
import type { MapRuntimeFrameScheduler } from "./map-runtime-resize-coordinator";

export const MAP_RUNTIME_CAMERA_COORDINATOR_PROFILE =
  "kfm.map-runtime-camera-coordinator.v1" as const;

export type MapRuntimeCameraCoordinator = Readonly<{
  readonly profile: typeof MAP_RUNTIME_CAMERA_COORDINATOR_PROFILE;
  schedule(camera: MapRuntimeCamera): Promise<MapRuntimeSnapshot>;
  flush(): MapRuntimeSnapshot;
  hasPending(): boolean;
  dispose(): void;
}>;

type PendingNavigation = Readonly<{
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

function disposedError(
  message = "Map runtime camera coordinator is disposed.",
): MapRuntimePortError {
  return new MapRuntimePortError("MAP_RUNTIME_DISPOSED", message);
}

function normalizeNavigationError(error: unknown): MapRuntimePortError {
  if (error instanceof MapRuntimePortError) return error;
  return new MapRuntimePortError(
    "MAP_RUNTIME_NAVIGATION_FAILED",
    "Map runtime camera scheduling failed.",
  );
}

/**
 * Frame-coalesced renderer-neutral camera helper.
 *
 * Repeated schedule() calls before the next frame share one promise and retain
 * only the most recent valid KFM-owned camera. This bounds renderer work during
 * rapid shell/navigation updates without creating animation, source/layer,
 * evidence, policy, release, or publication authority.
 */
export class DefaultMapRuntimeCameraCoordinator
  implements MapRuntimeCameraCoordinator
{
  readonly profile = MAP_RUNTIME_CAMERA_COORDINATOR_PROFILE;

  private readonly runtime: MapRuntimePort;
  private readonly scheduler: MapRuntimeFrameScheduler;
  private frameHandle: number | null = null;
  private pending: PendingNavigation | null = null;
  private nextCamera: MapRuntimeCamera | null = null;
  private disposed = false;

  constructor(
    runtime: MapRuntimePort,
    scheduler: MapRuntimeFrameScheduler = createDefaultFrameScheduler(),
  ) {
    this.runtime = runtime;
    this.scheduler = scheduler;
  }

  schedule(camera: MapRuntimeCamera): Promise<MapRuntimeSnapshot> {
    if (this.disposed) return Promise.reject(disposedError());

    let frozenCamera: MapRuntimeCamera;
    try {
      frozenCamera = freezeMapRuntimeCamera(camera);
    } catch (error) {
      return Promise.reject(normalizeNavigationError(error));
    }
    this.nextCamera = frozenCamera;

    if (this.pending !== null) return this.pending.promise;

    let resolvePending!: (snapshot: MapRuntimeSnapshot) => void;
    let rejectPending!: (error: unknown) => void;
    const promise = new Promise<MapRuntimeSnapshot>((resolve, reject) => {
      resolvePending = resolve;
      rejectPending = reject;
    });
    const pending: PendingNavigation = Object.freeze({
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
      this.nextCamera = null;
      pending.reject(normalizeNavigationError(error));
    }

    return promise;
  }

  flush(): MapRuntimeSnapshot {
    if (this.disposed) throw disposedError();

    const pending = this.pending;
    if (pending === null) return this.runtime.getSnapshot();

    const camera = this.takePendingCamera();
    this.clearScheduledFrame();
    this.pending = null;
    try {
      const snapshot = this.runtime.setCamera(camera);
      pending.resolve(snapshot);
      return snapshot;
    } catch (error) {
      const normalized = normalizeNavigationError(error);
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
    this.nextCamera = null;
    pending?.reject(
      disposedError(
        "Map runtime camera coordinator was disposed before its scheduled navigation.",
      ),
    );
  }

  private runScheduled(pending: PendingNavigation): void {
    if (this.pending !== pending) return;
    this.frameHandle = null;

    if (this.disposed) {
      this.pending = null;
      this.nextCamera = null;
      pending.reject(disposedError());
      return;
    }

    const camera = this.takePendingCamera();
    this.pending = null;
    try {
      pending.resolve(this.runtime.setCamera(camera));
    } catch (error) {
      pending.reject(normalizeNavigationError(error));
    }
  }

  private takePendingCamera(): MapRuntimeCamera {
    const camera = this.nextCamera;
    this.nextCamera = null;
    if (camera !== null) return camera;
    throw new MapRuntimePortError(
      "MAP_RUNTIME_NAVIGATION_FAILED",
      "Map runtime camera scheduling lost its pending camera.",
    );
  }

  private clearScheduledFrame(): void {
    const handle = this.frameHandle;
    this.frameHandle = null;
    if (handle === null) return;
    try {
      this.scheduler.cancel(handle);
    } catch {
      // Scheduler cancellation is best-effort. A stale callback is harmless
      // because runScheduled() verifies the exact pending-navigation identity.
    }
  }
}

export function createMapRuntimeCameraCoordinator(
  runtime: MapRuntimePort,
  scheduler?: MapRuntimeFrameScheduler,
): MapRuntimeCameraCoordinator {
  return new DefaultMapRuntimeCameraCoordinator(runtime, scheduler);
}
