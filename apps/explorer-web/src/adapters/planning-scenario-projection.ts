/**
 * Strict fixture-only projection for a bounded planning-scenario review.
 *
 * The adapter validates a pre-governed display packet. It never computes a
 * scenario, resolves evidence, infers consensus, recommends action, evaluates
 * policy, or reads a lifecycle store.
 */

export const PLANNING_SCENARIO_PROJECTION_PROFILE =
  "kfm.explorer.planning-scenario.fixture.v1" as const;

export type PlanningScenarioOutcome = "ABSTAIN" | "DENY" | "ERROR";
export type PlanningScenarioReasonCode =
  | "SCENARIO_HELD"
  | "SCENARIO_MISSING"
  | "POLICY_DENIED"
  | "UPSTREAM_ERROR";
export type PlanningScenarioUncertainty =
  | "LOW"
  | "MEDIUM"
  | "HIGH"
  | "UNRESOLVED";

export type PlanningScenarioGeography = Readonly<{
  scopeType: "STATEWIDE_GENERALIZED";
  label: string;
  exactGeometry: false;
}>;

export type PlanningScenarioHorizon = Readonly<{
  baselineAsOf: string;
  horizonStart: string;
  horizonEnd: string;
}>;

export type PlanningScenarioInputVariable = Readonly<{
  variableId: string;
  label: string;
  sourceRef: string;
  uncertainty: PlanningScenarioUncertainty;
}>;

export type PlanningScenarioAssumption = Readonly<{
  assumptionId: string;
  statement: string;
  evidenceRefs: readonly string[];
  uncertainty: PlanningScenarioUncertainty;
}>;

export type PlanningScenarioEquityDimension = Readonly<{
  dimensionId: string;
  description: string;
  evidenceRefs: readonly string[];
  limitation: string;
}>;

export type GovernedPlanningScenarioProjection = Readonly<{
  profile: typeof PLANNING_SCENARIO_PROJECTION_PROFILE;
  scenarioId: string;
  outcome: PlanningScenarioOutcome;
  reasonCode: PlanningScenarioReasonCode;
  status: "PROPOSED_INACTIVE";
  executionMode: "FIXTURE_ONLY";
  scenarioStatus: "HELD" | null;
  synthetic: true;
  title: string | null;
  purpose: string | null;
  geography: PlanningScenarioGeography | null;
  horizon: PlanningScenarioHorizon | null;
  inputVariables: readonly PlanningScenarioInputVariable[];
  assumptions: readonly PlanningScenarioAssumption[];
  equityDimensions: readonly PlanningScenarioEquityDimension[];
  participationRefs: readonly string[];
  evidenceRefs: readonly string[];
  limitations: readonly string[];
  nonAuthorityLabels: readonly string[];
  evidenceResolved: false;
  policyApproved: false;
  reviewApproved: false;
  recommendationAuthorized: false;
  publicationAuthorized: false;
}>;

export type PlanningScenarioProjectionResult =
  | Readonly<{ ok: true; payload: GovernedPlanningScenarioProjection }>
  | Readonly<{
      ok: false;
      code: "MALFORMED_PLANNING_SCENARIO_PROJECTION";
    }>;

const TOP_LEVEL_FIELDS = new Set([
  "profile",
  "scenario_id",
  "outcome",
  "reason_code",
  "status",
  "execution_mode",
  "scenario_status",
  "synthetic",
  "title",
  "purpose",
  "geography",
  "horizon",
  "input_variables",
  "assumptions",
  "equity_dimensions",
  "participation_refs",
  "evidence_refs",
  "limitations",
  "non_authority_labels",
  "evidence_resolved",
  "policy_approved",
  "review_approved",
  "recommendation_authorized",
  "publication_authorized",
]);
const GEOGRAPHY_FIELDS = new Set(["scope_type", "label", "exact_geometry"]);
const HORIZON_FIELDS = new Set([
  "baseline_as_of",
  "horizon_start",
  "horizon_end",
]);
const INPUT_FIELDS = new Set([
  "variable_id",
  "label",
  "source_ref",
  "uncertainty",
]);
const ASSUMPTION_FIELDS = new Set([
  "assumption_id",
  "statement",
  "evidence_refs",
  "uncertainty",
]);
const EQUITY_FIELDS = new Set([
  "dimension_id",
  "description",
  "evidence_refs",
  "limitation",
]);
const OUTCOMES = new Set<PlanningScenarioOutcome>([
  "ABSTAIN",
  "DENY",
  "ERROR",
]);
const REASON_CODES = new Set<PlanningScenarioReasonCode>([
  "SCENARIO_HELD",
  "SCENARIO_MISSING",
  "POLICY_DENIED",
  "UPSTREAM_ERROR",
]);
const UNCERTAINTY = new Set<PlanningScenarioUncertainty>([
  "LOW",
  "MEDIUM",
  "HIGH",
  "UNRESOLVED",
]);
const REQUIRED_NON_AUTHORITY_LABELS = Object.freeze([
  "NOT_A_PREDICTION",
  "NOT_EMERGENCY_ALERTING",
  "NOT_REGULATORY_DETERMINATION",
]);
const SCENARIO_ID =
  /^kfm:planning-scenario:[A-Za-z0-9][A-Za-z0-9:._~+/-]{2,250}$/;
