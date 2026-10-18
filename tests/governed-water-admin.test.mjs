import { publicFixtureAuthority } from "./public-release-test-authority.mjs";
import test from "node:test";
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { DatabaseSync } from "node:sqlite";
import ts from "typescript";

const compile = (text, fileName) => ts.transpileModule(text, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 }, fileName }).outputText;
const moduleUrl = (text, name) => "data:text/javascript;base64," + Buffer.from(compile(text, name)).toString("base64");
const read = (path) => readFile(new URL(path, import.meta.url), "utf8");
const waterUrl = moduleUrl(await read("../app/governed-water.ts"), "governed-water.ts");
const adminUrl = moduleUrl((await read("../app/governed-water-admin.ts")).replace('"./governed-water"', JSON.stringify(waterUrl)), "governed-water-admin.ts");
const water = await import(waterUrl);
const admin = await import(adminUrl);
const fixture = (name) => read(`./fixtures/governed-water/${name}.json`);
const NOW = "2026-09-30T19:00:00Z";

// D1 stand-in: the Site's real migration on SQLite, with D1's prepare/bind/first/run/batch surface.
async function store() {
  const sqlite = new DatabaseSync(":memory:");
  sqlite.exec((await read("../drizzle/0001_governed_water.sql")).replaceAll("--> statement-breakpoint", ""));
  const statement = (sql, values = []) => ({
    bind: (...next) => statement(sql, next),
    first: async () => sqlite.prepare(sql).get(...values) ?? null,
    run: async () => ({ meta: { changes: Number(sqlite.prepare(sql).run(...values).changes) } }),
    all: async () => ({ results: sqlite.prepare(sql).all(...values) }),
  });
  const objects = new Map();
  return {
    sqlite, objects,
    db: {
      prepare: (sql) => statement(sql),
      batch: async (statements) => {
        sqlite.exec("BEGIN");
        try { const results = []; for (const s of statements) results.push(await s.run()); sqlite.exec("COMMIT"); return results; }
        catch (error) { sqlite.exec("ROLLBACK"); throw error; }
      },
    },
    bucket: {
      get: async (key) => objects.has(key) ? { size: Buffer.byteLength(objects.get(key)), text: async () => objects.get(key) } : null,
      put: async (key, value) => { objects.set(key, value); },
    },
  };
}
const rejects = (promise, reason) => assert.rejects(promise, (error) => error.message === reason);

test("the Site gate allows owner self-release only for the admitted public package", async () => {
  const admitted = await water.parseWaterPackage(await fixture("admitted-snapshot"));
  const owner = JSON.parse(await fixture("owner-decision"));
  assert.equal(owner.reviewer, owner.releaser);
  assert.equal(water.waterGate(admitted, owner, NOW), "ELIGIBLE");
  assert.equal((await water.projectWater(admitted, owner, "layers", NOW)).envelope.outcome, "ANSWER");
  const synthetic = await water.parseWaterPackage(await fixture("snapshot"));
  const decision = JSON.parse(await fixture("decision"));
  assert.equal(water.waterGate(synthetic, { ...decision, reviewer: "synthetic-releaser" }, NOW), "INDEPENDENT_REVIEW_REQUIRED");
  assert.equal(water.waterGate(synthetic, decision, NOW), "ELIGIBLE");
});

test("staging stores a validated package once and never activates it", async () => {
  const s = await store(), text = await fixture("admitted-snapshot");
  const staged = await admin.stageWaterPackage(s, text, "staging-token", NOW);
  assert.equal(staged.state, "STAGED");
  assert.equal(staged.activated, false);
  assert.deepEqual(await admin.stageWaterPackage(s, text, "staging-token", NOW), staged);
  assert.equal(s.sqlite.prepare("SELECT COUNT(*) AS n FROM water_active").get().n, 0);
  await rejects(admin.stageWaterPackage(s, "{}", "staging-token", NOW), "PACKAGE_INVALID");
  s.objects.set(admin.waterObjectKey(staged.package_id), text + " ");
  await rejects(admin.stageWaterPackage(s, text, "staging-token", NOW), "IMMUTABLE_OBJECT_CONFLICT");
});

