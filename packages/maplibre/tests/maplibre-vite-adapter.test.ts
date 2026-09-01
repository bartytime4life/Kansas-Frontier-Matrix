import { describe, expect, it, vi } from "vitest";

const harness = vi.hoisted(() => ({
  adapter: Object.freeze({ profile: "synthetic-adapter" }),
  createAdapter: vi.fn(),
  setWorkerUrl: vi.fn(),
}));

vi.mock("maplibre-gl", () => ({
  setWorkerUrl: harness.setWorkerUrl,
}));

vi.mock("maplibre-gl/dist/maplibre-gl-worker.mjs?worker&url", () => ({
  default: "/assets/maplibre-gl-worker.fixture.js",
}));

vi.mock("../src/maplibre-adapter", () => ({
  createMapLibreAdapter: harness.createAdapter,
}));

import { createViteMapLibreAdapter } from "../src/maplibre-vite-adapter";

describe("package-owned Vite MapLibre adapter", () => {
  it("configures the self-contained worker once before creating adapters", () => {
    harness.createAdapter.mockReturnValue(harness.adapter);
    const first = { containerId: "first-map", interactive: false };
    const second = { containerId: "second-map" };

    expect(createViteMapLibreAdapter(first)).toBe(harness.adapter);
    expect(createViteMapLibreAdapter(second)).toBe(harness.adapter);
    expect(harness.setWorkerUrl).toHaveBeenCalledWith(
      "/assets/maplibre-gl-worker.fixture.js",
    );
    expect(harness.setWorkerUrl).toHaveBeenCalledTimes(1);
    expect(harness.setWorkerUrl.mock.invocationCallOrder[0]).toBeLessThan(
      harness.createAdapter.mock.invocationCallOrder[0]!,
    );
    expect(harness.createAdapter).toHaveBeenNthCalledWith(1, first);
    expect(harness.createAdapter).toHaveBeenNthCalledWith(2, second);
  });
});