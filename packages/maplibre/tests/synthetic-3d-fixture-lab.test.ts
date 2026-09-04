import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

type Handler = (event?: unknown) => void;

type FakeMapInstance = {
  options: Record<string, unknown>;
  removed: boolean;
  resizeCalls: number;
  projectionCalls: unknown[];
  skyCalls: unknown[];
  lightCalls: unknown[];
  fieldOfViewCalls: number[];
  paintCalls: unknown[][];
  featureStateCalls: unknown[][];
  jumpToCalls: Record<string, unknown>[];
  queryFeatures: Array<{ id?: string | number }>;
  emit: (type: string, event?: unknown) => void;
};

const renderer = vi.hoisted(() => ({
  instances: [] as FakeMapInstance[],
  throwOnConstruct: false,
}));

const capabilities = vi.hoisted(() => ({
  webgl2: true,
  containerPresent: true,
}));

vi.mock("maplibre-gl", () => ({
  setWorkerUrl: vi.fn(),
  Map: class FakeMap {
    readonly options: Record<string, unknown>;
    readonly projectionCalls: unknown[] = [];
    readonly skyCalls: unknown[] = [];
    readonly lightCalls: unknown[] = [];
    readonly fieldOfViewCalls: number[] = [];
    readonly paintCalls: unknown[][] = [];
    readonly featureStateCalls: unknown[][] = [];
    readonly jumpToCalls: Record<string, unknown>[] = [];
    queryFeatures: Array<{ id?: string | number }> = [];
    removed = false;
    resizeCalls = 0;

    private readonly handlers = new globalThis.Map<string, Set<Handler>>();
    private camera = {
      longitude: -98.45,
      latitude: 38.45,
      zoom: 5.2,
      bearing: -18,
      pitch: 54,
    };

    constructor(options: Record<string, unknown>) {
      if (renderer.throwOnConstruct) {
        throw new Error("synthetic constructor failure");
      }
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

    on(type: string, handler: Handler): { unsubscribe: () => void } {
      const handlers = this.handlers.get(type) ?? new Set<Handler>();
      handlers.add(handler);
      this.handlers.set(type, handlers);
      return { unsubscribe: () => handlers.delete(handler) };
    }

    emit(type: string, event: unknown = { point: { x: 1, y: 1 } }): void {
      for (const handler of [...(this.handlers.get(type) ?? [])]) {
        handler(event);
      }
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

    setProjection(value: unknown): this {
      this.projectionCalls.push(value);
      return this;
    }

    setSky(value: unknown): this {
      this.skyCalls.push(value);
      return this;
    }

    setLight(value: unknown): this {
      this.lightCalls.push(value);
      return this;
    }

    setVerticalFieldOfView(value: number): this {
      this.fieldOfViewCalls.push(value);
      return this;
    }

    setPaintProperty(...values: unknown[]): this {
      this.paintCalls.push(values);
      return this;
    }

    setFeatureState(...values: unknown[]): this {
      this.featureStateCalls.push(values);
      return this;
    }

    queryRenderedFeatures(): Array<{ id?: string | number }> {
      return this.queryFeatures;
    }

    jumpTo(options: Record<string, unknown>): this {
      this.jumpToCalls.push(options);
      const center = options.center as [number, number] | undefined;
      if (center) {
        this.camera.longitude = center[0];
        this.camera.latitude = center[1];
      }
      if (typeof options.zoom === "number") this.camera.zoom = options.zoom;
      if (typeof options.bearing === "number") {
        this.camera.bearing = options.bearing;
      }
      if (typeof options.pitch === "number") this.camera.pitch = options.pitch;
      return this;
    }

    resize(): this {
      this.resizeCalls += 1;
      return this;
    }

    remove(): void {
      this.removed = true;
    }
  },
}));

import {
  SYNTHETIC_3D_EXTRUSION_LAYER_ID,
  SYNTHETIC_3D_FIXTURE_FEATURES,
  SYNTHETIC_3D_FIXTURE_SOURCE_ID,
  Synthetic3dFixtureLabError,
  createSynthetic3dFixtureLab,
} from "../src/synthetic-3d-fixture-lab";

describe("synthetic MapLibre 3D fixture lab", () => {
  beforeEach(() => {
    renderer.instances.length = 0;
    renderer.throwOnConstruct = false;
    capabilities.webgl2 = true;
    capabilities.containerPresent = true;

    vi.stubGlobal("document", {
      getElementById: () =>
        capabilities.containerPresent ? { id: "kfm-synthetic-map" } : null,
      createElement: () => ({
        getContext: (type: string) =>
          type === "webgl2" && capabilities.webgl2
            ? {
                getExtension: () => ({
                  loseContext: vi.fn(),
                }),
              }
            : null,
      }),
    });
  });

  afterEach(() => {
    vi.useRealTimers();
    vi.unstubAllGlobals();
  });

  it("constructs an inline-only globe scene with no external source surface", async () => {
    const status = vi.fn();
    const pending = createSynthetic3dFixtureLab({
      containerId: "kfm-synthetic-map",
      onStatus: status,
    });
    const map = renderer.instances[0];

    const style = map.options.style as {
      glyphs?: unknown;
      sprite?: unknown;
      terrain?: unknown;
      sources: Record<string, Record<string, unknown>>;
      layers: Array<Record<string, unknown>>;
    };

    expect(map.options).toMatchObject({
      container: "kfm-synthetic-map",
      interactive: true,
      hash: false,
      attributionControl: false,
      maplibreLogo: false,
      cooperativeGestures: true,
      renderWorldCopies: false,
    });
    expect(style.glyphs).toBeUndefined();
    expect(style.sprite).toBeUndefined();
    expect(style.terrain).toBeUndefined();
    expect(Object.keys(style.sources)).toEqual([
      SYNTHETIC_3D_FIXTURE_SOURCE_ID,
    ]);
    expect(style.sources[SYNTHETIC_3D_FIXTURE_SOURCE_ID]).toMatchObject({
      type: "geojson",
      lineMetrics: true,
    });
    expect(
      Object.values(style.sources).some(
        (source) => "url" in source || "tiles" in source,
      ),
    ).toBe(false);
    expect(style.layers.some((layer) => layer.type === "fill-extrusion")).toBe(
      true,
    );
    expect(
      style.layers.some(
        (layer) =>
          layer.id === SYNTHETIC_3D_EXTRUSION_LAYER_ID &&
          layer.source === SYNTHETIC_3D_FIXTURE_SOURCE_ID,
      ),
    ).toBe(true);

    map.emit("load");
    const controller = await pending;

    expect(controller.getSnapshot()).toMatchObject({
      status: "READY",
      projection: "globe",
      skyPreset: "night",
      verticalScale: 1,
      fieldOfView: 36,
      lightAzimuth: 210,
      selectedFeatureId: null,
    });
    expect(map.projectionCalls.at(-1)).toEqual({ type: "globe" });
    expect(map.skyCalls).toHaveLength(1);
    expect(map.lightCalls).toHaveLength(1);
    expect(map.fieldOfViewCalls).toEqual([36]);
    expect(map.paintCalls.at(-1)).toEqual([
      SYNTHETIC_3D_EXTRUSION_LAYER_ID,
      "fill-extrusion-height",
      ["*", ["get", "height"], 1],
    ]);
    expect(status).toHaveBeenCalledWith(
      expect.objectContaining({ status: "READY" }),
    );
  });

  it("applies projection, camera, atmosphere, light, extrusion, and feature-state controls", async () => {
    const selection = vi.fn();
    const pending = createSynthetic3dFixtureLab({
      containerId: "kfm-synthetic-map",
      onSelection: selection,
    });
    const map = renderer.instances[0];
    map.emit("load");
    const controller = await pending;

    expect(controller.setProjection("mercator").projection).toBe("mercator");
    expect(controller.setSkyPreset("dusk").skyPreset).toBe("dusk");
    expect(controller.setVerticalScale(1.75).verticalScale).toBe(1.75);
    expect(controller.setFieldOfView(48).fieldOfView).toBe(48);
    expect(controller.setLightAzimuth(125).lightAzimuth).toBe(125);
    expect(controller.setPitch(65).camera.pitch).toBe(65);
    expect(controller.setBearing(205).camera.bearing).toBe(-155);
    expect(controller.setZoom(6.5).camera.zoom).toBe(6.5);

    const feature = SYNTHETIC_3D_FIXTURE_FEATURES[0];
    const selected = controller.selectFeature(feature.id);
    expect(selected.selectedFeatureId).toBe(feature.id);
    expect(map.featureStateCalls.at(-1)).toEqual([
      { source: SYNTHETIC_3D_FIXTURE_SOURCE_ID, id: feature.id },
      { selected: true },
    ]);
    expect(selection).toHaveBeenCalledWith(
      expect.objectContaining({
        feature,
        selection: expect.objectContaining({
          profile: "kfm.explorer.map-feature-selection.v1",
          selectionId: `selection:${feature.id}`,
          featureId: feature.id,
          evidenceRefs: feature.evidenceRefs,
          historyEvidenceRefs: feature.historyEvidenceRefs,
        }),
      }),
    );

    const second = SYNTHETIC_3D_FIXTURE_FEATURES[1];
    map.queryFeatures = [{ id: second.id }];
    map.emit("click", { point: { x: 20, y: 25 } });
    expect(controller.getSnapshot().selectedFeatureId).toBe(second.id);
    expect(map.featureStateCalls.slice(-2)).toEqual([
      [
        { source: SYNTHETIC_3D_FIXTURE_SOURCE_ID, id: feature.id },
        { selected: false },
      ],
      [
        { source: SYNTHETIC_3D_FIXTURE_SOURCE_ID, id: second.id },
        { selected: true },
      ],
    ]);

    expect(controller.clearSelection().selectedFeatureId).toBeNull();
    expect(controller.resize().status).toBe("READY");
    expect(map.resizeCalls).toBe(1);
    expect(controller.reset()).toMatchObject({
      projection: "globe",
      skyPreset: "night",
      verticalScale: 1,
      fieldOfView: 36,
      lightAzimuth: 210,
      selectedFeatureId: null,
    });
  });

  it("fails before renderer construction when the container or WebGL2 is unavailable", async () => {
    capabilities.containerPresent = false;
    await expect(
      createSynthetic3dFixtureLab({
        containerId: "kfm-synthetic-map",
      }),
    ).rejects.toMatchObject({
      code: "SYNTHETIC_3D_CONTAINER_INVALID",
    });
    expect(renderer.instances).toHaveLength(0);

    capabilities.containerPresent = true;
    capabilities.webgl2 = false;
    await expect(
      createSynthetic3dFixtureLab({
        containerId: "kfm-synthetic-map",
      }),
    ).rejects.toMatchObject({
      code: "SYNTHETIC_3D_WEBGL2_UNAVAILABLE",
    });
    expect(renderer.instances).toHaveLength(0);
  });

  it("rejects invalid scene values and unknown feature identifiers", async () => {
    await expect(
      createSynthetic3dFixtureLab({
        containerId: " unsafe container ",
      }),
    ).rejects.toBeInstanceOf(Synthetic3dFixtureLabError);
    await expect(
      createSynthetic3dFixtureLab({
        containerId: "kfm-synthetic-map",
        initialVerticalScale: 8,
      }),
    ).rejects.toMatchObject({
      code: "SYNTHETIC_3D_VALUE_INVALID",
    });

    const pending = createSynthetic3dFixtureLab({
      containerId: "kfm-synthetic-map",
    });
    renderer.instances[0].emit("load");
    const controller = await pending;
    expect(() => controller.selectFeature("synthetic:missing")).toThrow(
      expect.objectContaining({ code: "SYNTHETIC_3D_FEATURE_INVALID" }),
    );
    expect(() => controller.setFieldOfView(90)).toThrow(
      expect.objectContaining({ code: "SYNTHETIC_3D_VALUE_INVALID" }),
    );
  });

  it("maps initialization errors to a finite failure and removes the renderer", async () => {
    const pending = createSynthetic3dFixtureLab({
      containerId: "kfm-synthetic-map",
    });
    const map = renderer.instances[0];

    map.emit("error");

    await expect(pending).rejects.toMatchObject({
      code: "SYNTHETIC_3D_INITIALIZATION_FAILED",
    });
    expect(map.removed).toBe(true);
  });

  it("tears down idempotently and refuses later mutation", async () => {
    const status = vi.fn();
    const pending = createSynthetic3dFixtureLab({
      containerId: "kfm-synthetic-map",
      onStatus: status,
    });
    const map = renderer.instances[0];
    map.emit("load");
    const controller = await pending;

    controller.destroy();
    controller.destroy();

    expect(map.removed).toBe(true);
    expect(controller.getSnapshot()).toMatchObject({
      status: "DISPOSED",
      selectedFeatureId: null,
      reason: "SYNTHETIC_3D_DISPOSED",
    });
    expect(() => controller.setProjection("globe")).toThrow(
      expect.objectContaining({ code: "SYNTHETIC_3D_DISPOSED" }),
    );
    expect(status).toHaveBeenCalledWith(
      expect.objectContaining({ status: "DISPOSED" }),
    );
  });
});
