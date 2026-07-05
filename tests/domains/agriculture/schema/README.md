# tests/domains/agriculture/schema

Schema-conformance test lane for the KFM Agriculture domain.

## Status

Draft. This file was expanded from an empty placeholder on 2026-07-05.

## Purpose

This directory is for tests that prove Agriculture objects conform to their accepted machine-readable schemas without turning `tests/` into a schema authority.

Schema tests should validate shape, required fields, version posture, references, fixture compatibility, and failure behavior for Agriculture object families. They should not define or duplicate JSON Schema files.

## Evidence basis

Current-session evidence supports these boundaries:

- `tests/` is the canonical enforceability-proof root.
- `tests/domains/agriculture/` exists but is still a greenfield stub.
- Agriculture file-system docs place agriculture tests under `tests/domains/agriculture/` as the domain test segment.
- Agriculture file-system docs place Agriculture schema authority under `schemas/contracts/v1/domains/agriculture/`.
- Agriculture no-network runbook docs identify schema validation with synthetic fixtures as part of the Agriculture trust spine.

## Authority boundary

| Concern | Authority home | This lane |
|---|---|---|
| Agriculture JSON Schema definitions | `schemas/contracts/v1/domains/agriculture/` | Tests only. |
| Agriculture object meaning | `contracts/domains/agriculture/` | Tests only. |
| Policy rules | `policy/domains/agriculture/` or accepted policy lane | Tests only. |
| Fixtures | `fixtures/domains/agriculture/` or accepted fixture lane | References only unless test-scoped. |
| Validators | `tools/validators/` | Tests only. |
| Lifecycle records | `data/` | References only. |
| Release decisions | `release/` | Tests only. |

## Test responsibilities

Schema tests should verify that:

- every tested Agriculture fixture declares the expected schema family and version;
- valid fixtures pass the accepted schema;
- invalid fixtures fail for the expected reason;
- required identity, evidence, source-role, lifecycle, and policy-facing fields are present where required by schema;
- schema validation does not imply release approval;
- schema validity does not override policy, evidence, rights, review, aggregation, or release gates;
- missing or mismatched schema references fail safely.

## Required negative cases

| Case | Expected posture |
|---|---|
| Fixture has no schema reference | fail closed |
| Fixture references an unknown schema version | fail closed |
| Required field is missing | schema failure |
| Field type or enum value is invalid | schema failure |
| Valid schema shape is treated as release approval | test failure |
| Schema test duplicates canonical schema contents | test failure |
| Fixture resembles live private material | test failure and fixture replacement |

## What belongs here

- This README.
- Agriculture schema-conformance test modules.
- Tests for valid and invalid synthetic Agriculture fixtures.
- Tests for schema-version and schema-reference handling.
- Tests that schema validity remains separate from policy, evidence, and release approval.
- Test-only references to contracts, schemas, policy, fixtures, validators, data records, and release records.

## What does not belong here

- Agriculture implementation code.
- Canonical JSON Schema files.
- Contracts.
- Policy rules.
- Validator implementation.
- General fixture libraries or source data.
- Lifecycle or release records.
- Live source calls.
- Generated text treated as authority.

## Validation

```bash
find tests/domains/agriculture/schema -maxdepth 5 -type f | sort
find schemas/contracts/v1/domains/agriculture fixtures/domains/agriculture tests/domains/agriculture contracts/domains/agriculture policy/domains/agriculture tools/validators -maxdepth 5 -type f 2>/dev/null | sort
pytest tests/domains/agriculture/schema tests/schemas || true
```

Replace `|| true` with fail-closed CI behavior once accepted agriculture schema test commands are confirmed.

## Open questions

| Question | Status |
|---|---|
| Which Agriculture schema files are canonical and accepted for tests? | NEEDS VERIFICATION |
| Which Agriculture fixtures are canonical for schema conformance? | NEEDS VERIFICATION |
| Which validator path owns schema validation behavior? | NEEDS VERIFICATION |
| Which CI workflow blocks promotion when Agriculture schema tests fail? | NEEDS VERIFICATION |
