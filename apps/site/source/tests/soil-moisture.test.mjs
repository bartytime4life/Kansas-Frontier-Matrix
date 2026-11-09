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
