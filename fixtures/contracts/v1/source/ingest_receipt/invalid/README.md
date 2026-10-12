<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/source/ingest-receipt/invalid/readme
title: ingest_receipt invalid fixtures README
type: fixture-readme
version: v0.2.0
status: draft; inventory-reconciled; deterministic-polarity; validator-prerequisite-executable; fixture-only
owners: TODO(owner): source steward; TODO(owner): ingest steward; TODO(owner): schema steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-07-01 expansion
updated: 2026-07-31
policy_label: public-review
related:
  - ../valid/valid_1.json
  - ../valid/valid_2.json
  - invalid_1.json
  - invalid_1.expected_error.txt
  - invalid_2.json
  - invalid_2.expected_error.txt
  - invalid_3.json
  - invalid_3.expected_error.txt
  - ../../../../../../schemas/contracts/v1/source/ingest_receipt.schema.json
  - ../../../../../../contracts/source/ingest_receipt.md
  - ../../../../../../contracts/source/source_descriptor.md
  - ../../../../../../contracts/runtime/run_receipt.md
  - ../../../../../../policy/source/
  - ../../../../../../tools/validators/validate_ingest_receipt.py
  - ../../../../../../tests/schemas/test_common_contracts.py
  - ../../../../../../tests/validators/test_validate_ingest_receipt.py
  - ../../../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, v1, source, ingest-receipt, invalid-fixtures, expected-error, json-schema, source-ingest, receipt, sha256, lifecycle, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/contracts/v1/source/ingest_receipt/invalid/README.md`."
  - "Invalid fixtures are intentionally failing examples for the `ingest_receipt` schema."
  - "Current invalid fixture coverage includes missing-required-id, additional-property, and invalid-id-pattern cases with paired matchers."
  - "The repository-owned no-network validator and focused direct suite exercise the nonempty valid/invalid fixture family; no connector is run."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `ingest_receipt` invalid fixtures

Negative fixture lane for the KFM `ingest_receipt` source contract schema.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Family: source" src="https://img.shields.io/badge/family-source-blue">
  <img alt="Contract: ingest_receipt" src="https://img.shields.io/badge/contract-ingest__receipt-purple">
  <img alt="Lane: invalid" src="https://img.shields.io/badge/lane-invalid-critical">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/contracts/v1/source/ingest_receipt/invalid/README.md`  
