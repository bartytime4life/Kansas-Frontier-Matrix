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
const keys = await import(await moduleUrl("app/map-keys.ts"));

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

test("fire detections keep their selectable ids, and the record says what the marker is and is not", () => {
  const source = context.OFFICIAL_CONTEXT_BY_ID["nasa-gibs-fire-points"];
  assert.deepEqual([...source.interactiveLayerIds], ["external-nasa-gibs-fire-points-halo", "external-nasa-gibs-fire-points-circle"]);
  assert.ok(source.interactiveLayerIds.every(id => source.layerIds.includes(id)));
  assert.deepEqual([...source.layerIds].sort(), Object.values(fire.FIRE_POINT_LAYER_IDS).sort());
  assert.ok(!source.layerIds.some(id => id.endsWith("-fill")), "not counted as a composed fill surface");
  assert.ok(fire.FIRE_FOOTPRINT_SOURCE_ID.startsWith("kfm-"), "derived rectangles are never inspected as a separate provider record");
  assert.match(source.boundary, /satellite detection pixel, not a fire perimeter, flame front, or burned area/);
  assert.match(source.boundary, /fixed-size dot at its pixel centre, coloured by the provider's detection confidence; its size does not encode radiative power/);
  assert.match(source.boundary, /not a verified wildfire, ignition point, fire perimeter, burned area/);
  assert.doesNotMatch(source.boundary + context.OFFICIAL_CONTEXT_BY_ID["nifc-fire-reports"].boundary, /animated/i);
});

test("a detection is a confidence-coloured dot with a transparent hit target and its ground pixel, following visibility, opacity and clearing", () => {
  const { map, sources, layers } = mapHarness();
  let images = 0; map.addImage = () => { images++; };
  const data = payload([detection("a", -96.1, 39.3, { confidence: "high" }), detection("b", -96.2, 39.4, { scanKm: undefined })]);
  context.applyOfficialContextState(map, only(["nasa-gibs-fire-points"]), { ...opacity, "nasa-gibs-fire-points": 0.5 }, { "nasa-gibs-fire-points": data });
  assert.equal(sources.get(fire.FIRE_FOOTPRINT_SOURCE_ID).data.features.length, 1);
  for (const id of Object.values(fire.FIRE_POINT_LAYER_IDS)) assert.equal(layers.get(id)?.layout?.visibility ?? "visible", "visible", id);
  const dot = layers.get(fire.FIRE_POINT_LAYER_IDS.circle).paint;
  assert.deepEqual(dot["circle-color"], ["match", ["get", "confidence"], "high", keys.FIRE_CONFIDENCE_COLORS.high, "low", keys.FIRE_CONFIDENCE_COLORS.low, keys.FIRE_CONFIDENCE_COLORS.nominal]);
  assert.equal(dot["circle-opacity"], 0.5);assert.equal(dot["circle-stroke-opacity"], 0.5);
  assert.deepEqual(dot["circle-radius"], fire.FIRE_MARKER_RADIUS);
  const hit = layers.get(fire.FIRE_POINT_LAYER_IDS.halo).paint;
  assert.equal(hit["circle-opacity"], 0);assert.equal(hit["circle-stroke-opacity"], 0);assert.deepEqual(hit["circle-radius"], fire.FIRE_HIT_RADIUS);
  assert.ok(![...layers.values()].some(layer => /fire/.test(String(layer.source)) && layer.type === "symbol"), "no illustrated fire symbols");
  assert.equal(images, 0, "no images are drawn or registered");
  const casing = layers.get(fire.FIRE_POINT_LAYER_IDS.shimmer).paint;
  const edge = layers.get(fire.FIRE_POINT_LAYER_IDS.edge).paint;
  assert.equal(casing["line-color"], "#253e46", "neutral dark casing survives a light basemap");
  assert.equal(edge["line-color"], "#fff1d1", "pale centre survives a dark basemap");
  assert.deepEqual(casing["line-opacity"], edge["line-opacity"]);
  assert.deepEqual(casing["line-dasharray"].map(n => n * casing["line-width"]), edge["line-dasharray"].map(n => n * edge["line-width"]), "both narrow dashed strokes share exact segment lengths");
  context.applyOfficialContextState(map, only([]), opacity, { "nasa-gibs-fire-points": data });
  for (const id of Object.values(fire.FIRE_POINT_LAYER_IDS)) assert.equal(layers.get(id).layout.visibility, "none", id);
  context.clearOfficialContextFeed(map, "nasa-gibs-fire-points");
  assert.equal(sources.get(fire.FIRE_FOOTPRINT_SOURCE_ID).data.features.length, 0);
});

test("the dot keeps one screen size at every zoom; close in, the dashed pixel shows the area a detection covers", async () => {
  const { createPropertyExpression, latest } = await import("@maplibre/maplibre-gl-style-spec");
  const radius = createPropertyExpression(fire.FIRE_MARKER_RADIUS, "paint", latest.paint_circle["circle-radius"]);
  assert.equal(radius.result, "success");
  const at = zoom => radius.value.evaluate({ zoom });
  assert.equal(at(4), 3.5);assert.equal(at(12), 5.5);assert.equal(at(18), 5.5, "a marker, never grown into a burning area");
  const { map, layers } = mapHarness();
  context.applyOfficialContextState(map, only(["nasa-gibs-fire-points"]), opacity, { "nasa-gibs-fire-points": payload([detection("pixel", -98, 38)]) });
  const edge = createPropertyExpression(layers.get(fire.FIRE_POINT_LAYER_IDS.edge).paint["line-opacity"], "paint", latest.paint_line["line-opacity"]);
  assert.equal(edge.value.evaluate({ zoom: 10 }), 0);assert.ok(edge.value.evaluate({ zoom: 13 }) > 0);
});

test("a reported incident is a ring coloured by incident type, never a detection dot, and keeps its source hit identity", () => {
  const { map, layers } = mapHarness();
  const report = context.OFFICIAL_CONTEXT_BY_ID["nifc-fire-reports"];
  assert.deepEqual([...report.interactiveLayerIds], ["external-nifc-fire-reports-halo", "external-nifc-fire-reports-point"]);
  const reports = { ...payload([detection("incident-1", -98, 38, { incidentType: "Prescribed fire" })]), feed: "nifc-fire-reports" };
  const visibility = { ...only([]), "nifc-fire-reports": true };
  context.applyOfficialContextState(map, visibility, { ...opacity, "nifc-fire-reports": 0.6 }, { "nifc-fire-reports": reports });
  const ring = layers.get(report.layerIds[1]).paint;
  assert.equal(ring["circle-color"], "#11161b", "a dark centre: a ring, not a filled dot");
  assert.deepEqual(ring["circle-stroke-color"], ["match", ["get", "incidentType"], ...keys.FIRE_REPORT_COLORS.flat(), keys.FIRE_REPORT_OTHER_COLOR]);
  assert.equal(ring["circle-stroke-width"], 2.5);assert.equal(ring["circle-stroke-opacity"], 0.6);
  const hit = layers.get(report.layerIds[0]).paint;
  assert.equal(hit["circle-opacity"], 0);assert.equal(hit["circle-stroke-opacity"], 0);
  const flat = structuredClone(ring["circle-radius"]);
  map.getProjection = () => ({ type: "globe" });
  context.applyOfficialContextState(map, visibility, opacity, { "nifc-fire-reports": reports });
  assert.notDeepEqual(layers.get(report.layerIds[1]).paint["circle-radius"], flat, "rings follow globe overview sizing");
  context.applyOfficialContextState(map, only([]), opacity, { "nifc-fire-reports": reports });
  for (const id of report.layerIds) assert.equal(layers.get(id).layout.visibility, "none");
});

test("MapLibre selection filter preserves ordinary points and never covers either fire marker", async () => {
  const runtime = await import(await moduleUrl("app/map-runtime.ts"));
  const {featureFilter} = await import("@maplibre/maplibre-gl-style-spec");
  const compiled = featureFilter(runtime.SELECTION_POINT_FILTER, "layers[0].filter");
  const point = displaySourceId => ({ type: 1, properties: displaySourceId ? {displaySourceId} : {}, geometry: [] });
  for (const id of ["nasa-gibs-fire-points", "nifc-fire-reports"]) assert.equal(compiled.filter({zoom:8}, point(id)), false);
  for (const id of [undefined, "usgs-streamflow", "census-counties"]) assert.equal(compiled.filter({zoom:8}, point(id)), true);
  assert.equal(compiled.filter({zoom:8}, {type:3,properties:{},geometry:[]}), false);
});


test("nothing about the fire display is animated", async () => {
  const source = await readFile("app/fire-detection-style.ts", "utf8");
  assert.doesNotMatch(source, /requestAnimationFrame|setTimeout|addImage|Canvas|icon-image/);
  assert.equal(fire.setFireDetectionMotion, undefined);
  assert.doesNotMatch(await readFile("app/page.tsx", "utf8"), /setFireDetectionMotion/);
});

test('a cleared or replacing style has no missing-layer visibility writes', () => {
  const {map,layers}=mapHarness();
  assert.doesNotThrow(()=>fire.syncFireReportDisplay(map,false,0));
  assert.doesNotThrow(()=>fire.syncFireDetectionDisplay(map,false,0));
  assert.equal(layers.size,0);
});
