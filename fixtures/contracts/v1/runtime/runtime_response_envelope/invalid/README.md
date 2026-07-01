<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/runtime/runtime-response-envelope/invalid/readme
title: runtime_response_envelope invalid fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): runtime steward; TODO(owner): API steward; TODO(owner): schema steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): evidence steward; TODO(owner): correction steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-06-30 expansion
updated: 2026-06-30
policy_label: public-review
related:
  - ../valid/valid_1.json
  - invalid_1.json
  - invalid_1.expected_error.txt
  - ../../../../../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
  - ../../../../../../schemas/contracts/v1/evidence/evidence_ref.schema.json
  - ../../../../../../contracts/runtime/runtime_response_envelope.md
  - ../../../../../../contracts/runtime/README.md
  - ../../../../../../contracts/runtime/decision_envelope.md
  - ../../../../../../contracts/runtime/run_receipt.md
  - ../../../../../../contracts/runtime/ai_receipt.md
  - ../../../../../../contracts/evidence/evidence_bundle.md
  - ../../../../../../contracts/policy/policy_decision.md
  - ../../../../../../policy/runtime/
  - ../../../../../../tools/validators/validate_runtime_response_envelope.py
  - ../../../../../../tests/schemas/test_common_contracts.py
  - ../../../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, v1, runtime, runtime-response-envelope, invalid-fixtures, expected-error, json-schema, governed-api, trust-membrane, finite-outcomes, evidence-refs, policy-state, freshness, correction-state, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/contracts/v1/runtime/runtime_response_envelope/invalid/README.md`."
  - "Invalid fixtures are intentionally failing examples for the `runtime_response_envelope` schema."
  - "Current invalid fixture coverage is one missing-required-field case: `invalid_1.json` omits `id`; expected error matcher is `required`."
  - "No tests, validators, runtime/API implementations, policy checks, evidence-ref resolution, correction-state checks, public-client tests, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `runtime_response_envelope` invalid fixtures

Negative fixture lane for the KFM `runtime_response_envelope` runtime contract schema.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Family: runtime" src="https://img.shields.io/badge/family-runtime-blue">
  <img alt="Contract: runtime_response_envelope" src="https://img.shields.io/badge/contract-runtime__response__envelope-purple">
  <img alt="Lane: invalid" src="https://img.shields.io/badge/lane-invalid-critical">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/contracts/v1/runtime/runtime_response_envelope/invalid/README.md`  
**Fixture posture:** invalid JSON Schema fixture lane  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/runtime/runtime_response_envelope.schema.json`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Schema basis](#schema-basis) · [Why this fixture fails](#why-this-fixture-fails) · [Authority boundary](#authority-boundary) · [Harness behavior](#harness-behavior) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are expected to fail schema validation. They are not RuntimeResponseEnvelopes, governed API responses, evidence, EvidenceBundles, PolicyDecisions, DecisionEnvelopes, AIReceipts, RunReceipts, release approval, review approval, public-client permission, or publication authority.

---

## Purpose

This directory stores negative JSON examples for the `runtime_response_envelope` schema.

Use this lane to prove that malformed or incomplete `RuntimeResponseEnvelope`-like objects are rejected before they can be treated as governed client-facing response envelopes. Invalid fixtures help preserve the KFM trust membrane: public and semi-public clients should receive bounded runtime envelopes, not incomplete response-shaped payloads that bypass identifier, evidence, policy, freshness, or correction posture.

---

## Current inventory

| File | Role | Expected result | Status |
|---|---|---|---|
| [`invalid_1.json`](invalid_1.json) | Negative fixture missing required `id`. | Schema validation should fail. | CONFIRMED |
| [`invalid_1.expected_error.txt`](invalid_1.expected_error.txt) | Expected-error matcher for `invalid_1.json`. | Combined schema errors should include `required`. | CONFIRMED / BROAD MATCHER |

Current invalid fixture:

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

The paired positive fixture currently includes the missing `id` field:

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

---

## Schema basis

The current schema evidence for this fixture lane is:

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

## Why this fixture fails

`invalid_1.json` omits `id`, which is required by the paired schema.

That failure matters because `id` is the stable identifier for the runtime response envelope. Without it, downstream clients and review/correction flows cannot reliably reconcile, supersede, withdraw, audit, or trace the envelope that was issued. A response-shaped payload with outcome, evidence refs, policy state, freshness, and correction state but no stable identifier must not silently pass as a governed `RuntimeResponseEnvelope`.

Expected-error matcher:

```text
required
```

This matcher is intentionally broad. It confirms the missing-field class of failure, but it does not pin the full validator wording. A later fixture pass may tighten it to the exact missing property name once validator output is stable enough.

> [!WARNING]
> A `RuntimeResponseEnvelope` is not raw evidence storage, canonical lifecycle storage, policy execution, model truth, or release approval. It is the governed response boundary clients may interpret only within policy and evidence constraints.

---

## Authority boundary

| Responsibility | Home | Status in this check |
|---|---|---|
| Negative fixture examples | `fixtures/contracts/v1/runtime/runtime_response_envelope/invalid/` | CONFIRMED |
| Positive fixture examples | `fixtures/contracts/v1/runtime/runtime_response_envelope/valid/` | CONFIRMED file present / README not checked in this update |
| Machine-checkable shape | `schemas/contracts/v1/runtime/runtime_response_envelope.schema.json` | CONFIRMED |
| Semantic contract | `contracts/runtime/runtime_response_envelope.md` | CONFIRMED |
| EvidenceRef schema | `schemas/contracts/v1/evidence/evidence_ref.schema.json` | REFERENCED BY SCHEMA / NOT RECHECKED HERE |
| Runtime policy | `policy/runtime/` | OUT OF SCOPE FOR THIS README |
| Validator implementation | `tools/validators/validate_runtime_response_envelope.py` | NEEDS VERIFICATION |
| Schema test harness | `tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN |

