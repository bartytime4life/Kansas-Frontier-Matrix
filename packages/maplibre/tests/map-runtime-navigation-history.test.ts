import { describe, expect, it } from "vitest";

import {
  DEFAULT_MAP_RUNTIME_NAVIGATION_HISTORY_CAPACITY,
  MAP_RUNTIME_NAVIGATION_HISTORY_PROFILE,
  MAX_MAP_RUNTIME_NAVIGATION_HISTORY_CAPACITY,
  createMapRuntimeNavigationHistory,
} from "../src/map-runtime-navigation-history";
import { MapRuntimePortError } from "../src/map-runtime-port";
import { createNullMapRuntime } from "../src/null-map-runtime";

const CAMERA_A = Object.freeze({
  longitude: -98,
  latitude: 38,
  zoom: 5,
  bearing: 0,
  pitch: 0,
});
const CAMERA_B = Object.freeze({
  longitude: -97,
  latitude: 38.5,
  zoom: 6,
  bearing: 0,
  pitch: 0,
});
const CAMERA_C = Object.freeze({
  longitude: -96,
  latitude: 39,
  zoom: 7,
  bearing: 5,
  pitch: 10,
});
const CAMERA_D = Object.freeze({
  longitude: -95,
  latitude: 39.5,
  zoom: 8,
  bearing: 10,
  pitch: 20,
});

function capturePortError(callback: () => unknown): MapRuntimePortError {
  try {
    callback();
  } catch (error) {
    if (error instanceof MapRuntimePortError) return error;
    throw error;
  }
  throw new Error("Expected MapRuntimePortError.");
}

describe("map runtime navigation history", () => {
  it("exposes one stable bounded renderer-neutral profile", () => {
    expect(MAP_RUNTIME_NAVIGATION_HISTORY_PROFILE).toBe(
      "kfm.map-runtime-navigation-history.v1",
    );
    expect(DEFAULT_MAP_RUNTIME_NAVIGATION_HISTORY_CAPACITY).toBe(32);
    expect(MAX_MAP_RUNTIME_NAVIGATION_HISTORY_CAPACITY).toBe(128);
  });

  it("captures the first READY camera when created before initialization", async () => {
    const runtime = createNullMapRuntime(CAMERA_A);
    const history = createMapRuntimeNavigationHistory(runtime);

    expect(history.getState()).toEqual({
      profile: MAP_RUNTIME_NAVIGATION_HISTORY_PROFILE,
      length: 0,
      index: -1,
      canGoBack: false,
      canGoForward: false,
    });

    await runtime.initialize();

    expect(history.getState()).toEqual({
      profile: MAP_RUNTIME_NAVIGATION_HISTORY_PROFILE,
      length: 1,
      index: 0,
      canGoBack: false,
      canGoForward: false,
    });
  });

  it("replays back and forward without duplicating history", async () => {
    const runtime = createNullMapRuntime(CAMERA_A);
    await runtime.initialize();
    const history = createMapRuntimeNavigationHistory(runtime);

    runtime.setCamera(CAMERA_B);
    runtime.setCamera(CAMERA_C);

    expect(history.getState()).toMatchObject({
      length: 3,
      index: 2,
      canGoBack: true,
      canGoForward: false,
    });
    expect(history.back()?.camera).toEqual(CAMERA_B);
    expect(history.getState()).toMatchObject({
      length: 3,
      index: 1,
      canGoBack: true,
      canGoForward: true,
    });
    expect(history.forward()?.camera).toEqual(CAMERA_C);
    expect(history.getState()).toMatchObject({
      length: 3,
      index: 2,
      canGoBack: true,
      canGoForward: false,
    });
  });

  it("truncates forward history after a new external camera change", async () => {
    const runtime = createNullMapRuntime(CAMERA_A);
    await runtime.initialize();
    const history = createMapRuntimeNavigationHistory(runtime);

    runtime.setCamera(CAMERA_B);
    runtime.setCamera(CAMERA_C);
    expect(history.back()?.camera).toEqual(CAMERA_B);

    runtime.setCamera(CAMERA_D);

    expect(history.getState()).toMatchObject({
      length: 3,
      index: 2,
      canGoForward: false,
    });
    expect(history.back()?.camera).toEqual(CAMERA_B);
    expect(history.back()?.camera).toEqual(CAMERA_A);
    expect(history.back()).toBeNull();
  });

  it("bounds retained camera history and ignores duplicate snapshots", async () => {
    const runtime = createNullMapRuntime(CAMERA_A);
    await runtime.initialize();
    const history = createMapRuntimeNavigationHistory(runtime, { capacity: 3 });

    runtime.setCamera(CAMERA_A);
    runtime.setCamera(CAMERA_B);
    runtime.setCamera(CAMERA_C);
    runtime.setCamera(CAMERA_D);

    expect(history.getState()).toMatchObject({ length: 3, index: 2 });
    expect(history.back()?.camera).toEqual(CAMERA_C);
    expect(history.back()?.camera).toEqual(CAMERA_B);
    expect(history.back()).toBeNull();
  });

  it.each([1, 129, 2.5, Number.NaN])(
    "fails closed for invalid capacity %#",
    (capacity) => {
      const runtime = createNullMapRuntime(CAMERA_A);
      expect(
        capturePortError(() =>
          createMapRuntimeNavigationHistory(runtime, { capacity }),
        ).code,
      ).toBe("MAP_RUNTIME_STATE_INVALID");
    },
  );

  it("unsubscribes and rejects navigation after disposal", async () => {
    const runtime = createNullMapRuntime(CAMERA_A);
    await runtime.initialize();
    const history = createMapRuntimeNavigationHistory(runtime);

    runtime.setCamera(CAMERA_B);
    history.dispose();
    runtime.setCamera(CAMERA_C);

    expect(history.getState()).toEqual({
      profile: MAP_RUNTIME_NAVIGATION_HISTORY_PROFILE,
      length: 0,
      index: -1,
      canGoBack: false,
      canGoForward: false,
    });
    expect(capturePortError(() => history.back()).code).toBe(
      "MAP_RUNTIME_DISPOSED",
    );
  });
});
