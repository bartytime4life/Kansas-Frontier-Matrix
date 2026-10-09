import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const read = path => readFile(new URL(`../${path}`, import.meta.url), "utf8");
const toUrl = source => `data:text/javascript;base64,${Buffer.from(source).toString("base64")}`;
const transpile = source => ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const modelUrl = toUrl(transpile(await read("app/terrain-drawing.ts")));
const model = await import(modelUrl);
const surfaceUrl = toUrl(transpile((await read("app/terrain-surface.ts")).replace('"./terrain-drawing"', JSON.stringify(modelUrl))));

const grid = (size, height) => ({ size, bounds: [0, 0, size - 1, size - 1], spacingMeters: 100, heights: Array.from({ length: size ** 2 }, (_, index) => height(index % size, Math.floor(index / size))) });
const contours = geometry => geometry.data.features.filter(feature => feature.properties.role === "contour");
const segments = geometry => geometry.data.features.flatMap(feature => feature.geometry.coordinates);

test("terrain footprint is local, Kansas-bounded and quality-limited", () => {
  for (const [efficient, detail, size] of [[true, true, 33], [false, false, 49], [false, true, 65]]) {
    const patch = model.terrainDrawingFootprint([-98, 38], 8.5, efficient, detail);
    assert.equal(patch.size, size);
    assert.ok(patch.size ** 2 <= model.TERRAIN_DRAWING_MAX_SAMPLES);
    assert.ok(patch.spacingMeters * (size - 1) <= 24_000.0001);
  }
  const edge = model.terrainDrawingFootprint([-102.09, 39.98], 9, false, false);
  assert.ok(edge.bounds[0] >= -102.1 && edge.bounds[3] <= 40.1);
  for (const args of [[[0, 38], 10], [[-98, 45], 10], [[NaN, 38], 10], [[-98, 38], 8], [[-98, 38], Infinity]]) assert.equal(model.terrainDrawingFootprint(...args, false, false), null);
  const close = model.terrainDrawingFootprint([-98, 38], 13, false, false);
  assert.ok(close.spacingMeters < edge.spacingMeters, "closer views sample a smaller patch");
});

test("sloping plane contours use actual linear crossings and every fifth interval is stronger", () => {
  const geometry = model.buildTerrainDrawingGeometry(grid(5, col => 100 + col * 20), { intervalMeters: 10 });
  assert.equal(geometry.intervalMeters, 10);
  assert.equal(geometry.coverage, 1);
  for (const feature of contours(geometry)) {
    for (const line of feature.geometry.coordinates) for (const [x] of line) assert.equal(x, (feature.properties.elevation - 100) / 20);
    assert.equal(feature.properties.index, feature.properties.elevation % 50 === 0);
  }
  assert.ok(contours(geometry).some(feature => feature.properties.elevation === 130));
});

test("hill geometry contains repeated elevation bands with finite two-point cell segments", () => {
  const geometry = model.buildTerrainDrawingGeometry(grid(9, (col, row) => 300 - 4 * ((col - 4) ** 2 + (row - 4) ** 2)), { intervalMeters: 10 });
  assert.ok(contours(geometry).length > 5);
  for (const line of segments(geometry)) {
    assert.equal(line.length, 2);
    assert.ok(line.flat().every(Number.isFinite));
    assert.notDeepEqual(line[0], line[1]);
  }
});

