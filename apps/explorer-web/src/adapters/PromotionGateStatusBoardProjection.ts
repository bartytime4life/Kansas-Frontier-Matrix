/**
 * Strict display-only projection for the Pass 32 promotion-gate status board.
 *
 * The adapter validates a bounded reviewer-facing summary. It does not execute
 * a monitor, scorecard, validator, OPA policy, attestation verification, release
 * assembly, promotion, or publication decision.
 */

export const PROMOTION_GATE_STATUS_BOARD_PROJECTION_PROFILE =
  "kfm.explorer.promotion-gate-status-board.public-safe.v1" as const;

export type PromotionGateStatusBoardOutcome =
  | "ANSWER"
  | "ABSTAIN"
  | "DENY"
  | "ERROR";

export type PromotionGateStatusBoardReasonCode =
  | "BOARD_AVAILABLE"
  | "BOARD_UNAVAILABLE"
  | "POLICY_DENIED"
  | "UPSTREAM_ERROR";

export type PromotionGateBoardState =
  | "READY_FOR_REVIEW"
  | "HOLD"
  | "DENY"
  | "ERROR";

export type PromotionGateComponentKind =
  | "SOURCE_MONITOR"
  | "SCORECARD"
  | "SCHEMA_VALIDATOR"
  | "OPA_DECISION"
  | "ATTESTATION"
  | "RELEASE_MANIFEST_CANDIDATE";

export type PromotionGateComponentState =
  | "PASS"
  | "HOLD"
  | "DENY"
  | "ERROR"
  | "NOT_RUN";

export type PromotionGateComponentReasonCode =
  | "CHECK_PASSED"
  | "CHECK_HELD"
  | "CHECK_DENIED"
  | "CHECK_ERROR"
  | "CHECK_NOT_RUN";

export type PromotionGateComponent = Readonly<{
  kind: PromotionGateComponentKind;
  state: PromotionGateComponentState;
  artifactRef: string | null;
  reasonCode: PromotionGateComponentReasonCode;
}>;

export type PromotionGateStatusSummary = Readonly<{
  passCount: number;
  holdCount: number;
  denyCount: number;
  errorCount: number;
  notRunCount: number;
}>;

export type PromotionGateStatusGovernance = Readonly<{
  sourceMonitorExecuted: false;
  validatorExecuted: false;
  policyEvaluated: false;
  attestationVerified: false;
  reviewAuthenticated: false;
  promotionAllowed: false;
  releaseAuthorized: false;
  publicationAllowed: false;
}>;

export type GovernedPromotionGateStatusBoardProjection = Readonly<{
  profile: typeof PROMOTION_GATE_STATUS_BOARD_PROJECTION_PROFILE;
  boardId: string;
  outcome: PromotionGateStatusBoardOutcome;
  reasonCode: PromotionGateStatusBoardReasonCode;
  observedAt: string | null;
  candidateRef: string | null;
  boardState: PromotionGateBoardState | null;
  components: readonly PromotionGateComponent[];
  summary: PromotionGateStatusSummary | null;
  governance: PromotionGateStatusGovernance;
}>;

export type PromotionGateStatusBoardProjectionResult =
  | Readonly<{ ok: true; payload: GovernedPromotionGateStatusBoardProjection }>
  | Readonly<{ ok: false; code: "MALFORMED_PROMOTION_GATE_STATUS_BOARD_PROJECTION" }>;

export const COMPONENT_ORDER = Object.freeze([
  "SOURCE_MONITOR",
  "SCORECARD",
  "SCHEMA_VALIDATOR",
  "OPA_DECISION",
  "ATTESTATION",
  "RELEASE_MANIFEST_CANDIDATE",
] as const satisfies readonly PromotionGateComponentKind[]);

const TOP_LEVEL_FIELDS = new Set([
  "profile",
  "board_id",
  "outcome",
  "reason_code",
  "observed_at",
  "candidate_ref",
  "board_state",
  "components",
  "summary",
  "governance",
]);
const COMPONENT_FIELDS = new Set([
  "kind",
  "state",
  "artifact_ref",
  "reason_code",
]);
const SUMMARY_FIELDS = new Set([
  "pass_count",
  "hold_count",
  "deny_count",
  "error_count",
  "not_run_count",
]);
const GOVERNANCE_FIELDS = new Set([
  "source_monitor_executed",
  "validator_executed",
  "policy_evaluated",
  "attestation_verified",
  "review_authenticated",
  "promotion_allowed",
  "release_authorized",
  "publication_allowed",
]);

const OUTCOMES = new Set<PromotionGateStatusBoardOutcome>([
  "ANSWER",
  "ABSTAIN",
  "DENY",
  "ERROR",
]);
const REASONS = new Set<PromotionGateStatusBoardReasonCode>([
  "BOARD_AVAILABLE",
  "BOARD_UNAVAILABLE",
  "POLICY_DENIED",
  "UPSTREAM_ERROR",
]);
const EXPECTED_REASON: Readonly<
  Record<PromotionGateStatusBoardOutcome, PromotionGateStatusBoardReasonCode>
