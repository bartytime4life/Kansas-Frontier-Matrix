import { publicFixtureAuthority } from "./public-release-test-authority.mjs";
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
const soilUrl = moduleUrl((await read("../app/governed-soil.ts")).replace('"./governed-water"', JSON.stringify(waterUrl)).replace('"./governed-weather"', JSON.stringify(weatherUrl)));
const waterAdminUrl = moduleUrl((await read("../app/governed-water-admin.ts")).replace('"./governed-water"', JSON.stringify(waterUrl)));
const weatherAdminUrl = moduleUrl((await read("../app/governed-weather-admin.ts")).replace('"./governed-water-admin"', JSON.stringify(waterAdminUrl)).replace('"./governed-weather"', JSON.stringify(weatherUrl)));
const admin = await import(moduleUrl((await read("../app/governed-soil-admin.ts"))
  .replace('"./governed-water-admin"', JSON.stringify(waterAdminUrl)).replace('"./governed-soil"', JSON.stringify(soilUrl))));
const waterAdmin = await import(waterAdminUrl), weatherAdmin = await import(weatherAdminUrl);
const soil = await read("./fixtures/governed-soil/admitted-snapshot.json");
const decision = JSON.parse(await read("./fixtures/governed-soil/owner-decision.json"));
const water = await read("./fixtures/governed-water/admitted-snapshot.json");
const weather = await read("./fixtures/governed-weather/admitted-snapshot.json");
const weatherDecision = JSON.parse(await read("./fixtures/governed-weather/owner-decision.json"));
const NOW = "2026-10-11T13:00:00Z";