test("saddles have deterministic bilinear connectivity; exact-level vertices avoid zero segments", () => {
  const points = [[0, 1], [1, 1], [1, 0], [0, 0]];
  const expected = [
    [[2 / 3, 1], [1, 2 / 3]], [[1 / 3, 0], [0, 1 / 3]],
  ];
  const actual = model.contourCell(points, [2, -1, 2, -1], 0);
  for (let line = 0; line < 2; line += 1) for (let point = 0; point < 2; point += 1) for (let axis = 0; axis < 2; axis += 1)
    assert.ok(Math.abs(expected[line][point][axis] - actual[line][point][axis]) < 1e-12);
  const saddle = model.contourCell(points, [1, -1, 1, -1], 0);
  assert.deepEqual(saddle, model.contourCell(points, [1, -1, 1, -1], 0));
  assert.equal(saddle.length, 2);
  assert.deepEqual(model.contourCell(points, [0, 1, 2, 1], 0), [], "an isolated level vertex is not a line");
  assert.deepEqual(model.contourCell(points, [0, 1, 1, 0], 0), [[[0, 1], [0, 0]]], "exact equal edge is retained once within a cell");
  assert.deepEqual(model.contourCell(points, [1, 1, 1, 1], 1), []);
  const exactValley = model.buildTerrainDrawingGeometry(grid(3, col => 100 + Math.abs(col - 1) * 10), { intervalMeters: 10 });
  const valley = contours(exactValley).find(feature => feature.properties.elevation === 100);
  assert.equal(valley.geometry.coordinates.length, 2, "the shared exact-level edge is not duplicated by its neighboring cells");
});

test("unknown corners and NaN create holes in contours and in adjacent grid edges", () => {
  const input = grid(3, (col, row) => 100 + col * 10 + row * 5);
  input.heights[4] = null;
  const geometry = model.buildTerrainDrawingGeometry(input, { intervalMeters: 5 });
  assert.equal(contours(geometry).length, 0, "all four cells touch the missing center");
  assert.equal(geometry.coverage, 8 / 9);
  const lines = geometry.data.features.find(feature => feature.properties.role === "grid").geometry.coordinates;
  assert.equal(lines.length, 8);
  for (const line of lines) assert.ok(line.every(([x, y]) => x !== 1 || y !== 1));
  input.heights[4] = NaN;
  assert.deepEqual(model.buildTerrainDrawingGeometry(input), geometry);
  assert.deepEqual(model.contourCell([[0, 0], [1, 0], [1, 1], [0, 1]], [1, 2, NaN, 4], 2), []);
});

test("constant and wholly missing surfaces do not invent contour variation", () => {
  const flat = model.buildTerrainDrawingGeometry(grid(4, () => 250));
  assert.equal(flat.intervalMeters, null);
  assert.equal(contours(flat).length, 0);
  assert.equal(flat.data.features[0].properties.role, "grid");
  const missing = model.buildTerrainDrawingGeometry(grid(4, () => null));
  assert.equal(missing.coverage, 0);
  assert.equal(missing.sampleCount, 16, "unavailable readings still count as attempted samples");
  assert.equal(missing.data.features.length, 0);
});

test("sample, level and segment caps bound worst-case geometry; batches yield regularly", () => {
  const input = grid(65, (col, row) => (col + row) % 2 ? 2000 : 100);
  const geometry = model.buildTerrainDrawingGeometry(input, { intervalMeters: 0.0001, maxSegments: 9000 });
  assert.ok(contours(geometry).length <= model.TERRAIN_DRAWING_MAX_LEVELS);
  assert.equal(geometry.segmentCount, 9000);
  assert.equal(geometry.clipped, true);
  assert.equal(segments(geometry).length, 9000);
  assert.equal(model.buildTerrainDrawingGeometry(grid(66, () => 100)).sampleCount, 0);
  const batches = model.terrainDrawingGeometryBatches(grid(49, (x, y) => 100 + x + y));
  let yields = 0, next = batches.next();
  while (!next.done) { yields += 1; next = batches.next(); }
  assert.ok(yields >= 20);
});

// Use the real elevation normalization and source identity helpers, extracted
// without importing the browser-only map runtime and its unrelated providers.
const mapRuntimeSource = await read("app/map-runtime.ts");
const realHelper = name => {
  const match = mapRuntimeSource.match(new RegExp(`export const ${name} = [\\s\\S]*?\\n};`));
  assert.ok(match, `${name} remains testable`);
  return match[0];
};
const runtimeHelpersUrl = toUrl(transpile(`export const TERRAIN_SOURCE_ID = "kfm-terrain-dem";\n${realHelper("terrainPresentationSourceMatches")}\n${realHelper("unexaggeratedTerrainElevation")}`));
const compositionUrl = toUrl(transpile((await read("app/map-layer-composition.ts"))
  .replace('"./explorer-data"', JSON.stringify(toUrl('export const LAYER_REGISTRY = [{ renderers: [{ id: "provider-data" }] }];')))));
