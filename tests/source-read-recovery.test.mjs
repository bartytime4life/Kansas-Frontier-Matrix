import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { setImmediate as nextTurn } from "node:timers/promises";
import test from "node:test";
import ts from "typescript";

async function compile(name, imports = {}) {
  const source = await readFile(new URL(`../app/${name}.ts`, import.meta.url), "utf8");
  const code = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 } }).outputText;
  const mod = { exports: {} };
  new Function("require", "module", "exports", code)(id => imports[id], mod, mod.exports);
  return mod.exports;
}
const bounded = await compile("bounded-json");
const transport = await compile("browser-json-request", { "./bounded-json": bounded });
const { LayerJsonReads } = await compile("layer-json-reads", { "./browser-json-request": transport });
const census = "/api/live-context?feed=census-counties";
const river = "/api/hydrology/streamflow?mode=network&range=24h&encoding=columns-v1";
const originTime = Date.parse("2026-10-17T12:00:00Z");
const snapshot = { state: "ready", retrievedAt: "2026-10-17T11:59:00Z", observations: [{ value: 0 }] };
const options = (recovery = "census", extra = {}) => ({ signal: new AbortController().signal, maxBytes: 4096, timeoutMs: 30_000, recovery, ...extra });
function clock(t) { t.mock.timers.enable({ apis: ["setTimeout", "Date"], now: originTime }); }
async function drive(t, promise, budget = 151_000) {
  let done = false, value, error;
  promise.then(result => { done = true; value = result; }, reason => { done = true; error = reason; });
  for (let elapsed = 0; !done && elapsed <= budget; elapsed += 1_000) {
    await nextTurn();
    if (!done) t.mock.timers.tick(1_000);
  }
  assert.equal(done, true, "request must settle within the bounded recovery window");
  if (error) throw error;
  return value;
}

test("Census recovers from temporary HTTP failures, including a gateway HTML error, without rewriting source times", async t => {
  clock(t); const calls = [];
  t.mock.method(globalThis, "fetch", async (url, init) => {
    calls.push(Date.now()); assert.equal(url, census); assert.equal(init.cache, "no-store"); assert.equal(init.credentials, "same-origin");
    if (calls.length === 1) return Response.json({ error: "temporary source failure" }, { status: 502 });
    if (calls.length === 2) return new Response("<html>gateway timeout</html>", { status: 504 });
    return Response.json(snapshot);
  });
  const result = await drive(t, transport.browserJsonRequest(census, options()));
  assert.deepEqual(result.body, snapshot); assert.equal(calls.length, 3);
  assert.ok(calls[1] - calls[0] >= 1000); assert.ok(calls[2] - calls[1] >= 2000);
});

test("River Pulse waits for another tab's full network acquisition and then accepts the original cached capture", async t => {
  clock(t); const calls = [];
  t.mock.method(globalThis, "fetch", async () => {
    calls.push(Date.now());
    return Date.now() < originTime + 60_000
      ? Response.json({ code: "USGS_STREAMFLOW_NETWORK_BUSY" }, { status: 429, headers: { "Retry-After": "2" } })
      : Response.json(snapshot, { headers: { "X-KFM-Network-Cache": "HIT" } });
  });
  const result = await drive(t, transport.browserJsonRequest(river, options("river-network", { timeoutMs: 75_000 })));
  assert.deepEqual(result.body, snapshot); assert.equal(result.response.headers.get("X-KFM-Network-Cache"), "HIT");
  assert.ok(calls.length <= 11); assert.ok(calls.at(-1) - originTime >= 60_000);
  assert.ok(calls.slice(1).every((at, i) => at - calls[i] >= 2_000));
});

test("the River Pulse response can finish after the server's 60-second acquisition budget", async t => {
  clock(t); let calls = 0;
  t.mock.method(globalThis, "fetch", async (_url, { signal }) => {
    calls++;
    await new Promise((resolve, reject) => {
      setTimeout(resolve, 65_000);
      signal.addEventListener("abort", () => reject(signal.reason), { once: true });
    });
    return Response.json(snapshot);
  });
  const result = await drive(t, transport.browserJsonRequest(river, options("river-network", { timeoutMs: 75_000 })));
  assert.deepEqual(result.body, snapshot); assert.equal(calls, 1);
});

