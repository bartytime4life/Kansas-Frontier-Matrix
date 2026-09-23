/** A fixed, low-resolution Kansas sampling grid for an optional model display. */
export const WIND_GRID = Object.freeze([
  [-101.8, 39.8], [-98.4, 39.8], [-95.0, 39.8],
  [-101.8, 38.5], [-98.4, 38.5], [-95.0, 38.5],
  [-101.8, 37.3], [-98.4, 37.3], [-95.0, 37.3],
] as const);

export const WIND_SOURCE_URL = "https://open-meteo.com/en/docs";
export const WIND_REFERENCE_URL = "https://earth.nullschool.net/";
export const WIND_API_PATH = "/api/weather/wind";

export type WindSample = Readonly<{ longitude: number; latitude: number; speedKmh: number; fromDegrees: number }>;
export type WindFrame = Readonly<{ validAt: string; samples: readonly WindSample[] }>;
export type WindField = Readonly<{
  source: "Open-Meteo forecast API";
  role: "EXTERNAL_MODEL_DISPLAY_ONLY";
  retrievedAt: string;
  frames: readonly WindFrame[];
  method: string;
}>;

type RecordValue = Record<string, unknown>;
const record = (value: unknown): value is RecordValue => value !== null && typeof value === "object" && !Array.isArray(value);
const date = (value: unknown): string | null => {
  if (typeof value !== "string" || !/^\d{4}-\d\d-\d\dT\d\d:00$/.test(value)) return null;
  const ms = Date.parse(`${value}Z`);
  return Number.isFinite(ms) ? new Date(ms).toISOString() : null;
};

export function parseWindForecast(payload: unknown, retrievedAt: string): WindField {
  if (!Array.isArray(payload) || payload.length !== WIND_GRID.length || !Number.isFinite(Date.parse(retrievedAt))) {
    throw new Error("Wind forecast grid is incomplete.");
  }
  let times: string[] | null = null;
  const locations = payload.map((entry, index) => {
    if (!record(entry) || !record(entry.hourly) || !record(entry.hourly_units)) throw new Error("Wind forecast location is invalid.");
    const [longitude, latitude] = WIND_GRID[index];
    if (typeof entry.longitude !== "number" || typeof entry.latitude !== "number"
      || Math.abs(entry.longitude - longitude) > 0.35 || Math.abs(entry.latitude - latitude) > 0.35
      || entry.utc_offset_seconds !== 0 || entry.hourly_units.wind_speed_10m !== "km/h"
      || entry.hourly_units.wind_direction_10m !== "°") throw new Error("Wind forecast location or units changed.");
    const hourly = entry.hourly;
    const values = hourly.wind_speed_10m;
    const directions = hourly.wind_direction_10m;
    if (!Array.isArray(hourly.time) || !Array.isArray(values) || !Array.isArray(directions)
      || hourly.time.length < 2 || hourly.time.length > 8 || values.length !== hourly.time.length
      || directions.length !== hourly.time.length) throw new Error("Wind forecast series is incomplete.");
    const parsedTimes = hourly.time.map(date);
    if (parsedTimes.some((value) => value === null)) throw new Error("Wind forecast time is invalid.");
    if (times && JSON.stringify(parsedTimes) !== JSON.stringify(times)) throw new Error("Wind forecast locations use different times.");
    times = parsedTimes as string[];
    return hourly.time.map((_: unknown, frameIndex: number) => {
      const speed = values[frameIndex];
      const direction = directions[frameIndex];
      if (typeof speed !== "number" || !Number.isFinite(speed) || speed < 0 || speed > 250
        || typeof direction !== "number" || !Number.isFinite(direction) || direction < 0 || direction > 360) {
        throw new Error("Wind forecast contains an invalid vector.");
      }
      return Object.freeze({ longitude, latitude, speedKmh: speed, fromDegrees: direction });
    });
  });
  const frames = (times ?? [] as string[]).map((validAt, index) => Object.freeze({
    validAt,
    samples: Object.freeze(locations.map((location) => location[index])),
  }));
  if (frames.length < 2) throw new Error("Wind forecast has no usable frame sequence.");
  return Object.freeze({
    source: "Open-Meteo forecast API",
    role: "EXTERNAL_MODEL_DISPLAY_ONLY",
    retrievedAt: new Date(retrievedAt).toISOString(),
    frames: Object.freeze(frames),
    method: "Nine forecast grid samples; visual streamlines are bilinearly interpolated between samples. They are illustrative model display, not measured wind or a KFM EvidenceBundle.",
  });
}

export function isWindField(value: unknown): value is WindField {
  if (!record(value) || value.role !== "EXTERNAL_MODEL_DISPLAY_ONLY" || !Array.isArray(value.frames)
    || value.frames.length < 2 || value.frames.length > 8 || !Number.isFinite(Date.parse(String(value.retrievedAt)))) return false;
  return value.frames.every((frame) => record(frame) && typeof frame.validAt === "string" && Number.isFinite(Date.parse(frame.validAt))
    && Array.isArray(frame.samples) && frame.samples.length === WIND_GRID.length
    && frame.samples.every((sample: unknown) => record(sample) && typeof sample.speedKmh === "number"
      && Number.isFinite(sample.speedKmh) && sample.speedKmh >= 0 && sample.speedKmh <= 250
      && typeof sample.fromDegrees === "number" && Number.isFinite(sample.fromDegrees)
      && sample.fromDegrees >= 0 && sample.fromDegrees <= 360));
}

/** Meteorological direction is where wind comes from; particles travel the opposite way. */
export function windVector(sample: Pick<WindSample, "speedKmh" | "fromDegrees">): readonly [number, number] {
  const toward = (sample.fromDegrees + 180) * Math.PI / 180;
  return [Math.sin(toward) * sample.speedKmh, Math.cos(toward) * sample.speedKmh];
}

export function interpolateWind(samples: readonly WindSample[], longitude: number, latitude: number): readonly [number, number] | null {
  if (samples.length !== WIND_GRID.length || longitude < -101.8 || longitude > -95 || latitude < 37.3 || latitude > 39.8) return null;
  const x = (longitude + 101.8) / 3.4;
  const y = latitude >= 38.5 ? (39.8 - latitude) / 1.3 : 1 + (38.5 - latitude) / 1.2;
  const column = Math.min(1, Math.floor(x));
  const row = Math.min(1, Math.floor(y));
  const tx = x - column;
  const ty = y - row;
  const index = row * 3 + column;
  const vectors = [index, index + 1, index + 3, index + 4].map((i) => windVector(samples[i]));
  return [0, 1].map((axis) => (vectors[0][axis] * (1 - tx) + vectors[1][axis] * tx) * (1 - ty)
    + (vectors[2][axis] * (1 - tx) + vectors[3][axis] * tx) * ty) as [number, number];
}
