import { NextRequest, NextResponse } from "next/server";
import { readBoundedJson } from "../../../bounded-json";
import { FLOWLINE_LIMITATION, FLOWLINE_SERVICE, parseFlowRequest, type FlowlineCellPayload } from "../../../water-flow-motion";
import { parseWaterReaches } from "../../../water-path-analysis";

export const dynamic = "force-dynamic";

const round = (value: number) => Math.round(value * 1e5) / 1e5;

/**
 * One fixed overview, regional or local Kansas grid cell of 3DHP flowlines with
 * provider's explicit downstream flag (flowdirection = 1, in digitized
 * order). Reaches without that flag are not returned, so the Site never
 * animates a direction the provider did not supply.
 */
export async function GET(request: NextRequest) {
  const query = request.nextUrl.searchParams;
  const plan = query.size === 1 && query.getAll("cell").length === 1 ? parseFlowRequest(query.get("cell")) : null;
  if (!plan) return NextResponse.json({ error: "A fixed Kansas flowline cell is required." }, { status: 400 });
  const { cell } = plan;
  const [west, south] = cell;
  const upstream = new URL(FLOWLINE_SERVICE);
  for (const [key, value] of Object.entries({
    f: "geojson",
    geometry: [west, south, plan.east, plan.north].map((v) => v.toFixed(2)).join(","),
    geometryType: "esriGeometryEnvelope", inSR: "4326", spatialRel: "esriSpatialRelIntersects",
    outFields: "id3dhp,hydrosequence,dnhydrosequence,uphydrosequence,levelpath,gnisidlabel,flowdirection,featuretype,streamorder",
    where: `flowdirection=1 AND featuretype IN (1,4,5,6)${plan.minimumOrder ? ` AND streamorder>=${plan.minimumOrder}` : ""}`,
    outSR: "4326", returnGeometry: "true", returnZ: "false", resultRecordCount: "400",
    // Tier-bounded generalization; the provider keeps digitized direction.
    maxAllowableOffset: String(plan.offset), orderByFields: "hydrosequence DESC",
  })) upstream.searchParams.set(key, value);
  const signal = AbortSignal.any([request.signal, AbortSignal.timeout(30_000)]);
  try {
    const response = await fetch(upstream, { headers: { Accept: "application/json" }, redirect: "manual", cache: "no-store", signal });
    if (!response.ok) throw new Error("USGS service unavailable.");
    const raw = await readBoundedJson(response, 6 * 1024 * 1024, signal) as { exceededTransferLimit?: unknown; features?: { properties?: Record<string, unknown> }[] };
    const orders = new Map((Array.isArray(raw.features) ? raw.features : []).map(feature => {
      const p = feature?.properties;
      const value = p?.streamorder;
      return [p?.id3dhp, typeof value === "number" && Number.isInteger(value) && value >= 1 && value <= 20 ? value : null];
    }));
    const reaches = parseWaterReaches(raw).map((reach) => ({
      id: reach.id, sequence: reach.sequence, downstream: reach.downstream, levelpath: reach.levelpath,
      name: reach.name, featureType: reach.featureType ?? 1,
      streamOrder: orders.get(reach.id) ?? null,
      coordinates: reach.coordinates.map(([lng, lat]) => [round(lng), round(lat)] as [number, number]),
    })).filter(reach => !plan.minimumOrder || (reach.streamOrder !== null && reach.streamOrder >= plan.minimumOrder));
    const payload: FlowlineCellPayload = {
      format: "kfm-3dhp-flowlines-v2", requestKey: plan.key, cell, state: reaches.length ? "ready" : "empty",
      truncated: raw.exceededTransferLimit === true || reaches.length === 400, reaches,
      source: FLOWLINE_SERVICE, retrievedAt: new Date().toISOString(), evidenceRole: "EXTERNAL_CONTEXT_ONLY", limitation: FLOWLINE_LIMITATION,
    };
    return NextResponse.json(payload, { headers: { "Cache-Control": "private, max-age=3600" } });
  } catch {
    return NextResponse.json({ error: "USGS 3DHP flowlines are unavailable for this cell." }, { status: 503, headers: { "Cache-Control": "no-store" } });
  }
}
