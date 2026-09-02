<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-release-promotion-decision
title: contracts/release/promotion_decision.md — PromotionDecision Contract
type: contract
version: v0.2
status: draft; PROPOSED; schema-paired; promotion-gate; fail-closed
owners: OWNER_TBD — Release steward · Promotion steward · Contracts steward · Schema steward · Policy steward · Evidence steward · Review steward · Rollback steward · Docs steward
created: NEEDS VERIFICATION — file existed before v0.2 expansion
updated: 2026-06-24
policy_label: public; contracts; release; promotion-decision; governed-state-transition; review-required; evidence-required; rollback-required; fail-closed; no-file-move
tags: [kfm, contracts, release, promotion-decision, promotion, release-gate, review, evidence-ref, evidence-bundle, rollback-card, policy-bundle, approve, deny, abstain, fail-closed]
related:
  - ./README.md
  - ./release_manifest.md
  - ./rollback_card.md
  - ./withdrawal_notice.md
  - ./map_release_manifest.md
  - ./layer_manifest.md
  - ../policy/policy_decision.md
  - ../evidence/evidence_bundle.md
  - ../../schemas/contracts/v1/release/promotion_decision.schema.json
  - ../../policy/promotion/
  - ../../policy/release/
  - ../../release/
  - ../../fixtures/release/promotion_decision/
  - ../../tools/validators/release/validate_promotion_decision.py
  - ../../docs/architecture/release-discipline.md
  - ../../docs/architecture/contract-schema-policy-split.md
notes:
  - "Expanded from existing `contracts/release/promotion_decision.md`."
  - "Paired schema verified at `schemas/contracts/v1/release/promotion_decision.schema.json`; schema status is PROPOSED."
  - "The schema requires id, version, domain, run_id, decision, evidence_ref, evidence_bundle_uri, rollback_card_uri, policy_bundle, decided_at, and review."
  - "PromotionDecision records a governed transition decision; it is not a file move, not release approval by itself, not the ReleaseManifest, and not the runtime PolicyDecision object."
  - "Rollback target for this expansion is previous blob SHA `cba01b0126cd6adb0d74617bfb5be9fffa26b773`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# PromotionDecision Contract

> `PromotionDecision` records a reviewed, evidence-bound, policy-bound decision about whether a specific run or release candidate may cross a governed lifecycle boundary. It is a release-family decision object, not a file move, deployment shortcut, release manifest, or public-surface permission by itself.

<p>
  <img alt="Status: proposed" src="https://img.shields.io/badge/status-PROPOSED-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts-blue">
  <img alt="Object: PromotionDecision" src="https://img.shields.io/badge/object-PromotionDecision-0a7ea4">
  <img alt="Schema: paired" src="https://img.shields.io/badge/schema-paired-green">
  <img alt="Invariant: no file move" src="https://img.shields.io/badge/promotion-not__a__file__move-critical">
  <img alt="Review: required" src="https://img.shields.io/badge/review-required-critical">
</p>

**Status:** draft / PROPOSED  
**Path:** `contracts/release/promotion_decision.md`  
**Paired schema:** `schemas/contracts/v1/release/promotion_decision.schema.json`  
**Validator path named by schema:** `tools/validators/release/validate_promotion_decision.py` — NEEDS VERIFICATION for implementation/wiring  
**Policy authority:** `policy/promotion/` and `policy/release/`, not this contract  
**Release artifact/process authority:** `release/`, not this contract  
**Truth posture:** CONFIRMED schema pairing and required field surface · CONFIRMED finite decision enum · CONFIRMED promotion doctrine says promotion is governed state transition, not file move · NEEDS VERIFICATION for fixtures, validator wiring, policy behavior, release runtime, receipt emission, and CI enforcement

## Quick jumps

