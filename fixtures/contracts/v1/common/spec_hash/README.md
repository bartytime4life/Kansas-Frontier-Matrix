<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/common/spec-hash/readme
title: spec_hash fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): schema steward; TODO(owner): common contracts steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-06-30 expansion
updated: 2026-06-30
policy_label: public-review
related: [valid/README.md, valid/valid_1.json, invalid/README.md, invalid/invalid_1.json, invalid/invalid_1.expected_error.txt, ../../../../../schemas/contracts/v1/common/spec_hash.schema.json, ../../../../../contracts/common/spec_hash.md, ../../../../../tools/validators/validate_spec_hash.py, ../../../../../tests/schemas/test_common_contracts.py]
tags: [kfm, fixtures, contracts, v1, common, spec-hash, json-schema, valid-fixtures, invalid-fixtures, expected-error, positive-tests, negative-tests, non-authoritative]
notes: ["This README replaces a blank file at `fixtures/contracts/v1/common/spec_hash/README.md`.", "This directory is the schema-declared fixture root for `spec_hash`; fixture placement does not make fixture content schema authority, contract authority, policy authority, proof authority, release authority, or production data.", "The active schema evidence for this fixture family is `schemas/contracts/v1/common/spec_hash.schema.json`, whose `x-kfm.fixtures_root` points here.", "The dedicated `tools/validators/validate_spec_hash.py` file exists but is a greenfield placeholder; current executable fixture behavior is documented from `tests/schemas/test_common_contracts.py` and JSON Schema validation."]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `spec_hash` fixtures

