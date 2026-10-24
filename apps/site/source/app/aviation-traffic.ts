/**
 * Live aircraft positions from public, community-run ADS-B/Mode S receiver
 * networks (readsb / ADSBExchange-v2-compatible JSON). Observed positions only:
 * coverage is receiver-dependent, so an empty sky on the map is not evidence of
 * no traffic, and nothing here identifies owners, missions or intent.
 */
export const AVIATION_TRAFFIC_API_PATH = "/api/aviation/traffic";
// Kansas centre; 250 NM reaches every corner of the state (~200 NM) with margin.
export const TRAFFIC_CENTER = Object.freeze({ lat: 38.5, lon: -98.35, radiusNm: 250 });

export type TrafficProvider = Readonly<{ id: "adsb-lol" | "adsb-fi"; title: string; url: string; homepage: string; terms: string }>;
// Fixed, ordered provider list; the server never builds an upstream URL from caller input.
// adsb.lol needs no key today but says one will be required "in the future"; adsb.fi then carries the layer.
// adsb.fi marks its /v2/lat route deprecated in favour of /v3 (max 250 NM, 1 request/second).
export const TRAFFIC_PROVIDERS: readonly TrafficProvider[] = Object.freeze([
  Object.freeze({ id: "adsb-lol", title: "adsb.lol", url: `https://api.adsb.lol/v2/point/${TRAFFIC_CENTER.lat}/${TRAFFIC_CENTER.lon}/${TRAFFIC_CENTER.radiusNm}`,
    homepage: "https://adsb.lol/", terms: "Open Database License (ODbL) 1.0: attribution and share-alike." }),
  Object.freeze({ id: "adsb-fi", title: "adsb.fi", url: `https://opendata.adsb.fi/api/v3/lat/${TRAFFIC_CENTER.lat}/lon/${TRAFFIC_CENTER.lon}/dist/${TRAFFIC_CENTER.radiusNm}`,
    homepage: "https://adsb.fi/", terms: "adsb.fi open data: personal, non-commercial use with attribution and a link to adsb.fi." }),
]);
export const TRAFFIC_MAX_POSITION_AGE_S = 60;
export const TRAFFIC_MAX_AIRCRAFT = 3000;

export type Aircraft = Readonly<{
  hex: string; callsign: string | null; registration: string | null; type: string | null; category: string | null;
  lon: number; lat: number; onGround: boolean; altBaroFt: number | null; altGeomFt: number | null;
  groundSpeedKt: number | null; trackDeg: number | null; verticalRateFpm: number | null; squawk: string | null;
  emergency: string | null; positionAgeS: number; military: boolean;
}>;
export type TrafficEnvelope = Readonly<{ retrievedAt: string; provider: TrafficProvider; evidenceRole: "EXTERNAL_CONTEXT_ONLY";
  records: readonly Aircraft[]; dropped: number; limitation: string }>;

const isObject = (value: unknown): value is Record<string, unknown> => Boolean(value) && typeof value === "object" && !Array.isArray(value);
const num = (value: unknown, low: number, high: number): number | null => typeof value === "number" && Number.isFinite(value) && value >= low && value <= high ? value : null;
const str = (value: unknown, pattern: RegExp): string | null => typeof value === "string" && pattern.test(value.trim()) ? value.trim() : null;
// The state plus ~50 NM, so aircraft about to cross the border stay visible.
const inRegion = (lon: number, lat: number) => lon >= -103.2 && lon <= -93.6 && lat >= 36.2 && lat <= 40.9;
const EMERGENCY_SQUAWKS: Readonly<Record<string, string>> = Object.freeze({ "7500": "unlawful interference", "7600": "radio failure", "7700": "general emergency" });

