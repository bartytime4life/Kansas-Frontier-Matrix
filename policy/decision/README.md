<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://policy/decision
title: policy/decision/ — Finite Outcome and Decision-Normalization Boundary
type: policy-readme; directory-readme; decision-policy-boundary
version: v0.3
status: draft; repository-grounded; mixed-maturity; inactive-machine-vocabularies; schema-paired; fixture-validated; evaluator-unbound; non-release; non-publication
owners: OWNER_TBD — CODEOWNERS routes /policy/ to @bartytime4life; accepted policy stewardship, independent review assignment, evaluator ownership, and release authority remain NEEDS VERIFICATION
created: 2026-06-15
updated: 2026-08-13
policy_label: "public-governance; restricted-review; finite-outcomes; cite-or-abstain; fail-closed; obligation-preserving; reason-coded; replayable; proposed-inactive; no-runtime-authority; no-release-authority; no-truth-authority"
current_path: policy/decision/README.md
owning_root: policy/
responsibility: define and index the decision-policy boundary and host inactive candidate vocabularies for canonical finite outcomes, reasons, obligations, and reviewer roles without owning semantic contracts, machine schemas, evaluator implementation, receipts, evidence, lifecycle mutation, release approval, or publication
truth_posture: CONFIRMED accepted Directory Rules v2 placement, canonical singular policy root, four-outcome PolicyDecision shape, six policy families, two valid and three invalid shape fixtures, two direct PROPOSED_INACTIVE machine vocabularies, nine reason codes, eight obligation codes, five reviewer-role codes, focused fixture-only validators and workflows, an explicit PolicyInputBundle profile, declared-only evaluation binding, obligation profiles, one separately governed PROPOSED_INACTIVE OPA-tested release-gate profile, placeholder general policy runtime, empty machine policy-gate register, and absent schema-declared canonical validator/policy paths / PROPOSED activation of current vocabularies and profiles, native-result normalization, operational-state carrier, accepted composition, direct decision rules, deterministic identity, replay, supersession, and correction integration / UNKNOWN accepted general evaluator, repository-wide bundle selection, authenticated PolicyDecision emitters, production consumers, required-check configuration, decision receipt persistence, promotion/release enforcement, and public runtime use / NEEDS VERIFICATION accepted owners, ADR-0020 acceptance or supersession, vocabulary compatibility policy, obligation interpreters, reviewer assignment, consumer inventory, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  visibility: public
  base_ref: main
  base_commit: 1a61d3fbdc111bb3292086a30a53ccc50ed1bb8a
  prior_blob: 1ab41e00cb77c0bb34e2169a13261486f5b9c7dd
  inventory_method: complete recursive Git tree plus exact GitHub connector reads, target history, exact-target pull-request search, planned-branch lookup, and bounded consumer/workflow inspection
  direct_lane_files_confirmed:
    - policy/decision/.gitkeep
    - policy/decision/README.md
    - policy/decision/reviewer_roles.v1.json
    - policy/decision/vocabulary.v1.json
  bounded_inventory_note: no Rego module, native policy test, active registry, accepted evaluator, authenticated emitter, receipt writer, runtime consumer binding, release integration, or publication effect exists in the direct lane; bounded absence does not prove repository-wide permanent absence
related:
  - ../README.md
  - ../bundles/README.md
  - ../rego/README.md
  - ../runtime/README.md
  - ./vocabulary.v1.json
  - ./reviewer_roles.v1.json
  - ../../contracts/policy/policy_decision.md
  - ../../contracts/policy/policy_decision_vocabulary.md
  - ../../contracts/policy/policy_decision_semantics_profile_v1.md
  - ../../contracts/policy/policy_reviewer_role_vocabulary.md
  - ../../contracts/policy/policy_input_bundle.md
  - ../../contracts/policy/policy_input_bundle_profile_v1.md
  - ../../contracts/policy/policy_evaluation_binding_v1.md
  - ../../contracts/policy/policy_obligation_set.md
  - ../../contracts/policy/policy_obligation_reduction.md
  - ../../contracts/runtime/decision_envelope.md
  - ../../schemas/contracts/v1/policy/policy_decision.schema.json
  - ../../fixtures/contracts/v1/policy/policy_decision/README.md
  - ../../tools/validators/policy/README.md
  - ../../tests/schemas/test_common_contracts.py
  - ../../.github/workflows/policy-test.yml
  - ../../.github/workflows/policy-decision-vocabulary.yml
  - ../../.github/workflows/policy-decision-semantics-v1.yml
  - ../../.github/workflows/policy-reviewer-role-vocabulary.yml
  - ../../.github/workflows/pass12-release-policy-v1.yml
  - ../../docs/adr/ADR-0020-abstain-is-a-first-class-decision.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/doctrine/directory-rules.md
  - ../../control_plane/root_registry.yaml
  - ../../control_plane/policy_gate_register.yaml
  - ../../packages/policy-runtime/README.md
  - ../../release/README.md
tags: [kfm, policy, decision, PolicyDecision, DecisionEnvelope, finite-outcomes, answer, abstain, deny, error, allow, restrict, hold, normalization, reason-codes, obligations, reviewer-roles, composition, replay, supersession, fail-closed]
notes:
  - "This revision reconciles the v0.2 README with machine-checkable candidate artifacts added after its 2026-07-19 evidence snapshot."
  - "The current PolicyDecision schema remains PROPOSED, closed, and limited to ANSWER, ABSTAIN, DENY, and ERROR."
  - "The direct vocabularies and every linked decision-policy profile remain PROPOSED_INACTIVE; passing validation does not activate policy or authenticate a decision."
  - "The separately governed Pass 12 Rego profile returns native allow and deny_reasons, not a canonical PolicyDecision."
  - "The schema-declared tools/validators/validate_policy_decision.py and policy/policy/ paths remain absent by design under the broad readiness hold."
  - "ADR-0029, not the internal pre-adoption label retained in the adopted doctrine bytes, makes docs/doctrine/directory-rules.md the writable Directory Rules authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Decision Policy

`policy/decision/`

