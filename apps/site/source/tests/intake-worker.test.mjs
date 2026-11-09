import assert from "node:assert/strict";
import { webcrypto } from "node:crypto";
import { readFileSync, readdirSync } from "node:fs";
import path from "node:path";
import test from "node:test";
import { Miniflare, convertV4MiniflareOptions } from "miniflare";
import ts from "typescript";

const compile = (file, imports = {}, signal = AbortSignal) => {
  const output = ts.transpileModule(readFileSync(file, "utf8"), { compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 } }).outputText;
  const mod = { exports: {} };
  new Function("require", "module", "exports", "AbortSignal", output)(name => {
    if (!(name in imports)) throw new Error(`Unexpected intake fixture import: ${name}`);
    return imports[name];
  }, mod, mod.exports, signal);
  return mod.exports;
};
const bounded = compile("app/bounded-json.ts");
const MAX_UPLOAD_BYTES = 10 * 1024 * 1024;
const original = Uint8Array.of(0, 255, 13, 10, 195, 169, 42);
const digest = async bytes => Buffer.from(await webcrypto.subtle.digest("SHA-256", bytes)).toString("hex");
class IntakeError extends Error { constructor(message, status = 400) { super(message); this.status = status; } }
const intakeHeaders = { "Cache-Control": "private, no-store", "X-Content-Type-Options": "nosniff", Vary: "Cookie" };
async function downloadFixture({ bytes = original, size = bytes.length, rowChanges = {}, body, authStatus, ownershipStatus, signal = AbortSignal } = {}) {
  const calls = [], mutations = [];
  const id = "12345678-1234-1234-1234-123456789abc";
  const row = { id, fileName: "measurements résumé's.csv", fileBytes: original.length, fileSha256: await digest(original), ownerKey: "fixture-owner", objectKey: "quarantine/fixture-owner/original", ...rowChanges };
  let stream;
  const server = {
    IntakeError, intakeHeaders,
    intakeUser: async () => { calls.push("authenticate"); if (authStatus) throw new IntakeError("Sign in.", authStatus); return { key: row.ownerKey, steward: false }; },
    ownedSubmission: async (requested, user) => { calls.push("ownership"); assert.equal(requested, id); assert.equal(user.key, row.ownerKey); if (ownershipStatus) throw new IntakeError("Submission not found.", ownershipStatus); return row; },
    intakeStore: () => { calls.push("store"); return { bucket: {
      get: async key => { calls.push("object"); assert.equal(key, row.objectKey); stream = body ? body() : new Response(bytes).body; return { body: stream, size }; },
      put: (...args) => { mutations.push(["put", ...args]); throw new Error("Fixture original must not be changed"); },
      delete: (...args) => { mutations.push(["delete", ...args]); throw new Error("Fixture original must not be deleted"); },
    } }; },
    sha256: async bytes => { calls.push("digest"); return digest(bytes); },
    submissionReviews: async () => [],
    intakeFailure: error => {
      assert.ok(error instanceof IntakeError, `Unexpected fixture failure: ${error}`);
      return Response.json({ error: error.message }, { status: error.status, headers: intakeHeaders });
    },
  };
  const route = compile("app/api/data-submissions/[id]/route.ts", { "../../../data-intake": { MAX_UPLOAD_BYTES }, "../../../data-intake-server": server, "../../../bounded-json": bounded }, signal);
  return { calls, mutations, row, get stream() { return stream; },
    get: (options = {}) => route.GET(new Request(`https://site.test/api/data-submissions/${id}?download=1`, options), { params: Promise.resolve({ id }) }),
    detail: () => route.GET(new Request(`https://site.test/api/data-submissions/${id}`), { params: Promise.resolve({ id }) }),
  };
}

