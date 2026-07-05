# tests/domains/agriculture/aggregate_only

Aggregate-only test lane for the KFM Agriculture domain.

## Status

Draft. This file was expanded from an empty placeholder on 2026-07-05.

## Purpose

This directory is for tests that prove Agriculture outputs remain aggregate, public-safe, evidence-backed, and release-gated.

The lane focuses on aggregate observations such as county-year, crop-reporting-district-year, or other approved public-safe summaries. It should verify that aggregate outputs are never treated as field-level, operator-level, parcel-level, or private-party truth.

## Evidence basis

Current-session evidence supports these boundaries:

- `tests/` is the canonical enforceability-proof root.
- `tests/domains/agriculture/` exists but is still a greenfield stub.
- Agriculture sensitivity docs describe aggregate county-year statistics as public-safe by default when they remain aggregate.
- Agriculture runbook docs require deterministic no-network tests with synthetic fixtures before live sources or public surfaces.
- Agriculture file-system docs place agriculture tests under `tests/domains/agriculture/` as the domain test segment.

## Authority boundary

| Concern | Authority home | This lane |
|---|---|---|
| Agriculture object meaning | `contracts/domains/agriculture/` | Tests only. |
| Machine shape | `schemas/contracts/v1/domains/agriculture/` | Tests only. |
| Policy rules | `policy/domains/agriculture/` or accepted policy lane | Tests only. |
| Fixtures | `fixtures/domains/agriculture/` or accepted fixture lane | References only unless test-scoped. |
| Validators | `tools/validators/` | Tests only. |
| Lifecycle records | `data/` | References only. |
| Release decisions | `release/` | Tests only. |

## Test responsibilities

Aggregate-only tests should verify that:

- the aggregation unit is explicit;
- the output keeps its aggregate source role;
- any required aggregation receipt or equivalent proof pointer is present;
- evidence support resolves before answer-like output is accepted;
- policy state is checked before public use;
- field-level or private-party interpretation is denied or fails safely;
- public API, UI, tile, report, and AI surfaces cannot imply more precision than the aggregate supports.

## Required negative cases

| Case | Expected posture |
|---|---|
| Aggregate record has no aggregation unit | fail closed |
| Aggregate record lacks evidence support | abstain |
| Aggregate output is interpreted as a specific field or operator claim | fail closed |
| Aggregate output bypasses policy or release posture | fail closed |
| Aggregate fixture resembles live private data | test failure and fixture replacement |

## What belongs here

- This README.
- Aggregate-only Agriculture test modules.
- Tests for aggregation-unit presence.
- Tests for source-role preservation.
- Tests for aggregate evidence closure.
- Tests for public-safe response posture.
- Test-only references to contracts, schemas, policy, fixtures, validators, receipts, data records, and release records.

## What does not belong here

- Agriculture implementation code.
- Contracts or schemas.
- Policy rules.
- Validator implementation.
- General fixture libraries or source data.
- Lifecycle or release records.
- Live source calls.
- Generated text treated as authority.

## Validation

```bash
find tests/domains/agriculture/aggregate_only -maxdepth 5 -type f | sort
find tests/domains/agriculture fixtures/domains/agriculture policy/domains/agriculture schemas/contracts/v1/domains/agriculture contracts/domains/agriculture tools/validators -maxdepth 5 -type f 2>/dev/null | sort
pytest tests/domains/agriculture/aggregate_only tests/policy || true
```

Replace `|| true` with fail-closed CI behavior once accepted agriculture test commands are confirmed.

## Open questions

| Question | Status |
|---|---|
| Which aggregation receipt schema or contract is canonical for Agriculture aggregate tests? | NEEDS VERIFICATION |
| Which agriculture fixtures are canonical for aggregate-only tests? | NEEDS VERIFICATION |
| Which validator path owns aggregate-only checks? | NEEDS VERIFICATION |
| Which CI workflow blocks promotion when aggregate-only tests fail? | NEEDS VERIFICATION |
