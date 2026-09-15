import "maplibre-gl/dist/maplibre-gl.css";

import { Map as MapLibreMap, type StyleSpecification } from "maplibre-gl";

import {
  MAP_RUNTIME_PORT_PROFILE,
  MAP_RUNTIME_TRUST_STATE_REASONS,
  MapRuntimePortError,
  freezeMapFeatureSelection,
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
const MAX_FIXTURE_SELECTIONS = 64;
const MAX_FIXTURE_QUERY_HITS = 128;

function createEmptyStyle() {
  return { version: 8 as const, sources: {}, layers: [] };
}

export type MapLibreSafeStyle = StyleSpecification;

const STYLE_RESOURCE_KEYS = new Set([
  "data",
  "glyphs",
  "sprite",
  "tiles",
  "url",
  "urls",
]);

function containsExternalStyleResource(value: unknown, key = ""): boolean {
  if (typeof value === "string") {
    return (
      STYLE_RESOURCE_KEYS.has(key) ||
      /^(?:https?:|data:|blob:|file:|pmtiles:)/i.test(value.trim())
    );
  }
  if (Array.isArray(value)) {
    return value.some((item) => containsExternalStyleResource(item, key));
  }
  if (typeof value !== "object" || value === null) return false;
  return Object.entries(value).some(([childKey, child]) =>
    containsExternalStyleResource(child, childKey),
  );
}

function cloneSafeInlineStyle(
  style: StyleSpecification | undefined,
): StyleSpecification {
  if (style === undefined) return createEmptyStyle();
  let cloned: unknown;
  try {
    cloned = JSON.parse(JSON.stringify(style)) as unknown;
  } catch {
    throw new MapRuntimePortError(
      "MAP_RUNTIME_INITIALIZATION_FAILED",
      "Map runtime style must be JSON-serializable.",
    );
  }
  if (containsExternalStyleResource(cloned)) {
    throw new MapRuntimePortError(
      "MAP_RUNTIME_INITIALIZATION_FAILED",
      "Map runtime style must not contain an external resource locator.",
    );
  }
  return cloned as StyleSpecification;
}

type FixtureSelectionBinding = Readonly<{
  selection: MapFeatureSelection;
  sourceId: string;
  rendererFeatureId: number;
}>;

function dependsOnFeatureId(value: unknown): boolean {
  if (value === "$id") return true;
  if (Array.isArray(value)) {
    return value[0] === "id" || value.some(dependsOnFeatureId);
  }
  return typeof value === "object" && value !== null &&
    Object.values(value).some(dependsOnFeatureId);
}

function fixtureSelectionBindings(
  selections: readonly MapFeatureSelection[] | undefined,
  style: StyleSpecification,
): readonly FixtureSelectionBinding[] {
  if (selections === undefined) return Object.freeze([]);
  const invalid = (): never => {
    throw new MapRuntimePortError(
      "MAP_RUNTIME_SELECTION_INVALID",
      "Map runtime fixture selections are invalid.",
    );
  };
  if (!Array.isArray(selections) || selections.length > MAX_FIXTURE_SELECTIONS) {
    return invalid();
  }
  const keys = new Set<string>();
  const ids = new Set<string>();
  const rendererSources = new Map<string, { id?: string | number }[]>();
  // Resolve every binding against the original IDs before changing the
  // package-owned clone. Several layers can share the same inline source.
  const bindings = selections.map((input) => {
    const selection = freezeMapFeatureSelection(input);
    const key = JSON.stringify([selection.layerId, selection.featureId]);
    if (keys.has(key) || ids.has(selection.selectionId)) return invalid();
    keys.add(key);
    ids.add(selection.selectionId);
    const layers = style.layers.filter((layer) => layer.id === selection.layerId);
    if (layers.length !== 1 || !("source" in layers[0])) return invalid();
    const sourceId = layers[0].source;
    if (typeof sourceId !== "string" || !Object.hasOwn(style.sources, sourceId)) {
      return invalid();
    }
    const source = style.sources[sourceId];
    if (source.type !== "geojson" || typeof source.data !== "object" || source.data === null) {
      return invalid();
    }
    // MapLibre can replace GeoJSON IDs from properties, enumeration or
    // clustering. Those identities are not the literal reviewed fixture IDs.
    if (source.promoteId !== undefined || source.generateId || source.cluster) return invalid();
    const features = source.data.type === "FeatureCollection"
      ? source.data.features
      : source.data.type === "Feature" ? [source.data] : [];
    const matches = features.filter((feature: { id?: string | number; properties?: Record<string, unknown> | null }) =>
      feature.id === selection.featureId,
    );
    if (matches.length !== 1 || matches[0].properties?.fixture !== true) return invalid();
    rendererSources.set(sourceId, features);
    return Object.freeze({ selection, sourceId, rendererFeatureId: features.indexOf(matches[0]) });
  });
  // GeoJSON tiling does not retain arbitrary string IDs. Use unique numeric
  // addresses only inside the cloned renderer projection, including unbound
  // features so none can alias an approved binding. Original KFM identities
  // and evidence references stay in the immutable binding, never properties.
  for (const [sourceId, features] of rendererSources) {
    // ID-dependent styling/filtering would change meaning after projection.
    // Keep that unsupported input fail-closed, including unbound sibling
    // layers that share this source.
    const source = style.sources[sourceId];
    if (source.type !== "geojson" || dependsOnFeatureId(source.filter)) return invalid();
    for (const layer of style.layers) {
      if (!("source" in layer) || layer.source !== sourceId) continue;
      if (dependsOnFeatureId(["filter" in layer ? layer.filter : undefined, layer.paint, layer.layout])) return invalid();
    }
    features.forEach((feature, index) => { feature.id = index; });
  }
  return Object.freeze(bindings);
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
  /**
   * Optional already-reviewed, inline-only style. External URLs and protocol
   * locators fail closed before renderer acquisition.
   */
  style?: StyleSpecification;
  /**
   * Optional pre-reviewed synthetic fixture bindings (at most 64). Each must
   * match one inline GeoJSON feature with properties.fixture === true.
   * This is identity translation, not policy, evidence or release admission.
   * Evidence references come only from these copied KFM-owned values.
   */
  fixtureSelections?: readonly MapFeatureSelection[];
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
 * This slice owns renderer construction, a bounded inline-only style input,
 * camera synchronization, finite lifecycle state, and teardown. It performs no
 * source discovery or transport and exposes no raw MapLibre values. External
 * source, layer, protocol, plugin, worker, and style admission stay out of scope
 * until separately governed inputs and browser probes exist.
 */
export class MapLibreAdapter implements MapRuntimePort {
  readonly profile = MAP_RUNTIME_PORT_PROFILE;

  private readonly containerId: string;
  private readonly interactive: boolean;
  private readonly initializationDeadlineMs: number;
  private readonly style: StyleSpecification;
  private readonly fixtureBindings: readonly FixtureSelectionBinding[];
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
    this.style = cloneSafeInlineStyle(options.style);
    this.fixtureBindings = fixtureSelectionBindings(options.fixtureSelections, this.style);
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
      if (!this.isDisposed()) this.failInitialization();
      return initialization;
    }
    if (this.isDisposed()) return initialization;

    if (!supportsWebGL2()) {
      this.failInitialization();
      return initialization;
    }

    try {
      if (this.map !== null) this.clearRenderer();
      const map = new MapLibreMap({
        container: this.containerId,
        style: this.style,
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
          this.camera = this.readRendererCamera(map);
          this.state = "READY";
          this.reason = null;
          this.clearInitializationDeadline();
          const snapshot = this.notifySnapshot();
          if (this.isDisposed()) return;
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
          if (camerasEqual(this.camera, nextCamera)) return;
          this.camera = nextCamera;
          this.notifySnapshot();
        } catch {
          this.failRuntime();
        }
      });
      this.rendererUnsubscribers.add(moveSubscription.unsubscribe);

      if (this.fixtureBindings.length > 0) {
        const layers = [...new Set(this.fixtureBindings.map(({ selection }) => selection.layerId))];
        const clickSubscription = map.on("click", (event) => {
          if (this.state !== "READY" || this.map !== map) return;
          try {
            const features = map.queryRenderedFeatures(event.point, { layers });
            if (features.length > MAX_FIXTURE_QUERY_HITS) return;
            let matched: MapFeatureSelection | null = null;
            for (const feature of features) {
              const binding = this.fixtureBindings.find((candidate) =>
                candidate.selection.layerId === feature.layer.id &&
                candidate.rendererFeatureId === feature.id &&
                candidate.sourceId === feature.source,
              );
              // Unknown or ambiguous hits must not fall through to a supported
              // feature. Renderer properties never supply evidence references.
              if (binding === undefined || (matched !== null && matched !== binding.selection)) return;
              matched = binding.selection;
            }
            if (matched === null) return;
            this.selection = matched;
            this.notifySnapshot();
            for (const listener of [...this.selectionListeners]) {
              if (this.state !== "READY" || this.map !== map || this.selection !== matched) break;
              listener(matched);
            }
          } catch {
            if (!this.isDisposed()) {
              try { this.failRuntime(); } catch { /* Listener failure stays finite. */ }
            }
          }
        });
        this.rendererUnsubscribers.add(clickSubscription.unsubscribe);
      }

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
    this.map!.jumpTo({
      center: [frozen.longitude, frozen.latitude],
      zoom: frozen.zoom,
      bearing: frozen.bearing,
      pitch: frozen.pitch,
    });
    this.camera = frozen;
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
    this.selection = null;
    this.state = "ERROR";
    this.reason = MAP_RUNTIME_TRUST_STATE_REASONS.ERROR;
    this.notifySnapshot();
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
    for (const listener of [...this.snapshotListeners]) listener(snapshot);
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

  private isDisposed(): boolean {
    return this.state === "DISPOSED";
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
