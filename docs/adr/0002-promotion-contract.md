# ADR 0002: Promotion Contract

## Status

Accepted

## Context

Promotion previously depended on ad hoc conventions: reviewers checked some artifacts, CI checked others, and final publication could occur without a complete evidence chain. The organization needs a contract that maps gates to specific jobs, artifacts, policies, and integrity checks.

## Decision

Adopt the Promotion Contract defined in `promotion-contract.json` and summarized in `PROMOTION_CONTRACT.md`. Gates A→G are mandatory and fail closed:

- A: evidence integrity
- B: run provenance
- C: rights and sensitivity
- D: obligations applied
- E: stewardship approvals
- F: deploy preflight
- G: final publish and archive

Each gate has a Rego policy pack under `policy/<gate>/main.rego`. CI invokes `tools/validators/run_gate.sh <gate>` so every gate receives a normalized policy input and the same required artifact list.

## Consequences

A promotion cannot proceed when an artifact is missing, malformed, unsigned when a signature is required, or denied by policy. The contract is now part of the release surface and must be reviewed like production code.

## Validation / Enforcement

GitHub Actions runs validation and promotion jobs. Conftest evaluates each gate policy. Cosign verifies signed blobs. Validators verify canonical `spec_hash` and release manifest artifact hashes.

## Rollback

To roll back this ADR, revert `promotion-contract.json`, `.github/workflows/promotion.yml`, `policy/`, and `tools/validators/` together. Partial rollback is not allowed because it can create disagreement between policy and CI.
