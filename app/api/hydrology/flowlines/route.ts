import { NextRequest, NextResponse } from "next/server";
import { readBoundedJson } from "../../../bounded-json";
import { createFlowlineRequestPool } from "../../../flowline-request-pool";
import { FLOW_PROFILES, FLOWLINE_EXTENT, isFlowDetail, FLOWLINE_LIMITATION, FLOWLINE_SERVICE, parseFlowlineCell, type FlowlineCellPayload } from "../../../water-flow-motion";
import { parseWaterReaches } from "../../../water-path-analysis";

export const dynamic = "force-dynamic";

const round = (value: number) => Math.round(value * 1e5) / 1e5;
const requests = createFlowlineRequestPool();

/**
 * One fixed Kansas grid cell at the requested display detail of USGS 3DHP flowlines that carry the
 * provider's explicit downstream flag (flowdirection = 1, in digitized
 * order). Reaches without that flag are not returned, so the Site never
 * animates a direction the provider did not supply.
 */
export async function GET(request: NextRequest) {
  const query = request.nextUrl.searchParams;
  const detail = query.has("detail") ? query.get("detail") : "local";
  const validQuery = query.getAll("cell").length === 1 && query.getAll("detail").length <= 1
    && [...query.keys()].every(key => key === "cell" || key === "detail") && isFlowDetail(detail);
  const cell = validQuery ? parseFlowlineCell(query.get("cell"), detail) : null;
  if (!cell || !isFlowDetail(detail)) return NextResponse.json({ error: "A fixed Kansas flowline cell and supported detail are required." }, { status: 400 });
  const [west, south] = cell, profile = FLOW_PROFILES[detail];
  const upstream = new URL(FLOWLINE_SERVICE);
  for (const [key, value] of Object.entries({
    f: "geojson",
    geometry: [west, south, Math.min(FLOWLINE_EXTENT.east, west + profile.step), Math.min(FLOWLINE_EXTENT.north, south + profile.step)].map((v) => v.toFixed(2)).join(","),
    geometryType: "esriGeometryEnvelope", inSR: "4326", spatialRel: "esriSpatialRelIntersects",
    outFields: "id3dhp,hydrosequence,dnhydrosequence,uphydrosequence,levelpath,gnisidlabel,flowdirection,featuretype,streamorder",
    where: "flowdirection=1 AND featuretype IN (1,4,5,6)" + (profile.minOrder ? " AND streamorder>=" + profile.minOrder : ""),
    outSR: "4326", returnGeometry: "true", returnZ: "false", resultRecordCount: "400",
    // Profile-specific display simplification preserves downstream vertex order.
    maxAllowableOffset: profile.offset, orderByFields: profile.minOrder ? "streamorder DESC,hydrosequence DESC" : "hydrosequence DESC",
  })) upstream.searchParams.set(key, value);
  const result = await requests.get(detail + ":" + cell.join(","), request.signal, async signal => {
    const response = await fetch(upstream, { headers: { Accept: "application/json" }, redirect: "manual", cache: "no-store", signal });
    if (!response.ok) {
      await response.body?.cancel().catch(() => undefined);
      throw new Error("USGS service unavailable.");
    }
    const raw = await readBoundedJson(response, 6 * 1024 * 1024, signal) as { exceededTransferLimit?: unknown };
    const parsed = parseWaterReaches(raw);
    if (profile.minOrder && parsed.some(reach => !(typeof reach.streamOrder === "number" && reach.streamOrder >= profile.minOrder))) throw new Error("Provider stream order does not match the requested detail.");
    const reaches = parsed.map((reach) => ({
      id: reach.id, sequence: reach.sequence, downstream: reach.downstream, levelpath: reach.levelpath,
      name: reach.name, featureType: reach.featureType ?? 1, ...(reach.streamOrder === undefined ? {} : { streamOrder: reach.streamOrder }),
      coordinates: reach.coordinates.map(([lng, lat]) => [round(lng), round(lat)] as [number, number]),
    }));
    const payload: FlowlineCellPayload = {
      format: "kfm-3dhp-flowlines-v1", cell, detail, state: reaches.length ? "ready" : "empty",
      truncated: raw.exceededTransferLimit === true, reaches,
      source: FLOWLINE_SERVICE, retrievedAt: new Date().toISOString(), evidenceRole: "EXTERNAL_CONTEXT_ONLY", limitation: FLOWLINE_LIMITATION + " " + profile.label + "; stream order " + (profile.minOrder || "all supplied") + "; display geometry generalization " + profile.offset + " degrees. Stream order is not discharge. Coverage is limited to returned tiles and reaches.",
    };
    return JSON.stringify(payload);
  });
  if (result.state === "ready") return new NextResponse(result.body, { headers: {
    "Content-Type": "application/json", "Cache-Control": "private, max-age=" + Math.max(0, Math.floor((result.expires - Date.now()) / 1000)),
  } });
  return NextResponse.json({ error: "USGS 3DHP flowlines are unavailable for this cell." }, { status: 503, headers: {
    "Cache-Control": "no-store", ...(result.state === "cancelled" ? {} : { "Retry-After": "1" }),
  } });
}
