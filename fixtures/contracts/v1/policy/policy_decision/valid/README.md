<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/policy/policy-decision/valid/readme
title: policy_decision valid fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): policy steward; TODO(owner): schema steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-06-30 expansion
updated: 2026-06-30
policy_label: public-review
related:
  - valid_1.json
  - ../invalid/README.md
  - ../invalid/invalid_1.json
  - ../invalid/invalid_1.expected_error.txt
  - ../../../../../../schemas/contracts/v1/policy/policy_decision.schema.json
  - ../../../../../../contracts/policy/policy_decision.md
  - ../../../../../../contracts/policy/policy_decision/README.md
  - ../../../../../../policy/
  - ../../../../../../tools/validators/validate_policy_decision.py
  - ../../../../../../tests/schemas/test_common_contracts.py
  - ../../../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, v1, policy, policy-decision, valid-fixtures, json-schema, finite-outcomes, fail-closed, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/contracts/v1/policy/policy_decision/valid/README.md`."
  - "Valid fixtures are positive schema examples for the `policy_decision` schema."
  - "Current valid fixture coverage is one minimal passing case: `valid_1.json`."
  - "No tests, validators, policy bundles, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `policy_decision` valid fixtures

Positive fixture lane for the KFM `policy_decision` contract schema.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Family: policy" src="https://img.shields.io/badge/family-policy-blue">
  <img alt="Contract: policy_decision" src="https://img.shields.io/badge/contract-policy__decision-purple">
  <img alt="Lane: valid" src="https://img.shields.io/badge/lane-valid-success">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/contracts/v1/policy/policy_decision/valid/README.md`  
**Fixture posture:** valid JSON Schema fixture lane  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/policy/policy_decision.schema.json`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Schema basis](#schema-basis) · [Why this fixture passes](#why-this-fixture-passes) · [Authority boundary](#authority-boundary) · [Harness behavior](#harness-behavior) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are expected to pass schema validation. They are not executable policy, policy approval, release approval, review approval, evidence, receipts, proofs, or runtime transport envelopes.

---

## Purpose

This directory stores positive JSON examples for the `policy_decision` schema.

Use this lane to prove that a minimal well-shaped `PolicyDecision`-like object can pass schema validation before it is used by higher-level policy, runtime, release, review, or publication workflows. Passing this schema fixture only proves shape. It does not prove that the policy evaluation was authorized, that policy bundles ran, that release gates passed, or that a public surface may render the decision.

---

## Current inventory

| File | Role | Expected result | Status |
|---|---|---|---|
| [`valid_1.json`](valid_1.json) | Minimal positive fixture for `policy_decision`. | Schema validation should pass. | CONFIRMED |

Current valid fixture:

```json
{
  "decision_id": "pd1",
  "outcome": "ABSTAIN",
  "policy_family": "access",
  "reasons": ["none"],
  "obligations": [],
  "evaluated_at": "2026-05-09T00:00:00Z"
}
```

The paired negative fixture currently omits the required `decision_id` field and is expected to fail with a `required` error:

```json
{
  "outcome": "ABSTAIN",
  "policy_family": "access",
  "reasons": ["none"],
  "obligations": [],
  "evaluated_at": "2026-05-09T00:00:00Z"
}
```

---

## Schema basis

The current schema evidence for this fixture lane is:

```text
schemas/contracts/v1/policy/policy_decision.schema.json
```

Confirmed schema facts:

| Item | Value |
|---|---|
| Schema title | `policy_decision` |
| Root type | object |
| Required fields | `decision_id`, `outcome`, `policy_family`, `reasons`, `obligations`, `evaluated_at` |
| `decision_id` | string matching `^[a-z][a-z0-9_:.-]*$` |
| `outcome` enum values | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` |
| `policy_family` enum values | `promotion`, `access`, `render`, `capability`, `consent`, `sensitivity` |
| `evaluated_at` | string with `date-time` format |
| Additional properties | false |
| Declared contract doc | `contracts/policy/policy_decision.md` |
| Declared fixture root | `fixtures/contracts/v1/policy/policy_decision/` |
| Declared validator | `tools/validators/validate_policy_decision.py` |
| Declared policy path | `policy/policy/` |
| Schema status | `PROPOSED` |

---

## Why this fixture passes

`valid_1.json` includes every field currently required by the paired schema:

- `decision_id`
- `outcome`
- `policy_family`
- `reasons`
- `obligations`
- `evaluated_at`

It also uses schema-allowed enum values:

| Field | Fixture value | Schema posture |
|---|---|---|
| `outcome` | `ABSTAIN` | Allowed finite outcome. |
| `policy_family` | `access` | Allowed policy family. |

