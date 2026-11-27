import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { createHash } from "node:crypto";
import test from "node:test";
import { createElement } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import ts from "typescript";
import * as model from "../app/labs/sunlight-and-sky/sunlight-model.mjs";
import { componentHarness, findNode, settle } from "./component-harness.mjs";

const route = new URL("../app/labs/sunlight-and-sky/", import.meta.url);
const manifest = JSON.parse(await readFile(new URL("snapshot-manifest.json", route), "utf8"));
const snapshots = new Map(await Promise.all(manifest.points.map(async (descriptor) => {
  const snapshot = JSON.parse(await readFile(new URL(`../public${descriptor.url}`, import.meta.url), "utf8"));
  return [descriptor.id, model.validateSunlightSnapshot(snapshot, descriptor)];
})));
const source = (await readFile(new URL("sunlight-and-sky.jsx", route), "utf8"))
  .replace('import styles from "./sunlight-and-sky.module.css";', 'const styles = new Proxy({}, { get: (_target, name) => String(name) });')
  .replace('import Link from "next/link";', 'const Link = "a";')
  .replace('import ScienceNav from "../../science/science-nav";', 'const ScienceNav = () => null;');
let javascript = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022, jsx: ts.JsxEmit.ReactJSX }, fileName: "sunlight-and-sky.jsx" }).outputText;
for (const name of ["react", "react/jsx-runtime"]) javascript = javascript.replaceAll(`from "${name}"`, `from ${JSON.stringify(import.meta.resolve(name))}`);
for (const name of ["sunlight-model.mjs", "snapshot-loader.mjs"]) javascript = javascript.replaceAll(`from "./${name}"`, `from ${JSON.stringify(new URL(name, route).href)}`);
const ui = await import(`data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`);
const render = (component, props) => renderToStaticMarkup(createElement(component, props));
const baseline = model.analyseSunlight(snapshots.get("dodge-city"), snapshots.get("topeka"));
const styles = new Proxy({}, { get: (_target, name) => String(name) });

// Explicitly synthetic, in-memory fixtures cover zero, gaps and above-reference
// values absent from the real complete capture. They are never saved or shipped.
function syntheticSnapshot(id, overrides = {}) {
  const snapshot = structuredClone(snapshots.get(id));
  snapshot.source.sha256 = "f".repeat(64);
  for (const row of snapshot.records) { row.allSky = -999; row.clearSky = -999; Object.assign(row, overrides[row.date]); }
  const bytes = Buffer.from(JSON.stringify(snapshot));
  const sha256 = createHash("sha256").update(bytes).digest("hex");
  const descriptor = { ...manifest.points.find((point) => point.id === id), source: snapshot.source, sha256, bytes: bytes.length, url: `/science-data/sunlight/${id}-${sha256.slice(0, 16)}.json` };
  return model.validateSunlightSnapshot(snapshot, descriptor);
}
const syntheticPrimary = syntheticSnapshot("dodge-city", { "2025-01-01": { allSky: 0, clearSky: 1 }, "2025-01-03": { allSky: 4, clearSky: 3 }, "2025-01-05": { allSky: 2 } });
const syntheticComparison = syntheticSnapshot("topeka", { "2025-01-01": { allSky: 1, clearSky: 2 } });
const syntheticAnalysis = model.analyseSunlight(syntheticPrimary, syntheticComparison, { year: 2025, month: 1 });

function nodes(tree, predicate) {
  const found = [];
  function visit(node) {
    if (!node || typeof node !== "object") return;
    if (predicate(node)) found.push(node);
    for (const child of [node.props?.children].flat(Infinity)) visit(child);
  }
  visit(tree);
  return found;
}

test("sunlight links preserve validated places, same-point comparisons, leap dates and selection context", () => {
  assert.deepEqual(ui.sunlightSelection(manifest), { primary: "dodge-city", comparison: "topeka", year: 2025, month: 0, date: "2025-07-01" });
  const selection = ui.sunlightSelection(manifest, "?primary=wichita&comparison=wichita&year=2024&month=2&date=2024-02-29");
  assert.deepEqual(selection, { primary: "wichita", comparison: "wichita", year: 2024, month: 2, date: "2024-02-29" });
  const link = new URL(ui.sunlightLink("https://example.test/labs/sunlight-and-sky?unrelated=old#old", selection));
  assert.deepEqual(ui.sunlightSelection(manifest, link.search), selection);
  assert.equal(link.searchParams.has("unrelated"), false);
  assert.equal(link.hash, "");
  assert.deepEqual(ui.sunlightSelection(manifest, "?primary=unknown&comparison=other&year=2026&month=13&date=2025-02-30"), ui.sunlightSelection(manifest));
  assert.equal(ui.sunlightSelection(manifest, "?year=2024&month=2&date=2024-02-30").date, "2024-02-01");
  assert.equal(ui.sunlightSelection(manifest, "?year=2025&month=1&date=2025-07-01").date, "2025-01-01");
});

