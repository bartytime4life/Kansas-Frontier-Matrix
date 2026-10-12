# GeometryQualityScopeAssessment

`GeometryQualityScopeAssessmentCandidate` is an inactive, fixture-only profile for keeping geometric accuracy, coordinate precision, acquisition method, derivation lineage, and quality-attachment scope separate. It implements the narrow design gap in Pass 18 card `KFM-P18-INV-052` without asserting that any real geometry is accurate.

## Purpose

A coordinate may be recorded with fine precision and still be far from the real-world location. A generalized public geometry may intentionally use coarser precision while remaining appropriate for a declared use. This assessment makes those distinctions reviewable and answers the Pass 18 open question about per-feature versus dataset-level quality by supporting three explicit scopes:

| Scope | Required record pattern |
|---|---|
| `DATASET_INHERITED` | One dataset quality record applies to every feature. |
| `FEATURE_EXPLICIT` | One quality record is present for every feature in the bounded fixture. |
| `MIXED_OVERRIDE` | One dataset record supplies the default and one or more feature records supply explicit overrides. |
| `UNKNOWN` | No quality record is claimed; validation abstains. |

The profile does not require feature-level duplication when a versioned dataset profile is honest, and it does not allow an override to exist without an explicit subject and provenance.

## Accuracy and precision

Each quality record carries independent `accuracy_class` and `precision_class` values. The shared labels are disclosure bands, not universal scientific thresholds or policy. The validator deliberately permits a fine precision class with a coarse accuracy class; it never infers one from the other.

Known quality requires an acquisition method, observation-method reference, and provenance reference. `UNKNOWN` and `WITHHELD` remain explicit finite states. No numeric coordinate, uncertainty geometry, or sensitive feature identity is stored; subjects are SHA-256 digests.

## Derivation rules

`NONE` carries no input classes or transform receipt. `REPROJECTED`, `GENERALIZED`, and `AGGREGATED` require an input-quality reference, input accuracy and precision classes, and a transform receipt. A derived output cannot claim finer accuracy or precision than its input. The declared effect must match the class change. `WITHHELD` requires withheld output classes and a receipt.

These checks prove declaration coherence only. They do not run a transform, measure residuals, inspect coordinates, or decide whether a band is fit for a use.

## Finite validator outcomes

- `PASS`: attachment scope, quality records, provenance, summary, derivation, and identity are internally coherent and ready for human fitness review.
- `ABSTAIN`: scope, accuracy, precision, method, provenance, or withheld state is unresolved without an adverse contradiction.
- `DENY`: attachment scope, lineage, derivation effect, canonical ordering, or recommendation is contradictory.
- `ERROR`: input shape or deterministic identity is invalid.

Every stored review state remains `HOLD`. A pass is not evidence, review approval, policy permission, release, publication, or public-use authority.

## Adjacent-family boundary

- `RepresentationFitnessAssessment` continues to decide use-specific support across positional, thematic, temporal, completeness, and lineage dimensions.
- `IdentifierPrecisionLineageAssessment` continues to own identifier crosswalk and effective precision after privacy transforms.
- `FieldCaptureEvidenceHandoffAssessment` continues to own capture-to-evidence handoff readiness.
- Georeference control-point and transform-quality profiles continue to own their specialized observations.

This profile owns only accuracy/precision separation, attachment scope, and declared derivation coherence.

## Deterministic identity

`spec_hash` is SHA-256 over canonical JSON after removing only `assessment_id` and `spec_hash`. `assessment_id` is the first 24 digest characters prefixed with `geometry-quality-scope:`. Quality records are unique and ordered by `(subject_kind, subject_ref_digest)`; summaries are recomputed.

## Directory Rules basis

This object assesses spatial evidence metadata, so meaning belongs in `contracts/evidence/`; shape in `schemas/contracts/v1/evidence/`; fixtures in `fixtures/contracts/v1/evidence/`; validation in `tools/validators/evidence/`; tests in `tests/evidence/`; orchestration in `.github/workflows/`; source adaptation in `docs/intake/exploratory/`; and generated-work provenance in `data/receipts/generated/`. These are existing responsibility roots adopted by ADR-0029.

## Rollback

Before merge, close the draft pull request and remove its branch. After an authorized merge, revert this additive packet and rerun its focused workflow. No geometry, evidence, lifecycle data, release, deployment, cache, or public surface requires restoration.
