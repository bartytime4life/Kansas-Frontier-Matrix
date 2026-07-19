<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://app/review-console/src/features/promotion/readme
title: Review Console Promotion — Governed Readiness Boundary
type: app-readme; directory-readme; feature-boundary
version: v0.2
status: draft; repository-grounded; shape-validation-executable; promotion-held; feature-not-implemented
owners: OWNER_TBD — Review steward · Promotion steward · Release steward · Policy steward · Evidence steward · Security steward · API steward · UI steward · Validation steward · Docs steward
created: 2026-06-16
updated: 2026-07-19
policy_label: "restricted-review; role-gated; evidence-bound; release-subordinate; no-local-promotion; no-file-move; no-publication-authority"
current_path: apps/review-console/src/features/promotion/README.md
owning_root: apps/
responsibility: define the app-local promotion-readiness projection and bounded recommendation handoff without creating or mutating PromotionDecision, ReviewRecord, PolicyDecision, ReleaseManifest, RollbackCard, lifecycle state, release records, evidence, policy, receipts, proofs, or published artifacts
truth_posture: CONFIRMED existing v0.1 README, executable PromotionDecision shape validation, hydrology fixtures, hard-coded APPROVE promoter stub, unresolved smoke record, read-only promotion-gate hold, policy stubs, placeholder semantic validators, and thin ReleaseManifest and RollbackCard schemas / PROPOSED governed UI projection and recommendation handoff / CONFLICTED promotion, review, policy, release, and UI vocabularies / UNKNOWN authoritative API, evaluator, writer, cross-domain runtime, deployment, and full-suite state
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
  - ../../../../../pipelines/domains/hydrology/promote.py
  - ../../../../../release/promotion_decisions/hydrology/run-local-smoke.json
  - ../../../../../.github/workflows/promotion-gate.yml
tags: [kfm, apps, review-console, promotion, release-readiness, evidence, policy, review, rollback, fail-closed]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Review Console Promotion

`apps/review-console/src/features/promotion/`

> Role-gated promotion-readiness view and bounded recommendation handoff. It must not promote, publish, move lifecycle files, write release records, execute policy in the browser, or treat schema-valid `APPROVE` as release authority.

