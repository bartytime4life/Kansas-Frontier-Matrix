<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/source-role-transition-assessment
title: SourceRoleTransitionAssessment Contract
type: contract
version: v1.0.0
status: proposed; fixture-first; no-network; non-publisher
owners: OWNER_TBD — source steward; affected domain steward; evidence steward; validation steward
created: 2026-08-07
updated: 2026-08-07
policy_label: repository-facing; source-role; anti-collapse; fail-closed
owning_root: contracts/
responsibility: Check whether a declared transformation preserves source-role meaning and required receipts without reclassifying candidate, modeled, aggregate, synthetic, regulatory, administrative, or observed material as another authority class.
truth_posture: cite-or-abstain
related:
  - ../../schemas/contracts/v1/source/source_role_transition_assessment.schema.json
  - ../../tools/validators/source_role/validate_source_role_transition_assessment.py
  - ../../fixtures/contracts/v1/source/source_role_transition_assessment/
  - ../../tests/source/test_source_role_transition_assessment.py
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "Lifecycle promotion does not upgrade source role."
  - "Domain source-role matrices remain authoritative for lane-specific semantics; this profile supplies a shared minimum anti-collapse grammar."
[/KFM_META_BLOCK_V2] -->

# SourceRoleTransitionAssessment

> **Purpose.** Prevent silent role laundering by making transformations and required process receipts explicit. An observed record, modeled estimate, regulatory determination, administrative compilation, aggregate, candidate, or synthetic representation remains distinguishable after processing.

## Source basis

- *KFM Components Pass 18* requires source descriptors to preserve source role and warns that clean visual products can hide mediation, scale, uncertainty, and provenance.
- *KFM Components Pass 13* and *Pass 15* call for shared proof grammar rather than lane-specific reinvention.
- Current repository evidence contains multiple domain source-role matrices but no shared transition-assessment contract at this path.

## Transition rules

| Operation | Allowed output | Required support |
|---|---|---|
| `PASSTHROUGH`, `GENERALIZE` | Same role as the single input role | Input EvidenceBundle linkage. |
| `PROMOTE_LIFECYCLE` | Same role; candidate inputs remain on `HOLD` until resolved | Promotion cannot manufacture authority. |
| `AGGREGATE` | `AGGREGATE` | `aggregation_receipt_ref`; candidate inputs hold. |
| `MODEL` | `MODELED` | `model_run_receipt_ref`; candidate inputs hold. |
| `SYNTHESIZE` | `SYNTHETIC` | `representation_receipt_ref` and `reality_boundary_note_ref`; candidate inputs hold. |

Output lineage must preserve the distinct set of input roles. A valid `DENY` or `HOLD` record is a governed result; the validator rejects only inconsistent declarations, such as a denied transition marked `PASS`.

## Directory Rules basis

Source semantics belong in `contracts/source/`; shape in `schemas/contracts/v1/source/`; the cross-domain checker in `tools/validators/source_role/`; fixtures in `fixtures/contracts/v1/source/`; tests in `tests/source/`; authoring provenance in `data/receipts/generated/`. No source is activated and no lifecycle data is written.

## Non-effects and rollback

This profile neither changes domain source matrices nor rewrites SourceDescriptor values. Revert the bounded commit to remove it; no source, published artifact, or release state is affected.
