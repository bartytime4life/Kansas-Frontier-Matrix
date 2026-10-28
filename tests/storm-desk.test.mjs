import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import path from 'node:path';
import ts from 'typescript';
import {componentHarness, findNode} from './component-harness.mjs';

// Run the real TS modules against a recording renderer, without provider I/O.
const modules = new Map();
function load(file) {
  file = path.resolve(file);
  if (modules.has(file)) return modules.get(file);
  const exports = {};
  modules.set(file, exports);
  const code = ts.transpileModule(readFileSync(file, 'utf8'), {compilerOptions: {module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022}}).outputText;
  new Function('exports', 'require', code)(exports, name => {
    if (name === './map-layer-composition') return {
      balanceMapFills() {}, balanceMapRasters() {}, composeMapLayers() {}, requestFillOpacity() {}, requestRasterOpacity() {},
    };
    assert.ok(name.startsWith('.'), `Unexpected runtime dependency: ${name}`);
    return load(path.resolve(path.dirname(file), name) + '.ts');
  });
  return exports;
}
const live = load('app/live-context.ts');
const maps = load('app/category-maps.ts');
const topics = load('app/layer-workspaces.ts');
const page = readFileSync('app/page.tsx', 'utf8');
const first = '2026-10-27T12:00:00.000Z', second = '2026-10-27T12:04:00.000Z';

function recordingMap() {
  const sources = new Map(), layers = new Map();
  return {
    sources, layers, tilesChanged: 0, projection: 'mercator',
    getStyle: () => ({layers: [...layers.values()]}),
    getProjection() {return {type: this.projection};},
    getZoom: () => 6,
    getLayer: id => layers.get(id),
    getSource: id => sources.get(id),
    addSource(id, spec) {sources.set(id, {serialize: () => spec, setData() {}, setTiles: tiles => {this.tilesChanged++; spec.tiles = tiles;}});},
    addLayer: layer => layers.set(layer.id, {...layer, layout: {...layer.layout}, paint: {...layer.paint}}),
    getPaintProperty: (id, key) => layers.get(id)?.paint[key],
    setPaintProperty: (id, key, value) => {layers.get(id).paint[key] = value;},
    getLayoutProperty: (id, key) => layers.get(id)?.layout[key],
    setLayoutProperty: (id, key, value) => {layers.get(id).layout[key] = value;},
    eligibleRasters() {return [...layers.values()].filter(l => l.type === 'raster' && l.layout.visibility !== 'none').map(l => l.source);},
  };
}
const radar = live.OFFICIAL_CONTEXT_BY_ID['nws-radar'];
const visibility = on => Object.fromEntries(live.OFFICIAL_CONTEXT_SOURCES.map(s => [s.id, s.id === 'nws-radar' && on]));
const opacity = Object.fromEntries(live.OFFICIAL_CONTEXT_SOURCES.map(s => [s.id, s.defaultOpacity]));

test('radar parks the inactive buffer after commit, including repeated visibility updates', () => {
  const map = recordingMap();
  live.setNoaaRadarObservationTime(map, first);
  live.commitNoaaRadarObservationTime(map, radar.sourceId, true, 0.68);
  assert.deepEqual(map.eligibleRasters(), [radar.sourceId]);
  const staged = live.stageNoaaRadarObservationTime(map, second);
  live.applyOfficialContextState(map, visibility(true), opacity, {});
  assert.equal(map.eligibleRasters().length, 2, 'pending scan remains eligible alongside the last confirmed image');
  assert.equal(map.getPaintProperty(radar.layerIds[0], 'raster-opacity'), 0.68);
  live.commitNoaaRadarObservationTime(map, staged, true, 0.68);
  for (let i = 0; i < 3; i++) live.applyOfficialContextState(map, visibility(true), opacity, {});
  assert.deepEqual(map.eligibleRasters(), [staged], 'one source eligible on subsequent pans, rather than two');
  assert.match(map.getSource(staged).serialize().tiles[0], /time=2026-10-27T12%3A04%3A00\.000Z/);
  const pending = live.stageNoaaRadarObservationTime(map, first);
  assert.notEqual(pending, staged, 'buffers alternate without adding a third source');
  live.discardNoaaRadarStagedFrame(map, pending);
  live.applyOfficialContextState(map, visibility(true), opacity, {});
  assert.deepEqual(map.eligibleRasters(), [staged], 'failed load keeps only the confirmed scan eligible');
  live.applyOfficialContextState(map, visibility(false), opacity, {});
  assert.deepEqual(map.eligibleRasters(), []);
  map.projection = 'globe';
  live.applyOfficialContextState(map, visibility(true), opacity, {});
  assert.deepEqual(map.eligibleRasters(), [], 'Mercator radar stays held on the globe');
});

