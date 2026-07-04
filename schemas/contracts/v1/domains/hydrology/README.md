# `schemas/contracts/v1/domains/hydrology/` — Hydrology Domain Schema Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-domains-hydrology-readme
title: schemas/contracts/v1/domains/hydrology/ — Hydrology Domain Schema Index
version: v1
status: draft
policy_label: public
owners:
  - <schema-steward>
  - <hydrology-domain-steward>
  - <contract-steward>
  - <validation-steward>
  - <source-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, contracts, v1, domains, hydrology, huc, gauge, flow-observation, watershed, json-schema]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![domain](https://img.shields.io/badge/domain-hydrology-blue)
![posture](https://img.shields.io/badge/posture-domain--schema--index-orange)
![canonical](https://img.shields.io/badge/canonical-PROPOSED-yellow)

## Purpose

`schemas/contracts/v1/domains/hydrology/` is the draft Hydrology domain schema lane.

This path is for machine-checkable Hydrology schema shapes: JSON Schema files, schema-family README files, schema index notes, migration notes, and links to paired contracts, fixtures, validators, registry records, tests, policy references, source-registry references, correction references, rollback references, and release references.

This path is not a home for Hydrology contract prose, policy rules, validator code, packages, pipelines, lifecycle data, source registry records, emitted receipts, proof outputs, catalog records, release records, review records, or public map/API artifacts.

This README is documentation only. It is not itself a schema file, contract prose, policy, validator code, pipeline code, lifecycle data, registry data, proof output, receipt instance, source descriptor instance, or release authority.

## Status & authority

| Field | Value |
|---|---|
| Document type | Hydrology domain schema README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/v1/domains/hydrology/` |
| Status | Draft |
| Authority level | Domain schema index guidance. Schema files, paired contracts, registry records, validators, fixtures, tests, ADRs, policy records, release records, and steward decisions outrank this README. |
| Path posture | Current-session evidence confirms this README existed as a greenfield scaffold before this update. |
| Canonical posture | PROPOSED Hydrology domain schema lane under ADR-0001 and Hydrology canonical-paths guidance. Implementation completeness remains NEEDS VERIFICATION. |
| Path drift note | Current contracts README records flat-vs-domain path-form drift from older atlas/crosswalk material; keep migration/drift visible until resolved. |
| Concrete schema inventory | NEEDS VERIFICATION. Current-session search found Hydrology docs/contracts but did not confirm concrete `.schema.json` files under this path. |
| Known child lanes | None confirmed during this edit. |
| Required reviewers | Schema steward, Hydrology domain steward, contract steward, validation steward, source steward, policy/release stewards where applicable, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the machine-checkable shape root and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says domain-specific schemas nest under `schemas/contracts/v1/domains/<domain>/...`, while `contracts/` retains object meaning and `schemas/` owns machine-checkable shape.

Current-session Directory Rules evidence confirms field-level shape belongs under `schemas/`, while lifecycle data, registries, proofs, receipts, policy decisions, and release materials are separate responsibility roots and parallel homes require ADR review.

Current-session evidence confirms this README previously claimed broadly that docs, contracts, schemas, policies, fixtures, tests, packages, pipelines, registries, and data lifecycle artifacts could belong here. This update corrects that boundary: this path is schema-shape only.

Current-session Hydrology canonical-paths evidence names `schemas/contracts/v1/domains/hydrology/` as the machine-shape lane and states Hydrology schemas default to this path under the schema-home rule.

Current-session Hydrology contract-root evidence says `contracts/domains/hydrology/` owns human-readable meaning, while machine shape belongs in `schemas/contracts/v1/domains/hydrology/`. It also records that some older atlas/crosswalk material proposed flat `contracts/hydrology/` and `schemas/contracts/v1/hydrology/` forms, leaving path form CONFLICTED / NEEDS VERIFICATION before promotion.

Current-session search found Hydrology semantic contract surfaces such as `flow_observation.md`, `watershed.md`, `gauge_site.md`, `water_use_link.md`, `domain_observation.md`, `huc_unit.md`, `hydro_feature.md`, `evidence_bundle.md`, `reach_identity.md`, and `domain_layer_descriptor.md`.

Current-session search did not confirm concrete Hydrology `.schema.json` files under `schemas/contracts/v1/domains/hydrology/`.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    └── v1/
        └── domains/
            └── hydrology/
                └── README.md                  # you are here

contracts/
└── domains/
    └── hydrology/                              # semantic meaning; not schema shape

docs/
└── domains/
    └── hydrology/                              # human-facing doctrine; not schema shape

policy/
└── domains/hydrology/                          # policy; not schema shape

fixtures/
└── domains/hydrology/                          # test examples; coverage NEEDS VERIFICATION

data/                                           # lifecycle, registry, proof, receipt roots; not schema home

release/                                        # release decisions and release records; not schema home
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/contracts/v1/domains/hydrology/README.md` | Greenfield scaffold before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms domain schemas nest under `schemas/contracts/v1/domains/<domain>/...`. |
| Directory Rules | Confirms machine shape belongs under `schemas/`; parallel homes require ADR review. |
| `docs/domains/hydrology/CANONICAL_PATHS.md` | Names `schemas/contracts/v1/domains/hydrology/` as the Hydrology machine-shape lane and records schema-home rule. |
| `contracts/domains/hydrology/README.md` | Confirms contracts own meaning, schemas own shape, and path-form drift remains visible. |
| Search for Hydrology schema/contract surfaces | Found Hydrology contracts and docs; did not confirm concrete schema files under this path. |

This README does not verify complete Hydrology schema coverage, schema registry entries, fixture coverage, validator wiring, CI behavior, source-admission behavior, policy behavior, release integration, runtime behavior, public API behavior, or map rendering behavior.

## Current schema inventory

| Schema file | Paired contract | Status | Notes |
|---|---|---|---|
| No concrete `.schema.json` file confirmed in this edit | N/A | NEEDS VERIFICATION | Current-session search found Hydrology contracts and docs but did not confirm concrete Hydrology schemas under this path. |

## Current child lanes

| Child path | Status | Responsibility |
|---|---|---|
| No child schema lane confirmed in this edit | NEEDS VERIFICATION | Add child lanes only after schema-home and object-family review confirm a need. |

## Candidate schema inventory

Hydrology schema candidates below come from current Hydrology contract/docs evidence. They require steward review, schema files, paired contracts, fixtures, validators, registry records, source-role semantics, and CI support before promotion.

| Candidate schema | Status | Notes |
|---|---|---|
| `watershed.schema.json` | NEEDS VERIFICATION | Candidate watershed object shape. |
| `huc_unit.schema.json` | NEEDS VERIFICATION | Candidate HUC unit identity and boundary/reference shape. |
| `hydro_feature.schema.json` | NEEDS VERIFICATION | Candidate hydrologic feature shape. |
| `reach_identity.schema.json` | NEEDS VERIFICATION | Candidate deterministic reach identity shape. |
| `gauge_site.schema.json` | NEEDS VERIFICATION | Candidate gauge/site metadata shape. |
| `flow_observation.schema.json` | NEEDS VERIFICATION | Candidate flow observation shape. |
| `water_level_observation.schema.json` | NEEDS VERIFICATION | Candidate water-level observation shape. |
| `water_quality_observation.schema.json` | NEEDS VERIFICATION | Candidate water-quality observation shape. |
| `groundwater_well.schema.json` | NEEDS VERIFICATION | Candidate groundwater well/reference shape. |
| `aquifer_observation.schema.json` | NEEDS VERIFICATION | Candidate aquifer observation shape. |
| `nfhl_zone.schema.json` | NEEDS VERIFICATION | Candidate regulatory flood-zone context shape. |
| `observed_flood_event.schema.json` | NEEDS VERIFICATION | Candidate observed flood event shape with evidence support. |
| `flood_context.schema.json` | NEEDS VERIFICATION | Candidate flood context envelope shape. |
| `hydrograph.schema.json` | NEEDS VERIFICATION | Candidate hydrograph shape. |
| `upstream_trace.schema.json` | NEEDS VERIFICATION | Candidate upstream trace/network traversal shape. |
| `water_use_link.schema.json` | NEEDS VERIFICATION | Candidate cross-domain water-use link shape. |
| `domain_observation.schema.json` | NEEDS VERIFICATION | Candidate domain observation envelope. |
| `domain_layer_descriptor.schema.json` | NEEDS VERIFICATION | Candidate layer descriptor shape; not release authority. |
| `evidence_bundle_ref.schema.json` | NEEDS VERIFICATION | Candidate evidence-reference/profile shape; proof authority remains outside this README. |

## Schema-lane responsibilities

| Responsibility | Expectation |
|---|---|
| Domain schema index | List Hydrology schema files and child schema lanes as they are verified. |
| Contract pairing | Link each schema to paired semantic contracts under `contracts/domains/hydrology/` or another verified contract lane. |
| Path-drift discipline | Keep flat-vs-domain path drift visible until ADR/steward resolution confirms final homes. |
| Source-role discipline | Preserve differences among observation, regulatory context, model output, derived summary, and candidate records. |
| Boundary preservation | Keep policy, fixtures, validators, pipelines, lifecycle data, source registry records, receipt instances, proofs, catalog records, and release records in their own responsibility roots. |
| Adjacent-domain discipline | Hydrology may reference Hazards, Atmosphere, Soil, Agriculture, Geology, Habitat, Infrastructure, Roads/Rail/Trade, land/title, and People context, but must not replace their owned truth. |
| Drift prevention | Prevent duplicate canonical schema definitions across requested domain path, possible flat Hydrology path, child lanes, cross-domain lanes, and common schema families. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## What belongs here

- This README.
- Machine-checkable Hydrology JSON Schema files once placement is confirmed.
- Hydrology schema-family and child-lane README files.
- Schema index notes.
- Migration notes for Hydrology schema placement.
- Drift notes about duplicate or stale Hydrology schema paths.
- Links to paired contracts, fixtures, validators, schema registry records, source-registry records, policy references, release references, correction references, rollback references, and tests.

## What does not belong here

- Contract prose.
- Policy rules or sensitivity decisions.
- Validator implementation code.
- Runtime code.
- Packages or pipeline implementation.
- Lifecycle data payloads.
- Source registry records or SourceDescriptor instances.
- Emitted receipt instances.
- Proof outputs or EvidenceBundles.
- Catalog records.
- Release records, release manifests, or release decisions.
- Public tiles, map/UI behavior, dashboards, screenshots, or generated summaries.
- Canonical Soil, Agriculture, Geology, Infrastructure, Habitat, Fauna, Flora, land/title, People, or Spatial Foundation truth.
- Cross-domain schemas that belong under `schemas/contracts/v1/cross/` or another lowest-common responsibility root.
- Generic reusable schemas that belong under `schemas/contracts/v1/common/`.
- Claims that a schema is complete without fixtures, validators, registry records, and steward review support.

## Schema status values

| Status | Meaning |
|---|---|
| `STUB` | Schema exists but is not field-complete. |
| `DRAFT_SCHEMA` | Schema has meaningful fields but still needs review and test support. |
| `ACTIVE_SCHEMA` | Schema has accepted contract pairing, fixtures, validator support, registry record, and review status. |
| `PATH_CONFLICT` | Schema placement is blocked by unresolved flat-vs-domain Hydrology schema-home drift. |
| `PROFILE` | Schema profiles a shared source, spatial, time, or common schema without creating duplicate authority. |
| `MIRROR` | Schema mirrors another accepted schema location. |
| `TRANSITIONAL` | Schema is awaiting migration to the accepted home. |
| `DEPRECATED` | Schema should no longer receive new consumers. |
| `NEEDS_VERIFICATION` | Pairing, fixture, validator, registry, review, or CI support has not been verified. |

## Review checklist

- [ ] Schema has a stable `$id`.
- [ ] Schema has `$schema` set to JSON Schema draft 2020-12 unless an ADR says otherwise.
- [ ] Paired contract path is linked or marked NEEDS VERIFICATION.
- [ ] Flat-vs-domain schema-home drift is resolved or explicitly marked PROPOSED / CONFLICTED.
- [ ] Schema registry entry is linked or marked NEEDS VERIFICATION.
- [ ] Valid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Invalid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Source-role and temporal-basis behavior is linked or marked NEEDS VERIFICATION where relevant.
- [ ] Validator path is linked or marked NEEDS VERIFICATION.
- [ ] CI/schema-test support is linked or marked NEEDS VERIFICATION.
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
watershed.schema.json
huc_unit.schema.json
hydro_feature.schema.json
reach_identity.schema.json
gauge_site.schema.json
flow_observation.schema.json
water_level_observation.schema.json
water_quality_observation.schema.json
groundwater_well.schema.json
aquifer_observation.schema.json
nfhl_zone.schema.json
observed_flood_event.schema.json
flood_context.schema.json
hydrograph.schema.json
upstream_trace.schema.json
water_use_link.schema.json
domain_observation.schema.json
domain_layer_descriptor.schema.json
evidence_bundle_ref.schema.json
```

Use lowercase snake_case for schema filenames unless the schema registry or ADR specifies otherwise. Do not silently create duplicate schemas across `schemas/contracts/v1/domains/hydrology/`, `schemas/contracts/v1/hydrology/`, cross-domain, or common schema paths.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/contracts/v1/domains/hydrology/`.
- [ ] Resolve flat-vs-domain Hydrology schema-home drift noted by `contracts/domains/hydrology/README.md`.
- [ ] Confirm complete Hydrology schema inventory.
- [ ] Confirm whether concrete schema files exist under alternate casing or alternate paths.
- [ ] Confirm paired contract paths for all accepted schemas.
- [ ] Confirm schema registry records.
- [ ] Confirm valid fixture paths.
- [ ] Confirm invalid fixture paths.
- [ ] Confirm source-role and temporal-basis fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm policy, source-registry, release, correction, and rollback references for Hydrology schemas.
- [ ] Confirm whether `schemas/README.md` should index this Hydrology domain schema lane.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing greenfield scaffold |
| Next review trigger | Hydrology schema-home resolution, new Hydrology schema, child-lane decision, schema-home migration, validator update, fixture update, schema registry update, ADR update, Hydrology contract update, source-role/policy update, policy/release reference update, or compatibility-lane decision |
