import assert from "node:assert/strict";
import test from "node:test";
import { componentHarness, findNode, settle } from "./component-harness.mjs";

const snapshot = {
  basemap: "standard", representation: "2D", projection: "mercator", visibleLayers: [],
  camera: { center: [-97.8, 38.8], zoom: 11, pitch: 0, bearing: 0 },
  area: { kind: "viewport" }, committedTime: { start: 2026, end: 2026 },
};
async function harness() {
  let terrainState = "LOADING";
  const maps = [];
  const terrain = [], styles = [], moves = [], statuses = [];
  class Map {
    listeners = {}; loaded = false;
    constructor(options) { maps.push(this); styles.push(options.style); }
    on(name, handler) { this.listeners[name] = handler; }
    emit(name) { this.loaded = true; this.listeners[name]?.(); }
    isStyleLoaded() { return this.loaded; }
    addControl() {} setProjection() {} resize() {} remove() {}
    setStyle(style) { styles.push(style); this.loaded = false; }
    jumpTo(camera) { moves.push(camera); this.listeners.move?.(); }
  }
  const h = await componentHarness("app/snapshot-map.tsx", {
    "./basemap-cache": { basemapCacheRequest: url => ({url}) },
    "./maplibre-seam": { loadMapLibre: async () => ({ Map, setWorkerUrl() {}, NavigationControl: class {}, ScaleControl: class {} }) },
    "./explorer-data": { LAYER_REGISTRY: [] },
    "./map-runtime": { BASEMAPS: { standard: { style: "vector" }, imagery: { style: "imagery" } }, applyRegistryState() {}, updateAnalysisAreaSource() {}, updateSelectionSource() {},
      setTerrainPresentation: (...args) => { terrain.push(args.slice(1)); return terrainState; } },
    "./terrain-sources": { terrainSourceFor: provider => ({ id: provider }) },
    "./scene-effects": { readSceneEffects: () => ({ cinematic: true, curtain: true, sunSync: false }), registerSceneEffects() {} },
    "./temporal-sweep": { isFeatureAvailableForTemporalQuery: () => true },
    "./map-performance": { browserRenderBudget: () => ({ pixelRatio: 1, tileCache: 48 }) },
  }, { document: { createElement: () => ({ getContext: () => ({}) }) }, ResizeObserver: class { observe() {} disconnect() {} } });
  function render(state, onCameraChange = camera => statuses.push(camera)) {
    const tree = h.render(h.exports.default, { snapshot: state, label: "Test scene", onCameraChange });
    findNode(tree, n => n.props?.ref && n.type === "div").props.ref.current = {};
    h.commit();
    return tree;
  }
  return { h, render, terrain, styles, moves, statuses, map: () => maps.at(-1), failTerrain: () => { terrainState = "ERROR"; } };
}
test("story scenes restore their basemap, terrain source and scale after the new style loads", async () => {
  const t = await harness(); t.render(snapshot); await settle(); t.map().emit("load");
  const before = t.terrain.length;
  const next = { ...snapshot, basemap: "imagery", representation: "Terrain 3D", terrainProvider: "usgs-3dep", terrainExaggeration: 1.35 };
  t.render(next);
  assert.deepEqual(t.styles, ["vector", "imagery"]);
  assert.equal(t.terrain.length, before, "do not mutate the style before it loads");
  t.map().emit("style.load");
  assert.equal(t.terrain.at(-1)[0], true);
  assert.equal(t.terrain.at(-1)[1], 1.35);
  assert.equal(t.terrain.at(-1)[2].id, "usgs-3dep");
  assert.equal(t.moves.at(-1), next.camera);
  assert.equal(t.statuses.length, 0, "restoration must not feed camera synchronization back to its owner");
  t.h.dispose();
});
test("a redacted story scene resets a previous precise camera and legacy terrain keeps its default", async () => {
  const t = await harness(); t.render({ ...snapshot, representation: "Terrain 3D" }); await settle(); t.map().emit("load");
  assert.equal(t.terrain.at(-1)[1], 1);
  assert.equal(t.terrain.at(-1)[2].id, "mapzen");
  t.render({ ...snapshot, camera: { center: "WITHHELD_BROWSER_LOCATION" } });
  assert.equal(JSON.stringify(t.moves.at(-1)), JSON.stringify({ center: [-98.38, 38.48], zoom: 5.4, bearing: 0, pitch: 0 }));
  assert.equal(t.terrain.at(-1)[0], false);
  t.h.dispose();
});
test("snapshot terrain failures remain visible without hiding scene details", async () => {
  const t = await harness(); t.render(snapshot); await settle(); t.failTerrain(); t.map().emit("load");
  const tree = t.render(snapshot);
  assert.match(findNode(tree, n => n.type === "figcaption").props.children, /MAP_RENDER_FAILED/);
  t.h.dispose();
});
