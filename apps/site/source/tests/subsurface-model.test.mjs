import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
const urls = new Map();
async function moduleUrl(name) {
  if (urls.has(name)) return urls.get(name);
  let js = ts.transpileModule(await readFile(new URL(`../app/${name}.ts`, import.meta.url), 'utf8'), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
  js = js.replaceAll('from "sunrise-sunset-js"', `from ${JSON.stringify(import.meta.resolve('sunrise-sunset-js'))}`).replaceAll('from "polygon-clipping"', `from ${JSON.stringify(new URL('../node_modules/polygon-clipping/dist/polygon-clipping.esm.js', import.meta.url).href)}`);
  for (const [, dep] of [...js.matchAll(/from "\.\/([a-z-]+)"/g)]) js = js.replaceAll(`from "./${dep}"`, `from "${await moduleUrl(dep)}"`);
  const url = `data:text/javascript;base64,${Buffer.from(js).toString('base64')}`; urls.set(name, url); return url;
}
const m = await import(await moduleUrl('subsurface-model'));
const saved = await import(await moduleUrl('saved-workspaces'));
const reports = await import(await moduleUrl('workspace-model'));
const storage = await import(await moduleUrl('workspace-storage'));
const date = '2026-10-06T00:00:00Z';
const record = (patch = {}) => ({ id: 'wwc5-test', sourceId: 'kgs-wwc5', kind: 'well', name: 'Test well', coordinates: [-95,39], coordinateReference: 'WGS84 display', locationMethod: 'PLSS approximate', sourceUrl: 'https://www.kgs.ku.edu/', sourceTime: '2000-01-01', depthUnit: 'ft', depthReference: 'land-surface', totalDepth: 100, intervals: [{ top: 0, bottom: 10, description: 'sand' }, { top: 20, bottom: 30, description: 'clay' }], ...patch });
const context = () => ({ version: 1, capturedAt: date, anchor: [-95,39], pinned: true, transect: [], depthRange: [0,100], display: 'section', exaggeration: 1, selectedSources: ['kgs-wwc5'], sourceVersions: [{ id: 'kgs-wwc5', title: 'KGS wells', url: 'https://www.kgs.ku.edu/', retrievedAt: date, sourceTime: '2026', limitation: 'Approximate locations', sha256: 'a'.repeat(64) }], recordIds: ['wwc5-test'], records: [record()], coverage: ['Loaded subset only'] });
const workspace = { id: 'test', name: 'Test', savedAt: date, view: { center: [-95,39], zoom: 5, bearing: 0, pitch: 0 }, locationCameraRedacted: false, visibility: {}, opacity: {}, layerOrder: [], year: 2026, basemap: 'standard', projection: 'mercator', selection: null, report: { title: 'Test', scope: 'VIEWPORT', detail: 'STANDARD', layerIds: [], sections: {}, query: '' } };
const snapshot = { id: 'test', createdAt: date, area: { kind: 'viewport', label: 'Kansas' }, camera: workspace.view, representation: '2D', projection: 'mercator', basemap: 'standard', committedTime: { start: 2026, end: 2026, label: '2026', mode: 'instant' }, visibleLayers: [], selection: null, evidenceRefs: [], inspectableRecordCount: 0, sourceBackedCount: 0, boundedCount: 0, policy: reports.policyDecisionFromEvidenceState('MISSING_EVIDENCE') };

test('depth conversion preserves drilling reference; radar requires published velocity', () => {
  assert.equal(m.meters(100, 'ft'), 30.48); assert.equal(m.meters(12, 'm'), 12);
  assert.equal(m.radarDepth(100), null); assert.equal(m.radarDepth(100, .1), 5); assert.equal(m.radarDepth(100, .4), null);
  for (const args of [['drilled-depth',true,true],['unknown',true,true],['land-surface',false,true],['land-surface',true,false]]) assert.equal(m.canPlaceInGeologicalModel(...args),false);
  assert.equal(m.canPlaceInGeologicalModel('land-surface',true,true),true);
});
test('coordinates, source links, missing units, invalid intervals and giant records fail validation', () => {
  assert.equal(m.validBorehole(record()), true);
  for (const patch of [{coordinates:null},{coordinates:[NaN,39]},{coordinates:[-120,39]},{sourceUrl:'javascript:alert(1)'},{sourceUrl:'https://user:password@example.org'},{depthUnit:'feet'},{intervals:[{top:20,bottom:10,description:'bad'}]},{intervals:[{top:-1,bottom:10,description:'bad'}]}]) assert.equal(m.validBorehole(record(patch)),false);
});
test('gaps and overlaps remain explicit and records never become seams', () => {
  assert.deepEqual(m.intervalIssues([{top:5,bottom:20},{top:15,bottom:30},{top:40,bottom:50}]),{gaps:[[0,5],[30,40]],overlaps:[[15,20]]});
  assert.equal(m.validBorehole(record({intervals:[{top:0,bottom:30,description:'a'},{top:20,bottom:40,description:'b'}]})),true);
});
test('great-circle offsets clamp to endpoints and tolerate zero-length segments', () => {
  const route=[[-96,39],[-95,39]];
  const center=m.sectionOffset([-95.5,39],route);
  assert.ok(Math.abs(center.alongMeters-m.distanceMeters(...route)/2)<1);
  assert.ok(center.offsetMeters < 130); // Geographic parallel is slightly south of the great-circle arc.
  const end=m.sectionOffset([-94.9,39],route);assert.equal(end.alongMeters,m.distanceMeters(...route));assert.ok(end.offsetMeters>8000);
  assert.deepEqual(m.sectionOffset([-95,39],[[-95,39],[-95,39],[-94.9,39]]),{alongMeters:0,offsetMeters:0});
});
test('radius boundary, identity deduplication and tied ordering are deterministic', () => {
  const a=record({id:'a',coordinates:[-95,39.1]}), b=record({id:'b',coordinates:[-95,39.1]});
  const radius=m.distanceMeters([-95,39],a.coordinates);
  assert.deepEqual(m.nearbyColumns([b,a,a],[-95,39],[],radius).map(r=>r.record.id),['a','b']);
  assert.equal(m.nearbyColumns([a],[-95,39],[],radius-.001).length,0);
});
test('saved context validation is bounded; redaction removes coordinates, lines, identities and images', () => {
  const c=context();assert.equal(m.validSubsurfaceContext(c),true);
  for(const patch of [{records:[...c.records,...c.records]},{depthRange:[100,0]},{transect:[[100,0]]},{exaggeration:0},{sourceVersions:[{...c.sourceVersions[0],sha256:'bad'}]}]) assert.equal(m.validSubsurfaceContext({...c,...patch}),false);
  assert.equal(m.persistableSubsurface(c,true),undefined);assert.equal(m.sectionSvg(c,true),null);assert.equal(m.intervalCsv(c,true),null);
  const settings=m.persistableSubsurface(c,false,true);assert.equal(settings.records.length,0);assert.deepEqual(settings.recordIds,c.recordIds);assert.equal(m.validSubsurfaceContext(settings),true);
});
test('old saves remain readable; underground contexts require explicit non-redacted storage', () => {
  assert.equal(saved.validSavedWorkspaceRecord(workspace),true);
  assert.equal(saved.validSavedWorkspaceRecord({...workspace,subsurfaceContext:context()}),true);
  assert.equal(saved.validSavedWorkspaceRecord({...workspace,locationCameraRedacted:true,subsurfaceContext:context()}),false);
  assert.equal(saved.validSavedWorkspaceRecord({...workspace,locationCameraRedacted:undefined,subsurfaceContext:context()}),false);
  assert.equal(saved.writeSavedWorkspaceList({setItem(){throw new Error('quota');}},'test',[workspace]),false);
});
test('report capture is separate from included evidence and obeys location redaction', () => {
  const report=reports.createReportDraft(snapshot,[],undefined,undefined,context());assert.equal(report.includedEvidenceIds.length,0);assert.ok(report.subsurfaceContext);assert.equal(storage.validReportDraft(report),true);
  const privateSnapshot={...snapshot,camera:{center:'WITHHELD_BROWSER_LOCATION',zoom:'WITHHELD',bearing:'WITHHELD',pitch:'WITHHELD'}};
  assert.equal(reports.createReportDraft(privateSnapshot,[],undefined,undefined,context()).subsurfaceContext,undefined);
  assert.equal(storage.validReportDraft({...report,snapshot:privateSnapshot}),false);
});
test('source-labelled exports escape SVG markup and spreadsheet formulas', () => {
  const c=context();c.records[0].intervals[0].description='=HYPERLINK("unsafe") <script>bad</script>';
  const csv=m.intervalCsv(c);assert.ok(csv.includes('source_url'));assert.ok(csv.includes("'=HYPERLINK"));assert.ok(csv.includes('https://www.kgs.ku.edu/'));
  const svg=m.sectionSvg(c);assert.ok(!svg.includes('<script>'));assert.ok(svg.includes('&lt;script&gt;'));assert.ok(svg.includes('Unknown between observations'));
  assert.ok(m.subsurfaceMarkdown(c).includes('separate from included evidence'));
});
