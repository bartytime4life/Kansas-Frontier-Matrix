/**
 * Strict, fixture-first adapter for a governed reveal-session projection.
 *
 * The browser receives only an opaque key-handle reference, fixed scope codes,
 * bounded KFM references, and canonical UTC timestamps. It never receives key
 * material, consent tokens, genomic payloads, exact sensitive geometry, or
 * free-form denial detail. This adapter performs no transport, policy
 * evaluation, credential verification, release action, or lifecycle-store read.
 */

export const REVEAL_SESSION_PROJECTION_PROFILE =
  "kfm.explorer.reveal-session.public-safe.v1" as const;

export type RevealSessionOutcome = "ANSWER" | "ABSTAIN" | "DENY" | "ERROR";

export type RevealSessionProjectionReasonCode =
  | "REVEAL_ACTIVE"
  | "REVEAL_UNAVAILABLE"
  | "POLICY_DENIED"
  | "UPSTREAM_ERROR";

export type RevealScopeCode =
  | "GENERALIZED_VIEW"
  | "NO_EXPORT"
  | "NO_REDISTRIBUTION"
  | "STEWARD_SESSION";

export type GovernedRevealSessionProjection = Readonly<{
  profile: typeof REVEAL_SESSION_PROJECTION_PROFILE;
  sessionId: string;
  outcome: RevealSessionOutcome;
  reasonCode: RevealSessionProjectionReasonCode;
  layerRef: string | null;
  scopeCodes: readonly RevealScopeCode[];
  startedAt: string | null;
  expiresAt: string | null;
  keyHandleRef: string | null;
  auditRef: string | null;
  policyDecisionRef: string | null;
}>;

export type RevealSessionProjectionResult =
  | Readonly<{ ok: true; payload: GovernedRevealSessionProjection }>
  | Readonly<{ ok: false; code: "MALFORMED_REVEAL_SESSION_PROJECTION" }>;

const TOP_LEVEL_FIELDS = new Set([
  "profile",
  "session_id",
  "outcome",
  "reason_code",
  "layer_ref",
  "scope_codes",
  "started_at",
  "expires_at",
  "key_handle_ref",
  "audit_ref",
  "policy_decision_ref",
]);

const OUTCOMES = new Set<RevealSessionOutcome>([
  "ANSWER",
  "ABSTAIN",
  "DENY",
  "ERROR",
]);
const REASON_CODES = new Set<RevealSessionProjectionReasonCode>([
  "REVEAL_ACTIVE",
  "REVEAL_UNAVAILABLE",
  "POLICY_DENIED",
  "UPSTREAM_ERROR",
]);
const SCOPE_CODES = new Set<RevealScopeCode>([
  "GENERALIZED_VIEW",
  "NO_EXPORT",
  "NO_REDISTRIBUTION",
  "STEWARD_SESSION",
]);
const EXPECTED_REASON: Readonly<
  Record<RevealSessionOutcome, RevealSessionProjectionReasonCode>
> = Object.freeze({
  ANSWER: "REVEAL_ACTIVE",
  ABSTAIN: "REVEAL_UNAVAILABLE",
  DENY: "POLICY_DENIED",
  ERROR: "UPSTREAM_ERROR",
});

