import { parseTopoOverlayManifest, topoCandidateKey, topoManifestKey, topoRequestKey, topoTileKey } from "../../../historical-topo-overlay";
import { topoBucket, topoBytes, topoDigest, topoFailure, topoJson, topoScanId, topoWorker, TopoOverlayError } from "../../../historical-topo-overlay-server";
export const dynamic = "force-dynamic";
const png = [137, 80, 78, 71, 13, 10, 26, 10];

export async function PUT(request: Request) {
  try {
    topoWorker(request);
    const params = new URL(request.url).searchParams;
    if ([...params.keys()].some((key) => !["scan", "package", "address"].includes(key) || params.getAll(key).length !== 1)) throw new TopoOverlayError("Invalid tile address.");
    const scanId = topoScanId(params.get("scan"));
    const packageId = params.get("package") ?? "";
    const address = params.get("address") ?? "";
    if (!/^[0-9a-f]{24}$/.test(packageId) || !(address === "manifest" || /^(?:[0-9]|1[0-6])\/(?:0|[1-9]\d{0,7})\/(?:0|[1-9]\d{0,7})$/.test(address))) throw new TopoOverlayError("Invalid tile address.");
    if (!await topoBytes(topoRequestKey(scanId), 4096)) throw new TopoOverlayError("No Kansas sheet request exists for this scan.", 409);
    const maximum = address === "manifest" ? 750_000 : 2_000_000;
    const declared = Number(request.headers.get("content-length") ?? "0");
    if (!request.body || !Number.isInteger(declared) || declared < 1 || declared > maximum) throw new TopoOverlayError("Prepared map object exceeds its limit.", 413);
    const bytes = await request.arrayBuffer();
    if (bytes.byteLength < 24 || bytes.byteLength > maximum) throw new TopoOverlayError("Prepared map object exceeds its limit.", 413);
    const digest = await topoDigest(bytes);
    if (request.headers.get("x-kfm-sha256") !== digest) throw new TopoOverlayError("Prepared map digest does not match.", 409);
    const key = address === "manifest" ? topoManifestKey(scanId, packageId) : topoTileKey(scanId, packageId, address);
    if (address === "manifest") {
      if (request.headers.get("content-type")?.split(";")[0] !== "application/json") throw new TopoOverlayError("Expected a JSON manifest.", 415);
      const manifest = parseTopoOverlayManifest(topoJson(bytes));
      const requestRecord = topoJson((await topoBytes(topoRequestKey(scanId), 4096))!) as { id: number; name: string; year: number; scale: number };
      if (!manifest || manifest.packageId !== packageId || manifest.sheet.scanId !== scanId || manifest.sheet.id !== requestRecord.id
        || manifest.sheet.name !== requestRecord.name || manifest.sheet.year !== requestRecord.year || manifest.sheet.scale !== requestRecord.scale) throw new TopoOverlayError("Manifest does not match the requested Kansas sheet.", 409);
    } else {
      const parts = address.split("/").map(Number), [z, x, y] = parts;
      if (x >= 2 ** z || y >= 2 ** z || request.headers.get("content-type")?.split(";")[0] !== "image/png"
        || !png.every((part, index) => new Uint8Array(bytes)[index] === part)) throw new TopoOverlayError("Invalid prepared map tile.", 415);
    }
    const prior = await topoBytes(key, maximum);
    if (prior) {
      if (await topoDigest(prior) !== digest) throw new TopoOverlayError("An immutable map object already exists with different bytes.", 409);
      // An interrupted run may have stored the immutable manifest before it
      // could publish the review candidate. Repeating the same bytes repairs
      // that pointer without weakening the digest or edition checks above.
      if (address === "manifest") {
        const candidate = new TextEncoder().encode(JSON.stringify({ scanId, packageId, manifestSha256: digest, stagedAt: new Date().toISOString() })).buffer as ArrayBuffer;
        await topoBucket().put(topoCandidateKey(scanId), candidate, { httpMetadata: { contentType: "application/json" } });
      }
      return Response.json({ staged: true, alreadyPresent: true, sha256: digest });
    }
    await topoBucket().put(key, bytes, { httpMetadata: { contentType: address === "manifest" ? "application/json" : "image/png" } });
    const stored = await topoBytes(key, maximum);
    if (!stored || await topoDigest(stored) !== digest) throw new TopoOverlayError("Prepared map object failed readback.", 503);
    if (address === "manifest") {
      const candidate = new TextEncoder().encode(JSON.stringify({ scanId, packageId, manifestSha256: digest, stagedAt: new Date().toISOString() })).buffer as ArrayBuffer;
      await topoBucket().put(topoCandidateKey(scanId), candidate, { httpMetadata: { contentType: "application/json" } });
    }
    return Response.json({ staged: true, alreadyPresent: false, sha256: digest }, { status: 201 });
  } catch (error) { return topoFailure(error); }
}
