<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/governance/review-record/readme
title: review_record fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): schema steward; TODO(owner): governance contracts steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-06-30 expansion
updated: 2026-06-30
policy_label: public-review
related: [valid/README.md, valid/valid_1.json, invalid/README.md, invalid/invalid_1.json, invalid/invalid_1.expected_error.txt, ../../../../../schemas/contracts/v1/governance/review_record.schema.json, ../../../../../contracts/governance/review_record.md, ../../../../../tools/validators/validate_review_record.py, ../../../../../tests/schemas/test_common_contracts.py, ../../../../../docs/doctrine/directory-rules.md]
tags: [kfm, fixtures, contracts, v1, governance, review-record, json-schema, valid-fixtures, invalid-fixtures, expected-error, non-authoritative]
notes: ["This README replaces a blank file at `fixtures/contracts/v1/governance/review_record/README.md`.", "This directory is the schema-declared fixture root for `review_record`.", "Fixtures are schema test inputs only; schema shape, contract meaning, validator implementation, and policy rules stay in their owning roots.", "The current fixture family has one valid case and one invalid case.", "The schema metadata declares `contracts/governance/review_record.md`, but that file was not found during the paired lane checks.", "The dedicated validator file exists but is a greenfield placeholder and was not executed during this update."]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `review_record` fixtures

