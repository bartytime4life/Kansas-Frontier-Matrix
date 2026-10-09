import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";
import { createRequire } from "node:module";
import { createElement } from "react";
import { renderToStaticMarkup } from "react-dom/server";

async function compile(name, imports = {}) {
  const source = await readFile(new URL(`../app/${name}.ts`, import.meta.url), "utf8");
  const code = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 } }).outputText;
  const compiled = { exports: {} };
  new Function("require", "module", "exports", code)(id => imports[id], compiled, compiled.exports);
  return compiled.exports;
}
const context = await compile("earth-engine-context");
const comparison = await compile("earth-engine-comparison", { "./earth-engine-context": context });
const hash = "a".repeat(64);
const index = { sha256: hash, count: 4, minX: 7, maxX: 8, minY: 12, maxY: 13 };
const manifest = (year, overrides = {}) => ({
  schema: "kfm-earth-engine-context/v1", setId: `ks-${year}-synthetic`, boundary: "Kansas · TIGER/2018/States · STATEFP 20", approvedAt: "2026-10-06T00:00:00Z", reviewState: "APPROVED_VISUAL_CONTEXT", admission: "NOT_ADMITTED", evidence: "NOT_CLAIM_EVIDENCE",
  layers: [{ id: "ee-chirps", status: "approved", source: "UCSB-CHG/CHIRPS/DAILY", period: `${year} calendar year`, resolutionMeters: 5566, attribution: "UCSB Climate Hazards Center · CHIRPS", limits: "Synthetic test only", legend: "Annual precipitation · mm", geotiffSha256: hash, reviewSha256: hash, tileIndexes: { 5: structuredClone(index) }, ...overrides }],
});
const png = Uint8Array.from([137,80,78,71,13,10,26,10,0,0,0,13,73,72,68,82,0,0,1,0,0,0,1,0]);
const tilePath = "/api/earth-engine-context/ks-2024-synthetic/ee-chirps/5/7/12.png";
const response = bytes => new Response(bytes, { headers: { "content-type": "image/png" } });

test("only unique approved annual products become choices; invalid, held, and ambiguous years stay unavailable", () => {
  const good = manifest(2024), older = manifest(2023), held = manifest(2022, { status: "held" });
  assert.deepEqual(comparison.comparisonYears([good, older, held], "ee-chirps"), [2023, 2024]);
  assert.deepEqual(comparison.comparisonYears([good, { ...good, setId: "ks-2024-another1" }, older], "ee-chirps"), [2023]);
  assert.deepEqual(comparison.comparisonYears([{ ...good, reviewState: "UNREVIEWED" }], "ee-chirps"), []);
  assert.deepEqual(comparison.comparisonYears([good], "ee-3dep"), []);
});

test("pairs require distinct installed years of one compatible product and a common prepared zoom", () => {
  const a = manifest(2023), b = manifest(2024);
  const pair = comparison.comparisonPair([a, b], "ee-chirps", 2023, 2024);
  assert.equal(pair.kind, "ready");
  assert.equal(pair.a.year, 2023); assert.equal(pair.b.year, 2024);
  assert.equal(pair.overviewZoom, 5);
  assert.equal(comparison.comparisonPair([a, b], "ee-chirps", 2023, 2023).kind, "unavailable");
  assert.equal(comparison.comparisonPair([a], "ee-chirps", 2023, 2024).kind, "unavailable");
  assert.equal(comparison.comparisonPair([a, b], "ee-cdl", 2023, 2024).kind, "unavailable");
  assert.equal(comparison.comparisonPair([a, manifest(2024, { legend: "Different units" })], "ee-chirps", 2023, 2024).kind, "unavailable");
  assert.equal(comparison.comparisonPair([a, manifest(2024, { tileIndexes: { 6: index } })], "ee-chirps", 2023, 2024).kind, "unavailable");
});

