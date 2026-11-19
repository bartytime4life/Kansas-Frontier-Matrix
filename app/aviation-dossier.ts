/**
 * Airport dossier helpers: the observed activity board around one public-use
 * airport, the temporary flight restrictions whose drawn area reaches it, and
 * runway summaries. Everything is derived from data already in the browser:
 * the same traffic envelope the map draws, the pinned NASR airport record and
 * the TFR shapes already drawn. The board is an observation list, not an
 * arrivals/departures schedule: this site knows no flight plans.
 *
 * No runtime imports: tests load this file as a standalone module.
 */
import type { Aircraft } from "./aviation-traffic";
import type { AviationAirport, AviationRunway } from "./aviation-airspace";
import type { TfrShape } from "./aviation-drone-data";
import { PHASE_LOW_HEIGHT_FT, PHASE_LOW_RADIUS_NM, distanceNm, reportedHeightFt, verticalTrend, type PhaseTrend } from "./aviation-phase";

export const ACTIVITY_RADIUS_NM = PHASE_LOW_RADIUS_NM;
export const ACTIVITY_HEIGHT_FT = PHASE_LOW_HEIGHT_FT;
/** A track within this many degrees of the bearing to (or from) the field counts as pointed toward (or away from) it. */
export const ACTIVITY_HEADING_TOLERANCE_DEG = 60;
export const ACTIVITY_MAX_ROWS = 40;
export type ActivityGroup = "descending-toward" | "climbing-away" | "on-surface" | "other-low";
export const ACTIVITY_GROUP_TITLES: Readonly<Record<ActivityGroup, string>> = Object.freeze({
  "descending-toward": "Descending, track toward the field",
  "climbing-away": "Climbing, track away from the field",
  "on-surface": "On the surface (reported)",
  "other-low": "Other low traffic nearby (level, crossing or rate not reported)",
});
export const ACTIVITY_BASIS = `Aircraft within ${ACTIVITY_RADIUS_NM} NM and ${ACTIVITY_HEIGHT_FT.toLocaleString("en-US")} ft above field elevation, from the live receiver feed. Groups use the reported vertical rate and the reported track against the bearing to the field; no arrival, departure or destination is known to this site.`;

export type ActivityRow = Readonly<{
  hex: string; label: string; type: string | null; group: ActivityGroup; trend: PhaseTrend | null;
  distanceNm: number; bearingToFieldDeg: number; trackDeg: number | null; aboveFieldFt: number | null; verticalRateFpm: number | null;
  observationAgeS: number | null; emergency: string | null; basis: string;
}>;
export type ActivityBoard = Readonly<{ rows: readonly ActivityRow[]; groups: Readonly<Record<ActivityGroup, readonly ActivityRow[]>>; truncated: boolean }>;

/** Initial great-circle bearing from the aircraft to the field, 0–360. */
export function bearingDeg(fromLon: number, fromLat: number, toLon: number, toLat: number): number {
  const toRad = Math.PI / 180, p1 = fromLat * toRad, p2 = toLat * toRad, dl = (toLon - fromLon) * toRad;
  const y = Math.sin(dl) * Math.cos(p2), x = Math.cos(p1) * Math.sin(p2) - Math.sin(p1) * Math.cos(p2) * Math.cos(dl);
  return ((Math.atan2(y, x) * 180) / Math.PI + 360) % 360;
}

export const angleDiffDeg = (a: number, b: number): number => { const d = Math.abs(((a - b) % 360) + 360) % 360; return d > 180 ? 360 - d : d; };

const activityGroup = (aircraft: Pick<Aircraft, "onGround" | "trackDeg">, trend: PhaseTrend | null, bearingToField: number): ActivityGroup => {
  if (aircraft.onGround) return "on-surface";
  if (aircraft.trackDeg === null || trend === null || trend === "level") return "other-low";
  const toward = angleDiffDeg(aircraft.trackDeg, bearingToField) <= ACTIVITY_HEADING_TOLERANCE_DEG;
  const away = angleDiffDeg(aircraft.trackDeg, (bearingToField + 180) % 360) <= ACTIVITY_HEADING_TOLERANCE_DEG;
  if (trend === "descending" && toward) return "descending-toward";
  if (trend === "climbing" && away) return "climbing-away";
  return "other-low";
};

const label = (aircraft: Pick<Aircraft, "callsign" | "registration" | "hex">) => aircraft.callsign ?? aircraft.registration ?? aircraft.hex.toUpperCase();
const fpm = (value: number) => `${value > 0 ? "+" : ""}${Math.round(value).toLocaleString("en-US")} ft/min`;

/**
 * Observed aircraft within 10 NM of the airport and no more than 3,000 ft above
 * its field elevation, grouped by reported rate and track. `now` is the clock
 * the observation ages are measured against (milliseconds).
 */
