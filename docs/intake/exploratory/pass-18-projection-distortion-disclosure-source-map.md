<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-18-projection-distortion-disclosure-source-map
title: Pass 18 Projection Distortion Disclosure Source Map
type: source-map
version: v1.0.0
status: exploratory; implementation-mapped; non-authoritative
owners: OWNER_TBD — Intake steward · Evidence steward · Cartography steward · Spatial-reference steward
created: 2026-08-10
updated: 2026-08-10
owning_root: docs/
policy_label: internal; exploratory; source-reconciliation; projection; distortion
responsibility: Reconcile one supplied projection-distortion disclosure idea with current repository evidence while withholding private discovery-source identifiers from public provenance.
truth_posture: "CONFIRMED supplied-card and repository gap; PROPOSED inactive implementation profile; UNKNOWN consumer adoption and cartographic fitness; NEEDS VERIFICATION human review and hosted CI"
related:
  - ../../../contracts/evidence/projection_distortion_disclosure.md
  - ../../../contracts/evidence/representation_fitness_assessment.md
  - ../../../contracts/data/cartographic_omission_disclosure.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, intake, pass-18, projection, distortion, cartography]
[/KFM_META_BLOCK_V2] -->

# Pass 18 Projection Distortion Disclosure Source Map

## Source and gap

| Evidence | Observation | Status |
|---|---|---|
| Supplied Pass 18 card `KFM-P18-INV-426` | Statewide or regional map claims should disclose projection choice and material distortion risks when transformation choices can affect interpretation. | `CONFIRMED` source statement |
| `contracts/evidence/representation_fitness_assessment.md` | Existing representation fitness semantics bind CRS and spatial support to intended use, but do not provide a projection-specific four-dimension disclosure. | `CONFIRMED` adjacent contract |
| `contracts/data/cartographic_omission_disclosure.md` | Existing cartographic disclosure covers omission, simplification, and emphasis rather than projection distortion. | `CONFIRMED` adjacent contract |
| Starting `main@7301a90ff528b7f620c22e57a2b624cbca45e570` search | No exact card ID, projection-distortion disclosure profile, fixture family, validator, workflow, branch, or matching pull request was found before implementation. | `CONFIRMED` bounded gap |
| Connected private research corpus | Used for candidate discovery and corroboration. Private file identifiers, URLs, and copied prose are intentionally excluded. | `CONFIRMED` provenance boundary |

## Adaptation

The implementation is a closed, synthetic declaration under the existing evidence family. It composes candidate layer, EvidenceBundle, area-of-use, transformation, distortion-assessment, review, and Evidence Drawer identities by opaque reference. The validator checks authored coherence only and never infers a projection's fitness or computes distortion.

## Directory Rules basis

The packet uses existing responsibility roots: semantic meaning in `contracts/evidence/`, shape in `schemas/contracts/v1/evidence/`, synthetic replay in `fixtures/contracts/v1/evidence/`, validation in `tools/validators/evidence/`, conformance evidence in `tests/validators/evidence/`, orchestration in `.github/workflows/`, this reconciliation in `docs/intake/exploratory/`, and authoring accountability in `data/receipts/generated/`.

No CRS registry, coordinate service, layer registry, evidence store, policy rule, release record, or public map authority is created.

## Non-effects and rollback

A local `PASS` authenticates no CRS, transformation, distortion assessment, layer, evidence, policy, review, release, publication, or public-use state. Rollback is a single additive revert with no external cleanup.
