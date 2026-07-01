<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/evidence/evidence-ref/valid/readme
title: evidence_ref valid fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): schema steward; TODO(owner): evidence contracts steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-06-30 expansion
updated: 2026-06-30
policy_label: public-review
related: [valid_1.json, ../invalid/README.md, ../invalid/invalid_1.json, ../invalid/invalid_1.expected_error.txt, ../../../../../../schemas/contracts/v1/evidence/evidence_ref.schema.json, ../../../../../../contracts/evidence/evidence_ref.md, ../../../../../../tests/schemas/test_common_contracts.py, ../../../../../../docs/doctrine/directory-rules.md]
tags: [kfm, fixtures, contracts, v1, evidence, evidence-ref, valid-fixtures, json-schema, positive-tests, non-authoritative]
notes: ["This README replaces a blank file at `fixtures/contracts/v1/evidence/evidence_ref/valid/README.md`.", "Valid fixtures are schema test inputs only; schema shape, contract meaning, validator implementation, and policy rules stay in their owning roots.", "The active schema evidence is `schemas/contracts/v1/evidence/evidence_ref.schema.json`, whose `x-kfm.fixtures_root` points to `fixtures/contracts/v1/evidence/evidence_ref/`.", "The current valid fixture includes required `ref` and `kind` fields and omits optional `bundle_ref`.", "The schema metadata declares `tools/validators/validate_evidence_ref.py`, but that file was not found during the paired invalid-lane check."]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `evidence_ref` valid fixtures

Intentional positive fixtures for the KFM `evidence_ref` evidence contract.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Family: evidence" src="https://img.shields.io/badge/family-evidence-blue">
  <img alt="Contract: evidence_ref" src="https://img.shields.io/badge/contract-evidence__ref-purple">
  <img alt="Fixture kind: valid" src="https://img.shields.io/badge/fixture-valid-2ea44f">
</p>

**Path:** `fixtures/contracts/v1/evidence/evidence_ref/valid/README.md`  
**Fixture posture:** positive JSON Schema fixture lane  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/evidence/evidence_ref.schema.json`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Schema basis](#schema-basis) · [Harness behavior](#harness-behavior) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are expected to pass validation. They are not the semantic contract, schema authority, validator implementation, or policy authority.

---

## Purpose

This directory holds valid JSON fixtures for the `evidence_ref` contract schema.

Use this lane to verify that a minimal EvidenceRef-like object with required `ref` and `kind` fields is accepted by schema validation.

---

## Current inventory

| Fixture | Valid because | Notes |
|---|---|---|
| [`valid_1.json`](valid_1.json) | Contains required `ref` and `kind` fields. | Minimal positive case with `kind: measurement`; optional `bundle_ref` is omitted. |

Current fixture shape:

```json
{
  "ref": "obs:1",
  "kind": "measurement"
}
```

---

## Schema basis

The current schema evidence for this fixture lane is:

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

This README documents fixture behavior only. It does not claim that pytest, CI, or a dedicated EvidenceRef validator was run during this update.

---

## Maintenance checklist

Before changing valid fixtures here:

- [ ] Keep file names in the `valid_<n>.json` pattern.
- [ ] Keep the passing case narrow and reviewable.
- [ ] Include required `ref` and `kind` fields.
- [ ] Use a `kind` value allowed by the schema enum.
- [ ] Add optional `bundle_ref` only when that case is intentional.
- [ ] Check the matching negative fixture under `../invalid/` when changing schema behavior.
- [ ] Run the relevant schema tests before promotion.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED | This path existed as a blank file before this update. |
| Valid fixture | CONFIRMED | `valid_1.json` exists and includes `ref` and `kind`. |
| Invalid sibling lane | CONFIRMED | `../invalid/README.md` documents the current invalid fixture and expected-error matcher. |
| Schema | CONFIRMED | `evidence_ref.schema.json` defines required `ref` and `kind`. |
| Contract doc | CONFIRMED | `contracts/evidence/evidence_ref.md` exists and defines EvidenceRef as a governed pointer. |
| Declared validator wrapper | NOT FOUND | `tools/validators/validate_evidence_ref.py` is declared in schema metadata but was not found during the paired invalid-lane check. |
| Test execution | NOT RUN | No validators, pytest, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define valid fixture guidance. |
| [`valid_1.json`](valid_1.json) | CONFIRMED | Current positive fixture includes required `ref` and `kind`. | Only one valid fixture is currently verified. |
| [`../invalid/README.md`](../invalid/README.md) | CONFIRMED | Sibling invalid fixture lane and schema/test boundary pattern. | Does not prove valid fixture behavior by itself. |
| [`../invalid/invalid_1.json`](../invalid/invalid_1.json) | CONFIRMED | Negative comparison fixture omits required `ref`. | Belongs to the invalid lane. |
| [`../../../../../../schemas/contracts/v1/evidence/evidence_ref.schema.json`](../../../../../../schemas/contracts/v1/evidence/evidence_ref.schema.json) | CONFIRMED | Schema shape, required fields, enum values, fixture root, and declared validator path. | Schema status is `PROPOSED`. |
| [`../../../../../../contracts/evidence/evidence_ref.md`](../../../../../../contracts/evidence/evidence_ref.md) | CONFIRMED | Semantic contract and EvidenceRef boundary. | Runtime behavior remains separately verified. |
| [`../../../../../../tests/schemas/test_common_contracts.py`](../../../../../../tests/schemas/test_common_contracts.py) | CONFIRMED | Fixture discovery and valid-fixture validation behavior. | Tests were not run during this update. |
| [`../../../../../../docs/doctrine/directory-rules.md`](../../../../../../docs/doctrine/directory-rules.md) | CONFIRMED | `fixtures/` is a canonical root for valid/invalid test inputs. | Specific fixture coverage still requires tests or inventory. |

[Back to top](#top)
