<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/runtime/runtime-response-envelope/readme
title: runtime_response_envelope fixtures README
type: fixture-readme
version: v0.2.0
status: draft
owners: TODO(owner): runtime steward; TODO(owner): API steward; TODO(owner): schema steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): evidence steward; TODO(owner): correction steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-06-30 expansion
updated: 2026-08-02
policy_label: public-review
related:
  - valid/README.md
  - valid/valid_1.json
  - valid/valid_2.json
  - valid/valid_3.json
  - valid/valid_4.json
  - invalid/README.md
  - invalid/invalid_1.json
  - invalid/invalid_1.expected_error.txt
  - invalid/invalid_2.json
  - invalid/invalid_2.expected_error.txt
  - invalid/invalid_3.json
  - invalid/invalid_3.expected_error.txt
  - invalid/invalid_4.json
  - invalid/invalid_4.expected_error.txt
  - ../../../../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
  - ../../../../../schemas/contracts/v1/evidence/evidence_ref.schema.json
  - ../../../../../contracts/runtime/runtime_response_envelope.md
  - ../../../../../contracts/runtime/README.md
  - ../../../../../contracts/runtime/decision_envelope.md
  - ../../../../../contracts/runtime/run_receipt.md
  - ../../../../../contracts/runtime/ai_receipt.md
  - ../../../../../contracts/evidence/evidence_bundle.md
  - ../../../../../contracts/policy/policy_decision.md
  - ../../../../../policy/runtime/
  - ../../../../../tools/validators/validate_runtime_response_envelope.py
  - ../../../../../tests/schemas/test_common_contracts.py
  - ../../../../../tests/runtime_proof/test_envelope_finite_outcomes.py
  - ../../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, v1, runtime, runtime-response-envelope, valid-fixtures, invalid-fixtures, expected-error, json-schema, governed-api, trust-membrane, finite-outcomes, evidence-refs, policy-state, freshness, correction-state, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/contracts/v1/runtime/runtime_response_envelope/README.md`."
  - "This directory is the schema-declared fixture root for `runtime_response_envelope`."
  - "Fixtures are sample test inputs only; semantic meaning, machine schema shape, runtime/API behavior, evidence resolution, policy behavior, and release authority stay in their owning roots."
  - "Current valid fixtures cover ANSWER, ABSTAIN, DENY, and ERROR machine shape."
  - "Current invalid fixtures cover missing id, extra property, invalid id pattern, and unknown outcome rejection."
  - "Schema fixtures and no-network runtime-proof tests do not establish semantic outcome selection, runtime/API behavior, evidence resolution, policy correctness, release approval, or publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `runtime_response_envelope` fixtures

Fixture family for the KFM `runtime_response_envelope` runtime contract schema.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Family: runtime" src="https://img.shields.io/badge/family-runtime-blue">
  <img alt="Contract: runtime_response_envelope" src="https://img.shields.io/badge/contract-runtime__response__envelope-purple">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
  <img alt="Outcomes: finite" src="https://img.shields.io/badge/outcomes-ANSWER%20%7C%20ABSTAIN%20%7C%20DENY%20%7C%20ERROR-informational">
</p>

**Path:** `fixtures/contracts/v1/runtime/runtime_response_envelope/README.md`  
**Fixture posture:** JSON Schema valid/invalid fixture family  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/runtime/runtime_response_envelope.schema.json`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Schema basis](#schema-basis) · [Authority boundary](#authority-boundary) · [Harness behavior](#harness-behavior) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are schema fixtures. They are not governed API responses, evidence records, EvidenceBundles, PolicyDecisions, DecisionEnvelopes, AIReceipts, RunReceipts, release approval, review approval, public-client permission, or publication authority.

---

## Purpose

This directory groups positive and negative JSON fixtures for the `runtime_response_envelope` schema.

Use this fixture family to verify that KFM accepts well-shaped examples for all four finite outcomes and rejects incomplete or open-ended shapes. The schema-declared fixture root is:

```text
fixtures/contracts/v1/runtime/runtime_response_envelope/
```

A passing fixture proves schema shape only. It does not prove that evidence refs resolve, policy evaluation was correct, runtime/API behavior is implemented, correction state is current, release gates passed, or a public API, map, AI, or UI surface may render the response.

---

## Current inventory

| Lane | File | Current role | Status |
|---|---|---|---|
| [`valid/`](valid/README.md) | [`valid_1.json`](valid/valid_1.json) | Minimal positive fixture with every required top-level field, SHA-256 spec hash, finite outcome, state strings, and empty `evidence_refs`. | CONFIRMED |
| [`valid/`](valid/README.md) | [`valid_2.json`](valid/valid_2.json) | Shape-valid `ANSWER` with one synthetic EvidenceRef. | CONFIRMED |
| [`valid/`](valid/README.md) | [`valid_3.json`](valid/valid_3.json) | Shape-valid `DENY` without a restricted payload. | CONFIRMED |
| [`valid/`](valid/README.md) | [`valid_4.json`](valid/valid_4.json) | Shape-valid safe `ERROR` without internal diagnostics. | CONFIRMED |
| [`invalid/`](invalid/README.md) | [`invalid_1.json`](invalid/invalid_1.json) | Minimal negative fixture matching the positive case but missing required `id`. | CONFIRMED |
| [`invalid/`](invalid/README.md) | [`invalid_1.expected_error.txt`](invalid/invalid_1.expected_error.txt) | Current expected-error matcher: `required`. | CONFIRMED / BROAD MATCHER |
| [`invalid/`](invalid/README.md) | [`invalid_2.json`](invalid/invalid_2.json) | Negative fixture with a disallowed extra property. | CONFIRMED |
| [`invalid/`](invalid/README.md) | [`invalid_3.json`](invalid/invalid_3.json) | Negative fixture with an invalid identifier. | CONFIRMED |
| [`invalid/`](invalid/README.md) | [`invalid_4.json`](invalid/invalid_4.json) | Negative fixture with unknown outcome `WAITING`. | CONFIRMED |

Current positive fixture shape:

```json
{
  "id": "resp1",
  "spec_hash": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "version": "v1",
  "issued_at": "2026-05-09T00:00:00Z",
  "outcome": "ABSTAIN",
  "reason_code": "NOT_IMPLEMENTED",
  "evidence_refs": [],
  "policy_state": "baseline",
  "freshness": "current",
  "correction_state": "none"
}
```

Current negative fixture shape:

```json
{
  "spec_hash": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "version": "v1",
  "issued_at": "2026-05-09T00:00:00Z",
  "outcome": "ABSTAIN",
  "reason_code": "NOT_IMPLEMENTED",
  "evidence_refs": [],
  "policy_state": "baseline",
  "freshness": "current",
  "correction_state": "none"
}
```

---

## Schema basis

The current schema evidence for this fixture family is:

```text
schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
```

Confirmed schema facts:

| Item | Value |
|---|---|
| Schema title | `runtime_response_envelope` |
| Root type | object |
| Required fields | `id`, `spec_hash`, `version`, `issued_at`, `outcome`, `reason_code`, `evidence_refs`, `policy_state`, `freshness`, `correction_state` |
| `id` | string matching `^[a-z][a-z0-9_:.-]*$` |
| `spec_hash` | string matching `^sha256:[a-f0-9]{64}$` |
| `issued_at` | string with `date-time` format |
| `outcome` enum values | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` |
| `evidence_refs` | array of `evidence_ref` objects |
| `policy_state` | string |
| `freshness` | string |
| `correction_state` | string |
| Additional properties | false |
| Declared contract doc | `contracts/runtime/runtime_response_envelope.md` |
| Declared fixture root | `fixtures/contracts/v1/runtime/runtime_response_envelope/` |
| Declared validator | `tools/validators/validate_runtime_response_envelope.py` |
| Declared policy path | `policy/runtime/` |
| Schema status | `PROPOSED` |

---

## Authority boundary

| Responsibility | Home | Status in this check |
|---|---|---|
| Fixture examples | `fixtures/contracts/v1/runtime/runtime_response_envelope/` | CONFIRMED |
| Valid examples | `fixtures/contracts/v1/runtime/runtime_response_envelope/valid/` | CONFIRMED |
| Invalid examples | `fixtures/contracts/v1/runtime/runtime_response_envelope/invalid/` | CONFIRMED |
| Machine-checkable shape | `schemas/contracts/v1/runtime/runtime_response_envelope.schema.json` | CONFIRMED |
| Semantic contract | `contracts/runtime/runtime_response_envelope.md` | CONFIRMED |
| EvidenceRef schema | `schemas/contracts/v1/evidence/evidence_ref.schema.json` | REFERENCED BY SCHEMA / NOT RECHECKED HERE |
| Runtime policy | `policy/runtime/` | OUT OF SCOPE FOR THIS README |
| Validator implementation | `tools/validators/validate_runtime_response_envelope.py` | NEEDS VERIFICATION |
| Schema test harness | `tests/schemas/test_common_contracts.py` | CONFIRMED executable coverage |
| Finite-outcome proof | `tests/runtime_proof/test_envelope_finite_outcomes.py` | CONFIRMED standard-library positive, negative, boundary, and alias coverage |

`RuntimeResponseEnvelope` must remain distinguishable from:

| Do not collapse `RuntimeResponseEnvelope` into | Why |
|---|---|
| Runtime/API implementation | The envelope is a contract-shaped response boundary; implementation lives elsewhere. |
| `EvidenceBundle` | Evidence supports claims; the envelope only carries evidence refs. |
| EvidenceRef resolution | Resolution must be performed by governed evidence/runtime logic, not assumed from fixture shape. |
| `PolicyDecision` | Policy decisions govern response posture; the envelope reports policy state. |
| `DecisionEnvelope` | Decision envelopes record finite runtime decision posture; this is the client-facing response envelope. |
| `AIReceipt` | AI receipts record AI-mediated accountability; this envelope is the response boundary. |
| `RunReceipt` | Run receipts record pipeline/runtime execution summaries; this envelope is client-facing response context. |
| Release or publication approval | A response envelope alone cannot publish content or approve release. |

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
fixtures/contracts/v1/runtime/runtime_response_envelope/
```

Observed expectations:

| Fixture pattern | Expected result |
|---|---|
| `valid/valid_*.json` | no JSON Schema errors |
| `invalid/invalid_*.json` | at least one JSON Schema error |
| `invalid/invalid_*.expected_error.txt` | expected text appears in combined error messages |

This README documents expected fixture behavior only. It does not claim that pytest, CI, runtime/API behavior, policy evaluation, evidence-ref resolution, correction-state handling, public-client rendering, or the dedicated RuntimeResponseEnvelope validator was run during this update.

---

## Maintenance checklist

Before changing this fixture family:

- [ ] Keep passing examples under `valid/valid_<n>.json`.
- [ ] Keep failing examples under `invalid/invalid_<n>.json`.
- [ ] Keep expected-error text beside the invalid fixture it describes.
- [ ] Keep fixture cases small, deterministic, public-safe, and reviewable.
- [ ] Keep at least one valid minimal fixture and one missing-required-field invalid fixture.
- [ ] Add identifier-pattern, digest-pattern, enum, date-time, evidence-ref shape, and additional-property fixtures as coverage expands.
- [ ] Add non-empty `evidence_refs` examples only when EvidenceRef schema expectations are verified in the same update.
- [ ] Avoid private, unpublished, source-system, prompt-like, or policy-restricted content.
- [ ] Keep fixture refs small, deterministic, public-safe, and reviewable.
- [ ] Update fixture docs when schema behavior changes.
- [ ] Verify the validator implementation before claiming validator maturity.
- [ ] Run the relevant schema tests before promotion.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Valid lane | CONFIRMED | Four fixtures cover the complete schema outcome enum. |
| Invalid lane | CONFIRMED | Four fixtures cover missing, extra, pattern, and enum failure classes with expected-error sidecars. |
| Schema | CONFIRMED | `runtime_response_envelope.schema.json` defines required fields, digest pattern, date-time field, finite outcome enum, EvidenceRef array, fixture root, and additional-property behavior. |
| Contract | CONFIRMED | `contracts/runtime/runtime_response_envelope.md` defines semantic meaning and separates RuntimeResponseEnvelope from evidence storage, canonical lifecycle storage, policy execution, model truth, and release approval. |
| Validator file | NEEDS VERIFICATION | `tools/validators/validate_runtime_response_envelope.py` is declared by schema but implementation/wiring was not verified during this update. |
| Test wiring | CONFIRMED | The canonical validator, common schema harness, runtime-proof suite, and finite-envelope workflow cover this fixture family. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define fixture-family guidance. |
| [`valid/README.md`](valid/README.md) | CONFIRMED | Positive fixture lane guidance. | Does not prove tests were run. |
| [`valid/`](valid/README.md) | CONFIRMED | Four synthetic fixtures cover every finite outcome and the closed top-level shape. | Shape coverage is not semantic/runtime proof. |
| [`invalid/README.md`](invalid/README.md) | CONFIRMED | Negative fixture lane guidance. | Does not prove tests were run. |
| [`invalid/`](invalid/README.md) | CONFIRMED | Four synthetic fixtures exercise missing field, extra property, identifier pattern, and finite enum rejection. | Does not cover every possible schema failure. |
| [`../../../../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json`](../../../../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json) | CONFIRMED | Schema shape, required fields, digest pattern, date-time field, enum values, EvidenceRef array, fixture root, validator path, and status. | Schema status is `PROPOSED`; validator implementation was not verified. |
| [`../../../../../contracts/runtime/runtime_response_envelope.md`](../../../../../contracts/runtime/runtime_response_envelope.md) | CONFIRMED | Semantic meaning, governed API trust membrane, field surface, and distinction from evidence storage, policy execution, model truth, and release approval. | Does not prove runtime/API implementation, evidence-ref resolution, policy behavior, correction handling, validator wiring, or CI status. |
| `../../../../../tests/schemas/test_common_contracts.py` | CONFIRMED | Fixture discovery and JSON Schema polarity. | Does not prove semantic outcome selection or runtime behavior. |
| `../../../../../tests/runtime_proof/test_envelope_finite_outcomes.py` | CONFIRMED | No-network closed-shape, alias, outcome coverage, and negative boundary checks. | Lightweight proof complements rather than replaces JSON Schema validation. |
| `../../../../../docs/doctrine/directory-rules.md` | CONFIRMED | `fixtures/` is the root for golden, valid, and invalid test inputs; contracts/schemas/policy split remains separate. | Specific fixture completeness requires tests or inventory. |

[Back to top](#top)
