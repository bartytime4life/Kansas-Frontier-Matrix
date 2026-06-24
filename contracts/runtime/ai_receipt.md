<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-runtime-ai-receipt
title: contracts/runtime/ai_receipt.md — AIReceipt Contract
type: contract
version: v0.2
status: draft; PROPOSED; schema-paired; governed-ai; receipt-contract
owners: OWNER_TBD — Runtime steward · Governed AI steward · Contracts steward · Schema steward · Policy steward · Evidence steward · Citation steward · Docs steward
created: NEEDS VERIFICATION — file existed before v0.2 expansion
updated: 2026-06-24
policy_label: public; contracts; runtime; ai-receipt; governed-ai; receipt; finite-outcomes; cite-or-abstain; no-chain-of-thought; no-model-truth
tags: [kfm, contracts, runtime, ai-receipt, governed-ai, receipt, model-adapter, model-ref, inputs-digest, outputs-digest, policy-decision-ref, citation-validation-ref, finite-outcomes, cite-or-abstain]
related:
  - ./README.md
  - ./runtime_response_envelope.md
  - ./decision_envelope.md
  - ../policy/policy_decision.md
  - ../evidence/evidence_bundle.md
  - ../../schemas/contracts/v1/runtime/ai_receipt.schema.json
  - ../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
  - ../../policy/runtime/
  - ../../policy/ai/
  - ../../fixtures/contracts/v1/runtime/ai_receipt/
  - ../../tools/validators/validate_ai_receipt.py
  - ../../docs/architecture/governed-ai.md
  - ../../docs/architecture/contract-schema-policy-split.md
notes:
  - "Expanded from existing schema-paired stub at `contracts/runtime/ai_receipt.md`."
  - "Paired schema verified at `schemas/contracts/v1/runtime/ai_receipt.schema.json`; schema status is PROPOSED."
  - "The schema requires id, run_id, adapter, model_ref, inputs_digest, outputs_digest, policy_decision_ref, citation_validation_ref, and outcome; additional properties are false."
  - "AIReceipt records accountability for an AI-mediated runtime event; it is not model truth, not EvidenceBundle, not PolicyDecision, not RuntimeResponseEnvelope, not chain-of-thought storage, and not publication authority."
  - "Rollback target for this expansion is previous blob SHA `985aff8caf79ed98a4cd0a0ddff1c6ff01c75e28`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# AIReceipt Contract

> `AIReceipt` records the accountable trace boundary for an AI-mediated KFM runtime event: which run used which adapter/model, which input/output digests were bound, which policy decision and citation validation were attached, and which finite outcome was returned. It is a receipt, not model truth.

<p>
  <img alt="Status: proposed" src="https://img.shields.io/badge/status-PROPOSED-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts-blue">
  <img alt="Family: runtime" src="https://img.shields.io/badge/family-runtime-0a7ea4">
  <img alt="Object: AIReceipt" src="https://img.shields.io/badge/object-AIReceipt-blueviolet">
  <img alt="Schema: paired" src="https://img.shields.io/badge/schema-paired-green">
  <img alt="AI: not truth" src="https://img.shields.io/badge/AI-not__truth-critical">
</p>

**Status:** draft / PROPOSED  
**Path:** `contracts/runtime/ai_receipt.md`  
**Paired schema:** `schemas/contracts/v1/runtime/ai_receipt.schema.json`  
**Schema status:** PROPOSED  
**Validator path named by schema:** `tools/validators/validate_ai_receipt.py` — NEEDS VERIFICATION for implementation/wiring  
**Policy authority:** `policy/runtime/` and `policy/ai/`, not this contract  
**Runtime/API authority:** implementation/API roots, not this contract  
**Truth posture:** CONFIRMED schema pairing and required field surface · CONFIRMED finite outcome enum · CONFIRMED governed-AI doctrine says AI is interpretive, downstream of evidence and policy, and must emit an AIReceipt · NEEDS VERIFICATION for validator wiring, fixtures, policy behavior, runtime adapter implementation, citation-validation implementation, receipt persistence, and CI enforcement

## Quick jumps

