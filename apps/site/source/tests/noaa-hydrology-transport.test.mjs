import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const compile = source => ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 } }).outputText;
const bounded = { exports: {} };
new Function("module", "exports", compile(await readFile("app/bounded-json.ts", "utf8")))(bounded, bounded.exports);
const source = compile(await readFile("app/api/hydrology/noaa/route.ts", "utf8"));
function route(fetcher, timers = { setTimeout, clearTimeout }) {
  const mod = { exports: {} };
  new Function("require", "module", "exports", "fetch", "setTimeout", "clearTimeout", source)(name => {
    if (name === "next/server") return { NextResponse: Response };
    if (name === "../../../bounded-json") return bounded.exports;
    throw new Error(`Unexpected NOAA fixture import: ${name}`);
  }, mod, mod.exports, fetcher, timers.setTimeout, timers.clearTimeout);
  return () => mod.exports.GET({ nextUrl: new URL("https://site.test/api/hydrology/noaa?mode=network") });
}
const limit = 1024 * 1024;
const bytes = text => new TextEncoder().encode(text);

test("NOAA header and schema failures retain their public errors and cancel rejected bodies", { timeout: 1000 }, async () => {
  for (const [init, code] of [
    [{ status: 302, headers: { Location: "http://127.0.0.1/private" } }, "NOAA_UPSTREAM_STATUS"],
    [{ status: 503 }, "NOAA_UPSTREAM_STATUS"],
    [{ headers: { "Content-Type": "text/html" } }, "NOAA_MEDIA_TYPE"],
    [{ headers: { "Content-Type": "application/json", "Content-Length": String(limit + 1) } }, "NOAA_RESPONSE_TOO_LARGE"],
  ]) {
    let pulls = 0, canceled = 0, calls = 0;
    const upstream = new Response(new ReadableStream({ pull() { pulls++; }, cancel() { canceled++; return new Promise(() => {}); } }, { highWaterMark: 0 }), init);
    const GET = route(async (input, options) => {
      calls++; assert.equal(new URL(input).origin, "https://api.water.noaa.gov");
      assert.equal(options.redirect, "manual"); assert.equal(options.cache, "no-store");
      assert.equal(options.headers.Accept, "application/json"); assert.match(options.headers["User-Agent"], /KansasFrontierMatrixExplorer/);
      return upstream;
    });
    const response = await GET(), body = await response.json();
    assert.equal(response.status, 502); assert.equal(body.error.code, code); assert.equal(body.state, "error");
    assert.deepEqual(body.records, []); assert.equal(response.headers.get("cache-control"), "no-store");
    assert.equal(calls, 1); assert.equal(pulls, 0); assert.equal(canceled, 1); assert.equal(upstream.body.locked, false);
  }
  for (const [payload, code] of [[null, "NOAA_EMPTY_RESPONSE"], ["{", "NOAA_INVALID_JSON"], ["[]", "NOAA_CONTRACT_MISMATCH"], ["{}", "NOAA_CONTRACT_MISMATCH"]]) {
    const upstream = new Response(payload, { headers: { "Content-Type": "application/json" } });
    const response = await route(async () => upstream)();
    assert.equal(response.status, 502); assert.equal((await response.json()).error.code, code);
    assert.equal(upstream.body?.locked ?? false, false);
  }
});

test("NOAA actual-byte caps stop chunked responses without waiting for provider cancellation", { timeout: 1000 }, async () => {
  for (const declared of [undefined, "1", "not-a-number"]) {
    let pulls = 0, canceled = 0;
    const upstream = new Response(new ReadableStream({
      pull(controller) { pulls++; controller.enqueue(new Uint8Array(limit / 4)); },
      cancel() { canceled++; return new Promise(() => {}); },
    }, { highWaterMark: 0 }), { headers: { "Content-Type": "application/json", ...(declared ? { "Content-Length": declared } : {}) } });
    const response = await route(async () => upstream)();
    assert.equal(response.status, 502); assert.equal((await response.json()).error.code, "NOAA_RESPONSE_TOO_LARGE");
    assert.equal(pulls, 5); assert.equal(canceled, 1); assert.equal(upstream.body.locked, false);
  }
});

test("NOAA exact-cap responses release readers and retain the existing nonfatal UTF-8 policy", async () => {
  const prefix = '{"gauges":[],"padding":"', suffix = '"}';
  const exact = bytes(prefix + " ".repeat(limit - prefix.length - suffix.length) + suffix);
  const replacement = new Uint8Array([...bytes('{"gauges":[],"note":"'), 255, ...bytes('"}')]);
  for (const payload of [exact, replacement]) {
    const upstream = new Response(payload, { headers: { "Content-Type": "application/json", "Content-Length": String(payload.length) } });
    const response = await route(async () => upstream)(), body = await response.json();
    assert.equal(response.status, 200); assert.equal(body.state, "empty"); assert.deepEqual(body.records, []);
    assert.equal(body.partial, false); assert.equal(body.truncated, false);
    assert.equal(response.headers.get("cache-control"), "public, max-age=120"); assert.equal(upstream.body.locked, false);
    assert.equal(body.sourceLinks[0].href.startsWith("https://api.water.noaa.gov/nwps/v1/gauges?"), true);
  }
});

test("NOAA deadlines cancel stalled bodies after headers and map to the existing timeout response", { timeout: 1000 }, async () => {
  let expire, cleared = 0, started, signal, canceled;
  const reading = new Promise(resolve => { started = resolve; });
  let pulls = 0;
  const upstream = new Response(new ReadableStream({
    pull(controller) { if (pulls++ === 0) controller.enqueue(bytes('{"gauges":[')); else started(); },
    cancel(reason) { canceled = reason; return new Promise(() => {}); },
  }, { highWaterMark: 0 }), { headers: { "Content-Type": "application/json" } });
  const GET = route(async (_input, options) => { signal = options.signal; return upstream; }, {
    setTimeout(callback, delay) { assert.equal(delay, 15_000); expire = callback; return 1; },
    clearTimeout() { cleared++; },
  });
  const pending = GET(); await reading; expire();
  const response = await pending, body = await response.json();
  assert.equal(signal.aborted, true); assert.equal(response.status, 504); assert.equal(body.error.code, "NOAA_TIMEOUT");
  assert.equal(body.state, "error"); assert.deepEqual(body.records, []);
  assert.equal(canceled.name, "AbortError"); assert.equal(upstream.body.locked, false); assert.equal(cleared, 1);
});

test("NOAA broken streams remain unavailable and release their reader", async () => {
  const upstream = new Response(new ReadableStream({ pull(controller) { controller.error(new Error("PRIVATE_PROVIDER_ERROR")); } }, { highWaterMark: 0 }), { headers: { "Content-Type": "application/json" } });
  const response = await route(async () => upstream)(), body = await response.json();
  assert.equal(response.status, 502); assert.equal(body.error.code, "NOAA_UNAVAILABLE");
  assert.doesNotMatch(JSON.stringify(body), /PRIVATE_PROVIDER_ERROR/); assert.equal(upstream.body.locked, false);
});
