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

test("terrain persistence projects metadata and rejects ambiguous work-unit identities", async () => {
  const value = discovery(), projected = terrain.parseAcquisitionTerrain({ ...value, private_extra: "not retained" });
  assert.ok(projected); assert.equal(projected.private_extra, undefined); assert.equal(projected.complete_for_state, false);
  assert.deepEqual(terrain.parseAcquisitionTerrain(projected), projected, "canonical projection remains stable when saved and read");
  for (const bad of [{ ...value, project_count: 2 }, { ...value, projects: [...value.projects, ...value.projects], project_count: 2 }, { ...value, projects: [{ ...value.projects[0], source_url: "https://other.example/ept.json" }] }]) assert.equal(terrain.parseAcquisitionTerrain(bad), null);
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
});


test("receipt inspector imports local files without hosted reads or save controls",async()=>{
 const {componentHarness,findNode,settle}=await import('./component-harness.mjs');
 let requests=0;
 const h=await componentHarness(new URL('../app/acquisition/workspace.tsx',import.meta.url),{
  'next/link':{default:'a'},'../acquisition-inventory':schema,'../acquisition-client':client,
  '../terrain-provenance':{TerrainProvenancePanel:()=>null},'../acquisition-terrain':terrain,'./workspace.module.css':{default:{}}
 },{fetch:()=>{requests++;throw new Error('No hosted request is expected');},AbortController});
 try{
  let tree=h.render(h.exports.default);h.commit();await settle();
  assert.equal(requests,0);assert.equal(findNode(tree,node=>node.type==='button'&&String(node.props.children).includes('Save')),undefined);
  const file=findNode(tree,node=>node.type==='input'&&node.props.type==='file');
  const value=inventory(),raw=JSON.stringify(value);file.props.onChange({target:{files:[{size:Buffer.byteLength(raw),text:async()=>raw}]}});
  await settle();tree=h.render(h.exports.default);h.commit();
  assert.equal(requests,0);assert.ok(findNode(tree,node=>node.type==='time'&&node.props.dateTime===value.generated_at));
 }finally{h.dispose();}
});
