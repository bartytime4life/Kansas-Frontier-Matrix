import type { Feature, FeatureCollection, Point } from "geojson";

export const NOAA_HYDROLOGY_NETWORK_API_PATH = "/api/hydrology/noaa?mode=network";

export type NoaaHydrologyState = "ready" | "empty" | "partial";

export type NoaaGaugeStatus = Readonly<{
  sourceRole: "OFFICIAL_NWS_OBSERVATION" | "OFFICIAL_NWS_FORECAST";
  validTime: string | null;
  primary: Readonly<{ value: number | null; unit: string | null }>;
  secondary: Readonly<{ value: number | null; unit: string | null }>;
  floodCategory: string | null;
}>;

export type NoaaGaugeRecord = Readonly<{
  lid: string;
  name: string | null;
  longitude: number;
  latitude: number;
  rfc: string | null;
  wfo: string | null;
  observed: NoaaGaugeStatus;
  forecast: NoaaGaugeStatus;
}>;

export type NoaaGaugeNetwork = Readonly<{
  state: NoaaHydrologyState;
  retrievedAt: string;
  records: readonly NoaaGaugeRecord[];
  partial: boolean;
  truncated: boolean;
  limitation: string;
  sourceUrl: string;
}>;

type JsonRecord = Record<string, unknown>;

const isRecord = (value: unknown): value is JsonRecord => Boolean(value) && typeof value === "object" && !Array.isArray(value);
const text = (value: unknown, maximum = 500) => typeof value === "string" && value.trim() && value.length <= maximum ? value.trim() : null;
const finite = (value: unknown) => typeof value === "number" && Number.isFinite(value) ? value : null;
const iso = (value: unknown) => {
  const candidate = text(value, 80);
  if (!candidate || !Number.isFinite(Date.parse(candidate))) return null;
  return new Date(candidate).toISOString();
};

const parseStatus = (value: unknown, sourceRole: NoaaGaugeStatus["sourceRole"]): NoaaGaugeStatus | null => {
  if (!isRecord(value) || value.sourceRole !== sourceRole || !isRecord(value.primary) || !isRecord(value.secondary)) return null;
  return Object.freeze({
    sourceRole,
    validTime: value.validTime === null ? null : iso(value.validTime),
    primary: Object.freeze({ value: value.primary.value === null ? null : finite(value.primary.value), unit: value.primary.unit === null ? null : text(value.primary.unit, 40) }),
    secondary: Object.freeze({ value: value.secondary.value === null ? null : finite(value.secondary.value), unit: value.secondary.unit === null ? null : text(value.secondary.unit, 40) }),
    floodCategory: value.floodCategory === null ? null : text(value.floodCategory, 80),
  });
};

