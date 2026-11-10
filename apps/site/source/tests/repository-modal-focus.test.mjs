import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";
import { componentHarness } from "./component-harness.mjs";

// Run the actual page effects/handlers and shared isolation helper. These DOM
// fixtures test ownership and cleanup; root browser QA verifies native focus.
const source = await readFile("app/page.tsx", "utf8");
const ast = ts.createSourceFile("page.tsx", source, ts.ScriptTarget.ES2022, true, ts.ScriptKind.TSX);
const callbacks = new Map(); let modalEffect, shortcutEffect, focusableExpression, selector;
const ownershipEffects = [];
function visit(node) {
  if (ts.isVariableDeclaration(node) && node.initializer) {
    const name = node.name.getText(ast), init = node.initializer;
    if (ts.isArrowFunction(init)) callbacks.set(name, init.getText(ast));
    if (ts.isCallExpression(init) && init.expression.getText(ast) === "useCallback") callbacks.set(name, init.arguments[0].getText(ast));
    if (name === "visibleFocusableElements") focusableExpression = init.getText(ast);
    if (name === "FOCUSABLE_SELECTOR") selector = init.getText(ast);
  }
  if (ts.isCallExpression(node) && ["useEffect", "useLayoutEffect"].includes(node.expression.getText(ast))) {
    const effect = node.arguments[0]?.getText(ast) ?? "";
    if (effect.includes("const panel = repositoryPanelRef.current;")) modalEffect = effect;
    if (effect.includes("const handleWorkspaceShortcut =")) shortcutEffect = effect;
    if (effect.includes("const panel = repositoryPanelRef.current;") || effect.includes("const panel = qwenPanelRef.current;")
      || effect.includes("const panel = leftPanelRef.current;") && effect.includes("isolateModalBackground") || effect.includes("const returningToScene")) {
      ownershipEffects.push({ hook:node.expression.getText(ast), effect, dependencies:node.arguments[1].getText(ast) });
    }
  }
  ts.forEachChild(node, visit);
}
visit(ast);
assert.ok(modalEffect && shortcutEffect && focusableExpression && selector);
const evaluate = (code, scope) => new Function(...Object.keys(scope), ts.transpileModule(`return (${code});`, { compilerOptions:{ target:ts.ScriptTarget.ES2022 } }).outputText)(...Object.values(scope));

