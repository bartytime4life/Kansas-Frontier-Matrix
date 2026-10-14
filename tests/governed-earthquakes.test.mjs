import test from "node:test";
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { createHash } from "node:crypto";
import { createRequire } from "node:module";
const require = createRequire(import.meta.url), ts = require("typescript");
const compile = text => ts.transpileModule(text, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const url = text => "data:text/javascript;base64," + Buffer.from(compile(text)).toString("base64");
const read = path => readFile(new URL(path, import.meta.url), "utf8");
const waterUrl = url(await read("../app/governed-water.ts"));
const weatherUrl = url((await read("../app/governed-weather.ts")).replace('"./governed-water"', JSON.stringify(waterUrl)));
const quakes = await import(url((await read("../app/governed-earthquakes.ts")).replace('"./governed-water"', JSON.stringify(waterUrl)).replace('"./governed-weather"', JSON.stringify(weatherUrl))));
const fixture = async name => JSON.parse(await read(`./fixtures/governed-earthquakes/${name}.json`));
const raw = async () => await read("./fixtures/governed-earthquakes/admitted-snapshot.json");
const NOW = "2025-11-02T13:00:00Z";
const pkg = async () => quakes.parseEarthquakePackage(await raw());
const omit = (value, key) => Object.fromEntries(Object.entries(value).filter(([name]) => name !== key));
const sha = text => "sha256:" + createHash("sha256").update(text).digest("hex");
// Python canonical_bytes for these ASCII fixtures: sorted keys, compact separators, shortest number spelling.
const pyJson = value => value === null || typeof value !== "object" ? JSON.stringify(value) : Array.isArray(value) ? `[${value.map(pyJson).join(",")}]`
  : `{${Object.keys(value).sort().map(k => `${JSON.stringify(k)}:${pyJson(value[k])}`).join(",")}}`;

/** Rewrite one artifact and every outer digest, as a forger would. */
async function resealed(mutate, artifact = "candidate.json") {
  const snapshot = JSON.parse(await raw());
  const value = JSON.parse(snapshot.artifacts[artifact]);
  mutate(value);
  const text = pyJson(value);
  snapshot.artifacts[artifact] = text;
  snapshot.manifest.artifacts[artifact] = sha(text);
  snapshot.manifest.package_id = sha(pyJson(omit(snapshot.manifest, "package_id")));
  return JSON.stringify(snapshot);
}

/** Change candidate records and reseal every record digest, the candidate id, its bindings and the receipt, so only the
 *  Python validator's semantic rules can refuse the package. ``patch`` rewrites the serialized candidate text (applied
 *  consistently to every digest input), for forgeries JSON values cannot express, such as 5.0 for 5. */
async function forgedCandidate(mutate, patch = text => text) {
  const snapshot = JSON.parse(await raw()), candidate = JSON.parse(snapshot.artifacts["candidate.json"]);
  mutate(candidate);
  for (const r of candidate.observations) r.record_digest = sha(patch(pyJson(omit(r, "record_digest"))));
  candidate.candidate_id = sha(patch(pyJson(omit(candidate, "candidate_id"))));
  const report = omit({ ...JSON.parse(snapshot.artifacts["validation.json"]), candidate_id: candidate.candidate_id }, "receipt_digest");
  const texts = { "candidate.json": patch(pyJson(candidate)), "validation.json": pyJson({ ...report, receipt_digest: sha(pyJson(report)) }) };
  for (const name of ["catalog.json", "evidence.json"]) texts[name] = pyJson({ ...JSON.parse(snapshot.artifacts[name]), candidate_id: candidate.candidate_id });
  for (const [name, text] of Object.entries(texts)) { snapshot.artifacts[name] = text; snapshot.manifest.artifacts[name] = sha(text); }
  snapshot.manifest.candidate_id = candidate.candidate_id;
  snapshot.manifest.package_id = sha(pyJson(omit(snapshot.manifest, "package_id")));
  return JSON.stringify(snapshot);
}

test("Worker and Python return identical released earthquake responses", async () => {
  const parsed = await pkg(), decision = await fixture("owner-decision");
  for (const view of ["bootstrap", "layers", "evidence"]) assert.deepEqual(await quakes.projectEarthquakes(parsed, decision, view, NOW), await fixture(view));
  assert.deepEqual(await quakes.projectEarthquakes(parsed, decision, "layers", NOW, 5), await fixture("layers-may"));
});

test("a month selects its parts, and the selection describes exactly the returned records", async () => {
  const parsed = await pkg(), decision = await fixture("owner-decision");
  const may = await quakes.projectEarthquakes(parsed, decision, "layers", NOW, 5);
  assert.deepEqual(may.data.observations.map(r => r.event_id), ["us7000p004", "ok2025p005", "us7000p006"]);
  assert.deepEqual(may.data.selection, { months: [5], observation_count: 3, review_status: { automatic: 1, reviewed: 2 }, context_margin_count: 1,
    magnitude_range: [2.1, 2.8], latest_event_date: "2025-05-27" });
  assert.equal(may.data.dataset.scope, "data_year");
  assert.equal(may.data.dataset.observation_count, 5);
  const none = await quakes.projectEarthquakes(parsed, decision, "layers", NOW, 3);
  assert.equal(none.envelope.reason_code, "EVIDENCE_NOT_FOUND");
  assert.equal(none.data, undefined);
  const layers = await quakes.projectEarthquakes(parsed, decision, "layers", NOW);
  assert.equal(layers.data.life_safety, "not_for_life_safety");
  assert.deepEqual(layers.data.bounds, [-102.1, 36.9, -94.5, 40.1]);
  assert.match(layers.envelope.precision_actually_used.spatial.accuracy, /not the state boundary/);
});

test("the earthquake gate refuses other families' decisions, expiry, withdrawal and the rights hold", async () => {
  const parsed = await pkg(), decision = await fixture("owner-decision");
  assert.equal(quakes.earthquakesGate(parsed, decision, NOW), "ELIGIBLE");
  for (const profile of ["kfm.water-release-decision/v1", "kfm.weather-release-decision/v1", "kfm.soil-release-decision/v1", "kfm.storm-events-release-decision/v1"]) {
    assert.equal(quakes.earthquakesGate(parsed, { ...decision, profile }, NOW), "RELEASE_BINDING_MISMATCH");
  }
  assert.equal(quakes.earthquakesGate(parsed, { ...decision, correction_state: "WITHDRAWN" }, NOW), "CORRECTION_HOLD");
  assert.equal(quakes.earthquakesGate(parsed, decision, "2025-11-09T12:45:00Z"), "RELEASE_TIME_INVALID");
  assert.equal(quakes.earthquakesGate(parsed, null, NOW), "REVIEW_REQUIRED");
  // The Storm Events license is not on the earthquake list, so the owner cannot self-release it.
  for (const entry of parsed.evidence.entries) entry.bundle.rights.license = "U.S. Public Domain (NOAA federal records, 17 U.S.C. 105); Storm Events data subject to revision";
  assert.equal(quakes.earthquakesGate(parsed, decision, NOW), "INDEPENDENT_REVIEW_REQUIRED");
});

test("freshness is the age of the capture", async () => {
  const parsed = await pkg(), decision = { ...(await fixture("owner-decision")), expires_at: "2025-12-30T00:00:00Z" };
  const fresh = async now => (await quakes.projectEarthquakes(parsed, decision, "bootstrap", now)).envelope.freshness;
  // The capture is 2025-11-01T12:00:00Z: current for 30 days, then stale-accepted.
  assert.equal(await fresh("2025-12-01T12:00:00Z"), "current");
  assert.equal(await fresh("2025-12-01T12:00:01Z"), "stale-accepted");
});

test("month bundles split into parts of 127 records by UTC origin month", () => {
  const events = Array.from({ length: 256 }, (_, i) => ({ origin_utc: "2025-05-01T00:00:00.000Z", event_id: `e${i}` }));
  assert.deepEqual(quakes.earthquakeMonthGroups(events).map(([m, p, r]) => [m, p, r.length]), [[5, 1, 127], [5, 2, 127], [5, 3, 2]]);
});

test("resealed packages that break the Python validator's rules are refused", async () => {
  const cases = [
    [c => { c.observations[3].flags = []; }, "RECORD_FLAGS_MISMATCH"],
    [c => { c.observations[0].origin_utc = "2025-02-30T08:23:45.120Z"; }, "RECORD_TIME_INVALID"],
    [c => { c.observations.reverse(); }, "RECORD_ORDER_OR_DUPLICATE"],
    [c => { c.observations[0].aliases = ["ok2025a001", "us7000p001"]; }, "RECORD_ORDER_OR_DUPLICATE"],
    [c => { c.observations[1].aliases = ["ok2025b002", "ok2025a001"]; }, "RECORD_ORDER_OR_DUPLICATE"],
    [c => { c.observations[0].raw_feature_json = "{}"; }, "EARTHQUAKE_SCHEMA_INVALID"],
    [c => { c.observations[0].longitude = -93.0; }, "EARTHQUAKE_SCHEMA_INVALID"],
    [c => { c.observations[0].latitude = 37.27412; }, "RECORD_NUMBER_NOT_CANONICAL"],
    [c => { c.observations[0].review_status = "deleted"; }, "RECORD_STATUS_WITHHELD"],
    [c => { c.months[4].events = 2; }, "MONTH_SUMMARY_MISMATCH"],
    [c => { c.months[0].query_status = 204; }, "MONTH_SUMMARY_MISMATCH"],
    [c => { c.latest_event_date = "2025-12-31"; }, "LATEST_EVENT_DATE_MISMATCH"],
    [c => { c.year_state = "CLOSED"; }, "CANDIDATE_TIME_INVALID"],
    [c => { c.withheld_counts = {}; }, "WITHHELD_COUNTS_INVALID"],
    [c => { c.coverage = "COMPLETE"; }, "CANDIDATE_AUTHORITY_OR_PROFILE_INVALID"],
    [c => { c.bounds = [-102, 37, -94.6, 40]; }, "CANDIDATE_AUTHORITY_OR_PROFILE_INVALID"],
  ];
  for (const [mutate, reason] of cases) await assert.rejects(quakes.parseEarthquakePackage(await forgedCandidate(mutate)), new RegExp(reason), reason);
  // A whole number written as a float (5.0 for 5) is refused, as the Python type check refuses it.
  await assert.rejects(quakes.parseEarthquakePackage(await forgedCandidate(() => {}, text => text.replace('"depth_km":5,', '"depth_km":5.0,'))), /RECORD_NUMBER_NOT_CANONICAL/);
  // An unsealed change is caught by the candidate digest, and a released carrier is refused outright.
  await assert.rejects(quakes.parseEarthquakePackage(await resealed(c => { c.observations[0].magnitude = 4.1; })), /CANDIDATE_DIGEST_MISMATCH/);
  await assert.rejects(quakes.parseEarthquakePackage(await resealed(c => { c.release_state = "RELEASED"; })), /CARRIER_CANNOT_SELF_APPROVE/);
  // A forged catalog cannot misreport the year it describes.
  await assert.rejects(quakes.parseEarthquakePackage(await resealed(c => { c.dataset.context_margin_count = 0; }, "catalog.json")), /CATALOG_MISMATCH/);
  // Evidence must be exactly the month parts the records produce.
  await assert.rejects(quakes.parseEarthquakePackage(await resealed(e => { e.entries.pop(); }, "evidence.json")), /EVIDENCE_CLOSURE_INVALID/);
  await assert.rejects(quakes.parseEarthquakePackage(await resealed(e => { e.entries[0].month = 3; }, "evidence.json")), /SERIES_EVIDENCE_MISMATCH/);
});

test("only the earthquake profile parses", async () => {
  const storm = await read("./fixtures/governed-storm-events/admitted-snapshot.json");
  await assert.rejects(quakes.parseEarthquakePackage(storm), /MANIFEST_PROFILE_INVALID/);
  const snapshot = JSON.parse(await raw());
  snapshot.manifest.start = "2025-02-01";
  await assert.rejects(quakes.parseEarthquakePackage(JSON.stringify(snapshot)), /PACKAGE_DIGEST_MISMATCH/);
});
