<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-policy-runtime-src-policy-runtime-readme
title: packages/policy-runtime/src/policy_runtime/ — Python Namespace and Policy-Evaluation Placeholder Boundary
type: readme
version: v1.1
status: draft
owners: OWNER_TBD — Policy steward · Policy-runtime steward · Contracts steward · Schema steward · Evidence steward · Rights/sensitivity steward · Security steward · Validation steward · Runtime/API steward · Release steward · CI steward · Docs steward
created: NEEDS VERIFICATION — target existed before this evidence-grounded revision
updated: 2026-07-15
policy_label: "public-doctrine; package-source-boundary; python-namespace; greenfield-placeholder; evaluator-unbound; bundle-selection-unratified; api-unratified; consumers-unverified; tests-unestablished; fail-closed; explicit-inputs; no-hidden-fetches; no-network-by-default; policy-authority-external; evidence-subordinate; rights-aware; sensitivity-aware; release-subordinate; no-truth-authority; no-publication-authority; migration-required; rollback-aware"
current_path: packages/policy-runtime/src/policy_runtime/README.md
truth_posture: >
  CONFIRMED target README v1, package metadata name kfm-policy-runtime and version 0.0.0,
  repository-present policy_runtime namespace, empty __init__.py, comment-only core.py greenfield
  placeholder, parent package/source READMEs, root Python scaffold, packages responsibility-root doctrine,
  PolicyInputBundle semantic contract v0.2, permissive PROPOSED PolicyInputBundle schema requiring only id,
  canonical PolicyDecision semantic contract v0.2, concrete PROPOSED PolicyDecision schema requiring six
  fields and using ANSWER|ABSTAIN|DENY|ERROR, runtime DecisionEnvelope contract with the same primary outcome
  vocabulary, one documented valid and one invalid PolicyDecision fixture, absent dedicated validator files
  at schema-declared paths, README-only bounded policy-bundle lane, TODO-only policy-test workflow, and
  bounded absence of functional namespace modules, public exports, repository consumers, package-local
  tests, package-specific CI, accepted evaluator/bundle binding, receipt persistence, release use,
  deployment use, or operational health / PROPOSED a small reusable Python namespace for explicit policy-
  input validation, deterministic engine-adapter boundaries, engine-native result normalization, canonical
  PolicyDecision candidate assembly, obligation/reason preservation, replay metadata, test matrices, staged
  adoption, correction, deprecation, and rollback / CONFLICTED prior README claims that described implemented
  modules and usable imports; presented ALLOW|DENY|RESTRICT|HOLD|ABSTAIN|ERROR as package outcomes while
  canonical PolicyDecision and DecisionEnvelope schemas use ANSWER|ABSTAIN|DENY|ERROR; schema-declared
  validator paths that do not exist; PolicyInputBundle contract richness versus its permissive placeholder
  schema; distribution name kfm-policy-runtime versus unconfigured import-package discovery; policy-bundle
  intent versus no accepted bundle artifact, format, selector, or evaluator binding / UNKNOWN accepted API,
  build backend, Python support policy, package discovery, dependencies, type-checking, semantic versioning,
  reason-code registry, obligation registry, engine-native result contract, bundle format, active selection,
  OPA/WASM binding, consumer set, runtime integration, receipt/proof integration, CI enforcement, deployment,
  release use, and operational health / NEEDS VERIFICATION owners, maintainer approval, metadata completion,
  import-name decision, evaluator adapter ADR, bundle activation contract, PolicyInputBundle schema
  strengthening, outcome-normalization mapping, test home, first consumer, CI path coverage, security review,
  correction process, deprecation window, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 37025300a2a3639c4ee68f0dba4b179f6e15b63d
  prior_blob: 34d6c813aaa5173fc6d936a6bb560a5db8981ece
  package_readme_blob: e70246ec4770399b41b6c07e3f97a4c66e17503d
  source_readme_blob: 4d658ab4e68913a30fdd1456fc648260a356d71e
  package_metadata_blob: ebb6725ad9a00d77df06f779a603814027abe084
  namespace_init_blob: e69de29bb2d1d6434b8b29ae775ad8c2e48c5391
  namespace_core_blob: e7e14cf39ae6919fbbc80f1b471de6b907292edb
  root_pyproject_blob: e3bd40e8e6ce14dfcde78ff5c09608095c3eca76
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  policy_input_contract_blob: 545c352681dd0db0cd4d169a5d2f9c364356457c
  policy_input_schema_blob: b89db4b1730c61258441e0eed037276b910b1990
  policy_decision_contract_blob: ebfe97f98263e6309db6d2772cb2c5e548819650
  policy_decision_schema_blob: 1472d26a42c73f17545b4464a275412ffa1d098e
  decision_envelope_contract_blob: b5120a208910f5e2907874b03af1fc8c7f43363d
  policy_decision_fixtures_blob: 0169614d568cfc32bc7fb257fb42f1e6b792bae3
  validator_index_blob: 56ef4bd527ddfc8d726662092ca589ab2340b401
  policy_bundles_readme_blob: 77f59c399fbce668c916cbbc385009121d6169f4
  policy_test_workflow_blob: 2bba88bb018600f54995d06b03cac02145b96fe7
  bounded_path_checks:
    - packages/policy-runtime/src/policy_runtime/README.md existed at version v1 before this revision
    - packages/policy-runtime/pyproject.toml exists with project name kfm-policy-runtime and version 0.0.0
    - package pyproject contains no build-system, Python requirement, dependencies, optional dependencies, scripts, entry points, package-discovery configuration, or tool configuration
    - packages/policy-runtime/src/policy_runtime/__init__.py exists and is empty
    - packages/policy-runtime/src/policy_runtime/core.py exists and contains only a greenfield-placeholder comment
    - bounded repository search found no functional policy_runtime consumer import or package pytest reference
    - tools/validators/validate_policy_decision.py was not found
    - tools/validators/policy/validate_policy_decision.py was not found
    - tools/validators/policy/validate_policy_input_bundle.py was not found
    - policy/bundles bounded evidence describes the lane as README-only with no accepted bundle instance, manifest instance, selector, or evaluator binding
    - PolicyInputBundle schema is PROPOSED, requires only id, and allows additional properties
    - PolicyDecision schema is PROPOSED, requires decision_id/outcome/policy_family/reasons/obligations/evaluated_at, and disallows additional properties
    - PolicyDecision schema outcome enum is ANSWER|ABSTAIN|DENY|ERROR
    - PolicyDecision schema policy_family enum is promotion|access|render|capability|consent|sensitivity
    - PolicyDecision fixture family documents one valid example and one invalid example missing decision_id
    - policy-test workflow runs echo-only TODO steps for opa-test and policy-fixture-coverage
