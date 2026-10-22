import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { readFile } from "node:fs/promises";
import { createRequire } from "node:module";
import { test, before, after, beforeEach } from "node:test";
import ts from "typescript";

// Exercise the real route, quota, catalog parser and server with actual local
// R2 conditional writes. Only identity and the external USGS response are fake.
const compile = source => `data:text/javascript;base64,${Buffer.from(ts.transpileModule(source, {
  compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
}).outputText).toString("base64")}`;
const source = name => readFile(new URL(`../app/${name}.ts`, import.meta.url), "utf8");
const model = compile(await source("historical-topo"));
const overlay = compile(await source("historical-topo-overlay"));
const state = { env: {}, user: null, calls: 0, aliases: false, providerStatus: 200, gate: null };
globalThis.__topoQuota = state;
const server = compile((await source("historical-topo-overlay-server"))
  .replace('import { env } from "cloudflare:workers";', "const env = globalThis.__topoQuota.env; const fetch = (...args) => globalThis.__topoQuota.fetch(...args);")
  .replace('import { getChatGPTUser } from "./chatgpt-auth";', "const getChatGPTUser = async () => globalThis.__topoQuota.user;")
  .replace('"./historical-topo"', JSON.stringify(model))
  .replace('"./historical-topo-overlay"', JSON.stringify(overlay)));
const quota = compile((await source("historical-topo-request-quota"))
  .replace('"./historical-topo-overlay"', JSON.stringify(overlay))
  .replace('"./historical-topo-overlay-server"', JSON.stringify(server)));
const route = await import(compile((await source("api/historical-topo/overlay/route"))
  .replaceAll('"../../../historical-topo-overlay"', JSON.stringify(overlay))
  .replaceAll('"../../../historical-topo-overlay-server"', JSON.stringify(server))
  .replaceAll('"../../../historical-topo-request-quota"', JSON.stringify(quota))));
const require = createRequire(import.meta.url), runtimeRequire = createRequire(require.resolve("wrangler"));
const { Miniflare, convertV4MiniflareOptions } = runtimeRequire("miniflare");
let runtime, bucket;
const hash = bytes => createHash("sha256").update(bytes).digest("hex");
const day = () => new Date().toISOString().slice(0, 10);
const quotaKey = () => `historical-topo/v1/requesters/${hash(state.user.id || state.user.email.toLowerCase())}/${day()}.json`;
const queueKey = scan => `historical-topo/v1/requests/${scan}.json`;
const ask = (id, headers = {}) => route.POST(new Request("https://site.test/api/historical-topo/overlay", {
  method: "POST", headers: { Origin: "https://site.test", "Content-Type": "application/json", ...headers }, body: JSON.stringify({ id }),
}));
const accounting = async () => (await bucket.get(quotaKey())).json();
const queued = async () => (await bucket.list({ prefix: "historical-topo/v1/requests/" })).objects;
const wrapBucket = overrides => new Proxy(bucket, { get(target, key) { return overrides[key] ?? (typeof target[key] === "function" ? target[key].bind(target) : target[key]); } });

before(async () => {
  runtime = new Miniflare(convertV4MiniflareOptions({ modules: true,
    script: "export default { fetch() { return new Response('quota-test'); } }", r2Buckets: ["BUCKET"] }));
  bucket = await runtime.getR2Bucket("BUCKET");
  state.fetch = async url => {
    state.calls++;
    const provider = new URL(url);
    assert.equal(provider.origin, "https://ngmdb.usgs.gov");
    const id = Number(/^OBJECTID = (\d+)/.exec(provider.searchParams.get("where"))[1]);
    if (state.gate) await state.gate;
    if (state.providerStatus !== 200) return Response.json({}, { status: state.providerStatus });
    return Response.json({ features: [{ attributes: { OBJECTID: id, scan_id: state.aliases ? 200001 : 200000 + id,
      map_name: "Sheet", primary_state: "KS", date_on_map: 1890, map_scale: 125000 },
      geometry: { rings: [[[-96, 39], [-95.5, 39], [-95.5, 39.5], [-96, 39.5], [-96, 39]]] } }] });
  };
});
after(async () => { delete globalThis.__topoQuota; await runtime?.dispose(); });
beforeEach(async () => {
  const keys = (await bucket.list()).objects.map(o => o.key);
  if (keys.length) await bucket.delete(keys);
  state.env.BUCKET = bucket;
  Object.assign(state, { user: { id: "viewer-1", email: "viewer@example.test" }, calls: 0, aliases: false, providerStatus: 200, gate: null });
});

