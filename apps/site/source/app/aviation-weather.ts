/**
 * Airport weather (METAR from ASOS/AWOS) and pilot reports (PIREP) from the
 * NOAA/NWS Aviation Weather Center Data API. Observed context only: a missing
 * station or report is not evidence of good weather or of no traffic.
 */
export const AWC_SOURCE_TITLE = "NOAA/NWS Aviation Weather Center Data API";
export const AWC_SOURCE_URL = "https://aviationweather.gov/data/api/";
export const AWC_API_BASE = "https://aviationweather.gov/api/data";
// lat0,lon0,lat1,lon1 per the AWC Data API; matches the airspace product region.
export const AWC_KANSAS_BBOX = "36.7,-102.3,40.3,-94.3";
export const AVIATION_METAR_API_PATH = "/api/aviation/metar";
export const AVIATION_PIREP_API_PATH = "/api/aviation/pireps";
export const METAR_MAX_AGE_MINUTES = 90;
export const MAX_METARS = 400;
export const MAX_PIREPS = 300;

export type FlightCategory = "VFR" | "MVFR" | "IFR" | "LIFR";
const PIREP_FLIGHT_LEVEL_TYPES = ["GRND", "DURC", "DURD", "CRUISE", "OTHER", "UNKN"] as const;
export type PirepFlightLevelType = (typeof PIREP_FLIGHT_LEVEL_TYPES)[number];
export type CloudLayer = Readonly<{ cover: string; baseFtAgl: number | null }>;
export type MetarObservation = Readonly<{
  station: string; name: string | null; lon: number; lat: number; elevationFt: number | null; observedAt: string; raw: string;
  tempC: number | null; dewpointC: number | null; windDirDeg: number | null; windVariable: boolean; windKt: number | null; gustKt: number | null;
  visibilitySm: number | null; visibilityAtLeast: boolean; altimeterInHg: number | null; weather: string | null;
  clouds: readonly CloudLayer[]; ceilingFtAgl: number | null; ceilingCover: string | null; flightCategory: FlightCategory | null;
  providerCategory: string | null; densityAltitudeFt: number | null;
}>;
export type PirepReport = Readonly<{
  id: string; observedAt: string; aircraftType: string | null; lon: number; lat: number; altitudeFtMsl: number | null; flightLevelType: PirepFlightLevelType | null; urgent: boolean;
  turbulence: string | null; icing: string | null; skyCondition: string | null; raw: string;
}>;
export type AviationWeatherEnvelope<T> = Readonly<{ retrievedAt: string; sourceTitle: string; sourceUrl: string; evidenceRole: "EXTERNAL_CONTEXT_ONLY"; records: readonly T[]; dropped: number; limitation: string }>;

const isObject = (value: unknown): value is Record<string, unknown> => Boolean(value) && typeof value === "object" && !Array.isArray(value);
const num = (value: unknown, low: number, high: number): number | null => typeof value === "number" && Number.isFinite(value) && value >= low && value <= high ? value : null;
const str = (value: unknown, max = 512): string | null => typeof value === "string" && value.trim() && value.length <= max ? value.trim() : null;
const inRegion = (lon: number, lat: number) => lon >= -102.3 && lon <= -94.3 && lat >= 36.7 && lat <= 40.3;

/** AWC JSON carries `obsTime` as Unix seconds; ISO text is accepted for older payloads. */
export function observationTime(value: unknown): string | null {
  const milliseconds = typeof value === "number" && Number.isFinite(value) ? value * 1000
    : typeof value === "string" && /^\d{4}-\d{2}-\d{2}[T ]\d{2}:\d{2}(:\d{2}(\.\d+)?)?Z?$/.test(value.trim()) ? Date.parse(value.trim().replace(" ", "T").replace(/Z?$/, "Z")) : Number.NaN;
  return Number.isFinite(milliseconds) && milliseconds > Date.UTC(2000, 0, 1) ? new Date(milliseconds).toISOString() : null;
}

