<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/source/ingest-receipt/readme
title: ingest_receipt fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): source steward; TODO(owner): ingest steward; TODO(owner): schema steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-07-01 expansion
updated: 2026-07-01
policy_label: public-review
related:
  - valid/README.md
  - valid/valid_1.json
  - invalid/README.md
  - invalid/invalid_1.json
  - invalid/invalid_1.expected_error.txt
  - ../../../../../schemas/contracts/v1/source/ingest_receipt.schema.json
  - ../../../../../contracts/source/ingest_receipt.md
  - ../../../../../contracts/source/source_descriptor.md
  - ../../../../../contracts/runtime/run_receipt.md
  - ../../../../../policy/source/
  - ../../../../../tools/validators/validate_ingest_receipt.py
  - ../../../../../tests/schemas/test_common_contracts.py
  - ../../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, v1, source, ingest-receipt, valid-fixtures, invalid-fixtures, expected-error, json-schema, source-ingest, receipt, sha256, lifecycle, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/contracts/v1/source/ingest_receipt/README.md`."
  - "This directory is the fixture family for `ingest_receipt`."
  - "Fixtures are sample test inputs only; semantic meaning, schema shape, source ingest, policy behavior, lifecycle transitions, and release authority stay in their owning roots."
  - "Current fixture coverage includes one valid case and one invalid missing-required-field case."
  - "No tests, validators, source ingest workflows, source registry checks, policy checks, release checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `ingest_receipt` fixtures

Fixture family for the KFM `ingest_receipt` source contract schema.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Family: source" src="https://img.shields.io/badge/family-source-blue">
  <img alt="Contract: ingest_receipt" src="https://img.shields.io/badge/contract-ingest__receipt-purple">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
  <img alt="Integrity: SHA-256" src="https://img.shields.io/badge/integrity-SHA--256-informational">
</p>

**Path:** `fixtures/contracts/v1/source/ingest_receipt/README.md`  
**Fixture posture:** JSON Schema valid/invalid fixture family  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/source/ingest_receipt.schema.json`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Schema basis](#schema-basis) · [Authority boundary](#authority-boundary) · [Harness behavior](#harness-behavior) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are schema fixtures. They are not source ingest workflow proof, source truth, SourceDescriptors, RunReceipts, EvidenceBundles, ValidationReports, PolicyDecisions, ReleaseManifests, release approval, review approval, or publication authority.

---

## Purpose

This directory groups positive and negative JSON fixtures for the `ingest_receipt` schema.

Use this fixture family to verify that KFM accepts a minimal well-shaped `IngestReceipt`-like object and rejects receipt-shaped metadata that lacks a required stable identifier. The fixture family helps protect KFM's source-ingest boundary by keeping ingest receipt shape testable without turning fixture examples into real ingest workflow proof, source truth, policy approval, release approval, or permission for public clients to read lifecycle-internal source material.

A passing fixture proves schema shape only. It does not prove the described ingest actually ran, `source_id` resolves to a governed source descriptor, digest values were computed from real captured material, source policy allows downstream use, or any lifecycle transition is approved.

---

## Current inventory

| Lane | File | Current role | Status |
|---|---|---|---|
| [`valid/`](valid/README.md) | [`valid_1.json`](valid/valid_1.json) | Minimal positive fixture with every required field, valid date-time values, allowed `SUCCESS` outcome, nonnegative `bytes_in`, and one SHA-256 digest value. | CONFIRMED |
| [`invalid/`](invalid/README.md) | [`invalid_1.json`](invalid/invalid_1.json) | Negative fixture missing required `id`. | CONFIRMED |
| [`invalid/`](invalid/README.md) | [`invalid_1.expected_error.txt`](invalid/invalid_1.expected_error.txt) | Expected-error matcher currently set to `required`. | CONFIRMED |

Current positive fixture shape:

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

Current negative fixture shape:

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

The current schema evidence for this fixture family is:

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

## Authority boundary

| Responsibility | Home | Status in this check |
|---|---|---|
| Fixture examples | `fixtures/contracts/v1/source/ingest_receipt/` | CONFIRMED |
| Valid examples | `fixtures/contracts/v1/source/ingest_receipt/valid/` | CONFIRMED |
| Invalid examples | `fixtures/contracts/v1/source/ingest_receipt/invalid/` | CONFIRMED |
| Machine-checkable shape | `schemas/contracts/v1/source/ingest_receipt.schema.json` | CONFIRMED |
| Semantic contract | `contracts/source/ingest_receipt.md` | CONFIRMED |
| Source policy | `policy/source/` | OUT OF SCOPE FOR THIS README |
| Dedicated validator implementation | `tools/validators/validate_ingest_receipt.py` | NEEDS VERIFICATION |
| Common schema fixture harness | `tests/schemas/test_common_contracts.py` | CONFIRMED doctrine pattern from prior fixture work / NOT RUN |

`IngestReceipt` must remain distinguishable from:

| Do not collapse `IngestReceipt` into | Why |
|---|---|
| SourceDescriptor | SourceDescriptor governs source identity, role, rights, and sensitivity; IngestReceipt records a capture event. |
| RunReceipt | RunReceipt summarizes broader runtime or pipeline execution; IngestReceipt is source-ingest-specific. |
| ValidationReport | ValidationReport owns validation pass/fail details; IngestReceipt pins captured inputs. |
| EvidenceBundle | EvidenceBundle supports claims; IngestReceipt supports source-capture provenance. |
| PolicyDecision | Policy decides admissibility; receipt records ingest outcome. |
| ReleaseManifest | ReleaseManifest binds published artifacts; ingest receipt does not publish. |
| Source raw data | Receipt contains metadata and digests, not the source payload itself. |
| Publication authority | Publication still requires governed release, review, policy, provenance, and rollback posture. |

---

## Harness behavior

The common schema fixture convention for contract fixtures is:

```text
fixtures/contracts/v1/<family>/<name>/
```

For this source family, that means:

```text
fixtures/contracts/v1/source/ingest_receipt/
```

Expected fixture layout:

```text
fixtures/contracts/v1/source/ingest_receipt/
  README.md
  valid/
    README.md
    valid_1.json
  invalid/
    README.md
    invalid_1.json
    invalid_1.expected_error.txt
```

Observed expectations:

| Fixture pattern | Expected result |
|---|---|
| `valid/valid_*.json` | no JSON Schema errors |
| `invalid/invalid_*.json` | at least one JSON Schema error |
| `invalid/invalid_*.expected_error.txt` | expected text appears in combined schema error messages |

This README documents expected fixture behavior only. It does not claim that pytest, CI, source ingest policy, source registry resolution, lifecycle transition checks, release checks, or the dedicated IngestReceipt validator was run during this update.

---

## Maintenance checklist

Before changing this fixture family:

- [ ] Keep passing examples under `valid/valid_<n>.json`.
- [ ] Keep failing examples under `invalid/invalid_<n>.json`.
- [ ] Keep expected-error text beside the invalid fixture it describes.
- [ ] Keep at least one minimal positive fixture and one missing-required-field invalid fixture.
- [ ] Add id-pattern, digest-pattern, empty-digests, outcome-enum, date-time, bytes-minimum, additional-property, multi-digest, partial-outcome, fail-outcome, and zero-byte cases as coverage expands.
- [ ] Keep digest values shaped as `sha256:<64 lowercase hex>` unless the schema changes.
- [ ] Use only allowed `outcome` values: `SUCCESS`, `PARTIAL`, or `FAIL`.
- [ ] Keep fixture examples public-safe and limited to receipt-shaped metadata.
- [ ] Avoid private, unpublished, source-system, prompt-like, or policy-restricted content.
- [ ] Do not embed full source payloads or release-blocked material in fixtures.
- [ ] Update parent and lane READMEs when schema fields, enum values, digest requirements, ingest metadata expectations, or fixture coverage changes.
- [ ] Run the common schema fixture test before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Valid lane | CONFIRMED | `valid/README.md` and `valid/valid_1.json` exist. |
| Invalid lane | CONFIRMED | `invalid/README.md`, `invalid/invalid_1.json`, and `invalid_1.expected_error.txt` exist. |
| Schema | CONFIRMED | `ingest_receipt.schema.json` defines required fields, identifier pattern, date-time fields, finite outcome enum, byte minimum, digest object, digest pattern, declared fixture root, declared validator, declared policy path, and additional-property behavior. |
| Contract | CONFIRMED | `contracts/source/ingest_receipt.md` defines semantic meaning and separates IngestReceipt from SourceDescriptor, RunReceipt, ValidationReport, EvidenceBundle, PolicyDecision, ReleaseManifest, source raw data, and publication authority. |
| Test execution | NOT RUN | No validators, pytest, source policy checks, source registry checks, ingest workflow checks, lifecycle transition checks, release checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define fixture-family guidance. |
| [`valid/README.md`](valid/README.md) | CONFIRMED | Positive fixture lane guidance. | Does not prove tests were run. |
| [`valid/valid_1.json`](valid/valid_1.json) | CONFIRMED | Current positive fixture includes all required fields and schema-compatible values. | Only one valid fixture is currently documented. |
| [`invalid/README.md`](invalid/README.md) | CONFIRMED | Negative fixture lane guidance. | Does not prove tests were run. |
| [`invalid/invalid_1.json`](invalid/invalid_1.json) | CONFIRMED | Current negative fixture omits required `id`. | Only one invalid fixture is currently documented. |
| [`invalid/invalid_1.expected_error.txt`](invalid/invalid_1.expected_error.txt) | CONFIRMED | Current expected matcher is `required`. | Broad matcher; may be tightened later. |
| [`../../../../../schemas/contracts/v1/source/ingest_receipt.schema.json`](../../../../../schemas/contracts/v1/source/ingest_receipt.schema.json) | CONFIRMED | Schema shape, required fields, identifier pattern, date-time fields, outcome enum, byte minimum, digest object, digest value pattern, fixture root, validator path, policy path, and status. | Schema status is `PROPOSED`; validator implementation was not verified. |
| [`../../../../../contracts/source/ingest_receipt.md`](../../../../../contracts/source/ingest_receipt.md) | CONFIRMED | Semantic meaning, source-ingest lifecycle role, field surface, invariants, and boundary against source truth, RunReceipt, ValidationReport, EvidenceBundle, PolicyDecision, ReleaseManifest, and source raw data. | Does not prove ingest workflow, source registry resolution, validator wiring, policy behavior, release checks, or CI status. |
| `../../../../../docs/doctrine/directory-rules.md` | CONFIRMED doctrine | `fixtures/` is within the validate/operate authority surface and supports test inputs while contracts, schemas, policy, and lifecycle data remain separate roots. | Specific fixture completeness requires inventory and tests. |

[Back to top](#top)
