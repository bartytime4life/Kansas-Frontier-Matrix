import { describe, expect, it } from "vitest";

import { fitMapRuntimeCameraToBounds } from "../src/map-runtime-bounds-fit";

describe("Map runtime bounds fit", () => {
  it("fits ordinary bounds into a finite renderer-neutral camera", () => {
    const camera = fitMapRuntimeCameraToBounds(
      { west: -102.0517, south: 36.993, east: -94.5884, north: 40.0032 },
      { widthPx: 1200, heightPx: 800, paddingPx: 32 },
    );

    expect(camera.longitude).toBeCloseTo(-98.32005, 5);
    expect(camera.latitude).toBeGreaterThan(38);
    expect(camera.latitude).toBeLessThan(39);
    expect(camera.zoom).toBeGreaterThan(5);
    expect(camera.zoom).toBeLessThan(7);
    expect(camera.bearing).toBe(0);
    expect(camera.pitch).toBe(0);
    expect(Object.isFrozen(camera)).toBe(true);
  });

  it("supports antimeridian-crossing bounds without expanding to the long world arc", () => {
    const camera = fitMapRuntimeCameraToBounds(
      { west: 170, south: -10, east: -170, north: 10 },
      { widthPx: 1024, heightPx: 768 },
    );

    expect(camera.longitude).toBe(180);
    expect(camera.latitude).toBeCloseTo(0, 10);
    expect(camera.zoom).toBeGreaterThan(4);
  });

  it("reduces zoom when padding consumes viewport area", () => {
    const bounds = { west: -101, south: 37, east: -95, north: 40 } as const;
    const unpadded = fitMapRuntimeCameraToBounds(bounds, {
      widthPx: 1200,
      heightPx: 800,
    });
    const padded = fitMapRuntimeCameraToBounds(bounds, {
      widthPx: 1200,
      heightPx: 800,
      paddingPx: 200,
    });

    expect(padded.zoom).toBeLessThan(unpadded.zoom);
  });

  it("uses maxZoom for a point bounds and honors an explicit zoom ceiling", () => {
    const camera = fitMapRuntimeCameraToBounds(
      { west: -98, south: 38, east: -98, north: 38 },
      { widthPx: 800, heightPx: 600 },
      { maxZoom: 14 },
    );

    expect(camera).toMatchObject({
      longitude: -98,
      latitude: 38,
      zoom: 14,
      bearing: 0,
      pitch: 0,
    });
  });

  it("fails closed on invalid geographic, shape, viewport, and zoom inputs", () => {
    expect(() =>
      fitMapRuntimeCameraToBounds(
        { west: -181, south: 37, east: -95, north: 40 },
        { widthPx: 800, heightPx: 600 },
      ),
    ).toThrow(expect.objectContaining({ code: "MAP_RUNTIME_STATE_INVALID" }));

    const extraFieldBounds = {
      west: -101,
      south: 37,
      east: -95,
      north: 40,
      rawSource: "forbidden",
    } as unknown as Parameters<typeof fitMapRuntimeCameraToBounds>[0];
    expect(() =>
      fitMapRuntimeCameraToBounds(extraFieldBounds, {
        widthPx: 800,
        heightPx: 600,
      }),
    ).toThrow(expect.objectContaining({ code: "MAP_RUNTIME_STATE_INVALID" }));

    expect(() =>
      fitMapRuntimeCameraToBounds(
        { west: -101, south: 37, east: -95, north: 40 },
        { widthPx: 100, heightPx: 100, paddingPx: 50 },
      ),
    ).toThrow(expect.objectContaining({ code: "MAP_RUNTIME_STATE_INVALID" }));

    expect(() =>
      fitMapRuntimeCameraToBounds(
        { west: -101, south: 37, east: -95, north: 40 },
        { widthPx: 800, heightPx: 600 },
        { minZoom: 12, maxZoom: 8 },
      ),
    ).toThrow(expect.objectContaining({ code: "MAP_RUNTIME_STATE_INVALID" }));
  });
});