related:
  - ../../README.md
  - ../README.md
  - ../../pyproject.toml
  - __init__.py
  - core.py
  - ../../../../pyproject.toml
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/architecture/contract-schema-policy-split.md
  - ../../../../docs/doctrine/trust-membrane.md
  - ../../../../contracts/policy/policy_input_bundle.md
  - ../../../../contracts/policy/policy_decision.md
  - ../../../../contracts/runtime/decision_envelope.md
  - ../../../../schemas/contracts/v1/policy/policy_input_bundle.schema.json
  - ../../../../schemas/contracts/v1/policy/policy_decision.schema.json
  - ../../../../policy/README.md
  - ../../../../policy/bundles/README.md
  - ../../../../tools/validators/policy/README.md
  - ../../../../fixtures/contracts/v1/policy/policy_decision/README.md
  - ../../../../tests/schemas/test_common_contracts.py
  - ../../../../.github/workflows/policy-test.yml
tags: [kfm, packages, policy-runtime, policy_runtime, python, namespace, scaffold, policy-evaluation, PolicyInputBundle, PolicyDecision, DecisionEnvelope, finite-outcomes, obligations, reason-codes, bundles, opa, fail-closed, evidence, rights, sensitivity, validation, compatibility, migration, rollback]
notes:
  - "This revision changes only packages/policy-runtime/src/policy_runtime/README.md."
  - "The namespace currently contains this README, an empty __init__.py, and a comment-only core.py placeholder."
  - "This README does not install the package, define an accepted API, create exports, approve an evaluator, activate a policy bundle, establish consumers, run policy, write receipts, accept an ADR, or prove CI/runtime behavior."
  - "Prior proposed module names, imports, exports, helper outcomes, and broad consumer claims are retained only as superseded documentation lineage; they are not implementation facts or compatibility commitments."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `policy_runtime` Python Namespace and Policy-Evaluation Placeholder Boundary

`packages/policy-runtime/src/policy_runtime/`

> Repository-present Python namespace scaffold for a future reusable policy-evaluation helper library. Current evidence establishes an empty package initializer and a comment-only `core.py` placeholder—not a functional evaluator, OPA adapter, policy-bundle loader, accepted API, PolicyInputBundle validator, PolicyDecision builder, receipt writer, policy authority, evidence authority, or release component.