test("original download verifies binary bytes and preserves private filename and receipt provenance", async () => {
  const h = await downloadFixture(), before = structuredClone(h.row);
  const response = await h.get();
  assert.equal(response.status, 200);
  assert.deepEqual(new Uint8Array(await response.arrayBuffer()), original);
  assert.equal(response.headers.get("content-length"), String(original.length));
  assert.equal(response.headers.get("content-type"), "application/octet-stream");
  assert.equal(response.headers.get("cache-control"), "private, no-store");
  assert.equal(response.headers.get("x-content-type-options"), "nosniff");
  assert.equal(response.headers.get("vary"), "Cookie");
  assert.equal(response.headers.get("content-security-policy"), "sandbox; default-src 'none'");
  assert.match(response.headers.get("content-disposition"), /^attachment; filename="kfm-[0-9a-f-]+\.csv"; filename\*=UTF-8''measurements%20r%C3%A9sum%C3%A9%27s\.csv$/);
  assert.deepEqual(h.calls, ["authenticate", "ownership", "store", "object", "digest"]);
  assert.equal(h.stream.locked, false);
  const detail = await (await h.detail()).json();
  assert.equal(detail.submission.fileBytes, original.length);
  assert.equal(detail.submission.fileSha256, await digest(original));
  assert.equal(detail.submission.fileName, h.row.fileName);
  assert.equal("objectKey" in detail.submission, false); assert.equal("ownerKey" in detail.submission, false);
  assert.deepEqual(h.row, before); assert.deepEqual(h.mutations, []);
});

test("original download rejects short and same-length changed bodies before returning bytes", async () => {
  for (const bytes of [original.slice(0, -1), original.map(byte => byte ^ 1)]) {
    const h = await downloadFixture({ bytes, size: original.length }), before = structuredClone(h.row);
    const response = await h.get();
    assert.equal(response.status, 409);
    assert.match((await response.json()).error, /Original file integrity failed/);
    assert.equal(response.headers.has("content-disposition"), false);
    assert.equal(response.headers.get("cache-control"), "private, no-store");
    assert.equal(h.stream.locked, false);
    assert.deepEqual(h.row, before); assert.deepEqual(h.mutations, []);
  }
});

test("original download accepts the exact 10 MiB upload boundary without changing bytes", async () => {
  const bytes = new Uint8Array(MAX_UPLOAD_BYTES); bytes[0] = 255; bytes[bytes.length - 1] = 42;
  const hash = await digest(bytes);
  const h = await downloadFixture({ bytes, rowChanges: { fileBytes: bytes.length, fileSha256: hash } });
  const response = await h.get();
  assert.equal(response.status, 200); assert.equal(response.headers.get("content-length"), String(bytes.length));
  assert.equal(await digest(await response.arrayBuffer()), hash);
  assert.deepEqual(h.mutations, []);
});

test("original download checks recorded and storage size metadata after ownership and before body reads", { timeout: 1000 }, async () => {
  for (const rowChanges of [{ fileBytes: 0 }, { fileBytes: MAX_UPLOAD_BYTES + 1 }, { fileBytes: 1.5 }, { fileSha256: "not-a-sha" }]) {
    const h = await downloadFixture({ rowChanges });
    assert.equal((await h.get()).status, 409);
    assert.deepEqual(h.calls, ["authenticate", "ownership"]);
    assert.deepEqual(h.mutations, []);
  }
  let canceled = 0, pulled = 0;
  const h = await downloadFixture({ size: original.length + 1, body: () => new ReadableStream({ pull() { pulled++; }, cancel() { canceled++; return new Promise(() => {}); } }, { highWaterMark: 0 }) });
  assert.equal((await h.get()).status, 409);
  assert.equal(canceled, 1); assert.equal(pulled, 0); assert.deepEqual(h.mutations, []);
  for (const status of [401, 404]) {
    const denied = await downloadFixture(status === 401 ? { authStatus: status } : { ownershipStatus: status });
    assert.equal((await denied.get()).status, status);
    assert.deepEqual(denied.calls, status === 401 ? ["authenticate"] : ["authenticate", "ownership"]);
  }
});

test("original download caps an oversized stream despite recorded size and nonsettling cancellation", { timeout: 1000 }, async () => {
  let pulls = 0, canceled = 0;
  const h = await downloadFixture({ body: () => new ReadableStream({
    pull(controller) { pulls++; controller.enqueue(new Uint8Array(3)); },
    cancel() { canceled++; return new Promise(() => {}); },
  }, { highWaterMark: 0 }) });
  const response = await h.get();
  assert.equal(response.status, 409); assert.match((await response.json()).error, /integrity failed/);
  assert.equal(pulls, 3); assert.equal(canceled, 1); assert.equal(h.stream.locked, false);
  assert.equal(h.calls.includes("digest"), false); assert.deepEqual(h.mutations, []);
});

