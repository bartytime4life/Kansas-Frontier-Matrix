import assert from "node:assert/strict";
import test from "node:test";
import { componentHarness, findNode, settle } from "./component-harness.mjs";

const snapshot = {
  basemap: "standard", representation: "2D", projection: "mercator", visibleLayers: [],
  camera: { center: [-97.8, 38.8], zoom: 11, pitch: 0, bearing: 0 },
  area: { kind: "viewport" }, committedTime: { start: 2026, end: 2026 },
};
const temporal = (await componentHarness("app/temporal-sweep.ts", {})).exports;
const deferred = () => { let resolve, reject; const promise = new Promise((done, fail) => { resolve = done; reject = fail; }); return { promise, resolve, reject }; };
const textOf = node => typeof node === "string" || typeof node === "number" ? String(node) : node && typeof node === "object" ? [node.props?.children].flat(Infinity).map(textOf).join(" ").replace(/\s+/g, " ") : "";
const statusOf = tree => textOf(findNode(tree, node => node.props?.role === "status" || node.props?.role === "alert"));
const action = tree => findNode(tree, node => node.type === "button");
async function harness(options = {}) {
  let terrainState = "LOADING";
  const maps = [], observers = [], timers = new globalThis.Map(); let serial = 0, acquisitions = 0, webgl = true;
  const terrain = [], styles = [], moves = [], statuses = [], registry = [], selections = [], areas = [], effects = [];
  class Map {
    listeners = {}; loaded = false; removed = false; removals = 0;
    constructor(config) { this.config = config; this.maxPitch = config.maxPitch; maps.push(this); styles.push(config.style); if (options.failConstruction?.()) throw new Error("Synthetic renderer failure"); }
    on(name, handler) { this.listeners[name] = handler; }
    emit(name) { if (name === "load" || name === "style.load") this.loaded = true; this.listeners[name]?.(); }
    isStyleLoaded() { return this.loaded; }
    addControl() {} setProjection() {} resize() { if (this.removed) throw new Error("removed"); }
    remove() { this.removed = true; this.removals++; }
    setMaxPitch(value) { this.maxPitch = value; }
    setStyle(style) { if (options.failStyle?.()) throw new Error("Synthetic style failure"); styles.push(style); this.loaded = false; }
    jumpTo(camera) { moves.push(camera); this.camera = { ...camera, pitch:Math.min(this.maxPitch, camera.pitch) }; this.listeners.move?.(); }
    getCenter() { return { toArray:() => this.camera.center }; } getZoom() { return this.camera.zoom; } getBearing() { return this.camera.bearing; } getPitch() { return this.camera.pitch; }
  }
  const lib = { Map, setWorkerUrl() {}, NavigationControl: class {}, ScaleControl: class {} };
  const h = await componentHarness("app/snapshot-map.tsx", {
    "./basemap-cache": { basemapCacheRequest: url => ({url}) },
    "./maplibre-seam": { loadMapLibre: () => options.acquire ? options.acquire(++acquisitions, lib) : Promise.resolve(lib) },
    "./explorer-data": { LAYER_REGISTRY: options.layers ?? [] },
    "./map-runtime": { BASEMAPS: { standard: { style: "vector" }, imagery: { style: "imagery" } }, applyRegistryState:(...args) => registry.push(args.slice(1)), updateAnalysisAreaSource:(_map, area) => areas.push(area), updateSelectionSource:(_map, selected) => selections.push(selected),
      setTerrainPresentation: (...args) => { terrain.push(args.slice(1)); return terrainState; } },
    "./terrain-sources": { terrainSourceFor: provider => ({ id: provider }) },
    "./scene-effects": { readSceneEffects: () => ({ cinematic: true, curtain: true, sunSync: false }), registerSceneEffects:(_map, settings) => effects.push(settings) },
    "./temporal-sweep": temporal,
    "./map-performance": { browserRenderBudget: () => ({ pixelRatio: 1, tileCache: 48 }) },
    "./webgl-support": { webgl2Available: () => webgl },
  }, { ResizeObserver: class { constructor(callback) { this.callback = callback; observers.push(this); } observe() {} disconnect() { this.disconnected = true; } },
    setTimeout:(fn, delay) => { const id = ++serial; timers.set(id, { fn, delay }); return id; }, clearTimeout:id => timers.delete(id) });
  let state = snapshot;
  function render(next = state, onCameraChange = camera => statuses.push(camera)) {
    state = next;
    const tree = h.render(h.exports.default, { snapshot: state, label: "Test scene", onCameraChange });
    findNode(tree, n => n.props?.ref && n.type === "div").props.ref.current = {};
    h.commit();
    return tree;
  }
  return { h, render, terrain, styles, moves, statuses, maps, registry, selections, areas, effects, observers, timers, map: () => maps.at(-1), failTerrain: () => { terrainState = "ERROR"; }, webgl:value => { webgl = value; },
    expire() { const timer = [...timers].find(([, value]) => value.delay === 15_000); assert.ok(timer, "a whole-readiness deadline must be active"); timers.delete(timer[0]); timer[1].fn(); } };
}
test("story scenes restore their basemap, terrain source and scale after the new style loads", async () => {
  const t = await harness(); t.render(snapshot); await settle(); t.map().emit("load");
  const before = t.terrain.length;
  const next = { ...snapshot, basemap: "imagery", representation: "Terrain 3D", terrainProvider: "usgs-3dep", terrainExaggeration: 1.35, camera:{ ...snapshot.camera, pitch:72 } };
  t.render(next);
  assert.deepEqual(t.styles, ["vector", "imagery"]);
  assert.equal(t.terrain.length, before, "do not mutate the style before it loads");
  t.map().emit("style.load");
  assert.equal(t.terrain.at(-1)[0], true);
  assert.equal(t.terrain.at(-1)[1], 1.35);
  assert.equal(t.terrain.at(-1)[2].id, "usgs-3dep");
  assert.equal(t.moves.at(-1), next.camera);
  assert.equal(t.map().camera.pitch, 72, "a captured Explorer terrain camera must not clamp to 60 degrees");
  assert.equal(t.timers.size, 0);
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
  assert.match(statusOf(tree), /MAP_RENDER_FAILED/);
  assert.equal(action(tree).props.children, "Retry preview"); assert.equal(t.timers.size, 0);
  t.h.dispose();
});

