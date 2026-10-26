import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';

// The real welcome map engine against a stand-in MapLibre, view module and
// style fetch: these tests are about which style and camera apply when, not rendering.
const toUrl = source => `data:text/javascript;base64,${Buffer.from(source).toString('base64')}`;
const stubs = {
  "'../maplibre-seam'": toUrl(`export const loadMapLibre = async () => ({ setWorkerUrl() {}, Map: globalThis.__welcome.FakeMap });`),
  "'../map-runtime'": toUrl(`export const BASEMAPS = { standard: { style: 'https://style.test/standard' }, relief: { style: { version: 8, name: 'relief', sources: {}, layers: [] } } };`),
  "'../basemap-cache'": toUrl(`export const basemapCacheRequest = url => ({ url });`),
  "'../map-performance'": toUrl(`export const browserRenderBudget = () => ({ pixelRatio: 1, tileCache: 8 });`),
  "'../webgl-support'": toUrl(`export const webgl2Available = () => true;`),
  "'../welcome-map-view'": toUrl(`
    const view = (topic, basemap, scene, zoom) => ({ topic, basemap, scene, camera: { center: [-98, 38], zoom, pitch: 0, bearing: 0 } });
    const VIEWS = { evidence: view('evidence', 'standard', '2d', 6.4), science: view('science', 'standard', 'globe', 3.2), sky: view('sky', 'standard', 'globe', 2.6), terrain: view('terrain', 'relief', 'terrain', 7.4) };
    export const WELCOME_IDLE_VIEW = view(null, 'standard', '2d', 6.1);
    export const welcomeView = topic => VIEWS[topic] ?? WELCOME_IDLE_VIEW;
    export const welcomeStyle = (style, v) => ({ ...style, scene: v.scene });
    export const welcomeDriftLeg = v => ({ bearing: v.camera.bearing + 24, zoom: v.camera.zoom, duration: 30000 });`),
};
let source = await readFile('app/living-welcome/map-engine.mjs', 'utf8');
for (const [from, to] of Object.entries(stubs)) {
  assert.ok(source.includes(`from ${from};`), `engine still imports ${from}`);
  source = source.replace(`from ${from};`, `from '${to}';`);
}
// Each test loads its own copy, so the engine's shared style-document cache starts empty.
let copies = 0;
const loadEngine = () => import(toUrl(`${source}\n// copy ${++copies}`));
const { SETTLE_MS } = await loadEngine();

class FakeMap {
  constructor() { globalThis.__welcome.map = this; this.handlers = new Map(); this.log = []; this.isLoaded = false; this.canvas = { setAttribute() {}, tabIndex: 0 }; }
  getCanvas() { return this.canvas; }
  on(type, fn) { this.handlers.set(type, [...(this.handlers.get(type) ?? []), { fn }]); }
  once(type, fn) { this.handlers.set(type, [...(this.handlers.get(type) ?? []), { fn, once: true }]); }
  emit(type, event = {}) { const list = this.handlers.get(type) ?? []; this.handlers.set(type, list.filter(h => !h.once)); for (const h of list) h.fn(event); }
  setStyle(style) { this.log.push(['setStyle', style.name ?? style.url, style.scene]); }
  // Camera moves end at once, as a programmatic jump does.
  jumpTo(camera) { this.log.push(['jumpTo', camera.zoom]); this.emit('moveend'); }
  flyTo(camera) { this.log.push(['flyTo', camera.zoom]); }
  easeTo(camera) { this.log.push(['easeTo', camera.bearing]); }
  stop() {}
  loaded() { return this.isLoaded; }
  remove() {}
}
const settle = () => new Promise(resolve => setTimeout(resolve, SETTLE_MS + 30));
async function start() {
  const fetches = [];
  globalThis.__welcome = { FakeMap };
  globalThis.fetch = url => new Promise(resolve => fetches.push({ url, resolve: () => resolve({ ok: true, json: async () => ({ version: 8, url, sources: {}, layers: [] }) }) }));
  let ready = 0;
  const { createWelcomeMap } = await loadEngine();
  const engine = await createWelcomeMap({}, { onReady: () => ready++ });
  return { engine, fetches, map: globalThis.__welcome.map, ready: () => ready };
}
const tick = () => new Promise(resolve => setTimeout(resolve, 0));

test('a topic that shares a pending style gets that style when it arrives', async () => {
  // Evidence uses the same default map as the idle view, Sky the same globe style as Science.
  for (const [first, second, zoom] of [[null, 'evidence', 6.4], ['science', 'sky', 2.6]]) {
    const { engine, fetches, map } = await start();
    engine.show(first);
    if (first) { await settle(); }
    engine.show(second); await settle();
    assert.equal(fetches.length, 1, 'one style document for both topics');
    fetches[0].resolve(); await tick(); await tick();
    assert.deepEqual(map.log.filter(([k]) => k === 'setStyle').length, 1, 'the pending style is applied, not dropped');
    map.emit('style.load');
    assert.deepEqual(map.log.find(([k]) => k === 'jumpTo'), ['jumpTo', zoom], 'it opens on the topic selected when it loaded');
    engine.dispose();
  }
});

test('a style superseded by a different map is dropped', async () => {
  const { engine, fetches, map } = await start();
  engine.show(null);
  engine.show('terrain'); await settle(); await tick();
  fetches[0].resolve(); await tick(); await tick();
  assert.deepEqual(map.log.filter(([k]) => k === 'setStyle'), [['setStyle', 'relief', 'terrain']], 'only the relief style reaches the map');
  engine.dispose();
});

test('the preview is ready on its first settled frame even while the camera drifts', async () => {
  const { engine, fetches, map, ready } = await start();
  engine.setPaused(false);
  engine.show(null);
  fetches[0].resolve(); await tick(); await tick();
  map.emit('render'); map.isLoaded = true; map.emit('render');
  assert.equal(ready(), 0, 'not before a real style has loaded');
  map.emit('style.load');
  assert.ok(map.log.some(([k]) => k === 'easeTo'), 'the drift is running');
  map.emit('render');
  assert.equal(ready(), 1, 'ready without waiting for the camera to stop');
  map.emit('render');
  assert.equal(ready(), 1, 'reported once');
  engine.dispose();
});