test("summary labels keep actual modeled means and per-area and common-date support distinct", () => {
  const html = render(ui.SunlightSummary, { analysis: baseline });
  for (const value of ["4.80", "4.30", "+0.50"]) assert.ok(html.includes(value));
  assert.equal((html.match(/365\/365 valid modeled days/g) ?? []).length, 2);
  assert.match(html, /Primary − comparison · 365\/365 common dates/);
  assert.match(html, /kWh\/m²\/day/);
  const sparse = render(ui.SunlightSummary, { analysis: syntheticAnalysis });
  assert.match(sparse, /3\/31 valid modeled days/);
  assert.match(sparse, /1\/31 valid modeled days/);
  assert.match(sparse, /1\/31 common dates/);
  const empty = model.analyseSunlight(syntheticPrimary, syntheticComparison, { year: 2025, month: 2 });
  const absent = render(ui.SunlightSummary, { analysis: empty });
  assert.match(absent, /0\/28 valid modeled days/);
  assert.doesNotMatch(absent, />0\.00<\/strong>/);
  const same = model.analyseSunlight(snapshots.get("dodge-city"), snapshots.get("dodge-city"));
  assert.match(render(ui.SunlightSummary, { analysis: same }), />0\.00<\/strong>/);
});

test("the trace keeps synthetic zero, isolated days, source gaps and all-sky above clear-sky without clipping", () => {
  const path = ui.sunlightSeriesPath(syntheticAnalysis.days, "primary", "allSky", (index) => index, (value) => value);
  assert.deepEqual(path.match(/[ML][\d.,]+/g), ["M0.00,0.00", "M2.00,4.00", "M4.00,2.00"]);
  const html = render(ui.SunlightPlot, { analysis: syntheticAnalysis, selectedIndex: 1 });
  assert.equal((html.match(/class="primaryLinePoint"/g) ?? []).length, 3);
  assert.equal((html.match(/class="comparisonLinePoint"/g) ?? []).length, 1);
  assert.match(html, /Unavailable values break each line/);
  assert.match(html, /not measured cloud effect or cloud percentage/);
  assert.match(html, /All-sky values above the reference remain unchanged/);
  assert.doesNotMatch(html, /NaN|Infinity/);
});

