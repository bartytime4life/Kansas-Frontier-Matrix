import assert from 'node:assert/strict';
import test from 'node:test';
import { readFile } from 'node:fs/promises';
import { setImmediate as settle } from 'node:timers/promises';
import ts from 'typescript';

const source = await readFile('app/maplibre-seam.ts', 'utf8');
const javascript = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const { createStageFullscreenControl } = await import('data:text/javascript;base64,' + Buffer.from(javascript).toString('base64'));

class ElementStub extends EventTarget {
  constructor(ownerDocument, tagName) { super(); this.ownerDocument = ownerDocument; this.tagName = tagName; this.children = []; this.attributes = {}; this.style = {}; }
  appendChild(child) { this.children.push(child); return child; }
  append(...children) { this.children.push(...children); }
  setAttribute(name, value) { this.attributes[name] = value; }
  getAttribute(name) { return this.attributes[name] ?? null; }
  remove() { this.removed = true; }
}
function setup({ enabled = true, reject = false } = {}) {
  const owner = new EventTarget();
  owner.fullscreenEnabled = enabled;
  owner.fullscreenElement = null;
  owner.createElement = tag => new ElementStub(owner, tag);
  let requests = 0, exits = 0, resizes = 0;
  const target = new ElementStub(owner, 'section');
  target.requestFullscreen = async () => {
    requests++;
    if (reject) throw new Error('browser denied fullscreen');
    owner.fullscreenElement = target; owner.dispatchEvent(new Event('fullscreenchange'));
  };
  owner.exitFullscreen = async () => { exits++; owner.fullscreenElement = null; owner.dispatchEvent(new Event('fullscreenchange')); };
  const control = createStageFullscreenControl(target);
  const root = control.onAdd({ resize: () => resizes++ });
  return { owner, target, control, root, button: root.children[0], status: root.children[1], counts: () => ({ requests, exits, resizes }) };
}

test('fullscreen follows the entire stage and exposes truthful Enter and Exit actions', async () => {
  const h = setup();
  assert.equal(h.button.getAttribute('aria-label'), 'Enter fullscreen');
  assert.equal(h.button.getAttribute('aria-pressed'), 'false');
  h.button.dispatchEvent(new Event('click')); await settle();
  assert.equal(h.owner.fullscreenElement, h.target);
  assert.equal(h.button.getAttribute('aria-label'), 'Exit fullscreen');
  assert.equal(h.button.getAttribute('aria-pressed'), 'true');
  h.button.dispatchEvent(new Event('click')); await settle();
  assert.equal(h.owner.fullscreenElement, null);
  assert.equal(h.button.getAttribute('aria-label'), 'Enter fullscreen');
  assert.deepEqual(h.counts(), { requests: 1, exits: 1, resizes: 2 });
});

test('browser rejection retains an honest state and an accessible status', async () => {
  const h = setup({ reject: true });
  h.button.dispatchEvent(new Event('click')); await settle();
  assert.equal(h.owner.fullscreenElement, null);
  assert.equal(h.button.getAttribute('aria-label'), 'Enter fullscreen');
  assert.equal(h.status.getAttribute('role'), 'status');
  assert.match(h.status.textContent, /Fullscreen is unavailable/);
});

test('unsupported fullscreen stays hidden and teardown removes listeners', async () => {
  const unsupported = setup({ enabled: false });
  assert.equal(unsupported.root.style.display, 'none');
  const h = setup();
  h.control.onRemove();
  assert.equal(h.root.removed, true);
  h.owner.dispatchEvent(new Event('fullscreenchange'));
  h.button.dispatchEvent(new Event('click')); await settle();
  assert.deepEqual(h.counts(), { requests: 0, exits: 0, resizes: 0 });
});