const runtimeSource = (await read("app/terrain-drawing-runtime.ts"))
  .replace('"./map-runtime"', JSON.stringify(runtimeHelpersUrl))
  .replace('"./scene-effects"', JSON.stringify(toUrl('export const effectiveSceneLight = (_map,preset,azimuth) => ({preset,azimuth});')))
  .replace('"./terrain-sources"', JSON.stringify(toUrl('export const terrainSourceFor = provider => ({tileTemplate: provider});')))
  .replace('"./terrain-surface"', JSON.stringify(surfaceUrl))
  .replace('"./map-layer-composition"', JSON.stringify(compositionUrl))
  .replace('"./terrain-drawing"', JSON.stringify(modelUrl));
const runtime = await import(toUrl(transpile(runtimeSource)));
const activeConfig = { mode: "both", enabled: true, provider: "mapzen", efficient: true, detail: false, light: "clear", azimuth: 210 };

function fakeMap() {
  const handlers = new Map();
  const layers = [{ id: "provider-evidence", type: "symbol" }];
  const sources = new Map([["kfm-terrain-dem", { type: "raster-dem", tiles: ["mapzen"] }]]);
  const addedSources = [], published = [], paint = new Map(), featureStates = new Map(), moves = [];
  const state = { center: { lng: -98, lat: 38 }, zoom: 10, exaggeration: 1, projection: "mercator", terrain: true, queries: 0, reads: [], afterQuery: null };
  const map = {
    state, handlers, sources, addedSources, published, layers, paint, featureStates, moves,
    emit(type, event = {}) { for (const callback of [...handlers.get(type) ?? []]) callback(event); },
    on(type, callback) { if (!handlers.has(type)) handlers.set(type, new Set()); handlers.get(type).add(callback); },
    off(type, callback) { handlers.get(type)?.delete(callback); },
    getCenter: () => state.center, getZoom: () => state.zoom,
    getProjection: () => ({ type: state.projection }),
    getTerrain: () => state.terrain ? { source: "kfm-terrain-dem", exaggeration: state.exaggeration } : null,
    getSource: id => sources.get(id),
    getStyle: () => ({ layers, sources: Object.fromEntries(sources) }),
    getLayer: id => layers.find(layer => layer.id === id),
    queryTerrainElevation(coordinate) {
      state.queries += 1; state.reads.push(coordinate);
      const height = (500 + (coordinate[0] + 98) * 800 + (coordinate[1] - 38) * 500) * state.exaggeration;
      state.afterQuery?.(state.queries);
      return height;
    },
    addSource(id, spec) {
      addedSources.push([id, spec.type]);
      if (spec.data) published.push(spec.data);
      sources.set(id, { ...spec, setData(data) { this.data = data; published.push(data); map.emit("sourcedata", { sourceId: id, sourceDataType: "content" }); } });
      map.emit("styledata");
    },
    removeSource(id) { sources.delete(id); map.emit("styledata"); },
    addLayer(layer, before) { const index = layers.findIndex(item => item.id === before); layers.splice(index < 0 ? layers.length : index, 0, layer); map.emit("styledata"); },
    removeLayer(id) { const index = layers.findIndex(layer => layer.id === id); if (index !== -1) layers.splice(index, 1); map.emit("styledata"); },
    moveLayer(id, before) { moves.push([id, before]); const index = layers.findIndex(layer => layer.id === id); const [layer] = layers.splice(index, 1); const destination = layers.findIndex(layer => layer.id === before); layers.splice(destination < 0 ? layers.length : destination, 0, layer); map.emit("styledata"); },
    setFeatureState(feature, state) { featureStates.set(feature.id, state); },
    setLayoutProperty(id, property, value) { const layer = map.getLayer(id); layer.layout ??= {}; layer.layout[property] = value; },
    setPaintProperty(id, property, value) { paint.set(`${id}:${property}`, value); },
  };
  return map;
}

