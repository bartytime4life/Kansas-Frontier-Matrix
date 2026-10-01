import test from "node:test";
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { createRequire } from "node:module";
const require = createRequire(import.meta.url), ts = require("typescript");
const source = await readFile(new URL("../app/governed-water.ts", import.meta.url), "utf8");
const compiled = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const water = await import("data:text/javascript;base64," + Buffer.from(compiled).toString("base64"));
const fixture = async name => JSON.parse(await readFile(new URL(`./fixtures/governed-water/${name}.json`, import.meta.url), "utf8"));
const NOW = "2026-09-30T19:00:00Z";
test("Worker and Python return identical synthetic released responses", async () => {
  const pkg = await water.parseWaterPackage(JSON.stringify(await fixture("snapshot")));
  for (const view of ["bootstrap", "layers", "evidence"]) assert.deepEqual(await water.projectWater(pkg, await fixture("decision"), view, NOW), await fixture(view));
});
test("null discharge does not refresh the served measurement", async () => {
  const pkg = await water.parseWaterPackage(JSON.stringify(await fixture("snapshot")));
  const decision = await fixture("decision");
  const old = { ...pkg.candidate.observations[0], observed_at: "2026-09-29T18:00:00Z" };
  const recentNull = { ...pkg.candidate.observations[0], value: null };
  pkg.candidate.observations = [old, recentNull];
  const stale = await water.projectWater(pkg, decision, "layers", NOW);
  assert.equal(stale.envelope.freshness, "stale-accepted");
  assert.equal(stale.envelope.precision_actually_used.temporal.freshness_class, "stale-accepted");
  pkg.candidate.observations = [recentNull];
  const empty = await water.projectWater(pkg, decision, "layers", NOW);
  assert.equal(empty.envelope.freshness, "unknown");
});
test("missing review, withdrawal, expiry and quarantine omit data", async () => {
  const pkg = await water.parseWaterPackage(JSON.stringify(await fixture("snapshot"))), decision = await fixture("decision");
  for (const denied of [null, { ...decision, correction_state: "WITHDRAWN" }, { ...decision, rights_ref: null }, { ...decision, expires_at: "2026-09-30T18:59:00Z" }]) {
    const result = await water.projectWater(pkg, denied, "layers", NOW); assert.equal(result.envelope.outcome, "ABSTAIN"); assert.equal(result.data, undefined);
  }
  const held = await water.parseWaterPackage(JSON.stringify(await fixture("held-snapshot")));
  assert.equal((await water.projectWater(held, { ...decision, package_id: held.manifest.package_id }, "layers", NOW)).envelope.reason_code, "RIGHTS_OR_SENSITIVITY_HOLD");
});
test("impossible release and package dates are rejected rather than normalized", async () => {
  const pkg = await water.parseWaterPackage(JSON.stringify(await fixture("snapshot")));
  const decision = await fixture("decision");
  for (const expires_at of ["2026-09-31T00:00:00Z", "0000-10-01T00:00:00Z"]) {
    assert.equal(water.waterGate(pkg, { ...decision, expires_at }, NOW), "RELEASE_TIME_INVALID");
  }
  const snapshot = await fixture("snapshot");
  snapshot.manifest.end = "2026-09-31T18:00:00Z";
  const { package_id, ...unsignedManifest } = snapshot.manifest;
  snapshot.manifest.package_id = await water.digest(water.canonical(unsignedManifest));
  await assert.rejects(water.parseWaterPackage(JSON.stringify(snapshot)), /TIME_INVALID/);
});
test("approval expiry checks withhold invalid, missing, and elapsed dates", () => {
  const now = Date.parse(NOW);
  assert.equal(water.approvalRemainingMs("2026-10-01T00:00:00Z", now), 5 * 60 * 60 * 1000);
  for (const expiry of [undefined, null, "bad", "2026-09-31T00:00:00Z", "2026-09-30T18:59:59Z"]) {
    assert.equal(water.approvalRemainingMs(expiry, now), 0);
  }
});
test("tampered artifacts and unexpected paths fail before serving", async () => {
  const snapshot = await fixture("snapshot"); snapshot.artifacts["candidate.json"] += " ";
  await assert.rejects(water.parseWaterPackage(JSON.stringify(snapshot)), /ARTIFACT_DIGEST/);
  const injected = await fixture("snapshot"); injected.artifacts["../../private"] = "{}";
  await assert.rejects(water.parseWaterPackage(JSON.stringify(injected)), /ARTIFACT_CLOSURE/);
});

test("duplicate escaped keys and excessive nesting are rejected", () => {
  assert.throws(() => water.parseWaterJson('{"decision":1,"deci\\u0073ion":2}'), /DUPLICATE/);
  assert.throws(() => water.parseWaterJson('['.repeat(33) + '0' + ']'.repeat(33)), /DEPTH/);
  assert.deepEqual(water.parseWaterJson('{"list":[{"a":1},{"a":2}]}'), {list:[{a:1},{a:2}]});
});
