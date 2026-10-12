<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-policy-policy-decision
title: PolicyDecision Semantic Contract
type: contract
version: v0.2
status: draft; PROPOSED; schema-paired; policy-runtime-aware
owners: OWNER_TBD — Policy steward · Contracts steward · Schema steward · Policy-runtime steward · Evidence steward · Release steward · Docs steward
created: NEEDS VERIFICATION — contract existed before v0.2 expansion
updated: 2026-06-24
policy_label: public; contracts; policy; policy-decision; finite-outcomes; fail-closed; evidence-aware; release-gated; no-runtime-authority
related:
  - ./README.md
  - ./policy_input_bundle.md
  - ./sensitivity_label.md
  - ../runtime/decision_envelope.md
  - ../../schemas/contracts/v1/policy/policy_decision.schema.json
  - ../../policy/
  - ../../packages/policy-runtime/README.md
  - ../../docs/architecture/contract-schema-policy-split.md
  - ../../docs/architecture/governed-ai/FOCUS_FLOW.md
  - ../../docs/standards/MAP_TRUST_STATES.md
  - ../../docs/architecture/publication/RELEASE_GATES.md
  - ../../fixtures/contracts/v1/policy/policy_decision/
  - ../../tests/contracts/policy/
tags: [kfm, contracts, policy, policy-decision, finite-outcomes, answer, abstain, deny, error, allow, restrict, hold, reasons, obligations, evidence-bundle, release-gate, fail-closed]
notes:
  - "Expanded from existing `contracts/policy/policy_decision.md`."
  - "Paired schema verified at `schemas/contracts/v1/policy/policy_decision.schema.json`; schema status is PROPOSED."
  - "This contract defines semantic meaning only. It does not author executable policy, define JSON Schema shape, execute policy runtime helpers, issue receipts, publish artifacts, or override release gates."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# PolicyDecision

> `PolicyDecision` records the finite, auditable outcome of one policy evaluation event. It says what gate evaluated what policy family, what outcome was reached, why, what obligations apply, and when the decision was evaluated. It does **not** execute policy, publish artifacts, replace release approval, or serve as a runtime transport envelope.

<p>
  <img alt="Status: proposed" src="https://img.shields.io/badge/status-PROPOSED-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts-blue">
  <img alt="Object: PolicyDecision" src="https://img.shields.io/badge/object-PolicyDecision-0a7ea4">
  <img alt="Authority: semantic meaning" src="https://img.shields.io/badge/authority-semantic__meaning-blueviolet">
  <img alt="Outcome: finite" src="https://img.shields.io/badge/outcome-finite-critical">
  <img alt="Publication: not sufficient" src="https://img.shields.io/badge/publication-not__sufficient-critical">
</p>

**Status:** draft / PROPOSED  
**Contract path:** `contracts/policy/policy_decision.md`  
**Schema path:** `schemas/contracts/v1/policy/policy_decision.schema.json`  
**Schema status:** PROPOSED  
**Validator path named by schema:** `tools/validators/validate_policy_decision.py` — NEEDS VERIFICATION for implementation/wiring  
**Policy rule authority:** `policy/`, not this contract  
**Runtime helper authority:** `packages/policy-runtime/`, not this contract  
**Runtime envelope distinction:** `contracts/runtime/decision_envelope.md`  
**Truth posture:** CONFIRMED schema pairing and field surface · PROPOSED semantic invariants beyond current schema · NEEDS VERIFICATION for validators, fixtures, policy bundles, runtime adapters, receipts, and CI enforcement

## Quick jumps