Fixture family for the KFM `review_record` governance contract.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Family: governance" src="https://img.shields.io/badge/family-governance-blue">
  <img alt="Contract: review_record" src="https://img.shields.io/badge/contract-review__record-purple">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/contracts/v1/governance/review_record/README.md`  
**Fixture posture:** JSON Schema valid/invalid fixture family  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/governance/review_record.schema.json`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Schema basis](#schema-basis) · [Authority boundary](#authority-boundary) · [Harness behavior](#harness-behavior) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are schema fixtures. They are not the semantic contract, schema authority, validator implementation, policy authority, review approval, or release approval.

---

## Purpose

This directory groups positive and negative JSON fixtures for the `review_record` governance contract schema.

Use this fixture family to verify that KFM accepts a minimal valid ReviewRecord-like object and rejects an incomplete one. The schema-declared fixture root is:

```text
fixtures/contracts/v1/governance/review_record/
```

---

## Current inventory

| Lane | File | Current role | Status |
|---|---|---|---|
| [`valid/`](valid/README.md) | [`valid_1.json`](valid/valid_1.json) | Minimal positive fixture with `review_id` and all required top-level fields. | CONFIRMED |
| [`invalid/`](invalid/README.md) | [`invalid_1.json`](invalid/invalid_1.json) | Minimal negative fixture with matching review context but missing required `review_id`. | CONFIRMED |
| [`invalid/`](invalid/README.md) | [`invalid_1.expected_error.txt`](invalid/invalid_1.expected_error.txt) | Current expected-error matcher: `required`. | CONFIRMED / BROAD MATCHER |

Current positive fixture shape:

```json
{
  "review_id": "rev1",
  "subject_ref": "bundle:1",
  "reviewer_role": "steward",
  "decision": "approve",
  "reasons": ["ok"],
  "obligations": [],
  "reviewed_at": "2026-05-09T00:00:00Z"
}
```

Current negative fixture shape:

```json
{
  "subject_ref": "bundle:1",
  "reviewer_role": "steward",
  "decision": "approve",
  "reasons": ["ok"],
  "obligations": [],
  "reviewed_at": "2026-05-09T00:00:00Z"
}
```

---

## Schema basis

The current schema evidence for this fixture family is:

```text
schemas/contracts/v1/governance/review_record.schema.json
```

Confirmed schema facts:

| Item | Value |
|---|---|
| Schema title | `review_record` |
| Root type | object |
| Required fields | `review_id`, `subject_ref`, `reviewer_role`, `decision`, `reasons`, `obligations`, `reviewed_at` |
| `review_id` | string matching `^[a-z][a-z0-9_:.-]*$` |
| `reviewer_role` enum values | `steward`, `reviewer`, `auditor` |
| `decision` enum values | `approve`, `reject`, `request_changes` |
| `reviewed_at` | string with `date-time` format |
| Additional properties | false |
| Declared contract doc | `contracts/governance/review_record.md` |
| Declared fixture root | `fixtures/contracts/v1/governance/review_record/` |
| Declared validator | `tools/validators/validate_review_record.py` |
| Declared policy path | `policy/governance/` |
| Schema status | `PROPOSED` |

---

## Authority boundary

| Responsibility | Home | Status in this check |
|---|---|---|
| Fixture examples | `fixtures/contracts/v1/governance/review_record/` | CONFIRMED |
| Machine-checkable shape | `schemas/contracts/v1/governance/review_record.schema.json` | CONFIRMED |
| Semantic contract | `contracts/governance/review_record.md` | NOT FOUND |
| Validator implementation | `tools/validators/validate_review_record.py` | CONFIRMED PLACEHOLDER / NOT RUN |
| Schema test harness | `tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN |
| Governance policy | `policy/governance/` | DECLARED BY SCHEMA / NOT VERIFIED IN THIS UPDATE |

---

## Harness behavior

`tests/schemas/test_common_contracts.py` includes the `governance` family and discovers fixture families under:

```text
fixtures/contracts/v1/<family>/<name>/
```

Observed harness expectations:

| Fixture pattern | Expected result |
|---|---|
| `valid/valid_*.json` | no JSON Schema errors |
| `invalid/invalid_*.json` | at least one JSON Schema error |
| `invalid/invalid_*.expected_error.txt` | expected text appears in combined error messages |

This README documents expected fixture behavior only. It does not claim that pytest, CI, or the dedicated review-record validator was run during this update.

---

## Maintenance checklist

Before changing this fixture family:

- [ ] Keep passing examples under `valid/valid_<n>.json`.
- [ ] Keep failing examples under `invalid/invalid_<n>.json`.
- [ ] Keep expected-error text beside the invalid fixture it describes.
- [ ] Keep fixture cases small and reviewable.
- [ ] Update fixture docs when schema behavior changes.
- [ ] Verify the validator implementation before claiming validator maturity.
- [ ] Run the relevant schema tests before promotion.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED | This path existed as a blank file before this update. |
| Valid lane | CONFIRMED | `valid/README.md` and `valid/valid_1.json` exist. |
| Invalid lane | CONFIRMED | `invalid/README.md`, `invalid/invalid_1.json`, and `invalid/invalid_1.expected_error.txt` exist. |
| Schema | CONFIRMED | `review_record.schema.json` defines required fields, enums, date-time format, fixture root, and additional-property behavior. |
| Contract doc | NOT FOUND | `contracts/governance/review_record.md` is declared in schema metadata but was not found during paired lane checks. |
| Validator file | CONFIRMED PLACEHOLDER / NOT RUN | `tools/validators/validate_review_record.py` exists but raises `NotImplementedError`. |
| Test execution | NOT RUN | No validators, pytest, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define fixture-family guidance. |
| [`valid/README.md`](valid/README.md) | CONFIRMED | Positive fixture lane guidance. | Does not prove tests were run. |
| [`valid/valid_1.json`](valid/valid_1.json) | CONFIRMED | Current positive fixture includes `review_id` and all required top-level fields. | Only one valid fixture is currently verified. |
| [`invalid/README.md`](invalid/README.md) | CONFIRMED | Negative fixture lane guidance. | Does not prove tests were run. |
| [`invalid/invalid_1.json`](invalid/invalid_1.json) | CONFIRMED | Current negative fixture omits required `review_id`. | Only one invalid fixture is currently verified. |
| [`invalid/invalid_1.expected_error.txt`](invalid/invalid_1.expected_error.txt) | CONFIRMED | Current expected-error matcher is `required`. | Broad matcher; may be tightened later. |
| [`../../../../../schemas/contracts/v1/governance/review_record.schema.json`](../../../../../schemas/contracts/v1/governance/review_record.schema.json) | CONFIRMED | Schema shape, required fields, enum values, date-time format, fixture root, and declared validator path. | Schema status is `PROPOSED`. |
| `../../../../../contracts/governance/review_record.md` | NOT FOUND | Schema metadata declares this contract path. | No contract file was found during the paired lane checks. |
| [`../../../../../tools/validators/validate_review_record.py`](../../../../../tools/validators/validate_review_record.py) | CONFIRMED PLACEHOLDER | Validator file exists. | It is a greenfield placeholder and was not executed. |
| [`../../../../../tests/schemas/test_common_contracts.py`](../../../../../tests/schemas/test_common_contracts.py) | CONFIRMED | Fixture discovery and valid/invalid fixture behavior. | Tests were not run during this update. |
| [`../../../../../docs/doctrine/directory-rules.md`](../../../../../docs/doctrine/directory-rules.md) | CONFIRMED | `fixtures/` is a canonical root for valid/invalid test inputs. | Specific fixture coverage still requires tests or inventory. |

[Back to top](#top)
