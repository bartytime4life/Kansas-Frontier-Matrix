import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';
import { componentHarness, findNode } from './component-harness.mjs';
const code = ts.transpileModule(await readFile('app/river-pulse-visuals.ts', 'utf8'), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const { riverSignalGroups, nearestRiverSample } = await import(`data:text/javascript;base64,${Buffer.from(code).toString('base64')}`);

test('network segments partition gauges without counting zero as flowing or stale as measured', () => {
  const values = [{ value: 5, trend: 'rising' }, { value: 3, trend: 'falling' }, { value: 9, trend: 'steady' }, { value: 2, trend: 'unknown' }, { value: 0, trend: 'falling' }, { value: 4, missing: true, trend: 'rising' }, { value: null }];
  const groups = riverSignalGroups({ features: values.map((properties, i) => ({ properties: { ...properties, stationId: String(i) } })) });
  assert.deepEqual(groups.map(g => g.stations.length), [1, 1, 1, 1, 1, 2]);
  assert.equal(new Set(groups.flatMap(g => g.stations)).size, values.length);
  assert.ok(riverSignalGroups(null).every(g => g.stations.length === 0));
});

test('sample inspection chooses actual nulls and boundaries without interpolation', () => {
  const values = [0, 15, 60].map((minute, i) => ({ observedAt: new Date(Date.UTC(2026, 9, 4, 0, minute)).toISOString(), value: i === 1 ? null : i }));
  const origin = Date.parse(values[0].observedAt);
  assert.equal(nearestRiverSample(values, origin + 15 * 60000), 1);
  assert.equal(nearestRiverSample(values, origin + 30 * 60000), 1);
  assert.equal(nearestRiverSample(values, origin - 60000), 0);
  assert.equal(nearestRiverSample(values, origin + 100 * 60000), 2);
  assert.equal(nearestRiverSample([], origin), -1);
  assert.equal(nearestRiverSample(values, NaN), -1);
});

const moduleUrl = source => `data:text/javascript;base64,${Buffer.from(ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText).toString('base64')}`;
const moduleFor = async (file, replacements = {}) => {
  let source = await readFile(file, 'utf8');
  for (const [name, url] of Object.entries(replacements)) source = source.replaceAll(`"${name}"`, JSON.stringify(url));
  return import(moduleUrl(source));
};
const streamflow = await moduleFor('app/streamflow.ts');
const waterContext = await moduleFor('app/water-flow-context.ts', {
  './water-flow-motion': moduleUrl(await readFile('app/water-flow-motion.ts', 'utf8')),
});
const riverVisuals = { riverSignalGroups, nearestRiverSample };
const harnessFor = () => componentHarness('app/hydrology-observatory.tsx', {
  './river-network-signal': { RiverNetworkSignal: 'river-network-signal' },
  './river-pulse-visuals': riverVisuals,
  './water-terrain-profile': { WaterTerrainProfile: 'water-terrain-profile' },
  './water-flow-context': waterContext,
  './streamflow': streamflow,
});
const emptyProps = onClose => ({
  bundle: null, state: 'idle', error: null, frame: null, frameIndex: 0, playing: false,
  speed: 1, range: '24h', selectedStationId: null, reducedMotion: false,
  downstreamState: 'idle', downstreamPathCount: 0, onClose,
  onRefresh() {}, onTogglePlay() {}, onStep() {}, onSeek() {}, onJumpLatest() {},
  onSpeed() {}, onRange() {}, onSelectStation() {}, onShowDirection() {},
});

test('River Pulse always offers a named enabled close button, including loading and unavailable states', async () => {
  const h = await harnessFor();
  let closed = 0;
  for (const state of ['idle', 'loading', 'ready', 'partial', 'empty', 'stale', 'error']) {
    const tree = h.render(h.exports.HydrologyObservatory, { ...emptyProps(() => closed++), state });
    const close = findNode(tree, node => node.type === 'button' && node.props['aria-label'] === 'Close River Pulse');
    assert.ok(close, state);
    assert.equal(close.props.type, 'button');
    assert.ok(!close.props.disabled, state);
    assert.ok(findNode(tree, node => node.type === 'header' && findNode(node, child => child === close)));
    close.props.onClick();
  }
  assert.equal(closed, 7);
});

test('Escape dismisses from any panel control without leaking to the map; playback keys stay local', async () => {
  const h = await harnessFor();
  let closed = 0, toggled = 0;
  const props = { ...emptyProps(() => closed++), state: 'ready', frameTimes: ['2026-10-22T00:00:00Z', '2026-10-22T00:15:00Z'], onTogglePlay: () => toggled++ };
  const tree = h.render(h.exports.HydrologyObservatory, props);
  for (const target of [tree, { type: 'button' }, { type: 'select' }, { type: 'input' }]) {
    let prevented = false, stopped = false;
    tree.props.onKeyDown({ key: 'Escape', target, currentTarget: tree, preventDefault: () => prevented = true, stopPropagation: () => stopped = true });
    assert.equal(prevented, true); assert.equal(stopped, true);
  }
  assert.equal(closed, 4);
  tree.props.onKeyDown({ key: ' ', target: {}, currentTarget: tree, preventDefault: () => assert.fail('child control owns Space') });
  assert.equal(toggled, 0);
  tree.props.onKeyDown({ key: ' ', target: tree, currentTarget: tree, preventDefault() {} });
  assert.equal(toggled, 1);
});

test('the wired dismiss action hides controls, pauses all live playback and returns map focus without changing observations', async () => {
  const source = await readFile('app/page.tsx', 'utf8');
  const ast = ts.createSourceFile('page.tsx', source, ts.ScriptTarget.ES2022, true, ts.ScriptKind.TSX);
  let callback, closeAttribute;
  function visit(node) {
    if (ts.isVariableDeclaration(node) && node.name.getText(ast) === 'closeLiveInstrument') callback = node.initializer.arguments[0].getText(ast);
    if (ts.isJsxSelfClosingElement(node) && node.tagName.getText(ast) === 'HydrologyObservatory') closeAttribute = node.attributes.properties.find(attr => attr.name?.getText(ast) === 'onClose')?.initializer?.expression?.getText(ast);
    ts.forEachChild(node, visit);
  }
  visit(ast);
  assert.equal(closeAttribute, 'closeLiveInstrument');
  assert.ok(callback);
  const mutations = [], frames = [];
  const names = ['setInstrumentOpen', 'setStreamflowPlaying', 'setNoaaRadarPlaying', 'setLightningPlaying'];
  const run = new Function(...names, 'window', 'mapContainerRef', `return (${ts.transpileModule(callback, { compilerOptions: { target: ts.ScriptTarget.ES2022 } }).outputText.trim().replace(/;$/, '')})`)(
    ...names.map(name => value => mutations.push([name, value])),
    { requestAnimationFrame: fn => frames.push(fn) },
    { current: { focus: options => mutations.push(['focus', options.preventScroll]) } },
  );
  run();
  assert.deepEqual(mutations, names.map(name => [name, false]));
  assert.equal(frames.length, 1);
  frames[0]();
  assert.deepEqual(mutations.at(-1), ['focus', true]);
});

test('map Escape cancels an active measurement before dismissing live controls or evidence', async () => {
  const source=await readFile('app/page.tsx','utf8');
  const ast=ts.createSourceFile('page.tsx',source,ts.ScriptTarget.ES2022,true,ts.ScriptKind.TSX);
  let handler;
  function visit(node) {
    if(ts.isVariableDeclaration(node) && node.name.getText(ast)==='handleEscape') handler=node.initializer.getText(ast);
    ts.forEachChild(node,visit);
  }
  visit(ast);assert.ok(handler);
  const calls=[];
  const scope={repositoryOpen:false,workspaceDetailsRef:{current:null},sourceStatusOpen:false,qwenOpen:false,mapContextOpen:false,helpOpen:false,mapUtilityOpen:false,
    liveDockVisible:true,glmFlashesEnabled:false,isCompact:false,rightOpen:true,
    measureModeRef:{current:'distance'},measurementGeometryModeRef:{current:'distance'},measureCoordinatesRef:{current:[[0,0]]},
    mapRef:{current:{doubleClickZoom:{enable:()=>calls.push('zoom enabled')},isStyleLoaded:()=>false}},
    setMeasureCoordinateCount:value=>calls.push(['count',value]),setMeasureMode:value=>calls.push(['mode',value]),
    setMeasurementGeometryMode:value=>calls.push(['geometry',value]),setMeasurement:value=>calls.push(['message',value]),
    closeLiveInstrument:()=>calls.push('dock dismissed'),closeRightPanel:()=>calls.push('evidence dismissed'),
  };
  const javascript=ts.transpileModule(handler,{compilerOptions:{target:ts.ScriptTarget.ES2022}}).outputText.trim().replace(/;$/,'');
  const run=new Function('scope',`with(scope){return (${javascript})}`)(scope);
  const event={key:'Escape',defaultPrevented:false,target:{closest:()=>null}};
  run(event);
  assert.equal(scope.measureModeRef.current,null);assert.equal(scope.measurementGeometryModeRef.current,null);
  assert.deepEqual(scope.measureCoordinatesRef.current,[]);assert.ok(calls.includes('zoom enabled'));
  assert.ok(!calls.includes('dock dismissed'));assert.ok(!calls.includes('evidence dismissed'));
  run(event);assert.equal(calls.at(-1),'dock dismissed');assert.ok(!calls.includes('evidence dismissed'));
});


test('map display changes only presentation and keeps source measurements and selection intact', () => {
  const feature = { type: 'Feature', geometry: { type: 'Point', coordinates: [-98, 38] }, properties: { stationId: 'gauge', value: 0, missing: false, observedAt: '2026-10-23T00:00:00Z', trend: 'steady' } };
  const frame = { type: 'FeatureCollection', features: [feature] };
  const bundle = { retrievedAt: '2026-10-23T00:05:00Z', observations: [{}], state: 'ready', source: {}, limitation: 'context', truncated: false };
  const quiet = streamflow.streamflowContextPayload(bundle, frame, '2026-10-23T00:00:00Z', 'gauge');
  const conditions = streamflow.streamflowContextPayload(bundle, frame, '2026-10-23T00:00:00Z', 'gauge', 'conditions');
  assert.equal(quiet.data.features[0].properties.gaugeConditions, false);
  assert.equal(conditions.data.features[0].properties.gaugeConditions, true);
  assert.equal(quiet.data.features[0].properties.selected, true);
  const stripDisplay = payload => { const properties = { ...payload.data.features[0].properties }; delete properties.gaugeConditions; return properties; };
  assert.deepEqual(stripDisplay(quiet), stripDisplay(conditions));
  assert.equal(feature.properties.gaugeConditions, undefined);
  assert.equal(streamflow.streamflowContextPayload(bundle, null, null, 'gauge').featureCount, 0);
});

test('presentation controls announce their state and do not seek or select a station', async () => {
  const h = await harnessFor();
  const changes = [];
  const props = { ...emptyProps(() => {}), mapDisplay: 'rivers', onMapDisplay: mode => changes.push(mode), onSeek: () => assert.fail('no seek'), onSelectStation: () => assert.fail('no station change') };
  const tree = h.render(h.exports.HydrologyObservatory, props);
  const group = findNode(tree, node => node.props?.['aria-label'] === 'River Pulse map display');
  const rivers = findNode(group, node => node.type === 'button' && node.props['aria-pressed'] === true);
  const conditions = findNode(group, node => node.type === 'button' && node.props['aria-pressed'] === false);
  assert.ok(rivers); assert.ok(conditions);
  conditions.props.onClick(); rivers.props.onClick();
  assert.deepEqual(changes, ['conditions', 'rivers']);
  const details = findNode(tree, node => node.type === 'details' && node.props.className === 'river-network-details');
  assert.ok(details); assert.ok(!details.props.open);
});
