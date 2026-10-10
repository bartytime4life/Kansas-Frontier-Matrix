import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { createHash } from "node:crypto";
import test from "node:test";
import ts from "typescript";

async function compile(path, imports = {}) {
  const source = await readFile(new URL(`../app/${path}.ts`, import.meta.url), "utf8");
  const code = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 } }).outputText;
  const compiled = { exports: {} };
  new Function("require", "module", "exports", code)(id => imports[id], compiled, compiled.exports);
  return compiled.exports;
}
const schema = await compile("acquisition-inventory");
const client = await compile("acquisition-client", { "./acquisition-inventory": schema });
const bounded = await compile("bounded-json");
const terrainData = await compile("terrain-provenance-data");
const terrain = await compile("acquisition-terrain", { "./terrain-provenance-data": terrainData });
const inventory = () => ({ schema_version: "kfm-acquisition-inventory-v1", lifecycle: "candidate-only", generated_at: "2026-10-06T12:00:00Z", cache: { limit_bytes: 500_000_000_000, used_bytes: 6, temporary_bytes: 2, replaceable_bytes: 3 }, jobs: [] });
const job = () => ({ job_id: "test-file", source_id: "usgs", dataset_id: "terrain", label: "Selected terrain", state: "complete", reason: null, expected_bytes: null, approved_max_bytes: 100, downloaded_bytes: 40, sha256: "a".repeat(64), checksum_verified: true, temporal_start: "2010", temporal_end: "2010-12", storage: "local-replaceable-cache", source_url: "https://www.usgs.gov/3d-elevation-program", updated_at: "2026-10-06T12:00:00Z", scope: "kansas", estimate_basis: "unknown", rights_url: null, protected: true });
const discovery = () => ({ schema_version: "kfm-3dep-discovery-v1", selection: "KS_ provider prefix", captured_at: "2026-10-06T16:39:43Z", complete_for_prefix: true, complete_for_state: false, project_count: 1, metadata_bytes_captured: 2300, projects: [{ provider_work_unit: "KS_Example_2019", source_url: "https://usgs-lidar-public.s3.amazonaws.com/KS_Example_2019/ept.json", metadata_sha256: "1".repeat(64), metadata_bytes: 2300, point_count: 1000, bounds: [-100, 38, 100, -99, 39, 900], srs: { authority: "EPSG", horizontal: "4326" }, temporal_start: null, temporal_end: null }] });
const hash = bytes => createHash("sha256").update(Buffer.from(bytes)).digest("hex");
const encode = object => new TextEncoder().encode(JSON.stringify(object)).buffer;

test("calendar normalization cannot turn impossible dates into valid receipt chronology", () => {
  assert.ok(schema.parseAcquisitionInventory(inventory()));
  for (const generated_at of ["2026-02-31T12:00:00Z", "2026-04-31T12:00:00Z", "2026-01-01T24:00:00Z", "2026-01-01T12:00:00", "2025-02-29T12:00:00Z"]) assert.equal(schema.parseAcquisitionInventory({ ...inventory(), generated_at }), null, generated_at);
  for (const generated_at of ["2024-02-29T12:00:00Z", "2026-10-06T07:00:00.123456-05:00"]) assert.ok(schema.parseAcquisitionInventory({ ...inventory(), generated_at }), generated_at);
});

