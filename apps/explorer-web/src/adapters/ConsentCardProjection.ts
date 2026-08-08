/**
 * Strict, fixture-first adapter for the Explorer consent-card projection.
 *
 * This module performs no transport, policy evaluation, EvidenceBundle
 * resolution, lifecycle-store access, consent issuance, or revocation. It
 * accepts only a small public-safe projection produced upstream by a governed
 * service and fails closed on malformed or contradictory input.
 */

export const CONSENT_CARD_PROJECTION_PROFILE =
  "kfm.explorer.consent-card.public-safe.v1" as const;

export type ConsentCardOutcome = "ANSWER" | "ABSTAIN" | "DENY" | "ERROR";

export type ConsentCardProjectionReasonCode =
  | "CONSENT_CARD_READY"
  | "CONSENT_UNRESOLVED"
  | "POLICY_DENIED"
  | "UPSTREAM_ERROR";

export type SubjectConsentState =
  | "RECORDED"
  | "NOT_APPLICABLE"
  | "WITHHELD"
  | "UNRESOLVED";

export type GovernedConsentCardProjection = Readonly<{
  profile: typeof CONSENT_CARD_PROJECTION_PROFILE;
  id: string;
  outcome: ConsentCardOutcome;
  reasonCode: ConsentCardProjectionReasonCode;
  layerRef: string | null;
  layerLabel: string | null;
  basis: string | null;
  scope: readonly string[];
  expiresAt: string | null;
  subjectConsentState: SubjectConsentState;
  obligationSetRef: string | null;
  policyDecisionRef: string | null;
}>;

export type ConsentCardProjectionResult =
  | Readonly<{ ok: true; payload: GovernedConsentCardProjection }>
  | Readonly<{ ok: false; code: "MALFORMED_CONSENT_CARD_PROJECTION" }>;

const TOP_LEVEL_FIELDS = new Set([
  "profile",
  "id",
  "outcome",
  "reason_code",
  "layer_ref",
  "layer_label",
  "basis",
  "scope",
  "expires_at",
  "subject_consent_state",
  "obligation_set_ref",
  "policy_decision_ref",
]);

const OUTCOMES = new Set<ConsentCardOutcome>([
  "ANSWER",
  "ABSTAIN",
  "DENY",
  "ERROR",
]);
const REASON_CODES = new Set<ConsentCardProjectionReasonCode>([
  "CONSENT_CARD_READY",
  "CONSENT_UNRESOLVED",
  "POLICY_DENIED",
  "UPSTREAM_ERROR",
]);
const SUBJECT_CONSENT_STATES = new Set<SubjectConsentState>([
  "RECORDED",
  "NOT_APPLICABLE",
  "WITHHELD",
  "UNRESOLVED",
]);
const EXPECTED_REASON: Readonly<
  Record<ConsentCardOutcome, ConsentCardProjectionReasonCode>
> = Object.freeze({
  ANSWER: "CONSENT_CARD_READY",
  ABSTAIN: "CONSENT_UNRESOLVED",
  DENY: "POLICY_DENIED",
  ERROR: "UPSTREAM_ERROR",
});

