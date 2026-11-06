import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';
const code = ts.transpileModule(await readFile('app/explorer-layer-history.ts', 'utf8'), { compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 } }).outputText;
const mod = { exports: {} };
new Function('require', 'exports', code)(() => ({ isEmbeddedSiteRuntime: () => false }), mod.exports);
const { ensureExplorerHistoryEntry, explorerHistoryEntryKey, explorerHistoryParams, explorerHistoryWelcome, saveExplorerHistoryView, restoreArchiveViewDays } = mod.exports;

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


test('startup, a chosen map and another map remain reachable by Back and Forward without changing the route', () => {
  const entries = [{ router: 'keep-router-state' }];
  let index = 0;
  const history = {
    get state() { return entries[index]; },
    replaceState(state, title, ...url) { assert.equal(title, ''); assert.equal(url.length, 0); entries[index] = state; },
    pushState(state, title, ...url) { assert.equal(title, ''); assert.equal(url.length, 0); entries.splice(++index); entries.push(state); },
  };
  const save = (query, welcome, navigation = false) => saveExplorerHistoryView(new URLSearchParams(query), history, false, { welcome, navigation });
  save('topic=all&base=standard', true);
  save('topic=government&base=civic&c=-98,38&z=6', false, true);
  save('topic=government&base=civic&c=-97,39&z=8', false); // Pan/zoom update this step.
  save('topic=agriculture&base=kansas-aerial', false, true);
  assert.equal(entries.length, 3, 'only deliberate destinations add entries');
  index--;
  assert.equal(explorerHistoryParams('', history.state).get('topic'), 'government');
  assert.equal(explorerHistoryParams('', history.state).get('z'), '8', 'the latest camera belongs to its previous map');
  index--;
  assert.equal(explorerHistoryWelcome(history.state), true, 'Back from the first map returns to startup');
  index++;
  assert.equal(explorerHistoryWelcome(history.state), false);
  assert.equal(explorerHistoryParams('', history.state).get('topic'), 'government');
  index++;
  assert.equal(explorerHistoryParams('', history.state).get('topic'), 'agriculture');
  assert.ok(entries.every(entry => entry.router === 'keep-router-state'));
  save('topic=agriculture&base=kansas-aerial', false, true);
  assert.equal(entries.length, 3, 'reselecting an unchanged destination adds no empty step');
});

test('navigation after Back retires only forward entries; embedded and blocked history remain usable', () => {
  const entries = [{}]; let index = 0;
  const history = { get state() { return entries[index]; }, replaceState(state) { entries[index] = state; },
    pushState(state) { entries.splice(++index); entries.push(state); } };
  const save = topic => saveExplorerHistoryView(new URLSearchParams({ topic }), history, false, { navigation: true });
  save('all'); save('government'); save('water'); index--;
  save('agriculture');
  assert.deepEqual(entries.map(entry => explorerHistoryParams('', entry).get('topic')), ['all', 'government', 'agriculture']);
  const before = entries.length;
  assert.equal(saveExplorerHistoryView(new URLSearchParams('topic=geology'), history, true, { navigation: true }), false);
  assert.equal(entries.length, before);
  assert.equal(saveExplorerHistoryView(new URLSearchParams('topic=geology'), { state: history.state, replaceState() {}, pushState() { throw new Error('blocked'); } }, false, { navigation: true }), false);
  for (const state of [null, {}, { kfmExplorerWelcome: 'true' }]) assert.equal(explorerHistoryWelcome(state), null);
});

test('a delayed startup save cannot overwrite the map entry selected by Forward', async () => {
  const page = ts.createSourceFile('page.tsx', await readFile('app/page.tsx', 'utf8'), ts.ScriptTarget.Latest, true, ts.ScriptKind.TSX);
  let effect;
  const visit = node => {
    if (ts.isCallExpression(node) && ['useEffect','useLayoutEffect'].includes(node.expression.getText(page)) && node.arguments[0]?.getText(page).includes('saveExplorerHistoryView(')) effect = node.arguments[0];
    ts.forEachChild(node, visit);
  };
  visit(page);
  assert.ok(effect, 'execute the production save effect');
  const entries = [
    { router: 'preserved', kfmExplorerEntry: 'startup', kfmExplorerView: 'topic=all', kfmExplorerWelcome: true },
    { router: 'preserved', kfmExplorerEntry: 'map', kfmExplorerView: 'topics=government', kfmExplorerWelcome: false },
  ];
  let index = 0, owned = 'startup';
  const history = {
    get state() { return entries[index]; },
    replaceState(state) { entries[index] = state; },
    pushState(state) { entries.splice(++index); entries.push(state); },
  };
  const bindings = {
    explorerRestoredRef: { current: true }, explorerNavigationPendingRef: { current: false },
    explorerHistoryEntry: owned, guideOpen: true, readExplorerGuideDismissed: () => false,
    explorerHistoryWelcome, explorerHistoryEntryKey: state => state?.kfmExplorerEntry ?? null,
    setExplorerHistoryEntry: key => { owned = key; },
    buildExplorerParams: () => new URLSearchParams('topic=all'), saveExplorerHistoryView,
    window: { history },
  };
  const delayedStartupSave = new Function(...Object.keys(bindings), `${ts.transpile(`const result = ${effect.getText(page)};`)} return result;`)(...Object.values(bindings));
  // Back has committed startup; Forward selects its destination before React
  // flushes that startup commit's passive effects or delivers the next popstate.
  index = 1;
  delayedStartupSave();
  assert.equal(explorerHistoryWelcome(history.state), false, 'Forward retains its map marker');
  assert.equal(explorerHistoryParams('', history.state).get('topics'), 'government');
  assert.equal(entries.length, 2, 'a stale save never adds an entry');
  assert.equal(owned, 'startup', 'a stale render cannot adopt the new entry');
});

