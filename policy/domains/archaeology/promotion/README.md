<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://policy/domains/archaeology/promotion
title: Archaeology Promotion Policy README
type: readme; directory-readme; domain-policy-sublane; governed-promotion-boundary; sensitive-domain
version: v0.2
status: draft; repository-grounded; README-only-direct-lane; shared-shape-validation-confirmed; archaeology-enforcement-unestablished; fail-closed; non-authoritative-for-release
owners: OWNER_TBD — Archaeology steward · Promotion steward · Policy steward · Sensitivity reviewer · Cultural/sovereignty reviewer · Rights-holder representative · Evidence steward · Contract/schema steward · Validator/test steward · Release authority · Correction/rollback steward · Security reviewer · Docs steward
created: 2026-06-15
updated: 2026-07-19
supersedes: v0.1 Archaeology promotion policy guide
policy_label: restricted-review; policy; archaeology; promotion; sensitive-domain; evidence-bound; review-gated; rollback-required; no-public-authority
current_path: policy/domains/archaeology/promotion/README.md
owning_root: policy/
responsibility: >
  Archaeology-specific promotion-policy boundary for governed lifecycle transitions. It records
  current repository maturity, separates shared PromotionDecision shape validation from
  Archaeology-specific policy enforcement, defines the gate inputs, finite decisions, obligations,
  cultural/sensitivity overlays, public-surface restrictions, tests, review duties, and rollback
  requirements without promoting data, approving release, storing protected material, or claiming
  that documentation, schemas, fixtures, validators, or workflow holds equal runtime enforcement.
truth_posture: >
  CONFIRMED target v0.1 README and direct-lane path; bounded search surfaced only this README under
  policy/domains/archaeology/promotion; parent Archaeology policy, sensitivity, review, publication,
  runbook, release-candidate, fixture, validator, proof, and workflow documentation exists; shared
  PromotionDecision semantic contract, paired PROPOSED schema, validator entry point, non-vacuous
  valid/invalid fixture requirement, executable schema test, and promotion-gate CI shape check exist;
  shared promotion prerequisite and rollback-card Rego files are fourteen-line PROPOSED stubs with
  default deny false; domain-archaeology CI is an explicit readiness hold; release/candidates/
  archaeology contains no child dossier in bounded evidence; broad Archaeology validator lanes are
  README-only; policy runtime/evaluator and Archaeology-specific promotion policy execution are not
  established /
  PROPOSED bounded gate model, Archaeology overlay requirements, policy-input packet, reason-code and
  obligation families, decision normalization, anti-leak controls, validation matrix, reviewer
  separation, correction handling, and reversible implementation sequence /
  CONFLICTED promotion doctrine and v0.1 vocabulary using ALLOW/RESTRICT/HOLD versus the shared
  PromotionDecision schema's APPROVE/DENY/ABSTAIN enum and runtime PolicyDecision's
  ANSWER/ABSTAIN/DENY/ERROR enum; doctrine flow names PromotionReceipt while checked contract/schema
  paths are absent; shared PromotionDecision schema is concrete but PROPOSED, has a hydrology-only id
  conditional, and does not itself require Archaeology-specific redaction, cultural review,
  sovereignty, consent, or exact-location controls; shared promotion policy stubs default deny false
  despite fail-closed doctrine /
  UNKNOWN accepted Archaeology promotion bundle, evaluator, selector, bundle digest, policy input
  schema, executable domain policy tests, PromotionReceipt authority, emitted Archaeology
  PromotionDecision records, actual ReviewRecords, candidate dossier, proof producer, release dry-run,
  production consumers, branch-protection significance, monitoring, and release adoption /
  NEEDS VERIFICATION owners and CODEOWNERS, canonical gate identifiers, exact policy/receipt homes,
  Archaeology decision-id convention, source and rights authority, cultural/sovereignty review
  protocol implementation, named redaction profiles and thresholds, evidence closure, deterministic
  domain fixtures, no-network tests, public API/UI/map/AI obligation handling, correction cascade,
  cache invalidation, withdrawal, rollback drill, and independent release review.
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: f73caa6dece3a4459b1298dc9b105256fb1f67d5
  prior_blob: 3dd85efb1134fc310b5191efde04dec086eb2b05
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  parent_archaeology_policy_blob: 8d03cdb11361739e7ad33214f76a0cfe4836ff9b
  archaeology_promotion_runbook_blob: 1be7cf86cf928116435c775ad9b1815f9b199af0
  archaeology_publication_policy_blob: 835bd3afb1b6a41de8f598d16b794873df0b6f75
  archaeology_sensitivity_blob: ca7888f2d43f022faeef5e1a6e16ab00526cf7aa
  promotion_decision_contract_blob: 42295bfc83a621cf125d33aa821912b426f70bd2
  promotion_decision_schema_blob: a2d087a46772cf60e4b9dfb394892690e8a88b31
  promotion_decision_validator_blob: ead33d6c5c073f319627ee42d99c5933c0e370d1
  promotion_decision_test_blob: 495c76aa9d3a016b7a60831e47c15d3a21efaa0c
  promotion_fixture_readme_blob: 184c40ee4345b482df7a6f17c65e354e09114c7a
  archaeology_test_local_promotion_fixture_blob: e16733aa226e5eb24f09225e64bc920cbb0b32a3
  promotion_prerequisites_policy_blob: 782b24af3c0fe28871a58da202a3efdbd5991647
  rollback_card_required_policy_blob: b2eb37b31b572e1d97d1afbe4babe8200f87df7d
  promotion_gate_workflow_blob: feb8bef88c197bc27a4ed1aa692f72b86f7a9a1f
  domain_archaeology_workflow_blob: 41e377f50ca310eccdc4b716ba8374c4fa8181db
  archaeology_release_candidate_readme_blob: bc5edc7a44ea77a6b8ed25b95569646d8df72754
  archaeology_validator_readme_blob: bae2eabb5d29bf7099ed74a66a17c0071ae98557
related:
  - ../README.md
  - ../../README.md
  - ../../../../docs/runbooks/archaeology/PROMOTION_RUNBOOK.md
  - ../../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md
  - ../../../../docs/domains/archaeology/SENSITIVITY.md
  - ../../../../docs/domains/archaeology/CULTURAL_REVIEW.md
  - ../../../../docs/domains/archaeology/PIPELINE.md
  - ../../../../docs/domains/archaeology/PRESERVATION_MATRIX.md
  - ../../../../docs/domains/archaeology/RELEASE_INDEX.md
  - ../review/README.md
  - ../sensitivity/README.md
  - ../../../promotion/promotion_prerequisites.rego
  - ../../../promotion/rollback_card_required.rego
  - ../../../../contracts/release/promotion_decision.md
  - ../../../../contracts/release/release_manifest.md
  - ../../../../contracts/release/rollback_card.md
  - ../../../../contracts/governance/review_record.md
  - ../../../../contracts/evidence/evidence_bundle.md
  - ../../../../schemas/contracts/v1/release/promotion_decision.schema.json
  - ../../../../fixtures/release/promotion_decision/README.md
  - ../../../../tests/release/test_promotion_decision_schema.py
  - ../../../../tools/validators/release/validate_promotion_decision.py
  - ../../../../tests/fixtures/domains/archaeology/promotion/README.md
  - ../../../../fixtures/domains/archaeology/README.md
  - ../../../../tools/validators/archaeology/README.md
  - ../../../../data/proofs/archaeology/README.md
  - ../../../../release/candidates/archaeology/README.md
  - ../../../../data/published/archaeology/README.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/doctrine/ai-build-operating-contract.md
  - ../../../../.github/workflows/promotion-gate.yml
  - ../../../../.github/workflows/domain-archaeology.yml
tags:
  - kfm
  - policy
  - archaeology
  - promotion
  - governed-state-transition
  - sensitive-domain
  - exact-location-deny
  - candidate-not-site
  - evidence-bundle
  - cultural-review
  - sovereignty
  - rights
  - redaction
  - promotion-decision
  - release-manifest
  - rollback-card
  - finite-outcomes
  - no-network
  - release-gated
  - correction
  - rollback
notes:
  - "This revision changes only policy/domains/archaeology/promotion/README.md plus the required AI-generated provenance receipt."
  - "No Rego/YAML rule, policy value, schema, contract, fixture payload, test, validator, workflow, protected record, evidence object, review record, candidate dossier, receipt/proof instance, release artifact, deployment, public route, map layer, or AI behavior is created or modified."
  - "Shared PromotionDecision shape validation is confirmed; Archaeology promotion enforcement, cultural authority, evidence closure, candidate approval, release, and publication are not."
  - "Promotion is a governed state transition, not a file move, merge, workflow result, directory presence, or generated summary."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `policy/domains/archaeology/promotion/` — Archaeology Promotion Policy Boundary

