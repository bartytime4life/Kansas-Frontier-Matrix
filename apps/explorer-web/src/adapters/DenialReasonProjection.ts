/**
 * Strict app-local adapter for a public-safe release-review denial projection.
 *
 * Only fixed reason codes and digest-bound references cross this boundary. The
 * browser never accepts free-form policy detail, counts, thresholds, geometry,
 * attestation diagnostics, credentials, source payloads, or override data.
 */

export const DENIAL_REASON_PROJECTION_PROFILE =
  "kfm.explorer.denial-reason.public-safe.v1" as const;

export type DenialReasonCode =
  | "MISSING_RECEIPT"
  | "ZOOM_TOO_FINE"
  | "LOW_COUNT_CELL"
  | "INVALID_ATTESTATION";

export type GovernedDenialReasonProjection = Readonly<{
  profile: typeof DENIAL_REASON_PROJECTION_PROFILE;
  reviewId: string;
  outcome: "DENY";
  reasonCodes: readonly DenialReasonCode[];
  releaseCandidateRef: string;
  policyDecisionRef: string;
  evaluatedAt: string;
}>;

export type DenialReasonProjectionResult =
  | Readonly<{ ok: true; payload: GovernedDenialReasonProjection }>
  | Readonly<{ ok: false; code: "MALFORMED_DENIAL_REASON_PROJECTION" }>;

const TOP_LEVEL_FIELDS = new Set([
  "profile",
  "review_id",
  "outcome",
  "reason_codes",
  "release_candidate_ref",
  "policy_decision_ref",
  "evaluated_at",
]);
const REASON_CODES = new Set<DenialReasonCode>([
  "MISSING_RECEIPT",
  "ZOOM_TOO_FINE",
  "LOW_COUNT_CELL",
  "INVALID_ATTESTATION",
]);
const MAX_REASONS = 4;
const MAX_REFERENCE_LENGTH = 320;
const SAFE_ID = /^kfm:[A-Za-z0-9][A-Za-z0-9:._~+/-]{2,235}$/;
const DIGEST_BOUND_REFERENCE =
  /^kfm:\/\/[A-Za-z0-9][A-Za-z0-9._~:/+-]{2,220}@sha256:[a-f0-9]{64}$/;
const CANONICAL_UTC_SECOND = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$/;
const CONTROL_CHARACTER = /[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/;

function malformed(): DenialReasonProjectionResult {
  return Object.freeze({
    ok: false,
    code: "MALFORMED_DENIAL_REASON_PROJECTION",
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
    value.length <= 240 &&
    SAFE_ID.test(value) &&
    !CONTROL_CHARACTER.test(value)
  );
}

function isDigestBoundReference(value: unknown): value is string {
  return (
    typeof value === "string" &&
    value.length <= MAX_REFERENCE_LENGTH &&
    DIGEST_BOUND_REFERENCE.test(value) &&
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

function parseReasonCodes(value: unknown): readonly DenialReasonCode[] | null {
  if (
    !Array.isArray(value) ||
    value.length === 0 ||
    value.length > MAX_REASONS ||
    !value.every(
      (item) =>
        typeof item === "string" && REASON_CODES.has(item as DenialReasonCode),
    ) ||
    new Set(value).size !== value.length
  ) {
    return null;
  }
  return Object.freeze([...value] as DenialReasonCode[]);
}

/** Parse one closed, detail-free denial-reason projection. */
export function parseDenialReasonProjection(
  input: unknown,
): DenialReasonProjectionResult {
  if (!isRecord(input) || !hasExactFields(input, TOP_LEVEL_FIELDS)) {
    return malformed();
  }
  if (
    input.profile !== DENIAL_REASON_PROJECTION_PROFILE ||
    !isSafeId(input.review_id) ||
    input.outcome !== "DENY" ||
    !isDigestBoundReference(input.release_candidate_ref) ||
    !isDigestBoundReference(input.policy_decision_ref) ||
    !isCanonicalUtcSecond(input.evaluated_at)
  ) {
    return malformed();
  }
  const reasonCodes = parseReasonCodes(input.reason_codes);
  if (reasonCodes === null) return malformed();

  return Object.freeze({
    ok: true,
    payload: Object.freeze({
      profile: DENIAL_REASON_PROJECTION_PROFILE,
      reviewId: input.review_id,
      outcome: "DENY",
      reasonCodes,
      releaseCandidateRef: input.release_candidate_ref,
      policyDecisionRef: input.policy_decision_ref,
      evaluatedAt: input.evaluated_at,
    }),
  });
}
