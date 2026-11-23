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

const storyModel = await import(moduleUrl((await source("neon-lidar-story")).replace('"./neon-lidar-preview"', JSON.stringify(previewUrl))));

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
    addLayer(spec, beforeId) {
      const entries = [...layers];
      const before = entries.findIndex(([id]) => id === beforeId);
      entries.splice(before < 0 ? entries.length : before, 0, [spec.id, structuredClone(spec)]);
      layers.clear(); for (const [id, layer] of entries) layers.set(id, layer);
    },
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

test("relative columns use one baseline for every surface and scale canopy base and top equally", () => {
  const p = fixture();
  p.grid.dtm[0] = -10; p.grid.dsm[0] = -12; p.grid.chm[0] = 0;
  p.grid.dtm[1] = 5; p.grid.dsm[1] = 8; p.grid.chm[1] = 20;
  const data = model.buildNeonMapData(p), original = structuredClone(data);
  const ground = model.buildNeon3DMapData(data, "dtm", 2), surface = model.buildNeon3DMapData(data, "dsm", 2);
  const canopy = model.buildNeon3DMapData(data, "chm", 2);
  assert.equal(ground.metadata.baseline_m, -12);
  assert.equal(surface.metadata.baseline_m, -12);
  assert.equal(canopy.metadata.baseline_m, -12);
  assert.deepEqual(ground.metadata, { baseline_m: -12, eligible_cells: 64, omitted_cells: 0, input_cells: 64, vertical_exaggeration: 2, render_height_limit_m: 100000 });
  assert.equal(ground.data.features[0].properties.display_top_m, 4, "negative absolute elevation is retained relative to the common baseline");
  assert.equal(surface.data.features[0].properties.display_top_m, 0, "a real zero relative height is not replaced by a fabricated minimum");
  const firstCanopy = canopy.data.features[0], secondCanopy = canopy.data.features[1];
  assert.equal(firstCanopy.properties.display_base_m, 4); assert.equal(firstCanopy.properties.display_top_m, 4);
  assert.equal(secondCanopy.properties.display_base_m, 34); assert.equal(secondCanopy.properties.display_top_m, 74);
  assert.equal(secondCanopy.properties.chm, 20); assert.equal(secondCanopy.properties.dsm - secondCanopy.properties.dtm, 3);
  assert.equal(secondCanopy.geometry, data.features[1].geometry, "display edges retain exact source footprint identity");
  assert.deepEqual(data, original, "drawing never scales or changes original sample/probe values");
});

test("unsupported 3D cells are omitted with counts, without imputing missing ground or corrupting source values", () => {
  const p = fixture(); p.grid.dtm[0] = null; p.grid.chm[1] = null;
  const data = model.buildNeonMapData(p);
  data.features[2].properties.chm = -1;
  data.features[3].properties.dtm = NaN;
  data.features[4].properties.dtm = Number.MAX_VALUE;
  data.features[5].properties.chm = Number.MAX_VALUE;
  data.features[6].properties.chm = 1e100; // finite JS value, nonfinite float render attribute
  data.features[7].properties.chm = 1e6; // finite float, outside the explicit local display budget
  const canopy = model.buildNeon3DMapData(data, "chm", 5);
  assert.equal(canopy.metadata.eligible_cells, 56); assert.equal(canopy.metadata.omitted_cells, 8);
  assert.equal(canopy.metadata.baseline_m, 300);
  assert.ok(canopy.data.features.every(f => f.id >= 8 && Number.isFinite(f.properties.display_top_m)));
  assert.ok(Number.isNaN(data.features[3].properties.dtm));
  const noGround = structuredClone(data);
  for (const feature of noGround.features) { feature.properties.dtm = null; feature.properties.dsm = null; }
  assert.deepEqual(model.buildNeon3DMapData(noGround, "chm").metadata,
    { baseline_m: null, eligible_cells: 0, omitted_cells: 64, input_cells: 64, vertical_exaggeration: 1, render_height_limit_m: 100000 });
  const overflow = structuredClone(data); overflow.features[0].properties.dtm = -Number.MAX_VALUE;
  assert.equal(model.buildNeon3DMapData(overflow, "dtm", 5).data.features.length, 1, "only the zero-relative-height minimum survives an overflowing range");
  for (const scale of [0, .99, 5.01, NaN, Infinity]) assert.throws(() => model.buildNeon3DMapData(data, "chm", scale), /Invalid/);
});

