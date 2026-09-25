import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { readFileSync, readdirSync } from "node:fs";
import path from "node:path";
import test from "node:test";
import { Miniflare, convertV4MiniflareOptions } from "miniflare";
import ts from "typescript";

const hash = (value) => createHash("sha256").update(value).digest("hex");
const json = (value) => Buffer.from(JSON.stringify(value) + "\n");
const source = readFileSync("app/earth-engine-context.ts", "utf8");
const compiled = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const schema = await import(`data:text/javascript;base64,${Buffer.from(compiled).toString("base64")}`);

test("annual snapshots respect the map year while mixed-date terrain remains available", () => {
  assert.equal(schema.earthEngineTileVisibleAtYear("ee-cdl", 2024), true);
  assert.equal(schema.earthEngineTileVisibleAtYear("ee-cdl", 2025), false);
  assert.equal(schema.earthEngineTileVisibleAtYear("ee-3dep", 2025), true);
  assert.equal(schema.earthEngineTileVisibleAtYear("ee-3dep", -1), true);
});

test("owner tile serving requires exact hashed manifest membership and fails closed", async () => {
  const root = path.resolve("dist/server");
  const files = readdirSync(root, { recursive: true }).filter((p) => p.endsWith(".js"));
  const modules = ["index.js", ...files.filter((p) => p !== "index.js")].map((p) => ({ type: "ESModule", path: path.join(root, p) }));
  const mf = new Miniflare(convertV4MiniflareOptions({ modules, modulesRoot: root, compatibilityDate: "2026-08-28", compatibilityFlags: ["nodejs_compat"], r2Buckets: ["BUCKET"], bindings: { KFM_EARTH_ENGINE_OWNER_EMAILS: "owner@example.test" } }));
  try {
    const origin = (await mf.ready).origin;
    const request = async (route, email, init = {}) => {
      const req = new Request(origin + route, { ...init, headers: { ...(email ? { "oai-authenticated-user-email": email } : {}), Origin: origin, ...init.headers } });
      return mf.dispatchFetch(req.url, { method: req.method, headers: Object.fromEntries(req.headers), body: ["GET", "HEAD"].includes(req.method) ? undefined : await req.arrayBuffer() });
    };
    const active = "/api/earth-engine-context/active";
    assert.equal((await request(active)).status, 401);
    assert.equal((await request(active, "other@example.test")).status, 403);
    const empty = await request(active, "owner@example.test");
    assert.equal(empty.status, 200);
    assert.equal((await empty.json()).available, false);

    const setId = "ks-2024-test123";
    const prefix = `earth-engine-context/v1/sets/${setId}`;
    const png = Buffer.from("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQIHWP4z8DwHwAFgAI/ScL/nwAAAABJRU5ErkJggg==", "base64");
    const index = json({ tiles: { "7/12": hash(png) } });
    const manifest = json({ schema: "kfm-earth-engine-context/v1", setId, boundary: "Kansas · TIGER/2018/States · STATEFP 20", approvedAt: "2026-09-25T15:00:00Z", reviewState: "APPROVED_VISUAL_CONTEXT", admission: "NOT_ADMITTED", evidence: "NOT_CLAIM_EVIDENCE", layers: [{ id: "ee-cdl", status: "approved", source: "USDA/NASS/CDL", period: "2024 harvest year", resolutionMeters: 30, attribution: "USDA NASS Cropland Data Layer", limits: "Review only", legend: "Crop classes", geotiffSha256: hash("geotiff"), reviewSha256: hash("review"), tileIndexes: { "5": { sha256: hash(index), count: 1, minX: 7, maxX: 7, minY: 12, maxY: 12 } } }] });
    const pointer = json({ schema: "kfm-earth-engine-context-pointer/v1", setId, manifestSha256: hash(manifest) });
    const stage = (key, bytes, digest = hash(bytes)) => request(`/api/earth-engine-context/stage?key=${encodeURIComponent(key)}`, "owner@example.test", { method: "PUT", headers: { "content-type": key.endsWith(".png") ? "image/png" : "application/json", "x-kfm-ee-sha256": digest }, body: bytes });
    assert.equal((await stage(`${prefix}/manifest.json`, manifest, hash("wrong"))).status, 400);
    assert.equal((await stage("earth-engine-context/v1/sets/../active.json", manifest)).status, 400);
    assert.equal((await stage(`${prefix}/manifest.json`, manifest)).status, 200);
    assert.equal((await stage(`${prefix}/indexes/ee-cdl/5.json`, index)).status, 200);
    const activation = () => request("/api/earth-engine-context/activate", "owner@example.test", { method: "POST", headers: { "content-type": "application/json" }, body: pointer });
    assert.equal((await activation()).status, 409, "a missing indexed tile must block activation");
    assert.equal((await stage(`${prefix}/tiles/ee-cdl/5/7/12.png`, png)).status, 200);
    assert.equal((await activation()).status, 200);
    const tile = `/api/earth-engine-context/${setId}/ee-cdl/5/7/12.png`;
    const served = await request(tile, "owner@example.test");
    assert.equal(served.status, 200, await served.clone().text());
    assert.equal(served.headers.get("content-type"), "image/png");
    assert.equal(served.headers.get("cache-control"), "private, no-store");
    assert.deepEqual(Buffer.from(await served.arrayBuffer()), png);
    assert.equal((await request(tile, "other@example.test")).status, 403);
    assert.equal((await request(`/api/earth-engine-context/${setId}/ee-cdl/5/7/13.png`, "owner@example.test")).status, 404);
    assert.equal((await request(`/api/earth-engine-context/${setId}/ee-cdl/19/7/12.png`, "owner@example.test")).status, 404);
    assert.equal((await request(`/api/earth-engine-context/${setId}/ee-chirps/5/7/12.png`, "owner@example.test")).status, 404);
    const bucket = await mf.getR2Bucket("BUCKET");
    await bucket.delete(`${prefix}/tiles/ee-cdl/5/7/12.png`);
    assert.equal((await request(tile, "owner@example.test")).status, 404, "missing tile stays unavailable");
    await bucket.put(`${prefix}/tiles/ee-cdl/5/7/12.png`, Buffer.from("not a PNG"));
    assert.equal((await request(tile, "owner@example.test")).status, 503, "corrupt tile must fail validation");
  } finally { await mf.dispose(); }
});