/** FAA categories: LIFR <500 ft or <1 SM; IFR 500–<1,000 or 1–<3; MVFR 1,000–3,000 or 3–5; VFR otherwise. */
export function flightCategory(ceilingFtAgl: number | null, visibilitySm: number | null): FlightCategory | null {
  if (ceilingFtAgl === null && visibilitySm === null) return null;
  const ceiling = ceilingFtAgl ?? Number.POSITIVE_INFINITY, visibility = visibilitySm ?? Number.POSITIVE_INFINITY;
  if (ceiling < 500 || visibility < 1) return "LIFR";
  if (ceiling < 1000 || visibility < 3) return "IFR";
  if (ceiling <= 3000 || visibility <= 5) return "MVFR";
  return "VFR";
}

/** Ceiling = lowest broken/overcast layer or vertical visibility (14 CFR 1.1). */
export function ceilingOf(clouds: readonly CloudLayer[], verticalVisibilityFt: number | null): Readonly<{ ft: number | null; cover: string | null }> {
  const layers = clouds.filter(layer => ["BKN", "OVC", "OVX"].includes(layer.cover) && layer.baseFtAgl !== null).map(layer => ({ ft: layer.baseFtAgl as number, cover: layer.cover }));
  if (verticalVisibilityFt !== null) layers.push({ ft: verticalVisibilityFt, cover: "VV" });
  layers.sort((left, right) => left.ft - right.ft);
  return layers[0] ?? { ft: null, cover: null };
}

/** Density altitude ≈ pressure altitude + 120 ft per °C above ISA (FAA-H-8083-25 rule of thumb). */
export function densityAltitudeFt(elevationFt: number | null, altimeterInHg: number | null, tempC: number | null): number | null {
  if (elevationFt === null || altimeterInHg === null || tempC === null) return null;
  const pressureAltitude = elevationFt + (29.92 - altimeterInHg) * 1000;
  const isa = 15 - 2 * (pressureAltitude / 1000);
  return Math.round(pressureAltitude + 120 * (tempC - isa));
}

const visibility = (value: unknown): Readonly<{ sm: number | null; atLeast: boolean }> => {
  if (typeof value === "string") {
    const match = value.trim().match(/^(\d+(?:\.\d+)?)(\+)?$/);
    return match ? { sm: Number(match[1]), atLeast: Boolean(match[2]) } : { sm: null, atLeast: false };
  }
  return { sm: num(value, 0, 100), atLeast: false };
};

