# `schemas/contracts/v1/domains/habitat/` — Habitat Domain Schema Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-domains-habitat-readme
title: schemas/contracts/v1/domains/habitat/ — Habitat Domain Schema Index
version: v1
status: draft
policy_label: public
owners:
  - <schema-steward>
  - <habitat-domain-steward>
  - <contract-steward>
  - <validation-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, contracts, v1, domains, habitat, land-cover, ecoregions, json-schema]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![domain](https://img.shields.io/badge/domain-habitat-green)
![posture](https://img.shields.io/badge/posture-domain--schema--index-orange)
![canonical](https://img.shields.io/badge/canonical-PROPOSED-yellow)

## Purpose

`schemas/contracts/v1/domains/habitat/` is the draft Habitat domain schema lane.

This path is for machine-checkable Habitat schema shapes: JSON Schema files, schema-family README files, schema index notes, migration notes, and links to paired contracts, fixtures, validators, registry records, tests, policy references, source-registry references, correction references, rollback references, and release references.

This path is not a home for Habitat contract prose, policy rules, validator code, packages, pipelines, pipeline specs, lifecycle data, source registry records, emitted receipts, proof outputs, catalog records, release records, review records, or public map/API artifacts.

This README is documentation only. It is not itself a schema file, contract prose, policy, validator code, pipeline code, lifecycle data, registry data, proof output, receipt instance, source descriptor instance, catalog record, or release authority.

## Status & authority

| Field | Value |
|---|---|
| Document type | Habitat domain schema README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/v1/domains/habitat/` |
| Status | Draft |
| Authority level | Domain schema index guidance. Schema files, paired contracts, registry records, validators, fixtures, tests, ADRs, policy records, release records, and steward decisions outrank this README. |
| Path posture | Current-session evidence confirms this README existed as a greenfield scaffold before this update. |
| Canonical posture | PROPOSED Habitat domain schema lane under ADR-0001. Implementation completeness remains NEEDS VERIFICATION. |
| Known child lanes | `land_cover/` and `ecoregions/` READMEs exist as draft schema indexes. |
| Confirmed concrete schema file | `land_cover/observation.schema.json` exists as a PROPOSED scaffold. |
| Ecoregions schema inventory | NEEDS VERIFICATION. The ecoregions lane is currently an index with candidate names but no confirmed concrete schema file in this edit. |
| Required reviewers | Schema steward, Habitat domain steward, relevant sublane steward, contract steward, validation steward, policy/release stewards where applicable, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the machine-checkable shape root and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says domain-specific schemas nest under `schemas/contracts/v1/domains/<domain>/...`, while `contracts/` retains object meaning and `schemas/` owns machine-checkable shape.

Current-session Directory Rules evidence confirms field-level shape belongs under `schemas/`, while lifecycle data, registries, proofs, receipts, and release materials are separate responsibility roots and parallel homes require ADR review.

Current-session evidence confirms this README previously claimed broadly that docs, contracts, schemas, policies, fixtures, tests, packages, pipelines, registries, and data lifecycle artifacts could belong here. This update corrects that boundary: this path is schema-shape only.

Current-session Habitat domain evidence identifies `schemas/contracts/v1/domains/habitat/` as the machine-shape home while keeping implementation maturity PROPOSED / NEEDS VERIFICATION.

Current-session evidence confirms `schemas/contracts/v1/domains/habitat/land_cover/README.md` exists as a draft Habitat Land Cover schema index and records `land_cover/observation.schema.json` as a PROPOSED scaffold paired with `contracts/domains/habitat/land_cover/observation.md`.

Current-session evidence confirms `schemas/contracts/v1/domains/habitat/ecoregions/README.md` exists as a draft Habitat Ecoregions schema index and keeps its concrete schema inventory NEEDS VERIFICATION.

Current-session search found Habitat land-cover contracts, fixtures, docs, and ecoregion doctrine. It did not confirm a complete Habitat-wide schema inventory.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    └── v1/
        └── domains/
            └── habitat/
                ├── README.md                    # you are here
                ├── ecoregions/
                │   └── README.md                # draft schema index
                └── land_cover/
                    ├── README.md                # draft schema index
                    └── observation.schema.json   # confirmed PROPOSED scaffold

contracts/
└── domains/
    └── habitat/                                  # semantic meaning; not schema shape
        ├── land_cover/
        ├── SuitabilityModel.md
        └── suitability_model.md

docs/
└── domains/
    └── habitat/                                  # human-facing doctrine; not schema shape

policy/
└── domains/habitat/                              # admissibility/policy; not schema shape

fixtures/
└── domains/habitat/                              # test examples; coverage NEEDS VERIFICATION

data/                                             # lifecycle, registry, proof, receipt roots; not schema home

release/                                          # release decisions and release records; not schema home
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/contracts/v1/domains/habitat/README.md` | Greenfield scaffold before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms domain schemas nest under `schemas/contracts/v1/domains/<domain>/...`. |
| Directory Rules | Confirms machine shape belongs under `schemas/`; parallel homes require ADR review. |
| `docs/domains/habitat/README.md` | Confirms Habitat's role and names the schema responsibility lane. |
| `schemas/contracts/v1/domains/habitat/land_cover/README.md` | Existing Land Cover schema index; confirms `observation.schema.json` scaffold. |
| `schemas/contracts/v1/domains/habitat/ecoregions/README.md` | Existing Ecoregions schema index; concrete schemas remain NEEDS VERIFICATION. |
| Search for Habitat schema surfaces | Found land-cover contract/fixture/doc surfaces and ecoregion doctrine; did not confirm complete Habitat schema coverage. |

This README does not verify complete Habitat schema coverage, schema registry entries, fixture coverage, validator wiring, CI behavior, policy behavior, release integration, runtime behavior, public API behavior, or map rendering behavior.

## Current schema inventory

| Schema file | Paired contract | Status | Notes |
|---|---|---|---|
| `land_cover/observation.schema.json` | `contracts/domains/habitat/land_cover/observation.md` | PROPOSED scaffold | Confirmed file exists, but field-level enforcement remains NEEDS VERIFICATION. |

## Current child lanes

| Child path | Status | Responsibility |
|---|---|---|
| `land_cover/` | Draft schema index | Habitat land-cover schema lane with confirmed `observation.schema.json` scaffold. |
| `ecoregions/` | Draft schema index / NEEDS VERIFICATION | Habitat ecoregions and landscape-regionalization schema lane; candidate schema names only in current evidence. |

## Candidate schema inventory

Habitat schema candidates below require steward review, schema files, paired contracts, fixtures, validators, registry records, and CI support before promotion.

| Candidate schema | Status | Notes |
|---|---|---|
| `land_cover/observation.schema.json` | PROPOSED scaffold | Current `LandCoverObservation` shape scaffold. |
| `land_cover/class_scheme.schema.json` | NEEDS VERIFICATION | Candidate land-cover class scheme shape. |
| `land_cover/crosswalk.schema.json` | NEEDS VERIFICATION | Candidate class-crosswalk shape. |
| `land_cover/change_summary.schema.json` | NEEDS VERIFICATION | Candidate land-cover change summary shape. |
| `land_cover/uncertainty.schema.json` | NEEDS VERIFICATION | Candidate uncertainty/quality shape. |
| `ecoregions/ecoregion.schema.json` | NEEDS VERIFICATION | Candidate ecoregion object shape. |
| `ecoregions/ecoregion_snapshot.schema.json` | NEEDS VERIFICATION | Candidate framework/version snapshot shape. |
| `ecoregions/ecoregion_context_join.schema.json` | NEEDS VERIFICATION | Candidate governed context-join shape. |
| `suitability_model.schema.json` | NEEDS VERIFICATION | Candidate suitability model shape. |
| `habitat_patch.schema.json` | NEEDS VERIFICATION | Candidate HabitatPatch shape. |
| `connectivity_corridor.schema.json` | NEEDS VERIFICATION | Candidate connectivity/corridor shape. |
| `domain_feature_identity.schema.json` | NEEDS VERIFICATION | Candidate deterministic identity support shape. |
| `domain_validation_report.schema.json` | NEEDS VERIFICATION | Candidate validation-report shape; not proof or release authority. |

## Schema-lane responsibilities

| Responsibility | Expectation |
|---|---|
| Domain schema index | List Habitat schema files and child schema lanes as they are verified. |
| Contract pairing | Link each schema to paired semantic contracts under `contracts/domains/habitat/` or another verified contract lane. |
| Child-lane discipline | Keep `land_cover/` and `ecoregions/` scoped as schema sublanes, not parallel authority roots. |
| Boundary preservation | Keep policy, fixtures, validators, pipelines, pipeline specs, lifecycle data, source registry records, receipt instances, proofs, catalog records, and release records in their own responsibility roots. |
| Cross-lane discipline | Habitat schemas may reference Fauna, Flora, Hydrology, Soil, Hazards, Agriculture, Spatial Foundation, and land/people context, but must not replace their owned truth. |
| Drift prevention | Prevent duplicate canonical schema definitions across parent Habitat, child lanes, cross-domain lanes, and common schema families. |
| Fixture linkage | Point to valid, invalid, public-safe, and edge-case fixtures when verified. |
| Validator linkage | Point to validators or CI checks when verified. |
| Registry linkage | Point to schema registry records when verified. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## What belongs here

- This README.
- Machine-checkable Habitat JSON Schema files once placement is confirmed.
- Habitat schema-family and child-lane README files.
- Schema index notes.
- Migration notes for Habitat schema placement.
- Drift notes about duplicate or stale Habitat schema paths.
- Links to paired contracts, fixtures, validators, schema registry records, source-registry records, policy references, release references, correction references, rollback references, and tests.

## What does not belong here

- Contract prose.
- Policy rules or sensitivity decisions.
- Validator implementation code.
- Runtime code.
- Packages or pipeline implementation.
- Pipeline specs.
- Lifecycle data payloads.
- Source registry records or SourceDescriptor instances.
- Emitted receipt instances.
- Proof outputs.
- Catalog records.
- Release records, release manifests, or release decisions.
- Public tiles, map/UI behavior, dashboards, screenshots, or generated summaries.
- Species occurrence truth, plant occurrence truth, critical-habitat designation truth, crop truth, soil truth, hydrology truth, hazards truth, land/title truth, or public release approval.
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
| `PROFILE` | Schema profiles a shared source, spatial, raster, or common schema without creating duplicate authority. |
| `MIRROR` | Schema mirrors another accepted schema location. |
| `TRANSITIONAL` | Schema is awaiting migration to the accepted home. |
| `DEPRECATED` | Schema should no longer receive new consumers. |
| `NEEDS_VERIFICATION` | Pairing, fixture, validator, registry, review, or CI support has not been verified. |

## Minimal schema note

```markdown
# <habitat-schema-note-id>

## Status
STUB / DRAFT_SCHEMA / ACTIVE_SCHEMA / PROFILE / MIRROR / TRANSITIONAL / DEPRECATED / NEEDS_VERIFICATION

## Schema path
<schemas/contracts/v1/domains/habitat/...>

## Paired contract
<contracts/domains/habitat/... or N/A>

## Child lane
<root / land_cover / ecoregions / other / N/A>

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
- [ ] Child-lane placement is justified when schema is not at the Habitat schema root.
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
land_cover/observation.schema.json
land_cover/class_scheme.schema.json
land_cover/crosswalk.schema.json
land_cover/change_summary.schema.json
land_cover/uncertainty.schema.json
ecoregions/ecoregion.schema.json
ecoregions/ecoregion_snapshot.schema.json
ecoregions/ecoregion_context_join.schema.json
suitability_model.schema.json
habitat_patch.schema.json
connectivity_corridor.schema.json
domain_feature_identity.schema.json
domain_validation_report.schema.json
```

Use lowercase snake_case for schema filenames unless the schema registry or ADR specifies otherwise. If existing contracts use alternate naming, record the mismatch and do not silently rename without a migration note.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/contracts/v1/domains/habitat/`.
- [ ] Confirm complete Habitat schema inventory.
- [ ] Confirm whether any concrete schema files exist under alternate casing or alternate paths.
- [ ] Confirm paired contract paths for all accepted schemas.
- [ ] Confirm schema registry records.
- [ ] Confirm valid fixture paths.
- [ ] Confirm invalid fixture paths.
- [ ] Confirm public-safe/generalized fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm policy, source-registry, release, correction, and rollback references for Habitat schemas.
- [ ] Confirm whether `schemas/README.md` should index this Habitat domain schema lane.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing greenfield scaffold |
| Next review trigger | New Habitat schema, child-lane decision, schema-home migration, validator update, fixture update, schema registry update, ADR update, Habitat contract update, policy/release reference update, or compatibility-lane decision |
