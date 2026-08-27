import { beforeEach, describe, expect, it, vi } from "vitest";

type RendererHandler = (event?: unknown) => void;

type RendererInstance = {
  options: Record<string, unknown>;
  removed: boolean;
  jumpToCalls: Record<string, unknown>[];
  emit: (type: string) => void;
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

vi.mock("maplibre-gl", () => ({
  Map: class FakeMap {
    readonly options: Record<string, unknown>;
    readonly jumpToCalls: Record<string, unknown>[] = [];
    removed = false;
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

    emit(type: string): void {
      for (const handler of [...(this.handlers.get(type) ?? [])]) {
        handler({ type, error: { message: "synthetic renderer error" } });
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
  MapRuntimePortError,
} from "../src/index";
import { createMapLibreAdapter } from "../src/maplibre-adapter";

describe("package-owned MapLibreAdapter", () => {
  beforeEach(() => {
    renderer.instances.length = 0;
    renderer.throwOnConstruct = false;
  });

  it("fails closed before renderer acquisition for an invalid container ID", () => {
    expect(() => createMapLibreAdapter({ containerId: " unsafe container " })).toThrow(
      expect.objectContaining({ code: "MAP_RUNTIME_CONTAINER_INVALID" }),
    );
    expect(renderer.instances).toHaveLength(0);
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

  it("rejects an in-flight initialization when disposed", async () => {
    const runtime = createMapLibreAdapter({ containerId: "kfm-map-root" });
    const pending = runtime.initialize();
    const map = renderer.instances[0];

    runtime.dispose();

    await expect(pending).rejects.toMatchObject({ code: "MAP_RUNTIME_DISPOSED" });
    expect(map.removed).toBe(true);
    expect(runtime.getSnapshot().state).toBe("DISPOSED");
  });
});
