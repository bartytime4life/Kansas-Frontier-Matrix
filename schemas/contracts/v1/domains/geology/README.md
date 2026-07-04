# `schemas/contracts/v1/domains/geology/` — Geology Domain Schema Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-domains-geology-readme
title: schemas/contracts/v1/domains/geology/ — Geology Domain Schema Index
version: v1
status: draft
policy_label: public
owners:
  - <schema-steward>
  - <geology-domain-steward>
  - <contract-steward>
  - <validation-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, contracts, v1, domains, geology, sublanes, surficial, bedrock, stratigraphy, lithology, json-schema]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![domain](https://img.shields.io/badge/domain-geology-green)
![posture](https://img.shields.io/badge/posture-domain--schema--index-orange)
![canonical](https://img.shields.io/badge/canonical-PROPOSED-yellow)

## Purpose

`schemas/contracts/v1/domains/geology/` is the draft Geology domain schema lane.

This path is for machine-checkable Geology schema shapes: JSON Schema files, schema-family README files, schema index notes, migration notes, and links to paired contracts, fixtures, validators, registry records, tests, policy references, source-registry references, correction references, rollback references, and release references.

This path is not a home for Geology contract prose, policy rules, validator code, packages, pipelines, lifecycle data, source registry records, emitted receipts, proof outputs, catalog records, release records, review records, or public map/API artifacts.

This README is documentation only. It is not itself a schema file, contract prose, policy, validator code, pipeline code, lifecycle data, registry data, proof output, receipt instance, source descriptor instance, or release authority.

## Status & authority

| Field | Value |
|---|---|
| Document type | Geology domain schema README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/v1/domains/geology/` |
| Status | Draft |
| Authority level | Domain schema index guidance. Schema files, paired contracts, registry records, validators, fixtures, tests, ADRs, policy records, release records, and steward decisions outrank this README. |
| Path posture | Current-session evidence confirms this README existed as a greenfield scaffold before this update. |
| Canonical posture | PROPOSED Geology domain schema lane under ADR-0001. Implementation completeness remains NEEDS VERIFICATION. |
| Concrete schema inventory | NEEDS VERIFICATION. Current-session search found Geology contracts and docs, but did not confirm concrete `.schema.json` files under this path. |
| Known child lanes | `sublanes/` exists as a draft index; `sublanes/surficial/` exists as a draft child index. |
| Sublane convention | NEEDS VERIFICATION. The literal `sublanes/` segment remains a proposed convention until ADR/steward decision confirms it. |
| Required reviewers | Schema steward, Geology domain steward, relevant sublane steward, contract steward, validation steward, policy/release stewards where applicable, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the machine-checkable shape root and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says domain-specific schemas nest under `schemas/contracts/v1/domains/<domain>/...`, while `contracts/` retains object meaning and `schemas/` owns machine-checkable shape.

Current-session Directory Rules evidence confirms field-level shape belongs under `schemas/`, while lifecycle data, registries, proofs, receipts, and release materials are separate responsibility roots and parallel homes require ADR review.

Current-session evidence confirms this README previously claimed broadly that docs, contracts, schemas, policies, fixtures, tests, packages, pipelines, registries, and data lifecycle artifacts could belong here. This update corrects that boundary: this path is schema-shape only.

Current-session evidence confirms `schemas/contracts/v1/domains/geology/sublanes/README.md` exists as a draft child-index parent and remains index-only until the sublane convention is accepted.

Current-session evidence confirms `schemas/contracts/v1/domains/geology/sublanes/surficial/README.md` exists as a draft Surficial child index and marks the `sublanes/` convention as NEEDS VERIFICATION.

Current-session search found Geology semantic contract surfaces such as `GeologicUnit`, `GeologicAge`, `StratigraphicInterval`, `Lithology`, `domain_feature_identity`, and `domain_validation_report`, but did not confirm paired schema files under this path.

Current-session evidence from `contracts/domains/geology/GeologicUnit.md` says the exact paired schema path for `GeologicUnit` was not found and that `GeologicUnit` does not replace adjacent objects or release approval.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    └── v1/
        └── domains/
            └── geology/
                ├── README.md                    # you are here
                └── sublanes/
                    ├── README.md                # draft sublane index
                    └── surficial/
                        └── README.md            # draft Surficial schema sublane index

contracts/
└── domains/
    └── geology/                                 # semantic meaning; not schema shape
        ├── GeologicUnit.md
        ├── GeologicAge.md
        ├── StratigraphicInterval.md
        ├── Lithology.md
        ├── domain_feature_identity.md
        └── domain_validation_report.md

docs/
└── domains/
    └── geology/                                 # human-facing doctrine; not schema shape

policy/
└── domains/geology/                             # admissibility/policy; not schema shape

fixtures/
└── domains/geology/                             # test examples; coverage NEEDS VERIFICATION

data/                                             # lifecycle, registry, proof, receipt roots; not schema home

release/                                          # release decisions and release records; not schema home
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/contracts/v1/domains/geology/README.md` | Greenfield scaffold before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms domain schemas nest under `schemas/contracts/v1/domains/<domain>/...`. |
| Directory Rules | Confirms machine shape belongs under `schemas/`; parallel homes require ADR review. |
| `schemas/contracts/v1/domains/geology/sublanes/README.md` | Existing draft parent index for proposed Geology schema sublanes. |
| `schemas/contracts/v1/domains/geology/sublanes/surficial/README.md` | Existing draft Surficial child index; marks sublane convention NEEDS VERIFICATION. |
| Search for Geology schema/contract surfaces | Found Geology contracts and docs; did not confirm concrete schema files under this path. |
| `contracts/domains/geology/GeologicUnit.md` | Semantic contract; exact paired schema path was not found and adjacent-object/release boundaries remain explicit. |

This README does not verify complete Geology schema coverage, schema registry entries, fixture coverage, validator wiring, CI behavior, policy behavior, release integration, runtime behavior, public API behavior, or map rendering behavior.

## Current schema inventory

| Schema file | Paired contract | Status | Notes |
|---|---|---|---|
| No concrete `.schema.json` file confirmed in this edit | N/A | NEEDS VERIFICATION | Current-session search found contract surfaces but did not confirm a concrete schema file under `schemas/contracts/v1/domains/geology/`. |

## Current child lanes

| Child path | Status | Responsibility |
|---|---|---|
| `sublanes/` | Draft index / NEEDS VERIFICATION | Parent index for proposed Geology schema sublanes; index-only until placement is accepted. |
| `sublanes/surficial/` | Draft child index / NEEDS VERIFICATION | Candidate schema sublane for surficial geology objects such as `SurficialUnit` and public-safe surficial derivatives. |

## Candidate schema inventory

Geology schema candidates below come from current search and adjacent evidence. They require steward review, schema files, paired contracts, fixtures, validators, registry records, and CI support before promotion.

| Candidate schema | Status | Notes |
|---|---|---|
| `geologic_unit.schema.json` or `GeologicUnit.schema.json` | NEEDS VERIFICATION | Candidate mapped geologic-unit shape. Existing contract notes exact schema path/casing was not found. |
| `geologic_age.schema.json` or `GeologicAge.schema.json` | NEEDS VERIFICATION | Candidate geologic-age shape. |
| `stratigraphic_interval.schema.json` or `StratigraphicInterval.schema.json` | NEEDS VERIFICATION | Candidate stratigraphic interval/correlation shape. |
| `lithology.schema.json` or `Lithology.schema.json` | NEEDS VERIFICATION | Candidate lithology vocabulary/reference shape. |
| `domain_feature_identity.schema.json` | NEEDS VERIFICATION | Candidate deterministic identity support shape. |
| `domain_validation_report.schema.json` | NEEDS VERIFICATION | Candidate validation-report shape; not proof or release authority. |
| `surficial_unit.schema.json` | NEEDS VERIFICATION | Candidate SurficialUnit shape; may belong under root, `sublanes/surficial/`, cross-domain, or common path after review. |
| `geology_boundary_version.schema.json` | NEEDS VERIFICATION | Candidate versioned boundary shape for geologic/surficial units. |
| `cross_section.schema.json` | NEEDS VERIFICATION | Candidate cross-section/interpretation shape if accepted. |
| `borehole_reference.schema.json` | NEEDS VERIFICATION | Candidate borehole/log reference shape if accepted. |
| `geology_public_derivative.schema.json` | NEEDS VERIFICATION | Candidate public-safe derivative shape with rights, release, correction, and rollback support. |

## Schema-lane responsibilities

| Responsibility | Expectation |
|---|---|
| Domain schema index | List Geology schema files and child schema lanes as they are verified. |
| Contract pairing | Link each schema to paired semantic contracts under `contracts/domains/geology/` or another verified contract lane. |
| Sublane discipline | Keep `sublanes/` index-only and NEEDS VERIFICATION until an ADR or steward decision accepts the convention. |
| Boundary preservation | Keep policy, fixtures, validators, pipelines, lifecycle data, source registry records, receipt instances, proofs, catalog records, and release records in their own responsibility roots. |
| Adjacent-domain discipline | Do not replace Soil, Hydrology, Hazards, Archaeology, land/title, or other adjacent-domain truth. |
| Drift prevention | Prevent duplicate canonical schema definitions across parent Geology, child sublanes, cross-domain lanes, and common schema families. |
| Fixture linkage | Point to valid, invalid, public-safe, and edge-case fixtures when verified. |
| Validator linkage | Point to validators or CI checks when verified. |
| Registry linkage | Point to schema registry records when verified. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## What belongs here

- This README.
- Machine-checkable Geology JSON Schema files once placement is confirmed.
- Geology schema-family and child-lane README files.
- Schema index notes.
- Migration notes for Geology schema placement.
- Drift notes about duplicate or stale Geology schema paths.
- Links to paired contracts, fixtures, validators, schema registry records, policy references, source-registry references, release references, correction references, rollback references, and tests.

## What does not belong here

- Contract prose.
- Policy rules.
- Validator implementation code.
- Runtime code.
- Packages or pipeline implementation.
- Lifecycle data payloads.
- Source registry records or SourceDescriptor instances.
- Emitted receipt instances.
- Proof outputs.
- Catalog records.
- Release records, release manifests, or release decisions.
- Public API or map/UI behavior.
- Soil map-unit truth, Hydrology measurement truth, Hazards risk truth, Archaeology site truth, land/title claims, or ownership/lease/permit decisions.
- Cross-domain schemas that belong under `schemas/contracts/v1/cross/` or another lowest-common responsibility root.
- Generic reusable schemas that belong under `schemas/contracts/v1/common/`.
- Claims that a schema is complete without fixtures, validators, registry records, and steward review support.

## Schema status values

Use finite status values where possible:

| Status | Meaning |
|---|---|
| `STUB` | Schema exists but is not field-complete. |
| `DRAFT_SCHEMA` | Schema has meaningful fields but still needs review and test support. |
| `ACTIVE_SCHEMA` | Schema has accepted contract pairing, fixtures, validator support, registry record, and review status. |
| `SUBLANE_INDEX` | Child lane indexes proposed schema subfamilies but placement remains open. |
| `MIRROR` | Schema mirrors another accepted schema location. |
| `TRANSITIONAL` | Schema is awaiting migration to the accepted home. |
| `DEPRECATED` | Schema should no longer receive new consumers. |
| `NEEDS_VERIFICATION` | Pairing, fixture, validator, registry, review, or CI support has not been verified. |

## Minimal schema note

```markdown
# <geology-schema-note-id>

## Status
STUB / DRAFT_SCHEMA / ACTIVE_SCHEMA / SUBLANE_INDEX / MIRROR / TRANSITIONAL / DEPRECATED / NEEDS_VERIFICATION

## Schema path
<schemas/contracts/v1/domains/geology/...>

## Paired contract
<contracts/domains/geology/... or N/A>

## Child lane
<root / sublanes / sublanes/surficial / other / N/A>

## Adjacent-domain references
<soil / hydrology / hazards / archaeology / none / NEEDS VERIFICATION>

## Fixtures
<fixtures path or N/A>

## Validator
<tools/validators path or N/A>

## Policy and release references
<policy/release path or N/A>

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
- [ ] Public-safe/generalized fixtures are linked or marked NEEDS VERIFICATION where applicable.
- [ ] Validator path is linked or marked NEEDS VERIFICATION.
- [ ] CI/schema-test support is linked or marked NEEDS VERIFICATION.
- [ ] Child-lane placement is justified when schema is not at the Geology schema root.
- [ ] `sublanes/` placement is accepted by ADR/steward decision or marked NEEDS VERIFICATION.
- [ ] Pipeline, policy, data, registry, proof, receipt, catalog, and release records remain outside `schemas/`.
- [ ] Adjacent-domain boundaries are preserved.
- [ ] Any migration or compatibility claim cites an ADR, migration note, or verified repo evidence.

## Naming guidance

Recommended schema filename pattern:

```text
<object_name>.schema.json
```

Examples:

```text
geologic_unit.schema.json
geologic_age.schema.json
stratigraphic_interval.schema.json
lithology.schema.json
domain_feature_identity.schema.json
domain_validation_report.schema.json
surficial_unit.schema.json
geology_boundary_version.schema.json
cross_section.schema.json
borehole_reference.schema.json
geology_public_derivative.schema.json
```

Use lowercase snake_case for schema filenames unless the schema registry or ADR specifies otherwise. If existing contracts use CamelCase while schema files use snake_case, record the mismatch and do not silently rename without a migration note.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/contracts/v1/domains/geology/`.
- [ ] Confirm complete Geology schema inventory.
- [ ] Confirm whether any concrete schema files already exist under alternate casing or alternate paths.
- [ ] Confirm paired contract paths for all accepted schemas.
- [ ] Resolve casing/path posture for `GeologicUnit.schema.json` versus `geologic_unit.schema.json`.
- [ ] Confirm whether `sublanes/` is an accepted schema organization pattern or should remain a proposed convention.
- [ ] Confirm whether `surficial/` schemas should live under the sublane or directly under the Geology root.
- [ ] Confirm schema registry records.
- [ ] Confirm valid fixture paths.
- [ ] Confirm invalid fixture paths.
- [ ] Confirm public-safe/generalized fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm policy, source-registry, release, correction, and rollback references for Geology schemas.
- [ ] Confirm whether `schemas/README.md` should index this Geology domain schema lane.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing greenfield scaffold |
| Next review trigger | New Geology schema, child-lane decision, sublane placement decision, schema-home migration, validator update, fixture update, schema registry update, ADR update, Geology contract update, policy/release reference update, or compatibility-lane decision |
