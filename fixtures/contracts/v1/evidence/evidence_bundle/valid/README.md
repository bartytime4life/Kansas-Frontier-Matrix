<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/evidence/evidence-bundle/valid/readme
title: evidence_bundle valid fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): schema steward; TODO(owner): evidence contracts steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): evidence steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-06-30 expansion
updated: 2026-06-30
policy_label: public-review
related: [../README.md, valid_1.json, ../invalid/README.md, ../invalid/invalid_1.json, ../invalid/invalid_1.expected_error.txt, ../../../../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json, ../../../../../../schemas/contracts/v1/evidence/README.md, ../../../../../../contracts/evidence/evidence_bundle.md, ../../../../../../tools/validators/validate_evidence_bundle.py, ../../../../../../tests/schemas/test_common_contracts.py]
tags: [kfm, fixtures, contracts, v1, evidence, evidence-bundle, valid-fixtures, json-schema, positive-tests, evidence-bundle-not-proof, non-authoritative]
notes: ["This README replaces a blank file at `fixtures/contracts/v1/evidence/evidence_bundle/valid/README.md`.", "Valid fixtures are intentionally passing inputs for schema enforcement; they are not operational EvidenceBundle authority, proof authority, source truth, contract authority, schema authority, policy authority, release authority, or production data.", "The active schema evidence for this lane is `schemas/contracts/v1/evidence/evidence_bundle.schema.json`; the fixture root is declared in that schema's `x-kfm.fixtures_root`.", "The current valid fixture includes `bundle_id` and all top-level required fields named by the schema.", "The dedicated `tools/validators/validate_evidence_bundle.py` wrapper exists and points at the evidence_bundle schema and fixture root, but this README update did not run it or the pytest harness."]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `evidence_bundle` valid fixtures

Intentional positive fixtures for the KFM `evidence_bundle` evidence contract.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Contract family: evidence" src="https://img.shields.io/badge/family-evidence-blue">
  <img alt="Contract: evidence_bundle" src="https://img.shields.io/badge/contract-evidence__bundle-purple">
  <img alt="Fixture kind: valid" src="https://img.shields.io/badge/fixture-valid-2ea44f">
</p>

