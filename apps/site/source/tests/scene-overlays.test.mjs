import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const read = (path) => readFile(new URL(`../${path}`, import.meta.url), "utf8");
const toUrl = (javascript) => `data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`;
const transpile = (source) => ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;

// The settings registry is stubbed: each fake map carries its own settings.
const sceneEffectsStub = toUrl(`
export const CURTAIN_MIN_PITCH = 12;
export const sceneEffectsFor = (map) => map.fx;
export const effectiveSceneLight = (_map, preset, azimuth) => ({ preset, azimuth, altitude: 30, source: "manual" });
`);

async function loadOverlays() {
  let source = await read("app/scene-overlays.ts");
  const replacements = [
    ['from "./kansas-orientation";', `from "${toUrl(transpile(await read("app/kansas-orientation.ts")))}";`],
    ['from "./map-performance";', `from "${toUrl(transpile(await read("app/map-performance.ts")))}";`],
    ['from "./scene-effects";', `from "${sceneEffectsStub}";`],
  ];
  for (const [before, after] of replacements) {
    assert.ok(source.includes(before), `scene-overlays still imports ${before}`);
    source = source.replace(before, after);
  }
  return import(toUrl(transpile(source)));
}

const ALL_ON = { cinematic: true, curtain: true, sunSync: false, kansasGlow: true, relief2d: true, columns: true, buildings: true };

/** A small in-memory stand-in for the MapLibre style API. */
function fakeMap({ fx = ALL_ON, pitch = 50, projection = "mercator", terrain = null, layers = [], sources = {} } = {}) {
  const style = { layers: layers.map((layer) => ({ ...layer })), sources: { ...sources } };
  const paint = new Map();
  const layout = new Map();
  return {
    fx, style, paint, layout,
    getPitch: () => pitch,
    getProjection: () => ({ type: projection }),
    getTerrain: () => terrain,
    getStyle: () => ({ layers: style.layers, sources: style.sources }),
    getLayer: (id) => style.layers.find((layer) => layer.id === id),
    getSource: (id) => style.sources[id],
    addSource(id, spec) { style.sources[id] = { ...spec, setData(data) { this.data = data; } }; },
    removeSource(id) { delete style.sources[id]; },
    addLayer(layer, beforeId) {
      const index = beforeId ? style.layers.findIndex((candidate) => candidate.id === beforeId) : -1;
      style.layers.splice(index < 0 ? style.layers.length : index, 0, { ...layer });
      for (const [key, value] of Object.entries(layer.layout ?? {})) layout.set(`${layer.id}:${key}`, value);
      for (const [key, value] of Object.entries(layer.paint ?? {})) paint.set(`${layer.id}:${key}`, value);
    },
    removeLayer(id) { style.layers = style.layers.filter((layer) => layer.id !== id); },
    getLayoutProperty: (id, key) => layout.get(`${id}:${key}`),
    setLayoutProperty: (id, key, value) => layout.set(`${id}:${key}`, value),
    getPaintProperty: (id, key) => paint.get(`${id}:${key}`),
    setPaintProperty: (id, key, value) => paint.set(`${id}:${key}`, value),
  };
}

test("columns encode only provider values; missing or zero values draw nothing", async () => {
  const overlays = await loadOverlays();
  assert.equal(overlays.columnValue("earthquake", { magnitude: null }), null);
  assert.equal(overlays.columnValue("earthquake", {}), null);
  assert.equal(overlays.columnValue("earthquake", { magnitude: -1 }), null);
  assert.equal(overlays.columnValue("earthquake", { magnitude: 6 }).h, 1);
  assert.equal(overlays.columnValue("earthquake", { magnitude: 3 }).h, 0.5);
  assert.equal(overlays.columnValue("earthquake", { magnitude: 0 }).h, 0.04, "a recorded zero still marks its location");
  assert.equal(overlays.columnValue("streamflow", { value: 0, visualMagnitude: 0 }), null, "zero flow draws no column");
  assert.equal(overlays.columnValue("streamflow", { value: 12, visualMagnitude: 1.1, missing: true }), null);
  assert.equal(overlays.columnValue("streamflow", { value: 100, visualMagnitude: 2.5, trend: "rising" }).color, "#55e6ff");
  assert.equal(overlays.earthquakeColumnColor(0), "#ffd7a8");
  assert.equal(overlays.earthquakeColumnColor(6), "#d9364f");
  assert.equal(overlays.earthquakeColumnColor(9), "#d9364f");
});

