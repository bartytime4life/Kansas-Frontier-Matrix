<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://policy/bundles
title: policy/bundles/ — Governed Policy Bundle Boundary
type: policy-readme
version: v0.2
status: draft
owners: OWNER_TBD — Policy steward · Security steward · Policy-runtime steward · Contracts steward · Schema steward · Validation steward · Release steward · Docs steward
created: 2026-06-15
updated: 2026-07-14
policy_label: "restricted-review; policy-bundle-boundary; finite-outcomes; explicit-inputs; immutable-digests; fail-closed; evidence-aware; rights-aware; sensitivity-aware; release-gated; replayable; rollback-aware; no-secrets; no-hidden-fetches; no-directory-activation; no-public-bundle-selection"
current_path: policy/bundles/README.md
truth_posture: CONFIRMED policy/bundles README path, canonical singular policy root, policy bundle responsibility under policy/, paired PolicyInputBundle and PolicyDecision contracts and schemas, concrete PolicyDecision outcome and policy-family enums, minimal PolicyDecision fixtures and common schema harness, policy-runtime package version 0.0.0 placeholder, absent declared dedicated policy validators, TODO-only policy-test workflow, and search-limited README-only bundle-lane inventory / PROPOSED bundle artifact, manifest, lock, build, signing, activation, replay, and rollback contracts / CONFLICTED engine-native policy result vocabulary versus canonical PolicyDecision outcome vocabulary, policy schema fixture paths, policy schema x-kfm policy path, promotion/redaction schema overlap, and accepted evaluator/bundle format / UNKNOWN executable bundle artifacts, manifest instances, direct consumers, runtime selection, policy-engine binding, activation state, deployment state, receipt emission, branch protection, and production enforcement / NEEDS VERIFICATION accepted owners, canonical bundle format, deterministic builder, manifest schema home, reason-code and obligation registries, dependency closure, tests, CI, signatures, receipt/proof links, retention, supersession, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 8c8a8d8b216030ed32fb440deadb37968841e03e
  prior_blob: 2e52fa9b8c4bd12d5847244dec9a5c68e4f29d0d
  bounded_path_search: policy/bundles/README.md and repository-indexed bundle terminology
related:
  - ../README.md
  - ../access/README.md
  - ../ai_builder/README.md
  - ../decision/README.md
  - ../../packages/policy-runtime/README.md
  - ../../contracts/policy/README.md
  - ../../contracts/policy/policy_input_bundle.md
  - ../../contracts/policy/policy_decision.md
  - ../../schemas/contracts/v1/policy/README.md
  - ../../schemas/contracts/v1/policy/policy_input_bundle.schema.json
  - ../../schemas/contracts/v1/policy/policy_decision.schema.json
  - ../../tools/validators/policy/README.md
  - ../../fixtures/contracts/v1/policy/policy_decision/README.md
  - ../../tests/schemas/test_common_contracts.py
  - ../../.github/workflows/policy-test.yml
  - ../../docs/adr/ADR-0003-policy-singular-is-canonical-(policies-is-compatibility).md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/doctrine/trust-membrane.md
  - ../../docs/architecture/contract-schema-policy-split.md
  - ../../docs/registers/DRIFT_REGISTER.md
  - ../../apps/governed-api/README.md
tags: [kfm, policy, bundles, manifest, rego, opa, policy-runtime, PolicyInputBundle, PolicyDecision, finite-outcomes, reason-codes, obligations, deterministic-build, digest, replay, fail-closed, release-gated, rollback]
notes:
  - "The bounded repository search surfaced this README for policy/bundles and did not surface an executable bundle, bundle manifest instance, bundle lock, bundle registry, or direct runtime selection file in this lane. Treat the lane as README-only unless a later recursive checkout proves otherwise."
  - "The policy runtime package is version 0.0.0 and indexed implementation references resolve to README documentation rather than evaluator code. Runtime execution remains unproved."
  - "PolicyInputBundle has a permissive PROPOSED schema requiring only id. PolicyDecision has a concrete PROPOSED schema with outcomes ANSWER, ABSTAIN, DENY, and ERROR and policy families promotion, access, render, capability, consent, and sensitivity."
  - "The dedicated validator paths declared by the policy schemas were not found. The common schema fixture harness and one valid/one invalid PolicyDecision fixture family are repository-present."
  - "The policy-test workflow currently echoes TODO for OPA tests and fixture coverage. Workflow success does not prove policy behavior until meaningful checks replace those stubs."
  - "Only this Markdown file changes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Policy Bundles

