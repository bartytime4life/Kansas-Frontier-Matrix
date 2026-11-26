import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import { createElement } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import ts from "typescript";
import { analyseDrought, validateDroughtSnapshot } from "../app/labs/county-drought/drought-model.mjs";

const route = new URL("../app/labs/county-drought/", import.meta.url);
const manifest = JSON.parse(await readFile(new URL("snapshot-manifest.json", route), "utf8"));
const snapshot = validateDroughtSnapshot(JSON.parse(await readFile(new URL(`../public${manifest.snapshot.url}`, import.meta.url), "utf8")), manifest);
const analysis = analyseDrought(snapshot);
const source = (await readFile(new URL("county-drought.jsx", route), "utf8"))
  .replace('import styles from "./county-drought.module.css";', 'const styles = new Proxy({}, { get: (_target, name) => String(name) });')
  .replace('import Link from "next/link";', 'const Link = "a";');

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

test("science entry offers three real routes and uses actual manifest scope counts", async () => {
  const scienceRoute = new URL("../app/science/", import.meta.url);
  const climate = JSON.parse(await readFile(new URL("../labs/heat-and-rain/snapshot-manifest.json", scienceRoute), "utf8"));
  const soil = JSON.parse(await readFile(new URL("../labs/soil-profile/snapshot-manifest.json", scienceRoute), "utf8"));
  const hubSource = (await readFile(new URL("page.tsx", scienceRoute), "utf8"))
    .replace('import Link from "next/link";', 'const Link = "a";')
    .replace('import styles from "./science.module.css";', 'const styles = new Proxy({}, { get: (_target, name) => String(name) });')
    .replace('import climate from "../labs/heat-and-rain/snapshot-manifest.json";', `const climate = ${JSON.stringify(climate)};`)
    .replace('import drought from "../labs/county-drought/snapshot-manifest.json";', `const drought = ${JSON.stringify(manifest)};`)
    .replace('import soil from "../labs/soil-profile/snapshot-manifest.json";', `const soil = ${JSON.stringify(soil)};`);
  const hub = await compile(hubSource, "page.tsx");
  const html = render(hub.default);
  for (const route of ["heat-and-rain", "county-drought", "soil-profile"]) assert.ok(html.includes(`href="/labs/${route}"`));
  assert.ok(html.includes(String(manifest.counties.length)));
  assert.ok(html.includes(String(manifest.snapshot.weeks)));
  assert.ok(html.includes(String(soil.depthsCm.length)));
  assert.ok(html.includes("not counts of valid measurements"));
  assert.doesNotMatch(html, /coming soon|unavailable/i);
  const tools = [...html.matchAll(/<article\b[^>]*>([\s\S]*?)<\/article>/g)];
  assert.equal(tools.length, 3);
  for (const [, tool] of tools) assert.doesNotMatch(tool, /href="\/labs"/);
  assert.match(html, /href="\/labs">Full research atlas/);
  assert.match(html, /href="\/research">Source discovery/);
});
