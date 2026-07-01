<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/evidence/readme
title: Evidence Contract Fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): schema steward; TODO(owner): evidence contracts steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-06-30 expansion
updated: 2026-06-30
policy_label: public-review
related: [evidence_bundle/README.md, evidence_ref/README.md, ../../../../schemas/contracts/v1/evidence/README.md, ../../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json, ../../../../schemas/contracts/v1/evidence/evidence_ref.schema.json, ../../../../contracts/evidence/evidence_bundle.md, ../../../../contracts/evidence/evidence_ref.md, ../../../../tests/schemas/test_common_contracts.py, ../../../../docs/doctrine/directory-rules.md]
tags: [kfm, fixtures, contracts, v1, evidence, evidence-bundle, evidence-ref, json-schema, valid-fixtures, invalid-fixtures, schema-tests, non-authoritative]
notes: ["This README replaces a blank file at `fixtures/contracts/v1/evidence/README.md`.", "This directory groups evidence-family contract fixtures under the discovery shape used by `tests/schemas/test_common_contracts.py`.", "Fixture content is schema-test input only; contract meaning, schema shape, validator code, policy rules, release decisions, and operational proof support stay in their owning roots.", "Verified child fixture families in this pass are `evidence_bundle/` and `evidence_ref/`; broader evidence-family coverage is PARTIAL until a full recursive inventory or test run is performed.", "`tools/validators/validate_evidence_bundle.py` exists and points to its schema and fixture root. `tools/validators/validate_evidence_ref.py` is declared by schema metadata but was not found during this check."]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Evidence contract fixtures

Parent fixture lane for KFM `v1/evidence` contract schema fixtures.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Contract family: evidence" src="https://img.shields.io/badge/family-evidence-blue">
  <img alt="Inventory: partial" src="https://img.shields.io/badge/inventory-partial-orange">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/contracts/v1/evidence/README.md`  
**Fixture posture:** evidence-family valid/invalid schema fixture parent  
**Authority posture:** fixture only; schema authority lives under `schemas/contracts/v1/evidence/`  
**Quick links:** [Purpose](#purpose) · [Verified inventory](#verified-inventory) · [Schema and contract basis](#schema-and-contract-basis) · [Harness behavior](#harness-behavior) · [Accepted layout](#accepted-layout) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files under this directory are contract fixtures. They are not semantic contracts, schema authority, validator implementation, policy authority, release approval, claim closure, or operational proof support.

---

## Purpose

This directory groups valid and invalid fixture families for KFM evidence contract schemas.

The expected shape is:

```text
fixtures/contracts/v1/evidence/<schema_name>/
├── README.md
├── valid/
│   ├── README.md
│   └── valid_<n>.json
└── invalid/
    ├── README.md
    ├── invalid_<n>.json
    └── invalid_<n>.expected_error.txt
