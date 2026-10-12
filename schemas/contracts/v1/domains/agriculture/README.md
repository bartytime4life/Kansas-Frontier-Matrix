# `schemas/contracts/v1/domains/agriculture/` — Agriculture Domain Schema Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-domains-agriculture-readme
title: schemas/contracts/v1/domains/agriculture/ — Agriculture Domain Schema Index
version: v1
status: draft
policy_label: public
owners:
  - <schema-steward>
  - <agriculture-domain-steward>
  - <contract-steward>
  - <validation-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, contracts, v1, domains, agriculture, receipts, hydrology-ext, json-schema]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![domain](https://img.shields.io/badge/domain-agriculture-green)
![posture](https://img.shields.io/badge/posture-domain--schema--index-orange)
![canonical](https://img.shields.io/badge/canonical-PROPOSED-yellow)

## Purpose

`schemas/contracts/v1/domains/agriculture/` is the draft Agriculture domain schema lane.

This path is for machine-checkable Agriculture schema shapes: JSON Schema files, schema-family README files, schema index notes, migration notes, and links to paired contracts, fixtures, validators, registry records, tests, policy references, and release references.

This path is not a home for Agriculture contract prose, policy rules, validator code, packages, pipelines, lifecycle data, registry records, proof outputs, emitted receipts, or release records.

This README is documentation only. It is not itself a schema file, contract prose, policy, validator code, lifecycle data, registry data, proof output, receipt instance, or release authority.

## Status & authority

| Field | Value |
|---|---|
| Document type | Agriculture domain schema README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/v1/domains/agriculture/` |
| Status | Draft |
| Authority level | Domain schema index guidance. Schema files, paired contracts, registry records, validators, fixtures, tests, ADRs, policy records, release records, and steward decisions outrank this README. |
| Path posture | Current-session evidence confirms this README existed as a greenfield scaffold before this update. |
| Canonical posture | PROPOSED Agriculture domain schema lane under ADR-0001. Implementation completeness remains NEEDS VERIFICATION. |
| Known child lanes | `hydrology-ext/` and `receipts/` READMEs exist and are draft indexes. |
| Known schema file | `aggregation_receipt.schema.json` exists as a PROPOSED scaffold. |
| Shorter alias lane | `schemas/contracts/v1/agriculture/` exists as a compatibility/index lane pointing toward this domain path. |
| Required reviewers | Schema steward, Agriculture domain steward, contract steward, validation steward, policy steward where applicable, release steward where applicable, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the machine-checkable shape root and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says domain-specific schemas nest under `schemas/contracts/v1/domains/<domain>/...`, while `contracts/` retains object meaning and `schemas/` owns machine-checkable shape.

Current-session evidence from Agriculture canonical paths identifies `schemas/contracts/v1/domains/agriculture/` as the Agriculture machine-shape location while noting Agriculture-specific paths are PROPOSED until verified.

Current-session evidence confirms this path already had a greenfield scaffold. This update narrows the README to the actual `schemas/` responsibility: machine-checkable shape and schema-index support only.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    └── v1/
        ├── agriculture/                         # shorter compatibility/index lane
        └── domains/
            └── agriculture/
                ├── README.md                    # you are here
                ├── aggregation_receipt.schema.json
                ├── hydrology-ext/
                │   └── README.md
                └── receipts/
                    └── README.md

contracts/
└── domains/
    └── agriculture/                             # semantic meaning; not schema shape

policy/
└── domains/
    └── agriculture/                             # admissibility/policy; not schema shape

fixtures/
└── domains/
    └── agriculture/                             # test examples; coverage NEEDS VERIFICATION

data/                                            # lifecycle data / registry / proof / receipt roots; not schema home

release/                                         # release decisions and release records; not schema home
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/contracts/v1/domains/agriculture/README.md` | Greenfield scaffold before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms domain schemas nest under `schemas/contracts/v1/domains/<domain>/...`. |
| `docs/domains/agriculture/CANONICAL_PATHS.md` | Agriculture path doctrine; says Agriculture machine shape lives under this path while concrete Agriculture paths remain PROPOSED until verified. |
| `schemas/contracts/v1/domains/agriculture/hydrology-ext/README.md` | Existing Agriculture-owned Hydrology extension schema index. |
| `schemas/contracts/v1/domains/agriculture/receipts/README.md` | Existing Agriculture receipts schema index. |
| `schemas/contracts/v1/domains/agriculture/aggregation_receipt.schema.json` | Existing PROPOSED scaffold schema. |

This README does not verify complete Agriculture schema coverage, schema registry entries, fixture coverage, validator wiring, CI behavior, policy behavior, release integration, runtime behavior, or public API/UI behavior.

## Current schema inventory

| Schema file | Paired contract | Status | Notes |
|---|---|---|---|
| `aggregation_receipt.schema.json` | `contracts/domains/agriculture/aggregation_receipt.md` in schema metadata; `contracts/domains/agriculture/aggregation-receipt.md` exists and records a path conflict | PROPOSED / scaffold | Schema has `$schema`, `$id`, title, description, empty `properties`, `additionalProperties: true`, and `x-kfm.status: PROPOSED`. |

## Current child lanes

| Child path | Status | Responsibility |
|---|---|---|
| `hydrology-ext/` | Draft index | Agriculture-owned extension lane for bounded Hydrology references; must not redefine Hydrology-owned schemas. |
| `receipts/` | Draft index | Agriculture receipt schema index; must not store emitted receipt instances or collapse receipts with proofs, catalog records, or release records. |

## Schema-lane responsibilities

| Responsibility | Expectation |
|---|---|
| Domain schema index | List Agriculture schema files and child schema lanes. |
| Contract pairing | Link each schema to paired semantic contracts under `contracts/domains/agriculture/` or another verified contract lane. |
| Alias discipline | Keep `schemas/contracts/v1/agriculture/` as compatibility/index unless an ADR or migration note changes it. |
| Child-lane discipline | Keep `hydrology-ext/` and `receipts/` as scoped sublanes with their own review status. |
| Boundary preservation | Keep policy, fixtures, validators, data records, receipts, proofs, and release records in their own responsibility roots. |
| Drift prevention | Prevent duplicate canonical schema definitions across short alias, domain root, child lanes, and cross-domain lanes. |
| Fixture linkage | Point to valid and invalid fixtures when verified. |
| Validator linkage | Point to validators or CI checks when verified. |
| Registry linkage | Point to schema registry records when verified. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## What belongs here

- This README.
- Machine-checkable Agriculture JSON Schema files.
- Agriculture schema-family and child-lane README files.
- Schema index notes.
- Migration notes for Agriculture schema placement.
- Drift notes about duplicate or stale Agriculture schema paths.
- Links to paired contracts, fixtures, validators, schema registry records, policy references, release references, and tests.

## What does not belong here

- Contract prose.
- Policy rules.
- Validator implementation code.
- Runtime code.
- Packages or pipeline implementation.
- Lifecycle data payloads.
- Registry records.
- Proof outputs.
- Emitted receipt instances.
- Release records, release manifests, or release decisions.
- Public API or map/UI behavior.
- Cross-domain schemas that belong under `schemas/contracts/v1/cross/`.
- Generic reusable schemas that belong under `schemas/contracts/v1/common/`.
- Claims that a schema is complete without fixtures, validators, registry records, and review support.

## Schema status values

Use finite status values where possible:

| Status | Meaning |
|---|---|
| `STUB` | Schema exists but is not field-complete. |
| `DRAFT_SCHEMA` | Schema has meaningful fields but still needs review and test support. |
| `ACTIVE_SCHEMA` | Schema has accepted contract pairing, fixtures, validator support, registry record, and review status. |
| `EXTENSION_INDEX` | Child lane indexes extension schemas but has not accepted a concrete schema yet. |
| `MIRROR` | Schema mirrors another accepted schema location. |
| `TRANSITIONAL` | Schema is awaiting migration to the accepted home. |
| `DEPRECATED` | Schema should no longer receive new consumers. |
| `NEEDS_VERIFICATION` | Pairing, fixture, validator, registry, or CI support has not been verified. |

## Minimal schema note

```markdown
# <agriculture-schema-note-id>

## Status
STUB / DRAFT_SCHEMA / ACTIVE_SCHEMA / EXTENSION_INDEX / MIRROR / TRANSITIONAL / DEPRECATED / NEEDS_VERIFICATION

## Schema path
<schemas/contracts/v1/domains/agriculture/...>

## Paired contract
<contracts/domains/agriculture/... or N/A>

## Child lane
<root / hydrology-ext / receipts / other / N/A>

## Fixtures
<fixtures path or N/A>

## Validator
<tools/validators path or N/A>

## Policy references
<policy path or N/A>

## Release references
<release path or N/A>

## Notes
<short note grounded in repo evidence>

## Follow-up
<open items or none>
```

## Review checklist

- [ ] Schema has a stable `$id`.
- [ ] Schema has `$schema` set to JSON Schema draft 2020-12 unless an ADR says otherwise.
- [ ] Paired contract path is linked or marked NEEDS VERIFICATION.
- [ ] Schema registry entry is linked or marked NEEDS VERIFICATION.
- [ ] Valid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Invalid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Validator path is linked or marked NEEDS VERIFICATION.
- [ ] CI/schema-test support is linked or marked NEEDS VERIFICATION.
- [ ] Child-lane placement is justified when schema is not at the Agriculture schema root.
- [ ] Short alias path does not contain duplicate canonical schema definitions.
- [ ] Policy, data, proof, receipt-instance, and release records remain outside `schemas/`.
- [ ] Any migration or compatibility claim cites an ADR, migration note, or verified repo evidence.

## Naming guidance

Recommended schema filename pattern:

```text
<object_name>.schema.json
```

Examples:

```text
aggregation_receipt.schema.json
crop_observation.schema.json
field_boundary.schema.json
agriculture_layer_manifest.schema.json
```

Use lowercase snake_case for schema filenames unless the schema registry or ADR specifies otherwise. If an existing contract path uses hyphenated naming while schema metadata uses snake_case, record the conflict and do not silently rename without migration notes.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/contracts/v1/domains/agriculture/`.
- [ ] Confirm complete Agriculture schema inventory.
- [ ] Confirm whether `aggregation_receipt.schema.json` should remain at the Agriculture schema root or migrate under `receipts/`.
- [ ] Resolve the `aggregation-receipt` / `aggregation_receipt` contract-path conflict.
- [ ] Confirm whether `hydrology-ext/` is an accepted Agriculture schema subfamily.
- [ ] Confirm schema registry records.
- [ ] Confirm valid fixture paths.
- [ ] Confirm invalid fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm policy and release references for Agriculture schemas.
- [ ] Confirm whether `schemas/contracts/v1/agriculture/README.md` remains a compatibility/index lane.
- [ ] Confirm whether `schemas/README.md` should index this Agriculture domain schema lane.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing greenfield scaffold |
| Next review trigger | New Agriculture schema, child-lane decision, schema-home migration, validator update, fixture update, schema registry update, ADR update, Agriculture contract update, policy update, release reference update, or compatibility-lane decision |
