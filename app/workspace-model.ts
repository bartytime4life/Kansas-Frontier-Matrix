import type { EvidenceState, LayerRecord } from "./explorer-data";
import type { TemporalStepRule, TemporalSweepMode } from "./temporal-sweep";

export type { LayerRecord };

export type TrustState =
  | "Released"
  | "Source-backed context"
  | "Site-local demo"
  | "Synthetic"
  | "Generalized"
  | "Stale"
  | "Degraded"
  | "Held"
  | "Restricted"
  | "Denied"
  | "Unavailable";

export type TemporalExtent = Readonly<{
  start: number;
  end: number;
  label: string;
  mode: "instant" | "interval" | "cumulative" | "timeless" | "unknown";
  uncertainty?: string;
}>;

export type SourceDescriptor = Readonly<{
  id: string;
  organization: string;
  title: string;
  role: string;
  admission: "candidate" | "context-only" | "admitted" | "held" | "quarantined" | "denied";
  officialUrl?: string;
  checkedAt?: string;
  licenseOrAccess: string;
  limitation: string;
}>;

export type EvidenceRecord = Readonly<{
  id: string;
  featureId: string;
  layerId: string;
  title: string;
  domain: string;
  sourceOrganization: string;
  sourceRole: string;
  citation: string;
  officialUrl?: string;
  spatialScope: string;
  temporalExtent: TemporalExtent;
  trustState: TrustState;
  evidenceState: EvidenceState;
  supports: string;
  cannotProve: string;
  caveat: string;
  policyStatus: string;
  includedByDefault: boolean;
  displayFocus?: readonly [number, number];
}>;

export type PolicyDecision = Readonly<{
  outcome: "ALLOW" | "ABSTAIN" | "DENY" | "ERROR";
  reason: string;
  publicEffect: "NONE" | "DRAFT_ONLY";
}>;

export type MapSnapshot = Readonly<{
  id: string;
  createdAt: string;
  area: Readonly<{
    kind: "selection" | "aoi" | "viewport";
    label: string;
    bounds?: Readonly<{ west: number; south: number; east: number; north: number }>;
  }>;
  camera: Readonly<{
    center: readonly [number, number] | "WITHHELD_BROWSER_LOCATION";
    zoom: number | "WITHHELD";
    bearing: number | "WITHHELD";
    pitch: number | "WITHHELD";
  }>;
  representation: "2D" | "Terrain 3D" | "Globe" | "Compare";
  projection: "mercator" | "globe";
  basemap: string;
  evidenceFilter?: EvidenceState | "ALL";
  comparison?: Readonly<{ layerA: string; layerB: string; timeA: number; timeB: number }>;
  temporalSweep?: Readonly<{
    mode: TemporalSweepMode;
    frame: number;
    rangeStart: number;
    rangeEnd: number;
    windowStart: number;
    windowFrames: number;
    stepRule: TemporalStepRule;
    interpolation: false;
  }>;
  committedTime: TemporalExtent;
  visibleLayers: readonly Readonly<{
    id: string;
    title: string;
    domain: string;
    order: number;
    opacity: number;
    trustState: TrustState;
  }>[];
  selection: Readonly<{
    featureId: string;
    layerId: string;
    title: string;
    evidenceReference: string;
    trustState: TrustState;
  }> | null;
  evidenceRefs: readonly string[];
  inspectableFeatureIds?: readonly string[];
  inspectableRecordCount: number;
  sourceBackedCount: number;
  boundedCount: number;
  policy: PolicyDecision;
}>;

export type ReportDraft = Readonly<{
  id: string;
  status: "DRAFT";
  updatedAt: string;
  snapshot: MapSnapshot;
  title: string;
  researchQuestion: string;
  includedEvidenceIds: readonly string[];
  sections: Readonly<{
    summary: string;
    observations: string;
    findings: string;
    limitations: string;
    openQuestions: string;
    sources: string;
  }>;
  generatedFields: readonly (keyof ReportDraft["sections"])[];
}>;

