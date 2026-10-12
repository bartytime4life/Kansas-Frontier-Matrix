import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const source = await readFile(new URL("../app/terrain-relief-style.ts", import.meta.url), "utf8");
const compiled = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const { applyTopographicRasterDepth } = await import(`data:text/javascript;base64,${Buffer.from(compiled).toString("base64")}`);

test("topographic depth restores the original 2D raster paint without touching map content", () => {
  const original = new Map([["raster-opacity", 0.94], ["raster-fade-duration", 120]]);
  const paint = new Map(original);
  const writes = [];
  let layerPresent = true;
  const map = {
    getLayer: () => layerPresent ? { type: "raster" } : undefined,
    getPaintProperty: (_layer, property) => paint.get(property),
    setPaintProperty: (_layer, property, value) => {
      writes.push([property, value]);
      if (value === undefined) paint.delete(property);
      else paint.set(property, value);
    },
  };

  applyTopographicRasterDepth(map, true);
  assert.equal(paint.get("raster-opacity"), 0.94);
  assert.equal(paint.get("raster-fade-duration"), 120);
  assert.ok(paint.get("raster-contrast") > 0);
  assert.ok(paint.get("raster-brightness-max") < 1);
  assert.equal(writes.length, 3);
  applyTopographicRasterDepth(map, true);
  assert.equal(writes.length, 3, "an unchanged view does not repaint tiles");

  applyTopographicRasterDepth(map, false);
  assert.deepEqual(paint, original, "2D returns to the original raster style properties");
  assert.equal(writes.length, 6);
  applyTopographicRasterDepth(map, false);
  assert.equal(writes.length, 6, "restoration is idempotent");

  layerPresent = false;
  applyTopographicRasterDepth(map, true);
  assert.equal(writes.length, 6, "a different basemap has no topo raster to restyle");
});