test("ten acquisitions block further USGS work; cached retries remain free and immutable", async () => {
  for (let id = 1; id <= 10; id++) { const response = await ask(id); assert.equal(response.status, 202, await response.text()); }
  const first = await (await bucket.get(queueKey(200001))).text();
  assert.equal((await ask(11)).status, 429);
  assert.equal((await ask(1)).status, 200);
  assert.equal(state.calls, 10);
  assert.equal((await accounting()).count, 10);
  assert.equal(await (await bucket.get(queueKey(200001))).text(), first);
  assert.equal((await queued()).length, 10);
  const record = JSON.parse(first), sha = "a".repeat(64), packageId = sha.slice(0, 24);
  const manifest = { version: 1, packageId, sheet: record,
    geotiff: { url: `https://prd-tnm.s3.amazonaws.com/StagedProducts/Maps/HistoricalTopo/GeoTIFF/KS/KS_Sheet_200001_1890_125000_geo.tif`,
      sha256: sha, bytes: 5372903, crs: "EPSG:4326", transform: [0, 10, 0, 0, 0, -10], width: 500, height: 500 },
    bounds: [-96, 39, -95.5, 39.5], minZoom: 9, maxZoom: 14, sourceRetrievedAt: "2026-09-30T00:00:00Z",
    tiles: { "9/119/195": { sha256: sha, bytes: 32 } }, evidenceRole: "EXTERNAL_CONTEXT_ONLY" };
  const manifestBytes = JSON.stringify(manifest);
  await bucket.put(`historical-topo/v1/packages/200001/${packageId}/manifest.json`, manifestBytes);
  await bucket.put("historical-topo/v1/active/200001.json", JSON.stringify({ scanId: 200001, packageId,
    manifestSha256: hash(manifestBytes), reviewedAt: new Date().toISOString(), reviewedBy: sha,
    note: "Synthetic owner review", previousPackageId: null, previousManifestSha256: null }));
  assert.equal((await (await ask(1)).json()).state, "ready");
  assert.equal((await (await route.GET(new Request("https://site.test/api/historical-topo/overlay?scan=200001"))).json()).state, "ready");
  assert.equal(state.calls, 10);
});

test("concurrent requests cannot exceed ten acquisitions or queue records", async () => {
  const responses = await Promise.all(Array.from({ length: 30 }, (_, i) => ask(i + 1)));
  assert.equal(responses.filter(r => r.status === 202).length, 10);
  assert.equal(responses.filter(r => r.status === 429).length, 20);
  assert.equal(state.calls, 10);
  assert.equal((await queued()).length, 10);
  assert.equal((await accounting()).count, 10);
});

test("concurrent count-nine updates preserve legacy usage and allow just one provider call", async () => {
  await bucket.put(quotaKey(), JSON.stringify({ count: 9 }));
  const responses = await Promise.all(Array.from({ length: 15 }, (_, i) => ask(i + 1)));
  assert.equal(responses.filter(r => r.status === 202).length, 1);
  assert.equal(responses.filter(r => r.status === 429).length, 14);
  assert.equal(state.calls, 1);
  assert.equal((await accounting()).count, 10);
});

test("same-ID in-flight duplicates do not start another lookup; completion can be retried", async () => {
  let release;
  state.gate = new Promise(resolve => { release = resolve; });
  const first = ask(1);
  try {
    for (let i = 0; i < 200 && !state.calls; i++) await new Promise(resolve => setTimeout(resolve, 5));
    assert.equal(state.calls, 1);
    assert.equal((await ask(1)).status, 429);
  }
  finally { release(); }
  assert.equal((await first).status, 202);
  assert.equal((await ask(1)).status, 200);
  assert.equal(state.calls, 1);
  assert.equal((await accounting()).count, 1);
});

test("distinct catalog aliases retain upstream charges and preserve the first scan request", async () => {
  state.aliases = true;
  assert.equal((await ask(1)).status, 202);
  const first = await (await bucket.get(queueKey(200001))).text();
  for (let id = 2; id <= 10; id++) assert.equal((await ask(id)).status, 200);
  assert.equal((await ask(11)).status, 429);
  assert.equal(state.calls, 10);
  assert.equal((await queued()).length, 1);
  assert.equal(await (await bucket.get(queueKey(200001))).text(), first);
});