function setup(t, config = activeConfig) {
  t.mock.timers.enable({ apis: ["setTimeout", "Date"], now: 100_000 });
  const map = fakeMap(), statuses = [], probes = [];
  const controller = runtime.createTerrainDrawing(map, status => statuses.push(status), probe => probes.push(probe));
  controller.update(config);
  const flush = () => { for (let i = 0; i < 250; i += 1) t.mock.timers.tick(10); };
  t.after(() => controller.destroy());
  return { map, statuses, probes, controller, flush };
}

test("runtime draws only loaded samples with one GeoJSON source, bounded work and no DEM acquisition", t => {
  const { map, statuses, flush } = setup(t);
  flush();
  assert.equal(map.state.queries, 33 ** 2);
  assert.deepEqual(map.addedSources, [[runtime.TERRAIN_DRAWING_SOURCE_ID, "geojson"]]);
  assert.equal(statuses.at(-1).state, "ready");
  assert.equal(statuses.at(-1).sampleCount, 1089);
  assert.equal(statuses.at(-1).coverage, 1);
  assert.equal(map.layers.at(-1).id, "provider-evidence");
  for (const point of map.state.reads) assert.ok(point[0] >= -102.1 && point[0] <= -94.5 && point[1] >= 36.9 && point[1] <= 40.1);
});

test("exaggeration changes preserve source heights, contour bands and geometry", t => {
  const { map, controller, flush } = setup(t);
  flush();
  const first = structuredClone(map.published.at(-1));
  controller.update({ ...activeConfig, mode: "off" });
  map.state.exaggeration = 2;
  controller.update(activeConfig);
  flush();
  assert.deepEqual(map.published.at(-1), first);
});

test("off during a sampling batch cancels every late publication and removes its listeners on destroy", t => {
  const { map, controller, flush } = setup(t);
  map.state.afterQuery = count => { if (count === 128) controller.update({ ...activeConfig, mode: "off" }); };
  flush();
  assert.equal(map.state.queries, 128);
  assert.equal(map.published.length, 0);
  assert.equal(map.getSource(runtime.TERRAIN_DRAWING_SOURCE_ID), undefined);
  controller.destroy();
  for (const callbacks of map.handlers.values()) assert.equal(callbacks.size, 0);
  map.emit("sourcedata", { sourceId: "kfm-terrain-dem", sourceDataType: "content" });
  flush();
  assert.equal(map.state.queries, 128);
});

test("source replacement mid-batch cannot publish old samples under a new provider", t => {
  const { map, controller, flush } = setup(t);
  map.state.afterQuery = count => {
    if (count !== 128) return;
    map.sources.set("kfm-terrain-dem", { type: "raster-dem", tiles: ["usgs-3dep"] });
    map.emit("styledata");
  };
  flush();
  assert.equal(map.published.length, 0);
  controller.update({ ...activeConfig, provider: "usgs-3dep" });
  flush();
  assert.equal(map.published.length, 1);
  assert.equal(map.state.queries, 128 + 1089);
});

test("motion during a sampling turn stops at its 128-reading budget and cannot publish late", t => {
  const { map, flush } = setup(t);
  map.state.afterQuery = count => {
    if (count !== 128) return;
    map.emit("movestart");
    map.state.center = { lng: -98.1, lat: 38 };
    map.emit("move");
  };
  flush();
  assert.equal(map.state.queries, 128, "the next scheduled batch is cancelled");
  assert.equal(map.published.length, 0);
  map.emit("moveend"); flush();
  assert.equal(map.state.queries, 128 + 1089);
  assert.equal(map.published.length, 1);
});

test("DEM arrivals during sampling cause one coalesced trailing pass without discarding the first", t => {
  const { map, flush } = setup(t);
  map.state.afterQuery = count => {
    if (count !== 128) return;
    for (let i = 0; i < 100; i += 1) map.emit("sourcedata", { sourceId: "kfm-terrain-dem", sourceDataType: "content" });
  };
  flush();
  assert.equal(map.state.queries, 1089 * 2);
  assert.equal(map.published.length, 2);
  flush();
  assert.equal(map.state.queries, 1089 * 2);
});

