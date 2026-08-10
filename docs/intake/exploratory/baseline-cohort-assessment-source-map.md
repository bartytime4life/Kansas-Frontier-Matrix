<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/baseline-cohort-assessment-source-map
title: Baseline Cohort Assessment Source Map
type: exploratory-source-map
version: v1.0.0
status: proposed; review-pending
owners: OWNER_TBD — Atlas steward · Data steward · Domain steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; exploratory; source-grounded; non-authoritative
owning_root: docs/
responsibility: source-grounded mapping from baseline cohort and drift candidates to bounded repository artifacts without treating proposal cards as implementation evidence or authority
truth_posture: CONFIRMED candidate transcription and repository comparison / PROPOSED bounded adaptation pending steward review / NEEDS VERIFICATION hosted exact-head execution
related:
  - ../../../contracts/data/baseline_cohort_assessment.md
  - ../../kfm_full_atlas_seed_cards.md
  - ./new-ideas-4-16-source-map.md
  - ../../../docs/doctrine/directory-rules.md
tags: [kfm, atlas, baseline, cohort, discontinuity, source-map]
[/KFM_META_BLOCK_V2] -->

# Baseline Cohort Assessment Source Map

## Source cards

| Card | Retained proposal | Bounded implementation |
|---|---|---|
| `KFM-TRIAD-036` | Make baseline meaning inspectable through cohort, window, method, missingness, and discontinuity declarations. | One fixture-only cohort assessment with exact inputs, exclusions, holds, and finite outcomes. |
| `KFM-CAND-0106` | Treat eligibility, exclusions, windows, missingness, method continuity, relocation, uncertainty, and cadence as baseline meaning. | Valid-time, recorded-time, method, missingness, evidence, disposition, and discontinuity invariants. |
| `KFM-CAND-0107` | Provide reviewer-readable coverage, exclusions, discontinuities, versions, and blind spots. | Deterministic candidate/discontinuity inventories and summary; no production UI. |
| `KFM-CAND-0108` | Define manifest, eligibility, discontinuity, validation, and rebuild artifacts with digest-bound inputs. | One narrow assessment references method and prior-baseline authorities; it does not create validation or rebuild authority. |

The Full Atlas and Drive-derived `New Ideas 4-16-26` source map are candidate evidence, not implementation authority. The packet excludes observation values, baseline statistics, thresholds, and anomaly conclusions.

## Repository reconciliation

- Source descriptors and observations remain under their existing authorities.
- Domain anomaly and threshold contracts remain downstream and must reference an exact accepted baseline version separately.
- Correction, policy, review, release, and publication families retain their current responsibilities.
- Repository search at base `9e76413313b8529091d01be6132d6e987e3f9fae` found baseline vocabulary in domain fixtures but no common `BaselineManifest`, `CohortEligibilityReport`, `DiscontinuityRecord`, `BaselineValidationReport`, or `BaselineRebuildReceipt` assessment family outside proposal material.

## Path decision

```yaml
path_decision:
  artifact: BaselineCohortAssessmentCandidate
  proposed_path: contracts/data/baseline_cohort_assessment.md
  artifact_kind: semantic contract
  authority_owner: baseline input lifecycle and provenance declaration
  lifecycle_stage: data
  execution_role: none
  scope_kind: object_family
  scope_id: baseline-cohort
  exposure: internal
  mutability: versioned
  evidence:
    - docs/doctrine/directory-rules.md
    - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
    - docs/kfm_full_atlas_seed_cards.md
    - docs/intake/exploratory/new-ideas-4-16-source-map.md
  rules:
    - DIR-SIGNATURE-001
    - DIR-AUTHROOT-001
    - DIR-SCOPELANE-004
    - DIR-DATALIFE-001
    - DIR-DEP-001
  outcome: PLACE
```

## Non-effects

This packet does not fetch source data, store observation values, calculate or rebuild a baseline, evaluate an anomaly, infer drift or materiality, mutate data, authenticate evidence or review, evaluate policy, promote, release, deploy, publish, or authorize public use.