[Purpose](#purpose) · [Meaning](#meaning) · [Schema-paired field surface](#schema-paired-field-surface) · [Field semantics](#field-semantics) · [Decision semantics](#decision-semantics) · [Invariants](#invariants) · [Lifecycle role](#lifecycle-role) · [Boundaries](#boundaries) · [Validation expectations](#validation-expectations) · [Fixtures](#fixtures) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

`PromotionDecision` is the auditable decision record for a governed transition.

It answers:

- which promotion decision was made;
- which domain/lane and run were evaluated;
- whether the transition was `APPROVE`, `DENY`, or `ABSTAIN`;
- which evidence and EvidenceBundle support the decision;
- which rollback card applies;
- which policy bundle was used;
- when the decision was made;
- who reviewed it and which ticket binds the review.

It does not answer:

- whether files were physically moved or copied;
- whether a release manifest has been emitted;
- whether the public API/UI/map/AI surface may serve the artifact;
- whether evidence is true by itself;
- whether a rollback has executed;
- whether policy logic is implemented correctly.

---

## Meaning

A `PromotionDecision` is a release-governance record. It is produced by a promotion gate after explicit inputs are evaluated against evidence, policy, review, and rollback requirements.

Promotion is not a storage operation. A file copied into a directory, a merged pull request, a deployed tile, or a generated AI response is not a promotion unless the decision, required artifacts, resolving references, and policy record exist.

A `PromotionDecision` must preserve:

- evidence closure;
- policy bundle identity;
- reviewer accountability;
- rollback readiness;
- finite decision outcome;
- lifecycle boundary context;
- failure-closed behavior.

---

## Schema-paired field surface

The paired schema currently defines these required fields and disallows additional properties.

| Field | Required | Schema-confirmed shape | Semantic role |
|---|---:|---|---|
| `id` | yes | string, minLength 1; hydrology conditional pattern for hydrology domain | Stable promotion decision id. |
| `version` | yes | string const `v1` | Object/schema version marker. |
| `domain` | yes | string, minLength 1 | Domain or lane being evaluated. |
| `run_id` | yes | string, minLength 1 | Candidate run or pipeline execution id. |
| `decision` | yes | enum: `APPROVE`, `DENY`, `ABSTAIN` | Finite transition decision. |
| `evidence_ref` | yes | string, minLength 1 | Evidence reference supporting decision. |
| `evidence_bundle_uri` | yes | string, minLength 1 | EvidenceBundle closure URI/ref. |
| `rollback_card_uri` | yes | string, minLength 1 | Rollback target/ref required for safe transition. |
| `policy_bundle` | yes | string, minLength 1 | Policy bundle used during evaluation. |
| `decided_at` | yes | string, `date-time` | Decision timestamp. |
| `review` | yes | object with required `reviewer` and `ticket`; no extra fields | Reviewer and ticket binding. |

Schema-confirmed hydrology rule:

- if `domain` is `hydrology`, `id` must match `^promo:hydrology:[A-Za-z0-9._:-]+$`.

---

## Field semantics

### `id`

Stable id for the promotion decision event.

Requirements:

- should be deterministic enough to audit and cite;
- should not be reused for a later decision;
- should encode domain/lane where convention allows;
- for hydrology, the current schema requires `promo:hydrology:<suffix>`.

### `version`

Schema/object version marker.

Current schema requires exactly:

```text
v1
```

### `domain`

Domain, lane, or release family being evaluated.

Examples may include `hydrology`, `flora`, `fauna`, `geology`, `settlements`, `roads-rail-trade`, `map`, or another accepted domain/lane. The schema currently only applies a specific id pattern when `domain` is `hydrology`.

### `run_id`

Pipeline execution, candidate build, processing run, or release-candidate run being evaluated.

A `run_id` should identify the exact unit whose lifecycle transition is under review.

### `decision`

Finite transition decision:

- `APPROVE`
- `DENY`
- `ABSTAIN`

This is release/promotion vocabulary. It is distinct from runtime `PolicyDecision` vocabulary such as `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`.

### `evidence_ref` and `evidence_bundle_uri`

Evidence reference and closure URI/ref supporting the decision.

Semantic expectations:

- references must resolve before approval;
- reference alone is not closure;
- EvidenceBundle remains the evidence authority;
- if evidence cannot resolve, the promotion decision must not approve.

### `rollback_card_uri`

Ref to rollback target/instructions for the promoted unit.

A material promotion without rollback support is unsafe unless an explicit, reviewed waiver exists elsewhere. The current schema requires the field; this contract treats rollback readiness as a core invariant.

### `policy_bundle`

Identity of the policy bundle used during evaluation.

This should be specific enough to reproduce or audit policy behavior, such as a bundle id, version, hash, or release ref.

### `decided_at`

Decision timestamp.

Use UTC RFC 3339 / JSON Schema `date-time` compatible form. Do not rewrite timestamps to make stale decisions appear current.

### `review`

Reviewer and ticket binding.

Current schema requires:

- `reviewer`
- `ticket`

The review object is not a full `ReviewRecord`. It is a minimal binding for accountability. A richer ReviewRecord may still be required by policy/release discipline.

---

## Decision semantics

| Decision | Meaning | Downstream posture |
|---|---|---|
| `APPROVE` | Gate has enough evidence, policy, review, and rollback support to permit the evaluated transition. | May proceed only through release process; still not a public API/UI/map/AI permission by itself. |
| `DENY` | Gate finds a blocking condition. | Preserve prior state; record safe reason in policy/review artifacts. |
| `ABSTAIN` | Gate cannot decide due to insufficient, unresolved, stale, conflicted, or unsafe context. | Fail closed; preserve prior state; route for review/remediation. |

> [!WARNING]
> `APPROVE` is not publication by itself. It permits the transition only when all required release artifacts, schemas, policies, reviews, receipts, proofs, manifests, and rollback paths are also satisfied.

---

## Invariants

CONFIRMED by paired schema:

- All required fields listed above must exist.
- `version` must be `v1`.
- `decision` must be one of `APPROVE | DENY | ABSTAIN`.
- `review.reviewer` and `review.ticket` are required.
- `review` does not allow additional properties.
- The object does not allow additional properties.
- Hydrology decision ids must match the schema pattern when `domain` is `hydrology`.

PROPOSED semantic invariants:

- Promotion is a governed state transition, not a file move, rename, merge, deployment, or UI action.
- `APPROVE` requires resolvable evidence and EvidenceBundle support.
- `APPROVE` requires rollback-card support.
- `APPROVE` requires an identified policy bundle.
- `APPROVE` requires review binding and may also require a full ReviewRecord depending on materiality/sensitivity.
- `DENY` and `ABSTAIN` must preserve the prior lifecycle state and should carry safe reason codes in policy/review artifacts.
- Missing evidence, rollback, review, policy bundle, release manifest, validation report, or sensitivity/rights support must fail closed.
- A later promotion decision supersedes prior decisions by emitting a new object, not silently mutating history.

---

## Lifecycle role

Promotion decisions may occur at governed transition gates across the lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Typical release-facing use:

| Gate | Role of PromotionDecision |
|---|---|
| RAW → WORK / QUARANTINE | May record normalization/admission gate decision where release discipline requires it. |
| WORK → PROCESSED | May record validation-gate readiness decision. |
| PROCESSED → CATALOG/TRIPLET | May record catalog/triplet closure readiness. |
| CATALOG/TRIPLET → PUBLISHED | Required for release approval/hold/denial where material release is governed. |
| PUBLISHED correction/rollback | May record superseding decision for corrected, withdrawn, or rollback release state. |

---

## Boundaries

| Boundary | Rule |
|---|---|
| Contract vs schema | This contract defines meaning; schema defines machine shape. |
| Contract vs policy | Policy decides admissibility; this object records the transition decision. |
| PromotionDecision vs PolicyDecision | PromotionDecision is release transition vocabulary; PolicyDecision is policy gate/runtime vocabulary. |
| PromotionDecision vs ReleaseManifest | PromotionDecision is the gate decision; ReleaseManifest binds the release artifact set. |
| PromotionDecision vs RollbackCard | PromotionDecision references rollback support; RollbackCard defines rollback target/instructions. |
| PromotionDecision vs ReviewRecord | This schema has minimal review binding; full ReviewRecord may be separate. |
| PromotionDecision vs public surface | Public API/UI/map/AI are downstream and cannot rely on this object alone. |

---

## Validation expectations

NEEDS VERIFICATION in implementation:

- validator existence and wiring for `tools/validators/release/validate_promotion_decision.py`;
- fixture coverage under `fixtures/release/promotion_decision/`;
- tests for approve, deny, abstain, missing evidence, missing rollback, missing review, invalid hydrology id, invalid decision enum, extra properties, stale policy bundle, and supersession;
- policy behavior under `policy/promotion/` and `policy/release/`;
- receipt/proof emission for decision events;
- release process storage under `release/promotion_decisions/<domain>/` or accepted release decision home;
- separation-of-duties enforcement.

---

## Fixtures

Minimum fixture set PROPOSED:

| Fixture | Purpose |
|---|---|
| `valid_hydrology_approve.json` | Valid APPROVE with hydrology id pattern, evidence, rollback, policy bundle, review. |
| `valid_deny_missing_rights.json` | DENY due to rights/policy blocker. |
| `valid_abstain_unresolved_evidence.json` | ABSTAIN due to unresolved EvidenceBundle. |
| `invalid_missing_rollback_card_uri.json` | Confirms rollback field is required. |
| `invalid_missing_review_ticket.json` | Confirms review ticket is required. |
| `invalid_hydrology_id_pattern.json` | Confirms hydrology id pattern. |
| `invalid_unknown_decision.json` | Confirms finite enum. |
| `invalid_extra_property.json` | Confirms additional properties are closed. |
| `valid_superseding_decision.json` | Demonstrates new decision superseding a prior decision. |

Fixtures must use synthetic or safe refs only.

---

## Open questions

- Should every domain get a domain-specific `id` pattern, or should only hydrology remain special?
- Should `review` reference a full `ReviewRecord` instead of embedding reviewer/ticket only?
- Should `evidence_ref` and `evidence_bundle_uri` be collapsed into typed EvidenceRef/EvidenceBundle refs?
- Should `decision=APPROVE` require a companion `ReleaseManifest` ref in the schema?
- Which release root is canonical for persisted promotion decision instances?

---

## Rollback

Rollback is required if this contract is used as a file-move shortcut, public-surface permission, release manifest, policy engine, evidence authority, review replacement, or rollback execution record.

Rollback target for this expansion: previous blob SHA `cba01b0126cd6adb0d74617bfb5be9fffa26b773`.

<p align="right"><a href="#top">Back to top</a></p>
