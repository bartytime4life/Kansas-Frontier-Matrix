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
// Access terms checked 2026-11-04; do not treat fallback permission as a commercial license.
// adsb.fi marks its /v2/lat route deprecated in favour of /v3 (max 250 NM, 1 request/second).
export const TRAFFIC_PROVIDERS: readonly TrafficProvider[] = Object.freeze([
  Object.freeze({ id: "adsb-lol", title: "adsb.lol", url: `https://api.adsb.lol/v2/point/${TRAFFIC_CENTER.lat}/${TRAFFIC_CENTER.lon}/${TRAFFIC_CENTER.radiusNm}`,
    homepage: "https://adsb.lol/", terms: "Open Database License (ODbL) 1.0: attribution and share-alike." }),
  Object.freeze({ id: "adsb-fi", title: "adsb.fi", url: `https://opendata.adsb.fi/api/v3/lat/${TRAFFIC_CENTER.lat}/lon/${TRAFFIC_CENTER.lon}/dist/${TRAFFIC_CENTER.radiusNm}`,
    homepage: "https://adsb.fi/", terms: "adsb.fi open data: personal, non-commercial use with attribution and a link to adsb.fi." }),
]);
export const TRAFFIC_MAX_POSITION_AGE_S = 60;
export const TRAFFIC_MAX_AIRCRAFT = 3000;
export const TRAFFIC_MAX_SPEED_KT = 1500;

export type Aircraft = Readonly<{
  hex: string; callsign: string | null; registration: string | null; type: string | null; category: string | null;
  lon: number; lat: number; onGround: boolean; altBaroFt: number | null; altGeomFt: number | null;
  groundSpeedKt: number | null; trackDeg: number | null; verticalRateFpm: number | null; squawk: string | null;
  emergency: string | null; positionAgeS: number; military: boolean;
  observedAt?: string; timestampBasis?: "provider" | "retrieval-estimate";
  positionMethod?: string | null; rollDeg?: number | null; indicatedAirSpeedKt?: number | null;
  mach?: number | null; interpolated?: boolean;
  trueHeadingDeg?: number | null;
  /** Display calculations stay separate from the earlier source observation. */
  sampledAt?: string;
  renderedTrackDeg?: number | null;
  interpolation?: Readonly<{ fromObservedAt: string; toObservedAt: string; model: "bounded-hermite" | "great-circle" }>;
  verticalRateReference?: "barometric" | "geometric" | null;
  positionQuality?: Readonly<{ nic: number | null; nacP: number | null; sil: number | null; rcM: number | null; rssi: number | null }>;
  traceFlags?: number;
}>;
export type TrafficEnvelope = Readonly<{ retrievedAt: string; provider: TrafficProvider; evidenceRole: "EXTERNAL_CONTEXT_ONLY";
  records: readonly Aircraft[]; dropped: number; truncated?: boolean; limitation: string }>;

const isObject = (value: unknown): value is Record<string, unknown> => Boolean(value) && typeof value === "object" && !Array.isArray(value);
const num = (value: unknown, low: number, high: number): number | null => typeof value === "number" && Number.isFinite(value) && value >= low && value <= high ? value : null;
const str = (value: unknown, pattern: RegExp): string | null => typeof value === "string" && pattern.test(value.trim()) ? value.trim() : null;
// The state plus ~50 NM, so aircraft about to cross the border stay visible.
const inRegion = (lon: number, lat: number) => lon >= -103.2 && lon <= -93.6 && lat >= 36.2 && lat <= 40.9;
const EMERGENCY_SQUAWKS: Readonly<Record<string, string>> = Object.freeze({ "7500": "unlawful interference", "7600": "radio failure", "7700": "general emergency" });

