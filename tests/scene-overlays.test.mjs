import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const read = (path) => readFile(new URL(`../${path}`, import.meta.url), "utf8");
const toUrl = (javascript) => `data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`;
const transpile = (source) => ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;

// The settings registry is stubbed: each fake map carries its own settings.
const sceneEffectsStub = toUrl(`
export const sceneEffectsFor = (map) => map.fx;
export const effectiveSceneLight = (_map, preset, azimuth) => ({ preset, azimuth, altitude: 30, source: "manual" });
`);

async function loadOverlays() {
  let source = await read("app/scene-overlays.ts");
  const replacements = [
    ['from "./kansas-orientation";', `from "${toUrl(transpile(await read("app/kansas-orientation.ts")))}";`],
    ['from "./night-sky";', `from "${toUrl(transpile(await read("app/night-sky.ts")))}";`],
    ['from "./scene-effects";', `from "${sceneEffectsStub}";`],
  ];
  for (const [before, after] of replacements) {
    assert.ok(source.includes(before), `scene-overlays still imports ${before}`);
    source = source.replace(before, after);
  }
  return import(toUrl(transpile(source)));
}

const ALL_ON = { cinematic: true, curtain: true, sunSync: false, kansasGlow: true, relief2d: true, buildings: true, stars: true };

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

test("a category basemap's own hillshade follows the scene light and suppresses the second 2D relief", async () => {
  const overlays = await loadOverlays();
  const dem = { tileTemplate: "https://example.test/{z}/{x}/{y}.png", tileSize: 256, maxZoom: 11, encoding: "terrarium", attribution: "DEM" };
  const id = overlays.CATEGORY_BASEMAP_HILLSHADE_LAYER_ID;
  for (const relief2d of [true, false]) {
    const map = fakeMap({ fx: { ...ALL_ON, relief2d }, layers: [{ id: "kfm-background", type: "background" }, { id, type: "hillshade", paint: { "hillshade-illumination-direction": 315 } }] });
    map.paint.set(`${id}:hillshade-illumination-direction`, 315);
    overlays.syncRelief2d(map, dem, "dusk", 100);
    assert.equal(map.getPaintProperty(id, "hillshade-illumination-direction"), 100, "the dock's sun control moves the basemap's shadows");
    overlays.syncRelief2d(map, dem, "dusk", -45);
    assert.equal(map.getPaintProperty(id, "hillshade-illumination-direction"), 315, "normalized to 0–360");
    assert.equal(map.getLayer(overlays.RELIEF_2D_LAYER_ID), undefined, "no second hillshade is added");
    assert.equal(map.getSource(overlays.RELIEF_2D_SOURCE_ID), undefined);
  }
});

