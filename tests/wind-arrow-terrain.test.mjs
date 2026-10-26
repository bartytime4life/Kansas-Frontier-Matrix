import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test, { mock } from "node:test";
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

test("a missing model direction is unavailable rather than an invented wind bearing", async () => {
  const serve = wind.createWindArrowService({ now: () => NOW, fetchUpstream: async url => {
    const rows = modelRows(url);
    rows[0].hourly.wind_direction_10m[0] = null;
    return Response.json(rows);
  } });
  const response = await serve(extent("-98,38,-97,39"));
  assert.equal(response.status, 502);
  const body = await response.json();
  assert.equal(body.code, "MODEL_INVALID_GRID");
  assert.equal(body.samples, undefined);
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

test("still direction arrows use meteorological model bearings and the projected map camera", () => {
  for (const [from, bearing, expectedX, expectedY] of [[270, 0, 1, 0], [0, 0, 0, 1], [270, 90, 0, -1]]) {
    const map = cameraMap({ bearing });
    const glyphs = windCanvas.windDirectionGlyphs(map, gridFrame(from));
    assert.ok(glyphs.length > 0);
    for (const glyph of glyphs) {
      assert.ok(Math.abs(glyph.dx - expectedX) < 0.02 && Math.abs(glyph.dy - expectedY) < 0.02);
      assert.ok(gridFrame(from).samples.some(sample => {
        const point = map.project([sample.longitude, sample.latitude]);
        return point.x === glyph.x && point.y === glyph.y;
      }), "every arrow is anchored at a model sample, not a random particle");
    }
  }
  assert.deepEqual(windCanvas.windDirectionGlyphs(cameraMap(), gridFrame(270, 0.2)), []);
  assert.deepEqual(windCanvas.windDirectionGlyphs(cameraMap(), { samples: [] }), []);
  const missing = gridFrame(270).samples.map(sample => ({ ...sample, windFromDegrees: NaN }));
  assert.deepEqual(windCanvas.windDirectionGlyphs(cameraMap(), { samples: missing }), []);
  const globe = { ...cameraMap({ center: { lng: 82, lat: 39 } }), getProjection: () => ({ type: "globe" }) };
  assert.deepEqual(windCanvas.windDirectionGlyphs(globe, gridFrame(270)), []);
});

const findWindEffect = async () => {
  const source = await readFile("app/page.tsx", "utf8");
  const tree = ts.createSourceFile("page.tsx", source, ts.ScriptTarget.Latest, true, ts.ScriptKind.TSX);
  let effect;
  const visit = node => {
    if (ts.isCallExpression(node) && node.expression.getText(tree) === "useEffect"
      && node.arguments[0]?.getText(tree).includes("const canvas = windArrowCanvasRef.current;")) effect = node;
    ts.forEachChild(node, visit);
  };
  visit(tree);
  assert.ok(effect);
  return { tree, effect };
};

test("unrelated source selections do not restart the wind effect", async () => {
  const { tree, effect } = await findWindEffect();
  const dependencies = effect.arguments[1].elements.map(node => node.getText(tree));
  assert.ok(dependencies.includes("windLayerSelected"));
  assert.ok(!dependencies.includes("officialVisibility"), "another source's visibility must not clear/reload wind");
});

test("wind reloads ignore late success and failure from superseded camera requests", async () => {
  const { tree, effect } = await findWindEffect();
  const requests = [], events = new Map(), pendingTimers = [];
  const states = { frame: null, state: null };
  const canvas = { width: 800, height: 600, getContext: () => ({ clearRect() {} }) };
  const map = {
    getBounds: () => ({ getWest: () => -99, getEast: () => -97, getSouth: () => 38, getNorth: () => 39 }),
    getCenter: () => ({ lng: -98, lat: 38.5 }),
    getCanvas: () => ({ addEventListener() {}, removeEventListener() {} }),
    on: (name, callback) => events.set(name, callback), off() {},
  };
  const values = {
    mapRef: { current: map }, windArrowCanvasRef: { current: canvas }, buildYearCurrent: true,
    windLayerSelected: true, officialVisibility: { "nws-forecast-wind": true }, temporalQuery: { frame: 2026 }, OFFICIAL_CONTEXT_PRESENT_FRAME: 2026,
    styleReady: true, dynamicEffects: false, reducedMotion: true,
    document: { hidden: false, addEventListener() {}, removeEventListener() {} },
    window: { setTimeout: callback => { pendingTimers.push(callback); return pendingTimers.length; }, clearTimeout() {},
      setInterval: () => 1, clearInterval() {}, cancelAnimationFrame() {} },
    performance: { now: () => 0 }, AbortController, DOMException,
    setWindArrowState: value => { states.state = value; }, setWindArrowFrame: value => { states.frame = value; },
    setWindArrowDirect() {}, setWindArrowHover() {},
    loadWindFlowFrame: (_bbox, signal) => new Promise((resolve, reject) => requests.push({ resolve, reject, signal })),
    drawWindFlowCanvas() {}, resetWindFlowCanvas() {}, windFlowToneForBasemap: () => "light",
    basemapRef: { current: "standard" },
  };
  const code = ts.transpileModule(`const effect = ${effect.arguments[0].getText(tree)};`, {
    compilerOptions: { target: ts.ScriptTarget.ES2022 },
  }).outputText;
  const cleanup = new Function(...Object.keys(values), `${code}; return effect();`)(...Object.values(values));
  const move = () => { events.get("moveend")(); pendingTimers.pop()(); };
  const settle = async () => { await Promise.resolve(); await Promise.resolve(); };
  move();
  assert.equal(requests[0].signal.aborted, true);
  const current = { samples: [], validTimeUtc: "new" };
  requests[1].resolve({ frame: current, transport: "site" }); await settle();
  requests[0].resolve({ frame: { samples: [], validTimeUtc: "old" }, transport: "site" }); await settle();
  assert.equal(states.frame, current);
  assert.equal(states.state, "READY");
  move(); move();
  requests[3].resolve({ frame: current, transport: "site" }); await settle();
  requests[2].reject(new Error("late failure")); await settle();
  assert.equal(states.frame, current);
  assert.equal(states.state, "READY");
  cleanup();
});

const withWindow = (run, now = () => 0) => {
  const previousWindow = globalThis.window;
  // Geometry must not depend on CI scheduling: the renderer deliberately
  // reduces particle density when measured frame CPU time exceeds its budget.
  // Animation still advances through each draw's explicit elapsedMs argument.
  const clock = mock.method(performance, "now", now);
  globalThis.window = { devicePixelRatio: 1 };
  try { return run(); } finally {
    clock.mock.restore();
    if (previousWindow === undefined) delete globalThis.window;
    else globalThis.window = previousWindow;
  }
};
// Records every stroked polyline as head→tail segments; filled glyphs or text fail.
const recordingCanvas = () => {
  const strokes = [];
  let path = [], pen = null;
  const context = {
    setTransform() {}, clearRect() {}, beginPath() { path = []; pen = null; },
    moveTo(x, y) { pen = [x, y]; }, lineTo(x, y) { path.push([pen[0], pen[1], x, y]); pen = [x, y]; },
    stroke() { strokes.push({ lineWidth: this.lineWidth, style: this.strokeStyle, segments: path }); },
    fill() { throw new Error("stationary glyph drawn"); },
    fillText() { throw new Error("stationary speed label drawn"); },
  };
  return { strokes, canvas: { width: 0, height: 0, getContext: () => context } };
};
const mercatorY = (latitude) => (180 - (180 / Math.PI) * Math.log(Math.tan(Math.PI / 4 + latitude * Math.PI / 360))) / 360;
// A flat Mercator camera: rotate by bearing, then a perspective tilt. Exact
// ground→screen projective map, as MapLibre's pitched Mercator view is.
const cameraMap = ({ zoom = 7, bearing = 0, pitch = 0, center = { lng: -98, lat: 38.5 } } = {}) => {
  const worldSize = 512 * 2 ** zoom, cx = (center.lng + 180) / 360, cy = mercatorY(center.lat);
  const b = bearing * Math.PI / 180, tilt = Math.tan(pitch * Math.PI / 180) / 900;
  return {
    getCanvas: () => ({ clientWidth: 800, clientHeight: 600 }), getZoom: () => zoom, getCenter: () => center,
    getBearing: () => bearing, getPitch: () => pitch,
    project: ([longitude, latitude]) => {
      const X = ((longitude + 180) / 360 - cx) * worldSize, Y = (mercatorY(latitude) - cy) * worldSize;
      const rx = X * Math.cos(b) + Y * Math.sin(b), ry = -X * Math.sin(b) + Y * Math.cos(b);
      const w = 1 - ry * tilt; // farther (screen-up) ground shrinks
      return { x: 400 + rx / w, y: 300 + ry / w };
    },
  };
};
const gridFrame = (windFromDegrees, speedMetersPerSecond = 6) => ({ samples: Array.from({ length: 16 }, (_, index) => ({
  latitude: 38.1 + Math.floor(index / 4) * 0.25, longitude: -98.45 + (index % 4) * 0.3,
  speedMetersPerSecond, windFromDegrees, windToDegrees: (windFromDegrees + 180) % 360,
})) });
const segmentsOf = (strokes) => strokes.flatMap((stroke) => stroke.segments);
const meanVector = (segments) => {
  let x = 0, y = 0;
  // Segments run head → tail, so travel is the reverse of each segment.
  for (const [x0, y0, x1, y1] of segments) { x += x0 - x1; y += y0 - y1; }
  const length = Math.hypot(x, y);
  return [x / length, y / length];
};

test("wind flow draws moving ground streamlines toward where the wind blows, without arrowheads or labels", () => withWindow(() => {
  const { strokes, canvas } = recordingCanvas();
  const map = cameraMap();
  const westerly = gridFrame(270);
  windCanvas.drawWindFlowCanvas(canvas, map, westerly, 0, true);
  for (let time = 33; time <= 1000; time += 33) { strokes.length = 0; windCanvas.drawWindFlowCanvas(canvas, map, westerly, time, true); }
  const stats = windCanvas.windFlowCanvasStats(canvas);
  assert.equal(stats.mode, "homography", "a flat Mercator view projects through the exact homography");
  assert.ok(stats.particles > 12, `${stats.particles} streamlines`);
  const first = segmentsOf(strokes).map((segment) => [...segment]);
  const [east, south] = meanVector(first);
  assert.ok(east > 0.99 && Math.abs(south) < 0.05, `wind from the west flows east on screen (${east}, ${south})`);
  strokes.length = 0;
  windCanvas.drawWindFlowCanvas(canvas, map, westerly, 1100, true);
  assert.notDeepEqual(segmentsOf(strokes).slice(0, 20), first.slice(0, 20), "streamlines advance with elapsed time");

  const northerly = gridFrame(0);
  const { strokes: south2, canvas: canvas2 } = recordingCanvas();
  for (let time = 0; time <= 900; time += 33) { south2.length = 0; windCanvas.drawWindFlowCanvas(canvas2, map, northerly, time, true); }
  const [, down] = meanVector(segmentsOf(south2));
  assert.ok(down > 0.99, "wind from the north flows south (screen down at bearing 0)");
}));

test("wind density reduces after an expensive frame and recovers when CPU headroom returns", () => {
  let cpuMs = 0, reads = 0;
  withWindow(() => {
    const { canvas } = recordingCanvas(), map = cameraMap(), frame = gridFrame(270);
    let elapsed = 0;
    for (; elapsed <= 1000; elapsed += 33) windCanvas.drawWindFlowCanvas(canvas, map, frame, elapsed, true);
    const normal = windCanvas.windFlowCanvasStats(canvas);
    assert.equal(normal.mode, "homography");
    assert.ok(normal.particles > 12);
    cpuMs = 8;
    for (let i = 0; i < 12; i++, elapsed += 33) windCanvas.drawWindFlowCanvas(canvas, map, frame, elapsed, true);
    const limited = windCanvas.windFlowCanvasStats(canvas);
    assert.equal(limited.cpuMs, 8);
    assert.ok(limited.active < normal.active, "the real frame-budget control lowers density");
    cpuMs = 0;
    for (let i = 0; i < 50; i++, elapsed += 33) windCanvas.drawWindFlowCanvas(canvas, map, frame, elapsed, true);
    assert.equal(windCanvas.windFlowCanvasStats(canvas).active, normal.active, "density recovers without changing the data or animation time");
  }, () => reads++ % 2 === 0 ? 0 : cpuMs);
});

test("streamlines rotate with bearing and foreshorten with pitch because they live on the ground", () => withWindow(() => {
  const run = (options) => {
    const { strokes, canvas } = recordingCanvas();
    const map = cameraMap(options);
    for (let time = 0; time <= 1200; time += 33) { strokes.length = 0; windCanvas.drawWindFlowCanvas(canvas, map, gridFrame(270), time, true); }
    return segmentsOf(strokes);
  };
  const [, rotated] = meanVector(run({ bearing: 90 }));
  assert.ok(Math.abs(rotated) > 0.99, "a 90° bearing turns eastward travel to the screen vertical");
  const pitched = run({ pitch: 60 });
  const lengthIn = (band) => {
    const lengths = pitched.filter(([, y0]) => band(y0)).map(([x0, y0, x1, y1]) => Math.hypot(x1 - x0, y1 - y0));
    return lengths.reduce((sum, value) => sum + value, 0) / lengths.length;
  };
  const far = lengthIn((y) => y < 250), near = lengthIn((y) => y > 400);
  assert.ok(far < near * 0.8, `far ground segments are foreshortened (${far.toFixed(2)} vs ${near.toFixed(2)} px)`);
}));

test("calm forecasts draw nothing and a still frame does not move with time", () => withWindow(() => {
  const calm = recordingCanvas();
  windCanvas.drawWindFlowCanvas(calm.canvas, cameraMap(), gridFrame(270, 0.2), 0, true);
  windCanvas.drawWindFlowCanvas(calm.canvas, cameraMap(), gridFrame(270, 0.2), 500, true);
  assert.equal(segmentsOf(calm.strokes).length, 0);
  windCanvas.drawWindFlowCanvas(calm.canvas, cameraMap(), gridFrame(270, 0.2), 1000, false);
  assert.equal(segmentsOf(calm.strokes).length, 0, "calm has no direction arrow with motion off either");
  const still = recordingCanvas();
  const map = cameraMap({ pitch: 30 });
  const frame = gridFrame(200);
  windCanvas.drawWindFlowCanvas(still.canvas, map, frame, 0, false);
  const first = segmentsOf(still.strokes);
  const arrows = windCanvas.windDirectionGlyphs(map, frame);
  assert.ok(arrows.length > 0);
  assert.ok(still.strokes.slice(-arrows.length * 2).every(stroke => stroke.segments.length === 3), "still rendering includes arrow shafts and two wings at model points");
  still.strokes.length = 0;
  windCanvas.drawWindFlowCanvas(still.canvas, map, frame, 5000, false);
  assert.ok(first.length > 0);
  assert.deepEqual(segmentsOf(still.strokes), first, "motion off (or reduced motion) holds one still frame");
}));

test("wind streamlines and hover shrink with Kansas on the globe and stop behind it", () => withWindow(() => {
  const { strokes, canvas } = recordingCanvas();
  let zoom = 0.6, center = { lng: -98, lat: 39 };
  const map = {
    getCanvas: () => ({ clientWidth: 800, clientHeight: 600 }), getZoom: () => zoom,
    getProjection: () => ({ type: "globe" }), getCenter: () => center,
    project: ([longitude, latitude]) => ({ x: (longitude + 99) * 100, y: (latitude - 38) * 100 }),
  };
  const frame = gridFrame(270, 5);
  windCanvas.drawWindFlowCanvas(canvas, map, frame, 0, true);
  assert.deepEqual(strokes, []);
  assert.equal(windCanvas.nearestWindFlowSample(map, frame, 100, 100), null);
  zoom = 5.45;
  for (let time = 0; time <= 900; time += 33) { strokes.length = 0; windCanvas.drawWindFlowCanvas(canvas, map, frame, time, true); }
  assert.ok(strokes.length > 0);
  assert.equal(windCanvas.windFlowCanvasStats(canvas).mode, "per-point", "globe points are projected one by one");
  const flat = recordingCanvas();
  for (let time = 0; time <= 900; time += 33) { flat.strokes.length = 0; windCanvas.drawWindFlowCanvas(flat.canvas, cameraMap(), frame, time, true); }
  const narrowest = (list) => Math.min(...list.map((stroke) => stroke.lineWidth));
  zoom = 3.5;
  for (let time = 1000; time <= 1900; time += 33) { strokes.length = 0; windCanvas.drawWindFlowCanvas(canvas, map, frame, time, true); }
  assert.ok(strokes.length > 0 && narrowest(strokes) < narrowest(flat.strokes) * 0.7, "a zoomed-out globe keeps lines Kansas-sized");
  zoom = 5.45;
  assert.ok(windCanvas.nearestWindFlowSample(map, frame, 100, 100));
  center = { lng: 82, lat: 39 };
  strokes.length = 0;
  windCanvas.drawWindFlowCanvas(canvas, map, frame, 2000, true);
  assert.deepEqual(strokes, []);
  assert.equal(windCanvas.nearestWindFlowSample(map, frame, 100, 100), null);
}));

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

test("one hillshade at most: none over the photograph, and none doubling a category basemap's own", () => {
  const sources = new Map(), layers = new Map();
  const map = {
    getSource: (id) => sources.get(id), addSource: (id, spec) => sources.set(id, { ...spec }), removeSource: (id) => sources.delete(id),
    getLayer: (id) => layers.get(id), addLayer: (layer) => layers.set(layer.id, structuredClone(layer)), removeLayer: (id) => layers.delete(id),
    setLayoutProperty: (id, key, value) => { layers.get(id).layout[key] = value; },
    getStyle: () => ({ layers: [...layers.values()] }), setTerrain() {},
  };
  layers.set(terrain.PHOTOREAL_IMAGERY_LAYER_ID, { id: terrain.PHOTOREAL_IMAGERY_LAYER_ID, type: "raster", source: "esri-imagery", layout: {} });
  assert.equal(terrain.setTerrainPresentation(map, true, 1), "LOADING");
  assert.equal(layers.get(terrain.TERRAIN_HILLSHADE_LAYER_ID).layout.visibility, "none", "the photograph carries its own light");
  layers.delete(terrain.PHOTOREAL_IMAGERY_LAYER_ID);
  terrain.setTerrainPresentation(map, true, 2.5);
  assert.equal(layers.get(terrain.TERRAIN_HILLSHADE_LAYER_ID).layout.visibility, "visible", "relief colours shade the terrain again");
  layers.set("basemap-relief-hillshade", { id: "basemap-relief-hillshade", type: "hillshade", source: "basemap-relief-dem", layout: {} });
  terrain.setTerrainPresentation(map, true, 2.5);
  assert.equal(layers.get(terrain.TERRAIN_HILLSHADE_LAYER_ID).layout.visibility, "none", "a category basemap's own sun-lit hillshade is not doubled in 3D");
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
  // Before the standard style document loads, an unidentified error is the style
  // itself (JSON, sprite or glyphs), so the local style may replace it once.
  assert.equal(terrain.shouldFallbackStandardBasemap(undefined, false, false, false), true);
  assert.equal(terrain.shouldFallbackStandardBasemap(undefined, false, false, true), false);
  assert.equal(terrain.shouldFallbackStandardBasemap("kfm-terrain-dem", false, false, false), false);
  assert.equal(terrain.shouldFallbackStandardBasemap(undefined, true, false, false), false);
});