/** Latest observation per station inside the Kansas region; malformed records are counted, not guessed. */
export function parseMetars(value: unknown, now: number): Readonly<{ records: readonly MetarObservation[]; dropped: number }> {
  if (!Array.isArray(value)) throw new Error("The METAR response was not a list.");
  const latest = new Map<string, MetarObservation>();
  let dropped = 0;
  for (const item of value.slice(0, MAX_METARS * 4)) {
    const lon = isObject(item) ? num(item.lon, -180, 180) : null, lat = isObject(item) ? num(item.lat, -90, 90) : null;
    const station = isObject(item) ? str(item.icaoId, 8) : null, observedAt = isObject(item) ? observationTime(item.obsTime) : null, raw = isObject(item) ? str(item.rawOb, 1024) : null;
    if (!isObject(item) || lon === null || lat === null || !station || !/^[A-Z0-9]{3,4}$/.test(station) || !observedAt || !raw || !inRegion(lon, lat)) { dropped++; continue; }
    const ageMinutes = (now - Date.parse(observedAt)) / 60000;
    if (ageMinutes > METAR_MAX_AGE_MINUTES || ageMinutes < -10) { dropped++; continue; }
    const clouds = (Array.isArray(item.clouds) ? item.clouds : []).filter(isObject).slice(0, 8)
      .map(layer => Object.freeze({ cover: str(layer.cover, 8) ?? "?", baseFtAgl: num(layer.base, 0, 60000) }));
    const vis = visibility(item.visib);
    // Vertical visibility (VVhhh) may arrive in hundreds of feet or in feet; the smallest real value is 100 ft.
    const verticalVisibility = num(item.vertVis, 0, 10000);
    const ceiling = ceilingOf(clouds, verticalVisibility === null ? null : verticalVisibility < 100 ? verticalVisibility * 100 : verticalVisibility);
    const elevationM = num(item.elev, -500, 5000);
    const altimeterRaw = num(item.altim, 20, 1100);
    // AWC reports altimeter in hPa; values under 40 are already inHg.
    const altimeterInHg = altimeterRaw === null ? null : altimeterRaw > 40 ? Math.round(altimeterRaw * 0.02953 * 100) / 100 : altimeterRaw;
    const tempC = num(item.temp, -80, 60), elevationFt = elevationM === null ? null : Math.round(elevationM / 0.3048);
    const record = Object.freeze({ station, name: str(item.name, 160), lon, lat, elevationFt, observedAt, raw, tempC, dewpointC: num(item.dewp, -80, 60),
      windDirDeg: num(item.wdir, 0, 360), windVariable: item.wdir === "VRB", windKt: num(item.wspd, 0, 250), gustKt: num(item.wgst, 0, 300),
      visibilitySm: vis.sm, visibilityAtLeast: vis.atLeast, altimeterInHg, weather: str(item.wxString, 64), clouds: Object.freeze(clouds),
      ceilingFtAgl: ceiling.ft, ceilingCover: ceiling.cover, flightCategory: flightCategory(ceiling.ft, vis.sm),
      providerCategory: str(item.fltCat, 8), densityAltitudeFt: densityAltitudeFt(elevationFt, altimeterInHg, tempC) });
    const previous = latest.get(station);
    if (!previous || previous.observedAt < observedAt) latest.set(station, record);
  }
  const records = [...latest.values()].sort((left, right) => left.station.localeCompare(right.station)).slice(0, MAX_METARS);
  return Object.freeze({ records: Object.freeze(records), dropped });
}

const intensity = (item: Record<string, unknown>, prefix: "tb" | "icg"): string | null => {
  const level = str(item[`${prefix}Int1`], 16);
  if (!level) return null;
  const base = num(item[`${prefix}Bas1`], 0, 600), top = num(item[`${prefix}Top1`], 0, 600), type = str(item[`${prefix}Type1`], 16);
  const span = base !== null || top !== null ? ` ${base === null ? "?" : `${base * 100}`}–${top === null ? "?" : `${top * 100}`} ft` : "";
  return `${level}${type ? ` ${type}` : ""}${span}`;
};

/** AWC PIREPJSON.fltLvl is a digit string in hundreds of feet; live JSON also uses numbers. */
const pirepFlightLevel = (value: unknown): number | null => {
  const parsed = typeof value === "string" && /^\d{1,3}$/.test(value.trim()) ? Number(value.trim()) : value;
  const level = num(parsed, 0, 600);
  return level !== null && Number.isInteger(level) ? level : null;
};

