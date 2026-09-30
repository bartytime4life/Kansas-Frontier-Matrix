import { parseTopoOverlayManifest, topoCandidateKey, topoManifestKey, topoTileKey } from "../../../../../../../../../historical-topo-overlay";
import { topoActive, topoBytes, topoDigest, topoFailure, topoJson, topoOwner, topoScanId, TopoOverlayError } from "../../../../../../../../../historical-topo-overlay-server";
export const dynamic = "force-dynamic";
const png = [137, 80, 78, 71, 13, 10, 26, 10];

export async function GET(_request: Request, context: { params: Promise<{ scan: string; package: string; z: string; x: string; y: string }> }) {
  try {
    await topoOwner();
    const p = await context.params;
    const scanId = topoScanId(p.scan);
    const candidateBytes = await topoBytes(topoCandidateKey(scanId), 2048);
    const candidate = candidateBytes ? topoJson(candidateBytes) as { packageId?: string; manifestSha256?: string } : null;
    const active = await topoActive(scanId);
    const expectedHash = candidate?.packageId === p.package ? candidate.manifestSha256
      : active?.pointer.previousPackageId === p.package ? active.pointer.previousManifestSha256 : null;
    if (!expectedHash) throw new TopoOverlayError("Prepared map tile not found.", 404);
    const manifestBytes = await topoBytes(topoManifestKey(scanId, p.package), 750_000);
    if (!manifestBytes || await topoDigest(manifestBytes) !== expectedHash) throw new TopoOverlayError("Prepared map manifest failed validation.", 503);
    const manifest = parseTopoOverlayManifest(topoJson(manifestBytes));
    if (!manifest || !/^(?:0|[1-9]\d?)$/.test(p.z) || !/^(?:0|[1-9]\d{0,7})$/.test(p.x) || !/^(?:0|[1-9]\d{0,7})\.png$/.test(p.y)) throw new TopoOverlayError("Invalid prepared tile.");
    const z = Number(p.z), x = Number(p.x), y = Number(p.y.slice(0, -4));
    const address = `${z}/${x}/${y}`;
    const expected = manifest.tiles[address];
    if (!expected || z < manifest.minZoom || z > manifest.maxZoom || x >= 2 ** z || y >= 2 ** z) throw new TopoOverlayError("Prepared map tile not found.", 404);
    const bytes = await topoBytes(topoTileKey(scanId, p.package, address), 2_000_000);
    if (!bytes || bytes.byteLength !== expected.bytes || !png.every((value, index) => new Uint8Array(bytes)[index] === value)
      || await topoDigest(bytes) !== expected.sha256) throw new TopoOverlayError("Prepared map tile failed validation.", 503);
    return new Response(bytes, { headers: { "Content-Type": "image/png", "Cache-Control": "private, no-store", "X-Content-Type-Options": "nosniff", "Vary": "Cookie" } });
  } catch (error) { return topoFailure(error); }
}
