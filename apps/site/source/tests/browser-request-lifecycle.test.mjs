import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

async function compile(name, imports = {}) {
  const source = await readFile(new URL(`../app/${name}.ts`, import.meta.url), "utf8");
  const code = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 } }).outputText;
  const compiled = { exports: {} };
  new Function("require", "module", "exports", code)(id => imports[id], compiled, compiled.exports);
  return compiled.exports;
}
const bounded = await compile("bounded-json");
const transport = await compile("browser-json-request", { "./bounded-json": bounded });
const pure = await compile("kansas-knowledge");
const knowledge = await compile("knowledge-read", { "./browser-json-request": transport, "./kansas-knowledge": pure });
const { browserJsonRequest } = transport;
const bytes = text => new TextEncoder().encode(text);
const release = `sha256:${"a".repeat(64)}`;
const ref = name => `kfm://knowledge/${name}`;
const record = pure.publicKnowledgeRecord({
  record_id: "ks-place-1", release_id: release, kind: "place", title: "Kansas test place", summary: "Synthetic test fixture.",
  location_label: "Kansas", geometry_role: "statewide", time_start: null, time_end: null,
  source_ref: ref("source"), source_url: "https://www.usgs.gov/us-board-on-geographic-names/download-gnis-data",
  evidence_ref: ref("evidence"), rights_ref: ref("rights"), sensitivity_ref: ref("sensitivity"), review_ref: ref("review"),
  correction_state: "ACTIVE", public_state: "PUBLIC_SAFE",
  assertions_json: JSON.stringify([{ text: "Synthetic assertion.", status: "documented", source_ref: ref("source"), evidence_ref: ref("evidence") }]),
});
const released = () => ({ envelope: { outcome: "ANSWER", reason_code: "RELEASED" }, data: {
  records: [structuredClone(record)], release_id: release, reviewed_at: "2026-09-29T00:00:00Z", released_at: "2026-09-30T00:00:00Z", has_more: false,
} });
const recordQuery = { kind: "record", id: record.record_id };

function mockFetch(t, implementation) { t.mock.method(globalThis, "fetch", implementation); }

test("request transport keeps cookies same-origin, disables cache, and preserves explicit write bodies", async t => {
  mockFetch(t, async (url, options) => {
    assert.equal(url, "/api/historical-topo/overlay");
    assert.equal(options.credentials, "same-origin");
    assert.equal(options.cache, "no-store");
    assert.equal(options.method, "POST");
    assert.deepEqual(JSON.parse(options.body), { id: 4628 });
    return Response.json({ state: "preparing", scanId: 122705 });
  });
  const result = await browserJsonRequest("/api/historical-topo/overlay", { method: "POST", body: JSON.stringify({ id: 4628 }), signal: new AbortController().signal, maxBytes: 4096 });
  assert.equal(result.body.state, "preparing");
});

test("a deadline cancels a stalled body and releases its stream lock", async t => {
  let canceled = false;
  const response = new Response(new ReadableStream({ start(controller) { controller.enqueue(bytes('{"pending":')); }, cancel() { canceled = true; } }));
  mockFetch(t, async () => response);
  await assert.rejects(browserJsonRequest("/api/historical-topo/review?scan=122705", { signal: new AbortController().signal, maxBytes: 4096, timeoutMs: 15 }), { name: "TimeoutError" });
  assert.equal(canceled, true);
  assert.equal(response.body.locked, false);
});

test("a deadline also aborts a request that has not received headers", async t => {
  mockFetch(t, (_url, { signal }) => new Promise((_resolve, reject) => signal.addEventListener("abort", () => reject(signal.reason), { once: true })));
  await assert.rejects(browserJsonRequest("/api/historical-topo/overlay?scan=122705", { signal: new AbortController().signal, maxBytes: 4096, timeoutMs: 15 }), { name: "TimeoutError" });
});

test("changing selection cancels a partial body before any result can be delivered", async t => {
  let entered;
  const started = new Promise(resolve => { entered = resolve; });
  let canceled = false;
  mockFetch(t, async () => new Response(new ReadableStream({
    start(controller) { controller.enqueue(bytes('{"envelope":')); entered(); },
    cancel() { canceled = true; },
  })));
  const selected = new AbortController();
  const pending = knowledge.readKnowledge(recordQuery, selected.signal);
  await started;
  selected.abort();
  await assert.rejects(pending, { name: "AbortError" });
  assert.equal(canceled, true);
});

