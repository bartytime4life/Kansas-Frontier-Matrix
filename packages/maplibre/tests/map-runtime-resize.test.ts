import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

type RendererHandler = () => void;

type RendererInstance = {
  removed: boolean;
  resizeCalls: number;
  emit: (type: string) => void;
};

const renderer = vi.hoisted(() => ({
  instances: [] as RendererInstance[],
  throwOnResize: false,
  emitErrorOnResize: false,
}));

vi.mock("maplibre-gl", () => ({
  Map: class FakeMap {
    removed = false;
    resizeCalls = 0;
    private readonly handlers = new globalThis.Map<string, Set<RendererHandler>>();
    private camera = {
      longitude: -98.4842,
      latitude: 38.4988,
      zoom: 6,
      bearing: 0,
      pitch: 0,
    };

    constructor(options: Record<string, unknown>) {
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
      const handlers = this.handlers.get(type) ?? new Set<RendererHandler>();
      handlers.add(handler);
      this.handlers.set(type, handlers);
      return { unsubscribe: () => handlers.delete(handler) };
    }

    emit(type: string): void {
      for (const handler of [...(this.handlers.get(type) ?? [])]) handler();
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

    jumpTo(): this {
      return this;
    }

    resize(): this {
      this.resizeCalls += 1;
      if (renderer.throwOnResize) throw new Error("synthetic renderer resize failure");
      if (renderer.emitErrorOnResize) this.emit("error");
      return this;
    }

    remove(): void {
      this.removed = true;
    }
  },
}));

import { createMapLibreAdapter } from "../src/maplibre-adapter";
import { createNullMapRuntime } from "../src/null-map-runtime";

describe("MapRuntimePort responsive resize boundary", () => {
  beforeEach(() => {
    renderer.instances.length = 0;
    renderer.throwOnResize = false;
    renderer.emitErrorOnResize = false;
    vi.stubGlobal("document", {
      createElement: () => ({
        getContext: (type: string) =>
          type === "webgl2" ? { getExtension: () => null } : null,
      }),
    });
  });

  afterEach(() => vi.unstubAllGlobals());

  it("resizes a ready MapLibre runtime without changing governed camera state", async () => {
    const runtime = createMapLibreAdapter({ containerId: "kfm-map-root" });

    expect(() => runtime.resize()).toThrow(
      expect.objectContaining({ code: "MAP_RUNTIME_NOT_READY" }),
    );

    const pending = runtime.initialize();
    const map = renderer.instances[0];
    map.emit("load");
    const ready = await pending;

    expect(runtime.resize()).toEqual(ready);
    expect(map.resizeCalls).toBe(1);
    expect(runtime.getSnapshot()).toEqual(ready);

    runtime.dispose();
    expect(() => runtime.resize()).toThrow(
      expect.objectContaining({ code: "MAP_RUNTIME_DISPOSED" }),
    );
  });

  it("maps a renderer resize exception to a finite KFM failure and tears down", async () => {
    const runtime = createMapLibreAdapter({ containerId: "kfm-map-root" });
    const pending = runtime.initialize();
    const map = renderer.instances[0];
    map.emit("load");
    await pending;

    renderer.throwOnResize = true;
    expect(() => runtime.resize()).toThrow(
      expect.objectContaining({
        name: "MapRuntimePortError",
        code: "MAP_RUNTIME_RESIZE_FAILED",
      }),
    );

    expect(map.removed).toBe(true);
    expect(runtime.getSnapshot()).toMatchObject({
      state: "ERROR",
      reason: "MAP_RUNTIME_ERROR",
      selection: null,
    });
  });

  it("converts a synchronous renderer error during resize to the same finite boundary", async () => {
    const runtime = createMapLibreAdapter({ containerId: "kfm-map-root" });
    const pending = runtime.initialize();
    const map = renderer.instances[0];
    map.emit("load");
    await pending;

    renderer.emitErrorOnResize = true;
    expect(() => runtime.resize()).toThrow(
      expect.objectContaining({ code: "MAP_RUNTIME_RESIZE_FAILED" }),
    );
    expect(map.removed).toBe(true);
    expect(runtime.getSnapshot()).toMatchObject({
      state: "ERROR",
      reason: "MAP_RUNTIME_ERROR",
    });
  });

  it("keeps the dependency-free Null runtime behaviorally compatible", async () => {
    const runtime = createNullMapRuntime();

    expect(() => runtime.resize()).toThrow(
      expect.objectContaining({ code: "MAP_RUNTIME_NOT_READY" }),
    );

    const ready = await runtime.initialize();
    expect(runtime.resize()).toEqual(ready);
    expect(runtime.getSnapshot()).toEqual(ready);

    runtime.dispose();
    expect(() => runtime.resize()).toThrow(
      expect.objectContaining({ code: "MAP_RUNTIME_DISPOSED" }),
    );
  });
});
