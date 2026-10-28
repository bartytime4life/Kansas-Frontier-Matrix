import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';

// The real welcome map engine against a stand-in MapLibre, view module and
// style fetch: these tests are about which style and camera apply when, not rendering.
const toUrl = source => `data:text/javascript;base64,${Buffer.from(source).toString('base64')}`;
const stubs = {
  "'../noaa-satellite'": toUrl(`export const NOAA_SATELLITE_FRAMES_PATH = '/api/noaa-satellite/frames'; export const NOAA_SATELLITE_FRESH_AGE_MS = 5400000; export const isNoaaSatelliteManifest = value => Array.isArray(value?.frames);`),
  "'../maplibre-seam'": toUrl(`export const loadMapLibre = async () => ({ setWorkerUrl() {}, Map: globalThis.__welcome.FakeMap });`),
  "'../map-runtime'": toUrl(`export const BASEMAPS = { standard: { style: 'https://style.test/standard' }, relief: { style: { version: 8, name: 'relief', sources: {}, layers: [] } } };`),
  "'../basemap-cache'": toUrl(`export const basemapCacheRequest = url => ({ url });`),
  "'../map-performance'": toUrl(`export const browserRenderBudget = () => globalThis.__welcome.budget;`),
  "'../webgl-support'": toUrl(`export const webgl2Available = () => globalThis.__welcome.webgl;`),
  "'../live-context'": toUrl(`
    const SOURCES = [{ id: 'noaa-goes-geocolor', kind: 'OPERATIONAL_WMS' }, { id: 'nws-radar', kind: 'OPERATIONAL_WMS' }, { id: 'nws-alerts', kind: 'OPERATIONAL_GEOJSON', apiPath: '/api/live-context?feed=nws-alerts' }, { id: 'usgs-earthquakes', kind: 'OPERATIONAL_GEOJSON', apiPath: '/api/live-context?feed=usgs-earthquakes' }, { id: 'kdot-roads', kind: 'OPERATIONAL_WMS' }, { id: 'census-counties', kind: 'SNAPSHOT_GEOJSON', apiPath: '/api/live-context?feed=census-counties' }];
    export const OFFICIAL_CONTEXT_SOURCES = SOURCES;
    export const OFFICIAL_CONTEXT_BY_ID = Object.fromEntries(SOURCES.map(s => [s.id, s]));
    export const defaultOfficialContextOpacity = () => ({});
    export const applyOfficialContextState = (map, visibility, opacity, payloads) => globalThis.__welcome.drawn.push({ shown: Object.keys(visibility).filter(id => visibility[id]), payloads: Object.keys(payloads) });
    export const clearNoaaSatelliteFrame = () => {};
    export const setNoaaSatelliteFrame = (map, frame) => globalThis.__welcome.satellite.push(frame);
    export const setNoaaRadarObservationTime = (map, at) => globalThis.__welcome.radar.push(at);`),
  "'../population-prisms'": toUrl(`export const setPopulationPrisms = (map, on) => globalThis.__welcome.prisms.push(on);`),
  "'../noaa-radar'": toUrl(`
    export const NOAA_RADAR_FRAME_API_PATH = '/api/noaa-radar/frames';
    export const isNoaaRadarManifest = value => Array.isArray(value?.frames);
    export const noaaRadarManifestIsFresh = manifest => globalThis.__welcome.fresh(manifest.frames.at(-1));`),
  "'../welcome-map-view'": toUrl(`
    const view = (topic, basemap, scene, zoom, starters = [], prisms = false) => ({ topic, basemap, scene, camera: { center: topic === 'terrain' ? [-99.6, 38.9] : [-98, 38], zoom, pitch: 0, bearing: 0 }, starters, prisms });
    const VIEWS = { satellite: view('satellite', 'standard', '2d', 5.4, ['noaa-goes-geocolor']), evidence: view('evidence', 'standard', '2d', 6.4), science: view('science', 'standard', 'globe', 3.2), sky: view('sky', 'standard', 'globe', 2.6), terrain: view('terrain', 'relief', 'terrain', 7.4), geology: view('geology', 'relief', 'terrain', 6.1, ['usgs-earthquakes']), transport: view('transport', 'relief', 'terrain', 6.1, ['kdot-roads']), weather: view('weather', 'relief', 'terrain', 5.9, ['nws-alerts', 'nws-radar']), people: view('people', 'relief', 'terrain', 6.3, ['census-counties'], true) };
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
  constructor(options) { globalThis.__welcome.map = this; this.options = options; this.handlers = new Map(); this.log = []; this.isLoaded = false; this.canvas = { setAttribute() {}, tabIndex: 0 }; }
  getCanvas() { return this.canvas; }
  on(type, fn) { this.handlers.set(type, [...(this.handlers.get(type) ?? []), { fn }]); }
  once(type, fn) { this.handlers.set(type, [...(this.handlers.get(type) ?? []), { fn, once: true }]); }
  emit(type, event = {}) { const list = this.handlers.get(type) ?? []; this.handlers.set(type, list.filter(h => !h.once)); for (const h of list) h.fn(event); }
  setStyle(style) { this.log.push(['setStyle', style.name ?? style.url, style.scene]); }
  // Camera moves end at once, as a programmatic jump does.
  jumpTo(camera) { this.camera = camera; this.log.push(['jumpTo', camera.zoom]); this.emit('moveend'); }
  flyTo(camera) { this.log.push(['flyTo', camera.zoom]); }
  easeTo(camera) { this.log.push(['easeTo', camera.bearing]); }
  stop() {}
  loaded() { return this.isLoaded; }
  remove() {}
}
const settle = () => new Promise(resolve => setTimeout(resolve, SETTLE_MS + 30));
async function start(budget = { pixelRatio: 1, tileCache: 8 }, overrides = {}) {
  const fetches = [];
  globalThis.__welcome = { FakeMap, budget, webgl: true, drawn: [], radar: [], satellite: [], prisms: [], fresh: () => true, ...overrides };
  // Style documents and starter payloads each wait until the test releases them.
  globalThis.fetch = url => new Promise((resolve, reject) => fetches.push({ url, fail: () => reject(new Error('style unavailable')), resolve: () => resolve({ ok: true, json: async () => url === '/api/noaa-satellite/frames' ? globalThis.__welcome.satelliteManifest : url === '/api/noaa-radar/frames' ? globalThis.__welcome.radarManifest : url.startsWith('/api/') ? { feed: new URL(url, 'http://x').searchParams.get('feed'), data: { type: 'FeatureCollection', features: [] } } : { version: 8, url, sources: {}, layers: [] } }) }));
  let ready = 0, errors = 0;
  const radarReports = [], sourceReports = [];
  const { createWelcomeMap } = await loadEngine();
  const engine = await createWelcomeMap({}, { onReady: () => ready++, onError: () => errors++, onRadar: at => radarReports.push(at), onSources: value => sourceReports.push(value) });
  return { engine, fetches, map: globalThis.__welcome.map, ready: () => ready, errors: () => errors, radarReports, sourceReports };
}
const tick = () => new Promise(resolve => setTimeout(resolve, 0));

test('disabled WebGL and failed map construction report failure without fetching providers',async()=>{
 for(const overrides of [{webgl:false},{FakeMap:class{constructor(){throw new Error('Map initialization failed');}}}]){
  const {engine,map,fetches,errors}=await start(undefined,overrides);
  assert.equal(engine,null);assert.equal(map,undefined);assert.equal(errors(),1);assert.equal(fetches.length,0);
 }
});

test('layer comparison hides late payloads and restores cached data without rebuilding the map', async t => {
  const { engine, map, fetches, sourceReports } = await start();
  t.after(() => engine.dispose());
  engine.show('people'); await tick(); await tick(); map.emit('style.load');
  const requests = fetches.length, styles = map.log.filter(([name]) => name === 'setStyle').length;
  engine.setLayersVisible(false);
  assert.deepEqual(globalThis.__welcome.drawn.at(-1).shown, []);
  assert.equal(globalThis.__welcome.prisms.at(-1), false);
  assert.equal(sourceReports.at(-1).sources[0].state, 'hidden');
  fetches[0].resolve(); await tick();
  assert.deepEqual(globalThis.__welcome.drawn.at(-1).shown, [], 'a late response never reveals a hidden layer');
  engine.setLayersVisible(true);
  assert.deepEqual(globalThis.__welcome.drawn.at(-1).shown, ['census-counties']);
  assert.equal(globalThis.__welcome.prisms.at(-1), true);
  assert.equal(fetches.length, requests, 'restoring already fetched data makes no new request');
  assert.equal(map.log.filter(([name]) => name === 'setStyle').length, styles, 'comparison does not reload the basemap or its tiles');
});

test('base-only comparison defers provider payloads until starter layers are explicitly restored', async t => {
  const { engine, map, fetches } = await start();
  t.after(() => engine.dispose());
  engine.setLayersVisible(false); engine.show('people'); await tick(); await tick(); map.emit('style.load');
  assert.equal(fetches.length, 0);
  engine.setLayersVisible(true);
  assert.equal(fetches.length, 1);
  engine.setLayersVisible(true);
  assert.equal(fetches.length, 1, 'idempotent updates cannot duplicate a pending request');
});

test('returning to a still-pending style applies it only once', async t => {
  const { engine, fetches, map } = await start();
  t.after(() => engine.dispose());
  engine.show('evidence');
  engine.show('terrain'); await settle();
  engine.show('evidence'); await settle();
  fetches[0].resolve(); await tick(); await tick();
  assert.equal(fetches.length, 1, 'the pending document is reused');
  assert.equal(map.log.filter(([name, style]) => name === 'setStyle' && style === 'https://style.test/standard').length, 1, 'one style rebuild for the returning category');
  const jumps = map.log.filter(([name]) => name === 'jumpTo').length;
  map.emit('style.load');
  assert.equal(map.log.filter(([name]) => name === 'jumpTo').length, jumps + 1, 'only the current application owns style.load');
  engine.dispose();
});

test('preview retention is bounded without reducing the selected pixel density', async t => {
  for (const [budget, expected] of [
    [{ pixelRatio: 3, tileCache: 112 }, 48],
    [{ pixelRatio: 2, tileCache: 64, coarsePointer: true }, 32],
    [{ pixelRatio: 1, tileCache: 48, efficient: true }, 24],
    [{ pixelRatio: 1, tileCache: 8 }, 8],
  ]) {
    const { engine, map } = await start(budget);
    t.after(() => engine.dispose());
    assert.equal(map.options.maxTileCacheSize, expected);
    assert.equal(map.options.pixelRatio, budget.pixelRatio);
    engine.dispose();
  }
});

test('battery saver previews stay still across focus and category changes', async t => {
  const { engine, map } = await start({ pixelRatio: 1, tileCache: 48, efficient: true });
  t.after(() => engine.dispose());
  engine.setPaused(false); engine.show('terrain'); await tick(); await tick(); map.emit('style.load');
  engine.show('geology'); await settle();
  engine.setReduced(true); engine.setReduced(false);
  engine.setPaused(true); engine.setPaused(false);
  assert.equal(map.log.filter(([name]) => name === 'easeTo' || name === 'flyTo').length, 0);
  assert.equal(map.log.filter(([name]) => name === 'jumpTo').length, 2, 'the requested cameras still update');
  engine.dispose();
});

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
  assert.ok(!map.log.some(([k]) => k === 'easeTo'), 'the unselected default map does not spend frames drifting');
  map.emit('render');
  assert.equal(ready(), 1, 'ready without waiting for the camera to stop');
  map.emit('render');
  assert.equal(ready(), 1, 'reported once');
  engine.dispose();
});

test('a drawn style stays visible while optional starter sources are pending, including reduced motion', async t => {
  const { engine, map, ready, sourceReports } = await start();
  t.after(() => engine.dispose());
  engine.setReduced(true);
  engine.show('weather');
  await tick(); await tick();
  map.emit('render');
  assert.equal(ready(), 0, 'a render before the selected style is installed is not readiness');
  map.emit('style.load');
  assert.equal(map.isLoaded, false, 'the source/terrain completion gate deliberately remains pending');
  map.emit('render');
  assert.equal(ready(), 1, 'a completed styled frame is usable without waiting on optional providers');
  assert.ok(sourceReports.at(-1).sources.every(source => source.state === 'loading'), 'source loading is still disclosed');
  assert.ok(!map.log.some(([name]) => name === 'easeTo'), 'reduced motion stays still');
  map.emit('render');
  assert.equal(ready(), 1, 'subsequent frames do not announce duplicate readiness');
});

test('a rejected style installation reports unavailable and remains retryable without leaking its error',async t=>{
 const {engine,map,fetches,sourceReports}=await start();t.after(()=>engine.dispose());
 const install=map.setStyle.bind(map);let reject=true;
 map.setStyle=style=>{if(reject)throw new Error('Private style diagnostic');install(style);};
 engine.show('evidence');await tick();fetches[0].resolve();await tick();await tick();
 assert.equal(sourceReports.at(-1).mapState,'unavailable');
 assert.ok(!JSON.stringify(sourceReports).includes('Private style diagnostic'));
 reject=false;engine.show('evidence');await settle();await tick();
 assert.equal(fetches.length,2,'retry re-reads a rejected style document');
 fetches[1].resolve();await tick();await tick();map.emit('style.load');
 assert.equal(sourceReports.at(-1).mapState,'ready');
 assert.equal(map.log.filter(([name])=>name==='setStyle').length,1);
});

test('context loss hides a rendered preview and a real restored frame recovers it',async t=>{
 const {engine,map,ready,errors,sourceReports}=await start();t.after(()=>engine.dispose());
 engine.show('terrain');await tick();map.emit('style.load');map.emit('render');assert.equal(ready(),1);
 map.emit('webglcontextlost');assert.equal(errors(),1);
 assert.equal(sourceReports.at(-1).mapState,'unavailable','parent status receives context loss');
 engine.setLayersVisible(false);
 assert.equal(sourceReports.at(-1).mapState,'unavailable','source refresh cannot imply a restored renderer');
 map.emit('render');assert.equal(ready(),2,'only a new rendered frame restores visibility');
 assert.equal(sourceReports.at(-1).mapState,'ready','restored frame clears the parent failure status');
});

test('a previewed category draws its starter data with the Explorer renderer, and its GeoJSON when it arrives', async () => {
  const { engine, fetches, map } = await start();
  engine.show('geology'); await tick(); await tick();
  const quakes = fetches.find(f => f.url.startsWith('/api/'));
  assert.equal(quakes.url, '/api/live-context?feed=usgs-earthquakes', 'the same adapter the Explorer reads');
  map.emit('style.load');
  const drawn = () => globalThis.__welcome.drawn;
  assert.deepEqual(drawn().at(-1), { shown: ['usgs-earthquakes'], payloads: [] }, 'drawn as soon as the style loads; every other provider layer hidden');
  quakes.resolve(); await tick(); await tick();
  assert.deepEqual(drawn().at(-1), { shown: ['usgs-earthquakes'], payloads: ['usgs-earthquakes'] }, 'redrawn with its payload');
  engine.show('transport'); await settle();
  assert.deepEqual(drawn().at(-1), { shown: ['kdot-roads'], payloads: ['usgs-earthquakes'] }, 'the same style switches its data in place; tile starters need no payload');
  assert.equal(fetches.filter(f => f.url.startsWith('/api/')).length, 1, 'tile starters make no adapter request');
  engine.dispose();
});

test('the storm preview draws the newest radar scan only while it is current, and reports its time', async () => {
  for (const fresh of [true, false]) {
    const { engine, fetches, map, radarReports } = await start();
    globalThis.__welcome.radarManifest = { frames: ['2026-10-26T16:00:00Z', '2026-10-26T16:04:00Z'] };
    globalThis.__welcome.fresh = () => fresh;
    engine.show('weather'); await tick(); await tick();
    map.emit('style.load');
    fetches.find(f => f.url === '/api/noaa-radar/frames').resolve(); await tick(); await tick(); await tick();
    const last = globalThis.__welcome.drawn.at(-1);
    if (fresh) {
      assert.deepEqual(globalThis.__welcome.radar, ['2026-10-26T16:04:00Z'], 'the newest advertised scan, by its exact time');
      assert.ok(last.shown.includes('nws-radar'));
      assert.deepEqual(radarReports, ['2026-10-26T16:04:00Z'], 'the caption learns the scan time');
      engine.show('geology'); await settle();
      assert.deepEqual(radarReports, ['2026-10-26T16:04:00Z', null], 'and loses it when the next map has no radar');
    } else {
      assert.deepEqual(globalThis.__welcome.radar, [], 'a stale scan list shows no radar');
      assert.ok(!last.shown.includes('nws-radar'));
      assert.deepEqual(radarReports, [], 'and the caption claims none');
    }
    engine.dispose();
  }
});

test('a radar scan that ages past the freshness rule leaves the preview and its caption', async t => {
  t.mock.timers.enable({ apis: ['setInterval'] });
  const { engine, fetches, map, radarReports } = await start();
  const { RADAR_RECHECK_MS } = await loadEngine();
  globalThis.__welcome.radarManifest = { frames: ['2026-10-26T16:00:00Z', '2026-10-26T16:04:00Z'] };
  engine.show('weather'); await tick(); await tick();
  map.emit('style.load');
  fetches.find(f => f.url === '/api/noaa-radar/frames').resolve(); await tick(); await tick(); await tick();
  assert.deepEqual(radarReports, ['2026-10-26T16:04:00Z']);
  // Fifteen minutes later the same scan is no longer current.
  globalThis.__welcome.fresh = () => false;
  t.mock.timers.tick(RADAR_RECHECK_MS); await tick(); await tick(); await tick();
  assert.deepEqual(radarReports, ['2026-10-26T16:04:00Z', null], 'the caption drops the stale scan');
  assert.ok(!globalThis.__welcome.drawn.at(-1).shown.includes('nws-radar'), 'and the radar layer is hidden');
  engine.dispose();
});

test('satellite previews request one checked current frame and preserve its product/time', async () => {
 for (const kind of ['geocolor', 'visible']) {
  const { engine, fetches, map, sourceReports } = await start();
  const frame = { kind, observedAt: new Date().toISOString(), validThrough: null };
  globalThis.__welcome.satelliteManifest = { frames: [frame] };
  engine.show('satellite'); await tick(); await tick();
  assert.equal(fetches.filter(f => f.url === '/api/noaa-satellite/frames').length, 1);
  fetches.find(f => f.url === '/api/noaa-satellite/frames').resolve();
  fetches.find(f => !f.url.startsWith('/api/')).resolve(); await tick(); await tick();
  map.emit('style.load');
  assert.deepEqual(globalThis.__welcome.satellite, [frame]);
  const state = sourceReports.at(-1).sources[0];
  assert.equal(state.state, 'dated-frame'); assert.equal(state.product, kind); assert.equal(state.observedAt, frame.observedAt);
  assert.ok(!globalThis.__welcome.drawn.at(-1).shown.includes('noaa-goes-geocolor'), 'generic undated imagery is never enabled');
  engine.dispose();
 }
});

test('stale satellite imagery is withheld and a paused preview does not poll', async t => {
 t.mock.timers.enable({ apis: ['setInterval'] });
 const { engine, fetches, map, sourceReports } = await start();
 globalThis.__welcome.satelliteManifest = { frames: [{ kind: 'visible', observedAt: '2000-01-01T00:00:00.000Z', validThrough: null }] };
 engine.show('satellite'); await tick(); await tick();
 fetches.find(f => f.url === '/api/noaa-satellite/frames').resolve();
 fetches.find(f => !f.url.startsWith('/api/')).resolve(); await tick(); await tick(); map.emit('style.load');
 assert.deepEqual(globalThis.__welcome.satellite, []);
 assert.equal(sourceReports.at(-1).sources[0].state, 'unavailable');
 const requests = fetches.length;
 t.mock.timers.tick(180000); await tick(); await tick();
 assert.equal(fetches.length, requests, 'holding/hidden state expires data without new network work');
 engine.dispose();
});

test('an empty GeoJSON feed is reported as empty rather than claimed visible observations', async () => {
 const { engine, fetches, map, sourceReports } = await start();
 engine.show('geology'); await tick(); await tick(); map.emit('style.load');
 assert.equal(sourceReports.at(-1).sources[0].state, 'loading');
 fetches.find(f => f.url.startsWith('/api/')).resolve(); await tick(); await tick();
 assert.equal(sourceReports.at(-1).sources[0].state, 'empty');
 assert.equal(sourceReports.at(-1).sources[0].count, 0);
 engine.dispose();
});

test('the People preview draws its counties as population prisms, and the next map does not', async () => {
  const { engine, map } = await start();
  engine.show('people'); await tick(); await tick();
  map.emit('style.load');
  assert.deepEqual(globalThis.__welcome.prisms.at(-1), true, 'prisms asked for before the counties are drawn');
  assert.deepEqual(globalThis.__welcome.drawn.at(-1).shown, ['census-counties']);
  engine.show('geology'); await settle();
  assert.equal(globalThis.__welcome.prisms.at(-1), false, 'a map without the overlay draws flat');
  engine.dispose();
});


test('a failed style is disclosed and the same selected category can retry', async () => {
 const { engine, fetches, map, sourceReports } = await start();
 engine.show('evidence'); await tick();
 fetches[0].fail(); await tick(); await tick();
 assert.equal(sourceReports.at(-1).mapState, 'unavailable');
 engine.show('evidence'); await settle(); await tick();
 assert.equal(fetches.length, 2, 'reselection is not swallowed by the same-topic optimization');
 fetches[1].resolve(); await tick(); await tick(); map.emit('style.load');
 assert.equal(sourceReports.at(-1).mapState, 'ready');
 assert.equal(map.log.filter(([name]) => name === 'setStyle').length, 1);
 engine.dispose();
});


test('pausing an interrupted same-style flight leaves the selected category camera, not an intermediate view', async t => {
 for (const pause of ['setPaused', 'setReduced']) {
 const { engine, map } = await start();
 t.after(() => engine.dispose());
 engine.setPaused(false); engine.show('geology'); await tick(); await tick(); map.emit('style.load');
 engine.show('terrain'); await settle();
 assert.ok(map.log.some(([name]) => name === 'flyTo'));
 engine[pause](true);
 assert.deepEqual(map.camera.center, [-99.6, 38.9]);
 assert.equal(map.camera.zoom, 7.4);
 engine[pause](false);
 assert.deepEqual(map.camera.center, [-99.6, 38.9], 'resuming drift cannot keep the previous category center');
 engine.dispose();
 }
});
