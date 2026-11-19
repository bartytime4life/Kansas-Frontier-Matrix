import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const source = ts.transpileModule(await readFile(new URL("../app/basemap-health.ts", import.meta.url), "utf8"), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const health = await import(`data:text/javascript;base64,${Buffer.from(source).toString("base64")}`);
const kansas = { west: -102.1, east: -94.6, south: 36.9, north: 40.1, zoom: 7.4 };
const tileAt = (z, lon, lat, wrap = 0, overscaledZ = z) => {
  const n = 2 ** z, x = Math.floor((lon + 180) / 360 * n);
  const y = Math.floor((1 - Math.log(Math.tan(lat * Math.PI / 180) + 1 / Math.cos(lat * Math.PI / 180)) / Math.PI) / 2 * n);
  return `${z}/${x}/${y}/${wrap}/${overscaledZ}`;
};
const failure = (key, sourceId = "openmaptiles") => {
  const [z, x, y, wrap, overscaledZ] = key.split("/").map(Number);
  const tileID = { canonical: { z, x, y }, wrap, overscaledZ };
  return { sourceId, sourceSpec: { type: "vector", url: "https://example.invalid/planet" }, event: { tile: { tileID, state: "errored" }, coord: tileID, error: { status: 503 } } };
};

test("tiles in the settled view stay in view across vector, raster and pitched-horizon zooms", () => {
  for (const z of [4, 5, 6, 7, 8, 9]) assert.equal(health.basemapTileInView(tileAt(z, -98, 38.5), kansas), true, `z${z}`);
});

test("intermediate-zoom and off-screen tiles leave the view; malformed keys stay conservative", () => {
  assert.equal(health.basemapTileInView(tileAt(3, -98, 38.5), kansas), false, "coarser than the pitched-horizon window");
  assert.equal(health.basemapTileInView(tileAt(10, -98, 38.5), kansas), false, "finer than any tile the view requests");
  assert.equal(health.basemapTileInView(tileAt(7, 10, 50), kansas), false, "another continent");
  assert.equal(health.basemapTileInView(tileAt(7, -98, 38.5, 1), kansas), false, "a wrapped world copy is a different place");
  assert.equal(health.basemapTileInView(tileAt(7, -98, 38.5, 0, 10), kansas), false, "overscaled zoom decides the window");
  assert.equal(health.basemapTileInView("not-a-key", kansas), true);
  assert.equal(health.basemapTileInView(tileAt(7, -98, 38.5), { ...kansas, zoom: Number.NaN }), true);
});

test("retainInView retires only off-view tile failures and never a source failure", () => {
  const model = health.createBasemapHealth(); model.beginStyle();
  model.error(failure(tileAt(3, -98, 38.5)));
  assert.equal(model.warning(), health.BASEMAP_TILE_WARNING);
  model.retainInView(kansas);
  assert.equal(model.warning(), null, "the coarse flight tile is not part of the settled view");
  model.error(failure(tileAt(8, -98, 38.5)));
  model.retainInView(kansas);
  assert.equal(model.warning(), health.BASEMAP_TILE_WARNING, "a real gap in view still warns");
  const sourceOnly = health.createBasemapHealth(); sourceOnly.beginStyle();
  sourceOnly.error({ sourceId: "openmaptiles", sourceSpec: { type: "vector", url: "https://example.invalid/planet" }, event: { error: { status: 503 } } });
  sourceOnly.retainInView({ ...kansas, west: 100, east: 110 });
  assert.equal(sourceOnly.warning(), health.BASEMAP_SOURCE_WARNING, "a tileless source failure has no view to leave");
});
