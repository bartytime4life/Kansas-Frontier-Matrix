import type { PMTilesRuntimeEvaluation } from "./types";

export function toPMTilesEvidenceRows(evaluations: PMTilesRuntimeEvaluation[]) {
  return evaluations.map((entry) => ({
    href: entry.archive.href,
    digest: entry.archive.digest,
    spec_hash: entry.archive.spec_hash,
    generated_at: entry.archive.generated_at,
    promotion_or_release_ref: entry.archive.release_ref ?? entry.archive.promotion_decision_ref,
    completeness_pct: entry.archive.completeness_pct,
    masked_pct: entry.archive.masked_pct,
    coverage_pct: entry.archive.coverage_pct,
    signature_ref: entry.archive.signature_ref,
    proof_ref: entry.archive.proof_ref,
    geoprivacy_receipt_ref: entry.archive.geoprivacy_receipt_ref,
    redaction_receipt_ref: entry.archive.redaction_receipt_ref,
    runtime_decision: entry.decision,
    deny_reasons: entry.reasons,
    review_badge_reason: entry.review_badge_reason
  }));
}
