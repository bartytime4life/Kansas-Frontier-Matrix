<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/data/baseline-cohort-assessment
title: BaselineCohortAssessment Contract
type: contract
version: v0.1.0
status: proposed; fixture-first; local-only; non-authoritative
owners: OWNER_TBD — data steward; analysis steward; domain baseline steward; validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: repository-facing; baseline; cohort; discontinuity; fail-closed
owning_root: contracts/
responsibility: Bind a versioned baseline manifest, cohort eligibility, discontinuities, validation result, and rebuild provenance into one replayable review candidate.
truth_posture: cite-or-abstain
related:
  - ../../schemas/contracts/v1/data/baseline_cohort_assessment.schema.json
  - ../../tools/validators/data/validate_baseline_cohort_assessment.py
  - ../../fixtures/contracts/v1/data/baseline_cohort_assessment/cases.json
  - ../../tests/data/test_baseline_cohort_assessment.py
  - ../../docs/intake/exploratory/new-ideas-4-16-source-map.md
  - ../../docs/kfm_full_atlas_seed_cards.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "A coherent baseline is a review candidate, not a scientific threshold, anomaly decision, policy decision, or release object."
  - "The profile uses synthetic references and digests only; it does not fetch observations or prove the referenced bytes exist."
[/KFM_META_BLOCK_V2] -->

# BaselineCohortAssessment

> **Purpose.** Make a baseline inspectable as a versioned, replayable evidence artifact whose cohort eligibility, exclusions, missingness, method identity, discontinuities, validation result, and rebuild provenance remain explicit.

## Source basis and dependency readiness

Full Atlas triad `KFM-TRIAD-036`, especially programming card `KFM-CAND-0108`, proposes `BaselineManifest`, `CohortEligibilityReport`, `DiscontinuityRecord`, `BaselineValidationReport`, and `BaselineRebuildReceipt` semantics. The reconciled April 16 intake orders stable diff and material-change meaning before baseline governance. Both prerequisites now exist on `main` as `tools/diff/stable_diff.py` and `contracts/data/material_change_assessment.md`. This proposed composite is the next contract-only step; it activates no source and computes no operational baseline.

## Composite parts

| Part | Required meaning | Authority limit |
|---|---|---|
| `baseline_manifest` | Pinned inputs, source roles, lookback and seasonal windows, parameters, method, tool versions, and recalculation cadence. | Does not admit sources or prove input availability. |
| `cohort_eligibility_report` | Candidate, eligible, excluded, and missing counts plus versioned eligibility and blind-spot declarations. | Does not choose a scientific population or threshold. |
| `discontinuity_records` | Method, instrument, sensor-relocation, or source changes with effective time, evidence, and explicit resolution. | Does not erase or smooth a discontinuity. |
| `baseline_validation_report` | One derived finite state and its review obligation. | `REVIEW_CANDIDATE` is not approval or fitness for a downstream claim. |
| `baseline_rebuild_receipt` | Output and toolchain digests, generation time, predecessor, and correction lineage. | Process memory only; not proof, catalog closure, or release. |

## Finite baseline states

| State | Decision | Required condition |
|---|---|---|
| `REPLAYABLE` | `REVIEW_CANDIDATE` | At least one eligible input; no exclusions, missing inputs, or discontinuities. |
| `QUALIFIED` | `REVIEW_CANDIDATE` | At least one eligible input and every discontinuity resolved, but exclusions, missing inputs, or declared discontinuities require review. |
| `INSUFFICIENT` | `HOLD` | No candidate or no eligible cohort member remains. |
| `DISCONTINUITY_UNRESOLVED` | `HOLD` | At least one method, sensor, instrument, or source discontinuity remains unresolved. |

The validator derives state, decision, required reason, and required obligation. A candidate cannot self-promote by editing those fields. Counts must close exactly, exclusion reason counts must reconcile, discontinuities must be unique and chronological, and rebuild supersession must match the manifest predecessor.

## Identity and validation boundary

`spec_hash` is RFC 8785 JCS plus SHA-256 over the assessment with `assessment_id` and `spec_hash` omitted. `assessment_id` is `kfm:baseline-cohort:<digest>`. Local validation returns `HOLD` for a coherent proposed object and `DENY` for schema, identity, count, temporal, lineage, discontinuity, or authority failures. It does not recompute referenced input or output digests.

## Directory Rules basis

Meaning belongs in `contracts/data/`; machine shape in `schemas/contracts/v1/data/`; validation in `tools/validators/data/`; synthetic cases in `fixtures/contracts/v1/data/`; tests in `tests/data/`; provenance in `data/receipts/generated/`. No new responsibility root, policy home, lifecycle stage, catalog, proof, release, or publication authority is added.

## Non-effects and rollback

This profile performs no network access, retrieves no observation, selects no scientific threshold, calculates no anomaly, changes no source or lifecycle record, and grants no policy, review, release, publication, or public-use authority. Revert the bounded commit to remove the contract, schema, fixtures, validator, tests, workflow, and generated receipt together.