```

Use this lane to keep evidence schema examples small, deterministic, reviewable, and testable.

---

## Verified inventory

This inventory is **PARTIAL / CONFIRMED WHERE FETCHED**. It is not a complete recursive tree listing.

| Fixture family | Current positive case | Current negative case | Validator posture | Status |
|---|---|---|---|---|
| [`evidence_bundle/`](evidence_bundle/README.md) | `valid/valid_1.json` includes `bundle_id` and required top-level fields. | `invalid/invalid_1.json` omits required `bundle_id`; expected error matcher is `required`. | `tools/validators/validate_evidence_bundle.py` exists; not run. | CONFIRMED fixture family / schema status `PROPOSED` |
| [`evidence_ref/`](evidence_ref/README.md) | `valid/valid_1.json` includes required `ref` and `kind`. | `invalid/invalid_1.json` omits required `ref`; expected error matcher is `required`. | `tools/validators/validate_evidence_ref.py` is declared in schema metadata but was not found. | CONFIRMED fixture family / schema status `PROPOSED` |

---

## Schema and contract basis

| Family | Schema | Contract | Fixture root declared by schema |
|---|---|---|---|
| `evidence_bundle` | [`../../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json`](../../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json) | [`../../../../contracts/evidence/evidence_bundle.md`](../../../../contracts/evidence/evidence_bundle.md) | `fixtures/contracts/v1/evidence/evidence_bundle/` |
| `evidence_ref` | [`../../../../schemas/contracts/v1/evidence/evidence_ref.schema.json`](../../../../schemas/contracts/v1/evidence/evidence_ref.schema.json) | [`../../../../contracts/evidence/evidence_ref.md`](../../../../contracts/evidence/evidence_ref.md) | `fixtures/contracts/v1/evidence/evidence_ref/` |

The schema parent README at `schemas/contracts/v1/evidence/README.md` identifies this as the evidence schema family. Directory Rules identifies `fixtures/` as a canonical root for valid/invalid test inputs paired with `tests/`.

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

This README documents expected fixture behavior only. It does not claim that pytest, CI, or the validator suite was run during this update.

---

## Accepted layout

| Accepted item | Purpose |
|---|---|
| `<schema_name>/README.md` | Fixture-family boundary, inventory, and schema linkage. |
| `<schema_name>/valid/README.md` | Positive-fixture lane notes. |
| `<schema_name>/valid/valid_*.json` | JSON instances expected to pass the matching evidence schema. |
| `<schema_name>/invalid/README.md` | Negative-fixture lane notes. |
| `<schema_name>/invalid/invalid_*.json` | JSON instances expected to fail the matching evidence schema. |
| `<schema_name>/invalid/invalid_*.expected_error.txt` | Optional expected error fragment for the matching invalid fixture. |

---

## Maintenance checklist

Before adding or changing evidence fixtures here:

- [ ] Match the fixture family name to a schema name under `schemas/contracts/v1/evidence/`.
- [ ] Keep positive examples under `<schema_name>/valid/valid_<n>.json`.
- [ ] Keep negative examples under `<schema_name>/invalid/invalid_<n>.json`.
- [ ] Keep expected-error text beside the invalid fixture it describes.
- [ ] Keep fixture cases small, deterministic, and reviewable.
- [ ] Update fixture docs when schema behavior changes.
- [ ] Verify validator-wrapper paths before claiming validator maturity.
- [ ] Run the relevant schema tests before promotion.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED | `fixtures/contracts/v1/evidence/README.md` existed as a blank file before this update. |
| Immediate version parent | CONFIRMED BLANK | `fixtures/contracts/v1/README.md` exists but is blank. |
| Evidence schema parent | CONFIRMED README | `schemas/contracts/v1/evidence/README.md` exists and identifies evidence schemas. |
| Verified child families | CONFIRMED PARTIAL | `evidence_bundle/` and `evidence_ref/` are documented. No full recursive inventory was performed. |
| Directory Rules fixture root | CONFIRMED doctrine | `fixtures/` is a canonical root for valid/invalid test inputs. |
| Schema harness | CONFIRMED / NOT RUN | `tests/schemas/test_common_contracts.py` includes `evidence` and discovers this fixture shape. |
| `evidence_bundle` validator wrapper | CONFIRMED / NOT RUN | Wrapper exists and targets the bundle schema and fixture root. |
| `evidence_ref` validator wrapper | NOT FOUND | Schema metadata declares the wrapper path, but the file was not found during this check. |
| Runtime validation results | NOT RUN | This README update did not run validators, pytest, or CI. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define evidence fixture-family guidance. |
| [`evidence_bundle/README.md`](evidence_bundle/README.md) | CONFIRMED | Bundle fixture family inventory and schema/harness linkage. | Its parent README is intentionally compact; richer lane details live under `valid/` and `invalid/`. |
| [`evidence_ref/README.md`](evidence_ref/README.md) | CONFIRMED | EvidenceRef fixture family inventory, schema basis, and validator-path issue. | Does not prove tests were run. |
| [`../../../../schemas/contracts/v1/evidence/README.md`](../../../../schemas/contracts/v1/evidence/README.md) | CONFIRMED README | Evidence schema family exists. | It is short and does not inventory all evidence schemas. |
| [`../../../../tests/schemas/test_common_contracts.py`](../../../../tests/schemas/test_common_contracts.py) | CONFIRMED | Evidence-family fixture discovery and valid/invalid behavior. | Tests were not run during this update. |
| [`../../../../docs/doctrine/directory-rules.md`](../../../../docs/doctrine/directory-rules.md) | CONFIRMED | `fixtures/` is canonical and paired with `tests/`. | Specific fixture coverage still requires tests or inventory. |
| [`../../../../tools/validators/validate_evidence_bundle.py`](../../../../tools/validators/validate_evidence_bundle.py) | CONFIRMED | Bundle validator wrapper exists and points to the bundle schema and fixture root. | Wrapper was not executed during this update. |
| `../../../../tools/validators/validate_evidence_ref.py` | NOT FOUND | EvidenceRef schema declares this path. | File was not found during this check. |

[Back to top](#top)
