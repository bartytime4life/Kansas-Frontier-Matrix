import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";
import ts from "typescript";
import { settle } from "./component-harness.mjs";

const compile = (source, module = ts.ModuleKind.CommonJS) => ts.transpileModule(source, {
  compilerOptions: { module, target: ts.ScriptTarget.ES2022 },
}).outputText;
const bounded = await import(`data:text/javascript;base64,${Buffer.from(compile(
  await readFile("app/bounded-json.ts", "utf8"), ts.ModuleKind.ESNext,
)).toString("base64")}`);
const code = compile(await readFile("app/api/live-context/route.ts", "utf8"));

function setup(fetch) {
  const timers = new Map();
  const exports = {};
  vm.runInNewContext(code, {
    exports, Error, Date, URL, Response, AbortController,
    fetch,
    setTimeout: (callback, milliseconds) => { const id = {}; timers.set(id, { callback, milliseconds }); return id; },
    clearTimeout: id => timers.delete(id),
    require(name) {
      if (name === "../../bounded-json") return bounded;
      if (name === "next/server") return { NextResponse: Response };
      if (name === "./kdot-bridges") return { isBridgeFeed: () => false };
      return {};
    },
  });
  const request = () => exports.GET({
    nextUrl: new URL("https://fixture.test/api/live-context?feed=usgs-earthquakes"),
    signal: new AbortController().signal,
  });
  const expire = () => {
    assert.equal(timers.size, 1);
    const { callback, milliseconds } = timers.values().next().value;
    assert.equal(milliseconds, 15_000); callback();
  };
  return { request, expire, timers };
}

test("a stalled live-context body times out, cancels its stream and returns an uncached timeout response", async () => {
  let stream, cancelled = 0, settled = false, signal;
  const response = new Response(new ReadableStream({
    start(controller) { stream = controller; controller.enqueue(new TextEncoder().encode('{"type":"FeatureCollection",')); },
    cancel() { cancelled++; },
  }));
  const h = setup(async (_url, options) => { signal = options.signal; return response; });
  const pending = h.request().then(value => { settled = true; return value; });
  try {
    await settle(); h.expire(); await settle();
    assert.equal(signal.aborted, true);
    assert.equal(settled, true, "the deadline must cover response-body reads");
    const result = await pending;
    assert.equal(result.status, 503);
    assert.equal(result.headers.get("x-kfm-upstream-failure"), "timeout"); assert.equal(result.headers.get("cache-control"), "no-store");
    assert.equal(result.headers.get("x-kfm-context-state"), "error");
    const body = await result.json();
    assert.equal(body.state, "error"); assert.match(body.error, /timed out/); assert.equal("data" in body, false);
    assert.equal(cancelled, 1); assert.equal(h.timers.size, 0);
  } finally {
    if (!settled) { stream.error(new Error("test cleanup")); await pending; }
  }
});

test("a late response after the deadline cannot be published as an empty ready catalog", async () => {
  let resolve, signal;
  const delayed = new Promise(done => { resolve = done; });
  const h = setup((_url, options) => { signal = options.signal; return delayed; });
  const pending = h.request();
  await settle(); h.expire();
  assert.equal(signal.aborted, true);
  resolve(Response.json({ type: "FeatureCollection", features: [] }));
  const response = await pending;
  assert.equal(response.status, 503);
  assert.equal(response.headers.get("x-kfm-upstream-failure"), "timeout"); assert.equal((await response.json()).state, "error");
  assert.equal(h.timers.size, 0);
});

test("failed upstream HTTP responses cancel their bodies before returning a safe source error", async () => {
  let cancelled = 0;
  const h = setup(async () => new Response(new ReadableStream({ cancel() { cancelled++; } }), { status: 503 }));
  const response = await h.request();
  assert.equal(response.status, 503);
  assert.equal(response.headers.get("x-kfm-upstream-failure"), "error"); assert.equal(cancelled, 1);
  assert.equal(h.timers.size, 0);
  assert.match((await response.json()).error, /HTTP 503/);
});


test("a complete response keeps the existing healthy catalog and clears its deadline", async () => {
  let signal;
  const h = setup(async (_url, options) => {
    signal = options.signal;
    return Response.json({ type: "FeatureCollection", features: [], metadata: { count: 0 } });
  });
  const response = await h.request();
  assert.equal(response.status, 200);
  assert.equal(response.headers.get("x-kfm-context-state"), "empty");
  assert.equal((await response.json()).featureCount, 0);
  assert.equal(signal.aborted, false);
  assert.equal(h.timers.size, 0);
});
