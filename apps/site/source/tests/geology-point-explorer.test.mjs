import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";
import { componentHarness, findNode, settle } from "./component-harness.mjs";

const moduleUrl = source => `data:text/javascript;base64,${Buffer.from(ts.transpileModule(source, {
  compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
}).outputText).toString("base64")}`;
const subsurface = moduleUrl((await readFile("app/subsurface-model.ts", "utf8"))
  .replace('import { atRecordYear } from "./subsurface-materials";', "const atRecordYear = () => true;"));
const model = await import(moduleUrl((await readFile("app/underground-resources-model.ts", "utf8"))
  .replace('"./subsurface-model"', JSON.stringify(subsurface))));
const bounded = await import(moduleUrl(await readFile("app/bounded-json.ts", "utf8")));
const frame = [-99.7, 38.7, -99.3, 39];
const row = (kind, overrides = {}) => ({
  id: `${kind}:1`, name: "Test resource", material: "Limestone", status: "Recorded",
  coordinates: [-99.5, 38.8], details: [["County", "Test county"]], ...overrides,
});
const catalog = (kind, rows = [row(kind)], overrides = {}) => ({
  kind, bounds: frame, rows, partial: false, rejected: 0, retrievedAt: "2026-11-19T12:00:00Z", ...overrides,
});
const deferred = () => { let resolve; const promise = new Promise(done => { resolve = done; }); return { promise, resolve }; };

function fakeMap() {
  const sources = new Map(), layers = new Map(), handlers = new Map();
  const map = {
    sources, layers, writes: 0,
    isStyleLoaded: () => true,
    getCenter: () => ({ lng: -99.5, lat: 38.85 }),
    getBounds: () => ({ getWest: () => -99.7, getEast: () => -99.3, getSouth: () => 38.7, getNorth: () => 39 }),
    getSource: id => sources.get(id), getLayer: id => layers.get(id),
    addSource(id, value) {
      sources.set(id, { data: value.data, setData(data) { this.data = data; map.writes++; map.emit("styledata"); } });
      map.emit("styledata");
    },
    addLayer(layer) { layers.set(layer.id, layer); map.emit("styledata"); },
    removeLayer(id) { layers.delete(id); map.emit("styledata"); },
    removeSource(id) { sources.delete(id); map.emit("styledata"); },
    on(event, callback) { if (!handlers.has(event)) handlers.set(event, new Set()); handlers.get(event).add(callback); },
    off(event, callback) { handlers.get(event)?.delete(callback); },
    emit(event, value) { for (const callback of [...handlers.get(event) ?? []]) callback(value); },
    queryRenderedFeatures: () => [{ properties: { id: "oilgas:1" } }],
  };
  return map;
}

async function setup(fetch, globals = {}) {
  const h = await componentHarness("app/geology-point-explorer.tsx", {
    "./bounded-json": bounded, "./subsurface-model": await import(subsurface),
    "./underground-resources-model": model,
    "./geology-point-explorer.module.css": { default: new Proxy({}, { get: (_, key) => key }) },
  }, { URLSearchParams, fetch, ...globals }, "\nexport { GeologyPointSample };");
  const map = fakeMap();
  const render = () => { const tree = h.render(h.exports.GeologyPointSample, { map, frameKey: frame.join(","), monitoringVisible: false }); h.commit(); return tree; };
  return { h, map, render };
}

test("valid resource rows render markers and selected details without a style update loop", async () => {
  const { h, map, render } = await setup(async url => Response.json(catalog(new URL(url, "https://fixture.test").searchParams.get("kind"))));
  try {
    assert.match(findNode(render(), node => node.props?.role === "status").props.children, /Loading/);
    await settle(); render();
    assert.equal([...map.sources.values()][0].data.features.length, 2);
    for (let index = 0; index < 5; index++) map.emit("styledata");
    assert.equal(map.writes, 0, "style events cannot trigger recursive source writes");
    map.emit("click", { point: {} });
    const tree = render();
    assert.equal(findNode(tree, node => node.type === "h3").props.children, "Test resource");
    assert.match(JSON.stringify(tree), /Test county/);
    map.sources.clear(); map.layers.clear(); map.emit("styledata");
    assert.equal([...map.sources.values()][0].data.features.length, 2, "a replacement style restores markers");
  } finally { h.dispose(); }
  assert.equal(map.sources.size, 0); assert.equal(map.layers.size, 0);
});

