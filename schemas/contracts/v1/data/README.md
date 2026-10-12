# `schemas/contracts/v1/data/` — Data Schema Family Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-data-readme
title: schemas/contracts/v1/data/ — Data Schema Family Index
version: v1
status: draft
policy_label: public
owners:
  - <schema-steward>
  - <data-steward>
  - <contract-steward>
  - <validation-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, contracts, v1, data, dataset-version, json-schema]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-data-blueviolet)
![posture](https://img.shields.io/badge/posture-schema--family-orange)
![schema](https://img.shields.io/badge/schema-placeholder-yellow)

## Purpose

`schemas/contracts/v1/data/` is the draft schema family lane for data-related contract object shapes.

This path is for machine-checkable schemas that describe governed data-object metadata. It is not the actual KFM data storage root and must not store payloads, proofs, release records, or public products.

This README is documentation only. It is not itself a schema file, contract prose, policy, validator code, data payload, proof output, or release authority.

## Status & authority

| Field | Value |
|---|---|
| Document type | Data schema family README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/v1/data/` |
| Status | Draft |
| Authority level | Schema-family index guidance. Schema files, paired contracts, registry records, validators, fixtures, tests, ADRs, and steward decisions outrank this README. |
| Path posture | Current-session evidence confirms this README existed as a short stub before this update. |
| Confirmed child schema | `dataset_version.schema.json` exists as a PROPOSED placeholder schema. |
| Paired contract lane | `contracts/data/` exists as the semantic-contract lane for data object meanings, not the data storage root. |
| Validator posture | NEEDS VERIFICATION. The schema-declared validator path was not verified in this edit. |
| Fixture posture | NEEDS VERIFICATION. The schema-declared fixture root was not verified in this edit. |
| Required reviewers | Schema steward, data steward, contract steward, validation steward, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the root for machine-checkable shape and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says the default schema home is `schemas/contracts/v1/<family>/...`, while `contracts/` retains object meaning and `schemas/` owns machine-checkable shape.

Current-session evidence from Directory Rules confirms field-level shape belongs under `schemas/`, data storage belongs under `data/`, and creating parallel homes for schemas, contracts, registries, releases, proofs, or receipts requires an ADR.

Current-session evidence confirms `contracts/data/` is the semantic-contract directory for data-related governed object families and explicitly says it is not the actual data store.

Current-session evidence confirms `schemas/contracts/v1/data/dataset_version.schema.json` exists and is paired to `contracts/data/dataset_version.md`, but the paired contract and schema identify it as a placeholder / PROPOSED shape needing verification.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    └── v1/
        └── data/
            ├── README.md
            └── dataset_version.schema.json

contracts/
└── data/
    ├── README.md
    └── dataset_version.md

data/                                      # actual data responsibility root; not schema home
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/contracts/v1/data/README.md` | Short stub before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms `schemas/contracts/v1/` as the proposed canonical schema home and separates contract meaning from schema shape. |
| Directory Rules | Confirms field-level shape belongs under `schemas/`; data storage belongs under `data/`; parallel homes require ADR review. |
| `contracts/data/README.md` | Semantic-contract lane for data-related governed object meanings; not the data store. |
| `contracts/data/dataset_version.md` | Paired semantic contract for `DatasetVersion`; says paired schema is a placeholder and validator behavior remains NEEDS VERIFICATION. |
| `schemas/contracts/v1/data/dataset_version.schema.json` | Existing JSON Schema draft 2020-12 placeholder with `$id`, `x-kfm`, `spec_hash`, `id`, `version`, required `id`, and `additionalProperties: true`. |

This README does not verify schema completeness, schema registry entries, fixture coverage, validator wiring, CI behavior, policy behavior, release integration, or runtime behavior.

## Current schema inventory

| Schema file | Paired contract | Status | Notes |
|---|---|---|---|
| `dataset_version.schema.json` | `contracts/data/dataset_version.md` | PROPOSED / placeholder | Current schema requires only `id`, allows additional properties, and declares fixture, validator, and policy pointers that remain NEEDS VERIFICATION. |

## Responsibilities

| Responsibility | Expectation |
|---|---|
| Schema-family index | List data object schemas and their status. |
| Contract pairing | Maintain links to semantic contracts under `contracts/data/` or another verified contract lane. |
| Boundary preservation | Keep actual data records outside `schemas/`. |
| Drift prevention | Prevent payloads, registry records, proofs, or releases from being stored in `schemas/`. |
| Fixture linkage | Point to valid and invalid fixtures when verified. |
| Validator linkage | Point to validators or CI checks when verified. |
| Registry linkage | Point to schema registry records when verified. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## What belongs here

- This README.
- Machine-checkable JSON Schema files for data contract object shapes.
- Short schema-family index notes.
- Migration notes for data schema placement.
- Drift notes about duplicate or stale data schema paths.
- Links to paired contracts, fixtures, validators, schema registry records, policy references, release references, and tests.

## What does not belong here

- Actual data payloads.
- Registry records.
- Proof records.
- Release records.
- Contract prose.
- Policy rules.
- Validator implementation code.
- Runtime code.
- Public data products or map/UI behavior.
- Claims that a schema is complete without fixtures, validators, registry records, and review support.

## Schema status values

Use finite status values where possible:

| Status | Meaning |
|---|---|
| `STUB` | Schema exists but is not field-complete. |
| `DRAFT_SCHEMA` | Schema has meaningful fields but still needs review and test support. |
| `ACTIVE_SCHEMA` | Schema has accepted contract pairing, fixtures, validator support, registry record, and review status. |
| `MIRROR` | Schema mirrors another accepted schema location. |
| `TRANSITIONAL` | Schema is awaiting migration to the accepted home. |
| `DEPRECATED` | Schema should no longer receive new consumers. |
| `NEEDS_VERIFICATION` | Pairing, fixture, validator, registry, or CI support has not been verified. |

## Review checklist

- [ ] Schema has a stable `$id`.
- [ ] Schema has `$schema` set to JSON Schema draft 2020-12 unless an ADR says otherwise.
- [ ] Paired contract path is linked.
- [ ] Schema registry entry is linked or marked NEEDS VERIFICATION.
- [ ] Valid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Invalid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Validator path is linked or marked NEEDS VERIFICATION.
- [ ] CI/schema-test support is linked or marked NEEDS VERIFICATION.
- [ ] Actual data records remain outside `schemas/`.
- [ ] Any migration or compatibility claim cites an ADR, migration note, or verified repo evidence.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/contracts/v1/data/`.
- [ ] Confirm whether `dataset_version.schema.json` should remain permissive or become strict.
- [ ] Confirm schema registry records.
- [ ] Confirm valid fixture paths.
- [ ] Confirm invalid fixture paths.
- [ ] Confirm validator path and behavior.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm whether additional data object schemas belong in this family or narrower families.
- [ ] Confirm whether `schemas/README.md` should index this data lane.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing short stub |
| Next review trigger | New data schema, schema-home migration, validator update, fixture update, schema registry update, ADR update, data contract update, or compatibility-lane decision |
