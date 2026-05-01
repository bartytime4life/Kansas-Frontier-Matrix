import type { PMTilesArchiveRef, PMTilesRuntimeEvaluation } from "./types";

const DIGEST_RE = /^sha256:[0-9a-f]{64}$/i;

export function evaluatePMTilesArchive(ref: PMTilesArchiveRef): PMTilesRuntimeEvaluation {
  const reasons: string[] = [];
  const digest_format_valid = Boolean(ref.digest && DIGEST_RE.test(ref.digest));
  const verification_status = ref.verification_status ?? "unknown";
  const proof_ref_present = Boolean(ref.signature_ref || ref.proof_ref);

  if (!digest_format_valid) reasons.push("missing_or_invalid_digest");
  if (ref.public_safe && ["RAW", "WORK", "QUARANTINE"].includes(ref.stage)) {
    reasons.push("forbidden_stage_for_public_runtime");
  }

  const completeness = ref.completeness_pct ?? 0;
  if (completeness < 0.95) reasons.push("completeness_below_threshold");

  const masked = ref.masked_pct ?? 0;
  const hasAttestation = Boolean(ref.steward_attestation_ref || ref.reviewer_attestation_ref);
  let review_badge_reason: string | undefined;
  if (masked > 0.3) {
    reasons.push("masked_pct_above_max");
  } else if (masked > 0.15 && !hasAttestation) {
    reasons.push("masked_pct_requires_attestation");
  } else if (masked > 0.15) {
    review_badge_reason = "masked_pct_review_band";
  }

  if (!ref.rights_status || ref.rights_status === "unknown") {
    reasons.push("unknown_rights_or_license_posture");
  }

  if (ref.public_safe && ref.sensitivity === "exact") {
    if (!ref.geoprivacy_receipt_ref && !ref.redaction_receipt_ref) {
      reasons.push("missing_geoprivacy_or_redaction_receipt");
    }
  }

  if (ref.public_safe && ref.stage === "RELEASED" && !proof_ref_present) {
    reasons.push("missing_signature_or_proof_for_released_public_artifact");
  }

  if (verification_status !== "verified") {
    reasons.push("unknown_or_unimplemented_verification_status");
  }

  const decision = reasons.length
    ? "DENY_RENDER"
    : review_badge_reason
      ? "ALLOW_RENDER_WITH_REVIEW_BADGE"
      : "ALLOW_RENDER";

  return { archive: ref, decision, reasons, review_badge_reason, proof_ref_present, digest_format_valid, verification_status };
}
