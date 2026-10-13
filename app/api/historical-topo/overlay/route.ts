import { topoRequestKey } from "../../../historical-topo-overlay";
import { topoActive, topoBucket, topoBytes, topoCatalogSheet, topoFailure, topoJson, topoPrivateHeaders, topoSameOrigin, topoScanId, topoUser, TopoOverlayError } from "../../../historical-topo-overlay-server";
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
    topoSameOrigin(request); await topoUser();
    if (!request.headers.get("content-type")?.startsWith("application/json") || Number(request.headers.get("content-length") ?? 0) > 256) throw new TopoOverlayError("Invalid sheet request.");
    const raw = await request.arrayBuffer();
    if (raw.byteLength > 256) throw new TopoOverlayError("Invalid sheet request.");
    const body = topoJson(raw) as { id?: unknown };
    if (!body || !Number.isInteger(body.id)) throw new TopoOverlayError("Invalid sheet request.");
    const sheet = await topoCatalogSheet(body.id as number);
    const active = await topoActive(sheet.scanId);
    if (active) return Response.json({ state: "ready", scanId: sheet.scanId }, { headers: topoPrivateHeaders });
    const key = topoRequestKey(sheet.scanId);
    if (await topoBytes(key, 4096)) return Response.json({ state: "preparing", scanId: sheet.scanId }, { headers: topoPrivateHeaders });
    const points = sheet.footprint.geometry.coordinates.flat();
    const west = Math.min(...points.map((point) => point[0])), east = Math.max(...points.map((point) => point[0]));
    const south = Math.min(...points.map((point) => point[1])), north = Math.max(...points.map((point) => point[1]));
    const requestRecord = { version: 1, id: sheet.id, scanId: sheet.scanId, name: sheet.name, year: sheet.year, scale: sheet.scale,
      state: "KS", footprint: [[[west, south], [east, south], [east, north], [west, north], [west, south]]], requestedAt: new Date().toISOString() };
    await topoBucket().put(key, new TextEncoder().encode(JSON.stringify(requestRecord)).buffer as ArrayBuffer, { httpMetadata: { contentType: "application/json" } });
    return Response.json({ state: "preparing", scanId: sheet.scanId }, { status: 202, headers: topoPrivateHeaders });
  } catch (error) { return topoFailure(error); }
}