test("pan removes stale lines immediately; pure orbit keeps finished geographic drawing", t => {
  const { map, flush } = setup(t);
  flush();
  const source = map.getSource(runtime.TERRAIN_DRAWING_SOURCE_ID), queries = map.state.queries;
  map.emit("movestart"); map.emit("move"); map.emit("moveend"); flush();
  assert.equal(map.getSource(runtime.TERRAIN_DRAWING_SOURCE_ID), source);
  assert.equal(map.state.queries, queries, "bearing and pitch do not invalidate a geographic patch");
  map.emit("movestart"); map.state.center = { lng: -97.99, lat: 38 }; map.emit("move");
  assert.equal(map.getSource(runtime.TERRAIN_DRAWING_SOURCE_ID), undefined);
  flush(); assert.equal(map.state.queries, queries, "moving camera cannot resample");
  map.emit("moveend"); flush();
  assert.equal(map.state.queries, queries + 1089);
  assert.ok(map.getSource(runtime.TERRAIN_DRAWING_SOURCE_ID));
});

test("light and mode changes restyle without sampling or replacing geometry", t => {
  const { map, controller, flush } = setup(t);
  flush(); const queries = map.state.queries, source = map.getSource(runtime.TERRAIN_DRAWING_SOURCE_ID);
  controller.update({ ...activeConfig, light: "dusk", mode: "contours" }); flush();
  assert.equal(map.state.queries, queries);
  assert.equal(map.getSource(runtime.TERRAIN_DRAWING_SOURCE_ID), source);
  assert.equal(map.getLayer("scene-terrain-grid").layout.visibility, "none");
  assert.equal(map.getLayer("scene-terrain-grid-casing").layout.visibility, "none");
  assert.equal(map.paint.get("scene-terrain-index:line-color"), "#fff1c6");
  assert.equal(map.paint.get("scene-terrain-contour-casing:line-color"), "#493329");
  controller.update({ ...activeConfig, mode: "grid" }); flush();
  assert.equal(map.getLayer("scene-terrain-grid").layout.visibility, "visible");
  assert.equal(map.getLayer("scene-terrain-contours").layout.visibility, "none");
  assert.equal(map.getLayer("scene-terrain-contour-casing").layout.visibility, "none");
  assert.equal(map.state.queries, queries);
});

test("only matching DEM content schedules work; burst events cannot starve or loop on setData", t => {
  const { map, flush } = setup(t);
  flush(); const queries = map.state.queries;
  for (const sourceId of [runtime.TERRAIN_DRAWING_SOURCE_ID, "unrelated", "kfm-terrain-shadow-dem"]) map.emit("sourcedata", { sourceId, sourceDataType: "content" });
  map.emit("sourcedata", { sourceId: "kfm-terrain-dem", sourceDataType: "metadata" });
  flush(); assert.equal(map.state.queries, queries);
  for (let i = 0; i < 100; i += 1) map.emit("sourcedata", { sourceId: "kfm-terrain-dem", sourceDataType: "content" });
  flush(); assert.equal(map.state.queries, queries + 1089);
  flush(); assert.equal(map.state.queries, queries + 1089, "own GeoJSON setData does not schedule another pass");
});

test("style replacement and disabled terrain clear lines; minimum zoom and globe never sample", t => {
  const { map, controller, statuses, flush } = setup(t);
  flush(); const queries = map.state.queries;
  map.sources.delete("kfm-terrain-dem"); map.emit("styledata");
  assert.equal(map.getSource(runtime.TERRAIN_DRAWING_SOURCE_ID), undefined);
  flush(); assert.equal(statuses.at(-1).state, "unavailable");
  map.sources.set("kfm-terrain-dem", { type: "raster-dem", tiles: ["mapzen"] }); map.emit("style.load"); flush();
  assert.equal(map.state.queries, queries + 1089);
  controller.update({ ...activeConfig, enabled: false });
  assert.equal(map.getSource(runtime.TERRAIN_DRAWING_SOURCE_ID), undefined);
  controller.update(activeConfig); map.state.zoom = 6; flush();
  assert.match(statuses.at(-1).message, /Zoom to 8.5/);
  map.state.zoom = 10; map.state.projection = "globe"; map.emit("style.load"); flush();
  assert.equal(map.state.queries, queries + 1089);
  assert.equal(statuses.at(-1).state, "unavailable");
});

