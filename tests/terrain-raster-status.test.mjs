import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const source = await readFile("app/terrain-raster-status.ts", "utf8");
const js = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const { terrainRasterStatus, terrainRasterNeedsCloserView, terrainRasterErrorTile, TerrainRasterViewTracker } = await import(`data:text/javascript;base64,${Buffer.from(js).toString("base64")}`);

test("3DEP raster state requires a loaded tile and discloses partial coverage", () => {
  assert.equal(terrainRasterStatus(false, false, true), "loading", "a settled source alone is not coverage");
  assert.equal(terrainRasterStatus(false, true, true), "error");
  assert.equal(terrainRasterStatus(true, true, true), "partial");
  assert.equal(terrainRasterStatus(true, false, false), "loading");
  assert.equal(terrainRasterStatus(true, false, true), "ready");
});

test("selected 3DEP rasters explain their minimum zoom even when no tile has loaded", () => {
  assert.equal(terrainRasterNeedsCloserView(true, false, "loading", 6.8), true);
  assert.equal(terrainRasterNeedsCloserView(true, false, "ready", 6.8), true);
  assert.equal(terrainRasterNeedsCloserView(true, false, "error", 6.8), false);
  assert.equal(terrainRasterNeedsCloserView(false, false, "loading", 6.8), false);
  assert.equal(terrainRasterNeedsCloserView(true, false, "loading", 7.1), false);
});

test("MapLibre tile errors resolve either tileID or coord without inventing source-wide failures", () => {
  const tile = { z: 11, x: 475, y: 785 };
  assert.deepEqual(terrainRasterErrorTile({ tile: { tileID: { canonical: tile } } }), tile);
  assert.deepEqual(terrainRasterErrorTile({ coord: { canonical: tile } }), tile);
  assert.equal(terrainRasterErrorTile({}), undefined);
});

test("a successful wide-view tile cannot make a disjoint failed viewport partial", () => {
  const tracker = new TerrainRasterViewTracker();
  const id = "usgs-3dep-hillshade";
  const wideRice = { west: -99, east: -97, south: 38, north: 40 };
  const smallMove = { west: -98.7, east: -97.1, south: 38.1, north: 39.7 };
  const closeEast = { west: -97, east: -95, south: 38, north: 39 };
  tracker.markLoaded(id, { z: 8, x: 58, y: 98 });
  assert.equal(tracker.status(id, wideRice, 8, true), "ready");
  assert.equal(tracker.status(id, smallMove, 8, true), "ready", "a pan within cached tile coverage stays ready");
  assert.equal(tracker.status(id, wideRice, 11, true), "loading", "an old coarse tile is not close-zoom coverage");
  tracker.markFailed(id, { z: 11, x: 475, y: 785 });
  assert.equal(tracker.status(id, wideRice, 8, true), "ready", "a failed close tile does not taint the successful wide view");
  assert.equal(tracker.status(id, closeEast, 11, true), "error", "old success must not count as current partial coverage");
  tracker.markLoaded(id, { z: 11, x: 475, y: 785 });
  assert.equal(tracker.status(id, closeEast, 11, true), "ready", "the successful retry replaces that tile's failure");
  tracker.markFailed(id, { z: 11, x: 476, y: 785 });
  assert.equal(tracker.status(id, closeEast, 11, true), "partial", "a different current-view failure establishes partial coverage");
  tracker.reset(id); // an explicit retry discards the former tile results
  assert.equal(tracker.status(id, closeEast, 11, true), "loading", "retrying cannot inherit old success or failure");
});

test("a failed fine child at the same Rice location cannot taint a returned wide view", () => {
  const tracker = new TerrainRasterViewTracker();
  const id = "usgs-3dep-slope";
  const rice = { west: -99, east: -97, south: 38, north: 40 };
  tracker.markLoaded(id, { z: 8, x: 58, y: 98 });
  assert.equal(tracker.status(id, rice, 8, true), "ready");
  tracker.markFailed(id, { z: 11, x: 464, y: 784 });
  assert.equal(tracker.status(id, rice, 9, true), "error", "pitched z9 views may request z11 raster tiles");
  assert.equal(tracker.status(id, rice, 10, true), "error", "the coarse z8 tile cannot attest the close view");
  assert.equal(tracker.status(id, rice, 8, true), "ready", "the failed z11 child cannot taint the returned z8 view");
});

