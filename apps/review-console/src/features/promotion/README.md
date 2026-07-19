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

The most important current distinction is:

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

This path is correctly placed as an app-local feature lane because its responsibility is reviewer-facing presentation and bounded recommendation handoff.

```text
apps/review-console/src/features/promotion/
    presentation, interaction, safe state, recommendation handoff

contracts/release/
    PromotionDecision, ReleaseManifest, RollbackCard meaning

schemas/contracts/v1/
    machine-checkable shapes

policy/promotion/ and policy/release/
    admissibility and gate rules

tools/validators/ and tests/
    enforceability and regression proof

data/proofs/ and data/receipts/
    evidence/proof and process memory

release/promotion_decisions/
    actual promotion-decision records

release/manifests/ and release governance lanes
    release binding and publication decisions

pipelines/
    governed lifecycle execution

apps/governed-api/
    trusted API boundary
```

### Feature authority

The feature may:

- render governed projections;
- display missing, stale, incompatible, unresolved, denied, or restricted support;
- compare PromotionDecision shape state with external closure state;
- show release, rollback, correction, and review references;
- collect a bounded recommendation intent;
- submit that intent to an external governed recorder when implemented.

The feature must not:

- create or edit a PromotionDecision locally;
- run or embed policy as authoritative browser logic;
- write ReviewRecord, ReleaseManifest, RollbackCard, receipt, proof, or release files;
- move files between lifecycle directories;
- invoke the hydrology promoter directly;
- treat fixture, smoke, CI, or schema success as approval;
- expose raw, work, quarantine, canonical, restricted, or internal stores;
- publish or repoint public aliases.

