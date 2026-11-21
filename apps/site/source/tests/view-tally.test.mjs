import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import ts from "typescript";

// Compile the real modules and their relative imports to data URLs, as the other layer tests do.
const modules = new Map();
async function moduleUrl(file) {
  file = path.resolve(file);
  if (modules.has(file)) return modules.get(file);
  let js = ts.transpileModule(await readFile(file, "utf8"), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
  for (const match of [...js.matchAll(/from ["'](\.[^"']+)["']/g)]) {
    js = js.replace(match[0], `from ${JSON.stringify(await moduleUrl(path.resolve(path.dirname(file), match[1]) + ".ts"))}`);
  }
  const url = `data:text/javascript;base64,${Buffer.from(js).toString("base64")}`;
  modules.set(file, url); return url;
}
const { viewTally, viewTallyBrief, isCountedLayer, COUNTED_LAYER_IDS } = await import(await moduleUrl("app/view-tally.ts"));
const clusters = await import(await moduleUrl("app/context-clusters.ts"));

const point = (x, y, properties = {}) => ({ type: "Feature", geometry: { type: "Point", coordinates: [x, y] }, properties });
const collection = features => ({ type: "FeatureCollection", features });
const square = (x, y, properties) => ({ type: "Feature", properties,
  geometry: { type: "Polygon", coordinates: [[[x - .01, y - .01], [x + .01, y - .01], [x + .01, y + .01], [x - .01, y + .01], [x - .01, y - .01]]] } });
const KANSAS = { west: -102.1, south: 36.9, east: -94.5, north: 40.1 };
const TOPEKA = { west: -96, south: 38.9, east: -95.4, north: 39.2 };

test("only the layers drawn as numbered circles get a view tally", () => {
  for (const id of ["kdot-bridges-state", "kdot-bridges-local", "kdot-bridges-historic", "kdot-bridges-old", "kdot-bridges-closed", "nps-nrhp-places", "nps-trail-places", "kdwp-wiha-access"]) assert.equal(isCountedLayer(id), true, id);
  for (const id of ["kdwp-wildlife-areas", "usgs-earthquakes", "nps-historic-trails", "toString", ""]) assert.equal(isCountedLayer(id), false, id);
  assert.equal(viewTally("usgs-earthquakes", collection([point(-95.7, 39)]), KANSAS), null);
  assert.equal(viewTally("kdot-bridges-state", collection([]), KANSAS), null, "a layer with no located records has nothing to count");
  assert.equal(viewTally("kdot-bridges-state", undefined, KANSAS), null);
  assert.equal(viewTally("kdot-bridges-state", collection([point(-95.7, 39)]), { ...KANSAS, north: NaN }), null);
});

test("bridges in view are counted exactly and described the way a numbered circle is", () => {
  const bridges = collection([
    point(-95.7, 39.05, { built: 1931, lengthFt: 120, statusClass: "posted" }),
    point(-95.6, 39.0, { built: 1978, lengthFt: 1450 }),
    point(-95.5, 39.1, { lengthFt: 60, statusClass: "closed" }),
    point(-100.9, 37.9, { built: 1899, lengthFt: 2100 }),
    { type: "Feature", geometry: null, properties: {} },
  ]);
  const near = viewTally("kdot-bridges-local", bridges, TOPEKA);
  assert.deepEqual([near.count, near.total, near.nearest], [3, 4, null]);
  assert.equal(near.title, "3 of 4 bridges in this view");
  assert.equal(near.detail, "earliest recorded build year 1931 · longest 1,450 ft · 1 recorded closed · 1 posted with a restriction");
  // The same three records as one numbered circle read identically.
  assert.equal(near.detail, clusters.officialClusterSummary("kdot-bridges-local", { cluster: true, point_count: 3, earliest: 1931, longestFt: 1450, closed: 1, posted: 1 }).detail);
  const all = viewTally("kdot-bridges-local", bridges, KANSAS);
  assert.equal(all.title, "All 4 bridges are in this view");
  assert.match(all.detail, /^earliest recorded build year 1899 · longest 2,100 ft/);
});

test("a single record in view is counted without group wording", () => {
  const one = viewTally("kdot-bridges-state", collection([point(-95.7, 39.05, { built: 1931 }), point(-100.9, 37.9)]), TOPEKA);
  assert.deepEqual([one.title, one.detail], ["1 of 2 bridges in this view", ""]);
});

test("an empty view points to the nearest record by distance and direction", () => {
  const places = collection([point(-100.9, 37.9, { resourceType: "building" }), point(-97.3, 37.7, { resourceType: "site" })]);
  const none = viewTally("nps-nrhp-places", places, TOPEKA);
  assert.equal(none.count, 0);
  assert.equal(none.title, "No National Register markers in this view");
  assert.equal(none.detail, "The nearest of 2 is about 125 mi southwest of the middle of the map.");
  assert.deepEqual(none.nearest, [-97.3, 37.7]);
  const close = viewTally("nps-trail-places", collection([point(-95.7, 39.26)]), TOPEKA);
  assert.equal(close.detail, "The nearest of 1 is about 15 mi north of the middle of the map.");
  assert.match(viewTally("nps-trail-places", collection([point(-95.33, 39.05)]), TOPEKA).detail, /about 20 mi east of/);
  assert.match(viewTally("nps-trail-places", collection([point(-95.7, 38.85)]), TOPEKA).detail, /about 15 mi south of/);
  // Under ten miles the distance is given to the mile; beyond that, to the nearest five.
  assert.match(viewTally("nps-trail-places", collection([point(-95.7, 39.09)]), { west: -95.72, south: 39.04, east: -95.68, north: 39.06 }).detail, /about 3 mi north of/);
});

test("National Register markers and trail sites keep their circles' facts", () => {
  const places = collection([point(-95.7, 39, { resourceType: "building", landmark: true }), point(-95.6, 39.1, { resourceType: "building" }), point(-95.5, 39.0, { resourceType: "district" })]);
  assert.equal(viewTally("nps-nrhp-places", places, TOPEKA).detail, "1 National Historic Landmark · 2 buildings · 1 district");
  const sites = collection([point(-95.7, 39, { trails: "Santa Fe, Oregon, California", certified: "NPS-certified trail site" }), point(-95.6, 39.1, { trails: "Pony Express" })]);
  const tally = viewTally("nps-trail-places", sites, TOPEKA);
  assert.equal(tally.title, "All 2 trail sites are in this view");
  assert.equal(tally.detail, "1 NPS-certified · Santa Fe 1 · Oregon 1 · California 1 · Pony Express 1");
});

test("hunting tracts count where the middle of the outline falls, with acres and archery-only totals", () => {
  const tracts = collection([square(-95.7, 39, { featureId: "a", acres: 320, archeryOnly: "Archery only" }), square(-95.6, 39.1, { featureId: "b", acres: 160.4 }), square(-100.9, 37.9, { featureId: "c", acres: 640 })]);
  const tally = viewTally("kdwp-wiha-access", tracts, TOPEKA);
  assert.equal(tally.title, "2 of 3 walk-in hunting tracts in this view");
  assert.equal(tally.detail, "480 recorded acres · 1 archery-only");
  assert.equal(viewTally("kdwp-wiha-access", tracts, { west: -99, south: 38.9, east: -98, north: 39.2 }).title, "No walk-in hunting tracts in this view");
});

test("a view that crosses the date line still tests longitude correctly", () => {
  const tally = viewTally("nps-trail-places", collection([point(179.5, 10), point(-179.5, 10), point(0, 10)]), { west: 170, south: 0, east: -170, north: 20 });
  assert.equal(tally.count, 2);
});

test("the Layers panel shows the tally only for a counted layer that is drawn on the flat map", async () => {
  const page = await readFile("app/page.tsx", "utf8"), line = await readFile("app/view-tally-line.tsx", "utf8"), css = await readFile("app/map-layers.css", "utf8");
  const mount = page.split("\n").find(row => row.includes("<ViewTallyLine"));
  assert.ok(mount, "the tally is mounted in the layer row");
  for (const guard of ["isCountedLayer(source.id)", "effectiveOfficialVisibility[source.id]", 'projection !== "globe"', "styleReady"]) assert.ok(mount.includes(guard), guard);
  assert.ok(page.indexOf("<ViewTallyLine") < page.indexOf('<details className="official-context-options">'), "above the collapsed details, so it shows without opening them");
  // It recounts when the map stops, not on every frame of a move, and is not announced on every pan.
  assert.match(line, /map\.on\("moveend", read\)/); assert.match(line, /map\.off\("moveend", read\)/);
  assert.ok(!/aria-live="(polite|assertive)"|role="(status|alert)"/.test(line));
  assert.match(line, /duration: reducedMotion \? 0 : 600/);
  assert.match(css, /@media \(max-width: 980px\) \{ \.view-tally button \{ min-height: 44px; \} \}/);
});

test("the status bar line names each counted layer briefly and stays short", () => {
  assert.equal(COUNTED_LAYER_IDS.length, 8);
  for (const id of COUNTED_LAYER_IDS) assert.equal(isCountedLayer(id), true, id);
  assert.equal(viewTallyBrief([]), "");
  assert.equal(viewTallyBrief([{ contextId: "usgs-earthquakes", count: 4 }]), "", "other layers are not counted");
  assert.equal(viewTallyBrief([{ contextId: "kdot-bridges-local", count: 265 }]), "In view: 265 local bridges");
  assert.equal(viewTallyBrief([{ contextId: "nps-trail-places", count: 0 }, { contextId: "nps-nrhp-places", count: 1 }]), "In view: no trail sites · 1 Register marker");
  // Three bridge layers are parts of the local list, so the line never adds layers together.
  assert.equal(viewTallyBrief([{ contextId: "kdot-bridges-state", count: 5580 }, { contextId: "kdot-bridges-local", count: 19291 }, { contextId: "kdot-bridges-closed", count: 91 },
    { contextId: "kdwp-wiha-access", count: 3591 }, { contextId: "nps-trail-places", count: 96 }]),
    "In view: 5,580 state highway bridges · 19,291 local bridges · 91 closed local bridges · +2 more layers");
  assert.match(viewTallyBrief(COUNTED_LAYER_IDS.slice(0, 4).map(contextId => ({ contextId, count: 2 }))), / · \+1 more layer$/);
  assert.equal(viewTallyBrief([{ contextId: "nps-trail-places", count: -1 }, { contextId: "nps-trail-places", count: 1.5 }]), "");
});

test("the status bar shows the line on the flat map, after the map's name, and drops it on narrow screens", async () => {
  const page = await readFile("app/page.tsx", "utf8"), line = await readFile("app/view-tally-line.tsx", "utf8"), css = await readFile("app/map-layers.css", "utf8");
  const bar = page.slice(page.indexOf('<footer className="status-bar"'), page.indexOf("</footer>", page.indexOf('<footer className="status-bar"')));
  assert.match(bar, /projection !== "globe" && styleReady && <ViewTallyStatus layers=\{viewTallyLayers\} mapRef=\{mapRef\} \/>\}<\/span>/);
  // It sits inside the first cell, so the bar's cell order and its narrow-screen rules are unchanged.
  assert.equal(bar.match(/<span/g).length, (bar.match(/<span>\{mapRepresentationLabel\}/) ? 3 : 2));
  assert.match(page, /COUNTED_LAYER_IDS\.filter\(id => effectiveOfficialVisibility\[id as OfficialContextFeedId\]\)/);
  assert.match(line, /<output className="status-view-tally" aria-live="off">/);
  assert.match(css, /@media \(max-width: 760px\) \{ \.status-view-tally \{ display: none; \} \}/);
});

