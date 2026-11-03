import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';

const page = await readFile('app/page.tsx', 'utf8');
const source = ts.createSourceFile('page.tsx', page, ts.ScriptTarget.Latest, true, ts.ScriptKind.TSX);
let initializer;
function visit(node) {
  if (ts.isVariableDeclaration(node) && node.name.getText(source) === 'closeExplorerGuide') initializer = node.initializer.getText(source);
  ts.forEachChild(node, visit);
}
visit(source);
assert.ok(initializer);
const compiled = ts.transpileModule(`const close = ${initializer};`, { compilerOptions: { target: ts.ScriptTarget.ES2022 } }).outputText;

function fixture() {
  const callbacks = [], calls = [];
  let shown = true;
  const body = {}, card = { closest: () => true };
  const document = { body, activeElement: card, querySelector(selector) {
    if (selector === '.living-welcome') return shown ? card : null;
    return { focus() { assert.equal(shown, false, 'header must no longer be inert'); calls.push('focus'); } };
  } };
  const close = new Function('document', 'window', 'setGuideOpen', 'setWelcomeSourcesOpen', 'writeExplorerGuideDismissed', compiled + '\nreturn close;')(
    document, { requestAnimationFrame: fn => callbacks.push(fn) }, value => calls.push(['guide', value]),
    value => calls.push(['sources', value]), value => calls.push(['remember', value]),
  );
  return { document, close, calls, callbacks, commit() { shown = false; document.activeElement = body; } };
}

test('welcome dismissal restores keyboard focus after the header becomes interactive', () => {
  const f = fixture();
  f.close(true);
  assert.deepEqual(f.calls, [['guide', false], ['sources', false], ['remember', true]]);
  f.commit(); f.callbacks.shift()();
  assert.equal(f.calls.at(-1), 'focus');
});

test('deferred welcome focus preserves a destination action and an immediately reopened guide', () => {
  const f = fixture();
  f.close(false); f.commit();
  f.document.activeElement = { closest: () => null };
  f.callbacks.shift()();
  assert.ok(!f.calls.includes('focus'));
  const reopened = fixture(); reopened.close(false); reopened.callbacks.shift()();
  assert.ok(!reopened.calls.includes('focus'));
});
