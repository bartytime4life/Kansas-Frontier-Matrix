import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const source = await readFile(new URL("../app/noaa-satellite.ts", import.meta.url), "utf8");
const javascript = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const satellite = await import(`data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`);
const retrievedAt = "2026-09-23T23:50:00.000Z";
const frame = (objectid, name, start, end) => ({ attributes: { objectid, name, start_time: Date.parse(start), end_time: Date.parse(end) } });

test("NOAA frame catalog retains exact provider times and locks tile URL to a raster ID", () => {
  const manifest = satellite.buildNoaaSatelliteManifest({ features: [
    frame(2, "MERGEDGC.10-minute.20260923_2340.color", "2026-09-23T23:30:00Z", "2026-09-23T23:39:00Z"),
    frame(1, "MERGEDGC.10-minute.20260923_2320.color", "2026-09-23T23:10:00Z", "2026-09-23T23:19:00Z"),
  ] }, retrievedAt);
  assert.equal(manifest.freshness, "current");
  assert.deepEqual(manifest.frames.map((item) => item.objectId), [1, 2]);
  assert.equal(satellite.isNoaaSatelliteManifest(manifest), true);
  assert.match(decodeURIComponent(satellite.noaaSatelliteTileUrl(2)), /"mosaicMethod":"esriMosaicLockRaster","lockRasterIds":\[2\]/);
});

test("malformed or stale satellite catalogs stay explicit", () => {
  const stale = satellite.buildNoaaSatelliteManifest({ features: [frame(1, "MERGEDGC.10-minute.20260923_1900.color", "2026-09-23T18:50:00Z", "2026-09-23T18:59:00Z")] }, retrievedAt);
  assert.equal(stale.freshness, "delayed");
  assert.throws(() => satellite.buildNoaaSatelliteManifest({ features: [frame(1, "wrong", "2026-09-23T23:30:00Z", "2026-09-23T23:39:00Z")] }, retrievedAt));
  assert.throws(() => satellite.noaaSatelliteTileUrl(0));
  assert.equal(satellite.isNoaaSatelliteManifest({ ...stale, frames: [{ ...stale.frames[0], objectId: -1 }] }), false);
});
