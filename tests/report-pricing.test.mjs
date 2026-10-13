import assert from "node:assert/strict";
import test from "node:test";
import ts from "typescript";
import { readFile } from "node:fs/promises";
import { createRequire } from "node:module";

const source = await readFile(new URL("../server/reports/pricing.ts", import.meta.url), "utf8");
const code = ts.transpileModule(source, { compilerOptions: { target: ts.ScriptTarget.ES2022, module: ts.ModuleKind.CommonJS } }).outputText;
const mod = { exports: {} };
new Function("require", "module", "exports", code)(createRequire(import.meta.url), mod, mod.exports);
const { createReportQuote, assertQuoteCurrent, validatePricingPolicy, reportDigest } = mod.exports;

// Illustrative test-only amounts. These are not owner settings or sale prices.
const policy = () => ({ schemaVersion: 1, version: "test-only-v1", currency: "USD", minimumMinor: 500, maximumMinor: 100000,
  laborRateMinorPerHour: 6001, productBaseMinor: { brief: 100, standard: 200, technical: 300 },
  evidenceBaseMinor: { "source-context": 50, corroborated: 100, measured: 200 }, quoteTtlSeconds: 900 });
const assessment = () => ({ input: { stationId: "fixture-1", scope: "station", year: 2026 }, product: "standard", eligibility: "eligible",
  evidenceBand: "source-context", evidenceBasis: "Test provider response, not independently validated accuracy.",
  estimatedManualMinutes: 10, effortBasis: "Test retrieval and writing estimate; no measured labor claim.",
  sources: [{ sourceId: "fixture-source", title: "Test source", digest: reportDigest({ value: 17, unit: "ft" }),
    officialUrl: "https://example.test/source", rights: "public", observationTime: "2026-10-12T12:00:00Z",
    retrievedAt: "2026-10-13T12:00:00Z", units: ["ft"], limitations: ["Fixture only."] }], limitations: ["Not a live provider report."] });
const now = new Date("2026-10-13T12:00:00Z");
const rejectsCode = (fn, code) => assert.throws(fn, (error) => error.code === code);

test("quotes combine owner product/evidence rates and documented effort using integer money", () => {
  const quote = createReportQuote("guest-1", assessment(), policy(), now);
  assert.equal(quote.amountMinor, 1251);
  assert.deepEqual(quote.breakdown, { productMinor: 200, evidenceMinor: 50, effortMinor: 1001, minimumAdjustmentMinor: 0 });
  assert.equal(quote.currency, "USD");
  assert.equal(quote.expiresAt, "2026-10-13T12:15:00.000Z");
  assert.equal(quote.assessment.sources[0].observationTime, "2026-10-12T12:00:00Z");
  assert.deepEqual(quote.assessment.sources[0].units, ["ft"]);
});

test("no invented defaults, zero-price public reports, negative money or invalid currency", () => {
  for (const invalid of [null, {}, { ...policy(), minimumMinor: 0 }, { ...policy(), currency: "XYZ" },
    { ...policy(), laborRateMinorPerHour: -1 }, { ...policy(), maximumMinor: 10 },
    { ...policy(), productBaseMinor: { brief: 1, standard: 2 } }, { ...policy(), quoteTtlSeconds: Infinity }]) {
    rejectsCode(() => validatePricingPolicy(invalid), "REPORT_PRICING_NOT_CONFIGURED");
  }
});

test("minimum adjustments are disclosed and over-limit scope requires a new custom quote", () => {
  const low = { ...assessment(), estimatedManualMinutes: 0 };
  const quote = createReportQuote("guest-1", low, policy(), now);
  assert.equal(quote.amountMinor, 500);
  assert.equal(quote.breakdown.minimumAdjustmentMinor, 250);
  rejectsCode(() => createReportQuote("guest-1", assessment(), { ...policy(), maximumMinor: 1000 }, now), "REPORT_REQUIRES_CUSTOM_QUOTE");
});

test("insufficient, held and restricted evidence is rejected before quoting", () => {
  for (const eligibility of ["insufficient", "held", "restricted"]) {
    rejectsCode(() => createReportQuote("guest-1", { ...assessment(), eligibility }, policy(), now), "REPORT_EVIDENCE_INSUFFICIENT");
  }
  for (const rights of ["restricted", "unreviewed"]) {
    const item = assessment(); item.sources[0].rights = rights;
    rejectsCode(() => createReportQuote("guest-1", item, policy(), now), "REPORT_SOURCE_NOT_ELIGIBLE");
  }
});

test("a measured quality tier requires an actual validation method, measurement, unit and basis", () => {
  rejectsCode(() => createReportQuote("guest-1", { ...assessment(), evidenceBand: "measured" }, policy(), now), "REPORT_VALIDATION_MISSING");
  const measured = { ...assessment(), evidenceBand: "measured", measuredValidation: { method: "fixture validation", value: 0.2, unit: "m", basisUrl: "https://example.test/validation" } };
  assert.equal(createReportQuote("guest-1", measured, policy(), now).breakdown.evidenceMinor, 200);
});

test("quotes capture immutable scope, source times, units, limits and pricing without drift", () => {
  const input = assessment(); const rates = policy();
  const quote = createReportQuote("guest-1", input, rates, now);
  input.input.year = 2025; input.sources[0].digest = reportDigest("changed source"); rates.productBaseMinor.standard = 999;
  assert.equal(quote.assessment.input.year, 2026);
  assert.equal(quote.amountMinor, 1251);
  assert.ok(Object.isFrozen(quote.assessment.sources[0]));
  assertQuoteCurrent(quote, "guest-1", { year: 2026, scope: "station", stationId: "fixture-1" }, now);
  rejectsCode(() => assertQuoteCurrent(quote, "other-guest", quote.assessment.input, now), "REPORT_NOT_FOUND");
  rejectsCode(() => assertQuoteCurrent(quote, "guest-1", input.input, now), "REPORT_SCOPE_CHANGED");
  rejectsCode(() => assertQuoteCurrent(quote, "guest-1", quote.assessment.input, new Date(quote.expiresAt)), "REPORT_QUOTE_EXPIRED");
});

test("changed source snapshots or report content cannot be substituted under an existing quote", () => {
  const quote = structuredClone(createReportQuote("guest-1", assessment(), policy(), now));
  quote.assessment.sources[0].digest = reportDigest("replacement");
  rejectsCode(() => assertQuoteCurrent(quote, "guest-1", quote.assessment.input, now), "REPORT_QUOTE_CORRUPT");
});

test("invalid, oversized or ambiguous input never becomes a billable quote", () => {
  for (const input of [undefined, { value: NaN }, { value: () => {} }, { value: new Date() }, new Array(3)]) {
    rejectsCode(() => createReportQuote("guest-1", { ...assessment(), input }, policy(), now), "REPORT_INPUT_INVALID");
  }
  rejectsCode(() => createReportQuote("guest-1", { ...assessment(), input: "x".repeat(32769) }, policy(), now), "REPORT_INPUT_TOO_LARGE");
  const bad = assessment(); bad.sources = [];
  rejectsCode(() => createReportQuote("guest-1", bad, policy(), now), "REPORT_ASSESSMENT_INVALID");
});

test("source and policy digests change when source values, units or rates change", () => {
  const first = createReportQuote("guest-1", assessment(), policy(), now);
  const changed = assessment(); changed.sources[0].units = ["m"];
  const second = createReportQuote("guest-1", changed, { ...policy(), laborRateMinorPerHour: 6002 }, now);
  assert.notEqual(first.sourceDigest, second.sourceDigest);
  assert.notEqual(first.policyDigest, second.policyDigest);
});
