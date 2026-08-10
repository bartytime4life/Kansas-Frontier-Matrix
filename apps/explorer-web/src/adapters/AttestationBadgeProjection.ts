/**
 * Strict public-safe projection for the Pass 32 attestation badge.
 *
 * The projection reports a finite upstream result and, only for a verified
 * result, carries bounded references that a governed evidence surface may
 * inspect. It performs no cryptographic verification, evidence resolution,
 * policy evaluation, release action, transport, or lifecycle-store read.
 */

export const ATTESTATION_BADGE_PROJECTION_PROFILE =
  "kfm.explorer.attestation-badge.public-safe.v1" as const;

export type AttestationBadgeOutcome = "ANSWER" | "ABSTAIN" | "DENY" | "ERROR";

export type AttestationBadgeReasonCode =
  | "CHECKS_VERIFIED"
  | "CHECKS_INCOMPLETE"
  | "CHECKS_FAILED"
  | "UPSTREAM_ERROR";

export type GovernedAttestationBadgeProjection = Readonly<{
  profile: typeof ATTESTATION_BADGE_PROJECTION_PROFILE;
  badgeId: string;
  outcome: AttestationBadgeOutcome;
  reasonCode: AttestationBadgeReasonCode;
  layerRef: string | null;
  evaluatedAt: string | null;
  attestationRef: string | null;
  runReceiptRef: string | null;
  evidenceBundleRef: string | null;
  releaseManifestRef: string | null;
}>;

export type AttestationBadgeProjectionResult =
  | Readonly<{ ok: true; payload: GovernedAttestationBadgeProjection }>
  | Readonly<{ ok: false; code: "MALFORMED_ATTESTATION_BADGE_PROJECTION" }>;

const TOP_LEVEL_FIELDS = new Set([
  "profile",
  "badge_id",
  "outcome",
  "reason_code",
  "layer_ref",
  "evaluated_at",
  "attestation_ref",
  "run_receipt_ref",
  "evidence_bundle_ref",
  "release_manifest_ref",
]);

const OUTCOMES = new Set<AttestationBadgeOutcome>([
  "ANSWER",
  "ABSTAIN",
  "DENY",
  "ERROR",
]);
const REASON_CODES = new Set<AttestationBadgeReasonCode>([
  "CHECKS_VERIFIED",
  "CHECKS_INCOMPLETE",
  "CHECKS_FAILED",
  "UPSTREAM_ERROR",
]);
const EXPECTED_REASON: Readonly<
  Record<AttestationBadgeOutcome, AttestationBadgeReasonCode>
> = Object.freeze({
  ANSWER: "CHECKS_VERIFIED",
  ABSTAIN: "CHECKS_INCOMPLETE",
  DENY: "CHECKS_FAILED",
  ERROR: "UPSTREAM_ERROR",
});

