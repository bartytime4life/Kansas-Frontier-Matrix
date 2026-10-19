import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const dataUrl = (source, name) => `data:text/javascript;base64,${Buffer.from(ts.transpileModule(source, {
  compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 }, fileName: name,
}).outputText).toString("base64")}`;
const overlay = dataUrl(await readFile(new URL("../app/historical-topo-overlay.ts", import.meta.url), "utf8"), "historical-topo-overlay.ts");
const server = dataUrl(`
  export class TopoOverlayError extends Error { constructor(message, status = 400) { super(message); this.status = status; } }
  export const topoBucket = () => globalThis.__topo.bucket;
  export const topoBytes = async (key, max) => { const value = globalThis.__topo.objects.get(key); if (!value) return null; if (value.byteLength > max) throw new TopoOverlayError("too large", 503); return value.buffer.slice(value.byteOffset, value.byteOffset + value.byteLength); };
  export const topoDigest = async (bytes) => [...new Uint8Array(await crypto.subtle.digest("SHA-256", bytes))].map(n => n.toString(16).padStart(2, "0")).join("");
  export const topoJson = bytes => JSON.parse(new TextDecoder().decode(bytes));
  export const topoScanId = raw => { if (!/^[1-9]\\d{0,9}$/.test(String(raw))) throw new TopoOverlayError("invalid scan"); return Number(raw); };
  export const topoWorker = request => { if (request.headers.get("authorization") !== "Bearer worker-secret") throw new TopoOverlayError("worker denied", 403); };
  export const topoOwner = async () => { if (!globalThis.__topo.owner) throw new TopoOverlayError("owner denied", 403); return { id: "owner-1", email: "owner@example.test" }; };
  export const topoUser = async () => ({ id: "viewer-1", email: "viewer@example.test" });
  export const topoSameOrigin = request => { if (request.headers.get("origin") !== new URL(request.url).origin) throw new TopoOverlayError("origin denied", 403); };
  export const topoPrivateHeaders = { "Cache-Control": "private, no-store" };
  export const topoActive = async scan => { const bytes = await topoBytes("historical-topo/v1/active/" + scan + ".json", 2048); if (!bytes) return null; const pointer = topoJson(bytes); const manifestBytes = await topoBytes("historical-topo/v1/packages/" + scan + "/" + pointer.packageId + "/manifest.json", 750000); if (!manifestBytes || await topoDigest(manifestBytes) !== pointer.manifestSha256) throw new TopoOverlayError("bad active manifest", 503); return { pointer, manifest: topoJson(manifestBytes) }; };
  export const topoFailure = error => Response.json({ error: error.message }, { status: error.status ?? 503 });
`, "topo-server-stub.ts");
async function route(name) {
  let source = await readFile(new URL(`../app/api/historical-topo/${name}/route.ts`, import.meta.url), "utf8");
  source = source.replaceAll(/"(?:\.\.\/)+historical-topo-overlay"/g, JSON.stringify(overlay));
  source = source.replaceAll(/"(?:\.\.\/)+historical-topo-overlay-server"/g, JSON.stringify(server));
  return import(dataUrl(source, name));
}
const digest = value => createHash("sha256").update(value).digest("hex");
const scan = 122705;
const requestRecord = { id: 4628, scanId: scan, name: "Topeka", year: 1889, scale: 125000, state: "KS" };
const png = Buffer.concat([Buffer.from([137, 80, 78, 71, 13, 10, 26, 10]), Buffer.alloc(24, 7)]);
const manifestFor = (letter) => {
  const sha = letter.repeat(64);
  return { version: 1, packageId: sha.slice(0, 24), sheet: requestRecord,
    geotiff: { url: "https://prd-tnm.s3.amazonaws.com/StagedProducts/Maps/HistoricalTopo/GeoTIFF/KS/KS_Topeka_122705_1889_125000_geo.tif", sha256: sha, bytes: 5372903, crs: "EPSG:4326", transform: [0, 10, 0, 0, 0, -10], width: 500, height: 500 },
    bounds: [-96, 39, -95.5, 39.5], minZoom: 9, maxZoom: 14, sourceRetrievedAt: "2026-09-30T00:00:00Z",
    tiles: { "9/119/195": { sha256: digest(png), bytes: png.byteLength } }, evidenceRole: "EXTERNAL_CONTEXT_ONLY" };
};
const key = (packageId, address) => `historical-topo/v1/packages/${scan}/${packageId}/${address}`;
const stageRequest = (packageId, address, body) => new Request(`https://site.test/api/historical-topo/stage?scan=${scan}&package=${packageId}&address=${address}`, {
  method: "PUT", headers: { Authorization: "Bearer worker-secret", "Content-Type": address === "manifest" ? "application/json" : "image/png", "Content-Length": String(body.byteLength), "X-KFM-SHA256": digest(body) }, body,
});
const activateRequest = (body) => new Request("https://site.test/api/historical-topo/activate", { method: "POST",
  headers: { Origin: "https://site.test", "Content-Type": "application/json" }, body: JSON.stringify(body) });

