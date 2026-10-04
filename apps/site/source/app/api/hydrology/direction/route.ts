import { NextRequest, NextResponse } from "next/server";
import { readBoundedJson } from "../../../bounded-json";
import { ELEVATION_SOURCE, nearestWaterReach, parseWaterElevations, parseWaterReaches, sampleWaterPath, traceWaterPath, type WaterPathAnalysis } from "../../../water-path-analysis";

export const dynamic = "force-dynamic";
const SERVICE = "https://3dhp.nationalmap.gov/arcgis/rest/services/usgs_3dhp_all/MapServer/50/query";
const LIMITATION = "Nearest USGS mapped river, followed only through supplied downstream network identifiers and meeting endpoints. Direction is provider-supplied; terrain sampling does not establish hydraulic velocity, wet-channel extent, water depth or flood level.";

export async function GET(request: NextRequest) {
  const query = request.nextUrl.searchParams;
  const longitude = Number(query.get("lon")), latitude = Number(query.get("lat"));
  if (query.size !== 2 || query.getAll("lon").length !== 1 || query.getAll("lat").length !== 1
    || !query.get("lon") || !query.get("lat") || !Number.isFinite(longitude) || !Number.isFinite(latitude)
    || longitude < -102.1 || longitude > -94.5 || latitude < 36.9 || latitude > 40.1) {
    return NextResponse.json({ error: "A Kansas gauge coordinate is required." }, { status: 400 });
  }
  const signal = AbortSignal.any([request.signal, AbortSignal.timeout(35_000)]);
  const read = async (url: URL, limit: number) => {
    const response = await fetch(url, { headers: { Accept: "application/json" }, redirect: "manual", cache: "no-store", signal });
    if (!response.ok) throw new Error("USGS service unavailable.");
    return await readBoundedJson(response, limit, signal);
  };
  const channels = async (distance: number, levelpath?: number) => {
    const upstream = new URL(SERVICE);
    for (const [key, value] of Object.entries({
      f: "geojson", geometry: `${longitude.toFixed(5)},${latitude.toFixed(5)}`, geometryType: "esriGeometryPoint", inSR: "4326",
      distance: String(distance), units: "esriSRUnit_Meter", outFields: "id3dhp,hydrosequence,dnhydrosequence,levelpath,gnisidlabel,flowdirection,featuretype",
      outSR: "4326", returnGeometry: "true", returnZ: "false", resultRecordCount: "400", orderByFields: "hydrosequence DESC",
      where: `flowdirection=1 AND featuretype IN (1,4,5,6)${levelpath ? ` AND levelpath=${levelpath}` : ""}`,
    })) upstream.searchParams.set(key, value);
    const raw = await read(upstream, 4 * 1024 * 1024) as { exceededTransferLimit?: boolean };
    return { reaches: parseWaterReaches(raw), truncated: raw.exceededTransferLimit === true };
  };
  try {
    const nearby = await channels(1200);
    if (nearby.truncated) throw new Error("Nearby channel inventory incomplete.");
    const seed = nearestWaterReach(nearby.reaches, [longitude, latitude]);
    let analysis: WaterPathAnalysis | null = null;
    const paths = [];
    if (seed) {
      let network = nearby.reaches, notice = "";
      if (seed.reach.levelpath) {
        try {
          const expanded = await channels(25000, seed.reach.levelpath);
          network = [...new Map([...nearby.reaches, ...expanded.reaches].map(reach => [reach.id, reach])).values()];
          if (expanded.truncated) notice = " The river inventory reached its response limit.";
        } catch { notice = " The extended river inventory was unavailable; showing checked nearby connections."; }
      }
      signal.throwIfAborted();
      const traced = traceWaterPath(seed, network);
      if (traced.path.coordinates.length >= 2 && traced.lengthM >= 1) {
        paths.push(traced.path);
        const requested = sampleWaterPath(traced.path.coordinates);
        let elevation: WaterPathAnalysis["elevation"] = { state: "unavailable", samples: [], dropM: null, slopePercent: null, source: ELEVATION_SOURCE, retrievedAt: null, notice: "Elevation service unavailable. Mapped direction remains visible without an elevation estimate." };
        try {
          const upstream = new URL(ELEVATION_SOURCE);
          upstream.search = new URLSearchParams({ f: "json", geometry: JSON.stringify({ points: requested.map(s => s.coordinate), spatialReference: { wkid: 4326 } }), geometryType: "esriGeometryMultipoint", returnFirstValueOnly: "true", interpolation: "RSP_BilinearInterpolation", outFields: "VerticalDatum", renderingRule: JSON.stringify({ rasterFunction: "None" }) }).toString();
          elevation = parseWaterElevations(await read(upstream, 128 * 1024), requested);
        } catch { /* Direction remains useful when elevation is unavailable. */ }
        analysis = { lengthM: traced.lengthM, gaugeOffsetM: traced.gaugeOffsetM, segments: traced.segments, connectors: traced.connectors, name: traced.name, stopReason: traced.stopReason + notice, elevation };
      }
    }
    return NextResponse.json({ format: "kfm-3dhp-direction-v2", state: paths.length ? "ready" : "empty", paths, analysis,
      source: SERVICE, retrievedAt: new Date().toISOString(), evidenceRole: "EXTERNAL_CONTEXT_ONLY", limitation: LIMITATION,
    }, { headers: { "Cache-Control": "private, max-age=3600" } });
  } catch {
    return NextResponse.json({ error: "USGS mapped downstream direction is unavailable for this gauge." }, { status: 503, headers: { "Cache-Control": "no-store" } });
  }
}
