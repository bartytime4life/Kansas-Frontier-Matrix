import assert from "node:assert/strict";
import test from "node:test";
import { readFile } from "node:fs/promises";
import { createRequire } from "node:module";
import ts from "typescript";

const nodeRequire = createRequire(import.meta.url);
async function load(path, imports = {}) {
  const source = await readFile(new URL(path, import.meta.url), "utf8");
  const code = ts.transpileModule(source, { compilerOptions: { target: ts.ScriptTarget.ES2022, module: ts.ModuleKind.CommonJS } }).outputText;
  const mod = { exports: {} };
  new Function("require", "module", "exports", code)((id) => imports[id] ?? nodeRequire(id), mod, mod.exports);
  return mod.exports;
}
const pricing = await load("../server/reports/pricing.ts");
const { ReportPurchaseService } = await load("../server/reports/purchases.ts", { "./pricing": pricing });

// This transactional reference store is a test fixture, never a runtime adapter.
function repository() {
  let state = { quotes: new Map(), orders: new Map(), roles: new Map(), payments: new Map() };
  let queue = Promise.resolve();
  const repo = { transaction(action) {
    const task = queue.then(async () => {
      const next = structuredClone(state);
      const tx = { getQuote: async (id) => next.quotes.get(id) ?? null, putQuote: async (q) => { next.quotes.set(q.id, q); },
        getOrder: async (id) => next.orders.get(id) ?? null, putOrder: async (o) => { next.orders.set(o.id, o); },
        staffAssignment: async (owner) => next.roles.get(owner) ?? null,
        claimPayment: async (provider, id, order) => { const key = provider + ":" + id; const prior = next.payments.get(key);
          if (prior && prior !== order) return false; next.payments.set(key, order); return true; } };
      const result = await action(tx); state = next; return structuredClone(result);
    });
    queue = task.catch(() => {}); return task;
  }, setRole: async (owner, assignment) => { await queue; state.roles.set(owner, assignment); },
  mutateOrder: async (id, fn) => repo.transaction(async (tx) => { const order = await tx.getOrder(id); fn(order); await tx.putOrder(order); }) };
  return repo;
}

function fixture() {
  let time = new Date("2026-10-13T12:00:00Z");
  const repo = repository(); const receipts = new Map();
  const counts = { checkouts: 0, renders: 0 };
  const policy = { schemaVersion: 1, version: "test-only-v1", currency: "USD", minimumMinor: 100, maximumMinor: 10000,
    laborRateMinorPerHour: 600, productBaseMinor: { brief: 100, standard: 200, technical: 300 },
    evidenceBaseMinor: { "source-context": 50, corroborated: 100, measured: 200 }, quoteTtlSeconds: 900 };
  const payment = { provider: "godaddy-payments", storeId: "fixture-store", checkoutHosts: ["checkout.example.test"],
    createCheckout: async (quote, reference) => { counts.checkouts++; const sessionId = "session-" + quote.id;
      receipts.set(sessionId, { status: "PENDING", transactionId: "transaction-" + quote.id, storeId: "fixture-store",
        reference, amountMinor: quote.amountMinor, currency: quote.currency, inputDigest: quote.inputDigest, sourceDigest: quote.sourceDigest });
      return { sessionId, url: "https://checkout.example.test/" + sessionId }; },
    verifyCheckout: async (id) => structuredClone(receipts.get(id)) };
  const assess = async (input) => ({ input, product: "standard", eligibility: "eligible", evidenceBand: "source-context",
    evidenceBasis: "Fixture source; no independently measured accuracy.", estimatedManualMinutes: 10,
    effortBasis: "Test-only documented retrieval and writing estimate.", limitations: ["Fixture only."],
    sources: [{ sourceId: "fixture-1", title: "Test source", digest: pricing.reportDigest({ value: 17, unit: "ft" }),
      officialUrl: "https://example.test/source", rights: "public", observationTime: "2026-10-12T12:00:00Z",
      retrievedAt: "2026-10-13T12:00:00Z", units: ["ft"], limitations: ["Fixture, not a live report."] }] });
  const deps = { repository: repo, payment, pricing: policy, assess, now: () => new Date(time),
    render: async (quote) => { counts.renders++; return { fileName: "report.md", contentType: "text/markdown",
      bytes: new TextEncoder().encode("# Test report\n17 ft\nFixture only."), inputDigest: quote.inputDigest,
      sourceDigest: quote.sourceDigest, assessmentDigest: quote.assessmentDigest }; } };
  const service = new ReportPurchaseService(deps);
  return { service, repo, counts, receipts, payment, deps, policy, advance: (ms) => { time = new Date(time.getTime() + ms); },
    capture: (order) => { receipts.get(order.checkout.sessionId).status = "CAPTURED"; } };
}
const rejectsCode = (promise, code) => assert.rejects(promise, (error) => error.code === code);
const input = { scope: "fixture-station", year: 2026 };

