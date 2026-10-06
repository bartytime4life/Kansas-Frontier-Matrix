import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

async function compile(name, imports = {}) {
  const source = await readFile(new URL(`../app/${name}.ts`, import.meta.url), "utf8");
  const code = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 } }).outputText;
  const result = { exports: {} };
  new Function("require", "module", "exports", code)(id => imports[id], result, result.exports);
  return result.exports;
}
const context = await compile("earth-engine-context");
const comparison = await compile("earth-engine-comparison", { "./earth-engine-context": context });
const hash = value => createHash("sha256").update(Buffer.from(value)).digest("hex");
const bytes = value => new TextEncoder().encode(JSON.stringify(value)).buffer;
const digest = "a".repeat(64);
function manifest(year, id = "ee-prism-monthly") {
  const source = context.EARTH_ENGINE_CONTEXT_LAYERS.find(item => item.id === id);
  return { schema: "kfm-earth-engine-context/v1", setId: `ks-${year}-synthetic`, boundary: "Kansas · TIGER/2018/States · STATEFP 20", approvedAt: "2026-10-06T00:00:00Z", reviewState: "APPROVED_VISUAL_CONTEXT", admission: "NOT_ADMITTED", evidence: "NOT_CLAIM_EVIDENCE", layers: [{ id, status: "approved", source: source.source, period: context.earthEngineLayerPeriod(id, year), resolutionMeters: id.startsWith("ee-prism-") || id === "ee-terraclimate" ? 4638 : id === "ee-chirps" ? 5566 : 30, attribution: context.earthEngineLayerAttribution(id, year), limits: "Synthetic contract fixture; no observations", legend: source.legend, geotiffSha256: digest, reviewSha256: digest, tileIndexes: { 0: { sha256: digest, count: 1, minX: 0, maxX: 0, minY: 0, maxY: 0 } } }] };
}

test("new products validate only their own source/year contracts and preserve terrain semantics", () => {
  for (const id of ["ee-prism-monthly", "ee-prism-daily", "ee-landsat4", "ee-landsat5", "ee-landsat7", "ee-landsat8", "ee-landsat9"]) {
    const [first, last] = context.EARTH_ENGINE_SOURCE_YEARS[id];
    for (const year of [first, last]) assert.ok(context.parseEarthEngineManifest(manifest(year, id)), `${id} ${year}`);
    for (const year of [first - 1, last + 1]) assert.equal(context.parseEarthEngineManifest(manifest(year, id)), null, `${id} ${year}`);
    const wrongSource = manifest(first, id); wrongSource.layers[0].source += "-wrong";
    assert.equal(context.parseEarthEngineManifest(wrongSource), null);
  }
  assert.equal(context.earthEngineSetYear({ setId: "ks-1895-synthetic" }), 1895);
  for (const year of [1894, 2026, 9999]) assert.equal(context.parseEarthEnginePointer({ schema: "kfm-earth-engine-context-pointer/v1", setId: `ks-${year}-synthetic`, manifestSha256: digest }), null);
  assert.ok(context.parseEarthEngineManifest(manifest(2024, "ee-3dep")));
  assert.equal(context.parseEarthEngineManifest(manifest(1895, "ee-3dep")), null);
  const terrain = manifest(2024, "ee-3dep"); terrain.setId = "ks-terrain-synthetic";
  assert.ok(context.parseEarthEngineManifest(terrain));
  assert.equal(context.parseEarthEngineCatalog({ manifests: [terrain, manifest(1895)] }).length, 2);
  assert.equal(context.parseEarthEngineCatalog({ manifests: [terrain, manifest(2024)] }), null);
});

test("full 1895–2025 catalog fits the bounded client contract; duplicates and extra history fail", () => {
  const manifests = Array.from({ length: 131 }, (_, i) => manifest(1895 + i));
  assert.equal(context.parseEarthEngineCatalog({ manifests }).length, 131);
  assert.equal(context.parseEarthEngineCatalog({ manifests: [...manifests, manifest(1895)] }), null);
  assert.equal(context.parseEarthEngineCatalog({ manifests: [manifest(1895), manifest(1895)] }), null);
  assert.ok(context.EARTH_ENGINE_CATALOG_MAX_BYTES >= 131 * 96_000);
});

