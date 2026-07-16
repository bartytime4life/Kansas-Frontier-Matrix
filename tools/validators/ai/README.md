<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-ai-readme
title: tools/validators/ai/ — Governed-AI Validator Routing and Compatibility Boundary
type: readme; directory-readme; validator-parent-index; governed-ai; non-authoritative
version: v0.2
status: draft; repository-grounded; parent-index; one-child-readme; mixed-validator-maturity; policy-home-drift; schema-authority-drift; runtime-enforcement-unverified
owners: OWNER_TBD — Governed AI steward · Validator steward · Evidence steward · Policy steward · Runtime steward · Citation steward · Schema steward · Security steward · Privacy/sensitivity steward · Release steward · Docs steward
created: 2026-07-07
updated: 2026-07-16
supersedes: v0.1 proposed AI validator parent guide
policy_label: "repository-facing; tools; validators; governed-ai; evidence-first; policy-aware; cite-or-abstain; fail-closed; provider-neutral; finite-outcomes; receipt-aware; prompt-injection-aware; no-chain-of-thought; correction-aware; rollback-aware; no-network-by-default; no-truth-authority; no-policy-authority; no-release-authority"
owning_root: tools/
current_path: tools/validators/ai/README.md
responsibility: >
  Repository-grounded parent routing and compatibility boundary for AI-specific validators. This lane indexes
  governed-AI invariants, child validator ownership, shared/top-level validator dependencies, contract/schema/policy/
  fixture/test/CI maturity, finite findings, correction and rollback expectations, and the prohibition on treating
  generated language or validator success as truth, policy permission, release approval, or publication authority.
truth_posture: >
  CONFIRMED target README v0.1 and prior blob; one direct child README at evidence_before_model/; parent-level
  validate_evidence_before_model.py as a docstring-only placeholder; top-level validate_ai_receipt.py as a
  NotImplementedError stub; working shared-schema wrappers for RuntimeResponseEnvelope, DecisionEnvelope, and
  EvidenceBundle; strict PROPOSED runtime AIReceipt schema with valid/invalid JSON fixtures; generic contract-fixture
  test discovery and contracts-validate workflow; permissive duplicate AIReceipt scaffold under schemas/contracts/v1/ai
  despite index-only guidance; permissive CitationValidationReport schema scaffold; canonical provider-neutral
  runtime/model_adapters documentation lane; proposed ADR-0019; absent policy/ai/README.md; greenfield policy/focus and
  policy/runtime READMEs; repository-present policy/ai_builder lane that governs repository authoring rather than
  public/runtime AI answers / PROPOSED parent validator profile, delegation contract, validation packet/report, finite
  finding vocabulary, child admission rules, tests, CI, migration, correction, deprecation, and rollback / CONFLICTED
  child-lane implementation placement versus the parent-level evidence-before-model placeholder; strict runtime
  AIReceipt schema versus permissive AI-family duplicate; AIReceipt fixture coverage versus dedicated validator stub;
  proposed policy/ai references versus absent path / UNKNOWN active governed-AI runtime enforcement, production
  consumers, policy pre/post entrypoints, evidence resolver admission behavior, citation validator implementation,
  AIReceipt persistence, child runner, emitted AI validation reports, operational metrics, release-gate adoption,
  deployment, and current end-to-end results / NEEDS VERIFICATION owners, CODEOWNERS, accepted AI validator topology,
  schema-family disposition, policy-family disposition, stable report contract, reason-code registry,
  canonicalization/digest rules, resource budgets, security review, correction propagation, deprecation window, and
  rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: d6efbbf69a6d2f5a3eeff1512e9c57e2131a12cf
  prior_blob: 829589614cff7aec864e3d5802fcc693dc30d3a5
  child_readme_blob: 53734e6c23d64b911f565b6e9a182a4c98511148
  child_placeholder_blob: 06b714d90874d69e6ba64cd674ff0c7dfe40e774
  ai_receipt_validator_stub_blob: 76a03f2c81e7e86057e342447f29efdf0f824468
  runtime_response_validator_blob: 11ddc64c4299d103b0eef383c2f7bdd3bb12f1f9
  common_schema_test_blob: b04342cc034d7f1cc554e155fdd02d6e972976e6
  contracts_validate_workflow_blob: fba63efbae13c665a04d699f0651937dfbf633b3
  ai_receipt_runtime_schema_blob: 2e0bebdb3a38acbc3c58a919db46970c6e829b4a
  ai_receipt_ai_schema_blob: 81425a2c34396f1ad969ad39236a02f45fde4265
  ai_receipt_valid_fixture_blob: 224965e8e6971d7b203d66b5a9258fa04dd1c9d6
  ai_receipt_invalid_fixture_blob: 5cd6644d671eae08de018815f576ae5e46ee41ed
  ai_schema_index_blob: 4e644ec1dd2dfda05685348dced918791e4234d7
  contracts_ai_readme_blob: 31281539386f6757cb384f2645388fe626bb9eb3
  model_adapters_readme_blob: 16456452e03884dabb24c670c41c9e359f679769
  ai_builder_policy_readme_blob: c581bee37878223b8f0dba17828732b1de3bee31
  focus_policy_readme_blob: f20943b20fa5ac21c4ba7769e3ec14f463685bea
  runtime_policy_readme_blob: b9bfee731553c504b514f07a6862ef3e68328f02
  adr_0019_blob: db55defa15fa709b20c613cf595adc334fe785ba
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  pr_template_blob: 13c5d4ed045e201188ebb54b518a586b42b481d4
  generated_receipt_schema_blob: fba21ed27ebccf1362fe397fe0c3ebd85e072685
  bounded_path_checks:
    - tools/validators/ai/ surfaced this README, evidence_before_model/README.md, and validate_evidence_before_model.py
    - evidence_before_model/ is README-only in bounded search
    - validate_evidence_before_model.py is a docstring-only placeholder
    - tools/validators/validate_ai_receipt.py exists as a NotImplementedError greenfield stub
    - tools/validators/validate_runtime_response_envelope.py is a working shared-schema wrapper
    - AIReceipt runtime schema has valid and invalid JSON fixtures
    - tests/schemas/test_common_contracts.py discovers runtime schemas with matching fixture directories
    - contracts-validate workflow installs test dependencies and runs make test
    - tests/validators/ai/ did not surface as an implemented dedicated test lane
    - policy/ai/README.md did not surface
    - policy/focus/README.md and policy/runtime/README.md are greenfield bundle stubs
    - policy/ai_builder/ is repository-authoring policy and explicitly excludes public user answer generation
    - schemas/contracts/v1/ai/README.md says the lane is compatibility/index only, but ai_receipt.schema.json exists there as a permissive scaffold
