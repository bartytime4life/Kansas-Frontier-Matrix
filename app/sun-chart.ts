import type { FeatureCollection, Point } from "geojson";
import type { GeoJSONSource, Map as MapLibreMap } from "./maplibre-seam";
import { KANSAS_OUTLINE } from "./kansas-orientation";

/**
 * Daylight through the year at one Kansas place: sunrise and sunset, and the
 * civil, nautical and astronomical twilights, for every day of a year, in
 * Central clock time. Calculated with the NOAA solar equations (Meeus): the
 * Sun's declination and the equation of time, refined once at each event, so
 * times agree with NOAA's to about a minute. Sunrise and sunset are the upper
 * limb on a sea-level horizon (the centre 0.833° below it, for refraction and
 * the Sun's radius); twilights end with the centre 6°, 12° and 18° below.
 */

export const SUN_EVENTS = Object.freeze({ sun: -0.833, civil: -6, nautical: -12, astronomical: -18 } as const);
export type SunLimit = keyof typeof SUN_EVENTS;
export const KANSAS_CENTRE = Object.freeze({ lon: -98.698, lat: 38.498, name: "the geographic centre of Kansas, Barton County" });
/**
 * Selection follows the same simplified Census outline the map displays,
 * including the Missouri River edge. Display scope only, not a legal boundary.
 */
export function inKansas(lon: number, lat: number): boolean {
  if (!Number.isFinite(lon) || !Number.isFinite(lat)) return false;
  let inside = false;
  for (let i = 0, j = KANSAS_OUTLINE.length - 1; i < KANSAS_OUTLINE.length; j = i++) {
    const [ax, ay] = KANSAS_OUTLINE[j], [bx, by] = KANSAS_OUTLINE[i];
    const cross = (lon - ax) * (by - ay) - (lat - ay) * (bx - ax);
    if (Math.abs(cross) < 1e-12 && lon >= Math.min(ax, bx) && lon <= Math.max(ax, bx)
      && lat >= Math.min(ay, by) && lat <= Math.max(ay, by)) return true;
    if ((ay > lat) !== (by > lat) && lon < (bx - ax) * (lat - ay) / (by - ay) + ax) inside = !inside;
  }
  return inside;
}

export const SUN_TIME_NOTE = "All Sun and Moon times use Central time (CDT/CST). In Sherman, Wallace, Greeley and Hamilton counties, local Mountain clocks read one hour earlier. The panel does not determine a location's time zone.";

const RAD = Math.PI / 180;
const mod = (v: number, d: number) => ((v % d) + d) % d;
/** Declination (degrees) and equation of time (minutes) at a Julian date (NOAA solar calculator equations, after Meeus). */
export function solarParameters(jd: number): { declination: number; equationOfTime: number } {
  const T = (jd - 2451545) / 36525;
  const L0 = mod(280.46646 + T * (36000.76983 + T * 0.0003032), 360);
  const M = 357.52911 + T * (35999.05029 - 0.0001537 * T);
  const e = 0.016708634 - T * (0.000042037 + 0.0000001267 * T);
  const C = Math.sin(M * RAD) * (1.914602 - T * (0.004817 + 0.000014 * T)) + Math.sin(2 * M * RAD) * (0.019993 - 0.000101 * T) + Math.sin(3 * M * RAD) * 0.000289;
  const omega = 125.04 - 1934.136 * T;
  const lambda = L0 + C - 0.00569 - 0.00478 * Math.sin(omega * RAD);
  const eps0 = 23 + (26 + (21.448 - T * (46.815 + T * (0.00059 - T * 0.001813))) / 60) / 60;
  const eps = eps0 + 0.00256 * Math.cos(omega * RAD);
  const declination = Math.asin(Math.sin(eps * RAD) * Math.sin(lambda * RAD)) / RAD;
  const y = Math.tan(eps / 2 * RAD) ** 2;
  const equationOfTime = 4 / RAD * (y * Math.sin(2 * L0 * RAD) - 2 * e * Math.sin(M * RAD) + 4 * e * y * Math.sin(M * RAD) * Math.cos(2 * L0 * RAD)
    - 0.5 * y * y * Math.sin(4 * L0 * RAD) - 1.25 * e * e * Math.sin(2 * M * RAD));
  return { declination, equationOfTime };
}
const julianAt = (ms: number) => ms / 86_400_000 + 2_440_587.5;

/**
 * The instant (epoch ms) the Sun's centre crosses an altitude, before (morning)
 * or after (evening) solar noon on the UTC day of `dayMs`, or null when it does
 * not reach it that day. `noon` gives solar noon instead.
 */
export function sunEvent(dayMs: number, lat: number, lon: number, altitude: number | "noon", morning = true): number | null {
  let minutes = 720 - 4 * lon;
  for (let pass = 0; pass < 3; pass++) {
    const { declination, equationOfTime } = solarParameters(julianAt(dayMs + minutes * 60_000));
    const noon = 720 - 4 * lon - equationOfTime;
    if (altitude === "noon") { minutes = noon; continue; }
    const cosH = (Math.sin(altitude * RAD) - Math.sin(lat * RAD) * Math.sin(declination * RAD)) / (Math.cos(lat * RAD) * Math.cos(declination * RAD));
    if (cosH < -1 || cosH > 1) return null;
    const hourAngle = Math.acos(cosH) / RAD;
    minutes = noon + (morning ? -4 : 4) * hourAngle;
  }
  return dayMs + minutes * 60_000;
}

