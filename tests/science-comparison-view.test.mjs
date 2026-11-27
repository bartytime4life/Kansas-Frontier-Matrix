import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import { createElement } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import ts from "typescript";

const view = new URL("../app/science/compare/comparison-view.tsx", import.meta.url);
const source = (await readFile(view, "utf8")).replace('import styles from "./comparison.module.css";',
  'const styles = new Proxy({}, { get: (_target, name) => String(name) });');
const js = ts.transpileModule(source, {
  fileName: "comparison-view.tsx", compilerOptions: {
    module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022, jsx: ts.JsxEmit.ReactJSX,
  },
}).outputText.replaceAll('from "react/jsx-runtime"', `from ${JSON.stringify(import.meta.resolve("react/jsx-runtime"))}`)
  .replace('from "./comparison-selection.mjs"', `from ${JSON.stringify(new URL('./comparison-selection.mjs', view).href)}`);
const { default: ComparisonView } = await import(`data:text/javascript;base64,${Buffer.from(js).toString("base64")}`);

const covered = (value, valid, expected) => ({ value, valid, expected });
const metric = {
  id: "climate", label: "Total precipitation", unit: "mm", supportUnit: "days",
  location: { name: "Topeka", scale: "station" }, method: "Measured liquid-equivalent precipitation.",
  limitation: "Totals cover quantified observations.", timeStandard: "NOAA station observation date",
  labPath: "/labs/heat-and-rain", documentation: "https://example.test/provider",
  attribution: "NOAA GHCN-Daily",
  display: { url: "/science-data/daily-climate/test.json", sha256: "a".repeat(64) },
  sources: [{ url: "https://example.test/source", year: 2024, capturedAt: "2026-11-25T12:00:00Z" }],
  annual: { selected: covered(10, 300, 366), comparison: covered(5, 330, 365) },
  monthly: Array.from({ length: 12 }, (_, i) => ({
    month: i + 1,
    selected: covered(i === 0 ? 0 : 10, 29, 31),
    comparison: i === 0 ? covered(null, 0, 31) : covered(5, 30, 31),
  })),
};
const report = {
  location: { id: "topeka", name: "Topeka and Shawnee County" },
  selection: { year: 2024, compareYear: 2023 }, series: [metric],
};
const rendered = renderToStaticMarkup(createElement(ComparisonView, { report }));

test("comparison graph shares metric scale and distinguishes a reported zero from missing data", () => {
  assert.match(rendered, /<figure[^>]+aria-hidden="true"/);
  assert.match(rendered, /data-year-role="selected" data-value-state="zero" style="--bar-height:0%"/);
  assert.match(rendered, /data-year-role="comparison" data-value-state="missing"/);
  assert.match(rendered, /data-year-role="selected" data-value-state="value" style="--bar-height:100%"/);
  assert.match(rendered, /data-year-role="comparison" data-value-state="value" style="--bar-height:50%"/);
  assert.equal(rendered.match(/class="monthLabel"/g)?.length, 12);
});

test("native month rows preserve year, value and support, with original provider links", () => {
  assert.match(rendered, /<summary>Monthly values and coverage<\/summary><table>/);
  assert.match(rendered, /<th scope="col">2024<\/th><th scope="col">2023<\/th>/);
  assert.match(rendered, /<th scope="row">January<\/th><td><span>0<\/span><small>29 of 31 days<\/small><\/td><td><span>Unavailable<\/span><small>0 of 31 days<\/small><\/td>/);
  assert.match(rendered, /300 of 366 days/);
  assert.match(rendered, /Original provider file · 2024/);
  assert.match(rendered, /Captured 2026-11-25/);
  assert.match(rendered, /Topeka · station/);
  assert.match(rendered, /Topeka and Shawnee County/);
  assert.match(rendered, /href="\/labs\/heat-and-rain\?station=USW00013996&amp;year=2024"/);
  const wichita = renderToStaticMarkup(createElement(ComparisonView, {
    report: { ...report, location: { id: "wichita", name: "Wichita and Sedgwick County" } },
  }));
  assert.match(wichita, /href="\/labs\/heat-and-rain\?station=USW00003928&amp;year=2024"/);
});

test("the report shows signed differences only where both years have full provider coverage", () => {
  const drought = {
    ...metric, id: "drought", label: "Peak severe drought coverage", unit: "%", supportUnit: "assessments",
    annual: { selected: covered(20, 53, 53), comparison: covered(35, 52, 52) },
    monthly: [
      { month: 1, selected: covered(0, 5, 5), comparison: covered(0, 4, 4) },
      { month: 2, selected: covered(20, 4, 4), comparison: covered(15, 5, 5) },
      { month: 3, selected: covered(10, 4, 5), comparison: covered(15, 5, 5) },
      { month: 4, selected: covered(10, 5, 5), comparison: covered(null, 0, 5) },
    ],
  };
  const combined = renderToStaticMarkup(createElement(ComparisonView, { report: { ...report, series: [metric, drought] } }));
  assert.match(combined, /Coverage across both years/);
  assert.match(combined, /<a href="#comparison-drought">Peak severe drought coverage<\/a><span>2 of 4 months full in both years/);
  assert.match(combined, /data-coverage="complete"><abbr title="January">Jan<\/abbr> <span>Full/);
  assert.match(combined, /data-coverage="partial"><abbr title="March">Mar<\/abbr> <span>Partial/);
  assert.match(combined, /data-coverage="missing"><abbr title="April">Apr<\/abbr> <span>Missing/);
  assert.match(combined, /Change from 2023 to 2024 <strong>-15 percentage points<\/strong>/);
  assert.match(combined, /<strong>0 percentage points<\/strong>/);
  assert.match(combined, /<strong>\+5 percentage points<\/strong>/);
  assert.match(combined, /Change from 2023 to 2024 <span>Partial coverage<\/span>/);
  assert.match(combined, /<td><span>Partial coverage<\/span><\/td>/);
  assert.match(combined, /<td><span>Missing value<\/span><\/td>/);
});

test("the comparison report opts into document scrolling and printable content", async () => {
  const css = await readFile(new URL("./comparison.module.css", view), "utf8");
  assert.match(css, /:global\(body\):has\(\.page\)\s*\{[^}]*overflow:\s*auto;/);
  assert.match(css, /@media print\s*\{\s*:global\(body\):has\(\.page\)\s*\{[^}]*overflow:\s*visible;/);
});