/** readsb `alt_baro` is feet or the string "ground"; positions older than 60 s are dropped, not extrapolated. */
export function parseTraffic(value: unknown): Readonly<{ records: readonly Aircraft[]; dropped: number }> {
  if (!isObject(value)) throw new Error("The traffic response was not an object.");
  const list = Array.isArray(value.ac) ? value.ac : Array.isArray(value.aircraft) ? value.aircraft : null;
  if (!list) throw new Error("The traffic response had no aircraft list.");
  const seen = new Set<string>();
  const records: Aircraft[] = [];
  let dropped = 0;
  for (const item of list.slice(0, TRAFFIC_MAX_AIRCRAFT * 2)) {
    const hex = isObject(item) ? str(item.hex, /^~?[0-9a-fA-F]{6}$/) : null;
    const lon = isObject(item) ? num(item.lon, -180, 180) : null, lat = isObject(item) ? num(item.lat, -90, 90) : null;
    const age = isObject(item) ? num(item.seen_pos, 0, 86400) ?? num(item.seen, 0, 86400) : null;
    if (!isObject(item) || !hex || lon === null || lat === null || age === null || age > TRAFFIC_MAX_POSITION_AGE_S || !inRegion(lon, lat) || seen.has(hex.toLowerCase())) { dropped++; continue; }
    seen.add(hex.toLowerCase());
    const onGround = item.alt_baro === "ground";
    const squawk = str(item.squawk, /^[0-7]{4}$/);
    const declared = typeof item.emergency === "string" && item.emergency !== "none" && /^[a-z]{3,16}$/.test(item.emergency) ? item.emergency : null;
    records.push(Object.freeze({ hex: hex.toLowerCase(), callsign: str(item.flight, /^[A-Z0-9-]{1,8}$/i)?.toUpperCase() ?? null,
      registration: str(item.r, /^[A-Z0-9-]{1,10}$/i), type: str(item.t, /^[A-Z0-9]{2,4}$/i), category: str(item.category, /^[A-D][0-7]$/),
      lon, lat, onGround, altBaroFt: onGround ? 0 : num(item.alt_baro, -1500, 70000), altGeomFt: num(item.alt_geom, -1500, 70000),
      groundSpeedKt: num(item.gs, 0, 1500), trackDeg: num(item.track, 0, 360), verticalRateFpm: num(item.baro_rate, -20000, 20000) ?? num(item.geom_rate, -20000, 20000),
      squawk, emergency: declared ?? (squawk ? EMERGENCY_SQUAWKS[squawk] ?? null : null), positionAgeS: age,
      military: typeof item.dbFlags === "number" && (item.dbFlags & 1) === 1 }));
    if (records.length >= TRAFFIC_MAX_AIRCRAFT) break;
  }
  records.sort((left, right) => left.hex.localeCompare(right.hex));
  return Object.freeze({ records: Object.freeze(records), dropped });
}

/** Barometric altitude is pressure altitude above 18,000 ft; below it either reported altitude is close to MSL. */
export const aircraftAltitudeMsl = (aircraft: Pick<Aircraft, "onGround" | "altBaroFt" | "altGeomFt">): number | null =>
  aircraft.onGround ? null : aircraft.altGeomFt ?? aircraft.altBaroFt;

export const TRAFFIC_ALTITUDE_COLORS: readonly (readonly [number, string])[] = Object.freeze([
  [0, "#7d8a96"], [1000, "#e6a23c"], [5000, "#d4c23a"], [10000, "#3fae6b"], [18000, "#2f86c9"], [30000, "#7c5cc4"],
]);
const altitudeColor = (feet: number | null) => feet === null ? TRAFFIC_ALTITUDE_COLORS[0][1] : [...TRAFFIC_ALTITUDE_COLORS].reverse().find(([floor]) => feet >= floor)?.[1] ?? TRAFFIC_ALTITUDE_COLORS[0][1];

/**
 * Each aircraft is a small arrowhead pointing along its track, lifted to its
 * altitude above an approximate ground elevation (nearest airport). Emergencies
 * are red. The marker is ~1.3 km long so it stays visible at regional zoom.
 */
export function trafficFeatures(records: readonly Aircraft[], groundFtAt: (lon: number, lat: number) => number, exaggeration: number,
  occupied: (aircraft: Aircraft, groundFt: number) => string): GeoJSON.FeatureCollection {
  const features: GeoJSON.Feature[] = records.map(aircraft => {
    const ground = groundFtAt(aircraft.lon, aircraft.lat);
    const msl = aircraftAltitudeMsl(aircraft);
    const lift = msl === null ? 0 : Math.max(0, msl - ground) * 0.3048 * exaggeration;
    const heading = ((aircraft.trackDeg ?? 0) * Math.PI) / 180, kmPerLon = 111.32 * Math.cos(aircraft.lat * Math.PI / 180);
    const point = (forwardKm: number, rightKm: number) => [
      aircraft.lon + (forwardKm * Math.sin(heading) + rightKm * Math.cos(heading)) / kmPerLon,
      aircraft.lat + (forwardKm * Math.cos(heading) - rightKm * Math.sin(heading)) / 110.57,
    ];
    const ring = [point(0.8, 0), point(-0.5, 0.45), point(-0.25, 0), point(-0.5, -0.45), point(0.8, 0)];
    const altitudeText = aircraft.onGround ? "on ground" : msl === null ? "altitude n/a" : `${Math.round(msl).toLocaleString("en-US")} ft`;
    return { type: "Feature", id: aircraft.hex, geometry: { type: "Polygon", coordinates: [ring] },
      properties: { hex: aircraft.hex, base: lift, top: lift + 90 * exaggeration, emergency: Boolean(aircraft.emergency),
        color: aircraft.emergency ? "#e0301e" : altitudeColor(msl),
        label: `${aircraft.callsign ?? aircraft.registration ?? aircraft.hex.toUpperCase()}${aircraft.type ? ` ${aircraft.type}` : ""} · ${altitudeText}${aircraft.groundSpeedKt !== null ? ` · ${Math.round(aircraft.groundSpeedKt)} kt` : ""}${aircraft.emergency ? ` · ${aircraft.squawk ?? ""} ${aircraft.emergency.toUpperCase()}` : ""}`,
        airspace: msl === null ? "surface" : occupied(aircraft, ground) } };
  });
  return { type: "FeatureCollection", features };
}

