import {
  MapRuntimePortError,
  freezeMapRuntimeCamera,
  type MapRuntimeCamera,
  type MapRuntimePort,
  type MapRuntimeSnapshot,
} from "./map-runtime-port";

export const MAP_RUNTIME_NAVIGATION_HISTORY_PROFILE =
  "kfm.map-runtime-navigation-history.v1" as const;
export const DEFAULT_MAP_RUNTIME_NAVIGATION_HISTORY_CAPACITY = 32;
export const MAX_MAP_RUNTIME_NAVIGATION_HISTORY_CAPACITY = 128;

export type MapRuntimeNavigationHistoryState = Readonly<{
  profile: typeof MAP_RUNTIME_NAVIGATION_HISTORY_PROFILE;
  length: number;
  index: number;
  canGoBack: boolean;
  canGoForward: boolean;
}>;

export type MapRuntimeNavigationHistoryOptions = Readonly<{
  capacity?: number;
}>;

function camerasEqual(left: MapRuntimeCamera, right: MapRuntimeCamera): boolean {
  return (
    left.longitude === right.longitude &&
    left.latitude === right.latitude &&
    left.zoom === right.zoom &&
    left.bearing === right.bearing &&
    left.pitch === right.pitch
  );
}

/**
 * Renderer-neutral bounded navigation history for MapRuntimePort consumers.
 *
 * The coordinator observes READY camera snapshots and can replay prior/forward
 * cameras through the KFM-owned port. It stores no renderer objects, feature or
 * layer data, EvidenceRefs, source metadata, URLs, credentials, or policy state.
 */
export class MapRuntimeNavigationHistory {
  readonly profile = MAP_RUNTIME_NAVIGATION_HISTORY_PROFILE;

  private readonly runtime: MapRuntimePort;
  private readonly capacity: number;
  private entries: MapRuntimeCamera[] = [];
  private index = -1;
  private disposed = false;
  private replaying = false;
  private readonly unsubscribeSnapshot: () => void;

  constructor(
    runtime: MapRuntimePort,
    options: MapRuntimeNavigationHistoryOptions = {},
  ) {
    const capacity =
      options.capacity ?? DEFAULT_MAP_RUNTIME_NAVIGATION_HISTORY_CAPACITY;
    if (
      !Number.isSafeInteger(capacity) ||
      capacity < 2 ||
      capacity > MAX_MAP_RUNTIME_NAVIGATION_HISTORY_CAPACITY
    ) {
      throw new MapRuntimePortError(
        "MAP_RUNTIME_STATE_INVALID",
        "Map runtime navigation history capacity is invalid.",
      );
    }

    this.runtime = runtime;
    this.capacity = capacity;

    const initial = runtime.getSnapshot();
    if (initial.state === "READY") this.recordCamera(initial.camera);
    this.unsubscribeSnapshot = runtime.subscribeSnapshot((snapshot) => {
      this.observeSnapshot(snapshot);
    });
  }

  getState(): MapRuntimeNavigationHistoryState {
    return Object.freeze({
      profile: MAP_RUNTIME_NAVIGATION_HISTORY_PROFILE,
      length: this.entries.length,
      index: this.index,
      canGoBack: this.index > 0,
      canGoForward: this.index >= 0 && this.index < this.entries.length - 1,
    });
  }

  back(): MapRuntimeSnapshot | null {
    this.assertNotDisposed();
    if (this.index <= 0) return null;
    return this.replay(this.index - 1);
  }

  forward(): MapRuntimeSnapshot | null {
    this.assertNotDisposed();
    if (this.index < 0 || this.index >= this.entries.length - 1) return null;
    return this.replay(this.index + 1);
  }

  dispose(): void {
    if (this.disposed) return;
    this.disposed = true;
    this.unsubscribeSnapshot();
    this.entries = [];
    this.index = -1;
  }

  private observeSnapshot(snapshot: MapRuntimeSnapshot): void {
    if (this.disposed || this.replaying || snapshot.state !== "READY") return;
    this.recordCamera(snapshot.camera);
  }

  private recordCamera(camera: MapRuntimeCamera): void {
    const current = this.index >= 0 ? this.entries[this.index] : null;
    if (current !== null && camerasEqual(current, camera)) return;

    if (this.index < this.entries.length - 1) {
      this.entries = this.entries.slice(0, this.index + 1);
    }

    this.entries.push(freezeMapRuntimeCamera(camera));
    this.index = this.entries.length - 1;

    if (this.entries.length > this.capacity) {
      const overflow = this.entries.length - this.capacity;
      this.entries.splice(0, overflow);
      this.index -= overflow;
    }
  }

  private replay(targetIndex: number): MapRuntimeSnapshot {
    const camera = this.entries[targetIndex];
    if (camera === undefined) {
      throw new MapRuntimePortError(
        "MAP_RUNTIME_STATE_INVALID",
        "Map runtime navigation history target is invalid.",
      );
    }

    this.replaying = true;
    try {
      const snapshot = this.runtime.setCamera(camera);
      this.index = targetIndex;
      return snapshot;
    } finally {
      this.replaying = false;
    }
  }

  private assertNotDisposed(): void {
    if (this.disposed) {
      throw new MapRuntimePortError(
        "MAP_RUNTIME_DISPOSED",
        "Map runtime navigation history has been disposed.",
      );
    }
  }
}

export function createMapRuntimeNavigationHistory(
  runtime: MapRuntimePort,
  options: MapRuntimeNavigationHistoryOptions = {},
): MapRuntimeNavigationHistory {
  return new MapRuntimeNavigationHistory(runtime, options);
}
