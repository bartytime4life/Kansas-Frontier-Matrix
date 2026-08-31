import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

type RendererHandler = (event?: unknown) => void;

type RendererInstance = {
  options: Record<string, unknown>;
  removed: boolean;
  jumpToCalls: Record<string, unknown>[];
  addSourceCalls: Array<readonly [string, Record<string, unknown>]>;
  addLayerCalls: Record<string, unknown>[];
  removeLayerCalls: string[];
  removeSourceCalls: string[];
  queryCalls: Array<readonly [unknown, Record<string, unknown>]>;
  emit: (type: string, event?: unknown) => void;
  listenerCount: () => number;
  setQueryFeatures: (features: Array<Record<string, unknown>>) => void;
  setObservedCamera: (camera: {
    longitude: number;
    latitude: number;
    zoom: number;
    bearing: number;
    pitch: number;
  }) => void;
};

const renderer = vi.hoisted(() => ({
  instances: [] as RendererInstance[],
  throwOnConstruct: false,
  throwOnAddSource: false,
  throwOnAddLayer: false,
  emitErrorOnAddLayer: false,
  throwOnRemoveLayer: false,
  throwOnRemoveSource: false,
  throwOnQuery: false,
  throwOnJumpTo: false,
  throwOnRemove: false,
}));

const capabilities = vi.hoisted(() => ({ webgl2: true }));

vi.mock("maplibre-gl", () => ({
  Map: class FakeMap {
    readonly options: Record<string, unknown>;
    readonly jumpToCalls: Record<string, unknown>[] = [];
    readonly addSourceCalls: Array<
      readonly [string, Record<string, unknown>]
    > = [];
    readonly addLayerCalls: Record<string, unknown>[] = [];
    readonly removeLayerCalls: string[] = [];
    readonly removeSourceCalls: string[] = [];
    readonly queryCalls: Array<
      readonly [unknown, Record<string, unknown>]
    > = [];
    removed = false;
    private queryFeatures: Array<Record<string, unknown>> = [];
    private readonly handlers = new globalThis.Map<
      string,
      Set<RendererHandler>
    >();
    private camera: {
      longitude: number;
      latitude: number;
      zoom: number;
      bearing: number;
      pitch: number;
    };

    constructor(options: Record<string, unknown>) {
      if (renderer.throwOnConstruct) throw new Error("synthetic constructor failure");
      this.options = options;
      const center = options.center as [number, number];
      this.camera = {
        longitude: center[0],
        latitude: center[1],
        zoom: options.zoom as number,
        bearing: options.bearing as number,
        pitch: options.pitch as number,
      };
      renderer.instances.push(this);
    }

    on(type: string, handler: RendererHandler): { unsubscribe: () => void } {
      const listeners = this.handlers.get(type) ?? new Set<RendererHandler>();
      listeners.add(handler);
      this.handlers.set(type, listeners);
      return { unsubscribe: () => listeners.delete(handler) };
    }

    emit(type: string, event?: unknown): void {
      for (const handler of [...(this.handlers.get(type) ?? [])]) {
        handler(
          event ?? { type, point: { x: 10, y: 10 }, error: { message: "synthetic renderer error" } },
        );
      }
    }

    listenerCount(): number {
      return [...this.handlers.values()].reduce(
        (total, listeners) => total + listeners.size,
        0,
      );
    }

    setQueryFeatures(features: Array<Record<string, unknown>>): void {
      this.queryFeatures = features;
    }

    addSource(id: string, source: Record<string, unknown>): void {
      if (renderer.throwOnAddSource) throw new Error("raw add-source failure");
      this.addSourceCalls.push([id, source]);
    }

    addLayer(layer: Record<string, unknown>): void {
      if (renderer.throwOnAddLayer) throw new Error("raw add-layer failure");
      if (renderer.emitErrorOnAddLayer) {
        this.emit("error");
        return;
      }
      this.addLayerCalls.push(layer);
    }

    removeLayer(id: string): void {
      if (renderer.throwOnRemoveLayer) throw new Error("raw remove-layer failure");
      this.removeLayerCalls.push(id);
    }

    removeSource(id: string): void {
      if (renderer.throwOnRemoveSource) throw new Error("raw remove-source failure");
      this.removeSourceCalls.push(id);
    }

    queryRenderedFeatures(
      point: unknown,
      options: Record<string, unknown>,
    ): Array<Record<string, unknown>> {
      if (renderer.throwOnQuery) throw new Error("raw query failure");
      this.queryCalls.push([point, options]);
      return this.queryFeatures;
    }

    getCenter(): { lng: number; lat: number } {
      return { lng: this.camera.longitude, lat: this.camera.latitude };
    }

    getZoom(): number {
      return this.camera.zoom;
    }

    getBearing(): number {
      return this.camera.bearing;
    }

    getPitch(): number {
      return this.camera.pitch;
    }

    jumpTo(options: Record<string, unknown>): this {
      if (renderer.throwOnJumpTo) throw new Error("raw camera failure");
      this.jumpToCalls.push(options);
      const center = options.center as [number, number];
      this.camera = {
        longitude: center[0],
        latitude: center[1],
        zoom: options.zoom as number,
        bearing: options.bearing as number,
        pitch: options.pitch as number,
      };
      return this;
    }

    setObservedCamera(camera: typeof this.camera): void {
      this.camera = camera;
    }

    remove(): void {
      if (renderer.throwOnRemove) throw new Error("raw teardown failure");
      this.removed = true;
    }
  },
}));

