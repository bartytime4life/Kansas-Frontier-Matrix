import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const source = name => readFile(new URL(`../app/${name}.ts`, import.meta.url), "utf8");
const moduleUrl = text => `data:text/javascript;base64,${Buffer.from(ts.transpileModule(text, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText).toString("base64")}`;
const previewUrl = moduleUrl(await source("neon-lidar-preview"));
const previewModel = await import(previewUrl);
const composeUrl = 'data:text/javascript,export const composeMapLayers = map => map.composed++;';
const model = await import(moduleUrl((await source("neon-lidar-map")).replace('"./neon-lidar-preview"', JSON.stringify(previewUrl)).replace('"./map-layer-composition"', JSON.stringify(composeUrl))));

function fixture() {
  const width = 8, tile = "NEON_D06_KONZ_DP3_666000_4328000", crs = 'PROJCS["WGS84 / UTM zone14N"]';
  return {
    schema_version: "kfm-neon-lidar-preview-v1", data_kind: "synthetic-test", generated_at: "2026-11-23T20:00:00Z",
    source: { site: "KONZ", month: "2024-09", acquisition_run: "2024_KONZ_1", release: "RELEASE-2026", tile,
      attribution: "Synthetic", horizontal_crs: crs, vertical_reference: "Synthetic", vertical_reference_basis: "Test", canopy_floor_m: null, canopy_floor_basis: "Unknown",
      files: ["dtm", "dsm", "chm"].map(kind => ({ kind, name: `${tile}_${kind.toUpperCase()}.tif`, bytes: 1000, sha256: "a".repeat(64), product: kind === "chm" ? "DP3.30015.001" : "DP3.30024.001" })) },
    grid: { width, height: width, bounds: [666000, 4328000, 667000, 4329000], source_resolution_m: 1, preview_resolution_m: 125, sampling: "nearest-neighbor",
      dtm: Array(64).fill(300), dsm: Array(64).fill(312), chm: Array(64).fill(8) },
    georeferencing: { method: "rasterio-warp-transform", target_crs: "EPSG:4326", source_crs: crs, coordinate_epoch: null,
      height_values_transformed: false, horizontal_accuracy_m: null, corner_width: 9,
      corners: Array.from({ length: 81 }, (_, index) => [-97 + (index % 9) * .0014, 39 - Math.floor(index / 9) * .00112]) },
    lifecycle: "local-preview-only", source_admitted: false, released: false,
  };
}
function fakeMap() {
  const sources = new Map(), layers = new Map();
  return { sources, layers, composed: 0, dataUpdates: 0,
    getSource: id => sources.get(id), getLayer: id => layers.get(id),
    addSource(id, spec) { sources.set(id, { ...spec, setData: data => { this.dataUpdates++; sources.get(id).data = data; } }); },
    addLayer(spec) { layers.set(spec.id, structuredClone(spec)); },
    setFilter(id, filter) { layers.get(id).filter = filter; },
    setPaintProperty(id, key, value) { layers.get(id).paint[key] = value; },
    removeLayer(id) { layers.delete(id); },
    removeSource(id) { assert.ok(![...layers.values()].some(layer => layer.source === id)); sources.delete(id); },
  };
}

test("georeferencing is optional for the lab but required for map placement; invalid folds and CRS identity fail", () => {
  const p = fixture(); assert.ok(previewModel.parseNeonLidarPreview(p));
  const old = structuredClone(p); delete old.georeferencing;
  assert.ok(previewModel.parseNeonLidarPreview(old)); assert.equal(model.buildNeonMapData(old), null); assert.equal(model.neonMapBounds(old), null);
  for (const mutate of [g => g.corners.pop(), g => g.source_crs = 'PROJCS["different"]', g => g.height_values_transformed = true,
    g => g.horizontal_accuracy_m = .15, g => g.coordinate_epoch = 2024, g => g.corners[1] = [...g.corners[0]],
    g => g.corners[9] = [-97, 39.1], g => g.corners[0] = [NaN, 39], g => g.corners[0] = [-120, 39]]) {
    const bad = fixture(); mutate(bad.georeferencing); assert.equal(previewModel.parseNeonLidarPreview(bad), null);
  }
});