/** See https://aviationweather.gov/data/schema/openapi.yaml (PIREPJSON and CloudInfo). */
export function parsePireps(value: unknown, now: number, maxAgeHours = 3): Readonly<{ records: readonly PirepReport[]; dropped: number }> {
  if (!Array.isArray(value)) throw new Error("The PIREP response was not a list.");
  const records: PirepReport[] = [];
  let dropped = 0;
  for (const item of value.slice(0, MAX_PIREPS * 4)) {
    const lon = isObject(item) ? num(item.lon, -180, 180) : null, lat = isObject(item) ? num(item.lat, -90, 90) : null;
    const observedAt = isObject(item) ? observationTime(item.obsTime) : null, raw = isObject(item) ? str(item.rawOb, 1024) : null;
    if (!isObject(item) || lon === null || lat === null || !observedAt || !raw || !inRegion(lon, lat)) { dropped++; continue; }
    const ageHours = (now - Date.parse(observedAt)) / 3600000;
    if (ageHours > maxAgeHours || ageHours < -0.25) { dropped++; continue; }
    const phase = str(item.fltLvlType, 8);
    const flightLevelType = PIREP_FLIGHT_LEVEL_TYPES.find(type => type === phase) ?? null;
    // A climb/descent observation spans changing altitudes, not a single fixed flight level.
    const level = flightLevelType === "DURC" || flightLevelType === "DURD" ? null : pirepFlightLevel(item.fltLvl);
    const cloud = Array.isArray(item.clouds) ? item.clouds.filter(isObject).map(layer => {
      // CloudInfo.base is already integer feet, unlike fltLvl; do not scale it by 100.
      const base = num(layer.base, 0, 60000);
      return [str(layer.cover, 8), base !== null && Number.isInteger(base) ? `${base} ft` : null].filter(Boolean).join(" ");
    }).filter(Boolean).join(", ") : "";
    records.push(Object.freeze({ id: `${observedAt}:${lon.toFixed(3)}:${lat.toFixed(3)}:${records.length}`, observedAt, aircraftType: str(item.acType, 16), lon, lat,
      altitudeFtMsl: level === null ? null : level * 100, flightLevelType, urgent: /urgent|UUA/i.test(String(item.pirepType ?? "")) || /^\s*\S+\s+UUA\b/.test(raw),
      turbulence: intensity(item, "tb"), icing: intensity(item, "icg"), skyCondition: cloud || null, raw }));
    if (records.length >= MAX_PIREPS) break;
  }
  records.sort((left, right) => right.observedAt.localeCompare(left.observedAt));
  return Object.freeze({ records: Object.freeze(records), dropped });
}

export type VfrCheck = Readonly<{ meets: boolean | null; text: string; cite: string }>;

/**
 * Basic VFR weather against a column class at the surface, using the nearest
 * station. A station report describes its own site, not every point nearby.
 */
export function basicVfrCheck(airspaceClass: "B" | "C" | "D" | "E" | "G", metar: Pick<MetarObservation, "ceilingFtAgl" | "visibilitySm" | "station"> | null): VfrCheck {
  if (!metar || metar.visibilitySm === null) return Object.freeze({ meets: null, text: "No usable nearby observation; VFR status is unknown.", cite: "14 CFR 91.155" });
  const ceiling = metar.ceilingFtAgl ?? Number.POSITIVE_INFINITY;
  if (airspaceClass === "G") {
    const meets = metar.visibilitySm >= 1;
    return Object.freeze({ meets, text: `${metar.station}: ${metar.visibilitySm} SM ${meets ? "meets" : "is below"} Class G day minimum (1 SM).`, cite: "14 CFR 91.155(a)" });
  }
  const meets = ceiling >= 1000 && metar.visibilitySm >= 3;
  const ceilingText = metar.ceilingFtAgl === null ? "no ceiling" : `ceiling ${metar.ceilingFtAgl.toLocaleString("en-US")} ft`;
  return Object.freeze({ meets, text: `${metar.station}: ${ceilingText}, ${metar.visibilitySm} SM — ${meets ? "meets" : "below"} basic VFR (1,000 ft ceiling, 3 SM) for the ${airspaceClass === "E" ? "surface area" : `Class ${airspaceClass}`}${meets ? "" : "; special VFR or IFR needed"}.`,
    cite: "14 CFR 91.155(c), 91.157" });
}

export const FLIGHT_CATEGORY_COLORS: Readonly<Record<FlightCategory, string>> = Object.freeze({ VFR: "#2e9d4f", MVFR: "#2f6fd8", IFR: "#d33a2c", LIFR: "#b0329f" });