test("3D representation switches the owned layer, reuses stable columns, and preserves flat default and style recovery", () => {
  const map = fakeMap(), data = model.buildNeonMapData(fixture());
  map.getProjection = () => ({ type: "mercator" }); map.getTerrain = () => null;
  model.applyNeonMapOverlay(map, data, "chm", .8);
  assert.equal(map.getLayer(model.NEON_LOCAL_FILL).type, "fill");
  model.applyNeonMapOverlay(map, data, "chm", .8, { representation: "columns", verticalExaggeration: 3 });
  const layer = map.getLayer(model.NEON_LOCAL_FILL), source = map.getSource(model.NEON_LOCAL_SOURCE);
  assert.equal(layer.type, "fill-extrusion");
  assert.deepEqual(layer.paint["fill-extrusion-height"], ["get", "display_top_m"]);
  assert.deepEqual(layer.paint["fill-extrusion-base"], ["get", "display_base_m"]);
  assert.equal(layer.paint["fill-extrusion-vertical-gradient"], true);
  assert.equal(source.data.features[0].properties.display_top_m, 24);
  assert.equal(source.data.features[0].properties.row, 0); assert.equal(source.data.features[0].properties.column, 0);
  const updates = map.dataUpdates;
  model.applyNeonMapOverlay(map, data, "chm", .4, { representation: "columns", verticalExaggeration: 3 });
  assert.equal(map.dataUpdates, updates, "opacity changes do not resend 16k column polygons");
  assert.equal(layer.paint["fill-extrusion-opacity"], .4);
  model.applyNeonMapOverlay(map, data, "dsm", .4, { representation: "columns", verticalExaggeration: 3 });
  assert.equal(source.data.features[0].properties.display_top_m, 36);
  model.applyNeonMapOverlay(map, data, "dsm", .4);
  assert.equal(map.getLayer(model.NEON_LOCAL_FILL).type, "fill"); assert.equal(source.data, data);
  map.layers.clear(); map.sources.clear();
  model.applyNeonMapOverlay(map, data, "chm", .7, { representation: "columns" });
  assert.equal(map.getLayer(model.NEON_LOCAL_FILL).type, "fill-extrusion");
  model.applyNeonMapOverlay(map, data, "chm", 0, { representation: "columns" });
  assert.equal(map.sources.size, 0); assert.equal(map.layers.size, 0);
});

test("3D guards reject globe, active DEM, budget overflow and foreign layer/source IDs without mutation", () => {
  const data = model.buildNeonMapData(fixture());
  for (const [projection, terrain] of [["globe", null], ["mercator", { source: "foreign-dem" }]]) {
    const map = fakeMap(); map.getProjection = () => ({ type: projection }); map.getTerrain = () => terrain;
    assert.throws(() => model.applyNeonMapOverlay(map, data, "chm", .8, { representation: "columns" }), /Mercator without/);
    assert.equal(map.sources.size, 0); assert.equal(map.layers.size, 0);
  }
  const map = fakeMap(); map.getProjection = () => ({ type: "mercator" }); map.getTerrain = () => null;
  map.addLayer({ id: model.NEON_LOCAL_FILL, source: model.NEON_LOCAL_SOURCE, type: "fill", paint: { sentinel: "preserve" } });
  assert.throws(() => model.applyNeonMapOverlay(map, data, "chm", .8, { representation: "columns" }), /already owned/);
  assert.equal(map.sources.size, 0); assert.equal(map.getLayer(model.NEON_LOCAL_FILL).paint.sentinel, "preserve");
  const oversized = { type: "FeatureCollection", features: Array(128 ** 2 + 1).fill(data.features[0]) };
  assert.throws(() => model.buildNeon3DMapData(oversized, "dtm"), /Invalid/);
});

test("sample story stops use deterministic actual cells and distinguish independent canopy from surface difference", () => {
  const p = fixture();
  p.grid.dtm[0] = -10; p.grid.dsm[0] = -12;
  p.grid.dtm[1] = 400; p.grid.dsm[1] = 405;
  p.grid.chm[2] = 28.65; p.grid.chm[3] = 28.65;
  p.grid.dtm[4] = 310; p.grid.dsm[4] = 350; p.grid.chm[4] = 2;
  const story = storyModel.buildNeonStoryStops(p);
  assert.deepEqual(story.map(stop => [stop.id, stop.row, stop.column, stop.value_m]),
    [["low-ground", 0, 0, -10], ["high-ground", 0, 1, 400], ["high-canopy", 0, 2, 28.65], ["surface-gap", 0, 4, 40]]);
  assert.match(story[2].label, /sampled/); assert.equal(story[2].mode, "chm"); assert.equal(story[3].mode, "dsm");
  assert.equal(story[3].probe.chm, 2); assert.equal(story[3].probe.surfaceAboveGround, 40);
  assert.equal(story[2].probe.easting, 666312.5); assert.equal(story[2].probe.northing, 4328937.5);
  assert.ok(Math.abs(story[2].display_center[0] - (-97 + 2.5 * .0014)) < 1e-12);
  assert.ok(Math.abs(story[2].display_center[1] - (39 - .5 * .00112)) < 1e-12);
});

test("stories skip missing/nonfinite extrema, preserve finite negatives and do not invent a native outlier position", () => {
  const p = fixture();
  p.grid.dtm.fill(null); p.grid.dsm.fill(null); p.grid.chm.fill(null);
  assert.deepEqual(storyModel.buildNeonStoryStops(p), []);
  p.grid.dtm[0] = -4; p.grid.dsm[0] = -7; p.grid.chm[0] = 0;
  p.grid.dtm[1] = -Number.MAX_VALUE; p.grid.dsm[1] = Number.MAX_VALUE; p.grid.chm[1] = NaN;
  p.grid.dtm[2] = Infinity;
  delete p.georeferencing;
  const story = storyModel.buildNeonStoryStops(p);
  assert.equal(story.find(stop => stop.id === "surface-gap").value_m, -3, "finite negative differences remain real candidates");
  assert.equal(story.find(stop => stop.id === "high-canopy").value_m, 0);
  assert.ok(story.every(stop => stop.display_center === null));
  assert.ok(!story.some(stop => stop.value_m === 83.41000366210938));
});

