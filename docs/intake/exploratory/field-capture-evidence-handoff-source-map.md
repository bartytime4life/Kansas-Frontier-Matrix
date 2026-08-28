<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/field-capture-evidence-handoff-source-map
title: Field-Capture Evidence-Handoff Source Map
type: intake-source-map
version: v1.0
status: proposed; fixture-only; repository-grounded
owner: OWNER_TBD
created: 2026-08-10
updated: 2026-08-10
policy_label: public
owning_root: docs/
responsibility: Map a bounded field-capture evidence-handoff assessment to repository-resident evidence without exposing private research, creating evidence, or granting policy, review, release, or publication authority.
truth_posture: CONFIRMED repository candidate and contract seams / PROPOSED fixture-only assessment / NEEDS VERIFICATION human review and hosted CI
related: [contracts/evidence/field_capture_evidence_handoff.md, contracts/evidence/evidence_bundle.md, contracts/source/source_descriptor.md, contracts/map/georeference_transform_quality.md, docs/kfm_full_atlas_seed_cards.md, docs/doctrine/directory-rules.md, docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md]
tags: [kfm, intake, field-capture, evidence, handoff, geoprivacy, fixture]
notes: [Private research was used only for candidate discovery. Public provenance intentionally excludes private document identifiers and copied private content.]
[/KFM_META_BLOCK_V2] -->

# Field-capture evidence-handoff source map

## Status

This map records why a narrow, fixture-only assessment is proposed at the seam
between a field-capture candidate and an evidence workflow. It is not a field
system, source record, capture receipt, EvidenceBundle, policy decision, review
record, release manifest, or publication record.

## Repository evidence

| Evidence | Confirmed observation | Bounded implementation response |
|---|---|---|
| `docs/kfm_full_atlas_seed_cards.md`, KFM-CAND-0082 | The public atlas proposes acquisition, processing, interpretation, and sensitivity metadata for field, remote-sensing, 3D, LiDAR, terrain, and drone evidence carriers. | Carry a small capture-kind, acquisition, processing, geometry, rights, and sensitivity surface. |
| `docs/kfm_full_atlas_seed_cards.md`, KFM-CAND-0084 | The public atlas proposes capture receipts, source descriptors, georeferencing validators, and sensitivity gates for exact or high-resolution outputs. | Require opaque source, processing, georeference, and transform refs while leaving those object families independent. |
| `contracts/source/source_descriptor.md` | SourceDescriptor owns source role, rights, sensitivity, access, and admission posture. | Reference a descriptor; do not copy or override it. |
| `contracts/source/ingest_receipt.md` | IngestReceipt records capture/ingest process memory and remains distinct from evidence. | Reference processing memory; do not redefine an ingest receipt. |
| `contracts/evidence/evidence_bundle.md` | EvidenceBundle is a claim-scope closure artifact and is not policy, review, release, or publication authority. | Require an opaque bundle ref for `READY` while creating and resolving no bundle. |
| `contracts/map/georeference_transform_quality.md` | Georeference fit quality is distinct from evidence, rights, sensitivity, review, and release. | Require an opaque validation ref for spatial candidates without performing a transform. |
| Directory Rules and accepted ADR-0029 | Meaning, machine shape, fixtures, validation, tests, CI, intake mapping, and receipts have separate responsibility roots. | Place every artifact in its existing owner root and create no parallel authority home. |

## Adapted semantics

- Every assessed capture remains `CANDIDATE`.
- GNSS and manually placed points remain distinct acquisition classes.
- Exact geometry remains restricted and sensitive.
- A generalized-public claim requires public-transform lineage.
- Withheld posture carries no geometry reference.
- Drone records carry only an opaque authorization reference; no live legal or
  regulatory fact is encoded or verified.
- `PASS` means metadata-ready for a review handoff, never evidence creation.
- Unresolved rights, sensitivity, review, or evidence state yields `ABSTAIN`.

## Explicit non-effects

Validation does not:

- capture, read, transform, generalize, or publish coordinates, images, point
  clouds, scenes, or source payloads;
- contact a device, network, source, registry, reviewer, or authorization system;
- resolve or authenticate an opaque reference;
- create SourceDescriptor, receipt, EvidenceRef, EvidenceBundle, proof, policy,
  review, lifecycle, release, or publication objects; or
- authorize a map, 3D view, API, export, AI answer, deployment, or public use.

## Deferred work

- Accepted runtime capture and processing object families.
- Real device, analyst, revision, georeference, rights, sensitivity, and
  authorization resolvers.
- Domain-specific accuracy, survey, dimensional, and interpretation profiles.
- Policy, review, evidence, correction, rollback, release, API, map, and 3D
  consumers.

Those changes require separate dependency-closed review and are not implied by
a passing fixture workflow.
