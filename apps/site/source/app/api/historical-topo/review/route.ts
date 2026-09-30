import { parseTopoOverlayManifest, topoCandidateKey, topoManifestKey } from "../../../historical-topo-overlay";
import { topoActive, topoBytes, topoDigest, topoFailure, topoJson, topoOwner, topoPrivateHeaders, topoScanId, TopoOverlayError } from "../../../historical-topo-overlay-server";
export const dynamic = "force-dynamic";

export async function GET(request: Request) {
  try {
    await topoOwner();
    const params = new URL(request.url).searchParams;
    if ([...params.keys()].some((key) => !["scan", "mode"].includes(key) || params.getAll(key).length !== 1)) throw new TopoOverlayError("Invalid review request.");
    const scanId = topoScanId(params.get("scan"));
    const rollback = params.get("mode") === "previous";
    if (params.has("mode") && !rollback) throw new TopoOverlayError("Invalid review request.");
    if (rollback) {
      const active = await topoActive(scanId);
      const packageId = active?.pointer.previousPackageId;
      const manifestSha256 = active?.pointer.previousManifestSha256;
      if (!packageId || !manifestSha256) return Response.json({ state: "none" }, { headers: topoPrivateHeaders });
      const bytes = await topoBytes(topoManifestKey(scanId, packageId), 750_000);
      if (!bytes || await topoDigest(bytes) !== manifestSha256) throw new TopoOverlayError("Previous map package failed validation.", 503);
      const manifest = parseTopoOverlayManifest(topoJson(bytes));
      if (!manifest || manifest.sheet.scanId !== scanId || manifest.packageId !== packageId || manifest.sheet.id !== active.manifest.sheet.id) throw new TopoOverlayError("Previous map package failed validation.", 503);
      return Response.json({ state: "staged", rollback: true, scanId, packageId, manifestSha256,
        sheet: manifest.sheet, bounds: manifest.bounds, minZoom: manifest.minZoom, maxZoom: manifest.maxZoom,
        sourceUrl: manifest.geotiff.url, sourceSha256: manifest.geotiff.sha256, tileCount: Object.keys(manifest.tiles).length,
        previewTileTemplate: `/api/historical-topo/review/tiles/${scanId}/${packageId}/{z}/{x}/{y}.png` }, { headers: topoPrivateHeaders });
    }
    const candidateBytes = await topoBytes(topoCandidateKey(scanId), 2048);
    if (!candidateBytes) return Response.json({ state: "none" }, { headers: topoPrivateHeaders });
    const candidate = topoJson(candidateBytes) as { scanId?: number; packageId?: string; manifestSha256?: string; stagedAt?: string };
    if (candidate.scanId !== scanId || !candidate.packageId || !/^[0-9a-f]{24}$/.test(candidate.packageId)
      || !candidate.manifestSha256 || !/^[0-9a-f]{64}$/.test(candidate.manifestSha256)) throw new TopoOverlayError("Prepared map candidate failed validation.", 503);
    const manifestBytes = await topoBytes(topoManifestKey(scanId, candidate.packageId), 750_000);
    if (!manifestBytes || await topoDigest(manifestBytes) !== candidate.manifestSha256) throw new TopoOverlayError("Prepared map candidate failed validation.", 503);
    const manifest = parseTopoOverlayManifest(topoJson(manifestBytes));
    if (!manifest || manifest.sheet.scanId !== scanId || manifest.packageId !== candidate.packageId) throw new TopoOverlayError("Prepared map candidate failed validation.", 503);
    return Response.json({ state: "staged", scanId, packageId: candidate.packageId, manifestSha256: candidate.manifestSha256,
      sheet: manifest.sheet, bounds: manifest.bounds, minZoom: manifest.minZoom, maxZoom: manifest.maxZoom,
      sourceUrl: manifest.geotiff.url, sourceSha256: manifest.geotiff.sha256, tileCount: Object.keys(manifest.tiles).length,
      previewTileTemplate: `/api/historical-topo/review/tiles/${scanId}/${candidate.packageId}/{z}/{x}/{y}.png`, stagedAt: candidate.stagedAt }, { headers: topoPrivateHeaders });
  } catch (error) { return topoFailure(error); }
}
