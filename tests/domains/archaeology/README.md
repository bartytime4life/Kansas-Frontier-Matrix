# tests/domains/archaeology

Parent test lane for the KFM Archaeology domain.

## Status

Draft. This file replaces the greenfield stub on 2026-07-05.

## Purpose

`tests/domains/archaeology/` is the Archaeology domain segment inside the canonical `tests/` responsibility root.

This directory is for enforceability proof: fixture safety, source admission, schema behavior, policy behavior, candidate-vs-confirmed posture, evidence closure, review gating, release readiness, rollback readiness, and public-safe transformation checks for Archaeology.

It is not Archaeology implementation, fixture authority, schema authority, policy authority, lifecycle storage, catalog storage, source registry authority, release authority, or public-client authority.

## Evidence basis

Current-session evidence supports these boundaries:

- `tests/domains/archaeology/README.md` existed as a greenfield stub before this update.
- `tests/domains/archaeology/fixtures/README.md` exists and defines the fixture-test parent lane.
- `tests/domains/archaeology/fixtures/source_admission/README.md` exists as a child fixture-test lane.
- Archaeology file-system docs place domain tests under `tests/domains/archaeology/` and domain fixtures under `fixtures/domains/archaeology/`.
- Archaeology file-system docs place contracts, schemas, policy, lifecycle data, registry records, release decisions, and connectors in separate responsibility roots.
- Archaeology sensitivity docs describe the lane as deny-by-default and review-gated for protected details.

## Authority boundary

| Concern | Authority home | This lane |
|---|---|---|
| Archaeology tests | `tests/domains/archaeology/` | Owns test organization and proof expectations. |
| Archaeology fixtures | `fixtures/domains/archaeology/` or accepted fixture lane | Referenced here; not duplicated without a fixture rule. |
| Archaeology object meaning | `contracts/domains/archaeology/` | Tested here; not defined here. |
| Archaeology machine shape | `schemas/contracts/v1/domains/archaeology/` | Tested here; not authored here. |
| Archaeology policy rules | `policy/domains/archaeology/` or accepted policy lane | Tested here; not defined here. |
| Validator implementation | `tools/validators/` | Tested here; not implemented here. |
| Archaeology pipelines | `pipelines/domains/archaeology/` and `pipeline_specs/archaeology/` | Tested here; not implemented here. |
| Lifecycle, catalog, evidence, receipts, proofs | `data/` accepted lifecycle/proof/catalog lanes | Referenced here; not stored here. |
| Source registry and source descriptors | accepted source registry roots | Referenced here; not authored here. |
| Release and rollback decisions | `release/` | Tested here; not decided here. |

## Current child lanes

| Lane | Purpose | Status |
|---|---|---|
| `fixtures/` | Parent lane for archaeology fixture-safety tests. | README confirmed; implementation NEEDS VERIFICATION. |
| `fixtures/source_admission/` | Tests source-admission fixture safety and bounded use. | README confirmed; implementation NEEDS VERIFICATION. |

## Test responsibilities

Archaeology domain tests should verify that:

- fixture inputs are synthetic, test-scoped, and clearly marked;
- source identity, review posture, sensitivity posture, and source role are explicit where required;
- candidate-vs-confirmed posture is preserved;
- accepted schemas, contracts, policy, and validators are not bypassed;
- evidence and citation support resolves before answer-like output is accepted;
- denied, unsupported, or ambiguous cases fail safely;
- release-facing outputs have review and rollback posture;
- no default test requires live source access;
- generated text, model output, or convenience summaries never become authority.

## What belongs here

- This README.
- Archaeology domain test modules.
- Child-lane README files and test indexes.
- Deterministic no-network test cases.
- Test-only references to schemas, contracts, policy, fixtures, validators, data records, source records, release records, and governed API/UI expectations.

## What does not belong here

- Archaeology implementation code.
- Canonical fixture libraries or large fixture payloads.
- Canonical contracts or schemas.
- Policy rules.
- Validator implementation.
- Source registry records.
- Lifecycle, catalog, proof, receipt, published, release, correction, or rollback records.
- Live source calls in the default suite.
- Generated text treated as authority.

## Validation

```bash
find tests/domains/archaeology -maxdepth 5 -type f | sort
find fixtures/domains/archaeology schemas/contracts/v1/domains/archaeology contracts/domains/archaeology policy/domains/archaeology tools/validators data release -maxdepth 5 -type f 2>/dev/null | sort
pytest tests/domains/archaeology tests/policy tests/contracts tests/schemas || true
```

Replace `|| true` with fail-closed CI behavior once accepted Archaeology test commands are confirmed.

## Open questions

| Question | Status |
|---|---|
| Which Archaeology child lanes have actual test modules beyond README files? | NEEDS VERIFICATION |
| Which Archaeology fixtures are canonical for each child lane? | NEEDS VERIFICATION |
| Which validator paths own Archaeology test behavior? | NEEDS VERIFICATION |
| Which CI workflow blocks promotion when Archaeology domain tests fail? | NEEDS VERIFICATION |
| Should additional child lanes exist for schema, policy-deny, catalog closure, and rollback drills? | NEEDS VERIFICATION |
