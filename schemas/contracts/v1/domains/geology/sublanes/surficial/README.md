# `schemas/contracts/v1/domains/geology/sublanes/surficial/` — Geology Surficial Sublane Schema Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-domains-geology-sublanes-surficial-readme
title: schemas/contracts/v1/domains/geology/sublanes/surficial/ — Geology Surficial Sublane Schema Index
version: v1
status: draft
policy_label: public
owners:
  - <schema-steward>
  - <geology-domain-steward>
  - <surficial-geology-steward>
  - <contract-steward>
  - <validation-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, contracts, v1, domains, geology, sublanes, surficial, quaternary, map-units, json-schema]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![domain](https://img.shields.io/badge/domain-geology-green)
![sublane](https://img.shields.io/badge/sublane-surficial-blue)
![posture](https://img.shields.io/badge/posture-sublane--schema--index-orange)
![canonical](https://img.shields.io/badge/canonical-NEEDS%20VERIFICATION-yellow)

## Purpose

`schemas/contracts/v1/domains/geology/sublanes/surficial/` is a draft Geology-owned schema sublane for surficial geology shapes.

This path is for machine-checkable schema notes and candidate JSON Schema files for surficial geology objects, such as `SurficialUnit`, surficial map-unit boundary versions, surficial lithology references, and public-safe surficial map derivatives, once those schema homes are confirmed.

This path must not become a second Geology root, pipeline lane, documentation lane, lifecycle data lane, source registry, proof store, release lane, Hydrology authority, Soil authority, Hazards authority, or public map/UI authority.

This README is documentation only. It is not itself a schema file, contract prose, policy, validator code, pipeline code, lifecycle data, source data, registry data, proof output, receipt instance, or release authority.

## Status & authority

| Field | Value |
|---|---|
| Document type | Geology surficial sublane schema README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/v1/domains/geology/sublanes/surficial/` |
| Status | Draft |
| Authority level | Sublane schema-index guidance. Schema files, paired contracts, registry records, validators, fixtures, tests, ADRs, parent Geology schema decisions, and steward decisions outrank this README. |
| Path posture | Current-session evidence confirms this README was blank before this update. |
| Parent Geology schema lane | `schemas/contracts/v1/domains/geology/` exists as a PROPOSED greenfield scaffold. |
| Sublane posture | NEEDS VERIFICATION. Current Geology docs say the literal `sublanes/` segment is PROPOSED pending ADR. |
| Schema inventory | NEEDS VERIFICATION. This edit did not confirm concrete schema files under this sublane. |
| Likely paired contract surfaces | `contracts/domains/geology/GeologicUnit.md`, `contracts/domains/geology/Lithology.md`, and related Geology contracts are observed, but exact surficial schema pairing remains NEEDS VERIFICATION. |
| Default posture | Public-safe at map-unit scale when evidence, rights, validation, policy, release, correction, and rollback support are present. |
| Required reviewers | Schema steward, Geology steward, Surficial steward, contract steward, validation steward, policy/release stewards where applicable, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the machine-checkable shape root and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says domain-specific schemas nest under `schemas/contracts/v1/domains/<domain>/...`, while `contracts/` retains object meaning and `schemas/` owns machine-checkable shape.

Current-session Directory Rules evidence confirms field-level shape belongs under `schemas/`, while lifecycle data, registries, proofs, receipts, and release materials are separate responsibility roots and parallel homes require ADR review.

Current-session evidence confirms `schemas/contracts/v1/domains/geology/README.md` exists as a PROPOSED Geology domain schema scaffold. That parent file still needs expansion and does not by itself prove this sublane is canonical.

Current-session Geology surficial docs confirm the sublane covers Quaternary and unconsolidated map units, including alluvium, terrace deposits, loess/eolian cover, glacial material where applicable, colluvium, and residuum.

Current-session Geology surficial docs also say the `sublanes/` segment is PROPOSED / NEEDS VERIFICATION and recommends an ADR before freezing the convention.

Current-session search found `pipelines/domains/geology/surficial_units/README.md` and Geology surficial docs. Those are adjacent implementation or documentation surfaces, not schema authority.

Current-session evidence from `contracts/domains/geology/GeologicUnit.md` says exact paired schema path/casing for `GeologicUnit` was not found, and that the object must not replace `SurficialUnit`, Soil objects, Hydrology measurements, Hazards context, or release approval.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    └── v1/
        └── domains/
            └── geology/
                ├── README.md
                └── sublanes/
                    └── surficial/
                        └── README.md

contracts/
└── domains/
    └── geology/
        ├── GeologicUnit.md
        └── Lithology.md

docs/
└── domains/
    └── geology/
        ├── surficial.md
        └── sublanes/
            └── surficial.md

pipelines/
└── domains/
    └── geology/
        └── surficial_units/

data/
release/
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/contracts/v1/domains/geology/sublanes/surficial/README.md` | Blank before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms domain schemas nest under `schemas/contracts/v1/domains/<domain>/...`. |
| Directory Rules | Confirms machine shape belongs under `schemas/`; parallel homes require ADR review. |
| `schemas/contracts/v1/domains/geology/README.md` | Existing parent Geology schema scaffold; status PROPOSED. |
| Search for Geology surficial surfaces | Found surficial docs, a surficial-units pipeline, and Geology semantic contracts. |
| `docs/domains/geology/sublanes/surficial.md` | Surficial doctrine; confirms the scope and says the `sublanes/` segment remains PROPOSED / NEEDS VERIFICATION. |
| `docs/domains/geology/surficial.md` | Flat surficial doctrine file; confirms SurficialUnit, mostly public-safe posture, and object-family naming drift. |
| `contracts/domains/geology/GeologicUnit.md` | Semantic contract; exact paired schema path was not found and adjacent-domain boundaries remain explicit. |

This README does not verify complete schema fields, schema registry entries, fixture coverage, validator wiring, CI behavior, source-registry behavior, policy behavior, release integration, runtime behavior, public API behavior, or map rendering behavior.

## Candidate schema inventory

| Candidate schema | Status | Notes |
|---|---|---|
| `surficial_unit.schema.json` | NEEDS VERIFICATION | Candidate shape for mapped unconsolidated or semi-consolidated surface-cover units. |
| `surficial_map_unit.schema.json` | NEEDS VERIFICATION | Candidate public/map-facing unit shape if distinct from `SurficialUnit`. |
| `surficial_boundary_version.schema.json` | NEEDS VERIFICATION | Candidate boundary-version shape for surficial units. |
| `surficial_lithology_context.schema.json` | NEEDS VERIFICATION | Candidate context/reference shape; should not replace `Lithology`. |
| `surficial_age_context.schema.json` | NEEDS VERIFICATION | Candidate Quaternary/age context shape; should not replace broader Geology age/stratigraphy. |
| `surficial_soil_parent_material_link.schema.json` | NEEDS VERIFICATION | Candidate reference to Soil parent-material context; must not replace Soil truth. |
| `surficial_hydrology_context.schema.json` | NEEDS VERIFICATION | Candidate context/reference shape; must not replace Hydrology measurement truth. |
| `surficial_public_derivative.schema.json` | NEEDS VERIFICATION | Candidate public-safe derivative shape with rights, generalization, release, and rollback references. |

## Sublane responsibilities

| Responsibility | Expectation |
|---|---|
| Sublane schema index | Track surficial schema candidates and accepted schema files. |
| Parent-domain discipline | Keep this lane Geology-owned and subordinate to the parent Geology schema lane. |
| Contract pairing | Link each schema to paired semantic contracts under `contracts/domains/geology/` or accepted sublane contract paths when verified. |
| Sublane convention discipline | Mark the `sublanes/` segment NEEDS VERIFICATION until an ADR or steward decision freezes it. |
| Cross-lane discipline | Reference Soil, Hydrology, Hazards, and Archaeology as adjacent contexts only; do not duplicate their canonical truth. |
| Boundary preservation | Keep policy, fixtures, validators, pipelines, lifecycle data, source registry records, proofs, receipts, catalog records, and release records in their own responsibility roots. |
| Drift prevention | Prevent duplicate canonical schema definitions across parent Geology, sublane, cross-domain, and common schema paths. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## What belongs here

- This README.
- Machine-checkable surficial Geology JSON Schema files once placement is confirmed.
- Sublane schema index notes.
- Migration notes for surficial schema placement.
- Drift notes about duplicate or stale surficial schema paths.
- Links to paired contracts, fixtures, validators, schema registry records, policy references, source-registry references, release references, correction references, rollback references, and tests.

## What does not belong here

- Geology contract prose.
- Policy rules.
- Validator implementation code.
- Runtime code.
- Pipeline implementation.
- Lifecycle data payloads.
- Source registry records or SourceDescriptor instances.
- Emitted receipts.
- Proof outputs.
- Catalog records.
- Release records, release manifests, or release decisions.
- Public API or map/UI behavior.
- Soil map-unit truth, Hydrology measurement truth, Hazards risk truth, Archaeology site truth, or land/title claims.
- Bedrock-only, structure-only, borehole-only, geophysics-only, or resource/extraction schemas that belong to other Geology facets.
- Cross-domain schemas that belong under `schemas/contracts/v1/cross/` or another lowest-common responsibility root.
- Generic reusable schemas that belong under `schemas/contracts/v1/common/`.
- Claims that a schema is complete without fixtures, validators, registry records, and steward review support.

## Schema status values

Use finite status values where possible:

| Status | Meaning |
|---|---|
| `INDEX_ONLY` | This path only indexes candidate surficial schema locations. |
| `SUBLANE_CANDIDATE` | The `sublanes/surficial/` path may become an accepted schema sublane. |
| `DRAFT_SCHEMA` | Schema exists but still needs review and test support. |
| `ACTIVE_SCHEMA` | Schema has accepted contract pairing, fixtures, validator support, registry record, and review status. |
| `MIGRATE_TO_GEOLOGY_ROOT` | Content belongs directly under `schemas/contracts/v1/domains/geology/`. |
| `MIGRATE_TO_CROSS` | Content belongs under a cross-domain schema lane. |
| `MIGRATE_TO_COMMON` | Content belongs under a common reusable schema family. |
| `DEPRECATED` | Content should no longer receive new consumers. |
| `NEEDS_VERIFICATION` | Pairing, fixture, validator, registry, review, or CI support has not been verified. |

## Review checklist

- [ ] Canonical schema path is linked or marked NEEDS VERIFICATION.
- [ ] `sublanes/` placement is accepted by ADR/steward decision or marked NEEDS VERIFICATION.
- [ ] Paired contract path is linked or marked NEEDS VERIFICATION.
- [ ] Parent Geology object relationship is explicit.
- [ ] Adjacent-domain references preserve Soil, Hydrology, Hazards, Archaeology, and land/title boundaries.
- [ ] Schema registry entry is linked or marked NEEDS VERIFICATION.
- [ ] Valid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Invalid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Validator path is linked or marked NEEDS VERIFICATION.
- [ ] CI/schema-test support is linked or marked NEEDS VERIFICATION.
- [ ] Pipeline, data, registry, proof, receipt, catalog, and release records remain outside `schemas/`.
- [ ] Any migration or compatibility claim cites an ADR, migration note, or verified repo evidence.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/contracts/v1/domains/geology/sublanes/surficial/`.
- [ ] Confirm whether the `sublanes/` segment is accepted for schema paths or should remain a proposed convention.
- [ ] Confirm whether surficial schemas should live here, directly under `schemas/contracts/v1/domains/geology/`, or under a cross-domain lane.
- [ ] Confirm complete Geology schema inventory.
- [ ] Confirm paired Geology contract paths for `SurficialUnit` and related objects.
- [ ] Confirm whether `SurficialUnit` is a distinct object family or a subtype/profile of `GeologicUnit`.
- [ ] Confirm schema registry records.
- [ ] Confirm fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm policy, source-registry, release, correction, and rollback references for surficial schemas.
- [ ] Confirm whether `schemas/contracts/v1/domains/geology/README.md` should index this sublane.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | Sublane placement decision, new surficial schema, `SurficialUnit` object-family decision, schema-home migration, validator update, fixture update, schema registry update, ADR update, Geology contract update, policy/release reference update, or compatibility-lane decision |
