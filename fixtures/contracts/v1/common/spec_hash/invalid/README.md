<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/common/spec-hash/invalid/readme
title: spec_hash invalid fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): schema steward; TODO(owner): common contracts steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-06-30 expansion
updated: 2026-06-30
policy_label: public-review
related: [../README.md, ../valid/valid_1.json, invalid_1.json, invalid_1.expected_error.txt, ../../../../../../schemas/contracts/v1/common/spec_hash.schema.json, ../../../../../../contracts/common/spec_hash.md, ../../../../../../tools/validators/validate_spec_hash.py, ../../../../../../tests/schemas/test_common_contracts.py]
tags: [kfm, fixtures, contracts, v1, common, spec-hash, invalid-fixtures, json-schema, expected-error, negative-tests, non-authoritative]
notes: ["This README replaces a blank file at `fixtures/contracts/v1/common/spec_hash/invalid/README.md`.", "Invalid fixtures are intentionally failing inputs for schema enforcement; they are not schema authority, contract authority, policy authority, proof authority, release authority, or production data.", "The active schema evidence for this lane is `schemas/contracts/v1/common/spec_hash.schema.json`; the fixture root is declared in that schema's `x-kfm.fixtures_root`.", "The dedicated `tools/validators/validate_spec_hash.py` file exists but is a greenfield placeholder; current fixture behavior is documented from `tests/schemas/test_common_contracts.py` and the JSON Schema shape."]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `spec_hash` invalid fixtures

Intentional negative fixtures for the KFM `spec_hash` common contract.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Contract family: common" src="https://img.shields.io/badge/family-common-blue">
  <img alt="Contract: spec_hash" src="https://img.shields.io/badge/contract-spec__hash-purple">
  <img alt="Fixture kind: invalid" src="https://img.shields.io/badge/fixture-invalid-critical">
</p>

