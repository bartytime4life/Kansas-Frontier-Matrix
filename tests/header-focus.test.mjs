import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const page = await readFile("app/page.tsx", "utf8");
const ast = ts.createSourceFile("page.tsx", page, ts.ScriptTarget.ES2022, true, ts.ScriptKind.TSX);
let callback;
function visit(node) {
  if (ts.isVariableDeclaration(node) && node.name.getText(ast) === "closeHeaderOverflow") callback = node.initializer.arguments[0].getText(ast);
  ts.forEachChild(node, visit);
}
visit(ast);
assert.ok(callback, "execute the page's actual menu-close callback");
const code = ts.transpileModule(`const close = ${callback}; return close;`, { compilerOptions: { target: ts.ScriptTarget.ES2022 } }).outputText;

function harness() {
  const body = {}, action = {}, heading = {}, dialogControl = {}, canvas = {};
  const document = { body, activeElement: action }, timers = [];
  const summary = { focus(options) { assert.deepEqual(options, { preventScroll: true }); document.activeElement = summary; } };
  const menu = { open: true, removeAttribute(name) { assert.equal(name, "open"); this.open = false; }, querySelector(selector) { assert.equal(selector, "summary"); return summary; }, contains(element) { return element === action || element === summary; } };
  action.closest = selector => { assert.equal(selector, "details"); return menu; };
  const close = new Function("document", "window", code)(document, { setTimeout(fn, delay) { assert.equal(delay, 0); timers.push(fn); } });
  return { body, action, heading, dialogControl, canvas, document, summary, menu, close, flush() { timers.splice(0).forEach(fn => fn()); } };
}

test("closing More preserves a workspace heading that takes focus before the menu timer", () => {
  const h = harness(); h.close(h.action); assert.equal(h.menu.open, false);
  h.document.activeElement = h.heading; h.flush();
  assert.equal(h.document.activeElement, h.heading);
});

test("closing Map preserves a compact dialog's initial control and a map handoff", () => {
  for (const target of ["dialogControl", "canvas"]) {
    const h = harness(); h.close(h.action); h.document.activeElement = h[target]; h.flush();
    assert.equal(h.document.activeElement, h[target]);
  }
});

test("an action that leaves focus in the closed menu or on body still returns to its summary", () => {
  for (const target of ["action", "body"]) {
    const h = harness(); h.close(h.action); h.document.activeElement = h[target]; h.flush();
    assert.equal(h.document.activeElement, h.summary);
  }
});

test("a later user focus move is not overridden by delayed menu cleanup", () => {
  const h = harness(); h.close(h.action); const chosen = {}; h.document.activeElement = chosen; h.flush();
  assert.equal(h.document.activeElement, chosen);
});


test("panel actions explicitly leave focus restoration to the destination", () => {
  const h = harness(); h.close(h.action, false); assert.equal(h.menu.open, false);
  h.document.activeElement = h.body; h.flush(); assert.equal(h.document.activeElement, h.body);
});

test("opening Chat dismisses the welcome and focuses the requested composer without changing evidence", () => {
  let openCallback;
  function find(node) {
    if (ts.isVariableDeclaration(node) && node.name.getText(ast) === "openQwenCompanion") openCallback = node.initializer.arguments[0].getText(ast);
    ts.forEachChild(node, find);
  }
  find(ast);
  const code = ts.transpileModule(`return ${openCallback};`, { compilerOptions: { target: ts.ScriptTarget.ES2022 } }).outputText;
  for (const compact of [false, true]) {
    const state = {}, timers = [], trigger = {}, composer = {}, close = {};
    const context = { qwenReturnRef:{current:null}, document:{activeElement:trigger}, HTMLElement:class {}, isCompact:compact,
      globalSearchInputRef:{current:{focus:()=>{state.focus=composer;}}}, qwenPanelRef:{current:{querySelector:()=>({focus:()=>{state.focus=close;}})}},
      setPrimaryWorkspace:value=>{state.workspace=value;}, setGuideOpen:value=>{state.guide=value;}, setWelcomeSourcesOpen:value=>{state.sources=value;},
      setQwenOpen:value=>{state.chat=value;}, setHelpOpen(){}, dismissMapUtilityWithoutFocus(){},
      setLeftOpen(){}, setRightOpen(){}, setTimelineOpen(){}, window:{setTimeout:fn=>timers.push(fn)},
    };
    const open = new Function(...Object.keys(context), code)(...Object.values(context));
    open(trigger,"composer"); timers.splice(0).forEach(fn=>fn());
    assert.deepEqual(state,{workspace:"map",guide:false,sources:false,chat:true,focus:composer});
    assert.equal(context.qwenReturnRef.current,trigger,"close can return to the same header trigger");
  }
});
