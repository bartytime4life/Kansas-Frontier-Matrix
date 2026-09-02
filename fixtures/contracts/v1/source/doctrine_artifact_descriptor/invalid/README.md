<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/source/doctrine-artifact-descriptor/invalid/readme
title: doctrine_artifact_descriptor invalid fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): doctrine steward; TODO(owner): source steward; TODO(owner): schema steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): review steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-06-30 expansion
updated: 2026-06-30
policy_label: public-review
related:
  - ../valid/valid_1.json
  - invalid_1.json
  - invalid_1.expected_error.txt
  - ../../../../../../schemas/contracts/v1/source/doctrine_artifact_descriptor.schema.json
  - ../../../../../../contracts/source/doctrine_artifact_descriptor.md
  - ../../../../../../contracts/source/source_descriptor.md
  - ../../../../../../contracts/source/ingest_receipt.md
  - ../../../../../../policy/source/
  - ../../../../../../policy/rights/
  - ../../../../../../policy/sensitivity/
  - ../../../../../../tools/validators/source/validate_doctrine_artifact_descriptor.py
  - ../../../../../../tests/source/test_doctrine_artifact_descriptor_schema.py
  - ../../../../../../tests/schemas/test_common_contracts.py
  - ../../../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, v1, source, doctrine-artifact-descriptor, invalid-fixtures, expected-error, json-schema, doctrine, source-admission, sha256, provenance, authority-status, steward-signoff, integrity, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/contracts/v1/source/doctrine_artifact_descriptor/invalid/README.md`."
  - "Invalid fixtures are intentionally failing examples for the `doctrine_artifact_descriptor` schema."
  - "Current invalid fixture coverage is one integrity/date example: `invalid_1.json` has an invalid `sha256` pattern and a non-date `admitted_at`; the expected-error file currently pins the SHA-256 pattern error."
  - "No tests, validators, source admission workflows, steward review workflows, doctrine registry checks, rights/sensitivity policy checks, release checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `doctrine_artifact_descriptor` invalid fixtures

Negative fixture lane for the KFM `doctrine_artifact_descriptor` source contract schema.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Family: source" src="https://img.shields.io/badge/family-source-blue">
  <img alt="Contract: doctrine_artifact_descriptor" src="https://img.shields.io/badge/contract-doctrine__artifact__descriptor-purple">
  <img alt="Lane: invalid" src="https://img.shields.io/badge/lane-invalid-critical">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/contracts/v1/source/doctrine_artifact_descriptor/invalid/README.md`  
**Fixture posture:** invalid JSON Schema fixture lane  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/source/doctrine_artifact_descriptor.schema.json`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Schema basis](#schema-basis) · [Why this fixture fails](#why-this-fixture-fails) · [Authority boundary](#authority-boundary) · [Harness behavior](#harness-behavior) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are expected to fail schema validation. They are not DoctrineArtifactDescriptors, doctrine artifacts, EvidenceBundles, ReleaseManifests, source truth, schemas, policy decisions, steward review proof, or publication authority.

---

## Purpose

This directory stores negative JSON examples for the `doctrine_artifact_descriptor` schema.

Use this lane to prove that malformed or incomplete doctrine-admission descriptors are rejected before they can be treated as governed metadata for admitted doctrine artifacts. Invalid fixtures help preserve KFM's source and doctrine-admission boundary: a descriptor must identify the doctrine artifact, filename, content integrity digest, provenance, authority posture, admission time, and steward signoff reference before downstream contracts, schemas, policies, docs, or build plans rely on it.

---

## Current inventory

| File | Role | Expected result | Status |
|---|---|---|---|
| [`invalid_1.json`](invalid_1.json) | Negative fixture with invalid `sha256` pattern and invalid `admitted_at` value. | Schema validation should fail. | CONFIRMED |
| [`invalid_1.expected_error.txt`](invalid_1.expected_error.txt) | Expected-error matcher for `invalid_1.json`. | Combined schema errors should include the SHA-256 pattern failure. | CONFIRMED |

Current invalid fixture:

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

The paired positive fixture currently provides a 64-character hexadecimal digest and valid `admitted_at` timestamp:

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

---

## Schema basis

The current schema evidence for this fixture lane is:

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

## Why this fixture fails

`invalid_1.json` fails the current schema because its `sha256` value is:

```text
123
```

The paired schema requires `sha256` to match exactly 64 hexadecimal characters without a `sha256:` prefix. The fixture also contains `admitted_at: "not-a-date"`, which is not a valid JSON Schema `date-time` value, but the current expected-error file pins the SHA-256 pattern failure:

```text
'123' does not match '^[a-fA-F0-9]{64}$'
```

That failure matters because `sha256` is the integrity pin for the admitted doctrine artifact. A descriptor that identifies a doctrine file but fails to bind it to a valid content digest must not silently pass as a governed `DoctrineArtifactDescriptor`.

> [!WARNING]
> A `DoctrineArtifactDescriptor` records admission metadata for a doctrine artifact. It is not the doctrine artifact itself, not source truth, not implementation proof, not review proof by itself, and not release or publication approval.

---

## Authority boundary

| Responsibility | Home | Status in this check |
|---|---|---|
| Negative fixture examples | `fixtures/contracts/v1/source/doctrine_artifact_descriptor/invalid/` | CONFIRMED |
| Positive fixture examples | `fixtures/contracts/v1/source/doctrine_artifact_descriptor/valid/` | CONFIRMED file present / README not checked in this update |
| Machine-checkable shape | `schemas/contracts/v1/source/doctrine_artifact_descriptor.schema.json` | CONFIRMED |
| Semantic contract | `contracts/source/doctrine_artifact_descriptor.md` | CONFIRMED |
| Source, rights, and sensitivity policy | `policy/source/`, `policy/rights/`, `policy/sensitivity/` | OUT OF SCOPE FOR THIS README |
| Dedicated validator implementation | `tools/validators/source/validate_doctrine_artifact_descriptor.py` | NEEDS VERIFICATION |
| Dedicated source test | `tests/source/test_doctrine_artifact_descriptor_schema.py` | NEEDS VERIFICATION / NOT RUN |
| Common schema fixture harness | `tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN |

Do not collapse this fixture lane into the semantic contract, schema, source admission workflow, doctrine artifact registry, executable policy, steward review workflow, EvidenceBundle, ReleaseManifest, source truth, or publication authority.

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

This README documents expected fixture behavior only. It does not claim that pytest, CI, source admission policy, rights policy, sensitivity policy, doctrine review, registry admission, release checks, or the dedicated DoctrineArtifactDescriptor validator were run during this update.

---

## Maintenance checklist

Before changing this invalid fixture lane:

- [ ] Keep failing examples under `invalid/invalid_<n>.json`.
- [ ] Keep expected-error text beside the invalid fixture it describes.
- [ ] Keep at least one integrity-pattern failure unless another fixture family covers that failure class.
- [ ] Add required-field, authority-status enum, date-time, and additional-property failures when DoctrineArtifactDescriptor coverage expands.
- [ ] Keep fixture examples public-safe and limited to descriptor-shaped metadata.
- [ ] Avoid private, unpublished, source-system, prompt-like, or policy-restricted content.
- [ ] Do not embed full doctrine artifacts, raw evidence payloads, protected location detail, credentials, or release-blocked material in fixtures.
- [ ] Update this README when schema fields, enum values, digest requirements, admission metadata expectations, or expected-error behavior changes.
- [ ] Run the schema fixture test before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Invalid fixture | CONFIRMED | `invalid_1.json` exists and uses invalid `sha256: "123"`; it also uses invalid `admitted_at: "not-a-date"`. |
| Expected-error file | CONFIRMED | `invalid_1.expected_error.txt` exists and pins the SHA-256 pattern failure. |
| Positive fixture | CONFIRMED | `valid/valid_1.json` exists and includes a 64-character hex `sha256` plus valid date-time value. |
| Schema | CONFIRMED | `doctrine_artifact_descriptor.schema.json` defines required fields, SHA-256 pattern, authority-status enum, date-time field, and additional-property behavior. |
| Contract | CONFIRMED | `contracts/source/doctrine_artifact_descriptor.md` defines semantic meaning and distinguishes DoctrineArtifactDescriptor from doctrine artifact content, EvidenceBundle, ReleaseManifest, source truth, schema, policy decision, and review proof by itself. |
| Test execution | NOT RUN | No validators, pytest, source policy checks, doctrine registry checks, steward review checks, release checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define invalid-fixture guidance. |
| [`invalid_1.json`](invalid_1.json) | CONFIRMED | Current negative fixture has invalid `sha256: "123"` and invalid `admitted_at: "not-a-date"`. | Only one invalid case is currently documented here. |
| [`invalid_1.expected_error.txt`](invalid_1.expected_error.txt) | CONFIRMED | Expected matcher pins the SHA-256 pattern failure. | It does not pin the date-time failure also present in the fixture. |
| [`../valid/valid_1.json`](../valid/valid_1.json) | CONFIRMED | Paired positive fixture includes all required fields, valid digest shape, allowed authority status, and valid date-time. | Positive lane README was not checked during this update. |
| [`../../../../../../schemas/contracts/v1/source/doctrine_artifact_descriptor.schema.json`](../../../../../../schemas/contracts/v1/source/doctrine_artifact_descriptor.schema.json) | CONFIRMED | Schema shape, required fields, SHA-256 pattern, authority-status enum, date-time field, additional-property posture, contract path, and status. | Schema status is `PROPOSED`; fixture root and validator path are not declared in this schema's `x-kfm` block. |
| [`../../../../../../contracts/source/doctrine_artifact_descriptor.md`](../../../../../../contracts/source/doctrine_artifact_descriptor.md) | CONFIRMED | Semantic meaning, source/doctrine-admission boundary, field surface, and distinction from source truth, implementation proof, review proof, EvidenceBundle, ReleaseManifest, schema, policy decision, and publication authority. | Does not prove registry workflow, steward signoff workflow, validator wiring, policy behavior, release checks, or CI status. |
| `../../../../../../tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN | Common fixture discovery and invalid fixture behavior. | Tests were not run during this update. |
| `../../../../../../docs/doctrine/directory-rules.md` | CONFIRMED | `fixtures/` is the root for golden, valid, and invalid test inputs; contracts/schemas/policy split remains separate. | Specific fixture completeness requires tests or inventory. |

[Back to top](#top)