export const parseNoaaGaugeNetwork = (value: unknown): NoaaGaugeNetwork => {
  if (!isRecord(value)
    || value.mode !== "network"
    || !["ready", "empty", "partial"].includes(String(value.state))
    || !iso(value.retrievedAt)
    || !Array.isArray(value.records)
    || value.records.length > 400
    || typeof value.partial !== "boolean"
    || typeof value.truncated !== "boolean"
    || !text(value.limitation, 4_000)
    || !Array.isArray(value.sourceLinks)) throw new Error("The NOAA hydrology adapter returned an invalid network contract.");

  const records: NoaaGaugeRecord[] = [];
  const seen = new Set<string>();
  for (const candidate of value.records) {
    if (!isRecord(candidate)
      || candidate.kind !== "gauge"
      || candidate.sourceRole !== "OFFICIAL_NWS_GAUGE_STATUS"
      || !isRecord(candidate.location)
      || !isRecord(candidate.rfc)
      || !isRecord(candidate.wfo)) throw new Error("The NOAA hydrology network contained a malformed gauge.");
    const lid = text(candidate.lid, 8);
    const latitude = finite(candidate.location.latitude);
    const longitude = finite(candidate.location.longitude);
    const observed = parseStatus(candidate.observed, "OFFICIAL_NWS_OBSERVATION");
    const forecast = parseStatus(candidate.forecast, "OFFICIAL_NWS_FORECAST");
    if (!lid || !/^[A-Z0-9]{3,8}$/.test(lid) || seen.has(lid)
      || latitude === null || longitude === null
      || latitude < 36.993 || latitude > 40.003 || longitude < -102.0517 || longitude > -94.588
      || !observed || !forecast) throw new Error("The NOAA hydrology network contained an invalid Kansas gauge.");
    seen.add(lid);
    records.push(Object.freeze({
      lid,
      name: candidate.name === null ? null : text(candidate.name, 300),
      longitude,
      latitude,
      rfc: text(candidate.rfc.abbreviation, 16),
      wfo: text(candidate.wfo.abbreviation, 16),
      observed,
      forecast,
    }));
  }

  const sourceLink = value.sourceLinks.find((candidate) => isRecord(candidate) && candidate.rel === "upstream" && text(candidate.href, 2_000));
  const sourceUrl = sourceLink && isRecord(sourceLink) ? text(sourceLink.href, 2_000) : null;
  if (!sourceUrl || !sourceUrl.startsWith("https://api.water.noaa.gov/nwps/v1/gauges")) throw new Error("The NOAA hydrology network omitted its fixed source link.");
  return Object.freeze({
    state: value.state as NoaaHydrologyState,
    retrievedAt: iso(value.retrievedAt)!,
    records: Object.freeze(records.sort((left, right) => left.lid.localeCompare(right.lid))),
    partial: value.partial,
    truncated: value.truncated,
    limitation: text(value.limitation, 4_000)!,
    sourceUrl,
  });
};

export type NoaaGaugeFeatureProperties = Readonly<{
  featureId: string;
  name: string;
  lid: string;
  observedAt: string | null;
  observedValue: number | null;
  observedUnit: string | null;
  forecastAt: string | null;
  forecastValue: number | null;
  forecastUnit: string | null;
  floodCategory: string | null;
  hasForecast: boolean;
  displayValue: string;
  retrievedAt: string;
  sourceOrganization: "NOAA National Water Prediction Service";
  evidenceRole: "EXTERNAL_CONTEXT_ONLY";
}>;

const displayMeasurement = (value: number | null, unit: string | null) => value === null
  ? "not reported"
  : `${value.toLocaleString("en-US", { maximumFractionDigits: value >= 100 ? 0 : 2 })}${unit ? ` ${unit}` : ""}`;

export const noaaGaugeNetworkGeoJson = (network: NoaaGaugeNetwork): FeatureCollection<Point, NoaaGaugeFeatureProperties> => ({
  type: "FeatureCollection",
  features: network.records.map((gauge): Feature<Point, NoaaGaugeFeatureProperties> => ({
    type: "Feature",
    id: gauge.lid,
    geometry: { type: "Point", coordinates: [gauge.longitude, gauge.latitude] },
    properties: {
      featureId: `noaa-nwps-gauge-${gauge.lid}`,
      name: gauge.name ?? `NWPS gauge ${gauge.lid}`,
      lid: gauge.lid,
      observedAt: gauge.observed.validTime,
      observedValue: gauge.observed.primary.value,
      observedUnit: gauge.observed.primary.unit,
      forecastAt: gauge.forecast.validTime,
      forecastValue: gauge.forecast.primary.value,
      forecastUnit: gauge.forecast.primary.unit,
      floodCategory: gauge.observed.floodCategory ?? gauge.forecast.floodCategory,
      hasForecast: gauge.forecast.validTime !== null && gauge.forecast.primary.value !== null,
      displayValue: displayMeasurement(gauge.observed.primary.value, gauge.observed.primary.unit),
      retrievedAt: network.retrievedAt,
      sourceOrganization: "NOAA National Water Prediction Service",
      evidenceRole: "EXTERNAL_CONTEXT_ONLY",
    },
  })),
});
