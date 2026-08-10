/**
 * Strict fixture-only projection for the Pass 32 county environmental
 * cadence calendar. The adapter validates a pre-governed display packet; it
 * never probes sources, authors source health, or interprets conditions.
 */

export const COUNTY_ENVIRONMENTAL_CADENCE_PROJECTION_PROFILE =
  "kfm.explorer.county-environmental-cadence.fixture.v1" as const;

export type CountyCadenceOutcome = "ANSWER" | "ABSTAIN" | "DENY" | "ERROR";
export type CountyCadenceReasonCode =
  | "CALENDAR_AVAILABLE"
  | "CALENDAR_MISSING"
  | "POLICY_DENIED"
  | "UPSTREAM_ERROR";
export type CountyCadenceLaneName =
  | "AIR"
  | "BIODIVERSITY"
  | "HYDROLOGY"
  | "IMAGERY"
  | "SOILS"
  | "VEGETATION";
export type CountyCadenceHealth =
  | "HEALTHY"
  | "DEGRADED"
  | "STALE"
  | "UNAVAILABLE"
  | "UNKNOWN";
export type CountyCadenceCheckResult = "RECORDED" | "MISSED";
export type CountyCadenceStatus = "COMPLETE" | "HOLD";

export type CountyCadenceScope = Readonly<{
  scopeRef: string;
  stateCode: "KS";
  geometryRef: string;
}>;

export type CountyCadenceWeek = Readonly<{
  periodStart: string;
  periodEnd: string;
  assessedAt: string;
  cadenceHours: 168;
}>;

export type CountyCadenceLane = Readonly<{
  lane: CountyCadenceLaneName;
  sourceDescriptorRef: string;
  sourceHealthAssessmentRef: string;
  checkedAt: string | null;
  healthOutcome: CountyCadenceHealth;
  checkResult: CountyCadenceCheckResult;
  reasonCode:
    | "HEALTHY_WITHIN_WEEK"
    | "SOURCE_DEGRADED"
    | "SOURCE_STALE"
    | "SOURCE_UNAVAILABLE"
    | "CHECK_MISSING";
}>;

export type CountyCadenceSummary = Readonly<{
  laneCount: 6;
  recordedCount: number;
  holdCount: number;
  errorCount: 0;
  overallOutcome: CountyCadenceStatus;
  separateInterpretationGateRequired: true;
}>;

export type GovernedCountyEnvironmentalCadenceProjection = Readonly<{
  profile: typeof COUNTY_ENVIRONMENTAL_CADENCE_PROJECTION_PROFILE;
  calendarId: string;
  outcome: CountyCadenceOutcome;
  reasonCode: CountyCadenceReasonCode;
  status: "PROPOSED_INACTIVE";
  executionMode: "FIXTURE_ONLY";
  county: CountyCadenceScope | null;
  week: CountyCadenceWeek | null;
  sourceAvailabilityWatchlistRef: string | null;
  lanes: readonly CountyCadenceLane[];
  summary: CountyCadenceSummary | null;
  interpretationAuthorized: false;
  publicationAuthorized: false;
  publicUseAllowed: false;
}>;

export type CountyEnvironmentalCadenceProjectionResult =
  | Readonly<{
      ok: true;
      payload: GovernedCountyEnvironmentalCadenceProjection;
    }>
  | Readonly<{
      ok: false;
      code: "MALFORMED_COUNTY_ENVIRONMENTAL_CADENCE_PROJECTION";
    }>;

const TOP_LEVEL_FIELDS = new Set([
  "profile",
  "calendar_id",
  "outcome",
  "reason_code",
  "status",
  "execution_mode",
  "county",
  "week",
  "source_availability_watchlist_ref",
  "lanes",
  "summary",
  "interpretation_authorized",
  "publication_authorized",
  "public_use_allowed",
]);
const COUNTY_FIELDS = new Set(["scope_ref", "state_code", "geometry_ref"]);
const WEEK_FIELDS = new Set([
  "period_start",
  "period_end",
  "assessed_at",
  "cadence_hours",
]);
const LANE_FIELDS = new Set([
  "lane",
  "source_descriptor_ref",
  "source_health_assessment_ref",
  "checked_at",
  "health_outcome",
  "check_result",
  "reason_code",
]);
const SUMMARY_FIELDS = new Set([
  "lane_count",
  "recorded_count",
  "hold_count",
  "error_count",
  "overall_outcome",
  "separate_interpretation_gate_required",
]);
const OUTCOMES = new Set<CountyCadenceOutcome>([
  "ANSWER",
  "ABSTAIN",
  "DENY",
  "ERROR",
]);
const REASON_CODES = new Set<CountyCadenceReasonCode>([
  "CALENDAR_AVAILABLE",
  "CALENDAR_MISSING",
  "POLICY_DENIED",
  "UPSTREAM_ERROR",
]);
const EXPECTED_REASON: Readonly<
  Record<CountyCadenceOutcome, CountyCadenceReasonCode>