test("Kansas zero readings stay empty and never become flat fabricated terrain", t => {
  const { map, statuses, flush } = setup(t);
  map.queryTerrainElevation = () => 0;
  flush();
  assert.equal(map.published.at(-1).features.length, 0);
  assert.equal(statuses.at(-1).coverage, 0);
  assert.equal(statuses.at(-1).state, "loading");
});

test("surface-only display shares sampling/source with contours; lens, opacity and light are paint-only", t => {
  const config = { ...activeConfig, mode: "off", surface: "slope", surfaceOpacity: .55 };
  const { map, controller, statuses, flush } = setup(t, config);
  flush();
  const queries = map.state.queries, data = structuredClone(map.published.at(-1));
  assert.equal(queries, 1089);
  assert.equal(statuses.at(-1).validCellCount, 31 ** 2);
  assert.equal(statuses.at(-1).totalCellCount, 31 ** 2);
  assert.equal(map.getLayer(runtime.TERRAIN_SURFACE_LAYER_ID).layout.visibility, "visible");
  assert.ok(runtime.TERRAIN_DRAWING_LAYER_IDS.every(id => map.getLayer(id).layout.visibility === "none"));
  assert.deepEqual(map.addedSources, [[runtime.TERRAIN_DRAWING_SOURCE_ID, "geojson"]]);
  assert.equal(data.features.filter(feature => feature.properties.role === "surface").length, 961);
  controller.update({ ...config, surface: "aspect", surfaceOpacity: .75, light: "night", mode: "contours" }); flush();
  assert.equal(map.state.queries, queries);
  assert.deepEqual(map.published.at(-1), data, "fixed scientific classes and colors are unchanged by a scene look");
  assert.deepEqual(map.paint.get(`${runtime.TERRAIN_SURFACE_LAYER_ID}:fill-color`), ["get", "aspectColor"]);
  assert.equal(map.paint.get(`${runtime.TERRAIN_SURFACE_LAYER_ID}:fill-opacity`), .75);
  assert.equal(map.getLayer("scene-terrain-contours").layout.visibility, "visible");
  controller.update({ ...config, surface: "off", mode: "grid" }); flush();
  assert.equal(map.getLayer(runtime.TERRAIN_SURFACE_LAYER_ID).layout.visibility, "none");
  assert.equal(map.state.queries, queries);
  controller.update({ ...config, surface: "off", mode: "off" });
  assert.equal(map.getSource(runtime.TERRAIN_DRAWING_SOURCE_ID), undefined);
  assert.equal(map.getLayer(runtime.TERRAIN_SURFACE_LAYER_ID), undefined);
});

test("surface probe deduplicates pointer/tap/center cells and clears on exit, lens and measurement", t => {
  const config = { ...activeConfig, surface: "slope" };
  const { map, controller, probes, flush } = setup(t, config);
  flush(); const reads = map.state.queries;
  const center = controller.probeCenter();
  assert.ok(center.slopeDegrees > 0 && center.elevationMeters === 500);
  assert.equal(probes.length, 1);
  map.emit("mousemove", { lngLat: { lng: -98, lat: 38 } });
  map.emit("click", { lngLat: { lng: -98, lat: 38 } });
  assert.equal(probes.length, 1, "same-cell movement and touch click do not rerender the page");
  assert.ok([...map.featureStates.values()].some(state => state.probed === true));
  map.emit("mousemove", { lngLat: { lng: -90, lat: 38 } });
  assert.equal(probes.at(-1), null);
  map.emit("click", { lngLat: { lng: -98, lat: 38 } });
  assert.equal(probes.at(-1).elevationMeters, 500);
  controller.update({ ...config, surface: "aspect" });
  assert.equal(probes.at(-1), null);
  assert.ok(controller.probeCenter());
  controller.update({ ...config, probeEnabled: false });
  assert.equal(probes.at(-1), null);
  assert.equal(controller.probeCenter(), null);
  assert.equal(map.state.queries, reads, "probing never queries the DEM again");
});