test("overview has a bounded common grid and tile URLs never substitute missing data", () => {
  const pair = comparison.comparisonPair([manifest(2023), manifest(2024)], "ee-chirps", 2023, 2024);
  assert.equal(comparison.comparisonTileUrl(pair.b, 5, 7, 12), tilePath);
  for (const coords of [[5, 9, 12], [5, 7, 14], [5, 7.5, 12], [6, 7, 12]]) assert.equal(comparison.comparisonTileUrl(pair.b, ...coords), null);
  const large = { ...index, count: 100, minX: 0, maxX: 20, minY: 0, maxY: 20 };
  const bounded = comparison.comparisonPair([manifest(2023, { tileIndexes: { 5: large } }), manifest(2024, { tileIndexes: { 5: large } })], "ee-chirps", 2023, 2024);
  assert.equal(bounded.kind, "ready"); assert.equal(bounded.overviewZoom, null);
});

test("low-only prepared zooms produce legal camera bounds and an initial zoom within them", () => {
  for (const zoom of [0, 1, 5, 18]) {
    const tileIndexes = { [zoom]: { sha256: hash, count: 1, minX: 0, maxX: 0, minY: 0, maxY: 0 } };
    const pair = comparison.comparisonPair([manifest(2023, { tileIndexes }), manifest(2024, { tileIndexes })], "ee-chirps", 2023, 2024);
    assert.equal(pair.kind, "ready");
    const camera = comparison.comparisonCameraOptions(pair);
    assert.equal(camera.minZoom, zoom); assert.ok(camera.minZoom <= camera.maxZoom);
    assert.ok(camera.zoom >= camera.minZoom && camera.zoom <= camera.maxZoom);
    if (zoom === 0) assert.deepEqual(camera, { minZoom: 0, maxZoom: 2, zoom: 2 });
  }
});

test("tile requests retain same-origin owner identity, bypass caches, reject redirects and refuse arbitrary hosts", async t => {
  t.mock.method(globalThis, "fetch", async (url, options) => {
    assert.equal(url, tilePath); assert.equal(options.credentials, "same-origin"); assert.equal(options.cache, "no-store"); assert.equal(options.redirect, "error");
    return response(png);
  });
  assert.deepEqual(new Uint8Array(await comparison.readComparisonTile(tilePath, new AbortController().signal)), png);
  await assert.rejects(comparison.readComparisonTile("https://example.org/tile.png", new AbortController().signal), /Invalid/);
});

test("HTML sign-in responses, missing tiles, invalid PNG and oversized bodies remain unavailable", async t => {
  let next = new Response("sign in", { headers: { "content-type": "text/html" } });
  t.mock.method(globalThis, "fetch", async () => next);
  const read = () => comparison.readComparisonTile(tilePath, new AbortController().signal);
  await assert.rejects(read(), /unavailable/);
  next = new Response(null, { status: 404 }); await assert.rejects(read(), /unavailable/);
  next = response(new Uint8Array(32)); await assert.rejects(read(), /not a PNG/);
  next = response(new Uint8Array(512 * 1024 + 1)); await assert.rejects(read(), /byte limit/);
  next = new Response(png, { headers: { "content-type": "image/png", "content-length": "524289" } }); await assert.rejects(read(), /unavailable/);
});

test("pair changes cancel in-flight bodies; late responses cannot deliver old tiles", async t => {
  let finish, canceled = false;
  t.mock.method(globalThis, "fetch", () => new Promise(resolve => { finish = resolve; }));
  const selected = new AbortController(), pending = comparison.readComparisonTile(tilePath, selected.signal);
  selected.abort(); finish(response(png));
  await assert.rejects(pending, { name: "AbortError" });
  t.mock.method(globalThis, "fetch", async () => new Response(new ReadableStream({ start(controller) { controller.enqueue(png); }, cancel() { canceled = true; } }), { headers: { "content-type": "image/png" } }));
  await assert.rejects(comparison.readComparisonTile(tilePath, new AbortController().signal, 15), { name: "TimeoutError" });
  assert.equal(canceled, true);
});

