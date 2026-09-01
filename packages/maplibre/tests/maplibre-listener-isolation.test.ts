import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

type RendererHandler = () => void;

type RendererInstance = {
  removed: boolean;
  emit: (type: string) => void;
};

const renderer = vi.hoisted(() => ({
  instances: [] as RendererInstance[],
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

describe("MapLibre snapshot listener isolation", () => {
  beforeEach(() => {
    renderer.instances.length = 0;
    vi.stubGlobal("document", {
      createElement: () => ({
        getContext: (type: string) =>
          type === "webgl2" ? { getExtension: () => null } : null,
      }),
    });
  });

  afterEach(() => vi.unstubAllGlobals());

  it("keeps initialization finite when one snapshot listener throws", async () => {
    const runtime = createMapLibreAdapter({ containerId: "kfm-map-root" });
    const observedStates: string[] = [];

    runtime.subscribeSnapshot(() => {
      throw new Error("synthetic consumer listener failure");
    });
    runtime.subscribeSnapshot((snapshot) => observedStates.push(snapshot.state));

    const pending = runtime.initialize();
    const map = renderer.instances[0];
    expect(observedStates).toEqual(["INITIALIZING"]);

    expect(() => map.emit("load")).not.toThrow();
    await expect(pending).resolves.toMatchObject({ state: "READY", reason: null });
    expect(observedStates).toEqual(["INITIALIZING", "READY"]);
    expect(map.removed).toBe(false);
  });

  it("keeps successful navigation READY and notifies later listeners", async () => {
    const runtime = createMapLibreAdapter({ containerId: "kfm-map-root" });
    const pending = runtime.initialize();
    const map = renderer.instances[0];
    map.emit("load");
    await pending;

    const observedLongitudes: number[] = [];
    runtime.subscribeSnapshot(() => {
      throw new Error("synthetic consumer listener failure");
    });
    runtime.subscribeSnapshot((snapshot) =>
      observedLongitudes.push(snapshot.camera.longitude),
    );

    expect(() =>
      runtime.setCamera({
        longitude: -97,
        latitude: 39,
        zoom: 8,
        bearing: 12,
        pitch: 25,
      }),
    ).not.toThrow();

    expect(observedLongitudes).toEqual([-97]);
    expect(map.removed).toBe(false);
    expect(runtime.getSnapshot()).toMatchObject({
      state: "READY",
      reason: null,
      camera: { longitude: -97, latitude: 39, zoom: 8, bearing: 12, pitch: 25 },
    });
  });

  it("cannot block disposal or renderer teardown", async () => {
    const runtime = createMapLibreAdapter({ containerId: "kfm-map-root" });
    const pending = runtime.initialize();
    const map = renderer.instances[0];
    map.emit("load");
    await pending;

    const observedStates: string[] = [];
    runtime.subscribeSnapshot(() => {
      throw new Error("synthetic consumer listener failure");
    });
    runtime.subscribeSnapshot((snapshot) => observedStates.push(snapshot.state));

    expect(() => runtime.dispose()).not.toThrow();
    expect(observedStates).toEqual(["DISPOSED"]);
    expect(map.removed).toBe(true);
    expect(runtime.getSnapshot()).toMatchObject({
      state: "DISPOSED",
      reason: "MAP_RUNTIME_DISPOSED",
      selection: null,
    });
  });
});
