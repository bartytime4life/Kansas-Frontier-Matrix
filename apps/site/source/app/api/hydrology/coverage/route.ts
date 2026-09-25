import { boundedFetch, jsonHeaders } from "../../event-atlas/upstream";
export const dynamic = "force-dynamic";

/** Provider-declared series extents, never a promise of gap-free observations. */
export async function GET(request: Request) {
  const params = new URL(request.url).searchParams;
  const station = params.get("station") ?? "";
  if ([...params.keys()].some((key) => key !== "station") || params.getAll("station").length !== 1 || !/^USGS-\d{8,15}$/.test(station)) return Response.json({ message: "Choose a valid USGS station." }, { status: 400 });
  const url = new URL("https://api.waterdata.usgs.gov/ogcapi/v1/collections/time-series-metadata/items");
  url.search = new URLSearchParams({ f: "json", monitoring_location_id: station, parameter_code: "00060", limit: "100" }).toString();
  try {
    const body = JSON.parse((await boundedFetch(url.toString(), 1024 * 1024)).text());
    if (body.type !== "FeatureCollection" || !Array.isArray(body.features)) throw new Error("Unexpected USGS coverage response.");
    const series = body.features.flatMap((feature: { properties?: Record<string, unknown> }) => {
      const p = feature.properties;
      if (!p || p.monitoring_location_id !== station || p.parameter_code !== "00060") throw new Error("USGS returned another station or parameter.");
      const resolution = p.computation_period_identifier === "Daily" && p.statistic_id === "00003" ? "daily" : p.computation_period_identifier === "Points" && p.computation_identifier === "Instantaneous" ? "continuous" : null;
      if (!resolution || typeof p.begin !== "string" || typeof p.end !== "string" || !Number.isFinite(Date.parse(p.begin)) || !Number.isFinite(Date.parse(p.end)) || Date.parse(p.begin) > Date.parse(p.end)) return [];
      return [{ resolution, start: new Date(p.begin).toISOString(), end: new Date(p.end).toISOString(), unit: p.unit_of_measure, statistic: p.statistic_id }];
    });
    const extent = (resolution: string) => {
      const rows = series.filter((row: { resolution: string }) => row.resolution === resolution);
      return rows.length ? { start: rows.map((row: { start: string }) => row.start).sort()[0], end: rows.map((row: { end: string }) => row.end).sort().at(-1) } : null;
    };
    return Response.json({ station, continuous: extent("continuous"), daily: extent("daily"), series, partial: body.links?.some((link: { rel: string }) => link.rel === "next") ?? false, retrievedAt: new Date().toISOString(), source: url.toString(), message: "Provider-declared record span. Gaps may occur inside it. Daily means do not supply hourly observations." }, { headers: { ...jsonHeaders, "Cache-Control": "public, max-age=3600" } });
  } catch (error) {
    return Response.json({ message: error instanceof Error ? error.message : "USGS coverage unavailable." }, { status: 502, headers: { "Cache-Control": "no-store" } });
  }
}