Fixture root for the KFM `spec_hash` common contract.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Contract family: common" src="https://img.shields.io/badge/family-common-blue">
  <img alt="Contract: spec_hash" src="https://img.shields.io/badge/contract-spec__hash-purple">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/contracts/v1/common/spec_hash/README.md`  
**Fixture posture:** JSON Schema valid/invalid fixture family  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/common/spec_hash.schema.json`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Schema basis](#schema-basis) · [Test harness behavior](#test-harness-behavior) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Validation checklist](#validation-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are contract fixtures. They are not production spec hashes, source data, proof records, receipts, policy decisions, release decisions, contract authority, or schema authority.

---

## Purpose

This directory holds positive and negative JSON fixtures for the `spec_hash` common contract.

Use this fixture family to verify that KFM's JSON Schema accepts valid `spec_hash` objects and rejects invalid ones. The schema-declared fixture root is:

```text
fixtures/contracts/v1/common/spec_hash/
```

The fixture family currently covers the minimal shape: an object with required property `value` containing a lowercase SHA-256 digest string in `sha256:<64 lowercase hex>` form.

---

## Current inventory

| Lane | File | Purpose | Status |
|---|---|---|---|
| [`valid/`](valid/README.md) | [`valid_1.json`](valid/valid_1.json) | Minimal valid object with `value` matching `^sha256:[a-f0-9]{64}$`. | CONFIRMED |
| [`invalid/`](invalid/README.md) | [`invalid_1.json`](invalid/invalid_1.json) | Minimal invalid object `{}` missing required `value`. | CONFIRMED |
| [`invalid/`](invalid/README.md) | [`invalid_1.expected_error.txt`](invalid/invalid_1.expected_error.txt) | Expected JSON Schema error: `'value' is a required property`. | CONFIRMED |

---

## Schema basis

The current schema evidence for this fixture family is:

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
| Contract doc path in schema metadata | `contracts/common/spec_hash.md` |
| Fixtures root in schema metadata | `fixtures/contracts/v1/common/spec_hash/` |
| Dedicated validator path in schema metadata | `tools/validators/validate_spec_hash.py` |
| Policy path in schema metadata | `policy/common/` |
| Schema status in metadata | `PROPOSED` |

---

## Test harness behavior

`tests/schemas/test_common_contracts.py` discovers schema fixture families under:

```text
fixtures/contracts/v1/<family>/<name>/
```

For this family:

- `valid/valid_*.json` files must produce no JSON Schema errors.
- `invalid/invalid_*.json` files must produce at least one JSON Schema error.
- `invalid/invalid_*.expected_error.txt` files, when present, provide expected error text that must appear in the combined validation error messages.

The dedicated validator path exists, but `tools/validators/validate_spec_hash.py` is currently a greenfield placeholder, so this README does not claim a working dedicated CLI validator.

---

## Accepted material

| Accepted item | Purpose |
|---|---|
| `valid/valid_*.json` | JSON instances expected to pass `spec_hash` schema validation. |
| `invalid/invalid_*.json` | JSON instances expected to fail `spec_hash` schema validation. |
| `invalid/invalid_*.expected_error.txt` | Optional expected error fragment for matching invalid JSON fixtures. |
| `README.md` files | Local fixture boundaries, inventories, and validation notes. |

---

## Exclusions

| Do not place here | Correct home |
|---|---|
| JSON Schema authority | `../../../../../schemas/contracts/v1/common/spec_hash.schema.json` |
| Semantic contract documentation | `../../../../../contracts/common/spec_hash.md` |
| Validator implementation | `../../../../../tools/validators/validate_spec_hash.py` or accepted validator root |
| Policy rules | `../../../../../policy/common/` |
| Production digests or real artifact hashes | Operational manifest, receipt, proof, or release roots as appropriate |
| Runtime receipts, proofs, release records, source data, or published artifacts | Their canonical KFM roots, not fixtures |

---

## Validation checklist

Before adding or changing fixtures here:

- [ ] Valid fixture file names follow `valid/valid_<n>.json`.
- [ ] Invalid fixture file names follow `invalid/invalid_<n>.json`.
- [ ] Valid fixtures contain `value` matching `^sha256:[a-f0-9]{64}$`.
- [ ] Invalid fixtures are intentionally invalid under `spec_hash.schema.json`.
- [ ] Expected error files are specific enough to catch the intended failure and stable enough for the schema test harness.
- [ ] Fixtures do not redefine the schema, contract, policy, or validator.
- [ ] Fixtures do not contain production hashes, secrets, source data, receipts, proofs, release records, or published artifacts.
- [ ] Any schema change is paired with fixture updates and test-harness review.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target path presence | CONFIRMED | `fixtures/contracts/v1/common/spec_hash/README.md` existed as a blank file before this update. |
| Valid fixture lane | CONFIRMED | `valid/README.md` and `valid/valid_1.json` exist. |
| Invalid fixture lane | CONFIRMED | `invalid/README.md`, `invalid/invalid_1.json`, and `invalid/invalid_1.expected_error.txt` exist. |
| Schema authority | CONFIRMED | `schemas/contracts/v1/common/spec_hash.schema.json` defines the required `value` property and pattern. |
| Dedicated validator implementation | NEEDS VERIFICATION | `tools/validators/validate_spec_hash.py` is present but currently a greenfield placeholder. |
| Test harness behavior | CONFIRMED | `tests/schemas/test_common_contracts.py` validates valid and invalid contract fixtures. |
| Runtime validation results | NOT RUN | This README update did not run tests. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define fixture-family boundaries or inventory. |
| [`valid/README.md`](valid/README.md) | CONFIRMED | Positive fixture lane contract and inventory. | Does not prove runtime validation was executed in this update. |
| [`valid/valid_1.json`](valid/valid_1.json) | CONFIRMED | Minimal valid `spec_hash` example. | Only one valid case is currently verified. |
| [`invalid/README.md`](invalid/README.md) | CONFIRMED | Negative fixture lane contract and inventory. | Does not prove runtime validation was executed in this update. |
| [`invalid/invalid_1.json`](invalid/invalid_1.json) | CONFIRMED | Minimal invalid case omitting `value`. | Only one invalid case is currently verified. |
| [`invalid/invalid_1.expected_error.txt`](invalid/invalid_1.expected_error.txt) | CONFIRMED | Expected error text for missing `value`. | Depends on JSON Schema error wording remaining compatible with the test harness. |
| [`../../../../../schemas/contracts/v1/common/spec_hash.schema.json`](../../../../../schemas/contracts/v1/common/spec_hash.schema.json) | CONFIRMED | Schema shape, required field, pattern, additionalProperties rule, and declared fixtures root. | Schema status is `PROPOSED` in `x-kfm`. |
| [`../../../../../tools/validators/validate_spec_hash.py`](../../../../../tools/validators/validate_spec_hash.py) | CONFIRMED | Dedicated validator path exists. | File is a greenfield placeholder, not implemented validator behavior. |
| [`../../../../../tests/schemas/test_common_contracts.py`](../../../../../tests/schemas/test_common_contracts.py) | CONFIRMED | Test harness discovery and fixture behavior. | Tests were not run during this README update. |

[Back to top](#top)
