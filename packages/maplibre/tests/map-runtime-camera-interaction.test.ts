import { describe, expect, it } from "vitest";

import {
  MAP_RUNTIME_CAMERA_INTERACTION_PROFILE,
  applyMapRuntimeCameraInteraction,
} from "../src/map-runtime-camera-interaction";
import type { MapRuntimeCamera } from "../src/map-runtime-port";

const camera: MapRuntimeCamera = {
  longitude: -98,
  latitude: 38.5,
  zoom: 4,
  bearing: 0,
  pitch: 0,
};

function command(
  value:
    | "PAN_NORTH"
    | "PAN_SOUTH"
    | "PAN_EAST"
    | "PAN_WEST"
    | "ZOOM_IN"
    | "ZOOM_OUT"
    | "ROTATE_CLOCKWISE"
    | "ROTATE_COUNTERCLOCKWISE"
    | "PITCH_UP"
    | "PITCH_DOWN"
    | "RESET_ORIENTATION",
) {
  return {
    profile: MAP_RUNTIME_CAMERA_INTERACTION_PROFILE,
    command: value,
  } as const;
}

describe("Map runtime camera interaction", () => {
  it("applies zoom-scaled cardinal pan steps and wraps the antimeridian", () => {
    const east = applyMapRuntimeCameraInteraction(camera, command("PAN_EAST"));
    const north = applyMapRuntimeCameraInteraction(camera, command("PAN_NORTH"));
    const wrapped = applyMapRuntimeCameraInteraction(
      { ...camera, longitude: 179, zoom: 0 },
      command("PAN_EAST"),
    );

    expect(east.longitude).toBeCloseTo(-95.1875, 10);
    expect(north.latitude).toBeCloseTo(39.90625, 10);
    expect(wrapped.longitude).toBe(-136);
  });

  it("clamps polar pan to the Web Mercator latitude boundary", () => {
    const north = applyMapRuntimeCameraInteraction(
      { ...camera, latitude: 85, zoom: 0 },
      command("PAN_NORTH"),
    );
    const south = applyMapRuntimeCameraInteraction(
      { ...camera, latitude: -85, zoom: 0 },
      command("PAN_SOUTH"),
    );

    expect(north.latitude).toBe(85.051129);
    expect(south.latitude).toBe(-85.051129);
  });

  it("bounds zoom, bearing, and pitch while preserving a valid frozen camera", () => {
    const zoomIn = applyMapRuntimeCameraInteraction(
      { ...camera, zoom: 24 },
      command("ZOOM_IN"),
    );
    const zoomOut = applyMapRuntimeCameraInteraction(
      { ...camera, zoom: 0 },
      command("ZOOM_OUT"),
    );
    const clockwise = applyMapRuntimeCameraInteraction(
      { ...camera, bearing: 175 },
      command("ROTATE_CLOCKWISE"),
    );
    const counterclockwise = applyMapRuntimeCameraInteraction(
      { ...camera, bearing: -175 },
      command("ROTATE_COUNTERCLOCKWISE"),
    );
    const pitchUp = applyMapRuntimeCameraInteraction(
      { ...camera, pitch: 80 },
      command("PITCH_UP"),
    );
    const pitchDown = applyMapRuntimeCameraInteraction(
      { ...camera, pitch: 5 },
      command("PITCH_DOWN"),
    );

    expect(zoomIn.zoom).toBe(24);
    expect(zoomOut.zoom).toBe(0);
    expect(clockwise.bearing).toBe(-170);
    expect(counterclockwise.bearing).toBe(170);
    expect(pitchUp.pitch).toBe(85);
    expect(pitchDown.pitch).toBe(0);
    expect(Object.isFrozen(clockwise)).toBe(true);
  });

  it("resets orientation without changing center or zoom", () => {
    const original = {
      longitude: -101,
      latitude: 39,
      zoom: 7,
      bearing: 42,
      pitch: 55,
    } as const;
    const reset = applyMapRuntimeCameraInteraction(
      original,
      command("RESET_ORIENTATION"),
    );

    expect(reset).toEqual({
      longitude: -101,
      latitude: 39,
      zoom: 7,
      bearing: 0,
      pitch: 0,
    });
    expect(original.bearing).toBe(42);
    expect(original.pitch).toBe(55);
  });

  it("fails closed on malformed interaction envelopes", () => {
    const extraField = {
      profile: MAP_RUNTIME_CAMERA_INTERACTION_PROFILE,
      command: "ZOOM_IN",
      key: "+",
    } as unknown as Parameters<typeof applyMapRuntimeCameraInteraction>[1];
    const wrongProfile = {
      profile: "kfm.map-runtime-camera-interaction.v2",
      command: "ZOOM_IN",
    } as unknown as Parameters<typeof applyMapRuntimeCameraInteraction>[1];
    const unknownCommand = {
      profile: MAP_RUNTIME_CAMERA_INTERACTION_PROFILE,
      command: "FLY_TO_SECRET_SOURCE",
    } as unknown as Parameters<typeof applyMapRuntimeCameraInteraction>[1];

    for (const interaction of [extraField, wrongProfile, unknownCommand]) {
      expect(() =>
        applyMapRuntimeCameraInteraction(camera, interaction),
      ).toThrow(expect.objectContaining({ code: "MAP_RUNTIME_STATE_INVALID" }));
    }
  });

  it("preserves the finite camera-invalid boundary", () => {
    const invalidCamera = {
      ...camera,
      latitude: 90,
    } as MapRuntimeCamera;

    expect(() =>
      applyMapRuntimeCameraInteraction(invalidCamera, command("PAN_EAST")),
    ).toThrow(expect.objectContaining({ code: "MAP_RUNTIME_CAMERA_INVALID" }));
  });
});
