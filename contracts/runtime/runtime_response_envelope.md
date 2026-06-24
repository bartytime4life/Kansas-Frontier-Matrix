<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-runtime-runtime-response-envelope
title: contracts/runtime/runtime_response_envelope.md — RuntimeResponseEnvelope Contract
type: contract
version: v0.2
status: draft; PROPOSED; schema-paired; api-facing-runtime-envelope; trust-membrane
owners: OWNER_TBD — Runtime steward · API steward · Contracts steward · Schema steward · Policy steward · Evidence steward · Correction steward · Docs steward
created: NEEDS VERIFICATION — file existed before v0.2 expansion
updated: 2026-06-24
policy_label: public; contracts; runtime; runtime-response-envelope; api-facing; finite-outcomes; evidence-refs; policy-state; freshness; correction-state; governed-runtime; no-internal-store-bypass
tags: [kfm, contracts, runtime, runtime-response-envelope, governed-api, trust-membrane, answer, abstain, deny, error, evidence-refs, policy-state, freshness, correction-state, cite-or-abstain]
related:
  - ./README.md
  - ./decision_envelope.md
  - ./run_receipt.md
  - ./ai_receipt.md
  - ../policy/policy_decision.md
  - ../evidence/evidence_bundle.md
  - ../release/release_manifest.md
  - ../release/withdrawal_notice.md
  - ../release/rollback_card.md
  - ../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
  - ../../schemas/contracts/v1/evidence/evidence_ref.schema.json
  - ../../policy/runtime/
  - ../../fixtures/contracts/v1/runtime/runtime_response_envelope/
  - ../../tools/validators/validate_runtime_response_envelope.py
  - ../../docs/architecture/contract-schema-policy-split.md
  - ../../docs/architecture/governed-ai.md
notes:
  - "Expanded from existing `contracts/runtime/runtime_response_envelope.md`."
  - "Paired schema verified at `schemas/contracts/v1/runtime/runtime_response_envelope.schema.json`; schema status is PROPOSED."
  - "The schema requires id, spec_hash, version, issued_at, outcome, reason_code, evidence_refs, policy_state, freshness, and correction_state; additional properties are false."
  - "RuntimeResponseEnvelope is the governed API/client-facing response envelope. It is not raw evidence storage, not canonical lifecycle storage, not policy execution, not model truth, and not release approval."
  - "Rollback target for this expansion is previous blob SHA `070e7f178f04bd1cf7577de1046aa3eaa3530edc`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# RuntimeResponseEnvelope Contract

> `RuntimeResponseEnvelope` is the governed API-facing response object that tells a client what finite outcome it may render, which evidence refs support the response posture, what policy/freshness/correction state applies, and which contract/spec lineage produced the envelope. It is a trust-membrane envelope, not raw evidence, not canonical storage, and not public truth by itself.

<p>
  <img alt="Status: proposed" src="https://img.shields.io/badge/status-PROPOSED-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts-blue">
  <img alt="Family: runtime" src="https://img.shields.io/badge/family-runtime-0a7ea4">
  <img alt="Object: RuntimeResponseEnvelope" src="https://img.shields.io/badge/object-RuntimeResponseEnvelope-blueviolet">
  <img alt="Schema: paired" src="https://img.shields.io/badge/schema-paired-green">
  <img alt="Client: governed" src="https://img.shields.io/badge/client-governed-critical">
</p>

**Status:** draft / PROPOSED  
**Path:** `contracts/runtime/runtime_response_envelope.md`  
**Paired schema:** `schemas/contracts/v1/runtime/runtime_response_envelope.schema.json`  
**Schema status:** PROPOSED  
**Validator path named by schema:** `tools/validators/validate_runtime_response_envelope.py` — existing file previously marked wired in this document; current implementation wiring still NEEDS VERIFICATION unless checked in this session  
**Policy authority:** `policy/runtime/`, not this contract  
**Runtime/API authority:** implementation/API roots, not this contract  
**Truth posture:** CONFIRMED schema pairing and required field surface · CONFIRMED finite outcome enum · CONFIRMED evidence refs use the EvidenceRef schema · CONFIRMED additional properties are closed · NEEDS VERIFICATION for validator wiring, fixtures, policy-state/freshness/correction-state vocabularies, public-client tests, and runtime implementation

