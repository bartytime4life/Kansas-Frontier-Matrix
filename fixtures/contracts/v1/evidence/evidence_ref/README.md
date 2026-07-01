<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/evidence/evidence-ref/readme
title: evidence_ref fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): schema steward; TODO(owner): evidence contracts steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-06-30 expansion
updated: 2026-06-30
policy_label: public-review
related: [valid/README.md, valid/valid_1.json, invalid/README.md, invalid/invalid_1.json, invalid/invalid_1.expected_error.txt, ../../../../../schemas/contracts/v1/evidence/evidence_ref.schema.json, ../../../../../contracts/evidence/evidence_ref.md, ../../../../../tests/schemas/test_common_contracts.py, ../../../../../docs/doctrine/directory-rules.md]
tags: [kfm, fixtures, contracts, v1, evidence, evidence-ref, json-schema, valid-fixtures, invalid-fixtures, expected-error, non-authoritative]
notes: ["This README replaces a blank file at `fixtures/contracts/v1/evidence/evidence_ref/README.md`.", "This directory is the schema-declared fixture root for `evidence_ref`.", "Fixtures are schema test inputs only; schema shape, contract meaning, validator implementation, and policy rules stay in their owning roots.", "The current fixture family has one valid case and one invalid case.", "The schema metadata declares `tools/validators/validate_evidence_ref.py`, but that file was not found during the paired lane checks."]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `evidence_ref` fixtures