// D1 stand-in: all three governed migrations on SQLite, with D1's prepare/bind/first/run/batch surface.
async function store() {
  const sqlite = new DatabaseSync(":memory:");
  for (const name of ["0001_governed_water", "0006_governed_weather", "0007_governed_soil"]) sqlite.exec((await read(`../drizzle/${name}.sql`)).replaceAll("--> statement-breakpoint", ""));
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

test("soil staging uses its own prefix and table, and refuses water and weather packages", async () => {
  const s = await store();
  const staged = await admin.stageSoilPackage(s, soil, "staging-token", NOW);
  assert.deepEqual(staged, { package_id: decision.package_id, state: "STAGED", activated: false });
  assert.deepEqual([...s.objects.keys()], [admin.soilObjectKey(decision.package_id)]);
  assert.ok(admin.soilObjectKey(decision.package_id).startsWith("governed-soil/v1/objects/"));
  assert.equal(count(s, "soil_packages"), 1);
  assert.equal(count(s, "water_packages") + count(s, "weather_packages") + count(s, "soil_active"), 0);
  for (const other of [water, weather]) await rejects(admin.stageSoilPackage(s, other, "staging-token", NOW), "PACKAGE_INVALID");
  await rejects(waterAdmin.stageWaterPackage(s, soil, "staging-token", NOW), "PACKAGE_INVALID");
  await rejects(weatherAdmin.stageWeatherPackage(s, soil, "staging-token", NOW), "PACKAGE_INVALID");
});

test("activation passes the soil gate and leaves water and weather unserved", async () => {
  const s = await store();
  await admin.stageSoilPackage(s, soil, "staging-token", NOW);
  for (const profile of ["kfm.water-release-decision/v1", "kfm.weather-release-decision/v1"]) {
    await rejects(admin.activateSoilPackage(s, { package_id: decision.package_id, decision: { ...decision, profile }, expected_active: null }, NOW), "RELEASE_BINDING_MISMATCH");
  }
  await rejects(admin.activateSoilPackage(s, { package_id: decision.package_id, decision, expected_active: null }, "2026-10-18T12:45:00Z"), "RELEASE_TIME_INVALID");
  const activated = await admin.activateSoilPackage(s, { package_id: decision.package_id, decision, expected_active: null }, NOW);
  assert.equal(activated.outcome, "ACTIVATED");
  assert.match(activated.event_id, /^soil:[a-f0-9]{32}$/);
  assert.equal(count(s, "soil_activation_events"), 1);
  assert.equal(count(s, "water_active") + count(s, "weather_active") + count(s, "water_activation_events") + count(s, "weather_activation_events"), 0);
  assert.deepEqual(await admin.soilAdminStatus(s), { active_package_id: decision.package_id, previous_package_id: null, revision: 1, decision_expires_at: decision.expires_at });
  assert.equal((await weatherAdmin.weatherAdminStatus(s)).active_package_id, null);
  // A weather activation cannot point at a soil package: it was never staged as weather.
  await rejects(weatherAdmin.activateWeatherPackage(s, { package_id: decision.package_id, decision: weatherDecision, expected_active: null }, NOW), "ACTIVATION_BINDING_MISMATCH");
  await rejects(weatherAdmin.activateWeatherPackage(s, { package_id: decision.package_id, decision: { ...weatherDecision, package_id: decision.package_id }, expected_active: null }, NOW), "PACKAGE_NOT_STAGED");
  await rejects(admin.activateSoilPackage(s, { package_id: decision.package_id, decision, expected_active: null }, NOW), "ACTIVATION_CONFLICT");
});

test("withdrawal is compare-and-swap and stops the soil package only", async () => {
  const s = await store();
  await admin.stageSoilPackage(s, soil, "staging-token", NOW);
  await admin.activateSoilPackage(s, { package_id: decision.package_id, decision, expected_active: null }, NOW);
  await rejects(admin.withdrawSoilPackage(s, { package_id: decision.package_id, expected_active: null }, NOW), "WITHDRAW_CONFLICT");
  const withdrawn = await admin.withdrawSoilPackage(s, { package_id: decision.package_id, expected_active: decision.package_id }, NOW);
  assert.equal(withdrawn.outcome, "WITHDRAWN");
  assert.equal(s.sqlite.prepare("SELECT state FROM soil_packages").get().state, "WITHDRAWN");
  assert.equal(s.sqlite.prepare("SELECT action FROM soil_activation_events ORDER BY rowid DESC").get().action, "WITHDRAW");
});

// The read adapter, with its Cloudflare bindings swapped for the stand-in store.
const publicAuthorityUrl = await publicFixtureAuthority([{ family: "soil", raw: soil, decision }], waterUrl);
const server = (await read("../app/governed-soil-server.ts"))
  .replace('import { env } from "cloudflare:workers";', "const env = new Proxy({}, { get: (_, key) => globalThis.__soilStorage.env[key] });")
  .replace('import { getRawDb } from "../db";', "const getRawDb = () => globalThis.__soilStorage.db;")
  .replace('"./public-release-server"', JSON.stringify(publicAuthorityUrl)).replace('"./public-release"', JSON.stringify(publicAuthorityUrl))
  .replace('"./governed-water"', JSON.stringify(waterUrl)).replace('"./governed-soil"', JSON.stringify(soilUrl));
globalThis.__soilStorage = { env: {}, db: null };
const { governedSoilRead } = await import(moduleUrl(server));
const RealDate = Date;
async function request(view, query = "", clock = NOW) {
  class TestDate extends RealDate { constructor(...args) { super(...(args.length ? args : [clock])); } static now() { return RealDate.parse(clock); } }
  globalThis.Date = TestDate;
  try { const response = await governedSoilRead(new Request("https://example.test/api/governed/soil/v1/" + view + query), view); return { status: response.status, body: await response.json() }; }
  finally { globalThis.Date = RealDate; }
}

test("the read route serves only the active, staged soil package within its approval", async () => {
  const s = await store();
  globalThis.__soilStorage = { env: { BUCKET: s.bucket }, db: s.db };
  assert.equal((await request("layers")).body.envelope.reason_code, "NO_APPROVED_SNAPSHOT");
  await admin.stageSoilPackage(s, soil, "staging-token", NOW);
  await admin.activateSoilPackage(s, { package_id: decision.package_id, decision, expected_active: null }, NOW);
  for (const view of ["bootstrap", "layers", "evidence"]) {
    const { status, body } = await request(view);
    // The Worker clock carries milliseconds, so issued_at (and the envelope's spec_hash) differ from the fixture.
    const expected = JSON.parse(await read(`./fixtures/governed-soil/${view}.json`));
    assert.equal(status, 200);
    assert.deepEqual(body.data, expected.data);
    assert.equal(body.envelope.outcome, "ANSWER"); assert.equal(body.envelope.freshness, expected.envelope.freshness);
  }
  const one = await request("evidence", "?station_id=03067");
  assert.deepEqual(one.body.data.entries.map(e => [e.station_id, e.series]), [5, 10, 20, 50, 100].map(d => ["03067", d]));
  for (const query of ["?station_id=USW00013996", "?other=1", "?station_id=53974&station_id=03067", "?depth_cm=5"]) assert.equal((await request("layers", query)).status, 400);
  const lapsed = await request("layers", "", "2026-10-18T12:45:00Z");
  assert.equal(lapsed.body.envelope.reason_code, "RELEASE_TIME_INVALID"); assert.equal(lapsed.body.data, undefined);
  await admin.withdrawSoilPackage(s, { package_id: decision.package_id, expected_active: decision.package_id }, NOW);
  assert.equal((await request("layers")).body.envelope.reason_code, "NO_APPROVED_SNAPSHOT");
});

test("storage failures withhold data without leaking detail", async () => {
  const s = await store();
  await admin.stageSoilPackage(s, soil, "staging-token", NOW);
  await admin.activateSoilPackage(s, { package_id: decision.package_id, decision, expected_active: null }, NOW);
  globalThis.__soilStorage = { env: { BUCKET: { get: async () => { throw new Error("private upstream detail"); } } }, db: s.db };
  const failed = await request("layers");
  assert.equal(failed.status, 503); assert.equal(failed.body.envelope.reason_code, "RELEASE_STORE_UNAVAILABLE");
  assert.doesNotMatch(JSON.stringify(failed.body), /private upstream/);
  globalThis.__soilStorage = { env: { BUCKET: { get: async () => ({ size: 10, text: async () => weather.slice(0, 10) }) } }, db: s.db };
  assert.equal((await request("layers")).status, 503);
});
