/**
 * Strict app-local adapter for a public-safe streamflow QC dashboard packet.
 *
 * The packet carries only finite classifications and opaque evidence
 * references emitted after upstream validation. It carries no raw flow value,
 * percentile threshold, coordinate, detector configuration, or write control.
 */

export const STREAMFLOW_QC_DASHBOARD_PROJECTION_PROFILE =
  "kfm.explorer.streamflow-qc-dashboard.public-safe.v1" as const;

export type StreamflowQcDashboardOutcome =
  | "AVAILABLE"
  | "ABSTAIN"
  | "DENY"
  | "ERROR";

export type StreamflowQcDashboardStatus =
  | "REGIONAL_CONTEXT"
  | "LOCAL_REVIEW"
  | "NO_ESCALATION"
  | "HELD"
  | "DENIED"
  | "UPSTREAM_ERROR";

export type StreamflowQcDashboardReason =
  | "REGIONAL_CONTEXT_AVAILABLE"
  | "LOCAL_REVIEW_AVAILABLE"
  | "NO_ESCALATION_AVAILABLE"
  | "CONTEXT_HELD"
  | "RELEASE_DENIED"
  | "UPSTREAM_ERROR";

export type StreamflowFlowState =
  | "LOW_PERCENTILE"
  | "NOT_LOW"
  | "UNKNOWN";
export type StreamflowCorroboration =
  | "CORROBORATES_LOW_FLOW"
  | "DOES_NOT_CORROBORATE"
  | "INSUFFICIENT";
export type StreamflowDroughtContext =
  | "SUPPORTS_LOW_FLOW"
  | "DOES_NOT_SUPPORT"
  | "UNKNOWN";
export type StreamflowIngestState =
  | "CLEAN"
  | "GAP_OR_INTEGRATION_CONCERN"
  | "UNKNOWN";
export type StreamflowUnitState = "COMPATIBLE" | "CONFLICT" | "UNKNOWN";
export type StreamflowCadenceState = "ON_TIME" | "LATE" | "UNKNOWN";
export type StreamflowQcPriority =
  | "ROUTINE"
  | "ELEVATED"
  | "HIGH"
  | "NONE";

export type GovernedStreamflowQcDashboardProjection = Readonly<{
  profile: typeof STREAMFLOW_QC_DASHBOARD_PROJECTION_PROFILE;
  outcome: StreamflowQcDashboardOutcome;
  status: StreamflowQcDashboardStatus;
  reasonCode: StreamflowQcDashboardReason;
  assessmentId: string | null;
  specHash: string | null;
  evaluatedAt: string;
  gaugeRef: string | null;
  flowState: StreamflowFlowState | null;
  adjacentGaugeCount: number | null;
  corroboration: StreamflowCorroboration | null;
  droughtContext: StreamflowDroughtContext | null;
  ingestState: StreamflowIngestState | null;
  unitState: StreamflowUnitState | null;
  cadenceState: StreamflowCadenceState | null;
  priority: StreamflowQcPriority | null;
  evidenceRefs: readonly string[];
  sensorInvalidated: false;
  hydrologicEventDeclared: false;
  detectorConfigurationMutated: false;
  policyEvaluated: false;
  reviewApproved: false;
  releaseAuthorized: false;
  publicationAuthorized: false;
  publicUseAllowed: false;
}>;

export type StreamflowQcDashboardProjectionResult =
  | Readonly<{
      ok: true;
      payload: GovernedStreamflowQcDashboardProjection;
    }>
  | Readonly<{
      ok: false;
      code: "MALFORMED_STREAMFLOW_QC_DASHBOARD_PROJECTION";
    }>;

const TOP_LEVEL_FIELDS = new Set([
  "profile",
  "outcome",
  "status",
  "reason_code",
  "assessment_id",
  "spec_hash",
  "evaluated_at",
  "gauge_ref",
  "flow_state",
  "adjacent_gauge_count",
  "corroboration",
  "drought_context",
  "ingest_state",
  "unit_state",
  "cadence_state",
  "priority",
  "evidence_refs",
  "sensor_invalidated",
  "hydrologic_event_declared",
  "detector_configuration_mutated",
  "policy_evaluated",
  "review_approved",
  "release_authorized",
  "publication_authorized",
  "public_use_allowed",
]);

