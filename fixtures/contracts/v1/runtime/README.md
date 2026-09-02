<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/runtime/readme
title: runtime contract fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): runtime steward; TODO(owner): API steward; TODO(owner): governed AI steward; TODO(owner): schema steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): evidence steward; TODO(owner): correction steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-06-30 expansion
updated: 2026-06-30
policy_label: public-review
related:
  - ai_receipt/README.md
  - decision_envelope/README.md
  - run_receipt/README.md
  - runtime_response_envelope/README.md
  - ../../../../schemas/contracts/v1/runtime/
  - ../../../../contracts/runtime/
  - ../../../../policy/runtime/
  - ../../../../tools/validators/
  - ../../../../tests/schemas/test_common_contracts.py
  - ../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, v1, runtime, schema-fixtures, valid-fixtures, invalid-fixtures, expected-error, json-schema, runtime-boundary, governed-api, governed-ai, receipts, trust-membrane, finite-outcomes, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/contracts/v1/runtime/README.md`."
  - "This directory groups runtime contract fixture families used by the common schema fixture harness."
  - "This README documents the currently README-covered runtime fixture families: `ai_receipt`, `decision_envelope`, `run_receipt`, and `runtime_response_envelope`."
  - "Additional runtime schemas may exist under `schemas/contracts/v1/runtime/`; fixture-family completeness requires a separate inventory and test run."
  - "No tests, validators, runtime/API implementations, policy checks, evidence resolution checks, receipt persistence checks, public-client tests, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Runtime contract fixtures

Fixture root for KFM runtime contract schemas under `fixtures/contracts/v1/runtime/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Family: runtime" src="https://img.shields.io/badge/family-runtime-blue">
  <img alt="Harness: schema fixtures" src="https://img.shields.io/badge/harness-schema__fixtures-informational">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/contracts/v1/runtime/README.md`  
**Fixture posture:** runtime JSON Schema fixture-family index  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/runtime/`  
**Quick links:** [Purpose](#purpose) · [Current README-covered families](#current-readme-covered-families) · [Harness behavior](#harness-behavior) · [Authority boundary](#authority-boundary) · [Coverage notes](#coverage-notes) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files under this root are schema fixtures. They are not runtime implementations, governed API responses, evidence records, EvidenceBundles, PolicyDecisions, DecisionEnvelopes, AIReceipts, RunReceipts, release approval, review approval, public-client permission, or publication authority.

---

## Purpose

This directory groups valid and invalid fixtures for KFM runtime contract schemas.

Runtime fixtures help prove that runtime contract shapes reject incomplete payloads and accept minimal well-formed examples. They support schema-level validation only. They do not prove runtime behavior, policy execution, evidence resolution, citation validation, release approval, publication safety, or public-client rendering correctness.

The common pattern is:

```text
fixtures/contracts/v1/runtime/<contract_name>/
  README.md
  valid/
    README.md
    valid_1.json
  invalid/
    README.md
    invalid_1.json
    invalid_1.expected_error.txt
```

---

## Current README-covered families

This table is an index of runtime fixture families with README coverage completed in this documentation pass sequence. It is not a claim that every runtime schema has complete fixture coverage.

| Fixture family | Parent README | Positive lane | Negative lane | Current negative case |
|---|---|---|---|---|
| `ai_receipt` | [`ai_receipt/README.md`](ai_receipt/README.md) | [`ai_receipt/valid/README.md`](ai_receipt/valid/README.md) | [`ai_receipt/invalid/README.md`](ai_receipt/invalid/README.md) | Missing required `id`. |
| `decision_envelope` | [`decision_envelope/README.md`](decision_envelope/README.md) | [`decision_envelope/valid/README.md`](decision_envelope/valid/README.md) | [`decision_envelope/invalid/README.md`](decision_envelope/invalid/README.md) | Missing required `decision_id`. |
| `run_receipt` | [`run_receipt/README.md`](run_receipt/README.md) | [`run_receipt/valid/README.md`](run_receipt/valid/README.md) | [`run_receipt/invalid/README.md`](run_receipt/invalid/README.md) | Missing required `run_id`. |
| `runtime_response_envelope` | [`runtime_response_envelope/README.md`](runtime_response_envelope/README.md) | [`runtime_response_envelope/valid/README.md`](runtime_response_envelope/valid/README.md) | [`runtime_response_envelope/invalid/README.md`](runtime_response_envelope/invalid/README.md) | Missing required `id`. |

### Runtime fixture roles

| Family | Runtime role | Fixture boundary |
|---|---|---|
| `ai_receipt` | Accountability receipt for an AI-mediated runtime step. | Fixture shape only; not model truth, chain-of-thought, evidence, or publication authority. |
| `decision_envelope` | Finite runtime decision posture with policy family, reasons, obligations, and evaluation time. | Fixture shape only; not executable policy, promotion, release, or public answer. |
| `run_receipt` | Accountable summary of a governed runtime or pipeline stage execution. | Fixture shape only; not executed code, validation proof, evidence truth, or public-client permission. |
| `runtime_response_envelope` | Governed API/client-facing runtime response boundary. | Fixture shape only; not raw evidence storage, canonical storage, policy execution, model truth, or release approval. |

---

## Harness behavior

The common schema test harness includes `runtime` in its fixture families and discovers schemas from:

```text
schemas/contracts/v1/runtime/*.schema.json
```

For each schema with a matching fixture directory, it looks under:

```text
fixtures/contracts/v1/runtime/<schema_name>/
```

Observed harness expectations:

| Fixture pattern | Expected result |
|---|---|
| `valid/valid_*.json` | no JSON Schema errors |
| `invalid/invalid_*.json` | at least one JSON Schema error |
| `invalid/invalid_*.expected_error.txt` | expected text appears in combined schema error messages |

This root README documents expected harness behavior only. It does not claim that pytest, CI, validators, runtime/API implementations, policy rules, evidence-ref resolution, citation validation, receipt persistence, correction handling, or public-client rendering checks were run during this update.

---

## Authority boundary

| Responsibility | Home | Runtime fixture-root posture |
|---|---|---|
| Runtime fixture examples | `fixtures/contracts/v1/runtime/` | CONFIRMED root for examples documented here. |
| Machine-checkable runtime schema shape | `schemas/contracts/v1/runtime/` | Authoritative for JSON Schema shape. |
| Runtime semantic contracts | `contracts/runtime/` | Authoritative for contract meaning. |
| Runtime policy | `policy/runtime/` | Out of scope for fixtures. |
| Validators | `tools/validators/` | Declared by schemas; implementation/wiring must be verified separately. |
| Schema fixture harness | `tests/schemas/test_common_contracts.py` | CONFIRMED discovery pattern / NOT RUN. |
| Runtime/API implementation | implementation/API roots | Out of scope for fixtures. |
| Evidence, release, review, correction, receipt persistence | owning contract/policy/release/runtime roots | Out of scope for this README. |

Do not collapse this fixture root into runtime implementation, executable policy, semantic contracts, JSON Schemas, EvidenceBundles, source descriptors, validation reports, release manifests, review records, correction records, or public-client permission.

---

## Coverage notes

The README-covered fixture families listed above are confirmed by this documentation pass sequence, but the runtime schema namespace may contain additional schemas. A later coverage pass should compare:

```text
schemas/contracts/v1/runtime/*.schema.json
```

against:

```text
fixtures/contracts/v1/runtime/*/
```

and classify each schema as:

- fixture family present with valid and invalid lanes;
- fixture family present but incomplete;
- schema present with no fixture directory;
- fixture directory present with no matching schema;
- README present but stale against schema;
- expected-error matcher too broad for stable validator output.

Until that inventory and tests are run, root-level runtime fixture completeness remains **NEEDS VERIFICATION**.

---

## Maintenance checklist

Before changing this root or adding runtime fixture families:

- [ ] Confirm the paired schema exists under `schemas/contracts/v1/runtime/`.
- [ ] Confirm the paired contract exists under `contracts/runtime/`.
- [ ] Confirm the schema's `x-kfm.fixtures_root` points to the intended fixture directory.
- [ ] Keep passing examples under `<family>/valid/valid_<n>.json`.
- [ ] Keep failing examples under `<family>/invalid/invalid_<n>.json`.
- [ ] Keep expected-error text beside each invalid fixture it describes.
- [ ] Keep fixture cases small, deterministic, public-safe, and reviewable.
- [ ] Keep at least one minimal positive fixture and one missing-required-field invalid fixture for each active family.
- [ ] Add enum, pattern, date-time, digest, additional-property, and referenced-schema failures when coverage expands.
- [ ] Avoid private, unpublished, source-system, prompt-like, or policy-restricted content.
- [ ] Do not embed raw evidence payloads, protected location detail, credentials, private model internals, or release-blocked material in fixtures.
- [ ] Update parent and lane READMEs when schema fields, required lists, enum values, digest patterns, referenced schemas, or fixture coverage changes.
- [ ] Run the common schema fixture test before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Runtime fixture root | CONFIRMED | This README documents `fixtures/contracts/v1/runtime/`. |
| README-covered families | CONFIRMED PARTIAL | `ai_receipt`, `decision_envelope`, `run_receipt`, and `runtime_response_envelope` have parent and lane README coverage from this pass sequence. |
| Runtime schema namespace | NEEDS VERIFICATION | Additional runtime schemas may exist and require a separate schema-to-fixture inventory. |
| Validator wiring | NEEDS VERIFICATION | Schema-declared validator files were not all inspected or run during this root README update. |
| Test execution | NOT RUN | No validators, pytest, runtime/API tests, policy tests, evidence-ref checks, correction checks, public-client tests, receipt persistence checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define runtime fixture-root guidance. |
| [`ai_receipt/README.md`](ai_receipt/README.md) | CONFIRMED | README-covered AI receipt fixture family. | Does not prove tests were run. |
| [`decision_envelope/README.md`](decision_envelope/README.md) | CONFIRMED | README-covered decision envelope fixture family. | Does not prove tests were run. |
| [`run_receipt/README.md`](run_receipt/README.md) | CONFIRMED | README-covered run receipt fixture family. | Does not prove tests were run. |
| [`runtime_response_envelope/README.md`](runtime_response_envelope/README.md) | CONFIRMED | README-covered runtime response envelope fixture family. | Does not prove tests were run. |
| [`../../../../schemas/contracts/v1/runtime/`](../../../../schemas/contracts/v1/runtime/) | CONFIRMED AS SCHEMA ROOT / PARTIAL INVENTORY | Runtime schema namespace. | Full schema-to-fixture completeness was not checked in this update. |
| [`../../../../contracts/runtime/`](../../../../contracts/runtime/) | CONFIRMED AS CONTRACT ROOT / PARTIAL INVENTORY | Runtime semantic contract namespace. | Contract-to-schema completeness was not checked in this update. |
| [`../../../../tests/schemas/test_common_contracts.py`](../../../../tests/schemas/test_common_contracts.py) | CONFIRMED / NOT RUN | Common schema fixture discovery and valid/invalid fixture behavior. | Tests were not run during this update. |
| [`../../../../docs/doctrine/directory-rules.md`](../../../../docs/doctrine/directory-rules.md) | CONFIRMED | `fixtures/` is the root for golden, valid, and invalid test inputs; contracts/schemas/policy split remains separate. | Specific fixture completeness requires inventory and tests. |

[Back to top](#top)
