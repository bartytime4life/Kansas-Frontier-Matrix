<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://policy/decision
title: policy/decision/ — Finite Outcome and Decision-Normalization Boundary
type: policy-readme; directory-readme; decision-policy-boundary
version: v0.2
status: draft; repository-grounded; readme-only-direct-lane; schema-paired; shape-fixture-covered; executable-decision-policy-not-established
owners: OWNER_TBD — Policy steward · Governance steward · Policy-runtime steward · Contracts steward · Schema steward · Evidence steward · Rights/consent/sensitivity steward · API steward · Release steward · Security steward · Validation steward · Docs steward
created: 2026-06-15
updated: 2026-07-19
policy_label: "public-governance; restricted-review; finite-outcomes; cite-or-abstain; fail-closed; obligation-preserving; reason-coded; replayable; no-runtime-authority; no-release-authority; no-truth-authority"
current_path: policy/decision/README.md
owning_root: policy/
responsibility: define and index the decision-policy boundary for canonical finite outcomes, engine-result normalization, reason codes, obligations, composition, replay, supersession, and public-safe handling without owning semantic contracts, machine schemas, runtime evaluation, receipts, evidence, release approval, or publication
truth_posture: CONFIRMED target path, singular policy root, PolicyDecision semantic contract, concrete PROPOSED PolicyDecision schema, four schema outcomes ANSWER|ABSTAIN|DENY|ERROR, six schema policy families, two valid and three invalid shape fixtures, common schema fixture harness, policy-test readiness workflow, empty machine policy-gate register, proposed ADR-0020, README-only bundle lane, placeholder policy-runtime package, and absent schema-declared dedicated validator/policy paths / PROPOSED engine-result normalization, operational-state separation, controlled reason-code and obligation registries, composition rules, deterministic identity, replay, supersession, correction, and implementation sequence / UNKNOWN accepted evaluator, bundle format and selection, production consumers, branch-protection requirements, current full-suite pass rate, decision receipt persistence, and release enforcement / NEEDS VERIFICATION accepted owners, accepted outcome-normalization ADR, complete PolicyInputBundle shape, direct policy/decision rules, fixtures, tests, validator, reason-code registry, obligation interpreter, operational-state carrier, evidence linkage, review separation, metrics, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  visibility: public
  base_ref: main
  base_commit: 52192ad4f13033a70deec62917743bc6eec470fe
  prior_blob: 0f81c17a705dd29a2d4b6ba725070c1062f44306
  inventory_method: GitHub connector file reads plus bounded direct-lane, duplicate-identity, branch, and open-pull-request searches
  direct_lane_files_confirmed:
    - policy/decision/README.md
  bounded_inventory_note: no direct policy/decision Rego module, dedicated decision-policy fixture or test family, executable validator, accepted reason-code or obligation registry, runtime normalization implementation, receipt emitter, consumer binding, or release integration was established; bounded absence is not proof of permanent absence
related:
  - ../README.md
  - ../bundles/README.md
  - ../data/README.md
  - ../contract/README.md
  - ../../contracts/policy/policy_input_bundle.md
  - ../../contracts/policy/policy_decision.md
  - ../../contracts/runtime/decision_envelope.md
  - ../../schemas/contracts/v1/policy/policy_input_bundle.schema.json
  - ../../schemas/contracts/v1/policy/policy_decision.schema.json
  - ../../fixtures/contracts/v1/policy/policy_decision/README.md
  - ../../tests/schemas/test_common_contracts.py
  - ../../.github/workflows/policy-test.yml
  - ../../docs/adr/ADR-0020-abstain-is-a-first-class-decision.md
  - ../../docs/registers/POLICY_GATE.md
  - ../../control_plane/policy_gate_register.yaml
  - ../../packages/policy-runtime/README.md
  - ../../apps/governed-api/README.md
  - ../../release/README.md
  - ../../data/receipts/README.md
  - ../../docs/architecture/directory-rules.md
