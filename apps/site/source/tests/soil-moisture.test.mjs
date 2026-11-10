import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const compile = async (name, imports = {}) => {
  const source = await readFile(new URL(`../app/${name}.ts`, import.meta.url), "utf8");
  const output = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 } }).outputText;
  const mod = { exports: {} };
  new Function("require", "module", "exports", output)((key) => imports[key], mod, mod.exports);
  return mod.exports;
};
const soil = await compile("soil-moisture");
const bounded = await compile("bounded-json");
const server = await compile("soil-moisture-server", {
  "./soil-moisture": soil,
  "./bounded-json": bounded,
});
const availabilityRoute = await compile("api/soil-moisture/availability/route", {
  "../../../soil-moisture-server": {
    soilAvailability: async () => ({ value: { availableDays: ["2026-09-28"], latestCommonDay: "2026-09-28", daysByView: {}, checkedAt: "2026-09-29T12:00:00.000Z" }, cache: "miss" }),
    SoilSourceError: class SoilSourceError extends Error {},
  },
  "../../../soil-moisture": soil,
});
const now = new Date("2026-09-29T13:00:00Z");
const layer = (name, ranges) => `<Layer><ows:Identifier>${name}</ows:Identifier><Dimension><ows:Identifier>Time</ows:Identifier>${ranges.map(range => `<Value>${range}</Value>`).join("")}</Dimension><TileMatrixSetLink><TileMatrixSet>GoogleMapsCompatible_Level6</TileMatrixSet></TileMatrixSetLink></Layer>`;
const capabilities = overrides => `<Capabilities>${Object.entries(soil.SOIL_VIEWS).map(([view, spec]) => layer(spec.layer, overrides?.[view] ?? ["2026-09-25/2026-09-27/P1D"])).join("")}</Capabilities>`;

test("soil URL restoration rejects incomplete and malformed fields without throwing", () => {
  const invalid = new Set(["", "1|surface||", "1|surface|| ", "1|surface||NaN", "1|surface||Infinity", "1|surface||0.5|extra", "2|surface||0.5", "1|constructor||0.5", "1|__proto__||0.5", "1|surface|2026-02-30|0.5"]);
  for (const view of Object.keys(soil.SOIL_VIEWS)) for (const visible of ["0", "1"]) for (const day of ["", "2026-09-28"]) {
    const fields = [visible, view, day, "0.65"];
    for (let count = 0; count < 4; count++) invalid.add(fields.slice(0, count).join("|"));
  }
  for (const value of invalid) assert.deepEqual(soil.restoreSoilMapState(new URLSearchParams({ soil: value })), soil.DEFAULT_SOIL_MAP_STATE, value);
  assert.deepEqual(soil.restoreSoilMapState(new URLSearchParams()), soil.DEFAULT_SOIL_MAP_STATE);
});

test("the existing four-field soil URL format retains every view, visibility, day and bounded opacity", () => {
  for (const view of Object.keys(soil.SOIL_VIEWS)) for (const visible of [false, true]) for (const day of ["", "2015-03-31", "2024-02-29"]) {
    const expected = { visible, view, day, opacity: 0.73 }, params = new URLSearchParams();
    soil.serializeSoilMapState(params, expected);
    assert.deepEqual(soil.restoreSoilMapState(params), expected);
  }
  for (const [value, expected] of [["-1", 0], ["0", 0], ["1", 1], ["2", 1]]) {
    assert.equal(soil.restoreSoilMapState(new URLSearchParams({ soil: `1|root||${value}` })).opacity, expected);
  }
});

