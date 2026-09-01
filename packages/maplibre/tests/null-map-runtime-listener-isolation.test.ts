import { describe, expect, it, vi } from "vitest";

import {
  MAP_FEATURE_SELECTION_PROFILE,
  createNullMapRuntime,
  type MapFeatureSelection,
} from "../src/index";

const selection: MapFeatureSelection = Object.freeze({
  profile: MAP_FEATURE_SELECTION_PROFILE,
  selectionId: "selection:synthetic:null-listener-isolation",
  layerId: "layer:synthetic:null-listener-isolation",
  featureId: "feature:synthetic:null-listener-isolation",
  evidenceRefs: Object.freeze(["evidence:synthetic:null-listener-isolation"]),
});

describe("NullMapRuntime listener isolation", () => {
  it("keeps initialization finite when an earlier snapshot observer throws", async () => {
    const runtime = createNullMapRuntime();
    const later = vi.fn();

    runtime.subscribeSnapshot(() => {
      throw new Error("synthetic snapshot observer failure");
    });
    runtime.subscribeSnapshot(later);

    await expect(runtime.initialize()).resolves.toMatchObject({
      state: "READY",
      reason: null,
    });
    expect(later.mock.calls.map(([snapshot]) => snapshot.state)).toEqual([
      "INITIALIZING",
      "READY",
    ]);
  });

  it("does not convert a successful camera update into an observer failure", async () => {
    const runtime = createNullMapRuntime();
    await runtime.initialize();
    const later = vi.fn();

    runtime.subscribeSnapshot(() => {
      throw new Error("synthetic snapshot observer failure");
    });
    runtime.subscribeSnapshot(later);

    const nextCamera = {
      ...runtime.getSnapshot().camera,
      zoom: 7,
      bearing: 15,
    };

    expect(() => runtime.setCamera(nextCamera)).not.toThrow();
    expect(runtime.getSnapshot().camera).toEqual(nextCamera);
    expect(later).toHaveBeenCalledTimes(1);
    expect(later.mock.calls[0]?.[0].camera).toEqual(nextCamera);
  });

  it("keeps selection publication deterministic across faulty observers", async () => {
    const runtime = createNullMapRuntime();
    await runtime.initialize();
    const laterSnapshot = vi.fn();
    const laterSelection = vi.fn();

    runtime.subscribeSnapshot(() => {
      throw new Error("synthetic snapshot observer failure");
    });
    runtime.subscribeSnapshot(laterSnapshot);
    runtime.subscribeSelection(() => {
      throw new Error("synthetic selection observer failure");
    });
    runtime.subscribeSelection(laterSelection);

    expect(() => runtime.emitSelection(selection)).not.toThrow();
    expect(runtime.getSnapshot().selection).toEqual(selection);
    expect(laterSnapshot).toHaveBeenCalledTimes(1);
    expect(laterSelection).toHaveBeenCalledTimes(1);
    expect(laterSelection).toHaveBeenCalledWith(selection);
  });

  it("allows terminal disposal even when an observer throws", async () => {
    const runtime = createNullMapRuntime();
    await runtime.initialize();
    const later = vi.fn();

    runtime.subscribeSnapshot(() => {
      throw new Error("synthetic snapshot observer failure");
    });
    runtime.subscribeSnapshot(later);

    expect(() => runtime.dispose()).not.toThrow();
    expect(runtime.getSnapshot()).toMatchObject({
      state: "DISPOSED",
      selection: null,
      reason: "MAP_RUNTIME_DISPOSED",
    });
    expect(later).toHaveBeenCalledTimes(1);
    expect(later.mock.calls[0]?.[0].state).toBe("DISPOSED");
  });
});
