import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

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