[Purpose](#purpose) · [Meaning](#meaning) · [Schema-paired field surface](#schema-paired-field-surface) · [Field semantics](#field-semantics) · [Invariants](#invariants) · [Lifecycle role](#lifecycle-role) · [Boundaries](#boundaries) · [Validation expectations](#validation-expectations) · [Fixtures](#fixtures) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

`AIReceipt` is the accountability receipt for an AI-mediated runtime event.

It answers:

- which AI run occurred;
- which adapter and model reference were used;
- which canonicalized input digest was used;
- which canonicalized output digest was produced;
- which policy decision governed the event;
- which citation validation result governed the answer posture;
- whether the event ended as `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`.

It does not answer:

- whether the AI output is true;
- whether the AI output is publishable;
- whether evidence refs resolve;
- whether policy was correct;
- whether citation validation passed unless the referenced validation object says so;
- whether chain-of-thought or private model internals were stored;
- whether the public client may bypass governed runtime/API envelopes.

---

## Meaning

An `AIReceipt` is a trust-spine receipt for an AI step. It makes an AI-mediated response inspectable without turning generated language into authority.

A mature KFM AI flow should be:

```text
scope request
  -> retrieve released/policy-safe evidence
  -> resolve EvidenceRefs/EvidenceBundles
  -> evaluate policy
  -> run adapter/model only within allowed bounds
  -> validate citations / cite-or-abstain
  -> emit finite runtime outcome
  -> emit AIReceipt
  -> emit RuntimeResponseEnvelope for client rendering
```

`AIReceipt` belongs near the runtime trust membrane because it records the accountability boundary around AI interpretation. It should enable audit, replay checks, incident review, and correction/withdrawal linkage without exposing sensitive input content, chain-of-thought, credentials, raw stores, or private model internals.

---

## Schema-paired field surface

The paired schema currently confirms these fields:

| Field | Required | Schema-confirmed shape | Semantic role |
|---|---:|---|---|
| `id` | yes | string matching `^[a-z][a-z0-9_:.-]*$` | Stable receipt identifier. |
| `run_id` | yes | string | Runtime/model-adapter run identifier. |
| `adapter` | yes | string | Adapter or provider abstraction used. |
| `model_ref` | yes | string | Model reference/version/id used by the adapter. |
| `inputs_digest` | yes | string matching `^sha256:[a-f0-9]{64}$` | Digest of canonicalized inputs. |
| `outputs_digest` | yes | string matching `^sha256:[a-f0-9]{64}$` | Digest of canonicalized outputs. |
| `policy_decision_ref` | yes | string | Ref to governing policy decision. |
| `citation_validation_ref` | yes | string | Ref to citation validation result. |
| `outcome` | yes | enum: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | Finite runtime outcome. |

The schema also confirms:

```text
additionalProperties: false
```

---

## Field semantics

### `id`

Stable identifier for the AI receipt.

Requirements:

- must follow the schema pattern;
- should be deterministic or traceable enough for audit;
- should not encode secrets, private prompts, sensitive facts, or chain-of-thought.

PROPOSED convention:

```text
ai_receipt:<surface>:<run-or-digest>
```

### `run_id`

Identifier for the AI runtime event or adapter execution.

A `run_id` should connect the receipt to logs, validation, runtime envelope, and incident review where those exist. It should not expose secret infrastructure identifiers if the receipt is public-facing.

### `adapter`

Provider-neutral adapter identifier.

The adapter is the governed interface between KFM and an AI model/provider/runtime. It is not the model itself, not a policy authority, and not evidence authority.

### `model_ref`

Reference to the model used.

A model reference should be specific enough for audit, such as provider/model/version/profile where policy allows. It should not be used to infer truth or authority.

### `inputs_digest`

Digest of canonicalized AI input material.

This should bind the run to the actual bounded input set without storing sensitive payloads in the receipt. The schema requires a SHA-256 digest string.

### `outputs_digest`

Digest of canonicalized AI output material.

This supports audit and tamper detection. It does not make the output true, reviewed, released, or policy-safe by itself.

### `policy_decision_ref`

Reference to the policy decision governing the AI event.

The referenced policy decision must be resolvable for trust-bearing use. Missing or unresolved policy context should fail closed.

### `citation_validation_ref`

Reference to citation validation for AI output.

The citation-validation object/report owns whether the answer is sufficiently cited. The receipt only records the link.

### `outcome`

Finite AI/runtime outcome.

| Outcome | Meaning |
|---|---|
| `ANSWER` | AI output was allowed to proceed under policy/citation/runtime constraints. |
| `ABSTAIN` | AI declined because evidence, citation, rights, sensitivity, freshness, or policy conditions were insufficient or unsafe. |
| `DENY` | AI output or access/rendering was denied by policy. |
| `ERROR` | The AI runtime path failed safely or could not produce a valid governed result. |

---

## Invariants

CONFIRMED by paired schema:

- `id`, `run_id`, `adapter`, `model_ref`, `inputs_digest`, `outputs_digest`, `policy_decision_ref`, `citation_validation_ref`, and `outcome` are required.
- `id` must match `^[a-z][a-z0-9_:.-]*$`.
- `inputs_digest` and `outputs_digest` must match `^sha256:[a-f0-9]{64}$`.
- `outcome` must be one of `ANSWER | ABSTAIN | DENY | ERROR`.
- Additional properties are not allowed.

PROPOSED semantic invariants:

- AIReceipt must not store raw prompts, raw retrieved evidence, sensitive input text, credentials, or chain-of-thought.
- AIReceipt must not be treated as evidence truth; EvidenceBundle and citation validation remain separate authorities.
- `outcome=ANSWER` requires a resolvable policy decision and citation validation ref.
- `ABSTAIN`, `DENY`, and `ERROR` should be first-class outcomes, not exceptions hidden from audit.
- Inputs and outputs must be digest-bound in a stable canonicalization profile before the receipt is relied on.
- A public runtime response should not expose an AI-generated answer unless its AIReceipt, policy posture, citation validation, and runtime envelope permit display.
- Corrections, withdrawals, or stale evidence should supersede or invalidate affected AI receipts without mutating history silently.

---

## Lifecycle role

`AIReceipt` is created when AI participates in a governed runtime path.

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

AI should normally operate downstream of released or policy-safe evidence. The receipt records the AI step; it does not promote data through the lifecycle.

| Lifecycle point | Role of AIReceipt |
|---|---|
| WORK/CANDIDATE review | May record internal AI assistance, but not public truth. |
| CATALOG/TRIPLET runtime query | Records AI interpretation over governed evidence/context. |
| Public runtime response | Supports RuntimeResponseEnvelope accountability. |
| Correction/withdrawal | Affected receipts may be superseded/invalidated by correction posture. |
| Audit/incident review | Provides digest/model/policy/citation hooks for investigation. |

---

## Boundaries

| Boundary | Rule |
|---|---|
| AIReceipt vs EvidenceBundle | AIReceipt records AI run accountability; EvidenceBundle supports factual claims. |
| AIReceipt vs PolicyDecision | AIReceipt references policy decision; it does not decide policy. |
| AIReceipt vs CitationValidationReport | AIReceipt references citation validation; it does not validate citations itself. |
| AIReceipt vs RuntimeResponseEnvelope | AIReceipt is audit receipt; RuntimeResponseEnvelope is client-facing response envelope. |
| AIReceipt vs model output | Output digest binds content; receipt does not make generated content authoritative. |
| AIReceipt vs chain-of-thought | Chain-of-thought is not stored as evidence in this contract. |
| AIReceipt vs release | AIReceipt does not publish or promote artifacts. |
| AIReceipt vs runtime implementation | Runtime adapters and API behavior live outside contracts. |

---

## Validation expectations

NEEDS VERIFICATION in implementation:

- validator existence and wiring for `tools/validators/validate_ai_receipt.py`;
- fixture coverage under `fixtures/contracts/v1/runtime/ai_receipt/`;
- canonicalization rules for input/output digests;
- policy decision reference resolution;
- citation validation reference resolution;
- runtime adapter run-id linkage;
- correction/withdrawal invalidation behavior;
- public API/UI tests proving AIReceipt is not treated as truth or publication authority;
- tests proving chain-of-thought, secrets, raw evidence, and sensitive details are not stored in receipts.

---

## Fixtures

Minimum fixture set PROPOSED:

| Fixture | Purpose |
|---|---|
| `valid_answer.json` | Valid AI receipt with answer outcome and required refs/digests. |
| `valid_abstain_missing_evidence.json` | Valid abstention with policy/citation linkage. |
| `valid_deny_sensitive.json` | Valid denial due to sensitivity or access policy. |
| `valid_error_adapter_failure.json` | Valid safe error outcome. |
| `invalid_missing_policy_decision_ref.json` | Confirms required policy ref. |
| `invalid_missing_citation_validation_ref.json` | Confirms required citation-validation ref. |
| `invalid_bad_input_digest.json` | Confirms SHA-256 digest pattern. |
| `invalid_unknown_outcome.json` | Confirms finite outcome enum. |
| `invalid_extra_property_chain_of_thought.json` | Confirms additional properties are blocked and chain-of-thought is not stored. |

Fixtures must use synthetic/safe refs only.

---

## Open questions

- Should the schema include a canonicalization profile field for digest reproducibility?
- Should `policy_decision_ref` point to runtime `DecisionEnvelope`, `PolicyDecision`, or both?
- Should `citation_validation_ref` resolve to a dedicated contract under `contracts/citation/` or another accepted root?
- Should AIReceipt include redaction profile, sensitivity label, or capability policy refs, or should those remain reachable through policy decision refs?
- Which runtime root stores persisted AIReceipt instances?

---

## Rollback

Rollback is required if this contract is used to treat AI output as truth, store prompts/secrets/chain-of-thought, bypass evidence/policy/citation validation, publish content, replace RuntimeResponseEnvelope, or authorize public API/UI/map/AI behavior directly.

Rollback target for this expansion: previous blob SHA `985aff8caf79ed98a4cd0a0ddff1c6ff01c75e28`.

<p align="right"><a href="#top">Back to top</a></p>