Do not collapse this fixture lane into the semantic contract, schema, executable runtime/API behavior, evidence bundle, evidence-ref resolver, policy decision, decision envelope, AI receipt, run receipt, release manifest, review record, correction record, or receipt persistence layer.

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

This README documents expected fixture behavior only. It does not claim that pytest, CI, runtime/API behavior, policy evaluation, evidence-ref resolution, correction-state handling, public-client rendering, or the dedicated RuntimeResponseEnvelope validator were run during this update.

---

## Maintenance checklist

Before changing this invalid fixture lane:

- [ ] Keep failing examples under `invalid/invalid_<n>.json`.
- [ ] Keep expected-error text beside the invalid fixture it describes.
- [ ] Keep at least one missing-required-field fixture unless another fixture family covers that failure class.
- [ ] Add identifier-pattern, digest-pattern, enum, date-time, evidence-ref shape, and additional-property failures when RuntimeResponseEnvelope coverage expands.
- [ ] Avoid private, unpublished, source-system, prompt-like, or policy-restricted content.
- [ ] Keep fixture refs small, deterministic, public-safe, and reviewable.
- [ ] Update this README when schema fields, enum values, evidence-ref requirements, state vocabularies, or expected-error behavior changes.
- [ ] Run the schema fixture test before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Invalid fixture | CONFIRMED | `invalid_1.json` exists and omits required `id`. |
| Expected-error file | CONFIRMED | `invalid_1.expected_error.txt` exists and contains `required`. |
| Positive fixture | CONFIRMED | `valid/valid_1.json` exists and includes `id`. |
| Schema | CONFIRMED | `runtime_response_envelope.schema.json` defines required fields, digest pattern, date-time field, finite outcome enum, EvidenceRef array, fixture root, and additional-property behavior. |
| Contract | CONFIRMED | `contracts/runtime/runtime_response_envelope.md` defines semantic meaning and distinguishes RuntimeResponseEnvelope from raw evidence storage, canonical lifecycle storage, policy execution, model truth, and release approval. |
| Test execution | NOT RUN | No validators, pytest, runtime/API tests, policy tests, evidence-ref resolution checks, correction checks, public-client tests, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define invalid-fixture guidance. |
| [`invalid_1.json`](invalid_1.json) | CONFIRMED | Current negative fixture omits required `id`. | Only one invalid case is currently documented here. |
| [`invalid_1.expected_error.txt`](invalid_1.expected_error.txt) | CONFIRMED | Current expected-error matcher is `required`. | Broad matcher; may be tightened later. |
| [`../valid/valid_1.json`](../valid/valid_1.json) | CONFIRMED | Paired positive fixture includes `id` and other required fields. | Positive lane README was not checked during this update. |
| [`../../../../../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json`](../../../../../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json) | CONFIRMED | Schema shape, required fields, digest pattern, date-time field, enum values, EvidenceRef array, fixture root, validator path, and status. | Schema status is `PROPOSED`; validator implementation was not verified. |
| [`../../../../../../contracts/runtime/runtime_response_envelope.md`](../../../../../../contracts/runtime/runtime_response_envelope.md) | CONFIRMED | Semantic meaning, governed API trust membrane, field surface, and distinction from evidence storage, policy execution, model truth, and release approval. | Does not prove runtime/API implementation, evidence-ref resolution, policy behavior, correction handling, validator wiring, or CI status. |
| `../../../../../../tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN | Fixture discovery and invalid fixture behavior. | Tests were not run during this update. |
| `../../../../../../docs/doctrine/directory-rules.md` | CONFIRMED | `fixtures/` is the root for golden, valid, and invalid test inputs; contracts/schemas/policy split remains separate. | Specific fixture completeness requires tests or inventory. |

[Back to top](#top)