test('the storm starter pair excludes every optional layer, with related layers discoverable in Weather', () => {
  const look = maps.CATEGORY_MAPS.weather;
  assert.deepEqual(look.starters, ['nws-alerts', 'nws-radar']);
  for (const layer of look.contextLayers) {
    assert.ok(live.OFFICIAL_CONTEXT_BY_ID[layer.id], layer.id);
    assert.ok(!look.starters.includes(layer.id), layer.id);
    assert.ok(topics.officialSourceTopics(layer.id).includes('weather'), layer.id);
  }
  assert.ok(!look.contextLayers.some(l => l.id === 'nasa-lightning-climatology'), 'historical climatology is not presented as current storm context');
});

test('the dock exposes explicit starting and optional switches without toggling on render or disclosure', async () => {
  const h = await componentHarness('app/category-map-dock.tsx', {});
  const calls = [];
  const props = {look: maps.CATEGORY_MAPS.weather, mode: '2d', depth: 1, azimuth: 225, sun: null,
    sunAvailable: false, terrainAvailable: false, sunPlaying: false, motionAllowed: true,
    layerVisibility: {'nws-alerts': true, 'nws-radar': true}, onLayer: (...args) => calls.push(args)};
  let tree = h.render(h.exports.CategoryMapDock, props);
  const details = findNode(tree, n => n.type === 'details' && n.props.className === 'category-map-dock-context');
  assert.equal(details.props.open, undefined, 'optional context starts collapsed');
  assert.deepEqual(calls, [], 'rendering does not fetch or activate a layer');
  const button = title => findNode(tree, n => n.type === 'button' && n.props.children === title);
  assert.equal(button('Latest NOAA radar').props['aria-pressed'], true);
  assert.equal(button('GOES satellite').props['aria-pressed'], false);
  button('GOES satellite').props.onClick();
  assert.deepEqual(calls, [['noaa-goes-geocolor', true]]);
  tree = h.render(h.exports.CategoryMapDock, {...props, layerVisibility: {...props.layerVisibility, 'noaa-goes-geocolor': true}});
  button('GOES satellite').props.onClick();
  button('Latest NOAA radar').props.onClick();
  assert.deepEqual(calls.slice(-2), [['noaa-goes-geocolor', false], ['nws-radar', false]]);
});

// Exercise the actual page callbacks/effect bodies without rendering WebGL.
const ast = ts.createSourceFile('page.tsx', page, ts.ScriptTarget.Latest, true, ts.ScriptKind.TSX);
function callback(name) {
  let found;
  function visit(node) {
    if (ts.isVariableDeclaration(node) && node.name.getText(ast) === name) found = node.initializer.arguments[0].getText(ast);
    ts.forEachChild(node, visit);
  }
  visit(ast);
  assert.ok(found, name);
  return found;
}
function evaluate(source, scope) {
  const js = ts.transpileModule(`const result = ${source};`, {compilerOptions: {target: ts.ScriptTarget.ES2022}}).outputText;
  return new Function(...Object.keys(scope), js + '\nreturn result;')(...Object.values(scope));
}
test('a manifest refresh does not restage a confirmed scan, but style replacement can reload it', () => {
  const currentMap = recordingMap();
  live.setNoaaRadarObservationTime(currentMap, first);
  const ref = current => ({current});
  const manifest = {frames: [first, second]};
  let pending = 0, frameState = 'error', states = {'nws-radar': 'error'}, errors = {'nws-radar': 'Prior frame failed'};
  const scope = {
    noaaRadarManifestRef: ref(manifest), noaaRadarManifestIsFresh: () => true,
    noaaRadarFrameTimeRef: ref(first), noaaRadarReadyRef: ref(true),
    noaaRadarPendingFrameTimeRef: ref(null), mapRef: ref(currentMap), styleGenerationReadyRef: ref(true),
    noaaRadarObservationTimeIsApplied: live.noaaRadarObservationTimeIsApplied,
    setNoaaRadarPendingFrameTime: () => {pending++;}, noaaRadarFrameLoadCleanupRef: ref(null),
    noaaRadarFrameFailureRef: ref(null), setNoaaRadarFrameLoadState: value => {frameState = value;},
    setOfficialStates: update => {states = update(states);}, setOfficialErrors: update => {errors = update(errors);},
  };
  evaluate(callback('applyNoaaRadarFrame'), scope)(first);
  assert.equal(pending, 0, 'confirmed scan bypasses staging entirely');
  assert.equal(currentMap.tilesChanged, 0);
  assert.equal(frameState, 'ready'); assert.equal(states['nws-radar'], 'ready');
  assert.equal(errors['nws-radar'], undefined, 'a successful retry clears a prior error without reloading the scan');
  scope.mapRef.current = null; // Same timestamp must remain pending until the new style exists.
  evaluate(callback('applyNoaaRadarFrame'), scope)(first);
  assert.equal(pending, 1, 'no false cache hit when renderer sources have gone away');
});

