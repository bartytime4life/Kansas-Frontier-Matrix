import { fetchDailySummary } from "../../../iem-daily-source";
import { inCdlRegion } from "../../../cropland";
import { kansasStations } from "../../../kansas-stations";
import { nearestStation, parseDailyCsv, seasonRainfall, seasonDates, lastCompleteStationDate, type Station } from "../../../growing-degree-days";
import { normalYears, percentOfNormal, rainNormal, type YearRain } from "../../../rain-normal";

export const dynamic = "force-dynamic";
const DAILY_URL = (station: string, year: number, end: string) => `https://mesonet.agron.iastate.edu/cgi-bin/request/daily.py?network=KS_ASOS&stations=${station}&year1=${year}&month1=4&day1=1&year2=${year}&month2=${Number(end.slice(5, 7))}&day2=${Number(end.slice(8, 10))}&format=csv&var=max_temp_f,min_temp_f,precip_in&na=M`;
/** All three Field weather consumers use the same sequential IEM request queue. */
const READ_AT_ONCE = 1;
const KEPT_SEASONS = 500;
const noStore = { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" };
async function seasonFor(station: Station, year: number): Promise<Season> {
  const stationId = station.id;
  const key = `${stationId}:${year}`;
  const kept = seasons.get(key);
    if (seasons.size >= KEPT_SEASONS) seasons.delete(seasons.keys().next().value!);
    seasons.set(key, { at: Date.now(), season });
  }
  return season;
}

/**
 * The season's rain at the nearest Kansas ASOS station for the year asked for, against the average of the ten years before it.
 * A prior year that cannot be read, or has a missing day, is left out of the average rather than guessed.
 */
export async function GET(request: Request) {
  const params = new URL(request.url).searchParams;
  const lon = Number(params.get("lon")), lat = Number(params.get("lat")), year = Number(params.get("year"));
  const latestYear = new Date().getUTCFullYear();
  if ([...params.keys()].some(key => !["lon", "lat", "year"].includes(key)) || params.get("lon") === null || params.get("lat") === null || !inCdlRegion(lon, lat)
    || !Number.isInteger(year) || year < 2000 || year > latestYear)
    return Response.json({ state: "error", message: `Choose a point in or near Kansas and a year from 2000 to ${latestYear}.` }, { status: 400, headers: noStore });
  try {
    const station = nearestStation(await kansasStations(`${year}-04-01`, `${year}-10-31`), lon, lat);
    const retrievedAt = new Date().toISOString();
    if (station === null) return Response.json({ lon, lat, year, retrievedAt, state: "none", station: null, seasonInches: null, seasonDaysMissing: 0, normal: { average: null, years: 0 }, percentOfNormal: null }, { headers: noStore });
    const current = await seasonFor(station, year);
    if (current.inches === null) return Response.json({ lon, lat, year, retrievedAt, state: "none", station: { id: station.id, name: station.name, km: Math.round(station.km * 10) / 10 }, seasonInches: null, seasonDaysMissing: current.daysMissing, seasonDaysPending: current.daysPending, seasonTraceDays: 0, normal: { average: null, years: 0 }, percentOfNormal: null }, { headers: noStore });
    const prior: YearRain[] = [];
    const years = normalYears(year);
    for (let i = 0; i < years.length; i += READ_AT_ONCE) {
      prior.push(...await Promise.all(years.slice(i, i + READ_AT_ONCE).map(async y => {
        try {
          if (station.archiveBegin! > `${y}-10-31` || (station.archiveEnd !== null && station.archiveEnd! < `${y}-04-01`)) return { year: y, inches: null, daysMissing: 214 };
          const season = await seasonFor(station, y);
          return { year: y, inches: season.inches, daysMissing: season.daysMissing };
        } catch {
          return { year: y, inches: null, daysMissing: 1 };
        }
      })));
    }
    const normal = rainNormal(prior);
    return Response.json({
      lon, lat, year, retrievedAt, state: "ready",
      station: { id: station.id, name: station.name, km: Math.round(station.km * 10) / 10 },
    }, { headers: noStore });
  } catch {
    return Response.json({ state: "unavailable", message: "The Iowa Environmental Mesonet did not answer for this point. No rain normal is inferred." }, { status: 502, headers: noStore });
  }
}
