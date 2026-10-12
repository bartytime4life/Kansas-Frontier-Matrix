import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const source = await readFile(new URL("../app/noaa-satellite.ts", import.meta.url), "utf8");
const javascript = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const satellite = await import(`data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`);
const asModuleUrl = (source, fileName) => `data:text/javascript;base64,${Buffer.from(ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 }, fileName }).outputText).toString("base64")}`;
const retrievedAt = "2026-09-23T23:50:00.000Z";
const frame = (objectid, name, start, end) => ({ attributes: { objectid, name, start_time: Date.parse(start), end_time: Date.parse(end) } });

test("NOAA frame catalog retains exact provider times and locks tile URL to a raster ID", () => {
  const manifest = satellite.buildNoaaSatelliteManifest({ features: [
    frame(2, "MERGEDGC.10-minute.20260923_2340.color", "2026-09-23T23:30:00Z", "2026-09-23T23:39:00Z"),
    frame(1, "MERGEDGC.10-minute.20260923_2320.color", "2026-09-23T23:10:00Z", "2026-09-23T23:19:00Z"),
  ] }, retrievedAt);
  assert.equal(manifest.freshness, "current");
  assert.equal(manifest.product, "geocolor");
  assert.deepEqual(manifest.frames.map((item) => item.objectId), [1, 2]);
  assert.equal(satellite.isNoaaSatelliteManifest(manifest), true);
  assert.match(decodeURIComponent(satellite.noaaSatelliteTileUrl(manifest.frames[1])), /"mosaicMethod":"esriMosaicLockRaster","lockRasterIds":\[2\]/);
});

test("dated NOAA nowCOAST visible imagery is explicitly labeled when GeoColor is unavailable", () => {
  const xml = '<WMS_Capabilities><Layer><Name>goes_visible_imagery</Name><Dimension name="time" default="2026-09-23T23:45:00.000Z" units="ISO8601">2026-09-23T23:40:00.000Z,2026-09-23T23:45:00.000Z</Dimension></Layer></WMS_Capabilities>';
  const manifest = satellite.buildNoaaVisibleManifest(xml, retrievedAt);
  assert.equal(manifest.product, "visible");
  assert.equal(manifest.kind, "noaa-goes-visible-frames");
  assert.equal(manifest.frames.length, 2);
  assert.equal(satellite.isNoaaSatelliteManifest(manifest), true);
  assert.match(manifest.limitation, /not GeoColor/);
  assert.match(satellite.noaaSatelliteTileUrl(manifest.frames[1]), /layers=goes_visible_imagery/);
  assert.match(decodeURIComponent(satellite.noaaSatelliteTileUrl(manifest.frames[1])), /time=2026-09-23T23:45:00.000Z/);
  assert.throws(() => satellite.buildNoaaVisibleManifest(xml.replaceAll("2026-09-23T23:45:00.000Z", "latest"), retrievedAt));
});

test("the frames API uses only the fixed dated NOAA fallback when GeoColor fails", async () => {
  const routeSource = await readFile(new URL("../app/api/noaa-satellite/frames/route.ts", import.meta.url), "utf8");
  const boundedSource = await readFile(new URL("../app/bounded-json.ts", import.meta.url), "utf8");
  const nextStub = 'export const NextResponse = { json: (value, options) => Response.json(value, options) };';
  const routeUrl = asModuleUrl(routeSource
    .replace('"../../../bounded-json"', `"${asModuleUrl(boundedSource, "bounded-json.ts")}"`)
    .replace('"../../../noaa-satellite"', `"${asModuleUrl(source, "noaa-satellite.ts")}"`)
    .replace('"next/server"', `"data:text/javascript,${encodeURIComponent(nextStub)}"`), "noaa-satellite-route.ts");
  const { GET } = await import(routeUrl);
  const originalFetch = globalThis.fetch;
  const recent = new Date(Date.now() - 5 * 60_000).toISOString();
  const xml = `<WMS_Capabilities><Layer><Name>goes_visible_imagery</Name><Dimension name="time">${recent}</Dimension></Layer></WMS_Capabilities>`;
  const origins = [];
  globalThis.fetch = async (url, options) => {
    origins.push(String(url));
    assert.equal(options.redirect, "manual");
    if (origins.length === 2) assert.match(options.headers["User-Agent"], /^KansasFrontierMatrixExplorer\//);
    return origins.length === 1 ? new Response("Unavailable", { status: 503 }) : new Response(xml, { headers: { "content-type": "text/xml" } });
  };
  try {
    const response = await GET();
    assert.equal(response.status, 200);
    const manifest = await response.json();
    assert.equal(manifest.product, "visible");
    assert.equal(satellite.isNoaaSatelliteManifest(manifest), true);
    assert.equal(origins.length, 2);
    assert.ok(origins[0].startsWith(satellite.NOAA_SATELLITE_SERVICE_URL));
    assert.equal(origins[1], satellite.NOAA_SATELLITE_VISIBLE_CAPABILITIES_URL);
    globalThis.fetch = async () => new Response("Unavailable", { status: 503 });
    const unavailable = await GET();
    assert.equal(unavailable.status, 502);
    assert.equal((await unavailable.json()).state, "error");
  } finally { globalThis.fetch = originalFetch; }
});

test("malformed or stale satellite catalogs stay explicit", () => {
  const stale = satellite.buildNoaaSatelliteManifest({ features: [frame(1, "MERGEDGC.10-minute.20260923_1900.color", "2026-09-23T18:50:00Z", "2026-09-23T18:59:00Z")] }, retrievedAt);
  assert.equal(stale.freshness, "delayed");
  assert.throws(() => satellite.buildNoaaSatelliteManifest({ features: [frame(1, "wrong", "2026-09-23T23:30:00Z", "2026-09-23T23:39:00Z")] }, retrievedAt));
  assert.throws(() => satellite.noaaSatelliteTileUrl({ kind: "geocolor", objectId: 0, observedAt: retrievedAt, validThrough: retrievedAt }));
  assert.equal(satellite.isNoaaSatelliteManifest({ ...stale, frames: [{ ...stale.frames[0], objectId: -1 }] }), false);
});
