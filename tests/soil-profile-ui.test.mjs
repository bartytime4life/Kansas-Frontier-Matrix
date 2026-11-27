import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import { createElement } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import ts from "typescript";
import { analyseSoil, soilReadingLabel, validateSoilSnapshot } from "../app/labs/soil-profile/soil-model.mjs";

const route = new URL("../app/labs/soil-profile/", import.meta.url);
const manifest = JSON.parse(await readFile(new URL("snapshot-manifest.json", route), "utf8"));
const source = (await readFile(new URL("soil-profile.jsx", route), "utf8"))
  .replace('import styles from "./soil-profile.module.css";', 'const styles = new Proxy({}, { get: (_target, name) => String(name) });')
  .replace('import Link from "next/link";', 'const Link = "a";')
  .replace('import ScienceNav from "../../science/science-nav";', 'const ScienceNav = () => null;');
let javascript = ts.transpileModule(source, {
  compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022, jsx: ts.JsxEmit.ReactJSX },
  fileName: "soil-profile.jsx",
}).outputText;
for (const name of ["react", "react/jsx-runtime"]) javascript = javascript.replaceAll(`from "${name}"`, `from ${JSON.stringify(import.meta.resolve(name))}`);
for (const name of ["soil-model.mjs", "snapshot-loader.mjs"]) javascript = javascript.replaceAll(`from "./${name}"`, `from ${JSON.stringify(new URL(name, route).href)}`);
const ui = await import(`data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`);
const render = (component, props) => renderToStaticMarkup(createElement(component, props));
const captured = await Promise.all(manifest.stations.map(async (descriptor) => {
  const snapshot = validateSoilSnapshot(JSON.parse(await readFile(new URL(`../public${descriptor.url}`, import.meta.url), "utf8")), descriptor);
  return { descriptor, snapshot, analysis: analyseSoil(snapshot) };
}));

test("share links retain the exact validated soil selection including the inspected date", () => {
  const baseline = ui.soilSelection(manifest);
  assert.equal(baseline.station, "03067");
  assert.equal(baseline.date, "2025-07-15");
  const selection = ui.soilSelection(manifest, "?station=53974&year=2024&month=2&depth=50&variable=temperature&date=2024-02-29");
  assert.deepEqual(selection, { station: "53974", year: 2024, month: 2, depth: 50, variable: "temperature", date: "2024-02-29" });
  const link = new URL(ui.soilLink("https://example.test/labs/soil-profile?unrelated=old#old", selection));
  assert.deepEqual(ui.soilSelection(manifest, link.search), selection);
  assert.equal(link.hash, "");
  assert.equal(link.searchParams.has("unrelated"), false);
  assert.deepEqual(ui.soilSelection(manifest, "?station=bad&year=2026&month=13&depth=30&variable=percent&date=2025-02-30"), baseline);
  assert.equal(ui.soilSelection(manifest, "?year=2024&month=2&date=2024-03-01").date, "2024-02-15");
});

test("headline metrics expose independent moisture and temperature denominators", () => {
  for (const { snapshot } of captured) for (const depth of [20, 50, 100]) {
    const analysis = analyseSoil(snapshot, { year: 2025, depth });
    const html = render(ui.SoilMetrics, { analysis, variable: "moisture", depth });
    assert.ok(html.includes(`${analysis.valid}/${analysis.expected} valid daily readings`));
    assert.ok(html.includes(`${analysis.temperatureValid}/${analysis.expected} valid temperatures`));
    assert.ok(html.includes("calendar dates · no gap filling"));
    assert.ok(html.includes(`Median at ${depth} cm`));
  }
  const oakley = captured.find(({ descriptor }) => descriptor.id === "03067");
  const html = render(ui.SoilMetrics, { analysis: oakley.analysis, variable: "moisture", depth: 20 });
  assert.match(html, /0\.236/);
  assert.match(html, /331\/365 valid daily readings/);
  assert.match(html, /364\/365 valid temperatures/);
});

