<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/source/doctrine-artifact-preflight-summary/readme
title: doctrine_artifact_preflight_summary fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): doctrine steward; TODO(owner): source steward; TODO(owner): schema steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): maintenance steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-06-30 expansion
updated: 2026-06-30
policy_label: public-review
related:
  - valid/valid_1.json
  - invalid/README.md
  - invalid/invalid_1.json
  - invalid/invalid_1.expected_error.txt
  - ../../../../../schemas/contracts/v1/source/doctrine_artifact_preflight_summary.schema.json
  - ../../../../../tools/validators/source/validate_doctrine_artifact_preflight_summary.py
  - ../../../../../scripts/maintenance/run_doctrine_artifact_preflight.py
  - ../../../../../tests/source/test_doctrine_artifact_preflight_summary_schema.py
  - ../../../../../tests/policy/test_preflight_summary_schema_contract.py
  - ../../../../../tests/schemas/test_common_contracts.py
  - ../../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, v1, source, doctrine-artifact-preflight-summary, valid-fixtures, invalid-fixtures, expected-error, json-schema, doctrine, preflight, returncode, receipt, provenance, readiness, maintenance, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/contracts/v1/source/doctrine_artifact_preflight_summary/README.md`."
  - "This directory is the fixture family for `doctrine_artifact_preflight_summary`."
  - "Fixtures are sample test inputs only; schema shape, maintenance-script behavior, source admission, steward review, policy behavior, and release authority stay in their owning roots."
  - "Current fixture coverage includes one valid preflight-summary example and one invalid return-code enum example."
  - "No tests, validators, doctrine artifact preflight scripts, source admission workflows, steward review workflows, policy checks, release checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `doctrine_artifact_preflight_summary` fixtures

Fixture family for the KFM `doctrine_artifact_preflight_summary` source contract schema.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Family: source" src="https://img.shields.io/badge/family-source-blue">
  <img alt="Contract: doctrine_artifact_preflight_summary" src="https://img.shields.io/badge/contract-doctrine__artifact__preflight__summary-purple">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
  <img alt="Return codes: finite" src="https://img.shields.io/badge/return__codes-finite-informational">
</p>

**Path:** `fixtures/contracts/v1/source/doctrine_artifact_preflight_summary/README.md`  
**Fixture posture:** JSON Schema valid/invalid fixture family  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/source/doctrine_artifact_preflight_summary.schema.json`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Schema basis](#schema-basis) · [Authority boundary](#authority-boundary) · [Harness behavior](#harness-behavior) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are schema fixtures. They are not doctrine artifact preflight execution results, source admission decisions, receipts, provenance records, EvidenceBundles, ReleaseManifests, policy decisions, release approval, review approval, or publication authority.

---

## Purpose

This directory groups positive and negative JSON fixtures for the `doctrine_artifact_preflight_summary` schema.

Use this fixture family to verify that KFM accepts a minimal well-shaped doctrine artifact preflight summary and rejects summary-shaped metadata that falls outside the finite return-code contract. The fixture family keeps source-maintenance summary shapes testable without treating fixture examples as real preflight output, source truth, review proof, release approval, or implementation proof.

A passing fixture proves schema shape only. It does not prove the preflight script ran, doctrine artifacts are present, provenance is complete, readiness checks passed, source admission is approved, or release gates passed.

---

## Current inventory

| Lane | File | Current role | Status |
|---|---|---|---|
| `valid/` | [`valid_1.json`](valid/valid_1.json) | Minimal positive fixture with allowed return codes, string stderr fields, receipt path, and valid `presence_input`. | CONFIRMED |
| [`invalid/`](invalid/README.md) | [`invalid_1.json`](invalid/invalid_1.json) | Negative fixture with invalid `check_returncode: 3`. | CONFIRMED |
| [`invalid/`](invalid/README.md) | [`invalid_1.expected_error.txt`](invalid/invalid_1.expected_error.txt) | Expected-error matcher: `3 is not one of [0, 1, 2]`. | CONFIRMED |

Current positive fixture shape:

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

Current negative fixture shape:

```json
{
  "check_returncode": 3,
  "render_returncode": 0,
  "check_receipt": "x",
  "presence_input": null
}
```

---

## Schema basis

The current schema evidence for this fixture family is:

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
| `presence_input` | `null` or object with required `present` object of boolean values |
| `presence_output` | non-empty string when present |
| provenance return codes | finite integer enums when present |
| provenance sync return codes | finite integer enums when present |
| alignment return codes | finite integer enums when present |
| readiness return codes | finite integer enums when present |
| digest fields | `null` or 64-character lowercase hexadecimal strings |
| `artifact_digests` | object requiring `check_receipt`, `provenance_sync_receipt`, and `presence_output` when present |
| `artifact_paths` | object requiring `check_receipt`, `provenance_sync_receipt`, and `presence_output` when present |
| readiness payload | `null` or object with `check`, `result`, `consumer_count`, and `errors` |
| Additional properties | false at the root |

---

## Authority boundary

| Responsibility | Home | Status in this check |
|---|---|---|
| Fixture examples | `fixtures/contracts/v1/source/doctrine_artifact_preflight_summary/` | CONFIRMED |
| Valid examples | `fixtures/contracts/v1/source/doctrine_artifact_preflight_summary/valid/` | CONFIRMED fixture file |
| Invalid examples | `fixtures/contracts/v1/source/doctrine_artifact_preflight_summary/invalid/` | CONFIRMED fixture file and README |
| Machine-checkable shape | `schemas/contracts/v1/source/doctrine_artifact_preflight_summary.schema.json` | CONFIRMED |
| Semantic contract | `contracts/source/doctrine_artifact_preflight_summary.md` | NEEDS VERIFICATION |
| Dedicated validator implementation | `tools/validators/source/validate_doctrine_artifact_preflight_summary.py` | FOUND BY SEARCH / NEEDS VERIFICATION |
| Maintenance script | `scripts/maintenance/run_doctrine_artifact_preflight.py` | FOUND BY SEARCH / NOT RUN |
| Dedicated source schema test | `tests/source/test_doctrine_artifact_preflight_summary_schema.py` | FOUND BY SEARCH / NOT RUN |
| Policy schema-contract test | `tests/policy/test_preflight_summary_schema_contract.py` | FOUND BY SEARCH / NOT RUN |
| Common schema fixture harness | `tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN |

`doctrine_artifact_preflight_summary` must remain distinguishable from:

| Do not collapse this fixture family into | Why |
|---|---|
| Preflight execution output | Fixtures are static test inputs, not proof the script ran. |
| Source admission decision | Admission still requires governed source/review/policy flow. |
| Receipt or provenance record | The schema may reference receipt paths and provenance payloads, but fixtures do not replace those records. |
| Steward review proof | Review and signoff records must live in their owning roots. |
| EvidenceBundle | Evidence supports claims; preflight summaries are maintenance summary shapes. |
| ReleaseManifest | Release manifests bind released contents; a fixture cannot approve release. |
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
fixtures/contracts/v1/source/doctrine_artifact_preflight_summary/
```

Observed expectations:

| Fixture pattern | Expected result |
|---|---|
| `valid/valid_*.json` | no JSON Schema errors |
| `invalid/invalid_*.json` | at least one JSON Schema error |
| `invalid/invalid_*.expected_error.txt` | expected text appears in combined schema error messages |

This README documents expected fixture behavior only. It does not claim that pytest, CI, source admission policy, doctrine artifact preflight scripts, provenance checks, readiness checks, registry admission, release checks, or the dedicated DoctrineArtifactPreflightSummary validator was run during this update.

---

## Maintenance checklist

Before changing this fixture family:

- [ ] Keep passing examples under `valid/valid_<n>.json`.
- [ ] Keep failing examples under `invalid/invalid_<n>.json`.
- [ ] Keep expected-error text beside the invalid fixture it describes.
- [ ] Keep at least one minimal positive fixture and one bounded-return-code invalid fixture.
- [ ] Add required-field, render-returncode enum, presence-input shape, digest-pattern, artifact-path, artifact-digest, payload-const, readiness-payload, and additional-property fixtures as coverage expands.
- [ ] Keep fixture cases small, deterministic, public-safe, and reviewable.
- [ ] Avoid private, unpublished, source-system, prompt-like, or policy-restricted content.
- [ ] Do not embed full doctrine artifacts, raw evidence payloads, protected location detail, credentials, or release-blocked material in fixtures.
- [ ] Update parent and lane READMEs when schema fields, enum values, digest requirements, payload shapes, return-code semantics, or fixture coverage changes.
- [ ] Run the common schema fixture test before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Valid fixture | CONFIRMED | `valid/valid_1.json` exists and uses allowed return-code values plus valid `presence_input`. |
| Invalid lane | CONFIRMED | `invalid/README.md`, `invalid/invalid_1.json`, and `invalid_1.expected_error.txt` exist. |
| Schema | CONFIRMED | `doctrine_artifact_preflight_summary.schema.json` defines required fields, finite return-code enums, payload shapes, digest patterns, artifact path/digest shapes, readiness payload shape, and root additional-property behavior. |
| Semantic contract | NEEDS VERIFICATION | No semantic contract was verified during this update; schema evidence is the verified machine contract. |
| Test execution | NOT RUN | No validators, pytest, source policy checks, doctrine preflight scripts, registry checks, steward review checks, release checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define fixture-family guidance. |
| [`valid/valid_1.json`](valid/valid_1.json) | CONFIRMED | Current positive fixture uses allowed return codes and valid `presence_input`. | Only one valid fixture is currently documented. |
| [`invalid/README.md`](invalid/README.md) | CONFIRMED | Negative fixture lane guidance. | Does not prove tests were run. |
| [`invalid/invalid_1.json`](invalid/invalid_1.json) | CONFIRMED | Current negative fixture has invalid `check_returncode: 3`. | Only one invalid fixture is currently documented. |
| [`invalid/invalid_1.expected_error.txt`](invalid/invalid_1.expected_error.txt) | CONFIRMED | Current expected matcher pins the return-code enum failure. | Does not cover other possible schema failures. |
| [`../../../../../schemas/contracts/v1/source/doctrine_artifact_preflight_summary.schema.json`](../../../../../schemas/contracts/v1/source/doctrine_artifact_preflight_summary.schema.json) | CONFIRMED | Schema shape, required fields, enum values, payload shapes, digest patterns, artifact path/digest objects, readiness payload, and additional-property posture. | Semantic contract path is not verified here. |
| `../../../../../tools/validators/source/validate_doctrine_artifact_preflight_summary.py` | FOUND BY SEARCH / NEEDS VERIFICATION | Dedicated validator path exists in repository search results. | Implementation and wiring were not inspected or run. |
| `../../../../../scripts/maintenance/run_doctrine_artifact_preflight.py` | FOUND BY SEARCH / NOT RUN | Maintenance script path exists in repository search results. | Script behavior was not inspected or run. |
| `../../../../../tests/source/test_doctrine_artifact_preflight_summary_schema.py` | FOUND BY SEARCH / NOT RUN | Dedicated schema test path exists in repository search results. | Test behavior was not inspected or run. |
| `../../../../../tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN | Common fixture discovery and valid/invalid fixture behavior. | Tests were not run during this update. |
| `../../../../../docs/doctrine/directory-rules.md` | CONFIRMED | `fixtures/` is the root for golden, valid, and invalid test inputs; contracts/schemas/policy split remains separate. | Specific fixture completeness requires tests or inventory. |

[Back to top](#top)
