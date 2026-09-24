import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

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

test("globe viewpoints are distinct, while the recipe study area remains explicitly Kansas", async () => {
  assert.ok(globe.GLOBE_VIEWPOINTS.earth.zoom < globe.GLOBE_VIEWPOINTS.continent.zoom);
  assert.ok(globe.GLOBE_VIEWPOINTS.continent.zoom < globe.GLOBE_VIEWPOINTS.kansas.zoom);
  for (const preset of Object.values(globe.GLOBE_VIEWPOINTS)) {
    assert.equal(preset.pitch, 0); assert.equal(preset.bearing, 0);
  }
  const panel = await readFile(new URL("../app/earth-engine-globe.tsx", import.meta.url), "utf8");
  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  assert.match(panel, /Changing the viewpoint does not change the analysis area/);
  assert.match(panel, /Map readings, not satellite telemetry/);
  assert.match(panel, /No Earth Engine imagery or sensor telemetry is displayed/);
  assert.match(panel, /recipe summarizes the full year, not the selected map instant/);
  assert.match(page, /role="group" aria-label="Globe and Earth Engine"/);
  assert.match(page, /earthEngineOpen && projection === "globe" && <EarthEngineGlobe/);
  assert.match(page, /restoringGlobe \? 0 : 4/);
});
