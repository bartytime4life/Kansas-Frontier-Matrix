<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/focus-mode-state-finite-outcomes
title: Focus Mode Finite Outcome Documentation Boundary
type: standard; focus-mode; runtime-outcome; compatibility-lane
version: v1.0
status: draft; repository-grounded; four-outcome-runtime-boundary; compatibility-lane; non-runtime; non-release; non-publication
owner: "@bartytime4life via CODEOWNERS; runtime, policy, evidence, review, release, and independent publication authority NEEDS VERIFICATION"
created: 2026-05-24
updated: 2026-08-22
policy_label: public; documentation; focus-mode; runtime-outcome; finite-envelope; cite-or-abstain; fail-closed; trust-membrane; non-publication
owning_root: docs/
responsibility: >-
  Reconcile the repository-present finite-outcome documentation with the current
  RuntimeResponseEnvelope, DecisionEnvelope, AIReceipt, FocusResponse, schema,
  validator, fixture, and proof surfaces; distinguish client-facing runtime
  outcomes from HOLD posture, validator results, lifecycle, review, freshness,
  correction, and release state; preserve useful v0.1 reason-code lineage and
  compatibility anchors; and expose evidence, policy, review, correction,
  rollback, release, and publication limits without creating authority in
  another responsibility root.
authority: >-
  Human-readable explanation, reconciliation, and navigation only. Runtime
  semantic meaning belongs to contracts; machine shape belongs to schemas;
  executable validation belongs to tools and tests; policy, evidence, review,
  release, correction, rollback, API, UI, and model behavior remain in their
  owning roots. This document does not select an outcome or authorize an answer.
current_path: docs/focus-mode/state/finite-outcomes.md
canonical_relationship: >-
  Same-path documentation repair inside the repository-present singular Focus
  compatibility lane. Accepted Directory Rules v2 supports PLACE for this
  docs-root correction but does not settle the mixed state tree's final split,
  rename, move, mirror, or deletion. Structural convergence remains HOLD.
truth_posture: >-
  CONFIRMED current repository path and prior v0.1 blob, current parent state
  README, accepted ADR-0029 and adopted Directory Rules v2, paired
  RuntimeResponseEnvelope contract/schema, four schema-enumerated client
  outcomes ANSWER/ABSTAIN/DENY/ERROR, conditional ANSWER EvidenceRef and
  precision requirements, DecisionEnvelope and AIReceipt four-outcome shapes,
  FocusResponse projection boundary, deterministic runtime validator, four
  positive outcome fixtures, negative unknown-outcome coverage, and
  standard-library finite-envelope proof / LINEAGE the v0.1 seven-item
  vocabulary and proposed per-outcome reason-code lists / CONFLICTED sibling
  review and transition prose that still treats HOLD as a runtime outcome /
  PROPOSED semantic outcome-selection, controlled reason/policy/freshness/
  correction vocabularies, EvidenceRef resolution, policy and release
  prerequisites, client behavior, AIReceipt linkage, and HOLD projection /
  UNKNOWN live governed Focus service behavior, current evidence and policy
  evaluation, accountable review, release, correction propagation, rollback
  execution, deployment, and public parity / NEEDS VERIFICATION every claim
  beyond the inspected repository shape and bounded documentation assertions.
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: ec58517b74a02f5ce7dda3f407769c31d1393bb7
  target_prior_blob: 22df8e44b31cad5899339f665f205757d70ab47c
  parent_state_readme_blob: 34e2c6c90006937ea00d432689a36bf83fa5a898
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  runtime_response_contract_blob: 9dfc286984b5b52b383753fe6215a2b31df8c876
  runtime_response_schema_blob: 8b86e7db8b18b65a56a4e639dfc54e1b2db93155
  runtime_response_validator_blob: 44ce7d51038a9adf9fcbdb18108cc27da8381e33
  runtime_response_fixture_readme_blob: 8e65ba049a0ed51de6d69b4675b3e517255074fd
  runtime_finite_proof_blob: 70ca80226bf06c3b28b59096e3812312a00c03b6
  decision_envelope_contract_blob: b7e33c1351c9c28c5cfb3fc107d87204b3fdf455
  decision_envelope_schema_blob: 349782c8760f77e432ed1e9239d5ddc2ffe1f9b8
  ai_receipt_contract_blob: 1e028525569b6032cd573e71d98df6b961fa70db
  ai_receipt_schema_blob: 2e0bebdb3a38acbc3c58a919db46970c6e829b4a
  ui_focus_response_contract_blob: 5fe3e2763d2b3735e94a53a416114d9b37e7be64
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
inspection_boundary: >-
  Current-session GitHub reads covered the complete prior finite-outcomes
  document, the current parent state README, accepted Directory Rules evidence,
  RuntimeResponseEnvelope and DecisionEnvelope contracts and schemas, AIReceipt
  contract and schema identity, the FocusResponse contract, the runtime
  validator, fixture-family README, standard-library finite-outcome proof,
  CODEOWNERS, open pull-request overlap, and matching branch overlap. No source
  was admitted; no EvidenceRef was resolved; no policy evaluator, governed
  Focus request, UI, model adapter, release record, correction propagation,
  rollback drill, deployment, or public endpoint was exercised.
