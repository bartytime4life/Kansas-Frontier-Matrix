<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/runtime/ai-receipt/invalid/readme
title: ai_receipt invalid fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): runtime steward; TODO(owner): governed AI steward; TODO(owner): schema steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-06-30 expansion
updated: 2026-06-30
policy_label: public-review
related:
  - ../valid/valid_1.json
  - invalid_1.json
  - invalid_1.expected_error.txt
  - ../../../../../../schemas/contracts/v1/runtime/ai_receipt.schema.json
  - ../../../../../../contracts/runtime/ai_receipt.md
  - ../../../../../../contracts/runtime/README.md
  - ../../../../../../contracts/policy/policy_decision.md
  - ../../../../../../policy/runtime/
  - ../../../../../../policy/ai/
  - ../../../../../../tools/validators/validate_ai_receipt.py
  - ../../../../../../tests/schemas/test_common_contracts.py
  - ../../../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, v1, runtime, ai-receipt, invalid-fixtures, expected-error, json-schema, governed-ai, receipt, finite-outcomes, cite-or-abstain, no-chain-of-thought, no-model-truth, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/contracts/v1/runtime/ai_receipt/invalid/README.md`."
  - "Invalid fixtures are intentionally failing examples for the `ai_receipt` schema."
  - "Current invalid fixture coverage is one missing-required-field case: `invalid_1.json` omits `id`; expected error matcher is `required`."
  - "No tests, validators, policy bundles, runtime adapters, citation validators, receipt persistence checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `ai_receipt` invalid fixtures

Negative fixture lane for the KFM `ai_receipt` runtime contract schema.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Family: runtime" src="https://img.shields.io/badge/family-runtime-blue">
  <img alt="Contract: ai_receipt" src="https://img.shields.io/badge/contract-ai__receipt-purple">
  <img alt="Lane: invalid" src="https://img.shields.io/badge/lane-invalid-critical">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/contracts/v1/runtime/ai_receipt/invalid/README.md`  
**Fixture posture:** invalid JSON Schema fixture lane  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/runtime/ai_receipt.schema.json`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Schema basis](#schema-basis) · [Why this fixture fails](#why-this-fixture-fails) · [Authority boundary](#authority-boundary) · [Harness behavior](#harness-behavior) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are expected to fail schema validation. They are not AI receipts, evidence, model truth, chain-of-thought storage, policy decisions, citation validation results, public-release approval, runtime envelopes, receipts of persistence, or executable runtime policy.

---

## Purpose

This directory stores negative JSON examples for the `ai_receipt` schema.

Use this lane to prove that malformed or incomplete `AIReceipt`-like objects are rejected before they can be treated as accountable AI runtime receipts. Invalid fixtures help preserve KFM's governed-AI boundary: AI output is interpretive and downstream of evidence, policy, citation validation, finite runtime outcomes, receipts, and governed API/runtime envelopes.

---

## Current inventory

| File | Role | Expected result | Status |
|---|---|---|---|
| [`invalid_1.json`](invalid_1.json) | Negative fixture missing required `id`. | Schema validation should fail. | CONFIRMED |
| [`invalid_1.expected_error.txt`](invalid_1.expected_error.txt) | Expected-error matcher for `invalid_1.json`. | Combined schema errors should include `required`. | CONFIRMED / BROAD MATCHER |

Current invalid fixture:

```json
{
  "run_id": "run1",
  "adapter": "mock",
  "model_ref": "none",
  "inputs_digest": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "outputs_digest": "sha256:bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
  "policy_decision_ref": "dec1",
  "citation_validation_ref": "val1",
  "outcome": "ABSTAIN"
}
```

The paired positive fixture currently includes the missing `id` field:

```json
{
  "id": "ai1",
  "run_id": "run1",
  "adapter": "mock",
  "model_ref": "none",
  "inputs_digest": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "outputs_digest": "sha256:bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
  "policy_decision_ref": "dec1",
  "citation_validation_ref": "val1",
  "outcome": "ABSTAIN"
}
```

---

## Schema basis

The current schema evidence for this fixture lane is:

```text
schemas/contracts/v1/runtime/ai_receipt.schema.json
```

Confirmed schema facts:

| Item | Value |
|---|---|
| Schema title | `ai_receipt` |
| Root type | object |
| Required fields | `id`, `run_id`, `adapter`, `model_ref`, `inputs_digest`, `outputs_digest`, `policy_decision_ref`, `citation_validation_ref`, `outcome` |
| `id` | string matching `^[a-z][a-z0-9_:.-]*$` |
| `inputs_digest` | string matching `^sha256:[a-f0-9]{64}$` |
| `outputs_digest` | string matching `^sha256:[a-f0-9]{64}$` |
| `outcome` enum values | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` |
| Additional properties | false |
| Declared contract doc | `contracts/runtime/ai_receipt.md` |
| Declared fixture root | `fixtures/contracts/v1/runtime/ai_receipt/` |
| Declared validator | `tools/validators/validate_ai_receipt.py` |
| Declared policy path | `policy/runtime/` |
| Schema status | `PROPOSED` |

---

## Why this fixture fails

`invalid_1.json` omits `id`, which is required by the paired schema.

