<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/policy/sensitivity-label/readme
title: sensitivity_label fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): policy steward; TODO(owner): sensitivity steward; TODO(owner): schema steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-06-30 expansion
updated: 2026-06-30
policy_label: public-review
related:
  - valid/README.md
  - valid/valid_1.json
  - invalid/README.md
  - invalid/invalid_1.json
  - invalid/invalid_1.expected_error.txt
  - ../../../../../schemas/contracts/v1/policy/sensitivity_label.schema.json
  - ../../../../../contracts/policy/sensitivity_label.md
  - ../../../../../contracts/policy/README.md
  - ../../../../../policy/sensitivity/
  - ../../../../../policy/domains/
  - ../../../../../policy/release/
  - ../../../../../tools/validators/validate_sensitivity_label.py
  - ../../../../../tests/schemas/test_common_contracts.py
  - ../../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, v1, policy, sensitivity-label, valid-fixtures, invalid-fixtures, expected-error, json-schema, sensitivity, exposure-posture, public, generalized, restricted, quarantine, fail-closed, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/contracts/v1/policy/sensitivity_label/README.md`."
  - "This directory is the schema-declared fixture root for `sensitivity_label`."
  - "Fixtures are sample test inputs only; semantic meaning, machine schema shape, executable policy, and release authority stay in their owning roots."
  - "Current fixture coverage includes one valid case and one invalid missing-required-field case."
  - "No tests, validators, policy bundles, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `sensitivity_label` fixtures

Fixture family for the KFM `sensitivity_label` policy contract schema.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Family: policy" src="https://img.shields.io/badge/family-policy-blue">
  <img alt="Contract: sensitivity_label" src="https://img.shields.io/badge/contract-sensitivity__label-purple">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
  <img alt="Levels: finite" src="https://img.shields.io/badge/levels-public%20%7C%20generalized%20%7C%20restricted%20%7C%20quarantine-informational">
</p>

**Path:** `fixtures/contracts/v1/policy/sensitivity_label/README.md`  
**Fixture posture:** JSON Schema valid/invalid fixture family  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/policy/sensitivity_label.schema.json`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Schema basis](#schema-basis) · [Authority boundary](#authority-boundary) · [Harness behavior](#harness-behavior) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are schema fixtures. They are not executable sensitivity policy, public-release approval, review approval, evidence, receipts, proofs, runtime envelopes, semantic contract authority, or publication authority.

---

## Purpose

This directory groups positive and negative JSON fixtures for the `sensitivity_label` schema.

Use this fixture family to verify that KFM accepts a minimal well-shaped `SensitivityLabel`-like object and rejects an incomplete one. The schema-declared fixture root is:

```text
fixtures/contracts/v1/policy/sensitivity_label/
```

A passing fixture proves schema shape only. It does not prove that executable sensitivity policy ran, that a label is safe for a specific audience or operation, that release gates passed, that evidence and rights are sufficient, or that a public API, map, or AI surface may render the labeled material.

---

## Current inventory

| Lane | File | Current role | Status |
|---|---|---|---|
| [`valid/`](valid/README.md) | [`valid_1.json`](valid/valid_1.json) | Minimal positive fixture with every required top-level field and an allowed `level` value. | CONFIRMED |
| [`invalid/`](invalid/README.md) | [`invalid_1.json`](invalid/invalid_1.json) | Minimal negative fixture matching the positive case but missing required `level`. | CONFIRMED |
| [`invalid/`](invalid/README.md) | [`invalid_1.expected_error.txt`](invalid/invalid_1.expected_error.txt) | Current expected-error matcher: `required`. | CONFIRMED / BROAD MATCHER |

Current positive fixture shape:

```json
{
  "level": "public",
  "reason": "safe",
  "applied_at": "2026-05-09T00:00:00Z"
}
```

Current negative fixture shape:

```json
{
  "reason": "safe",
  "applied_at": "2026-05-09T00:00:00Z"
}
```

---

## Schema basis

The current schema evidence for this fixture family is:

```text
schemas/contracts/v1/policy/sensitivity_label.schema.json
```

Confirmed schema facts:

| Item | Value |
|---|---|
| Schema title | `sensitivity_label` |
| Root type | object |
| Required fields | `level`, `reason`, `applied_at` |
| `level` enum values | `public`, `generalized`, `restricted`, `quarantine` |
| `reason` | string |
| `applied_at` | string with `date-time` format |
| Additional properties | false |
| Declared contract doc | `contracts/policy/sensitivity_label.md` |
| Declared fixture root | `fixtures/contracts/v1/policy/sensitivity_label/` |
| Declared validator | `tools/validators/validate_sensitivity_label.py` |
| Declared policy path | `policy/policy/` |
| Schema status | `PROPOSED` |

---

## Authority boundary

| Responsibility | Home | Status in this check |
|---|---|---|
| Fixture examples | `fixtures/contracts/v1/policy/sensitivity_label/` | CONFIRMED |
| Valid examples | `fixtures/contracts/v1/policy/sensitivity_label/valid/` | CONFIRMED |
| Invalid examples | `fixtures/contracts/v1/policy/sensitivity_label/invalid/` | CONFIRMED |
| Machine-checkable shape | `schemas/contracts/v1/policy/sensitivity_label.schema.json` | CONFIRMED |
| Semantic contract | `contracts/policy/sensitivity_label.md` | CONFIRMED |
| Executable sensitivity rules | `policy/sensitivity/`, `policy/domains/`, `policy/release/` | OUT OF SCOPE FOR THIS README |
| Validator implementation | `tools/validators/validate_sensitivity_label.py` | NEEDS VERIFICATION |
| Schema test harness | `tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN |

`SensitivityLabel` must remain distinguishable from:

| Do not collapse `SensitivityLabel` into | Why |
|---|---|
| `PolicyDecision` | A sensitivity label supplies exposure context; policy decisions record evaluated gate outcomes. |
| `PolicyInputBundle` | The bundle is input to policy evaluation; the label is one policy-relevant datum. |
| `DecisionEnvelope` | The envelope transports runtime context and decisions; this object records an exposure posture. |
| `ReleaseManifest` | Release manifests bind released contents; a sensitivity label alone does not publish anything. |
| `ReviewRecord` | Review records capture steward/human/governed-process review; labels record exposure posture. |
| `EvidenceBundle` | Evidence supports claims; labels do not prove the underlying evidence true. |
| Receipt/proof artifacts | Receipts/proofs audit process and integrity; they do not replace the label object or its schema. |

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

For this policy family, that means:

```text
fixtures/contracts/v1/policy/sensitivity_label/
```

Observed expectations:

| Fixture pattern | Expected result |
|---|---|
| `valid/valid_*.json` | no JSON Schema errors |
| `invalid/invalid_*.json` | at least one JSON Schema error |
| `invalid/invalid_*.expected_error.txt` | expected text appears in combined error messages |

This README documents expected fixture behavior only. It does not claim that pytest, CI, policy bundles, or the dedicated sensitivity-label validator was run during this update.

---

## Maintenance checklist

Before changing this fixture family:

- [ ] Keep passing examples under `valid/valid_<n>.json`.
- [ ] Keep failing examples under `invalid/invalid_<n>.json`.
- [ ] Keep expected-error text beside the invalid fixture it describes.
- [ ] Keep fixture cases small, deterministic, public-safe, and reviewable.
- [ ] Keep at least one valid minimal fixture and one missing-required-field invalid fixture.
- [ ] Add enum, date-time, and additional-property fixtures as coverage expands.
- [ ] Add examples for `generalized`, `restricted`, and `quarantine` only when they remain public-safe and reviewable.
- [ ] Avoid sensitive, private, unpublished, source-system, or policy-restricted content.
- [ ] Never place sensitive values, exact protected coordinates, DNA/genomic details, living-person private identifiers, sacred-site identifiers, infrastructure vulnerabilities, or private source content in fixture `reason` text.
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
| Schema | CONFIRMED | `sensitivity_label.schema.json` defines required fields, enum values, date-time format, fixture root, and additional-property behavior. |
| Contract | CONFIRMED | `contracts/policy/sensitivity_label.md` defines semantic meaning and separates schema, executable policy, runtime, release, and fixture authority. |
| Validator file | NEEDS VERIFICATION | `tools/validators/validate_sensitivity_label.py` is declared by schema but implementation/wiring was not verified during this update. |
| Test execution | NOT RUN | No validators, pytest, policy tests, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define fixture-family guidance. |
| [`valid/README.md`](valid/README.md) | CONFIRMED | Positive fixture lane guidance. | Does not prove tests were run. |
| [`valid/valid_1.json`](valid/valid_1.json) | CONFIRMED | Current positive fixture includes required fields and an allowed finite `level`. | Only one valid fixture is currently documented. |
| [`invalid/README.md`](invalid/README.md) | CONFIRMED | Negative fixture lane guidance. | Does not prove tests were run. |
| [`invalid/invalid_1.json`](invalid/invalid_1.json) | CONFIRMED | Current negative fixture omits required `level`. | Only one invalid fixture is currently documented. |
| [`invalid/invalid_1.expected_error.txt`](invalid/invalid_1.expected_error.txt) | CONFIRMED | Current expected-error matcher is `required`. | Broad matcher; may be tightened later. |
| [`../../../../../schemas/contracts/v1/policy/sensitivity_label.schema.json`](../../../../../schemas/contracts/v1/policy/sensitivity_label.schema.json) | CONFIRMED | Schema shape, required fields, enum values, date-time format, fixture root, validator path, and status. | Schema status is `PROPOSED`; validator implementation was not verified. |
| [`../../../../../contracts/policy/sensitivity_label.md`](../../../../../contracts/policy/sensitivity_label.md) | CONFIRMED | Semantic meaning, finite exposure-level boundary, fail-closed posture, and distinction from schema, executable policy, release, and runtime envelopes. | Does not prove policy runtime enforcement or CI status. |
| `../../../../../tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN | Fixture discovery and valid/invalid fixture behavior. | Tests were not run during this update. |
| `../../../../../docs/doctrine/directory-rules.md` | CONFIRMED | `fixtures/` is the root for golden, valid, and invalid test inputs; contracts/schemas/policy split remains separate. | Specific fixture completeness requires tests or inventory. |

[Back to top](#top)
