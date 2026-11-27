import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import { createElement } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import ts from "typescript";
import * as model from "../app/labs/daily-air-quality/air-model.mjs";
import { componentHarness, findNode, settle } from "./component-harness.mjs";

const route = new URL("../app/labs/daily-air-quality/", import.meta.url);
const manifest = JSON.parse(await readFile(new URL("snapshot-manifest.json", route), "utf8"));
const snapshot = model.validateAirSnapshot(JSON.parse(await readFile(new URL(`../public${manifest.snapshot.url}`, import.meta.url), "utf8")), manifest);
const source = (await readFile(new URL("daily-air-quality.jsx", route), "utf8"))
  .replace('import styles from "./daily-air-quality.module.css";', 'const styles = new Proxy({}, { get: (_target, name) => String(name) });')
  .replace('import Link from "next/link";', 'const Link = "a";')
  .replace('import ScienceNav from "../../science/science-nav";', 'const ScienceNav = () => null;');
let javascript = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022, jsx: ts.JsxEmit.ReactJSX }, fileName: "daily-air-quality.jsx" }).outputText;
for (const name of ["react", "react/jsx-runtime"]) javascript = javascript.replaceAll(`from "${name}"`, `from ${JSON.stringify(import.meta.resolve(name))}`);
for (const name of ["air-model.mjs", "snapshot-loader.mjs"]) javascript = javascript.replaceAll(`from "./${name}"`, `from ${JSON.stringify(new URL(name, route).href)}`);
const ui = await import(`data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`);
const render = (component, props) => renderToStaticMarkup(createElement(component, props));
const baseline = model.analyseAir(snapshot);
const allAnalyses = manifest.counties.flatMap((county) => model.YEARS.map((year) => model.analyseAir(snapshot, { countyId: county.id, year })));
const styles = new Proxy({}, { get: (_target, name) => String(name) });

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

test("analysis links validate every selection and preserve a real leap date and AQI zero threshold", () => {
  assert.deepEqual(ui.airSelection(manifest), { county: "20173", year: 2023, month: 0, threshold: 101, date: "2023-09-06" });
  const selection = ui.airSelection(manifest, "?county=20045&year=2024&month=2&threshold=0&date=2024-02-29");
  assert.deepEqual(selection, { county: "20045", year: 2024, month: 2, threshold: 0, date: "2024-02-29" });
  const link = new URL(ui.airLink("https://example.test/labs/daily-air-quality?unrelated=old#old", selection));
  assert.deepEqual(ui.airSelection(manifest, link.search), selection);
  assert.equal(link.hash, "");
  assert.equal(link.searchParams.has("unrelated"), false);
  assert.deepEqual(ui.airSelection(manifest, "?county=unknown&year=2026&month=13&threshold=Infinity&date=2023-02-30"), ui.airSelection(manifest));
  assert.equal(ui.airSelection(manifest, "?month=2&date=2023-09-06").date, "2023-02-06");
  assert.equal(ui.airSelection(manifest, "?threshold=500").threshold, 500);
  for (const invalid of ["-1", "501", "1.5", "", "NaN"]) assert.equal(ui.airSelection(manifest, `?threshold=${invalid}`).threshold, 101);
});

test("metrics render the real EPA peak and separate reported-day and calendar denominators", () => {
  assert.equal(baseline.thresholdDays, 5);
  assert.equal(baseline.reported, 365);
  assert.equal(baseline.peak.aqi, 157);
  const html = render(ui.AirMetrics, { analysis: baseline });
  assert.match(html, /Days with AQI ≥ 101/);
  assert.match(html, /1\.4% of 365 reported days/);
  assert.match(html, />157<\/strong>/);
  assert.match(html, /Sep 6 · PM2\.5/);
  assert.match(html, /0 dates without a report/);
  const empty = allAnalyses.find((analysis) => analysis.reported === 0);
  assert.ok(empty, "the real capture includes a county-year with no reported dates");
  const noReports = render(ui.AirMetrics, { analysis: empty });
  assert.match(noReports, /No reported days in this window/);
  assert.match(noReports, /No report · no peak inferred/);
  assert.doesNotMatch(noReports, /0% of 0/);
});

