import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

type RendererHandler = () => void;

type RendererInstance = {
  removed: boolean;
  emit: (type: string) => void;
};

const renderer = vi.hoisted(() => ({
  instances: [] as RendererInstance[],
  throwOnJumpTo: false,
}));

vi.mock("maplibre-gl", () => ({
  Map: class FakeMap {
    removed = false;
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

    jumpTo(options: Record<string, unknown>): this {
      if (renderer.throwOnJumpTo) throw new Error("synthetic renderer navigation failure");
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

    remove(): void {
      this.removed = true;
    }
  },
}));

import { createMapLibreAdapter } from "../src/maplibre-adapter";

describe("MapLibre navigation failure boundary", () => {
  beforeEach(() => {
    renderer.instances.length = 0;
    renderer.throwOnJumpTo = false;
    vi.stubGlobal("document", {
      createElement: () => ({
        getContext: (type: string) =>
          type === "webgl2" ? { getExtension: () => null } : null,
      }),
    });
  });

  afterEach(() => vi.unstubAllGlobals());

  it("maps renderer camera failures to a finite KFM navigation error and tears down", async () => {
    const runtime = createMapLibreAdapter({ containerId: "kfm-map-root" });
    const pending = runtime.initialize();
    const map = renderer.instances[0];
    map.emit("load");
    await expect(pending).resolves.toMatchObject({ state: "READY" });

    const initialCamera = runtime.getSnapshot().camera;
    renderer.throwOnJumpTo = true;

    expect(() =>
      runtime.setCamera({
        longitude: -97,
        latitude: 39,
        zoom: 8,
        bearing: 12,
        pitch: 25,
      }),
    ).toThrow(
      expect.objectContaining({
        name: "MapRuntimePortError",
        code: "MAP_RUNTIME_NAVIGATION_FAILED",
      }),
    );

    expect(map.removed).toBe(true);
    expect(runtime.getSnapshot()).toMatchObject({
      state: "ERROR",
      reason: "MAP_RUNTIME_ERROR",
      selection: null,
      camera: initialCamera,
    });
  });

  it("contains post-ready renderer errors even when an ERROR listener throws", async () => {
    const runtime = createMapLibreAdapter({ containerId: "kfm-map-root" });
    const pending = runtime.initialize();
    const map = renderer.instances[0];
    map.emit("load");
    await expect(pending).resolves.toMatchObject({ state: "READY" });

    runtime.subscribeSnapshot((snapshot) => {
      if (snapshot.state === "ERROR") throw new Error("synthetic consumer listener failure");
    });

    expect(() => map.emit("error")).not.toThrow();
    expect(map.removed).toBe(true);
    expect(runtime.getSnapshot()).toMatchObject({
      state: "ERROR",
      reason: "MAP_RUNTIME_ERROR",
      selection: null,
    });
  });
});
