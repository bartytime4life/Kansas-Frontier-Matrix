import { env } from "cloudflare:workers";
import { getChatGPTUser } from "./chatgpt-auth";
import { parseTopoCatalog, TOPO_CATALOG_URL, type TopoSheet } from "./historical-topo";
import { parseTopoActivePointer, parseTopoOverlayManifest, topoActiveKey, topoManifestKey, type TopoActivePointer, type TopoOverlayManifest } from "./historical-topo-overlay";

type Stored = { size: number; arrayBuffer(): Promise<ArrayBuffer> };
export type TopoBucket = { get(key: string): Promise<Stored | null>; put(key: string, value: ArrayBuffer, options?: { httpMetadata?: { contentType: string } }): Promise<unknown>; list(options: { prefix: string; cursor?: string; limit: number }): Promise<{ objects: { key: string }[]; truncated: boolean; cursor?: string }> };
export class TopoOverlayError extends Error { constructor(message: string, readonly status = 400) { super(message); } }
export const topoPrivateHeaders = { "Cache-Control": "private, no-store", "X-Content-Type-Options": "nosniff", "Vary": "Cookie" };
export function topoBucket(): TopoBucket {
  const bucket = env.BUCKET as TopoBucket | undefined;
  if (!bucket) throw new TopoOverlayError("Historical map storage is unavailable.", 503);
  return bucket;
}
export function topoSameOrigin(request: Request) {
  if (request.headers.get("origin") !== new URL(request.url).origin || request.headers.get("sec-fetch-site") === "cross-site") throw new TopoOverlayError("Open this map on the Site.", 403);
}
export async function topoUser() {
  const user = await getChatGPTUser();
  if (!user) throw new TopoOverlayError("Sign in to request a historical map overlay.", 401);
  return user;
}
export async function topoOwner() {
  const user = await topoUser();
  const ids = String(env.KFM_HISTORICAL_OWNER_IDS ?? "").split(",").map((x) => x.trim()).filter(Boolean);
  const emails = String(env.KFM_HISTORICAL_OWNER_EMAILS ?? "").split(",").map((x) => x.trim().toLowerCase()).filter(Boolean);
  if (!ids.length && !emails.length) throw new TopoOverlayError("Historical map review is not configured.", 503);
  if (!(user.id && ids.includes(user.id)) && !emails.includes(user.email.toLowerCase())) throw new TopoOverlayError("Historical map review is unavailable.", 403);
  return user;
}
export function topoWorker(request: Request) {
  const expected = String(env.KFM_HISTORICAL_WORKER_TOKEN ?? "");
  const actual = request.headers.get("authorization")?.replace(/^Bearer /, "") ?? "";
  if (expected.length < 32) throw new TopoOverlayError("Historical map preparation is not configured.", 503);
  const a = new TextEncoder().encode(expected), b = new TextEncoder().encode(actual);
  let mismatch = a.length ^ b.length;
  for (let i = 0; i < a.length; i++) mismatch |= a[i] ^ (b[i] ?? 0);
  if (mismatch) throw new TopoOverlayError("Historical map preparation is unavailable.", 403);
}
export function topoScanId(raw: string | null): number {
  if (!raw || !/^[1-9]\d{0,9}$/.test(raw)) throw new TopoOverlayError("Invalid historical scan ID.");
  return Number(raw);
}
export async function topoBytes(key: string, maximum: number): Promise<ArrayBuffer | null> {
  const value = await topoBucket().get(key);
  if (!value) return null;
  if (!Number.isInteger(value.size) || value.size < 1 || value.size > maximum) throw new TopoOverlayError("Historical map package failed validation.", 503);
  const bytes = await value.arrayBuffer();
  if (bytes.byteLength !== value.size) throw new TopoOverlayError("Historical map package failed validation.", 503);
  return bytes;
}
export async function topoDigest(bytes: ArrayBuffer): Promise<string> {
  return Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256", bytes)), (value) => value.toString(16).padStart(2, "0")).join("");
}
export function topoJson(bytes: ArrayBuffer): unknown {
  try { return JSON.parse(new TextDecoder("utf-8", { fatal: true }).decode(bytes)); }
  catch { throw new TopoOverlayError("Historical map metadata failed validation.", 503); }
}
export async function topoActive(scanId: number): Promise<{ pointer: TopoActivePointer; manifest: TopoOverlayManifest } | null> {
  const bytes = await topoBytes(topoActiveKey(scanId), 2048);
  if (!bytes) return null;
  const pointer = parseTopoActivePointer(topoJson(bytes));
  if (!pointer || pointer.scanId !== scanId) throw new TopoOverlayError("Historical map release pointer failed validation.", 503);
  const manifestBytes = await topoBytes(topoManifestKey(scanId, pointer.packageId), 750_000);
  if (!manifestBytes || await topoDigest(manifestBytes) !== pointer.manifestSha256) throw new TopoOverlayError("Historical map manifest failed validation.", 503);
  const manifest = parseTopoOverlayManifest(topoJson(manifestBytes));
  if (!manifest || manifest.sheet.scanId !== scanId || manifest.packageId !== pointer.packageId) throw new TopoOverlayError("Historical map manifest failed validation.", 503);
  return { pointer, manifest };
}
export async function topoCatalogSheet(id: number): Promise<TopoSheet> {
  if (!Number.isInteger(id) || id < 1 || id > 1e10) throw new TopoOverlayError("Invalid historical sheet ID.");
  const url = new URL(TOPO_CATALOG_URL);
  url.search = new URLSearchParams({ where: `OBJECTID = ${id} AND primary_state = 'KS'`, outFields: "OBJECTID,map_scale,map_name,primary_state,date_on_map,imprint_year,scan_id,series,datum", returnGeometry: "true", outSR: "4326", f: "json" }).toString();
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 12_000);
  try {
    const response = await fetch(url, { cache: "no-store", redirect: "manual", signal: controller.signal, headers: { Accept: "application/json" } });
    if (!response.ok || response.redirected || !response.headers.get("content-type")?.includes("json") || Number(response.headers.get("content-length") ?? 0) > 512_000) throw new Error("USGS catalog unavailable.");
    const bytes = await response.arrayBuffer();
    if (bytes.byteLength > 512_000) throw new Error("USGS catalog response exceeded its limit.");
    const sheets = parseTopoCatalog(topoJson(bytes)).sheets;
    if (sheets.length !== 1 || sheets[0].id !== id) throw new TopoOverlayError("Kansas historical sheet not found.", 404);
    return sheets[0];
  } catch (error) {
    if (error instanceof TopoOverlayError) throw error;
    throw new TopoOverlayError("USGS catalog is temporarily unavailable.", 502);
  } finally { clearTimeout(timeout); }
}
export function topoFailure(error: unknown): Response {
  if (error instanceof TopoOverlayError) return Response.json({ error: error.message }, { status: error.status, headers: topoPrivateHeaders });
  console.error("KFM_HISTORICAL_TOPO_FAILED", error instanceof Error ? error.name : "Unknown error");
  return Response.json({ error: "Historical map overlay is temporarily unavailable." }, { status: 503, headers: topoPrivateHeaders });
}