test("comparisons use installed years of a single mission or PRISM cadence including 1895", async t => {
  const old = manifest(1895), next = manifest(1896);
  assert.equal(comparison.comparisonPair([old, next], "ee-prism-monthly", 1895, 1896).kind, "ready");
  assert.equal(comparison.comparisonPair([manifest(1984, "ee-landsat4"), manifest(1985, "ee-landsat5")], "ee-landsat4", 1984, 1985).kind, "unavailable");
  assert.equal(comparison.comparisonPair([manifest(1984, "ee-landsat4"), manifest(1985, "ee-landsat4")], "ee-landsat4", 1984, 1985).kind, "ready");
  const png = Uint8Array.from([137,80,78,71,13,10,26,10,0,0,0,13,73,72,68,82,0,0,1,0,0,0,1,0]);
  t.mock.method(globalThis, "fetch", async () => new Response(png, { headers: { "content-type": "image/png" } }));
  await comparison.readComparisonTile("/api/earth-engine-context/ks-1895-synthetic/ee-prism-monthly/0/0/0.png", new AbortController().signal);
  await assert.rejects(comparison.readComparisonTile("/api/earth-engine-context/ks-1894-synthetic/ee-prism-monthly/0/0/0.png", new AbortController().signal), /Invalid/);
});

async function harness() {
  const objects = new Map(), calls = []; let override;
  const bucket = {
    async get(key) { const raw = objects.get(key); return raw ? { size: raw.byteLength, arrayBuffer: async () => raw.slice(0) } : null; },
    async put(key, raw) { objects.set(key, raw.slice(0)); },
    async list(options) {
      calls.push(options);
      if (override) return override(options);
      const keys = [...objects.keys()].filter(key => key.startsWith(options.prefix)).sort();
      const start = Number(options.cursor ?? 0), slice = keys.slice(start, start + options.limit), next = start + slice.length;
      return { objects: slice.map(key => ({ key })), truncated: next < keys.length, ...(next < keys.length ? { cursor: String(next) } : {}) };
    },
  };
  const server = await compile("earth-engine-context-server", {
    "./earth-engine-context": context, "./earth-engine-local-read": { localImageryReadAllowed: () => false },
    "cloudflare:workers": { env: { BUCKET: bucket, KFM_EARTH_ENGINE_OWNER_EMAILS: "owner@example.test" } },
    "./chatgpt-auth": { getChatGPTUser: async () => ({ email: "owner@example.test" }) },
  });
  const activate = await compile("api/earth-engine-context/activate/route", { "../../../earth-engine-context": context, "../../../earth-engine-context-server": server });
  const stage = await compile("api/earth-engine-context/stage/route", { "../../../earth-engine-context": context, "../../../earth-engine-context-server": server });
  function install(value) {
    const raw = bytes(value); objects.set(context.earthEngineManifestKey(value.setId), raw);
    const year = context.earthEngineSetYear(value);
    objects.set(year === 2024 ? context.EARTH_ENGINE_CONTEXT_ACTIVE_KEY : context.earthEngineYearPointerKey(year), bytes({ schema: "kfm-earth-engine-context-pointer/v1", setId: value.setId, manifestSha256: hash(raw) }));
  }
  return { objects, calls, server, stage, activate, install, override: value => { override = value; } };
}

