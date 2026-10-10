import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const read = (path) => readFile(new URL(`../${path}`, import.meta.url), "utf8");
const toUrl = (javascript) => `data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`;
const transpile = (source) => ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;

async function loadSync() {
  const motionUrl = toUrl(transpile(await read("app/water-flow-motion.ts")));
  const layerSource = (await read("app/water-flow-layer.ts")).replace('from "./water-flow-motion";', `from "${motionUrl}";`);
  const layerUrl = toUrl(transpile(layerSource));
  const sceneStub = toUrl(`export const sceneEffectsFor = (map) => map.fx;
export const effectiveSceneLight = (_map, preset) => ({ preset, azimuth: 0, altitude: 30, source: "manual" });`);
  const performanceStub = toUrl("export const uploadedGeoJSON = (source) => source?.data;");
  let source = await read("app/water-flow-sync.ts");
  for (const [before, after] of [
    ['from "./map-performance";', `from "${performanceStub}";`],
    ['from "./scene-effects";', `from "${sceneStub}";`],
    ['from "./water-flow-layer";', `from "${layerUrl}";`],
    ['from "./water-flow-motion";', `from "${motionUrl}";`],
  ]) {
    assert.ok(source.includes(before), `water-flow-sync still imports ${before}`);
    source = source.replace(before, after);
  }
  return import(toUrl(transpile(source)));
}

globalThis.requestAnimationFrame ??= (callback) => setTimeout(() => callback(performance.now()), 0);
globalThis.cancelAnimationFrame ??= (handle) => clearTimeout(handle);
const settle = () => new Promise((resolve) => setTimeout(resolve, 5));

const GAUGE_SOURCE = "external-usgs-streamflow";
const GAUGE_LAYER = "external-usgs-streamflow-points";

function fakeMap({ zoom = 11, center = [-97.2, 38.1], gaugeVisible = true, gauges = [] } = {}) {
  const layers = [{ id: "background", type: "background" }, { id: "place-labels", type: "symbol" }, { id: GAUGE_LAYER, type: "circle" }];
  const layout = new Map([[`${GAUGE_LAYER}:visibility`, gaugeVisible ? "visible" : "none"]]);
  const handlers = new Map();
  const map = {
    fx: { waterFlow: true }, zoom, center, layers, layout, repaints: 0,
    sources: { [GAUGE_SOURCE]: { data: { type: "FeatureCollection", features: gauges } } },
    getZoom: () => map.zoom,
    getCenter: () => ({ lng: map.center[0], lat: map.center[1] }),
    getBounds: () => ({ getWest: () => map.center[0] - 0.3, getEast: () => map.center[0] + 0.3, getSouth: () => map.center[1] - 0.2, getNorth: () => map.center[1] + 0.2 }),
    getStyle: () => ({ layers }),
    getLayer: (id) => layers.find((layer) => layer.id === id),
    addLayer(layer, beforeId) {
      const index = beforeId ? layers.findIndex((candidate) => candidate.id === beforeId) : -1;
      layers.splice(index < 0 ? layers.length : index, 0, layer);
    },
    removeLayer(id) { layers.splice(layers.findIndex((layer) => layer.id === id), 1); },
    getLayoutProperty: (id, key) => layout.get(`${id}:${key}`),
    setLayoutProperty: (id, key, value) => layout.set(`${id}:${key}`, value),
    getSource: (id) => map.sources[id],
    on: (event, handler) => handlers.set(event, [...(handlers.get(event) ?? []), handler]),
    off: (event, handler) => handlers.set(event, (handlers.get(event) ?? []).filter((item) => item !== handler)),
    fire: (event, payload = {}) => (handlers.get(event) ?? []).forEach((handler) => handler(payload)),
    triggerRepaint() { map.repaints += 1; },
  };
  return map;
}

const OPTIONS = { light: "night", azimuth: 210, efficient: false, gaugeSourceId: GAUGE_SOURCE, gaugeLayerId: GAUGE_LAYER };
const payload = (key, reaches) => ({
  format: "kfm-3dhp-flowlines-v1", cell: key.split(",").map(Number), state: reaches.length ? "ready" : "empty", truncated: false, reaches,
  source: "https://3dhp.nationalmap.gov/arcgis/rest/services/usgs_3dhp_all/MapServer/50/query", retrievedAt: "2026-10-10T00:00:00Z", evidenceRole: "EXTERNAL_CONTEXT_ONLY", limitation: "fixture",
});

