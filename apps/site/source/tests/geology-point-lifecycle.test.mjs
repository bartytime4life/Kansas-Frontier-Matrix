import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import { componentHarness, findNode, settle } from "./component-harness.mjs";

const file = "app/geology-point-explorer.tsx";
const imports = {
  "./bounded-json": { readBoundedJson: response => response.json() },
  "./underground-resources-model": { RESOURCE_SOURCES: {
    oilgas: { limitation: "Oil and gas source context", link: "https://example.test/oilgas" },
    minerals: { limitation: "Mineral source context", link: "https://example.test/minerals" },
  } },
  "./geology-point-explorer.module.css": { default: new Proxy({}, { get: (_target, key) => key }) },
};
const row = (id, name = id) => ({ id, name, coordinates: [-98, 38], material: "Recorded material", status: "Recorded status", details: [["Source ID", id]] });
const response = rows => ({ ok: true, json: async () => ({ rows, partial: false, rejected: 0, retrievedAt: "2026-11-09T12:00:00Z" }) });
const status = tree => findNode(tree, node => node.props?.role === "status").props.children;

function mapFixture() {
  const listeners = new Map(), sources = new Map(), layers = new Map();
  const map = {
    center: [-98, 38], hit: null, data: null,
    getCenter: () => ({ lng: map.center[0], lat: map.center[1] }),
    getBounds: () => ({ getEast: () => map.center[0] + 1, getWest: () => map.center[0] - 1, getNorth: () => map.center[1] + 1, getSouth: () => map.center[1] - 1 }),
    on(name, callback) { if (!listeners.has(name)) listeners.set(name, new Set()); listeners.get(name).add(callback); },
    off(name, callback) { listeners.get(name)?.delete(callback); },
    emit(name) { for (const callback of [...listeners.get(name) ?? []]) callback({ point: { x: 1, y: 2 } }); },
    listenerCount: name => listeners.get(name)?.size ?? 0,
    isStyleLoaded: () => true,
    getSource: id => sources.get(id),
    addSource(id, source) { map.data = source.data; sources.set(id, { setData(data) { map.data = data; } }); },
    removeSource: id => sources.delete(id),
    getLayer: id => layers.get(id),
    addLayer: layer => layers.set(layer.id, layer),
    removeLayer: id => layers.delete(id),
    queryRenderedFeatures: () => map.hit ? [{ properties: { id: map.hit } }] : [],
    clearStyle() { sources.clear(); layers.clear(); },
    get sourceCount() { return sources.size; },
    get layerCount() { return layers.size; },
  };
  return map;
}

async function harness() {
  const requests = [];
  const h = await componentHarness(file, imports, {
    URLSearchParams,
    fetch: (url, options) => new Promise(resolve => requests.push({ url: new URL(url, "https://site.test"), options, resolve })),
  }, "\nexports.Sample = GeologyPointSample;\n");
  return { h, requests };
}

async function sample(map, frameKey) {
  const { h, requests } = await harness();
  const props = { map, frameKey, monitoringVisible: false };
  const render = () => { const tree = h.render(h.exports.Sample, props); h.commit(); return tree; };
  return { h, requests, render };
}

test("geology sample mounting follows enabled, redacted and current bounded map frames", async () => {
  const { h, requests } = await harness(), map = mapFixture();
  let props = { map, enabled: false, redacted: false, monitoringVisible: true };
  const render = () => { const tree = h.render(h.exports.default, props); h.commit(); return tree; };
  assert.equal(render(), null);
  assert.equal(map.listenerCount("moveend"), 0);
  props = { ...props, enabled: true, redacted: true };
  assert.equal(render(), null);
  props = { ...props, redacted: false };
  assert.equal(render(), null, "the frame must be known before a sample mounts");
  let tree = render();
  assert.equal(tree.type.name, "GeologyPointSample");
  assert.equal(tree.props.frameKey, "-98.4,37.6,-97.6,38.4");
  assert.equal(map.listenerCount("moveend"), 1);
  map.center = [-97, 39]; map.emit("moveend"); tree = render();
  assert.equal(tree.props.frameKey, "-97.4,38.6,-96.6,39.4");
  // React uses this identity to unmount the old requests and selection when the
  // bounded frame changes; the sample behavior is exercised separately below.
  assert.match(await readFile(file, "utf8"), /<GeologyPointSample key=\{frameKey\}/);
  props = { ...props, redacted: true };
  assert.equal(render(), null); assert.equal(map.listenerCount("moveend"), 0);
  props = { ...props, redacted: false, enabled: false };
  assert.equal(render(), null); assert.equal(map.listenerCount("moveend"), 0);
  props = { ...props, enabled: true, map: null };
  assert.equal(render(), null);
  assert.equal(requests.length, 0, "the outer frame subscription does not fetch source data");
  h.dispose();
});

