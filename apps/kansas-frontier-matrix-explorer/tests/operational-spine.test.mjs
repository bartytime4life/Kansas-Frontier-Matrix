import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

test("adds one persistent map-to-report operational spine without replacing Explorer state", async () => {
  const [layout, spine, transformation, explorer] = await Promise.all([
    readFile(new URL("../app/layout.tsx", import.meta.url), "utf8"),
    readFile(new URL("../app/operational-spine.tsx", import.meta.url), "utf8"),
    readFile(new URL("../app/transformation.css", import.meta.url), "utf8"),
    readFile(new URL("../app/page.tsx", import.meta.url), "utf8"),
  ]);

  assert.match(layout, /import "\.\/transformation\.css"/);
  assert.match(layout, /<OperationalSpine \/>/);
  assert.match(spine, /data-kfm-enhancement="operational-spine-v1"/);
  assert.match(spine, /usePathname/);
  assert.match(spine, /pathname !== "\/"/);
  assert.match(spine, /"scope"[\s\S]*"layers"[\s\S]*"time"[\s\S]*"measure"[\s\S]*"inspect"[\s\S]*"evidence"[\s\S]*"report"[\s\S]*"share"/);
  assert.match(spine, /\.map-mobile-actions button/);
  assert.match(spine, /#map-utility-tab-\$\{view\}/);
  assert.match(spine, /\.report-map-query button/);
  assert.doesNotMatch(spine, /\bfetch\s*\(/);
  assert.doesNotMatch(spine, /localStorage|sessionStorage/);
  assert.match(transformation, /--kfm-spine-height/);
  assert.match(transformation, /\.kfm-report-ribbon/);
  assert.match(transformation, /prefers-reduced-motion/);

  // Existing report/evidence state remains owned by the mature Explorer route.
  assert.match(explorer, /kfm-custom-map-report-v1/);
  assert.match(explorer, /Evidence Drawer/);
  assert.match(explorer, /buildExplorerParams/);
});

test("the operational spine transpiles as a React client component", async () => {
  const ts = await import("typescript");
  const source = await readFile(new URL("../app/operational-spine.tsx", import.meta.url), "utf8");
  const result = ts.transpileModule(source, {
    compilerOptions: {
      jsx: ts.JsxEmit.ReactJSX,
      module: ts.ModuleKind.ESNext,
      target: ts.ScriptTarget.ES2022,
      strict: true,
    },
    fileName: "operational-spine.tsx",
    reportDiagnostics: true,
  });
  const errors = (result.diagnostics ?? []).filter((diagnostic) => diagnostic.category === ts.DiagnosticCategory.Error);
  assert.deepEqual(errors, []);
});