test("a view picks out its oldest and longest bridge, and says so only when it is true", () => {
  const bridges = collection([
    point(-95.7, 39.05, { built: 1931, lengthFt: 120 }), point(-95.6, 39.0, { built: 1978, lengthFt: 1450 }),
    point(-95.5, 39.1, { built: 1931, lengthFt: 60 }), point(-95.55, 39.0, { built: 1700, lengthFt: 90 }), point(-100.9, 37.9, { built: 1899, lengthFt: 2100 }),
  ]);
  const tied = viewTally("kdot-bridges-local", bridges, TOPEKA);
  // Two bridges share the earliest believable year, so neither is called "the oldest"; 1700 is outside the range the circles accept.
  assert.deepEqual(tied.highlights, [
    { label: "Show one of 2 from 1931", center: [-95.7, 39.05], zoom: 14.5 },
    { label: "Show the longest (1,450 ft)", center: [-95.6, 39.0], zoom: 14.5 },
  ]);
  const all = viewTally("kdot-bridges-local", bridges, KANSAS);
  assert.deepEqual(all.highlights.map(h => [h.label, h.center]), [["Show the oldest (1899)", [-100.9, 37.9]], ["Show the longest (2,100 ft)", [-100.9, 37.9]]]);
  // Records outside the view are never offered, and one record alone has nothing to pick out.
  assert.ok(tied.highlights.every(h => h.center[0] > TOPEKA.west && h.center[0] < TOPEKA.east));
  assert.deepEqual(viewTally("kdot-bridges-state", collection([point(-95.7, 39.05, { built: 1931, lengthFt: 120 }), point(-100.9, 37.9)]), TOPEKA).highlights, []);
  assert.deepEqual(viewTally("kdot-bridges-state", collection([point(-95.7, 39.05), point(-95.6, 39.0)]), TOPEKA).highlights, [], "no recorded year or length, no button");
});

