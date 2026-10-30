import { fetchDailySummary } from "../../../iem-daily-source";
import { inCdlRegion } from "../../../cropland";
import { kansasStations } from "../../../kansas-stations";
import { nearestStation, parseDailyCsv, lastCompleteStationDate } from "../../../growing-degree-days";
import { frostDates } from "../../../frost-dates";

export const dynamic = "force-dynamic";
const DAILY_URL = (station: string, year: number, end: string) => `https://mesonet.agron.iastate.edu/cgi-bin/request/daily.py?network=KS_ASOS&stations=${station}&year1=${year}&month1=1&day1=1&year2=${year}&month2=${Number(end.slice(5, 7))}&day2=${Number(end.slice(8, 10))}&format=csv&var=max_temp_f,min_temp_f,precip_in&na=M`;
const noStore = { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" };
const cacheable = { "Cache-Control": "public, max-age=86400, s-maxage=604800", "X-Content-Type-Options": "nosniff" };

/**
 * The last spring freeze and the first fall freeze of a year at the nearest Kansas ASOS airport station to a point in or
 * near Kansas, from the Iowa Environmental Mesonet. A finished year with both dates certain is kept a day; anything else is
 * sent no-store.
 */
export async function GET(request: Request) {
  const params = new URL(request.url).searchParams;
  const lon = Number(params.get("lon")), lat = Number(params.get("lat")), year = Number(params.get("year"));
  const latestYear = new Date().getUTCFullYear();
  if ([...params.keys()].some(key => !["lon", "lat", "year"].includes(key)) || params.get("lon") === null || params.get("lat") === null || !inCdlRegion(lon, lat)
    || !Number.isInteger(year) || year < 2000 || year > latestYear)
    return Response.json({ state: "error", message: `Choose a point in or near Kansas and a year from 2000 to ${latestYear}.` }, { status: 400, headers: noStore });
  try {
    const station = nearestStation(await kansasStations(`${year}-01-01`, `${year}-12-31`), lon, lat);
    const retrievedAt = new Date().toISOString();
    if (station === null) return Response.json({ lon, lat, year, retrievedAt, state: "none", station: null, lastSpring: null, firstFall: null, springKnown: true, fallKnown: true, frostFreeDays: null, daysMissing: 0 }, { headers: noStore });
    const completedThrough = [lastCompleteStationDate(new Date(retrievedAt), station.tzname!), `${year}-12-31`].sort()[0];
    const daily = completedThrough < `${year}-01-01` ? [] : parseDailyCsv(await fetchDailySummary(DAILY_URL(station.id, year, completedThrough)), { station: station.id, start: `${year}-01-01`, end: completedThrough });
    const frost = frostDates(daily, year, completedThrough);
    const body = {
      lon, lat, year, retrievedAt, state: "ready",
      station: { id: station.id, name: station.name, km: Math.round(station.km * 10) / 10 },
      ...frost,
    };
    const complete = frost.springKnown && frost.fallKnown && year < latestYear;
    return Response.json(body, { headers: complete ? cacheable : noStore });
  } catch {
    return Response.json({ state: "unavailable", message: "The Iowa Environmental Mesonet did not answer for this point. No frost dates are inferred." }, { status: 502, headers: noStore });
  }
}
