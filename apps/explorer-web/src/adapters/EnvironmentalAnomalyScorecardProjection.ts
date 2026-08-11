/**
 * Strict fixture-only projection for Pass 32 environmental anomaly scorecards.
 * The adapter validates a pre-governed display packet; it never computes an
 * anomaly, probes a source, or interprets environmental conditions.
 */

export const ENVIRONMENTAL_ANOMALY_SCORECARD_PROJECTION_PROFILE =
  "kfm.explorer.environmental-anomaly-scorecard.fixture.v1" as const;

export type EnvironmentalScorecardOutcome =
  | "ANSWER"
  | "ABSTAIN"
  | "DENY"
  | "ERROR";
export type EnvironmentalScorecardReasonCode =
  | "SCORECARD_AVAILABLE"
  | "SCORECARD_MISSING"
  | "POLICY_DENIED"
  | "UPSTREAM_ERROR";
export type EnvironmentalScorecardLaneName =
  | "AIR"
  | "BIODIVERSITY"
  | "HYDROLOGY"
  | "SOILS"
  | "VEGETATION";
export type EnvironmentalFreshnessState =
  | "CURRENT"
  | "STALE"
  | "MISSING"
  | "UNKNOWN";
export type EnvironmentalCandidateState =
  | "NONE"
  | "PROPOSED"
  | "HOLD"
  | "ERROR";
export type EnvironmentalScorecardStatus = "COMPLETE" | "HOLD";

export type EnvironmentalScorecardScope = Readonly<{
  scopeRef: string;
  stateCode: "KS";
  geometryRef: string;
}>;

export type EnvironmentalScorecardLane = Readonly<{
  lane: EnvironmentalScorecardLaneName;
  freshnessState: EnvironmentalFreshnessState;
  candidateState: EnvironmentalCandidateState;
  reasonCode:
    | "NO_ANOMALY_CANDIDATE"
    | "ANOMALY_CANDIDATE_PROPOSED"
    | "FRESHNESS_HOLD"
    | "UPSTREAM_ERROR";
  sourceHealthAssessmentRef: string;
  evidenceRef: string | null;
  candidateRef: string | null;
}>;

export type EnvironmentalScorecardSummary = Readonly<{
  laneCount: 5;
  currentCount: number;
  candidateCount: number;
  holdCount: number;
  errorCount: number;
  overallOutcome: EnvironmentalScorecardStatus;
  separateInterpretationGateRequired: true;
}>;

export type GovernedEnvironmentalAnomalyScorecardProjection = Readonly<{
  profile: typeof ENVIRONMENTAL_ANOMALY_SCORECARD_PROJECTION_PROFILE;
  scorecardId: string;
  outcome: EnvironmentalScorecardOutcome;
  reasonCode: EnvironmentalScorecardReasonCode;
  status: "PROPOSED_INACTIVE";
  executionMode: "FIXTURE_ONLY";
  county: EnvironmentalScorecardScope | null;
  assessedAt: string | null;
  lanes: readonly EnvironmentalScorecardLane[];
  summary: EnvironmentalScorecardSummary | null;
  interpretationAuthorized: false;
  publicationAuthorized: false;
  publicUseAllowed: false;
}>;

export type EnvironmentalAnomalyScorecardProjectionResult =
  | Readonly<{
      ok: true;
      payload: GovernedEnvironmentalAnomalyScorecardProjection;
    }>
  | Readonly<{
      ok: false;
      code: "MALFORMED_ENVIRONMENTAL_ANOMALY_SCORECARD_PROJECTION";
    }>;

const TOP_LEVEL_FIELDS = new Set([
  "profile",
  "scorecard_id",
  "outcome",
  "reason_code",
  "status",
  "execution_mode",
  "county",
  "assessed_at",
  "lanes",
  "summary",
  "interpretation_authorized",
  "publication_authorized",
  "public_use_allowed",
]);
const COUNTY_FIELDS = new Set(["scope_ref", "state_code", "geometry_ref"]);
const LANE_FIELDS = new Set([
  "lane",
  "freshness_state",
  "candidate_state",
  "reason_code",
  "source_health_assessment_ref",
  "evidence_ref",
  "candidate_ref",
]);
const SUMMARY_FIELDS = new Set([
  "lane_count",
  "current_count",
  "candidate_count",
  "hold_count",
  "error_count",
  "overall_outcome",
  "separate_interpretation_gate_required",
]);
const OUTCOMES = new Set<EnvironmentalScorecardOutcome>([
  "ANSWER",
  "ABSTAIN",
  "DENY",
  "ERROR",
]);
const REASON_CODES = new Set<EnvironmentalScorecardReasonCode>([
  "SCORECARD_AVAILABLE",
  "SCORECARD_MISSING",
  "POLICY_DENIED",
  "UPSTREAM_ERROR",
]);
const EXPECTED_REASON: Readonly<
  Record<EnvironmentalScorecardOutcome, EnvironmentalScorecardReasonCode>
