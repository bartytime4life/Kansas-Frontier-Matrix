import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

type RendererHandler = (event?: {
  features?: Array<{ id?: string | number }>;
}) => void;

type RendererInstance = {
  options: Record<string, unknown>;
  removed: boolean;
  projectionCalls: string[];
  featureStateCalls: Array<{
    feature: Record<string, unknown>;
    state: Record<string, unknown>;
  }>;
  jumpToCalls: Record<string, unknown>[];
  verticalFieldOfViewCalls: number[];
  emit: (
    type: string,
    event?: { features?: Array<{ id?: string | number }> },
  ) => void;
  emitLayer: (
    type: string,
    layerId: string,
    event?: { features?: Array<{ id?: string | number }> },
  ) => void;
};

const renderer = vi.hoisted(() => ({
  instances: [] as RendererInstance[],
}));

const capabilities = vi.hoisted(() => ({ webgl2: true }));

vi.mock("maplibre-gl", () => ({
  Map: class FakeMap {
    readonly options: Record<string, unknown>;
    readonly projectionCalls: string[] = [];
    readonly featureStateCalls: Array<{
      feature: Record<string, unknown>;
      state: Record<string, unknown>;
    }> = [];
    readonly jumpToCalls: Record<string, unknown>[] = [];
    readonly verticalFieldOfViewCalls: number[] = [];
    removed = false;
    private readonly handlers = new globalThis.Map<
      string,
      Set<RendererHandler>
    >();
    private projection = "mercator";
    private pitch: number;
    private bearing: number;
    private verticalFieldOfView = 36.87;

    constructor(options: Record<string, unknown>) {
      this.options = options;
      this.pitch = options.pitch as number;
      this.bearing = options.bearing as number;
      renderer.instances.push(this);
    }

    on(
      type: string,
      layerOrHandler: string | RendererHandler,
      maybeHandler?: RendererHandler,
    ): { unsubscribe: () => void } {
      const layerId =
        typeof layerOrHandler === "string" ? layerOrHandler : null;
      const handler =
        typeof layerOrHandler === "function"
          ? layerOrHandler
          : maybeHandler;
      if (handler === undefined) throw new Error("handler missing");
      const key = layerId === null ? type : `${type}:${layerId}`;
      const listeners = this.handlers.get(key) ?? new Set<RendererHandler>();
      listeners.add(handler);
      this.handlers.set(key, listeners);
      return { unsubscribe: () => listeners.delete(handler) };
    }

    emit(
      type: string,
      event: { features?: Array<{ id?: string | number }> } = {},
    ): void {
      for (const handler of [...(this.handlers.get(type) ?? [])]) {
        handler(event);
      }
    }

    emitLayer(
      type: string,
      layerId: string,
      event: { features?: Array<{ id?: string | number }> } = {},
    ): void {
      for (const handler of [
        ...(this.handlers.get(`${type}:${layerId}`) ?? []),
      ]) {
        handler(event);
      }
    }

    setVerticalFieldOfView(value: number): this {
      this.verticalFieldOfView = value;
      this.verticalFieldOfViewCalls.push(value);
      return this;
    }

    getVerticalFieldOfView(): number {
      return this.verticalFieldOfView;
    }

    getCanvas(): { setAttribute: (name: string, value: string) => void } {
      return { setAttribute: vi.fn() };
    }

    setProjection(projection: { type: string }): this {
      this.projection = projection.type;
      this.projectionCalls.push(projection.type);
      return this;
    }

    getProjection(): { type: string } {
      return { type: this.projection };
    }

    jumpTo(options: Record<string, unknown>): this {
      this.jumpToCalls.push(options);
      if (typeof options.pitch === "number") this.pitch = options.pitch;
      if (typeof options.bearing === "number") this.bearing = options.bearing;
      return this;
    }

    getPitch(): number {
      return this.pitch;
    }

    getBearing(): number {
      return this.bearing;
    }

    setFeatureState(
      feature: Record<string, unknown>,
      state: Record<string, unknown>,
    ): this {
      this.featureStateCalls.push({ feature, state });
      return this;
    }

    remove(): void {
      this.removed = true;
    }
  },
}));

import {
  SYNTHETIC_3D_FIXTURE_EXTRUSION_LAYER_ID,
  SYNTHETIC_3D_FIXTURE_FEATURES,
  SYNTHETIC_3D_FIXTURE_SOURCE_ID,
  createSynthetic3DFixtureLab,
  createSynthetic3DFixtureStyle,
} from "../src/synthetic-3d-fixture-lab";

