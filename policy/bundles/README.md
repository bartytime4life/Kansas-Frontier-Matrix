<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://policy/bundles
title: policy/bundles/ — Governed Policy Bundle Boundary
type: policy-readme; directory-readme; boundary-compact; policy-bundle-boundary
version: v0.3
status: draft; repository-grounded; current-state-reconciled; documentation-led; one-proposed-inactive-packaging-profile; bounded-executable-rego-outside-lane; active-bundle-unaccepted; general-evaluator-unbound; fail-closed; non-release; non-publication
owner: NEEDS VERIFICATION — .github/CODEOWNERS routes /policy/ to @bartytime4life; accepted bundle stewardship, independent policy approval, and release separation remain unproved
created: 2026-06-15
updated: 2026-08-13
policy_label: "restricted-review; policy-bundle-boundary; finite-outcomes; explicit-inputs; immutable-digests; fail-closed; evidence-aware; rights-aware; sensitivity-aware; release-gated; replayable; rollback-aware; no-secrets; no-hidden-fetches; no-directory-activation; no-public-bundle-selection"
supersedes: v0.2 (2026-07-14)
current_path: policy/bundles/README.md
owning_root: policy/
canonical_relationship: canonical policy-packaging boundary inside the singular policy root; the present Pass 12 child is a documentation-only packaging profile whose Rego source, native test, and fixtures remain in their responsibility lanes
directory_governance: accepted ADR-0029 adopts Directory Rules v2; the root-registry projection classifies policy/ as canonical for policy rules and bundles; this BOUNDARY_COMPACT README does not assemble, select, activate, evaluate, release, or publish a bundle
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 06ea27fd9b996adb21b2545f69e6860c0c681bc5
  base_tree: ae0e3620ad30d41efb3401c4f0dcdc6f9a645f7e
  target_baseline_blob: 77f59c399fbce668c916cbbc385009121d6169f4
  target_tree: 01eec7348cd3032137aada5b6f00e0c12619a2a5
  pass12_profile_tree: ec7537c9f6544abd6b0511d75c77dedceb2d65c9
  pass12_profile_readme_blob: 0c36c7c68180e74ccd9277f92284530cc2a96db0
  rego_lane_readme_blob: 0d8ddd117e091d5af099fa36aaa94487eafd20a4
  pass12_rego_blob: 175871cb929663e7a19345fd18f97a81a850b628
  pass12_rego_test_blob: 3dd5dcc6ae14381949d9aba453da9acaa9a7731f
  pass12_workflow_blob: 478f910e8e899796d15b8921e3baa55f4ce1ce73
  policy_root_blob: 6c5021f9d92778581a4e9331a9dd6ddb7efc5e35
  policy_input_contract_blob: 545c352681dd0db0cd4d169a5d2f9c364356457c
  policy_input_schema_blob: b89db4b1730c61258441e0eed037276b910b1990
  policy_input_profile_contract_blob: 3af1c2c8d525f60f6e2aac89c5a0455898d77768
  policy_input_profile_schema_blob: d72288fe5e807ea76ad65636cca682cd0c3631e7
  policy_input_profile_validator_blob: dacb6ca9a1092c23becff22c5efca4ae81c5a6fe
  policy_decision_contract_blob: ebfe97f98263e6309db6d2772cb2c5e548819650
  policy_decision_schema_blob: 1472d26a42c73f17545b4464a275412ffa1d098e
  policy_vocabulary_registry_blob: ae68a9f3cf80308f18bd04207ef2c85057750f12
  policy_vocabulary_validator_blob: 285a24415fa7cc8358f445c8d5c8ff3e5f2b03f4
  policy_evaluation_binding_validator_blob: d2c158646de6fcc56d5506219231d6f307e32c76
  policy_runtime_metadata_blob: ebb6725ad9a00d77df06f779a603814027abe084
  policy_runtime_core_blob: e7e14cf39ae6919fbbc80f1b471de6b907292edb
  policy_test_workflow_blob: ac8f125e8a4d3634d86f66836d2aa2c0e3925e75
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: b01322ef64f8c2b1ecb41de7ef4685b97cfa2a62
  root_registry_blob: 024f668b5f0a9239bafa4f8b09e2afd86300ff8c
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  contributing_blob: de5bf143e601e36a794e6e5442ae8f91c6f75aad
  pull_request_template_blob: c5624d7dbc2b83055421b4fb4542794bafa10bee
  direct_lane_files_confirmed:
    - policy/bundles/README.md
    - policy/bundles/pass12-release-gate-v1/README.md
  open_overlapping_pull_requests_found: "0 at preflight"
  inventory_method: authenticated GitHub reads of the target and history, complete 16,985-entry recursive tree, direct lane, accepted directory governance, root registry, policy source and native tests, synthetic fixtures, contracts, schemas, inactive profiles, validators, workflows, placeholder runtime, ownership routing, contribution controls, branches, and open pull requests
  bounded_inventory_note: the complete direct lane contains documentation only; no non-document bundle payload, manifest instance, lock, selector, signature, activation record, emitted decision, evaluation receipt, or publisher was established there
related:
  - ../README.md
  - ./pass12-release-gate-v1/README.md
  - ../rego/README.md
  - ../rego/release_gate_v1.rego
  - ../rego/release_gate_v1_test.rego
  - ../../fixtures/policy/release_gate_v1/allow_public.json
  - ../../fixtures/policy/release_gate_v1/deny_missing_evidence.json
  - ../../fixtures/policy/release_gate_v1/deny_missing_sensitivity.json
  - ../../fixtures/policy/release_gate_v1/deny_missing_attestation.json
  - ../../contracts/policy/policy_input_bundle.md
  - ../../contracts/policy/policy_input_bundle_profile_v1.md
  - ../../contracts/policy/policy_decision.md
  - ../../contracts/policy/policy_decision_vocabulary.md
  - ../../contracts/policy/policy_evaluation_binding_v1.md
  - ../../contracts/policy/policy_obligation_set.md
  - ../../contracts/policy/policy_obligation_reduction.md
  - ../../contracts/policy/policy_enforcement_maturity.md
  - ../../schemas/contracts/v1/policy/policy_input_bundle.schema.json
  - ../../schemas/contracts/v1/policy/policy_input_bundle_profile_v1.schema.json
  - ../../schemas/contracts/v1/policy/policy_decision.schema.json
  - ../../schemas/contracts/v1/policy/policy_decision_vocabulary.schema.json
  - ../../schemas/contracts/v1/policy/policy_evaluation_binding_v1.schema.json
  - ../decision/vocabulary.v1.json
  - ../../tools/validators/policy/README.md
  - ../../tools/validators/policy/validate_policy_input_bundle_profile_v1.py
  - ../../tools/validators/policy/validate_policy_decision_vocabulary.py
  - ../../tools/validators/policy/validate_policy_evaluation_binding_v1.py
  - ../../packages/policy-runtime/README.md
  - ../../.github/workflows/pass12-release-policy-v1.yml
  - ../../.github/workflows/policy-input-bundle-profile-v1.yml
  - ../../.github/workflows/policy-decision-vocabulary.yml
  - ../../.github/workflows/policy-evaluation-binding-v1.yml
  - ../../.github/workflows/policy-test.yml
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/doctrine/trust-membrane.md
  - ../../docs/architecture/contract-schema-policy-split.md
  - ../../control_plane/root_registry.yaml
  - ../../release/README.md
  - ../../.github/CODEOWNERS
  - ../../CONTRIBUTING.md
  - ../../.github/PULL_REQUEST_TEMPLATE.md
tags: [kfm, policy, bundles, manifest, rego, opa, pass12, policy-runtime, PolicyInputBundle, PolicyDecision, finite-outcomes, reason-codes, obligations, deterministic-build, digest, replay, fail-closed, release-gated, rollback, boundary-compact]
truth_posture: "CONFIRMED exact two-file documentation-only direct lane, canonical singular policy root, accepted ADR-0029 placement, one PROPOSED_INACTIVE Pass 12 packaging profile, its external deny-by-default Rego source, six native tests, four workflow-evaluated fixtures, checksum-pinned OPA 1.19.0 workflow, static broad policy-readiness hold, permissive parent PolicyInputBundle schema, restrictive inactive PolicyInputBundle profile with validator, two valid and three invalid PolicyDecision shape fixtures, inactive reason/obligation vocabulary, declared-only exact-byte evaluation binding, multiple profile-specific policy validators, and placeholder general policy runtime / PROPOSED executable bundle artifact, manifest, lock, deterministic builder, accepted evaluator, normalization, selector, signing, activation, replay, and rollback contracts / CONFLICTED Pass 12 engine-native boolean/set result versus canonical PolicyDecision, documentation-only bundle profile versus an executable bundle, and stale general schema-declared validator/policy paths / UNKNOWN accepted local owner, canonical executable bundle format, bundle instance, manifest instance, runtime selector, evaluator binding, production consumer, decision receipt, required-check coupling, deployment enforcement, and publication behavior"
notes:
  - "v0.3 reconciles the substantive v0.2 boundary against current main and preserves all thirty prior H2 sections."
  - "The Pass 12 child is a packaging profile README only; executable Rego remains under policy/rego and reusable fixtures remain under fixtures/."
  - "The dedicated Pass 12 workflow executes the named Rego source and native test under checksum-pinned OPA 1.19.0; the broad policy-test workflow remains a static readiness hold and does not establish a general evaluator."
  - "Profile-specific validators and workflows validate inactive declarations; the parent PolicyInputBundle and PolicyDecision schema-declared validators remain absent at their declared paths."
  - "This revision changes only policy/bundles/README.md and creates no policy behavior, bundle payload, selector, runtime, decision, receipt, release, deployment, or publication state."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Policy Bundles