Fixture family for the KFM `evidence_ref` evidence contract.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Family: evidence" src="https://img.shields.io/badge/family-evidence-blue">
  <img alt="Contract: evidence_ref" src="https://img.shields.io/badge/contract-evidence__ref-purple">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/contracts/v1/evidence/evidence_ref/README.md`  
**Fixture posture:** JSON Schema valid/invalid fixture family  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/evidence/evidence_ref.schema.json`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Schema basis](#schema-basis) · [Contract boundary](#contract-boundary) · [Harness behavior](#harness-behavior) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are schema fixtures. They are not the semantic contract, schema authority, validator implementation, policy authority, release approval, or claim closure.

---

## Purpose

This directory groups positive and negative JSON fixtures for the `evidence_ref` contract schema.

Use this fixture family to verify that KFM accepts a minimal valid EvidenceRef-like pointer and rejects an incomplete one. The schema-declared fixture root is:

```text
fixtures/contracts/v1/evidence/evidence_ref/
```

---

## Current inventory

| Lane | File | Current role | Status |
|---|---|---|---|
| [`valid/`](valid/README.md) | [`valid_1.json`](valid/valid_1.json) | Minimal positive fixture with required `ref` and `kind`. | CONFIRMED |
| [`invalid/`](invalid/README.md) | [`invalid_1.json`](invalid/invalid_1.json) | Minimal negative fixture with `kind` but missing required `ref`. | CONFIRMED |
| [`invalid/`](invalid/README.md) | [`invalid_1.expected_error.txt`](invalid/invalid_1.expected_error.txt) | Current expected-error matcher: `required`. | CONFIRMED / BROAD MATCHER |

Current positive fixture shape:

```json
{
  "ref": "obs:1",
  "kind": "measurement"
}
```

Current negative fixture shape:

```json
{
  "kind": "measurement"
}
```

---

## Schema basis

The current schema evidence for this fixture family is:

```text
schemas/contracts/v1/evidence/evidence_ref.schema.json
```

Confirmed schema facts:

| Item | Value |
|---|---|
| Schema title | `evidence_ref` |
| Root type | object |
| Required fields | `ref`, `kind` |
| `kind` enum values | `measurement`, `record`, `dataset`, `artifact` |
| Optional field | `bundle_ref` |
| Additional properties | false |
| Declared contract doc | `contracts/evidence/evidence_ref.md` |
| Declared fixture root | `fixtures/contracts/v1/evidence/evidence_ref/` |
| Declared validator | `tools/validators/validate_evidence_ref.py` |
| Declared policy path | `policy/evidence/` |
| Schema status | `PROPOSED` |

---

## Contract boundary

The semantic contract describes `EvidenceRef` as a governed pointer to supporting material. It is smaller than an `EvidenceBundle` and does not close a claim by itself.

| Responsibility | Home | Status in this check |
|---|---|---|
| Fixture examples | `fixtures/contracts/v1/evidence/evidence_ref/` | CONFIRMED |
| Machine-checkable shape | `schemas/contracts/v1/evidence/evidence_ref.schema.json` | CONFIRMED |
| Semantic meaning | `contracts/evidence/evidence_ref.md` | CONFIRMED |
| Schema test harness | `tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN |
| Dedicated validator wrapper | `tools/validators/validate_evidence_ref.py` | NOT FOUND |

---

## Harness behavior

`tests/schemas/test_common_contracts.py` includes the `evidence` family and discovers fixture families under:

```text
fixtures/contracts/v1/<family>/<name>/
```

Observed harness expectations:

| Fixture pattern | Expected result |
|---|---|
| `valid/valid_*.json` | no JSON Schema errors |
| `invalid/invalid_*.json` | at least one JSON Schema error |
| `invalid/invalid_*.expected_error.txt` | expected text appears in combined error messages |

This README documents expected fixture behavior only. It does not claim that pytest, CI, or a dedicated EvidenceRef validator was run during this update.

---

## Maintenance checklist

Before changing this fixture family:

- [ ] Keep passing examples under `valid/valid_<n>.json`.
- [ ] Keep failing examples under `invalid/invalid_<n>.json`.
- [ ] Keep expected-error text beside the invalid fixture it describes.
- [ ] Keep fixture cases small and reviewable.
- [ ] Update fixture docs when schema behavior changes.
- [ ] Run the relevant schema tests before promotion.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED | This path existed as a blank file before this update. |
| Valid lane | CONFIRMED | `valid/README.md` and `valid/valid_1.json` exist. |
| Invalid lane | CONFIRMED | `invalid/README.md`, `invalid/invalid_1.json`, and `invalid/invalid_1.expected_error.txt` exist. |
| Schema | CONFIRMED | `evidence_ref.schema.json` defines required `ref` and `kind`. |
| Contract doc | CONFIRMED | `contracts/evidence/evidence_ref.md` defines EvidenceRef as a governed pointer. |
| Declared validator wrapper | NOT FOUND | `tools/validators/validate_evidence_ref.py` is declared in schema metadata but was not found during the lane checks. |
| Test execution | NOT RUN | No validators, pytest, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define fixture-family guidance. |
| [`valid/README.md`](valid/README.md) | CONFIRMED | Positive fixture lane guidance. | Does not prove tests were run. |
| [`valid/valid_1.json`](valid/valid_1.json) | CONFIRMED | Current positive fixture includes required `ref` and `kind`. | Only one valid fixture is currently verified. |
| [`invalid/README.md`](invalid/README.md) | CONFIRMED | Negative fixture lane guidance. | Does not prove tests were run. |
| [`invalid/invalid_1.json`](invalid/invalid_1.json) | CONFIRMED | Current negative fixture omits required `ref`. | Only one invalid fixture is currently verified. |
| [`invalid/invalid_1.expected_error.txt`](invalid/invalid_1.expected_error.txt) | CONFIRMED | Current expected-error matcher is `required`. | Broad matcher; may be tightened later. |
| [`../../../../../schemas/contracts/v1/evidence/evidence_ref.schema.json`](../../../../../schemas/contracts/v1/evidence/evidence_ref.schema.json) | CONFIRMED | Schema shape, required fields, enum values, fixture root, and declared validator path. | Schema status is `PROPOSED`. |
| [`../../../../../contracts/evidence/evidence_ref.md`](../../../../../contracts/evidence/evidence_ref.md) | CONFIRMED | Semantic contract and EvidenceRef boundary. | Runtime behavior remains separately verified. |
| [`../../../../../tests/schemas/test_common_contracts.py`](../../../../../tests/schemas/test_common_contracts.py) | CONFIRMED | Fixture discovery and valid/invalid fixture behavior. | Tests were not run during this update. |
| [`../../../../../docs/doctrine/directory-rules.md`](../../../../../docs/doctrine/directory-rules.md) | CONFIRMED | `fixtures/` is a canonical root for valid/invalid test inputs. | Specific fixture coverage still requires tests or inventory. |

[Back to top](#top)
