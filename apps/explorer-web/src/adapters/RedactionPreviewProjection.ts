/**
 * Strict public-safe projection for a pre-release redaction preview.
 *
 * The projection carries only finite transform summaries and digest-bound
 * references produced upstream by governed services. It accepts no geometry,
 * coordinates, counts, thresholds, hidden values, transform secrets, free-form
 * diagnostics, policy evaluation, review approval, or release authority.
 */

export const REDACTION_PREVIEW_PROJECTION_PROFILE =
  "kfm.explorer.redaction-preview.public-safe.v1" as const;

export type RedactionPreviewOutcome = "ANSWER" | "ABSTAIN" | "DENY" | "ERROR";

export type RedactionPreviewReasonCode =
  | "PREVIEW_READY"
  | "PREVIEW_INCOMPLETE"
  | "POLICY_DENIED"
  | "UPSTREAM_ERROR";

export type GeometryTransformSummary =
  | "GEOMETRY_GENERALIZED"
  | "GEOMETRY_WITHHELD"
  | "GEOMETRY_NOT_APPLICABLE";

export type SuppressionTransformSummary =
  | "LOW_COUNT_SUPPRESSED"
  | "ALL_COUNTS_WITHHELD"
  | "SUPPRESSION_NOT_APPLICABLE";

export type PublicSafeAbstractionKind =
  | "COUNTY_AGGREGATE"
  | "WATERSHED_AGGREGATE"
  | "GRID_AGGREGATE"
  | "TEMPORAL_BUCKET"
  | "PUBLIC_SAFE_SYMBOL"
  | "FEATURES_WITHHELD";

export type GovernedRedactionPreviewProjection = Readonly<{
  profile: typeof REDACTION_PREVIEW_PROJECTION_PROFILE;
  previewId: string;
  outcome: RedactionPreviewOutcome;
  reasonCode: RedactionPreviewReasonCode;
  evaluatedAt: string | null;
  releaseCandidateRef: string | null;
  policyDecisionRef: string | null;
  redactionReceiptRef: string | null;
  geometryTransform: GeometryTransformSummary | null;
  suppressionTransform: SuppressionTransformSummary | null;
  maximumPublicZoom: number | null;
  abstractionKind: PublicSafeAbstractionKind | null;
}>;

export type RedactionPreviewProjectionResult =
  | Readonly<{ ok: true; payload: GovernedRedactionPreviewProjection }>
  | Readonly<{ ok: false; code: "MALFORMED_REDACTION_PREVIEW_PROJECTION" }>;

const TOP_LEVEL_FIELDS = new Set([
  "profile",
  "preview_id",
  "outcome",
  "reason_code",
  "evaluated_at",
  "release_candidate_ref",
  "policy_decision_ref",
  "redaction_receipt_ref",
  "geometry_transform",
  "suppression_transform",
  "maximum_public_zoom",
  "abstraction_kind",
]);

const OUTCOMES = new Set<RedactionPreviewOutcome>([
  "ANSWER",
  "ABSTAIN",
  "DENY",
  "ERROR",
]);
const REASON_CODES = new Set<RedactionPreviewReasonCode>([
  "PREVIEW_READY",
  "PREVIEW_INCOMPLETE",
  "POLICY_DENIED",
  "UPSTREAM_ERROR",
]);
const GEOMETRY_TRANSFORMS = new Set<GeometryTransformSummary>([
  "GEOMETRY_GENERALIZED",
  "GEOMETRY_WITHHELD",
  "GEOMETRY_NOT_APPLICABLE",
]);
const SUPPRESSION_TRANSFORMS = new Set<SuppressionTransformSummary>([
  "LOW_COUNT_SUPPRESSED",
  "ALL_COUNTS_WITHHELD",
  "SUPPRESSION_NOT_APPLICABLE",
]);
const ABSTRACTION_KINDS = new Set<PublicSafeAbstractionKind>([
  "COUNTY_AGGREGATE",
  "WATERSHED_AGGREGATE",
  "GRID_AGGREGATE",
  "TEMPORAL_BUCKET",
  "PUBLIC_SAFE_SYMBOL",
  "FEATURES_WITHHELD",
]);
const EXPECTED_REASON: Readonly<
  Record<RedactionPreviewOutcome, RedactionPreviewReasonCode>
