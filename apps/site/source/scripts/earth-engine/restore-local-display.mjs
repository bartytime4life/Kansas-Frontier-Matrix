// Restore an already reviewed display package to a STOPPED loopback preview.
// No network, Earth Engine credentials, hosted storage, or approval writes.
import { readFile, realpath, stat } from "node:fs/promises";
import { createHash } from "node:crypto";
import path from "node:path";
import { Miniflare, convertV4MiniflareOptions } from "miniflare";
import ts from "typescript";
const args = process.argv.slice(2);
const option = name => args[args.indexOf(name) + 1];
if (!args.includes("--package") || !args.includes("--reviewed-set")) throw new Error("Require --package DIR --reviewed-set SET_ID; optionally --persist-to LOCAL_STATE/v3/r2");
const root = await realpath(option("--package"));
const hash = bytes => createHash("sha256").update(bytes).digest("hex");
const source = await readFile(new URL("../../app/earth-engine-context.ts", import.meta.url), "utf8");
const js = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext } }).outputText;
const schema = await import(`data:text/javascript;base64,${Buffer.from(js).toString("base64")}`);
const read = async (key, max) => {
  const file = await realpath(path.join(root, key));
  if (!file.startsWith(root + path.sep) || (await stat(file)).size > max) throw new Error("Invalid package path or size");
  return readFile(file);
};
const pointerKey = schema.EARTH_ENGINE_CONTEXT_ACTIVE_KEY;
const pointerBytes = await read(pointerKey, 2048), pointer = schema.parseEarthEnginePointer(JSON.parse(pointerBytes));
if (!pointer || pointer.setId !== option("--reviewed-set") || schema.earthEngineSetYear(pointer) !== 2024) throw new Error("Exact reviewed 2024 restoration identity required");
const manifestKey = schema.earthEngineManifestKey(pointer.setId), manifestBytes = await read(manifestKey, 96000);
const manifest = schema.parseEarthEngineManifest(JSON.parse(manifestBytes));
if (!manifest || manifest.setId !== pointer.setId || hash(manifestBytes) !== pointer.manifestSha256) throw new Error("Manifest failed integrity or review contract");
const objects = [{ key: manifestKey, sha256: hash(manifestBytes), max: 96000 }];
for (const layer of manifest.layers) for (const [zText, expected] of Object.entries(layer.tileIndexes)) {
  const z = Number(zText), key = schema.earthEngineIndexKey(pointer.setId, layer.id, z), bytes = await read(key, 4_000_000);
  const index = schema.parseEarthEngineTileIndex(JSON.parse(bytes), expected, z);
  if (!index || hash(bytes) !== expected.sha256) throw new Error("Tile index failed integrity");
  objects.push({ key, sha256: expected.sha256, max: 4_000_000 });
  for (const [xy, digest] of Object.entries(index)) {
    const [x, y] = xy.split("/").map(Number);
    objects.push({ key: schema.earthEngineTileKey(pointer.setId, layer.id, z, x, y), sha256: digest, max: 2_000_000 });
  }
}
if (objects.length > 100_000) throw new Error("Restoration exceeds local object budget");
for (const object of objects) {
  const bytes = await read(object.key, object.max);
  if (hash(bytes) !== object.sha256 || object.key.endsWith(".png") && !bytes.subarray(0, 8).equals(Buffer.from([137,80,78,71,13,10,26,10]))) throw new Error("Package object failed integrity");
}
console.log(JSON.stringify({ setId: pointer.setId, manifestSha256: pointer.manifestSha256, verifiedObjects: objects.length, reviewState: manifest.reviewState }));
if (args.includes("--persist-to")) {
  const persistence = path.resolve(option("--persist-to"));
  if (!persistence.endsWith("/v3/r2")) throw new Error("Require explicit local Wrangler v3/r2 directory");
  const options = convertV4MiniflareOptions({ modules: true, script: "export default { fetch() { return new Response(null,{status:404}); } }", compatibilityDate: "2026-08-28", r2Buckets: { BUCKET: "site-creator-r2" }, });
  options.resourcePersistencePath = path.dirname(persistence);
  const mf = new Miniflare(options);
  try {
    const bucket = await mf.getR2Bucket("BUCKET"), prior = await bucket.get(pointerKey);
    if (prior && hash(Buffer.from(await prior.arrayBuffer())) !== hash(pointerBytes)) throw new Error("A different local active pointer exists; preserve and reconcile it first");
    // Every input was checked before storage mutation; immutable conflicts fail.
    let cursor = 0;
    await Promise.all(Array.from({ length: 6 }, async () => {
      while (cursor < objects.length) {
        const object = objects[cursor++], prior = await bucket.get(object.key);
        if (prior) {
          if (hash(Buffer.from(await prior.arrayBuffer())) !== object.sha256) throw new Error("Immutable local object conflict");
          continue;
        }
        const bytes = await read(object.key, object.max);
        if (hash(bytes) !== object.sha256) throw new Error("Package changed during restoration");
        await bucket.put(object.key, bytes, { httpMetadata: { contentType: object.key.endsWith(".png") ? "image/png" : "application/json" } });
        const check = await bucket.get(object.key);
        if (!check || hash(Buffer.from(await check.arrayBuffer())) !== object.sha256) throw new Error("Local copy readback failed");
      }
    }));
    await bucket.put(pointerKey, pointerBytes, { httpMetadata: { contentType: "application/json" } });
    console.log(JSON.stringify({ localRestored: true, setId: pointer.setId, objects: objects.length, hostedChanged: false }));
  } finally { await mf.dispose(); }
}
