import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

async function compile(name, dependencies = {}) {
  const source = await readFile(`app/${name}.ts`, "utf8");
  const code = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 } }).outputText;
  const compiled = { exports: {} };
  new Function("require", "module", "exports", code)(id => dependencies[id], compiled, compiled.exports);
  return compiled.exports;
}
const bounded = await compile("bounded-json");
const smoke = await compile("hms-smoke-playback", { "./bounded-json": bounded });
const day = "2024-06-01";
const payload = { feed: "noaa-hms-smoke", state: "empty", retrievedAt: "2024-06-02T00:00:00Z", smokeCoverage: { day, availableDays: [day], missingDays: [] }, featureCount: 0, data: { type: "FeatureCollection", features: [] } };
const deferred = () => { let resolve, reject; const promise = new Promise((a, b) => { resolve = a; reject = b; }); return { promise, resolve, reject }; };

test("smoke cancellation settles a stalled JSON body and releases its reader", async () => {
  const started = deferred(); let stream, canceled = false;
  const response = new Response(new ReadableStream({ start(controller) { stream = controller; controller.enqueue(new TextEncoder().encode('{"feed":')); started.resolve(); }, cancel() { canceled = true; } }));
  const cache = new smoke.HmsFrameCache(async () => response);
  const controller = new AbortController();
  const pending = cache.get(day, controller.signal);
  await started.promise;
  await new Promise(resolve => setTimeout(resolve, 0));
  controller.abort();
  let timer;
  try {
    assert.equal(await Promise.race([pending.then(() => "resolved", error => error.name), new Promise(resolve => { timer = setTimeout(() => resolve("still waiting"), 80); })]), "AbortError");
    assert.equal(canceled, true); assert.equal(response.body.locked, false); assert.equal(cache.size, 0);
  } finally { clearTimeout(timer); if (!canceled) stream.error(new Error("test cleanup")); await pending.catch(() => {}); }
});

test("smoke cannot cache a day claimed both available and missing", async () => {
  const cache = new smoke.HmsFrameCache(async () => Response.json({ ...payload, smokeCoverage: { ...payload.smokeCoverage, missingDays: [day] } }));
  await assert.rejects(cache.get(day, new AbortController().signal));
  assert.equal(cache.size, 0);
});

// Exercise the production callback with a controlled renderer; no WebGL or
// provider request is substituted by these unit tests.
const page = await readFile("app/page.tsx", "utf8");
const callback = page.slice(page.indexOf("  const commitSmokePlayback ="), page.indexOf("  const loadOfficialArchiveDay ="));
const callbackCode = ts.transpileModule(callback, { compilerOptions: { target: ts.ScriptTarget.ES2022 } }).outputText;
function renderer(overrides = {}) {
  const prior = { id: "confirmed" }, next = { id: "next" };
  const ref = value => ({ current: value });
  const source = { type: "geojson" };
  const writes = [], paints = [], commits = [];
  const context = {
    useCallback: fn => fn,
    mapRef: ref({ getSource: () => source }), styleGenerationReadyRef: ref(true),
    officialPayloadsRef: ref({ "noaa-hms-smoke": prior }), officialArchivePayloadsRef: ref({}),
    officialArchiveDaysRef: ref({ "noaa-hms-smoke": day }),
    officialVisibilityRef: ref({ "noaa-hms-smoke": true }), temporalQueryRef: ref({ frame: 2026 }),
    noaaRadarReadyRef: ref(false), noaaRadarFrameTimeRef: ref(null), officialOpacityRef: ref({ "noaa-hms-smoke": .38 }),
    runtimeOfficialVisibility: v => v, OFFICIAL_CONTEXT_BY_ID: { "noaa-hms-smoke": { sourceId: "smoke" } },
    applyOfficialContextState: (_map, _visibility, _opacity, values) => writes.push(values["noaa-hms-smoke"]),
    setHmsSmokeFade: (_map, factor) => paints.push(factor),
    resetHmsSmokeFade: () => paints.push("reset"),
    hmsFade: async (from, to, signal, paint) => { signal.throwIfAborted(); paint(to); },
    waitForGeoJSON: async () => {},
    geoJSONHasData: () => true,
    setOfficialPayloads: () => {}, setOfficialArchiveDays: fn => commits.push(fn({})),
    setOfficialStates: () => {}, setOfficialErrors: () => {},
    smokeTransitionsRef: ref(new smoke.HmsFrameTransitions()),
    ...overrides,
  };
  const commit = new Function(...Object.keys(context), callbackCode + "\nreturn commitSmokePlayback;")(...Object.values(context));
  return { context, commit, prior, next, source, writes, paints, commits };
}

test("smoke cannot accept a displayed date without an available renderer", async () => {
  const r = renderer({ mapRef: { current: null } });
  await assert.rejects(r.commit(day, r.next, new AbortController().signal, true));
  assert.equal(r.context.officialPayloadsRef.current["noaa-hms-smoke"], r.prior);
  assert.deepEqual(r.commits, []);
});

