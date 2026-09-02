<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/runtime/run-receipt/valid/readme
title: run_receipt valid fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): runtime steward; TODO(owner): schema steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): source steward; TODO(owner): validation steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-06-30 expansion
updated: 2026-06-30
policy_label: public-review
related:
  - valid_1.json
  - ../invalid/README.md
  - ../invalid/invalid_1.json
  - ../invalid/invalid_1.expected_error.txt
  - ../../../../../../schemas/contracts/v1/runtime/run_receipt.schema.json
  - ../../../../../../contracts/runtime/run_receipt.md
  - ../../../../../../contracts/runtime/README.md
  - ../../../../../../contracts/runtime/decision_envelope.md
  - ../../../../../../contracts/runtime/runtime_response_envelope.md
  - ../../../../../../contracts/runtime/ai_receipt.md
  - ../../../../../../contracts/evidence/evidence_bundle.md
  - ../../../../../../policy/runtime/
  - ../../../../../../tools/validators/validate_run_receipt.py
  - ../../../../../../tests/schemas/test_common_contracts.py
  - ../../../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, v1, runtime, run-receipt, valid-fixtures, json-schema, execution-audit, provenance, validation-aware, source-aware, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/contracts/v1/runtime/run_receipt/valid/README.md`."
  - "Valid fixtures are positive schema examples for the `run_receipt` schema."
  - "Current valid fixture coverage is one minimal passing case: `valid_1.json`."
  - "No tests, validators, runtime/pipeline integrations, validation report resolution, source descriptor resolution, receipt persistence checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `run_receipt` valid fixtures

Positive fixture lane for the KFM `run_receipt` runtime contract schema.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Family: runtime" src="https://img.shields.io/badge/family-runtime-blue">
  <img alt="Contract: run_receipt" src="https://img.shields.io/badge/contract-run__receipt-purple">
  <img alt="Lane: valid" src="https://img.shields.io/badge/lane-valid-success">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/contracts/v1/runtime/run_receipt/valid/README.md`  
**Fixture posture:** valid JSON Schema fixture lane  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/runtime/run_receipt.schema.json`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Schema basis](#schema-basis) · [Why this fixture passes](#why-this-fixture-passes) · [Authority boundary](#authority-boundary) · [Harness behavior](#harness-behavior) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are expected to pass schema validation. They are not executable pipeline records, validation reports, SourceDescriptors, EvidenceBundles, PolicyDecisions, ReleaseManifests, public-client permissions, or publication authority.

---

## Purpose

This directory stores positive JSON examples for the `run_receipt` schema.

Use this lane to prove that a minimal well-shaped `RunReceipt`-like object can pass schema validation before it is used by higher-level runtime, validation, source, policy, review, promotion, release, correction, or publication workflows. Passing this schema fixture only proves shape. It does not prove that a pipeline ran, validation passed, source descriptors resolved, outputs are true, release gates passed, or a public client may read the outputs.

---

## Current inventory

| File | Role | Expected result | Status |
|---|---|---|---|
| [`valid_1.json`](valid_1.json) | Minimal positive fixture for `run_receipt`. | Schema validation should pass. | CONFIRMED |

Current valid fixture:

```json
{
  "run_id": "run1",
  "stage": "ingest",
  "inputs": ["in1"],
  "outputs": ["out1"],
  "code_ref": "git:abc",
  "spec_hash": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "source_descriptor_refs": ["src1"],
  "validation_refs": ["val1"],
  "outcome": "SUCCESS"
}
```

The paired negative fixture currently omits the required `run_id` field and is expected to fail with a `required` error:

```json
{
  "stage": "ingest",
  "inputs": ["in1"],
  "outputs": ["out1"],
  "code_ref": "git:abc",
  "spec_hash": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "source_descriptor_refs": ["src1"],
  "validation_refs": ["val1"],
  "outcome": "SUCCESS"
}
```

---

## Schema basis

The current schema evidence for this fixture lane is:

```text
schemas/contracts/v1/runtime/run_receipt.schema.json
```

Confirmed schema facts:

| Item | Value |
|---|---|
| Schema title | `run_receipt` |
| Root type | object |
| Required fields | `run_id`, `stage`, `inputs`, `outputs`, `code_ref`, `spec_hash`, `source_descriptor_refs`, `validation_refs`, `outcome` |
| `run_id` | string matching `^[a-z][a-z0-9_:.-]*$` |
| `inputs` | array of strings |
| `outputs` | array of strings |
| `spec_hash` | string matching `^sha256:[a-f0-9]{64}$` |
| `source_descriptor_refs` | array of strings |
| `validation_refs` | array of strings |
| `outcome` enum values | `SUCCESS`, `PARTIAL`, `FAIL` |
| Additional properties | false |
| Declared contract doc | `contracts/runtime/run_receipt.md` |
| Declared fixture root | `fixtures/contracts/v1/runtime/run_receipt/` |
| Declared validator | `tools/validators/validate_run_receipt.py` |
| Declared policy path | `policy/runtime/` |
| Schema status | `PROPOSED` |

---

## Why this fixture passes

`valid_1.json` includes every field currently required by the paired schema:

- `run_id`
- `stage`
- `inputs`
- `outputs`
- `code_ref`
- `spec_hash`
- `source_descriptor_refs`
- `validation_refs`
- `outcome`

It also uses schema-compatible values:

| Field | Fixture value | Schema posture |
|---|---|---|
| `run_id` | `run1` | Matches identifier pattern. |
| `stage` | `ingest` | String. |
| `inputs` | `["in1"]` | Array of strings. |
| `outputs` | `["out1"]` | Array of strings. |
| `spec_hash` | `sha256:` plus 64 lowercase hex characters | Matches SHA-256 digest pattern. |
| `source_descriptor_refs` | `["src1"]` | Array of strings. |
| `validation_refs` | `["val1"]` | Array of strings. |
| `outcome` | `SUCCESS` | Allowed finite run outcome. |

This positive fixture is intentionally minimal. It proves the schema accepts a compact RunReceipt object, not that the receipt is persisted, validation-backed, source-resolved, release-approved, or safe for public-client use.

> [!WARNING]
> A `RunReceipt` is not validation proof by itself, not executable code, not an EvidenceBundle, not a PolicyDecision, not a ReleaseManifest, and not public-client permission. It is an accountability receipt for a governed runtime or pipeline stage.

---

## Authority boundary

| Responsibility | Home | Status in this check |
|---|---|---|
| Positive fixture examples | `fixtures/contracts/v1/runtime/run_receipt/valid/` | CONFIRMED |
| Negative fixture examples | `fixtures/contracts/v1/runtime/run_receipt/invalid/` | CONFIRMED |
| Machine-checkable shape | `schemas/contracts/v1/runtime/run_receipt.schema.json` | CONFIRMED |
| Semantic contract | `contracts/runtime/run_receipt.md` | CONFIRMED |
| Runtime policy | `policy/runtime/` | OUT OF SCOPE FOR THIS README |
| Validator implementation | `tools/validators/validate_run_receipt.py` | NEEDS VERIFICATION |
| Schema test harness | `tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN |

Do not collapse this fixture lane into the semantic contract, schema, executable runtime, validation report, SourceDescriptor, EvidenceBundle, policy decision, release manifest, review record, or receipt persistence layer.

---

## Harness behavior

The common schema test harness discovers fixture families under:

```text
fixtures/contracts/v1/<family>/<name>/
```

For valid fixtures, the observed harness pattern is:

```text
valid/valid_*.json
```

Expected behavior:

| Fixture pattern | Expected result |
|---|---|
| `valid/valid_*.json` | No JSON Schema errors. |

This README documents expected fixture behavior only. It does not claim that pytest, CI, runtime policy, pipeline integration, validation resolution, source descriptor resolution, receipt persistence, or the dedicated RunReceipt validator were run during this update.

---

## Maintenance checklist

Before changing this valid fixture lane:

- [ ] Keep passing examples under `valid/valid_<n>.json`.
- [ ] Keep at least one minimal positive fixture unless the schema family is intentionally retired.
- [ ] Keep positive fixtures paired with negative fixtures under `../invalid/`.
- [ ] Add richer valid fixtures only when they remain public-safe and reviewable.
- [ ] Avoid private, unpublished, source-system, prompt-like, or policy-restricted content.
- [ ] Keep fixture refs small, deterministic, public-safe, and reviewable.
- [ ] Update this README when schema fields, enum values, digest requirements, or fixture coverage changes.
- [ ] Run the schema fixture test before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Valid fixture | CONFIRMED | `valid_1.json` exists and includes all schema-required fields. |
| Invalid lane README | CONFIRMED | `../invalid/README.md` exists and documents the missing-`run_id` negative case. |
| Invalid fixture | CONFIRMED | `../invalid/invalid_1.json` exists and omits required `run_id`. |
| Expected-error file | CONFIRMED | `../invalid/invalid_1.expected_error.txt` exists and contains `required`. |
| Schema | CONFIRMED | `run_receipt.schema.json` defines required fields, digest pattern, finite outcome enum, fixture root, and additional-property behavior. |
| Contract | CONFIRMED | `contracts/runtime/run_receipt.md` defines semantic meaning and distinguishes RunReceipt from executable code, validation proof, EvidenceBundle, PolicyDecision, ReleaseManifest, and public-client permission. |
| Test execution | NOT RUN | No validators, pytest, runtime policy tests, pipeline checks, validation-resolution checks, source-resolution checks, receipt persistence checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define valid-fixture guidance. |
| [`valid_1.json`](valid_1.json) | CONFIRMED | Current positive fixture includes required fields, digest pattern, refs, and finite `outcome`. | Only one valid case is currently documented here. |
| [`../invalid/README.md`](../invalid/README.md) | CONFIRMED | Documents the negative fixture lane. | Does not prove tests were run. |
| [`../invalid/invalid_1.json`](../invalid/invalid_1.json) | CONFIRMED | Paired negative fixture omits required `run_id`. | Only one invalid case is currently documented here. |
| [`../invalid/invalid_1.expected_error.txt`](../invalid/invalid_1.expected_error.txt) | CONFIRMED | Current expected-error matcher is `required`. | Broad matcher; may be tightened later. |
| [`../../../../../../schemas/contracts/v1/runtime/run_receipt.schema.json`](../../../../../../schemas/contracts/v1/runtime/run_receipt.schema.json) | CONFIRMED | Schema shape, required fields, digest pattern, enum values, fixture root, validator path, and status. | Schema status is `PROPOSED`; validator implementation was not verified. |
| [`../../../../../../contracts/runtime/run_receipt.md`](../../../../../../contracts/runtime/run_receipt.md) | CONFIRMED | Semantic meaning, runtime receipt boundary, field surface, and distinction from validation proof, evidence, policy, release, and public-client authority. | Does not prove runtime/pipeline integration, source descriptor resolution, validation resolution, receipt persistence, validator wiring, or CI status. |
| `../../../../../../tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN | Fixture discovery and valid fixture behavior. | Tests were not run during this update. |
| `../../../../../../docs/doctrine/directory-rules.md` | CONFIRMED | `fixtures/` is the root for golden, valid, and invalid test inputs; contracts/schemas/policy split remains separate. | Specific fixture completeness requires tests or inventory. |

[Back to top](#top)
