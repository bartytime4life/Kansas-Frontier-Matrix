import { eventInterval, intervalDays, parseRadarDirectory, radarDirectory, parseSmokeKml, smokeUrl, imageryDomainUrl, domainIncludes, type EventManifest, type RadarScan, type SmokeCollection } from "../../../event-atlas";
import { boundedFetch, jsonHeaders } from "../upstream";
export const dynamic = "force-dynamic";

export async function GET(request: Request) {
  const url = new URL(request.url);
  try {
    for (const key of url.searchParams.keys()) if (!["start", "hours"].includes(key) || url.searchParams.getAll(key).length !== 1) throw new Error("Unsupported or repeated query parameter.");
    const { start, end } = eventInterval(url.searchParams.get("start") ?? "", Number(url.searchParams.get("hours")));
    const days = intervalDays(start, end);
    const smokeDays = [new Date(Date.parse(days[0]) - 86_400_000).toISOString().slice(0,10), ...days];
    const radarGaps: string[] = [], smokeGaps: string[] = [], scans: RadarScan[] = [];
    const smoke: SmokeCollection = { type: "FeatureCollection", features: [] };
    const imageryDates: string[] = [];
    await Promise.all([
      ...days.map(async (day) => {
        if (day < "1995-01-01") { radarGaps.push(day); return; }
        try {
          const body = await boundedFetch(radarDirectory(day), 1024 * 1024);
          scans.push(...parseRadarDirectory(body.text(), day, start, end));
        } catch { radarGaps.push(day); }
      }),
      ...smokeDays.map(async (day) => {
        if (day < "2005-08-05") { smokeGaps.push(day); return; }
        try {
          const body = await boundedFetch(smokeUrl(day), 2 * 1024 * 1024);
          smoke.features.push(...parseSmokeKml(body.text(), smokeUrl(day)).features.filter((f) => f.properties.start < end && f.properties.end > start));
        } catch { smokeGaps.push(day); }
      }),
      ...days.map(async (day) => {
        if (day < "2000-02-24") return;
        try {
          const body = await boundedFetch(imageryDomainUrl(day), 32_768);
          if (domainIncludes(body.text(), day)) imageryDates.push(day);
        } catch { /* Exact date is withheld without an availability confirmation. */ }
      }),
    ]);
    scans.sort((a,b) => a.time.localeCompare(b.time));
    // Neighboring daily publications can contain the same observation.
    const seen = new Set<string>();
    smoke.features = smoke.features.filter((f) => {
      const key = JSON.stringify([f.properties.start, f.properties.end, f.properties.density, f.geometry]);
      if (seen.has(key)) return false; seen.add(key); return true;
    });
    const manifest: EventManifest = {
      format: "kfm-event-atlas-v1", start, end, retrievedAt: new Date().toISOString(), evidenceRole: "EXTERNAL_CONTEXT_ONLY",
      radar: { state: radarGaps.length ? "partial" : scans.length ? "ready" : "empty", scans, gaps: radarGaps.sort(), message: "NOAA/NWS observations mosaicked by Iowa State IEM. Exact archive artifacts; 5-minute mosaic slots can contain radar inputs up to 15 minutes old. Blank pixels do not prove no precipitation." },
      smoke: { state: smokeGaps.length ? "partial" : smoke.features.length ? "ready" : "empty", data: smoke, gaps: smokeGaps.sort(), message: "NOAA HMS satellite-analyzed smoke extent, only within supplied Start/End intervals. Qualitative column density, not surface PM2.5, altitude, or measured transport. Missing polygons do not prove clear air." },
      imagery: { dates: imageryDates.sort(), message: "NASA Terra MODIS daily acquisition mosaic, not an intraday image or historical roads/boundaries map. Cloud and coverage gaps remain." },
    };
    return Response.json(manifest, { headers: jsonHeaders });
  } catch (error) {
    return Response.json({ message: error instanceof Error ? error.message : "Invalid interval." }, { status: 400, headers: { "Cache-Control": "no-store" } });
  }
}