test("competing scan aliases create exactly one immutable queue object", async () => {
  state.aliases = true;
  let reads = 0, release;
  const gate = new Promise(resolve => { release = resolve; });
  state.env.BUCKET = wrapBucket({ get: async key => {
    const value = await bucket.get(key);
    if (key === queueKey(200001) && !value) {
      if (++reads === 2) release();
      await gate;
    }
    return value;
  } });
  const responses = await Promise.all([ask(1), ask(2)]);
  assert.deepEqual(responses.map(r => r.status).sort(), [200, 202]);
  assert.equal((await queued()).length, 1);
  const original = await (await bucket.get(queueKey(200001))).text();
  state.env.BUCKET = bucket;
  assert.equal((await ask(1)).status, 200);
  assert.equal((await ask(2)).status, 200);
  assert.equal(await (await bucket.get(queueKey(200001))).text(), original);
  assert.equal(state.calls, 2);
});

test("provider failures retain their charges and retries stop at ten", async () => {
  state.providerStatus = 502;
  for (let i = 0; i < 10; i++) assert.equal((await ask(1)).status, 502);
  assert.equal((await ask(1)).status, 429);
  assert.equal(state.calls, 10);
  assert.equal((await accounting()).count, 10);
  assert.equal((await queued()).length, 0);
});

test("failed and ambiguous queue writes retry from cached metadata without new USGS work", async () => {
  for (const commit of [false, true]) {
    const id = commit ? 2 : 1;
    state.env.BUCKET = wrapBucket({ put: async (key, value, options) => {
      if (key === queueKey(200000 + id)) {
        if (commit) await bucket.put(key, value, options);
        throw new Error("response lost");
      }
      return bucket.put(key, value, options);
    } });
    assert.equal((await ask(id)).status, 503);
    const record = (await accounting()).requests.find(r => r.id === id).record;
    state.env.BUCKET = bucket;
    assert.equal((await ask(id)).status, commit ? 200 : 202);
    assert.deepEqual(await (await bucket.get(queueKey(200000 + id))).json(), record);
  }
  assert.equal(state.calls, 2);
  assert.equal((await accounting()).count, 2);
});

test("malformed counters and caches fail closed without upstream or queue work", async () => {
  for (const value of [null, [], {}, { count: -1 }, { count: "0" }, { count: 0.5 }, { count: 11 },
    { count: 0, requests: [{}] }, { count: 1, requests: null },
    { count: 1, requests: [{ id: 1, token: crypto.randomUUID(), record: { id: 2 } }] }]) {
    await bucket.put(quotaKey(), JSON.stringify(value));
    assert.equal((await ask(1)).status, 503);
  }
  assert.equal(state.calls, 0);
  assert.equal((await queued()).length, 0);
});

test("missing ETags, CAS contention and ambiguous reservations never authorize USGS work", async () => {
  await bucket.put(quotaKey(), JSON.stringify({ count: 0 }));
  state.env.BUCKET = wrapBucket({ get: async key => { const stored = await bucket.get(key); return stored && { size: stored.size, arrayBuffer: () => stored.arrayBuffer() }; } });
  assert.equal((await ask(1)).status, 503);
  state.env.BUCKET = wrapBucket({ put: async () => null });
  assert.equal((await ask(1)).status, 429);
  state.env.BUCKET = wrapBucket({ put: async (key, value, options) => { await bucket.put(key, value, options); throw new Error("response lost"); } });
  assert.equal((await ask(1)).status, 503);
  state.env.BUCKET = bucket;
  assert.equal((await ask(1)).status, 429);
  assert.equal((await accounting()).count, 1);
  assert.equal(state.calls, 0);
});

test("quota is isolated by requester and UTC day, with email fallback normalized", async () => {
  await bucket.put(quotaKey(), JSON.stringify({ count: 10 }));
  assert.equal((await ask(1)).status, 429);
  state.user = { id: "viewer-2", email: "other@example.test" };
  const prior = quotaKey().replace(`${day()}.json`, "2000-01-01.json");
  await bucket.put(prior, JSON.stringify({ count: 10 }));
  assert.equal((await ask(1)).status, 202);
  state.user = { id: null, email: "EMAIL@example.test" };
  assert.equal((await ask(2)).status, 202);
  state.user.email = "email@EXAMPLE.test";
  assert.equal((await ask(2)).status, 200);
  assert.equal(state.calls, 2);
});

test("authentication, same-origin and ID validation precede quota and provider access", async () => {
  assert.equal((await ask(1, { Origin: "https://other.test" })).status, 403);
  for (const id of [0, -1, 1.5, 1e10 + 1, "1", null, []]) assert.equal((await ask(id)).status, 400);
  state.user = null;
  assert.equal((await ask(1)).status, 401);
  assert.equal(state.calls, 0);
  assert.equal((await bucket.list()).objects.length, 0);
});