test('radar polling suspends while hidden and unregisters its timer and visibility listener', () => {
  let source;
  function visit(node) {
    if (ts.isCallExpression(node) && node.expression.getText(ast) === 'useEffect'
      && node.arguments[0]?.getText(ast).includes('if (!noaaRadarSelectedAtPresent)')) source = node.arguments[0].getText(ast);
    ts.forEachChild(node, visit);
  }
  visit(ast);
  assert.ok(source);
  let refreshes = 0, aborts = 0, interval, listener, cleared = false;
  const document = {hidden: false, addEventListener: (_, fn) => {listener = fn;}, removeEventListener: (_, fn) => {assert.equal(fn, listener); listener = null;}};
  const cleanup = evaluate(source, {
    noaaRadarSelectedAtPresent: true, document,
    refreshNoaaRadarManifest: () => {refreshes++;}, noaaRadarRequestRef: {current: {abort: () => {aborts++;}}},
    window: {setInterval: (fn, delay) => {assert.equal(delay, 240_000); interval = fn; return 7;}, clearInterval: id => {assert.equal(id, 7); cleared = true;}},
  })();
  assert.equal(refreshes, 1);
  document.hidden = true;
  listener(); interval();
  assert.equal(refreshes, 1, 'no hidden-tab manifest polling');
  assert.ok(aborts > 0);
  document.hidden = false; listener();
  assert.equal(refreshes, 2, 'visibility return requests a freshness check');
  cleanup();
  assert.equal(cleared, true); assert.equal(listener, null);
  assert.doesNotMatch(page, /noaaRadarAutoStartRef/, 'page entry and shared views never start radar motion automatically');
});

test('GOES polling follows its own selection, suspends when hidden and releases in-flight work', () => {
  let effect;
  function visit(node) {
    if (ts.isCallExpression(node) && node.expression.getText(ast) === 'useEffect'
      && node.arguments[0]?.getText(ast).includes('if (!noaaSatelliteSelectedAtPresent)')) effect = node;
    ts.forEachChild(node, visit);
  }
  visit(ast);
  assert.ok(effect);
  assert.equal(effect.arguments[1].getText(ast), '[noaaSatelliteSelectedAtPresent, refreshNoaaSatelliteFrames]', 'unrelated switches do not restart polling');
  let refreshes = 0, aborts = 0, interval, listener, clears = 0;
  const request = {current: {abort() {aborts++;}}};
  const document = {hidden: false, addEventListener: (_, fn) => {listener = fn;}, removeEventListener: (_, fn) => {assert.equal(listener, fn); listener = null;}};
  const scope = {noaaSatelliteSelectedAtPresent: true, document, noaaSatelliteRequestRef: request,
    refreshNoaaSatelliteFrames: () => {refreshes++;},
    window: {setInterval: (fn, delay) => {assert.equal(delay, 300_000); interval = fn; return 3;}, clearInterval: id => {assert.equal(id, 3); clears++;}},
  };
  const cleanup = evaluate(effect.arguments[0].getText(ast), scope)();
  assert.equal(refreshes, 1);
  document.hidden = true; listener(); interval(); interval();
  assert.equal(refreshes, 1); assert.equal(aborts, 1); assert.equal(request.current, null);
  document.hidden = false; listener(); assert.equal(refreshes, 2);
  request.current = {abort() {aborts++;}};
  cleanup(); assert.equal(aborts, 2); assert.equal(clears, 1); assert.equal(listener, null);
  evaluate(effect.arguments[0].getText(ast), {...scope, noaaSatelliteSelectedAtPresent: false})();
  assert.equal(refreshes, 2, 'deselected GOES schedules nothing');
});

test('an aborted GOES response cannot select an image after hide or deselection', async () => {
  let resolveBody, selections = 0, fetches = 0;
  const request = {current: null};
  const document = {hidden: true};
  const selected = {current: {'noaa-goes-geocolor': true}};
  const scope = {document, officialVisibilityRef: selected, buildYearCurrentRef: {current: true},
    noaaSatelliteRequestRef: request, temporalQueryRef: {current: {frame: 2026}}, OFFICIAL_CONTEXT_PRESENT_FRAME: 2026,
    AbortController, setOfficialStates() {}, setOfficialErrors() {}, NOAA_SATELLITE_FRAMES_PATH: '/api/noaa-satellite/frames',
    fetch: async () => {fetches++; return {ok: true};}, readBoundedJson: () => new Promise(resolve => {resolveBody = resolve;}),
    isNoaaSatelliteManifest: () => true, selectNoaaSatelliteFrame: () => {selections++;},
  };
  const refresh = evaluate(callback('refreshNoaaSatelliteFrames'), scope);
  await refresh(); assert.equal(fetches, 0, 'hidden callback guard also covers manual refresh');
  document.hidden = false; selected.current['noaa-goes-geocolor'] = false;
  await refresh(); assert.equal(fetches, 0);
  selected.current['noaa-goes-geocolor'] = true;
  const pending = refresh(); await Promise.resolve();
  request.current.abort(); resolveBody({frames: [{observedAt: second}]});
  await pending;
  assert.equal(selections, 0); assert.equal(request.current, null);
});
