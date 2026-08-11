<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/data/spatial-table-normalization-assessment
title: SpatialTableNormalizationAssessmentCandidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Data contract steward · Schema steward · Data-quality steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; data; spatial-table; normalization; keys; dependencies; relationships
responsibility: Define a fixture-only assessment of declared entity keys, attribute dependencies, relationship fields, and intentional release-derivative denormalization without inspecting table values or creating schema, data, policy, review, release, or publication authority.
truth_posture: "CONFIRMED supplied-card traceability and repository placement; PROPOSED inactive contract; UNKNOWN consumer adoption; NEEDS VERIFICATION human review and hosted CI"
related:
  - ./validation_report.md
  - ./dataset_version.md
  - ../common/aggregate_statistic.md
  - ../../schemas/contracts/v1/data/spatial_table_normalization_assessment.schema.json
  - ../../fixtures/contracts/v1/data/spatial_table_normalization_assessment/cases.json
  - ../../tools/validators/data/validate_spatial_table_normalization_assessment.py
  - ../../tests/validators/test_validate_spatial_table_normalization_assessment.py
  - ../../docs/intake/exploratory/pass-18-spatial-table-normalization-assessment-source-map.md
[/KFM_META_BLOCK_V2] -->

# SpatialTableNormalizationAssessmentCandidate

`SpatialTableNormalizationAssessmentCandidate` records a closed, synthetic declaration of one spatial table's field inventory, entity key, functional dependencies, relationship fields, assessed normal form, and any intentionally denormalized release-derivative posture.

It implements the smallest reviewable portion of supplied Pass 18 card `KFM-P18-INV-402`: feature identity, dependent attributes, and relationship fields should remain distinguishable before publication-oriented work proceeds.

## Boundary

A validator `PASS` proves only that the candidate's closed shape, deterministic identity, canonical ordering, field references, dependency declarations, relationship declarations, derivative binding, anomaly disclosure, review references, and fixed-false authority declarations are internally coherent under this fixture profile.

It does **not** open or sample a table, inspect values, infer candidate keys, prove a functional dependency, resolve a schema registry, modify a database, normalize or denormalize data, establish a canonical schema, validate a PMTiles/GeoParquet artifact, evaluate policy, approve review, promote lifecycle state, release, deploy, publish, or authorize public use.

## Declared profiles

| Lifecycle role | Locally coherent complete posture |
|---|---|
| `PROCESSED_CANONICAL_CANDIDATE` | Declares `THIRD_NORMAL_FORM` or `BOYCE_CODD_NORMAL_FORM`, no normalization anomaly, no canonical-source back-reference, and at least one review record. |
| `RELEASE_DERIVATIVE_CANDIDATE` | Declares `DENORMALIZED_DERIVATIVE`, binds the canonical source and purpose, limits local anomaly vocabulary to intentional derivative duplication, and retains review records. |

This split preserves the card's explicit tension: a normalized canonical table and a deliberately denormalized delivery carrier can both be legitimate, but they are not the same authority object.

## Profile fields

| Field | Meaning |
|---|---|
| `profile_spec_hash` | Canonical JSON plus SHA-256 binding of the candidate except this field. |
| `table_artifact_ref` / `table_artifact_digest` | Pinned candidate-table identity; no bytes are read. |
| `schema_registry` | Pinned schema reference and explicit local resolution posture. |
| `field_inventory` / `entity_key_fields` | Canonically ordered declared fields and entity key. |
| `dependencies` | Canonically ordered determinant/dependent declarations with bounded dependency kinds and evidence references. |
| `relationships` | Canonically ordered local-to-target key declarations and cardinality. |
| `assessment` | Completeness, declared normal form, anomaly codes, derivative source binding, purpose, and review references. |
| `authority_claims` | Fixed-false schema, data, evidence, policy, review, promotion, release, publication, and public-use declarations. |

## Finite validation outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Shape, identity, field, key, dependency, relationship, form, anomaly, derivative, and review invariants are coherent. |
| `ABSTAIN` | Schema reference, assessment, or normal-form declaration remains unresolved or incomplete. |
| `DENY` | A field, dependency, anomaly, canonical-form, derivative-source, review, canonicalization, or identity invariant fails. |
| `ERROR` | The candidate cannot be evaluated safely under the closed schema. |

These outcomes are local validator results, not database facts, data-quality findings, policy decisions, review decisions, release states, or runtime answers.

## Directory Rules basis

Accepted Directory Rules place semantic data-object meaning under `contracts/data/`, closed machine shape under `schemas/contracts/v1/data/`, synthetic cases under `fixtures/contracts/v1/data/`, repository validation under `tools/validators/data/`, executable conformance under `tests/validators/`, orchestration under `.github/workflows/`, source reconciliation under `docs/intake/exploratory/`, and authoring accountability under `data/receipts/generated/`.

The profile composes existing dataset, validation-report, schema-registry, and derivative-carrier responsibilities only by reference. It creates no parallel schema registry, canonical table store, relationship model, release record, or published artifact.

## Validation

```bash
python -m unittest tests.validators.test_validate_spatial_table_normalization_assessment -v
python tools/validators/data/validate_spatial_table_normalization_assessment.py --fixtures
```

## Rollback

Revert the additive packet. It has no runtime consumer and changes no table, database, schema registry, evidence, policy, review, lifecycle state, release, deployment, or public artifact.
