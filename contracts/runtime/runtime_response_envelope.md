<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-runtime-runtime-response-envelope
title: contracts/runtime/runtime_response_envelope.md — RuntimeResponseEnvelope Contract
type: contract
version: v0.4
status: draft; PROPOSED; schema-paired; api-facing-runtime-envelope; trust-membrane
owners: OWNER_TBD — Runtime steward · API steward · Contracts steward · Schema steward · Policy steward · Evidence steward · Correction steward · Docs steward
created: NEEDS VERIFICATION — file existed before v0.2 expansion
updated: 2026-08-14
policy_label: public; contracts; runtime; runtime-response-envelope; api-facing; finite-outcomes; evidence-refs; precision-disclosure; policy-state; freshness; correction-state; governed-runtime; no-internal-store-bypass
tags: [kfm, contracts, runtime, runtime-response-envelope, governed-api, trust-membrane, answer, abstain, deny, error, evidence-refs, precision-actually-used, precision-disclosure, policy-state, freshness, correction-state, cite-or-abstain]
related:
  - ./README.md
  - ./decision_envelope.md
  - ./run_receipt.md
  - ./ai_receipt.md
  - ./precision_actually_used.md
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
  - ../../tests/contracts/test_runtime_response_contract_alignment.py
  - ../../tests/runtime_proof/test_envelope_finite_outcomes.py
  - ../../docs/architecture/contract-schema-policy-split.md
  - ../../docs/architecture/governed-ai/README.md
notes:
  - "Expanded from existing `contracts/runtime/runtime_response_envelope.md`."
  - "Paired schema verified at `schemas/contracts/v1/runtime/runtime_response_envelope.schema.json`; schema status is PROPOSED."
  - "The schema has ten unconditional required fields and conditionally requires `precision_actually_used` plus at least one top-level EvidenceRef for `ANSWER`; it forbids precision disclosure for the other three outcomes."
  - "The structured precision semantics are owned by `contracts/runtime/precision_actually_used.md` and are implemented consistently by the schema, fixture, validator, candidate builder, and bounded proof tests."
  - "v0.4 repairs the v0.3 prose omission without changing schema bytes, runtime behavior, provider/model integration, policy, release, deployment, or publication posture."
  - "RuntimeResponseEnvelope is the governed API/client-facing response envelope. It is not raw evidence storage, not canonical lifecycle storage, not policy execution, not model truth, and not release approval."
  - "Rollback target for this correction is prior contract blob SHA `97ff95ba5527968f3db70cd710682176444e4cde`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# RuntimeResponseEnvelope Contract

> `RuntimeResponseEnvelope` is the governed API-facing response object that tells a client what finite outcome it may render, which evidence refs support the response posture, what precision was actually supported for an answer, what policy/freshness/correction state applies, and which contract/spec lineage produced the envelope. It is a trust-membrane envelope, not raw evidence, not canonical storage, and not public truth by itself.

<p>
  <img alt="Status: proposed" src="https://img.shields.io/badge/status-PROPOSED-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts-blue">
  <img alt="Family: runtime" src="https://img.shields.io/badge/family-runtime-0a7ea4">
  <img alt="Object: RuntimeResponseEnvelope" src="https://img.shields.io/badge/object-RuntimeResponseEnvelope-blueviolet">
  <img alt="Schema: paired" src="https://img.shields.io/badge/schema-paired-green">
  <img alt="Precision: answer-only" src="https://img.shields.io/badge/precision-ANSWER--only-0a7ea4">
  <img alt="Client: governed" src="https://img.shields.io/badge/client-governed-critical">
</p>

**Status:** draft / PROPOSED  
**Path:** `contracts/runtime/runtime_response_envelope.md`  
**Paired schema:** `schemas/contracts/v1/runtime/runtime_response_envelope.schema.json`  
**Precision semantics:** [`contracts/runtime/precision_actually_used.md`](./precision_actually_used.md)  
**Schema status:** PROPOSED  
**Validator path named by schema:** `tools/validators/validate_runtime_response_envelope.py` — wired to the canonical schema and its positive/negative fixture root  
**Policy authority:** `policy/runtime/`, not this contract  
**Runtime/API authority:** implementation/API roots, not this contract  
**Truth posture:** CONFIRMED schema pairing, precision-profile pairing, validator wiring, four-outcome schema fixtures, conditional `ANSWER` precision disclosure, EvidenceRef shape reference, and closed additional properties · NEEDS VERIFICATION for policy-state/freshness/correction-state vocabularies, semantic outcome selection, evidence resolution, public-client behavior, and governed runtime/API integration

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
- for `ANSWER`, which spatial, temporal, and attribute precision was actually supported and disclosed;
- what policy state applies;
- whether the response is fresh or stale;
- whether correction, withdrawal, or supersession posture affects the response.

