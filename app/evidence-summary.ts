import { officialSourceTopics, registryLayerTopics, type TopicId } from "./layer-workspaces";

/**
 * The Evidence Drawer's plain-language summary of a selection, in the same
 * three questions for every category: what it is, where and when, and its
 * source and limits. It restates fields the selection already carries; it
 * never upgrades an evidence state or adds a claim.
 */
export type EvidenceSummaryInput = Readonly<{
  kind: "registry" | "basemap";
  officialId: string | null;
  layerDomain: string;
  title: string;
  summary: string;
  sourceOrganization: string;
  spatialScope: string;
  temporalScope: string;
  observedAt?: string | null;
  lastUpdate?: string;
  evidenceState: string;
  generalizationNote: string;
  uncertainty: string;
  focusLng: number;
  focusLat: number;
}>;

export type EvidenceSummary = Readonly<{
  topics: readonly TopicId[];
  what: string;
  where: string;
  when: string;
  source: string;
  status: string;
  limits: string;
}>;

/** Category membership by source identity, the same rule the Layers catalogue uses. */
export function selectionTopics(kind: EvidenceSummaryInput["kind"], officialId: string | null, layerDomain: string): readonly TopicId[] {
  if (officialId) return officialSourceTopics(officialId);
  if (kind === "registry") return registryLayerTopics(layerDomain);
  return [];
}

const coordinate = (lng: number, lat: number): string | null => Number.isFinite(lng) && Number.isFinite(lat) && Math.abs(lat) <= 90 && Math.abs(lng) <= 180
  ? `${Math.abs(lat).toFixed(3)}° ${lat >= 0 ? "N" : "S"}, ${Math.abs(lng).toFixed(3)}° ${lng >= 0 ? "E" : "W"}`
  : null;
const clean = (value: string | null | undefined) => (value ?? "").replace(/\s+/g, " ").trim();
const ISO_TIME = /^\d{4}-\d{2}-\d{2}(?:[T ][\d:.]+(?:Z|[+-]\d{2}:?\d{2})?)?$/;

/**
 * `lastUpdate` means different things by carrier, so it is labelled by what it
 * is, never as a provider update: an official feature carries its retrieval
 * time (or the source's listed freshness when none was recorded), a basemap
 * record carries no time, and a registry record carries its own update.
 */
function updateClause(input: EvidenceSummaryInput, value: string): string {
  if (!value) return "";
  // Official provider features arrive as basemap-kind selections with their source id.
  if (input.officialId) return ISO_TIME.test(value) ? `retrieved ${value}` : `listed freshness: ${value}`;
  return input.kind === "basemap" ? "" : `record updated ${value}`;
}

export function evidenceSummary(input: EvidenceSummaryInput): EvidenceSummary {
  const at = coordinate(input.focusLng, input.focusLat);
  const scope = clean(input.spatialScope);
  const time = clean(input.observedAt) || clean(input.temporalScope);
  const updated = clean(input.lastUpdate);
  return {
    topics: selectionTopics(input.kind, input.officialId, input.layerDomain),
    what: input.kind === "basemap" ? "A provider’s mapped record and the attributes it reports." : clean(input.summary) || clean(input.title),
    where: [scope, at && `display anchor ${at}`].filter(Boolean).join(" · ") || "No location recorded",
    when: [time || "No time recorded", updated !== time ? updateClause(input, updated) : ""].filter(Boolean).join(" · "),
    source: clean(input.sourceOrganization) || "Source not recorded",
    status: input.kind === "basemap" ? "External context only · no KFM EvidenceBundle" : clean(input.evidenceState) || "Evidence state not recorded",
    limits: [clean(input.generalizationNote), clean(input.uncertainty)].filter(Boolean).join(" ") || "No limitation is recorded; that does not mean there is none.",
  };
}
