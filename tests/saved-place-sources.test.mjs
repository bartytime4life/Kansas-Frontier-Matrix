import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';

const page = ts.createSourceFile('page.tsx', await readFile('app/page.tsx', 'utf8'), ts.ScriptTarget.ES2022, true, ts.ScriptKind.TSX);
const callbacks = new Map();
function visit(node) {
  if (ts.isVariableDeclaration(node) && node.initializer) {
    if (ts.isArrowFunction(node.initializer)) callbacks.set(node.name.getText(page), node.initializer);
    else if (ts.isCallExpression(node.initializer) && node.initializer.expression.getText(page) === 'useCallback') callbacks.set(node.name.getText(page), node.initializer.arguments[0]);
  }
  ts.forEachChild(node, visit);
}
visit(page);
const sources = [{ id: 'usgs-streamflow', defaultOpacity: .92 }, { id: 'nws-radar', defaultOpacity: .7 }];
const visibility = { 'usgs-streamflow': true, 'nws-radar': false };
const opacity = { 'usgs-streamflow': .37, 'nws-radar': .61 };
const view = { center: [-98, 38], zoom: 6, bearing: 0, pitch: 0 };
const report = { title: 'Saved view', scope: 'VIEWPORT', detail: 'STANDARD', layerIds: [], sections: {}, query: '', evidenceFilter: 'ALL' };
const base = { id: 'place', name: 'River view', savedAt: '2026-10-31T22:00:00Z', view, locationCameraRedacted: false, visibility: {}, opacity: {}, layerOrder: [], year: 2026, basemap: 'standard', projection: 'mercator', report, selection: null };
const trail = await import('data:text/javascript;base64,' + Buffer.from(ts.transpileModule(await readFile('app/places-trail.ts', 'utf8'), {compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText).toString('base64'));

function handler(name, extra = {}) {
  const node = callbacks.get(name);
  assert.ok(node, `execute the actual ${name} handler`);
  const state = {}, calls = [];
  const scope = {
    ...trail,stopPlaceTour(){},
    stopSceneOrbit(){}, LAYER_REGISTRY: [], defaultOrder: [], KNOWN_TEMPORAL_FRAMES: new Set([2026]), OFFICIAL_CONTEXT_PRESENT_FRAME: 2026,
    isBasemapKey: () => true, clamp: (n, min, max) => Math.max(min, Math.min(max, n)), evidenceLabels: {}, TIME_STEPS: [2026],
    defaultReportSections: {}, validSubsurfaceContext: () => false, validResearchContext: value => Boolean(value), isCompact: false,
    OFFICIAL_CONTEXT_SOURCES: sources, officialVisibilityRef: { current: { 'usgs-streamflow': false, 'nws-radar': true } }, officialOpacityRef: { current: { 'usgs-streamflow': .92, 'nws-radar': .7 } }, officialPayloadsRef: { current: {} },
    setOfficialContextVisible: (id, value) => calls.push(['visible', id, value]), setOfficialContextOpacity: (id, value) => calls.push(['opacity', id, value]),
    retryOfficialLayer: id => calls.push(['refresh', id]), announce: message => calls.push(['announce', message]),
  };
  // Supply React setters and refs, while running the complete production handler.
  function bindings(n) {
    if (ts.isCallExpression(n) && ts.isIdentifier(n.expression) && /^set[A-Z]/.test(n.expression.text) && !(n.expression.text in scope)) {
      const key = n.expression.text; scope[key] = value => { state[key] = typeof value === 'function' ? value(state[key] ?? 0) : value; };
    }
    if (ts.isPropertyAccessExpression(n) && n.name.text === 'current' && ts.isIdentifier(n.expression) && !(n.expression.text in scope)) scope[n.expression.text] = { current: null };
    ts.forEachChild(n, bindings);
  }
  bindings(node); Object.assign(scope, extra);
  const js = ts.transpileModule(`return ${node.getText(page)};`, { compilerOptions: { target: ts.ScriptTarget.ES2022 } }).outputText;
  return { run: new Function(...Object.keys(scope), js)(...Object.values(scope)), state, calls };
}

test('saving a place copies official source settings without retaining observation responses', () => {
  let captured;
  const h = handler('saveCurrentWorkspace', {
    locationCameraRedacted: false, researchLocationRedacted: false, subsurfacePrivate: false, researchOpen: false, workspaceName: 'River view', savedWorkspaces: [],
    normalizePlaceStopName: name => name, view, researchContext: null, subsurfaceContext: null, persistableResearch: () => undefined, persistableSubsurface: () => undefined,
    visibility: {}, opacity: {}, officialVisibility: visibility, officialOpacity: opacity, layerOrder: [], year: 2026, mapEvidenceFilter: 'ALL', basemap: 'standard', projection: 'mercator',
    scenePreset: 'overview-2d', verticalExaggeration: 1, atmospherePreset: 'clear', lightAzimuth: 210, fieldOfView: 36,
    measurementGeometryMode: null, analysisArea: null, compareTimeA: 2026, compareTimeB: 2026, temporalMode: 'snapshot', temporalStepRule: 'regular-calendar', sweepRangeStart: 2026, sweepRangeEnd: 2026,
    movingWindowFrames: 3, playbackDirection: 'forward', playbackLoopMode: 'stop', reportTitle: report.title, reportScope: report.scope, reportDetail: report.detail,
    reportLayerIds: [], reportSections: {}, reportQuery: '', reportEvidenceFilter: 'ALL', selected: null,
    persistSavedWorkspaces: records => { captured = records[0]; return true; },
  });
  h.run();
  assert.deepEqual(captured.officialContext, { visibility, opacity });
  assert.notEqual(captured.officialContext.visibility, visibility);
  assert.notEqual(captured.officialContext.opacity, opacity);
  assert.deepEqual(Object.keys(captured.officialContext).sort(), ['opacity', 'visibility']);
  assert.equal(h.state.setRemovedPlace,null,'a successful addition ends the preceding removal undo');
});

test('every save entry refuses a thirteenth place before capturing or writing anything',()=>{
 const records=Array.from({length:12},(_,i)=>({...base,id:`place-${i}`}));
 const h=handler('saveCurrentWorkspace',{savedWorkspaces:records,persistSavedWorkspaces(){assert.fail('must not evict an existing place');}});h.run();
 assert.equal(h.state.setWorkspaceName,undefined);assert.equal(h.state.setActivePlaceId,undefined);assert.equal(h.state.setRemovedPlace,undefined);
 assert.equal(h.state.setPlaceNotice,trail.PLACES_FULL_MESSAGE);assert.match(h.calls[0][1],/Remove a saved place/);
});

test('persistence refuses over-capacity input without truncation or storage access',()=>{
 const h=handler('persistSavedWorkspaces',{window:{get localStorage(){assert.fail('capacity must be checked first');}}});
 assert.equal(h.run(Array(13).fill(base)),false);assert.equal(h.state.setSavedWorkspaces,undefined);assert.equal(h.state.setPlaceNotice,trail.PLACES_FULL_MESSAGE);
});

test('storage failure keeps the saved list and exposes persistent recovery feedback',()=>{
 const h=handler('persistSavedWorkspaces',{window:{localStorage:{}},WORKSPACE_STORAGE_KEY:'places',writeSavedWorkspaceList:()=>false});
 assert.equal(h.run([base]),false);assert.equal(h.state.setSavedWorkspaces,undefined);assert.match(h.state.setPlaceNotice,/existing places are unchanged/);
});

test('removal and undo restore the same record at its original position in either control surface',()=>{
 for(const context of ['places','workspace']){
  const records=['a','b','c'].map(id=>({...base,id,name:`Place ${id}`}));let current=records;
  const persistSavedWorkspaces=next=>{current=next;return true;};
  const remove=handler('deleteSavedWorkspace',{savedWorkspaces:records,activePlaceId:'b',persistSavedWorkspaces});remove.run(records[1],context);
  assert.deepEqual(current.map(x=>x.id),['a','c']);assert.equal(remove.state.setRemovedPlace.snapshot,records[1]);assert.equal(remove.state.setRemovedPlace.index,1);
  assert.equal(remove.state.setActivePlaceId,null);assert.equal(remove.state.setPlaceFocus.context,context);assert.equal(remove.state.setPlaceFocus.target,'undo');
  const undo=handler('undoRemovedPlace',{savedWorkspaces:current,removedPlace:remove.state.setRemovedPlace,activePlaceId:null,persistSavedWorkspaces});undo.run(context);
  assert.deepEqual(current,records);assert.equal(current[1],records[1]);assert.equal(undo.state.setActivePlaceId,'b');assert.equal(undo.state.setRemovedPlace,null);assert.equal(undo.state.setPlaceFocus.target,'name');
 }
});

test('failed removal and failed undo retain recovery state, and retry preserves a different active place',()=>{
 const records=['a','b'].map(id=>({...base,id}));
 const remove=handler('deleteSavedWorkspace',{savedWorkspaces:records,activePlaceId:'a',persistSavedWorkspaces:()=>false});remove.run(records[0]);
 assert.equal(remove.state.setRemovedPlace,undefined);assert.equal(remove.state.setPlaceFocus,undefined);assert.equal(remove.state.setActivePlaceId,undefined);
 let fail=true,current=[records[1]];
 const undo=handler('undoRemovedPlace',{savedWorkspaces:current,removedPlace:{snapshot:records[0],index:0,wasActive:true},activePlaceId:'b',persistSavedWorkspaces:next=>{if(fail)return false;current=next;return true;}});
 undo.run('places');assert.equal(undo.state.setRemovedPlace,undefined);assert.equal(undo.state.setPlaceFocus,undefined);assert.equal(undo.state.setActivePlaceId,undefined);
 fail=false;undo.run('places');assert.deepEqual(current,records);assert.equal(undo.state.setActivePlaceId,undefined,'undo does not replace a subsequently selected place');
});

test('reordering clears removal undo only after a successful write',()=>{
 const records=['a','b'].map(id=>({...base,id}));
 for(const succeeds of [false,true]){
  const h=handler('reorderSavedWorkspace',{savedWorkspaces:records,persistSavedWorkspaces:()=>succeeds});h.run(records[0],1);
  assert.equal(h.state.setRemovedPlace,succeeds?null:undefined);
 }
});

test('undo cannot evict another stop or duplicate an existing identity',()=>{
 const records=Array.from({length:12},(_,i)=>({...base,id:`place-${i}`})),original=[...records];
 assert.equal(trail.restorePlaceStop(records,{...base,id:'missing'},4),null);assert.deepEqual(records,original);
 assert.equal(trail.restorePlaceStop(records.slice(0,2),records[0],0),null);
 assert.equal(trail.restorePlaceStop([],base,-1),null);
 assert.deepEqual(trail.restorePlaceStop(records.slice(0,1),records[1],10),records.slice(0,2));
});

test('restoring a place applies known official selections and opacity through their existing owners', () => {
  const h = handler('loadSavedWorkspace');
  h.run({ ...base, officialContext: { visibility: { ...visibility, 'retired-source': true }, opacity: { ...opacity, 'retired-source': .1 } } });
  assert.deepEqual(h.calls.filter(c => c[0] !== 'announce'), [
    ['opacity', 'usgs-streamflow', .37], ['visible', 'usgs-streamflow', true],
    ['opacity', 'nws-radar', .61], ['visible', 'nws-radar', false],
  ]);
});

test('legacy places preserve current official settings and legacy research still restores its coverage', () => {
  const h = handler('loadSavedWorkspace'); h.run(base);
  assert.deepEqual(h.calls.filter(c => c[0] !== 'announce'), []);
  const research = { coverage: [{ sourceId: 'usgs-streamflow' }] };
  const legacy = handler('loadSavedWorkspace'); legacy.run({ ...base, researchContext: research });
  assert.deepEqual(legacy.calls.filter(c => c[0] === 'visible'), [['visible', 'usgs-streamflow', true], ['visible', 'nws-radar', false]]);
  const current = handler('loadSavedWorkspace');
  current.run({ ...base, researchContext: research, officialContext: { visibility: { 'usgs-streamflow': false, 'nws-radar': true }, opacity } });
  assert.deepEqual(current.calls.filter(c => c[0] === 'visible'), [], 'an explicit saved selection takes precedence over the research coverage list');
});

test('missing source opacity uses defaults and finite out-of-range values are bounded', () => {
  const owner = handler('setOfficialContextOpacity');
  const h = handler('loadSavedWorkspace', { officialOpacityRef: { current: {} }, setOfficialContextOpacity: owner.run });
  h.run({ ...base, officialContext: { visibility, opacity: { 'usgs-streamflow': 8 } } });
  assert.deepEqual(owner.state.setOfficialOpacity, { 'usgs-streamflow': 1, 'nws-radar': .7 });
});
