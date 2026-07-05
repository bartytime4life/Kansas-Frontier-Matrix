# tests/domains/archaeology/fixtures

Fixture-test parent lane for the KFM Archaeology domain.

## Status

Draft. This file was expanded from an empty placeholder on 2026-07-05.

## Purpose

This directory is for tests that verify archaeology fixture handling, fixture safety, and fixture boundaries.

It is not the canonical fixture data home. Canonical archaeology fixtures belong under `fixtures/domains/archaeology/` or another accepted fixture lane. This path is for tests and test indexes that check fixture behavior.

## Evidence basis

Current-session evidence supports these boundaries:

- `tests/domains/archaeology/fixtures/README.md` existed as an empty placeholder before this update.
- `tests/domains/archaeology/fixtures/source_admission/README.md` exists and defines a source-admission fixture-test child lane.
- `tests/` is the enforceability-proof root and validates contracts, schemas, policy, release, governed API/UI, pipelines, and validators.
- Archaeology file-system docs place domain tests under `tests/domains/archaeology/` and domain fixtures under `fixtures/domains/archaeology/`.
- Archaeology sensitivity docs describe the lane as deny-by-default and review-gated for protected details.

## Authority boundary

| Concern | Authority home | This lane |
|---|---|---|
| Archaeology fixture tests | `tests/domains/archaeology/fixtures/` | Owns test organization only. |
| Canonical archaeology fixtures | `fixtures/domains/archaeology/` or accepted fixture lane | Referenced only. |
| Source-admission fixture checks | `tests/domains/archaeology/fixtures/source_admission/` | Child test lane. |
| Archaeology contracts | `contracts/domains/archaeology/` | Tested here; not defined here. |
| Archaeology schemas | `schemas/contracts/v1/domains/archaeology/` | Tested here; not authored here. |
| Archaeology policy | `policy/domains/archaeology/` or accepted policy lane | Tested here; not defined here. |
| Lifecycle, catalog, proof, and release records | `data/` and `release/` accepted lanes | Referenced only. |

## Current child lanes

| Lane | Purpose | Status |
|---|---|---|
| `source_admission/` | Tests source-admission fixture safety and bounded use. | README confirmed; implementation NEEDS VERIFICATION. |

## Test responsibilities

Fixture tests should verify that:

- fixture inputs are synthetic, test-scoped, and clearly marked;
- source identity, review posture, and sensitivity posture are explicit where required;
- fixture examples do not become source authority or release approval;
- fixture references do not bypass accepted schemas, contracts, policy, or validator paths;
- fixture cases fail safely when required support is missing;
- default tests do not require live source access.

## What belongs here

- This README.
- Child-lane README files and test indexes.
- Fixture-safety test modules.
- Test-only references to accepted archaeology fixture files.
- Tests for fixture markers, source posture, review posture, and fail-safe behavior.

## What does not belong here

- Canonical fixture libraries or large fixture payloads.
- Source registry records.
- Archaeology implementation code.
- Contracts or schemas.
- Policy rules.
- Validator implementation.
- Lifecycle, catalog, proof, receipt, release, or rollback records.
- Live source calls.
- Generated text treated as authority.

## Validation

```bash
find tests/domains/archaeology/fixtures -maxdepth 5 -type f | sort
find fixtures/domains/archaeology tests/domains/archaeology schemas/contracts/v1/domains/archaeology contracts/domains/archaeology policy/domains/archaeology data release -maxdepth 5 -type f 2>/dev/null | sort
pytest tests/domains/archaeology/fixtures tests/policy tests/contracts || true
```

Replace `|| true` with fail-closed CI behavior once accepted archaeology fixture-test commands are confirmed.

## Open questions

| Question | Status |
|---|---|
| Which archaeology fixture lane is canonical for test inputs? | NEEDS VERIFICATION |
| Which fixture-test child lanes should exist under this parent? | NEEDS VERIFICATION |
| Which validator path owns archaeology fixture safety checks? | NEEDS VERIFICATION |
| Which CI workflow blocks promotion when these tests fail? | NEEDS VERIFICATION |