// Execute the actual complete page callback and its initialization/popstate
// registration. The renderer and public registries are empty fixtures; every
// provider dispatch is forbidden, and no browser/private state is read.
const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
const pageTree = ts.createSourceFile("page.tsx", page, ts.ScriptTarget.ES2022, true, ts.ScriptKind.TSX);
let restoreCallback, restoreEffect;
function findRestore(node) {
  if (ts.isVariableDeclaration(node) && node.name.getText(pageTree) === "restoreExplorerFromUrl") restoreCallback = node.initializer.arguments[0].getText(pageTree);
  if (ts.isCallExpression(node) && node.expression.getText(pageTree) === "useEffect" && node.arguments[0]?.getText(pageTree).includes("const handlePopState = () => restoreExplorerFromUrl();")) restoreEffect = node.arguments[0].getText(pageTree);
  ts.forEachChild(node, findRestore);
}
findRestore(pageTree); assert.ok(restoreCallback && restoreEffect);
const evaluateRestore = code => ts.transpileModule(`return (${code});`, { compilerOptions: { target: ts.ScriptTarget.ES2022 } }).outputText;
const restoreCode = evaluateRestore(restoreCallback), effectCode = evaluateRestore(restoreEffect);
function soilRestoreFixture(initialSoil, mapReady) {
  const state = {}, refs = {}, timers = new Map(), listeners = new Map(), jumps = []; let timerId = 0, providerCalls = 0;
  const denied = () => { providerCalls++; assert.fail("URL parsing must not dispatch a provider in this fixture"); };
  const map = { jumpTo: view => jumps.push(view), setMaxPitch() {}, isStyleLoaded: () => true };
  const window = { location: { search: new URLSearchParams({ soil: initialSoil, units: "metric", t: "2026", c: "-97,39" }).toString() }, history: { state: null },
    setTimeout(fn) { const id = ++timerId; timers.set(id, fn); return id; }, clearTimeout: id => timers.delete(id),
    addEventListener(type, fn) { assert.equal(type, "popstate"); listeners.set(type, fn); }, removeEventListener(type, fn) { assert.equal(listeners.get(type), fn); listeners.delete(type); },
  };
  const bindings = {
    window, URLSearchParams, Number, Object, Set, Date, Boolean, Math,
    explorerHistoryParams: search => new URLSearchParams(search), restoreTopic: () => "all",
    restoreDaylightView: () => ({ day: "2026-09-29", throughDay: "2026-09-29", instantMs: Date.parse("2026-09-29T12:00:00Z"), enabled: false, playing: false }),
    currentKansasCalendarDay: () => "2026-09-29", currentUtcDay: () => "2026-09-29",
    mapRef: { current: mapReady ? map : null }, KANSAS_VIEW: { center: [-98, 38], zoom: 6, bearing: 0, pitch: 0 },
    SUPPORTED_CONTEXT_BOUNDS: { west: -104.8, east: -92, south: 34.8, north: 42.2 },
    parseNumber: (value, fallback) => value === null || value.trim() === "" || !Number.isFinite(Number(value)) ? fallback : Number(value), clamp: (value, min, max) => Math.min(max, Math.max(min, value)),
    LAYER_REGISTRY: [], OFFICIAL_CONTEXT_SOURCES: [], defaultVisibility: {}, defaultOpacity: {}, defaultOfficialVisibility: {}, defaultOfficialOpacity: {}, defaultOrder: [],
    preferredContextIds: () => [], readContextPreference: () => null, restoreArchiveViewDays: () => ({}), restoreSoilMapState: soil.restoreSoilMapState,
    normalizeUsgsStationId: () => null, restoreStreamflowArchiveDay: () => null, KNOWN_TEMPORAL_FRAMES: new Set([1910, 2026]), OFFICIAL_CONTEXT_PRESENT_FRAME: 2026, TIME_STEPS: [1910, 2026], evidenceLabels: {},
    officialArchiveDaysRef: { current: {} }, officialRequestsRef: { current: new Map() }, officialPayloadsRef: { current: {} }, officialArchivePayloadsRef: { current: {} },
    applyProjectionNavigationLimits() {}, updateAnalysisAreaSource() {}, setDaylightMapLayer() {},
    loadOfficialArchiveDay: denied, refreshOfficialContext: denied, refreshNoaaRadarManifest: denied, refreshStreamflow: denied, refreshNoaaHydrologyNetwork: denied,
  };
  const scope = new Proxy(bindings, { has: () => true, get(target, key) {
    if (key === Symbol.unscopables) return undefined;
    if (Object.hasOwn(target, key)) return target[key];
    if (typeof key === "string" && key.startsWith("set")) return value => { state[key] = value; };
    if (typeof key === "string" && key.endsWith("Ref")) return refs[key] ??= { current: null };
    throw new Error(`Missing URL fixture binding: ${String(key)}`);
  } });
  const restore = new Function("scope", `with (scope) { ${restoreCode} }`)(scope);
  bindings.restoreExplorerFromUrl = restore;
  const cleanup = new Function("scope", `with (scope) { ${effectCode} }`)(scope)();
  return { state, refs, jumps,
    initialize() { assert.equal(timers.size, 1); const [id, fn] = [...timers][0]; timers.delete(id); fn(); },
    navigate(soilValue) { window.location.search = new URLSearchParams({ soil: soilValue, units: "imperial", t: "1910", c: "-96,37" }).toString(); listeners.get("popstate")(); },
    dispose() { cleanup(); assert.equal(timers.size, 0); assert.equal(listeners.size, 0); assert.equal(providerCalls, 0); },
  };
}

