import assert from "node:assert/strict";
import test from "node:test";
import { compile, deferred, feature, installProvider, loadRoute, request, tick } from "./flowline-request-harness.mjs";

const { createFlowlineRequestPool, FLOWLINE_REQUEST_LIMITS: limits } = await import(await compile("app/flowline-request-pool.ts"));
const signal = () => new AbortController().signal;

test("24 duplicate clients share one validated read, cache bytes and original retrieval time", async t => {
  const GET = await loadRoute(), gate = deferred();
  const reads = installProvider(t, async () => { await gate.promise; return Response.json({ features: [feature], exceededTransferLimit: true }); });
  const clients = Array.from({ length: 24 }, (_, i) => GET(request(i % 2 ? "cell=-97.25,38&detail=local" : undefined)));
  await tick(); assert.equal(reads.length, 1);
  gate.resolve();
  const responses = await Promise.all(clients);
  assert.ok(responses.every(r => r.status === 200));
  const bodies = await Promise.all(responses.map(r => r.text()));
  assert.equal(new Set(bodies).size, 1);
  const payload = JSON.parse(bodies[0]);
  assert.equal(payload.source, "https://3dhp.nationalmap.gov/arcgis/rest/services/usgs_3dhp_all/MapServer/50/query");
  assert.equal(payload.evidenceRole, "EXTERNAL_CONTEXT_ONLY");
  assert.equal(payload.truncated, true); assert.deepEqual(payload.reaches[0].coordinates, feature.geometry.coordinates);
  assert.match(payload.limitation, /Stream order is not discharge/);
  const cached = await GET(request()); assert.equal(await cached.text(), bodies[0]); assert.equal(reads.length, 1);
  assert.match(cached.headers.get("cache-control"), /^private, max-age=\d+$/);
  assert.equal(reads[0].redirect, "manual"); assert.equal(reads[0].cache, "no-store");
});

test("24 different cells admit nine reads with no hidden queue and recover when drained", async t => {
  const GET = await loadRoute(), gate = deferred();
  const reads = installProvider(t, async () => { await gate.promise; return Response.json({ features: [] }); });
  const clients = Array.from({ length: 24 }, (_, i) => GET(request("cell=" + [-101 + (i % 12) * .25, 37 + Math.floor(i / 12) * .25].join(","))));
  await tick(); assert.equal(reads.length, limits.active);
  gate.resolve(); const responses = await Promise.all(clients);
  assert.equal(responses.filter(r => r.status === 200).length, 9);
  assert.equal(responses.filter(r => r.status === 503).length, 15);
  for (const response of responses.filter(r => r.status === 503)) {
    assert.equal(response.headers.get("retry-after"), "1"); assert.equal(response.headers.get("cache-control"), "no-store");
  }
  await tick(); assert.equal((await GET(request("cell=-97.25,38.00"))).status, 200); assert.equal(reads.length, 10);
});

test("detail separates cache identity; invalid queries cannot use a cached success", async t => {
  const GET = await loadRoute();
  const reads = installProvider(t, async () => Response.json({ features: [] }));
  assert.equal((await GET(request("cell=-98.25,36.75&detail=overview"))).status, 200);
  assert.equal((await GET(request("cell=-98.25,36.75&detail=local"))).status, 200);
  assert.equal(reads.length, 2);
  for (const query of ["cell=-98.25,36.75&detail=overview&url=https://evil.invalid", "cell=-98.25,36.75&cell=-98.25,36.75", "cell=-98.25,36.75&detail=unknown"]) assert.equal((await GET(request(query))).status, 400);
  assert.equal(reads.length, 2);
});

test("provider failures and malformed/oversized responses coalesce without becoming successes", async t => {
  let mode;
  const reads = installProvider(t, async () => mode());
  for (const response of [
    () => new Response("down", { status: 502 }),
    () => new Response(null, { status: 302, headers: { Location: "https://evil.invalid" } }),
    () => new Response("not-json"),
    () => Response.json({ error: { message: "provider error" } }),
    () => new Response("{}", { headers: { "content-length": String(6 * 1024 * 1024 + 1) } }),
    () => new Response(new ReadableStream({ start(c) { c.enqueue(new Uint8Array(6 * 1024 * 1024 + 1)); c.close(); } })),
    () => Response.json({ features: [feature, feature] }),
    () => { throw new Error("network failure"); },
  ]) {
    mode = response; const GET = await loadRoute(), before = reads.length;
    const responses = await Promise.all(Array.from({ length: 24 }, () => GET(request())));
    assert.ok(responses.every(r => r.status === 503)); assert.equal(reads.length - before, 1);
    assert.equal((await GET(request())).status, 503); assert.equal(reads.length - before, 1, "short failure cooldown");
  }
});

