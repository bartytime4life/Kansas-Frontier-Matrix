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
const storm = await import(url((await read("../app/governed-storm-events.ts")).replace('"./governed-water"', JSON.stringify(waterUrl)).replace('"./governed-weather"', JSON.stringify(weatherUrl))));
const fixture = async name => JSON.parse(await read(`./fixtures/governed-storm-events/${name}.json`));
const raw = async () => await read("./fixtures/governed-storm-events/admitted-snapshot.json");
const NOW = "2025-11-02T13:00:00Z";
const pkg = async () => storm.parseStormEventsPackage(await raw());
const omit = (value, key) => Object.fromEntries(Object.entries(value).filter(([name]) => name !== key));
const sha = text => "sha256:" + createHash("sha256").update(text).digest("hex");
// Python canonical_bytes: sorted keys, compact separators, non-ASCII escaped as json.dumps does by default.
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

test("Worker and Python return identical released storm events responses", async () => {
  const parsed = await pkg(), decision = await fixture("owner-decision");
  for (const view of ["bootstrap", "layers", "evidence"]) assert.deepEqual(await storm.projectStormEvents(parsed, decision, view, NOW), await fixture(view));
  assert.deepEqual(await storm.projectStormEvents(parsed, decision, "layers", NOW, 5), await fixture("layers-may"));
});

test("a month selects its parts, and the selection describes exactly the returned records", async () => {
  const parsed = await pkg(), decision = await fixture("owner-decision");
  const may = await storm.projectStormEvents(parsed, decision, "layers", NOW, 5);
  assert.deepEqual(may.data.observations.map(r => r.event_id), [9000102]);
  assert.deepEqual(may.data.selection, { months: [5], observation_count: 1, event_types: { Hail: 1 }, latest_event_date: "2025-05-19" });
  assert.equal(may.data.dataset.scope, "data_year");
  assert.equal(may.data.dataset.observation_count, 6);
  const none = await storm.projectStormEvents(parsed, decision, "layers", NOW, 2);
  assert.equal(none.envelope.reason_code, "EVIDENCE_NOT_FOUND");
  assert.equal(none.data, undefined);
  const layers = await storm.projectStormEvents(parsed, decision, "layers", NOW);
  assert.equal(layers.data.life_safety, "not_for_life_safety");
  assert.ok(!JSON.stringify(layers).includes("Synthetic narrative"));
});

test("the storm events gate refuses other families' decisions, expiry, withdrawal and the rights hold", async () => {
  const parsed = await pkg(), decision = await fixture("owner-decision");
  assert.equal(storm.stormEventsGate(parsed, decision, NOW), "ELIGIBLE");
  for (const profile of ["kfm.water-release-decision/v1", "kfm.weather-release-decision/v1", "kfm.soil-release-decision/v1"]) assert.equal(storm.stormEventsGate(parsed, { ...decision, profile }, NOW), "RELEASE_BINDING_MISMATCH");
  assert.equal(storm.stormEventsGate(parsed, { ...decision, correction_state: "WITHDRAWN" }, NOW), "CORRECTION_HOLD");
  assert.equal(storm.stormEventsGate(parsed, decision, "2025-11-09T12:45:00Z"), "RELEASE_TIME_INVALID");
  assert.equal(storm.stormEventsGate(parsed, null, NOW), "REVIEW_REQUIRED");
  // The soil license is not on the storm events list, so the owner cannot self-release it.
  for (const entry of parsed.evidence.entries) entry.bundle.rights.license = "U.S. Public Domain (NOAA federal station data, 17 U.S.C. 105); USCRN data subject to revision";
  assert.equal(storm.stormEventsGate(parsed, decision, NOW), "INDEPENDENT_REVIEW_REQUIRED");
});

test("freshness is the age of the NCEI file vintage", async () => {
  const parsed = await pkg(), decision = { ...(await fixture("owner-decision")), expires_at: "2025-12-30T00:00:00Z" };
  const fresh = async now => (await storm.projectStormEvents(parsed, decision, "bootstrap", now)).envelope.freshness;
  // The vintage is 2025-10-20: current through 45 days, then stale-accepted.
  assert.equal(await fresh("2025-12-04T23:59:59Z"), "current");
  assert.equal(await fresh("2025-12-05T00:00:00Z"), "stale-accepted");
});

test("damage strings parse exactly, and blank stays unreported", () => {
  assert.equal(storm.parseDamage(""), null);
  assert.equal(storm.parseDamage("250.00K"), 250000);
  assert.equal(storm.parseDamage("1.5K"), 1500);
  assert.equal(storm.parseDamage("2.00M"), 2000000);
  assert.equal(storm.parseDamage("0.00K"), 0);
  assert.equal(storm.parseDamage(" 10k "), 10000);
  for (const bad of ["abc", "1.2345K", "1..0K", "-5K", "1e3"]) assert.throws(() => storm.parseDamage(bad));
});

