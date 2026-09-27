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
  for (const query of ["z=8&x=58&y=98&url=https://other.test", "z=8&x=58&y=98&z=9", "z=8&x=0&y=0", "z=16&x=58&y=98", "z=8&x=-1&y=98", "z=NaN&x=58&y=98", "z=8&x=256&y=98"]) assert.equal((await serve(tile(query))).status, 400);
  assert.equal(calls, 0);
  const upstream = new URL(dem.demTileRequest(new URL(tile().url)).upstream);
  assert.equal(upstream.origin, "https://elevation.nationalmap.gov");
  assert.equal(upstream.searchParams.get("format"), "lerc");
  assert.equal(upstream.searchParams.get("pixelType"), "F32");
  assert.equal(upstream.searchParams.get("size"), "256,256");
  assert.equal(upstream.searchParams.get("renderingRule"), null);
});

test("LERC elevation becomes a correctly encoded Terrarium PNG without inventing masked pixels", async () => {
  const values = new Float32Array(256 * 256).fill(512.25);
  const mask = new Uint8Array(values.length).fill(1);
  mask[1] = 0;
  const png = await dem.lercToTerrarium(new Uint8Array(32), () => ({ width: 256, height: 256, pixels: [values], mask }));
  assert.deepEqual([...png.subarray(0, 8)], [137, 80, 78, 71, 13, 10, 26, 10]);
  const view = new DataView(png.buffer, png.byteOffset, png.byteLength);
  assert.equal(view.getUint32(16), 256);
  assert.equal(view.getUint32(20), 256);
  const compressedLength = view.getUint32(33);
  const raw = inflateSync(png.subarray(41, 41 + compressedLength));
  assert.equal(raw[0], 0);
  assert.equal(raw[4], 255);
  assert.equal(raw[8], 0);
  assert.equal(raw[1] * 256 + raw[2] + raw[3] / 256 - 32768, 512.25);
  await assert.rejects(() => dem.lercToTerrarium(new Uint8Array(32), () => ({ width: 512, height: 256, pixels: [values] })));
});

test("3DEP tile work coalesces, caches, and leaves bad provider responses retryable", async () => {
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
  let attempts = 0;
  const retry = dem.create3DepDemTileService({ fetchBytes: async () => { attempts += 1; return new Uint8Array(32); }, convert: async () => { if (attempts === 1) throw Error("bad LERC"); return output; } });
  const failed = await retry(tile());
  assert.equal(failed.status, 502);
  assert.equal(failed.headers.get("Cache-Control"), "no-store");
  assert.equal((await retry(tile())).status, 200);
});
