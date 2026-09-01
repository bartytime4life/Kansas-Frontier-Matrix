import { describe, expect, it } from "vitest";

import {
  MAP_RUNTIME_TERRAIN_FALLBACK_PROFILE,
  resolveMapRuntimeTerrainState,
} from "../src/map-runtime-terrain-fallback";

const terrainRequest = {
  profile: MAP_RUNTIME_TERRAIN_FALLBACK_PROFILE,
  mode: "TERRAIN",
  exaggeration: 1.5,
  fallback: "FLAT",
} as const;

describe("renderer-neutral terrain fallback", () => {
  it("retains flat mode without requiring terrain capabilities", () => {
    const state = resolveMapRuntimeTerrainState(
      {
        profile: MAP_RUNTIME_TERRAIN_FALLBACK_PROFILE,
        mode: "FLAT",
        exaggeration: 0,
        fallback: "FLAT",
      },
      { terrainSupported: false, demSourceReady: false },
    );

    expect(state).toEqual({
      profile: MAP_RUNTIME_TERRAIN_FALLBACK_PROFILE,
      mode: "FLAT",
      exaggeration: 0,
      reason: null,
    });
    expect(Object.isFrozen(state)).toBe(true);
  });

  it("selects terrain only when renderer support and source readiness are supplied", () => {
    expect(
      resolveMapRuntimeTerrainState(terrainRequest, {
        terrainSupported: true,
        demSourceReady: true,
      }),
    ).toEqual({
      profile: MAP_RUNTIME_TERRAIN_FALLBACK_PROFILE,
      mode: "TERRAIN",
      exaggeration: 1.5,
      reason: null,
    });
  });

  it("falls back to flat when terrain is unsupported", () => {
    expect(
      resolveMapRuntimeTerrainState(terrainRequest, {
        terrainSupported: false,
        demSourceReady: true,
      }),
    ).toEqual({
      profile: MAP_RUNTIME_TERRAIN_FALLBACK_PROFILE,
      mode: "FLAT",
      exaggeration: 0,
      reason: "TERRAIN_UNSUPPORTED",
    });
  });

  it("falls back to flat when the supplied DEM readiness fact is false", () => {
    expect(
      resolveMapRuntimeTerrainState(terrainRequest, {
        terrainSupported: true,
        demSourceReady: false,
      }),
    ).toEqual({
      profile: MAP_RUNTIME_TERRAIN_FALLBACK_PROFILE,
      mode: "FLAT",
      exaggeration: 0,
      reason: "TERRAIN_SOURCE_UNAVAILABLE",
    });
  });

  it.each([
    { ...terrainRequest, profile: "wrong" },
    { ...terrainRequest, mode: "GLOBE" },
    { ...terrainRequest, exaggeration: 0 },
    { ...terrainRequest, exaggeration: 5.1 },
    { ...terrainRequest, exaggeration: Number.NaN },
    { ...terrainRequest, fallback: "TERRAIN" },
    { ...terrainRequest, extra: true },
    {
      profile: MAP_RUNTIME_TERRAIN_FALLBACK_PROFILE,
      mode: "FLAT",
      exaggeration: 1,
      fallback: "FLAT",
    },
  ])("rejects malformed terrain requests", (request) => {
    expect(() =>
      resolveMapRuntimeTerrainState(request as never, {
        terrainSupported: true,
        demSourceReady: true,
      }),
    ).toThrow(expect.objectContaining({ code: "MAP_RUNTIME_STATE_INVALID" }));
  });

  it.each([
    { terrainSupported: true },
    { terrainSupported: true, demSourceReady: "yes" },
    { terrainSupported: true, demSourceReady: true, extra: true },
  ])("rejects malformed supplied capabilities", (capabilities) => {
    expect(() =>
      resolveMapRuntimeTerrainState(terrainRequest, capabilities as never),
    ).toThrow(expect.objectContaining({ code: "MAP_RUNTIME_STATE_INVALID" }));
  });
});
