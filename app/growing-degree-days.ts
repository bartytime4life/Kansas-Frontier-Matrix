/**
 * Growing degree days at a clicked point: the warmth a season gives a crop, from the daily high and low at the nearest
 * Kansas ASOS airport station. Stations are points, not fields; the reading is the station's, and it varies across a county.
 */

/** Corn's base temperature: growth is counted above 50 °F and the day's high and low are capped at 86 °F. */
export const GDD_BASE_F = 50;
export const GDD_CAP_F = 86;
/** The season the reading covers: April 1 to October 31 of the chosen year. */
export const GDD_SEASON_LABEL = "Apr 1–Oct 31";
/** The longest distance from a click to a station that still gives a reading. */
export const GDD_MAX_KM = 150;

export const GDD_API_PATH = (lon: number, lat: number, year: number) => `/api/farming/degree-days?lon=${lon.toFixed(5)}&lat=${lat.toFixed(5)}&year=${year}`;

export type DailyTemperature = Readonly<{ day: string; maxF: number | null; minF: number | null; precipIn?: number | null }>;
export type Station = Readonly<{ id: string; name: string; lon: number; lat: number }>;

/** One day's degree days: the high capped and the low floored at the base, averaged, less the base, never negative. */
export function dailyDegreeDays(maxF: number | null, minF: number | null): number | null {
  if (maxF === null || minF === null) return null;
  const high = Math.min(maxF, GDD_CAP_F), low = Math.max(minF, GDD_BASE_F);
  return Math.max(0, (high + low) / 2 - GDD_BASE_F);
}

/** Every date of the season, April 1 to October 31 of a year, as YYYY-MM-DD. */
export function seasonDates(year: number): string[] {
  const dates: string[] = [];
  for (let t = Date.UTC(year, 3, 1); t <= Date.UTC(year, 9, 31); t += 86_400_000) dates.push(new Date(t).toISOString().slice(0, 10));
  return dates;
}

/**
 * The season's total. Every date of the season is counted: a date with no row, or a row with a missing reading, is missing and
 * not guessed. A season is complete only when no date is missing.
 */
export function seasonDegreeDays(days: readonly DailyTemperature[], year: number) {
  const byDay = new Map(days.map(day => [day.day, day]));
  let total = 0, daysRead = 0, daysMissing = 0;
  for (const date of seasonDates(year)) {
    const day = byDay.get(date);
    const value = day ? dailyDegreeDays(day.maxF, day.minF) : null;
    if (value === null) { daysMissing++; continue; }
    total += value; daysRead++;
  }
  return { degreeDays: Math.round(total), daysRead, daysMissing };
}

/**
 * The season's rainfall in inches. Every date of the season is counted: a date with no row, or a blank reading, is missing.
 * The rain is read only when the summary has a precipitation column; without one every date is missing.
 */
export function seasonRainfall(days: readonly DailyTemperature[], year: number) {
  const byDay = new Map(days.map(day => [day.day, day]));
  let inches = 0, daysRead = 0, daysMissing = 0;
  for (const date of seasonDates(year)) {
    const value = byDay.get(date)?.precipIn ?? null;
    if (value === null) { daysMissing++; continue; }
    inches += value; daysRead++;
  }
  return { inches: Math.round(inches * 100) / 100, daysRead, daysMissing };
}

/**
 * The daily summary CSV from the Iowa Environmental Mesonet, read by its header names. A missing reading is "M" or blank.
 * Throws when the temperature columns are absent, so an unexpected answer is not read as an empty season.
 */