> **One-line purpose.** Define the fail-closed Archaeology policy boundary for deciding whether a specific governed artifact may cross a lifecycle gate while preserving exact-location denial, candidate-versus-site separation, evidence closure, cultural and sovereignty review, rights, redaction, separation of duties, correction, and rollback.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Version: v0.2" src="https://img.shields.io/badge/version-v0.2-informational">
  <img alt="Root: policy" src="https://img.shields.io/badge/root-policy%2F-blue">
  <img alt="Domain: archaeology" src="https://img.shields.io/badge/domain-archaeology-6E4C1E">
  <img alt="Direct lane: README only" src="https://img.shields.io/badge/direct__lane-README__only-lightgrey">
  <img alt="Shared shape checks: present" src="https://img.shields.io/badge/shared__shape__checks-present-success">
  <img alt="Domain enforcement: unestablished" src="https://img.shields.io/badge/domain__enforcement-unestablished-critical">
  <img alt="Default: hold or deny" src="https://img.shields.io/badge/default-HOLD__or__DENY-critical">
</p>

> [!IMPORTANT]
> **Shape validation is not promotion enforcement.** The repository has a concrete `PromotionDecision` schema, validator entry point, synthetic fixtures, a pytest wrapper, and a CI job that requires nonempty valid/invalid fixture sets. Those checks prove the selected machine shape only. They do not resolve Archaeology evidence, run promotion policy, validate cultural authority, approve a candidate, emit a release manifest, or publish.

> [!CAUTION]
> **Archaeology remains deny-by-default.** Exact or reverse-engineerable site locations, burials, human remains, sacred or culturally restricted material, collection-security detail, private-landowner information, looting-risk information, protected oral history, sovereignty-bearing knowledge, and sensitive review substance must not cross a gate merely because a schema, fixture, workflow, or README passes.

