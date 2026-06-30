<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/common/spec-hash/valid/readme
title: spec_hash valid fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): schema steward; TODO(owner): common contracts steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-06-30 expansion
updated: 2026-06-30
policy_label: public-review
related: [../README.md, valid_1.json, ../invalid/README.md, ../invalid/invalid_1.json, ../invalid/invalid_1.expected_error.txt, ../../../../../../schemas/contracts/v1/common/spec_hash.schema.json, ../../../../../../contracts/common/spec_hash.md, ../../../../../../tools/validators/validate_spec_hash.py, ../../../../../../tests/schemas/test_common_contracts.py]
tags: [kfm, fixtures, contracts, v1, common, spec-hash, valid-fixtures, json-schema, positive-tests, non-authoritative]
notes: ["This README replaces a blank file at `fixtures/contracts/v1/common/spec_hash/valid/README.md`.", "Valid fixtures are intentionally passing inputs for schema enforcement; they are not schema authority, contract authority, policy authority, proof authority, release authority, or production data.", "The active schema evidence for this lane is `schemas/contracts/v1/common/spec_hash.schema.json`; the fixture root is declared in that schema's `x-kfm.fixtures_root`.", "The dedicated `tools/validators/validate_spec_hash.py` file exists but is a greenfield placeholder; current fixture behavior is documented from `tests/schemas/test_common_contracts.py` and the JSON Schema shape."]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `spec_hash` valid fixtures

Intentional positive fixtures for the KFM `spec_hash` common contract.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Contract family: common" src="https://img.shields.io/badge/family-common-blue">
  <img alt="Contract: spec_hash" src="https://img.shields.io/badge/contract-spec__hash-purple">
  <img alt="Fixture kind: valid" src="https://img.shields.io/badge/fixture-valid-2ea44f">
</p>

**Path:** `fixtures/contracts/v1/common/spec_hash/valid/README.md`  
**Fixture posture:** positive JSON Schema fixture lane  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/common/spec_hash.schema.json`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Schema basis](#schema-basis) · [Test harness behavior](#test-harness-behavior) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Validation checklist](#validation-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are expected to pass validation. They are not production spec hashes, source data, proof records, receipts, policy decisions, release decisions, or contract/schema authority.

---

## Purpose

This directory holds valid JSON fixtures for the `spec_hash` common contract.

Use this lane to verify that the schema accepts the minimal valid `spec_hash` object shape: an object with a required `value` property containing a lowercase SHA-256 digest string in KFM's `sha256:<64 lowercase hex>` form.

---

## Current inventory

| Fixture | Valid because | Notes |
|---|---|---|
| [`valid_1.json`](valid_1.json) | Contains `value` with `sha256:` plus 64 lowercase `a` hex characters. | Minimal positive case for required field and pattern. |

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

For each valid fixture matching `valid/valid_*.json`, the test harness loads the matching schema and asserts that JSON Schema validation produces no errors.

For this directory, `valid_1.json` is intentionally minimal:

```json
{
  "value": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
}
```

---

## Accepted material

| Accepted item | Purpose |
|---|---|
| `valid_*.json` | JSON instances expected to pass `spec_hash` schema validation. |
| `README.md` | Local fixture boundary and inventory. |

---

## Exclusions

| Do not place here | Correct home |
|---|---|
| Invalid `spec_hash` examples | `../invalid/` |
| Expected error text files | `../invalid/` with matching invalid fixtures |
| Parent contract fixture guidance | `../README.md` |
| JSON Schema authority | `../../../../../../schemas/contracts/v1/common/spec_hash.schema.json` |
| Semantic contract documentation | `../../../../../../contracts/common/spec_hash.md` |
| Validator implementation | `../../../../../../tools/validators/validate_spec_hash.py` or accepted validator root |
| Policy rules | `../../../../../../policy/common/` |
| Runtime receipts, proofs, release records, source data, production hashes, or published artifacts | Their canonical KFM roots, not fixtures |

---

## Validation checklist

Before adding or changing valid fixtures here:

- [ ] The fixture file name follows `valid_<n>.json`.
- [ ] The fixture is intentionally valid under `spec_hash.schema.json`.
- [ ] The fixture contains a `value` property.
- [ ] The `value` field matches `^sha256:[a-f0-9]{64}$`.
- [ ] The fixture does not include additional properties unless the schema changes first.
- [ ] The fixture does not redefine the schema, contract, policy, or validator.
- [ ] The fixture does not contain production hashes, secrets, source data, receipts, proofs, release records, or published artifacts.
- [ ] New valid cases are paired with invalid cases only when that improves coverage and does not blur fixture purpose.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target path presence | CONFIRMED | `fixtures/contracts/v1/common/spec_hash/valid/README.md` existed as a blank file before this update. |
| Valid fixture inventory | CONFIRMED | `valid_1.json` exists and contains a minimal valid `value`. |
| Invalid sibling lane | CONFIRMED | `../invalid/README.md` documents the current invalid fixture and expected error. |
| Schema authority | CONFIRMED | `schemas/contracts/v1/common/spec_hash.schema.json` defines the required `value` property and pattern. |
| Dedicated validator implementation | NEEDS VERIFICATION | `tools/validators/validate_spec_hash.py` is present but currently a greenfield placeholder. |
| Test harness behavior | CONFIRMED | `tests/schemas/test_common_contracts.py` validates valid fixtures by asserting no schema errors. |
| Runtime validation results | NOT RUN | This README update did not run tests. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define fixture boundaries or inventory. |
| [`valid_1.json`](valid_1.json) | CONFIRMED | Shows the minimal positive fixture shape. | Only one valid case is currently verified. |
| [`../invalid/README.md`](../invalid/README.md) | CONFIRMED | Sibling invalid fixture documentation and schema/test boundary pattern. | Does not prove valid fixture behavior by itself. |
| [`../invalid/invalid_1.json`](../invalid/invalid_1.json) | CONFIRMED | Negative comparison case omits required `value`. | Belongs to invalid lane, not valid lane. |
| [`../../../../../../schemas/contracts/v1/common/spec_hash.schema.json`](../../../../../../schemas/contracts/v1/common/spec_hash.schema.json) | CONFIRMED | Schema shape, required field, pattern, additionalProperties rule, and declared fixtures root. | Schema status is `PROPOSED` in `x-kfm`. |
| [`../../../../../../tools/validators/validate_spec_hash.py`](../../../../../../tools/validators/validate_spec_hash.py) | CONFIRMED | Dedicated validator path exists. | File is a greenfield placeholder, not implemented validator behavior. |
| [`../../../../../../tests/schemas/test_common_contracts.py`](../../../../../../tests/schemas/test_common_contracts.py) | CONFIRMED | Test harness discovery and valid-fixture behavior. | Tests were not run during this README update. |

[Back to top](#top)