test("staging and activation both reject changed measurements with resealed outer hashes", async () => {
  const s = await store(), snapshot = JSON.parse(await fixture("admitted-snapshot"));
  const candidate = JSON.parse(snapshot.artifacts["candidate.json"]);
  candidate.observations[0].value = 17.5;
  snapshot.artifacts["candidate.json"] = water.canonical(candidate);
  snapshot.manifest.artifacts["candidate.json"] = await water.digest(snapshot.artifacts["candidate.json"]);
  const manifest = Object.fromEntries(Object.entries(snapshot.manifest).filter(([name]) => name !== "package_id"));
  snapshot.manifest.package_id = await water.digest(water.canonical(manifest));
  const text = JSON.stringify(snapshot), id = snapshot.manifest.package_id;
  await rejects(admin.stageWaterPackage(s, text, "staging-token", NOW), "PACKAGE_INVALID");
  assert.equal(s.objects.size, 0);
  assert.equal(s.sqlite.prepare("SELECT COUNT(*) AS n FROM water_packages").get().n, 0);
  // An object left by an older parser is rechecked before activation, too.
  s.objects.set(admin.waterObjectKey(id), text);
  s.sqlite.prepare("INSERT INTO water_packages (package_id, object_key, staged_at, staged_by, state) VALUES (?, ?, ?, ?, 'STAGED')")
    .run(id, admin.waterObjectKey(id), NOW, "synthetic-legacy-stage");
  const owner = { ...JSON.parse(await fixture("owner-decision")), package_id: id };
  await rejects(admin.activateWaterPackage(s, { package_id: id, decision: owner, expected_active: null }, NOW), "CANDIDATE_DIGEST_MISMATCH");
  assert.equal(s.sqlite.prepare("SELECT COUNT(*) AS n FROM water_active").get().n, 0);
});

test("activation is compare-and-swap, gate-checked and logged", async () => {
  const s = await store(), owner = JSON.parse(await fixture("owner-decision"));
  const id = owner.package_id;
  await rejects(admin.activateWaterPackage(s, { package_id: id, decision: owner, expected_active: null }, NOW), "PACKAGE_NOT_STAGED");
  await admin.stageWaterPackage(s, await fixture("admitted-snapshot"), "staging-token", NOW);
  await rejects(admin.activateWaterPackage(s, { package_id: id, decision: { ...owner, expires_at: "2026-09-30T18:59:00Z" }, expected_active: null }, NOW), "RELEASE_TIME_INVALID");
  await rejects(admin.activateWaterPackage(s, { package_id: id, decision: { ...owner, package_id: "sha256:" + "0".repeat(64) }, expected_active: null }, NOW), "ACTIVATION_BINDING_MISMATCH");
  await rejects(admin.activateWaterPackage(s, "not an object", NOW), "ACTIVATION_REQUEST_INVALID");
  const active = await admin.activateWaterPackage(s, { package_id: id, decision: owner, expected_active: null }, NOW);
  assert.deepEqual([active.outcome, active.revision, active.previous_package_id], ["ACTIVATED", 1, null]);
  await rejects(admin.activateWaterPackage(s, { package_id: id, decision: owner, expected_active: null }, NOW), "ACTIVATION_CONFLICT");
  assert.deepEqual(await admin.waterAdminStatus(s), { active_package_id: id, previous_package_id: null, revision: 1, decision_expires_at: owner.expires_at });
  assert.equal(s.sqlite.prepare("SELECT COUNT(*) AS n FROM water_activation_events WHERE action = 'ACTIVATE'").get().n, 1);

  // A second package must have been prepared against the current active package.
  const synthetic = await fixture("snapshot"), decision = JSON.parse(await fixture("decision"));
  await admin.stageWaterPackage(s, synthetic, "staging-token", NOW);
  await rejects(admin.activateWaterPackage(s, { package_id: decision.package_id, decision, expected_active: id }, NOW), "ROLLBACK_BINDING_MISMATCH");
  assert.equal((await admin.waterAdminStatus(s)).revision, 1);
});