test("late response from a transport that ignores cancellation cannot replace the new selection", async t => {
  let finishOld;
  const oldResponse = new Promise(resolve => { finishOld = resolve; });
  mockFetch(t, url => url.endsWith("id=ks-place-1") ? oldResponse : Promise.resolve(Response.json({ envelope: { outcome: "ABSTAIN", reason_code: "RECORD_NOT_FOUND" } })));
  const oldSelection = new AbortController();
  const pending = knowledge.readKnowledge(recordQuery, oldSelection.signal);
  oldSelection.abort();
  const current = await knowledge.readKnowledge({ kind: "record", id: "ks-place-2" }, new AbortController().signal);
  finishOld(Response.json(released()));
  await assert.rejects(pending, { name: "AbortError" });
  assert.equal(current.envelope.reason_code, "RECORD_NOT_FOUND");
  assert.equal(current.data, undefined);
});

test("bounded transport rejects declared and streaming oversize responses and malformed JSON", async t => {
  let response = new Response("{}", { headers: { "content-length": "4097" } });
  mockFetch(t, async () => response);
  const read = () => browserJsonRequest("/api/historical-topo/overlay", { signal: new AbortController().signal, maxBytes: 4096 });
  await assert.rejects(read(), bounded.JsonLimitError);
  response = new Response("x".repeat(4097));
  await assert.rejects(read(), bounded.JsonLimitError);
  response = new Response('{"state":');
  await assert.rejects(read(), SyntaxError);
});

test("an aborted request never starts another fetch", async t => {
  let requests = 0;
  mockFetch(t, async () => { requests++; return Response.json({}); });
  const controller = new AbortController(); controller.abort();
  await assert.rejects(browserJsonRequest("/api/historical-topo/overlay", { signal: controller.signal, maxBytes: 4096 }), { name: "AbortError" });
  assert.equal(requests, 0);
});

test("knowledge reads retain exact identity and reject a different record or release", () => {
  assert.deepEqual(knowledge.parseKnowledgeRead(released(), recordQuery).data.records, [record]);
  assert.throws(() => knowledge.parseKnowledgeRead(released(), { kind: "record", id: "ks-place-2" }), /identity mismatch/);
  const wrongRelease = released(); wrongRelease.data.release_id = `sha256:${"b".repeat(64)}`;
  assert.throws(() => knowledge.parseKnowledgeRead(wrongRelease, recordQuery), /identity mismatch/);
});

test("negative knowledge outcomes discard injected records and contradictory outcomes fail closed", () => {
  for (const reason of ["NO_APPROVED_KNOWLEDGE", "RECORD_NOT_FOUND", "RELEASE_HELD", "INVALID_QUERY"]) {
    const result = knowledge.parseKnowledgeRead({ ...released(), envelope: { outcome: "ABSTAIN", reason_code: reason } }, recordQuery);
    assert.equal(result.data, undefined);
  }
  assert.throws(() => knowledge.parseKnowledgeRead({ ...released(), envelope: { outcome: "ABSTAIN", reason_code: "RELEASED" } }, recordQuery));
  assert.throws(() => knowledge.parseKnowledgeRead({ ...released(), envelope: { outcome: "ANSWER", reason_code: "RELEASE_HELD" } }, recordQuery));
});

test("knowledge display rejects withheld records, malformed assertions, unsafe links and duplicate rows", () => {
  for (const patch of [{ public_state: "WITHHELD" }, { source_url: "javascript:alert(1)" }, { assertions: [] }, { private_note: "hidden" }]) {
    const value = released(); Object.assign(value.data.records[0], patch);
    assert.throws(() => knowledge.parseKnowledgeRead(value, recordQuery));
  }
  const duplicates = released(); duplicates.data.records.push(record);
  assert.throws(() => knowledge.parseKnowledgeRead(duplicates, { kind: "search", term: "Kansas" }), /Duplicate/);
});

test("invalid-query responses stay explainable while HTTP failures cannot masquerade as releases", async t => {
  let response = Response.json({ envelope: { outcome: "ABSTAIN", reason_code: "INVALID_QUERY" } }, { status: 400 });
  mockFetch(t, async () => response);
  assert.equal((await knowledge.readKnowledge({ kind: "record", id: "" }, new AbortController().signal)).envelope.reason_code, "INVALID_QUERY");
  response = Response.json(released(), { status: 503 });
  await assert.rejects(knowledge.readKnowledge(recordQuery, new AbortController().signal), /unavailable/);
});
