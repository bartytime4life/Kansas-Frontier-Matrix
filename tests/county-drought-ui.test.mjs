import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import { createElement } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import ts from "typescript";
import { analyseDrought, validateDroughtSnapshot, winterWheatSeason } from "../app/labs/county-drought/drought-model.mjs";
import * as model from "../app/labs/county-drought/drought-model.mjs";
import { componentHarness, findNode, settle } from "./component-harness.mjs";

const route = new URL("../app/labs/county-drought/", import.meta.url);
const manifest = JSON.parse(await readFile(new URL("snapshot-manifest.json", route), "utf8"));
const snapshot = validateDroughtSnapshot(JSON.parse(await readFile(new URL(`../public${manifest.snapshot.url}`, import.meta.url), "utf8")), manifest);
const analysis = analyseDrought(snapshot);
const source = (await readFile(new URL("county-drought.jsx", route), "utf8"))
  .replace('import styles from "./county-drought.module.css";', 'const styles = new Proxy({}, { get: (_target, name) => String(name) });')
  .replace('import Link from "next/link";', 'const Link = "a";')
  .replace('import ScienceNav from "../../science/science-nav";', 'const ScienceNav = () => null;');

function compile(source, fileName) {
  let javascript = ts.transpileModule(source, {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022, jsx: ts.JsxEmit.ReactJSX }, fileName,
  }).outputText;
  for (const name of ["react", "react/jsx-runtime"]) javascript = javascript.replaceAll(`from "${name}"`, `from ${JSON.stringify(import.meta.resolve(name))}`);
  for (const name of ["drought-model.mjs", "snapshot-loader.mjs"]) javascript = javascript.replaceAll(`from "./${name}"`, `from ${JSON.stringify(new URL(name, route).href)}`);
  return import(`data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`);
}
const ui = await compile(source, "county-drought.jsx");
const render = (component, props) => renderToStaticMarkup(createElement(component, props));

function findElement(node, type) {
  if (!node || typeof node !== "object") return null;
  if (node.type === type) return node;
  const children = Array.isArray(node.props?.children) ? node.props.children.flat() : [node.props?.children];
  return children.map((child) => findElement(child, type)).find(Boolean);
}

test("drought share state validates all settings and keeps the two counties distinct", () => {
  const defaults = ui.droughtSelection(manifest);
  assert.deepEqual(defaults, { countyId: "20055", compareId: "20161", fromYear: 2020, toYear: 2025, level: 2, threshold: 50 });
  const selection = ui.droughtSelection(manifest, "?county=20001&compare=20003&from=2022&to=2024&level=4&threshold=12.5");
  assert.deepEqual(selection, { countyId: "20001", compareId: "20003", fromYear: 2022, toYear: 2024, level: 4, threshold: 12.5 });
  const link = new URL(ui.droughtLink("https://example.test/labs/county-drought?old=value#old", selection));
  assert.deepEqual(ui.droughtSelection(manifest, link.search), selection);
  assert.equal(link.hash, "");
  assert.equal(link.searchParams.has("old"), false);
  const minimumThreshold = { ...defaults, threshold: 0.01 };
  assert.deepEqual(ui.droughtSelection(manifest, new URL(ui.droughtLink("https://example.test/labs/county-drought", minimumThreshold)).search), minimumThreshold);
  for (const threshold of ["1e-7", "0.001", "50.001", "100.01"]) assert.equal(ui.droughtSelection(manifest, `?threshold=${threshold}`).threshold, 50);
  assert.deepEqual(ui.droughtSelection(manifest, "?county=unknown&compare=20055&from=2026&to=2019&level=0&threshold=0"), defaults);
  const reversed = ui.droughtSelection(manifest, "?county=20161&compare=20161&from=2025&to=2020");
  assert.notEqual(reversed.countyId, reversed.compareId);
  assert.deepEqual([reversed.fromYear, reversed.toYear], [2020, 2025]);
});

test("area thresholds preserve source precision without silently rounding accepted values", () => {
  for (const value of [0.01, 0.29, 12.34, 50, 100]) assert.equal(ui.validDroughtThreshold(value), true);
  for (const value of [0, 0.0000001, 0.001, 12.345, 100.01, NaN, Infinity]) assert.equal(ui.validDroughtThreshold(value), false);
  const selection = ui.droughtSelection(manifest, "?threshold=12.34");
  assert.deepEqual(ui.droughtSelection(manifest, new URL(ui.droughtLink("https://example.test/labs/county-drought", selection)).search), selection);
});