describe("synthetic MapLibre 3D fixture lab", () => {
  beforeEach(() => {
    renderer.instances.length = 0;
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
    vi.unstubAllGlobals();
    vi.useRealTimers();
  });

  it("builds an inline-only style with a fill extrusion and no external source surface", () => {
    const style = createSynthetic3DFixtureStyle();
    const serialized = JSON.stringify(style);

    expect(style.sources[SYNTHETIC_3D_FIXTURE_SOURCE_ID]).toMatchObject({
      type: "geojson",
      data: { type: "FeatureCollection" },
    });
    expect(style.layers).toEqual(
      expect.arrayContaining([
        expect.objectContaining({
          id: SYNTHETIC_3D_FIXTURE_EXTRUSION_LAYER_ID,
          type: "fill-extrusion",
          source: SYNTHETIC_3D_FIXTURE_SOURCE_ID,
        }),
      ]),
    );
    expect(serialized).not.toMatch(/https?:\/\//i);
    expect(serialized).not.toMatch(/"tiles"\s*:/i);
    expect(serialized).not.toMatch(/"(?:glyphs|sprite)"\s*:/i);
    expect(serialized).not.toMatch(
      /(?:pmtiles|raster-dem|terrain|hillshade|lidar|3d tiles)/i,
    );
  });

  it("initializes, switches projection, updates camera, and selects through feature state", async () => {
    const onSelection = vi.fn();
    const lab = createSynthetic3DFixtureLab({
      containerId: "kfm-maplibre-fixture",
      interactive: false,
      onSelection,
    });

    const pending = lab.initialize();
    const map = renderer.instances[0];

    expect(lab.getSnapshot()).toMatchObject({
      state: "INITIALIZING",
      projection: "mercator",
      selection: null,
    });
    expect(map.options).toMatchObject({
      container: "kfm-maplibre-fixture",
      interactive: false,
      hash: false,
      attributionControl: false,
      maplibreLogo: false,
      renderWorldCopies: false,
    });
    expect(() =>
      (
        map.options.transformRequest as (url: string) => never
      )("https://example.invalid/forbidden"),
    ).toThrow(
      expect.objectContaining({ code: "NETWORK_REQUEST_BLOCKED" }),
    );

    map.emit("load");
    await expect(pending).resolves.toMatchObject({
      state: "READY",
      projection: "mercator",
    });

    expect(lab.setProjection("globe")).toMatchObject({
      state: "READY",
      projection: "globe",
    });
    expect(map.projectionCalls).toEqual(["globe"]);

    expect(
      lab.setCamera({
        pitch: 40,
        bearing: 25,
        verticalFieldOfView: 45,
      }),
    ).toMatchObject({
      camera: {
        pitch: 40,
        bearing: 25,
        verticalFieldOfView: 45,
      },
    });
    expect(map.jumpToCalls.at(-1)).toEqual({ pitch: 40, bearing: 25 });
    expect(map.verticalFieldOfViewCalls.at(-1)).toBe(45);

    const selected = SYNTHETIC_3D_FIXTURE_FEATURES[1]!;
    expect(lab.selectFeature(selected.featureId)).toMatchObject({
      selection: {
        featureId: selected.featureId,
        evidenceRef: selected.evidenceRef,
      },
    });
    expect(map.featureStateCalls.at(-1)).toEqual({
      feature: {
        source: SYNTHETIC_3D_FIXTURE_SOURCE_ID,
        id: selected.featureId,
      },
      state: { selected: true },
    });
    expect(onSelection).toHaveBeenCalledWith(
      expect.objectContaining({
        featureId: selected.featureId,
        evidenceRef: selected.evidenceRef,
      }),
    );

    const pointerSelected = SYNTHETIC_3D_FIXTURE_FEATURES[2]!;
    map.emitLayer("click", SYNTHETIC_3D_FIXTURE_EXTRUSION_LAYER_ID, {
      features: [{ id: pointerSelected.featureId }],
    });
    expect(lab.getSnapshot()).toMatchObject({
      selection: { featureId: pointerSelected.featureId },
    });
    expect(map.featureStateCalls.slice(-2)).toEqual([
      {
        feature: {
          source: SYNTHETIC_3D_FIXTURE_SOURCE_ID,
          id: selected.featureId,
        },
        state: { selected: false },
      },
      {
        feature: {
          source: SYNTHETIC_3D_FIXTURE_SOURCE_ID,
          id: pointerSelected.featureId,
        },
        state: { selected: true },
      },
    ]);

    lab.dispose();
    expect(map.removed).toBe(true);
    expect(lab.getSnapshot()).toMatchObject({
      state: "DISPOSED",
      reason: "DISPOSED",
      selection: null,
    });
  });

  it("fails closed before renderer construction when WebGL2 is unavailable", async () => {
    capabilities.webgl2 = false;
    const lab = createSynthetic3DFixtureLab({
      containerId: "kfm-maplibre-fixture",
    });

    await expect(lab.initialize()).rejects.toMatchObject({
      code: "WEBGL2_UNAVAILABLE",
    });
    expect(renderer.instances).toHaveLength(0);
    expect(lab.getSnapshot()).toMatchObject({
      state: "ERROR",
      reason: "WEBGL2_UNAVAILABLE",
    });
  });

  it("rejects invalid camera values without changing the last valid snapshot", async () => {
    const lab = createSynthetic3DFixtureLab({
      containerId: "kfm-maplibre-fixture",
    });
    const pending = lab.initialize();
    const map = renderer.instances[0];
    map.emit("load");
    await pending;

    const before = lab.getSnapshot();
    expect(() =>
      lab.setCamera({
        pitch: 61,
        bearing: 0,
        verticalFieldOfView: 37,
      }),
    ).toThrow(expect.objectContaining({ code: "RUNTIME_ERROR" }));
    expect(lab.getSnapshot()).toEqual(before);
  });
});