test("withdrawal stops the active package and is logged once", async () => {
  const s = await store(), owner = JSON.parse(await fixture("owner-decision"));
  await admin.stageWaterPackage(s, await fixture("admitted-snapshot"), "staging-token", NOW);
  await admin.activateWaterPackage(s, { package_id: owner.package_id, decision: owner, expected_active: null }, NOW);
  assert.equal((await admin.withdrawWaterPackage(s, { package_id: owner.package_id, expected_active: owner.package_id }, NOW)).outcome, "WITHDRAWN");
  assert.equal(s.sqlite.prepare("SELECT state FROM water_packages").get().state, "WITHDRAWN");
  await rejects(admin.withdrawWaterPackage(s, { package_id: owner.package_id, expected_active: owner.package_id }, NOW), "PACKAGE_NOT_STAGED");
  assert.equal(s.sqlite.prepare("SELECT COUNT(*) AS n FROM water_activation_events WHERE action = 'WITHDRAW'").get().n, 1);
  await rejects(admin.activateWaterPackage(s, { package_id: owner.package_id, decision: owner, expected_active: owner.package_id }, NOW), "PACKAGE_NOT_STAGED");
});

// Routes run against the real admin module with the auth/storage boundary stubbed.
const publicAuthorityUrl = await publicFixtureAuthority([{ family: "water", raw: await fixture("admitted-snapshot"), decision: JSON.parse(await fixture("owner-decision")) }], waterUrl);
const serverStub = moduleUrl(`
  import { WaterAdminError } from ${JSON.stringify(adminUrl)};
  export const waterAdminHeaders = { "Cache-Control": "private, no-store" };
  export const waterAdminStore = () => globalThis.__waterAdmin.store;
  export const waterSameOrigin = (request) => { if (request.headers.get("origin") !== new URL(request.url).origin) throw new WaterAdminError("SAME_ORIGIN_REQUIRED", 403); };
  export const waterOwner = async () => { if (!globalThis.__waterAdmin.owner) throw new WaterAdminError("OWNER_REQUIRED", 403); return { id: "owner-1", email: "owner@example.test" }; };
  export const waterWorker = (request) => { if (request.headers.get("authorization") !== "Bearer staging-secret") throw new WaterAdminError("STAGING_TOKEN_REQUIRED", 403); };
  export const readBoundedText = async (request) => request.text();
  export const waterAdminFailure = (error) => Response.json({ outcome: "ERROR", reason_code: error instanceof WaterAdminError ? error.message : "WATER_ADMIN_UNAVAILABLE" }, { status: error.status ?? 503 });
`, "governed-water-admin-server.ts");
const route = async (name) => import(moduleUrl((await read(`../app/api/governed/water-admin/${name}/route.ts`))
  .replaceAll('"../../../../public-release-server"', JSON.stringify(publicAuthorityUrl))
  .replaceAll('"../../../../governed-water-admin-server"', JSON.stringify(serverStub))
  .replaceAll('"../../../../governed-water-admin"', JSON.stringify(adminUrl))
  .replaceAll('"../../../../governed-water"', JSON.stringify(waterUrl)), name));

test("routes require the staging token, the owner and the Site origin", async () => {
  const s = await store();
  globalThis.__waterAdmin = { store: s, owner: false };
  const stage = await route("stage"), activate = await route("activate");
  const text = await fixture("admitted-snapshot"), owner = JSON.parse(await fixture("owner-decision"));
  const post = (path, body, headers) => new Request("https://site.test/api/governed/water-admin/" + path, { method: "POST", headers: { "Content-Type": "application/json", ...headers }, body });

  assert.equal((await stage.POST(post("stage", text, {}))).status, 403);
  assert.equal((await stage.POST(post("stage", text, { Authorization: "Bearer staging-secret" }))).status, 200);
  const body = JSON.stringify({ package_id: owner.package_id, expected_active: null });
  assert.equal((await activate.POST(post("activate", body, { Origin: "https://elsewhere.test" }))).status, 403);
  assert.equal((await activate.POST(post("activate", body, { Origin: "https://site.test" }))).status, 403);
  globalThis.__waterAdmin.owner = true;
  const posted = JSON.stringify({ package_id: owner.package_id, expected_active: null, decision: owner });
  assert.equal((await activate.POST(post("activate", posted, { Origin: "https://site.test" }))).status, 400);
  const response = await activate.POST(post("activate", body, { Origin: "https://site.test" }));
  // The route stamps the real clock; the fixture decision expired on 2026-10-01, so the gate refuses it.
  assert.deepEqual([response.status, (await response.json()).reason_code], [409, "RELEASE_TIME_INVALID"]);
});