class Element {
  children = []; parentElement = null; inert = false; attributes = new Map(); listeners = new Map(); tabIndex = -1; isConnected = true;
  classList = { contains:() => false };
  constructor(name, tag = "div") { this.name = name; this.tag = tag; }
  add(...children) { for (const child of children) { child.parentElement = this; child.document = this.document; this.children.push(child); } return this; }
  contains(node) { while (node) { if (node === this) return true; node = node.parentElement; } return false; }
  getAttribute(key) { return this.attributes.get(key) ?? null; }
  setAttribute(key, value) { this.attributes.set(key, value); }
  removeAttribute(key) { this.attributes.delete(key); }
  getClientRects() { return this.closest("[hidden]") ? [] : [{}]; }
  matches() { return ["input", "textarea", "select"].includes(this.tag) || this.getAttribute("contenteditable") === "true"; }
  closest(selector) {
    if (selector === ".site-root" && this.root || selector === "details" && this instanceof Details
      || selector === '[role="dialog"][aria-modal="true"]' && this.getAttribute("role") === "dialog" && this.getAttribute("aria-modal") === "true"
      || selector === "[hidden]" && this.attributes.has("hidden") || selector === "[hidden], [inert]" && (this.inert || this.attributes.has("hidden"))) return this;
    return this.parentElement?.closest(selector) ?? null;
  }
  querySelector(selector) { if (selector.endsWith("summary")) return this.children.find(child => child.tag === "summary") ?? null; return null; }
  querySelectorAll() { return this.children.flatMap(child => [child, ...child.querySelectorAll()]).filter(child => child.tabIndex >= 0); }
  addEventListener(type, callback) { this.listeners.set(type, callback); }
  removeEventListener(type, callback) { assert.equal(this.listeners.get(type), callback); this.listeners.delete(type); }
  focus() {
    if (!this.isConnected || this.closest("[hidden], [inert]")) return;
    this.document.activeElement = this;
    for (const fn of this.document.listeners.get("focusin") ?? []) fn({ target:this });
  }
}
class Details extends Element { open = false; }
const background = (await componentHarness("app/modal-background.ts", {}, { HTMLElement:Element, HTMLDetailsElement:Details })).exports;
const focusable = evaluate(focusableExpression, { FOCUSABLE_SELECTOR:JSON.parse(selector), HTMLDetailsElement:Details });
function fixture({ open = true, withPanel = true, menu = true } = {}) {
  const document = { activeElement:null, listeners:new Map(), addEventListener(type, fn, capture) { if (type === "focusin") assert.equal(capture, true); const list = this.listeners.get(type) ?? []; list.push(fn); this.listeners.set(type, list); }, removeEventListener(type, fn) { const list = this.listeners.get(type) ?? []; assert.ok(list.includes(fn)); this.listeners.set(type, list.filter(item => item !== fn)); } };
  const root = new Element("root"); root.root = true; root.document = document;
  const header = new Element("header"), main = new Element("main"), held = new Element("held"), overlay = new Element("overlay"), panel = new Element("repository");
  root.add(header, main, held, overlay); overlay.add(panel); panel.setAttribute("role", "dialog"); panel.setAttribute("aria-modal", "true");
  held.inert = true; held.setAttribute("aria-hidden", "false");
  const details = new Details("more"), summary = new Element("more-summary", "summary"), trigger = new Element("status-trigger", "button"), search = new Element("global-search", "input"), map = new Element("map");
  header.add(details, search); details.add(summary, trigger); main.add(map); for (const node of [summary, trigger, search, map]) node.tabIndex = 0;
  const close = new Element("close", "button"), filter = new Element("filter", "input"), refresh = new Element("refresh", "button"); for (const node of [close, filter, refresh]) node.tabIndex = 0; panel.add(close, filter, refresh);
  const state = { open, primary:"map", layers:false, utility:null, current:null }, timers = [], changes = [];
  const common = {
    document, Node:Element, repositoryOpen:open, repositoryPanelRef:{ current:withPanel ? panel : null },
    visibleFocusableElements:focusable, ...background, repositoryButtonRef:{ current:trigger },
    rightOpen:false, selectedRef:{ current:null }, setRepositoryOpen:value => { state.open = value; }, setCurrentWorkspace:value => { state.current = value; },
    window:{ setTimeout:fn => timers.push(fn) },
  };
  if (!menu) trigger.parentElement = header;
  const closeRepository = evaluate(callbacks.get("closeRepository"), common);
  let cleanup;
  const scope = () => ({ ...common, repositoryOpen:state.open, closeRepository });
  const shortcuts = ({ repositoryOpen = state.open } = {}) => evaluate(shortcutEffect, {
    repositoryOpen, primaryWorkspace:state.primary, isCompact:false, document,
    globalSearchInputRef:{ current:search },
    openMapUtility:view => { state.utility = view; changes.push(view); },
    setPrimaryWorkspace:value => { state.primary = value; }, dismissMapUtilityWithoutFocus:() => changes.push("dismiss"),
    setLeftPanelMode:value => { state.mode = value; }, setLeftOpen:update => { state.layers = update(state.layers); }, setRightOpen() {}, setTimelineOpen() {},
  })();
  const mount = () => { cleanup = evaluate(modalEffect, scope())(); };
  const unmount = () => { cleanup?.(); cleanup = undefined; };
  const key = (key, target = document.activeElement, extra = {}) => {
    const event = { key, target, defaultPrevented:false, stopped:false, shiftKey:false, ...extra, preventDefault() { this.defaultPrevented = true; }, stopPropagation() { this.stopped = true; } };
    for (let node = target; node && !event.stopped; node = node.parentElement) node.listeners.get("keydown")?.(event);
    if (!event.stopped) for (const fn of document.listeners.get("keydown") ?? []) fn(event);
    return event;
  };
  return { document, root, header, main, held, overlay, panel, close, filter, refresh, search, map, summary, trigger, state, changes, mount, unmount, key, shortcuts, closeRepository, scope, flush:() => timers.splice(0).forEach(fn => fn()) };
}

