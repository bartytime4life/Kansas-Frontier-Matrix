# `schemas/contracts/v1/cross/atmosphere_biodiversity/` — Atmosphere × Biodiversity Cross-Schema Compatibility Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-cross-atmosphere-biodiversity-readme
title: schemas/contracts/v1/cross/atmosphere_biodiversity/ — Atmosphere × Biodiversity Cross-Schema Compatibility Index
version: v1
status: draft
policy_label: public
owners:
  - <schema-steward>
  - <atmosphere-domain-steward>
  - <biodiversity-steward>
  - <flora-steward>
  - <fauna-steward>
  - <habitat-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, contracts, v1, cross-domain, atmosphere, biodiversity, ecology, compatibility, geoprivacy, json-schema]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![lane](https://img.shields.io/badge/lane-cross--domain-blueviolet)
![domains](https://img.shields.io/badge/domains-atmosphere%20%C3%97%20biodiversity-green)
![posture](https://img.shields.io/badge/posture-compatibility--index-orange)
![canonical](https://img.shields.io/badge/canonical-NEEDS%20VERIFICATION-yellow)
![sensitivity](https://img.shields.io/badge/sensitivity-geoprivacy--required-red)

## Purpose

`schemas/contracts/v1/cross/atmosphere_biodiversity/` is a draft compatibility and index lane for schema notes that join Atmosphere and Biodiversity concepts.

Use this README to prevent cross-domain products from becoming a parallel authority over the owning Atmosphere and ecology-related schema lanes. Cross-domain schemas should describe composed or derived shapes only when the owning domain facts, evidence, policy posture, sensitivity posture, and release state remain traceable to their source lanes.

This README is documentation only. It is not a schema file, contract prose, policy, validator code, runtime code, lifecycle data, or release authority.

## Status & authority

| Field | Value |
|---|---|
| Document type | Atmosphere × Biodiversity cross-schema compatibility README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/v1/cross/atmosphere_biodiversity/` |
| Status | Draft |
| Authority level | Compatibility/index guidance. Canonical schemas, paired contracts, schema registry records, validators, fixtures, tests, ADRs, domain stewards, sensitivity review, and release records outrank this README. |
| Path posture | Current-session evidence confirms this README was blank before this update. |
| Canonical status | NEEDS VERIFICATION. This path is not confirmed as a canonical schema family in this session. |
| Atmosphere schema lane | `schemas/contracts/v1/domains/atmosphere/` exists as a PROPOSED domain schema lane. |
| Biodiversity schema lane | NEEDS VERIFICATION. Current-session evidence confirms `schemas/contracts/v1/biodiversity/` as a compatibility lane and says biodiversity remains cross-domain rather than a confirmed sovereign schema family. |
| Default posture | Do not create canonical cross-domain schemas here until a steward decision, ADR, registry entry, or migration note confirms this cross-family home. |
| Sensitivity posture | Geoprivacy and sensitivity review are required where biodiversity joins involve rare species, sensitive occurrence records, habitat joins, or protected locations. |
| Required reviewers | Schema steward, Atmosphere steward, biodiversity steward, relevant Flora/Fauna/Habitat steward, sensitivity steward when applicable, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the root for machine-checkable shape and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says the default schema home is `schemas/contracts/v1/<family>/...`, and domain-specific schemas nest under `schemas/contracts/v1/domains/<domain>/...`.

Current-session evidence confirms the Atmosphere domain schema lane exists at `schemas/contracts/v1/domains/atmosphere/` and is marked PROPOSED.

Current-session evidence confirms Biodiversity is currently represented by a compatibility README at `schemas/contracts/v1/biodiversity/`, where canonical schema placement remains NEEDS VERIFICATION and atomic biodiversity facts are expected to remain with owning lanes such as Flora, Fauna, and Habitat.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    └── v1/
        ├── cross/
        │   └── atmosphere_biodiversity/    # you are here; cross-domain compatibility/index lane
        ├── domains/
        │   ├── atmosphere/                 # confirmed PROPOSED Atmosphere domain schema lane
        │   ├── flora/                      # possible biodiversity-owning domain lane; NEEDS VERIFICATION
        │   ├── fauna/                      # possible biodiversity-owning domain lane; NEEDS VERIFICATION
        │   └── habitat/                    # possible biodiversity-owning domain lane; NEEDS VERIFICATION
        ├── atmosphere/                     # shorter Atmosphere compatibility lane
        └── biodiversity/                   # Biodiversity compatibility lane

contracts/
└── biodiversity/                           # observed compatibility/cross-domain contract lane
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/contracts/v1/cross/atmosphere_biodiversity/README.md` | Blank before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms `schemas/contracts/v1/` as the proposed canonical schema home and says domain schemas nest under `schemas/contracts/v1/domains/<domain>/...`. |
| `schemas/contracts/v1/domains/atmosphere/README.md` | Existing Atmosphere domain schema lane; status PROPOSED. |
| `schemas/contracts/v1/biodiversity/README.md` | Existing Biodiversity compatibility lane; canonical schema family remains NEEDS VERIFICATION. |
| Biodiversity posture | Current-session evidence says biodiversity is cross-domain composition, not a confirmed sovereign domain/schema root. |

This README does not verify schema contents, schema registry entries, fixture coverage, validator wiring, CI behavior, cross-domain policy behavior, sensitivity behavior, release integration, or whether this cross path should remain as a compatibility lane.

## Cross-lane responsibilities

| Responsibility | Expectation |
|---|---|
| Canonical-home decision | Determine whether this cross-domain schema lane should exist, remain index-only, or migrate elsewhere. |
| Domain ownership | Keep Atmosphere-owned facts with Atmosphere schemas and biodiversity-owned atomic facts with Flora, Fauna, Habitat, or other accepted owning lanes. |
| Cross-domain composition | Document only the shape of composed products when all owning domain records remain traceable. |
| Drift prevention | Prevent duplicated Atmosphere or ecology-domain canonical schemas under this cross path. |
| Sensitivity linkage | Preserve geoprivacy and sensitivity review for rare species, sensitive occurrence, or protected-location joins. |
| Contract linkage | Point to paired cross-domain or owning-domain contract files when verified. |
| Fixture linkage | Point to valid, invalid, public-safe, and edge-case fixtures when verified. |
| Validator linkage | Point to validators or CI checks when verified. |
| Registry linkage | Point to schema registry records when verified. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## What belongs here

- This compatibility README.
- Short index notes that point to accepted Atmosphere, Biodiversity, Flora, Fauna, Habitat, or cross-domain schema files once confirmed.
- Migration notes for any cross-domain schema files that need to move.
- Drift notes about duplicate or stale Atmosphere × Biodiversity schema paths.
- Links to canonical schemas, paired contracts, fixtures, validators, registry records, policy references, release references, and tests.
- Notes describing cross-domain schema composition without replacing owning domain truth.
- Public-safe notes that avoid exposing sensitive occurrence or protected-location details.

## What does not belong here

- New canonical Atmosphere schemas.
- New canonical Biodiversity schemas.
- Duplicate copies of schemas owned by Atmosphere, Flora, Fauna, Habitat, or other owning lanes.
- Contract prose.
- Policy rules.
- Validator implementation code.
- Runtime code.
- Lifecycle data payloads.
- EvidenceBundle contents or source records.
- Release records.
- Rare-species exact locations or protected ecological details.
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
| `MIGRATE_TO_BIODIVERSITY_OWNER` | Content belongs under the accepted biodiversity-owning lane such as Flora, Fauna, or Habitat. |
| `HELD_FOR_REVIEW` | Content requires schema, domain, sensitivity, or policy review before use. |
| `NEEDS_VERIFICATION` | Pairing, fixture, validator, registry, sensitivity, or CI support has not been verified. |

## Minimal compatibility note

```markdown
# <atmosphere-biodiversity-schema-compatibility-note-id>

## Status
INDEX_ONLY / CROSS_FAMILY_CANDIDATE / ALIAS_CANDIDATE / TRANSITIONAL / DEPRECATED / MIGRATE_TO_ATMOSPHERE / MIGRATE_TO_BIODIVERSITY_OWNER / HELD_FOR_REVIEW / NEEDS_VERIFICATION

## Compatibility path
<schemas/contracts/v1/cross/atmosphere_biodiversity/... or N/A>

## Proposed canonical path
<schemas/contracts/v1/domains/atmosphere/... / schemas/contracts/v1/domains/flora/... / schemas/contracts/v1/domains/fauna/... / schemas/contracts/v1/domains/habitat/... / schemas/contracts/v1/cross/atmosphere_biodiversity/... / NEEDS VERIFICATION>

## Paired contract
<contract path or N/A>

## Owning domain facts
<atmosphere / flora / fauna / habitat / biodiversity composition / NEEDS VERIFICATION>

## Sensitivity posture
<public-safe / generalized / held / denied / NEEDS VERIFICATION>

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
- [ ] Biodiversity owner-lane schema references are linked or marked NEEDS VERIFICATION.
- [ ] Paired contract path is linked or marked NEEDS VERIFICATION.
- [ ] Sensitivity posture is explicit.
- [ ] Schema registry entry is linked or marked NEEDS VERIFICATION.
- [ ] Valid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Invalid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Public-safe fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Validator path is linked or marked NEEDS VERIFICATION.
- [ ] CI/schema-test support is linked or marked NEEDS VERIFICATION.
- [ ] Cross-domain policy or release references are linked or marked NEEDS VERIFICATION.
- [ ] No duplicate canonical domain schemas are placed under this path.
- [ ] No sensitive occurrence or protected-location details are stored here.
- [ ] Any migration or compatibility claim cites an ADR, migration note, or verified repo evidence.

## Naming guidance

Recommended compatibility-note pattern:

```text
<YYYY-MM-DD>_<schema-shortname>_atmosphere-biodiversity-cross-note.md
```

Examples:

```text
2026-07-03_climate-biodiversity-risk_cross-note.md
2026-07-03_air-quality-habitat-suitability_cross-note.md
2026-07-03_atmosphere-biodiversity-path-decision_cross-note.md
```

Use lowercase filenames and hyphenated schema short names.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/contracts/v1/cross/atmosphere_biodiversity/`.
- [ ] Confirm whether cross-domain schema families are permitted under `schemas/contracts/v1/cross/`.
- [ ] Confirm whether this path should remain index-only.
- [ ] Confirm canonical biodiversity owner lanes for Flora, Fauna, Habitat, or another accepted family.
- [ ] Confirm paired Atmosphere and biodiversity-owning contract paths.
- [ ] Confirm cross-domain contract path, if any.
- [ ] Confirm schema registry records.
- [ ] Confirm valid fixture paths.
- [ ] Confirm invalid fixture paths.
- [ ] Confirm public-safe fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm geoprivacy and sensitivity-review pointers for schema work.
- [ ] Confirm whether `schemas/README.md` should index this cross-domain compatibility lane.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | Cross-domain schema-home decision, new Atmosphere × Biodiversity schema, biodiversity owner-lane decision, schema migration, validator update, fixture update, registry update, sensitivity update, ADR update, or compatibility-lane decision |
