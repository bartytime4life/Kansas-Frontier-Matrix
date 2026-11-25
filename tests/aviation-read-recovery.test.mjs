import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";
import { settle } from "./component-harness.mjs";

const source = ts.createSourceFile("aviation-layer-control.tsx", await readFile(new URL("../app/aviation-layer-control.tsx", import.meta.url), "utf8"), ts.ScriptTarget.ES2022, true, ts.ScriptKind.TSX);
const transpile = text => ts.transpileModule(text, { compilerOptions: { target: ts.ScriptTarget.ES2022, module: ts.ModuleKind.CommonJS } }).outputText;
const bounded = {};
new Function("exports", transpile(await readFile(new URL("../app/bounded-json.ts", import.meta.url), "utf8")))(bounded);
const functions = source.statements.filter(node => ts.isFunctionDeclaration(node) && ["withinAviationRead", "readFeed", "loadContext", "isEnvelope"].includes(node.name?.text)).map(node => node.getText(source)).join("\n");
const effectFor = name => {
  let result;
  function visit(node) {
    if (ts.isCallExpression(node) && node.expression.getText(source) === "useEffect" && node.arguments[0]?.getText(source).includes(name)) result = node.arguments[0].getText(source);
    ts.forEachChild(node, visit);
  }
  visit(source);
  assert.ok(result, `execute the actual ${name} effect`);
  return result;
};
const deferred = () => { let resolve, reject; const promise = new Promise((yes, no) => { resolve = yes; reject = no; }); return { promise, resolve, reject }; };
function timers() {
  const jobs = new Map(); let id = 0;
  return { jobs, setTimeout(fn, delay) { jobs.set(++id, { fn, delay }); return id; }, clearTimeout(id) { jobs.delete(id); }, fire(delay) { for (const [id, job] of [...jobs]) if (job.delay === delay) { jobs.delete(id); job.fn(); } } };
}
function readers(fetch, extra = {}) {
  const clock = timers();
  const scope = { ...bounded, fetch, AbortController, AbortSignal, DOMException, TextDecoder, Uint8Array, crypto: globalThis.crypto,
    AVIATION_READ_TIMEOUT_MS: 25_000, ...clock, ...extra };
  return { clock, ...new Function(...Object.keys(scope), transpile(`${functions}\nreturn { readFeed, loadContext };`))(...Object.values(scope)) };
}
const feed = (label = "current") => ({ evidenceRole: "EXTERNAL_CONTEXT_ONLY", records: [], provider: { title: label } });
const readFeed = h => h.readFeed("/api/aviation/traffic", new AbortController().signal, 512, value => Array.isArray(value.records));

test("failed HTTP feeds cancel the body before trying to parse it", async () => {
  let cancelled = false, pulled = false;
  const response = new Response(new ReadableStream({ pull() { pulled = true; }, cancel() { cancelled = true; } }, { highWaterMark: 0 }), { status: 503 });
  const h = readers(async () => response);
  const pending = readFeed(h);
  void pending.catch(() => {});
  // This must reject without waiting for an error response's unfinished body.
  await settle();
  assert.equal(cancelled, true);
  await assert.rejects(pending, /unavailable/);
  assert.equal(pulled, false);
  assert.equal(h.clock.jobs.size, 0);
});

test("feed deadlines include missing headers, even when a transport ignores cancellation", async () => {
  const late = deferred(); let signal;
  const h = readers((_path, init) => { signal = init.signal; return late.promise; });
  const pending = readFeed(h);
  void pending.catch(() => {});
  try {
    assert.equal(h.clock.jobs.size, 1, "a finite budget starts before fetch");
    h.clock.fire(25_000);
    await assert.rejects(pending, { name: "TimeoutError" });
    assert.equal(signal.aborted, true);
  } finally { late.resolve(Response.json(feed())); }
  await settle();
  assert.equal(h.clock.jobs.size, 0);
});

test("feed deadlines cancel stalled bodies and release their locks", async () => {
  let cancelled = false, stream;
  const response = new Response(new ReadableStream({ start(controller) { stream = controller; controller.enqueue(new TextEncoder().encode('{"records":')); }, cancel() { cancelled = true; } }));
  const h = readers(async () => response);
  const pending = readFeed(h); void pending.catch(() => {});
  try {
    await settle();
    assert.equal(h.clock.jobs.size, 1);
    h.clock.fire(25_000);
    await assert.rejects(pending, { name: "TimeoutError" }); await settle();
    assert.equal(cancelled, true);
    assert.equal(response.body.locked, false);
    assert.equal(h.clock.jobs.size, 0);
  } finally { if (!cancelled) stream.close(); }
});

