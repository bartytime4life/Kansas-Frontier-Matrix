<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/dataset-version-source-reconciliation
title: DatasetVersion source reconciliation and implementation map
type: source-reconciliation
version: v1.0
status: draft
created: 2026-08-15
updated: 2026-08-15
policy_label: public
owning_root: docs/
truth_posture: CONFIRMED repository gap / PROPOSED fixture-first profile / UNKNOWN external integration
related:
  - ../../../contracts/data/dataset_version.md
  - ../../../schemas/contracts/v1/data/dataset_version.schema.json
  - ../../../tools/validators/data/validate_dataset_version.py
  - ../../../tests/validators/data/test_validate_dataset_version.py
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# DatasetVersion source reconciliation and implementation map

## Determination

`CONFIRMED`: current main at `695c4e67063481236e627f8652faf17619260a5a` contained a mature semantic contract but only a permissive placeholder schema. The schema required `id`, allowed arbitrary properties, and declared a validator path that did not exist. Repository search found no concrete base-family fixtures, validator, dedicated workflow, or direct schema consumer.

`PROPOSED`: implement a strict fixture-first v1 shape at the already-declared canonical schema path, with deterministic identity and bounded lifecycle/lineage checks. Keep the object family `draft` and explicitly deny any inference of source, evidence, policy, release, publication, or public-use authority.

## Source ledger

| Source | Location | Supported idea | Authority / limit |
|---|---|---|---|
| `# Kansas Frontier Matrix Implementation Reference.pdf` | page 6, recommended schema families | `DatasetVersion` carries dataset identity, source/schema version, hash, and time range; it is needed for reproducibility and rollback. | Source-derived architecture; does not prove current implementation. |
| Same reference | page 9, identity/evidence normalization and validation rules | Stable `dataset_version_id`; consequential observations/release candidates resolve through `DatasetVersion`; referential checks hold or reject missing versions. | Source-derived implementation guidance. |
| `kfm_encyclopedia.pdf` | page 14, Cross-Domain Capability Taxonomy | Normalization emits `TransformReceipt` and `DatasetVersion`; temporal modeling uses `DatasetVersion`; deterministic hashes stay distinct. | Planning manuscript; shape remains proposed. |
| Google Drive `Comprehensive Research and Verification Report` | W04 — Contracts, schemas, identity, and trust-object model | Calls for one versioned trust-object catalog with canonical homes, identities, reference rules, validators, and migration policy. | Newer research/verification source; current repo evidence still controls. |
| `contracts/data/dataset_version.md` | baseline v0.2 Status, Schema pairing, Recommended semantic fields, Validation | Existing semantic meaning and exact missing implementation support. | Current repository semantic authority for this draft family. |
| `schemas/contracts/v1/data/dataset_version.schema.json` | baseline blob `b511812…` | Confirms the field-incomplete permissive placeholder. | Current machine-shape evidence; does not settle policy. |
| ADR-0029 and adopted Directory Rules | accepted authority | Existing roots own contract meaning, machine shape, fixtures, validator code, tests, workflow, docs, and generated receipt. | Governs placement; does not grant release authority. |

## Repository reconciliation

| Question | Result |
|---|---|
| Already implemented? | `PARTIAL`: semantic contract only; schema was a placeholder. |
| Open PR overlap? | None found at campaign selection. |
| Recent merged overlap? | TemporalSlice references a `dataset_version_ref` but does not implement or validate the base family. |
| Superseded? | No. The repeatedly referenced object remains active vocabulary. |
| Contradicted? | No current accepted ADR selects a different object family or schema home. |
| Rights/sensitivity impact | Synthetic metadata only. No live source, protected data, exact location, or public release. |

## PR boundary

The slice changes only:

- the existing semantic contract and schema;
- synthetic valid/invalid fixtures;
- one no-network validator and focused unit test;
- one path-filtered workflow;
- this source map and a generated authoring receipt.

It does not create a registry entry, fetch source bytes, validate external references, alter policy, touch lifecycle data, create a release, or change repository settings.

## Acceptance criteria

1. Three valid fixtures pass and ten invalid fixtures produce exact reviewed reason-code sets.
2. IDs replay deterministically from version-defining fields.
3. Placeholder digests, temporal inversions, noncanonical references, self-lineage, incomplete derivative/correction lineage, and unsupported published states fail closed.
4. Tests prove duplicate-key/non-finite rejection, no candidate-value echo, and no network access.
5. Generated receipt hashes match the authored files.
6. Baseline topology-ratchet failure remains classified as inherited and outside this PR.

## Rollback

Revert the single implementation commit and remove all newly added companion files. This restores the prior permissive schema and draft contract without leaving a validator or workflow pointed at incompatible fixtures.
