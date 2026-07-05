# tests/domains/archaeology/fixtures/source_admission

Source-admission fixture-test lane for the KFM Archaeology domain.

## Status

Draft. This file was expanded from an empty placeholder on 2026-07-05.

## Purpose

This directory is for tests that verify archaeology source-admission fixtures are safe, synthetic, reviewable, and bounded before they are used by default test runs.

Because Archaeology is a sensitive domain, this lane must prove that fixture-shaped source inputs do not become source authority, lifecycle data, catalog truth, release approval, or public output.

## Evidence basis

Current-session evidence supports these boundaries:

- `tests/domains/archaeology/fixtures/source_admission/README.md` existed as an empty placeholder before this update.
- `tests/domains/archaeology/README.md` exists but is still a greenfield stub.
- Archaeology file-system docs place domain tests under `tests/domains/archaeology/` and domain fixtures under `fixtures/domains/archaeology/`.
- Archaeology file-system docs mark implementation maturity as proposed or needing verification.
- Archaeology sensitivity docs describe the lane as deny-by-default and review-gated for protected details.

## Authority boundary

| Concern | Authority home | This lane |
|---|---|---|
| Source-admission fixture tests | `tests/domains/archaeology/fixtures/source_admission/` | Tests only. |
| Canonical fixture payloads | `fixtures/domains/archaeology/` or accepted fixture lane | Referenced only unless explicitly test-scoped. |
| Archaeology object meaning | `contracts/domains/archaeology/` | Tested here; not defined here. |
| Machine shape | `schemas/contracts/v1/domains/archaeology/` | Tested here; not authored here. |
| Policy rules | `policy/domains/archaeology/` or accepted policy lane | Tested here; not defined here. |
| Source descriptors and source registry | accepted source registry roots | Referenced here; not authored here. |
| Lifecycle and catalog records | `data/` accepted lifecycle/catalog lanes | Referenced here; not stored here. |
| Release and rollback decisions | `release/` | Tested here; not decided here. |

## Test responsibilities

Source-admission fixture tests should verify that:

- every fixture is marked as synthetic or test-scoped;
- source identity, rights posture, review posture, and sensitivity posture are explicit;
- protected details are absent, generalized, or represented only by safe mock markers;
- source-role and candidate-vs-confirmed posture are preserved;
- evidence and policy prerequisites are not assumed from fixture existence;
- fixtures never promote themselves into lifecycle, catalog, proof, or release records;
- unsupported fixture cases deny, abstain, quarantine, or fail safely.

## Required negative cases

| Case | Expected posture |
|---|---|
| Fixture has no synthetic or test marker | test failure |
| Fixture lacks source identity | fail closed |
| Fixture lacks rights or review posture | deny or fail closed |
| Fixture contains protected details instead of safe mock material | test failure |
| Fixture is treated as admitted source truth because it exists | test failure |
| Source role is missing or upgraded by a test helper | fail closed |
| Fixture requires live source access in the default suite | test failure |

## What belongs here

- This README.
- Tests for archaeology source-admission fixture safety.
- Tests for fixture markers, source identity, rights posture, review posture, and sensitivity posture.
- Tests for candidate-vs-confirmed and source-role preservation.
- Test-only references to contracts, schemas, policy, fixtures, source records, data records, and release records.

## What does not belong here

- Canonical archaeology fixture libraries.
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
find tests/domains/archaeology/fixtures/source_admission -maxdepth 5 -type f | sort
find fixtures/domains/archaeology tests/domains/archaeology schemas/contracts/v1/domains/archaeology contracts/domains/archaeology policy/domains/archaeology data release -maxdepth 5 -type f 2>/dev/null | sort
pytest tests/domains/archaeology/fixtures/source_admission tests/policy tests/contracts || true
```

Replace `|| true` with fail-closed CI behavior once accepted archaeology source-admission fixture test commands are confirmed.

## Open questions

| Question | Status |
|---|---|
| Which archaeology fixture lane is canonical for source-admission inputs? | NEEDS VERIFICATION |
| Which source-admission schema or contract is canonical for these tests? | NEEDS VERIFICATION |
| Which policy bundle owns archaeology source-admission denial behavior? | NEEDS VERIFICATION |
| Which CI workflow blocks promotion when these tests fail? | NEEDS VERIFICATION |