// React destroys changed layout effects before mounting their replacements;
// passive cleanup follows layout setup. Keep those phases separate so this
// exercises cross-dialog ownership rather than isolated callback snapshots.
function ownershipFixture(initial = {}) {
  const f = fixture({ open:false });
  const qwen = new Element("qwen"), qwenClose = new Element("qwen-close", "button"), qwenInput = new Element("qwen-input", "input");
  f.map.add(qwen); qwen.add(qwenClose, qwenInput); qwen.setAttribute("role", "dialog"); qwen.setAttribute("aria-modal", "true");
  const layers = new Element("layers"), layersClose = new Element("layers-close", "button"), layersLast = new Element("layers-last", "button");
  f.main.add(layers); layers.add(layersClose, layersLast);
  for (const node of [qwenClose, qwenInput, layersClose, layersLast]) node.tabIndex = 0;
  const state = { repositoryOpen:false, qwenOpen:false, isCompact:false, leftOpen:false, ...initial };
  const closeQwenCompanion = () => { state.qwenOpen = false; };
  const closeLeftPanel = () => { state.leftOpen = false; };
  const stableScope = { Node:Element, HTMLElement:Element, Element, qwenPanelRef:{ current:qwen }, leftPanelRef:{ current:layers },
    rightPanelRef:{ current:null }, mapUtilityPanelRef:{ current:null }, timelineRef:{ current:null },
    primaryWorkspace:"map", rightOpen:false, mapUtilityOpen:false, mapUtilityView:"report", localAtlasPeek:false,
    surfaceInspectionOpen:false, terrainSurfaceMode:"off", timelineOpen:false, sourceStatusOpen:false,
    closeQwenCompanion, closeLeftPanel, closeSourceStatus() {}, closeMapUtility() {}, closeRightPanel() {}, closeTimelinePanel() {},
  };
  const active = new Map();
  const render = next => {
    Object.assign(state, next);
    f.state.open = state.repositoryOpen;
    const scope = { ...f.scope(), ...stableScope, ...state };
    const changed = ownershipEffects.flatMap((entry, index) => {
      const dependencies = evaluate(entry.dependencies, scope), prior = active.get(index);
      return prior && dependencies.every((value, i) => Object.is(value, prior.dependencies[i])) ? [] : [{ ...entry, index, dependencies }];
    });
    for (const hook of ["useLayoutEffect", "useEffect"]) {
      for (const entry of changed.filter(entry => entry.hook === hook)) active.get(entry.index)?.cleanup?.();
      for (const entry of changed.filter(entry => entry.hook === hook)) active.set(entry.index, { dependencies:entry.dependencies, cleanup:evaluate(entry.effect, scope)() });
    }
  };
  const dispose = () => { for (const entry of active.values()) entry.cleanup?.(); active.clear(); };
  render();
  return { ...f, qwen, qwenClose, qwenInput, layers, layersClose, layersLast, ownership:state, render, dispose };
}

test("repository dialog isolates the whole app and restores exact prior input state on close or unmount", () => {
  for (const exit of ["close", "unmount"]) {
    const f = fixture(); f.mount(); assert.equal(f.document.activeElement, f.close);
    for (const node of [f.header, f.main, f.held]) { assert.equal(node.inert, true); assert.equal(node.getAttribute("aria-hidden"), "true"); }
    for (const node of [f.root, f.overlay, f.panel]) assert.equal(node.inert, false);
    if (exit === "close") f.closeRepository(); f.unmount();
    for (const node of [f.header, f.main]) { assert.equal(node.inert, false); assert.equal(node.getAttribute("aria-hidden"), null); }
    assert.equal(f.held.inert, true); assert.equal(f.held.getAttribute("aria-hidden"), "false"); assert.equal(f.panel.listeners.size, 0); assert.equal(f.document.listeners.get("focusin").length, 0);
    f.state.open = true; f.mount(); f.unmount(); assert.equal(f.header.inert, false, "repeat navigation must not leave the header inert");
  }
});

test("the actual / then Escape sequence stays in the dialog and returns to the closed More menu summary", () => {
  const f = fixture(); f.mount(); const removeShortcuts = f.shortcuts();
  const slash = f.key("/"); assert.equal(f.document.activeElement, f.close); assert.equal(slash.defaultPrevented, false); assert.equal(f.state.open, true);
  const escape = f.key("Escape"); assert.equal(escape.defaultPrevented, true); assert.equal(escape.stopped, true); assert.equal(f.state.open, false);
  f.unmount(); f.flush(); assert.equal(f.document.activeElement, f.summary); removeShortcuts();
});

