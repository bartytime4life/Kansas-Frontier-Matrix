<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-runtime-decision-envelope
title: contracts/runtime/decision_envelope.md — DecisionEnvelope Contract
type: contract
version: v0.2
status: draft; PROPOSED; schema-paired; finite-outcome-envelope; runtime-boundary
owners: OWNER_TBD — Runtime steward · Contracts steward · Schema steward · Policy steward · Evidence steward · API steward · Docs steward
created: NEEDS VERIFICATION — file existed before v0.2 expansion
updated: 2026-06-24
policy_label: public; contracts; runtime; decision-envelope; finite-outcomes; policy-family; obligations; evidence-refs; governed-runtime; no-executable-authority
tags: [kfm, contracts, runtime, decision-envelope, finite-outcomes, answer, abstain, deny, error, policy-family, obligations, reasons, evidence-refs, trust-membrane, schema-paired]
related:
  - ./README.md
  - ./decision_envelope/README.md
  - ./DecisionEnvelope.md
  - ./runtime_response_envelope.md
  - ./ai_receipt.md
  - ../policy/policy_decision.md
  - ../release/promotion_decision.md
  - ../release/release_manifest.md
  - ../../schemas/contracts/v1/runtime/decision_envelope.schema.json
  - ../../policy/runtime/
  - ../../fixtures/contracts/v1/runtime/decision_envelope/
  - ../../tools/validators/validate_decision_envelope.py
  - ../../docs/architecture/contract-schema-policy-split.md
  - ../../docs/architecture/governed-ai.md
notes:
  - "Expanded from existing schema-paired stub at `contracts/runtime/decision_envelope.md`."
  - "Paired schema verified at `schemas/contracts/v1/runtime/decision_envelope.schema.json`; schema status is PROPOSED."
  - "The schema requires decision_id, outcome, policy_family, reasons, obligations, and evaluated_at; additional properties are false."
  - "DecisionEnvelope records a finite runtime decision envelope. It is not PolicyDecision, not PromotionDecision, not ReleaseManifest, not RuntimeResponseEnvelope, not executable runtime behavior, and not public truth by itself."
  - "Rollback target for this expansion is previous blob SHA `f91aa0991a02b758626d978d177cbb1bc0cc1b98`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# DecisionEnvelope Contract

> `DecisionEnvelope` is the governed runtime object that records a finite decision outcome, policy family, reasons, obligations, evidence references, and evaluation time for a runtime decision. It is semantic contract meaning, not runtime code, not policy execution, and not a public answer by itself.

<p>
  <img alt="Status: proposed" src="https://img.shields.io/badge/status-PROPOSED-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts-blue">
  <img alt="Family: runtime" src="https://img.shields.io/badge/family-runtime-0a7ea4">
  <img alt="Object: DecisionEnvelope" src="https://img.shields.io/badge/object-DecisionEnvelope-blueviolet">
  <img alt="Schema: paired" src="https://img.shields.io/badge/schema-paired-green">
  <img alt="Outcomes: finite" src="https://img.shields.io/badge/outcomes-finite-critical">
</p>

**Status:** draft / PROPOSED  
**Path:** `contracts/runtime/decision_envelope.md`  
**Paired schema:** `schemas/contracts/v1/runtime/decision_envelope.schema.json`  
**Schema status:** PROPOSED  
**Validator path named by schema:** `tools/validators/validate_decision_envelope.py` — NEEDS VERIFICATION for implementation/wiring  
**Policy authority:** `policy/runtime/`, not this contract  
**Runtime/API authority:** implementation/API roots, not this contract  
**Truth posture:** CONFIRMED canonical snake_case runtime contract · CONFIRMED paired schema and required field surface · CONFIRMED finite outcome and policy-family enums · CONFIRMED additional properties are closed · NEEDS VERIFICATION for validator wiring, fixtures, runtime policy behavior, API implementation, receipt persistence, and CI enforcement

