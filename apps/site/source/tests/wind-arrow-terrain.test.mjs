import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import ts from "typescript";

const modules = new Map();
const spaUrl = import.meta.resolve("sunrise-sunset-js");
const clippingUrl = new URL("../node_modules/polygon-clipping/dist/polygon-clipping.esm.js", import.meta.url).href;
async function moduleUrl(file) {
  file = path.resolve(file);
  if (modules.has(file)) return modules.get(file);
  let js = ts.transpileModule(await readFile(file, "utf8"), {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
  }).outputText;
  js = js.replaceAll('from "sunrise-sunset-js"', `from ${JSON.stringify(spaUrl)}`);
  js = js.replaceAll('from "polygon-clipping"', `from ${JSON.stringify(clippingUrl)}`);
  for (const match of [...js.matchAll(/from ["'](\.[^"']+)["']/g)]) {
    js = js.replace(match[0], `from ${JSON.stringify(await moduleUrl(path.resolve(path.dirname(file), match[1]) + ".ts"))}`);
  }
  const url = `data:text/javascript;base64,${Buffer.from(js).toString("base64")}`;
  modules.set(file, url);
  return url;
}

const wind = await import(await moduleUrl("app/wind-arrow-data.ts"));
const windClient = await import(await moduleUrl("app/wind-flow-client.ts"));
const windCanvas = await import(await moduleUrl("app/wind-arrow-canvas.ts"));
const terrain = await import(await moduleUrl("app/map-runtime.ts"));
const terrainSources = await import(await moduleUrl("app/terrain-sources.ts"));
const NOW = Date.parse("2026-09-27T16:20:00Z");
const extent = (bbox) => new Request(`https://kfm.test/api/wind-arrows?bbox=${bbox}`);
const modelRows = (url, time = "2026-09-27T16:00") => {
  const query = new URL(url).searchParams;
  const latitudes = query.get("latitude").split(",").map(Number);
  const longitudes = query.get("longitude").split(",").map(Number);
  return latitudes.map((latitude, index) => ({
    latitude,
    longitude: longitudes[index],
    hourly: { time: [time], wind_speed_10m: [4], wind_direction_10m: [270] },
  }));
};

test("wind route rejects arbitrary requests before contacting its fixed model source", async () => {
  let calls = 0;
  const serve = wind.createWindArrowService({ now: () => NOW, fetchUpstream: async () => { calls += 1; throw new Error("unexpected fetch"); } });
  for (const bbox of ["-150,20,-140,30", "-98,38,-98,39", "-98,38,-97,39&url=https://other.test", "NaN,38,-97,39"]) {
    assert.equal((await serve(extent(bbox))).status, 400);
  }
  assert.equal(calls, 0);
});

test("wind arrow samples use the model valid hour and point toward wind travel", async () => {
  let calls = 0;
  const serve = wind.createWindArrowService({ now: () => NOW, fetchUpstream: async (url) => {
    calls += 1;
    assert.equal(new URL(url).origin, "https://api.open-meteo.com");
    return Response.json(modelRows(url));
  } });
  const request = extent("-98.001,38.001,-97.901,38.101");
  const first = await serve(request);
  assert.equal(first.status, 200);
  const frame = await first.json();
  assert.equal(frame.samples.length, 16);
  assert.equal(frame.validTimeUtc, "2026-09-27T16:00:00.000Z");
  assert.equal(frame.samples[0].windFromDegrees, 270);
  assert.equal(frame.samples[0].windToDegrees, 90);
  const cached = await serve(request);
  assert.equal(cached.headers.get("X-KFM-Wind-Cache"), "HIT");
  assert.equal(cached.headers.get("X-KFM-Wind-Source"), "Open-Meteo NCEP GFS 10 m model");
  for (const header of ["X-KFM-Wind-Source", "X-KFM-Wind-Valid-Time", "X-KFM-Wind-Retrieved-At"]) {
    assert.equal(cached.headers.get(header), first.headers.get(header), `${header} must survive a cache hit`);
  }
  assert.equal(calls, 1);
  await serve(extent("-98.002,38.001,-97.902,38.101"));
  assert.equal(calls, 2, "nearby views must not reuse a different grid");
});