const CENTRAL = "America/Chicago";
const OFFSET = new Intl.DateTimeFormat("en-US", { timeZone: CENTRAL, timeZoneName: "shortOffset" });
/** The Central time offset from UTC, in minutes, at an instant (−360 in winter, −300 in summer). */
export function centralOffset(ms: number): number {
  const name = OFFSET.formatToParts(ms).find(part => part.type === "timeZoneName")?.value ?? "GMT-6";
  const match = /GMT([+-]\d+)(?::(\d+))?/.exec(name);
  return match ? Number(match[1]) * 60 + Math.sign(Number(match[1])) * Number(match[2] ?? 0) : -360;
}

export type SunDay = Readonly<{
  date: string; offset: number;
  /** Central clock minutes after local midnight (null when the Sun does not reach that altitude). */
  astroDawn: number | null; nauticalDawn: number | null; civilDawn: number | null; sunrise: number | null; noon: number;
  sunset: number | null; civilDusk: number | null; nauticalDusk: number | null; astroDusk: number | null;
  /** Minutes of daylight, sunrise to sunset. */
  length: number;
}>;

/** Every day of a Kansas calendar year at one place. */
export function sunYear(year: number, lat: number, lon: number): SunDay[] {
  const days: SunDay[] = [];
  for (let t = Date.UTC(year, 0, 1); new Date(t).getUTCFullYear() === year; t += 86_400_000) {
    // The UTC day of local noon (about 18:00 UTC in Kansas) holds the local day's events.
    const offset = centralOffset(t + 18 * 3_600_000);
    const local = (ms: number | null) => ms === null ? null : (ms - t) / 60_000 + offset;
    const ev = (altitude: number, morning: boolean) => local(sunEvent(t, lat, lon, altitude, morning));
    const sunrise = ev(SUN_EVENTS.sun, true), sunset = ev(SUN_EVENTS.sun, false);
    days.push(Object.freeze({
      date: new Date(t).toISOString().slice(0, 10), offset,
      astroDawn: ev(SUN_EVENTS.astronomical, true), nauticalDawn: ev(SUN_EVENTS.nautical, true), civilDawn: ev(SUN_EVENTS.civil, true), sunrise,
      noon: local(sunEvent(t, lat, lon, "noon"))!,
      sunset, civilDusk: ev(SUN_EVENTS.civil, false), nauticalDusk: ev(SUN_EVENTS.nautical, false), astroDusk: ev(SUN_EVENTS.astronomical, false),
      length: sunrise !== null && sunset !== null ? sunset - sunrise : 0,
    }));
  }
  return days;
}

export const clock = (minutes: number, offset?: number) => {
  const m = mod(Math.round(minutes), 1440);
  const h = Math.floor(m / 60), mm = m % 60;
  return `${h % 12 === 0 ? 12 : h % 12}:${String(mm).padStart(2, "0")} ${h < 12 ? "AM" : "PM"}${offset === undefined ? "" : offset === -300 ? " CDT" : " CST"}`;
};
const span = (minutes: number) => {
  const rounded = Math.round(minutes);
  return `${Math.floor(rounded / 60)} h ${String(rounded % 60).padStart(2, "0")} min`;
};
const DAY = new Intl.DateTimeFormat("en-US", { timeZone: "UTC", month: "short", day: "numeric" });
const dayLabel = (date: string) => DAY.format(Date.parse(`${date}T12:00:00Z`));
export const coordinateLabel = (lon: number, lat: number) => `${Math.abs(lat).toFixed(2)}°${lat >= 0 ? "N" : "S"}, ${Math.abs(lon).toFixed(2)}°${lon >= 0 ? "E" : "W"}`;

/** The day's line: its sunrise, sunset, length and change, then the year's longest and shortest days. */
export function sunReading(days: readonly SunDay[], date: string): string | null {
  const i = days.findIndex(d => d.date === date);
  if (i < 0) return null;
  const d = days[i], prev = days[i - 1] ?? null;
  const change = prev ? Math.round((d.length - prev.length) * 60) : null;
  const longest = days.reduce((a, b) => b.length > a.length ? b : a), shortest = days.reduce((a, b) => b.length < a.length ? b : a);
  const changed = change === null || change === 0 ? "" : ` (${change > 0 ? "+" : "−"}${Math.floor(Math.abs(change) / 60)} min ${String(Math.abs(change) % 60).padStart(2, "0")} s on the day before)`;
  return `${dayLabel(d.date)}: first light ${d.civilDawn === null ? "–" : clock(d.civilDawn)}, sunrise ${d.sunrise === null ? "–" : clock(d.sunrise)}, solar noon ${clock(d.noon)}, sunset ${d.sunset === null ? "–" : clock(d.sunset)}, last light ${d.civilDusk === null ? "–" : clock(d.civilDusk, d.offset)}`
    + ` · ${span(d.length)} of daylight${changed} · longest ${dayLabel(longest.date)}, ${span(longest.length)}; shortest ${dayLabel(shortest.date)}, ${span(shortest.length)}`;
}