import {
  MAP_FEATURE_SELECTION_PROFILE,
  MAP_RUNTIME_INLINE_GEOJSON_LAYER_PROFILE,
  MAP_RUNTIME_PORT_PROFILE,
  MapRuntimePortError,
  type MapRuntimeInlineGeoJsonLayer,
} from "../src/index";
import {
  DEFAULT_MAPLIBRE_INITIALIZATION_DEADLINE_MS,
  createMapLibreAdapter,
} from "../src/maplibre-adapter";

function inlineLayer(
  evidenceRef = "kfm:evidence:synthetic:flow-001",
): MapRuntimeInlineGeoJsonLayer {
  return {
    profile: MAP_RUNTIME_INLINE_GEOJSON_LAYER_PROFILE,
    sourceId: "source:synthetic-streamflow",
    layerId: "layer:synthetic-streamflow",
    kind: "circle",
    data: {
      type: "FeatureCollection",
      features: [
        {
          type: "Feature",
          id: "feature:flow-001",
          geometry: { type: "Point", coordinates: [-98.5, 38.5] },
          properties: null,
        },
      ],
    },
    selection: {
      profile: MAP_FEATURE_SELECTION_PROFILE,
      selectionId: "selection:flow-001",
      layerId: "layer:synthetic-streamflow",
      featureId: "feature:flow-001",
      evidenceRefs: [evidenceRef],
    },
  };
}