**Path:** `fixtures/contracts/v1/common/spec_hash/invalid/README.md`  
**Fixture posture:** negative JSON Schema fixture lane  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/common/spec_hash.schema.json`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Schema basis](#schema-basis) · [Test harness behavior](#test-harness-behavior) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Validation checklist](#validation-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are expected to fail validation. They are not production spec hashes, source data, proof records, receipts, policy decisions, release decisions, or contract/schema authority.

---

## Purpose

This directory holds invalid JSON fixtures for the `spec_hash` common contract.

Use this lane to verify that the schema rejects malformed or incomplete `spec_hash` objects. Each invalid fixture should pair with an optional `.expected_error.txt` file when the test harness should assert a specific error message fragment.

---

## Current inventory

| Fixture | Invalid because | Expected error |
|---|---|---|
| [`invalid_1.json`](invalid_1.json) | The object is `{}` and omits required property `value`. | [`invalid_1.expected_error.txt`](invalid_1.expected_error.txt): `'value' is a required property` |

---

## Schema basis

The current schema evidence for this fixture lane is:

```text
schemas/contracts/v1/common/spec_hash.schema.json
```

Relevant shape:

| Field | Requirement |
|---|---|
| Root type | object |
| Required property | `value` |
| `value` type | string |
| `value` pattern | `^sha256:[a-f0-9]{64}$` |
| Additional properties | false |
| Schema-declared fixtures root | `fixtures/contracts/v1/common/spec_hash/` |
| Dedicated validator path | `tools/validators/validate_spec_hash.py` |
| Dedicated validator maturity | `NEEDS VERIFICATION` — current file is a greenfield placeholder. |

---

## Test harness behavior

`tests/schemas/test_common_contracts.py` discovers schema fixture families under:

```text
fixtures/contracts/v1/<family>/<name>/
```

For each invalid fixture matching `invalid/invalid_*.json`, the test harness expects JSON Schema validation errors. When a sibling `.expected_error.txt` file exists, the harness lowercases the expected text and checks that each expected non-empty line appears in the combined JSON Schema error messages.

For this directory, `invalid_1.expected_error.txt` is intentionally specific:

```text
'value' is a required property
```

That expected line corresponds to `invalid_1.json` omitting the schema-required `value` field.

---

## Accepted material

| Accepted item | Purpose |
|---|---|
| `invalid_*.json` | JSON instances expected to fail `spec_hash` schema validation. |
| `invalid_*.expected_error.txt` | Optional expected error fragment for the matching invalid JSON fixture. |
| `README.md` | Local fixture boundary and inventory. |

---

## Exclusions

| Do not place here | Correct home |
|---|---|
| Valid `spec_hash` examples | `../valid/` |
| Parent contract fixture guidance | `../README.md` |
| JSON Schema authority | `../../../../../../schemas/contracts/v1/common/spec_hash.schema.json` |
| Semantic contract documentation | `../../../../../../contracts/common/spec_hash.md` |
| Validator implementation | `../../../../../../tools/validators/validate_spec_hash.py` or accepted validator root |
| Policy rules | `../../../../../../policy/common/` |
| Runtime receipts, proofs, release records, source data, or published artifacts | Their canonical KFM roots, not fixtures |

---

## Validation checklist

Before adding or changing invalid fixtures here:

- [ ] The fixture file name follows `invalid_<n>.json`.
- [ ] The fixture is intentionally invalid under `spec_hash.schema.json`.
- [ ] The failure reason is narrow and easy to understand.
- [ ] The expected error file, when present, matches the JSON Schema error text closely enough for `tests/schemas/test_common_contracts.py`.
- [ ] The fixture does not redefine the schema, contract, policy, or validator.
- [ ] The fixture does not contain production hashes, secrets, source data, receipts, proofs, release records, or published artifacts.
- [ ] New invalid cases are paired with a matching valid case only when that improves coverage and does not blur fixture purpose.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target path presence | CONFIRMED | `fixtures/contracts/v1/common/spec_hash/invalid/README.md` existed as a blank file before this update. |
| Invalid fixture inventory | CONFIRMED | `invalid_1.json` exists and contains `{}`. |
| Expected error inventory | CONFIRMED | `invalid_1.expected_error.txt` exists and contains `'value' is a required property`. |
| Valid sibling example | CONFIRMED | `../valid/valid_1.json` contains a `sha256:` value with 64 lowercase hex characters. |
| Schema authority | CONFIRMED | `schemas/contracts/v1/common/spec_hash.schema.json` defines the required `value` property and pattern. |
| Dedicated validator implementation | NEEDS VERIFICATION | `tools/validators/validate_spec_hash.py` is present but currently a greenfield placeholder. |
| Test harness behavior | CONFIRMED | `tests/schemas/test_common_contracts.py` validates invalid fixtures and expected error text. |
| Runtime validation results | NOT RUN | This README update did not run tests. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define fixture boundaries or inventory. |
| [`invalid_1.json`](invalid_1.json) | CONFIRMED | Invalid fixture omits required `value`. | Only one invalid case is currently verified. |
| [`invalid_1.expected_error.txt`](invalid_1.expected_error.txt) | CONFIRMED | Expected error asserts missing required `value`. | Depends on JSON Schema error wording remaining compatible with the test harness. |
| [`../valid/valid_1.json`](../valid/valid_1.json) | CONFIRMED | Shows the positive fixture shape for comparison. | Does not prove all valid cases are covered. |
| [`../../../../../../schemas/contracts/v1/common/spec_hash.schema.json`](../../../../../../schemas/contracts/v1/common/spec_hash.schema.json) | CONFIRMED | Schema shape, required field, pattern, additionalProperties rule, and declared fixtures root. | Schema status is `PROPOSED` in `x-kfm`. |
| [`../../../../../../tools/validators/validate_spec_hash.py`](../../../../../../tools/validators/validate_spec_hash.py) | CONFIRMED | Dedicated validator path exists. | File is a greenfield placeholder, not implemented validator behavior. |
| [`../../../../../../tests/schemas/test_common_contracts.py`](../../../../../../tests/schemas/test_common_contracts.py) | CONFIRMED | Test harness discovery and expected-error matching behavior. | Tests were not run during this README update. |

[Back to top](#top)