test("axis labels live outside the scaled SVG and the plot describes its actual selected calendar", async () => {
  const month = model.analyseSunlight(snapshots.get("dodge-city"), snapshots.get("topeka"), { year: 2024, month: 2 });
  const html = render(ui.SunlightPlot, { analysis: month, selectedIndex: 0 });
  assert.match(html, /class="yAxis" aria-hidden="true"/);
  assert.match(html, /class="xAxis" aria-hidden="true"/);
  assert.match(html, /2024-02-01 through 2024-02-29/);
  for (const date of ["Feb 1", "Feb 8", "Feb 15", "Feb 22", "Feb 29"]) assert.ok(html.includes(date));
  const css = await readFile(new URL("sunlight-and-sky.module.css", route), "utf8");
  assert.match(css, /\.yAxis > span, \.xAxis > span\s*\{[^}]*font: 12px\//);
});

test("date inspector renders exact actual source tokens and explains synthetic missing separately from zero", () => {
  const index = baseline.days.findIndex((day) => day.date === "2025-07-01");
  const actual = render(ui.SunlightDayInspector, { analysis: baseline, selectedIndex: index, onSelectDate() {} });
  for (const value of ["6.9461", "8.4046", "8.4658", "20250701", "ALLSKY_SFC_SW_DWN", "CLRSKY_SFC_SW_DWN"]) assert.ok(actual.includes(value), value);
  for (const side of ["primary", "comparison"]) assert.ok(actual.includes(baseline.sources[side].sha256));
  const zero = render(ui.SunlightDayInspector, { analysis: syntheticAnalysis, selectedIndex: 0, onSelectDate() {} });
  assert.match(zero, /<strong>0\.00<\/strong>/);
  assert.match(zero, /raw <code>0<\/code> · modeled/);
  const missing = render(ui.SunlightDayInspector, { analysis: syntheticAnalysis, selectedIndex: 1, onSelectDate() {} });
  assert.match(missing, /Unavailable/);
  assert.match(missing, /raw <code>-999<\/code> · missing/);
  assert.doesNotMatch(missing, /<strong>0\.00<\/strong>/);
});

test("native date controls validate real calendar dates and navigate through unavailable dates", () => {
  const chosen = [];
  const inspector = ui.SunlightDayInspector({ analysis: syntheticAnalysis, selectedIndex: 0, onSelectDate: (date) => chosen.push(date) });
  const input = findNode(inspector, (node) => node.type === "input");
  assert.equal(input.props.onInput, input.props.onChange);
  input.props.onInput({ currentTarget: { value: "2025-01-02" } });
  input.props.onChange({ currentTarget: { value: "2025-01-03" } });
  for (const value of ["", "2025-02-01", "2025-01-32"]) input.props.onInput({ currentTarget: { value } });
  findNode(inspector, (node) => node.props?.["aria-label"] === "Next calendar day").props.onClick();
  assert.deepEqual(chosen, ["2025-01-02", "2025-01-03", "2025-01-02"]);
  assert.equal(findNode(inspector, (node) => node.props?.["aria-label"] === "Previous calendar day").props.disabled, true);
});

test("monthly navigation retains the whole year while clearly selecting the filtered month", () => {
  const analysis = model.analyseSunlight(snapshots.get("dodge-city"), snapshots.get("topeka"), { year: 2024, month: 2 });
  const selected = [];
  const tree = ui.SunlightMonths({ analysis, onSelectMonth: (month) => selected.push(month) });
  const buttons = nodes(tree, (node) => node.type === "button");
  assert.equal(buttons.length, 13);
  assert.equal(buttons.filter((button) => button.props["aria-pressed"]).length, 1);
  buttons.find((button) => button.props["aria-label"]?.startsWith("Inspect February ")).props.onClick();
  buttons.find((button) => button.props.children === "Show full year").props.onClick();
  assert.deepEqual(selected, [2, 0]);
  const html = render(ui.SunlightMonths, { analysis, onSelectMonth() {} });
  for (const month of ["January", "February", "December"]) assert.ok(html.includes(month));
  assert.match(html, /29\/29 valid/);
  assert.match(html, /29\/29 common dates/);
});

test("initial loading keeps export controls disabled and preserves scientific distinctions and original source identities", () => {
  const html = render(ui.default, { manifest });
  assert.match(html, /Reading the modeled sunlight record/);
  assert.match(html, /aria-busy="true"/);
  assert.match(html, /<button[^>]*disabled=""[^>]*>Download daily CSV/);
  assert.match(html, /<button[^>]*disabled=""[^>]*>Download analysis receipt/);
  assert.match(html, /NASA Local Solar Time/);
  assert.match(html, /not civil CST\/CDT/);
  assert.match(html, /nominal 1° × 1° radiation grid/);
  assert.match(html, /not ground-station readings, sunlight hours or panel output/);
  assert.match(html, /monthly PRISM solar archive and calculated daylight/);
  assert.match(html, /Scientific review and dataset admission remain pending/);
  assert.ok(html.includes(manifest.points[0].source.sha256));
  assert.ok(html.includes(manifest.points[2].source.sha256));
});

async function viewHarness(loader, initial = "https://example.test/labs/sunlight-and-sky") {
  const current = new URL(initial), pushed = [], blobs = [], downloads = [];
  const window = { location: { href: current.href, search: current.search }, history: { state: null, pushState(_state, _unused, href) { pushed.push(href); window.location.href = href; window.location.search = new URL(href).search; } }, dispatchEvent() {}, addEventListener() {}, removeEventListener() {} };
  class ViewURL extends URL { static createObjectURL(blob) { blobs.push(blob); return "blob:test"; } static revokeObjectURL() {} }
  const harness = await componentHarness("app/labs/sunlight-and-sky/sunlight-and-sky.jsx", {
    "../../science/science-nav": { default: "science-nav" }, "next/link": { default: "a" }, "./sunlight-model.mjs": model, "./snapshot-loader.mjs": { loadSunlightSnapshot: loader }, "./sunlight-and-sky.module.css": { default: styles },
  }, { URLSearchParams, URL: ViewURL, Blob, window, navigator: {}, document: { body: { appendChild() {} }, createElement() { return { click() { downloads.push(this.download); }, remove() {} }; } }, setTimeout(fn) { fn(); return 0; } });
  return { ...harness, window, pushed, blobs, downloads };
}

test("controls persist browser history and exports bind the exact selected full leap-month analysis", async () => {
  const calls = [];
  const harness = await viewHarness(async (descriptor) => { calls.push(descriptor.id); return snapshots.get(descriptor.id); });
  harness.render(harness.exports.default, { manifest }); harness.commit(); await settle();
  let tree = harness.render(harness.exports.default, { manifest });
  findNode(tree, (node) => node.type === "select" && node.props.value === 0).props.onChange({ target: { value: "2" } });
  tree = harness.render(harness.exports.default, { manifest });
  findNode(tree, (node) => node.type === "select" && node.props.value === 2025).props.onChange({ target: { value: "2024" } });
  tree = harness.render(harness.exports.default, { manifest });
  assert.equal(harness.pushed.length, 2);
  assert.equal(new URL(harness.pushed[1]).searchParams.get("date"), "2024-02-01");
  const csv = findNode(tree, (node) => node.type === "button" && node.props.children === "Download daily CSV ↓");
  const receipt = findNode(tree, (node) => node.type === "button" && node.props.children === "Download analysis receipt ↓");
  assert.equal(csv.props.disabled, false);
  csv.props.onClick(); receipt.props.onClick();
  const analysis = model.analyseSunlight(snapshots.get("dodge-city"), snapshots.get("topeka"), { year: 2024, month: 2 });
  assert.equal(await harness.blobs[0].text(), model.sunlightCsv(analysis));
  const json = JSON.parse(await harness.blobs[1].text());
  const { uiContext, ...core } = json;
  assert.deepEqual(core, model.sunlightReceipt(analysis));
  assert.equal(uiContext.inspectedDate, "2024-02-01");
  assert.equal(json.selection.from, "2024-02-01");
  assert.equal(json.selection.to, "2024-02-29");
  assert.equal(harness.downloads[0], "kfm-sunlight-dodge-city-vs-topeka-2024-02.csv");
  assert.deepEqual(calls, ["dodge-city", "topeka"], "date-window changes reuse the current verified point pair");
  // A popstate render consumes the restored URL through useSyncExternalStore.
  harness.window.location.search = "?primary=dodge-city&comparison=topeka&year=2025&month=7&date=2025-07-15";
  tree = harness.render(harness.exports.default, { manifest });
  const inspector = findNode(tree, (node) => typeof node.type === "function" && node.type.name === "SunlightDayInspector");
  assert.equal(inspector.props.analysis.days[inspector.props.selectedIndex].date, "2025-07-15");
  harness.dispose();
});

test("same-point reads are deduplicated and clipboard failure offers a complete copyable link", async () => {
  const calls = [];
  const harness = await viewHarness(async (descriptor) => { calls.push(descriptor.id); return snapshots.get(descriptor.id); }, "https://example.test/labs/sunlight-and-sky?primary=wichita&comparison=wichita&year=2024&month=2&date=2024-02-29");
  harness.render(harness.exports.default, { manifest }); harness.commit(); await settle();
  let tree = harness.render(harness.exports.default, { manifest });
  assert.deepEqual(calls, ["wichita"]);
  const summary = findNode(tree, (node) => typeof node.type === "function" && node.type.name === "SunlightSummary");
  assert.equal(summary.props.analysis.summary.paired.meanDifference, 0);
  await findNode(tree, (node) => node.type === "button" && node.props.children === "Copy analysis link ↗").props.onClick();
  tree = harness.render(harness.exports.default, { manifest });
  const fallback = findNode(tree, (node) => node.type === "input" && node.props.readOnly);
  assert.ok(fallback);
  assert.equal(new URL(fallback.props.value).searchParams.get("date"), "2024-02-29");
  harness.dispose();
});

test("failed and obsolete point-pair loads disable exports, expose retry and cancel both stale reads", async () => {
  const failure = await viewHarness(async () => { throw new Error("Integrity check failed"); });
  failure.render(failure.exports.default, { manifest }); failure.commit(); await settle();
  let tree = failure.render(failure.exports.default, { manifest });
  assert.ok(findNode(tree, (node) => node.props?.role === "alert"));
  assert.ok(findNode(tree, (node) => node.type === "button" && node.props.children === "Retry sunlight snapshots"));
  assert.equal(findNode(tree, (node) => node.type === "button" && node.props.children === "Download daily CSV ↓").props.disabled, true);
  failure.dispose();
  const reads = [];
  const stale = await viewHarness((descriptor, { signal }) => new Promise((resolve) => reads.push({ descriptor, signal, resolve })));
  stale.render(stale.exports.default, { manifest }); stale.commit();
  tree = stale.render(stale.exports.default, { manifest });
  findNode(tree, (node) => node.type === "select" && node.props.value === "dodge-city").props.onChange({ target: { value: "wichita" } });
  stale.render(stale.exports.default, { manifest }); stale.commit();
  assert.equal(reads[0].signal.aborted, true);
  assert.equal(reads[1].signal.aborted, true);
  reads[0].resolve(snapshots.get("dodge-city")); reads[1].resolve(snapshots.get("topeka")); await settle();
  tree = stale.render(stale.exports.default, { manifest });
  assert.equal(findNode(tree, (node) => node.type === "button" && node.props.children === "Download analysis receipt ↓").props.disabled, true);
  reads[2].resolve(snapshots.get("wichita")); reads[3].resolve(snapshots.get("topeka")); await settle();
  tree = stale.render(stale.exports.default, { manifest });
  assert.equal(findNode(tree, (node) => node.type === "button" && node.props.children === "Download analysis receipt ↓").props.disabled, false);
  stale.dispose();
  assert.equal(reads[2].signal.aborted, true);
  assert.equal(reads[3].signal.aborted, true);
});
