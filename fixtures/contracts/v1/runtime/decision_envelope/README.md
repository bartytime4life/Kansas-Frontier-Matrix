<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/runtime/decision-envelope/readme
title: decision_envelope fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): runtime steward; TODO(owner): schema steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): policy steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-06-30 expansion
updated: 2026-06-30
policy_label: public-review
related:
  - valid/README.md
  - valid/valid_1.json
  - invalid/README.md
  - invalid/invalid_1.json
  - invalid/invalid_1.expected_error.txt
  - ../../../../../schemas/contracts/v1/runtime/decision_envelope.schema.json
  - ../../../../../contracts/runtime/decision_envelope.md
  - ../../../../../contracts/runtime/decision_envelope/README.md
  - ../../../../../contracts/runtime/DecisionEnvelope.md
  - ../../../../../contracts/runtime/runtime_response_envelope.md
  - ../../../../../contracts/runtime/ai_receipt.md
  - ../../../../../contracts/policy/policy_decision.md
  - ../../../../../policy/runtime/
  - ../../../../../tools/validators/validate_decision_envelope.py
  - ../../../../../tests/schemas/test_common_contracts.py
  - ../../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, v1, runtime, decision-envelope, valid-fixtures, invalid-fixtures, expected-error, json-schema, finite-outcomes, policy-family, obligations, evidence-refs, trust-membrane, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/contracts/v1/runtime/decision_envelope/README.md`."
  - "This directory is the schema-declared fixture root for `decision_envelope`."
  - "Fixtures are sample test inputs only; semantic meaning, machine schema shape, executable runtime policy, API behavior, and release authority stay in their owning roots."
  - "Current fixture coverage includes one valid case and one invalid missing-required-field case."
  - "No tests, validators, runtime policy checks, API/runtime behavior checks, receipt persistence checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `decision_envelope` fixtures

Fixture family for the KFM `decision_envelope` runtime contract schema.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Family: runtime" src="https://img.shields.io/badge/family-runtime-blue">
  <img alt="Contract: decision_envelope" src="https://img.shields.io/badge/contract-decision__envelope-purple">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
  <img alt="Outcomes: finite" src="https://img.shields.io/badge/outcomes-ANSWER%20%7C%20ABSTAIN%20%7C%20DENY%20%7C%20ERROR-informational">
</p>

**Path:** `fixtures/contracts/v1/runtime/decision_envelope/README.md`  
**Fixture posture:** JSON Schema valid/invalid fixture family  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/runtime/decision_envelope.schema.json`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Schema basis](#schema-basis) · [Authority boundary](#authority-boundary) · [Harness behavior](#harness-behavior) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are schema fixtures. They are not executable runtime decisions, PolicyDecisions, PromotionDecisions, ReleaseManifests, RuntimeResponseEnvelopes, AIReceipts, evidence, public answers, release approval, review approval, or publication authority.

---

## Purpose

This directory groups positive and negative JSON fixtures for the `decision_envelope` schema.

Use this fixture family to verify that KFM accepts a minimal well-shaped `DecisionEnvelope`-like object and rejects an incomplete one. The schema-declared fixture root is:

```text
fixtures/contracts/v1/runtime/decision_envelope/
```

A passing fixture proves schema shape only. It does not prove that runtime policy executed, that policy evaluation was correct, that evidence refs resolve, that API/runtime behavior is implemented, that release gates passed, or that a public API, map, AI, or UI surface may render the result.

---

## Current inventory

| Lane | File | Current role | Status |
|---|---|---|---|
| [`valid/`](valid/README.md) | [`valid_1.json`](valid/valid_1.json) | Minimal positive fixture with every required top-level field and allowed enum values. | CONFIRMED |
| [`invalid/`](invalid/README.md) | [`invalid_1.json`](invalid/invalid_1.json) | Minimal negative fixture matching the positive case but missing required `decision_id`. | CONFIRMED |
| [`invalid/`](invalid/README.md) | [`invalid_1.expected_error.txt`](invalid/invalid_1.expected_error.txt) | Current expected-error matcher: `required`. | CONFIRMED / BROAD MATCHER |

Current positive fixture shape:

```json
{
  "decision_id": "dec1",
  "outcome": "ABSTAIN",
  "policy_family": "capability",
  "reasons": ["not ready"],
  "obligations": [],
  "evaluated_at": "2026-05-09T00:00:00Z"
}
```

Current negative fixture shape:

```json
{
  "outcome": "ABSTAIN",
  "policy_family": "capability",
  "reasons": ["not ready"],
  "obligations": [],
  "evaluated_at": "2026-05-09T00:00:00Z"
}
```

---

## Schema basis

The current schema evidence for this fixture family is:

```text
schemas/contracts/v1/runtime/decision_envelope.schema.json
```

Confirmed schema facts:

| Item | Value |
|---|---|
| Schema title | `decision_envelope` |
| Root type | object |
| Required fields | `decision_id`, `outcome`, `policy_family`, `reasons`, `obligations`, `evaluated_at` |
| `decision_id` | string matching `^[a-z][a-z0-9_:.-]*$` |
| `outcome` enum values | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` |
| `policy_family` enum values | `promotion`, `access`, `render`, `capability`, `consent`, `sensitivity` |
| `reasons` | array of strings |
| `obligations` | array of strings |
| `evaluated_at` | string with `date-time` format |
| Optional compatibility fields | `id`, `decision`, `reason_code`, `evidence_refs`, `spec_hash`, `version`, `issued_at` |
| Additional properties | false |
| Declared contract doc | `contracts/runtime/decision_envelope.md` |
| Declared fixture root | `fixtures/contracts/v1/runtime/decision_envelope/` |
| Declared validator | `tools/validators/validate_decision_envelope.py` |
| Declared policy path | `policy/runtime/` |
| Schema status | `PROPOSED` |

---

## Authority boundary

| Responsibility | Home | Status in this check |
|---|---|---|
| Fixture examples | `fixtures/contracts/v1/runtime/decision_envelope/` | CONFIRMED |
| Valid examples | `fixtures/contracts/v1/runtime/decision_envelope/valid/` | CONFIRMED |
| Invalid examples | `fixtures/contracts/v1/runtime/decision_envelope/invalid/` | CONFIRMED |
| Machine-checkable shape | `schemas/contracts/v1/runtime/decision_envelope.schema.json` | CONFIRMED |
| Semantic contract | `contracts/runtime/decision_envelope.md` | CONFIRMED |
| Runtime policy | `policy/runtime/` | OUT OF SCOPE FOR THIS README |
| Validator implementation | `tools/validators/validate_decision_envelope.py` | NEEDS VERIFICATION |
| Schema test harness | `tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN |

`DecisionEnvelope` must remain distinguishable from:

| Do not collapse `DecisionEnvelope` into | Why |
|---|---|
| Executable runtime behavior | The envelope records decision posture; runtime/API code performs behavior elsewhere. |
| `PolicyDecision` | Policy decisions are policy-evaluation outputs; this envelope is runtime-facing decision posture. |
| `PromotionDecision` | Promotion decisions govern lifecycle movement; this envelope does not promote anything. |
| `ReleaseManifest` | Release manifests bind released contents; a decision envelope alone cannot publish content. |
| `RuntimeResponseEnvelope` | Runtime response envelopes carry client-facing response payload context; this object records a finite decision. |
| `AIReceipt` | AI receipts record AI-mediated accountability; DecisionEnvelope records runtime decision posture. |
| `EvidenceBundle` | Evidence supports claims; decision envelopes may reference evidence but do not prove it true. |
| Public answer or map rendering permission | Public surfaces still require governed API/runtime, policy, evidence, release, and sensitivity checks. |

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

For this runtime family, that means:

```text
fixtures/contracts/v1/runtime/decision_envelope/
```

Observed expectations:

| Fixture pattern | Expected result |
|---|---|
| `valid/valid_*.json` | no JSON Schema errors |
| `invalid/invalid_*.json` | at least one JSON Schema error |
| `invalid/invalid_*.expected_error.txt` | expected text appears in combined error messages |

This README documents expected fixture behavior only. It does not claim that pytest, CI, runtime policy, API behavior, receipt persistence, or the dedicated DecisionEnvelope validator was run during this update.

---

## Maintenance checklist

Before changing this fixture family:

- [ ] Keep passing examples under `valid/valid_<n>.json`.
- [ ] Keep failing examples under `invalid/invalid_<n>.json`.
- [ ] Keep expected-error text beside the invalid fixture it describes.
- [ ] Keep fixture cases small, deterministic, public-safe, and reviewable.
- [ ] Keep at least one valid minimal fixture and one missing-required-field invalid fixture.
- [ ] Add identifier-pattern, enum, date-time, additional-property, and optional-field consistency fixtures as coverage expands.
- [ ] Avoid sensitive, private, unpublished, source-system, prompt-like, or policy-restricted content.
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
| Schema | CONFIRMED | `decision_envelope.schema.json` defines required fields, finite enums, date-time field, optional compatibility fields, fixture root, and additional-property behavior. |
| Contract | CONFIRMED | `contracts/runtime/decision_envelope.md` defines semantic meaning and separates DecisionEnvelope from executable runtime behavior, PolicyDecision, PromotionDecision, ReleaseManifest, RuntimeResponseEnvelope, AIReceipt, and public truth. |
| Validator file | NEEDS VERIFICATION | `tools/validators/validate_decision_envelope.py` is declared by schema but implementation/wiring was not verified during this update. |
| Test execution | NOT RUN | No validators, pytest, runtime policy tests, API behavior checks, receipt persistence checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define fixture-family guidance. |
| [`valid/README.md`](valid/README.md) | CONFIRMED | Positive fixture lane guidance. | Does not prove tests were run. |
| [`valid/valid_1.json`](valid/valid_1.json) | CONFIRMED | Current positive fixture includes required fields, allowed finite `outcome`, allowed `policy_family`, and valid date-time value. | Only one valid fixture is currently documented. |
| [`invalid/README.md`](invalid/README.md) | CONFIRMED | Negative fixture lane guidance. | Does not prove tests were run. |
| [`invalid/invalid_1.json`](invalid/invalid_1.json) | CONFIRMED | Current negative fixture omits required `decision_id`. | Only one invalid fixture is currently documented. |
| [`invalid/invalid_1.expected_error.txt`](invalid/invalid_1.expected_error.txt) | CONFIRMED | Current expected-error matcher is `required`. | Broad matcher; may be tightened later. |
| [`../../../../../schemas/contracts/v1/runtime/decision_envelope.schema.json`](../../../../../schemas/contracts/v1/runtime/decision_envelope.schema.json) | CONFIRMED | Schema shape, required fields, enum values, optional compatibility fields, fixture root, validator path, and status. | Schema status is `PROPOSED`; validator implementation was not verified. |
| [`../../../../../contracts/runtime/decision_envelope.md`](../../../../../contracts/runtime/decision_envelope.md) | CONFIRMED | Semantic meaning, runtime decision boundary, field surface, and distinction from policy, release, runtime envelope, AI, evidence, and publication authority. | Does not prove runtime/API implementation, policy evaluation, receipt persistence, validator wiring, or CI status. |
| `../../../../../tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN | Fixture discovery and valid/invalid fixture behavior. | Tests were not run during this update. |
| `../../../../../docs/doctrine/directory-rules.md` | CONFIRMED | `fixtures/` is the root for golden, valid, and invalid test inputs; contracts/schemas/policy split remains separate. | Specific fixture completeness requires tests or inventory. |

[Back to top](#top)