> = Object.freeze({
  ANSWER: "CALENDAR_AVAILABLE",
  ABSTAIN: "CALENDAR_MISSING",
  DENY: "POLICY_DENIED",
  ERROR: "UPSTREAM_ERROR",
});
const LANE_NAMES: readonly CountyCadenceLaneName[] = Object.freeze([
  "AIR",
  "BIODIVERSITY",
  "HYDROLOGY",
  "IMAGERY",
  "SOILS",
  "VEGETATION",
]);
const HEALTH_REASON = Object.freeze({
  HEALTHY: "HEALTHY_WITHIN_WEEK",
  DEGRADED: "SOURCE_DEGRADED",
  STALE: "SOURCE_STALE",
  UNAVAILABLE: "SOURCE_UNAVAILABLE",
} as const);
const HEALTH_OUTCOMES = new Set<CountyCadenceHealth>([
  "HEALTHY",
  "DEGRADED",
  "STALE",
  "UNAVAILABLE",
  "UNKNOWN",
]);
const CHECK_RESULTS = new Set<CountyCadenceCheckResult>(["RECORDED", "MISSED"]);
const CALENDAR_ID =
  /^kfm:county-environmental-cadence:[A-Za-z0-9][A-Za-z0-9:._~+/-]{2,250}$/;
