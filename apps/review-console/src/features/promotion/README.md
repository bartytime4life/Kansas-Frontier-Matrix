<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://app/review-console/src/features/promotion/readme
title: Review Console Promotion — Governed Readiness and Recommendation-Handoff Boundary
type: app-readme; directory-readme; feature-boundary; promotion-review-support
version: v0.2
status: draft; repository-grounded; readme-only-direct-lane; shape-validation-executable; promotion-held; executable-feature-not-established
owners: OWNER_TBD — Review steward · Promotion steward · Release steward · Policy steward · Evidence steward · Security steward · API steward · UI steward · Validation steward · Docs steward
created: 2026-06-16
updated: 2026-07-19
policy_label: "public-governance; restricted-review; role-gated; evidence-bound; release-subordinate; no-local-promotion; no-file-move; no-publication-authority"
current_path: apps/review-console/src/features/promotion/README.md
owning_root: apps/
responsibility: define the app-local promotion-readiness projection and bounded recommendation handoff without creating or mutating PromotionDecision, ReviewRecord, PolicyDecision, ReleaseManifest, RollbackCard, lifecycle state, release records, evidence, policy, receipts, proofs, or published artifacts
truth_posture: CONFIRMED existing v0.1 README, Review Console parent boundaries, README-only bounded feature search, closed PromotionDecision schema, executable shape validator and fixture test, hydrology fixtures, hard-coded hydrology APPROVE stub, tracked unresolved smoke decision, read-only promotion-gate workflow hold, non-enforcing promotion policy stubs, placeholder semantic gate and ReviewRecord validators, and thin ReleaseManifest and RollbackCard schemas / PROPOSED governed UI projection and recommendation handoff / CONFLICTED promotion, review, policy, release, and UI vocabularies / UNKNOWN governed API DTO, authoritative evaluator/writer, real review records, cross-domain runtime, deployment, and full-suite status
base_commit: 74c669f23e675fc48fbff72a5c0c9bb055fb1080
prior_blob: eee28922e3e74019fd2d35a2a03da3f9cd9c81ef
related:
  - ../README.md
  - ../audit_log/README.md
  - ../correction/README.md
  - ../rollback/README.md
  - ../../../../governed-api/README.md
  - ../../../../../docs/architecture/directory-rules.md
  - ../../../../../contracts/release/promotion_decision.md
  - ../../../../../contracts/release/release_manifest.md
  - ../../../../../contracts/release/rollback_card.md
  - ../../../../../schemas/contracts/v1/release/promotion_decision.schema.json
  - ../../../../../schemas/contracts/v1/governance/review_record.schema.json
  - ../../../../../schemas/contracts/v1/policy/policy_decision.schema.json
  - ../../../../../fixtures/release/promotion_decision/README.md
  - ../../../../../tools/validators/release/validate_promotion_decision.py
  - ../../../../../tools/validators/validate_promotion_gate.py
  - ../../../../../tests/release/test_promotion_decision_schema.py
  - ../../../../../policy/promotion/README.md
  - ../../../../../policy/promotion/promotion_prerequisites.rego
  - ../../../../../policy/promotion/rollback_card_required.rego
  - ../../../../../pipelines/domains/hydrology/promote.py
  - ../../../../../release/promotion_decisions/README.md
  - ../../../../../release/promotion_decisions/hydrology/run-local-smoke.json
  - ../../../../../.github/workflows/promotion-gate.yml
tags: [kfm, apps, review-console, promotion, release-readiness, evidence, policy, review, rollback, fail-closed]
notes:
  - "PromotionDecision shape validation is executable; promotion authorization and publication remain held."
  - "The tracked hydrology APPROVE record is an unresolved smoke artifact, not release authority."
  - "This update changes documentation and its generated-work receipt only."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Review Console Promotion

`apps/review-console/src/features/promotion/`

> Role-gated, app-local promotion-readiness view and recommendation handoff. It must not promote, publish, move lifecycle files, write release records, execute policy in the browser, or treat a schema-valid `APPROVE` as release authority.

