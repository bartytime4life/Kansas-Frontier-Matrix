import assert from 'node:assert/strict';
import test from 'node:test';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
import { componentHarness, findNode, settle } from './component-harness.mjs';
const source = ts.transpileModule(await readFile('app/public-map-preview-model.ts', 'utf8'), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const model = await import(`data:text/javascript;base64,${Buffer.from(source).toString('base64')}`);
const record = id => ({ id, publisher: 'OSMRE', point: [-94.9, 37.5], assets: [] });
const payload = id => ({ type: 'FeatureCollection', features: [{ type: 'Feature', geometry: { type: 'Point', coordinates: [-94.9, 37.5] }, properties: { objectid: id, documentnumber: 34, mapscale: 100, names: `Source ${id}` } }] });
const deferred = () => { let resolve; const promise = new Promise(done => { resolve = done; }); return { promise, resolve }; };

async function previewHarness({ deferRuntime = false } = {}) {
  const maps = [], requests = [], runtimes = [];
  class Map {
    constructor() { this.events = new globalThis.Map(); this.layers = new globalThis.Map(); this.sources = new globalThis.Map(); this.removed = 0; this.writes = []; maps.push(this); }
    addControl() {}
    on(name, callback) { this.events.set(name, callback); }
    addSource(name, specification) { this.sources.set(name, { setData: value => this.writes.push(value), specification }); }
    addLayer(layer) { this.layers.set(layer.id, layer); }
    getLayer(id) { return this.layers.get(id); }
    getSource(id) { return this.sources.get(id); }
    queryRenderedFeatures() { return []; }
    getBounds() { return { getWest: () => -95.1, getSouth: () => 37.3, getEast: () => -94.7, getNorth: () => 37.7 }; }
    remove() { this.removed++; }
  }
  const runtime = { Map, NavigationControl: class {}, setWorkerUrl() {} };
  const h = await componentHarness('app/public-map-preview.tsx', {
    './maplibre-seam': { loadMapLibre: () => { if (!deferRuntime) return Promise.resolve(runtime); const pending = deferred(); runtimes.push(pending); return pending.promise; } },
    './bounded-json': { readBoundedJson: response => response.json() }, './public-map-preview-model': model,
  }, { URLSearchParams, queueMicrotask, fetch: (url, options) => { const pending = deferred(); requests.push({ url, options, ...pending }); return pending.promise; } });
  let current = record('first'), lastContainer = null;
  const render = () => {
    const tree = h.render(h.exports.PublicMapPreview, { record: current });
    const container = findNode(tree, node => node.type === 'div' && node.props['aria-label'] === 'Interactive source map');
    if (container) { container.props.ref.current = {}; lastContainer = container.props.ref; }
    else if (lastContainer) { lastContainer.current = null; lastContainer = null; }
    h.commit(); return tree;
  };
  const button = (tree, label) => findNode(tree, node => node.type === 'button' && node.props.children === label);
  const open = async () => { let tree = render(); button(tree, 'Open source map preview').props.onClick(); render(); await settle(); if (!deferRuntime) maps.at(-1).events.get('load')(); return render(); };
  const finish = async (index, id, ok = true) => { requests[index].resolve({ ok, json: async () => payload(id) }); await settle(); return render(); };
  return { h, render, button, open, finish, maps, requests, runtimes, runtime, setRecord: next => { current = next; } };
}

test('closing a pending preview aborts its work; reopening releases busy state and withholds the late result', async () => {
  const p = await previewHarness(); let tree = await p.open();
  assert.equal(p.button(tree, 'Load this map area').props.disabled, false);
  p.button(tree, 'Load this map area').props.onClick(); tree = p.render();
  assert.equal(p.button(tree, 'Loading source records…').props.disabled, true); assert.equal(p.requests.length, 1);
  p.button(tree, 'Close map preview').props.onClick(); tree = p.render();
  assert.equal(p.requests[0].options.signal.aborted, true); assert.equal(p.maps[0].removed, 1);
  tree = await p.open(); assert.equal(p.button(tree, 'Load this map area').props.disabled, false);
  p.button(tree, 'Load this map area').props.onClick(); tree = p.render(); assert.equal(p.requests.length, 2);
  tree = await p.finish(0, 101);
  assert.equal(p.button(tree, 'Loading source records…').props.disabled, true, 'late old request cannot release the new request busy state');
  assert.equal(p.maps[0].writes.filter(value => value.features.length).length, 0); assert.equal(p.maps[1].writes.filter(value => value.features.length).length, 0);
  tree = await p.finish(1, 202); assert.equal(p.button(tree, 'Load this map area').props.disabled, false);
  assert.match(JSON.stringify(tree), /Source 202/); assert.doesNotMatch(JSON.stringify(tree), /Source 101/);
  p.h.dispose(); assert.equal(p.maps[1].removed, 1);
});

test('changing records closes the old preview, aborts pending work and allows an independent new load', async () => {
  const p = await previewHarness(); let tree = await p.open();
  p.button(tree, 'Load this map area').props.onClick(); p.render();
  p.setRecord(record('second')); p.render(); await settle(); tree = p.render();
  assert.equal(p.requests[0].options.signal.aborted, true); assert.equal(p.maps[0].removed, 1);
  assert.ok(p.button(tree, 'Open source map preview')); assert.equal(p.button(tree, 'Loading source records…'), undefined);
  tree = await p.open(); assert.equal(p.button(tree, 'Load this map area').props.disabled, false);
  tree = await p.finish(0, 303); assert.doesNotMatch(JSON.stringify(tree), /Source 303/);
  p.button(tree, 'Load this map area').props.onClick(); tree = p.render();
  assert.match(p.requests[1].url, /kind=osmre-nmmr/);
  tree = await p.finish(1, 404); assert.match(JSON.stringify(tree), /Source 404/);
  p.h.dispose();
});

test('explicit cancellation clears busy state immediately and late responses cannot replace cancellation or a newer result', async () => {
  const p = await previewHarness(); let tree = await p.open();
  p.button(tree, 'Load this map area').props.onClick(); tree = p.render();
  p.button(tree, 'Cancel preview').props.onClick(); tree = p.render();
  assert.equal(p.requests[0].options.signal.aborted, true); assert.equal(p.button(tree, 'Load this map area').props.disabled, false);
  assert.match(JSON.stringify(tree), /Preview cancelled/);
  tree = await p.finish(0, 505); assert.match(JSON.stringify(tree), /Preview cancelled/); assert.doesNotMatch(JSON.stringify(tree), /Source 505/);
  p.button(tree, 'Load this map area').props.onClick(); tree = p.render(); assert.equal(p.button(tree, 'Loading source records…').props.disabled, true);
  tree = await p.finish(1, 606); assert.match(JSON.stringify(tree), /Source 606/); assert.doesNotMatch(JSON.stringify(tree), /Preview cancelled/);
  p.h.dispose();
});

test('a renderer module resolving after close does not create a stale map on a reopened container', async () => {
  const p = await previewHarness({ deferRuntime: true }); let tree = await p.open();
  assert.equal(p.runtimes.length, 1); assert.equal(p.maps.length, 0); assert.equal(p.button(tree, 'Load this map area').props.disabled, true);
  p.button(tree, 'Close map preview').props.onClick(); p.render(); tree = await p.open(); assert.equal(p.runtimes.length, 2);
  p.runtimes[0].resolve(p.runtime); await settle(); tree = p.render(); assert.equal(p.maps.length, 0);
  p.runtimes[1].resolve(p.runtime); await settle(); assert.equal(p.maps.length, 1); p.maps[0].events.get('load')(); tree = p.render();
  assert.equal(p.button(tree, 'Load this map area').props.disabled, false); p.h.dispose(); assert.equal(p.maps[0].removed, 1);
});