const STATUS_BINDING = Object.freeze({
  REGIONAL_CONTEXT: Object.freeze({
    outcome: "AVAILABLE",
    reasonCode: "REGIONAL_CONTEXT_AVAILABLE",
  }),
  LOCAL_REVIEW: Object.freeze({
    outcome: "AVAILABLE",
    reasonCode: "LOCAL_REVIEW_AVAILABLE",
  }),
  NO_ESCALATION: Object.freeze({
    outcome: "AVAILABLE",
    reasonCode: "NO_ESCALATION_AVAILABLE",
  }),
  HELD: Object.freeze({
    outcome: "ABSTAIN",
    reasonCode: "CONTEXT_HELD",
  }),
  DENIED: Object.freeze({
    outcome: "DENY",
    reasonCode: "RELEASE_DENIED",
  }),
  UPSTREAM_ERROR: Object.freeze({
    outcome: "ERROR",
    reasonCode: "UPSTREAM_ERROR",
  }),
}) satisfies Readonly<
  Record<
    StreamflowQcDashboardStatus,
    Readonly<{
      outcome: StreamflowQcDashboardOutcome;
      reasonCode: StreamflowQcDashboardReason;
    }>
  >
>;

const FLOW_STATES = new Set<StreamflowFlowState>([
  "LOW_PERCENTILE",
  "NOT_LOW",
  "UNKNOWN",
]);
const CORROBORATION_STATES = new Set<StreamflowCorroboration>([
  "CORROBORATES_LOW_FLOW",
  "DOES_NOT_CORROBORATE",
  "INSUFFICIENT",
]);
const DROUGHT_STATES = new Set<StreamflowDroughtContext>([
  "SUPPORTS_LOW_FLOW",
  "DOES_NOT_SUPPORT",
  "UNKNOWN",
]);
const INGEST_STATES = new Set<StreamflowIngestState>([
  "CLEAN",
  "GAP_OR_INTEGRATION_CONCERN",
  "UNKNOWN",
]);
const UNIT_STATES = new Set<StreamflowUnitState>([
  "COMPATIBLE",
  "CONFLICT",
  "UNKNOWN",
]);
const CADENCE_STATES = new Set<StreamflowCadenceState>([
  "ON_TIME",
  "LATE",
  "UNKNOWN",
]);
const PRIORITIES = new Set<StreamflowQcPriority>([
  "ROUTINE",
  "ELEVATED",
  "HIGH",
  "NONE",
]);
const ASSESSMENT_ID = /^kfm:streamflow-qc-context:[a-f0-9]{24}$/;
const SPEC_HASH = /^sha256:[a-f0-9]{64}$/;
const GAUGE_REFERENCE = /^kfm:gauge:[a-z0-9][a-z0-9:._/-]{5,200}$/;
const EVIDENCE_REFERENCE =
  /^evidence:[a-z0-9][a-z0-9:._-]{5,200}$/;
const CANONICAL_UTC_SECOND =
  /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$/;
