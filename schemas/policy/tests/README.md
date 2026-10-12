# `schemas/policy/tests/` — Policy Schema Test Compatibility Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-policy-tests-readme
title: schemas/policy/tests/ README
type: readme; compatibility-index; test-placement-guardrail
version: v0.1
status: draft; root-level-policy-test-compatibility-path; empty-test-path; NEEDS VERIFICATION
updated: 2026-07-04
policy_label: public
tags: [kfm, schemas, policy, tests, fixtures, compatibility, validation]
[/KFM_META_BLOCK_V2] -->

## Purpose

`schemas/policy/tests/` is a README-only compatibility guardrail for a root-level policy schema test path.

The inspected active policy schema family lives at `schemas/contracts/v1/policy/`.

The inspected policy fixture lane lives at `fixtures/contracts/v1/policy/`.

## Status

| Item | Status |
|---|---|
| README | present |
| Direct test files found under this path | none found in current search |
| Current role | compatibility guardrail |
| Placement | NEEDS VERIFICATION |

## Boundary

This directory is not the policy schema family, policy authority, fixture authority, validator implementation, CI configuration, or emitted test-result store.

It should not contain canonical policy schemas, policy rules, policy decision records, release records, fixtures, or validator code while the accepted homes remain separate.

## Current inventory

| Path | Status | Notes |
|---|---|---|
| `schemas/policy/tests/README.md` | present | Empty file expanded by this README. |
| `schemas/policy/tests/*` | not found in current search | No direct test files were found under this path. |
| `schemas/contracts/v1/policy/README.md` | present | Inspected policy schema family index. |
| `fixtures/contracts/v1/policy/README.md` | present | Inspected policy contract fixture lane. |

## Correct nearby lanes

| Need | Preferred lane |
|---|---|
| Policy schema shape | `schemas/contracts/v1/policy/` |
| Policy semantic meaning | `contracts/policy/` |
| Policy fixture examples | `fixtures/contracts/v1/policy/` |
| Schema test code | `tests/schemas/` or accepted project test root |
| Validator implementation | `tools/validators/` |
| Policy rules or operation | `policy/` |
| Release, correction, rollback decisions | `release/` |

## What belongs here

- This README.
- Temporary compatibility notes for this root-level path.
- Migration notes if any historical test files are discovered here.

## What does not belong here

- Canonical `.schema.json` files.
- Valid or invalid fixture JSON files that should live under `fixtures/contracts/v1/policy/`.
- Pytest files or validator code unless an ADR or migration note moves test ownership here.
- Policy rules, policy bundles, policy decisions, release records, receipts, proofs, or emitted validation reports.
- Claims that policy behavior is tested or enforced merely because this path exists.

## Compatibility rules

| Rule | Requirement |
|---|---|
| Keep schemas versioned | Policy schemas belong under `schemas/contracts/v1/policy/` unless an accepted migration says otherwise. |
| Keep fixtures out of schemas | Valid and invalid examples belong under fixture roots, not under this schema compatibility path. |
| Tests are not policy authority | A passing schema test proves shape behavior only; it does not prove policy enforcement. |
| Do not create parallel test roots | Add test files only to accepted test homes unless a migration note explains the exception. |

## Validation

```bash
find schemas/policy/tests -maxdepth 4 -type f | sort
find schemas/contracts/v1/policy -maxdepth 4 -type f | sort
find fixtures/contracts/v1/policy -maxdepth 5 -type f 2>/dev/null | sort
pytest tests/schemas tests/contract || true
```

Replace `|| true` with fail-closed CI behavior once the relevant test paths are confirmed.

## Open questions

| Question | Status |
|---|---|
| Should `schemas/policy/tests/` remain as a compatibility guardrail or be retired? | NEEDS VERIFICATION |
| Are there historical references that expect tests under this path? | NEEDS VERIFICATION |
| Should policy schema tests be generated from fixture manifests instead of hand-maintained paths? | NEEDS VERIFICATION |
