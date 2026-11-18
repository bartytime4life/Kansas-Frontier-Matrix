import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const source = await readFile("app/basemap-raster-health.ts", "utf8");
const js = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const { BasemapRasterHealth, rasterTileInView, rasterSourceMaxzooms, BASEMAP_TILE_GAP_MESSAGE } = await import(`data:text/javascript;base64,${Buffer.from(js).toString("base64")}`);

// Tile 7/28/48 covers about -101.25..-98.44 E, 37.72..39.91 N, inside Kansas.
const kansasTile = { z: 7, x: 28, y: 48 };
const kansasView = { west: -102, east: -94.6, south: 37, north: 40 };
const coloradoView = { west: -109, east: -102.1, south: 37, north: 41 };

test("a tile is in view only near the drawn zoom and inside the settled bounds", () => {
  assert.equal(rasterTileInView(kansasTile, kansasView, 6.2), true, "256 px tile one level above the map zoom");
  assert.equal(rasterTileInView(kansasTile, kansasView, 7.4), true, "512 px tile at the map zoom");
  assert.equal(rasterTileInView(kansasTile, kansasView, 9.6), true, "coarser horizon tile in a pitched view");
  assert.equal(rasterTileInView(kansasTile, kansasView, 11), false, "four levels below the drawn zoom");
  assert.equal(rasterTileInView(kansasTile, kansasView, 4), false, "three levels above the map zoom");
  assert.equal(rasterTileInView(kansasTile, coloradoView, 7), false, "outside the settled bounds");
});

test("overzoom past the source maxzoom still counts the maxzoom tile as drawn", () => {
  const deepTile = { z: 18, x: 59170, y: 100400 };
  const view = { west: -98.75, east: -98.73, south: 38.0, north: 39.9 };
  assert.equal(rasterTileInView(deepTile, view, 22.5, 18), true, "a 1 ft aerial at maxzoom 18 is drawn at map zoom 22.5");
  assert.equal(rasterTileInView(deepTile, view, 22.5, 22), false, "with maxzoom 22 the map would draw finer tiles instead");
});

test("world copies past ±180° are matched, and malformed input is treated as in view", () => {
  const dateline = { z: 2, x: 0, y: 1 }; // -180..-90 E
  assert.equal(rasterTileInView(dateline, { west: 170, east: 200, south: -10, north: 60 }, 2), true, "east world copy");
  assert.equal(rasterTileInView(dateline, { west: 0, east: 80, south: -10, north: 60 }, 2), false);
  assert.equal(rasterTileInView(kansasTile, { ...kansasView, west: Number.NaN }, 7), true);
  assert.equal(rasterTileInView({ z: 7, x: 999, y: 48 }, kansasView, 7), true, "an impossible tile cannot be retired");
});

test("a failure retires when its tile reloads or leaves the settled view, never while drawn", () => {
  const health = new BasemapRasterHealth();
  const sources = new Map([["esri-imagery", 19]]);
  assert.equal(health.hasFailureInView(sources, kansasView, 7), false);
  health.markFailed("esri-imagery", kansasTile);
  assert.equal(health.hasFailureInView(sources, kansasView, 7), true, "a real gap in view still warns");
  assert.equal(health.hasFailureInView(sources, coloradoView, 7), false, "settled elsewhere, the old failure is not drawn");
  assert.equal(health.hasFailureInView(sources, kansasView, 7), true, "revisiting keeps the gap until the tile loads");
  health.markLoaded("esri-imagery", kansasTile);
  assert.equal(health.hasFailureInView(sources, kansasView, 7), false);
});

test("source-level failures persist for that basemap; other basemaps never inherit them", () => {
  const health = new BasemapRasterHealth();
  health.markFailed("esri-imagery");
  assert.equal(health.hasFailureInView(new Map([["esri-imagery", 19]]), coloradoView, 3), true);
  assert.equal(health.hasFailureInView(new Map([["kansas-ng911-2024", 18]]), kansasView, 7), false);
  health.markFailed("kansas-ng911-2024", kansasTile);
  assert.equal(health.hasFailureInView(new Map(), kansasView, 7), false, "a vector basemap has no raster sources");
  health.reset();
  assert.equal(health.hasFailureInView(new Map([["esri-imagery", 19]]), kansasView, 7), false);
});

test("the tracker keeps only recent failures and the style helper lists raster sources", () => {
  const health = new BasemapRasterHealth();
  for (let x = 0; x < 300; x += 1) health.markFailed("esri-imagery", { z: 9, x, y: 0 });
  const world = { west: -180, east: 180, south: -85, north: 85 };
  assert.equal(health.hasFailureInView(new Map([["esri-imagery", 19]]), world, 9), true);
  health.markLoaded("esri-imagery", { z: 9, x: 299, y: 0 });
  assert.deepEqual([...rasterSourceMaxzooms({ sources: { a: { type: "raster", maxzoom: 18 }, b: { type: "vector" }, c: { type: "raster" } } })], [["a", 18], ["c", 22]]);
  assert.equal(rasterSourceMaxzooms("https://example.invalid/style.json").size, 0);
  assert.match(BASEMAP_TILE_GAP_MESSAGE, /Gaps are unknown/);
});