test("500 GB is the default while configurable and historical receipt budgets are preserved", () => {
  assert.equal(schema.ACQUISITION_CACHE_LIMIT, 500_000_000_000);
  for (const limit_bytes of [100_000_000_000, 500_000_000_000, 2_000_000_000_000]) {
    const value = inventory(); value.cache.limit_bytes = limit_bytes;
    assert.equal(schema.parseAcquisitionInventory(value).cache.limit_bytes, limit_bytes);
  }
  for (const limit_bytes of [0, -1, Number.MAX_SAFE_INTEGER + 1, 500_000_000_000.5, "500000000000", null]) {
    const value = inventory(); value.cache.limit_bytes = limit_bytes;
    assert.equal(schema.parseAcquisitionInventory(value), null, String(limit_bytes));
  }
  const value = { ...inventory(), jobs: [{ ...job(), approved_max_bytes: 200_000_000_000 }] };
  assert.ok(schema.parseAcquisitionInventory(value), "current receipts can select a bound above the old ceiling");
  value.cache.limit_bytes = 100_000_000_000;
  assert.equal(schema.parseAcquisitionInventory(value), null, "new policy cannot retroactively expand a historical receipt's file bound");
  value.cache.budget_scope = "new-cache-transfers";
  assert.equal(schema.parseAcquisitionInventory(value).jobs[0].approved_max_bytes, 200_000_000_000, "a new inventory can retain older selections after the owner lowers the active budget");
  value.jobs[0].approved_max_bytes = 100_000_000_000;
  assert.ok(schema.parseAcquisitionInventory(value));
});

test("temporary and reproducible cache are disjoint parts of total reported use; real over-budget use remains visible", () => {
  const value = inventory(); value.cache.used_bytes = 1;
  assert.equal(schema.parseAcquisitionInventory(value), null);
  value.cache.used_bytes = 4; assert.equal(schema.parseAcquisitionInventory(value), null);
  value.cache.used_bytes = 500_000_000_001; assert.ok(schema.parseAcquisitionInventory(value));
});

test("worker nullable fields and a checksum-verified unknown-size capture preserve their actual meanings", () => {
  const value = { ...inventory(), jobs: [job()] }, parsed = schema.parseAcquisitionInventory(value);
  assert.ok(parsed); assert.equal(parsed.jobs[0].reason, ""); assert.equal(parsed.jobs[0].rights_url, undefined);
  assert.equal(parsed.jobs[0].expected_bytes, null); assert.equal(parsed.jobs[0].approved_max_bytes, 100);
  assert.equal(parsed.jobs[0].downloaded_bytes, 40); assert.equal(parsed.jobs[0].protected, true);
  for (const mutation of [{ approved_max_bytes: undefined }, { approved_max_bytes: null }, { approved_max_bytes: 0 }, { approved_max_bytes: 500_000_000_001 }, { approved_max_bytes: 39 }, { approved_max_bytes: "100" }, { expected_bytes: 39 }, { expected_bytes: 100, approved_max_bytes: 40 }, { downloaded_bytes: 0 }, { checksum_verified: false }, { sha256: null }, { storage: "provider-remote" }, { protected: "false" }]) assert.equal(schema.parseAcquisitionInventory({ ...value, jobs: [{ ...job(), ...mutation }] }), null, JSON.stringify(mutation));
  const exact = { ...job(), expected_bytes: 40, approved_max_bytes: null, estimate_basis: "provider" };
  assert.ok(schema.parseAcquisitionInventory({ ...value, jobs: [exact] }));
});

test("offline zero counts stay explicitly uninspected rather than measured empty", () => {
  for (const inspected of [false, true, undefined]) {
    const value = inventory(); value.cache = { ...value.cache, used_bytes: 0, temporary_bytes: 0, replaceable_bytes: 0, inspected };
    const parsed = schema.parseAcquisitionInventory(value); assert.ok(parsed); assert.equal(parsed.cache.inspected, inspected);
  }
  const value = inventory(); value.cache.inspected = "false"; assert.equal(schema.parseAcquisitionInventory(value), null);
});

test("a new local selection retires initial load, earlier file reads, saves, and unmounted requests", async () => {
  const session = client.createAcquisitionSession(), first = session.begin();
  let resolveFile, view = "empty";
  const oldFile = session.begin();
  const pending = new Promise(resolve => { resolveFile = resolve; }).then(value => { if (oldFile.current()) view = value; });
  assert.equal(first.signal.aborted, true); assert.equal(first.current(), false);
  const newFile = session.begin(); if (newFile.current()) view = "new local preview";
  resolveFile("old local preview"); await pending;
  assert.equal(view, "new local preview"); assert.equal(oldFile.signal.aborted, true);
  const save = session.begin(); assert.equal(newFile.current(), false);
  session.cancel(); assert.equal(save.signal.aborted, true); assert.equal(save.current(), false);
});

