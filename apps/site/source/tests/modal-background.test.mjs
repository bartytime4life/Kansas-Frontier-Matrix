import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const compile = source => ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
class Element {
  children = []; parentElement = null; inert = false; attributes = new Map(); isConnected = true; boxes = [{}];
  add(...children) { for (const child of children) { child.parentElement = this; this.children.push(child); } return this; }
  contains(node) { while (node) { if (node === this) return true; node = node.parentElement; } return false; }
  getAttribute(name) { return this.attributes.get(name) ?? null; }
  setAttribute(name, value) { this.attributes.set(name, value); }
  removeAttribute(name) { this.attributes.delete(name); }
  getClientRects() { return this.boxes; }
  closest(selector) {
    if (selector === ".site-root" ? this.root : this.inert || this.attributes.has("hidden")) return this;
    return this.parentElement?.closest(selector) ?? null;
  }
}
class Details extends Element {
  open = false;
  querySelector(selector) { assert.equal(selector, ":scope > summary"); return this.children[0] ?? null; }
}
const source = await readFile("app/modal-background.ts", "utf8");
const { isolateModalBackground, modalReturnTarget } = new Function("HTMLElement", "HTMLDetailsElement", compile(source).replaceAll("export ", "") + "return { isolateModalBackground, modalReturnTarget };")(Element, Details);
function fixture() {
  const root = new Element(); root.root = true;
  const page = new Element(), header = new Element(), main = new Element(), panel = new Element(), map = new Element(), held = new Element();
  held.inert = true; held.setAttribute("aria-hidden", "false");
  page.add(root, new Element()); root.add(header, main); main.add(panel, map, held);
  return { page, root, header, main, panel, map, held };
}
test("compact modal excludes sibling input at every app ancestor and restores exact prior state", () => {
  const f = fixture(), cleanup = isolateModalBackground(f.panel, f.root);
  for (const e of [f.header, f.map, f.held]) { assert.equal(e.inert, true); assert.equal(e.getAttribute("aria-hidden"), "true"); }
  for (const e of [f.panel, f.main, f.root, f.page.children[1]]) assert.equal(e.inert, false, "dialog branch and platform chrome stay intact");
  cleanup();
  for (const e of [f.header, f.map]) { assert.equal(e.inert, false); assert.equal(e.getAttribute("aria-hidden"), null); }
  assert.equal(f.held.inert, true); assert.equal(f.held.getAttribute("aria-hidden"), "false");
  const next = isolateModalBackground(f.panel, f.root); next(); assert.equal(f.map.inert, false, "repeat navigation leaves no stuck input");
  isolateModalBackground(f.panel, null)(); assert.equal(f.header.inert, false, "missing app root cannot isolate the entire browser page");
});
test("modal close returns to visible trigger, closed-menu summary or map fallback", () => {
  const fallback = new Element(), trigger = new Element();
  assert.equal(modalReturnTarget(trigger, fallback), trigger);
  const outer = new Details(), outerSummary = new Element(), inner = new Details(), innerSummary = new Element();
  outer.add(outerSummary, inner); inner.add(innerSummary, trigger);
  assert.equal(modalReturnTarget(trigger, fallback), outerSummary, "outer closed disclosure wins even if descendant boxes remain");
  outer.open = true; assert.equal(modalReturnTarget(trigger, fallback), innerSummary);
  inner.open = true; trigger.inert = true; assert.equal(modalReturnTarget(trigger, fallback), fallback);
  trigger.inert = false; trigger.boxes = []; assert.equal(modalReturnTarget(trigger, fallback), fallback);
  trigger.boxes = [{}]; trigger.isConnected = false; assert.equal(modalReturnTarget(trigger, fallback), fallback);
});
const page = await readFile("app/page.tsx", "utf8"), ast = ts.createSourceFile("page.tsx", page, ts.ScriptTarget.ES2022, true, ts.ScriptKind.TSX);
let effect;
function visit(node) {
  if (ts.isCallExpression(node) && node.expression.getText(ast) === "useEffect" && node.arguments[0]?.getText(ast).includes("const restoreBackground = isolateModalBackground")) effect = node.arguments[0].getText(ast);
  ts.forEachChild(node, visit);
}
visit(ast); assert.ok(effect);
test("actual Layers effect owns external focus and releases it when another tool or workspace takes over", () => {
  for (const overrides of [{}, { isCompact: false }, { primaryWorkspace: "reports" }, { leftOpen: false }, { rightOpen: true }, { mapUtilityOpen: true }, { qwenOpen: true }]) {
    const f = fixture(), listeners = new Map(), focused = [];
    const scope = { primaryWorkspace: "map", isCompact: true, leftOpen: true, rightOpen: false, mapUtilityOpen: false, qwenOpen: false,
      ...overrides, leftPanelRef: { current: f.panel }, isolateModalBackground, Node: Element,
      visibleFocusableElements: () => [{ focus: () => focused.push("close") }],
      document: { addEventListener: (name, callback, capture) => { assert.equal(capture, true); listeners.set(name, callback); }, removeEventListener: (name, callback, capture) => { assert.equal(capture, true); assert.equal(listeners.get(name), callback); listeners.delete(name); } } };
    const cleanup = new Function(...Object.keys(scope), compile(`return ${effect};`))(...Object.values(scope))();
    if (Object.keys(overrides).length) { assert.equal(cleanup, undefined); assert.equal(f.map.inert, false); continue; }
    listeners.get("focusin")({ target: f.map }); assert.deepEqual(focused, ["close"]);
    listeners.get("focusin")({ target: f.panel }); assert.deepEqual(focused, ["close"]);
    cleanup(); assert.equal(listeners.size, 0); assert.equal(f.header.inert, false); assert.equal(f.map.inert, false);
  }
});