export function metarFeatures(records: readonly MetarObservation[], exaggeration: number): Readonly<{ stations: GeoJSON.FeatureCollection; ceilings: GeoJSON.FeatureCollection }> {
  const stations: GeoJSON.Feature[] = records.map(record => ({ type: "Feature", id: record.station, geometry: { type: "Point", coordinates: [record.lon, record.lat] },
    properties: { station: record.station, category: record.flightCategory ?? "UNKNOWN", color: record.flightCategory ? FLIGHT_CATEGORY_COLORS[record.flightCategory] : "#7a7a7a",
      label: `${record.station} ${record.flightCategory ?? "?"}${record.windKt !== null ? ` · ${record.windVariable ? "VRB" : String(record.windDirDeg ?? "").padStart(3, "0")}@${record.windKt}${record.gustKt ? `G${record.gustKt}` : ""}kt` : ""}`,
      wind_dir: record.windDirDeg ?? 0, wind_kt: record.windKt ?? 0 } }));
  // A ceiling is drawn as a thin disc ~2.5 km across at its reported height above the station.
  const ceilings: GeoJSON.Feature[] = records.filter(record => record.ceilingFtAgl !== null && record.ceilingFtAgl <= 12000).map(record => {
    const radiusKm = 1.25, steps = 24, kmPerLon = 111.32 * Math.cos(record.lat * Math.PI / 180);
    const ring = Array.from({ length: steps + 1 }, (_, i) => { const angle = (i % steps) / steps * 2 * Math.PI; return [record.lon + Math.cos(angle) * radiusKm / kmPerLon, record.lat + Math.sin(angle) * radiusKm / 110.57]; });
    const base = (record.ceilingFtAgl as number) * 0.3048 * exaggeration;
    return { type: "Feature", id: `ceiling:${record.station}`, geometry: { type: "Polygon", coordinates: [ring] },
      properties: { station: record.station, base, top: base + 40 * exaggeration, color: record.flightCategory ? FLIGHT_CATEGORY_COLORS[record.flightCategory] : "#9a9a9a",
        label: `${record.station} ${record.ceilingCover} ${(record.ceilingFtAgl as number).toLocaleString("en-US")} ft AGL` } };
  });
  return Object.freeze({ stations: { type: "FeatureCollection", features: stations }, ceilings: { type: "FeatureCollection", features: ceilings } });
}

export function pirepAltitudeLabel(record: Pick<PirepReport, "altitudeFtMsl" | "flightLevelType">): string {
  return record.flightLevelType === "DURC" ? "climb (altitude varies)" : record.flightLevelType === "DURD" ? "descent (altitude varies)"
    : record.altitudeFtMsl === null ? "altitude unavailable" : `${record.altitudeFtMsl.toLocaleString("en-US")} ft MSL`;
}

/**
 * Pilot reports with a fixed altitude are placed above an approximate ground
 * elevation (nearest airport). Unknown/variable heights stay in the inspector,
 * not at an invented zero in the altitude layer.
 */
export function pirepFeatures(records: readonly PirepReport[], groundFtAt: (lon: number, lat: number) => number, exaggeration: number): GeoJSON.FeatureCollection {
  const features: GeoJSON.Feature[] = records.filter(record => record.altitudeFtMsl !== null).map(record => {
    const aboveGround = Math.max(0, (record.altitudeFtMsl as number) - groundFtAt(record.lon, record.lat));
    const half = 0.012, kmLift = aboveGround * 0.3048 * exaggeration;
    return { type: "Feature", id: record.id, geometry: { type: "Polygon", coordinates: [[[record.lon - half, record.lat - half], [record.lon + half, record.lat - half], [record.lon + half, record.lat + half], [record.lon - half, record.lat + half], [record.lon - half, record.lat - half]]] },
      properties: { id: record.id, base: kmLift, top: kmLift + 120 * exaggeration, urgent: record.urgent,
        altitude_ft_msl: record.altitudeFtMsl, flight_level_type: record.flightLevelType,
        color: record.urgent ? "#d33a2c" : record.turbulence || record.icing ? "#e08a1c" : "#4a6fa5",
        label: `${record.urgent ? "UUA " : ""}${record.aircraftType ?? "Aircraft"} ${pirepAltitudeLabel(record)}${record.turbulence ? ` · TB ${record.turbulence}` : ""}${record.icing ? ` · IC ${record.icing}` : ""}` } };
  });
  return { type: "FeatureCollection", features };
}