describe("package-owned MapLibreAdapter", () => {
  beforeEach(() => {
    renderer.instances.length = 0;
    renderer.throwOnConstruct = false;
    renderer.throwOnAddSource = false;
    renderer.throwOnAddLayer = false;
    renderer.emitErrorOnAddLayer = false;
    renderer.throwOnRemoveLayer = false;
    renderer.throwOnRemoveSource = false;
    renderer.throwOnQuery = false;
    renderer.throwOnJumpTo = false;
    renderer.throwOnRemove = false;
    capabilities.webgl2 = true;
    vi.stubGlobal("document", {
      createElement: () => ({
        getContext: (type: string) =>
          type === "webgl2" && capabilities.webgl2
            ? { getExtension: () => null }
            : null,
      }),
    });
  });

  afterEach(() => {
    vi.useRealTimers();
    vi.unstubAllGlobals();
  });

  it("fails closed before renderer acquisition for an invalid container ID", () => {
    expect(() => createMapLibreAdapter({ containerId: " unsafe container " })).toThrow(
      expect.objectContaining({ code: "MAP_RUNTIME_CONTAINER_INVALID" }),
    );
    expect(renderer.instances).toHaveLength(0);
  });

  it.each([0, -1, 1.5, 60_001, Number.POSITIVE_INFINITY])(
    "rejects an unbounded initialization deadline before renderer acquisition (%s)",
    (initializationDeadlineMs) => {
      expect(() =>
        createMapLibreAdapter({
          containerId: "kfm-map-root",
          initializationDeadlineMs,
        }),
      ).toThrow(
        expect.objectContaining({ code: "MAP_RUNTIME_INITIALIZATION_FAILED" }),
      );
      expect(renderer.instances).toHaveLength(0);
    },
  );

  it("settles a never-loading renderer to finite ERROR at the injected deadline", async () => {
    vi.useFakeTimers();
    expect(DEFAULT_MAPLIBRE_INITIALIZATION_DEADLINE_MS).toBe(10_000);
    const runtime = createMapLibreAdapter({
      containerId: "kfm-map-root",
      initializationDeadlineMs: 25,
    });
    const listener = vi.fn();
    runtime.subscribeSnapshot(listener);
    const pending = runtime.initialize();
    const rejection = expect(pending).rejects.toMatchObject({
      name: "MapRuntimePortError",
      code: "MAP_RUNTIME_INITIALIZATION_FAILED",
      message: "Map runtime initialization failed.",
    });
    const map = renderer.instances[0];

    expect(vi.getTimerCount()).toBe(1);
    await vi.advanceTimersByTimeAsync(24);
    expect(runtime.getSnapshot()).toMatchObject({ state: "INITIALIZING" });

    await vi.advanceTimersByTimeAsync(1);
    await rejection;
    expect(runtime.getSnapshot()).toMatchObject({
      state: "ERROR",
      reason: "MAP_RUNTIME_ERROR",
      selection: null,
    });
    expect(map.removed).toBe(true);
    expect(map.listenerCount()).toBe(0);
    expect(vi.getTimerCount()).toBe(0);
    expect(listener.mock.calls.map(([snapshot]) => snapshot.state)).toEqual([
      "INITIALIZING",
      "ERROR",
    ]);

    map.emit("load");
    expect(runtime.getSnapshot().state).toBe("ERROR");
  });

  it("clears the initialization deadline when the renderer becomes ready", async () => {
    vi.useFakeTimers();
    const runtime = createMapLibreAdapter({
      containerId: "kfm-map-root",
      initializationDeadlineMs: 25,
    });
    const pending = runtime.initialize();
    const map = renderer.instances[0];

    expect(vi.getTimerCount()).toBe(1);
    map.emit("load");
    await expect(pending).resolves.toMatchObject({ state: "READY" });
    expect(vi.getTimerCount()).toBe(0);

    await vi.advanceTimersByTimeAsync(25);
    expect(runtime.getSnapshot()).toMatchObject({ state: "READY", reason: null });
  });

  it("fails closed before renderer construction when WebGL2 is unavailable", async () => {
    capabilities.webgl2 = false;
    const runtime = createMapLibreAdapter({ containerId: "kfm-map-root" });

    await expect(runtime.initialize()).rejects.toMatchObject({
      code: "MAP_RUNTIME_INITIALIZATION_FAILED",
    });
    expect(renderer.instances).toHaveLength(0);
    expect(runtime.getSnapshot()).toMatchObject({
      state: "ERROR",
      reason: "MAP_RUNTIME_ERROR",
    });
  });

  it("initializes with an inline empty style and synchronizes camera state", async () => {
    const runtime = createMapLibreAdapter({
      containerId: "kfm-map-root",
      interactive: false,
    });
    const listener = vi.fn();
    runtime.subscribeSnapshot(listener);

    const initialCamera = {
      longitude: -98.4842,
      latitude: 38.4988,
      zoom: 6,
      bearing: 10,
      pitch: 20,
    } as const;
    const pending = runtime.initialize(initialCamera);
    const map = renderer.instances[0];

    expect(runtime.getSnapshot()).toMatchObject({
      profile: MAP_RUNTIME_PORT_PROFILE,
      state: "INITIALIZING",
      camera: initialCamera,
      selection: null,
      reason: null,
    });
    expect(map.options).toMatchObject({
      container: "kfm-map-root",
      center: [-98.4842, 38.4988],
      interactive: false,
      hash: false,
      attributionControl: false,
      maplibreLogo: false,
      style: { version: 8, sources: {}, layers: [] },
    });

    map.emit("load");
    await expect(pending).resolves.toMatchObject({ state: "READY" });

    const requestedCamera = {
      longitude: -97,
      latitude: 39,
      zoom: 8,
      bearing: -15,
      pitch: 30,
    } as const;
    expect(runtime.setCamera(requestedCamera)).toMatchObject({
      state: "READY",
      camera: requestedCamera,
    });
    expect(map.jumpToCalls).toEqual([
      {
        center: [-97, 39],
        zoom: 8,
        bearing: -15,
        pitch: 30,
      },
    ]);

    map.setObservedCamera({
      longitude: -96.5,
      latitude: 38.5,
      zoom: 8.5,
      bearing: 0,
      pitch: 25,
    });
    map.emit("moveend");
    expect(runtime.getSnapshot().camera).toEqual({
      longitude: -96.5,
      latitude: 38.5,
      zoom: 8.5,
      bearing: 0,
      pitch: 25,
    });
    expect(Object.keys(runtime.getSnapshot()).sort()).toEqual([
      "camera",
      "profile",
      "reason",
      "selection",
      "state",
    ]);
    expect(listener).toHaveBeenCalled();

    runtime.dispose();
    expect(map.removed).toBe(true);
    expect(runtime.getSnapshot()).toMatchObject({
      state: "DISPOSED",
      reason: "MAP_RUNTIME_DISPOSED",
      selection: null,
    });
    expect(map.listenerCount()).toBe(0);
  });

  it("binds one bounded source/layer and normalizes pointer and accessible selection", async () => {
    const runtime = createMapLibreAdapter({ containerId: "kfm-map-root" });
    const selectionListener = vi.fn();
    const pending = runtime.initialize();
    const map = renderer.instances[0];
    map.emit("load");
    await pending;
    runtime.subscribeSelection(selectionListener);
    runtime.subscribeSnapshot((snapshot) => {
      if (snapshot.selection !== null) throw new Error("synthetic snapshot listener");
    });
    runtime.subscribeSelection(() => {
      throw new Error("synthetic selection listener");
    });

    expect(runtime.bindInlineGeoJsonLayer(inlineLayer())).toMatchObject({
      state: "READY",
      selection: null,
      reason: null,
    });
    expect(map.addSourceCalls).toEqual([
      [
        "source:synthetic-streamflow",
        {
          type: "geojson",
          data: {
            type: "FeatureCollection",
            features: [
              {
                type: "Feature",
                id: "feature:flow-001",
                geometry: { type: "Point", coordinates: [-98.5, 38.5] },
                properties: null,
              },
            ],
          },
        },
      ],
    ]);
    expect(JSON.stringify(map.addSourceCalls)).not.toContain(
      "kfm:evidence:synthetic:flow-001",
    );
    expect(map.addLayerCalls).toEqual([
      {
        id: "layer:synthetic-streamflow",
        type: "circle",
        source: "source:synthetic-streamflow",
        paint: {
          "circle-color": "#0f766e",
          "circle-radius": 9,
          "circle-stroke-color": "#ffffff",
          "circle-stroke-width": 2,
        },
      },
    ]);

    map.setQueryFeatures([
      {
        id: "renderer:untrusted-id",
        properties: { evidenceRefs: ["forged:renderer:evidence"] },
      },
    ]);
    expect(() => map.emit("click", { point: { x: 20, y: 30 } })).not.toThrow();
    expect(map.queryCalls).toEqual([
      [
        { x: 20, y: 30 },
        { layers: ["layer:synthetic-streamflow"] },
      ],
    ]);
    expect(selectionListener).toHaveBeenLastCalledWith(inlineLayer().selection);

    expect(() =>
      runtime.selectFeature(
        "layer:synthetic-streamflow",
        "feature:flow-001",
      ),
    ).not.toThrow();
    expect(selectionListener).toHaveBeenCalledTimes(2);
    expect(selectionListener.mock.calls[0]?.[0]).toEqual(
      selectionListener.mock.calls[1]?.[0],
    );
    expect(selectionListener.mock.calls[1]?.[0].evidenceRefs).toEqual([
      "kfm:evidence:synthetic:flow-001",
    ]);
    expect(runtime.getSnapshot()).toMatchObject({
      state: "READY",
      selection: inlineLayer().selection,
      reason: null,
    });
  });

  it("invalidates removed and replaced selections and releases owned resources", async () => {
    const runtime = createMapLibreAdapter({ containerId: "kfm-map-root" });
    const pending = runtime.initialize();
    const map = renderer.instances[0];
    map.emit("load");
    await pending;
    runtime.bindInlineGeoJsonLayer(inlineLayer());
    runtime.selectFeature("layer:synthetic-streamflow", "feature:flow-001");

    expect(runtime.removeLayer("layer:synthetic-streamflow")).toMatchObject({
      state: "READY",
      selection: null,
      reason: "MAP_RUNTIME_SELECTION_INVALIDATED",
    });
    expect(map.removeLayerCalls).toEqual(["layer:synthetic-streamflow"]);
    expect(runtime.removeSource("source:synthetic-streamflow")).toMatchObject({
      state: "READY",
      selection: null,
      reason: null,
    });
    expect(map.removeSourceCalls).toEqual(["source:synthetic-streamflow"]);

    runtime.bindInlineGeoJsonLayer(inlineLayer());
    runtime.selectFeature("layer:synthetic-streamflow", "feature:flow-001");
    expect(
      runtime.bindInlineGeoJsonLayer(
        inlineLayer("kfm:evidence:synthetic:flow-002"),
      ),
    ).toMatchObject({
      state: "READY",
      selection: null,
      reason: "MAP_RUNTIME_SELECTION_INVALIDATED",
    });
    expect(map.removeLayerCalls).toEqual([
      "layer:synthetic-streamflow",
      "layer:synthetic-streamflow",
    ]);
    expect(map.removeSourceCalls).toEqual([
      "source:synthetic-streamflow",
      "source:synthetic-streamflow",
    ]);
    expect(map.addSourceCalls).toHaveLength(3);
    expect(map.addLayerCalls).toHaveLength(3);
    expect(map.listenerCount()).toBe(3);

    for (const evidenceRef of [
      "kfm:evidence:synthetic:flow-003",
      "kfm:evidence:synthetic:flow-004",
    ]) {
      runtime.selectFeature("layer:synthetic-streamflow", "feature:flow-001");
      expect(
        runtime.bindInlineGeoJsonLayer(inlineLayer(evidenceRef)),
      ).toMatchObject({
        state: "READY",
        selection: null,
        reason: "MAP_RUNTIME_SELECTION_INVALIDATED",
      });
      expect(map.listenerCount()).toBe(3);
    }

    runtime.selectFeature("layer:synthetic-streamflow", "feature:flow-001");
    expect(runtime.removeSource("source:synthetic-streamflow")).toMatchObject({
      selection: null,
      reason: "MAP_RUNTIME_SELECTION_INVALIDATED",
    });
    expect(map.removeLayerCalls).toHaveLength(5);
    expect(map.removeSourceCalls).toHaveLength(5);
    runtime.dispose();
    expect(map.listenerCount()).toBe(0);
    expect(runtime.getSnapshot()).toMatchObject({
      state: "DISPOSED",
      selection: null,
      reason: "MAP_RUNTIME_DISPOSED",
    });
  });

  it("returns the post-callback state when bind observers throw and dispose", async () => {
    const runtime = createMapLibreAdapter({ containerId: "kfm-map-root" });
    const pending = runtime.initialize();
    const map = renderer.instances[0];
    map.emit("load");
    await pending;
    const throwingObserver = vi.fn(() => {
      throw new Error("synthetic bind observer failure");
    });
    const trailingObserver = vi.fn();
    runtime.subscribeSnapshot(throwingObserver);
    runtime.subscribeSnapshot(() => runtime.dispose());
    runtime.subscribeSnapshot(trailingObserver);

    expect(runtime.bindInlineGeoJsonLayer(inlineLayer())).toMatchObject({
      state: "DISPOSED",
      selection: null,
      reason: "MAP_RUNTIME_DISPOSED",
    });
    expect(
      throwingObserver.mock.calls.map(([snapshot]) => snapshot.state),
    ).toEqual(["READY", "DISPOSED"]);
    expect(
      trailingObserver.mock.calls.map(([snapshot]) => snapshot.state),
    ).toEqual(["DISPOSED"]);
    expect(map.removed).toBe(true);
  });

  it("returns the post-callback state when removal observers throw and dispose", async () => {
    const runtime = createMapLibreAdapter({ containerId: "kfm-map-root" });
    const pending = runtime.initialize();
    const map = renderer.instances[0];
    map.emit("load");
    await pending;
    runtime.bindInlineGeoJsonLayer(inlineLayer());
    const throwingObserver = vi.fn(() => {
      throw new Error("synthetic removal observer failure");
    });
    const trailingObserver = vi.fn();
    runtime.subscribeSnapshot(throwingObserver);
    runtime.subscribeSnapshot(() => runtime.dispose());
    runtime.subscribeSnapshot(trailingObserver);

    expect(runtime.removeLayer("layer:synthetic-streamflow")).toMatchObject({
      state: "DISPOSED",
      selection: null,
      reason: "MAP_RUNTIME_DISPOSED",
    });
    expect(
      throwingObserver.mock.calls.map(([snapshot]) => snapshot.state),
    ).toEqual(["READY", "DISPOSED"]);
    expect(
      trailingObserver.mock.calls.map(([snapshot]) => snapshot.state),
    ).toEqual(["DISPOSED"]);
    expect(map.removed).toBe(true);
  });

  it("stops selection fanout when a publish observer disposes then throws", async () => {
    const runtime = createMapLibreAdapter({ containerId: "kfm-map-root" });
    const pending = runtime.initialize();
    const map = renderer.instances[0];
    map.emit("load");
    await pending;
    runtime.bindInlineGeoJsonLayer(inlineLayer());
    const selectionObserver = vi.fn();
    runtime.subscribeSnapshot((snapshot) => {
      if (snapshot.selection === null) return;
      runtime.dispose();
      throw new Error("synthetic publish observer failure after disposal");
    });
    runtime.subscribeSelection(selectionObserver);

    expect(
      runtime.selectFeature("layer:synthetic-streamflow", "feature:flow-001"),
    ).toMatchObject({
      state: "DISPOSED",
      selection: null,
      reason: "MAP_RUNTIME_DISPOSED",
    });
    expect(selectionObserver).not.toHaveBeenCalled();
    expect(map.removed).toBe(true);
  });

  it("rejects invalid and unknown binding operations without renderer effects", async () => {
    const runtime = createMapLibreAdapter({ containerId: "kfm-map-root" });
    const pending = runtime.initialize();
    const map = renderer.instances[0];
    map.emit("load");
    await pending;

    expect(() =>
      runtime.bindInlineGeoJsonLayer({
        ...inlineLayer(),
        selection: { ...inlineLayer().selection, featureId: "feature:other" },
      }),
    ).toThrow(expect.objectContaining({ code: "MAP_RUNTIME_LAYER_INVALID" }));
    expect(map.addSourceCalls).toHaveLength(0);
    expect(map.addLayerCalls).toHaveLength(0);

    runtime.bindInlineGeoJsonLayer(inlineLayer());
    expect(() => runtime.removeLayer("layer:other")).toThrow(
      expect.objectContaining({ code: "MAP_RUNTIME_LAYER_NOT_FOUND" }),
    );
    expect(() => runtime.removeSource("source:other")).toThrow(
      expect.objectContaining({ code: "MAP_RUNTIME_SOURCE_NOT_FOUND" }),
    );
    expect(() =>
      runtime.selectFeature("layer:synthetic-streamflow", "feature:other"),
    ).toThrow(expect.objectContaining({ code: "MAP_RUNTIME_FEATURE_NOT_FOUND" }));
  });

  it("maps source/layer binding failure to a finite KFM error and full teardown", async () => {
    const runtime = createMapLibreAdapter({ containerId: "kfm-map-root" });
    const pending = runtime.initialize();
    const map = renderer.instances[0];
    map.emit("load");
    await pending;
    renderer.throwOnAddLayer = true;

    expect(() => runtime.bindInlineGeoJsonLayer(inlineLayer())).toThrow(
      expect.objectContaining({
        name: "MapRuntimePortError",
        code: "MAP_RUNTIME_LAYER_BIND_FAILED",
        message: "Inline GeoJSON map layer binding failed.",
      }),
    );
    expect(runtime.getSnapshot()).toMatchObject({
      state: "ERROR",
      selection: null,
      reason: "MAP_RUNTIME_ERROR",
    });
    expect(map.removed).toBe(true);
    expect(map.listenerCount()).toBe(0);
  });

  it("maps a synchronous renderer error event during binding and leaves no stale binding", async () => {
    const runtime = createMapLibreAdapter({ containerId: "kfm-map-root" });
    const pending = runtime.initialize();
    const firstMap = renderer.instances[0];
    firstMap.emit("load");
    await pending;
    renderer.emitErrorOnAddLayer = true;

    expect(() => runtime.bindInlineGeoJsonLayer(inlineLayer())).toThrow(
      expect.objectContaining({
        code: "MAP_RUNTIME_LAYER_BIND_FAILED",
        message: "Inline GeoJSON map layer binding failed.",
      }),
    );
    expect(runtime.getSnapshot()).toMatchObject({
      state: "ERROR",
      selection: null,
      reason: "MAP_RUNTIME_ERROR",
    });
    expect(firstMap.removed).toBe(true);
    expect(firstMap.listenerCount()).toBe(0);

    renderer.emitErrorOnAddLayer = false;
    const retry = runtime.initialize();
    const secondMap = renderer.instances[1];
    secondMap.emit("load");
    await expect(retry).resolves.toMatchObject({ state: "READY" });
    expect(() =>
      runtime.selectFeature("layer:synthetic-streamflow", "feature:flow-001"),
    ).toThrow(expect.objectContaining({ code: "MAP_RUNTIME_LAYER_NOT_FOUND" }));
    expect(secondMap.addSourceCalls).toHaveLength(0);
    expect(secondMap.addLayerCalls).toHaveLength(0);
  });

  it("maps pointer-query failure to finite ERROR and cannot emit stale selection", async () => {
    const runtime = createMapLibreAdapter({ containerId: "kfm-map-root" });
    const selectionListener = vi.fn();
    const pending = runtime.initialize();
    const map = renderer.instances[0];
    map.emit("load");
    await pending;
    runtime.subscribeSelection(selectionListener);
    runtime.bindInlineGeoJsonLayer(inlineLayer());
    renderer.throwOnQuery = true;

    map.emit("click", { point: { x: 20, y: 30 } });

    expect(runtime.getSnapshot()).toMatchObject({
      state: "ERROR",
      selection: null,
      reason: "MAP_RUNTIME_ERROR",
    });
    expect(selectionListener).not.toHaveBeenCalled();
    expect(map.removed).toBe(true);
    expect(map.listenerCount()).toBe(0);
  });

  it("maps camera, removal, and teardown exceptions without leaking renderer errors", async () => {
    const cameraRuntime = createMapLibreAdapter({ containerId: "camera-map" });
    const cameraPending = cameraRuntime.initialize();
    const cameraMap = renderer.instances[0];
    cameraMap.emit("load");
    await cameraPending;
    renderer.throwOnJumpTo = true;

    expect(() => cameraRuntime.setCamera(cameraRuntime.getSnapshot().camera)).toThrow(
      expect.objectContaining({
        code: "MAP_RUNTIME_CAMERA_UPDATE_FAILED",
        message: "Map runtime camera update failed.",
      }),
    );
    expect(cameraRuntime.getSnapshot()).toMatchObject({
      state: "ERROR",
      reason: "MAP_RUNTIME_ERROR",
    });
    expect(cameraMap.removed).toBe(true);

    renderer.throwOnJumpTo = false;
    const removalRuntime = createMapLibreAdapter({ containerId: "removal-map" });
    const removalPending = removalRuntime.initialize();
    const removalMap = renderer.instances[1];
    removalMap.emit("load");
    await removalPending;
    removalRuntime.bindInlineGeoJsonLayer(inlineLayer());
    renderer.throwOnRemoveLayer = true;

    expect(() => removalRuntime.removeLayer("layer:synthetic-streamflow")).toThrow(
      expect.objectContaining({
        code: "MAP_RUNTIME_LAYER_REMOVAL_FAILED",
        message: "Map runtime layer removal failed.",
      }),
    );
    expect(removalRuntime.getSnapshot()).toMatchObject({
      state: "ERROR",
      selection: null,
      reason: "MAP_RUNTIME_ERROR",
    });
    expect(removalMap.removed).toBe(true);

    renderer.throwOnRemoveLayer = false;
    const sourceRuntime = createMapLibreAdapter({ containerId: "source-map" });
    const sourcePending = sourceRuntime.initialize();
    const sourceMap = renderer.instances[2];
    sourceMap.emit("load");
    await sourcePending;
    sourceRuntime.bindInlineGeoJsonLayer(inlineLayer());
    renderer.throwOnRemoveSource = true;

    expect(() => sourceRuntime.removeSource("source:synthetic-streamflow")).toThrow(
      expect.objectContaining({
        code: "MAP_RUNTIME_SOURCE_REMOVAL_FAILED",
        message: "Map runtime source removal failed.",
      }),
    );
    expect(sourceRuntime.getSnapshot()).toMatchObject({
      state: "ERROR",
      selection: null,
      reason: "MAP_RUNTIME_ERROR",
    });
    expect(sourceMap.removed).toBe(true);

    renderer.throwOnRemoveSource = false;
    const teardownRuntime = createMapLibreAdapter({ containerId: "teardown-map" });
    const teardownPending = teardownRuntime.initialize();
    const teardownMap = renderer.instances[3];
    teardownMap.emit("load");
    await teardownPending;
    renderer.throwOnRemove = true;
    teardownRuntime.subscribeSnapshot((snapshot) => {
      if (snapshot.state === "DISPOSED") {
        throw new Error("synthetic disposal listener failure");
      }
    });

    expect(() => teardownRuntime.dispose()).not.toThrow();
    expect(teardownRuntime.getSnapshot()).toMatchObject({
      state: "DISPOSED",
      selection: null,
      reason: "MAP_RUNTIME_DISPOSED",
    });
    expect(teardownMap.listenerCount()).toBe(0);
  });

  it("cleans a failed ready renderer before a finite retry", async () => {
    const runtime = createMapLibreAdapter({ containerId: "kfm-map-root" });
    const pending = runtime.initialize();
    const firstMap = renderer.instances[0];
    firstMap.emit("load");
    await pending;
    runtime.bindInlineGeoJsonLayer(inlineLayer());

    firstMap.emit("error");
    expect(firstMap.removed).toBe(true);
    expect(firstMap.listenerCount()).toBe(0);
    expect(runtime.getSnapshot()).toMatchObject({
      state: "ERROR",
      selection: null,
      reason: "MAP_RUNTIME_ERROR",
    });

    const retry = runtime.initialize();
    const secondMap = renderer.instances[1];
    secondMap.emit("load");
    await expect(retry).resolves.toMatchObject({ state: "READY", reason: null });
    expect(secondMap.listenerCount()).toBe(3);
  });

  it("maps renderer initialization errors to one KFM-owned failure", async () => {
    vi.useFakeTimers();
    const runtime = createMapLibreAdapter({ containerId: "kfm-map-root" });
    const pending = runtime.initialize();
    const map = renderer.instances[0];

    expect(vi.getTimerCount()).toBe(1);

    map.emit("error");

    await expect(pending).rejects.toMatchObject({
      name: "MapRuntimePortError",
      code: "MAP_RUNTIME_INITIALIZATION_FAILED",
    });
    expect(map.removed).toBe(true);
    expect(runtime.getSnapshot()).toMatchObject({
      state: "ERROR",
      reason: "MAP_RUNTIME_ERROR",
      selection: null,
    });
    expect(vi.getTimerCount()).toBe(0);
    expect(() => runtime.setCamera(runtime.getSnapshot().camera)).toThrow(
      MapRuntimePortError,
    );
  });

  it("fails closed when renderer construction throws", async () => {
    renderer.throwOnConstruct = true;
    const runtime = createMapLibreAdapter({ containerId: "kfm-map-root" });

    await expect(runtime.initialize()).rejects.toMatchObject({
      code: "MAP_RUNTIME_INITIALIZATION_FAILED",
    });
    expect(renderer.instances).toHaveLength(0);
    expect(runtime.getSnapshot()).toMatchObject({
      state: "ERROR",
      reason: "MAP_RUNTIME_ERROR",
    });

    renderer.throwOnConstruct = false;
    const retry = runtime.initialize();
    renderer.instances[0].emit("load");
    await expect(retry).resolves.toMatchObject({ state: "READY", reason: null });
  });

  it("rejects an in-flight initialization when disposed", async () => {
    vi.useFakeTimers();
    const runtime = createMapLibreAdapter({ containerId: "kfm-map-root" });
    const pending = runtime.initialize();
    const map = renderer.instances[0];

    expect(vi.getTimerCount()).toBe(1);

    runtime.dispose();

    await expect(pending).rejects.toMatchObject({ code: "MAP_RUNTIME_DISPOSED" });
    expect(map.removed).toBe(true);
    expect(runtime.getSnapshot().state).toBe("DISPOSED");
    expect(vi.getTimerCount()).toBe(0);
  });

  it("stops initialization when a snapshot listener disposes synchronously", async () => {
    const runtime = createMapLibreAdapter({ containerId: "kfm-map-root" });
    runtime.subscribeSnapshot((snapshot) => {
      if (snapshot.state === "INITIALIZING") runtime.dispose();
    });

    const pending = runtime.initialize();

    expect(renderer.instances).toHaveLength(0);
    await expect(pending).rejects.toMatchObject({ code: "MAP_RUNTIME_DISPOSED" });
    expect(runtime.getSnapshot()).toMatchObject({
      state: "DISPOSED",
      reason: "MAP_RUNTIME_DISPOSED",
    });
  });

  it("isolates an initializing snapshot listener exception", async () => {
    const runtime = createMapLibreAdapter({ containerId: "kfm-map-root" });
    runtime.subscribeSnapshot((snapshot) => {
      if (snapshot.state === "INITIALIZING") {
        throw new Error("synthetic listener failure");
      }
    });

    const pending = runtime.initialize();
    expect(renderer.instances).toHaveLength(1);
    renderer.instances[0].emit("load");

    await expect(pending).resolves.toMatchObject({ state: "READY", reason: null });
  });

  it("preserves disposal when an initializing listener disposes then throws", async () => {
    const runtime = createMapLibreAdapter({ containerId: "kfm-map-root" });
    runtime.subscribeSnapshot((snapshot) => {
      if (snapshot.state !== "INITIALIZING") return;
      runtime.dispose();
      throw new Error("synthetic listener failure after disposal");
    });

    const pending = runtime.initialize();

    expect(renderer.instances).toHaveLength(0);
    await expect(pending).rejects.toMatchObject({ code: "MAP_RUNTIME_DISPOSED" });
    expect(runtime.getSnapshot()).toMatchObject({
      state: "DISPOSED",
      reason: "MAP_RUNTIME_DISPOSED",
    });
  });
});
