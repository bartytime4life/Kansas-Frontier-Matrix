<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/source/doctrine-artifact-preflight-summary/invalid/readme
title: doctrine_artifact_preflight_summary invalid fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): doctrine steward; TODO(owner): source steward; TODO(owner): schema steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): maintenance steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-06-30 expansion
updated: 2026-06-30
policy_label: public-review
related:
  - ../valid/valid_1.json
  - invalid_1.json
  - invalid_1.expected_error.txt
  - ../../../../../../schemas/contracts/v1/source/doctrine_artifact_preflight_summary.schema.json
  - ../../../../../../tools/validators/source/validate_doctrine_artifact_preflight_summary.py
  - ../../../../../../scripts/maintenance/run_doctrine_artifact_preflight.py
  - ../../../../../../tests/source/test_doctrine_artifact_preflight_summary_schema.py
  - ../../../../../../tests/policy/test_preflight_summary_schema_contract.py
  - ../../../../../../tests/schemas/test_common_contracts.py
  - ../../../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, v1, source, doctrine-artifact-preflight-summary, invalid-fixtures, expected-error, json-schema, doctrine, preflight, returncode, receipt, provenance, readiness, maintenance, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/contracts/v1/source/doctrine_artifact_preflight_summary/invalid/README.md`."
  - "Invalid fixtures are intentionally failing examples for the `doctrine_artifact_preflight_summary` schema."
  - "Current invalid fixture coverage is one enum failure: `invalid_1.json` uses `check_returncode: 3`, while the schema allows only `0`, `1`, or `2`."
  - "A semantic contract file was not found by the `doctrine_artifact_preflight_summary` repository search used during this update; schema, validator, maintenance script, and tests were found."
  - "No tests, validators, doctrine artifact preflight scripts, source admission workflows, steward review workflows, policy checks, release checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `doctrine_artifact_preflight_summary` invalid fixtures

Negative fixture lane for the KFM `doctrine_artifact_preflight_summary` source contract schema.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Family: source" src="https://img.shields.io/badge/family-source-blue">
  <img alt="Contract: doctrine_artifact_preflight_summary" src="https://img.shields.io/badge/contract-doctrine__artifact__preflight__summary-purple">
  <img alt="Lane: invalid" src="https://img.shields.io/badge/lane-invalid-critical">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/contracts/v1/source/doctrine_artifact_preflight_summary/invalid/README.md`  
**Fixture posture:** invalid JSON Schema fixture lane  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/source/doctrine_artifact_preflight_summary.schema.json`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Schema basis](#schema-basis) · [Why this fixture fails](#why-this-fixture-fails) · [Authority boundary](#authority-boundary) · [Harness behavior](#harness-behavior) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are expected to fail schema validation. They are not preflight execution results, doctrine artifact admission decisions, receipts, provenance records, source truth, policy decisions, release approval, review approval, or publication authority.

---

## Purpose

This directory stores negative JSON examples for the `doctrine_artifact_preflight_summary` schema.

Use this lane to prove that malformed or out-of-contract doctrine artifact preflight summaries are rejected before they can be treated as governed source-maintenance outputs. Invalid fixtures help protect KFM's source and doctrine-artifact admission boundary: preflight summaries may record checks, return codes, receipts, provenance payloads, synchronization payloads, alignment payloads, readiness payloads, paths, and digests, but fixture shape alone must not become source truth, policy approval, review proof, or release authority.

---

## Current inventory

| File | Role | Expected result | Status |
|---|---|---|---|
| [`invalid_1.json`](invalid_1.json) | Negative fixture with invalid `check_returncode`. | Schema validation should fail. | CONFIRMED |
| [`invalid_1.expected_error.txt`](invalid_1.expected_error.txt) | Expected-error matcher for `invalid_1.json`. | Combined schema errors should include `3 is not one of [0, 1, 2]`. | CONFIRMED |

Current invalid fixture:

```json
{
  "check_returncode": 3,
  "render_returncode": 0,
  "check_receipt": "x",
  "presence_input": null
}
```

The paired positive fixture currently uses an allowed `check_returncode`, an allowed `render_returncode`, a receipt path string, and a valid `presence_input` object:

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
| `presence_input` | `null` or object with required `present` object of boolean values |
| `presence_output` | non-empty string when present |
| provenance/alignment/readiness return codes | finite integer enums when present |
| digest fields | `null` or 64-character lowercase hexadecimal strings |
| `artifact_digests` | object requiring `check_receipt`, `provenance_sync_receipt`, and `presence_output` when present |
| `artifact_paths` | object requiring `check_receipt`, `provenance_sync_receipt`, and `presence_output` when present |
| Additional properties | false at the root |

---

## Why this fixture fails

`invalid_1.json` fails the current schema because its `check_returncode` value is:

```text
3
```

The paired schema only allows:

```text
0, 1, 2
```

The expected-error file pins that enum failure:

```text
3 is not one of [0, 1, 2]
```

That failure matters because preflight summaries use finite return-code values to communicate bounded check outcomes. Allowing an unrecognized return code would weaken downstream interpretation, automated maintenance checks, readiness reporting, and governance review.

> [!WARNING]
> A `doctrine_artifact_preflight_summary` fixture is not evidence that the preflight script ran, that doctrine artifacts are present, that provenance is complete, that source admission is approved, or that release gates passed. It is only a schema-shaped test input.

---

## Authority boundary

| Responsibility | Home | Status in this check |
|---|---|---|
| Negative fixture examples | `fixtures/contracts/v1/source/doctrine_artifact_preflight_summary/invalid/` | CONFIRMED |
| Positive fixture examples | `fixtures/contracts/v1/source/doctrine_artifact_preflight_summary/valid/` | CONFIRMED file present / README not checked in this update |
| Machine-checkable shape | `schemas/contracts/v1/source/doctrine_artifact_preflight_summary.schema.json` | CONFIRMED |
| Semantic contract | `contracts/source/doctrine_artifact_preflight_summary.md` | NOT FOUND BY SEARCH / NEEDS VERIFICATION |
| Dedicated validator implementation | `tools/validators/source/validate_doctrine_artifact_preflight_summary.py` | FOUND BY SEARCH / NEEDS VERIFICATION |
| Maintenance script | `scripts/maintenance/run_doctrine_artifact_preflight.py` | FOUND BY SEARCH / NOT RUN |
| Dedicated source schema test | `tests/source/test_doctrine_artifact_preflight_summary_schema.py` | FOUND BY SEARCH / NOT RUN |
| Policy schema-contract test | `tests/policy/test_preflight_summary_schema_contract.py` | FOUND BY SEARCH / NOT RUN |
| Common schema fixture harness | `tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN |

Do not collapse this fixture lane into the schema, validator, maintenance script, source admission workflow, doctrine registry, executable policy, steward review workflow, receipts, provenance records, EvidenceBundle, ReleaseManifest, source truth, or publication authority.

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

This README documents expected fixture behavior only. It does not claim that pytest, CI, source admission policy, doctrine artifact preflight scripts, provenance checks, readiness checks, registry admission, release checks, or the dedicated DoctrineArtifactPreflightSummary validator were run during this update.

---

## Maintenance checklist

Before changing this invalid fixture lane:

- [ ] Keep failing examples under `invalid/invalid_<n>.json`.
- [ ] Keep expected-error text beside the invalid fixture it describes.
- [ ] Keep at least one enum failure for bounded return-code handling unless another fixture family covers that failure class.
- [ ] Add required-field, render-returncode enum, presence-input shape, digest-pattern, artifact-path, artifact-digest, payload-const, readiness-payload, and additional-property failures when coverage expands.
- [ ] Keep fixture examples public-safe and limited to summary-shaped metadata.
- [ ] Avoid private, unpublished, source-system, prompt-like, or policy-restricted content.
- [ ] Do not embed full doctrine artifacts, raw evidence payloads, protected location detail, credentials, or release-blocked material in fixtures.
- [ ] Update this README when schema fields, enum values, digest requirements, payload shape, return-code semantics, or expected-error behavior changes.
- [ ] Run the schema fixture test before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Invalid fixture | CONFIRMED | `invalid_1.json` exists and uses invalid `check_returncode: 3`. |
| Expected-error file | CONFIRMED | `invalid_1.expected_error.txt` exists and pins the enum failure. |
| Positive fixture | CONFIRMED | `valid/valid_1.json` exists and uses allowed return-code values plus valid `presence_input`. |
| Schema | CONFIRMED | `doctrine_artifact_preflight_summary.schema.json` defines required fields, finite return-code enums, payload shapes, digest patterns, artifact path/digest shapes, readiness payload shape, and root additional-property behavior. |
| Semantic contract | NEEDS VERIFICATION | Repository search did not return `contracts/source/doctrine_artifact_preflight_summary.md`; the schema itself is the verified machine contract in this update. |
| Test execution | NOT RUN | No validators, pytest, source policy checks, doctrine preflight scripts, registry checks, steward review checks, release checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define invalid-fixture guidance. |
| [`invalid_1.json`](invalid_1.json) | CONFIRMED | Current negative fixture has invalid `check_returncode: 3`. | Only one invalid case is currently documented here. |
| [`invalid_1.expected_error.txt`](invalid_1.expected_error.txt) | CONFIRMED | Expected matcher pins the return-code enum failure. | Does not cover other possible schema failures. |
| [`../valid/valid_1.json`](../valid/valid_1.json) | CONFIRMED | Paired positive fixture uses allowed return codes and valid `presence_input`. | Positive lane README was not checked during this update. |
| [`../../../../../../schemas/contracts/v1/source/doctrine_artifact_preflight_summary.schema.json`](../../../../../../schemas/contracts/v1/source/doctrine_artifact_preflight_summary.schema.json) | CONFIRMED | Schema shape, required fields, enum values, payload shapes, digest patterns, artifact path/digest objects, readiness payload, and additional-property posture. | Schema does not include an `x-kfm` contract doc block in the fetched content. |
| `../../../../../../tools/validators/source/validate_doctrine_artifact_preflight_summary.py` | FOUND BY SEARCH / NEEDS VERIFICATION | Dedicated validator path exists in repository search results. | Implementation and wiring were not inspected or run. |
| `../../../../../../scripts/maintenance/run_doctrine_artifact_preflight.py` | FOUND BY SEARCH / NOT RUN | Maintenance script path exists in repository search results. | Script behavior was not inspected or run. |
| `../../../../../../tests/source/test_doctrine_artifact_preflight_summary_schema.py` | FOUND BY SEARCH / NOT RUN | Dedicated schema test path exists in repository search results. | Test behavior was not inspected or run. |
| `../../../../../../tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN | Common fixture discovery and invalid fixture behavior. | Tests were not run during this update. |
| `../../../../../../docs/doctrine/directory-rules.md` | CONFIRMED | `fixtures/` is the root for golden, valid, and invalid test inputs; contracts/schemas/policy split remains separate. | Specific fixture completeness requires tests or inventory. |

[Back to top](#top)