test("stale or incomplete wind model data draws no arrows and remains retryable", async () => {
  let calls = 0;
  const serve = wind.createWindArrowService({ now: () => NOW, fetchUpstream: async (url) => {
    calls += 1;
    const rows = modelRows(url, calls === 1 ? "2026-09-27T14:00" : "2026-09-27T16:00");
    return Response.json(rows);
  } });
  const request = extent("-98,38,-97,39");
  const failed = await serve(request);
  assert.equal(failed.status, 502);
  assert.equal(failed.headers.get("Cache-Control"), "no-store");
  assert.equal((await failed.json()).samples, undefined);
  assert.equal((await serve(request)).status, 200);
  assert.equal(calls, 2);
});

test("cached forecast is dropped as soon as its valid hour becomes stale", async () => {
  let clock = Date.parse("2026-09-27T16:34:00Z");
  let calls = 0;
  const serve = wind.createWindArrowService({ now: () => clock, fetchUpstream: async (url) => {
    calls += 1;
    return Response.json(modelRows(url, calls === 1 ? "2026-09-27T16:00" : "2026-09-27T17:00"));
  } });
  const request = extent("-98,38,-97,39");
  const first = await serve(request);
  assert.equal(first.status, 200);
  assert.equal(first.headers.get("Cache-Control"), "public, max-age=60");
  clock += 2 * 60_000;
  const second = await serve(request);
  assert.equal(second.status, 200);
  assert.equal((await second.json()).validTimeUtc, "2026-09-27T17:00:00.000Z");
  assert.equal(calls, 2);
});

test("shared Site rate limit recovers through the same validated GFS grid in the viewer", async () => {
  const calls = [];
  const fetcher = async (url, options) => {
    calls.push({ url, options });
    if (calls.length === 1) return Response.json({ code: "MODEL_HTTP_429" }, { status: 502 });
    return Response.json(modelRows(url));
  };
  const result = await windClient.loadWindFlowFrame("-98,38,-97,39", new AbortController().signal, fetcher, () => NOW);
  assert.equal(result.transport, "direct-provider");
  assert.equal(result.frame.samples.length, 16);
  assert.equal(result.frame.validTimeUtc, "2026-09-27T16:00:00.000Z");
  assert.equal(new URL(calls[1].url).origin, "https://api.open-meteo.com");
  assert.equal(calls[1].options.mode, "cors");
  assert.equal(calls.length, 2);

  let rejectedCalls = 0;
  await assert.rejects(() => windClient.loadWindFlowFrame("-98,38,-97,39", new AbortController().signal, async () => {
    rejectedCalls++;
    return Response.json({ code: "MODEL_INVALID_GRID" }, { status: 502 });
  }, () => NOW), /unavailable/i);
  assert.equal(rejectedCalls, 1, "bad model samples must not trigger a second request");
});

test("wind flow hover only reports a nearby model point and a travel direction", () => {
  const frame = { samples: [
    { latitude: 39, longitude: -98, speedMetersPerSecond: 5, windFromDegrees: 270, windToDegrees: 90 },
    { latitude: 39.2, longitude: -97.8, speedMetersPerSecond: 8, windFromDegrees: 0, windToDegrees: 180 },
  ] };
  const map = { project: ([longitude, latitude]) => ({ x: (longitude + 99) * 100, y: (latitude - 38) * 100 }) };
  assert.equal(windCanvas.nearestWindFlowSample(map, frame, 102, 99), frame.samples[0]);
  assert.equal(windCanvas.nearestWindFlowSample(map, frame, 119, 121), frame.samples[1]);
  assert.equal(windCanvas.nearestWindFlowSample(map, frame, 500, 500), null);
  assert.equal(windCanvas.nearestWindFlowSample(map, { samples: [{ ...frame.samples[0], speedMetersPerSecond: 0.2 }] }, 100, 100), null);
  assert.equal(windCanvas.windToCompass(frame.samples[0].windToDegrees), "E");
  assert.equal(windCanvas.windToCompass(frame.samples[1].windToDegrees), "S");
});