export function parseDailyCsv(text: string): DailyTemperature[] {
  const lines = text.split(/\r?\n/).filter(line => line.trim() !== "");
  if (lines.length === 0) throw new Error("Empty daily summary.");
  const header = lines[0].split(",").map(name => name.trim());
  const day = header.indexOf("day"), max = header.indexOf("max_temp_f"), min = header.indexOf("min_temp_f"), precip = header.indexOf("precip_in");
  if (day < 0 || max < 0 || min < 0) throw new Error("Unrecognised daily summary columns.");
  const number = (cell: string | undefined) => {
    if (cell === undefined || cell.trim() === "" || cell.trim() === "M") return null;
    const value = Number(cell);
    return Number.isFinite(value) ? value : null;
  };
  return lines.slice(1).map(line => {
    const cells = line.split(",");
    return { day: (cells[day] ?? "").trim(), maxF: number(cells[max]), minF: number(cells[min]), precipIn: precip < 0 ? null : number(cells[precip]) };
  });
}

/** Great-circle distance in kilometres. */
export function distanceKm(lon1: number, lat1: number, lon2: number, lat2: number): number {
  const toRad = (degrees: number) => degrees * Math.PI / 180;
  const a = Math.sin(toRad(lat2 - lat1) / 2) ** 2 + Math.cos(toRad(lat1)) * Math.cos(toRad(lat2)) * Math.sin(toRad(lon2 - lon1) / 2) ** 2;
  return 2 * 6371 * Math.asin(Math.sqrt(a));
}

/** The station nearest the point, with its distance, if it lies within the reach of a reading. */
export function nearestStation(stations: readonly Station[], lon: number, lat: number): (Station & { km: number }) | null {
  let best: (Station & { km: number }) | null = null;
  for (const station of stations) {
    const km = distanceKm(lon, lat, station.lon, station.lat);
    if (best === null || km < best.km) best = { ...station, km };
  }
  return best !== null && best.km <= GDD_MAX_KM ? best : null;
}

export type DegreeDaysReading = Readonly<{
  lon: number;
  lat: number;
  retrievedAt: string;
  year: number;
  state: "ready" | "none";
  station: Readonly<{ id: string; name: string; km: number }> | null;
  degreeDays: number | null;
  daysRead: number;
  daysMissing: number;
  rainInches: number | null;
  rainDaysMissing: number;
}>;

export function validDegreeDays(value: unknown, lon: number, lat: number, year: number): value is DegreeDaysReading {
  if (!value || typeof value !== "object") return false;
  const v = value as Partial<DegreeDaysReading>;
  const station = v.station;
  return v.lon === lon && v.lat === lat && v.year === year && (v.state === "ready" || v.state === "none")
    && (station === null || (typeof station === "object" && typeof station.id === "string" && typeof station.name === "string" && typeof station.km === "number"))
    && (v.degreeDays === null || typeof v.degreeDays === "number") && typeof v.daysRead === "number" && typeof v.daysMissing === "number"
    && (v.rainInches === null || typeof v.rainInches === "number") && typeof v.rainDaysMissing === "number";
}

/** The season's rain as the dock says it, or null when no rain was read. */
export function rainLine(reading: DegreeDaysReading): string | null {
  if (reading.state !== "ready" || reading.rainInches === null) return null;
  const days = reading.rainDaysMissing === 0 ? "every day read" : `${reading.rainDaysMissing} days missing`;
  return `${reading.rainInches.toFixed(2)} in of rain, ${GDD_SEASON_LABEL} ${reading.year} · ${days}`;
}

/** The reading as the dock says it: the total, the season, the station, and how many days were read. */
export function degreeDaysLine(reading: DegreeDaysReading): string | null {
  if (reading.state !== "ready" || reading.degreeDays === null || reading.station === null) return null;
  const total = reading.degreeDays.toLocaleString("en-US");
  const days = reading.daysMissing === 0 ? `${reading.daysRead} days read` : `${reading.daysRead} days read, ${reading.daysMissing} missing`;
  return `${total} growing degree days, base 50 °F, capped at 86 °F, ${GDD_SEASON_LABEL} ${reading.year} · from ${reading.station.name}, ${Math.round(reading.station.km)} km away · ${days}`;
}