test("malformed soil links finish initialization and popstate restoration instead of leaving a partial map setup", () => {
  for (const mapReady of [false, true]) for (const value of ["1|surface|", "1|root|2026-09-28", "0|surface-uncertainty|", "1|root-uncertainty||bad"]) {
    const f = soilRestoreFixture(value, mapReady);
    f.initialize(); assert.deepEqual(f.state.setSoilMapState, soil.DEFAULT_SOIL_MAP_STATE);
    assert.equal(f.state.setLayerPreferencesReady, true); assert.equal(f.refs.explorerRestoredRef.current, true);
    assert.equal(f.state.setMeasureUnit, "metric"); assert.equal(f.state.setYear, 2026);
    assert.deepEqual(f.state.setView.center, [-97, 39]); assert.equal(f.jumps.length, Number(mapReady));
    f.navigate("1|root|2026-09-28|0.73"); assert.deepEqual(f.state.setSoilMapState, { visible: true, view: "root", day: "2026-09-28", opacity: 0.73 });
    f.state.setLayerPreferencesReady = false; f.refs.explorerRestoredRef.current = false;
    f.navigate(value); assert.deepEqual(f.state.setSoilMapState, soil.DEFAULT_SOIL_MAP_STATE);
    assert.equal(f.state.setLayerPreferencesReady, true); assert.equal(f.refs.explorerRestoredRef.current, true);
    assert.equal(f.state.setMeasureUnit, "imperial"); assert.equal(f.state.setYear, 1910); assert.deepEqual(f.state.setView.center, [-96, 37]);
    f.dispose();
  }
});

test("four fixed views share only exact available UTC days and preserve gaps", () => {
  const parsed = soil.parseSoilAvailability(capabilities({ root: ["2026-09-25/2026-09-25/P1D", "2026-09-27/2026-09-27/P1D"] }), now);
  assert.deepEqual(soil.commonSoilDays(parsed), ["2026-09-27", "2026-09-25"]);
  assert.equal(parsed.root.includes("2026-09-26"), false);
  assert.equal(Object.keys(soil.SOIL_VIEWS).length, 4);
  assert.equal(new Set(Object.values(soil.SOIL_VIEWS).map(view => view.layer)).size, 4);
  assert.match(soil.soilLegendUrl("root-uncertainty"), /Uncertainty/);
  assert.match(soil.soilLegendUrl("surface"), /Analyzed_Soil_Moisture_H/);
});

test("visual playback blends only neighboring UTC days and never bridges missing days", () => {
  assert.equal(soil.soilVisualTransition("2026-09-21", "2026-09-22", true), "adjacent-visual-blend");
  assert.equal(soil.soilVisualTransition("2026-09-22", "2026-09-21", true), "adjacent-visual-blend");
  assert.equal(soil.soilVisualTransition("2026-09-21", "2026-09-23", true), "gap-or-loop-reset");
  assert.equal(soil.soilVisualTransition("2026-09-27", "2026-09-14", true), "gap-or-loop-reset");
  assert.equal(soil.soilVisualTransition("2026-09-21", "2026-09-22", false), "gap-or-loop-reset");
  assert.deepEqual(soil.soilVisualOpacities("adjacent-visual-blend", 0, 0.7), [0.7, 0]);
  assert.deepEqual(soil.soilVisualOpacities("adjacent-visual-blend", 1, 0.7), [0.7, 0.7]);
  assert.deepEqual(soil.soilVisualOpacities("gap-or-loop-reset", 0.5, 0.7), [0, 0]);
  assert.deepEqual(soil.soilVisualOpacities("gap-or-loop-reset", 1, 0.7), [0, 0.7]);
});

