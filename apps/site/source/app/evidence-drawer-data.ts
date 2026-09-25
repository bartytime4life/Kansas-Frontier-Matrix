import type { OfficialContextId } from "./live-context";

export type DrawerAttribute = Readonly<{ label: string; value: string }>;

const FIELDS: Readonly<Record<OfficialContextId | "registry" | "basemap", readonly (readonly [string, string])[]>> = {
  "census-counties": [["geoid", "County GEOID"], ["name", "County"], ["vintage", "Census edition"], ["population", "Population count"], ["housingUnits", "Housing units"], ["landSquareMiles", "Land · sq mi"], ["waterSquareMiles", "Water · sq mi"]],
  "usgs-streamflow": [["stationId", "USGS station"], ["displayValue", "Discharge at frame"], ["observedAt", "Observed at"], ["approvalStatus", "USGS status"], ["trend", "Trend at frame"]],
  "noaa-nwps-gauges": [["lid", "NOAA gauge"], ["observedValue", "Observed value"], ["observedUnit", "Observed unit"], ["observedAt", "Observed at"], ["forecastValue", "Forecast value"], ["forecastUnit", "Forecast unit"], ["forecastAt", "Forecast valid at"], ["floodCategory", "Provider flood category"]],
  "usgs-earthquakes": [["magnitude", "Magnitude"], ["magnitudeType", "Magnitude type"], ["depthKilometers", "Depth · km"], ["observedAt", "Event time"], ["updatedAt", "Provider update"], ["reviewStatus", "Review status"], ["eventType", "Event type"], ["place", "Place"]],
  "noaa-hms-smoke": [["density", "Smoke density category"], ["start", "Valid from"], ["end", "Valid through"], ["satellite", "Satellite"], ["artifact", "Provider artifact"]],
  "nasa-gibs-fire-points": [["acquiredAt", "Acquired · UTC"], ["sourceDay", "NASA image day · UTC"], ["latitude", "Latitude · degrees"], ["longitude", "Longitude · degrees"], ["frpMw", "Fire radiative power · MW"], ["confidence", "Detection confidence"], ["hotSpotType", "Inferred hot-spot type"], ["brightnessI4Kelvin", "Brightness I-4 · K"], ["brightnessI5Kelvin", "Brightness I-5 · K"], ["scanKm", "Along-scan pixel · km"], ["trackKm", "Along-track pixel · km"], ["dayNight", "Day or night"], ["satellite", "Satellite"], ["instrument", "Instrument"], ["processingVersion", "Processing version"], ["providerUid", "Provider UID"], ["retrievedAt", "Retrieved · UTC"]],
  "nifc-fire-reports": [["incidentType", "Reported incident type"], ["reportState", "Report state"], ["discoveryAt", "Discovered · UTC"], ["modifiedAt", "Last modified · UTC"], ["reportedOutAt", "Reported out · UTC"], ["county", "County"], ["reportedAcres", "Reported area · acres"], ["percentContained", "Reported containment · %"], ["reportedCause", "Reported cause"], ["jurisdiction", "Jurisdiction"], ["protectingAgency", "Protecting agency"], ["uniqueFireIdentifier", "Interagency fire ID"], ["irwinId", "IRWIN record ID"], ["latitude", "Reported latitude"], ["longitude", "Reported longitude"], ["retrievedAt", "Retrieved · UTC"]],
  "raspberry-shake-stations": [["network", "Network"], ["station", "Station"], ["elevationMeters", "Elevation · m"], ["startTime", "Station start"], ["endTime", "Station end"], ["dataRole", "Data role"], ["waveformAvailability", "Waveform availability"]],
  "nws-alerts": [["event", "Event"], ["severity", "Severity"], ["urgency", "Urgency"], ["certainty", "Certainty"], ["headline", "Headline"], ["zoneName", "Zone"], ["effective", "Effective"], ["expires", "Expires"], ["senderName", "Issuer"]],
  "usgs-3dhp-hydrography": [], "usgs-wbd-watersheds": [], "noaa-nwm-analysis": [], "noaa-nwm-short-range": [], "nasa-firms-active-fire": [], "noaa-goes-geocolor": [], "usgs-3dep-hillshade": [], "usgs-3dep-slope": [], "nws-radar": [], "nws-forecast-wind": [],
  registry: [["displayElevationFt", "Display elevation · ft"], ["relativeHeightM", "Relative height · m"], ["smokeDensity", "Smoke density"], ["watershedClass", "Watershed class"], ["settlementClass", "Settlement class"], ["transportMode", "Transport mode"], ["habitatClass", "Habitat class"], ["faunaClass", "Fauna class"], ["floraClass", "Flora class"], ["fireClass", "Fire class"], ["hazardClass", "Hazard class"], ["consentPosture", "Consent posture"], ["tileLabel", "Tile label"], ["displayLabel", "Display label"]],
  basemap: [["name", "Name"], ["name:en", "English name"], ["class", "Map class"], ["type", "Map type"], ["ref", "Reference"]],
};