> = Object.freeze({
  ANSWER: "BOARD_AVAILABLE",
  ABSTAIN: "BOARD_UNAVAILABLE",
  DENY: "POLICY_DENIED",
  ERROR: "UPSTREAM_ERROR",
});
const COMPONENT_STATES = new Set<PromotionGateComponentState>([
  "PASS",
  "HOLD",
  "DENY",
  "ERROR",
  "NOT_RUN",
]);
const COMPONENT_REASONS = new Set<PromotionGateComponentReasonCode>([
  "CHECK_PASSED",
  "CHECK_HELD",
  "CHECK_DENIED",
  "CHECK_ERROR",
  "CHECK_NOT_RUN",
]);
const EXPECTED_COMPONENT_REASON: Readonly<
  Record<PromotionGateComponentState, PromotionGateComponentReasonCode>
> = Object.freeze({
  PASS: "CHECK_PASSED",
  HOLD: "CHECK_HELD",
  DENY: "CHECK_DENIED",
  ERROR: "CHECK_ERROR",
  NOT_RUN: "CHECK_NOT_RUN",
});

const BOARD_ID = /^kfm:promotion-gate-status-board:[A-Za-z0-9][A-Za-z0-9:._~+/-]{2,245}$/;
const KFM_REFERENCE = /^kfm:\/\/[A-Za-z0-9][A-Za-z0-9._~:/+-]{2,315}$/;
const CANONICAL_TIMESTAMP = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$/;
const CONTROL_CHARACTER = /[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/;

function malformed(): PromotionGateStatusBoardProjectionResult {
  return Object.freeze({
    ok: false,
    code: "MALFORMED_PROMOTION_GATE_STATUS_BOARD_PROJECTION",
  });
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function hasExactFields(
  value: Record<string, unknown>,
  expected: ReadonlySet<string>,
): boolean {
  return (
    Object.keys(value).length === expected.size &&
    Object.keys(value).every((field) => expected.has(field))
  );
}

function isIdentifier(value: unknown, pattern: RegExp, max = 320): value is string {
  return (
    typeof value === "string" &&
    value.length <= max &&
    value === value.trim() &&
    pattern.test(value) &&
    !CONTROL_CHARACTER.test(value)
  );
}

function isCanonicalTimestamp(value: unknown): value is string {
  if (typeof value !== "string" || !CANONICAL_TIMESTAMP.test(value)) return false;
  const parsed = new Date(value);
  return (
    Number.isFinite(parsed.getTime()) &&
    parsed.toISOString().replace(".000Z", "Z") === value
  );
}

function parseGovernance(input: unknown): PromotionGateStatusGovernance | null {
  if (!isRecord(input) || !hasExactFields(input, GOVERNANCE_FIELDS)) return null;
  if (
    input.source_monitor_executed !== false ||
    input.validator_executed !== false ||
    input.policy_evaluated !== false ||
    input.attestation_verified !== false ||
    input.review_authenticated !== false ||
    input.promotion_allowed !== false ||
    input.release_authorized !== false ||
    input.publication_allowed !== false
  ) {
    return null;
  }
  return Object.freeze({
    sourceMonitorExecuted: false,
    validatorExecuted: false,
    policyEvaluated: false,
    attestationVerified: false,
    reviewAuthenticated: false,
    promotionAllowed: false,
    releaseAuthorized: false,
    publicationAllowed: false,
  });
}

function parseComponent(
  input: unknown,
  expectedKind: PromotionGateComponentKind,
): PromotionGateComponent | null {
  if (!isRecord(input) || !hasExactFields(input, COMPONENT_FIELDS)) return null;
  if (
    input.kind !== expectedKind ||
    typeof input.state !== "string" ||
    !COMPONENT_STATES.has(input.state as PromotionGateComponentState) ||
    typeof input.reason_code !== "string" ||
    !COMPONENT_REASONS.has(input.reason_code as PromotionGateComponentReasonCode)
  ) {
    return null;
  }
  const state = input.state as PromotionGateComponentState;
  const reasonCode = input.reason_code as PromotionGateComponentReasonCode;
  if (EXPECTED_COMPONENT_REASON[state] !== reasonCode) return null;

  const artifactRef =
    input.artifact_ref === null
      ? null
      : isIdentifier(input.artifact_ref, KFM_REFERENCE)
        ? input.artifact_ref
        : undefined;
  if (artifactRef === undefined || (state === "NOT_RUN") !== (artifactRef === null)) {
    return null;
  }
  return Object.freeze({
    kind: expectedKind,
    state,
    artifactRef,
    reasonCode,
  });
}

function parseComponents(input: unknown): readonly PromotionGateComponent[] | null {
  if (!Array.isArray(input) || input.length !== COMPONENT_ORDER.length) return null;
  const components: PromotionGateComponent[] = [];
  const refs = new Set<string>();
  for (let index = 0; index < COMPONENT_ORDER.length; index += 1) {
    const component = parseComponent(input[index], COMPONENT_ORDER[index]);
    if (component === null) return null;
    if (component.artifactRef !== null) {
      if (refs.has(component.artifactRef)) return null;
      refs.add(component.artifactRef);
    }
    components.push(component);
  }
  return Object.freeze(components);
}

function parseSummary(input: unknown): PromotionGateStatusSummary | null {
  if (!isRecord(input) || !hasExactFields(input, SUMMARY_FIELDS)) return null;
  const raw = [
    input.pass_count,
    input.hold_count,
    input.deny_count,
    input.error_count,
    input.not_run_count,
  ];
  if (
    raw.some(
      (value) =>
        typeof value !== "number" ||
        !Number.isInteger(value) ||
        value < 0 ||
        value > COMPONENT_ORDER.length,
    )
  ) {
    return null;
  }
  return Object.freeze({
    passCount: input.pass_count as number,
    holdCount: input.hold_count as number,
    denyCount: input.deny_count as number,
    errorCount: input.error_count as number,
    notRunCount: input.not_run_count as number,
  });
}

function deriveBoardState(
  components: readonly PromotionGateComponent[],
): PromotionGateBoardState {
  if (components.some((component) => component.state === "ERROR")) return "ERROR";
  if (components.some((component) => component.state === "DENY")) return "DENY";
  if (
    components.some(
      (component) => component.state === "HOLD" || component.state === "NOT_RUN",
    )
  ) {
    return "HOLD";
  }
  return "READY_FOR_REVIEW";
}

/** Parse one exact, bounded promotion-gate board projection. */
export function parsePromotionGateStatusBoardProjection(
  input: unknown,
): PromotionGateStatusBoardProjectionResult {
  if (!isRecord(input) || !hasExactFields(input, TOP_LEVEL_FIELDS)) return malformed();
  if (
    input.profile !== PROMOTION_GATE_STATUS_BOARD_PROJECTION_PROFILE ||
    !isIdentifier(input.board_id, BOARD_ID) ||
    typeof input.outcome !== "string" ||
    !OUTCOMES.has(input.outcome as PromotionGateStatusBoardOutcome) ||
    typeof input.reason_code !== "string" ||
    !REASONS.has(input.reason_code as PromotionGateStatusBoardReasonCode)
  ) {
    return malformed();
  }
  const outcome = input.outcome as PromotionGateStatusBoardOutcome;
  const reasonCode = input.reason_code as PromotionGateStatusBoardReasonCode;
  if (EXPECTED_REASON[outcome] !== reasonCode) return malformed();
  const governance = parseGovernance(input.governance);
  if (governance === null) return malformed();

  if (outcome !== "ANSWER") {
    if (
      input.observed_at !== null ||
      input.candidate_ref !== null ||
      input.board_state !== null ||
      !Array.isArray(input.components) ||
      input.components.length !== 0 ||
      input.summary !== null
    ) {
      return malformed();
    }
    return Object.freeze({
      ok: true,
      payload: Object.freeze({
        profile: PROMOTION_GATE_STATUS_BOARD_PROJECTION_PROFILE,
        boardId: input.board_id,
        outcome,
        reasonCode,
        observedAt: null,
        candidateRef: null,
        boardState: null,
        components: Object.freeze([]),
        summary: null,
        governance,
      }),
    });
  }

  if (
    !isCanonicalTimestamp(input.observed_at) ||
    !isIdentifier(input.candidate_ref, KFM_REFERENCE) ||
    !input.candidate_ref.startsWith("kfm://release-candidate/") ||
    typeof input.board_state !== "string" ||
    !["READY_FOR_REVIEW", "HOLD", "DENY", "ERROR"].includes(input.board_state)
  ) {
    return malformed();
  }
  const components = parseComponents(input.components);
  const summary = parseSummary(input.summary);
  if (components === null || summary === null) return malformed();

  const passCount = components.filter((component) => component.state === "PASS").length;
  const holdCount = components.filter((component) => component.state === "HOLD").length;
  const denyCount = components.filter((component) => component.state === "DENY").length;
  const errorCount = components.filter((component) => component.state === "ERROR").length;
  const notRunCount = components.filter((component) => component.state === "NOT_RUN").length;
  if (
    summary.passCount !== passCount ||
    summary.holdCount !== holdCount ||
    summary.denyCount !== denyCount ||
    summary.errorCount !== errorCount ||
    summary.notRunCount !== notRunCount ||
    passCount + holdCount + denyCount + errorCount + notRunCount !==
      COMPONENT_ORDER.length ||
    input.board_state !== deriveBoardState(components)
  ) {
    return malformed();
  }

  return Object.freeze({
    ok: true,
    payload: Object.freeze({
      profile: PROMOTION_GATE_STATUS_BOARD_PROJECTION_PROFILE,
      boardId: input.board_id,
      outcome,
      reasonCode,
      observedAt: input.observed_at,
      candidateRef: input.candidate_ref,
      boardState: input.board_state as PromotionGateBoardState,
      components,
      summary,
      governance,
    }),
  });
}