test("server reads all131 supported years through bounded pagination and rejects duplicate or stuck pages", async () => {
  const h = await harness(); for (let year = 1895; year <= 2025; year++) h.install(manifest(year));
  assert.equal((await h.server.activeEarthEngineCatalog()).length, 131);
  assert.equal(h.calls.length, 2); assert.equal(h.calls[1].cursor, "100"); assert.equal(h.calls[0].limit, 100);
  h.override(() => ({ objects: [{ key: context.earthEngineYearPointerKey(1895) }], truncated: true, cursor: "stuck" }));
  await assert.rejects(h.server.activeEarthEngineCatalog(), /failed validation|cursor/);
  h.override(() => ({ objects: [], truncated: true })); await assert.rejects(h.server.activeEarthEngineCatalog(), /cursor/);
  h.override(() => ({ objects: [{ key: context.earthEngineYearPointerKey(1894) }], truncated: false })); await assert.rejects(h.server.activeEarthEngineCatalog(), /failed validation/);
});

test("stage accepts hashed 1895 PRISM and sensor-specific index paths while refusing out-of-contract paths", async () => {
  const h = await harness(), raw = bytes(manifest(1895));
  const put = key => h.stage.PUT(new Request(`https://kfm.example/api/earth-engine-context/stage?key=${encodeURIComponent(key)}`, { method: "PUT", headers: { origin: "https://kfm.example", "content-type": "application/json", "x-kfm-ee-sha256": hash(raw) }, body: raw }));
  assert.equal((await put(context.earthEngineManifestKey("ks-1895-synthetic"))).status, 200);
  assert.equal((await put(context.earthEngineIndexKey("ks-1982-synthetic", "ee-landsat4", 0))).status, 200);
  assert.equal((await put(context.earthEngineIndexKey("ks-1895-synthetic", "ee-prism-monthly", 0))).status, 200);
  assert.equal((await put(context.earthEngineManifestKey("ks-1894-synthetic"))).status, 400);
  assert.equal((await put(context.earthEngineIndexKey("ks-1895-synthetic", "ee-landsat-mss", 0))).status, 400);
});


test("new historical products still require activation and exact tile integrity", async () => {
  for (const [year, id] of [[1895, "ee-prism-monthly"], [1981, "ee-prism-daily"], [1982, "ee-landsat4"], [1984, "ee-landsat5"], [1999, "ee-landsat7"], [2013, "ee-landsat8"], [2021, "ee-landsat9"]]) {
    const h = await harness(), value = manifest(year, id);
    const png = Uint8Array.from(Buffer.from("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQIHWP4z8DwHwAFgAI/ScL/nwAAAABJRU5ErkJggg==", "base64")).buffer;
    const index = bytes({ tiles: { "0/0": hash(png) } });
    value.layers[0].tileIndexes[0].sha256 = hash(index);
    const raw = bytes(value), pointer = bytes({ schema: "kfm-earth-engine-context-pointer/v1", setId: value.setId, manifestSha256: hash(raw) });
    h.objects.set(context.earthEngineManifestKey(value.setId), raw);
    h.objects.set(context.earthEngineIndexKey(value.setId, id, 0), index);
    const activate = () => h.activate.POST(new Request("https://kfm.example/api/earth-engine-context/activate", { method: "POST", headers: { origin: "https://kfm.example", "content-type": "application/json" }, body: pointer }));
    assert.equal(await h.server.earthEngineTile(value.setId, id, "0", "0", "0.png"), null, "staged data cannot render");
    assert.equal((await activate()).status, 409, `${id}: missing tile blocks activation`);
    const key = context.earthEngineTileKey(value.setId, id, 0, 0, 0);
    h.objects.set(key, png);
    assert.equal((await activate()).status, 200, id);
    assert.deepEqual(await h.server.earthEngineTile(value.setId, id, "0", "0", "0.png"), png);
    assert.equal(await h.server.earthEngineTile(value.setId.replace("synthetic", "another"), id, "0", "0", "0.png"), null);
    h.objects.delete(key);
    assert.equal(await h.server.earthEngineTile(value.setId, id, "0", "0", "0.png"), null);
    const corrupt = png.slice(0); new Uint8Array(corrupt)[24] ^= 1; h.objects.set(key, corrupt);
    await assert.rejects(h.server.earthEngineTile(value.setId, id, "0", "0", "0.png"), /failed validation/);
  }
});
