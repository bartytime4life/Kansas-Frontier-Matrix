# tests/domains/agriculture/ssurgo_lineage

SSURGO-lineage test lane for the KFM Agriculture domain.

## Status

Draft. This file was expanded from an empty placeholder on 2026-07-05.

## Purpose

This directory is for tests that prove Agriculture uses SSURGO-derived context with clear lineage, source role, evidence support, and ownership boundaries.

Agriculture may use SSURGO-derived context for suitability, crop stress, or aggregate interpretation, but this test lane must not make Agriculture the owner of canonical Soil-domain semantics, source registry records, lifecycle data, or release decisions.

## Evidence basis

Current-session evidence supports these boundaries:

- `tests/` is the canonical enforceability-proof root.
- `tests/domains/agriculture/` exists but is still a greenfield stub.
- Agriculture file-system docs place Agriculture tests under `tests/domains/agriculture/` as the domain test segment.
- Agriculture file-system docs identify source-descriptor, evidence-closure, citation-validation, release-manifest, rollback-drill, and non-regression tests as Agriculture test responsibilities.
- Agriculture file-system docs identify connectors such as NRCS as source-specific fetch/admission lanes and state that connectors must not publish or mutate canonical truth.
- Agriculture sensitivity docs state that canonical soil semantics are owned by the Soil domain, not Agriculture.

## Authority boundary

| Concern | Authority home | This lane |
|---|---|---|
| SSURGO-lineage tests for Agriculture use | `tests/domains/agriculture/ssurgo_lineage/` | Tests only. |
| Soil-domain meaning and static soil authority | `contracts/domains/soil/` and Soil-domain roots | Referenced only; not redefined here. |
| Agriculture object meaning | `contracts/domains/agriculture/` | Tests only. |
| Machine shape | `schemas/contracts/v1/domains/agriculture/` and Soil companion schemas where accepted | Tests only. |
| Source descriptors and source registry | accepted source registry roots under `data/registry/sources/` | References only. |
| Connectors and source admission | accepted connector roots | References only. |
| Fixtures | `fixtures/domains/agriculture/` or accepted fixture lane | References only unless test-scoped. |
| Validators | `tools/validators/` | Tests only. |
| Lifecycle and catalog records | `data/` accepted lifecycle/catalog lanes | References only. |
| Release decisions | `release/` | Tests only. |

## Test responsibilities

SSURGO-lineage tests should verify that:

- SSURGO-derived context has an explicit source descriptor or accepted source pointer;
- lineage from source-shaped fixture to Agriculture output is traceable;
- source role is preserved and not upgraded by Agriculture tests;
- Soil-domain meaning remains owned by Soil-domain roots;
- Agriculture suitability or stress outputs cite soil context rather than re-owning it;
- evidence and citation support resolves before answer-like output is accepted;
- aggregation, generalization, review, policy, and release posture are explicit where public-facing output is tested;
- unsupported or ambiguous lineage abstains, denies, or fails safely.

## Required negative cases

| Case | Expected posture |
|---|---|
| SSURGO-derived fixture has no source pointer | fail closed |
| Source role is missing or unclear | fail closed |
| Agriculture output claims canonical Soil-domain truth | test failure |
| Evidence or citation support cannot resolve | abstain or fail closed |
| Connector output is treated as published truth | test failure |
| Lifecycle phase is skipped | fail closed |
| Release-facing output lacks policy or release posture | deny or fail closed |
| Test requires live source access in the default suite | test failure |

## What belongs here

- This README.
- Agriculture SSURGO-lineage test modules.
- Tests for source-pointer and source-role preservation.
- Tests for source-to-fixture-to-output traceability.
- Tests for EvidenceRef, EvidenceBundle, citation, receipt, and catalog closure where relevant.
- Tests that Agriculture consumers cite Soil context without re-owning Soil truth.
- Test-only references to contracts, schemas, policy, fixtures, validators, source registry records, data records, and release records.

## What does not belong here

- Agriculture implementation code.
- Soil implementation code.
- Contracts or schemas.
- Source registry records.
- Connector implementation.
- Policy rules.
- Validator implementation.
- General fixture libraries or source data.
- Lifecycle, catalog, proof, receipt, or release records.
- Live source calls.
- Generated text treated as authority.

## Validation

```bash
find tests/domains/agriculture/ssurgo_lineage -maxdepth 5 -type f | sort
find tests/domains/agriculture fixtures/domains/agriculture schemas/contracts/v1/domains/agriculture contracts/domains/agriculture contracts/domains/soil data/registry/sources policy/domains/agriculture tools/validators -maxdepth 5 -type f 2>/dev/null | sort
pytest tests/domains/agriculture/ssurgo_lineage tests/policy tests/contracts || true
```

Replace `|| true` with fail-closed CI behavior once accepted Agriculture SSURGO-lineage test commands are confirmed.

## Open questions

| Question | Status |
|---|---|
| Which SSURGO source descriptor or registry entry is canonical for Agriculture lineage tests? | NEEDS VERIFICATION |
| Which Agriculture or Soil contract governs SSURGO-derived suitability context? | NEEDS VERIFICATION |
| Which fixtures are canonical for SSURGO-lineage tests? | NEEDS VERIFICATION |
| Which validator path owns SSURGO-lineage checks? | NEEDS VERIFICATION |
| Which CI workflow blocks promotion when SSURGO-lineage tests fail? | NEEDS VERIFICATION |