> [!WARNING]
> **The shared promotion policy stubs are not safe runtime rules.** `promotion_prerequisites.rego` and `rollback_card_required.rego` are marked `PROPOSED` and default `deny := false`; their substantive rules are comments. Do not activate or cite them as fail-closed enforcement until an accepted bundle, input contract, negative tests, evaluator, and parity proof exist.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status-and-repository-evidence) · [Belongs](#what-belongs-here) · [Does not](#what-does-not-belong-here) · [Lifecycle](#governed-lifecycle-and-gates) · [Inventory](#confirmed-promotion-surface) · [Inputs](#minimum-promotion-policy-input) · [Decisions](#decision-vocabularies-and-normalization) · [Artifacts](#gate-artifact-matrix) · [Sensitivity](#archaeology-sensitive-domain-overlays) · [Candidate boundary](#candidate-versus-confirmed-site-boundary) · [Review](#review-and-separation-of-duties) · [Public surfaces](#public-surface-and-trust-membrane) · [Validation](#validation-tests-and-ci) · [Threats](#threat-and-failure-model) · [Sequence](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Conflicts](#conflict-and-adr-register) · [Open](#open-verification-register) · [Rollback](#maintenance-correction-and-rollback) · [Evidence](#evidence-ledger) · [Changelog](#changelog)

---

## Purpose

`policy/domains/archaeology/promotion/` is the Archaeology-specific promotion-policy documentation sublane under KFM's canonical singular `policy/` responsibility root.

Its durable question is:

> Given an explicitly identified Archaeology artifact, lifecycle transition, audience, source, evidence, sensitivity, cultural-review, rights, validation, policy, release, correction, and rollback context, may the transition proceed—and which obligations must every downstream system preserve?

A complete implementation behind this README should answer:

1. Which artifact or candidate is being evaluated?
2. Which lifecycle state is current, and which state is requested?
3. Is the object a `CandidateFeature`, contextual signal, or confirmed archaeological assertion?
4. Are source identity, source role, rights, and authority explicit?
5. Do EvidenceRefs resolve to the required EvidenceBundle or proof support?
6. Are exact and reverse-engineerable geometry risks evaluated?
7. Are cultural, sovereignty, consent, embargo, revocation, and rights-holder constraints resolved?
8. Is the required named redaction/generalization profile applied and receipt-backed?
9. Are validation reports, review records, policy decisions, and release records complete?
10. Are author, sensitivity reviewer, rights-holder representative, cultural reviewer, and release authority separated where required?
11. Is the rollback target real, resolvable, and tested?
12. Can public APIs, maps, exports, search, graphs, screenshots, embeddings, and AI answers preserve all resulting obligations?
13. Can the decision be reproduced from a pinned policy bundle and deterministic no-network fixtures?
14. Does every unresolved or unsafe state preserve the prior lifecycle state?
15. Does correction, withdrawal, supersession, or rollback remain possible after promotion?

### Scope

This lane may document or eventually host accepted Archaeology-specific promotion policy for:

- admission and source-role prerequisites;
- RAW to WORK or QUARANTINE routing;
- WORK to PROCESSED validation closure;
- PROCESSED to CATALOG/TRIPLET evidence and catalog closure;
- CATALOG/TRIPLET to release-candidate admission;
- release-candidate to PUBLISHED readiness;
- PUBLISHED correction, withdrawal, supersession, and rollback;
- exact-location and reverse-inference denial;
- candidate-versus-confirmed-site anti-collapse;
- cultural, sovereignty, CARE, consent, rights-holder, and embargo review;
- named redaction, generalization, aggregation, suppression, and delayed-release obligations;
- PolicyDecision and PromotionDecision normalization;
- reason codes, obligations, audit metadata, and safe public summaries;
- policy parity between CI and runtime;
- deterministic negative tests and no-network fixtures;
- public trust-membrane and bypass tests.

This lane does **not** establish that any Archaeology artifact is accurate, culturally authorized, rights-cleared, evidence-closed, safe, approved, released, public, or suitable for field, enforcement, preservation, land-use, or operational decisions.

[Back to top](#top)

---

## Authority level

**Canonical policy responsibility for an accepted Archaeology promotion rule set; non-authoritative for every adjacent concern.**

Directory Rules place admissibility under `policy/`, object meaning under `contracts/`, machine shape under `schemas/`, operational steps under `docs/runbooks/`, lifecycle artifacts under `data/`, enforceability under `tests/` and validators, and release decisions under `release/`.

| Concern | Authority home | This lane's role |
|---|---|---|
| Archaeology promotion policy | Accepted sources under `policy/` | May own domain-specific promotion admissibility after acceptance. |
| Cross-domain promotion policy | [`policy/promotion/`](../../../promotion/) | Supplies shared prerequisites and rollback requirements after real implementation. |
| Archaeology policy parent | [`policy/domains/archaeology/`](../README.md) | Supplies domain-wide deny-by-default obligations. |
| Archaeology sensitivity policy | [`policy/domains/archaeology/sensitivity/`](../sensitivity/README.md) and accepted cross-cutting sensitivity lane | Promotion consumes sensitivity decisions; does not redefine sensitivity doctrine. |
| Archaeology review policy | [`policy/domains/archaeology/review/`](../review/README.md) | Promotion consumes review state; cannot invent cultural authority. |
| Human-facing procedure | [`docs/runbooks/archaeology/PROMOTION_RUNBOOK.md`](../../../../docs/runbooks/archaeology/PROMOTION_RUNBOOK.md) | Explains how to operate; not policy code. |
| Domain publication doctrine | [`PUBLICATION_AND_POLICY.md`](../../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md) | Supplies policy intent and trust-membrane rules. |
| Sensitivity doctrine | [`SENSITIVITY.md`](../../../../docs/domains/archaeology/SENSITIVITY.md) | Owns the detailed sensitivity catalogue and transform expectations. |
| Cultural-review protocol | [`CULTURAL_REVIEW.md`](../../../../docs/domains/archaeology/CULTURAL_REVIEW.md) | Defines review procedure and authority relationships. |
| Archaeology object meaning | [`contracts/domains/archaeology/`](../../../../contracts/domains/archaeology/) | Promotion consumes meaning; does not redefine it. |
| PromotionDecision meaning | [`contracts/release/promotion_decision.md`](../../../../contracts/release/promotion_decision.md) | Defines the release-transition decision object. |
| Machine shape | [`schemas/contracts/v1/`](../../../../schemas/contracts/v1/) | Validates structures; schema validity is not permission. |
| PromotionDecision shape | [`promotion_decision.schema.json`](../../../../schemas/contracts/v1/release/promotion_decision.schema.json) | Shared cross-domain shape; Archaeology overlays remain policy/review obligations. |
| Source identity and rights | Governed source registries and review records | Promotion evaluates supplied facts; does not invent them. |
| Evidence and proof | EvidenceBundle/proof families | Promotion requires closure; cannot create proof authority. |
| Validation | `tools/validators/` and `tests/` | Proves declared behavior; validator success is not approval. |
| Test-local and reusable fixtures | `tests/fixtures/` and `fixtures/` according to documented scope | Supply synthetic inputs only. |
| Candidate dossiers | [`release/candidates/archaeology/`](../../../../release/candidates/archaeology/README.md) | Candidate review and blocker state; not release. |
| Promotion decisions, manifests, correction, rollback | `release/` | Own governed release records and state transitions. |
| Public API, UI, map, export, AI | Governed applications and released artifacts | Must preserve policy obligations; cannot choose policy ad hoc. |
| CI orchestration | `.github/workflows/` | Runs checks; a green hold or shape pass is not promotion. |

### Governing order

When Archaeology promotion sources conflict, apply the most restrictive result from:

1. KFM core invariants and operating law;
2. accepted ADRs and release-governance decisions;
3. sensitive-domain and sovereignty/rights rules;
4. Archaeology sensitivity and cultural-review doctrine;
5. accepted source-specific rights and authority records;
6. accepted contracts, schemas, policy bundle, reviewer records, and release records;
7. this README;
8. proposed scaffolds, examples, and planning documents.

A lower-ranked artifact must not weaken a denial, hold, review, redaction, evidence, correction, or rollback obligation from a higher-ranked source.

[Back to top](#top)

---

## Status and repository evidence

### Safe conclusion

At `main@f73caa6dece3a4459b1298dc9b105256fb1f67d5`:

- the direct `policy/domains/archaeology/promotion/` lane is README-only in bounded search;
- the parent Archaeology policy, sensitivity, and review documentation exists;
- the PromotionDecision semantic contract exists;
- the paired PromotionDecision schema is concrete but marked `PROPOSED`;
- a validator entry point delegates to the shared JSON Schema runner;
- an executable pytest test invokes that validator;
- the promotion-gate workflow requires nonempty valid and invalid PromotionDecision fixture sets and runs the test;
- that workflow explicitly holds real promotion because it does not resolve evidence, execute policy, verify bundle identity, enforce review separation, or validate rollback;
- the shared promotion Rego files remain proposed comment-only stubs with `default deny := false`;
- the Archaeology domain workflow reports explicit holds for validation, proof, and release dry run;
- the Archaeology release-candidate lane has no child candidate dossier in bounded evidence;
- the broad Archaeology validator lanes remain README-only;
- no Archaeology-specific promotion bundle, PromotionReceipt implementation, reviewed candidate, emitted PromotionDecision, release manifest, or published release is established.

### Maturity matrix

| Surface | Confirmed state | Safe conclusion |
|---|---|---|
| Target promotion README | Present, prior v0.1 | Documentation exists; v0.1 predates current shared promotion-gate evidence. |
| Direct promotion policy source | Not surfaced beyond README | Do not claim domain policy execution. |
| Parent Archaeology policy | Draft README | Domain obligations are documented; runtime remains unproved. |
| PromotionDecision contract | Draft v0.2 | Meaning is documented; it is not a release or PolicyDecision. |
| PromotionDecision schema | Concrete `PROPOSED` JSON Schema | Shape can be checked; Archaeology semantics and authority are not closed. |
| PromotionDecision validator | Executable wrapper around shared schema runner | Shape validation is available. |
| PromotionDecision pytest | Executable one-test wrapper | Selected fixture validation is callable. |
| PromotionDecision fixtures | CI requires nonempty valid/invalid JSON sets | Non-vacuous shape examples exist; they are synthetic. |
| Promotion-gate workflow | Substantive shape checks plus explicit holds | Real promotion remains blocked. |
| Shared promotion Rego | Two fourteen-line proposed stubs; `default deny := false` | No fail-closed policy enforcement. |
| Test-local Archaeology promotion fixture lane | README-only direct lane in its pinned research | Routing contract exists; no direct payload/test implementation established there. |
| Archaeology validator lanes | README-only in bounded evidence | No domain validator command is established. |
| Domain Archaeology workflow | Explicit readiness holds | No domain validation, proof production, promotion, or release. |
| Candidate lane | Parent README only in bounded evidence | No reviewed Archaeology candidate dossier established. |
| Review record state | Shared workflow holds on minimal release-review inventory | No Archaeology review record is established by that workflow evidence. |
| PromotionReceipt | Named in doctrine; checked contract/schema paths absent in fixture research | Contract, schema, validator, and storage authority remain unresolved. |
| Release/published state | No candidate, manifest, or published release established | Public transition remains denied/held. |

### Authoring truth labels

| Label | Use in this README |
|---|---|
| `CONFIRMED` | Verified from current repository files, schemas, tests, workflows, or pinned artifacts. |
| `PROPOSED` | A policy, profile, reason code, obligation, path, or implementation design not accepted as runtime authority. |
| `CONFLICTED` | Repository or doctrine surfaces disagree and no accepted decision resolves them. |
| `UNKNOWN` | Not resolved strongly enough in this task. |
| `NEEDS VERIFICATION` | Checkable, but not yet proven sufficiently for action. |

[Back to top](#top)

---

## What belongs here

After policy topology is accepted, this lane may contain:

- Archaeology-specific Rego/OPA or equivalent promotion rules;
- domain policy data that belongs with those rules and contains no protected payload;
- promotion input adapters that are policy-local and do not become general runtime code;
- rule documentation tightly coupled to executable policy;
- package namespace and entrypoint notes;
- reason-code and obligation mappings;
- compatibility shims approved by migration governance;
- local README/index material;
- test pointers and bundle references;
- deprecation, supersession, and rollback notes for promotion rules.

Every executable rule must state or bind:

- exact policy package and query entrypoint;
- supported input schema/version;
- gate and transition;
- domain/object families;
- default outcome;
- finite engine result;
- normalized PromotionDecision/PolicyDecision outcome;
- safe reason codes;
- obligations;
- required evidence, rights, sensitivity, review, release, and rollback context;
- fixture and test references;
- policy bundle identity/digest;
- correction and deprecation behavior.

## What does not belong here

| Does not belong here | Correct authority home |
|---|---|
| Operational promotion procedure | `docs/runbooks/archaeology/` |
| Archaeology object meaning | `contracts/domains/archaeology/` |
| PromotionDecision meaning | `contracts/release/` |
| JSON Schemas | `schemas/contracts/v1/` |
| Source descriptors or authority records | Governed `data/registry/` and control-plane registers |
| Raw, work, quarantine, processed, catalog, triplet, or published payloads | Governed `data/` lifecycle roots |
| Exact site coordinates or protected cultural substance | Restricted governed stores; never public repo docs or fixtures |
| EvidenceBundle, proof, or evidence payload | Evidence/proof roots |
| Actual ReviewRecords | Governed review/release record lanes |
| PromotionDecision instances | `release/promotion_decisions/` or accepted release record home |
| Release manifests, withdrawal notices, correction notices, rollback cards | `release/` |
| Reusable fixtures or executable tests | `fixtures/` and `tests/` |
| Validator implementations | `tools/validators/` |
| General policy runtime | `packages/policy-runtime/` or accepted evaluator lane |
| Pipeline transforms | `pipelines/domains/archaeology/` |
| API, UI, MapLibre, search, export, graph, or AI implementation | Governed application/package roots |
| Secrets, consent tokens, embargo details, protected review substance | Approved secret/restricted systems |

[Back to top](#top)

---

## Governed lifecycle and gates

KFM's lifecycle is invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is the governed decision to cross a boundary. It is not:

- a file move;
- a directory copy;
- a pull-request merge;
- a successful schema test;
- a green workflow;
- a candidate folder;
- a deployed tile;
- a generated report;
- a published-looking URL;
- an AI answer.

### Gate model

The Archaeology runbook describes seven doctrine gates:

| Gate | Durable concern | Archaeology overlay | Default when incomplete |
|---|---|---|---|
| **A — Structure and metadata** | Identity, MetaBlock, required metadata | Source role, candidate/site class, CARE/authority metadata where applicable | `ABSTAIN` or hold prior state |
| **B — Schemas and contracts** | Machine shape and semantic contract alignment | Archaeology object family, PromotionDecision shape, no contract/schema collapse | Deny transition |
| **C — Policy parity** | Same accepted bundle/digest in CI and runtime | Archaeology promotion, sensitivity, cultural-review, rights, consent, and public-surface policy parity | Deny activation |
| **D — Security and sensitivity** | Rights, sensitivity, license, secret, redaction controls | No exact/reverse-engineerable geometry; protected cultural categories; sovereignty and consent; named transform receipt | `DENY`, `ABSTAIN`, or quarantine |
| **E — Data quality** | Required validators and thresholds | Candidate/site separation, evidence quality, geometry safety, source role, temporal and catalog checks | Hold or quarantine |
| **F — Provenance and lineage** | Receipts, hashes, lineage, EvidenceBundle resolution | SensitivityTransform/RedactionReceipt, EvidenceRef closure, review refs, immutable history | `ABSTAIN` or deny |
| **G — Reviewability** | Named accountable review and release readiness | Author ≠ release authority; sensitivity reviewer; cultural/sovereignty reviewer; rights-holder representative when applicable; rollback target | Hold |

### Transition matrix

| Requested transition | Minimum policy question | Safe default |
|---|---|---|
| Source discovery → RAW | Is source identity, role, authority, rights, sensitivity, and payload hash minimally recorded? | Do not admit or hold for source review. |
| RAW → WORK | Is processing allowed and bounded? | Route unresolved material to QUARANTINE. |
| RAW → QUARANTINE | Is a fail-closed reason recorded without leaking protected content? | Quarantine with safe reason code. |
| WORK → PROCESSED | Do schema, validation, identity, evidence, rights, and sensitivity transforms pass? | Hold or quarantine. |
| PROCESSED → CATALOG/TRIPLET | Are evidence, catalog, source-role, graph, review, and redaction closures complete? | `ABSTAIN` or hold. |
| CATALOG/TRIPLET → release candidate | Can a safe review dossier be assembled without protected substance? | Hold; candidate is not release. |
| Release candidate → PUBLISHED | Do policy, evidence, review, release manifest, correction, and rollback gates all close? | `DENY` or `ABSTAIN`. |
| PUBLISHED → corrected/superseded/withdrawn | Is the defect and affected derivative set known? | Restrict/withdraw immediately where risk exists. |
| PUBLISHED → rolled back | Can the prior safe artifact set be verified and restored through governed release? | Hold public serving or withdraw until safe state is restored. |

### State-preservation invariant

For `DENY`, `ABSTAIN`, policy/runtime error, missing review, or unresolved support:

- preserve the prior lifecycle state;
- do not copy the candidate into a more public path;
- do not change a registry status to imply promotion;
- do not emit a public layer or answer;
- do not overwrite prior decision history;
- record only safe metadata and references;
- route remediation to the owning authority;
- keep rollback and correction handles visible.

[Back to top](#top)

---

## Confirmed promotion surface

```text
policy/domains/archaeology/promotion/
└── README.md                              # direct lane; documentation only

policy/promotion/
├── promotion_prerequisites.rego          # PROPOSED stub; default deny := false
└── rollback_card_required.rego           # PROPOSED stub; default deny := false

contracts/release/
└── promotion_decision.md                 # draft semantic contract

schemas/contracts/v1/release/
└── promotion_decision.schema.json        # concrete PROPOSED shape

tools/validators/release/
└── validate_promotion_decision.py        # executable schema-runner adapter

tests/release/
└── test_promotion_decision_schema.py     # executable fixture-validation test

fixtures/release/promotion_decision/
├── valid/                                # workflow requires nonempty JSON inventory
└── invalid/                              # workflow requires nonempty JSON inventory

.github/workflows/
├── promotion-gate.yml                    # shape checks + explicit implementation holds
└── domain-archaeology.yml                # domain validation/proof/release holds

release/candidates/archaeology/
└── README.md                              # no child candidate established in bounded evidence
```

This inventory is a current evidence snapshot, not proof of exhaustive permanent absence elsewhere.

### No activation by presence

None of these activates promotion:

- a Rego file;
- a README;
- a schema;
- fixture JSON;
- passing schema tests;
- a workflow definition;
- a candidate README;
- a generated receipt;
- a review-console screen;
- a branch-protection check name;
- a merged PR.

Activation requires an accepted, digest-pinned bundle; explicit selector; evaluator; input contract; substantive positive and negative tests; reviewer authority; deployment binding; audit receipt; rollback path; and governed consumer integration.

[Back to top](#top)

---

## Minimum promotion policy input

A future Archaeology promotion evaluator should receive one immutable, explicit input packet. It must not fetch hidden facts during evaluation.

| Input family | Minimum information | Fail-closed condition |
|---|---|---|
| Request | operation, requested transition, requested audience, purpose, caller/capability | Missing or unsupported request |
| Identity | candidate id, run id, artifact refs/digests, domain, object family, version | Ambiguous or mutable identity |
| Lifecycle | current state, requested state, prior decision refs, candidate/release refs | Illegal or skipped transition |
| Source | source id, source role, authority, rights/license, attribution, source digest | Missing role, authority, or rights |
| Candidate/site class | candidate, anomaly, contextual signal, confirmed site assertion | Candidate presented as confirmed |
| Evidence | EvidenceRef list, EvidenceBundle URI/ref, closure status, freshness | Unresolved, stale, contradictory, or missing evidence |
| Geometry | precision, public geometry, reverse-inference risk, transform profile | Exact or reconstructable protected location |
| Sensitivity | audience tier, per-record rank, burial/remains/sacred/looting/security flags | Unknown or prohibited sensitivity |
| Cultural/sovereignty | steward/rights-holder authority, CARE labels, review state, consent, embargo, revocation | Required authority or consent unresolved |
| Transform | redaction/generalization profile id/version, receipt ref, determinism inputs | Missing or unverifiable transform |
| Validation | ValidationReport refs, validator versions, pass/hold/deny findings | Required validator absent or non-pass |
| Policy | bundle id/version/digest, evaluator profile, query, policy-data digest | Unpinned or mismatched policy |
| Review | author, sensitivity reviewer, cultural reviewer, rights-holder representative, release authority, tickets/records | Missing or non-independent required role |
| Promotion record | PromotionDecision id/version/domain/run/decision support | Invalid or incomplete decision record |
| Release | candidate ref, ReleaseManifest ref/state, published carrier refs | Release prerequisites incomplete |
| Correction | correction/withdrawal/supersession refs and affected derivative inventory | No correction path |
| Rollback | RollbackCard ref, prior safe digests, drill status, disablement plan | Missing or untested rollback |
| Runtime/public | intended API/UI/map/export/AI consumers and obligation handlers | Consumer cannot enforce obligations |
| Audit | evaluation time, trace id, spec hash, receipts, safe reason/obligation refs | Consequential decision not auditable |

### Input minimization

Policy input must contain enough context to decide safely, but must not include protected substance unnecessarily.

Do not place in a generic policy input:

- raw exact coordinates;
- burial or human-remains details;
- sacred-site narratives;
- consent secrets or tokens;
- private landowner identifiers;
- collection-security locations;
- restricted review deliberations;
- looting-risk operational details.

Use governed references and coarse classifications where possible.

[Back to top](#top)

---

## Decision vocabularies and normalization

KFM currently has distinct decision vocabularies. They must not be collapsed by string substitution.

### Shared PromotionDecision vocabulary

The paired release schema permits:

```text
APPROVE | DENY | ABSTAIN
```

`APPROVE` means the evaluated transition may proceed through the governed release process. It does not mean published, public, safe for all audiences, or approved by every downstream authority.

### Runtime PolicyDecision / response vocabulary

The shared policy/runtime surface uses:

```text
ANSWER | ABSTAIN | DENY | ERROR
```

This is used for governed response envelopes and policy decisions, not as a direct replacement for release-transition `APPROVE`.

### Internal workflow dispositions

Policy and orchestration may need internal states such as:

```text
HOLD | RESTRICT | QUARANTINE | NEEDS_REVIEW | REDIRECT
```

These are dispositions/obligations, not automatically valid fields in the shared PromotionDecision schema.

### Proposed normalization

| Internal result | PromotionDecision | Runtime/public result | Required behavior |
|---|---|---|---|
| `ALLOW` / gate pass | `APPROVE` only when all required release-transition inputs close | `ANSWER` only for released, bounded public content | Preserve scope and obligations. |
| `RESTRICT` | Usually `ABSTAIN` until required transform/review is completed, or `APPROVE` only for an explicitly restricted governed transition | `ANSWER` at bounded scope or `DENY` for unsupported audience | Emit and enforce obligations. |
| `HOLD` / `NEEDS_REVIEW` | `ABSTAIN` | `ABSTAIN` | Preserve prior state. |
| `QUARANTINE` | `DENY` or `ABSTAIN` according to reason | `DENY` or `ABSTAIN` | No public path. |
| `DENY` | `DENY` | `DENY` | Do not reveal protected detail. |
| Policy/evaluator error | No approval; record failed evaluation separately | `ERROR` | Fail closed. |
| Unsupported input | `ABSTAIN` | `ABSTAIN` | Request governed remediation. |

### PromotionDecision schema boundary

The shared schema currently requires:

- `id`;
- `version = "v1"`;
- `domain`;
- `run_id`;
- `decision`;
- `evidence_ref`;
- `evidence_bundle_uri`;
- `rollback_card_uri`;
- `policy_bundle`;
- `decided_at`;
- `review.reviewer`;
- `review.ticket`.

It disallows additional properties.

This is useful shape closure, but it does not itself require:

- Archaeology object family;
- current/requested lifecycle state;
- exact-location risk;
- sensitivity tier/rank;
- named redaction profile;
- RedactionReceipt;
- cultural or sovereignty review;
- rights-holder sign-off;
- consent/embargo/revocation state;
- release manifest;
- correction/withdrawal state;
- public-consumer obligation handling;
- separation of all required reviewer roles.

Those requirements must be supplied by accepted policy, companion contracts/records, and tests—not silently stuffed into the closed schema without governed schema evolution.

### ID conflict

The current schema includes a hydrology-specific `id` conditional but no Archaeology-specific identifier rule. An Archaeology promotion-decision id convention remains `NEEDS VERIFICATION`; do not invent one in production from this README.

[Back to top](#top)

---

## Gate artifact matrix

| Gate/transition | Required support | Archaeology-specific requirement | Blocking examples |
|---|---|---|---|
| Admission | SourceDescriptor or accepted source record, source hash, role, authority, rights | Cultural/sovereignty authority and sensitivity posture identified where applicable | Unknown role, rights, authority, or protected payload in public fixture |
| RAW → WORK/QUARANTINE | Intake/transform context, schema selection, identity | Candidate/site class and sensitive-category classification | Candidate mislabeled site; exact geometry unbounded |
| WORK → PROCESSED | ValidationReport, TransformReceipt, schema/contract refs | Named SensitivityTransform/RedactionReceipt and no protected leakage | Missing validators, failed transform, unresolved rights |
| PROCESSED → CATALOG/TRIPLET | EvidenceRef→EvidenceBundle closure, catalog/proof refs | Review refs and source-role preservation; graph cannot expose protected edges | Unresolved evidence; location reconstruction |
| CATALOG/TRIPLET → candidate | Candidate dossier, blocker list, safe summary | No protected substance; cultural/sensitivity review queued or complete | Public-review dossier leaks detail |
| Candidate → PromotionDecision | Policy bundle/digest, evaluator, evidence, rollback, review binding | Archaeology overlays and independent reviewers | Stub policy, automation-only reviewer, unresolved cultural authority |
| PromotionDecision → ReleaseManifest | Approved transition plus complete release artifact set | Redaction/cultural-review/release obligations preserved | `APPROVE` treated as manifest |
| ReleaseManifest → PUBLISHED | Governed release action, signatures, rollback/correction path | Public carriers generalized and reverse-inference tested | Direct internal-store route; no rollback |
| PUBLISHED → corrected/withdrawn | CorrectionNotice/WithdrawalNotice and derivative inventory | Immediate restriction for sensitivity, rights, or geometry defects | Silent mutation; stale unsafe cache |
| Corrected/withdrawn → rollback/supersession | RollbackCard or superseding manifest, prior digests | Disablement, cache invalidation, public stale/withdrawn state | Hidden file copy; history overwritten |

### Receipt/proof separation

- A `RedactionReceipt` records a transform; it is not evidence or release approval.
- A `PromotionDecision` records a transition decision; it is not a ReleaseManifest.
- A `PromotionReceipt`, if accepted, would record process memory; it would not replace PromotionDecision, ReviewRecord, evidence, or release authority.
- A generated AI receipt records generation provenance; it is not cultural review, policy approval, or proof.
- A ProofPack/EvidenceBundle supports claims; it does not approve promotion.
- A ReleaseManifest binds released artifacts; it does not retroactively validate source truth.

[Back to top](#top)

---

## Archaeology sensitive-domain overlays

### Default posture

When sensitivity or authority is unresolved:

```text
DENY exact exposure
-> GENERALIZE / REDACT / WITHHOLD
-> REQUIRE named review
-> REQUIRE receipt and evidence closure
-> ABSTAIN or HOLD until all required gates close
```

### Protected categories

Promotion must fail closed for:

- exact or reverse-engineerable site locations;
- burial and human-remains information;
- sacred or ceremonial sites;
- culturally restricted knowledge;
- collection-security detail;
- looting-risk information;
- private landowner or access details;
- restricted oral history;
- sovereignty-bearing labels and review substance;
- embargoed or revoked material;
- sensitive LiDAR, geophysics, SAR, AOD-like, 3D, terrain, or imagery derivatives capable of reconstruction;
- graph, search, vector-index, screenshot, tile, or AI outputs that reveal protected detail indirectly.

### Named transform requirement

A public-safe derivative must identify:

- profile id;
- version;
- steward/owner;
- input precision/class;
- output precision/class;
- deterministic parameters/seed where applicable;
- suppression/generalization method;
- sensitivity basis;
- reason;
- receipt ref;
- reviewer refs;
- affected outputs;
- correction and rollback refs.

No numeric geometry, H3, jitter, differential-privacy, or k-anonymity threshold is accepted by this README. Current doctrine proposes examples and floors; operational values require accepted policy/profile authority and tests.

### No public T0 assumption

A generalized output is not automatically T0/public. It still requires:

- source and rights clearance;
- evidence closure;
- sensitivity/cultural review;
- transform and receipt verification;
- policy approval;
- release manifest;
- correction/rollback readiness;
- public-consumer obligation tests.

### Rights and sovereignty

A valid license does not erase cultural authority, sovereignty, consent, embargo, or sensitivity obligations. The most restrictive applicable rule wins.

[Back to top](#top)

---

## Candidate versus confirmed site boundary

Promotion must preserve distinct knowledge characters:

```text
CandidateFeature / anomaly / model / remote-sensing signal
!= confirmed ArchaeologicalSite
```

### Required behavior

- A remote-sensing, LiDAR, geophysics, model, or imagery candidate remains a candidate unless admissible evidence and review support confirmation.
- Promotion of a candidate artifact may approve processing or review without approving a site assertion.
- A schema-valid candidate cannot be relabeled as a confirmed site through a field rename, UI label, graph edge, search index, or AI summary.
- Adjacent Roads, Settlement, Geology, Soil, Hydrology, Habitat, Hazards, or land-context evidence may support context but cannot independently confirm an ArchaeologicalSite.
- A PromotionDecision must scope its subject and transition; it must not be interpreted as blanket domain truth.

### Negative tests

Required negative cases include:

- candidate relabeled as confirmed site;
- contextual source role collapsed into primary archaeological evidence;
- model output presented as observation;
- candidate geometry exposed at protected precision;
- graph join reconstructing an exact location;
- AI answer adding certainty absent from evidence;
- public map symbol implying confirmation;
- release summary omitting candidate status.

[Back to top](#top)

---

## Review and separation of duties

### Required roles by materiality

| Role | Responsibility | Must be independent when |
|---|---|---|
| Author/producer | Prepares candidate and support packet | Always distinct from final release authority for material sensitive releases |
| Archaeology steward | Confirms domain scope and object-family posture | Archaeology meaning or identity is material |
| Sensitivity reviewer | Reviews exact/reconstruction risk and transform | Any sensitive geometry/category is involved |
| Cultural/sovereignty reviewer | Reviews cultural authority, CARE, sovereignty, consent, embargo | Cultural or sovereignty-bearing material is involved |
| Rights-holder representative | Confirms applicable authority/permission | Named rights-holder or sovereign authority applies |
| Evidence reviewer | Confirms evidence closure and source-role integrity | Claim-bearing promotion |
| Policy reviewer | Confirms bundle/query/input/decision parity | Policy-bearing change or release |
| Validator/test reviewer | Confirms deterministic negative coverage | New rule/profile/contract/schema |
| Release authority | Approves governed release transition | Any public-impacting promotion |
| Correction/rollback reviewer | Confirms recovery path and derivative inventory | Public-impacting promotion |
| Security reviewer | Confirms logs, access, leakage, and secret handling | Protected or high-risk material |

### Review record requirements

A real review must bind:

- subject/artifact;
- transition;
- reviewer identity and authority;
- role;
- scope;
- decision;
- conditions/obligations;
- timestamp;
- ticket/record id;
- policy/profile version;
- evidence and receipt refs;
- conflicts/recusals;
- expiry or revocation conditions where applicable.

The minimal `review.reviewer` and `review.ticket` inside PromotionDecision do not replace a richer ReviewRecord when materiality requires one.

### Automation boundary

Automation may validate shape, inventory, hashes, deterministic fixtures, and explicit prerequisites. Automation must not impersonate:

- cultural authority;
- rights-holder authority;
- sensitivity review;
- independent release approval;
- consent;
- sovereignty review;
- evidence interpretation.

An automation-only `APPROVE` with unresolved refs is not a governed release decision.

[Back to top](#top)

---

## Reason codes and obligations

The following are `PROPOSED` families for future accepted policy and shared registries. They are not yet a machine contract.

### Safe reason-code families

| Family | Examples | Disclosure posture |
|---|---|---|
| Identity/lifecycle | `object_family_unresolved`, `transition_invalid`, `candidate_status_unresolved` | Safe if no protected subject detail is exposed |
| Source/rights | `source_role_unresolved`, `rights_unresolved`, `authority_unresolved` | Do not reveal confidential source terms |
| Evidence | `evidence_ref_unresolved`, `evidence_bundle_incomplete`, `evidence_stale` | Return bounded support status only |
| Sensitivity | `exact_geometry_prohibited`, `reverse_inference_risk`, `sensitivity_unresolved` | Never echo coordinates or protected categories unnecessarily |
| Cultural/sovereignty | `cultural_review_required`, `sovereignty_review_required`, `consent_unresolved`, `embargo_active`, `revocation_active` | Minimize protected review substance |
| Transform | `redaction_profile_missing`, `redaction_receipt_missing`, `transform_unverifiable` | Do not reveal transformation secrets that increase risk |
| Validation | `validation_report_missing`, `validator_failed`, `policy_parity_failed` | Expose safe summary, not sensitive payload |
| Review | `review_record_missing`, `separation_of_duties_failed`, `review_expired` | Avoid leaking reviewer-sensitive deliberations |
| Promotion/release | `promotion_decision_invalid`, `release_manifest_missing`, `candidate_not_reviewed` | State held/denied status |
| Rollback/correction | `rollback_target_missing`, `rollback_unverified`, `correction_path_missing` | Do not reveal protected artifact locations |
| Runtime/system | `policy_bundle_missing`, `evaluator_unavailable`, `policy_input_invalid` | Fail closed; log securely |

### Obligation families

- `preserve_prior_state`;
- `quarantine_required`;
- `source_review_required`;
- `rights_review_required`;
- `cultural_review_required`;
- `sovereignty_review_required`;
- `consent_review_required`;
- `sensitivity_review_required`;
- `generalization_required`;
- `redaction_required`;
- `aggregation_required`;
- `embargo_required`;
- `delay_required`;
- `audience_restriction_required`;
- `evidence_bundle_required`;
- `validation_report_required`;
- `redaction_receipt_required`;
- `review_record_required`;
- `promotion_decision_required`;
- `release_manifest_required`;
- `rollback_card_required`;
- `correction_path_required`;
- `withdrawal_required`;
- `cache_invalidation_required`;
- `public_bypass_denied`;
- `official_authority_or_steward_redirect_required`;
- `audit_receipt_required`.

Downstream systems must treat obligations as enforceable constraints, not decorative metadata.

[Back to top](#top)

---

## Public surface and trust membrane

Normal public clients must use governed interfaces and released public-safe artifacts. They must not read:

- RAW;
- WORK;
- QUARANTINE;
- unrestricted PROCESSED records;
- internal catalog/triplet detail;
- candidate dossiers as if released;
- PromotionDecision objects as public permission;
- review records;
- receipts or proofs directly as truth;
- internal policy inputs or protected reason detail.

### Surface-specific requirements

| Surface | Required behavior |
|---|---|
| Governed API | Resolve release state and obligations; return finite envelope; never fall back to internal stores. |
| Explorer/MapLibre | Render only released carriers; no exact or reconstructable locations; preserve candidate and uncertainty labels. |
| Evidence Drawer | Show safe citations and release state without exposing protected evidence or coordinates. |
| Focus Mode / AI | Cite or abstain; deny exact-location and cultural-detail requests; never infer hidden location from combined clues. |
| Search/index | Exclude or generalize protected fields; prevent facet combinations that reconstruct location. |
| Graph | Suppress protected nodes/edges and indirect traversal paths. |
| Export/download | Require audience/capability checks and released artifact binding. |
| Screenshot/report | Apply the same sensitivity policy as interactive surfaces. |
| Tiles/PMTiles | Verify generalized geometry and metadata; tile presence is not release authority. |
| Cache/CDN | Support revocation, withdrawal, stale marking, and invalidation. |

### Public bypass checks

Tests must prove that:

- unreleased candidate ids cannot resolve through public routes;
- internal object refs do not become downloadable URLs;
- a denied or abstained transition cannot be rendered by alternate endpoint;
- stale or withdrawn content is visibly blocked/marked;
- vector, graph, search, and AI paths cannot reconstruct protected locations;
- a schema-valid PromotionDecision does not bypass ReleaseManifest checks.

[Back to top](#top)

---

## Validation, tests, and CI

### Confirmed shared shape lane

The repository currently has:

1. a PromotionDecision contract;
2. a closed PromotionDecision schema;
3. a validator adapter;
4. an executable pytest wrapper;
5. valid/invalid fixture inventories required to be nonempty by workflow;
6. a promotion-gate job that runs the shape test.

This is meaningful progress, but limited to selected shape checks.

### Explicit workflow holds

The promotion-gate workflow states that it does **not**:

- resolve EvidenceRefs;
- execute promotion policy;
- verify policy bundle digest;
- enforce review separation;
- validate rollback targets;
- authorize lifecycle transition;
- emit PromotionDecision, receipt, proof, manifest, release, or publication.

The domain-archaeology workflow likewise holds:

- executable Archaeology validation;
- proof construction;
- release dry run;
- candidate publication.

### Required test matrix

| Case | Expected promotion posture | Required assertion |
|---|---|---|
| Complete synthetic shared shape | Shape pass only | Must not imply Archaeology approval |
| Missing required schema field | Validation failure | No decision emitted |
| Extra property | Validation failure | Closed shape preserved |
| Invalid decision enum | Validation failure | Vocabulary stays bounded |
| Missing evidence closure | `ABSTAIN` or `DENY` | Prior state preserved |
| Missing rollback target | `ABSTAIN` or `DENY` | No public transition |
| Missing review binding | `ABSTAIN` | No approval |
| Automation-only reviewer | `ABSTAIN` or `DENY` for material Archaeology release | Human/cultural authority required |
| Candidate presented as site | `DENY` | Anti-collapse preserved |
| Exact geometry | `DENY` | No coordinates in result/log |
| Reverse-inference geometry | `DENY` or `ABSTAIN` | Cross-output reconstruction blocked |
| Missing cultural review | `ABSTAIN` or `DENY` | Required reviewer named |
| Revoked/embargoed material | `DENY` | Cache invalidation/withdrawal obligation |
| Rights unresolved | `ABSTAIN` or `DENY` | No release |
| Redaction profile missing | `ABSTAIN` | Transform cannot proceed |
| Redaction receipt missing | `ABSTAIN` or `DENY` | No catalog/public promotion |
| Policy bundle missing/stale | `ERROR` or `ABSTAIN` | Fail closed |
| CI/runtime digest mismatch | `DENY` | Parity failure visible |
| ReleaseManifest missing | `ABSTAIN` | `APPROVE` is not publication |
| Public route bypass | Test failure / `DENY` | No internal-state exposure |
| Correction after sensitivity defect | Restrict/withdraw | Derivatives and caches invalidated |
| Rollback drill | Deterministic restore | Prior safe digests verified |

### No-network default

Default tests must:

- use synthetic public-safe data;
- block live source requests;
- avoid secrets and protected endpoints;
- avoid real site coordinates;
- avoid real cultural-review substance;
- use deterministic timestamps/ids/hashes where practical;
- test positive and negative cases;
- fail on empty fixture polarity;
- preserve safe logs.

### CI admission criteria

Archaeology promotion enforcement should not become a required check until:

- policy package/query is accepted;
- default semantics are fail-closed;
- input contract is accepted;
- bundle manifest/digest is pinned;
- evaluator is available;
- positive and negative fixtures are nonempty;
- exact-location and reverse-inference cases exist;
- cultural/sovereignty/rights cases exist;
- decision normalization is tested;
- public obligation handlers are tested;
- correction and rollback are tested;
- reviewer ownership and escalation are assigned.

[Back to top](#top)

---

## Threat and failure model

| Threat/failure | Risk | Required control |
|---|---|---|
| File-presence activation | Scaffold treated as live policy | Explicit allowlisted selector and bundle digest |
| Fail-open default | Missing rules permit promotion | Default-deny/abstain semantics and negative tests |
| Schema-laundered approval | Shape pass treated as safe release | Separate semantic, evidence, policy, review, and release gates |
| Candidate/site collapse | Unconfirmed signal presented as site | Knowledge-character rules and tests |
| Exact-location leak | Looting, harm, sovereignty violation | Deny, generalize, redact, reverse-inference tests |
| Cross-output reconstruction | Multiple generalized outputs reveal location | Differencing/mosaic/join risk evaluation |
| Reviewer spoofing | Automation or author impersonates authority | Signed/registered ReviewRecord and separation of duties |
| Cultural-authority bypass | License mistaken for sovereignty/consent | Most-restrictive review and rights-holder checks |
| Receipt-as-proof | Transform process record treated as evidence | Artifact-family separation |
| PromotionDecision-as-release | `APPROVE` served publicly | ReleaseManifest and governed serving checks |
| Hidden policy fetch | Non-replayable or mutable input | Immutable explicit input packet |
| CI/runtime drift | Different decisions in review and production | Bundle/query/evaluator digest parity |
| Sensitive logging | Protected details leak in error output | Safe reason codes and log minimization |
| Stale policy/review | Old approval reused after change/revocation | Expiry, supersession, correction, reevaluation |
| Incomplete rollback | Unsafe release persists | Prior digests, disablement, cache invalidation, drills |
| Public fallback | Governed route failure reads internal store | Deny/abstain; no fallback |
| AI triangulation | Generated answer infers exact location | Bounded retrieval, policy, anti-inference tests |
| Orphan fixture | Synthetic example has no consumer | Consumer backlinks and inventory checks |
| Vacuous green | Empty fixture/test suite passes | Nonempty polarity assertions |

### Safe failure interpretation

A failed check means the evaluated prerequisite did not close. It does not mean:

- the repository is corrupted;
- the source is false;
- the cultural authority rejected the material;
- the artifact should be deleted;
- a public explanation should reveal the hidden reason.

Route failure to the owning authority with minimal safe context.

[Back to top](#top)

---

## Review burden and separation of duties

Changes to this lane require:

- Archaeology steward review;
- policy steward review;
- sensitivity and cultural/sovereignty review;
- rights-holder representation when the rule affects governed cultural material;
- contract/schema review when decision/input shapes change;
- validator/test review when enforcement changes;
- security review for exposure/logging/access changes;
- release and rollback review for public-impacting changes.

### Changes that require ADR or migration governance

- moving promotion policy between domain and shared policy homes;
- introducing a second promotion decision or receipt family;
- changing the canonical policy result vocabulary;
- changing the PromotionDecision schema incompatibly;
- creating a new source, review, receipt, proof, or release authority home;
- relaxing exact-location or protected-category denial;
- changing cultural/sovereignty authority model;
- allowing direct public use of promotion records;
- replacing the canonical evaluator or bundle format.

### Emergency bypass

Documentation must not invent emergency bypass authority. Any override must be:

- explicitly authorized;
- narrowly scoped;
- signed and audited;
- time-bounded;
- incapable of exposing protected archaeological material without required authority;
- reversible;
- reviewed after use.

[Back to top](#top)

---

## Smallest sound implementation sequence

1. **Freeze current scaffolds.**
   - Keep direct lane documentation-only.
   - Prevent shared default-allow behavior from being activated.

2. **Resolve decision and artifact vocabulary.**
   - Confirm PromotionDecision versus PolicyDecision normalization.
   - Decide whether PromotionReceipt exists, its meaning, schema, validator, and storage home.

3. **Define immutable policy input.**
   - Create/accept semantic contract and schema.
   - Include lifecycle, evidence, sensitivity, cultural review, rights, transform, review, release, and rollback references.

4. **Define package/query and default semantics.**
   - Adopt one namespace convention.
   - Default to deny/abstain on missing context.
   - Return bounded engine result, reasons, and obligations.

5. **Implement shared prerequisites safely.**
   - Replace comment-only promotion Rego stubs.
   - Add negative tests before activation.

6. **Implement Archaeology overlays.**
   - Candidate/site separation.
   - Exact and reverse-inference denial.
   - Cultural/sovereignty/rights/consent/embargo/revocation checks.
   - Named transform/receipt requirements.
   - Separation of duties.

7. **Build deterministic fixture matrix.**
   - Use synthetic public-safe examples.
   - Cover every gate and negative condition.
   - Require nonempty valid/invalid/deny/abstain inventories.

8. **Implement evaluator and validator integration.**
   - Pin evaluator and bundle digest.
   - Validate input, result normalization, and obligation propagation.
   - Minimize logs.

9. **Add review and release record validation.**
   - Real ReviewRecord semantics.
   - PromotionDecision reference validation.
   - ReleaseManifest, correction, withdrawal, rollback closure.

10. **Add public-surface tests.**
    - Governed API, MapLibre, Evidence Drawer, Focus Mode, search, graph, export, cache, and AI.

11. **Run correction and rollback drills.**
    - Geometry over-precision.
    - Cultural-review revocation.
    - Rights withdrawal.
    - Evidence defect.
    - Policy regression.

12. **Graduate CI deliberately.**
    - Replace readiness holds only after commands, fixtures, ownership, and rollback are accepted.
    - Record branch-protection significance.

13. **Document and monitor.**
    - Update runbooks and evidence ledgers.
    - Track denials, abstentions, stale approvals, rollback readiness, and drift without exposing sensitive details.

Each step should be independently reviewable and reversible.

[Back to top](#top)

---

## Definition of done

### Governance and placement

- [ ] Owners and CODEOWNERS are assigned.
- [ ] Domain versus shared promotion policy topology is accepted.
- [ ] No parallel contract, schema, policy, receipt, proof, review, or release home exists without migration governance.
- [ ] PromotionDecision/PolicyDecision/PromotionReceipt vocabulary is resolved.
- [ ] Archaeology-specific id and gate conventions are accepted.

### Policy and runtime

- [ ] Immutable policy input contract and schema are accepted.
- [ ] Policy package/query/default semantics are accepted.
- [ ] Shared promotion prerequisites are substantive and fail closed.
- [ ] Archaeology overlays are implemented.
- [ ] Bundle manifest/digest and evaluator profile are accepted.
- [ ] CI/runtime parity is tested.

### Evidence, sensitivity, and review

- [ ] EvidenceRef-to-EvidenceBundle closure is validated.
- [ ] Candidate-versus-site anti-collapse is enforced.
- [ ] Exact and reverse-inference location denial is enforced.
- [ ] Named redaction/generalization profiles are accepted and receipt-backed.
- [ ] Cultural, sovereignty, rights-holder, consent, embargo, and revocation checks are implemented.
- [ ] Reviewer authority and separation of duties are validated.

### Fixtures, validators, and tests

- [ ] Reusable and test-local fixture responsibilities are clear.
- [ ] Positive and negative fixture sets are nonempty.
- [ ] Every gate has approve, deny, abstain, error, and obligation cases as applicable.
- [ ] No-network and sensitive-log controls are tested.
- [ ] Archaeology validator commands are implemented.
- [ ] Shared PromotionDecision shape tests remain green and non-vacuous.
- [ ] Domain promotion behavior is tested beyond shape.

### Release and public surfaces

- [ ] Candidate dossier exists only when safe public-review metadata is available.
- [ ] PromotionDecision references resolve.
- [ ] ReleaseManifest, correction, withdrawal, and rollback records validate.
- [ ] Governed public routes enforce all obligations.
- [ ] Internal lifecycle and review stores have no public fallback.
- [ ] Cache invalidation and stale/withdrawn rendering are tested.
- [ ] No protected location or cultural detail can be reconstructed across outputs.

### Operations and reversibility

- [ ] Promotion dry run exists and performs no release.
- [ ] Human review records are accountable and inspectable.
- [ ] Correction and rollback drills pass.
- [ ] Monitoring and audit reports avoid protected detail.
- [ ] Documentation matches actual commands and maturity.
- [ ] Required checks are deliberately configured.

Until all applicable items close, this lane remains draft and promotion remains fail-closed.

[Back to top](#top)

---

## Conflict and ADR register

| Conflict | Current evidence | Required resolution |
|---|---|---|
| Domain vs shared promotion policy | This README is under domain policy; shared stubs live under `policy/promotion/` | Define composition, ownership, and bundle topology |
| Fail-closed doctrine vs `default deny := false` stubs | Shared Rego files contain no active rules | Implement safe defaults and negative tests before activation |
| Promotion vocabulary | v0.1/runbook uses ALLOW/RESTRICT/HOLD; PromotionDecision schema uses APPROVE/DENY/ABSTAIN; runtime uses ANSWER/ABSTAIN/DENY/ERROR | Accept normalization contract |
| PromotionReceipt | Doctrine flow names it; checked contract/schema paths absent in fixture research | Decide object meaning, shape, validator, storage, or retire term |
| Archaeology overlays absent from shared schema | Schema is closed and cross-domain | Keep overlays in policy/companion records or evolve schema through governance |
| Hydrology-only id conditional | Shared schema has no Archaeology id rule | Accept cross-domain or domain-specific identity convention |
| Minimal review binding vs full SoD | PromotionDecision includes reviewer/ticket only | Require linked ReviewRecord for material Archaeology promotion |
| Fixture documentation drift | Fixture README previously claimed no payloads; workflow now requires nonempty valid/invalid | Reconcile fixture docs separately |
| Domain workflow vs shared promotion workflow | Domain workflow holds all executable domain maturity; shared workflow validates shape | Define graduation and dependency order |
| Candidate/release topology drift | Shared and domain release lanes carry naming/segmentation history | Use narrowest verified path and migration notes |

No conflict is resolved merely by this README.

[Back to top](#top)

---

## Open verification register

| Item | Evidence needed |
|---|---|
| Direct-lane exhaustive inventory | Recursive repository checkout at pinned ref |
| Accepted Archaeology promotion bundle/query | Reviewed policy source, manifest, tests, evaluator binding |
| Shared promotion policy implementation | Substantive rules and negative fixtures |
| Policy input contract/schema | Accepted semantic contract, JSON Schema, fixtures |
| PromotionReceipt status | ADR/contract/schema/validator/storage decision |
| PromotionDecision Archaeology identity | Accepted deterministic id convention |
| Real Archaeology ReviewRecords | Governed review record instances and authority registry |
| Cultural/sovereignty workflow implementation | Review service/records, consent/embargo/revocation handling |
| Named transform profiles | Accepted policy data, reviewer approval, deterministic tests |
| Evidence closure | Resolver, EvidenceBundle instances, proof validation |
| Archaeology validator implementation | Executable commands, reports, tests |
| Domain promotion fixtures/tests | Nonempty, public-safe, deterministic suites |
| Candidate dossier | Reviewed safe dossier with protected substance excluded |
| Promotion decision instance | Valid, evidence-bound, review-bound, rollback-bound record |
| Release dry run | Deterministic command and report with no publication |
| Public-surface obligation handlers | API/UI/map/search/graph/export/AI tests |
| Correction/withdrawal propagation | Notices, derivative inventory, cache invalidation |
| Rollback execution | Drill logs and prior safe digest restoration |
| CI/branch protection | Required check configuration and owners |
| Production consumer/monitoring | Deployment bindings, logs, dashboards, alerts |

[Back to top](#top)

---

## Maintenance, correction, and rollback

### README maintenance triggers

Update this README when any of these change:

- direct lane inventory;
- shared promotion policy;
- PromotionDecision contract/schema/validator/fixtures;
- PromotionReceipt decision;
- Archaeology sensitivity/review policy;
- candidate/release topology;
- domain or promotion workflows;
- policy runtime/evaluator;
- public-surface handlers;
- correction or rollback process;
- owners or required reviews.

### Policy correction triggers

Re-evaluate affected decisions and releases when:

- evidence is corrected or withdrawn;
- source authority or rights change;
- cultural or sovereignty review is revoked;
- consent or embargo state changes;
- sensitivity ranking/profile changes;
- geometry is found too precise or reconstructable;
- candidate/site classification changes;
- policy bundle/query/evaluator changes;
- validator defect is found;
- review independence was invalid;
- rollback target is missing or corrupt;
- public consumers failed to enforce obligations.

### Rollback behavior

A policy or release rollback must:

1. identify affected bundle, decisions, candidates, releases, and derivatives;
2. disable or restrict unsafe public surfaces;
3. invalidate caches and indexes;
4. preserve audit history;
5. issue correction/withdrawal records;
6. restore prior safe bundle/artifact digests;
7. rerun policy, evidence, review, validation, release, and public-surface checks;
8. record rollback outcome;
9. avoid revealing protected detail in notices.

### Rollback for this documentation change

Restore prior README blob:

```text
3dd85efb1134fc310b5191efde04dec086eb2b05
```

Remove the paired generated receipt if this revision is reverted. No policy source, protected payload, evidence object, review record, release object, runtime behavior, deployment, or public state requires restoration.

[Back to top](#top)

---

## Evidence ledger

| Evidence | What it supports | Limitation |
|---|---|---|
| Directory Rules | `policy/` is canonical admissibility root; lifecycle and responsibility split | Doctrine, not runtime proof |
| Prior target README | Existing v0.1 scope and promotion concepts | Predates current repository maturity |
| Archaeology parent policy | Domain deny-by-default and responsibility boundary | Draft; no runtime enforcement |
| Promotion runbook | Gates A–G, required artifacts, state preservation, correction/rollback | Operational doctrine; many implementation paths were proposed |
| Publication and policy doc | Trust membrane, separation of duties, bounded public surfaces | Draft doctrine |
| Sensitivity doc | T4/rank-5 defaults, named transform/receipt/review posture | Operational profile values remain verification-bound |
| PromotionDecision contract | Meaning and release-transition vocabulary | Draft; not release authority |
| PromotionDecision schema | Concrete required fields and closed shape | Status `PROPOSED`; limited Archaeology semantics |
| PromotionDecision validator/test | Executable shape-validation path | Does not evaluate policy/evidence/review/release |
| PromotionDecision fixtures/workflow | Nonempty shape fixture requirement and CI execution | Synthetic examples only |
| Shared promotion Rego files | Current policy source stubs and default semantics | No substantive rules |
| Promotion-gate workflow | Real shape checks and explicit promotion/review holds | Does not promote or publish |
| Domain-archaeology workflow | Explicit validation/proof/release readiness holds | Structural evidence only |
| Archaeology test-local promotion fixture README | Fixture routing and missing PromotionReceipt paths at its snapshot | README-only direct lane; later fixture state may differ |
| Archaeology release-candidate README | No child candidate established in bounded evidence | Public-review index, not exhaustive restricted inventory |
| Archaeology validator README | Broad validator lane is README-only | No executable domain validator |
| This revision | Repository-grounded policy-boundary update | Documentation, not implementation or approval |

---

## Changelog

### v0.2 — 2026-07-19

- Replaced the generic v0.1 policy guide with a repository-grounded promotion boundary.
- Added a pinned evidence snapshot and explicit truth-label split.
- Distinguished confirmed shared PromotionDecision shape validation from unimplemented Archaeology promotion enforcement.
- Added current promotion surface inventory and no-activation-by-presence rule.
- Added Gates A–G and transition-specific Archaeology overlays.
- Added immutable promotion-policy input, decision normalization, artifact matrix, reason codes, obligations, public-surface controls, threat model, validation matrix, review duties, implementation sequence, definition of done, conflict register, open verification, and rollback.
- Recorded PromotionReceipt, decision-vocabulary, shared-schema, reviewer-binding, fixture-documentation, and shared-policy-default conflicts.
- Added a generated provenance receipt separately.
- Changed no executable policy or release behavior.

### v0.1 — 2026-06-15

- Introduced a bounded Archaeology promotion-policy sublane.
- Documented fail-closed lifecycle gates, artifact expectations, promotion obligations, and open verification items.

---

KFM rule: an Archaeology artifact advances only through a governed, evidence-bound, policy-bound, culturally and sensitivity reviewed, rollback-ready transition. A file move, schema pass, workflow result, candidate directory, PromotionDecision shape, generated receipt, map layer, or AI answer is never promotion authority by itself.

<p align="right"><a href="#top">Back to top</a></p>
