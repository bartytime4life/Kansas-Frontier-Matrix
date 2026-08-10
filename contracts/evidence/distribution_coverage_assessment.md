<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/distribution-coverage-assessment
title: DistributionCoverageAssessment Contract
type: contract
version: v0.1.0
status: proposed; fixture-first; local-only; non-authoritative
owners: OWNER_TBD — evidence steward; biodiversity domain steward; spatial-foundation steward; validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: repository-facing; distribution; coverage; fail-closed
owning_root: contracts/
responsibility: Preserve source-native distribution status and geography-version context while deriving a bounded coverage decision that never treats a missing row as absence.
truth_posture: cite-or-abstain
related:
  - ../../schemas/contracts/v1/evidence/distribution_coverage_assessment.schema.json
  - ../../tools/validators/evidence/validate_distribution_coverage_assessment.py
  - ../../fixtures/contracts/v1/evidence/distribution_coverage_assessment/cases.json
  - ../../tests/evidence/test_distribution_coverage_assessment.py
  - ../../docs/intake/exploratory/new-ideas-4-30-source-map.md
  - ../../docs/kfm_full_atlas_seed_cards.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "EXPLICITLY_ABSENT means only that the pinned source explicitly reported that status for the bound geography and version; it is not biological absence."
  - "MISSING_ROW, NOT_ASSESSED, UNKNOWN, SUPPRESSED, and STALE never become absence or presence."
  - "The profile is synthetic and fixture-only; domain adoption requires separate source, rights, sensitivity, evidence, and policy review."
[/KFM_META_BLOCK_V2] -->

# DistributionCoverageAssessment

> **Purpose.** Preserve what a source actually reported, the vocabulary and geography version under which it reported it, and whether that report can support a bounded distribution answer. Blank geography and missing rows must never silently become absence.

## Source basis

The reconciled April 30 intake names a contract-only `DistributionAssertion` and `CoverageAssessment` slice as its recommended next bounded action. Full Atlas triad `KFM-TRIAD-046`, especially programming card `KFM-CAND-0138`, calls for source-native status preservation, geography bindings, supersession, and negative fixtures for missing rows, changed boundaries, conflicting sources, and unsupported first-observed dates. This proposed composite is the smallest dependency-closed implementation of that idea; it does not activate a source or create a public distribution layer.

## Finite row and coverage states

| Source row state | Coverage state | Decision | Required boundary |
|---|---|---|---|
| `PRESENT` | `ASSESSED` | `ANSWER` | Reported presence is scoped to the pinned source, geography, vocabulary, and time; it is not abundance. |
| `EXPLICITLY_ABSENT` | `ASSESSED` | `ANSWER` | Reported absence is source-native status only; it is not proof of true absence. |
| `NOT_ASSESSED` | `NOT_ASSESSED` | `ABSTAIN` | Preserve the source's explicit non-assessment. |
| `UNKNOWN` | `UNKNOWN` | `ABSTAIN` | Preserve unresolved source meaning. |
| `SUPPRESSED` | `SUPPRESSED` | `DENY` | Withhold restricted detail and preserve the safe source status. |
| `STALE` | `STALE` | `ABSTAIN` | Do not answer consequentially from expired coverage. |
| `MISSING_ROW` | `MISSING_ROW` | `ABSTAIN` | A missing row is neither presence nor absence. |

An unresolved geography-version change or any declared conflicting assertion overrides an otherwise answerable row with `ABSTAIN`. A reviewed boundary crosswalk may retain the row's finite state, but the crosswalk reference remains visible.

## Geography binding

Every candidate binds a source geography to a canonical geography version. `FIPS` requires a five-digit code. `BOUNDARY_CROSSWALK` requires a crosswalk reference and a `CROSSWALKED` relation. `SOURCE_NATIVE` is permitted only when the source and canonical geography references are identical. `CHANGED` and `UNRESOLVED` relations fail closed until a separate spatial review resolves them.

## Source-native preservation and first-observed dates

Every non-missing row retains `source_native_status`, source vocabulary identity, and source-record identity. `MISSING_ROW` requires both record identity and native status to be null. A `first_observed_at` value is admissible only for `PRESENT` and only when an explicit support reference is supplied. The validator does not infer a first-observed date from a first database appearance.

## Identity and validation boundary

`spec_hash` is RFC 8785 JCS plus SHA-256 over the assessment with `assessment_id` and `spec_hash` omitted. `assessment_id` is `kfm:distribution-coverage:<digest>`. Local validation returns `HOLD` for a coherent proposed object and `DENY` for schema, identity, semantic, geography, conflict, temporal, or authority failures. `HOLD` is not an allow decision.

## Directory Rules basis

Meaning belongs in `contracts/evidence/`; machine shape in `schemas/contracts/v1/evidence/`; validation in `tools/validators/evidence/`; synthetic cases in `fixtures/contracts/v1/evidence/`; tests in `tests/evidence/`; provenance in `data/receipts/generated/`. No new responsibility root, lifecycle stage, policy home, registry, release object, or publication authority is added.

## Non-effects and rollback

This profile performs no network access, fetches no biodiversity records, exposes no coordinates, activates no source, chooses no scientific threshold, creates no occurrence or absence fact, and grants no policy, review, release, publication, or public-use authority. Revert the bounded commit to remove the contract, schema, fixtures, validator, tests, workflow, and generated receipt together.
