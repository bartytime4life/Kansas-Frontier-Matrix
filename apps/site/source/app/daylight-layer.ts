import type { Feature, FeatureCollection, Polygon, Position } from "geojson";
import { getSolarPosition } from "sunrise-sunset-js";
import type { SpaOptions } from "sunrise-sunset-js";

export const KANSAS_DAYLIGHT_TIME_ZONE = "America/Chicago";
export const DAYLIGHT_LOOP_DURATION_MS = 60_000;
const RAD = Math.PI / 180;
const DEG = 180 / Math.PI;

export type KansasDayInterval = Readonly<{ startMs: number; endMs: number; durationMs: number }>;
export type SolarPosition = Readonly<{
  rightAscensionDegrees: number;
  declinationDegrees: number;
  subsolarLongitudeDegrees: number;
  azimuthDegrees: number;
  elevationDegrees: number;
}>;
export type DaylightBand = "night" | "astronomical" | "nautical" | "civil";
type DaylightProperties = Readonly<{ band: DaylightBand; shade: number }>;

const mod = (value: number, divisor: number): number => ((value % divisor) + divisor) % divisor;
const signedDegrees = (value: number): number => mod(value + 180, 360) - 180;

const partsForDate = (date: Date, timeZone: string) => {
  const parts = new Intl.DateTimeFormat("en-CA", {
    timeZone,
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
    hourCycle: "h23",
  }).formatToParts(date);
  return Object.fromEntries(parts.map((part) => [part.type, part.value]));
};

const validCalendarDay = (day: string): boolean => {
  if (!/^\d{4}-\d{2}-\d{2}$/.test(day)) return false;
  const [year, month, date] = day.split("-").map(Number);
  const check = new Date(Date.UTC(year, month - 1, date));
  return check.getUTCFullYear() === year && check.getUTCMonth() === month - 1 && check.getUTCDate() === date;
};

const addCalendarDays = (day: string, amount: number): string => {
  const [year, month, date] = day.split("-").map(Number);
  const next = new Date(Date.UTC(year, month - 1, date + amount));
  return `${next.getUTCFullYear()}-${String(next.getUTCMonth() + 1).padStart(2, "0")}-${String(next.getUTCDate()).padStart(2, "0")}`;
};

/** Convert a wall-clock midnight in a named IANA zone to its UTC instant. */
const zonedMidnight = (day: string, timeZone: string): number => {
  if (!validCalendarDay(day)) throw new RangeError("A real YYYY-MM-DD calendar day is required.");
  const [year, month, date] = day.split("-").map(Number);
  const targetWallAsUtc = Date.UTC(year, month - 1, date);
  let instant = targetWallAsUtc;
  for (let attempt = 0; attempt < 4; attempt += 1) {
    const parts = partsForDate(new Date(instant), timeZone);
    const representedWallAsUtc = Date.UTC(
      Number(parts.year), Number(parts.month) - 1, Number(parts.day),
      Number(parts.hour), Number(parts.minute), Number(parts.second),
    );
    const correction = targetWallAsUtc - representedWallAsUtc;
    instant += correction;
    if (correction === 0) break;
  }
  return instant;
};

export const currentKansasCalendarDay = (now = new Date()): string => {
  const parts = partsForDate(now, KANSAS_DAYLIGHT_TIME_ZONE);
  return `${parts.year}-${parts.month}-${parts.day}`;
};

export const kansasLocalDayInterval = (day: string): KansasDayInterval => {
  const startMs = zonedMidnight(day, KANSAS_DAYLIGHT_TIME_ZONE);
  const endMs = zonedMidnight(addCalendarDays(day, 1), KANSAS_DAYLIGHT_TIME_ZONE);
  return { startMs, endMs, durationMs: endMs - startMs };
};

export const isInstantInKansasDay = (instantMs: number, day: string): boolean => {
  if (!Number.isFinite(instantMs)) return false;
  try {
    const { startMs, endMs } = kansasLocalDayInterval(day);
    return instantMs >= startMs && instantMs < endMs;
  } catch {
    return false;
  }
};

export const instantAtDayFraction = (day: string, fraction: number): number => {
  const interval = kansasLocalDayInterval(day);
  const bounded = Math.max(0, Math.min(1, Number.isFinite(fraction) ? fraction : 0));
  return interval.startMs + bounded * interval.durationMs;
};