**Fixture posture:** invalid JSON Schema fixture lane  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/source/ingest_receipt.schema.json`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Schema basis](#schema-basis) · [Why this fixture fails](#why-this-fixture-fails) · [Authority boundary](#authority-boundary) · [Harness behavior](#harness-behavior) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are expected to fail schema validation. They are not IngestReceipts, SourceDescriptors, RunReceipts, EvidenceBundles, PolicyDecisions, ReleaseManifests, source truth, ingest workflow proof, release approval, or publication authority.

---

## Purpose

This directory stores negative JSON examples for the `ingest_receipt` schema.

Use this lane to prove that incomplete ingest receipts are rejected before they can be treated as governed source-ingest receipts. Invalid fixtures help preserve KFM's source-admission and lifecycle boundary: an ingest receipt can record capture time, outcome, byte count, source id, run id, and digests, but fixture shape alone must not become source truth, policy approval, release approval, or permission for public clients to read lifecycle-internal source material.

---

## Current inventory

| File | Role | Expected result | Status |
|---|---|---|---|
| [`invalid_1.json`](invalid_1.json) | Negative fixture missing required `id`. | Schema validation should fail. | CONFIRMED |
| [`invalid_1.expected_error.txt`](invalid_1.expected_error.txt) | Expected-error matcher for `invalid_1.json`. | Combined schema errors should include `required`. | CONFIRMED |
| [`invalid_2.json`](invalid_2.json) / [`invalid_2.expected_error.txt`](invalid_2.expected_error.txt) | Negative fixture containing an unknown property. | Schema validation should fail with the additional-properties family. | CONFIRMED |
| [`invalid_3.json`](invalid_3.json) / [`invalid_3.expected_error.txt`](invalid_3.expected_error.txt) | Negative fixture containing an uppercase `id`. | Schema validation should fail with the pattern family. | CONFIRMED |

Current invalid fixture:

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

The paired positive fixture currently includes the required `id` field:

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

## Why this fixture fails

`invalid_1.json` fails the current schema because it omits:

```text
id
```

The paired schema requires `id` as the stable ingest receipt identifier. The first expected-error file uses the broad matcher:

```text
required
```

That failure matters because an ingest receipt without a stable `id` cannot be reliably referenced, superseded, audited, corrected, or tied to downstream lifecycle and validation records. `invalid_2.json` separately proves `additionalProperties: false`; `invalid_3.json` proves the lowercase identifier pattern. Their expected-error files bind the applicable error families.

> [!WARNING]
> `IngestReceipt` records a source ingest or capture event. It is not source truth, not a source descriptor, not a runtime run receipt, not validation proof, not a policy decision, and not release or publication approval.

---

## Authority boundary

| Responsibility | Home | Status in this check |
|---|---|---|
| Negative fixture examples | `fixtures/contracts/v1/source/ingest_receipt/invalid/` | CONFIRMED |
| Positive fixture examples | `fixtures/contracts/v1/source/ingest_receipt/valid/` | CONFIRMED two-case lane and README |
| Machine-checkable shape | `schemas/contracts/v1/source/ingest_receipt.schema.json` | CONFIRMED |
| Semantic contract | `contracts/source/ingest_receipt.md` | CONFIRMED |
| Source policy | `policy/source/` | OUT OF SCOPE FOR THIS README |
| Dedicated validator implementation | `tools/validators/validate_ingest_receipt.py` | CONFIRMED repository-owned, no-network, and aggregate-registered |
| Focused validator tests | `tests/validators/test_validate_ingest_receipt.py` | CONFIRMED direct semantic, binding, diagnostic, and fixture-polarity coverage |
| Common schema fixture harness | `tests/schemas/test_common_contracts.py` | CONFIRMED adjacent schema-conformance coverage |

Do not collapse this fixture lane into the semantic contract, schema, source registry, ingest workflow, SourceDescriptor, RunReceipt, EvidenceBundle, ValidationReport, PolicyDecision, ReleaseManifest, source truth, or publication authority.

---

## Harness behavior

The common schema fixture convention for contract fixtures is:

```text
fixtures/contracts/v1/<family>/<name>/
```

For invalid fixtures, the expected pattern is:

```text
invalid/invalid_*.json
invalid/invalid_*.expected_error.txt
```

Expected behavior:

| Fixture pattern | Expected result |
|---|---|
| `invalid/invalid_*.json` | At least one JSON Schema error. |
| `invalid/invalid_*.expected_error.txt` | Expected text appears in the combined schema error messages. |

The stable no-network commands are:

```bash
python tools/validators/validate_ingest_receipt.py --fixtures
python -m pytest tests/validators/test_validate_ingest_receipt.py -q
```

They exercise the fixture family and focused validator behavior. They do not run a connector or establish source policy, registry resolution, connector-emitted receipt presence, persistence, lifecycle transition, release, or publication.

---

## Maintenance checklist

Before changing this invalid fixture lane:

- [ ] Keep failing examples under `invalid/invalid_<n>.json`.
- [ ] Keep expected-error text beside the invalid fixture it describes.
- [ ] Keep at least one missing-required-field failure unless another fixture family covers that failure class.
- [ ] Add id-pattern, digest-pattern, empty-digests, outcome-enum, date-time, bytes minimum, and additional-property failures when coverage expands.
- [ ] Keep fixture examples public-safe and limited to receipt-shaped metadata.
- [ ] Avoid private, unpublished, source-system, prompt-like, or policy-restricted content.
- [ ] Do not embed full source payloads or release-blocked material in fixtures.
- [ ] Update this README when schema fields, enum values, digest requirements, ingest metadata expectations, or expected-error behavior changes.
- [ ] Run the schema fixture test before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Invalid fixtures | CONFIRMED | Three JSON fixtures cover required id, additional-property denial, and id-pattern denial. |
| Expected-error files | CONFIRMED | Each invalid JSON fixture has a paired matcher for its failure family. |
| Positive fixtures | CONFIRMED | `valid/valid_1.json` and `valid/valid_2.json` preserve schema-valid `SUCCESS` and `PARTIAL` outcomes. |
| Schema | CONFIRMED | `ingest_receipt.schema.json` defines required fields, identifier pattern, date-time fields, finite outcome enum, byte minimum, digest object, digest pattern, declared fixture root, declared validator, declared policy path, and additional-property behavior. |
| Contract | CONFIRMED | `contracts/source/ingest_receipt.md` defines semantic meaning and distinguishes IngestReceipt from SourceDescriptor, RunReceipt, ValidationReport, EvidenceBundle, PolicyDecision, ReleaseManifest, and source raw data. |
| Validator and focused tests | CONFIRMED | The repository-owned fixture command and focused no-network suite execute this family; no connector run or release state is implied. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define invalid-fixture guidance. |
| `invalid_1.json` through `invalid_3.json` and paired expected-error files | CONFIRMED | Current negative fixtures cover required id, unknown property, and id pattern. | The family does not exhaust every schema or semantic failure. |
| [`../valid/valid_1.json`](../valid/valid_1.json) and [`../valid/valid_2.json`](../valid/valid_2.json) | CONFIRMED | Paired positive fixtures include required fields and schema-valid outcome values. | Synthetic shapes, not observed ingest runs. |
| [`../../../../../../schemas/contracts/v1/source/ingest_receipt.schema.json`](../../../../../../schemas/contracts/v1/source/ingest_receipt.schema.json) | CONFIRMED | Schema shape, fields, patterns, fixture root, validator path, policy path, and status. | Schema status remains `PROPOSED`; schema validity is not source admission. |
| [`../../../../../../tools/validators/validate_ingest_receipt.py`](../../../../../../tools/validators/validate_ingest_receipt.py) and [`../../../../../../tests/validators/test_validate_ingest_receipt.py`](../../../../../../tests/validators/test_validate_ingest_receipt.py) | CONFIRMED | No-network fixture polarity plus focused semantic, binding, and diagnostic behavior. | No connector execution, live source, persistence, policy, release, or publication. |
| [`../../../../../../contracts/source/ingest_receipt.md`](../../../../../../contracts/source/ingest_receipt.md) | CONFIRMED | Semantic meaning, source-ingest lifecycle role, field surface, invariants, and boundary against source truth, RunReceipt, ValidationReport, EvidenceBundle, PolicyDecision, ReleaseManifest, and source raw data. | Does not prove ingest workflow, source registry resolution, validator wiring, policy behavior, release checks, or CI status. |
| `../../../../../../docs/doctrine/directory-rules.md` | CONFIRMED doctrine | `fixtures/` is within the validate/operate authority surface and supports test inputs while contracts, schemas, policy, and lifecycle data remain separate roots. | Specific fixture completeness requires inventory and tests. |

[Back to top](#top)
