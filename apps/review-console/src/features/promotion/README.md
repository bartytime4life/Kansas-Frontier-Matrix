<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://app/review-console/src/features/promotion/readme
title: Review Console Promotion — Governed Readiness Projection and Recommendation-Handoff Boundary
type: app-readme; directory-readme; feature-boundary; promotion-review-support
version: v0.2
status: draft; repository-grounded; readme-only-direct-lane; schema-validator-executable; promotion-runtime-held; policy-stubs-non-enforcing; hydrology-smoke-artifact; executable-feature-not-established
owners: OWNER_TBD — Review steward · Promotion steward · Release steward · Governance steward · Security steward · Policy steward · Evidence steward · Source steward · Rights steward · Sensitivity reviewer · API steward · UI steward · Validation steward · Docs steward
created: 2026-06-16
updated: 2026-07-19
policy_label: "public-governance; restricted-review; promotion-review-support; role-gated; evidence-bound; release-subordinate; no-local-promotion; no-file-move; no-publication-authority; no-truth-authority"
current_path: apps/review-console/src/features/promotion/README.md
owning_root: apps/
responsibility: document the app-local promotion-review feature boundary for displaying governed candidate readiness, PromotionDecision shape and status, evidence and policy closure, review and separation-of-duty posture, rollback and correction readiness, release-manifest readiness, and a typed external recommendation handoff without creating or mutating PromotionDecision, ReviewRecord, PolicyDecision, ReleaseManifest, RollbackCard, lifecycle state, published artifacts, policy, evidence, proofs, receipts, or canonical audit history
truth_posture: CONFIRMED target README and prior v0.1 contract, Review Console parent boundaries, private version 0.0.0 package manifest with no scripts or dependencies, bounded direct-lane search surfacing only this README, schema-paired PromotionDecision contract with closed eleven-field shape and APPROVE/DENY/ABSTAIN vocabulary, executable PromotionDecision JSON Schema validator and fixture test, valid and invalid hydrology fixtures, hydrology promoter stub that hard-codes APPROVE, tracked hydrology automation-smoke decision whose evidence and rollback paths remain unresolved, read-only promotion-gate workflow that explicitly holds implementation and does not execute the promoter, promotion policy files that declare greenfield stubs with no real rules, placeholder promotion-gate and ReviewRecord validators, thin permissive ReleaseManifest and RollbackCard schemas, release promotion-decision lane, current ReviewRecord and PolicyDecision vocabularies, and absence of overlapping open PR/branch work / PROPOSED governed promotion-review projection, explicit readiness axes, support-resolution matrix, safe recommendation handoff, deterministic identity and time semantics, stale-policy handling, field minimization, security controls, negative fixtures, staged implementation, correction and rollback behavior, and safe disablement / CONFLICTED PromotionDecision APPROVE/DENY/ABSTAIN vocabulary versus release/promotion_decisions PROMOTE_TO_MANIFEST and HOLD/REPAIR outcomes, ReviewRecord approve/reject/request_changes vocabulary versus feature action labels, PolicyDecision ANSWER/ABSTAIN/DENY/ERROR vocabulary versus promotion decisions, schema-valid hydrology smoke APPROVE versus unresolved support references and workflow hold, minimal PromotionDecision review binding versus richer ReviewRecord governance, and strong PromotionDecision schema versus thin ReleaseManifest and RollbackCard schemas / UNKNOWN recursive feature inventory, accepted promotion policy semantics, canonical evaluator/writer, governed API route and DTO, real review records, support-reference resolution service, cross-domain promotion implementation, branch protection, deployment, telemetry, and current full-suite pass state / NEEDS VERIFICATION owners, vocabulary reconciliation, policy fail-closed rules, replacement of hard-coded APPROVE, hardened release-manifest and rollback schemas, resolvable evidence and rollback refs, review separation, release handoff, feature source, tests, accessibility, observability, receipts/proofs, correction, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  visibility: public
  base_ref: main
  base_commit: 2783739bba744f560772388a9969ed3107d08930
  prior_blob: eee28922e3e74019fd2d35a2a03da3f9cd9c81ef
  inventory_method: GitHub connector exact reads plus bounded code, branch, and open-PR searches
  bounded_direct_lane_result: promotion feature search surfaced this README only; recursive enumeration remains NEEDS VERIFICATION
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../audit_log/README.md
  - ../correction/README.md
  - ../rollback/README.md
  - ../../../../governed-api/README.md
  - ../../../../../docs/architecture/ui/REVIEW_CONSOLE.md
  - ../../../../../docs/architecture/directory-rules.md
  - ../../../../../contracts/release/promotion_decision.md
  - ../../../../../contracts/release/release_manifest.md
  - ../../../../../contracts/release/rollback_card.md
  - ../../../../../contracts/governance/ReviewRecord.md
  - ../../../../../schemas/contracts/v1/release/promotion_decision.schema.json
  - ../../../../../schemas/contracts/v1/release/release_manifest.schema.json
  - ../../../../../schemas/contracts/v1/release/rollback_card.schema.json
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
  - ../../../../../release/README.md
  - ../../../../../.github/workflows/promotion-gate.yml
