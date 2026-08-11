/**
 * Strict fixture-only projection for a PM2.5 trigger-candidate panel.
 *
 * The browser accepts categorical, reference-only display state. It never
 * receives concentrations, thresholds, AQI values, coordinates, station
 * identities, health categories, detector configuration, or policy detail.
 */

export const AIR_QUALITY_TRIGGER_PROJECTION_PROFILE =
  "kfm.explorer.air-quality-trigger.fixture.v1" as const;

export type AirQualityPanelOutcome = "ANSWER" | "ABSTAIN" | "DENY" | "ERROR";
export type AirQualityPanelReasonCode =
  | "TRIGGER_CANDIDATE_AVAILABLE"
  | "NO_TRIGGER_CANDIDATE"
  | "CONTEXT_HELD"
  | "POLICY_DENIED"
  | "UPSTREAM_ERROR";
export type AirQualityCandidateState =
  | "PROPOSED_TRIGGER_CANDIDATE"
  | "NO_TRIGGER_CANDIDATE";
export type AirQualityThresholdRelation =
  | "ABOVE_MONITORED_THRESHOLD"
  | "AT_OR_BELOW_MONITORED_THRESHOLD";
export type AirQualityMedianRelation =
  | "ABOVE_TRAILING_MEDIAN"
  | "AT_OR_BELOW_TRAILING_MEDIAN";

export type AirQualityTriggerCandidate = Readonly<{
  assessmentRef: string;
  candidateState: AirQualityCandidateState;
  observationRef: string;
  trailingMedianRef: string;
  observedAt: string;
  knowledgeCharacter: "OBSERVED_SENSOR";
  thresholdRelation: AirQualityThresholdRelation;
  trailingMedianRelation: AirQualityMedianRelation;
  evidenceState: "REFERENCED_NOT_RESOLVED";
  evidenceRefs: readonly string[];
}>;

export type GovernedAirQualityTriggerProjection = Readonly<{
  profile: typeof AIR_QUALITY_TRIGGER_PROJECTION_PROFILE;
  panelId: string;
  outcome: AirQualityPanelOutcome;
  reasonCode: AirQualityPanelReasonCode;
  status: "PROPOSED_INACTIVE";
  executionMode: "FIXTURE_ONLY";
  candidate: AirQualityTriggerCandidate | null;
  networkAttempted: false;
  detectorConfigurationMutated: false;
  airQualityEventDeclared: false;
  regulatoryComplianceDecided: false;
  healthAdviceIssued: false;
  policyEvaluated: false;
  reviewApproved: false;
  promotionAuthorized: false;
  releaseAuthorized: false;
  publicationAuthorized: false;
  publicUseAllowed: false;
}>;

export type AirQualityTriggerProjectionResult =
  | Readonly<{ ok: true; payload: GovernedAirQualityTriggerProjection }>
  | Readonly<{
      ok: false;
      code: "MALFORMED_AIR_QUALITY_TRIGGER_PROJECTION";
    }>;

const TOP_LEVEL_FIELDS = new Set([
  "profile",
  "panel_id",
  "outcome",
  "reason_code",
  "status",
  "execution_mode",
  "candidate",
  "network_attempted",
  "detector_configuration_mutated",
  "air_quality_event_declared",
  "regulatory_compliance_decided",
  "health_advice_issued",
  "policy_evaluated",
  "review_approved",
  "promotion_authorized",
  "release_authorized",
  "publication_authorized",
  "public_use_allowed",
]);
const CANDIDATE_FIELDS = new Set([
  "assessment_ref",
  "candidate_state",
  "observation_ref",
  "trailing_median_ref",
  "observed_at",
  "knowledge_character",
  "threshold_relation",
  "trailing_median_relation",
  "evidence_state",
  "evidence_refs",
]);
const OUTCOMES = new Set<AirQualityPanelOutcome>([
  "ANSWER",
  "ABSTAIN",
  "DENY",
  "ERROR",
]);
const REASON_CODES = new Set<AirQualityPanelReasonCode>([
  "TRIGGER_CANDIDATE_AVAILABLE",
  "NO_TRIGGER_CANDIDATE",
  "CONTEXT_HELD",
  "POLICY_DENIED",
  "UPSTREAM_ERROR",
]);
const THRESHOLD_RELATIONS = new Set<AirQualityThresholdRelation>([
  "ABOVE_MONITORED_THRESHOLD",
  "AT_OR_BELOW_MONITORED_THRESHOLD",
]);
const MEDIAN_RELATIONS = new Set<AirQualityMedianRelation>([
  "ABOVE_TRAILING_MEDIAN",
  "AT_OR_BELOW_TRAILING_MEDIAN",
]);
const PANEL_ID =
  /^kfm:air-quality-trigger-panel:[A-Za-z0-9][A-Za-z0-9:._~+/-]{2,240}$/;