test("staging is immutable and an interrupted manifest rerun restores owner review", async () => {
  const objects = new Map([[`historical-topo/v1/requests/${scan}.json`, Buffer.from(JSON.stringify(requestRecord))]]);
  globalThis.__topo = { objects, owner: true, bucket: {
    get: async key => { const value = objects.get(key); return value ? { size: value.byteLength, arrayBuffer: async () => value.buffer.slice(value.byteOffset, value.byteOffset + value.byteLength) } : null; },
    put: async (key, value) => { objects.set(key, Buffer.from(value)); },
    list: async ({ prefix }) => ({ objects: [...objects.keys()].filter(key => key.startsWith(prefix)).map(key => ({ key })), truncated: false }),
  } };
  const { PUT } = await route("stage");
  const { POST } = await route("activate");
  const { GET: reviewGet } = await route("review");
  const { GET: tileGet } = await route("tiles/[scan]/[package]/[z]/[x]/[y]");
  const first = manifestFor("a");
  const manifestBytes = Buffer.from(JSON.stringify(first));
  const review = { scanId: scan, packageId: first.packageId, manifestSha256: digest(manifestBytes), note: "Checked source and placement" };
  assert.equal((await PUT(stageRequest(first.packageId, "manifest", manifestBytes))).status, 201);
  objects.delete(`historical-topo/v1/candidates/${scan}.json`);
  assert.equal((await PUT(stageRequest(first.packageId, "manifest", manifestBytes))).status, 200);
  assert.ok(objects.has(`historical-topo/v1/candidates/${scan}.json`));
  assert.equal((await POST(activateRequest(review))).status, 409, "a manifest alone cannot activate missing tiles");
  assert.equal((await PUT(stageRequest(first.packageId, "9/119/195", png))).status, 201);
  assert.equal((await POST(activateRequest(review))).status, 200);
  const second = manifestFor("b"), secondBytes = Buffer.from(JSON.stringify(second));
  assert.equal((await PUT(stageRequest(second.packageId, "9/119/195", png))).status, 201);
  assert.equal((await PUT(stageRequest(second.packageId, "manifest", secondBytes))).status, 201);
  assert.equal((await POST(activateRequest({ ...review, packageId: second.packageId, manifestSha256: digest(secondBytes) }))).status, 200);
  assert.equal((await POST(activateRequest({ ...review, rollback: true }))).status, 200);
  const priorReview = await reviewGet(new Request(`https://site.test/api/historical-topo/review?scan=${scan}&mode=previous`));
  assert.equal(priorReview.status, 200);
  assert.equal((await priorReview.json()).packageId, second.packageId);
  const tileContext = packageId => ({ params: Promise.resolve({ scan: String(scan), package: packageId, z: "9", x: "119", y: "195.png" }) });
  assert.equal((await tileGet(new Request("https://site.test/tiles"), tileContext(first.packageId))).status, 200);
  assert.equal((await tileGet(new Request("https://site.test/tiles"), tileContext("c".repeat(24)))).status, 404);
  objects.set(key(first.packageId, "tiles/9/119/195.png"), Buffer.alloc(32, 1));
  assert.equal((await tileGet(new Request("https://site.test/tiles"), tileContext(first.packageId))).status, 503);
  globalThis.__topo.owner = false;
  assert.equal((await POST(activateRequest(review))).status, 403);
  assert.equal((await PUT(new Request(stageRequest(first.packageId, "9/119/195", png), { headers: { "Content-Type": "image/png", "Content-Length": String(png.byteLength), "X-KFM-SHA256": digest(png) } }))).status, 403);
});