`policy/bundles/`

> Governed boundary for immutable, reviewable, replayable policy bundle artifacts and their manifests. This lane may package accepted policy source for an approved evaluator, but it is not the policy runtime, input schema, decision contract, receipt store, release authority, or public trust path.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.3-informational)
![maturity](https://img.shields.io/badge/maturity-docs%2Bbounded__Rego-lightgrey)
![authority](https://img.shields.io/badge/authority-policy__bundle__boundary-6f42c1)
![outcomes](https://img.shields.io/badge/canonical__outcomes-ANSWER%20%7C%20ABSTAIN%20%7C%20DENY%20%7C%20ERROR-0b7285)
![default](https://img.shields.io/badge/default-fail__closed-critical)
![activation](https://img.shields.io/badge/directory__activation-forbidden-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status-and-evidence) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Repo fit](#repository-fit-and-directory-rules-basis) · [Bundle classes](#bundle-artifact-classes) · [Manifest](#minimum-bundle-manifest-contract) · [Identity](#identity-version-digest-and-canonicalization) · [Composition](#composition-and-dependency-closure) · [Inputs](#policy-input-binding) · [Decisions](#decision-vocabulary-and-normalization) · [Activation](#activation-selection-and-deployment) · [Lifecycle](#bundle-lifecycle-and-promotion) · [Supply chain](#build-and-supply-chain-controls) · [Reasons](#reason-codes-and-obligations) · [Audit](#audit-replay-receipts-and-retention) · [Sensitivity](#rights-sensitivity-and-data-minimization) · [Failure](#failure-behavior) · [Threats](#threat-model) · [Validation](#validation-and-test-matrix) · [Implementation](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Ledger](#no-loss-and-evidence-ledger) · [Changelog](#changelog) · [Rollback](#rollback-correction-and-supersession)

> [!IMPORTANT]
> **Document lifecycle:** draft `v0.3`<br>
> **Observed lane maturity:** two documentation files; one bounded Rego source/test profile is validated in adjacent responsibility lanes<br>
> **Authority:** policy-bundle packaging and manifest boundary only<br>
> **Runtime posture:** no accepted executable bundle format, bundle payload, manifest instance, general evaluator, active selector, deployed enforcement, or production consumer is established

> [!CAUTION]
> File presence is never activation. A valid archive, successful schema check, OPA-compatible directory, matching digest, or `ANSWER` decision does not authorize release or publication. Missing or stale bundle identity, input context, evidence, rights, sensitivity, review, evaluator integrity, reason-code mapping, obligation handling, release state, correction path, or rollback support must fail closed.

---

## Purpose

`policy/bundles/` is the canonical policy-root sublane for packaging reviewed policy source into an immutable evaluation unit and describing that unit with inspectable metadata.

The current `pass12-release-gate-v1/` child documents one proposed, inactive packaging profile. Its Rego source, native test, fixtures, and dedicated workflow are real repository artifacts in adjacent responsibility lanes, but no executable bundle payload is assembled here.

A future executable bundle may support:

- access gates;
- capability gates;
- consent and revocation gates;
- sensitivity and public-exposure gates;
- render and export gates;
- governed-AI answer gates;
- lifecycle promotion gates;
- release, correction, withdrawal, and rollback checks.

The lane exists to make the exact policy evaluated by a governed caller:

- identifiable;
- immutable;
- versioned;
- hashable;
- dependency-complete;
- evaluator-compatible;
- testable;
- reviewable;
- replayable;
- supersedable;
- withdrawable;
- rollback-safe.

It must not turn policy packaging into a second source of semantic truth. Policy source rules remain under their accepted `policy/` lanes. Contracts define meaning, schemas define shape, runtime helpers execute, receipts and proofs audit, release records authorize publication, and governed applications enforce public access.

[Back to top](#top)

---

## Authority level

**Policy-authoritative only for an accepted bundle's exact packaged rule content and manifest binding. Non-authoritative for every adjacent responsibility.**

| Concern | Authority in this lane |
|---|---|
| Policy source rules | **Packaging reference only.** Accepted source modules remain in reviewed policy lanes under `policy/`. |
| Bundle composition | **Potential authority after acceptance.** A reviewed manifest may bind exact source paths, dependencies, data documents, evaluator profile, and digest. No accepted instance is confirmed today. |
| Policy input meaning | **None.** [`PolicyInputBundle`](../../contracts/policy/policy_input_bundle.md) owns semantic meaning; its paired schema owns machine shape. |
| Policy decision meaning | **None.** [`PolicyDecision`](../../contracts/policy/policy_decision.md) and its paired schema own the canonical result surface. |
| Engine-native result | **Packaging/runtime interface only.** Lower-level `ALLOW`, `RESTRICT`, or `HOLD` values require explicit normalization. |
| Runtime execution | **None.** [`packages/policy-runtime/`](../../packages/policy-runtime/README.md) is the proposed executor/helper boundary. |
| Evidence | **None.** Evidence references and status may be inputs; bundles cannot create evidence closure. |
| Rights, consent, or sensitivity facts | **None.** Bundles evaluate supplied governed context; they do not discover or invent it. |
| Review approval | **None.** Review records and separation of duties remain external governed artifacts. |
| Release and publication | **None.** `release/` owns release state, correction, withdrawal, supersession, and rollback decisions. |
| Public API or UI behavior | **None.** Public clients use governed interfaces and cannot load or choose bundles directly. |
| Receipts and proofs | **None.** This lane may define receipt-ready metadata requirements but must not store emitted receipt or proof instances. |

A bundle is a frozen evaluation input, not a universal permission grant.

[Back to top](#top)

---

## Status and evidence

### Current repository state

| Surface | Status | Safe conclusion |
|---|---:|---|
| `policy/bundles/README.md` | **CONFIRMED** | This v0.2 baseline exists and defines a substantive proposed bundle boundary. |
| Complete direct lane | **CONFIRMED TWO FILES** | The recursive tree contains this README and `pass12-release-gate-v1/README.md`; both are documentation. |
| Pass 12 packaging profile | **CONFIRMED / PROPOSED_INACTIVE** | The child README names exact source, test, fixtures, and workflow, and explicitly grants no publication authority. It is not a bundle payload or manifest. |
| Pass 12 Rego source | **CONFIRMED BOUNDED EXECUTABLE SOURCE** | `policy/rego/release_gate_v1.rego` is deny-by-default and exposes `allow`, a deterministic `deny` set, and a decision object with sorted reasons. |
| Pass 12 native tests and fixtures | **CONFIRMED BOUNDED COVERAGE** | Six native Rego tests exist; the dedicated workflow evaluates one allow fixture and three denial fixtures. This is not complete policy coverage. |
| Pass 12 hosted workflow | **CONFIRMED COMMAND-BEARING DEFINITION** | Installs checksum-pinned OPA 1.19.0, checks formatting, runs native tests, verifies fixture polarity, and asserts three stable deny reasons. A workflow definition is not current-run or production evidence. |
| Canonical policy root | **CONFIRMED MIXED MATURITY** | `policy/` is the singular policy-source root. Its v0.3.1 README records one bounded Rego lane, multiple inactive profiles, and a general evaluator hold. |
| Directory governance | **CONFIRMED ACCEPTED** | ADR-0029 adopts Directory Rules v2; the root registry projects `policy/` as canonical for policy rules and bundles. |
| Parent `PolicyInputBundle` | **CONFIRMED PROPOSED PERMISSIVE STUB** | The parent schema requires only `id` and permits additional properties. |
| Explicit input profile v1 | **CONFIRMED PROPOSED_INACTIVE / FIXTURE_ONLY** | A closed schema, semantic validator, synthetic fixtures, tests, and read-only workflow check one bounded input profile without evaluating policy. |
| `PolicyDecision` schema and fixtures | **CONFIRMED PROPOSED SHAPE** | The schema permits only `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` across six families; two valid and three invalid shape fixtures are inventoried. |
| Decision vocabulary v1 | **CONFIRMED PROPOSED_INACTIVE** | A reviewed candidate registry contains nine reason codes and eight obligation codes with a validator, fixtures, tests, and workflow; it is not evaluator or consumer authority. |
| Evaluation binding v1 | **CONFIRMED PROPOSED_INACTIVE / DECLARED_ONLY** | The profile checks exact input/decision file digests and evaluator-declaration coherence; it proves no execution or decision authenticity. |
| Policy validators | **CONFIRMED PARTIAL** | Multiple profile-specific Python validators have focused tests and workflows. The parent schema-declared `validate_policy_input_bundle.py` and `tools/validators/validate_policy_decision.py` remain absent. |
| Policy runtime package | **CONFIRMED PLACEHOLDER** | `kfm-policy-runtime` remains version `0.0.0` and `core.py` is comment-only. |
| Broad `policy-test` workflow | **CONFIRMED STATIC READINESS HOLD** | It inventories the bounded Pass 12 lane and profile-validator support, rejects non-document bundle payloads, preserves the placeholder runtime hold, and evaluates no general policy. |
| Accepted executable bundle format | **UNKNOWN / NOT ESTABLISHED** | No accepted OPA bundle, archive, WASM package, or other executable bundle profile was established. |
| Active bundle selection | **UNKNOWN / NOT ESTABLISHED** | No allowlisted selector, activation record, deployment binding, or active bundle registry was established. |
| Receipt/proof linkage | **NEEDS VERIFICATION** | Declared-only bindings and documentation do not establish authenticated evaluation receipts or replay closure. |

### Current direct map

```text
policy/bundles/
├── README.md
└── pass12-release-gate-v1/
    └── README.md
```

The executable Pass 12 materials remain outside this directory by responsibility:

```text
policy/rego/release_gate_v1.rego
policy/rego/release_gate_v1_test.rego
fixtures/policy/release_gate_v1/*.json
.github/workflows/pass12-release-policy-v1.yml
```

### Evidence boundary

This README may state repository presence, inspected file content, and bounded validation wiring. It must not claim:

- an assembled or signed bundle;
- accepted bundle format or manifest;
- general or production policy evaluation;
- active bundle deployment or selector state;
- complete policy coverage;
- runtime compatibility or consumer enforcement;
- branch-protection or required-check enforcement;
- authenticated decision or reviewer authority;
- receipt emission, release approval, or public safety.

Those remain `UNKNOWN`, `NEEDS VERIFICATION`, or explicitly proposed until accepted artifacts, current-run evidence, runtime bindings, receipts, deployment records, and independent review prove them.

[Back to top](#top)

---

## Scope and bounded context

### In scope

This lane may govern the packaging contract for:

- an immutable policy bundle artifact;
- a bundle manifest;
- a source/dependency lock;
- a deterministic build receipt reference;
- a signature or attestation reference when accepted;
- a bundle family index;
- deprecation, supersession, withdrawal, and rollback pointers;
- documentation that explains bundle composition and safe selection.

### Out of scope

This lane does not own:

- policy runtime implementation;
- source rule authoring outside accepted policy child lanes;
- JSON Schema;
- semantic contracts;
- source data or lifecycle data;
- real policy inputs or emitted decisions as stored instances;
- receipts, proofs, or evidence bundles;
- release manifests;
- credentials or private evaluator configuration;
- arbitrary runtime bundle discovery;
- public-client bundle selection;
- generated claims.

### Non-collapse rules

Keep these objects distinct:

| Object | Meaning |
|---|---|
| Policy source module | Human-reviewed rule source under an accepted policy lane. |
| Bundle artifact | Immutable packaged evaluation unit built from exact source and dependency inputs. |
| Bundle manifest | Metadata binding identity, digest, source lineage, evaluator compatibility, tests, review, and rollback. |
| PolicyInputBundle | Explicit policy-relevant facts supplied for one evaluation. |
| Engine result | Evaluator-native result before canonical normalization. |
| PolicyDecision | Canonical finite result record. |
| DecisionEnvelope | Runtime transport and public-surface context. |
| Evaluation receipt | Audit record binding bundle, input, evaluator, result, and time. |
| ReleaseManifest | Release authority record for published contents. |
| ReviewRecord | Human or steward review artifact. |
| EvidenceBundle | Evidence closure supporting claims. |

No one object substitutes for another.

[Back to top](#top)

---

## What belongs here

| Material | Purpose | Minimum posture |
|---|---|---|
| `README.md` | Define this bundle boundary. | Preserve authority separation and current truth labels. |
| Bundle manifest instance | Bind immutable bundle identity and review state. | Schema-validated after a schema is accepted; no secrets; digest-pinned. |
| Immutable bundle artifact | Package exact reviewed policy modules and approved static data. | Deterministic build; content-addressed; no mutable dependencies. |
| Bundle lock | Pin module paths, source digests, dependency digests, evaluator requirements, and build profile. | Machine-readable; complete closure; no `latest`. |
| Bundle family index | Point to active, candidate, superseded, withdrawn, and rollback-safe bundle refs. | Pointer-only; cannot activate by directory presence. |
| Attestation/signature pointer | Bind external signature or provenance attestation. | Accepted trust root and verification process required. |
| Migration or deprecation note | Explain bundle-family transition. | Time-bounded, reversible, backlink-aware. |
| Synthetic examples | Explain manifest or mapping shape. | Clearly illustrative; no live selector or real sensitive values. |

Directory and filename conventions are `PROPOSED` until an accepted manifest schema and build process exist.

[Back to top](#top)

---

## What does not belong here

| Do not place here | Correct responsibility |
|---|---|
| Reusable evaluator or loader code | `packages/policy-runtime/` |
| API middleware, route handlers, serializers, or deployment code | Governed application/runtime roots |
| Semantic policy-object meaning | `contracts/policy/` |
| JSON Schema definitions | `schemas/contracts/v1/policy/` or an ADR-approved schema home |
| PolicyInputBundle instances containing real request context | Governed runtime or accepted receipt/input-record lane |
| Emitted PolicyDecision instances | Accepted receipt, proof, runtime, or governance record lane |
| EvidenceBundle or EvidenceRef authority | Evidence/proof roots |
| ReleaseManifest, PromotionDecision, CorrectionNotice, or RollbackCard | `release/` |
| Source descriptors or source registries | `data/registry/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | `data/` lifecycle roots |
| Production credentials, signing keys, tokens, private endpoints, or secret evaluator settings | Secret manager / deployment controls |
| Sensitive exact coordinates, living-person data, genomic data, archaeology details, infrastructure details, or restricted cultural knowledge | Restricted governed stores; never bundle examples |
| Mutable cache, temporary compiler output, or local workstation artifacts | Build cache/artifact roots outside policy authority |
| Generated prose presented as policy | Governed AI output remains non-authoritative |

[Back to top](#top)

---

## Repository fit and Directory Rules basis

Accepted ADR-0029 and Directory Rules v2 place normative policy rules and bundles under the singular `policy/` root. The root-registry projection records the same responsibility but is machine projection, not independent authority.

The complete bundle-lane file map and its bounded executable dependencies are:

```text
policy/
├── bundles/
│   ├── README.md
│   └── pass12-release-gate-v1/
│       └── README.md
└── rego/
    ├── README.md
    ├── release_gate_v1.rego
    ├── release_gate_v1_test.rego
    └── tiles_publish.rego

fixtures/policy/release_gate_v1/
├── allow_public.json
├── deny_missing_attestation.json
├── deny_missing_evidence.json
└── deny_missing_sensitivity.json

.github/workflows/pass12-release-policy-v1.yml
```

This is a relevant-surface map, not an exhaustive `policy/` inventory. The Pass 12 source remains source, the fixtures remain reusable synthetic inputs, CI remains orchestration, and the child README remains a packaging profile.

### Responsibility split

```text
policy source + bundle authority  -> policy/
semantic meaning                  -> contracts/
machine shape                     -> schemas/
runtime helper code               -> packages/
validation code                   -> tools/
fixtures and tests                -> fixtures/ + tests/
inputs, receipts, proofs, data    -> governed data roots
release/correction/rollback       -> release/
public enforcement                -> governed apps/APIs
```

### BOUNDARY_COMPACT responsibility signature

| Dimension | Boundary |
|---|---|
| Owns | Proposed bundle packaging, immutable identity, dependency closure, manifest expectations, and safe selection requirements. |
| Receives | Reviewed policy source references, accepted contracts/schemas, explicit evaluator requirements, synthetic validation evidence, and external review/release references. |
| Produces | Documentation today; a future accepted lane may produce immutable bundle payloads and manifests. |
| Must not own | Semantic object meaning, JSON Schema authority, evaluator/runtime code, request facts, decisions, receipts, release state, credentials, deployment, or public presentation. |
| Activation | Directory presence, valid Markdown, Rego success, or a passing workflow never activates a bundle. |
| Mutation and retention | Versioned Git history; future payloads require immutable identities, supersession, withdrawal, replay, and rollback retention. |
| Exposure | Repository-public documentation and source; operating selection remains internal and governed. |
| Correction | Revert or forward-fix documentation; correct active policy through separately governed withdrawal, supersession, reevaluation, cache invalidation, and release correction. |

### Placement constraints

- `policy/` is singular and canonical.
- `policies/`, if present, must remain compatibility-only unless a successor accepted decision changes that posture.
- Bundle artifacts must not be copied into `packages/policy-runtime/` as a second policy authority.
- Bundle manifests must not be placed in `release/` merely because a bundle is deployed; release manifests and policy bundle manifests are different object families.
- Schema files must not be placed beside bundle instances.
- Emitted evaluation receipts must not be stored as bundle source.
- Domain-specific policies may be included by reference, but the bundle does not transfer domain ownership into this directory.
- Creating a parallel `bundles/` root or independent compatibility authority requires a governed path decision and, when triggered, an accepted ADR and migration plan.

[Back to top](#top)

---

## Bundle artifact classes

The following classes are `PROPOSED` and must remain distinct.

### Source bundle

A deterministic collection of reviewed policy modules and approved non-secret policy data.

May include:

- Rego modules or equivalent policy source;
- static reason-code or obligation data if policy-owned;
- package namespace metadata;
- dependency declarations.

Must not include:

- live request facts;
- source payloads;
- secrets;
- release records;
- receipt instances;
- mutable network dependencies.

### Compiled bundle

A deterministic compiled form such as WASM or an engine-specific package.

Requirements:

- exact compiler/evaluator toolchain version;
- source bundle digest;
- compiled artifact digest;
- reproducible or independently verifiable build;
- semantic-equivalence tests;
- rollback to a source-backed prior version.

A compiled bundle cannot become the only retained policy source.

### Bundle manifest

The identity and governance record for one immutable artifact.

### Bundle lock

The complete dependency closure needed to rebuild or verify the artifact.

### Bundle family index

A pointer-oriented record that distinguishes candidate, active, superseded, withdrawn, and rollback-safe versions. It must not be a mutable unreviewed `latest` alias.

[Back to top](#top)

---

## Minimum bundle manifest contract

No accepted bundle-manifest schema was surfaced. The fields below are `PROPOSED` requirements for the next contract/schema pass.

### Identity and status

| Field | Requirement |
|---|---|
| `bundle_id` | Stable bundle-family identifier. |
| `bundle_version` | Immutable semantic or release version; never inferred from directory mtime. |
| `bundle_status` | Proposed finite status such as `draft`, `candidate`, `reviewed`, `active`, `deprecated`, `superseded`, or `withdrawn`. |
| `artifact_ref` | Repository or artifact-store reference to the immutable artifact. |
| `artifact_digest` | Content digest using an accepted algorithm and canonical representation. |
| `manifest_digest` | Digest of the canonical manifest, excluding or normalizing signature fields by an accepted profile. |
| `created_at` | Original build time; must not be rewritten on replay. |
| `supersedes` | Prior bundle ref when applicable. |
| `rollback_target` | Known-good immutable bundle ref or explicit disabled state. |

### Source and dependency lineage

| Field | Requirement |
|---|---|
| `source_paths` | Exact reviewed policy source paths included in the build. |
| `source_digests` | Digest for each included source file or source tree. |
| `dependency_lock_ref` | Immutable dependency closure. |
| `policy_families` | Gate families implemented by the bundle. |
| `module_namespaces` | Allowed package/module namespaces. |
| `static_data_paths` | Explicit approved policy data documents, if any. |
| `excluded_paths` | Optional explicit exclusions when the build root is broader than the bundle. |
| `build_profile` | Deterministic packaging/canonicalization profile. |

### Evaluator compatibility

| Field | Requirement |
|---|---|
| `evaluator_family` | OPA, WASM runtime, or another accepted engine. |
| `evaluator_version_range` | Bounded compatibility; no unpinned universal support claim. |
| `entrypoints` | Explicit policy entrypoints. |
| `capabilities_ref` | Engine capabilities/built-ins profile when material. |
| `timeout_profile` | Bounded runtime timeout and failure semantics. |
| `fail_closed` | Must be `true` for trust-bearing use. |

### Contracts and schemas

| Field | Requirement |
|---|---|
| `policy_input_contract_ref` | `PolicyInputBundle` semantic contract or accepted profile. |
| `policy_input_schema_ref` | Exact schema `$id`, path, and digest. |
| `policy_decision_contract_ref` | `PolicyDecision` semantic contract. |
| `policy_decision_schema_ref` | Exact schema `$id`, path, and digest. |
| `engine_result_mapping_ref` | Versioned mapping from engine-native results to canonical outcomes. |
| `reason_code_registry_ref` | Versioned stable reason-code vocabulary. |
| `obligation_registry_ref` | Versioned obligation vocabulary and interpreter contract. |

### Validation and review

| Field | Requirement |
|---|---|
| `fixture_refs` | Synthetic valid, deny, restrict, hold, abstain, error, stale, and adversarial fixtures. |
| `test_refs` | Exact tests and expected results. |
| `validation_report_refs` | Results for schema, syntax, semantic, determinism, replay, and security checks. |
| `review_refs` | Policy, security, domain, rights, sensitivity, and release-adjacent reviews as applicable. |
| `required_review_roles` | Roles required; identities remain in review records rather than mutable prose. |
| `approved_at` | Review completion time if the bundle is reviewed or active. |

### Deployment and rollback

| Field | Requirement |
|---|---|
| `allowed_consumers` | Explicit component identities permitted to select the bundle. |
| `allowed_operations` | Bounded operations and gate families. |
| `activation_ref` | External governed activation/deployment record. |
| `deactivation_ref` | External safe-stop or withdrawal record when applicable. |
| `retention_until` | Minimum replay/audit retention. |
| `correction_ref` | Correction or supersession lineage. |

The manifest must not contain secret keys, raw sensitive inputs, or release approval.

[Back to top](#top)

---

## Identity, version, digest, and canonicalization

### Deterministic identity

A bundle identity should bind:

```text
bundle family
+ immutable version
+ source/dependency closure
+ build profile
+ evaluator compatibility
+ artifact digest
```

A directory name, Git branch, tag named `latest`, deployment label, or human-readable version alone is insufficient.

### Digest posture

An accepted implementation should record at least:

- source tree or per-file digests;
- dependency lock digest;
- bundle artifact digest;
- manifest digest;
- input bundle hash for each evaluation;
- evaluator/build toolchain identity;
- decision or receipt hash where the accepted receipt contract permits it.

### Canonicalization

Before hashing, define:

- path normalization;
- line-ending normalization;
- archive member ordering;
- timestamp normalization or exclusion;
- file-mode normalization;
- symlink policy;
- compression profile;
- JSON canonicalization profile;
- signature-field treatment;
- excluded temporary files.

Without a canonical build profile, two archives can represent the same rules but produce different digests, or different rules can be hidden behind mutable metadata.

### Version rules

- Do not overwrite an immutable version.
- Do not mutate a superseded artifact.
- Do not use branch names as runtime versions.
- Do not let a tag move without an auditable correction.
- A rebuild with changed bytes gets a new digest even when semantic version remains under correction review.
- A semantic change requires a new bundle version and review.
- A dependency or evaluator-compatibility change requires revalidation and may require a new version.

[Back to top](#top)

---

## Composition and dependency closure

### Explicit composition

A bundle builder must use an allowlisted manifest or lock. It must not recursively package everything beneath `policy/` by default.

Explicit composition prevents:

- test modules entering production bundles;
- compatibility paths becoming authority;
- experimental rules becoming active;
- domain rules leaking into unrelated gates;
- duplicate package namespaces;
- shadowed data documents;
- secrets or local files entering an archive;
- cross-family rule conflicts.

### Namespace and entrypoint controls

Every accepted bundle must declare:

- module/package namespaces;
- entrypoints;
- policy families;
- allowed built-ins/capabilities;
- static data roots;
- dependency order or conflict behavior;
- undefined-result handling;
- multiple-result handling.

Namespace collision or ambiguous entrypoint resolution must fail the build.

### Static policy data

Static data documents may be bundled only when:

- policy owns the data;
- the data is non-secret and appropriate for repository storage;
- the source and digest are explicit;
- rights and sensitivity posture are reviewed;
- the data is immutable for the bundle version;
- updates require rebuild and review.

Source registries, EvidenceBundles, user context, runtime environment, and release state must not be copied into a bundle as stale hidden facts.

### Cross-domain composition

When one bundle composes multiple domain policies:

- preserve each domain's ownership;
- preserve most-restrictive sensitivity and rights behavior;
- avoid one domain's permissive rule overriding another domain's denial;
- require explicit precedence or aggregation semantics;
- test joins and indirect reconstruction;
- identify the policy family returned for each gate.

[Back to top](#top)

---

## Policy input binding

A governed caller should construct an explicit [`PolicyInputBundle`](../../contracts/policy/policy_input_bundle.md) before evaluation.

### Current contract reality

The semantic parent expects operation, audience, object, evidence, source, rights, sensitivity, review, release, and evaluator context. Its current schema, however:

- requires only `id`;
- optionally shapes `spec_hash` and `version`;
- allows arbitrary additional properties;
- remains `PROPOSED`; and
- still declares validator and policy paths that are absent.

The additive [explicit context profile v1](../../contracts/policy/policy_input_bundle_profile_v1.md) closes one bounded shape for `ANSWER`, `RENDER`, `EXPORT`, `PROMOTE`, and `RELEASE` inputs. Its validator checks sorted references, evidence/citation coherence, public rights and sensitivity, release prerequisites, fail-closed evaluator declaration, and false authority flags.

That profile is `PROPOSED_INACTIVE` and `FIXTURE_ONLY`. Passing it means the declared input is coherent enough for a future evaluator boundary; it does not evaluate a rule or authorize an outcome.

Therefore:

- parent-schema validity alone is insufficient;
- the profile must not be described as the universal accepted input shape;
- callers and policy modules must not silently disagree on field names;
- missing facts remain explicitly unresolved;
- hidden fetches are forbidden; and
- every active evaluator profile must version and bind its exact input contract.

### Required evaluator binding

A consequential evaluation should bind:

```text
PolicyInputBundle id/hash
+ bundle id/version/digest
+ manifest digest
+ evaluator family/version
+ entrypoint
+ evaluation time
+ engine result
+ canonical PolicyDecision
+ receipt/proof target
```

The inactive [Policy Evaluation Binding v1](../../contracts/policy/policy_evaluation_binding_v1.md) currently checks only exact input/decision file SHA-256 values and equality of a declared `bundle_ref` and `bundle_version`. Its `execution_mode` is `DECLARED_ONLY` and all authority flags remain false. It does not prove that the named bundle exists, that an evaluator ran, or that the decision is authentic.

The current `PolicyDecision` schema does not carry all replay fields and rejects undeclared properties. Carry additional replay metadata only in an accepted envelope, receipt, binding revision, or future schema—not by extending an instance ad hoc.

### Input immutability

After evaluation:

- do not mutate the input and reuse the old decision;
- create a new input id/hash for changed context;
- preserve prior input and decision references for audit;
- re-evaluate when evidence, rights, sensitivity, release state, bundle, or evaluator changes.

[Back to top](#top)

---

## Decision vocabulary and normalization

### Two distinct vocabularies

KFM currently documents two general layers:

1. **Engine-native or internal policy result classes**
   `ALLOW | RESTRICT | HOLD | DENY | ABSTAIN | ERROR`
2. **Canonical `PolicyDecision.outcome` values confirmed by schema**
   `ANSWER | ABSTAIN | DENY | ERROR`

The current Pass 12 Rego profile uses a narrower engine-native surface: Boolean `allow`, a set-valued `deny`, and `decision = {profile, allow, deny_reasons}`. Its child README explicitly says the result is not normalized into `PolicyDecision`. Neither native form may be stored or advertised as a canonical decision without an accepted mapping and authenticated evaluation boundary.

The inactive `policy/decision/vocabulary.v1.json` registry supplies candidate reason and obligation codes for the canonical decision contract. Fixture validation of that registry does not activate it.

### Required normalization

The following general mapping remains `PROPOSED` until accepted and implemented:

| Engine-native result | Canonical outcome | Required handling |
|---|---|---|
| `ALLOW` | `ANSWER` | Proceed only for the evaluated operation and audience; preserve citations, obligations, and release gates. |
| `RESTRICT` | `ANSWER` | `obligations` encode every enforceable restriction; fail closed if any required interpreter is unavailable. |
| `HOLD` | `ABSTAIN` | Preserve pending review, maturity, or support without turning uncertainty into permission. |
| `ABSTAIN` | `ABSTAIN` | Preserve unresolved support and do not turn it into a denial or answer. |
| `DENY` | `DENY` | Preserve a public-safe reason code without exposing protected facts. |
| `ERROR` | `ERROR` | Preserve evaluator/process failure; never normalize it to `ANSWER`. |

For Pass 12, `allow: true` must not be mapped mechanically to `ANSWER`. A future adapter must also bind the exact input, source/bundle identity, evaluator, entrypoint, denial set, review context, and receipt target, and it must preserve the profile's explicit non-release boundary.

### Canonical policy family

The current `PolicyDecision.policy_family` enum is:

- `promotion`;
- `access`;
- `render`;
- `capability`;
- `consent`;
- `sensitivity`.

`bundle` and `release` are not policy families in the current schema. Bundle integrity or selection failure must map to the family of the evaluated gate under an accepted contract; do not emit a schema-invalid family merely because packaging failed.

### Composition rules

When multiple policy evaluations apply:

- do not let `ANSWER` override `DENY`;
- do not let an empty or undefined result become `ANSWER`;
- preserve `ERROR` as process failure;
- preserve `ABSTAIN` when evidence or authority is unresolved;
- apply the most restrictive unsatisfied obligation;
- record which family and exact bundle/evaluator identity produced each decision; and
- use an accepted aggregation contract rather than free-text precedence.

A safe default proposal is:

```text
ERROR or DENY blocks
ABSTAIN prevents authoritative answer/publication
ANSWER proceeds only when every required obligation is enforceable
```

This remains proposed until accepted in contracts, policy, tests, runtime, consumers, and receipts.

[Back to top](#top)

---

## Activation, selection, and deployment

### Directory presence is not activation

The runtime must not:

- scan `policy/bundles/` and pick the newest file;
- infer activity from filename order;
- follow a mutable `latest` symlink;
- choose a bundle from request parameters;
- allow a public client to supply a repository path or digest;
- silently fall back to an older bundle;
- fetch a bundle from an unapproved network location;
- activate a bundle because CI built it.

### Allowed selection posture

A governed deployment should select an immutable bundle through an external reviewed binding that includes:

- consumer identity;
- environment or deployment identity;
- bundle id/version/digest;
- manifest digest;
- evaluator profile;
- activation time;
- authorizing review/deployment reference;
- rollback target;
- expiration or reevaluation trigger.

### Public clients

Public, ordinary UI, map, export, and AI clients:

- do not enumerate bundles;
- do not select bundle versions;
- do not provide policy source paths;
- do not bypass the governed API;
- receive only policy-safe outcomes and bounded explanations.

### Staging

Candidate bundles may run in:

- offline validation;
- no-network fixtures;
- shadow evaluation;
- deterministic replay;
- non-authoritative comparison.

Shadow evaluation must not affect public behavior unless a separately reviewed activation changes the selected bundle.

[Back to top](#top)

---

## Bundle lifecycle and promotion

Bundle authoring status and deployment state must remain distinct.

### Proposed artifact lifecycle

| State | Meaning | Selection posture |
|---|---|---|
| `draft` | Source, manifest, or build profile is incomplete. | Never selected. |
| `candidate` | Immutable artifact built and validation-ready. | Offline/shadow only. |
| `reviewed` | Required reviews complete for the artifact and manifest. | Eligible for staged activation, not automatically active. |
| `active` | External governed deployment selects this exact digest. | Allowed only for listed consumers/operations. |
| `deprecated` | Still replayable but not selected for new deployments. | Existing use requires explicit bounded plan. |
| `superseded` | Replaced by a reviewed successor. | Retain for audit and rollback analysis. |
| `withdrawn` | Known unsafe, invalid, compromised, or prohibited. | Must not execute. |

These statuses are `PROPOSED`; no accepted manifest schema currently enforces them.

### Governed promotion sequence

```text
policy source review
        ↓
explicit bundle manifest + dependency lock
        ↓
deterministic build
        ↓
syntax/schema/semantic/security tests
        ↓
digest + validation report
        ↓
policy/security/domain review
        ↓
candidate shadow/replay
        ↓
external activation decision
        ↓
runtime selection by immutable digest
        ↓
evaluation receipts + monitoring
```

Promotion is a governed state transition, not a file move from `candidate/` to `active/`.

### Separation of duties

For trust-significant bundles, prefer separation among:

- rule author;
- bundle builder;
- policy reviewer;
- security/sensitivity reviewer;
- deployment activator;
- release reviewer;
- rollback operator.

One person or automation may perform multiple duties in an early-stage repository, but the concentration must be explicit and reviewable rather than hidden.

[Back to top](#top)

---

## Build and supply-chain controls

### Deterministic build

A bundle build should:

1. start from a pinned repository commit;
2. use an explicit source allowlist;
3. validate every source path;
4. reject symlinks or handle them by an accepted policy;
5. reject path traversal and duplicate archive members;
6. normalize file order, metadata, and line endings;
7. include a complete dependency lock;
8. run no-network by default;
9. produce artifact and manifest digests;
10. generate a validation report;
11. compare a second build when reproducibility is required.

### Toolchain pinning

Record:

- builder version;
- evaluator/compiler version;
- capability set;
- JSON canonicalization version;
- archive/compression profile;
- schema versions;
- test harness version;
- operating assumptions that affect bytes or semantics.

### Signatures and attestations

Signatures are `NEEDS VERIFICATION`, not assumed.

Before signing is treated as a gate, define:

- trust root;
- key custody;
- signer authorization;
- signature format;
- what bytes are signed;
- key rotation;
- revocation;
- verification failure behavior;
- offline replay support.

A signature proves binding to a key under a process. It does not prove policy correctness, complete inputs, or release safety.

### External bundles

An externally produced bundle must not enter active use without:

- source/provenance evidence;
- rights to use and redistribute;
- malware/archive inspection;
- dependency inventory;
- digest verification;
- evaluator compatibility checks;
- policy and security review;
- local synthetic tests;
- rollback target.

[Back to top](#top)

---

## Reason codes and obligations

### Reason codes

Reason codes should be stable, versioned, public-safe, gate-specific where necessary, separable from protected detail, fixture-covered, and mapped to bounded explanations.

A real candidate registry now exists at [`policy/decision/vocabulary.v1.json`](../decision/vocabulary.v1.json). It is `PROPOSED_INACTIVE` and currently contains nine candidate reason codes:

```text
CONSENT_REQUIRED
EVIDENCE_STALE
EVIDENCE_UNRESOLVED
OPERATION_ALLOWED_WITH_OBLIGATIONS
POLICY_BUNDLE_UNAVAILABLE
POLICY_INPUT_INCOMPLETE
PUBLIC_PRECISION_UNSAFE
RIGHTS_UNKNOWN
SENSITIVITY_UNRESOLVED
```

The Pass 12 Rego profile separately emits ten engine-native denial codes, including `MISSING_EVIDENCE`, `MISSING_SENSITIVITY_REVIEW`, and `MISSING_REQUIRED_ATTESTATION`. Those codes are not automatically entries in the canonical registry. A future normalization contract must resolve naming, outcome, family, public-safety, versioning, and compatibility explicitly.

Additional bundle/runtime failure codes such as digest mismatch, invalid manifest, unsupported evaluator, incomplete dependency closure, timeout, undefined result, or multiple results remain proposed until registered and tested.

### Obligations

The inactive vocabulary currently contains eight candidate obligation codes:

```text
ATTACH_CITATIONS
ATTACH_RIGHTS_NOTICE
DELAY_PUBLICATION
GENERALIZE_GEOMETRY
REDACT_EXACT_LOCATION
REQUIRE_STEWARD_REVIEW
VERIFY_ROLLBACK_TARGET
WITHHOLD_EXPORT
```

The additive `PolicyObligationSet` and `PolicyObligationReduction` profiles provide deterministic fixture-only shape and reduction evidence. They do not prove that an accepted bundle issued an obligation or that a consumer enforced one.

Before any obligation is active:

- define exact semantics and versioning;
- identify every responsible interpreter;
- define success, failure, ordering, and composition;
- test supported and unsupported consumers;
- bind enforcement evidence and correction behavior;
- keep logs free of protected values; and
- fail closed when a caller cannot enforce the obligation.

`RESTRICT` must not disappear during normalization: it becomes `ANSWER` only when all restrictions are represented by complete, enforceable obligations under an accepted mapping.

[Back to top](#top)

---

## Audit, replay, receipts, and retention

### Minimum replay record

A consequential evaluation should be reconstructable from:

- policy input id/hash;
- object, operation, audience, and gate context;
- bundle id/version/digest;
- manifest digest;
- source/dependency lock digest;
- evaluator family/version/capabilities;
- entrypoint;
- evaluation time;
- engine-native result;
- normalization profile;
- canonical PolicyDecision id/outcome/reasons/obligations;
- review or release refs when material;
- correction/supersession lineage.

### Receipt boundary

This lane does not store evaluation receipts.

An accepted receipt should reference the immutable bundle and input rather than embedding:

- full policy source;
- raw sensitive input;
- secret evaluator configuration;
- protected location detail;
- private review notes.

### Decision schema limitation

The current `PolicyDecision` schema has no fields for:

- bundle digest;
- input hash;
- evaluator version;
- entrypoint;
- prior decision;
- expiration;
- receipt ref.

Because additional properties are forbidden, those fields require:

- an accepted `DecisionEnvelope`;
- a separate evaluation receipt;
- or a reviewed schema revision.

Do not break schema conformance by appending convenient replay fields ad hoc.

### Retention

Retain enough material to:

- reproduce consequential decisions;
- explain a denial or abstention;
- verify a bundle was not withdrawn at evaluation time;
- compare superseding policy;
- support correction and rollback;
- investigate exposure incidents.

Retention periods, restricted access, and deletion rules remain `NEEDS VERIFICATION`.

[Back to top](#top)

---

## Rights, sensitivity, and data minimization

### Bundle content

Bundles must not contain:

- credentials;
- source-system tokens;
- private endpoints;
- raw personal records;
- DNA/genomic data;
- exact rare-species locations;
- archaeological site detail;
- sensitive infrastructure detail;
- restricted cultural knowledge;
- source payloads used as hidden facts;
- reversible redaction secrets.

### Policy inputs

Bundles evaluate supplied context. They must not:

- query RAW or canonical stores directly;
- fetch missing rights or evidence from the network;
- infer public status from absence;
- reconstruct sensitive detail;
- log complete sensitive inputs;
- downgrade a sensitivity class;
- treat generalized data as exact;
- treat an anonymized label as proof of non-reidentifiability.

### Most-restrictive composition

When rights, sensitivity, consent, access, and release policies overlap:

- apply the strongest unresolved restriction;
- preserve abstention for missing evidence;
- preserve denial for explicit prohibition;
- require new review after a join changes reconstruction risk;
- keep public explanation separate from restricted diagnostic detail.

### Policy data updates

Static allowlists, denylists, thresholds, or classifications included in a bundle are policy source changes. They require:

- source and authority explanation;
- rights/sensitivity review;
- version and digest update;
- regression tests;
- correction/rollback plan.

[Back to top](#top)

---

## Failure behavior

| Condition | Safe disposition |
|---|---|
| No bundle selected | `ERROR` or gate-appropriate `ABSTAIN`; never implicit answer. |
| Bundle path exists but no accepted manifest | Reject selection. |
| Artifact digest mismatch | `ERROR`; quarantine/withdraw candidate and investigate. |
| Manifest digest mismatch | `ERROR`; do not load. |
| Bundle is `withdrawn` | `DENY` or `ERROR` according to gate contract; never fall back silently. |
| Bundle is stale or superseded | Re-evaluate against accepted selection policy; preserve old decision for audit. |
| Evaluator family/version unsupported | `ERROR`; fail closed. |
| Entrypoint missing or undefined | `ERROR`; no default allow. |
| Multiple ambiguous results | `ERROR`; require explicit aggregation. |
| Policy input schema passes but semantic context is incomplete | `ABSTAIN`, `DENY`, or `ERROR` according to gate; schema validity is insufficient. |
| Evidence unresolved | `ABSTAIN`; do not invent support. |
| Rights or sensitivity unknown | `ABSTAIN` or `DENY`; do not infer permission. |
| Explicit prohibition | `DENY`. |
| Review pending | Engine `HOLD` normalized to canonical `ABSTAIN` with safe reasons/obligations. |
| Restriction required and caller supports all obligations | Engine `RESTRICT` normalized to `ANSWER` with obligations. |
| Caller cannot enforce an obligation | `DENY` or `ERROR`; never drop the obligation. |
| Evaluator timeout/crash | `ERROR`; record receipt-ready failure metadata. |
| Receipt sink unavailable | Apply gate-specific fail-closed rule for consequential operations; do not claim auditability. |
| Rollback target missing | Do not activate the new bundle. |
| Network required during validation | Fail unless an explicitly governed, recorded exception exists. |

[Back to top](#top)

---

## Threat model

| Threat | Control |
|---|---|
| Mutable `latest` selector | Immutable digest selection plus reviewed activation record. |
| Directory auto-discovery | Explicit allowlisted bundle ref; file presence is inert. |
| Shadow policy path | Canonical singular `policy/`; compatibility paths frozen and drift-checked. |
| Archive path traversal | Reject absolute paths, `..`, duplicate members, and unsafe symlinks. |
| Namespace collision | Validate unique package/module namespaces and entrypoints. |
| Test rule packaged as production | Explicit source allowlist and build exclusions. |
| Hidden data document changes policy | Lock and digest every policy data document. |
| Non-deterministic build | Canonicalization profile and reproducibility check. |
| Compiler/evaluator drift | Pin and record toolchain/capabilities. |
| Stale decision reused after policy change | Bind decisions/receipts to bundle digest and input hash. |
| `RESTRICT` obligation dropped | Typed obligation registry and caller conformance test. |
| `HOLD` represented as public success | Normalize to `ABSTAIN`, never `ANSWER`. |
| Engine error converted to allow | Preserve `ERROR`; fail closed. |
| Public client chooses weaker bundle | Bundle selection inaccessible to public request parameters. |
| Sensitive values leak in reasons/logs | Public-safe reason codes, structured restricted diagnostics, data minimization. |
| Compromised signing key | Rotation, revocation, revalidation, and withdrawal process. |
| Withdrawn bundle remains cached | Cache invalidation keyed by selection state and digest. |
| Rollback reintroduces known vulnerability | Rollback target must remain reviewed, compatible, and not withdrawn. |

[Back to top](#top)

---

## Validation and test matrix

### Documentation validation

For this README:

- one H1;
- balanced KFM Meta Block;
- balanced fenced blocks;
- no trailing whitespace;
- unique heading anchors;
- resolvable relative links;
- no real policy secrets or sensitive inputs;
- explicit truth labels;
- final newline.

### Bundle build validation

| Check | Expected result |
|---|---|
| Manifest shape | Accepted schema passes; unknown safety-relevant fields fail. |
| Source allowlist | Every packaged member is declared. |
| Dependency closure | No undeclared import/data dependency. |
| Namespace integrity | No package or entrypoint collision. |
| Archive safety | No traversal, unsafe symlink, duplicate member, or device file. |
| Determinism | Repeated clean build yields the accepted digest. |
| Digest verification | Artifact and manifest digests match. |
| Toolchain compatibility | Evaluator/compiler profile is supported. |
| No-network | Build and tests pass without live fetches. |
| Secret scan | No credential, token, key, or private endpoint. |
| Sensitive-data scan | No real protected input or reconstruction clue. |

### Policy behavior validation

Minimum synthetic cases:

- unconstrained allowed operation;
- allowed operation with citation obligation;
- restricted geometry with generalization obligation;
- restricted export with block-export obligation;
- explicit deny;
- pending steward review;
- missing evidence;
- unknown rights;
- unresolved sensitivity;
- invalid input shape;
- semantically incomplete but schema-valid input;
- missing bundle;
- digest mismatch;
- stale/superseded bundle;
- withdrawn bundle;
- unsupported evaluator;
- missing entrypoint;
- undefined result;
- multiple results;
- timeout/error;
- unsupported obligation;
- correction and rollback replay.

### Canonical outcome validation

Tests must prove:

- `ALLOW -> ANSWER`;
- `RESTRICT -> ANSWER` with non-empty enforceable obligations;
- `HOLD -> ABSTAIN`;
- `ABSTAIN -> ABSTAIN`;
- `DENY -> DENY`;
- `ERROR -> ERROR`;
- no canonical `ALLOW`, `RESTRICT`, or `HOLD` outcome is emitted;
- no invalid `policy_family: bundle` is emitted;
- `ANSWER` cannot bypass release or evidence gates.

### Current CI reality

The current CI posture is split:

| Surface | Confirmed behavior | Limit |
|---|---|---|
| `pass12-release-policy-v1` | Downloads checksum-pinned OPA 1.19.0; formats and tests the named Rego source; evaluates four fixtures; checks three stable deny reasons | One proposed inactive release-gate profile only; no bundle assembly, canonical decision, release, or publication |
| `policy-test` OPA readiness job | Inventories all Rego, requires the sole native-test profile and its dedicated workflow, rejects non-document bundle payloads, verifies the placeholder runtime, and preserves the `make policy` TODO hold | Static readiness only; evaluates no general policy and proves no active evaluator |
| `policy-test` fixture job | Inventories two valid and three invalid `PolicyDecision` shape fixtures and the common harness | Shape-only; no dedicated parent validator, bundle identity, reason/obligation semantics, or evaluated decision |
| Profile-specific workflows | Run deterministic validators and fixtures for inactive input, vocabulary, binding, obligation, and related profiles | Validator results are not policy outcomes, bundle activation, or runtime enforcement |

A green run may therefore prove the exact bounded command or invariant it reports. It does not by itself prove:

- an executable bundle archive or manifest;
- deterministic bundle assembly or digest reproducibility;
- accepted evaluator selection;
- canonical outcome normalization;
- obligation enforcement by consumers;
- authenticated decision receipts;
- production deployment, replay, rollback, release, or publication.

[Back to top](#top)

---

## Smallest sound implementation sequence

The repository has completed parts of a fixture-first slice, but executable bundle activation remains held. The smallest dependency-ordered sequence is:

1. **Accept the executable bundle format and evaluator.**
   OPA directory/tar bundle, WASM, or another profile needs an explicit decision, capability contract, provenance, and rollback.
2. **Define and accept the semantic bundle-manifest contract.**
3. **Add a restrictive manifest schema, fixtures, validator, and tests.**
4. **Reconcile the existing Pass 12 packaging profile.**
   Bind exact `release_gate_v1.rego` and dependency digests without moving source authority into this lane.
5. **Version the engine-result-to-`PolicyDecision` mapping.**
   The current declared-only evaluation binding is provenance scaffolding, not execution evidence.
6. **Review the inactive reason and obligation vocabulary.**
   Accept, revise, or supersede it; define consumer interpreters and compatibility.
7. **Add a deterministic builder and complete lock.**
8. **Build one synthetic immutable bundle candidate.**
9. **Expand negative coverage.**
   Include malformed input, undefined or multiple results, stale/withdrawn bundle, digest mismatch, unsupported evaluator, unsupported obligation, timeout, and replay/correction cases.
10. **Close validator gaps.**
    Keep profile-specific validators; reconcile the missing parent `PolicyInputBundle` and `PolicyDecision` validator declarations.
11. **Graduate broad CI deliberately.**
    Preserve the readiness hold until repository-wide bundle, evaluator, manifest, fixture, and normalization checks exist.
12. **Add shadow evaluation and authenticated receipts.**
13. **Add reviewed activation, deactivation, correction, and rollback records.**
14. **Bind governed consumers and caches to immutable identities.**
15. **Promote only after acceptance gates pass.**

The first executable candidate should remain a thin, synthetic, reversible slice rather than a repository-wide policy rewrite.

[Back to top](#top)

---

## Definition of done

### Documentation boundary

- [x] Canonical root and adjacent authority boundaries are explicit.
- [x] Complete current direct-lane and Pass 12 dependency maps are recorded.
- [x] Current repository maturity is separated from proposal.
- [x] Pass 12 engine-native output and canonical decision vocabulary are separated.
- [x] Bounded OPA execution, static readiness, fixture validators, and placeholder runtime are qualified independently.
- [x] No executable bundle, evaluator, selector, receipt, deployment, release, or publication maturity is overclaimed.
- [x] Failure, threat, replay, correction, supersession, and rollback posture remains explicit.
- [x] All thirty prior H2 sections and their substantive doctrine are retained.

### First executable candidate bundle

- [ ] Accepted owners and independent reviewers are assigned.
- [ ] Bundle format, builder, evaluator, capabilities, and entrypoints are accepted.
- [ ] Semantic bundle-manifest contract exists.
- [ ] Restrictive bundle-manifest schema exists.
- [ ] Immutable version and digest rules are enforced.
- [ ] Complete source/dependency lock exists.
- [ ] Deterministic clean build passes.
- [ ] Artifact and manifest digest verification passes.
- [ ] The inactive input profile is accepted or superseded for the exact evaluator.
- [ ] `PolicyDecision` normalization passes the current schema through an accepted mapping.
- [ ] The inactive reason-code vocabulary is accepted or superseded.
- [ ] Obligation vocabulary and all required caller interpreters are accepted.
- [ ] Valid, invalid, deny, restrict, hold, abstain, error, stale, withdrawn, and adversarial cases pass.
- [ ] Parent validator declarations and implementations agree.
- [ ] No-network, secret, archive-safety, and sensitive-data checks pass.
- [ ] Broad bundle/evaluator CI runs meaningful checks beyond static readiness.
- [ ] Policy, security, domain, rights, sensitivity, runtime, and release-adjacent reviews close as applicable.
- [ ] Shadow/replay behavior is verified.
- [ ] External activation binding is immutable and auditable.
- [ ] Evaluation receipts bind input, bundle, evaluator, entrypoint, result, and decision.
- [ ] Rollback target is present, reviewed, compatible, and not withdrawn.
- [ ] Public clients cannot enumerate, upload, select, or bypass bundles.

The current Pass 12 profile partially supplies source, native tests, four workflow-evaluated fixtures, and a dedicated pinned-OPA workflow. It does not satisfy the executable bundle checklist.

### Active bundle

- [ ] Deployment selects an immutable digest.
- [ ] Activation and deactivation records exist.
- [ ] Monitoring covers errors, abstentions, denials, unsupported obligations, and stale selection.
- [ ] Cache invalidation follows withdrawal, supersession, and correction.
- [ ] Replay artifacts remain retained and access-controlled.
- [ ] Release/publication gates remain separate.

[Back to top](#top)

---

## Open verification register

| Item | Status | Required evidence |
|---|---:|---|
| Accepted executable bundle format | **UNKNOWN / NOT ESTABLISHED** | Accepted decision, contract, builder, and tested example. |
| Bundle lane inventory | **CONFIRMED** | Complete recursive tree at the pinned base: two documentation files and no non-document payload. |
| Pass 12 packaging profile | **CONFIRMED PROPOSED_INACTIVE** | Current README, exact external Rego/test/fixtures, and dedicated workflow; activation remains absent. |
| Manifest contract and schema home | **NEEDS VERIFICATION** | Accepted semantic contract, Directory Rules review, restrictive schema, fixtures, validator, and tests. |
| General policy runtime | **CONFIRMED PLACEHOLDER** | `0.0.0` metadata and comment-only core; implementation, package tests, and runtime observations remain absent. |
| Evaluator family/version | **UNKNOWN / NOT ACCEPTED** | Accepted configuration, provenance, capability checks, and successful execution evidence. |
| Deterministic builder and lock | **UNKNOWN / NOT ESTABLISHED** | Code, pinned toolchain, complete closure, clean rebuild comparison, and validation report. |
| Bundle selector/activation | **UNKNOWN / NOT ESTABLISHED** | Governed selector, immutable binding, activation/deactivation records, and consumer evidence. |
| Policy validators | **CONFIRMED PARTIAL** | Profile validators have tests/workflows; parent schema-declared validators still require reconciliation. |
| Restrictive `PolicyInputBundle` shape | **CONFIRMED INACTIVE PROFILE / PARENT GAP** | Profile v1 is closed and validated; acceptance, generality, and runtime binding remain open. |
| `PolicyDecision` mapping | **CONFIRMED DECLARED-ONLY SCAFFOLD / RUNTIME GAP** | Exact-byte binding exists; accepted mapping, executed adapter, authentication, receipts, and tests remain open. |
| Reason-code registry | **CONFIRMED PROPOSED_INACTIVE** | Review, adoption or supersession, bundle linkage, and compatibility policy. |
| Obligation registry/interpreters | **CONFIRMED PROPOSED_INACTIVE / PARTIAL** | Candidate vocabulary and fixture profiles exist; accepted issuers, consumers, enforcement, and negative tests remain open. |
| Bundle signatures | **UNKNOWN** | Trust model, key custody, verification, rotation, and revocation. |
| Receipt/proof home | **NEEDS VERIFICATION** | Accepted contract, path, authenticated instances, retention, and replay test. |
| Retention policy | **NEEDS VERIFICATION** | Governance decision and deletion/access controls for bundles, inputs, decisions, and receipts. |
| Policy CI | **CONFIRMED SPLIT / PARTIAL** | One bounded OPA lane executes; the broad workflow remains a static readiness hold. |
| Branch protection/required checks | **UNKNOWN** | Repository ruleset and required-check evidence. |
| Governed consumer enforcement | **UNKNOWN** | Implemented server-side binding, negative tests, runtime observations, and correction handling. |
| Rollback automation | **UNKNOWN** | Runbook, selector rollback, cache invalidation, reevaluation, and drill evidence. |
| Generated-receipt enforcement | **NEEDS VERIFICATION** | Contribution policy names the requirement; complete automated enforcement and exception handling remain unproved. |

[Back to top](#top)

---

## Illustrative manifest

> [!WARNING]
> This example is `PROPOSED`, synthetic, and intentionally not asserted to validate against an accepted schema.

```json
{
  "bundle_id": "kfm-policy-demo-access",
  "bundle_version": "0.1.0-candidate",
  "bundle_status": "candidate",
  "artifact_ref": "ARTIFACT_REF_TBD",
  "artifact_digest": "sha256:DIGEST_TBD",
  "manifest_digest": "sha256:MANIFEST_DIGEST_TBD",
  "source_paths": [
    "policy/access/example.rego"
  ],
  "source_digests": {
    "policy/access/example.rego": "sha256:SOURCE_DIGEST_TBD"
  },
  "dependency_lock_ref": "DEPENDENCY_LOCK_TBD",
  "policy_families": [
    "access"
  ],
  "module_namespaces": [
    "kfm.example.access"
  ],
  "evaluator_family": "EVALUATOR_TBD",
  "evaluator_version_range": "VERSION_RANGE_TBD",
  "entrypoints": [
    "kfm.example.access.result"
  ],
  "fail_closed": true,
  "policy_input_contract_ref": "contracts/policy/policy_input_bundle.md",
  "policy_input_schema_ref": "schemas/contracts/v1/policy/policy_input_bundle.schema.json",
  "policy_decision_contract_ref": "contracts/policy/policy_decision.md",
  "policy_decision_schema_ref": "schemas/contracts/v1/policy/policy_decision.schema.json",
  "engine_result_mapping_ref": "MAPPING_REF_TBD",
  "reason_code_registry_ref": "REASON_REGISTRY_TBD",
  "obligation_registry_ref": "OBLIGATION_REGISTRY_TBD",
  "fixture_refs": [
    "FIXTURE_REF_TBD"
  ],
  "test_refs": [
    "TEST_REF_TBD"
  ],
  "review_refs": [
    "REVIEW_REF_TBD"
  ],
  "allowed_consumers": [
    "CONSUMER_TBD"
  ],
  "allowed_operations": [
    "OPERATION_TBD"
  ],
  "activation_ref": null,
  "supersedes": null,
  "rollback_target": "DISABLED"
}
```

[Back to top](#top)

---

## Maintenance and review burden

### README-only changes

Require:

- policy or governance review;
- documentation review;
- verification that claims match current repository evidence.

### Manifest or bundle changes

Also require, as applicable:

- policy steward;
- bundle/runtime owner;
- security reviewer;
- contracts/schema reviewer;
- validator/test owner;
- affected domain steward;
- rights and sensitivity reviewers;
- governed API or consumer owner;
- release/rollback reviewer.

### Review triggers

Review this README again when:

- the first non-document bundle payload, manifest instance, or lock is added;
- the Pass 12 profile is assembled, renamed, superseded, or activated;
- a bundle manifest contract or schema is accepted;
- evaluator or policy-runtime implementation appears;
- a parent policy validator declaration is implemented or changed;
- the broad readiness hold becomes repository-wide bundle/evaluator execution;
- active bundle selection is introduced;
- the inactive reason/obligation vocabulary is accepted, changed, or superseded;
- `PolicyDecision` schema or normalization changes;
- a signing/attestation trust process is added;
- a bundle is withdrawn, corrected, or rolled back; or
- canonical policy/bundle placement changes.

[Back to top](#top)

---

## ADRs and drift triggers

No new ADR is created by this README. Accepted ADR-0029 and Directory Rules v2 establish the current placement basis; they do not accept a bundle format or evaluator.

Separate governed decisions are required to:

- accept the executable bundle and manifest formats;
- accept evaluator/compiler compatibility and provenance rules;
- change the canonical policy root or create a parallel bundle authority;
- change canonical `PolicyDecision` outcomes or families;
- accept or supersede the reason/obligation vocabulary;
- allow network-dependent builds;
- introduce signing keys or trust roots;
- define production selection and activation;
- permit public/client bundle selection;
- merge bundle activation with release approval; or
- move decisions, receipts, proofs, or release records into this lane.

Record drift when:

- a non-document bundle payload exists without a manifest and immutable identity;
- manifests, locks, source closure, and payload digests disagree;
- runtime follows a mutable alias or request-selected path;
- compatibility policy roots evolve independently;
- bundle copies appear under packages, apps, release, artifacts, or data roots as parallel authority;
- parent schema-declared validator or policy paths remain stale without explicit qualification;
- a static readiness or fixture workflow is cited as general policy or production proof;
- the Pass 12 Boolean/set result is stored directly as canonical `PolicyDecision`; or
- an inactive vocabulary, input profile, or declared-only binding is presented as accepted runtime authority.

[Back to top](#top)

---

## Rollback, correction, and supersession

### README rollback

Before merge, close the draft PR and abandon the scoped branch when authorized.

After merge, revert the documentation commit to restore the previous README. Do not rewrite shared history.

### Candidate bundle rollback

If a candidate fails validation:

1. mark it rejected or withdrawn in its governed status record;
2. preserve the artifact and report if needed for audit;
3. prevent activation;
4. correct source or build inputs;
5. produce a new digest/version;
6. rerun the full validation matrix.

### Active bundle rollback

A bundle rollback is a deployment/governance action, not a file move.

1. stop new selection of the affected digest;
2. confirm the rollback target is reviewed, compatible, and not withdrawn;
3. activate the immutable rollback target through the governed selector;
4. invalidate evaluator and decision caches;
5. identify decisions produced by the affected bundle;
6. re-evaluate consequential in-flight or cached outputs where required;
7. issue correction, withdrawal, or release records when public effects occurred;
8. preserve old bundle/input/decision/receipt lineage;
9. verify public and restricted clients use the intended bundle;
10. document the incident and follow-up tests.

### Compromised or unsafe bundle

If integrity, signing, source, rights, sensitivity, or policy correctness is compromised:

- withdraw the bundle;
- deny or error rather than silently fall back when no safe target exists;
- rotate/revoke credentials or keys outside this lane;
- assess exposed decisions and downstream artifacts;
- correct or withdraw affected public outputs;
- preserve audit evidence without exposing sensitive details.

A Git revert alone does not revoke a deployed bundle, invalidate caches, correct decisions, or withdraw published artifacts.

[Back to top](#top)

---

## Last reviewed

**2026-08-13**, against `main@06ea27fd9b996adb21b2545f69e6860c0c681bc5` and complete tree `ae0e3620ad30d41efb3401c4f0dcdc6f9a645f7e`.

Review again before the first non-document bundle artifact, manifest, lock, general evaluator binding, active selector, authenticated receipt integration, signature trust root, deployment, required-check claim, production consumer, or rollback drill.

[Back to top](#top)

---

## No-loss and evidence ledger

| v0.2 concern | v0.3 disposition |
|---|---|
| Purpose, authority, scope, belongs/exclusions | **RETAINED** with current Pass 12 qualification. |
| Directory placement and singular policy root | **RETAINED AND UPDATED** to accepted ADR-0029, Directory Rules v2, root-registry projection, and the exact direct map. |
| Bundle classes, manifest fields, identity, canonicalization, dependency closure | **RETAINED AS PROPOSED**; no executable format or manifest is silently accepted. |
| Explicit inputs and no-hidden-fetch rule | **RETAINED AND EXTENDED** with the inactive input-profile evidence and parent-schema gap. |
| Engine/canonical outcome separation | **RETAINED AND EXTENDED** with the actual Pass 12 Boolean/set shape and declared-only binding limit. |
| Activation, lifecycle, build, supply chain, audit, sensitivity, failure, and threat controls | **RETAINED** without activation or production claims. |
| Reason codes and obligations | **RETAINED AND RECONCILED** with the inactive candidate registry and fixture-only obligation profiles. |
| Validation and implementation sequence | **RETAINED AND UPDATED** to distinguish the bounded OPA workflow, broad static readiness hold, and remaining bundle/runtime work. |
| Definition of done and open work | **RETAINED AND RE-BASED** against complete current evidence. |
| Illustrative manifest | **RETAINED** as synthetic and non-validating. |
| Maintenance, ADR triggers, rollback, correction, supersession | **RETAINED** with current trigger language. |
| Repository-state claims | **SUPERSEDED** where v0.2 said README-only, TODO-only, minimal fixtures, proposed placement basis, or globally absent validators. |

No prior H2 section was removed. This revision adds evidence and change ledgers only; it does not create or modify any bundle payload, policy source, contract, schema, registry, fixture, validator, test, workflow, runtime, decision, receipt, release object, deployment, or public behavior.

[Back to top](#top)

---

## Changelog

### v0.3 — 2026-08-13

- pinned the complete current repository tree and exact target preimage;
- replaced the stale README-only lane claim with the exact two-file documentation map;
- recorded the Pass 12 source, six native tests, four workflow-evaluated fixtures, and checksum-pinned OPA workflow without calling them a bundle;
- reconciled the restrictive inactive input profile, inactive vocabulary, declared-only binding, profile validators, and placeholder general runtime;
- reclassified `policy-test` from TODO-only to a static broad readiness hold with one separately governed executable Rego lane;
- added the `BOUNDARY_COMPACT` responsibility signature;
- preserved all thirty prior H2 sections and recorded the no-loss disposition.

### v0.2 — 2026-07-14

Established the comprehensive proposed bundle boundary, artifact and manifest model, immutable identity, dependency closure, finite-outcome normalization, selection controls, supply-chain posture, replay, sensitivity, validation, rollback, and open-work register. Its repository-state snapshot is superseded by v0.3; its substantive doctrine remains retained.

[Back to top](#top)
