import assert from 'node:assert/strict';
import test from 'node:test';
import { readFile } from 'node:fs/promises';
import vm from 'node:vm';
import ts from 'typescript';

const exports = {};
vm.runInNewContext(ts.transpileModule(await readFile('app/explorer-menu-dismissal.ts', 'utf8'), {
  compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 },
}).outputText, { exports });

function setup() {
  const listeners = new Map(), summary = {}, action = {}, outside = {};
  const menu = { open: true, contains: target => target === summary || target === action };
  const document = {
    addEventListener: (type, handler, capture = false) => listeners.set(`${type}:${capture}`, handler),
    removeEventListener: (type, handler, capture = false) => {
      const key = `${type}:${capture}`;
      assert.equal(listeners.get(key), handler);
      listeners.delete(key);
    },
  };
  const dispose = exports.installExplorerMenuDismissal({
    ownerDocument: document, querySelectorAll: () => menu.open ? [menu] : [],
  });
  const emit = (type, target) => {
    for (const [key, handler] of listeners) if (key.startsWith(`${type}:`)) handler({ target, relatedTarget: null });
  };
  return { menu, summary, action, outside, emit, listeners, dispose };
}

test('Safari-style tap with no button focus keeps the action present through pointerdown and blur', () => {
  const h = setup();
  h.emit('focusin', h.summary);
  h.emit('pointerdown', h.action);
  h.emit('blur', h.summary);
  assert.equal(h.menu.open, true, 'null relatedTarget must not hide the button before click');
  let clicks = 0;
  if (h.menu.open) { clicks++; h.menu.open = false; }
  assert.equal(clicks, 1);
  h.dispose();
});

test('an outside tap and keyboard focus departure each dismiss the menu', () => {
  for (const type of ['pointerdown', 'focusin']) {
    const h = setup();
    h.emit(type, h.outside);
    assert.equal(h.menu.open, false, type);
    h.dispose();
  }
});

test('keyboard focus within the menu preserves it and unmount removes listeners', () => {
  const h = setup();
  h.emit('focusin', h.action);
  assert.equal(h.menu.open, true);
  h.dispose();
  assert.equal(h.listeners.size, 0);
});

test('both header menus use outside dismissal while retaining Escape and their native action handlers', async () => {
  const source = await readFile('app/page.tsx', 'utf8');
  const ast = ts.createSourceFile('page.tsx', source, ts.ScriptTarget.ES2022, true, ts.ScriptKind.TSX);
  const menus = [];
  function visit(node) {
    if (ts.isJsxOpeningElement(node) && node.tagName.getText(ast) === 'details') {
      const attrs = node.attributes.properties;
      const cls = attrs.find(a => a.name?.getText(ast) === 'className')?.initializer?.text;
      if (cls === 'header-overflow-menu' || cls?.includes('map-dock-map-menu')) menus.push(attrs);
    }
    ts.forEachChild(node, visit);
  }
  visit(ast);
  assert.equal(menus.length, 2);
  for (const attrs of menus) {
    assert.equal(attrs.some(a => a.name?.getText(ast) === 'onBlur'), false);
    const escape = attrs.find(a => a.name?.getText(ast) === 'onKeyDown').initializer.expression.getText(ast);
    const fn = new Function('return ' + ts.transpileModule(escape, { compilerOptions: { target: ts.ScriptTarget.ES2022 } }).outputText)();
    let focused = false, stopped = false;
    const menu = { open: true, querySelector: () => ({ focus: () => focused = true }) };
    fn({ key: 'Escape', currentTarget: menu, stopPropagation: () => stopped = true });
    assert.equal(menu.open, false); assert.equal(focused, true); assert.equal(stopped, true);
  }
  assert.match(source, /installExplorerMenuDismissal\(explorerHeaderRef.current\)/);
});
