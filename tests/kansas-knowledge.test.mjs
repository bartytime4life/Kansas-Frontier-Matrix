import assert from "node:assert/strict";
import test from "node:test";
import { readFile } from "node:fs/promises";
import ts from "typescript";

const moduleUrl = source => "data:text/javascript;base64," + Buffer.from(ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText).toString("base64");
const pureUrl = moduleUrl(await readFile(new URL("../app/kansas-knowledge.ts", import.meta.url), "utf8"));
const pure = await import(pureUrl);
const serverSource = (await readFile(new URL("../app/kansas-knowledge-server.ts", import.meta.url), "utf8"))
  .replace('import { env } from "cloudflare:workers";', "const env = {};")
  .replace('import { getRawDb } from "../db";', "const getRawDb = () => null;")
  .replace('"./kansas-knowledge"', JSON.stringify(pureUrl));
const { readKansasKnowledge } = await import(moduleUrl(serverSource));

const now = "2026-09-30T18:00:00Z";
const ref = value => `kfm://knowledge/${value}`;
const record = {
  record_id: "ks-place-1", kind: "place", title: "Kansas place", summary: "A reviewed place description.",
  location_label: "Kansas", geometry_role: "statewide", time_start: null, time_end: null,
  source_ref: ref("source/gnis"), source_url: "https://www.usgs.gov/us-board-on-geographic-names/download-gnis-data",
  evidence_ref: ref("evidence/one"), rights_ref: ref("rights/one"), sensitivity_ref: ref("sensitivity/one"),
  review_ref: ref("review/one"), correction_state: "ACTIVE", public_state: "PUBLIC_SAFE",
  assertions_json: JSON.stringify([{ text: "The name is documented in the source.", source_ref: ref("source/gnis"), evidence_ref: ref("evidence/one"), status: "documented" }]),
};
const bytes = new TextEncoder().encode(JSON.stringify({ profile: "kfm.kansas-knowledge/v1", records: [record] }));
const releaseId = await pure.knowledgeDigest(bytes);
const release = {
  release_id: releaseId, package_sha256: releaseId,
  package_key: `kansas-knowledge/v1/objects/${releaseId.slice(7)}.json`,
  state: "APPROVED", reviewer_key: "reviewer", releaser_key: "releaser",
  reviewed_at: "2026-09-29T12:00:00Z", released_at: "2026-09-30T12:00:00Z",
  source_admission_ref: ref("admission/one"), rights_ref: ref("rights/one"), sensitivity_ref: ref("sensitivity/one"),
  policy_ref: ref("policy/one"), review_ref: ref("review/one"), release_ref: ref("release/one"),
};
let selectedRelease = release;
let rows = [{ ...record, release_id: releaseId }];
let storedBytes = bytes;
const db = { prepare(sql) { return { bind(...args) { this.args = args; return this; },
  async first() { return selectedRelease; },
  async all() { return { results: rows.filter(row => row.release_id === this.args[0] && row.public_state === "PUBLIC_SAFE" && row.correction_state === "ACTIVE" && (sql.includes("record_id = ?") ? row.record_id === this.args[1] : true)) }; },
}; } };
const bucket = { async get(key) { assert.equal(key, release.package_key); return { size: storedBytes.length, arrayBuffer: async () => Uint8Array.from(storedBytes).buffer }; } };
const read = async suffix => readKansasKnowledge(new Request(`https://example.test/api/governed/v1/knowledge${suffix}`), db, bucket, now);

test("released Kansas record is traceable through a versioned read", async () => {
  const response = await read("?term=Kansas");
  assert.equal(response.status, 200);
  const body = await response.json();
  assert.equal(body.envelope.outcome, "ANSWER");
  assert.equal(body.data.records[0].record_id, "ks-place-1");
  assert.equal(body.data.records[0].assertions[0].status, "documented");
  assert.equal(body.data.records[0].assertions_json, undefined);
  assert.equal(body.data.release_id, releaseId);
});

test("record detail selects exactly one released identifier", async () => {
  const selected = await (await read("?id=ks-place-1")).json();
  assert.equal(selected.envelope.reason_code, "RELEASED");
  assert.deepEqual(selected.data.records.map(item => item.record_id), ["ks-place-1"]);
  const absent = await (await read("?id=ks-place-2")).json();
  assert.equal(absent.envelope.reason_code, "RECORD_NOT_FOUND");
  assert.equal(absent.data, undefined);
});

test("missing review, withdrawal, and unreleased rows never enter search", async () => {
  try {
    selectedRelease = null;
    assert.equal((await (await read("")).json()).envelope.reason_code, "NO_APPROVED_KNOWLEDGE");
    selectedRelease = { ...release, state: "WITHDRAWN" };
    assert.equal((await (await read("")).json()).data, undefined);
    selectedRelease = release;
    rows = [{ ...record, release_id: releaseId, public_state: "WITHHELD" }];
    assert.equal((await (await read("?term=Kansas")).json()).envelope.reason_code, "RECORD_NOT_FOUND");
  } finally { selectedRelease = release; rows = [{ ...record, release_id: releaseId }]; }
});

test("tampered R2 package or D1 projection fails closed", async () => {
  try {
    storedBytes = new TextEncoder().encode("tampered");
    const badPackage = await read("");
    assert.equal(badPackage.status, 503);
    assert.equal((await badPackage.json()).data, undefined);
    storedBytes = bytes;
    rows = [{ ...record, release_id: releaseId, summary: "Altered in D1" }];
    assert.equal((await read("")).status, 503);
  } finally { storedBytes = bytes; rows = [{ ...record, release_id: releaseId }]; }
});

test("unsafe links, private fields, and unbounded queries are refused", async () => {
  assert.throws(() => pure.publicKnowledgeRecord({ ...record, release_id: releaseId, source_url: "https://evil.example/gnis" }), /SOURCE_LINK_INVALID/);
  assert.throws(() => pure.publicKnowledgeRecord({ ...record, release_id: releaseId, private_note: "secret" }), /RECORD_WITHHELD/);
  assert.equal((await read("?term=one&id=ks-place-1")).status, 400);
  assert.equal((await read("?term=" + "x".repeat(81))).status, 400);
});
