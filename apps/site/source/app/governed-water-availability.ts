import type { WaterResponse } from "./governed-water";

export type WaterBrowserState = "not-checked" | "checking" | "received" | "no-release" | "withheld" | "unavailable";

/** Classify the response observed by this browser; never infer a release from a transport failure. */
export function waterBrowserStateForResponse(value: WaterResponse | null, httpOk: boolean): WaterBrowserState {
  if (!httpOk || !value?.envelope) return "unavailable";
  if (value.envelope.outcome === "ANSWER") {
    return Array.isArray(value.data?.stations) && Array.isArray(value.data?.observations) ? "received" : "withheld";
  }
  return value.envelope.reason_code === "NO_APPROVED_SNAPSHOT" ? "no-release" : "withheld";
}

export function waterBrowserLabel(state: WaterBrowserState): string {
  switch (state) {
    case "not-checked": return "Not checked";
    case "checking": return "Checking";
    case "received": return "Received";
    case "no-release": return "No reviewed release active";
    case "withheld": return "Withheld";
    case "unavailable": return "Unavailable";
  }
}

/** A station's evidence must be bound to the same released package and measurements. */
export function waterEvidenceMatchesSelection(layers: WaterResponse | null, evidence: WaterResponse, stationId: string): boolean {
  const a = layers?.data, b = evidence.data;
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
      || typeof dataset.ref !== "string" || !dataset.ref.startsWith(`kfm://water/station/${stationId}/`)
      || !Array.isArray(bundle.evidence_refs) || !Array.isArray(bundle.citations)
      || typeof bundle.citations[0] !== "string" || !bundle.citations[0].startsWith("https://")) return false;

  const measurements = a.observations.filter(observation => observation?.station_id === stationId);
  if (measurements.length > 127 || bundle.evidence_refs.length !== measurements.length + 1) return false;
  const refs = bundle.evidence_refs;
  return refs[0]?.kind === "dataset" && refs[0]?.ref === dataset.ref && refs[0]?.bundle_ref === bundle.bundle_id
    && measurements.every((observation, index) => typeof observation.evidence_ref === "string"
      && refs[index + 1]?.kind === "measurement" && refs[index + 1]?.ref === observation.evidence_ref
      && refs[index + 1]?.bundle_ref === bundle.bundle_id);
}

/** A fresh export must contain only the requested station, even if a route regresses. */
export function waterExportMatchesSelection(layers: WaterResponse, evidence: WaterResponse, stationId: string): boolean {
  const stations = layers.data?.stations, observations = layers.data?.observations;
  return Array.isArray(stations) && stations.length === 1 && stations[0]?.id === stationId
    && Array.isArray(observations) && observations.length <= 127
    && observations.every(observation => observation?.station_id === stationId)
    && waterEvidenceMatchesSelection(layers, evidence, stationId);
}
