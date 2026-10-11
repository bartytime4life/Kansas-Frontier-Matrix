import test from "node:test";
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import ts from "typescript";

const source = await readFile(new URL("../app/governed-water.ts", import.meta.url), "utf8");
const compiled = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const water = await import("data:text/javascript;base64," + Buffer.from(compiled).toString("base64"));
const fixture = async () => JSON.parse(await readFile(new URL("./fixtures/governed-water/snapshot.json", import.meta.url), "utf8"));
const omit = (value, key) => Object.fromEntries(Object.entries(value).filter(([name]) => name !== key));
const values = snapshot => Object.fromEntries(Object.entries(snapshot.artifacts).map(([name, text]) => [name, JSON.parse(text)]));
const hash = value => water.digest(water.canonical(value));
async function refreshOuter(snapshot) {
  for (const [name, text] of Object.entries(snapshot.artifacts)) snapshot.manifest.artifacts[name] = await water.digest(text);
  snapshot.manifest.package_id = await hash(omit(snapshot.manifest, "package_id"));
  return JSON.stringify(snapshot);
}
async function reseal(snapshot, contents, { records = false, receipt = true } = {}) {
  const candidate = contents["candidate.json"], validation = contents["validation.json"], oldId = snapshot.manifest.candidate_id;
  if (records) for (const field of ["observations", "revision_history"]) for (const record of candidate[field]) record.record_digest = await hash(omit(record, "record_digest"));
  candidate.candidate_id = await hash(omit(candidate, "candidate_id"));
  const newId = candidate.candidate_id;
  for (const content of Object.values(contents)) content.candidate_id = newId;
  if (receipt) validation.receipt_digest = await hash(omit(validation, "receipt_digest"));
  for (const entry of contents["catalog.json"].entries) {
    entry.evidence_ref = entry.evidence_ref.replace(oldId.slice(7), newId.slice(7));
    entry.validation_ref = validation.receipt_digest;
  }
  for (const entry of contents["evidence.json"].entries) {
    const bundle = entry.bundle;
    bundle.bundle_id = bundle.bundle_id.replace(oldId.slice(7), newId.slice(7));
    entry.evidence_ref.ref = entry.evidence_ref.ref.replace(oldId.slice(7), newId.slice(7));
    entry.evidence_ref.bundle_ref = bundle.bundle_id;
    bundle.evidence_refs[0] = entry.evidence_ref;
    for (const ref of bundle.evidence_refs) ref.bundle_ref = bundle.bundle_id;
    bundle.checksums = { candidate: newId, validation: validation.receipt_digest };
    bundle.spec_hash = { value: await hash(omit(bundle, "spec_hash")) };
    const history = entry.verification_history;
    history.subject_ref = entry.evidence_ref.ref;
    history.events[0].basis_refs = ["kfm://receipt/validation/" + validation.receipt_digest.slice(7)];
    history.spec_hash = await hash(omit(history, "spec_hash"));
  }
  snapshot.manifest.candidate_id = newId;
  for (const [name, content] of Object.entries(contents)) snapshot.artifacts[name] = water.canonical(content);
  return refreshOuter(snapshot);
}

test("refreshed carrier hashes cannot retain a stale candidate identity after a measurement change", async () => {
  const snapshot = await fixture(), candidate = JSON.parse(snapshot.artifacts["candidate.json"]);
  candidate.observations[0].value = 17.5;
  snapshot.artifacts["candidate.json"] = water.canonical(candidate);
  await assert.rejects(water.parseWaterPackage(await refreshOuter(snapshot)), /CANDIDATE_DIGEST_MISMATCH/);
});

for (const field of ["observations", "revision_history"]) test(`independently resealed candidate cannot retain a stale ${field} record digest`, async () => {
  const snapshot = await fixture(), contents = values(snapshot);
  contents["candidate.json"][field][0].value = 17.5;
  await assert.rejects(water.parseWaterPackage(await reseal(snapshot, contents)), /OBSERVATION_DIGEST_MISMATCH/);
});

test("refreshed carrier hashes cannot retain a stale validation receipt digest", async () => {
  const snapshot = await fixture(), contents = values(snapshot);
  contents["validation.json"].release_authorized = true;
  await assert.rejects(water.parseWaterPackage(await reseal(snapshot, contents, { receipt: false })), /VALIDATION_RECEIPT_INVALID/);
});

for (const [field, value] of [["profile", "kfm.forged-validation/v1"], ["observations", 1], ["review_required", false], ["promotion_authorized", true], ["release_authorized", true], ["publication_authorized", true], ["extra_authority", true]]) test(`a fully resealed receipt cannot change ${field}`, async () => {
  const snapshot = await fixture(), contents = values(snapshot);
  contents["validation.json"][field] = value;
  await assert.rejects(water.parseWaterPackage(await reseal(snapshot, contents)), /VALIDATION_RECEIPT_MISMATCH/);
});

test("a fully resealed record must retain its stable measurement identity", async () => {
  const snapshot = await fixture(), contents = values(snapshot);
  contents["candidate.json"].observations[0].time_series_id = "changed-series";
  await assert.rejects(water.parseWaterPackage(await reseal(snapshot, contents, { records: true })), /OBSERVATION_IDENTITY_MISMATCH/);
});