test("wind flow moves curved wisps without drawing arrowheads or stationary labels", () => {
  const previousWindow = globalThis.window;
  globalThis.window = { devicePixelRatio: 1 };
  try {
    const curves = [];
    const context = {
      setTransform() {}, clearRect() {}, save() {}, restore() {}, beginPath() {}, moveTo() {}, stroke() {},
      quadraticCurveTo(x, y) { curves.push([x, y]); },
      createLinearGradient() { return { addColorStop() {} }; },
      fill() { throw new Error("stationary glyph drawn"); },
      fillText() { throw new Error("stationary speed label drawn"); },
    };
    const canvas = { width: 0, height: 0, getContext: () => context };
    const map = {
      getCanvas: () => ({ clientWidth: 800, clientHeight: 600 }),
      getZoom: () => 7,
      project: ([longitude, latitude]) => ({ x: (longitude + 99) * 300, y: (latitude - 38) * 300 }),
    };
    const frame = { samples: [{ latitude: 39, longitude: -98, speedMetersPerSecond: 5, windFromDegrees: 270, windToDegrees: 90 }] };
    windCanvas.drawWindFlowCanvas(canvas, map, frame, 0, true);
    const first = curves.map((point) => [...point]);
    curves.length = 0;
    windCanvas.drawWindFlowCanvas(canvas, map, frame, 800, true);
    assert.equal(first.length, 7);
    assert.equal(curves.length, 7);
    assert.notDeepEqual(curves, first, "wind wisps should move with elapsed time");
  } finally {
    if (previousWindow === undefined) delete globalThis.window;
    else globalThis.window = previousWindow;
  }
});

test("terrain hover and profile readings remove display exaggeration", () => {
  const map = { getTerrain: () => ({ source: "terrain", exaggeration: 1.6 }), queryTerrainElevation: () => 480 };
  assert.equal(terrain.unexaggeratedTerrainElevation(map, [-97, 39]), 300);
  assert.equal(terrain.unexaggeratedTerrainElevation({ ...map, queryTerrainElevation: () => null }, [-97, 39]), null);
  assert.equal(terrain.unexaggeratedTerrainElevation({ ...map, getTerrain: () => null }, [-97, 39]), null);
  assert.equal(terrain.unexaggeratedTerrainElevation({ ...map, queryTerrainElevation: () => 0 }, [-97, 39]), null,
    "MapLibre's missing-tile zero must not become a Kansas height reading");
  assert.equal(terrain.unexaggeratedTerrainElevation({ ...map, queryTerrainElevation: () => 0 }, [-74, 40]), 0,
    "a sea-level height outside the Kansas focus area can be legitimate");
});

test("leaving 3D destroys DEM tile managers before the next terrain entry", () => {
  const sources = new Map();
  const layers = new Map();
  const operations = [];
  let currentTerrain = null;
  const map = {
    getSource: (id) => sources.get(id),
    addSource: (id, spec) => { sources.set(id, { ...spec }); operations.push(`add source ${id}`); },
    removeSource: (id) => {
      assert.equal(currentTerrain?.source, undefined, "the terrain mesh must be detached first");
      assert.ok(![...layers.values()].some((layer) => layer.source === id), "source layers must be removed first");
      sources.delete(id);
      operations.push(`remove source ${id}`);
    },
    getLayer: (id) => layers.get(id),
    addLayer: (layer) => { assert.ok(sources.has(layer.source)); layers.set(layer.id, layer); },
    removeLayer: (id) => { layers.delete(id); operations.push(`remove layer ${id}`); },
    getStyle: () => ({ layers: [...layers.values()] }),
    setTerrain: (value) => { currentTerrain = value; operations.push(value ? "attach terrain" : "detach terrain"); },
  };

  assert.equal(terrain.setTerrainPresentation(map, true, 1.6), "LOADING");
  assert.equal(terrain.setTerrainHeightOverlay(map, true), true);
  const firstDem = sources.get(terrain.TERRAIN_SOURCE_ID);
  assert.ok(firstDem);
  assert.equal(terrain.setTerrainPresentation(map, false, 1), "OFF");
  assert.equal(currentTerrain, null);
  assert.equal(sources.size, 0);
  assert.equal(layers.size, 0);
  assert.ok(operations.indexOf("detach terrain") < operations.indexOf(`remove source ${terrain.TERRAIN_SOURCE_ID}`));

  assert.equal(terrain.setTerrainPresentation(map, true, 1.6), "LOADING");
  assert.notEqual(sources.get(terrain.TERRAIN_SOURCE_ID), firstDem, "re-entry gets a fresh DEM source");
  assert.equal(terrain.setTerrainHeightOverlay(map, true), true);
  assert.equal(layers.has(terrain.TERRAIN_COLOR_RELIEF_LAYER_ID), true);
});

