import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const read = path => readFile(new URL(`../${path}`, import.meta.url), "utf8");
const toUrl = source => `data:text/javascript;base64,${Buffer.from(source).toString("base64")}`;
const transpile = source => ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const modelUrl = toUrl(transpile(await read("app/terrain-drawing.ts")));
const model = await import(modelUrl);
const surface = await import(toUrl(transpile((await read("app/terrain-surface.ts")).replace('"./terrain-drawing"', JSON.stringify(modelUrl)))));
const close = (actual, expected, epsilon = 1e-8) => assert.ok(Math.abs(actual - expected) < epsilon, `${actual} ≈ ${expected}`);

function plane(east, north, { size = 5, latitude = 38, elevation = 500 } = {}) {
  const grid = { size, bounds: [-98.002, latitude - 0.001, -97.998, latitude + 0.001], spacingMeters: 150, heights: [] };
  grid.heights = Array.from({ length: size ** 2 }, (_, index) => {
    const [lng, lat] = model.terrainDrawingCoordinate(grid, index);
    return elevation + east * (lng + 98) * 111_320 * Math.cos(latitude * Math.PI / 180) + north * (lat - latitude) * 111_320;
  });
  return grid;
}

test("Horn gradients point downhill clockwise from north on cardinal and diagonal planes", () => {
  for (const [east, north, degrees, compass] of [
    [0, -.1, 0, "N"], [-.1, -.1, 45, "NE"], [-.1, 0, 90, "E"], [-.1, .1, 135, "SE"],
    [0, .1, 180, "S"], [.1, .1, 225, "SW"], [.1, 0, 270, "W"], [.1, -.1, 315, "NW"],
  ]) {
    const cell = surface.terrainSurfaceCell(plane(east, north), 2, 2);
    close(cell.slopeDegrees, Math.atan(Math.hypot(east, north)) * 180 / Math.PI);
    close(cell.aspectDegrees, degrees);
    assert.equal(surface.terrainAspectDirection(cell.aspectDegrees), compass);
    assert.equal(cell.elevationMeters, 500, "probe elevation is the actual central sample");
  }
  close(surface.terrainSurfaceCell(plane(1, 0), 2, 2).slopeDegrees, 45, 1e-8);
});

test("east-west ground spacing adjusts for latitude independently of north-south spacing", () => {
  const atEquator = plane(.1, .04, { latitude: 0 });
  const atSixty = plane(.1, .04, { latitude: 60 });
  atSixty.heights = [...atEquator.heights];
  const equator = surface.terrainSurfaceCell(atEquator, 2, 2), sixty = surface.terrainSurfaceCell(atSixty, 2, 2);
  close(equator.slopeDegrees, Math.atan(Math.hypot(.1, .04)) * 180 / Math.PI);
  close(sixty.slopeDegrees, Math.atan(Math.hypot(.2, .04)) * 180 / Math.PI);
  close(sixty.aspectDegrees, (Math.atan2(-.2, -.04) * 180 / Math.PI + 360) % 360);
});

test("flat and near-flat surfaces retain elevation but have no stable facing direction", () => {
  for (const degrees of [0, .1, .49]) {
    const cell = surface.terrainSurfaceCell(plane(Math.tan(degrees * Math.PI / 180), 0, { elevation: 412 }), 2, 2);
    close(cell.slopeDegrees, degrees);
    assert.equal(cell.aspectDegrees, null);
    assert.equal(surface.terrainAspectDirection(cell.aspectDegrees), "Flat");
    assert.equal(cell.elevationMeters, 412);
  }
  assert.equal(surface.TERRAIN_SURFACE_FLAT_DEGREES, .5);
  assert.equal(surface.terrainSurfaceCell(plane(Math.tan(.501 * Math.PI / 180), 0), 2, 2).aspectDegrees, 270);
});