**Path:** `fixtures/contracts/v1/evidence/evidence_bundle/valid/README.md`  
**Fixture posture:** positive JSON Schema fixture lane  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/evidence/evidence_bundle.schema.json`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Schema basis](#schema-basis) · [Test harness behavior](#test-harness-behavior) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Validation checklist](#validation-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are expected to pass validation. They are not operational EvidenceBundles, ProofPacks, source data, proof records, receipts, policy decisions, release decisions, or contract/schema authority.

> [!CAUTION]
> `evidence_bundle` fixture examples may look like proof objects, but fixture placement does not make them proof. Operational proof support belongs under governed proof roots with provenance, policy, validation, review, release/correction/rollback context, and auditable support.

---

## Purpose

This directory holds valid JSON fixtures for the `evidence_bundle` evidence contract.

Use this lane to verify that the schema accepts a minimal EvidenceBundle-like object containing the required top-level fields, valid checksum/spec-hash shapes, rights metadata, sensitivity metadata, source/citation refs, and at least one evidence reference.

---

## Current inventory

| Fixture | Valid because | Notes |
|---|---|---|
| [`valid_1.json`](valid_1.json) | Includes `bundle_id` plus all required top-level fields named by `evidence_bundle.schema.json`. | Minimal positive case paired with `../invalid/invalid_1.json`, which omits `bundle_id`. |

Current `valid_1.json` includes:

| Field | Example value or shape |
|---|---|
| `bundle_id` | `bundle:1` |
| `claim_scope` | `route abstain` |
| `evidence_refs` | one object with `ref: obs:1` and `kind: measurement` |
| `source_records` | one string: `src1` |
| `citations` | one string: `cite1` |
| `rights.license` | `CC-BY-4.0` |
| `sensitivity` | public label with reason and applied timestamp |
| `transforms` | one string: `normalize` |
| `checksums.bundle` | `sha256:` plus 64 lowercase hex characters |
| `spec_hash.value` | `sha256:` plus 64 lowercase hex characters |

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

For each valid fixture matching `valid/valid_*.json`, the test harness loads the matching schema and asserts that JSON Schema validation produces no errors.

For this directory, `valid_1.json` is intentionally minimal:

```json
{
  "bundle_id": "bundle:1",
  "claim_scope": "route abstain",
  "evidence_refs": [
    {
      "ref": "obs:1",
      "kind": "measurement"
    }
  ],
  "source_records": ["src1"],
  "citations": ["cite1"],
  "rights": {
    "license": "CC-BY-4.0"
  },
  "sensitivity": {
    "level": "public",
    "reason": "open",
    "applied_at": "2026-05-09T00:00:00Z"
  },
  "transforms": ["normalize"],
  "checksums": {
    "bundle": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  },
  "spec_hash": {
    "value": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  }
}
```

This README documents expected fixture behavior. It does not claim that pytest or the dedicated validator wrapper was run during this update.

---

## Accepted material

| Accepted item | Purpose |
|---|---|
| `valid_*.json` | JSON instances expected to pass `evidence_bundle` schema validation. |
| `README.md` | Local fixture boundary and inventory. |

---

## Exclusions

| Do not place here | Correct home |
|---|---|
| Invalid `evidence_bundle` examples | `../invalid/` |
| Expected error text files | `../invalid/` with matching invalid fixtures |
| Parent contract fixture guidance | `../README.md` |
| JSON Schema authority | `../../../../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json` |
| Semantic contract documentation | `../../../../../../contracts/evidence/evidence_bundle.md` |
| Validator implementation | `../../../../../../tools/validators/validate_evidence_bundle.py` or accepted validator root |
| Evidence policy rules | `../../../../../../policy/evidence/` |
| Operational EvidenceBundles, ProofPacks, citation validation, proof indexes, or integrity records | Governed proof roots, not fixtures |
| Runtime receipts, release records, source data, production hashes, or published artifacts | Their canonical KFM roots, not fixtures |

---

## Validation checklist

Before adding or changing valid fixtures here:

- [ ] The fixture file name follows `valid_<n>.json`.
- [ ] The fixture is intentionally valid under `evidence_bundle.schema.json`.
- [ ] The fixture includes every required top-level field named by the schema.
- [ ] `evidence_refs`, `source_records`, and `citations` are non-empty arrays.
- [ ] `rights` includes `license` and does not include extra properties unless the schema changes first.
- [ ] `checksums` has at least one property and each value matches `^sha256:[a-f0-9]{64}$`.
- [ ] `spec_hash` satisfies the common `spec_hash` contract.
- [ ] The fixture does not redefine the schema, contract, policy, validator, proof model, or release behavior.
- [ ] The fixture does not contain production evidence, real source records, sensitive data, receipts, proofs, release records, or published artifacts.
- [ ] New valid cases are paired with invalid cases only when that improves coverage and does not blur fixture purpose.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target path presence | CONFIRMED | `fixtures/contracts/v1/evidence/evidence_bundle/valid/README.md` existed as a blank file before this update. |
| Valid fixture inventory | CONFIRMED | `valid_1.json` exists and includes `bundle_id` plus all top-level required fields. |
| Invalid sibling lane | CONFIRMED | `../invalid/README.md` documents the current invalid fixture and broad expected error matcher. |
| Schema authority | CONFIRMED | `schemas/contracts/v1/evidence/evidence_bundle.schema.json` defines required fields, refs, checksums, and additional-property behavior. |
| Dedicated validator wrapper | CONFIRMED / NOT RUN | `tools/validators/validate_evidence_bundle.py` exists and invokes the shared JSON Schema runner for this schema and fixture root. |
| Test harness behavior | CONFIRMED / NOT RUN | `tests/schemas/test_common_contracts.py` discovers evidence fixtures and validates valid fixtures by asserting no schema errors. |
| Runtime validation results | NOT RUN | This README update did not run validators or pytest. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define fixture boundaries or inventory. |
| [`valid_1.json`](valid_1.json) | CONFIRMED | Positive fixture includes `bundle_id` and all required top-level fields. | Only one valid case is currently verified. |
| [`../invalid/README.md`](../invalid/README.md) | CONFIRMED | Sibling invalid fixture documentation and schema/test boundary pattern. | Does not prove valid fixture behavior by itself. |
| [`../invalid/invalid_1.json`](../invalid/invalid_1.json) | CONFIRMED | Negative comparison case omits required `bundle_id`. | Belongs to invalid lane, not valid lane. |
| [`../../../../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json`](../../../../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json) | CONFIRMED | Schema shape, required fields, referenced schemas, checksum pattern, and declared fixtures root. | Schema status is `PROPOSED` in `x-kfm`. |
| [`../../../../../../tools/validators/validate_evidence_bundle.py`](../../../../../../tools/validators/validate_evidence_bundle.py) | CONFIRMED | Dedicated validator wrapper points at this schema and fixture root. | Validator was not executed during this README update. |
| [`../../../../../../tests/schemas/test_common_contracts.py`](../../../../../../tests/schemas/test_common_contracts.py) | CONFIRMED | Test harness discovery and valid-fixture behavior. | Tests were not run during this README update. |

[Back to top](#top)