related:
  - ../README.md
  - ../_common/README.md
  - ../evidence/README.md
  - ./evidence_before_model/README.md
  - ./validate_evidence_before_model.py
  - ../validate_ai_receipt.py
  - ../validate_evidence_bundle.py
  - ../validate_decision_envelope.py
  - ../validate_runtime_response_envelope.py
  - ../../../docs/architecture/governed-ai.md
  - ../../../docs/architecture/governed-ai/FOCUS_FLOW.md
  - ../../../docs/architecture/governed-ai/AI_RECEIPTS.md
  - ../../../docs/architecture/governed-ai/BOUNDARIES.md
  - ../../../docs/architecture/governed-ai/PROMPT_INJECTION.md
  - ../../../docs/doctrine/ai-as-assistant.md
  - ../../../docs/doctrine/evidence-first.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0019-ai-adapter-contract-and-finite-envelopes.md
  - ../../../contracts/ai/README.md
  - ../../../contracts/runtime/ai_receipt.md
  - ../../../contracts/runtime/decision_envelope.md
  - ../../../contracts/runtime/runtime_response_envelope.md
  - ../../../contracts/runtime/run_receipt.md
  - ../../../contracts/evidence/evidence_ref.md
  - ../../../contracts/evidence/evidence_bundle.md
  - ../../../contracts/evidence/citation_validation_report.md
  - ../../../schemas/contracts/v1/ai/README.md
  - ../../../schemas/contracts/v1/ai/ai_receipt.schema.json
  - ../../../schemas/contracts/v1/runtime/ai_receipt.schema.json
  - ../../../schemas/contracts/v1/runtime/decision_envelope.schema.json
  - ../../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
  - ../../../schemas/contracts/v1/evidence/evidence_ref.schema.json
  - ../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json
  - ../../../schemas/contracts/v1/evidence/citation_validation_report.schema.json
  - ../../../fixtures/contracts/v1/runtime/ai_receipt/
  - ../../../fixtures/contracts/v1/runtime/decision_envelope/
  - ../../../fixtures/contracts/v1/runtime/runtime_response_envelope/
  - ../../../policy/ai_builder/README.md
  - ../../../policy/focus/README.md
  - ../../../policy/runtime/README.md
  - ../../../runtime/model_adapters/README.md
  - ../../../runtime/model_adapters/AdapterContract.md
  - ../../../runtime/model_adapters/mock/README.md
  - ../../../data/proofs/evidence_bundle/
  - ../../../data/proofs/citation_validation/
  - ../../../data/receipts/ai/
  - ../../../data/receipts/validation/
  - ../../../apps/governed-api/
  - ../../../tests/schemas/test_common_contracts.py
  - ../../../.github/workflows/contracts-validate.yml
  - ../../../release/
tags: [kfm, tools, validators, ai, governed-ai, parent-index, evidence-before-model, evidence-ref, evidence-bundle, ai-receipt, decision-envelope, runtime-response-envelope, citation-validation, provider-neutral, finite-outcomes, prompt-injection, no-chain-of-thought, fail-closed, cite-or-abstain, schema-drift, policy-drift, migration, correction, rollback]
notes:
  - "This revision changes only tools/validators/ai/README.md plus the required generated provenance receipt."
  - "No validator code, schema, contract, policy, fixture, test, workflow, adapter, receipt instance, proof, release record, API route, model call, or public output is created or modified."
  - "This README corrects the stale assumption that validate_ai_receipt.py and AIReceipt JSON fixtures were absent; both are present, but the dedicated validator remains a stub."
  - "A later code move, activation, schema consolidation, policy-home decision, or release-gate adoption must use a reviewed migration/ADR path."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed-AI Validator Routing and Compatibility Boundary

`tools/validators/ai/`

> **One-line purpose.** This directory is the parent routing and compatibility boundary for deterministic governed-AI validators. It coordinates evidence-before-model ordering, evidence and citation closure, policy pre/post posture, provider-neutral adapter boundaries, finite runtime envelopes, AIReceipt accountability, safe negative outcomes, correction, and rollback—without calling models or becoming evidence, policy, release, or public-answer authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Version: v0.2" src="https://img.shields.io/badge/version-v0.2-informational">
  <img alt="Root: tools" src="https://img.shields.io/badge/root-tools%2F-blue">
  <img alt="Lane: parent index" src="https://img.shields.io/badge/lane-parent__index-lightgrey">
  <img alt="Child lanes: one README" src="https://img.shields.io/badge/children-one__README-orange">
  <img alt="Implementation: mixed" src="https://img.shields.io/badge/implementation-mixed-critical">
  <img alt="Posture: cite or abstain" src="https://img.shields.io/badge/posture-cite__or__abstain-success">
</p>

> [!IMPORTANT]
> **AI validation is not AI truth.** A passing schema validator, receipt validator, stage-order validator, or parent runner means only that configured checks passed for a declared scope. It does not make generated text true, evidence complete, policy permissive, a model approved, a release accepted, or a public answer authorized.

> [!CAUTION]
> **Current implementation is fragmented.** The only child lane is README-only; `validate_evidence_before_model.py` is a docstring placeholder; `validate_ai_receipt.py` raises `NotImplementedError`; shared runtime-envelope and evidence schema wrappers exist outside this directory; policy homes are unresolved or stubbed; and no dedicated `tests/validators/ai/` lane surfaced.