/** readsb `alt_baro` is feet or the string "ground"; positions older than 60 s are dropped, not extrapolated. */
export function parseTraffic(value: unknown, retrievedAt = Date.now()): Readonly<{ records: readonly Aircraft[]; dropped: number; truncated: boolean }> {
  if (!isObject(value)) throw new Error("The traffic response was not an object.");
  const list = Array.isArray(value.ac) ? value.ac : Array.isArray(value.aircraft) ? value.aircraft : null;
  if (!list) throw new Error("The traffic response had no aircraft list.");
  const rawNow = num(value.now, 1_000_000_000, 9_000_000_000_000);
  const providerNow = rawNow === null ? null : rawNow > 1e12 ? rawNow : rawNow * 1000;
  if (!Number.isFinite(retrievedAt) || (providerNow !== null && (providerNow > retrievedAt + 5000 || providerNow < retrievedAt - 60_000))) throw new Error("The traffic snapshot is stale or future-dated.");
  const snapshot = providerNow ?? retrievedAt;
  const seen = new Set<string>();
  const records: Aircraft[] = [];
  let dropped = Math.max(0, list.length - TRAFFIC_MAX_AIRCRAFT * 2);
  let scanned = 0;
  for (const item of list.slice(0, TRAFFIC_MAX_AIRCRAFT * 2)) {
    scanned++;
    const hex = isObject(item) ? str(item.hex, /^~?[0-9a-fA-F]{6}$/) : null;
    const lon = isObject(item) ? num(item.lon, -180, 180) : null, lat = isObject(item) ? num(item.lat, -90, 90) : null;
    const age = isObject(item) ? num(item.seen_pos, 0, 86400) : null;
    if (!isObject(item) || !hex || lon === null || lat === null || age === null || age + Math.max(0, (retrievedAt - snapshot) / 1000) > TRAFFIC_MAX_POSITION_AGE_S || !inRegion(lon, lat) || seen.has(hex.toLowerCase())) { dropped++; continue; }
    seen.add(hex.toLowerCase());
    const onGround = item.alt_baro === "ground";
    const squawk = str(item.squawk, /^[0-7]{4}$/);
    const declared = typeof item.emergency === "string" && item.emergency !== "none" && /^[a-z]{3,16}$/.test(item.emergency) ? item.emergency : null;
    records.push(Object.freeze({ hex: hex.toLowerCase(), callsign: str(item.flight, /^[A-Z0-9-]{1,8}$/i)?.toUpperCase() ?? null,
      registration: str(item.r, /^[A-Z0-9-]{1,10}$/i), type: str(item.t, /^[A-Z0-9]{2,4}$/i), category: str(item.category, /^[A-D][0-7]$/),
      lon, lat, onGround, altBaroFt: onGround ? 0 : num(item.alt_baro, -1500, 70000), altGeomFt: num(item.alt_geom, -1500, 70000),
      groundSpeedKt: num(item.gs, 0, TRAFFIC_MAX_SPEED_KT), trackDeg: num(item.track, 0, 360), trueHeadingDeg: num(item.true_heading, 0, 360), verticalRateFpm: num(item.baro_rate, -20000, 20000) ?? num(item.geom_rate, -20000, 20000),
      squawk, emergency: declared ?? (squawk ? EMERGENCY_SQUAWKS[squawk] ?? null : null), positionAgeS: age + Math.max(0, (retrievedAt - snapshot) / 1000),
      observedAt: new Date(snapshot - age * 1000).toISOString(), timestampBasis: providerNow === null ? "retrieval-estimate" : "provider",
      positionMethod: str(item.type, /^[a-z0-9_]{1,32}$/), rollDeg: num(item.roll, -180, 180),
      indicatedAirSpeedKt: num(item.ias, 0, 1500), mach: num(item.mach, 0, 5),
      verticalRateReference: num(item.baro_rate, -20000, 20000) !== null ? "barometric" : num(item.geom_rate, -20000, 20000) !== null ? "geometric" : null,
      positionQuality: { nic: num(item.nic, 0, 11), nacP: num(item.nac_p, 0, 11), sil: num(item.sil, 0, 3), rcM: num(item.rc, 0, 100000), rssi: num(item.rssi, -100, 0) },
      military: typeof item.dbFlags === "number" && (item.dbFlags & 1) === 1 }));
    if (records.length >= TRAFFIC_MAX_AIRCRAFT) break;
  }
  records.sort((left, right) => left.hex.localeCompare(right.hex));
  dropped += Math.max(0, Math.min(list.length, TRAFFIC_MAX_AIRCRAFT * 2) - scanned);
  return Object.freeze({ records: Object.freeze(records), dropped, truncated: scanned < list.length });
}

// The route's edge cache serves a response for at most max-age 15 s + stale-while-revalidate 15 s.
export const TRAFFIC_MAX_CACHE_AGE_S = 30;

