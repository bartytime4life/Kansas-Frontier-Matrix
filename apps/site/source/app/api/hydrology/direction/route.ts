import { NextRequest, NextResponse } from "next/server";
import { boundedDirectionPaths } from "../../../water-flow-context";

export const dynamic = "force-dynamic";

const SERVICE = "https://3dhp.nationalmap.gov/arcgis/rest/services/usgs_3dhp_all/MapServer/50/query";
const LIMITATION = "USGS 3DHP digitized downstream channel direction near the selected gauge. The animated guide is illustrative: it is not a measured water speed, wet channel extent, flood level, or forecast.";

export async function GET(request: NextRequest) {
  const query = request.nextUrl.searchParams;
  const longitude = Number(query.get("lon"));
  const latitude = Number(query.get("lat"));
  if (query.size !== 2 || query.getAll("lon").length !== 1 || query.getAll("lat").length !== 1
    || !query.get("lon") || !query.get("lat") || !Number.isFinite(longitude) || !Number.isFinite(latitude)
    || longitude < -102.1 || longitude > -94.5 || latitude < 36.9 || latitude > 40.1) {
    return NextResponse.json({ error: "A Kansas gauge coordinate is required." }, { status: 400 });
  }
  const upstream = new URL(SERVICE);
  for (const [key, value] of Object.entries({
    f: "geojson", geometry: `${longitude.toFixed(5)},${latitude.toFixed(5)}`,
    geometryType: "esriGeometryPoint", inSR: "4326", distance: "1200", units: "esriSRUnit_Meter",
    outFields: "id3dhp,flowdirection,featuretype", outSR: "4326", returnGeometry: "true",
    resultRecordCount: "100",
  })) upstream.searchParams.set(key, value);
  try {
    const response = await fetch(upstream, { headers: { Accept: "application/geo+json" }, redirect: "manual", cache: "no-store", signal: AbortSignal.timeout(8_000) });
    const length = Number(response.headers.get("content-length") ?? 0);
    if (!response.ok || (Number.isFinite(length) && length > 512_000)) throw new Error("USGS 3DHP is unavailable.");
    const body = await response.text();
    if (body.length > 512_000) throw new Error("USGS 3DHP response exceeded its limit.");
    const paths = boundedDirectionPaths(JSON.parse(body));
    return NextResponse.json({
      format: "kfm-3dhp-direction-v1", state: paths.length ? "ready" : "empty", paths,
      source: SERVICE, retrievedAt: new Date().toISOString(), evidenceRole: "EXTERNAL_CONTEXT_ONLY", limitation: LIMITATION,
    }, { headers: { "Cache-Control": "private, max-age=3600" } });
  } catch {
    return NextResponse.json({ error: "USGS mapped downstream direction is unavailable for this gauge." }, { status: 503, headers: { "Cache-Control": "no-store" } });
  }
}
