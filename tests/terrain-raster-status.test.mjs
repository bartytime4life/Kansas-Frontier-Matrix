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
  tracker.reset(id); // hide then re-enable or explicit retry
  assert.equal(tracker.status(id, closeEast, 11, true), "loading", "reselecting or retrying cannot inherit old success or failure");
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