test("global /R/L cannot take input from this modal, even before the document shortcut effect refreshes", () => {
  for (const staleListener of [false, true]) for (const key of ["/", "r", "R", "l", "L"]) {
    const f = fixture(); f.mount(); const cleanup = f.shortcuts({ repositoryOpen:!staleListener }); f.key(key);
    assert.equal(f.document.activeElement, f.close); assert.equal(f.state.utility, null); assert.equal(f.state.layers, false); assert.deepEqual(f.changes, []); cleanup(); f.unmount();
  }
});

test("repository-open state also suppresses shortcuts for an unexpected background event target", () => {
  for (const key of ["/", "r", "l"]) {
    const f = fixture(); f.mount(); const cleanup = f.shortcuts(); f.key(key, f.map);
    assert.equal(f.document.activeElement, f.close); assert.equal(f.state.utility, null); assert.equal(f.state.layers, false); cleanup(); f.unmount();
  }
});

test("modal Tab order wraps at both ends while input editing and ordinary control keys stay local", () => {
  const f = fixture(); f.mount(); const cleanup = f.shortcuts();
  assert.equal(f.key("Tab", f.close, { shiftKey:true }).defaultPrevented, true); assert.equal(f.document.activeElement, f.refresh);
  assert.equal(f.key("Tab").defaultPrevented, true); assert.equal(f.document.activeElement, f.close);
  f.filter.focus(); assert.equal(f.key("Tab").defaultPrevented, false); assert.equal(f.key("/").defaultPrevented, false); assert.equal(f.key(" ").defaultPrevented, false); assert.equal(f.document.activeElement, f.filter); assert.equal(f.state.open, true);
  for (const node of [f.close, f.filter, f.refresh]) node.tabIndex = -1;
  assert.equal(f.key("Tab", f.panel).defaultPrevented, true, "an empty focus list cannot send Tab to background controls"); cleanup(); f.unmount();
});

test("programmatic outside focus is returned to the dialog without stealing focus from its inputs", () => {
  const f = fixture(); f.mount(); f.filter.focus(); assert.equal(f.document.activeElement, f.filter);
  f.search.focus(); assert.equal(f.document.activeElement, f.filter, "native inert background cannot acquire focus");
  for (const fn of f.document.listeners.get("focusin")) fn({ target:f.search }); assert.equal(f.document.activeElement, f.close);
  f.unmount(); f.search.focus(); assert.equal(f.document.activeElement, f.search);
});

test("closed or unmounted dialogs release shortcuts, with normal map /R/L and editing/modifier guards preserved", () => {
  for (const key of ["/", "r", "l"]) {
    const f = fixture(); f.mount(); f.closeRepository(); f.unmount(); f.flush(); const cleanup = f.shortcuts(); f.map.focus(); const event = f.key(key);
    assert.equal(event.defaultPrevented, true); if (key === "/") assert.equal(f.document.activeElement, f.search); else if (key === "r") assert.equal(f.state.utility, "report"); else { assert.equal(f.state.layers, true); assert.equal(f.state.mode, "layers"); }
    cleanup(); assert.equal(f.document.listeners.get("keydown").length, 0);
  }
  for (const extra of [{ ctrlKey:true }, { altKey:true }, { metaKey:true }, { defaultPrevented:true }]) {
    const f = fixture({ open:false }); const cleanup = f.shortcuts(); f.map.focus(); f.key("r", f.map, extra); assert.equal(f.state.utility, null); cleanup();
  }
  const f = fixture({ open:false }); const cleanup = f.shortcuts(); f.search.focus(); f.key("/"); f.key("r"); f.key("l"); assert.equal(f.document.activeElement, f.search); assert.equal(f.state.utility, null); assert.equal(f.state.layers, false); cleanup();
});

test("a closed or missing dialog mounts no trap; close keeps the standalone trigger fallback", () => {
  for (const options of [{ open:false }, { withPanel:false }]) {
    const f = fixture(options); f.mount(); assert.equal(f.header.inert, false); assert.equal(f.document.activeElement, null); assert.equal(f.document.listeners.size, 0); f.unmount();
  }
  const f = fixture({ menu:false }); f.mount(); f.closeRepository(); f.unmount(); f.flush(); assert.equal(f.document.activeElement, f.trigger);
});