test("ordinary purchasers cannot render/download from client paid/role/amount assertions", async () => {
  const f = fixture(); const forged = { ...input, paid: true, role: "admin", amount: 0 };
  const quote = await f.service.quote("guest-1", forged);
  const order = await f.service.start(quote.id, "guest-1", forged);
  assert.equal(order.status, "AWAITING_PAYMENT"); assert.equal(order.entitlement, null);
  f.receipts.get(order.checkout.sessionId).transactionId = null;
  await rejectsCode(f.service.fulfill(order.id, "guest-1"), "REPORT_PAYMENT_REQUIRED");
  await rejectsCode(f.service.download(order.id, "guest-1"), "REPORT_PAYMENT_REQUIRED");
  assert.equal(f.counts.renders, 0);
});

test("only active authoritative steward/admin assignments grant exemptions; revocation removes access", async () => {
  for (const role of ["steward", "admin"]) {
    const f = fixture(); await f.repo.setRole("staff-1", { role, expiresAt: "2026-10-14T12:00:00Z", revoked: false });
    const quote = await f.service.quote("staff-1", input); const order = await f.service.start(quote.id, "staff-1", input);
    assert.equal(order.entitlement, "staff"); assert.equal(f.counts.checkouts, 0);
    assert.equal((await f.service.fulfill(order.id, "staff-1")).status, "READY");
    assert.ok((await f.service.download(order.id, "staff-1")).bytes.length);
    await f.repo.setRole("staff-1", { role, expiresAt: "2026-10-14T12:00:00Z", revoked: true });
    await rejectsCode(f.service.download(order.id, "staff-1"), "REPORT_STAFF_EXEMPTION_EXPIRED");
    await rejectsCode(f.service.start(quote.id, "staff-1", input), "REPORT_STAFF_EXEMPTION_EXPIRED");
  }
  const f = fixture(); await f.repo.setRole("expired", { role: "steward", expiresAt: "2026-10-13T11:00:00Z", revoked: false });
  const q = await f.service.quote("expired", input); assert.equal((await f.service.start(q.id, "expired", input)).entitlement, null);
});

test("repeated/concurrent start requests create one checkout for a quote", async () => {
  const f = fixture(); const quote = await f.service.quote("guest-1", input);
  const orders = await Promise.all(Array.from({ length: 12 }, () => f.service.start(quote.id, "guest-1", input)));
  assert.equal(f.counts.checkouts, 1); assert.equal(new Set(orders.map((order) => order.id)).size, 1);
});

test("uncertain provider creates cannot be blindly retried into duplicate orders", async () => {
  const f = fixture(); f.payment.createCheckout = async () => { f.counts.checkouts++; throw new Error("response lost"); };
  const quote = await f.service.quote("guest-1", input);
  assert.equal((await f.service.start(quote.id, "guest-1", input)).status, "CHECKOUT_UNCERTAIN");
  assert.equal((await f.service.start(quote.id, "guest-1", input)).status, "CHECKOUT_UNCERTAIN");
  assert.equal(f.counts.checkouts, 1);
});

