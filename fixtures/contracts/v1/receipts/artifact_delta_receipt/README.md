# Artifact delta receipt fixtures

These fixtures exercise only the proposed `ArtifactDeltaReceiptCandidate` shape and local
consistency rules. Every identifier, digest, actor, registry locator, release, review, policy
record, and attestation is synthetic.

## Valid lane

- `valid_approved.json`: distinct before/after revisions with approved review, declared
  verified COSE metadata, OCI referrer metadata, and a rollback target.
- `valid_rollback.json`: a compensating rollback candidate with correction and rollback
  references.

## Invalid lane

- `invalid_no_effect.json`: no artifact/spec change and reused run receipt.
- `invalid_approval_unverified_attestation.json`: approval with unverified attestation metadata.
- `invalid_rollback_missing_target.json`: approved rollback without a rollback target.
- `invalid_digest_mismatch.json`: stored canonical payload digest does not recompute.

`expected_findings_manifest.json` pins exact expected semantic finding codes. A fixture pass
is not signature verification, policy approval, review approval, promotion, release, rollback,
or publication authority.
