import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";
import { validateStyleMin } from "@maplibre/maplibre-gl-style-spec";

const source = await readFile(new URL("../app/globe-context.ts", import.meta.url), "utf8");
const js = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const globe = await import(`data:text/javascript;base64,${Buffer.from(js).toString("base64")}`);

test("globe releases regional navigation limits and repeated transitions restore them without drift", () => {
  let bounds = [[-104.8, 34.8], [-92, 42.2]], minZoom = 4;
  const mutations = [];
  const map = {
    getMaxBounds() { return bounds && { getWest: () => bounds[0][0], getSouth: () => bounds[0][1], getEast: () => bounds[1][0], getNorth: () => bounds[1][1] }; },
    getMinZoom: () => minZoom,
    setMaxBounds(value) { mutations.push("bounds"); bounds = value; },
    setMinZoom(value) { mutations.push("zoom"); minZoom = value; },
  };
  for (let i = 0; i < 3; i++) {
    globe.applyProjectionNavigationLimits(map, "globe");
    assert.equal(bounds, null); assert.equal(minZoom, 0);
    const count = mutations.length;
    globe.applyProjectionNavigationLimits(map, "globe");
    assert.equal(mutations.length, count);
    globe.applyProjectionNavigationLimits(map, "mercator");
    assert.deepEqual(bounds, [[-104.8, 34.8], [-92, 42.2]]); assert.equal(minZoom, 4);
  }
  const count = mutations.length;
  globe.applyProjectionNavigationLimits(map, "mercator");
  assert.equal(mutations.length, count);
});

test("camera readings use observed renderer values and fail closed when they cannot be read", () => {
  const map = {
    getCenter: () => ({ lng: 261.62, lat: 38.48 }), getZoom: () => .6,
    getBearing: () => 18.2, getPitch: () => 0, getProjection: () => ({ type: "globe" }),
    isStyleLoaded: () => true, areTilesLoaded: () => false,
  };
  const reading = globe.readGlobeCamera(map, new Date("2026-09-24T23:00:00Z"));
  assert.ok(Math.abs(reading.longitude - -98.38) < .000001);
  assert.equal(reading.latitude, 38.48); assert.equal(reading.zoom, .6);
  assert.equal(reading.projection, "globe"); assert.equal(reading.tilesLoaded, false);
  assert.equal(reading.sampledAt, "2026-09-24T23:00:00.000Z");
  assert.equal("altitude" in reading, false);
  assert.equal(globe.readGlobeCamera({ ...map, getZoom: () => NaN }), null);
  assert.equal(globe.readGlobeCamera({ ...map, getCenter: () => ({ lng: 0, lat: 91 }) }), null);
  assert.equal(globe.readGlobeCamera({ ...map, getProjection() { throw new Error("style missing"); } }), null);
  assert.equal(globe.readGlobeCamera({ ...map, getProjection: () => undefined }).projection, "mercator");
  assert.equal(globe.readGlobeCamera({ ...map, getProjection: () => ({ type: "unknown" }) }).projection, "unknown");
});

test("globe viewpoints remain distinct while Earth Engine opens installed map layers", async () => {
  assert.ok(globe.GLOBE_VIEWPOINTS.earth.zoom < globe.GLOBE_VIEWPOINTS.continent.zoom);
  assert.ok(globe.GLOBE_VIEWPOINTS.continent.zoom < globe.GLOBE_VIEWPOINTS.kansas.zoom);
  for (const preset of Object.values(globe.GLOBE_VIEWPOINTS)) {
    assert.equal(preset.pitch, 0); assert.equal(preset.bearing, 0);
  }
  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  assert.match(page, /onClick={\(\) => { setUndergroundOpen\(false\); activateMapRepresentation\("globe"\); }}/);
  assert.match(page, /const openEarthEngineLayers = useCallback/);
  assert.match(page, /setPendingCatalogTarget\("earth-engine-context-controls"\)/);
  assert.doesNotMatch(page, /<EarthEngineGlobe/);
  assert.match(page, /restoringGlobe \? 0 : 4/);
});

test("globe cue sizing is continuous and returns to full size at close view", () => {
  assert.equal(globe.globeOverviewSizeScale(0), 0);
  assert.ok(globe.globeOverviewSizeScale(2) < globe.globeOverviewSizeScale(4));
  assert.ok(globe.globeOverviewSizeScale(4) < globe.globeOverviewSizeScale(5.45));
  assert.ok(globe.globeOverviewSizeScale(5.45) < globe.globeOverviewSizeScale(10));
  assert.equal(globe.globeOverviewSizeScale(10), 1);
  assert.equal(globe.globeOverviewSizeScale(18), 1);
  const paint = globe.globeOverviewPaintSize(["interpolate", ["linear"], ["zoom"], 4, 20, 10, 34]);
  assert.deepEqual(paint.slice(0, 9), ["interpolate", ["linear"], ["zoom"], 0, 0, 2, 1.6, 4, 4.4]);
  assert.deepEqual(paint.slice(-2), [10, 34]);
  const style = {
    version: 8,
    sources: { sample: { type: "geojson", data: { type: "FeatureCollection", features: [] } } },
    layers: [{ id: "sample", type: "circle", source: "sample", paint: {
      "circle-radius": globe.globeOverviewPaintSize(["interpolate", ["linear"], ["zoom"], 4, ["+", 7, ["get", "magnitude"]], 10, ["+", 12, ["get", "magnitude"]]]),
      "circle-stroke-width": globe.globeOverviewPaintSize(["case", ["get", "selected"], 3.4, 1.4]),
    } }],
  };
  assert.deepEqual(validateStyleMin(style).map((error) => error.message), []);
  assert.equal(globe.onVisibleGlobeHemisphere({ lng: -98, lat: 39 }, [-97, 39]), true);
  assert.equal(globe.onVisibleGlobeHemisphere({ lng: 82, lat: 39 }, [-97, 39]), false);
});