![status](https://img.shields.io/badge/status-draft-yellow)
![version](https://img.shields.io/badge/version-v1.1-informational)
![maturity](https://img.shields.io/badge/maturity-greenfield__placeholder-lightgrey)
![distribution](https://img.shields.io/badge/distribution-kfm--policy--runtime-blue)
![package-version](https://img.shields.io/badge/package__version-0.0.0-lightgrey)
![evaluator](https://img.shields.io/badge/evaluator-unbound-orange)
![api](https://img.shields.io/badge/API-unratified-orange)
![tests](https://img.shields.io/badge/package__tests-not__established-orange)
![authority](https://img.shields.io/badge/policy__authority-none-red)

**Quick links:** [Purpose](#purpose) · [Evidence](#status-and-evidence) · [Placement](#directory-rules-and-authority) · [Vocabulary](#bounded-context-and-ubiquitous-language) · [Inventory](#confirmed-namespace-inventory) · [Packaging](#packaging-import-and-api-status) · [Contracts](#contract-schema-and-policy-boundaries) · [Outcomes](#outcome-vocabularies-and-normalization) · [Responsibilities](#proposed-responsibility-envelope) · [Bundles](#policy-bundle-and-evaluator-boundary) · [Inputs](#policyinputbundle-boundary) · [Decisions](#policydecision-candidate-boundary) · [Obligations](#reasons-obligations-and-safe-explanations) · [Lifecycle](#lifecycle-and-trust-membrane) · [Effects](#side-effects-network-and-determinism) · [Replay](#identity-hashing-replay-and-freshness) · [Security](#security-rights-sensitivity-and-privacy) · [Consumers](#consumer-runtime-and-public-surface-boundary) · [Testing](#testing-fixtures-and-ci) · [Implementation](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Open](#verification-register) · [Drift](#drift-and-conflicts) · [Rollback](#rollback-correction-and-deprecation)

> [!IMPORTANT]
> **This README is not implementation evidence for a policy runtime.** It does not establish installation, import success, exports, OPA availability, bundle activation, evaluator integrity, consumer adoption, policy execution, receipt persistence, tests, CI enforcement, deployment, or operational health.

> [!CAUTION]
> **Policy evaluation is not truth or publication.** A policy result cannot create evidence, cure unresolved rights, downgrade sensitivity, satisfy review, promote lifecycle state, authorize release, or make generated language authoritative.

---

<a id="purpose"></a>

## Purpose

This README defines the responsibility and verification boundary for:

```text
packages/policy-runtime/src/policy_runtime/
```

The namespace is intended to become a **small reusable helper library** for policy-evaluation mechanics shared by more than one governed API, pipeline, worker, validator, release gate, map/runtime component, or maintenance tool.

The current state is narrower:

- `__init__.py` is empty;
- `core.py` is a comment-only placeholder;
- no functional module or export is established;
- no consuming import or package pytest reference surfaced in bounded search;
- the package manifest is a `0.0.0` stub without build/discovery configuration;
- no accepted policy bundle instance, selector, evaluator binding, or deployment path is established;
- validator paths named by the policy schemas were not found;
- the policy-test workflow contains echo-only TODO steps.

This README therefore records the **CONFIRMED placeholder state**, defines a **PROPOSED governed boundary**, and makes the contract, schema, policy, evidence, rights, sensitivity, validation, release, correction, and rollback burden explicit before adoption.

[Back to top](#top)

---

<a id="status-and-evidence"></a>

## Status and evidence

| Surface | Status | Safe conclusion |
|---|---:|---|
| Target README | **CONFIRMED v1 before revision** | Namespace documentation existed but over-described implementation. |
| Distribution metadata | **CONFIRMED placeholder** | `kfm-policy-runtime`, version `0.0.0`. |
| Build/discovery | **NOT DECLARED** | The subpackage is not proved buildable or importable. |
| Namespace | **CONFIRMED present** | Repository path exists. |
| `__init__.py` | **CONFIRMED empty** | No exports. |
| `core.py` | **CONFIRMED comment-only** | No behavior. |
| Functional modules | **NOT FOUND by bounded checks** | Prior module names are not facts. |
| Consumers/tests | **NOT FOUND by bounded search** | No adoption or behavior is proved. |
| PolicyInputBundle contract | **CONFIRMED draft/PROPOSED** | Rich semantic context is documented. |
| PolicyInputBundle schema | **CONFIRMED permissive PROPOSED stub** | Requires only `id`; allows extras. |
| PolicyDecision contract/schema | **CONFIRMED draft/PROPOSED** | Six required fields; closed finite enums. |
| DecisionEnvelope contract | **CONFIRMED draft/PROPOSED** | Runtime transport uses the canonical finite outcome vocabulary. |
| PolicyDecision fixtures | **CONFIRMED minimal family** | One valid and one missing-id invalid fixture. |
| Dedicated validators | **NOT FOUND at declared paths** | No dedicated validation implementation is proved. |
| Policy bundles | **README-only by bounded evidence** | No accepted instance/selector/evaluator binding. |
| Policy CI | **TODO-only** | Green status would not prove policy behavior. |
| Runtime health | **UNKNOWN** | No operational evaluator is proved. |

### Corrections from v1

| Prior implication | Current evidence | Correction |
|---|---|---|
| Importable helper implementation exists | Only empty/comment placeholders exist | Reclassify as greenfield scaffold. |
| Named modules/exports/imports are usable | They are absent | Retain only as superseded lineage. |
| Rich PolicyInputBundle values are validated | Schema requires only `id` | Separate schema validity from semantic readiness. |
| `ALLOW|DENY|RESTRICT|HOLD|ABSTAIN|ERROR` are canonical package outcomes | Canonical schemas use `ANSWER|ABSTAIN|DENY|ERROR` | Require an explicit normalization contract. |
| Approved bundles can be invoked | No accepted bundle instance or binding is proved | File presence must not activate policy. |
| Dedicated validators exist | Declared files are absent | Do not claim validator execution. |
| Policy CI verifies behavior | Jobs only echo TODO | Replace stubs before enforcement claims. |

[Back to top](#top)

---

<a id="directory-rules-and-authority"></a>

## Directory Rules and authority

Directory Rules place reusable shared libraries under `packages/` and state that a package must be reusable; one-off workflow steps belong in `tools/` or `pipelines/`.

The namespace is correctly placed only if future code is shared, bounded, deterministic where promised, testable without production data, and subordinate to its governing roots.

| Responsibility | Governing home | Namespace relationship |
|---|---|---|
| Python mechanics | This namespace | Candidate implementation only. |
| Package metadata | `packages/policy-runtime/pyproject.toml` | Currently incomplete. |
| Policy rules | `policy/` | Authoritative rule source; never authored here. |
| Bundle packaging/manifest | `policy/bundles/` | Activation remains unproved. |
| Input semantics/shape | `contracts/policy/` and `schemas/contracts/v1/policy/` | Implement and validate; do not redefine. |
| Decision semantics/shape | PolicyDecision contract/schema | Canonical output surface. |
| Runtime transport | DecisionEnvelope/RuntimeResponseEnvelope | Downstream transport. |
| Evidence | EvidenceBundle/resolver roots | Consume status/refs only. |
| Rights/consent/sensitivity facts | Governing registries/contracts/policy | Do not discover or invent. |
| Lifecycle state | `data/<phase>/` and governed workflows | Do not read/write as authority. |
| Receipts/proofs | `data/receipts/`, `data/proofs/` | Candidate metadata only until approved. |
| Review/release | Governance and `release/` | Never approve or publish. |
| Public surfaces | Governed apps/runtime | Must not expose namespace internals as authority. |

This namespace may eventually execute approved policy mechanics. It must never become policy rule authority, evidence truth, rights/consent authority, sensitivity authority, review approval, lifecycle promotion, release approval, or public truth.

[Back to top](#top)

---

<a id="bounded-context-and-ubiquitous-language"></a>

## Bounded context and ubiquitous language

| Term | Meaning here | Must not mean |
|---|---|---|
| `PolicyInputBundle` | Explicit input snapshot for a policy gate. | Hidden fetch or approval. |
| `PolicyDecision` | Canonical record of one policy evaluation. | Engine-native result or release approval. |
| `DecisionEnvelope` | Runtime transport for finite decision context. | Policy rule authority. |
| Policy bundle | Immutable reviewed evaluation unit with explicit identity. | Directory presence or mutable “latest”. |
| Evaluator | Approved engine/profile executing an explicit bundle. | Policy authority. |
| Engine-native result | Evaluator-specific lower-level result. | Canonical KFM decision without mapping. |
| Reason | Stable safe explanation/code. | Sensitive dump or chain-of-thought. |
| Obligation | Mandatory downstream duty. | Optional hint. |
| Activation | Reviewed binding of bundle, evaluator, caller, and environment. | File existence. |
| Fail closed | Refuse unsafe progress when support is absent. | Collapse every failure to one value. |

```text
PolicyInputBundle != PolicyDecision
PolicyDecision != DecisionEnvelope
EngineNativeResult != PolicyDecision.outcome
SchemaValid != SemanticallyComplete
Policy ANSWER != ReleaseApproved
Policy ERROR != Policy DENY
BundlePresent != BundleActive
ReceiptCandidate != ReceiptPersisted
```

[Back to top](#top)

---

<a id="confirmed-namespace-inventory"></a>

## Confirmed namespace inventory

```text
packages/policy-runtime/src/policy_runtime/
├── README.md
├── __init__.py
└── core.py
```

| Path | Status | Meaning |
|---|---:|---|
| `README.md` | **CONFIRMED** | Namespace boundary. |
| `__init__.py` | **CONFIRMED empty** | Marker only; no exports. |
| `core.py` | **CONFIRMED comment-only** | Greenfield placeholder. |

Not established: input, engine, decision, obligation, reason-code, receipt, replay, validation, fixture, typed-marker, evaluator, bundle selector, public API, test, consumer, CI, deployment, or telemetry modules.

Prior module names remain design prompts only—not implementation, architecture approval, reserved API, or compatibility commitments.

[Back to top](#top)

---

<a id="packaging-import-and-api-status"></a>

## Packaging, import, and API status

Confirmed metadata:

```toml
[project]
name = "kfm-policy-runtime"
version = "0.0.0"
```

Unconfigured surfaces include build backend, Python requirement, `src/` discovery, dependencies, optional dependencies, scripts, entry points, license, type support, version policy, and artifact publication.

The distribution name `kfm-policy-runtime` and namespace path `policy_runtime` are present, but their mapping is not configured or tested.

Before treating the namespace as importable:

1. declare a build backend and Python support;
2. configure `src/` discovery;
3. build and inspect an artifact;
4. install into a clean environment;
5. import `policy_runtime`;
6. verify metadata/dependencies;
7. prove import has no side effects;
8. prove import does not select or activate a policy bundle.

**No public package API is established.**

[Back to top](#top)

---

<a id="contract-schema-and-policy-boundaries"></a>

## Contract, schema, and policy boundaries

| Surface | Owns | Namespace duty |
|---|---|---|
| Contract | Meaning and obligations | Implement without redefining. |
| Schema | Machine shape | Validate exact accepted version. |
| Policy source | Executable admissibility | Execute only through explicit approved binding. |
| Bundle manifest | Immutable composition | Verify supplied identity/digest/profile. |
| Namespace | Mechanical normalization/evaluation adapters | Remain subordinate. |
| Validator | Independent conformance checks | Produce inspectable results. |
| Receipt/proof | Audit and integrity | Preserve refs/candidates; do not self-authorize. |
| Release | Publication decision | Never bypass. |

### PolicyInputBundle maturity

The semantic contract describes operation, audience, evidence, source role, rights, sensitivity, lifecycle, release, review, and evaluator context. The paired schema currently requires only `id`, permits optional `spec_hash`/`version`, allows additional properties, and is `PROPOSED`.

A schema-valid PolicyInputBundle may therefore be semantically unusable. Namespace code must not invent missing context.

### PolicyDecision maturity

The paired schema requires:

```text
decision_id
outcome
policy_family
reasons
obligations
evaluated_at
```

It disallows additional properties.

Outcomes:

```text
ANSWER | ABSTAIN | DENY | ERROR
```

Policy families:

```text
promotion | access | render | capability | consent | sensitivity
```

### Safe flow

```text
PolicyInputBundle
  -> explicit approved bundle + evaluator
  -> engine-native result
  -> versioned normalization
  -> PolicyDecision candidate
  -> schema + semantic validation
  -> DecisionEnvelope / RuntimeResponseEnvelope
  -> obligations + release/public gates
```

[Back to top](#top)

---

<a id="outcome-vocabularies-and-normalization"></a>

## Outcome vocabularies and normalization

The prior README used lower-level values:

```text
ALLOW | DENY | RESTRICT | HOLD | ABSTAIN | ERROR
```

Canonical PolicyDecision and primary DecisionEnvelope schemas use:

```text
ANSWER | ABSTAIN | DENY | ERROR
```

These vocabularies are not interchangeable.

| Layer | Values | Status |
|---|---|---:|
| Engine-native/bundle-local | Evaluator-specific; prior docs name ALLOW/DENY/RESTRICT/HOLD/ABSTAIN/ERROR | **UNRATIFIED** |
| PolicyDecision | ANSWER/ABSTAIN/DENY/ERROR | **SCHEMA-CONFIRMED PROPOSED** |
| DecisionEnvelope | ANSWER/ABSTAIN/DENY/ERROR | **CONTRACT/SCHEMA-CONFIRMED PROPOSED** |
| Validator result | PASS/FAIL/DENY/RESTRICT/HOLD/ABSTAIN and reason codes | **DOCUMENTED; IMPLEMENTATION UNPROVED** |
| Release state | Separate release vocabulary | **NEEDS VERIFICATION** |

A normalization adapter must specify source/target versions, obligations, restrictions, holds, error preservation, reason mapping, missing-context behavior, stale-bundle behavior, and policy-family rules.

Illustrative questions—not accepted mappings:

| Native result | Possible canonical treatment | Decision required |
|---|---|---|
| `ALLOW` | `ANSWER` candidate | Confirm context and downstream gates. |
| `RESTRICT` | `ANSWER` with mandatory obligations, or negative result | Define by family/surface. |
| `HOLD` | Internal review state, `ABSTAIN`, or `DENY` | Ratify explicitly. |
| `ABSTAIN` | `ABSTAIN` | Preserve evidence deficiency. |
| `DENY` | `DENY` | Preserve safe reason. |
| `ERROR` | `ERROR` | Never silently convert. |

Restrictions and obligations must not disappear during normalization. `ABSTAIN`, `DENY`, and `ERROR` must remain distinct.

[Back to top](#top)

---

<a id="proposed-responsibility-envelope"></a>

## Proposed responsibility envelope

Everything here is **PROPOSED**.

| Candidate area | Narrow role | Excluded authority |
|---|---|---|
| Input candidate | Parse/validate explicit PolicyInputBundle values. | No hidden fetch. |
| Semantic completeness | Report missing context under accepted profile. | No invented facts. |
| Bundle reference | Validate supplied id/version/digest/profile. | No discovery/activation. |
| Evaluator adapter | Execute an injected approved interface. | No policy selection authority. |
| Native result | Parse evaluator output. | No direct canonical exposure. |
| Normalization | Map under a versioned contract. | No guessed mapping. |
| Decision candidate | Assemble exact fields. | No persistence/approval. |
| Obligations/reasons | Preserve reviewed values. | No silent discard. |
| Replay | Compare explicit lineage. | No release certification. |
| Test builders | Synthetic public-safe values. | No production copies. |

The namespace must not become a policy editor, bundle registry, mutable selector, OPA control plane, evidence resolver, consent/sensitivity registry, lifecycle store, receipt database, release manager, public API, AI truth source, or secrets manager.

[Back to top](#top)

---

<a id="policy-bundle-and-evaluator-boundary"></a>

## Policy bundle and evaluator boundary

Current bounded evidence establishes no accepted bundle instance, manifest instance, selector, evaluator binding, or deployment.

### File presence is not activation

Directory name, newest file, symlink, environment fallback, “latest” alias, successful parse, schema pass, OPA-compatible layout, or digest alone must not activate policy.

A future explicit binding should identify bundle id/version/digest, manifest ref, policy family, evaluator profile/version, input/output contract versions, timeout/failure posture, activation record, and supersession state.

### Evaluator adapter requirements

- explicit immutable bundle input;
- digest/manifest verification;
- no mutable path selection;
- timeout/resource limits;
- structured native result/diagnostics;
- evaluator version preservation;
- no hidden network calls;
- no arbitrary environment secret reads;
- no sensitive input logging;
- fail closed on unsupported output;
- process success must not equal policy approval by itself.

OPA is mentioned in existing docs, but no subprocess, server, or WASM binding is accepted. Mode, provenance, version pinning, query contract, serialization, limits, network boundary, error mapping, replay, supply chain, and ownership require review before implementation.

Public clients, UI state, query parameters, and AI prompts must not select a bundle, evaluator, policy version, or fail-open mode.

[Back to top](#top)

---

<a id="policyinputbundle-boundary"></a>

## PolicyInputBundle boundary

A PolicyInputBundle is explicit input—not a decision, evidence, source authority, consent approval, sensitivity authority, release approval, runtime response, or AI authority.

The current schema confirms only `id` required, optional string `spec_hash`/`version`, and additional properties allowed. The namespace must distinguish minimal schema validation from future semantic-profile validation.

A future profile may require operation, audience, object/domain refs, lifecycle/release state, evidence refs/resolver state, source roles, rights/consent, sensitivity, geometry precision, review refs, correction/rollback context, bundle/evaluator context, prior decisions, and freshness.

### No-hidden-fetch invariant

Do not fill missing fields from source systems, RAW/WORK/QUARANTINE, implicit registries, UI/browser state, operator memory, vector search, AI prompts, model output, current release, or current bundle.

After evaluation begins, input content should be immutable. Changes require a new id/version/hash. Sensitive values should be minimized or referenced.

[Back to top](#top)

---

<a id="policydecision-candidate-boundary"></a>

## PolicyDecision candidate boundary

A future helper may assemble a PolicyDecision **candidate**. It must not persist authority, claim release approval, claim evidence closure, authorize public rendering, or mutate history.

Candidate rules:

1. accept all required fields explicitly;
2. validate exact enums/pattern/date-time;
3. receive time from the caller/injected clock;
4. preserve deterministic reason/obligation ordering or define semantics;
5. reject unsupported extra fields;
6. avoid sensitive diagnostics;
7. return validation separately;
8. support schema validation before persistence;
9. preserve lineage in adjacent metadata when the closed schema has no field;
10. never equate construction with policy success.

`decision_id` must match `^[a-z][a-z0-9_:.-]*$` and must not contain credentials, raw prompts, protected locations, private identifiers, or mutable “latest” state.

A later decision supersedes through explicit lineage, not mutation.

[Back to top](#top)

---

<a id="reasons-obligations-and-safe-explanations"></a>

## Reasons, obligations, and safe explanations

Reasons should be stable, policy-family scoped, audience-safe, separable into internal/public detail, free of raw sensitive facts, and sufficient to distinguish missing support, denial, and process error.

Obligations are mandatory duties. Contract examples include citation attachment, coordinate redaction, geometry generalization, exact-location withholding, steward review, delayed publication, rights notice, export block, and rollback checks. They are examples—not a confirmed closed registry.

The namespace may preserve/validate obligations. Callers and release workflows enforce them. Unknown or unsupported obligations must block progress rather than be ignored.

Never expose exact sensitive locations, private person/DNA data, reconstruction thresholds, restricted policy details, credentials, raw evidence, or chain-of-thought in reasons, obligations, exceptions, or logs.

[Back to top](#top)

---

<a id="lifecycle-and-trust-membrane"></a>

## Lifecycle and trust membrane

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

The namespace may evaluate explicit context at a gate. It does not own lifecycle reads/writes.

| Unsafe collapse | Required behavior |
|---|---|
| RAW ref -> public answer | Fail closed under accepted mapping. |
| WORK candidate -> published object | Require validation/evidence/policy/review/release. |
| QUARANTINE -> normal response | Preserve quarantine and block exposure. |
| Schema-valid input -> policy-ready | Run semantic-profile validation. |
| Policy `ANSWER` -> release approved | Require release gates/obligations. |
| Evaluator success -> evidence truth | Preserve evidence separation. |
| Bundle digest -> active policy | Require activation binding. |
| Receipt candidate -> persisted receipt | Require owning workflow. |
| Merge -> KFM PUBLISHED | Preserve governed release state. |

When evidence required by an operation is missing or unresolved, do not manufacture support. Preserve the deficiency and map only through accepted policy rules.

[Back to top](#top)

---

<a id="side-effects-network-and-determinism"></a>

## Side effects, network, and determinism

Core helpers should be pure/offline: parsing, schema/profile validation, native-result parsing, normalization, candidate assembly, obligation/reason checks, and replay comparisons.

Core code must not fetch source data, query lifecycle stores, select bundles from filesystem, call remote OPA by default, open sockets at import, read credentials at import, write decisions/receipts/proofs/releases, modify policy source, sleep/retry internally, invoke AI, or emit public responses.

Effectful evaluator execution must be isolated behind an injected protocol, clearly named, resource-limited, visible, and absent from import-time behavior.

Given identical explicit input, profile version, bundle digest, evaluator version, normalization version, clock input, and dependencies, deterministic paths should produce equivalent output. Control JSON canonicalization, ordering, Unicode, timestamps, timeout behavior, and environment paths.

Logs are diagnostics—not decisions, receipts, evidence, or release proof.

[Back to top](#top)

---

<a id="identity-hashing-replay-and-freshness"></a>

## Identity, hashing, replay, and freshness

Keep separate identities for PolicyInputBundle, bundle, manifest, evaluator profile, evaluation event, PolicyDecision, DecisionEnvelope, receipt/proof, and release.

Delegate repository-standard hashing rather than inventing a competing digest/canonicalization rule.

Replay should preserve input, bundle/manifest, evaluator, normalization, expected/observed decision, reasons/obligations, time policy, and contract/schema versions.

Replay outcomes should distinguish exact match, semantic match, approved migration difference, unexplained drift, missing support, evaluator error, and comparison error. Exact enum names remain proposed.

Policy results may become stale through bundle supersession, rights/consent/sensitivity changes, evidence freshness, release correction, evaluator vulnerability, or contract migration. Never refresh a stale decision by rewriting its timestamp; re-evaluate and preserve supersession lineage.

[Back to top](#top)

---

<a id="security-rights-sensitivity-and-privacy"></a>

## Security, rights, sensitivity, and privacy

Threats include hidden context fills, arbitrary bundle paths, mutable directories, unreviewed bundle content, evaluator failure converted to allow, dropped obligations, sensitive logs, internal reasons exposed publicly, stale decisions, public bundle selection, and hidden fail-open configuration.

Prefer refs and bounded attributes over raw records. Avoid raw payloads, credentials, private keys, living-person/DNA data, exact rare-species/archaeological/cultural locations, sensitive infrastructure, private joins, and unrestricted review notes.

The namespace consumes supplied rights/consent/sensitivity posture. It does not discover, approve, or downgrade it. Unknown/stale context must fail closed.

Bundle/evaluator supply-chain review must cover provenance, version pinning, build provenance, dependency closure, digests/signatures, parser safety, subprocess/WASM/server constraints, vulnerability response, and rollback.

[Back to top](#top)

---

<a id="consumer-runtime-and-public-surface-boundary"></a>

## Consumer, runtime, and public-surface boundary

No functional consumer import was established. Repeat consumer search before changing exports or paths.

The first consumer should have a narrow shared need, use the smallest accepted symbol set, supply explicit bundle/evaluator context, include package and integration tests, preserve previous behavior, include rollback, remain behind governed APIs, and avoid exposing internals.

A mature flow may assemble input, resolve an approved bundle through governed configuration, call an injected evaluator, normalize output, validate a PolicyDecision candidate, persist through owning workflows, build a DecisionEnvelope, enforce obligations, evaluate release/public gates, and return a governed response. The namespace should cover only the reusable mechanical subset.

Public clients must not import internals, choose bundles/endpoints, bypass obligations, infer truth from `ANSWER`, receive sensitive negative-state detail, or access RAW/WORK/QUARANTINE through helpers.

[Back to top](#top)

---

<a id="testing-fixtures-and-ci"></a>

## Testing, fixtures, and CI

Current status: no namespace tests, no functional exports, missing dedicated validators, minimal PolicyDecision fixture coverage, no established rich PolicyInputBundle fixtures, and TODO-only policy workflow steps.

### Minimum test matrix

| Family | Minimum proof |
|---|---|
| Build/install/import | Isolated artifact and import. |
| Import safety | No selection/evaluation/network/write/secret read. |
| PolicyInputBundle schema | Exact current schema behavior. |
| Semantic profile | Missing operation/audience/evidence/rights/sensitivity fails explicitly. |
| Bundle binding | Id/version/digest/manifest/profile checked. |
| Activation | File presence cannot activate policy. |
| Evaluator | Timeout, exit, malformed/unsupported result, resource errors. |
| Normalization | Every accepted native result maps explicitly. |
| Vocabulary separation | RESTRICT/HOLD do not disappear. |
| PolicyDecision | Exact fields/enums/pattern/date-time/no extras. |
| Reasons/obligations | Negative reasons; unknown obligations fail closed. |
| Evidence/rights/sensitivity | Missing, stale, revoked, unknown, contradictory cases. |
| Lifecycle | RAW/WORK/QUARANTINE never become public candidates. |
| Determinism/replay | Stable output; match/drift/migration/error distinct. |
| Security | Traversal, injection, oversized input, log leakage, arbitrary endpoint. |
| Consumer/public | Governed integration and bypass denial. |

Fixtures must be synthetic, deterministic, public-safe, versioned, paired valid/invalid/edge, and explicit about whether they prove shape or behavior.

Expand PolicyDecision fixtures across all outcomes/families, invalid enums/id/date/extra fields, constrained answers, sensitive reasons, staleness, and replay. Expand PolicyInputBundle fixtures for minimal-valid, missing id, missing operation/audience/evidence/rights/sensitivity, consent revocation, protected location, stale bundle, hidden-fetch attempt, release gap, and invalid evaluator profile.

A meaningful CI lane must replace TODO echoes and run build/import, unit/property/security/no-network tests, contract/schema fixtures, deterministic mock evaluator tests, dependency review, consumer integration, and docs validation.

[Back to top](#top)

---

<a id="smallest-sound-implementation-sequence"></a>

## Smallest sound implementation sequence

### Gate 0 — ownership and architecture

- [ ] Assign owners and confirm first consumer.
- [ ] Decide build/Python support.
- [ ] Decide evaluator mode and ADR need.
- [ ] Accept bundle format/manifest/activation contract.
- [ ] Ratify native vocabulary and normalization.
- [ ] Define reason/obligation governance and rollback.

### Gate 1 — installable inert namespace

- [ ] Complete metadata/discovery.
- [ ] Add clean build/install/import tests.
- [ ] Prove import has no effects.
- [ ] Keep exports empty or minimal.

### Gate 2 — explicit values

- [ ] Add one consumer-needed typed value/result surface.
- [ ] Bind contract/schema versions.
- [ ] Separate schema and semantic-profile validation.
- [ ] Preserve unknown/missing context.

### Gate 3 — deterministic mock evaluator

- [ ] Define injected evaluator protocol.
- [ ] Implement mock only.
- [ ] Add timeout/error/malformed tests.
- [ ] Prove no path-based activation.

### Gate 4 — normalization

- [ ] Ratify native vocabulary.
- [ ] Define RESTRICT/HOLD treatment.
- [ ] Preserve ERROR/ABSTAIN distinctions.
- [ ] Add exhaustive mapping tests.

### Gate 5 — PolicyDecision candidate

- [ ] Assemble exact schema fields.
- [ ] Validate enums/id/time/no extras.
- [ ] Expand fixtures.
- [ ] Prove no persistence.

### Gate 6 — first governed consumer

- [ ] Integrate one caller.
- [ ] Preserve prior behavior.
- [ ] Enforce obligations downstream.
- [ ] Add rollback and runtime evidence.

### Gate 7 — approved evaluator

- [ ] Add OPA/WASM/server adapter only after approval.
- [ ] Pin evaluator and verify bundle manifest/digest.
- [ ] Enforce limits/security/replay/supply-chain checks.

### Gate 8 — CI and operations

- [ ] Replace TODO workflows.
- [ ] Verify required checks/settings.
- [ ] Establish versioning/deprecation/compatibility.
- [ ] Test correction and rollback.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

- [ ] Reusability and ownership are demonstrated.
- [ ] Build backend, Python support, discovery, dependencies, license, and artifact inspection are complete.
- [ ] Import is effect-free.
- [ ] PolicyInputBundle schema/profile strategy is accepted.
- [ ] Native result contract and normalization are versioned/exhaustive.
- [ ] API exports are intentional/minimal.
- [ ] Bundle format/manifest/activation and evaluator profile are accepted/pinned.
- [ ] Reasons/obligations have governance.
- [ ] Evidence, rights, consent, sensitivity, lifecycle, receipts, review, and release remain external authorities.
- [ ] Public clients use governed envelopes.
- [ ] Unit/negative/property/security/no-network tests exist.
- [ ] PolicyDecision and PolicyInputBundle fixtures are expanded.
- [ ] Consumer integration and rollback tests exist.
- [ ] Meaningful CI replaces TODO echoes and settings are verified.
- [ ] Package/source/namespace docs agree.
- [ ] Correction/deprecation/rollback paths are current.

[Back to top](#top)

---

<a id="verification-register"></a>

## Verification register

| ID | Verification item | Status | Evidence required |
|---|---|---:|---|
| PRN-001 | Assign namespace owner | **NEEDS VERIFICATION** | Maintainer assignment. |
| PRN-002 | Confirm CODEOWNERS coverage | **UNKNOWN** | CODEOWNERS/settings inspection. |
| PRN-003 | Confirm package placement approval | **NEEDS VERIFICATION** | Directory Rules review. |
| PRN-004 | Confirm build backend | **UNKNOWN** | Completed manifest. |
| PRN-005 | Confirm supported Python versions | **UNKNOWN** | Metadata and CI. |
| PRN-006 | Confirm package discovery/import mapping | **UNKNOWN** | Artifact and clean import. |
| PRN-007 | Confirm license and dependencies | **UNKNOWN** | Approved metadata/review. |
| PRN-008 | Confirm accepted API/exports | **UNKNOWN** | Source/docs/tests/review. |
| PRN-009 | Confirm first consumer | **UNKNOWN** | Consumer integration. |
| PRN-010 | Confirm package tests/CI | **UNKNOWN** | Tests/workflow/settings. |
| PRN-011 | Strengthen PolicyInputBundle schema | **NEEDS VERIFICATION** | Schema/fixtures/migration. |
| PRN-012 | Define semantic input profile | **UNKNOWN** | Accepted contract/profile. |
| PRN-013 | Implement PolicyInputBundle validator | **UNKNOWN** | Source/tests. |
| PRN-014 | Resolve missing schema-declared validators | **CONFLICTED** | Add scripts or correct metadata. |
| PRN-015 | Accept bundle format/manifest | **UNKNOWN** | ADR/contracts/artifacts. |
| PRN-016 | Accept activation/selection contract | **UNKNOWN** | Governed binding. |
| PRN-017 | Confirm active bundle selection | **UNKNOWN** | Runtime/deployment evidence. |
| PRN-018 | Accept evaluator mode/version | **UNKNOWN** | ADR/security/config. |
| PRN-019 | Define native result vocabulary | **CONFLICTED** | Accepted contract. |
| PRN-020 | Define normalization mapping | **CONFLICTED** | Versioned mapping/tests. |
| PRN-021 | Define RESTRICT/HOLD handling | **UNKNOWN** | Policy-family decisions. |
| PRN-022 | Define reason-code registry | **UNKNOWN** | Accepted registry. |
| PRN-023 | Define obligation registry | **UNKNOWN** | Accepted registry/interpreters. |
| PRN-024 | Implement PolicyDecision candidate/validator | **UNKNOWN** | Source/schema tests. |
| PRN-025 | Expand PolicyDecision fixtures | **NEEDS VERIFICATION** | Enum/pattern/date/semantic cases. |
| PRN-026 | Establish mock evaluator protocol | **UNKNOWN** | Protocol/tests. |
| PRN-027 | Establish no-network/import-safety enforcement | **UNKNOWN** | Tests/CI. |
| PRN-028 | Define deterministic serialization/hashing | **UNKNOWN** | Versioned spec/tests. |
| PRN-029 | Define replay/freshness/supersession | **UNKNOWN** | Contract/integration tests. |
| PRN-030 | Confirm receipt/proof integration | **UNKNOWN** | Owning workflow evidence. |
| PRN-031 | Confirm DecisionEnvelope mapping | **UNKNOWN** | Explicit adapter/tests. |
| PRN-032 | Confirm rights/consent/sensitivity failure posture | **UNKNOWN** | Policy tests/fixtures. |
| PRN-033 | Confirm lifecycle/public exposure gates | **UNKNOWN** | Integration tests. |
| PRN-034 | Complete security/supply-chain review | **UNKNOWN** | Threat model/attestation. |
| PRN-035 | Replace policy-test TODO steps | **NEEDS VERIFICATION** | Meaningful workflow. |
| PRN-036 | Establish versioning/deprecation/correction | **UNKNOWN** | Accepted policies/runbook. |
| PRN-037 | Test software rollback | **UNKNOWN** | Drill/evidence. |
| PRN-038 | Confirm deployment/runtime/health | **UNKNOWN** | Config/logs/telemetry. |

Open items must not be upgraded by README edits alone.

[Back to top](#top)

---

<a id="drift-and-conflicts"></a>

## Drift and conflicts

| Topic | Observed state | Risk | Required handling |
|---|---|---|---|
| Namespace maturity | Broad README; placeholder code | False API assumptions | Record exact inventory. |
| Importability | Path exists; build/discovery absent | Source-tree imports mask packaging gap | Require clean artifact/import. |
| PolicyInputBundle | Rich contract; minimal permissive schema | Shape pass mistaken for readiness | Separate schema/profile validation. |
| Native outcomes | Prior docs use ALLOW/RESTRICT/HOLD | Incompatible mapping | Ratify normalization. |
| PolicyDecision outcomes | ANSWER/ABSTAIN/DENY/ERROR | Restrictions may be lost | Preserve obligations/mapping. |
| Validators | Schemas name absent files | Validation assumed | Add scripts or correct metadata. |
| Bundle lane | Design exists; no active instance | File presence mistaken for activation | Require explicit binding. |
| OPA | Mentioned; no accepted integration | Technology assumption ossifies | ADR/security/test decision. |
| Fixtures | Minimal coverage | Weak negative proof | Expand before adoption. |
| Policy CI | TODO echoes | Green check overread | Replace stubs. |
| Consumers | Broad callers named; no import found | Premature framework | Start with one consumer. |
| Public outcome | `ANSWER` misread as truth/release | Trust bypass | Keep evidence/release separate. |

When implementation, policy, contract, schema, fixture, validator, or runtime disagree: stop adoption, identify exact versions/authorities, preserve the conflict, resolve through proper review, update code/tests/docs together, and define migration/rollback. Namespace behavior must not silently become canonical.

[Back to top](#top)

---

<a id="maintenance-checklist"></a>

## Maintenance checklist

### Before change

- [ ] Pin base and blobs.
- [ ] Inspect package/source/namespace and contracts/schemas/policy bundles.
- [ ] Search consumers/duplicates.
- [ ] Check Directory Rules, ADRs, drift, and verification backlog.
- [ ] Identify rights/sensitivity/security impact.
- [ ] Define compatibility/rollback.

### During change

- [ ] Keep the smallest reusable mechanic.
- [ ] Preserve explicit inputs and vocabulary layers.
- [ ] Avoid hidden fetches, selection, and effects.
- [ ] Add tests with behavior.
- [ ] Keep policy rules outside package code.
- [ ] Synchronize docs and preserve unknowns/conflicts.

### Before review

- [ ] Build/install/import when applicable.
- [ ] Run unit/negative/property/security/no-network/schema/fixture/mock tests.
- [ ] Inspect artifacts and secrets/sensitive data.
- [ ] Read back remote blobs and confirm intended diff.

### Before merge/release

- [ ] Confirm owners/reviewers and meaningful required checks.
- [ ] Resolve/carry blockers.
- [ ] Confirm migration/deprecation/rollback.
- [ ] Do not treat merge as KFM publication.
- [ ] Do not activate a bundle through placement.

[Back to top](#top)

---

<a id="evidence-ledger"></a>

## Evidence ledger

| Evidence | Status | Supports | Does not support |
|---|---:|---|---|
| Prior target README | **CONFIRMED** | Documentation lineage. | Functional implementation. |
| Package pyproject | **CONFIRMED placeholder** | Name/version. | Build/import. |
| Empty `__init__.py` / comment-only `core.py` | **CONFIRMED** | Placeholder state. | API/behavior. |
| Directory Rules | **CONFIRMED doctrine** | Reusable package placement. | Namespace maturity. |
| PolicyInputBundle contract/schema | **CONFIRMED draft/PROPOSED** | Meaning and minimal shape. | Rich machine enforcement. |
| PolicyDecision contract/schema | **CONFIRMED draft/PROPOSED** | Canonical fields/enums. | Correct policy execution/release. |
| DecisionEnvelope contract | **CONFIRMED draft/PROPOSED** | Runtime transport distinction. | Public permission. |
| PolicyDecision fixtures | **CONFIRMED minimal** | One valid/invalid shape pair. | Exhaustive behavior. |
| Validator index / missing scripts | **CONFIRMED** | Expectations and bounded absence. | Executable validation. |
| Policy bundle README | **CONFIRMED README-only bounded state** | Governance design. | Active bundle. |
| Policy-test workflow | **CONFIRMED TODO-only** | Job names/echo behavior. | Enforcement. |
| Consumer search | **CONFIRMED bounded** | No functional import surfaced. | Permanent absence. |
| This revision | **CONFIRMED docs-only** | One README update. | Code/runtime/release change. |

[Back to top](#top)

---

<a id="rollback-correction-and-deprecation"></a>

## Rollback, correction, and deprecation

### Documentation rollback

Revert the documentation or eventual merge commit, or restore prior blob `34d6c813aaa5173fc6d936a6bb560a5db8981ece`. Preserve history; do not reset or force-rewrite shared history. Record the reason and re-run documentation checks.

### Software rollback expectations

Future behavior changes must identify prior version/commit, consumers, bundle/evaluator versions, contract/schema versions, decision/receipt consequences, safe restoration order, bundle-selection rollback, post-rollback validation, and correction/withdrawal duties.

Rolling back code does not automatically roll back decisions, receipts, proofs, releases, or public artifacts.

### Correction

Correct wrong claims with explicit truth labels and current evidence; preserve superseded history; update package/source/namespace docs together; record unresolved drift; never use documentation to canonize unreviewed behavior.

### Deprecation

No API is currently established. After adoption, deprecation must name the symbol/version, replacement, consumers, support window, warnings, old/new tests, normalization compatibility, migration record, and rollback.

### Immediate rollback triggers

Review and likely rollback are required if namespace code authors policy, activates bundles from file presence, accepts arbitrary bundle paths/endpoints, fetches missing governed facts, converts errors to answer, discards restrictions/holds/obligations, downgrades sensitivity, writes authoritative decisions/receipts/releases, exposes non-published lifecycle data, creates parallel contract/schema/outcome authority, logs secrets/sensitive data, or lets AI/UI state imply approval.

[Back to top](#top)

---

<a id="final-status"></a>

## Final status

**CONFIRMED:** `policy_runtime` is a repository-present namespace containing this README, an empty `__init__.py`, and a comment-only `core.py` under a `0.0.0` package scaffold.

**PROPOSED:** evolve it into a small explicit-input, fail-closed, deterministic policy-evaluation mechanics library only after contract, schema, bundle, evaluator, normalization, test, consumer, security, CI, compatibility, correction, and rollback gates are satisfied.

**CONFLICTED:** lower-level `ALLOW|RESTRICT|HOLD` vocabulary versus canonical `ANSWER|ABSTAIN|DENY|ERROR`; rich PolicyInputBundle semantics versus minimal schema; schema-declared validators versus missing scripts; bundle/evaluator intent versus no accepted activation binding.

**UNKNOWN:** installability, API, evaluator mode, bundle format, active policy, consumers, tests, CI enforcement, runtime integration, receipts/proofs, deployment, release use, and operational health.

**DO NOT CLAIM:** policy authority, evidence truth, rights/consent authority, sensitivity authority, release approval, publication, public safety, or production readiness.

[Back to top](#top)
