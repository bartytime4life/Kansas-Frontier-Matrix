import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';

const page = await readFile(process.env.KFM_PAGE_PATH ?? 'app/page.tsx', 'utf8');
const ast = ts.createSourceFile('page.tsx', page, ts.ScriptTarget.ES2022, true, ts.ScriptKind.TSX);
let effect;
function visit(node) {
  if (ts.isCallExpression(node) && node.expression.getText(ast) === 'useEffect' && node.arguments[0]?.getText(ast).includes('if (!streamflowSelectedAtPresent)')) {
    assert.equal(effect, undefined, 'one production owner of the River Pulse cadence');
    effect = node.arguments[0].getText(ast);
  }
  ts.forEachChild(node, visit);
}
visit(ast); assert.ok(effect);
const compiled = ts.transpileModule(`return ${effect};`, { compilerOptions: { target: ts.ScriptTarget.ES2022 } }).outputText;
function mount({ restored = false, selected = true } = {}) {
  const calls = [], intervals = [], cleared = [], playing = [];
  const scope = {
    explorerRestoredRef: { current: restored }, streamflowSelectedAtPresent: selected,
    streamflowArchiveDayRef: { current: null }, streamflowRequestRef: { current: null },
    streamflowRange: '24h', streamflowSelectedStationId: null,
    document: Object.assign(new EventTarget(), { hidden: false }), setStreamflowPlaying: value => playing.push(value),
    refreshStreamflow: (...args) => calls.push(args),
    window: Object.assign(new EventTarget(), { setInterval(callback, ms) { assert.equal(ms, 300_000); intervals.push(callback); return 17; }, clearInterval(id) { cleared.push(id); } }),
  };
  const cleanup = new Function(...Object.keys(scope), compiled)(...Object.values(scope))();
  return { scope, calls, intervals, cleared, playing, cleanup };
}
test('mount cannot issue a default network request before deferred URL/history restoration', () => {
  const h = mount();
  assert.deepEqual(h.calls, [], 'do not start then cancel an obsolete statewide read');
  h.intervals[0](); assert.deepEqual(h.calls, [], 'cadence cannot bypass pending restoration');
  h.cleanup(); assert.deepEqual(h.cleared, [17]);
});
test('restored archive remains owned by its station/day; automatic current cadence stays quiet', () => {
  const h = mount(); h.scope.explorerRestoredRef.current = true;
  h.scope.streamflowArchiveDayRef.current = '2024-09-02';
  h.intervals[0](); assert.deepEqual(h.calls, []);
  h.cleanup();
});
test('restored current view keeps immediate and five-minute refresh, avoiding hidden/in-flight work', () => {
  const h = mount({ restored: true });
  assert.deepEqual(h.calls, [['24h', null, true]]);
  h.scope.document.hidden = true; h.intervals[0](); assert.equal(h.calls.length, 1);
  h.scope.document.hidden = false; h.scope.streamflowRequestRef.current = {};
  h.intervals[0](); assert.equal(h.calls.length, 1);
  h.scope.streamflowRequestRef.current = null; h.intervals[0](); assert.equal(h.calls.length, 2);
  h.cleanup(); assert.deepEqual(h.cleared, [17]);
});
test('deselected or non-present River Pulse does not register a refresh cadence', () => {
  const h = mount({ restored: true, selected: false });
  assert.deepEqual(h.calls, []); assert.deepEqual(h.intervals, []);
  assert.deepEqual(h.playing, [false]); assert.equal(h.cleanup, undefined);
});