test("initial terrain construction accepts the captured 72-degree camera and retains scene effects", async () => {
  const t = await harness(); t.render({ ...snapshot, representation:"Terrain 3D", camera:{ ...snapshot.camera, pitch:72 } }); await settle(); t.map().emit("load");
  assert.equal(t.map().config.maxPitch, 72); assert.equal(t.map().camera.pitch, 72); assert.equal(t.effects.length, 1); assert.equal(t.effects[0].cinematic, true);
  t.render(snapshot); assert.equal(t.map().maxPitch, 60); assert.equal(t.map().camera.pitch, 0); t.h.dispose();
});

test("a stalled adapter has a finite whole-attempt deadline and retry uses the latest snapshot", async () => {
  const late = deferred(); const t = await harness({ acquire:(count, lib) => count === 1 ? late.promise : Promise.resolve(lib) });
  let tree = t.render(); await settle(); assert.equal(action(tree).props.children, "Restart preview"); assert.equal(Boolean(action(tree).props.disabled), false);
  t.expire(); tree = t.render(); assert.match(statusOf(tree), /timed out.*Retry.*scene details.*Provider overlays are not replayed/); assert.ok(findNode(tree, n => n.props?.role === "alert")); assert.equal(t.timers.size, 0);
  const next = { ...snapshot, basemap:"imagery", camera:{ ...snapshot.camera, center:[-96.5, 38.5] } }; tree = t.render(next);
  action(tree).props.onClick(); t.render(); await settle(); const fresh = t.map(); assert.equal(fresh.config.style, "imagery"); fresh.emit("load");
  assert.equal(fresh.camera.center, next.camera.center); assert.match(statusOf(t.render()), /Saved map context.*provider overlays are not replayed/);
  late.resolve({ Map:class { constructor() { throw new Error("late adapter must not construct a map"); } } }); await settle(); assert.equal(t.maps.length, 1); assert.match(statusOf(t.render()), /Saved map context/); t.h.dispose(); assert.equal(t.timers.size, 0);
});

test("adapter time and stalled style share one deadline; a timed-out map cannot update a replacement", async () => {
  const pending = deferred(); let runtime;
  const t = await harness({ acquire:(count, lib) => { runtime = lib; return count === 1 ? pending.promise : Promise.resolve(lib); } });
  t.render(); const timer = [...t.timers.keys()][0]; pending.resolve(runtime); await settle(); const old = t.map(); assert.equal([...t.timers.keys()][0], timer, "adapter completion must not extend style readiness");
  t.expire(); let tree = t.render(); assert.equal(old.removed, true); assert.equal(t.observers[0].disconnected, true); assert.match(statusOf(tree), /timed out/);
  action(tree).props.onClick(); t.render(); await settle(); const fresh = t.map(); old.emit("error"); old.emit("load"); t.observers[0].callback();
  assert.match(statusOf(t.render()), /Loading map context/); assert.equal(fresh.loaded, false); fresh.emit("load"); assert.match(statusOf(t.render()), /Saved map context/); t.h.dispose(); assert.equal(fresh.removals, 1); assert.equal(old.removals, 1);
});

test("resource errors remain visible through incidental load or snapshot application until fresh retry succeeds", async () => {
  const t = await harness(); t.render(); await settle(); const old = t.map(); old.emit("error"); let tree = t.render(); const failure = statusOf(tree);
  assert.match(failure, /Some map context is unavailable/); old.emit("style.load"); old.emit("load");
  tree = t.render({ ...snapshot, camera:{ ...snapshot.camera, zoom:12 } }); assert.equal(statusOf(tree), failure); assert.equal(action(tree).props.children, "Retry preview");
  action(tree).props.onClick(); t.render(); await settle(); t.map().emit("load"); tree = t.render(); assert.match(statusOf(tree), /Saved map context/); assert.equal(findNode(tree, n => n.props?.role === "alert"), undefined); assert.equal(t.map().camera.zoom, 12); t.h.dispose();
});