test("local inventory and terrain reads reject oversized metadata before reading and retire stale file bytes", async () => {
  const session = client.createAcquisitionSession(); let reads = 0;
  const oversized = { size: schema.ACQUISITION_MAX_BYTES + 1, text: async () => { reads++; return "{}"; } };
  await assert.rejects(client.readAcquisitionLocalJson(oversized, session.begin().signal), /1 MiB/); assert.equal(reads, 0);
  let complete; const old = session.begin();
  const first = client.readAcquisitionLocalJson({ size: 2, text: () => new Promise(resolve => { complete = resolve; }) }, old.signal);
  const current = session.begin();
  assert.deepEqual(await client.readAcquisitionLocalJson({ size: 15, text: async () => '{"newest":true}' }, current.signal), { newest: true });
  complete("{}"); await assert.rejects(first, { name: "AbortError" });
  await assert.rejects(client.readAcquisitionLocalJson({ size: 1, text: async () => "{" }, current.signal), SyntaxError);
});

test("empty receipt is distinct from malformed GET and save must return the exact submitted digest", async () => {
  assert.equal(client.acquisitionRead({ inventory: null }), null);
  for (const body of [{}, null, { inventory: {} }, { inventory: [] }]) assert.throws(() => client.acquisitionRead(body));
  const value = inventory();
  await client.verifyAcquisitionSave({ saved: true, inventory: value, sha256: hash(encode(value)) }, value);
  await assert.rejects(client.verifyAcquisitionSave({ saved: true, inventory: value, sha256: "b".repeat(64) }, value), /digest/);
  const changed = { ...value, generated_at: "2026-10-05T12:00:00Z" };
  await assert.rejects(client.verifyAcquisitionSave({ saved: true, inventory: changed, sha256: hash(encode(changed)) }, value), /identity/);
  await assert.rejects(client.verifyAcquisitionSave({ inventory: value }, value), /not confirmed/);
});

async function harness() {
  const objects = new Map(); let owner = true, breakReceiptReadback = false, beforeGet = async () => {};
  class ContextError extends Error { constructor(message, status) { super(message); this.status = status; } }
  const bucket = {
    async get(key) { await beforeGet(key); const bytes = objects.get(key); return bytes ? { size: bytes.byteLength, arrayBuffer: async () => breakReceiptReadback && key.includes("/receipts/") ? encode({ corrupt: true }) : bytes.slice(0) } : null; },
    async put(key, bytes) { objects.set(key, bytes.slice(0)); },
    async list() { throw new Error("Receipt history must not be enumerated to read latest."); },
  };
  const server = await compile("acquisition-receipt-server", {
    "./acquisition-inventory": schema, "./bounded-json": bounded,
    "./earth-engine-context-server": {
      earthEngineBucket: () => bucket, earthEngineDigest: async bytes => hash(bytes),
      earthEngineOwner: async () => { if (!owner) throw new ContextError("Sign in", 401); },
      earthEnginePrivateHeaders: { "Cache-Control": "private, no-store" }, EarthEngineContextError: ContextError,
      earthEngineFailure: error => Response.json({ error: "Unavailable" }, { status: error.status ?? 503 }),
    },
  });
  const routes = await compile("api/acquisition/route", { "../../acquisition-inventory": schema, "../../acquisition-receipt-server": server });
  const terrainRoutes = await compile("api/acquisition/terrain/route", { "../../../acquisition-terrain": terrain, "../../../acquisition-receipt-server": server });
  return { objects, routes, terrainRoutes, owner: value => { owner = value; }, breakReadback: () => { breakReceiptReadback = true; }, beforeGet: callback => { beforeGet = callback; } };
}
const request = (value = inventory(), overrides = {}) => new Request("https://kfm.example/api/acquisition", { method: "POST", headers: { origin: "https://kfm.example", "content-type": "application/json" }, body: JSON.stringify(value), ...overrides });

