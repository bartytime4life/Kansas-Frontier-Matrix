<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/source/doctrine-artifact-preflight-summary/valid/readme
title: doctrine_artifact_preflight_summary valid fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): doctrine steward; TODO(owner): source steward; TODO(owner): schema steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): maintenance steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-07-01 expansion
updated: 2026-07-01
policy_label: public-review
related:
  - valid_1.json
  - ../invalid/invalid_1.json
  - ../invalid/invalid_1.expected_error.txt
  - ../../../../../../schemas/contracts/v1/source/doctrine_artifact_preflight_summary.schema.json
  - ../../../../../../tools/validators/source/validate_doctrine_artifact_preflight_summary.py
  - ../../../../../../scripts/maintenance/run_doctrine_artifact_preflight.py
  - ../../../../../../tests/source/test_doctrine_artifact_preflight_summary_schema.py
  - ../../../../../../tests/policy/test_preflight_summary_schema_contract.py
  - ../../../../../../tests/schemas/test_common_contracts.py
  - ../../../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, v1, source, doctrine-artifact-preflight-summary, valid-fixtures, json-schema, doctrine, preflight, returncode, receipt, presence-input, provenance, readiness, maintenance, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/contracts/v1/source/doctrine_artifact_preflight_summary/valid/README.md`."
  - "Valid fixtures are positive schema examples for the `doctrine_artifact_preflight_summary` schema."
  - "Current valid fixture coverage is one minimal passing case: `valid_1.json`."
  - "The paired invalid fixture currently covers an out-of-range `check_returncode: 3` enum failure."
  - "No tests, validators, doctrine artifact preflight scripts, source admission workflows, policy checks, release checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `doctrine_artifact_preflight_summary` valid fixtures

Positive fixture lane for the KFM `doctrine_artifact_preflight_summary` source contract schema.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Family: source" src="https://img.shields.io/badge/family-source-blue">
  <img alt="Contract: doctrine_artifact_preflight_summary" src="https://img.shields.io/badge/contract-doctrine__artifact__preflight__summary-purple">
  <img alt="Lane: valid" src="https://img.shields.io/badge/lane-valid-success">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/contracts/v1/source/doctrine_artifact_preflight_summary/valid/README.md`  