[Purpose](#purpose) · [Meaning](#meaning) · [Schema-paired field surface](#schema-paired-field-surface) · [Field semantics](#field-semantics) · [Outcome semantics](#outcome-semantics) · [Invariants](#invariants) · [Lifecycle role](#lifecycle-role) · [Boundaries](#boundaries) · [Validation expectations](#validation-expectations) · [Fixtures](#fixtures) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

`PolicyDecision` is the canonical semantic object for a single policy evaluation result.

It answers:

- which policy-decision event was produced;
- which finite outcome was reached;
- which policy family produced the result;
- which reasons explain the result;
- which obligations must be honored by downstream systems;
- when the decision was evaluated.

It does not answer:

- whether the JSON instance is well-shaped — that is the schema validator's job;
- whether executable policy should allow a future action — that is `policy/` and the policy runtime's job;
- whether a release is approved — that is the release gate's job;
- whether a public API, UI, map, or AI response may render the object — that requires governed runtime envelopes and release/publication checks.

---

## Meaning

A `PolicyDecision` is an evidence-aware, policy-family-scoped, finite decision record. It is produced when a governed gate evaluates explicit policy inputs against the policy rules in force.

A `PolicyDecision` may be used by:

- runtime gates before a governed API response;
- map/layer render gates before public display;
- governed AI envelopes before answering or abstaining;
- promotion gates before CATALOG/TRIPLET/PUBLISHED movement;
- release gates before publication;
- correction, withdrawal, and rollback workflows.

A `PolicyDecision` must remain distinguishable from:

- a `PolicyInputBundle` — input to policy evaluation;
- a `DecisionEnvelope` — runtime transport envelope carrying decisions and context;
- a `ReleaseManifest` — release artifact binding published contents;
- a `ReviewRecord` — human/steward review artifact;
- an `EvidenceBundle` — evidence closure;
- a receipt/proof artifact — auditable emitted record.

---

## Schema-paired field surface

The paired schema currently defines these fields as required and disallows additional properties.

| Field | Required | Schema-confirmed shape | Semantic role |
|---|---:|---|---|
| `decision_id` | yes | string matching `^[a-z][a-z0-9_:.-]*$` | Stable identifier for this policy evaluation event. |
| `outcome` | yes | enum: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | Finite outcome consumed by callers/envelopes. |
| `policy_family` | yes | enum: `promotion`, `access`, `render`, `capability`, `consent`, `sensitivity` | Policy lane that produced the decision. |
| `reasons` | yes | array of strings | Reason codes or explanations supporting the outcome. |
| `obligations` | yes | array of strings | Required downstream conditions or duties. |
| `evaluated_at` | yes | string, `date-time` | Time of evaluation for audit/freshness/supersession. |

> [!NOTE]
> This contract may recommend semantics that are not yet schema-enforced. Those recommendations are labeled PROPOSED or NEEDS VERIFICATION until paired validators, policy rules, fixtures, and tests prove them.

---

## Field semantics

### `decision_id`

Unique identifier for one policy evaluation event.

Requirements:

- stable enough to cite in receipts, logs, release gates, validation reports, and correction workflows;
- specific to this evaluation, not a mutable pointer to the newest decision;
- safe to expose where policy permits.

PROPOSED convention:

```text
poldec:<date-or-run-id>:<policy-family>:<short-purpose>
```

### `outcome`

Finite outcome returned by the policy decision object.

The current schema uses runtime-facing outcome vocabulary: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`. This differs from lower-level policy-bundle vocabulary such as `ALLOW`, `DENY`, `RESTRICT`, `HOLD`, or equivalent engine-native results.

The semantic rule is:

- `ANSWER` means the governed caller may proceed for the evaluated operation, subject to obligations;
- `ABSTAIN` means admissible support is insufficient or unresolved, so the system refuses to manufacture a claim;
- `DENY` means a policy rule blocks the operation;
- `ERROR` means shape, integrity, evaluator, process, or missing-context failure.

### `policy_family`

Policy lane that produced the decision.

Current schema values:

- `promotion`
- `access`
- `render`
- `capability`
- `consent`
- `sensitivity`

Each family should have a documented reason-code vocabulary and obligation interpreter before public clients rely on it.

### `reasons`

Machine/human-readable reason list explaining why the outcome was reached.

PROPOSED requirements:

- non-empty for `ABSTAIN`, `DENY`, and `ERROR`;
- stable reason codes preferred over free prose;
- safe public explanation should be separable from internal/steward-only detail;
- sensitive facts must not be embedded directly in reason strings.

### `obligations`

Required downstream duties attached to the decision.

Examples:

- `attach_citation`
- `redact_coordinates`
- `generalize_geometry`
- `withhold_exact_location`
- `require_steward_review`
- `delay_publication`
- `attach_rights_notice`
- `block_export`
- `rollback_check_required`

Obligations are not suggestions. If a caller cannot satisfy an obligation, it must fail closed rather than proceed.

### `evaluated_at`

Time the policy decision was evaluated.

Semantics:

- used for freshness checks;
- used to compare superseding decisions;
- must not be rewritten to make stale decisions appear current;
- should use UTC RFC 3339 / JSON Schema `date-time` compatible form.

---

## Outcome semantics

| Outcome | Meaning | Typical downstream posture |
|---|---|---|
| `ANSWER` | Policy and evidence context allow the requested operation. | Proceed only if obligations and release/runtime gates also pass. |
| `ABSTAIN` | Admissible support is insufficient, unresolved, stale, or not policy-safe. | Do not answer or publish; surface bounded explanation. |
| `DENY` | A rule blocks the requested operation. | Block operation; surface safe reason where allowed. |
| `ERROR` | Shape, integrity, evaluator, process, missing-context, or wiring failure. | Fail closed; log/receipt if configured; do not convert to answer. |

> [!WARNING]
> `ANSWER` is not a release approval. It is a policy-decision outcome for the evaluated context. Publication still requires release gates, evidence, rights, review, integrity, correction, and rollback support.

---

## Invariants

CONFIRMED by paired schema:

- `decision_id` is required.
- `outcome` is required and must be one of `ANSWER | ABSTAIN | DENY | ERROR`.
- `policy_family` is required and must be one of `promotion | access | render | capability | consent | sensitivity`.
- `reasons` is required and is an array of strings.
- `obligations` is required and is an array of strings.
- `evaluated_at` is required and must be a `date-time` string.
- No additional properties are allowed by the current schema.

PROPOSED semantic invariants:

- `reasons` SHOULD be non-empty for `ABSTAIN`, `DENY`, and `ERROR`.
- `obligations` SHOULD be non-empty when `ANSWER` depends on constraints, redactions, delayed release, staged access, or citations.
- `ERROR` MUST NOT be converted into `DENY` or `ABSTAIN` without preserving process-failure detail.
- `ABSTAIN` MUST remain distinct from `DENY` so evidence shortage does not masquerade as policy refusal.
- `ANSWER` MUST NOT bypass release, review, evidence, rights, sensitivity, or rollback gates.
- A later decision supersedes earlier decisions by issuing a new `decision_id` / `evaluated_at`, not by mutating old decisions.
- Sensitive details must not be embedded in public reason strings or obligations.

---

## Lifecycle role

Policy decisions may be produced at multiple gates across the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Expected uses:

- **WORK / QUARANTINE:** block unsafe promotion, quarantine rights/sensitivity issues, or require review.
- **PROCESSED:** confirm admissibility before catalog/triplet projection.
- **CATALOG / TRIPLET:** gate search, graph, layer, and API exposure.
- **PUBLISHED:** verify release-state, correction, rollback, export, public UI, map, and AI response safety.

A `PolicyDecision` may accompany a release candidate or runtime request, but it does not itself move an artifact through the lifecycle.

---

## Boundaries

| Boundary | Rule |
|---|---|
| Contract vs schema | This contract defines meaning; schema defines shape. |
| Contract vs policy | This contract names decision semantics; `policy/` owns executable admissibility. |
| Contract vs runtime | Runtime envelopes carry decisions; this object is not the transport wrapper. |
| Contract vs release | Release gates may require policy decisions, but policy decisions do not publish artifacts. |
| Contract vs evidence | Policy may consume evidence status; EvidenceBundle remains evidence authority. |
| Contract vs AI | AI may explain a decision with citations; it cannot create or override one. |

---

## Validation expectations

NEEDS VERIFICATION in implementation:

- schema validation command for `schemas/contracts/v1/policy/policy_decision.schema.json`;
- validator existence and wiring for `tools/validators/validate_policy_decision.py`;
- fixtures under `fixtures/contracts/v1/policy/policy_decision/`;
- tests for valid, invalid, answer, abstain, deny, error, constrained-answer, stale-decision, and sensitive-reason cases;
- policy-runtime adapter mapping from engine-native results to schema-confirmed outcome vocabulary;
- release/runtime checks that prevent `ANSWER` from bypassing release gates.

---

## Fixtures

Minimum fixture set PROPOSED:

| Fixture | Purpose |
|---|---|
| `valid_answer_minimal.json` | Valid `ANSWER` decision with explicit evidence-safe reasons. |
| `valid_abstain_missing_evidence.json` | First-class abstention for missing admissible evidence. |
| `valid_deny_sensitive_location.json` | Denial for sensitive exposure. |
| `valid_error_invalid_bundle.json` | Process/evaluator failure distinguished from content denial. |
| `invalid_extra_property.json` | Confirms `additionalProperties: false`. |
| `invalid_unknown_outcome.json` | Confirms finite outcome enum. |
| `valid_answer_with_obligations.json` | Allows operation only with enforceable obligations. |
| `valid_superseding_decision.json` | Demonstrates new decision superseding older one without mutation. |

Fixtures for sensitive lanes must use synthetic or generalized values only.

---

## Open questions

- Should `PolicyDecision.outcome` remain runtime vocabulary `ANSWER | ABSTAIN | DENY | ERROR`, or should a separate engine-facing enum support `ALLOW | DENY | RESTRICT | HOLD | ABSTAIN | ERROR`?
- Should `reasons` and `obligations` become typed objects instead of strings in a future schema version?
- Should `PolicyDecision` reference `PolicyInputBundle` hash, policy bundle hash, evaluator version, EvidenceBundle refs, and receipt refs directly, or should those stay in `DecisionEnvelope` / receipt records?
- Where should public-safe vs steward-only explanations be modeled?
- What validator should enforce non-empty `reasons` for negative outcomes?

---

## Rollback

Rollback is required if this contract is used to host executable policy, bypass release gates, collapse `ABSTAIN` and `DENY`, treat `ANSWER` as publication approval, embed sensitive facts in public reason strings, or treat AI-generated text as policy authority.

Rollback target for this expansion: previous blob SHA `35f137e3e0d433abe78f5e5f3139b180cb8ed682`.

<p align="right"><a href="#top">Back to top</a></p>