test("receipt route keeps owner and origin gates and rejects malformed or aborted imports without writes", async () => {
  const h = await harness(); h.owner(false);
  assert.equal((await h.routes.GET()).status, 401); assert.equal((await h.routes.POST(request())).status, 401);
  h.owner(true);
  assert.equal((await h.routes.POST(request(undefined, { headers: { origin: "https://other.example", "content-type": "application/json" } }))).status, 403);
  assert.equal((await h.routes.POST(request(undefined, { headers: { origin: "https://kfm.example", "content-type": "text/plain" } }))).status, 415);
  assert.equal((await h.routes.POST(request({}))).status, 400);
  const canceled = new AbortController(); canceled.abort();
  assert.equal((await h.routes.POST(request(undefined, { signal: canceled.signal }))).status, 400);
  assert.equal(h.objects.size, 0);
});

test("latest pointer preserves archive and works beyond 1000 receipts without a listing", async () => {
  const h = await harness();
  for (let i = 0; i < 1001; i++) h.objects.set(`acquisition/v1/receipts/old-${i}.json`, encode({ historical: i }));
  assert.deepEqual(await (await h.routes.GET()).json(), { inventory: null });
  const saved = await h.routes.POST(request()); assert.equal(saved.status, 201);
  const payload = await saved.json(); await client.verifyAcquisitionSave(payload, inventory());
  const pointer = JSON.parse(new TextDecoder().decode(h.objects.get("acquisition/v1/latest.json")));
  assert.equal(pointer.schema, "kfm-acquisition-pointer-v1"); assert.equal(pointer.sha256, payload.sha256);
  const loaded = await h.routes.GET(); assert.equal(loaded.status, 200); assert.deepEqual((await loaded.json()).inventory, inventory());
  assert.equal(h.objects.size, 1003);
});

test("an existing 100 GB saved receipt remains readable without rewriting bytes or its recorded budget", async () => {
  const h = await harness(), value = inventory(); value.cache.limit_bytes = 100_000_000_000;
  const raw = encode(value), digest = hash(raw), key = `acquisition/v1/receipts/1700000000000-${digest}.json`;
  h.objects.set(key, raw); h.objects.set("acquisition/v1/latest.json", encode({ schema: "kfm-acquisition-pointer-v1", key, sha256: digest }));
  const response = await h.routes.GET(); assert.equal(response.status, 200);
  const parsed = (await response.json()).inventory; assert.equal(parsed.cache.limit_bytes, 100_000_000_000);
  assert.deepEqual(h.objects.get(key), raw); assert.equal(hash(h.objects.get(key)), digest);
  const resaved = await h.routes.POST(request(parsed)); assert.equal(resaved.status, 201);
  const receipt = await resaved.json(); assert.equal(receipt.inventory.cache.limit_bytes, 100_000_000_000); assert.equal(receipt.sha256, digest);
  await client.verifyAcquisitionSave(receipt, parsed);
});

test("last completed import wins only after its own receipt readback; prior immutable imports remain", async () => {
  const h = await harness(); let release, entered;
  const held = new Promise(resolve => { release = resolve; }), started = new Promise(resolve => { entered = resolve; });
  let firstKey;
  h.beforeGet(async key => { if (key.includes("/receipts/") && !firstKey) { firstKey = key; entered(); await held; } });
  const first = h.routes.POST(request()); await started;
  const secondValue = { ...inventory(), generated_at: "2026-10-06T13:00:00Z", jobs: [job()] };
  assert.equal((await h.routes.POST(request(secondValue))).status, 201);
  assert.equal((await (await h.routes.GET()).json()).inventory.generated_at, secondValue.generated_at);
  release(); assert.equal((await first).status, 201);
  assert.equal((await (await h.routes.GET()).json()).inventory.generated_at, inventory().generated_at);
  assert.equal(h.objects.size, 3);
});