> = Object.freeze({
  ANSWER: "SCORECARD_AVAILABLE",
  ABSTAIN: "SCORECARD_MISSING",
  DENY: "POLICY_DENIED",
  ERROR: "UPSTREAM_ERROR",
});
const LANE_NAMES: readonly EnvironmentalScorecardLaneName[] = Object.freeze([
  "AIR",
  "BIODIVERSITY",
  "HYDROLOGY",
  "SOILS",
  "VEGETATION",
]);
const FRESHNESS_STATES = new Set<EnvironmentalFreshnessState>([
  "CURRENT",
  "STALE",
  "MISSING",
  "UNKNOWN",
]);
const CANDIDATE_STATES = new Set<EnvironmentalCandidateState>([
  "NONE",
  "PROPOSED",
  "HOLD",
  "ERROR",
]);
const SCORECARD_ID =
  /^kfm:environmental-anomaly-scorecard:[A-Za-z0-9][A-Za-z0-9:._~+/-]{2,250}$/;
const KFM_REFERENCE = /^kfm:(?:\/\/)?[A-Za-z0-9][A-Za-z0-9._~:/+-]{2,315}$/;
const UTC_SECOND = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$/;
const CONTROL_CHARACTER = /[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/;

function malformed(): EnvironmentalAnomalyScorecardProjectionResult {
  return Object.freeze({
    ok: false,
    code: "MALFORMED_ENVIRONMENTAL_ANOMALY_SCORECARD_PROJECTION",
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

function isReference(value: unknown): value is string {
  return (
    typeof value === "string" &&
    value.length <= 320 &&
    KFM_REFERENCE.test(value) &&
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

function parseCounty(input: unknown): EnvironmentalScorecardScope | null {
  if (!isRecord(input) || !hasExactFields(input, COUNTY_FIELDS)) return null;
  if (
    !isReference(input.scope_ref) ||
    !input.scope_ref.startsWith("kfm://scope/county/") ||
    input.state_code !== "KS" ||
    !isReference(input.geometry_ref) ||
    !input.geometry_ref.startsWith("kfm://geometry/county/")
  ) {
    return null;
  }
  return Object.freeze({
    scopeRef: input.scope_ref,
    stateCode: "KS",
    geometryRef: input.geometry_ref,
  });
}

function parseLane(input: unknown): EnvironmentalScorecardLane | null {
  if (!isRecord(input) || !hasExactFields(input, LANE_FIELDS)) return null;
  if (
    typeof input.lane !== "string" ||
    !LANE_NAMES.includes(input.lane as EnvironmentalScorecardLaneName) ||
    typeof input.freshness_state !== "string" ||
    !FRESHNESS_STATES.has(
      input.freshness_state as EnvironmentalFreshnessState,
    ) ||
    typeof input.candidate_state !== "string" ||
    !CANDIDATE_STATES.has(
      input.candidate_state as EnvironmentalCandidateState,
    ) ||
    typeof input.reason_code !== "string" ||
    !isReference(input.source_health_assessment_ref) ||
    !input.source_health_assessment_ref.startsWith("kfm:source-health:")
  ) {
    return null;
  }

  const freshness = input.freshness_state as EnvironmentalFreshnessState;
  const candidate = input.candidate_state as EnvironmentalCandidateState;
  const evidence = input.evidence_ref;
  const candidateRef = input.candidate_ref;
  if (
    candidate === "NONE" &&
    !(
      freshness === "CURRENT" &&
      input.reason_code === "NO_ANOMALY_CANDIDATE" &&
      isReference(evidence) &&
      evidence.startsWith("kfm://evidence/") &&
      candidateRef === null
    )
  ) {
    return null;
  }
  if (
    candidate === "PROPOSED" &&
    !(
      freshness === "CURRENT" &&
      input.reason_code === "ANOMALY_CANDIDATE_PROPOSED" &&
      isReference(evidence) &&
      evidence.startsWith("kfm://evidence/") &&
      isReference(candidateRef) &&
      candidateRef.startsWith("kfm:anomaly-candidate:")
    )
  ) {
    return null;
  }
  if (
    candidate === "HOLD" &&
    !(
      freshness !== "CURRENT" &&
      input.reason_code === "FRESHNESS_HOLD" &&
      evidence === null &&
      candidateRef === null
    )
  ) {
    return null;
  }
  if (
    candidate === "ERROR" &&
    !(
      freshness === "UNKNOWN" &&
      input.reason_code === "UPSTREAM_ERROR" &&
      evidence === null &&
      candidateRef === null
    )
  ) {
    return null;
  }

  return Object.freeze({
    lane: input.lane as EnvironmentalScorecardLaneName,
    freshnessState: freshness,
    candidateState: candidate,
    reasonCode: input.reason_code as EnvironmentalScorecardLane["reasonCode"],
    sourceHealthAssessmentRef: input.source_health_assessment_ref,
    evidenceRef: evidence as string | null,
    candidateRef: candidateRef as string | null,
  });
}

function parseLanes(input: unknown): readonly EnvironmentalScorecardLane[] | null {
  if (!Array.isArray(input) || input.length !== LANE_NAMES.length) return null;
  const lanes: EnvironmentalScorecardLane[] = [];
  const healthRefs = new Set<string>();
  const evidenceRefs = new Set<string>();
  const candidateRefs = new Set<string>();
  for (let index = 0; index < LANE_NAMES.length; index += 1) {
    const lane = parseLane(input[index]);
    if (
      lane === null ||
      lane.lane !== LANE_NAMES[index] ||
      healthRefs.has(lane.sourceHealthAssessmentRef) ||
      (lane.evidenceRef !== null && evidenceRefs.has(lane.evidenceRef)) ||
      (lane.candidateRef !== null && candidateRefs.has(lane.candidateRef))
    ) {
      return null;
    }
    healthRefs.add(lane.sourceHealthAssessmentRef);
    if (lane.evidenceRef !== null) evidenceRefs.add(lane.evidenceRef);
    if (lane.candidateRef !== null) candidateRefs.add(lane.candidateRef);
    lanes.push(lane);
  }
  return Object.freeze(lanes);
}

function parseSummary(
  input: unknown,
  lanes: readonly EnvironmentalScorecardLane[],
): EnvironmentalScorecardSummary | null {
  if (!isRecord(input) || !hasExactFields(input, SUMMARY_FIELDS)) return null;
  const current = lanes.filter(
    (lane) => lane.freshnessState === "CURRENT",
  ).length;
  const candidates = lanes.filter(
    (lane) => lane.candidateState === "PROPOSED",
  ).length;
  const holds = lanes.filter((lane) => lane.candidateState === "HOLD").length;
  const errors = lanes.filter((lane) => lane.candidateState === "ERROR").length;
  const overall: EnvironmentalScorecardStatus =
    current === 5 && holds === 0 && errors === 0 ? "COMPLETE" : "HOLD";
  if (
    input.lane_count !== 5 ||
    input.current_count !== current ||
    input.candidate_count !== candidates ||
    input.hold_count !== holds ||
    input.error_count !== errors ||
    input.overall_outcome !== overall ||
    input.separate_interpretation_gate_required !== true
  ) {
    return null;
  }
  return Object.freeze({
    laneCount: 5,
    currentCount: current,
    candidateCount: candidates,
    holdCount: holds,
    errorCount: errors,
    overallOutcome: overall,
    separateInterpretationGateRequired: true,
  });
}

/** Parse one exact, fixture-only environmental anomaly scorecard projection. */
export function parseEnvironmentalAnomalyScorecardProjection(
  input: unknown,
): EnvironmentalAnomalyScorecardProjectionResult {
  if (!isRecord(input) || !hasExactFields(input, TOP_LEVEL_FIELDS)) {
    return malformed();
  }
  if (
    input.profile !== ENVIRONMENTAL_ANOMALY_SCORECARD_PROJECTION_PROFILE ||
    typeof input.scorecard_id !== "string" ||
    !SCORECARD_ID.test(input.scorecard_id) ||
    typeof input.outcome !== "string" ||
    !OUTCOMES.has(input.outcome as EnvironmentalScorecardOutcome) ||
    typeof input.reason_code !== "string" ||
    !REASON_CODES.has(input.reason_code as EnvironmentalScorecardReasonCode) ||
    input.status !== "PROPOSED_INACTIVE" ||
    input.execution_mode !== "FIXTURE_ONLY" ||
    input.interpretation_authorized !== false ||
    input.publication_authorized !== false ||
    input.public_use_allowed !== false
  ) {
    return malformed();
  }

  const outcome = input.outcome as EnvironmentalScorecardOutcome;
  const reasonCode = input.reason_code as EnvironmentalScorecardReasonCode;
  if (EXPECTED_REASON[outcome] !== reasonCode) return malformed();

  let county: EnvironmentalScorecardScope | null = null;
  let assessedAt: string | null = null;
  let lanes: readonly EnvironmentalScorecardLane[] = Object.freeze([]);
  let summary: EnvironmentalScorecardSummary | null = null;
  if (outcome === "ANSWER") {
    county = parseCounty(input.county);
    if (county === null || !isUtcSecond(input.assessed_at)) return malformed();
    assessedAt = input.assessed_at;
    const parsedLanes = parseLanes(input.lanes);
    if (parsedLanes === null) return malformed();
    lanes = parsedLanes;
    summary = parseSummary(input.summary, lanes);
    if (summary === null) return malformed();
  } else if (
    input.county !== null ||
    input.assessed_at !== null ||
    !Array.isArray(input.lanes) ||
    input.lanes.length !== 0 ||
    input.summary !== null
  ) {
    return malformed();
  }

  return Object.freeze({
    ok: true,
    payload: Object.freeze({
      profile: ENVIRONMENTAL_ANOMALY_SCORECARD_PROJECTION_PROFILE,
      scorecardId: input.scorecard_id,
      outcome,
      reasonCode,
      status: "PROPOSED_INACTIVE",
      executionMode: "FIXTURE_ONLY",
      county,
      assessedAt,
      lanes,
      summary,
      interpretationAuthorized: false,
      publicationAuthorized: false,
      publicUseAllowed: false,
    }),
  });
}
