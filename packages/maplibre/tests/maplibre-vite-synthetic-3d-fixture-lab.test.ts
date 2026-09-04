import { describe, expect, it, vi } from "vitest";

const harness = vi.hoisted(() => ({
  fixtureLab: Object.freeze({ profile: "synthetic-3d-fixture-lab" }),
  createFixtureLab: vi.fn(),
  setWorkerUrl: vi.fn(),
}));

vi.mock("maplibre-gl", () => ({
  setWorkerUrl: harness.setWorkerUrl,
}));

vi.mock("maplibre-gl/dist/maplibre-gl-worker.mjs?worker&url", () => ({
  default: "/assets/maplibre-gl-worker.fixture.js",
}));

vi.mock("../src/maplibre-adapter", () => ({
  createMapLibreAdapter: vi.fn(),
}));

vi.mock("../src/synthetic-3d-fixture-lab", () => ({
  createSynthetic3DFixtureLab: harness.createFixtureLab,
}));

import { createViteSynthetic3DFixtureLab } from "../src/maplibre-vite-adapter";

describe("package-owned Vite synthetic 3D fixture seam", () => {
  it("configures the same-origin worker before dynamically creating the lab", async () => {
    harness.createFixtureLab.mockReturnValue(harness.fixtureLab);
    const options = {
      containerId: "kfm-maplibre-fixture",
      interactive: false,
    };

    await expect(createViteSynthetic3DFixtureLab(options)).resolves.toBe(
      harness.fixtureLab,
    );
    expect(harness.setWorkerUrl).toHaveBeenCalledWith(
      "/assets/maplibre-gl-worker.fixture.js",
    );
    expect(harness.setWorkerUrl).toHaveBeenCalledTimes(1);
    expect(harness.createFixtureLab).toHaveBeenCalledWith(options);
    expect(harness.setWorkerUrl.mock.invocationCallOrder[0]).toBeLessThan(
      harness.createFixtureLab.mock.invocationCallOrder[0]!,
    );
  });
});