This positive fixture is intentionally minimal. It proves the schema accepts a compact policy-decision object, not that the decision is complete enough for release, publication, review, audit, rollback, or public rendering.

---

## Authority boundary

| Responsibility | Home | Status in this check |
|---|---|---|
| Positive fixture examples | `fixtures/contracts/v1/policy/policy_decision/valid/` | CONFIRMED |
| Negative fixture examples | `fixtures/contracts/v1/policy/policy_decision/invalid/` | CONFIRMED |
| Machine-checkable shape | `schemas/contracts/v1/policy/policy_decision.schema.json` | CONFIRMED |
| Semantic contract | `contracts/policy/policy_decision.md` | CONFIRMED |
| Executable policy rules | `policy/` | OUT OF SCOPE FOR THIS README |
| Validator implementation | `tools/validators/validate_policy_decision.py` | NEEDS VERIFICATION |
| Schema test harness | `tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN |

Do not collapse this fixture lane into the semantic contract, schema, policy bundle, release gate, runtime decision envelope, evidence bundle, review record, or receipt/proof object.

---

## Harness behavior

The common schema test harness discovers fixture families under:

```text
fixtures/contracts/v1/<family>/<name>/
```

For valid fixtures, the observed harness pattern is:

```text
valid/valid_*.json
```

Expected behavior:

| Fixture pattern | Expected result |
|---|---|
| `valid/valid_*.json` | No JSON Schema errors. |

This README documents expected fixture behavior only. It does not claim that pytest, CI, policy bundles, or dedicated policy-decision validators were run during this update.

---

## Maintenance checklist

Before changing this valid fixture lane:

- [ ] Keep passing examples under `valid/valid_<n>.json`.
- [ ] Keep at least one minimal positive fixture unless the schema family is intentionally retired.
- [ ] Add richer valid fixtures only when they remain public-safe and reviewable.
- [ ] Keep positive fixtures paired with negative fixtures under `../invalid/`.
- [ ] Avoid sensitive, private, unpublished, or policy-restricted content.
- [ ] Update this README when schema fields, enum values, or fixture coverage changes.
- [ ] Run the schema fixture test before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Valid fixture | CONFIRMED | `valid_1.json` exists and includes all schema-required fields. |
| Invalid lane README | CONFIRMED | `../invalid/README.md` exists and documents the missing-`decision_id` negative case. |
| Invalid fixture | CONFIRMED | `../invalid/invalid_1.json` exists and omits required `decision_id`. |
| Expected-error file | CONFIRMED | `../invalid/invalid_1.expected_error.txt` exists and contains `required`. |
| Parent fixture README | NOT FOUND | `fixtures/contracts/v1/policy/policy_decision/README.md` was not found during the paired invalid-lane update. |
| Schema | CONFIRMED | `policy_decision.schema.json` defines required fields, enums, date-time format, fixture root, and additional-property behavior. |
| Contract | CONFIRMED | `contracts/policy/policy_decision.md` defines semantic meaning and distinguishes schema, policy, runtime, release, and fixture roles. |
| Test execution | NOT RUN | No validators, pytest, policy tests, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define valid-fixture guidance. |
| [`valid_1.json`](valid_1.json) | CONFIRMED | Current positive fixture includes required fields and allowed enum values. | Only one valid case is currently documented here. |
| [`../invalid/README.md`](../invalid/README.md) | CONFIRMED | Documents the negative fixture lane. | Does not prove tests were run. |
| [`../invalid/invalid_1.json`](../invalid/invalid_1.json) | CONFIRMED | Paired negative fixture omits required `decision_id`. | Only one invalid case is currently documented here. |
| [`../invalid/invalid_1.expected_error.txt`](../invalid/invalid_1.expected_error.txt) | CONFIRMED | Current expected-error matcher is `required`. | Broad matcher; may be tightened later. |
| [`../../../../../../schemas/contracts/v1/policy/policy_decision.schema.json`](../../../../../../schemas/contracts/v1/policy/policy_decision.schema.json) | CONFIRMED | Schema shape, required fields, enum values, date-time format, fixture root, validator path, and status. | Schema status is `PROPOSED`; validator implementation was not verified. |
| [`../../../../../../contracts/policy/policy_decision.md`](../../../../../../contracts/policy/policy_decision.md) | CONFIRMED | Semantic meaning, finite outcome boundary, and distinction from schema, executable policy, release, and runtime envelopes. | Does not prove policy runtime enforcement or CI status. |
| `../../../../../../tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN | Fixture discovery and valid fixture behavior. | Tests were not run during this update. |
| `../../../../../../docs/doctrine/directory-rules.md` | CONFIRMED | `fixtures/` is the root for golden, valid, and invalid test inputs; contracts/schemas/policy split remains separate. | Specific fixture completeness requires tests or inventory. |

[Back to top](#top)