const KFM_REFERENCE = /^kfm:(?:\/\/)?[A-Za-z0-9][A-Za-z0-9._~:/+-]{2,315}$/;
const UTC_SECOND = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$/;
const CONTROL_CHARACTER = /[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/;
const WEEK_MILLISECONDS = 168 * 60 * 60 * 1000;

function malformed(): CountyEnvironmentalCadenceProjectionResult {
  return Object.freeze({
    ok: false,
    code: "MALFORMED_COUNTY_ENVIRONMENTAL_CADENCE_PROJECTION",
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

function parseCounty(input: unknown): CountyCadenceScope | null {
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

function parseWeek(input: unknown): CountyCadenceWeek | null {
  if (!isRecord(input) || !hasExactFields(input, WEEK_FIELDS)) return null;
  if (
    !isUtcSecond(input.period_start) ||
    !isUtcSecond(input.period_end) ||
    !isUtcSecond(input.assessed_at) ||
    input.cadence_hours !== 168
  ) {
    return null;
  }
  const start = Date.parse(input.period_start);
  const end = Date.parse(input.period_end);
  const assessed = Date.parse(input.assessed_at);
  if (end - start !== WEEK_MILLISECONDS || assessed < end) return null;
  return Object.freeze({
    periodStart: input.period_start,
    periodEnd: input.period_end,
    assessedAt: input.assessed_at,
    cadenceHours: 168,
  });
}

function parseLane(
  input: unknown,
  week: CountyCadenceWeek,
): CountyCadenceLane | null {
  if (!isRecord(input) || !hasExactFields(input, LANE_FIELDS)) return null;
  if (
    typeof input.lane !== "string" ||
    !LANE_NAMES.includes(input.lane as CountyCadenceLaneName) ||
    !isReference(input.source_descriptor_ref) ||
    !input.source_descriptor_ref.startsWith("kfm://source/") ||
    !isReference(input.source_health_assessment_ref) ||
    !input.source_health_assessment_ref.startsWith("kfm:source-health:") ||
    typeof input.health_outcome !== "string" ||
    !HEALTH_OUTCOMES.has(input.health_outcome as CountyCadenceHealth) ||
    typeof input.check_result !== "string" ||
    !CHECK_RESULTS.has(input.check_result as CountyCadenceCheckResult) ||
    typeof input.reason_code !== "string"
  ) {
    return null;
  }

  const health = input.health_outcome as CountyCadenceHealth;
  const result = input.check_result as CountyCadenceCheckResult;
  let checkedAt: string | null;
  if (result === "MISSED") {
    if (
      input.checked_at !== null ||
      health !== "UNKNOWN" ||
      input.reason_code !== "CHECK_MISSING"
    ) {
      return null;
    }
    checkedAt = null;
  } else {
    if (
      !isUtcSecond(input.checked_at) ||
      health === "UNKNOWN" ||
      input.reason_code !== HEALTH_REASON[health]
    ) {
      return null;
    }
    const checked = Date.parse(input.checked_at);
    if (checked < Date.parse(week.periodStart) || checked > Date.parse(week.periodEnd)) {
      return null;
    }
    checkedAt = input.checked_at;
  }

  return Object.freeze({
    lane: input.lane as CountyCadenceLaneName,
    sourceDescriptorRef: input.source_descriptor_ref,
    sourceHealthAssessmentRef: input.source_health_assessment_ref,
    checkedAt,
    healthOutcome: health,
    checkResult: result,
    reasonCode: input.reason_code as CountyCadenceLane["reasonCode"],
  });
}

function parseLanes(
  input: unknown,
  week: CountyCadenceWeek,
): readonly CountyCadenceLane[] | null {
  if (!Array.isArray(input) || input.length !== LANE_NAMES.length) return null;
  const lanes: CountyCadenceLane[] = [];
  const sourceRefs = new Set<string>();
  const healthRefs = new Set<string>();
  for (let index = 0; index < LANE_NAMES.length; index += 1) {
    const lane = parseLane(input[index], week);
    if (
      lane === null ||
      lane.lane !== LANE_NAMES[index] ||
      sourceRefs.has(lane.sourceDescriptorRef) ||
      healthRefs.has(lane.sourceHealthAssessmentRef)
    ) {
      return null;
    }
    sourceRefs.add(lane.sourceDescriptorRef);
    healthRefs.add(lane.sourceHealthAssessmentRef);
    lanes.push(lane);
  }
  return Object.freeze(lanes);
}

function parseSummary(
  input: unknown,
  lanes: readonly CountyCadenceLane[],
): CountyCadenceSummary | null {
  if (!isRecord(input) || !hasExactFields(input, SUMMARY_FIELDS)) return null;
  const recorded = lanes.filter((lane) => lane.checkResult === "RECORDED").length;
  const holds = lanes.filter(
    (lane) => lane.checkResult === "MISSED" || lane.healthOutcome !== "HEALTHY",
  ).length;
  const overall: CountyCadenceStatus = holds === 0 ? "COMPLETE" : "HOLD";
  if (
    input.lane_count !== 6 ||
    input.recorded_count !== recorded ||
    input.hold_count !== holds ||
    input.error_count !== 0 ||
    input.overall_outcome !== overall ||
    input.separate_interpretation_gate_required !== true
  ) {
    return null;
  }
  return Object.freeze({
    laneCount: 6,
    recordedCount: recorded,
    holdCount: holds,
    errorCount: 0,
    overallOutcome: overall,
    separateInterpretationGateRequired: true,
  });
}

/** Parse one exact, fixture-only county cadence display projection. */
export function parseCountyEnvironmentalCadenceProjection(
  input: unknown,
): CountyEnvironmentalCadenceProjectionResult {
  if (!isRecord(input) || !hasExactFields(input, TOP_LEVEL_FIELDS)) {
    return malformed();
  }
  if (
    input.profile !== COUNTY_ENVIRONMENTAL_CADENCE_PROJECTION_PROFILE ||
    typeof input.calendar_id !== "string" ||
    !CALENDAR_ID.test(input.calendar_id) ||
    typeof input.outcome !== "string" ||
    !OUTCOMES.has(input.outcome as CountyCadenceOutcome) ||
    typeof input.reason_code !== "string" ||
    !REASON_CODES.has(input.reason_code as CountyCadenceReasonCode) ||
    input.status !== "PROPOSED_INACTIVE" ||
    input.execution_mode !== "FIXTURE_ONLY" ||
    input.interpretation_authorized !== false ||
    input.publication_authorized !== false ||
    input.public_use_allowed !== false
  ) {
    return malformed();
  }

  const outcome = input.outcome as CountyCadenceOutcome;
  const reasonCode = input.reason_code as CountyCadenceReasonCode;
  if (EXPECTED_REASON[outcome] !== reasonCode) return malformed();

  let county: CountyCadenceScope | null = null;
  let week: CountyCadenceWeek | null = null;
  let watchlistRef: string | null = null;
  let lanes: readonly CountyCadenceLane[] = Object.freeze([]);
  let summary: CountyCadenceSummary | null = null;
  if (outcome === "ANSWER") {
    county = parseCounty(input.county);
    week = parseWeek(input.week);
    if (
      county === null ||
      week === null ||
      !isReference(input.source_availability_watchlist_ref) ||
      !input.source_availability_watchlist_ref.startsWith(
        "kfm:source-availability-watchlist:",
      )
    ) {
      return malformed();
    }
    watchlistRef = input.source_availability_watchlist_ref;
    const parsedLanes = parseLanes(input.lanes, week);
    if (parsedLanes === null) return malformed();
    lanes = parsedLanes;
    summary = parseSummary(input.summary, lanes);
    if (summary === null) return malformed();
  } else if (
    input.county !== null ||
    input.week !== null ||
    input.source_availability_watchlist_ref !== null ||
    !Array.isArray(input.lanes) ||
    input.lanes.length !== 0 ||
    input.summary !== null
  ) {
    return malformed();
  }

  return Object.freeze({
    ok: true,
    payload: Object.freeze({
      profile: COUNTY_ENVIRONMENTAL_CADENCE_PROJECTION_PROFILE,
      calendarId: input.calendar_id,
      outcome,
      reasonCode,
      status: "PROPOSED_INACTIVE",
      executionMode: "FIXTURE_ONLY",
      county,
      week,
      sourceAvailabilityWatchlistRef: watchlistRef,
      lanes,
      summary,
      interpretationAuthorized: false,
      publicationAuthorized: false,
      publicUseAllowed: false,
    }),
  });
}