test("verified capture permits one artifact and free repeat downloads after quote expiry", async () => {
  const f = fixture(); const quote = await f.service.quote("guest-1", input); const order = await f.service.start(quote.id, "guest-1", input);
  f.capture(order); assert.equal((await f.service.fulfill(order.id, "guest-1")).status, "READY");
  const first = await f.service.download(order.id, "guest-1"); f.advance(86400000); f.policy.productBaseMinor.standard = 9000;
  const second = await f.service.download(order.id, "guest-1");
  assert.deepEqual(second.bytes, first.bytes); assert.equal(first.digest, second.digest);
  assert.equal((await f.service.start(quote.id, "guest-1", input)).status, "READY");
  assert.deepEqual(Object.keys(await f.service.start(quote.id, "guest-1", input)).sort(), ["checkout", "entitlement", "id", "status"]);
  assert.equal(f.counts.checkouts, 1); assert.equal(f.counts.renders, 1);
});

test("another purchaser cannot inspect, start, verify, generate or download an order", async () => {
  const f = fixture(); const quote = await f.service.quote("guest-1", input); const order = await f.service.start(quote.id, "guest-1", input);
  for (const attempt of [f.service.start(quote.id, "other-guest", input), f.service.refreshPayment(order.id, "other-guest"),
    f.service.fulfill(order.id, "other-guest"), f.service.download(order.id, "other-guest")]) await rejectsCode(attempt, "REPORT_NOT_FOUND");
  assert.equal(f.counts.renders, 0);
});

test("wrong merchant, amount, currency, scope, source snapshot or reference cannot grant entitlement", async () => {
  for (const patch of [{ storeId: "other-store" }, { amountMinor: 1 }, { amountMinor: 350.1 }, { currency: "EUR" },
    { inputDigest: pricing.reportDigest("other scope") }, { sourceDigest: pricing.reportDigest("other data") }, { reference: "other-order" }]) {
    const f = fixture(); const q = await f.service.quote("guest-1", input); const o = await f.service.start(q.id, "guest-1", input); f.capture(o);
    Object.assign(f.receipts.get(o.checkout.sessionId), patch);
    await rejectsCode(f.service.fulfill(o.id, "guest-1"), "REPORT_PAYMENT_MISMATCH"); assert.equal(f.counts.renders, 0);
  }
});

test("one captured transaction cannot fulfill two purchases", async () => {
  const f = fixture(); const q1 = await f.service.quote("guest-1", input); const q2 = await f.service.quote("guest-1", { ...input, year: 2025 });
  const o1 = await f.service.start(q1.id, "guest-1", input); const o2 = await f.service.start(q2.id, "guest-1", q2.assessment.input);
  f.capture(o1); f.capture(o2); await f.service.fulfill(o1.id, "guest-1");
  f.receipts.get(o2.checkout.sessionId).transactionId = f.receipts.get(o1.checkout.sessionId).transactionId;
  await rejectsCode(f.service.fulfill(o2.id, "guest-1"), "REPORT_PAYMENT_ALREADY_USED");
});

test("concurrent fulfillment acquires one generation lease", async () => {
  const f = fixture(); const q = await f.service.quote("guest-1", input); const o = await f.service.start(q.id, "guest-1", input); f.capture(o);
  let release; const gate = new Promise((resolve) => { release = resolve; }); const original = f.deps.render;
  f.deps.render = async (quote) => { const artifact = await original(quote); await gate; return artifact; };
  const first = f.service.fulfill(o.id, "guest-1");
  while (f.counts.renders === 0) await new Promise(setImmediate);
  const concurrent = await Promise.all(Array.from({ length: 8 }, () => f.service.fulfill(o.id, "guest-1")));
  assert.ok(concurrent.every((order) => order.status === "GENERATING")); assert.equal(f.counts.renders, 1);
  release(); assert.equal((await first).status, "READY");
});

