import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';

const page = await readFile(process.env.KFM_PAGE_PATH ?? 'app/page.tsx', 'utf8');
const source = ts.createSourceFile('page.tsx', page, ts.ScriptTarget.Latest, true, ts.ScriptKind.TSX);
let initializer, mapEntry;
function visit(node) {
  if (ts.isVariableDeclaration(node) && node.name.getText(source) === 'closeExplorerGuide') initializer = node.initializer.getText(source);
  if (ts.isVariableDeclaration(node) && node.name.getText(source) === 'runWelcomeMaps') mapEntry = node.initializer.getText(source);
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

// Exercise map entry together with dismissal: they used to queue independent
// handoffs, and the unconditional second frame could overwrite a newer choice.
function mapEntryFixture(nested) {
  const frames = [], focused = [], state = { shown: true };
  const body = {}, origin = { closest: () => nested ? null : origin };
  const document = { body, activeElement: origin,
    querySelector(selector) { return selector === '.living-welcome' ? state.shown ? origin : null : guide; },
    querySelectorAll() { return [edit]; },
  };
  const control = name => ({ name, closest: () => null, getClientRects: () => [{}],
    focus(options) { assert.equal(state.shown, false); assert.deepEqual(options, { preventScroll: true }); focused.push(name); document.activeElement = this; },
  });
  const guide = control('guide-trigger'), edit = control('map-topic-edit');
  const context = { document, window: { requestAnimationFrame(fn) { frames.push(fn); } },
    normalizeCategoryTopics: topics => topics, OFFICIAL_CONTEXT_PRESENT_FRAME: 2026,
    setGuideOpen: value => { state.shown = value; },
  };
  for (const name of ['openCategoryMap', 'setPrimaryWorkspace', 'setLeftOpen', 'setRightOpen', 'setTimelineOpen',
    'setCategoryDockHidden', 'setInstrumentOpen', 'setLayerCatalogView', 'setPlaying', 'setTemporalMode',
    'commitTemporalFrame', 'dismissMapUtilityWithoutFocus', 'setWelcomeSourcesOpen', 'writeExplorerGuideDismissed']) context[name] = () => {};
  const load = code => new Function(...Object.keys(context), ts.transpileModule(`return (${code});`, {
    compilerOptions: { target: ts.ScriptTarget.ES2022 },
  }).outputText)(...Object.values(context));
  assert.ok(mapEntry, 'execute the actual welcome map entry');
  const open = load(mapEntry), close = load(initializer);
  return { body, document, focused, guide, edit, control, state,
    enter() { open(['sky']); close(false); document.activeElement = body; },
    nextFrame() { frames.shift()?.(); },
    flush() { while (frames.length) frames.shift()(); },
  };
}

test('welcome map entry focuses Edit topics after card or nested-notes dismissal', () => {
  for (const nested of [false, true]) {
    const h = mapEntryFixture(nested); h.enter();
    assert.deepEqual(h.focused, [], 'the mounted welcome still owns focus until commit');
    h.flush();
    assert.equal(h.document.activeElement, h.edit, 'the intended map-entry destination wins over dismissal fallback');
  }
});

for (const name of ['Layers', 'Chart location', 'guide-trigger']) {
  test(`pending welcome map entry preserves newer ${name} focus`, () => {
    for (const nested of [false, true]) {
      const h = mapEntryFixture(nested); h.enter();
      const newer = name === 'guide-trigger' ? h.guide : h.control(name);
      newer.focus({ preventScroll: true });
      h.flush();
      assert.equal(h.document.activeElement, newer, 'a delayed map handoff must not redirect the next key to Edit topics');
      assert.deepEqual(h.focused, [name]);
    }
  });
}

test('a keyboard choice between queued entry frames is not overwritten by remaining callbacks', () => {
  for (const nested of [false, true]) {
    const h = mapEntryFixture(nested); h.enter(); h.nextFrame();
    const newer = h.control('Chart location'); newer.focus({ preventScroll: true });
    h.flush();
    assert.equal(h.document.activeElement, newer);
  }
});
