<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/distribution-coverage-assessment
title: Distribution Coverage Assessment Candidate Contract
type: contract
version: v0.1.0
status: proposed; fixture-first; local-only; non-authoritative
owners: OWNER_TBD — evidence steward; biodiversity steward; geography steward; validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: repository-facing; distribution-semantics; coverage; fail-closed
owning_root: contracts/
responsibility: Preserve source-native distribution meaning while distinguishing positive presence, explicit absence, missing rows, incomplete assessment, suppression, dispute, staleness, and scope.
truth_posture: cite-or-abstain
related:
  - ../../schemas/contracts/v1/evidence/distribution_coverage_assessment.schema.json
  - ../../fixtures/contracts/v1/evidence/distribution_coverage_assessment/cases.json
  - ../../tools/validators/evidence/validate_distribution_coverage_assessment.py
  - ../../tests/evidence/test_distribution_coverage_assessment.py
  - ../../docs/intake/exploratory/distribution-coverage-semantics-source-map.md
  - ../domains/flora/usda_plants_distribution_snapshot.md
  - ./non_detection_support_assessment.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "A missing row is UNKNOWN, never explicit absence."
  - "Presence is not abundance; explicit source absence is bounded to the declared coverage and is not biological absence."
[/KFM_META_BLOCK_V2] -->

# DistributionCoverageAssessmentCandidate

> **Purpose.** Give reviewers one finite, cross-domain vocabulary for what a source says about distribution and what its declared coverage can support, without replacing source-native records or silently turning blanks into absence.

## Source basis

Full Atlas `KFM-TRIAD-046` and programming card `KFM-CAND-0138` call for `DistributionAssertion`, `CoverageAssessment`, `DistributionStatusProfile`, and `GeographyBinding` semantics. The repository already has a source-specific USDA PLANTS snapshot and a separate non-detection assessment. This proposed composite fills only the common interpretation seam between those families; it does not supersede either contract.

## Finite states

| State | Decision | Required interpretation |
|---|---|---|
| `PRESENT` | `ANSWER` | The source explicitly reports presence for the bound geography. It does not report abundance. |
| `EXPLICITLY_ABSENT` | `ANSWER` | The source explicitly reports absence and declares complete assessment support. It is not biological absence beyond that scope. |
| `NOT_ASSESSED` | `ABSTAIN` | The source does not declare adequate assessment coverage for the requested assertion. |
| `UNKNOWN` | `ABSTAIN` | The row, source-native status, or geography binding is unresolved. A missing row always lands here. |
| `SUPPRESSED` | `DENY` | Distribution detail is intentionally withheld. |
| `DISPUTED` | `ABSTAIN` | One or more preserved assertions conflict. |
| `STALE` | `ABSTAIN` | Coverage or the geography version is no longer current for the assertion. |
| `OUT_OF_SCOPE` | `ABSTAIN` | The subject is outside the declared assessment scope. |

The validator derives the state, decision, required reason, and required obligation. Precedence is suppression, out-of-scope, missing/unresolved geography, stale/superseded coverage, dispute, undeclared assessment, explicit presence, supported explicit absence, then unknown.

## Anti-collapse rules

- `source_row_state = MISSING` derives `UNKNOWN` and `DO_NOT_INFER_ABSENCE`.
- `EXPLICITLY_ABSENT` requires an explicit source-native absence mapping, complete assessment scope, and at least one coverage-effort evidence reference.
- `PRESENT` requires an explicit source-native presence mapping and does not support abundance or density.
- `first_observed` is fixed to `null` in this profile; a distribution row cannot invent an observation date.
- `EXACT` geography binding forbids a crosswalk reference. `CROSSWALKED` and `SUPERSEDED` bindings require one.
- Unresolved, superseded, or withheld boundaries fail closed as `UNKNOWN`, `STALE`, or `SUPPRESSED` respectively.
- Source-native status remains visible; the normalized state never rewrites the source record.

## Identity and validation boundary

`spec_hash` is RFC 8785 JCS plus SHA-256 over the candidate with `assessment_id` and `spec_hash` omitted. `assessment_id` is `kfm:distribution-coverage:<digest>`. A coherent fixture returns local validator outcome `HOLD`, never `ALLOW`. `HOLD` means structurally reviewable only.

## Directory Rules basis

Cross-domain assertion meaning belongs in `contracts/evidence/`; machine shape in `schemas/contracts/v1/evidence/`; synthetic cases in `fixtures/contracts/v1/evidence/`; validation in `tools/validators/evidence/`; tests in `tests/evidence/`; workflow orchestration in `.github/workflows/`; and authoring provenance in `data/receipts/generated/`. No new root, source registry, distribution registry, evidence store, policy home, or release path is created.

## Non-effects and rollback

This profile performs no network request, activates no source, creates no occurrence or biological absence claim, resolves no evidence, chooses no geography authority, evaluates no sensitivity or policy, and grants no review, release, publication, or public-use authority. Revert the dependency-closed candidate commit to remove it.
