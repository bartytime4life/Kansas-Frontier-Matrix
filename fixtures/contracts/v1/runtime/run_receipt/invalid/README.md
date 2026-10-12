<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/runtime/run-receipt/invalid/readme
title: run_receipt invalid fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): runtime steward; TODO(owner): schema steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): source steward; TODO(owner): validation steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-06-30 expansion
updated: 2026-06-30
policy_label: public-review
related:
  - ../valid/valid_1.json
  - invalid_1.json
  - invalid_1.expected_error.txt
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
tags: [kfm, fixtures, contracts, v1, runtime, run-receipt, invalid-fixtures, expected-error, json-schema, execution-audit, provenance, validation-aware, source-aware, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/contracts/v1/runtime/run_receipt/invalid/README.md`."
  - "Invalid fixtures are intentionally failing examples for the `run_receipt` schema."
  - "Current invalid fixture coverage is one missing-required-field case: `invalid_1.json` omits `run_id`; expected error matcher is `required`."
  - "No tests, validators, runtime/pipeline integrations, validation report resolution, source descriptor resolution, receipt persistence checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `run_receipt` invalid fixtures

Negative fixture lane for the KFM `run_receipt` runtime contract schema.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Family: runtime" src="https://img.shields.io/badge/family-runtime-blue">
  <img alt="Contract: run_receipt" src="https://img.shields.io/badge/contract-run__receipt-purple">
  <img alt="Lane: invalid" src="https://img.shields.io/badge/lane-invalid-critical">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/contracts/v1/runtime/run_receipt/invalid/README.md`  
**Fixture posture:** invalid JSON Schema fixture lane  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/runtime/run_receipt.schema.json`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Schema basis](#schema-basis) · [Why this fixture fails](#why-this-fixture-fails) · [Authority boundary](#authority-boundary) · [Harness behavior](#harness-behavior) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are expected to fail schema validation. They are not RunReceipts, executable pipeline records, validation reports, SourceDescriptors, EvidenceBundles, PolicyDecisions, ReleaseManifests, public-client permissions, or publication authority.

---

## Purpose

This directory stores negative JSON examples for the `run_receipt` schema.

Use this lane to prove that malformed or incomplete `RunReceipt`-like objects are rejected before they can be treated as accountable runtime or pipeline-stage receipts. Invalid fixtures help preserve KFM's audit boundary: a stage receipt must identify the run, stage, inputs, outputs, code/spec identity, source references, validation references, and finite outcome before downstream review, policy, promotion, release, or correction workflows rely on it.

---

## Current inventory

| File | Role | Expected result | Status |
|---|---|---|---|
| [`invalid_1.json`](invalid_1.json) | Negative fixture missing required `run_id`. | Schema validation should fail. | CONFIRMED |
| [`invalid_1.expected_error.txt`](invalid_1.expected_error.txt) | Expected-error matcher for `invalid_1.json`. | Combined schema errors should include `required`. | CONFIRMED / BROAD MATCHER |

Current invalid fixture:

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

The paired positive fixture currently includes the missing `run_id` field:

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

## Why this fixture fails

`invalid_1.json` omits `run_id`, which is required by the paired schema.

That failure matters because `run_id` is the stable identifier for the stage execution receipt. Without it, downstream audit, validation lookup, source descriptor lookup, correction, rollback, and release review cannot reliably connect a receipt-like payload to the run it describes. A runtime payload with stage, refs, spec hash, and outcome but no stable run identifier must not silently pass as a governed `RunReceipt`.

Expected-error matcher:

```text
required
```

This matcher is intentionally broad. It confirms the missing-field class of failure, but it does not pin the full validator wording. A later fixture pass may tighten it to the exact missing property name once validator output is stable enough.

> [!WARNING]
> A `RunReceipt` is not validation proof by itself, not executable code, not an EvidenceBundle, not a PolicyDecision, not a ReleaseManifest, and not public-client permission. It is an accountability receipt for a governed runtime or pipeline stage.

---

## Authority boundary

| Responsibility | Home | Status in this check |
|---|---|---|
| Negative fixture examples | `fixtures/contracts/v1/runtime/run_receipt/invalid/` | CONFIRMED |
| Positive fixture examples | `fixtures/contracts/v1/runtime/run_receipt/valid/` | CONFIRMED file present / README not checked in this update |
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

For invalid fixtures, the observed harness pattern is:

```text
invalid/invalid_*.json
invalid/invalid_*.expected_error.txt
```

Expected behavior:

| Fixture pattern | Expected result |
|---|---|
| `invalid/invalid_*.json` | At least one JSON Schema error. |
| `invalid/invalid_*.expected_error.txt` | Expected text appears in the combined schema error messages. |

This README documents expected fixture behavior only. It does not claim that pytest, CI, runtime policy, pipeline integration, validation resolution, source descriptor resolution, receipt persistence, or the dedicated RunReceipt validator were run during this update.

---

## Maintenance checklist

Before changing this invalid fixture lane:

- [ ] Keep failing examples under `invalid/invalid_<n>.json`.
- [ ] Keep expected-error text beside the invalid fixture it describes.
- [ ] Keep at least one missing-required-field fixture unless another fixture family covers that failure class.
- [ ] Add identifier-pattern, digest-pattern, enum, array-shape, and additional-property failures when RunReceipt coverage expands.
- [ ] Avoid private, unpublished, source-system, prompt-like, or policy-restricted content.
- [ ] Keep fixture refs small, deterministic, public-safe, and reviewable.
- [ ] Update this README when schema fields, enum values, digest requirements, or expected-error behavior changes.
- [ ] Run the schema fixture test before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Invalid fixture | CONFIRMED | `invalid_1.json` exists and omits required `run_id`. |
| Expected-error file | CONFIRMED | `invalid_1.expected_error.txt` exists and contains `required`. |
| Positive fixture | CONFIRMED | `valid/valid_1.json` exists and includes `run_id`. |
| Schema | CONFIRMED | `run_receipt.schema.json` defines required fields, digest pattern, finite outcome enum, fixture root, and additional-property behavior. |
| Contract | CONFIRMED | `contracts/runtime/run_receipt.md` defines semantic meaning and distinguishes RunReceipt from executable code, validation proof, EvidenceBundle, PolicyDecision, ReleaseManifest, and public-client permission. |
| Test execution | NOT RUN | No validators, pytest, runtime policy tests, pipeline checks, validation-resolution checks, source-resolution checks, receipt persistence checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define invalid-fixture guidance. |
| [`invalid_1.json`](invalid_1.json) | CONFIRMED | Current negative fixture omits required `run_id`. | Only one invalid case is currently documented here. |
| [`invalid_1.expected_error.txt`](invalid_1.expected_error.txt) | CONFIRMED | Current expected-error matcher is `required`. | Broad matcher; may be tightened later. |
| [`../valid/valid_1.json`](../valid/valid_1.json) | CONFIRMED | Paired positive fixture includes `run_id` and other required fields. | Positive lane README was not checked during this update. |
| [`../../../../../../schemas/contracts/v1/runtime/run_receipt.schema.json`](../../../../../../schemas/contracts/v1/runtime/run_receipt.schema.json) | CONFIRMED | Schema shape, required fields, digest pattern, enum values, fixture root, validator path, and status. | Schema status is `PROPOSED`; validator implementation was not verified. |
| [`../../../../../../contracts/runtime/run_receipt.md`](../../../../../../contracts/runtime/run_receipt.md) | CONFIRMED | Semantic meaning, runtime receipt boundary, field surface, and distinction from validation proof, evidence, policy, release, and public-client authority. | Does not prove runtime/pipeline integration, source descriptor resolution, validation resolution, receipt persistence, validator wiring, or CI status. |
| `../../../../../../tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN | Fixture discovery and invalid fixture behavior. | Tests were not run during this update. |
| `../../../../../../docs/doctrine/directory-rules.md` | CONFIRMED | `fixtures/` is the root for golden, valid, and invalid test inputs; contracts/schemas/policy split remains separate. | Specific fixture completeness requires tests or inventory. |

[Back to top](#top)
