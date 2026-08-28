<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/historic-map-scan-lineage-assessment
title: Historic Map Scan Lineage Assessment Candidate
type: semantic-contract
version: v0.1.0
status: proposed; experimental; fixture-only; non-authoritative
owners: OWNER_TBD — Evidence steward · Source steward · Map steward · Rights steward
created: 2026-08-11
updated: 2026-08-11
policy_label: internal; evidence; historic-map; scan-lineage; georeference; fixture-only
owning_root: contracts/
responsibility: Define a bounded synthetic assessment that preserves original-map rights, scan provenance, georeference quality, and derivative-use limits without activating a source, deciding rights, executing georeferencing, admitting evidence, or authorizing release.
truth_posture: PROPOSED source-grounded adaptation / CONFIRMED deterministic synthetic implementation / NEEDS VERIFICATION source rights, operational readers, and steward review
related:
  - ../../schemas/contracts/v1/evidence/historic_map_scan_lineage_assessment.schema.json
  - ../../fixtures/contracts/v1/evidence/historic_map_scan_lineage_assessment/cases.json
  - ../../tools/validators/evidence/validate_historic_map_scan_lineage_assessment.py
  - ../../tests/validators/evidence/test_validate_historic_map_scan_lineage_assessment.py
  - ../../docs/intake/exploratory/pass-18-historic-map-scan-lineage-source-map.md
  - ../map/georeference_control_point_set.md
  - ../map/georeference_transform_quality.md
  - ../source/source_rights_currentness_assessment.md
tags: [kfm, historic-map, scan, provenance, rights, georeference, evidence, fixture-only]
notes:
  - "Implements the smallest dependency-closed slice of Pass 18 card KFM-P18-INV-252."
  - "The candidate records opaque references to existing map and source assessments; it does not replace or execute them."
[/KFM_META_BLOCK_V2] -->

# Historic Map Scan Lineage Assessment Candidate

## Status and purpose

`HistoricMapScanLineageAssessmentCandidate` is a **PROPOSED**,
experimental, fixture-only contract for keeping four facts distinct when a
historic paper or film map becomes a digital map derivative:

1. rights and citation for the original map;
2. provenance for the scan artifact;
3. method and quality evidence for georeferencing; and
4. limits on derivative use.

The contract adapts Pass 18 card `KFM-P18-INV-252`. A validator `PASS` proves
only that one synthetic declaration is internally coherent. It does not prove
that a map, scan, citation, rights review, control-point set, quality
assessment, or EvidenceBundle exists or is trustworthy.

## Preserved distinctions

- **Original map vs. scan.** The original-map reference and scan-artifact
  reference must be different. The original retains its own citation and
  rights review; the scan retains its own source, capture declaration, digest,
  and receipt.
- **Scan vs. georeferenced derivative.** An assessable derivative has a third,
  distinct artifact reference. A raw scan never silently becomes positional
  evidence.
- **Rights vs. geometry quality.** Cleared rights do not establish positional
  accuracy, and an assessable transform does not clear rights.
- **Context vs. evidence.** A derivative may be declared only as
  `CONTEXT_REPRESENTATION`. This candidate always denies
  `POSITIONAL_EVIDENCE` use.
- **Declaration vs. authority.** Source activation, rights decisions,
  georeference execution, evidence admission, release, and publication remain
  false.

## Candidate shape

| Section | Meaning | Required boundary |
|---|---|---|
| `original_map` | Stable original reference, physical/digital format, citation, rights state, and review reference. | A rights label is a declaration, not a legal determination. |
| `scan` | Separate scan reference, provider/source, capture method and time, byte digest, and receipt reference. | The validator never opens or retrieves scan bytes. |
| `georeference` | Status, method, GCP count, existing control-point and quality references, RMS declaration, reality-boundary note, and derivative reference. | References are opaque; existing map contracts retain their authority. |
| `derivative_use` | Requested use, finite permitted uses, explicit limits, representation role, and fixed non-public posture. | Positional-evidence permission and public-use authority are denied. |
| `evidence` | Canonically ordered EvidenceBundle references. | Evidence is referenced, not resolved or admitted. |
| `summary` | Deterministic replay of rights state, georeference state, and permitted-use count. | State remains `REVIEW_REQUIRED`. |
| `governance` | Fixed fixture-only and non-authoritative flags. | No operational effect. |

## Conservative invariants

- citation, rights-review, scan-receipt, and EvidenceBundle references are
  required for a valid declaration;
- evidence references, permitted uses, and derivative-use limits use canonical
  lexical ordering;
- an `ASSESSABLE` georeference requires a non-placeholder method, at least
  three GCPs, a control-point-set reference, a transform-quality reference, an
  RMS declaration, a reality-boundary note, and a distinct derivative;
- `NOT_ATTEMPTED` requires `NONE`, zero GCPs, and no georeference detail;
- `CONTEXT_OVERLAY` requires both `CLEARED` declared rights and an
  `ASSESSABLE` georeference;
- `POSITIONAL_EVIDENCE` is never requested or permitted by a passing
  candidate; and
- identity and summary are recomputed from the complete declaration.

## Finite outcomes

| Outcome | Meaning | Non-effect |
|---|---|---|
| `PASS` | The synthetic lineage declaration is internally coherent. | Still `REVIEW_REQUIRED`; no map or derivative is admitted. |
| `DENY` | Shape, identity, lineage, rights, georeference, use, or boundary invariants fail. | No fallback permission or inferred provenance. |
| `ERROR` | Input or schema cannot be boundedly read. | No partial declaration is trusted. |

## Directory Rules basis

The candidate is an evidence-lineage meaning, so its semantic owner is
`contracts/evidence/`. Machine shape, fixtures, validation, tests, source
adaptation, workflow orchestration, and authoring provenance remain in their
adopted responsibility lanes. Opaque references to
`GeoreferenceControlPointSet`, `GeoreferenceTransformQuality`, and
`SourceRightsCurrentnessAssessment` compose existing owners without creating a
parallel map, source, policy, or receipt authority.

## Non-effects

A green result does not:

- activate or fetch a Library of Congress or other map source;
- open, hash, scan, crop, georeference, transform, render, tile, or publish map
  bytes;
- make a copyright, license, public-domain, or derivative-use decision;
- validate a control point, RMS value, CRS, geometry, or positional accuracy;
- admit evidence, execute policy, approve review, promote, release, deploy, or
  authorize public use.

## Rollback

Before merge, close the draft pull request and remove its branch. After an
authorized merge, revert this additive packet and rerun its dedicated
workflow. No source, map, evidence, release, deployment, or public state
requires restoration.