test("desktop Qwen → Status → compact resize keeps Status usable, then returns ownership to Qwen", () => {
  const f = ownershipFixture({ qwenOpen:true, leftOpen:true });
  f.render({ repositoryOpen:true }); assert.equal(f.document.activeElement, f.close);
  f.render({ isCompact:true });
  assert.equal(f.ownership.qwenOpen, true, "opening Status retains the existing companion");
  assert.equal(f.overlay.inert, false); assert.equal(f.main.inert, true);
  assert.equal(focusable(f.panel).length, 3); assert.equal(focusable(f.qwen).length, 0);
  assert.equal(f.document.listeners.get("focusin").length, 1); assert.equal(f.layers.listeners.size, 0);
  f.key("Tab", f.close, { shiftKey:true }); assert.equal(f.document.activeElement, f.refresh);
  f.key("Tab"); assert.equal(f.document.activeElement, f.close);
  f.key("Escape"); f.render({ repositoryOpen:f.state.open }); f.flush();
  assert.equal(f.ownership.qwenOpen, true); assert.equal(f.document.activeElement, f.qwenClose, "delayed More focus cannot displace the resumed modal");
  assert.equal(f.main.inert, false); assert.equal(f.overlay.inert, true); assert.equal(f.layers.inert, true);
  assert.equal(focusable(f.qwen).length, 2); assert.equal(f.document.listeners.get("focusin").length, 1);
  f.key("Tab", f.qwenClose, { shiftKey:true }); assert.equal(f.document.activeElement, f.qwenInput);
  f.key("Tab"); assert.equal(f.document.activeElement, f.qwenClose);
  f.render({ isCompact:false }); assert.equal(f.header.inert, false); assert.equal(f.overlay.inert, false);
  assert.equal(f.document.listeners.get("focusin").length, 0); assert.equal(f.qwen.listeners.size, 0);
  f.render({ isCompact:true }); assert.equal(f.document.activeElement, f.qwenClose);
  f.dispose(); assert.equal(f.header.inert, false); assert.equal(f.main.inert, false); assert.equal(f.overlay.inert, false);
  assert.equal(f.held.inert, true); assert.equal(f.held.getAttribute("aria-hidden"), "false");
  assert.equal(f.document.listeners.get("focusin").length, 0); assert.equal(f.qwen.listeners.size, 0);
});

test("already-compact modal handoffs release prior isolation before the next owner captures background state", () => {
  for (const owner of ["qwen", "layers"]) {
    const f = ownershipFixture({ isCompact:true, qwenOpen:owner === "qwen", leftOpen:owner === "layers" });
    const ownerPanel = owner === "qwen" ? f.qwen : f.layers, ownerClose = owner === "qwen" ? f.qwenClose : f.layersClose;
    assert.equal(f.header.inert, true); assert.equal(f.overlay.inert, true);
    f.render({ repositoryOpen:true });
    assert.equal(f.overlay.inert, false); assert.equal(focusable(f.panel).length, 3); assert.equal(f.document.activeElement, f.close);
    assert.equal(focusable(ownerPanel).length, 0); assert.equal(f.document.listeners.get("focusin").length, 1);
    f.key("Escape"); f.render({ repositoryOpen:f.state.open }); f.flush();
    assert.equal(focusable(ownerPanel).length, 2); assert.equal(f.document.activeElement, ownerClose);
    assert.equal(f.overlay.inert, true); assert.equal(f.document.listeners.get("focusin").length, 1);
    f.key("Escape"); f.render({});
    assert.equal(f.header.inert, false); assert.equal(f.overlay.inert, false); assert.equal(f.document.listeners.get("focusin").length, 0);
    assert.equal(f.held.inert, true); assert.equal(f.held.getAttribute("aria-hidden"), "false");
    f.dispose(); assert.equal(ownerPanel.listeners.size, 0); assert.equal(f.panel.listeners.size, 0);
  }
});

test("Status unmount during a compact resize leaves no suspended dialog trap or stale inert state", () => {
  for (const owner of ["qwen", "layers"]) {
    const f = ownershipFixture({ qwenOpen:owner === "qwen", leftOpen:owner === "layers" });
    f.render({ repositoryOpen:true }); f.render({ isCompact:true }); f.dispose();
    for (const node of [f.header, f.main, f.overlay, f.layers, f.map]) { assert.equal(node.inert, false); assert.equal(node.getAttribute("aria-hidden"), null); }
    assert.equal(f.held.inert, true); assert.equal(f.held.getAttribute("aria-hidden"), "false");
    assert.equal(f.document.listeners.get("focusin").length, 0);
    for (const panel of [f.panel, f.qwen, f.layers]) assert.equal(panel.listeners.size, 0);
  }
});
