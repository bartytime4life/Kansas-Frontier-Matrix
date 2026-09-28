import test from "node:test";
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import ts from "typescript";

const loadSource = async (path, replacements = []) => {
  let source = await readFile(new URL(path, import.meta.url), "utf8");
  for (const [before, after] of replacements) source = source.replace(before, after);
  const javascript = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
  return import(`data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`);
};

test("draws raster under areas and points, with selections above data", async () => {
  const registryUrl = `data:text/javascript;base64,${Buffer.from('export const LAYER_REGISTRY=[{renderers:[{id:"local-fill"},{id:"local-point"}]}];').toString("base64")}`;
  const composition = await loadSource("../app/map-layer-composition.ts", [['from "./explorer-data";', `from "${registryUrl}";`]]);
  const layers = [
    { id: "base", type: "background" }, { id: "local-point", type: "circle" },
    { id: "external-smoke-fill", type: "fill" }, { id: "kfm-selection-point", type: "circle" },
    { id: "kfm-ee-context-layer-2024", type: "raster" }, { id: "local-fill", type: "fill" },
  ];
  const map = { getStyle: () => ({ layers }), moveLayer(id) { layers.push(layers.splice(layers.findIndex((layer) => layer.id === id), 1)[0]); } };
  composition.composeMapLayers(map);
  assert.deepEqual(layers.map((layer) => layer.id), ["base", "kfm-ee-context-layer-2024", "external-smoke-fill", "local-fill", "local-point", "kfm-selection-point"]);
  composition.composeMapLayers(map);
  assert.equal(layers.length, 6);
});

test("shares opacity among visible rasters and restores it when one is hidden", async () => {
  const registryUrl = `data:text/javascript;base64,${Buffer.from('export const LAYER_REGISTRY=[];').toString("base64")}`;
  const composition = await loadSource("../app/map-layer-composition.ts", [['from "./explorer-data";', `from "${registryUrl}";`]]);
  const visible = new Set(["external-a", "external-b"]);
  const paint = new Map();
  const map = { getLayer: (id) => ({ id }), getLayoutProperty: (id) => visible.has(id) ? "visible" : "none", getPaintProperty: (id) => paint.get(id), setPaintProperty: (id, key, value) => paint.set(id, value) };
  composition.requestRasterOpacity(map, "external-a", 0.8);
  composition.requestRasterOpacity(map, "external-b", 0.7);
  composition.balanceMapRasters(map);
  assert.ok(Math.abs(paint.get("external-a") + paint.get("external-b") - 0.9) < 1e-10);
  visible.delete("external-b");
  composition.balanceMapRasters(map);
  assert.equal(paint.get("external-a"), 0.8);
});

test("orders terrain, water, and dated radar without burying radar when satellite is enabled", async () => {
  const registryUrl = `data:text/javascript;base64,${Buffer.from('export const LAYER_REGISTRY=[];').toString("base64")}`;
  const composition = await loadSource("../app/map-layer-composition.ts", [['from "./explorer-data";', `from "${registryUrl}";`]]);
  const layers = [
    { id: "external-nws-radar-raster", type: "raster" },
    { id: "external-noaa-goes-geocolor-raster", type: "raster" },
    { id: "external-usgs-3dhp-hydrography-raster", type: "raster" },
    { id: "external-noaa-hms-smoke-fill", type: "fill" },
  ];
  const map = { getStyle: () => ({ layers }), moveLayer(id) { layers.push(layers.splice(layers.findIndex((layer) => layer.id === id), 1)[0]); } };
  composition.composeMapLayers(map);
  assert.deepEqual(layers.map(({ id }) => id), [
    "external-noaa-goes-geocolor-raster", "external-usgs-3dhp-hydrography-raster",
    "external-nws-radar-raster", "external-noaa-hms-smoke-fill",
  ]);
});

test("balances related rasters while retaining a separate visible radar frame", async () => {
  const registryUrl = `data:text/javascript;base64,${Buffer.from('export const LAYER_REGISTRY=[];').toString("base64")}`;
  const composition = await loadSource("../app/map-layer-composition.ts", [['from "./explorer-data";', `from "${registryUrl}";`]]);
  const visible = new Set(["external-usgs-3dep-hillshade-raster", "external-noaa-goes-geocolor-raster", "external-nws-radar-raster"]);
  const paint = new Map();
  const map = { getLayer: (id) => ({ id }), getLayoutProperty: (id) => visible.has(id) ? "visible" : "none", getPaintProperty: (id) => paint.get(id), setPaintProperty: (id, key, value) => paint.set(id, value) };
  for (const [id, value] of [["external-usgs-3dep-hillshade-raster", 0.46], ["external-noaa-goes-geocolor-raster", 0.58], ["external-nws-radar-raster", 0.68]]) composition.requestRasterOpacity(map, id, value);
  composition.balanceMapRasters(map);
  assert.ok(Math.abs(paint.get("external-usgs-3dep-hillshade-raster") + paint.get("external-noaa-goes-geocolor-raster") - 0.68) < 1e-10);
  assert.equal(paint.get("external-nws-radar-raster"), 0.68);
  visible.delete("external-noaa-goes-geocolor-raster");
  composition.balanceMapRasters(map);
  assert.equal(paint.get("external-usgs-3dep-hillshade-raster"), 0.46);
});

test("bounded time bins keep gaps and omit invented counts", async () => {
  const { buildAvailabilityBins } = await loadSource("../app/timeline-availability.ts");
  const bins = buildAvailabilityBins([1800, 1801, 1802, 1803, 1804, 1805], { 1801: 3, 1805: 1 }, 3);
  assert.deepEqual(bins, [
    { start: 1800, end: 1801, peak: 3, total: 3 },
    { start: 1802, end: 1803, peak: 0, total: 0 },
    { start: 1804, end: 1805, peak: 1, total: 1 },
  ]);
});

test("signals require comparable observed or provider forecast data", async () => {
  const { deriveMapSignals } = await loadSource("../app/map-signals.ts");
  const gauges = [
    { hasForecast: true, observedValue: 3, forecastValue: 4, observedUnit: "ft", forecastUnit: "ft", observedAt: "2026-09-27T00:00:00Z", forecastAt: "2026-09-28T00:00:00Z" },
    { hasForecast: true, observedValue: 5, forecastValue: 6, observedUnit: "ft", forecastUnit: "ft", observedAt: "2026-09-27T00:00:00Z", forecastAt: "2026-09-28T00:00:00Z" },
  ];
  assert.equal(deriveMapSignals({ gauges }).length, 1);
  assert.equal(deriveMapSignals({ gauges: [{ ...gauges[0], forecastUnit: "m" }] }).length, 0);
  assert.equal(deriveMapSignals({ entered: 0, exited: 0 }).length, 0);
});