test("canceled selection never starts a request and stalled headers have a visible timeout path", async t => {
  let calls = 0;
  t.mock.method(globalThis, "fetch", (_url, { signal }) => {
    calls++;
    return new Promise((_resolve, reject) => signal.addEventListener("abort", () => reject(signal.reason), { once: true }));
  });
  const canceled = new AbortController(); canceled.abort();
  await assert.rejects(comparison.readComparisonTile(tilePath, canceled.signal), { name: "AbortError" }); assert.equal(calls, 0);
  await assert.rejects(comparison.readComparisonTile(tilePath, new AbortController().signal, 15), { name: "TimeoutError" });
});

test("camera synchronization is bidirectional, flat, nonrecursive, and detached on removal", () => {
  const map = () => ({
    listeners: new Set(), center: [0, 0], zoom: 5, jumps: 0,
    on(_event, fn) { this.listeners.add(fn); }, off(_event, fn) { this.listeners.delete(fn); },
    getCenter() { return this.center; }, getZoom() { return this.zoom; },
    jumpTo(camera) { this.jumps++; this.center = camera.center; this.zoom = camera.zoom; assert.equal(camera.bearing, 0); assert.equal(camera.pitch, 0); for (const fn of this.listeners) fn(); },
  });
  const a = map(), b = map(), stop = comparison.synchronizeComparisonMaps([a, b]);
  a.center = [-98, 38]; a.zoom = 8; for (const fn of a.listeners) fn();
  assert.deepEqual(b.center, a.center); assert.equal(b.zoom, 8); assert.equal(b.jumps, 1); assert.equal(a.jumps, 0);
  b.center = [-100, 39]; b.zoom = 9; for (const fn of b.listeners) fn();
  assert.deepEqual(a.center, b.center); assert.equal(a.zoom, 9); assert.equal(a.jumps, 1);
  stop(); assert.equal(a.listeners.size, 0); assert.equal(b.listeners.size, 0);
});

const require = createRequire(import.meta.url);
const panelSource = await readFile(new URL("../app/earth-engine-comparison-panel.tsx", import.meta.url), "utf8");
const panelCode = ts.transpileModule(panelSource, { compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022, jsx: ts.JsxEmit.ReactJSX } }).outputText;
const panel = { exports: {} };
const datasets = await compile("earth-engine-data");
new Function("require", "module", "exports", panelCode)(id => ({
  "./earth-engine-context": context, "./earth-engine-data": datasets, "./earth-engine-comparison": comparison,
  "./maplibre-seam": {}, "./webgl-support": { webgl2Available: () => true }, "./earth-engine-comparison.module.css": { default: new Proxy({}, { get: (_target, key) => String(key) }) },
}[id] ?? require(id)), panel, panel.exports);
const render = manifests => renderToStaticMarkup(createElement(panel.exports.EarthEngineComparisonDialog, { manifests, loading: false, error: null, onClose() {} }));

test("rendered comparison exposes a native keyboard divider, alternative layout, independent dates and limits", () => {
  const html = render([manifest(2023), manifest(2024)]);
  assert.match(html, /<dialog[^>]+aria-labelledby=/);
  assert.match(html, /type="range"[^>]+min="0"[^>]+max="100"[^>]+step="1"/);
  assert.match(html, /aria-label="Comparison divider"/);
  assert.match(html, /aria-valuetext="Year A covers 50 percent; year B covers 50 percent"/);
  assert.match(html, /Side by side/); assert.match(html, /Home and End show one complete year/);
  assert.match(html, /A · 2023 calendar year/); assert.match(html, /B · 2024 calendar year/);
  assert.equal((html.match(/Annual precipitation · mm/g) ?? []).length, 2);
  assert.match(html, /Synthetic test only/); assert.match(html, /Visual comparison only/);
  assert.match(html, /Use 2D images/); assert.match(html, /Retry tiles/);
});

test("rendered missing and incompatible pairs retain explanations without rendering a map or divider", () => {
  const missing = render([]);
  assert.match(missing, /installed years are required/); assert.match(missing, /No installed year/);
  assert.doesNotMatch(missing, /aria-label="Comparison divider"|class="stage"/);
  const invalid = render([manifest(2023), manifest(2024, { legend: "Incompatible legend" })]);
  assert.match(invalid, /different source, grid resolution, or legend/);
  assert.doesNotMatch(invalid, /class="stage"/);
});
