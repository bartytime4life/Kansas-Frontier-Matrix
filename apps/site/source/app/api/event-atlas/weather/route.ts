import { eventDay, EVENT_BOUNDS } from "../../../event-atlas";
import { boundedFetch, jsonHeaders } from "../upstream";
export const dynamic = "force-dynamic";

// Kansas station identifiers verified against NOAA's GHCN-D station inventory.
// Include long-running cooperative stations alongside current airport stations.
const STATIONS = ["USC00142459", "USC00142980", "USC00143093", "USC00143527", "USC00144559", "USC00144972", "USC00148163", "USC00148172", "USC00148826", "USW00003928", "USW00003936", "USW00003997", "USW00013920", "USW00013984", "USW00013985", "USW00013996", "USW00013998", "USW00023064", "USW00023065"];
const numeric = (value: unknown) => typeof value === "string" && value.trim() !== "" && Number.isFinite(Number(value)) ? Number(value) : null;
// NOAA GHCN-Daily README: T is trace, P is missing presumed zero; PRCP H
// notes precipitation without a resolved amount and I has no report. A
// nonblank QFLAG means failed QA. Keep source attributes and raw values.
// https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt
const MEASUREMENT_FLAGS = new Set(["", "A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "O", "P", "T", "W"]);
function reading(row: Record<string, unknown>, code: string) {
  const rawValue = typeof row[code] === "string" ? row[code] : null;
  const attributes = typeof row[`${code}_ATTRIBUTES`] === "string" ? row[`${code}_ATTRIBUTES`] as string : null;
  const flags = attributes?.split(",").map(flag => flag.trim());
  const value = numeric(rawValue);
  if (value === null || value === -9999) return { value: null, state: "missing", rawValue, attributes };
  if (flags?.[1]) return { value: null, state: "quality-withheld", rawValue, attributes };
  if (!flags || flags.length < 3 || flags.length > 4 || !MEASUREMENT_FLAGS.has(flags[0])) return { value: null, state: "unqualified", rawValue, attributes };
  if (code === "PRCP" && flags[0] === "H") return { value: null, state: "precipitation-noted", rawValue, attributes };
  if (code === "PRCP" && flags[0] === "I") return { value: null, state: "precipitation-not-reported", rawValue, attributes };
  if (flags[0] === "P") return { value: null, state: "missing-presumed-zero", rawValue, attributes };
  if (flags[0] === "T") return { value: value === 0 && ["PRCP", "SNOW", "SNWD"].includes(code) ? 0 : null,
    state: value === 0 && ["PRCP", "SNOW", "SNWD"].includes(code) ? "trace" : "unqualified", rawValue, attributes };
  return { value, state: "reported", rawValue, attributes };
}

export async function GET(request: Request) {
  const params = new URL(request.url).searchParams, day = params.get("day") ?? "";
  if (!eventDay(day) || day < "1800-01-01" || day > new Date().toISOString().slice(0,10) || [...params.keys()].some((key) => key !== "day" || params.getAll(key).length !== 1)) return Response.json({ message: "Choose an exact past calendar day." }, { status: 400 });
  const source = new URL("https://www.ncei.noaa.gov/access/services/data/v1");
  source.search = new URLSearchParams({ dataset: "daily-summaries", stations: STATIONS.join(","), startDate: day, endDate: day, dataTypes: "TMAX,TMIN,PRCP,SNOW,SNWD", units: "standard", includeStationLocation: "1", includeStationName: "1", includeAttributes: "1", format: "json" }).toString();
  try {
    const rows = JSON.parse((await boundedFetch(source.toString(), 1024 * 1024)).text());
    if (!Array.isArray(rows) || rows.length > STATIONS.length) throw new Error("Unexpected NOAA daily-summary response.");
    const features = rows.flatMap((row) => {
      if (!row || !STATIONS.includes(row.STATION) || row.DATE !== day) throw new Error("NOAA returned a different station or date.");
      const lat = numeric(row.LATITUDE), lon = numeric(row.LONGITUDE);
      if (lat === null || lon === null || lat < EVENT_BOUNDS[1] || lat > EVENT_BOUNDS[3] || lon < EVENT_BOUNDS[0] || lon > EVENT_BOUNDS[2]) return [];
      const maximum = reading(row, "TMAX"), minimum = reading(row, "TMIN"), precipitation = reading(row, "PRCP"), snow = reading(row, "SNOW"), depth = reading(row, "SNWD");
      return [{ type: "Feature", id: row.STATION, geometry: { type: "Point", coordinates: [lon,lat] }, properties: {
        station: row.STATION, name: row.NAME ?? row.STATION, day,
        maximumF: maximum.value, maximumFState: maximum.state, maximumFRawValue: maximum.rawValue,
        minimumF: minimum.value, minimumFState: minimum.state, minimumFRawValue: minimum.rawValue,
        precipitationInches: precipitation.value, precipitationInchesState: precipitation.state, precipitationInchesRawValue: precipitation.rawValue,
        snowfallInches: snow.value, snowfallInchesState: snow.state, snowfallInchesRawValue: snow.rawValue,
        snowDepthInches: depth.value, snowDepthInchesState: depth.state, snowDepthInchesRawValue: depth.rawValue,
        temperatureAttributes: maximum.attributes, minimumTemperatureAttributes: minimum.attributes,
        precipitationAttributes: precipitation.attributes, snowAttributes: snow.attributes, snowDepthAttributes: depth.attributes,
        clock: "Daily station summary; not hourly weather", source: source.toString(),
      } }];
    });
    return Response.json({ data: { type: "FeatureCollection", features }, day, source: source.toString(), retrievedAt: new Date().toISOString(), message: `${features.length} of ${STATIONS.length} selected Kansas stations returned a daily record. Daily maximum/minimum temperature (°F), precipitation, snowfall and snow depth (in). Station observation-day conventions vary; these values are not hourly or county-wide estimates. Trace amounts are qualified, not measured zeros; missing, presumed-zero, quality-flagged or unqualified values are withheld. Raw values and provider attributes remain attached.` }, { headers: jsonHeaders });
  } catch (error) {
    return Response.json({ message: error instanceof Error ? error.message : "NOAA daily weather unavailable." }, { status: 502, headers: { "Cache-Control": "no-store" } });
  }
}
