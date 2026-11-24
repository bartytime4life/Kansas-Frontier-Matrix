import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { inflateSync } from "node:zlib";
import test from "node:test";
import ts from "typescript";

const moduleUrl = (source) => `data:text/javascript;base64,${Buffer.from(source).toString("base64")}`;
const stubLerc = moduleUrl("export default { decode() { throw Error('decoder fixture required'); } };");
const stubUpstream = moduleUrl("export const boundedFetch = () => { throw Error('network forbidden in tests'); };");
const stubTerrain = moduleUrl("export const TERRAIN_TILE_BOUNDS = [-104.8,34.8,-92,42.2]; export const TERRAIN_TILE_TTL = 21600;");
const source = await readFile(new URL("../app/3dep-dem-tiles.ts", import.meta.url), "utf8");
const javascript = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText
  .replace('from "lerc"', `from "${stubLerc}"`)
  .replace('from "./api/event-atlas/upstream"', `from "${stubUpstream}"`)
  .replace('from "./terrain-tiles"', `from "${stubTerrain}"`);
const dem = await import(moduleUrl(javascript));
const tile = (query = "z=8&x=58&y=98") => new Request(`https://kfm.test/api/3dep-dem-tile?${query}`);

test("3DEP elevation requests are Kansas-bound and cannot select arbitrary origins or transformations", async () => {
  let calls = 0;
  const serve = dem.create3DepDemTileService({ fetchBytes: async () => { calls += 1; return new Uint8Array(32); } });
  for (const query of ["z=8&x=58&y=98&url=https://other.test", "z=8&x=58&y=98&z=9", "z=8&x=0&y=0", "z=18&x=58&y=98", "z=8&x=-1&y=98", "z=NaN&x=58&y=98", "z=8&x=256&y=98", "v=1&z=8&x=58&y=98", "v=2&v=2&z=8&x=58&y=98"]) assert.equal((await serve(tile(query))).status, 400);
  assert.equal(calls, 0);
  const upstream = new URL(dem.demTileRequest(new URL(tile().url)).upstream);
  assert.equal(upstream.origin, "https://elevation.nationalmap.gov");
  assert.equal(upstream.searchParams.get("format"), "lerc");
  assert.equal(upstream.searchParams.get("pixelType"), "F32");
  assert.equal(upstream.searchParams.get("size"), "256,256");
  assert.equal(upstream.searchParams.get("renderingRule"), null);
  assert.equal(new URL(dem.demTileRequest(new URL(tile().url)).canonical).searchParams.get("v"), "2");
  assert.equal(dem.demTileRequest(new URL(tile("v=2&z=8&x=58&y=98").url)).key, "8/58/98");
});

test("LERC elevation becomes a correctly encoded Terrarium PNG only when every pixel is valid", async () => {
  const values = new Float32Array(256 * 256).fill(512.25);
  const mask = new Uint8Array(values.length).fill(1);
  const png = await dem.lercToTerrarium(new Uint8Array(32), () => ({ width: 256, height: 256, pixels: [values], mask }));
  assert.deepEqual([...png.subarray(0, 8)], [137, 80, 78, 71, 13, 10, 26, 10]);
  const view = new DataView(png.buffer, png.byteOffset, png.byteLength);
  assert.equal(view.getUint32(16), 256);
  assert.equal(view.getUint32(20), 256);
  const compressedLength = view.getUint32(33);
  const raw = inflateSync(png.subarray(41, 41 + compressedLength));
  assert.equal(raw[0], 0);
  assert.equal(raw[4], 255);
  assert.equal(raw[8], 255);
  assert.equal(raw[1] * 256 + raw[2] + raw[3] / 256 - 32768, 512.25);
  mask[1] = 0;
  await assert.rejects(() => dem.lercToTerrarium(new Uint8Array(32), () => ({ width: 256, height: 256, pixels: [values], mask })), /no-data pixels/);
  mask[1] = 1;
  values[1] = Number.NaN;
  await assert.rejects(() => dem.lercToTerrarium(new Uint8Array(32), () => ({ width: 256, height: 256, pixels: [values], mask })), /no-data pixels/);
  await assert.rejects(() => dem.lercToTerrarium(new Uint8Array(32), () => ({ width: 512, height: 256, pixels: [values] })));
});

