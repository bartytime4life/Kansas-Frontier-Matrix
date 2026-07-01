<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/runtime/ai-receipt/readme
title: ai_receipt fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): runtime steward; TODO(owner): governed AI steward; TODO(owner): schema steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-06-30 expansion
updated: 2026-06-30
policy_label: public-review
related:
  - valid/README.md
  - valid/valid_1.json
  - invalid/README.md
  - invalid/invalid_1.json
  - invalid/invalid_1.expected_error.txt
  - ../../../../../schemas/contracts/v1/runtime/ai_receipt.schema.json
  - ../../../../../contracts/runtime/ai_receipt.md
  - ../../../../../contracts/runtime/README.md
  - ../../../../../contracts/policy/policy_decision.md
  - ../../../../../policy/runtime/
  - ../../../../../policy/ai/
  - ../../../../../tools/validators/validate_ai_receipt.py
  - ../../../../../tests/schemas/test_common_contracts.py
  - ../../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, v1, runtime, ai-receipt, valid-fixtures, invalid-fixtures, expected-error, json-schema, governed-ai, receipt, finite-outcomes, cite-or-abstain, no-chain-of-thought, no-model-truth, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/contracts/v1/runtime/ai_receipt/README.md`."
  - "This directory is the schema-declared fixture root for `ai_receipt`."
  - "Fixtures are sample test inputs only; semantic meaning, machine schema shape, executable runtime policy, citation validation, and release authority stay in their owning roots."
  - "Current fixture coverage includes one valid case and one invalid missing-required-field case."
  - "No tests, validators, policy bundles, runtime adapters, citation validators, receipt persistence checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `ai_receipt` fixtures

Fixture family for the KFM `ai_receipt` runtime contract schema.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Family: runtime" src="https://img.shields.io/badge/family-runtime-blue">
  <img alt="Contract: ai_receipt" src="https://img.shields.io/badge/contract-ai__receipt-purple">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
  <img alt="AI: not truth" src="https://img.shields.io/badge/AI-not__truth-critical">
</p>

**Path:** `fixtures/contracts/v1/runtime/ai_receipt/README.md`  
**Fixture posture:** JSON Schema valid/invalid fixture family  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/runtime/ai_receipt.schema.json`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Schema basis](#schema-basis) · [Authority boundary](#authority-boundary) · [Harness behavior](#harness-behavior) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are schema fixtures. They are not model truth, EvidenceBundles, PolicyDecisions, citation validation results, RuntimeResponseEnvelopes, chain-of-thought storage, persisted receipt records, release approval, review approval, or publication authority.

---

## Purpose

This directory groups positive and negative JSON fixtures for the `ai_receipt` schema.

Use this fixture family to verify that KFM accepts a minimal well-shaped `AIReceipt`-like object and rejects an incomplete one. The schema-declared fixture root is:

```text
fixtures/contracts/v1/runtime/ai_receipt/
```

A passing fixture proves schema shape only. It does not prove that generated language is true, that evidence refs resolve, that citation validation passed, that policy was correct, that a runtime adapter behaved correctly, that receipt persistence worked, that release gates passed, or that a public API, map, or AI surface may render the result.

---

## Current inventory

| Lane | File | Current role | Status |
|---|---|---|---|
| [`valid/`](valid/README.md) | [`valid_1.json`](valid/valid_1.json) | Minimal positive fixture with every required top-level field, SHA-256 digests, and allowed finite `outcome`. | CONFIRMED |
| [`invalid/`](invalid/README.md) | [`invalid_1.json`](invalid/invalid_1.json) | Minimal negative fixture matching the positive case but missing required `id`. | CONFIRMED |
| [`invalid/`](invalid/README.md) | [`invalid_1.expected_error.txt`](invalid/invalid_1.expected_error.txt) | Current expected-error matcher: `required`. | CONFIRMED / BROAD MATCHER |

Current positive fixture shape:

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

Current negative fixture shape:

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

The current schema evidence for this fixture family is:

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

## Authority boundary

| Responsibility | Home | Status in this check |
|---|---|---|
| Fixture examples | `fixtures/contracts/v1/runtime/ai_receipt/` | CONFIRMED |
| Valid examples | `fixtures/contracts/v1/runtime/ai_receipt/valid/` | CONFIRMED |
| Invalid examples | `fixtures/contracts/v1/runtime/ai_receipt/invalid/` | CONFIRMED |
| Machine-checkable shape | `schemas/contracts/v1/runtime/ai_receipt.schema.json` | CONFIRMED |
| Semantic contract | `contracts/runtime/ai_receipt.md` | CONFIRMED |
| Runtime / AI policy | `policy/runtime/`, `policy/ai/` | OUT OF SCOPE FOR THIS README |
| Validator implementation | `tools/validators/validate_ai_receipt.py` | NEEDS VERIFICATION |
| Schema test harness | `tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN |

`AIReceipt` must remain distinguishable from:

| Do not collapse `AIReceipt` into | Why |
|---|---|
| Generated AI text | Generated language is interpretive and must not become source-of-truth. |
| `EvidenceBundle` | Evidence supports claims; the receipt only records an AI-mediated runtime event. |
| `PolicyDecision` | Policy decisions govern the event; the receipt references them. |
| Citation validation result | Citation validation governs cite-or-abstain posture; the receipt references it. |
| `RuntimeResponseEnvelope` | Runtime envelopes carry client-facing response context; AIReceipt records accountability for the AI step. |
| Chain-of-thought or private model internals | The receipt must not store private reasoning, hidden prompts, or model internals. |
| Release or publication approval | A receipt alone cannot approve, publish, or expose content. |

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
fixtures/contracts/v1/runtime/ai_receipt/
```

Observed expectations:

| Fixture pattern | Expected result |
|---|---|
| `valid/valid_*.json` | no JSON Schema errors |
| `invalid/invalid_*.json` | at least one JSON Schema error |
| `invalid/invalid_*.expected_error.txt` | expected text appears in combined error messages |

This README documents expected fixture behavior only. It does not claim that pytest, CI, runtime adapters, policy bundles, citation validators, receipt persistence, or the dedicated AIReceipt validator was run during this update.

---

## Maintenance checklist

Before changing this fixture family:

- [ ] Keep passing examples under `valid/valid_<n>.json`.
- [ ] Keep failing examples under `invalid/invalid_<n>.json`.
- [ ] Keep expected-error text beside the invalid fixture it describes.
- [ ] Keep fixture cases small, deterministic, public-safe, and reviewable.
- [ ] Keep at least one valid minimal fixture and one missing-required-field invalid fixture.
- [ ] Add digest-pattern, enum, identifier-pattern, and additional-property fixtures as coverage expands.
- [ ] Avoid sensitive, private, unpublished, source-system, prompt, credential, or policy-restricted content.
- [ ] Never place chain-of-thought, private model internals, raw prompts, secrets, sensitive evidence payloads, exact protected coordinates, living-person private identifiers, unpublished source excerpts, or policy-restricted material in fixture content.
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
| Schema | CONFIRMED | `ai_receipt.schema.json` defines required fields, digest patterns, finite outcome enum, fixture root, and additional-property behavior. |
| Contract | CONFIRMED | `contracts/runtime/ai_receipt.md` defines semantic meaning and separates AIReceipt from model truth, EvidenceBundle, PolicyDecision, RuntimeResponseEnvelope, chain-of-thought storage, and publication authority. |
| Validator file | NEEDS VERIFICATION | `tools/validators/validate_ai_receipt.py` is declared by schema but implementation/wiring was not verified during this update. |
| Test execution | NOT RUN | No validators, pytest, policy tests, runtime checks, citation checks, receipt persistence checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define fixture-family guidance. |
| [`valid/README.md`](valid/README.md) | CONFIRMED | Positive fixture lane guidance. | Does not prove tests were run. |
| [`valid/valid_1.json`](valid/valid_1.json) | CONFIRMED | Current positive fixture includes required fields, digest patterns, and finite `outcome`. | Only one valid fixture is currently documented. |
| [`invalid/README.md`](invalid/README.md) | CONFIRMED | Negative fixture lane guidance. | Does not prove tests were run. |
| [`invalid/invalid_1.json`](invalid/invalid_1.json) | CONFIRMED | Current negative fixture omits required `id`. | Only one invalid fixture is currently documented. |
| [`invalid/invalid_1.expected_error.txt`](invalid/invalid_1.expected_error.txt) | CONFIRMED | Current expected-error matcher is `required`. | Broad matcher; may be tightened later. |
| [`../../../../../schemas/contracts/v1/runtime/ai_receipt.schema.json`](../../../../../schemas/contracts/v1/runtime/ai_receipt.schema.json) | CONFIRMED | Schema shape, required fields, digest patterns, enum values, fixture root, validator path, and status. | Schema status is `PROPOSED`; validator implementation was not verified. |
| [`../../../../../contracts/runtime/ai_receipt.md`](../../../../../contracts/runtime/ai_receipt.md) | CONFIRMED | Semantic meaning, governed-AI accountability boundary, and distinction from evidence, policy, runtime envelopes, model truth, and chain-of-thought storage. | Does not prove runtime adapter enforcement, citation validation, receipt persistence, or CI status. |
| `../../../../../tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN | Fixture discovery and valid/invalid fixture behavior. | Tests were not run during this update. |
| `../../../../../docs/doctrine/directory-rules.md` | CONFIRMED | `fixtures/` is the root for golden, valid, and invalid test inputs; contracts/schemas/policy split remains separate. | Specific fixture completeness requires tests or inventory. |

[Back to top](#top)
