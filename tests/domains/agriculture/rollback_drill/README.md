# tests/domains/agriculture/rollback_drill

Rollback-drill test lane for the KFM Agriculture domain.

## Status

Draft. This file was expanded from an empty placeholder on 2026-07-05.

## Purpose

This directory is for tests that prove Agriculture release-facing outputs have a viable rollback path before they are treated as release-ready or public-facing.

A rollback drill test does not perform a real rollback and does not approve release. It proves that the records, pointers, manifests, receipts, catalog state, and correction path needed for rollback are present, coherent, and testable.

## Evidence basis

Current-session evidence supports these boundaries:

- `tests/` is the canonical enforceability-proof root.
- `tests/domains/agriculture/` exists but is still a greenfield stub.
- Agriculture file-system docs place agriculture tests under `tests/domains/agriculture/` as the domain test segment.
- Agriculture no-network runbook docs identify rollback target shape, release-manifest shape, and deterministic fixture testing as part of the Agriculture trust spine.
- Agriculture sensitivity docs require release-facing Agriculture outputs to preserve aggregation, rights, policy, and review posture.

## Authority boundary

| Concern | Authority home | This lane |
|---|---|---|
| Agriculture rollback decision | `release/` | Tests only. |
| Agriculture release records | `release/` and accepted release lanes | Tests only. |
| Catalog, evidence, receipts, proofs | `data/` accepted lifecycle/proof/catalog lanes | References only. |
| Agriculture object meaning | `contracts/domains/agriculture/` | Tests only. |
| Machine shape | `schemas/contracts/v1/domains/agriculture/` | Tests only. |
| Policy rules | `policy/domains/agriculture/` or accepted policy lane | Tests only. |
| Fixtures | `fixtures/domains/agriculture/` or accepted fixture lane | References only unless test-scoped. |
| Validators | `tools/validators/` | Tests only. |

## Test responsibilities

Rollback-drill tests should verify that:

- release-facing Agriculture output has a rollback target;
- release manifest pointers are coherent and resolvable in test fixtures;
- catalog entries can be traced back to evidence and receipts;
- policy and sensitivity posture are preserved through rollback checks;
- correction paths are explicit where public output is tested;
- aggregate-only public products can be withdrawn or superseded without exposing more detail;
- rollback readiness is not inferred from catalog existence alone;
- missing rollback support blocks promotion or fails safely.

## Required negative cases

| Case | Expected posture |
|---|---|
| Release-facing record has no rollback target | fail closed |
| Rollback target points to the wrong lifecycle state | fail closed |
| Release manifest is missing or incomplete | fail closed |
| Evidence or receipt pointer cannot resolve | abstain or fail closed |
| Policy posture changes without a correction or rollback path | fail closed |
| Catalog entry is treated as rollback-ready only because it exists | test failure |
| Rollback drill requires live source access | test failure |

## What belongs here

- This README.
- Agriculture rollback-drill test modules.
- Tests for rollback target shape and resolvability.
- Tests for release-manifest linkage.
- Tests for catalog-to-evidence-to-receipt traceability.
- Tests for correction and supersession readiness.
- Test-only references to contracts, schemas, policy, fixtures, validators, data records, and release records.

## What does not belong here

- Agriculture implementation code.
- Contracts or schemas.
- Policy rules.
- Validator implementation.
- General fixture libraries or source data.
- Catalog, lifecycle, proof, receipt, or release records.
- Actual rollback decisions or publication approvals.
- Live source calls.
- Generated text treated as authority.

## Validation

```bash
find tests/domains/agriculture/rollback_drill -maxdepth 5 -type f | sort
find tests/domains/agriculture fixtures/domains/agriculture policy/domains/agriculture schemas/contracts/v1/domains/agriculture contracts/domains/agriculture tools/validators data release -maxdepth 5 -type f 2>/dev/null | sort
pytest tests/domains/agriculture/rollback_drill tests/policy tests/contracts || true
```

Replace `|| true` with fail-closed CI behavior once accepted agriculture rollback-drill test commands are confirmed.

## Open questions

| Question | Status |
|---|---|
| Which Agriculture rollback card or release manifest schema is canonical for tests? | NEEDS VERIFICATION |
| Which rollback fixtures are canonical for Agriculture release-facing outputs? | NEEDS VERIFICATION |
| Which validator path owns rollback-drill checks? | NEEDS VERIFICATION |
| Which CI workflow blocks promotion when rollback-drill tests fail? | NEEDS VERIFICATION |
