<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/source/doctrine-artifact-descriptor/readme
title: doctrine_artifact_descriptor fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): doctrine steward; TODO(owner): source steward; TODO(owner): schema steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): review steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-06-30 expansion
updated: 2026-06-30
policy_label: public-review
related:
  - valid/README.md
  - valid/valid_1.json
  - invalid/README.md
  - invalid/invalid_1.json
  - invalid/invalid_1.expected_error.txt
  - ../../../../../schemas/contracts/v1/source/doctrine_artifact_descriptor.schema.json
  - ../../../../../contracts/source/doctrine_artifact_descriptor.md
  - ../../../../../contracts/source/source_descriptor.md
  - ../../../../../contracts/source/ingest_receipt.md
  - ../../../../../policy/source/
  - ../../../../../policy/rights/
  - ../../../../../policy/sensitivity/
  - ../../../../../tools/validators/source/validate_doctrine_artifact_descriptor.py
  - ../../../../../tests/source/test_doctrine_artifact_descriptor_schema.py
  - ../../../../../tests/schemas/test_common_contracts.py
  - ../../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, v1, source, doctrine-artifact-descriptor, valid-fixtures, invalid-fixtures, expected-error, json-schema, doctrine, source-admission, sha256, provenance, authority-status, steward-signoff, integrity, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/contracts/v1/source/doctrine_artifact_descriptor/README.md`."
  - "This directory is the fixture family for `doctrine_artifact_descriptor`."
  - "Fixtures are sample test inputs only; semantic meaning, schema shape, source admission, steward review, policy behavior, and release authority stay in their owning roots."
  - "Current fixture coverage includes one valid case and one invalid integrity/date case."
  - "No tests, validators, source admission workflows, steward review workflows, doctrine registry checks, rights/sensitivity policy checks, release checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `doctrine_artifact_descriptor` fixtures

Fixture family for the KFM `doctrine_artifact_descriptor` source contract schema.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Family: source" src="https://img.shields.io/badge/family-source-blue">
  <img alt="Contract: doctrine_artifact_descriptor" src="https://img.shields.io/badge/contract-doctrine__artifact__descriptor-purple">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
  <img alt="Integrity: SHA-256" src="https://img.shields.io/badge/integrity-SHA--256-informational">
</p>

**Path:** `fixtures/contracts/v1/source/doctrine_artifact_descriptor/README.md`  
**Fixture posture:** JSON Schema valid/invalid fixture family  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/source/doctrine_artifact_descriptor.schema.json`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Schema basis](#schema-basis) · [Authority boundary](#authority-boundary) · [Harness behavior](#harness-behavior) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are schema fixtures. They are not doctrine artifacts, EvidenceBundles, ReleaseManifests, source truth, schemas, policy decisions, steward review proof, release approval, review approval, or publication authority.

---

## Purpose

This directory groups positive and negative JSON fixtures for the `doctrine_artifact_descriptor` schema.

Use this fixture family to verify that KFM accepts a minimal well-shaped `DoctrineArtifactDescriptor`-like object and rejects descriptor-shaped metadata that fails integrity/date constraints. The fixture family helps protect the doctrine/source-admission boundary by keeping doctrine-artifact admission metadata testable without turning fixture examples into admitted doctrine, source truth, review proof, release approval, or implementation proof.

A passing fixture proves schema shape only. It does not prove the described doctrine artifact is current, authoritative, implemented, reviewed, release-approved, or publishable.

---

## Current inventory

| Lane | File | Current role | Status |
|---|---|---|---|
| [`valid/`](valid/README.md) | [`valid_1.json`](valid/valid_1.json) | Minimal positive fixture with every required top-level field, valid SHA-256 digest shape, allowed `authority_status`, and valid `admitted_at`. | CONFIRMED |
| [`invalid/`](invalid/README.md) | [`invalid_1.json`](invalid/invalid_1.json) | Negative fixture with invalid short `sha256` value and invalid date-time value. | CONFIRMED |
| [`invalid/`](invalid/README.md) | [`invalid_1.expected_error.txt`](invalid/invalid_1.expected_error.txt) | Expected-error matcher currently pins the SHA-256 pattern failure. | CONFIRMED |

Current positive fixture shape:

```json
{
  "doc_id": "kfm://doc/doctrine/master-maplibre-components-functions-features",
  "filename": "Master_MapLibre_Components-Functions-Features.pdf",
  "sha256": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "provenance": "repo://docs/doctrine/artifacts/Master_MapLibre_Components-Functions-Features.pdf",
  "authority_status": "NEEDS_VERIFICATION",
  "admitted_at": "2026-05-12T00:00:00Z",
  "steward_signoff_ref": "review://docs-steward/2026-05-12/001"
}
```

Current negative fixture shape:

```json
{
  "doc_id": "kfm://doc/doctrine/missing-hash",
  "filename": "Kansas_Frontier_Matrix_Definitive_Greenfield_Building_Plan_v1_1.pdf",
  "sha256": "123",
  "provenance": "repo://docs/doctrine/artifacts/Kansas_Frontier_Matrix_Definitive_Greenfield_Building_Plan_v1_1.pdf",
  "authority_status": "CONFIRMED",
  "admitted_at": "not-a-date",
  "steward_signoff_ref": "review://docs-steward/2026-05-12/002"
}
```

---

## Schema basis

The current schema evidence for this fixture family is:

```text
schemas/contracts/v1/source/doctrine_artifact_descriptor.schema.json
```

Confirmed schema facts:

| Item | Value |
|---|---|
| Schema title | `doctrine_artifact_descriptor` |
| Root type | object |
| Required fields | `doc_id`, `filename`, `sha256`, `provenance`, `authority_status`, `admitted_at`, `steward_signoff_ref` |
| `sha256` | string matching `^[a-fA-F0-9]{64}$` |
| `authority_status` enum values | `CONFIRMED`, `NEEDS_VERIFICATION`, `PROPOSED` |
| `admitted_at` | string with `date-time` format |
| Additional properties | false |
| Declared contract doc | `contracts/source/doctrine_artifact_descriptor.md` |
| Schema status | `PROPOSED` |

---

## Authority boundary

| Responsibility | Home | Status in this check |
|---|---|---|
| Fixture examples | `fixtures/contracts/v1/source/doctrine_artifact_descriptor/` | CONFIRMED |
| Valid examples | `fixtures/contracts/v1/source/doctrine_artifact_descriptor/valid/` | CONFIRMED |
| Invalid examples | `fixtures/contracts/v1/source/doctrine_artifact_descriptor/invalid/` | CONFIRMED |
| Machine-checkable shape | `schemas/contracts/v1/source/doctrine_artifact_descriptor.schema.json` | CONFIRMED |
| Semantic contract | `contracts/source/doctrine_artifact_descriptor.md` | CONFIRMED |
| Source, rights, and sensitivity policy | `policy/source/`, `policy/rights/`, `policy/sensitivity/` | OUT OF SCOPE FOR THIS README |
| Dedicated validator implementation | `tools/validators/source/validate_doctrine_artifact_descriptor.py` | NEEDS VERIFICATION |
| Dedicated source test | `tests/source/test_doctrine_artifact_descriptor_schema.py` | NEEDS VERIFICATION / NOT RUN |
| Common schema fixture harness | `tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN |

`DoctrineArtifactDescriptor` must remain distinguishable from:

| Do not collapse `DoctrineArtifactDescriptor` into | Why |
|---|---|
| Doctrine artifact content | The descriptor records admission metadata; it is not the artifact itself. |
| Source truth | The descriptor pins and describes a doctrine artifact; it does not prove statements inside it true. |
| Implementation proof | Downstream code still needs tests, contracts, validators, and runtime evidence. |
| Steward review proof | The descriptor references signoff; it is not the full review record. |
| `EvidenceBundle` | Evidence supports claims; doctrine descriptors are admission metadata. |
| `ReleaseManifest` | Release manifests bind released contents; this descriptor cannot approve release. |
| Schema or executable policy | Schema and policy live in their own roots and must not be collapsed into fixtures. |
| Publication authority | Publication still requires governed release, rights, sensitivity, provenance, review, and rollback posture. |

---

## Harness behavior

The common schema test harness includes `source` in its fixture families and discovers schemas from:

```text
schemas/contracts/v1/source/*.schema.json
```

For a matching fixture directory, the observed harness expects:

```text
fixtures/contracts/v1/source/<schema_name>/valid/valid_*.json
fixtures/contracts/v1/source/<schema_name>/invalid/invalid_*.json
fixtures/contracts/v1/source/<schema_name>/invalid/invalid_*.expected_error.txt
```

For this source family, that means:

```text
fixtures/contracts/v1/source/doctrine_artifact_descriptor/
```

Observed expectations:

| Fixture pattern | Expected result |
|---|---|
| `valid/valid_*.json` | no JSON Schema errors |
| `invalid/invalid_*.json` | at least one JSON Schema error |
| `invalid/invalid_*.expected_error.txt` | expected text appears in combined schema error messages |

This README documents expected fixture behavior only. It does not claim that pytest, CI, source admission policy, rights policy, sensitivity policy, doctrine review, registry admission, release checks, or the dedicated DoctrineArtifactDescriptor validator was run during this update.

---

## Maintenance checklist

Before changing this fixture family:

- [ ] Keep passing examples under `valid/valid_<n>.json`.
- [ ] Keep failing examples under `invalid/invalid_<n>.json`.
- [ ] Keep expected-error text beside the invalid fixture it describes.
- [ ] Keep at least one minimal positive fixture and one integrity-pattern invalid fixture.
- [ ] Add required-field, authority-status enum, date-time, and additional-property fixtures as coverage expands.
- [ ] Keep digest examples as 64 hexadecimal characters unless the schema changes.
- [ ] Use only allowed `authority_status` values: `CONFIRMED`, `NEEDS_VERIFICATION`, or `PROPOSED`.
- [ ] Keep fixture cases small, deterministic, public-safe, and reviewable.
- [ ] Avoid private, unpublished, source-system, prompt-like, or policy-restricted content.
- [ ] Do not embed full doctrine artifacts, raw evidence payloads, protected location detail, credentials, or release-blocked material in fixtures.
- [ ] Update parent and lane READMEs when schema fields, enum values, digest requirements, admission metadata expectations, or fixture coverage changes.
- [ ] Run the common schema fixture test before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Valid lane | CONFIRMED | `valid/README.md` and `valid/valid_1.json` exist. |
| Invalid lane | CONFIRMED | `invalid/README.md`, `invalid/invalid_1.json`, and `invalid_1.expected_error.txt` exist. |
| Schema | CONFIRMED | `doctrine_artifact_descriptor.schema.json` defines required fields, SHA-256 pattern, authority-status enum, date-time field, and additional-property behavior. |
| Contract | CONFIRMED | `contracts/source/doctrine_artifact_descriptor.md` defines semantic meaning and separates DoctrineArtifactDescriptor from doctrine artifact content, EvidenceBundle, ReleaseManifest, source truth, schema, policy decision, review proof by itself, and publication authority. |
| Schema `x-kfm` fixture root | NOT DECLARED | The schema names its contract doc and status, but does not declare `fixtures_root` or validator path in the fetched `x-kfm` block. |
| Test execution | NOT RUN | No validators, pytest, source policy checks, doctrine registry checks, steward review checks, release checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define fixture-family guidance. |
| [`valid/README.md`](valid/README.md) | CONFIRMED | Positive fixture lane guidance. | Does not prove tests were run. |
| [`valid/valid_1.json`](valid/valid_1.json) | CONFIRMED | Current positive fixture includes all required fields, valid digest shape, allowed authority status, and valid date-time. | Only one valid fixture is currently documented. |
| [`invalid/README.md`](invalid/README.md) | CONFIRMED | Negative fixture lane guidance. | Does not prove tests were run. |
| [`invalid/invalid_1.json`](invalid/invalid_1.json) | CONFIRMED | Current negative fixture has invalid `sha256: "123"` and invalid `admitted_at: "not-a-date"`. | Only one invalid fixture is currently documented. |
| [`invalid/invalid_1.expected_error.txt`](invalid/invalid_1.expected_error.txt) | CONFIRMED | Current expected matcher pins the SHA-256 pattern failure. | It does not pin the date-time failure also present in the fixture. |
| [`../../../../../schemas/contracts/v1/source/doctrine_artifact_descriptor.schema.json`](../../../../../schemas/contracts/v1/source/doctrine_artifact_descriptor.schema.json) | CONFIRMED | Schema shape, required fields, SHA-256 pattern, authority-status enum, date-time field, additional-property posture, contract path, and status. | Schema status is `PROPOSED`; fixture root and validator path are not declared in this schema's `x-kfm` block. |
| [`../../../../../contracts/source/doctrine_artifact_descriptor.md`](../../../../../contracts/source/doctrine_artifact_descriptor.md) | CONFIRMED | Semantic meaning, source/doctrine-admission boundary, field surface, and distinction from source truth, implementation proof, review proof, EvidenceBundle, ReleaseManifest, schema, policy decision, and publication authority. | Does not prove registry workflow, steward signoff workflow, validator wiring, policy behavior, release checks, or CI status. |
| `../../../../../tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN | Common fixture discovery and valid/invalid fixture behavior. | Tests were not run during this update. |
| `../../../../../docs/doctrine/directory-rules.md` | CONFIRMED | `fixtures/` is the root for golden, valid, and invalid test inputs; contracts/schemas/policy split remains separate. | Specific fixture completeness requires tests or inventory. |

[Back to top](#top)
