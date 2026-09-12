import { eventDay, EVENT_BOUNDS } from "../../../event-atlas";
import { boundedFetch, jsonHeaders } from "../upstream";
export const dynamic = "force-dynamic";

// Kansas station identifiers verified against NOAA's GHCN-D station inventory.
// Include long-running cooperative stations alongside current airport stations.
const STATIONS = ["USC00142459", "USC00142980", "USC00143093", "USC00143527", "USC00144559", "USC00144972", "USC00148163", "USC00148172", "USC00148826", "USW00003928", "USW00003936", "USW00003997", "USW00013920", "USW00013984", "USW00013985", "USW00013996", "USW00013998", "USW00023064", "USW00023065"];
const numeric = (value: unknown) => typeof value === "string" && value.trim() !== "" && Number.isFinite(Number(value)) ? Number(value) : null;

export async function GET(request: Request) {
  const params = new URL(request.url).searchParams, day = params.get("day") ?? "";
  if (!eventDay(day) || day < "1800-01-01" || day > new Date().toISOString().slice(0,10) || [...params.keys()].some((key) => key !== "day" || params.getAll(key).length !== 1)) return Response.json({ message: "Choose an exact past calendar day." }, { status: 400 });
  const source = new URL("https://www.ncei.noaa.gov/access/services/data/v1");
  source.search = new URLSearchParams({ dataset: "daily-summaries", stations: STATIONS.join(","), startDate: day, endDate: day, dataTypes: "TMAX,TMIN,PRCP", units: "standard", includeStationLocation: "1", includeStationName: "1", includeAttributes: "1", format: "json" }).toString();
  try {
    const rows = JSON.parse((await boundedFetch(source.toString(), 1024 * 1024)).text());
    if (!Array.isArray(rows) || rows.length > STATIONS.length) throw new Error("Unexpected NOAA daily-summary response.");
    const features = rows.flatMap((row) => {
      if (!row || !STATIONS.includes(row.STATION) || row.DATE !== day) throw new Error("NOAA returned a different station or date.");
      const lat = numeric(row.LATITUDE), lon = numeric(row.LONGITUDE);
      if (lat === null || lon === null || lat < EVENT_BOUNDS[1] || lat > EVENT_BOUNDS[3] || lon < EVENT_BOUNDS[0] || lon > EVENT_BOUNDS[2]) return [];
      // Preserve attributes, and withhold any value carrying a NOAA quality flag.
      const value = (code: string) => {
        const flags = typeof row[`${code}_ATTRIBUTES`] === "string" ? row[`${code}_ATTRIBUTES`].split(",") : [];
        const v = numeric(row[code]);
        return flags[1]?.trim() || v === -9999 ? null : v;
      };
      return [{ type: "Feature", id: row.STATION, geometry: { type: "Point", coordinates: [lon,lat] }, properties: { station: row.STATION, name: row.NAME ?? row.STATION, day, maximumF: value("TMAX"), minimumF: value("TMIN"), precipitationInches: value("PRCP"), temperatureAttributes: row.TMAX_ATTRIBUTES ?? null, precipitationAttributes: row.PRCP_ATTRIBUTES ?? null, clock: "Daily station summary; not hourly weather", source: source.toString() } }];
    });
    return Response.json({ data: { type: "FeatureCollection", features }, day, source: source.toString(), retrievedAt: new Date().toISOString(), message: `${features.length} of ${STATIONS.length} selected Kansas stations returned a daily record. Daily maximum/minimum temperature (°F) and precipitation (in). Station observation-day conventions vary; these values are not hourly or county-wide estimates. Flagged or absent values stay missing.` }, { headers: jsonHeaders });
  } catch (error) {
    return Response.json({ message: error instanceof Error ? error.message : "NOAA daily weather unavailable." }, { status: 502, headers: { "Cache-Control": "no-store" } });
  }
}
