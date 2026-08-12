<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/pass-18-georeference-control-point-evidence-source-map
title: Pass 18 georeference control-point evidence assessment — source map
type: intake/exploratory
version: v1
status: draft
owners: map-steward, evidence-steward, docs-steward
created: 2026-08-11
updated: 2026-08-11
policy_label: public
owning_root: docs/
responsibility: Exploratory source-to-repository adaptation record for fixture-only GCP evidence assessment.
truth_posture: Proposed implementation source map; does not create GCP, accuracy, evidence, policy, review, release, publication, or public-use authority.
related:
  - contracts/map/georeference_control_point_evidence_assessment.md
  - contracts/map/georeference_control_point_set.md
  - contracts/map/georeference_spatial_distribution.md
  - contracts/map/georeference_transform_quality.md
tags: [georeference, gcp, photogrammetry, evidence, pass-18, intake, exploratory]
notes: Source-backed, fixture-only adaptation of KFM-P18-INV-317.
[/KFM_META_BLOCK_V2] -->

# Pass 18 georeference control-point evidence assessment — source map

## Source evidence

**CONFIRMED:** Pass 18 idea card `KFM-P18-INV-317`, “GCP distribution and visibility as photogrammetry evidence quality,” proposes recording GCP count, distribution, visibility, contrast, RTK/GNSS source, and matching method as evidence-quality fields. The card appears on physical PDF pages 329–330 (printed pages 326–327) of `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, locally verified with SHA-256 `efc0d159761581b5ae043c607dfa28bbc58b3ca5423c9d18a659e650271d73b9`.

**CONFIRMED:** The card cites `SRC-P18-010`, *Earth, Space, and Environmental Science Explorations with ArcGIS Pro ed2.pdf*, pages 85–86. The connected Google Drive item was verified as file ID `11GH5lYaa-lqXDKhG20GmiSetFgh5VWx3`. Its readable text says GCP targets should be large, clear, and high-contrast; describes collecting their coordinates with a high-accuracy unit such as RTK GPS; and describes matching those coordinates to target locations in drone photographs.

**UNKNOWN:** Neither source proves that the proposed KFM profile is used at runtime or that any real GCP evidence is accurate, admissible, rights-cleared, reviewed, released, or public-safe.

## Repository gap and collision check

**CONFIRMED:** The repository already separates three adjacent responsibilities:

- `GeoreferenceControlPointSet` owns deterministic point-set identity and coordinates;
- `GeoreferenceSpatialDistribution` owns image-space distribution metrics; and
- `GeoreferenceTransformQuality` owns transform residual quality.

**CONFIRMED:** Repository and pull-request searches performed before authoring found no profile or active proposal for GCP marker visibility, contrast, surveyed-coordinate provenance, and image-matching review as one evidence assessment.

## Adaptation

**PROPOSED:** Add an inactive `GeoreferenceControlPointEvidenceAssessmentCandidate` that binds an existing control-point-set identity and records only the missing qualitative evidence fields. It repeats point IDs, not coordinates, and records deterministic counts and identity so fixture behavior is auditable.

The profile uses four outcomes:

- `PASS`: internally coherent synthetic declarations are ready for human review;
- `ABSTAIN`: evidence is unknown, partial, or unreviewed;
- `DENY`: the candidate declares an adverse state or violates internal coherence; and
- `ERROR`: input, schema, or deterministic identity is invalid.

These outcomes do not establish a public-geometry adequacy threshold. The atlas explicitly leaves that threshold as an open question.

## Directory placement

**CONFIRMED:** `docs/doctrine/directory-rules.md`, adopted by `docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md`, requires responsibility-aligned placement and reuse of existing roots. This packet therefore places semantics in `contracts/map/`, machine shape in `schemas/contracts/v1/map/`, examples in `fixtures/contracts/v1/map/`, executable checking in `tools/validators/map/`, tests in `tests/map/`, CI orchestration in `.github/workflows/`, this adaptation record in `docs/intake/exploratory/`, and authoring provenance in `data/receipts/generated/`.

## Deliberate limits

This proposal does not dereference inputs, open images, inspect pixels, contact a positioning service, verify coordinates, duplicate distribution or transform metrics, determine positional accuracy, evaluate rights/CARE/policy, approve review, register a runtime component, mutate data, or authorize release, publication, or public use.

## Follow-up candidates

1. **NEEDS VERIFICATION:** A later policy proposal may define context-specific adequacy thresholds, but only with domain review and explicit public-geometry safeguards.
2. **NEEDS VERIFICATION:** A separately reviewed adapter may project evidence from a governed `EvidenceBundle` into this assessment without giving the adapter evidence authority.
3. **NEEDS VERIFICATION:** Future compatibility work may bind this assessment and `GeoreferenceSpatialDistribution` to the same `resource_set_hash` without merging their responsibilities.