test("restart and unmount remove maps, deadlines and observers and ignore all old callbacks", async () => {
  for (const stage of ["adapter", "style"]) {
    const late = deferred(); const t = await harness({ acquire:(count, lib) => stage === "adapter" && count === 1 ? late.promise : Promise.resolve(lib) });
    t.render(); await settle(); const old = t.map(); action(t.render()).props.onClick(); t.render(); await settle(); const fresh = t.map();
    assert.equal(t.timers.size, 1); if (old) { assert.equal(old.removed, true); old.emit("load"); old.emit("error"); old.listeners.move?.(); }
    assert.match(statusOf(t.render()), /Loading map context/); assert.equal(t.statuses.length, 0);
    t.h.dispose(); assert.equal(t.timers.size, 0); assert.equal(fresh.removed, true); assert.ok(t.observers.every(observer => observer.disconnected));
    fresh.emit("load"); fresh.emit("error"); fresh.listeners.move?.(); assert.equal(t.statuses.length, 0);
    late.resolve({ Map:class { constructor() { throw new Error("disposed adapter must not construct a map"); } } }); await settle(); assert.equal(t.timers.size, 0);
  }
});

test("readiness covers later basemap changes and preserves failed style guidance", async () => {
  let failStyle = false; const t = await harness({ failStyle:() => failStyle }); t.render(); await settle(); t.map().emit("load"); assert.equal(t.timers.size, 0);
  t.render({ ...snapshot, basemap:"imagery" }); assert.equal(t.timers.size, 1); assert.match(statusOf(t.render()), /Loading saved basemap/); t.expire(); assert.match(statusOf(t.render()), /timed out/);
  action(t.render()).props.onClick(); t.render(); await settle(); t.map().emit("load"); failStyle = true;
  let tree = t.render(snapshot); tree = t.render(); assert.match(statusOf(tree), /Snapshot basemap update.*MAP_RENDER_FAILED/); assert.equal(t.timers.size, 0); t.map().emit("style.load"); assert.match(statusOf(t.render()), /MAP_RENDER_FAILED/); t.h.dispose();
});

test("retry retains registry time, filter, order, selection eligibility and AOI boundaries", async () => {
  const selected = { properties:{ fid:"record-a", year:2000, evidenceState:"ANSWER" } };
  const layer = { id:"layer-a", temporal:{ mode:"instant" }, data:{ features:[selected] } };
  const t = await harness({ layers:[layer] });
  const state = { ...snapshot, visibleLayers:[{ id:layer.id, opacity:0.4 }], selection:{ layerId:layer.id, featureId:"record-a" }, evidenceFilter:"ANSWER", temporalSweep:{ mode:"snapshot", frame:2000, rangeStart:2000, rangeEnd:2000, windowStart:2000 }, area:{ kind:"aoi", bounds:{ west:-99, south:38, east:-98, north:39 } } };
  t.render(state); await settle(); t.map().emit("error"); action(t.render()).props.onClick(); t.render(); await settle(); t.map().emit("load");
  const [visible, opacity, year, order, filter, query] = t.registry.at(-1);
  assert.equal(visible[layer.id], true); assert.equal(opacity[layer.id], 0.4); assert.equal(year, 2000); assert.equal(order[0], layer.id); assert.equal(filter, "ANSWER"); assert.equal(query.frame, 2000); assert.equal(t.selections.at(-1), selected); assert.equal(t.areas.at(-1), state.area.bounds);
  t.render({ ...state, evidenceFilter:"MISSING_EVIDENCE" }); assert.equal(t.selections.at(-1), null);
  t.render({ ...state, temporalSweep:{ ...state.temporalSweep, frame:1999 } }); assert.equal(t.selections.at(-1), null);
  t.render({ ...state, visibleLayers:[] }); assert.equal(t.selections.at(-1), null); t.h.dispose();
});

test("adapter rejection, unsupported graphics and constructor failures provide retry without lingering timers", async () => {
  for (const kind of ["adapter", "graphics", "constructor"]) {
    let failed = true; const t = await harness({ acquire:(_count, lib) => kind === "adapter" && failed ? Promise.reject(new Error("fixture")) : Promise.resolve(lib), failConstruction:() => kind === "constructor" && failed });
    if (kind === "graphics") t.webgl(false); t.render(); await settle(); let tree = t.render(); assert.equal(action(tree).props.children, "Retry preview"); assert.equal(t.timers.size, 0); assert.match(statusOf(tree), /unavailable|WebGL2/);
    failed = false; t.webgl(true); action(tree).props.onClick(); t.render(); await settle(); t.map().emit("load"); tree = t.render(); assert.match(statusOf(tree), /Saved map context/); t.h.dispose();
  }
});
