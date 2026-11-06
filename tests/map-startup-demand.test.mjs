import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import ts from 'typescript';

const source = ts.createSourceFile('page.tsx', readFileSync(process.env.KFM_STARTUP_PAGE ?? 'app/page.tsx', 'utf8'), ts.ScriptTarget.Latest, true, ts.ScriptKind.TSX);
let startup, latch, dependencies;
function visit(node) {
  if (ts.isCallExpression(node) && node.expression.getText(source) === 'useEffect') {
    const body = node.arguments[0]?.getText(source) ?? '';
    if (body.includes('new mapLibre.Map(')) { startup = body; dependencies = node.arguments[1].getText(source); }
    if (body.includes('setMapRequested(true)')) latch = body;
  }
  ts.forEachChild(node, visit);
}
visit(source);
function run(code, context) {
  return new Function(...Object.keys(context), ts.transpileModule(`return (${code});`, { compilerOptions: { target: ts.ScriptTarget.ES2022 } }).outputText)(...Object.values(context));
}
function fixture(requested) {
  let loads = 0;
  const context = { mapRequested: requested, mapContainerRef: { current: {} },
    loadConfiguredMapLibre() { loads++; return { then() { return { catch() {} }; } }; } };
  const cleanup = run(startup, context)();
  return { loads, cleanup };
}

test('welcome and unresolved startup allocate no hidden Explorer renderer', () => {
  assert.equal(fixture(false).loads, 0);
  assert.equal(fixture(false).cleanup, undefined);
});
test('opening the Explorer starts its real bootstrap exactly once', () => {
  const f = fixture(true);
  assert.equal(f.loads, 1);
  assert.equal(typeof f.cleanup, 'function', 'existing map cleanup remains owned by its effect');
});
test('initial restore and guide reopening retain a one-way startup request', () => {
  assert.ok(latch, 'actual page owns the startup latch');
  let requested = false;
  for (const [guideOpen, expected] of [[null, false], [true, false], [false, true], [true, true], [false, true]]) {
    run(latch, { guideOpen, setMapRequested(value) { requested = value; } })();
    assert.equal(requested, expected);
  }
  const stable = { announce() {}, runMapMutation() {}, runtimeOfficialVisibility() {}, mapRequested: true };
  const before = run(`() => ${dependencies}`, { ...stable, guideOpen: false })();
  const after = run(`() => ${dependencies}`, { ...stable, guideOpen: true })();
  assert.deepEqual(after, before, 'returning to welcome must not dispose and recreate Explorer');
});
