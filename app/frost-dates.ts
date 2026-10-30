/**
 * Frost dates at a clicked point: the last spring freeze and the first fall freeze, from the daily low at the nearest
 * Kansas ASOS airport station. A freeze is a low at or below 32 °F. Stations are points, not fields.
 */
import type { DailyTemperature } from "./growing-degree-days";

export const FROST_F = 32;
const DAY_MS = 86_400_000;

export const FROST_API_PATH = (lon: number, lat: number, year: number) => `/api/farming/frost-dates?lon=${lon.toFixed(5)}&lat=${lat.toFixed(5)}&year=${year}`;

export type FrostDates = Readonly<{
  lon: number;
  lat: number;
  retrievedAt: string;
  year: number;
  state: "ready" | "none";
  station: Readonly<{ id: string; name: string; km: number }> | null;
  lastSpring: string | null;
  firstFall: string | null;
  springKnown: boolean;
  fallKnown: boolean;
  frostFreeDays: number | null;
  daysMissing: number;
}>;

/** Every date of a year, January 1 to December 31, as YYYY-MM-DD. */
export function yearDates(year: number): string[] {
  const dates: string[] = [];
  for (let t = Date.UTC(year, 0, 1); t <= Date.UTC(year, 11, 31); t += DAY_MS) dates.push(new Date(t).toISOString().slice(0, 10));
  return dates;
}

const ms = (date: string) => Date.parse(`${date}T00:00:00Z`);

/**
 * The last freeze before July 1 and the first freeze from July 1 on, up to the day given as today. A date with no reading
 * is missing, and a missing date could hide a freeze: the spring date is known only when no date after it is missing, and the
 * fall date only when no date before it is missing. Dates after today are not yet due, so they are not missing.
 */
export function frostDates(days: readonly DailyTemperature[], year: number, today: string) {
  const byDay = new Map(days.map(day => [day.day, day]));
  const due = yearDates(year).filter(date => date <= today);
  const isFreeze = (date: string) => { const minF = byDay.get(date)?.minF ?? null; return minF !== null && minF <= FROST_F; };
  const isMissing = (date: string) => (byDay.get(date)?.minF ?? null) === null;
  const spring = due.filter(date => date < `${year}-07-01`);
  const fall = due.filter(date => date >= `${year}-07-01`);
  const lastSpring = [...spring].reverse().find(isFreeze) ?? null;
  const firstFall = fall.find(isFreeze) ?? null;
  const springKnown = !spring.some(date => (lastSpring === null || date > lastSpring) && isMissing(date));
  const fallKnown = !fall.some(date => (firstFall === null || date < firstFall) && isMissing(date));
  const frostFreeDays = springKnown && fallKnown && lastSpring !== null && firstFall !== null ? Math.round((ms(firstFall) - ms(lastSpring)) / DAY_MS) : null;
  const daysMissing = due.filter(isMissing).length;
  return { lastSpring, firstFall, springKnown, fallKnown, frostFreeDays, daysMissing };
}

export function validFrostDates(value: unknown, lon: number, lat: number, year: number): value is FrostDates {
  if (!value || typeof value !== "object") return false;
  const v = value as Partial<FrostDates>;
  const station = v.station;
  const date = (d: unknown) => d === null || (typeof d === "string" && /^\d{4}-\d{2}-\d{2}$/.test(d));
  return v.lon === lon && v.lat === lat && v.year === year && (v.state === "ready" || v.state === "none")
    && (station === null || (typeof station === "object" && typeof station.id === "string" && typeof station.name === "string" && typeof station.km === "number"))
    && date(v.lastSpring) && date(v.firstFall) && typeof v.springKnown === "boolean" && typeof v.fallKnown === "boolean"
    && (v.frostFreeDays === null || typeof v.frostFreeDays === "number") && typeof v.daysMissing === "number";
}

const MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
const short = (date: string) => { const [, m, d] = date.split("-"); return `${MONTHS[Number(m) - 1]} ${Number(d)}`; };

/** The frost dates as the dock says them: each freeze, or that it is not certain, and the frost-free days. */
export function frostLine(reading: FrostDates): string | null {
  if (reading.state !== "ready" || reading.station === null) return null;
  const spring = reading.springKnown
    ? (reading.lastSpring ? `last spring freeze ${short(reading.lastSpring)}` : "no spring freeze recorded")
    : "last spring freeze not certain, days missing";
  const fall = reading.fallKnown
    ? (reading.firstFall ? `first fall freeze ${short(reading.firstFall)}` : "no fall freeze yet")
    : "first fall freeze not certain, days missing";
  const free = reading.frostFreeDays === null ? null : `${reading.frostFreeDays} frost-free days`;
  return [spring, fall, free, `from ${reading.station.name}, ${Math.round(reading.station.km)} km away`].filter(Boolean).join(" · ");
}
