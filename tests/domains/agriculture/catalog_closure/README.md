# tests/domains/agriculture/catalog_closure

Catalog-closure test lane for the KFM Agriculture domain.

## Status

Draft. This file was expanded from an empty placeholder on 2026-07-05.

## Purpose

This directory is for tests that prove Agriculture catalog records close against governed support before they can be treated as release-ready or public-facing.

Catalog closure means an Agriculture catalog entry has enough support to be inspectable and governable: source role, evidence support, aggregation or redaction posture where needed, policy posture, lifecycle state, validation result, receipt/proof pointers, release posture, and correction or rollback path where material.

## Evidence basis

Current-session evidence supports these boundaries:

- `tests/` is the canonical enforceability-proof root.
- `tests/domains/agriculture/` exists but is still a greenfield stub.
- Agriculture file-system docs place agriculture tests under `tests/domains/agriculture/` as the domain test segment.
- Agriculture no-network runbook docs identify catalog closure, release-manifest shape, rollback target shape, and no-network fixture testing as part of the Agriculture trust spine.
- Agriculture sensitivity docs require aggregate outputs and satellite products not to collapse into field-level or private-party truth.

## Authority boundary

| Concern | Authority home | This lane |
|---|---|---|
| Agriculture object meaning | `contracts/domains/agriculture/` | Tests only. |
| Machine shape | `schemas/contracts/v1/domains/agriculture/` | Tests only. |
| Policy rules | `policy/domains/agriculture/` or accepted policy lane | Tests only. |
| Fixtures | `fixtures/domains/agriculture/` or accepted fixture lane | References only unless test-scoped. |
| Validators | `tools/validators/` | Tests only. |
| Catalog, evidence, receipts, proofs | `data/` accepted lifecycle/proof/catalog lanes | References only. |
| Release decisions | `release/` | Tests only. |

## Test responsibilities

Catalog-closure tests should verify that:

- each Agriculture catalog record has a stable identity;
- source role is explicit and not collapsed;
- EvidenceRef resolves to adequate evidence support;
- aggregation, redaction, or model-run proof is linked where needed;
- policy state is available before public use;
- lifecycle state does not skip required gates;
- release posture is explicit and not inferred from catalog existence;
- correction and rollback pointers exist where release-facing output is tested;
- unsupported records abstain, deny, or fail safely.

## Required negative cases

| Case | Expected posture |
|---|---|
| Catalog entry has no stable identifier | fail closed |
| Catalog entry lacks EvidenceRef or EvidenceBundle support | abstain |
| Catalog entry has unclear source role | fail closed |
| Aggregate record lacks aggregation proof pointer | fail closed |
| Policy posture is missing for release-facing use | deny or fail closed |
| Catalog entry is treated as published only because it exists | test failure |
| Correction or rollback target is missing for release-facing record | fail closed |

## What belongs here

- This README.
- Agriculture catalog-closure test modules.
- Tests for EvidenceRef and EvidenceBundle closure.
- Tests for source-role preservation.
- Tests for aggregation, redaction, receipt, and proof pointers.
- Tests for catalog-to-release readiness boundaries.
- Test-only references to contracts, schemas, policy, fixtures, validators, data records, and release records.

## What does not belong here

- Agriculture implementation code.
- Contracts or schemas.
- Policy rules.
- Validator implementation.
- General fixture libraries or source data.
- Catalog, lifecycle, proof, receipt, or release records.
- Live source calls.
- Generated text treated as authority.

## Validation

```bash
find tests/domains/agriculture/catalog_closure -maxdepth 5 -type f | sort
find tests/domains/agriculture fixtures/domains/agriculture policy/domains/agriculture schemas/contracts/v1/domains/agriculture contracts/domains/agriculture tools/validators data release -maxdepth 5 -type f 2>/dev/null | sort
pytest tests/domains/agriculture/catalog_closure tests/policy tests/contracts || true
```

Replace `|| true` with fail-closed CI behavior once accepted agriculture test commands are confirmed.

## Open questions

| Question | Status |
|---|---|
| Which Agriculture catalog object contract is canonical for catalog-closure tests? | NEEDS VERIFICATION |
| Which evidence and receipt fixtures are canonical for Agriculture catalog closure? | NEEDS VERIFICATION |
| Which validator path owns catalog-closure checks? | NEEDS VERIFICATION |
| Which CI workflow blocks promotion when catalog-closure tests fail? | NEEDS VERIFICATION |
