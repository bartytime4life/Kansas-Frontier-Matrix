import { boundedFetch } from "../../event-atlas/upstream";
import { inCdlRegion } from "../../../cropland";
import { nearestStation, parseDailyCsv, seasonDegreeDays, type Station } from "../../../growing-degree-days";

export const dynamic = "force-dynamic";
const STATIONS_URL = "https://mesonet.agron.iastate.edu/geojson/network/KS_ASOS.geojson";
const DAILY_URL = (station: string, year: number) => `https://mesonet.agron.iastate.edu/cgi-bin/request/daily.py?network=KS_ASOS&stations=${station}&year1=${year}&month1=4&day1=1&year2=${year}&month2=10&day2=31&format=csv`;
const MAX_BYTES = 512 * 1024;
const DAY_MS = 24 * 60 * 60 * 1000;
const noStore = { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" };
const cacheable = { "Cache-Control": "public, max-age=86400, s-maxage=604800", "X-Content-Type-Options": "nosniff" };
let stationList: { at: number; stations: Station[] } | null = null;

/** The Kansas ASOS stations with their identifiers and positions, kept a day. */
async function kansasStations(): Promise<Station[]> {
  if (stationList && Date.now() - stationList.at < DAY_MS) return stationList.stations;
  const data = JSON.parse((await boundedFetch(STATIONS_URL, MAX_BYTES, { timeoutMs: 15_000 })).text()) as { features?: unknown };
  const stations: Station[] = [];
  for (const feature of Array.isArray(data.features) ? data.features : []) {
    const f = feature as { properties?: { sid?: unknown; sname?: unknown }; geometry?: { coordinates?: unknown } };
    const [lon, lat] = Array.isArray(f.geometry?.coordinates) ? f.geometry.coordinates : [];
    const id = f.properties?.sid;
    if (typeof id !== "string" || !/^[A-Za-z0-9]{3,5}$/.test(id) || typeof lon !== "number" || typeof lat !== "number") continue;
    stations.push({ id, name: typeof f.properties?.sname === "string" ? f.properties.sname : id, lon, lat });
  }
  if (stations.length === 0) throw new Error("No stations in the network.");
  stationList = { at: Date.now(), stations };
  return stations;
}

/**
 * Growing degree days for the season (April 1 to October 31) at the nearest Kansas ASOS airport station to a point in or
 * near Kansas, from the Iowa Environmental Mesonet. A complete season is kept a day; a partial one is sent no-store.
 */
export async function GET(request: Request) {
  const params = new URL(request.url).searchParams;
  const lon = Number(params.get("lon")), lat = Number(params.get("lat")), year = Number(params.get("year"));
  const latestYear = new Date().getUTCFullYear();
  if ([...params.keys()].some(key => !["lon", "lat", "year"].includes(key)) || params.get("lon") === null || params.get("lat") === null || !inCdlRegion(lon, lat)
    || !Number.isInteger(year) || year < 2000 || year > latestYear)
    return Response.json({ state: "error", message: `Choose a point in or near Kansas and a year from 2000 to ${latestYear}.` }, { status: 400, headers: noStore });
  try {
    const station = nearestStation(await kansasStations(), lon, lat);
    if (station === null) return Response.json({ lon, lat, year, retrievedAt: new Date().toISOString(), state: "none", station: null, degreeDays: null, daysRead: 0, daysMissing: 0 }, { headers: noStore });
    const season = seasonDegreeDays(parseDailyCsv(await boundedFetch(DAILY_URL(station.id, year), MAX_BYTES, { timeoutMs: 15_000 }).then(response => response.text())));
    const body = {
      lon, lat, year, retrievedAt: new Date().toISOString(),
      state: season.daysRead > 0 ? "ready" : "none",
      station: { id: station.id, name: station.name, km: Math.round(station.km * 10) / 10 },
      degreeDays: season.daysRead > 0 ? season.degreeDays : null,
      daysRead: season.daysRead, daysMissing: season.daysMissing,
    };
    const complete = season.daysRead > 0 && season.daysMissing === 0;
    return Response.json(body, { headers: complete ? cacheable : noStore });
  } catch {
    return Response.json({ state: "unavailable", message: "The Iowa Environmental Mesonet did not answer for this point. No growing degree days are inferred." }, { status: 502, headers: noStore });
  }
}