test("3DEP tile work coalesces, caches, and pauses only the failed tile before retry", async () => {
  let now = 1000, calls = 0;
  const output = new Uint8Array([137, 80, 78, 71]);
  const serve = dem.create3DepDemTileService({ now: () => now, fetchBytes: async () => { calls += 1; return new Uint8Array(32); }, convert: async () => output });
  const responses = await Promise.all([serve(tile()), serve(tile())]);
  assert.equal(calls, 1);
  assert.ok(responses.every(response => response.status === 200));
  assert.equal((await serve(tile())).headers.get("X-KFM-Tile-Cache"), "MEMORY");
  now += 21601 * 1000;
  await serve(tile());
  assert.equal(calls, 2);
  let attempts = 0, retryNow = 1000;
  const retry = dem.create3DepDemTileService({ now: () => retryNow, fetchBytes: async () => { attempts += 1; return new Uint8Array(32); }, convert: async () => { if (attempts === 1) throw Error("bad LERC"); return output; } });
  const failed = await Promise.all([retry(tile()), retry(tile())]);
  assert.equal(attempts, 1);
  assert.ok(failed.every(response => response.status === 502 && response.headers.get("Retry-After") === "5"));
  assert.equal(failed[0].headers.get("Cache-Control"), "no-store");
  const paused = await retry(tile());
  assert.equal(paused.status, 502);
  assert.equal(paused.headers.get("X-KFM-Tile-Cache"), "RECENT_FAILURE");
  assert.equal(attempts, 1);
  assert.equal((await retry(tile("z=8&x=59&y=98"))).status, 200);
  assert.equal(attempts, 2);
  retryNow += 5_001;
  assert.equal((await retry(tile())).status, 200);
  assert.equal(attempts, 3);
});

test("masked elevation tiles report a persistent source gap without repeated upstream fetches", async () => {
  let now = 1000, calls = 0;
  const values = new Float32Array(256 * 256).fill(500);
  const mask = new Uint8Array(values.length).fill(1);
  mask[1] = 0;
  const serve = dem.create3DepDemTileService({ now: () => now, fetchBytes: async () => { calls += 1; return new Uint8Array(32); }, convert: (bytes) => dem.lercToTerrarium(bytes, () => ({ width: 256, height: 256, pixels: [values], mask })) });
  const first = await serve(tile());
  assert.equal(first.status, 422);
  assert.match((await first.json()).error, /missing data/);
  assert.equal(first.headers.get("Retry-After"), "21600");
  const paused = await serve(tile());
  assert.equal(paused.status, 422);
  assert.equal(paused.headers.get("X-KFM-Tile-Cache"), "RECENT_FAILURE");
  assert.equal(calls, 1);
  now += 21_600_001;
  assert.equal((await serve(tile())).status, 422);
  assert.equal(calls, 2);
});


test("continuous Kansas terrain admits z16/z17 detail with the same bounded provider and metre encoding", () => {
  for (const z of [6, 15, 16, 17]) {
    const n = 2 ** z, lon = -96.56, lat = 39.1;
    const x = Math.floor((lon + 180) / 360 * n);
    const y = Math.floor((1 - Math.asinh(Math.tan(lat * Math.PI / 180)) / Math.PI) / 2 * n);
    const result = dem.demTileRequest(new URL(tile(`z=${z}&x=${x}&y=${y}`).url));
    const upstream = new URL(result.upstream);
    assert.equal(upstream.origin, "https://elevation.nationalmap.gov");
    assert.equal(upstream.searchParams.get("pixelType"), "F32");
    assert.equal(upstream.searchParams.get("size"), "256,256");
    const extent = upstream.searchParams.get("bbox").split(",").map(Number);
    assert.ok(extent.every(Number.isFinite));
    assert.ok(Math.abs((extent[2] - extent[0]) - 40075016.68557849 / n) < 1e-7);
    const groundPixelMetres = (extent[2] - extent[0]) / 256 * Math.cos(lat * Math.PI / 180);
    if (z === 17) assert.ok(groundPixelMetres > 0.8 && groundPixelMetres < 1.1);
  }
});

test("3DEP memory and edge replies cannot outlive their original source-cache expiry", async () => {
  const ttl = 21_600_000, started = 1000;
  let now = started, calls = 0;
  const bytes = new Uint8Array([137, 80, 78, 71]);
  const serve = dem.create3DepDemTileService({ now: () => now, fetchBytes: async () => { calls++; return new Uint8Array(32); }, convert: async () => bytes });
  assert.equal((await serve(tile())).headers.get("Cache-Control"), "public, max-age=900, s-maxage=21600");
  now = started + ttl - 5000;
  const memory = await serve(tile());
  assert.equal(memory.headers.get("Cache-Control"), "public, max-age=5, s-maxage=5");
  assert.equal(memory.headers.get("X-KFM-Retrieved-At"), new Date(started).toISOString());
  assert.equal(calls, 1);
  const edge = dem.create3DepDemTileService({ now: () => now, fetchBytes: async () => assert.fail("fresh edge copy must not fetch"), edgeCache: () => ({ match: async () => new Response(bytes, { headers: { "Content-Type": "image/png", "X-KFM-Retrieved-At": new Date(started).toISOString(), "Cache-Control": "public, max-age=900, s-maxage=21600" } }) }) });
  const cached = await edge(tile());
  assert.equal(cached.headers.get("X-KFM-Tile-Cache"), "EDGE");
  assert.equal(cached.headers.get("Cache-Control"), "public, max-age=5, s-maxage=5");
  now = started + ttl - 1;
  assert.equal((await serve(tile())).headers.get("Cache-Control"), "public, max-age=0, s-maxage=0");
  now++;
  assert.equal((await serve(tile())).headers.get("X-KFM-Tile-Cache"), "ORIGIN");
  assert.equal(calls, 2, "expired data requires a new source read");
});