test("provider-advertised daily history includes the full product archive without inventing gaps", () => {
  const parsed = soil.parseSoilAvailability(capabilities({
    surface: ["2015-03-30/2015-04-02/P1D", "2026-09-28/2026-10-02/P1D"],
    root: ["2015-03-31/2015-04-01/P1D", "2026-09-28/2026-09-29/P1D"],
    "surface-uncertainty": ["2015-03-31/2015-04-02/P1D", "2026-09-28/2026-09-29/P1D"],
    "root-uncertainty": ["2015-03-31/2015-04-02/P1D", "2026-09-28/2026-09-29/P1D"],
  }), now);
  assert.equal(parsed.surface[0], "2026-09-29");
  assert.equal(parsed.surface.at(-1), "2015-03-31");
  assert.equal(parsed.surface.includes("2015-03-30"), false);
  assert.equal(parsed.surface.includes("2026-09-30"), false);
  assert.deepEqual(soil.commonSoilDays(parsed), ["2026-09-29", "2026-09-28", "2015-04-01", "2015-03-31"]);
  assert.equal(soil.validSoilDay("2015-03-31", now), true);
  assert.equal(soil.validSoilDay("2015-03-30", now), false);
});

test("a long NASA daily range reaches early product days and leap days", () => {
  const parsed = soil.parseSoilAvailability(capabilities(Object.fromEntries(
    Object.keys(soil.SOIL_VIEWS).map(view => [view, ["2015-03-31/2026-09-29/P1D"]]),
  )), now);
  const days = soil.commonSoilDays(parsed);
  assert.equal(days[0], "2026-09-29");
  assert.equal(days.at(-1), "2015-03-31");
  assert.equal(days.includes("2020-02-29"), true);
  assert.ok(days.length > 4_000);
});

test("availability response declares daily display and native product boundaries", async () => {
  const response = await availabilityRoute.GET(new Request("https://example.test/api/soil-moisture/availability"));
  const value = await response.json();
  assert.equal(response.status, 200);
  assert.equal(value.displayCadence, "daily");
  assert.equal(value.displayFrameTimeUtc, "12:00");
  assert.match(value.nativeCadence, /3-hourly/);
  assert.equal(value.numericPixelsAvailable, false);
  assert.equal(value.role, "EXTERNAL_CONTEXT_ONLY");
  assert.deepEqual(value.coverageBoundsWgs84, [-180, -85.044, 180, 85.044]);
  assert.equal(value.latestCommonDay, "2026-09-28");
});

test("malformed provider time and missing layers fail closed", () => {
  assert.throws(() => soil.parseSoilAvailability(capabilities({ root: ["2026-09-25/2026-09-27/P2D"] }), now));
  assert.throws(() => soil.parseSoilAvailability(capabilities({ root: ["2026-02-30/2026-03-02/P1D"] }), now));
  assert.throws(() => soil.parseSoilAvailability("<Capabilities></Capabilities>", now));
  assert.equal(soil.validSoilDay("2026-02-30", now), false);
  assert.equal(soil.validSoilDay("2014-12-31", now), false);
  assert.equal(soil.validSoilDay("2026-09-30", now), false);
});

test("tile address allowlist rejects invalid view, day, duplicate query, and out of range coordinates", () => {
  const good = new URL("https://example.test/api/soil-moisture/tile?view=surface&day=2026-09-27&z=6&x=14&y=24");
  // Request parser accepts product-history dates; the route separately checks NASA availability.
  good.searchParams.set("day", "2015-03-31");
  assert.equal(server.parseTileRequest(good.href).view, "surface");
  for (const [key, value] of [["view", "other"], ["day", "2015-03-30"], ["x", "64"], ["z", "7"], ["y", "-1"]]) {
    const bad = new URL(good); bad.searchParams.set(key, value);
    assert.throws(() => server.parseTileRequest(bad.href), { code: "INVALID_TILE_REQUEST" });
  }
  const duplicate = new URL(good); duplicate.searchParams.append("view", "root");
  assert.throws(() => server.parseTileRequest(duplicate.href));
});

