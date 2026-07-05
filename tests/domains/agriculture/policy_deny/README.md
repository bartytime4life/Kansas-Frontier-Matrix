# tests/domains/agriculture/policy_deny

Policy-deny test lane for the KFM Agriculture domain.

## Status

Draft. This file was expanded from an empty placeholder on 2026-07-05.

## Purpose

This directory is for tests that prove Agriculture policy-deny and fail-closed behavior works before any Agriculture output is treated as public-safe, release-ready, or answer-ready.

The lane focuses on cases where Agriculture material must not pass through as public output because policy, rights, sensitivity, source role, evidence, lifecycle, aggregation, review, or release posture is missing or negative.

## Evidence basis

Current-session evidence supports these boundaries:

- `tests/` is the canonical enforceability-proof root.
- `tests/domains/agriculture/` exists but is still a greenfield stub.
- Agriculture sensitivity docs require aggregate outputs and satellite products not to collapse into field-level or private-party truth.
- Agriculture no-network runbook docs require deterministic offline tests with synthetic fixtures before live sources or public surfaces.
- Agriculture file-system docs place agriculture tests under `tests/domains/agriculture/` as the domain test segment.

## Authority boundary

| Concern | Authority home | This lane |
|---|---|---|
| Agriculture policy rules | `policy/domains/agriculture/` or accepted policy lane | Tests only. |
| Agriculture object meaning | `contracts/domains/agriculture/` | Tests only. |
| Machine shape | `schemas/contracts/v1/domains/agriculture/` | Tests only. |
| Fixtures | `fixtures/domains/agriculture/` or accepted fixture lane | References only unless test-scoped. |
| Validators | `tools/validators/` | Tests only. |
| Lifecycle records | `data/` | References only. |
| Release decisions | `release/` | Tests only. |

## Test responsibilities

Policy-deny tests should verify that:

- denied Agriculture cases do not fall through to public output;
- missing policy state fails safely;
- missing rights, review, aggregation, or release posture blocks release-facing output;
- source roles are preserved and not upgraded by tests;
- evidence gaps produce abstain or deny behavior as appropriate;
- aggregate records are not interpreted with more precision than they support;
- deny results do not become release approvals or catalog truth.

## Required negative cases

| Case | Expected posture |
|---|---|
| Policy decision is missing for release-facing Agriculture output | deny or fail closed |
| Policy decision explicitly denies the case | deny |
| Evidence support is missing | abstain or deny |
| Source role is unclear or collapsed | fail closed |
| Aggregate output is treated as a more precise claim | fail closed |
| Required review or release posture is missing | deny or fail closed |
| Test fixture could be mistaken for live private material | test failure and fixture replacement |

## What belongs here

- This README.
- Agriculture policy-deny test modules.
- Negative policy fixtures or references to accepted fixture lanes.
- Tests for deny, abstain, and fail-closed Agriculture outcomes.
- Tests that policy denial prevents catalog, release, API, UI, tile, report, or AI answer promotion.
- Test-only references to contracts, schemas, policy, fixtures, validators, data records, and release records.

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
find tests/domains/agriculture/policy_deny -maxdepth 5 -type f | sort
find tests/domains/agriculture fixtures/domains/agriculture policy/domains/agriculture schemas/contracts/v1/domains/agriculture contracts/domains/agriculture tools/validators data release -maxdepth 5 -type f 2>/dev/null | sort
pytest tests/domains/agriculture/policy_deny tests/policy || true
```

Replace `|| true` with fail-closed CI behavior once accepted agriculture policy-deny test commands are confirmed.

## Open questions

| Question | Status |
|---|---|
| Which Agriculture policy bundle is canonical for deny tests? | NEEDS VERIFICATION |
| Which deny fixtures are canonical for Agriculture policy tests? | NEEDS VERIFICATION |
| Which validator path owns Agriculture policy-deny checks? | NEEDS VERIFICATION |
| Which CI workflow blocks promotion when policy-deny tests fail? | NEEDS VERIFICATION |