> Repository-grounded policy boundary for finite outcomes, decision normalization, stable reason and obligation codes, reviewer-role vocabulary, multi-gate composition, replay, supersession, and public-safe handling. The direct lane now contains machine-checkable candidate vocabularies, but it does not evaluate policy, authenticate decisions, create evidence, approve release, or publish.

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#current-repository-status)
[![Version: v0.3](https://img.shields.io/badge/version-v0.3-0969da?style=flat-square)](#change-history)
[![Direct lane: proposed inactive](https://img.shields.io/badge/direct%20lane-PROPOSED__INACTIVE-d97706?style=flat-square)](#current-direct-child-map)
[![Outcomes: finite four](https://img.shields.io/badge/outcomes-ANSWER%20%7C%20ABSTAIN%20%7C%20DENY%20%7C%20ERROR-8250df?style=flat-square)](#canonical-policydecision-outcomes)
[![Vocabulary: fixture validated](https://img.shields.io/badge/vocabulary-fixture--validated-2da44e?style=flat-square)](#reason-code-boundary)
[![General evaluator: unbound](https://img.shields.io/badge/general%20evaluator-unbound-d97706?style=flat-square)](#validation-negative-cases-and-ci)
[![Publisher: no](https://img.shields.io/badge/publisher-no-b42318?style=flat-square)](#lifecycle-and-release-boundary)

**Quick navigation:** [Purpose](#purpose) · [Status](#current-repository-status) · [Direct children](#current-direct-child-map) · [Authority](#authority-and-repository-fit) · [Outcome axes](#outcome-axes-must-remain-separate) · [Canonical outcomes](#canonical-policydecision-outcomes) · [Normalization](#engine-result-normalization) · [Inputs](#required-evaluation-input) · [Reasons](#reason-code-boundary) · [Obligations](#obligation-boundary) · [Composition](#multi-gate-composition) · [Replay](#identity-replay-freshness-and-supersession) · [Public boundary](#public-interface-and-sensitive-data-boundary) · [Validation](#validation-negative-cases-and-ci) · [Implementation](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Evidence](#evidence-ledger) · [Rollback](#correction-rollback-and-supersession) · [History](#change-history)

> [!IMPORTANT]
> **Safe current conclusion:** the direct lane contains a `PROPOSED_INACTIVE` reason/obligation registry with nine reasons and eight `ANSWER`-only obligations, plus a `PROPOSED_INACTIVE` reviewer-role registry with five role codes. Dedicated no-network validators, synthetic fixtures, unit tests, and focused workflows check those candidates. The base `PolicyDecision` shape still has two valid and three invalid shape fixtures. None of this activates a policy bundle, proves evaluator execution, authenticates a decision, assigns a reviewer, enforces an obligation, approves release, or publishes.

> [!NOTE]
> One separately governed Pass 12 release-gate profile under [`policy/rego/`](../rego/README.md) is `PROPOSED_INACTIVE` but genuinely OPA-tested with checksum-pinned OPA 1.19.0. It returns native `allow` and sorted `deny_reasons`; it does not emit the canonical six-field `PolicyDecision` and does not establish a repository-wide evaluator.

> [!CAUTION]
> A decision record is not evidence, truth, consent, rights clearance, review approval, lifecycle promotion, release approval, or publication. `ANSWER` only permits the evaluated operation within its exact context and enforceable obligations; it cannot repair missing EvidenceBundle support, downgrade sensitivity, infer consent, bypass review, or authorize public release.

---

## Purpose

`policy/decision/` defines the policy-side boundary for how governed KFM decision points should:

- use a finite, auditable outcome vocabulary;
- distinguish policy denial from evidence-based abstention and machinery failure;
- normalize lower-level engine results into the canonical decision surface;
- attach stable, public-safe reasons and enforceable obligations;
- compose multiple gate results without weakening the most protective outcome;
- preserve deterministic identity, evaluation time, replay inputs, and supersession lineage;
- route public decisions through governed interfaces;
- fail closed when an outcome, reason, obligation, evaluator, bundle, or input cannot be trusted.

This README is a governance and implementation boundary. It is not executable policy and does not prove that any caller currently emits a valid `PolicyDecision`.

---

## Current repository status

| Surface | Status at `main@1a61d3fb…` | Evidence-bounded conclusion |
|---|---:|---|
| `policy/decision/README.md` | **CONFIRMED v0.2 baseline** | This v0.3 revision reconciles the same document identity with current repository evidence. |
| [`vocabulary.v1.json`](vocabulary.v1.json) | **CONFIRMED / `PROPOSED_INACTIVE`** | Nine sorted reason codes and eight sorted obligation codes; every authority flag is `false`. |
| [`reviewer_roles.v1.json`](reviewer_roles.v1.json) | **CONFIRMED / `PROPOSED_INACTIVE`** | Five stable role codes; the registry assigns no people, records no approval, and grants no policy, promotion, release, or publication authority. |
| Direct decision Rego or native tests | **CONFIRMED ABSENT** | The complete recursive tree contains no `.rego` module or test under `policy/decision/`. |
| [`PolicyDecision` semantic contract](../../contracts/policy/policy_decision.md) | **CONFIRMED / PROPOSED** | Defines meaning without executing policy or approving release. |
| [`PolicyDecision` schema](../../schemas/contracts/v1/policy/policy_decision.schema.json) | **CONFIRMED / PROPOSED CONCRETE SHAPE** | Requires six fields, closes additional properties, and permits four outcomes and six policy families. |
| Base [shape fixtures](../../fixtures/contracts/v1/policy/policy_decision/README.md) | **CONFIRMED MINIMAL COVERAGE** | Two valid instances and three invalid shape cases remain discoverable by the common schema harness. |
| [Decision vocabulary contract](../../contracts/policy/policy_decision_vocabulary.md), schema, fixtures, validator, tests, workflow | **CONFIRMED / FIXTURE-ONLY** | Checks shape, canonical ordering, unique and disjoint code namespaces, family/outcome bindings, `ANSWER`-only obligations, and false authority flags. |
| [Decision semantics profile v1](../../contracts/policy/policy_decision_semantics_profile_v1.md) | **CONFIRMED / `PROPOSED_INACTIVE`** | Checks base-schema validity plus inactive reason/obligation coherence against synthetic records; it is intentionally not the held canonical evaluator-bound validator. |
| [Reviewer-role vocabulary contract](../../contracts/policy/policy_reviewer_role_vocabulary.md), schema, cases, validator, tests, workflow | **CONFIRMED / FIXTURE-ONLY** | Checks sorted unique role codes, bounded scopes, alias collisions, and false authority flags; it does not assign or authenticate reviewers. |
| Parent [`PolicyInputBundle`](../../contracts/policy/policy_input_bundle.md) schema | **CONFIRMED PERMISSIVE PARENT** | The parent machine shape remains too permissive to prove complete evaluation context. |
| [Explicit input profile v1](../../contracts/policy/policy_input_bundle_profile_v1.md) | **CONFIRMED / `PROPOSED_INACTIVE`** | Closed, fixture-tested profile for five operations and seven audiences; passing proves context coherence only. |
| [Evaluation binding v1](../../contracts/policy/policy_evaluation_binding_v1.md) | **CONFIRMED / `DECLARED_ONLY`** | Binds exact input and decision bytes plus evaluator declarations; it does not execute policy or authenticate a decision. |
| [Obligation set](../../contracts/policy/policy_obligation_set.md) and [obligation reduction](../../contracts/policy/policy_obligation_reduction.md) | **CONFIRMED / FIXTURE-ONLY CANDIDATES** | Structured carriers and deterministic reduction evidence exist; no production interpreter or enforcement receipt is established. |
| Schema-declared canonical validator | **CONFIRMED ABSENT AT DECLARED PATH** | `tools/validators/validate_policy_decision.py` remains absent and is guarded by [`policy-test`](../../.github/workflows/policy-test.yml). |
| Schema-declared policy path | **CONFIRMED ABSENT AT DECLARED PATH** | `policy/policy/` remains absent and conflicts with the accepted singular, purpose-specific `policy/` layout. |
| Broad [`policy-test` workflow](../../.github/workflows/policy-test.yml) | **CONFIRMED READINESS HOLD** | Inventories the broad boundary and explicitly emits no `PolicyDecision`. |
| Focused decision workflows | **CONFIRMED READ-ONLY VALIDATION** | Vocabulary, semantics, reviewer roles, explicit inputs, evaluation binding, obligations, and maturity profiles have bounded workflows; workflow presence is not activation or required-check proof. |
| [Pass 12 release-gate Rego](../rego/release_gate_v1.rego) | **CONFIRMED OPA-TESTED / `PROPOSED_INACTIVE`** | One bounded native `allow`/`deny_reasons` profile exists outside this lane; it is not a general evaluator or canonical decision emitter. |
| [Policy bundles](../bundles/README.md) | **CONFIRMED DOCUMENTATION-ONLY PAYLOAD SET** | The tracked bundle subtree contains READMEs only; no accepted machine bundle manifest, selector, signature, or active bundle is established. |
| [Policy runtime package](../../packages/policy-runtime/README.md) | **CONFIRMED `0.0.0` PLACEHOLDER** | Empty initializer and comment-only core; no functional general evaluator or adapter. |
| [Machine policy-gate register](../../control_plane/policy_gate_register.yaml) | **CONFIRMED EMPTY** | `entries: []`; the direct candidate vocabulary does not populate or supersede this separate machine projection. |
| [ADR-0020](../../docs/adr/ADR-0020-abstain-is-a-first-class-decision.md) | **CONFIRMED FILE / PROPOSED ADR** | Proposes exhaustive four-outcome composition and first-class abstention; acceptance remains unresolved. |
| Runtime consumers, required checks, and release enforcement | **UNKNOWN** | No exhaustive production-consumer inventory, ruleset proof, authenticated decision flow, or release coupling was established. |

### Current direct-child map

| Direct child | Kind | Current role | Authority boundary |
|---|---|---|---|
| [`README.md`](./README.md) | Human-readable directory contract | Explains the lane, current evidence, proposed operating model, and trust boundaries. | Prose cannot activate or evaluate policy. |
| [`vocabulary.v1.json`](vocabulary.v1.json) | Machine-readable candidate registry | Nine reason codes and eight obligation codes for fixture-only coherence checks. | `PROPOSED_INACTIVE`; all governance flags are `false`. |
| [`reviewer_roles.v1.json`](reviewer_roles.v1.json) | Machine-readable candidate registry | Five stable classes for review routing vocabulary. | Assigns no people, records no approval, and grants no authority. |
| `.gitkeep` | Empty path-retention marker | Preserves directory existence in Git history. | No semantic or policy meaning. |

No direct child is an evaluator, active bundle, emitted decision, receipt, approval, release record, or public carrier.

### What this status does not prove

A green schema test, validator, focused workflow, or OPA fixture suite does not prove:

- that a candidate vocabulary or profile is accepted or active;
- that a repository-wide bundle was selected or evaluated;
- that a `PolicyDecision` was produced by an accepted evaluator or authenticated emitter;
- that input facts, evidence, rights, consent, sensitivity, review, or release context were authoritative and current;
- that a named reviewer was assigned, qualified, independent, or approved a candidate;
- that obligations were interpreted and enforced by a downstream consumer;
- that an `ANSWER` was promoted, released, rendered, exported, or published;
- that a decision receipt exists or replay reproduces the same result;
- that a workflow is configured as a required merge check;
- that correction, withdrawal, supersession, or rollback propagation is automated.

---

## Authority and repository fit

Accepted [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) makes [Directory Rules v2](../../docs/doctrine/directory-rules.md) the writable placement authority and classifies `policy/` as the canonical policy-rule root. The architecture-path Directory Rules body is retained as read-only compatibility evidence, not a second writable authority.

| Responsibility | Owning surface | Boundary |
|---|---|---|
| Decision-policy posture and inactive policy-side vocabularies | `policy/decision/` | This lane owns the README and candidate registries. It currently owns no evaluator, active bundle, emitted decision, or direct Rego rule. |
| Executable policy source | Purpose-specific lanes under [`policy/`](../README.md) | Rule source stays under the singular policy root; presence does not imply activation. |
| Policy bundle packaging | [`policy/bundles/`](../bundles/README.md) | Future manifest, digest, dependency closure, selection, and activation; current payload set is documentation-only. |
| Policy-decision semantic meaning | [`contracts/policy/policy_decision.md`](../../contracts/policy/policy_decision.md) | Meaning of one decision result; no evaluation or release authority. |
| Candidate vocabulary meaning | [decision vocabulary](../../contracts/policy/policy_decision_vocabulary.md) and [reviewer-role vocabulary](../../contracts/policy/policy_reviewer_role_vocabulary.md) contracts | Semantics for the two direct registries. |
| Machine shape | [`schemas/contracts/v1/policy/`](../../schemas/contracts/v1/policy/README.md) | Shape authority for decisions and candidate profiles; schemas do not activate policy. |
| Synthetic examples | [contract fixture guidance](../../fixtures/contracts/v1/policy/README.md) and the root [fixture contract](../../fixtures/README.md), including `fixtures/policy/` | Public-safe positive and negative inputs; fixtures are not production decisions. |
| Deterministic checking | [`tools/validators/policy/`](../../tools/validators/policy/README.md), `tests/validators/`, and workflows | Bounded conformance evidence; validators are not policy evaluators unless an accepted contract says so. |
| Runtime transport | [`contracts/runtime/decision_envelope.md`](../../contracts/runtime/decision_envelope.md) and paired schema | Carrier distinct from policy authority, evidence closure, and release approval. |
| General evaluation mechanics | [`packages/policy-runtime/`](../../packages/policy-runtime/README.md) or an accepted evaluator | Proposed reusable executor/normalizer boundary; current package is a placeholder. |
| Bounded native release-gate evaluation | [`policy/rego/release_gate_v1.rego`](../rego/release_gate_v1.rego) | Separately governed `PROPOSED_INACTIVE` OPA profile; native result is not canonical `PolicyDecision` emission. |
| Human gate index | [`docs/registers/POLICY_GATE.md`](../../docs/registers/POLICY_GATE.md) | Explanation and review index; not executable policy. |
| Machine gate projection | [`control_plane/policy_gate_register.yaml`](../../control_plane/policy_gate_register.yaml) | Separate empty projection; does not inherit candidate codes automatically. |
| Evidence support | Evidence contracts, EvidenceBundles, validators, and proof lanes | Decisions may consume supplied status; they cannot create evidence closure. |
| Receipts and replay records | [`data/receipts/`](../../data/receipts/README.md) or another accepted receipt home | Process memory; not approval, truth, or release authority. |
| Promotion, release, correction, withdrawal, and rollback | [`release/`](../../release/README.md) | Policy decisions may be required inputs; they do not move or publish artifacts. |
| Public enforcement | Governed APIs and released clients | Public callers must not select bundles, invoke internal evaluators, or read protected decision stores directly. |

### Authority order for decision behavior

When sources disagree, use this order:

1. accepted doctrine and core invariants: cite-or-abstain, fail closed, trust membrane, lifecycle law, evidence-first, and correction visibility;
2. accepted ADRs that explicitly govern the affected decision behavior;
3. an accepted, digest-bound executable policy bundle and evaluator for the exact context;
4. accepted semantic contracts and paired schemas for emitted objects;
5. accepted and active gate, reason, obligation, reviewer, and normalization registries;
6. authenticated tests, fixtures, receipts, runtime traces, release records, and required-check evidence;
7. human-facing README and register prose.

Current candidate registries and profiles occupy the evidence and design layers, not the accepted active-policy layer. When activation evidence is missing or conflicting, preserve the inactive status and fail closed.

---

## Supersession and preserved lineage

This v0.3 README supersedes v0.2 documentation at the same path. It preserves the strongest v0.2 concepts:

- finite canonical outcomes and first-class abstention;
- separation of canonical outcomes, native engine results, and operational state;
- stable, public-safe reasons and obligation preservation;
- explicit input, deterministic normalization, and multi-gate composition;
- governed public interfaces, sensitive-data protections, receipts, replay, correction, and rollback;
- separation from contracts, schemas, evidence, runtime, lifecycle mutation, release, and publication authority.

It corrects repository-state claims that became stale after 2026-07-19:

- the direct lane is no longer README-only; it now contains two machine-readable `PROPOSED_INACTIVE` registries;
- stable reason, obligation, and reviewer-role candidates now exist with schemas, fixtures, validators, tests, and focused workflows;
- a closed explicit-input profile and declared-only evaluation binding now supplement the permissive parent `PolicyInputBundle` shape;
- fixture-only semantics, obligation-set, obligation-reduction, and enforcement-maturity profiles now exist;
- one bounded Pass 12 release-gate Rego profile is OPA-tested outside the direct lane;
- hosted actions in the inspected policy workflows are pinned by commit SHA, and the OPA binary is checksum-pinned;
- ADR-0029 has accepted `docs/doctrine/directory-rules.md` as the writable Directory Rules authority.

It does **not** upgrade the still-open claims: the current registries and profiles remain inactive; ADR-0020 remains proposed; the canonical schema-declared decision validator and policy path remain absent; no accepted general evaluator, authenticated emitter, active bundle selector, production consumer, decision receipt flow, release integration, or publication effect is established.

---

## Outcome axes must remain separate

KFM decision systems need at least three distinct axes. Collapsing them creates policy drift.

| Axis | Examples | Current status | Rule |
|---|---|---:|---|
| Canonical finite outcome | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | **SCHEMA-CONFIRMED** | Exactly one value in `PolicyDecision.outcome`. |
| Engine-native result | `ALLOW`, `RESTRICT`, `HOLD`, `PASS`, `FAIL`, evaluator-specific values | **PROPOSED / CONFLICTED** | Internal only until deterministically normalized. |
| Operational/review state | `HOLD`, `REVIEW_REQUIRED`, `QUARANTINED`, `STALE`, `SUPERSEDED` | **PROPOSED** | Must not be inserted into `PolicyDecision.outcome`. Use a separate accepted carrier. |

> [!WARNING]
> The current `PolicyDecision` schema has `additionalProperties: false` and no `operational_state` field. A producer cannot safely add `HOLD`, `review_state`, `supersedes`, `evidence_refs`, `bundle_ref`, `input_hash`, or `decision_hash` to that object without a deliberate schema revision. Until an accepted carrier exists, preserve those details in a paired runtime envelope, review record, receipt, or other governed record rather than creating ad hoc properties.

---

## Canonical PolicyDecision outcomes

The current schema confirms this exhaustive output surface:

```text
ANSWER | ABSTAIN | DENY | ERROR
```

| Outcome | Use when | Must preserve | Must not imply |
|---|---|---|---|
| `ANSWER` | The evaluated operation may proceed within the supplied context and all obligations are enforceable. | Scope, policy family, reasons, obligations, evaluation time, and external evidence/release references where required. | Truth by itself, release approval, unrestricted access, or permission outside the evaluated context. |
| `ABSTAIN` | A cited, policy-passed result cannot be responsibly produced because evidence, source authority, scope, freshness, corroboration, or required review support is unresolved. | Safe reason, unresolved handles in a protected receipt/envelope, and a bounded next step where available. | Machinery failure, policy prohibition, low-confidence guessing, or silent fallback. |
| `DENY` | Policy or governance prohibits the requested access, render, capability, consent-dependent action, sensitivity exposure, promotion, or release-adjacent action. | Safe public reason and protected internal detail where authorized. | Missing evidence alone or evaluator failure. |
| `ERROR` | Shape, integrity, evaluator, bundle, registry, signature, runtime, or process machinery failed or cannot be trusted. | Failure provenance and safe non-leaking explanation. | Permission, denial on policy merits, or evidence-based abstention. |

### Narrowed-scope answers

A safely narrowed, generalized, redacted, or audience-restricted result may still be `ANSWER` only when:

- the evaluated scope is explicit;
- all obligations are understood and enforced;
- required citations and evidence support remain valid;
- the public/restricted carrier is allowed for that audience;
- release and lifecycle gates remain satisfied where relevant.

Otherwise the result must normalize to `ABSTAIN`, `DENY`, or `ERROR` according to the cause.

---

## Engine-result normalization

Engine-native results are implementation details. They must not leak directly into `PolicyDecision.outcome`.

### Proposed normalization table

| Native result or condition | Canonical outcome | Required conditions |
|---|---|---|
| `ALLOW` / `PASS` | `ANSWER` | Input valid; bundle/evaluator trusted; evidence/release context sufficient; every obligation enforceable. |
| `RESTRICT` | `ANSWER` with obligations | Only when the restricted result is fully materialized as an enforceable narrowed/redacted/generalized scope. Otherwise normalize by cause. |
| `RESTRICT` with unenforceable or unknown obligation | `ERROR` | Registry/interpreter or enforcement machinery cannot be trusted. |
| `RESTRICT` because required support is not yet available | `ABSTAIN` | Missing evidence, source resolution, freshness, corroboration, or review support—not policy prohibition. |
| `RESTRICT` because requested exposure is prohibited for the caller/audience | `DENY` | Policy blocks the requested operation; a separate narrower request may be evaluated independently. |
| `HOLD` / review pending | `ABSTAIN` plus separate operational/review state | Machinery is healthy but the system cannot responsibly proceed yet. Current `PolicyDecision` shape cannot carry the state directly. |
| Policy rule explicitly blocks | `DENY` | Preserve safe reason code and no protected detail leakage. |
| Evidence unresolved or stale beyond policy | `ABSTAIN` | Preserve unresolved handles in a governed receipt/envelope where safe. |
| Shape, bundle, registry, signature, evaluator, or runtime failure | `ERROR` | Do not downgrade machinery failure to improve availability metrics. |
| Generic `FAIL` | **NO DEFAULT** | Classify the cause first. Structural/machinery failure is `ERROR`; policy prohibition is `DENY`; insufficient support is `ABSTAIN`. |

This mapping is **PROPOSED**. It requires an accepted ADR or equivalent governance decision, fixtures, tests, runtime implementation, and consumer agreement before use.

### Normalization invariants

A future normalizer must:

- accept explicit native result, policy family, gate identity, bundle digest, evaluator identity/version, and input digest;
- reject unknown native result values;
- reject unknown reason codes or obligations unless the accepted registry explicitly permits extension;
- preserve all obligations through mapping;
- make scope narrowing explicit;
- never convert `ERROR` into `ABSTAIN` or `DENY` to hide machinery failure;
- never convert `ABSTAIN` into `ANSWER` through a model fallback;
- never convert `DENY` into `ABSTAIN` to soften a policy prohibition;
- emit deterministic output for identical canonical inputs and pinned policy/evaluator versions;
- record enough protected process memory for replay without leaking sensitive inputs.

---

## Required evaluation input

A trustworthy decision cannot be produced from the permissive parent `PolicyInputBundle` shape alone. The repository now contains a closed [explicit context profile v1](../../contracts/policy/policy_input_bundle_profile_v1.md), its [schema](../../schemas/contracts/v1/policy/policy_input_bundle_profile_v1.schema.json), fixtures, deterministic validator, tests, and focused workflow. That profile is `PROPOSED_INACTIVE` and checks coherence; it does not evaluate policy.

The profile currently admits five operations:

`ANSWER | RENDER | EXPORT | PROMOTE | RELEASE`

and seven audiences:

`PUBLIC | RESTRICTED_REVIEW | STEWARD | INTERNAL | AI_ADAPTER | MAP_RUNTIME | RELEASE_GATE`

It makes subject, evidence, source, rights, sensitivity, review, release, evaluator, and false-governance context explicit. Its validator requires, among other things, resolved evidence and passing citations for answer/render/export operations, public-safe rights and sensitivity posture for public audiences, and review/rollback bindings for promotion and release. Those checks are useful pre-evaluator evidence, not a decision.

A future accepted evaluation should bind at least:

| Input family | Minimum content | Failure posture |
|---|---|---|
| Request/gate identity | request or operation id, gate id, policy family, intended action | `ERROR` if malformed or unrecognized. |
| Subject/object scope | governed object ref, requested fields/geometry/action, audience, purpose | `ABSTAIN` if scope cannot be responsibly resolved; `DENY` if prohibited. |
| Caller/access context | authenticated role, capability, and consent context where required | `DENY` when authorization is missing or invalid. |
| Evidence context | EvidenceRefs, resolution/closure status, citation readiness, freshness, contradiction state | `ABSTAIN` when support is insufficient; `ERROR` on resolver integrity failure. |
| Source context | source id, role, authority, rights, cadence, and limitation flags | `ABSTAIN` or `DENY` according to whether support is unresolved or prohibited. |
| Rights/consent/sensitivity | rights, license, consent, geoprivacy, cultural/ecological/infrastructure restrictions | Fail closed; the most restrictive applicable posture wins. |
| Lifecycle/release context | lifecycle state, release state, correction/withdrawal/supersession state, rollback target | `DENY`, `ABSTAIN`, or `ERROR` according to the accepted gate contract. |
| Policy bundle context | bundle id, version, digest, dependency closure, activation and selection evidence | `ERROR` when missing, stale, untrusted, or not reproducible. |
| Evaluator context | engine, adapter/version, timeout, and deterministic configuration | `ERROR` when unavailable or untrusted. |
| Registry context | reason, obligation, reviewer, and normalization profile versions | `ERROR` when incompatible or unavailable. |
| Replay/audit context | canonical input digest, correlation id, evaluated time, and protected unresolved handles | Required for consequential decisions and correction investigation. |

### Explicit-input rule

Policy evaluation must not secretly fetch or infer facts from model memory, the public internet, canonical or internal stores, environment variables, or unreviewed caches. Any permitted retrieval must occur through an admitted, observable, policy-aware dependency whose output becomes part of the governed input and replay record.

### Declared-only binding is not execution

The [evaluation binding v1](../../contracts/policy/policy_evaluation_binding_v1.md) records SHA-256 digests for one exact input fixture and one exact decision fixture and checks that their evaluator declarations agree. Its execution mode is fixed to `DECLARED_ONLY`. A passing binding proves byte identity and declaration coherence only—not that OPA, Rego, or another evaluator executed, and not that the decision is authentic.

---

## Reason-code boundary

The direct [`vocabulary.v1.json`](vocabulary.v1.json) registry is a real machine-readable candidate, but its status is explicitly `PROPOSED_INACTIVE`. It contains nine sorted, unique reason codes. The paired contract, schema, fixtures, validator, unit tests, and [focused workflow](../../.github/workflows/policy-decision-vocabulary.yml) enforce bounded shape and coherence without activating policy.

| Reason code | Canonical outcome | Bounded meaning |
|---|---|---|
| `CONSENT_REQUIRED` | `DENY` | Required consent is absent, expired, revoked, or out of scope. |
| `EVIDENCE_STALE` | `ABSTAIN` | Evidence is outside the admitted freshness window. |
| `EVIDENCE_UNRESOLVED` | `ABSTAIN` | Required EvidenceRefs do not resolve to admissible support. |
| `OPERATION_ALLOWED_WITH_OBLIGATIONS` | `ANSWER` | The bounded operation may proceed only after every attached obligation is enforced. |
| `POLICY_BUNDLE_UNAVAILABLE` | `ERROR` | Bundle or evaluator context is missing, stale, or unverifiable. |
| `POLICY_INPUT_INCOMPLETE` | `ERROR` | Explicit operation, audience, evidence, rights, sensitivity, review, release, or evaluator context is incomplete. |
| `PUBLIC_PRECISION_UNSAFE` | `DENY` | Requested public precision exceeds the approved public-safe posture. |
| `RIGHTS_UNKNOWN` | `DENY` | Storage, transformation, redistribution, attribution, export, or public-use rights are unresolved. |
| `SENSITIVITY_UNRESOLVED` | `DENY` | Sensitivity classification or required public-safe transformation is unresolved. |

Every current reason description is marked `public_safe: true`, but that flag is a candidate-registry declaration—not proof that every runtime message or contextual detail is safe to expose.

The validator checks:

1. JSON Schema Draft 2020-12 shape;
2. sorted, unique reason and obligation entries;
3. sorted, unique policy-family arrays;
4. disjoint reason and obligation namespaces;
5. `ANSWER`-only obligation applicability in v1;
6. all governance authority flags remain `false`;
7. deterministic findings that do not echo untrusted values.

The separate [semantics profile v1](../../contracts/policy/policy_decision_semantics_profile_v1.md) checks synthetic `PolicyDecision` records against this inactive registry: codes must exist, match the decision outcome and policy family, negative outcomes need at least one reason and no obligations, `ANSWER` needs a reason, and `OPERATION_ALLOWED_WITH_OBLIGATIONS` requires at least one obligation. Passing proves shape plus candidate-vocabulary coherence only.

### Reason safety rules

Reason records and public explanations must not contain:

- exact protected locations;
- living-person, genomic, or consent-revocable details;
- credentials, secrets, internal tokens, or raw prompts;
- restricted source excerpts or private review notes;
- private land/title joins or sensitive infrastructure details;
- hidden thresholds, transform seeds, offsets, or reversal instructions;
- untrusted exception text, stack traces, or chain-of-thought.

Public explanations should reveal enough to understand the outcome and next safe step without revealing what the policy protects. Internal detail belongs only in an accepted protected carrier with explicit retention and access rules.

### Change and compatibility discipline

Adding, renaming, reclassifying, or removing a reason code is a compatibility change. Before activation, governance must define aliases, deprecation, consumer compatibility, bundle and registry version binding, correction behavior, and how historical decisions remain replayable. No caller may treat an unknown code as `ANSWER` or silently discard it.

---

## Obligation boundary

The same inactive registry contains eight sorted obligation codes. Version 1 allows them only on `ANSWER`.

| Obligation code | Required downstream effect |
|---|---|
| `ATTACH_CITATIONS` | Carry resolvable evidence citations into the governed response or release surface. |
| `ATTACH_RIGHTS_NOTICE` | Carry approved attribution, license, terms, or reuse notice. |
| `DELAY_PUBLICATION` | Prevent exposure until the approved embargo or delayed-release condition ends. |
| `GENERALIZE_GEOMETRY` | Replace exact geometry with the approved generalized representation. |
| `REDACT_EXACT_LOCATION` | Remove exact coordinates or location-bearing attributes before exposure. |
| `REQUIRE_STEWARD_REVIEW` | Require the named steward or qualified reviewer to approve the exact candidate version. |
| `VERIFY_ROLLBACK_TARGET` | Confirm an executable rollback target before promotion or release. |
| `WITHHOLD_EXPORT` | Permit bounded viewing while blocking download or bulk export. |

These are stable candidate tokens, not proof of enforcement. In particular, `REQUIRE_STEWARD_REVIEW` does not name a person, authenticate a review record, or grant approval.

The repository also contains two related fixture-first object families:

- [`PolicyObligationSet`](../../contracts/policy/policy_obligation_set.md) represents structured candidate duties and provenance without evaluating policy or authorizing effects.
- [`PolicyObligationReduction`](../../contracts/policy/policy_obligation_reduction.md) deterministically reduces declared obligation carriers without resolving or authenticating their decision references and without applying a transform.

A future active obligation system still needs:

| Concern | Requirement |
|---|---|
| Identity | Accepted stable code, registry version, aliases, and deprecation policy. |
| Parameters | Typed, bounded values for precision, audience, expiry, citation, transform, review, or rollback requirements. |
| Interpreter | Named consumer capability that deterministically understands the exact version. |
| Enforcement proof | Receipt or runtime evidence that the duty was applied before the protected action. |
| Compatibility | Consumers reject unknown or unsupported codes and versions. |
| Composition | Duties from every applicable gate are preserved, deduplicated, and tightened—not weakened. |
| Expiry and correction | Stale, withdrawn, or superseded duties trigger re-evaluation and carrier invalidation. |

> [!IMPORTANT]
> Unknown obligations must never be ignored. If an `ANSWER` depends on an obligation the consumer cannot interpret or prove enforced, the safe result is `ERROR` for contract/interpreter failure or a newly evaluated `ABSTAIN` or `DENY` according to the underlying policy cause—never silent success.

---

## Multi-gate composition

Composition must occur **after** every native result is normalized into the canonical four outcomes.

ADR-0020 proposes:

```text
ERROR > DENY > ABSTAIN > ANSWER
```

Until that ADR or an equivalent decision is accepted, this order remains **PROPOSED** even though it aligns with the current four-outcome schemas.

### Proposed composition algorithm

1. Verify every child decision is schema-valid and tied to the expected gate, bundle, input, and registry versions.
2. Reject stale, unsigned, contradictory, duplicated, or context-mismatched child decisions.
3. Normalize native engine results before composition.
4. Select the most protective canonical outcome.
5. Union and deterministically order all compatible obligations.
6. Preserve gate-specific reason codes; do not collapse distinct causes into one free-text summary.
7. Narrow the result scope to the intersection of all allowed scopes.
8. If obligations conflict or cannot be enforced, return `ERROR` rather than choosing arbitrarily.
9. Record the child decision identifiers/digests in a governed external receipt or envelope; the current `PolicyDecision` shape cannot carry them.

### Composition examples

| Child outcomes | Composite outcome | Notes |
|---|---|---|
| `ANSWER`, `ANSWER` | `ANSWER` | All obligations and allowed scopes must be combined. |
| `ANSWER`, `ABSTAIN` | `ABSTAIN` | One unresolved evidence/source/review dependency prevents a complete cited result. |
| `ANSWER`, `DENY` | `DENY` | Policy prohibition dominates. |
| `ABSTAIN`, `ERROR` | `ERROR` | Machinery failure must remain visible. |
| `DENY`, `ERROR` | `ERROR` | Do not hide broken governance machinery behind a denial. |

A composite outcome never grants authority outside the exact evaluated scope and does not replace release approval.

---

## Identity, replay, freshness, and supersession

A decision is only inspectable when the system can explain exactly what was evaluated and reproduce the result.

### Proposed identity inputs

A deterministic or traceable decision identity should bind:

- canonical request/gate identity;
- policy family;
- governed subject/object reference;
- canonical input digest;
- bundle digest;
- evaluator/normalizer version;
- reason/obligation registry versions;
- evaluation timestamp or run identity where nondeterministic time context matters.

Illustrative format:

```text
poldec:<run-or-request>:<policy-family>:<digest-prefix>
```

The exact format is `NEEDS VERIFICATION`.

### Replay requirements

A replay system should be able to determine:

- whether the same canonical input and pinned policy/evaluator versions produce the same outcome, reasons, and obligations;
- whether an outcome changed because input facts, evidence, source authority, rights, consent, sensitivity, release state, policy bundle, registry, or evaluator changed;
- whether a previous decision was stale, superseded, corrected, withdrawn, or invalidated;
- whether a public carrier stopped using an invalidated decision.

### Current shape limitation

`PolicyDecision` has no fields for input digest, bundle digest, evaluator version, registry version, evidence refs, child decisions, expiry, or supersession. Do not invent those properties in a schema-closed object. Use an accepted paired receipt/envelope/index or revise the schema deliberately with contracts, fixtures, tests, migration, and rollback.

### Mutation rule

Do not edit an emitted decision to change its outcome or time. Correction and supersession should create a new governed record and retain the earlier record as audit history.

---

## Lifecycle and release boundary

Policy decisions may support gates throughout:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

They do not move artifacts through that lifecycle.

| Stage or action | Decision role | Additional authority required |
|---|---|---|
| Source admission / RAW | Evaluate known source, rights, sensitivity, and capability context. | Source admission, connector policy, provenance, and intake receipt. |
| WORK / QUARANTINE | Evaluate whether processing may continue or material must remain held. | Validation, steward review, quarantine-exit record, and transform provenance. |
| PROCESSED | Evaluate admissibility for catalog/triplet projection. | Contract/schema validity, evidence, source role, and validation support. |
| CATALOG / TRIPLET | Evaluate access, render, export, graph, and claim exposure. | Evidence closure, public-safe projection rules, and governed interface. |
| PUBLISHED candidate | Evaluate policy prerequisites for release. | ReleaseManifest, review, proof, rights, sensitivity, integrity, correction, and rollback authority. |
| Correction / withdrawal / rollback | Re-evaluate affected operations and carriers. | Governed release/correction records and downstream invalidation. |

`ANSWER` for `policy_family=promotion` is not a `PromotionDecision`. `ANSWER` for `policy_family=render` is not a release. Policy families identify context; they do not collapse adjacent object families.

---

## Public interface and sensitive data boundary

Public clients must receive decision-aware responses only through governed interfaces. They must not:

- read policy bundles directly;
- choose policy versions or evaluators;
- read internal decision, receipt, evidence, RAW, WORK, QUARANTINE, PROCESSED, catalog, triplet, or release stores;
- treat a missing decision as permission;
- treat `ANSWER` as release approval;
- ignore unknown obligations;
- reveal internal reason details or protected unresolved handles.

### Surface behavior

| Outcome | Public-safe behavior |
|---|---|
| `ANSWER` | Return only the evaluated, released, policy-cleared, obligation-compliant scope with citations where required. |
| `ABSTAIN` | Show a bounded explanation and allowed next step; preserve unresolved handles only in protected audit records. |
| `DENY` | Refuse the operation and expose only a safe reason. Do not confirm protected facts through the denial wording. |
| `ERROR` | Fail closed with a safe error and correlation handle. Do not infer permission or truth. |

### Sensitive-domain posture

Living-person data, DNA/genomic context, archaeology, cultural knowledge, rare-species locations, critical infrastructure, private land/title joins, consent-revocable data, and precise protected locations require most-restrictive handling across all gates.

When rights, consent, sovereignty, sensitivity, or reconstruction risk is unresolved, prefer:

- `ABSTAIN` when support is incomplete;
- `DENY` when policy prohibits the operation;
- `ERROR` when governance machinery cannot be trusted;
- staged review, redaction, generalization, delayed exposure, restricted access, quarantine, correction, or withdrawal through their owning systems.

---

## Validation, negative cases, and CI

### Confirmed current coverage

| Surface | Positive evidence | Negative or boundary evidence | What passing proves |
|---|---|---|---|
| Base `PolicyDecision` shape | Two valid JSON fixtures | Three invalid JSON fixtures | Six-field schema shape only. |
| Decision vocabulary v1 | Candidate registry plus valid fixture | Invalid fixture and mutation tests for ordering, collision, unsupported outcome, and authority overclaim | Inactive registry shape and deterministic semantic invariants. |
| Decision semantics v1 | One valid `ANSWER` fixture | Unit-test mutations for unknown codes, outcome/family mismatch, negative obligations, missing reason/obligation, and noncanonical arrays | Base shape plus inactive vocabulary coherence. |
| Reviewer-role vocabulary v1 | Five-code registry and passing registry/case checks | Duplicate role and authority-leak tests | Candidate role/scopes invariants; no assignment or approval. |
| Explicit input profile v1 | Closed valid fixture | Invalid shape and semantic mutations | Bounded input coherence; no policy result. |
| Evaluation binding v1 | Exact-byte valid binding | Digest-substitution denial | File identity and evaluator declaration coherence; no execution. |
| Obligation set | Valid structured candidate | Schema, authority, canonicalization, parameter, and hash failures | Fixture-only carrier coherence. |
| Obligation reduction | Five valid reduction cases | Shape, governance, transform, ordering, weakening, provenance, identity, and hash failures | Mechanical reduction of declared inputs only. |
| Enforcement maturity | Cumulative-stage fixture cases | Maturity overclaim and identity failures | Evidence-chain classification only; no repository-setting or runtime proof. |
| Pass 12 release gate | Native Rego unit tests and allow fixture | Three deny-polarity fixtures plus deterministic deny reasons | One bounded `PROPOSED_INACTIVE` Rego profile evaluates as tested. |
| Broad policy readiness | Static inventory and drift guards | Unexpected evaluator, bundle payload, runtime implementation, or canonical validator causes a hold failure | The guarded repository boundary has not silently graduated. |

### Focused commands

From a repository checkout with declared dependencies installed:

```bash
# Base contract/schema fixtures.
python -m pytest tests/schemas/test_common_contracts.py -q -k policy_decision

# Inactive reason/obligation vocabulary.
python -m unittest discover   --start-directory tests/validators   --pattern 'test_validate_policy_decision_vocabulary.py'   --verbose
python tools/validators/policy/validate_policy_decision_vocabulary.py --registry

# Inactive PolicyDecision semantic binding.
python -m unittest discover   --start-directory tests/validators   --pattern 'test_validate_policy_decision_semantics_v1.py'   --verbose
python tools/validators/policy/validate_policy_decision_semantics_v1.py   fixtures/contracts/v1/policy/policy_decision_semantics_v1/valid_answer.json

# Candidate reviewer-role vocabulary.
python -m unittest tests.validators.test_validate_policy_reviewer_role_vocabulary -v
python tools/validators/policy/validate_policy_reviewer_role_vocabulary.py --registry
python tools/validators/policy/validate_policy_reviewer_role_vocabulary.py --fixtures
```

The hosted [Pass 12 workflow](../../.github/workflows/pass12-release-policy-v1.yml) installs checksum-pinned OPA 1.19.0, verifies checkout provenance, runs `opa fmt --fail` and native `opa test`, checks allow/deny fixture polarity, and verifies stable deny reasons. Reproduce that exact binary version and checksum rather than substituting an unpinned evaluator.

### Required future decision matrix

| Case | Expected result |
|---|---|
| Fully supported, policy-passed operation | `ANSWER` with every applicable obligation enforced. |
| Missing EvidenceBundle resolution | `ABSTAIN`; no generated fallback. |
| Stale evidence beyond accepted policy | `ABSTAIN` or the accepted freshness outcome; never stale `ANSWER`. |
| Unauthorized caller or revoked consent | `DENY`; downstream invalidation where applicable. |
| Unsafe exact public location | Safely narrowed `ANSWER` with enforced generalization, or `DENY` when narrowing is not allowed. |
| Review pending | `ABSTAIN` plus a separate accepted review/hold state. |
| Bundle digest missing or untrusted | `ERROR`. |
| Unknown native engine result | `ERROR`. |
| Unknown reason, obligation, reviewer role, or registry version | `ERROR`; never ignore. |
| `RESTRICT` maps to safe narrowed output | `ANSWER` only when typed obligations are enforceable and proven. |
| Restriction cannot be enforced | `ERROR`, `DENY`, or `ABSTAIN` according to cause; never unrestricted `ANSWER`. |
| Conflicting child obligations | `ERROR` until an accepted reducer resolves the conflict without weakening. |
| Child `ERROR` plus child `DENY` | Composite `ERROR`. |
| Public reason attempts sensitive disclosure | Validation failure and safe `ERROR` response. |
| Same fixture bytes but no evaluator execution evidence | No authenticated decision; remain `DECLARED_ONLY`. |
| Replay uses changed bundle, registry, or evaluator version | New decision identity; prior result remains auditable and potentially stale. |
| `ANSWER` lacks release support | Release remains blocked. |
| Correction or withdrawal invalidates support | Prior decision becomes unusable; re-evaluation and carrier invalidation are required. |

### CI maturity

| Capability | Current posture |
|---|---|
| Base `PolicyDecision` schema and fixture shape | **CONFIRMED fixture-tested** |
| Candidate reason/obligation vocabulary | **CONFIRMED `PROPOSED_INACTIVE` / fixture-tested** |
| Candidate decision semantic binding | **CONFIRMED `PROPOSED_INACTIVE` / fixture-tested** |
| Candidate reviewer-role vocabulary | **CONFIRMED `PROPOSED_INACTIVE` / fixture-tested** |
| Explicit input coherence | **CONFIRMED `PROPOSED_INACTIVE` / fixture-tested** |
| Exact-byte evaluation declaration binding | **CONFIRMED `DECLARED_ONLY` / fixture-tested** |
| Structured obligation carriers and reduction | **CONFIRMED fixture-only** |
| One bounded native Rego release gate | **CONFIRMED OPA-tested / `PROPOSED_INACTIVE`** |
| Canonical evaluator-bound `PolicyDecision` validator | **ABSENT AT DECLARED PATH** |
| Accepted native-to-canonical normalizer | **NOT ESTABLISHED** |
| Authenticated decision emission | **NOT ESTABLISHED** |
| Production obligation interpretation and proof | **NOT ESTABLISHED** |
| Runtime consumer, receipt, replay, release, and correction integration | **UNKNOWN / NOT ESTABLISHED** |
| Rulesets, branch protection, and required-check coupling | **UNKNOWN** |

### Workflow threat posture for this documentation change

The inspected policy workflows:

- use GitHub-hosted runners and read-only repository permissions;
- pin checkout and setup actions by full commit SHA;
- set deterministic/no-network environment flags for fixture-only Python validators;
- use repository-declared dependency installation where required;
- checksum-pin OPA 1.19.0 in the bounded native Rego workflow;
- emit no decision, receipt, promotion, release, deployment, publication, or public-use authority.

The focused workflows are path-filtered to their governed artifacts and do not necessarily run for this README-only change. The broad `policy-test` workflow runs on pull requests, but its success remains a readiness result. Required-check and ruleset configuration is still `UNKNOWN` until verified from GitHub settings or equivalent evidence.

---

## Review burden and separation of duties

The direct [reviewer-role registry](reviewer_roles.v1.json) provides stable candidate role **classes**, not assignments:

| Role code | Declared review scopes | Boundary |
|---|---|---|
| `DOMAIN_STEWARD` | domain, policy | Reviews domain meaning, burden, and admissibility implications. |
| `EVIDENCE_STEWARD` | evidence, policy, release | Reviews EvidenceRef resolution, provenance, freshness, and evidence burden. |
| `POLICY_STEWARD` | policy | Reviews policy source, finite outcomes, reasons, obligations, and fail-closed behavior. |
| `RELEASE_STEWARD` | release | Reviews release eligibility, rollback, correction, proof, and publication separation. |
| `SECURITY_PRIVACY_REVIEWER` | policy, security/privacy | Reviews privacy, access, living-person, sensitive-location, and exposure controls. |

Every governance flag in the registry is `false`. A role code does not prove that a qualified person exists, is assigned, is independent, reviewed the exact bytes, or approved anything.

Consequential changes should also involve contract, schema, runtime, API, validation, source, rights, consent, and documentation owners when those responsibilities are affected. A generator, rule author, registry editor, evaluator maintainer, reviewer, and release approver must not be treated as automatically interchangeable.

Changes requiring especially strong review include:

- canonical outcome or composition changes;
- native-to-canonical normalization mappings;
- reason, obligation, reviewer-role, or alias changes;
- bundle selection, evaluator, or registry-version changes;
- public reason wording for sensitive cases;
- schema compatibility or decision-identity changes;
- obligation interpreter and enforcement-proof changes;
- receipt/replay retention changes;
- promotion, release, correction, withdrawal, or rollback coupling.

CODEOWNERS routes `/policy/` to `@bartytime4life`. That is a repository review route, not proof of semantic acceptance, independent review, policy evaluation, or release authorization.

---

## Smallest sound implementation sequence

Current inactive profiles reduce design ambiguity, but activation still requires explicit governance. The smallest sound sequence is:

1. **Resolve the outcome decision.** Accept, amend, or supersede ADR-0020 and pin canonical outcome precedence separately from native results and operational state.
2. **Review the candidate vocabularies.** Accept or revise reason, obligation, and reviewer-role codes; define aliases, deprecation, version negotiation, public-safety review, and historical compatibility.
3. **Reconcile the base schema metadata.** Resolve the absent `policy/policy/` and `tools/validators/validate_policy_decision.py` declarations without creating a parallel policy root or silently repurposing the fixture-only semantics validator.
4. **Choose the first governed input profile.** Accept or narrow the explicit input profile for one consumer and verify source, evidence, rights, consent, sensitivity, review, release, and evaluator bindings.
5. **Accept a bundle and evaluator contract.** Pin manifest, digest, dependency closure, selector, evaluator binary/adapter, timeout, deterministic configuration, availability behavior, and rollback.
6. **Implement native-result normalization.** Produce the canonical four outcomes from accepted native results; reject unknown values and preserve cause, scope, and obligations.
7. **Add evaluator-bound decision fixtures.** Cover all four outcomes, vocabulary failures, input failures, normalization, sensitive reasons, obligation conflicts, replay, freshness, and composition.
8. **Establish canonical validation and emission.** Implement the accepted validator/emitter boundary, authenticated identity, deterministic serialization, and protected process memory.
9. **Implement obligation consumers.** Prove each accepted obligation is supported, applied before the protected effect, and recorded without leaking restricted context.
10. **Integrate one governed non-public consumer.** Verify fail-closed behavior and replay before broad API, map, AI, export, or release adoption.
11. **Integrate release and correction.** Prove that a policy decision is required but insufficient for publication and that correction, withdrawal, supersession, and rollback invalidate downstream use.
12. **Graduate CI deliberately.** Make evaluator-backed checks required through reviewed repository settings while retaining explicit distinctions among fixture-tested, merge-blocking, promotion-blocking, and runtime-enforced maturity.

Each increment should be independently reviewable, content-addressed where consequential, and reversible without mutating historical decisions.

---

## Definition of done

### Evidence foundation already present

These checked items describe repository evidence, not activation:

- [x] A closed six-field `PolicyDecision` schema and minimal positive/negative shape fixtures exist.
- [x] Versioned candidate reason and obligation codes exist with schema, fixtures, deterministic validation, tests, and focused CI.
- [x] Versioned candidate reviewer-role codes exist with fixtures, validation, tests, and focused CI.
- [x] A closed explicit-input profile exists with valid/invalid evidence and no hidden-fetch authority.
- [x] A declared-only exact-byte evaluation binding exists and rejects digest substitution.
- [x] Fixture-only decision semantics, obligation-set, obligation-reduction, and enforcement-maturity profiles exist.
- [x] One bounded `PROPOSED_INACTIVE` release-gate Rego profile has native OPA tests and exact-polarity fixtures.

### Activation and operational closure

This lane is not operationally complete until every applicable item below is closed:

- [ ] Policy owners, qualified reviewers, independent review duties, evaluator owner, and release authority are assigned.
- [ ] ADR-0020 is accepted, amended, or superseded with an explicit outcome/composition decision.
- [ ] Candidate vocabularies are accepted or replaced with compatibility and deprecation rules.
- [ ] Reviewer codes are bound to authenticated assignments and review records where required.
- [ ] Native engine normalization is versioned, deterministic, documented, and tested.
- [ ] Operational and review states have a separate accepted carrier.
- [ ] The first `PolicyInputBundle` profile is accepted for a named consumer.
- [ ] `PolicyDecision` compatibility, identity, registry binding, and migration policy are accepted.
- [ ] Gate and normalization registries are populated or an accepted alternative is named.
- [ ] Bundle format, manifest, selector, digest, evaluator, and rollback contract are accepted.
- [ ] Canonical evaluator-bound validation and authenticated decision emission exist.
- [ ] Unknown results, reasons, obligations, roles, and registry versions fail closed.
- [ ] Multi-gate composition preserves the most protective outcome and every compatible obligation.
- [ ] Every active obligation has a supported interpreter and enforcement proof.
- [ ] Decision receipts support replay without leaking sensitive data.
- [ ] Stale, corrected, withdrawn, or superseded decisions cannot remain active silently.
- [ ] At least one governed consumer enforces outcomes and obligations end to end.
- [ ] Public clients receive only governed, release-aware, public-safe envelopes.
- [ ] Release approval remains separate and requires its own records and reviewers.
- [ ] Evaluator-backed checks are verified as required where policy demands merge blocking.
- [ ] Correction and rollback drills are documented and tested.

---

## Open verification register

| Item | Status | Why it matters |
|---|---:|---|
| Accepted decision-policy owner and independent reviewers | `NEEDS VERIFICATION` | CODEOWNERS confirms one route, not accepted role assignment or separation of duties. |
| ADR-0020 acceptance or supersession | `NEEDS VERIFICATION` | Pins exhaustive outcomes and composition precedence. |
| Direct child layout | `CONFIRMED PARTIAL` | README plus two inactive registries exist; executable child naming remains unaccepted. |
| Parent `PolicyInputBundle` field set | `CONFIRMED PERMISSIVE` | Parent shape cannot prove complete context. |
| Explicit input profile v1 | `CONFIRMED / PROPOSED_INACTIVE` | Useful closed profile exists; consumer acceptance and runtime use remain open. |
| `PolicyDecision` compatibility strategy | `NEEDS VERIFICATION` | Closed shape lacks bundle, registry, evidence, replay, and supersession fields. |
| Native-result normalization profile | `NOT ESTABLISHED` | Prevents `allow`, `restrict`, `hold`, `pass`, and `fail` drift. |
| Operational-state carrier | `NEEDS VERIFICATION` | Prevents `HOLD` or review state from leaking into canonical outcome. |
| Reason/obligation registry | `CONFIRMED / PROPOSED_INACTIVE` | Candidate codes exist; activation, aliases, and consumer negotiation do not. |
| Reviewer-role registry | `CONFIRMED / PROPOSED_INACTIVE` | Candidate classes exist; people, qualification, independence, and approval records do not. |
| Obligation interpreter and enforcement proof | `NOT ESTABLISHED` | Candidate code presence cannot make an `ANSWER` safe. |
| Gate and normalization machine registries | `NEEDS VERIFICATION` | The machine policy-gate projection remains empty. |
| Accepted general evaluator and bundle selection | `UNKNOWN` | One bounded inactive Rego profile does not establish a general evaluator. |
| Canonical evaluator-bound decision validator | `CONFIRMED ABSENT` | The schema-declared path remains held. |
| Authenticated decision emitter | `NOT ESTABLISHED` | Fixture coherence is not decision authenticity. |
| Receipt and replay record family | `NEEDS VERIFICATION` | Required to reproduce consequential decisions and corrections. |
| EvidenceRef/EvidenceBundle binding | `NEEDS VERIFICATION` | Base `PolicyDecision` cannot carry evidence refs. |
| Production consumer inventory | `UNKNOWN` | Bounded repository inspection does not prove exhaustive absence or use. |
| Promotion, release, correction, and rollback integration | `UNKNOWN` | A decision must not become de facto release authority. |
| Metrics and abstain/deny/error observability | `NEEDS VERIFICATION` | Needed to detect fallback, manipulation, and machinery failure. |
| Rulesets, required checks, and branch protection | `UNKNOWN` | Workflow files alone do not prove merge blocking. |
| Canonical Directory Rules path | `CONFIRMED` | ADR-0029 accepts `docs/doctrine/directory-rules.md`; the architecture body remains read-only compatibility pending migration. |

---

## Evidence ledger

| Evidence | Verified observation | Status |
|---|---|---:|
| [`policy/decision/README.md`](./README.md) at `main@1a61d3fb…` | v0.2 baseline; Git blob `1ab41e00…` and 51,208 bytes. | `CONFIRMED` |
| [`policy/decision/vocabulary.v1.json`](vocabulary.v1.json) | Nine reason codes, eight obligation codes, `PROPOSED_INACTIVE`, and all governance flags false. | `CONFIRMED CANDIDATE` |
| [`policy/decision/reviewer_roles.v1.json`](reviewer_roles.v1.json) | Five role codes, five finite review scopes, `PROPOSED_INACTIVE`, and no assignment/approval authority. | `CONFIRMED CANDIDATE` |
| [Decision vocabulary contract](../../contracts/policy/policy_decision_vocabulary.md), [schema](../../schemas/contracts/v1/policy/policy_decision_vocabulary.schema.json), validator, tests, and workflow | Closed fixture-only registry checks and deterministic no-network validation. | `CONFIRMED IMPLEMENTATION / INACTIVE` |
| [Decision semantics profile v1](../../contracts/policy/policy_decision_semantics_profile_v1.md), validator, tests, and workflow | Checks base schema plus inactive code coherence; intentionally does not satisfy the held canonical validator path. | `CONFIRMED IMPLEMENTATION / INACTIVE` |
| [Reviewer-role contract](../../contracts/policy/policy_reviewer_role_vocabulary.md), [schema](../../schemas/contracts/v1/policy/policy_reviewer_role_vocabulary.schema.json), validator, tests, and workflow | Checks candidate role vocabulary without assigning people or recording approval. | `CONFIRMED IMPLEMENTATION / INACTIVE` |
| [`PolicyDecision` contract](../../contracts/policy/policy_decision.md) and [schema](../../schemas/contracts/v1/policy/policy_decision.schema.json) | Six required fields, four outcomes, six families, and closed additional properties. | `CONFIRMED SHAPE / PROPOSED STATUS` |
| [Base decision fixtures](../../fixtures/contracts/v1/policy/policy_decision/README.md) | Two valid and three invalid instances. | `CONFIRMED MINIMAL SHAPE COVERAGE` |
| [Explicit input profile v1](../../contracts/policy/policy_input_bundle_profile_v1.md) | Closed profile for five operations and seven audiences; no evaluator authority. | `CONFIRMED IMPLEMENTATION / INACTIVE` |
| [Evaluation binding v1](../../contracts/policy/policy_evaluation_binding_v1.md) | Exact-byte binding and declaration coherence with `DECLARED_ONLY` execution. | `CONFIRMED IMPLEMENTATION / NON-EXECUTION` |
| [Obligation set](../../contracts/policy/policy_obligation_set.md) and [reduction](../../contracts/policy/policy_obligation_reduction.md) | Structured fixture-first candidates with deterministic validators and negative evidence. | `CONFIRMED IMPLEMENTATION / INACTIVE` |
| [`policy-test`](../../.github/workflows/policy-test.yml) | Broad readiness and drift hold; no policy evaluation or decision emission. | `CONFIRMED WORKFLOW` |
| [Pass 12 Rego](../rego/release_gate_v1.rego), tests, fixtures, and [workflow](../../.github/workflows/pass12-release-policy-v1.yml) | Native `allow` and sorted deny reasons tested with checksum-pinned OPA 1.19.0. | `CONFIRMED BOUNDED EXECUTION / PROPOSED_INACTIVE` |
| Complete `policy/**/*.rego` tree | 173 Rego files and one native Rego test file; none under `policy/decision/`. | `CONFIRMED INVENTORY` |
| [`policy/bundles/`](../bundles/README.md) | Two tracked READMEs and no non-document payload. | `CONFIRMED DOCUMENTATION-ONLY PAYLOAD SET` |
| [`packages/policy-runtime/`](../../packages/policy-runtime/README.md) | `0.0.0` package with empty initializer and comment-only core. | `CONFIRMED PLACEHOLDER` |
| [ADR-0020](../../docs/adr/ADR-0020-abstain-is-a-first-class-decision.md) | Four-outcome and abstention decision remains proposed. | `CONFIRMED FILE / PROPOSED ADR` |
| [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) and [Directory Rules v2](../../docs/doctrine/directory-rules.md) | Placement doctrine accepted; `policy/` is the canonical policy root and the doctrine path is the writable authority. | `CONFIRMED / ACCEPTED` |
| [Root Registry](../../control_plane/root_registry.yaml) | Machine projection classifies `policy/` as canonical policy-rule root without creating policy authority. | `CONFIRMED PROJECTION` |
| Exact-target PR and planned-branch preflight | No open PR touching this exact README and no `agent/modernize-policy-decision-readme-20260813` ref existed before mutation. | `CONFIRMED BOUNDED SEARCH` |

### Evidence conflicts and drift

- `policy/decision/vocabulary.v1.json` and `reviewer_roles.v1.json` are machine-checkable but explicitly `PROPOSED_INACTIVE`. Registry presence must not be described as adoption.
- The base `PolicyDecision` schema points to absent `tools/validators/validate_policy_decision.py` and `policy/policy/` paths. The focused semantics validator deliberately does not satisfy or silently rewrite those declarations.
- The broad `policy-test` summary retains older language about absent reason/obligation semantics, while newer focused fixture-only profiles now exist. The safe reading is “no accepted canonical evaluator-bound semantics,” not “no semantic test code anywhere.”
- The Pass 12 profile returns native `allow` and `deny_reasons`. No accepted adapter currently maps that object into `ANSWER | ABSTAIN | DENY | ERROR`.
- The human policy-gate register includes `HOLD`, `PASS`, and `FAIL` alongside canonical terms, while the current `PolicyDecision` shape exposes only four outcomes.
- The base `PolicyDecision` is schema-closed and has no bundle digest, evaluator version, registry version, EvidenceRefs, child decisions, expiry, operational state, or supersession field.
- Directory Rules v2 retains a pre-adoption internal label in its accepted exact bytes. ADR-0029 supplies the acceptance decision and makes the doctrine path authoritative; prose must not mistake the embedded historical label for current governance status.
- Workflow presence and green runs do not prove GitHub ruleset or required-check enforcement.

These conflicts are surfaced here; this README does not resolve them by assertion.

---

## Correction, rollback, and supersession

### Documentation rollback

Before merge, close the review pull request or abandon the review branch. After merge, revert the generated receipt and README commits in reverse order. The prior README blob is recorded in the Meta Block and PR handoff.

### Decision correction

A decision correction should:

- preserve the original decision and receipt;
- create a new decision under the accepted identity/version model;
- identify why prior support, policy, rights, consent, sensitivity, release, evaluator, registry, or input context changed;
- invalidate or re-evaluate dependent envelopes, releases, carriers, caches, indexes, exports, maps, and AI outputs;
- preserve public-safe notices without exposing protected reasons;
- never rewrite `evaluated_at` to make the old decision appear current.

### Bundle or registry rollback

Rolling back a policy bundle, reason-code registry, obligation registry, or normalizer must not silently reactivate decisions produced under the superseded version. A rollback plan should declare:

- affected bundle/registry/normalizer versions;
- affected decision and receipt digests;
- re-evaluation scope;
- public-carrier invalidation;
- release/correction implications;
- retained audit history;
- named approval and rollback authority.

---

## Maintenance triggers

Review this README whenever any of the following changes:

- direct files under `policy/decision/`;
- candidate reason, obligation, reviewer-role, alias, or deprecation rules;
- `PolicyDecision`, `PolicyInputBundle`, `PolicyObligationSet`, `PolicyObligationReduction`, or `DecisionEnvelope` contract/schema;
- ADR-0020 status or canonical outcome/composition vocabulary;
- ADR-0029 or Directory Rules placement;
- native-result normalization or operational-state carrier;
- policy bundle format, manifest, evaluator, selector, activation, or rollback contract;
- canonical validator/emitter or focused policy validators;
- direct or repository-wide Rego test posture;
- obligation interpreters or enforcement receipts;
- first runtime, API, UI, AI, map, export, promotion, or release consumer;
- decision identity, receipt, replay, correction, withdrawal, supersession, or rollback format;
- public reason-safety or sensitive-data rules;
- workflow triggers, dependency pins, required-check configuration, or branch protection.

---

## No-loss preservation note

The prior v0.2 README established a strong finite-decision operating model: canonical outcomes, native normalization, explicit input, stable reasons, obligations, composition, replay, public-interface protections, validation, implementation sequencing, and rollback.

This v0.3 preserves those concepts while replacing stale evidence claims. It distinguishes:

- the confirmed direct candidate registries from active policy;
- fixture-only semantic checking from evaluator execution and decision authentication;
- one bounded native OPA profile from a repository-wide decision runtime;
- candidate reviewer roles from people, assignments, independence, and approval;
- declared-only byte binding from replayable evaluator proof;
- structured obligation candidates from interpretation and enforcement;
- accepted Directory Rules placement from the historical status label retained inside the adopted bytes;
- policy decisions from evidence, truth, lifecycle promotion, review, release, deployment, and publication authority.

No prior policy rule, contract, schema, fixture, validator, test, workflow, registry entry, runtime implementation, receipt, release record, or public carrier is changed by this documentation revision.

---

## Change history

| Version | Date | Change |
|---|---|---|
| `v0.3` | 2026-08-13 | Reconciled the README with current inactive machine vocabularies, explicit input and semantics profiles, obligation and evaluation-binding evidence, bounded OPA-tested release-gate posture, accepted Directory Rules authority, current workflow pinning, and remaining activation gaps. |
| `v0.2` | 2026-07-19 | Grounded finite outcomes, normalization, composition, replay, sensitivity, and rollback against the then-current schema and readiness hold. |
| `v0.1` | 2026-06-16 | Established the initial substantive decision-policy boundary and vocabulary guidance. |

<p align="right"><a href="#top">Back to top</a></p>
