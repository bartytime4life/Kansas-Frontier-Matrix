<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/source/ingest-receipt/valid/readme
title: ingest_receipt valid fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): source steward; TODO(owner): ingest steward; TODO(owner): schema steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-07-01 expansion
updated: 2026-07-01
policy_label: public-review
related:
  - valid_1.json
  - ../invalid/README.md
  - ../invalid/invalid_1.json
  - ../invalid/invalid_1.expected_error.txt
  - ../../../../../../schemas/contracts/v1/source/ingest_receipt.schema.json
  - ../../../../../../contracts/source/ingest_receipt.md
  - ../../../../../../contracts/source/source_descriptor.md
  - ../../../../../../contracts/runtime/run_receipt.md
  - ../../../../../../policy/source/
  - ../../../../../../tools/validators/validate_ingest_receipt.py
  - ../../../../../../tests/schemas/test_common_contracts.py
  - ../../../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, v1, source, ingest-receipt, valid-fixtures, json-schema, source-ingest, receipt, sha256, lifecycle, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/contracts/v1/source/ingest_receipt/valid/README.md`."
  - "Valid fixtures are positive schema examples for the `ingest_receipt` schema."
  - "Current valid fixture coverage is one minimal passing case: `valid_1.json`."
  - "No tests, validators, source ingest workflows, source registry checks, policy checks, release checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `ingest_receipt` valid fixtures

Positive fixture lane for the KFM `ingest_receipt` source contract schema.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Family: source" src="https://img.shields.io/badge/family-source-blue">
  <img alt="Contract: ingest_receipt" src="https://img.shields.io/badge/contract-ingest__receipt-purple">
  <img alt="Lane: valid" src="https://img.shields.io/badge/lane-valid-success">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/contracts/v1/source/ingest_receipt/valid/README.md`  
