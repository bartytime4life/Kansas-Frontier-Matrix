<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-validators-readme
title: Validator Tests README
type: test-readme
version: v0.1
status: draft; greenfield-stub-replaced; validator-test-lane; PROPOSED / NEEDS VERIFICATION
owners:
  - OWNER_TBD - Test steward
  - OWNER_TBD - Validation steward
  - OWNER_TBD - Schema steward
  - OWNER_TBD - Contract steward
  - OWNER_TBD - Policy steward
created: 2026-07-07
updated: 2026-07-07
policy_label: public-doc; tests; validators; validation; no-network; synthetic-only; fail-closed
tags: [kfm, tests, validators, validation, schema, contracts, fixtures, fail-closed, NEEDS_VERIFICATION]
related:
  - ../README.md
  - ../fixtures/README.md
  - ../schemas/README.md
  - ../../tools/validators/
  - ../../pipelines/validate/README.md
  - ../../schemas/
  - ../../contracts/
  - ../../policy/
  - ../../release/
notes:
  - "This README replaces the greenfield stub at tests/validators/README.md."
  - "This lane documents executable validator unit tests, not validator implementation or authority records."
  - "Validator tests should prove validation behavior and fail-closed boundaries without turning validation success into truth, evidence closure, or release approval."
  - "Validator inventory, executable tests, fixtures, runner, CI, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Validator tests

> Test-lane README for validator unit tests under `tests/validators/`. This lane proves validator behavior, accepted/rejected cases, and boundary checks without becoming validator implementation, schema authority, contract authority, policy authority, release authority, or fixture storage.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: validator tests" src="https://img.shields.io/badge/lane-validator__tests-purple">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
</p>

**Path:** `tests/validators/README.md`  
**Status:** draft / greenfield stub replaced / validator test lane / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Lane family:** `validators`  
**Implementation companion:** `tools/validators/` or accepted validator/tool roots  
**Default posture:** deterministic, synthetic, no-network, fail-closed validator tests only  
**Truth posture:** CONFIRMED target file existed as a greenfield stub before replacement; CONFIRMED `tests/README.md` lists `tests/validators/` as validator unit tests; CONFIRMED validation appears in the trust-spine flow; CONFIRMED `pipelines/validate/README.md` separates validation logic from schemas, contracts, policy, data, proof, and release authority; NEEDS VERIFICATION for validator inventory, executable tests, fixture use, runner, CI, and pass rates.

---

## Scope

In scope:

- unit tests for validators and validation helpers;
- valid and invalid fixture-driven validation checks;
- schema wrapper and contract conformance checks;
- source descriptor, lifecycle, evidence-reference, policy-input, receipt, proof, and release-preflight validator checks;
- reason-code, error-message, and fail-closed behavior checks.

Out of scope:

- validator implementation code;
- schema, contract, policy, release, evidence, proof, receipt, lifecycle, or fixture authority;
- generated validation reports as authority records;
- production records or public artifacts.

---

## Repo fit

| Responsibility | Correct home | Relationship |
|---|---|---|
| Validator unit tests | `tests/validators/` | This lane. |
| Validator implementation | `tools/validators/` or accepted tool/package roots | Code under test; not owned here. |
| Pipeline validation helpers | `pipelines/validate/` | Executable pipeline logic; tests may verify behavior. |
| Schema tests | `tests/schemas/` | Machine-shape test lane. |
| Unit-test fixtures | `tests/fixtures/` | Test-local inputs. |
| Shared fixtures | `fixtures/` | Reusable synthetic examples. |
| Schemas and contracts | `schemas/`, `contracts/` | Shape and meaning authority. |
| Policy and release | `policy/`, `release/` | Gate and publication authority. |

> [!IMPORTANT]
> `tests/validators/` must not become validator implementation, a schema mirror, a contract mirror, a policy lane, a release lane, fixture storage, validation-report storage, lifecycle data, proof storage, or public artifact storage.

---

## Validator-test rule

Validator tests prove that validators accept supported inputs, reject unsupported inputs, preserve useful diagnostics, and fail closed. A validation pass is not evidence closure, catalog truth, policy approval, release approval, or publication.

| Expectation | Required posture |
|---|---|
| Unit-scoped | Test one validator or helper behavior clearly. |
| Fixture-backed | Use synthetic valid and invalid fixtures where practical. |
| No-network default | Use local fixtures and local authority files only. |
| Fail closed | Missing schemas, unresolved refs, malformed payloads, unsupported versions, and boundary gaps fail visibly. |
| Boundary safe | Validator success does not skip evidence, policy, release, correction, rollback, or runtime gates. |

---

## Expected test families

| Family | What it proves |
|---|---|
| `schema_validator_valid` | Valid fixture passes schema wrapper. |
| `schema_validator_invalid` | Invalid fixture fails with bounded diagnostics. |
| `contract_validator_valid` | Object meaning and lifecycle role align with contract expectations. |
| `source_descriptor_validator` | Source descriptor requirements are checked. |
| `evidence_ref_validator` | EvidenceRef readiness checks do not fabricate support. |
| `policy_input_validator` | Policy-facing payloads carry required fields before policy execution. |
| `release_manifest_validator` | Release preflight checks required refs. |
| `receipt_or_proof_validator` | Receipt/proof preflight matches declared run or integrity posture. |
| `lifecycle_transition_validator` | Phase skips and public pre-release reads are rejected. |
| `reason_codes_stable` | Diagnostic reason codes remain stable and reviewable. |

---

## Suggested layout

```text
tests/validators/
|-- README.md
|-- schema_validator_valid.test.PROPOSED
|-- schema_validator_invalid.test.PROPOSED
|-- contract_validator_valid.test.PROPOSED
|-- source_descriptor_validator.test.PROPOSED
|-- evidence_ref_validator.test.PROPOSED
|-- policy_input_validator.test.PROPOSED
|-- release_manifest_validator.test.PROPOSED
|-- receipt_or_proof_validator.test.PROPOSED
|-- lifecycle_transition_validator.test.PROPOSED
`-- reason_codes_stable.test.PROPOSED
```

Actual filenames, runner, framework, validator inventory, and CI wiring remain NEEDS VERIFICATION.

---

## Run posture

No executable runner was verified while authoring this README.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/validators
```

---

## Maintenance checklist

- [ ] Keep validator implementation outside `tests/validators/`.
- [ ] Keep fixtures in `tests/fixtures/` or `fixtures/` and reference them from tests.
- [ ] Pair accepted and rejected cases where material.
- [ ] Assert validation passes do not equal evidence closure, policy approval, release approval, catalog truth, or publication.
- [ ] Link tests to validators, schemas, contracts, fixtures, policies, release gates, receipts, and proofs after verification.

---

## Verification status

| Item | Status |
|---|---|
| Target README path | CONFIRMED; greenfield stub replaced. |
| `tests/validators/` placement | CONFIRMED in `tests/README.md` as validator unit tests. |
| Trust-spine validation gate | CONFIRMED in `tests/README.md`. |
| Validation pipeline boundary | CONFIRMED in `pipelines/validate/README.md`. |
| Validator implementation inventory | NEEDS VERIFICATION. |
| Executable test inventory | NEEDS VERIFICATION. |
| Fixture inventory | NEEDS VERIFICATION. |
| Runner and CI | NEEDS VERIFICATION. |
| Tests and validators | NOT RUN. |
