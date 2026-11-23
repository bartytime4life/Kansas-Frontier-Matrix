import assert from "node:assert/strict";
import test from "node:test";
import { readFile } from "node:fs/promises";
import { DatabaseSync } from "node:sqlite";
import ts from "typescript";
import { createPublicAiHandler } from "../server/public-ai-handler.mjs";

const moduleUrl = source => "data:text/javascript;base64," + Buffer.from(ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText).toString("base64");
const pureUrl = moduleUrl(await readFile(new URL("../app/kansas-knowledge.ts", import.meta.url), "utf8"));
const pure = await import(pureUrl);
const serverSource = (await readFile(new URL("../app/kansas-knowledge-server.ts", import.meta.url), "utf8"))
  .replace('import { env } from "cloudflare:workers";', "const env = {};")
  .replace('import { getRawDb } from "../db";', "const getRawDb = () => null;")
  .replace('"./kansas-knowledge"', JSON.stringify(pureUrl));
const { readKansasKnowledge } = await import(moduleUrl(serverSource));
const readerUrl = moduleUrl((await readFile(new URL("../app/knowledge-read.ts", import.meta.url), "utf8"))
  .replace('import { browserJsonRequest } from "./browser-json-request";', "")
  .replace('"./kansas-knowledge"', JSON.stringify(pureUrl)));
const evidenceSource = (await readFile(new URL("../app/hosted-ai-evidence.ts", import.meta.url), "utf8"))
  .replace("import { kansasKnowledgeRead } from './kansas-knowledge-server';", "export let kansasKnowledgeRead; export const setReader = reader => { kansasKnowledgeRead = reader; };")
  .replace("'./knowledge-read'", JSON.stringify(readerUrl));

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