/** Only already public, explicitly selected properties can become drawer data. */
export const drawerArtifactAttributes = (source: OfficialContextId | "registry" | "basemap", properties: unknown): readonly DrawerAttribute[] => {
  if (!properties || typeof properties !== "object" || Array.isArray(properties)) return [];
  const record = properties as Record<string, unknown>;
  return FIELDS[source].flatMap(([key, label]) => {
    const raw = record[key];
    const value = typeof raw === "number" && Number.isFinite(raw) ? raw.toLocaleString("en-US", { maximumFractionDigits: 3 })
      : typeof raw === "string" ? raw.trim().slice(0, 240) : "";
    return value !== "" ? [{ label, value }] : [];
  });
};

type StageSample = Readonly<{ observedAt: string; value: number | null; unit: string; approvalStatus: string | null; qualifiers: readonly string[] }>;
export type UsgsStageDetail = Readonly<{
  stationId: string; name: string; county: string | null; huc: string | null;
  drainageArea: number | null; contributingDrainageArea: number | null;
  siteTypeCode: string | null; latitude: number; longitude: number;
  queryStart: string; queryEnd: string; retrievedAt: string;
  partial: boolean; truncated: boolean; observationCount: number;
  latest: StageSample | null; recent: readonly StageSample[];
}>;

const object = (value: unknown): value is Record<string, unknown> => Boolean(value) && typeof value === "object" && !Array.isArray(value);
const optionalText = (value: unknown, maximum = 240) => typeof value === "string" && value.length <= maximum ? value : null;
const optionalNumber = (value: unknown) => typeof value === "number" && Number.isFinite(value) ? value : null;
const iso = (value: unknown): value is string => typeof value === "string" && /^\d{4}-\d{2}-\d{2}T/.test(value) && Number.isFinite(Date.parse(value));

/** Parse only the fixed station/00065 contract returned by the existing Site adapter. */
export const parseUsgsStageDetail = (payload: unknown, expectedStationId: string): UsgsStageDetail => {
  if (!/^USGS-\d{8,15}$/.test(expectedStationId) || !object(payload)
    || payload.kind !== "usgs-streamflow-bundle" || payload.mode !== "station" || payload.parameterCode !== "00065"
    || !iso(payload.queryStart) || !iso(payload.queryEnd) || !iso(payload.retrievedAt)
    || !Array.isArray(payload.stations) || payload.stations.length !== 1
    || !Array.isArray(payload.observations) || payload.observations.length > 20_000
    || typeof payload.partial !== "boolean" || typeof payload.truncated !== "boolean") {
    throw new Error("The USGS gauge-height response was invalid.");
  }
  const station = payload.stations[0];
  if (!object(station) || station.stationId !== expectedStationId || station.agencyCode !== "USGS"
    || !optionalText(station.name) || optionalNumber(station.latitude) === null || optionalNumber(station.longitude) === null) {
    throw new Error("The USGS station metadata did not match the selected gauge.");
  }
  const samples: StageSample[] = payload.observations.map((item: unknown) => {
    if (!object(item) || item.stationId !== expectedStationId || item.parameterCode !== "00065"
      || !iso(item.observedAt) || optionalText(item.unit, 64) === null
      || item.value !== null && optionalNumber(item.value) === null
      || item.approvalStatus !== null && optionalText(item.approvalStatus, 80) === null
      || !Array.isArray(item.qualifiers) || item.qualifiers.length > 16
      || !item.qualifiers.every((qualifier: unknown) => optionalText(qualifier, 80) !== null)) {
      throw new Error("The USGS gauge-height observations were invalid.");
    }
    return { observedAt: item.observedAt as string, value: item.value as number | null, unit: item.unit as string,
      approvalStatus: item.approvalStatus as string | null, qualifiers: item.qualifiers as string[] };
  }).sort((left, right) => Date.parse(right.observedAt) - Date.parse(left.observedAt));
  return {
    stationId: expectedStationId, name: station.name as string,
    county: optionalText(station.county), huc: optionalText(station.huc, 40),
    drainageArea: optionalNumber(station.drainageArea), contributingDrainageArea: optionalNumber(station.contributingDrainageArea),
    siteTypeCode: optionalText(station.siteTypeCode, 40), latitude: station.latitude as number, longitude: station.longitude as number,
    queryStart: payload.queryStart, queryEnd: payload.queryEnd, retrievedAt: payload.retrievedAt,
    partial: payload.partial, truncated: payload.truncated, observationCount: samples.length,
    latest: samples.find((sample) => sample.value !== null) ?? null, recent: samples.slice(0, 8),
  };
};