test("original download returns a finite failure for deadline and caller-aborted stalled storage reads", { timeout: 1000 }, async () => {
  for (const abortCaller of [false, true]) {
    const deadline = new AbortController(), caller = new AbortController(), deadlines = [];
    let started, canceled = 0;
    const reading = new Promise(resolve => { started = resolve; });
    const h = await downloadFixture({ signal: { any: signals => AbortSignal.any(signals), timeout: ms => { deadlines.push(ms); return deadline.signal; } }, body: () => new ReadableStream({
      pull() { started(); }, cancel() { canceled++; return new Promise(() => {}); },
    }, { highWaterMark: 0 }) });
    const pending = h.get({ signal: caller.signal });
    await reading; (abortCaller ? caller : deadline).abort(new DOMException("Fixture interrupted", abortCaller ? "AbortError" : "TimeoutError"));
    const response = await pending;
    assert.equal(response.status, 503); assert.match((await response.json()).error, /could not be read/);
    assert.deepEqual(deadlines, [10_000]); assert.equal(canceled, 1); assert.equal(h.stream.locked, false);
    assert.equal(h.calls.includes("digest"), false); assert.deepEqual(h.mutations, []);
  }
});

test("private intake persists bytes and audit history, scopes reads, and serializes competing reviews", async () => {
  const root = path.resolve("dist/server");
  const files = readdirSync(root, { recursive: true }).filter((p) => p.endsWith(".js"));
  const modules = ["index.js", ...files.filter((p) => p !== "index.js")].map((p) => ({ type: "ESModule", path: path.join(root, p) }));
  const mf = new Miniflare(convertV4MiniflareOptions({ modules, modulesRoot: root, compatibilityDate: "2026-08-28", compatibilityFlags: ["nodejs_compat"], d1Databases: ["DB"], r2Buckets: ["BUCKET"], bindings: { KFM_STEWARD_EMAILS: "steward@example.test" } }));
  try {
    const db = await mf.getD1Database("DB");
    for (const file of readdirSync("drizzle").filter((p) => p.endsWith(".sql")).sort()) for (const sql of readFileSync(`drizzle/${file}`, "utf8").split("--> statement-breakpoint").map((v) => v.trim()).filter(Boolean)) await db.prepare(sql).run();
    const origin = (await mf.ready).origin;
    const headers = (email) => ({ "oai-authenticated-user-email": email, "oai-authenticated-user-id": `test-${email}`, Origin: origin });
    const request = async (url, email, init = {}) => {
      // Serialize browser-native FormData before crossing Miniflare's separate
      // fetch implementation; preserve the generated multipart boundary.
      const req = new Request(origin + url, { ...init, headers: { ...headers(email), ...init.headers } });
      return mf.dispatchFetch(req.url, { method: req.method, headers: Object.fromEntries(req.headers), body: ["GET","HEAD"].includes(req.method) ? undefined : await req.arrayBuffer() });
    };
    const form = (overrides = {}, file = "readings.csv") => {
      const data = new FormData();
      const fields = { title: "Kansas station readings", sourceId: "usgs-streamflow", sourceUrl: "https://waterdata.usgs.gov/", description: "Public historical stream observations with units and source dates.", license: "US public domain", sensitivity: "public", startDate: "1917-06-12", endDate: "1917-06-12", permission: "yes", ...overrides };
      for (const [k,v] of Object.entries(fields)) data.set(k,v);
      data.set("file", new File(["date,flow_cfs\n1917-06-12,12400\n"], file, { type: "text/csv" })); return data;
    };
    assert.equal((await mf.dispatchFetch(origin + "/api/data-submissions")).status, 401);
    assert.equal((await request("/api/data-submissions?scope=review", "contributor@example.test")).status, 403);
    assert.equal((await request("/api/data-submissions", "contributor@example.test", { method: "POST", body: form(), headers: { Origin: "https://other.test" } })).status, 403);
    const badFile = await request("/api/data-submissions", "contributor@example.test", { method: "POST", body: form({}, "payload.html") });
    assert.equal(badFile.status, 400, await badFile.text());
    assert.equal((await request("/api/data-submissions", "contributor@example.test", { method: "POST", body: form({ sourceUrl: "javascript:alert(1)" }) })).status, 400);
    const upload = await request("/api/data-submissions", "contributor@example.test", { method: "POST", body: form() });
    assert.equal(upload.status, 201, await upload.clone().text());
    const receipt = await upload.json(); assert.match(receipt.fileSha256, /^[0-9a-f]{64}$/);
    const id = receipt.id; const url = `/api/data-submissions/${id}`;
    assert.equal((await request(url, "other@example.test")).status, 404);
    assert.equal((await request(url + "?download=1", "other@example.test")).status, 404);
    const file = await request(url + "?download=1", "contributor@example.test");
    assert.equal(file.status, 200); assert.match(file.headers.get("content-disposition"), /^attachment;/); assert.equal(file.headers.get("cache-control"), "private, no-store");
    assert.equal(file.headers.get("content-length"), String(new TextEncoder().encode("date,flow_cfs\n1917-06-12,12400\n").length));
    assert.equal(file.headers.get("x-content-type-options"), "nosniff"); assert.equal(file.headers.get("content-security-policy"), "sandbox; default-src 'none'");
    assert.equal(await file.text(), "date,flow_cfs\n1917-06-12,12400\n");
    const initial = await (await request(url, "steward@example.test")).json();
    assert.equal(initial.submission.version, 1); assert.equal(initial.reviews.length, 0); assert.equal(initial.canReview, true);
    assert.equal("objectKey" in initial.submission, false); assert.equal("ownerKey" in initial.submission, false);
    const patch = (version, status) => ({ method: "PATCH", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ version, status, note: "Inspected source, public reuse terms, units and completeness." }) });
    assert.equal((await request(url, "contributor@example.test", patch(1,"accepted"))).status, 403);
    assert.equal((await request(url, "steward@example.test", patch(1,"accepted"))).status, 200);
    const reviewed = await (await request(url, "contributor@example.test")).json();
    assert.equal(reviewed.submission.status, "accepted"); assert.equal(reviewed.submission.version, 2); assert.equal(reviewed.reviews.length, 1);
    const competition = await Promise.all([request(url, "steward@example.test", patch(2,"under_review")), request(url, "steward@example.test", patch(2,"changes_requested"))]);
    assert.deepEqual(competition.map((r) => r.status).sort(), [200,409]);
    const final = await (await request(url, "contributor@example.test")).json(); assert.equal(final.reviews.length, 2); assert.equal(final.submission.version, 3);
    const mine = await (await request("/api/data-submissions", "contributor@example.test")).json(); assert.equal(mine.items.length, 1);
    const others = await (await request("/api/data-submissions", "other@example.test")).json(); assert.equal(others.items.length, 0);
    const queue = await (await request("/api/data-submissions?scope=review", "steward@example.test")).json(); assert.equal(queue.items.length, 1);
    const heldUpload = await request("/api/data-submissions", "contributor@example.test", { method: "POST", body: form({ license: "Unknown", sensitivity: "unknown" }) });
    const held = await heldUpload.json(); assert.equal(heldUpload.status,201);
    assert.equal((await request(`/api/data-submissions/${held.id}`, "steward@example.test", patch(1,"accepted"))).status,400);
    assert.equal((await request(`/api/data-submissions/${held.id}`, "steward@example.test", patch(1,"changes_requested"))).status,200);
    const larger = form(); larger.set("file", new File(["a,b\n".repeat(300_000)], "larger.csv", { type: "text/csv" }));
    const largeResponse = await request("/api/data-submissions", "contributor@example.test", { method: "POST", body: larger });
    assert.equal(largeResponse.status,201,await largeResponse.text());
    // Corrupt only disposable fixture objects. The route must report a conflict
    // without replacing bytes or changing the receipt, status or review history.
    const bucket = await mf.getR2Bucket("BUCKET");
    const submitted = "date,flow_cfs\n1917-06-12,12400\n";
    for (const changed of [submitted.slice(0, -1), submitted.replace("12400", "99999")]) {
      const upload = await request("/api/data-submissions", "contributor@example.test", { method: "POST", body: form() });
      assert.equal(upload.status, 201); const receipt = await upload.json();
      const row = await db.prepare("SELECT object_key, file_bytes, file_sha256, status, version FROM data_submissions WHERE id = ?").bind(receipt.id).first();
      await bucket.put(row.object_key, changed);
      const denied = await request(`/api/data-submissions/${receipt.id}?download=1`, "contributor@example.test");
      assert.equal(denied.status, 409); assert.match((await denied.json()).error, /Original file integrity failed/);
      assert.equal(denied.headers.has("content-disposition"), false);
      assert.equal(await (await bucket.get(row.object_key)).text(), changed);
      assert.deepEqual(await db.prepare("SELECT object_key, file_bytes, file_sha256, status, version FROM data_submissions WHERE id = ?").bind(receipt.id).first(), row);
      const detail = await (await request(`/api/data-submissions/${receipt.id}`, "contributor@example.test")).json();
      assert.equal(detail.submission.fileSha256, receipt.fileSha256); assert.equal(detail.reviews.length, 0);
    }
  } finally { await mf.dispose(); }
});
