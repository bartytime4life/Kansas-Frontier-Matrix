<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/source/ingest-receipt/valid/readme
title: ingest_receipt valid fixtures README
type: fixture-readme
version: v0.2.0
status: draft; inventory-reconciled; deterministic-polarity; validator-prerequisite-executable; fixture-only
owners: TODO(owner): source steward; TODO(owner): ingest steward; TODO(owner): schema steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-07-01 expansion
updated: 2026-07-31
policy_label: public-review
related:
  - valid_1.json
  - valid_2.json
  - ../invalid/README.md
  - ../invalid/invalid_1.json
  - ../invalid/invalid_1.expected_error.txt
  - ../invalid/invalid_2.json
  - ../invalid/invalid_2.expected_error.txt
  - ../invalid/invalid_3.json
  - ../invalid/invalid_3.expected_error.txt
  - ../../../../../../schemas/contracts/v1/source/ingest_receipt.schema.json
  - ../../../../../../contracts/source/ingest_receipt.md
  - ../../../../../../contracts/source/source_descriptor.md
  - ../../../../../../contracts/runtime/run_receipt.md
  - ../../../../../../policy/source/
  - ../../../../../../tools/validators/validate_ingest_receipt.py
  - ../../../../../../tests/schemas/test_common_contracts.py
  - ../../../../../../tests/validators/test_validate_ingest_receipt.py
  - ../../../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, v1, source, ingest-receipt, valid-fixtures, json-schema, source-ingest, receipt, sha256, lifecycle, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/contracts/v1/source/ingest_receipt/valid/README.md`."
  - "Valid fixtures are positive schema examples for the `ingest_receipt` schema."
  - "Current valid fixture coverage includes `SUCCESS` and `PARTIAL` cases in `valid_1.json` and `valid_2.json`."
  - "The repository-owned no-network validator and focused direct suite exercise the nonempty valid/invalid fixture family; no connector is run."
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

Use this lane to prove that well-shaped `SUCCESS` and `PARTIAL` IngestReceipt examples can pass schema validation before higher-level source-ingest, registry, policy, or pipeline work. Passing these fixtures proves shape and validator polarity only. It does not prove that source material was captured, that digests came from real payloads, that source policy allows downstream use, or that any lifecycle transition is approved.

---

## Current inventory

| File | Role | Expected result | Status |
|---|---|---|---|
| [`valid_1.json`](valid_1.json) | Minimal positive fixture for `ingest_receipt`. | Schema validation should pass. | CONFIRMED |
| [`valid_2.json`](valid_2.json) | Positive `PARTIAL` fixture with zero captured bytes and one well-shaped digest. | Schema validation should pass; `--require-success` may separately reject the outcome. | CONFIRMED |

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

`valid_2.json` uses the same required field surface with `outcome: "PARTIAL"` and `bytes_in: 0`. Together the two fixtures prove that both schema-valid outcome shapes are retained; they do not prove either described ingest ran, that `source_id` resolves, that digest values were computed from source material, or that captured material is admissible or publishable.

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

For valid fixtures, the expected pattern is:

```text
valid/valid_*.json
```

Expected behavior:

| Fixture pattern | Expected result |
|---|---|
| `valid/valid_*.json` | No JSON Schema errors. |

The stable no-network commands are:

```bash
python tools/validators/validate_ingest_receipt.py --fixtures
python -m pytest tests/validators/test_validate_ingest_receipt.py -q
```

They exercise the fixture family and focused validator behavior. They do not run a connector or establish source policy, registry resolution, connector-emitted receipt presence, persistence, lifecycle transition, release, or publication.

---

## Maintenance checklist

Before changing this valid fixture lane:

- [ ] Keep passing examples under `valid/valid_<n>.json`.
- [ ] Keep at least one minimal positive fixture unless the schema family is intentionally retired.
- [ ] Keep positive fixtures paired with negative fixtures under `../invalid/`.
- [ ] Add multi-digest, fail-outcome, and richer metadata-safe valid examples when coverage expands; preserve the existing `PARTIAL`/zero-byte case.
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
| Valid fixtures | CONFIRMED | `valid_1.json` and `valid_2.json` preserve schema-valid `SUCCESS` and `PARTIAL` outcomes. |
| Invalid lane README | CONFIRMED | `../invalid/README.md` documents all three paired negative cases. |
| Invalid fixtures | CONFIRMED | Three JSON/expected-error pairs cover required id, additional-property denial, and id-pattern denial. |
| Schema | CONFIRMED | `ingest_receipt.schema.json` defines required fields, identifier pattern, date-time fields, finite outcome enum, byte minimum, digest object, digest pattern, declared fixture root, declared validator, declared policy path, and additional-property behavior. |
| Contract | CONFIRMED | `contracts/source/ingest_receipt.md` defines semantic meaning and distinguishes IngestReceipt from SourceDescriptor, RunReceipt, ValidationReport, EvidenceBundle, PolicyDecision, ReleaseManifest, and source raw data. |
| Validator and focused tests | CONFIRMED | The repository-owned fixture command and focused no-network suite execute this family; no connector run or release state is implied. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define valid-fixture guidance. |
| [`valid_1.json`](valid_1.json) and [`valid_2.json`](valid_2.json) | CONFIRMED | Current positive fixtures include all required fields and schema-compatible `SUCCESS`/`PARTIAL` values. | Synthetic shapes, not observed ingest runs. |
| [`../invalid/README.md`](../invalid/README.md) | CONFIRMED | Documents the three-case negative fixture lane and expected matchers. | The family does not exhaust every failure mode. |
| [`../../../../../../schemas/contracts/v1/source/ingest_receipt.schema.json`](../../../../../../schemas/contracts/v1/source/ingest_receipt.schema.json) | CONFIRMED | Schema shape, fields, patterns, fixture root, validator path, policy path, and status. | Schema status remains `PROPOSED`; schema validity is not source admission. |
| [`../../../../../../tools/validators/validate_ingest_receipt.py`](../../../../../../tools/validators/validate_ingest_receipt.py) and [`../../../../../../tests/validators/test_validate_ingest_receipt.py`](../../../../../../tests/validators/test_validate_ingest_receipt.py) | CONFIRMED | No-network fixture polarity plus focused semantic, binding, and diagnostic behavior. | No connector execution, live source, persistence, policy, release, or publication. |
| [`../../../../../../contracts/source/ingest_receipt.md`](../../../../../../contracts/source/ingest_receipt.md) | CONFIRMED | Semantic meaning, source-ingest lifecycle role, field surface, invariants, and boundary against source truth, RunReceipt, ValidationReport, EvidenceBundle, PolicyDecision, ReleaseManifest, and source raw data. | Does not prove ingest workflow, source registry resolution, validator wiring, policy behavior, release checks, or CI status. |
| `../../../../../../docs/doctrine/directory-rules.md` | CONFIRMED doctrine | `fixtures/` is within the validate/operate authority surface and supports test inputs while contracts, schemas, policy, and lifecycle data remain separate roots. | Specific fixture completeness requires inventory and tests. |

[Back to top](#top)
