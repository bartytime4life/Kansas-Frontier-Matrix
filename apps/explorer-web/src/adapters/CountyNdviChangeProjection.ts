/**
 * Strict fixture-only projection for a county NDVI change panel.
 *
 * The browser validates a bounded display packet. It does not fetch imagery,
 * calculate NDVI, resolve evidence, interpret environmental conditions, or
 * acquire lifecycle, policy, promotion, release, or publication authority.
 */

export const COUNTY_NDVI_CHANGE_PROJECTION_PROFILE =
  "kfm.explorer.county-ndvi-change.fixture.v1" as const;

export type CountyNdviPanelOutcome = "ANSWER" | "ABSTAIN" | "DENY" | "ERROR";
export type CountyNdviPanelReasonCode =
  | "PANEL_AVAILABLE"
  | "PANEL_MISSING"
  | "POLICY_DENIED"
  | "UPSTREAM_ERROR";
export type CountyNdviClassification =
  | "GAIN_CANDIDATE"
  | "LOSS_CANDIDATE"
  | "STABLE";

export type CountyNdviScope = Readonly<{
  scopeRef: string;
  stateCode: "KS";
}>;

export type CountyNdviWindows = Readonly<{
  baselineStart: string;
  baselineEnd: string;
  recentStart: string;
  recentEnd: string;
}>;

export type CountyNdviMetrics = Readonly<{
  baselineMedianMillionths: number;
  recentMedianMillionths: number;
  deltaNdviMillionths: number;
  deltaThresholdMillionths: number;
  changedAreaBasisPoints: number;
  clusterCount: number;
  classification: CountyNdviClassification;
}>;

export type CountyNdviEvidence = Readonly<{
  state: "REFERENCED_NOT_RESOLVED";
  ndviComputationRef: string;
  connectivityAssessmentRef: string;
}>;

export type GovernedCountyNdviChangeProjection = Readonly<{
  profile: typeof COUNTY_NDVI_CHANGE_PROJECTION_PROFILE;
  panelId: string;
  outcome: CountyNdviPanelOutcome;
  reasonCode: CountyNdviPanelReasonCode;
  status: "PROPOSED_INACTIVE";
  executionMode: "FIXTURE_ONLY";
  county: CountyNdviScope | null;
  windows: CountyNdviWindows | null;
  metrics: CountyNdviMetrics | null;
  evidence: CountyNdviEvidence | null;
  networkAttempted: false;
  sourceActivated: false;
  interpretationAuthorized: false;
  promotionAuthorized: false;
  releaseAuthorized: false;
  publicationAuthorized: false;
  publicUseAllowed: false;
}>;

export type CountyNdviChangeProjectionResult =
  | Readonly<{ ok: true; payload: GovernedCountyNdviChangeProjection }>
  | Readonly<{
      ok: false;
      code: "MALFORMED_COUNTY_NDVI_CHANGE_PROJECTION";
    }>;

const TOP_LEVEL_FIELDS = new Set([
  "profile",
  "panel_id",
  "outcome",
  "reason_code",
  "status",
  "execution_mode",
  "county",
  "windows",
  "metrics",
  "evidence",
  "network_attempted",
  "source_activated",
  "interpretation_authorized",
  "promotion_authorized",
  "release_authorized",
  "publication_authorized",
  "public_use_allowed",
]);
const COUNTY_FIELDS = new Set(["scope_ref", "state_code"]);
const WINDOW_FIELDS = new Set([
  "baseline_start",
  "baseline_end",
  "recent_start",
  "recent_end",
]);
const METRIC_FIELDS = new Set([
  "baseline_median_millionths",
  "recent_median_millionths",
  "delta_ndvi_millionths",
  "delta_threshold_millionths",
  "changed_area_basis_points",
  "cluster_count",
  "classification",
]);
const EVIDENCE_FIELDS = new Set([
  "state",
  "ndvi_computation_ref",
  "connectivity_assessment_ref",
]);
const OUTCOMES = new Set<CountyNdviPanelOutcome>([
  "ANSWER",
  "ABSTAIN",
  "DENY",
  "ERROR",
]);
const REASON_CODES = new Set<CountyNdviPanelReasonCode>([
  "PANEL_AVAILABLE",
  "PANEL_MISSING",
  "POLICY_DENIED",
  "UPSTREAM_ERROR",
]);
const EXPECTED_REASON: Readonly<
  Record<CountyNdviPanelOutcome, CountyNdviPanelReasonCode>
