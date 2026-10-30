import { fetchDailySummary } from "../../../iem-daily-source";
import { inCdlRegion } from "../../../cropland";
import { kansasStations } from "../../../kansas-stations";
import { nearestStation, parseDailyCsv, seasonDegreeDays, seasonRainfall, seasonDates, lastCompleteStationDate } from "../../../growing-degree-days";

export const dynamic = "force-dynamic";
const DAILY_URL = (station: string, year: number, end: string) => `https://mesonet.agron.iastate.edu/cgi-bin/request/daily.py?network=KS_ASOS&stations=${station}&year1=${year}&month1=4&day1=1&year2=${year}&month2=${Number(end.slice(5, 7))}&day2=${Number(end.slice(8, 10))}&format=csv&var=max_temp_f,min_temp_f,precip_in&na=M`;
const noStore = { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" };
const cacheable = { "Cache-Control": "public, max-age=86400, s-maxage=86400", "X-Content-Type-Options": "nosniff" };

/**
 * Growing degree days for the season (April 1 to October 31) at the nearest Kansas ASOS airport station to a point in or
 * near Kansas, from the Iowa Environmental Mesonet. A complete season is kept a day; a partial one is sent no-store.
 */
export async function GET(request: Request) {
  const params = new URL(request.url).searchParams;
  const lon = Number(params.get("lon")), lat = Number(params.get("lat")), year = Number(params.get("year"));
  const latestYear = new Date().getUTCFullYear();
  if ([...params.keys()].some(key => !["lon", "lat", "year", "v"].includes(key) || params.getAll(key).length !== 1) || params.get("lon") === null || params.get("lat") === null || !inCdlRegion(lon, lat)
    || (params.has("v") && params.get("v") !== "2") || !Number.isInteger(year) || year < 2000 || year > latestYear)
    return Response.json({ state: "error", message: `Choose a point in or near Kansas and a year from 2000 to ${latestYear}.` }, { status: 400, headers: noStore });
  try {
    const station = nearestStation(await kansasStations(`${year}-04-01`, `${year}-10-31`), lon, lat);
    if (station === null) return Response.json({ lon, lat, year, retrievedAt: new Date().toISOString(), state: "none", station: null, degreeDays: null, daysRead: 0, daysMissing: 0, rainInches: null, rainDaysMissing: 0 }, { headers: noStore });
    const retrievedAt = new Date().toISOString();
    const completedThrough = [lastCompleteStationDate(new Date(retrievedAt), station.tzname!), `${year}-10-31`].sort()[0];
    const daysPending = seasonDates(year).filter(date => date > completedThrough).length;
    const sourceUrl = DAILY_URL(station.id, year, completedThrough);
    const daily = completedThrough < `${year}-04-01` ? [] : parseDailyCsv(await fetchDailySummary(sourceUrl), { station: station.id, start: `${year}-04-01`, end: completedThrough });
    const season = seasonDegreeDays(daily, year, completedThrough);
    const rain = seasonRainfall(daily, year, completedThrough);
    const body = {
      lon, lat, year, retrievedAt, contractVersion: 2, completedThrough, daysPending,
      sourceUrl: daily.length ? sourceUrl : null,
      state: season.daysRead > 0 || rain.daysRead > 0 ? "ready" : "none",
      station: { id: station.id, name: station.name, km: Math.round(station.km * 10) / 10, tzname: station.tzname },
      degreeDays: season.daysRead > 0 ? season.degreeDays : null,
      daysRead: season.daysRead, daysMissing: season.daysMissing,
      rainInches: rain.daysRead > 0 ? rain.inches : null, rainDaysMissing: rain.daysMissing, rainTraceDays: rain.traceDays,
    };
    const complete = season.daysRead > 0 && season.daysMissing === 0 && rain.daysMissing === 0 && daysPending === 0;
    return Response.json(body, { headers: complete ? cacheable : noStore });
  } catch {
    return Response.json({ state: "unavailable", message: "The Iowa Environmental Mesonet did not answer for this point. No growing degree days are inferred." }, { status: 502, headers: noStore });
  }
}