test("the 30-second deadline includes a stalled smoke body", async (t) => {
  t.mock.timers.enable({ apis: ["setTimeout"] });
  let canceled = false;
  const response = new Response(new ReadableStream({ start(controller) { controller.enqueue(new TextEncoder().encode('{"feed":')); }, cancel() { canceled = true; } }));
  const cache = new smoke.HmsFrameCache(async () => response);
  const pending = cache.get(day, new AbortController().signal);
  const result = assert.rejects(pending, { name: "TimeoutError" });
  await new Promise(resolve => setImmediate(resolve));
  t.mock.timers.tick(30_000);
  await result;
  assert.equal(canceled, true); assert.equal(response.body.locked, false); assert.equal(cache.size, 0);
});

test("a source replaced during upload cannot advance the date or retain the old fade", async () => {
  const uploaded = deferred(), started = deferred();
  const r = renderer({ waitForGeoJSON: () => { started.resolve(); return uploaded.promise; } });
  const pending = r.commit(day, r.next, new AbortController().signal, true);
  await started.promise;
  r.context.mapRef.current.getSource = () => ({ type: "geojson" });
  uploaded.resolve();
  await assert.rejects(pending, /map changed/);
  assert.equal(r.context.officialPayloadsRef.current["noaa-hms-smoke"], r.prior);
  assert.deepEqual(r.commits, []);
  assert.deepEqual(r.paints.slice(-2), ["reset", 1]);
});

test("display date commits only after upload and fade finish; exact payload is retained", async () => {
  const uploaded = deferred(), started = deferred(), faded = deferred(), fading = deferred();
  const r = renderer({
    waitForGeoJSON: () => { started.resolve(); return uploaded.promise; },
    hmsFade: async (from, to, signal, paint) => { signal.throwIfAborted(); if (to === 1) { fading.resolve(); await faded.promise; } paint(to); },
  });
  const pending = r.commit(day, r.next, new AbortController().signal, true);
  await started.promise; assert.deepEqual(r.commits, []);
  uploaded.resolve(); await fading.promise; assert.deepEqual(r.commits, []);
  faded.resolve(); await pending;
  assert.deepEqual(r.commits, [{ "noaa-hms-smoke": day }]);
  assert.equal(r.context.officialArchivePayloadsRef.current["noaa-hms-smoke"], r.next);
  assert.deepEqual(r.writes, [r.next]);
});

test("queued superseded frames cannot run after a slow restoration", async () => {
  const transitions = new smoke.HmsFrameTransitions(), cleanup = deferred(), started = deferred();
  const calls = [];
  const first = transitions.run(new AbortController().signal, async signal => {
    calls.push("first"); started.resolve();
    try { await new Promise((_resolve, reject) => signal.addEventListener("abort", () => reject(signal.reason), { once: true })); }
    finally { await cleanup.promise; calls.push("restored"); }
  });
  const firstResult = assert.rejects(first, { name: "AbortError" });
  await started.promise;
  const second = transitions.run(new AbortController().signal, async () => { calls.push("superseded"); });
  const secondResult = assert.rejects(second, { name: "AbortError" });
  const third = transitions.run(new AbortController().signal, async () => { calls.push("latest"); });
  assert.deepEqual(calls, ["first"]);
  cleanup.resolve(); await Promise.all([firstResult, secondResult, third]);
  assert.deepEqual(calls, ["first", "restored", "latest"]);
});

test("a competing map-state update cannot be labeled as the requested smoke day", async () => {
  const r = renderer({ geoJSONHasData: () => false });
  await assert.rejects(r.commit(day, r.next, new AbortController().signal, false), /map changed/);
  assert.deepEqual(r.commits, []);
  assert.equal(r.context.officialPayloadsRef.current["noaa-hms-smoke"], r.prior);
});

test("a superseded upload is restored before the next transition reads its prior frame", async () => {
  const entered = deferred(); let call = 0;
  const r = renderer({ waitForGeoJSON: (_source, signal) => {
    call++;
    if (call === 1) { entered.resolve(); return new Promise((_resolve, reject) => signal.addEventListener("abort", () => reject(signal.reason), { once: true })); }
    if (call === 3) return Promise.reject(new Error("second upload failed"));
    return Promise.resolve();
  } });
  const old = new AbortController();
  const first = r.commit(day, r.next, old.signal, true);
  const firstResult = first.catch(error => error);
  await entered.promise;
  old.abort();
  const newer = { id: "newer" };
  const second = r.commit("2024-06-02", newer, new AbortController().signal, true);
  await firstResult;
  await assert.rejects(second, /second upload failed/);
  assert.equal(r.context.officialPayloadsRef.current["noaa-hms-smoke"], r.prior);
  assert.deepEqual(r.commits, []);
  assert.equal(r.writes.at(-1), r.prior);
});