test("tile view selectors reject prototype names before any provider dispatch and retain all four fixed views", async () => {
  let availabilityCalls = 0;
  const tileCalls = [], bytes = Uint8Array.of(137, 80, 78, 71, 13, 10, 26, 10);
  const route = await compile("api/soil-moisture/tile/route", {
    "../../../soil-moisture-server": {
      ...server,
      soilAvailability: async () => { availabilityCalls++; return { value: { availableDays: ["2026-09-27"] } }; },
      soilTileBytes: async (...args) => { tileCalls.push(args); return bytes; },
    },
  });
  const request = view => new Request(`https://example.test/api/soil-moisture/tile?view=${view}&day=2026-09-27&z=6&x=14&y=24`);
  for (const view of ["constructor", "__proto__", "toString", "hasOwnProperty"]) {
    assert.throws(() => server.parseTileRequest(request(view).url), { code: "INVALID_TILE_REQUEST" });
    const response = await route.GET(request(view));
    assert.equal(response.status, 400);
    assert.equal((await response.json()).code, "INVALID_TILE_REQUEST");
    assert.equal(response.headers.get("cache-control"), "no-store");
  }
  assert.equal(availabilityCalls, 0);
  assert.deepEqual(tileCalls, []);
  for (const view of Object.keys(soil.SOIL_VIEWS)) {
    assert.equal(server.parseTileRequest(request(view).url).view, view);
    const response = await route.GET(request(view));
    assert.equal(response.status, 200);
    assert.equal(response.headers.get("content-type"), "image/png");
    assert.equal(response.headers.get("x-soil-source-day"), "2026-09-27");
    assert.deepEqual(new Uint8Array(await response.arrayBuffer()), bytes);
  }
  assert.equal(availabilityCalls, 4);
  assert.deepEqual(tileCalls, Object.keys(soil.SOIL_VIEWS).map(view => [view, "2026-09-27", 6, 14, 24]));
});

test("provider redirect and oversized responses are rejected before reading", async () => {
  const original = global.fetch;
  try {
    global.fetch = async () => new Response(null, { status: 302, headers: { Location: "https://other.test" } });
    await assert.rejects(server.boundedNasaFetch("https://gibs.earthdata.nasa.gov/test", "image/png", 100), { code: "NASA_REDIRECT_REJECTED" });
    global.fetch = async () => new Response("a", { headers: { "Content-Length": "101" } });
    await assert.rejects(server.boundedNasaFetch("https://gibs.earthdata.nasa.gov/test", "image/png", 100), { code: "NASA_RESPONSE_TOO_LARGE" });
  } finally { global.fetch = original; }
});

test("tile bytes reject false PNG content and oversized streamed body", async () => {
  const original = global.fetch;
  try {
    global.fetch = async () => new Response("not PNG", { headers: { "Content-Type": "image/png" } });
    await assert.rejects(server.soilTileBytes("surface", "2026-09-27", 6, 14, 24), { code: "NASA_INVALID_PNG" });
    const forged = new Uint8Array(33); forged.set([137,80,78,71,13,10,26,10], 0); forged.set([0,0,0,13,73,72,68,82], 8);
    global.fetch = async () => new Response(forged, { headers: { "Content-Type": "image/png" } });
    await assert.rejects(server.soilTileBytes("surface", "2026-09-27", 6, 14, 24), { code: "NASA_INVALID_PNG" });
    global.fetch = async () => new Response(new Uint8Array(1024 * 1024 + 1), { headers: { "Content-Type": "image/png" } });
    await assert.rejects(server.soilTileBytes("surface", "2026-09-27", 6, 14, 24), { code: "NASA_MALFORMED_OR_OVERSIZED" });
  } finally { global.fetch = original; }
});

const tilePng = size => {
  const bytes = new Uint8Array(size); bytes.set([137, 80, 78, 71, 13, 10, 26, 10]);
  const header = new DataView(bytes.buffer); header.setUint32(8, 13); bytes.set([73, 72, 68, 82], 12);
  header.setUint32(16, 256); header.setUint32(20, 256); return bytes;
};
const tile = () => server.soilTileBytes("surface", "2026-09-27", 6, 14, 24);

test("soil tiles stop at the streamed budget without awaiting cancellation", { timeout: 1000 }, async t => {
  let response;
  t.mock.method(globalThis, "fetch", async () => response);
  for (const contentLength of [undefined, "1"]) {
    let pulls = 0, canceled = 0;
    response = new Response(new ReadableStream({
      pull(controller) { pulls++; controller.enqueue(tilePng(256 * 1024)); },
      cancel() { canceled++; return new Promise(() => {}); },
    }, { highWaterMark: 0 }), { headers: { "Content-Type": "image/png", ...(contentLength ? { "Content-Length": contentLength } : {}) } });
    await assert.rejects(tile(), { code: "NASA_MALFORMED_OR_OVERSIZED", httpStatus: 502 });
    assert.equal(pulls, 5); assert.equal(canceled, 1); assert.equal(response.body.locked, false);
  }
});

