import { topoRequestKey } from "../../../historical-topo-overlay";
import { topoCatalogRequest } from "../../../historical-topo-request-quota";
import { topoActive, topoBucket, topoBytes, topoDigest, topoFailure, topoJson, topoPrivateHeaders, topoSameOrigin, topoScanId, topoUser, TopoOverlayError } from "../../../historical-topo-overlay-server";
export const dynamic = "force-dynamic";

export async function GET(request: Request) {
  try {
    await topoUser();
    const scanId = topoScanId(new URL(request.url).searchParams.get("scan"));
    const active = await topoActive(scanId);
    if (active) {
      const m = active.manifest;
      return Response.json({ state: "ready", sheet: m.sheet, bounds: m.bounds, minZoom: m.minZoom, maxZoom: m.maxZoom,
        sourceUrl: m.geotiff.url, sourceSha256: m.geotiff.sha256, nativeWidth: m.geotiff.width, nativeHeight: m.geotiff.height,
        packageId: m.packageId, reviewedAt: active.pointer.reviewedAt,
        tileTemplate: `/api/historical-topo/tiles/${scanId}/${m.packageId}/{z}/{x}/{y}.png`, evidenceRole: m.evidenceRole }, { headers: topoPrivateHeaders });
    }
    const pending = await topoBytes(topoRequestKey(scanId), 4096);
    return Response.json({ state: pending ? "preparing" : "unavailable", scanId,
      message: pending ? "This Kansas sheet has been requested for preparation and review." : "A verified map image has not been prepared for this sheet." }, { headers: topoPrivateHeaders });
  } catch (error) { return topoFailure(error); }
}

export async function POST(request: Request) {
  try {
    topoSameOrigin(request); const user = await topoUser();
    if (!request.headers.get("content-type")?.startsWith("application/json") || Number(request.headers.get("content-length") ?? 0) > 256) throw new TopoOverlayError("Invalid sheet request.");
    const raw = await request.arrayBuffer();
    if (raw.byteLength > 256) throw new TopoOverlayError("Invalid sheet request.");
    const body = topoJson(raw) as { id?: unknown };
    if (!body || !Number.isInteger(body.id)) throw new TopoOverlayError("Invalid sheet request.");
    const requester = await topoDigest(new TextEncoder().encode(user.id || user.email.toLowerCase()).buffer as ArrayBuffer);
    const record = await topoCatalogRequest(requester, body.id as number);
    const active = await topoActive(record.scanId);
    if (active) return Response.json({ state: "ready", scanId: record.scanId }, { headers: topoPrivateHeaders });
    const key = topoRequestKey(record.scanId);
    if (await topoBytes(key, 4096)) return Response.json({ state: "preparing", scanId: record.scanId }, { headers: topoPrivateHeaders });
    const created = await topoBucket().put(key, new TextEncoder().encode(JSON.stringify(record)).buffer as ArrayBuffer, {
      httpMetadata: { contentType: "application/json" }, onlyIf: { etagDoesNotMatch: "*" },
    });
    return Response.json({ state: "preparing", scanId: record.scanId }, { status: created ? 202 : 200, headers: topoPrivateHeaders });
  } catch (error) { return topoFailure(error); }
}
