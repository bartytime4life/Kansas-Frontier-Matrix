import { env } from "cloudflare:workers";
import { getChatGPTUser } from "./chatgpt-auth";
import {
  EARTH_ENGINE_CONTEXT_ACTIVE_KEY,
  earthEngineIndexKey,
  earthEngineManifestKey,
  earthEngineTileKey,
  parseEarthEngineManifest,
  parseEarthEnginePointer,
  parseEarthEngineTileIndex,
  type EarthEngineContextManifest,
} from "./earth-engine-context";

type ObjectBody = { size: number; arrayBuffer(): Promise<ArrayBuffer> };
export type EarthEngineBucket = {
  get(key: string): Promise<ObjectBody | null>;
  put(key: string, value: ArrayBuffer, options?: { httpMetadata?: { contentType: string } }): Promise<unknown>;
  list(options: { prefix: string; cursor?: string; limit: number }): Promise<{ objects: { key: string }[]; truncated: boolean; cursor?: string }>;
};
export class EarthEngineContextError extends Error { constructor(message: string, readonly status: number) { super(message); } }
export const earthEnginePrivateHeaders = { "Cache-Control": "private, no-store", "X-Content-Type-Options": "nosniff", "Vary": "Cookie" };

export async function earthEngineOwner() {
  const user = await getChatGPTUser();
  if (!user) throw new EarthEngineContextError("Sign in to view Earth Engine context.", 401);
  const ids = String(env.KFM_EARTH_ENGINE_OWNER_IDS ?? "").split(",").map((id) => id.trim()).filter(Boolean);
  const emails = String(env.KFM_EARTH_ENGINE_OWNER_EMAILS ?? "").split(",").map((email) => email.trim().toLowerCase()).filter(Boolean);
  if (!ids.length && !emails.length) throw new EarthEngineContextError("Earth Engine context is not configured.", 503);
  if (!(user.id && ids.includes(user.id)) && !emails.includes(user.email.toLowerCase())) throw new EarthEngineContextError("Earth Engine context is unavailable.", 403);
}

export function earthEngineBucket(): EarthEngineBucket {
  const value = env.BUCKET as EarthEngineBucket | undefined;
  if (!value) throw new EarthEngineContextError("Earth Engine context storage is unavailable.", 503);
  return value;
}

async function bytes(key: string, maximum: number): Promise<ArrayBuffer | null> {
  const object = await earthEngineBucket().get(key);
  if (!object) return null;
  if (!Number.isInteger(object.size) || object.size < 1 || object.size > maximum) throw new EarthEngineContextError("Earth Engine context object failed validation.", 503);
  const result = await object.arrayBuffer();
  if (result.byteLength !== object.size) throw new EarthEngineContextError("Earth Engine context object failed validation.", 503);
  return result;
}

export async function earthEngineDigest(value: ArrayBuffer) {
  return Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256", value)), (part) => part.toString(16).padStart(2, "0")).join("");
}

function json(value: ArrayBuffer): unknown {
  try { return JSON.parse(new TextDecoder("utf-8", { fatal: true }).decode(value)); }
  catch { throw new EarthEngineContextError("Earth Engine context metadata failed validation.", 503); }
}

export async function activeEarthEngineManifest(): Promise<EarthEngineContextManifest | null> {
  const pointerBytes = await bytes(EARTH_ENGINE_CONTEXT_ACTIVE_KEY, 2048);
  if (!pointerBytes) return null;
  const pointer = parseEarthEnginePointer(json(pointerBytes));
  if (!pointer) throw new EarthEngineContextError("Earth Engine context pointer failed validation.", 503);
  return earthEngineManifestForPointer(pointer);
}

export async function earthEngineManifestForPointer(pointer: { setId: string; manifestSha256: string }): Promise<EarthEngineContextManifest> {
  const manifestBytes = await bytes(earthEngineManifestKey(pointer.setId), 96_000);
  if (!manifestBytes || await earthEngineDigest(manifestBytes) !== pointer.manifestSha256) throw new EarthEngineContextError("Earth Engine context manifest failed validation.", 503);
  const manifest = parseEarthEngineManifest(json(manifestBytes));
  if (!manifest || manifest.setId !== pointer.setId) throw new EarthEngineContextError("Earth Engine context manifest failed validation.", 503);
  return manifest;
}

export async function earthEngineTile(setId: string, layerId: string, zText: string, xText: string, yFile: string): Promise<ArrayBuffer | null> {
  const manifest = await activeEarthEngineManifest();
  if (!manifest || manifest.setId !== setId) return null;
  if (!/^(0|[1-9]\d*)$/.test(zText) || !/^(0|[1-9]\d*)$/.test(xText) || !/^(0|[1-9]\d*)\.png$/.test(yFile)) return null;
  const z = Number(zText), x = Number(xText), y = Number(yFile.slice(0, -4));
  if (!Number.isSafeInteger(z) || z > 18 || !Number.isSafeInteger(x) || !Number.isSafeInteger(y) || x >= 2 ** z || y >= 2 ** z) return null;
  const layer = manifest.layers.find((entry) => entry.id === layerId && entry.status === "approved");
  const indexRecord = layer?.tileIndexes[String(z)];
  if (!indexRecord || x < indexRecord.minX || x > indexRecord.maxX || y < indexRecord.minY || y > indexRecord.maxY) return null;
  const index = await earthEngineReadIndex(setId, layerId, z, indexRecord);
  const expectedHash = index[`${x}/${y}`];
  if (!expectedHash) return null;
  const tile = await bytes(earthEngineTileKey(setId, layerId, z, x, y), 2_000_000);
  if (!tile) return null;
  const signature = [137, 80, 78, 71, 13, 10, 26, 10];
  const octets = new Uint8Array(tile);
  if (octets.length < 24 || !signature.every((byte, i) => octets[i] === byte) || await earthEngineDigest(tile) !== expectedHash) throw new EarthEngineContextError("Earth Engine tile failed validation.", 503);
  return tile;
}

export async function earthEngineReadIndex(setId: string, layerId: string, z: number, expected: Parameters<typeof parseEarthEngineTileIndex>[1]) {
  const indexBytes = await bytes(earthEngineIndexKey(setId, layerId, z), 4_000_000);
  if (!indexBytes || await earthEngineDigest(indexBytes) !== expected.sha256) throw new EarthEngineContextError("Earth Engine tile index failed validation.", 503);
  const index = parseEarthEngineTileIndex(json(indexBytes), expected, z);
  if (!index) throw new EarthEngineContextError("Earth Engine tile index failed validation.", 503);
  return index;
}

export function earthEngineFailure(error: unknown): Response {
  if (error instanceof EarthEngineContextError) return Response.json({ error: error.message }, { status: error.status, headers: earthEnginePrivateHeaders });
  console.error("KFM_EARTH_ENGINE_CONTEXT_FAILED", error instanceof Error ? error.name : "Unknown error");
  return Response.json({ error: "Earth Engine context is temporarily unavailable." }, { status: 503, headers: earthEnginePrivateHeaders });
}
