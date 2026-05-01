# Promotion Gate

## KFM Meta Block v2
- **Status:** PROPOSED
- **Layer:** Promotion Gate (post evidence-ci)
- **Scope:** Fixture-backed, no-network validation + policy checks in CI
- **Last Updated:** 2026-05-01

## Purpose
Promotion is a governed state transition that denies release unless evidence, receipts, policy posture, and registration posture pass together.

## Lifecycle placement
This gate runs between evidence-ci outputs and release manifest publication.

## Inputs / outputs
- **Inputs:** `PromotionCandidate` JSON fixtures containing evidence bundle refs, spec hash, receipt refs, rights, sensitivity, and release intent.
- **Outputs:** `PromotionDecision` JSON (`APPROVE` or `DENY`) with explicit reason codes.

## Deny rules
- Public release from `RAW`, `WORK`, or `QUARANTINE`.
- `target_state=PUBLISHED` without reviewer.
- `rights_status=unknown`.
- `sensitivity=restricted` with `public_release=true`.
- Missing `evidencebundle_spec_hash`.
- Missing run receipt ref or run receipt bundle ref.
- Public release without Cosign receipt verification.
- Public release without `gatehouse_registration_posture=registered`.

## CI behavior
Workflow `.github/workflows/promotion-gate.yml` runs validator + Conftest on fixture inputs and fails closed on invalid policy posture.

## Artifact separation
Promotion decisions are emitted as separate artifacts; they do not replace or merge with receipts, manifests, catalogs, or published objects.

## Rollback / correction notes
Denied candidates remain non-published; correction requires updated candidate posture and rerun through this gate.

## Open questions
- Canonical EvidenceBundle signature/verification adapter shape for future strict cryptographic checks.
- Standardized Gatehouse posture vocabulary beyond `registered|pending|unknown`.
- Whether to require schema validation in validator runtime once shared contract tooling is centralized.