test("fully resealed revision history must match the observations selected for serving", async () => {
  const snapshot = await fixture(), contents = values(snapshot);
  contents["candidate.json"].revision_history[0].value = 17.5;
  await assert.rejects(water.parseWaterPackage(await reseal(snapshot, contents, { records: true })), /LATEST_REVISION_MISMATCH/);
});

test("fully resealed record times and provisional status remain bound to provider provenance", async () => {
  for (const mutation of [record => record.provider_revision_at = "2026-09-30T18:00:00.000001Z", record => record.provisional = false]) {
    const snapshot = await fixture(), contents = values(snapshot);
    mutation(contents["candidate.json"].revision_history[0]);
    // A revision one microsecond after observation is valid; make the retrieval
    // one microsecond earlier so millisecond truncation would wrongly allow it.
    if (contents["candidate.json"].revision_history[0].provisional) contents["candidate.json"].revision_history[0].retrieved_at = "2026-09-30T18:00:00Z";
    await assert.rejects(water.parseWaterPackage(await reseal(snapshot, contents, { records: true })), /OBSERVATION_TIME_MISMATCH|PROVISIONAL_STATUS_MISMATCH/);
  }
});

test("duplicate provider revisions cannot be hidden inside a fully resealed history", async () => {
  const snapshot = await fixture(), contents = values(snapshot);
  contents["candidate.json"].revision_history.push(structuredClone(contents["candidate.json"].revision_history[0]));
  await assert.rejects(water.parseWaterPackage(await reseal(snapshot, contents, { records: true })), /DUPLICATE_REVISION/);
});

test("Python-produced float tokens, exact large integers and codepoint-sorted metadata retain their identities", async () => {
  // Generated with Python json.dumps(ensure_ascii=False, allow_nan=False,
  // sort_keys=True, separators=(",", ":")); kept outside historical fixtures.
  const snapshot = JSON.parse(await readFile(new URL("./fixtures/governed-water-integrity/python-numbers.json", import.meta.url), "utf8"));
  const text = snapshot.artifacts["candidate.json"];
  assert.match(text, /"value":1\.0/);
  assert.match(text, /"value":1e-07/);
  assert.match(text, /"value":-0\.0/);
  assert.match(text, /"coordinates":\[-98\.0,38\.0\]/);
  assert.match(text, /9007199254740993/);
  const pkg = await water.parseWaterPackage(JSON.stringify(snapshot));
  assert.deepEqual(pkg.candidate.observations.map(record => record.value), [1, 1e-7]);
  // The newest revision is one microsecond later in the same millisecond.
  assert.equal(pkg.candidate.observations[0].provider_revision_at, "2026-09-30T18:00:01.123457Z");
});

test("equal JavaScript numeric values cannot conceal changed captured numeric identities", async () => {
  const original = JSON.parse(await readFile(new URL("./fixtures/governed-water-integrity/python-numbers.json", import.meta.url), "utf8"));
  for (const [before, after] of [['"value":1.0', '"value":1'], ['"value":-0.0', '"value":0.0'], ["-98.0", "-98"], ["9007199254740993", "9007199254740992"]]) {
    const snapshot = structuredClone(original);
    snapshot.artifacts["candidate.json"] = snapshot.artifacts["candidate.json"].replace(before, after);
    await assert.rejects(water.parseWaterPackage(await refreshOuter(snapshot)), /CANDIDATE_DIGEST_MISMATCH/);
  }
});

test("captured artifacts reject noncanonical aliases, whitespace, key order and escaped strings", async () => {
  const original = await fixture();
  for (const mutate of [
    text => " " + text,
    text => text.replace('"candidate_id":', '"candidate_\\u0069d":'),
    text => text.replace('"value":12.5', '"value":12.50'),
    text => text.replace('"value":12.5', '"value":1.25e+01'),
    text => JSON.stringify(Object.fromEntries(Object.entries(JSON.parse(text)).reverse())),
  ]) {
    const snapshot = structuredClone(original);
    snapshot.artifacts["candidate.json"] = mutate(snapshot.artifacts["candidate.json"]);
    await assert.rejects(water.parseWaterPackage(await refreshOuter(snapshot)), /CAPTURED_JSON_NOT_CANONICAL/);
  }
});

test("malformed, escaped duplicate, deep, nonfinite and impossible-time carriers fail safely", async () => {
  const original = await fixture();
  for (const mutate of [
    text => text.slice(0, -1),
    text => text.replace('{"candidate_id":', '{"candidate_\\u0069d":"duplicate","candidate_id":'),
    text => text.replace('"horizontal_accuracy":null', '"horizontal_accuracy":' + '['.repeat(33) + '0' + ']'.repeat(33)),
    text => text.replace('"value":12.5', '"value":1e999'),
  ]) {
    const snapshot = structuredClone(original);
    snapshot.artifacts["candidate.json"] = mutate(snapshot.artifacts["candidate.json"]);
    await assert.rejects(water.parseWaterPackage(await refreshOuter(snapshot)));
  }
  const snapshot = await fixture(), contents = values(snapshot);
  contents["candidate.json"].revision_history[0].retrieved_at = "2026-09-31T18:01:00Z";
  await assert.rejects(water.parseWaterPackage(await reseal(snapshot, contents, { records: true })), /TIME_INVALID/);
});
