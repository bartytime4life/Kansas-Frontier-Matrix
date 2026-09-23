import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { stripTypeScriptTypes } from "node:module";
import test from "node:test";

// Dependency-free decoder tests. Type stripping is execution, not type checking.
// Load the app-local candidate; the only rewrite supplies Node's explicit module URL.
const boundedText = await readFile(new URL("../app/bounded-json.ts", import.meta.url), "utf8");
const toModuleUrl = (source) => `data:text/javascript;base64,${Buffer.from(stripTypeScriptTypes(source, { mode: "strip" })).toString("base64")}`;
const boundedUrl = toModuleUrl(boundedText);
const decoderText = await readFile(new URL("../app/usgs-earthquake-response.ts", import.meta.url), "utf8");
assert.equal(decoderText.split('from "./bounded-json"').length, 2, "Expected exactly one bounded-reader import.");
const decoderUrl = toModuleUrl(decoderText.replace('from "./bounded-json"', `from ${JSON.stringify(boundedUrl)}`));
const { readBoundedJson } = await import(boundedUrl);
const { readUsgsEarthquakeResponse: decode } = await import(decoderUrl);
const limit = 1024;
const empty = { type: "FeatureCollection", metadata: { count: 0 }, features: [] };
const event = {
  type: "Feature", id: "synthetic-test-only",
  geometry: { type: "Point", coordinates: [-98.2, 38.4, 4] },
  properties: { time: 1770000000000, mag: 1.2, status: "automatic" },
};
const populated = { type: "FeatureCollection", metadata: { count: 1 }, features: [event] };
const jsonResponse = (value, init) => new Response(JSON.stringify(value), {
  headers: { "Content-Type": "application/json" }, ...init,
});

// Regression: reproduce the old, body-only parser's behavior without a network.
test("historical bounded reader rejects documented USGS 204 no-data", async () => {
  await assert.rejects(readBoundedJson(new Response(null, { status: 204 }), limit), /Missing JSON body/);
});
test("USGS-specific decoder normalizes 204 to zero observations", async () => {
  assert.deepEqual(await decode(new Response(null, { status: 204 }), limit), empty);
});
test("generic reader remains strict: other feeds do not gain a 204 fallback", async () => {
  await assert.rejects(readBoundedJson(new Response(null, { status: 204 }), limit));
});
test("valid 200 empty collection is preserved", async () => {
  assert.deepEqual(await decode(jsonResponse(empty), limit), empty);
});
test("valid 200 populated collection and provider metadata are preserved", async () => {
  assert.deepEqual(await decode(jsonResponse(populated), limit), populated);
});
test("decoder populated -> empty -> populated has no retained events (not a map test)", async () => {
  let decoded = await decode(jsonResponse(populated), limit);
  assert.equal(decoded.features.length, 1);
  decoded = await decode(new Response(null, { status: 204 }), limit);
  assert.equal(decoded.features.length, 0);
  decoded = await decode(jsonResponse(populated), limit);
  assert.deepEqual(decoded.features, [event]);
});
test("successive empty responses do not share mutable feature arrays", async () => {
  const first = await decode(new Response(null, { status: 204 }), limit);
  const second = await decode(new Response(null, { status: 204 }), limit);
  first.features.push(event);
  assert.deepEqual(second.features, []);
});
for (const status of [201, 206, 301, 302, 307, 308, 400, 401, 403, 404, 429, 500, 503]) {
  test(`HTTP ${status} is an error, never no observations`, async () => {
    await assert.rejects(decode(new Response("provider error", { status }), limit), new RegExp(`HTTP ${status}`));
  });
}
for (const [label, value] of [
  ["missing features", { type: "FeatureCollection" }],
  ["features is not an array", { type: "FeatureCollection", features: {} }],
  ["wrong GeoJSON type", { type: "Feature", features: [] }],
  ["null top-level body", null],
  ["array top-level body", []],
  ["provider error object", { error: "unavailable" }],
  ["null feature", { type: "FeatureCollection", features: [null] }],
  ["wrong feature type", { type: "FeatureCollection", features: [{ type: "Polygon" }] }],
]) {
  test(`malformed 200 (${label}) cannot become an empty success`, async () => {
    await assert.rejects(decode(jsonResponse(value), limit), /invalid GeoJSON FeatureCollection/);
  });
}
test("200 with no body is an error", async () => {
  await assert.rejects(decode(new Response(null), limit), /Missing JSON body/);
});
test("200 with empty text is an error", async () => {
  await assert.rejects(decode(new Response(""), limit), SyntaxError);
});
test("HTML authentication or error page is not a GeoJSON success", async () => {
  await assert.rejects(decode(new Response("<html>Sign in</html>"), limit), SyntaxError);
});
test("declared byte limit is preserved", async () => {
  await assert.rejects(decode(jsonResponse(empty, { headers: { "Content-Length": "2048" } }), limit), /byte limit/);
});
test("streamed byte limit is preserved without Content-Length", async () => {
  const bytes = new TextEncoder().encode(" ".repeat(limit + 1));
  const stream = new ReadableStream({ start(controller) { controller.enqueue(bytes); controller.close(); } });
  await assert.rejects(decode(new Response(stream), limit), /byte limit/);
});
test("invalid UTF-8 is rejected", async () => {
  await assert.rejects(decode(new Response(new Uint8Array([0xc3, 0x28])), limit), TypeError);
});
test("a broken response stream is an error, not no observations", async () => {
  const stream = new ReadableStream({ start(controller) { controller.error(new Error("fixture stream failure")); } });
  await assert.rejects(decode(new Response(stream), limit), /fixture stream failure/);
});
test("204 normalization performs no network request", async () => {
  const originalFetch = globalThis.fetch;
  let calls = 0;
  globalThis.fetch = () => { calls += 1; throw new Error("Network forbidden in decoder test"); };
  try {
    assert.deepEqual(await decode(new Response(null, { status: 204 }), limit), empty);
    assert.equal(calls, 0);
  } finally {
    globalThis.fetch = originalFetch;
  }
});
