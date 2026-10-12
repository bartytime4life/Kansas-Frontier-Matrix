import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const js = ts.transpileModule(await readFile("app/terrain-provenance-data.ts", "utf8"), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const terrain = await import(`data:text/javascript;base64,${Buffer.from(js).toString("base64")}`);
const pointX = longitude => longitude * Math.PI / 180 * 6378137;
const pointY = latitude => Math.log(Math.tan(Math.PI / 4 + latitude * Math.PI / 360)) * 6378137;
const workUnit = (changes = {}) => ({
  provider_work_unit: "KS_Example_2019", source_url: "https://usgs-lidar-public.s3.amazonaws.com/KS_Example_2019/ept.json",
  metadata_sha256: "1".repeat(64), metadata_bytes: 2300, point_count: 88_025_227_400,
  bounds: [pointX(-100), pointY(38), 100, pointX(-99), pointY(39), 900], srs: { authority: "EPSG", horizontal: "3857" },
  temporal_start: null, temporal_end: null, temporal_reason: "Acquisition dates not asserted by captured EPT metadata", ...changes,
});
const discovery = (projects = [workUnit()], changes = {}) => ({
  schema_version: "kfm-3dep-discovery-v1", selection: "KS_ provider prefix", captured_at: "2026-10-06T16:39:43Z",
  complete_for_prefix: true, complete_for_state: false, project_count: projects.length, metadata_bytes_captured: 2600, projects, ...changes,
});
const close = (actual, expected) => assert.ok(Math.abs(actual - expected) < 1e-9, `${actual} differs from ${expected}`);

test("Web Mercator bounds become a rectangular extent without treating Z as latitude", () => {
  const parsed = terrain.parseTerrainDiscovery(discovery());
  assert.equal(parsed.projects.length, 1);
  parsed.projects[0].geographicExtent.forEach((value, index) => close(value, [-100, 38, -99, 39][index]));
  assert.equal(parsed.projects[0].pointCount, 88_025_227_400);
  assert.equal(parsed.projects[0].verticalCrs, null);
  assert.equal(parsed.projects[0].acquisitionStart, null, "a year in the provider ID is not an acquisition date");
  assert.equal(parsed.projects[0].acquisitionEnd, null);
});

test("only supported, explicit horizontal CRS and legal extents can be plotted", () => {
  const raw = [-100, 38, -50, -99, 39, 850];
  assert.deepEqual(terrain.terrainGeographicExtent(raw, "EPSG", 4326), [-100, 38, -99, 39]);
  assert.equal(terrain.terrainGeographicExtent(raw, "EPSG", "26914"), null);
  assert.equal(terrain.terrainGeographicExtent(raw, null, "4326"), null);
  assert.equal(terrain.terrainGeographicExtent(raw, "OTHER", "4326"), null);
  assert.equal(terrain.terrainGeographicExtent([-181, 38, 0, -99, 39, 1], "EPSG", "4326"), null);
  assert.equal(terrain.terrainGeographicExtent([-100, 38, 0, -100, 39, 1], "EPSG", "4326"), null);
  assert.equal(terrain.terrainGeographicExtent([0, 0, 0, 30_000_000, 1, 1], "EPSG", "3857"), null);
  assert.equal(terrain.terrainGeographicExtent(null, "EPSG", "3857"), null);
});

test("unsupported CRS retains provenance and native bounds without fabricating geography", () => {
  const item = terrain.parseTerrainDiscovery(discovery([workUnit({ srs: { authority: "EPSG", horizontal: "26914", vertical: "5703" } })])).projects[0];
  assert.equal(item.geographicExtent, null);
  assert.equal(item.horizontalCrs, "EPSG:26914");
  assert.equal(item.verticalCrs, "EPSG:5703", "reported code is retained, not translated into a verified datum");
  assert.equal(item.nativeBounds.length, 6);
});

test("source links require the exact public work-unit metadata URL", () => {
  for (const source_url of ["javascript:alert(1)", "https://evil.example/KS_Example_2019/ept.json", "https://user@usgs-lidar-public.s3.amazonaws.com/KS_Example_2019/ept.json", "https://usgs-lidar-public.s3.amazonaws.com/KS_Other/ept.json", "https://usgs-lidar-public.s3.amazonaws.com/KS_Example_2019/ept.json?download=1"]) {
    const result = terrain.parseTerrainDiscovery(discovery([workUnit({ source_url })]));
    assert.equal(result.projects.length, 0);
    assert.equal(result.completeForPrefix, false);
  }
});

test("invalid or duplicate provenance cannot retain complete-listing labels", () => {
  const result = terrain.parseTerrainDiscovery(discovery([workUnit(), workUnit(), workUnit({ metadata_sha256: "bad" })]));
  assert.equal(result.projects.length, 1);
  assert.equal(result.rejectedProjects, 2);
  assert.equal(result.completeForPrefix, false);
  assert.equal(terrain.parseTerrainDiscovery(discovery(undefined, { project_count: 99 })).completeForPrefix, false);
  assert.equal(terrain.parseTerrainDiscovery(discovery(undefined, { complete_for_state: true })).completeForState, false);
  assert.equal(terrain.parseTerrainDiscovery({}), null);
  assert.equal(terrain.parseTerrainDiscovery(discovery(undefined, { selection: "all Kansas" })), null);
});

test("invalid dates and non-finite geometry remain missing instead of appearing valid", () => {
  const result = terrain.parseTerrainDiscovery(discovery([workUnit({ temporal_start: "2019-02-30", temporal_end: "2019-03-10", bounds: [0, 0, 0, Infinity, 1, 1], point_count: Number.MAX_SAFE_INTEGER + 1 })]));
  const item = result.projects[0];
  assert.equal(item.acquisitionStart, null);
  assert.equal(item.acquisitionEnd, null);
  assert.equal(item.geographicExtent, null);
  assert.equal(item.pointCount, null);
  assert.equal(terrain.parseTerrainDiscovery(discovery(undefined, { captured_at: "2026-02-30T00:00:00Z" })), null);
});

test("empty searches do not retain stale selected geometry and diagram always identifies study bounds", () => {
  const projects = terrain.parseTerrainDiscovery(discovery()).projects;
  assert.equal(terrain.filterTerrainWorkUnits(projects, "example").length, 1);
  assert.equal(terrain.filterTerrainWorkUnits(projects, "missing").length, 0);
  const [west, south, east, north] = terrain.terrainDiagramBounds([]);
  assert.ok(west < terrain.TERRAIN_STUDY_BOUNDS[0] && south < terrain.TERRAIN_STUDY_BOUNDS[1]);
  assert.ok(east > terrain.TERRAIN_STUDY_BOUNDS[2] && north > terrain.TERRAIN_STUDY_BOUNDS[3]);
});
