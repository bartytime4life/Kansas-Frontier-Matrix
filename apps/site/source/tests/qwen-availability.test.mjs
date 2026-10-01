import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const source = await readFile(new URL("../app/qwen-availability.ts", import.meta.url), "utf8");
const compiled = ts.transpileModule(source, {
  compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
}).outputText;
const { qwenStatusLabel, shouldUseLocalQwen, successfulQwenState } = await import(
  `data:text/javascript;base64,${Buffer.from(compiled).toString("base64")}`
);

test("model-list health means installed, not an observed inference answer", () => {
  assert.equal(qwenStatusLabel("installed"), "LOCAL MODEL INSTALLED");
  assert.equal(shouldUseLocalQwen("installed"), true);
  assert.equal(qwenStatusLabel("local-answered"), "LOCAL MODEL ANSWERED");
});

test("a hosted answer never upgrades local bridge status", () => {
  assert.equal(successfulQwenState(false), "hosted-answered");
  assert.equal(qwenStatusLabel("hosted-answered"), "HOSTED MODEL ANSWERED");
  assert.equal(shouldUseLocalQwen("hosted-answered"), false);
  assert.equal(successfulQwenState(true), "local-answered");
  assert.equal(shouldUseLocalQwen("local-answered"), true);
});
