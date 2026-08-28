<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/pass-18-spatial-table-normalization-assessment
title: Pass 18 Spatial Table Normalization Assessment Source Map
type: exploratory-source-map
version: v1.0.0
status: draft; proposed-inactive; implementation-candidate
owners: OWNER_TBD — Intake steward · Data contract steward · Schema steward · Data-quality steward
created: 2026-08-11
updated: 2026-08-11
owning_root: docs/
policy_label: internal; source-lineage; spatial-table; normalization; data-quality
responsibility: Preserve source and repository lineage for a bounded spatial-table normalization assessment without promoting proposal material into schema, data, policy, release, or publication authority.
truth_posture: "CONFIRMED attached-card transcription, visual review, Drive discovery, and inspected-repository comparison; PROPOSED bounded adaptation; NEEDS VERIFICATION human review and hosted exact-head CI"
related:
  - ../../../contracts/data/spatial_table_normalization_assessment.md
  - ../../../contracts/data/validation_report.md
  - ../../../contracts/data/dataset_version.md
  - ../../../schemas/contracts/v1/data/spatial_table_normalization_assessment.schema.json
  - ../../../fixtures/contracts/v1/data/spatial_table_normalization_assessment/cases.json
  - ../../doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 Spatial Table Normalization Assessment Source Map

## Evidence basis

| Evidence | Observation | Status |
|---|---|---|
| Supplied `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, SHA-256 `efc0d159761581b5ae043c607dfa28bbc58b3ca5423c9d18a659e650271d73b9`, physical page 76 / printed page 73 | Card `KFM-P18-INV-402` proposes normalization-style checks that separate entity keys, dependent attributes, and relationship fields before publication. It explicitly allows denormalized public tiles as derivatives of normalized canonical tables. The page was rendered and visually checked. | `CONFIRMED` |
| Connected Drive `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf` (`1ww-h3abQkxXeBvSxO5YV6_yvsZ9Wn1P5`) | Drive metadata confirms the named Pass 18 dossier is present. Byte identity with the supplied attachment was not asserted. | `CONFIRMED` metadata only |
| Connected Drive `Kansas Frontier Matrix — Connected-Dots Architecture Brief` (`1sdiLNDLFr2cVD3Q8h3ZvHO4D96WLJ6V7vf5neNzEyTM`) | The brief separates normalization and processing authority from delivery carriers and requires public surfaces to remain downstream of validation, evidence, policy, and release. | `CONFIRMED` thematic corroboration |
| `main@90deefee3c30dd5878e704cdfc621f89f1edf1f0` | Exact repository, PR, branch, and GitHub code searches found schema, DatasetVersion, ValidationReport, aggregate, GeoParquet, PMTiles, and source-normalizer seams but no card `KFM-P18-INV-402` or equivalent spatial-table normalization assessment packet. The intervening main change from the original inspection was limited to an unrelated generated receipt. | `CONFIRMED` for the inspected snapshot |

The sources establish candidate design pressure, not current implementation or permission to alter canonical data. Repository evidence and accepted Directory Rules determine the bounded adaptation.

## Reconciliation and selected increment

Implementing a live table scanner or altering every schema/table consumer would require data access, domain-specific dependency rules, reprocessing, and release decisions that this card does not resolve.

The selected increment is therefore a closed synthetic assessment candidate. It checks the internal coherence of declared fields, keys, dependencies, relationships, normal-form posture, derivative source binding, and review references. It does not inspect a table or claim that a declared dependency is true.

## Source-to-profile mapping

| Source pressure | Bounded adaptation | Held boundary |
|---|---|---|
| Separate entity keys and dependent attributes. | Explicit field inventory, entity-key fields, and determinant/dependent declarations. | No key or dependency inference from values. |
| Make relationship fields auditable. | Local fields, target entity/key references, and cardinality declarations. | No referential-integrity query or database mutation. |
| Check normalization before publication. | Canonical candidates require a complete third-normal-form-or-higher declaration with no anomaly. | No promotion or release gate is created. |
| Permit valid delivery denormalization. | Derivative candidates bind a canonical source, purpose, intentional duplication, and review references. | No PMTiles/GeoParquet build or public activation. |

## Directory Rules basis

The assessment's semantic meaning is a data contract. Its schema, fixtures, validator, tests, workflow, lineage note, and generated receipt remain in their established responsibility roots. No new root or parallel schema registry, data store, relationship authority, release record, or publication home is introduced.

## Deferred questions

- Which domain-specific tables require stricter normal-form or key rules?
- Which component may inspect table values and prove functional dependencies?
- Which derivative duplications are permitted for PMTiles, GeoParquet, API responses, or exports?
- Which release gate consumes a future active assessment remains undecided.

## Validation and rollback

Focused validation covers closed shape, deterministic identity, UTC timestamps, canonical arrays, field reference closure, determinant/dependent separation, dependency/anomaly parity, canonical normal-form posture, derivative source binding, review references, malformed Unicode, and unknown-field rejection.

Rollback is a focused revert of this additive packet. No table migration, reprocessing, release withdrawal, correction notice, cache invalidation, or public cleanup is required because the profile has no consumer and mutates no data.