const MAX_REFERENCE_LENGTH = 240;
const MAX_SCOPE_ITEMS = 4;
const MAX_SESSION_TTL_MS = 24 * 60 * 60 * 1000;
const SAFE_REFERENCE = /^kfm:(?:\/\/)?[A-Za-z0-9][A-Za-z0-9._~:/+-]{2,239}$/;
const SAFE_ID = /^kfm:[A-Za-z0-9][A-Za-z0-9:._~+/-]{2,235}$/;
const CANONICAL_UTC_SECOND = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$/;
const CONTROL_CHARACTER = /[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/;

function malformed(): RevealSessionProjectionResult {
  return Object.freeze({
    ok: false,
    code: "MALFORMED_REVEAL_SESSION_PROJECTION",
  });
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function hasExactFields(
  value: Record<string, unknown>,
  allowed: ReadonlySet<string>,
): boolean {
  return (
    Object.keys(value).length === allowed.size &&
    Object.keys(value).every((field) => allowed.has(field))
  );
}

function isSafeId(value: unknown): value is string {
  return (
    typeof value === "string" &&
    value.length <= MAX_REFERENCE_LENGTH &&
    SAFE_ID.test(value) &&
    !CONTROL_CHARACTER.test(value)
  );
}

function isReference(value: unknown): value is string {
  return (
    typeof value === "string" &&
    value.length <= MAX_REFERENCE_LENGTH &&
    SAFE_REFERENCE.test(value) &&
    !CONTROL_CHARACTER.test(value)
  );
}

function parseNullableReference(value: unknown): string | null | undefined {
  if (value === null) return null;
  if (isReference(value)) return value;
  return undefined;
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

function parseNullableTimestamp(value: unknown): string | null | undefined {
  if (value === null) return null;
  if (isCanonicalUtcSecond(value)) return value;
  return undefined;
}

function parseScopes(value: unknown): readonly RevealScopeCode[] | null {
  if (
    !Array.isArray(value) ||
    value.length > MAX_SCOPE_ITEMS ||
    !value.every(
      (item) =>
        typeof item === "string" && SCOPE_CODES.has(item as RevealScopeCode),
    ) ||
    new Set(value).size !== value.length
  ) {
    return null;
  }
  return Object.freeze([...value] as RevealScopeCode[]);
}

function activeDetailIsValid(
  layerRef: string | null,
  scopeCodes: readonly RevealScopeCode[],
  startedAt: string | null,
  expiresAt: string | null,
  keyHandleRef: string | null,
  auditRef: string | null,
  policyDecisionRef: string | null,
): boolean {
  if (
    layerRef === null ||
    scopeCodes.length === 0 ||
    startedAt === null ||
    expiresAt === null ||
    keyHandleRef === null ||
    auditRef === null ||
    policyDecisionRef === null
  ) {
    return false;
  }
  const startedMs = Date.parse(startedAt);
  const expiresMs = Date.parse(expiresAt);
  return (
    startedMs < expiresMs &&
    expiresMs - startedMs <= MAX_SESSION_TTL_MS &&
    keyHandleRef.startsWith("kfm://key-handle/") &&
    auditRef.startsWith("kfm://audit/") &&
    policyDecisionRef.startsWith("kfm://policy/decision/")
  );
}

function negativeDetailIsEmpty(
  layerRef: string | null,
  scopeCodes: readonly RevealScopeCode[],
  startedAt: string | null,
  expiresAt: string | null,
  keyHandleRef: string | null,
  auditRef: string | null,
  policyDecisionRef: string | null,
): boolean {
  return (
    layerRef === null &&
    scopeCodes.length === 0 &&
    startedAt === null &&
    expiresAt === null &&
    keyHandleRef === null &&
    auditRef === null &&
    policyDecisionRef === null
  );
}

/** Parse one strict, public-safe reveal-session projection. */
export function parseRevealSessionProjection(
  input: unknown,
): RevealSessionProjectionResult {
  if (!isRecord(input) || !hasExactFields(input, TOP_LEVEL_FIELDS)) {
    return malformed();
  }
  if (
    input.profile !== REVEAL_SESSION_PROJECTION_PROFILE ||
    !isSafeId(input.session_id) ||
    typeof input.outcome !== "string" ||
    !OUTCOMES.has(input.outcome as RevealSessionOutcome) ||
    typeof input.reason_code !== "string" ||
    !REASON_CODES.has(input.reason_code as RevealSessionProjectionReasonCode)
  ) {
    return malformed();
  }

  const outcome = input.outcome as RevealSessionOutcome;
  const reasonCode = input.reason_code as RevealSessionProjectionReasonCode;
  if (EXPECTED_REASON[outcome] !== reasonCode) return malformed();

  const layerRef = parseNullableReference(input.layer_ref);
  const scopeCodes = parseScopes(input.scope_codes);
  const startedAt = parseNullableTimestamp(input.started_at);
  const expiresAt = parseNullableTimestamp(input.expires_at);
  const keyHandleRef = parseNullableReference(input.key_handle_ref);
  const auditRef = parseNullableReference(input.audit_ref);
  const policyDecisionRef = parseNullableReference(input.policy_decision_ref);
  if (
    layerRef === undefined ||
    scopeCodes === null ||
    startedAt === undefined ||
    expiresAt === undefined ||
    keyHandleRef === undefined ||
    auditRef === undefined ||
    policyDecisionRef === undefined
  ) {
    return malformed();
  }

  const detailIsValid =
    outcome === "ANSWER"
      ? activeDetailIsValid(
          layerRef,
          scopeCodes,
          startedAt,
          expiresAt,
          keyHandleRef,
          auditRef,
          policyDecisionRef,
        )
      : negativeDetailIsEmpty(
          layerRef,
          scopeCodes,
          startedAt,
          expiresAt,
          keyHandleRef,
          auditRef,
          policyDecisionRef,
        );
  if (!detailIsValid) return malformed();

  return Object.freeze({
    ok: true,
    payload: Object.freeze({
      profile: REVEAL_SESSION_PROJECTION_PROFILE,
      sessionId: input.session_id,
      outcome,
      reasonCode,
      layerRef,
      scopeCodes,
      startedAt,
      expiresAt,
      keyHandleRef,
      auditRef,
      policyDecisionRef,
    }),
  });
}