const MAX_REFERENCE_LENGTH = 320;
const BADGE_ID = /^kfm:attestation-badge:[A-Za-z0-9][A-Za-z0-9:._~+/-]{2,280}$/;
const KFM_REFERENCE = /^kfm:(?:\/\/)?[A-Za-z0-9][A-Za-z0-9._~:/+-]{2,315}$/;
const RELEASE_REF_PREFIX = ["kfm://release", "/"].join("");
const UTC_SECOND = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$/;
const CONTROL_CHARACTER = /[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/;

function malformed(): AttestationBadgeProjectionResult {
  return Object.freeze({
    ok: false,
    code: "MALFORMED_ATTESTATION_BADGE_PROJECTION",
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

function isBadgeId(value: unknown): value is string {
  return (
    typeof value === "string" &&
    value.length <= MAX_REFERENCE_LENGTH &&
    BADGE_ID.test(value) &&
    !CONTROL_CHARACTER.test(value)
  );
}

function isReference(value: unknown): value is string {
  return (
    typeof value === "string" &&
    value.length <= MAX_REFERENCE_LENGTH &&
    KFM_REFERENCE.test(value) &&
    !CONTROL_CHARACTER.test(value)
  );
}

function parseNullableReference(value: unknown): string | null | undefined {
  if (value === null) return null;
  if (isReference(value)) return value;
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

function positiveReferencesAreValid(
  layerRef: string | null,
  evaluatedAt: string | null,
  attestationRef: string | null,
  runReceiptRef: string | null,
  evidenceBundleRef: string | null,
  releaseManifestRef: string | null,
): boolean {
  return (
    layerRef?.startsWith("kfm://layer/") === true &&
    evaluatedAt !== null &&
    attestationRef?.startsWith("kfm://attestation/") === true &&
    runReceiptRef?.startsWith("kfm://receipt/") === true &&
    (evidenceBundleRef?.startsWith("kfm://evidence/") === true ||
      evidenceBundleRef?.startsWith("kfm:evidence:") === true) &&
    releaseManifestRef?.startsWith(RELEASE_REF_PREFIX) === true
  );
}

function negativeReferencesAreEmpty(
  layerRef: string | null,
  evaluatedAt: string | null,
  attestationRef: string | null,
  runReceiptRef: string | null,
  evidenceBundleRef: string | null,
  releaseManifestRef: string | null,
): boolean {
  return (
    layerRef === null &&
    evaluatedAt === null &&
    attestationRef === null &&
    runReceiptRef === null &&
    evidenceBundleRef === null &&
    releaseManifestRef === null
  );
}

/** Parse one exact, public-safe attestation badge projection. */
export function parseAttestationBadgeProjection(
  input: unknown,
): AttestationBadgeProjectionResult {
  if (!isRecord(input) || !hasExactFields(input)) return malformed();
  if (
    input.profile !== ATTESTATION_BADGE_PROJECTION_PROFILE ||
    !isBadgeId(input.badge_id) ||
    typeof input.outcome !== "string" ||
    !OUTCOMES.has(input.outcome as AttestationBadgeOutcome) ||
    typeof input.reason_code !== "string" ||
    !REASON_CODES.has(input.reason_code as AttestationBadgeReasonCode)
  ) {
    return malformed();
  }

  const outcome = input.outcome as AttestationBadgeOutcome;
  const reasonCode = input.reason_code as AttestationBadgeReasonCode;
  if (EXPECTED_REASON[outcome] !== reasonCode) return malformed();

  const layerRef = parseNullableReference(input.layer_ref);
  const evaluatedAt = parseNullableTimestamp(input.evaluated_at);
  const attestationRef = parseNullableReference(input.attestation_ref);
  const runReceiptRef = parseNullableReference(input.run_receipt_ref);
  const evidenceBundleRef = parseNullableReference(input.evidence_bundle_ref);
  const releaseManifestRef = parseNullableReference(input.release_manifest_ref);
  if (
    layerRef === undefined ||
    evaluatedAt === undefined ||
    attestationRef === undefined ||
    runReceiptRef === undefined ||
    evidenceBundleRef === undefined ||
    releaseManifestRef === undefined
  ) {
    return malformed();
  }

  const referencesAreValid =
    outcome === "ANSWER"
      ? positiveReferencesAreValid(
          layerRef,
          evaluatedAt,
          attestationRef,
          runReceiptRef,
          evidenceBundleRef,
          releaseManifestRef,
        )
      : negativeReferencesAreEmpty(
          layerRef,
          evaluatedAt,
          attestationRef,
          runReceiptRef,
          evidenceBundleRef,
          releaseManifestRef,
        );
  if (!referencesAreValid) return malformed();

  return Object.freeze({
    ok: true,
    payload: Object.freeze({
      profile: ATTESTATION_BADGE_PROJECTION_PROFILE,
      badgeId: input.badge_id,
      outcome,
      reasonCode,
      layerRef,
      evaluatedAt,
      attestationRef,
      runReceiptRef,
      evidenceBundleRef,
      releaseManifestRef,
    }),
  });
}