test("one cancellation leaves the shared read alive; all cancellations abort it and allow recovery", async t => {
  const GET = await loadRoute(), gate = deferred();
  const reads = installProvider(t, async (_url, { signal }) => {
    await Promise.race([gate.promise, new Promise((_, reject) => signal.addEventListener("abort", () => reject(new Error("aborted")), { once: true }))]);
    return Response.json({ features: [feature] });
  });
  const a = new AbortController(), b = new AbortController();
  const first = GET(request(undefined, a.signal)), second = GET(request(undefined, b.signal));
  await tick(); a.abort(); assert.equal((await first).status, 503); assert.equal(reads[0].signal.aborted, false);
  b.abort(); assert.equal((await second).status, 503); assert.equal(reads[0].signal.aborted, true);
  await tick(); gate.resolve(); assert.equal((await GET(request())).status, 200); assert.equal(reads.length, 2);
  const already = new AbortController(); already.abort(); assert.equal((await GET(request(undefined, already.signal))).status, 503); assert.equal(reads.length, 2);
});

test("a departing first subscriber does not poison the survivor or its cached result", async t => {
  const GET = await loadRoute(), gate = deferred();
  const reads = installProvider(t, async () => { await gate.promise; return Response.json({ features: [feature] }); });
  const a = new AbortController(), first = GET(request(undefined, a.signal)), survivor = GET(request());
  await tick(); a.abort(); await first; gate.resolve(); assert.equal((await survivor).status, 200);
  assert.equal((await GET(request())).status, 200); assert.equal(reads.length, 1);
});

test("rejected upstream bodies are cancelled before reads release their slots", async t => {
  const GET = await loadRoute(), cancellation = deferred(); let cancelled = 0;
  const reads = installProvider(t, async () => new Response(new ReadableStream({ cancel() { cancelled++; return cancellation.promise; } }), { status: 503 }));
  const pending = Array.from({ length: 9 }, (_, i) => GET(request("cell=" + [-101 + i * .25, 37].join(","))));
  await tick(); assert.equal(reads.length, 9); assert.equal(cancelled, 9);
  assert.equal((await GET(request())).status, 503); assert.equal(reads.length, 9, "pending body cleanup still occupies all slots");
  cancellation.resolve(); assert.ok((await Promise.all(pending)).every(r => r.status === 503));
  await tick(); await GET(request()); assert.equal(reads.length, 10);
});

test("cancellation churn releases admission while a surviving subscriber still shares one read", async () => {
  const pool = createFlowlineRequestPool({ waiters: 2 }), gate = deferred(); let calls = 0;
  const load = async () => { calls++; await gate.promise; return "ok"; };
  const survivor = pool.get("a", signal(), load);
  for (let i = 0; i < 2000; i++) {
    const controller = new AbortController(), pending = pool.get("a", controller.signal, load);
    controller.abort(); assert.equal((await pending).state, "cancelled");
  }
  assert.equal(calls, 1); gate.resolve(); assert.equal((await survivor).state, "ready");
});

test("route deadline aborts a stalled body and returns no-store; a fresh instance can recover", async t => {
  const GET = await loadRoute(); let cancelled = false, mode = "stall";
  const reads = installProvider(t, async () => mode === "stall" ? new Response(new ReadableStream({ cancel() { cancelled = true; } })) : Response.json({ features: [] }));
  t.mock.timers.enable({ apis: ["setTimeout"] });
  const clients = Array.from({ length: 24 }, () => GET(request())); await tick();
  t.mock.timers.tick(30_000);
  const responses = await Promise.all(clients); assert.ok(responses.every(r => r.status === 503)); assert.equal(cancelled, true); assert.equal(reads.length, 1);
  assert.equal(responses[0].headers.get("cache-control"), "no-store");
  // Date-based failure expiry is verified below with a deterministic clock.
  mode = "ready"; const coldGET = await loadRoute(); assert.equal((await coldGET(request())).status, 200);
});