test("column footprints are closed hexagons and the feature count is capped", async () => {
  const overlays = await loadOverlays();
  const ring = overlays.hexagon([-98, 38], 1000).coordinates[0];
  assert.equal(ring.length, 7);
  assert.deepEqual(ring[0], ring[6]);
  const point = (index) => ({ type: "Feature", properties: { magnitude: 2, featureId: `e${index}` }, geometry: { type: "Point", coordinates: [-98 + index * 0.0001, 38] } });
  const many = { type: "FeatureCollection", features: Array.from({ length: overlays.MAX_COLUMNS + 50 }, (_, index) => point(index)) };
  const built = overlays.buildValueColumns([{ kind: "earthquake", data: many }]);
  assert.equal(built.features.length, overlays.MAX_COLUMNS);
  assert.equal(built.features[0].properties.id, "e0");
  const mixed = { type: "FeatureCollection", features: [point(1), { type: "Feature", properties: { magnitude: 4 }, geometry: { type: "LineString", coordinates: [[0, 0], [1, 1]] } }, { type: "Feature", properties: { magnitude: 4 }, geometry: { type: "Point", coordinates: [0, 89] } }] };
  assert.equal(overlays.buildValueColumns([{ kind: "earthquake", data: mixed }]).features.length, 1, "non-points and polar points are skipped");
});

test("columns follow the official point layer's visibility and appear only when tilted", async () => {
  const overlays = await loadOverlays();
  const feeds = [{ kind: "earthquake", sourceId: "quakes", pointLayerId: "quake-points" }];
  const map = fakeMap({ layers: [{ id: "quake-points", type: "circle" }], sources: { quakes: {} } });
  map.layout.set("quake-points:visibility", "none");
  overlays.syncValueColumns(map, feeds, false);
  assert.equal(map.getSource(overlays.COLUMNS_SOURCE_ID).data.features.length, 0, "hidden point layer contributes no columns");
  assert.equal(map.style.layers[0].id, overlays.COLUMNS_LAYER_ID, "columns sit beneath the point symbols");
  assert.equal(map.getLayoutProperty(overlays.COLUMNS_LAYER_ID, "visibility"), "visible");
  const flat = fakeMap({ pitch: 0, layers: [{ id: "quake-points", type: "circle" }] });
  overlays.syncValueColumns(flat, feeds, false);
  assert.equal(flat.getLayoutProperty(overlays.COLUMNS_LAYER_ID, "visibility"), "none");
  const saver = fakeMap({ layers: [{ id: "quake-points", type: "circle" }] });
  overlays.syncValueColumns(saver, feeds, true);
  assert.equal(saver.getLayoutProperty(overlays.COLUMNS_LAYER_ID, "visibility"), "none", "Battery saver hides columns");
  map.fx = { ...ALL_ON, columns: false };
  overlays.syncValueColumns(map, feeds, false);
  assert.equal(map.getLayer(overlays.COLUMNS_LAYER_ID), undefined);
  assert.equal(map.getSource(overlays.COLUMNS_SOURCE_ID), undefined);
});