test("soil tile success and invalid PNG failures release their readers", async t => {
  let response;
  t.mock.method(globalThis, "fetch", async () => response);
  for (const length of [33, 1024 * 1024]) {
    const bytes = tilePng(length);
    response = new Response(bytes, { headers: { "Content-Type": "image/png" } });
    assert.deepEqual(await tile(), bytes); assert.equal(response.body.locked, false);
  }
  response = new Response(tilePng(33).fill(0, 16, 20), { headers: { "Content-Type": "image/png" } });
  await assert.rejects(tile(), { code: "NASA_INVALID_PNG" }); assert.equal(response.body.locked, false);
  response = new Response(null, { headers: { "Content-Type": "image/png" } });
  await assert.rejects(tile(), { code: "NASA_MALFORMED_OR_OVERSIZED" });
});

test("NASA header and MIME rejections cancel their bodies without reading or following redirects", { timeout: 1000 }, async t => {
  let response;
  const calls = [];
  t.mock.method(globalThis, "fetch", async (input, init) => { calls.push({ input, init }); return response; });
  for (const [init, code, read] of [
    [{ status: 302, headers: { Location: "http://127.0.0.1/private" } }, "NASA_REDIRECT_REJECTED", () => tile()],
    [{ status: 503 }, "NASA_HTTP_ERROR", () => tile()],
    [{ headers: { "Content-Type": "image/png", "Content-Length": String(1024 * 1024 + 1) } }, "NASA_RESPONSE_TOO_LARGE", () => tile()],
    [{ headers: { "Content-Type": "text/html" } }, "NASA_UNEXPECTED_CONTENT", () => tile()],
    [{ headers: { "Content-Type": "text/html" } }, "NASA_UNEXPECTED_CONTENT", () => server.soilAvailability(true)],
  ]) {
    let pulls = 0, canceled = 0;
    response = new Response(new ReadableStream({ pull() { pulls++; }, cancel() { canceled++; return new Promise(() => {}); } }, { highWaterMark: 0 }), init);
    await assert.rejects(read(), { code, httpStatus: 502 });
    assert.equal(pulls, 0); assert.equal(canceled, 1); assert.equal(response.body.locked, false);
  }
  assert.equal(calls.length, 5);
  for (const { input, init } of calls) {
    assert.equal(new URL(input).origin, "https://gibs.earthdata.nasa.gov");
    assert.equal(init.redirect, "manual"); assert.equal(init.cache, "no-store");
    assert.match(init.headers.Accept, /image\/png|application\/xml/);
  }
});

test("NASA deadlines cancel stalled image and capabilities bodies after headers", { timeout: 1000 }, async t => {
  let controller, response, started, cancelReason;
  t.mock.method(AbortSignal, "timeout", delay => { assert.equal(delay, 12_000); return controller.signal; });
  t.mock.method(globalThis, "fetch", async (_input, init) => { assert.equal(init.signal, controller.signal); return response; });
  for (const kind of ["tile", "capabilities"]) {
    controller = new AbortController(); cancelReason = undefined;
    const reading = new Promise(resolve => { started = resolve; });
    let pulls = 0;
    response = new Response(new ReadableStream({
      pull(stream) { if (pulls++ === 0) stream.enqueue(kind === "tile" ? tilePng(33) : new TextEncoder().encode("<Capabilities>")); else started(); },
      cancel(reason) { cancelReason = reason; return new Promise(() => {}); },
    }, { highWaterMark: 0 }), { headers: { "Content-Type": kind === "tile" ? "image/png" : "application/xml" } });
    const pending = kind === "tile" ? tile() : server.soilAvailability(true);
    await reading; controller.abort(new DOMException("Fixture NASA deadline", "TimeoutError"));
    await assert.rejects(pending, { code: "NASA_TIMEOUT", httpStatus: 504 });
    assert.equal(cancelReason.name, "TimeoutError"); assert.equal(response.body.locked, false);
  }
});