tags: [kfm, policy, decision, PolicyDecision, DecisionEnvelope, finite-outcomes, answer, abstain, deny, error, allow, restrict, hold, normalization, reason-codes, obligations, composition, replay, supersession, fail-closed]
notes:
  - "This revision updates the existing v0.1 README; the prior file was substantive, not an empty placeholder."
  - "The current PolicyDecision schema is concrete but PROPOSED and allows only ANSWER, ABSTAIN, DENY, and ERROR in outcome."
  - "ALLOW, RESTRICT, HOLD, PASS, and FAIL are lower-level or operational terms unless an accepted adapter maps them into the canonical four-outcome surface."
  - "The current PolicyDecision schema has additionalProperties false and no operational_state, evidence_refs, supersedes, bundle_ref, input_hash, or decision_hash fields; those concerns require a separate governed carrier, receipt, or deliberate schema revision."
  - "The policy-test workflow validates the bounded shape-fixture/readiness state and explicitly does not evaluate policy or emit PolicyDecision records."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Decision Policy

`policy/decision/`

> Repository-grounded policy boundary for finite outcomes, decision normalization, reason codes, obligations, multi-gate composition, replay, supersession, and public-safe handling. This lane does not execute policy, create evidence, approve release, or make generated language true.

![status](https://img.shields.io/badge/status-draft-yellow)
![version](https://img.shields.io/badge/version-v0.2-informational)
![maturity](https://img.shields.io/badge/maturity-README--only-lightgrey)
![shape](https://img.shields.io/badge/PolicyDecision-schema--paired-0a7ea4)
![outcomes](https://img.shields.io/badge/outcomes-ANSWER%20%7C%20ABSTAIN%20%7C%20DENY%20%7C%20ERROR-blueviolet)
![runtime](https://img.shields.io/badge/runtime-not__established-orange)
![default](https://img.shields.io/badge/default-fail__closed-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

**Quick links:** [Purpose](#purpose) · [Current status](#current-repository-status) · [Authority](#authority-and-repository-fit) · [Outcome axes](#outcome-axes-must-remain-separate) · [Canonical outcomes](#canonical-policydecision-outcomes) · [Normalization](#engine-result-normalization) · [Inputs](#required-evaluation-input) · [Reasons](#reason-code-boundary) · [Obligations](#obligation-boundary) · [Composition](#multi-gate-composition) · [Replay](#identity-replay-freshness-and-supersession) · [Public boundary](#public-interface-and-sensitive-data-boundary) · [Tests](#validation-negative-cases-and-ci) · [Implementation](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Evidence](#evidence-ledger) · [Rollback](#correction-rollback-and-supersession)

> [!IMPORTANT]
> **Observed direct-lane maturity:** README-only in bounded repository evidence.<br>
> **Confirmed machine shape:** `PolicyDecision.outcome` is closed to `ANSWER | ABSTAIN | DENY | ERROR`.<br>
> **Confirmed shape coverage:** two valid and three invalid JSON fixtures are inventoried by a common schema harness.<br>
> **Not established:** decision-policy evaluation, engine-result normalization, accepted bundle selection, dedicated validator execution, reason/obligation registries, receipt emission, runtime consumers, release enforcement, or production replay.

> [!CAUTION]
> A decision record is not evidence, truth, consent, rights clearance, review approval, release approval, or publication. `ANSWER` only permits the evaluated operation within its exact context and obligations; it cannot repair missing EvidenceBundle support, downgrade sensitivity, infer consent, bypass lifecycle state, or authorize public release.

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

| Surface | Status | Evidence-bounded conclusion |
|---|---:|---|
| `policy/decision/README.md` | **CONFIRMED** | Existing v0.1 decision-policy README; this revision supersedes it in place. |
| Other direct `policy/decision/` artifacts | **NOT SURFACED IN BOUNDED SEARCH** | No rule module, test module, fixture family, registry, validator, or consumer binding was established in this lane. |
| `PolicyDecision` semantic contract | **CONFIRMED / PROPOSED** | Contract exists and defines meaning without executing policy or approving release. |
| `PolicyDecision` schema | **CONFIRMED / PROPOSED CONCRETE SHAPE** | Requires six fields, closes additional properties, and permits four outcomes and six policy families. |
| `PolicyInputBundle` schema | **CONFIRMED / PROPOSED PERMISSIVE STUB** | Requires only `id` and permits arbitrary additional properties; rich input readiness is not machine-enforced. |
| Valid fixtures | **CONFIRMED MINIMAL SHAPE COVERAGE** | One `ABSTAIN/access` and one `DENY/sensitivity` fixture are present. |
| Invalid fixtures | **CONFIRMED MINIMAL NEGATIVE SHAPE COVERAGE** | Missing required field, additional property, and enum/pattern/date-time failures are represented. |
| Common schema harness | **CONFIRMED CODE** | Discovers policy schemas with corresponding fixture directories and checks valid/invalid instances. |
| Dedicated `PolicyDecision` validator | **CONFIRMED ABSENT AT DECLARED PATH** | `tools/validators/validate_policy_decision.py` is asserted absent by the current readiness workflow. |
| Schema-declared policy path | **CONFIRMED ABSENT AT DECLARED PATH** | `policy/policy/` is asserted absent by the current readiness workflow and conflicts with the existing singular policy lanes. |
| Policy-test workflow | **CONFIRMED READINESS HOLD** | Checks repository shape and drift; explicitly evaluates no policy and emits no `PolicyDecision`. |
| Policy bundle lane | **CONFIRMED README-ONLY IN BOUNDED EVIDENCE** | No accepted bundle artifact, manifest, selector, or evaluator binding is established. |
| Policy runtime package | **CONFIRMED GREENFIELD PLACEHOLDER** | Package is version `0.0.0`, with an empty initializer and comment-only core implementation. |
| ADR-0020 | **CONFIRMED FILE / PROPOSED ADR** | Proposes the exhaustive four-outcome model and first-class abstention; it is not accepted implementation evidence. |
| Human policy-gate register | **CONFIRMED DRAFT** | Contains mixed gate/status vocabulary and proposed operational guidance. |
| Machine policy-gate register | **CONFIRMED EMPTY** | `entries: []`; no machine reason, gate, or normalization registry is populated. |
| Runtime consumers and release enforcement | **UNKNOWN** | No exhaustive consumer inventory or production execution evidence was established. |

### What this status does not prove

A green schema test or green readiness workflow does not prove:

- that a policy bundle was evaluated;
- that a decision was produced by an accepted evaluator;
- that input facts were complete, current, or authoritative;
- that reason codes or obligations are registry-backed;
- that an `ANSWER` was released or rendered publicly;
- that a decision receipt exists;
- that replay reproduces the same decision;
- that correction, withdrawal, or rollback propagation is automated.

---

## Authority and repository fit

Directory Rules treat repository roots as responsibility boundaries. The existing path remains under the singular `policy/` root because it concerns admissibility and policy decision posture, not contracts, schemas, runtime code, receipts, lifecycle data, or release records.

| Responsibility | Owning surface | Boundary |
|---|---|---|
| Decision-policy posture and future executable decision rules | `policy/decision/` | This lane. Direct executable modules and child naming remain `NEEDS VERIFICATION`. |
| Policy bundle packaging and immutable evaluated rule set | `policy/bundles/` | Bundle content, manifest, digest, selection, and activation after acceptance. |
| Policy-input semantic meaning | `contracts/policy/policy_input_bundle.md` | Meaning only; no hidden fact retrieval. |
| Policy-input machine shape | `schemas/contracts/v1/policy/policy_input_bundle.schema.json` | Current permissive placeholder; not rich input proof. |
| Policy-decision semantic meaning | `contracts/policy/policy_decision.md` | Canonical semantic contract for one policy evaluation result. |
| Policy-decision machine shape | `schemas/contracts/v1/policy/policy_decision.schema.json` | Closed six-field `PolicyDecision` shape. |
| Runtime transport envelope | `contracts/runtime/decision_envelope.md` and paired schema | Runtime carrier; distinct from policy authority and release approval. |
| Policy evaluation mechanics | `packages/policy-runtime/` | Proposed reusable executor/normalizer boundary; currently a placeholder. |
| Human gate index | `docs/registers/POLICY_GATE.md` | Explanation and review index; not executable policy. |
| Machine gate registry | `control_plane/policy_gate_register.yaml` | Proposed machine index; currently empty. |
| Evidence support | Evidence contracts, EvidenceBundles, validators, and proof lanes | Decisions may consume evidence status; cannot create evidence closure. |
| Receipts and replay records | `data/receipts/` or accepted receipt homes | Process memory; not approval or truth. |
| Release, correction, withdrawal, and rollback authority | `release/` | Policy decisions may be required inputs; they do not publish. |
| Public enforcement | `apps/governed-api/` and governed clients | Public callers must not choose bundles or read internal decision stores directly. |

### Authority order for decision behavior

When decision sources disagree, use this order:

1. KFM core invariants: cite-or-abstain, fail closed, trust membrane, lifecycle law, evidence-first, and correction/rollback visibility.
2. Accepted ADRs that explicitly govern decision outcomes or normalization.
3. Accepted executable policy bundle and pinned digest for the evaluated context.
4. Accepted semantic contract and paired schema for the emitted object.
5. Machine gate/reason/obligation registries when accepted and populated.
6. Tests, fixtures, receipts, runtime traces, and release records proving behavior.
7. Human-facing README and register prose.

The current repository has no accepted evidence at every layer of this ladder. Therefore implementation claims remain bounded.

---

## Supersession and preserved lineage

This v0.2 README supersedes v0.1 documentation at the same path. It preserves the strong v0.1 concepts:

- finite decision outcomes;
- first-class abstention;
- reason-code stability;
- obligation preservation;
- multi-gate composition;
- governed public interfaces;
- receipts, replay, correction, and rollback expectations;
- separation from contracts, schemas, runtime, lifecycle data, and release authority.

It corrects or narrows these v0.1 implications:

- v0.1 described `ALLOW`, `ANSWER`, `RESTRICT`, `HOLD`, `ABSTAIN`, `DENY`, and `ERROR` together as decision vocabulary. Current `PolicyDecision` shape permits only four outcomes.
- v0.1 proposed a seven-term severity order. ADR-0020 proposes a four-outcome composition order and treats operational state as a separate axis.
- v0.1 said decision-policy schemas, fixtures, tests, and CI needed verification. Current evidence confirms a concrete schema, minimal shape fixtures, a common harness, and a readiness workflow—but not executable decision behavior.
- v0.1 claimed the predecessor was an empty placeholder. The predecessor was a substantive 342-line README and is preserved as documentation lineage.

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

A trustworthy decision cannot be produced from `PolicyInputBundle.id` alone. The current schema is a permissive placeholder, so richer readiness remains semantic and `NEEDS VERIFICATION` until schema and validator changes are accepted.

A future decision evaluation should bind at least:

| Input family | Minimum content | Failure posture |
|---|---|---|
| Request/gate identity | request or operation id, gate id, policy family, intended action | `ERROR` if malformed or unrecognized. |
| Subject/object scope | governed object ref, requested fields/geometry/action, audience, purpose | `ABSTAIN` if scope cannot be responsibly resolved; `DENY` if prohibited. |
| Caller/access context | authenticated role/capability/consent context where required | `DENY` when authorization is missing or invalid. |
| Evidence context | EvidenceRefs, resolution/closure status, citation readiness, freshness, contradiction state | `ABSTAIN` when support is insufficient; `ERROR` on resolver integrity failure. |
| Source context | source id, role, authority, rights, cadence, limitation flags | `ABSTAIN` or `DENY` according to whether support is unresolved or prohibited. |
| Rights/consent/sensitivity | rights, license, consent, geoprivacy, cultural/ecological/infrastructure restrictions | Fail closed; most restrictive applicable posture wins. |
| Lifecycle/release context | current lifecycle state, release state, correction/withdrawal/supersession state, rollback target | `DENY`, `ABSTAIN`, or `ERROR` according to the accepted gate contract. |
| Policy bundle context | bundle id, version, digest, dependency closure, activation/selection evidence | `ERROR` when missing, stale, untrusted, or not reproducible. |
| Evaluator context | engine, adapter/version, timeout and deterministic configuration | `ERROR` when unavailable or untrusted. |
| Registry context | reason-code registry version, obligation registry/interpreter version, normalization profile | `ERROR` when incompatible or unavailable. |
| Replay/audit context | canonical input digest, correlation id, evaluated time, protected unresolved handles | Required for consequential decisions and correction investigation. |

### Explicit-input rule

Policy evaluation must not secretly fetch or infer facts from model memory, public internet, canonical/internal stores, environment variables, or unreviewed caches. Any permitted retrieval must occur through an admitted, observable, policy-aware dependency whose output becomes part of the governed input and replay record.

---

## Reason-code boundary

The current machine policy-gate register contains no entries. Stable machine reason codes are therefore **not established**.

A future reason-code registry should be:

- versioned and append-oriented;
- namespaced by policy family or gate;
- safe to expose by default or explicitly marked internal-only;
- separated from free-text internal detail;
- linked to canonical outcome compatibility;
- linked to allowed next steps;
- linked to metrics without exposing sensitive facts;
- replayable against the registry version used at evaluation time.

### Proposed reason record shape

```yaml
code: policy.<family>.<condition>
registry_version: <version>
compatible_outcomes: [ANSWER | ABSTAIN | DENY | ERROR]
public_message: <safe bounded explanation>
internal_detail_allowed: <true|false>
next_steps: [<controlled-step>]
sensitivity: <public|restricted|internal>
deprecated_by: <code-or-null>
```

This is illustrative, not an accepted schema or path.

### Reason safety rules

Reasons must not contain:

- exact protected locations;
- living-person or genomic details;
- credentials, secrets, internal tokens, or raw prompts;
- restricted source excerpts;
- private land/title joins or sensitive infrastructure details;
- hidden thresholds, transform seeds, offsets, or reversal instructions;
- chain-of-thought or private model reasoning.

Public explanations should reveal enough to understand the outcome without revealing what the policy protects.

---

## Obligation boundary

The current schema represents obligations as unconstrained strings. No accepted obligation registry or interpreter was established.

A future obligation system must distinguish:

| Concern | Requirement |
|---|---|
| Identity | Stable obligation code and registry version. |
| Parameters | Typed, bounded values where the obligation needs a precision, audience, expiry, citation, or transform profile. |
| Interpreter | Named consumer capability that can deterministically enforce the obligation. |
| Enforcement proof | Receipt or runtime evidence that the obligation was applied before the protected action. |
| Compatibility | Consumer must reject unknown or unsupported obligation versions. |
| Composition | Obligations from all evaluated gates are preserved, deduplicated, and tightened—not weakened. |
| Expiry/correction | Stale or superseded obligations must trigger re-evaluation. |

Candidate obligation families, all **PROPOSED**, include:

- citation/attribution display;
- geometry or attribute redaction;
- spatial or temporal generalization;
- audience restriction;
- no-export/no-download/no-index;
- steward review;
- delayed exposure or expiry;
- rights notice;
- refresh/re-evaluation requirement;
- correction/rollback check.

> [!IMPORTANT]
> Unknown obligations must never be ignored. If an `ANSWER` depends on an obligation the consumer cannot interpret or prove enforced, the safe outcome is `ERROR` for interpreter/contract failure or a newly evaluated `ABSTAIN`/`DENY` according to the underlying policy cause—not silent success.

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

The current repository confirms:

- schema validation through the common fixture harness;
- two valid fixture instances (`ABSTAIN` and `DENY`);
- three invalid shape cases;
- a policy-test workflow that inventories the schema, fixtures, placeholder policy lanes, and missing dedicated validator/evaluator surfaces;
- explicit workflow output stating that no policy rule was evaluated and no `PolicyDecision` was emitted.

This is shape/readiness evidence, not decision-behavior proof.

### Required future fixture matrix

| Case | Expected result |
|---|---|
| Fully supported, policy-passed operation | `ANSWER` with enforceable obligations as applicable. |
| Missing EvidenceBundle resolution | `ABSTAIN`; no generated fallback. |
| Stale evidence beyond accepted policy | `ABSTAIN` or accepted freshness rule; never stale `ANSWER`. |
| Unauthorized caller | `DENY`. |
| Consent revoked | `DENY` or accepted restricted state; downstream invalidation required. |
| Sensitive location exactness prohibited | Safely narrowed `ANSWER` with enforced generalization, or `DENY` if narrowing is not allowed. |
| Review pending | `ABSTAIN` plus separate review/hold state after a carrier is accepted. |
| Bundle digest missing or untrusted | `ERROR`. |
| Unknown native engine result | `ERROR`. |
| Unknown reason code or obligation | `ERROR`; never ignore. |
| Normalizer maps `RESTRICT` to safe narrowed output | `ANSWER` with typed, enforced obligations. |
| Restriction cannot be enforced | `ERROR`, `DENY`, or `ABSTAIN` according to the underlying cause; never unrestricted `ANSWER`. |
| Conflicting child obligations | `ERROR` until conflict is resolved. |
| Child `ERROR` plus child `DENY` | Composite `ERROR`. |
| Public reason attempts to leak sensitive details | Validation failure / safe `ERROR`. |
| Decision is replayed with changed bundle or registry version | New decision identity; old result remains auditable and potentially stale. |
| `ANSWER` lacks release support for a public artifact | Release remains blocked. |
| Correction or withdrawal invalidates support | Prior decision is no longer usable; re-evaluation required. |

### CI maturity

| Check | Current posture |
|---|---|
| PolicyDecision schema/fixture inventory | **CONFIRMED readiness check** |
| Common schema validation | **CONFIRMED code path** |
| Dedicated PolicyDecision semantic validator | **NOT ESTABLISHED** |
| Decision-policy Rego tests | **NOT ESTABLISHED** |
| Accepted OPA/evaluator command | **NOT ESTABLISHED** |
| Native-result normalization tests | **NOT ESTABLISHED** |
| Reason/obligation registry validation | **NOT ESTABLISHED** |
| Runtime consumer contract tests | **NOT ESTABLISHED** |
| Receipt/replay tests | **NOT ESTABLISHED** |
| Release/correction/rollback integration tests | **NOT ESTABLISHED** |
| Branch protection / required-check enforcement | **UNKNOWN** |

### Workflow threat posture for documentation changes

The inspected `policy-test` workflow:

- runs on pull requests and pushes to `main`;
- uses GitHub-hosted runners;
- declares read-only repository contents permission;
- installs no policy engine or repository runtime dependencies;
- performs bounded file and fixture inspection;
- emits no receipt, proof, release, deployment, or publication authority.

Major-version action tags are used rather than immutable SHAs, and repository rulesets/required checks remain `NEEDS VERIFICATION`.

---

## Review burden and separation of duties

Consequential decision-policy changes should involve, as applicable:

- policy steward;
- contracts/schema steward;
- policy-runtime steward;
- evidence/source steward;
- rights/consent/sensitivity steward;
- API/runtime consumer owner;
- release steward;
- security/validation steward;
- affected domain steward.

A generator, rule author, evaluator maintainer, and release approver should not be treated as automatically interchangeable roles. CODEOWNERS routing is not proof that semantic review, independent approval, policy evaluation, or release authorization occurred.

Changes requiring especially strong review include:

- outcome enum or composition changes;
- normalization mappings;
- reason/obligation registry changes;
- bundle selection or evaluator changes;
- public reason wording for sensitive cases;
- schema compatibility changes;
- receipt/replay retention changes;
- release, correction, withdrawal, or rollback coupling.

---

## Smallest sound implementation sequence

The smallest evidence-backed implementation sequence is:

1. **Resolve the outcome model.** Accept or supersede ADR-0020 and explicitly separate canonical outcomes, engine-native results, and operational states.
2. **Reconcile schema and contracts.** Confirm whether `PolicyDecision` remains the six-field record or gains explicit lineage/replay fields through a versioned migration.
3. **Strengthen PolicyInputBundle.** Define explicit governed input fields, close arbitrary additions where practical, and provide valid/invalid fixtures.
4. **Populate machine registries.** Accept gate, reason-code, obligation, next-step, normalization-profile, and compatibility records; keep sensitive detail classifications explicit.
5. **Choose evaluator and bundle contract.** Accept bundle format, manifest, digest, dependency closure, selector, evaluator profile, and fail-closed availability behavior.
6. **Implement normalization.** Add a small deterministic normalizer under the accepted policy-runtime boundary; exact module paths and APIs remain `NEEDS VERIFICATION` until reviewed.
7. **Add direct policy/decision rules.** Use the existing lane only after permanent child naming and responsibility are accepted; avoid parallel policy authority.
8. **Add dedicated validators and fixtures.** Cover all four canonical outcomes, native-result mappings, registry failures, sensitive reasons, obligation conflicts, replay, freshness, and composition.
9. **Emit governed receipts.** Record input/bundle/evaluator/registry/decision digests and protected unresolved handles without treating receipts as proof or approval.
10. **Integrate one governed consumer.** Start with one non-public or fixture-backed path; verify fail-closed behavior before broader adoption.
11. **Integrate release and correction.** Prove that policy decisions are required but insufficient for publication, and that withdrawal/supersession invalidates downstream use.
12. **Graduate CI deliberately.** Replace readiness holds with real evaluator-backed tests while preserving workflow identity or documenting migration.

Each increment should be independently reviewable and reversible.

---

## Definition of done

This lane is not operationally complete until all applicable items are closed:

- [ ] Owners and independent reviewers are assigned.
- [ ] Canonical outcome model is accepted by ADR or equivalent governance decision.
- [ ] Engine-native result normalization is versioned, deterministic, documented, and tested.
- [ ] Operational/review states have a separate accepted carrier.
- [ ] PolicyInputBundle meaning and machine shape are sufficiently explicit for the first consumer.
- [ ] PolicyDecision contract/schema version and migration policy are accepted.
- [ ] Gate, reason-code, obligation, next-step, and normalization registries are populated and versioned.
- [ ] Accepted bundle format, manifest, selector, digest, evaluator, and rollback contract exist.
- [ ] Direct decision-policy rules exist under an accepted child layout.
- [ ] Dedicated validators and negative fixtures cover all four outcomes and mapping failures.
- [ ] Unknown native results, reason codes, obligations, and registry versions fail closed.
- [ ] Multi-gate composition preserves the most protective outcome and all obligations.
- [ ] Decision receipts support replay without leaking sensitive data.
- [ ] Stale, corrected, withdrawn, or superseded decisions cannot remain active silently.
- [ ] At least one governed consumer enforces outcomes and obligations end to end.
- [ ] Public clients receive only governed, release-aware, safe decision envelopes.
- [ ] Release approval remains separate and requires its own records and reviewers.
- [ ] CI runs real evaluator-backed tests rather than readiness inventory alone.
- [ ] Branch protection and required checks are verified.
- [ ] Correction and rollback drills are documented and tested.

---

## Open verification register

| Item | Status | Why it matters |
|---|---:|---|
| Accepted decision-policy owners | `NEEDS VERIFICATION` | Required for durable review and maintenance. |
| ADR-0020 acceptance or supersession | `NEEDS VERIFICATION` | Pins exhaustive outcomes and composition. |
| Permanent child layout under `policy/decision/` | `NEEDS VERIFICATION` | Prevents parallel or ambiguous policy authority. |
| PolicyInputBundle field set | `NEEDS VERIFICATION` | Current schema cannot prove complete evaluation context. |
| PolicyDecision v1 compatibility strategy | `NEEDS VERIFICATION` | Closed shape lacks replay/supersession fields. |
| Engine-native normalization profile | `NEEDS VERIFICATION` | Prevents `ALLOW`/`RESTRICT`/`HOLD` drift. |
| Operational-state carrier | `NEEDS VERIFICATION` | Prevents `HOLD` from leaking into finite outcome. |
| Gate/reason/obligation registries | `NEEDS VERIFICATION` | Machine register is empty; strings are uncontrolled. |
| Accepted evaluator and bundle selection | `UNKNOWN` | No production execution can be inferred. |
| Dedicated validator and direct tests | `NEEDS VERIFICATION` | Current coverage is shape/readiness only. |
| Receipt and replay record family | `NEEDS VERIFICATION` | Required to reproduce consequential decisions. |
| EvidenceRef/EvidenceBundle binding | `NEEDS VERIFICATION` | Current PolicyDecision shape cannot carry evidence refs. |
| Consumer inventory | `UNKNOWN` | Bounded search does not prove exhaustive absence or use. |
| Release/correction/rollback integration | `UNKNOWN` | Policy decisions must not become de facto release authority. |
| Metrics and abstain/deny/error observability | `NEEDS VERIFICATION` | Required to detect fallback and status manipulation. |
| Rulesets, required checks, and branch protection | `UNKNOWN` | Workflow presence alone does not prove enforcement. |
| Canonical Directory Rules document placement | `NEEDS VERIFICATION` | Live file is under `docs/architecture/`; older links name `docs/doctrine/`. |

---

## Evidence ledger

| Evidence | Verified observation | Status |
|---|---|---:|
| `policy/decision/README.md@52192ad4…` | v0.1 substantive README; prior blob `0f81c17a…`. | `CONFIRMED` |
| `contracts/policy/policy_decision.md@52192ad4…` | v0.2 proposed semantic contract; distinguishes policy decision from runtime/release/evidence objects. | `CONFIRMED FILE / PROPOSED CONTRACT` |
| `schemas/contracts/v1/policy/policy_decision.schema.json@52192ad4…` | Six required fields; four outcomes; six families; additional properties closed. | `CONFIRMED SHAPE / PROPOSED STATUS` |
| `schemas/contracts/v1/policy/policy_input_bundle.schema.json@52192ad4…` | Requires only `id`; additional properties allowed. | `CONFIRMED PERMISSIVE STUB` |
| `fixtures/contracts/v1/policy/policy_decision/` | Two valid and three invalid instances inventoried by workflow. | `CONFIRMED MINIMAL SHAPE COVERAGE` |
| `tests/schemas/test_common_contracts.py@52192ad4…` | Common harness validates matching schema/fixture families. | `CONFIRMED CODE` |
| `.github/workflows/policy-test.yml@52192ad4…` | Readiness hold checks exact schema/fixtures and confirms no rule evaluation or emitted decision. | `CONFIRMED WORKFLOW` |
| `docs/adr/ADR-0020-abstain-is-a-first-class-decision.md@52192ad4…` | Proposed four-outcome model and first-class abstention. | `CONFIRMED FILE / PROPOSED ADR` |
| `docs/registers/POLICY_GATE.md@52192ad4…` | Draft human register with mixed outcome/operational vocabulary. | `CONFIRMED DRAFT` |
| `control_plane/policy_gate_register.yaml@52192ad4…` | Metadata only; `entries: []`. | `CONFIRMED EMPTY REGISTER` |
| `policy/bundles/README.md@52192ad4…` | README-only bounded lane; documents native/canonical vocabulary conflict. | `CONFIRMED DOCUMENTATION` |
| `packages/policy-runtime/README.md@52192ad4…` | Greenfield package boundary, version `0.0.0`, functional evaluation not established. | `CONFIRMED PLACEHOLDER` |
| Open PR and branch searches | No overlapping `policy/decision/README.md` work surfaced before mutation. | `CONFIRMED BOUNDED SEARCH` |

### Evidence conflicts and drift

- `policy/bundles/README.md` and `packages/policy-runtime/README.md` still describe an older TODO-only policy-test workflow, while the current workflow is a command-bearing readiness hold. Those docs need separate governed updates; this README does not silently rewrite their history.
- The human policy-gate register includes `HOLD`, `PASS`, and `FAIL` alongside finite outcomes, while the current `PolicyDecision` and `DecisionEnvelope` primary outcome schemas use four values.
- The `PolicyDecision` schema points to `policy/policy/`, but the current readiness workflow asserts that path is absent and the repository already has singular purpose-specific policy lanes.
- ADR-0020 uses the four-outcome model but remains proposed.
- Older documentation links refer to `docs/doctrine/directory-rules.md`, while the live Directory Rules artifact is under `docs/architecture/` and records that placement conflict.

These conflicts are surfaced, not resolved by prose.

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

Review this README when any of the following changes:

- `PolicyDecision`, `PolicyInputBundle`, or `DecisionEnvelope` contract/schema;
- ADR-0020 status or outcome vocabulary;
- engine-native normalization mapping;
- operational-state carrier;
- policy bundle format, evaluator, selector, or activation contract;
- gate, reason-code, obligation, or next-step registry;
- policy-test workflow or direct policy tests;
- first runtime/API/UI/release consumer;
- decision receipt or replay format;
- public reason-safety rules;
- release, correction, withdrawal, supersession, or rollback behavior;
- Directory Rules or policy-root placement.

---

## No-loss preservation note

The prior v0.1 README was not empty. It established a useful decision-policy vocabulary, reason/obligation expectations, composition posture, public-interface boundary, validation checklist, and rollback posture.

This v0.2 preserves those concepts while distinguishing:

- confirmed shape and fixture evidence;
- proposed semantic and implementation design;
- absent or unknown runtime enforcement;
- canonical four-outcome fields from lower-level engine and operational states;
- policy decision from evidence, receipt, review, promotion, release, and publication authority.

<p align="right"><a href="#top">Back to top</a></p>
