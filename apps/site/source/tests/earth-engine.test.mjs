import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";
import ts from "typescript";

const transpile = (text) => `data:text/javascript;base64,${Buffer.from(ts.transpileModule(text, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText).toString("base64")}`;
const read = (path) => readFile(new URL(path, import.meta.url), "utf8");
const catalogUrl = transpile(await read("../app/earth-engine-data.ts"));
const contextUrl = transpile(await read("../app/earth-engine-context.ts"));
const catalog = await import(catalogUrl);
const exporter = await import(transpile((await read("../app/earth-engine-export.ts"))
  .replace('"./earth-engine-data"', JSON.stringify(catalogUrl)).replace('"./earth-engine-context"', JSON.stringify(contextUrl))));
const context = await import(contextUrl);

test("discovery supports multi-word searches and combined topic filters", () => {
  assert.equal(new Set(catalog.EARTH_ENGINE_DATASETS.map((d) => d.id)).size, 17);
  assert.deepEqual(catalog.findEarthEngineDatasets("USGS reflectance", "Imagery").map((d) => d.id), ["ee-landsat8", "ee-landsat4", "ee-landsat5", "ee-landsat7", "ee-landsat9"]);
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
    if (key === "aggregate_array") return () => ({ map: () => ({ distinct: () => ({ size: () => value(periods, dateError) }) }), distinct: () => ({ size: () => value(periods, dateError) }) });
    if (key === "map") return (fn) => { fn(chain); return chain; };
    return (...args) => { operations.push([key, ...args]); return chain; };
  } });
  const ee = { FeatureCollection: () => chain, ImageCollection: () => chain, Image: () => chain, Filter: { eq: () => chain, gte: () => chain, lt: () => chain }, Reducer: { max: () => chain } };
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
  for (const [id, year, expected] of [["ee-chirps", 2024, 366], ["ee-chirps", 2023, 365], ["ee-terraclimate", 2024, 12], ["ee-prism-monthly", 1895, 12], ["ee-prism-daily", 1984, 366], ["ee-prism-daily", 1981, 365]]) {
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

test("historical sensors keep band families and inventory-only products do not fabricate RGB", () => {
  for (const [mission, year] of [[4, 1982], [5, 1984], [7, 1999]]) {
    const result = runRecipe("ee-landsat" + mission, year);
    assert.ok(result.operations.some(([name, bands]) => name === "select" && JSON.stringify(bands) === '["SR_B3","SR_B2","SR_B1"]'));
    assert.ok(result.operations.some(([name, band]) => name === "select" && band === "QA_RADSAT"));
  }
  for (const [mission, year] of [[8, 2013], [9, 2021]]) {
    const result = runRecipe("ee-landsat" + mission, year);
    assert.ok(result.operations.some(([name, bands]) => name === "select" && JSON.stringify(bands) === '["SR_B4","SR_B3","SR_B2"]'));
  }
  for (const [id, year] of [["ee-landsat-mss", 1972], ["ee-era5", 1940], ["ee-era5-land", 1950]]) {
    const result = runRecipe(id, year);
    assert.equal(result.layers.length, 0);
    assert.match(result.messages.join(" "), /INVENTORY ONLY/);
  }
  assert.ok(runRecipe("ee-sentinel2", 2017).layers.some((title) => title.includes("2017") && title.includes("RGB")));
  assert.throws(() => exporter.buildEarthEngineExportRecipe("ee-sentinel2", "statewide", 2017));
});

const channels = (color) => [1, 3, 5].map((i) => parseInt(color.replace(/^#?/, "#").slice(i, i + 2), 16));
function interp(value, stops, colors) {
  const i = Math.max(0, stops.findIndex((stop, index) => index > 0 && value <= stop) - 1);
  const t = (value - stops[i]) / (stops[i + 1] - stops[i]);
  return channels(colors[i]).map((channel, c) => channel + (channels(colors[i + 1])[c] - channel) * t);
}

test("display ramps match the tile renderer and reproduce uneven stops as Earth Engine palettes", async () => {
  const python = await read("../scripts/earth-engine/prepare_display_set.py");
  const rendered = Object.fromEntries([...python.matchAll(/"(ee-[a-z0-9-]+)": \(\[([^\]]*)\], \[([^\]]*)\]\)/g)]
    .map(([, id, stops, colors]) => [id, { stops: stops.split(",").map(Number), colors: [...colors.matchAll(/"(#[0-9a-f]{6})"/g)].map((m) => m[1]) }]));
  assert.deepEqual(rendered, JSON.parse(JSON.stringify(catalog.EARTH_ENGINE_DISPLAY_RAMPS)));
  assert.deepEqual(catalog.earthEnginePalette(catalog.EARTH_ENGINE_DISPLAY_RAMPS["ee-chirps"]), ["fff4c2", "79c9bc", "235ca8"]);
  for (const ramp of Object.values(catalog.EARTH_ENGINE_DISPLAY_RAMPS)) {
    const palette = catalog.earthEnginePalette(ramp);
    const first = ramp.stops[0], last = ramp.stops.at(-1), step = (last - first) / (palette.length - 1);
    // Earth Engine interpolates evenly spaced palette entries; every sample and midpoint must track the renderer ramp.
    for (let value = first; value <= last; value += step / 2) {
      const index = (value - first) / step, low = Math.floor(index), high = Math.min(palette.length - 1, low + 1);
      const ee = channels(palette[low]).map((channel, c) => channel + (channels(palette[high])[c] - channel) * (index - low));
      interp(value, ramp.stops, ramp.colors).forEach((expected, c) => assert.ok(Math.abs(expected - ee[c]) <= 1, `${value}: ${expected} vs ${ee[c]}`));
    }
    for (const [i, stop] of ramp.stops.entries()) assert.equal("#" + palette[(stop - first) / step], ramp.colors[i]);
  }
  assert.equal(catalog.earthEnginePalette(catalog.EARTH_ENGINE_DISPLAY_RAMPS["ee-3dep"]).length, 12);
  assert.equal(catalog.earthEngineLegendGradient(catalog.EARTH_ENGINE_DISPLAY_RAMPS["ee-3dep"]), "linear-gradient(90deg, #28594e 0%, #c4c98a 36.4%, #a67e54 63.6%, #efe7d4 100%)");
  assert.match(python, /^MIN_ZOOM = 0$/m);
  assert.match(python, /for z in range\(MIN_ZOOM, spec\["maxZoom"\] \+ 1\)/);
});

test("every installed layer has a legend swatch and discovery previews use the installed styling", async () => {
  const css = await read("../app/earth-engine-display.module.css");
  for (const layer of context.EARTH_ENGINE_CONTEXT_LAYERS) {
    assert.ok(catalog.EARTH_ENGINE_DISPLAY_RAMPS[layer.id] || css.includes(`data-layer=${layer.id}]`), `${layer.id} legend`);
  }
  for (const id of ["ee-chirps", "ee-terraclimate", "ee-3dep"]) {
    const recipe = catalog.buildEarthEngineRecipe(id, id === "ee-3dep" ? undefined : 2024);
    assert.ok(recipe.includes(catalog.earthEngineVisParams(catalog.EARTH_ENGINE_DISPLAY_RAMPS[id])), id);
  }
  assert.ok(catalog.buildEarthEngineRecipe("ee-sentinel2", 2024).includes(catalog.EARTH_ENGINE_REFLECTANCE_VIS));
});

// A local EE double checks the generated control flow and task parameters, not provider execution.
function runExport(id, scope, count, year = id === "ee-3dep" ? undefined : Math.min(2024, context.EARTH_ENGINE_SOURCE_YEARS[id][1]), gridOkay = true) {
  const layers = [], images = [], tables = [];
  const chain = new Proxy(function () {}, {
    get(_target, key) {
      if (key === "getInfo") return () => count;
      if (key === "aggregate_min") return () => ({ getInfo: () => gridOkay ? 1 : 0 });
      if (key === "map") return (fn) => { fn(chain); return chain; };
      return () => chain;
    },
    apply: () => chain,
  });
  const script = exporter.buildEarthEngineExportRecipe(id, scope, year);
  let error = null;
  try {
    vm.runInNewContext(script, {
      ee: new Proxy({}, { get: () => chain }), print() {},
      Map: { centerObject() {}, addLayer(_image, vis, title) { layers.push({ vis: JSON.parse(JSON.stringify(vis)), title }); } },
      Export: { image: { toDrive(options) { images.push(JSON.parse(JSON.stringify(options))); } }, table: { toDrive(options) { tables.push(JSON.parse(JSON.stringify(options))); } } },
    }, { timeout: 1000 });
  } catch (cause) { error = cause; }
  return { script, layers, images, tables, error };
}

test("Drive export recipes export the complete source inventory, the documented grid and a styled preview", () => {
  const expected = { "ee-cdl": 1, "ee-chirps": 366, "ee-terraclimate": 12, "ee-sentinel2": 4000, "ee-3dep": 40, "ee-prism-monthly": 12, "ee-prism-daily": 366, "ee-landsat4": 40, "ee-landsat5": 40, "ee-landsat7": 40, "ee-landsat8": 40, "ee-landsat9": 40 };
  for (const layer of context.EARTH_ENGINE_CONTEXT_LAYERS) for (const scope of ["sample", "statewide"]) {
    const run = runExport(layer.id, scope, expected[layer.id]);
    assert.equal(run.error, null, `${layer.id} ${scope}: ${run.error}`);
    assert.doesNotThrow(() => new vm.Script(run.script));
    assert.equal(run.tables.length, 1);
    assert.deepEqual(run.tables[0].selectors, ["source_image_id", "time_start_ms"]);
    assert.equal(run.tables[0].fileFormat, "CSV");
    assert.match(run.tables[0].description, new RegExp(`^kfm_${layer.id.replaceAll("-", "_")}_.*_${scope}_source_ids$`));
    assert.equal(run.images.length, 1);
    const highResolution = !["ee-chirps", "ee-terraclimate", "ee-prism-monthly", "ee-prism-daily"].includes(layer.id);
    assert.deepEqual(run.images[0].crsTransform, highResolution ? [30, 0, -1200000, 0, -30, 2400000]
      : layer.id.startsWith("ee-prism-") ? [0.041666666667, 0, -125.0208333333335, 0, -0.041666666667, 49.9375000000005] : layer.id === "ee-chirps" ? [0.05, 0, -180, 0, -0.05, 50] : [1 / 24, 0, -180, 0, -(1 / 24), 90]);
    assert.equal(run.images[0].crs, highResolution ? "EPSG:5070" : layer.id.startsWith("ee-prism-") ? "EPSG:4269" : "EPSG:4326");
    assert.equal(run.images[0].fileDimensions, scope === "statewide" && highResolution ? 2048 : undefined);
    assert.equal(run.layers.length, 1);
    const ramp = catalog.EARTH_ENGINE_DISPLAY_RAMPS[layer.id];
    if (ramp) assert.deepEqual(run.layers[0].vis, { min: ramp.stops[0], max: ramp.stops.at(-1), palette: catalog.earthEnginePalette(ramp) });
    assert.match(run.script, /reduceRegion\(\{reducer: ee\.Reducer\.count\(\), geometry: sample, crs: /);
  }
  const cdl = runExport("ee-cdl", "sample", 1);
  assert.deepEqual(cdl.layers[0].vis, {});
  assert.match(cdl.script, /Map\.addLayer\(ee\.Image\(source\.first\(\)\)\.select\('cropland'\)\.clip\(region\), \{\}/);
  assert.deepEqual(runExport("ee-sentinel2", "sample", 10).layers[0].vis, { min: 0, max: 0.3, gamma: 1.2 });
  const priorYear = runExport("ee-chirps", "statewide", 365, 2023);
  assert.equal(priorYear.error, null);
  assert.equal(priorYear.images.length, 1);
  assert.equal(priorYear.tables[0].description, "kfm_ee_chirps_2023_statewide_source_ids");
  assert.deepEqual(priorYear.layers[0].vis, runExport("ee-chirps", "statewide", 366, 2024).layers[0].vis);
  assert.match(String(runExport("ee-chirps", "statewide", 364, 2023).error), /Export held/);
  for (const [id, count] of [["ee-cdl", 2], ["ee-chirps", 365], ["ee-terraclimate", 11], ["ee-sentinel2", 0], ["ee-3dep", 0]]) {
    const held = runExport(id, "statewide", count);
    assert.match(String(held.error), /Export held/);
    assert.equal(held.images.length, 0);
  }
});


test("PRISM exports retain the native day labels and reject changed scene grids before tasks", () => {
  for (const [id, year, count, firstLabel, nextLabel] of [["ee-prism-monthly", 1895, 12, "189501", "189601"], ["ee-prism-daily", 1981, 365, "19810101", "19820101"]]) {
    const result = runExport(id, "sample", count, year);
    assert.equal(result.error, null); assert.equal(result.images.length, 1);
    assert.match(result.script, new RegExp(`gte\\('system:index', '${firstLabel}'\\)`));
    assert.match(result.script, new RegExp(`lt\\('system:index', '${nextLabel}'\\)`));
    assert.doesNotMatch(result.script, /filterDate/);
    assert.match(result.script, /aggregate_array\('system:index'\)\.distinct/);
    assert.match(result.script, /time_start_ms: scene.get\('system:time_start'\)/);
    const badGrid = runExport(id, "sample", count, year, false);
    assert.match(String(badGrid.error), /native grid differs/); assert.equal(badGrid.images.length, 0); assert.equal(badGrid.tables.length, 0);
    const missing = runExport(id, "sample", count - 1, year);
    assert.match(String(missing.error), /time coverage is incomplete/); assert.equal(missing.images.length, 0);
  }
});

test("Landsat exports use sensor-specific RGB, QA screening, common grid and retained-count band", () => {
  for (const [mission, year] of [[4, 1982], [5, 1984], [7, 1999], [8, 2013], [9, 2021]]) {
    const result = runExport(`ee-landsat${mission}`, "statewide", 40, year);
    assert.equal(result.error, null); assert.equal(result.images[0].fileDimensions, 2048);
    assert.match(result.script, /QA_PIXEL'\)\.bitwiseAnd\(63\)\.eq\(0\)\.and\(scene.select\('QA_RADSAT'\)\.eq\(0\)\)/);
    assert.match(result.script, new RegExp(mission < 8 ? "SR_B3','SR_B2','SR_B1" : "SR_B4','SR_B3','SR_B2"));
    assert.match(result.script, /multiply\(0.0000275\)\.add\(-0.2\)/);
    assert.match(result.script, /addBands\(clean.select\(0\)\.count\(\)\.rename\('retained_count'\)/);
    assert.deepEqual(result.layers[0].vis, { min: 0, max: 0.3, gamma: 1.2 });
    assert.match(String(runExport(`ee-landsat${mission}`, "sample", 0, year).error), /No .* Landsat/);
  }
});
