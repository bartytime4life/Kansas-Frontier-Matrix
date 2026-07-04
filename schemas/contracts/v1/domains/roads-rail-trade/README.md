# `schemas/contracts/v1/domains/roads-rail-trade/` — Roads / Rail / Trade Domain Schema Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-domains-roads-rail-trade-readme
title: schemas/contracts/v1/domains/roads-rail-trade/ — Roads / Rail / Trade Domain Schema Index
version: v1
status: draft; PROPOSED; slug-CONFLICTED; schema-index
policy_label: public
owners:
  - <schema-steward>
  - <roads-rail-trade-domain-steward>
  - <roads-steward>
  - <rail-steward>
  - <trade-routes-steward>
  - <validation-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, contracts, v1, domains, roads-rail-trade, transport, roads, rail, trade-routes, routes, network, json-schema]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![domain](https://img.shields.io/badge/domain-roads--rail--trade-slategray)
![posture](https://img.shields.io/badge/posture-domain--schema--index-orange)
![slug](https://img.shields.io/badge/slug-PROPOSED%20%2F%20CONFLICTED-red)
![truth](https://img.shields.io/badge/truth-evidence--first-blue)

## Purpose

`schemas/contracts/v1/domains/roads-rail-trade/` is the draft Roads / Rail / Trade domain schema lane.

This path is for machine-checkable Roads / Rail / Trade schema shapes: JSON Schema files, schema-family README files, schema index notes, migration notes, and links to paired contracts, fixtures, validators, registry records, tests, policy references, source-registry references, correction references, rollback references, and release references.

This path is not a home for Roads / Rail / Trade contract prose, policy rules, validator code, packages, pipelines, lifecycle data, source registry records, emitted receipts, proof outputs, catalog records, release records, review records, public map/API artifacts, routing advice, legal road-status advice, or emergency access instructions.

This README is documentation only. It is not itself a schema file, contract prose, policy, validator code, pipeline code, lifecycle data, registry data, proof output, receipt instance, source descriptor instance, route authority, network authority, or release authority.

## Status & authority

| Field | Value |
|---|---|
| Document type | Roads / Rail / Trade domain schema README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/v1/domains/roads-rail-trade/` |
| Status | Draft / PROPOSED / slug-CONFLICTED |
| Authority level | Domain schema index guidance. Schema files, paired contracts, registry records, validators, fixtures, tests, ADRs, policy records, release records, and steward decisions outrank this README. |
| Path posture | Current-session evidence confirms this README existed as a greenfield scaffold before this update. |
| Canonical posture | PROPOSED under Directory Rules and ADR-0001; slug/path conflict remains visible because Roads/Rail/Trade docs record unresolved `roads-rail-trade` vs `transport` and `domains/` vs flat-path drift. |
| Concrete schema inventory | NEEDS VERIFICATION. Current-session search found semantic contracts and docs but did not confirm concrete `.schema.json` files under this path. |
| Known child lanes | None confirmed during this edit. |
| Default public posture | Public-safe for many historical/contextual transport features after evidence, rights, source-role, validation, policy, release, correction, and rollback support; not live routing or legal-status authority. |
| Required reviewers | Schema steward, Roads/Rail/Trade steward, roads steward, rail steward, trade-routes steward, validation steward, policy/release stewards where applicable, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the machine-checkable shape root and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says domain-specific schemas nest under `schemas/contracts/v1/domains/<domain>/...`, while `contracts/` retains object meaning and `schemas/` owns machine-checkable shape.

Current-session Directory Rules evidence confirms field-level shape belongs under `schemas/`, while lifecycle data, registries, proofs, receipts, policy decisions, and release materials are separate responsibility roots and parallel homes require ADR review.

Current-session evidence confirms this README previously claimed broadly that docs, contracts, schemas, policies, fixtures, tests, packages, pipelines, registries, and data lifecycle artifacts could belong here. This update corrects that boundary: this path is schema-shape only.

Current-session Roads/Rail/Trade file-system evidence names `schemas/contracts/v1/domains/roads-rail-trade/` as the schema responsibility lane while keeping the `roads-rail-trade` vs `transport` naming conflict visible and ADR-bound.

Current-session Roads/Rail/Trade canonical-paths evidence records a two-dimensional conflict: Directory Rules uses `schemas/contracts/v1/domains/<domain>/` with the `roads-rail-trade` slug, while older Atlas crosswalk material used flat `schemas/contracts/v1/transport/` style paths. This README does not resolve that conflict.

Current-session Roads/Rail/Trade contract-root evidence confirms `contracts/domains/roads-rail-trade/` is a human-readable semantic contract lane, not a schema, policy, data, fixture, release, API, map, graph, or runtime authority.

Current-session search found Roads/Rail/Trade semantic contract surfaces such as `corridor_route.md`, `rail_segment.md`, `route_membership.md`, `bridge.md`, `access_restriction.md`, `restriction_event.md`, `operator_assignment.md`, `status_event.md`, `siding.md`, `depot.md`, `yard.md`, `operator_status.md`, `domain_observation.md`, and `transport_facility.md`.

Current-session search did not confirm concrete Roads/Rail/Trade `.schema.json` files under `schemas/contracts/v1/domains/roads-rail-trade/`.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    └── v1/
        └── domains/
            └── roads-rail-trade/
                └── README.md                  # you are here

contracts/
└── domains/
    └── roads-rail-trade/                       # semantic meaning; not schema shape
        ├── corridor_route.md
        ├── rail_segment.md
        ├── route_membership.md
        ├── bridge.md
        ├── access_restriction.md
        ├── restriction_event.md
        ├── operator_assignment.md
        ├── status_event.md
        ├── siding.md
        ├── depot.md
        └── yard.md

docs/
└── domains/
    └── roads-rail-trade/                       # human-facing doctrine and placement docs

policy/
└── domains/roads-rail-trade/                   # policy; not schema shape

fixtures/
└── domains/roads-rail-trade/                   # test examples; coverage NEEDS VERIFICATION

data/                                           # lifecycle, registry, proof, receipt roots; not schema home

release/                                        # release decisions and release records; not schema home
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/contracts/v1/domains/roads-rail-trade/README.md` | Greenfield scaffold before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms domain schemas nest under `schemas/contracts/v1/domains/<domain>/...`. |
| Directory Rules | Confirms machine shape belongs under `schemas/`; parallel homes require ADR review. |
| `docs/domains/roads-rail-trade/FILE_SYSTEM_PLAN.md` | Names this schema lane and records lane placement plus slug drift. |
| `docs/domains/roads-rail-trade/CANONICAL_PATHS.md` | Records the `roads-rail-trade` vs `transport` and `domains/` vs flat-path conflict. |
| `contracts/domains/roads-rail-trade/README.md` | Confirms contracts own meaning and that the folder is not schema, policy, data, release, public API, map, graph, or runtime authority. |
| Search for Roads/Rail/Trade schema/contract surfaces | Found semantic contracts and docs; did not confirm concrete schema files under this path. |

This README does not verify complete Roads/Rail/Trade schema coverage, schema registry entries, fixture coverage, validator wiring, CI behavior, source-admission behavior, policy behavior, release integration, runtime behavior, public API behavior, graph materialization, routing behavior, or map rendering behavior.

## Current schema inventory

| Schema file | Paired contract | Status | Notes |
|---|---|---|---|
| No concrete `.schema.json` file confirmed in this edit | N/A | NEEDS VERIFICATION | Current-session search found contracts/docs but did not confirm concrete schema files under this path. |

## Current child lanes

| Child path | Status | Responsibility |
|---|---|---|
| No child schema lane confirmed in this edit | NEEDS VERIFICATION | Add child lanes only after schema-home, slug, and object-family review confirm a need. |

## Candidate schema inventory

Roads/Rail/Trade schema candidates below come from current contract/docs evidence. They require steward review, schema files, paired contracts, fixtures, validators, registry records, source-role semantics, and CI support before promotion.

| Candidate schema | Status | Notes |
|---|---|---|
| `road_segment.schema.json` | NEEDS VERIFICATION | Candidate road segment shape. |
| `rail_segment.schema.json` | NEEDS VERIFICATION | Candidate rail segment shape. |
| `corridor_route.schema.json` | NEEDS VERIFICATION | Candidate corridor or route object shape. |
| `route_membership.schema.json` | NEEDS VERIFICATION | Candidate segment-to-route/corridor membership shape. |
| `bridge.schema.json` | NEEDS VERIFICATION | Candidate transport-side bridge/crossing shape; must not replace infrastructure or hydrology truth. |
| `river_crossing.schema.json` | NEEDS VERIFICATION | Candidate transport-side river crossing shape; hydrology owns water evidence. |
| `ferry.schema.json` | NEEDS VERIFICATION | Candidate ferry crossing/service shape. |
| `depot.schema.json` | NEEDS VERIFICATION | Candidate depot/facility shape. |
| `siding.schema.json` | NEEDS VERIFICATION | Candidate rail siding shape. |
| `yard.schema.json` | NEEDS VERIFICATION | Candidate rail yard shape. |
| `transport_facility.schema.json` | NEEDS VERIFICATION | Candidate shared transport facility shape. |
| `operator_assignment.schema.json` | NEEDS VERIFICATION | Candidate operator/time assignment shape. |
| `operator_status.schema.json` | NEEDS VERIFICATION | Candidate operator/status shape. |
| `status_event.schema.json` | NEEDS VERIFICATION | Candidate time-bound status event shape. |
| `restriction_event.schema.json` | NEEDS VERIFICATION | Candidate restriction event shape. |
| `access_restriction.schema.json` | NEEDS VERIFICATION | Candidate access restriction shape; not legal routing authority by itself. |
| `domain_observation.schema.json` | NEEDS VERIFICATION | Candidate domain observation envelope. |
| `domain_validation_report.schema.json` | NEEDS VERIFICATION | Candidate validation-report shape; not proof or release authority. |
| `network_edge.schema.json` | NEEDS VERIFICATION | Candidate derived graph projection shape; not canonical route/segment truth. |
| `public_safe_route_summary.schema.json` | NEEDS VERIFICATION | Candidate release-facing derivative descriptor with evidence, policy, correction, and rollback references. |

## Schema-lane responsibilities

| Responsibility | Expectation |
|---|---|
| Domain schema index | List Roads/Rail/Trade schema files and child schema lanes as they are verified. |
| Contract pairing | Link each schema to paired semantic contracts under `contracts/domains/roads-rail-trade/` or another verified contract lane. |
| Slug-drift discipline | Keep `roads-rail-trade` vs `transport` and `domains/` vs flat schema-home drift visible until ADR/steward resolution confirms final homes. |
| Source-role discipline | Preserve differences among observed source records, administrative context, historic interpretations, modeled/candidate routes, derived graph projections, and released summaries. |
| Boundary preservation | Keep policy, fixtures, validators, pipelines, lifecycle data, source registry records, receipt instances, proofs, catalog records, and release records in their own responsibility roots. |
| Adjacent-domain discipline | Roads/Rail/Trade may reference Hydrology, Settlements/Infrastructure, Hazards, Archaeology, Agriculture, People/Land, and Map/UI context, but must not replace their owned truth. |
| Graph discipline | Derived network edges and graph projections must not replace canonical source-bound route, segment, membership, or facility records. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## What belongs here

- This README.
- Machine-checkable Roads/Rail/Trade JSON Schema files once placement is confirmed.
- Roads/Rail/Trade schema-family and child-lane README files.
- Schema index notes.
- Migration notes for Roads/Rail/Trade schema placement.
- Drift notes about duplicate or stale Roads/Rail/Trade vs `transport` schema paths.
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
- Live routing, emergency access instructions, road-closure advice, or legal road/rail status determinations.
- Canonical Hydrology, Settlements/Infrastructure, Hazards, Archaeology, Agriculture, People/Land, or Map/UI truth.
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
| `PATH_CONFLICT` | Schema placement is blocked by unresolved `roads-rail-trade` vs `transport` or `domains/` vs flat path drift. |
| `PROFILE` | Schema profiles a shared source, spatial, time, network, or common schema without creating duplicate authority. |
| `MIRROR` | Schema mirrors another accepted schema location. |
| `TRANSITIONAL` | Schema is awaiting migration to the accepted home. |
| `DEPRECATED` | Schema should no longer receive new consumers. |
| `NEEDS_VERIFICATION` | Pairing, fixture, validator, registry, review, or CI support has not been verified. |

## Minimal schema note

```markdown
# <roads-rail-trade-schema-note-id>

## Status
STUB / DRAFT_SCHEMA / ACTIVE_SCHEMA / PATH_CONFLICT / PROFILE / MIRROR / TRANSITIONAL / DEPRECATED / NEEDS_VERIFICATION

## Schema path
<schemas/contracts/v1/domains/roads-rail-trade/... or alternate path under review>

## Paired contract
<contracts/domains/roads-rail-trade/... or N/A>

## Source role
<observed / administrative / modeled / candidate / derived / released-summary / NEEDS VERIFICATION>

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
- [ ] Roads/Rail/Trade slug/path drift is resolved or explicitly marked PROPOSED / CONFLICTED.
- [ ] Schema registry entry is linked or marked NEEDS VERIFICATION.
- [ ] Valid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Invalid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Source-role and temporal-basis behavior is linked or marked NEEDS VERIFICATION where relevant.
- [ ] Validator path is linked or marked NEEDS VERIFICATION.
- [ ] CI/schema-test support is linked or marked NEEDS VERIFICATION.
- [ ] Pipeline, policy, data, registry, proof, receipt, catalog, and release records remain outside `schemas/`.
- [ ] Adjacent-domain boundaries are preserved.
- [ ] Graph projections remain derived and evidence-subordinate.
- [ ] Any migration or compatibility claim cites an ADR, migration note, or verified repo evidence.

## Naming guidance

Recommended schema filename pattern:

```text
<object_name>.schema.json
```

Examples:

```text
road_segment.schema.json
rail_segment.schema.json
corridor_route.schema.json
route_membership.schema.json
bridge.schema.json
river_crossing.schema.json
ferry.schema.json
depot.schema.json
siding.schema.json
yard.schema.json
transport_facility.schema.json
operator_assignment.schema.json
operator_status.schema.json
status_event.schema.json
restriction_event.schema.json
access_restriction.schema.json
domain_observation.schema.json
domain_validation_report.schema.json
network_edge.schema.json
public_safe_route_summary.schema.json
```

Use lowercase snake_case for schema filenames unless the schema registry or ADR specifies otherwise. Do not silently create duplicate schemas across `schemas/contracts/v1/domains/roads-rail-trade/`, older `schemas/contracts/v1/transport/` references, cross-domain lanes, or common schema paths.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/contracts/v1/domains/roads-rail-trade/`.
- [ ] Resolve the Roads/Rail/Trade schema-home and slug drift against older `transport` references.
- [ ] Confirm complete Roads/Rail/Trade schema inventory.
- [ ] Confirm whether concrete schema files exist under alternate casing or alternate paths.
- [ ] Confirm paired contract paths for all accepted schemas.
- [ ] Confirm schema registry records.
- [ ] Confirm valid fixture paths.
- [ ] Confirm invalid fixture paths.
- [ ] Confirm source-role and temporal-basis fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm policy, source-registry, release, correction, and rollback references for Roads/Rail/Trade schemas.
- [ ] Confirm whether `schemas/README.md` should index this Roads/Rail/Trade domain schema lane.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing greenfield scaffold |
| Next review trigger | Roads/Rail/Trade slug/schema-home resolution, new Roads/Rail/Trade schema, child-lane decision, schema-home migration, validator update, fixture update, schema registry update, ADR update, Roads/Rail/Trade contract update, policy/release reference update, or compatibility-lane decision |