// Control display frames independently of promise settlement: several provider
// responses may arrive before the browser can paint once.
function displayFrames(t) {
  let next = 1;
  const pending = new Map();
  t.mock.method(globalThis, "requestAnimationFrame", (callback) => { const id = next++; pending.set(id, callback); return id; });
  t.mock.method(globalThis, "cancelAnimationFrame", (id) => pending.delete(id));
  return {
    pending,
    flush() { const callbacks = [...pending.values()]; pending.clear(); callbacks.forEach((callback) => callback(performance.now())); },
  };
}
const drain = () => new Promise((resolve) => setImmediate(resolve));
const deferred = () => { let resolve, reject; const promise = new Promise((yes, no) => { resolve = yes; reject = no; }); return { promise, resolve, reject }; };

test("cell and gauge bursts build once per display frame with byte-identical geometry", async (t) => {
  const frames = displayFrames(t);
  const flow = await loadSync();
  const motion = await import(toUrl(transpile(await read("app/water-flow-motion.ts"))));
  const requests = [];
  flow.setWaterFlowFetcher((key) => { const request = { key, ...deferred() }; requests.push(request); return request.promise; });
  const gauges = [
    { type: "Feature", geometry: { type: "Point", coordinates: [-97.2, 38.1] }, properties: { value: 310, readingState: "measured", trend: "rising", visualMagnitude: 2.5 } },
    { type: "Feature", geometry: { type: "Point", coordinates: [-97.19, 38.1] }, properties: { value: 0, readingState: "zero" } },
  ];
  const map = fakeMap({ gauges });
  flow.syncWaterFlow(map, OPTIONS);
  assert.equal(requests.length, 9);
  const layer = map.getLayer(flow.WATER_FLOW_LAYER_ID);
  const original = layer.setGeometry;
  let builds = 0, submittedSegments = 0, finalGeometry;
  layer.setGeometry = (geometry) => { builds++; submittedSegments += geometry?.count ?? 0; finalGeometry = geometry; original(geometry); };
  const allReaches = requests.map(({ key }, cell) => Array.from({ length: 200 }, (_, i) => fixtureReach(`R${cell}X${i}`,
    Array.from({ length: 16 }, (_, vertex) => [-97.2 + cell * 0.01 + vertex * 0.0001, 38.1 + i * 0.0001]))));
  const started = performance.now();
  for (let i = 0; i < requests.length; i++) {
    requests[i].resolve(payload(requests[i].key, allReaches[i]));
    await drain();
    map.fire("sourcedata", { sourceId: GAUGE_SOURCE });
  }
  frames.flush();
  const elapsed = performance.now() - started;
  t.diagnostic(JSON.stringify({ case: "synthetic-nine-cell-burst", cells: 9, reaches: 1800, builds, submittedSegments, elapsedMs: Number(elapsed.toFixed(2)) }));
  const expected = motion.buildFlowGeometry(allReaches.flat(), gauges.map((gauge) => motion.gaugeCue(gauge.properties, gauge.geometry.coordinates)));
  assert.deepEqual(finalGeometry, expected, "positions, direction, gauge styling and vertex slots are identical");
  assert.equal(flow.waterFlowStatus(map).reaches, 1800);
  assert.equal(builds, 1, "provider and gauge callbacks share one pending display update");
  map.fire("moveend");
  frames.flush();
  assert.equal(builds, 1, "unchanged cached cells do not rebuild");
});

test("a partial first cell appears on the next frame without waiting for slow cells", async (t) => {
  const frames = displayFrames(t);
  const flow = await loadSync();
  const requests = [];
  flow.setWaterFlowFetcher((key) => { const request = { key, ...deferred() }; requests.push(request); return request.promise; });
  const map = fakeMap();
  flow.syncWaterFlow(map, OPTIONS);
  const first = requests[0];
  first.resolve({ ...payload(first.key, [fixtureReach("FIRST", [[-97.2, 38.1], [-97.19, 38.1]])]), truncated: true });
  await drain(); frames.flush();
  assert.equal(flow.waterFlowStatus(map).state, "loading");
  assert.equal(flow.waterFlowStatus(map).reaches, 1);
  for (const request of requests.slice(1)) request.reject(new Error("provider unavailable"));
  await drain(); frames.flush();
  assert.equal(flow.waterFlowStatus(map).state, "partial");
  assert.equal(flow.waterFlowStatus(map).failedCells, 8);
  assert.equal(flow.waterFlowStatus(map).truncatedCells, 1);
  assert.ok(map.getLayer(flow.WATER_FLOW_LAYER_ID).segmentCount > 0);
});