test("surface probe clears across orbit, pan, source changes and teardown; cached orbit cells survive", t => {
  const { map, controller, probes, flush } = setup(t, { ...activeConfig, surface: "aspect" });
  flush(); controller.probeCenter();
  const source = map.getSource(runtime.TERRAIN_DRAWING_SOURCE_ID), queries = map.state.queries;
  map.emit("movestart");
  assert.equal(probes.at(-1), null);
  assert.equal(controller.probeCenter(), null);
  map.emit("move"); map.emit("moveend"); flush();
  assert.equal(map.getSource(runtime.TERRAIN_DRAWING_SOURCE_ID), source);
  assert.equal(map.state.queries, queries);
  assert.ok(controller.probeCenter());
  map.sources.set("kfm-terrain-dem", { type: "raster-dem", tiles: ["usgs-3dep"] }); map.emit("styledata");
  assert.equal(probes.at(-1), null);
  assert.equal(controller.probeCenter(), null);
  assert.equal(map.getSource(runtime.TERRAIN_DRAWING_SOURCE_ID), undefined);
  controller.update({ ...activeConfig, surface: "aspect", provider: "usgs-3dep" }); flush();
  assert.ok(controller.probeCenter());
  controller.destroy();
  assert.equal(probes.at(-1), null);
  assert.equal(controller.probeCenter(), null);
  for (const callbacks of map.handlers.values()) assert.equal(callbacks.size, 0);
});

test("surface cells expose missing neighborhoods separately from loaded sample coverage", t => {
  const { map, statuses, controller, flush } = setup(t, { ...activeConfig, surface: "slope" });
  const query = map.queryTerrainElevation;
  map.queryTerrainElevation = point => point[0] === -98 && point[1] === 38 ? 0 : query(point);
  flush();
  assert.ok(statuses.at(-1).coverage > .99);
  assert.equal(statuses.at(-1).validCellCount, 31 ** 2 - 9);
  assert.equal(statuses.at(-1).totalCellCount, 31 ** 2);
  assert.equal(controller.probeCenter(), null);
});

test("surface fill remains above a later-added native tint and below contour casings and evidence", t => {
  const { map, flush } = setup(t, { ...activeConfig, surface: "slope" });
  flush();
  map.addLayer({ id: "kfm-terrain-color-relief", type: "color-relief" }, "provider-evidence");
  const index = id => map.layers.findIndex(layer => layer.id === id);
  assert.ok(index("kfm-terrain-color-relief") < index(runtime.TERRAIN_SURFACE_LAYER_ID));
  assert.ok(index(runtime.TERRAIN_SURFACE_LAYER_ID) < index(runtime.TERRAIN_DRAWING_LAYER_IDS[0]));
  assert.equal(map.layers.at(-1).id, "provider-evidence");
});

test("local base context is below surface and a late tint converges below actual evidence without reorder loops", t => {
  const { map, controller, flush } = setup(t, { ...activeConfig, surface: "slope" });
  map.layers.splice(0, map.layers.length,
    { id: "kfm-background", type: "background" }, { id: "kfm-orientation-land", type: "fill" },
    { id: "kfm-orientation-rivers", type: "line" }, { id: "provider-data", type: "circle" },
    { id: "kfm-selection-line", type: "line" });
  flush();
  const index = id => map.layers.findIndex(layer => layer.id === id);
  assert.ok(index("kfm-orientation-land") < index(runtime.TERRAIN_SURFACE_LAYER_ID));
  assert.ok(index("kfm-orientation-rivers") < index(runtime.TERRAIN_SURFACE_LAYER_ID));
  assert.ok(index(runtime.TERRAIN_SURFACE_LAYER_ID) < index("provider-data"));
  // A no-symbol local style appends native tint after the data layer.
  map.addLayer({ id: "kfm-terrain-color-relief", type: "color-relief" });
  assert.ok(index("kfm-terrain-color-relief") < index(runtime.TERRAIN_SURFACE_LAYER_ID));
  assert.ok(index(runtime.TERRAIN_DRAWING_LAYER_IDS.at(-1)) < index("provider-data"));
  const moves = map.moves.length;
  for (let i = 0; i < 5; i += 1) map.emit("styledata");
  controller.update({ ...activeConfig, surface: "aspect", light: "dusk" });
  assert.equal(map.moves.length, moves, "settled style and paint updates never move the group repeatedly");
});
