import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

type RendererHandler = (event?: unknown) => void;

type RendererInstance = {
  options: Record<string, unknown>;
  removed: boolean;
  jumpToCalls: Record<string, unknown>[];
  emit: (type: string, event?: unknown) => void;
  queryCalls: number;
  renderedFeatures: unknown[];
  queryError: boolean;
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
}));

const capabilities = vi.hoisted(() => ({ webgl2: true }));

vi.mock("maplibre-gl", () => ({
  Map: class FakeMap {
    readonly options: Record<string, unknown>;
    readonly jumpToCalls: Record<string, unknown>[] = [];
    removed = false;
    queryCalls = 0;
    renderedFeatures: unknown[] = [];
    queryError = false;
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
        handler(event ?? { type, point: { x: 10, y: 20 }, error: { message: "synthetic renderer error" } });
      }
    }

    queryRenderedFeatures(): unknown[] {
      this.queryCalls += 1;
      if (this.queryError) throw new Error("synthetic query failure");
      return this.renderedFeatures;
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
      this.removed = true;
    }
  },
}));

import {
  MAP_RUNTIME_PORT_PROFILE,
  MAP_FEATURE_SELECTION_PROFILE,
  MapRuntimePortError,
} from "../src/index";
import { createMapLibreAdapter } from "../src/maplibre-adapter";

function fixtureSelection(featureId = "feature:fixture:kansas-001") {
  return {
    profile: MAP_FEATURE_SELECTION_PROFILE,
    selectionId: `selection:${featureId}`,
    layerId: "layer:fixture:kansas",
    featureId,
    evidenceRefs: ["kfm:evidence:synthetic:flow-001"],
    historyEvidenceRefs: ["kfm:evidence:synthetic:flow-000"],
  };
}

function fixtureStyle() {
  return {
    version: 8 as const,
    sources: {
      "source:fixture:kansas": {
        type: "geojson" as const,
        data: {
          type: "FeatureCollection" as const,
          features: ["feature:fixture:kansas-001", "feature:fixture:kansas-002"].map((id) => ({
            type: "Feature" as const,
            id,
            properties: { fixture: true },
            geometry: { type: "Point" as const, coordinates: [-98.5, 38.5] },
          })),
        },
      },
    },
    layers: [{ id: "layer:fixture:kansas", type: "circle" as const, source: "source:fixture:kansas" }],
  };
}

function renderedFixture(featureId = 0) {
  return {
    id: featureId,
    layer: { id: "layer:fixture:kansas" },
    source: "source:fixture:kansas",
    properties: { evidence_refs: ["UNTRUSTED_RENDERER_PROPERTY"], fixture: true },
  };
}