## Quick jumps

[Purpose](#purpose) · [Meaning](#meaning) · [Schema-paired field surface](#schema-paired-field-surface) · [Field semantics](#field-semantics) · [Outcome semantics](#outcome-semantics) · [State semantics](#state-semantics) · [Invariants](#invariants) · [Lifecycle role](#lifecycle-role) · [Boundaries](#boundaries) · [Validation expectations](#validation-expectations) · [Fixtures](#fixtures) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

`RuntimeResponseEnvelope` is the client-facing runtime envelope for governed KFM responses.

It answers:

- which runtime response envelope was issued;
- which contract/spec version produced it;
- when it was issued;
- whether the client receives `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`;
- why that outcome was selected at a safe high level;
- which evidence refs are attached;
- what policy state applies;
- whether the response is fresh or stale;
- whether correction, withdrawal, or supersession posture affects the response.

It does not answer:

- whether raw evidence can be read directly;
- whether canonical/internal stores can be exposed;
- whether the evidence refs actually resolve unless resolution is performed;
- whether policy evaluation was correct;
- whether AI output is true;
- whether a release is approved;
- whether client rendering is safe if obligations are ignored.

---

## Meaning

A `RuntimeResponseEnvelope` is the trust membrane object between governed backend state and downstream clients.

A mature governed runtime response flow should look like:

```text
request/context
  -> resolve released or policy-safe state
  -> evaluate policy and sensitivity
  -> resolve evidence refs or abstain
  -> account for freshness/correction/withdrawal
  -> produce DecisionEnvelope / PolicyDecision / AIReceipt as applicable
  -> emit RuntimeResponseEnvelope
  -> client renders only what the envelope permits
```

The envelope is not the payload store. It carries the governance posture needed for safe display and traceability.

---

## Schema-paired field surface

The paired schema currently confirms these fields:

| Field | Required | Schema-confirmed shape | Semantic role |
|---|---:|---|---|
| `id` | yes | string matching `^[a-z][a-z0-9_:.-]*$` | Stable response-envelope identifier. |
| `spec_hash` | yes | string matching `^sha256:[a-f0-9]{64}$` | Contract/spec lineage hash. |
| `version` | yes | string | Envelope version token. |
| `issued_at` | yes | date-time string | Emission timestamp. |
| `outcome` | yes | enum: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | Finite runtime response outcome. |
| `reason_code` | yes | string | Primary reason classification. |
| `evidence_refs` | yes | array of EvidenceRef objects | Evidence pointers attached to response posture. |
| `policy_state` | yes | string | Policy state summary. |
| `freshness` | yes | string | Freshness/staleness posture. |
| `correction_state` | yes | string | Correction/withdrawal/supersession posture. |

The schema also confirms:

```text
additionalProperties: false
```

---

## Field semantics

### `id`

Stable identifier for one runtime response envelope.

Requirements:

- must follow the schema pattern;
- should support traceability, correction, replay detection, and client reconciliation;
- must not encode secrets, private prompts, sensitive exact-location values, or credentials.

PROPOSED convention:

```text
resp:<surface>:<date-or-run>:<suffix>
```

### `spec_hash`

SHA-256 hash binding the envelope to a contract/spec/config lineage.

The hash guards against serving responses from mismatched contract baselines. It is an integrity hook, not proof of truth.

### `version`

Envelope version token.

Use for client compatibility, migration, deprecation, and schema negotiation.

### `issued_at`

Timestamp when the envelope was emitted.

The schema requires date-time format. Do not rewrite this value to make stale responses appear current.

### `outcome`

Finite client-facing runtime outcome.

The outcome directly gates client behavior. Clients must not treat missing or unknown outcomes as success.

### `reason_code`

Primary reason classification for the outcome.

Reason codes should be safe to expose and should avoid leaking sensitive details, hidden source content, raw evidence, precise protected locations, private data, credentials, or chain-of-thought.

### `evidence_refs`

Evidence references attached to the response posture.

The schema makes `evidence_refs` required and uses the EvidenceRef schema for each item. Refs are not evidence closure unless they resolve to admissible evidence bundles or evidence records through governed interfaces.

### `policy_state`

Policy state summary for the response.

This may summarize whether a response is allowed, restricted, withheld, obligated, or denied. A controlled vocabulary is NEEDS VERIFICATION.

### `freshness`

Freshness/staleness posture for the response.

This should tell clients whether the response is current enough for the use case, stale, degraded, awaiting refresh, or time-limited. A controlled vocabulary is NEEDS VERIFICATION.

### `correction_state`

Correction, supersession, withdrawal, rollback, or stale-publication posture.

This tells clients whether the response lineage is normal, corrected, superseded, withdrawn, rollback-affected, or otherwise constrained. A controlled vocabulary is NEEDS VERIFICATION.

---

## Outcome semantics

| Outcome | Runtime response meaning | Client posture |
|---|---|---|
| `ANSWER` | The system may present the requested response under current evidence, policy, rights, sensitivity, freshness, correction, and release constraints. | Render only with required evidence refs, notices, and obligations. |
| `ABSTAIN` | The system refuses to answer because evidence, citation, rights, sensitivity, freshness, correction state, or context is insufficient or unsafe. | Show safe abstention reason; do not infer the answer. |
| `DENY` | Access, render, export, capability, consent, or sensitivity policy blocks response delivery. | Do not render restricted payload; show safe denial. |
| `ERROR` | Runtime could not complete safely or deterministically. | Show safe error; do not infer truth, permission, or availability. |

`ABSTAIN`, `DENY`, and `ERROR` are first-class governed outcomes.

---

## State semantics

### `policy_state`

PROPOSED examples:

- `allow`
- `allow_with_obligations`
- `restricted`
- `withheld`
- `deny`
- `needs_review`
- `unknown_fail_closed`

### `freshness`

PROPOSED examples:

- `fresh`
- `stale`
- `degraded`
- `pending_refresh`
- `time_limited`
- `unknown_fail_closed`

### `correction_state`

PROPOSED examples:

- `none`
- `corrected`
- `superseded`
- `withdrawn`
- `rollback_affected`
- `under_review`
- `unknown_fail_closed`

These vocabularies are semantic recommendations only until schemas, policy registers, fixtures, and client tests enforce them.

---

## Invariants

CONFIRMED by paired schema:

- `id`, `spec_hash`, `version`, `issued_at`, `outcome`, `reason_code`, `evidence_refs`, `policy_state`, `freshness`, and `correction_state` are required.
- `id` must match `^[a-z][a-z0-9_:.-]*$`.
- `spec_hash` must match `^sha256:[a-f0-9]{64}$`.
- `issued_at` must be a date-time string.
- `outcome` must be one of `ANSWER | ABSTAIN | DENY | ERROR`.
- `evidence_refs` items must match the EvidenceRef schema ref declared by the runtime schema.
- Additional properties are not allowed.

PROPOSED semantic invariants:

- `ANSWER` should include at least one resolvable evidence ref unless the response is explicitly non-claim or policy-exempt.
- `ABSTAIN`, `DENY`, and `ERROR` must not leak restricted details through `reason_code` or state fields.
- Public clients must not render payloads when outcome is `DENY` or `ERROR`.
- Public clients must not manufacture answers when outcome is `ABSTAIN`.
- Correction/withdrawal/supersession state must override stale client assumptions.
- Runtime responses must not imply direct access to RAW, WORK, QUARANTINE, unpublished candidate, canonical/internal, graph/vector, direct source-system, or direct model-runtime stores.
- The envelope should be superseded rather than silently mutated when correction/freshness/policy posture changes.

---

## Lifecycle role

`RuntimeResponseEnvelope` is emitted at the trust membrane for governed client-facing responses.

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Typical roles:

| Lifecycle / runtime point | Role of RuntimeResponseEnvelope |
|---|---|
| Runtime query | Carries finite outcome and safe display posture. |
| Evidence-backed answer | Carries evidence refs and cite-or-abstain posture. |
| Policy denial | Carries safe denial state without leaking restricted content. |
| Stale or corrected content | Carries freshness/correction state to clients. |
| AI-mediated answer | May be paired with AIReceipt and citation validation. |
| Map/UI/API rendering | Tells public/restricted clients what can be rendered and with what obligations. |

---

## Boundaries

| Boundary | Rule |
|---|---|
| RuntimeResponseEnvelope vs DecisionEnvelope | DecisionEnvelope records finite decision context; RuntimeResponseEnvelope is the client-facing response envelope. |
| RuntimeResponseEnvelope vs AIReceipt | AIReceipt records AI run accountability; RuntimeResponseEnvelope tells client rendering posture. |
| RuntimeResponseEnvelope vs PolicyDecision | PolicyDecision records policy evaluation; RuntimeResponseEnvelope carries client-safe policy state. |
| RuntimeResponseEnvelope vs EvidenceBundle | EvidenceBundle supports claims; envelope carries EvidenceRefs only. |
| RuntimeResponseEnvelope vs ReleaseManifest | ReleaseManifest binds released artifacts; envelope references/reflects release-safe state. |
| RuntimeResponseEnvelope vs runtime code | Envelope defines meaning; code executes elsewhere. |
| RuntimeResponseEnvelope vs UI/map/API | Envelope informs downstream rendering; clients must still honor policy/obligations. |

---

## Validation expectations

NEEDS VERIFICATION in implementation:

- validator existence and current wiring for `tools/validators/validate_runtime_response_envelope.py`;
- fixture coverage under `fixtures/contracts/v1/runtime/runtime_response_envelope/`;
- controlled vocabularies for `policy_state`, `freshness`, and `correction_state`;
- required non-empty evidence refs for public `ANSWER` cases, if adopted;
- safe reason-code vocabulary;
- public client tests for `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` behavior;
- tests proving no public client reads RAW/WORK/QUARANTINE/canonical/internal stores;
- correction/withdrawal/rollback propagation through runtime envelopes;
- AIReceipt and citation-validation linkage where AI produces or shapes the response.

---

## Fixtures

Minimum fixture set PROPOSED:

| Fixture | Purpose |
|---|---|
| `valid_answer_with_evidence.json` | Valid answer with evidence refs and allow policy state. |
| `valid_abstain_no_evidence.json` | Valid abstention when evidence is insufficient. |
| `valid_deny_sensitive.json` | Valid denial due to sensitivity/access policy. |
| `valid_error_safe.json` | Valid safe runtime error envelope. |
| `valid_stale_corrected.json` | Valid stale/corrected response posture. |
| `valid_withdrawn.json` | Valid withdrawn/correction-state envelope. |
| `invalid_missing_spec_hash.json` | Confirms required spec hash. |
| `invalid_bad_spec_hash.json` | Confirms SHA-256 pattern. |
| `invalid_unknown_outcome.json` | Confirms finite outcome enum. |
| `invalid_extra_property.json` | Confirms additional properties are closed. |

Fixtures must use synthetic/safe refs only.

---

## Open questions

- What is the accepted vocabulary for `policy_state`, `freshness`, and `correction_state`?
- Should `evidence_refs` be required non-empty for every `ANSWER`?
- Should the schema include explicit `obligations`, or should obligations remain in DecisionEnvelope/PolicyDecision and be summarized by policy_state?
- Should AI-mediated responses require an `ai_receipt_ref` field in a future version?
- How should release/correction/withdrawal refs be represented without overloading `correction_state`?

---

## Rollback

Rollback is required if this contract is used as raw evidence storage, canonical lifecycle storage, executable runtime/API code, policy authority, AI truth, release approval, or permission for public clients to bypass governed interfaces.

Rollback target for this expansion: previous blob SHA `070e7f178f04bd1cf7577de1046aa3eaa3530edc`.

<p align="right"><a href="#top">Back to top</a></p>
