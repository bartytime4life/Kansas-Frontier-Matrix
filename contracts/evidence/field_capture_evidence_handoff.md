<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/field-capture-evidence-handoff
title: FieldCaptureEvidenceHandoffAssessment Candidate Contract
type: semantic-contract
version: v0.1.0
status: proposed; inactive; fixture-only; review-required
owners: OWNER_TBD — Evidence steward · Field-capture steward · Geospatial steward · Sensitivity reviewer · Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; evidence; field-capture; geoprivacy; no-network
owning_root: contracts/
responsibility: Define a bounded assessment of field-capture metadata readiness for EvidenceBundle handoff without promoting a capture candidate, resolving references, deciding policy, approving review, or authorizing release or publication.
truth_posture: CONFIRMED repository candidate and contract seams / PROPOSED inactive fixture profile / NEEDS VERIFICATION steward adoption and hosted exact-head execution
related:
  - ./evidence_bundle.md
  - ../source/source_descriptor.md
  - ../source/ingest_receipt.md
  - ../map/georeference_transform_quality.md
  - ../../schemas/contracts/v1/evidence/field_capture_evidence_handoff.schema.json
  - ../../fixtures/contracts/v1/evidence/field_capture_evidence_handoff/cases.json
  - ../../tools/validators/evidence/validate_field_capture_evidence_handoff.py
  - ../../tests/validators/evidence/test_validate_field_capture_evidence_handoff.py
  - ../../docs/intake/exploratory/field-capture-evidence-handoff-source-map.md
tags: [kfm, evidence, field-capture, gnss, manual-point, drone, lidar, photogrammetry, geoprivacy, handoff, fixture-only]
notes:
  - "Adapts the public Full Atlas field-and-3D-capture governance candidates into a narrow evidence-handoff assessment."
  - "A PASS means only that declared metadata is internally coherent for a review handoff; it does not create or authenticate an EvidenceBundle."
[/KFM_META_BLOCK_V2] -->

# FieldCaptureEvidenceHandoffAssessment Candidate

> A deterministic, fixture-only boundary between a field-capture candidate and
> an evidence workflow. It records whether acquisition, processing, geometry,
> rights, sensitivity, revision, analyst, review, and evidence references are
> coherent enough for handoff without treating the capture as evidence or
> public-safe output.

## Purpose

The repository already defines `SourceDescriptor`, ingest receipts,
`EvidenceBundle`, georeference quality, sensitivity, policy, review, and release
families. The missing seam is a small object that keeps a capture candidate from
becoming an orphan observation or silently becoming evidence.

The assessment carries only opaque references and bounded classifications:

- capture kind and acquisition method;
- acquisition and assessment time;
- source, analyst, and revision references;
- exact-restricted, generalized-public, or withheld geometry posture;
- geometry, CRS, accuracy, processing, and georeference references;
- rights and sensitivity posture;
- an authorization reference for drone captures, without encoding live legal
  or regulatory claims;
- EvidenceBundle and review references; and
- finite `PASS`, `ABSTAIN`, or `DENY` disposition.

It contains no coordinates, source payload, imagery, point cloud, model, scene,
credentials, personal identity, or legal conclusion.

## Capture kinds and acquisition methods

| Capture kind | Required acquisition method |
|---|---|
| `FIELD_OBSERVATION` | `HUMAN_RECORDED` |
| `GNSS_POINT` | `GNSS_RECEIVER` |
| `MANUAL_POINT` | `MANUAL_MAP_PLACEMENT` |
| `DRONE_CAPTURE` | `UAS_SENSOR` |
| `PHOTOGRAMMETRY` | `CAMERA_RIG` |
| `LIDAR` | `LIDAR_SENSOR` |

The manual-point and GNSS-point classes remain distinct. A manually placed point
cannot inherit device accuracy by naming itself GNSS, and a GNSS capture cannot
erase its acquisition method.

## Geometry posture

| Posture | Required closure | Forbidden collapse |
|---|---|---|
| `EXACT_RESTRICTED` | Opaque geometry and CRS refs, resolved accuracy class, georeference-validation ref, `SENSITIVE` posture. | No public-transform claim or public-safe classification. |
| `GENERALIZED_PUBLIC` | Opaque geometry and CRS refs, resolved accuracy class, georeference-validation ref, public-transform receipt, `PUBLIC_SAFE` posture. | No generalized-public label without transform lineage. |
| `WITHHELD` | No geometry ref and no public-transform receipt. | No hidden exact geometry reference in the assessment. |

Raw coordinate fields are outside the closed schema. This fixture profile does
not evaluate whether a real geometry is correct, sufficiently generalized, or
lawfully publishable.

## Finite disposition

| Outcome | Handoff state | Meaning |
|---|---|---|
| `PASS` | `READY` | Rights are verified, sensitivity is resolved, required spatial metadata is coherent, an EvidenceBundle ref is declared, review is approved, and any drone authorization ref is present. |
| `ABSTAIN` | `HELD` | One or more required handoff dimensions remain unresolved. No fallback evidence claim is invented. |
| `DENY` | `DENIED` | Rights or review is explicitly denied, or the candidate violates the closed shape or semantic boundary. |
| `ERROR` | none | The bounded file operation could not complete safely; `ERROR` is a validator envelope outcome, not a stored assessment decision. |

`READY` does not mean evidence was created. Opaque references are not resolved or
authenticated, and the governance block fixes evidence creation, policy,
review, lifecycle, release, and publication authority to false.

## Deterministic identity

The validator computes RFC 8785 JCS plus SHA-256 over the full object after
removing only `assessment_id` and `spec_hash`.

```text
spec_hash      = SHA-256(JCS(identity subject))
assessment_id  = kfm:field-capture-handoff:<first 24 digest hex>
```

Stored disposition, content identity, timestamps, capture metadata, opaque
references, limitations, and governance claims are bound together. Drift fails
closed.

## Directory Rules basis

This object assesses readiness at the evidence boundary, so semantic meaning
belongs under `contracts/evidence/`; shape under
`schemas/contracts/v1/evidence/`; synthetic cases under
`fixtures/contracts/v1/evidence/`; reusable validation under
`tools/validators/evidence/`; executable checks under
`tests/validators/evidence/`; read-only orchestration under `.github/workflows/`;
source adaptation under `docs/intake/exploratory/`; and authoring accountability
under `data/receipts/generated/`.

These are existing responsibility roots adopted by ADR-0029. No field system,
source registry, evidence store, policy home, review queue, map surface, public
API, release lane, or publication path is created.

## Validation

```bash
python -m pytest -q tests/validators/evidence/test_validate_field_capture_evidence_handoff.py
python tools/validators/evidence/validate_field_capture_evidence_handoff.py --fixtures
```

## Non-effects and rollback

A passing fixture proves only local structural and semantic consistency. It does
not capture data, process coordinates, verify a person or device, determine
survey quality, validate a flight or authorization, resolve a source, create
evidence, authenticate review, decide policy, change lifecycle state, release,
deploy, or publish.

Before merge, close the draft pull request and delete its branch. After an
authorized merge, revert the additive packet. No live capture, evidence, policy,
review, lifecycle, release, deployment, or public artifact requires operational
rollback.