test("all nine Horn neighbors must be finite; missing neighborhoods stay holes", () => {
  for (const missing of [null, NaN, Infinity]) {
    const grid = plane(.1, .05, { size: 7 });
    grid.heights[3 * 7 + 3] = missing;
    const geometry = surface.buildTerrainSurfaceGeometry(grid);
    assert.equal(geometry.totalCellCount, 25);
    assert.equal(geometry.cells.size, 16, "one missing central sample invalidates its nine surrounding cells");
    for (let row = 2; row <= 4; row += 1) for (let column = 2; column <= 4; column += 1) assert.equal(geometry.cells.has(row * 7 + column), false);
    assert.equal(surface.terrainSurfaceCellAt(grid, geometry.cells, [-98, 38]), null);
  }
});

test("invalid or zero-sized grids and outer-rim samples cannot create polygons", () => {
  const valid = plane(.1, 0);
  for (const patch of [{ size: 2 }, { size: 66 }, { size: 4.5 }, { heights: [] }, { spacingMeters: 0 }, { spacingMeters: NaN },
    { bounds: [1, 1, 1, 2] }, { bounds: [1, 2, 2, 1] }, { bounds: [1, 89, 2, 90] }, { bounds: [NaN, 0, 1, 1] }]) {
    const result = surface.buildTerrainSurfaceGeometry({ ...valid, ...patch });
    assert.equal(result.data.features.length, 0);
    assert.equal(result.totalCellCount, 0);
  }
  assert.equal(surface.terrainSurfaceCell(valid, 0, 2), null);
  assert.equal(surface.terrainSurfaceCell(valid, 4, 2), null);
});

test("surface polygons center on exact samples; probes resolve cached cells and reject outside/rim", () => {
  const grid = plane(.1, 0), geometry = surface.buildTerrainSurfaceGeometry(grid);
  const center = surface.terrainSurfaceCellAt(grid, geometry.cells, [-98, 38]);
  assert.equal(center.id, 12);
  const feature = geometry.data.features.find(feature => feature.id === center.id);
  const ring = feature.geometry.coordinates[0];
  assert.equal(ring.length, 5);
  assert.deepEqual(ring[0], ring.at(-1));
  close((ring[0][0] + ring[2][0]) / 2, center.center[0]);
  close((ring[0][1] + ring[2][1]) / 2, center.center[1]);
  const anotherPoint = surface.terrainSurfaceCellAt(grid, geometry.cells, [-98.0001, 38.0001]);
  assert.equal(anotherPoint, center, "deduplication can use stable cached cell identity");
  for (const coordinate of [[-98.1, 38], [-98, 38.1], [grid.bounds[0], 38], [NaN, 38]]) assert.equal(surface.terrainSurfaceCellAt(grid, geometry.cells, coordinate), null);
});

test("fixed slope bins and compass classes are stable at boundaries and independent of look", () => {
  assert.deepEqual([0, 1.999, 2, 5, 10, 20, 89].map(value => surface.terrainSlopeBand(value).key), ["gentle", "gentle", "low", "moderate", "steep", "very-steep", "very-steep"]);
  assert.equal(surface.terrainAspectDirection(22.499), "N");
  assert.equal(surface.terrainAspectDirection(22.5), "NE");
  assert.equal(surface.terrainAspectDirection(337.5), "N");
  assert.equal(surface.terrainAspectDirection(-45), "NW");
  assert.equal(surface.terrainAspectDirection(null), "Flat");
  assert.equal(new Set(surface.TERRAIN_ASPECT_LEGEND.map(entry => entry.color)).size, 9);
  assert.equal(surface.terrainSurfaceOpacity(NaN), .55);
  assert.equal(surface.terrainSurfaceOpacity(1), .75);
  assert.equal(surface.terrainSurfaceOpacity(-1), .2);
});

test("detail grid has at most 3969 cells and yields between bounded four-row batches", () => {
  const grid = plane(.1, 0, { size: 65 }), iterator = surface.terrainSurfaceGeometryBatches(grid);
  let yields = 0, result = iterator.next();
  while (!result.done) { yields += 1; result = iterator.next(); }
  assert.equal(result.value.cells.size, 3969);
  assert.equal(result.value.data.features.length, surface.TERRAIN_SURFACE_MAX_CELLS);
  assert.equal(yields, 15);
});