test("network disconnects and per-attempt timeouts recover, including cancellation of a stalled response body", async t => {
  clock(t); let calls = 0, canceled = false;
  t.mock.method(globalThis, "fetch", async () => {
    calls++;
    if (calls === 1) throw new TypeError("Failed to fetch");
    if (calls === 2) return new Response(new ReadableStream({ start(c) { c.enqueue(new TextEncoder().encode('{"pending":')); }, cancel() { canceled = true; } }));
    return Response.json(snapshot);
  });
  assert.deepEqual((await drive(t, transport.browserJsonRequest(census, options(undefined, { timeoutMs: 2_000 })))).body, snapshot);
  assert.equal(calls, 3); assert.equal(canceled, true);
});

test("provider cooldowns are never shortened and short Retry-After dates are honored", async t => {
  clock(t); let calls = 0;
  t.mock.method(globalThis, "fetch", async () => {
    calls++; return Response.json({ code: "USGS_STREAMFLOW_RATE_LIMITED" }, { status: 429, headers: { "Retry-After": "300" } });
  });
  assert.equal((await transport.browserJsonRequest(river, options("river-network"))).response.status, 429);
  assert.equal(calls, 1); assert.equal(Date.now(), originTime);
  calls = 0; const requestedAt = [];
  t.mock.method(globalThis, "fetch", async () => {
    requestedAt.push(Date.now()); calls++;
    return calls === 1 ? Response.json({}, { status: 503, headers: { "Retry-After": new Date(originTime + 10_000).toUTCString() } }) : Response.json(snapshot);
  });
  await drive(t, transport.browserJsonRequest(census, options()));
  assert.ok(requestedAt[1] - requestedAt[0] >= 10_000);
});

test("public source reads recover from HTML rate-limit pages after the provider's numeric or dated cooldown", async t => {
  clock(t);
  for (const [url, recovery, dated] of [[census, "census", false], [river, "river-network", true]]) {
    const calls = [], started = Date.now();
    t.mock.method(globalThis, "fetch", async () => {
      calls.push(Date.now());
      return calls.length === 1
        ? new Response("<html>Too many requests</html>", { status: 429, headers: { "Retry-After": dated ? new Date(started + 10_000).toUTCString() : "10" } })
        : Response.json(snapshot);
    });
    const result = await drive(t, transport.browserJsonRequest(url, options(recovery)));
    assert.deepEqual(result.body, snapshot); assert.equal(calls.length, 2);
    assert.ok(calls[1] - calls[0] >= 10_000, "a non-JSON response must not shorten the provider cooldown");
  }
});

test("HTML rate-limit pages require a usable cooldown within the recovery budget and cannot bypass byte limits", async t => {
  clock(t);
  for (const headers of [{}, { "Retry-After": "invalid" }, { "Retry-After": "300" }, { "Retry-After": "1", "content-length": "4097" }]) {
    let calls = 0;
    t.mock.method(globalThis, "fetch", async () => {
      calls++; return new Response("<html>Too many requests</html>", { status: 429, headers });
    });
    await assert.rejects(transport.browserJsonRequest(census, options()));
    assert.equal(calls, 1); assert.equal(Date.now(), originTime);
  }
});

test("HTML rate-limit recovery stops after three attempts or caller cancellation", async t => {
  clock(t); let calls = 0;
  t.mock.method(globalThis, "fetch", async () => {
    calls++; return new Response("<html>Too many requests</html>", { status: 429, headers: { "Retry-After": "2" } });
  });
  await assert.rejects(drive(t, transport.browserJsonRequest(census, options())), SyntaxError);
  assert.equal(calls, 3);
  calls = 0;
  const controller = new AbortController();
  const pending = transport.browserJsonRequest(river, options("river-network", { signal: controller.signal }));
  const rejected = assert.rejects(pending, { name: "AbortError" });
  await nextTurn(); controller.abort(); await rejected;
  t.mock.timers.tick(150_000); await nextTurn(); assert.equal(calls, 1);
});

