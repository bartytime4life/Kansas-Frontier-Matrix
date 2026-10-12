<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/common/spatial-model-family-assessment
title: SpatialModelFamilyAssessment Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Domain steward · Evidence steward · Map steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; common; spatial-model; representation; uncertainty; review-required
responsibility: Define a fixture-only assessment that distinguishes positional, network, field, transformation, and decomposed composite spatial models without creating a registry, validating scientific truth, or granting policy, review, release, or publication authority.
truth_posture: "CONFIRMED supplied Pass 18 card, accepted Directory Rules, adjacent repository contracts, and bounded implementation gap; PROPOSED inactive assessment; UNKNOWN domain adoption and scientific validation profiles; NEEDS VERIFICATION steward review and hosted exact-head CI"
related:
  - ./spatial_geometry.md
  - ./modeled_surface.md
  - ../evidence/representation_fitness_assessment.md
  - ../../schemas/contracts/v1/common/spatial_model_family_assessment.schema.json
  - ../../fixtures/contracts/v1/common/spatial_model_family_assessment/cases.json
  - ../../tools/validators/validate_spatial_model_family_assessment.py
  - ../../tests/validators/test_validate_spatial_model_family_assessment.py
  - ../../docs/intake/exploratory/pass-18-spatial-model-family-assessment-source-map.md
[/KFM_META_BLOCK_V2] -->

# SpatialModelFamilyAssessment Candidate

`SpatialModelFamilyAssessmentCandidate` is an additive declaration for deciding
which validation family applies to one spatial subject. It implements the
smallest reviewable portion of supplied Pass 18 card `KFM-P18-INV-054`.

The profile keeps four base families distinct:

| Family | Declared characteristic | Minimum evidence |
|---|---|---|
| `POSITION` | Discrete spatial identity or occurrence. | Position or coordinate-method reference. |
| `NETWORK` | Nodes, edges, direction, connectivity, or flow. | Topology-semantics reference. |
| `FIELD` | A value supported continuously or by cells over an extent. | Support, resolution, unit, or interpolation reference. |
| `TRANSFORMATION` | A declared input-to-output spatial derivation. | Method and lineage or run-receipt reference. |

`COMPOSITE` is not a fifth undifferentiated rubric. It must declare at least two
base characteristics, cite the corresponding family evidence, reference at
least two component assessments, and partition uncertainty by family.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The declared family, evidence, uncertainty, review record, identity, and non-authority boundary are locally coherent. |
| `ABSTAIN` | The family or review posture remains unresolved. |
| `DENY` | The declaration mixes family semantics, omits required evidence, flattens composite uncertainty, crosses the trust membrane, or tampers with content identity. |
| `ERROR` | The candidate cannot be safely evaluated under the closed schema. |

A `PASS` is a fixture result, not proof that a point is accurate, a network is
connected, a field is scientifically valid, a transformation is reproducible,
or a composite is fit for use.

## Invariants

- One base family declares exactly its own characteristic and evidence lane.
- A composite declares two or more base characteristics and retains component
  assessment references plus family-partitioned uncertainty.
- An unresolved family carries no positive family assertion.
- Reference arrays and the limitation set are sorted and duplicate-free.
- Content identity binds the entire declaration except the two identity fields.
- RAW, WORK, QUARANTINE, direct-store, and embedded-query references are denied.
- All authority claims remain fixed to `false`.

## Authority boundary

The profile does not create or mutate a domain-object family registry, layer,
feature, graph, raster, modeled surface, geometry, source, evidence bundle,
review record, policy decision, release manifest, or published surface. It does
not dispatch production validators, execute a transformation, calculate
uncertainty, establish fitness for use, or authorize lifecycle movement,
release, deployment, publication, or public interpretation.

## Directory Rules basis

Cross-family meaning belongs under `contracts/common/`; machine shape under
`schemas/contracts/v1/common/`; synthetic examples under
`fixtures/contracts/v1/common/`; repository validation under
`tools/validators/`; conformance evidence under `tests/validators/`; read-only
orchestration under `.github/workflows/`; source reconciliation under
`docs/intake/exploratory/`; and authoring accountability under
`data/receipts/generated/`. No parallel authority root is introduced.

## Validation and rollback

```bash
python -m unittest tests.validators.test_validate_spatial_model_family_assessment -v
python tools/validators/validate_spatial_model_family_assessment.py --fixtures
```

Rollback is one additive commit revert. The inactive packet has no runtime
consumer and creates no external state.