test("switching terrain providers replaces both DEM tile managers and verifies the attached source", () => {
  const sources = new Map(), layers = new Map(), operations = [];
  let currentTerrain = null;
  const map = {
    getSource: id => sources.get(id),
    addSource: (id, spec) => { sources.set(id, spec); operations.push(`add ${id}`); },
    removeSource: id => { assert.equal(currentTerrain, null); sources.delete(id); operations.push(`remove ${id}`); },
    getLayer: id => layers.get(id),
    addLayer: layer => layers.set(layer.id, layer),
    removeLayer: id => layers.delete(id),
    setLayoutProperty: () => {},
    getStyle: () => ({ sources: Object.fromEntries(sources), layers: [...layers.values()] }),
    setTerrain: value => { currentTerrain = value; },
  };
  const mapzen = terrainSources.terrainSourceFor("mapzen");
  const usgs = terrainSources.terrainSourceFor("usgs-3dep");
  assert.equal(terrain.setTerrainPresentation(map, true, 1.6, mapzen), "LOADING");
  const first = sources.get(terrain.TERRAIN_SOURCE_ID);
  assert.equal(terrain.terrainPresentationSourceMatches(map, mapzen), true);
  assert.equal(terrain.terrainPresentationSourceMatches(map, usgs), false);
  assert.equal(terrain.setTerrainPresentation(map, true, 1.6, usgs), "LOADING");
  assert.notEqual(sources.get(terrain.TERRAIN_SOURCE_ID), first);
  assert.equal(sources.get(terrain.TERRAIN_SOURCE_ID).tiles[0], usgs.tileTemplate);
  assert.equal(sources.get(terrain.TERRAIN_HILLSHADE_SOURCE_ID).tiles[0], usgs.tileTemplate);
  assert.equal(terrain.terrainPresentationSourceMatches(map, usgs), true);
  assert.ok(operations.indexOf(`remove ${terrain.TERRAIN_SOURCE_ID}`) < operations.lastIndexOf(`add ${terrain.TERRAIN_SOURCE_ID}`));
});

test("a failed DEM stays unavailable until a new source starts loading", () => {
  assert.equal(terrain.terrainSourceLoadState("LOADING", false, true), "ERROR");
  assert.equal(terrain.terrainSourceLoadState("LOADING", true, true), "ERROR");
  assert.equal(terrain.terrainSourceLoadState("LOADING", false, false), "LOADING");
  assert.equal(terrain.terrainSourceLoadState("LOADING", true, false), "READY");
  assert.equal(terrain.terrainSourceLoadState("OFF", true, true), "OFF");
});

test("terrain tile errors stay in terrain recovery instead of switching the basemap", () => {
  for (const sourceId of [terrain.TERRAIN_SOURCE_ID, terrain.TERRAIN_HILLSHADE_SOURCE_ID, terrain.TERRAIN_COLOR_SOURCE_ID]) {
    assert.equal(terrain.shouldFallbackStandardBasemap(sourceId, false, false), false);
  }
  assert.equal(terrain.shouldFallbackStandardBasemap("external-official", false, true), false);
  assert.equal(terrain.shouldFallbackStandardBasemap("kfm-local", true, false), false);
  assert.equal(terrain.shouldFallbackStandardBasemap("openmaptiles", false, false), true);
  assert.equal(terrain.shouldFallbackStandardBasemap("ne2_shaded", false, false), true);
  assert.equal(terrain.shouldFallbackStandardBasemap("standard-vector-tiles", false, false), false);
  assert.equal(terrain.shouldFallbackStandardBasemap(undefined, false, false), false);
});
