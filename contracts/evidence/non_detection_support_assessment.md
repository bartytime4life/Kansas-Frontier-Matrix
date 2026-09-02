<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/non-detection-support-assessment
title: NonDetectionSupportAssessment Contract
type: contract
version: v0.1.0
status: proposed; fixture-first; local-only; non-authoritative
owners: OWNER_TBD — evidence steward; domain sampling steward; privacy steward; validation steward
created: 2026-08-09
updated: 2026-08-09
policy_label: repository-facing; sampling-effort; non-detection; fail-closed
owning_root: contracts/
responsibility: Determine whether a detection or non-detection statement is coherent with one declared sampling event and detection opportunity.
truth_posture: cite-or-abstain
related:
  - ../../schemas/contracts/v1/evidence/non_detection_support_assessment.schema.json
  - ../../tools/validators/evidence/validate_non_detection_support_assessment.py
  - ../../fixtures/contracts/v1/evidence/non_detection_support_assessment/cases.json
  - ../../tests/evidence/test_non_detection_support_assessment.py
  - ../../docs/intake/exploratory/full-atlas-nondetection-support-source-map.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "SUPPORTED_NON_DETECTION means only that a declared target was not detected within the declared effort. It never means biological absence."
  - "The profile is synthetic and fixture-only; domain adoption requires separate policy, privacy, and evidence review."
[/KFM_META_BLOCK_V2] -->

# NonDetectionSupportAssessment

> **Purpose.** Keep sampling effort, detection opportunity, and the resulting bounded statement together so missing or incompatible effort cannot silently become an absence claim.

## Source basis

`KFM-TRIAD-045` and programming card `KFM-CAND-0135` in the Full Atlas call for reusable `SamplingEvent`, `DetectionOpportunity`, `EffortProfile`, and `NonDetectionAssertion` semantics with negative fixtures. This proposed composite is the smallest dependency-closed implementation of that idea. It does not replace domain-specific event records or activate a new source.

## Finite assertion states

| State | Decision | Required meaning |
|---|---|---|
| `OBSERVED_DETECTION` | `ANSWER` | A positive count is declared for this event; any broader occurrence claim still needs its own evidence review. |
| `SUPPORTED_NON_DETECTION` | `ANSWER` | Zero detections under complete, current, in-scope, suitable, and season-supported effort. This is not absence. |
| `NOT_SAMPLED` | `ABSTAIN` | No usable duration or observer/instrument effort is declared. |
| `INCOMPLETE_EFFORT` | `ABSTAIN` | An event exists, but its checklist or detection opportunity is incomplete or inadequate. |
| `UNKNOWN_EFFORT` | `ABSTAIN` | Method, season, or opportunity support remains unknown. |
| `SUPPRESSED_RESULT` | `DENY` | Restricted event detail is withheld and a declared privacy transform is required. |
| `STALE_COVERAGE` | `ABSTAIN` | The declared sampling coverage is not current for the requested statement. |

The validator derives the state, decision, required reason, and required obligation. A candidate cannot self-promote by changing those fields. Restricted events fail closed unless `privacy_transform_ref` is present, and their fixture result remains suppressed even when a transform is declared.

## Identity and validation boundary

`spec_hash` is RFC 8785 JCS plus SHA-256 over the assessment with `assessment_id` and `spec_hash` omitted. `assessment_id` is `kfm:non-detection-support:<digest>`. Local validation returns `HOLD` for a coherent proposed object and `DENY` for schema, identity, semantic, privacy, or authority failures. `HOLD` is not an allow decision.

## Directory Rules basis

Meaning belongs in `contracts/evidence/`; machine shape in `schemas/contracts/v1/evidence/`; validation in `tools/validators/evidence/`; synthetic cases in `fixtures/contracts/v1/evidence/`; tests in `tests/evidence/`; provenance in `data/receipts/generated/`. No root, lifecycle, or release authority is added.

## Non-effects and rollback

This profile creates no observation or evidence, performs no network access, discloses no coordinates, activates no source, and grants no policy, review, release, publication, or public-use authority. Revert the bounded commit to remove it.