export const dayFractionAtInstant = (instantMs: number, day: string): number => {
  const interval = kansasLocalDayInterval(day);
  return Math.max(0, Math.min(1, (instantMs - interval.startMs) / interval.durationMs));
};

export const daylightLoopFraction = (startFraction: number, elapsedWallMs: number): number =>
  mod((Number.isFinite(startFraction) ? startFraction : 0) + Math.max(0, elapsedWallMs) / DAYLIGHT_LOOP_DURATION_MS, 1);

export const daylightShouldAutoplay = (reducedMotion: boolean, documentHidden: boolean): boolean =>
  !reducedMotion && !documentHidden;

export const restoreDaylightView = (
  dayValue: string | null,
  instantValue: string | null,
  enabled: boolean,
  fallbackDay = currentKansasCalendarDay(),
): Readonly<{ day: string; instantMs: number; enabled: boolean; playing: false }> => {
  let day = dayValue ?? fallbackDay;
  let interval: KansasDayInterval;
  try {
    interval = kansasLocalDayInterval(day);
  } catch {
    day = fallbackDay;
    interval = kansasLocalDayInterval(day);
  }
  const requested = instantValue ? Date.parse(instantValue) : Number.NaN;
  return {
    day,
    instantMs: isInstantInKansasDay(requested, day) ? requested : interval.startMs,
    enabled,
    playing: false,
  };
};

export const formatKansasSolarTime = (instantMs: number): Readonly<{ central: string; utc: string }> => {
  const date = new Date(instantMs);
  if (!Number.isFinite(date.getTime())) return { central: "Time unavailable", utc: "Time unavailable" };
  const central = new Intl.DateTimeFormat("en-US", {
    timeZone: KANSAS_DAYLIGHT_TIME_ZONE,
    weekday: "short", month: "short", day: "numeric", hour: "numeric", minute: "2-digit", second: "2-digit", hour12: true, timeZoneName: "short",
  }).format(date);
  const utc = new Intl.DateTimeFormat("en-GB", {
    timeZone: "UTC", year: "numeric", month: "short", day: "2-digit", hour: "2-digit", minute: "2-digit", second: "2-digit", hourCycle: "h23",
  }).format(date).replace(",", "") + " UTC";
  return { central, utc };
};

/**
 * Solar coordinates from the published Meeus/NREL solar-position equations:
 * mean longitude/anomaly, equation of center, apparent ecliptic longitude,
 * nutation/aberration correction, apparent obliquity, and apparent RA/Dec.
 * The observer coordinates are passed through to SPA, so the returned
 * azimuth/elevation are topocentric. The global overlay uses an equatorial
 * reference observer (0°, 0°) for its subsolar center; its apparent horizon
 * uses the conventional -0.833 degree sunrise/sunset boundary.
 */
export const solarPositionAt = (
  instant: Date | number,
  latitudeDegrees = 0,
  longitudeDegrees = 0,
  options: SpaOptions = {},
): SolarPosition => {
  const date = instant instanceof Date ? instant : new Date(instant);
  const timestamp = date.getTime();
  if (!Number.isFinite(timestamp) || !Number.isFinite(latitudeDegrees) || !Number.isFinite(longitudeDegrees)
    || latitudeDegrees < -90 || latitudeDegrees > 90) throw new RangeError("A valid instant and geographic coordinate are required.");
  const spa = getSolarPosition(latitudeDegrees, longitudeDegrees, date, options);
  if (!spa) throw new RangeError("NREL SPA could not calculate this solar position.");

  // Use Greenwich apparent sidereal time to turn the NREL apparent RA into the
  // subsolar longitude. The four largest nutation terms complete the equation
  // of the equinoxes used by the SPA apparent coordinates.
  const julianDay = (timestamp + (options.deltaUt1 ?? 0) * 1000) / 86_400_000 + 2_440_587.5;
  const centuries = (julianDay - 2_451_545) / 36_525;
  const meanSiderealDegrees = mod(
    280.46061837 + 360.98564736629 * (julianDay - 2_451_545)
      + 0.000387933 * centuries ** 2 - centuries ** 3 / 38_710_000,
    360,
  );
  const omega = 125.04452 - 1934.136261 * centuries + 0.0020708 * centuries ** 2 + centuries ** 3 / 450_000;
  const solarMeanLongitude = 280.4665 + 36_000.7698 * centuries;
  const lunarMeanLongitude = 218.3165 + 481_267.8813 * centuries;
  const nutationLongitudeArcSeconds = -17.20 * Math.sin(omega * RAD)
    - 1.32 * Math.sin(2 * solarMeanLongitude * RAD)
    - 0.23 * Math.sin(2 * lunarMeanLongitude * RAD)
    + 0.21 * Math.sin(2 * omega * RAD);
  const meanObliquityDegrees = 23.439291 - 0.0130042 * centuries - 1.64e-7 * centuries ** 2 + 5.04e-7 * centuries ** 3;
  const apparentSiderealDegrees = meanSiderealDegrees + (nutationLongitudeArcSeconds / 3600) * Math.cos(meanObliquityDegrees * RAD);
  const rightAscensionDegrees = mod(spa.rightAscension, 360);
  return {
    rightAscensionDegrees,
    declinationDegrees: spa.declination,
    subsolarLongitudeDegrees: signedDegrees(rightAscensionDegrees - apparentSiderealDegrees),
    azimuthDegrees: spa.azimuth,
    elevationDegrees: spa.elevation,
  };
};