export const SUN_BAND_COLORS = Object.freeze({ night: "#0b1430", astronomical: "#1d2c5c", nautical: "#2f4a8a", civil: "#5f7fbf", day: "#f2d27a" });
export type SunChart = Readonly<{
  width: number; height: number; left: number; top: number; plotWidth: number; plotHeight: number;
  night: string; bands: readonly Readonly<{ id: keyof typeof SUN_BAND_COLORS; color: string; d: string }>[]; noon: string;
  months: readonly Readonly<{ x: number; label: string }>[]; hours: readonly Readonly<{ y: number; label: string }>[]; today: number | null;
}>;

/**
 * The year as a chart: days across, Central clock time up (midnight at the
 * foot), daylight gold between the sunrise and sunset curves, the twilights in
 * deepening blues, and solar noon through the middle. The steps in March and
 * November are the clock changing, not the Sun.
 */
export function sunChart(days: readonly SunDay[], today: string | null): SunChart {
  const width = 260, height = 168, left = 26, right = 4, top = 4, bottom = 14;
  const plotWidth = width - left - right, plotHeight = height - top - bottom;
  const x = (i: number) => left + (i + 0.5) / days.length * plotWidth;
  const y = (minutes: number) => top + plotHeight - Math.max(0, Math.min(1440, minutes)) / 1440 * plotHeight;
  const curve = (pick: (d: SunDay) => number) => days.map((d, i) => `${x(i).toFixed(1)},${y(pick(d)).toFixed(1)}`);
  const band = (lower: (d: SunDay) => number, upper: (d: SunDay) => number) => `M${curve(lower).join("L")}L${curve(upper).reverse().join("L")}Z`;
  const or = (value: number | null, fallback: number) => value ?? fallback;
  const bands = [
    { id: "astronomical" as const, d: band(d => or(d.astroDawn, 0), d => or(d.nauticalDawn, 0)) + band(d => or(d.nauticalDusk, 1440), d => or(d.astroDusk, 1440)) },
    { id: "nautical" as const, d: band(d => or(d.nauticalDawn, 0), d => or(d.civilDawn, 0)) + band(d => or(d.civilDusk, 1440), d => or(d.nauticalDusk, 1440)) },
    { id: "civil" as const, d: band(d => or(d.civilDawn, 0), d => or(d.sunrise, 0)) + band(d => or(d.sunset, 1440), d => or(d.civilDusk, 1440)) },
    { id: "day" as const, d: band(d => or(d.sunrise, 720), d => or(d.sunset, 720)) },
  ].map(b => ({ ...b, color: SUN_BAND_COLORS[b.id] }));
  const months = days.flatMap((d, i) => d.date.endsWith("-01") ? [{ x: x(i), label: DAY.format(Date.parse(`${d.date}T12:00:00Z`)).slice(0, 3) }] : []);
  const hours = [0, 360, 720, 1080, 1440].map(m => ({ y: y(m), label: m === 0 || m === 1440 ? "12a" : m === 720 ? "12p" : m < 720 ? "6a" : "6p" }));
  const index = today ? days.findIndex(d => d.date === today) : -1;
  return Object.freeze({ width, height, left, top, plotWidth, plotHeight, night: SUN_BAND_COLORS.night, bands, noon: `M${curve(d => d.noon).join("L")}`, months, hours, today: index < 0 ? null : x(index) });
}

// The charted place, above the globe's daylight shading.
export const SUN_PLACE_SOURCE_ID = "kfm-sun-place";
export const SUN_PLACE_LAYER_ID = "kfm-sun-place-mark";
/** A sun-gold ring at the charted place (or nothing, for null). */
export function syncSunPlace(map: MapLibreMap, place: { lon: number; lat: number } | null): void {
  if (!place) {
    if (map.getLayer(SUN_PLACE_LAYER_ID)) map.removeLayer(SUN_PLACE_LAYER_ID);
    if (map.getSource(SUN_PLACE_SOURCE_ID)) map.removeSource(SUN_PLACE_SOURCE_ID);
    return;
  }
  const data: FeatureCollection<Point> = { type: "FeatureCollection", features: [{ type: "Feature", geometry: { type: "Point", coordinates: [place.lon, place.lat] }, properties: {} }] };
  const source = map.getSource(SUN_PLACE_SOURCE_ID) as GeoJSONSource | undefined;
  if (source) source.setData(data);
  else map.addSource(SUN_PLACE_SOURCE_ID, { type: "geojson", data });
  if (!map.getLayer(SUN_PLACE_LAYER_ID)) map.addLayer({ id: SUN_PLACE_LAYER_ID, type: "circle", source: SUN_PLACE_SOURCE_ID,
    paint: { "circle-color": "#f2d27a", "circle-radius": 4, "circle-stroke-color": "#0b1430", "circle-stroke-width": 2 } });
}
