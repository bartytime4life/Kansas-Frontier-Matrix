import { NextRequest, NextResponse } from "next/server";
import { readBoundedJson } from "../../../bounded-json";
import { FLOWLINE_CELL_DEGREES, FLOWLINE_LIMITATION, FLOWLINE_SERVICE, parseFlowlineCell, type FlowlineCellPayload } from "../../../water-flow-motion";
import { parseWaterReaches } from "../../../water-path-analysis";

export const dynamic = "force-dynamic";

const round = (value: number) => Math.round(value * 1e5) / 1e5;

/**
 * One fixed 0.25° Kansas grid cell of USGS 3DHP flowlines that carry the
 * provider's explicit downstream flag (flowdirection = 1, in digitized
 * order). Reaches without that flag are not returned, so the Site never
 * animates a direction the provider did not supply.
 */
export async function GET(request: NextRequest) {
  const query = request.nextUrl.searchParams;
  const cell = query.size === 1 && query.getAll("cell").length === 1 ? parseFlowlineCell(query.get("cell")) : null;
  if (!cell) return NextResponse.json({ error: "A Kansas 0.25° flowline cell is required." }, { status: 400 });
  const [west, south] = cell;
  const upstream = new URL(FLOWLINE_SERVICE);
  for (const [key, value] of Object.entries({
    f: "geojson",
    geometry: [west, south, west + FLOWLINE_CELL_DEGREES, south + FLOWLINE_CELL_DEGREES].map((v) => v.toFixed(2)).join(","),
    geometryType: "esriGeometryEnvelope", inSR: "4326", spatialRel: "esriSpatialRelIntersects",
    outFields: "id3dhp,hydrosequence,dnhydrosequence,uphydrosequence,levelpath,gnisidlabel,flowdirection,featuretype",
    where: "flowdirection=1 AND featuretype IN (1,4,5,6)",
    outSR: "4326", returnGeometry: "true", returnZ: "false", resultRecordCount: "400",
    // About 20 m: keeps vertex order (and so direction) while trimming detail.
    maxAllowableOffset: "0.0002", orderByFields: "hydrosequence DESC",
  })) upstream.searchParams.set(key, value);
  const signal = AbortSignal.any([request.signal, AbortSignal.timeout(30_000)]);
  try {
    const response = await fetch(upstream, { headers: { Accept: "application/json" }, redirect: "manual", cache: "no-store", signal });
    if (!response.ok) throw new Error("USGS service unavailable.");
    const raw = await readBoundedJson(response, 6 * 1024 * 1024, signal) as { exceededTransferLimit?: unknown };
    const reaches = parseWaterReaches(raw).map((reach) => ({
      id: reach.id, sequence: reach.sequence, downstream: reach.downstream, levelpath: reach.levelpath,
      name: reach.name, featureType: reach.featureType ?? 1,
      coordinates: reach.coordinates.map(([lng, lat]) => [round(lng), round(lat)] as [number, number]),
    }));
    const payload: FlowlineCellPayload = {
      format: "kfm-3dhp-flowlines-v1", cell, state: reaches.length ? "ready" : "empty",
      truncated: raw.exceededTransferLimit === true, reaches,
      source: FLOWLINE_SERVICE, retrievedAt: new Date().toISOString(), evidenceRole: "EXTERNAL_CONTEXT_ONLY", limitation: FLOWLINE_LIMITATION,
    };
    return NextResponse.json(payload, { headers: { "Cache-Control": "private, max-age=3600" } });
  } catch {
    return NextResponse.json({ error: "USGS 3DHP flowlines are unavailable for this cell." }, { status: 503, headers: { "Cache-Control": "no-store" } });
  }
}