test("cancelling before headers returns promptly and never accepts the delayed reply", async () => {
  const late = deferred(); const parent = new AbortController();
  const h = readers(() => late.promise);
  const pending = h.readFeed("/api/aviation/traffic", parent.signal, 512, () => true);
  let outcome = "pending";
  void pending.then(() => { outcome = "accepted"; }, () => { outcome = "rejected"; });
  parent.abort();
  try { await settle(); assert.equal(outcome, "rejected"); assert.equal(h.clock.jobs.size, 0); await assert.rejects(pending, { name: "AbortError" }); }
  finally { late.resolve(Response.json(feed())); }
});

test("an already cancelled feed cannot start a fetch", async () => {
  let calls = 0; const parent = new AbortController(); parent.abort();
  const h = readers(async () => { calls++; return Response.json(feed()); });
  await assert.rejects(h.readFeed("/api/aviation/traffic", parent.signal, 512, () => true), { name: "AbortError" });
  assert.equal(calls, 0);
});

test("successful feeds retain external-context semantics and reject malformed or oversized bodies", async () => {
  let response = Response.json(feed()); const h = readers(async () => response);
  assert.deepEqual(await readFeed(h), feed());
  for (const value of [{ records: [] }, { ...feed(), records: null }, [feed()]]) {
    response = Response.json(value); await assert.rejects(readFeed(h));
  }
  response = Response.json({ ...feed(), extra: "x".repeat(513) });
  await assert.rejects(readFeed(h), bounded.JsonLimitError);
  assert.equal(h.clock.jobs.size, 0);
});