const MAX_ID_LENGTH = 240;
const MAX_LABEL_LENGTH = 160;
const MAX_BASIS_LENGTH = 480;
const MAX_SCOPE_LENGTH = 240;
const MAX_SCOPE_ITEMS = 12;
const SAFE_REFERENCE = /^kfm:(?:\/\/)?[A-Za-z0-9][A-Za-z0-9._~:/+-]{2,239}$/;
const SAFE_ID = /^kfm:[A-Za-z0-9][A-Za-z0-9:._~+/-]{2,235}$/;
const CANONICAL_UTC_SECOND = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$/;
const CONTROL_CHARACTER = /[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/;

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function hasExactFields(
  value: Record<string, unknown>,
  allowed: ReadonlySet<string>,
): boolean {
  return Object.keys(value).every((field) => allowed.has(field));
}

function isBoundedString(value: unknown, maximum: number): value is string {
  return (
    typeof value === "string" &&
    value.length > 0 &&
    value.length <= maximum &&
    value.trim() === value &&
    !CONTROL_CHARACTER.test(value)
  );
}

function isSafeId(value: unknown): value is string {
  return (
    typeof value === "string" &&
    value.length <= MAX_ID_LENGTH &&
    SAFE_ID.test(value)
  );
}

function isReference(value: unknown): value is string {
  return (
    typeof value === "string" &&
    value.length <= MAX_ID_LENGTH &&
    SAFE_REFERENCE.test(value) &&
    !CONTROL_CHARACTER.test(value)
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

function parseNullableBoundedString(
  value: unknown,
  maximum: number,
): string | null | undefined {
  if (value === null) return null;
  if (isBoundedString(value, maximum)) return value;
  return undefined;
}

function parseNullableReference(value: unknown): string | null | undefined {
  if (value === null) return null;
  if (isReference(value)) return value;
  return undefined;
}

function parseScope(value: unknown): readonly string[] | null {
  if (!Array.isArray(value) || value.length > MAX_SCOPE_ITEMS) return null;
  if (!value.every((item) => isBoundedString(item, MAX_SCOPE_LENGTH))) {
    return null;
  }
  if (new Set(value).size !== value.length) return null;
  return Object.freeze([...value]);
}

function isEmptyNegativeDetail(
  layerRef: string | null,
  layerLabel: string | null,
  basis: string | null,
  scope: readonly string[],
  expiresAt: string | null,
  obligationSetRef: string | null,
  policyDecisionRef: string | null,
): boolean {
  return (
    layerRef === null &&
    layerLabel === null &&
    basis === null &&
    scope.length === 0 &&
    expiresAt === null &&
    obligationSetRef === null &&
    policyDecisionRef === null
  );
}

/** Parse one strict public-safe consent-card projection. */
export function parseConsentCardProjection(
  input: unknown,
): ConsentCardProjectionResult {
  if (!isRecord(input) || !hasExactFields(input, TOP_LEVEL_FIELDS)) {
    return Object.freeze({
      ok: false,
      code: "MALFORMED_CONSENT_CARD_PROJECTION",
    });
  }

  if (input.profile !== CONSENT_CARD_PROJECTION_PROFILE) {
    return Object.freeze({
      ok: false,
      code: "MALFORMED_CONSENT_CARD_PROJECTION",
    });
  }
  if (!isSafeId(input.id)) {
    return Object.freeze({
      ok: false,
      code: "MALFORMED_CONSENT_CARD_PROJECTION",
    });
  }
  if (typeof input.outcome !== "string" || !OUTCOMES.has(input.outcome as ConsentCardOutcome)) {
    return Object.freeze({
      ok: false,
      code: "MALFORMED_CONSENT_CARD_PROJECTION",
    });
  }
  if (
    typeof input.reason_code !== "string" ||
    !REASON_CODES.has(input.reason_code as ConsentCardProjectionReasonCode)
  ) {
    return Object.freeze({
      ok: false,
      code: "MALFORMED_CONSENT_CARD_PROJECTION",
    });
  }
  if (
    typeof input.subject_consent_state !== "string" ||
    !SUBJECT_CONSENT_STATES.has(
      input.subject_consent_state as SubjectConsentState,
    )
  ) {
    return Object.freeze({
      ok: false,
      code: "MALFORMED_CONSENT_CARD_PROJECTION",
    });
  }

  const outcome = input.outcome as ConsentCardOutcome;
  const reasonCode = input.reason_code as ConsentCardProjectionReasonCode;
  if (EXPECTED_REASON[outcome] !== reasonCode) {
    return Object.freeze({
      ok: false,
      code: "MALFORMED_CONSENT_CARD_PROJECTION",
    });
  }

  const layerRef = parseNullableReference(input.layer_ref);
  const layerLabel = parseNullableBoundedString(
    input.layer_label,
    MAX_LABEL_LENGTH,
  );
  const basis = parseNullableBoundedString(input.basis, MAX_BASIS_LENGTH);
  const scope = parseScope(input.scope);
  const obligationSetRef = parseNullableReference(input.obligation_set_ref);
  const policyDecisionRef = parseNullableReference(input.policy_decision_ref);
  const expiresAt =
    input.expires_at === null
      ? null
      : isCanonicalUtcSecond(input.expires_at)
        ? input.expires_at
        : undefined;

  if (
    layerRef === undefined ||
    layerLabel === undefined ||
    basis === undefined ||
    scope === null ||
    expiresAt === undefined ||
    obligationSetRef === undefined ||
    policyDecisionRef === undefined
  ) {
    return Object.freeze({
      ok: false,
      code: "MALFORMED_CONSENT_CARD_PROJECTION",
    });
  }

  const subjectConsentState =
    input.subject_consent_state as SubjectConsentState;

  if (outcome === "ANSWER") {
    if (
      layerRef === null ||
      layerLabel === null ||
      basis === null ||
      scope.length === 0 ||
      obligationSetRef === null ||
      policyDecisionRef === null ||
      subjectConsentState === "UNRESOLVED"
    ) {
      return Object.freeze({
        ok: false,
        code: "MALFORMED_CONSENT_CARD_PROJECTION",
      });
    }
  } else if (
    !isEmptyNegativeDetail(
      layerRef,
      layerLabel,
      basis,
      scope,
      expiresAt,
      obligationSetRef,
      policyDecisionRef,
    ) ||
    subjectConsentState !== "UNRESOLVED"
  ) {
    return Object.freeze({
      ok: false,
      code: "MALFORMED_CONSENT_CARD_PROJECTION",
    });
  }

  return Object.freeze({
    ok: true,
    payload: Object.freeze({
      profile: CONSENT_CARD_PROJECTION_PROFILE,
      id: input.id,
      outcome,
      reasonCode,
      layerRef,
      layerLabel,
      basis,
      scope,
      expiresAt,
      subjectConsentState,
      obligationSetRef,
      policyDecisionRef,
    }),
  });
}
