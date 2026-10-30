import { boundedFetch } from "../../event-atlas/upstream";
import { inCdlRegion } from "../../../cropland";
import { kansasStations } from "../../../kansas-stations";
import { nearestStation, parseDailyCsv, seasonRainfall } from "../../../growing-degree-days";
import { normalYears, percentOfNormal, rainNormal, type YearRain } from "../../../rain-normal";

export const dynamic = "force-dynamic";
const DAILY_URL = (station: string, year: number) => `https://mesonet.agron.iastate.edu/cgi-bin/request/daily.py?network=KS_ASOS&stations=${station}&year1=${year}&month1=4&day1=1&year2=${year}&month2=10&day2=31&format=csv`;
const MAX_BYTES = 512 * 1024;
/** The prior years are read a few at a time, so one click does not open a dozen requests to the Mesonet at once. */
const READ_AT_ONCE = 3;
const KEPT_SEASONS = 500;
const noStore = { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" };
type Season = Readonly<{ inches: number | null; daysMissing: number }>;
/** Only a season with every day read is kept: it does not change once the season is over. */
const seasons = new Map<string, Season>();

async function seasonFor(stationId: string, year: number): Promise<Season> {
  const key = `${stationId}:${year}`;
  const kept = seasons.get(key);
  if (kept) return kept;
  const daily = parseDailyCsv(await boundedFetch(DAILY_URL(stationId, year), MAX_BYTES, { timeoutMs: 15_000 }).then(response => response.text()));
  const rain = seasonRainfall(daily, year);
  // A season with no rain read at all is no total, not a total of zero.
  const season = { inches: rain.daysRead > 0 ? rain.inches : null, daysMissing: rain.daysMissing };
  if (rain.daysMissing === 0) {
    if (seasons.size >= KEPT_SEASONS) seasons.delete(seasons.keys().next().value!);
    seasons.set(key, season);
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
    const station = nearestStation(await kansasStations(), lon, lat);
    const retrievedAt = new Date().toISOString();
    if (station === null) return Response.json({ lon, lat, year, retrievedAt, state: "none", station: null, seasonInches: null, seasonDaysMissing: 0, normal: { average: null, years: 0 }, percentOfNormal: null }, { headers: noStore });
    const current = await seasonFor(station.id, year);
    const prior: YearRain[] = [];
    const years = normalYears(year);
    for (let i = 0; i < years.length; i += READ_AT_ONCE) {
      prior.push(...await Promise.all(years.slice(i, i + READ_AT_ONCE).map(async y => {
        try {
          const season = await seasonFor(station.id, y);
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
      seasonInches: current.inches, seasonDaysMissing: current.daysMissing, normal,
      percentOfNormal: current.inches !== null && current.daysMissing === 0 ? percentOfNormal(current.inches, normal.average) : null,
    }, { headers: noStore });
  } catch {
    return Response.json({ state: "unavailable", message: "The Iowa Environmental Mesonet did not answer for this point. No rain normal is inferred." }, { status: 502, headers: noStore });
  }
}
