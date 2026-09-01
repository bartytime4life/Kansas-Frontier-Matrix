import { describe, expect, it } from "vitest";

import {
  MAP_RUNTIME_CAMERA_STATE_PROFILE,
  MAX_MAP_RUNTIME_CAMERA_STATE_LENGTH,
  decodeMapRuntimeCameraState,
  encodeMapRuntimeCameraState,
  isMapRuntimeCameraState,
} from "../src/map-runtime-navigation-state";
import { MapRuntimePortError } from "../src/map-runtime-port";

const KANSAS_CAMERA = Object.freeze({
  longitude: -98.4842,
  latitude: 38.4988,
  zoom: 5.5,
  bearing: 0,
  pitch: 0,
});

describe("map runtime navigation state", () => {
  it("exposes one stable renderer-neutral profile", () => {
    expect(MAP_RUNTIME_CAMERA_STATE_PROFILE).toBe(
      "kfm.map-runtime-camera-state.v1",
    );
    expect(MAX_MAP_RUNTIME_CAMERA_STATE_LENGTH).toBe(160);
  });

  it("round-trips a camera through one canonical token", () => {
    const token = encodeMapRuntimeCameraState(KANSAS_CAMERA);

    expect(token).toBe("v1:-98.4842,38.4988,5.5,0,0");
    const decoded = decodeMapRuntimeCameraState(token);
    expect(decoded).toEqual(KANSAS_CAMERA);
    expect(Object.isFrozen(decoded)).toBe(true);
    expect(isMapRuntimeCameraState(token)).toBe(true);
  });

  it("normalizes negative zero during encoding", () => {
    expect(
      encodeMapRuntimeCameraState({
        longitude: -0,
        latitude: 0,
        zoom: 0,
        bearing: -0,
        pitch: 0,
      }),
    ).toBe("v1:0,0,0,0,0");
  });

  it.each([
    null,
    "",
    "v2:-98,38,5,0,0",
    "v1:-98,38,5,0",
    "v1:-98,38,25,0,0",
    "v1:-0,0,0,0,0",
    "v1: -98,38,5,0,0",
    "v1:NaN,38,5,0,0",
    `v1:${"1".repeat(MAX_MAP_RUNTIME_CAMERA_STATE_LENGTH)}`,
  ])("fails closed for non-canonical or invalid state %#", (value) => {
    expect(isMapRuntimeCameraState(value)).toBe(false);
    expect(() => decodeMapRuntimeCameraState(value)).toThrowError(
      expect.objectContaining<MapRuntimePortError>({
        code: "MAP_RUNTIME_STATE_INVALID",
      }),
    );
  });

  it("preserves direct camera validation for encode callers", () => {
    expect(() =>
      encodeMapRuntimeCameraState({
        longitude: 181,
        latitude: 38,
        zoom: 5,
        bearing: 0,
        pitch: 0,
      }),
    ).toThrowError(
      expect.objectContaining<MapRuntimePortError>({
        code: "MAP_RUNTIME_CAMERA_INVALID",
      }),
    );
  });
});