**Fixture posture:** valid JSON Schema fixture lane  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/source/ingest_receipt.schema.json`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Schema basis](#schema-basis) · [Why this fixture passes](#why-this-fixture-passes) · [Authority boundary](#authority-boundary) · [Harness behavior](#harness-behavior) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are expected to pass schema validation. They are not source ingest workflow proof, source truth, SourceDescriptors, RunReceipts, EvidenceBundles, PolicyDecisions, ReleaseManifests, release approval, or publication authority.

---

## Purpose

This directory stores positive JSON examples for the `ingest_receipt` schema.

Use this lane to prove that a minimal well-shaped `IngestReceipt`-like object can pass schema validation before it is used by higher-level source ingest, source registry, validation, policy, release, documentation, or pipeline workflows. Passing this schema fixture only proves shape. It does not prove that source material was actually captured, that digests were computed from real payloads, that source policy allows downstream use, or that any lifecycle transition is approved.

---

## Current inventory

| File | Role | Expected result | Status |
|---|---|---|---|
| [`valid_1.json`](valid_1.json) | Minimal positive fixture for `ingest_receipt`. | Schema validation should pass. | CONFIRMED |

Current valid fixture:

```json
{
  "id": "ing1",
  "source_id": "src1",
  "run_id": "run1",
  "started_at": "2026-05-09T00:00:00Z",
  "finished_at": "2026-05-09T00:10:00Z",
  "outcome": "SUCCESS",
  "bytes_in": 12,
  "digests": {
    "raw": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  }
}
```

The paired negative fixture currently omits required `id`:

```json
{
  "source_id": "src1",
  "run_id": "run1",
  "started_at": "2026-05-09T00:00:00Z",
  "finished_at": "2026-05-09T00:10:00Z",
  "outcome": "SUCCESS",
  "bytes_in": 12,
  "digests": {
    "raw": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  }
}
```

---

## Schema basis

The current schema evidence for this fixture lane is:

```text
schemas/contracts/v1/source/ingest_receipt.schema.json
```

Confirmed schema facts:

| Item | Value |
|---|---|
| Schema title | `ingest_receipt` |
| Root type | object |
| Required fields | `id`, `source_id`, `run_id`, `started_at`, `finished_at`, `outcome`, `bytes_in`, `digests` |
| `id` | string matching `^[a-z][a-z0-9_:.-]*$` |
| `started_at` / `finished_at` | strings with `date-time` format |
| `outcome` enum values | `SUCCESS`, `PARTIAL`, `FAIL` |
| `bytes_in` | integer with minimum `0` |
| `digests` | object with at least one property |
| digest values | strings matching `^sha256:[a-f0-9]{64}$` |
| Additional properties | false |
| Declared contract doc | `contracts/source/ingest_receipt.md` |
| Declared fixture root | `fixtures/contracts/v1/source/ingest_receipt/` |
| Declared validator | `tools/validators/validate_ingest_receipt.py` |
| Declared policy path | `policy/source/` |
| Schema status | `PROPOSED` |

---

## Why this fixture passes

`valid_1.json` includes every field currently required by the paired schema:

- `id`
- `source_id`
- `run_id`
- `started_at`
- `finished_at`
- `outcome`
- `bytes_in`
- `digests`

It also uses schema-compatible values:

| Field | Fixture value | Schema posture |
|---|---|---|
| `id` | `ing1` | Matches `^[a-z][a-z0-9_:.-]*$`. |
| `source_id` | `src1` | String. |
| `run_id` | `run1` | String. |
| `started_at` | `2026-05-09T00:00:00Z` | JSON Schema `date-time` string. |
| `finished_at` | `2026-05-09T00:10:00Z` | JSON Schema `date-time` string. |
| `outcome` | `SUCCESS` | Allowed finite outcome value. |
| `bytes_in` | `12` | Integer greater than or equal to `0`. |
| `digests.raw` | `sha256:` plus 64 lowercase hexadecimal characters | Matches digest pattern. |

This positive fixture is intentionally minimal. It proves the schema accepts a compact ingest-receipt object, not that the described ingest actually ran, not that `source_id` resolves, not that digest values were computed from source material, and not that captured material is admissible or publishable.

> [!WARNING]
> `IngestReceipt` records a source ingest or capture event. It is not source truth, not a source descriptor, not a runtime run receipt, not validation proof, not a policy decision, and not release or publication approval.

---

## Authority boundary

| Responsibility | Home | Status in this check |
|---|---|---|
| Positive fixture examples | `fixtures/contracts/v1/source/ingest_receipt/valid/` | CONFIRMED |
| Negative fixture examples | `fixtures/contracts/v1/source/ingest_receipt/invalid/` | CONFIRMED |
| Machine-checkable shape | `schemas/contracts/v1/source/ingest_receipt.schema.json` | CONFIRMED |
| Semantic contract | `contracts/source/ingest_receipt.md` | CONFIRMED |
| Source policy | `policy/source/` | OUT OF SCOPE FOR THIS README |
| Dedicated validator implementation | `tools/validators/validate_ingest_receipt.py` | NEEDS VERIFICATION |
| Common schema fixture harness | `tests/schemas/test_common_contracts.py` | CONFIRMED doctrine pattern from prior fixture work / NOT RUN |

Do not collapse this fixture lane into the semantic contract, schema, source registry, ingest workflow, SourceDescriptor, RunReceipt, EvidenceBundle, ValidationReport, PolicyDecision, ReleaseManifest, source truth, or publication authority.

---

## Harness behavior

The common schema fixture convention for contract fixtures is:

```text
fixtures/contracts/v1/<family>/<name>/
```

For valid fixtures, the expected pattern is:

```text
valid/valid_*.json
```

Expected behavior:

| Fixture pattern | Expected result |
|---|---|
| `valid/valid_*.json` | No JSON Schema errors. |

This README documents expected fixture behavior only. It does not claim that pytest, CI, source ingest policy, source registry resolution, lifecycle transition checks, release checks, or the dedicated IngestReceipt validator were run during this update.

---

## Maintenance checklist

Before changing this valid fixture lane:

- [ ] Keep passing examples under `valid/valid_<n>.json`.
- [ ] Keep at least one minimal positive fixture unless the schema family is intentionally retired.
- [ ] Keep positive fixtures paired with negative fixtures under `../invalid/`.
- [ ] Add multi-digest, partial-outcome, fail-outcome, zero-byte, and richer metadata-safe valid examples when coverage expands.
- [ ] Keep digest values shaped as `sha256:<64 lowercase hex>` unless the schema changes.
- [ ] Use only allowed `outcome` values: `SUCCESS`, `PARTIAL`, or `FAIL`.
- [ ] Keep fixture examples public-safe and limited to receipt-shaped metadata.
- [ ] Avoid private, unpublished, source-system, prompt-like, or policy-restricted content.
- [ ] Do not embed full source payloads or release-blocked material in fixtures.
- [ ] Update this README when schema fields, enum values, digest requirements, ingest metadata expectations, or fixture coverage changes.
- [ ] Run the schema fixture test before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Valid fixture | CONFIRMED | `valid_1.json` exists and includes all schema-required fields. |
| Invalid lane README | CONFIRMED | `../invalid/README.md` exists and documents the missing-required-field case. |
| Invalid fixture | CONFIRMED | `../invalid/invalid_1.json` exists and omits required `id`. |
| Expected-error file | CONFIRMED | `../invalid/invalid_1.expected_error.txt` exists and contains `required`. |
| Schema | CONFIRMED | `ingest_receipt.schema.json` defines required fields, identifier pattern, date-time fields, finite outcome enum, byte minimum, digest object, digest pattern, declared fixture root, declared validator, declared policy path, and additional-property behavior. |
| Contract | CONFIRMED | `contracts/source/ingest_receipt.md` defines semantic meaning and distinguishes IngestReceipt from SourceDescriptor, RunReceipt, ValidationReport, EvidenceBundle, PolicyDecision, ReleaseManifest, and source raw data. |
| Test execution | NOT RUN | No validators, pytest, source policy checks, source registry checks, ingest workflow checks, lifecycle transition checks, release checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define valid-fixture guidance. |
| [`valid_1.json`](valid_1.json) | CONFIRMED | Current positive fixture includes all required fields and schema-compatible values. | Only one valid case is currently documented here. |
| [`../invalid/README.md`](../invalid/README.md) | CONFIRMED | Documents the negative fixture lane. | Does not prove tests were run. |
| [`../invalid/invalid_1.json`](../invalid/invalid_1.json) | CONFIRMED | Paired negative fixture omits required `id`. | Only one invalid case is currently documented there. |
| [`../invalid/invalid_1.expected_error.txt`](../invalid/invalid_1.expected_error.txt) | CONFIRMED | Expected matcher is `required`. | Broad matcher; may be tightened later. |
| [`../../../../../../schemas/contracts/v1/source/ingest_receipt.schema.json`](../../../../../../schemas/contracts/v1/source/ingest_receipt.schema.json) | CONFIRMED | Schema shape, required fields, identifier pattern, date-time fields, outcome enum, byte minimum, digest object, digest value pattern, fixture root, validator path, policy path, and status. | Schema status is `PROPOSED`; validator implementation was not verified. |
| [`../../../../../../contracts/source/ingest_receipt.md`](../../../../../../contracts/source/ingest_receipt.md) | CONFIRMED | Semantic meaning, source-ingest lifecycle role, field surface, invariants, and boundary against source truth, RunReceipt, ValidationReport, EvidenceBundle, PolicyDecision, ReleaseManifest, and source raw data. | Does not prove ingest workflow, source registry resolution, validator wiring, policy behavior, release checks, or CI status. |
| `../../../../../../docs/doctrine/directory-rules.md` | CONFIRMED doctrine | `fixtures/` is within the validate/operate authority surface and supports test inputs while contracts, schemas, policy, and lifecycle data remain separate roots. | Specific fixture completeness requires inventory and tests. |

[Back to top](#top)