`policy/bundles/`

> Governed boundary for immutable, reviewable, replayable policy bundle artifacts and their manifests. This lane may package accepted policy source for an approved evaluator, but it is not the policy runtime, input schema, decision contract, receipt store, release authority, or public trust path.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.2-informational)
![maturity](https://img.shields.io/badge/maturity-README--only-lightgrey)
![authority](https://img.shields.io/badge/authority-policy__bundle__boundary-6f42c1)
![outcomes](https://img.shields.io/badge/canonical__outcomes-ANSWER%20%7C%20ABSTAIN%20%7C%20DENY%20%7C%20ERROR-0b7285)
![default](https://img.shields.io/badge/default-fail__closed-critical)
![activation](https://img.shields.io/badge/directory__activation-forbidden-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status-and-evidence) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Repo fit](#repository-fit-and-directory-rules-basis) · [Bundle classes](#bundle-artifact-classes) · [Manifest](#minimum-bundle-manifest-contract) · [Identity](#identity-version-digest-and-canonicalization) · [Composition](#composition-and-dependency-closure) · [Inputs](#policy-input-binding) · [Decisions](#decision-vocabulary-and-normalization) · [Activation](#activation-selection-and-deployment) · [Lifecycle](#bundle-lifecycle-and-promotion) · [Supply chain](#build-and-supply-chain-controls) · [Reasons](#reason-codes-and-obligations) · [Audit](#audit-replay-receipts-and-retention) · [Sensitivity](#rights-sensitivity-and-data-minimization) · [Failure](#failure-behavior) · [Threats](#threat-model) · [Validation](#validation-and-test-matrix) · [Implementation](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Rollback](#rollback-correction-and-supersession)

> [!IMPORTANT]
> **Document lifecycle:** draft `v0.2`<br>
> **Observed lane maturity:** README-only in the bounded repository search<br>
> **Authority:** policy-bundle packaging and manifest boundary only<br>
> **Runtime posture:** no accepted bundle format, bundle instance, manifest instance, evaluator binding, active selection, or deployed enforcement is established by this README

> [!CAUTION]
> File presence is never activation. A valid archive, successful schema check, OPA-compatible directory, matching digest, or `ANSWER` decision does not authorize release or publication. Missing or stale bundle identity, input context, evidence, rights, sensitivity, review, evaluator integrity, reason-code mapping, obligation handling, release state, correction path, or rollback support must fail closed.

---

## Purpose

`policy/bundles/` is the canonical policy-root sublane for packaging reviewed policy source into an immutable evaluation unit and describing that unit with inspectable metadata.

A future bundle may support:

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
| `policy/bundles/README.md` | **CONFIRMED** | This README exists and previously documented a proposed bundle boundary. |
| Other indexed files in `policy/bundles/` | **NOT SURFACED IN BOUNDED SEARCH** | No executable bundle, manifest instance, lock, registry, signature, or bundle-local test file was found. This is search-limited, not proof of permanent absence. |
| Canonical policy root | **CONFIRMED repository-present** | `policy/` exists and is the singular policy authority root; the root README remains a short `PROPOSED` scaffold. |
| Policy-root ADR | **CONFIRMED repository-present / PROPOSED ADR** | ADR-0003 records `policy/` as canonical and `policies/` as compatibility if present. Its acceptance status remains proposed. |
| `PolicyInputBundle` contract | **CONFIRMED** | Semantic contract exists and explicitly forbids hidden fact fetching. |
| `PolicyInputBundle` schema | **CONFIRMED / PROPOSED PERMISSIVE STUB** | Requires only `id`; allows additional properties. Rich policy context is not yet machine-enforced. |
| `PolicyDecision` contract | **CONFIRMED** | Semantic contract exists and distinguishes engine-native results from canonical outcomes. |
| `PolicyDecision` schema | **CONFIRMED / PROPOSED CONCRETE SHAPE** | Requires six fields and permits only `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`. |
| PolicyDecision fixtures | **CONFIRMED MINIMAL COVERAGE** | One valid fixture and one invalid missing-`decision_id` fixture are documented. |
| Common schema harness | **CONFIRMED CODE** | `tests/schemas/test_common_contracts.py` discovers policy schemas with matching fixture directories. |
| Dedicated policy validators | **ABSENT AT DECLARED PATHS** | `tools/validators/validate_policy_decision.py` and `tools/validators/policy/validate_policy_input_bundle.py` were not found. |
| Policy validator index | **CONFIRMED README** | Validator expectations are documented; executable policy validation remains unproved. |
| Policy runtime package | **CONFIRMED PLACEHOLDER** | `pyproject.toml` declares `kfm-policy-runtime` version `0.0.0`; indexed evaluator references lead to READMEs, not code. |
| Policy-test workflow | **CONFIRMED TODO-ONLY** | OPA tests and fixture coverage are echo stubs. A successful run does not prove policy behavior. |
| Accepted bundle format | **UNKNOWN** | OPA directory bundle, tarball, WASM package, or another format has not been accepted in inspected evidence. |
| Active bundle selection | **UNKNOWN** | No allowlisted selector, deployment binding, or active bundle registry is confirmed. |
| Receipt/proof linkage | **NEEDS VERIFICATION** | Required for consequential replay, but no accepted bundle-evaluation receipt path was established here. |

### Evidence boundary

This README may confidently state repository presence and inspected file contents. It must not claim:

- production policy enforcement;
- active bundle deployment;
- runtime compatibility;
- complete policy coverage;
- branch-protection enforcement;
- accepted signing;
- bundle registry operation;
- receipt emission;
- public release safety.

Those remain `UNKNOWN` or `NEEDS VERIFICATION` until tests, runtime evidence, manifests, receipts, or deployment records prove them.

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

`policy/bundles/` belongs under the singular `policy/` responsibility root because bundles package executable policy authority.

```text
policy/
├── README.md
├── access/
├── ai_builder/
├── decision/
├── domains/
├── sensitivity/
├── rights/
├── runtime/
├── promotion/
├── release/
└── bundles/
    └── README.md
```

The tree above is a responsibility map, not a confirmed exhaustive inventory.

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

### Placement constraints

- `policy/` is singular and canonical.
- `policies/`, if present, must remain a compatibility lane and cannot evolve independently.
- Bundle artifacts must not be copied into `packages/policy-runtime/` as a second policy authority.
- Bundle manifests must not be placed in `release/` merely because a bundle is deployed; release manifests and policy bundle manifests are different object families.
- Schema files must not be placed beside bundle instances.
- Emitted evaluation receipts must not be stored as bundle source.
- Domain-specific policies may be included by reference, but the bundle does not transfer domain ownership into this directory.
- Creating a parallel `bundles/` root or `policies/bundles/` authority requires an accepted ADR or migration decision.

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

The semantic contract expects operation, audience, object, evidence, source, rights, sensitivity, review, release, and evaluator context. The current schema, however:

- requires only `id`;
- optionally shapes `spec_hash` and `version`;
- allows arbitrary additional properties;
- remains `PROPOSED`.

Therefore:

- schema validity alone is insufficient;
- a bundle must not assume rich fields are machine-enforced;
- callers and policy modules must not silently disagree on field names;
- accepted profiles must version the expected semantic field set;
- missing facts must remain explicitly unresolved;
- hidden fetches are forbidden.

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

The current `PolicyDecision` schema does not carry all of those fields. Do not add undeclared properties to a `PolicyDecision` instance because `additionalProperties` is `false`. Carry replay metadata in an accepted `DecisionEnvelope`, evaluation receipt, or future schema revision.

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

KFM currently documents two layers:

1. **Engine-native or internal policy result classes**
   `ALLOW | RESTRICT | HOLD | DENY | ABSTAIN | ERROR`

2. **Canonical `PolicyDecision.outcome` values confirmed by schema**
   `ANSWER | ABSTAIN | DENY | ERROR`

These must not be mixed in one field or described as interchangeable.

### Required normalization

| Engine-native result | Canonical outcome | Required handling |
|---|---|---|
| `ALLOW` | `ANSWER` | Proceed only for the evaluated operation and audience; preserve any citations and release gates. |
| `RESTRICT` | `ANSWER` | `obligations` must encode every enforceable restriction; caller fails closed if any obligation cannot be satisfied. |
| `HOLD` | `ABSTAIN` | Reasons identify pending review/maturity/support safely; obligations may require steward review or reevaluation. |
| `ABSTAIN` | `ABSTAIN` | Preserve unresolved support and do not turn it into a denial or answer. |
| `DENY` | `DENY` | Preserve safe reason code; do not reveal protected facts. |
| `ERROR` | `ERROR` | Preserve evaluator/process failure; never normalize to `ANSWER`. |

### Canonical policy family

The current `PolicyDecision.policy_family` enum is:

- `promotion`;
- `access`;
- `render`;
- `capability`;
- `consent`;
- `sensitivity`.

`bundle` is not a policy family in the current schema. Bundle packaging, integrity, or selection failure must map to the gate family being evaluated, with an appropriate reason, or to a separately accepted future contract. Do not emit an invalid `policy_family: "bundle"` merely because the bundle failed.

### Composition rules

When multiple policy evaluations apply:

- do not let `ANSWER` override `DENY`;
- do not let an empty result become `ANSWER`;
- preserve `ERROR` as a process failure;
- preserve `ABSTAIN` when evidence or authority is unresolved;
- apply the most restrictive unsatisfied obligation;
- record which family and bundle version produced each decision;
- use an accepted aggregation contract rather than free-text precedence.

A safe default aggregation posture is:

```text
ERROR or DENY blocks
ABSTAIN prevents authoritative answer/publication
ANSWER proceeds only when every required obligation is enforceable
```

This is a `PROPOSED` composition rule until accepted in contracts, policy, tests, and runtime.

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

Reason codes should be:

- stable;
- versioned;
- public-safe;
- gate-specific where necessary;
- append-only when practical;
- separable from sensitive internal detail;
- covered by fixtures and metrics;
- mapped to a human-readable explanation.

Examples of `PROPOSED` bundle/runtime reason families:

```text
bundle.missing
bundle.digest_mismatch
bundle.manifest_invalid
bundle.withdrawn
bundle.unsupported_evaluator
bundle.entrypoint_missing
bundle.dependency_incomplete
input.missing_operation
input.missing_audience
input.schema_invalid
evidence.unresolved
rights.unknown
sensitivity.unresolved
review.required
obligation.unsupported
runtime.timeout
runtime.undefined_result
runtime.multiple_results
```

These are examples, not an accepted registry.

### Obligations

Obligations must be executable downstream duties, not advisory prose.

Examples already documented by the `PolicyDecision` contract include:

- `attach_citation`;
- `redact_coordinates`;
- `generalize_geometry`;
- `withhold_exact_location`;
- `require_steward_review`;
- `delay_publication`;
- `attach_rights_notice`;
- `block_export`;
- `rollback_check_required`.

Before an obligation is allowed in an active bundle:

- define its exact semantics;
- identify the responsible interpreter;
- define success and failure;
- define ordering and composition;
- test supported and unsupported consumers;
- ensure logs do not leak protected values;
- fail closed when the caller cannot enforce it.

`RESTRICT` must not disappear during normalization: it becomes `ANSWER` only with complete, enforceable obligations.

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

The repository's `policy-test` workflow currently performs:

```text
echo TODO opa-test
echo TODO policy-fixture-coverage
```

Therefore a green workflow run proves only that those echo commands ran. It does not prove:

- OPA/Rego syntax;
- bundle assembly;
- digest reproducibility;
- manifest validation;
- policy behavior;
- outcome normalization;
- obligation enforcement;
- runtime selection;
- replay;
- rollback.

[Back to top](#top)

---

## Smallest sound implementation sequence

This sequence is `PROPOSED` and preserves reversible change.

1. **Confirm bundle format and evaluator.**
   Accept OPA directory/tar bundle, WASM, or another explicit profile.

2. **Define semantic manifest contract.**
   Keep bundle manifest meaning under `contracts/policy/` or another Directory-Rules-approved contract path.

3. **Create restrictive manifest schema.**
   Use `schemas/contracts/v1/policy/` only after checking overlap and schema naming rules.

4. **Define engine-result mapping contract.**
   Version the mapping to canonical `PolicyDecision`.

5. **Define reason-code and obligation registries.**
   Specify interpreters and failure behavior.

6. **Build one synthetic bundle.**
   Use non-sensitive toy rules covering one policy family.

7. **Add deterministic builder and lock.**
   Keep implementation in the appropriate tool/package root, not in this README lane.

8. **Add valid, invalid, deny, restrict, hold, abstain, and error fixtures.**

9. **Implement dedicated validators.**
   Reconcile the currently missing declared validator paths.

10. **Replace TODO workflow jobs with meaningful checks.**

11. **Add shadow/replay integration.**
   Do not activate in public paths.

12. **Add reviewed activation and rollback records.**

13. **Add receipt/proof linkage.**

14. **Promote only after acceptance gates pass.**

The first implementation should be a thin slice, not a repository-wide policy rewrite.

[Back to top](#top)

---

## Definition of done

### Documentation boundary

- [x] Canonical root and adjacent authority boundaries are explicit.
- [x] Current repository maturity is separated from proposal.
- [x] Engine-native and canonical decision vocabularies are separated.
- [x] No bundle, evaluator, validator, CI, activation, receipt, or deployment maturity is overclaimed.
- [x] Failure, threat, replay, correction, and rollback posture is explicit.

### First candidate bundle

- [ ] Accepted owners and reviewers are assigned.
- [ ] Bundle format, builder, evaluator, capabilities, and entrypoints are accepted.
- [ ] Semantic bundle-manifest contract exists.
- [ ] Restrictive bundle-manifest schema exists.
- [ ] Immutable version and digest rules are enforced.
- [ ] Complete source/dependency lock exists.
- [ ] Deterministic clean build passes.
- [ ] Artifact and manifest digest verification passes.
- [ ] PolicyInputBundle profile is explicit and semantically validated.
- [ ] PolicyDecision normalization passes current schema.
- [ ] Reason-code registry is accepted.
- [ ] Obligation registry and caller interpreters are accepted.
- [ ] Valid, invalid, deny, restrict, hold, abstain, error, stale, withdrawn, and adversarial fixtures pass.
- [ ] Dedicated validators exist and declared paths are correct.
- [ ] No-network, secret, archive-safety, and sensitive-data checks pass.
- [ ] Policy-test workflow runs meaningful checks.
- [ ] Policy, security, domain, rights, sensitivity, and release-adjacent reviews close as applicable.
- [ ] Shadow/replay behavior is verified.
- [ ] External activation binding is immutable and auditable.
- [ ] Evaluation receipts bind input, bundle, evaluator, and decision.
- [ ] Rollback target is present, reviewed, compatible, and not withdrawn.
- [ ] Public clients cannot enumerate, upload, select, or bypass bundles.

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
| Accepted bundle format | **NEEDS VERIFICATION** | ADR, contract, builder, and tested example. |
| Bundle lane inventory | **NEEDS VERIFICATION** | Recursive checkout or tree listing beyond indexed search. |
| Manifest schema home | **NEEDS VERIFICATION** | Directory Rules review and schema/contract split. |
| Policy runtime implementation | **UNKNOWN** | Importable code, package tests, and runtime logs. |
| Evaluator family/version | **UNKNOWN** | Accepted configuration and successful tests. |
| Deterministic builder | **UNKNOWN** | Code, clean rebuild comparison, and validation report. |
| Bundle selector/activation | **UNKNOWN** | Deployment/activation record and consumer binding. |
| Dedicated validators | **ABSENT AT DECLARED PATHS** | Implemented files and tests. |
| PolicyInputBundle restrictive shape | **NEEDS VERIFICATION** | Schema revision and fixtures. |
| PolicyDecision mapping | **NEEDS VERIFICATION** | Mapping contract, runtime adapter, fixtures, and tests. |
| Reason-code registry | **NEEDS VERIFICATION** | Versioned accepted registry. |
| Obligation registry/interpreters | **NEEDS VERIFICATION** | Contract, consumer matrix, and negative tests. |
| Bundle signatures | **UNKNOWN** | Trust model, key custody, verification, revocation. |
| Receipt/proof home | **NEEDS VERIFICATION** | Accepted contract, path, instances, and replay test. |
| Retention policy | **NEEDS VERIFICATION** | Governance decision and deletion/access controls. |
| Policy-test CI | **CONFIRMED TODO-ONLY** | Real OPA/bundle/fixture/normalization checks. |
| Branch protection/review enforcement | **UNKNOWN** | Repository rules and protected-check evidence. |
| Public API enforcement | **UNKNOWN** | Implemented trust-membrane integration and tests. |
| Rollback automation | **UNKNOWN** | Runbook, selection rollback, cache invalidation, drill. |
| Generated-receipt requirement for docs changes | **NEEDS VERIFICATION** | Accepted AI-build/provenance enforcement path. |

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

- the first bundle file is added;
- a manifest contract or schema is accepted;
- evaluator code appears;
- dedicated validators are implemented;
- policy-test stops being TODO-only;
- active bundle selection is introduced;
- reason-code or obligation vocabularies change;
- `PolicyDecision` schema changes;
- a signing/attestation process is added;
- a bundle is withdrawn or rolled back;
- `policy/` versus compatibility-root placement changes.

[Back to top](#top)

---

## ADRs and drift triggers

No new ADR is created by this README.

Separate governance is required to:

- accept the bundle format;
- accept a bundle manifest contract/schema;
- change the canonical policy root;
- create a parallel bundle root;
- accept evaluator/compiler compatibility policy;
- change canonical PolicyDecision outcome or family enums;
- accept reason-code or obligation registries;
- allow network-dependent builds;
- introduce signing keys or trust roots;
- define production activation;
- define public/client bundle selection;
- merge bundle activation with release approval;
- move receipts or proofs into this lane.

Record drift when:

- a bundle exists without a manifest;
- manifests and artifacts disagree;
- a mutable alias is used by runtime;
- `policies/` evolves independently;
- bundle copies exist under packages, apps, release, or artifacts;
- schema-declared validator paths remain stale;
- workflow success is cited as policy proof while jobs remain TODO stubs;
- engine-native results are stored directly as canonical PolicyDecision outcomes.

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

**2026-07-14**, against `main@8c8a8d8b216030ed32fb440deadb37968841e03e`.

Review again before the first non-README bundle artifact, manifest instance, dependency lock, evaluator binding, dedicated validator, real policy-test job, active selector, receipt integration, signature, deployment, or rollback drill.
