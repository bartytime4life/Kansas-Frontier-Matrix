import { ACQUISITION_MAX_BYTES } from "./acquisition-inventory";
import { readBoundedJson } from "./bounded-json";
import { earthEngineBucket, earthEngineDigest, earthEngineFailure, earthEngineOwner, earthEnginePrivateHeaders, EarthEngineContextError } from "./earth-engine-context-server";

const namespaces = {
  inventory: { root: "acquisition/v1", field: "inventory", schema: "kfm-acquisition-pointer-v1" },
  terrain: { root: "acquisition/terrain/v1", field: "discovery", schema: "kfm-acquisition-terrain-pointer-v1" },
} as const;

/** Fixed private metadata namespaces; input values never choose storage keys. */
export function acquisitionReceiptRoutes<T>(kind: keyof typeof namespaces, parse: (value: unknown) => T | null) {
  const config = namespaces[kind];
  const PREFIX = `${config.root}/receipts/`, LATEST = `${config.root}/latest.json`;
  async function GET() {
    try {
      await earthEngineOwner();
      const bucket = earthEngineBucket();
      const pointerObject = await bucket.get(LATEST);
      if (!pointerObject) return Response.json({ [config.field]: null }, { headers: earthEnginePrivateHeaders });
      if (!Number.isSafeInteger(pointerObject.size) || pointerObject.size < 1 || pointerObject.size > 1000) throw new Error("Receipt pointer size");
      const pointerBytes = await pointerObject.arrayBuffer();
      if (pointerBytes.byteLength !== pointerObject.size) throw new Error("Receipt pointer size");
      const pointer = JSON.parse(new TextDecoder("utf-8", { fatal: true }).decode(pointerBytes));
      if (!pointer || typeof pointer !== "object" || Array.isArray(pointer) || pointer.schema !== config.schema
        || Object.keys(pointer).sort().join(",") !== "key,schema,sha256" || typeof pointer.key !== "string" || !pointer.key.startsWith(PREFIX) || !/^\d{13}-[a-f0-9]{64}\.json$/.test(pointer.key.slice(PREFIX.length))
        || typeof pointer.sha256 !== "string" || !/^[a-f0-9]{64}$/.test(pointer.sha256) || pointer.key.slice(-69, -5) !== pointer.sha256) throw new Error("Receipt pointer contract");
      const key = pointer.key;
      const object = await bucket.get(key);
      if (!object || !Number.isSafeInteger(object.size) || object.size > ACQUISITION_MAX_BYTES || object.size < 1) throw new Error("Receipt size");
      const raw = await object.arrayBuffer();
      if (raw.byteLength !== object.size || await earthEngineDigest(raw) !== key.slice(-69, -5)) throw new Error("Receipt digest");
      const inventory = parse(JSON.parse(new TextDecoder("utf-8", { fatal: true }).decode(raw)));
      if (!inventory) throw new Error("Receipt contract");
      return Response.json({ [config.field]: inventory }, { headers: earthEnginePrivateHeaders });
    } catch (error) { return earthEngineFailure(error); }
  }
  async function POST(request: Request) {
    try {
      await earthEngineOwner();
      if (request.headers.get("origin") !== new URL(request.url).origin) throw new EarthEngineContextError("Same-origin receipt import required.", 403);
      if (request.headers.get("content-type")?.split(";")[0] !== "application/json") throw new EarthEngineContextError("JSON receipt required.", 415);
      let inventory;
      try { inventory = parse(await readBoundedJson(request, ACQUISITION_MAX_BYTES, AbortSignal.any([request.signal, AbortSignal.timeout(15_000)]))); }
      catch { throw new EarthEngineContextError("Receipt is invalid, oversized or incomplete.", 400); }
      if (!inventory) throw new EarthEngineContextError("Acquisition receipt failed validation.", 400);
      const raw = new TextEncoder().encode(JSON.stringify(inventory)).buffer;
      if (raw.byteLength > ACQUISITION_MAX_BYTES) throw new EarthEngineContextError("Projected receipt exceeds the metadata limit.", 400);
      const digest = await earthEngineDigest(raw);
      if (request.signal.aborted) throw new EarthEngineContextError("Receipt import was canceled.", 400);
      const key = `${PREFIX}${Date.now()}-${digest}.json`;
      const bucket = earthEngineBucket();
      await bucket.put(key, raw, { httpMetadata: {contentType: "application/json"} });
      const check = await bucket.get(key);
      if (!check || check.size !== raw.byteLength || await earthEngineDigest(await check.arrayBuffer()) !== digest) throw new Error("Receipt readback");
      // Publish only the verified immutable receipt; historical objects are preserved.
      // Concurrent imports use last pointer-write wins. No archive enumeration is needed.
      await bucket.put(LATEST, new TextEncoder().encode(JSON.stringify({ schema: config.schema, key, sha256: digest })).buffer, { httpMetadata: {contentType: "application/json"} });
      return Response.json({ [config.field]: inventory, saved: true, sha256: digest }, { status: 201, headers: earthEnginePrivateHeaders });
    } catch (error) { return earthEngineFailure(error); }
  }

  return { GET, POST };
}
