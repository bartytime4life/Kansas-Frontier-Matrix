import assert from 'node:assert/strict';
import test from 'node:test';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
const source = ts.transpileModule(await readFile('app/download-focus.ts', 'utf8'), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const { transferFocusDelta, revealTransferControls } = await import(`data:text/javascript;base64,${Buffer.from(source).toString('base64')}`);

test('reviewer mobile obstruction is removed for both maximum and final action above the actual task strip', () => {
  const field = { top: 767.328125, bottom: 812.125 }, action = { top: 925, bottom: 973 };
  const visible = { top: 16, bottom: 751 - 16 };
  const delta = transferFocusDelta(field, action, visible);
  assert.ok(field.top - delta >= visible.top); assert.ok(action.bottom - delta <= visible.bottom);
  assert.ok(delta > 0, 'moves the form above the strip, rather than treating it as already visible');
});
test('keyboard viewport and larger active strip retain the focused control when the whole action group cannot fit', () => {
  const field = { top: 767.328125, bottom: 812.125 }, action = { top: 925, bottom: 973 };
  const visible = { top: 16, bottom: 175 - 16 };
  const delta = transferFocusDelta(field, action, visible);
  assert.ok(field.top - delta >= visible.top); assert.ok(field.bottom - delta <= visible.bottom);
});
test('layout-aware reveal uses the visual viewport and measured fixed strip including its safe-area offset', () => {
  const prior = globalThis.window;
  const field = { top: 767.328125, bottom: 812.125 }, action = { top: 925, bottom: 973 };
  let scroll;
  const strip = { getBoundingClientRect: () => ({ top: 751, bottom: 802 }) };
  const scroller = { getBoundingClientRect: () => ({ top: 0, bottom: 812 }), querySelector: () => strip, scrollBy: options => { scroll = options; } };
  try {
    globalThis.window = { visualViewport: { offsetTop: 0, height: 812 }, innerHeight: 812, getComputedStyle: () => ({ position: 'fixed' }) };
    revealTransferControls({ closest: () => scroller, getBoundingClientRect: () => field }, { getBoundingClientRect: () => action });
    assert.equal(scroll.behavior, 'instant'); assert.ok(field.top - scroll.top >= 16); assert.ok(action.bottom - scroll.top <= 735);
    window.visualViewport = { offsetTop: 0, height: 420 }; revealTransferControls({ closest: () => scroller, getBoundingClientRect: () => field }, { getBoundingClientRect: () => action });
    assert.ok(field.top - scroll.top >= 16); assert.ok(action.bottom - scroll.top <= 404);
  } finally { if (prior === undefined) delete globalThis.window; else globalThis.window = prior; }
});
