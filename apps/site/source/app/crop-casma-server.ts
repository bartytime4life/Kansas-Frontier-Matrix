import { env } from "cloudflare:workers";
import { getRawDb } from "../db";

type Statement = { first<T>(): Promise<T | null> };
type Db = { prepare(sql: string): Statement };
type ObjectBody = { size: number; arrayBuffer(): Promise<ArrayBuffer> };
type Bucket = { get(key: string): Promise<ObjectBody | null> };
type Row = Record<string, unknown> & { package_id: string; day: string; manifest_key: string; source_sha256: string };
type Tile = { z: number; x: number; y: number; bytes: number; sha256: string };
type Manifest = { profile: string; candidate_id: string; day: string; layer: string; source_sha256: string;
  state: string; release_state: string; source_crs: string; tile_crs: string; source_resolution_m: number;
  numeric_unit: string; numeric_resampling: string; color_interpolation: string; source_nodata: number;
  bounds_wgs84: number[]; zooms: number[]; tiles: Tile[]; valid_cells: number; min: number; max: number;
  coverage_state: string; coverage_checkpoints_m3_m3: Record<string, number | null> };
const DIGEST = /^sha256:[a-f0-9]{64}$/;
const REF = /^kfm:\/\/[A-Za-z0-9._~:/-]{1,240}$/;
const HEADERS = { "Cache-Control": "private, no-store", "X-Content-Type-Options": "nosniff", "Vary": "Cookie" };
const MANIFEST_LIMIT = 128 * 1024, TILE_LIMIT = 1024 * 1024;