## Quick jumps

[Purpose](#purpose) · [Meaning](#meaning) · [Schema-paired field surface](#schema-paired-field-surface) · [Field semantics](#field-semantics) · [Outcome semantics](#outcome-semantics) · [Policy family semantics](#policy-family-semantics) · [Invariants](#invariants) · [Lifecycle role](#lifecycle-role) · [Boundaries](#boundaries) · [Validation expectations](#validation-expectations) · [Fixtures](#fixtures) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

`DecisionEnvelope` gives runtime systems a bounded, finite, policy-aware decision object.

It answers:

- which runtime decision was evaluated;
- what finite outcome was selected;
- which policy family governed the decision;
- which reasons explain the decision;
- which obligations attach to the decision;
- which evidence refs may be relevant to the decision;
- when the decision was evaluated;
- which optional compatibility id/version/spec/issued-time fields are present.

It does not answer:

- whether the runtime may execute an action by itself;
- whether public clients may render protected content;
- whether policy evaluation was correct;
- whether evidence refs resolve into EvidenceBundles;
- whether AI output is true;
- whether release publication is approved;
- whether promotion through the lifecycle is allowed.

---

## Meaning

A `DecisionEnvelope` is a runtime-facing contract object. It records the decision posture that downstream runtime/API/UI/map/AI surfaces can interpret without ambiguous success/failure language.

The envelope carries policy-family context and obligations but does not perform policy evaluation. Policy rules live in `policy/runtime/` and adjacent policy roots. Runtime/API implementation lives outside `contracts/`.

A mature decision flow should look like:

```text
request/context
  -> evidence/policy/sensitivity/rights evaluation
  -> runtime decision evaluation
  -> DecisionEnvelope
  -> optional AIReceipt / RuntimeResponseEnvelope / release-aware downstream envelope
  -> governed client rendering or safe denial/abstention/error
```

---

## Schema-paired field surface

The paired schema currently confirms these fields:

| Field | Required | Schema-confirmed shape | Semantic role |
|---|---:|---|---|
| `decision_id` | yes | string matching `^[a-z][a-z0-9_:.-]*$` | Stable runtime decision id. |
| `outcome` | yes | enum: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | Finite decision outcome. |
| `policy_family` | yes | enum: `promotion`, `access`, `render`, `capability`, `consent`, `sensitivity` | Policy family governing the decision. |
| `reasons` | yes | array of strings | Human- and machine-inspectable decision reasons. |
| `obligations` | yes | array of strings | Runtime/client obligations attached to the decision. |
| `evaluated_at` | yes | date-time string | Evaluation timestamp. |
| `id` | no | string | Optional compatibility/general id. |
| `decision` | no | enum: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | Optional legacy/alias outcome field. |
| `reason_code` | no | string | Optional primary reason code. |
| `evidence_refs` | no | array of strings | Optional evidence references. |
| `spec_hash` | no | string | Optional spec/content lineage hash. |
| `version` | no | string | Optional version marker. |
| `issued_at` | no | date-time string | Optional issuance timestamp. |

The schema also confirms:

```text
additionalProperties: false
```

---

## Field semantics

### `decision_id`

Stable id for this decision envelope.

Requirements:

- must follow the schema pattern;
- should be deterministic or traceable enough for audit;
- must not encode secrets, raw prompt text, sensitive coordinates, private data, or credentials.

PROPOSED convention:

```text
decision:<policy_family>:<surface-or-run>:<suffix>
```

### `outcome`

Finite runtime outcome.

The outcome is required and should be the primary field used by clients. The optional `decision` field exists as a schema-supported compatibility alias and should not conflict with `outcome` when both are present.

### `policy_family`

The policy family used to evaluate the decision.

This is required and closed to the schema-confirmed set:

```text
promotion
access
render
capability
consent
sensitivity
```

### `reasons`

Structured reason strings explaining why the decision was produced.

Reason strings should be safe to expose according to the runtime surface. They should not leak sensitive facts, hidden source details, credentials, raw evidence snippets, chain-of-thought, or precise protected locations.

### `obligations`

Runtime/client obligations attached to the decision.

Examples may include citation display, redaction notice, attribution, no-export, restricted rendering, refresh requirement, review requirement, or safe denial messaging. The exact vocabulary is NEEDS VERIFICATION until policy/runtime registers define it.

### `evaluated_at`

Timestamp for decision evaluation.

Use RFC 3339 / JSON Schema `date-time` compatible form. Do not rewrite this timestamp to make stale decisions appear current.

### Optional fields

- `id` may support compatibility with common object id conventions.
- `decision` may act as a compatibility alias for `outcome`.
- `reason_code` may carry a primary reason classification.
- `evidence_refs` may link to EvidenceRefs, but refs alone are not evidence closure.
- `spec_hash`, `version`, and `issued_at` support lineage and compatibility where used.

---

## Outcome semantics

| Outcome | Runtime meaning | Client posture |
|---|---|---|
| `ANSWER` | Runtime may provide the requested answer/payload under current evidence, policy, rights, sensitivity, release, and citation constraints. | Render only with required obligations, citations, and safe-display limits. |
| `ABSTAIN` | Runtime refuses to answer because evidence, citation, rights, sensitivity, freshness, context, or policy support is insufficient or unsafe. | Show safe abstention reason; do not infer answer. |
| `DENY` | Runtime denies access/render/action under policy or governance rules. | Do not render restricted content; show safe denial. |
| `ERROR` | Runtime path failed safely or could not complete deterministically. | Show safe error; do not infer truth or permission. |

`ABSTAIN`, `DENY`, and `ERROR` are first-class outcomes, not hidden exceptions.

---

## Policy family semantics

| Policy family | Meaning boundary |
|---|---|
| `promotion` | Runtime decision related to lifecycle/promotion readiness. Not a PromotionDecision by itself. |
| `access` | Runtime access decision for caller/surface/context. |
| `render` | Runtime display/render decision for UI/map/API output. |
| `capability` | Runtime capability/tool/action permission decision. |
| `consent` | Runtime decision depending on consent posture. |
| `sensitivity` | Runtime decision depending on sensitivity, redaction, or geoprivacy posture. |

Policy-family choice does not execute policy. It identifies the family whose rules or decision context govern the envelope.

---

## Invariants

CONFIRMED by paired schema:

- `decision_id`, `outcome`, `policy_family`, `reasons`, `obligations`, and `evaluated_at` are required.
- `decision_id` must match `^[a-z][a-z0-9_:.-]*$`.
- `outcome` must be one of `ANSWER | ABSTAIN | DENY | ERROR`.
- `decision`, if present, must also be one of `ANSWER | ABSTAIN | DENY | ERROR`.
- `policy_family` must be one of `promotion | access | render | capability | consent | sensitivity`.
- `evaluated_at` and `issued_at`, if present, must be date-time strings.
- Additional properties are not allowed.

PROPOSED semantic invariants:

- If both `outcome` and `decision` are present, they should match.
- `ANSWER` should require evidence/citation/policy support appropriate to the surface.
- `ABSTAIN` should be used when evidence or policy cannot safely support a definitive response.
- `DENY` should be used for policy or access prohibitions, not generic runtime errors.
- `ERROR` should be safe and non-leaking.
- `reasons` and `obligations` should use controlled vocabularies once registers exist.
- Runtime envelopes must not leak sensitive details through reason strings or obligation text.
- Public clients must not treat the envelope as permission to bypass governed APIs, release manifests, or policy gates.

---

## Lifecycle role

`DecisionEnvelope` may be produced at runtime or internal gate boundaries where a finite outcome is needed.

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Typical uses:

| Context | Role of DecisionEnvelope |
|---|---|
| Access check | Carries access result and obligations. |
| Render check | Carries display/redaction/withhold posture. |
| AI answer path | Carries finite answer/abstain/deny/error posture, often alongside AIReceipt. |
| Promotion helper | Carries runtime decision context, but not final PromotionDecision. |
| Public response | May inform RuntimeResponseEnvelope, but is not a full client response by itself. |
| Correction/withdrawal | May carry stale/deny/abstain posture when release state changes. |

---

## Boundaries

| Boundary | Rule |
|---|---|
| DecisionEnvelope vs PolicyDecision | DecisionEnvelope carries runtime-facing decision posture; PolicyDecision records policy evaluation object semantics. |
| DecisionEnvelope vs PromotionDecision | DecisionEnvelope may support promotion context; PromotionDecision records governed lifecycle transition decisions. |
| DecisionEnvelope vs RuntimeResponseEnvelope | DecisionEnvelope is a decision object; RuntimeResponseEnvelope is API/client-facing response envelope. |
| DecisionEnvelope vs AIReceipt | DecisionEnvelope records finite decision; AIReceipt records AI run accountability. |
| DecisionEnvelope vs EvidenceBundle | EvidenceBundle supports factual claims; evidence refs in this envelope are pointers only. |
| DecisionEnvelope vs release | It does not publish, promote, or release artifacts. |
| DecisionEnvelope vs runtime code | It is not executable behavior or API implementation. |

---

## Validation expectations

NEEDS VERIFICATION in implementation:

- validator existence and wiring for `tools/validators/validate_decision_envelope.py`;
- fixture coverage under `fixtures/contracts/v1/runtime/decision_envelope/`;
- controlled vocabulary for `reasons`, `reason_code`, and `obligations`;
- cross-field check that `decision` matches `outcome` if both exist;
- policy-family-specific obligation rules;
- public API/UI/map/AI tests proving no RAW/WORK/QUARANTINE/internal-store bypass;
- tests proving sensitive facts are not leaked in reason/obligation fields;
- correction/withdrawal/stale-state propagation through runtime envelopes.

---

## Fixtures

Minimum fixture set PROPOSED:

| Fixture | Purpose |
|---|---|
| `valid_answer_access.json` | Valid ANSWER for access policy family with obligations and evaluated_at. |
| `valid_abstain_sensitivity.json` | Valid ABSTAIN for sensitivity uncertainty. |
| `valid_deny_render.json` | Valid DENY for restricted render. |
| `valid_error_capability.json` | Valid ERROR for safe tool/capability failure. |
| `valid_with_evidence_refs.json` | Valid envelope with evidence refs. |
| `invalid_missing_decision_id.json` | Confirms required id. |
| `invalid_bad_decision_id_pattern.json` | Confirms id pattern. |
| `invalid_unknown_outcome.json` | Confirms finite outcome enum. |
| `invalid_unknown_policy_family.json` | Confirms policy-family enum. |
| `invalid_extra_property.json` | Confirms additional properties are closed. |
| `governance_invalid_outcome_decision_mismatch.json` | Schema may pass; semantic validator should fail if adopted. |

Fixtures must use synthetic/safe refs only.

---

## Open questions

- Should `decision` be deprecated in favor of `outcome`, or retained as compatibility alias?
- Should `reasons`, `reason_code`, and `obligations` use central runtime vocabularies?
- Should `evidence_refs` become required for `ANSWER` in public-facing contexts?
- Should the schema include `policy_decision_ref` directly, or should that remain in adjacent objects?
- Which runtime root persists DecisionEnvelope instances?

---

## Rollback

Rollback is required if this contract is used as executable runtime behavior, public API permission, release approval, policy authority, evidence authority, AI truth, or a way to bypass governed runtime/API envelopes.

Rollback target for this expansion: previous blob SHA `f91aa0991a02b758626d978d177cbb1bc0cc1b98`.

<p align="right"><a href="#top">Back to top</a></p>
