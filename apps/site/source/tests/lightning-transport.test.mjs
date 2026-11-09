import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

async function compile(name, imports = {}) {
  const source = await readFile(new URL(`../app/${name}.ts`, import.meta.url), "utf8");
  const output = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 } }).outputText;
  const mod = { exports: {} };
  new Function("require", "module", "exports", output)(name => imports[name], mod, mod.exports);
  return mod.exports;
}
const { fetchLightningPng } = await compile("lightning-server", {
  "./bounded-json": await compile("bounded-json"), "./lightning-data": await compile("lightning-data"),
});
const url = "https://nowcoast.noaa.gov/geoserver/observations/lightning_detection/ows?fixture=1";
const limit = 1024 * 1024;
const png = size => { const bytes = new Uint8Array(size); bytes.set([137, 80, 78, 71, 13, 10, 26, 10]); return bytes; };

test("streamed lightning images stop at the actual byte limit without waiting for cancellation", { timeout: 1000 }, async t => {
  let response;
  t.mock.method(globalThis, "fetch", async () => response);
  for (const contentLength of [undefined, "1"]) {
    let pulls = 0, canceled = false;
    response = new Response(new ReadableStream({
      pull(controller) { if (pulls++ === 10) controller.close(); else controller.enqueue(png(limit / 4)); },
      cancel() { canceled = true; return new Promise(() => {}); },
    }, { highWaterMark: 0 }), { headers: { "Content-Type": "image/png", ...(contentLength ? { "Content-Length": contentLength } : {}) } });
    await assert.rejects(fetchLightningPng(url), /limit|bounded PNG/);
    assert.equal(canceled, true);
    assert.equal(pulls, 5, "the remaining provider body is never read after the first over-budget chunk");
    assert.equal(response.body.locked, false);
  }
});

test("declared oversized lightning images cancel their body before a read", { timeout: 1000 }, async t => {
  let pulls = 0, canceled = false;
  const response = new Response(new ReadableStream({
    pull() { pulls++; }, cancel() { canceled = true; return new Promise(() => {}); },
  }, { highWaterMark: 0 }), { headers: { "Content-Type": "image/png", "Content-Length": String(limit + 1) } });
  t.mock.method(globalThis, "fetch", async () => response);
  await assert.rejects(fetchLightningPng(url), /exceeds the limit/);
  assert.equal(pulls, 0); assert.equal(canceled, true); assert.equal(response.body.locked, false);
});

test("lightning transport retains redirect, status and content-type checks and cancels rejected bodies", async t => {
  const calls = []; let response;
  t.mock.method(globalThis, "fetch", async (input, options) => { calls.push({ input, options }); return response; });
  for (const init of [
    { status: 302, headers: { Location: "http://127.0.0.1/private", "Content-Type": "image/png" } },
    { status: 503, headers: { "Content-Type": "image/png" } },
    { headers: { "Content-Type": "text/html" } },
  ]) {
    let canceled = false;
    response = new Response(new ReadableStream({ cancel() { canceled = true; } }), init);
    await assert.rejects(fetchLightningPng(url), /NOAA lightning image HTTP/);
    assert.equal(canceled, true); assert.equal(response.body.locked, false);
  }
  assert.equal(calls.length, 3, "no redirect target is fetched");
  for (const { input, options } of calls) {
    assert.equal(input, url); assert.equal(options.redirect, "manual"); assert.equal(options.cache, "no-store");
    assert.equal(options.headers.Accept, "image/png"); assert.match(options.headers["User-Agent"], /KansasFrontierMatrixExplorer/);
  }
});

test("lightning images preserve valid bytes at the cap and still reject malformed or short PNGs", async t => {
  let response;
  t.mock.method(globalThis, "fetch", async () => response);
  for (const size of [64, limit]) {
    const bytes = png(size);
    response = new Response(bytes, { headers: { "Content-Type": "image/png" } });
    assert.deepEqual(await fetchLightningPng(url), bytes);
    assert.equal(response.body.locked, false);
  }
  for (const bytes of [png(63), new Uint8Array(64)]) {
    response = new Response(bytes, { headers: { "Content-Type": "image/png" } });
    await assert.rejects(fetchLightningPng(url), /not a bounded PNG/);
    assert.equal(response.body.locked, false);
  }
});

test("lightning timeouts and caller aborts cancel a stalled partial body and release its lock", { timeout: 1000 }, async t => {
  for (const mode of ["timeout", "caller"]) {
    let expire, cleared = false, reading, cancelReason;
    const started = new Promise(resolve => { reading = resolve; });
    const controller = new AbortController();
    const reason = new DOMException("Viewer closed the preview.", "AbortError");
    let pulls = 0;
    const response = new Response(new ReadableStream({
      pull(stream) { if (pulls++ === 0) stream.enqueue(png(64)); else reading(); },
      cancel(value) { cancelReason = value; return new Promise(() => {}); },
    }, { highWaterMark: 0 }), { headers: { "Content-Type": "image/png" } });
    const fetchMock = t.mock.method(globalThis, "fetch", async () => response);
    const timerMock = t.mock.method(globalThis, "setTimeout", (callback, delay) => { assert.equal(delay, 15_000); expire = callback; return 1; });
    const clearMock = t.mock.method(globalThis, "clearTimeout", () => { cleared = true; });
    try {
      const pending = fetchLightningPng(url, controller.signal);
      await started; assert.equal(response.body.locked, true);
      if (mode === "timeout") expire(); else controller.abort(reason);
      await assert.rejects(pending, error => mode === "caller" ? error === reason : error.name === "TimeoutError");
      assert.equal(cancelReason.name, mode === "caller" ? "AbortError" : "TimeoutError");
      assert.equal(response.body.locked, false); assert.equal(cleared, true);
    } finally { fetchMock.mock.restore(); timerMock.mock.restore(); clearMock.mock.restore(); }
  }
});

test("lightning transport releases an errored reader and never starts a canceled request", async t => {
  let calls = 0;
  const response = new Response(new ReadableStream({ pull(controller) { controller.error(new Error("Broken image stream")); } }), { headers: { "Content-Type": "image/png" } });
  t.mock.method(globalThis, "fetch", async () => { calls++; return response; });
  await assert.rejects(fetchLightningPng(url), /Broken image stream/);
  assert.equal(response.body.locked, false);
  const controller = new AbortController(); controller.abort();
  await assert.rejects(fetchLightningPng(url, controller.signal), { name: "AbortError" });
  assert.equal(calls, 1);
});