test("repeated failures and busy responses have finite attempt and elapsed-time limits", async t => {
  clock(t); let calls = 0;
  t.mock.method(globalThis, "fetch", async () => { calls++; return Response.json({}, { status: 502 }); });
  assert.equal((await drive(t, transport.browserJsonRequest(census, options()))).response.status, 502);
  assert.equal(calls, 3);
  calls = 0;
  t.mock.method(globalThis, "fetch", async () => { calls++; return Response.json({ code: "USGS_STREAMFLOW_NETWORK_BUSY" }, { status: 429 }); });
  assert.equal((await drive(t, transport.browserJsonRequest(river, options("river-network")))).response.status, 429);
  assert.equal(calls, 11);
  calls = 0;
  t.mock.method(globalThis, "fetch", (_url, { signal }) => {
    calls++; return new Promise((_resolve, reject) => signal.addEventListener("abort", () => reject(signal.reason), { once: true }));
  });
  const start = Date.now();
  await assert.rejects(drive(t, transport.browserJsonRequest(census, options())), { name: "TimeoutError" });
  assert.ok(Date.now() - start <= 65_000); assert.equal(calls, 3);
});

test("invalid successful JSON, byte-limit violations, permanent HTTP failures and server work limits stay failed", async t => {
  clock(t);
  for (const makeResponse of [() => new Response("{"), () => new Response("{}", { headers: { "content-length": "4097" } })]) {
    let calls = 0; t.mock.method(globalThis, "fetch", async () => { calls++; return makeResponse(); });
    await assert.rejects(transport.browserJsonRequest(census, options())); assert.equal(calls, 1);
  }
  for (const status of [400, 401, 403, 404, 429, 503]) {
    let calls = 0;
    t.mock.method(globalThis, "fetch", async () => { calls++; return Response.json({ code: "USGS_STREAMFLOW_BUDGET_EXCEEDED" }, { status }); });
    assert.equal((await transport.browserJsonRequest(river, options("river-network"))).response.status, status); assert.equal(calls, 1);
  }
});

test("private and write requests remain one-shot and cannot opt into public recovery", async t => {
  clock(t); let calls = 0;
  t.mock.method(globalThis, "fetch", async () => { calls++; return Response.json({}, { status: 503 }); });
  const oneShot = { signal: new AbortController().signal, maxBytes: 4096 };
  await transport.browserJsonRequest("/api/knowledge", oneShot);
  await transport.browserJsonRequest("/api/archive/capture", { ...oneShot, method: "POST", body: "{}" });
  assert.equal(calls, 2);
  for (const [url, init] of [["/api/knowledge", {}], [census, { method: "POST" }], [census, { body: "{}" }], [census + "&day=2024-01-01", {}], ["https://other.example" + census, {}]]) {
    await assert.rejects(transport.browserJsonRequest(url, options("census", init)), /limited/);
  }
  assert.equal(calls, 2);
});

test("hiding the final Census consumer cancels retry backoff; another consumer may still recover", async t => {
  clock(t); let calls = 0;
  t.mock.method(globalThis, "fetch", async () => { calls++; return calls < 3 ? Response.json({}, { status: 502 }) : Response.json(snapshot); });
  const pool = new LayerJsonReads(), first = new AbortController(), second = new AbortController();
  const readOptions = signal => ({ signal, maxBytes: 4096, validate: body => body.state === "ready" });
  const a = pool.read(census, readOptions(first.signal)); const canceled = assert.rejects(a, { name: "AbortError" });
  const b = pool.read(census, readOptions(second.signal));
  await nextTurn(); first.abort(); await canceled;
  assert.deepEqual((await drive(t, b)).body, snapshot); assert.equal(calls, 3);
  const final = new AbortController();
  t.mock.method(globalThis, "fetch", async () => { calls++; return Response.json({}, { status: 502 }); });
  const pending = pool.read(census, readOptions(final.signal)); const rejected = assert.rejects(pending, { name: "AbortError" });
  await nextTurn(); final.abort(); await rejected;
  await nextTurn(); const stoppedAt = calls; t.mock.timers.tick(65_000); await nextTurn(); assert.equal(calls, stoppedAt);
});

test("canceling River Pulse during backoff stops further requests", async t => {
  clock(t); let calls = 0; const controller = new AbortController();
  t.mock.method(globalThis, "fetch", async () => { calls++; return Response.json({ code: "USGS_STREAMFLOW_NETWORK_BUSY" }, { status: 429 }); });
  const pending = transport.browserJsonRequest(river, options("river-network", { signal: controller.signal }));
  const rejected = assert.rejects(pending, { name: "AbortError" });
  await nextTurn(); controller.abort(); await rejected;
  t.mock.timers.tick(150_000); await nextTurn(); assert.equal(calls, 1);
});

