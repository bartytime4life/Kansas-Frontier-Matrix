# tests/domains/agriculture/veg_index

Vegetation-index context test lane for the KFM Agriculture domain.

## Status

Draft. This file was expanded from an empty placeholder on 2026-07-05.

## Purpose

This directory is for tests that prove Agriculture vegetation-index context is handled as governed context, not as direct field truth or release approval.

Vegetation-index tests should verify source role, derivation posture, evidence support, transform posture, policy state, and release readiness before any public-facing use.

## Evidence basis

Current-session evidence supports these boundaries:

- `tests/` is the canonical enforceability-proof root.
- `tests/domains/agriculture/` exists but is still a greenfield stub.
- Agriculture file-system docs identify vegetation context, stress indicators, crop observations, field candidates, and public-safe products as part of the Agriculture lane.
- Agriculture file-system docs place Agriculture tests under `tests/domains/agriculture/` as the domain test segment.
- Agriculture sensitivity docs treat field-level satellite indices as generalized context, not field truth.
- Agriculture sensitivity docs require support, transform, review, policy, and release posture for field-level or release-facing cases.

## Authority boundary

| Concern | Authority home | This lane |
|---|---|---|
| Agriculture vegetation-index tests | `tests/domains/agriculture/veg_index/` | Tests only. |
| Agriculture object meaning | `contracts/domains/agriculture/` | Tests only. |
| Machine shape | `schemas/contracts/v1/domains/agriculture/` | Tests only. |
| Policy rules | `policy/domains/agriculture/` or accepted policy lane | Tests only. |
| Fixtures | `fixtures/domains/agriculture/` or accepted fixture lane | References only unless test-scoped. |
| Evidence and receipt records | accepted `data/` proof/receipt/catalog lanes | References only. |
| Validators | `tools/validators/` | Tests only. |
| Lifecycle and catalog records | `data/` accepted lifecycle/catalog lanes | References only. |
| Release decisions | `release/` | Tests only. |

## Test responsibilities

Vegetation-index tests should verify that:

- vegetation-index values preserve source role and derivation posture;
- index-derived context is not mislabeled as direct observation;
- field-level context is transformed or blocked before public-facing use;
- evidence, citation, receipt, and model-run pointers are present where required;
- uncertainty, scale, time window, and product identity are preserved where required;
- public outputs do not imply more precision than the index supports;
- unsupported or ambiguous vegetation-index context abstains, denies, or fails safely.

## Required negative cases

| Case | Expected posture |
|---|---|
| Vegetation-index fixture has no source or derivation pointer | fail closed |
| Index-derived context is treated as direct field truth | test failure |
| Required transform posture is missing for public-facing use | deny or fail closed |
| Evidence, citation, or model-run support cannot resolve | abstain or fail closed |
| Output implies more precision than the index supports | fail closed |
| Policy or release posture is missing for public-facing use | deny or fail closed |
| Test requires live source access in the default suite | test failure |

## What belongs here

- This README.
- Agriculture vegetation-index test modules.
- Tests for source-role and derivation preservation.
- Tests for evidence, receipt, model-run, and transform pointer requirements.
- Tests for public-safe vegetation-index context handling.
- Tests that vegetation-index context does not become direct field truth.
- Test-only references to contracts, schemas, policy, fixtures, validators, data records, and release records.

## What does not belong here

- Agriculture implementation code.
- Contracts or schemas.
- Policy rules.
- Validator implementation.
- Model-run outputs, lifecycle data, catalog records, proof records, receipt records, or release records.
- General fixture libraries or source data.
- Live source calls.
- Generated text treated as authority.

## Validation

```bash
find tests/domains/agriculture/veg_index -maxdepth 5 -type f | sort
find tests/domains/agriculture fixtures/domains/agriculture schemas/contracts/v1/domains/agriculture contracts/domains/agriculture policy/domains/agriculture tools/validators data release -maxdepth 5 -type f 2>/dev/null | sort
pytest tests/domains/agriculture/veg_index tests/policy tests/contracts || true
```

Replace `|| true` with fail-closed CI behavior once accepted Agriculture vegetation-index test commands are confirmed.

## Open questions

| Question | Status |
|---|---|
| Which Agriculture vegetation-index schema or contract is canonical for tests? | NEEDS VERIFICATION |
| Which fixtures are canonical for vegetation-index tests? | NEEDS VERIFICATION |
| Which validator path owns vegetation-index source-role and transform checks? | NEEDS VERIFICATION |
| Which CI workflow blocks promotion when vegetation-index tests fail? | NEEDS VERIFICATION |
