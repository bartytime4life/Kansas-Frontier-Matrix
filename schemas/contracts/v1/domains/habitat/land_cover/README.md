# `schemas/contracts/v1/domains/habitat/land_cover/` — Habitat Land Cover Schema Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-domains-habitat-land-cover-readme
title: schemas/contracts/v1/domains/habitat/land_cover/ — Habitat Land Cover Schema Index
version: v1
status: draft
policy_label: public
owners:
  - <schema-steward>
  - <habitat-domain-steward>
  - <land-cover-steward>
  - <contract-steward>
  - <validation-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, contracts, v1, domains, habitat, land-cover, LandCoverObservation, json-schema]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![domain](https://img.shields.io/badge/domain-habitat-green)
![sublane](https://img.shields.io/badge/sublane-land__cover-blue)
![posture](https://img.shields.io/badge/posture-schema--index-orange)
![canonical](https://img.shields.io/badge/canonical-PROPOSED-yellow)

## Purpose

`schemas/contracts/v1/domains/habitat/land_cover/` is the draft Habitat schema sublane for land-cover object shapes.

This path is for machine-checkable Habitat land-cover schema shapes, schema index notes, migration notes, and links to paired contracts, fixtures, validators, schema registry records, tests, policy references, source-registry references, release references, correction references, and rollback references.

This path is not a home for Habitat contract prose, policy rules, validator code, packages, pipelines, pipeline specs, lifecycle data, source registry records, emitted receipts, proof outputs, catalog records, release records, review records, or public map/API artifacts.

This README is documentation only. It is not itself a schema file, contract prose, policy, validator code, pipeline code, lifecycle data, source registry data, proof output, receipt instance, catalog record, or release authority.

## Status & authority

| Field | Value |
|---|---|
| Document type | Habitat land-cover schema README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/v1/domains/habitat/land_cover/` |
| Status | Draft |
| Authority level | Schema-index guidance. Schema files, paired contracts, registry records, validators, fixtures, tests, ADRs, parent Habitat schema decisions, and steward decisions outrank this README. |
| Path posture | Current-session evidence confirms this README was blank before this update. |
| Parent Habitat schema lane | `schemas/contracts/v1/domains/habitat/` exists as a PROPOSED greenfield scaffold. |
| Confirmed schema file | `observation.schema.json` exists as a PROPOSED scaffold. |
| Confirmed paired contract | `contracts/domains/habitat/land_cover/observation.md` exists for `LandCoverObservation`. |
| Field-level enforcement | NEEDS VERIFICATION. The confirmed schema scaffold has empty `properties` and `additionalProperties: true`. |
| Required reviewers | Schema steward, Habitat steward, land-cover steward, contract steward, validation steward, policy/release stewards where applicable, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the machine-checkable shape root and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says domain-specific schemas nest under `schemas/contracts/v1/domains/<domain>/...`, while `contracts/` retains object meaning and `schemas/` owns machine-checkable shape.

Current-session Directory Rules evidence confirms field-level shape belongs under `schemas/`, while lifecycle data, registries, proofs, receipts, and release materials are separate responsibility roots and parallel homes require ADR review.

Current-session evidence confirms `schemas/contracts/v1/domains/habitat/README.md` exists as a PROPOSED Habitat domain schema scaffold. That parent file still needs expansion and does not by itself prove this sublane is complete.

Current-session Habitat land-cover doctrine names `schemas/contracts/v1/domains/habitat/land_cover/` as the proposed machine schema home and identifies `LandCoverObservation` as a Habitat land-cover object family.

Current-session evidence confirms `contracts/domains/habitat/land_cover/observation.md` is the semantic contract for `LandCoverObservation` and points to `schemas/contracts/v1/domains/habitat/land_cover/observation.schema.json`.

Current-session evidence confirms `schemas/contracts/v1/domains/habitat/land_cover/observation.schema.json` exists as a PROPOSED scaffold with empty properties and permissive additional properties.

Current-session evidence confirms `pipelines/domains/habitat/land_cover/` is executable pipeline support only and does not own schemas, source descriptors, policy, lifecycle data, catalog truth, occurrence truth, or release decisions.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    └── v1/
        └── domains/
            └── habitat/
                ├── README.md
                └── land_cover/
                    ├── README.md
                    └── observation.schema.json

contracts/
└── domains/
    └── habitat/
        └── land_cover/
            ├── observation.md
            ├── class_scheme.md
            ├── crosswalk.md
            ├── change_summary.md
            └── uncertainty.md

docs/
└── domains/
    └── habitat/
        └── sublanes/
            └── land_cover.md

pipelines/
└── domains/
    └── habitat/
        └── land_cover/

data/
├── processed/habitat/land_cover/
└── receipts/habitat/land_cover/

policy/
fixtures/
release/
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/contracts/v1/domains/habitat/land_cover/README.md` | Blank before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms domain schemas nest under `schemas/contracts/v1/domains/<domain>/...`. |
| Directory Rules | Confirms machine shape belongs under `schemas/`; parallel homes require ADR review. |
| `schemas/contracts/v1/domains/habitat/README.md` | Existing parent Habitat schema scaffold; status PROPOSED. |
| Search for Habitat land-cover surfaces | Found contracts, pipeline, pipeline specs, processed data, receipt lanes, and docs. |
| `docs/domains/habitat/sublanes/land_cover.md` | Land-cover sublane doctrine; names this schema path and identifies `LandCoverObservation`. |
| `contracts/domains/habitat/land_cover/observation.md` | Semantic contract for `LandCoverObservation`; paired schema exists but is a scaffold. |
| `observation.schema.json` | Existing PROPOSED scaffold schema. |
| `pipelines/domains/habitat/land_cover/README.md` | Pipeline lane; executable logic only, not schema or release authority. |

This README does not verify complete land-cover schema fields, schema registry entries, fixture coverage, validator wiring, CI behavior, source-admission behavior, policy behavior, release integration, runtime behavior, public API behavior, or map rendering behavior.

## Current schema inventory

| Schema file | Paired contract | Status | Notes |
|---|---|---|---|
| `observation.schema.json` | `contracts/domains/habitat/land_cover/observation.md` | PROPOSED scaffold | Confirmed file exists, but field-level enforcement remains NEEDS VERIFICATION. |

## Candidate schema inventory

| Candidate schema | Status | Notes |
|---|---|---|
| `observation.schema.json` | PROPOSED scaffold | Current `LandCoverObservation` schema scaffold. |
| `class_scheme.schema.json` | NEEDS VERIFICATION | Candidate schema for land-cover class scheme profiles. |
| `crosswalk.schema.json` | NEEDS VERIFICATION | Candidate schema for crosswalks between land-cover class schemes. |
| `change_summary.schema.json` | NEEDS VERIFICATION | Candidate schema for land-cover change summaries. |
| `uncertainty.schema.json` | NEEDS VERIFICATION | Candidate schema for land-cover uncertainty surfaces or reports. |
| `public_derivative.schema.json` | NEEDS VERIFICATION | Candidate public-safe derivative descriptor with release and rollback refs. |

## Land-cover schema responsibilities

| Responsibility | Expectation |
|---|---|
| Schema index | Track Habitat land-cover schema files and candidates. |
| Contract pairing | Link each schema to paired semantic contracts under `contracts/domains/habitat/land_cover/`. |
| Boundary preservation | Keep policy, fixtures, validators, pipelines, pipeline specs, lifecycle data, source registry records, receipts, proofs, catalog records, and release records in their own responsibility roots. |
| Cross-lane discipline | Land-cover observations may inform Habitat workflows but do not become occurrence, regulatory, crop, soil, hydrology, hazard, land/title, or release truth. |
| Drift prevention | Prevent duplicate canonical schema definitions across parent Habitat, land-cover, cross-domain, and common schema paths. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## What belongs here

- This README.
- Machine-checkable Habitat land-cover JSON Schema files.
- Schema index notes.
- Schema migration notes.
- Drift notes about duplicate or stale land-cover schema paths.
- Links to paired contracts, fixtures, validators, schema registry records, source-registry records, policy references, release references, correction references, rollback references, and tests.

## What does not belong here

- Contract prose.
- Policy rules or sensitivity decisions.
- Validator implementation code.
- Runtime code.
- Pipeline implementation.
- Pipeline specs.
- SourceDescriptor instances or source registry records.
- Source payloads or lifecycle data.
- Emitted receipts.
- Proof outputs.
- Catalog records.
- Release records, release manifests, or release decisions.
- Public tiles, map/UI behavior, dashboards, screenshots, or generated summaries.
- Species occurrence truth, plant occurrence truth, critical-habitat designation truth, crop truth, soil truth, hydrology truth, hazards truth, land/title truth, or public release approval.
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

## Review checklist

- [ ] Schema has a stable `$id`.
- [ ] Schema has `$schema` set to JSON Schema draft 2020-12 unless an ADR says otherwise.
- [ ] Paired contract path is linked or marked NEEDS VERIFICATION.
- [ ] Schema registry entry is linked or marked NEEDS VERIFICATION.
- [ ] Valid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Invalid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Validator path is linked or marked NEEDS VERIFICATION.
- [ ] CI/schema-test support is linked or marked NEEDS VERIFICATION.
- [ ] Pipeline, data, registry, proof, receipt, catalog, and release records remain outside `schemas/`.
- [ ] Any migration or compatibility claim cites an ADR, migration note, or verified repo evidence.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/contracts/v1/domains/habitat/land_cover/`.
- [ ] Confirm complete Habitat land-cover schema inventory.
- [ ] Confirm whether additional land-cover schemas exist under alternate paths.
- [ ] Confirm paired contract paths for all accepted schemas.
- [ ] Confirm schema registry records.
- [ ] Confirm fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm policy, source-registry, release, correction, and rollback references for land-cover schemas.
- [ ] Confirm whether `schemas/contracts/v1/domains/habitat/README.md` should index this land-cover lane.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | New land-cover schema, schema-home decision, parent Habitat schema update, validator update, fixture update, schema registry update, ADR update, Habitat land-cover contract update, source-registry update, policy/release reference update, or compatibility-lane decision |
