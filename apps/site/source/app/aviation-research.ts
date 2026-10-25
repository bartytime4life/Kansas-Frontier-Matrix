/**
 * Aviation points for the "Near here" research dossier, so any selected
 * feature lists the nearby public-use airports and weather stations. Only
 * supplied point geometry joins (the dossier's rule): airspace volumes and TFR
 * polygons stay out, as do private-use strips (so they cannot crowd the
 * 50-record dossier near towns) and live aircraft (transient positions).
 * Standalone on purpose (no runtime imports), like the other aviation model modules.
 */
import type { ResearchRecord } from "./research-context";

export const AVIATION_RESEARCH_SOURCE = Object.freeze({
  airports: "faa-nasr-public-use-airports",
  metar: "noaa-awc-metar",
});
const NASR_URL = "https://www.faa.gov/air_traffic/flight_info/aeronav/aero_data/NASR_Subscription/";
const AWC_URL = "https://aviationweather.gov/data/api/";

type Airport = Readonly<{ faa_id: string; icao_id: string | null; name: string; lon: number; lat: number; elevation_ft: number; facility_type: string; use: string; tower: string | null }>;
type Metar = Readonly<{ station: string; name: string | null; lon: number; lat: number; observedAt: string; flightCategory: string | null }>;
export type AviationResearchInput = Readonly<{
  airports: readonly Airport[]; nasrCycle: string; validFrom: string; validToExclusive: string;
  metars: readonly Metar[]; metarRetrievedAt: string | null;
}>;

const feet = (value: number) => `${Math.round(value).toLocaleString("en-US")} ft`;

export function aviationResearchPoints(input: AviationResearchInput): readonly ResearchRecord[] {
  const airports = input.airports.filter(airport => airport.use === "PUBLIC").map((airport): ResearchRecord => ({
    kind: "provider", sourceId: AVIATION_RESEARCH_SOURCE.airports, featureId: `airport:${airport.faa_id}`,
    title: `${airport.name} (${airport.icao_id ?? airport.faa_id}) · public-use ${airport.facility_type.toLowerCase().replace(/_/g, " ")}${airport.tower && airport.tower !== "NON-ATCT" ? ", towered" : ""} · ${feet(airport.elevation_ft)}`,
    coordinates: [airport.lon, airport.lat], sourceTitle: `FAA NASR airports, cycle ${input.nasrCycle}`, sourceUrl: NASR_URL,
    sourceTime: `NASR cycle ${input.nasrCycle}, valid ${input.validFrom} to ${input.validToExclusive} (exclusive)`, retrievedAt: null,
    evidenceLabel: "EXTERNAL_CONTEXT_ONLY",
    limitation: "Airport reference point and field elevation from the FAA NASR subscription; display context, not navigation. Private-use facilities are on the aviation layer but not in this dossier.",
  }));
  const metars = input.metars.map((metar): ResearchRecord => ({
    kind: "provider", sourceId: AVIATION_RESEARCH_SOURCE.metar, featureId: `metar:${metar.station}`,
    title: `${metar.station}${metar.name ? ` ${metar.name}` : ""} weather station · ${metar.flightCategory ?? "category unavailable"}`,
    coordinates: [metar.lon, metar.lat], sourceTitle: "NOAA/NWS Aviation Weather Center METAR", sourceUrl: AWC_URL,
    sourceTime: `Observed ${metar.observedAt}`, retrievedAt: input.metarRetrievedAt,
    evidenceLabel: "EXTERNAL_CONTEXT_ONLY",
    limitation: "Latest ASOS/AWOS observation at the station site, within 90 minutes; describes the station only and is not a forecast or briefing.",
  }));
  return Object.freeze([...airports, ...metars]);
}
