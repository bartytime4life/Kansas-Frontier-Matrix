<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/evidence/evidence-bundle/invalid/readme
title: evidence_bundle invalid fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): schema steward; TODO(owner): evidence contracts steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): evidence steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-06-30 expansion
updated: 2026-06-30
policy_label: public-review
related: [../README.md, ../valid/valid_1.json, invalid_1.json, invalid_1.expected_error.txt, ../../../../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json, ../../../../../../schemas/contracts/v1/evidence/README.md, ../../../../../../contracts/evidence/evidence_bundle.md, ../../../../../../tools/validators/validate_evidence_bundle.py, ../../../../../../tests/schemas/test_common_contracts.py]
tags: [kfm, fixtures, contracts, v1, evidence, evidence-bundle, invalid-fixtures, json-schema, expected-error, negative-tests, evidence-bundle-not-proof, non-authoritative]
notes: ["This README replaces a blank file at `fixtures/contracts/v1/evidence/evidence_bundle/invalid/README.md`.", "Invalid fixtures are intentionally failing inputs for schema enforcement; they are not EvidenceBundle authority, proof authority, source truth, contract authority, schema authority, policy authority, release authority, or production data.", "The active schema evidence for this lane is `schemas/contracts/v1/evidence/evidence_bundle.schema.json`; the fixture root is declared in that schema's `x-kfm.fixtures_root`.", "The current invalid fixture omits required `bundle_id`. The sibling expected-error file currently contains the broad matcher text `required`.", "The dedicated `tools/validators/validate_evidence_bundle.py` wrapper exists and points at the evidence_bundle schema and fixture root, but this README update did not run it or the pytest harness."]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `evidence_bundle` invalid fixtures

Intentional negative fixtures for the KFM `evidence_bundle` evidence contract.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Contract family: evidence" src="https://img.shields.io/badge/family-evidence-blue">
  <img alt="Contract: evidence_bundle" src="https://img.shields.io/badge/contract-evidence__bundle-purple">
  <img alt="Fixture kind: invalid" src="https://img.shields.io/badge/fixture-invalid-critical">
</p>

