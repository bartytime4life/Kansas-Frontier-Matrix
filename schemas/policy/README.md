# `schemas/policy/` — Policy Schema Compatibility Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-policy-readme
title: schemas/policy/ README
type: readme; compatibility-index; schema-boundary
version: v0.1
status: draft; root-level-policy-compatibility-path; no-direct-schema-files-found; NEEDS VERIFICATION
updated: 2026-07-04
policy_label: public
tags: [kfm, schemas, policy, compatibility, validation]
[/KFM_META_BLOCK_V2] -->

## Purpose

`schemas/policy/` is a root-level compatibility guardrail for policy schema placement.

The inspected active policy schema family lives at `schemas/contracts/v1/policy/`.

The inspected root-level policy test guardrail lives at `schemas/policy/tests/`.

## Status

| Item | Status |
|---|---|
| README | present |
| Direct schema files found under this root-level path | none found in current search |
| Child test guardrail | `schemas/policy/tests/README.md` present |
| Current role | compatibility guardrail |
| Placement | NEEDS VERIFICATION |

## Boundary

This folder is under `schemas/`, so it may contain machine-checkable shape material only if accepted here.

It is not the active v1 policy schema family, policy rule root, policy engine, fixture root, validator root, test root, data root, emitted decision store, or release root.

Schema validation here does not implement policy, grant access, downgrade sensitivity, approve release, redact data, or prove that a policy check happened.

## Current inventory

| Path | Status | Notes |
|---|---|---|
| `schemas/policy/README.md` | present | Empty file expanded by this README. |
| `schemas/policy/*` | not found in current search | No direct policy schema files were found under this root-level path. |
| `schemas/policy/tests/README.md` | present | README-only compatibility guardrail for root-level policy schema test placement. |
| `schemas/contracts/v1/policy/README.md` | present | Inspected active policy schema family index. |
| `fixtures/contracts/v1/policy/README.md` | present | Inspected policy contract fixture lane. |

## Correct nearby lanes

| Need | Preferred lane |
|---|---|
| Policy schema shape | `schemas/contracts/v1/policy/` |
| Policy semantic meaning | `contracts/policy/` |
| Policy fixtures | `fixtures/contracts/v1/policy/` |
| Schema tests | `tests/schemas/` or accepted project test root |
| Validator implementation | `tools/validators/` |
| Policy rules or operation | `policy/` |
| Release, correction, rollback decisions | `release/` |

## What belongs here

- This README.
- Compatibility notes for this root-level policy schema path.
- Migration notes if historical policy schema or test files are discovered here.
- Temporary mirror notes while placement is unresolved.

## What does not belong here

- New canonical v1 policy schemas while `schemas/contracts/v1/policy/` remains the active lane.
- Valid or invalid fixture JSON files that belong under `fixtures/contracts/v1/policy/`.
- Policy rules, policy bundles, policy decisions, access-control config, sensitivity decisions, redaction decisions, release records, receipts, proofs, emitted validation reports, or public artifacts.
- Validator code, runtime code, API/UI implementation, dashboards, screenshots, or generated summaries.
- Claims that policy behavior is tested, enforced, complete, or public-safe merely because this path exists or a payload validates against a schema.

## Compatibility rules

| Rule | Requirement |
|---|---|
| Keep schemas versioned | Policy schemas belong under `schemas/contracts/v1/policy/` unless an accepted migration says otherwise. |
| Keep fixtures out of schemas | Valid and invalid examples belong under fixture roots, not under this compatibility path. |
| Shape is not enforcement | A policy schema constrains record shape; it does not run or enforce policy. |
| Do not create parallel roots | Add schemas, tests, fixtures, or validators only to accepted homes unless a migration note explains the exception. |

## Validation

```bash
find schemas/policy -maxdepth 4 -type f | sort
find schemas/contracts/v1/policy -maxdepth 4 -type f | sort
find fixtures/contracts/v1/policy -maxdepth 5 -type f 2>/dev/null | sort
find schemas/policy -name '*.json' -print0 | xargs -0 -r -I{} python -m json.tool {} >/dev/null
pytest tests/schemas tests/contract || true
```

Replace `|| true` with fail-closed CI behavior once the relevant test paths are confirmed.

## Open questions

| Question | Status |
|---|---|
| Should `schemas/policy/` remain as a compatibility guardrail or be retired? | NEEDS VERIFICATION |
| Are there historical references that expect policy schemas under this path? | NEEDS VERIFICATION |
| Should `schemas/policy/tests/` be migrated, retained as a guardrail, or retired? | NEEDS VERIFICATION |
| Which policy fixture and schema-test manifests should drive validation? | NEEDS VERIFICATION |
