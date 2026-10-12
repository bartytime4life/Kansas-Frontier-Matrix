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
    private readonly handlers = new globalThis.Map<
      string,
      Set<RendererHandler>
    >();

    constructor() {
      renderer.instances.push(this);
    }

    on(type: string, handler: RendererHandler): { unsubscribe: () => void } {
      const listeners = this.handlers.get(type) ?? new Set<RendererHandler>();
      listeners.add(handler);
      this.handlers.set(type, listeners);
      return { unsubscribe: () => listeners.delete(handler) };
    }

    emit(type: string): void {
      for (const handler of [...(this.handlers.get(type) ?? [])]) handler();
    }

    getCenter(): { lng: number; lat: number } {
      return { lng: -98.4842, lat: 38.4988 };
    }

    getZoom(): number {
      return 6;
    }

    getBearing(): number {
      return 0;
    }

    getPitch(): number {
      return 0;
    }

    jumpTo(): this {
      return this;
    }

    remove(): void {
      this.removed = true;
    }
  },
}));

import {
  DEFAULT_MAPLIBRE_INITIALIZATION_DEADLINE_MS,
  createMapLibreAdapter,
} from "../src/maplibre-adapter";

describe("MapLibreAdapter finite initialization deadline", () => {
  beforeEach(() => {
    renderer.instances.length = 0;
    vi.useFakeTimers();
    vi.stubGlobal("document", {
      createElement: () => ({
        getContext: (type: string) =>
          type === "webgl2" ? { getExtension: () => null } : null,
      }),
    });
  });

  afterEach(() => {
    vi.useRealTimers();
    vi.unstubAllGlobals();
  });

  it.each([0, -1, 1.5, 60_001, Number.POSITIVE_INFINITY])(
    "rejects an invalid initialization deadline before renderer acquisition (%s)",
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

  it("fails a renderer that never settles instead of leaving initialization pending", async () => {
    expect(DEFAULT_MAPLIBRE_INITIALIZATION_DEADLINE_MS).toBe(10_000);
    const runtime = createMapLibreAdapter({
      containerId: "kfm-map-root",
      initializationDeadlineMs: 25,
    });
    const pending = runtime.initialize();
    const rejection = expect(pending).rejects.toMatchObject({
      code: "MAP_RUNTIME_INITIALIZATION_FAILED",
    });
    const map = renderer.instances[0];

    expect(vi.getTimerCount()).toBe(1);
    await vi.advanceTimersByTimeAsync(24);
    expect(runtime.getSnapshot().state).toBe("INITIALIZING");

    await vi.advanceTimersByTimeAsync(1);
    await rejection;
    expect(runtime.getSnapshot()).toMatchObject({
      state: "ERROR",
      reason: "MAP_RUNTIME_ERROR",
      selection: null,
    });
    expect(map.removed).toBe(true);
    expect(vi.getTimerCount()).toBe(0);

    map.emit("load");
    expect(runtime.getSnapshot().state).toBe("ERROR");
  });

  it("clears the deadline after successful load", async () => {
    const runtime = createMapLibreAdapter({
      containerId: "kfm-map-root",
      initializationDeadlineMs: 25,
    });
    const pending = runtime.initialize();
    const map = renderer.instances[0];

    map.emit("load");
    await expect(pending).resolves.toMatchObject({ state: "READY" });
    expect(vi.getTimerCount()).toBe(0);

    await vi.advanceTimersByTimeAsync(25);
    expect(runtime.getSnapshot()).toMatchObject({ state: "READY", reason: null });
  });

  it("converts a ready-listener exception into a finite initialization failure", async () => {
    const runtime = createMapLibreAdapter({
      containerId: "kfm-map-root",
      initializationDeadlineMs: 25,
    });
    runtime.subscribeSnapshot((snapshot) => {
      if (snapshot.state === "READY" || snapshot.state === "ERROR") {
        throw new Error("synthetic ready listener failure");
      }
    });
    const pending = runtime.initialize();
    const map = renderer.instances[0];

    map.emit("load");
    await expect(pending).rejects.toMatchObject({
      code: "MAP_RUNTIME_INITIALIZATION_FAILED",
    });
    expect(runtime.getSnapshot()).toMatchObject({
      state: "ERROR",
      reason: "MAP_RUNTIME_ERROR",
    });
    expect(map.removed).toBe(true);
    expect(vi.getTimerCount()).toBe(0);
  });
});
