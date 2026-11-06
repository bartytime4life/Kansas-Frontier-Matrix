import test from "node:test";
import assert from "node:assert/strict";
import { mkdtemp, mkdir, writeFile, rm, symlink } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { createHash } from "node:crypto";
import { gzipSync } from "node:zlib";
import { verifyKansasSkyDay, importKansasSkyDay } from "../server/kansas-sky-archive.mjs";
import { RECEIPT_ALLOWANCE } from "../server/ingestion-config.mjs";

const sha = value => createHash("sha256").update(value).digest("hex");
const encoded = value => Buffer.from(`${JSON.stringify(value)}\n`);
async function candidate(t, { coverage = "provider-day-processed", hex = "abc123" } = {}) {
  const root = await mkdtemp(join(tmpdir(), "kfm-sky-import-test-"));
  t.after(() => rm(root, { recursive: true, force: true }));
  await mkdir(join(root, "raw")); await mkdir(join(root, "replays"));
  const day = "2025-11-03", tag = "v2025.11.03-planes-readsb-prod-0", id = `${day}-${hex.replace("~", "nonicao-")}-p0001`;
  const sourceUrl = `https://github.com/adsblol/globe_history_2025/releases/download/${tag}/${tag}.tar.aa`;
  const raw = gzipSync(encoded({ icao: hex, timestamp: Date.parse(day) / 1000, trace: [[100, 38, -98, 1000, 100, 90, 0, 0]] }));
  const point = { hex, providerId: "adsb-lol", timestampBasis: "provider", interpolated: false, breakBefore: true, observedAt: Date.parse(day) + 100_000, lon: -98, lat: 38 };
  const replay = { schemaVersion: 1, id, day, provider: "adsb.lol", license: "ODbL-1.0", licenseUrl: "https://opendatacommons.org/licenses/odbl/1-0/", sourceUrl, sourceSha256: sha(raw), sourceMember: `2025/11/03/traces/23/trace_full_${hex}.json`, points: [point] };
  const replayBytes = encoded(replay);
  const flight = { id, title: "Synthetic archive-import fixture", hex, day, part: 1, partCount: 1, pointCount: 1, segmentCount: 1, coverage,
    start: new Date(point.observedAt).toISOString(), end: new Date(point.observedAt).toISOString(), url: `/data/aviation/replays/days/${day}/${id}.json`, sha256: sha(replayBytes), provider: "adsb.lol", license: "ODbL-1.0", sourceUrl };
  const catalog = { schemaVersion: 1, flights: [flight] };
  const artifacts = [[`raw/${hex}.json.gz`, raw], [`replays/${id}.json`, replayBytes], ["replays/index.json", encoded(catalog)]];
  for (const [path, bytes] of artifacts) await writeFile(join(root, path), bytes);
  const receipt = { schemaVersion: 1, profile: "kfm-sky-day-candidate/v1", day, preparedAt: "2025-11-04T06:00:00Z", coverage,
    lifecycle: "WORK/QUARANTINE", releaseState: "unreleased", evidenceRole: "EXTERNAL_CONTEXT_ONLY", membersScanned: 1, aircraftCount: 1, pointCount: 1, fileCount: 1,
    source: { day, releaseUrl: `https://api.github.com/repos/adsblol/globe_history_2025/releases/tags/${tag}`, sourcePublishedAt: "2025-11-04T04:00:00Z",
      assets: [{ name: `${tag}.tar.aa`, url: sourceUrl, sha256: "a".repeat(64), bytes: 1024 }], downloadBytes: 1024, maxCandidateBytes: 2 * 1024 ** 3,
      provider: "adsb.lol", license: "ODbL-1.0", licenseUrl: "https://opendatacommons.org/licenses/odbl/1-0/", region: { west: -103.2, east: -93.6, south: 36.2, north: 40.9 } },
    artifacts: artifacts.map(([path, bytes]) => ({ path, bytes: bytes.length, sha256: sha(bytes) })) };
  const updateReceipt = async () => writeFile(join(root, "receipt.json"), encoded(receipt));
  await updateReceipt();
  return { root, receipt, replay, catalog, updateReceipt, async replaceArtifact(path, bytes) {
    await writeFile(join(root, path), bytes);
    Object.assign(receipt.artifacts.find(item => item.path === path), { bytes: bytes.length, sha256: sha(bytes) });
    await updateReceipt();
  } };
}
class Store {
  captures = new Map(); writes = []; claims = 0; releases = 0; used = 0; reserved = 0; capacity = Infinity; paused = false; failPath = null; corruptPath = null; expired = false; held = false;
  async claim() { this.claims++; if (this.paused) return null; this.token = String(this.claims); return this.token; }
  fence(token) { if (token !== this.token || this.expired) throw new Error("LEASE_LOST"); }
  async due(request, token) { this.fence(token); return !this.captures.has(request.id) && !this.held; }
  async reserve(request, token) { this.fence(token); const amount = request.limitBytes + RECEIPT_ALLOWANCE; if (this.used + amount > this.capacity) throw new Error("ARCHIVE_LIMIT_REACHED"); this.reserved = amount; return amount; }
  async save(request, capture, token, reservation) {
    this.fence(token); assert.equal(reservation, this.reserved);
    if (capture.receipt.candidatePath === this.failPath) throw new Error("synthetic interrupted write");
    const copy = { bytes: Buffer.from(capture.bytes), receipt: structuredClone(capture.receipt) };
    this.captures.set(request.id, copy); this.writes.push(copy.receipt.candidatePath); this.used += capture.bytes.length + 8192 + Buffer.byteLength(JSON.stringify(capture.receipt)); this.reserved = 0;
  }
  async read(id) { const value = this.captures.get(id); if (!value) throw new Error("CAPTURE_NOT_FOUND"); if (value.receipt.candidatePath === this.corruptPath) return { ...value, bytes: Buffer.from("corrupted") }; return value; }
  async failure(_request, token) { this.fence(token); this.reserved = 0; }
  async release(token) { assert.equal(token, this.token); this.releases++; this.reserved = 0; this.token = null; }
}
const apply = (root, store) => importKansasSkyDay(root, { apply: true, config: { ready: true }, store });

