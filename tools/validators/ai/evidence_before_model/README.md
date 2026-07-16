<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-ai-evidence-before-model-readme
title: tools/validators/ai/evidence_before_model/ — Governed-AI Gate-Ordering Validation Boundary
type: readme; directory-readme; validator-child-lane; governed-ai; evidence-before-model; non-authoritative
version: v0.2
status: draft; repository-grounded; README-only-child; parent-placeholder-confirmed; executable-enforcement-unimplemented; tests-unestablished; ci-unverified; policy-home-drift; migration-required-before-activation
owners: OWNER_TBD — Governed AI steward · Evidence steward · Policy steward · Runtime steward · Citation steward · Validator steward · Security steward · Privacy/sensitivity steward · Release steward · Docs steward
created: 2026-07-07
updated: 2026-07-16
supersedes: v0.1 proposed evidence-before-model validator guide
policy_label: "repository-facing; tools; validator; governed-ai; evidence-first; policy-aware; cite-or-abstain; fail-closed; released-context-only; prompt-injection-aware; no-chain-of-thought; finite-outcomes; receipt-aware; correction-aware; rollback-aware; no-network-by-default; no-truth-authority; no-policy-authority; no-release-authority"
owning_root: tools/
current_path: tools/validators/ai/evidence_before_model/README.md
responsibility: >
  Repository-grounded contract and compatibility boundary for a future deterministic validator that proves
  governed-AI stage ordering and gate closure around model use: request scope, policy precheck, EvidenceRef
  resolution, admissible EvidenceBundle context, adapter invocation, citation validation, policy postcheck,
  finite RuntimeResponseEnvelope outcome, AIReceipt/RunReceipt linkage, correction state, and safe logging,
  while deferring evidence meaning, schemas, policy decisions, runtime/model adapters, receipts, proof storage,
  release authority, public serving, and generated answers to their owning roots.
truth_posture: >
  CONFIRMED target README v0.1 and prior blob; direct child lane contains only this README in bounded search;
  parent-level tools/validators/ai/validate_evidence_before_model.py exists as an eight-line PROPOSED docstring
  placeholder with no executable validation logic; parent AI validator README v0.1; evidence validator README;
  governed-AI Focus Flow doctrine and stage sequence; AIReceipt contract plus strict PROPOSED schema;
  RuntimeResponseEnvelope contract plus strict PROPOSED schema and working top-level schema-validator wrapper;
  CitationValidationReport contract plus permissive scaffold schema; absent policy/ai/README.md; repository-present
  policy/ai_builder/ lane is not proven equivalent; absent tests/validators/ai child test lane in bounded search;
  AIReceipt fixture lanes surface as README-only in bounded search / PROPOSED canonical lane placement,
  immutable validation profile, stage ledger, deterministic report, finite findings, reason codes, no-network
  tests, CI admission, migration, correction, deprecation, and rollback / CONFLICTED child README says the
  validator entrypoint belongs here while the only named placeholder sits one level above; docs and contracts
  reference policy/ai/ although that README was not found; current governed-AI architecture is detailed but
  implementation remains largely proposed / UNKNOWN active evidence-before-model runtime enforcement, accepted
  policy entrypoints, exhaustive consumers, report schema, receipt emission, production use, release-gate use,
  operational metrics, incident linkage, and current pass results / NEEDS VERIFICATION owners, accepted topology,
  EvidenceRef/EvidenceBundle resolver contract, policy pre/post decision contract, citation validator contract,
  event ordering identity, stage timestamps, digest/canonicalization rules, sensitivity propagation, prompt
  injection controls, resource budgets, CODEOWNERS, tests, CI, deprecation, correction cascade, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 1852516d033a6180507c7ad0b4390689a401c988
  prior_blob: bd64123fa9d1f62baad49f51c05e6e5ef201dda6
  parent_ai_readme_blob: 829589614cff7aec864e3d5802fcc693dc30d3a5
  parent_placeholder_blob: 06b714d90874d69e6ba64cd674ff0c7dfe40e774
  evidence_validator_readme_blob: c163fd6f77f1f8c0ce8a2e042e8594c7e73658a7
  focus_flow_blob: 2dc6213d667e7d2f130427355c5af6b7d59813e2
  ai_receipt_contract_blob: f4d8183dbed38f83144f6d9dbde30ae02a01edb8
  ai_receipt_schema_blob: 2e0bebdb3a38acbc3c58a919db46970c6e829b4a
  runtime_response_contract_blob: b81d67dccdd8470e066ab8247eb93c5df67a6679
  runtime_response_validator_blob: 11ddc64c4299d103b0eef383c2f7bdd3bb12f1f9
  citation_report_contract_blob: 36cdb2bab1e47479b816950d907868c4e4689283
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  pr_template_blob: 13c5d4ed045e201188ebb54b518a586b42b481d4
  generated_receipt_schema_blob: fba21ed27ebccf1362fe397fe0c3ebd85e072685
  bounded_path_checks:
    - tools/validators/ai/evidence_before_model/ surfaced only this README
    - tools/validators/ai/validate_evidence_before_model.py exists outside the child lane as a docstring-only placeholder
    - tests/validators/ai/ did not surface as an implemented test lane
    - policy/ai/README.md was not found
    - policy/ai_builder/ exists but is not proven to be the runtime governed-AI policy home
    - AIReceipt valid/invalid fixture search surfaced README files, not confirmed JSON payloads
    - validate_ai_receipt.py was named by schema/docs but did not surface as a repository file
    - validate_runtime_response_envelope.py is a working shared-schema wrapper, but it validates envelope shape rather than end-to-end stage ordering
related:
  - ../README.md
  - ../../README.md
  - ../../_common/README.md
  - ../../evidence/README.md
  - ../validate_evidence_before_model.py
  - ../../validate_runtime_response_envelope.py
  - ../../../../docs/architecture/governed-ai.md
  - ../../../../docs/architecture/governed-ai/FOCUS_FLOW.md
  - ../../../../docs/architecture/governed-ai/AI_RECEIPTS.md
  - ../../../../docs/architecture/governed-ai/ADAPTER_CONTRACT.md
  - ../../../../docs/architecture/governed-ai/BOUNDARIES.md
  - ../../../../docs/architecture/governed-ai/PROMPT_INJECTION.md
  - ../../../../docs/doctrine/ai-as-assistant.md
  - ../../../../docs/doctrine/evidence-first.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../contracts/runtime/ai_receipt.md
  - ../../../../contracts/runtime/runtime_response_envelope.md
  - ../../../../contracts/runtime/run_receipt.md
  - ../../../../contracts/evidence/evidence_ref.md
  - ../../../../contracts/evidence/evidence_bundle.md
  - ../../../../contracts/evidence/citation_validation_report.md
  - ../../../../schemas/contracts/v1/runtime/ai_receipt.schema.json
  - ../../../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
  - ../../../../schemas/contracts/v1/evidence/evidence_ref.schema.json
  - ../../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json
  - ../../../../schemas/contracts/v1/evidence/citation_validation_report.schema.json
  - ../../../../fixtures/contracts/v1/runtime/ai_receipt/
  - ../../../../fixtures/contracts/v1/runtime/runtime_response_envelope/
  - ../../../../data/proofs/evidence_bundle/
  - ../../../../data/proofs/citation_validation/
  - ../../../../data/receipts/ai/
  - ../../../../data/receipts/validation/
  - ../../../../runtime/model_adapters/
  - ../../../../apps/governed-api/
  - ../../../../release/
