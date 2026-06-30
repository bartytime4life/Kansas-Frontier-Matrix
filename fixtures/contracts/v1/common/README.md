<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/common/readme
title: Common Contract Fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): schema steward; TODO(owner): common contracts steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-06-30 expansion
updated: 2026-06-30
policy_label: public-review
related: [spec_hash/README.md, spec_hash/valid/README.md, spec_hash/invalid/README.md, ../../../../schemas/contracts/v1/common/README.md, ../../../../schemas/contracts/v1/common/spec_hash.schema.json, ../../../../tests/schemas/test_common_contracts.py, ../../../../fixtures/README.md, ../../../../docs/doctrine/directory-rules.md]
tags: [kfm, fixtures, contracts, v1, common, json-schema, valid-fixtures, invalid-fixtures, expected-error, schema-tests, non-authoritative]
notes: ["This README replaces a blank file at `fixtures/contracts/v1/common/README.md`.", "This directory groups common-family contract fixtures under the test-discovery shape used by `tests/schemas/test_common_contracts.py`.", "Fixture content is not schema authority, contract authority, policy authority, proof authority, release authority, or production data.", "Current verified child fixture family is `spec_hash/`; broader common-family fixture inventory remains PARTIAL until recursively listed or verified by tests.", "There is a documentation tension: `fixtures/README.md` currently emphasizes runtime/benchmark fixture corpora, while Directory Rules and the schema test harness support `fixtures/` as a canonical valid/invalid fixture root. This README documents the live contract-fixture sublane without resolving that root-level wording drift."]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Common contract fixtures

Parent fixture lane for KFM `v1/common` contract schema fixtures.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Contract family: common" src="https://img.shields.io/badge/family-common-blue">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
  <img alt="Inventory: partial" src="https://img.shields.io/badge/inventory-partial-orange">
</p>