test("corrupt pointer, digest mismatch, and failed readback never silently become no receipt", async () => {
  const h = await harness(); await h.routes.POST(request());
  const key = "acquisition/v1/latest.json", pointer = JSON.parse(new TextDecoder().decode(h.objects.get(key)));
  h.objects.set(key, encode({ ...pointer, key: "../private" })); assert.equal((await h.routes.GET()).status, 503);
  h.objects.set(key, new ArrayBuffer(1001)); assert.equal((await h.routes.GET()).status, 503);
  h.objects.set(key, encode(pointer)); h.objects.set(pointer.key, encode({ bad: true })); assert.equal((await h.routes.GET()).status, 503);
  const failed = await harness(); failed.breakReadback();
  assert.equal((await failed.routes.POST(request())).status, 503);
  assert.equal(failed.objects.has(key), false, "Unverified receipts cannot become the latest pointer");
});

test("terrain persistence projects metadata and rejects ambiguous work-unit identities", async () => {
  const value = discovery(), projected = terrain.parseAcquisitionTerrain({ ...value, private_extra: "not retained" });
  assert.ok(projected); assert.equal(projected.private_extra, undefined); assert.equal(projected.complete_for_state, false);
  assert.deepEqual(terrain.parseAcquisitionTerrain(projected), projected, "canonical projection remains stable when saved and read");
  for (const bad of [{ ...value, project_count: 2 }, { ...value, projects: [...value.projects, ...value.projects], project_count: 2 }, { ...value, projects: [{ ...value.projects[0], source_url: "https://other.example/ept.json" }] }]) assert.equal(terrain.parseAcquisitionTerrain(bad), null);
  assert.equal(terrain.acquisitionTerrainRead({ discovery: null }), null);
  for (const bad of [{}, { discovery: {} }, { discovery: [] }]) assert.throws(() => terrain.acquisitionTerrainRead(bad));
  await terrain.verifyAcquisitionTerrainSave({ saved: true, discovery: projected, sha256: hash(encode(projected)) }, projected);
  await assert.rejects(terrain.verifyAcquisitionTerrainSave({ saved: true, discovery: projected, sha256: "b".repeat(64) }, projected), /digest/);
});

test("terrain requires owner and same-origin writes, has an independent pointer, and verifies saved hashes", async () => {
  const h = await harness(); h.owner(false);
  assert.equal((await h.terrainRoutes.GET()).status, 401); assert.equal((await h.terrainRoutes.POST(request(discovery()))).status, 401);
  h.owner(true);
  assert.equal((await h.terrainRoutes.POST(request(discovery(), { headers: { origin: "https://other.example", "content-type": "application/json" } }))).status, 403);
  assert.equal((await h.terrainRoutes.POST(request(inventory()))).status, 400);
  assert.deepEqual(await (await h.terrainRoutes.GET()).json(), { discovery: null });
  assert.equal((await h.routes.POST(request())).status, 201);
  const saved = await h.terrainRoutes.POST(request(discovery())); assert.equal(saved.status, 201);
  const body = await saved.json(); await terrain.verifyAcquisitionTerrainSave(body, terrain.parseAcquisitionTerrain(discovery()));
  const read = await h.terrainRoutes.GET(); assert.match(read.headers.get("cache-control"), /private, no-store/);
  assert.deepEqual((await read.json()).discovery, terrain.parseAcquisitionTerrain(discovery()));
  const pointerKey = "acquisition/terrain/v1/latest.json", pointer = JSON.parse(new TextDecoder().decode(h.objects.get(pointerKey)));
  const inventoryPointer = JSON.parse(new TextDecoder().decode(h.objects.get("acquisition/v1/latest.json")));
  h.objects.set(pointerKey, encode({ ...pointer, key: inventoryPointer.key, sha256: inventoryPointer.sha256 }));
  assert.equal((await h.terrainRoutes.GET()).status, 503, "cannot cross the inventory storage namespace");
  h.objects.set(pointerKey, encode(pointer)); h.objects.set(pointer.key, encode({ corrupt: true }));
  assert.equal((await h.terrainRoutes.GET()).status, 503);
  assert.equal((await h.routes.GET()).status, 200, "terrain failure does not replace inventory");
});

