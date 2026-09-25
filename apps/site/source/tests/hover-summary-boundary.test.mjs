import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const source = await readFile(new URL("../app/hover-summary-boundary.ts", import.meta.url), "utf8");
const compiled = ts.transpileModule(source, {
  compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
  fileName: "hover-summary-boundary.ts",
}).outputText;
const { externalHoverTitle, localHoverTitle } = await import(`data:text/javascript;base64,${Buffer.from(compiled).toString("base64")}`);

test("protected local titles are withheld across evidence, release, and layer status", () => {
  const record = { title: "Exact protected site", evidenceState: "ANSWER", releaseState: "DEMONSTRATION" };
  assert.equal(localHoverTitle(record), record.title);
  assert.equal(localHoverTitle(record, "RESTRICTED"), "Protected feature");
  assert.equal(localHoverTitle({ ...record, releaseState: "RESTRICTED" }), "Protected feature");
  assert.equal(localHoverTitle({ ...record, evidenceState: "RESTRICTED_ACCESS" }), "Protected feature");
  assert.equal(localHoverTitle({ ...record, evidenceState: "DENIED_BY_POLICY" }), "Protected feature");
});

test("external display labels are bounded and controls cannot become text", () => {
  assert.equal(externalHoverTitle(null), "Basemap feature");
  assert.equal(externalHoverTitle({ name: "untrusted" }), "Basemap feature");
  assert.equal(externalHoverTitle("\n \t"), "Basemap feature");
  assert.equal(externalHoverTitle("  Kansas\n river\t"), "Kansas river");
  assert.equal(externalHoverTitle("x".repeat(200)).length, 90);
});

test("the site uses the bounded projection and records partial maturity", async () => {
  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  const registry = await readFile(new URL("../app/function-registry.ts", import.meta.url), "utf8");
  assert.match(page, /localHoverTitle\(hoverRecord\.feature\.properties, hoverLayer\?\.publicStatus\)/);
  assert.match(page, /externalHoverTitle\(externalCandidate\?\.properties\?\.name/);
  assert.match(registry, /id: "hover-summary",[\s\S]*?maturity: "PARTIAL"/);
});
