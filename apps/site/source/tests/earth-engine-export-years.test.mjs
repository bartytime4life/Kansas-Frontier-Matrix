import assert from "node:assert/strict";
import test from "node:test";
import vm from "node:vm";
import { build } from "esbuild";

const bundled = await build({ entryPoints: ["app/earth-engine-export.ts"], bundle: true, platform: "node", format: "esm", write: false });
const { buildEarthEngineExportRecipe: recipe } = await import(`data:text/javascript;base64,${Buffer.from(bundled.outputFiles[0].text).toString("base64")}`);

test("annual Drive exports use the requested year and exact calendar length", () => {
  for (const [id, year, count] of [["ee-chirps", 2023, 365], ["ee-chirps", 2024, 366], ["ee-terraclimate", 1999, 12]]) {
    const script = recipe(id, "sample", year);
    assert.doesNotThrow(() => new vm.Script(script));
    assert.match(script, new RegExp(`filterDate\\('${year}-01-01', '${year + 1}-01-01'\\)`));
    assert.match(script, new RegExp(`var expected = ${count};`));
    assert.match(script, new RegExp(`kfm_${id.replaceAll("-", "_")}_${year}_sample`));
    if (year !== 2024) assert.doesNotMatch(script, /source = source.filterDate\('2024-01-01', '2025-01-01'\)/);
  }
});

test("unsupported years and annualized terrain are rejected before export", () => {
  for (const [id, year] of [["ee-cdl", 2007], ["ee-cdl", 2025], ["ee-sentinel2", 2018], ["ee-chirps", 1980], ["ee-terraclimate", 2025], ["ee-chirps", 2023.5]]) {
    assert.throws(() => recipe(id, "statewide", year));
  }
  assert.throws(() => recipe("ee-3dep", "sample", 2024));
  assert.doesNotMatch(recipe("ee-3dep", "sample"), /filterDate/);
});