test("Ask BARTA applies Unicode place and date scope before the real SQLite search limit", async t => {
  const sqlite = new DatabaseSync(":memory:");
  t.after(() => sqlite.close());
  const candidates = Array.from({ length: 22 }, (_, index) => ({
    ...record,
    record_id: `drought-${index + 1}`,
    title: `Drought ${String(index + 1).padStart(2, "0")}`,
    location_label: index >= 20 || index < 10 ? "Éllsworth County, Kansas" : "Allen County, Kansas",
    time_start: index === 21 ? null : index < 10 ? "2020-01-01" : "2026-08-18",
    time_end: index === 21 ? null : index < 10 ? "2020-12-31" : "2026-08-25",
  }));
  const candidateBytes = new TextEncoder().encode(JSON.stringify({ profile: "kfm.kansas-knowledge/v1", records: candidates }));
  const id = await pure.knowledgeDigest(candidateBytes);
  const approved = { ...release, release_id: id, package_sha256: id, package_key: `kansas-knowledge/v1/objects/${id.slice(7)}.json` };
  sqlite.exec("CREATE TABLE knowledge_active (singleton INTEGER, release_id TEXT)");
  sqlite.exec("CREATE TABLE knowledge_releases (" + Object.keys(approved).map(key => key + " TEXT").join(",") + ")");
  const approvedRows = candidates.map(candidate => ({ ...candidate, release_id: id }));
  sqlite.exec("CREATE TABLE knowledge_public (" + Object.keys(approvedRows[0]).map(key => key + " TEXT").join(",") + ")");
  sqlite.prepare("INSERT INTO knowledge_active VALUES (1, ?)").run(id);
  sqlite.prepare("INSERT INTO knowledge_releases VALUES (" + Object.keys(approved).map(() => "?").join(",") + ")").run(...Object.values(approved));
  const insert = sqlite.prepare("INSERT INTO knowledge_public VALUES (" + Object.keys(approvedRows[0]).map(() => "?").join(",") + ")");
  for (const row of approvedRows) insert.run(...Object.values(row));
  // These projections must stay outside the public reader, before verification.
  insert.run(...Object.values({ ...approvedRows[20], record_id: "withheld", public_state: "WITHHELD" }));
  insert.run(...Object.values({ ...approvedRows[20], record_id: "other-release", release_id: releaseId }));
  insert.run(...Object.values({ ...approvedRows[20], record_id: "superseded", correction_state: "SUPERSEDED" }));
  const actualDb = { prepare(sql) {
    const prepared = sqlite.prepare(sql);
    let parameters = [];
    return {
      bind(...args) { parameters = args; return this; },
      async first() { return prepared.get(...parameters); },
      async all() { return { results: prepared.all(...parameters) }; },
    };
  } };
  let storageAvailable = true;
  const actualBucket = { async get(key) {
    assert.equal(key, approved.package_key);
    if (!storageAvailable) return null;
    return { size: candidateBytes.length, arrayBuffer: async () => Uint8Array.from(candidateBytes).buffer };
  } };
  const origin = "https://kansasfrontiermatrix.com";
  const readFixture = (request, scope) => readKansasKnowledge(request, actualDb, actualBucket, now, scope);
  const url = origin + "/api/governed/v1/knowledge?";
  const http = await (await readFixture(new Request(url + "term=drought"))).json();
  assert.equal(http.data.records.length, 20);
  assert.equal(http.data.records.at(-1).record_id, "drought-20");
  assert.equal(http.data.has_more, true);
  assert.equal((await readFixture(new Request(url + "term=drought&place=Allen"))).status, 400);

  const { researchEvidence, setReader } = await import(moduleUrl(evidenceSource));
  setReader(readFixture);
  const query = { term: "drought", place: "éLLsworth", start: "2026-08-25", end: "2026-09-01" };

  let calls = 0;
  const handle = createPublicAiHandler({ origin, resolveEvidence: value => researchEvidence(value, origin),
    model: { ready: true, online: true, discuss: async () => { calls++; throw new Error("Evidence must not run inference"); } } });
  const ask = async selection => {
    const accepted = await handle(new Request(origin + "/api/ai/jobs", { method: "POST",
      headers: { "content-type": "application/json", origin }, body: JSON.stringify({ ...selection, question: "Find dated drought records.", mode: "evidence" }) }));
    assert.equal(accepted.status, 202);
    const cookie = accepted.headers.get("set-cookie").split(";")[0];
    const { id: jobId } = await accepted.json();
    const check = async () => (await handle(new Request(origin + "/api/ai/jobs/" + jobId, { headers: { cookie } }))).json();
    for (let i = 0; i < 30; i++) {
      const job = await check();
      if (job.state === "completed") return { result: job.result, check };
      await new Promise(resolve => setImmediate(resolve));
    }
    throw new Error("Evidence job did not complete");
  };
  const found = await ask(query);
  assert.equal(found.result.outcome, "ABSTAIN");
  assert.equal(found.result.reasonCode, "EVIDENCE_MODEL_UNQUALIFIED");
  assert.equal(found.result.answer, null);
  assert.deepEqual(found.result.citations.map(citation => citation.url), [origin + "/knowledge/record?id=drought-21"]);
  assert.equal((await ask({ ...query, place: "Saline County" })).result.reasonCode, "NO_RELEASED_EVIDENCE");

  const scoped = await (await readFixture(new Request(url + "term=drought"), { place: query.place, start: query.start, end: query.end })).json();
  assert.deepEqual(scoped.data.records.map(item => item.record_id), ["drought-21"]);
  assert.equal(scoped.data.has_more, false);
  assert.equal((await readFixture(new Request(url + "term=drought"), { place: "", start: "2026-02-30", end: "" })).status, 400);
  const literal = await (await readFixture(new Request(url + "term=drought"), { place: "%_", start: "", end: "" })).json();
  assert.equal(literal.envelope.reason_code, "RECORD_NOT_FOUND");

  sqlite.prepare("UPDATE knowledge_releases SET state = 'WITHDRAWN' WHERE release_id = ?").run(id);
  const withdrawn = (await found.check()).result;
  assert.equal(withdrawn.reasonCode, "RELEASE_CHANGED");
  assert.equal(withdrawn.citations, undefined);
  assert.equal((await ask(query)).result.reasonCode, "EVIDENCE_WITHHELD");
  sqlite.prepare("UPDATE knowledge_releases SET state = 'APPROVED' WHERE release_id = ?").run(id);
  storageAvailable = false;
  assert.equal((await ask(query)).result.reasonCode, "EVIDENCE_WITHHELD");
  assert.equal(calls, 0);
});
