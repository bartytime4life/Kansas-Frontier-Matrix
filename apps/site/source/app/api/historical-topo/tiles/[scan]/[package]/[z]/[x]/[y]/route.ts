import { topoTileKey } from "../../../../../../../../historical-topo-overlay";
import { topoActive, topoBytes, topoDigest, topoFailure, topoScanId, topoUser, TopoOverlayError } from "../../../../../../../../historical-topo-overlay-server";
export const dynamic = "force-dynamic";
const png = [137, 80, 78, 71, 13, 10, 26, 10];

export async function GET(_request: Request, context: { params: Promise<{ scan: string; package: string; z: string; x: string; y: string }> }) {
  try {
    await topoUser();
    const p = await context.params;
    const scanId = topoScanId(p.scan);
    const active = await topoActive(scanId);
    if (!active || active.pointer.packageId !== p.package) throw new TopoOverlayError("Reviewed historical map tile not found.", 404);
    if (!/^(?:0|[1-9]\d?)$/.test(p.z) || !/^(?:0|[1-9]\d{0,7})$/.test(p.x) || !/^(?:0|[1-9]\d{0,7})\.png$/.test(p.y)) throw new TopoOverlayError("Invalid tile coordinate.");
    const z = Number(p.z), x = Number(p.x), y = Number(p.y.slice(0, -4));
    if (z < active.manifest.minZoom || z > active.manifest.maxZoom || x >= 2 ** z || y >= 2 ** z) throw new TopoOverlayError("Invalid tile coordinate.");
    const address = `${z}/${x}/${y}`;
    const expected = active.manifest.tiles[address];
    if (!expected) throw new TopoOverlayError("Reviewed historical map tile not found.", 404);
    const bytes = await topoBytes(topoTileKey(scanId, p.package, address), 2_000_000);
    if (!bytes || bytes.byteLength !== expected.bytes || !png.every((value, index) => new Uint8Array(bytes)[index] === value)
      || await topoDigest(bytes) !== expected.sha256) throw new TopoOverlayError("Reviewed historical map tile failed validation.", 503);
    return new Response(bytes, { headers: { "Content-Type": "image/png", "Cache-Control": "private, max-age=3600", "X-Content-Type-Options": "nosniff", "Vary": "Cookie" } });
  } catch (error) { return topoFailure(error); }
}