> = Object.freeze({
  ANSWER: "PREVIEW_READY",
  ABSTAIN: "PREVIEW_INCOMPLETE",
  DENY: "POLICY_DENIED",
  ERROR: "UPSTREAM_ERROR",
});

const MAX_REFERENCE_LENGTH = 320;
const PREVIEW_ID =
  /^kfm:redaction-preview:[A-Za-z0-9][A-Za-z0-9:._~+/-]{2,280}$/;
const DIGEST_BOUND_REFERENCE =
  /^kfm:\/\/[A-Za-z0-9][A-Za-z0-9._~:/+-]{2,220}@sha256:[a-f0-9]{64}$/;
const UTC_SECOND = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$/;
const CONTROL_CHARACTER = /[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/;

function malformed(): RedactionPreviewProjectionResult {
  return Object.freeze({
    ok: false,
    code: "MALFORMED_REDACTION_PREVIEW_PROJECTION",
  });
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function hasExactFields(value: Record<string, unknown>): boolean {
  return (
    Object.keys(value).length === TOP_LEVEL_FIELDS.size &&
    Object.keys(value).every((field) => TOP_LEVEL_FIELDS.has(field))
  );
}

function isPreviewId(value: unknown): value is string {
  return (
    typeof value === "string" &&
    value.length <= MAX_REFERENCE_LENGTH &&
    PREVIEW_ID.test(value) &&
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

function parseNullableReference(value: unknown): string | null | undefined {
  if (value === null) return null;
  if (isDigestBoundReference(value)) return value;
  return undefined;
}

function isCanonicalUtcSecond(value: unknown): value is string {
  if (typeof value !== "string" || !UTC_SECOND.test(value)) return false;
  const milliseconds = Date.parse(value);
  return (
    Number.isFinite(milliseconds) &&
    new Date(milliseconds).toISOString().replace(".000Z", "Z") === value
  );
}

function parseNullableTimestamp(value: unknown): string | null | undefined {
  if (value === null) return null;
  if (isCanonicalUtcSecond(value)) return value;
  return undefined;
}

function parseNullableEnum<T extends string>(
  value: unknown,
  values: ReadonlySet<T>,
): T | null | undefined {
  if (value === null) return null;
  if (typeof value === "string" && values.has(value as T)) return value as T;
  return undefined;
}

function parseNullableZoom(value: unknown): number | null | undefined {
  if (value === null) return null;
  if (Number.isInteger(value) && Number(value) >= 0 && Number(value) <= 22) {
    return Number(value);
  }
  return undefined;
}

function isReferenceFamily(value: string | null, family: string): boolean {
  return value?.startsWith(`kfm://${family}/`) === true;
}

function positiveClosureIsValid(
  evaluatedAt: string | null,
  releaseCandidateRef: string | null,
  policyDecisionRef: string | null,
  redactionReceiptRef: string | null,
  geometryTransform: GeometryTransformSummary | null,
  suppressionTransform: SuppressionTransformSummary | null,
  maximumPublicZoom: number | null,
  abstractionKind: PublicSafeAbstractionKind | null,
): boolean {
  return (
    evaluatedAt !== null &&
    isReferenceFamily(releaseCandidateRef, "release-candidate") &&
    isReferenceFamily(policyDecisionRef, "policy-decision") &&
    isReferenceFamily(redactionReceiptRef, "redaction-receipt") &&
    geometryTransform !== null &&
    suppressionTransform !== null &&
    maximumPublicZoom !== null &&
    abstractionKind !== null
  );
}

function negativeDetailIsEmpty(
  evaluatedAt: string | null,
  releaseCandidateRef: string | null,
  policyDecisionRef: string | null,
  redactionReceiptRef: string | null,
  geometryTransform: GeometryTransformSummary | null,
  suppressionTransform: SuppressionTransformSummary | null,
  maximumPublicZoom: number | null,
  abstractionKind: PublicSafeAbstractionKind | null,
): boolean {
  return (
    evaluatedAt === null &&
    releaseCandidateRef === null &&
    policyDecisionRef === null &&
    redactionReceiptRef === null &&
    geometryTransform === null &&
    suppressionTransform === null &&
    maximumPublicZoom === null &&
    abstractionKind === null
  );
}

/** Parse one exact, non-authoritative redaction-preview projection. */
export function parseRedactionPreviewProjection(
  input: unknown,
): RedactionPreviewProjectionResult {
  if (!isRecord(input) || !hasExactFields(input)) return malformed();
  if (
    input.profile !== REDACTION_PREVIEW_PROJECTION_PROFILE ||
    !isPreviewId(input.preview_id) ||
    typeof input.outcome !== "string" ||
    !OUTCOMES.has(input.outcome as RedactionPreviewOutcome) ||
    typeof input.reason_code !== "string" ||
    !REASON_CODES.has(input.reason_code as RedactionPreviewReasonCode)
  ) {
    return malformed();
  }

  const outcome = input.outcome as RedactionPreviewOutcome;
  const reasonCode = input.reason_code as RedactionPreviewReasonCode;
  if (EXPECTED_REASON[outcome] !== reasonCode) return malformed();

  const evaluatedAt = parseNullableTimestamp(input.evaluated_at);
  const releaseCandidateRef = parseNullableReference(input.release_candidate_ref);
  const policyDecisionRef = parseNullableReference(input.policy_decision_ref);
  const redactionReceiptRef = parseNullableReference(input.redaction_receipt_ref);
  const geometryTransform = parseNullableEnum(
    input.geometry_transform,
    GEOMETRY_TRANSFORMS,
  );
  const suppressionTransform = parseNullableEnum(
    input.suppression_transform,
    SUPPRESSION_TRANSFORMS,
  );
  const maximumPublicZoom = parseNullableZoom(input.maximum_public_zoom);
  const abstractionKind = parseNullableEnum(
    input.abstraction_kind,
    ABSTRACTION_KINDS,
  );

  if (
    evaluatedAt === undefined ||
    releaseCandidateRef === undefined ||
    policyDecisionRef === undefined ||
    redactionReceiptRef === undefined ||
    geometryTransform === undefined ||
    suppressionTransform === undefined ||
    maximumPublicZoom === undefined ||
    abstractionKind === undefined
  ) {
    return malformed();
  }

  const detailIsValid =
    outcome === "ANSWER"
      ? positiveClosureIsValid(
          evaluatedAt,
          releaseCandidateRef,
          policyDecisionRef,
          redactionReceiptRef,
          geometryTransform,
          suppressionTransform,
          maximumPublicZoom,
          abstractionKind,
        )
      : negativeDetailIsEmpty(
          evaluatedAt,
          releaseCandidateRef,
          policyDecisionRef,
          redactionReceiptRef,
          geometryTransform,
          suppressionTransform,
          maximumPublicZoom,
          abstractionKind,
        );
  if (!detailIsValid) return malformed();

  return Object.freeze({
    ok: true,
    payload: Object.freeze({
      profile: REDACTION_PREVIEW_PROJECTION_PROFILE,
      previewId: input.preview_id,
      outcome,
      reasonCode,
      evaluatedAt,
      releaseCandidateRef,
      policyDecisionRef,
      redactionReceiptRef,
      geometryTransform,
      suppressionTransform,
      maximumPublicZoom,
      abstractionKind,
    }),
  });
}