test("landmarks and the largest hunting tract are offered; trail sites and empty views offer nothing", () => {
  const places = collection([point(-95.7, 39, { resourceType: "building" }), point(-95.6, 39.1, { resourceType: "building", landmark: true }), point(-95.5, 39.0, { resourceType: "district", landmark: true })]);
  assert.deepEqual(viewTally("nps-nrhp-places", places, TOPEKA).highlights, [{ label: "Show one of 2 National Historic Landmarks", center: [-95.6, 39.1], zoom: 13.5 }]);
  const one = collection([point(-95.7, 39, { resourceType: "building" }), point(-95.6, 39.1, { resourceType: "building", landmark: true })]);
  assert.equal(viewTally("nps-nrhp-places", one, TOPEKA).highlights[0].label, "Show the National Historic Landmark");
  assert.deepEqual(viewTally("nps-nrhp-places", collection([point(-95.7, 39), point(-95.6, 39.1)]), TOPEKA).highlights, []);
  const tracts = collection([square(-95.7, 39, { featureId: "a", acres: 320 }), square(-95.6, 39.1, { featureId: "b", acres: 1122.4 }), square(-100.9, 37.9, { featureId: "c", acres: 6400 })]);
  const [largest] = viewTally("kdwp-wiha-access", tracts, TOPEKA).highlights;
  assert.equal(largest.label, "Show the largest tract (1,122 acres)"); assert.equal(largest.zoom, 12);
  assert.ok(Math.abs(largest.center[0] + 95.6) < 1e-9 && Math.abs(largest.center[1] - 39.1) < 1e-9);
  const sites = collection([point(-95.7, 39, { trails: "Santa Fe", certified: "NPS-certified trail site" }), point(-95.6, 39.1, { trails: "Oregon" })]);
  assert.deepEqual(viewTally("nps-trail-places", sites, TOPEKA).highlights, []);
  assert.deepEqual(viewTally("nps-trail-places", sites, { west: -99, south: 38.9, east: -98, north: 39.2 }).highlights, []);
});

test("a highlight button moves to the record without ever zooming out", async () => {
  const line = await readFile("app/view-tally-line.tsx", "utf8");
  assert.match(line, /zoom: Math\.max\(map\.getZoom\(\), highlight\.zoom\)/);
  assert.match(line, /duration: reducedMotion \? 0 : 900/);
  assert.match(line, /tally\.highlights\.length > 0 &&/);
});