test('a visible chooser owns its history step before the next map action can run', async () => {
  const page = ts.createSourceFile('page.tsx', await readFile('app/page.tsx', 'utf8'), ts.ScriptTarget.Latest, true, ts.ScriptKind.TSX);
  let hook;
  const visit = node => {
    if (ts.isCallExpression(node) && ['useEffect','useLayoutEffect'].includes(node.expression.getText(page)) && node.arguments[0]?.getText(page).includes('saveExplorerHistoryView(')) hook = node;
    ts.forEachChild(node, visit);
  };
  visit(page); assert.ok(hook, 'execute the production history hook');
  const entries = [{ router: 'kept', kfmExplorerEntry: 'government', kfmExplorerView: 'topics=government', kfmExplorerWelcome: false }];
  const history = { get state() { return entries.at(-1); }, replaceState(state) { entries[entries.length-1] = state; }, pushState(state) { entries.push(state); } };
  const pending = { current: true }, deferred = [];
  let owned = 'government';
  const commit = (guideOpen, topic, request) => {
    const bindings = {
      explorerRestoredRef: { current: true }, explorerNavigationPendingRef: pending, explorerHistoryEntry: owned,
      explorerNavigationRequest: request, guideOpen, readExplorerGuideDismissed: () => false,
      explorerHistoryWelcome, explorerHistoryEntryKey, setExplorerHistoryEntry: key => { owned = key; },
      buildExplorerParams: () => new URLSearchParams({ topics: topic }), saveExplorerHistoryView,
      window: { history }, useEffect: fn => deferred.push(fn), useLayoutEffect: fn => fn(),
    };
    new Function(...Object.keys(bindings), ts.transpile(hook.getText(page)))(...Object.values(bindings));
  };
  commit(true, 'government', 1);
  assert.equal(entries.length, 2, 'the chooser is saved before another visible control can be activated');
  assert.equal(explorerHistoryWelcome(history.state), true);
  pending.current = true; commit(false, 'weather', 2);
  assert.equal(entries.length, 3, 'the following map gets its own step');
  assert.equal(explorerHistoryWelcome(entries[1]), true);
  assert.equal(explorerHistoryParams('', history.state).get('topics'), 'weather');
  assert.equal(deferred.length, 0, 'no old history save can consume the later action');
});

test('entry ownership survives router-state clones, reload and passive updates; deliberate navigation owns a fresh entry', () => {
  let writes = 0;
  const history = { state: { router: 'kept' }, replaceState(state) { this.state = state; writes++; }, pushState(state) { this.state = state; writes++; } };
  const initial = ensureExplorerHistoryEntry(history, false);
  assert.equal(typeof initial, 'string');
  assert.equal(history.state.router, 'kept');
  assert.equal(ensureExplorerHistoryEntry(history, false), initial);
  assert.equal(writes, 1, 'identifying a known entry does not write again');
  history.state = { ...history.state, framework: 'updated' };
  const save = (query, navigation, expectedEntry) => saveExplorerHistoryView(new URLSearchParams(query), history, false, { navigation, expectedEntry });
  assert.equal(save('topic=all', false, initial), true);
  assert.equal(save('topic=government', true, initial), true);
  const destination = explorerHistoryEntryKey(history.state);
  assert.notEqual(destination, initial);
  assert.equal(save('topic=government&z=8', false, destination), true);
  assert.equal(explorerHistoryEntryKey(history.state), destination);
  assert.equal(history.state.framework, 'updated');
  assert.equal(ensureExplorerHistoryEntry(history, false), destination, 'reload retains entry identity');
  const before = writes;
  assert.equal(save('topic=all', false, initial), false);
  assert.equal(writes, before, 'an old owner never writes or pushes');
  assert.equal(ensureExplorerHistoryEntry(history, true), null);
  assert.equal(ensureExplorerHistoryEntry({ state: null, replaceState() { throw Error('blocked'); } }, false), null);
  for (const state of [null, {}, { kfmExplorerEntry: '' }, { kfmExplorerEntry: 4 }, { kfmExplorerEntry: 'x'.repeat(129) }]) assert.equal(explorerHistoryEntryKey(state), null);
});