related:
  - ./README.md
  - ./review-state.md
  - ./payload-state.md
  - ./map-context-state.md
  - ./revocation-state.md
  - ./transitions/answer-to-abstain.md
  - ./transitions/hold-to-deny.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../contracts/runtime/runtime_response_envelope.md
  - ../../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
  - ../../../contracts/runtime/decision_envelope.md
  - ../../../schemas/contracts/v1/runtime/decision_envelope.schema.json
  - ../../../contracts/runtime/ai_receipt.md
  - ../../../schemas/contracts/v1/runtime/ai_receipt.schema.json
  - ../../../contracts/ui/focus_response.md
  - ../../../tools/validators/validate_runtime_response_envelope.py
  - ../../../fixtures/contracts/v1/runtime/runtime_response_envelope/README.md
  - ../../../tests/runtime_proof/test_envelope_finite_outcomes.py
  - ../../../.github/CODEOWNERS
tags: [kfm, focus-mode, state, runtime-outcome, finite-outcomes, runtime-response-envelope, decision-envelope, ai-receipt, evidence-ref, precision, cite-or-abstain, compatibility, non-publication]
notes:
  - "v1.0 reconciles the stale seven-item v0.1 vocabulary with the current four-outcome runtime machine shape."
  - "HOLD remains a review, placement, promotion, correction, or workflow posture; PASS and FAIL remain validator results."
  - "The legacy reason-code tables are preserved as LINEAGE candidates, not represented as current machine enums."
  - "The current path remains writable for this same-path documentation correction; structural convergence remains separate governed work."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Focus Mode Finite Outcome Documentation Boundary

> **Purpose.** Explain the four client-facing runtime outcomes currently carried
> by KFM's repository-present runtime envelope, keep adjacent state families
> separate, and preserve the evidence, policy, review, correction, release, and
> rollback conditions that prose must not silently replace.

> [!IMPORTANT]
> **The current machine-enumerated runtime outcomes are exactly `ANSWER`,
> `ABSTAIN`, `DENY`, and `ERROR`.** The paired runtime schema, DecisionEnvelope
> schema, AIReceipt schema, valid fixtures, validator, and bounded proof use that
> four-value set. Their repository presence proves shape and bounded checks—not
> semantic correctness, live service behavior, evidence closure, policy
> permission, release, deployment, or publication.

> [!CAUTION]
> **`HOLD`, `PASS`, and `FAIL` are not current
> `RuntimeResponseEnvelope.outcome` values.** `HOLD` is a fail-closed review,
> placement, promotion, correction, or workflow posture. `PASS` and `FAIL` are
> validator or check results. They may influence a runtime decision but must not
> be substituted for one of the four client outcomes.

> [!WARNING]
> **A schema-valid `ANSWER` is not automatically true or publishable.** The
> schema requires evidence references and a structured disclosure of the
> precision actually used, but an `EvidenceRef` is only a pointer. Consequential
> support still requires governed resolution to admissible evidence, policy and
> sensitivity checks, release fitness, and visible correction/rollback state.

