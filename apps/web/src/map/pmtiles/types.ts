export type PMTilesArchiveStage = "RELEASED" | "RAW" | "WORK" | "QUARANTINE";
export type PMTilesDecision =
  | "ALLOW_RENDER"
  | "ALLOW_RENDER_WITH_REVIEW_BADGE"
  | "DENY_RENDER";

export type PMTilesVerificationStatus = "verified" | "not_implemented" | "unknown";

export type PMTilesArchiveRef = {
  archive_id: string;
  href: string;
  stage: PMTilesArchiveStage;
  public_safe: boolean;
  digest?: string;
  signature_ref?: string;
  proof_ref?: string;
  spec_hash?: string;
  generated_at?: string;
  expected_tile_count?: number;
  tile_count?: number;
  completeness_pct?: number;
  masked_pct?: number;
  coverage_pct?: number;
  rights_status?: string;
  sensitivity?: "generalized" | "exact";
  geoprivacy_receipt_ref?: string;
  redaction_receipt_ref?: string;
  steward_attestation_ref?: string;
  reviewer_attestation_ref?: string;
  release_ref?: string;
  promotion_decision_ref?: string;
  verification_status?: PMTilesVerificationStatus;
};

export type PMTilesTimeIndex = {
  object_type: "PMTilesTimeIndex";
  generated_at?: string;
  base_archive: PMTilesArchiveRef;
  delta_archives?: PMTilesArchiveRef[];
};

export type PMTilesRuntimeEvaluation = {
  archive: PMTilesArchiveRef;
  decision: PMTilesDecision;
  reasons: string[];
  review_badge_reason?: string;
  proof_ref_present: boolean;
  digest_format_valid: boolean;
  verification_status: PMTilesVerificationStatus;
};

export type PMTilesRuntimeDecision = {
  base: PMTilesRuntimeEvaluation;
  deltas: PMTilesRuntimeEvaluation[];
};