test("the latest result for one terrain tile replaces its prior result", () => {
  const tracker = new TerrainRasterViewTracker();
  const id = "usgs-3dep-hillshade";
  const rice = { west: -99, east: -97, south: 38, north: 40 };
  const tile = { z: 11, x: 464, y: 784 };
  tracker.markFailed(id, tile);
  assert.equal(tracker.status(id, rice, 9, true), "error");
  tracker.markLoaded(id, tile);
  assert.equal(tracker.status(id, rice, 9, true), "ready", "a successful retry clears the same tile's failure");
  tracker.markFailed(id, tile);
  assert.equal(tracker.status(id, rice, 9, true), "error", "a later failure clears the same tile's old success");
});

test("coverage belongs to the exact renderer source and resets on replacement or style removal", () => {
  const tracker = new TerrainRasterViewTracker(), id = "usgs-3dep-hillshade";
  const bounds = { west: -99, east: -97, south: 38, north: 40 }, sourceA = {}, sourceB = {};
  tracker.bindSource(id, sourceA);
  tracker.markLoaded(id, { z: 11, x: 464, y: 784 });
  tracker.markFailed(id, { z: 11, x: 465, y: 784 });
  tracker.bindSource(id, sourceA);
  assert.equal(tracker.status(id, bounds, 10.5, true), "partial", "visibility cannot erase same-source coverage or failures");
  tracker.bindSource(id, sourceB);
  assert.equal(tracker.status(id, bounds, 10.5, true), "loading", "a replacement source must earn its own coverage");
  tracker.markLoaded(id, { z: 11, x: 464, y: 784 });
  tracker.reset(id);
  tracker.bindSource(id, sourceB);
  assert.equal(tracker.status(id, bounds, 10.5, true), "loading", "explicit retry stays empty even with the same source");
  tracker.markLoaded(id, { z: 11, x: 464, y: 784 });
  tracker.bindSource(id, undefined);
  assert.equal(tracker.status(id, bounds, 10.5, true), "loading");
  tracker.bindSource(id, sourceA);
  tracker.markLoaded(id, { z: 11, x: 464, y: 784 });
  tracker.resetAll();
  tracker.bindSource(id, sourceA);
  assert.equal(tracker.status(id, bounds, 10.5, true), "loading", "style reset cannot resurrect earlier coverage");
});

const pageSource = await readFile(process.env.KFM_TERRAIN_TOGGLE_PAGE ?? "app/page.tsx", "utf8");
const pageAst = ts.createSourceFile("page.tsx", pageSource, ts.ScriptTarget.ES2022, true, ts.ScriptKind.TSX);
let toggleCallback, sourceDataCallback;
function findCallbacks(node) {
  if (ts.isVariableDeclaration(node) && node.name.getText(pageAst) === "setOfficialContextVisible") toggleCallback = node.initializer.arguments[0].getText(pageAst);
  if (ts.isCallExpression(node) && node.expression.getText(pageAst) === "map.on" && node.arguments[0]?.text === "sourcedata" && ts.isArrowFunction(node.arguments[1]) && node.arguments[1].getText(pageAst).includes("terrainRasterViewRef")) sourceDataCallback = node.arguments[1].getText(pageAst);
  ts.forEachChild(node, findCallbacks);
}
findCallbacks(pageAst);
function executeCallback(callback, scope) {
  assert.ok(callback, "execute the actual page callback, not a mirrored implementation");
  const compiled = ts.transpileModule(`return ${callback};`, { compilerOptions: { target: ts.ScriptTarget.ES2022 } }).outputText;
  return new Function(...Object.keys(scope), compiled)(...Object.values(scope));
}
function toggleHarness(id = "usgs-3dep-hillshade") {
  const tracker = new TerrainRasterViewTracker(), source = { id, kind: "OPERATIONAL_WMS", sourceId: `external-${id}` };
  const h = { tracker, source, renderer: {}, settled: true, zoom: 10.5, bounds: { west: -99, east: -97, south: 38, north: 40 }, states: {}, errors: {}, applies: 0 };
  const map = { isStyleLoaded: () => true, getSource: () => h.renderer, isSourceLoaded: () => h.settled, getZoom: () => h.zoom,
    getBounds: () => ({ getWest: () => h.bounds.west, getEast: () => h.bounds.east, getSouth: () => h.bounds.south, getNorth: () => h.bounds.north }) };
  h.scope = { terrainRasterViewRef: { current: tracker }, officialRasterFailuresRef: { current: new Set() }, OFFICIAL_CONTEXT_BY_ID: { [id]: source },
    officialVisibilityRef: { current: { [id]: true } }, setOfficialVisibility: () => {}, officialOpacityRef: { current: { [id]: 0.46 } }, officialPayloadsRef: { current: {} },
    mapRef: { current: map }, temporalQueryRef: { current: { frame: 2026 } }, OFFICIAL_CONTEXT_PRESENT_FRAME: 2026, noaaRadarReadyRef: { current: false }, noaaRadarFrameTimeRef: { current: null },
    setOfficialStates: update => { h.states = update(h.states); }, setOfficialErrors: update => { h.errors = update(h.errors); },
    runtimeOfficialVisibility: visibility => visibility, applyOfficialContextState: () => { h.applies += 1; },
    map, TERRAIN_SOURCE_ID: "display-dem", OFFICIAL_CONTEXT_BY_SOURCE_ID: { [source.sourceId]: source }, rasterRetryTimers: new Map(), LAYER_REGISTRY: [],
    terrainRasterBounds: () => h.bounds };
  tracker.bindSource(id, h.renderer);
  h.toggle = executeCallback(toggleCallback, h.scope);
  h.sourceData = executeCallback(sourceDataCallback, h.scope);
  return h;
}