function canonical(value: unknown): string {
  if (value === null || typeof value === "string" || typeof value === "boolean" || typeof value === "number" && Number.isFinite(value)) return JSON.stringify(value);
  if (Array.isArray(value)) return `[${value.map(canonical).join(",")}]`;
  if (!value || typeof value !== "object") throw new Error("INVALID_MANIFEST");
  const data = value as Record<string, unknown>;
  return `{${Object.keys(data).sort().map(key => `${JSON.stringify(key)}:${canonical(data[key])}`).join(",")}}`;
}
async function digest(bytes: Uint8Array) {
  return "sha256:" + Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256", Uint8Array.from(bytes).buffer)), b => b.toString(16).padStart(2, "0")).join("");
}
function validRow(row: Row | null): row is Row {
  if (!row || row.state !== "APPROVED" || !DIGEST.test(row.package_id) || !DIGEST.test(row.source_sha256) ||
      row.manifest_key !== `crop-casma/v1/objects/${row.package_id.slice(7)}/manifest.json` ||
      !/^20\d{2}-\d\d-\d\d$/.test(row.day) ||
      !row.reviewer_key || !row.releaser_key || row.reviewer_key === row.releaser_key) return false;
  for (const key of ["source_admission_ref", "rights_ref", "sensitivity_ref", "policy_ref", "review_ref", "release_ref"]) if (typeof row[key] !== "string" || !REF.test(row[key])) return false;
  const reviewed = Date.parse(String(row.reviewed_at)), released = Date.parse(String(row.released_at));
  return Number.isFinite(reviewed) && Number.isFinite(released) && reviewed <= released && released <= Date.now();
}
function tileQuery(request: Request): { day: string; z: number; x: number; y: number } {
  const url = new URL(request.url), fields = [...url.searchParams.entries()];
  if (url.search.length > 100 || fields.length !== 4 || fields.some(([key]) => !["day", "z", "x", "y"].includes(key)) || new Set(fields.map(([key]) => key)).size !== 4) throw new Error("INVALID_TILE_REQUEST");
  const day = url.searchParams.get("day") ?? "";
  const numbers = ["z", "x", "y"].map(key => url.searchParams.get(key) ?? "");
  if (!/^20\d{2}-\d\d-\d\d$/.test(day) || numbers.some(value => !/^\d+$/.test(value))) throw new Error("INVALID_TILE_REQUEST");
  const [z, x, y] = numbers.map(Number), n = 2 ** z;
  if (![z, x, y].every(Number.isSafeInteger) || z < 4 || z > 9 || x >= n || y >= n) throw new Error("INVALID_TILE_REQUEST");
  return { day, z, x, y };
}
async function manifestFor(row: Row, bucket: Bucket): Promise<Manifest> {
  const stored = await bucket.get(row.manifest_key);
  if (!stored || !Number.isSafeInteger(stored.size) || stored.size < 100 || stored.size > MANIFEST_LIMIT) throw new Error("MANIFEST_MISSING");
  const bytes = new Uint8Array(await stored.arrayBuffer());
  if (bytes.length !== stored.size) throw new Error("MANIFEST_SIZE");
  let raw: unknown;
  try { raw = JSON.parse(new TextDecoder("utf-8", { fatal: true }).decode(bytes)); } catch { throw new Error("MANIFEST_JSON"); }
  if (!raw || typeof raw !== "object" || Array.isArray(raw)) throw new Error("MANIFEST_SHAPE");
  const value = raw as Record<string, unknown>;
  const { candidate_id: _id, ...unsigned } = value;
  if (await digest(new TextEncoder().encode(canonical(unsigned))) !== row.package_id || value.candidate_id !== row.package_id) throw new Error("MANIFEST_DIGEST");
  const data = value as Manifest;
  if (data.profile !== "kfm.crop-casma-tiles/v1" || data.state !== "PREPARED_CANDIDATE" || data.release_state !== "UNRELEASED" ||
      data.day !== row.day || data.layer !== `SMAP-HYB-1KM-DAILY_${row.day.slice(0,4)}.${row.day.slice(5,7)}.${row.day.slice(8)}_PM` || data.source_sha256 !== row.source_sha256 || data.source_crs !== "EPSG:5070" || data.tile_crs !== "EPSG:3857" ||
      data.source_resolution_m !== 1000 || data.source_nodata !== -9999 || data.numeric_unit !== "m3/m3" ||
      data.numeric_resampling !== "nearest" || data.color_interpolation !== "palette only" ||
      !Array.isArray(data.bounds_wgs84) || canonical(data.bounds_wgs84) !== "[-102.1,36.95,-94.55,40.05]" ||
      !Array.isArray(data.zooms) || canonical(data.zooms) !== "[4,9]" ||
      !Array.isArray(data.tiles) || data.tiles.length < 1 || data.tiles.length > 160 ||
      !Number.isSafeInteger(data.valid_cells) || data.valid_cells < 1 ||
      !["PARTIAL_AT_CHECKPOINTS", "SAMPLED_ONLY"].includes(data.coverage_state) ||
      !data.coverage_checkpoints_m3_m3 || Object.keys(data.coverage_checkpoints_m3_m3).sort().join(",") !== "Dodge City,Kansas City,Salina,Topeka,Wichita" ||
      Object.values(data.coverage_checkpoints_m3_m3).some(value => value !== null && (!Number.isFinite(value) || value < 0 || value > 1)) ||
      (data.coverage_state === "PARTIAL_AT_CHECKPOINTS") !== Object.values(data.coverage_checkpoints_m3_m3).some(value => value === null) ||
      !Number.isFinite(data.min) || !Number.isFinite(data.max) || data.min < 0 || data.max > 1 || data.min > data.max) throw new Error("MANIFEST_SCOPE");
  const seen = new Set<string>();
  for (const tile of data.tiles) {
    const n = 2 ** tile.z, key = `${tile.z}/${tile.x}/${tile.y}`;
    if (![tile.z, tile.x, tile.y, tile.bytes].every(Number.isSafeInteger) || tile.z < 4 || tile.z > 9 || tile.x < 0 || tile.x >= n || tile.y < 0 || tile.y >= n || tile.bytes < 33 || tile.bytes > TILE_LIMIT || !DIGEST.test(tile.sha256) || seen.has(key)) throw new Error("MANIFEST_TILES");
    seen.add(key);
  }
  return data;
}

