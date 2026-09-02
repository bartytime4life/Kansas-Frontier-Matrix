# `schemas/contracts/v1/domains/air/` — Air Domain Schema Compatibility Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-domains-air-readme
title: schemas/contracts/v1/domains/air/ — Air Domain Schema Compatibility Index
version: v1
status: draft
policy_label: public
owners:
  - <schema-steward>
  - <air-domain-steward>
  - <atmosphere-domain-steward>
  - <contract-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, contracts, v1, domains, air, atmosphere, compatibility, json-schema]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![domain](https://img.shields.io/badge/domain-air-blue)
![posture](https://img.shields.io/badge/posture-compatibility--index-orange)
![canonical](https://img.shields.io/badge/canonical-NEEDS%20VERIFICATION-yellow)

## Purpose

`schemas/contracts/v1/domains/air/` is a draft compatibility and index lane for Air schema notes.

Current-session evidence points Air-related schema material to the Atmosphere domain lane, especially `schemas/contracts/v1/domains/atmosphere/atmosphere_air_decision_envelope.schema.json`. Until stewards confirm Air as its own schema domain lane, this path should remain an index and placement note rather than a second schema authority.

This README is documentation only. It is not a schema file, contract prose, policy, validator code, lifecycle data, registry data, proof output, or release authority.

## Status & authority

| Field | Value |
|---|---|
| Document type | Air domain schema compatibility README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/v1/domains/air/` |
| Status | Draft |
| Authority level | Compatibility/index guidance. Canonical schemas, paired contracts, registry records, validators, fixtures, tests, ADRs, domain stewards, and release records outrank this README. |
| Path posture | Current-session evidence confirms this README was blank before this update. |
| Canonical status | NEEDS VERIFICATION. This edit did not confirm Air as an accepted standalone domain schema lane. |
| Confirmed related lane | `schemas/contracts/v1/domains/atmosphere/` exists as a PROPOSED Atmosphere domain schema lane. |
| Confirmed related schema | `schemas/contracts/v1/domains/atmosphere/atmosphere_air_decision_envelope.schema.json` exists as a PROPOSED scaffold. |
| Shorter alias lane | `schemas/contracts/v1/air/` exists as a compatibility placeholder and does not claim canonical status. |
| Default posture | Do not add canonical Air schema definitions here until an ADR, steward decision, registry entry, or migration note confirms this path. |
| Required reviewers | Schema steward, Air steward if assigned, Atmosphere steward, contract steward, validation steward where applicable, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the machine-checkable shape root and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says domain-specific schemas nest under `schemas/contracts/v1/domains/<domain>/...`, while `contracts/` retains object meaning and `schemas/` owns machine-checkable shape.

Current-session evidence confirms `schemas/contracts/v1/air/README.md` is a compatibility placeholder and says related material was found under the Atmosphere domain schema lane.

Current-session evidence confirms `schemas/contracts/v1/domains/atmosphere/README.md` exists as a PROPOSED Atmosphere domain schema lane.

Current-session evidence confirms an Atmosphere Air decision-envelope schema exists under the Atmosphere domain schema lane, paired to an Atmosphere contract.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    └── v1/
        ├── air/                              # shorter compatibility placeholder
        └── domains/
            ├── air/                          # you are here; compatibility/index lane
            └── atmosphere/                   # confirmed PROPOSED Atmosphere domain schema lane
                └── atmosphere_air_decision_envelope.schema.json

contracts/
└── domains/
    └── atmosphere/
        └── AtmosphereAirDecisionEnvelope.md
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/contracts/v1/domains/air/README.md` | Blank before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms domain schemas nest under `schemas/contracts/v1/domains/<domain>/...`. |
| `schemas/contracts/v1/air/README.md` | Existing shorter compatibility placeholder; canonical status NEEDS VERIFICATION. |
| `schemas/contracts/v1/domains/atmosphere/README.md` | Existing Atmosphere domain schema lane; status PROPOSED. |
| `schemas/contracts/v1/domains/atmosphere/atmosphere_air_decision_envelope.schema.json` | Existing PROPOSED scaffold schema for an Atmosphere Air decision envelope. |
| `contracts/domains/atmosphere/AtmosphereAirDecisionEnvelope.md` | Paired semantic contract for the Atmosphere/Air decision envelope. |

This README does not verify Air as a separate domain, schema completeness, schema registry entries, fixture coverage, validator wiring, CI behavior, policy behavior, release integration, runtime behavior, or public API/UI behavior.

## Compatibility-lane responsibilities

| Responsibility | Expectation |
|---|---|
| Canonical-home decision | Determine whether Air remains under Atmosphere, becomes a standalone domain lane, or stays index-only. |
| Drift prevention | Prevent duplicate Air schema definitions across `air/`, `domains/air/`, and `domains/atmosphere/`. |
| Atmosphere linkage | Point to Atmosphere-owned Air schemas and contracts when they are the confirmed home. |
| Contract linkage | Point to paired contracts when verified. |
| Fixture linkage | Point to valid and invalid fixtures when verified. |
| Validator linkage | Point to validators or CI checks when verified. |
| Registry linkage | Point to schema registry records when verified. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## What belongs here

- This README.
- Short index notes for Air schema placement.
- Migration notes if Air schema files move between compatibility, Atmosphere, or standalone Air lanes.
- Drift notes about duplicate or stale Air schema paths.
- Links to accepted schemas, paired contracts, fixtures, validators, schema registry records, policy references, release references, and tests.

## What does not belong here

- Canonical Air schema definitions before this path is confirmed.
- Duplicate copies of Atmosphere-owned Air schemas.
- Contract prose.
- Policy rules.
- Validator implementation code.
- Runtime code.
- Lifecycle data payloads.
- Registry records.
- Proof outputs.
- Release records.
- Public API or map/UI behavior.
- Claims that this path is canonical without ADR, registry, migration note, or steward confirmation.

## Compatibility status values

Use finite compatibility status values where possible:

| Status | Meaning |
|---|---|
| `INDEX_ONLY` | This path only indexes candidate Air schema locations. |
| `DOMAIN_CANDIDATE` | Air may become an accepted standalone schema domain. |
| `ATMOSPHERE_ALIAS` | Air material remains under the Atmosphere schema lane. |
| `TRANSITIONAL` | Content is awaiting migration to the accepted schema home. |
| `DEPRECATED` | Content should no longer receive new files. |
| `MIGRATE_TO_ATMOSPHERE` | Content belongs under `schemas/contracts/v1/domains/atmosphere/`. |
| `NEEDS_VERIFICATION` | Pairing, fixture, validator, registry, or CI support has not been verified. |

## Minimal compatibility note

```markdown
# <air-schema-compatibility-note-id>

## Status
INDEX_ONLY / DOMAIN_CANDIDATE / ATMOSPHERE_ALIAS / TRANSITIONAL / DEPRECATED / MIGRATE_TO_ATMOSPHERE / NEEDS_VERIFICATION

## Compatibility path
<schemas/contracts/v1/domains/air/... or N/A>

## Proposed canonical path
<schemas/contracts/v1/domains/air/... / schemas/contracts/v1/domains/atmosphere/... / NEEDS VERIFICATION>

## Paired contract
<contract path or N/A>

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

- [ ] Canonical schema path is linked or marked NEEDS VERIFICATION.
- [ ] Air vs Atmosphere ownership is explicit.
- [ ] Paired contract path is linked or marked NEEDS VERIFICATION.
- [ ] Schema registry entry is linked or marked NEEDS VERIFICATION.
- [ ] Valid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Invalid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Validator path is linked or marked NEEDS VERIFICATION.
- [ ] CI/schema-test support is linked or marked NEEDS VERIFICATION.
- [ ] No duplicate Atmosphere-owned schema definitions are placed under this path.
- [ ] Any migration or compatibility claim cites an ADR, migration note, or verified repo evidence.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/contracts/v1/domains/air/`.
- [ ] Confirm whether Air is an accepted standalone schema domain lane.
- [ ] Confirm whether Air should remain a compatibility alias to Atmosphere.
- [ ] Confirm schema registry records.
- [ ] Confirm paired Air or Atmosphere contract paths.
- [ ] Confirm valid fixture paths.
- [ ] Confirm invalid fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm whether `schemas/contracts/v1/domains/atmosphere/README.md` should index Air-related schemas.
- [ ] Confirm whether `schemas/contracts/v1/air/README.md` should remain a compatibility placeholder.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | Air domain-home decision, new Air schema, migration note, validator update, fixture update, schema registry update, ADR update, Atmosphere contract update, or compatibility-lane decision |
