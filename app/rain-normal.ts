/**
 * Season rain against normal at a clicked point: the April 1 to October 31 rain at the nearest Kansas ASOS station for the year
 * on show, against the average of the ten years before it. A year counts only when every day in it was read. Stations are
 * points; the reading is the station's, and rain varies across a county.
 */

export const NORMAL_YEARS = 10;
/** Fewer complete years than this and no normal is read. */
export const NORMAL_MIN_YEARS = 5;

export const RAIN_NORMAL_API_PATH = (lon: number, lat: number, year: number) => `/api/farming/rain-normal?lon=${lon.toFixed(5)}&lat=${lat.toFixed(5)}&year=${year}`;

/** The years the normal is averaged over: the ten years before the year on show. */
export function normalYears(year: number): number[] {
  return Array.from({ length: NORMAL_YEARS }, (_, i) => year - NORMAL_YEARS + i);
}

export type YearRain = Readonly<{ year: number; inches: number | null; daysMissing: number }>;

/** The normal: the average over the years with every day read, or none when there are too few such years. */
export function rainNormal(years: readonly YearRain[]): Readonly<{ average: number | null; years: number }> {
  const complete = years.filter(y => y.inches !== null && y.daysMissing === 0);
  if (complete.length < NORMAL_MIN_YEARS) return { average: null, years: complete.length };
  const total = complete.reduce((sum, y) => sum + (y.inches ?? 0), 0);
  return { average: Math.round((total / complete.length) * 100) / 100, years: complete.length };
}

/** The season's rain as a percentage of the normal, or null without a normal or a complete season. */
export function percentOfNormal(inches: number, average: number | null): number | null {
  return average === null || average <= 0 ? null : Math.round((inches / average) * 100);
}

export type RainNormalReading = Readonly<{
  lon: number;
  lat: number;
  retrievedAt: string;
  year: number;
  state: "ready" | "none";
  station: Readonly<{ id: string; name: string; km: number }> | null;
  seasonInches: number | null;
  seasonDaysMissing: number;
  seasonDaysPending?: number;
  seasonTraceDays?: number;
  normal: Readonly<{ average: number | null; years: number }>;
  percentOfNormal: number | null;
}>;

export function validRainNormal(value: unknown, lon: number, lat: number, year: number): value is RainNormalReading {
  if (!value || typeof value !== "object") return false;
  const v = value as Partial<RainNormalReading>;
  const station = v.station;
  const normal = v.normal;
  const count = (n: unknown, max: number): n is number => typeof n === "number" && Number.isInteger(n) && n >= 0 && n <= max;
  const amount = (n: unknown): n is number => typeof n === "number" && Number.isFinite(n) && n >= 0;
  const pending = v.seasonDaysPending ?? 0, traces = v.seasonTraceDays ?? 0;
  if (v.lon !== lon || v.lat !== lat || v.year !== year || !["ready", "none"].includes(v.state ?? "")
    || typeof v.retrievedAt !== "string" || !Number.isFinite(Date.parse(v.retrievedAt))
    || !count(v.seasonDaysMissing, 214) || !count(pending, 214) || !count(traces, 214)
    || v.seasonDaysMissing + pending + traces > 214
    || (station !== null && (!station || !/^[A-Z0-9]{2,5}$/.test(station.id) || typeof station.name !== "string" || !station.name.trim() || !amount(station.km) || station.km > 150))
    || (v.seasonInches !== null && !amount(v.seasonInches)) || !normal || !count(normal.years, NORMAL_YEARS)
    || (normal.average !== null && (!amount(normal.average) || normal.years < NORMAL_MIN_YEARS))
    || (v.percentOfNormal !== null && (!count(v.percentOfNormal, Number.MAX_SAFE_INTEGER) || !normal.average || v.seasonDaysMissing > 0 || pending > 0))) return false;
  return v.state === "ready" ? station !== null && v.seasonInches !== null : v.seasonInches === null && v.percentOfNormal === null;
}

/** The season against normal as the dock says it, or null when there is no season reading. */
export function rainNormalLine(reading: RainNormalReading): string | null {
  if (reading.state !== "ready" || reading.station === null || reading.seasonInches === null) return null;
  const season = `${reading.seasonDaysMissing || reading.seasonDaysPending ? "Partial: " : ""}${reading.seasonInches.toFixed(2)} in precipitation${reading.seasonTraceDays ? ` + trace on ${reading.seasonTraceDays} days` : ""}, Apr 1–Oct 31 ${reading.year}`;
  const days = `${reading.seasonDaysMissing ? ` (${reading.seasonDaysMissing} days missing)` : ""}${reading.seasonDaysPending ? ` (${reading.seasonDaysPending} days not yet due)` : ""}`;
  if (reading.normal.average === null) return `${season}${days} · no earlier-year average: ${reading.normal.years} of ${NORMAL_YEARS} earlier years are complete, and ${NORMAL_MIN_YEARS} are needed`;
  const share = reading.percentOfNormal === null || reading.seasonDaysMissing > 0 || (reading.seasonDaysPending ?? 0) > 0 ? "" : ` · ${reading.percentOfNormal}% of earlier-year average`;
  return `${season}${days} · ${reading.normal.years}-year average ${reading.normal.average.toFixed(2)} in${share} · from ${reading.station.name}, ${Math.round(reading.station.km)} km away`;
}

/** Ten earlier station seasons, in calendar order. Null records a gap or an incomplete season. */
export type SeasonHistory = Readonly<{
  year: number; inches: number | null;
}>;
export type RainOutlook = Readonly<{
  year: number; lon: number; lat: number; station: { id:string; name:string; km:number };
  retrievedAt:string; history: readonly SeasonHistory[];
}>;

export function validOutlook(value: unknown, lon: number, lat: number, year: number): value is RainOutlook {
  const v = value as RainOutlook | null;
  return !!v && v.lon === lon && v.lat === lat && v.year === year && !!v.station &&
    /^[A-Z0-9]{3,5}$/.test(v.station.id) && typeof v.station.name === "string" && v.station.name.length > 0 &&
    Number.isFinite(v.station.km) && v.station.km >= 0 && v.station.km <= 150 &&
    Number.isFinite(Date.parse(v.retrievedAt)) && Array.isArray(v.history) && v.history.length === NORMAL_YEARS &&
    v.history.every((r,i) => r && r.year === year-NORMAL_YEARS+i &&
      (r.inches === null || typeof r.inches === "number" && Number.isFinite(r.inches) && r.inches >= 0));
}

/** Expanding-window hindcast: each test season sees only earlier complete seasons. */
export function rainBaseline(history: readonly SeasonHistory[]) {
  const amounts: number[] = [];
  const errors: number[] = [];
  const median = (sorted: number[]) => (sorted[Math.floor((sorted.length-1)/2)] + sorted[Math.floor(sorted.length/2)]) / 2;
  for (const season of history) {
    if (season.inches === null) continue;
    if (amounts.length >= NORMAL_MIN_YEARS) errors.push(Math.abs(median(amounts) - season.inches));
    amounts.push(season.inches);
    amounts.sort((a,b) => a-b);
  }
  if (amounts.length < NORMAL_MIN_YEARS) return null;
  return { median:median(amounts), min:amounts[0], max:amounts[amounts.length-1], count:amounts.length,
    hindcasts:errors.length, mae:errors.length ? errors.reduce((sum,x)=>sum+x,0)/errors.length : null };
}
