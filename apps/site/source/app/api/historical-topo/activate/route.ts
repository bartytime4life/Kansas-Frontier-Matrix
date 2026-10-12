import { parseTopoOverlayManifest, topoActiveKey, topoManifestKey, topoOverlayPrefix, topoRequestKey, topoTileKey, type TopoActivePointer } from "../../../historical-topo-overlay";
import { topoActive, topoBucket, topoBytes, topoDigest, topoFailure, topoJson, topoOwner, topoSameOrigin, topoScanId, TopoOverlayError } from "../../../historical-topo-overlay-server";
export const dynamic = "force-dynamic";

export async function POST(request: Request) {
  try {
    topoSameOrigin(request);
    const user = await topoOwner();
    if (!request.headers.get("content-type")?.startsWith("application/json") || Number(request.headers.get("content-length") ?? 0) > 2048) throw new TopoOverlayError("Invalid review record.");
    const raw = await request.arrayBuffer();
    if (raw.byteLength > 2048) throw new TopoOverlayError("Invalid review record.");
    const body = topoJson(raw) as { scanId?: unknown; packageId?: unknown; manifestSha256?: unknown; note?: unknown; rollback?: unknown };
    const scanId = topoScanId(String(body.scanId ?? ""));
    const packageId = body.packageId;
    const hash = body.manifestSha256;
    const note = body.note;
    if (typeof packageId !== "string" || !/^[0-9a-f]{24}$/.test(packageId) || typeof hash !== "string" || !/^[0-9a-f]{64}$/.test(hash)
      || typeof note !== "string" || note.trim().length < 10 || note.length > 1000 || ![undefined, true].includes(body.rollback as undefined | true)) throw new TopoOverlayError("Invalid review record.");
    const manifestBytes = await topoBytes(topoManifestKey(scanId, packageId), 750_000);
    if (!manifestBytes || await topoDigest(manifestBytes) !== hash) throw new TopoOverlayError("Prepared map manifest failed validation.", 409);
    const manifest = parseTopoOverlayManifest(topoJson(manifestBytes));
    const requested = await topoBytes(topoRequestKey(scanId), 4096);
    if (!manifest || !requested || manifest.sheet.scanId !== scanId || manifest.packageId !== packageId) throw new TopoOverlayError("Prepared map does not match a Kansas request.", 409);
    const requestRecord = topoJson(requested) as { id: number; name: string; year: number; scale: number };
    if (manifest.sheet.id !== requestRecord.id || manifest.sheet.name !== requestRecord.name || manifest.sheet.year !== requestRecord.year || manifest.sheet.scale !== requestRecord.scale) throw new TopoOverlayError("Prepared map does not match the requested edition.", 409);
    const previous = await topoActive(scanId);
    if (body.rollback === true && (!previous || previous.pointer.previousPackageId !== packageId || previous.pointer.previousManifestSha256 !== hash)) throw new TopoOverlayError("Rollback target is not the previous reviewed package.", 409);
    if (previous?.pointer.packageId === packageId) throw new TopoOverlayError("This package is already active.", 409);
    const expected = new Set(Object.keys(manifest.tiles).map((address) => topoTileKey(scanId, packageId, address)));
    const prefix = `${topoOverlayPrefix}/packages/${scanId}/${packageId}/tiles/`;
    const bucket = topoBucket();
    let cursor: string | undefined, pages = 0;
    for (;;) {
      const page = await bucket.list({ prefix, cursor, limit: 1000 });
      for (const object of page.objects) if (!expected.delete(object.key)) throw new TopoOverlayError("Prepared map contains an unexpected tile.", 409);
      if (!page.truncated) break;
      if (!page.cursor || ++pages > 5) throw new TopoOverlayError("Prepared map tile inventory is incomplete.", 503);
      cursor = page.cursor;
    }
    if (expected.size) throw new TopoOverlayError("Prepared map is missing tiles.", 409);
    const reviewer = new TextEncoder().encode(user.id ? `id:${user.id}` : `email:${user.email.toLowerCase()}`);
    const pointer: TopoActivePointer = { scanId, packageId, manifestSha256: hash, reviewedAt: new Date().toISOString(), reviewedBy: await topoDigest(reviewer.buffer as ArrayBuffer), note: note.trim(), previousPackageId: previous?.pointer.packageId ?? null, previousManifestSha256: previous?.pointer.manifestSha256 ?? null };
    const pointerBytes = new TextEncoder().encode(JSON.stringify(pointer)).buffer as ArrayBuffer;
    if (previous) {
      const oldBytes = await topoBytes(topoActiveKey(scanId), 2048);
      if (!oldBytes) throw new TopoOverlayError("Previous review pointer disappeared.", 503);
      await bucket.put(`${topoOverlayPrefix}/history/${scanId}/${Date.now()}-${await topoDigest(oldBytes)}.json`, oldBytes, { httpMetadata: { contentType: "application/json" } });
    }
    await bucket.put(topoActiveKey(scanId), pointerBytes, { httpMetadata: { contentType: "application/json" } });
    const readback = await topoActive(scanId);
    if (readback?.pointer.manifestSha256 !== hash) throw new TopoOverlayError("Historical map activation readback failed.", 503);
    return Response.json({ active: true, scanId, packageId, tileCount: Object.keys(manifest.tiles).length, reviewedAt: pointer.reviewedAt }, { headers: { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" } });
  } catch (error) { return topoFailure(error); }
}
