import test from "node:test";
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { DatabaseSync } from "node:sqlite";
import ts from "typescript";

const compile = text => ts.transpileModule(text, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const moduleUrl = text => "data:text/javascript;base64," + Buffer.from(compile(text)).toString("base64");
const read = path => readFile(new URL(path, import.meta.url), "utf8");
const waterUrl = moduleUrl(await read("../app/governed-water.ts"));
const weatherUrl = moduleUrl((await read("../app/governed-weather.ts")).replace('"./governed-water"', JSON.stringify(waterUrl)));
const stormUrl = moduleUrl((await read("../app/governed-storm-events.ts")).replace('"./governed-water"', JSON.stringify(waterUrl)).replace('"./governed-weather"', JSON.stringify(weatherUrl)));
const quakeUrl = moduleUrl((await read("../app/governed-earthquakes.ts")).replace('"./governed-water"', JSON.stringify(waterUrl)).replace('"./governed-weather"', JSON.stringify(weatherUrl)));
const waterAdminUrl = moduleUrl((await read("../app/governed-water-admin.ts")).replace('"./governed-water"', JSON.stringify(waterUrl)));
const stormAdmin = await import(moduleUrl((await read("../app/governed-storm-events-admin.ts")).replace('"./governed-water-admin"', JSON.stringify(waterAdminUrl)).replace('"./governed-storm-events"', JSON.stringify(stormUrl))));
const admin = await import(moduleUrl((await read("../app/governed-earthquakes-admin.ts"))
  .replace('"./governed-water-admin"', JSON.stringify(waterAdminUrl)).replace('"./governed-earthquakes"', JSON.stringify(quakeUrl))));
const waterAdmin = await import(waterAdminUrl);
const quakes = await read("./fixtures/governed-earthquakes/admitted-snapshot.json");
const decision = JSON.parse(await read("./fixtures/governed-earthquakes/owner-decision.json"));
const water = await read("./fixtures/governed-water/admitted-snapshot.json");
const storm = await read("./fixtures/governed-storm-events/admitted-snapshot.json");
const stormDecision = JSON.parse(await read("./fixtures/governed-storm-events/owner-decision.json"));
const NOW = "2025-11-02T13:00:00Z";

// D1 stand-in: every governed migration on SQLite, with D1's prepare/bind/first/run/batch surface.
async function store() {
  const sqlite = new DatabaseSync(":memory:");
  for (const name of ["0001_governed_water", "0006_governed_weather", "0007_governed_soil", "0008_governed_storm_events", "0009_governed_earthquakes"]) sqlite.exec((await read(`../drizzle/${name}.sql`)).replaceAll("--> statement-breakpoint", ""));
  const statement = (sql, values = []) => ({
    bind: (...next) => statement(sql, next),
    first: async () => sqlite.prepare(sql).get(...values) ?? null,
    run: async () => ({ meta: { changes: Number(sqlite.prepare(sql).run(...values).changes) } }),
  });
  const objects = new Map();
  return {
    sqlite, objects,
    db: {
      prepare: sql => statement(sql),
      batch: async statements => {
        sqlite.exec("BEGIN");
        try { const results = []; for (const s of statements) results.push(await s.run()); sqlite.exec("COMMIT"); return results; }
        catch (error) { sqlite.exec("ROLLBACK"); throw error; }
      },
    },
    bucket: {
      get: async key => objects.has(key) ? { size: Buffer.byteLength(objects.get(key)), text: async () => objects.get(key) } : null,
      put: async (key, value) => { objects.set(key, value); },
    },
  };
}
const rejects = (promise, reason) => assert.rejects(promise, error => error.message === reason);
const count = (s, table) => s.sqlite.prepare(`SELECT COUNT(*) AS n FROM ${table}`).get().n;

test("earthquake staging uses its own prefix and table, and refuses other families' packages", async () => {
  const s = await store();
  const staged = await admin.stageEarthquakePackage(s, quakes, "staging-token", NOW);
  assert.deepEqual(staged, { package_id: decision.package_id, state: "STAGED", activated: false });
  assert.deepEqual([...s.objects.keys()], [admin.earthquakesObjectKey(decision.package_id)]);
  assert.ok(admin.earthquakesObjectKey(decision.package_id).startsWith("governed-earthquakes/v1/objects/"));
  assert.equal(count(s, "earthquakes_packages"), 1);
  assert.equal(count(s, "water_packages") + count(s, "weather_packages") + count(s, "soil_packages") + count(s, "storm_events_packages") + count(s, "earthquakes_active"), 0);
  for (const other of [water, storm]) await rejects(admin.stageEarthquakePackage(s, other, "staging-token", NOW), "PACKAGE_INVALID");
  await rejects(waterAdmin.stageWaterPackage(s, quakes, "staging-token", NOW), "PACKAGE_INVALID");
  await rejects(stormAdmin.stageStormEventsPackage(s, quakes, "staging-token", NOW), "PACKAGE_INVALID");
});

test("activation passes the earthquake gate and leaves the other families unserved", async () => {
  const s = await store();
  await admin.stageEarthquakePackage(s, quakes, "staging-token", NOW);
  for (const profile of ["kfm.water-release-decision/v1", "kfm.weather-release-decision/v1", "kfm.soil-release-decision/v1", "kfm.storm-events-release-decision/v1"]) {
    await rejects(admin.activateEarthquakePackage(s, { package_id: decision.package_id, decision: { ...decision, profile }, expected_active: null }, NOW), "RELEASE_BINDING_MISMATCH");
  }
  await rejects(admin.activateEarthquakePackage(s, { package_id: decision.package_id, decision, expected_active: null }, "2025-11-09T12:45:00Z"), "RELEASE_TIME_INVALID");
  const activated = await admin.activateEarthquakePackage(s, { package_id: decision.package_id, decision, expected_active: null }, NOW);
  assert.equal(activated.outcome, "ACTIVATED");
  assert.match(activated.event_id, /^earthquakes:[a-f0-9]{32}$/);
  assert.equal(count(s, "earthquakes_activation_events"), 1);
  assert.equal(count(s, "water_active") + count(s, "weather_active") + count(s, "soil_active") + count(s, "storm_events_active") + count(s, "storm_events_activation_events"), 0);
  assert.deepEqual(await admin.earthquakesAdminStatus(s), { active_package_id: decision.package_id, previous_package_id: null, revision: 1, decision_expires_at: decision.expires_at });
  assert.equal((await stormAdmin.stormEventsAdminStatus(s)).active_package_id, null);
  // A storm events activation cannot point at an earthquake package: it was never staged as storm events.
  await rejects(stormAdmin.activateStormEventsPackage(s, { package_id: decision.package_id, decision: stormDecision, expected_active: null }, NOW), "ACTIVATION_BINDING_MISMATCH");
  await rejects(stormAdmin.activateStormEventsPackage(s, { package_id: decision.package_id, decision: { ...stormDecision, package_id: decision.package_id }, expected_active: null }, NOW), "PACKAGE_NOT_STAGED");
  await rejects(admin.activateEarthquakePackage(s, { package_id: decision.package_id, decision, expected_active: null }, NOW), "ACTIVATION_CONFLICT");
});

test("withdrawal is compare-and-swap and stops the earthquake package only", async () => {
  const s = await store();
  await admin.stageEarthquakePackage(s, quakes, "staging-token", NOW);
  await admin.activateEarthquakePackage(s, { package_id: decision.package_id, decision, expected_active: null }, NOW);
  await rejects(admin.withdrawEarthquakePackage(s, { package_id: decision.package_id, expected_active: null }, NOW), "WITHDRAW_CONFLICT");
  const withdrawn = await admin.withdrawEarthquakePackage(s, { package_id: decision.package_id, expected_active: decision.package_id }, NOW);
  assert.equal(withdrawn.outcome, "WITHDRAWN");
  assert.equal(s.sqlite.prepare("SELECT state FROM earthquakes_packages").get().state, "WITHDRAWN");
  assert.equal(s.sqlite.prepare("SELECT action FROM earthquakes_activation_events ORDER BY rowid DESC").get().action, "WITHDRAW");
});

// The read adapter, with its Cloudflare bindings swapped for the stand-in store.
const server = (await read("../app/governed-earthquakes-server.ts"))
  .replace('import { env } from "cloudflare:workers";', "const env = new Proxy({}, { get: (_, key) => globalThis.__quakeStorage.env[key] });")
  .replace('import { getRawDb } from "../db";', "const getRawDb = () => globalThis.__quakeStorage.db;")
  .replace('"./governed-water"', JSON.stringify(waterUrl)).replace('"./governed-earthquakes"', JSON.stringify(quakeUrl));
globalThis.__quakeStorage = { env: {}, db: null };
const { governedEarthquakesRead } = await import(moduleUrl(server));
const RealDate = Date;
async function request(view, query = "", clock = NOW) {
  class TestDate extends RealDate { constructor(...args) { super(...(args.length ? args : [clock])); } static now() { return RealDate.parse(clock); } }
  globalThis.Date = TestDate;
  try { const response = await governedEarthquakesRead(new Request("https://example.test/api/governed/earthquakes/v1/" + view + query), view); return { status: response.status, body: await response.json() }; }
  finally { globalThis.Date = RealDate; }
}

test("the read route serves only the active, staged earthquake package within its approval", async () => {
  const s = await store();
  globalThis.__quakeStorage = { env: { BUCKET: s.bucket }, db: s.db };
  assert.equal((await request("layers")).body.envelope.reason_code, "NO_APPROVED_SNAPSHOT");
  await admin.stageEarthquakePackage(s, quakes, "staging-token", NOW);
  await admin.activateEarthquakePackage(s, { package_id: decision.package_id, decision, expected_active: null }, NOW);
  for (const view of ["bootstrap", "layers", "evidence"]) {
    const { status, body } = await request(view);
    // The Worker clock carries milliseconds, so issued_at (and the envelope's spec_hash) differ from the fixture.
    const expected = JSON.parse(await read(`./fixtures/governed-earthquakes/${view}.json`));
    assert.equal(status, 200);
    assert.deepEqual(body.data, expected.data);
    assert.equal(body.envelope.outcome, "ANSWER"); assert.equal(body.envelope.freshness, expected.envelope.freshness);
  }
  const may = await request("layers", "?month=5");
  assert.deepEqual(may.body.data, JSON.parse(await read("./fixtures/governed-earthquakes/layers-may.json")).data);
  for (const query of ["?month=13", "?month=0", "?month=05", "?month=+5", "?month=%205", "?month=", "?other=1", "?month=5&month=6", "?station_id=53974"]) assert.equal((await request("layers", query)).status, 400, query);
  assert.equal((await request("layers", "?month=3")).body.envelope.reason_code, "EVIDENCE_NOT_FOUND");
  const lapsed = await request("layers", "", "2025-11-09T12:45:00Z");
  assert.equal(lapsed.body.envelope.reason_code, "RELEASE_TIME_INVALID"); assert.equal(lapsed.body.data, undefined);
  await admin.withdrawEarthquakePackage(s, { package_id: decision.package_id, expected_active: decision.package_id }, NOW);
  assert.equal((await request("layers")).body.envelope.reason_code, "NO_APPROVED_SNAPSHOT");
});

test("storage failures withhold data without leaking detail", async () => {
  const s = await store();
  await admin.stageEarthquakePackage(s, quakes, "staging-token", NOW);
  await admin.activateEarthquakePackage(s, { package_id: decision.package_id, decision, expected_active: null }, NOW);
  globalThis.__quakeStorage = { env: { BUCKET: { get: async () => { throw new Error("private upstream detail"); } } }, db: s.db };
  const failed = await request("layers");
  assert.equal(failed.status, 503); assert.equal(failed.body.envelope.reason_code, "RELEASE_STORE_UNAVAILABLE");
  assert.doesNotMatch(JSON.stringify(failed.body), /private upstream/);
  globalThis.__quakeStorage = { env: { BUCKET: { get: async () => ({ size: 10, text: async () => storm.slice(0, 10) }) } }, db: s.db };
  assert.equal((await request("layers")).status, 503);
});
