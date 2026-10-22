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
  assert.match(source.boundary, /illustrative, not measured fire behaviour or intensity/);
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
  assert.equal(layers.get(fire.FIRE_POINT_LAYER_IDS.heat).paint["fill-pattern"], fire.FIRE_EMBER_PATTERN_ID);
  // The user's opacity scales every zoom stop.
  context.applyOfficialContextState(map, only(["nasa-gibs-fire-points"]), { ...opacity, "nasa-gibs-fire-points": 0.5 }, { "nasa-gibs-fire-points": data });
  assert.equal(layers.get(fire.FIRE_POINT_LAYER_IDS.flame).paint["icon-opacity"][4], 0.5);
  assert.equal(layers.get(fire.FIRE_POINT_LAYER_IDS.halo).paint["circle-opacity"][4], 0.15);
  context.applyOfficialContextState(map, only([]), opacity, { "nasa-gibs-fire-points": data });
  for (const id of Object.values(fire.FIRE_POINT_LAYER_IDS)) assert.equal(layers.get(id).layout.visibility, "none", id);
  context.clearOfficialContextFeed(map, "nasa-gibs-fire-points");
  assert.equal(sources.get(fire.FIRE_FOOTPRINT_SOURCE_ID).data.features.length, 0);
});

test("the ember texture tiles seamlessly and loops in time", () => {
  const size = 32;
  const frame = fire.renderEmberFrame(0, size);
  assert.equal(frame.length, size * size * 4);
  const pixel = (x, y) => frame.slice((y * size + x) * 4, (y * size + x) * 4 + 3);
  const step = (a, b) => a.reduce((sum, value, index) => sum + Math.abs(value - b[index]), 0);
  let seam = 0, inner = 0;
  for (let y = 0; y < size; y++) { seam += step(pixel(size - 1, y), pixel(0, y)); inner += step(pixel(1, y), pixel(0, y)); }
  assert.ok(seam < inner * 2.5, "wrapping across the tile edge is no harsher than an ordinary step");
  const loop = fire.renderEmberFrame(fire.FIRE_FRAME_COUNT, size);
  assert.deepEqual([...loop], [...frame]);
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
  apply(["nifc-fire-reports"]); assert.equal(timers.size, 1, "hiding detections must not stop report motion");
  apply([]); assert.equal(timers.size, 0);
});
