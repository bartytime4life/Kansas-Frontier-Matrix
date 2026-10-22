import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const compile = source => ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
class Element {
  children = []; parentElement = null; inert = false; attributes = new Map(); isConnected = true; boxes = [{}];
  disabled = false; fieldsetDisabled = false; style = { display: "block", visibility: "visible" };
  ownerDocument = { defaultView: { getComputedStyle: element => element.style } };
  constructor(tagName = "div") { this.tagName = tagName.toUpperCase(); this.tabIndex = ["BUTTON", "INPUT", "SELECT", "TEXTAREA", "SUMMARY"].includes(this.tagName) ? 0 : -1; }
  add(...children) { for (const child of children) { child.parentElement = this; this.children.push(child); } return this; }
  contains(node) { while (node) { if (node === this) return true; node = node.parentElement; } return false; }
  getAttribute(name) { return this.attributes.get(name) ?? null; }
  setAttribute(name, value) { this.attributes.set(name, value); }
  removeAttribute(name) { this.attributes.delete(name); }
  getClientRects() { return this.boxes; }
  matches(selector) {
    if (selector === ":disabled") return this.disabled || this.fieldsetDisabled;
    const tag = selector.match(/^[a-z]+/i)?.[0];
    if (tag && this.tagName !== tag.toUpperCase()) return false;
    for (const [, name] of selector.matchAll(/\[([a-z]+)\]/gi)) if (!this.attributes.has(name)) return false;
    return true;
  }
  querySelectorAll(selector) {
    const selectors = selector.split(",").map(item => item.trim()), result = [];
    const visit = element => { for (const child of element.children) { if (selectors.some(item => child.matches(item))) result.push(child); visit(child); } };
    visit(this); return result;
  }
  closest(selector) {
    if (selector === ".site-root" ? this.root : this.inert || this.attributes.has("hidden")) return this;
    return this.parentElement?.closest(selector) ?? null;
  }
}
class Details extends Element {
  open = false;
  constructor() { super("details"); }
  querySelector(selector) { assert.equal(selector, ":scope > summary"); return this.children.find(child => child.tagName === "SUMMARY") ?? null; }
}
const source = await readFile("app/modal-background.ts", "utf8");
const { isolateModalBackground, modalReturnTarget, modalFocusableElements } = new Function("HTMLElement", "HTMLDetailsElement", compile(source).replaceAll("export ", "") + "return { isolateModalBackground, modalReturnTarget, modalFocusableElements };")(Element, Details);
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
  const outer = new Details(), outerSummary = new Element("summary"), inner = new Details(), innerSummary = new Element("summary");
  outer.add(outerSummary, inner); inner.add(innerSummary, trigger);
  assert.equal(modalReturnTarget(trigger, fallback), outerSummary, "outer closed disclosure wins even if descendant boxes remain");
  outer.open = true; assert.equal(modalReturnTarget(trigger, fallback), innerSummary);
  inner.open = true; trigger.inert = true; assert.equal(modalReturnTarget(trigger, fallback), fallback);
  trigger.inert = false; trigger.boxes = []; assert.equal(modalReturnTarget(trigger, fallback), fallback);
  trigger.boxes = [{}]; trigger.isConnected = false; assert.equal(modalReturnTarget(trigger, fallback), fallback);
});
test("modal tab candidates preserve native controls and scrolled content in DOM order", () => {
  const panel = new Element(), button = new Element("button"), input = new Element("input"), select = new Element("select"), textarea = new Element("textarea"), summary = new Element("summary"), link = new Element("a"), custom = new Element(), plain = new Element();
  link.setAttribute("href", "#help"); link.tabIndex = 0;
  custom.setAttribute("tabindex", "2"); custom.tabIndex = 2;
  const disclosure = new Details(); disclosure.open = true; disclosure.add(summary);
  const scroll = new Element(), belowFold = new Element("button");
  // A scroll container clips this control without removing its layout box.
  // Native focus can scroll it into view; viewport filtering would strand it.
  scroll.clientHeight = 100; scroll.scrollHeight = 800; scroll.scrollTop = 0;
  belowFold.offsetTop = 600;
  belowFold.getBoundingClientRect = () => { throw new Error("Tab candidates must not require viewport intersection"); };
  scroll.add(belowFold);
  panel.add(button, input, select, textarea, disclosure, link, custom, plain, scroll);
  assert.deepEqual(modalFocusableElements(panel), [button, input, select, textarea, summary, link, custom, belowFold]);
});
test("modal tab candidates exclude disabled, negative tabindex and hidden controls", () => {
  const panel = new Element(), visible = new Element("button"), disabled = new Element("button"), fieldsetControl = new Element("input"), negative = new Element("button"), hidden = new Element("button"), inertBranch = new Element(), inertControl = new Element("button"), hiddenBranch = new Element(), hiddenDescendant = new Element("button"), noLayout = new Element("button"), cssHidden = new Element("button"), cssCollapsed = new Element("button"), cssNone = new Element("button");
  disabled.disabled = true;
  // :disabled includes controls disabled by a fieldset, without their own attribute.
  fieldsetControl.fieldsetDisabled = true; assert.equal(fieldsetControl.disabled, false); assert.equal(fieldsetControl.getAttribute("disabled"), null);
  negative.tabIndex = -1; negative.setAttribute("tabindex", "-1");
  hidden.setAttribute("hidden", "");
  inertBranch.inert = true; inertBranch.add(inertControl);
  hiddenBranch.setAttribute("hidden", ""); hiddenBranch.add(hiddenDescendant);
  noLayout.boxes = [];
  cssHidden.style.visibility = "hidden"; cssCollapsed.style.visibility = "collapse"; cssNone.style.display = "none";
  panel.add(visible, disabled, fieldsetControl, negative, hidden, inertBranch, hiddenBranch, noLayout, cssHidden, cssCollapsed, cssNone);
  assert.deepEqual(modalFocusableElements(panel), [visible]);
});
test("closed disclosures retain only their first summary subtree despite retained layout boxes", () => {
  const panel = new Element(), details = new Details(), beforeSummary = new Element("button"), summary = new Element("summary"), summaryControl = new Element("button"), secondSummary = new Element("summary"), content = new Element("button"), inner = new Details(), innerSummary = new Element("summary"), innerContent = new Element("select"), noSummary = new Details(), orphanedContent = new Element("textarea");
  secondSummary.setAttribute("tabindex", "0");
  summary.add(summaryControl); inner.add(innerSummary, innerContent);
  details.add(beforeSummary, summary, secondSummary, content, inner);
  noSummary.add(orphanedContent); panel.add(details, noSummary);
  assert.deepEqual(modalFocusableElements(panel), [summary, summaryControl], "inner summaries remain hidden by an outer closed disclosure");
  details.open = true;
  assert.deepEqual(modalFocusableElements(panel), [beforeSummary, summary, summaryControl, secondSummary, content, innerSummary]);
  inner.open = true;
  assert.deepEqual(modalFocusableElements(panel), [beforeSummary, summary, summaryControl, secondSummary, content, innerSummary, innerContent]);
  assert.deepEqual(modalFocusableElements(noSummary), [], "the panel itself can be a closed disclosure");
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
