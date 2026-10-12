<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/runtime/run-receipt/readme
title: run_receipt fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): runtime steward; TODO(owner): schema steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): source steward; TODO(owner): validation steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-06-30 expansion
updated: 2026-06-30
policy_label: public-review
related:
  - valid/README.md
  - valid/valid_1.json
  - invalid/README.md
  - invalid/invalid_1.json
  - invalid/invalid_1.expected_error.txt
  - ../../../../../schemas/contracts/v1/runtime/run_receipt.schema.json
  - ../../../../../contracts/runtime/run_receipt.md
  - ../../../../../contracts/runtime/README.md
  - ../../../../../contracts/runtime/decision_envelope.md
  - ../../../../../contracts/runtime/runtime_response_envelope.md
  - ../../../../../contracts/runtime/ai_receipt.md
  - ../../../../../contracts/evidence/evidence_bundle.md
  - ../../../../../policy/runtime/
  - ../../../../../tools/validators/validate_run_receipt.py
  - ../../../../../tests/schemas/test_common_contracts.py
  - ../../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, v1, runtime, run-receipt, valid-fixtures, invalid-fixtures, expected-error, json-schema, execution-audit, provenance, validation-aware, source-aware, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/contracts/v1/runtime/run_receipt/README.md`."
  - "This directory is the schema-declared fixture root for `run_receipt`."
  - "Fixtures are sample test inputs only; semantic meaning, machine schema shape, executable runtime behavior, validation records, and release authority stay in their owning roots."
  - "Current fixture coverage includes one valid case and one invalid missing-required-field case."
  - "No tests, validators, runtime/pipeline integrations, validation report resolution, source descriptor resolution, receipt persistence checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `run_receipt` fixtures

Fixture family for the KFM `run_receipt` runtime contract schema.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Family: runtime" src="https://img.shields.io/badge/family-runtime-blue">
  <img alt="Contract: run_receipt" src="https://img.shields.io/badge/contract-run__receipt-purple">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
  <img alt="Outcomes: finite" src="https://img.shields.io/badge/outcomes-SUCCESS%20%7C%20PARTIAL%20%7C%20FAIL-informational">
</p>

**Path:** `fixtures/contracts/v1/runtime/run_receipt/README.md`  
**Fixture posture:** JSON Schema valid/invalid fixture family  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/runtime/run_receipt.schema.json`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Schema basis](#schema-basis) · [Authority boundary](#authority-boundary) · [Harness behavior](#harness-behavior) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are schema fixtures. They are not executable pipeline records, validation reports, SourceDescriptors, EvidenceBundles, PolicyDecisions, ReleaseManifests, public-client permissions, release approval, review approval, or publication authority.

---

## Purpose

This directory groups positive and negative JSON fixtures for the `run_receipt` schema.

Use this fixture family to verify that KFM accepts a minimal well-shaped `RunReceipt`-like object and rejects an incomplete one. The schema-declared fixture root is:

```text
fixtures/contracts/v1/runtime/run_receipt/
```

A passing fixture proves schema shape only. It does not prove that a pipeline ran, validation passed, source descriptors resolved, outputs are true, release gates passed, receipt persistence worked, or a public API, map, AI, or UI surface may read the outputs.

---

## Current inventory

| Lane | File | Current role | Status |
|---|---|---|---|
| [`valid/`](valid/README.md) | [`valid_1.json`](valid/valid_1.json) | Minimal positive fixture with every required top-level field, SHA-256 spec hash, reference arrays, and allowed finite `outcome`. | CONFIRMED |
| [`invalid/`](invalid/README.md) | [`invalid_1.json`](invalid/invalid_1.json) | Minimal negative fixture matching the positive case but missing required `run_id`. | CONFIRMED |
| [`invalid/`](invalid/README.md) | [`invalid_1.expected_error.txt`](invalid/invalid_1.expected_error.txt) | Current expected-error matcher: `required`. | CONFIRMED / BROAD MATCHER |

Current positive fixture shape:

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

Current negative fixture shape:

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

The current schema evidence for this fixture family is:

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

## Authority boundary

| Responsibility | Home | Status in this check |
|---|---|---|
| Fixture examples | `fixtures/contracts/v1/runtime/run_receipt/` | CONFIRMED |
| Valid examples | `fixtures/contracts/v1/runtime/run_receipt/valid/` | CONFIRMED |
| Invalid examples | `fixtures/contracts/v1/runtime/run_receipt/invalid/` | CONFIRMED |
| Machine-checkable shape | `schemas/contracts/v1/runtime/run_receipt.schema.json` | CONFIRMED |
| Semantic contract | `contracts/runtime/run_receipt.md` | CONFIRMED |
| Runtime policy | `policy/runtime/` | OUT OF SCOPE FOR THIS README |
| Validator implementation | `tools/validators/validate_run_receipt.py` | NEEDS VERIFICATION |
| Schema test harness | `tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN |

`RunReceipt` must remain distinguishable from:

| Do not collapse `RunReceipt` into | Why |
|---|---|
| Executable runtime or pipeline code | The receipt records a stage execution summary; implementation performs the work elsewhere. |
| Validation report | The receipt references validation records; it does not replace them. |
| `SourceDescriptor` | Source descriptors describe source authority and access posture; the receipt references them. |
| `EvidenceBundle` | Evidence supports claims; a run receipt does not prove claim truth. |
| `PolicyDecision` | Policy decisions govern action; the receipt records what happened in a stage. |
| `ReleaseManifest` | Release manifests bind released contents; a receipt alone cannot publish content. |
| Public-client permission | Public surfaces still require governed API/runtime, policy, evidence, sensitivity, review, and release checks. |

---

## Harness behavior

The common schema test harness discovers contract schemas from:

```text
schemas/contracts/v1/<family>/*.schema.json
```

When a matching fixture directory exists, it expects:

```text
fixtures/contracts/v1/<family>/<schema_name>/valid/valid_*.json
fixtures/contracts/v1/<family>/<schema_name>/invalid/invalid_*.json
fixtures/contracts/v1/<family>/<schema_name>/invalid/invalid_*.expected_error.txt
```

For this runtime family, that means:

```text
fixtures/contracts/v1/runtime/run_receipt/
```

Observed expectations:

| Fixture pattern | Expected result |
|---|---|
| `valid/valid_*.json` | no JSON Schema errors |
| `invalid/invalid_*.json` | at least one JSON Schema error |
| `invalid/invalid_*.expected_error.txt` | expected text appears in combined error messages |

This README documents expected fixture behavior only. It does not claim that pytest, CI, runtime policy, pipeline integration, validation resolution, source descriptor resolution, receipt persistence, or the dedicated RunReceipt validator was run during this update.

---

## Maintenance checklist

Before changing this fixture family:

- [ ] Keep passing examples under `valid/valid_<n>.json`.
- [ ] Keep failing examples under `invalid/invalid_<n>.json`.
- [ ] Keep expected-error text beside the invalid fixture it describes.
- [ ] Keep fixture cases small, deterministic, public-safe, and reviewable.
- [ ] Keep at least one valid minimal fixture and one missing-required-field invalid fixture.
- [ ] Add identifier-pattern, digest-pattern, enum, array-shape, and additional-property fixtures as coverage expands.
- [ ] Avoid private, unpublished, source-system, prompt-like, or policy-restricted content.
- [ ] Keep fixture refs small, deterministic, public-safe, and reviewable.
- [ ] Update fixture docs when schema behavior changes.
- [ ] Verify the validator implementation before claiming validator maturity.
- [ ] Run the relevant schema tests before promotion.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Valid lane | CONFIRMED | `valid/README.md` and `valid/valid_1.json` exist. |
| Invalid lane | CONFIRMED | `invalid/README.md`, `invalid/invalid_1.json`, and `invalid_1.expected_error.txt` exist. |
| Schema | CONFIRMED | `run_receipt.schema.json` defines required fields, digest pattern, finite outcome enum, fixture root, and additional-property behavior. |
| Contract | CONFIRMED | `contracts/runtime/run_receipt.md` defines semantic meaning and separates RunReceipt from executable code, validation proof, EvidenceBundle, PolicyDecision, ReleaseManifest, and public-client permission. |
| Validator file | NEEDS VERIFICATION | `tools/validators/validate_run_receipt.py` is declared by schema but implementation/wiring was not verified during this update. |
| Test execution | NOT RUN | No validators, pytest, runtime policy tests, pipeline checks, validation-resolution checks, source-resolution checks, receipt persistence checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define fixture-family guidance. |
| [`valid/README.md`](valid/README.md) | CONFIRMED | Positive fixture lane guidance. | Does not prove tests were run. |
| [`valid/valid_1.json`](valid/valid_1.json) | CONFIRMED | Current positive fixture includes required fields, digest pattern, refs, and finite `outcome`. | Only one valid fixture is currently documented. |
| [`invalid/README.md`](invalid/README.md) | CONFIRMED | Negative fixture lane guidance. | Does not prove tests were run. |
| [`invalid/invalid_1.json`](invalid/invalid_1.json) | CONFIRMED | Current negative fixture omits required `run_id`. | Only one invalid fixture is currently documented. |
| [`invalid/invalid_1.expected_error.txt`](invalid/invalid_1.expected_error.txt) | CONFIRMED | Current expected-error matcher is `required`. | Broad matcher; may be tightened later. |
| [`../../../../../schemas/contracts/v1/runtime/run_receipt.schema.json`](../../../../../schemas/contracts/v1/runtime/run_receipt.schema.json) | CONFIRMED | Schema shape, required fields, digest pattern, enum values, fixture root, validator path, and status. | Schema status is `PROPOSED`; validator implementation was not verified. |
| [`../../../../../contracts/runtime/run_receipt.md`](../../../../../contracts/runtime/run_receipt.md) | CONFIRMED | Semantic meaning, runtime receipt boundary, field surface, and distinction from validation proof, evidence, policy, release, and public-client authority. | Does not prove runtime/pipeline integration, source descriptor resolution, validation resolution, receipt persistence, validator wiring, or CI status. |
| `../../../../../tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN | Fixture discovery and valid/invalid fixture behavior. | Tests were not run during this update. |
| `../../../../../docs/doctrine/directory-rules.md` | CONFIRMED | `fixtures/` is the root for golden, valid, and invalid test inputs; contracts/schemas/policy split remains separate. | Specific fixture completeness requires tests or inventory. |

[Back to top](#top)
