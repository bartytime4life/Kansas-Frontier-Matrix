import type { Earthquake, EarthquakeResponse } from "./governed-earthquakes";
import type { WaterBrowserState } from "./governed-water-availability";

/** The most records one month can carry: a package holds at most 6000 events (release.core EARTHQUAKES). */
export const EARTHQUAKE_MONTH_ROWS = 6000;
export const EARTHQUAKE_MONTH_NAMES = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"] as const;
const monthOf = (row: Earthquake | undefined) => Number(row?.origin_utc?.slice(5, 7));

/** Classify an earthquake response; never infer a release from a transport failure. Bootstrap lists months,
 *  layers carry observations: earthquakes have no stations, so the water classifier does not apply. */
export function earthquakeBrowserStateForResponse(value: EarthquakeResponse | null, httpOk: boolean): WaterBrowserState {
  if (!httpOk || !value?.envelope) return "unavailable";
  if (value.envelope.outcome === "ANSWER") return Array.isArray(value.data?.observations) || Array.isArray(value.data?.months) ? "received" : "withheld";
  return value.envelope.reason_code === "NO_APPROVED_SNAPSHOT" ? "no-release" : "withheld";
}

/** A month's evidence must be every part of that month, in order, bound to the same released package and records. */
export function earthquakeEvidenceMatchesSelection(layers: EarthquakeResponse | null, evidence: EarthquakeResponse, month: number): boolean {
  const a = layers?.data, b = evidence?.data;
  if (layers?.envelope?.outcome !== "ANSWER" || evidence?.envelope?.outcome !== "ANSWER" || !a || !b
      || typeof a.package_id !== "string" || !a.package_id || a.package_id !== b.package_id
      || a.released_at !== b.released_at || a.reviewed_at !== b.reviewed_at
      || a.approval_expires_at !== b.approval_expires_at
      || a.correction_state !== "ACTIVE" || b.correction_state !== "ACTIVE"
      || !Array.isArray(a.observations) || !Array.isArray(b.entries) || !b.entries.length) return false;
  const rows = a.observations.filter(row => monthOf(row) === month);
  if (rows.length > EARTHQUAKE_MONTH_ROWS) return false;
  let next = 0;
  const bound = b.entries.every((entry, index) => {
    const bundle = entry?.bundle, dataset = entry?.evidence_ref;
    if (entry?.month !== month || entry.part !== index + 1 || !bundle || !dataset
        || dataset.kind !== "dataset" || dataset.bundle_ref !== bundle.bundle_id
        || typeof dataset.ref !== "string" || !dataset.ref.startsWith(`kfm://hazards/earthquakes/${String(a.data_year)}-${String(month).padStart(2, "0")}/part-${index + 1}/`)
        || !Array.isArray(bundle.evidence_refs) || bundle.evidence_refs.length < 2 || !Array.isArray(bundle.citations)
        || typeof bundle.citations[0] !== "string" || !bundle.citations[0].startsWith("https://earthquake.usgs.gov/")) return false;
    const refs = bundle.evidence_refs;
    if (refs[0]?.kind !== "dataset" || refs[0]?.ref !== dataset.ref || refs[0]?.bundle_ref !== bundle.bundle_id) return false;
    return refs.slice(1).every(ref => {
      const row = rows[next++];
      return typeof row?.evidence_ref === "string" && ref?.kind === "record" && ref.ref === row.evidence_ref && ref.bundle_ref === bundle.bundle_id;
    });
  });
  return bound && next === rows.length;
}

/** A fresh export must contain only the requested month, even if a route regresses. */
export function earthquakeExportMatchesSelection(layers: EarthquakeResponse, evidence: EarthquakeResponse, month: number): boolean {
  const rows = layers?.data?.observations, selection = layers?.data?.selection;
  return Array.isArray(rows) && rows.length <= EARTHQUAKE_MONTH_ROWS && rows.every(row => monthOf(row) === month)
    && Array.isArray(selection?.months) && selection.months.length === 1 && selection.months[0] === month && selection.observation_count === rows.length
    && earthquakeEvidenceMatchesSelection(layers, evidence, month);
}

/** Magnitude with its type; a missing magnitude is not reported, never zero. Types are not interchangeable. */
export function earthquakeMagnitudeText(magnitude: number | null | undefined, type: string | null | undefined): string {
  if (magnitude === null || magnitude === undefined) return "Not reported";
  return `M ${magnitude}${type ? " " + type : ""}`;
}

/** Every record is an epicenter point; the margin flag lets the map draw out-of-rectangle points distinctly. */
export function earthquakePoints(rows: Earthquake[] | undefined) {
  return (rows ?? []).filter(row => typeof row?.longitude === "number" && typeof row?.latitude === "number").map(row => ({
    type: "Feature" as const, id: row.event_id, geometry: { type: "Point" as const, coordinates: [row.longitude, row.latitude] },
    properties: { eventId: row.event_id, magnitude: row.magnitude ?? -1, margin: row.flags.includes("CONTEXT_MARGIN"), automatic: row.review_status === "automatic" } }));
}
