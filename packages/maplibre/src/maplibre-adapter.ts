import "maplibre-gl/dist/maplibre-gl.css";

import { Map as MapLibreMap } from "maplibre-gl";

import {
  MAP_RUNTIME_PORT_PROFILE,
  MAP_RUNTIME_TRUST_STATE_REASONS,
  MapRuntimePortError,
  freezeMapRuntimeCamera,
  type MapFeatureSelection,
  type MapRuntimeCamera,
  type MapRuntimePort,
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
 * This first slice owns only renderer construction, camera synchronization,
 * responsive container resize, finite lifecycle state, and teardown. It starts
 * with an inline empty style, performs no source discovery, and exposes no raw
 * MapLibre values. Source, layer, selection, protocol, plugin, worker, and
 * external-style admission stay out of scope until separately governed inputs
 * and browser probes exist.
 */
export class MapLibreAdapter implements MapRuntimePort {
  readonly profile = MAP_RUNTIME_PORT_PROFILE;

  private readonly containerId: string;
  private readonly interactive: boolean;
  private readonly initializationDeadlineMs: number;
  private state: MapRuntimeState = "IDLE";
  private camera: MapRuntimeCamera = DEFAULT_MAP_RUNTIME_CAMERA;
  private selection: MapFeatureSelection | null = null;
  private reason: MapRuntimeReasonCode | null = null;
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
    try {
      this.notifySnapshot();
    } catch {
      if (this.state !== "DISPOSED") this.failInitialization();
      return initialization;
    }
    if (this.state === "DISPOSED") return initialization;

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
        if (this.state === "DISPOSED") return;
        try {
          this.camera = this.readRendererCamera(map);
          this.state = "READY";
          this.reason = null;
          this.clearInitializationDeadline();
          const snapshot = this.notifySnapshot();
          if (this.state === "DISPOSED") return;
          this.initialization = null;
          this.rejectInitialization = null;
          resolveInitialization(snapshot);
        } catch {
          if (this.state !== "DISPOSED") this.failInitialization();
        }
      });
      this.rendererUnsubscribers.add(loadSubscription.unsubscribe);

      const moveSubscription = map.on("moveend", () => {
        if (this.state !== "READY") return;
        try {
          const nextCamera = this.readRendererCamera(map);
          if (camerasEqual(this.camera, nextCamera)) return;
          this.camera = nextCamera;
          this.notifySnapshot();
        } catch {
          this.failRuntime();
        }
      });
      this.rendererUnsubscribers.add(moveSubscription.unsubscribe);

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
    } catch {
      this.failRuntime();
      throw new MapRuntimePortError(
        "MAP_RUNTIME_NAVIGATION_FAILED",
        "Map runtime navigation failed.",
      );
    }
    if (this.state !== "READY" || this.map !== map) {
      throw new MapRuntimePortError(
        "MAP_RUNTIME_NAVIGATION_FAILED",
        "Map runtime navigation failed.",
      );
    }
    this.camera = frozen;
    return this.notifySnapshot();
  }

  resize(): MapRuntimeSnapshot {
    this.assertReady();
    const map = this.map!;
    try {
      map.resize();
    } catch {
      this.failRuntime();
      throw new MapRuntimePortError(
        "MAP_RUNTIME_RESIZE_FAILED",
        "Map runtime resize failed.",
      );
    }
    if (this.state !== "READY" || this.map !== map) {
      throw new MapRuntimePortError(
        "MAP_RUNTIME_RESIZE_FAILED",
        "Map runtime resize failed.",
      );
    }
    return this.getSnapshot();
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
    this.clearRendererSubscriptions();
    const map = this.map;
    this.map = null;
    map?.remove();
    this.selection = null;
    this.state = "DISPOSED";
    this.reason = "MAP_RUNTIME_DISPOSED";
    this.notifySnapshot();
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
    if (this.state === "DISPOSED") return;
    this.clearInitializationDeadline();
    this.clearRenderer();
    this.selection = null;
    this.state = "ERROR";
    this.reason = MAP_RUNTIME_TRUST_STATE_REASONS.ERROR;
    try {
      this.notifySnapshot();
    } catch {
      // Snapshot listeners cannot leak renderer failures or prevent teardown.
    }
  }

  private clearInitializationDeadline(): void {
    if (this.initializationDeadline === null) return;
    clearTimeout(this.initializationDeadline);
    this.initializationDeadline = null;
  }

  private clearRenderer(): void {
    this.clearRendererSubscriptions();
    const map = this.map;
    this.map = null;
    map?.remove();
  }

  private clearRendererSubscriptions(): void {
    for (const unsubscribe of this.rendererUnsubscribers) unsubscribe();
    this.rendererUnsubscribers.clear();
  }

  private notifySnapshot(): MapRuntimeSnapshot {
    const snapshot = this.getSnapshot();
    for (const listener of [...this.snapshotListeners]) {
      try {
        listener(snapshot);
      } catch {
        // Snapshot listeners are observational consumers. A consumer failure
        // must not change renderer lifecycle, block later listeners, or leak
        // through the MapRuntimePort call that produced this snapshot.
      }
    }
    return snapshot;
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
    if (this.state === "DISPOSED") {
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
}

export function createMapLibreAdapter(
  options: MapLibreAdapterOptions,
): MapLibreAdapter {
  return new MapLibreAdapter(options);
}
