import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { createRequire } from "node:module";
import vm from "node:vm";
import test from "node:test";

const loadBoundary = async (logs = []) => {
  const ts = await import("typescript");
  const source = await readFile(new URL("../app/error.tsx", import.meta.url), "utf8");
  const javascript = ts.transpileModule(source, {
    compilerOptions: { jsx: ts.JsxEmit.ReactJSX, module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 },
    fileName: "error.tsx",
  }).outputText;
  const exports = {};
  vm.runInNewContext(javascript, { exports, require: createRequire(import.meta.url), console: { error: (...args) => logs.push(args) } });
  return exports;
};

test("the Vite client mounts the recovery boundary around both routes and auxiliary UI", async () => {
  const source = await readFile(new URL("../main.tsx", import.meta.url), "utf8");
  const ts = await import("typescript");
  const root = ts.createSourceFile("main.tsx", source, ts.ScriptTarget.Latest, true, ts.ScriptKind.TSX);
  let boundary;
  const visit = (node) => {
    if (ts.isJsxElement(node) && node.openingElement.tagName.getText(root) === "ExplorerErrorBoundary") boundary = node;
    ts.forEachChild(node, visit);
  };
  visit(root);
  assert.ok(boundary, "A fallback file alone does not catch errors in Vite");
  for (const child of ["ExplorerPage", "AboutPage", "OperationalSpine", "SiteRuntimeRepair"]) {
    assert.match(boundary.getText(root), new RegExp(`<${child}\\s*/>`));
  }
  for (const callback of ["onCaughtError", "onUncaughtError", "onRecoverableError"]) {
    assert.match(source, new RegExp(`${callback}: reportUiError`));
  }
});

test("the root error boundary fails closed and preserves a recovery action", async () => {
  const [boundary, readme, styles] = await Promise.all([
    readFile(new URL("../app/error.tsx", import.meta.url), "utf8"),
    readFile(new URL("../README.md", import.meta.url), "utf8"),
    readFile(new URL("../app/transformation.css", import.meta.url), "utf8"),
  ]);

  assert.match(boundary, /^"use client";/);
  assert.match(boundary, /UI_ERROR_CODE = "KFM-UI-UNEXPECTED-ERROR"/);
  assert.match(boundary, /SAFE_CORRELATION_ID/);
  assert.match(boundary, /correlationIdForError/);
  assert.match(boundary, /console\.error\("\[KFM UI error boundary\]"/);
  assert.match(boundary, /code: UI_ERROR_CODE/);
  assert.match(boundary, /role="alert"/);
  assert.match(boundary, /onClick=\{reset\}/);
  assert.match(boundary, /href="\/"/);
  assert.doesNotMatch(boundary, /error\.(?:message|stack)/);
  assert.doesNotMatch(boundary, /JSON\.stringify\(error/);
  assert.match(readme, /KFM-UI-UNEXPECTED-ERROR/);
  assert.match(styles, /\.kfm-error-boundary/);
});

test("the root error boundary transpiles with the declared TypeScript toolchain", async () => {
  const ts = await import("typescript");
  const source = await readFile(new URL("../app/error.tsx", import.meta.url), "utf8");
  const result = ts.transpileModule(source, {
    compilerOptions: {
      jsx: ts.JsxEmit.ReactJSX,
      module: ts.ModuleKind.ESNext,
      target: ts.ScriptTarget.ES2022,
      strict: true,
    },
    fileName: "error.tsx",
    reportDiagnostics: true,
  });
  const errors = (result.diagnostics ?? []).filter(
    (diagnostic) => diagnostic.category === ts.DiagnosticCategory.Error,
  );
  assert.deepEqual(errors, []);
});

test("diagnostics accept bounded own-data digests and reject unsafe or throwing values", async () => {
  const logs = [];
  const { correlationIdForError, reportUiError, ExplorerErrorBoundary } = await loadBoundary(logs);
  let getterReads = 0;
  const getter = Object.defineProperty({}, "digest", { get() { getterReads++; throw new Error("PRIVATE_GETTER"); } });
  const revoked = Proxy.revocable({}, {});
  revoked.revoke();
  for (const value of [null, undefined, "PRIVATE_THROW", 0, new Error("PRIVATE_MESSAGE"),
    { digest: "https://private.invalid/?secret=PRIVATE_TOKEN" }, { digest: "a".repeat(129) },
    { digest: "" }, { digest: 12 }, Object.create({ digest: "inherited" }), getter, revoked.proxy]) {
    assert.equal(correlationIdForError(value), "unavailable");
    assert.equal(ExplorerErrorBoundary.getDerivedStateFromError(value).failure.digest, "unavailable");
    reportUiError(value);
  }
  assert.equal(getterReads, 0);
  assert.equal(correlationIdForError({ digest: "  trace_123-safe  " }), "trace_123-safe");
  assert.equal(correlationIdForError({ digest: "a".repeat(128) }), "a".repeat(128));
  assert.doesNotMatch(JSON.stringify(logs), /PRIVATE_|private\.invalid/);
  for (const [label, diagnostic] of logs) {
    assert.equal(label, "[KFM UI error boundary]");
    assert.deepEqual(Object.keys(diagnostic).sort(), ["code", "correlationId"]);
    assert.equal(diagnostic.code, "KFM-UI-UNEXPECTED-ERROR");
    assert.equal(diagnostic.correlationId, "unavailable");
  }
});
