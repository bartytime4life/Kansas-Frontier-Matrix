import { Map as MapLibreMap } from "maplibre-gl";

import {
  MAP_RUNTIME_PORT_PROFILE,
  MAP_RUNTIME_TRUST_STATE_REASONS,
  MapRuntimePortError,
  freezeMapRuntimeCamera,
  freezeMapRuntimeInlineGeoJsonLayer,
  type InlineGeoJsonMapRuntimePort,
  type MapFeatureSelection,
  type MapRuntimeCamera,
  type MapRuntimeInlineGeoJsonLayer,
  type MapRuntimeReasonCode,
  type MapRuntimeSelectionListener,
  type MapRuntimeSnapshot,
  type MapRuntimeSnapshotListener,
  type MapRuntimeState,
} from "./map-runtime-port";
import { DEFAULT_MAP_RUNTIME_CAMERA } from "./null-map-runtime";

const CONTAINER_ID = /^[A-Za-z][A-Za-z0-9._:-]{0,127}$/;
export const DEFAULT_MAPLIBRE_INITIALIZATION_DEADLINE_MS = 10_000;
const MAX_MAPLIBRE_INITIALIZATION_DEADLINE_MS = 60_000;

function createEmptyStyle() {
  return { version: 8 as const, sources: {}, layers: [] };
}

function createRendererGeoJsonData(layer: MapRuntimeInlineGeoJsonLayer) {
  const feature = layer.data.features[0];
  return {
    type: "FeatureCollection" as const,
    features: [
      {
        type: "Feature" as const,
        id: feature.id,
        geometry: {
          type: "Point" as const,
          coordinates: [
            feature.geometry.coordinates[0],
            feature.geometry.coordinates[1],
          ],
        },
        properties: null,
      },
    ],
  };
}

function supportsWebGL2(): boolean {
  if (typeof document === "undefined") return false;
  try {
    const context = document.createElement("canvas").getContext("webgl2");
    if (context === null) return false;
    context.getExtension("WEBGL_lose_context")?.loseContext();
    return true;
  } catch {
    return false;
  }
}

