import { topoRequestKey } from "../../../historical-topo-overlay";
import { topoOverlayPrefix } from "../../../historical-topo-overlay";
import { topoActive, topoBucket, topoBytes, topoCatalogSheet, topoDigest, topoFailure, topoJson, topoPrivateHeaders, topoSameOrigin, topoScanId, topoUser, TopoOverlayError } from "../../../historical-topo-overlay-server";
export const dynamic = "force-dynamic";

// Any signed-in viewer may queue a sheet, so new queue entries are capped per
// requester per UTC day. The counter is advisory (not atomic) and bounds bulk
// queue flooding rather than enforcing an exact quota.
const DAILY_REQUEST_LIMIT = 10;

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
    const sheet = await topoCatalogSheet(body.id as number);
    const active = await topoActive(sheet.scanId);
    if (active) return Response.json({ state: "ready", scanId: sheet.scanId }, { headers: topoPrivateHeaders });
    const key = topoRequestKey(sheet.scanId);
    if (await topoBytes(key, 4096)) return Response.json({ state: "preparing", scanId: sheet.scanId }, { headers: topoPrivateHeaders });
    const requester = await topoDigest(new TextEncoder().encode(user.id || user.email.toLowerCase()).buffer as ArrayBuffer);
    const quotaKey = `${topoOverlayPrefix}/requesters/${requester}/${new Date().toISOString().slice(0, 10)}.json`;
    const quotaBytes = await topoBytes(quotaKey, 256);
    const used = quotaBytes ? Number((topoJson(quotaBytes) as { count?: unknown }).count) || 0 : 0;
    if (used >= DAILY_REQUEST_LIMIT) throw new TopoOverlayError("Daily historical map request limit reached. Try again tomorrow.", 429);
    const points = sheet.footprint.geometry.coordinates.flat();
    const west = Math.min(...points.map((point) => point[0])), east = Math.max(...points.map((point) => point[0]));
    const south = Math.min(...points.map((point) => point[1])), north = Math.max(...points.map((point) => point[1]));
    const requestRecord = { version: 1, id: sheet.id, scanId: sheet.scanId, name: sheet.name, year: sheet.year, scale: sheet.scale,
      state: "KS", footprint: [[[west, south], [east, south], [east, north], [west, north], [west, south]]], requestedAt: new Date().toISOString() };
    await topoBucket().put(quotaKey, new TextEncoder().encode(JSON.stringify({ count: used + 1 })).buffer as ArrayBuffer, { httpMetadata: { contentType: "application/json" } });
    await topoBucket().put(key, new TextEncoder().encode(JSON.stringify(requestRecord)).buffer as ArrayBuffer, { httpMetadata: { contentType: "application/json" } });
    return Response.json({ state: "preparing", scanId: sheet.scanId }, { status: 202, headers: topoPrivateHeaders });
  } catch (error) { return topoFailure(error); }
}
