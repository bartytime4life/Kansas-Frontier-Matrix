import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";
import { componentHarness, findNode } from "./component-harness.mjs";

test("one inspection slot handles selection, delayed hover and dismissal without closing another view", async () => {
  const harness = await componentHarness(new URL("../app/inspection-panel.tsx", import.meta.url), {});
  const render = () => harness.render(harness.exports.useInspectionPanel);
  let panel = render();
  assert.equal(panel.inspectionPanel, null);
  panel.previewEvidence(); panel = render();
  assert.equal(panel.rightOpen, true);
  panel.setQwenOpen(true); panel = render();
  assert.equal(panel.qwenOpen, true); assert.equal(panel.rightOpen, false);
  // A map hover was queued before the user opened Qwen; it must not steal the slot.
  panel.previewEvidence(); panel.setRightOpen(false); panel = render();
  assert.equal(panel.inspectionPanel, "qwen");
  // An explicit selection replaces Qwen, without clearing the selection or draft.
  panel.setRightOpen(true); panel = render();
  assert.equal(panel.inspectionPanel, "evidence"); assert.equal(panel.qwenOpen, false);
  panel.setQwenOpen(false); panel = render();
  assert.equal(panel.inspectionPanel, "evidence");
  panel.setRightOpen(false); panel = render();
  assert.equal(panel.inspectionPanel, null);
});

test("inspection switches expose the active view and invoke their actual callbacks", async () => {
  const h = await componentHarness(new URL("../app/inspection-panel.tsx", import.meta.url), {});
  for (const active of ["evidence", "qwen"]) {
    const calls = [];
    const tree = h.render(h.exports.InspectionPanelSwitch, { active, onEvidence: () => calls.push("evidence"), onQwen: () => calls.push("qwen"), onClose: () => calls.push("close") });
    const close = findNode(tree, n => n.props?.className === "inspection-close");
    close.props.onClick(); assert.equal(calls.at(-1), "close");
    assert.equal(close.props["aria-label"], active === "qwen" ? "Close Qwen companion" : "Close Evidence Drawer");
    for (const [label, mode] of [["Evidence", "evidence"], ["Ask Qwen", "qwen"]]) {
      const button = findNode(tree, n => n.type === "button" && n.props.children === label);
      assert.equal(button.props["aria-pressed"], active === mode);
      button.props.onClick(); assert.equal(calls.at(-1), mode);
    }
  }
});

test("the actual delayed map hover uses non-interrupting preview arbitration", async () => {
  const source = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  const tree = ts.createSourceFile("page.tsx", source, ts.ScriptTarget.Latest, true, ts.ScriptKind.TSX);
  let show;
  const visit = n => { if (ts.isVariableDeclaration(n) && n.name.getText(tree) === "showHoverInDrawer") show = n.initializer; ts.forEachChild(n, visit); };
  visit(tree); assert.ok(show);
  const h = await componentHarness(new URL("../app/inspection-panel.tsx", import.meta.url), {});
  const render = () => h.render(h.exports.useInspectionPanel);
  const timers = [];
  const context = { surfaceInspectionOpenRef: { current: false }, hoverCandidateIdRef: { current: null }, hoverDrawerTimerRef: { current: null }, compactRef: { current: false }, rightPanelRef: { current: { dataset: { open: "false" } } }, window: { setTimeout(fn) { timers.push(fn); return timers.length; }, clearTimeout() {} }, previewEvidence: render().previewEvidence, setHoverActive() {}, setHoverSummary() {} };
  const code = ts.transpileModule(`const show = ${show.getText(tree)};`, { compilerOptions: { target: ts.ScriptTarget.ES2022, module: ts.ModuleKind.CommonJS } }).outputText;
  const hover = new Function(...Object.keys(context), `${code}; return show;`)(...Object.values(context));
  hover({ id: "county", title: "Seward" }, true);
  assert.equal(timers.length, 1);
  render().setQwenOpen(true); timers[0]();
  assert.equal(render().inspectionPanel, "qwen");
});

test("a Scene map sample retains selection without resizing its canvas; closing Scene reveals evidence", async () => {
  const source = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  const tree = ts.createSourceFile("page.tsx", source, ts.ScriptTarget.Latest, true, ts.ScriptKind.TSX);
  const nodes = []; const visit = n => { nodes.push(n); ts.forEachChild(n, visit); }; visit(tree);
  const declaration = nodes.find(n => ts.isVariableDeclaration(n) && n.name.getText(tree) === "openSelection");
  const effect = nodes.find(n => ts.isCallExpression(n) && n.expression.getText(tree) === "useEffect" && n.arguments[0]?.getText(tree).includes("surfaceEvidencePendingRef.current = false"));
  const evaluate = (node, ctx) => new Function(...Object.keys(ctx), ts.transpileModule(`const result = ${node.getText(tree)};`, { compilerOptions: { target: ts.ScriptTarget.ES2022 } }).outputText + '; return result;')(...Object.values(ctx));
  for (const competing of ["qwenOpen", "leftOpen", "mapUtilityOpen", "timelineOpen", "sourceStatusOpen", "helpOpen", "repositoryOpen", "mapContextOpen"]) {
    let opened = false;
    const ctx = { surfaceInspectionOpen: false, surfaceEvidencePendingRef: { current: true }, qwenOpen: false, leftOpen: false, mapUtilityOpen: false, timelineOpen: false, sourceStatusOpen: false, helpOpen: false, repositoryOpen: false, mapContextOpen: false, setRightOpen() { opened = true; }, [competing]: true };
    evaluate(effect.arguments[0], ctx)();
    assert.equal(opened, false, `${competing} keeps foreground ownership`);
    assert.equal(ctx.surfaceEvidencePendingRef.current, false, "cancel stale deferred reveal");
  }
  for (const sampling of [false, true]) for (const compact of [false, true]) {
    let selected, drawer = false, mapWidth = 1000, probe = "fresh sample", leftChanges = 0;
    const map = {};
    const ctx = { useCallback: fn => fn, surfaceInspectionOpen: sampling, isCompact: compact, mapContainerRef: { current: map }, surfaceEvidencePendingRef: { current: false }, hoverDrawerTimerRef: { current: null }, hoverCandidateIdRef: { current: null }, returnFocusRef: { current: null }, mapUtilityReturnRef: { current: null }, selectedRef: { current: null }, setSelected(value) { selected = value; }, setRightOpen(value) { drawer = value; if (value && !compact) { mapWidth = 660; probe = null; } }, setLeftOpen() { leftChanges++; }, setTimelineOpen() { leftChanges++; } };
    for (const name of ["setSubsurfaceInspection","setHoverSummary","setHoverActive","setMapUtilityOpen","setMapQueryCandidates","setFocusStage","setFocusIntent","setPendingFocusAction","setResearchOpen","setDrawerView","setCurrentWorkspace"]) ctx[name] = () => {};
    const record = { id: "selected-county" };
    evaluate(declaration.initializer, ctx)(record, map);
    assert.equal(selected, record, "the evidence record is retained while sampling");
    assert.equal(drawer, !sampling);
    if (sampling) {
      assert.equal(mapWidth, 1000); assert.equal(probe, "fresh sample"); assert.equal(leftChanges, 0);
      evaluate(effect.arguments[0], { ...ctx, surfaceInspectionOpen: false, qwenOpen: false, leftOpen: false, mapUtilityOpen: false, timelineOpen: false, sourceStatusOpen: false, helpOpen: false, repositoryOpen: false, mapContextOpen: false })();
      assert.equal(drawer, true); assert.equal(ctx.surfaceEvidencePendingRef.current, false);
    }
  }
});