const MEMBER_ID = /^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$/;
const SAFE_REFERENCE = /^(?:fixture|kfm):(?:\/\/)?[A-Za-z0-9][A-Za-z0-9._~:/+-]{2,315}$/;
const DENIED_REFERENCE_PREFIXES = [
  "raw:",
  "work:",
  "quarantine:",
  "internal:",
  "canonical:",
];
const ISO_DATE = /^\d{4}-\d{2}-\d{2}$/;
const CONTROL_CHARACTER = /[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/;

function malformed(): PlanningScenarioProjectionResult {
  return Object.freeze({
    ok: false,
    code: "MALFORMED_PLANNING_SCENARIO_PROJECTION",
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

function isSafeText(value: unknown, maxLength: number): value is string {
  return (
    typeof value === "string" &&
    value.length > 0 &&
    value.length <= maxLength &&
    !CONTROL_CHARACTER.test(value)
  );
}

function isReference(value: unknown): value is string {
  return (
    typeof value === "string" &&
    value.length <= 320 &&
    SAFE_REFERENCE.test(value) &&
    !CONTROL_CHARACTER.test(value) &&
    !DENIED_REFERENCE_PREFIXES.some((prefix) => value.startsWith(prefix))
  );
}

function isIsoDate(value: unknown): value is string {
  if (typeof value !== "string" || !ISO_DATE.test(value)) return false;
  const milliseconds = Date.parse(`${value}T00:00:00Z`);
  return (
    Number.isFinite(milliseconds) &&
    new Date(milliseconds).toISOString().slice(0, 10) === value
  );
}

function parseStringArray(
  input: unknown,
  options: Readonly<{
    min: number;
    max: number;
    validate: (value: unknown) => value is string;
    canonical?: boolean;
  }>,
): readonly string[] | null {
  if (
    !Array.isArray(input) ||
    input.length < options.min ||
    input.length > options.max ||
    !input.every(options.validate)
  ) {
    return null;
  }
  const values = input as string[];
  if (
    new Set(values).size !== values.length ||
    (options.canonical !== false &&
      values.some((value, index) => index > 0 && values[index - 1] > value))
  ) {
    return null;
  }
  return Object.freeze([...values]);
}

function parseGeography(input: unknown): PlanningScenarioGeography | null {
  if (!isRecord(input) || !hasExactFields(input, GEOGRAPHY_FIELDS)) return null;
  if (
    input.scope_type !== "STATEWIDE_GENERALIZED" ||
    !isSafeText(input.label, 160) ||
    input.exact_geometry !== false
  ) {
    return null;
  }
  return Object.freeze({
    scopeType: "STATEWIDE_GENERALIZED",
    label: input.label,
    exactGeometry: false,
  });
}

function parseHorizon(input: unknown): PlanningScenarioHorizon | null {
  if (!isRecord(input) || !hasExactFields(input, HORIZON_FIELDS)) return null;
  if (
    !isIsoDate(input.baseline_as_of) ||
    !isIsoDate(input.horizon_start) ||
    !isIsoDate(input.horizon_end) ||
    input.baseline_as_of > input.horizon_start ||
    input.horizon_start >= input.horizon_end
  ) {
    return null;
  }
  return Object.freeze({
    baselineAsOf: input.baseline_as_of,
    horizonStart: input.horizon_start,
    horizonEnd: input.horizon_end,
  });
}

function parseInputVariable(input: unknown): PlanningScenarioInputVariable | null {
  if (!isRecord(input) || !hasExactFields(input, INPUT_FIELDS)) return null;
  if (
    typeof input.variable_id !== "string" ||
    !MEMBER_ID.test(input.variable_id) ||
    !isSafeText(input.label, 200) ||
    !isReference(input.source_ref) ||
    typeof input.uncertainty !== "string" ||
    !UNCERTAINTY.has(input.uncertainty as PlanningScenarioUncertainty)
  ) {
    return null;
  }
  return Object.freeze({
    variableId: input.variable_id,
    label: input.label,
    sourceRef: input.source_ref,
    uncertainty: input.uncertainty as PlanningScenarioUncertainty,
  });
}

function parseAssumption(input: unknown): PlanningScenarioAssumption | null {
  if (!isRecord(input) || !hasExactFields(input, ASSUMPTION_FIELDS)) return null;
  const evidenceRefs = parseStringArray(input.evidence_refs, {
    min: 1,
    max: 12,
    validate: isReference,
  });
  if (
    typeof input.assumption_id !== "string" ||
    !MEMBER_ID.test(input.assumption_id) ||
    !isSafeText(input.statement, 700) ||
    evidenceRefs === null ||
    typeof input.uncertainty !== "string" ||
    !UNCERTAINTY.has(input.uncertainty as PlanningScenarioUncertainty)
  ) {
    return null;
  }
  return Object.freeze({
    assumptionId: input.assumption_id,
    statement: input.statement,
    evidenceRefs,
    uncertainty: input.uncertainty as PlanningScenarioUncertainty,
  });
}

function parseEquityDimension(
  input: unknown,
): PlanningScenarioEquityDimension | null {
  if (!isRecord(input) || !hasExactFields(input, EQUITY_FIELDS)) return null;
  const evidenceRefs = parseStringArray(input.evidence_refs, {
    min: 1,
    max: 12,
    validate: isReference,
  });
  if (
    typeof input.dimension_id !== "string" ||
    !MEMBER_ID.test(input.dimension_id) ||
    !isSafeText(input.description, 700) ||
    evidenceRefs === null ||
    !isSafeText(input.limitation, 500)
  ) {
    return null;
  }
  return Object.freeze({
    dimensionId: input.dimension_id,
    description: input.description,
    evidenceRefs,
    limitation: input.limitation,
  });
}

function parseObjectArray<T>(
  input: unknown,
  options: Readonly<{
    min: number;
    max: number;
    parse: (value: unknown) => T | null;
    id: (value: T) => string;
  }>,
): readonly T[] | null {
  if (!Array.isArray(input) || input.length < options.min || input.length > options.max) {
    return null;
  }
  const parsed: T[] = [];
  for (const value of input) {
    const item = options.parse(value);
    if (item === null) return null;
    parsed.push(item);
  }
  const ids = parsed.map(options.id);
  if (
    new Set(ids).size !== ids.length ||
    ids.some((value, index) => index > 0 && ids[index - 1] > value)
  ) {
    return null;
  }
  return Object.freeze(parsed);
}

function referencesClose(
  inputs: readonly PlanningScenarioInputVariable[],
  assumptions: readonly PlanningScenarioAssumption[],
  equity: readonly PlanningScenarioEquityDimension[],
  evidenceRefs: readonly string[],
): boolean {
  const declared = new Set(evidenceRefs);
  return (
    inputs.every((item) => declared.has(item.sourceRef)) &&
    assumptions.every((item) => item.evidenceRefs.every((ref) => declared.has(ref))) &&
    equity.every((item) => item.evidenceRefs.every((ref) => declared.has(ref)))
  );
}

function emptyDetail(input: Record<string, unknown>): boolean {
  return (
    input.scenario_status === null &&
    input.title === null &&
    input.purpose === null &&
    input.geography === null &&
    input.horizon === null &&
    Array.isArray(input.input_variables) &&
    input.input_variables.length === 0 &&
    Array.isArray(input.assumptions) &&
    input.assumptions.length === 0 &&
    Array.isArray(input.equity_dimensions) &&
    input.equity_dimensions.length === 0 &&
    Array.isArray(input.participation_refs) &&
    input.participation_refs.length === 0 &&
    Array.isArray(input.evidence_refs) &&
    input.evidence_refs.length === 0 &&
    Array.isArray(input.limitations) &&
    input.limitations.length === 0 &&
    Array.isArray(input.non_authority_labels) &&
    input.non_authority_labels.length === 0
  );
}

/** Parse one exact, bounded planning-scenario display projection. */
export function parsePlanningScenarioProjection(
  input: unknown,
): PlanningScenarioProjectionResult {
  if (!isRecord(input) || !hasExactFields(input, TOP_LEVEL_FIELDS)) {
    return malformed();
  }
  if (
    input.profile !== PLANNING_SCENARIO_PROJECTION_PROFILE ||
    typeof input.scenario_id !== "string" ||
    !SCENARIO_ID.test(input.scenario_id) ||
    typeof input.outcome !== "string" ||
    !OUTCOMES.has(input.outcome as PlanningScenarioOutcome) ||
    typeof input.reason_code !== "string" ||
    !REASON_CODES.has(input.reason_code as PlanningScenarioReasonCode) ||
    input.status !== "PROPOSED_INACTIVE" ||
    input.execution_mode !== "FIXTURE_ONLY" ||
    input.synthetic !== true ||
    input.evidence_resolved !== false ||
    input.policy_approved !== false ||
    input.review_approved !== false ||
    input.recommendation_authorized !== false ||
    input.publication_authorized !== false
  ) {
    return malformed();
  }

  const outcome = input.outcome as PlanningScenarioOutcome;
  const reasonCode = input.reason_code as PlanningScenarioReasonCode;
  const outcomeMatchesReason =
    (outcome === "ABSTAIN" &&
      (reasonCode === "SCENARIO_HELD" || reasonCode === "SCENARIO_MISSING")) ||
    (outcome === "DENY" && reasonCode === "POLICY_DENIED") ||
    (outcome === "ERROR" && reasonCode === "UPSTREAM_ERROR");
  if (!outcomeMatchesReason) return malformed();

  if (reasonCode !== "SCENARIO_HELD") {
    if (!emptyDetail(input)) return malformed();
    return Object.freeze({
      ok: true,
      payload: Object.freeze({
        profile: PLANNING_SCENARIO_PROJECTION_PROFILE,
        scenarioId: input.scenario_id,
        outcome,
        reasonCode,
        status: "PROPOSED_INACTIVE",
        executionMode: "FIXTURE_ONLY",
        scenarioStatus: null,
        synthetic: true,
        title: null,
        purpose: null,
        geography: null,
        horizon: null,
        inputVariables: Object.freeze([]),
        assumptions: Object.freeze([]),
        equityDimensions: Object.freeze([]),
        participationRefs: Object.freeze([]),
        evidenceRefs: Object.freeze([]),
        limitations: Object.freeze([]),
        nonAuthorityLabels: Object.freeze([]),
        evidenceResolved: false,
        policyApproved: false,
        reviewApproved: false,
        recommendationAuthorized: false,
        publicationAuthorized: false,
      }),
    });
  }

  const geography = parseGeography(input.geography);
  const horizon = parseHorizon(input.horizon);
  const inputVariables = parseObjectArray(input.input_variables, {
    min: 1,
    max: 12,
    parse: parseInputVariable,
    id: (value) => value.variableId,
  });
  const assumptions = parseObjectArray(input.assumptions, {
    min: 1,
    max: 12,
    parse: parseAssumption,
    id: (value) => value.assumptionId,
  });
  const equityDimensions = parseObjectArray(input.equity_dimensions, {
    min: 1,
    max: 8,
    parse: parseEquityDimension,
    id: (value) => value.dimensionId,
  });
  const participationRefs = parseStringArray(input.participation_refs, {
    min: 1,
    max: 16,
    validate: isReference,
  });
  const evidenceRefs = parseStringArray(input.evidence_refs, {
    min: 1,
    max: 24,
    validate: isReference,
  });
  const limitations = parseStringArray(input.limitations, {
    min: 1,
    max: 12,
    validate: (value): value is string => isSafeText(value, 500),
    canonical: false,
  });
  const nonAuthorityLabels = parseStringArray(input.non_authority_labels, {
    min: 3,
    max: 3,
    validate: (value): value is string => isSafeText(value, 80),
  });
  if (
    input.scenario_status !== "HELD" ||
    !isSafeText(input.title, 240) ||
    !isSafeText(input.purpose, 900) ||
    geography === null ||
    horizon === null ||
    inputVariables === null ||
    assumptions === null ||
    equityDimensions === null ||
    participationRefs === null ||
    evidenceRefs === null ||
    limitations === null ||
    nonAuthorityLabels === null ||
    nonAuthorityLabels.length !== REQUIRED_NON_AUTHORITY_LABELS.length ||
    nonAuthorityLabels.some(
      (value, index) => value !== REQUIRED_NON_AUTHORITY_LABELS[index],
    ) ||
    !referencesClose(inputVariables, assumptions, equityDimensions, evidenceRefs)
  ) {
    return malformed();
  }

  return Object.freeze({
    ok: true,
    payload: Object.freeze({
      profile: PLANNING_SCENARIO_PROJECTION_PROFILE,
      scenarioId: input.scenario_id,
      outcome,
      reasonCode,
      status: "PROPOSED_INACTIVE",
      executionMode: "FIXTURE_ONLY",
      scenarioStatus: "HELD",
      synthetic: true,
      title: input.title,
      purpose: input.purpose,
      geography,
      horizon,
      inputVariables,
      assumptions,
      equityDimensions,
      participationRefs,
      evidenceRefs,
      limitations,
      nonAuthorityLabels,
      evidenceResolved: false,
      policyApproved: false,
      reviewApproved: false,
      recommendationAuthorized: false,
      publicationAuthorized: false,
    }),
  });
}
