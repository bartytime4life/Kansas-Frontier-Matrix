import type { WeatherObservation, WeatherResponse } from "./governed-weather";

/** 30 station-local days × PRCP/TMAX/TMIN: the most rows one station can carry. */
export const WEATHER_STATION_ROWS = 90;
const ELEMENTS = ["PRCP", "TMAX", "TMIN"] as const;

/** A station's evidence must be bound to the same released package and observations. */
export function weatherEvidenceMatchesSelection(layers: WeatherResponse | null, evidence: WeatherResponse, stationId: string): boolean {
  const a = layers?.data, b = evidence?.data;
  if (layers?.envelope?.outcome !== "ANSWER" || evidence?.envelope?.outcome !== "ANSWER" || !a || !b
      || typeof a.package_id !== "string" || !a.package_id || a.package_id !== b.package_id
      || a.released_at !== b.released_at || a.reviewed_at !== b.reviewed_at
      || a.approval_expires_at !== b.approval_expires_at
      || a.correction_state !== "ACTIVE" || b.correction_state !== "ACTIVE"
      || !Array.isArray(a.stations) || !a.stations.some(station => station?.id === stationId)
      || !Array.isArray(a.observations) || !Array.isArray(b.entries) || b.entries.length !== 1) return false;

  const entry = b.entries[0], bundle = entry?.bundle, dataset = entry?.evidence_ref;
  if (entry?.station_id !== stationId || !bundle || !dataset
      || dataset.kind !== "dataset" || dataset.bundle_ref !== bundle.bundle_id
      || typeof dataset.ref !== "string" || !dataset.ref.startsWith(`kfm://weather/station/${stationId}/`)
      || !Array.isArray(bundle.evidence_refs) || !Array.isArray(bundle.citations)
      || typeof bundle.citations[0] !== "string" || !bundle.citations[0].startsWith("https://www.ncei.noaa.gov/")) return false;

  const rows = a.observations.filter(observation => observation?.station_id === stationId);
  if (rows.length > WEATHER_STATION_ROWS || bundle.evidence_refs.length !== rows.length + 1) return false;
  const refs = bundle.evidence_refs;
  return refs[0]?.kind === "dataset" && refs[0]?.ref === dataset.ref && refs[0]?.bundle_ref === bundle.bundle_id
    && rows.every((row, index) => typeof row.evidence_ref === "string"
      && refs[index + 1]?.kind === "measurement" && refs[index + 1]?.ref === row.evidence_ref
      && refs[index + 1]?.bundle_ref === bundle.bundle_id);
}

/** A fresh export must contain only the requested station, even if a route regresses. */
export function weatherExportMatchesSelection(layers: WeatherResponse, evidence: WeatherResponse, stationId: string): boolean {
  const stations = layers?.data?.stations, rows = layers?.data?.observations;
  return Array.isArray(stations) && stations.length === 1 && stations[0]?.id === stationId
    && Array.isArray(rows) && rows.length <= WEATHER_STATION_ROWS
    && rows.every(row => row?.station_id === stationId)
    && weatherEvidenceMatchesSelection(layers, evidence, stationId);
}

export type WeatherDay = { date: string; values: Record<string, WeatherObservation | undefined>; withheld: number };

/** The station's latest observation day, with each element's row (withheld rows stay null-valued). */
export function latestWeatherDay(rows: WeatherObservation[] | undefined, stationId: string): WeatherDay | null {
  const own = (rows ?? []).filter(row => row?.station_id === stationId);
  const date = own.map(row => row.observation_date).sort().at(-1);
  if (!date) return null;
  const day = own.filter(row => row.observation_date === date);
  return { date, withheld: day.filter(row => row.withheld).length,
    values: Object.fromEntries(ELEMENTS.map(element => [element, day.find(row => row.element === element)])) };
}

/** Text for one element; a withheld or missing value is never shown as zero. */
export function weatherValueText(row: WeatherObservation | undefined): string {
  if (!row) return "Not reported";
  if (row.withheld || row.value === null) return row.withheld === "QUALITY_FLAG" ? "Withheld (failed provider quality check)" : "Withheld (missing)";
  if (row.trace) return "Trace";
  return `${row.value} ${row.unit === "degC" ? "°C" : row.unit}`;
}
