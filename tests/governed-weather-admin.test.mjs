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
const waterAdminUrl = moduleUrl((await read("../app/governed-water-admin.ts")).replace('"./governed-water"', JSON.stringify(waterUrl)));
const admin = await import(moduleUrl((await read("../app/governed-weather-admin.ts"))
  .replace('"./governed-water-admin"', JSON.stringify(waterAdminUrl)).replace('"./governed-weather"', JSON.stringify(weatherUrl))));
const waterAdmin = await import(waterAdminUrl);
const weather = await read("./fixtures/governed-weather/admitted-snapshot.json");
const decision = JSON.parse(await read("./fixtures/governed-weather/owner-decision.json"));
const water = await read("./fixtures/governed-water/admitted-snapshot.json");
const NOW = "2026-10-11T13:00:00Z";

// D1 stand-in: both governed migrations on SQLite, with D1's prepare/bind/first/run/batch surface.
async function store() {
  const sqlite = new DatabaseSync(":memory:");
  for (const name of ["0001_governed_water", "0006_governed_weather"]) sqlite.exec((await read(`../drizzle/${name}.sql`)).replaceAll("--> statement-breakpoint", ""));
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

test("weather staging uses its own prefix and table, and refuses water packages", async () => {
  const s = await store();
  const staged = await admin.stageWeatherPackage(s, weather, "staging-token", NOW);
  assert.deepEqual(staged, { package_id: decision.package_id, state: "STAGED", activated: false });
  assert.deepEqual([...s.objects.keys()], [admin.weatherObjectKey(decision.package_id)]);
  assert.ok(admin.weatherObjectKey(decision.package_id).startsWith("governed-weather/v1/objects/"));
  assert.equal(count(s, "weather_packages"), 1);
  assert.equal(count(s, "water_packages"), 0);
  assert.equal(count(s, "weather_active"), 0);
  await rejects(admin.stageWeatherPackage(s, water, "staging-token", NOW), "PACKAGE_INVALID");
  await rejects(waterAdmin.stageWaterPackage(s, weather, "staging-token", NOW), "PACKAGE_INVALID");
});

test("activation passes the weather gate and leaves water unserved", async () => {
  const s = await store();
  await admin.stageWeatherPackage(s, weather, "staging-token", NOW);
  await rejects(admin.activateWeatherPackage(s, { package_id: decision.package_id, decision: { ...decision, profile: "kfm.water-release-decision/v1" }, expected_active: null }, NOW), "RELEASE_BINDING_MISMATCH");
  await rejects(admin.activateWeatherPackage(s, { package_id: decision.package_id, decision, expected_active: null }, "2026-10-18T12:45:00Z"), "RELEASE_TIME_INVALID");
  const activated = await admin.activateWeatherPackage(s, { package_id: decision.package_id, decision, expected_active: null }, NOW);
  assert.equal(activated.outcome, "ACTIVATED");
  assert.match(activated.event_id, /^weather:[a-f0-9]{32}$/);
  assert.equal(count(s, "weather_activation_events"), 1);
  assert.equal(count(s, "water_active") + count(s, "water_activation_events"), 0);
  assert.deepEqual(await admin.weatherAdminStatus(s), { active_package_id: decision.package_id, previous_package_id: null, revision: 1, decision_expires_at: decision.expires_at });
  assert.equal((await waterAdmin.waterAdminStatus(s)).active_package_id, null);
  // A water activation cannot point at a weather package: it was never staged as water.
  await rejects(waterAdmin.activateWaterPackage(s, { package_id: decision.package_id, decision, expected_active: null }, NOW), "PACKAGE_NOT_STAGED");
  await rejects(admin.activateWeatherPackage(s, { package_id: decision.package_id, decision, expected_active: null }, NOW), "ACTIVATION_CONFLICT");
});

test("withdrawal is compare-and-swap and stops the weather package only", async () => {
  const s = await store();
  await admin.stageWeatherPackage(s, weather, "staging-token", NOW);
  await admin.activateWeatherPackage(s, { package_id: decision.package_id, decision, expected_active: null }, NOW);
  await rejects(admin.withdrawWeatherPackage(s, { package_id: decision.package_id, expected_active: null }, NOW), "WITHDRAW_CONFLICT");
  const withdrawn = await admin.withdrawWeatherPackage(s, { package_id: decision.package_id, expected_active: decision.package_id }, NOW);
  assert.equal(withdrawn.outcome, "WITHDRAWN");
  assert.equal(s.sqlite.prepare("SELECT state FROM weather_packages").get().state, "WITHDRAWN");
  assert.equal(s.sqlite.prepare("SELECT action FROM weather_activation_events ORDER BY rowid DESC").get().action, "WITHDRAW");
});

// The read adapter, with its Cloudflare bindings swapped for the stand-in store.
const publicAuthorityUrl = await publicFixtureAuthority([{ family: "weather", raw: weather, decision }], waterUrl);
const server = (await read("../app/governed-weather-server.ts"))
  .replace('import { env } from "cloudflare:workers";', "const env = new Proxy({}, { get: (_, key) => globalThis.__weatherStorage.env[key] });")
  .replace('import { getRawDb } from "../db";', "const getRawDb = () => globalThis.__weatherStorage.db;")
  .replace('"./public-release-server"', JSON.stringify(publicAuthorityUrl)).replace('"./public-release"', JSON.stringify(publicAuthorityUrl))
  .replace('"./governed-water"', JSON.stringify(waterUrl)).replace('"./governed-weather"', JSON.stringify(weatherUrl));
globalThis.__weatherStorage = { env: {}, db: null };
const { governedWeatherRead } = await import(moduleUrl(server));
const RealDate = Date;
async function request(view, query = "", clock = NOW) {
  class TestDate extends RealDate { constructor(...args) { super(...(args.length ? args : [clock])); } static now() { return RealDate.parse(clock); } }
  globalThis.Date = TestDate;
  try { const response = await governedWeatherRead(new Request("https://example.test/api/governed/weather/v1/" + view + query), view); return { status: response.status, body: await response.json() }; }
  finally { globalThis.Date = RealDate; }
}

test("the read route serves only the active, staged weather package within its approval", async () => {
  const s = await store();
  globalThis.__weatherStorage = { env: { BUCKET: s.bucket }, db: s.db };
  assert.equal((await request("layers")).body.envelope.reason_code, "NO_APPROVED_SNAPSHOT");
  await admin.stageWeatherPackage(s, weather, "staging-token", NOW);
  await admin.activateWeatherPackage(s, { package_id: decision.package_id, decision, expected_active: null }, NOW);
  for (const view of ["bootstrap", "layers", "evidence"]) {
    const { status, body } = await request(view);
    // The Worker clock carries milliseconds, so issued_at (and the envelope's spec_hash) differ from the fixture.
    const expected = JSON.parse(await read(`./fixtures/governed-weather/${view}.json`));
    assert.equal(status, 200);
    assert.deepEqual(body.data, expected.data);
    assert.equal(body.envelope.outcome, "ANSWER"); assert.equal(body.envelope.freshness, expected.envelope.freshness);
  }
  const one = await request("evidence", "?station_id=USW00013996");
  assert.deepEqual(one.body.data.entries.map(e => e.station_id), ["USW00013996"]);
  for (const query of ["?station_id=USGS-06892518", "?other=1", "?station_id=USW00013996&station_id=USW00003928"]) assert.equal((await request("layers", query)).status, 400);
  const lapsed = await request("layers", "", "2026-10-18T12:45:00Z");
  assert.equal(lapsed.body.envelope.reason_code, "RELEASE_TIME_INVALID"); assert.equal(lapsed.body.data, undefined);
  await admin.withdrawWeatherPackage(s, { package_id: decision.package_id, expected_active: decision.package_id }, NOW);
  assert.equal((await request("layers")).body.envelope.reason_code, "NO_APPROVED_SNAPSHOT");
});

test("storage failures withhold data without leaking detail", async () => {
  const s = await store();
  await admin.stageWeatherPackage(s, weather, "staging-token", NOW);
  await admin.activateWeatherPackage(s, { package_id: decision.package_id, decision, expected_active: null }, NOW);
  globalThis.__weatherStorage = { env: { BUCKET: { get: async () => { throw new Error("private upstream detail"); } } }, db: s.db };
  const failed = await request("layers");
  assert.equal(failed.status, 503); assert.equal(failed.body.envelope.reason_code, "RELEASE_STORE_UNAVAILABLE");
  assert.doesNotMatch(JSON.stringify(failed.body), /private upstream/);
  globalThis.__weatherStorage = { env: { BUCKET: { get: async () => ({ size: 10, text: async () => water.slice(0, 10) }) } }, db: s.db };
  assert.equal((await request("layers")).status, 503);
});
