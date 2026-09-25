import { EARTH_ENGINE_CONTEXT_ACTIVE_KEY, EARTH_ENGINE_CONTEXT_PREFIX, earthEngineTileKey, parseEarthEnginePointer } from "../../../earth-engine-context";
import { EarthEngineContextError, earthEngineBucket, earthEngineDigest, earthEngineFailure, earthEngineManifestForPointer, earthEngineOwner, earthEnginePrivateHeaders, earthEngineReadIndex } from "../../../earth-engine-context-server";

export async function POST(request: Request) {
  try {
    await earthEngineOwner();
    if (request.headers.get("origin") !== new URL(request.url).origin) throw new EarthEngineContextError("Open the installer on this Site.", 403);
    if (!request.headers.get("content-type")?.startsWith("application/json") || Number(request.headers.get("content-length") ?? 0) > 2048) throw new EarthEngineContextError("Invalid display pointer.", 400);
    const raw = await request.arrayBuffer();
    if (raw.byteLength > 2048) throw new EarthEngineContextError("Invalid display pointer.", 400);
    let value: unknown;
    try { value = JSON.parse(new TextDecoder("utf-8", { fatal: true }).decode(raw)); }
    catch { throw new EarthEngineContextError("Invalid display pointer.", 400); }
    const pointer = parseEarthEnginePointer(value);
    if (!pointer) throw new EarthEngineContextError("Invalid display pointer.", 400);
    const manifest = await earthEngineManifestForPointer(pointer);
    const bucket = earthEngineBucket();
    let tileCount = 0;
    for (const layer of manifest.layers.filter((item) => item.status === "approved")) {
      for (const [zText, record] of Object.entries(layer.tileIndexes)) {
        const z = Number(zText), index = await earthEngineReadIndex(pointer.setId, layer.id, z, record);
        const expected = new Set(Object.keys(index).map((coordinate) => {
          const [x, y] = coordinate.split("/").map(Number);
          return earthEngineTileKey(pointer.setId, layer.id, z, x, y);
        }));
        const prefix = `${EARTH_ENGINE_CONTEXT_PREFIX}/sets/${pointer.setId}/tiles/${layer.id}/${z}/`;
        let cursor: string | undefined, pages = 0;
        for (;;) {
          const page = await bucket.list({ prefix, cursor, limit: 1000 });
          for (const item of page.objects) {
            if (!expected.delete(item.key)) throw new EarthEngineContextError("Unexpected tile in immutable display set.", 409);
          }
          if (!page.truncated) break;
          if (!page.cursor || ++pages > 250) throw new EarthEngineContextError("Tile inventory is incomplete.", 503);
          cursor = page.cursor;
        }
        if (expected.size) throw new EarthEngineContextError("Display set has missing tiles.", 409);
        tileCount += record.count;
      }
    }
    if (!tileCount) throw new EarthEngineContextError("Display set has no approved tiles.", 409);
    // The active pointer is the only mutable object in this separate R2 prefix.
    const prior = await bucket.get(EARTH_ENGINE_CONTEXT_ACTIVE_KEY);
    if (prior && prior.size <= 2048) {
      const previous = await prior.arrayBuffer();
      const archival = `${EARTH_ENGINE_CONTEXT_PREFIX}/history/${Date.now()}-${await earthEngineDigest(previous)}.json`;
      await bucket.put(archival, previous, { httpMetadata: { contentType: "application/json" } });
    }
    await bucket.put(EARTH_ENGINE_CONTEXT_ACTIVE_KEY, raw, { httpMetadata: { contentType: "application/json" } });
    const active = await bucket.get(EARTH_ENGINE_CONTEXT_ACTIVE_KEY);
    if (!active || await earthEngineDigest(await active.arrayBuffer()) !== await earthEngineDigest(raw)) throw new EarthEngineContextError("Active display pointer readback failed.", 503);
    return Response.json({ active: true, setId: pointer.setId, layers: manifest.layers.filter((item) => item.status === "approved").map((item) => item.id), tileCount }, { headers: earthEnginePrivateHeaders });
  } catch (error) { return earthEngineFailure(error); }
}