test("local readback capture remains protected and cannot become provider-verified completion", async () => {
  const captured = { ...job(), state: "captured", checksum_basis: "capture-readback", provider_digest: null, checksum_verified: false, bytes_received: 40, storage: "local-protected-candidate", protected: true, intended_destination: "local-pc" };
  const value = { ...inventory(), jobs: [captured] };
  const parsed = schema.parseAcquisitionInventory(value); assert.ok(parsed);
  const projected = parsed.jobs[0];
  assert.equal(projected.state, "captured"); assert.equal(projected.bytes_received, 40);
  assert.equal(projected.checksum_verified, false); assert.equal(projected.provider_digest, null);
  assert.equal(projected.checksum_basis, "capture-readback"); assert.equal(projected.intended_destination, "local-pc");
  assert.equal(projected.storage, "local-protected-candidate");
  assert.equal(JSON.stringify(schema.parseAcquisitionInventory(parsed)), JSON.stringify(parsed), "projection remains stable for receipt readback hashes");
  assert.deepEqual(schema.acquisitionJobLabels(projected), { status: "Captured locally · not reviewed or admitted", checksum: "Stored-file hash checked; provider checksum unavailable", digest: "Stored-file SHA-256", storage: "Protected local candidate · outside replaceable cache" });
  for (const mutation of [
    { state: "complete" }, { state: "planned" }, { checksum_basis: undefined }, { checksum_basis: "provider-expected" },
    { provider_digest: undefined }, { provider_digest: "a".repeat(64) }, { checksum_verified: true },
    { sha256: null }, { sha256: "A".repeat(64) }, { bytes_received: undefined }, { bytes_received: 0 },
    { bytes_received: 41 }, { downloaded_bytes: 101, bytes_received: 101 }, { approved_max_bytes: undefined },
    { protected: false }, { storage: "local-replaceable-cache" }, { storage: "provider-remote" },
    { intended_destination: undefined }, { intended_destination: "remote" },
    { source_url: "https://earthengine.googleapis.com/download?token=secret" },
  ]) assert.equal(schema.parseAcquisitionInventory({ ...value, jobs: [{ ...captured, ...mutation }] }), null, JSON.stringify(mutation));
  const planned = { ...job(), state: "planned", storage: "provider-remote", sha256: null, checksum_verified: false, downloaded_bytes: 0, bytes_received: 0, protected: false, intended_destination: "local-pc" };
  assert.ok(schema.parseAcquisitionInventory({ ...value, jobs: [planned] }), "selected local destination is separate from current storage");
  const complete = schema.parseAcquisitionInventory({ ...value, jobs: [job()] }).jobs[0];
  assert.equal(complete.checksum_basis, undefined); assert.equal(complete.provider_digest, undefined);
  assert.equal(schema.acquisitionJobLabels(complete).digest, "Expected SHA-256");
  const h = await harness(), saved = await h.routes.POST(request(value)); assert.equal(saved.status, 201);
  const receipt = await saved.json(); await client.verifyAcquisitionSave(receipt, parsed);
  assert.deepEqual((await (await h.routes.GET()).json()).inventory, parsed);
  const prior = h.objects.get("acquisition/v1/latest.json");
  assert.equal((await h.routes.POST(request({ ...value, jobs: [{ ...captured, state: "complete" }] }))).status, 400);
  assert.deepEqual(h.objects.get("acquisition/v1/latest.json"), prior, "a forged complete claim cannot replace the valid snapshot");
});
