import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';
const code = ts.transpileModule(await readFile('app/explorer-layer-history.ts', 'utf8'), { compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 } }).outputText;
const mod = { exports: {} };
new Function('require', 'exports', code)(() => ({ isEmbeddedSiteRuntime: () => false }), mod.exports);
const { explorerHistoryParams, saveExplorerHistoryView, restoreArchiveViewDays } = mod.exports;

test('navigation history retains layer dates, hidden selections, opacity and camera without replacing router state or URL', () => {
  const history = { state: { router: 'retained', key: 42 }, replaceState(state, title, ...url) { assert.equal(title, ''); assert.equal(url.length, 0); this.state = state; } };
  const params = new URLSearchParams('ctx=usgs-earthquakes&ctxo=usgs-earthquakes:0.73&ctxd=usgs-earthquakes:2024-09-02,nasa-gibs-fire-points:2024-06-01&c=-98.4,38.5953&z=6');
  assert.equal(saveExplorerHistoryView(params, history), true);
  assert.equal(history.state.router, 'retained'); assert.equal(history.state.key, 42);
  const restored = explorerHistoryParams('?ctx=default', history.state);
  assert.equal(restored.toString(), params.toString());
  assert.deepEqual(restoreArchiveViewDays(restored.get('ctxd'), '2026-10-11'), { 'usgs-earthquakes': '2024-09-02', 'nasa-gibs-fire-points': '2024-06-01' });
  params.delete('ctxd'); assert.equal(saveExplorerHistoryView(params, history), true);
  assert.deepEqual(restoreArchiveViewDays(explorerHistoryParams('', history.state).get('ctxd'), '2026-10-11'), {}, 'returning to Current cannot resurrect the previous day');
});

test('archive restoration rejects unsupported feeds, invalid calendar days, future dates, precoverage and prototype keys', () => {
  const value = '__proto__:2024-01-01,census-counties:2024-01-01,usgs-earthquakes:2024-02-30,nasa-gibs-fire-points:2017-12-31,noaa-hms-smoke:2005-08-04,raspberry-shake-stations:2026-10-12';
  assert.deepEqual(restoreArchiveViewDays(value, '2026-10-11'), {});
  assert.deepEqual(restoreArchiveViewDays('usgs-earthquakes:2024-02-29,noaa-hms-smoke:2005-08-05,nasa-gibs-fire-points:2018-01-01', '2026-10-11'), { 'usgs-earthquakes': '2024-02-29', 'noaa-hms-smoke': '2005-08-05', 'nasa-gibs-fire-points': '2018-01-01' });
});

test('embedded or blocked history leaves host navigation untouched; invalid saved state falls back to URL', () => {
  let writes = 0; const history = { state: null, replaceState() { writes++; throw new Error('blocked'); } };
  assert.equal(saveExplorerHistoryView(new URLSearchParams('ctx=test'), history, true), false); assert.equal(writes, 0);
  assert.equal(saveExplorerHistoryView(new URLSearchParams('ctx=test'), history), false); assert.equal(writes, 1);
  for (const state of [null, { kfmExplorerView: 42 }, { kfmExplorerView: 'x'.repeat(12001) }]) assert.equal(explorerHistoryParams('?ctx=explicit', state).get('ctx'), 'explicit');
});