const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
const effectStart = page.lastIndexOf("  useEffect(() => {", page.indexOf("    if (!streamflowSelectedAtPresent) {"));
const riverEffect = page.slice(effectStart, page.indexOf("\n  useEffect(", effectStart + 1));
function installRiverEffect(selected = true) {
  const window = new EventTarget(), document = new EventTarget();
  let cleanup, calls = 0, intervalCleared = false;
  Object.assign(window, { setInterval: () => 1, clearInterval: () => { intervalCleared = true; } });
  document.hidden = false;
  const active = new AbortController();
  const bindings = { navigationReadEpoch: 0, window, document, useEffect: fn => { cleanup = fn(); }, streamflowSelectedAtPresent: selected,
    setStreamflowPlaying: () => {}, streamflowRequestRef: { current: active }, explorerRestoredRef: { current: true },
    streamflowArchiveDayRef: { current: null }, streamflowRange: "24h", streamflowSelectedStationId: null,
    refreshStreamflow: () => { calls++; } };
  new Function(...Object.keys(bindings), riverEffect)(...Object.values(bindings));
  return { bindings, active, cleanup, calls: () => calls, cleared: () => intervalCleared };
}

test("the production River Pulse effect cancels hidden/history acquisition and recovers on reconnect or tab return", () => {
  const hidden = installRiverEffect(false);
  assert.equal(hidden.active.signal.aborted, true); assert.equal(hidden.bindings.streamflowRequestRef.current, null); assert.equal(hidden.calls(), 0);
  const view = installRiverEffect(), b = view.bindings;
  b.window.dispatchEvent(new Event("online")); assert.equal(view.calls(), 0, "active request is not duplicated");
  b.streamflowRequestRef.current = null;
  b.window.dispatchEvent(new Event("online")); assert.equal(view.calls(), 1);
  b.document.hidden = true; b.document.dispatchEvent(new Event("visibilitychange")); assert.equal(view.calls(), 1);
  b.document.hidden = false; b.document.dispatchEvent(new Event("visibilitychange")); assert.equal(view.calls(), 2);
  b.streamflowArchiveDayRef.current = "2026-10-16";
  b.window.dispatchEvent(new Event("online")); assert.equal(view.calls(), 2, "archive view never becomes a current-source read");
  view.cleanup(); assert.equal(view.cleared(), true);
  b.streamflowArchiveDayRef.current = null;
  b.window.dispatchEvent(new Event("online")); b.document.dispatchEvent(new Event("visibilitychange")); assert.equal(view.calls(), 2);
});

test("a successful but incompatible Census payload is rejected without caching or retrying it as a valid snapshot", async t => {
  let calls = 0;
  t.mock.method(globalThis, "fetch", async () => { calls++; return Response.json({ feed: "wrong-source" }); });
  const pool = new LayerJsonReads();
  const read = () => pool.read(census, { signal: new AbortController().signal, maxBytes: 4096, cacheMs: 300_000, validate: body => body.feed === "census-counties" });
  await assert.rejects(read(), /incompatible/); assert.equal(calls, 1);
  await assert.rejects(read(), /incompatible/); assert.equal(calls, 2);
});

test("the production Census reconnect listener refreshes only selected present-day context and is removed on cleanup", () => {
  const start = page.lastIndexOf("  useEffect(() => {", page.indexOf("      const day = currentUtcDay();", page.indexOf("  const hideAllOfficialContext =")));
  const source = page.slice(start, page.indexOf("\n  useEffect(", start + 1));
  const compiled = ts.transpileModule(source, { compilerOptions: { target: ts.ScriptTarget.ES2022 } }).outputText;
  const window = new EventTarget(), document = new EventTarget(), calls = [];
  let cleanup;
  window.setInterval = () => 1;
  document.hidden = false;
  const bindings = { navigationReadEpoch: 0, window, document, clearInterval: () => {}, useEffect: fn => { cleanup = fn(); },
    currentUtcDay: () => "2026-10-17", setBaselineDay: () => {}, buildYearCurrentRef: { current: true },
    officialVisibilityRef: { current: { "census-counties": true } }, temporalQueryRef: { current: { frame: 2026 } },
    OFFICIAL_CONTEXT_PRESENT_FRAME: 2026, OFFICIAL_CONTEXT_SOURCES: [], refreshOfficialContext: feed => calls.push(feed) };
  new Function(...Object.keys(bindings), compiled)(...Object.values(bindings));
  window.dispatchEvent(new Event("online")); assert.deepEqual(calls, ["census-counties"]);
  document.hidden = true; window.dispatchEvent(new Event("online"));
  document.hidden = false; bindings.temporalQueryRef.current.frame = 1900; window.dispatchEvent(new Event("online"));
  bindings.temporalQueryRef.current.frame = 2026; bindings.officialVisibilityRef.current["census-counties"] = false;
  window.dispatchEvent(new Event("online")); assert.equal(calls.length, 1);
  cleanup(); bindings.officialVisibilityRef.current["census-counties"] = true;
  window.dispatchEvent(new Event("online")); assert.equal(calls.length, 1);
});


