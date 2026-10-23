import test from "node:test";
import assert from "node:assert/strict";
import { request as httpRequest } from "node:http";
import { deferred } from "./flowline-request-harness.mjs";

// Real built Vinext HTTP dispatch, with USGS fetch replaced inside this process.
// Ephemeral loopback only, no provider traffic or externally selected origin.
test("built flowline HTTP route coalesces 24 clients and bounds different-cell admission", { timeout: 20_000 }, async t => {
  const original = globalThis.fetch, previousEnv = process.env.NODE_ENV;
  let gate = deferred(), started = deferred(), calls = 0, active = 0, peak = 0;
  let managedServer;
  t.after(async () => {
    try {
      gate.resolve();
      if (managedServer) { managedServer.closeAllConnections(); await new Promise(resolve => managedServer.close(resolve)); }
    } finally {
      globalThis.fetch = original;
      if (previousEnv === undefined) delete process.env.NODE_ENV; else process.env.NODE_ENV = previousEnv;
    }
  });
  globalThis.fetch = async (input, options) => {
    assert.equal(new URL(input).hostname, "3dhp.nationalmap.gov", "unexpected outbound request denied");
    calls++; active++; peak = Math.max(peak, active);
    started.resolve();
    try { await gate.promise; options.signal.throwIfAborted(); return Response.json({ features: [] }); }
    finally { active--; }
  };
  process.env.NODE_ENV = "production";
  const { startProdServer } = await import("vinext/server/prod-server");
  const { server, port } = await startProdServer({ port: 0, host: "127.0.0.1" });
  managedServer = server;
  const get = query => new Promise((resolve, reject) => {
    const req = httpRequest({ hostname: "127.0.0.1", port, path: "/api/hydrology/flowlines?" + query }, response => {
      const chunks = []; response.on("data", c => chunks.push(c));
      response.on("error", reject); response.on("end", () => resolve({ status: response.statusCode, headers: response.headers, body: Buffer.concat(chunks).toString() }));
    });
    req.setTimeout(10_000, () => req.destroy(new Error("loopback deadline"))); req.on("error", reject); req.end();
  });
  // Wait for all 24 native HTTP clients to be dispatched, not a timed throughput assertion.
  let arrivals = 0, arrived = deferred();
  server.on("request", () => { if (++arrivals === 24) arrived.resolve(); });
  const duplicates = Array.from({ length: 24 }, () => get("cell=-97.25,38.00"));
  await Promise.all([arrived.promise, started.promise]);
  assert.equal(calls, 1); gate.resolve(); const responses = await Promise.all(duplicates);
  assert.ok(responses.every(r => r.status === 200)); assert.equal(new Set(responses.map(r => r.body)).size, 1);
  await Promise.all(Array.from({ length: 24 }, () => get("cell=-97.25,38.00"))); assert.equal(calls, 1);
  gate = deferred(); arrivals = 0; arrived = deferred();
  const overloaded = deferred(); let rejected = 0;
  const unique = Array.from({ length: 24 }, (_, i) => get("cell=" + [-101 + (i % 12) * .25, 37 + Math.floor(i / 12) * .25].join(",")).then(result => {
    if (result.status === 503 && ++rejected === 15) overloaded.resolve(); return result;
  }));
  await Promise.all([arrived.promise, overloaded.promise]);
  assert.equal(calls, 10); assert.equal(peak, 9); gate.resolve();
  const distinct = await Promise.all(unique); assert.equal(distinct.filter(r => r.status === 200).length, 9); assert.equal(distinct.filter(r => r.status === 503).length, 15);
  assert.ok(distinct.filter(r => r.status === 503).every(r => r.headers["cache-control"] === "no-store" && r.headers["retry-after"] === "1"));
});
