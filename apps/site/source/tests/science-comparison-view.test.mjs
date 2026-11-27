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
const report = { selection: { year: 2024, compareYear: 2023 }, series: [metric] };
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
  assert.match(rendered, /href="\/labs\/heat-and-rain\?station=USW00013996&amp;year=2024"/);
});