test("warm hide/show restores coverage immediately without a new tile event or request", () => {
  for (const id of ["usgs-3dep-hillshade", "usgs-3dep-slope"]) {
    const h = toggleHarness(id);
    h.tracker.markLoaded(id, { z: 11, x: 464, y: 784 });
    for (let repeat = 0; repeat < 8; repeat += 1) { h.toggle(id, false); h.toggle(id, true); }
    assert.equal(h.states[id], "ready");
    assert.equal(h.scope.officialVisibilityRef.current[id], true);
    assert.equal(h.scope.officialOpacityRef.current[id], 0.46);
    assert.equal(h.applies, 16, "only existing visibility application runs; no refresh API is supplied");
  }
});

test("warm toggles keep current partial failures and never attest a disjoint, coarse or unsettled view", () => {
  const id = "usgs-3dep-hillshade", h = toggleHarness(id);
  h.tracker.markLoaded(id, { z: 11, x: 464, y: 784 });
  h.tracker.markFailed(id, { z: 11, x: 465, y: 784 });
  h.scope.officialRasterFailuresRef.current.add(id); h.errors[id] = "known partial failure";
  h.toggle(id, false); h.toggle(id, true);
  assert.equal(h.states[id], "partial"); assert.equal(h.errors[id], "known partial failure");
  h.bounds = { west: -96, east: -95, south: 38, north: 40 };
  h.toggle(id, true); assert.equal(h.states[id], "loading", "other locations cannot inherit cached coverage");
  h.bounds = { west: -99, east: -97, south: 38, north: 40 }; h.zoom = 14;
  h.toggle(id, true); assert.equal(h.states[id], "loading", "coarse parents cannot attest a close zoom");
  h.zoom = 10.5; h.tracker.reset(id); h.tracker.markLoaded(id, { z: 11, x: 464, y: 784 }); h.settled = false;
  h.toggle(id, true); assert.equal(h.states[id], "loading", "loaded coverage still requires a settled source");
});

test("a replacement or absent source cannot inherit the previous renderer's tile results", () => {
  const id = "usgs-3dep-hillshade", h = toggleHarness(id);
  h.tracker.markLoaded(id, { z: 11, x: 464, y: 784 });
  h.renderer = {};
  h.toggle(id, true); assert.equal(h.states[id], "loading");
  h.tracker.markLoaded(id, { z: 11, x: 464, y: 784 }); h.renderer = undefined;
  h.toggle(id, true); assert.equal(h.states[id], "loading");
});

test("tile completion while hidden is usable when that same source is shown again", () => {
  const id = "usgs-3dep-hillshade", h = toggleHarness(id);
  h.toggle(id, false);
  h.sourceData({ sourceId: h.source.sourceId, isSourceLoaded: true, tile: { state: "loaded" }, coord: { canonical: { z: 11, x: 464, y: 784 } } });
  h.toggle(id, true);
  assert.equal(h.states[id], "ready", "showing cached tiles need not emit a second completion event");
});