> [!WARNING]
> **Do not preserve private chain-of-thought.** AI validators may inspect bounded request metadata, stage records, refs, hashes, finite decisions, and safe findings. They must not require, log, store, or treat private chain-of-thought, hidden model state, credentials, raw restricted content, or sensitive exact-location data as evidence.

**Quick links:** [Purpose](#purpose) · [Status](#status-and-evidence) · [Placement](#directory-rules-and-authority) · [Inventory](#confirmed-repository-inventory) · [Routing](#validator-routing-map) · [Children](#child-lane-contract) · [Dependencies](#shared-and-top-level-validator-dependencies) · [Invariants](#governed-ai-validation-invariants) · [Reports](#validation-report-contract) · [Outcomes](#finite-validator-outcomes) · [Contracts](#contract-schema-and-fixture-maturity) · [Policy](#policy-routing-and-drift) · [Runtime](#runtime-adapter-and-public-boundary) · [Security](#security-privacy-and-prompt-injection) · [Lifecycle](#lifecycle-release-correction-and-rollback) · [Tests](#tests-fixtures-and-ci) · [Implementation](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Migration](#migration-compatibility-and-deprecation) · [Open](#open-verification-register) · [Rollback](#rollback-path) · [Ledger](#evidence-ledger) · [Changelog](#changelog)

---

<a id="purpose"></a>

## Purpose

`tools/validators/ai/` is the parent lane for AI-specific checker orchestration and routing.

It answers:

> Which deterministic validators are required to prove that an AI-mediated KFM event remained downstream of evidence, policy, release, correction state, and governed runtime envelopes—and which missing or contradictory support must force failure, abstention, denial, hold, or review?

The parent may:

- index child AI validator lanes;
- identify shared validator dependencies;
- define cross-child routing and aggregation;
- document accepted input/report envelopes;
- normalize finite findings and safe reason codes;
- surface contract, schema, policy, fixture, and path drift;
- require no-network tests, correction, and rollback.

The parent must not:

- invoke or select a model;
- define evidence or policy;
- repair missing evidence by fabrication;
- approve release;
- expose raw model output;
- publish answers;
- persist private chain-of-thought;
- convert generated language into evidence;
- treat a passing child as publication permission.

```text
AI validator result          != runtime answer outcome
AIReceipt shape pass         != evidence-before-model proof
RuntimeResponseEnvelope pass != policy/evidence/citation closure
EvidenceBundle closure       != policy permission
Policy allow                 != release approval
Release approval             != model truth
```

[Back to top](#top)

---

<a id="status-and-evidence"></a>

## Status and evidence

| Surface | Status | Safe conclusion |
|---|---:|---|
| Parent README | **CONFIRMED v0.1 before revision** | Proposed guide existed but understated mixed implementation and drift. |
| Direct child lanes | **CONFIRMED one README child** | `evidence_before_model/README.md` exists; no executable surfaced inside that child directory. |
| Parent-level evidence-before-model file | **CONFIRMED placeholder** | `validate_evidence_before_model.py` contains only a `PROPOSED` docstring. |
| Top-level AIReceipt validator | **CONFIRMED stub** | `tools/validators/validate_ai_receipt.py` raises `NotImplementedError`. |
| RuntimeResponseEnvelope validator | **CONFIRMED working schema wrapper** | Validates envelope shape/fixtures; not end-to-end AI ordering. |
| DecisionEnvelope and EvidenceBundle validators | **CONFIRMED working schema wrappers** | Reusable shape checks exist outside the AI parent lane. |
| AIReceipt runtime schema | **CONFIRMED strict, status PROPOSED** | Required fields, digests, refs, finite outcome, and closed properties are machine-shaped. |
| AIReceipt runtime fixtures | **CONFIRMED JSON payloads** | Valid and invalid files exist. |
| Generic fixture harness | **CONFIRMED** | Discovers runtime schemas with matching fixture directories. |
| Contract test workflow | **CONFIRMED wiring** | `contracts-validate` runs `make test`; current pass results are not claimed here. |
| Duplicate AIReceipt schema | **CONFIRMED conflict** | AI-family copy is a permissive empty-property scaffold. |
| AI schema parent guidance | **CONFIRMED index-only guidance** | Says not to add canonical definitions without ADR/migration. |
| AI policy home | **CONFLICTED / unresolved** | `policy/ai/README.md` absent; Focus/runtime policy are stubs; AI-builder policy is a different bounded context. |
| Provider-neutral adapter lane | **CONFIRMED docs lane / implementation mixed** | `runtime/model_adapters/` is canonical documentation/handoff. |
| ADR-0019 | **CONFIRMED proposed/draft** | Not accepted authority. |
| Dedicated AI tests, parent runner, runtime invocation, emitted reports, release-gate adoption | **UNKNOWN / NEEDS VERIFICATION** | No operational claim is made. |

Safe maturity summary:

```text
parent routing README                       CONFIRMED
one child README                            CONFIRMED
evidence-before-model implementation        PLACEHOLDER ONLY
AIReceipt dedicated validator               STUB / NotImplementedError
shared runtime/evidence shape validators    PARTIALLY IMPLEMENTED
AIReceipt strict schema + JSON fixtures     CONFIRMED / PROPOSED status
generic schema fixture tests                CONFIRMED WIRING
dedicated AI behavior tests                 NOT ESTABLISHED
runtime AI policy                           UNRESOLVED / STUBBED
active model/runtime enforcement            UNKNOWN
release-gate use                            UNKNOWN
```

[Back to top](#top)

---

<a id="directory-rules-and-authority"></a>

## Directory Rules and authority

The existing parent path remains correct:

```text
tools/validators/ai/
```

`tools/` owns reusable checkers. It does not own contracts, schemas, policy, evidence, receipts, runtime adapters, public serving, tests, or release decisions.

| Responsibility | Owning home | Parent role |
|---|---|---|
| AI validator parent routing | `tools/validators/ai/` | Index and optional future parent runner. |
| Evidence-before-model invariant | child lane after topology resolution | Child contract; implementation unestablished there. |
| Shared validator plumbing | `tools/validators/_common/` | Consume; do not duplicate. |
| Generic evidence validation | `tools/validators/evidence/` and top-level validators | Delegate/reference. |
| AIReceipt shape validator | current top-level stub or ADR-selected successor | Track; do not claim active validation. |
| Runtime/decision/evidence envelope validators | top-level shared wrappers | Consume; do not fork runner logic. |
| Semantic meaning | `contracts/ai/`, `contracts/runtime/`, `contracts/evidence/` | Validate, never redefine. |
| Machine shape | runtime/evidence schema families; AI compatibility lane pending disposition | Validate, never choose silently. |
| Runtime answer policy | accepted Focus/runtime policy lane | Check refs/outcomes, never author policy. |
| AI-builder repository policy | `policy/ai_builder/` | Separate concern. |
| Evidence/citation proof | `data/proofs/` | Check refs; never create authority. |
| Receipts | `data/receipts/` | Check links; do not store instances here. |
| Provider-neutral adapters | `runtime/model_adapters/` | Validate boundary; do not implement adapters. |
| Public API | `apps/governed-api/` | Validate envelopes/boundaries; no routes here. |
| Tests and fixtures | `tests/`, `fixtures/` | Require proof; do not bury fixtures in tools. |
| Release/correction/rollback | `release/` | Check refs; never decide promotion. |

The parent prevents these collapses:

- schema presence into semantic correctness;
- validator pass into policy permission;
- policy permission into release approval;
- AIReceipt presence into evidence closure;
- EvidenceRef presence into EvidenceBundle resolution;
- report presence into citation pass;
- RuntimeResponseEnvelope shape into stage-order proof;
- model execution into public authorization;
- generated language into evidence;
- unknown policy into implicit allow;
- duplicate schema paths into dual authority;
- receipt hashes into truth.

[Back to top](#top)

---

<a id="confirmed-repository-inventory"></a>

## Confirmed repository inventory

### Direct parent inventory

| Path | State |
|---|---|
| `README.md` | Parent README. |
| `evidence_before_model/README.md` | Repository-grounded child contract; child implementation absent. |
| `validate_evidence_before_model.py` | Eight-line docstring placeholder. |

```text
tools/validators/ai/
├── README.md
├── validate_evidence_before_model.py           # placeholder; placement conflict
└── evidence_before_model/
    └── README.md                                # child contract; no implementation
```

### Relevant validators outside the parent

| Path | State | Relationship |
|---|---|---|
| `tools/validators/validate_ai_receipt.py` | `NotImplementedError` stub | Dedicated AIReceipt path, not active. |
| `tools/validators/validate_runtime_response_envelope.py` | Working schema wrapper | Validates response shape. |
| `tools/validators/validate_decision_envelope.py` | Working schema wrapper | Validates decision shape. |
| `tools/validators/validate_evidence_bundle.py` | Working schema wrapper | Validates EvidenceBundle shape. |
| `tools/validators/_common/` | Working registry/runner | Shared compatibility-sensitive plumbing. |
| `tools/validators/evidence/README.md` | Evidence validator index | Evidence closure routing, not proof storage. |

This inventory is bounded to the pinned snapshot; it is not a deployment inventory.

[Back to top](#top)

---

<a id="validator-routing-map"></a>

## Validator routing map

One active implementation is allowed per concern.

| Concern | Preferred routing | Current state |
|---|---|---|
| Parent aggregation | `tools/validators/ai/` | README only. |
| Evidence-before-model ordering | child lane after accepted placement | Child README plus parent-level placeholder conflict. |
| AIReceipt shape | strict runtime schema plus accepted validator | Schema/fixtures exist; dedicated validator stubbed. |
| RuntimeResponseEnvelope shape | top-level wrapper | Implemented. |
| DecisionEnvelope shape | top-level wrapper | Implemented. |
| EvidenceBundle shape | top-level wrapper | Implemented. |
| Evidence resolution/closure | accepted resolver/evidence validator | Runtime behavior unverified. |
| Citation validation | accepted evidence/citation validator | Contract detailed; schema permissive. |
| Policy pre/post checks | accepted Focus/runtime policy lane | Current READMEs stubbed/unresolved. |
| Provider/model boundary | `runtime/model_adapters/` | Canonical docs lane; implementation mixed. |
| Public answer | governed runtime/API | Not owned by validators. |

A future parent runner should only aggregate:

```text
parent request
  -> validate profile identity
  -> invoke declared child/dependency validators
  -> verify cross-report identity and ordering
  -> aggregate deterministically
  -> emit one parent ValidationReport
  -> never call a model
  -> never approve release
```

Forbidden shortcuts:

- infer implementation from README presence;
- infer order from timestamps without stable event identity;
- treat an envelope as proof of its producing stages;
- accept the permissive AI-family AIReceipt schema as coequal;
- treat `policy/ai_builder/` as runtime answer policy;
- default to `ANSWER` when policy/evidence/citation is missing;
- run provider-specific code from a validator;
- store hidden reasoning for audit;
- combine validator findings and public answers into one authority object.

[Back to top](#top)

---

<a id="child-lane-contract"></a>

## Child-lane contract

| Child | Invariant | Status |
|---|---|---|
| [`evidence_before_model/`](evidence_before_model/) | Evidence/policy/release/correction gates precede model influence; citation validation and policy postcheck close the result. | README confirmed; child executable absent; parent placeholder conflict confirmed. |

A child must expose:

- stable profile identity/version;
- explicit input and report contracts;
- deterministic outcomes and safe reason codes;
- declared dependencies;
- no-network fixtures;
- positive and negative tests;
- security/privacy review;
- correction and rollback behavior;
- no model calls;
- no policy authorship;
- no release authority.

Do not add or activate another child until:

1. its invariant is distinct;
2. it is not already shared/top-level logic;
3. input/report contracts are accepted or clearly proposed;
4. fixtures/tests exist;
5. placement follows Directory Rules;
6. migration from duplicates is documented;
7. one active implementation remains.

[Back to top](#top)

---

<a id="shared-and-top-level-validator-dependencies"></a>

## Shared and top-level validator dependencies

| Validator/test | Can prove | Cannot prove |
|---|---|---|
| `validate_ai_receipt.py` today | File presence only; it raises `NotImplementedError`. | AIReceipt conformance or runtime behavior. |
| `validate_runtime_response_envelope.py` | Envelope JSON shape. | Evidence resolution, policy execution, ordering, citation pass, receipt persistence. |
| `validate_decision_envelope.py` | Decision-envelope shape. | Correct policy logic or release permission. |
| `validate_evidence_bundle.py` | EvidenceBundle JSON shape. | Claim truth, rights clearance, policy/release approval. |
| `test_common_contracts.py` | Discovered valid fixtures pass and invalid fixtures fail. | Dedicated AI behavior, causality, provider safety. |
| Future parent runner | Cross-report identity, dependencies, aggregation. | Model truth, policy authorship, release approval. |

Required failure posture:

| Gap | Parent result |
|---|---|
| AIReceipt validator required but stubbed | `HOLD` or `ERROR`. |
| Evidence-before-model implementation missing | `HOLD` / `AI_CHILD_UNIMPLEMENTED`. |
| Runtime envelope invalid | `FAIL`. |
| EvidenceRef unresolved | `ABSTAIN` or `DENY` under accepted policy. |
| Policy unavailable | fail closed; never implicit allow. |
| Citation validation unavailable | `ABSTAIN` or `HOLD` for answer-bearing output. |
| Schema authority conflict | `HOLD`. |

[Back to top](#top)

---

<a id="governed-ai-validation-invariants"></a>

## Governed-AI validation invariants

1. **Evidence outranks generation.**

   ```text
   EvidenceRef -> EvidenceBundle -> admissibility/policy -> bounded context -> model
   ```

2. **Policy surrounds model use.**

   ```text
   policy precheck -> model boundary -> policy postcheck
   ```

3. **Context is released or review-authorized.** RAW, WORK, QUARANTINE, unreleased candidates, private source bytes, secrets, and unauthorized sensitive geometry are denied.

4. **Adapters are provider-neutral.** Default validator tests do not require provider APIs, tokens, or network access.

5. **Runtime outcomes are finite.**

   ```text
   ANSWER | ABSTAIN | DENY | ERROR
   ```

6. **Validator results are separate.** Validator `PASS` is not runtime `ANSWER`.

7. **Citations close before answer posture.** Report presence alone is insufficient.

8. **Receipts are accountability, not truth.**

9. **No private chain-of-thought retention.** Audit uses IDs, refs, hashes, stages, versions, finite outcomes, and safe reasons.

10. **Corrections propagate.** Evidence, policy, rights, citation, release, model/profile, and schema changes can invalidate prior answers.

11. **Public clients remain downstream.** Browser, map, Focus Mode, export, and report surfaces use governed interfaces.

[Back to top](#top)

---

<a id="validation-report-contract"></a>

## Validation report contract

A future parent should consume an immutable packet containing, as applicable:

- validation/profile identity and version;
- subject ref/type/digest;
- requested surface, audience, and outcome;
- stage ledger;
- request contract/schema;
- policy precheck;
- EvidenceRefs and admitted EvidenceBundles;
- bounded context manifest/digest;
- adapter/model ref;
- citation validation;
- policy postcheck;
- DecisionEnvelope;
- AIReceipt/RunReceipt;
- RuntimeResponseEnvelope;
- release/correction/rollback refs;
- sensitivity/rights context;
- offline flag and resource limits.

A report should contain:

- report/profile identity;
- subject identity/digest;
- child/dependency report refs;
- ordered findings;
- finite validator outcome;
- reason codes;
- blocking state and obligations;
- evidence/policy/schema/receipt/release refs;
- checks run/skipped;
- limitations;
- spec/profile hash;
- explicit non-authority statement.

Report instances do not belong under `tools/validators/ai/`. Use an accepted QA/receipt destination such as `artifacts/qa/` or `data/receipts/validation/` after governance resolves the exact contract.

[Back to top](#top)

---

<a id="finite-validator-outcomes"></a>

## Finite validator outcomes

| Outcome | Meaning |
|---|---|
| `AI_VALIDATORS_PASS` | Required configured checks passed for the declared scope. |
| `AI_VALIDATORS_FAIL` | One or more required checks failed. |
| `AI_VALIDATORS_HOLD` | Required implementation, review, schema disposition, policy, or closure is pending. |
| `AI_VALIDATORS_ABSTAIN` | Parent cannot decide safely from available governed inputs. |
| `AI_VALIDATORS_DENY` | Requested operation is disallowed by validated policy/rights/sensitivity posture. |
| `AI_VALIDATORS_ERROR` | Validation could not complete safely. |

Rules:

- `PASS` does not imply `ANSWER`.
- `FAIL` is not silently converted to `ABSTAIN`.
- `ERROR` is not silently converted to `PASS`.
- `HOLD` blocks required promotion/public use.
- `DENY` requires policy/rights/sensitivity basis; validators do not invent policy.
- Unknown outcomes fail closed.
- Every outcome carries safe reason codes.

Key reason-code families include:

```text
AI_PARENT_RUNNER_UNIMPLEMENTED
AI_CHILD_UNIMPLEMENTED
AI_VALIDATOR_PLACEMENT_CONFLICT
AI_RECEIPT_VALIDATOR_STUB
AI_SCHEMA_AUTHORITY_CONFLICT
AI_POLICY_HOME_UNRESOLVED
EVIDENCE_REF_UNRESOLVED
EVIDENCE_BUNDLE_INCOMPLETE
POLICY_PRECHECK_MISSING
MODEL_BEFORE_CONTEXT_ADMISSION
CITATION_VALIDATION_MISSING
POLICY_POSTCHECK_MISSING
RECEIPT_LINKAGE_MISSING
PRIVATE_COT_PERSISTED
PROMPT_INJECTION_SIGNAL
SENSITIVE_CONTEXT_LEAK
PUBLIC_BOUNDARY_VIOLATION
ROLLBACK_TARGET_MISSING
```

[Back to top](#top)

---

<a id="contract-schema-and-fixture-maturity"></a>

## Contract, schema, and fixture maturity

| Object/family | Meaning | Shape | Fixtures/tests | Validator posture |
|---|---|---|---|---|
| `AIReceipt` | Runtime contract, draft/PROPOSED | Strict runtime schema; permissive AI-family duplicate conflict | Valid/invalid JSON fixtures; generic discovery confirmed | Dedicated validator stub; generic schema tests can exercise runtime shape. |
| `RuntimeResponseEnvelope` | Runtime contract, draft/PROPOSED | Strict runtime schema | Fixtures and working wrapper | Shape only, not stage order. |
| `DecisionEnvelope` | Runtime contract, draft/PROPOSED | Strict paired schema | Fixtures and working wrapper | Shape only, not policy correctness. |
| `EvidenceRef` | Evidence pointer contract | Paired schema | Shared family fixtures | Pointer is not closure. |
| `EvidenceBundle` | Evidence closure contract | Paired schema | Shared fixtures/wrapper | Shape is not truth/policy/release. |
| `CitationValidationReport` | Detailed semantic contract | Permissive empty-property scaffold | Behavior unverified | Substantive validation not established. |
| Focus request/response | AI child READMEs plus older Focus surfaces | Multiple proposed families | Dedicated AI tests absent | Canonical topology unresolved. |
| Model adapter | Descriptive runtime note and proposed ADR | Canonical adapter schema absent at checked path | Mock/runtime tests unverified | Docs lane confirmed; implementation mixed. |

### AIReceipt authority conflict

```text
schemas/contracts/v1/runtime/ai_receipt.schema.json   # strict, paired, fixtures
schemas/contracts/v1/ai/ai_receipt.schema.json       # permissive scaffold
```

The runtime schema requires nine fields, closes properties, and has fixtures. The AI-family scaffold has no declared properties, allows extras, and has no contract-doc pointer.

The AI schema README says the lane is compatibility/index only.

Until disposition is governed:

- treat the strict runtime schema as the stronger implementation candidate;
- mark canonical authority `NEEDS VERIFICATION`;
- fail/hold on ambiguous schema selection;
- require migration/deprecation for the losing path;
- prevent duplicate active object-family authority in tests.

A schema pass still cannot prove ref resolution, policy execution, stage order, citation support, receipt persistence, release state, correction state, or truth.

[Back to top](#top)

---

<a id="policy-routing-and-drift"></a>

## Policy routing and drift

| Path | State | Parent interpretation |
|---|---|---|
| `policy/ai/` | README absent | Not an implemented policy home. |
| `policy/focus/README.md` | Five-line greenfield stub | Candidate Focus policy lane only. |
| `policy/runtime/README.md` | Five-line greenfield stub | Candidate runtime policy lane only. |
| `policy/ai_builder/README.md` | Detailed repository-authoring policy | Separate bounded context; explicitly excludes public user answer generation. |
| ADR-0019 | Proposed/draft | Does not authorize runtime or settle policy. |

The parent may validate policy ref presence, version, order, finite decision, obligations, audience/surface alignment, and consistency with runtime outcome.

It must not:

- invent policy rules;
- call AI-builder policy for public runtime answers merely because it exists;
- infer policy from a folder;
- treat missing policy as allow;
- expose hidden policy parameters;
- emit PolicyDecision authority.

Before activation, governance must settle runtime/Focus policy ownership, entrypoints, input contract, decision vocabulary, obligations, public-safe reasons, receipt/envelope binding, tests, and rollback.

[Back to top](#top)

---

<a id="runtime-adapter-and-public-boundary"></a>

## Runtime adapter and public boundary

`runtime/model_adapters/` is the confirmed canonical provider-neutral adapter documentation/handoff lane.

Validators may check:

- adapter/mode/model identity and version;
- input/output contract refs;
- network/tool posture;
- bounded-context digest;
- finite output envelope;
- receipt/policy/evidence refs;
- correction/rollback state.

Validators must not implement adapters, store credentials, approve providers/models, make network calls in default tests, expose provider response objects, or allow provider-specific bypasses.

```text
browser / map / Focus Mode / export
  -> governed API
  -> policy + evidence + release adapters
  -> provider-neutral model adapter when allowed
  -> citation + post-policy checks
  -> receipts + RuntimeResponseEnvelope
  -> client-safe rendering
```

Forbidden:

```text
browser -> model
UI -> canonical/internal store
validator -> public answer
model output -> EvidenceBundle
AIReceipt -> release approval
```

[Back to top](#top)

---

<a id="security-privacy-and-prompt-injection"></a>

## Security, privacy, and prompt injection

All retrieved documents, webpages, PDFs, OCR, comments, uploads, map attributes, database values, and generated text are data—not instructions or authority.

Flag content attempting to:

- override system/policy rules;
- grant permissions;
- request secrets;
- redirect tools;
- suppress citations;
- bypass evidence/release gates;
- reveal hidden reasoning;
- alter sensitivity;
- select an unapproved provider/model.

Most-restrictive posture wins for living-person data, DNA, private parcels/operators, rare species, archaeology/cultural resources, sovereignty-sensitive material, infrastructure, restricted records, and precise coordinates.

Logs should prefer IDs, refs, hashes, counts, stage names, versions, finite outcomes, and redacted field paths.

Avoid raw prompts, full outputs, restricted evidence, exact coordinates, personal identifiers, policy secrets, credentials, and chain-of-thought.

A mature profile must bound request/context bytes, ref/bundle/citation counts, nesting depth, retry count, tool calls, timeout, report size, logs, and concurrency.

[Back to top](#top)

---

<a id="lifecycle-release-correction-and-rollback"></a>

## Lifecycle, release, correction, and rollback

Preserve:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Rules:

- RAW/WORK/QUARANTINE do not become public AI context.
- Processed/cataloged does not mean published.
- Models and validators cannot promote lifecycle state.
- Receipts cannot promote lifecycle state.
- Public-bound output may require release, policy, evidence, citation, receipt, freshness, correction, and rollback refs.

Revalidate when evidence, rights, sensitivity, citation, policy, model/adapter, prompt/profile, schema/contract, release, or correction state changes.

Affected answers should be discoverable, supersedable, withdrawable, or rollback-aware. Prior receipts remain auditable; history is not silently mutated.

[Back to top](#top)

---

<a id="tests-fixtures-and-ci"></a>

## Tests, fixtures, and CI

### Confirmed

- Strict runtime AIReceipt schema exists.
- Valid and invalid AIReceipt JSON fixtures exist.
- Generic schema discovery includes runtime families with matching fixture directories.
- `contracts-validate` runs `make test`.
- RuntimeResponseEnvelope, DecisionEnvelope, and EvidenceBundle wrappers exist.

### Not established

- dedicated `tests/validators/ai/`;
- parent AI runner;
- evidence-before-model implementation;
- dedicated AIReceipt validator;
- end-to-end ordering tests;
- runtime AI policy tests;
- prompt-injection/privacy/correction AI validator suite;
- release-gate adoption.

### Required test families

- parent routing and deterministic aggregation;
- missing/duplicate child;
- valid answer/deny/abstain/error flows;
- unresolved/incomplete evidence;
- model-before-evidence;
- missing pre/post policy;
- missing/failed citation validation;
- AIReceipt valid/invalid/inconsistent refs;
- strict-versus-permissive schema selection;
- prompt injection;
- secret/sensitive location leakage;
- oversized context/resource abuse;
- no-network provider bypass;
- evidence/policy/citation correction;
- release withdrawal and rollback.

Proposed layout:

```text
tests/validators/ai/
├── README.md
├── test_parent_router.py
├── test_ai_receipt_integration.py
├── test_runtime_envelope_integration.py
├── test_policy_routing.py
├── test_security_and_redaction.py
├── test_correction_and_rollback.py
└── evidence_before_model/
    └── test_evidence_before_model.py
```

This layout is `PROPOSED`.

Substantive CI should run no-network tests, strict fixtures, duplicate-authority checks, stub detection, security negatives, deterministic repeats, report validation, and public-safe log checks. It remains separate from release approval.

[Back to top](#top)

---

<a id="smallest-sound-implementation-sequence"></a>

## Smallest sound implementation sequence

1. **Resolve topology**
   - Select evidence-before-model implementation path.
   - Preserve one active implementation.
   - Record migration/deprecation.

2. **Resolve schema authority**
   - Designate strict runtime AIReceipt schema or accepted successor.
   - Deprecate/remove/convert permissive duplicate.
   - Add duplicate-authority tests.

3. **Resolve policy ownership**
   - Select runtime/Focus policy homes and entrypoints.
   - Keep AI-builder policy separate.
   - Add fail-closed tests.

4. **Realize report contracts**
   - Ratify parent/child ValidationReport.
   - Realize substantive CitationValidationReport schema.
   - Define reason-code registry and destinations.

5. **Implement validators**
   - Replace AIReceipt stub.
   - Implement evidence-before-model without model calls.
   - Reuse `_common`.
   - Add direct tests.

6. **Implement parent router**
   - Child registry/config;
   - version/dependency checks;
   - deterministic aggregation;
   - structured report;
   - bounded side effects.

7. **Add security/correction proof**
   - prompt injection, privacy, redaction, limits, correction, withdrawal, rollback.

8. **Admit CI**
   - no-network, schema, behavior, artifact, duplicate-authority, stub, and determinism checks.

9. **Adopt runtime/release only after evidence**
   - runtime invokes profile;
   - reports/receipts resolve;
   - clients honor envelopes;
   - correction and rollback work;
   - release gate references reviewed validation.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

- [ ] Owners and CODEOWNERS are confirmed.
- [ ] Parent/child topology is resolved.
- [ ] One active implementation exists per concern.
- [ ] AIReceipt schema conflict is resolved.
- [ ] Runtime AI policy home/entrypoints are accepted.
- [ ] Parent and child input/report contracts are accepted.
- [ ] CitationValidationReport schema is substantive.
- [ ] AIReceipt validator no longer raises `NotImplementedError`.
- [ ] Evidence-before-model validator is implemented.
- [ ] Parent runner is deterministic.
- [ ] No validator calls a model or writes outside accepted destinations.
- [ ] Dedicated AI tests and no-network fixtures exist.
- [ ] Prompt-injection, privacy, duplicate-schema, correction, and rollback tests pass.
- [ ] CI runs the substantive suite.
- [ ] Current pass evidence is available.
- [ ] Adapter profile, policy, evidence resolver, citation validator, receipts, and client envelopes are operational.
- [ ] Release-gate adoption is reviewed.
- [ ] Monitoring, incident response, correction, and rollback are operational.

[Back to top](#top)

---

<a id="migration-compatibility-and-deprecation"></a>

## Migration, compatibility, and deprecation

Confirmed drift:

1. child evidence-before-model contract versus parent-level placeholder;
2. strict runtime AIReceipt schema versus permissive AI-family scaffold;
3. docs referencing absent `policy/ai/`;
4. Focus/runtime policy stubs versus detailed AI-builder policy for another bounded context;
5. generic AIReceipt schema fixture coverage versus dedicated validator stub.

Any move, consolidation, activation, or deprecation requires:

- current/target paths and root basis;
- canonical owner;
- contract/schema/profile versions;
- compatibility behavior;
- fixture/test/CI parity;
- report/receipt destination;
- migration window and deprecation notice;
- correction impact;
- rollback target;
- ADR/migration note where required.

A shim must delegate to one implementation, add no semantic/policy logic, preserve outcomes, be tested, warn when appropriate, and have a removal condition.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| ID | Question | Status |
|---|---|---|
| AI-V-001 | Which path owns evidence-before-model implementation? | **NEEDS VERIFICATION** |
| AI-V-002 | Is a parent runner required and what is its CLI/API? | **UNKNOWN** |
| AI-V-003 | Which AIReceipt schema is canonical? | **NEEDS VERIFICATION** |
| AI-V-004 | How is the permissive duplicate retired/converted? | **NEEDS VERIFICATION** |
| AI-V-005 | Which runtime AI policy root/entrypoints are authoritative? | **UNKNOWN** |
| AI-V-006 | How do Focus and runtime policy relate? | **UNKNOWN** |
| AI-V-007 | Why is `policy/ai/` referenced but absent? | **NEEDS VERIFICATION** |
| AI-V-008 | What resolver/admission contract governs EvidenceRef/EvidenceBundle? | **UNKNOWN** |
| AI-V-009 | What substantive schema governs CitationValidationReport? | **NEEDS VERIFICATION** |
| AI-V-010 | What parent report schema/destination are accepted? | **UNKNOWN** |
| AI-V-011 | Which reason-code registry is authoritative? | **UNKNOWN** |
| AI-V-012 | Which canonicalization/digest standard applies? | **NEEDS VERIFICATION** |
| AI-V-013 | Which AI tests/CI checks are branch-protection significant? | **UNKNOWN** |
| AI-V-014 | Does current contracts-validate pass on this branch? | **NEEDS VERIFICATION** |
| AI-V-015 | Which runtime surfaces invoke AI validators today? | **UNKNOWN** |
| AI-V-016 | Are AIReceipt instances persisted/resolvable? | **UNKNOWN** |
| AI-V-017 | Are provider/model admission records implemented? | **UNKNOWN** |
| AI-V-018 | What resource limits apply? | **NEEDS VERIFICATION** |
| AI-V-019 | Which sensitive-domain reviewers apply? | **NEEDS VERIFICATION** |
| AI-V-020 | How are injection findings represented safely? | **NEEDS VERIFICATION** |
| AI-V-021 | How are retries/replays/superseding runs linked? | **UNKNOWN** |
| AI-V-022 | How do corrections invalidate prior answers? | **UNKNOWN** |
| AI-V-023 | What killswitch forces safe abstention/denial? | **UNKNOWN** |
| AI-V-024 | What rollback drill restores last safe profile? | **UNKNOWN** |
| AI-V-025 | Do clients reject unknown outcomes/raw model output? | **UNKNOWN** |
| AI-V-026 | When is ADR-0019 accepted, superseded, or retired? | **NEEDS VERIFICATION** |

[Back to top](#top)

---

<a id="rollback-path"></a>

## Rollback path

For this documentation-only revision:

1. revert the README commit;
2. restore prior blob `829589614cff7aec864e3d5802fcc693dc30d3a5`;
3. revert/remove the generated receipt;
4. rerun Markdown/link/receipt checks;
5. confirm no runtime, validator, policy, schema, fixture, or release state changed.

Future implementation rollback should support disabling parent/child profiles, restoring prior schema/policy/profile digests, forcing safe abstention/denial, revoking adapter/model profiles, invalidating affected caches, marking responses stale/withdrawn, and restoring last known safe public state.

Rollback must never re-enable direct browser-to-model access, expose internal stores, erase receipts, hide corrections, accept unknown evidence, silently change policy, drop sensitivity/rights obligations, or publish raw output.

[Back to top](#top)

---

<a id="evidence-ledger"></a>

## Evidence ledger

| Evidence | Supports | Limit |
|---|---|---|
| Prior parent README | Existing parent intent | Understated implementation and drift. |
| Revised child README | Evidence-before-model contract/status | Earlier bounded absence claims became stale under broader search. |
| Evidence-before-model placeholder | Named path exists | No behavior. |
| AIReceipt validator | Dedicated path exists | Stub only. |
| Shared wrappers | Runtime/evidence shape mechanics | Not behavioral proof. |
| Strict runtime AIReceipt schema | Required shape/outcomes | PROPOSED status; runtime refs/persistence unverified. |
| Permissive AI-family schema | Duplicate scaffold conflict | Not safe as coequal authority. |
| AIReceipt JSON fixtures | Valid/invalid payloads | Not dedicated runtime proof. |
| Generic test harness | Runtime fixture discovery | Current result not claimed. |
| Contracts workflow | `make test` CI wiring | Not dedicated AI behavior/release gate. |
| Focus Flow | Stage order and finite outcomes | Implementation proposed. |
| Citation report contract | Detailed semantic intent | Schema permissive. |
| AI contracts index | Contract compatibility drift | Canonical topology unresolved. |
| AI schema index | Compatibility-only guidance | Conflicts with actual duplicate file. |
| Model-adapter README | Canonical runtime docs/handoff | Executable/provider maturity unknown. |
| AI-builder policy | Repository-authoring policy | Not runtime answer policy. |
| Focus/runtime policy READMEs | Candidate paths | Stubs only. |
| ADR-0019 | Proposed adapter/envelope decision | Not accepted. |
| Directory Rules | Responsibility placement | No implementation proof. |

[Back to top](#top)

---

<a id="changelog"></a>

## Changelog

### v0.2 — 2026-07-16

- Replaced the generic proposed guide with a repository-grounded parent routing and compatibility boundary.
- Confirmed direct parent inventory and one README-only child.
- Recorded evidence-before-model placeholder and AIReceipt `NotImplementedError` stub.
- Confirmed strict runtime AIReceipt schema, JSON fixtures, generic schema discovery, and contracts workflow.
- Corrected the stale assumption that AIReceipt validator/fixtures were absent.
- Surfaced strict runtime versus permissive AI-family AIReceipt schema conflict.
- Distinguished runtime/Focus policy from AI-builder repository policy.
- Added routing, child admission, dependency, report, outcome, security, privacy, lifecycle, testing, CI, implementation, migration, rollback, and verification contracts.
- Preserved AI as interpretive and non-authoritative.

### v0.1 — 2026-07-07

- Replaced an empty file with a proposed parent guide.
- Documented one child lane and broad governed-AI expectations.
- Did not verify executable, fixture, policy, test, or CI maturity.

[Back to top](#top)
