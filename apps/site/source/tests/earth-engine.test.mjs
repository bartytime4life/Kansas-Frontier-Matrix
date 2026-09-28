import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";
import ts from "typescript";

const source = await readFile(new URL("../app/earth-engine-data.ts", import.meta.url), "utf8");
const js = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const catalog = await import(`data:text/javascript;base64,${Buffer.from(js).toString("base64")}`);

test("discovery supports multi-word searches and combined topic filters", () => {
  assert.equal(new Set(catalog.EARTH_ENGINE_DATASETS.map((d) => d.id)).size, 8);
  assert.deepEqual(catalog.findEarthEngineDatasets("USGS reflectance", "Imagery").map((d) => d.id), ["ee-landsat8"]);
  assert.equal(catalog.findEarthEngineDatasets("  drought  ", "Climate").length, 1);
  assert.equal(catalog.findEarthEngineDatasets("no such source").length, 0);
  assert.equal(catalog.findEarthEngineDatasets("USGS", "Agriculture").length, 0);
});

test("recipe requests reject unknown assets, invalid years and invented annual coverage", () => {
  for (const id of ["unknown", "ee-cdl');fetch('https://example.com')"]) assert.throws(() => catalog.buildEarthEngineRecipe(id, 2024));
  for (const year of [undefined, NaN, Infinity, 2024.5, 0, 1997, 2025, "2024"]) assert.throws(() => catalog.buildEarthEngineRecipe("ee-cdl", year));
  assert.throws(() => catalog.buildEarthEngineRecipe("ee-surface-water", 2021));
  assert.throws(() => catalog.buildEarthEngineRecipe("ee-3dep", 2022));
  for (const d of catalog.EARTH_ENGINE_DATASETS) {
    for (const year of d.temporalMode === "annual" ? [d.firstYear, d.lastYear] : [undefined]) {
      const recipe = catalog.buildEarthEngineRecipe(d.id, year);
      assert.doesNotThrow(() => new vm.Script(recipe));
      assert.match(recipe, /TIGER\/2018\/States/);
      assert.match(recipe, /STATEFP', '20'/);
      assert.doesNotMatch(recipe, /Export\.|fetch\(|XMLHttpRequest|toAsset\(/);
    }
  }
});

// A local EE surface double tests control flow, not provider execution or scientific accuracy.
function runRecipe(id, year, { count = 1, sourceError, periods, dateError } = {}) {
  const layers = [], messages = [], operations = [];
  const value = (result, error) => ({ evaluate(fn) { fn(result, error); } });
  const chain = new Proxy({}, { get(_target, key) {
    if (key === "size") return () => value(count, sourceError);
    if (key === "aggregate_array") return () => ({ map: () => ({ distinct: () => ({ size: () => value(periods, dateError) }) }) });
    if (key === "map") return (fn) => { fn(chain); return chain; };
    return (...args) => { operations.push([key, ...args]); return chain; };
  } });
  const ee = { FeatureCollection: () => chain, ImageCollection: () => chain, Image: () => chain, Filter: { eq: () => chain }, Reducer: { max: () => chain } };
  vm.runInNewContext(catalog.buildEarthEngineRecipe(id, year), {
    ee, Map: { centerObject() {}, addLayer(_image, _vis, title) { layers.push(title); } },
    print(...args) { messages.push(args.map((arg) => typeof arg === "object" ? "[EE object]" : String(arg)).join(" ")); },
  }, { timeout: 1000 });
  return { layers: layers.filter((title) => !title.includes("study boundary")), messages, operations };
}

test("empty collections and source errors do not fabricate preview data", () => {
  for (const d of catalog.EARTH_ENGINE_DATASETS.filter((d) => d.temporalMode !== "period-summary")) {
    const year = d.temporalMode === "annual" ? d.lastYear : undefined;
    const empty = runRecipe(d.id, year, { count: 0 });
    assert.equal(empty.layers.length, 0);
    assert.match(empty.messages.join(" "), /NO DATA/);
    const failed = runRecipe(d.id, year, { sourceError: "unauthorized" });
    assert.equal(failed.layers.length, 0);
    assert.match(failed.messages.join(" "), /SOURCE ERROR/);
  }
  assert.equal(runRecipe("ee-cdl", 2024, { count: 2 }).layers.length, 0);
});

test("annual climate results require all unique periods including leap days", () => {
  for (const [id, year, expected] of [["ee-chirps", 2024, 366], ["ee-chirps", 2023, 365], ["ee-terraclimate", 2024, 12]]) {
    assert.equal(runRecipe(id, year, { count: expected, periods: expected }).layers.length, 1);
    assert.equal(runRecipe(id, year, { count: expected - 1, periods: expected - 1 }).layers.length, 0);
    assert.equal(runRecipe(id, year, { count: expected, periods: expected - 1 }).layers.length, 0);
    assert.equal(runRecipe(id, year, { count: expected, periods: expected, dateError: "failed" }).layers.length, 0);
  }
  const rain = runRecipe("ee-chirps", 2024, { count: 366, periods: 366 });
  assert.ok(rain.operations.some(([name]) => name === "sum"));
  assert.ok(rain.operations.some(([name, value]) => name === "eq" && value === 366));
  const drought = runRecipe("ee-terraclimate", 2024, { count: 12, periods: 12 });
  assert.ok(drought.operations.some(([name, value]) => name === "multiply" && value === .01));
});

test("imagery recipes apply scale and quality rules, and fixed products preserve their time semantics", () => {
  const landsat = runRecipe("ee-landsat8", 2024);
  assert.ok(landsat.operations.some(([name, value]) => name === "bitwiseAnd" && value === 63));
  assert.ok(landsat.operations.some(([name, value]) => name === "multiply" && value === .0000275));
  assert.ok(landsat.operations.some(([name, value]) => name === "add" && value === -.2));
  const sentinel = runRecipe("ee-sentinel2", 2024);
  assert.ok(sentinel.operations.some(([name, value]) => name === "multiply" && value === .0001));
  const dynamic = runRecipe("ee-dynamic-world", 2024);
  assert.ok(dynamic.operations.some(([name, value]) => name === "gte" && value === .6));
  assert.ok(dynamic.operations.some(([name]) => name === "mode"));
  assert.equal(runRecipe("ee-surface-water").layers.length, 1);
  assert.doesNotMatch(catalog.buildEarthEngineRecipe("ee-surface-water"), /filterDate/);
  assert.match(catalog.buildEarthEngineRecipe("ee-3dep"), /USGS\/3DEP\/10m_collection/);
  assert.equal(runRecipe("ee-3dep").layers.length, 1);
});

test("review drafts retain provenance questions without granting admission or execution", () => {
  const draft = catalog.earthEngineReviewPacket("ee-chirps", 2024);
  assert.deepEqual(draft.requestedPeriod, { startInclusive: "2024-01-01", endExclusive: "2025-01-01" });
  assert.equal(draft.status, "PROPOSED");
  assert.equal(draft.execution, "NOT_RUN");
  assert.equal(draft.admission, "NOT_ADMITTED");
  assert.equal(draft.release, "NOT_RELEASED");
  assert.equal(catalog.earthEngineReviewPacket("ee-3dep").requestedPeriod, null);
  assert.throws(() => catalog.earthEngineReviewPacket("ee-cdl", 2026));
  for (const d of catalog.EARTH_ENGINE_DATASETS) assert.equal(new URL(catalog.earthEngineUrl(d)).hostname, "developers.google.com");
});