That failure matters because `id` is the stable receipt identifier for an AI-mediated runtime event. Without a stable receipt ID, downstream audit, replay checks, incident review, correction, rollback, citation validation linkage, and receipt lookup become ambiguous. A runtime AI record without `id` must not silently pass as a governed `AIReceipt`.

Expected-error matcher:

```text
required
```

This matcher is intentionally broad. It confirms the missing-field class of failure, but it does not pin the full validator wording. A later fixture pass may tighten it to the exact missing property name once validator output is stable enough.

> [!WARNING]
> An `AIReceipt` is not proof that generated language is true, publishable, policy-approved, evidence-backed, or safe to render. It is an accountability receipt for a bounded AI-mediated runtime event.

---

## Authority boundary

| Responsibility | Home | Status in this check |
|---|---|---|
| Negative fixture examples | `fixtures/contracts/v1/runtime/ai_receipt/invalid/` | CONFIRMED |
| Positive fixture examples | `fixtures/contracts/v1/runtime/ai_receipt/valid/` | CONFIRMED file present / README not checked in this update |
| Machine-checkable shape | `schemas/contracts/v1/runtime/ai_receipt.schema.json` | CONFIRMED |
| Semantic contract | `contracts/runtime/ai_receipt.md` | CONFIRMED |
| Runtime / AI policy | `policy/runtime/`, `policy/ai/` | OUT OF SCOPE FOR THIS README |
| Validator implementation | `tools/validators/validate_ai_receipt.py` | NEEDS VERIFICATION |
| Schema test harness | `tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN |

Do not collapse this fixture lane into the semantic contract, schema, executable policy, runtime adapter, citation validator, runtime response envelope, decision envelope, evidence bundle, policy decision, review record, or receipt/proof persistence layer.

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

This README documents expected fixture behavior only. It does not claim that pytest, CI, runtime adapters, policy bundles, citation validators, receipt persistence, or the dedicated AIReceipt validator were run during this update.

---

## Maintenance checklist

Before changing this invalid fixture lane:

- [ ] Keep failing examples under `invalid/invalid_<n>.json`.
- [ ] Keep expected-error text beside the invalid fixture it describes.
- [ ] Keep at least one missing-required-field fixture unless another fixture family covers that failure class.
- [ ] Add digest-pattern, enum, identifier-pattern, and additional-property failures when AIReceipt coverage expands.
- [ ] Avoid sensitive, private, unpublished, source-system, prompt, credential, or policy-restricted content.
- [ ] Never place chain-of-thought, private model internals, raw prompts, secrets, sensitive evidence payloads, exact protected coordinates, living-person private identifiers, or unpublished source excerpts in fixture content.
- [ ] Update this README when schema fields, enum values, digest requirements, or expected-error behavior changes.
- [ ] Run the schema fixture test before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Invalid fixture | CONFIRMED | `invalid_1.json` exists and omits required `id`. |
| Expected-error file | CONFIRMED | `invalid_1.expected_error.txt` exists and contains `required`. |
| Positive fixture | CONFIRMED | `valid/valid_1.json` exists and includes `id`. |
| Schema | CONFIRMED | `ai_receipt.schema.json` defines required fields, digest patterns, finite outcome enum, fixture root, and additional-property behavior. |
| Contract | CONFIRMED | `contracts/runtime/ai_receipt.md` defines semantic meaning and distinguishes AIReceipt from model truth, EvidenceBundle, PolicyDecision, RuntimeResponseEnvelope, chain-of-thought storage, and publication authority. |
| Test execution | NOT RUN | No validators, pytest, policy tests, runtime checks, citation checks, receipt persistence checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define invalid-fixture guidance. |
| [`invalid_1.json`](invalid_1.json) | CONFIRMED | Current negative fixture omits required `id`. | Only one invalid case is currently documented here. |
| [`invalid_1.expected_error.txt`](invalid_1.expected_error.txt) | CONFIRMED | Current expected-error matcher is `required`. | Broad matcher; may be tightened later. |
| [`../valid/valid_1.json`](../valid/valid_1.json) | CONFIRMED | Paired positive fixture includes `id` and other required fields. | Positive lane README was not checked during this update. |
| [`../../../../../../schemas/contracts/v1/runtime/ai_receipt.schema.json`](../../../../../../schemas/contracts/v1/runtime/ai_receipt.schema.json) | CONFIRMED | Schema shape, required fields, digest patterns, enum values, fixture root, validator path, and status. | Schema status is `PROPOSED`; validator implementation was not verified. |
| [`../../../../../../contracts/runtime/ai_receipt.md`](../../../../../../contracts/runtime/ai_receipt.md) | CONFIRMED | Semantic meaning, governed-AI accountability boundary, and distinction from evidence, policy, runtime envelopes, model truth, and chain-of-thought storage. | Does not prove runtime adapter enforcement, citation validation, receipt persistence, or CI status. |
| `../../../../../../tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN | Fixture discovery and invalid fixture behavior. | Tests were not run during this update. |
| `../../../../../../docs/doctrine/directory-rules.md` | CONFIRMED | `fixtures/` is the root for golden, valid, and invalid test inputs; contracts/schemas/policy split remains separate. | Specific fixture completeness requires tests or inventory. |

[Back to top](#top)
