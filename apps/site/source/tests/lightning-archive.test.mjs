import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import ts from "typescript";
import * as hdf from "h5wasm";
await hdf.ready;
async function load(file) {
  let js = ts.transpileModule(await readFile(file, "utf8"), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
  for (const match of [...js.matchAll(/from ["'](\.[^"']+)["']/g)]) js = js.replace(match[0], `from ${JSON.stringify(await load(path.resolve(path.dirname(file), match[1]) + ".ts"))}`);
  return `data:text/javascript;base64,${Buffer.from(js).toString("base64")}`;
}
const archive = await import(await load("app/lightning-archive.ts"));
const { decodeArchiveFlashes } = await import(await load("app/lightning-archive-decode.ts"));
const { loadLightningArchive } = await import(await load("app/lightning-archive-client.ts"));
const query = { day: "2024-05-21", hour: 21, minute: 0, duration: 15 };
const { start, end } = archive.archiveInterval(query);
const key = "GLM-L2-LCFA/2024/142/21/OR_GLM-L2-LCFA_G16_s20241422100000_e20241422100200_c20241422100217.nc";
const listing = (truncated = false) => `<ListBucketResult><IsTruncated>${truncated}</IsTruncated><Contents><Key>${key}</Key><Size>584935</Size></Contents></ListBucketResult>`;

test("archive dates, leap days, completed intervals and GOES-East transition are explicit", () => {
  assert.equal(archive.archiveInterval({ ...query, day: "2024-02-29" }).end - archive.archiveInterval({ ...query, day: "2024-02-29" }).start, 900000);
  for (const invalid of [{ day: "2023-02-29" }, { day: "2017-07-04" }, { day: "2099-01-01" }, { minute: 15, duration: 30 }, { hour: 24 }, { duration: 1440 }]) assert.throws(() => archive.archiveInterval({ ...query, ...invalid }));
  assert.equal(archive.archiveLocation(Date.parse("2025-04-04T14:00:00Z")).satellite, 16);
  assert.equal(archive.archiveLocation(Date.parse("2025-04-04T15:00:00Z")).satellite, 19);
  assert.throws(() => archive.archiveKeyTime("20243672500000"));
});

test("archive inventory refuses truncation, unexpected keys and ambiguous coverage", () => {
  const location = archive.archiveLocation(start);
  const files = archive.parseArchiveListing(listing(), location);
  assert.equal(files[0].start, start);
  assert.equal(files[0].end, start + 20000);
  assert.throws(() => archive.parseArchiveListing(listing(true), location));
  assert.throws(() => archive.parseArchiveListing(listing().replace("OR_GLM", "../OR_GLM"), location));
  assert.throws(() => archive.selectArchiveFiles([files[0], files[0]], start, end));
  const following = { ...files[0], start: end, end: end + 20000 };
  assert.equal(archive.selectArchiveFiles([files[0], following], start, end).length, 2);
});

test("real NOAA compressed NetCDF decodes geolocation, packed unsigned time and quality", async () => {
  const bytes = await readFile("tests/fixtures/lightning/goes16-20240521t210000.nc");
  const buffer = bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength);
  const file = archive.parseArchiveListing(listing(), archive.archiveLocation(start))[0];
  const result = decodeArchiveFlashes(buffer, file, start, end, hdf);
  assert.equal(result.flashes.length, 25);
  assert.equal(result.omittedQuality, 0);
  assert.deepEqual([result.flashes[0].longitude, result.flashes[0].latitude, result.flashes[0].observedAt], [-94.48589324951172, 38.48883819580078, "2024-05-21T21:00:01.447Z"]);
  assert.ok(result.flashes.some(flash => flash.timeMs > start + 15000));
  assert.ok(result.flashes.every(flash => flash.timeMs >= start && flash.timeMs < end));
  assert.throws(() => decodeArchiveFlashes(buffer, { ...file, size: 1 }, start, end, hdf));
  assert.throws(() => decodeArchiveFlashes(buffer, { ...file, start: start + 1000 }, start, end, hdf));
});

const fakeDecode = () => ({ flashes: [{ id: "known", longitude: -98, latitude: 38.5, timeMs: start + 1000, observedAt: new Date(start + 1000).toISOString(), energyFj: null, areaKm2: null }], omittedQuality: 0 });
function fakeArchive({ missing = 0, corrupt = false, abort } = {}) {
  const total = 46 - missing, id = "a".repeat(64);
  const flash = { id: "known", longitude: -98, latitude: 38.5, timeMs: start + 1000, observedAt: new Date(start + 1000).toISOString(), energyFj: null, areaKm2: null };
  return async url => {
    const p = new URL(url, "https://site.test").searchParams;
    if (!p.has("part")) return Response.json({ id, query, start: new Date(start).toISOString(), end: new Date(end).toISOString(), files: Array.from({ length: total }, () => ({})), expectedFiles: 46, missingFiles: missing, parts: total });
    abort?.abort();
    const part = +p.get("part");
    return new Response(new Uint8Array([part]), { headers: { "X-GLM-Manifest": corrupt ? "b".repeat(64) : id } });
  };
}
test("complete archive assembly deduplicates flashes and discloses missing files", async () => {
  const signal = new AbortController().signal;
  const complete = await loadLightningArchive(query, signal, () => {}, fakeArchive(), hdf, fakeDecode);
  assert.equal(complete.providerCount, 1); assert.equal(complete.state, "ready");
  assert.equal(complete.source, "NOAA_GOES_GLM_ARCHIVE");
  assert.equal(complete.archive.files, 46);
  const partial = await loadLightningArchive(query, signal, () => {}, fakeArchive({ missing: 1 }), hdf, fakeDecode);
  assert.equal(partial.state, "partial"); assert.match(partial.partialReason, /1 of 46/);
});
test("date changes and changing manifests cannot return a mislabeled archive snapshot", async () => {
  const abort = new AbortController();
  await assert.rejects(loadLightningArchive(query, abort.signal, () => {}, fakeArchive({ abort }), hdf, fakeDecode), /abort/i);
  await assert.rejects(loadLightningArchive(query, new AbortController().signal, () => {}, fakeArchive({ corrupt: true }), hdf, fakeDecode), /changed/i);
});

test("legacy signed millisecond and modern dense-attribute NOAA files decode and clean up", async () => {
  const samples = [
    ["goes16-20180501t180000.nc", 16, "2018-05-01T18:00:00Z", "GLM-L2-LCFA/2018/121/18/OR_GLM-L2-LCFA_G16_s20181211800000_e20181211800200_c20181211800223.nc"],
    ["goes19-20261002t180000.nc", 19, "2026-10-02T18:00:00Z", "GLM-L2-LCFA/2026/275/18/OR_GLM-L2-LCFA_G19_s20262751800000_e20262751800200_c20262751800217.nc"],
  ];
  for (const [filename, satellite, time, key] of samples) {
    const bytes = await readFile(`tests/fixtures/lightning/${filename}`), start = Date.parse(time);
    const file = { satellite, key, start, end: start + 20000, size: bytes.length };
    const buffer = bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength);
    assert.equal(decodeArchiveFlashes(buffer, file, start, start + 900000, hdf).flashes.length, 0);
    assert.throws(() => decodeArchiveFlashes(buffer, { ...file, satellite: satellite === 16 ? 19 : 16 }, start, start + 900000, hdf), /identity/);
  }
  assert.equal(hdf.FS.readdir("/").some(name => name.startsWith("kfm-lightning-")), false);
});
