# `schemas/contracts/v1/correction/` — Correction Schema Family Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-correction-readme
title: schemas/contracts/v1/correction/ — Correction Schema Family Index
version: v1
status: draft
policy_label: public
owners:
  - <schema-steward>
  - <correction-steward>
  - <release-steward>
  - <contract-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, contracts, v1, correction, correction-notice, release, rollback, json-schema]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-correction-blueviolet)
![posture](https://img.shields.io/badge/posture-schema--family-orange)
![schema](https://img.shields.io/badge/schema-stub-yellow)

## Purpose

`schemas/contracts/v1/correction/` is the draft schema family lane for correction-related KFM objects.

It should index machine-checkable schema files that support correction notices, supersession notices, withdrawals, rollback-aware correction flows, and release-facing repair records without silently mutating prior published records.

This README is documentation only. It is not itself a schema file, contract prose, policy, validator code, runtime code, lifecycle data, or release authority.

## Status & authority

| Field | Value |
|---|---|
| Document type | Correction schema family README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/v1/correction/` |
| Status | Draft |
| Authority level | Schema-family index guidance. Schema files, paired contracts, schema registry records, validators, fixtures, tests, ADRs, release records, and steward decisions outrank this README. |
| Path posture | Current-session evidence confirms this README existed as a minimal stub before this update. |
| Confirmed child schema | `correction_notice.schema.json` exists as a draft / PROPOSED stub. |
| Validator posture | NEEDS VERIFICATION. The schema-declared validator path was not verified in this edit. |
| Fixture posture | NEEDS VERIFICATION. The schema-declared fixture root was not verified in this edit. |
| Required reviewers | Schema steward, correction steward, release steward, contract steward, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the root for machine-checkable shape and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says the default schema home is `schemas/contracts/v1/<family>/...`, while `contracts/` retains object meaning and `schemas/` owns machine-checkable shape.

Current-session evidence confirms `contracts/correction/correction_notice.md` points to `schemas/contracts/v1/correction/correction_notice.schema.json` as its machine-checkable schema, while noting that the schema is a greenfield placeholder and validator behavior remains NEEDS VERIFICATION.

Current-session evidence confirms `release/corrections/` is a release responsibility root for governed release correction records. This schema lane supports machine shape; release state and correction records themselves do not live here.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    └── v1/
        └── correction/
            ├── README.md                    # you are here
            └── correction_notice.schema.json

contracts/
└── correction/
    └── correction_notice.md

release/
├── correction/
├── corrections/
└── correction_notices/
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/contracts/v1/correction/README.md` | Minimal stub before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms `schemas/contracts/v1/` as the proposed canonical schema home. |
| `schemas/contracts/v1/correction/correction_notice.schema.json` | Existing draft schema stub with `$id`, `x-kfm`, minimal fields, and `additionalProperties: true`. |
| `contracts/correction/correction_notice.md` | Paired semantic contract for `CorrectionNotice`. |
| `release/corrections/README.md` | Release corrections index; release records and steward decisions are not schema files. |

This README does not verify schema completeness, schema registry entries, fixture coverage, validator wiring, CI behavior, release-state integration, policy behavior, or public UI/API behavior.

## Current schema inventory

| Schema file | Paired contract | Status | Notes |
|---|---|---|---|
| `correction_notice.schema.json` | `contracts/correction/correction_notice.md` | PROPOSED / stub | Current schema requires `id`, allows additional properties, and declares x-kfm pointers for fixtures, validator, and policy. |

## Correction-lane responsibilities

| Responsibility | Expectation |
|---|---|
| Schema-family index | List correction schema files and their status. |
| Contract pairing | Maintain one-to-one pairing with correction semantic contracts. |
| Drift prevention | Prevent correction schemas from being duplicated under release or domain lanes unless an ADR or migration note permits it. |
| Release separation | Keep release records, correction notices, rollback records, and steward decisions in release lanes, not in schema files. |
| Fixture linkage | Point to valid and invalid fixtures when verified. |
| Validator linkage | Point to validators or CI checks when verified. |
| Registry linkage | Point to schema registry records when verified. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## What belongs here

- This README.
- Machine-checkable correction schemas.
- Short schema-family index notes.
- Migration notes for correction schema placement.
- Drift notes about duplicate or stale correction schema paths.
- Links to paired contracts, fixtures, validators, registry records, policy references, release references, and tests.

## What does not belong here

- Contract prose.
- Policy rules.
- Validator implementation code.
- Runtime code.
- Lifecycle data payloads.
- EvidenceBundle contents or source records.
- Release records.
- Correction records, correction notices, rollback records, or steward decisions as data.
- Silent mutation instructions for published material.
- Claims that a schema is complete without fixtures, validators, registry records, and review support.

## Schema status values

Use finite status values where possible:

| Status | Meaning |
|---|---|
| `STUB` | Schema exists but is not field-complete. |
| `DRAFT_SCHEMA` | Schema has meaningful fields but still needs review and test support. |
| `ACTIVE_SCHEMA` | Schema has accepted contract pairing, fixtures, validator support, registry record, and review status. |
| `MIRROR` | Schema mirrors another accepted schema location. |
| `TRANSITIONAL` | Schema is awaiting migration to the accepted home. |
| `DEPRECATED` | Schema should no longer receive new consumers. |
| `NEEDS_VERIFICATION` | Pairing, fixture, validator, registry, or CI support has not been verified. |

## Minimal schema note

```markdown
# <correction-schema-note-id>

## Status
STUB / DRAFT_SCHEMA / ACTIVE_SCHEMA / MIRROR / TRANSITIONAL / DEPRECATED / NEEDS_VERIFICATION

## Schema path
<schemas/contracts/v1/correction/...>

## Paired contract
<contracts/correction/... or N/A>

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

- [ ] Schema has a stable `$id`.
- [ ] Schema has `$schema` set to JSON Schema draft 2020-12 unless an ADR says otherwise.
- [ ] Paired contract path is linked.
- [ ] Schema registry entry is linked or marked NEEDS VERIFICATION.
- [ ] Valid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Invalid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Validator path is linked or marked NEEDS VERIFICATION.
- [ ] CI/schema-test support is linked or marked NEEDS VERIFICATION.
- [ ] Release/correction records remain outside `schemas/`.
- [ ] Any migration or compatibility claim cites an ADR, migration note, or verified repo evidence.

## Naming guidance

Recommended schema filename pattern:

```text
<object_name>.schema.json
```

Examples:

```text
correction_notice.schema.json
supersession_notice.schema.json
withdrawal_notice.schema.json
```

Use lowercase snake_case for schema filenames unless the schema registry or ADR specifies otherwise.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/contracts/v1/correction/`.
- [ ] Confirm whether `correction_notice.schema.json` should remain permissive or become strict.
- [ ] Confirm schema registry records.
- [ ] Confirm valid fixture paths.
- [ ] Confirm invalid fixture paths.
- [ ] Confirm validator path and behavior.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm whether supersession and withdrawal schemas belong in this family or another release/correction family.
- [ ] Confirm placement relationship between `contracts/correction/` and `contracts/release/` for correction-related objects.
- [ ] Confirm whether `schemas/README.md` should index this correction lane.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing minimal stub |
| Next review trigger | New correction schema, schema-home migration, validator update, fixture update, schema registry update, ADR update, correction contract update, release correction update, or compatibility-lane decision |