It does not answer:

- whether raw evidence can be read directly;
- whether canonical/internal stores can be exposed;
- whether the evidence refs actually resolve unless resolution is performed;
- whether disclosed precision is fit for a use case, policy-approved, release-approved, or stronger than its cited evidence;
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
  -> determine evidence-supported precision
  -> account for freshness/correction/withdrawal
  -> produce DecisionEnvelope / PolicyDecision / AIReceipt as applicable
  -> emit RuntimeResponseEnvelope
  -> client renders only what the envelope permits
```

The envelope is not the payload store. It carries the governance posture needed for safe display and traceability. Requested resolution, map zoom, formatting precision, or model confidence must not be substituted for the evidence-supported precision actually used.

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
| `evidence_refs` | yes; at least one item for `ANSWER` | array of EvidenceRef objects | Evidence pointers attached to response posture and the support set for answer precision. |
| `policy_state` | yes | string | Policy state summary. |
| `freshness` | yes | string | Freshness/staleness posture. |
| `correction_state` | yes | string | Correction/withdrawal/supersession posture. |
| `precision_actually_used` | conditional — required for `ANSWER`; forbidden otherwise | closed object with required `spatial`, `temporal`, `attribute`, `evidence_refs`, and `transform_receipt_refs`; optional `requested_precision` | Evidence-supported precision disclosed for an answer. |

The schema also confirms:

```text
additionalProperties: false
```

Conditional shape rules are part of the same canonical schema, not a separate response profile:

| Condition | Machine rule |
|---|---|
| `outcome == ANSWER` | `evidence_refs` has at least one item and `precision_actually_used` is required. |
| `outcome != ANSWER` | `precision_actually_used` is forbidden. |

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

The schema makes `evidence_refs` required and uses the EvidenceRef schema for each item. It requires at least one item for `ANSWER`. Refs are not evidence closure unless they resolve to admissible evidence bundles or evidence records through governed interfaces.

### `precision_actually_used`

Structured disclosure of the precision actually supported by the evidence used for an `ANSWER`.

The canonical semantic profile is [`precision_actually_used.md`](./precision_actually_used.md). The profile is required only for `ANSWER` and forbidden for `ABSTAIN`, `DENY`, and `ERROR`; it does not create a second RuntimeResponseEnvelope shape.

| Nested field | Required | Meaning |
|---|---:|---|
| `spatial` | yes | Representation, resolution, accuracy statement, and whether outward generalization was applied. |
| `temporal` | yes | Granularity, supported observation interval, and freshness class. |
| `attribute` | yes | Measure, unit, significant precision, and optional classification granularity. |
| `requested_precision` | no | Optional record of requested spatial, temporal, or attribute precision for an explicit requested-versus-actual comparison. |
| `evidence_refs` | yes; nonempty | EvidenceRefs supporting the precision disclosure; every item must also occur in the envelope's top-level `evidence_refs`. |
| `transform_receipt_refs` | yes; may be empty only when no generalization requires a receipt | Transform receipts supporting outward generalization or related precision-changing operations. |

Actual precision controls the response. Requested precision, map zoom, formatting, or model confidence cannot upgrade it. A precision disclosure is not a quality score, policy decision, source-authority decision, fitness-for-use determination, release approval, or publication authority.

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

| Outcome | Runtime response meaning | Precision posture | Client posture |
|---|---|---|---|
| `ANSWER` | The system may present the requested response under current evidence, policy, rights, sensitivity, freshness, correction, and release constraints. | Required. Disclose only the spatial, temporal, and attribute precision actually supported by the bound evidence. | Render only with required evidence refs, notices, and obligations. |
| `ABSTAIN` | The system refuses to answer because evidence, citation, rights, sensitivity, freshness, correction state, or context is insufficient or unsafe. | Forbidden. Negative outcomes must not carry an answer-shaped precision disclosure. | Show safe abstention reason; do not infer the answer. |
| `DENY` | Access, render, export, capability, consent, or sensitivity policy blocks response delivery. | Forbidden. | Do not render restricted payload; show safe denial. |
| `ERROR` | Runtime could not complete safely or deterministically. | Forbidden. | Show safe error; do not infer truth, permission, or availability. |

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

CONFIRMED by the paired schema:

- `id`, `spec_hash`, `version`, `issued_at`, `outcome`, `reason_code`, `evidence_refs`, `policy_state`, `freshness`, and `correction_state` are unconditionally required.
- `id` must match `^[a-z][a-z0-9_:.-]*$`.
- `spec_hash` must match `^sha256:[a-f0-9]{64}$`.
- `issued_at` must be a date-time string.
- `outcome` must be one of `ANSWER | ABSTAIN | DENY | ERROR`.
- `evidence_refs` items must match the EvidenceRef schema ref declared by the runtime schema.
- Every `ANSWER` requires at least one top-level EvidenceRef and a closed `precision_actually_used` object.
- `ABSTAIN`, `DENY`, and `ERROR` forbid `precision_actually_used`.
- The precision object requires `spatial`, `temporal`, `attribute`, `evidence_refs`, and `transform_receipt_refs`; `requested_precision` is optional.
- `spatial`, `temporal`, and `attribute` are closed objects with the fields defined by the paired precision profile.
- `attribute.significant_precision` is an integer from `0` through `12`.
- Additional properties are not allowed at the envelope level or within the precision sub-objects.

CONFIRMED by the precision profile, validator, candidate builder, and focused proofs:

- precision-level `evidence_refs` must be nonempty and must be a subset of the envelope's top-level `evidence_refs`;
- `spatial.generalization_applied: true` requires at least one `transform_receipt_refs` item;
- `temporal.observation_interval.start` must not be after `end`;
- optional `requested_precision` is informative only; actual precision remains controlling;
- builders and selectors must preserve the structured disclosure without inventing evidence, precision, policy, or authority.

PROPOSED runtime and client invariants:

- a schema-valid EvidenceRef must resolve to admissible support before an `ANSWER` is authorized;
- `ABSTAIN`, `DENY`, and `ERROR` must not leak restricted details through `reason_code` or state fields;
- public clients must not render payloads when outcome is `DENY` or `ERROR`;
- public clients must not manufacture answers when outcome is `ABSTAIN`;
- correction/withdrawal/supersession state must override stale client assumptions;
- runtime responses must not imply direct access to RAW, WORK, QUARANTINE, unpublished candidate, canonical/internal, graph/vector, direct source-system, or direct model-runtime stores;
- the envelope should be superseded rather than silently mutated when correction/freshness/policy posture changes.

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
| Evidence-backed answer | Carries evidence refs, evidence-supported precision, and cite-or-abstain posture. |
| Policy denial | Carries safe denial state without leaking restricted content. |
| Stale or corrected content | Carries freshness/correction state to clients. |
| AI-mediated answer | May be paired with AIReceipt and citation validation. |
| Map/UI/API rendering | Tells public/restricted clients what can be rendered and with what obligations. |

---

## Boundaries

| Boundary | Rule |
|---|---|
| RuntimeResponseEnvelope vs PrecisionActuallyUsed | RuntimeResponseEnvelope carries the answer-only field; [`precision_actually_used.md`](./precision_actually_used.md) owns its structured semantic profile. |
| RuntimeResponseEnvelope vs DecisionEnvelope | DecisionEnvelope records finite decision context; RuntimeResponseEnvelope is the client-facing response envelope. |
| RuntimeResponseEnvelope vs AIReceipt | AIReceipt records AI run accountability; RuntimeResponseEnvelope tells client rendering posture. |
| RuntimeResponseEnvelope vs PolicyDecision | PolicyDecision records policy evaluation; RuntimeResponseEnvelope carries client-safe policy state. |
| RuntimeResponseEnvelope vs EvidenceBundle | EvidenceBundle supports claims and precision; the envelope carries EvidenceRefs only. |
| RuntimeResponseEnvelope vs ReleaseManifest | ReleaseManifest binds released artifacts; envelope references/reflects release-safe state. |
| RuntimeResponseEnvelope vs runtime code | Envelope defines meaning; code executes elsewhere. |
| RuntimeResponseEnvelope vs UI/map/API | Envelope informs downstream rendering; clients must still honor policy/obligations. |

---

## Validation expectations

CONFIRMED contract/schema/fixture validation surface:

- `tools/validators/validate_runtime_response_envelope.py` targets the canonical schema and fixture root;
- valid synthetic fixtures cover `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`;
- the valid `ANSWER` fixture carries nonempty top-level EvidenceRefs and the structured precision profile;
- invalid fixtures cover a missing required field, an extra property, an invalid identifier, and an unknown outcome;
- the validator additionally fails closed on precision EvidenceRefs outside the top-level support set, generalized precision without a transform receipt, and inverted temporal intervals;
- `tests/runtime_proof/test_envelope_finite_outcomes.py` checks the closed profile and Focus compatibility alias without network access;
- `tests/packages/envelopes/test_runtime_response_candidate.py` proves the candidate builder emits the selected representation for `ANSWER` and forbids it for negative outcomes;
- `tests/contracts/test_runtime_response_contract_alignment.py` checks that this contract documents every top-level schema property, points to the schema-selected precision profile, and preserves the schema's conditional outcome law.

NEEDS VERIFICATION in runtime and client implementation:

- controlled vocabularies for `policy_state`, `freshness`, and `correction_state`;
- safe reason-code vocabulary;
- resolution of every `ANSWER` EvidenceRef to admissible support;
- calculation of precision from governed evidence rather than caller assertion;
- public client tests for `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` behavior;
- client rendering of requested-versus-actual precision without overstatement;
- tests proving no public client reads RAW/WORK/QUARANTINE/canonical/internal stores;
- correction/withdrawal/rollback propagation through runtime envelopes;
- AIReceipt and citation-validation linkage where AI produces or shapes the response.

---

## Fixtures

Current synthetic schema fixtures:

| Fixture | Purpose |
|---|---|
| `valid/valid_1.json` | Shape-valid `ABSTAIN` with no evidence refs and no precision disclosure. |
| `valid/valid_2.json` | Shape-valid `ANSWER` with one synthetic EvidenceRef and structured requested-versus-actual precision disclosure. |
| `valid/valid_3.json` | Shape-valid `DENY` without a restricted payload or precision disclosure. |
| `valid/valid_4.json` | Shape-valid safe `ERROR` without internal diagnostics or precision disclosure. |
| `invalid/invalid_1.json` | Missing required `id`. |
| `invalid/invalid_2.json` | Disallowed extra property. |
| `invalid/invalid_3.json` | Identifier pattern violation. |
| `invalid/invalid_4.json` | Unknown outcome outside the finite enum. |

Focused tests derive additional invalid precision cases from the valid `ANSWER` fixture so the canonical fixture family remains small and deterministic.

Additional semantic/runtime fixture set PROPOSED:

| Fixture | Purpose |
|---|---|
| `valid_stale_corrected.json` | Valid stale/corrected response posture. |
| `valid_withdrawn.json` | Valid withdrawn/correction-state envelope. |
| `invalid_missing_spec_hash.json` | Confirms required spec hash. |
| `invalid_bad_spec_hash.json` | Confirms SHA-256 pattern. |

Fixtures must use synthetic/safe refs only.

---

## Open questions

- What is the accepted vocabulary for `policy_state`, `freshness`, and `correction_state`?
- Which governed component calculates the precision profile from resolved evidence, and which component independently verifies it?
- How should public clients render requested-versus-actual precision and transform lineage without overstating fitness for use?
- Should the schema include explicit `obligations`, or should obligations remain in DecisionEnvelope/PolicyDecision and be summarized by `policy_state`?
- Should AI-mediated responses require an `ai_receipt_ref` field in a future version?
- How should release/correction/withdrawal refs be represented without overloading `correction_state`?

---

## Rollback

This v0.4 correction aligns contract prose with the existing schema-selected precision representation and adds no runtime, API, provider/model, policy, release, deployment, or publication behavior.

Rollback is required if the contract again omits or contradicts the canonical conditional precision shape, if the alignment test becomes a shadow schema instead of an enforceability check, or if this contract is used as raw evidence storage, canonical lifecycle storage, executable runtime/API code, policy authority, AI truth, release approval, or permission for public clients to bypass governed interfaces.

Rollback target: restore prior contract blob SHA `97ff95ba5527968f3db70cd710682176444e4cde` and remove the paired semantic-alignment test. Re-run the contract, schema, fixture, validator, and finite-envelope checks. No provider, model, source, lifecycle, release, deployment, or publication rollback is required because this correction creates none.

<p align="right"><a href="#top">Back to top</a></p>
