import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { createHash } from "node:crypto";
import test from "node:test";
import ts from "typescript";
const source = (await readFile(new URL("../app/crop-casma-server.ts", import.meta.url), "utf8"))
  .replace('import { env } from "cloudflare:workers";', "const env = {};")
  .replace('import { getRawDb } from "../db";', "const getRawDb = () => null;");
const js = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const { readCropCasma } = await import("data:text/javascript;base64," + Buffer.from(js).toString("base64"));
const sha = bytes => "sha256:" + createHash("sha256").update(bytes).digest("hex");
function canonical(value) { if (value === null || typeof value !== "object") return JSON.stringify(value); if (Array.isArray(value)) return `[${value.map(canonical).join(",")}]`; return `{${Object.keys(value).sort().map(key => `${JSON.stringify(key)}:${canonical(value[key])}`).join(",")}}`; }
const png = Buffer.alloc(33); Buffer.from([137,80,78,71,13,10,26,10]).copy(png); png.writeUInt32BE(256,16); png.writeUInt32BE(256,20);
const unsigned = { profile: "kfm.crop-casma-tiles/v1", state: "PREPARED_CANDIDATE", release_state: "UNRELEASED", source_crs: "EPSG:5070", tile_crs: "EPSG:3857", day: "2026-09-28", layer: "SMAP-HYB-1KM-DAILY_2026.09.28_PM", source_sha256: "sha256:" + "a".repeat(64), source_resolution_m: 1000, source_nodata: -9999, numeric_unit: "m3/m3", numeric_resampling: "nearest", color_interpolation: "palette only", bounds_wgs84: [-102.1,36.95,-94.55,40.05], zooms: [4,9], valid_cells: 149102, min: 0.02, max: 0.33, coverage_state: "PARTIAL_AT_CHECKPOINTS", coverage_checkpoints_m3_m3: { "Dodge City": 0.12, "Wichita": 0.18, "Salina": 0.25, "Topeka": null, "Kansas City": null }, tiles: [{ z: 8, x: 57, y: 98, bytes: 33, sha256: sha(png) }] };
const id = sha(canonical(unsigned));
let manifestBytes = Buffer.from(JSON.stringify({ ...unsigned, candidate_id: id }));
let tileBytes = png;
let active = { package_id: id, day: "2026-09-28", manifest_key: `crop-casma/v1/objects/${id.slice(7)}/manifest.json`, source_sha256: unsigned.source_sha256, state: "APPROVED", reviewer_key: "one", releaser_key: "two", reviewed_at: "2026-09-29T00:00:00Z", released_at: "2026-09-30T00:00:00Z", source_admission_ref: "kfm://admission/one", rights_ref: "kfm://rights/one", sensitivity_ref: "kfm://sensitivity/one", policy_ref: "kfm://policy/one", review_ref: "kfm://review/one", release_ref: "kfm://release/one" };
const db = { prepare: () => ({ first: async () => active }) };
const bucket = { get: async key => {
  const bytes = key.endsWith("manifest.json") ? manifestBytes : key.endsWith("tiles/8/57/98.png") ? tileBytes : null;
  return bytes ? { size: bytes.length, arrayBuffer: async () => Uint8Array.from(bytes).buffer } : null;
} };
const read = (view, query = "") => readCropCasma(new Request(`https://example.test/api/crop-casma/${view}${query}`), view, db, bucket);

test("Python integral-float candidate identity verifies after JSON parsing", async () => {
  const sample = JSON.parse('{"min":0.0,"max":1.0,"points":[0.0,0.25],"source_nodata":-9999}');
  assert.equal(sha(canonical(sample)), "sha256:766a276fe639d4e6195e13f12ad3f886314ed0f424709d95aef745aa11005f21");
  const withZero = { ...unsigned, min: 0, coverage_checkpoints_m3_m3: { ...unsigned.coverage_checkpoints_m3_m3, Wichita: 0 } };
  const zeroId = sha(canonical(withZero));
  try {
    active = { ...activeRow, package_id: zeroId, manifest_key: `crop-casma/v1/objects/${zeroId.slice(7)}/manifest.json` };
    manifestBytes = Buffer.from(JSON.stringify({ ...withZero, candidate_id: zeroId }).replace('"min":0', '"min":0.0').replace('"Wichita":0', '"Wichita":0.0'));
    assert.equal((await (await read("availability")).json()).state, "available");
  } finally { active = activeRow; manifestBytes = Buffer.from(JSON.stringify({ ...unsigned, candidate_id: id })); }
});

test("approved exact-day source exposes validated availability and tile", async () => {
  const availability = await (await read("availability")).json();
  assert.equal(availability.state, "available");
  assert.equal(availability.nativeResolutionMeters, 1000);
  const tile = await read("tile", "?day=2026-09-28&z=8&x=57&y=98");
  assert.equal(tile.status, 200);
  assert.equal(tile.headers.get("content-type"), "image/png");
});
test("missing approval, wrong day, invalid coordinates and storage tampering fail safely", async () => {
  try {
    active = null;
    assert.equal((await (await read("availability")).json()).state, "held");
    active = { ...activeRow, state: "WITHDRAWN" };
    assert.equal((await (await read("availability")).json()).state, "held");
    active = activeRow;
    assert.equal((await read("tile", "?day=2026-09-27&z=8&x=57&y=98")).status, 404);
    assert.equal((await read("tile", "?day=2026-09-28&z=8&x=57&y=98&x=1")).status, 400);
    manifestBytes = Buffer.from("tampered".repeat(50));
    assert.equal((await read("availability")).status, 503);
    manifestBytes = Buffer.from(JSON.stringify({ ...unsigned, candidate_id: id }));
    tileBytes = Buffer.from("tampered");
    assert.equal((await read("tile", "?day=2026-09-28&z=8&x=57&y=98")).status, 503);
  } finally { active = activeRow; manifestBytes = Buffer.from(JSON.stringify({ ...unsigned, candidate_id: id })); tileBytes = png; }
});
const activeRow = active;
