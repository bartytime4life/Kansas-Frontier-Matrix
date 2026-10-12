<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/pass-18-geometry-quality-scope-assessment-source-map
title: Pass 18 geometry quality scope assessment — source map
type: intake/exploratory
version: v1
status: draft
owners: evidence-steward, spatial-representation-steward, validation-steward
created: 2026-08-11
updated: 2026-08-11
policy_label: public
owning_root: docs/
responsibility: Exploratory source-to-repository adaptation record for fixture-only accuracy, precision, provenance, derivation, and quality-scope assessment.
truth_posture: Proposed implementation source map; no geometry truth, evidence, fitness, policy, review, release, publication, or public-use authority.
related:
  - contracts/evidence/geometry_quality_scope_assessment.md
  - contracts/evidence/representation_fitness_assessment.md
  - contracts/common/identifier_precision_lineage_assessment.md
  - contracts/evidence/field_capture_evidence_handoff.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [geometry, accuracy, precision, provenance, evidence, pass-18, intake, exploratory]
notes: Source-backed, fixture-only adaptation of KFM-P18-INV-052.
[/KFM_META_BLOCK_V2] -->

# Pass 18 geometry quality scope assessment — source map

## Source evidence

**CONFIRMED:** Pass 18 card `KFM-P18-INV-052`, “Accuracy and precision split for observations and geometry,” was visually inspected on physical PDF pages 35–36 (printed pages 32–33) of the supplied `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, SHA-256 `efc0d159761581b5ae043c607dfa28bbc58b3ca5423c9d18a659e650271d73b9`.

The card proposes:

- keeping accuracy and precision separate for surveyed, GPS-derived, digitized, and remotely sensed geometry;
- recognizing that a precise coordinate can still be wrong;
- allowing public generalization to reduce precision intentionally when fitness and accuracy remain clear;
- adding `accuracy_class` and `precision_class` with source-method provenance; and
- resolving whether quality belongs on every feature or can be inherited from dataset-level metadata.

**CONFIRMED:** Google Drive metadata identifies a same-titled dossier at file ID `1ww-h3abQkxXeBvSxO5YV6_yvsZ9Wn1P5`. Its reported byte size differs from the supplied local PDF, so this source map does not claim byte identity or substitute the Drive item for the visually inspected attachment.

**CONFIRMED:** The card cites `SRC-P18-002`, *a-primer-of-gis-fundamental-geographic-and-cartographic-concepts.pdf*, pages 150 and 161, as support for the surveying/GPS/digitization and accuracy-versus-precision concept. The source citation supports the planning concept; it does not prove KFM runtime behavior or real geometry quality.

## Repository gap and collision check

**CONFIRMED:** The implementation base was `main@ded9a9755316fee97827d5d65b8fc26e31c2ae4b`. Current-tree, history, branch, and pull-request searches were reviewed before authoring.

**CONFIRMED:** Adjacent implemented responsibilities already exist:

- `RepresentationFitnessAssessment` owns use-specific representation fitness and rejects declared precision finer than nominal resolution;
- `IdentifierPrecisionLineageAssessment` owns identifier crosswalk outcomes and effective precision after generalization, aggregation, or withholding;
- `FieldCaptureEvidenceHandoffAssessment` owns capture-metadata readiness, including an accuracy class; and
- map georeference profiles own control points, distribution, transform residuals, and GCP evidence.

**CONFIRMED:** None of those profiles models dataset inheritance versus per-feature quality overrides while also keeping accuracy and precision as independent declarations with derivation effects. No exact `KFM-P18-INV-052` implementation or active matching pull request was found.

## Adaptation

**PROPOSED:** Add one inactive `GeometryQualityScopeAssessmentCandidate` that supports `DATASET_INHERITED`, `FEATURE_EXPLICIT`, `MIXED_OVERRIDE`, and `UNKNOWN` attachment modes. Every quality record carries separate accuracy and precision classes, acquisition and observation-method provenance, opaque subject identity, geometry revision, and bounded derivation lineage.

The validator intentionally permits fine precision with coarse accuracy. It prevents derived records from claiming finer quality than their input, requires declared effects to match class changes, and treats generalization as a lineage event rather than an accuracy upgrade. Disclosure bands remain fixture vocabulary, not universal scientific thresholds.

`PASS` means internal coherence and readiness for a separate human fitness review. Unresolved or withheld quality yields `ABSTAIN`; contradictory scope or derivation yields `DENY`; malformed or identity-tampered input yields `ERROR`.

## Directory placement

**CONFIRMED:** Accepted Directory Rules and ADR-0029 place spatial evidence semantics under `contracts/evidence/`, machine shape under `schemas/contracts/v1/evidence/`, fixtures under `fixtures/contracts/v1/evidence/`, reusable checks under `tools/validators/evidence/`, tests under `tests/evidence/`, orchestration under `.github/workflows/`, exploratory adaptation under `docs/intake/exploratory/`, and generated-work provenance under `data/receipts/generated/`.

`contracts/map/` remains a compatibility/orientation root whose README warns against absorbing map-facing concepts merely because they appear on a map. Evidence responsibility therefore controls placement here.

## Deliberate limits

This proposal carries no coordinates, raw feature identifiers, uncertainty geometry, real thresholds, or source payload. It does not resolve references, measure accuracy or precision, execute a transform, authenticate provenance, decide fitness, create evidence, decide rights or policy, approve review, mutate lifecycle state, release, deploy, publish, or authorize public use.

## Follow-up candidates

1. **NEEDS VERIFICATION:** Evidence and spatial-representation stewards should review the disclosure-band vocabulary before any non-fixture adoption.
2. **NEEDS VERIFICATION:** A future adapter may bind an accepted geometry-quality profile to `RepresentationFitnessAssessment` without merging quality declaration and use-specific fitness decisions.
3. **NEEDS VERIFICATION:** Large datasets need a scalable manifest or partition-level binding; this bounded fixture profile intentionally caps feature-explicit examples at 256 records.