export type MapLibreAdapterOptions = Readonly<{
  /** ID of an existing, empty browser element owned by the calling app. */
  containerId: string;
  /** Whether MapLibre should attach its normal pointer and keyboard handlers. */
  interactive?: boolean;
  /** Bounded wait for MapLibre's load/error initialization signals. */
  initializationDeadlineMs?: number;
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
 * Minimal package-owned MapLibre implementation of the accepted MapRuntimePort.
 *
 * This bounded slice owns renderer construction, camera synchronization, one
 * deterministic inline GeoJSON point/circle binding, normalized selection,
 * finite lifecycle state, removal, and teardown. It performs no source
 * discovery and exposes no raw MapLibre value. External styles, protocols,
 * plugins, tiles, terrain, and arbitrary network sources remain out of scope.
 */
export class MapLibreAdapter implements InlineGeoJsonMapRuntimePort {
  readonly profile = MAP_RUNTIME_PORT_PROFILE;

  private readonly containerId: string;
  private readonly interactive: boolean;
  private readonly initializationDeadlineMs: number;
  private state: MapRuntimeState = "IDLE";
  private camera: MapRuntimeCamera = DEFAULT_MAP_RUNTIME_CAMERA;
  private selection: MapFeatureSelection | null = null;
  private reason: MapRuntimeReasonCode | null = null;
  private binding: MapRuntimeInlineGeoJsonLayer | null = null;
  private layerBound = false;
  private map: MapLibreMap | null = null;
  private initialization: Promise<MapRuntimeSnapshot> | null = null;
  private rejectInitialization: ((error: MapRuntimePortError) => void) | null =
    null;
  private initializationDeadline: ReturnType<typeof setTimeout> | null = null;
  private readonly rendererUnsubscribers = new Set<() => void>();
  private readonly selectionListeners = new Set<MapRuntimeSelectionListener>();
  private readonly snapshotListeners = new Set<MapRuntimeSnapshotListener>();

  constructor(options: MapLibreAdapterOptions) {
    if (!CONTAINER_ID.test(options.containerId)) {
      throw new MapRuntimePortError(
        "MAP_RUNTIME_CONTAINER_INVALID",
        "Map runtime container ID is invalid.",
      );
    }
    this.containerId = options.containerId;
    this.interactive = options.interactive ?? true;
    const initializationDeadlineMs =
      options.initializationDeadlineMs ??
      DEFAULT_MAPLIBRE_INITIALIZATION_DEADLINE_MS;
    if (
      !Number.isSafeInteger(initializationDeadlineMs) ||
      initializationDeadlineMs < 1 ||
      initializationDeadlineMs > MAX_MAPLIBRE_INITIALIZATION_DEADLINE_MS
    ) {
      throw new MapRuntimePortError(
        "MAP_RUNTIME_INITIALIZATION_FAILED",
        "Map runtime initialization deadline is invalid.",
      );
    }
    this.initializationDeadlineMs = initializationDeadlineMs;
  }

  initialize(
    initialCamera: MapRuntimeCamera = this.camera,
  ): Promise<MapRuntimeSnapshot> {
    this.assertNotDisposed();
    if (this.state === "READY") return Promise.resolve(this.getSnapshot());
    if (this.initialization !== null) return this.initialization;

    let resolveInitialization!: (snapshot: MapRuntimeSnapshot) => void;
    let rejectInitialization!: (error: MapRuntimePortError) => void;
    const initialization = new Promise<MapRuntimeSnapshot>((resolve, reject) => {
      resolveInitialization = resolve;
      rejectInitialization = reject;
    });
    this.initialization = initialization;
    this.rejectInitialization = rejectInitialization;

    this.camera = freezeMapRuntimeCamera(initialCamera);
    this.state = "INITIALIZING";
    this.reason = null;
    this.notifySnapshot();
    if (this.isDisposed()) return initialization;

    if (!supportsWebGL2()) {
      this.failInitialization();
      return initialization;
    }

    try {
      const map = new MapLibreMap({
        container: this.containerId,
        style: createEmptyStyle(),
        center: [this.camera.longitude, this.camera.latitude],
        zoom: this.camera.zoom,
        bearing: this.camera.bearing,
        pitch: this.camera.pitch,
        interactive: this.interactive,
        hash: false,
        attributionControl: false,
        maplibreLogo: false,
      });
      this.map = map;
      this.initializationDeadline = setTimeout(() => {
        if (
          this.state === "INITIALIZING" &&
          this.initialization === initialization &&
          this.map === map
        ) {
          this.failInitialization();
        }
      }, this.initializationDeadlineMs);

      const loadSubscription = map.on("load", () => {
        loadSubscription.unsubscribe();
        this.rendererUnsubscribers.delete(loadSubscription.unsubscribe);
        if (this.isDisposed()) return;
        try {
          const loadedCamera = this.readRendererCamera(map);
          if (this.state !== "INITIALIZING" || this.map !== map) return;
          this.camera = loadedCamera;
          this.state = "READY";
          this.reason = null;
          this.clearInitializationDeadline();
          const snapshot = this.notifySnapshot();
          if (this.isDisposed()) return;
          if (!this.isReadyRenderer(map)) {
            this.failInitialization();
            return;
          }
          this.initialization = null;
          this.rejectInitialization = null;
          resolveInitialization(snapshot);
        } catch {
          if (!this.isDisposed()) this.failInitialization();
        }
      });
      this.rendererUnsubscribers.add(loadSubscription.unsubscribe);

      const moveSubscription = map.on("moveend", () => {
        if (this.state !== "READY") return;
        try {
          const nextCamera = this.readRendererCamera(map);
          if (!this.isReadyRenderer(map)) return;
          if (camerasEqual(this.camera, nextCamera)) return;
          this.camera = nextCamera;
          this.notifySnapshot();
        } catch {
          this.failRuntime();
        }
      });
      this.rendererUnsubscribers.add(moveSubscription.unsubscribe);

      const clickSubscription = map.on("click", (event) => {
        const binding = this.binding;
        if (!this.isReadyRenderer(map) || binding === null || !this.layerBound) return;
        let candidates;
        try {
          candidates = map.queryRenderedFeatures(event.point, {
            layers: [binding.layerId],
          });
        } catch {
          this.failRuntime();
          return;
        }
        if (
          !this.isReadyRenderer(map) ||
          this.binding !== binding ||
          !this.layerBound
        ) {
          return;
        }
        // This capability binds exactly one governed feature to exactly one
        // queried layer. MapLibre does not preserve every valid GeoJSON string
        // ID in rendered-query results, so renderer IDs/properties cannot be
        // used as identity authority. A hit in the bound layer resolves only to
        // the already-validated KFM-owned sidecar selection.
        if (candidates.length === 0) return;
        this.publishSelection(binding.selection);
      });
      this.rendererUnsubscribers.add(clickSubscription.unsubscribe);

      const errorSubscription = map.on("error", () => {
        if (this.state === "INITIALIZING") {
          this.failInitialization();
          return;
        }
        if (this.state !== "DISPOSED") this.failRuntime();
      });
      this.rendererUnsubscribers.add(errorSubscription.unsubscribe);
    } catch {
      this.failInitialization();
    }

    return initialization;
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
    const frozen = freezeMapRuntimeCamera(camera);
    const map = this.map!;
    try {
      map.jumpTo({
        center: [frozen.longitude, frozen.latitude],
        zoom: frozen.zoom,
        bearing: frozen.bearing,
        pitch: frozen.pitch,
      });
      if (!this.isReadyRenderer(map)) throw new Error("renderer state changed");
    } catch {
      this.failRuntime();
      throw new MapRuntimePortError(
        "MAP_RUNTIME_CAMERA_UPDATE_FAILED",
        "Map runtime camera update failed.",
      );
    }
    this.camera = frozen;
    return this.notifySnapshot();
  }

  bindInlineGeoJsonLayer(
    layer: MapRuntimeInlineGeoJsonLayer,
  ): MapRuntimeSnapshot {
    this.assertReady();
    const frozen = freezeMapRuntimeInlineGeoJsonLayer(layer);
    const invalidated = this.selection !== null;
    const map = this.map!;
    try {
      this.removeBoundRendererResources(map, true);
      map.addSource(frozen.sourceId, {
        type: "geojson",
        data: createRendererGeoJsonData(frozen),
      });
      if (!this.isReadyRenderer(map)) throw new Error("renderer state changed");
      map.addLayer({
        id: frozen.layerId,
        type: "circle",
        source: frozen.sourceId,
        paint: {
          "circle-color": "#0f766e",
          "circle-radius": 9,
          "circle-stroke-color": "#ffffff",
          "circle-stroke-width": 2,
        },
      });
      if (!this.isReadyRenderer(map)) throw new Error("renderer state changed");
    } catch {
      this.failRuntime();
      throw new MapRuntimePortError(
        "MAP_RUNTIME_LAYER_BIND_FAILED",
        "Inline GeoJSON map layer binding failed.",
      );
    }
    this.binding = frozen;
    this.layerBound = true;
    return this.invalidateSelection(invalidated);
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
    const map = this.map!;
    try {
      map.removeLayer(layerId);
      if (!this.isReadyRenderer(map)) throw new Error("renderer state changed");
    } catch {
      this.failRuntime();
      throw new MapRuntimePortError(
        "MAP_RUNTIME_LAYER_REMOVAL_FAILED",
        "Map runtime layer removal failed.",
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
    try {
      this.removeBoundRendererResources(this.map!, true);
    } catch {
      this.failRuntime();
      throw new MapRuntimePortError(
        "MAP_RUNTIME_SOURCE_REMOVAL_FAILED",
        "Map runtime source removal failed.",
      );
    }
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
    return this.unsubscribeOnce(this.snapshotListeners, listener);
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
    return this.unsubscribeOnce(this.selectionListeners, listener);
  }

  dispose(): void {
    if (this.state === "DISPOSED") return;
    this.clearInitializationDeadline();
    const rejection = this.rejectInitialization;
    this.rejectInitialization = null;
    this.initialization = null;
    this.clearRenderer();
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
    rejection?.(
      new MapRuntimePortError(
        "MAP_RUNTIME_DISPOSED",
        "Map runtime was disposed during initialization.",
      ),
    );
  }

  private readRendererCamera(map: MapLibreMap): MapRuntimeCamera {
    const center = map.getCenter();
    return freezeMapRuntimeCamera({
      longitude: center.lng,
      latitude: center.lat,
      zoom: map.getZoom(),
      bearing: map.getBearing(),
      pitch: map.getPitch(),
    });
  }

  private failInitialization(): void {
    this.clearInitializationDeadline();
    const rejection = this.rejectInitialization;
    this.rejectInitialization = null;
    this.initialization = null;
    this.clearRenderer();
    this.binding = null;
    this.layerBound = false;
    this.selection = null;
    this.state = "ERROR";
    this.reason = MAP_RUNTIME_TRUST_STATE_REASONS.ERROR;
    rejection?.(
      new MapRuntimePortError(
        "MAP_RUNTIME_INITIALIZATION_FAILED",
        "Map runtime initialization failed.",
      ),
    );
    try {
      this.notifySnapshot();
    } catch {
      // Snapshot listeners cannot prevent terminal initialization settlement.
    }
  }

  private failRuntime(): void {
    if (this.state === "ERROR" && this.map === null) return;
    this.clearRenderer();
    this.binding = null;
    this.layerBound = false;
    this.selection = null;
    this.state = "ERROR";
    this.reason = MAP_RUNTIME_TRUST_STATE_REASONS.ERROR;
    try {
      this.notifySnapshot();
    } catch {
      // Runtime listeners cannot prevent finite teardown and terminal state.
    }
  }

  private clearRenderer(): void {
    this.clearRendererSubscriptions();
    const map = this.map;
    this.map = null;
    try {
      map?.remove();
    } catch {
      // Renderer teardown is best-effort; KFM state still settles finitely.
    }
  }

  private clearInitializationDeadline(): void {
    if (this.initializationDeadline === null) return;
    clearTimeout(this.initializationDeadline);
    this.initializationDeadline = null;
  }

  private clearRendererSubscriptions(): void {
    for (const unsubscribe of this.rendererUnsubscribers) {
      try {
        unsubscribe();
      } catch {
        // Package-owned cleanup continues through every registered listener.
      }
    }
    this.rendererUnsubscribers.clear();
  }

  private removeBoundRendererResources(
    map: MapLibreMap,
    removeSource: boolean,
  ): void {
    const binding = this.binding;
    if (binding === null) return;
    if (this.layerBound) {
      map.removeLayer(binding.layerId);
      if (!this.isReadyRenderer(map)) throw new Error("renderer state changed");
      this.layerBound = false;
    }
    if (removeSource) {
      map.removeSource(binding.sourceId);
      if (!this.isReadyRenderer(map)) throw new Error("renderer state changed");
      this.binding = null;
    }
  }

  private publishSelection(selection: MapFeatureSelection): MapRuntimeSnapshot {
    this.selection = selection;
    this.reason = null;
    const publishedSnapshot = this.getSnapshot();
    for (const listener of [...this.snapshotListeners]) {
      try {
        listener(publishedSnapshot);
      } catch {
        // A consumer callback cannot make pointer and accessible selection diverge.
      }
      if (!this.selectionIsActive(selection)) return this.getSnapshot();
    }
    for (const listener of [...this.selectionListeners]) {
      try {
        listener(selection);
      } catch {
        // Continue delivering the same normalized selection to other consumers.
      }
      if (!this.selectionIsActive(selection)) return this.getSnapshot();
    }
    return this.getSnapshot();
  }

  private invalidateSelection(invalidated: boolean): MapRuntimeSnapshot {
    this.selection = null;
    this.reason = invalidated ? "MAP_RUNTIME_SELECTION_INVALIDATED" : null;
    return this.notifySnapshot();
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

  private selectionIsActive(selection: MapFeatureSelection): boolean {
    return this.state === "READY" && this.selection === selection;
  }

  private unsubscribeOnce<T>(listeners: Set<T>, listener: T): () => void {
    let active = true;
    return (): void => {
      if (!active) return;
      active = false;
      listeners.delete(listener);
    };
  }

  private assertNotDisposed(): void {
    if (this.isDisposed()) {
      throw new MapRuntimePortError(
        "MAP_RUNTIME_DISPOSED",
        "Map runtime has been disposed.",
      );
    }
  }

  private assertReady(): void {
    this.assertNotDisposed();
    if (this.state !== "READY" || this.map === null) {
      throw new MapRuntimePortError(
        "MAP_RUNTIME_NOT_READY",
        "Map runtime is not ready.",
      );
    }
  }

  private isDisposed(): boolean {
    return this.state === "DISPOSED";
  }

  private isReadyRenderer(map: MapLibreMap): boolean {
    return this.state === "READY" && this.map === map;
  }
}

export function createMapLibreAdapter(
  options: MapLibreAdapterOptions,
): MapLibreAdapter {
  return new MapLibreAdapter(options);
}
