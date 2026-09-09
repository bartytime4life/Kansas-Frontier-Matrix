export const LIVING_ATLAS_PROFILE = "kfm.explorer.living-atlas.v1" as const;

export const MAP_REPRESENTATIONS = [
  "2D",
  "TERRAIN_3D",
  "GLOBE",
  "COMPARE",
] as const;

export type MapRepresentation = (typeof MAP_REPRESENTATIONS)[number];

export const TRUST_STATES = [
  "RELEASED",
  "SOURCE_BACKED_CONTEXT",
  "SITE_LOCAL_DEMO",
  "SYNTHETIC",
  "GENERALIZED",
  "STALE",
  "DEGRADED",
  "HELD",
  "RESTRICTED",
  "DENIED",
  "UNAVAILABLE",
] as const;

export type TrustState = (typeof TRUST_STATES)[number];

export type FocusOutcome = "ANSWER" | "ABSTAIN" | "DENY" | "ERROR";

export type SourceAdmissionState =
  | "CANDIDATE"
  | "CONTEXT_ONLY"
  | "ADMITTED"
  | "HELD"
  | "QUARANTINED"
  | "DENIED";

export type TemporalExtent = Readonly<{
  id: string;
  label: string;
  startLabel: string;
  endLabel: string;
  precision:
    | "GEOLOGIC"
    | "ERA"
    | "PERIOD"
    | "CENTURY"
    | "YEAR"
    | "DATE"
    | "UNKNOWN";
  kind: "INTERVAL" | "INSTANT" | "TIMELESS" | "UNKNOWN";
  order: number;
  uncertainty: string | null;
}>;

export type SourceDescriptor = Readonly<{
  id: string;
  title: string;
  organization: string;
  domain: string;
  admissionState: SourceAdmissionState;
  sourceRole: "OFFICIAL" | "CONTEXT" | "SITE_LOCAL_FIXTURE";
  cadence: string;
  dataMode: string;
  value: string;
  cannotProve: string;
  nextGate: string;
  officialUrl: string | null;
  lastChecked: string;
  rights: string;
  sensitivity: string;
}>;

export type LayerRecord = Readonly<{
  id: string;
  name: string;
  domain: string;
  sourceId: string;
  evidenceId: string;
  geometryType: "POINT" | "LINE" | "POLYGON" | "RASTER" | "GRID";
  temporalExtentId: string;
  trustState: TrustState;
  availability: "AVAILABLE" | "HELD" | "DENIED" | "UNAVAILABLE";
  representation: "MAPLIBRE_INLINE" | "CATALOG_ONLY";
  scaleLimit: string;
  warning: string;
  defaultVisible: boolean;
  defaultOpacity: number;
  color: string;
}>;

export type EvidenceRecord = Readonly<{
  id: string;
  title: string;
  layerId: string;
  sourceId: string;
  trustState: TrustState;
  confidence: "BOUNDED" | "CONTEXT_ONLY" | "NOT_ASSESSED";
  spatialScope: string;
  temporalScope: string;
  supports: string;
  cannotProve: string;
  limitations: readonly string[];
  sensitivity: string;
  policyStatus: "ALLOW_DEMO" | "ABSTAIN" | "DENY";
  evidenceRefs: readonly string[];
}>;

export type AtlasView = Readonly<{
  id: string;
  name: string;
  question: string;
  representation: MapRepresentation;
  layerIds: readonly string[];
  temporalExtentId: string;
  status: "SITE_LOCAL_DEMO" | "DESIGN_DATA_HOLD";
  statusReason: string;
  camera: Readonly<{
    longitude: number;
    latitude: number;
    zoom: number;
    bearing: number;
    pitch: number;
  }>;
}>;

export type MapLayerState = Readonly<{
  id: string;
  visible: boolean;
  opacity: number;
}>;

export type MapSnapshot = Readonly<{
  profile: "kfm.explorer.map-snapshot.v1";
  capturedAt: string;
  area: string;
  representation: MapRepresentation;
  basemap: "SITE_LOCAL_ATLAS";
  camera: AtlasView["camera"];
  committedTimeId: string;
  activeViewId: string;
  layers: readonly MapLayerState[];
  selectedLayerId: string | null;
  evidenceRefs: readonly string[];
  publicSafe: true;
  draftOnly: true;
}>;

export type ReportDraft = Readonly<{
  profile: "kfm.explorer.report-draft.v1";
  id: string;
  title: string;
  researchQuestion: string;
  createdAt: string;
  snapshot: MapSnapshot;
  includedEvidenceRefs: readonly string[];
  sections: Readonly<{
    summary: string;
    observations: string;
    findings: string;
    limitations: string;
    openQuestions: string;
  }>;
  lifecycle: "DRAFT";
  publishable: false;
}>;

export type StoryScene = Readonly<{
  profile: "kfm.explorer.story-scene.v1";
  id: string;
  title: string;
  narrative: string;
  order: number;
  snapshot: MapSnapshot;
  evidenceRefs: readonly string[];
  caveats: readonly string[];
  motion: "NONE" | "CAMERA_GUIDE";
  lifecycle: "DRAFT";
}>;

export type PolicyDecision = Readonly<{
  profile: "kfm.explorer.policy-decision.v1";
  outcome: FocusOutcome;
  reasonCode: string;
  summary: string;
  evidenceRefs: readonly string[];
  proposedActions: readonly string[];
  generated: false;
}>;

export type RepositoryConnectionState =
  | "FIXTURE_ONLY"
  | "CAPTURE_FIXTURE"
  | "PROPOSED_INACTIVE"
  | "DOCUMENTED_ONLY";

export type RepositoryArtifactRef = Readonly<{
  kind: "CONNECTOR" | "PIPELINE" | "CONTRACT";
  label: string;
  path: string;
}>;

export type RepositoryLayerConnection = Readonly<{
  id: string;
  name: string;
  domain: string;
  geometryType: LayerRecord["geometryType"];
  source: string;
  state: RepositoryConnectionState;
  summary: string;
  statusReason: string;
  cannotProve: string;
  nextGate: string;
  artifacts: readonly RepositoryArtifactRef[];
  relatedToolIds: readonly string[];
}>;

export type MapInteractionTool = Readonly<{
  id: "select" | "draw" | "measure" | "profile";
  name: string;
  state: "AVAILABLE_IN_SITE" | "HELD";
  summary: string;
  statusReason: string;
}>;

export type AtlasWorkbenchTool = Readonly<{
  id: string;
  name: string;
  maturity: "FIXTURE_FIRST" | "DOCUMENTED";
  summary: string;
  featurePath: string;
  catalogQuery: string;
  relatedLayerConnectionIds: readonly string[];
}>;