**Fixture posture:** valid JSON Schema fixture lane  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/source/doctrine_artifact_preflight_summary.schema.json`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Schema basis](#schema-basis) · [Why this fixture passes](#why-this-fixture-passes) · [Authority boundary](#authority-boundary) · [Harness behavior](#harness-behavior) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are expected to pass schema validation. They are not doctrine artifact preflight execution results, source admission decisions, receipts, provenance records, EvidenceBundles, ReleaseManifests, policy decisions, review approval, release approval, or publication authority.

---

## Purpose

This directory stores positive JSON examples for the `doctrine_artifact_preflight_summary` schema.

Use this lane to prove that a minimal, well-shaped doctrine artifact preflight summary can pass schema validation before higher-level maintenance, source admission, provenance, review, release, or documentation workflows rely on the shape. Passing this schema fixture proves shape only. It does not prove that the preflight script ran, doctrine artifacts are present, source provenance is complete, readiness checks passed, release gates passed, or public use is authorized.

---

## Current inventory

| File | Role | Expected result | Status |
|---|---|---|---|
| [`valid_1.json`](valid_1.json) | Minimal positive fixture for `doctrine_artifact_preflight_summary`. | Schema validation should pass. | CONFIRMED |

Current valid fixture:

```json
{
  "check_returncode": 1,
  "render_returncode": 0,
  "check_stderr": "",
  "render_stderr": "",
  "check_receipt": "receipts/doctrine_artifacts/check_required_doctrine_artifacts.20260513T000000Z.json",
  "presence_input": {
    "present": {
      "a.pdf": false
    }
  }
}
```

The paired negative fixture currently uses an out-of-range return code:

```json
{
  "check_returncode": 3,
  "render_returncode": 0,
  "check_receipt": "x",
  "presence_input": null
}
```

The paired expected-error matcher is:

```text
3 is not one of [0, 1, 2]
```

---

## Schema basis

The current schema evidence for this fixture lane is:

```text
schemas/contracts/v1/source/doctrine_artifact_preflight_summary.schema.json
```

Confirmed schema facts:

| Item | Value |
|---|---|
| Schema title | `doctrine_artifact_preflight_summary` |
| Root type | object |
| Required fields | `check_returncode`, `render_returncode`, `presence_input` |
| `check_returncode` enum values | `0`, `1`, `2` |
| `render_returncode` enum values | `0`, `2` |
| `check_stderr` / `render_stderr` | strings when present |
| `check_receipt` | non-empty string when present |
| `presence_input` | `null` or object requiring `present` object of boolean values |
| `presence_output` | non-empty string when present |
| provenance return codes | finite integer enums when present |
| provenance sync return codes | finite integer enums when present |
| alignment return codes | finite integer enums when present |
| readiness return codes | finite integer enums when present |
| digest fields | `null` or 64-character lowercase hexadecimal strings |
| `artifact_digests` | closed object requiring `check_receipt`, `provenance_sync_receipt`, and `presence_output` when present |
| `artifact_paths` | closed object requiring `check_receipt`, `provenance_sync_receipt`, and `presence_output` when present |
| readiness payload | `null` or object with `check`, `result`, `consumer_count`, and `errors` |
| Additional properties | false at the root |

---

## Why this fixture passes

`valid_1.json` includes all fields required by the paired schema:

- `check_returncode`
- `render_returncode`
- `presence_input`

It also uses schema-compatible values:

| Field | Fixture value | Schema posture |
|---|---|---|
| `check_returncode` | `1` | Allowed enum value. |
| `render_returncode` | `0` | Allowed enum value. |
| `check_stderr` | empty string | String. |
| `render_stderr` | empty string | String. |
| `check_receipt` | receipt path string | Non-empty string. |
| `presence_input.present.a.pdf` | `false` | Boolean value under the required `present` object. |

This positive fixture is intentionally minimal. It proves that a compact preflight-summary object can pass the machine schema, not that any receipt path resolves, any artifact exists, any provenance record is complete, or any release decision has been made.

> [!WARNING]
> A valid preflight-summary fixture is not a maintenance run result, not a doctrine artifact registry, not a source admission decision, and not release or publication approval.

---

## Authority boundary

| Responsibility | Home | Status in this check |
|---|---|---|
| Positive fixture examples | `fixtures/contracts/v1/source/doctrine_artifact_preflight_summary/valid/` | CONFIRMED |
| Negative fixture examples | `fixtures/contracts/v1/source/doctrine_artifact_preflight_summary/invalid/` | CONFIRMED fixture files |
| Machine-checkable shape | `schemas/contracts/v1/source/doctrine_artifact_preflight_summary.schema.json` | CONFIRMED |
| Semantic contract | `contracts/source/doctrine_artifact_preflight_summary.md` | NEEDS VERIFICATION |
| Dedicated validator implementation | `tools/validators/source/validate_doctrine_artifact_preflight_summary.py` | NEEDS VERIFICATION |
| Maintenance script | `scripts/maintenance/run_doctrine_artifact_preflight.py` | NEEDS VERIFICATION / NOT RUN |
| Common schema fixture harness | `tests/schemas/test_common_contracts.py` | CONFIRMED doctrine pattern from prior fixture work / NOT RUN |

Do not collapse this fixture lane into the preflight maintenance script, doctrine artifact registry, source admission workflow, provenance check, readiness check, receipt, EvidenceBundle, ReleaseManifest, policy decision, review approval, release approval, or publication authority.

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

This README documents expected fixture behavior only. It does not claim that pytest, CI, source admission policy, doctrine artifact preflight scripts, provenance checks, readiness checks, registry admission, release checks, or the dedicated DoctrineArtifactPreflightSummary validator were run during this update.

---

## Maintenance checklist

Before changing this valid fixture lane:

- [ ] Keep passing examples under `valid/valid_<n>.json`.
- [ ] Keep at least one minimal positive fixture unless the schema family is intentionally retired.
- [ ] Keep positive fixtures paired with negative fixtures under `../invalid/`.
- [ ] Add provenance payload, provenance sync payload, alignment payload, readiness payload, artifact path, artifact digest, and receipt digest positive fixtures when coverage expands.
- [ ] Keep return-code values inside the finite enums defined by the schema.
- [ ] Keep fixture examples public-safe and limited to summary-shaped metadata.
- [ ] Avoid private, unpublished, source-system, prompt-like, or policy-restricted content.
- [ ] Do not embed full doctrine artifacts, raw evidence payloads, or release-blocked material in fixtures.
- [ ] Update this README when schema fields, enum values, digest requirements, payload shapes, return-code semantics, or fixture coverage changes.
- [ ] Run the schema fixture test before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Valid fixture | CONFIRMED | `valid_1.json` exists and includes all currently required fields. |
| Invalid fixture | CONFIRMED | `../invalid/invalid_1.json` exists and uses invalid `check_returncode: 3`. |
| Expected-error file | CONFIRMED | `../invalid/invalid_1.expected_error.txt` exists and contains `3 is not one of [0, 1, 2]`. |
| Schema | CONFIRMED | `doctrine_artifact_preflight_summary.schema.json` defines required fields, finite return-code enums, payload shapes, digest patterns, artifact path/digest shapes, readiness payload shape, and root additional-property behavior. |
| Semantic contract | NEEDS VERIFICATION | A directly named semantic contract was not verified during this update. |
| Test execution | NOT RUN | No validators, pytest, source policy checks, doctrine preflight scripts, provenance checks, readiness checks, registry checks, steward review checks, release checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define valid-fixture guidance. |
| [`valid_1.json`](valid_1.json) | CONFIRMED | Current positive fixture includes all required fields and schema-compatible values. | Only one valid case is currently documented here. |
| [`../invalid/invalid_1.json`](../invalid/invalid_1.json) | CONFIRMED | Paired negative fixture uses invalid `check_returncode: 3`. | Only one invalid case is currently documented there. |
| [`../invalid/invalid_1.expected_error.txt`](../invalid/invalid_1.expected_error.txt) | CONFIRMED | Expected matcher pins the return-code enum failure. | Does not cover other possible schema failures. |
| [`../../../../../../schemas/contracts/v1/source/doctrine_artifact_preflight_summary.schema.json`](../../../../../../schemas/contracts/v1/source/doctrine_artifact_preflight_summary.schema.json) | CONFIRMED | Schema shape, required fields, enum values, payload shapes, digest patterns, artifact path/digest objects, readiness payload, and additional-property posture. | Semantic contract path is not verified here. |
| `../../../../../../docs/doctrine/directory-rules.md` | CONFIRMED doctrine | `fixtures/` is within the validate/operate authority surface and supports test inputs while contracts, schemas, policy, and lifecycle data remain separate roots. | Specific fixture completeness requires inventory and tests. |

[Back to top](#top)
