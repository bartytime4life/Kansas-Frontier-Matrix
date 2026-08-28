<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/runtime/decision-envelope/invalid/readme
title: decision_envelope invalid fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): runtime steward; TODO(owner): schema steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): policy steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-06-30 expansion
updated: 2026-06-30
policy_label: public-review
related:
  - ../valid/valid_1.json
  - invalid_1.json
  - invalid_1.expected_error.txt
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
tags: [kfm, fixtures, contracts, v1, runtime, decision-envelope, invalid-fixtures, expected-error, json-schema, finite-outcomes, policy-family, obligations, evidence-refs, trust-membrane, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/contracts/v1/runtime/decision_envelope/invalid/README.md`."
  - "Invalid fixtures are intentionally failing examples for the `decision_envelope` schema."
  - "Current invalid fixture coverage is one missing-required-field case: `invalid_1.json` omits `decision_id`; expected error matcher is `required`."
  - "No tests, validators, runtime policy checks, API/runtime behavior checks, receipt persistence checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `decision_envelope` invalid fixtures

Negative fixture lane for the KFM `decision_envelope` runtime contract schema.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Family: runtime" src="https://img.shields.io/badge/family-runtime-blue">
  <img alt="Contract: decision_envelope" src="https://img.shields.io/badge/contract-decision__envelope-purple">
  <img alt="Lane: invalid" src="https://img.shields.io/badge/lane-invalid-critical">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/contracts/v1/runtime/decision_envelope/invalid/README.md`  
**Fixture posture:** invalid JSON Schema fixture lane  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/runtime/decision_envelope.schema.json`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Schema basis](#schema-basis) · [Why this fixture fails](#why-this-fixture-fails) · [Authority boundary](#authority-boundary) · [Harness behavior](#harness-behavior) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are expected to fail schema validation. They are not DecisionEnvelopes, executable runtime decisions, PolicyDecisions, PromotionDecisions, ReleaseManifests, RuntimeResponseEnvelopes, AIReceipts, evidence, public answers, or publication authority.

---

## Purpose

This directory stores negative JSON examples for the `decision_envelope` schema.

Use this lane to prove that malformed or incomplete `DecisionEnvelope`-like objects are rejected before they can be treated as governed runtime decision envelopes. Invalid fixtures help preserve the runtime trust membrane: public clients should consume bounded, finite, policy-aware envelopes, not ambiguous or incomplete decision-shaped payloads.

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
  "policy_family": "capability",
  "reasons": ["not ready"],
  "obligations": [],
  "evaluated_at": "2026-05-09T00:00:00Z"
}
```

The paired positive fixture currently includes the missing `decision_id` field:

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

## Why this fixture fails

`invalid_1.json` omits `decision_id`, which is required by the paired schema.

That failure matters because `decision_id` is the stable runtime decision identifier. Without it, downstream runtime/API/UI/map/AI surfaces cannot reliably cite, audit, supersede, review, or roll back the decision envelope. A runtime payload with outcome, family, reasons, obligations, and timestamp but no stable decision identifier must not silently pass as a governed `DecisionEnvelope`.

Expected-error matcher:

```text
required
```

This matcher is intentionally broad. It confirms the missing-field class of failure, but it does not pin the full validator wording. A later fixture pass may tighten it to the exact missing property name once validator output is stable enough.

> [!WARNING]
> A `DecisionEnvelope` is not executable policy, not a public answer by itself, and not publication approval. It records bounded runtime decision posture for downstream governed handling.

---

## Authority boundary

| Responsibility | Home | Status in this check |
|---|---|---|
| Negative fixture examples | `fixtures/contracts/v1/runtime/decision_envelope/invalid/` | CONFIRMED |
| Positive fixture examples | `fixtures/contracts/v1/runtime/decision_envelope/valid/` | CONFIRMED file present / README not checked in this update |
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

This README documents expected fixture behavior only. It does not claim that pytest, CI, runtime policy, API behavior, receipt persistence, or the dedicated DecisionEnvelope validator were run during this update.

---

## Maintenance checklist

Before changing this invalid fixture lane:

- [ ] Keep failing examples under `invalid/invalid_<n>.json`.
- [ ] Keep expected-error text beside the invalid fixture it describes.
- [ ] Keep at least one missing-required-field fixture unless another fixture family covers that failure class.
- [ ] Add identifier-pattern, enum, date-time, additional-property, and optional-field consistency failures when DecisionEnvelope coverage expands.
- [ ] Avoid sensitive, private, unpublished, source-system, prompt, credential, or policy-restricted content.
- [ ] Never place chain-of-thought, private model internals, raw prompts, secrets, sensitive evidence payloads, exact protected coordinates, living-person private identifiers, unpublished source excerpts, or policy-restricted material in fixture content.
- [ ] Update this README when schema fields, enum values, optional compatibility fields, or expected-error behavior changes.
- [ ] Run the schema fixture test before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Invalid fixture | CONFIRMED | `invalid_1.json` exists and omits required `decision_id`. |
| Expected-error file | CONFIRMED | `invalid_1.expected_error.txt` exists and contains `required`. |
| Positive fixture | CONFIRMED | `valid/valid_1.json` exists and includes `decision_id`. |
| Schema | CONFIRMED | `decision_envelope.schema.json` defines required fields, finite enums, date-time field, optional compatibility fields, fixture root, and additional-property behavior. |
| Contract | CONFIRMED | `contracts/runtime/decision_envelope.md` defines semantic meaning and distinguishes DecisionEnvelope from executable runtime behavior, PolicyDecision, PromotionDecision, ReleaseManifest, RuntimeResponseEnvelope, AIReceipt, and public truth. |
| Test execution | NOT RUN | No validators, pytest, runtime policy tests, API behavior checks, receipt persistence checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define invalid-fixture guidance. |
| [`invalid_1.json`](invalid_1.json) | CONFIRMED | Current negative fixture omits required `decision_id`. | Only one invalid case is currently documented here. |
| [`invalid_1.expected_error.txt`](invalid_1.expected_error.txt) | CONFIRMED | Current expected-error matcher is `required`. | Broad matcher; may be tightened later. |
| [`../valid/valid_1.json`](../valid/valid_1.json) | CONFIRMED | Paired positive fixture includes `decision_id` and other required fields. | Positive lane README was not checked during this update. |
| [`../../../../../../schemas/contracts/v1/runtime/decision_envelope.schema.json`](../../../../../../schemas/contracts/v1/runtime/decision_envelope.schema.json) | CONFIRMED | Schema shape, required fields, enum values, optional compatibility fields, fixture root, validator path, and status. | Schema status is `PROPOSED`; validator implementation was not verified. |
| [`../../../../../../contracts/runtime/decision_envelope.md`](../../../../../../contracts/runtime/decision_envelope.md) | CONFIRMED | Semantic meaning, runtime decision boundary, field surface, and distinction from policy, release, runtime envelope, AI, evidence, and publication authority. | Does not prove runtime/API implementation, policy evaluation, receipt persistence, validator wiring, or CI status. |
| `../../../../../../tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN | Fixture discovery and invalid fixture behavior. | Tests were not run during this update. |
| `../../../../../../docs/doctrine/directory-rules.md` | CONFIRMED | `fixtures/` is the root for golden, valid, and invalid test inputs; contracts/schemas/policy split remains separate. | Specific fixture completeness requires tests or inventory. |

[Back to top](#top)