test("the calendar retains every selected date and uses text labels in addition to category colors", () => {
  for (const analysis of [baseline, allAnalyses.find((value) => value.reported > 0 && value.missing > 100)]) {
    const html = render(ui.AirCalendar, { analysis, selectedIndex: 0, onSelectDate() {} });
    assert.equal((html.match(/<button\b/g) ?? []).length, analysis.expected);
    assert.equal((html.match(/aria-pressed="true"/g) ?? []).length, 1);
    assert.equal((html.match(/class="calendarDay missingDay/g) ?? []).length, analysis.missing);
    assert.equal((html.match(/calendarDay meets/g) ?? []).length, analysis.thresholdDays);
    for (const category of model.CATEGORIES) assert.ok(html.includes(category));
    assert.match(html, /black corner marks AQI ≥ 101/);
    for (const day of analysis.days) {
      assert.ok(html.includes(`aria-label="${new Intl.DateTimeFormat("en-US", { timeZone: "UTC", month: "long", day: "numeric", year: "numeric" }).format(new Date(`${day.date}T12:00:00Z`))}: ${day.missing ? "no report" : `AQI ${day.aqi}, ${day.category}, ${day.parameter}`}`));
    }
  }
});

test("the inspector retains original row, site and AQI tokens and explains an actual missing date", () => {
  const selectedIndex = baseline.days.findIndex((day) => day.date === "2023-09-06");
  const day = baseline.days[selectedIndex];
  const html = render(ui.AirDayInspector, { analysis: baseline, selectedIndex, onSelectDate() {} });
  for (const token of [day.rawAqi, day.category, day.parameter, day.site, day.sourceRow.toLocaleString("en-US")]) assert.ok(html.includes(token), token);
  assert.match(html, /header is row 1/);
  assert.match(html, /value="2023-09-06"/);
  assert.match(html, /aria-label="Previous calendar day"/);
  const missingAnalysis = allAnalyses.find((analysis) => analysis.missing > 0);
  const missingIndex = missingAnalysis.days.findIndex((item) => item.missing);
  const missing = render(ui.AirDayInspector, { analysis: missingAnalysis, selectedIndex: missingIndex, onSelectDate() {} });
  assert.match(missing, /No report for this county and date/);
  assert.match(missing, /not AQI zero/);
  assert.doesNotMatch(missing, /class="recordFacts"/);
  const zeroAnalysis = allAnalyses.find((analysis) => analysis.days.some((item) => item.aqi === 0));
  assert.ok(zeroAnalysis, "the captured observations include reported AQI zero");
  const zero = render(ui.AirDayInspector, { analysis: zeroAnalysis, selectedIndex: zeroAnalysis.days.findIndex((item) => item.aqi === 0), onSelectDate() {} });
  assert.match(zero, /<strong>0<\/strong>/);
  assert.match(zero, /class="recordFacts"/);
  assert.doesNotMatch(zero, /No report for this county and date/);
});

test("native date input and change share validation while previous and next include unreported calendar days", () => {
  const selected = [];
  const inspector = ui.AirDayInspector({ analysis: baseline, selectedIndex: 0, onSelectDate: (date) => selected.push(date) });
  const input = findNode(inspector, (node) => node.type === "input");
  assert.equal(input.props.onInput, input.props.onChange);
  input.props.onInput({ currentTarget: { value: "2023-02-06" } });
  input.props.onChange({ currentTarget: { value: "2023-02-07" } });
  for (const value of ["", "2023-02-30", "2024-01-01"]) input.props.onInput({ currentTarget: { value } });
  findNode(inspector, (node) => node.props?.["aria-label"] === "Next calendar day").props.onClick();
  assert.deepEqual(selected, ["2023-02-06", "2023-02-07", "2023-01-02"]);
  assert.equal(findNode(inspector, (node) => node.props?.["aria-label"] === "Previous calendar day").props.disabled, true);
});

test("the timeline leaves real report gaps and retains isolated zero-valued observations", () => {
  const analysis = allAnalyses.find((value) => value.reported > 0 && value.missing > 100);
  const path = ui.airSeriesPath(analysis.days, (index) => index, (value) => value);
  const segments = analysis.days.filter((day, index) => !day.missing && (index === 0 || analysis.days[index - 1].missing)).length;
  assert.equal((path.match(/M/g) ?? []).length, segments);
  assert.doesNotMatch(path, /NaN|null|undefined/);
  const html = render(ui.AirTimeline, { analysis, selectedIndex: 0 });
  assert.equal((html.match(/class="missingMark"/g) ?? []).length, analysis.missing);
  assert.match(html, /Missing dates break the line/);
  assert.match(html, /inclusive AQI threshold of 101/);
});

test("phone axes use HTML text at the same projected ticks without changing the daily trace", () => {
  const html = render(ui.AirTimeline, { analysis: baseline, selectedIndex: 0 });
  const path = ui.airSeriesPath(baseline.days, (index) => 54 + index / (baseline.days.length - 1) * 904, (value) => 242 - value / 200 * 214);
  assert.ok(html.includes(`class="aqiLine" d="${path}"`), "the original daily trace and gaps are unchanged");
  assert.match(html, /preserveAspectRatio="none"/);
  const yAxis = html.match(/class="mobileYAxis" aria-hidden="true">([\s\S]*?)<\/div>/)?.[1];
  const xAxis = html.match(/class="mobileXAxis" aria-hidden="true">([\s\S]*?)<\/div>/)?.[1];
  assert.ok(yAxis && xAxis, "phone labels are independent of the SVG's scale");
  assert.match(yAxis, />AQI<\/span>/);
  for (const tick of [0, 40, 80, 120, 160, 200]) assert.ok(yAxis.includes(`>${tick}</span>`));
  for (const date of ["Jan 1", "Mar 1", "May 1", "Jul 1", "Sep 1", "Nov 1"]) assert.ok(xAxis.includes(`>${date}</span>`));
});

test("initial rendering is a true loading state with disabled exports and all six original sources", () => {
  const html = render(ui.default, { manifest });
  assert.match(html, /Reading the county AQI observations/);
  assert.match(html, /aria-busy="true"/);
  assert.match(html, /<button[^>]*disabled=""[^>]*>Download daily CSV/);
  assert.match(html, /<button[^>]*disabled=""[^>]*>Download analysis receipt/);
  assert.doesNotMatch(html, /class="metrics"/);
  for (const source of manifest.sources) { assert.ok(html.includes(source.url)); assert.ok(html.includes(source.sha256)); }
  assert.match(html, /href="\/labs\/heat-and-rain"/);
  assert.match(html, /href="https:\/\/www.airnow.gov\/"/);
  assert.match(html, /Scientific review and dataset admission remain pending/);
});

function viewHarness(loader, initial = "https://example.test/labs/daily-air-quality") {
  const current = new URL(initial), pushed = [], blobs = [], downloads = [];
  const window = { location: { href: current.href, search: current.search }, history: { state: null, pushState(_state, _unused, href) { pushed.push(href); window.location.href = href; window.location.search = new URL(href).search; } }, dispatchEvent() {}, addEventListener() {}, removeEventListener() {} };
  class ViewURL extends URL { static createObjectURL(blob) { blobs.push(blob); return "blob:test"; } static revokeObjectURL() {} }
  return componentHarness("app/labs/daily-air-quality/daily-air-quality.jsx", {
    "../../science/science-nav": { default: "science-nav" }, "next/link": { default: "a" }, "./air-model.mjs": model, "./snapshot-loader.mjs": { loadAirSnapshot: loader }, "./daily-air-quality.module.css": { default: styles },
  }, { URLSearchParams, URL: ViewURL, Blob, window, navigator: {}, document: { body: { appendChild() {} }, createElement() { return { click() { downloads.push(this.download); }, remove() {} }; } }, setTimeout(fn) { fn(); return 0; } }).then((harness) => ({ ...harness, window, pushed, blobs, downloads }));
}

test("the verified view persists controls in browser history and downloads exactly the chosen model analysis", async () => {
  const harness = await viewHarness(async () => snapshot);
  harness.render(harness.exports.default, { manifest }); harness.commit(); await settle();
  let tree = harness.render(harness.exports.default, { manifest });
  const presets = nodes(tree, (node) => node.type === "button" && node.props?.["aria-pressed"] !== undefined);
  presets.find((node) => node.props.children === "151 · Unhealthy or higher").props.onClick();
  assert.equal(harness.pushed.length, 1);
  assert.equal(new URL(harness.pushed[0]).searchParams.get("threshold"), "151");
  tree = harness.render(harness.exports.default, { manifest });
  const csv = findNode(tree, (node) => node.type === "button" && node.props.children === "Download daily CSV ↓");
  const receipt = findNode(tree, (node) => node.type === "button" && node.props.children === "Download analysis receipt ↓");
  assert.equal(csv.props.disabled, false);
  csv.props.onClick(); receipt.props.onClick();
  const selected = model.analyseAir(snapshot, { threshold: 151 });
  assert.equal(await harness.blobs[0].text(), model.airCsv(selected));
  assert.deepEqual(JSON.parse(await harness.blobs[1].text()), model.airReceipt(selected, manifest.snapshot, { inspectedDate: "2023-09-06" }));
  assert.equal(harness.downloads.length, 2);
  // useSyncExternalStore reads the restored browser URL on a popstate render.
  harness.window.location.search = "?county=20045&year=2024&month=2&threshold=0&date=2024-02-29";
  tree = harness.render(harness.exports.default, { manifest });
  const countySelect = findNode(tree, (node) => node.type === "select" && node.props.value === "20045");
  assert.ok(countySelect);
  assert.equal(findNode(tree, (node) => node.type === "input" && node.props.type === "number").props.value, 0);
  const bound = findNode(tree, (node) => typeof node.type === "function" && node.type.name === "AirDayInspector");
  assert.equal(bound.props.analysis.days[bound.props.selectedIndex].date, "2024-02-29");
  harness.dispose();
});

test("failed and stale snapshot states keep downloads disabled, expose retry and abort obsolete reads", async () => {
  const failure = await viewHarness(async () => { throw new Error("Integrity check failed"); });
  failure.render(failure.exports.default, { manifest }); failure.commit(); await settle();
  let tree = failure.render(failure.exports.default, { manifest });
  assert.ok(findNode(tree, (node) => node.props?.role === "alert"));
  assert.ok(findNode(tree, (node) => node.type === "button" && node.props.children === "Retry county AQI snapshot"));
  assert.equal(findNode(tree, (node) => node.type === "button" && node.props.children === "Download daily CSV ↓").props.disabled, true);
  failure.dispose();
  const pending = [];
  const stale = await viewHarness((_manifest, { signal }) => new Promise((resolve) => pending.push({ resolve, signal })));
  stale.render(stale.exports.default, { manifest }); stale.commit();
  const changedManifest = { ...manifest, snapshot: { ...manifest.snapshot, sha256: "0".repeat(64) } };
  stale.render(stale.exports.default, { manifest: changedManifest }); stale.commit();
  assert.equal(pending[0].signal.aborted, true);
  pending[0].resolve(snapshot); await settle();
  tree = stale.render(stale.exports.default, { manifest: changedManifest });
  assert.equal(findNode(tree, (node) => node.type === "button" && node.props.children === "Download analysis receipt ↓").props.disabled, true);
  assert.ok(findNode(tree, (node) => node.props?.role === "status"));
  stale.dispose();
  assert.equal(pending[1].signal.aborted, true);
});