const CONTROL_CHARACTER =
  /[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/;
const DENIED_REFERENCE_MARKERS = [
  "postgres://",
  "neo4j://",
  "s3://",
  "file://",
  "select *",
  "match (",
] as const;
const INTERNAL_DATA_STAGES = [
  "raw",
  "work",
  "quarantine",
  "processed",
  "published",
] as const;

function malformed(): StreamflowQcDashboardProjectionResult {
  return Object.freeze({
    ok: false,
    code: "MALFORMED_STREAMFLOW_QC_DASHBOARD_PROJECTION",
  });
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function hasExactFields(
  value: Record<string, unknown>,
  fields: ReadonlySet<string>,
): boolean {
  return (
    Object.keys(value).length === fields.size &&
    Object.keys(value).every((field) => fields.has(field))
  );
}

function isCanonicalUtcSecond(value: unknown): value is string {
  if (typeof value !== "string" || !CANONICAL_UTC_SECOND.test(value)) {
    return false;
  }
  const parsed = Date.parse(value);
  return (
    Number.isFinite(parsed) &&
    new Date(parsed).toISOString().replace(".000Z", "Z") === value
  );
}

function isSafeReference(
  value: unknown,
  pattern: RegExp,
): value is string {
  if (
    typeof value !== "string" ||
    value.length > 256 ||
    !pattern.test(value) ||
    CONTROL_CHARACTER.test(value)
  ) {
    return false;
  }
  const lowered = value.toLowerCase();
  return (
    !DENIED_REFERENCE_MARKERS.some((marker) => lowered.includes(marker)) &&
    !INTERNAL_DATA_STAGES.some((stage) => lowered.includes(`data/${stage}`))
  );
}

function parseEvidenceRefs(value: unknown): readonly string[] | null {
  if (
    !Array.isArray(value) ||
    value.length < 1 ||
    value.length > 32 ||
    !value.every((item) => isSafeReference(item, EVIDENCE_REFERENCE))
  ) {
    return null;
  }
  const references = value as string[];
  if (
    new Set(references).size !== references.length ||
    references.some(
      (item, index) => index > 0 && references[index - 1] >= item,
    )
  ) {
    return null;
  }
  return Object.freeze([...references]);
}

function hasFalseAuthorityFlags(input: Record<string, unknown>): boolean {
  return [
    "sensor_invalidated",
    "hydrologic_event_declared",
    "detector_configuration_mutated",
    "policy_evaluated",
    "review_approved",
    "release_authorized",
    "publication_authorized",
    "public_use_allowed",
  ].every((field) => input[field] === false);
}

function hasNullDetails(input: Record<string, unknown>): boolean {
  return (
    input.assessment_id === null &&
    input.spec_hash === null &&
    input.gauge_ref === null &&
    input.flow_state === null &&
    input.adjacent_gauge_count === null &&
    input.corroboration === null &&
    input.drought_context === null &&
    input.ingest_state === null &&
    input.unit_state === null &&
    input.cadence_state === null &&
    input.priority === null &&
    Array.isArray(input.evidence_refs) &&
    input.evidence_refs.length === 0
  );
}

function hasPositiveSemantics(
  input: Record<string, unknown>,
  status: Extract<
    StreamflowQcDashboardStatus,
    "REGIONAL_CONTEXT" | "LOCAL_REVIEW" | "NO_ESCALATION"
  >,
): boolean {
  if (
    typeof input.flow_state !== "string" ||
    !FLOW_STATES.has(input.flow_state as StreamflowFlowState) ||
    !Number.isInteger(input.adjacent_gauge_count) ||
    (input.adjacent_gauge_count as number) < 0 ||
    (input.adjacent_gauge_count as number) > 64 ||
    typeof input.corroboration !== "string" ||
    !CORROBORATION_STATES.has(
      input.corroboration as StreamflowCorroboration,
    ) ||
    typeof input.drought_context !== "string" ||
    !DROUGHT_STATES.has(
      input.drought_context as StreamflowDroughtContext,
    ) ||
    typeof input.ingest_state !== "string" ||
    !INGEST_STATES.has(input.ingest_state as StreamflowIngestState) ||
    typeof input.unit_state !== "string" ||
    !UNIT_STATES.has(input.unit_state as StreamflowUnitState) ||
    typeof input.cadence_state !== "string" ||
    !CADENCE_STATES.has(input.cadence_state as StreamflowCadenceState) ||
    typeof input.priority !== "string" ||
    !PRIORITIES.has(input.priority as StreamflowQcPriority)
  ) {
    return false;
  }

  if (
    input.corroboration === "CORROBORATES_LOW_FLOW" &&
    (input.adjacent_gauge_count as number) < 1
  ) {
    return false;
  }

  const integrityClear =
    input.ingest_state === "CLEAN" &&
    input.unit_state === "COMPATIBLE" &&
    input.cadence_state === "ON_TIME";

  if (status === "REGIONAL_CONTEXT") {
    return (
      input.flow_state === "LOW_PERCENTILE" &&
      input.corroboration === "CORROBORATES_LOW_FLOW" &&
      input.drought_context === "SUPPORTS_LOW_FLOW" &&
      integrityClear &&
      input.priority === "ROUTINE"
    );
  }

  if (status === "LOCAL_REVIEW") {
    return (
      input.flow_state === "LOW_PERCENTILE" &&
      (input.priority === "ELEVATED" || input.priority === "HIGH") &&
      (!integrityClear ||
        input.corroboration !== "CORROBORATES_LOW_FLOW" ||
        input.drought_context !== "SUPPORTS_LOW_FLOW")
    );
  }

  return (
    input.flow_state === "NOT_LOW" &&
    input.adjacent_gauge_count === 0 &&
    input.corroboration === "INSUFFICIENT" &&
    input.drought_context === "UNKNOWN" &&
    integrityClear &&
    input.priority === "NONE"
  );
}

/**
 * Parse one closed dashboard projection emitted after the domain assessment.
 *
 * A successful result proves only browser-local packet consistency. It does
 * not recalculate a percentile or authorize review, release, or publication.
 */
export function parseStreamflowQcDashboardProjection(
  input: unknown,
): StreamflowQcDashboardProjectionResult {
  if (
    !isRecord(input) ||
    !hasExactFields(input, TOP_LEVEL_FIELDS) ||
    input.profile !== STREAMFLOW_QC_DASHBOARD_PROJECTION_PROFILE ||
    typeof input.status !== "string" ||
    !Object.hasOwn(STATUS_BINDING, input.status) ||
    !isCanonicalUtcSecond(input.evaluated_at) ||
    !hasFalseAuthorityFlags(input)
  ) {
    return malformed();
  }

  const status = input.status as StreamflowQcDashboardStatus;
  const binding = STATUS_BINDING[status];
  if (
    input.outcome !== binding.outcome ||
    input.reason_code !== binding.reasonCode
  ) {
    return malformed();
  }

  if (binding.outcome !== "AVAILABLE") {
    if (!hasNullDetails(input)) return malformed();
    return Object.freeze({
      ok: true,
      payload: Object.freeze({
        profile: STREAMFLOW_QC_DASHBOARD_PROJECTION_PROFILE,
        outcome: binding.outcome,
        status,
        reasonCode: binding.reasonCode,
        assessmentId: null,
        specHash: null,
        evaluatedAt: input.evaluated_at,
        gaugeRef: null,
        flowState: null,
        adjacentGaugeCount: null,
        corroboration: null,
        droughtContext: null,
        ingestState: null,
        unitState: null,
        cadenceState: null,
        priority: null,
        evidenceRefs: Object.freeze([]),
        sensorInvalidated: false,
        hydrologicEventDeclared: false,
        detectorConfigurationMutated: false,
        policyEvaluated: false,
        reviewApproved: false,
        releaseAuthorized: false,
        publicationAuthorized: false,
        publicUseAllowed: false,
      }),
    });
  }

  const positiveStatus = status as Extract<
    StreamflowQcDashboardStatus,
    "REGIONAL_CONTEXT" | "LOCAL_REVIEW" | "NO_ESCALATION"
  >;
  if (
    typeof input.assessment_id !== "string" ||
    !ASSESSMENT_ID.test(input.assessment_id) ||
    typeof input.spec_hash !== "string" ||
    !SPEC_HASH.test(input.spec_hash) ||
    input.assessment_id.slice("kfm:streamflow-qc-context:".length) !==
      input.spec_hash.slice("sha256:".length, "sha256:".length + 24) ||
    !isSafeReference(input.gauge_ref, GAUGE_REFERENCE) ||
    !hasPositiveSemantics(input, positiveStatus)
  ) {
    return malformed();
  }
  const evidenceRefs = parseEvidenceRefs(input.evidence_refs);
  if (evidenceRefs === null) return malformed();

  return Object.freeze({
    ok: true,
    payload: Object.freeze({
      profile: STREAMFLOW_QC_DASHBOARD_PROJECTION_PROFILE,
      outcome: "AVAILABLE",
      status: positiveStatus,
      reasonCode: binding.reasonCode,
      assessmentId: input.assessment_id,
      specHash: input.spec_hash,
      evaluatedAt: input.evaluated_at,
      gaugeRef: input.gauge_ref,
      flowState: input.flow_state as StreamflowFlowState,
      adjacentGaugeCount: input.adjacent_gauge_count as number,
      corroboration: input.corroboration as StreamflowCorroboration,
      droughtContext: input.drought_context as StreamflowDroughtContext,
      ingestState: input.ingest_state as StreamflowIngestState,
      unitState: input.unit_state as StreamflowUnitState,
      cadenceState: input.cadence_state as StreamflowCadenceState,
      priority: input.priority as StreamflowQcPriority,
      evidenceRefs,
      sensorInvalidated: false,
      hydrologicEventDeclared: false,
      detectorConfigurationMutated: false,
      policyEvaluated: false,
      reviewApproved: false,
      releaseAuthorized: false,
      publicationAuthorized: false,
      publicUseAllowed: false,
    }),
  });
}