describe("package-owned MapLibreAdapter", () => {
  beforeEach(() => {
    renderer.instances.length = 0;
    renderer.throwOnConstruct = false;
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

  afterEach(() => vi.unstubAllGlobals());

  it("fails closed before renderer acquisition for an invalid container ID", () => {
    expect(() => createMapLibreAdapter({ containerId: " unsafe container " })).toThrow(
      expect.objectContaining({ code: "MAP_RUNTIME_CONTAINER_INVALID" }),
    );
    expect(renderer.instances).toHaveLength(0);
  });

  it("fails closed before renderer acquisition for external style resources", () => {
    expect(() =>
      createMapLibreAdapter({
        containerId: "safe-map",
        style: {
          version: 8,
          sources: {
            external: {
              type: "raster",
              tiles: ["https://example.invalid/{z}/{x}/{y}.png"],
              tileSize: 256,
            },
          },
          layers: [],
        },
      }),
    ).toThrow(
      expect.objectContaining({ code: "MAP_RUNTIME_INITIALIZATION_FAILED" }),
    );
    expect(renderer.instances).toHaveLength(0);
  });

  it("fails closed when serialization reveals an external locator", () => {
    expect(() =>
      createMapLibreAdapter({
        containerId: "safe-map",
        style: {
          version: 8,
          sources: {
            external: {
              type: "geojson",
              data: new URL("https://example.invalid/data.geojson") as never,
            },
          },
          layers: [],
        },
      }),
    ).toThrow(
      expect.objectContaining({ code: "MAP_RUNTIME_INITIALIZATION_FAILED" }),
    );
    expect(renderer.instances).toHaveLength(0);
  });

  it("fails closed for relative resource paths as well as absolute URLs", () => {
    expect(() =>
      createMapLibreAdapter({
        containerId: "safe-map",
        style: {
          version: 8,
          glyphs: "/fonts/{fontstack}/{range}.pbf",
          sources: {},
          layers: [],
        },
      }),
    ).toThrow(
      expect.objectContaining({ code: "MAP_RUNTIME_INITIALIZATION_FAILED" }),
    );
    expect(renderer.instances).toHaveLength(0);
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
  });

  it("maps renderer initialization errors to one KFM-owned failure", async () => {
    const runtime = createMapLibreAdapter({ containerId: "kfm-map-root" });
    const pending = runtime.initialize();
    const map = renderer.instances[0];

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

  it("accepts a bounded inline style without widening the runtime port", async () => {
    const runtime = createMapLibreAdapter({
      containerId: "safe-map",
      style: {
        version: 8,
        sources: {
          fixture: {
            type: "geojson",
            data: {
              type: "FeatureCollection",
              features: [],
            },
          },
        },
        layers: [
          {
            id: "background",
            type: "background",
            paint: { "background-color": "#071517" },
          },
        ],
      },
    });

    const pending = runtime.initialize();
    expect(renderer.instances[0]?.options.style).toMatchObject({
      version: 8,
      sources: { fixture: { type: "geojson" } },
      layers: [{ id: "background", type: "background" }],
    });
    renderer.instances[0]?.emit("load");
    await expect(pending).resolves.toMatchObject({ state: "READY" });
    expect(Object.keys(runtime.getSnapshot()).sort()).toEqual([
      "camera",
      "profile",
      "reason",
      "selection",
      "state",
    ]);
  });

  it("rejects an in-flight initialization when disposed", async () => {
    const runtime = createMapLibreAdapter({ containerId: "kfm-map-root" });
    const pending = runtime.initialize();
    const map = renderer.instances[0];

    runtime.dispose();

    await expect(pending).rejects.toMatchObject({ code: "MAP_RUNTIME_DISPOSED" });
    expect(map.removed).toBe(true);
    expect(runtime.getSnapshot().state).toBe("DISPOSED");
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

  it("fails finitely when an initializing snapshot listener throws", async () => {
    const runtime = createMapLibreAdapter({ containerId: "kfm-map-root" });
    const unsubscribe = runtime.subscribeSnapshot((snapshot) => {
      if (snapshot.state === "INITIALIZING" || snapshot.state === "ERROR") {
        throw new Error("synthetic listener failure");
      }
    });

    await expect(runtime.initialize()).rejects.toMatchObject({
      code: "MAP_RUNTIME_INITIALIZATION_FAILED",
    });
    expect(renderer.instances).toHaveLength(0);
    expect(runtime.getSnapshot()).toMatchObject({
      state: "ERROR",
      reason: "MAP_RUNTIME_ERROR",
    });

    unsubscribe();
    const retry = runtime.initialize();
    renderer.instances[0].emit("load");
    await expect(retry).resolves.toMatchObject({ state: "READY", reason: null });
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

  it("keeps selection disabled unless explicit fixture bindings are supplied", async () => {
    const runtime = createMapLibreAdapter({ containerId: "fixture-map", style: fixtureStyle() });
    const consume = vi.fn();
    runtime.subscribeSelection(consume);
    const pending = runtime.initialize();
    const map = renderer.instances[0];
    map.renderedFeatures = [renderedFixture()];
    map.emit("load");
    await pending;
    map.emit("click");
    expect(map.queryCalls).toBe(0);
    expect(consume).not.toHaveBeenCalled();
    expect(runtime.getSnapshot().selection).toBeNull();
    runtime.dispose();
  });

  it("emits copied fixture identity without trusting renderer properties or replacing the map", async () => {
    const requested = fixtureSelection();
    const expected = structuredClone(requested);
    const runtime = createMapLibreAdapter({
      containerId: "fixture-map", style: fixtureStyle(), fixtureSelections: [requested],
    });
    requested.evidenceRefs.push("kfm:evidence:synthetic:post-construction-mutation");
    const noNetwork = vi.fn(() => { throw new Error("network forbidden"); });
    vi.stubGlobal("fetch", noNetwork);
    const consume = vi.fn();
    runtime.subscribeSelection(consume);
    const pending = runtime.initialize();
    const map = renderer.instances[0];
    map.renderedFeatures = [renderedFixture(), renderedFixture()];
    map.emit("click");
    expect(map.queryCalls).toBe(0);
    map.emit("load");
    await pending;
    const camera = runtime.getSnapshot().camera;
    map.emit("click");
    expect(consume).toHaveBeenCalledExactlyOnceWith(expected);
    expect(runtime.getSnapshot()).toMatchObject({ state: "READY", selection: expected, camera });
    expect(Object.isFrozen(runtime.getSnapshot().selection?.evidenceRefs)).toBe(true);
    expect(JSON.stringify(runtime.getSnapshot())).not.toContain("UNTRUSTED_RENDERER_PROPERTY");
    expect(renderer.instances).toHaveLength(1);
    expect(map.removed).toBe(false);
    expect(map.jumpToCalls).toEqual([]);
    expect(noNetwork).not.toHaveBeenCalled();
    runtime.dispose();
  });

  it("projects shared-source string IDs once while preserving caller geometry and original selections", async () => {
    const style = fixtureStyle();
    const original = structuredClone(style);
    const first = fixtureSelection();
    const second = { ...fixtureSelection("feature:fixture:kansas-002"), layerId: "layer:fixture:second" };
    style.layers.push({ ...style.layers[0], id: second.layerId });
    original.layers.push({ ...original.layers[0], id: second.layerId });
    const runtime = createMapLibreAdapter({ containerId: "fixture-map", style, fixtureSelections: [first, second] });
    const consume = vi.fn();
    runtime.subscribeSelection(consume);
    const pending = runtime.initialize();
    const map = renderer.instances[0];
    const projected = map.options.style as ReturnType<typeof fixtureStyle>;
    expect(style).toEqual(original);
    expect(projected.sources["source:fixture:kansas"].data.features.map((feature) => feature.id)).toEqual([0, 1]);
    expect(projected.sources["source:fixture:kansas"].data.features.map((feature) => feature.geometry))
      .toEqual(original.sources["source:fixture:kansas"].data.features.map((feature) => feature.geometry));
    map.emit("load");
    await pending;
    map.renderedFeatures = [renderedFixture(0)];
    map.emit("click");
    map.renderedFeatures = [{ ...renderedFixture(1), layer: { id: second.layerId } }];
    map.emit("click");
    expect(consume.mock.calls).toEqual([[first], [second]]);
    runtime.dispose();
  });

  it("cannot alias an unbound numeric-ID feature to a reviewed string-ID feature", async () => {
    const style = fixtureStyle();
    Object.assign(style.sources["source:fixture:kansas"].data.features[1], {
      id: 0, properties: { fixture: false, id: fixtureSelection().featureId },
    });
    const runtime = createMapLibreAdapter({ containerId: "fixture-map", style, fixtureSelections: [fixtureSelection()] });
    const consume = vi.fn();
    runtime.subscribeSelection(consume);
    const pending = runtime.initialize();
    const map = renderer.instances[0];
    map.emit("load");
    await pending;
    // The unbound feature is rendered as index 1 even though its authored ID
    // was the bound feature's projected address 0.
    map.renderedFeatures = [renderedFixture(1)];
    map.emit("click");
    map.renderedFeatures = [{ ...renderedFixture(), id: "0" }];
    map.emit("click");
    expect(consume).not.toHaveBeenCalled();
    map.renderedFeatures = [renderedFixture(0)];
    map.emit("click");
    expect(consume).toHaveBeenCalledExactlyOnceWith(fixtureSelection());
    runtime.dispose();
  });

  it("maps a single GeoJSON Feature without altering the authored ID", async () => {
    const style = fixtureStyle();
    const feature = style.sources["source:fixture:kansas"].data.features[0];
    const singleFeatureStyle = {
      ...style,
      sources: { "source:fixture:kansas": { type: "geojson" as const, data: feature } },
    };
    const runtime = createMapLibreAdapter({ containerId: "fixture-map", style: singleFeatureStyle, fixtureSelections: [fixtureSelection()] });
    const consume = vi.fn();
    runtime.subscribeSelection(consume);
    const pending = runtime.initialize();
    const map = renderer.instances[0];
    map.emit("load");
    await pending;
    map.renderedFeatures = [renderedFixture(0)];
    map.emit("click");
    expect(feature.id).toBe(fixtureSelection().featureId);
    expect(consume).toHaveBeenCalledExactlyOnceWith(fixtureSelection());
    runtime.dispose();
  });

  it.each(["filter-expression", "legacy-filter", "paint-expression", "sibling-layer", "source-filter"])(
    "rejects ID-dependent %s before renderer acquisition", (kind) => {
      const style = fixtureStyle();
      const filter = ["==", ["id"], fixtureSelection().featureId];
      if (kind === "filter-expression") Object.assign(style.layers[0], { filter });
      if (kind === "legacy-filter") Object.assign(style.layers[0], { filter: ["==", "$id", fixtureSelection().featureId] });
      if (kind === "paint-expression") Object.assign(style.layers[0], { paint: { "circle-radius": ["case", filter, 10, 2] } });
      if (kind === "sibling-layer") style.layers.push({ ...style.layers[0], id: "unbound-sibling", ...{ filter } });
      if (kind === "source-filter") Object.assign(style.sources["source:fixture:kansas"], { filter });
      expect(() => createMapLibreAdapter({ containerId: "fixture-map", style, fixtureSelections: [fixtureSelection()] }))
        .toThrow(expect.objectContaining({ code: "MAP_RUNTIME_SELECTION_INVALID" }));
      expect(renderer.instances).toHaveLength(0);
    },
  );

  it.each(["unknown-id", "unknown-layer", "unknown-source", "ambiguous", "empty", "excessive"])(
    "does not emit selection for %s hits", async (kind) => {
      const runtime = createMapLibreAdapter({
        containerId: "fixture-map", style: fixtureStyle(),
        fixtureSelections: [fixtureSelection(), fixtureSelection("feature:fixture:kansas-002")],
      });
      const consume = vi.fn();
      runtime.subscribeSelection(consume);
      const pending = runtime.initialize();
      const map = renderer.instances[0];
      map.emit("load");
      await pending;
      map.renderedFeatures = kind === "empty" ? [] : kind === "excessive"
        ? Array.from({ length: 129 }, () => renderedFixture()) : kind === "ambiguous"
        ? [renderedFixture(), renderedFixture(1)]
        : [{ ...renderedFixture(), ...(kind === "unknown-id" ? { id: "feature:unknown" }
          : kind === "unknown-layer" ? { layer: { id: "layer:unknown" } }
            : { source: "source:unknown" }) }];
      map.emit("click");
      expect(consume).not.toHaveBeenCalled();
      expect(runtime.getSnapshot()).toMatchObject({ state: "READY", selection: null });
      expect(map.removed).toBe(false);
      runtime.dispose();
    },
  );

  it.each(["unsafe-reference", "duplicate-binding", "duplicate-selection-id", "duplicate-feature-id", "missing-layer", "missing-feature", "not-synthetic", "too-many"])(
    "rejects %s bindings before renderer acquisition", (kind) => {
      const style = fixtureStyle();
      const selections = [fixtureSelection()];
      if (kind === "unsafe-reference") selections[0].evidenceRefs = [" unsafe "];
      if (kind === "duplicate-binding") selections.push(fixtureSelection());
      if (kind === "duplicate-selection-id") selections.push({ ...fixtureSelection("feature:fixture:kansas-002"), selectionId: selections[0].selectionId });
      if (kind === "duplicate-feature-id") style.sources["source:fixture:kansas"].data.features.push(structuredClone(style.sources["source:fixture:kansas"].data.features[0]));
      if (kind === "missing-layer") selections[0].layerId = "layer:missing";
      if (kind === "missing-feature") selections[0].featureId = "feature:missing";
      if (kind === "not-synthetic") style.sources["source:fixture:kansas"].data.features[0].properties.fixture = false;
      if (kind === "too-many") selections.push(...Array.from({ length: 64 }, () => fixtureSelection()));
      expect(() => createMapLibreAdapter({ containerId: "fixture-map", style, fixtureSelections: selections }))
        .toThrow(expect.objectContaining({ code: "MAP_RUNTIME_SELECTION_INVALID" }));
      expect(renderer.instances).toHaveLength(0);
    },
  );

  it.each([
    { promoteId: "alias" },
    { promoteId: { "source:fixture:kansas": "alias" } },
    { generateId: true },
    { cluster: true },
  ])("rejects renderer identity transforms before acquisition (%j)", (transform) => {
    const style = fixtureStyle();
    Object.assign(style.sources["source:fixture:kansas"], transform);
    // With promoteId, this different non-fixture feature could otherwise
    // acquire the reviewed feature's ID from its arbitrary alias property.
    Object.assign(style.sources["source:fixture:kansas"].data.features[1].properties, {
      fixture: false, alias: fixtureSelection().featureId,
    });
    expect(() => createMapLibreAdapter({ containerId: "fixture-map", style, fixtureSelections: [fixtureSelection()] }))
      .toThrow(expect.objectContaining({ code: "MAP_RUNTIME_SELECTION_INVALID" }));
    expect(renderer.instances).toHaveLength(0);
  });

  it("removes click handlers on disposal and honors selection unsubscribe", async () => {
    const runtime = createMapLibreAdapter({ containerId: "fixture-map", style: fixtureStyle(), fixtureSelections: [fixtureSelection()] });
    const consume = vi.fn();
    const unsubscribe = runtime.subscribeSelection(consume);
    const pending = runtime.initialize();
    const map = renderer.instances[0];
    map.renderedFeatures = [renderedFixture()];
    map.emit("load");
    await pending;
    unsubscribe();
    unsubscribe();
    map.emit("click");
    expect(consume).not.toHaveBeenCalled();
    expect(map.queryCalls).toBe(1);
    runtime.dispose();
    runtime.dispose();
    map.emit("click");
    expect(map.queryCalls).toBe(1);
    expect(runtime.getSnapshot()).toMatchObject({ state: "DISPOSED", selection: null });
  });

  it("stops further delivery when a selection listener disposes synchronously", async () => {
    const runtime = createMapLibreAdapter({ containerId: "fixture-map", style: fixtureStyle(), fixtureSelections: [fixtureSelection()] });
    const later = vi.fn();
    runtime.subscribeSelection(() => runtime.dispose());
    runtime.subscribeSelection(later);
    const pending = runtime.initialize();
    const map = renderer.instances[0];
    map.renderedFeatures = [renderedFixture()];
    map.emit("load");
    await pending;
    map.emit("click");
    expect(later).not.toHaveBeenCalled();
    expect(runtime.getSnapshot()).toMatchObject({ state: "DISPOSED", selection: null });
  });

  it("does not deliver selection after a snapshot listener disposes synchronously", async () => {
    const runtime = createMapLibreAdapter({ containerId: "fixture-map", style: fixtureStyle(), fixtureSelections: [fixtureSelection()] });
    runtime.subscribeSnapshot((snapshot) => { if (snapshot.selection !== null) runtime.dispose(); });
    const consume = vi.fn();
    runtime.subscribeSelection(consume);
    const pending = runtime.initialize();
    const map = renderer.instances[0];
    map.renderedFeatures = [renderedFixture()];
    map.emit("load");
    await pending;
    map.emit("click");
    expect(consume).not.toHaveBeenCalled();
    expect(runtime.getSnapshot()).toMatchObject({ state: "DISPOSED", selection: null });
  });

  it("keeps query failures finite and preserves the mounted renderer", async () => {
    const runtime = createMapLibreAdapter({ containerId: "fixture-map", style: fixtureStyle(), fixtureSelections: [fixtureSelection()] });
    const consume = vi.fn();
    runtime.subscribeSelection(consume);
    const pending = runtime.initialize();
    const map = renderer.instances[0];
    map.emit("load");
    await pending;
    map.queryError = true;
    expect(() => map.emit("click")).not.toThrow();
    expect(runtime.getSnapshot()).toMatchObject({ state: "ERROR", reason: "MAP_RUNTIME_ERROR", selection: null });
    expect(consume).not.toHaveBeenCalled();
    expect(map.removed).toBe(false);
    const retry = runtime.initialize();
    expect(map.removed).toBe(true);
    const replacement = renderer.instances[1];
    replacement.renderedFeatures = [renderedFixture()];
    replacement.emit("load");
    await retry;
    map.emit("click");
    expect(map.queryCalls).toBe(1);
    replacement.emit("click");
    expect(consume).toHaveBeenCalledExactlyOnceWith(fixtureSelection());
    runtime.dispose();
  });
});