test("default verification never obtains a store and reports no active collection", async t => {
  const input = await candidate(t); let accessed = false;
  const result = await importKansasSkyDay(input.root, { config: { ready: true }, storeFactory: () => { accessed = true; throw new Error("unexpected access"); } });
  assert.equal(result.state, "verified-plan"); assert.equal(result.collectionActive, false); assert.equal(result.aircraftCount, 1); assert.equal(result.artifacts, 4); assert.equal(accessed, false);
});
test("unready configuration and partial diagnostic input cannot reach the store", async t => {
  const input = await candidate(t), partial = await candidate(t, { coverage: "partial-input" });
  const factory = () => { throw new Error("must not connect"); };
  assert.equal((await importKansasSkyDay(input.root, { apply: true, config: { ready: false }, storeFactory: factory })).reason, "STORAGE_CONFIGURATION_REQUIRED");
  assert.equal((await importKansasSkyDay(partial.root, { apply: true, config: { ready: true }, storeFactory: factory })).reason, "SKY_PARTIAL_INPUT_HELD");
});
test("candidate byte tampering is rejected before storage", async t => {
  const input = await candidate(t), store = new Store();
  await writeFile(join(input.root, input.receipt.artifacts[1].path), "tampered");
  await assert.rejects(apply(input.root, store), /SKY_ARTIFACT_INTEGRITY_FAILED/); assert.equal(store.claims, 0);
});
test("traversal and symlinked input directories cannot become archive artifacts", async t => {
  const input = await candidate(t);
  input.receipt.artifacts[0].path = "../outside.json.gz"; await input.updateReceipt();
  await assert.rejects(verifyKansasSkyDay(input.root), /SKY_ARTIFACT_MANIFEST_INVALID/);
  const clean = await candidate(t), link = `${clean.root}-linked`;
  await symlink(clean.root, link); t.after(() => rm(link, { force: true }));
  await assert.rejects(verifyKansasSkyDay(link), /SKY_PATH_REJECTED/);
  await rm(join(clean.root, "raw"), { recursive: true }); await symlink(input.root, join(clean.root, "raw"));
  await assert.rejects(verifyKansasSkyDay(clean.root), /SKY_PATH_REJECTED/);
});
test("source assets, catalog counts and unlisted files are independently checked", async t => {
  const source = await candidate(t); source.receipt.source.assets[0].url = "https://example.invalid/archive"; await source.updateReceipt();
  await assert.rejects(verifyKansasSkyDay(source.root), /SKY_ASSET_METADATA_INVALID/);
  const counts = await candidate(t); counts.receipt.pointCount++; await counts.updateReceipt();
  await assert.rejects(verifyKansasSkyDay(counts.root), /SKY_CATALOG_COUNTS_INVALID/);
  const extra = await candidate(t); await writeFile(join(extra.root, "unexpected.txt"), "extra");
  await assert.rejects(verifyKansasSkyDay(extra.root), /SKY_UNEXPECTED_ARTIFACT/);
});
test("raw expansion bounds apply even when the gzip digest is valid", async t => {
  const input = await candidate(t);
  await input.replaceArtifact(input.receipt.artifacts[0].path, gzipSync(Buffer.alloc(16 * 1024 * 1024 + 1, 32)));
  await assert.rejects(verifyKansasSkyDay(input.root), /SKY_RAW_TRACE_INVALID/);
});
test("non-ICAO hex identities use the preparer's encoded replay filenames", async t => {
  const input = await candidate(t, { hex: "~abc123" });
  assert.equal((await verifyKansasSkyDay(input.root)).plan.aircraftCount, 1);
});
test("fenced bounded writes retain the manifest last and retries are idempotent", async t => {
  const input = await candidate(t), store = new Store();
  const first = await apply(input.root, store);
  assert.equal(first.state, "retained-private"); assert.equal(first.complete, true); assert.equal(first.collectionActive, false); assert.equal(first.imported, 4);
  assert.equal(store.writes.at(-1), "receipt.json"); assert.equal(store.claims, 4); assert.equal(store.releases, 4);
  for (const capture of store.captures.values()) {
    assert.equal(capture.receipt.lifecycle, "WORK/QUARANTINE"); assert.equal(capture.receipt.releaseState, "unreleased"); assert.equal(capture.receipt.rightsReview, "pending"); assert.equal(capture.receipt.sensitivityReview, "pending");
  }
  const next = await apply(input.root, store); assert.equal(next.imported, 0); assert.equal(next.existing, 4); assert.equal(store.writes.length, 4);
});
test("an interrupted import has no completed-day receipt and resumes verified artifacts", async t => {
  const input = await candidate(t), store = new Store(); store.failPath = input.receipt.artifacts[1].path;
  const failed = await apply(input.root, store); assert.equal(failed.complete, false); assert.equal(failed.imported, 1); assert.equal(store.writes.includes("receipt.json"), false); assert.equal(store.reserved, 0);
  store.failPath = null;
  const resumed = await apply(input.root, store); assert.equal(resumed.complete, true); assert.equal(resumed.existing, 1); assert.equal(resumed.imported, 3); assert.equal(store.writes.at(-1), "receipt.json");
});
test("pause, capacity, retry holds and lost leases remain incomplete", async t => {
  const input = await candidate(t);
  for (const [property, value, reason] of [["paused", true, "PIPELINE_PAUSED_OR_BUSY"], ["capacity", 1, "ARCHIVE_LIMIT_REACHED"], ["held", true, "SKY_RETRY_HELD"], ["expired", true, "LEASE_LOST"]]) {
    const store = new Store(); store[property] = value;
    const result = await apply(input.root, store); assert.equal(result.complete, false); assert.equal(result.reason, reason); assert.equal(store.writes.includes("receipt.json"), false);
  }
});
test("stored readback corruption prevents the completed-day receipt", async t => {
  const input = await candidate(t), store = new Store(); store.corruptPath = input.receipt.artifacts[0].path;
  const result = await apply(input.root, store); assert.equal(result.reason, "SKY_STORED_INTEGRITY_FAILED"); assert.equal(result.complete, false); assert.equal(store.writes.includes("receipt.json"), false);
});