test("status answers the owner or the staging token, and nobody else", async () => {
  const s = await store(), owner = JSON.parse(await fixture("owner-decision"));
  await admin.stageWaterPackage(s, await fixture("admitted-snapshot"), "staging-token", NOW);
  await admin.activateWaterPackage(s, { package_id: owner.package_id, decision: owner, expected_active: null }, NOW);
  const status = await route("status");
  const get = (headers) => status.GET(new Request("https://site.test/api/governed/water-admin/status", { headers }));
  globalThis.__waterAdmin = { store: s, owner: false };
  assert.equal((await get({})).status, 403);
  // A wrong token is refused even if the caller also holds an owner session.
  globalThis.__waterAdmin.owner = true;
  assert.equal((await get({ Authorization: "Bearer wrong" })).status, 403);
  globalThis.__waterAdmin.owner = false;
  const byToken = await get({ Authorization: "Bearer staging-secret" });
  assert.deepEqual([byToken.status, await byToken.json()], [200, { active_package_id: owner.package_id, previous_package_id: null, revision: 1, decision_expires_at: owner.expires_at, authorized_packages: [], release_hold: "PUBLIC_RELEASE_EXPIRED" }]);
  globalThis.__waterAdmin.owner = true;
  assert.equal((await (await get({})).json()).active_package_id, owner.package_id);
});

test("status reports no expiry when nothing is active or the stored decision is unreadable", async () => {
  const s = await store(), owner = JSON.parse(await fixture("owner-decision"));
  assert.deepEqual(await admin.waterAdminStatus(s), { active_package_id: null, previous_package_id: null, revision: 0, decision_expires_at: null });
  await admin.stageWaterPackage(s, await fixture("admitted-snapshot"), "staging-token", NOW);
  await admin.activateWaterPackage(s, { package_id: owner.package_id, decision: owner, expected_active: null }, NOW);
  s.sqlite.prepare("UPDATE water_active SET decision_json = 'not json' WHERE singleton = 1").run();
  assert.equal((await admin.waterAdminStatus(s)).decision_expires_at, null);
});

test("a losing concurrent activation logs no event", async () => {
  const s = await store(), owner = JSON.parse(await fixture("owner-decision"));
  await admin.stageWaterPackage(s, await fixture("admitted-snapshot"), "staging-token", NOW);
  const request = { package_id: owner.package_id, decision: owner, expected_active: null };
  // Hold both writes until both requests have read the same (empty) pointer.
  const batch = s.db.batch, waiting = [];
  s.db.batch = (statements) => new Promise((resolve, reject) => {
    waiting.push(() => batch(statements).then(resolve, reject));
    if (waiting.length === 2) void waiting.reduce((done, run) => done.then(run), Promise.resolve());
  });
  const results = await Promise.allSettled([admin.activateWaterPackage(s, request, NOW), admin.activateWaterPackage(s, request, NOW)]);
  assert.deepEqual(results.map((r) => r.status).sort(), ["fulfilled", "rejected"]);
  assert.equal(results.find((r) => r.status === "rejected").reason.message, "ACTIVATION_CONFLICT");
  assert.equal(s.sqlite.prepare("SELECT COUNT(*) AS n FROM water_activation_events").get().n, 1);
});

test("withdrawal refuses when the active package changed since the page loaded", async () => {
  const s = await store(), owner = JSON.parse(await fixture("owner-decision"));
  await admin.stageWaterPackage(s, await fixture("admitted-snapshot"), "staging-token", NOW);
  await admin.stageWaterPackage(s, await fixture("snapshot"), "staging-token", NOW);
  const synthetic = JSON.parse(await fixture("decision"));
  // The page loaded with nothing active; the admitted package was activated afterwards.
  await admin.activateWaterPackage(s, { package_id: owner.package_id, decision: owner, expected_active: null }, NOW);
  await rejects(admin.withdrawWaterPackage(s, { package_id: synthetic.package_id, expected_active: null }, NOW), "WITHDRAW_CONFLICT");
  await rejects(admin.withdrawWaterPackage(s, { package_id: owner.package_id }, NOW), "WITHDRAW_REQUEST_INVALID");
  assert.equal(s.sqlite.prepare("SELECT COUNT(*) AS n FROM water_packages WHERE state = 'WITHDRAWN'").get().n, 0);
  assert.equal((await admin.withdrawWaterPackage(s, { package_id: owner.package_id, expected_active: owner.package_id }, NOW)).outcome, "WITHDRAWN");
});
