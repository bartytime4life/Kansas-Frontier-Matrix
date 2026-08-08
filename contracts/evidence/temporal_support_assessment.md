<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/temporal-support-assessment
title: TemporalSupportAssessment Contract
type: contract
version: v1.0.0
status: proposed; fixture-first; local-only; non-authoritative
owners: OWNER_TBD — evidence steward; temporal-data steward; correction steward; validation steward
created: 2026-08-07
updated: 2026-08-07
policy_label: repository-facing; temporal-support; correction-aware; fail-closed
owning_root: contracts/
responsibility: Determine whether one claim or artifact is supported for one requested time basis while preserving freshness, correction, supersession, withdrawal, and rollback state.
truth_posture: cite-or-abstain
related:
  - ../../schemas/contracts/v1/evidence/temporal_support_assessment.schema.json
  - ../../tools/validators/evidence/validate_temporal_support_assessment.py
  - ../../fixtures/contracts/v1/evidence/temporal_support_assessment/
  - ../../tests/evidence/test_temporal_support_assessment.py
  - ../release/trust_projection_manifest.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "This assessment references TimeSliceManifest; it does not duplicate or replace released asset identity."
  - "Temporal support is query-specific. Fresh data can still be out of scope, and in-scope data can still be stale."
[/KFM_META_BLOCK_V2] -->

# TemporalSupportAssessment

> **Purpose.** Bind a query interval and query mode to declared valid time, source-update time, retrieval time, freshness tolerance, released time-slice identity, correction lineage, and rollback support.

## Source basis

- *KFM Components Pass 18* calls for temporal-support and correction-support acceptance criteria and treats time as a first-class evidence dimension.
- *KFM Components Pass 13* and *Pass 15* require trust-visible freshness and correction state and a common proof-object/schema wave.

The profile operationalizes those ideas against current repository evidence: `TimeSliceManifest` already exists, so this object evaluates support and references it instead of creating a competing manifest.

## Finite outcomes

| Outcome | Required meaning |
|---|---|
| `SUPPORTED` | Query is within valid time, temporal basis is complete, source is fresh, no conflict is declared, and release state is usable. |
| `STALE` | Query may be in scope, but freshness tolerance is exceeded. |
| `OUT_OF_SCOPE` | Requested time is outside declared valid time or the released slice is withdrawn. |
| `CONFLICTED` | Two or more incompatible temporal supports remain unresolved. |
| `UNKNOWN` | Required temporal basis is incomplete. |

## Correction rules

`CORRECTED`, `WITHDRAWN`, and `SUPERSEDED` require `correction_ref`; `SUPERSEDED` also requires `superseded_by_ref`. Every assessment requires a rollback reference through the referenced release state. A corrected current release may still support a query when the correction is explicit.

## Directory Rules basis

Meaning belongs in `contracts/evidence/`; shape in `schemas/contracts/v1/evidence/`; validation in `tools/validators/evidence/`; fixtures in `fixtures/contracts/v1/evidence/`; tests in `tests/evidence/`; provenance in `data/receipts/generated/`. No new lifecycle or release authority is created.

## Non-effects and rollback

The profile does not mutate `TimeSliceManifest`, `CorrectionNotice`, `ReleaseManifest`, rollback state, caches, maps, or APIs. Revert the bounded commit to remove the profile.
