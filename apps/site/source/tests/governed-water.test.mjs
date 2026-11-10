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

// Expected outcomes follow the Python policy runtime's exact datetime ordering.
const releaseClockCases = [
  ["release equals the current whole second", "2026-09-30T19:00:00Z", { released_at: "2026-09-30T19:00:00Z" }, "ELIGIBLE"],
  ["a release one microsecond in the future", "2026-09-30T19:00:00.000Z", { released_at: "2026-09-30T19:00:00.000001Z" }, "RELEASE_TIME_INVALID"],
  ["review one microsecond after release", "2026-09-30T19:00:00Z", { reviewed_at: "2026-09-30T18:59:00.000002Z", released_at: "2026-09-30T18:59:00.000001Z" }, "RELEASE_TIME_INVALID"],
  ["expiry one microsecond in the future", "2026-09-30T19:00:00Z", { expires_at: "2026-09-30T19:00:00.000001Z" }, "ELIGIBLE"],
  ["expiry equals now", "2026-09-30T19:00:00Z", { expires_at: "2026-09-30T19:00:00.000000Z" }, "RELEASE_TIME_INVALID"],
  ["expiry is one microsecond before now", "2026-09-30T19:00:00.000001Z", { expires_at: "2026-09-30T19:00:00Z" }, "RELEASE_TIME_INVALID"],
  ["review and release equal now with different fraction lengths", "2026-09-30T19:00:00.100000Z", { reviewed_at: "2026-09-30T19:00:00.1Z", released_at: "2026-09-30T19:00:00.10Z", expires_at: "2026-09-30T19:00:00.100001Z" }, "ELIGIBLE"],
  ["all bounds within one millisecond", "2026-09-30T19:00:00.123456Z", { reviewed_at: "2026-09-30T19:00:00.123454Z", released_at: "2026-09-30T19:00:00.123455Z", expires_at: "2026-09-30T19:00:00.123457Z" }, "ELIGIBLE"],
  ["a future release within that millisecond", "2026-09-30T19:00:00.123456Z", { released_at: "2026-09-30T19:00:00.123457Z" }, "RELEASE_TIME_INVALID"],
  ["an impossible release date", "2026-09-30T19:00:00Z", { released_at: "2026-09-31T18:00:00Z" }, "RELEASE_TIME_INVALID"],
  ["a date-only release outside the instant contract", "2026-09-30T19:00:00Z", { released_at: "2026-09-30" }, "RELEASE_TIME_INVALID"],
  ["a fraction beyond the microsecond contract", "2026-09-30T19:00:00Z", { released_at: "2026-09-30T18:59:00.0000001Z" }, "RELEASE_TIME_INVALID"],
];
for (const [name, now, clocks, expected] of releaseClockCases) test(`exact release clocks: ${name}`, async () => {
  const pkg = await water.parseWaterPackage(JSON.stringify(await fixture("snapshot")));
  const decision = { ...await fixture("decision"), ...clocks };
  assert.equal(water.waterGate(pkg, decision, now), expected);
  const response = await water.projectWater(pkg, decision, "layers", now);
  if (expected === "ELIGIBLE") {
    assert.equal(response.envelope.outcome, "ANSWER");
    assert.equal(response.data.released_at, decision.released_at, "source clock representation is preserved");
    assert.equal(response.data.approval_expires_at, decision.expires_at);
  } else {
    assert.equal(response.envelope.outcome, "ABSTAIN");
    assert.equal(response.envelope.reason_code, "RELEASE_TIME_INVALID");
    assert.equal(response.data, undefined);
  }
});

test("equal review and release instants retain every supported UTC fraction representation", async () => {
  const pkg = await water.parseWaterPackage(JSON.stringify(await fixture("snapshot"))), original = await fixture("decision");
  for (const fraction of ["", ".1", ".10", ".100", ".1000", ".10000", ".100000"]) {
    const now = `2026-09-30T19:00:00${fraction}Z`;
    const decision = { ...original, reviewed_at: now, released_at: now, expires_at: "2026-09-30T19:00:01Z" };
    assert.equal(water.waterGate(pkg, decision, now), "ELIGIBLE");
    const response = await water.projectWater(pkg, decision, "layers", now);
    assert.equal(response.envelope.outcome, "ANSWER");
    assert.equal(response.data.reviewed_at, now); assert.equal(response.data.released_at, now);
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