tags: [kfm, tools, validators, ai, governed-ai, evidence-before-model, evidence-ref, evidence-bundle, policy-precheck, citation-validation, policy-postcheck, ai-receipt, runtime-response-envelope, finite-outcomes, prompt-injection, no-chain-of-thought, fail-closed, cite-or-abstain, migration, rollback]
notes:
  - "This revision changes only tools/validators/ai/evidence_before_model/README.md plus the required generated provenance receipt."
  - "No validator code, contract, schema, policy, fixture, test, workflow, runtime adapter, receipt instance, proof, release record, API route, model call, or public output is created or modified."
  - "The existing parent-level placeholder is documented, not moved or promoted."
  - "A later code move or activation must select one implementation home and include migration/deprecation evidence."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed-AI Evidence-Before-Model Validation Boundary

`tools/validators/ai/evidence_before_model/`

> **One-line purpose.** This lane defines how KFM should prove that evidence, policy, rights, sensitivity, release, freshness, and correction gates were satisfied before a model could influence an answer—and that citation validation, policy postcheck, finite outcome, and receipts closed the flow afterward—without treating validator output or generated language as truth.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Version: v0.2" src="https://img.shields.io/badge/version-v0.2-informational">
  <img alt="Root: tools" src="https://img.shields.io/badge/root-tools%2F-blue">
  <img alt="Lane: README only" src="https://img.shields.io/badge/lane-README__only-lightgrey">
  <img alt="Implementation: placeholder only" src="https://img.shields.io/badge/implementation-placeholder__only-orange">
  <img alt="Policy: unresolved home" src="https://img.shields.io/badge/policy-home__unresolved-critical">
  <img alt="Posture: cite or abstain" src="https://img.shields.io/badge/posture-cite__or__abstain-success">
</p>

> [!IMPORTANT]
> **Current implementation is not established.** The child directory is README-only in bounded search. The only repository file named for this invariant is `tools/validators/ai/validate_evidence_before_model.py`, one level above this directory, and it contains only a `PROPOSED` docstring placeholder.

> [!CAUTION]
> **A valid response envelope is not proof that evidence came before the model.** `validate_runtime_response_envelope.py` can validate the machine shape of a runtime envelope, but it does not prove stage ordering, EvidenceRef resolution, admissible context construction, policy execution, citation validation, or receipt linkage.

> [!WARNING]
> **Do not persist hidden reasoning.** Validation may require request metadata, stage records, refs, hashes, finite decisions, and safe findings. It must not require or store private chain-of-thought, hidden model state, credentials, raw restricted content, or sensitive exact-location data.