const DIGEST_BOUND_REFERENCE =
  /^kfm:\/\/[A-Za-z0-9][A-Za-z0-9._~:/+-]{2,220}@sha256:[a-f0-9]{64}$/;
const UTC_SECOND = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$/;
const CONTROL_CHARACTER = /[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/;

function malformed(): AirQualityTriggerProjectionResult {
  return Object.freeze({
    ok: false,
    code: "MALFORMED_AIR_QUALITY_TRIGGER_PROJECTION",
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

function isDigestBoundReference(value: unknown): value is string {
  return (
    typeof value === "string" &&
    value.length <= 320 &&
    DIGEST_BOUND_REFERENCE.test(value) &&
    !CONTROL_CHARACTER.test(value)
  );
}

function isUtcSecond(value: unknown): value is string {
  if (typeof value !== "string" || !UTC_SECOND.test(value)) return false;
  const milliseconds = Date.parse(value);
  return (
    Number.isFinite(milliseconds) &&
    new Date(milliseconds).toISOString().replace(".000Z", "Z") === value
  );
}

function parseCandidate(
  input: unknown,
  reasonCode: "TRIGGER_CANDIDATE_AVAILABLE" | "NO_TRIGGER_CANDIDATE",
): AirQualityTriggerCandidate | null {
  if (!isRecord(input) || !hasExactFields(input, CANDIDATE_FIELDS)) return null;
  if (
    !isDigestBoundReference(input.assessment_ref) ||
    !isDigestBoundReference(input.observation_ref) ||
    !isDigestBoundReference(input.trailing_median_ref) ||
    !isUtcSecond(input.observed_at) ||
    input.knowledge_character !== "OBSERVED_SENSOR" ||
    typeof input.threshold_relation !== "string" ||
    !THRESHOLD_RELATIONS.has(input.threshold_relation as AirQualityThresholdRelation) ||
    typeof input.trailing_median_relation !== "string" ||
    !MEDIAN_RELATIONS.has(input.trailing_median_relation as AirQualityMedianRelation) ||
    input.evidence_state !== "REFERENCED_NOT_RESOLVED" ||
    !Array.isArray(input.evidence_refs) ||
    input.evidence_refs.length < 2 ||
    input.evidence_refs.length > 8 ||
    !input.evidence_refs.every(
      (reference) =>
        isDigestBoundReference(reference) &&
        reference.startsWith("kfm://evidence-ref/"),
    ) ||
    new Set(input.evidence_refs).size !== input.evidence_refs.length
  ) {
    return null;
  }
  const identityRefs = [
    input.assessment_ref,
    input.observation_ref,
    input.trailing_median_ref,
    ...input.evidence_refs,
  ];
  if (new Set(identityRefs).size !== identityRefs.length) return null;

  const trigger = reasonCode === "TRIGGER_CANDIDATE_AVAILABLE";
  const expectedState: AirQualityCandidateState = trigger
    ? "PROPOSED_TRIGGER_CANDIDATE"
    : "NO_TRIGGER_CANDIDATE";
  const aboveBoth =
    input.threshold_relation === "ABOVE_MONITORED_THRESHOLD" &&
    input.trailing_median_relation === "ABOVE_TRAILING_MEDIAN";
  if (
    input.candidate_state !== expectedState ||
    (trigger && !aboveBoth) ||
    (!trigger && aboveBoth)
  ) {
    return null;
  }
  return Object.freeze({
    assessmentRef: input.assessment_ref,
    candidateState: expectedState,
    observationRef: input.observation_ref,
    trailingMedianRef: input.trailing_median_ref,
    observedAt: input.observed_at,
    knowledgeCharacter: "OBSERVED_SENSOR",
    thresholdRelation: input.threshold_relation as AirQualityThresholdRelation,
    trailingMedianRelation: input.trailing_median_relation as AirQualityMedianRelation,
    evidenceState: "REFERENCED_NOT_RESOLVED",
    evidenceRefs: Object.freeze([...input.evidence_refs] as string[]),
  });
}

/** Parse one exact, fixture-only air-quality trigger display projection. */
export function parseAirQualityTriggerProjection(
  input: unknown,
): AirQualityTriggerProjectionResult {
  if (!isRecord(input) || !hasExactFields(input, TOP_LEVEL_FIELDS)) {
    return malformed();
  }
  if (
    input.profile !== AIR_QUALITY_TRIGGER_PROJECTION_PROFILE ||
    typeof input.panel_id !== "string" ||
    !PANEL_ID.test(input.panel_id) ||
    typeof input.outcome !== "string" ||
    !OUTCOMES.has(input.outcome as AirQualityPanelOutcome) ||
    typeof input.reason_code !== "string" ||
    !REASON_CODES.has(input.reason_code as AirQualityPanelReasonCode) ||
    input.status !== "PROPOSED_INACTIVE" ||
    input.execution_mode !== "FIXTURE_ONLY" ||
    input.network_attempted !== false ||
    input.detector_configuration_mutated !== false ||
    input.air_quality_event_declared !== false ||
    input.regulatory_compliance_decided !== false ||
    input.health_advice_issued !== false ||
    input.policy_evaluated !== false ||
    input.review_approved !== false ||
    input.promotion_authorized !== false ||
    input.release_authorized !== false ||
    input.publication_authorized !== false ||
    input.public_use_allowed !== false
  ) {
    return malformed();
  }
  const outcome = input.outcome as AirQualityPanelOutcome;
  const reasonCode = input.reason_code as AirQualityPanelReasonCode;
  const outcomeMatchesReason =
    (outcome === "ANSWER" &&
      (reasonCode === "TRIGGER_CANDIDATE_AVAILABLE" ||
        reasonCode === "NO_TRIGGER_CANDIDATE")) ||
    (outcome === "ABSTAIN" && reasonCode === "CONTEXT_HELD") ||
    (outcome === "DENY" && reasonCode === "POLICY_DENIED") ||
    (outcome === "ERROR" && reasonCode === "UPSTREAM_ERROR");
  if (!outcomeMatchesReason) return malformed();

  let candidate: AirQualityTriggerCandidate | null = null;
  if (
    outcome === "ANSWER" &&
    (reasonCode === "TRIGGER_CANDIDATE_AVAILABLE" ||
      reasonCode === "NO_TRIGGER_CANDIDATE")
  ) {
    candidate = parseCandidate(input.candidate, reasonCode);
    if (candidate === null) return malformed();
  } else if (input.candidate !== null) {
    return malformed();
  }

  return Object.freeze({
    ok: true,
    payload: Object.freeze({
      profile: AIR_QUALITY_TRIGGER_PROJECTION_PROFILE,
      panelId: input.panel_id,
      outcome,
      reasonCode,
      status: "PROPOSED_INACTIVE",
      executionMode: "FIXTURE_ONLY",
      candidate,
      networkAttempted: false,
      detectorConfigurationMutated: false,
      airQualityEventDeclared: false,
      regulatoryComplianceDecided: false,
      healthAdviceIssued: false,
      policyEvaluated: false,
      reviewApproved: false,
      promotionAuthorized: false,
      releaseAuthorized: false,
      publicationAuthorized: false,
      publicUseAllowed: false,
    }),
  });
}