test("a copied drought view carries only a Tuesday assessment within its selected years", () => {
  const search = "?county=20177&compare=20055&from=2024&to=2024&date=2024-06-04";
  const selection = ui.droughtSelection(manifest, search);
  const link = new URL(ui.droughtLink("https://example.test/labs/county-drought", selection));
  assert.equal(link.searchParams.get("date"), "2024-06-04");
  assert.equal(ui.droughtSelection(manifest, link.search).date, "2024-06-04");
  for (const date of ["2024-06-05", "2023-06-06", "2024-02-30", "2024-06-04&date=2024-06-11"]) {
    assert.equal(ui.droughtSelection(manifest, search.replace("2024-06-04", date)).date, undefined);
  }
  assert.equal(new URL(ui.droughtLink("https://example.test/labs/county-drought", { ...selection, fromYear: 2025, toYear: 2025 })).searchParams.has("date"), false);
});

test("assessment stepping, copying, and Back preserve the inspected week without rerunning the analysis", async t => {
  const entries = ["https://example.test/labs/county-drought?from=2024&to=2024&date=2024-06-04"];
  const window = new EventTarget();
  window.location = new URL(entries[0]);
  window.history = {
    state: null,
    pushState(_state, _title, href) { entries.push(href); window.location = new URL(href); },
    replaceState(_state, _title, href) { entries[entries.length - 1] = href; window.location = new URL(href); },
  };
  let analyses = 0, shared;
  const harness = await componentHarness("app/labs/county-drought/county-drought.jsx", {
    "next/link": { default: "a" },
    "../../science/science-nav": { default: "science-nav" },
    "./snapshot-loader.mjs": { loadDroughtSnapshot: async () => snapshot },
    "./drought-model.mjs": { ...model, analyseDrought(...args) { analyses += 1; return analyseDrought(...args); } },
    "./county-drought.module.css": { default: {} },
  }, { window, URLSearchParams, navigator: { clipboard: { async writeText(href) { shared = href; } } } });
  t.after(() => harness.dispose());
  function draw() { const tree = harness.render(harness.exports.default, { manifest }); harness.commit(); return tree; }
  function inspector(tree) { return findNode(tree, node => node.type === harness.exports.DroughtInspector).props; }
  function inspected(tree) { const panel = inspector(tree); return panel.analysis.primary.weeks[panel.selectedIndex].date; }
  draw(); await settle();
  assert.equal(inspected(draw()), "2024-06-04");
  inspector(draw()).onSelectDate("2024-06-11");
  const next = draw();
  assert.equal(inspected(next), "2024-06-11");
  assert.equal(analyses, 1);
  assert.equal(entries.length, 1);
  const share = findNode(next, node => node.type === "button" && node.props.children === "Copy comparison link ↗");
  await share.props.onClick();
  assert.equal(new URL(shared).searchParams.get("date"), "2024-06-11");

  const county = findNode(next, node => node.type === "select" && node.props.value === "20055");
  county.props.onChange({ currentTarget: { value: "20177" } });
  const changed = draw();
  assert.equal(inspector(changed).analysis.primary.id, "20177");
  assert.equal(inspected(changed), "2024-06-11");
  assert.equal(entries.length, 2);
  window.location = new URL(entries[0]);
  window.dispatchEvent(new Event("popstate"));
  assert.equal(inspector(draw()).analysis.primary.id, "20055");
  assert.equal(inspected(draw()), "2024-06-11");
});

test("comparison metrics render actual county support and distinguish the DSCI scale", () => {
  const html = render(ui.DroughtMetrics, { analysis });
  assert.ok(html.includes(analysis.primary.name));
  assert.ok(html.includes(analysis.comparison.name));
  assert.ok(html.includes(`${analysis.primary.valid}/${analysis.primary.expected} assessments reported`));
  assert.ok(html.includes(`${analysis.comparison.valid}/${analysis.comparison.expected} assessments reported`));
  assert.ok(html.includes(`<strong>${analysis.primary.thresholdWeeks}</strong>`));
  assert.ok(html.includes(`<strong>${analysis.comparison.thresholdWeeks}</strong>`));
  assert.ok(html.includes("index points · 0–500"));
  assert.doesNotMatch(html, /residents affected|drought days/);
});