/**
 * Records still inside the 60-second position limit at `now`. A record's age is
 * its age at retrieval, plus how long the response sat in the edge cache (from
 * the server's `retrievedAt`, with no upper clamp: an old cached response must not
 * become live because its cache age was capped), plus the time since this browser received it.
 * Returns the same array while the kept set is unchanged (including one shared
 * empty array), so callers keyed on identity redraw only when a position expires.
 */
export function freshAircraft(load: (Pick<TrafficEnvelope, "retrievedAt" | "records"> & { receivedAt: number }) | null, now: number): readonly Aircraft[] {
  const retrieved = load ? Date.parse(load.retrievedAt) : Number.NaN;
  if (!load || !Number.isFinite(retrieved) || !Number.isFinite(load.receivedAt)) return NO_AIRCRAFT;
  if (retrieved > load.receivedAt + TRAFFIC_MAX_CACHE_AGE_S * 1000) return NO_AIRCRAFT;
  const cachedS = Math.max(0, (load.receivedAt - retrieved) / 1000);
  const elapsedS = cachedS + Math.max(0, (now - load.receivedAt) / 1000);
  const kept = load.records.filter(record => record.positionAgeS + elapsedS <= TRAFFIC_MAX_POSITION_AGE_S);
  if (!kept.length) return NO_AIRCRAFT;
  if (kept.length === load.records.length) return load.records;
  // For one response the kept sets are nested (one age threshold), so an equal count means an equal set.
  const previous = keptByLoad.get(load);
  if (previous?.length === kept.length) return previous;
  keptByLoad.set(load, kept);
  return kept;
}
const NO_AIRCRAFT: readonly Aircraft[] = Object.freeze([]);
const keptByLoad = new WeakMap<object, readonly Aircraft[]>();

/** Render-only approximation. GNSS is WGS84 ellipsoid height; barometric is pressure altitude, neither is established MSL. */
export const aircraftDisplayAltitude = (aircraft: Pick<Aircraft, "onGround" | "altBaroFt" | "altGeomFt">): number | null =>
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
  _occupied: (aircraft: Aircraft, groundFt: number) => string): GeoJSON.FeatureCollection {
  // Preserve the legacy call signature without treating approximate heights as occupancy evidence.
  void _occupied;
  const features: GeoJSON.Feature[] = records.map(aircraft => {
    const ground = groundFtAt(aircraft.lon, aircraft.lat);
    const msl = aircraftDisplayAltitude(aircraft);
    const lift = msl === null ? 0 : Math.max(0, msl - ground) * 0.3048 * exaggeration;
    const heading = ((aircraft.trackDeg ?? 0) * Math.PI) / 180, kmPerLon = 111.32 * Math.cos(aircraft.lat * Math.PI / 180);
    const point = (forwardKm: number, rightKm: number) => [
      aircraft.lon + (forwardKm * Math.sin(heading) + rightKm * Math.cos(heading)) / kmPerLon,
      aircraft.lat + (forwardKm * Math.cos(heading) - rightKm * Math.sin(heading)) / 110.57,
    ];
    const ring = [point(0.8, 0), point(-0.5, 0.45), point(-0.25, 0), point(-0.5, -0.45), point(0.8, 0)];
    const altitudeText = aircraft.onGround ? "on ground" : msl === null ? "altitude n/a" : `${Math.round(msl).toLocaleString("en-US")} ft ${aircraft.altGeomFt !== null ? "WGS84" : "pressure"}`;
    return { type: "Feature", id: aircraft.hex, geometry: { type: "Polygon", coordinates: [ring] },
      properties: { hex: aircraft.hex, base: lift, top: lift + 90 * exaggeration, groundFt: ground, emergency: Boolean(aircraft.emergency),
        color: aircraft.emergency ? "#e0301e" : altitudeColor(msl),
        label: `${aircraft.callsign ?? aircraft.registration ?? aircraft.hex.toUpperCase()}${aircraft.type ? ` ${aircraft.type}` : ""} · ${altitudeText}${aircraft.groundSpeedKt !== null ? ` · ${Math.round(aircraft.groundSpeedKt)} kt` : ""}${aircraft.emergency ? ` · ${aircraft.squawk ?? ""} ${aircraft.emergency.toUpperCase()}` : ""}`,
        airspace: aircraft.onGround ? "surface report" : "Not established: altitude datum differs from airspace limits" } };
  });
  return { type: "FeatureCollection", features };
}

