# `schemas/contracts/v1/domains/atmosphere/registry/` — Atmosphere Registry Schema Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-domains-atmosphere-registry-readme
title: schemas/contracts/v1/domains/atmosphere/registry/ — Atmosphere Registry Schema Index
version: v1
status: draft
policy_label: public
owners:
  - <schema-steward>
  - <atmosphere-domain-steward>
  - <registry-steward>
  - <source-steward>
  - <contract-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, contracts, v1, domains, atmosphere, registry, sources, source-descriptor, json-schema]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![domain](https://img.shields.io/badge/domain-atmosphere-green)
![family](https://img.shields.io/badge/family-registry-blueviolet)
![posture](https://img.shields.io/badge/posture-schema--index-orange)
![canonical](https://img.shields.io/badge/canonical-NEEDS%20VERIFICATION-yellow)

## Purpose

`schemas/contracts/v1/domains/atmosphere/registry/` is a draft Atmosphere schema sublane for registry-shaped Atmosphere objects.

This path should index machine-checkable schema shapes for Atmosphere registry objects, especially source-descriptor or admission-control record shapes when those shapes are confirmed as Atmosphere-owned. It must not store actual registry records, source descriptors, source payloads, policy decisions, proofs, receipts, catalog records, release manifests, release decisions, or public artifacts.

This README is documentation only. It is not a schema file, contract prose, policy, validator code, lifecycle data, registry data, source-descriptor instance, proof output, receipt instance, or release authority.

## Status & authority

| Field | Value |
|---|---|
| Document type | Atmosphere registry schema README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/v1/domains/atmosphere/registry/` |
| Status | Draft |
| Authority level | Schema-index guidance. Schema files, paired contracts, registry records, validators, fixtures, tests, ADRs, source/registry rules, and steward decisions outrank this README. |
| Path posture | Current-session evidence confirms this README was blank before this update. |
| Atmosphere schema lane | `schemas/contracts/v1/domains/atmosphere/` exists as a PROPOSED domain schema lane. |
| Registry schema inventory | NEEDS VERIFICATION. This edit did not confirm concrete registry schemas under this path. |
| Related registry instance lanes | `data/registry/sources/atmosphere/` and `data/registry/atmosphere/sources/` exist as registry/source-descriptor lanes. |
| Registry boundary | Schema shape belongs under `schemas/`; actual registry records belong under governed `data/registry/` lanes. |
| Default posture | Do not add canonical registry schemas here until paired contracts, fixtures, validators, registry records, and steward review are confirmed. |
| Required reviewers | Schema steward, Atmosphere steward, registry steward, source steward, contract steward, validation steward where applicable, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the root for machine-checkable shape and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says domain-specific schemas nest under `schemas/contracts/v1/domains/<domain>/...`, while `contracts/` retains object meaning and `schemas/` owns machine-checkable shape.

Current-session evidence confirms `schemas/contracts/v1/domains/atmosphere/README.md` exists as a PROPOSED Atmosphere domain schema lane.

Current-session search found Atmosphere registry/source-descriptor instance lanes under `data/registry/sources/atmosphere/` and `data/registry/atmosphere/sources/`, plus Atmosphere source-registry documentation. That does not by itself confirm registry schemas under this path.

Current-session evidence from `docs/domains/atmosphere/SOURCE_REGISTRY.md` says the human-facing source-registry surface pairs with a companion machine-readable register under `data/registry/sources/atmosphere/`, while schema-home placement remains under the schema rules.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    └── v1/
        └── domains/
            └── atmosphere/
                ├── README.md
                ├── atmosphere_air_decision_envelope.schema.json
                └── registry/
                    └── README.md                        # you are here

contracts/
└── domains/
    └── atmosphere/                                       # semantic contracts; not schema shape

data/
└── registry/
    ├── sources/
    │   └── atmosphere/                                  # source registry records / admission control
    └── atmosphere/
        └── sources/                                     # alternate lane-order pattern; NEEDS VERIFICATION

docs/
└── domains/
    └── atmosphere/
        └── SOURCE_REGISTRY.md                           # human-facing source-admission doctrine
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/contracts/v1/domains/atmosphere/registry/README.md` | Blank before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms domain schemas nest under `schemas/contracts/v1/domains/<domain>/...`. |
| `schemas/contracts/v1/domains/atmosphere/README.md` | Existing Atmosphere domain schema lane; status PROPOSED. |
| Search for Atmosphere registry surfaces | Found Atmosphere registry/source-descriptor lanes and Atmosphere source-registry docs; did not confirm concrete registry schemas under this path. |
| `data/registry/sources/atmosphere/README.md` | Canonical-looking source-registry domain lane; records registry/source-descriptor routing and admission-control boundaries. |
| `data/registry/atmosphere/sources/README.md` | Alternate lane-order source registry path; marks lane-order conflict as NEEDS VERIFICATION. |
| `docs/domains/atmosphere/SOURCE_REGISTRY.md` | Human-facing Atmosphere source-admission surface; points to `data/registry/sources/atmosphere/` as companion register. |

This README does not verify complete registry schema fields, schema registry entries, fixture coverage, validator wiring, CI behavior, source-activation behavior, policy behavior, release integration, or actual registry record layout.

## Candidate registry-shape families

Candidate Atmosphere registry schemas should be introduced only after contract, fixture, validator, registry, and steward support is clear.

| Candidate family | Status | Notes |
|---|---|---|
| Atmosphere source descriptor | NEEDS VERIFICATION | Could describe Atmosphere-specific source descriptor shape if not fully covered by shared source schemas. |
| Atmosphere source activation decision | NEEDS VERIFICATION | Could describe activation/admission routing shape if accepted. |
| Atmosphere source-role boundary record | NEEDS VERIFICATION | Could describe source-role anti-collapse checks for Atmosphere records. |
| Atmosphere source freshness profile | NEEDS VERIFICATION | Could describe update cadence, stale-state, and time-basis shape if accepted. |
| Atmosphere registry migration note | NEEDS VERIFICATION | Could document lane-order resolution between `data/registry/sources/atmosphere/` and `data/registry/atmosphere/sources/`. |

## Registry-lane responsibilities

| Responsibility | Expectation |
|---|---|
| Schema index | Track Atmosphere registry schema files and their placement status. |
| Contract pairing | Link each registry schema to an Atmosphere or shared source semantic contract when verified. |
| Instance separation | Keep actual registry/source-descriptor records outside `schemas/`. |
| Shared-source discipline | Do not duplicate shared `source/` schema families unless an Atmosphere-specific extension is approved. |
| Drift prevention | Prevent duplicate registry schemas under conflicting Atmosphere, source, or data-registry paths. |
| Fixture linkage | Point to valid and invalid fixtures when verified. |
| Validator linkage | Point to validators or CI checks when verified. |
| Registry linkage | Point to schema registry records when verified. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## What belongs here

- This README.
- Atmosphere-owned registry schema files once placement is confirmed.
- Short schema-family index notes.
- Migration notes for registry schema placement.
- Drift notes about duplicate or stale Atmosphere registry schema paths.
- Links to paired contracts, shared source schemas, fixtures, validators, schema registry records, policy references, release references, and tests.
- Notes that preserve the distinction between schema shape and registry records.

## What does not belong here

- Actual registry records.
- SourceDescriptor instances.
- Source payloads.
- Receipt records.
- Proof records.
- Catalog records.
- Release manifests or release decisions.
- Contract prose.
- Policy rules.
- Validator implementation code.
- Runtime code.
- Lifecycle data payloads.
- Public API or map/UI behavior.
- Claims that a registry schema is complete without fixtures, validators, registry records, and review support.

## Registry schema status values

Use finite status values where possible:

| Status | Meaning |
|---|---|
| `INDEX_ONLY` | This path only indexes candidate registry schema locations. |
| `REGISTRY_SCHEMA_CANDIDATE` | The schema may become an accepted Atmosphere registry schema. |
| `DRAFT_SCHEMA` | Schema exists but still needs review and test support. |
| `ACTIVE_SCHEMA` | Schema has accepted contract pairing, fixtures, validator support, registry record, and review status. |
| `MIGRATE_TO_ATMOSPHERE_ROOT` | Content belongs directly under `schemas/contracts/v1/domains/atmosphere/`. |
| `MIGRATE_TO_SOURCE` | Content belongs under a shared source schema family. |
| `MIGRATE_TO_REGISTRY` | Content belongs under this registry sublane. |
| `DEPRECATED` | Content should no longer receive new consumers. |
| `NEEDS_VERIFICATION` | Pairing, fixture, validator, registry, or CI support has not been verified. |

## Minimal registry schema note

```markdown
# <atmosphere-registry-schema-note-id>

## Status
INDEX_ONLY / REGISTRY_SCHEMA_CANDIDATE / DRAFT_SCHEMA / ACTIVE_SCHEMA / MIGRATE_TO_ATMOSPHERE_ROOT / MIGRATE_TO_SOURCE / MIGRATE_TO_REGISTRY / DEPRECATED / NEEDS_VERIFICATION

## Schema path
<schemas/contracts/v1/domains/atmosphere/registry/... or current schema path>

## Paired contract
<contract path or N/A>

## Registry instance lane
<data registry path or NEEDS VERIFICATION>

## Fixtures
<fixtures path or N/A>

## Validator
<tools/validators path or N/A>

## Notes
<short note grounded in repo evidence>

## Follow-up
<open items or none>
```

## Review checklist

- [ ] Canonical registry schema path is linked or marked NEEDS VERIFICATION.
- [ ] Paired contract path is linked or marked NEEDS VERIFICATION.
- [ ] Registry instance lane is linked or marked NEEDS VERIFICATION.
- [ ] Shared source-schema relationship is linked or marked NEEDS VERIFICATION.
- [ ] Schema registry entry is linked or marked NEEDS VERIFICATION.
- [ ] Valid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Invalid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Validator path is linked or marked NEEDS VERIFICATION.
- [ ] CI/schema-test support is linked or marked NEEDS VERIFICATION.
- [ ] Schema/registry/source-record boundaries are preserved.
- [ ] Any migration or compatibility claim cites an ADR, migration note, or verified repo evidence.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/contracts/v1/domains/atmosphere/registry/`.
- [ ] Confirm whether Atmosphere registry schemas belong in this sublane, the Atmosphere schema root, or a shared source schema family.
- [ ] Confirm paired Atmosphere or shared source contract paths.
- [ ] Resolve registry lane-order relation between `data/registry/sources/atmosphere/` and `data/registry/atmosphere/sources/`.
- [ ] Confirm registry instance lanes for Atmosphere records.
- [ ] Confirm schema registry records.
- [ ] Confirm valid fixture paths.
- [ ] Confirm invalid fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm whether `schemas/contracts/v1/domains/atmosphere/README.md` should index this registry lane.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | Registry schema-home decision, new Atmosphere registry schema, source-schema alignment, registry lane-order decision, migration note, validator update, fixture update, schema registry update, ADR update, Atmosphere registry contract update, or compatibility-lane decision |