test("the selected assessment readout retains reported zero area and exclusive category values", () => {
  const selectedIndex = analysis.primary.weeks.findIndex((week) => week.categories.some((value) => value === 0));
  assert.ok(selectedIndex >= 0);
  const html = render(ui.DroughtInspector, { analysis, selectedIndex, onSelectDate() {} });
  assert.ok(html.includes("0%"), "reported zero stays quantified");
  assert.ok(html.includes("exclusive county-area percentages"));
  assert.ok(html.includes("D2+ cumulative area"));
  assert.ok(html.includes(`value="${analysis.primary.weeks[selectedIndex].date}" selected=""`));
  assert.match(html, /aria-label="Previous Tuesday assessment"/);
  assert.match(html, /aria-label="Next Tuesday assessment"/);
  const selected = [];
  const element = ui.DroughtInspector({ analysis, selectedIndex: 0, onSelectDate: (date) => selected.push(date) });
  const select = findElement(element, "select");
  select.props.onChange({ currentTarget: { value: analysis.primary.weeks[5].date } });
  select.props.onChange({ currentTarget: { value: "2025-01-01" } });
  assert.deepEqual(selected, [analysis.primary.weeks[5].date]);
});

test("the severity strip uses exclusive shares rather than stacking cumulative percentages", () => {
  const html = render(ui.DroughtChart, { analysis, selectedIndex: 0 });
  assert.ok(html.includes("Threshold ≥ 50%"));
  assert.equal((html.match(/class="plotScroll"/g) ?? []).length, 1, "both plots share one horizontal scroll canvas");
  assert.match(html, /aria-label="County drought chart and severity strip, horizontally scrollable together"/);
  assert.ok(html.includes("Exclusive categories · approximately 100% per assessment, with source rounding"));
  for (let category = 0; category < 6; category++) assert.equal((html.match(new RegExp(`data-category="${category}"`, "g")) ?? []).length, analysis.primary.weeks.length);
  const dateIndex = analysis.primary.weeks.findIndex((week) => week.categories.filter((value) => value > 0).length >= 3);
  assert.ok(dateIndex >= 0);
  const week = analysis.primary.weeks[dateIndex];
  const focus = { ...analysis, primary: { ...analysis.primary, weeks: [week] }, comparison: { ...analysis.comparison, weeks: [analysis.comparison.weeks[dateIndex]] } };
  const focusHtml = render(ui.DroughtChart, { analysis: focus, selectedIndex: 0 });
  for (let category = 0; category < 6; category++) {
    const rectangle = focusHtml.match(new RegExp(`<rect[^>]+height="([^"]+)"[^>]+data-category="${category}"`));
    assert.ok(rectangle);
    assert.ok(Math.abs(Number(rectangle[1]) - 44 * week.categories[category] / 100) < 1e-9);
  }
});

test("missing assessments break lines and keep missing values visible in the inspector", () => {
  // Remove an actual assessment; no observations or numeric weather values are fabricated.
  const weeks = analysis.primary.weeks.slice(0, 3).map((week, index) => index === 1 ? { ...week, missing: true, share: null, categories: null, dsci: null } : week);
  const path = ui.droughtSharePath(weeks, (index) => index, (value) => value);
  assert.equal((path.match(/M/g) ?? []).length, 2);
  assert.doesNotMatch(path, /NaN|null/);
  const masked = { ...analysis, primary: { ...analysis.primary, weeks }, comparison: { ...analysis.comparison, weeks: analysis.comparison.weeks.slice(0, 3) } };
  const html = render(ui.DroughtInspector, { analysis: masked, selectedIndex: 1, onSelectDate() {} });
  assert.equal((html.match(/<td>Missing<\/td>/g) ?? []).length, 8);
});

test("observed-run labels distinguish window clipping and missing boundaries", () => {
  const run = analysis.primary.longestRun;
  assert.match(ui.droughtRunNote(run), /Consecutive observed Tuesday assessments/);
  assert.match(ui.droughtRunNote({ ...run, leftBoundary: "window" }), /may extend beyond/);
  assert.match(ui.droughtRunNote({ ...run, rightBoundary: "missing" }), /full episode length is unknown/);
});

test("loading and retry states keep comparison exports and share unavailable until data is ready", () => {
  const html = render(ui.default, { manifest });
  assert.match(html, /Reading Kansas county assessments/);
  assert.match(html, /aria-busy="true"/);
  assert.ok(html.includes('<label for="drought-threshold">County area threshold (%)</label>'));
  for (const label of ["Copy comparison link", "Download comparison CSV", "Download analysis receipt"]) assert.match(html, new RegExp(`<button[^>]*disabled=""[^>]*>${label}`));
  const element = ui.DroughtLoadState({ error: "Integrity check failed.", onRetry() {} });
  const errorHtml = renderToStaticMarkup(element);
  assert.match(errorHtml, /role="alert"/);
  assert.match(errorHtml, /Integrity check failed/);
  assert.match(errorHtml, /Retry drought snapshot/);
});