**Quick links:** [Purpose](#purpose) · [Status](#status-and-evidence) · [Placement](#directory-rules-and-authority) · [Inventory](#confirmed-repository-inventory) · [Conflict](#placement-and-implementation-conflict) · [Invariant](#governed-ai-ordering-invariant) · [Stages](#stage-contract) · [Inputs](#validation-input-packet) · [Outputs](#validation-report-contract) · [Outcomes](#finite-outcomes-and-reason-codes) · [Contracts](#contract-and-schema-maturity) · [Security](#security-privacy-and-prompt-injection) · [Lifecycle](#lifecycle-release-and-correction-boundary) · [Tests](#test-and-fixture-contract) · [CI](#ci-admission-contract) · [Migration](#migration-and-compatibility) · [Implementation](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Rollback](#correction-rollback-and-deprecation) · [Evidence](#evidence-ledger)

---

<a id="purpose"></a>

## Purpose

KFM treats AI as an **interpretive subsystem**, never as a sovereign truth source.

The evidence-before-model invariant exists to make that rule testable. A validator for this lane should determine whether a governed-AI event proves the following sequence:

```text
scope request
  -> validate request shape
  -> policy precheck
  -> resolve EvidenceRefs
  -> confirm admissible EvidenceBundles
  -> construct bounded released/authorized context
  -> call provider-neutral model adapter
  -> validate structured candidate output
  -> validate citations
  -> policy postcheck
  -> emit finite runtime outcome
  -> bind AIReceipt / RunReceipt
  -> expose only governed client-safe output
```

The validator should answer:

> Did the flow establish enough inspectable, ordered, policy-safe evidence to justify model use and the final finite outcome—or must the event fail, abstain, deny, hold, or route to review?

It must not:

- call a model;
- retrieve live source data by default;
- create or repair EvidenceBundles;
- make policy decisions;
- approve release;
- emit public answers;
- transform generated text into evidence;
- store private chain-of-thought;
- infer success from file names, path presence, or fluent output.

[Back to top](#top)

---

<a id="status-and-evidence"></a>

## Status and evidence

### Evidence verdict

| Surface | Status | Safe conclusion |
|---|---:|---|
| Target README | **CONFIRMED v0.1 before revision** | Documentation existed for the proposed invariant. |
| Direct child inventory | **CONFIRMED README-only in bounded search** | No executable, fixture, test, or configuration file surfaced under this directory. |
| Parent-level named validator | **CONFIRMED placeholder** | `tools/validators/ai/validate_evidence_before_model.py` contains only an eight-line docstring and no executable logic. |
| Parent AI validator README | **CONFIRMED draft** | Documents this child lane and governed-AI expectations but does not prove implementation. |
| Governed-AI Focus Flow | **CONFIRMED doctrine / implementation PROPOSED** | Documents the fixed policy → evidence → adapter → citation → policy → envelope sequence. |
| `AIReceipt` contract/schema | **CONFIRMED paired, strict, PROPOSED** | Required fields and finite outcomes are machine-shaped; runtime emission and validation remain unverified. |
| `RuntimeResponseEnvelope` contract/schema | **CONFIRMED paired, strict, PROPOSED** | A shared schema validator wrapper exists, but it proves envelope shape only. |
| `CitationValidationReport` | **CONFIRMED semantic contract / permissive schema scaffold** | Citation report meaning is documented; field-level machine enforcement is not established. |
| `policy/ai/` | **NOT FOUND at checked README path** | Referenced policy home is not verified. |
| `policy/ai_builder/` | **CONFIRMED separate lane / equivalence UNKNOWN** | AI-build governance is not proven to be runtime governed-AI policy. |
| Child test lane | **NOT FOUND in bounded search** | `tests/validators/ai/evidence_before_model/` is not implementation evidence. |
| CI enforcement | **UNKNOWN** | No evidence-before-model workflow or blocking job was verified. |
| Production/runtime use | **UNKNOWN** | No active consumer, emitted report, deployment, metrics, or current pass result is claimed. |

### Truth labels

- **CONFIRMED:** repository files and exact behavior explicitly inspected in this session.
- **PROPOSED:** design and future behavior consistent with KFM doctrine but not implemented.
- **NEEDS VERIFICATION:** checkable details that require code, fixtures, tests, policy, CI, or runtime evidence.
- **UNKNOWN:** claims not resolved by bounded repository evidence.

### Current safe status

```text
README contract present
+ parent-level placeholder present
+ supporting contract/schema scaffolds present
- active gate-ordering validator
- direct test suite
- accepted policy entrypoints
- structured validation report schema
- CI enforcement
- runtime adoption proof
```

[Back to top](#top)

---

<a id="directory-rules-and-authority"></a>

## Directory Rules and authority

The existing path is compatible with the `tools/` responsibility root because this concern is a reusable checker/validator responsibility.

| Concern | Owning root | This lane's role |
|---|---|---|
| Evidence-before-model validation implementation | `tools/validators/ai/evidence_before_model/` **or accepted migrated path** | PROPOSED durable implementation home; not yet active. |
| Parent AI validator index | `tools/validators/ai/` | Routes AI-specific validators and shared parent behavior. |
| Shared schema-validation plumbing | `tools/validators/_common/` | Generic resolver/runner utilities only. |
| Evidence semantics | `contracts/evidence/` | Defines EvidenceRef, EvidenceBundle, and citation-report meaning. |
| Runtime/AI receipt semantics | `contracts/runtime/`, `contracts/ai/` | Defines AIReceipt, RunReceipt, and response-envelope meaning. |
| Machine shape | `schemas/contracts/v1/` | Defines JSON Schema shape; validation code must not duplicate it. |
| Policy decisions | `policy/` and accepted runtime policy lanes | Owns allow/deny/restrict/hold/abstain logic. |
| Evidence/proof material | `data/proofs/` | Stores governed proof support, not validator code. |
| Receipt instances | `data/receipts/` | Stores AI, run, validation, and generated receipts. |
| Model adapters | `runtime/model_adapters/` or accepted runtime home | Performs provider-neutral model invocation. |
| Public API | `apps/governed-api/` | Enforces trust-membrane serving; not bypassed by validators or browsers. |
| Tests | `tests/` | Owns authored enforceability proof. |
| Fixtures | `fixtures/` or accepted test-fixture roots | Owns deterministic synthetic examples. |
| Release/correction/rollback | `release/` | Owns publication state and reversal authority. |

### Authority limits

This lane may check:

- ordered stage evidence;
- contract/schema conformance;
- reference presence and resolvability;
- finite outcomes;
- safe reason codes;
- hashes, timestamps, and stage identities;
- policy/citation/receipt linkage;
- lifecycle and public-surface boundaries.

This lane must not become:

- evidence authority;
- policy authority;
- source authority;
- schema authority;
- release authority;
- model runtime;
- answer generator;
- proof store;
- receipt store;
- public client;
- private reasoning archive.

[Back to top](#top)

---

<a id="confirmed-repository-inventory"></a>

## Confirmed repository inventory

### Direct child lane

Bounded search surfaced:

```text
tools/validators/ai/evidence_before_model/
└── README.md
```

No direct implementation file, package module, fixture, test, profile, registry, or CI file surfaced under the child directory.

### Named placeholder outside the child lane

Repository evidence confirms:

```text
tools/validators/ai/validate_evidence_before_model.py
```

Its entire content is a docstring declaring itself a `PROPOSED placeholder`. It has:

- no imports;
- no callable validation function;
- no CLI;
- no schema binding;
- no policy binding;
- no EvidenceRef resolver;
- no fixture support;
- no result object;
- no exit-code contract;
- no tests.

### Supporting artifacts

| Artifact | Confirmed maturity |
|---|---|
| `docs/architecture/governed-ai/FOCUS_FLOW.md` | Detailed doctrinal flow; implementation marked PROPOSED. |
| `contracts/runtime/ai_receipt.md` | Expanded semantic contract; strict paired schema exists. |
| `schemas/contracts/v1/runtime/ai_receipt.schema.json` | Strict PROPOSED shape with required fields and closed properties. |
| `contracts/runtime/runtime_response_envelope.md` | Expanded client-facing finite-envelope contract. |
| `tools/validators/validate_runtime_response_envelope.py` | Working wrapper around the shared JSON Schema runner. |
| `contracts/evidence/citation_validation_report.md` | Detailed semantic contract. |
| `schemas/contracts/v1/evidence/citation_validation_report.schema.json` | Permissive scaffold; no declared fields. |
| `tools/validators/evidence/README.md` | Evidence validation routing/index documentation. |
| `fixtures/contracts/v1/runtime/ai_receipt/` | README-backed fixture lanes surfaced; payload inventory not confirmed. |

[Back to top](#top)

---

<a id="placement-and-implementation-conflict"></a>

## Placement and implementation conflict

The repository currently expresses two placements for the same validator concern:

| Path | Current state | Conflict |
|---|---|---|
| `tools/validators/ai/evidence_before_model/` | README-only child lane | README says this is the validator entrypoint home. |
| `tools/validators/ai/validate_evidence_before_model.py` | Parent-level placeholder | Filename implies implementation ownership at the parent level. |

This is a compatibility and future-maintenance risk even though no logic exists yet.

### Required one-implementation rule

Before executable behavior lands, maintainers should choose one pattern:

**Pattern A — child-owned implementation**

```text
tools/validators/ai/evidence_before_model/
├── README.md
├── validate_evidence_before_model.py
└── profile.schema.json or profile pointer
```

**Pattern B — parent compatibility wrapper**

```text
tools/validators/ai/
├── validate_evidence_before_model.py   # thin compatibility wrapper only
└── evidence_before_model/
    ├── README.md
    └── implementation module(s)
```

**Pattern C — parent-owned implementation**

Retain the parent script as canonical and explicitly convert the child directory into documentation/index only. This requires the README, tests, profile registry, imports, and deprecation notes to agree.

### Forbidden state

Do not create two independent validators that:

- define different required stages;
- use different reason codes;
- resolve evidence differently;
- apply different policy paths;
- accept different finite outcomes;
- emit incompatible reports;
- pass/fail the same fixture differently.

A move or activation should include a migration note or ADR when compatibility, imports, CLI paths, or ownership are materially affected.

[Back to top](#top)

---

<a id="governed-ai-ordering-invariant"></a>

## Governed-AI ordering invariant

A mature validator should prove an **ordered event**, not merely the presence of fields in a final object.

### Required ordering

```text
REQUEST_SCOPED
  < REQUEST_SCHEMA_VALIDATED
  < POLICY_PRECHECK_COMPLETED
  < EVIDENCE_REFS_RESOLVED
  < EVIDENCE_BUNDLES_ADMITTED
  < CONTEXT_ASSEMBLED
  < MODEL_ADAPTER_INVOKED
  < CANDIDATE_OUTPUT_VALIDATED
  < CITATIONS_VALIDATED
  < POLICY_POSTCHECK_COMPLETED
  < FINITE_OUTCOME_EMITTED
  < RECEIPTS_BOUND
```

`<` means “must occur before,” not simply “has an earlier timestamp string.”

### Ordering proof should bind

- one stable request/run identity;
- one immutable validation profile;
- stage sequence numbers or causal parent refs;
- trusted timestamps where available;
- input/output digests;
- EvidenceRef and EvidenceBundle refs;
- policy decision refs;
- adapter/model ref;
- citation validation ref;
- final envelope ref;
- AIReceipt and RunReceipt refs;
- correction/supersession state;
- requested surface and audience.

### What does not prove order

- all fields appearing in one JSON object;
- file modification time;
- log line order without run identity;
- model-generated narration of what supposedly happened;
- a final `ANSWER` outcome;
- a valid AIReceipt by itself;
- a valid RuntimeResponseEnvelope by itself;
- a passing citation report by itself;
- a path named `released`;
- a UI showing citation badges.

[Back to top](#top)

---

<a id="stage-contract"></a>

## Stage contract

### Stage 1 — request scope

Required checks:

- request identifier is stable;
- requested operation is explicit;
- requested audience and public/private surface are explicit;
- geography, time, version, and object scope are bounded;
- user/principal role is represented only at the minimum necessary granularity;
- request does not carry raw restricted payloads when governed refs are sufficient;
- prompt text is treated as untrusted content, not instructions to the validator.

Failure posture:

- malformed scope → `ERROR`;
- unsupported or ambiguous scope → `ABSTAIN`;
- prohibited scope → `DENY`.

### Stage 2 — request schema validation

Required checks:

- request shape matches the accepted schema/profile;
- unknown fields fail closed when the schema is closed;
- enum values are recognized;
- length, count, and nesting limits are enforced;
- invalid encoding or duplicate-key behavior is defined.

Schema validity is only shape validity. It cannot grant evidence, rights, policy, or release permission.

### Stage 3 — policy precheck

Required checks:

- accepted policy entrypoint and version are explicit;
- policy input digest binds the evaluated request/context;
- result is finite;
- reason code and obligations are present when required;
- decision is resolvable and reviewable;
- policy failure does not silently become allow.

Current gap: `policy/ai/README.md` was not found, so the runtime policy home and entrypoints remain **NEEDS VERIFICATION**.

### Stage 4 — EvidenceRef resolution

Required checks:

- each required EvidenceRef is present;
- each ref resolves through a governed resolver;
- resolution is scoped to the requesting principal/surface;
- stale, withdrawn, superseded, embargoed, denied, or inaccessible refs do not pass;
- unresolved refs yield finite negative outcomes.

An EvidenceRef is a pointer, not closure.

### Stage 5 — EvidenceBundle admission

Required checks:

- claim scope matches the requested question/operation;
- required source records and citations exist;
- source roles remain visible;
- rights and sensitivity posture are explicit;
- transforms, digests, checksums, time, and geography are appropriate;
- review/release/correction/rollback support is present where required;
- most-restrictive policy wins across joined evidence.

An EvidenceBundle is evidence closure for a declared scope. It is not policy approval or release approval.

### Stage 6 — bounded context assembly

Required checks:

- context is assembled only from admitted evidence and approved metadata;
- RAW, WORK, QUARANTINE, unreleased candidates, canonical internal stores, credentials, and restricted exact locations are excluded unless an explicit governed operation authorizes them;
- context size and token budgets are bounded;
- context lineage is digest-bound;
- source boundaries and quotations remain traceable;
- untrusted source instructions are neutralized as data.

### Stage 7 — model adapter invocation

Required checks:

- adapter is provider-neutral and approved;
- model reference/version is explicit;
- input digest matches the admitted context;
- timeout, retry, and cancellation posture are explicit;
- direct browser-to-model and validator-to-model shortcuts are denied;
- adapter cannot silently retrieve additional ungoverned context;
- model output is treated as a candidate, not an answer.

### Stage 8 — candidate output validation

Required checks:

- candidate output matches the requested structured envelope;
- unknown outcome or unsupported fields fail closed;
- cited spans or claim references are bounded;
- output does not claim policy, evidence, or release authority;
- output does not expose hidden prompt, credentials, chain-of-thought, or protected context;
- output digest is reproducible under the accepted canonicalization rule.

### Stage 9 — citation validation

Required checks:

- every substantive claim requiring support has a citation;
- citations resolve to admitted EvidenceBundle material;
- citations support the actual claim scope;
- stale, withdrawn, rights-blocked, sensitivity-blocked, or out-of-scope citations fail;
- report outcome and blocking findings are explicit.

Current gap: the `CitationValidationReport` schema is permissive, so field-level report enforcement is not established.

### Stage 10 — policy postcheck

Required checks:

- accepted postcheck entrypoint/version is explicit;
- candidate output and citation report digest are evaluated;
- output obligations are preserved;
- sensitive leakage and reconstruction risk are checked;
- postcheck can downgrade `ANSWER` to `DENY`, `ABSTAIN`, or `ERROR`;
- postcheck absence cannot be treated as success.

### Stage 11 — finite outcome

The runtime-facing outcome must be exactly one of:

```text
ANSWER
ABSTAIN
DENY
ERROR
```

No null, implicit allow, warning-only answer, `UNKNOWN`, `PARTIAL`, or provider-native status should bypass the finite envelope.

### Stage 12 — receipt and envelope closure

Required checks:

- AIReceipt binds run, adapter/model, input/output digests, policy decision, citation validation, and outcome;
- RunReceipt is linked where required;
- RuntimeResponseEnvelope binds evidence refs, policy state, freshness, correction state, and finite outcome;
- receipt refs resolve through accepted stores;
- public clients receive only the governed envelope and approved payload;
- receipt presence is not treated as correctness or release approval.

[Back to top](#top)

---

<a id="validation-input-packet"></a>

## Validation input packet

A future validator should consume an immutable packet or explicit refs rather than scraping unrelated logs.

### Proposed minimum packet

| Field family | Purpose | Current authority |
|---|---|---|
| `profile_ref` / `profile_digest` | Selects accepted stage/order rules. | PROPOSED |
| `request_ref` / `request_digest` | Binds scope and request shape. | PROPOSED |
| `run_id` | Correlates all stages. | AIReceipt contract includes `run_id`. |
| `stage_records` | Ordered stage evidence with sequence/causal refs. | PROPOSED |
| `pre_policy_decision_ref` | Binds policy precheck. | Policy contract/home NEEDS VERIFICATION. |
| `evidence_refs` | Declares requested evidence pointers. | EvidenceRef contract/schema. |
| `resolved_bundle_refs` | Declares admitted EvidenceBundles. | EvidenceBundle contract/schema. |
| `context_digest` | Binds bounded model context without storing it. | PROPOSED |
| `adapter` / `model_ref` | Identifies governed adapter/model. | AIReceipt schema. |
| `candidate_output_digest` | Binds model candidate. | AIReceipt `outputs_digest` may serve or require profile-specific distinction. |
| `citation_validation_ref` | Binds citation findings. | AIReceipt schema requires it. |
| `post_policy_decision_ref` | Binds output policy postcheck. | PROPOSED / NEEDS VERIFICATION. |
| `runtime_response_ref` | Binds finite client envelope. | RuntimeResponseEnvelope contract/schema. |
| `ai_receipt_ref` | Binds AI accountability receipt. | AIReceipt contract/schema. |
| `run_receipt_ref` | Binds general run accountability when required. | RunReceipt contract. |
| `requested_surface` | Declares API/UI/map/export/Focus Mode use. | PROPOSED profile field. |
| `correction_state` | Prevents stale/withdrawn support from passing. | RuntimeResponseEnvelope requires it. |

### Input rejection rules

Reject or abstain when:

- packet schema/version is unknown;
- run identities disagree;
- refs point across incompatible runs;
- digests are malformed or inconsistent;
- stage records are duplicated or missing;
- timestamps regress without an accepted retry model;
- policy/citation/receipt refs are unresolved;
- stage evidence contains secrets or protected payloads;
- profile identity is missing or unaccepted.

[Back to top](#top)

---

<a id="validation-report-contract"></a>

## Validation report contract

The validator should emit a deterministic report, not only console text.

### Proposed report shape

```json
{
  "report_id": "validation:evidence-before-model:<digest>",
  "profile_ref": "profile:evidence-before-model:v1",
  "subject_run_id": "run:<id>",
  "outcome": "PASS",
  "blocking": false,
  "reason_codes": [],
  "stage_findings": [],
  "input_refs": [],
  "output_refs": [],
  "validator_version": "sha256:<digest>",
  "created_at": "RFC3339 timestamp"
}
```

The example is **PROPOSED**. It is not an accepted schema.

### Report requirements

- deterministic ordering;
- stable reason-code vocabulary;
- one primary outcome;
- explicit blocking state;
- per-stage finding identifiers;
- safe, bounded messages;
- ref/digest evidence instead of copied sensitive payloads;
- validator/profile identity;
- no model prose;
- no chain-of-thought;
- no publication decision;
- no automatic EvidenceBundle or PolicyDecision creation.

### Suggested report outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Required ordered gates and references were proven for the declared profile. |
| `FAIL` | One or more deterministic invariant violations were found. |
| `ABSTAIN` | Required support is unresolved or insufficient to decide safely. |
| `DENY` | The requested operation/surface is prohibited by explicit policy posture. |
| `HOLD` | Review, correction, release, or migration closure is required. |
| `ERROR` | Validator could not complete safely. |

`PASS` means only that the configured validator checks passed. It is not truth, policy approval, release approval, or answer authorization by itself.

[Back to top](#top)

---

<a id="finite-outcomes-and-reason-codes"></a>

## Finite outcomes and reason codes

### Validator-level reason-code families

| Family | Examples |
|---|---|
| Profile | `PROFILE_MISSING`, `PROFILE_UNACCEPTED`, `PROFILE_DIGEST_MISMATCH` |
| Request | `REQUEST_MALFORMED`, `REQUEST_SCOPE_AMBIGUOUS`, `REQUEST_LIMIT_EXCEEDED` |
| Ordering | `STAGE_MISSING`, `STAGE_OUT_OF_ORDER`, `DUPLICATE_STAGE`, `RUN_ID_MISMATCH` |
| Policy | `POLICY_PRECHECK_MISSING`, `POLICY_POSTCHECK_MISSING`, `POLICY_REF_UNRESOLVED`, `POLICY_DENIED` |
| Evidence | `EVIDENCE_REF_MISSING`, `EVIDENCE_REF_UNRESOLVED`, `EVIDENCE_BUNDLE_INCOMPLETE`, `EVIDENCE_STALE` |
| Context | `UNAUTHORIZED_CONTEXT`, `LIFECYCLE_CONTEXT_LEAK`, `CONTEXT_DIGEST_MISMATCH`, `CONTEXT_LIMIT_EXCEEDED` |
| Adapter | `ADAPTER_UNAPPROVED`, `MODEL_REF_MISSING`, `ADAPTER_CALLED_TOO_EARLY`, `ADAPTER_SIDE_FETCH_DETECTED` |
| Output | `OUTPUT_SCHEMA_INVALID`, `OUTPUT_DIGEST_MISMATCH`, `INVALID_AI_OUTCOME`, `PROTECTED_CONTENT_LEAK` |
| Citation | `CITATION_VALIDATION_MISSING`, `CITATION_REPORT_UNRESOLVED`, `CITATION_SUPPORT_INSUFFICIENT` |
| Receipt | `AI_RECEIPT_MISSING`, `AI_RECEIPT_INVALID`, `RUN_RECEIPT_MISSING`, `RECEIPT_REF_UNRESOLVED` |
| Correction | `CORRECTION_STATE_MISSING`, `UPSTREAM_WITHDRAWN`, `SUPERSEDED_EVIDENCE_USED`, `ROLLBACK_REQUIRED` |
| Privacy | `PRIVATE_COT_PERSISTED`, `SECRET_EXPOSURE_RISK`, `SENSITIVE_PAYLOAD_IN_REPORT` |
| Runtime | `RUNTIME_ENVELOPE_INVALID`, `PUBLIC_BOUNDARY_BYPASS`, `VALIDATOR_ERROR` |

### Safe reason-code rules

Reason codes should:

- be stable and machine-readable;
- avoid source payload fragments;
- avoid exact protected coordinates;
- avoid living-person identifiers;
- avoid confidential farm/operator data;
- avoid hidden policy thresholds when disclosure would weaken protection;
- avoid provider secrets and prompt text;
- link to detailed internal findings through governed refs where authorized.

[Back to top](#top)

---

<a id="contract-and-schema-maturity"></a>

## Contract and schema maturity

### `AIReceipt`

**CONFIRMED shape:**

- `id`;
- `run_id`;
- `adapter`;
- `model_ref`;
- `inputs_digest`;
- `outputs_digest`;
- `policy_decision_ref`;
- `citation_validation_ref`;
- `outcome`;
- `additionalProperties: false`;
- outcome enum `ANSWER | ABSTAIN | DENY | ERROR`.

**Important limitation:** the schema does not by itself prove that policy happened before model use, that citations were validated after output, or that refs resolve.

### `RuntimeResponseEnvelope`

**CONFIRMED shape and wrapper:**

- strict paired schema;
- finite outcome;
- evidence refs;
- policy state;
- freshness;
- correction state;
- existing top-level validator wrapper using shared JSON Schema plumbing.

**Important limitation:** envelope shape validation does not prove causal stage ordering or admissible context construction.

### `CitationValidationReport`

**CONFIRMED maturity:**

- detailed semantic contract;
- paired schema exists;
- schema has empty `properties` and `additionalProperties: true`;
- no field-level machine contract is established.

A validator cannot safely require a mature report shape until this drift is resolved or a profile explicitly binds a reviewed alternative schema.

### `EvidenceRef` and `EvidenceBundle`

The validator must preserve the distinction:

```text
EvidenceRef = governed pointer
EvidenceBundle = claim-scope closure artifact
```

Resolving a ref does not automatically prove bundle completeness, policy permission, release state, or requested-surface admissibility.

### Policy objects

The repository references `policy/ai/`, but the checked README path was absent. Do not hard-code a guessed policy query path. The accepted runtime policy contract, package namespace, bundle manifest, decision vocabulary, and pre/post distinction remain **NEEDS VERIFICATION**.

[Back to top](#top)

---

<a id="security-privacy-and-prompt-injection"></a>

## Security, privacy, and prompt injection

### Prompt injection posture

All user text, retrieved documents, HTML, PDFs, OCR, metadata, comments, citations, model output, and source-provided instructions are **untrusted content**.

The validator must not:

- execute instructions found in evidence;
- let source text alter validation policy;
- accept a source assertion that it is “approved” or “released”;
- trust model output claiming that gates passed;
- use an embedded prompt to change the accepted profile;
- reveal hidden system prompts or policy internals.

The validation profile and policy refs must come from governed configuration, not from the payload being validated.

### Chain-of-thought boundary

The validator may require:

- stage names;
- decisions;
- safe reason codes;
- refs;
- hashes;
- timestamps;
- tool/adapter identity;
- output/citation spans where authorized.

It must not require:

- private chain-of-thought;
- hidden scratchpad;
- token-by-token model state;
- proprietary provider internals;
- unrestricted prompt logs;
- raw sensitive context when a digest/ref is sufficient.

### Sensitive data posture

Default to deny, restrict, generalize, or abstain for:

- living-person data;
- DNA/genomic data;
- private parcel or operator data;
- rare species locations;
- archaeology site locations;
- protected cultural/sovereignty material;
- critical infrastructure details;
- restricted legal/rights-controlled sources;
- exact locations that enable reconstruction.

### Log minimization

Logs and reports should record:

- refs and digests;
- bounded safe reason codes;
- counts and stage status;
- redacted error locations;
- correlation/run IDs safe for the target audience.

They should not record full model context, credentials, exact protected geometry, source secrets, or private prompts by default.

### Resource and denial-of-service controls

A mature implementation should bound:

- request bytes;
- ref count;
- bundle count;
- stage count;
- nesting depth;
- string length;
- context/token budget;
- citation count;
- file count and size;
- resolver timeouts;
- adapter timeout;
- retry count;
- report size.

Exact limits are **NEEDS VERIFICATION** and should be profile/config driven.

[Back to top](#top)

---

<a id="lifecycle-release-and-correction-boundary"></a>

## Lifecycle, release, and correction boundary

The validator must preserve:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

### Context eligibility

Public or normal governed-AI context should use:

- released artifacts;
- released/policy-safe EvidenceBundles;
- explicitly review-authorized bounded context;
- governed API adapters;
- current correction and freshness state.

It should deny or abstain on:

- direct RAW reads;
- WORK or QUARANTINE material;
- unpromoted candidates;
- internal canonical-store bytes;
- withdrawn or superseded evidence;
- missing release refs where publication is required;
- stale evidence without an accepted stale-use rule.

### Release boundary

The validator can check release linkage. It cannot:

- create a ReleaseManifest;
- approve promotion;
- mark an answer published;
- bypass human review;
- convert a validation pass into public permission.

### Correction cascade

A later correction, withdrawal, rights change, sensitivity change, or source revocation should be able to identify:

- affected EvidenceRefs;
- affected EvidenceBundles;
- affected AIReceipts/RunReceipts;
- affected RuntimeResponseEnvelopes;
- affected cached answers;
- affected public surfaces;
- required revalidation or withdrawal.

A report should retain enough stable refs and digests to support that cascade without copying restricted content.

[Back to top](#top)

---

<a id="test-and-fixture-contract"></a>

## Test and fixture contract

### Current evidence

`tests/validators/ai/evidence_before_model/` did not surface in bounded search.

AIReceipt fixture paths surfaced README files, but concrete valid/invalid JSON payload inventory was not confirmed.

### Proposed test home

```text
tests/validators/ai/evidence_before_model/
├── README.md
├── test_profile_contract.py
├── test_stage_ordering.py
├── test_evidence_resolution.py
├── test_context_admission.py
├── test_citation_and_postcheck.py
├── test_receipt_closure.py
├── test_security_and_redaction.py
└── fixtures/
```

This tree is **PROPOSED**, not a repository fact.

### Required positive cases

- complete `ANSWER` flow;
- policy-precheck `DENY` terminal flow;
- evidence-insufficient `ABSTAIN` terminal flow;
- infrastructure/schema `ERROR` terminal flow;
- valid retry with explicit causal lineage;
- correction-aware revalidation;
- multiple EvidenceBundles with most-restrictive policy preserved.

### Required negative cases

- adapter invoked before policy precheck;
- adapter invoked before EvidenceRef resolution;
- missing EvidenceBundle closure;
- RAW/WORK/QUARANTINE context leak;
- evidence from a different run;
- unresolved policy ref;
- citation report missing;
- citation report exists but is non-blocking despite unsupported claim;
- postcheck missing;
- AIReceipt missing or digest mismatch;
- invalid runtime outcome;
- stale/withdrawn evidence used;
- direct browser-to-model path;
- model side-fetch of ungoverned context;
- private chain-of-thought included;
- prompt injection changes profile/policy;
- sensitive exact geometry leaked in findings;
- unknown stage silently ignored.

### Test properties

Tests should be:

- deterministic;
- no-network by default;
- synthetic or public-safe;
- independent of a live model;
- provider-neutral;
- fail-closed;
- explicit about expected reason codes;
- able to run in CI without secrets.

A mock adapter should be sufficient for ordering tests. Live-provider tests belong in a separately governed, opt-in integration lane.

[Back to top](#top)

---

<a id="ci-admission-contract"></a>

## CI admission contract

A substantive CI job should not merely confirm that files exist.

### Minimum CI checks

1. validate profile/schema files;
2. run positive and negative fixture matrix;
3. prove out-of-order adapter calls fail;
4. prove unresolved evidence cannot yield `ANSWER`;
5. prove missing citation/postcheck cannot yield `ANSWER`;
6. prove private chain-of-thought is rejected/redacted;
7. prove no default network call occurs;
8. validate emitted report shape;
9. validate AIReceipt and RuntimeResponseEnvelope refs;
10. detect duplicate canonical implementation paths;
11. upload a bounded machine-readable test report;
12. fail the job on any blocking finding.

### Current status

No evidence-before-model workflow or blocking job was verified. Workflow presence elsewhere does not establish this invariant.

### Merge/release significance

Before this validator becomes release-gating:

- owners must be assigned;
- profile/version policy must be accepted;
- fixtures and tests must be reviewed;
- report schema must be accepted;
- false-positive/false-negative posture must be documented;
- override process must be governed;
- release and rollback integration must be tested;
- separation of duties should be considered.

[Back to top](#top)

---

<a id="migration-and-compatibility"></a>

## Migration and compatibility

### Current migration question

Choose the durable relationship between:

```text
tools/validators/ai/validate_evidence_before_model.py
tools/validators/ai/evidence_before_model/
```

### Safe migration requirements

- name the canonical implementation path;
- preserve a compatibility wrapper only when necessary;
- publish a deprecation notice for old CLI/import paths;
- avoid two independent implementations;
- update parent and child READMEs;
- update tests, fixtures, profiles, CI, and docs;
- record behavior/version changes;
- provide rollback target;
- preserve finite outcomes and reason-code mapping;
- verify consumers before removing the old path.

### Compatibility rules

A compatibility wrapper should:

- contain minimal delegation code;
- import one canonical implementation;
- preserve documented exit codes;
- emit a deprecation warning that contains no sensitive data;
- have a removal version/date or explicit review trigger;
- be tested against the same fixture matrix.

A wrapper must not fork logic, maintain its own policy paths, or silently normalize failures into success.

[Back to top](#top)

---

<a id="smallest-sound-implementation-sequence"></a>

## Smallest sound implementation sequence

1. **Resolve topology.** Select child-owned implementation or parent-owned implementation and document migration.
2. **Define profile contract.** Establish immutable stage names, order, required refs, and version/digest rules.
3. **Define report schema.** Add a machine-checkable validation report with finite outcomes and safe findings.
4. **Verify policy contract.** Identify accepted precheck/postcheck entrypoints and decision object.
5. **Verify evidence resolution contract.** Define ref resolver and bundle-admission results.
6. **Resolve citation-report maturity.** Replace permissive scaffold or bind an accepted alternative.
7. **Add synthetic fixtures.** Include full positive and negative ordering matrix.
8. **Implement pure validation core.** No network, model, publication, or side effects.
9. **Add CLI wrapper.** Explicit inputs, JSON output, stable exit codes.
10. **Add tests.** Unit, contract, ordering, privacy, injection, and migration tests.
11. **Add CI.** Blocking no-network suite with artifact report.
12. **Integrate runtime in shadow mode.** Observe without granting authority.
13. **Review results.** Measure gaps and false classifications.
14. **Govern release-gate adoption.** Require appropriate review/ADR if validator becomes promotion-critical.
15. **Document correction and rollback.** Test invalidation of cached answers and receipts.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

This lane is not implementation-complete until all applicable items are verified:

- [ ] canonical implementation path accepted;
- [ ] parent placeholder removed, delegated, or formally retained;
- [ ] owners and CODEOWNERS assigned;
- [ ] profile schema/version/digest accepted;
- [ ] deterministic stage ledger defined;
- [ ] EvidenceRef resolver contract verified;
- [ ] EvidenceBundle admission contract verified;
- [ ] policy precheck/postcheck contract verified;
- [ ] CitationValidationReport schema made substantive or replaced by accepted profile;
- [ ] AIReceipt validator and fixtures verified;
- [ ] RuntimeResponseEnvelope linkage verified;
- [ ] structured validation report schema accepted;
- [ ] stable reason-code vocabulary accepted;
- [ ] no-network validation core implemented;
- [ ] model-independent mock tests pass;
- [ ] prompt-injection and sensitive-data cases pass;
- [ ] chain-of-thought non-persistence tests pass;
- [ ] correction/withdrawal cascade tests pass;
- [ ] CI blocks invalid ordering;
- [ ] emitted reports/receipts use accepted roots;
- [ ] runtime integration is observable and reversible;
- [ ] release-gate adoption, if any, is separately governed;
- [ ] rollback and deprecation are tested;
- [ ] human review recorded.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| ID | Question | Status | Required evidence |
|---|---|---|---|
| EBM-001 | Which path is the canonical implementation home? | **NEEDS VERIFICATION** | Maintainer decision, migration note, or ADR. |
| EBM-002 | Is the parent-level placeholder referenced by consumers? | **UNKNOWN** | Exhaustive imports/CLI/workflow search. |
| EBM-003 | What is the accepted validation profile object? | **UNKNOWN** | Contract/schema/profile registry. |
| EBM-004 | How is causal order proven beyond timestamps? | **NEEDS VERIFICATION** | Stage ledger/sequence/parent-ref contract and tests. |
| EBM-005 | What resolver proves EvidenceRef → EvidenceBundle closure? | **NEEDS VERIFICATION** | Package/API contract, tests, runtime evidence. |
| EBM-006 | What is the accepted precheck policy entrypoint? | **UNKNOWN** | Policy bundle/manifest/query contract. |
| EBM-007 | What is the accepted postcheck policy entrypoint? | **UNKNOWN** | Policy bundle/manifest/query contract. |
| EBM-008 | Why is `policy/ai/` referenced but not found? | **NEEDS VERIFICATION** | Directory audit and migration decision. |
| EBM-009 | Is `policy/ai_builder/` intentionally separate? | **NEEDS VERIFICATION** | Policy ownership docs/ADR. |
| EBM-010 | Is AIReceipt emitted by any active runtime? | **UNKNOWN** | Code, logs, receipts, tests. |
| EBM-011 | Where is `validate_ai_receipt.py`? | **NOT FOUND / NEEDS VERIFICATION** | Repository path or schema metadata correction. |
| EBM-012 | Are AIReceipt JSON fixtures present? | **NEEDS VERIFICATION** | Direct directory inventory. |
| EBM-013 | What schema governs CitationValidationReport fields? | **NEEDS VERIFICATION** | Expanded schema, fixtures, validator. |
| EBM-014 | Which runtime invokes the evidence-before-model check? | **UNKNOWN** | Application/runtime code and tests. |
| EBM-015 | Which CI job enforces it? | **UNKNOWN** | Workflow and current run evidence. |
| EBM-016 | What are resource budgets? | **NEEDS VERIFICATION** | Config/profile and stress tests. |
| EBM-017 | What canonicalization binds context and output digests? | **NEEDS VERIFICATION** | Spec/hash contract and tests. |
| EBM-018 | How are retries represented without false order violations? | **NEEDS VERIFICATION** | Retry/attempt lineage contract. |
| EBM-019 | How are partial citation failures mapped to finite outcomes? | **NEEDS VERIFICATION** | Policy/profile matrix and tests. |
| EBM-020 | What sensitive-data and sovereignty reviewers are required? | **NEEDS VERIFICATION** | Review policy/CODEOWNERS. |
| EBM-021 | What telemetry is safe and required? | **NEEDS VERIFICATION** | Telemetry contract and redaction tests. |
| EBM-022 | How are prior answers invalidated after correction? | **NEEDS VERIFICATION** | Correction cascade and cache invalidation tests. |
| EBM-023 | Is the validator release-gating or advisory? | **UNKNOWN** | Promotion/release configuration and governance decision. |
| EBM-024 | What is the deprecation window for moved entrypoints? | **NEEDS VERIFICATION** | Migration/deprecation record. |
| EBM-025 | What are current pass/fail rates? | **UNKNOWN** | CI/runtime artifacts and dashboards. |

[Back to top](#top)

---

<a id="correction-rollback-and-deprecation"></a>

## Correction, rollback, and deprecation

### Documentation-only rollback

For this README revision:

- restore the prior README blob;
- remove or revert the paired generated receipt;
- no runtime, model, policy, evidence, or release rollback is required.

### Future implementation rollback

An executable rollout should define:

- previous implementation/profile digest;
- feature flag or kill switch;
- previous CLI/import path;
- report schema compatibility;
- cached-answer invalidation;
- receipt and envelope version handling;
- migration reversal steps;
- data/report cleanup rules;
- incident owner;
- criteria for re-enabling.

### Correction handling

When this README or later implementation contains an incorrect claim:

1. record the correction;
2. identify affected consumers and docs;
3. update the truth label;
4. preserve prior version/history;
5. re-run link/contract/test checks;
6. invalidate misleading generated reports where necessary;
7. keep the correction path auditable.

### Deprecation

Do not delete a compatibility path merely because a new path exists. Verify consumers, publish a deprecation period, test the wrapper, and provide a rollback target.

[Back to top](#top)

---

<a id="evidence-ledger"></a>

## Evidence ledger

| Evidence | What it supports | Limit |
|---|---|---|
| Target README prior blob | Prior proposed lane contract. | Documentation only. |
| Parent placeholder file | Confirms named path but no executable behavior. | Does not prove imports or consumers. |
| Parent AI validator README | Confirms child routing and doctrine boundary. | Draft; no implementation proof. |
| Governed-AI Focus Flow | Confirms intended stage sequence and finite outcomes. | Implementation explicitly proposed. |
| AIReceipt contract/schema | Confirms required fields, closed shape, finite outcomes. | Status PROPOSED; runtime emission unverified. |
| RuntimeResponseEnvelope contract/schema | Confirms client envelope fields and finite outcomes. | Does not prove stage order. |
| Runtime response validator wrapper | Confirms schema wrapper implementation. | Validates envelope shape only. |
| CitationValidationReport contract/schema | Confirms semantic intent and schema permissiveness. | No substantive field enforcement. |
| Evidence validator README | Confirms evidence-validation responsibility split. | Draft/index; no runner proof. |
| Bounded test search | No `tests/validators/ai/` implementation surfaced. | Not exhaustive filesystem proof. |
| Bounded policy lookup | `policy/ai/README.md` not found. | Other policy files may exist; canonical home unresolved. |
| Directory Rules | Supports existing `tools/` placement and responsibility separation. | Does not choose child-vs-parent implementation automatically. |

### Evidence limits

This README does not prove:

- active runtime enforcement;
- model adapter behavior;
- policy decision correctness;
- EvidenceBundle completeness;
- citation validation correctness;
- current CI results;
- production use;
- release-gate adoption;
- operational health.

[Back to top](#top)

---

## Review checklist

- [ ] All implementation claims cite current repository evidence.
- [ ] Child/parent implementation topology is explicit.
- [ ] Validator remains model-independent and no-network by default.
- [ ] EvidenceRef and EvidenceBundle are not collapsed.
- [ ] Policy precheck and postcheck are distinct and resolvable.
- [ ] Citation validation is required before `ANSWER`.
- [ ] Runtime outcome is enum-strict.
- [ ] AIReceipt and RuntimeResponseEnvelope linkage is checked.
- [ ] Reports contain refs/digests rather than sensitive payloads.
- [ ] Private chain-of-thought is never required or persisted.
- [ ] Prompt injection cannot alter profile or policy.
- [ ] RAW/WORK/QUARANTINE/internal-store leakage fails closed.
- [ ] Correction, withdrawal, and rollback state are represented.
- [ ] Tests are deterministic, synthetic, and provider-neutral.
- [ ] CI is substantive, not presence-only.
- [ ] Release approval remains outside validator authority.
- [ ] Human review is recorded before merge/promotion.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-16 |
| Version | v0.2 |
| Review state | Draft repository-grounded README update; human review pending. |
| Current maturity | README-only child plus parent-level docstring placeholder. |
| Next smallest safe change | Resolve canonical implementation placement and define the immutable validation profile/report contract before adding executable behavior. |

## Changelog

### v0.2 — 2026-07-16

- Reclassified the child lane as README-only.
- Confirmed and bounded the parent-level docstring placeholder.
- Added explicit child/parent placement conflict and one-implementation rule.
- Grounded AIReceipt, RuntimeResponseEnvelope, and CitationValidationReport maturity.
- Distinguished envelope shape validation from end-to-end gate-ordering proof.
- Recorded absent `policy/ai/README.md`, absent child test lane, unverified CI, and fixture uncertainty.
- Added stage contract, input packet, deterministic report, outcome/reason-code guidance, prompt-injection controls, privacy/log limits, lifecycle/release/correction boundaries, test matrix, CI contract, migration, implementation sequence, definition of done, verification register, and rollback.

### v0.1 — 2026-07-07

- Introduced the proposed evidence-before-model validator lane.

[Back to top](#top)