for (const outcome of ["resolve", "reject"]) test(`cancelled ${outcome} cannot replace a new request for the same cell`, async (t) => {
  const frames = displayFrames(t);
  const flow = await loadSync();
  const requests = [];
  flow.setWaterFlowFetcher((key, signal) => { const request = { key, signal, ...deferred() }; requests.push(request); return request.promise; });
  const map = fakeMap();
  flow.syncWaterFlow(map, OPTIONS);
  const old = requests.splice(0);
  map.fx = { waterFlow: false }; flow.syncWaterFlow(map, OPTIONS);
  assert.ok(old.every((request) => request.signal.aborted));
  map.fx = { waterFlow: true }; flow.syncWaterFlow(map, OPTIONS);
  for (const request of old) request[outcome](outcome === "resolve" ? payload(request.key, [fixtureReach("OLD", [[-97.2, 38.1], [-97.19, 38.1]])]) : new Error("late failure"));
  await drain(); frames.flush();
  assert.equal(flow.waterFlowStatus(map).state, "loading");
  assert.equal(flow.waterFlowStatus(map).reaches, 0);
  for (const request of requests) request.resolve(payload(request.key, [fixtureReach("NEW", [[-97.2, 38.1], [-97.19, 38.1], [-97.18, 38.1]])]));
  await drain(); frames.flush();
  assert.equal(flow.waterFlowStatus(map).state, "ready");
  assert.equal(map.getLayer(flow.WATER_FLOW_LAYER_ID).segmentCount, 2);
});

test("map removal cancels pending geometry and network work", async (t) => {
  const frames = displayFrames(t);
  const flow = await loadSync();
  const requests = [];
  flow.setWaterFlowFetcher((key, signal) => { const request = { key, signal, ...deferred() }; requests.push(request); return request.promise; });
  const map = fakeMap();
  flow.syncWaterFlow(map, OPTIONS);
  requests[0].resolve(payload(requests[0].key, [fixtureReach("FIRST", [[-97.2, 38.1], [-97.19, 38.1]])]));
  await drain();
  map.fire("sourcedata", { sourceId: GAUGE_SOURCE });
  assert.equal(frames.pending.size, 1);
  map.fire("remove");
  assert.equal(frames.pending.size, 0);
  assert.ok(requests.slice(1).every((request) => request.signal.aborted));
  for (const request of requests.slice(1)) request.resolve(payload(request.key, []));
  await drain();
  assert.equal(frames.pending.size, 0, "late promises cannot schedule work on a removed map");
  assert.equal(flow.waterFlowStatus(map).state, "off");
});
const fixtureReach = (id, coordinates) => ({ id, sequence: 4, downstream: null, levelpath: 3, name: "Fixture Creek", featureType: 1, coordinates });

test("flowing water stays off, waits for river zoom, and draws provider reaches above the basemap", async () => {
  const flow = await loadSync();
  const requested = [];
  flow.setWaterFlowFetcher(async (key) => {
    requested.push(key);
    return payload(key, key === "-97.25,38.00" ? [fixtureReach("R1", [[-97.24, 38.1], [-97.2, 38.1], [-97.15, 38.12]])] : []);
  });

  const off = fakeMap();
  off.fx = { waterFlow: false };
  assert.equal(flow.syncWaterFlow(off, OPTIONS), true);
  assert.equal(off.getLayer(flow.WATER_FLOW_LAYER_ID), undefined);
  assert.equal(flow.waterFlowStatus(off).state, "off");

  const far = fakeMap({ zoom: 8 });
  flow.syncWaterFlow(far, OPTIONS);
  assert.equal(far.getLayoutProperty(flow.WATER_FLOW_LAYER_ID, "visibility"), "none");
  assert.equal(flow.waterFlowStatus(far).state, "zoom");
  assert.equal(requested.length, 0, "no flowline request below river zoom");

  const statuses = [];
  const unsubscribe = flow.subscribeWaterFlowStatus((status) => statuses.push(status.state));
  const gauge = { type: "Feature", geometry: { type: "Point", coordinates: [-97.2, 38.1005] }, properties: { value: 310, readingState: "measured", trend: "rising", visualMagnitude: 2.5 } };
  const map = fakeMap({ gauges: [gauge] });
  flow.syncWaterFlow(map, OPTIONS);
  const ids = map.layers.map((layer) => layer.id);
  assert.ok(ids.indexOf(flow.WATER_FLOW_LAYER_ID) < ids.indexOf("place-labels"), "below labels and data overlays");
  assert.ok(ids.indexOf(flow.WATER_FLOW_LAYER_ID) > ids.indexOf("background"), "above the basemap");
  assert.equal(map.getLayoutProperty(flow.WATER_FLOW_LAYER_ID, "visibility"), "visible");
  assert.ok(requested.length > 0 && requested.length <= 9);
  assert.equal(flow.waterFlowStatus(map).state, "loading");
  await settle();
  const status = flow.waterFlowStatus(map);
  assert.equal(status.state, "ready");
  assert.equal(status.reaches, 1);
  assert.equal(status.gaugedReaches, 1, "the gauge lights its own reach");
  assert.equal(flow.waterFlowIsAnimating(map), true);
  assert.ok(statuses.includes("loading") && statuses.at(-1) === "ready");
  assert.match(flow.waterFlowReading(status), /1 reach with a USGS flow direction · 1 lit by a gauge reading/);

  // Panning back over loaded cells reuses the cache.
  const before = requested.length;
  map.fire("moveend");
  await settle();
  assert.equal(requested.length, before, "cached cells are not fetched again");
  unsubscribe();
});

