import type { EvidenceState, LayerRecord } from "./explorer-data";
import type { TemporalStepRule, TemporalSweepMode } from "./temporal-sweep";
import type { FireReportContext } from "./fire-report-analysis";
import { persistableSubsurface, type SubsurfaceContext } from "./subsurface-model";
import { persistableResearch, type ResearchContext } from "./research-context";

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
  terrainProvider?: "mapzen" | "usgs-3dep";
  terrainExaggeration?: number;
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

export function terrainSnapshotDescription(snapshot: MapSnapshot): string | null {
  if (snapshot.representation !== "Terrain 3D") return null;
  if (!snapshot.terrainProvider || snapshot.terrainExaggeration === undefined) {
    return "DEM source and display scale were not recorded in this saved snapshot; external display context only, not admitted KFM evidence.";
  }
  const source = snapshot.terrainProvider === "usgs-3dep" ? "USGS 3DEP dynamic DEM mosaic" : "Mapzen Terrarium DEM";
  return `${source} at ${snapshot.terrainExaggeration.toFixed(2)}× vertical display scale; external display context only, not admitted KFM evidence.`;
}

export type ReportDraft = Readonly<{
  id: string;
  status: "DRAFT";
  updatedAt: string;
  snapshot: MapSnapshot;
  title: string;
  researchQuestion: string;
  includedEvidenceIds: readonly string[];
  fireContext?: FireReportContext;
  researchContext?: ResearchContext;
  subsurfaceContext?: SubsurfaceContext;
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

export const createReportDraft = (snapshot: MapSnapshot, evidence: readonly EvidenceRecord[], fireContext?: FireReportContext, research?: ResearchContext, subsurface?: SubsurfaceContext): ReportDraft => {
  const subsurfaceContext = persistableSubsurface(subsurface ?? null, snapshot.camera.center === "WITHHELD_BROWSER_LOCATION");
  const researchContext = persistableResearch(research ?? null, snapshot.camera.center === "WITHHELD_BROWSER_LOCATION");
  const included = evidence.filter((record) => snapshot.evidenceRefs.includes(record.citation) && record.includedByDefault
    && (snapshot.inspectableFeatureIds ? snapshot.inspectableFeatureIds.includes(record.featureId) || snapshot.selection?.featureId === record.featureId : snapshot.visibleLayers.some((layer) => layer.id === record.layerId)));
  return {
    id: `report-${snapshot.id}`,
    status: "DRAFT",
    updatedAt: snapshot.createdAt,
    snapshot,
    title: fireContext ? `${fireContext.title} fire report draft` : snapshot.selection ? `${snapshot.selection.title} evidence note` : "Kansas map investigation",
    researchQuestion: fireContext ? "What do the selected fire source and its dated context actually report?" : "What does the current map state support, and what remains uncertain?",
    includedEvidenceIds: included.map((record) => record.id),
    ...(fireContext ? { fireContext } : {}),
    ...(researchContext ? { researchContext } : {}),
    ...(subsurfaceContext ? { subsurfaceContext } : {}),
    sections: {
      summary: fireContext ? `Draft from ${fireContext.kind === "nifc-fire-reports" ? "a NIFC working incident record" : "a NASA thermal detection"}. Check the source record before making any claim.` : "This draft records the current map selection and its evidence posture.",
      observations: fireContext ? `Provider event/acquisition time: ${fireContext.observedAt ?? "not supplied"}. KFM retrieval time: ${fireContext.retrievedAt ?? "not supplied"}. Feed: ${fireContext.feedState}. Nearby records are comparison context, not an incident match.` : "Visible geometry and proximity are map observations only; they are not proof of a relationship.",
      findings: "No consequential finding has been asserted. Add a scoped finding only when the included evidence supports it.",
      limitations: fireContext ? "NIFC locations are approximate working records; NASA thermal points may be non-wildfire heat sources. News links are research leads, not matched articles. No perimeter, current activity, safety status, or independent corroboration is established." : "Basemap, terrain, synthetic, generalized, stale, held, and denied material remain visibly bounded by their source and policy states.",
      openQuestions: "Which source, temporal, spatial, rights, or review gate should be closed next?",
      sources: fireContext ? `${fireContext.sourceUrl}\nhttps://inciweb.wildfire.gov/\nhttps://www.nifc.gov/fire-information\nNo news article has been matched to this selected record.` : included.length
        ? included.map((record) => `${record.citation} — ${record.sourceOrganization}`).join("\n")
        : "No included evidence references yet.",
    },
    generatedFields: ["summary", "observations", "findings", "limitations", "openQuestions", "sources"],
  };
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
      id: `scene-current-${snapshot.id}`,
      title: snapshot.selection?.title ?? "Current Kansas investigation",
      narrative: "This scene preserves the captured map camera, representation, committed time, layer stack, selection, and evidence posture. Add a scoped narrative after checking the available sources.",
      snapshot,
      evidenceRefs: snapshot.evidenceRefs.filter((reference) => evidence.some((record) => record.citation === reference)),
      caveats: [
        "Map appearance and spatial overlap are context, not independent evidence.",
        "Protected detail fails closed; withheld locations remain absent.",
      ],
      motion: "none",
    },
  ],
});