**Path:** `fixtures/contracts/v1/common/README.md`  
**Fixture posture:** contract-schema valid/invalid fixture family root  
**Authority posture:** fixture only; schema authority lives under `schemas/contracts/v1/common/`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Placement note](#placement-note) · [Test harness behavior](#test-harness-behavior) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Validation checklist](#validation-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files under this directory are contract fixtures. They are not production objects, source data, proof records, receipts, policy decisions, release decisions, contract authority, or schema authority.

---

## Purpose

This directory groups valid and invalid fixtures for KFM common-family contract schemas.

The expected fixture pattern is:

```text
fixtures/contracts/v1/common/<schema_name>/
├── README.md
├── valid/
│   ├── README.md
│   └── valid_<n>.json
└── invalid/
    ├── README.md
    ├── invalid_<n>.json
    └── invalid_<n>.expected_error.txt
```

Use this lane to keep common schema examples testable and reviewable while preserving the separation between:

- fixtures as test inputs;
- schemas as machine-checkable shape;
- contracts as semantic meaning;
- tools as validator/runtime logic;
- policy as admissibility rules;
- proofs/receipts/release/data as governed operational artifacts.

---

## Current inventory

This inventory is **PARTIAL / CONFIRMED WHERE FETCHED**. It is not a complete recursive tree listing.

| Fixture family | Verified files | Schema basis | Status |
|---|---|---|---|
| [`spec_hash/`](spec_hash/README.md) | [`valid/`](spec_hash/valid/README.md), [`invalid/`](spec_hash/invalid/README.md), `valid_1.json`, `invalid_1.json`, `invalid_1.expected_error.txt` | [`schemas/contracts/v1/common/spec_hash.schema.json`](../../../../schemas/contracts/v1/common/spec_hash.schema.json) | CONFIRMED fixture family / schema status `PROPOSED` |

The current verified `spec_hash` fixture family covers:

| Case | File | Expected behavior |
|---|---|---|
| Minimal valid object | [`spec_hash/valid/valid_1.json`](spec_hash/valid/valid_1.json) | Passes schema shape: object with `value` matching `^sha256:[a-f0-9]{64}$`. |
| Missing required value | [`spec_hash/invalid/invalid_1.json`](spec_hash/invalid/invalid_1.json) | Fails because `{}` omits required `value`. |
| Expected error | [`spec_hash/invalid/invalid_1.expected_error.txt`](spec_hash/invalid/invalid_1.expected_error.txt) | Expected JSON Schema message: `'value' is a required property`. |

---

## Placement note

Directory Rules lists `fixtures/` as a canonical root for golden / valid / invalid test inputs, adjacent to `tests/`. The live test harness also discovers contract fixtures under `fixtures/contracts/v1/<family>/<name>/`.

However, the current `fixtures/README.md` says the root is for runtime/benchmark fixture corpora and "not validator-only test data." That is a documentation tension, not a reason to move this lane during this small change.

Current posture for this README:

| Claim | Status | Notes |
|---|---:|---|
| `fixtures/` is a canonical root in Directory Rules | CONFIRMED | Directory Rules lists `fixtures/` as canonical and paired with `tests/`. |
| Contract fixtures under `fixtures/contracts/v1/...` are used by tests | CONFIRMED | `tests/schemas/test_common_contracts.py` discovers fixture directories in this shape. |
| Root `fixtures/README.md` fully explains contract fixtures | NEEDS VERIFICATION / DRIFT | It currently emphasizes runtime/benchmark fixtures. |
| This README resolves the root-level wording drift | NO | It documents this sublane only. |

---

## Test harness behavior

`tests/schemas/test_common_contracts.py` includes the `common` family in its fixture sweep and discovers schema fixture families under:

```text
fixtures/contracts/v1/<family>/<name>/
```

For each discovered common schema fixture family:

- `valid/valid_*.json` files must produce no JSON Schema errors;
- `invalid/invalid_*.json` files must produce at least one JSON Schema error;
- `invalid/invalid_*.expected_error.txt` files, when present, must match expected text in the combined validation error messages.

This parent README does not claim that tests passed. It only documents the observed harness behavior and fixture layout.

---

## Accepted material

| Accepted item | Purpose |
|---|---|
| `<schema_name>/README.md` | Fixture-family boundary, schema basis, inventory, and local validation notes. |
| `<schema_name>/valid/valid_*.json` | JSON instances expected to pass the matching common schema. |
| `<schema_name>/valid/README.md` | Positive-fixture lane notes. |
| `<schema_name>/invalid/invalid_*.json` | JSON instances expected to fail the matching common schema. |
| `<schema_name>/invalid/invalid_*.expected_error.txt` | Optional expected error fragment for matching invalid fixtures. |
| `<schema_name>/invalid/README.md` | Negative-fixture lane notes. |

---

## Exclusions

| Do not place here | Correct home |
|---|---|
| Common schema definitions | `../../../../schemas/contracts/v1/common/` |
| Semantic contract documentation | `../../../../contracts/common/` |
| Validator implementation | `../../../../tools/validators/` or accepted validator root |
| Policy rules | `../../../../policy/common/` |
| Runtime receipts, proofs, release records, source data, production hashes, or published artifacts | Their canonical KFM roots, not fixtures |
| Generated CI outputs | `../../../../artifacts/` only when explicitly scoped and non-authoritative |

---

## Validation checklist

Before adding or changing common contract fixtures here:

- [ ] The fixture family name matches a schema name under `schemas/contracts/v1/common/`.
- [ ] The matching schema's `x-kfm.fixtures_root`, if present, points to the correct fixture family.
- [ ] Valid fixtures live under `<schema_name>/valid/valid_<n>.json`.
- [ ] Invalid fixtures live under `<schema_name>/invalid/invalid_<n>.json`.
- [ ] Expected error files use `<schema_name>/invalid/invalid_<n>.expected_error.txt`.
- [ ] Fixtures are intentionally small, deterministic, and reviewable.
- [ ] Fixtures do not redefine schemas, contracts, policies, or validators.
- [ ] Fixtures do not contain production hashes, secrets, source data, receipts, proofs, release records, or published artifacts.
- [ ] Any schema change is paired with fixture updates and test-harness review.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target path presence | CONFIRMED | `fixtures/contracts/v1/common/README.md` existed as a blank file before this update. |
| Parent `fixtures/contracts/v1/README.md` | CONFIRMED BLANK | The immediate version parent exists but is blank. |
| Parent `fixtures/README.md` | CONFIRMED README / DRIFT | It emphasizes runtime/benchmark fixtures and does not fully explain contract valid/invalid fixtures. |
| Directory Rules fixture root | CONFIRMED doctrine | Directory Rules lists `fixtures/` as canonical and adjacent to `tests/`. |
| Test harness common family | CONFIRMED | `tests/schemas/test_common_contracts.py` includes `common` in `FAMILIES`. |
| Verified child fixture family | CONFIRMED PARTIAL | `spec_hash/` is verified. No complete recursive inventory was performed. |
| Common schema parent | CONFIRMED README | `schemas/contracts/v1/common/README.md` exists and identifies common schemas. |
| Dedicated validators | PARTIAL / NEEDS VERIFICATION | `spec_hash` validator path exists but is a greenfield placeholder. Other common validators were not inventoried. |
| Runtime validation results | NOT RUN | This README update did not run tests. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define common fixture boundaries or inventory. |
| [`fixtures/README.md`](../../../../fixtures/README.md) | CONFIRMED README | Parent fixture root exists and defines runtime/benchmark fixture intent. | It currently conflicts or under-documents contract fixture usage. |
| [`docs/doctrine/directory-rules.md`](../../../../docs/doctrine/directory-rules.md) | CONFIRMED doctrine | `fixtures/` is canonical and paired with `tests/` for enforceability inputs. | Specific repo path presence still requires live verification. |
| [`tests/schemas/test_common_contracts.py`](../../../../tests/schemas/test_common_contracts.py) | CONFIRMED test harness | Discovers common schemas and fixture families under `fixtures/contracts/v1/common/<name>/`. | Tests were not run during this README update. |
| [`schemas/contracts/v1/common/README.md`](../../../../schemas/contracts/v1/common/README.md) | CONFIRMED README | Common schema parent exists. | It is short and does not inventory all common schemas. |
| [`spec_hash/README.md`](spec_hash/README.md) | CONFIRMED README | Verified child fixture-family contract and inventory. | Does not prove all common fixture families are covered. |
| [`schemas/contracts/v1/common/spec_hash.schema.json`](../../../../schemas/contracts/v1/common/spec_hash.schema.json) | CONFIRMED schema | `spec_hash` schema shape and declared fixtures root. | Schema status is `PROPOSED` in `x-kfm`. |

[Back to top](#top)
