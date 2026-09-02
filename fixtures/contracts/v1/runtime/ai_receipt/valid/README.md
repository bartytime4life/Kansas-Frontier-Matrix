<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/runtime/ai-receipt/valid/readme
title: ai_receipt valid fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): runtime steward; TODO(owner): governed AI steward; TODO(owner): schema steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-06-30 expansion
updated: 2026-06-30
policy_label: public-review
related:
  - valid_1.json
  - ../invalid/README.md
  - ../invalid/invalid_1.json
  - ../invalid/invalid_1.expected_error.txt
  - ../../../../../../schemas/contracts/v1/runtime/ai_receipt.schema.json
  - ../../../../../../contracts/runtime/ai_receipt.md
  - ../../../../../../contracts/runtime/README.md
  - ../../../../../../contracts/policy/policy_decision.md
  - ../../../../../../policy/runtime/
  - ../../../../../../policy/ai/
  - ../../../../../../tools/validators/validate_ai_receipt.py
  - ../../../../../../tests/schemas/test_common_contracts.py
  - ../../../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, v1, runtime, ai-receipt, valid-fixtures, json-schema, governed-ai, receipt, finite-outcomes, cite-or-abstain, no-chain-of-thought, no-model-truth, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/contracts/v1/runtime/ai_receipt/valid/README.md`."
  - "Valid fixtures are positive schema examples for the `ai_receipt` schema."
  - "Current valid fixture coverage is one minimal passing case: `valid_1.json`."
  - "No tests, validators, policy bundles, runtime adapters, citation validators, receipt persistence checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `ai_receipt` valid fixtures

Positive fixture lane for the KFM `ai_receipt` runtime contract schema.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Family: runtime" src="https://img.shields.io/badge/family-runtime-blue">
  <img alt="Contract: ai_receipt" src="https://img.shields.io/badge/contract-ai__receipt-purple">
  <img alt="Lane: valid" src="https://img.shields.io/badge/lane-valid-success">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/contracts/v1/runtime/ai_receipt/valid/README.md`  