test("malformed successful responses stay unavailable instead of reaching map and detail rendering", async () => {
  const invalid = [
    null, [], catalog("oilgas", [null]), catalog("oilgas", [row("oilgas", { coordinates: ["-99.5", 38.8] })]),
    catalog("oilgas", [row("oilgas", { coordinates: [-100, 38.8] })]),
    catalog("oilgas", [row("oilgas", { details: [null] })]),
    catalog("oilgas", [row("oilgas", { details: [["County", {}]] })]),
    catalog("oilgas", [row("oilgas", { name: {} })]),
    catalog("oilgas", [row("minerals")]), catalog("oilgas", [row("oilgas"), row("oilgas")]),
    catalog("oilgas", [], { bounds: [-100, 38, -99, 39] }), catalog("oilgas", [], { retrievedAt: "invalid" }),
    catalog("oilgas", [], { rejected: -1 }), catalog("oilgas", [], { partial: "false" }),
  ];
  for (const value of invalid) {
    const { h, map, render } = await setup(async () => Response.json(value));
    try {
      render(); await settle(); const tree = render();
      assert.equal([...map.sources.values()][0].data.features.length, 0);
      assert.match(JSON.stringify(tree), /sources are unavailable/);
      assert.equal(findNode(tree, node => node.type === "h3"), undefined);
    } finally { h.dispose(); }
  }
});

test("HTTP errors cancel their bodies before JSON parsing", async () => {
  let cancelled = 0;
  const { h, map, render } = await setup(async () => ({
    ok: false, body: { cancel: async () => { cancelled++; } },
    headers: { get: () => assert.fail("failed HTTP response must not be parsed") },
  }));
  try {
    render(); await settle(); render();
    assert.equal(cancelled, 2); assert.equal([...map.sources.values()][0].data.features.length, 0);
  } finally { h.dispose(); }
});

test("deadline ends loading even when fetch ignores abort and late responses cannot add markers", async () => {
  const timers = new Map(), pending = [], signals = [];
  const { h, map, render } = await setup((_url, options) => {
    const request = deferred(); pending.push(request); signals.push(options.signal); return request.promise;
  }, { setTimeout: (fn, ms) => { assert.equal(ms, 18_000); timers.set(1, fn); return 1; }, clearTimeout: id => timers.delete(id) });
  try {
    render(); assert.equal(timers.size, 1);
    timers.get(1)(); await settle(); const tree = render();
    assert.ok(signals.every(signal => signal.aborted)); assert.equal(timers.size, 0);
    assert.doesNotMatch(findNode(tree, node => node.props?.role === "status").props.children, /Loading/);
    assert.match(JSON.stringify(tree), /sources are unavailable/);
    pending[0].resolve(Response.json(catalog("oilgas"))); pending[1].resolve(Response.json(catalog("minerals")));
    await settle(); render();
    assert.equal([...map.sources.values()][0].data.features.length, 0);
  } finally { h.dispose(); }
});

test("hiding the sample aborts requests, clears its deadline and rejects late results", async () => {
  const pending = [], timers = new Map();
  const { h, map, render } = await setup((_url, options) => {
    const request = deferred(); pending.push({ ...request, signal: options.signal }); return request.promise;
  }, { setTimeout: fn => { timers.set(1, fn); return 1; }, clearTimeout: id => timers.delete(id) });
  render(); h.dispose();
  assert.equal(timers.size, 0); assert.ok(pending.every(request => request.signal.aborted));
  pending[0].resolve(Response.json(catalog("oilgas"))); pending[1].resolve(Response.json(catalog("minerals")));
  await settle();
  assert.equal(map.sources.size, 0); assert.equal(map.layers.size, 0);
});


test("a stalled source cannot discard a second source that completed before the deadline", async () => {
  const timers = new Map();
  const { h, map, render } = await setup(url => {
    const kind = new URL(url, "https://fixture.test").searchParams.get("kind");
    return kind === "oilgas" ? Promise.resolve(Response.json(catalog(kind))) : new Promise(() => {});
  }, { setTimeout: fn => { timers.set(1, fn); return 1; }, clearTimeout: id => timers.delete(id) });
  try {
    render(); await settle(); timers.get(1)(); await settle(); const tree = render();
    const features = [...map.sources.values()][0].data.features;
    assert.equal(features.length, 1); assert.equal(features[0].properties.id, "oilgas:1");
    assert.match(JSON.stringify(tree), /sources are unavailable/);
    assert.equal(timers.size, 0);
  } finally { h.dispose(); }
});
