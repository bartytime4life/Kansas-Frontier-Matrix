import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import ts from "typescript";

const modules = new Map();
async function moduleUrl(file) {
  file = path.resolve(file);
  if (modules.has(file)) return modules.get(file);
  let js = ts.transpileModule(await readFile(file, "utf8"), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
  for (const match of [...js.matchAll(/from ["'](\.[^"']+)["']/g)]) js = js.replace(match[0], `from ${JSON.stringify(await moduleUrl(path.resolve(path.dirname(file), match[1]) + ".ts"))}`);
  js = js.replace(/from ["']([^.'"][^'"]*)["']/g, (_match, name) => `from ${JSON.stringify(import.meta.resolve(name))}`);
  const url = `data:text/javascript;base64,${Buffer.from(js).toString("base64")}`;
  modules.set(file, url); return url;
}
const context = await import(await moduleUrl("app/live-context.ts"));
const fire = await import(await moduleUrl("app/fire-detection-style.ts"));

function mapHarness() {
  const sources = new Map(), layers = new Map();
  const map = {
    getSource: id => sources.get(id), getLayer: id => layers.get(id), getStyle: () => ({ layers: [...layers.values()] }),
    moveLayer(id) { const layer = layers.get(id); layers.delete(id); layers.set(id, layer); },
    getProjection: () => ({ type: "mercator" }),
    // Existing registered images exercise the successful display path without
    // requiring browser Canvas in the ordinary Node suite.
    hasImage: () => true, addImage() {},
    addSource(id, spec) { sources.set(id, { ...spec, setData(data) { this.data = data; } }); },
    addLayer(layer) { layers.set(layer.id, structuredClone(layer)); },
    getLayoutProperty: (id, key) => layers.get(id)?.layout?.[key], getPaintProperty: (id, key) => layers.get(id)?.paint?.[key],
    setLayoutProperty(id, key, value) { const layer = layers.get(id); layer.layout = { ...layer.layout, [key]: value }; },
    setPaintProperty(id, key, value) { const layer = layers.get(id); layer.paint = { ...layer.paint, [key]: value }; },
  };
  return { map, sources, layers };
}
const only = ids => Object.fromEntries(context.OFFICIAL_CONTEXT_SOURCES.map(s => [s.id, ids.includes(s.id)]));
const opacity = Object.fromEntries(context.OFFICIAL_CONTEXT_SOURCES.map(s => [s.id, s.defaultOpacity]));
const detection = (id, longitude, latitude, properties = {}) => ({ type: "Feature", id, geometry: { type: "Point", coordinates: [longitude, latitude] },
  properties: { featureId: id, confidence: "nominal", scanKm: 0.5, trackKm: 0.4, dayNight: "Day", ...properties } });
const payload = features => ({ feed: "nasa-gibs-fire-points", state: "ready", retrievedAt: "2026-04-05T20:00:00Z", featureCount: features.length, data: { type: "FeatureCollection", features } });
const metres = ([lon1, lat1], [lon2, lat2]) => Math.hypot((lon2 - lon1) * 111_320 * Math.cos(lat1 * Math.PI / 180), (lat2 - lat1) * 110_574);

test("a footprint is the provider scan × track pixel on the ground, around the pixel centre", () => {
  const polygon = fire.fireFootprintPolygon(-96.13, 39.37, 0.63, 0.72, -14);
  const ring = polygon.coordinates[0];
  assert.equal(ring.length, 5);
  assert.deepEqual(ring[0], ring[4]);
  assert.ok(Math.abs(metres(ring[0], ring[1]) - 630) < 3, "scan side");
  assert.ok(Math.abs(metres(ring[1], ring[2]) - 720) < 3, "track side");
  const centre = ring.slice(0, 4).reduce(([x, y], [lon, lat]) => [x + lon / 4, y + lat / 4], [0, 0]);
  assert.ok(Math.abs(centre[0] + 96.13) < 1e-5 && Math.abs(centre[1] - 39.37) < 1e-5);
});

test("footprint orientation follows the approximate NOAA-20 pass and stays north-aligned when unknown", () => {
  const day = fire.noaa20TrackAzimuth(38.5, "Day"), night = fire.noaa20TrackAzimuth(38.5, "Night");
  assert.ok(day < -10 && day > -18, `ascending day pass tilts west of north (${day})`);
  assert.ok(night > 10 && night < 18, `descending night pass tilts east of north (${night})`);
  assert.equal(fire.noaa20TrackAzimuth(38.5, undefined), 0);
  assert.equal(fire.noaa20TrackAzimuth(38.5, "Not supplied"), 0);
});

test("only detections with provider pixel dimensions get a footprint, and derivation is cached", () => {
  const points = { type: "FeatureCollection", features: [
    detection("a", -96.1, 39.3, { confidence: "high" }),
    detection("b", -96.2, 39.4, { scanKm: null }),
    detection("c", -96.3, 39.5, { trackKm: "0.4" }),
    detection("d", -96.4, 39.6, { confidence: "surprising" }),
  ] };
  const derived = fire.deriveFireFootprints(points);
  assert.deepEqual(derived.collection.features.map(f => f.properties.featureId), ["a", "d"]);
  assert.deepEqual(derived.collection.features.map(f => f.properties.confidence), ["high", "nominal"]);
  assert.ok(derived.collection.features.every(f => f.properties.display === "satellite-detection-pixel"));
  assert.deepEqual(derived.bounds, [-96.4, 39.3, -96.1, 39.6]);
  assert.equal(fire.deriveFireFootprints(points), derived);
  assert.equal(fire.deriveFireFootprints(undefined).collection.features.length, 0);
});

test("fire detections keep their selectable ids including the flame hit target without admitting its animation as evidence", () => {
  const source = context.OFFICIAL_CONTEXT_BY_ID["nasa-gibs-fire-points"];
  assert.deepEqual([...source.interactiveLayerIds], ["external-nasa-gibs-fire-points-halo", "external-nasa-gibs-fire-points-circle", "external-nasa-gibs-fire-points-flame"]);
  assert.ok(source.interactiveLayerIds.every(id => source.layerIds.includes(id)));
  assert.ok(Object.values(fire.FIRE_POINT_LAYER_IDS).every(id => source.layerIds.includes(id)));
  assert.ok(!source.layerIds.some(id => id.endsWith("-fill")), "not counted as a composed fill surface");
  assert.ok(fire.FIRE_FOOTPRINT_SOURCE_ID.startsWith("kfm-"), "derived rectangles are never inspected as a separate provider record");
  assert.match(source.boundary, /satellite detection pixel, not a fire perimeter, flame front, or burned area/);
  assert.match(source.boundary, /illustration, not measured fire behaviour or intensity/);
  assert.match(source.boundary, /not a verified wildfire, ignition point, fire perimeter, burned area/);
});

test("applying the fire source derives footprints, hides the old dot and follows visibility, opacity and clearing", () => {
  const { map, sources, layers } = mapHarness();
  const data = payload([detection("a", -96.1, 39.3, { confidence: "high" }), detection("b", -96.2, 39.4, { scanKm: undefined })]);
  context.applyOfficialContextState(map, only(["nasa-gibs-fire-points"]), opacity, { "nasa-gibs-fire-points": data });
  const footprints = sources.get(fire.FIRE_FOOTPRINT_SOURCE_ID);
  assert.equal(footprints.data.features.length, 1);
  for (const id of Object.values(fire.FIRE_POINT_LAYER_IDS)) assert.equal(layers.get(id)?.layout?.visibility ?? "visible", "visible", id);
  const circle = layers.get("external-nasa-gibs-fire-points-circle");
  assert.equal(circle.paint["circle-opacity"], 0);
  assert.equal(circle.paint["circle-stroke-opacity"], 0);
  assert.equal(layers.get(fire.FIRE_POINT_LAYER_IDS.flame).type, "symbol");
  assert.equal(layers.get(fire.FIRE_POINT_LAYER_IDS.flame).source, "external-nasa-gibs-fire-points");
  assert.equal(layers.get(fire.FIRE_POINT_LAYER_IDS.heat).source, fire.FIRE_FOOTPRINT_SOURCE_ID);
  assert.equal(layers.get(fire.FIRE_POINT_LAYER_IDS.heat).paint["fill-pattern"], undefined);
  assert.equal(layers.get(fire.FIRE_POINT_LAYER_IDS.heat).paint["fill-opacity"], 0);
  assert.equal(layers.get(fire.FIRE_POINT_LAYER_IDS.shimmer).paint["line-opacity"], 0);
  assert.deepEqual(layers.get(fire.FIRE_POINT_LAYER_IDS.edge).paint["line-dasharray"], [3, 4]);
  // The user's opacity scales every zoom stop.
  context.applyOfficialContextState(map, only(["nasa-gibs-fire-points"]), { ...opacity, "nasa-gibs-fire-points": 0.5 }, { "nasa-gibs-fire-points": data });
  assert.equal(layers.get(fire.FIRE_POINT_LAYER_IDS.flame).paint["icon-opacity"], 0.5);
  assert.equal(layers.get(fire.FIRE_POINT_LAYER_IDS.halo).paint["circle-opacity"][4], 0.15);
  context.applyOfficialContextState(map, only([]), opacity, { "nasa-gibs-fire-points": data });
  for (const id of Object.values(fire.FIRE_POINT_LAYER_IDS)) assert.equal(layers.get(id).layout.visibility, "none", id);
  context.clearOfficialContextFeed(map, "nasa-gibs-fire-points");
  assert.equal(sources.get(fire.FIRE_FOOTPRINT_SOURCE_ID).data.features.length, 0);
});

test("close zoom retains a bounded flame for detections with and without pixel dimensions", async () => {
  const { createPropertyExpression, latest } = await import("@maplibre/maplibre-gl-style-spec");
  const { map, layers } = mapHarness();
  context.applyOfficialContextState(map, only(["nasa-gibs-fire-points"]), opacity,
    { "nasa-gibs-fire-points": payload([detection("pixel", -98, 38), detection("no-pixel", -98.1, 38, {scanKm:null})]) });
  const flame = layers.get(fire.FIRE_POINT_LAYER_IDS.flame);
  assert.equal(flame.maxzoom, undefined, "close zoom never removes the flame layer");
  assert.equal(flame.paint["icon-opacity"], 1, "a known footprint no longer fades its flame out");
  const compiled = createPropertyExpression(flame.layout["icon-size"], "layout", latest.layout_symbol["icon-size"]);
  assert.equal(compiled.result, "success");
  const size = zoom => compiled.value.evaluate({zoom}, {type:1,properties:{scanKm:0.5,trackKm:0.4}});
  assert.ok(size(14) > size(10), "a close view reveals more flame detail");
  assert.equal(size(17), size(22), "the graphic stops growing at its screen-size cap");
  assert.ok(size(22) <= 2.1);
  assert.equal(flame.layout["icon-pitch-alignment"], "viewport", "tilting never flattens it into a ground rectangle");
});


test("incident flames replace report dots and retain source hit identity through opacity and visibility changes", () => {
  const { map, layers } = mapHarness();
  const report = context.OFFICIAL_CONTEXT_BY_ID["nifc-fire-reports"];
  const reports = { ...payload([detection("incident-1", -98, 38, {incidentType:"Prescribed fire"})]), feed:"nifc-fire-reports" };
  const visibility = { ...only([]), "nifc-fire-reports": true };
  context.applyOfficialContextState(map, visibility, { ...opacity, "nifc-fire-reports": 0.6 }, { "nifc-fire-reports": reports });
  for (const id of report.interactiveLayerIds.slice(0, 2)) {
    assert.equal(layers.get(id).paint["circle-opacity"], 0);
    assert.equal(layers.get(id).paint["circle-stroke-opacity"], 0);
  }
  const flame = layers.get(fire.FIRE_REPORT_FLAME_ID);
  assert.equal(flame.source, report.sourceId);
  assert.equal(flame.paint["icon-opacity"], 0.6);
  assert.ok(report.interactiveLayerIds.includes(flame.id));
  assert.equal(flame.maxzoom, undefined, "reported locations do not vanish at footprint zoom");
  const flatSize = structuredClone(flame.layout["icon-size"]);
  map.getProjection = () => ({ type: "globe" });
  context.applyOfficialContextState(map, visibility, opacity, { "nifc-fire-reports": reports });
  assert.notDeepEqual(layers.get(flame.id).layout["icon-size"], flatSize, "report icons follow globe overview sizing");
  context.applyOfficialContextState(map, only([]), opacity, { "nifc-fire-reports": reports });
  assert.equal(layers.get(flame.id).layout.visibility, "none");
  context.applyOfficialContextState(map, visibility, opacity, { "nifc-fire-reports": reports });
  assert.equal(layers.get(report.layerIds[1]).paint["circle-stroke-opacity"], 0, "generic opacity cannot restore a dot");
});


test("MapLibre selection filter preserves ordinary points and never covers either kind of flame", async () => {
  const runtime = await import(await moduleUrl("app/map-runtime.ts"));
  const {featureFilter} = await import("@maplibre/maplibre-gl-style-spec");
  const compiled = featureFilter(runtime.SELECTION_POINT_FILTER, "layers[0].filter");
  const point = displaySourceId => ({ type: 1, properties: displaySourceId ? {displaySourceId} : {}, geometry: [] });
  for (const id of ["nasa-gibs-fire-points", "nifc-fire-reports"]) assert.equal(compiled.filter({zoom:8}, point(id)), false);
  for (const id of [undefined, "usgs-streamflow", "census-counties"]) assert.equal(compiled.filter({zoom:8}, point(id)), true);
  assert.equal(compiled.filter({zoom:8}, {type:3,properties:{},geometry:[]}), false);
});


test("both fire displays share one ticker and reduced motion or a hidden tab settles them without losing selection layers", t => {
  const original = Object.fromEntries(["window", "document", "setTimeout", "clearTimeout"].map(key => [key, Object.getOwnPropertyDescriptor(globalThis, key)]));
  const timers = new Map(), listeners = new Map(), mediaListeners = new Map();
  const media = { matches: false, addEventListener: (name, fn) => mediaListeners.set(name, fn) };
  const document = { hidden: false, addEventListener: (name, fn) => listeners.set(name, fn) };
  let sequence = 0;
  Object.assign(globalThis, { document, window: { matchMedia: () => media, location: { search: "" } },
    setTimeout(fn) { const id = ++sequence; timers.set(id, fn); return id; },
    clearTimeout(id) { timers.delete(id); } });
  const { map, layers } = mapHarness();
  const removed = [];
  Object.assign(map, { triggerRepaint() {}, on() {}, off() {}, once(name, fn) { if (name === "remove") removed.push(fn); } });
  t.after(() => {
    for (const fn of removed) fn();
    fire.setFireDetectionMotion(false);
    for (const [key, descriptor] of Object.entries(original)) {
      if (descriptor) Object.defineProperty(globalThis, key, descriptor); else delete globalThis[key];
    }
  });
  const reports = { ...payload([detection("report", -98, 38, { incidentType: "Wildfire", scanKm: undefined, trackKm: undefined })]), feed: "nifc-fire-reports" };
  const data = { "nasa-gibs-fire-points": payload([detection("pixel", -98, 38)]), "nifc-fire-reports": reports };
  const apply = ids => context.applyOfficialContextState(map, only(ids), opacity, data);
  fire.setFireDetectionMotion(true);
  apply(["nasa-gibs-fire-points", "nifc-fire-reports"]);
  assert.equal(timers.size, 1, "two sources must not create competing repaint loops");
  media.matches = true; mediaListeners.get("change")();
  assert.equal(timers.size, 0, "system reduced motion overrides an enabled ambient preference");
  assert.equal(fire.fireMotionAllowed(), false);
  for (const id of [fire.FIRE_POINT_LAYER_IDS.flame, fire.FIRE_REPORT_FLAME_ID]) assert.equal(layers.get(id).layout.visibility ?? "visible", "visible", "reduced motion preserves still selectable symbols");
  media.matches = false; mediaListeners.get("change")(); assert.equal(timers.size, 1);
  document.hidden = true; listeners.get("visibilitychange")(); assert.equal(timers.size, 0);
  document.hidden = false; listeners.get("visibilitychange")(); assert.equal(timers.size, 1);
  map.hasImage = () => false;
  apply(["nasa-gibs-fire-points", "nifc-fire-reports"]);
  assert.equal(timers.size, 0, "unavailable flame images never keep a repaint timer alive");
  map.hasImage = () => true;
  apply(["nasa-gibs-fire-points", "nifc-fire-reports"]);
  assert.equal(timers.size, 1, "successful registration can resume the shared ticker");
  apply(["nifc-fire-reports"]); assert.equal(timers.size, 1, "hiding detections must not stop report motion");
  apply([]); assert.equal(timers.size, 0);
});


// Fresh renderer instances keep Canvas failures independent of successful caches.
async function freshFire(label) { return import((await moduleUrl('app/fire-detection-style.ts')) + '#' + label); }
function canvasStub(t, { offscreen = 'ok', readback = true, dom = true } = {}) {
  const keys = ['OffscreenCanvas', 'document'];
  const original = keys.map(key => Object.getOwnPropertyDescriptor(globalThis, key));
  const gradient = { addColorStop() {} };
  const ctx = new Proxy({
    getImageData: () => { if (!readback) throw new Error('readback unavailable'); return { data:new Uint8ClampedArray(144*192*4) }; },
    createRadialGradient: () => gradient, createLinearGradient: () => gradient,
  }, { get: (target,key) => target[key] ?? (() => {}) });
  globalThis.OffscreenCanvas = class { getContext() { if(offscreen==='throw') throw new Error('unsupported'); return offscreen==='null' ? null : ctx; } };
  globalThis.document = { createElement: () => ({ getContext: () => dom ? ctx : null }) };
  t.after(() => keys.forEach((key,i) => original[i] ? Object.defineProperty(globalThis,key,original[i]) : delete globalThis[key]));
}
function unregistered(map) {
  const images = new Set();
  map.hasImage = id => images.has(id);
  map.addImage = id => images.add(id);
  return images;
}
function assertFallback(layers, amount) {
  for (const id of [fire.FIRE_POINT_LAYER_IDS.circle, 'external-nifc-fire-reports-point']) {
    assert.equal(layers.get(id).paint['circle-opacity'], amount, id);
    assert.equal(layers.get(id).paint['circle-stroke-opacity'], amount, id);
    assert.deepEqual(layers.get(id).paint['circle-translate'], [0,0], 'fallback stays at the provider point');
  }
  for (const id of [fire.FIRE_POINT_LAYER_IDS.flame, fire.FIRE_REPORT_FLAME_ID]) {
    if(layers.has(id)) {
      assert.equal(layers.get(id).paint['icon-opacity'], 0);
      assert.equal(layers.get(id).layout.visibility, 'none');
    }
  }
}
function bothDisplays(map) {
  const reports = {...payload([detection('report', -98.1,38,{incidentType:'Incident complex'})]),feed:'nifc-fire-reports'};
  const data = {'nasa-gibs-fire-points':payload([detection('pixel',-98,38)]),'nifc-fire-reports':reports};
  const ids=['nasa-gibs-fire-points','nifc-fire-reports'];
  const apply=amount=>context.applyOfficialContextState(map,only(ids),{...opacity,...Object.fromEntries(ids.map(id=>[id,amount]))},data);
  return {apply,data};
}

test('missing Canvas keeps original incident and confidence markers visible and centred', t => {
  canvasStub(t, {offscreen:'null',dom:false});
  const {map,layers}=mapHarness(); unregistered(map);
  const {apply,data}=bothDisplays(map);
  apply(0.6); assertFallback(layers,0.6);
  assert.equal(layers.get(fire.FIRE_POINT_LAYER_IDS.circle).paint['circle-radius'].at(-1),8,'fallback size is capped, never satellite-pixel-sized');
  assert.deepEqual(layers.get('external-nifc-fire-reports-point').paint['circle-color'].slice(2,6),['Prescribed fire','#ffcb6a','Incident complex','#b9a4ff']);
  apply(0); assertFallback(layers,0);
  context.applyOfficialContextState(map,only([]),opacity,data);
  for(const id of [fire.FIRE_POINT_LAYER_IDS.circle,'external-nifc-fire-reports-point']) assert.equal(layers.get(id).layout.visibility,'none');
});

test('offscreen failure falls back to ordinary Canvas and registration recovers after partial failure and style reload', async t => {
  canvasStub(t,{offscreen:'throw'});
  const renderer=await freshFire('registration-recovery');
  const {map,layers}=mapHarness();
  const {apply}=bothDisplays(map); apply(1);
  const images=unregistered(map);
  let reject=true;
  map.addImage=id=>{if(reject && id.endsWith('nominal')) throw new Error('atlas unavailable'); images.add(id);};
  renderer.syncFireDetectionDisplay(map,true,0.5); renderer.syncFireReportDisplay(map,true,0.5);
  assertFallback(layers,0.5);
  assert.equal(images.size,1,'one registered palette never hides all provider markers');
  reject=false;
  renderer.syncFireDetectionDisplay(map,true,0.5); renderer.syncFireReportDisplay(map,true,0.5);
  assert.equal(images.size,3);
  for(const id of [fire.FIRE_POINT_LAYER_IDS.flame,fire.FIRE_REPORT_FLAME_ID]) assert.equal(layers.get(id).paint['icon-opacity'],0.5);
  images.clear();
  renderer.syncFireDetectionDisplay(map,true,1);
  assert.equal(images.size,3,'a new style gets its images back');
});

test('Canvas readback denial and silent registration failure retain markers without throwing', async t => {
  canvasStub(t,{readback:false});
  const renderer=await freshFire('denied-readback');
  const {map,layers}=mapHarness(); const {apply}=bothDisplays(map); apply(1); unregistered(map);
  renderer.syncFireDetectionDisplay(map,true,0.7); renderer.syncFireReportDisplay(map,true,0.7);
  assertFallback(layers,0.7);
  // An implementation exposing addImage but not registering must also fail closed.
  canvasStub(t);
  const silent=await freshFire('silent-registration'); map.addImage=()=>{};
  silent.syncFireDetectionDisplay(map,true,0.4); silent.syncFireReportDisplay(map,true,0.4);
  assertFallback(layers,0.4);
  delete map.addImage;
  silent.syncFireDetectionDisplay(map,true,0.3); silent.syncFireReportDisplay(map,true,0.3);
  assertFallback(layers,0.3);
});
