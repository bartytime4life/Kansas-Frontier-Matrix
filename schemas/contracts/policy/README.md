# `schemas/contracts/policy/` — Policy Schema Compatibility Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-policy-readme
title: schemas/contracts/policy/ — Policy Schema Compatibility Index
version: v1
status: draft
policy_label: public
owners:
  - <schema-steward>
  - <policy-steward>
  - <contract-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, contracts, policy, compatibility, schemas-contracts-v1, json-schema]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![lane](https://img.shields.io/badge/lane-policy-blueviolet)
![posture](https://img.shields.io/badge/posture-compatibility--index-orange)
![canonical](https://img.shields.io/badge/canonical-NEEDS%20VERIFICATION-yellow)

## Purpose

`schemas/contracts/policy/` is a draft compatibility and index lane for policy-related schema notes.

It should help maintainers avoid mixing four different KFM roots: `contracts/` for meaning, `schemas/` for machine-checkable shape, `policy/` for gate logic, and `tests/` plus `fixtures/` for proof examples.

This README is documentation only. It is not a schema file, not contract prose, not gate logic, not validator code, and not lifecycle data.

## Status & authority

| Field | Value |
|---|---|
| Document type | Policy schema compatibility README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/policy/` |
| Status | Draft |
| Authority level | Compatibility/index guidance. Canonical schemas, contracts, schema registry records, validators, fixtures, tests, ADRs, and steward decisions outrank this README. |
| Path posture | Current-session evidence confirms this README was blank before this update. Current-session evidence did not confirm a parent `schemas/contracts/README.md`. |
| Canonical schema home | NEEDS VERIFICATION. ADR-0001 says cross-cutting schema families should live under `schemas/contracts/v1/<family>/...`. |
| Default posture | Do not create canonical policy schema definitions directly under `schemas/contracts/policy/` unless an ADR or migration note explicitly changes the schema-home rule. |
| Required reviewers | Schema steward, policy steward, contract steward, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the root for machine-checkable shape, paired one-to-one with `contracts/`, and excludes semantic prose, policy material, data, and code.

Current-session evidence confirms ADR-0001 says the default schema home is `schemas/contracts/v1/<family>/...`, while `contracts/` retains object meaning and `schemas/` owns machine-checkable shape.

Current-session evidence also confirms the architecture split between contract, schema, policy, and test layers.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    ├── policy/                       # you are here; compatibility/index lane
    └── v1/
        └── policy/                   # possible canonical family home; NEEDS VERIFICATION

contracts/
└── policy/                           # object meaning, not schema shape

policy/                               # gate logic, not schema shape

fixtures/
└── contracts/
    └── v1/
        └── policy/                   # observed fixture lane for policy objects
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/contracts/policy/README.md` | Blank before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| `schemas/contracts/README.md` | Not found during this edit. |
| ADR-0001 | Confirms `schemas/contracts/v1/` as the proposed canonical schema home. |
| Search for policy schema paths | Did not confirm a canonical `schemas/contracts/v1/policy/README.md` in this edit. |
| Search for policy object surfaces | Found policy contract and fixture surfaces outside this path. |

This README does not verify schema contents, registry entries, validators, CI behavior, or whether a `schemas/contracts/v1/policy/` lane should be created.

## Compatibility-lane responsibilities

| Responsibility | Expectation |
|---|---|
| Canonical-home decision | Determine the accepted canonical schema path for policy-shaped objects. |
| Drift prevention | Prevent duplicate canonical schemas under `schemas/contracts/policy/`. |
| Split preservation | Keep meaning, shape, gate behavior, and fixture proof in separate roots. |
| Migration notes | Record migration notes if compatibility files need to move. |
| Contract linkage | Point to paired contract files when verified. |
| Fixture linkage | Point to valid and invalid fixtures when verified. |
| Validator linkage | Point to validators or CI checks when verified. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## What belongs here

- This compatibility README.
- Short index notes that point to canonical policy schema files once confirmed.
- Migration notes for moving policy schema files into the accepted schema-home path.
- Drift notes about duplicate or stale policy schema paths.
- Links to canonical schemas, contracts, fixtures, validators, registry records, and tests.
- Notes explaining how policy object schemas remain shape definitions.

## What does not belong here

- New canonical policy schema definitions.
- Duplicate copies of canonical schema files.
- Contract prose.
- Gate-rule files.
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
| `ALIAS_CANDIDATE` | This path may be an alias for `schemas/contracts/v1/policy/` or another accepted family. |
| `TRANSITIONAL` | Content is awaiting migration to canonical schema home. |
| `DEPRECATED` | Content should no longer receive new files. |
| `MIGRATE_TO_V1_POLICY` | Content should move under `schemas/contracts/v1/policy/` if that lane is confirmed. |
| `MIGRATE_TO_RUNTIME` | Content should move under `schemas/contracts/v1/runtime/` if it is a runtime policy-decision shape. |
| `NEEDS_VERIFICATION` | Path, pairing, fixture, validator, or CI support has not been verified. |

## Minimal compatibility note

```markdown
# <policy-schema-compatibility-note-id>

## Status
INDEX_ONLY / ALIAS_CANDIDATE / TRANSITIONAL / DEPRECATED / MIGRATE_TO_V1_POLICY / MIGRATE_TO_RUNTIME / NEEDS_VERIFICATION

## Compatibility path
<schemas/contracts/policy/... or N/A>

## Proposed canonical schema path
<schemas/contracts/v1/policy/... / schemas/contracts/v1/runtime/... / NEEDS VERIFICATION>

## Paired contract
<contracts/policy/... / contracts/runtime/... / N/A>

## Fixtures
<fixtures/contracts/v1/policy/... or N/A>

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
- [ ] No duplicate canonical schema definitions are placed under `schemas/contracts/policy/`.
- [ ] Any migration or compatibility claim cites an ADR, migration note, or verified repo evidence.

## Naming guidance

Recommended compatibility-note pattern:

```text
<YYYY-MM-DD>_<schema-shortname>_compatibility-note.md
```

Examples:

```text
2026-07-03_policy-decision_compatibility-note.md
2026-07-03_policy-input-bundle_compatibility-note.md
2026-07-03_sensitivity-label_compatibility-note.md
```

Use lowercase filenames and hyphenated schema short names.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/contracts/policy/`.
- [ ] Confirm whether `schemas/contracts/policy/` should remain an index-only compatibility lane.
- [ ] Confirm whether canonical schema home should be `schemas/contracts/v1/policy/`, `schemas/contracts/v1/runtime/`, another family, or a different accepted path.
- [ ] Confirm whether a parent `schemas/contracts/README.md` should exist.
- [ ] Confirm paired contract paths for policy-shaped objects.
- [ ] Confirm schema registry records.
- [ ] Confirm valid fixture paths.
- [ ] Confirm invalid fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm whether `schemas/README.md` should index `contracts/policy/` directly as a compatibility lane.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | Canonical-home decision, new policy schema, policy-decision schema migration, validator update, fixture update, schema registry update, ADR update, or compatibility-lane decision |