test('retained-document pageshow revalidates the restored view, while normal loading does not duplicate restoration', () => {
  const start = page.lastIndexOf('  useEffect(() => {', page.indexOf('    const restore = window.setTimeout(restoreExplorerFromUrl, 0);'));
  const source = page.slice(start, page.indexOf('\n  useEffect(', start + 1));
  const compiled = ts.transpileModule(source, { compilerOptions: { target: ts.ScriptTarget.ES2022 } }).outputText;
  const window = new EventTarget(); let initial, cleanup, restores = 0;
  window.setTimeout = fn => { initial = fn; return 1; }; window.clearTimeout = () => {};
  const restoreExplorerFromUrl = () => { restores++; };
  new Function('window', 'useEffect', 'restoreExplorerFromUrl', compiled)(window, fn => { cleanup = fn(); }, restoreExplorerFromUrl);
  initial(); assert.equal(restores, 1);
  const show = persisted => { const event = new Event('pageshow'); Object.defineProperty(event, 'persisted', {value:persisted}); window.dispatchEvent(event); };
  show(false); assert.equal(restores, 1);
  show(true); assert.equal(restores, 2, 'bfcache restore cannot retain unchecked current payloads indefinitely');
  window.dispatchEvent(new Event('popstate')); assert.equal(restores, 3);
  cleanup(); show(true); window.dispatchEvent(new Event('popstate')); assert.equal(restores, 3, 'both listeners are released');
});


test('history restoration schedules an uncached check even when the selected current view already has a payload', () => {
  const start = page.lastIndexOf('  useEffect(() => {', page.indexOf('    // Hydrate selected current sources on first entry'));
  const source = page.slice(start, page.indexOf('\n  const dismissMapUtilityWithoutFocus', start));
  const compiled = ts.transpileModule(source, { compilerOptions: { target: ts.ScriptTarget.ES2022 } }).outputText;
  const checks = [], timers = []; let dependencies;
  const bindings = {buildYearCurrent:true,calendarSweep:null,navigationReadEpoch:7,officialArchiveDays:{},temporalQuery:{frame:2026},OFFICIAL_CONTEXT_PRESENT_FRAME:2026,
    officialVisibilityRef:{current:{'usgs-earthquakes':true}}, officialRequestsRef:{current:new Map()},
    officialPayloadsRef:{current:{'usgs-earthquakes':snapshot}}, officialArchiveDaysRef:{current:{}},
    OFFICIAL_CONTEXT_SOURCES:[{id:'usgs-earthquakes',apiPath:'/api/live-context?feed=usgs-earthquakes'},{id:'hidden',apiPath:'/api/hidden'}],
    searchNeedsCounties:()=>false,refreshOfficialContext:feed=>checks.push(feed),setOfficialStates(){},
    window:{setTimeout:fn=>{timers.push(fn);return 1;},clearTimeout(){}},useEffect:(fn,deps)=>{dependencies=deps;fn();}};
  new Function(...Object.keys(bindings), compiled)(...Object.values(bindings));
  assert.ok(dependencies.includes(7), 'a same-date Back/Forward restore reruns the scheduler');
  timers.splice(0).forEach(fn=>fn());
  assert.deepEqual(checks,['usgs-earthquakes'],'an existing payload is rechecked; hidden sources stay idle');
  for (const extra of [{temporalQuery:{frame:1900}},{calendarSweep:{day:'2020-01-01'}},{buildYearCurrent:false}]) {
    checks.length=0; timers.length=0;
    const scope={...bindings,...extra};
    new Function(...Object.keys(scope), compiled)(...Object.values(scope));
    timers.splice(0).forEach(fn=>fn()); assert.deepEqual(checks,[], 'historical or invalid-build context does not request current sources');
  }
});
