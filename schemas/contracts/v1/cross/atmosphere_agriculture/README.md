# `schemas/contracts/v1/cross/atmosphere_agriculture/` — Atmosphere × Agriculture Cross-Schema Compatibility Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-cross-atmosphere-agriculture-readme
title: schemas/contracts/v1/cross/atmosphere_agriculture/ — Atmosphere × Agriculture Cross-Schema Compatibility Index
version: v1
status: draft
policy_label: public
owners:
  - <schema-steward>
  - <atmosphere-domain-steward>
  - <agriculture-domain-steward>
  - <contract-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, contracts, v1, cross-domain, atmosphere, agriculture, compatibility, json-schema]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![lane](https://img.shields.io/badge/lane-cross--domain-blueviolet)
![domains](https://img.shields.io/badge/domains-atmosphere%20%C3%97%20agriculture-green)
![posture](https://img.shields.io/badge/posture-compatibility--index-orange)
![canonical](https://img.shields.io/badge/canonical-NEEDS%20VERIFICATION-yellow)

## Purpose

`schemas/contracts/v1/cross/atmosphere_agriculture/` is a draft compatibility and index lane for schema notes that join Atmosphere and Agriculture concepts.

Use this README to prevent cross-domain products from becoming a parallel authority over the owning Atmosphere and Agriculture schema lanes. Cross-domain schemas should describe composed or derived shapes only when the owning domain facts, evidence, policy posture, and release state remain traceable to their source lanes.

This README is documentation only. It is not a schema file, contract prose, policy, validator code, runtime code, lifecycle data, or release authority.

## Status & authority

| Field | Value |
|---|---|
| Document type | Atmosphere × Agriculture cross-schema compatibility README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/v1/cross/atmosphere_agriculture/` |
| Status | Draft |
| Authority level | Compatibility/index guidance. Canonical schemas, paired contracts, schema registry records, validators, fixtures, tests, ADRs, domain stewards, and release records outrank this README. |
| Path posture | Current-session evidence confirms this README was blank before this update. |
| Canonical status | NEEDS VERIFICATION. This path is not confirmed as a canonical schema family in this session. |
| Atmosphere schema lane | `schemas/contracts/v1/domains/atmosphere/` exists as a PROPOSED domain schema lane. |
| Agriculture schema lane | NEEDS VERIFICATION. Current-session evidence confirms `schemas/contracts/v1/agriculture/` as a compatibility lane and did not confirm `schemas/contracts/v1/domains/agriculture/README.md`. |
| Default posture | Do not create canonical cross-domain schemas here until a steward decision, ADR, registry entry, or migration note confirms this cross-family home. |
| Required reviewers | Schema steward, Atmosphere steward, Agriculture steward, contract steward, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the root for machine-checkable shape and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says the default schema home is `schemas/contracts/v1/<family>/...`, and domain-specific schemas nest under `schemas/contracts/v1/domains/<domain>/...`.

Current-session evidence confirms the Atmosphere domain schema lane exists at `schemas/contracts/v1/domains/atmosphere/` and is marked PROPOSED.

Current-session evidence confirms Agriculture is currently represented by a shorter compatibility README at `schemas/contracts/v1/agriculture/`, with canonical domain placement still NEEDS VERIFICATION.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    └── v1/
        ├── cross/
        │   └── atmosphere_agriculture/     # you are here; cross-domain compatibility/index lane
        ├── domains/
        │   ├── atmosphere/                 # confirmed PROPOSED Atmosphere domain schema lane
        │   └── agriculture/                # likely Agriculture domain lane; NEEDS VERIFICATION
        ├── atmosphere/                     # shorter Atmosphere compatibility lane
        └── agriculture/                    # shorter Agriculture compatibility lane

contracts/
└── domains/
    ├── atmosphere/
    └── agriculture/
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/contracts/v1/cross/atmosphere_agriculture/README.md` | Blank before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms `schemas/contracts/v1/` as the proposed canonical schema home and says domain schemas nest under `schemas/contracts/v1/domains/<domain>/...`. |
| `schemas/contracts/v1/domains/atmosphere/README.md` | Existing Atmosphere domain schema lane; status PROPOSED. |
| `schemas/contracts/v1/agriculture/README.md` | Existing Agriculture compatibility lane; canonical domain lane remains NEEDS VERIFICATION. |
| Agriculture search | Found Agriculture contract, package, fixture, policy, pipeline, app, and related surfaces; did not confirm a `schemas/contracts/v1/domains/agriculture/README.md` path in this edit. |

This README does not verify schema contents, schema registry entries, fixture coverage, validator wiring, CI behavior, cross-domain policy behavior, release integration, or whether this cross path should remain as a compatibility lane.

## Cross-lane responsibilities

| Responsibility | Expectation |
|---|---|
| Canonical-home decision | Determine whether this cross-domain schema lane should exist, remain index-only, or migrate elsewhere. |
| Domain ownership | Keep Atmosphere-owned facts with Atmosphere schemas and Agriculture-owned facts with Agriculture schemas. |
| Cross-domain composition | Document only the shape of composed products when both owning domain records remain traceable. |
| Drift prevention | Prevent duplicated Atmosphere or Agriculture canonical schemas under this cross path. |
| Contract linkage | Point to paired cross-domain or owning-domain contract files when verified. |
| Fixture linkage | Point to valid, invalid, and edge-case fixtures when verified. |
| Validator linkage | Point to validators or CI checks when verified. |
| Registry linkage | Point to schema registry records when verified. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## What belongs here

- This compatibility README.
- Short index notes that point to accepted Atmosphere, Agriculture, or cross-domain schema files once confirmed.
- Migration notes for any cross-domain schema files that need to move.
- Drift notes about duplicate or stale Atmosphere × Agriculture schema paths.
- Links to canonical schemas, paired contracts, fixtures, validators, registry records, policy references, release references, and tests.
- Notes describing cross-domain schema composition without replacing owning domain truth.

## What does not belong here

- New canonical Atmosphere schemas.
- New canonical Agriculture schemas.
- Duplicate copies of schemas owned by Atmosphere or Agriculture lanes.
- Contract prose.
- Policy rules.
- Validator implementation code.
- Runtime code.
- Lifecycle data payloads.
- EvidenceBundle contents or source records.
- Release records.
- Claims that this cross path is canonical without ADR, registry, migration note, or steward confirmation.

## Compatibility status values

Use finite compatibility status values where possible:

| Status | Meaning |
|---|---|
| `INDEX_ONLY` | This path only points to candidate canonical schema homes. |
| `CROSS_FAMILY_CANDIDATE` | This path may become an accepted cross-domain schema family. |
| `ALIAS_CANDIDATE` | This path may remain a documented alias to owning domain schema lanes. |
| `TRANSITIONAL` | Content is awaiting migration to the accepted schema home. |
| `DEPRECATED` | Content should no longer receive new files. |
| `MIGRATE_TO_ATMOSPHERE` | Content belongs under the Atmosphere schema lane. |
| `MIGRATE_TO_AGRICULTURE` | Content belongs under the Agriculture schema lane. |
| `NEEDS_VERIFICATION` | Pairing, fixture, validator, registry, or CI support has not been verified. |

## Minimal compatibility note

```markdown
# <atmosphere-agriculture-schema-compatibility-note-id>

## Status
INDEX_ONLY / CROSS_FAMILY_CANDIDATE / ALIAS_CANDIDATE / TRANSITIONAL / DEPRECATED / MIGRATE_TO_ATMOSPHERE / MIGRATE_TO_AGRICULTURE / NEEDS_VERIFICATION

## Compatibility path
<schemas/contracts/v1/cross/atmosphere_agriculture/... or N/A>

## Proposed canonical path
<schemas/contracts/v1/domains/atmosphere/... / schemas/contracts/v1/domains/agriculture/... / schemas/contracts/v1/cross/atmosphere_agriculture/... / NEEDS VERIFICATION>

## Paired contract
<contract path or N/A>

## Owning domain facts
<atmosphere / agriculture / both / NEEDS VERIFICATION>

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

- [ ] Canonical schema path is linked or marked NEEDS VERIFICATION.
- [ ] Owning domain facts are identified.
- [ ] Atmosphere schema references are linked or marked NEEDS VERIFICATION.
- [ ] Agriculture schema references are linked or marked NEEDS VERIFICATION.
- [ ] Paired contract path is linked or marked NEEDS VERIFICATION.
- [ ] Schema registry entry is linked or marked NEEDS VERIFICATION.
- [ ] Valid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Invalid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Validator path is linked or marked NEEDS VERIFICATION.
- [ ] CI/schema-test support is linked or marked NEEDS VERIFICATION.
- [ ] Cross-domain policy or release references are linked or marked NEEDS VERIFICATION.
- [ ] No duplicate canonical domain schemas are placed under this path.
- [ ] Any migration or compatibility claim cites an ADR, migration note, or verified repo evidence.

## Naming guidance

Recommended compatibility-note pattern:

```text
<YYYY-MM-DD>_<schema-shortname>_atmosphere-agriculture-cross-note.md
```

Examples:

```text
2026-07-03_crop-weather-risk_cross-note.md
2026-07-03_agriculture-air-quality_cross-note.md
2026-07-03_atmosphere-agriculture-path-decision_cross-note.md
```

Use lowercase filenames and hyphenated schema short names.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/contracts/v1/cross/atmosphere_agriculture/`.
- [ ] Confirm whether cross-domain schema families are permitted under `schemas/contracts/v1/cross/`.
- [ ] Confirm whether this path should remain index-only.
- [ ] Confirm canonical Agriculture schema home.
- [ ] Confirm paired Atmosphere and Agriculture contract paths.
- [ ] Confirm cross-domain contract path, if any.
- [ ] Confirm schema registry records.
- [ ] Confirm valid fixture paths.
- [ ] Confirm invalid fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm whether `schemas/README.md` should index this cross-domain compatibility lane.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | Cross-domain schema-home decision, new Atmosphere × Agriculture schema, Agriculture canonical-home decision, schema migration, validator update, fixture update, registry update, ADR update, or compatibility-lane decision |