tags: [kfm, apps, review-console, promotion, promotion-decision, release-readiness, evidence-closure, policy, review, rollback, correction, manifest, fail-closed, no-file-move]
notes:
  - "v0.2 preserves the existing path and replaces generic greenfield language with current repository evidence."
  - "PromotionDecision shape validation is executable; promotion policy evaluation, support-reference resolution, accountable review, lifecycle transition, release-manifest emission, and publication remain explicitly held."
  - "The tracked hydrology smoke decision is a schema-shaped automation artifact with unresolved support references and is not promotion authority."
  - "This update changes documentation and its generated-work receipt only."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Review Console Promotion

`apps/review-console/src/features/promotion/`

> App-local, role-gated **promotion-readiness review** boundary. It may display governed candidate context, validate that required references and decision records are present, and hand a bounded reviewer recommendation to an external governed recorder. It must never promote by moving files, execute policy locally, write release records, treat a schema-valid object as governance-ready, or convert an `APPROVE` smoke record into publication authority.

![status](https://img.shields.io/badge/status-draft-yellow)
![version](https://img.shields.io/badge/version-v0.2-informational)
![feature](https://img.shields.io/badge/feature-README--only-lightgrey)
![shape](https://img.shields.io/badge/PromotionDecision-shape__validated-green)
![runtime](https://img.shields.io/badge/promotion-runtime__held-orange)
![authority](https://img.shields.io/badge/authority-review__support__only-critical)
![default](https://img.shields.io/badge/default-fail__closed-critical)

**Quick links:** [Purpose](#purpose) · [Current evidence](#current-repository-evidence) · [Authority](#authority-and-directory-rules-basis) · [Hydrology smoke](#hydrology-smoke-path) · [Decision axes](#separate-decision-and-state-axes) · [Readiness](#promotion-readiness-closure) · [Read model](#proposed-governed-read-model) · [Handoff](#recommendation-handoff) · [Security](#access-sensitivity-and-security) · [Tests](#validation-and-negative-paths) · [Implementation](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Rollback](#rollback-correction-and-supersession)

> [!IMPORTANT]
> **Observed maturity:** the feature lane itself is README-only in the bounded search. PromotionDecision JSON Schema validation and its fixture test are executable. The broader promotion gate is intentionally held: policy files contain no real rules, the dedicated gate validator is a placeholder, release review records are not established for the tracked smoke decision, and CI does not execute the hydrology promoter.

> [!CAUTION]
> `APPROVE` is not `PUBLISHED`. A schema-valid `PromotionDecision` is not evidence closure, policy approval, reviewer independence, rollback readiness, manifest readiness, lifecycle transition, release approval, deployment, or public availability.

---

<a id="purpose"></a>

## Purpose

This feature should help an authorized reviewer answer:

1. What exact candidate or run is being evaluated?
2. Which lifecycle boundary is proposed?
3. Is the PromotionDecision object shape valid?
4. Do all evidence, policy, review, validation, rollback, correction, and release references resolve?
5. Is each supporting object current, compatible, and applicable to the same candidate?
6. Are rights, sensitivity, source role, and public-safe derivative conditions closed?
7. Does separation of duties apply, and is it satisfied?
8. Is the candidate merely reviewable, eligible for a governed recommendation, ready for manifest assembly, or actually released?
9. What safe action may the current reviewer recommend?
10. What blocks the next state when the feature must abstain, deny, or remain held?

The feature must not answer these questions by inference from a green badge, path existence, successful schema test, dashboard state, smoke output, branch merge, or file placement alone.

[Back to top](#top)

---

<a id="current-repository-evidence"></a>

## Current repository evidence

| Surface | Status | What is established | What is not established |
|---|---:|---|---|
| Target README | **CONFIRMED** | Existing v0.1 promotion feature boundary. | No implementation proof. |
| Other direct feature files | **NOT SURFACED IN BOUNDED SEARCH** | Search surfaced only this README. | Recursive absence is not proven. |
| Review Console package | **CONFIRMED PLACEHOLDER** | Private package, version `0.0.0`, no scripts or dependencies. | Runnable app or feature registration. |
| PromotionDecision contract | **CONFIRMED / PROPOSED** | Meaning, boundaries, and finite `APPROVE | DENY | ABSTAIN` vocabulary. | Policy execution or release transition. |
| PromotionDecision schema | **CONFIRMED / PROPOSED CLOSED SHAPE** | Eleven required top-level fields; nested review binding; `additionalProperties: false`; hydrology ID condition. | Evidence resolution, policy evaluation, reviewer independence, rollback validity, manifest readiness. |
| PromotionDecision validator | **CONFIRMED EXECUTABLE** | Runs JSON Schema against fixture lanes. | Full promotion-gate validation. |
| PromotionDecision test | **CONFIRMED EXECUTABLE** | Calls the validator with `--fixtures` and expects success. | Production runtime, policy, release, or UI proof. |
| PromotionDecision fixtures | **CONFIRMED MINIMUM CASES** | Valid hydrology `APPROVE`; invalid missing-evidence case; non-empty valid/invalid inventory in CI. | Complete outcome and security coverage. |
| Promotion policy README | **CONFIRMED STUB** | Declares greenfield bundle status. | Accepted policy semantics. |
| Promotion Rego files | **CONFIRMED NON-ENFORCING STUBS** | Files exist; comments describe examples; no real rules are active. | Evidence, rollback, rights, sensitivity, or review enforcement. |
| Promotion-gate validator | **CONFIRMED PLACEHOLDER** | File exists and raises `NotImplementedError`. | Executable gate. |
| ReviewRecord validator | **CONFIRMED PLACEHOLDER** | CI expects the placeholder state. | Accountable review validation. |
| Hydrology promoter | **CONFIRMED STUB** | Writes a hard-coded `APPROVE` PromotionDecision. | Evaluation of evidence, policy, review, rollback, or release readiness. |
| Tracked hydrology smoke decision | **CONFIRMED** | Schema-shaped `APPROVE` record with automation reviewer. | Resolvable evidence or rollback support, human review, release authority. |
| Promotion-gate workflow | **CONFIRMED READ-ONLY HOLD** | Runs schema/fixture checks, confirms unresolved smoke refs and placeholders, does not execute promoter, emits summaries only. | Promotion, manifest emission, release, publication. |
| ReleaseManifest contract/schema | **CONFIRMED THIN PAIR** | Semantic target plus schema requiring only `id` and allowing extra fields. | Production manifest completeness. |
| RollbackCard contract/schema | **CONFIRMED THIN PAIR** | Semantic target plus schema requiring only `id` and allowing extra fields. | Valid rollback target or executable rollback. |
| Release promotion-decision lane | **CONFIRMED** | Release-root index and hydrology record lane. | Vocabulary reconciliation with PromotionDecision schema. |
| Governed API promotion route/DTO | **NOT ESTABLISHED** | No accepted route was verified. | Feature data source and mutation handoff. |
| Feature-specific tests | **NOT SURFACED** | No promotion UI test was established. | Rendering, access, accessibility, or handoff proof. |

### Evidence posture

```text
PromotionDecision shape validation = executable
Promotion policy evaluation        = not established
Support-reference resolution       = not established
Accountable review validation      = not established
Lifecycle transition               = held
ReleaseManifest readiness          = not established
Publication                        = not authorized
```

[Back to top](#top)

---

<a id="authority-and-directory-rules-basis"></a>

## Authority and Directory Rules basis

This path is an app-local presentation and recommendation-handoff lane.

| Responsibility | Owning root |
|---|---|
| Feature presentation and safe interaction | `apps/review-console/src/features/promotion/` |
| Trusted API projection | `apps/governed-api/` |
| PromotionDecision, ReleaseManifest, RollbackCard meaning | `contracts/release/` |
| Machine shape | `schemas/contracts/v1/` |
| Promotion/release policy | `policy/promotion/`, `policy/release/` |
| Validators and tests | `tools/validators/`, `tests/` |
| Evidence, proofs, and receipts | governed evidence/data roots |
| Actual promotion-decision records | `release/promotion_decisions/` |
| Release binding and publication decisions | `release/` |
| Lifecycle execution | `pipelines/` |

The feature may render governed projections, show unresolved support, compare shape state with closure state, and collect a bounded recommendation intent.

It must not:

- create or edit PromotionDecision, ReviewRecord, PolicyDecision, ReleaseManifest, or RollbackCard;
- execute authoritative policy in the browser;
- write release, proof, receipt, evidence, or lifecycle files;
- move files between lifecycle directories;
- invoke the hydrology promoter;
- treat fixture, smoke, CI, or schema success as approval;
- expose canonical/internal or restricted stores;
- publish or repoint public aliases.

[Back to top](#top)

---

<a id="hydrology-smoke-path"></a>

## Hydrology smoke path

The current hydrology promoter is explicitly a stub. It writes a hard-coded `APPROVE` record with automation review, path-shaped evidence/rollback refs, and a policy-bundle identifier.

The promotion-gate workflow confirms that:

- `APPROVE` remains hard-coded;
- reviewer remains `automation-smoke`;
- evidence and rollback paths are unresolved;
- accountable release review is absent;
- broader gate and ReviewRecord validators are placeholders;
- CI must not execute the promoter.

### Required UI treatment

```text
SHAPE_VALID
SMOKE_ARTIFACT
SUPPORT_UNRESOLVED
REVIEW_NOT_ESTABLISHED
POLICY_NOT_EVALUATED
TRANSITION_HELD
NOT_RELEASED
```

Forbidden labels include `APPROVED FOR RELEASE`, `READY TO PUBLISH`, `PROMOTED`, and `PUBLISHED`.

```text
decision == APPROVE
and schema_valid == true
and support_resolution == incomplete
therefore
promotion_state == HELD
```

[Back to top](#top)

---

<a id="promotiondecision-shape"></a>

## Current PromotionDecision shape

| Field | Required | Current shape |
|---|---:|---|
| `id` | yes | non-empty; hydrology pattern when applicable |
| `version` | yes | exactly `v1` |
| `domain` | yes | non-empty |
| `run_id` | yes | non-empty |
| `decision` | yes | `APPROVE`, `DENY`, `ABSTAIN` |
| `evidence_ref` | yes | non-empty reference string |
| `evidence_bundle_uri` | yes | non-empty reference string |
| `rollback_card_uri` | yes | non-empty reference string |
| `policy_bundle` | yes | non-empty identifier |
| `decided_at` | yes | date-time |
| `review` | yes | closed object: `reviewer`, `ticket` |

`additionalProperties` is false. Several required fields are references, not proof of resolution.

Schema validation does not establish support resolution, policy execution, reviewer authority/independence, ticket validity, freshness, candidate validation, rights/sensitivity closure, manifest completeness, lifecycle transition, or release.

The nested review binding is not a full ReviewRecord. Where a full ReviewRecord is required, the feature must show both objects separately.

[Back to top](#top)

---

<a id="separate-decision-and-state-axes"></a>

## Separate decision and state axes

| Axis | Current vocabulary |
|---|---|
| PromotionDecision | `APPROVE`, `DENY`, `ABSTAIN` |
| Release operational outcome | `PROMOTE_TO_MANIFEST`, evidence/validation/policy holds, `REPAIR_REQUIRED`, `SUPERSEDE_CANDIDATE`, `NO_ACTION` |
| ReviewRecord | `approve`, `reject`, `request_changes` |
| PolicyDecision | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` |
| Release state | `DRAFT`, `READY_FOR_REVIEW`, `HELD`, `READY_FOR_MANIFEST`, `APPROVED`, `RELEASED`, `CORRECTED`, `SUPERSEDED`, `WITHDRAWN`, `NO_ACTION` |
| UI state | `loading`, `ready`, `blocked`, `denied`, `abstained`, `stale`, `malformed`, `unavailable`, `error` |
| Recommendation intent | `recommend_route`, `recommend_hold`, `recommend_repair`, `recommend_deny`, `recommend_escalate`, `request_evidence` |

Do not silently normalize these vocabularies. Mapping requires a versioned tested adapter or accepted ADR. Unknown values fail closed.

[Back to top](#top)

---

<a id="promotion-readiness-closure"></a>

## Promotion readiness closure

| Closure family | Required posture | Failure posture |
|---|---|---|
| Candidate identity/lifecycle | exact run, domain, current state, intended boundary | block |
| Source identity/role | resolvable source role; no upcast | deny/abstain |
| Validation | applicable current reports/receipts | hold |
| Evidence | EvidenceRef resolves to compatible EvidenceBundle | abstain |
| Policy | evaluated versioned policy and PolicyDecision | deny/abstain/error |
| Rights/sensitivity | rights, consent, sovereignty, privacy, redaction/generalization resolved | deny/hold |
| Review | authorized role, ticket, ReviewRecord and separation where required | hold |
| PromotionDecision | valid, candidate-bound, fresh, current | hold |
| Rollback | resolvable valid RollbackCard/target | hold |
| Correction | named correction/public-notice path | hold |
| Manifest Meaning | Authority effect |
|---|---|---|
| `SHAPE_VALID` | PromotionDecision passes JSON Schema. | none |
| `SUPPORT_RESOLVED` | Required refs resolve and bind to candidate. | none |
| `REVIEW_READY` | Enough context exists for assessment. | none |
| `RECOMMENDATION_ELIGIBLE` | Current role may submit external intent. | handoff only |
| `TRANSITION_AUTHORIZED` | Governed evaluator authorizes transition. | not release |
| `READY_FOR_MANIFEST` | Release authority permits manifest assembly. | not published |
| `RELEASED` | Governed release and alias binding complete. | public effect as allowed |

[Back to top](#top)

---

<a id="proposed-governed-read-model"></a>

## Proposed governed read model

No accepted Review Console promotion DTO was established. A future versioned server projection should carry candidate identity, PromotionDecision shape/currentness, separate closure states for evidence, validation, policy, review, rollback, correction, manifest, proofs and receipts, explicit operational readiness, safe reasons, and permitted actions.

Rules:

- status comes from authoritative records or governed resolvers;
- a path-shaped string is never treated as resolved;
- missing sections are not success;
- unknown enums block;
- fields are minimized by role and sensitivity;
- cache keys include candidate, role/audience, projection version, policy, and release context;
- logout, role change, candidate change, supersession, correction, and policy refresh invalidate protected cache.

[Back to top](#top)

---

<a id="recommendation-handoff"></a>

## Recommendation handoff

The feature is not the PromotionDecision writer. A future handoff may submit candidate ref, bounded proposed action, reviewer-context ref, safe rationale code, supporting refs, and an optimistic concurrency token.

The governed recorder must revalidate authorization, freshness, policy, candidate binding, support refs, and separation of duties; return a finite authoritative response; create any PromotionDecision or ReviewRecord outside the feature; and reject duplicate or stale submissions safely.

The feature must not invoke `pipelines/domains/hydrology/promote.py`, write under `release/promotion_decisions/`, call filesystem mutation endpoints, create ReleaseManifest, repoint aliases, execute pipeline transitions, or bypass release authority.

[Back to top](#top)

---

<a id="access-sensitivity-and-security"></a>

## Access, sensitivity, and security

Promotion review may expose unreleased artifacts, policy reasons, reviewer identities, source limitations, exact sensitive locations, rights disputes, living-person data, archaeology, rare species, infrastructure, or internal paths.

Minimum controls:

- server-side role and item authorization;
- deny-by-default field projection;
- no direct lifecycle-store or raw EvidenceBundle access;
- no secret, token, internal path, stack trace, or policy-source leakage;
- safe reason summaries separated from restricted details;
- export/copy restrictions;
- role/audience-partitioned cache;
- stale and partial-data indicators;
- cross-candidate ref binding;
- concurrency and replay protection;
- accessible rendering without hidden privileged details.

| Threat | Required response |
|---|---|
| Forged `APPROVE` | verify provenance/authority or mark untrusted |
| Unresolved path | never mark resolved |
| Browser edits authority fields | server ignores them |
| Role downgrade | purge cache and reauthorize |
| Candidate changes | reject stale token |
| Unknown enum | block safely |
| Sensitive reason | show safe code/summary only |
| Cross-candidate ref | reject binding mismatch |
| Smoke artifact shown as release | label smoke/held/not released |
| Policy stub shown as allow | display `POLICY_UNEVALUATED` |
| `id`-only manifest shown ready | display `MANIFEST_INCOMPLETE` |

[Back to top](#top)

---

<a id="validation-and-negative-paths"></a>

## Validation and negative paths

### Current executable proof

| Check | Status | Proven scope |
|---|---:|---|
| PromotionDecision schema validator | executable | shape only |
| PromotionDecision fixture test | executable | fixture runner succeeds |
| Workflow fixture inventory | executable | non-empty sets and pinned metadata |
| Hydrology smoke hold assertions | executable | stub, unresolved refs, absent review, placeholders |
| Promotion policy | not established | no real rules |
| Gate validator | placeholder | no gate semantics |
| ReviewRecord validator | placeholder | no review validation |
| Support resolver | not established | no closure proof |
| UI tests | not surfaced | no feature proof |

Minimum negative coverage includes unauthorized or restricted access; missing/malformed/stale candidate or decision; unresolved/mismatched evidence; failed/missing validation; unevaluated/deny/abstain/error/stale policy; missing/conflicted review; missing/invalid rollback or correction; incomplete/mismatched manifest; missing proofs; superseded decision; hard-coded smoke `APPROVE`; extra property; invalid hydrology ID; cross-candidate substitution; duplicate/replayed intent; API failure; safe errors; and cache purge on logout or role change.

Required proof layers include schema, semantic validator, policy, evidence resolution, review/separation, rollback/correction, release manifest, API contract, component, accessibility, security-negative, integration, and end-to-end held/deny/abstain/error/recommendation paths.

[Back to top](#top)

---

<a id="smallest-sound-implementation-sequence"></a>

## Smallest sound implementation sequence

1. Reconcile PromotionDecision, operational release, ReviewRecord, PolicyDecision, UI, and recommendation vocabularies.
2. Replace comment-only promotion policy with tested fail-closed rules.
3. Replace hard-coded hydrology `APPROVE` with governed evaluation or keep promoter disabled.
4. Resolve and candidate-bind evidence, rollback, review, policy, and validation refs.
5. Implement semantic promotion-gate validation beyond JSON shape.
6. Implement ReviewRecord validation and separation of duties.
7. Harden ReleaseManifest and RollbackCard beyond `id`-only schemas.
8. Define a versioned, authorized, minimized API projection.
9. Build read-only feature rendering with explicit axes.
10. Add typed handoff with server revalidation, concurrency, idempotency, and audit.
11. Add security, accessibility, observability, and cache controls.
12. Replace CI holds only after accepted implementation exists.
13. Document correction, supersession, safe disablement, and rollback.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

- [ ] Owners and feature inventory are confirmed.
- [ ] Vocabularies are reconciled and versioned.
- [ ] PromotionDecision contract/schema status is accepted.
- [ ] Promotion policy contains real tested rules.
- [ ] Hard-coded `APPROVE` is removed or promoter stays disabled.
- [ ] Evidence, rollback, review, policy, validation, and manifest refs resolve.
- [ ] Semantic PromotionDecision validator exists.
- [ ] ReviewRecord validation and separation exist.
- [ ] Manifest and rollback readiness are machine-checkable.
- [ ] Governed API projection is versioned, authorized, and minimized.
- [ ] Feature is read-only outside typed handoff.
- [ ] Handoff revalidates server-side and is idempotent.
- [ ] No local lifecycle or release writes exist.
- [ ] Negative, sensitive, stale, inaccessible, malformed, and error states are tested.
- [ ] Accessibility, observability, safe disablement, correction, and rollback are covered.
- [ ] CI proves positive and negative paths.
- [ ] Generated receipt and human review are complete.
- [ ] Documentation claims remain bounded to executable evidence.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| ID | Item | Status |
|---|---|---:|
| PROMO-UI-01 | Recursive feature inventory | NEEDS VERIFICATION |
| PROMO-UI-02 | Accepted PromotionDecision version/authority | NEEDS VERIFICATION |
| PROMO-UI-03 | Vocabulary reconciliation | CONFLICTED |
| PROMO-UI-04 | Real promotion policy | NEEDS VERIFICATION |
| PROMO-UI-05 | Hydrology promoter disposition | NEEDS VERIFICATION |
| PROMO-UI-06 | Evidence/rollback resolution | NEEDS VERIFICATION |
| PROMO-UI-07 | Semantic promotion-gate validator | NEEDS VERIFICATION |
| PROMO-UI-08 | ReviewRecord validation and records | NEEDS VERIFICATION |
| PROMO-UI-09 | ReleaseManifest completeness | NEEDS VERIFICATION |
| PROMO-UI-10 | RollbackCard completeness | NEEDS VERIFICATION |
| PROMO-UI-11 | Governed API route/DTO | UNKNOWN |
| PROMO-UI-12 | Recommendation recorder | UNKNOWN |
| PROMO-UI-13 | Cross-domain promotion behavior | UNKNOWN |
| PROMO-UI-14 | Rights/sensitivity rules | NEEDS VERIFICATION |
| PROMO-UI-15 | Branch protection/check requirements | UNKNOWN |
| PROMO-UI-16 | Deployment/telemetry | UNKNOWN |
| PROMO-UI-17 | Full-suite pass state | UNKNOWN |

[Back to top](#top)

---

<a id="rollback-correction-and-supersession"></a>

## Rollback, correction, and supersession

Before merge, close the draft PR or reset/delete the scoped branch. After merge, revert the generated receipt and README commits or revert the PR merge, then restore prior blob `eee28922e3e74019fd2d35a2a03da3f9cd9c81ef`.

A future feature should allow recommendation actions, individual panels, exports, cross-domain views, or the entire route to be disabled without mutating PromotionDecision, ReviewRecord, PolicyDecision, ReleaseManifest, RollbackCard, evidence, receipts, proofs, or release state.

A wrong or stale PromotionDecision is corrected by a new governed decision or supersession record, never by editing history in place.

The previous v0.1 README was substantive. This revision preserves its core boundaries while replacing generic uncertainty with current repository evidence and explicit conflicts.

[Back to top](#top)

---

## Status summary

PromotionDecision shape validation is executable. Promotion authorization, accountable review, policy evaluation, reference closure, lifecycle transition, ReleaseManifest readiness, and publication remain held or unverified.

**Current safe conclusion:** the tracked hydrology `APPROVE` smoke record is not release authority. It must remain visibly held until evidence, rollback, policy, review, validation, manifest, correction, and release dependencies are governed and resolved.
