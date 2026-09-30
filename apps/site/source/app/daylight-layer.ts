import type { Feature, FeatureCollection, MultiPolygon, Polygon, Position } from "geojson";
import polygonClipping, { type MultiPolygon as ClippingMultiPolygon, type Polygon as ClippingPolygon, type Ring as ClippingRing } from "polygon-clipping";
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
type DaylightGeometry = Polygon | MultiPolygon;
const { difference, intersection, union } = polygonClipping;

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

const unwrapLongitude = (longitude: number, reference: number): number =>
  longitude + 360 * Math.round((reference - longitude) / 360);

/** Keep each circular boundary continuous in longitude before clipping it to
 * RFC 7946 world strips. A radius that encloses a pole winds by one world. */
const unwrappedCircle = (longitude: number, latitude: number, radius: number, samples: number): Position[] => {
  const startBearing = latitude < 0 ? 0 : 180; // begin away from the nearer pole
  const points: Position[] = [];
  let previousLongitude = longitude;
  for (let index = 0; index < samples; index += 1) {
    const [normalizedLongitude, pointLatitude] = destination(longitude, latitude, radius, startBearing + index * 360 / samples);
    const pointLongitude = unwrapLongitude(normalizedLongitude, previousLongitude);
    points.push([pointLongitude, pointLatitude]);
    previousLongitude = pointLongitude;
  }
  const [firstLongitude, firstLatitude] = points[0];
  return [...points, [unwrapLongitude(firstLongitude, previousLongitude), firstLatitude]];
};

const ringArea = (ring: readonly Position[]): number => {
  let sum = 0;
  for (let index = 0; index < ring.length - 1; index += 1) {
    const [x1, y1] = ring[index];
    const [x2, y2] = ring[index + 1];
    sum += x1 * y2 - x2 * y1;
  }
  return sum / 2;
};

const counterClockwise = (ring: Position[]): Position[] => ringArea(ring) >= 0 ? ring : [...ring].reverse();

/** Convert a spherical circle to a simple longitude/latitude disk. When the
 * boundary surrounds a pole, close it along that pole before clipping. */
const circleDisk = (longitude: number, latitude: number, radius: number, samples: number): ClippingPolygon => {
  const boundary = unwrappedCircle(longitude, latitude, radius, samples);
  const start = boundary[0];
  const end = boundary.at(-1)!;
  const winding = Math.round((end[0] - start[0]) / 360);
  let ring = boundary;
  if (winding !== 0) {
    const northDistance = 90 - latitude;
    const southDistance = 90 + latitude;
    const poleLatitude = northDistance <= radius + 1e-8 ? 90 : southDistance <= radius + 1e-8 ? -90 : null;
    if (poleLatitude === null) throw new RangeError("A winding solar circle must enclose a geographic pole.");
    ring = [...boundary, [end[0], poleLatitude], [start[0], poleLatitude], start];
  }
  return [counterClockwise(ring)];
};

const geometryBounds = (geometry: ClippingPolygon | ClippingMultiPolygon): [number, number] => {
  let minLongitude = Number.POSITIVE_INFINITY;
  let maxLongitude = Number.NEGATIVE_INFINITY;
  const polygons = geometry.length > 0 && Array.isArray(geometry[0]?.[0]?.[0])
    ? geometry as ClippingMultiPolygon
    : [geometry as ClippingPolygon];
  for (const polygon of polygons) for (const ring of polygon) for (const [longitude] of ring) {
    minLongitude = Math.min(minLongitude, longitude);
    maxLongitude = Math.max(maxLongitude, longitude);
  }
  return [minLongitude, maxLongitude];
};

/** Subtract every periodic copy of the inner disk that overlaps the outer
 * disk's unwrapped longitude branch. A pole-wrapping outer disk spans one
 * full world while a smaller non-wrapping disk can straddle its branch edge. */
const subtractAlignedDisk = (outer: ClippingPolygon, inner: ClippingPolygon): ClippingMultiPolygon => {
  const [outerMin, outerMax] = geometryBounds(outer);
  const [innerMin, innerMax] = geometryBounds(inner);
  const firstShift = Math.ceil((outerMin - innerMax) / 360);
  const lastShift = Math.floor((outerMax - innerMin) / 360);
  const alignedCopies: ClippingPolygon[] = [];
  for (let world = firstShift; world <= lastShift; world += 1) {
    const shift = world * 360;
    const overlap = Math.min(outerMax, innerMax + shift) - Math.max(outerMin, innerMin + shift);
    if (overlap <= 1e-9) continue;
    alignedCopies.push(inner.map((ring) => ring.map(([longitude, latitude]) => [longitude + shift, latitude] as Position)));
  }
  return alignedCopies.length ? difference(outer, union(...alignedCopies)) : [outer];
};