**Fixture posture:** valid JSON Schema fixture lane  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/runtime/ai_receipt.schema.json`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Schema basis](#schema-basis) · [Why this fixture passes](#why-this-fixture-passes) · [Authority boundary](#authority-boundary) · [Harness behavior](#harness-behavior) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are expected to pass schema validation. They are not model truth, evidence, chain-of-thought storage, policy decisions, citation validation results, public-release approval, runtime response envelopes, persisted receipts, or executable runtime policy.

---

## Purpose

This directory stores positive JSON examples for the `ai_receipt` schema.

Use this lane to prove that a minimal well-shaped `AIReceipt`-like object can pass schema validation before it is used by higher-level runtime, policy, citation-validation, receipt-persistence, review, correction, or publication workflows. Passing this schema fixture only proves shape. It does not prove that generated language is true, evidence-backed, cite-valid, policy-approved, release-approved, or safe for public rendering.

---

## Current inventory

| File | Role | Expected result | Status |
|---|---|---|---|
| [`valid_1.json`](valid_1.json) | Minimal positive fixture for `ai_receipt`. | Schema validation should pass. | CONFIRMED |

Current valid fixture:

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

The paired negative fixture currently omits the required `id` field and is expected to fail with a `required` error:

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

## Why this fixture passes

`valid_1.json` includes every field currently required by the paired schema:

- `id`
- `run_id`
- `adapter`
- `model_ref`
- `inputs_digest`
- `outputs_digest`
- `policy_decision_ref`
- `citation_validation_ref`
- `outcome`

It also uses schema-allowed values and digest patterns:

| Field | Fixture value | Schema posture |
|---|---|---|
| `id` | `ai1` | Matches identifier pattern. |
| `inputs_digest` | `sha256:` plus 64 lowercase hex characters | Matches SHA-256 digest pattern. |
| `outputs_digest` | `sha256:` plus 64 lowercase hex characters | Matches SHA-256 digest pattern. |
| `outcome` | `ABSTAIN` | Allowed finite outcome. |

This positive fixture is intentionally minimal. It proves the schema accepts a compact AIReceipt object, not that the receipt is persisted, cite-valid, policy-approved, evidence-backed, release-approved, or safe for public rendering.

> [!WARNING]
> An `AIReceipt` is not proof that generated language is true. It is an accountability receipt for a bounded AI-mediated runtime event.

---

## Authority boundary

| Responsibility | Home | Status in this check |
|---|---|---|
| Positive fixture examples | `fixtures/contracts/v1/runtime/ai_receipt/valid/` | CONFIRMED |
| Negative fixture examples | `fixtures/contracts/v1/runtime/ai_receipt/invalid/` | CONFIRMED |
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

For valid fixtures, the observed harness pattern is:

```text
valid/valid_*.json
```

Expected behavior:

| Fixture pattern | Expected result |
|---|---|
| `valid/valid_*.json` | No JSON Schema errors. |

This README documents expected fixture behavior only. It does not claim that pytest, CI, runtime adapters, policy bundles, citation validators, receipt persistence, or the dedicated AIReceipt validator were run during this update.

---

## Maintenance checklist

Before changing this valid fixture lane:

- [ ] Keep passing examples under `valid/valid_<n>.json`.
- [ ] Keep at least one minimal positive fixture unless the schema family is intentionally retired.
- [ ] Keep positive fixtures paired with negative fixtures under `../invalid/`.
- [ ] Add richer valid fixtures only when they remain public-safe and reviewable.
- [ ] Avoid sensitive, private, unpublished, source-system, prompt, credential, or policy-restricted content.
- [ ] Never place chain-of-thought, private model internals, raw prompts, secrets, sensitive evidence payloads, exact protected coordinates, living-person private identifiers, unpublished source excerpts, or policy-restricted material in fixture content.
- [ ] Update this README when schema fields, enum values, digest requirements, or fixture coverage changes.
- [ ] Run the schema fixture test before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Valid fixture | CONFIRMED | `valid_1.json` exists and includes all schema-required fields. |
| Invalid lane README | CONFIRMED | `../invalid/README.md` exists and documents the missing-`id` negative case. |
| Invalid fixture | CONFIRMED | `../invalid/invalid_1.json` exists and omits required `id`. |
| Expected-error file | CONFIRMED | `../invalid/invalid_1.expected_error.txt` exists and contains `required`. |
| Schema | CONFIRMED | `ai_receipt.schema.json` defines required fields, digest patterns, finite outcome enum, fixture root, and additional-property behavior. |
| Contract | CONFIRMED | `contracts/runtime/ai_receipt.md` defines semantic meaning and distinguishes AIReceipt from model truth, EvidenceBundle, PolicyDecision, RuntimeResponseEnvelope, chain-of-thought storage, and publication authority. |
| Test execution | NOT RUN | No validators, pytest, policy tests, runtime checks, citation checks, receipt persistence checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define valid-fixture guidance. |
| [`valid_1.json`](valid_1.json) | CONFIRMED | Current positive fixture includes required fields, digest patterns, and finite `outcome`. | Only one valid case is currently documented here. |
| [`../invalid/README.md`](../invalid/README.md) | CONFIRMED | Documents the negative fixture lane. | Does not prove tests were run. |
| [`../invalid/invalid_1.json`](../invalid/invalid_1.json) | CONFIRMED | Paired negative fixture omits required `id`. | Only one invalid case is currently documented here. |
| [`../invalid/invalid_1.expected_error.txt`](../invalid/invalid_1.expected_error.txt) | CONFIRMED | Current expected-error matcher is `required`. | Broad matcher; may be tightened later. |
| [`../../../../../../schemas/contracts/v1/runtime/ai_receipt.schema.json`](../../../../../../schemas/contracts/v1/runtime/ai_receipt.schema.json) | CONFIRMED | Schema shape, required fields, digest patterns, enum values, fixture root, validator path, and status. | Schema status is `PROPOSED`; validator implementation was not verified. |
| [`../../../../../../contracts/runtime/ai_receipt.md`](../../../../../../contracts/runtime/ai_receipt.md) | CONFIRMED | Semantic meaning, governed-AI accountability boundary, and distinction from evidence, policy, runtime envelopes, model truth, and chain-of-thought storage. | Does not prove runtime adapter enforcement, citation validation, receipt persistence, or CI status. |
| `../../../../../../tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN | Fixture discovery and valid fixture behavior. | Tests were not run during this update. |
| `../../../../../../docs/doctrine/directory-rules.md` | CONFIRMED | `fixtures/` is the root for golden, valid, and invalid test inputs; contracts/schemas/policy split remains separate. | Specific fixture completeness requires tests or inventory. |

[Back to top](#top)
