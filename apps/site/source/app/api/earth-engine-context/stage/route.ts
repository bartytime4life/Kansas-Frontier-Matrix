import { EARTH_ENGINE_CONTEXT_LAYERS, EARTH_ENGINE_CONTEXT_PREFIX } from "../../../earth-engine-context";
import { EarthEngineContextError, earthEngineBucket, earthEngineDigest, earthEngineFailure, earthEngineOwner, earthEnginePrivateHeaders } from "../../../earth-engine-context-server";

function checkedKey(value: string | null): { key: string; maximum: number; contentType: string } | null {
  if (!value || !value.startsWith(`${EARTH_ENGINE_CONTEXT_PREFIX}/sets/`)) return null;
  const tail = value.slice(`${EARTH_ENGINE_CONTEXT_PREFIX}/sets/`.length);
  const parts = tail.split("/");
  const setId = parts[0];
  if (!/^ks-(?:2024|terrain)-[a-z0-9-]{6,64}$/.test(setId)) return null;
  if (parts.length === 2 && parts[1] === "manifest.json") return { key: value, maximum: 96_000, contentType: "application/json" };
  if (!EARTH_ENGINE_CONTEXT_LAYERS.some((layer) => layer.id === parts[2])) return null;
  if (parts.length === 4 && parts[1] === "indexes" && /^(0|[1-9]\d?)\.json$/.test(parts[3]) && Number(parts[3].slice(0, -5)) <= 18) return { key: value, maximum: 4_000_000, contentType: "application/json" };
  if (parts.length === 6 && parts[1] === "tiles" && /^(0|[1-9]\d?)$/.test(parts[3]) && /^(0|[1-9]\d*)$/.test(parts[4]) && /^(0|[1-9]\d*)\.png$/.test(parts[5])) {
    const z = Number(parts[3]), x = Number(parts[4]), y = Number(parts[5].slice(0, -4));
    if (z <= 18 && x < 2 ** z && y < 2 ** z) return { key: value, maximum: 2_000_000, contentType: "image/png" };
  }
  return null;
}

async function bounded(request: Request, maximum: number) {
  if (!request.body || Number(request.headers.get("content-length") ?? 0) > maximum) throw new EarthEngineContextError("Display file exceeds its size limit.", 413);
  const chunks: Uint8Array[] = []; let length = 0;
  const reader = request.body.getReader();
  for (;;) {
    const { done, value } = await reader.read();
    if (done) break;
    length += value.length;
    if (length > maximum) { await reader.cancel(); throw new EarthEngineContextError("Display file exceeds its size limit.", 413); }
    chunks.push(value);
  }
  if (!length) throw new EarthEngineContextError("Display file is empty.", 400);
  const bytes = new Uint8Array(length); let offset = 0;
  for (const chunk of chunks) { bytes.set(chunk, offset); offset += chunk.length; }
  return bytes.buffer;
}

export async function PUT(request: Request) {
  try {
    await earthEngineOwner();
    if (request.headers.get("origin") !== new URL(request.url).origin) throw new EarthEngineContextError("Open the installer on this Site.", 403);
    const checked = checkedKey(new URL(request.url).searchParams.get("key"));
    if (!checked) throw new EarthEngineContextError("Display file path is not allowed.", 400);
    if (request.headers.get("content-type")?.split(";")[0] !== checked.contentType) throw new EarthEngineContextError("Unexpected display file type.", 415);
    const expected = request.headers.get("x-kfm-ee-sha256");
    if (!expected || !/^[0-9a-f]{64}$/.test(expected)) throw new EarthEngineContextError("Missing display file hash.", 400);
    const payload = await bounded(request, checked.maximum);
    if (await earthEngineDigest(payload) !== expected) throw new EarthEngineContextError("Display file hash mismatch.", 400);
    const bucket = earthEngineBucket();
    const prior = await bucket.get(checked.key);
    if (prior) {
      if (prior.size !== payload.byteLength || await earthEngineDigest(await prior.arrayBuffer()) !== expected) throw new EarthEngineContextError("Immutable display file already exists with different bytes.", 409);
    } else {
      await bucket.put(checked.key, payload, { httpMetadata: { contentType: checked.contentType } });
    }
    const stored = await bucket.get(checked.key);
    if (!stored || stored.size !== payload.byteLength || await earthEngineDigest(await stored.arrayBuffer()) !== expected) throw new EarthEngineContextError("Display file readback failed.", 503);
    return Response.json({ stored: true, key: checked.key, sha256: expected }, { headers: earthEnginePrivateHeaders });
  } catch (error) { return earthEngineFailure(error); }
}
