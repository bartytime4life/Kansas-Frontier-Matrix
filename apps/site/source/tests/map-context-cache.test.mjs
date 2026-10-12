import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const source = await readFile(new URL("../app/map-context-cache.ts", import.meta.url), "utf8");
const atlasSource = await readFile(new URL("../app/event-atlas.ts", import.meta.url), "utf8");
const atlasCode = ts.transpileModule(atlasSource, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const atlasUrl = `data:text/javascript;base64,${Buffer.from(atlasCode).toString("base64")}`;
const code = ts.transpileModule(source.replace('"./event-atlas"', JSON.stringify(atlasUrl)), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const cache = await import(`data:text/javascript;base64,${Buffer.from(code).toString("base64")}`);

function privateDirectory() {
  const files = new Map(), folders = new Map();
  const directory = (path = "") => ({
    async getDirectoryHandle(name, { create = false } = {}) {
      const key = path ? `${path}/${name}` : name;
      if (!folders.has(key)) { if (!create) throw new DOMException("Missing", "NotFoundError"); folders.set(key, directory(key)); }
      return folders.get(key);
    },
    async getFileHandle(name, { create = false } = {}) {
      const key = `${path}/${name}`;
      if (!files.has(key) && !create) throw new DOMException("Missing", "NotFoundError");
      return {
        async getFile() { return files.get(key); },
        async createWritable() {
          let next;
          return { async write(body) { next = new Blob([body]); }, async close() { files.set(key, next); }, async abort() {} };
        },
      };
    },
  });
  return { root: directory(), files };
}

test("private map directory stores only exact dated fire payloads and indexed radar frames", async () => {
  const prior = Object.getOwnPropertyDescriptor(globalThis, "navigator");
  const store = privateDirectory();
  Object.defineProperty(globalThis, "navigator", { configurable: true, value: { storage: { getDirectory: async () => store.root } } });
  try {
    const fire = { feed: "nasa-gibs-fire-points", sourceDay: "2024-05-19", state: "partial", featureCount: 1, retrievedAt: "2026-10-08T00:00:00Z", data: { type: "FeatureCollection", features: [{ type: "Feature", geometry: { type: "Point", coordinates: [-97, 38] }, properties: { acquiredAt: "2024-05-19T20:10:00Z" } }] } };
    assert.throws(() => cache.mapCachePath("fire", "2024-02-30"));
    await assert.rejects(() => cache.saveFireDay("2024-05-18", fire), /does not match/);
    assert.ok(await cache.saveFireDay("2024-05-19", fire));
    assert.deepEqual(await cache.readFireDay("2024-05-19"), fire);
    assert.equal(await cache.readFireDay("2024-05-18"), null);
    assert.ok(store.files.has("KFM-map-display-context/fire-detections/2024-05-19.json"));

    const time = "2007-05-05T02:45:00.000Z";
    const scan = { time, product: "n0r", artifact: "https://mesonet.agron.iastate.edu/archive/data/2007/05/05/GIS/uscomp/n0r_200705050245.png" };
    const frame = new Blob([Uint8Array.of(137,80,78,71,13,10,26,10,1)], { type: "image/png" });
    await cache.saveRadarFrame(time, frame);
    assert.equal(await cache.readRadarFrame(time), null, "an unindexed file is not map-ready");
    const index = { format: "kfm-radar-map-cache-v1", day: "2007-05-05", start: "2007-05-05T02:00:00.000Z", end: "2007-05-05T03:00:00.000Z", retrievedAt: "2026-10-08T00:00:00Z", savedAt: "2026-10-08T00:00:00Z", bytes: frame.size, partial: true, scans: [scan] };
    assert.equal(cache.validRadarCacheIndex(index), true);
    await cache.saveRadarIndex(index);
    assert.equal((await cache.readRadarFrame(time))?.size, frame.size);
    assert.deepEqual((await cache.readRadarIndex("2007-05-05"))?.scans, [scan]);
    const fallback = cache.radarManifestFromCache(index, index.start, index.end);
    assert.deepEqual(fallback.radar.scans, [scan]);
    assert.equal(fallback.evidenceRole, "EXTERNAL_CONTEXT_ONLY");
    assert.equal(cache.radarManifestFromCache(index, "2007-05-05T01:00:00.000Z", index.end), null);
  } finally {
    if (prior) Object.defineProperty(globalThis, "navigator", prior); else delete globalThis.navigator;
  }
});