test("display cells reuse projected edges, preserve row/column and independent heights, omit only entirely missing cells", () => {
  const p = fixture(); p.grid.dtm[0] = null; p.grid.dsm[0] = null; p.grid.chm[0] = null; p.grid.chm[1] = 0;
  const data = model.buildNeonMapData(p); assert.equal(data.features.length, 63);
  const first = data.features[0], next = data.features[1];
  assert.equal(first.id, 1); assert.deepEqual(first.properties, { row: 0, column: 1, dtm: 300, dsm: 312, chm: 0, local_preview: true, synthetic: true });
  const ring = first.geometry.coordinates[0]; assert.deepEqual(ring[0], ring.at(-1));
  assert.equal(ring[3], next.geometry.coordinates[0][0], "adjacent cells share the exact source corner object");
  assert.deepEqual(model.neonMapBounds(p), [[-97, 38.99104], [-96.9888, 39]]);
  assert.equal(model.hasNeonLocalHit([{ source: "county" }, { source: model.NEON_LOCAL_SOURCE }]), true);
  assert.equal(model.hasNeonLocalHit([{ source: "county" }]), false);
});

test("overlay switching reuses source data, masks NoData, preserves zero, and keeps a fixed canopy scale", () => {
  const map = fakeMap(), data = model.buildNeonMapData(fixture());
  model.applyNeonMapOverlay(map, data, "chm", .7);
  const layer = map.getLayer(model.NEON_LOCAL_FILL);
  assert.equal(layer.paint["fill-antialias"], false, "adjacent translucent sample cells do not introduce dark seams");
  assert.deepEqual(layer.filter, ["!=", ["get", "chm"], null]);
  assert.match(map.getSource(model.NEON_LOCAL_SOURCE).attribution, /Synthetic/);
  const color = layer.paint["fill-color"]; assert.equal(color[3], 0); assert.equal(color.at(-2), 30);
  model.applyNeonMapOverlay(map, data, "dtm", .4);
  assert.equal(map.sources.size, 1); assert.equal(map.layers.size, 1); assert.equal(map.dataUpdates, 0);
  assert.equal(layer.paint["fill-opacity"], .4); assert.deepEqual(layer.filter, ["!=", ["get", "dtm"], null]);
  const sharedDomain = layer.paint["fill-color"];
  model.applyNeonMapOverlay(map, data, "dsm", .4);
  assert.deepEqual(layer.paint["fill-color"].slice(3), sharedDomain.slice(3), "DTM and DSM retain identical color stops");
  const next = structuredClone(data); model.applyNeonMapOverlay(map, next, "dsm", .4); assert.equal(map.dataUpdates, 1);
  assert.equal(map.composed, 4);
});

test("zero opacity removes hit-testable geometry; style resets restore only requested data", () => {
  const map = fakeMap(), data = model.buildNeonMapData(fixture());
  model.applyNeonMapOverlay(map, data, "chm", 1);
  model.applyNeonMapOverlay(map, data, "chm", 0);
  assert.equal(map.sources.size, 0); assert.equal(map.layers.size, 0);
  model.applyNeonMapOverlay(map, data, "chm", 1);
  map.layers.clear(); map.sources.clear();
  model.applyNeonMapOverlay(map, data, "dtm", .5);
  assert.equal(map.sources.size, 1); assert.equal(map.layers.size, 1);
  model.clearNeonMapOverlay(map); model.clearNeonMapOverlay(map);
  assert.equal(map.sources.size, 0); assert.equal(map.layers.size, 0);
});

test("source collisions and invalid requests cannot overwrite or remove foreign source state", () => {
  const map = fakeMap(), data = model.buildNeonMapData(fixture());
  map.addSource(model.NEON_LOCAL_SOURCE, { type: "geojson", data: { marker: "foreign" } });
  assert.throws(() => model.applyNeonMapOverlay(map, data, "chm", 1), /already owned/);
  model.clearNeonMapOverlay(map); assert.deepEqual(map.getSource(model.NEON_LOCAL_SOURCE).data, { marker: "foreign" });
  for (const [mode, opacity] of [["other", .5], ["chm", NaN], ["chm", 1.1]]) assert.throws(() => model.applyNeonMapOverlay(fakeMap(), data, mode, opacity), /Invalid/);
});

test("near-constant elevation domains produce strictly increasing style stops", () => {
  const p = fixture(); p.grid.dtm.fill(1); p.grid.dsm.fill(1 + Number.EPSILON);
  const map = fakeMap(); model.applyNeonMapOverlay(map, model.buildNeonMapData(p), "dtm", .6);
  const color = map.getLayer(model.NEON_LOCAL_FILL).paint["fill-color"], stops = [];
  for (let index = 3; index < color.length; index += 2) stops.push(color[index]);
  for (let index = 1; index < stops.length; index++) assert.ok(stops[index] > stops[index - 1]);
});