test("failed rendering can retry the same purchase without another checkout", async () => {
  const f = fixture(); const q = await f.service.quote("guest-1", input); const o = await f.service.start(q.id, "guest-1", input); f.capture(o);
  const original = f.deps.render; let fail = true;
  f.deps.render = async (quote) => { if (fail) throw new Error("temporary renderer failure"); return original(quote); };
  assert.equal((await f.service.fulfill(o.id, "guest-1")).status, "FAILED");
  await rejectsCode(f.service.download(o.id, "guest-1"), "REPORT_NOT_READY");
  fail = false; assert.equal((await f.service.fulfill(o.id, "guest-1")).status, "READY"); assert.equal(f.counts.checkouts, 1);
});

test("refund during generation cannot publish an artifact; delayed capture cannot reverse refund", async () => {
  const f = fixture(); const q = await f.service.quote("guest-1", input); const o = await f.service.start(q.id, "guest-1", input); f.capture(o);
  let release; const gate = new Promise((resolve) => { release = resolve; }); const original = f.deps.render;
  f.deps.render = async (quote) => { const artifact = await original(quote); await gate; return artifact; };
  const work = f.service.fulfill(o.id, "guest-1"); while (f.counts.renders === 0) await new Promise(setImmediate);
  f.receipts.get(o.checkout.sessionId).status = "REFUNDED"; await f.service.refreshPayment(o.id, "guest-1");
  release(); assert.equal((await work).status, "REFUNDED");
  f.capture(o); await rejectsCode(f.service.download(o.id, "guest-1"), "REPORT_PAYMENT_REQUIRED");
});

test("unsafe checkout redirects, replaced source artifacts and corrupted bytes stay unavailable", async () => {
  const invalidCheckout = fixture(); invalidCheckout.payment.createCheckout = async () => ({ sessionId: "fixture-session", url: "https://attacker.example/collect" });
  const q = await invalidCheckout.service.quote("guest-1", input); assert.equal((await invalidCheckout.service.start(q.id, "guest-1", input)).status, "CHECKOUT_UNCERTAIN");
  const f = fixture(); const quote = await f.service.quote("guest-1", input); const order = await f.service.start(quote.id, "guest-1", input); f.capture(order);
  const original = f.deps.render; f.deps.render = async (q) => ({ ...await original(q), sourceDigest: pricing.reportDigest("replacement") });
  assert.equal((await f.service.fulfill(order.id, "guest-1")).status, "FAILED");
  await rejectsCode(f.service.download(order.id, "guest-1"), "REPORT_NOT_READY");
  f.deps.render = original; await f.service.fulfill(order.id, "guest-1");
  await f.repo.mutateOrder(order.id, (order) => { order.artifact.bytes[0] ^= 1; });
  await rejectsCode(f.service.download(order.id, "guest-1"), "REPORT_ARTIFACT_CORRUPT");
});

test("checkout/status responses exclude provider secrets and private report bytes", async () => {
  const f = fixture(); const original = f.payment.createCheckout;
  f.payment.createCheckout = async (...args) => ({ ...await original(...args), providerToken: "fixture-secret-not-for-browser" });
  const q = await f.service.quote("guest-1", input); const order = await f.service.start(q.id, "guest-1", input);
  assert.equal(JSON.stringify(order).includes("fixture-secret"), false);
  f.capture(order); const ready = await f.service.fulfill(order.id, "guest-1");
  assert.deepEqual(Object.keys(ready).sort(), ["checkout", "entitlement", "id", "status"]);
  assert.equal(ready.checkout, null);
  assert.equal(JSON.stringify(await f.service.refreshPayment(order.id, "guest-1")).includes("17 ft"), false);
});