test("each geology frame starts loading, then installs source markers and selected record details", async () => {
  const map = mapFixture(), current = await sample(map, "-98.4,37.6,-97.6,38.4");
  let tree = current.render();
  assert.equal(status(tree), "Loading local source points…");
  assert.equal(current.requests.length, 2);
  assert.deepEqual(current.requests.map(request => request.url.searchParams.get("kind")), ["oilgas", "minerals"]);
  for (const request of current.requests) {
    assert.equal(request.url.searchParams.get("bounds"), "-98.4,37.6,-97.6,38.4");
    assert.equal(request.options.cache, "no-store"); assert.equal(request.options.signal.aborted, false);
  }
  assert.equal(map.data.features.length, 0);
  current.requests[0].resolve(response([row("oilgas:1", "Source well")]));
  current.requests[1].resolve(response([row("minerals:2", "Source mine")]));
  await settle(); tree = current.render();
  assert.equal(status(tree), "Select a point for its 2D record details.");
  assert.deepEqual(Array.from(map.data.features, feature => feature.properties.id), ["oilgas:1", "minerals:2"]);
  map.hit = "oilgas:1"; map.emit("click"); tree = current.render();
  assert.equal(findNode(tree, node => node.type === "h3").props.children, "Source well");
  map.clearStyle(); map.emit("styledata");
  assert.equal(map.sourceCount, 1); assert.equal(map.layerCount, 1);
  assert.equal(map.data.features[0].properties.selected, true);
  current.h.dispose();
  assert.ok(current.requests.every(request => request.options.signal.aborted));
  assert.equal(map.listenerCount("click"), 0); assert.equal(map.listenerCount("styledata"), 0);
  assert.equal(map.sourceCount, 0); assert.equal(map.layerCount, 0);
});

test("retired geology frames abort requests and cannot overwrite a newer sample", async () => {
  const map = mapFixture(), old = await sample(map, "-98.4,37.6,-97.6,38.4");
  old.render(); old.h.dispose();
  assert.ok(old.requests.every(request => request.options.signal.aborted));
  const current = await sample(map, "-97.4,38.6,-96.6,39.4");
  current.render();
  for (const request of old.requests) request.resolve(response([row("oilgas:old", "STALE source")]));
  await settle();
  assert.equal(map.data.features.length, 0, "late retired responses cannot draw markers");
  assert.doesNotMatch(JSON.stringify(old.h.render(old.h.exports.Sample, { map, frameKey: "-98.4,37.6,-97.6,38.4", monitoringVisible: false })), /STALE source/);
  current.requests[0].resolve(response([row("oilgas:new", "Current source")]));
  current.requests[1].resolve(response([]));
  await settle(); current.render();
  assert.deepEqual(Array.from(map.data.features, feature => feature.properties.id), ["oilgas:new"]);
  map.hit = "oilgas:new"; map.emit("click");
  assert.equal(findNode(current.render(), node => node.type === "h3").props.children, "Current source");
  current.h.dispose();
  // Disabling or redacting removes the child. Reopening the same frame creates
  // a fresh sample with no former selection, even if its bounds are unchanged.
  const reopened = await sample(map, "-97.4,38.6,-96.6,39.4");
  const tree = reopened.render();
  assert.equal(status(tree), "Loading local source points…");
  assert.equal(findNode(tree, node => node.type === "h3"), undefined);
  assert.equal(map.data.features.length, 0);
  reopened.h.dispose();
  for (const request of reopened.requests) request.resolve(response([row("oilgas:hidden", "HIDDEN source")]));
  await settle();
  assert.equal(map.sourceCount, 0); assert.equal(map.layerCount, 0);
  assert.ok(reopened.requests.every(request => request.options.signal.aborted));
});

test("a failed geology source preserves the other source and reports unavailability", async () => {
  const map = mapFixture(), current = await sample(map, "-98.4,37.6,-97.6,38.4");
  current.render();
  current.requests[0].resolve(response([row("oilgas:1")]));
  current.requests[1].resolve({ ok: false });
  await settle(); const tree = current.render();
  assert.ok(findNode(tree, node => node.type === "p" && node.props.children === "One or more KGS resource sources are unavailable in this view."));
  assert.equal(map.data.features.length, 1);
  current.h.dispose();
});