**Path:** `fixtures/contracts/v1/evidence/evidence_bundle/invalid/README.md`  
**Fixture posture:** negative JSON Schema fixture lane  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/evidence/evidence_bundle.schema.json`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Schema basis](#schema-basis) · [Test harness behavior](#test-harness-behavior) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Validation checklist](#validation-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are expected to fail validation. They are not operational EvidenceBundles, ProofPacks, source data, proof records, receipts, policy decisions, release decisions, or contract/schema authority.

> [!CAUTION]
> `evidence_bundle` fixture examples may look like proof objects, but fixture placement does not make them proof. Operational proof support belongs under the governed proof roots, with policy, provenance, validation, review, release/correction/rollback context as applicable.

---

## Purpose

This directory holds invalid JSON fixtures for the `evidence_bundle` evidence contract.

Use this lane to verify that the schema rejects incomplete or malformed EvidenceBundle-like objects. Each invalid fixture may pair with a `.expected_error.txt` file when the test harness should assert a specific error-message fragment.

---

## Current inventory

| Fixture | Invalid because | Expected error |
|---|---|---|
| [`invalid_1.json`](invalid_1.json) | It matches the positive fixture shape except it omits the required `bundle_id` field. | [`invalid_1.expected_error.txt`](invalid_1.expected_error.txt): `required` |

The expected-error file currently uses a broad matcher. A future fixture tightening pass may choose to replace it with an exact message such as a missing-`bundle_id` required-property error after confirming JSON Schema error wording and test stability.

---

## Schema basis

The current schema evidence for this fixture lane is:

```text
schemas/contracts/v1/evidence/evidence_bundle.schema.json
```

Relevant shape:

| Field | Requirement |
|---|---|
| Root type | object |
| Required fields | `bundle_id`, `claim_scope`, `evidence_refs`, `source_records`, `citations`, `rights`, `sensitivity`, `transforms`, `checksums`, `spec_hash` |
| `bundle_id` | string matching `^[a-z][a-z0-9_:.-]*$` |
| `evidence_refs` | array, `minItems: 1`, items reference `evidence_ref.schema.json` |
| `source_records` | array of strings, `minItems: 1` |
| `citations` | array of strings, `minItems: 1` |
| `rights` | object requiring `license`; no additional properties |
| `sensitivity` | reference to `policy/sensitivity_label.schema.json` |
| `checksums` | object with at least one property; values match `^sha256:[a-f0-9]{64}$` |
| `spec_hash` | reference to `common/spec_hash.schema.json` |
| Additional properties | false |
| Schema-declared fixtures root | `fixtures/contracts/v1/evidence/evidence_bundle/` |
| Dedicated validator path | `tools/validators/validate_evidence_bundle.py` |
| Schema status in metadata | `PROPOSED` |

---

## Test harness behavior

`tests/schemas/test_common_contracts.py` includes the `evidence` family in its fixture sweep and discovers schema fixture families under:

```text
fixtures/contracts/v1/<family>/<name>/
```

For each invalid fixture matching `invalid/invalid_*.json`, the test harness expects JSON Schema validation errors. When a sibling `.expected_error.txt` file exists, the harness lowercases the expected text and checks that each expected non-empty line appears in the combined JSON Schema error messages.

For this directory, `invalid_1.expected_error.txt` currently contains:

```text
required
```

That broad expected line corresponds to the fixture omitting schema-required `bundle_id`.

---

## Accepted material

| Accepted item | Purpose |
|---|---|
| `invalid_*.json` | JSON instances expected to fail `evidence_bundle` schema validation. |
| `invalid_*.expected_error.txt` | Optional expected error fragment for the matching invalid JSON fixture. |
| `README.md` | Local fixture boundary and inventory. |

---

## Exclusions

| Do not place here | Correct home |
|---|---|
| Valid `evidence_bundle` examples | `../valid/` |
| Parent contract fixture guidance | `../README.md` |
| JSON Schema authority | `../../../../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json` |
| Semantic contract documentation | `../../../../../../contracts/evidence/evidence_bundle.md` |
| Validator implementation | `../../../../../../tools/validators/validate_evidence_bundle.py` or accepted validator root |
| Evidence policy rules | `../../../../../../policy/evidence/` |
| Operational EvidenceBundles, ProofPacks, citation validation, proof indexes, or integrity records | Governed proof roots, not fixtures |
| Runtime receipts, release records, source data, or published artifacts | Their canonical KFM roots, not fixtures |

---

## Validation checklist

Before adding or changing invalid fixtures here:

- [ ] The fixture file name follows `invalid_<n>.json`.
- [ ] The fixture is intentionally invalid under `evidence_bundle.schema.json`.
- [ ] The failure reason is narrow and easy to understand.
- [ ] The expected error file, when present, matches the JSON Schema error text closely enough for `tests/schemas/test_common_contracts.py`.
- [ ] The fixture does not redefine the schema, contract, policy, validator, proof model, or release behavior.
- [ ] The fixture does not contain production evidence, real source records, sensitive data, receipts, proofs, release records, or published artifacts.
- [ ] New invalid cases are paired with a matching valid case only when that improves coverage and does not blur fixture purpose.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target path presence | CONFIRMED | `fixtures/contracts/v1/evidence/evidence_bundle/invalid/README.md` existed as a blank file before this update. |
| Invalid fixture inventory | CONFIRMED | `invalid_1.json` exists and omits required `bundle_id`. |
| Expected error inventory | CONFIRMED | `invalid_1.expected_error.txt` exists and contains `required`. |
| Valid sibling example | CONFIRMED | `../valid/valid_1.json` exists and includes `bundle_id`. |
| Schema authority | CONFIRMED | `schemas/contracts/v1/evidence/evidence_bundle.schema.json` defines required fields, refs, checksums, and additional-property behavior. |
| Dedicated validator wrapper | CONFIRMED / NOT RUN | `tools/validators/validate_evidence_bundle.py` exists and invokes the shared JSON Schema runner for this schema and fixture root. |
| Test harness behavior | CONFIRMED / NOT RUN | `tests/schemas/test_common_contracts.py` discovers evidence fixtures and expected-error text, but tests were not run during this README update. |
| Runtime validation results | NOT RUN | This README update did not run validators or pytest. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define fixture boundaries or inventory. |
| [`invalid_1.json`](invalid_1.json) | CONFIRMED | Invalid fixture omits required `bundle_id`. | Only one invalid case is currently verified. |
| [`invalid_1.expected_error.txt`](invalid_1.expected_error.txt) | CONFIRMED | Expected error text is currently `required`. | Broad matcher; could be tightened in a future fixture-quality pass. |
| [`../valid/valid_1.json`](../valid/valid_1.json) | CONFIRMED | Positive comparison case includes `bundle_id` and otherwise similar fields. | Does not prove all valid cases are covered. |
| [`../../../../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json`](../../../../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json) | CONFIRMED | Schema shape, required fields, referenced schemas, checksum pattern, and declared fixtures root. | Schema status is `PROPOSED` in `x-kfm`. |
| [`../../../../../../schemas/contracts/v1/evidence/README.md`](../../../../../../schemas/contracts/v1/evidence/README.md) | CONFIRMED README | Evidence schema parent exists. | It is short and does not inventory all evidence schemas. |
| [`../../../../../../tools/validators/validate_evidence_bundle.py`](../../../../../../tools/validators/validate_evidence_bundle.py) | CONFIRMED | Dedicated validator wrapper points at this schema and fixture root. | Validator was not executed during this README update. |
| [`../../../../../../tests/schemas/test_common_contracts.py`](../../../../../../tests/schemas/test_common_contracts.py) | CONFIRMED | Test harness discovery and expected-error matching behavior. | Tests were not run during this README update. |

[Back to top](#top)