export type StoryScene = Readonly<{
  id: string;
  title: string;
  narrative: string;
  snapshot: MapSnapshot;
  evidenceRefs: readonly string[];
  caveats: readonly string[];
  motion: "none" | "ease";
}>;

export type StoryDraft = Readonly<{
  id: string;
  status: "DRAFT";
  updatedAt: string;
  title: string;
  researchQuestion: string;
  scenes: readonly StoryScene[];
  baseSnapshot?: MapSnapshot;
}>;

export const trustStateFromEvidenceState = (state: EvidenceState, sourceRole = "synthetic"): TrustState => {
  switch (state) {
    case "ANSWER":
    case "CORRECTED": return sourceRole === "source-backed-context" ? "Source-backed context" : sourceRole === "synthetic" ? "Synthetic" : "Site-local demo";
    case "GENERALIZED_GEOMETRY": return "Generalized";
    case "SOURCE_STALE": return "Stale";
    case "RESTRICTED_ACCESS": return "Restricted";
    case "DENIED_BY_POLICY": return "Denied";
    case "ERROR": return "Degraded";
    case "SUPERSEDED": return "Held";
    case "MISSING_EVIDENCE": return "Unavailable";
  }
};

export const policyDecisionFromEvidenceState = (state?: EvidenceState): PolicyDecision => {
  if (state === "DENIED_BY_POLICY" || state === "RESTRICTED_ACCESS") {
    return { outcome: "DENY", reason: "Policy or access controls prohibit precise disclosure.", publicEffect: "NONE" };
  }
  if (state === "ERROR") {
    return { outcome: "ERROR", reason: "Evidence resolution did not complete; no fallback claim is allowed.", publicEffect: "NONE" };
  }
  if (!state || state === "MISSING_EVIDENCE" || state === "SOURCE_STALE" || state === "GENERALIZED_GEOMETRY" || state === "SUPERSEDED") {
    return { outcome: "ABSTAIN", reason: "The current evidence posture does not close a consequential claim.", publicEffect: "DRAFT_ONLY" };
  }
  return { outcome: "ALLOW", reason: "The bounded demonstration record may be cited within its declared scope.", publicEffect: "DRAFT_ONLY" };
};

export const createReportDraft = (snapshot: MapSnapshot, evidence: readonly EvidenceRecord[]): ReportDraft => {
  const included = evidence.filter((record) => snapshot.evidenceRefs.includes(record.citation) && record.includedByDefault
    && (snapshot.inspectableFeatureIds ? snapshot.inspectableFeatureIds.includes(record.featureId) || snapshot.selection?.featureId === record.featureId : snapshot.visibleLayers.some((layer) => layer.id === record.layerId)));
  return {
    id: `report-${snapshot.id}`,
    status: "DRAFT",
    updatedAt: snapshot.createdAt,
    snapshot,
    title: snapshot.selection ? `${snapshot.selection.title} evidence note` : "Kansas map investigation",
    researchQuestion: "What does the current map state support, and what remains uncertain?",
    includedEvidenceIds: included.map((record) => record.id),
    sections: {
      summary: "This draft records the current map selection and its evidence posture.",
      observations: "Visible geometry and proximity are map observations only; they are not proof of a relationship.",
      findings: "No consequential finding has been asserted. Add a scoped finding only when the included evidence supports it.",
      limitations: "Basemap, terrain, synthetic, generalized, stale, held, and denied material remain visibly bounded by their source and policy states.",
      openQuestions: "Which source, temporal, spatial, rights, or review gate should be closed next?",
      sources: included.length
        ? included.map((record) => `${record.citation} — ${record.sourceOrganization}`).join("\n")
        : "No included evidence references yet.",
    },
    generatedFields: ["summary", "observations", "findings", "limitations", "openQuestions", "sources"],
  };
};

