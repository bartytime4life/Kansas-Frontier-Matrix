import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';
const page = await readFile('app/page.tsx', 'utf8'), ast = ts.createSourceFile('page.tsx', page, ts.ScriptTarget.ES2022, true, ts.ScriptKind.TSX);
const callbacks = new Map();
const declarations = new Map();
function visit(node) {
  if (ts.isVariableDeclaration(node) && node.initializer) {
    declarations.set(node.name.getText(ast), node.initializer.getText(ast));
    const init = node.initializer;
    if (ts.isArrowFunction(init)) callbacks.set(node.name.getText(ast), init.getText(ast));
    else if (ts.isCallExpression(init) && init.expression.getText(ast) === 'useCallback') callbacks.set(node.name.getText(ast), init.arguments[0].getText(ast));
  }
  ts.forEachChild(node, visit);
}
visit(ast);
function execute(name, scope) {
  assert.ok(callbacks.has(name));
  const js = ts.transpileModule(`return ${callbacks.get(name)};`, { compilerOptions: { target: ts.ScriptTarget.ES2022 } }).outputText;
  return new Function(...Object.keys(scope), js)(...Object.values(scope));
}
function harness(day = '2024-09-02') {
  const reads = [], owner = { current: day }, source = { kind: 'OBSERVATIONS' };
  const scope = { streamflowArchiveDayRef: owner, streamflowRange: '1y', streamflowSelectedStationId: 'USGS-06864500', refreshStreamflow: (...args) => { reads.push(args); return Promise.resolve(); },
    OFFICIAL_CONTEXT_BY_ID: { 'usgs-streamflow': source }, setLiveInstrument: () => {}, setStreamflowPlaying: () => {},
    officialVisibilityRef: { current: {} }, setOfficialVisibility: () => {}, streamflowBundleRef: { current: null }, mapRef: { current: null } };
  scope.refreshSelectedStreamflow = execute('refreshSelectedStreamflow', scope);
  return { reads, owner, scope };
}
test('Retry layer and ordinary refresh retain committed station/day even when the last successful range was longer', () => {
  const h = harness(), retry = execute('retryOfficialLayer', h.scope);
  retry('usgs-streamflow');
  assert.deepEqual(h.reads, [['24h', 'USGS-06864500', false, '2024-09-02']]);
  h.owner.current = '2024-09-03'; h.scope.refreshSelectedStreamflow(true);
  assert.deepEqual(h.reads.at(-1), ['24h', 'USGS-06864500', true, '2024-09-03'], 'read latest committed owner at action time, never the editable draft');
  h.owner.current = null; retry('usgs-streamflow');
  assert.deepEqual(h.reads.at(-1), ['1y', 'USGS-06864500', false, null], 'non-archive history keeps its existing range');
});

test('history projection retains the committed archive while hidden and rejects unbound or forged restored days', async () => {
  const compiled = ts.transpileModule(await readFile('app/streamflow.ts', 'utf8'), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
  const { restoreStreamflowArchiveDay } = await import(`data:text/javascript;base64,${Buffer.from(compiled).toString('base64')}`);
  const start = page.indexOf('    params.set("hydroRange", streamflowRange);'), end = page.indexOf('    if (officialVisibility["usgs-streamflow"] ||', start);
  assert.ok(start > 0 && end > start);
  const project = new Function('params', 'streamflowRange', 'streamflowPlaybackSpeed', 'streamflowFrameTime', 'streamflowSelectedStationId', 'streamflowArchiveDay', page.slice(start, end));
  const params = new URLSearchParams();
  project(params, '24h', 1, '2024-09-02T23:45:00Z', 'USGS-06864500', '2024-09-02');
  assert.equal(params.get('hydroDay'), '2024-09-02'); assert.equal(params.get('hydroStation'), 'USGS-06864500');
  const restore = new Function('params', 'normalizedHydroStation', 'currentUtcDay', 'restoreStreamflowArchiveDay', `return ${declarations.get('restoredHydroDay')};`);
  assert.equal(restore(params, 'USGS-06864500', () => '2026-10-11', restoreStreamflowArchiveDay), '2024-09-02');
  for (const day of ['2024-02-30', '2026-10-12', '1799-12-31', '2024-09-02T00:00Z']) {
    params.set('hydroDay', day); assert.equal(restore(params, 'USGS-06864500', () => '2026-10-11', restoreStreamflowArchiveDay), null);
  }
  assert.equal(restoreStreamflowArchiveDay('2024-09-02', null, '2026-10-11'), null);
  assert.equal(restoreStreamflowArchiveDay('2024-09-02', '../other', '2026-10-11'), null);
  const current = new URLSearchParams(); project(current, '24h', 1, null, null, null);
  assert.equal(current.has('hydroDay'), false, 'Recent network cannot resurrect the previous archive');
});
test('hide/show after a failed archive resumes that same day without refetching an already loaded bundle', () => {
  const h = harness(), show = execute('setOfficialContextVisible', h.scope);
  show('usgs-streamflow', false); assert.equal(h.reads.length, 0);
  show('usgs-streamflow', true); assert.deepEqual(h.reads, [['24h', 'USGS-06864500', false, '2024-09-02']]);
  h.scope.streamflowBundleRef.current = { state: 'ready' };
  show('usgs-streamflow', false); show('usgs-streamflow', true);
  assert.equal(h.reads.length, 1, 'warm archive toggles preserve the existing capture');
});
