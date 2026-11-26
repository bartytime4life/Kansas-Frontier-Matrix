import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import { createElement } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import ts from "typescript";
import { analyseClimate, readingLabel, validateSnapshot } from "../app/labs/heat-and-rain/climate-model.mjs";

const route = new URL("../app/labs/heat-and-rain/", import.meta.url);
const manifest = JSON.parse(await readFile(new URL("snapshot-manifest.json", route), "utf8"));
// Compile only the assigned view. Use the actual model and captured observations;
// CSS and client routing are presentation adapters in this server-rendered check.
const source = (await readFile(new URL("heat-and-rain.jsx", route), "utf8"))
  .replace('import styles from "./heat-and-rain.module.css";', 'const styles = new Proxy({}, { get: (_target, name) => String(name) });')
  .replace('import Link from "next/link";', 'const Link = "a";');
let javascript = ts.transpileModule(source, {
  compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022, jsx: ts.JsxEmit.ReactJSX },
  fileName: "heat-and-rain.jsx",
}).outputText;
for (const name of ["react", "react/jsx-runtime"]) javascript = javascript.replaceAll(`from "${name}"`, `from ${JSON.stringify(import.meta.resolve(name))}`);
for (const name of ["climate-model.mjs", "snapshot-loader.mjs"]) javascript = javascript.replaceAll(`from "./${name}"`, `from ${JSON.stringify(new URL(name, route).href)}`);
const ui = await import(`data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`);
const render = (component, props) => renderToStaticMarkup(createElement(component, props));
const snapshots = await Promise.all(manifest.stations.map(async (descriptor) => {
  const snapshot = JSON.parse(await readFile(new URL(`../public${descriptor.url}`, import.meta.url), "utf8"));
  return { descriptor, analysis: analyseClimate(validateSnapshot(snapshot, descriptor), { year: 2025 }) };
}));

test("analysis links retain validated settings and reject unsupported station, dates, units and thresholds", () => {
  const baseline = ui.climateSelection(manifest);
  assert.match(manifest.stations.find((station) => station.id === baseline.station).name, /WICHITA/);
  const selection = ui.climateSelection(manifest, `?station=${manifest.stations[0].id}&year=2024&month=2&units=imperial&heat=35&wet=2`);
  assert.deepEqual(selection, { station: manifest.stations[0].id, year: 2024, month: 2, units: "imperial", heat: 35, wet: 2 });
  const link = new URL(ui.climateLink("https://example.test/labs/heat-and-rain?unrelated=value#old", selection));
  assert.deepEqual(ui.climateSelection(manifest, link.search), selection);
  assert.equal(link.hash, "");
  assert.equal(link.searchParams.has("unrelated"), false);
  assert.deepEqual(ui.climateSelection(manifest, "?station=unknown&year=2026&month=13&units=kelvin&heat=Infinity&wet=0"), baseline);
});

test("rendered metrics keep separate support denominators and precise Fahrenheit heat threshold", () => {
  for (const { analysis } of snapshots) {
    const html = render(ui.ClimateMetrics, { analysis, units: "imperial" });
    assert.ok(html.includes("Maximum ≥ 89.96 °F"));
    assert.ok(html.includes(`${analysis.valid.tmax}/${analysis.expected} days with valid maximum`));
    assert.ok(html.includes(`${analysis.valid.tmin}/${analysis.expected} days with valid minimum`));
    assert.ok(html.includes(`${analysis.valid.prcp}/${analysis.expected} days with quantified rain`));
    assert.ok(html.includes(`${analysis.traceDays} trace days`));
    assert.doesNotMatch(html, /total rainfall/i);
  }
});

test("day inspector renders actual zero, trace and quantified rain using the model element contract", () => {
  for (const { analysis } of snapshots) {
    const indices = [
      analysis.days.findIndex((day) => day.prcp.state === "trace"),
      analysis.days.findIndex((day) => day.prcp.value === 0),
      analysis.days.findIndex((day) => day.prcp.value > 0),
    ];
    for (const units of ["metric", "imperial"]) for (const selectedIndex of indices) {
      assert.ok(selectedIndex >= 0, "captured station has the observation state under review");
      const day = analysis.days[selectedIndex];
      const html = render(ui.ClimateDayInspector, { days: analysis.days, selectedIndex, units, onSelectDate() {} });
      for (const element of ["tmax", "tmin", "prcp"]) assert.ok(html.includes(readingLabel(day[element], element, units)));
      assert.ok(html.includes(`value="${day.date}"`));
      assert.match(html, /aria-label="Previous observation day"/);
      assert.match(html, /Raw .* · M .* · Q .* · S /);
    }
  }
});

test("both native date events select validated calendar dates through the same handler", () => {
  const { analysis } = snapshots.find(({ descriptor }) => /WICHITA/.test(descriptor.name));
  const selected = [];
  const element = ui.ClimateDayInspector({ days: analysis.days, selectedIndex: 0, units: "metric", onSelectDate: (date) => selected.push(date) });
  function findInput(node) {
    if (!node || typeof node !== "object") return null;
    if (node.type === "input") return node;
    const children = Array.isArray(node.props?.children) ? node.props.children : [node.props?.children];
    return children.map(findInput).find(Boolean);
  }
  const input = findInput(element);
  assert.equal(input.props.onInput, input.props.onChange, "input and change preserve identical validation");
  input.props.onInput({ currentTarget: { value: "2025-01-06" } });
  input.props.onChange({ currentTarget: { value: "2025-01-07" } });
  for (const value of ["", "2024-12-31", "2025-02-30", "2026-01-01"]) input.props.onInput({ currentTarget: { value } });
  assert.deepEqual(selected, ["2025-01-06", "2025-01-07"]);
});

test("rain chart distinguishes recorded zero from trace and frost chart labels the correct inequality", () => {
  const { analysis } = snapshots.find(({ descriptor }) => /WICHITA/.test(descriptor.name));
  const html = render(ui.ClimatePlot, { analysis, units: "metric", view: "rain", selectedIndex: 0 });
  assert.equal((html.match(/class="traceMark"/g) ?? []).length, analysis.traceDays);
  assert.equal((html.match(/class="zeroMark"/g) ?? []).length, analysis.days.filter((day) => day.prcp.value === 0).length);
  assert.equal((html.match(/class="rainBar"/g) ?? []).length, analysis.days.filter((day) => day.prcp.value > 0).length);
  const frost = render(ui.ClimatePlot, { analysis, units: "imperial", view: "frost", selectedIndex: 0 });
  assert.ok(frost.includes("Frost ≤ 32 °F"));
  assert.ok(frost.includes("Missing readings leave line gaps"));
  assert.doesNotMatch(frost, /class="gapKey"/);
  assert.doesNotMatch(frost, /Frost ≥/);
});

test("initial page is a truthful loading state and keeps analytical exports disabled", () => {
  const html = render(ui.default, { manifest });
  assert.match(html, /Reading WICHITA observations/);
  assert.match(html, /aria-busy="true"/);
  assert.match(html, /<button[^>]*disabled=""[^>]*>Download daily CSV/);
  assert.match(html, /<button[^>]*disabled=""[^>]*>Download analysis receipt/);
  assert.doesNotMatch(html, /class="metrics"/);
});
