# `schemas/contracts/v1/agriculture/` — Agriculture Schema Compatibility Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-agriculture-readme
title: schemas/contracts/v1/agriculture/ — Agriculture Schema Compatibility Index
version: v1
status: draft
policy_label: public
owners:
  - <schema-steward>
  - <agriculture-domain-steward>
  - <contract-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, contracts, v1, agriculture, compatibility, json-schema]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![domain](https://img.shields.io/badge/domain-agriculture-green)
![posture](https://img.shields.io/badge/posture-compatibility--index-orange)
![canonical](https://img.shields.io/badge/canonical-NEEDS%20VERIFICATION-yellow)

## Purpose

`schemas/contracts/v1/agriculture/` is a draft compatibility and index lane for Agriculture schema notes.

It should help maintainers decide whether this shorter path remains as an index, migrates into `schemas/contracts/v1/domains/agriculture/`, or is deprecated once canonical Agriculture schema placement is confirmed.

This README is documentation only. It is not a schema file, not contract prose, not policy, not validator code, and not lifecycle data.

## Status & authority

| Field | Value |
|---|---|
| Document type | Agriculture schema compatibility README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/v1/agriculture/` |
| Status | Draft |
| Authority level | Compatibility/index guidance. Canonical schemas, contracts, schema registry records, validators, fixtures, tests, ADRs, and steward decisions outrank this README. |
| Path posture | Current-session evidence confirms this README was blank before this update. |
| Canonical schema home | NEEDS VERIFICATION. ADR-0001 says domain-specific schemas should nest under `schemas/contracts/v1/domains/<domain>/...`. |
| Default posture | Do not create new canonical Agriculture schema definitions directly under `schemas/contracts/v1/agriculture/` unless an ADR or migration note explicitly changes the schema-home rule. |
| Required reviewers | Schema steward, Agriculture domain steward, contract steward, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the root for machine-checkable shape and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says the default schema home is `schemas/contracts/v1/<family>/...`, and domain-specific schemas nest under `schemas/contracts/v1/domains/<domain>/...`.

Current-session search did not confirm a canonical `schemas/contracts/v1/domains/agriculture/README.md` path during this edit. Search did confirm Agriculture surfaces under contracts, fixtures, packages, policy, and docs.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    └── v1/
        ├── agriculture/                # you are here; compatibility/index lane
        └── domains/
            └── agriculture/            # likely canonical domain lane; NEEDS VERIFICATION

contracts/
└── domains/
    └── agriculture/                    # observed contract surface

fixtures/
└── domains/
    └── agriculture/                    # observed fixture surface
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/contracts/v1/agriculture/README.md` | Blank before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms `schemas/contracts/v1/` as the proposed canonical schema home and says domain schemas nest under `schemas/contracts/v1/domains/<domain>/...`. |
| Search for canonical Agriculture schema lane | Did not confirm `schemas/contracts/v1/domains/agriculture/README.md` in this edit. |
| Search for Agriculture surfaces | Found Agriculture contracts, fixtures, package, policy, and docs surfaces outside this path. |

This README does not verify schema contents, registry entries, fixture coverage, validator wiring, CI behavior, or whether `schemas/contracts/v1/agriculture/` should remain as a compatibility path.

## Compatibility-lane responsibilities

| Responsibility | Expectation |
|---|---|
| Canonical-home decision | Determine whether canonical Agriculture schemas belong under `schemas/contracts/v1/domains/agriculture/`. |
| Drift prevention | Prevent duplicate canonical schemas under `schemas/contracts/v1/agriculture/`. |
| Migration notes | Record migration notes if compatibility files need to move. |
| Contract linkage | Point to paired Agriculture contract files when verified. |
| Fixture linkage | Point to valid and invalid fixtures when verified. |
| Validator linkage | Point to validators or CI checks when verified. |
| Registry linkage | Point to schema registry records when verified. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## What belongs here

- This compatibility README.
- Short index notes that point to canonical Agriculture schema files once confirmed.
- Migration notes for moving Agriculture schemas into the accepted schema-home path.
- Drift notes about duplicate or stale Agriculture schema paths.
- Links to canonical schemas, contracts, fixtures, validators, registry records, and tests.

## What does not belong here

- New canonical Agriculture schema definitions.
- Duplicate copies of canonical schema files.
- Contract prose.
- Policy rules.
- Validator implementation code.
- Runtime code.
- Lifecycle data payloads.
- EvidenceBundle contents or source records.
- Release records.
- Claims that this path is canonical without ADR, registry, or steward confirmation.

## Compatibility status values

Use finite compatibility status values where possible:

| Status | Meaning |
|---|---|
| `INDEX_ONLY` | This path only indexes candidate canonical schema locations. |
| `ALIAS_CANDIDATE` | This path may be an alias for `schemas/contracts/v1/domains/agriculture/`. |
| `TRANSITIONAL` | Content is awaiting migration to canonical schema home. |
| `DEPRECATED` | Content should no longer receive new files. |
| `MIGRATE_TO_DOMAINS_AGRICULTURE` | Content should move under `schemas/contracts/v1/domains/agriculture/` if that lane is confirmed. |
| `NEEDS_VERIFICATION` | Path, pairing, fixture, validator, or CI support has not been verified. |

## Minimal compatibility note

```markdown
# <agriculture-schema-compatibility-note-id>

## Status
INDEX_ONLY / ALIAS_CANDIDATE / TRANSITIONAL / DEPRECATED / MIGRATE_TO_DOMAINS_AGRICULTURE / NEEDS_VERIFICATION

## Compatibility path
<schemas/contracts/v1/agriculture/... or N/A>

## Proposed canonical path
<schemas/contracts/v1/domains/agriculture/... or NEEDS VERIFICATION>

## Paired contract
<contracts/domains/agriculture/... or N/A>

## Fixtures
<fixtures/domains/agriculture/... or N/A>

## Validator
<tools/validators/... or N/A>

## Notes
<short note grounded in repo evidence>

## Follow-up
<open items or none>
```

## Review checklist

- [ ] Canonical schema path is linked or marked NEEDS VERIFICATION.
- [ ] Paired contract path is linked or marked NEEDS VERIFICATION.
- [ ] Schema registry entry is linked or marked NEEDS VERIFICATION.
- [ ] Valid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Invalid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Validator path is linked or marked NEEDS VERIFICATION.
- [ ] CI/schema-test support is linked or marked NEEDS VERIFICATION.
- [ ] No duplicate canonical schema definitions are placed under `schemas/contracts/v1/agriculture/`.
- [ ] Any migration or compatibility claim cites an ADR, migration note, or verified repo evidence.

## Naming guidance

Recommended compatibility-note pattern:

```text
<YYYY-MM-DD>_<schema-shortname>_compatibility-note.md
```

Examples:

```text
2026-07-03_domain-layer-descriptor_compatibility-note.md
2026-07-03_aggregation-receipt_compatibility-note.md
2026-07-03_crop-progress-panel_compatibility-note.md
```

Use lowercase filenames and hyphenated schema short names.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/contracts/v1/agriculture/`.
- [ ] Confirm whether `schemas/contracts/v1/agriculture/` should remain an index-only compatibility lane.
- [ ] Confirm whether canonical schema home should be `schemas/contracts/v1/domains/agriculture/`.
- [ ] Confirm whether `schemas/contracts/v1/domains/agriculture/README.md` should be created or already exists elsewhere.
- [ ] Confirm paired Agriculture contract paths.
- [ ] Confirm Agriculture schema registry records.
- [ ] Confirm valid fixture paths.
- [ ] Confirm invalid fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm whether `schemas/README.md` should index this compatibility lane.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | Canonical-home decision, new Agriculture schema, Agriculture schema migration, validator update, fixture update, schema registry update, ADR update, or compatibility-lane decision |