test("a hidden gauge layer lends no emphasis, and provider failure is reported and not hammered", async () => {
  const flow = await loadSync();
  let calls = 0;
  flow.setWaterFlowFetcher(async (key) => { calls += 1; return payload(key, [fixtureReach(`R${calls}`, [[-97.24, 38.1], [-97.2, 38.1]])]); });
  const gauge = { type: "Feature", geometry: { type: "Point", coordinates: [-97.22, 38.1] }, properties: { value: 50, readingState: "measured", trend: "steady", visualMagnitude: 1.7 } };
  const hidden = fakeMap({ gauges: [gauge], gaugeVisible: false });
  flow.syncWaterFlow(hidden, OPTIONS);
  await settle();
  assert.equal(flow.waterFlowStatus(hidden).gaugedReaches, 0, "gauge readings follow the gauge layer's visibility");

  let failures = 0;
  flow.setWaterFlowFetcher(async () => { failures += 1; throw new Error("blocked"); });
  const broken = fakeMap({ center: [-99.6, 38.6] });
  flow.syncWaterFlow(broken, OPTIONS);
  await settle();
  assert.equal(flow.waterFlowStatus(broken).state, "unavailable");
  assert.match(flow.waterFlowReading(flow.waterFlowStatus(broken)), /unavailable/);
  const attempts = failures;
  broken.fire("moveend");
  await settle();
  assert.equal(failures, attempts, "failed cells wait before retrying");
});

test("switching off removes the layer and cancels requests in flight; a failure to add never breaks the map", async () => {
  const flow = await loadSync();
  const aborted = [];
  flow.setWaterFlowFetcher((key, signal) => new Promise((_resolve, reject) => { signal.addEventListener("abort", () => { aborted.push(key); reject(new Error("aborted")); }); }));
  const map = fakeMap({ center: [-96.4, 38.3] });
  flow.syncWaterFlow(map, OPTIONS);
  assert.ok(map.getLayer(flow.WATER_FLOW_LAYER_ID));
  map.fx = { waterFlow: false };
  flow.syncWaterFlow(map, OPTIONS);
  assert.equal(map.getLayer(flow.WATER_FLOW_LAYER_ID), undefined);
  assert.ok(aborted.length > 0, "pending cells are cancelled");
  assert.equal(flow.waterFlowStatus(map).state, "off");

  const broken = fakeMap();
  broken.addLayer = () => { throw new Error("WebGL context lost"); };
  assert.equal(flow.syncWaterFlow(broken, OPTIONS), false);
  assert.equal(broken.getLayer(flow.WATER_FLOW_LAYER_ID), undefined);
});

test("the water layer shows only when on, at river zoom and outside Battery saver", async () => {
  const flow = await loadSync();
  assert.equal(flow.waterFlowShouldShow(true, false, 10), true);
  assert.equal(flow.waterFlowShouldShow(true, false, 9.9), false);
  assert.equal(flow.waterFlowShouldShow(true, true, 12), false);
  assert.equal(flow.waterFlowShouldShow(false, false, 12), false);
  assert.equal(flow.waterFlowReading({ state: "off", reaches: 0, gaugedReaches: 0, cells: 0, failedCells: 0, truncatedCells: 0 }), null);
  assert.match(flow.waterFlowReading({ state: "zoom", reaches: 0, gaugedReaches: 0, cells: 0, failedCells: 0, truncatedCells: 0 }), /Zoom to 10/);
  assert.match(flow.waterFlowReading({ state: "partial", reaches: 0, gaugedReaches: 0, cells: 1, failedCells: 1, truncatedCells: 0 }), /No mapped flow direction in view · some areas incomplete/);
});