export function activityBoard(airport: Pick<AviationAirport, "lon" | "lat" | "elevation_ft">, aircraft: readonly Aircraft[], now: number): ActivityBoard {
  const rows: ActivityRow[] = [];
  for (const record of aircraft) {
    const nm = distanceNm(record.lon, record.lat, airport.lon, airport.lat);
    if (nm > ACTIVITY_RADIUS_NM) continue;
    const height = reportedHeightFt(record);
    const aboveField = height === null ? null : Math.round(height - airport.elevation_ft);
    if (!record.onGround && (aboveField === null || aboveField > ACTIVITY_HEIGHT_FT)) continue;
    const trend = record.onGround ? null : verticalTrend(record.verticalRateFpm);
    const bearing = Math.round(bearingDeg(record.lon, record.lat, airport.lon, airport.lat));
    const group = activityGroup(record, trend, bearing);
    const observed = typeof record.observedAt === "string" ? Date.parse(record.observedAt) : Number.NaN;
    const ageS = Number.isFinite(observed) ? Math.max(0, Math.round((now - observed) / 1000)) : null;
    const basis = record.onGround ? "Reported surface flag."
      : `${record.verticalRateFpm === null ? "rate not reported" : `rate ${fpm(record.verticalRateFpm)}`}; track ${record.trackDeg === null ? "not reported" : `${Math.round(record.trackDeg)}°`} vs bearing to field ${bearing}°; ${aboveField === null ? "height not reported" : `${aboveField.toLocaleString("en-US")} ft above field`} (${record.altGeomFt !== null ? "WGS84 geometric" : "pressure altitude"}).`;
    rows.push(Object.freeze({ hex: record.hex, label: label(record), type: record.type, group, trend, distanceNm: Math.round(nm * 10) / 10, bearingToFieldDeg: bearing,
      trackDeg: record.trackDeg, aboveFieldFt: record.onGround ? 0 : aboveField, verticalRateFpm: record.verticalRateFpm, observationAgeS: ageS, emergency: record.emergency, basis }));
  }
  rows.sort((left, right) => left.distanceNm - right.distanceNm || left.label.localeCompare(right.label));
  const kept = rows.slice(0, ACTIVITY_MAX_ROWS);
  const groups = { "descending-toward": [], "climbing-away": [], "on-surface": [], "other-low": [] } as Record<ActivityGroup, ActivityRow[]>;
  for (const row of kept) groups[row.group].push(row);
  return Object.freeze({ rows: Object.freeze(kept), groups: Object.freeze(groups), truncated: rows.length > kept.length });
}

const insideRing = (lon: number, lat: number, ring: readonly (readonly [number, number])[]): boolean => {
  let inside = false;
  for (let i = 0, j = ring.length - 1; i < ring.length; j = i++) {
    const [xi, yi] = ring[i], [xj, yj] = ring[j];
    if ((yi > lat) !== (yj > lat) && lon < (xj - xi) * (lat - yi) / (yj - yi) + xi) inside = !inside;
  }
  return inside;
};

/** How close a TFR boundary must come to the field reference point to count as touching it. */
export const TFR_TOUCH_RADIUS_NM = 3;

/**
 * TFR areas whose drawn boundary reaches the airport: the reference point or a
 * runway end lies inside, or a boundary vertex is within 3 NM of the point.
 * The FAA NOTAM decides whether the restriction applies; this only says the area is drawn there.
 */
export function tfrsTouchingAirport(airport: Pick<AviationAirport, "lon" | "lat" | "runways">, shapes: readonly TfrShape[]): readonly TfrShape[] {
  const points = [[airport.lon, airport.lat] as const, ...airport.runways.flatMap(runway => runway.ends.map(end => [end.lon, end.lat] as const))];
  return shapes.filter(shape => {
    const near = shape.bbox[0] - 0.1 <= airport.lon && airport.lon <= shape.bbox[2] + 0.1 && shape.bbox[1] - 0.1 <= airport.lat && airport.lat <= shape.bbox[3] + 0.1;
    if (!near) return false;
    if (points.some(([lon, lat]) => insideRing(lon, lat, shape.ring))) return true;
    return shape.ring.some(([lon, lat]) => distanceNm(lon, lat, airport.lon, airport.lat) <= TFR_TOUCH_RADIUS_NM);
  });
}

const SURFACES: Readonly<Record<string, string>> = Object.freeze({ ASPH: "asphalt", CONC: "concrete", TURF: "turf", GRVL: "gravel", DIRT: "dirt", WATER: "water", TRTD: "treated", GRAVEL: "gravel" });

/** NASR surface codes in words: "ASPH-CONC" → "asphalt/concrete"; unknown codes stay as coded. */
export const runwaySurfaceText = (surface: string | null): string => surface ? surface.split(/[-/]/).map(part => SURFACES[part.toUpperCase()] ?? part).join("/") : "surface not listed";

/** "01L/19R · 10,302 × 150 ft · concrete · HIGH lighting" from the NASR runway record. */
export const runwayLine = (runway: AviationRunway): string =>
  `${runway.id} · ${Math.round(runway.length_ft).toLocaleString("en-US")}${runway.width_ft ? ` × ${Math.round(runway.width_ft).toLocaleString("en-US")}` : ""} ft · ${runwaySurfaceText(runway.surface)}${runway.lighting ? ` · ${runway.lighting.toLowerCase()} lighting` : ""}`;

/** Tower description from the NASR tower code; a non-towered field uses its CTAF. */
export const towerText = (airport: Pick<AviationAirport, "tower" | "ctaf_mhz">): string =>
  airport.tower && airport.tower !== "NON-ATCT" ? `Towered (${airport.tower})` : `Non-towered${airport.ctaf_mhz ? `, CTAF ${airport.ctaf_mhz.toFixed(3)} MHz` : ", CTAF not listed"}`;
