# tests/domains/agriculture

Parent test lane for the KFM Agriculture domain.

## Status

Draft. This file replaces the greenfield stub on 2026-07-05.

## Purpose

`tests/domains/agriculture/` is the Agriculture domain segment inside the canonical `tests/` responsibility root.

This directory is for enforceability proof: schema behavior, policy behavior, aggregation boundaries, evidence and catalog closure, rollback readiness, source-role preservation, and public-safe context handling for Agriculture.

It is not Agriculture implementation, schema authority, policy authority, fixture authority, lifecycle storage, release authority, source registry authority, or public-client authority.

## Evidence basis

Current-session evidence supports these boundaries:

- `tests/` is the canonical enforceability-proof root.
- Agriculture file-system docs place Agriculture tests under `tests/domains/agriculture/` as the domain test segment.
- Agriculture schemas, contracts, policy, fixtures, pipelines, data lifecycle, source registry, and release lanes remain separate responsibility roots.
- The child Agriculture test lanes listed below exist as README-backed lanes, but direct test modules and CI execution are still NEEDS VERIFICATION.

## Authority boundary

| Concern | Authority home | This lane |
|---|---|---|
| Agriculture tests | `tests/domains/agriculture/` | Owns test organization and proof expectations. |
| Agriculture object meaning | `contracts/domains/agriculture/` | Tested here; not defined here. |
| Agriculture machine shape | `schemas/contracts/v1/domains/agriculture/` | Tested here; not authored here. |
| Agriculture policy rules | `policy/domains/agriculture/` or accepted policy lane | Tested here; not defined here. |
| Agriculture fixtures | `fixtures/domains/agriculture/` or accepted fixture lane | Referenced here; not duplicated without a fixture rule. |
| Validator implementation | `tools/validators/` | Tested here; not implemented here. |
| Agriculture pipelines | `pipelines/domains/agriculture/` and `pipeline_specs/agriculture/` | Tested here; not implemented here. |
| Lifecycle, catalog, evidence, receipts, proofs | `data/` accepted lifecycle/proof/catalog lanes | Referenced here; not stored here. |
| Source registry and source descriptors | accepted source registry roots | Referenced here; not authored here. |
| Release and rollback decisions | `release/` | Tested here; not decided here. |

## Current child lanes

| Lane | Purpose | Status |
|---|---|---|
| `aggregate_only/` | Aggregate-only public-safe Agriculture tests. | README confirmed; implementation NEEDS VERIFICATION. |
| `catalog_closure/` | Catalog closure against evidence, receipts, policy, release, and rollback posture. | README confirmed; implementation NEEDS VERIFICATION. |
| `policy_deny/` | Deny, abstain, and fail-closed Agriculture policy behavior. | README confirmed; implementation NEEDS VERIFICATION. |
| `rollback_drill/` | Rollback-readiness proof without making rollback decisions. | README confirmed; implementation NEEDS VERIFICATION. |
| `schema/` | Agriculture schema-conformance tests. | README confirmed; implementation NEEDS VERIFICATION. |
| `soil_moisture/` | Soil-moisture context tests with Soil and Hydrology ownership preserved. | README confirmed; implementation NEEDS VERIFICATION. |
| `ssurgo_lineage/` | SSURGO lineage and source-role tests for Agriculture use of Soil context. | README confirmed; implementation NEEDS VERIFICATION. |
| `veg_index/` | Vegetation-index context tests. | README confirmed; implementation NEEDS VERIFICATION. |

## Test responsibilities

Agriculture domain tests should verify that:

- valid Agriculture fixtures satisfy accepted schemas and contracts;
- invalid Agriculture fixtures fail for expected reasons;
- source roles are preserved across fixtures, validators, catalog helpers, and public-surface helpers;
- aggregate outputs stay aggregate;
- evidence and citation support resolves before answer-like output is accepted;
- policy deny, abstain, and fail-closed behavior blocks unsafe use;
- catalog records do not imply publication by existence alone;
- release-facing outputs have rollback posture;
- no default test requires live source access;
- generated text, model output, or convenience summaries never become authority.

## What belongs here

- This README.
- Agriculture domain test modules.
- Child-lane README files and test indexes.
- Deterministic no-network test cases.
- Test-only references to schemas, contracts, policy, fixtures, validators, data records, source records, release records, and governed API/UI expectations.

## What does not belong here

- Agriculture implementation code.
- Canonical contracts or schemas.
- Policy rules.
- Validator implementation.
- General fixture libraries or source data.
- Source registry records.
- Lifecycle, catalog, proof, receipt, published, release, correction, or rollback records.
- Live source calls in the default suite.
- Generated text treated as authority.

## Validation

```bash
find tests/domains/agriculture -maxdepth 5 -type f | sort
find fixtures/domains/agriculture schemas/contracts/v1/domains/agriculture contracts/domains/agriculture policy/domains/agriculture tools/validators data release -maxdepth 5 -type f 2>/dev/null | sort
pytest tests/domains/agriculture tests/policy tests/contracts tests/schemas || true
```

Replace `|| true` with fail-closed CI behavior once accepted Agriculture test commands are confirmed.

## Open questions

| Question | Status |
|---|---|
| Which Agriculture child lanes have actual test modules beyond README files? | NEEDS VERIFICATION |
| Which Agriculture fixtures are canonical for each child lane? | NEEDS VERIFICATION |
| Which validator paths own Agriculture test behavior? | NEEDS VERIFICATION |
| Which CI workflow blocks promotion when Agriculture domain tests fail? | NEEDS VERIFICATION |
| Should this parent README be mirrored in a higher-level `tests/domains/README.md` index? | NEEDS VERIFICATION |
