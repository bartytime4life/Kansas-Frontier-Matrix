<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/governance/review-record/valid/readme
title: review_record valid fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): schema steward; TODO(owner): governance contracts steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-06-30 expansion
updated: 2026-06-30
policy_label: public-review
related: [valid_1.json, ../invalid/README.md, ../invalid/invalid_1.json, ../invalid/invalid_1.expected_error.txt, ../../../../../../schemas/contracts/v1/governance/review_record.schema.json, ../../../../../../contracts/governance/review_record.md, ../../../../../../tools/validators/validate_review_record.py, ../../../../../../tests/schemas/test_common_contracts.py, ../../../../../../docs/doctrine/directory-rules.md]
tags: [kfm, fixtures, contracts, v1, governance, review-record, valid-fixtures, json-schema, positive-tests, non-authoritative]
notes: ["This README replaces a blank file at `fixtures/contracts/v1/governance/review_record/valid/README.md`.", "Valid fixtures are schema test inputs only; schema shape, contract meaning, validator implementation, and policy rules stay in their owning roots.", "The active schema evidence is `schemas/contracts/v1/governance/review_record.schema.json`, whose `x-kfm.fixtures_root` points to `fixtures/contracts/v1/governance/review_record/`.", "The current valid fixture includes required `review_id` and all other required top-level fields.", "The schema metadata declares `contracts/governance/review_record.md`, but that file was not found during the paired invalid-lane check.", "The dedicated validator file exists but is a greenfield placeholder and was not executed during this update."]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `review_record` valid fixtures

Intentional positive fixtures for the KFM `review_record` governance contract.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Family: governance" src="https://img.shields.io/badge/family-governance-blue">
  <img alt="Contract: review_record" src="https://img.shields.io/badge/contract-review__record-purple">
  <img alt="Fixture kind: valid" src="https://img.shields.io/badge/fixture-valid-2ea44f">
</p>

**Path:** `fixtures/contracts/v1/governance/review_record/valid/README.md`  
**Fixture posture:** positive JSON Schema fixture lane  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/governance/review_record.schema.json`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Schema basis](#schema-basis) · [Harness behavior](#harness-behavior) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are expected to pass validation. They are not the semantic contract, schema authority, validator implementation, policy authority, review approval, or release approval.

---

## Purpose

This directory holds valid JSON fixtures for the `review_record` governance contract schema.

Use this lane to verify that a minimal ReviewRecord-like object with required governance-review fields is accepted by schema validation.

---

## Current inventory

| Fixture | Valid because | Notes |
|---|---|---|
| [`valid_1.json`](valid_1.json) | Includes `review_id` and every top-level field required by `review_record.schema.json`. | Minimal positive case paired with `../invalid/invalid_1.json`, which omits `review_id`. |

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

---

## Schema basis

The current schema evidence for this fixture lane is:

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

This README documents fixture behavior only. It does not claim that pytest, CI, or the dedicated review-record validator was run during this update.

---

## Maintenance checklist

Before changing valid fixtures here:

- [ ] Keep file names in the `valid_<n>.json` pattern.
- [ ] Keep the passing case narrow and reviewable.
- [ ] Include every field required by `review_record.schema.json`.
- [ ] Use schema-allowed `reviewer_role` and `decision` values.
- [ ] Keep `reviewed_at` in date-time form.
- [ ] Check the matching negative fixture under `../invalid/` when changing schema behavior.
- [ ] Verify the validator implementation before claiming validator maturity.
- [ ] Run the relevant schema tests before promotion.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED | This path existed as a blank file before this update. |
| Valid fixture | CONFIRMED | `valid_1.json` exists and includes `review_id` plus all required top-level fields. |
| Invalid sibling lane | CONFIRMED | `../invalid/README.md` documents the current invalid fixture and expected-error matcher. |
| Schema | CONFIRMED | `review_record.schema.json` defines required fields, enums, date-time format, and additional-property behavior. |
| Contract doc | NOT FOUND | `contracts/governance/review_record.md` is declared in schema metadata but was not found during the paired invalid-lane check. |
| Validator file | CONFIRMED PLACEHOLDER / NOT RUN | `tools/validators/validate_review_record.py` exists but raises `NotImplementedError`. |
| Test execution | NOT RUN | No validators, pytest, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define valid fixture guidance. |
| [`valid_1.json`](valid_1.json) | CONFIRMED | Current positive fixture includes `review_id` and all required top-level fields. | Only one valid fixture is currently verified. |
| [`../invalid/README.md`](../invalid/README.md) | CONFIRMED | Sibling invalid fixture lane and schema/test boundary pattern. | Does not prove valid fixture behavior by itself. |
| [`../invalid/invalid_1.json`](../invalid/invalid_1.json) | CONFIRMED | Negative comparison fixture omits required `review_id`. | Belongs to the invalid lane. |
| [`../../../../../../schemas/contracts/v1/governance/review_record.schema.json`](../../../../../../schemas/contracts/v1/governance/review_record.schema.json) | CONFIRMED | Schema shape, required fields, enum values, date-time format, fixture root, and declared validator path. | Schema status is `PROPOSED`. |
| `../../../../../../contracts/governance/review_record.md` | NOT FOUND | Schema metadata declares this contract path. | No contract file was found during the paired invalid-lane check. |
| [`../../../../../../tools/validators/validate_review_record.py`](../../../../../../tools/validators/validate_review_record.py) | CONFIRMED PLACEHOLDER | Validator file exists. | It is a greenfield placeholder and was not executed. |
| [`../../../../../../tests/schemas/test_common_contracts.py`](../../../../../../tests/schemas/test_common_contracts.py) | CONFIRMED | Fixture discovery and valid-fixture validation behavior. | Tests were not run during this update. |

[Back to top](#top)
