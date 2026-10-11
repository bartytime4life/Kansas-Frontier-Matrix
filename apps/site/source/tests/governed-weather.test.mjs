import test from "node:test";
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { createRequire } from "node:module";
const require = createRequire(import.meta.url), ts = require("typescript");
const compile = text => ts.transpileModule(text, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const url = text => "data:text/javascript;base64," + Buffer.from(compile(text)).toString("base64");
const read = path => readFile(new URL(path, import.meta.url), "utf8");
const waterUrl = url(await read("../app/governed-water.ts"));
const weather = await import(url((await read("../app/governed-weather.ts")).replace('"./governed-water"', JSON.stringify(waterUrl))));
const fixture = async name => JSON.parse(await read(`./fixtures/governed-weather/${name}.json`));
const NOW = "2026-10-11T13:00:00Z";
const pkg = async () => weather.parseWeatherPackage(JSON.stringify(await fixture("admitted-snapshot")));

test("Worker and Python return identical released weather responses", async () => {
  const parsed = await pkg(), decision = await fixture("owner-decision");
  for (const view of ["bootstrap", "layers", "evidence"]) assert.deepEqual(await weather.projectWeather(parsed, decision, view, NOW), await fixture(view));
});

test("one station can be selected and withheld values stay null", async () => {
  const layers = await weather.projectWeather(await pkg(), await fixture("owner-decision"), "layers", NOW, "USW00003928");
  assert.deepEqual(layers.data.stations.map(s => s.id), ["USW00003928"]);
  const withheld = layers.data.observations.filter(r => r.withheld);
  assert.ok(withheld.length > 0 && withheld.every(r => r.value === null));
  assert.deepEqual(Object.keys(layers.data.freshness_at_capture), ["USW00003928"]);
});

test("the weather gate refuses water decisions, expiry, withdrawal and the rights hold", async () => {
  const parsed = await pkg(), decision = await fixture("owner-decision");
  assert.equal(weather.weatherGate(parsed, decision, NOW), "ELIGIBLE");
  assert.equal(weather.weatherGate(parsed, { ...decision, profile: "kfm.water-release-decision/v1" }, NOW), "RELEASE_BINDING_MISMATCH");
  assert.equal(weather.weatherGate(parsed, { ...decision, correction_state: "WITHDRAWN" }, NOW), "CORRECTION_HOLD");
  assert.equal(weather.weatherGate(parsed, decision, "2026-10-18T12:45:00Z"), "RELEASE_TIME_INVALID");
  assert.equal(weather.weatherGate(parsed, null, NOW), "REVIEW_REQUIRED");
  // The NOAA license is not on the water list, and a held bundle cannot be self-released.
  for (const entry of parsed.evidence.entries) entry.bundle.rights.license = "NOAA NCEI source terms; independent rights review required";
  assert.equal(weather.weatherGate(parsed, decision, NOW), "INDEPENDENT_REVIEW_REQUIRED");
  for (const denied of [null, { ...decision, expires_at: "2026-10-11T12:59:00Z" }]) {
    const result = await weather.projectWeather(await pkg(), denied, "layers", NOW);
    assert.equal(result.envelope.outcome, "ABSTAIN"); assert.equal(result.data, undefined);
  }
});

test("freshness follows station-local days and ignores withheld values", async () => {
  const parsed = await pkg(), decision = await fixture("owner-decision");
  const late = await weather.projectWeather(parsed, decision, "layers", "2026-10-13T13:00:00Z");
  assert.equal(late.envelope.freshness, "current");
  const stale = await weather.projectWeather(parsed, decision, "layers", "2026-10-13T13:00:00Z", "USW00023065");
  assert.equal(stale.envelope.freshness, "stale-accepted");
  // Wichita's latest value is 2026-10-10: at 03:00Z on the 14th it is still the 13th in Kansas (UTC-6).
  const fresh = async (now, station) => (await weather.projectWeather(parsed, decision, "layers", now, station)).envelope.freshness;
  assert.equal(await fresh("2026-10-14T03:00:00Z", "USW00003928"), "current");
  assert.equal(await fresh("2026-10-14T06:00:00Z", "USW00003928"), "stale-accepted");
  parsed.candidate.observations = parsed.candidate.observations.map(r => ({ ...r, value: null }));
  assert.equal((await weather.projectWeather(parsed, decision, "layers", NOW)).envelope.freshness, "unknown");
});

test("tampered artifacts, water packages and impossible dates are rejected", async () => {
  const tampered = await fixture("admitted-snapshot"); tampered.artifacts["candidate.json"] += " ";
  await assert.rejects(weather.parseWeatherPackage(JSON.stringify(tampered)), /ARTIFACT_DIGEST/);
  const water = JSON.parse(await read("./fixtures/governed-water/admitted-snapshot.json"));
  await assert.rejects(weather.parseWeatherPackage(JSON.stringify(water)), /MANIFEST_PROFILE_INVALID/);
  for (const bad of ["2026-09-31", "0000-10-01", "2026-10-1"]) assert.throws(() => weather.day(bad), /DATE_INVALID/);
  const wrongWindow = await fixture("admitted-snapshot");
  wrongWindow.manifest.start = "2026-09-12";
  const shared = await import(waterUrl);
  wrongWindow.manifest.package_id = await shared.digest(shared.canonical(shared.without(wrongWindow.manifest, "package_id")));
  await assert.rejects(weather.parseWeatherPackage(JSON.stringify(wrongWindow)), /SNAPSHOT_INTERVAL_INVALID/);
});

test("the Site and Python weather license lists agree", async () => {
  const python = await read("../../../../packages/policy-runtime/src/policy_runtime/core.py");
  const block = /WEATHER_SELF_RELEASE_LICENSES = frozenset\(\{\s*"([^"]+)",\s*\}\)/.exec(python);
  assert.ok(block); assert.deepEqual([...weather.WEATHER_SELF_RELEASE_LICENSES], [block[1]]);
});

test("inner provenance and record rules match the Python validator", async () => {
  const shared = await import(waterUrl);
  const hex = value => value.slice(7);
  // Edit an artifact, then rehash every digest a forger can recompute, as the Python release code would.
  const forge = async (name, edit, { reseal = false } = {}) => {
    const snapshot = await fixture("admitted-snapshot"), texts = snapshot.artifacts;
    texts[name] = edit(texts[name]);
    if (reseal) {
      const swap = (from, to) => { for (const key of Object.keys(texts)) texts[key] = texts[key].replaceAll(from, to); };
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
  const rejects = async (text, reason) => assert.rejects(weather.parseWeatherPackage(text), new RegExp(reason));
  await rejects(await forge("candidate.json", t => t.replace("WICHITA DWIGHT D EISENHOWER NA", "WICHITA RENAMED")), "CANDIDATE_IDENTITY_MISMATCH");
  await rejects(await forge("validation.json", t => t.replace(/"receipt_digest":"sha256:[0-9a-f]{64}"/, `"receipt_digest":"sha256:${"0".repeat(64)}"`)), "VALIDATION_RECEIPT_INVALID");
  // A resealed candidate id still cannot hide an edited record, a mismatched reading or a false freshness claim.
  await rejects(await forge("candidate.json", t => t.replace('"value":0.8,', '"value":0.9,'), { reseal: true }), "OBSERVATION_DIGEST_MISMATCH");
  await rejects(await forge("candidate.json", t => t.replace('"USW00023065":"STALE"', '"USW00023065":"RECENT"'), { reseal: true }), "COVERAGE_OR_FRESHNESS_MISMATCH");
  // Number aliases are refused before any digest is compared.
  await rejects(await forge("candidate.json", t => t.replace('"value":0.8,', '"value":0.80,')), "CAPTURED_JSON_NOT_CANONICAL");
  // The unedited fixture, resealed the same way, still parses: the forger's path is the honest one.
  assert.equal((await weather.parseWeatherPackage(await forge("candidate.json", t => t, { reseal: true }))).manifest.candidate_id, (await pkg()).manifest.candidate_id);
});

test("the Site and Python station-local offsets agree", async () => {
  const python = await read("../../../../packages/release/src/release/weather_projection.py");
  const block = /STANDARD_OFFSET_HOURS = (\{[^}]+\})/.exec(python);
  assert.ok(block); assert.deepEqual(weather.STANDARD_OFFSET_HOURS, JSON.parse(block[1]));
  assert.deepEqual(Object.keys(weather.STANDARD_OFFSET_HOURS).sort(), [...weather.WEATHER_STATIONS].sort());
});
