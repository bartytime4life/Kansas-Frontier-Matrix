import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { runInNewContext } from "node:vm";
import test from "node:test";
import ts from "typescript";

// Execute the page's actual event registrations, not a copy of their logic.
const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
const tree = ts.createSourceFile("page.tsx", page, ts.ScriptTarget.Latest, true, ts.ScriptKind.TSX);
const registrations = [];
function visit(node) {
  if (ts.isCallExpression(node) && ts.isPropertyAccessExpression(node.expression)
    && node.expression.expression.getText(tree) === "map"
    && ["on", "once"].includes(node.expression.name.text)
    && ts.isStringLiteral(node.arguments[0])
    && ["style.load", "load"].includes(node.arguments[0].text)) registrations.push(node.getText(tree));
  ts.forEachChild(node, visit);
}
visit(tree);
assert.equal(registrations.length, 2, "cover both main-map style and initial-load callbacks");
const code = ts.transpileModule(registrations.join(";\n"), {
  compilerOptions: { target: ts.ScriptTarget.ES2022, module: ts.ModuleKind.CommonJS },
}).outputText;

function harness() {
  const handlers = new Map(), once = new Set(), runtime = [], finalizations = [];
  const styleGenerationReadyRef = { current: false };
  let synchronizations = 0, syncSucceeds = true, finalizeSucceeds = true;
  runInNewContext(code, {
    map: {
      on: (event, callback) => handlers.set(event, callback),
      once: (event, callback) => { handlers.set(event, callback); once.add(event); },
      setProjection: projection => finalizations.push(projection.type),
      resize: () => finalizations.push("resize"),
    },
    syncStyle: () => { synchronizations++; styleGenerationReadyRef.current = syncSucceeds; return syncSucceeds; },
    styleGenerationReadyRef,
    projectionRef: { current: "mercator" },
    runMapMutation: (_label, operation) => { if (!finalizeSucceeds) return false; operation(); return true; },
    setRuntime: state => runtime.push(state),
    version: "test-runtime",
  });
  return {
    emit(event) { const handler = handlers.get(event); if (once.has(event)) handlers.delete(event); handler?.(); },
    failSync(value = true) { syncSucceeds = !value; },
    failFinalization() { finalizeSucceeds = false; },
    invalidateStyle() { styleGenerationReadyRef.current = false; },
    count: () => synchronizations, runtime, finalizations,
  };
}

test("initial style/load sequence installs layers once and still waits for readiness proof", () => {
  const h = harness(); h.emit("style.load"); h.emit("load");
  assert.equal(h.count(), 1, "load must not reapply all sources, terrain and overlays");
  assert.deepEqual(h.finalizations, ["mercator", "resize"]);
  assert.equal(h.runtime.length, 1);
  assert.equal(h.runtime[0].kind, "loading", "installation is not tile readiness or evidence admission");
  assert.match(h.runtime[0].message, /verifying local sources and interactions/);
});

test("initial load can install a missing style or retry an unsuccessful synchronization", () => {
  const missing = harness(); missing.emit("load"); assert.equal(missing.count(), 1);
  const retry = harness(); retry.failSync(); retry.emit("style.load");
  retry.failSync(false); retry.emit("load");
  assert.equal(retry.count(), 2); assert.equal(retry.runtime.length, 1);
});

test("later style loads always reinstall the current layers, including before initial load", () => {
  const h = harness(); h.emit("style.load"); h.invalidateStyle(); h.emit("style.load"); h.emit("load");
  assert.equal(h.count(), 2);
  h.invalidateStyle(); h.emit("style.load"); assert.equal(h.count(), 3);
  h.emit("load"); assert.equal(h.count(), 3, "initial finalization remains one-shot");
});

test("failed style or finalization never advances runtime verification", () => {
  const style = harness(); style.failSync(); style.emit("style.load"); style.emit("load");
  assert.equal(style.count(), 2); assert.equal(style.runtime.length, 0); assert.equal(style.finalizations.length, 0);
  const finalize = harness(); finalize.emit("style.load"); finalize.failFinalization(); finalize.emit("load");
  assert.equal(finalize.runtime.length, 0);
});
