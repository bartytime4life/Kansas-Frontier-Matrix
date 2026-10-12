import test from "node:test";
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { createRequire } from "node:module";
const require = createRequire(import.meta.url), ts = require("typescript");
const compile = text => ts.transpileModule(text, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const url = text => "data:text/javascript;base64," + Buffer.from(compile(text)).toString("base64");
const read = path => readFile(new URL(path, import.meta.url), "utf8");
const waterUrl = url(await read("../app/governed-water.ts"));
const weatherUrl = url((await read("../app/governed-weather.ts")).replace('"./governed-water"', JSON.stringify(waterUrl)));
const soil = await import(url((await read("../app/governed-soil.ts")).replace('"./governed-water"', JSON.stringify(waterUrl)).replace('"./governed-weather"', JSON.stringify(weatherUrl))));
const shared = await import(waterUrl);
const fixture = async name => JSON.parse(await read(`./fixtures/governed-soil/${name}.json`));
const NOW = "2026-10-11T13:00:00Z";
const pkg = async () => soil.parseSoilPackage(JSON.stringify(await fixture("admitted-snapshot")));

test("Worker and Python return identical released soil responses", async () => {
  const parsed = await pkg(), decision = await fixture("owner-decision");
  for (const view of ["bootstrap", "layers", "evidence"]) assert.deepEqual(await soil.projectSoil(parsed, decision, view, NOW), await fixture(view));
});

test("one station selects its five depth bundles and withheld values stay null", async () => {
  const parsed = await pkg(), decision = await fixture("owner-decision");
  const layers = await soil.projectSoil(parsed, decision, "layers", NOW, "53974");
  assert.deepEqual(layers.data.stations.map(s => s.id), ["53974"]);
  const withheld = layers.data.observations.filter(r => r.withheld);
  assert.deepEqual([...new Set(withheld.map(r => r.withheld))].sort(), ["MISSING", "OUT_OF_RANGE"]);
  assert.ok(withheld.every(r => r.value === null));
  const evidence = await soil.projectSoil(parsed, decision, "evidence", NOW, "53974");
  assert.deepEqual(evidence.data.entries.map(e => [e.station_id, e.series]), [5, 10, 20, 50, 100].map(d => ["53974", d]));
});

test("the soil gate refuses water and weather decisions, expiry, withdrawal and the rights hold", async () => {
  const parsed = await pkg(), decision = await fixture("owner-decision");
  assert.equal(soil.soilGate(parsed, decision, NOW), "ELIGIBLE");
  for (const profile of ["kfm.water-release-decision/v1", "kfm.weather-release-decision/v1"]) assert.equal(soil.soilGate(parsed, { ...decision, profile }, NOW), "RELEASE_BINDING_MISMATCH");
  assert.equal(soil.soilGate(parsed, { ...decision, correction_state: "WITHDRAWN" }, NOW), "CORRECTION_HOLD");
  assert.equal(soil.soilGate(parsed, decision, "2026-10-18T12:45:00Z"), "RELEASE_TIME_INVALID");
  assert.equal(soil.soilGate(parsed, null, NOW), "REVIEW_REQUIRED");
  // The weather license is not on the soil list, and a held bundle cannot be self-released.
  for (const entry of parsed.evidence.entries) entry.bundle.rights.license = "U.S. Public Domain (NOAA federal station data, 17 U.S.C. 105); preliminary data subject to revision";
  assert.equal(soil.soilGate(parsed, decision, NOW), "INDEPENDENT_REVIEW_REQUIRED");
  for (const denied of [null, { ...decision, expires_at: "2026-10-11T12:59:00Z" }]) {
    const result = await soil.projectSoil(await pkg(), denied, "layers", NOW);
    assert.equal(result.envelope.outcome, "ABSTAIN"); assert.equal(result.data, undefined);
  }
});

test("freshness follows the Kansas local day and soil moisture only", async () => {
  const parsed = await pkg(), decision = await fixture("owner-decision");
  const fresh = async (now, station) => (await soil.projectSoil(parsed, decision, "layers", now, station)).envelope.freshness;
  // Manhattan's latest moisture is 2026-10-10: at 03:00Z on the 14th it is still the 13th in Kansas (UTC-6).
  assert.equal(await fresh("2026-10-14T03:00:00Z", "53974"), "current");
  assert.equal(await fresh("2026-10-14T06:00:00Z", "53974"), "stale-accepted");
  // Oakley's moisture stopped on 2026-10-05; its later temperatures do not make it current.
  assert.equal(await fresh("2026-10-12T03:00:00Z", "03067"), "stale-accepted");
  parsed.candidate.observations = parsed.candidate.observations.map(r => r.variable === "SOIL_MOISTURE" ? { ...r, value: null } : r);
  assert.equal((await soil.projectSoil(parsed, decision, "layers", NOW)).envelope.freshness, "unknown");
});

test("tampered artifacts, other families and wrong windows are rejected", async () => {
  const tampered = await fixture("admitted-snapshot"); tampered.artifacts["candidate.json"] += " ";
  await assert.rejects(soil.parseSoilPackage(JSON.stringify(tampered)), /ARTIFACT_DIGEST/);
  for (const family of ["governed-water", "governed-weather"]) {
    const other = JSON.parse(await read(`./fixtures/${family}/admitted-snapshot.json`));
    await assert.rejects(soil.parseSoilPackage(JSON.stringify(other)), /MANIFEST_PROFILE_INVALID/);
  }
  const wrongWindow = await fixture("admitted-snapshot");
  wrongWindow.manifest.start = "2026-09-12";
  wrongWindow.manifest.package_id = await shared.digest(shared.canonical(shared.without(wrongWindow.manifest, "package_id")));
  await assert.rejects(soil.parseSoilPackage(JSON.stringify(wrongWindow)), /SNAPSHOT_INTERVAL_INVALID/);
});

test("the Site and Python soil license lists, offsets and stations agree", async () => {
  const policy = await read("../../../../packages/policy-runtime/src/policy_runtime/core.py");
  const block = /SOIL_SELF_RELEASE_LICENSES = frozenset\(\{\s*"([^"]+)",\s*\}\)/.exec(policy);
  assert.ok(block); assert.deepEqual([...soil.SOIL_SELF_RELEASE_LICENSES], [block[1]]);
  const projection = await read("../../../../packages/release/src/release/soil_projection.py");
  const offsets = /STANDARD_OFFSET_HOURS = (\{[^}]+\})/.exec(projection);
  assert.ok(offsets); assert.deepEqual(soil.SOIL_STANDARD_OFFSET_HOURS, JSON.parse(offsets[1]));
  const connector = await read("../../../../connectors/noaa/src/noaa/uscrn_daily.py");
  assert.deepEqual([...connector.matchAll(/"(\d{5})": "KS_/g)].map(m => m[1]), [...soil.SOIL_STATIONS]);
});

test("inner provenance, record and depth-bundle rules match the Python validator", async () => {
  const hex = value => value.slice(7);
  // Edit an artifact, then rehash every digest a forger can recompute, as the Python release code would.
  const forge = async (name, edit, { reseal = false, records = true } = {}) => {
    const snapshot = await fixture("admitted-snapshot"), texts = snapshot.artifacts;
    texts[name] = edit(texts[name]);
    if (reseal) {
      const swap = (from, to) => { for (const key of Object.keys(texts)) texts[key] = texts[key].replaceAll(from, to); };
      if (records) for (const record of shared.parseCapturedObject(texts["candidate.json"]).observations) {
        const fresh = await shared.digest(shared.capturedCanonical(record, "record_digest"));
        if (fresh !== record.record_digest) swap(hex(record.record_digest), hex(fresh));
      }
      const oldId = snapshot.manifest.candidate_id;
      const newId = await shared.digest(shared.capturedCanonical(shared.parseCapturedObject(texts["candidate.json"]), "candidate_id"));
      swap(hex(oldId), hex(newId)); snapshot.manifest.candidate_id = newId;
      const oldReceipt = JSON.parse(texts["validation.json"]).receipt_digest;
      swap(hex(oldReceipt), hex(await shared.digest(shared.capturedCanonical(shared.parseCapturedObject(texts["validation.json"]), "receipt_digest"))));
    }
    for (const key of Object.keys(texts)) snapshot.manifest.artifacts[key] = await shared.digest(texts[key]);
    snapshot.manifest.package_id = await shared.digest(shared.canonical(shared.without(snapshot.manifest, "package_id")));
    return JSON.stringify(snapshot);
  };
  const rejects = async (text, reason) => assert.rejects(soil.parseSoilPackage(text), new RegExp(reason));
  // Records are flat objects in the captured text; return each one's exact span.
  const spans = text => [...text.matchAll(/\{"datalogger_version":[^{}]*\}/g)].map(m => [m.index, m.index + m[0].length]);
  const first = '"source_token":"0.234","station_id":"03067","unit":"m3/m3","value":0.234,';
  assert.ok((await fixture("admitted-snapshot")).artifacts["candidate.json"].includes(first));
  await rejects(await forge("candidate.json", t => t.replace("Manhattan 6 SSW", "Manhattan Renamed")), "CANDIDATE_DIGEST_MISMATCH");
  await rejects(await forge("validation.json", t => t.replace(/"receipt_digest":"sha256:[0-9a-f]{64}"/, `"receipt_digest":"sha256:${"0".repeat(64)}"`)), "VALIDATION_RECEIPT_INVALID");
  // A resealed candidate id still cannot hide an edited value, a non-daily01 token or a false freshness claim.
  await rejects(await forge("candidate.json", t => t.replace('"value":0.234,', '"value":0.235,'), { reseal: true }), "OBSERVATION_VALUE_MISMATCH");
  await rejects(await forge("candidate.json", t => t.replace('"value":0.234,', '"value":0.235,'), { reseal: true, records: false }), "OBSERVATION_DIGEST_MISMATCH");
  await rejects(await forge("candidate.json", t => t.replace(first, first.replace('"0.234"', '"0.23"').replace("0.234,", "0.23,")), { reseal: true }), "OBSERVATION_TOKEN_INVALID");
  await rejects(await forge("candidate.json", t => t.replace('"03067":"STALE"', '"03067":"RECENT"'), { reseal: true }), "COVERAGE_OR_FRESHNESS_MISMATCH");
  // Dropping one value from a station-day, or reordering two depths, is refused even when resealed.
  await rejects(await forge("candidate.json", t => { const [a, b] = spans(t)[0]; return t.slice(0, a) + t.slice(b + 1); }, { reseal: true }), "STATION_DAY_INCOMPLETE");
  await rejects(await forge("candidate.json", t => { const [[a, b], [c, d]] = spans(t); return t.slice(0, a) + t.slice(c, d) + t.slice(b, c) + t.slice(a, b) + t.slice(d); }, { reseal: true }), "OBSERVATION_ORDER_INVALID");
  // The closed observation, candidate and station schemas apply before any digest, as in the Python validator.
  for (const [from, to] of [['"source_role":"reference_station"', '"source_role":"modeled"'], ['"datalogger_version":"2.622"', '"datalogger_version":"2 622"'], ['"depth_cm":5,', '"depth_cm":7,']]) {
    await rejects(await forge("candidate.json", t => t.replace(from, to), { reseal: true }), "SOIL_OBSERVATION_SCHEMA_INVALID");
  }
  await rejects(await forge("candidate.json", t => t.replace('"source_admission":"PENDING"', '"source_admission":"APPROVED"'), { reseal: true }), "CANDIDATE_AUTHORITY_OR_PROFILE_INVALID");
  await rejects(await forge("candidate.json", t => t.replace('"geometry":{"coordinates"', '"extra":1,"geometry":{"coordinates"'), { reseal: true }), "STATION_SHAPE_INVALID");
  // Retrieval after capture is caught to the microsecond.
  await rejects(await forge("candidate.json", t => t.replace('"retrieved_at":"2026-10-11T12:00:00Z","source_role"', '"retrieved_at":"2026-10-11T12:00:00.000001Z","source_role"'), { reseal: true }), "OBSERVATION_DATE_INVALID");
  // A depth bundle relabeled as another depth no longer matches its members.
  await rejects(await forge("evidence.json", t => t.replace('"series":5,', '"series":7,')), "SERIES_EVIDENCE_MISMATCH");
  await rejects(await forge("evidence.json", t => t.replace('"series":5,', '"series":"5",')), "SERIES_EVIDENCE_MISMATCH");
  // Number aliases are refused before any digest is compared.
  await rejects(await forge("candidate.json", t => t.replace('"value":0.234,', '"value":0.2340,')), "CAPTURED_JSON_NOT_CANONICAL");
  // The unedited fixture, resealed the same way, still parses: the forger's path is the honest one.
  assert.equal((await soil.parseSoilPackage(await forge("candidate.json", t => t, { reseal: true }))).manifest.candidate_id, (await pkg()).manifest.candidate_id);
});