![status](https://img.shields.io/badge/status-draft-yellow)
![shape](https://img.shields.io/badge/shape-validation__executable-green)
![runtime](https://img.shields.io/badge/promotion-held-orange)
![authority](https://img.shields.io/badge/authority-review__support__only-critical)

[Purpose](#purpose) · [Evidence](#current-evidence) · [Authority](#authority-boundary) · [Smoke path](#hydrology-smoke-path) · [Decision axes](#decision-and-state-axes) · [Readiness](#readiness-closure) · [Handoff](#recommendation-handoff) · [Validation](#validation) · [Done](#definition-of-done) · [Rollback](#rollback-and-correction)

> [!IMPORTANT]
> PromotionDecision shape validation is executable. Promotion policy evaluation, support resolution, accountable review, lifecycle transition, ReleaseManifest readiness, and publication are not established.

> [!CAUTION]
> `APPROVE` is not `PUBLISHED`.

---

<a id="purpose"></a>

## Purpose

The feature should help an authorized reviewer determine:

- which candidate and run are under review;
- which lifecycle boundary is proposed;
- whether PromotionDecision shape is valid;
- whether evidence, validation, policy, review, rollback, correction, and manifest support resolve;
- whether rights, sensitivity, source role, and freshness are closed;
- which bounded recommendation may be sent to an external governed recorder;
- why the candidate remains held when closure is incomplete.

It must not infer readiness from path existence, a green CI check, a smoke record, a dashboard, or a merged branch.

[Back to top](#top)

---

<a id="current-evidence"></a>

## Current evidence

| Surface | Status | Safe conclusion |
|---|---:|---|
| Feature lane | README-only in bounded search | No UI implementation is established. |
| Review Console package | Placeholder | Private `0.0.0`; no scripts or dependencies. |
| PromotionDecision schema | Executable shape boundary | Closed required shape; `APPROVE`, `DENY`, `ABSTAIN`. |
| Validator and fixture test | Executable | JSON Schema fixture validation only. |
| Promotion policy | Non-enforcing stubs | No real active rules. |
| Promotion-gate validator | Placeholder | No semantic gate implementation. |
| ReviewRecord validator | Placeholder | No accountable-review enforcement. |
| Hydrology promoter | Stub | Hard-codes `APPROVE`. |
| Hydrology smoke record | Tracked, unresolved | Automation review; evidence and rollback paths unresolved. |
| Promotion-gate workflow | Read-only hold | Proves scaffold remains held; does not promote. |
| ReleaseManifest schema | Thin | Only `id` required; readiness is not enforced. |
| RollbackCard schema | Thin | Only `id` required; rollback readiness is not enforced. |
| Governed API DTO | Not established | No accepted feature data source or write handoff. |

```text
shape validation       = executable
policy evaluation      = not established
support resolution     = not established
accountable review     = not established
lifecycle transition   = held
manifest readiness     = not established
publication            = not authorized
```

[Back to top](#top)

---

<a id="authority-boundary"></a>

## Authority boundary

Directory Rules place presentation and interaction under `apps/`. Other authorities remain separate:

| Responsibility | Owning root |
|---|---|
| Feature projection and bounded handoff | `apps/review-console/` |
| Public/elevated trusted API | `apps/governed-api/` |
| Object meaning | `contracts/release/` |
| Machine shape | `schemas/contracts/v1/` |
| Promotion and release policy | `policy/promotion/`, `policy/release/` |
| Validation and tests | `tools/validators/`, `tests/`, `fixtures/` |
| Evidence, proofs, and receipts | governed evidence/data roots |
| Actual promotion records | `release/promotion_decisions/` |
| Lifecycle execution | `pipelines/` |
| Release and publication authority | `release/` |

The feature must not create governed records, write lifecycle or release files, invoke domain promoters, expose canonical/internal stores, or publish/repoint aliases.

[Back to top](#top)

---

<a id="hydrology-smoke-path"></a>

## Hydrology smoke path

The current hydrology promoter writes a schema-shaped decision with hard-coded `APPROVE`, reviewer `automation-smoke`, ticket `REL-SMOKE`, and path-shaped evidence and rollback references.

The promotion-gate workflow confirms those support paths are unresolved and deliberately does not execute the promoter.

A future UI must show:

```text
SHAPE_VALID
SMOKE_ARTIFACT
POLICY_UNEVALUATED
SUPPORT_UNRESOLVED
REVIEW_NOT_ESTABLISHED
TRANSITION_HELD
NOT_RELEASED
```

It must not show `PROMOTED`, `READY TO PUBLISH`, or `PUBLISHED`.

[Back to top](#top)

---

<a id="decision-and-state-axes"></a>

## Decision and state axes

| Axis | Current values |
|---|---|
| PromotionDecision | `APPROVE`, `DENY`, `ABSTAIN` |
| Release operational outcome | promote-to-manifest, evidence/validation/policy holds, repair, supersede, no action |
| ReviewRecord | `approve`, `reject`, `request_changes` |
| PolicyDecision | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` |
| Release state | draft, review, held, manifest-ready, approved, released, corrected, superseded, withdrawn |
| UI state | loading, ready, blocked, denied, abstained, stale, restricted, malformed, unavailable, error |
| Recommendation intent | recommend route/hold/repair/deny/escalate or request evidence |

Do not silently map one axis onto another. Unknown values fail closed. Normalization requires a versioned tested adapter or accepted ADR.

[Back to top](#top)

---

<a id="readiness-closure"></a>

## Readiness closure

A promotion recommendation requires explicit status for candidate identity and lifecycle state, source identity and role, validation, EvidenceRef-to-EvidenceBundle resolution, policy, rights and sensitivity, review and separation of duties, PromotionDecision freshness, rollback target, correction path, ReleaseManifest readiness, proofs/receipts, and public-safe derivatives.

Readiness levels remain separate:

```text
SHAPE_VALID
SUPPORT_RESOLVED
REVIEW_READY
RECOMMENDATION_ELIGIBLE
TRANSITION_AUTHORIZED
READY_FOR_MANIFEST
RELEASED
```

No level implies the next.

[Back to top](#top)

---

<a id="recommendation-handoff"></a>

## Recommendation handoff

A future handoff may send a candidate reference, bounded proposed action, reviewer-context reference, safe rationale code, supporting references, and concurrency token to an external governed recorder.

The server must reauthorize, revalidate freshness and support, apply policy and separation of duties, enforce idempotency, create authoritative records outside the feature, and return authoritative state.

The feature must never invoke `pipelines/domains/hydrology/promote.py` or write under `release/promotion_decisions/`.

[Back to top](#top)

---

<a id="validation"></a>

## Validation

Current executable proof is limited to PromotionDecision shape fixtures and CI assertions that the broader runtime remains held.

Minimum future negative cases include unauthorized access; missing, invalid, stale, or superseded candidates and decisions; unresolved or mismatched evidence; failed validation; unevaluated, denied, abstained, errored, or stale policy; missing/conflicted review; missing/invalid rollback or correction; incomplete manifest; hard-coded smoke `APPROVE`; invalid hydrology ID; extra fields; cross-candidate reference substitution; duplicate/stale recommendations; safe API errors; and cache purge after logout or role change.

Required proof layers include schema, semantic validator, policy, evidence resolution, review separation, rollback/correction, release manifest, API, component, accessibility, security, integration, and end-to-end tests.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

- [ ] Owners and recursive feature inventory are confirmed.
- [ ] Decision and state vocabularies are reconciled.
- [ ] PromotionDecision authority/version is accepted.
- [ ] Real promotion policy is tested.
- [ ] Hard-coded `APPROVE` is removed or disabled.
- [ ] Evidence, validation, policy, review, rollback, correction, and manifest references resolve.
- [ ] Promotion and ReviewRecord semantic validators exist.
- [ ] ReleaseManifest and RollbackCard readiness is machine-checkable.
- [ ] Governed API projection and server-revalidated handoff are tested.
- [ ] Feature performs no local lifecycle or release writes.
- [ ] Negative, sensitive, stale, accessibility, and security paths pass.
- [ ] Safe disablement, correction, supersession, and rollback are documented.
- [ ] CI proves held, deny, abstain, error, and eligible paths.
- [ ] Documentation claims remain bounded to executable proof.

[Back to top](#top)

---

<a id="rollback-and-correction"></a>

## Rollback and correction

Before merge, close the draft PR or reset/delete the scoped branch.

After merge, revert the generated receipt and README commits—or revert the PR merge—and restore prior blob `eee28922e3e74019fd2d35a2a03da3f9cd9c81ef`.

A future feature must allow recommendations to be disabled while retaining safe read-only state. Disabling the UI must not mutate governed objects.

A wrong or stale PromotionDecision is corrected by a new governed decision or supersession record, never by editing history in place.

The previous v0.1 README was substantive. This revision preserves its no-publication, no-file-move, evidence, policy, review, rollback, and correction boundaries while grounding them in current repository evidence.

[Back to top](#top)

---

## Status summary

PromotionDecision shape validation is executable. Promotion authorization, policy evaluation, support resolution, accountable review, lifecycle transition, manifest readiness, and publication remain held or unverified. The tracked hydrology `APPROVE` record must remain visibly labeled as an unresolved smoke artifact.