export async function readCropCasma(request: Request, view: "availability" | "tile", db: Db, bucket: Bucket): Promise<Response> {
  try {
    const coords = view === "tile" ? tileQuery(request) : null;
    if (view === "availability" && new URL(request.url).search) return Response.json({ state: "error", code: "INVALID_QUERY" }, { status: 400, headers: HEADERS });
    const row = await db.prepare("SELECT p.* FROM crop_casma_active a JOIN crop_casma_packages p ON p.package_id = a.package_id WHERE a.singleton = 1").first<Row>();
    if (!row || !validRow(row)) return Response.json({ state: "held", code: "NO_APPROVED_SOIL_PACKAGE" }, { headers: HEADERS });
    if (coords && coords.day !== row.day) return Response.json({ state: "held", code: "DAY_NOT_ACTIVE" }, { status: 404, headers: HEADERS });
    const manifest = await manifestFor(row, bucket);
    if (!coords) return Response.json({ state: "available", day: row.day, packageId: row.package_id,
      source: "USDA NASS Crop-CASMA SMAP Hybrid 1 km", unit: "m3/m3", nativeResolutionMeters: 1000,
      validCells: manifest.valid_cells, dataMin: manifest.min, dataMax: manifest.max, tileCount: manifest.tiles.length,
      coverageState: manifest.coverage_state, coverageCheckpoints: manifest.coverage_checkpoints_m3_m3,
      sourceUrl: "https://nassgeo.csiss.gmu.edu/Crop-CASMA-Developer/wcs/SMAP-HYB-1KM/",
      reviewedAt: row.reviewed_at, releasedAt: row.released_at }, { headers: HEADERS });
    const tile = manifest.tiles.find(item => item.z === coords.z && item.x === coords.x && item.y === coords.y);
    if (!tile) return Response.json({ state: "unavailable", code: "TILE_OUTSIDE_CAPTURE" }, { status: 404, headers: HEADERS });
    const stored = await bucket.get(`crop-casma/v1/objects/${row.package_id.slice(7)}/tiles/${coords.z}/${coords.x}/${coords.y}.png`);
    if (!stored || stored.size !== tile.bytes || stored.size > TILE_LIMIT) throw new Error("TILE_MISSING");
    const bytes = new Uint8Array(await stored.arrayBuffer());
    const header = new DataView(bytes.buffer, bytes.byteOffset, bytes.byteLength);
    if (bytes.length !== tile.bytes || await digest(bytes) !== tile.sha256 || bytes.length < 33 ||
        ![137,80,78,71,13,10,26,10].every((value, index) => bytes[index] === value) ||
        header.getUint32(16) !== 256 || header.getUint32(20) !== 256) throw new Error("TILE_TAMPERED");
    return new Response(Uint8Array.from(bytes).buffer, { headers: { "Content-Type": "image/png", "Cache-Control": "private, max-age=600", "X-Content-Type-Options": "nosniff" } });
  } catch (error) {
    const invalid = error instanceof Error && error.message === "INVALID_TILE_REQUEST";
    console.info(JSON.stringify({ event: "crop_casma_read", outcome: invalid ? "INVALID_QUERY" : "STORAGE_UNAVAILABLE" }));
    return Response.json({ state: "error", code: invalid ? "INVALID_TILE_REQUEST" : "STORAGE_UNAVAILABLE" }, { status: invalid ? 400 : 503, headers: HEADERS });
  }
}

export async function cropCasmaRead(request: Request, view: "availability" | "tile") {
  try {
    const bucket = env.BUCKET as Bucket | undefined;
    if (!bucket) throw new Error("BUCKET_MISSING");
    return await readCropCasma(request, view, getRawDb(), bucket);
  } catch {
    return Response.json({ state: "error", code: "STORAGE_UNAVAILABLE" }, { status: 503, headers: HEADERS });
  }
}
