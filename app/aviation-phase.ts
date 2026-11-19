/**
 * Observed flight phase, derived only from one ADS-B record and the pinned
 * NASR facility list: the reported surface flag, the reported vertical rate,
 * the reported height above the nearest public-use facility and the distance
 * to it. It is a description of the observation, never a statement of intent:
 * "descending" does not mean "landing" and "low near KICT" does not mean
 * "arriving at KICT". Every result names what it was derived from.
 *
 * No runtime imports: tests load this file as a standalone module.
 */
import type { Aircraft } from "./aviation-traffic";

export type PhaseFacility = Readonly<{ faa_id: string; icao_id: string | null; lon: number; lat: number; elevation_ft: number }>;
export type PhaseTrend = "climbing" | "level" | "descending";
export type PhaseKind = "on-surface" | PhaseTrend | "low-near" | "unknown";
export type ObservedPhase = Readonly<{
  kind: PhaseKind;
  /** Short label for instruments and map text, e.g. "low near KICT, descending". */
  label: string;
  /** What the label was derived from, in words, for the panel. */
  basis: string;
  trend: PhaseTrend | null;
  facility: string | null;
  distanceNm: number | null;
  aboveFieldFt: number | null;
}>;

/** Within 10 NM and 3,000 ft above a public-use field counts as "low near" it. */
export const PHASE_LOW_RADIUS_NM = 10;
export const PHASE_LOW_HEIGHT_FT = 3000;
/** readsb reports vertical rate in 64 ft/min steps; smaller magnitudes read as level. */
export const PHASE_LEVEL_RATE_FPM = 300;
export const PHASE_DERIVATION = "Derived from the reported surface flag, vertical rate and height above the nearest public-use facility; not a flight plan, clearance or intent.";
const KM_PER_NM = 1.852;

export function distanceNm(lon1: number, lat1: number, lon2: number, lat2: number): number {
  const toRad = Math.PI / 180, p1 = lat1 * toRad, p2 = lat2 * toRad;
  const a = Math.sin((p2 - p1) / 2) ** 2 + Math.cos(p1) * Math.cos(p2) * Math.sin((lon2 - lon1) * toRad / 2) ** 2;
  return 6371.0088 * 2 * Math.asin(Math.min(1, Math.sqrt(a))) / KM_PER_NM;
}

export function nearestFacility<T extends PhaseFacility>(facilities: readonly T[], lon: number, lat: number): Readonly<{ facility: T; nm: number }> | null {
  let best: { facility: T; nm: number } | null = null;
  for (const facility of facilities) {
    const nm = distanceNm(lon, lat, facility.lon, facility.lat);
    if (!best || nm < best.nm) best = { facility, nm };
  }
  return best ? Object.freeze(best) : null;
}

export const facilityCode = (facility: Pick<PhaseFacility, "faa_id" | "icao_id">): string => facility.icao_id ?? facility.faa_id;

/** Reported height for comparison with a field elevation: geometric (WGS84) if present, else pressure altitude. Approximate, not MSL. */
export const reportedHeightFt = (aircraft: Pick<Aircraft, "onGround" | "altBaroFt" | "altGeomFt">): number | null =>
  aircraft.onGround ? null : aircraft.altGeomFt ?? aircraft.altBaroFt;

export function verticalTrend(verticalRateFpm: number | null): PhaseTrend | null {
  if (verticalRateFpm === null || !Number.isFinite(verticalRateFpm)) return null;
  if (verticalRateFpm >= PHASE_LEVEL_RATE_FPM) return "climbing";
  if (verticalRateFpm <= -PHASE_LEVEL_RATE_FPM) return "descending";
  return "level";
}

const fpm = (value: number) => `${value > 0 ? "+" : ""}${Math.round(value).toLocaleString("en-US")} ft/min`;
const feet = (value: number) => `${Math.round(value).toLocaleString("en-US")} ft`;

/**
 * The observed phase of one aircraft. `facilities` should be the public-use,
 * non-heliport facilities (a heliport's published elevation can be a rooftop).
 */
export function observedPhase(aircraft: Pick<Aircraft, "onGround" | "verticalRateFpm" | "altBaroFt" | "altGeomFt" | "lon" | "lat">, facilities: readonly PhaseFacility[]): ObservedPhase {
  const near = nearestFacility(facilities, aircraft.lon, aircraft.lat);
  const facility = near ? facilityCode(near.facility) : null;
  const distance = near ? Math.round(near.nm * 10) / 10 : null;
  if (aircraft.onGround) {
    return Object.freeze({ kind: "on-surface" as const, label: "on surface", trend: null, facility, distanceNm: distance, aboveFieldFt: null,
      basis: `Reported surface flag (alt_baro "ground")${near ? `; nearest public-use facility ${facility}, ${distance} NM` : ""}.` });
  }
  const height = reportedHeightFt(aircraft);
  const trend = verticalTrend(aircraft.verticalRateFpm);
  const datum = aircraft.altGeomFt !== null ? "WGS84 geometric height" : "pressure altitude";
  const rateText = aircraft.verticalRateFpm === null ? "vertical rate not reported" : `vertical rate ${fpm(aircraft.verticalRateFpm)} reported`;
  const aboveField = near && height !== null ? Math.round(height - near.facility.elevation_ft) : null;
  if (near && aboveField !== null && near.nm <= PHASE_LOW_RADIUS_NM && aboveField <= PHASE_LOW_HEIGHT_FT) {
    return Object.freeze({ kind: "low-near" as const, label: `low near ${facility}${trend ? `, ${trend}` : ""}`, trend, facility, distanceNm: distance, aboveFieldFt: aboveField,
      basis: `${feet(aboveField)} above ${facility} field elevation (${datum} minus ${feet(near.facility.elevation_ft)}), ${distance} NM away; ${rateText}. Within ${PHASE_LOW_RADIUS_NM} NM and ${PHASE_LOW_HEIGHT_FT.toLocaleString("en-US")} ft. Not an arrival or departure statement.` });
  }
  if (!trend) {
    return Object.freeze({ kind: "unknown" as const, label: "phase not derivable", trend: null, facility, distanceNm: distance, aboveFieldFt: aboveField,
      basis: `${rateText}${height === null ? "; no altitude reported" : ""}. Airborne per the feed; no climb, level or descent label can be derived.` });
  }
  return Object.freeze({ kind: trend, label: trend, trend, facility, distanceNm: distance, aboveFieldFt: aboveField,
    basis: `${rateText} (level means within ±${PHASE_LEVEL_RATE_FPM} ft/min)${aboveField !== null ? `; ${feet(aboveField)} above ${facility}, ${distance} NM away` : height === null ? "; no altitude reported" : ""}.` });
}
