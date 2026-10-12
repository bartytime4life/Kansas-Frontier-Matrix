import type { SoilObservation, SoilResponse } from "./governed-soil";

export const SOIL_DEPTHS = [5, 10, 20, 50, 100] as const;
/** 30 local-standard-time days × moisture and temperature at five depths: the most rows one station can carry. */
export const SOIL_STATION_ROWS = 300;

/** A station's evidence must be its five depth bundles, bound to the same released package and observations. */
export function soilEvidenceMatchesSelection(layers: SoilResponse | null, evidence: SoilResponse, stationId: string): boolean {
  const a = layers?.data, b = evidence?.data;
  if (layers?.envelope?.outcome !== "ANSWER" || evidence?.envelope?.outcome !== "ANSWER" || !a || !b
      || typeof a.package_id !== "string" || !a.package_id || a.package_id !== b.package_id
      || a.released_at !== b.released_at || a.reviewed_at !== b.reviewed_at
      || a.approval_expires_at !== b.approval_expires_at
      || a.correction_state !== "ACTIVE" || b.correction_state !== "ACTIVE"
      || !Array.isArray(a.stations) || !a.stations.some(station => station?.id === stationId)
      || !Array.isArray(a.observations) || !Array.isArray(b.entries) || b.entries.length !== SOIL_DEPTHS.length) return false;
  const rows = a.observations.filter(observation => observation?.station_id === stationId);
  if (rows.length > SOIL_STATION_ROWS) return false;
  return SOIL_DEPTHS.every((depth, index) => {
    const entry = b.entries![index], bundle = entry?.bundle, dataset = entry?.evidence_ref;
    if (entry?.station_id !== stationId || entry.series !== depth || !bundle || !dataset
        || dataset.kind !== "dataset" || dataset.bundle_ref !== bundle.bundle_id
        || typeof dataset.ref !== "string" || !dataset.ref.startsWith(`kfm://soil/station/${stationId}/depth-${depth}cm/`)
        || !Array.isArray(bundle.evidence_refs) || !Array.isArray(bundle.citations)
        || typeof bundle.citations[0] !== "string" || !bundle.citations[0].startsWith("https://www.ncei.noaa.gov/")) return false;
    const own = rows.filter(row => row.depth_cm === depth), refs = bundle.evidence_refs;
    return refs.length === own.length + 1 && refs[0]?.kind === "dataset" && refs[0]?.ref === dataset.ref && refs[0]?.bundle_ref === bundle.bundle_id
      && own.every((row, i) => typeof row.evidence_ref === "string"
        && refs[i + 1]?.kind === "measurement" && refs[i + 1]?.ref === row.evidence_ref && refs[i + 1]?.bundle_ref === bundle.bundle_id);
  });
}

/** A fresh export must contain only the requested station, even if a route regresses. */
export function soilExportMatchesSelection(layers: SoilResponse, evidence: SoilResponse, stationId: string): boolean {
  const stations = layers?.data?.stations, rows = layers?.data?.observations;
  return Array.isArray(stations) && stations.length === 1 && stations[0]?.id === stationId
    && Array.isArray(rows) && rows.length <= SOIL_STATION_ROWS
    && rows.every(row => row?.station_id === stationId)
    && soilEvidenceMatchesSelection(layers, evidence, stationId);
}

export type SoilDay = { date: string; withheld: number; moisture: Record<number, SoilObservation | undefined>; temperature: Record<number, SoilObservation | undefined> };

/** The station's latest day, with moisture and temperature at each depth (withheld rows stay null-valued). */
export function latestSoilDay(rows: SoilObservation[] | undefined, stationId: string): SoilDay | null {
  const own = (rows ?? []).filter(row => row?.station_id === stationId);
  const date = own.map(row => row.observation_date).sort().at(-1);
  if (!date) return null;
  const day = own.filter(row => row.observation_date === date);
  const at = (variable: string) => Object.fromEntries(SOIL_DEPTHS.map(depth => [depth, day.find(row => row.variable === variable && row.depth_cm === depth)]));
  return { date, withheld: day.filter(row => row.withheld).length, moisture: at("SOIL_MOISTURE"), temperature: at("SOIL_TEMP") };
}

/** Text for one value; a withheld or missing value is never shown as zero. */
export function soilValueText(row: SoilObservation | undefined): string {
  if (!row) return "Not reported";
  if (row.withheld || row.value === null) return row.withheld === "OUT_OF_RANGE" ? "Withheld (outside the physical range)" : "Withheld (missing)";
  return row.unit === "degC" ? `${row.value.toFixed(1)} °C` : `${row.value.toFixed(3)} m³/m³`;
}
