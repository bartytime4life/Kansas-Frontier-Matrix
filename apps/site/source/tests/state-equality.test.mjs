import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const source = ts.transpileModule(await readFile(new URL("../app/state-equality.ts", import.meta.url), "utf8"), {
  compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
}).outputText;
const { sameRecord, sameValues } = await import(`data:text/javascript;base64,${Buffer.from(source).toString("base64")}`);

test("sameValues keeps a probe whose sampled fields did not change", () => {
  const probe = { version: "6.9.0", styleLoaded: true, idle: true, sourcesReady: 0, projection: "mercator", error: null, failedChecks: [] };
  assert.equal(sameValues(probe, { styleLoaded: true, idle: true, sourcesReady: 0, projection: "mercator", error: null, failedChecks: [] }), true);
  assert.equal(sameValues(probe, { idle: false }), false);
  assert.equal(sameValues(probe, { failedChecks: ["CANVAS"] }), false);
  assert.equal(sameValues({ failedChecks: ["CANVAS", "STYLE"] }, { failedChecks: ["CANVAS", "STYLE"] }), true);
  assert.equal(sameValues({ failedChecks: ["STYLE", "CANVAS"] }, { failedChecks: ["CANVAS", "STYLE"] }), false);
  assert.equal(sameValues({ error: null }, { error: undefined }), false);
  assert.equal(sameValues({ count: NaN }, { count: NaN }), true);
});

test("sameRecord compares whole records, including removed keys", () => {
  assert.equal(sameRecord({ a: "ready", b: "loading" }, { a: "ready", b: "loading" }), true);
  assert.equal(sameRecord({ a: "ready", b: "loading" }, { a: "ready" }), false);
  assert.equal(sameRecord({ a: "ready" }, { a: "ready", b: "loading" }), false);
  assert.equal(sameRecord({}, {}), true);
});

test("the Explorer's idle handler keeps unchanged state objects", async () => {
  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  // A fresh object here re-renders the whole Explorer on every animated map frame.
  assert.match(page, /setSourceStates\(\(current\) => sameRecord\(current, nextSourceStates\) \? current : nextSourceStates\)/);
  assert.match(page, /setMaplibreProbe\(\(current\) => sameValues\(current, nextProbe\) \? current : \{ \.\.\.current, \.\.\.nextProbe \}\)/);
  const idle = page.slice(page.indexOf('map.on("idle"'), page.indexOf("} catch {", page.indexOf('map.on("idle"')));
  assert.ok(idle.length > 0);
  assert.doesNotMatch(idle, /setRuntime\(\{/, "idle-time runtime updates go through an equality check");
  assert.equal((idle.match(/setRuntime\(\(current\) => sameValues\(current, next\) \? current : next\)/g) ?? []).length, 2);
});
