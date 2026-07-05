# tests/domains/agriculture/soil_moisture

Soil-moisture context test lane for the KFM Agriculture domain.

## Status

Draft. This file was expanded from an empty placeholder on 2026-07-05.

## Purpose

This directory is for tests that prove Agriculture soil-moisture context is handled safely, with source-role, evidence, policy, fixture, and ownership boundaries preserved.

Agriculture may cite soil-moisture context for crop stress, suitability, drought context, or aggregate interpretation, but this test lane must not make Agriculture the owner of canonical Soil or Hydrology truth.

## Evidence basis

Current-session evidence supports these boundaries:

- `tests/` is the canonical enforceability-proof root.
- `tests/domains/agriculture/` exists but is still a greenfield stub.
- Agriculture file-system docs place Agriculture tests under `tests/domains/agriculture/` as the domain test segment.
- Agriculture no-network runbook docs require deterministic synthetic fixtures before live sources or public surfaces.
- `fixtures/domains/agriculture/soil_moisture/README.md` exists and states that fixture material is not station truth, source registry authority, Soil-domain authority, catalog authority, policy authority, release approval, or publication authority.
- The soil-moisture fixture README requires source-role preservation for observed station-series context, modeled products, and aggregate summaries.

## Authority boundary

| Concern | Authority home | This lane |
|---|---|---|
| Agriculture soil-moisture tests | `tests/domains/agriculture/soil_moisture/` | Tests only. |
| Soil-moisture fixtures | `fixtures/domains/agriculture/soil_moisture/` | Referenced by tests. |
| Agriculture object meaning | `contracts/domains/agriculture/` | Tests only. |
| Soil-domain meaning | `contracts/domains/soil/` and Soil-domain roots | Referenced only; not redefined here. |
| Hydrology-domain meaning | Hydrology-domain roots | Referenced only; not redefined here. |
| Machine shape | `schemas/contracts/v1/domains/agriculture/` | Tests only. |
| Policy rules | `policy/domains/agriculture/` or accepted policy lane | Tests only. |
| Source registry and source descriptors | `data/registry/sources/` and accepted source roots | References only. |
| Lifecycle data and catalog records | `data/` accepted lifecycle/catalog lanes | References only. |
| Release decisions | `release/` | Tests only. |

## Test responsibilities

Soil-moisture tests should verify that:

- source role is explicit and preserved;
- observed station-series examples are not mislabeled as modeled products;
- modeled products are not mislabeled as observations;
- aggregate summaries keep their scale and time scope;
- source, depth, time, QA, uncertainty, and citation posture are present when required;
- Agriculture stress or suitability helpers cite soil-moisture context rather than owning it as root truth;
- evidence and policy posture are checked before public-facing use;
- unsupported or ambiguous soil-moisture context abstains, denies, or fails safely.

## Required negative cases

| Case | Expected posture |
|---|---|
| Source role is missing | fail closed |
| Observed context is mislabeled as modeled context | test failure |
| Modeled context is mislabeled as observed context | test failure |
| Time, depth, QA, citation, or uncertainty support is missing where required | abstain or fail closed |
| Agriculture output claims canonical Soil or Hydrology truth | test failure |
| Fixture bypasses the accepted fixture lane | test failure |
| Live source access is required for the default test | test failure |
| Public-facing output implies more precision than the fixture supports | fail closed |

## What belongs here

- This README.
- Agriculture soil-moisture test modules.
- Tests for source-role preservation.
- Tests for observed, modeled, and aggregate context handling.
- Tests for citation, evidence, time, QA, depth, and uncertainty posture.
- Tests that Agriculture consumers cite Soil or Hydrology context without re-owning it.
- Test-only references to contracts, schemas, policy, fixtures, validators, data records, and release records.

## What does not belong here

- Agriculture implementation code.
- Soil or Hydrology implementation code.
- Contracts or schemas.
- Policy rules.
- Validator implementation.
- General fixture libraries or source data.
- Source registry records.
- Lifecycle or release records.
- Live source calls.
- Generated text treated as authority.

## Validation

```bash
find tests/domains/agriculture/soil_moisture -maxdepth 5 -type f | sort
find fixtures/domains/agriculture/soil_moisture tests/domains/agriculture schemas/contracts/v1/domains/agriculture contracts/domains/agriculture contracts/domains/soil policy/domains/agriculture tools/validators data/registry/sources -maxdepth 5 -type f 2>/dev/null | sort
pytest tests/domains/agriculture/soil_moisture tests/policy tests/contracts || true
```

Replace `|| true` with fail-closed CI behavior once accepted agriculture soil-moisture test commands are confirmed.

## Open questions

| Question | Status |
|---|---|
| Which Agriculture soil-moisture schema or contract is canonical for tests? | NEEDS VERIFICATION |
| Which fixtures in `fixtures/domains/agriculture/soil_moisture/` are canonical? | NEEDS VERIFICATION |
| Which validator path owns soil-moisture source-role checks? | NEEDS VERIFICATION |
| Which CI workflow blocks promotion when soil-moisture tests fail? | NEEDS VERIFICATION |
