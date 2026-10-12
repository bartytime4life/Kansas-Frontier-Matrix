import {
  MAP_RUNTIME_PORT_PROFILE,
  MapRuntimePortError,
  freezeMapFeatureSelection,
  freezeMapRuntimeCamera,
  reasonForMapRuntimeTrustState,
  type MapFeatureSelection,
  type MapRuntimeCamera,
  type MapRuntimePort,
  type MapRuntimeReasonCode,
  type MapRuntimeSelectionListener,
  type MapRuntimeSnapshotListener,
  type MapRuntimeSnapshot,
  type MapRuntimeState,
  type MapRuntimeTrustState,
} from "./map-runtime-port";

/** Kansas-centered deterministic camera used by the dependency-free test port. */
export const DEFAULT_MAP_RUNTIME_CAMERA: MapRuntimeCamera = Object.freeze({
  longitude: -98.4842,
  latitude: 38.4988,
  zoom: 5.5,
  bearing: 0,
  pitch: 0,
});

/**
 * Dependency-free MapRuntimePort implementation for consumer migration and tests.
 *
 * It performs no network, DOM, WebGL, worker, protocol, plugin, tile, source,
 * evidence, policy, release, lifecycle, model, deployment, or publication work.
 * It is not a renderer and cannot satisfy issue #2906 runtime readiness.
 */
export class NullMapRuntime implements MapRuntimePort {
  readonly profile = MAP_RUNTIME_PORT_PROFILE;

  private state: MapRuntimeState = "IDLE";
  private camera: MapRuntimeCamera;
  private selection: MapFeatureSelection | null = null;
  private reason: MapRuntimeReasonCode | null = null;
  private readonly selectionListeners = new Set<MapRuntimeSelectionListener>();
  private readonly snapshotListeners = new Set<MapRuntimeSnapshotListener>();

  constructor(initialCamera: MapRuntimeCamera = DEFAULT_MAP_RUNTIME_CAMERA) {
    this.camera = freezeMapRuntimeCamera(initialCamera);
  }

  async initialize(
    initialCamera: MapRuntimeCamera = this.camera,
  ): Promise<MapRuntimeSnapshot> {
    this.assertNotDisposed();
    if (this.state === "READY") return this.getSnapshot();

    this.state = "INITIALIZING";
    this.reason = null;
    this.notifySnapshot();
    this.camera = freezeMapRuntimeCamera(initialCamera);
    this.state = "READY";
    return this.notifySnapshot();
  }

  getSnapshot(): MapRuntimeSnapshot {
    return Object.freeze({
      profile: MAP_RUNTIME_PORT_PROFILE,
      state: this.state,
      camera: this.camera,
      selection: this.selection,
      reason: this.reason,
    });
  }

  setCamera(camera: MapRuntimeCamera): MapRuntimeSnapshot {
    this.assertReady();
    this.camera = freezeMapRuntimeCamera(camera);
    return this.notifySnapshot();
  }

  subscribeSnapshot(listener: MapRuntimeSnapshotListener): () => void {
    this.assertNotDisposed();
    if (typeof listener !== "function") {
      throw new MapRuntimePortError(
        "MAP_RUNTIME_LISTENER_INVALID",
        "Map runtime snapshot listener is invalid.",
      );
    }
    this.snapshotListeners.add(listener);
    let active = true;
    return (): void => {
      if (!active) return;
      active = false;
      this.snapshotListeners.delete(listener);
    };
  }

  subscribeSelection(listener: MapRuntimeSelectionListener): () => void {
    this.assertNotDisposed();
    if (typeof listener !== "function") {
      throw new MapRuntimePortError(
        "MAP_RUNTIME_LISTENER_INVALID",
        "Map runtime selection listener is invalid.",
      );
    }
    this.selectionListeners.add(listener);
    let active = true;
    return (): void => {
      if (!active) return;
      active = false;
      this.selectionListeners.delete(listener);
    };
  }

  /** Test/control-plane hook; not part of the consumer-facing MapRuntimePort. */
  emitSelection(selection: MapFeatureSelection): MapRuntimeSnapshot {
    this.assertReady();
    const frozen = freezeMapFeatureSelection(selection);
    this.selection = frozen;
    const snapshot = this.notifySnapshot();
    for (const listener of [...this.selectionListeners]) listener(frozen);
    return snapshot;
  }

  /** Test/control-plane hook; consumes a state but grants no upstream authority. */
  emitTrustState(state: MapRuntimeTrustState): MapRuntimeSnapshot {
    this.assertNotDisposed();
    this.state = state;
    this.reason = reasonForMapRuntimeTrustState(state);
    this.selection = null;
    return this.notifySnapshot();
  }

  dispose(): void {
    if (this.state === "DISPOSED") return;
    this.selection = null;
    this.state = "DISPOSED";
    this.reason = "MAP_RUNTIME_DISPOSED";
    this.notifySnapshot();
    this.selectionListeners.clear();
    this.snapshotListeners.clear();
  }

  private notifySnapshot(): MapRuntimeSnapshot {
    const snapshot = this.getSnapshot();
    for (const listener of [...this.snapshotListeners]) listener(snapshot);
    return snapshot;
  }

  private assertNotDisposed(): void {
    if (this.state === "DISPOSED") {
      throw new MapRuntimePortError(
        "MAP_RUNTIME_DISPOSED",
        "Map runtime has been disposed.",
      );
    }
  }

  private assertReady(): void {
    this.assertNotDisposed();
    if (this.state !== "READY") {
      throw new MapRuntimePortError(
        "MAP_RUNTIME_NOT_READY",
        "Map runtime is not ready.",
      );
    }
  }
}

export function createNullMapRuntime(
  initialCamera: MapRuntimeCamera = DEFAULT_MAP_RUNTIME_CAMERA,
): NullMapRuntime {
  return new NullMapRuntime(initialCamera);
}
