import {
  MAP_RUNTIME_PORT_PROFILE,
  MapRuntimePortError,
  freezeMapFeatureSelection,
  freezeMapRuntimeInlineGeoJsonLayer,
  freezeMapRuntimeCamera,
  reasonForMapRuntimeTrustState,
  type InlineGeoJsonMapRuntimePort,
  type MapFeatureSelection,
  type MapRuntimeInlineGeoJsonLayer,
  type MapRuntimeCamera,
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
 * It performs no network, DOM, WebGL, worker, protocol, plugin, tile, source
 * acquisition, evidence, policy, release, model, deployment, or publication
 * work. It only models the bounded in-memory port state; it is not a renderer
 * and cannot satisfy issue #2906 runtime readiness.
 */
export class NullMapRuntime implements InlineGeoJsonMapRuntimePort {
  readonly profile = MAP_RUNTIME_PORT_PROFILE;

  private state: MapRuntimeState = "IDLE";
  private camera: MapRuntimeCamera;
  private selection: MapFeatureSelection | null = null;
  private reason: MapRuntimeReasonCode | null = null;
  private binding: MapRuntimeInlineGeoJsonLayer | null = null;
  private layerBound = false;
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
    this.assertNotDisposed();
    if (this.state !== "INITIALIZING") return this.getSnapshot();
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

  bindInlineGeoJsonLayer(
    layer: MapRuntimeInlineGeoJsonLayer,
  ): MapRuntimeSnapshot {
    this.assertReady();
    const frozen = freezeMapRuntimeInlineGeoJsonLayer(layer);
    const invalidated = this.selection !== null;
    this.binding = frozen;
    this.layerBound = true;
    this.selection = null;
    this.reason = invalidated ? "MAP_RUNTIME_SELECTION_INVALIDATED" : null;
    return this.notifySnapshot();
  }

  removeLayer(layerId: string): MapRuntimeSnapshot {
    this.assertReady();
    if (
      this.binding === null ||
      !this.layerBound ||
      this.binding.layerId !== layerId
    ) {
      throw new MapRuntimePortError(
        "MAP_RUNTIME_LAYER_NOT_FOUND",
        "Map runtime layer was not found.",
      );
    }
    this.layerBound = false;
    return this.invalidateSelection(this.selection?.layerId === layerId);
  }

  removeSource(sourceId: string): MapRuntimeSnapshot {
    this.assertReady();
    if (this.binding === null || this.binding.sourceId !== sourceId) {
      throw new MapRuntimePortError(
        "MAP_RUNTIME_SOURCE_NOT_FOUND",
        "Map runtime source was not found.",
      );
    }
    const invalidated = this.selection?.layerId === this.binding.layerId;
    this.layerBound = false;
    this.binding = null;
    return this.invalidateSelection(invalidated);
  }

  selectFeature(layerId: string, featureId: string): MapRuntimeSnapshot {
    this.assertReady();
    if (
      this.binding === null ||
      !this.layerBound ||
      this.binding.layerId !== layerId
    ) {
      throw new MapRuntimePortError(
        "MAP_RUNTIME_LAYER_NOT_FOUND",
        "Map runtime layer was not found.",
      );
    }
    if (this.binding.selection.featureId !== featureId) {
      throw new MapRuntimePortError(
        "MAP_RUNTIME_FEATURE_NOT_FOUND",
        "Map runtime feature was not found.",
      );
    }
    return this.publishSelection(this.binding.selection);
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
    return this.publishSelection(freezeMapFeatureSelection(selection));
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
    this.binding = null;
    this.layerBound = false;
    this.state = "DISPOSED";
    this.reason = "MAP_RUNTIME_DISPOSED";
    try {
      this.notifySnapshot();
    } catch {
      // Consumer listeners cannot interrupt terminal cleanup.
    }
    this.selectionListeners.clear();
    this.snapshotListeners.clear();
  }

  private notifySnapshot(): MapRuntimeSnapshot {
    const snapshot = this.getSnapshot();
    for (const listener of [...this.snapshotListeners]) {
      try {
        listener(snapshot);
      } catch {
        // One consumer observer cannot interrupt the remaining notification path.
      }
      if (!this.snapshotIsCurrent(snapshot)) return this.getSnapshot();
    }
    return this.getSnapshot();
  }

  private snapshotIsCurrent(snapshot: MapRuntimeSnapshot): boolean {
    return (
      this.state === snapshot.state &&
      this.camera === snapshot.camera &&
      this.selection === snapshot.selection &&
      this.reason === snapshot.reason
    );
  }

  private publishSelection(selection: MapFeatureSelection): MapRuntimeSnapshot {
    const frozen = freezeMapFeatureSelection(selection);
    this.selection = frozen;
    this.reason = null;
    const publishedSnapshot = this.getSnapshot();
    for (const listener of [...this.snapshotListeners]) {
      try {
        listener(publishedSnapshot);
      } catch {
        // A consumer callback cannot make runtime selection paths diverge.
      }
      if (!this.selectionIsActive(frozen)) return this.getSnapshot();
    }
    for (const listener of [...this.selectionListeners]) {
      try {
        listener(frozen);
      } catch {
        // Continue delivering the same normalized selection to other consumers.
      }
      if (!this.selectionIsActive(frozen)) return this.getSnapshot();
    }
    return this.getSnapshot();
  }

  private selectionIsActive(selection: MapFeatureSelection): boolean {
    return this.state === "READY" && this.selection === selection;
  }

  private invalidateSelection(invalidated: boolean): MapRuntimeSnapshot {
    this.selection = null;
    this.reason = invalidated ? "MAP_RUNTIME_SELECTION_INVALIDATED" : null;
    return this.notifySnapshot();
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
