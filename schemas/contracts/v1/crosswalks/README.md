# `schemas/contracts/v1/crosswalks/` — Crosswalks Schema Compatibility Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-crosswalks-readme
title: schemas/contracts/v1/crosswalks/ — Crosswalks Schema Compatibility Index
version: v1
status: draft
policy_label: public
owners:
  - <schema-steward>
  - <crosswalk-steward>
  - <contract-steward>
  - <registry-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, contracts, v1, crosswalks, mappings, compatibility, json-schema]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![lane](https://img.shields.io/badge/lane-crosswalks-blueviolet)
![posture](https://img.shields.io/badge/posture-compatibility--index-orange)
![canonical](https://img.shields.io/badge/canonical-NEEDS%20VERIFICATION-yellow)

## Purpose

`schemas/contracts/v1/crosswalks/` is a draft compatibility and index lane for crosswalk-related schema notes.

A crosswalk schema should describe machine-checkable shape for governed mapping objects only after the paired semantic contract, registry role, fixture set, validator behavior, and review path are clear.

This README is documentation only. It is not a schema file, contract prose, validator code, registry data, lifecycle data, or release material.

## Status & authority

| Field | Value |
|---|---|
| Document type | Crosswalks schema compatibility README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/v1/crosswalks/` |
| Status | Draft |
| Authority level | Compatibility/index guidance. Canonical schemas, paired contracts, registry records, validators, fixtures, tests, ADRs, and steward decisions outrank this README. |
| Path posture | Current-session evidence confirms this README was blank before this update. |
| Canonical status | NEEDS VERIFICATION. This edit did not confirm canonical schema files under `schemas/contracts/v1/crosswalks/`. |
| Paired semantic contract lane | `contracts/crosswalks/` exists and identifies this path as a candidate machine-shape home, still NEEDS VERIFICATION. |
| Registry lane | `data/registry/crosswalks/` exists as a governed mapping-state registry lane and does not replace schemas or contracts. |
| Default posture | Do not create canonical crosswalk schema definitions directly under this path until placement, pairing, validators, and fixtures are confirmed. |
| Required reviewers | Schema steward, crosswalk steward, contract steward, registry steward, validation steward, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the root for machine-checkable shape and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says the default schema home is `schemas/contracts/v1/<family>/...`, while `contracts/` retains object meaning and `schemas/` owns machine-checkable shape.

Current-session evidence from Directory Rules confirms machine shape belongs under `schemas/`, object meaning belongs under `contracts/`, and creating a parallel home for schemas, contracts, registries, releases, proofs, or receipts requires an ADR.

Current-session search found `contracts/crosswalks/README.md`, `data/registry/crosswalks/README.md`, source-catalog crosswalk documentation, and source registry surfaces. It did not confirm a populated canonical schema family under this path.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    └── v1/
        └── crosswalks/                    # you are here; compatibility/index lane

contracts/
└── crosswalks/                            # semantic meaning for crosswalk families
    └── taxonomy/                          # observed child semantic-contract lane

data/
└── registry/
    └── crosswalks/                        # governed mapping-state registry lane
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/contracts/v1/crosswalks/README.md` | Blank before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms `schemas/contracts/v1/` as the proposed canonical schema home and separates contract meaning from schema shape. |
| Directory Rules | Confirms machine shape belongs under `schemas/` and warns against creating parallel homes without an ADR. |
| Search for crosswalk surfaces | Found `contracts/crosswalks/README.md`, `data/registry/crosswalks/README.md`, source-catalog crosswalk docs, and related source registry surfaces. |
| `contracts/crosswalks/README.md` | Semantic contract parent for governed mapping families; paired schemas remain NEEDS VERIFICATION. |
| `data/registry/crosswalks/README.md` | Governed mapping-state registry lane; not a semantic contract or schema authority. |

This README does not verify schema contents, schema registry entries, fixture coverage, validator wiring, CI behavior, release integration, or whether `schemas/contracts/v1/crosswalks/` should host canonical schema files.

## Compatibility-lane responsibilities

| Responsibility | Expectation |
|---|---|
| Canonical-home decision | Determine whether crosswalk schemas belong here or under a narrower family path. |
| Contract pairing | Link each schema to a paired semantic contract in `contracts/crosswalks/` or a verified domain contract. |
| Registry boundary | Keep registry records in `data/registry/crosswalks/`, not in schema files. |
| Drift prevention | Prevent duplicate canonical crosswalk schema definitions under unreviewed paths. |
| Fixture linkage | Point to valid, invalid, conflicted, stale, deprecated, and public-safe fixtures when verified. |
| Validator linkage | Point to validators or CI checks when verified. |
| Registry linkage | Point to schema registry records when verified. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## What belongs here

- This compatibility README.
- Machine-checkable crosswalk schemas once placement is confirmed.
- Short index notes that point to accepted crosswalk schema files once confirmed.
- Migration notes for moving crosswalk schemas into the accepted schema-home path.
- Drift notes about duplicate or stale crosswalk schema paths.
- Links to canonical schemas, paired contracts, registry records, fixtures, validators, release references, and tests.

## What does not belong here

- New canonical crosswalk schema definitions before steward confirmation.
- Duplicate copies of canonical schema files.
- Contract prose.
- Validator implementation code.
- Registry records.
- Lifecycle data payloads.
- Release records.
- Public map/UI behavior.
- Claims that this path is canonical without ADR, registry, migration note, or steward confirmation.

## Compatibility status values

Use finite compatibility status values where possible:

| Status | Meaning |
|---|---|
| `INDEX_ONLY` | This path only indexes candidate canonical schema locations. |
| `FAMILY_CANDIDATE` | Crosswalks may become an accepted schema family. |
| `ACTIVE_SCHEMA_FAMILY` | Crosswalk schemas are accepted and supported by contracts, registry records, fixtures, validators, and review. |
| `TRANSITIONAL` | Content is awaiting migration to the accepted schema home. |
| `DEPRECATED` | Content should no longer receive new files. |
| `MIGRATE_TO_NARROWER_FAMILY` | Content belongs under a more specific schema family. |
| `NEEDS_VERIFICATION` | Path, pairing, fixture, validator, registry, or CI support has not been verified. |

## Minimal compatibility note

```markdown
# <crosswalk-schema-compatibility-note-id>

## Status
INDEX_ONLY / FAMILY_CANDIDATE / ACTIVE_SCHEMA_FAMILY / TRANSITIONAL / DEPRECATED / MIGRATE_TO_NARROWER_FAMILY / NEEDS_VERIFICATION

## Compatibility path
<schemas/contracts/v1/crosswalks/... or N/A>

## Proposed canonical path
<schemas/contracts/v1/crosswalks/... / schemas/contracts/v1/<narrower-family>/... / NEEDS VERIFICATION>

## Paired contract
<contracts/crosswalks/... or domain contract path or N/A>

## Registry lane
<data/registry/crosswalks/... or N/A>

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
- [ ] Paired semantic contract path is linked or marked NEEDS VERIFICATION.
- [ ] Registry lane is linked or marked N/A.
- [ ] Schema registry entry is linked or marked NEEDS VERIFICATION.
- [ ] Valid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Invalid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Conflicted/stale/deprecated fixtures are linked or marked NEEDS VERIFICATION where applicable.
- [ ] Validator path is linked or marked NEEDS VERIFICATION.
- [ ] CI/schema-test support is linked or marked NEEDS VERIFICATION.
- [ ] No duplicate canonical schema definitions are placed under this path.
- [ ] Registry records remain in `data/registry/crosswalks/`.
- [ ] Any migration or compatibility claim cites an ADR, migration note, or verified repo evidence.

## Naming guidance

Recommended schema filename pattern, if this family is accepted:

```text
<object_or_family_name>.schema.json
```

Recommended compatibility-note pattern:

```text
<YYYY-MM-DD>_<schema-shortname>_crosswalks-schema-note.md
```

Examples:

```text
taxonomy_crosswalk.schema.json
source_field_crosswalk.schema.json
authority_identifier_crosswalk.schema.json
2026-07-03_crosswalks-path-decision_crosswalks-schema-note.md
```

Use lowercase snake_case for schema filenames and lowercase hyphenated note filenames unless a schema registry or ADR specifies otherwise.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/contracts/v1/crosswalks/`.
- [ ] Confirm whether crosswalks is an accepted schema family or compatibility alias.
- [ ] Confirm canonical crosswalk schema home.
- [ ] Confirm paired `contracts/crosswalks/` contract paths.
- [ ] Confirm `data/registry/crosswalks/` record shape and relation to schemas.
- [ ] Confirm schema registry records.
- [ ] Confirm valid fixture paths.
- [ ] Confirm invalid fixture paths.
- [ ] Confirm conflicted, stale, deprecated, or public-safe fixture paths where applicable.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm release references for governed mappings.
- [ ] Confirm whether `schemas/README.md` should index this compatibility lane.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | Canonical-home decision, new crosswalk schema, migration note, validator update, fixture update, registry update, ADR update, contract update, registry-lane update, or compatibility-lane decision |
