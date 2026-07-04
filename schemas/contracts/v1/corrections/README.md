# `schemas/contracts/v1/corrections/` — Corrections Schema Compatibility Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-corrections-readme
title: schemas/contracts/v1/corrections/ — Corrections Schema Compatibility Index
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
tags: [kfm, schemas, contracts, v1, corrections, correction, compatibility, release, rollback, json-schema]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![lane](https://img.shields.io/badge/lane-corrections-blueviolet)
![posture](https://img.shields.io/badge/posture-compatibility--index-orange)
![canonical](https://img.shields.io/badge/canonical-correction%2F-green)

## Purpose

`schemas/contracts/v1/corrections/` is a draft compatibility and index lane for the plural corrections schema path.

Use this README to prevent the plural path from becoming a second schema authority beside the singular `schemas/contracts/v1/correction/` family. Current-session evidence supports the singular path as the active correction schema family lane.

This README is documentation only. It is not a schema file, contract prose, policy, validator code, runtime code, lifecycle data, release data, or release authority.

## Status & authority

| Field | Value |
|---|---|
| Document type | Corrections schema compatibility README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/v1/corrections/` |
| Status | Draft |
| Authority level | Compatibility/index guidance. Canonical schema files, paired contracts, schema registry records, validators, fixtures, tests, ADRs, release records, and steward decisions outrank this README. |
| Path posture | Current-session evidence confirms this README was blank before this update. |
| Canonical schema lane | `schemas/contracts/v1/correction/` unless a later ADR, registry decision, or migration note says otherwise. |
| Default posture | Do not add canonical correction schema definitions under this plural path. Place or migrate them under the accepted singular correction schema family unless maintainers explicitly decide otherwise. |
| Required reviewers | Schema steward, correction steward, release steward, contract steward, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the root for machine-checkable shape and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says the default schema home is `schemas/contracts/v1/<family>/...`, while `contracts/` retains object meaning and `schemas/` owns machine-checkable shape.

Current-session evidence confirms the singular `schemas/contracts/v1/correction/README.md` exists as the correction schema family index and currently inventories `correction_notice.schema.json` as a PROPOSED / stub schema paired to `contracts/correction/correction_notice.md`.

Current-session evidence also distinguishes schema shape from release correction records: `release/corrections/` is a release responsibility lane for governed release correction records, not a schema-definition home.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    └── v1/
        ├── correction/                  # canonical correction schema family lane
        │   ├── README.md
        │   └── correction_notice.schema.json
        └── corrections/                 # you are here; compatibility/index lane

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
| `schemas/contracts/v1/corrections/README.md` | Blank before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms `schemas/contracts/v1/` as the proposed canonical schema home. |
| `schemas/contracts/v1/correction/README.md` | Existing singular correction schema family index. |
| `schemas/contracts/v1/correction/correction_notice.schema.json` | Existing draft schema stub inventoried by the singular correction lane. |
| `contracts/correction/correction_notice.md` | Paired semantic contract for `CorrectionNotice`. |
| `release/corrections/README.md` | Release corrections index; release records and steward decisions are not schema files. |

This README does not verify schema completeness, schema registry entries, fixture coverage, validator wiring, CI behavior, release-state integration, policy behavior, or whether maintainers will retain both singular and plural correction schema paths.

## Compatibility-lane responsibilities

| Responsibility | Expectation |
|---|---|
| Canonical pointer | Point maintainers to `schemas/contracts/v1/correction/` as the active correction schema family lane. |
| Drift prevention | Prevent duplicate canonical schemas under `schemas/contracts/v1/corrections/`. |
| Migration notes | Record reversible migration notes if any files appear here. |
| Singular/plural decision | Track whether maintainers retain both paths, migrate this path, or deprecate it. |
| Contract linkage | Point to paired correction contracts when verified. |
| Fixture linkage | Point to valid and invalid fixtures when verified. |
| Validator linkage | Point to validators or CI checks when verified. |
| Registry linkage | Point to schema registry records when verified. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## What belongs here

- This compatibility README.
- Short index notes pointing to `schemas/contracts/v1/correction/`.
- Migration notes for any plural-path correction schema files that need to move.
- Drift notes about duplicate or stale correction schema paths.
- Links to canonical schemas, paired contracts, fixtures, validators, registry records, policy references, release references, and tests.

## What does not belong here

- New canonical correction schema definitions.
- Duplicate copies of schema files owned by `schemas/contracts/v1/correction/`.
- Contract prose.
- Policy rules.
- Validator implementation code.
- Runtime code.
- Lifecycle data payloads.
- EvidenceBundle contents or source records.
- Release records.
- Correction records, correction notices, rollback records, or steward decisions as data.
- Silent mutation instructions for published material.
- Claims that the plural path is canonical without ADR, registry, or steward confirmation.

## Compatibility status values

Use finite compatibility status values where possible:

| Status | Meaning |
|---|---|
| `INDEX_ONLY` | This path only points to the accepted correction schema lane. |
| `ALIAS_CANDIDATE` | This path may remain as a documented alias for `schemas/contracts/v1/correction/`. |
| `TRANSITIONAL` | Content is awaiting migration to the accepted schema home. |
| `DEPRECATED` | Content should no longer receive new files. |
| `MIGRATE_TO_CORRECTION` | Content should move under `schemas/contracts/v1/correction/`. |
| `NEEDS_VERIFICATION` | Pairing, fixture, validator, registry, or CI support has not been verified. |

## Minimal compatibility note

```markdown
# <corrections-schema-compatibility-note-id>

## Status
INDEX_ONLY / ALIAS_CANDIDATE / TRANSITIONAL / DEPRECATED / MIGRATE_TO_CORRECTION / NEEDS_VERIFICATION

## Compatibility path
<schemas/contracts/v1/corrections/... or N/A>

## Canonical path
<schemas/contracts/v1/correction/... or NEEDS VERIFICATION>

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

- [ ] Canonical correction schema path is linked.
- [ ] Any plural-path file is either migrated, justified, or marked NEEDS VERIFICATION.
- [ ] Paired contract path is linked or marked NEEDS VERIFICATION.
- [ ] Schema registry entry is linked or marked NEEDS VERIFICATION.
- [ ] Valid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Invalid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Validator path is linked or marked NEEDS VERIFICATION.
- [ ] CI/schema-test support is linked or marked NEEDS VERIFICATION.
- [ ] Release/correction records remain outside `schemas/`.
- [ ] Any migration or compatibility claim cites an ADR, migration note, or verified repo evidence.

## Naming guidance

If a compatibility note is needed, use:

```text
<YYYY-MM-DD>_<schema-shortname>_corrections-compatibility-note.md
```

Examples:

```text
2026-07-03_correction-notice_corrections-compatibility-note.md
2026-07-03_plural-path-decision_corrections-compatibility-note.md
```

Use lowercase filenames and hyphenated schema short names.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/contracts/v1/corrections/`.
- [ ] Confirm whether this plural path should remain as an index-only compatibility lane.
- [ ] Confirm whether this path should be deprecated in favor of `schemas/contracts/v1/correction/`.
- [ ] Confirm schema registry records reference the singular path, plural path, or both.
- [ ] Confirm valid fixture paths.
- [ ] Confirm invalid fixture paths.
- [ ] Confirm validator path and behavior.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm placement relationship between `schemas/contracts/v1/correction/` and `schemas/contracts/v1/corrections/`.
- [ ] Confirm whether `schemas/README.md` should index this plural compatibility lane.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | New correction schema, schema-home migration, singular/plural path decision, validator update, fixture update, schema registry update, ADR update, correction contract update, release correction update, or compatibility-lane decision |
