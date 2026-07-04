# `schemas/contracts/v1/domains/geology/sublanes/` — Geology Schema Sublanes Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-domains-geology-sublanes-readme
title: schemas/contracts/v1/domains/geology/sublanes/ — Geology Schema Sublanes Index
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
tags: [kfm, schemas, contracts, v1, domains, geology, sublanes, schema-index, json-schema]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![domain](https://img.shields.io/badge/domain-geology-green)
![lane](https://img.shields.io/badge/lane-sublanes-blue)
![posture](https://img.shields.io/badge/posture-index--only-orange)
![canonical](https://img.shields.io/badge/canonical-NEEDS%20VERIFICATION-yellow)

## Purpose

`schemas/contracts/v1/domains/geology/sublanes/` is a draft index for proposed Geology schema sublanes.

This path may organize machine-checkable Geology schema shapes by sublane when a sublane has enough distinct schema work to justify a child index. It must remain subordinate to `schemas/contracts/v1/domains/geology/` and must not create a second Geology schema authority.

This README is documentation only. It is not a schema file, contract prose, policy, validator code, pipeline code, lifecycle data, source registry data, proof output, receipt instance, catalog record, or release authority.

## Status & authority

| Field | Value |
|---|---|
| Document type | Geology schema sublanes index README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/v1/domains/geology/sublanes/` |
| Status | Draft |
| Authority level | Index guidance. Schema files, paired contracts, schema registry records, validators, fixtures, tests, ADRs, parent Geology schema decisions, and steward decisions outrank this README. |
| Path posture | Current-session evidence confirms this README was blank before this update. |
| Parent schema lane | `schemas/contracts/v1/domains/geology/` exists as a PROPOSED greenfield scaffold. |
| Sublanes convention | NEEDS VERIFICATION. Current Geology docs say literal `sublanes/` placement is PROPOSED pending ADR/steward decision. |
| Confirmed child README | `surficial/README.md` exists as a draft Geology Surficial Sublane schema index. |
| Concrete schema inventory | NEEDS VERIFICATION. This edit did not confirm concrete schema files under `sublanes/`. |
| Default posture | Index-only until the `sublanes/` convention, paired contracts, fixtures, validators, registry records, and review status are confirmed. |
| Required reviewers | Schema steward, Geology steward, relevant sublane steward, contract steward, validation steward, policy/release stewards where applicable, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the machine-checkable shape root and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says domain-specific schemas nest under `schemas/contracts/v1/domains/<domain>/...`, while `contracts/` retains object meaning and `schemas/` owns machine-checkable shape.

Current-session Directory Rules evidence confirms field-level shape belongs under `schemas/`, while lifecycle data, registries, proofs, receipts, and release materials are separate responsibility roots and parallel homes require ADR review.

Current-session evidence confirms `schemas/contracts/v1/domains/geology/README.md` exists as a PROPOSED Geology domain schema scaffold. That parent file still needs expansion and does not by itself prove `sublanes/` is canonical.

Current-session search for this schema sublane family only confirmed the Geology surficial sublane documentation path. It did not confirm additional schema sublane READMEs or concrete sublane schema files.

Current-session evidence confirms `schemas/contracts/v1/domains/geology/sublanes/surficial/README.md` exists and marks the `sublanes/` convention as NEEDS VERIFICATION.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    └── v1/
        └── domains/
            └── geology/
                ├── README.md                 # parent Geology schema lane; PROPOSED scaffold
                └── sublanes/
                    ├── README.md             # you are here
                    └── surficial/
                        └── README.md         # confirmed child index

contracts/
└── domains/
    └── geology/                              # semantic meaning; not schema shape

docs/
└── domains/
    └── geology/                              # prose doctrine; not schema shape

pipelines/
└── domains/
    └── geology/                              # executable processing; not schema shape

data/                                        # lifecycle and registry roots; not schema home
release/                                     # release decisions and release records; not schema home
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/contracts/v1/domains/geology/sublanes/README.md` | Blank before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms domain schemas nest under `schemas/contracts/v1/domains/<domain>/...`. |
| Directory Rules | Confirms machine shape belongs under `schemas/`; parallel homes require ADR review. |
| `schemas/contracts/v1/domains/geology/README.md` | Existing parent Geology schema scaffold; status PROPOSED. |
| Search for Geology schema sublanes | Confirmed only the Geology surficial documentation path in this search. |
| `schemas/contracts/v1/domains/geology/sublanes/surficial/README.md` | Existing Surficial child index; status draft and sublane convention NEEDS VERIFICATION. |

This README does not verify complete sublane inventory, concrete schema files, schema registry entries, fixture coverage, validator wiring, CI behavior, policy behavior, release integration, runtime behavior, public API behavior, or map rendering behavior.

## Current child lanes

| Child path | Status | Responsibility |
|---|---|---|
| `surficial/` | Draft index / NEEDS VERIFICATION | Candidate schema sublane for surficial geology objects such as `SurficialUnit` and public-safe surficial map derivatives. |

## Candidate sublane inventory

Candidate sublanes below require steward review, paired contracts, fixtures, validators, registry records, and CI support before promotion.

| Candidate sublane | Status | Notes |
|---|---|---|
| `surficial/` | Draft child index exists | Literal sublane convention remains NEEDS VERIFICATION. |
| `bedrock/` | NEEDS VERIFICATION | Candidate schema sublane for bedrock geologic units and related context. |
| `stratigraphy/` | NEEDS VERIFICATION | Candidate schema sublane for stratigraphic intervals and correlation context. |
| `lithology/` | NEEDS VERIFICATION | Candidate schema sublane for lithology vocabulary/reference shapes if not handled at root/common. |
| `structures/` | NEEDS VERIFICATION | Candidate schema sublane for faults, folds, and structural context. |
| `boreholes/` | NEEDS VERIFICATION | Candidate schema sublane for borehole and well-log references. |
| `geophysics/` | NEEDS VERIFICATION | Candidate schema sublane for geophysical observations or derived context. |
| `geochemistry/` | NEEDS VERIFICATION | Candidate schema sublane for geochemical sample/observation context. |
| `resources/` | NEEDS VERIFICATION | Candidate schema sublane for resource/mineral context where safe and policy-reviewed. |
| `extraction-reclamation/` | NEEDS VERIFICATION | Candidate schema sublane for extraction/reclamation context if accepted. |
| `hydrostratigraphy/` | NEEDS VERIFICATION | Candidate context lane; must not replace Hydrology measurement truth. |

## Sublanes-index responsibilities

| Responsibility | Expectation |
|---|---|
| Child index | Track Geology schema sublane READMEs and their placement status. |
| Parent-domain discipline | Keep all sublanes subordinate to `schemas/contracts/v1/domains/geology/`. |
| Convention discipline | Keep `sublanes/` as PROPOSED / NEEDS VERIFICATION until an ADR or steward decision accepts it. |
| Contract pairing | Link child schemas to paired semantic contracts when verified. |
| Boundary preservation | Keep policy, fixtures, validators, pipelines, lifecycle data, source registry records, proofs, receipts, catalog records, and release records in their own roots. |
| Drift prevention | Prevent duplicate canonical schema definitions across parent Geology, child sublanes, cross-domain lanes, and common schema families. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## What belongs here

- This README.
- Child README links for accepted or candidate Geology schema sublanes.
- Short index notes about sublane schema placement.
- Migration notes for Geology sublane schema placement.
- Drift notes about duplicate or stale Geology sublane schema paths.
- Links to paired contracts, fixtures, validators, schema registry records, policy references, source-registry references, release references, correction references, rollback references, and tests.

## What does not belong here

- Concrete schema files that belong in a confirmed child lane or directly under the parent Geology schema lane.
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
- Soil, Hydrology, Hazards, Archaeology, land/title, or other adjacent-domain truth.
- Generic reusable schemas that belong under `schemas/contracts/v1/common/`.
- Claims that a schema sublane is canonical without ADR, registry, migration note, or steward confirmation.

## Sublane status values

Use finite status values where possible:

| Status | Meaning |
|---|---|
| `INDEX_ONLY` | Parent file only indexes child sublane candidates. |
| `SUBLANE_CANDIDATE` | Child path may become an accepted schema sublane. |
| `ACTIVE_SUBLANE` | Child path has accepted placement, paired contracts, fixtures, validators, registry records, and review status. |
| `MIGRATE_TO_GEOLOGY_ROOT` | Content belongs directly under `schemas/contracts/v1/domains/geology/`. |
| `MIGRATE_TO_CROSS` | Content belongs under a cross-domain schema lane. |
| `MIGRATE_TO_COMMON` | Content belongs under a common reusable schema family. |
| `DEPRECATED` | Child path should no longer receive new consumers. |
| `NEEDS_VERIFICATION` | Placement, pairing, fixture, validator, registry, or CI support has not been verified. |

## Review checklist

- [ ] Parent Geology schema README is updated to reference this sublanes index.
- [ ] `sublanes/` placement is accepted by ADR/steward decision or marked NEEDS VERIFICATION.
- [ ] Each child sublane has a README before accepting concrete schema files.
- [ ] Each child schema has a paired contract path or NEEDS VERIFICATION note.
- [ ] Schema registry entries are linked or marked NEEDS VERIFICATION.
- [ ] Fixture paths are linked or marked NEEDS VERIFICATION.
- [ ] Validator paths are linked or marked NEEDS VERIFICATION.
- [ ] CI/schema-test support is linked or marked NEEDS VERIFICATION.
- [ ] Pipeline, data, registry, proof, receipt, catalog, and release records remain outside `schemas/`.
- [ ] Adjacent-domain boundaries are preserved.
- [ ] Any migration or compatibility claim cites an ADR, migration note, or verified repo evidence.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/contracts/v1/domains/geology/sublanes/`.
- [ ] Confirm whether the `sublanes/` segment is accepted for schema paths or should remain a proposed convention.
- [ ] Confirm complete Geology schema sublane inventory.
- [ ] Confirm whether sublane schemas should instead live directly under `schemas/contracts/v1/domains/geology/`.
- [ ] Confirm whether any sublane schemas belong under `schemas/contracts/v1/cross/` or `schemas/contracts/v1/common/`.
- [ ] Confirm paired Geology contract paths for each accepted sublane.
- [ ] Confirm schema registry records.
- [ ] Confirm fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm policy, source-registry, release, correction, and rollback references for sublane schemas.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | Sublane placement decision, new child sublane, new Geology schema, schema-home migration, validator update, fixture update, schema registry update, ADR update, Geology contract update, policy/release reference update, or compatibility-lane decision |