test("failure TTL expires and success TTL never slides; empty results are reusable", async () => {
  let now = 100, calls = 0, fail = true;
  const pool = createFlowlineRequestPool({ now: () => now, failureMs: 10, freshMs: 100 });
  const get = () => pool.get("a", signal(), async () => { calls++; if (fail) throw new Error("failure"); return "empty validated payload"; });
  assert.equal((await get()).state, "unavailable"); await tick();
  now = 109; fail = false; assert.equal((await get()).state, "unavailable"); assert.equal(calls, 1);
  now = 110; const first = await get(); assert.equal(first.state, "ready"); assert.equal(calls, 2); await tick();
  now = 209; assert.deepEqual(await get(), first); assert.equal(calls, 2);
  now = 210; assert.equal((await get()).state, "ready"); assert.equal(calls, 3);
});

test("waiter admission is bounded for duplicate and distinct requests", async () => {
  const pool = createFlowlineRequestPool({ active: 2, waiters: 3 }), gate = deferred(); let calls = 0;
  const load = async () => { calls++; await gate.promise; return "ok"; };
  const pending = [pool.get("a", signal(), load), pool.get("a", signal(), load), pool.get("b", signal(), load)];
  assert.equal((await pool.get("a", signal(), load)).state, "overloaded");
  assert.equal((await pool.get("c", signal(), load)).state, "overloaded");
  await tick(); assert.equal(calls, 2); gate.resolve(); assert.ok((await Promise.all(pending)).every(r => r.state === "ready"));
});

test("cache enforces entry count, UTF-8 bytes and per-entry budget with LRU eviction", async () => {
  const pool = createFlowlineRequestPool({ cacheEntries: 2, cacheBytes: 8, entryBytes: 4 }); let calls = 0;
  const get = async (key, value = "éé") => { const result = await pool.get(key, signal(), async () => { calls++; return value; }); await tick(); return result; };
  await get("a"); await get("b"); await get("a"); assert.equal(calls, 2);
  await get("c"); await get("a"); assert.equal(calls, 3); await get("b"); assert.equal(calls, 4, "least-recent b was evicted");
  await get("large", "12345"); await get("large", "12345"); assert.equal(calls, 6, "over-budget results are served but never retained");
  const bytes = createFlowlineRequestPool({ cacheEntries: 9, cacheBytes: 5, entryBytes: 4 }); let byteCalls = 0;
  for (const key of ["a", "b", "a"]) { await bytes.get(key, signal(), async () => { byteCalls++; return "éé"; }); await tick(); }
  assert.equal(byteCalls, 3, "UTF-8 byte bound evicts even below entry-count bound");
});

test("non-cooperative cancellation and timeout retain slots until the actual read settles", async t => {
  t.mock.timers.enable({ apis: ["setTimeout"] });
  for (const reason of ["cancel", "timeout"]) {
    let calls = 0, now = 0; const gate = deferred(), a = new AbortController();
    const pool = createFlowlineRequestPool({ active: 1, timeoutMs: 20, failureMs: 1, now: () => now });
    const load = async () => { calls++; await gate.promise; return "late"; };
    const pending = pool.get("a", a.signal, load); await tick();
    if (reason === "cancel") a.abort(); else t.mock.timers.tick(20);
    assert.equal((await pending).state, reason === "cancel" ? "cancelled" : "unavailable");
    now = 2; assert.equal((await pool.get("b", signal(), load)).state, "overloaded"); assert.equal(calls, 1);
    assert.equal((await pool.get("a", signal(), load)).state, "overloaded");
    gate.resolve(); await tick(); assert.equal((await pool.get("b", signal(), async () => { calls++; return "new"; })).state, "ready"); assert.equal(calls, 2);
    await tick(); assert.equal((await pool.get("a", signal(), async () => "fresh")).body, "fresh", "late aborted success is not cached");
  }
});