test("aviation and civic styles follow sun changes across flat, terrain and globe transitions", async () => {
  const vm = await import("node:vm");
  const modules = {
    "./category-basemaps": "app/category-basemaps.ts", "./category-basemap-keys": "app/category-basemap-keys.ts",
    "./external-context-sources": "app/external-context-sources.ts", "./kansas-orientation": "app/kansas-orientation.ts",
  };
  const cache = new Map();
  const compiled = Object.fromEntries(await Promise.all(Object.entries(modules).map(async ([id, path]) => [id,
    ts.transpileModule(await read(path), { compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 } }).outputText])));
  function load(id) {
    if (cache.has(id)) return cache.get(id);
    assert.ok(id in compiled, `known dependency ${id}`);
    const mod = { exports: {} }; cache.set(id, mod.exports);
    vm.runInNewContext(compiled[id], { module: mod, exports: mod.exports, require: load, URL });
    cache.set(id, mod.exports); return mod.exports;
  }
  const basemaps = load("./category-basemaps"), overlays = await loadOverlays();
  const id = basemaps.BASEMAP_HILLSHADE_LAYER_ID;
  const dem = { tileTemplate: "https://example.test/{z}/{x}/{y}.png", encoding: "terrarium", attribution: "test" };
  for (const key of ["aviation-chart", "civic"]) for (const relief2d of [true, false]) {
    for (const scene of [{ projection: "mercator", terrain: null }, { projection: "mercator", terrain: { source: "terrain" } }, { projection: "globe", terrain: null }]) {
      const style = basemaps.CATEGORY_BASEMAPS[key].style();
      const map = fakeMap({ ...scene, fx: { ...ALL_ON, relief2d }, layers: style.layers, sources: style.sources });
      const initial = style.layers.find(layer => layer.id === id).paint["hillshade-illumination-direction"];
      map.paint.set(`${id}:hillshade-illumination-direction`, initial);
      for (const [azimuth, expected] of [[90, 90], [235, 235], [-45, 315], [450, 90], [360, 0]]) {
        overlays.syncRelief2d(map, dem, "dusk", azimuth);
        assert.equal(map.getPaintProperty(id, "hillshade-illumination-direction"), expected, `${key}: ${scene.projection}, terrain=${!!scene.terrain}, relief=${relief2d}`);
        assert.equal(map.getLayer(overlays.RELIEF_2D_LAYER_ID), undefined, "category relief is never doubled");
      }
    }
  }
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

test("palette changes recolor decorative outlines in place, skip unchanged paints and restore offline colors on Plain", async () => {
  const overlays = await loadOverlays();
  const map = fakeMap({ layers: [
    { id: "orientation-kansas-glow", type: "line" },
    { id: "orientation-kansas-outline", type: "line" },
    { id: "provider-values", type: "circle" },
  ], sources: { "orientation-kansas": {} } });
  map.paint.set("orientation-kansas-glow:line-color", "#original-halo");
  map.paint.set("orientation-kansas-outline:line-color", "#original-edge");
  let writes = 0;
  const write = map.setPaintProperty;
  map.setPaintProperty = (...args) => { writes++; write(...args); };
  overlays.syncKansasGlow(map, "clear", 210);
  const source = map.getSource(overlays.KANSAS_GLOW_SOURCE_ID);
  const layer = map.getLayer("scene-kansas-glow-edge");
  for (const light of ["dusk", "night", "clear"]) {
    overlays.syncKansasGlow(map, light, 210);
    assert.equal(map.getSource(overlays.KANSAS_GLOW_SOURCE_ID), source);
    assert.equal(map.getLayer("scene-kansas-glow-edge"), layer);
    assert.equal(map.getPaintProperty("scene-kansas-glow-edge", "line-color"), overlays.KANSAS_GLOW_PALETTES[light][1]);
    assert.equal(map.getPaintProperty("orientation-kansas-outline", "line-color"), overlays.KANSAS_GLOW_PALETTES[light][1]);
    const unchanged = writes;
    overlays.syncKansasGlow(map, light, 210);
    assert.equal(writes, unchanged);
  }
  assert.equal(map.getPaintProperty("provider-values", "circle-color"), undefined, "provider palette never changes");
  map.fx = { ...ALL_ON, kansasGlow: false };
  overlays.syncKansasGlow(map, "dusk", 210);
  assert.equal(map.getPaintProperty("orientation-kansas-glow", "line-color"), "#original-halo");
  assert.equal(map.getPaintProperty("orientation-kansas-outline", "line-color"), "#original-edge");
});

const STARS_ON = { ...ALL_ON, stars: true };
const tick = () => new Promise((resolve) => setTimeout(resolve, 0));

test("the night sky sits beneath every layer and shows from orbit or under a dark tilted sky", async () => {
  const overlays = await loadOverlays();
  let loads = 0;
  overlays.setNightSkyCatalogLoader(async () => { loads += 1; return { count: 1, stars: [101.287, -16.716, -1.44, 0.01] }; });
  const base = [{ id: "background", type: "background" }, { id: "roads", type: "line" }];

  const night = fakeMap({ fx: STARS_ON, pitch: 70, layers: base });
  night.triggerRepaint = () => { night.repaints = (night.repaints ?? 0) + 1; };
  assert.equal(overlays.syncNightSky(night, "night", 210, false), true);
  assert.equal(night.style.layers[0].id, overlays.NIGHT_SKY_LAYER_ID, "below the basemap");
  assert.equal(night.style.layers[0].type, "custom");
  assert.equal(night.getLayoutProperty(overlays.NIGHT_SKY_LAYER_ID, "visibility"), "visible");
  assert.equal(overlays.nightSkyIsTwinkling(night), true, "stars twinkle through air");
  await tick();
  assert.equal(loads, 1, "catalog fetched once, when first shown");
  assert.ok(night.repaints >= 1, "map repaints once the catalog arrives");

  const day = fakeMap({ fx: STARS_ON, pitch: 70, layers: base });
  overlays.syncNightSky(day, "clear", 210, false);
  assert.equal(day.getLayoutProperty(overlays.NIGHT_SKY_LAYER_ID, "visibility"), "none", "no stars in a blue sky");

  const flat = fakeMap({ fx: STARS_ON, pitch: 20, layers: base });
  overlays.syncNightSky(flat, "night", 210, false);
  assert.equal(flat.getLayoutProperty(overlays.NIGHT_SKY_LAYER_ID, "visibility"), "none", "no horizon in view");

  const orbit = fakeMap({ fx: STARS_ON, pitch: 0, projection: "globe", layers: base });
  orbit.triggerRepaint = () => {};
  overlays.syncNightSky(orbit, "clear", 210, false);
  assert.equal(orbit.getLayoutProperty(overlays.NIGHT_SKY_LAYER_ID, "visibility"), "visible", "space is dark by day");
  assert.equal(overlays.nightSkyIsTwinkling(orbit), false, "no twinkle above the atmosphere");

  overlays.syncNightSky(orbit, "clear", 210, true);
  assert.equal(orbit.getLayoutProperty(overlays.NIGHT_SKY_LAYER_ID, "visibility"), "none", "Battery saver");
  await tick();
  assert.equal(loads, 1, "a loaded catalog is reused");
});

test("the night sky is removed when switched off, and a failure to add it never breaks the map", async () => {
  const overlays = await loadOverlays();
  overlays.setNightSkyCatalogLoader(async () => ({ count: 0, stars: [] }));
  const map = fakeMap({ fx: STARS_ON, pitch: 70, layers: [{ id: "background", type: "background" }] });
  map.triggerRepaint = () => {};
  overlays.syncNightSky(map, "night", 210, false);
  assert.ok(map.getLayer(overlays.NIGHT_SKY_LAYER_ID));
  map.fx = { ...STARS_ON, stars: false };
  assert.equal(overlays.syncNightSky(map, "night", 210, false), true);
  assert.equal(map.getLayer(overlays.NIGHT_SKY_LAYER_ID), undefined);

  const broken = fakeMap({ fx: STARS_ON, pitch: 70 });
  broken.addLayer = () => { throw new Error("WebGL context lost"); };
  assert.equal(overlays.syncNightSky(broken, "night", 210, false), false);
  assert.equal(broken.getLayer(overlays.NIGHT_SKY_LAYER_ID), undefined);
});