const canonicalRing = (ring: ClippingRing, world: number, exterior: boolean): Position[] => {
  const shifted = ring.map(([longitude, latitude]) => [longitude - 360 * world, latitude] as Position);
  if (shifted.length && (shifted[0][0] !== shifted.at(-1)![0] || shifted[0][1] !== shifted.at(-1)![1])) shifted.push(shifted[0]);
  const densified: Position[] = [];
  for (let index = 0; index < shifted.length - 1; index += 1) {
    const point = shifted[index];
    const next = shifted[index + 1];
    densified.push(point);
    const longitudeSpan = next[0] - point[0];
    if (Math.abs(longitudeSpan) > 180 && Math.abs(Math.abs(point[1]) - 90) < 1e-8 && Math.abs(Math.abs(next[1]) - 90) < 1e-8) {
      densified.push([(point[0] + next[0]) / 2, point[1]]);
    }
  }
  if (densified.length) densified.push(densified[0]);
  const isCounterClockwise = ringArea(densified) >= 0;
  return isCounterClockwise === exterior ? densified : [...densified].reverse();
};

/** Clip polygons to each 360-degree world strip, then shift the pieces into
 * canonical longitudes so neither flat nor globe rendering sees a dateline
 * edge that spans the map. Polygon clipping also preserves annulus holes. */
const clipToWorldStrips = (geometry: ClippingPolygon | ClippingMultiPolygon): MultiPolygon => {
  const [minLongitude, maxLongitude] = geometryBounds(geometry);
  if (!Number.isFinite(minLongitude) || !Number.isFinite(maxLongitude)) return { type: "MultiPolygon", coordinates: [] };
  const firstWorld = Math.floor((minLongitude + 180) / 360);
  const lastWorld = Math.floor((maxLongitude + 180) / 360);
  const coordinates: MultiPolygon["coordinates"] = [];
  for (let world = firstWorld; world <= lastWorld; world += 1) {
    const left = -180 + world * 360;
    const right = 180 + world * 360;
    const strip: ClippingPolygon = [[[left, -90], [right, -90], [right, 90], [left, 90], [left, -90]]];
    const clipped = intersection(geometry, strip);
    for (const polygon of clipped) {
      const rings = polygon.map((ring, index) => canonicalRing(ring, world, index === 0));
      if (rings.length && rings[0].length >= 4 && Math.abs(ringArea(rings[0])) > 1e-10) coordinates.push(rings);
    }
  }
  return { type: "MultiPolygon", coordinates };
};

/** Build projection-aware native map polygons for the night cap and twilight
 * bands. Every shape is clipped at the antimeridian before it reaches MapLibre. */
export const buildDaylightGeometry = (instant: Date | number, samples = 360): FeatureCollection<DaylightGeometry, DaylightProperties> => {
  const sun = solarPositionAt(instant);
  const antiLongitude = signedDegrees(sun.subsolarLongitudeDegrees + 180);
  const antiLatitude = -sun.declinationDegrees;
  const disks = new Map<number, ClippingPolygon>();
  const diskAt = (radius: number): ClippingPolygon => {
    const existing = disks.get(radius);
    if (existing) return existing;
    const created = circleDisk(antiLongitude, antiLatitude, radius, samples);
    disks.set(radius, created);
    return created;
  };
  const features: Array<Feature<DaylightGeometry, DaylightProperties>> = [];
  features.push({
    type: "Feature",
    properties: { band: "night", shade: -18 },
    geometry: clipToWorldStrips(diskAt(72)),
  });
  const twilightBands: ReadonlyArray<{ inner: number; outer: number; band: Exclude<DaylightBand, "night">; shade: number }> = [
    { inner: 72, outer: 78, band: "astronomical", shade: -15 },
    { inner: 78, outer: 84, band: "nautical", shade: -9 },
    { inner: 84, outer: 89.167, band: "civil", shade: -3.4165 }, // outer edge is the conventional -0.833° sunrise boundary
  ];
  for (const { inner, outer, band, shade } of twilightBands) {
    features.push({
      type: "Feature",
      properties: { band, shade },
      geometry: clipToWorldStrips(subtractAlignedDisk(diskAt(outer), diskAt(inner))),
    });
  }
  return { type: "FeatureCollection", features };
};

export const solarReferenceElevation = (instant: Date | number, latitude: number, longitude: number): number =>
  solarPositionAt(instant, latitude, longitude).elevationDegrees;