const contextBytes = await readFile(new URL("../public/data/aviation/kansas-aviation-context.json", import.meta.url));
const asset = { url: "/data/aviation/kansas-aviation-context.json", maxBytes: 2 * 1024 * 1024,
  sha256: Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256", contextBytes)), byte => byte.toString(16).padStart(2, "0")).join("") };
const contextReader = (fetch, extra = {}) => readers(fetch, { AVIATION_CONTEXT_ASSET: asset, parseAviationContext: value => value, ...extra });

test("airspace hashes exact streamed bytes and never calls an unbounded arrayBuffer", async () => {
  const response = new Response(contextBytes);
  response.arrayBuffer = () => { throw new Error("unbounded read"); };
  const h = contextReader(async () => response);
  const result = await h.loadContext(new AbortController().signal);
  assert.deepEqual(result, JSON.parse(contextBytes));
  assert.equal(h.clock.jobs.size, 0);
});

for (const declared of [false, true]) test(`airspace rejects ${declared ? "declared" : "streamed"} oversize before hashing or parsing`, async () => {
  let cancelled = false, parsed = false, hashed = false;
  const response = new Response(new ReadableStream({ start(controller) { controller.enqueue(new Uint8Array(asset.maxBytes + 1)); }, cancel() { cancelled = true; } }), declared ? { headers: { "content-length": String(asset.maxBytes + 1) } } : undefined);
  response.arrayBuffer = async () => { throw new Error("unbounded read"); };
  const h = contextReader(async () => response, { parseAviationContext() { parsed = true; }, crypto: { subtle: { digest() { hashed = true; } } } });
  await assert.rejects(h.loadContext(new AbortController().signal));
  assert.equal(cancelled, true); assert.equal(hashed, false); assert.equal(parsed, false);
});

test("airspace integrity still rejects altered bytes before parsing", async () => {
  let parsed = false;
  const h = contextReader(async () => new Response(contextBytes.toString() + " "), { parseAviationContext() { parsed = true; } });
  await assert.rejects(h.loadContext(new AbortController().signal), /pinned digest/);
  assert.equal(parsed, false);
});

test("the binary reader preserves chunk boundaries, BOM and exact-limit bytes for hashing", async () => {
  const expected = Uint8Array.from([239, 187, 191, 0, 255, 1]);
  const response = new Response(new ReadableStream({ start(controller) { controller.enqueue(expected.subarray(0, 2)); controller.enqueue(expected.subarray(2, 5)); controller.enqueue(expected.subarray(5)); controller.close(); } }));
  assert.deepEqual(await bounded.readBoundedBytes(response, expected.length), expected);
  assert.equal(response.body.locked, false);
});

test("cancelling an airspace stream releases the reader and discards partial bytes", async () => {
  const parent = new AbortController(); let cancelled = false;
  const response = new Response(new ReadableStream({ start(controller) { controller.enqueue(Uint8Array.of(1)); }, cancel() { cancelled = true; } }));
  const pending = bounded.readBoundedBytes(response, 32, parent.signal);
  await settle(); parent.abort();
  await assert.rejects(pending, { name: "AbortError" });
  assert.equal(cancelled, true); assert.equal(response.body.locked, false);
});

test("empty byte streams stay exact and a missing stream remains unavailable", async () => {
  assert.deepEqual(await bounded.readBoundedBytes(new Response(""), 1), new Uint8Array());
  await assert.rejects(bounded.readBoundedBytes(new Response(null), 1), /Missing response body/);
});

for (const kind of ["UASFM_API_PATH", "TFR_API_PATH"]) test(`a late ${kind} reply cannot commit after its layer is hidden`, async () => {
  const clock = timers(), pending = deferred(), commits = [], uasLoaded = { current: false };
  const scope = { ...clock, visible: true, showUas: true, uasLoaded, AbortController,
    UASFM_API_PATH: "/uas", TFR_API_PATH: "/tfr", TFR_REFRESH_MS: 600_000,
    readFeed: () => pending.promise, setUas: value => commits.push(value), setTfrs: value => commits.push(value),
    setInterval: () => 1, clearInterval() {},
  };
  const cleanup = new Function(...Object.keys(scope), transpile(`return (${effectFor(kind)})();`))(...Object.values(scope));
  clock.fire(0); cleanup(); const before = [...commits];
  pending.resolve({ cells: [], kansas: [] }); await settle();
  assert.deepEqual(commits, before);
  assert.equal(uasLoaded.current, false);
});

function trafficEffect() {
  const clock = timers(), intervals = new Map(), requests = [], commits = []; let id = 0;
  const scope = { ...clock, visible: true, showTraffic: true, AbortController, Date,
    TRAFFIC_REFRESH_MS: 20_000, TRAFFIC_EXPIRY_TICK_MS: 5_000, AVIATION_TRAFFIC_API_PATH: "/api/aviation/traffic",
    readFeed: (_path, signal) => { const request = { ...deferred(), signal }; requests.push(request); return request.promise; },
    setTraffic: value => commits.push(value), setTrafficNow() {},
    setInterval: (fn, delay) => { intervals.set(++id, { fn, delay }); return id; }, clearInterval: id => intervals.delete(id),
  };
  const cleanup = new Function(...Object.keys(scope), transpile(`return (${effectFor("TRAFFIC_REFRESH_MS")})();`))(...Object.values(scope));
  clock.fire(0);
  return { requests, commits, intervals, clock, cleanup, refresh() { for (const job of intervals.values()) if (job.delay === 20_000) job.fn(); } };
}

test("slow traffic refreshes never overlap or queue another immediate request", async () => {
  const h = trafficEffect();
  try {
    assert.equal(h.requests.length, 1);
    h.refresh(); h.refresh();
    assert.equal(h.requests.length, 1);
    h.requests[0].resolve(feed("first")); await settle();
    assert.equal(h.commits.at(-1).value.provider.title, "first");
    assert.equal(h.requests.length, 1);
    h.refresh(); assert.equal(h.requests.length, 2);
    h.requests[1].resolve(feed("next")); await settle();
    assert.equal(h.commits.at(-1).value.provider.title, "next");
  } finally { h.cleanup(); for (const request of h.requests) request.resolve(feed()); }
});

for (const fail of [false, true]) test(`a late traffic ${fail ? "failure" : "success"} cannot change a hidden layer`, async () => {
  const h = trafficEffect(); h.cleanup();
  if (fail) h.requests[0].reject(new Error("late")); else h.requests[0].resolve(feed("old"));
  await settle();
  assert.deepEqual(h.commits, [{ state: "idle", value: null }]);
  assert.equal(h.requests[0].signal.aborted, true);
  assert.equal(h.intervals.size, 0); assert.equal(h.clock.jobs.size, 0);
});

test("a failed traffic round permits the next paced retry", async () => {
  const h = trafficEffect();
  try {
    h.requests[0].reject(new DOMException("slow", "TimeoutError")); await settle();
    assert.deepEqual(h.commits.at(-1), { state: "error", value: null });
    h.refresh(); assert.equal(h.requests.length, 2);
    h.requests[1].resolve(feed("recovered")); await settle();
    assert.equal(h.commits.at(-1).value.provider.title, "recovered");
  } finally { h.cleanup(); }
});