const destination = (centerLongitude: number, centerLatitude: number, angularRadius: number, bearingDegrees: number): Position => {
  const phi1 = centerLatitude * RAD;
  const lambda1 = centerLongitude * RAD;
  const delta = angularRadius * RAD;
  const bearing = bearingDegrees * RAD;
  const sinPhi2 = Math.sin(phi1) * Math.cos(delta) + Math.cos(phi1) * Math.sin(delta) * Math.cos(bearing);
  const phi2 = Math.asin(Math.max(-1, Math.min(1, sinPhi2)));
  const lambda2 = lambda1 + Math.atan2(
    Math.sin(bearing) * Math.sin(delta) * Math.cos(phi1),
    Math.cos(delta) - Math.sin(phi1) * Math.sin(phi2),
  );
  return [signedDegrees(lambda2 * DEG), phi2 * DEG];
};

const circle = (longitude: number, latitude: number, radius: number, samples = 360): Position[] => {
  const points = Array.from({ length: samples }, (_, index) => destination(longitude, latitude, radius, index * 360 / samples));
  // RFC 7946 asks for counter-clockwise exterior and clockwise interior rings.
  points.reverse();
  return [...points, points[0]];
};

const clockwiseRing = (ring: Position[]): Position[] => {
  const reversedVertices = ring.slice(0, -1).reverse();
  return [...reversedVertices, reversedVertices[0]];
};

const annulus = (longitude: number, latitude: number, inner: number, outer: number): Polygon => ({
  type: "Polygon",
  coordinates: [circle(longitude, latitude, outer), clockwiseRing(circle(longitude, latitude, inner))],
});

/** Build native map polygons for the night cap and twilight bands. Each band
 * uses sub-degree rings so the color transition reads smoothly at world scale. */
export const buildDaylightGeometry = (instant: Date | number): FeatureCollection<Polygon, DaylightProperties> => {
  const sun = solarPositionAt(instant);
  const antiLongitude = signedDegrees(sun.subsolarLongitudeDegrees + 180);
  const antiLatitude = -sun.declinationDegrees;
  const features: Array<Feature<Polygon, DaylightProperties>> = [];
  features.push({
    type: "Feature",
    properties: { band: "night", shade: -18 },
    geometry: { type: "Polygon", coordinates: [circle(antiLongitude, antiLatitude, 72)] },
  });
  const startRadius = 72;
  const endRadius = 89.167; // center-of-Sun altitude -0.833° (conventional apparent sunrise)
  for (let inner = startRadius; inner < endRadius; inner += 0.5) {
    const outer = Math.min(endRadius, inner + 0.5);
    const centerAltitude = -18 + ((inner + outer) / 2 - startRadius) / (endRadius - startRadius) * 17.167;
    const band: DaylightBand = centerAltitude >= -6 ? "civil" : centerAltitude >= -12 ? "nautical" : "astronomical";
    features.push({
      type: "Feature",
      properties: { band, shade: centerAltitude },
      geometry: annulus(antiLongitude, antiLatitude, inner, outer),
    });
  }
  return { type: "FeatureCollection", features };
};

export const solarReferenceElevation = (instant: Date | number, latitude: number, longitude: number): number =>
  solarPositionAt(instant, latitude, longitude).elevationDegrees;