test("winter wheat replay crosses the calendar boundary and counts real assessments in the window", () => {
  const first = winterWheatSeason(snapshot, "20055", 2022);
  const second = winterWheatSeason(snapshot, "20055", 2023);
  assert.deepEqual([first.from, first.through, first.thresholdWeeks, first.reported, first.expected], ["2021-09-01", "2022-07-31", 20, 47, 47]);
  assert.deepEqual([second.from, second.through, second.thresholdWeeks, second.reported, second.expected], ["2022-09-01", "2023-07-31", 46, 47, 47]);
  assert.deepEqual(first.months.map((month) => month.label), ["Sep", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"]);
  assert.equal(second.months.reduce((total, month) => total + month.thresholdWeeks, 0), second.thresholdWeeks);
  assert.throws(() => winterWheatSeason(snapshot, "20055", 2020), /full calendar coverage/);
  assert.throws(() => winterWheatSeason(snapshot, "20000", 2024), /Kansas county/);
});

test("winter wheat replay treats missing assessments separately from observed zeros", () => {
  const actual = winterWheatSeason(snapshot, "20055", 2021);
  assert.equal(actual.thresholdWeeks, 0);
  assert.equal(actual.peakShare, 0);
  const masked = { ...snapshot, counties: snapshot.counties.map((county) => county.id === "20055" ? {
    ...county,
    values: county.values.map((value, index) => snapshot.weeks[index] >= actual.from && snapshot.weeks[index] <= actual.through ? null : value),
  } : county) };
  const missing = winterWheatSeason(masked, "20055", 2021);
  assert.equal(missing.expected, actual.expected);
  assert.equal(missing.reported, 0);
  assert.equal(missing.thresholdWeeks, null);
  assert.equal(missing.peakShare, null);
  assert.ok(missing.months.every((month) => month.thresholdWeeks === null && month.expected > 0));
});

test("winter wheat panel exposes distinct harvest years, reported support and official context", () => {
  const county = manifest.counties.find((entry) => entry.id === "20055");
  const html = render(ui.WinterWheatReplay, { county, snapshot, loading: false });
  assert.match(html, /Winter wheat drought replay/);
  assert.match(html, /Finney County/);
  assert.match(html, /2021-09-01/);
  assert.match(html, /2023-07-31/);
  assert.match(html, /<dd>20<\/dd>/);
  assert.match(html, /<dd>46<\/dd>/);
  assert.match(html, /47\/47/);
  assert.match(html, /no local copy of USDA yield, acreage or loss records/);
  for (const agency of ["nass", "fsa", "rma"]) assert.match(html, new RegExp(`href="https://www\\.${agency}\\.usda\\.gov/`));
  const waiting = render(ui.WinterWheatReplay, { county, snapshot: null, loading: true });
  assert.match(waiting, /Waiting for the verified county snapshot/);
  assert.doesNotMatch(waiting, /Peak D2\+ county area/);
});

test("science directory exposes the five lab routes and real manifest coverage", async () => {
  const dir = new URL("../app/science/", import.meta.url);
  const { nativeScienceDirectory } = await import(new URL("science-directory.mjs", dir));
  const index = async (lab) => JSON.parse(await readFile(new URL(`../labs/${lab}/snapshot-manifest.json`, dir), "utf8"));
  const [climate, drought, soil, air, sunlight] = await Promise.all(["heat-and-rain", "county-drought", "soil-profile", "daily-air-quality", "sunlight-and-sky"].map(index));
  const tools = nativeScienceDirectory({ climate, drought, soil, air, sunlight });
  for (const lab of ["heat-and-rain", "county-drought", "soil-profile", "daily-air-quality", "sunlight-and-sky"]) {
    assert.ok(tools.some(tool => tool.href === `/labs/${lab}`));
    const page = await readFile(new URL(`../labs/${lab}/page.tsx`, dir), "utf8");
    assert.match(page, /export default/);
  }
  assert.ok(tools.some(tool => tool.href === "/science/compare"));
  assert.match(tools.find(tool => tool.id === "drought").coverage, new RegExp(`${drought.counties.length} counties.*${drought.snapshot.weeks} weekly assessments`));
  assert.match(tools.find(tool => tool.id === "soil").coverage, new RegExp(`${soil.depthsCm.length} depths`));
  assert.match(tools.find(tool => tool.id === "air").coverage, new RegExp(`${air.counties.length} reporting counties`));
  assert.match(tools.find(tool => tool.id === "sunlight").coverage, new RegExp(`${sunlight.points.length} query points`));
  assert.match(await readFile(new URL("page.tsx", dir), "utf8"), /<ScienceLauncher entries=\{entries\}/);
});