test("canopy columns sit on neutral sampled ground using the same filtered cells and scale", () => {
  const map = fakeMap(), p = fixture();
  map.getProjection = () => ({ type: "mercator" }); map.getTerrain = () => null;
  p.grid.dtm[0] = null; p.grid.chm[1] = null;
  p.grid.dtm[2] = 303; p.grid.chm[2] = 0;
  const data = model.buildNeonMapData(p);
  model.applyNeonMapOverlay(map, data, "dtm", .8, { representation: "columns", verticalExaggeration: 2 });
  assert.equal(map.getLayer(model.NEON_LOCAL_GROUND), undefined);
  model.applyNeonMapOverlay(map, data, "chm", .8, { representation: "columns", verticalExaggeration: 2 });
  const ground = map.getLayer(model.NEON_LOCAL_GROUND), canopy = map.getLayer(model.NEON_LOCAL_FILL);
  assert.equal(map.sources.size, 1); assert.equal(map.layers.size, 2);
  assert.deepEqual([...map.layers.keys()], [model.NEON_LOCAL_GROUND, model.NEON_LOCAL_FILL], "ground is below the canopy within the composition tier");
  assert.equal(ground.source, canopy.source); assert.equal(ground.source, model.NEON_LOCAL_SOURCE);
  assert.equal(ground.paint["fill-extrusion-base"], 0);
  assert.deepEqual(ground.paint["fill-extrusion-height"], canopy.paint["fill-extrusion-base"]);
  assert.equal(ground.metadata.same_sampled_cells, true); assert.equal(ground.metadata.evidence, false);
  assert.equal(ground.metadata.representation, "sampled-ground-pedestal");
  const cells = map.getSource(model.NEON_LOCAL_SOURCE).data.features;
  assert.equal(cells.length, 62); assert.ok(cells.every(cell => cell.id >= 2), "unknown ground or unknown CHM cannot acquire fabricated supporting terrain");
  assert.equal(cells[0].properties.display_base_m, 6); assert.equal(cells[0].properties.display_top_m, 6);
  model.applyNeonMapOverlay(map, data, "chm", .35, { representation: "columns", verticalExaggeration: 2 });
  assert.equal(ground.paint["fill-extrusion-opacity"], .35);
  model.applyNeonMapOverlay(map, data, "dsm", .35, { representation: "columns" });
  assert.equal(map.getLayer(model.NEON_LOCAL_GROUND), undefined);
  model.applyNeonMapOverlay(map, data, "chm", .35, { representation: "columns" });
  map.layers.clear(); map.sources.clear();
  model.applyNeonMapOverlay(map, data, "chm", .35, { representation: "columns" });
  assert.deepEqual([...map.layers.keys()], [model.NEON_LOCAL_GROUND, model.NEON_LOCAL_FILL]);
  model.applyNeonMapOverlay(map, data, "chm", .35);
  assert.equal(map.getLayer(model.NEON_LOCAL_GROUND), undefined); assert.equal(map.layers.size, 1);
  model.applyNeonMapOverlay(map, data, "chm", .35, { representation: "columns" });
  model.applyNeonMapOverlay(map, data, "chm", 0, { representation: "columns" });
  assert.equal(map.layers.size, 0); assert.equal(map.sources.size, 0);
});

test("pedestal collisions and unexpected replacement layers stay untouched during apply and clear", () => {
  const data = model.buildNeonMapData(fixture()), map = fakeMap();
  map.getProjection = () => ({ type: "mercator" }); map.getTerrain = () => null;
  map.addLayer({ id: model.NEON_LOCAL_GROUND, type: "fill-extrusion", source: "foreign", paint: { sentinel: "external" } });
  assert.throws(() => model.applyNeonMapOverlay(map, data, "chm", .8, { representation: "columns" }), /already owned/);
  assert.equal(map.sources.size, 0); assert.equal(map.getLayer(model.NEON_LOCAL_GROUND).paint.sentinel, "external");
  map.layers.clear();
  model.applyNeonMapOverlay(map, data, "chm", .8, { representation: "columns" });
  map.removeLayer(model.NEON_LOCAL_GROUND);
  map.addLayer({ id: model.NEON_LOCAL_GROUND, type: "fill-extrusion", source: model.NEON_LOCAL_SOURCE, paint: { sentinel: "replacement" } });
  assert.throws(() => model.applyNeonMapOverlay(map, data, "dtm", .8), /already owned/);
  model.clearNeonMapOverlay(map);
  assert.equal(map.getLayer(model.NEON_LOCAL_FILL), undefined);
  assert.equal(map.getLayer(model.NEON_LOCAL_GROUND).paint.sentinel, "replacement");
  assert.equal(map.sources.size, 1, "unexpected replacement keeps its referenced source");
});