> = Object.freeze({
  ANSWER: "PANEL_AVAILABLE",
  ABSTAIN: "PANEL_MISSING",
  DENY: "POLICY_DENIED",
  ERROR: "UPSTREAM_ERROR",
});
const CLASSIFICATIONS = new Set<CountyNdviClassification>([
  "GAIN_CANDIDATE",
  "LOSS_CANDIDATE",
  "STABLE",
]);
const PANEL_ID =
  /^kfm:county-ndvi-change-panel:[A-Za-z0-9][A-Za-z0-9:._~+/-]{2,240}$/;
const COUNTY_REF =
  /^kfm:\/\/scope\/county\/[A-Za-z0-9][A-Za-z0-9._~:+/-]{2,280}$/;
const DIGEST_BOUND_REFERENCE =
  /^kfm:\/\/[A-Za-z0-9][A-Za-z0-9._~:/+-]{2,220}@sha256:[a-f0-9]{64}$/;
const UTC_SECOND = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$/;
const CONTROL_CHARACTER = /[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/;

function malformed(): CountyNdviChangeProjectionResult {
  return Object.freeze({
    ok: false,
    code: "MALFORMED_COUNTY_NDVI_CHANGE_PROJECTION",
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

function isBoundedInteger(
  value: unknown,
  minimum: number,
  maximum: number,
): value is number {
  return Number.isInteger(value) && Number(value) >= minimum && Number(value) <= maximum;
}

function isUtcSecond(value: unknown): value is string {
  if (typeof value !== "string" || !UTC_SECOND.test(value)) return false;
  const milliseconds = Date.parse(value);
  return (
    Number.isFinite(milliseconds) &&
    new Date(milliseconds).toISOString().replace(".000Z", "Z") === value
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

function parseCounty(input: unknown): CountyNdviScope | null {
  if (!isRecord(input) || !hasExactFields(input, COUNTY_FIELDS)) return null;
  if (
    typeof input.scope_ref !== "string" ||
    !COUNTY_REF.test(input.scope_ref) ||
    CONTROL_CHARACTER.test(input.scope_ref) ||
    input.state_code !== "KS"
  ) {
    return null;
  }
  return Object.freeze({ scopeRef: input.scope_ref, stateCode: "KS" });
}

function parseWindows(input: unknown): CountyNdviWindows | null {
  if (!isRecord(input) || !hasExactFields(input, WINDOW_FIELDS)) return null;
  if (
    !isUtcSecond(input.baseline_start) ||
    !isUtcSecond(input.baseline_end) ||
    !isUtcSecond(input.recent_start) ||
    !isUtcSecond(input.recent_end)
  ) {
    return null;
  }
  const baselineStart = Date.parse(input.baseline_start);
  const baselineEnd = Date.parse(input.baseline_end);
  const recentStart = Date.parse(input.recent_start);
  const recentEnd = Date.parse(input.recent_end);
  if (
    baselineStart >= baselineEnd ||
    recentStart >= recentEnd ||
    baselineEnd > recentStart
  ) {
    return null;
  }
  return Object.freeze({
    baselineStart: input.baseline_start,
    baselineEnd: input.baseline_end,
    recentStart: input.recent_start,
    recentEnd: input.recent_end,
  });
}

function parseMetrics(input: unknown): CountyNdviMetrics | null {
  if (!isRecord(input) || !hasExactFields(input, METRIC_FIELDS)) return null;
  if (
    !isBoundedInteger(input.baseline_median_millionths, -1_000_000, 1_000_000) ||
    !isBoundedInteger(input.recent_median_millionths, -1_000_000, 1_000_000) ||
    !isBoundedInteger(input.delta_ndvi_millionths, -2_000_000, 2_000_000) ||
    !isBoundedInteger(input.delta_threshold_millionths, 1, 2_000_000) ||
    !isBoundedInteger(input.changed_area_basis_points, 0, 10_000) ||
    !isBoundedInteger(input.cluster_count, 0, 100_000) ||
    typeof input.classification !== "string" ||
    !CLASSIFICATIONS.has(input.classification as CountyNdviClassification)
  ) {
    return null;
  }
  const baseline = input.baseline_median_millionths;
  const recent = input.recent_median_millionths;
  const delta = input.delta_ndvi_millionths;
  const threshold = input.delta_threshold_millionths;
  const changedArea = input.changed_area_basis_points;
  const clusters = input.cluster_count;
  const expected: CountyNdviClassification =
    delta >= threshold
      ? "GAIN_CANDIDATE"
      : delta <= -threshold
        ? "LOSS_CANDIDATE"
        : "STABLE";
  if (
    delta !== recent - baseline ||
    input.classification !== expected ||
    ((changedArea === 0) !== (clusters === 0)) ||
    (expected === "STABLE" && (changedArea !== 0 || clusters !== 0)) ||
    (expected !== "STABLE" && (changedArea === 0 || clusters === 0))
  ) {
    return null;
  }
  return Object.freeze({
    baselineMedianMillionths: baseline,
    recentMedianMillionths: recent,
    deltaNdviMillionths: delta,
    deltaThresholdMillionths: threshold,
    changedAreaBasisPoints: changedArea,
    clusterCount: clusters,
    classification: expected,
  });
}

function parseEvidence(input: unknown): CountyNdviEvidence | null {
  if (!isRecord(input) || !hasExactFields(input, EVIDENCE_FIELDS)) return null;
  if (
    input.state !== "REFERENCED_NOT_RESOLVED" ||
    !isDigestBoundReference(input.ndvi_computation_ref) ||
    !isDigestBoundReference(input.connectivity_assessment_ref) ||
    input.ndvi_computation_ref === input.connectivity_assessment_ref
  ) {
    return null;
  }
  return Object.freeze({
    state: "REFERENCED_NOT_RESOLVED",
    ndviComputationRef: input.ndvi_computation_ref,
    connectivityAssessmentRef: input.connectivity_assessment_ref,
  });
}

/** Parse one exact, fixture-only county NDVI display projection. */
export function parseCountyNdviChangeProjection(
  input: unknown,
): CountyNdviChangeProjectionResult {
  if (!isRecord(input) || !hasExactFields(input, TOP_LEVEL_FIELDS)) {
    return malformed();
  }
  if (
    input.profile !== COUNTY_NDVI_CHANGE_PROJECTION_PROFILE ||
    typeof input.panel_id !== "string" ||
    !PANEL_ID.test(input.panel_id) ||
    typeof input.outcome !== "string" ||
    !OUTCOMES.has(input.outcome as CountyNdviPanelOutcome) ||
    typeof input.reason_code !== "string" ||
    !REASON_CODES.has(input.reason_code as CountyNdviPanelReasonCode) ||
    input.status !== "PROPOSED_INACTIVE" ||
    input.execution_mode !== "FIXTURE_ONLY" ||
    input.network_attempted !== false ||
    input.source_activated !== false ||
    input.interpretation_authorized !== false ||
    input.promotion_authorized !== false ||
    input.release_authorized !== false ||
    input.publication_authorized !== false ||
    input.public_use_allowed !== false
  ) {
    return malformed();
  }
  const outcome = input.outcome as CountyNdviPanelOutcome;
  const reasonCode = input.reason_code as CountyNdviPanelReasonCode;
  if (EXPECTED_REASON[outcome] !== reasonCode) return malformed();

  let county: CountyNdviScope | null = null;
  let windows: CountyNdviWindows | null = null;
  let metrics: CountyNdviMetrics | null = null;
  let evidence: CountyNdviEvidence | null = null;
  if (outcome === "ANSWER") {
    county = parseCounty(input.county);
    windows = parseWindows(input.windows);
    metrics = parseMetrics(input.metrics);
    evidence = parseEvidence(input.evidence);
    if (county === null || windows === null || metrics === null || evidence === null) {
      return malformed();
    }
  } else if (
    input.county !== null ||
    input.windows !== null ||
    input.metrics !== null ||
    input.evidence !== null
  ) {
    return malformed();
  }

  return Object.freeze({
    ok: true,
    payload: Object.freeze({
      profile: COUNTY_NDVI_CHANGE_PROJECTION_PROFILE,
      panelId: input.panel_id,
      outcome,
      reasonCode,
      status: "PROPOSED_INACTIVE",
      executionMode: "FIXTURE_ONLY",
      county,
      windows,
      metrics,
      evidence,
      networkAttempted: false,
      sourceActivated: false,
      interpretationAuthorized: false,
      promotionAuthorized: false,
      releaseAuthorized: false,
      publicationAuthorized: false,
      publicUseAllowed: false,
    }),
  });
}
