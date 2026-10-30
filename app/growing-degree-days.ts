/**
 * Growing degree days at a clicked point: the warmth a season gives a crop, from the daily high and low at the nearest
 * Kansas ASOS airport station. Stations are points, not fields; the reading is the station's, and it varies across a county.
 */

/** Corn's base temperature: growth is counted above 50 °F and the high is capped at 86 °F and low floored at 50 °F. */
export const GDD_BASE_F = 50;
export const GDD_CAP_F = 86;
/** The season the reading covers: April 1 to October 31 of the chosen year. */
export const GDD_SEASON_LABEL = "Apr 1–Oct 31";
/** The longest distance from a click to a station that still gives a reading. */
export const GDD_MAX_KM = 150;

export const GDD_API_PATH = (lon: number, lat: number, year: number) => `/api/farming/degree-days?lon=${lon.toFixed(5)}&lat=${lat.toFixed(5)}&year=${year}&v=2`;

export type DailyTemperature = Readonly<{ day: string; maxF: number | null; minF: number | null; precipIn?: number | null }>;
export type Station = Readonly<{ id: string; name: string; lon: number; lat: number; tzname?: string; archiveBegin?: string; archiveEnd?: string | null }>;

/** One day's degree days: the high capped and the low floored at the base, averaged, less the base, never negative. */
export function dailyDegreeDays(maxF: number | null, minF: number | null): number | null {
  if (maxF === null || minF === null || !Number.isFinite(maxF) || !Number.isFinite(minF) || maxF < minF) return null;
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
export function seasonDegreeDays(days: readonly DailyTemperature[], year: number, through = `${year}-10-31`) {
  const byDay = new Map(days.map(day => [day.day, day]));
  let total = 0, daysRead = 0, daysMissing = 0;
  for (const date of seasonDates(year).filter(date => date <= through)) {
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
export function seasonRainfall(days: readonly DailyTemperature[], year: number, through = `${year}-10-31`) {
  const byDay = new Map(days.map(day => [day.day, day]));
  let inches = 0, daysRead = 0, daysMissing = 0, traceDays = 0;
  for (const date of seasonDates(year).filter(date => date <= through)) {
    const value = byDay.get(date)?.precipIn ?? null;
    if (value === null || !Number.isFinite(value) || value < 0) { daysMissing++; continue; }
    // IEM 0.0001 is a categorical trace sentinel, not a measured depth.
    if (value === 0.0001) traceDays++; else inches += value;
    daysRead++;
  }
  return { inches: Math.round(inches * 100) / 100, daysRead, daysMissing, traceDays };
}

/**
 * The daily summary CSV from the Iowa Environmental Mesonet, read by its header names. A missing reading is "M" or blank.
 * Throws when the temperature columns are absent, so an unexpected answer is not read as an empty season.
 */
export function parseDailyCsv(text: string, expected?: { station: string; start: string; end: string }): DailyTemperature[] {
  const lines = text.replace(/^\uFEFF/, "").split(/\r?\n/).filter(line => line.trim() !== "");
  if (lines.length === 0) throw new Error("Empty daily summary.");
  // Selected IEM fields are scalar identifiers, ISO dates and numbers. Quoted fields
  // are accepted, but extra/malformed columns must not shift observations silently.
  const cellsOf = (line: string) => line.split(",").map(cell => cell.trim().replace(/^"([^"\r\n]*)"$/, "$1"));
  const header = cellsOf(lines[0]);
  const day = header.indexOf("day"), max = header.indexOf("max_temp_f"), min = header.indexOf("min_temp_f"), precip = header.indexOf("precip_in");
  const station = header.indexOf("station"), network = header.indexOf("network");
  if (new Set(header).size !== header.length || day < 0 || max < 0 || min < 0 || station < 0 || (expected && (network < 0 || precip < 0))) throw new Error("Unrecognised daily summary columns.");
  const number = (cell: string | undefined) => {
    if (!cell || cell === "M" || cell === "None") return null;
    if (!/^-?\d+(?:\.\d+)?$/.test(cell)) return null;
    const value = Number(cell);
    return Number.isFinite(value) ? value : null;
  };
  const seen = new Set<string>();
  return lines.slice(1).map(line => {
    const cells = cellsOf(line), date = cells[day];
    if (cells.length !== header.length || !validDate(date) || seen.has(date)) throw new Error("Invalid or duplicate daily summary date.");
    if (expected && (cells[station] !== expected.station || cells[network] !== "KS_ASOS" || date < expected.start || date > expected.end)) throw new Error("Daily summary does not match the requested station and dates.");
    seen.add(date);
    let maxF = number(cells[max]), minF = number(cells[min]);
    if (maxF !== null && minF !== null && maxF < minF) { maxF = null; minF = null; }
    const rain = precip < 0 ? null : number(cells[precip]);
    return { day: date, maxF, minF, precipIn: rain !== null && rain >= 0 ? rain : null };
  });
}

export function validDate(date: unknown): date is string {
  if (typeof date !== "string" || !/^\d{4}-\d{2}-\d{2}$/.test(date)) return false;
  const time = Date.parse(`${date}T00:00:00Z`);
  return Number.isFinite(time) && new Date(time).toISOString().slice(0, 10) === date;
}

/** Conservative cutoff: wait until 02:00 station-local time before using yesterday.
 * This covers IEM's midnight or 01:00 daylight-time daily boundaries; it is not a
 * guarantee that the upstream observation has arrived or passed quality control.
 */
export function lastCompleteStationDate(now: Date, tzname: string): string {
  const parts = Object.fromEntries(new Intl.DateTimeFormat("en-US", { timeZone: tzname, year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit", hourCycle: "h23" }).formatToParts(now).map(p => [p.type, p.value]));
  const local = Date.parse(`${parts.year}-${parts.month}-${parts.day}T00:00:00Z`);
  return new Date(local - (Number(parts.hour) < 2 ? 2 : 1) * 86_400_000).toISOString().slice(0, 10);
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
  station: Readonly<{ id: string; name: string; km: number; tzname?: string }> | null;
  degreeDays: number | null;
  daysRead: number;
  daysMissing: number;
  rainInches?: number | null;
  rainDaysMissing?: number;
  rainTraceDays?: number;
  daysPending?: number;
  completedThrough?: string;
  contractVersion?: number;
}>;

export function validDegreeDays(value: unknown, lon: number, lat: number, year: number): value is DegreeDaysReading {
  if (!value || typeof value !== "object") return false;
  const v = value as Partial<DegreeDaysReading>, station = v.station;
  const count = (n: unknown): n is number => typeof n === "number" && Number.isInteger(n) && n >= 0 && n <= 214;
  const finite = (n: unknown): n is number => typeof n === "number" && Number.isFinite(n) && n >= 0;
  if (v.lon !== lon || v.lat !== lat || v.year !== year || !["ready", "none"].includes(v.state ?? "") || typeof v.retrievedAt !== "string" || !Number.isFinite(Date.parse(v.retrievedAt))) return false;
  if (station !== null && (!station || typeof station.id !== "string" || !/^[A-Z0-9]{3,5}$/.test(station.id) || typeof station.name !== "string" || !finite(station.km) || station.km > GDD_MAX_KM)) return false;
  if (!count(v.daysRead) || !count(v.daysMissing) || (v.daysPending !== undefined && !count(v.daysPending))) return false;
  const pending = v.daysPending ?? 0;
  if (station !== null && v.daysRead + v.daysMissing + pending !== 214) return false;
  if (!(v.degreeDays === null || finite(v.degreeDays)) || (v.daysRead === 0) !== (v.degreeDays === null)) return false;
  const legacyRain = v.rainInches === undefined && v.rainDaysMissing === undefined;
  if (!legacyRain && (!(v.rainInches === null || finite(v.rainInches)) || !count(v.rainDaysMissing) || v.rainDaysMissing + pending > 214)) return false;
  if (!legacyRain && station !== null && ((v.rainInches === null) !== (v.rainDaysMissing === 214 - pending))) return false;
  if (v.rainTraceDays !== undefined && (!count(v.rainTraceDays) || legacyRain || v.rainTraceDays > 214 - pending - (v.rainDaysMissing ?? 0))) return false;
  if (v.state === "ready" && (station === null || (v.degreeDays === null && (v.rainInches === null || v.rainInches === undefined)))) return false;
  if (v.state === "none" && (v.degreeDays !== null || (v.rainInches !== null && v.rainInches !== undefined))) return false;
  if (v.contractVersion !== undefined && (v.contractVersion !== 2 || !validDate(v.completedThrough) || !count(v.daysPending) || !count(v.rainTraceDays))) return false;
  if (v.contractVersion === 2 && (seasonDates(year).filter(date => date > v.completedThrough!).length !== pending || !["America/Chicago", "America/Denver"].includes(station?.tzname ?? ""))) return false;
  return true;
}

const pendingLine = (reading: DegreeDaysReading) => reading.daysPending ? ` · ${reading.daysPending} days not yet due` : "";

/** Precipitation includes liquid-equivalent frozen precipitation, not only rain. */
export function rainLine(reading: DegreeDaysReading): string | null {
  if (reading.state !== "ready") return null;
  if (typeof reading.rainInches !== "number") return "Precipitation unavailable for this response; no zero is inferred.";
  const days = reading.rainDaysMissing === 0 ? "every due day read" : `${reading.rainDaysMissing} days missing`;
  const trace = reading.rainTraceDays ? ` + trace on ${reading.rainTraceDays} days (not added as measured inches)` : "";
  const partial = reading.rainDaysMissing || reading.daysPending ? "Partial: " : "";
  return `${partial}${reading.rainInches.toFixed(2)} in precipitation${trace}, ${GDD_SEASON_LABEL} ${reading.year} · ${days}${pendingLine(reading)}`;
}

export function degreeDaysLine(reading: DegreeDaysReading): string | null {
  if (reading.state !== "ready" || reading.station === null) return null;
  const station = `from ${reading.station.name} (${reading.station.id}), ${Math.round(reading.station.km)} km away`;
  if (reading.degreeDays === null) return `No valid temperature days · ${station}`;
  const total = reading.degreeDays.toLocaleString("en-US");
  const days = `${reading.daysRead} days read, ${reading.daysMissing} missing`;
  const partial = reading.daysMissing || reading.daysPending ? "Partial: " : "";
  const through = reading.completedThrough ? ` · through ${reading.completedThrough}` : "";
  return `${partial}${total} growing degree days (°F-days; corn method), base 50 °F, high capped at 86 °F, ${GDD_SEASON_LABEL} ${reading.year} · ${station} · ${days}${pendingLine(reading)}${through}`;
}