test("2D relief appears only on flat Mercator maps and removes its DEM source when off", async () => {
  const overlays = await loadOverlays();
  assert.equal(overlays.relief2dShouldShow(true, false, "mercator"), true);
  assert.equal(overlays.relief2dShouldShow(true, true, "mercator"), false, "Terrain 3D has its own relief");
  assert.equal(overlays.relief2dShouldShow(true, false, "globe"), false);
  assert.equal(overlays.relief2dShouldShow(false, false, "mercator"), false);
  const dem = { tileTemplate: "https://example.test/{z}/{x}/{y}.png", tileSize: 256, maxZoom: 11, encoding: "terrarium", attribution: "DEM" };
  const map = fakeMap({ layers: [{ id: "background", type: "background" }, { id: "external-data", type: "circle" }] });
  overlays.syncRelief2d(map, dem, "dusk", 235);
  assert.equal(map.getSource(overlays.RELIEF_2D_SOURCE_ID).type, "raster-dem");
  assert.deepEqual(map.style.layers.map((layer) => layer.id), ["background", overlays.RELIEF_2D_LAYER_ID, "external-data"], "relief stays under data overlays");
  assert.equal(map.getPaintProperty(overlays.RELIEF_2D_LAYER_ID, "hillshade-illumination-direction"), 235);
  overlays.syncRelief2d(map, dem, "dusk", 90);
  assert.equal(map.getPaintProperty(overlays.RELIEF_2D_LAYER_ID, "hillshade-illumination-direction"), 90, "light direction follows the scene");
  map.fx = { ...ALL_ON, relief2d: false };
  overlays.syncRelief2d(map, dem, "dusk", 90);
  assert.equal(map.getSource(overlays.RELIEF_2D_SOURCE_ID), undefined, "no DEM requests once off");
});

test("Kansas glow adds a beacon everywhere and defers to the offline styles' own outline", async () => {
  const overlays = await loadOverlays();
  for (const layer of overlays.kansasGlowLayers()) {
    assert.doesNotMatch(layer.id, /^kfm-/, "kept out of overlay ordering");
    assert.notEqual(layer.type, "symbol", "no glyph dependency");
  }
  const online = fakeMap();
  overlays.syncKansasGlow(online);
  assert.ok(overlays.KANSAS_GLOW_LAYER_IDS.every((id) => online.getLayoutProperty(id, "visibility") === "visible"));
  const offline = fakeMap({ sources: { "orientation-kansas": {} } });
  overlays.syncKansasGlow(offline);
  assert.equal(offline.getLayoutProperty("scene-kansas-glow-halo", "visibility"), "none");
  assert.equal(offline.getLayoutProperty("scene-kansas-beacon", "visibility"), "visible");
  online.fx = { ...ALL_ON, kansasGlow: false };
  overlays.syncKansasGlow(online);
  assert.equal(online.getSource(overlays.KANSAS_GLOW_SOURCE_ID), undefined);
});

test("building styling uses provider heights only and restores the style's own paint", async () => {
  const overlays = await loadOverlays();
  const map = fakeMap({ layers: [{ id: "building-3d", type: "fill-extrusion" }] });
  map.paint.set("building-3d:fill-extrusion-color", "#provider");
  map.paint.set("building-3d:fill-extrusion-opacity", 0.6);
  overlays.syncBuildingStyle(map, "dusk", 200);
  const color = map.getPaintProperty("building-3d", "fill-extrusion-color");
  assert.deepEqual(color.slice(0, 3), ["interpolate", ["linear"], ["coalesce", ["get", "render_height"], 0]]);
  assert.equal(map.getPaintProperty("building-3d", "fill-extrusion-height"), undefined, "heights are never written");
  map.fx = { ...ALL_ON, buildings: false };
  overlays.syncBuildingStyle(map, "dusk", 200);
  assert.equal(map.getPaintProperty("building-3d", "fill-extrusion-color"), "#provider");
  assert.equal(map.getPaintProperty("building-3d", "fill-extrusion-opacity"), 0.6);
  const noBuildings = fakeMap();
  overlays.syncBuildingStyle(noBuildings, "dusk", 200);
  assert.equal(noBuildings.paint.size, 0, "styles without the provider layer are untouched");
});