![status](https://img.shields.io/badge/status-draft-yellow)
![shape](https://img.shields.io/badge/shape-validation__executable-green)
![runtime](https://img.shields.io/badge/promotion-held-orange)
![authority](https://img.shields.io/badge/authority-review__support__only-critical)

[Purpose](#purpose) · [Evidence](#current-evidence) · [Authority](#authority-boundary) · [Smoke](#hydrology-smoke-path) · [Axes](#decision-and-state-axes) · [Readiness](#readiness-closure) · [Validation](#validation) · [Done](#definition-of-done) · [Rollback](#rollback-and-correction)

> [!IMPORTANT]
> PromotionDecision shape validation is executable. Policy evaluation, support resolution, accountable review, lifecycle transition, manifest readiness, and publication are not established.

> [!CAUTION]
> `APPROVE` is not `PUBLISHED`.

---

<a id="purpose"></a>

## Purpose

The feature should show which candidate and run are under review, the proposed lifecycle boundary, PromotionDecision shape state, evidence and policy closure, review and separation-of-duty posture, rollback and correction readiness, manifest readiness, freshness, safe blockers, and the bounded recommendation permitted for the current reviewer.

It must not infer readiness from a path, green CI check, smoke record, dashboard, or merged branch.

[Back to top](#top)

---

<a id="current-evidence"></a>

## Current evidence

| Surface | Status | Safe conclusion |
|---|---:|---|
| Feature lane | README-only in bounded search | No UI implementation is established. |
| Review Console package | Placeholder | Private `0.0.0`; no scripts or dependencies. |
| PromotionDecision schema | Executable shape boundary | Closed required shape; `APPROVE`, `DENY`, `ABSTAIN`. |
| Validator and fixture test | Executable | JSON Schema shape validation only. |
| Promotion policy | Non-enforcing stubs | No real active rules. |
| Promotion-gate validator | Placeholder | No semantic gate. |
| ReviewRecord validator | Placeholder | No accountable-review enforcement. |
| Hydrology promoter | Stub | Hard-codes `APPROVE`. |
| Hydrology smoke record | Unresolved | Automation review; evidence and rollback refs unresolved. |
| Promotion-gate workflow | Read-only hold | Proves scaffold remains held; does not promote. |
| ReleaseManifest/RollbackCard schemas | Thin | Only `id` required; readiness is not enforced. |
| Governed API DTO | Not established | No accepted data source or writer handoff. |

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

Directory Rules keep presentation under `apps/`; object meaning under `contracts/`; shape under `schemas/`; policy under `policy/`; evidence, proofs, and receipts under their governed roots; executable lifecycle logic under `pipelines/`; and release/publication authority under `release/`.

The feature may render governed projections and submit a recommendation intent to an external recorder. It must not create governed records, write lifecycle or release files, invoke domain promoters, expose canonical/internal stores, or publish/repoint aliases.

[Back to top](#top)

---

<a id="hydrology-smoke-path"></a>

## Hydrology smoke path

The hydrology promoter writes hard-coded `APPROVE` with reviewer `automation-smoke`, ticket `REL-SMOKE`, and path-shaped evidence and rollback refs. The promotion-gate workflow confirms those refs do not resolve and deliberately does not execute the promoter.

Required UI state:

```text
SHAPE_VALID
SMOKE_ARTIFACT
POLICY_UNEVALUATED
SUPPORT_UNRESOLVED
REVIEW_NOT_ESTABLISHED
TRANSITION_HELD
NOT_RELEASED
```

Never show `PROMOTED`, `READY TO PUBLISH`, or `PUBLISHED` for this record.

[Back to top](#top)

---

<a id="decision-and-state-axes"></a>

## Decision and state axes

| Axis | Current values |
|---|---|
| PromotionDecision | `APPROVE`, `DENY`, `ABSTAIN` |
| Release operational outcome | promote-to-manifest, hold, repair, supersede, no action |
| ReviewRecord | `approve`, `reject`, `request_changes` |
| PolicyDecision | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` |
| Release state | draft, review, held, manifest-ready, approved, released, corrected, superseded, withdrawn |
| UI state | loading, ready, blocked, denied, abstained, stale, restricted, malformed, unavailable, error |

Do not silently map one axis onto another. Unknown values fail closed. Normalization requires a versioned tested adapter or accepted ADR.

[Back to top](#top)

---

<a id="readiness-closure"></a>

## Readiness closure

Promotion review requires explicit candidate/lifecycle identity, source role, validation, EvidenceRef-to-EvidenceBundle resolution, policy, rights and sensitivity, review and separation, current PromotionDecision, rollback target, correction path, ReleaseManifest readiness, proofs/receipts, and public-safe derivatives.

```text
SHAPE_VALID
SUPPORT_RESOLVED
REVIEW_READY
RECOMMENDATION_ELIGIBLE
TRANSITION_AUTHORIZED
READY_FOR_MANIFEST
RELEASED
```

No level implies the next. The server must reauthorize and revalidate all support before any recommendation handoff; the feature must never invoke the hydrology promoter or write under `release/promotion_decisions/`.

[Back to top](#top)

---

<a id="validation"></a>

## Validation

Current executable proof is limited to PromotionDecision shape fixtures and CI assertions that the broader runtime remains held.

Future negative coverage must include unauthorized access; invalid, stale, missing, or superseded decisions; unresolved/mismatched evidence; validation failure; unevaluated/deny/abstain/error policy; review conflict; missing rollback/correction; incomplete manifest; hard-coded smoke `APPROVE`; invalid hydrology ID; extra fields; cross-candidate substitution; duplicate/stale recommendation; safe API failure; and protected-cache purge.

Required proof layers: schema, semantic validator, policy, evidence resolution, review separation, rollback/correction, release manifest, API, component, accessibility, security, integration, and end-to-end tests.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

- [ ] Owners, feature inventory, and vocabulary mappings are confirmed.
- [ ] Real promotion policy and semantic validators exist.
- [ ] Hard-coded `APPROVE` is removed or disabled.
- [ ] Evidence, validation, policy, review, rollback, correction, and manifest refs resolve.
- [ ] ReleaseManifest and RollbackCard readiness is machine-checkable.
- [ ] Governed API projection and server-revalidated handoff are tested.
- [ ] Feature performs no local lifecycle or release writes.
- [ ] Negative, sensitive, stale, accessibility, and security paths pass.
- [ ] Safe disablement, correction, supersession, and rollback are documented.
- [ ] Documentation claims remain bounded to executable proof.

[Back to top](#top)

---

<a id="rollback-and-correction"></a>

## Rollback and correction

Before merge, close the draft PR or reset/delete the scoped branch. After merge, revert the receipt and README commits—or revert the PR merge—and restore prior blob `eee28922e3e74019fd2d35a2a03da3f9cd9c81ef`.

A future feature must allow recommendation actions to be disabled while retaining safe read-only state. A wrong or stale PromotionDecision is corrected by a new governed decision or supersession record, never by editing history in place.

[Back to top](#top)

---

## Status summary

PromotionDecision shape validation is executable. Promotion authorization, policy evaluation, support resolution, accountable review, lifecycle transition, manifest readiness, and publication remain held or unverified. The hydrology `APPROVE` record is an unresolved smoke artifact, not release authority.
