<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/policy/policy-decision/invalid/readme
title: policy_decision invalid fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): policy steward; TODO(owner): schema steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-06-30 expansion
updated: 2026-06-30
policy_label: public-review
related:
  - ../valid/valid_1.json
  - invalid_1.json
  - invalid_1.expected_error.txt
  - ../../../../../../schemas/contracts/v1/policy/policy_decision.schema.json
  - ../../../../../../contracts/policy/policy_decision.md
  - ../../../../../../contracts/policy/policy_decision/README.md
  - ../../../../../../policy/
  - ../../../../../../tools/validators/validate_policy_decision.py
  - ../../../../../../tests/schemas/test_common_contracts.py
  - ../../../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, v1, policy, policy-decision, invalid-fixtures, expected-error, json-schema, finite-outcomes, fail-closed, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/contracts/v1/policy/policy_decision/invalid/README.md`."
  - "Invalid fixtures are intentionally failing examples for the `policy_decision` schema."
  - "Current invalid fixture coverage is one missing-required-field case: `invalid_1.json` omits `decision_id`; expected error matcher is `required`."
  - "No tests, validators, policy bundles, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `policy_decision` invalid fixtures

Negative fixture lane for the KFM `policy_decision` contract schema.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Family: policy" src="https://img.shields.io/badge/family-policy-blue">
  <img alt="Contract: policy_decision" src="https://img.shields.io/badge/contract-policy__decision-purple">
  <img alt="Lane: invalid" src="https://img.shields.io/badge/lane-invalid-critical">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/contracts/v1/policy/policy_decision/invalid/README.md`  
**Fixture posture:** invalid JSON Schema fixture lane  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/policy/policy_decision.schema.json`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Schema basis](#schema-basis) · [Why this fixture fails](#why-this-fixture-fails) · [Authority boundary](#authority-boundary) · [Harness behavior](#harness-behavior) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are expected to fail schema validation. They are not policy decisions, policy approvals, release approvals, review records, evidence, receipts, proofs, runtime envelopes, or executable policy.

---

## Purpose

This directory stores negative JSON examples for the `policy_decision` schema.

Use this lane to prove that malformed or incomplete `PolicyDecision`-like objects are rejected before they can be treated as governed policy output. Invalid fixtures help preserve fail-closed behavior for policy-sensitive surfaces such as governed API responses, map rendering, Focus Mode answers, promotion gates, release gates, correction workflows, and redaction decisions.

---

## Current inventory

| File | Role | Expected result | Status |
|---|---|---|---|
| [`invalid_1.json`](invalid_1.json) | Negative fixture missing required `decision_id`. | Schema validation should fail. | CONFIRMED |
| [`invalid_1.expected_error.txt`](invalid_1.expected_error.txt) | Expected-error matcher for `invalid_1.json`. | Combined schema errors should include `required`. | CONFIRMED / BROAD MATCHER |

Current invalid fixture:

```json
{
  "outcome": "ABSTAIN",
  "policy_family": "access",
  "reasons": ["none"],
  "obligations": [],
  "evaluated_at": "2026-05-09T00:00:00Z"
}
```

The paired positive fixture currently includes the missing `decision_id` field:

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

## Why this fixture fails

`invalid_1.json` omits `decision_id`, which is required by the paired schema.

That failure matters because a `PolicyDecision` without a stable decision identifier is harder to cite in receipts, logs, validation reports, release gates, correction records, and rollback reviews. The semantic contract treats `PolicyDecision` as a finite, auditable policy evaluation record; an uncitable or unstable decision object should not silently pass as governed output.

Expected-error matcher:

```text
required
```

This matcher is intentionally broad. It confirms the missing-field class of failure, but it does not pin the full validator wording. A later fixture pass may tighten it to the exact missing property name once validator output is stable enough.

---

## Authority boundary

| Responsibility | Home | Status in this check |
|---|---|---|
| Negative fixture examples | `fixtures/contracts/v1/policy/policy_decision/invalid/` | CONFIRMED |
| Positive fixture examples | `fixtures/contracts/v1/policy/policy_decision/valid/` | CONFIRMED file present / README not found during this update |
| Machine-checkable shape | `schemas/contracts/v1/policy/policy_decision.schema.json` | CONFIRMED |
| Semantic contract | `contracts/policy/policy_decision.md` | CONFIRMED |
| Executable policy rules | `policy/` | OUT OF SCOPE FOR THIS README |
| Validator implementation | `tools/validators/validate_policy_decision.py` | NEEDS VERIFICATION |
| Schema test harness | `tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN |

Do not collapse this fixture lane into the semantic contract, schema, policy bundle, release gate, or runtime decision envelope.

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

This README documents expected fixture behavior only. It does not claim that pytest, CI, policy bundles, or dedicated policy-decision validators were run during this update.

---

## Maintenance checklist

Before changing this invalid fixture lane:

- [ ] Keep failing examples under `invalid/invalid_<n>.json`.
- [ ] Keep expected-error text beside the invalid fixture it describes.
- [ ] Keep at least one missing-required-field fixture unless another fixture family covers that failure class.
- [ ] Add enum, pattern, date-time, and additional-property failures when policy-decision coverage expands.
- [ ] Avoid sensitive, private, unpublished, or policy-restricted content.
- [ ] Update this README when schema fields, enum values, or expected-error behavior changes.
- [ ] Run the schema fixture test before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Invalid fixture | CONFIRMED | `invalid_1.json` exists and omits required `decision_id`. |
| Expected-error file | CONFIRMED | `invalid_1.expected_error.txt` exists and contains `required`. |
| Positive fixture | CONFIRMED | `valid/valid_1.json` exists and includes `decision_id`. |
| Parent fixture README | NOT FOUND | `fixtures/contracts/v1/policy/policy_decision/README.md` was not found during this update. |
| Valid-lane README | NOT FOUND | `fixtures/contracts/v1/policy/policy_decision/valid/README.md` was not found during this update. |
| Schema | CONFIRMED | `policy_decision.schema.json` defines required fields, enums, date-time format, fixture root, and additional-property behavior. |
| Contract | CONFIRMED | `contracts/policy/policy_decision.md` defines semantic meaning and distinguishes schema, policy, runtime, release, and fixture roles. |
| Test execution | NOT RUN | No validators, pytest, policy tests, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define invalid-fixture guidance. |
| [`invalid_1.json`](invalid_1.json) | CONFIRMED | Current negative fixture omits required `decision_id`. | Only one invalid case is currently documented here. |
| [`invalid_1.expected_error.txt`](invalid_1.expected_error.txt) | CONFIRMED | Current expected-error matcher is `required`. | Broad matcher; may be tightened later. |
| [`../valid/valid_1.json`](../valid/valid_1.json) | CONFIRMED | Paired positive fixture includes `decision_id` and other required fields. | Positive lane README was not found during this update. |
| [`../../../../../../schemas/contracts/v1/policy/policy_decision.schema.json`](../../../../../../schemas/contracts/v1/policy/policy_decision.schema.json) | CONFIRMED | Schema shape, required fields, enum values, date-time format, fixture root, validator path, and status. | Schema status is `PROPOSED`; validator implementation was not verified. |
| [`../../../../../../contracts/policy/policy_decision.md`](../../../../../../contracts/policy/policy_decision.md) | CONFIRMED | Semantic meaning, finite outcome boundary, and distinction from schema, executable policy, release, and runtime envelopes. | Does not prove policy runtime enforcement or CI status. |
| `../../../../../../tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN | Fixture discovery and valid/invalid fixture behavior. | Tests were not run during this update. |
| `../../../../../../docs/doctrine/directory-rules.md` | CONFIRMED | `fixtures/` is the root for golden, valid, and invalid test inputs; contracts/schemas/policy split remains separate. | Specific fixture completeness requires tests or inventory. |

[Back to top](#top)