const sceneSnapshot = (
  snapshot: MapSnapshot,
  id: string,
  label: string,
  time: number,
  evidenceRef: string,
  evidence: readonly EvidenceRecord[],
): MapSnapshot => {
  const record = evidence.find((item) => item.citation === evidenceRef);
  const layer = record ? { id: record.layerId, title: record.domain, domain: record.domain, order: 0, opacity: .85, trustState: record.trustState } : undefined;
  return ({
  ...snapshot,
  id: `${snapshot.id}-${id}`,
  committedTime: { start: time, end: time, label, mode: "instant" },
  temporalSweep: { mode: "snapshot", frame: time, rangeStart: time, rangeEnd: time, windowStart: time, windowFrames: 1, stepRule: "available-events", interpolation: false },
  comparison: undefined,
  evidenceFilter: "ALL",
  evidenceRefs: [evidenceRef],
  area: { kind: "viewport", label: record?.spatialScope ?? "Kansas demonstration context" },
  camera: { center: record?.displayFocus ?? [-98.38, 38.48], zoom: record ? 6.4 : 5.4, bearing: 0, pitch: 0 },
  representation: "2D",
  projection: "mercator",
  visibleLayers: layer ? [layer] : [],
  selection: record ? { featureId: record.featureId, layerId: record.layerId, title: record.title, evidenceReference: record.citation, trustState: record.trustState } : null,
  inspectableFeatureIds: record ? [record.featureId] : [],
  inspectableRecordCount: record ? 1 : 0,
  sourceBackedCount: 0,
  boundedCount: record ? 1 : 0,
  policy: policyDecisionFromEvidenceState(record?.evidenceState),
  });
};

export const createTrustStory = (snapshot: MapSnapshot, evidence: readonly EvidenceRecord[] = []): StoryDraft => ({
  id: `story-${snapshot.id}`,
  status: "DRAFT",
  updatedAt: snapshot.createdAt,
  baseSnapshot: snapshot,
  title: "Trust in the map",
  researchQuestion: "How does KFM keep evidence, correction, time, and policy visible?",
  scenes: [
    {
      id: `scene-supported-${snapshot.id}`,
      title: "A bounded claim can show its support",
      narrative: "A site-local Topeka observation demonstrates how a selected map candidate points to a visible evidence reference without turning the renderer into the source of truth.",
      snapshot: sceneSnapshot(snapshot, "supported", "2026 demonstration observation", 2026, "kfm:evidence:synthetic:atmo-2026", evidence),
      evidenceRefs: ["kfm:evidence:synthetic:atmo-2026"],
      caveats: ["Synthetic observation; not current weather, air-quality, forecasting, or life-safety guidance."],
      motion: "ease",
    },
    {
      id: `scene-corrected-${snapshot.id}`,
      title: "A correction stays with the record",
      narrative: "The 2024 Hays fixture keeps its correction state visible so a newer interpretation cannot silently erase lineage.",
      snapshot: sceneSnapshot(snapshot, "corrected", "2024 corrected demonstration", 2024, "kfm:evidence:synthetic:atmo-2024-r2", evidence),
      evidenceRefs: ["kfm:evidence:synthetic:atmo-2024-r2"],
      caveats: ["Correction behavior is demonstrated with invented values and geometry."],
      motion: "ease",
    },
    {
      id: `scene-historical-${snapshot.id}`,
      title: "Historical context remains historical",
      narrative: "A 1910 study-line fixture demonstrates a dated edition without asserting an undocumented route or carrying it forward as current truth.",
      snapshot: sceneSnapshot(snapshot, "historical", "1910 historical fixture", 1910, "kfm:evidence:synthetic:history-1910", evidence),
      evidenceRefs: ["kfm:evidence:synthetic:history-1910"],
      caveats: ["Illustrative line only; not a documented historical route."],
      motion: "ease",
    },
    {
      id: `scene-denied-${snapshot.id}`,
      title: "Protected detail fails closed",
      narrative: "A deliberately coarse envelope preserves the existence of a policy boundary while precise subject matter, attributes, and geometry remain absent.",
      snapshot: sceneSnapshot(snapshot, "denied", "Protected time withheld", 2026, "kfm:policy:public-safe:deny-demo", evidence),
      evidenceRefs: ["kfm:policy:public-safe:deny-demo"],
      caveats: ["No protected detail is present, inferred, reconstructed, or exposed."],
      motion: "none",
    },
  ],
});