[Back to top](#top)

---

<a id="hydrology-smoke-path"></a>

## Hydrology smoke path

The current hydrology promoter is explicitly a stub.

It generates:

- `domain: hydrology`;
- `decision: APPROVE`;
- an automation reviewer and smoke ticket;
- an EvidenceBundle path;
- a RollbackCard path;
- a policy bundle identifier;
- a tracked record under `release/promotion_decisions/hydrology/`.

The promotion-gate workflow intentionally proves that:

- the promoter still contains hard-coded `APPROVE`;
- the reviewer is still `automation-smoke`;
- the evidence-bundle path is unresolved;
- the rollback-card path is unresolved;
- no accountable release review record has appeared;
- the broader gate validator remains a placeholder;
- CI must not execute the promoter.

### Required UI treatment

A future feature must display the tracked record as:

```text
SHAPE_VALID
SMOKE_ARTIFACT
SUPPORT_UNRESOLVED
REVIEW_NOT_ESTABLISHED
POLICY_NOT_EVALUATED
TRANSITION_HELD
NOT_RELEASED
```

It must not display:

```text
APPROVED FOR RELEASE
READY TO PUBLISH
PROMOTED
PUBLISHED
```

### Promotion smoke anti-pattern

The following implication is forbidden:

```text
decision == APPROVE
therefore
promotion_ready == true
```

The safe relationship is:

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

The current closed schema requires:

| Field | Required | Current shape |
|---|---:|---|
| `id` | yes | non-empty string; hydrology-specific pattern when `domain == hydrology` |
| `version` | yes | exactly `v1` |
| `domain` | yes | non-empty string |
| `run_id` | yes | non-empty string |
| `decision` | yes | `APPROVE`, `DENY`, or `ABSTAIN` |
| `evidence_ref` | yes | non-empty string |
| `evidence_bundle_uri` | yes | non-empty string |
| `rollback_card_uri` | yes | non-empty string |
| `policy_bundle` | yes | non-empty string |
| `decided_at` | yes | date-time |
| `review` | yes | closed object with `reviewer` and `ticket` |

This shape is comparatively strong, but several fields are **reference strings**, not proof of resolution.

### Shape-validity limits

Schema validation does not establish that:

- `evidence_ref` resolves;
- `evidence_bundle_uri` exists or matches the candidate;
- `rollback_card_uri` exists or points to a safe target;
- `policy_bundle` exists, is active, or was evaluated;
- the reviewer is authorized or independent;
- the ticket exists;
- the decision is fresh;
- the candidate passed validation;
- rights and sensitivity permit release;
- the release manifest is complete;
- the lifecycle transition occurred.

### Minimal review binding is not a ReviewRecord

`review.reviewer` and `review.ticket` provide a minimal accountability binding. They do not carry:

- subject-bound review findings;
- reviewer role;
- reasons and obligations;
- evidence and policy basis;
- separation-of-duty proof;
- approval conditions;
- review expiry;
- supersession lineage.

Where materiality or policy requires a full ReviewRecord, the feature must show the minimal binding and the full review object as separate surfaces.

[Back to top](#top)

---

<a id="separate-decision-and-state-axes"></a>

## Separate decision and state axes

The repository currently contains multiple vocabularies. They must not be silently normalized.

| Axis | Current vocabulary | Meaning |
|---|---|---|
| PromotionDecision schema | `APPROVE`, `DENY`, `ABSTAIN` | Release-transition decision record |
| Release promotion lane README | `PROMOTE_TO_MANIFEST`, `HOLD_FOR_EVIDENCE`, `HOLD_FOR_VALIDATION`, `HOLD_FOR_POLICY`, `REPAIR_REQUIRED`, `SUPERSEDE_CANDIDATE`, `NO_ACTION` | Operational release-handling outcomes |
| ReviewRecord schema | `approve`, `reject`, `request_changes` | Review disposition |
| PolicyDecision schema | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | Policy finite outcome |
| Release root status | `DRAFT`, `READY_FOR_REVIEW`, `HELD`, `READY_FOR_MANIFEST`, `APPROVED`, `RELEASED`, `CORRECTED`, `SUPERSEDED`, `WITHDRAWN`, `NO_ACTION` | Release governance state |
| Feature UI state | `loading`, `ready`, `blocked`, `denied`, `abstained`, `stale`, `malformed`, `unavailable`, `error` | Presentation state |
| Recommendation intent | `recommend_route`, `recommend_hold`, `recommend_repair`, `recommend_deny`, `recommend_escalate`, `request_evidence` | Proposed user intent, not an authority record |

### Vocabulary rules

- Never render a PolicyDecision `ANSWER` as PromotionDecision `APPROVE`.
- Never render ReviewRecord `approve` as release `RELEASED`.
- Never convert `PROMOTE_TO_MANIFEST` into publication.
- Never treat `HELD` as `DENY` without a governed classification.
- Never use UI `ready` as a release state.
- Unknown values fail closed.
- Mapping requires a versioned, tested adapter or accepted ADR.

### Current conflict

The PromotionDecision contract and schema use `APPROVE | DENY | ABSTAIN`, while the release promotion lane README uses a richer operational outcome set. This README does not choose one as canonical. The UI must preserve both axes until governance reconciles them.

[Back to top](#top)

---

<a id="promotion-readiness-closure"></a>

## Promotion readiness closure

A promotion recommendation is safe only when all material closure families are explicit.

| Closure family | Required evidence | Failure posture |
|---|---|---|
| Candidate identity | stable candidate/run ref, domain/lane, lifecycle state, intended boundary | block |
| Source identity and role | SourceDescriptor/source-role refs and non-upcast posture | deny or abstain |
| Validation | applicable ValidationReports and transform receipts | hold |
| Evidence | resolvable EvidenceRef → EvidenceBundle support | abstain |
| Policy | evaluated, versioned policy bundle and PolicyDecision refs | deny, abstain, or error |
| Rights and sensitivity | resolved rights, consent, sovereignty, privacy, location exposure, redaction/generalization | deny or hold |
| Review | authorized reviewer, role, ticket, ReviewRecord where required, separation-of-duty state | hold |
| PromotionDecision | schema-valid, candidate-bound, fresh, non-superseded decision | hold |
| Rollback | resolvable RollbackCard/target and compatibility check | hold |
| Correction | named correction path and public-safe notice posture | hold |
| Manifest | ReleaseManifest readiness with content/digest/support closure | hold |
| Receipts and proofs | required validation, build, transformation, promotion, release, signature, and proof refs | hold |
| Freshness and time | decision, policy, evidence, source, validation, and release times compatible | stale/hold |
| Public-safe derivative | released projection with no restricted/internal data leakage | deny/hold |

### Readiness levels

| Level | Meaning | May feature show? | Authority effect |
|---|---|---:|---|
| `SHAPE_VALID` | PromotionDecision passes JSON Schema. | yes | none |
| `SUPPORT_RESOLVED` | Required references resolve and are compatible. | yes | none |
| `REVIEW_READY` | Candidate has enough context for reviewer assessment. | yes | none |
| `RECOMMENDATION_ELIGIBLE` | Current reviewer may submit a recommendation intent. | yes | external handoff only |
| `TRANSITION_AUTHORIZED` | Governed evaluator/recorder authorizes lifecycle transition. | only from authoritative response | does not equal release |
| `READY_FOR_MANIFEST` | Manifest assembly may proceed. | only from release authority | does not equal published |
| `RELEASED` | Governed release complete and public/restricted aliases bound. | only from released state | public effect as policy allows |

The feature must always show which level is being asserted.

[Back to top](#top)

---

<a id="proposed-governed-read-model"></a>

## Proposed governed read model

No accepted Review Console promotion DTO was established. The following is a **PROPOSED view model**, not a schema or API contract.

```yaml
promotion_review_projection:
  projection_version: v0
  candidate:
    ref: string
    domain: string
    run_id: string
    lifecycle_state: string
    proposed_transition: string
  promotion_decision:
    ref: string
    schema_status: valid | invalid | unavailable
    decision: APPROVE | DENY | ABSTAIN | unknown
    decided_at: date-time
    supersession_state: current | superseded | unknown
  closure:
    evidence: resolved | unresolved | stale | restricted | unavailable
    validation: pass | fail | incomplete | stale | unavailable
    policy: allow | deny | abstain | error | unevaluated | stale
    review: satisfied | missing | insufficient | conflicted | unavailable
    rollback: resolved | unresolved | invalid | unavailable
    correction: ready | missing | incomplete | unavailable
    manifest: ready | incomplete | unavailable
    receipts_and_proofs: complete | incomplete | unavailable
  operational_state:
    shape_valid: boolean
    review_ready: boolean
    recommendation_eligible: boolean
    transition_held: boolean
    release_state: string
  safe_reasons:
    - code: string
      public_summary: string
  permitted_actions:
    - string
```

### Read-model rules

- Every reference-bearing status must come from a governed resolver or authoritative record.
- The browser must not infer resolution from a path-shaped string.
- The server must minimize fields by role and sensitivity.
- Missing sections are not treated as success.
- Unknown enum values produce a safe blocked state.
- Projection version must be explicit.
- Cache keys must include subject, role/audience, projection version, policy context, and release context.
- Logout, role change, item change, supersession, correction, or policy refresh must invalidate relevant cached data.

[Back to top](#top)

---

<a id="recommendation-handoff"></a>

## Recommendation handoff

The feature is not the PromotionDecision writer.

A future handoff may submit a bounded intent such as:

```yaml
promotion_recommendation_intent:
  candidate_ref: string
  proposed_action: recommend_route | recommend_hold | recommend_repair | recommend_deny | recommend_escalate | request_evidence
  reviewer_context_ref: string
  rationale_code: string
  supporting_refs:
    - string
  optimistic_concurrency_token: string
```

This shape is illustrative only.

### Handoff requirements

Before submission:

- reviewer identity, role, assignment, and clearance are resolved;
- the projection is fresh;
- the candidate has not changed;
- the current policy context permits the action;
- required rationale and support refs are present;
- the feature displays that a recommendation is not final authority.

After submission:

- the governed recorder validates inputs again;
- policy and review separation run server-side;
- the recorder returns a finite authoritative response;
- any PromotionDecision or ReviewRecord is created outside the feature;
- the feature refreshes from authoritative state;
- failed writes do not leave an optimistic success state;
- duplicate submissions are idempotent or visibly rejected.

### No direct execution

The feature must not:

- invoke `pipelines/domains/hydrology/promote.py`;
- write under `release/promotion_decisions/`;
- call a file-system mutation endpoint;
- create a ReleaseManifest;
- repoint aliases;
- execute a pipeline transition;
- bypass the release authority.

[Back to top](#top)

---

<a id="freshness-identity-and-supersession"></a>

## Freshness, identity, and supersession

Promotion readiness is time-sensitive.

The feature should distinguish:

- source time;
- retrieval time;
- validation time;
- policy evaluation time;
- review time;
- promotion decision time;
- manifest build time;
- release time;
- correction/supersession time.

### Freshness rules

- A schema-valid decision may still be stale.
- A policy bundle identifier is insufficient without accepted version/freshness semantics.
- Evidence and validation must apply to the same candidate/run.
- A later decision does not mutate the earlier decision.
- Superseded decisions remain inspectable where policy permits.
- A current candidate must not reuse an old decision without explicit compatibility proof.
- Clock skew or missing time-kind context produces a safe stale/unknown state.

### Deterministic identity

Where practical, the projection should expose stable refs for:

- candidate;
- run;
- PromotionDecision;
- ReviewRecord;
- PolicyDecision;
- EvidenceBundle;
- RollbackCard;
- ReleaseManifest;
- correction/supersession record.

It must not invent canonical IDs in the browser.

[Back to top](#top)

---

<a id="access-sensitivity-and-security"></a>

## Access, sensitivity, and security

Promotion review may expose unreleased artifacts, policy reasons, reviewer identities, source limitations, exact sensitive geometry, rights disputes, living-person data, archaeological information, rare-species locations, infrastructure detail, or internal paths.

### Minimum controls

- server-side role and item authorization;
- deny-by-default field projection;
- no direct lifecycle-store access;
- no raw evidence-bundle payload by default;
- no secret, token, internal path, stack trace, or policy source leakage;
- safe reason summaries separated from restricted detail;
- field-level minimization;
- export and copy restrictions;
- cache partitioning by role/audience and item;
- explicit stale and partial-data indicators;
- audit of read and recommendation events where policy requires it;
- protection against cross-item and cross-tenant reference substitution;
- accessibility without hidden privileged detail in labels or tooltips.

### Threat matrix

| Threat | Required response |
|---|---|
| Forged `APPROVE` object | validate signature/provenance/authority when adopted; otherwise mark untrusted |
| Path-shaped unresolved reference | never treat as resolved |
| Browser changes decision value | server ignores client authority fields |
| Role downgrade with cached page | clear protected cache and rerun authorization |
| Candidate changes during review | reject stale concurrency token |
| Unsupported enum | block with safe malformed state |
| Sensitive reason leakage | show safe code/summary only |
| Cross-candidate ref substitution | verify all refs bind to candidate/run |
| Replay of old recommendation | idempotency and freshness checks |
| Hard-coded smoke artifact shown as release | label smoke/held/not released |
| Policy stub interpreted as allow | display `POLICY_UNEVALUATED`, not allow |
| Manifest `id`-only schema treated as readiness | display `MANIFEST_INCOMPLETE` |

[Back to top](#top)

---

<a id="finite-ui-states"></a>

## Finite UI states

The feature should use explicit presentation states:

| State | Meaning |
|---|---|
| `loading` | governed projection is loading |
| `ready_for_review` | enough context exists for inspection |
| `recommendation_eligible` | current role may submit an external recommendation |
| `blocked` | one or more closure requirements are incomplete |
| `denied` | authoritative policy or release gate denies access/action |
| `abstained` | authoritative evaluator cannot decide safely |
| `stale` | time or supersession invalidates current view |
| `restricted` | user may know an item exists but cannot inspect details |
| `malformed` | projection or referenced object violates accepted shape |
| `unavailable` | authoritative dependency cannot be reached |
| `error` | safe bounded failure |

These are UI states, not PromotionDecision, PolicyDecision, ReviewRecord, or release status values.

### Safe rendering

Each non-ready state should show:

- safe reason code;
- bounded summary;
- affected closure family;
- whether retry, refresh, escalation, or evidence request is permitted;
- no restricted payload or internal implementation detail.

[Back to top](#top)

---

<a id="validation-and-negative-paths"></a>

## Validation and negative paths

### Current executable proof

| Check | Current status | Proven scope |
|---|---:|---|
| PromotionDecision JSON Schema validator | executable | shape only |
| PromotionDecision fixture test | executable | fixture runner exits successfully |
| Promotion-gate workflow fixture inventory | executable | non-empty valid/invalid sets and pinned schema metadata |
| Hydrology smoke hold assertions | executable | confirms hard-coded stub, unresolved refs, absent real reviews, placeholder validators |
| Promotion policy behavior | not established | no real rules |
| Gate validator | placeholder | no gate semantics |
| ReviewRecord validator | placeholder | no review validation |
| Support-reference resolution | not established | no closure proof |
| UI tests | not surfaced | no feature proof |

### Minimum negative cases

A mature feature/test suite should cover:

1. unauthorized reviewer;
2. restricted candidate;
3. missing candidate identity;
4. lifecycle state mismatch;
5. invalid PromotionDecision shape;
6. missing PromotionDecision;
7. unknown PromotionDecision decision value;
8. unresolved EvidenceRef;
9. missing EvidenceBundle;
10. EvidenceBundle candidate mismatch;
11. stale evidence;
12. validation failure;
13. missing validation report;
14. policy unevaluated;
15. policy deny;
16. policy abstain;
17. policy error;
18. policy bundle stale or unknown;
19. missing reviewer binding;
20. missing full ReviewRecord where required;
21. self-review conflict;
22. reviewer role mismatch;
23. missing rollback target;
24. invalid rollback target;
25. missing correction path;
26. incomplete ReleaseManifest;
27. manifest candidate mismatch;
28. missing proof/receipt;
29. superseded PromotionDecision;
30. stale projection;
31. concurrent candidate change;
32. hard-coded smoke `APPROVE`;
33. extra field rejected by PromotionDecision schema;
34. invalid hydrology ID;
35. cross-candidate reference substitution;
36. sensitive reason minimization;
37. duplicate recommendation submission;
38. API unavailable;
39. safe error without stack trace;
40. logout or role-change cache purge.

### Required proof layers

- schema tests;
- semantic validator tests;
- policy tests;
- evidence-resolution tests;
- review/separation tests;
- rollback/correction tests;
- release-manifest tests;
- API contract tests;
- component tests;
- accessibility tests;
- security-negative tests;
- integration tests;
- end-to-end held/deny/abstain/error/recommendation paths.

[Back to top](#top)

---

<a id="smallest-sound-implementation-sequence"></a>

## Smallest sound implementation sequence

1. **Reconcile vocabularies.** Decide and document how PromotionDecision, release operational outcomes, ReviewRecord, PolicyDecision, and UI states relate.
2. **Implement promotion policy.** Replace comment-only stubs with tested fail-closed rules for evidence, rollback, review, rights, sensitivity, validation, and freshness.
3. **Replace hard-coded hydrology approval.** Make the promoter consume governed inputs and produce finite outcomes based on actual evaluation—or keep it disabled.
4. **Resolve support refs.** Add deterministic resolution and candidate-binding checks for evidence, rollback, review, policy, and validation.
5. **Implement the promotion-gate validator.** Validate semantic closure beyond JSON shape.
6. **Implement accountable review.** Complete ReviewRecord validation and separation-of-duty checks.
7. **Harden ReleaseManifest and RollbackCard.** Move beyond `id`-only schemas before claiming release or rollback readiness.
8. **Define the governed read DTO.** Version, schema, authorize, minimize, and test the Review Console projection.
9. **Build read-only feature rendering.** Render explicit axes and safe states without mutation.
10. **Add typed recommendation handoff.** Server revalidation, concurrency control, idempotency, and audit.
11. **Add security, accessibility, observability, and cache controls.**
12. **Bind CI to the accepted implementation.** Replace readiness holds deliberately; never execute a hard-coded promoter as a shortcut.
13. **Document correction and rollback.** Include safe-disable and supersession paths before operational use.

Each step should be independently reviewable and reversible.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

This feature is not done until:

- [ ] named owners are confirmed;
- [ ] direct feature implementation inventory is documented;
- [ ] decision and state vocabularies are reconciled;
- [ ] PromotionDecision schema and semantic contract are accepted or versioned;
- [ ] promotion policy contains real tested rules;
- [ ] hard-coded `APPROVE` is removed or the promoter remains disabled;
- [ ] evidence, rollback, review, policy, validation, and manifest refs resolve;
- [ ] PromotionDecision semantic validator exists;
- [ ] ReviewRecord validation and separation of duties exist;
- [ ] ReleaseManifest and RollbackCard readiness are machine-checkable;
- [ ] governed API read model is versioned and authorized;
- [ ] feature remains read-only outside typed handoff;
- [ ] recommendation handoff revalidates server-side;
- [ ] no local lifecycle or release writes exist;
- [ ] stale, denied, abstained, malformed, restricted, unavailable, and error states are tested;
- [ ] sensitive and internal data minimization is tested;
- [ ] accessibility is tested;
- [ ] audit and observability are bounded and non-authoritative;
- [ ] safe disablement, correction, supersession, and rollback are documented;
- [ ] CI proves the intended negative and positive paths;
- [ ] generated receipts and human review are complete for trust-significant changes;
- [ ] no README claim exceeds current executable proof.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| ID | Item | Status | Why it matters |
|---|---|---:|---|
| PROMO-UI-01 | Recursive feature inventory | NEEDS VERIFICATION | Direct search is bounded. |
| PROMO-UI-02 | Accepted PromotionDecision authority/version | NEEDS VERIFICATION | Schema remains PROPOSED. |
| PROMO-UI-03 | Vocabulary reconciliation | CONFLICTED | Multiple incompatible decision/state sets exist. |
| PROMO-UI-04 | Real promotion policy | NEEDS VERIFICATION | Current Rego files have no real rules. |
| PROMO-UI-05 | Hydrology promoter disposition | NEEDS VERIFICATION | Hard-coded `APPROVE` must not become production behavior. |
| PROMO-UI-06 | Evidence/rollback ref resolution | NEEDS VERIFICATION | Smoke refs are unresolved. |
| PROMO-UI-07 | Promotion-gate validator | NEEDS VERIFICATION | Current file is a placeholder. |
| PROMO-UI-08 | ReviewRecord validator and records | NEEDS VERIFICATION | Accountable review is not established. |
| PROMO-UI-09 | ReleaseManifest completeness | NEEDS VERIFICATION | Current schema is `id`-only. |
| PROMO-UI-10 | RollbackCard completeness | NEEDS VERIFICATION | Current schema is `id`-only. |
| PROMO-UI-11 | Governed API route/DTO | UNKNOWN | Feature data source is not established. |
| PROMO-UI-12 | Recommendation writer/recorder | UNKNOWN | No accepted handoff exists. |
| PROMO-UI-13 | Cross-domain promotion behavior | UNKNOWN | Confirmed implementation evidence is hydrology-specific. |
| PROMO-UI-14 | Rights/sensitivity policy | NEEDS VERIFICATION | Public exposure must fail closed. |
| PROMO-UI-15 | Branch protection and required checks | UNKNOWN | Platform controls not inspected. |
| PROMO-UI-16 | Deployment and telemetry | UNKNOWN | No runtime claim is supported. |
| PROMO-UI-17 | Full-suite pass state | UNKNOWN | Not established by this documentation update. |

[Back to top](#top)

---

<a id="evidence-ledger"></a>

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Prior promotion feature README | CONFIRMED | Existing intent and path. | Broadly greenfield. |
| Review Console parent READMEs/package manifest | CONFIRMED | App-local role-gated placement and placeholder maturity. | No feature runtime. |
| PromotionDecision contract | CONFIRMED file / PROPOSED semantics | Object boundaries, fields, outcomes. | Not policy or execution. |
| PromotionDecision schema | CONFIRMED / PROPOSED | Closed eleven-field shape and hydrology rule. | Does not resolve refs. |
| PromotionDecision validator/test | CONFIRMED executable | Shape fixture validation. | Not gate readiness. |
| PromotionDecision fixtures | CONFIRMED minimum cases | Valid and missing-evidence examples. | Incomplete coverage. |
| Promotion policy README/Rego | CONFIRMED stubs | Files and proposed homes. | No real rules. |
| Hydrology promoter | CONFIRMED stub | Current code writes hard-coded `APPROVE`. | Not governed evaluation. |
| Hydrology smoke decision | CONFIRMED | Tracked schema-shaped smoke record. | Unresolved support and no accountable review. |
| Promotion-gate workflow | CONFIRMED | Explicit read-only holds and negative assertions. | Does not promote. |
| Release promotion lane README | CONFIRMED | Release-root placement and operational vocabulary. | Conflicts with schema vocabulary. |
| ReleaseManifest contract/schema | CONFIRMED thin pair | Separation from PromotionDecision. | Manifest readiness not enforceable. |
| RollbackCard contract/schema | CONFIRMED thin pair | Rollback semantic boundary. | Rollback readiness not enforceable. |
| ReviewRecord schema | CONFIRMED / PROPOSED | Review vocabulary and closed shape. | Validator placeholder. |
| PolicyDecision schema | CONFIRMED / PROPOSED | Policy outcome vocabulary. | Policy runtime not proven. |
| Directory Rules | CONFIRMED live file / review status | Responsibility-root placement. | Does not prove feature implementation. |

[Back to top](#top)

---

<a id="maintenance-triggers"></a>

## Maintenance triggers

Update this README when any of these change:

- PromotionDecision contract, schema, fixtures, or validator;
- promotion or release policy;
- hydrology promoter or another domain promoter;
- tracked promotion decision records;
- support-reference resolution;
- ReviewRecord contract, schema, validator, or records;
- ReleaseManifest or RollbackCard schema;
- promotion-gate workflow;
- release promotion-decision vocabulary or lane structure;
- governed API route/DTO;
- feature source, tests, dependencies, accessibility, or deployment;
- rights, sensitivity, source-role, correction, rollback, or release doctrine;
- accepted ADRs;
- branch protection or required checks.

[Back to top](#top)

---

<a id="rollback-correction-and-supersession"></a>

## Rollback, correction, and supersession

### Documentation rollback

Before merge:

- close the draft PR; or
- reset/delete the scoped branch.

After merge:

1. revert the generated receipt commit;
2. revert the README commit;
3. restore prior target blob `eee28922e3e74019fd2d35a2a03da3f9cd9c81ef`;
4. record why the stronger evidence boundary was reverted.

### Feature safe disablement

A future feature should support disabling:

- recommendation actions while retaining safe read-only state;
- individual closure panels when their upstream contract changes;
- exports/copy actions;
- cross-domain promotion views;
- the entire feature route without affecting release records.

Disabling the UI must not mutate PromotionDecision, ReviewRecord, PolicyDecision, ReleaseManifest, RollbackCard, evidence, receipt, proof, or release state.

### Correction of promotion decisions

A wrong or stale PromotionDecision must be corrected by a new governed decision or supersession record. Do not edit the old decision in place.

### No-loss preservation note

The previous v0.1 README was substantive. This revision preserves its core boundaries—review support only, no publication authority, no file movement, evidence/policy/review/rollback/correction requirements—while replacing generic uncertainty with current repository evidence and explicit conflicts.

[Back to top](#top)

---

## Status summary

`apps/review-console/src/features/promotion/` remains an app-local documentation boundary. PromotionDecision shape validation is executable; promotion authorization, accountable review, policy evaluation, support closure, lifecycle transition, release-manifest readiness, and publication remain held or unverified.

**Current safe conclusion:** inspectable promotion review is a valid design target, but the tracked hydrology `APPROVE` smoke record is not release authority and must remain visibly held until its evidence, rollback, policy, review, validation, manifest, correction, and release dependencies are governed and resolved.