**Quick navigation:** [Scope](#1-scope) · [Outcomes](#2-current-four-runtime-outcomes) ·
[Carriers](#3-current-carriers-and-required-shape) ·
[Reason codes](#4-reason-code-status-and-v01-lineage) ·
[Surfaces](#5-outcome-authority-by-surface) ·
[State families](#6-runtime-outcomes-versus-adjacent-state-families) ·
[Composition](#7-composition-rules) · [Validation](#8-validation-and-evidence) ·
[Anti-patterns](#9-anti-patterns) · [Open work](#10-open-questions) ·
[Maintenance](#11-maintenance-correction-and-rollback) ·
[References](#12-cross-references)

---

<a id="1-scope"></a>

## 1. Scope

This document owns a human-readable reconciliation of finite **client-facing
runtime outcome** terminology. It explains:

- the exact outcome enum visible in current repository machine shape;
- the bounded semantics currently documented by the runtime contract;
- the conditional `ANSWER` requirements enforced by the schema and validator;
- how `DecisionEnvelope`, `AIReceipt`, and `FocusResponse` relate without
  collapsing into one object family;
- why HOLD posture, validator results, lifecycle, review, freshness, correction,
  and release state remain orthogonal;
- which v0.1 reason-code lists are retained as design lineage;
- what current repository checks prove and what they do not prove.

This document does not own:

| Responsibility | Owning surface or decision class | Effect here |
|---|---|---|
| Runtime response meaning | [`RuntimeResponseEnvelope` contract](../../../contracts/runtime/runtime_response_envelope.md) | This document summarizes; it cannot amend the contract |
| Runtime response machine shape | [Runtime response schema](../../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json) | The four-value enum and conditional shape outrank stale prose |
| Runtime decision detail | [`DecisionEnvelope` contract](../../../contracts/runtime/decision_envelope.md) | Separate decision object; not the client envelope |
| AI accountability | [`AIReceipt` contract](../../../contracts/runtime/ai_receipt.md) | Required when AI participates under its contract; not universal for non-AI paths |
| UI projection | [`FocusResponse` contract](../../../contracts/ui/focus_response.md) | Must preserve runtime outcome; cannot redefine it |
| Evidence truth | `EvidenceRef` and `EvidenceBundle` owners | A ref must resolve before it supports a consequential answer |
| Policy, rights, and sensitivity | `policy/` plus accountable review | Documentation cannot allow, deny, redact, or generalize |
| Review, HOLD, and separation of duties | Review records and accountable reviewer assignments | HOLD posture remains outside the current runtime enum |
| Validation results | `tools/`, `tests/`, and `fixtures/` | PASS/FAIL is bounded check evidence, not a public outcome |
| Release, correction, withdrawal, and rollback | `release/` and governed accountability objects | A Markdown edit or green check creates none of these states |
| Runtime, API, UI, map, and model implementation | Application/runtime roots | No operational behavior is implemented here |

### Placement

Accepted Directory Rules v2 supports `PLACE` for this same-path documentation
correction under `docs/`. It does not make the mixed `state/` tree a final
canonical structure. A move, split, rename, mirror, parallel tree, or deletion
remains `HOLD` or `DENY` until accepted authority, consumer closure, validated
migration, and rollback evidence exist.

[Back to top](#top)

---

<a id="2-the-seven-outcomes"></a>

## 2. Current four runtime outcomes

The v0.1 heading and anchor referred to “seven outcomes.” That anchor is
retained for compatibility, but the current repository evidence supports four
client-facing runtime values.

| Outcome | Current bounded runtime meaning | Machine-enforced shape | What remains unproved |
|---|---|---|---|
| `ANSWER` | The runtime may present a governed response under the current envelope proposal. | At least one top-level `EvidenceRef` and `precision_actually_used` are required. | Evidence resolution, policy correctness, source rights, release eligibility, answer truth, and public deployment |
| `ABSTAIN` | The runtime declines to answer because evidence, citation, rights, sensitivity, freshness, correction, context, or another prerequisite is insufficient or unsafe. | `precision_actually_used` is forbidden; the required `evidence_refs` array may be empty. | Final reason-code vocabulary and live selection behavior |
| `DENY` | Access, render, export, capability, consent, sensitivity, or release posture blocks delivery. | `precision_actually_used` is forbidden. | Active policy evaluation, obligations, role handling, and client behavior |
| `ERROR` | The runtime cannot complete safely or deterministically. | `precision_actually_used` is forbidden. | Production error taxonomy, retry behavior, and operational recovery |

### `ANSWER`

A shape-valid `ANSWER` must include:

1. all ten unconditional `RuntimeResponseEnvelope` fields;
2. at least one top-level `EvidenceRef`;
3. one closed `precision_actually_used` object;
4. nonempty precision-level evidence refs that are also present at the envelope
   top level;
5. a transform receipt when outward spatial generalization is declared;
6. a non-inverted temporal observation interval.

Those requirements make answer support and disclosed precision inspectable. They
do not prove that the references resolve, that policy allows display, that the
evidence is authoritative or current, or that release gates have passed.

### `ABSTAIN`

`ABSTAIN` is a first-class safe non-answer. A client must not reconstruct,
guess, or complete the withheld answer from map context, model confidence,
cached prose, partial evidence, or neighboring layers. The envelope may state a
public-safe reason, freshness posture, and correction posture; it may not carry
answer-shaped precision disclosure.

### `DENY`

`DENY` records that delivery is prohibited by the applicable governed boundary.
The response must not leak the denied fact, exact protected geometry, private
data, source internals, credentials, or tactical detail through the reason
string, state fields, logs, or UI fallback.

### `ERROR`

`ERROR` means the runtime path failed safely or could not complete
deterministically. It is not evidence that the underlying claim is true, false,
allowed, denied, available, or absent. Clients must show a safe diagnostic
posture and must not normalize the failure into an empty or uncited answer.

[Back to top](#top)

---

<a id="3-per-outcome-required-artifacts"></a>

## 3. Current carriers and required shape

The v0.1 table treated every public outcome as if it always required the same
`DecisionEnvelope`, `AIReceipt`, and evidence side-car. Current repository
evidence supports a more precise object-family split.

### RuntimeResponseEnvelope

The client-facing runtime schema unconditionally requires:

```text
id
spec_hash
version
issued_at
outcome
reason_code
evidence_refs
policy_state
freshness
correction_state
```

`precision_actually_used` is conditionally required only for `ANSWER` and
forbidden for the other three outcomes. The root object and the precision
sub-objects are closed against additional properties.

### Companion-object map

| Object or result | Role | Relationship to the four outcomes | Boundary |
|---|---|---|---|
| `RuntimeResponseEnvelope` | Governed API/client trust-membrane response | Carries exactly one of the four runtime outcomes | Not raw evidence, policy execution, or release approval |
| `DecisionEnvelope` | Runtime decision detail with policy family, reasons, and obligations | Its paired schema also uses the same four-value outcome enum | Not the full client response and not a `PolicyDecision` |
| `AIReceipt` | Accountability record for an AI-mediated runtime event | Uses the same four values **when AI participates** | Not required for a path with no AI step; not model truth |
| `FocusResponse` | UI-facing projection of a governed result | Must preserve the upstream four-outcome state | Current UI schema is a permissive stub; projection is not runtime authority |
| `EvidenceRef` | Pointer to governed evidence support | Required nonempty at the envelope top level for `ANSWER` | Pointer presence is not EvidenceBundle closure |
| `EvidenceBundle` | Evidence support for claims and precision | Must be resolved and admissible before a consequential answer is treated as supported | Generated language and receipts do not replace it |
| `PolicyDecision` | Policy evaluation record | May allow, restrict, abstain, or deny according to its own contract/policy family | Runtime envelope summarizes public-safe policy state |
| `ReleaseManifest` and correction records | Release and post-release accountability | Constrain whether an otherwise valid response may be served | Git state and envelope shape do not create release |
| `ValidationReport` or process exit result | Bounded validator/check result | Commonly represented as PASS/FAIL outside the runtime enum | Does not emit a public truth judgment |
| `ReviewRecord` or workflow posture | Review and intentional pause | May be held outside the runtime enum | Public behavior still must project through an accepted four-outcome runtime envelope |

### Per-outcome carrier requirements

| Outcome | Runtime envelope | Evidence and precision | AI receipt |
|---|---|---|---|
| `ANSWER` | Required for the current client-facing runtime shape | Top-level EvidenceRef nonempty; structured precision required; governed resolution remains a semantic/runtime prerequisite | Required only when AI participated under the AIReceipt contract |
| `ABSTAIN` | Required for the current client-facing runtime shape | EvidenceRef array may be empty; answer precision forbidden | Required only when AI participated |
| `DENY` | Required for the current client-facing runtime shape | Restricted payload and answer precision forbidden | Required only when AI participated |
| `ERROR` | Required for the current client-facing runtime shape | Answer precision forbidden; diagnostics must remain safe | Required only when AI participated and a receipt can be emitted safely |

[Back to top](#top)

---

<a id="4-reason-code-vocabularies"></a>

## 4. Reason-code status and v0.1 lineage

The current RuntimeResponseEnvelope and DecisionEnvelope schemas define
`reason_code` as a string. They do **not** enumerate the v0.1 lists below.
Accordingly:

- the old values are retained as `LINEAGE` candidates;
- none is represented here as an accepted or machine-enforced vocabulary;
- producers must not invent a private vocabulary and present it as canonical;
- public reason text must not expose restricted evidence, private data,
  credentials, protected locations, or hidden model internals;
- adopting or versioning a controlled vocabulary requires its owning contract,
  schema, policy, fixture, validator, client, compatibility, and migration work.

<a id="41-abstain-reason-codes-proposed-enum"></a>

### 4.1 Legacy `ABSTAIN` candidates

| v0.1 candidate | Prior intended meaning | Current disposition |
|---|---|---|
| `evidence_insufficient` | No released evidence support covered the query. | `LINEAGE`; useful concept, not a current enum |
| `citation_closure_failed` | One or more references did not resolve or close by digest. | `LINEAGE`; resolution and validation behavior remain separate |
| `payload_stale` | Focus payload was stale with no released alternative. | `LINEAGE`; freshness vocabulary remains unclosed |
| `not_yet_released` | Referenced material had not reached eligible release state. | `LINEAGE`; lifecycle and runtime outcome remain separate |
| `revoked_no_alternative` | Support was revoked with no released replacement. | `LINEAGE`; correction/withdrawal behavior remains unproved |
| `query_out_of_scope` | Requested spatial or temporal scope was outside the bounded Focus request. | `LINEAGE`; scope admission behavior remains unproved |
| `confidence_below_threshold` | Available support did not meet a configured threshold. | `LINEAGE`; no accepted threshold authority was verified |

<a id="42-deny-reason-codes-proposed-enum"></a>

### 4.2 Legacy `DENY` candidates

| v0.1 candidate | Prior intended meaning | Current disposition |
|---|---|---|
| `policy_deny` | Runtime policy prohibited delivery. | `LINEAGE`; active policy behavior not verified |
| `rights_deny` | Rights posture prohibited delivery at the requested surface or role. | `LINEAGE`; rights evaluation remains separate |
| `sensitivity_deny` | Protected sensitivity required withholding or generalization. | `LINEAGE`; current obligations and precision policy remain unclosed |
| `release_state_deny` | Release state did not permit exposure. | `LINEAGE`; release state is not selected by this document |
| `role_deny` | Caller role lacked access. | `LINEAGE`; authentication/role behavior remains unproved |
| `geofence_deny` | A protected spatial rule prohibited the request. | `LINEAGE`; no active geofence implementation was verified |

<a id="43-error-diagnostic-codes-proposed-enum"></a>

### 4.3 Legacy `ERROR` candidates

| v0.1 candidate | Prior intended meaning | Current disposition |
|---|---|---|
| `schema_missing` | A required schema was unavailable. | `LINEAGE`; current production error taxonomy unverified |
| `envelope_malformed` | A request/context envelope failed admission. | `LINEAGE`; exact owning validator and response mapping require verification |
| `contract_violation` | Caller or producer violated the selected contract. | `LINEAGE`; version negotiation behavior unverified |
| `resolver_failure` | A downstream resolver failed. | `LINEAGE`; live resolver behavior unverified |
| `infra_failure` | Infrastructure could not complete the request. | `LINEAGE`; retry and public diagnostic behavior unverified |
| `internal_invariant` | A bounded invariant failed. | `LINEAGE`; safe diagnostic mapping unverified |

<a id="44-hold-reason-codes-proposed-enum"></a>

### 4.4 Legacy HOLD-posture candidates

The anchor remains for older inbound links. These values may describe review,
placement, promotion, correction, or workflow posture; they are **not** current
runtime outcome codes.

| v0.1 candidate | Prior intended meaning | Current disposition |
|---|---|---|
| `steward_review_pending` | Steward review had not resolved. | `LINEAGE`; potential review reason |
| `rights_holder_review_pending` | Rights-holder or sovereignty review had not resolved. | `LINEAGE`; potential review reason |
| `policy_review_pending` | Policy review or revision had not resolved. | `LINEAGE`; potential review reason |
| `correction_pending` | A correction was in flight. | `LINEAGE`; public response mapping requires a four-outcome decision |
| `release_gate_pending` | A recoverable release gate remained open. | `LINEAGE`; promotion/release reason, not a runtime outcome |

[Back to top](#top)

---

<a id="5-outcome--surface-matrix"></a>

## 5. Outcome authority by surface

The v0.1 yes/no matrix assigned outcome behavior to several surfaces without
current implementation proof. The repository-grounded matrix is narrower.

| Surface | Confirmed outcome relationship | Current evidence | What remains unknown |
|---|---|---|---|
| `RuntimeResponseEnvelope` | Exact enum: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | Paired contract and closed schema | Live semantic selection, API behavior, evidence and policy closure |
| `DecisionEnvelope` | Exact enum: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | Paired contract and schema | Runtime production, persistence, and policy linkage |
| `AIReceipt` | Exact enum: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` for AI-mediated events | Paired contract and schema | Adapter integration, persistence, and citation/policy resolution |
| `FocusResponse` | Projection must preserve the upstream four-value outcome | UI semantic contract | Final UI schema, validator, fixtures, accessibility, and client behavior |
| Runtime envelope validator | Accepts/rejects shape and bounded precision semantics | Deterministic validator and fixtures | Evidence resolution, policy correctness, release, and public behavior |
| Finite-envelope proof | Checks the four-value enum, alias, fixtures, and critical precision rules without network | Standard-library test | Hosted exact-head result and live runtime behavior |
| Review, placement, promotion, correction, or workflow process | May enter a `HOLD` posture | Parent state README and governance doctrine | Accepted HOLD carrier and public projection |
| Other resolvers, drawers, maps, exports, or domain lookups | Must remain downstream of accepted contracts and governed interfaces | General KFM trust boundary | Exact per-surface implementation and allowed outcome mapping |

No resolver, map, drawer, layer, source summary, or domain lookup should be
assigned a runtime outcome vocabulary from filename resemblance or older prose.
Inspect its current contract, schema, implementation, policy, fixtures, tests,
and release boundary before making that claim.

[Back to top](#top)

---

<a id="6-public-class-vs-validator-class-outcomes"></a>

## 6. Runtime outcomes versus adjacent state families

The four runtime outcomes are one axis among several independent state families.

| Family | Current examples | Carrier or owner | Runtime relationship |
|---|---|---|---|
| Client runtime outcome | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | RuntimeResponseEnvelope and related runtime contracts | Exactly one value per current envelope |
| Validator/check result | `PASS`, `FAIL`, exit codes, findings | Validators, tests, CI, ValidationReport | May block or narrow work; never a public truth judgment |
| Review posture | draft, pending, held, approved, rejected, superseded *(proposal)* | ReviewRecord/review governance | May influence runtime selection; does not replace it |
| Placement/governance outcome | `PLACE`, `SPLIT`, `MIGRATE`, `MIRROR`, `HOLD`, `DENY` | Directory Rules decision process | Governs repository placement, not a client answer |
| Lifecycle stage | `RAW`, `WORK`, `QUARANTINE`, `PROCESSED`, `CATALOG`, `TRIPLETS`, `PUBLISHED` | Governed data/evidence lifecycle | Constrains eligibility; does not itself select a client outcome |
| Freshness posture | current, stale, historical, pending refresh, or other controlled terms | Source/evidence/runtime contracts and policy | May lead to `ANSWER` or `ABSTAIN`; vocabulary remains partly proposed |
| Correction posture | normal, corrected, superseded, withdrawn, rollback-affected, or other controlled terms | Release/correction governance | May narrow, deny, or replace a response; vocabulary remains partly proposed |
| Policy decision | allow, restrict, abstain, deny, obligations, or family-specific result | PolicyDecision and policy evaluator | Informs the client outcome; does not become the envelope itself |

A single request can therefore involve:

```text
lifecycle:          PROCESSED
review posture:     held
freshness:          stale
correction posture: superseded
validator result:   PASS for shape
runtime outcome:    ABSTAIN
```

None of those values may be silently substituted for another.

### HOLD behavior

Current repository evidence does not establish `HOLD` as a fifth client outcome.
When a review, placement, promotion, correction, or workflow is held, the
governed runtime still needs one of the four accepted client outcomes for a
response. Whether a prior released answer remains visible, is superseded,
withdrawn, abstained, or denied depends on current release, correction, policy,
freshness, and client rules—not on this document.

The sibling [`review-state.md`](./review-state.md) and some transition documents
still carry the older outcome-state HOLD model. They remain visible lineage and
require their own evidence-backed correction; this file does not silently amend
their bytes.

[Back to top](#top)

---

<a id="7-composition-rules"></a>

## 7. Composition rules

| Rule | Current bounded consequence |
|---|---|
| **One runtime outcome field per envelope.** | The current schema accepts one string value from the four-value enum; it cannot carry mixed outcomes in the same object. |
| **EvidenceRef is not evidence closure.** | A shape-valid `ANSWER` still needs governed resolution to admissible support before the claim is treated as supported. |
| **Actual precision controls.** | Requested precision, map zoom, formatting, or model confidence cannot upgrade `precision_actually_used`. |
| **Negative outcomes carry no answer precision.** | `ABSTAIN`, `DENY`, and `ERROR` must not include `precision_actually_used`. |
| **No restricted leakage.** | Reasons, state strings, logs, diagnostics, citations, and UI fallbacks must not expose protected content. |
| **No silent outcome mutation.** | A changed evidence, policy, freshness, or correction posture should issue a new traceable envelope rather than rewriting history invisibly. |
| **HOLD remains outside the runtime enum.** | Held work must be represented by its owning review/workflow/governance carrier and mapped to a current client outcome when a response is required. |
| **PASS/FAIL remains outside the runtime enum.** | A validator reports its bounded result; downstream governed logic decides the client outcome. |
| **AI participation is explicit.** | An AIReceipt is appropriate when AI participated; non-AI responses must not fabricate one. |
| **Git and CI are not publication.** | A branch, PR, merge, tag, release page, or green check cannot create source, policy, release, correction, or publication state. |

Compound or partially supportable requests require an accepted runtime strategy
such as narrowing, decomposition, or safe abstention. This documentation does
not choose that strategy or authorize partial answers.

[Back to top](#top)

---

<a id="8-validation-and-evidence"></a>

## 8. Validation and evidence

### Confirmed repository checks and carriers

| Surface | Confirmed bounded behavior | Does not prove |
|---|---|---|
| Runtime schema | Closed object; four outcomes; ten required fields; conditional ANSWER evidence and precision | Semantic outcome correctness or live service behavior |
| Runtime validator | Loads bounded JSON safely, applies schema validation, and checks precision evidence subset, generalization receipt, and temporal interval order | EvidenceBundle resolution, policy, review, release, or publication |
| Positive fixtures | Cover `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` | Production payloads or answer truth |
| Negative fixtures | Include rejection of an unknown outcome | Complete negative coverage |
| Standard-library proof | Checks enum closure, schema aliasing, fixtures, and precision invariants without network | Hosted exact-head result, API behavior, or public parity |
| Contract alignment tests named by the runtime contract | Guard contract/schema description alignment | Acceptance of proposed semantics or runtime deployment |
| This Markdown change | Can be checked for structure, links, anchors, and accurate repository claims | Any runtime or lifecycle transition |

### Required changed-area documentation checks

This revision should pass:

- one H1 and one complete `KFM_META_BLOCK_V2`;
- unique explicit anchors, including all retained v0.1 compatibility anchors;
- balanced fenced blocks and HTML comments;
- consistent Markdown tables;
- all same-document fragments resolving;
- repository-relative links resolving at the pinned base;
- UTF-8, LF line endings, final newline, no tabs, and no trailing whitespace;
- exact separation of four runtime outcomes from HOLD and PASS/FAIL;
- no claim that contracts, schemas, fixtures, tests, CI, commits, or PRs prove
  release or publication.

### Executable validation posture

The runtime schema, validator, fixtures, and proof tests are current repository
evidence, but this documentation slice does not modify them. Their local or
hosted execution must be reported separately as `PASS`, `FAIL`, `PENDING`,
`NOT_RUN`, or `UNKNOWN`; file presence is not an execution result.

[Back to top](#top)

---

<a id="8-anti-patterns"></a>

## 9. Anti-patterns

| Anti-pattern | Failure | Required posture |
|---|---|---|
| Seven-item runtime enum | Treating HOLD/PASS/FAIL as client outcomes | Preserve the current four-value machine shape until an accepted contract/schema change |
| Free-form success fallback | Returning answer-like prose outside a governed envelope | Fail closed through the accepted runtime boundary |
| Shape-valid equals true | Treating schema validity or fixture success as evidence closure | Resolve EvidenceRef to admissible EvidenceBundle support |
| AIReceipt always required | Fabricating AI accountability for a non-AI path | Emit AIReceipt only when AI participated under its contract |
| AIReceipt equals evidence | Treating model/run digests as factual support | EvidenceBundle outranks generated language and receipts |
| Reason-code invention | Declaring local strings canonical without contract/schema/policy ownership | Treat current strings as unclosed; version through owning surfaces |
| HOLD equals prior answer continues | Assuming held review automatically preserves a public claim | Follow release, correction, withdrawal, cache, and policy state |
| Validator emits client truth | Mapping PASS directly to ANSWER or FAIL directly to DENY | Validator results are bounded inputs to governed decision logic |
| Negative-state leakage | Embedding protected content in reasons, logs, partial payloads, or precision fields | Return public-safe reasons and no restricted answer material |
| Requested precision upgrade | Using map zoom or caller request as evidence-supported precision | Disclose only precision actually supported and transformed |
| Git state equals public state | Treating PR/merge/release-page state as KFM publication | Require governed promotion, release, correction, and rollback |
| Prose overrides machine shape | Letting this or another Markdown file redefine the paired schema | Update owning contract/schema through reviewed compatibility work |

[Back to top](#top)

---

<a id="9-open-questions"></a>

## 10. Open questions

The v0.1 cross-reference anchor is retained here; the references themselves are
collected in [§12](#12-cross-references).

| ID | Open question | Current state | Required closure |
|---|---|---|---|
| FO-Q1 | Which controlled `reason_code` vocabulary is authoritative? | `UNKNOWN`; schemas accept strings | Contract/schema/policy register, fixtures, validator, compatibility, and client review |
| FO-Q2 | Which vocabularies govern `policy_state`, `freshness`, and `correction_state`? | `PROPOSED` examples only | One owner per vocabulary plus schema/policy/client enforcement |
| FO-Q3 | How does held review or correction project to the four runtime outcomes? | `CONFLICTED` across sibling prose | Accepted carrier and explicit release/correction/client behavior |
| FO-Q4 | When must a DecisionEnvelope accompany a RuntimeResponseEnvelope? | `NEEDS VERIFICATION` | Runtime architecture, persistence, API, fixtures, and tests |
| FO-Q5 | How should AIReceipt and citation-validation refs attach to client responses? | `NEEDS VERIFICATION` | Contract/schema versioning and governed AI integration |
| FO-Q6 | Which component resolves EvidenceRefs and independently verifies answer precision? | `UNKNOWN` end to end | Governed resolver, policy, tests, receipts, and failure semantics |
| FO-Q7 | How should compound or partially supported questions be narrowed or decomposed? | `UNKNOWN` | Accepted runtime behavior and deterministic positive/negative tests |
| FO-Q8 | Are the runtime contract and schema to remain `PROPOSED`, or what decision accepts/supersedes them? | `NEEDS VERIFICATION` | Accountable contract/schema governance |
| FO-Q9 | Which sibling state documents must be corrected after this reconciliation? | `NEEDS VERIFICATION`; review/HOLD prose is stale | Bounded consumer and anchor inventory plus reviewable follow-up |
| FO-Q10 | Where should cross-cutting system-state documentation live after the mixed tree is split? | `HOLD` | Accepted placement decision, migration plan, consumers, and rollback |

Adding or removing a runtime outcome, changing conditional ANSWER shape, making
HOLD client-facing, or changing object-family ownership requires more than a
Markdown edit.

[Back to top](#top)

---

<a id="11-maintenance-correction-and-rollback"></a>

## 11. Maintenance, correction, and rollback

Update this document when:

- the RuntimeResponseEnvelope or DecisionEnvelope outcome enum changes through
  an accepted contract/schema process;
- conditional ANSWER evidence or precision rules change;
- controlled reason, policy, freshness, or correction vocabularies become
  machine-enforced;
- HOLD gains an accepted carrier and client projection;
- AIReceipt linkage becomes required or optional through a versioned contract;
- runtime resolver, policy, client, correction, withdrawal, or rollback behavior
  becomes verifiable;
- the mixed state tree receives an accepted split or migration plan;
- sibling documents are corrected and compatibility anchors can be retired.

### Correction discipline

A correction should:

1. pin the affected document, contract, schema, fixture, test, and runtime
   evidence;
2. identify whether the error is prose, semantic meaning, machine shape,
   implementation, policy, or release state;
3. update the owning authority rather than patching a derived surface;
4. preserve or deliberately migrate inbound anchors and consumers;
5. state compatibility, correction, withdrawal, cache, and rollback effects;
6. avoid rewriting historical receipts or shared Git history.

### Rollback

Before merge, close or abandon the draft pull request and feature branch. Branch
deletion is a separate action.

After merge, restore prior target blob
`22df8e44b31cad5899339f665f205757d70ab47c` through a transparent revert or apply a bounded forward
correction. Do not rewrite shared history.

This documentation rollback would change Markdown bytes only. It would not alter
contracts, schemas, validators, fixtures, runtime responses, evidence, policy,
release records, deployment, public caches, correction notices, or publication.

[Back to top](#top)

---

<a id="10-cross-references"></a>
<a id="12-cross-references"></a>

## 12. Cross-references

### Local state and transition lineage

- [State documentation boundary](./README.md)
- [Review-state and HOLD lineage](./review-state.md)
- [Payload-state lineage](./payload-state.md)
- [Map-context-state lineage](./map-context-state.md)
- [Revocation-state lineage](./revocation-state.md)
- [Answer-to-abstain transition lineage](./transitions/answer-to-abstain.md)
- [Hold-to-deny transition lineage](./transitions/hold-to-deny.md)

### Current runtime, UI, fixture, and validation seams

- [`RuntimeResponseEnvelope` contract](../../../contracts/runtime/runtime_response_envelope.md)
- [RuntimeResponseEnvelope schema](../../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json)
- [`DecisionEnvelope` contract](../../../contracts/runtime/decision_envelope.md)
- [DecisionEnvelope schema](../../../schemas/contracts/v1/runtime/decision_envelope.schema.json)
- [`AIReceipt` contract](../../../contracts/runtime/ai_receipt.md)
- [AIReceipt schema](../../../schemas/contracts/v1/runtime/ai_receipt.schema.json)
- [`FocusResponse` UI projection contract](../../../contracts/ui/focus_response.md)
- [Runtime envelope validator](../../../tools/validators/validate_runtime_response_envelope.py)
- [Runtime envelope fixtures](../../../fixtures/contracts/v1/runtime/runtime_response_envelope/README.md)
- [Finite-envelope no-network proof](../../../tests/runtime_proof/test_envelope_finite_outcomes.py)

### Placement and review boundaries

- [Accepted Directory Rules v2 bytes](../../doctrine/directory-rules.md)
- [ADR-0029 — accepted Directory Rules adoption](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [CODEOWNERS review routing](../../../.github/CODEOWNERS)

### Compatibility anchors retained from v0.1

- `#1-scope`
- `#2-the-seven-outcomes`
- `#3-per-outcome-required-artifacts`
- `#4-reason-code-vocabularies`
- `#41-abstain-reason-codes-proposed-enum`
- `#42-deny-reason-codes-proposed-enum`
- `#43-error-diagnostic-codes-proposed-enum`
- `#44-hold-reason-codes-proposed-enum`
- `#5-outcome--surface-matrix`
- `#6-public-class-vs-validator-class-outcomes`
- `#7-composition-rules`
- `#8-anti-patterns`
- `#9-open-questions`
- `#10-cross-references`

---

**Current document status:** repository-grounded draft · **Runtime machine
shape:** four outcomes · **HOLD/PASS/FAIL:** separate state families ·
**Path posture:** same-path `PLACE`, structural convergence `HOLD` ·
**Release/publication effect:** none.

[Back to top](#top)