test("soil series preserve reported zero and break the line on a missing observation", () => {
  const days = [0, null, 0.25].map((value) => ({ moisture: [{ value }] }));
  const path = ui.soilSeriesPath(days, "moisture", 0, (index) => index * 10, (value) => value * 100);
  assert.equal(path, "M0.00,0.00  M20.00,25.00");
  const { analysis } = captured.find(({ descriptor }) => descriptor.id === "03067");
  const html = render(ui.SoilPlot, { analysis, variable: "moisture", depth: 20, selectedIndex: 0, onSelectDepth() {} });
  assert.equal((html.match(/class="chosenLine"/g) ?? []).length, 1);
  assert.equal((html.match(/class="contextLine"/g) ?? []).length, 4);
  assert.ok(html.includes("missing readings leave line gaps"));
  assert.match(html, /role="group" aria-label="Choose highlighted depth"/);
});

test("selected-day profile retains source readings and datalogger version text", () => {
  const { snapshot } = captured.find(({ descriptor }) => descriptor.id === "03067");
  const analysis = analyseSoil(snapshot, { year: 2020 });
  const selectedIndex = analysis.days.findIndex((day) => day.version === "-9.000");
  assert.ok(selectedIndex >= 0, "capture includes the provider's missing version token");
  const day = analysis.days[selectedIndex];
  const html = render(ui.SoilDayInspector, { days: analysis.days, selectedIndex, variable: "moisture", depth: 20, onSelectDate() {}, onSelectDepth() {} });
  assert.ok(html.includes(`value="${day.date}"`));
  assert.ok(html.includes("Datalogger version -9.000"));
  for (const variable of ["moisture", "temperature"]) for (const reading of day[variable]) {
    assert.ok(html.includes(soilReadingLabel(reading, variable)));
    assert.ok(html.includes(`Raw ${reading.raw ?? "absent"}`));
  }
  assert.ok(html.includes("The soil between them is not measured here."));
  assert.ok(html.includes("Local standard day · UTC−6"));
});

test("both native date events accept only real dates in the current analysis", () => {
  const { analysis } = captured.find(({ descriptor }) => descriptor.id === "03067");
  const selected = [];
  const element = ui.SoilDayInspector({ days: analysis.days, selectedIndex: 0, variable: "moisture", depth: 20, onSelectDate: (date) => selected.push(date), onSelectDepth() {} });
  function findInput(node) {
    if (!node || typeof node !== "object") return null;
    if (node.type === "input") return node;
    const children = Array.isArray(node.props?.children) ? node.props.children : [node.props?.children];
    return children.map(findInput).find(Boolean);
  }
  const input = findInput(element);
  assert.equal(input.props.onInput, input.props.onChange);
  input.props.onInput({ currentTarget: { value: "2025-01-06" } });
  input.props.onChange({ currentTarget: { value: "2025-01-07" } });
  for (const value of ["", "2025-02-30", "2024-12-31", "2026-01-01"]) input.props.onInput({ currentTarget: { value } });
  assert.deepEqual(selected, ["2025-01-06", "2025-01-07"]);
});

test("depth coverage makes sparse deep moisture visible without implying no temperature record", () => {
  const { snapshot } = captured.find(({ descriptor }) => descriptor.id === "53974");
  const analysis = analyseSoil(snapshot, { year: 2025, depth: 50 });
  const html = render(ui.SoilCoverage, { analysis, variable: "moisture", depth: 50, onSelectDepth() {} });
  for (const row of analysis.depths) {
    assert.ok(html.includes(`${row.valid}/${analysis.expected}`));
    assert.ok(html.includes(`${row.temperatureValid}/${analysis.expected} valid temperatures`));
  }
  assert.match(html, /8\/365/);
  assert.match(html, /11\/365/);
  assert.ok(html.includes("A missing moisture reading alone does not identify frozen soil."));
});

test("initial page shows the selected station loading and keeps analytical exports disabled", () => {
  const html = render(ui.default, { manifest });
  assert.match(html, /Reading Oakley 19 SSW observations/);
  assert.match(html, /aria-busy="true"/);
  assert.match(html, /<button[^>]*disabled=""[^>]*>Download daily CSV/);
  assert.match(html, /<button[^>]*disabled=""[^>]*>Download analysis receipt/);
  assert.doesNotMatch(html, /class="metrics"/);
  assert.match(html, /href="\/science"/);
});