test("month bundles split into parts of 127 records", () => {
  const events = Array.from({ length: 256 }, (_, i) => ({ begin_local: "2025-05-01T00:00", event_id: i + 1 }));
  assert.deepEqual(storm.stormMonthGroups(events).map(([m, p, r]) => [m, p, r.length]), [[5, 1, 127], [5, 2, 127], [5, 3, 2]]);
});

/** Change candidate records and reseal every record digest, the candidate id, its bindings and the receipt,
 *  so only the Python validator's semantic rules can refuse the package. */
async function forgedCandidate(mutate) {
  const snapshot = JSON.parse(await raw()), candidate = JSON.parse(snapshot.artifacts["candidate.json"]);
  mutate(candidate);
  for (const r of candidate.observations) r.record_digest = sha(pyJson(omit(r, "record_digest")));
  candidate.candidate_id = sha(pyJson(omit(candidate, "candidate_id")));
  const report = omit({ ...JSON.parse(snapshot.artifacts["validation.json"]), candidate_id: candidate.candidate_id }, "receipt_digest");
  const texts = { "candidate.json": pyJson(candidate), "validation.json": pyJson({ ...report, receipt_digest: sha(pyJson(report)) }) };
  for (const name of ["catalog.json", "evidence.json"]) texts[name] = pyJson({ ...JSON.parse(snapshot.artifacts[name]), candidate_id: candidate.candidate_id });
  for (const [name, text] of Object.entries(texts)) { snapshot.artifacts[name] = text; snapshot.manifest.artifacts[name] = sha(text); }
  snapshot.manifest.candidate_id = candidate.candidate_id;
  snapshot.manifest.package_id = sha(pyJson(omit(snapshot.manifest, "package_id")));
  return JSON.stringify(snapshot);
}

test("resealed packages that break the Python validator's rules are refused", async () => {
  const cases = [
    [c => { c.observations[0].damage_property_usd = 2500000; }, "RECORD_DAMAGE_MISMATCH"],
    [c => { c.observations[0].begin_utc = "2025-04-28T22:12Z"; }, "RECORD_UTC_MISMATCH"],
    [c => { c.observations[4].flags = []; }, "RECORD_FLAGS_MISMATCH"],
    [c => { c.observations[4].begin_local = "2025-07-99T03:00"; }, "RECORD_TIME_INVALID"],
    [c => { c.observations.reverse(); }, "RECORD_ORDER_OR_DUPLICATE"],
    [c => { c.observations[0].narrative = "x"; }, "STORM_EVENT_SCHEMA_INVALID"],
    [c => { c.withheld_rows = 0; }, "WITHHELD_COUNTS_INVALID"],
    [c => { c.latest_event_date = "2025-12-31"; }, "LATEST_EVENT_DATE_MISMATCH"],
    [c => { c.freshness_at_capture = "STALE"; }, "FRESHNESS_MISMATCH"],
    [c => { c.vintage_created = "2025-10-21"; }, "CANDIDATE_SOURCE_FILE_INVALID"],
    [c => { c.coverage = "COMPLETE"; }, "CANDIDATE_AUTHORITY_OR_PROFILE_INVALID"],
  ];
  for (const [mutate, reason] of cases) await assert.rejects(storm.parseStormEventsPackage(await forgedCandidate(mutate)), new RegExp(reason), reason);
  // An unsealed change is caught by the candidate digest, and a released carrier is refused outright.
  await assert.rejects(storm.parseStormEventsPackage(await resealed(c => { c.observations[0].deaths_direct = 3; })), /CANDIDATE_DIGEST_MISMATCH/);
  await assert.rejects(storm.parseStormEventsPackage(await resealed(c => { c.release_state = "RELEASED"; })), /CARRIER_CANNOT_SELF_APPROVE/);
  // A forged catalog cannot misreport the year it describes.
  await assert.rejects(storm.parseStormEventsPackage(await resealed(c => { c.dataset.observation_count = 600; }, "catalog.json")), /CATALOG_MISMATCH/);
  // Evidence must be exactly the month parts the records produce.
  await assert.rejects(storm.parseStormEventsPackage(await resealed(e => { e.entries.pop(); }, "evidence.json")), /EVIDENCE_CLOSURE_INVALID/);
  await assert.rejects(storm.parseStormEventsPackage(await resealed(e => { e.entries[0].month = 2; }, "evidence.json")), /SERIES_EVIDENCE_MISMATCH/);
});

test("only the storm events profile parses", async () => {
  const soil = await read("./fixtures/governed-soil/admitted-snapshot.json");
  await assert.rejects(storm.parseStormEventsPackage(soil), /MANIFEST_PROFILE_INVALID/);
  const snapshot = JSON.parse(await raw());
  snapshot.manifest.start = "2025-02-01";
  await assert.rejects(storm.parseStormEventsPackage(JSON.stringify(snapshot)), /PACKAGE_DIGEST_MISMATCH/);
});
