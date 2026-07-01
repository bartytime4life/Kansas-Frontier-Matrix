<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/runtime/decision-envelope/valid/readme
title: decision_envelope valid fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): runtime steward; TODO(owner): schema steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): policy steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-06-30 expansion
updated: 2026-06-30
policy_label: public-review
related:
  - valid_1.json
  - ../invalid/README.md
  - ../invalid/invalid_1.json
  - ../invalid/invalid_1.expected_error.txt
  - ../../../../../../schemas/contracts/v1/runtime/decision_envelope.schema.json
  - ../../../../../../contracts/runtime/decision_envelope.md
  - ../../../../../../contracts/runtime/decision_envelope/README.md
  - ../../../../../../contracts/runtime/DecisionEnvelope.md
  - ../../../../../../contracts/runtime/runtime_response_envelope.md
  - ../../../../../../contracts/runtime/ai_receipt.md
  - ../../../../../../contracts/policy/policy_decision.md
  - ../../../../../../policy/runtime/
  - ../../../../../../tools/validators/validate_decision_envelope.py
  - ../../../../../../tests/schemas/test_common_contracts.py
  - ../../../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, v1, runtime, decision-envelope, valid-fixtures, json-schema, finite-outcomes, policy-family, obligations, evidence-refs, trust-membrane, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/contracts/v1/runtime/decision_envelope/valid/README.md`."
  - "Valid fixtures are positive schema examples for the `decision_envelope` schema."
  - "Current valid fixture coverage is one minimal passing case: `valid_1.json`."
  - "No tests, validators, runtime policy checks, API/runtime behavior checks, receipt persistence checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `decision_envelope` valid fixtures

Positive fixture lane for the KFM `decision_envelope` runtime contract schema.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Family: runtime" src="https://img.shields.io/badge/family-runtime-blue">
  <img alt="Contract: decision_envelope" src="https://img.shields.io/badge/contract-decision__envelope-purple">
  <img alt="Lane: valid" src="https://img.shields.io/badge/lane-valid-success">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/contracts/v1/runtime/decision_envelope/valid/README.md`  
**Fixture posture:** valid JSON Schema fixture lane  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/runtime/decision_envelope.schema.json`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Schema basis](#schema-basis) · [Why this fixture passes](#why-this-fixture-passes) · [Authority boundary](#authority-boundary) · [Harness behavior](#harness-behavior) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are expected to pass schema validation. They are not executable runtime decisions, PolicyDecisions, PromotionDecisions, ReleaseManifests, RuntimeResponseEnvelopes, AIReceipts, evidence, public answers, or publication authority.

---

## Purpose

This directory stores positive JSON examples for the `decision_envelope` schema.

Use this lane to prove that a minimal well-shaped `DecisionEnvelope`-like object can pass schema validation before it is used by higher-level runtime, policy, API, map, AI, release, review, correction, or publication workflows. Passing this schema fixture only proves shape. It does not prove that policy evaluation was correct, evidence refs resolve, runtime/API behavior is implemented, release gates passed, or a public client may render the result.

---

## Current inventory

| File | Role | Expected result | Status |
|---|---|---|---|
| [`valid_1.json`](valid_1.json) | Minimal positive fixture for `decision_envelope`. | Schema validation should pass. | CONFIRMED |

Current valid fixture:

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

The paired negative fixture currently omits the required `decision_id` field and is expected to fail with a `required` error:

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

The current schema evidence for this fixture lane is:

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

## Why this fixture passes

`valid_1.json` includes every field currently required by the paired schema:

- `decision_id`
- `outcome`
- `policy_family`
- `reasons`
- `obligations`
- `evaluated_at`

It also uses schema-allowed values:

| Field | Fixture value | Schema posture |
|---|---|---|
| `decision_id` | `dec1` | Matches identifier pattern. |
| `outcome` | `ABSTAIN` | Allowed finite outcome. |
| `policy_family` | `capability` | Allowed policy family. |
| `evaluated_at` | `2026-05-09T00:00:00Z` | JSON Schema `date-time` string. |

This positive fixture is intentionally minimal. It proves the schema accepts a compact DecisionEnvelope object, not that the decision is executable, policy-approved, release-approved, evidence-backed, or safe for public rendering.

> [!WARNING]
> A `DecisionEnvelope` is not a public answer by itself and not publication approval. It records bounded runtime decision posture for downstream governed handling.

---

## Authority boundary

| Responsibility | Home | Status in this check |
|---|---|---|
| Positive fixture examples | `fixtures/contracts/v1/runtime/decision_envelope/valid/` | CONFIRMED |
| Negative fixture examples | `fixtures/contracts/v1/runtime/decision_envelope/invalid/` | CONFIRMED |
| Machine-checkable shape | `schemas/contracts/v1/runtime/decision_envelope.schema.json` | CONFIRMED |
| Semantic contract | `contracts/runtime/decision_envelope.md` | CONFIRMED |
| Runtime policy | `policy/runtime/` | OUT OF SCOPE FOR THIS README |
| Validator implementation | `tools/validators/validate_decision_envelope.py` | NEEDS VERIFICATION |
| Schema test harness | `tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN |

Do not collapse this fixture lane into the semantic contract, schema, executable policy, runtime API behavior, runtime response envelope, policy decision, promotion decision, release manifest, AI receipt, evidence bundle, review record, or receipt/proof persistence layer.

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

This README documents expected fixture behavior only. It does not claim that pytest, CI, runtime policy, API behavior, receipt persistence, or the dedicated DecisionEnvelope validator were run during this update.

---

## Maintenance checklist

Before changing this valid fixture lane:

- [ ] Keep passing examples under `valid/valid_<n>.json`.
- [ ] Keep at least one minimal positive fixture unless the schema family is intentionally retired.
- [ ] Keep positive fixtures paired with negative fixtures under `../invalid/`.
- [ ] Add richer valid fixtures only when they remain public-safe and reviewable.
- [ ] Avoid sensitive, private, unpublished, source-system, prompt, credential, or policy-restricted content.
- [ ] Never place chain-of-thought, private model internals, raw prompts, secrets, sensitive evidence payloads, exact protected coordinates, living-person private identifiers, unpublished source excerpts, or policy-restricted material in fixture content.
- [ ] Update this README when schema fields, enum values, optional compatibility fields, or fixture coverage changes.
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
| Schema | CONFIRMED | `decision_envelope.schema.json` defines required fields, finite enums, date-time field, optional compatibility fields, fixture root, and additional-property behavior. |
| Contract | CONFIRMED | `contracts/runtime/decision_envelope.md` defines semantic meaning and distinguishes DecisionEnvelope from executable runtime behavior, PolicyDecision, PromotionDecision, ReleaseManifest, RuntimeResponseEnvelope, AIReceipt, and public truth. |
| Test execution | NOT RUN | No validators, pytest, runtime policy tests, API behavior checks, receipt persistence checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define valid-fixture guidance. |
| [`valid_1.json`](valid_1.json) | CONFIRMED | Current positive fixture includes required fields, allowed finite `outcome`, allowed `policy_family`, and valid date-time value. | Only one valid case is currently documented here. |
| [`../invalid/README.md`](../invalid/README.md) | CONFIRMED | Documents the negative fixture lane. | Does not prove tests were run. |
| [`../invalid/invalid_1.json`](../invalid/invalid_1.json) | CONFIRMED | Paired negative fixture omits required `decision_id`. | Only one invalid case is currently documented here. |
| [`../invalid/invalid_1.expected_error.txt`](../invalid/invalid_1.expected_error.txt) | CONFIRMED | Current expected-error matcher is `required`. | Broad matcher; may be tightened later. |
| [`../../../../../../schemas/contracts/v1/runtime/decision_envelope.schema.json`](../../../../../../schemas/contracts/v1/runtime/decision_envelope.schema.json) | CONFIRMED | Schema shape, required fields, enum values, optional compatibility fields, fixture root, validator path, and status. | Schema status is `PROPOSED`; validator implementation was not verified. |
| [`../../../../../../contracts/runtime/decision_envelope.md`](../../../../../../contracts/runtime/decision_envelope.md) | CONFIRMED | Semantic meaning, runtime decision boundary, field surface, and distinction from policy, release, runtime envelope, AI, evidence, and publication authority. | Does not prove runtime/API implementation, policy evaluation, receipt persistence, validator wiring, or CI status. |
| `../../../../../../tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN | Fixture discovery and valid fixture behavior. | Tests were not run during this update. |
| `../../../../../../docs/doctrine/directory-rules.md` | CONFIRMED | `fixtures/` is the root for golden, valid, and invalid test inputs; contracts/schemas/policy split remains separate. | Specific fixture completeness requires tests or inventory. |

[Back to top](#top)
