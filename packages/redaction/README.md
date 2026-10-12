<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION/packages-redaction-readme
title: packages/redaction/ — Package Boundary and Greenfield Public-Safe Transform Scaffold
type: readme
version: v1.1
prior_version: v1
status: draft
owners: OWNER_TBD — Redaction steward · Sensitivity steward · Policy steward · Contracts steward · Schema steward · Security/privacy steward · Validation steward · Package steward · Runtime/API steward · Release steward · CI steward · Docs steward
created: NEEDS VERIFICATION — target file existed before the evidence-grounded revisions
updated: 2026-07-19
policy_label: "public-doctrine; package-boundary; python-package-scaffold; greenfield-placeholder; build-unconfigured; no-supported-api; explicit-inputs; no-hidden-fetches; no-network-by-default; deterministic-transform-candidate; fail-closed; sensitive-data-minimization; policy-authority-external; contract-schema-subordinate; receipt-candidate-only; evidence-subordinate; release-subordinate; no-publication-authority; compatibility-unratified; correction-aware; rollback-aware"
current_path: packages/redaction/README.md
truth_posture: >
  CONFIRMED target README v1 before this revision, repository-present packages/redaction package,
  kfm-redaction distribution metadata version 0.0.0, merged source-envelope README v1.1, merged
  redaction namespace README v1.1, empty redaction/__init__.py, comment-only redaction/core.py
  greenfield placeholder, root Hatchling configuration that delegates subpackages to their own
  manifests, packages responsibility-root doctrine, draft shared RedactionReceipt contract,
  permissive empty PROPOSED redaction-receipt schema, placeholder PROPOSED
  policy/redaction/profiles.yaml, draft redaction-profile and determinism standards, and bounded
  absence of functional package modules, supported exports, consumer imports, package-local
  tests, receipt persistence, release integration, deployment, or runtime health / PROPOSED a
  small reusable Python package for explicit deterministic protective-transform mechanics,
  candidate validation, replay-safe metadata, and synthetic test support / CONFLICTED prior
  README implications that proposed module names, imports, helper outcomes, package layout, and
  broad consumers were usable implementation despite the placeholder inventory / UNKNOWN
  accepted public API, build backend, Python support policy for this subpackage, package
  discovery, dependencies, module decomposition, profile activation, first consumer, test home,
  CI enforcement, deployment, operational health, and release use / NEEDS VERIFICATION owners,
  package metadata completion, API approval, contract/schema/profile acceptance, implementation,
  validators, fixtures, security review, compatibility policy, correction process, and rollback
  drills
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 5cf7386b17a85feeadbb82a0eb9ec92bded68279
  prior_blob: 0003edfa3ac8de43d50f9b8ca72da356b9e534d0
  source_readme_blob: a8dcc3b2006414046487fcb82f8264af7d08c555
  namespace_readme_blob: 73d0a320b4a08d105aeb3d8822e421c74e356d7f
  package_metadata_blob: 72ef9d9a76407e2d8fc959d0a3f1f493dfa232c7
  root_pyproject_blob: e3bd40e8e6ce14dfcde78ff5c09608095c3eca76
  namespace_init_blob: e69de29bb2d1d6434b8b29ae775ad8c2e48c5391
  namespace_core_blob: 173f1a6eab02c47d829126e6b1c0bd5a5e836adb
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  shared_receipt_contract_blob: c686cdf5c79a8b99ac66d4b01cd30d2f450f645f
  receipt_schema_blob: 6251119ecc2293cd219e4ddfa5bbde8b9d6f8f24
  profile_registry_blob: e928e91ccf278fe42ac0cd83f571ba323787573d
  profile_standard_blob: 402abcf3e231db1c2ede5ed09d0d373d574e5053
  determinism_standard_blob: 9b3f54f23fc835d4c589c0edbeada72f88766f4d
  bounded_path_checks:
    - packages/redaction/README.md existed at version v1 before this revision
    - packages/redaction/pyproject.toml declares only project name kfm-redaction and version 0.0.0
    - package pyproject declares no build-system, Python requirement, package discovery, dependencies, scripts, entry points, optional dependencies, license, authors, or tool configuration
    - root pyproject uses Hatchling for the root kfm project and states subpackages carry their own pyproject files
    - packages/redaction/src/README.md exists at version v1.1 on main
    - packages/redaction/src/redaction/README.md exists at version v1.1 on main
    - packages/redaction/src/redaction/__init__.py is empty
    - packages/redaction/src/redaction/core.py is a comment-only greenfield placeholder
    - bounded repository search surfaced no functional redaction consumer import or package-test reference
    - shared RedactionReceipt semantics remain draft and PROPOSED
    - redaction-receipt schema remains a permissive scaffold with no declared properties
    - policy/redaction/profiles.yaml remains a PROPOSED placeholder with no confirmed active profile
related:
  - ../README.md
  - pyproject.toml
  - src/README.md
  - src/redaction/README.md
  - src/redaction/__init__.py
  - src/redaction/core.py
  - ../../pyproject.toml
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/doctrine/trust-membrane.md
  - ../../docs/doctrine/lifecycle-law.md
  - ../../docs/architecture/sensitive-domain-fail-closed.md
  - ../../docs/standards/REDACTION_PROFILES.md
  - ../../docs/standards/REDACTION_DETERMINISM.md
  - ../../docs/standards/SENSITIVITY_RUBRIC.md
  - ../../docs/security/DATA_CLASSIFICATION.md
  - ../../contracts/shared/redaction_receipt.md
  - ../../schemas/contracts/v1/receipts/redaction_receipt.schema.json
  - ../../policy/redaction/profiles.yaml
  - ../../docs/registers/DRIFT_REGISTER.md
  - ../../data/receipts/generated/README.md
  - ../../schemas/contracts/v1/receipts/generated_receipt.schema.json
tags: [kfm, packages, redaction, python, package, scaffold, public-safe-transform, geoprivacy, sensitivity, privacy, deterministic, replay, fail-closed, receipts, compatibility, correction, rollback]
notes:
  - "v1.1 aligns the package-level README with the merged source-envelope and namespace v1.1 boundaries."
  - "This README defines package ownership, packaging, adoption, compatibility, validation, and rollback burdens; source-file admission belongs to src/README.md and namespace/API detail belongs to src/redaction/README.md."
  - "This README does not make the package installable, define a supported API, accept a redaction profile, implement a transform, write a receipt, authorize release, or prove operational safety."
  - "The package remains a greenfield placeholder at the recorded evidence snapshot."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Redaction Package Boundary and Greenfield Public-Safe Transform Scaffold

`packages/redaction/`

> Package-level governance, packaging, adoption, compatibility, and rollback boundary for a future reusable Python redaction and public-safe transformation library. Current evidence establishes a `0.0.0` metadata stub, two evidence-grounded child READMEs, an empty package initializer, and a comment-only `core.py` placeholder—not an installable distribution, functional redactor, profile engine, geometry generalizer, supported API, receipt writer, policy evaluator, release component, or publication authority.

![status](https://img.shields.io/badge/status-draft-yellow)
![version](https://img.shields.io/badge/version-v1.1-informational)
![maturity](https://img.shields.io/badge/maturity-greenfield__placeholder-lightgrey)
![distribution](https://img.shields.io/badge/distribution-kfm--redaction-blue)
![package-version](https://img.shields.io/badge/package__version-0.0.0-lightgrey)
![build](https://img.shields.io/badge/build-unconfigured-orange)
![exports](https://img.shields.io/badge/exports-none-orange)
![tests](https://img.shields.io/badge/package__tests-not__established-orange)
![authority](https://img.shields.io/badge/publication__authority-none-red)

**Quick links:** [Purpose](#purpose) · [Impact](#impact-and-operating-posture) · [Evidence](#status-and-evidence) · [Placement](#directory-rules-and-authority) · [Inventory](#confirmed-package-inventory) · [Layers](#package-source-and-namespace-layers) · [Packaging](#packaging-build-import-and-api-status) · [Vocabulary](#bounded-context-and-ubiquitous-language) · [Responsibilities](#proposed-package-responsibility-envelope) · [Exclusions](#explicit-non-responsibilities) · [Contracts](#contract-schema-policy-profile-and-standard-boundaries) · [Inputs](#input-and-semantic-completeness-boundary) · [Transforms](#transform-and-profile-boundary) · [Outputs](#output-and-redactionreceipt-candidate-boundary) · [Outcomes](#outcome-vocabularies-and-fail-closed-behavior) · [Lifecycle](#lifecycle-and-trust-membrane) · [Dependencies](#dependency-direction) · [Effects](#inputs-outputs-and-side-effects) · [Reliability](#determinism-canonicalization-identity-replay-and-freshness) · [Security](#security-privacy-and-threat-model) · [Supply chain](#dependencies-supply-chain-and-resource-bounds) · [Telemetry](#logging-telemetry-and-error-hygiene) · [Consumers](#consumer-adoption-versioning-and-compatibility-boundary) · [Testing](#testing-fixtures-and-ci) · [Implementation](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Open](#verification-register) · [Drift](#drift-and-conflicts) · [Maintenance](#maintenance-and-change-review) · [Compatibility](#versioning-deprecation-correction-and-revocation) · [Evidence ledger](#evidence-ledger) · [Rollback](#rollback)

> [!IMPORTANT]
> **This README is not implementation evidence for redaction.** It does not establish installation, import success, exports, accepted profiles, transform correctness, policy integration, receipt persistence, consumer adoption, tests, CI enforcement, deployment, release use, or operational health.

> [!CAUTION]
> **Redaction is not truth or publication.** A protective transform cannot create evidence, cure unresolved rights or consent, downgrade sensitivity, satisfy review, authorize release, promote lifecycle state, or make generated language authoritative.

---

## Purpose

This README defines the package-level responsibility, packaging, trust, adoption, compatibility, validation, correction, and rollback boundary for:

```text
packages/redaction/
```

The package is intended to become a **small reusable library** of explicit-input, deterministic, fail-closed protective-transform mechanics shared by more than one governed API, pipeline, worker, tile builder, export path, validator, review tool, release gate, or maintenance utility.

The current repository state is narrower:

- `pyproject.toml` declares only `kfm-redaction` version `0.0.0`;
- the package manifest does not define a build backend, supported Python version, package discovery, dependencies, scripts, entry points, license, authors, or test configuration;
- `src/README.md` and `src/redaction/README.md` are evidence-grounded v1.1 boundary documents;
- `src/redaction/__init__.py` is empty;
- `src/redaction/core.py` is a comment-only greenfield placeholder;
- no functional package module, supported export, consumer import, package-local test lane, profile binding, receipt workflow, deployment, or runtime behavior is established;
- the governing redaction contract, schema, profile catalog, and determinism rules remain draft, permissive, placeholder, or PROPOSED.

This README therefore has three jobs:

1. record the **CONFIRMED placeholder state** without turning design intent into implementation fact;
2. define a **PROPOSED reusable package boundary** for future protective-transform mechanics; and
3. make packaging, contracts, schemas, policy, profiles, evidence, sensitivity, security, validation, compatibility, correction, and rollback burdens explicit before adoption.

[Back to top](#top)

---

## Impact and operating posture

| Surface | Current status | Package effect | Required posture |
|---|---:|---|---|
| Repository placement | **CONFIRMED** | Package exists under `packages/`. | Preserve shared-library responsibility. |
| Distribution metadata | **CONFIRMED placeholder** | Name and version exist. | Do not claim installability. |
| Source envelope | **CONFIRMED placeholder** | `src/` and one namespace exist. | Keep source admission narrow and evidence-backed. |
| Functional behavior | **NOT ESTABLISHED** | No transform behavior is implemented. | Treat algorithms and modules as proposals only. |
| Public API | **NOT ESTABLISHED** | No exports or compatibility promise exists. | No consumer may rely on README-only imports. |
| Redaction profiles | **NOT ESTABLISHED** | Registry is a placeholder. | File presence must never activate a profile. |
| RedactionReceipt | **DRAFT / PROPOSED** | Meaning exists separately; schema is permissive. | Candidate metadata only; no persistence authority. |
| Determinism | **DOCUMENTED / UNPROVED** | Standards describe intended burden. | Require executable vectors before support. |
| Consumers | **NOT ESTABLISHED** | Broad callers are design targets only. | Start with one governed consumer. |
| Tests and CI | **NOT ESTABLISHED for package behavior** | No package proof exists. | Add negative and replay tests before adoption. |
| Deployment and health | **UNKNOWN** | No runtime integration is proved. | Do not claim operational readiness. |
| Release and publication | **NONE** | Package has no release authority. | Preserve downstream gates and rollback. |

The package should reduce duplicated implementation risk. It must not become a shortcut around policy, contracts, schemas, evidence, rights, sensitivity, review, receipts, proofs, release, correction, or governed public interfaces.

[Back to top](#top)

---

## Status and evidence

| Surface | Status | Safe conclusion |
|---|---:|---|
| Target package README | **CONFIRMED v1 before revision** | The prior guide over-described implementation. |
| Package path | **CONFIRMED present** | `packages/redaction/` exists. |
| Subpackage metadata | **CONFIRMED placeholder** | `kfm-redaction`, version `0.0.0`. |
| Subpackage build/discovery | **NOT DECLARED** | Build, install, and import are unproved. |
| Root Python project | **CONFIRMED Hatchling root scaffold** | It configures root `kfm`, not this subpackage. |
| Source README | **CONFIRMED v1.1** | Source-admission boundary is evidence-grounded. |
| Namespace README | **CONFIRMED v1.1** | Namespace/API boundary is evidence-grounded. |
| `src/redaction/__init__.py` | **CONFIRMED empty** | No supported exports. |
| `src/redaction/core.py` | **CONFIRMED comment-only** | No transform behavior. |
| Functional modules | **NOT ESTABLISHED by bounded inspection** | Prior proposed module names are not facts. |
| Consumer imports | **NOT ESTABLISHED by bounded search** | No adoption behavior is proved. |
| Package-local tests | **NOT ESTABLISHED by bounded search** | No behavior is proved. |
| Shared `RedactionReceipt` contract | **CONFIRMED draft / PROPOSED** | Cross-domain receipt meaning exists separately. |
| Redaction receipt schema | **CONFIRMED permissive PROPOSED scaffold** | It declares no properties and allows additional fields. |
| Redaction profile registry | **CONFIRMED placeholder / PROPOSED** | No active profile is proved. |
| Redaction profiles standard | **CONFIRMED draft** | Intended profile lifecycle and burden are documented. |
| Redaction determinism standard | **CONFIRMED draft** | Intended replay burden is documented. |
| Runtime health | **UNKNOWN** | No operational package is proved. |

### Corrections from v1

| Prior implication | Current evidence | v1.1 correction |
|---|---|---|
| Package layout is merely proposed | Package, manifest, source tree, and namespace exist | Record exact confirmed inventory. |
| `pyproject.toml / package.json` is unknown | A minimal Python `pyproject.toml` exists | Confirm Python distribution intent; keep build unproved. |
| Proposed modules and imports are usable | Modules are absent | Remove speculative module/import examples. |
| Broad governed callers consume the package | No functional import surfaced | Consumer set remains UNKNOWN. |
| Custom helper outcomes are a stable package contract | No runtime outcome type exists | Require versioned mapping to accepted KFM contracts. |
| Root Hatchling config proves package build | Subpackage manifest lacks build-system/discovery | Treat build/install/import as unproved. |
| Package may contain fixtures beside code by default | No accepted test/fixture layout exists | Keep production distribution clean by default. |
| Checklist prose demonstrates readiness | Code, tests, and runtime are absent | Add staged implementation and completion gates. |
| A safe transform implies public safety | Release/evidence/policy remain external | Keep every transform result candidate-only. |

Open items must not be upgraded by README prose alone.

[Back to top](#top)

---

## Directory Rules and authority

Directory Rules place reusable implementation libraries under `packages/`. A package belongs here only when its mechanics are reusable across more than one governed caller; one-off pipeline logic belongs under `pipelines/` or `tools/`.

| Responsibility | Governing home | Package relationship |
|---|---|---|
| Package metadata and build | `packages/redaction/pyproject.toml` | Package-level responsibility; currently incomplete. |
| Source admission | `packages/redaction/src/README.md` | Defines what may enter source. |
| Python namespace and API | `packages/redaction/src/redaction/README.md` | Defines namespace-level boundary; API unratified. |
| Transform mechanics | Future source modules | Candidate implementation only. |
| Policy decisions and obligations | `policy/` and policy-runtime surfaces | Consume explicit decisions; never author policy here. |
| Profile definitions and activation | Policy/standards/governed configuration | Validate explicit identity; never activate by placement. |
| Semantic meaning | `contracts/` | Implement without redefining. |
| Machine shape | `schemas/contracts/v1/` | Validate exact accepted versions. |
| Evidence and identity | Evidence/identity/hashing authorities | Preserve refs and approved digests; do not invent. |
| Rights, consent, sensitivity | Governing registries/contracts/policy | Consume supplied posture; do not discover or downgrade. |
| Lifecycle state | `data/<phase>/` and governed workflows | Never own canonical phase transitions. |
| Receipts and proofs | `data/receipts/`, `data/proofs/` | Prepare candidates only; no persistence authority. |
| Review and release | Governance and `release/` | Never approve or publish. |
| Public surfaces | Governed applications and released artifacts | Never expose package internals as authority. |

This package must never become a parallel home for policy, profiles, contracts, schemas, source registries, evidence, lifecycle data, receipts, proofs, release manifests, public routes, UI state, credentials, or AI-generated truth.

### Directory Rules basis

- **Owning root:** `packages/`.
- **Primary responsibility:** reusable shared implementation mechanics.
- **Domain status:** cross-domain protective-transform utility, not a domain root.
- **Lifecycle status:** code only; no canonical lifecycle data.
- **ADR status:** no ADR is needed to revise the existing README in place.
- **Migration status:** no path move or new authority root is proposed here.

[Back to top](#top)

---

## Confirmed package inventory

```text
packages/redaction/
├── README.md
├── pyproject.toml
└── src/
    ├── README.md
    └── redaction/
        ├── README.md
        ├── __init__.py
        └── core.py
```

| Path | Status | Meaning |
|---|---:|---|
| `README.md` | **CONFIRMED** | Package-level governance and adoption boundary. |
| `pyproject.toml` | **CONFIRMED minimal placeholder** | Distribution name/version only. |
| `src/README.md` | **CONFIRMED v1.1** | Source-envelope admission boundary. |
| `src/redaction/README.md` | **CONFIRMED v1.1** | Namespace and future API boundary. |
| `src/redaction/__init__.py` | **CONFIRMED empty** | Package marker only; no exports. |
| `src/redaction/core.py` | **CONFIRMED comment-only** | Greenfield placeholder. |

Not established: build backend, package discovery, supported Python versions, dependencies, license, authors, optional dependencies, console scripts, entry points, type marker, functional modules, supported exports, package tests, fixtures, consumers, CI coverage, deployment, runtime health, receipt persistence, proof integration, or release use.

This is a bounded direct-read/search inventory, not proof that a later or unindexed file can never exist. Reinspect the target ref before acting.

[Back to top](#top)

---

## Package, source, and namespace layers

The three README layers must complement rather than repeat one another.

| Layer | Primary question | Owns | Must defer |
|---|---|---|---|
| Package README — this file | Why does the package exist, how is it built/adopted/versioned/rolled back? | Package role, metadata burden, dependency direction, consumer adoption, compatibility, release/correction posture. | Source-file admission and symbol-level design. |
| Source README | What code may enter `src/`? | Source placement, allowed file classes, no-hidden-fetch and side-effect rules. | Package distribution policy and namespace exports. |
| Namespace README | What may the Python namespace expose and how should behavior work? | Bounded language, candidate data/result surfaces, transform mechanics, validation, replay, API graduation. | Policy/profile authority and package release decisions. |

A change affecting package behavior should update the narrowest authoritative layer and any parent summary whose statements become false. Do not copy an implementation contract into all three files.

[Back to top](#top)

---

## Packaging, build, import, and API status

Confirmed subpackage metadata:

```toml
[project]
name = "kfm-redaction"
version = "0.0.0"
```

The manifest does **not** declare:

- a `[build-system]`;
- supported Python versions;
- `src/` package discovery;
- dependencies or optional dependencies;
- license or authors;
- scripts or entry points;
- typed-package support;
- build inclusion/exclusion rules;
- test, lint, formatting, or type-checker configuration;
- artifact publication policy.

The root `pyproject.toml` uses Hatchling for the root `kfm` project and explicitly says subpackages carry their own manifests. That root configuration does not make `kfm-redaction` buildable.

Before treating this package as installable:

1. approve the packaging and Python support posture;
2. complete the package manifest;
3. configure `src/` discovery;
4. build wheel and source artifacts;
5. inspect artifact contents for sensitive or unintended files;
6. install into a clean environment;
7. verify package metadata;
8. import `redaction`;
9. prove import has no network, profile selection, filesystem scan, secret read, logging, or write side effects;
10. verify all supported exports and version metadata;
11. uninstall cleanly and verify no unmanaged state remains.

### Public API posture

**No public Python API is established.**

An export becomes supported only when:

- a real consumer need exists;
- governing contracts/schemas/profile versions are accepted;
- its behavior is implemented and tested;
- finite outcomes and exceptions are documented;
- determinism and security properties are proved;
- compatibility and deprecation rules are approved;
- the symbol is intentionally exported;
- documentation and release notes agree;
- rollback is practical.

README examples, source paths, class names, file names, issue comments, or internal imports do not create compatibility commitments by themselves.

[Back to top](#top)

---

## Bounded context and ubiquitous language

| Term | Meaning in this package | Must not mean |
|---|---|---|
| Policy obligation | Explicit caller-supplied duty authorizing or requiring protective handling. | Locally inferred sensitivity or release permission. |
| Redaction profile | Named, versioned, reviewed transform definition supplied through governed binding. | Newest file, inline arbitrary parameters, or hidden default. |
| Profile activation | Explicit reviewed binding of profile identity/version/digest to caller/environment/policy. | File presence or environment fallback. |
| Protective transform | Deterministic operation producing a safer representation candidate. | Evidence truth, policy decision, or release approval. |
| Public-safe candidate | Output eligible for downstream validation and release review. | Published artifact or canonical record. |
| Withheld result | Explicit no-public-output result preserving safe reason and review path. | Empty success or silent drop. |
| RedactionReceipt candidate | Receipt-safe metadata prepared for an owning workflow. | Persisted receipt, proof, or approval. |
| Replay | Re-execution/comparison under pinned inputs and versions. | Retroactive authorization. |
| EvidenceRef | Reference to evidence supplied by the caller. | Evidence invented by the package. |
| Fail closed | Refuse unsafe progress when required support is absent or conflicted. | Collapse all negative states into one opaque error. |
| Safe diagnostic | Stable audience-appropriate reason/code without protected content. | Raw payload, secret, exact location, or chain-of-thought. |

```text
PolicyObligation != RedactionProfile
ProfilePresent != ProfileActive
ProtectiveTransform != PolicyDecision
PublicSafeCandidate != PublishedArtifact
RedactionReceiptCandidate != PersistedReceipt
Receipt != Proof
Proof != ReleaseApproval
SchemaValid != SemanticallyComplete
Redacted != True
Generalized != Exact
```

[Back to top](#top)

---

## Proposed package responsibility envelope

Everything in this section is **PROPOSED** until implementation and governance evidence exists.

| Candidate responsibility | Narrow role | Excluded authority |
|---|---|---|
| Explicit input values | Represent caller-supplied transform context. | No hidden lookup or authority discovery. |
| Profile reference validation | Validate supplied id/version/digest/parameters. | No profile selection or activation. |
| Field transforms | Mask, omit, replace, bucket, or suppress explicit fields. | No sensitivity classification. |
| Geometry transforms | Generalize, aggregate, clip, simplify, or withhold geometry. | No public release decision. |
| Time/detail transforms | Bucket, delay, reduce precision, or suppress detail under explicit obligation. | No historical truth rewriting. |
| Candidate validation | Check output against accepted invariants. | No contract/schema redefinition. |
| Receipt metadata candidate | Prepare non-sensitive method/input/output lineage. | No receipt persistence or approval. |
| Replay support | Compare pinned inputs, profiles, implementation, and results. | No release certification. |
| Synthetic test builders | Produce public-safe deterministic values. | No production data copies. |
| Compatibility adapters | Support reviewed migrations between package API versions. | No silent semantic conversion. |

The package should remain small. One-off orchestration, source access, domain-specific policy, registry mutation, release handling, and public response assembly belong elsewhere.

[Back to top](#top)

---

## Explicit non-responsibilities

The package must not:

- decide policy, sensitivity, rights, consent, audience, review, release, or publication;
- select a redaction profile by directory scan, newest version, environment fallback, or mutable alias;
- fetch source records, evidence, registries, lifecycle objects, or policy bundles;
- read RAW, WORK, QUARANTINE, unpublished candidates, canonical stores, or source credentials;
- mutate canonical input, lifecycle state, catalog records, triplets, evidence bundles, receipts, proofs, or release manifests;
- write public routes, UI components, map styles, tile sources, or exported artifacts;
- make direct network calls by default;
- invoke AI or use model output to infer sensitive facts;
- invent contract fields, profile identifiers, reason codes, obligations, hashing rules, or canonicalization rules;
- log raw sensitive input, exact protected locations, DNA/genomic values, personal identifiers, credentials, or reversible secrets;
- embed real sensitive records in tests, docs, examples, snapshots, or exceptions;
- treat `SAFE`, successful execution, schema validity, redaction, generalization, or receipt creation as evidence closure or release approval;
- silently continue on unsupported obligations, profiles, fields, geometry, algorithms, versions, or output shapes.

[Back to top](#top)

---

## Contract, schema, policy, profile, and standard boundaries

| Surface | Owns | Package duty |
|---|---|---|
| Semantic contract | Meaning, invariants, obligations, authority limits. | Implement accepted version without redefining it. |
| Machine schema | Accepted serialized shape and constraints. | Validate exact version where required. |
| Policy | Allow/deny/restrict/abstain/review obligations. | Consume explicit decision; never author policy. |
| Profile catalog | Named transform definitions and lifecycle state. | Validate supplied active binding; never self-select. |
| Determinism standard | Canonicalization, seed, replay, parity burden. | Implement only approved rules. |
| Package code | Reusable mechanical implementation. | Remain subordinate and candidate-producing. |
| Validator | Independent conformance check. | Expose testable values; do not self-certify. |
| Receipt/proof workflow | Persisted audit and integrity evidence. | Supply candidate metadata only. |
| Release workflow | Promotion, public exposure, correction, rollback. | Never bypass or approve. |

### Current maturity

- The shared `RedactionReceipt` contract is draft/PROPOSED.
- The paired schema is permissive and declares no properties.
- The profile catalog is a placeholder and proves no active profile.
- The profiles standard documents intended structure and lifecycle but includes proposed paths/behavior.
- The determinism standard documents intended replay burden but does not prove implementation or accepted vectors.

Implementation must not hard-code these incomplete surfaces as stable package API.

[Back to top](#top)

---

## Input and semantic-completeness boundary

Future package functions should receive explicit immutable values from a governed caller.

| Input family | Candidate content | Required posture |
|---|---|---|
| Operation context | Operation id, purpose, requested audience, caller profile. | Explicit; never infer from process or UI state. |
| Policy context | Decision ref, obligations, reason codes, review duties. | Consume without reinterpretation. |
| Profile context | Id, version, digest, strategy, parameters, activation ref. | Reject unknown, inactive, mutable, or incomplete binding. |
| Target context | Explicit record, field paths, geometry, time/detail target. | Operate only on declared target. |
| Evidence context | Evidence refs/bundle status/citation refs. | Preserve; never fabricate or resolve secretly. |
| Identity context | Object id, version, source/release refs. | Preserve stable identity and lineage. |
| Rights/sensitivity context | Classification, rights, consent, source role, disclosure limits. | Fail closed when required context is absent/stale/conflicted. |
| Canonicalization context | Approved profile/version and serialization rules. | Never invent competing rules. |
| Clock/random context | Injected clock and deterministic seed material where approved. | No ambient wall-clock or global PRNG dependency. |
| Correction context | Prior receipt/release/correction/withdrawal/rollback refs. | Preserve supersession; never overwrite history. |

### No-hidden-fetch invariant

The package must not fill missing context from:

- source systems or connectors;
- RAW/WORK/QUARANTINE;
- current catalog, release, or “latest” state;
- implicit registries or mutable filesystem paths;
- environment variables except explicitly approved non-secret configuration;
- UI/browser/request-global state;
- operator memory;
- search indexes, vector stores, graph projections, or AI prompts;
- generated language or model output.

Missing material must produce a typed negative result or bounded exception under an accepted contract.

[Back to top](#top)

---

## Transform and profile boundary

### Profile activation

Profile activation requires explicit governed binding. It must not result from:

- file or directory presence;
- lexicographic or modification-time ordering;
- symlink target;
- mutable “latest” alias;
- environment fallback;
- UI selection;
- query parameter;
- AI prompt;
- successful parse alone;
- schema validity alone.

A future binding should identify profile id/version/digest/status, manifest/catalog ref, policy obligation/family, transform implementation version, canonicalization/seed version, caller and audience, activation/review record, effective/superseded time, and failure posture.

### Transform requirements

A supported transform should:

1. accept explicit immutable input;
2. validate profile binding and semantic completeness;
3. preserve source and target identity;
4. use approved deterministic rules;
5. isolate approved stochastic behavior behind versioned seed construction;
6. preserve geometry CRS, scale, precision, and uncertainty semantics;
7. produce a typed candidate or typed negative result;
8. validate output shape and safety invariants;
9. prepare non-sensitive replay and receipt metadata;
10. have no hidden network, persistence, release, or publication effects;
11. fail closed on unsupported fields, geometry, profiles, versions, obligations, or diagnostics;
12. remain replayable under pinned dependencies.

### Transform classes are not policy

Field masking, geometry generalization, temporal bucketing, detail suppression, withholding, aggregation, and replacement are mechanical classes. Their admissibility and required parameters remain external policy/profile decisions.

[Back to top](#top)

---

## Output and RedactionReceipt candidate boundary

A future helper may return a typed **candidate result**. It must not persist authority or claim public release.

Candidate content may include:

- explicit candidate/no-output state;
- transformed value or derivative;
- profile and implementation identities;
- stable safe reason/obligation codes;
- input/output digests under approved canonicalization;
- changed-field or geometry-transform summary without protected values;
- policy/evidence/review/release refs supplied by the caller;
- replay, freshness, supersession, and correction metadata;
- validation results;
- safe diagnostics.

A candidate must not contain:

- raw protected inputs;
- reversible masking secrets or undisclosed seed material;
- credentials or private keys;
- exact protected locations when the output is generalized/withheld;
- private living-person/DNA values;
- hidden policy details unsafe for the audience;
- chain-of-thought;
- an assertion that the result is true, admissible, reviewed, released, or published.

`RedactionReceipt` persistence belongs to a separate owning workflow. A package result can prepare receipt-safe metadata; it cannot make itself an approved receipt or proof.

[Back to top](#top)

---

## Outcome vocabularies and fail-closed behavior

The current package defines no runtime outcome type.

The prior README used helper values such as:

```text
SAFE | REDACTED | GENERALIZED | WITHHELD | DENIED | HOLD | ABSTAIN | INVALID
```

These remain **documentation lineage**, not a supported package enum.

Canonical KFM runtime/policy surfaces commonly use finite primary outcomes such as:

```text
ANSWER | ABSTAIN | DENY | ERROR
```

Transform state, policy decision, review state, validation result, runtime outcome, and release state are different vocabularies.

| Layer | Candidate concepts | Status |
|---|---|---:|
| Transform effect | unchanged, redacted, generalized, withheld, suppressed | **PROPOSED** |
| Validation | pass/fail plus stable reason codes | **PROPOSED** |
| Review | hold/review-required/approved/rejected | **EXTERNAL / NEEDS VERIFICATION** |
| Runtime/policy primary outcome | ANSWER/ABSTAIN/DENY/ERROR | **DOCUMENTED elsewhere; exact binding unratified here** |
| Release state | candidate/released/withdrawn/superseded/etc. | **EXTERNAL / NEEDS VERIFICATION** |

A versioned mapping contract must define how transform effects and failures become downstream decisions. It must preserve:

- missing support versus policy denial;
- unsupported profile versus execution error;
- withheld output versus empty successful output;
- restriction/obligation details;
- review-required state;
- invalid input/output;
- stale/superseded profile or decision;
- ERROR without silent conversion to allow.

Unknown mappings must fail closed.

[Back to top](#top)

---

## Lifecycle and trust membrane

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

This package may operate on explicit values supplied by an owning workflow. It does not read or write lifecycle authority.

```text
governed caller
  -> explicit policy/profile/evidence/rights/sensitivity context
  -> redaction package candidate transform
  -> independent validation
  -> receipt/proof workflow
  -> review and release gates
  -> governed API or released artifact
```

| Unsafe collapse | Required behavior |
|---|---|
| RAW/private value -> package -> public response | Deny direct path; require owning lifecycle workflow. |
| Schema-valid input -> semantically ready | Run accepted semantic checks; do not invent context. |
| Profile file exists -> active profile | Require explicit reviewed binding. |
| Transform completes -> policy allows | Preserve external policy decision. |
| Output looks safe -> release approved | Require validation, review, receipt/proof, and release. |
| Candidate receipt metadata -> persisted receipt | Use owning receipt workflow. |
| Redacted derivative -> canonical exact truth | Preserve representation and uncertainty labels. |
| Merge -> KFM PUBLISHED | Preserve release state transition. |
| UI style hides field -> redacted | Transform or withhold upstream before delivery. |

When required evidence, rights, consent, sensitivity, review, or release context is missing or stale, the package must not manufacture support.

[Back to top](#top)

---

## Dependency direction

The package should depend **inward on small stable interfaces** and receive effectful capabilities through explicit injection.

### Allowed candidate dependency direction

```text
accepted contracts / schemas / profiles / primitives
                         |
                         v
                 packages/redaction
                         |
                         v
         candidate values + safe metadata
                         |
                         v
       governed callers and owning workflows
```

### Preferred dependencies

- standard library where sufficient;
- approved geometry primitives;
- approved hashing/canonicalization interfaces;
- exact contract/schema/profile versions;
- small injected clock/random/evaluator protocols;
- stable value/result types.

### Prohibited coupling

- applications, UI frameworks, route handlers, or browser state;
- source-specific connectors;
- lifecycle storage implementations;
- policy bundle discovery or mutable registry access;
- receipt/proof databases;
- release tooling;
- direct model runtimes;
- network clients in core paths;
- process-global mutable state;
- import-time configuration discovery;
- circular package dependencies;
- domain-specific policy logic that belongs in domain/policy lanes.

Every dependency must have provenance, license, security, maintenance, determinism, and rollback review appropriate to its role.

[Back to top](#top)

---

## Inputs, outputs, and side effects

### Pure core default

Core transforms should be pure or observationally equivalent given identical explicit:

- input value;
- policy obligation;
- profile identity/version/digest;
- parameters and seed material;
- canonicalization version;
- geometry/CRS/precision context;
- implementation/dependency versions;
- clock input where needed.

### Prohibited hidden side effects

Core package code must not:

- open network sockets;
- fetch or refresh profiles;
- scan directories for active state;
- read secrets or credentials;
- read current release/catalog/lifecycle state;
- write files, databases, caches, receipts, proofs, catalogs, releases, or telemetry containing sensitive values;
- mutate caller inputs;
- invoke AI;
- sleep/retry internally without explicit reviewed policy;
- emit public responses.

Effectful integration, if ever needed, belongs behind a narrow injected protocol and should remain outside the deterministic core.

[Back to top](#top)

---

## Determinism, canonicalization, identity, replay, and freshness

A transform is not supported until its reproducibility burden is explicit.

### Determinism dimensions

- input normalization and field ordering;
- Unicode handling;
- numeric precision and rounding;
- null/missing semantics;
- geometry CRS, axis order, validity, precision, and serialization;
- stable collection ordering;
- seed construction and PRNG algorithm;
- time/locale/environment handling;
- dependency and implementation versions;
- error/timeout behavior;
- output serialization and hashing.

### Identity separation

Keep separate identities for:

- source/canonical object;
- transform request;
- profile and activation binding;
- implementation and dependency set;
- transform execution;
- public-safe derivative candidate;
- RedactionReceipt;
- proof/validation record;
- release;
- correction/withdrawal/supersession.

Do not embed credentials, protected values, exact locations, raw prompts, or mutable “latest” state in identifiers.

### Replay

Replay should distinguish:

- exact byte match;
- semantic match under approved equivalence;
- approved migration difference;
- profile or implementation drift;
- input or parameter drift;
- output drift;
- missing support;
- stale/superseded context;
- execution error;
- comparison error.

A stale result must be re-evaluated under current approved context. Never “refresh” it by rewriting timestamps or mutating historical receipts.

[Back to top](#top)

---

## Security, privacy, and threat model

### Protected categories

Apply strict handling to:

- living-person and household information;
- genealogy and DNA/genomic data;
- rare species and rare plant locations;
- archaeology and cultural/sacred places;
- critical or sensitive infrastructure;
- private land and sensitive joins;
- credentials, secrets, private source payloads;
- reversal-enabling transform details;
- unresolved rights/consent/source terms.

### Threats

| Threat | Failure mode | Required control |
|---|---|---|
| Hidden context fill | Missing authority silently inferred. | Explicit inputs; semantic completeness checks. |
| Arbitrary profile path | Caller selects unreviewed file. | Governed id/version/digest binding. |
| Mutable “latest” | Behavior changes without version. | Immutable profile and implementation refs. |
| Fail-open error | Exception becomes unchanged/public output. | Typed failure; no unsafe fallback. |
| Partial transform | Some sensitive fields remain. | Atomic validation or explicit failure. |
| Obligation drop | Restriction disappears downstream. | Preserve/validate obligations and reason codes. |
| Sensitive logs | Raw protected material enters telemetry. | Structured allowlist logging and tests. |
| Reversal leakage | Seed/parameters enable reconstruction. | Separate internal/public metadata; secrecy review. |
| Geometry false safety | CRS/precision error exposes location. | Geometry-specific vectors and independent validation. |
| Stale profile/consent | Old approval reused after change/revocation. | Freshness and supersession checks. |
| Dependency compromise | Parser/geometry/hash behavior changes. | Pinning, provenance, review, SBOM/vulnerability response. |
| Resource exhaustion | Crafted values consume excessive CPU/memory. | Size, depth, complexity, coordinate, and timeout limits. |
| Public API bypass | Internals exposed directly. | Governed interfaces only. |

Unknown, stale, conflicted, or unsupported security context must fail closed.

[Back to top](#top)

---

## Dependencies, supply chain, and resource bounds

Before adding a dependency, document:

- exact purpose and why standard library/current packages are insufficient;
- authoritative source and maintainer status;
- license compatibility;
- supported versions and pinning strategy;
- transitive dependency closure;
- build/install provenance;
- vulnerability and security posture;
- deterministic/replay implications;
- network/native-extension behavior;
- platform support;
- update cadence and owner;
- fallback/removal/rollback plan.

Resource controls should cover:

- maximum record and field count;
- string/binary size;
- nesting depth;
- geometry coordinate/ring/feature complexity;
- collection size;
- numeric ranges and precision;
- transform time and memory;
- diagnostic size;
- batch limits;
- hostile or malformed serialization.

Resource failure must not return unchanged sensitive input as a fallback.

[Back to top](#top)

---

## Logging, telemetry, and error hygiene

Logs and metrics are operational signals—not evidence, policy decisions, receipts, proofs, or release approval.

### Permitted candidate telemetry

- package and implementation version;
- profile id/version/digest where safe;
- transform class;
- finite status and stable reason code;
- duration and bounded resource counters;
- validation summary;
- opaque correlation and caller-supplied refs;
- drift/freshness state;
- error category without protected payload.

### Prohibited telemetry

- raw input/output;
- personal identifiers or DNA/genomic values;
- exact protected coordinates;
- secrets, tokens, credentials, or private keys;
- reversible seed material;
- unrestricted policy details;
- raw evidence contents;
- prompts or chain-of-thought;
- exception representations that include protected values.

Public explanations and internal diagnostics may require different reviewed views. Unknown exceptions should be sanitized at the boundary.

[Back to top](#top)

---

## Consumer adoption, versioning, and compatibility boundary

No functional consumer import was established by bounded search.

The first consumer should:

1. demonstrate a shared need that belongs in a package;
2. use the smallest reviewed symbol set;
3. supply explicit policy/profile/evidence/rights/sensitivity context;
4. preserve existing behavior behind a feature/configuration gate where practical;
5. enforce downstream validation and obligations;
6. use synthetic/public-safe integration fixtures;
7. include rollback and correction handling;
8. remain behind a governed API or owning workflow;
9. avoid exposing package internals as public authority;
10. record package/profile/implementation versions in appropriate audit metadata.

### Compatibility policy

Until a supported API is approved, **no compatibility promise exists**.

After approval:

- use intentional exports;
- version semantic changes;
- distinguish internal modules from public API;
- provide migration notes and deprecation windows;
- test old/new consumer behavior;
- preserve negative-state semantics;
- never silently weaken redaction or fail-closed posture;
- require review for profile/canonicalization/geometry/seed changes;
- coordinate code, contracts, schemas, profiles, validators, docs, and release notes;
- retain rollback targets.

A source file path is not automatically a stable import path.

[Back to top](#top)

---

## Testing, fixtures, and CI

Current status: no functional package implementation, supported exports, package-local tests, or accepted CI enforcement is established.

### Minimum test matrix

| Family | Minimum proof |
|---|---|
| Build/artifact | Wheel/sdist build, content inspection, metadata, clean install/uninstall. |
| Import safety | No network, profile selection, secret read, filesystem scan, write, or logging side effect. |
| Contract/schema | Exact accepted versions; shape and semantic completeness remain separate. |
| Profile binding | Id/version/digest/status/activation checked; file presence cannot activate. |
| Field transforms | Allowlisted fields, missing paths, aliases, nested values, nulls, unknown fields. |
| Geometry | CRS, axis order, validity, precision, rounding, boundaries, multipart/empty geometry. |
| Temporal/detail | Bucketing, truncation, delay/embargo, boundary and timezone cases. |
| Negative states | Missing policy/profile/evidence/rights/sensitivity; unsupported obligations; invalid output. |
| Outcome mapping | Every transform effect/failure maps explicitly; no silent allow. |
| Receipt candidates | Required safe metadata; no protected/reversal leakage; no persistence side effect. |
| Determinism | Same inputs/versions produce equivalent results across runs/platforms where required. |
| Replay/drift | Input/profile/parameter/implementation/output/stale/supersession distinctions. |
| Security | Traversal, injection, oversized/deep input, parser abuse, log leakage, hostile geometry. |
| Privacy | Living-person, DNA, protected-location, cultural and infrastructure denial/generalization cases. |
| Property/fuzz | Invariants hold over generated valid/invalid values. |
| Consumer integration | Governed caller, obligations enforced, bypass denied, rollback proven. |
| Compatibility | Export/version/deprecation/migration behavior. |

Fixtures must be:

- synthetic and public-safe;
- deterministic and minimized;
- versioned;
- paired across valid/invalid/denied/abstained/error/edge cases;
- explicit about shape proof versus behavior proof;
- reviewed for reversal and disclosure risk;
- stored in the repository-confirmed fixture/test homes, not assumed here.

A meaningful CI lane should run build/import, unit, negative, property/fuzz, security, privacy, no-network, replay, fixture/schema, artifact inspection, dependency, consumer integration, docs/link, and rollback checks. A green generic workflow does not prove redaction behavior unless those tests run.

[Back to top](#top)

---

## Smallest sound implementation sequence

### Gate 0 — ownership and architecture

- [ ] Assign package and security/privacy owners.
- [ ] Confirm first governed consumer and shared need.
- [ ] Approve package build/Python/versioning posture.
- [ ] Accept contract/schema/profile/activation boundaries.
- [ ] Decide finite transform-state and downstream outcome mapping.
- [ ] Define canonicalization, geometry, seed, reason/obligation governance.
- [ ] Define correction, deprecation, revocation, and rollback.

### Gate 1 — installable inert package

- [ ] Complete package metadata and `src/` discovery.
- [ ] Build and inspect artifacts.
- [ ] Add clean install/import/uninstall tests.
- [ ] Prove import has no effects.
- [ ] Keep exports empty or intentionally minimal.

### Gate 2 — explicit value/result surface

- [ ] Implement one consumer-needed typed request/result boundary.
- [ ] Bind accepted contract/schema/profile versions.
- [ ] Separate shape validation from semantic completeness.
- [ ] Preserve missing/unknown/conflicted context.
- [ ] Add safe diagnostics.

### Gate 3 — one deterministic non-geometry transform

- [ ] Implement the smallest policy-supplied field transform.
- [ ] Add valid/invalid/negative/property/security tests.
- [ ] Produce candidate metadata without persistence.
- [ ] Prove no hidden fetch, network, or writes.

### Gate 4 — profile binding and replay

- [ ] Validate explicit profile id/version/digest/activation.
- [ ] Implement approved canonicalization and hashing.
- [ ] Add replay and drift outcomes.
- [ ] Prove file presence cannot activate behavior.

### Gate 5 — geometry only after dedicated review

- [ ] Accept CRS/precision/generalization contract.
- [ ] Implement one bounded geometry transform.
- [ ] Add boundary, parity, leakage, and hostile-complexity tests.
- [ ] Review reversal and false-precision risk.

### Gate 6 — RedactionReceipt candidate

- [ ] Assemble accepted safe metadata shape.
- [ ] Validate no protected/reversible content.
- [ ] Prove no persistence or approval.
- [ ] Integrate with owning receipt workflow separately.

### Gate 7 — first governed consumer

- [ ] Integrate one caller behind governed interfaces.
- [ ] Preserve prior behavior/rollback path.
- [ ] Enforce obligations and downstream gates.
- [ ] Capture runtime evidence without sensitive telemetry.

### Gate 8 — CI and operations

- [ ] Establish meaningful required checks.
- [ ] Verify dependency/supply-chain monitoring.
- [ ] Add correction, revocation, compatibility, and rollback drills.
- [ ] Verify operational health and incident response.

Do not begin with a broad transform framework, direct UI integration, production sensitive data, profile autodiscovery, or public API exposure.

[Back to top](#top)

---

## Definition of done

The package is not operationally complete until all applicable items are satisfied:

- [ ] Package reusability and ownership are demonstrated.
- [ ] Build backend, Python support, discovery, dependencies, license, authors, and artifacts are approved.
- [ ] Clean build/install/import/uninstall and import-safety tests pass.
- [ ] API exports are intentional, minimal, documented, versioned, and tested.
- [ ] Contracts, schemas, profiles, activation, canonicalization, and outcome mappings are accepted and versioned.
- [ ] Determinism, geometry, seed, identity, hashing, replay, and freshness rules are executable and independently validated.
- [ ] Package never decides policy, evidence, rights, consent, sensitivity, review, release, or publication.
- [ ] Receipt metadata remains candidate-only; owning persistence/proof workflow is separate.
- [ ] Sensitive data is absent from logs, errors, fixtures, artifacts, and public diagnostics.
- [ ] Unit, negative, property/fuzz, security, privacy, no-network, replay, artifact, and integration tests exist.
- [ ] First governed consumer, obligation enforcement, correction, and rollback are proved.
- [ ] CI executes meaningful package checks; settings and ownership are verified.
- [ ] Package/source/namespace docs agree with code and metadata.
- [ ] Compatibility, deprecation, revocation, correction, and rollback paths are current.
- [ ] Runtime health and incident response are established where deployed.
- [ ] Human policy/sensitivity/security review is complete for significant behavior.
- [ ] Merge and package release remain separate from KFM data publication.

[Back to top](#top)

---

## Verification register

| ID | Verification item | Status | Evidence required |
|---|---|---:|---|
| RPK-001 | Assign package owner and review roles | **NEEDS VERIFICATION** | Maintainer/CODEOWNERS decision. |
| RPK-002 | Confirm CODEOWNERS, branch/ruleset, and required-check coverage | **UNKNOWN** | Repository settings and workflow evidence. |
| RPK-003 | Confirm first governed consumer and shared need | **UNKNOWN** | Consumer design/integration evidence. |
| RPK-004 | Approve build backend | **UNKNOWN** | Completed manifest and review. |
| RPK-005 | Approve supported Python versions/platforms | **UNKNOWN** | Metadata and CI matrix. |
| RPK-006 | Configure and prove `src/` package discovery | **UNKNOWN** | Artifact and clean install/import. |
| RPK-007 | Approve license, authors, dependencies, and publication posture | **UNKNOWN** | Metadata/legal/release review. |
| RPK-008 | Approve public API and export policy | **UNKNOWN** | Source/docs/tests/review. |
| RPK-009 | Confirm package test and fixture homes | **UNKNOWN** | Directory Rules/repo convention decision. |
| RPK-010 | Accept RedactionReceipt contract version | **NEEDS VERIFICATION** | Contract review. |
| RPK-011 | Strengthen/accept RedactionReceipt schema | **NEEDS VERIFICATION** | Schema, fixtures, migration. |
| RPK-012 | Accept redaction profile shape and lifecycle | **NEEDS VERIFICATION** | Standard/catalog/schema/policy review. |
| RPK-013 | Define profile activation/binding contract | **UNKNOWN** | Governed immutable binding and tests. |
| RPK-014 | Define transform request/result types | **UNKNOWN** | Contract/schema/API review. |
| RPK-015 | Define transform effects and downstream outcome mapping | **CONFLICTED** | Versioned mapping and exhaustive tests. |
| RPK-016 | Accept canonicalization and hashing rules | **UNKNOWN** | Repository-standard spec and vectors. |
| RPK-017 | Accept geometry CRS/precision/generalization rules | **UNKNOWN** | Geometry contract, vectors, review. |
| RPK-018 | Decide stochastic transform and seed secrecy posture | **UNKNOWN** | Threat model, standard, vectors. |
| RPK-019 | Define reason-code and obligation registries | **UNKNOWN** | Reviewed registries and interpreters. |
| RPK-020 | Implement first non-geometry transform | **UNKNOWN** | Source and tests. |
| RPK-021 | Establish no-hidden-fetch/network/import-side-effect enforcement | **UNKNOWN** | Tests and CI. |
| RPK-022 | Implement output/candidate validation | **UNKNOWN** | Source, independent validator, tests. |
| RPK-023 | Integrate RedactionReceipt candidate with owning workflow | **UNKNOWN** | Workflow/receipt evidence. |
| RPK-024 | Confirm proof and release integration remain external | **UNKNOWN** | Integration and bypass tests. |
| RPK-025 | Establish replay/freshness/supersession behavior | **UNKNOWN** | Contract/source/tests. |
| RPK-026 | Complete privacy/security/cultural/sensitivity review | **UNKNOWN** | Threat model and approvals. |
| RPK-027 | Establish dependency/supply-chain controls | **UNKNOWN** | Pins, SBOM/provenance, scanning, response. |
| RPK-028 | Establish resource limits and hostile-input tests | **UNKNOWN** | Limits, fuzz/security evidence. |
| RPK-029 | Establish safe telemetry and incident handling | **UNKNOWN** | Logging contract, tests, runbook. |
| RPK-030 | Prove lifecycle/public-interface gates | **UNKNOWN** | Integration and bypass-denial tests. |
| RPK-031 | Establish meaningful package CI enforcement | **UNKNOWN** | Workflow logs/settings. |
| RPK-032 | Approve versioning, compatibility, and deprecation policy | **UNKNOWN** | Policy/docs/tests. |
| RPK-033 | Establish correction, profile revocation, and withdrawal handling | **UNKNOWN** | Runbook/integration evidence. |
| RPK-034 | Drill software and downstream artifact rollback | **UNKNOWN** | Drill receipts/results. |
| RPK-035 | Reconcile all three redaction README layers after implementation | **NEEDS VERIFICATION** | Docs/code review. |
| RPK-036 | Confirm deployment, operational health, and release use | **UNKNOWN** | Config/logs/telemetry/release evidence. |

Verification items must not be upgraded by documentation edits alone.

[Back to top](#top)

---

## Drift and conflicts

| Topic | Observed state | Risk | Required handling |
|---|---|---|---|
| Package maturity | Broad v1 README; placeholder code | False implementation/API assumptions | Record exact inventory and remove speculative imports. |
| Build status | Root Hatchling exists; subpackage manifest incomplete | Source-tree import masks packaging failure | Require clean artifact/install/import. |
| Package/source/namespace docs | Child docs v1.1; package doc v1 | Layer contradiction | Align parent summary and preserve layer ownership. |
| Public API | Proposed modules/imports; no exports | Premature compatibility commitment | No API until implementation/review/tests. |
| Helper outcomes | Custom values in prior docs; no type exists | Vocabulary drift and unsafe mapping | Ratify separate transform/runtime/release mappings. |
| Profile catalog | Placeholder file | File presence mistaken for activation | Require explicit immutable binding. |
| Receipt | Rich prose; empty permissive schema | Candidate metadata mistaken for enforced receipt | Strengthen contract/schema before integration. |
| Determinism | Draft standards; no code/vectors | Reproducibility overclaim | Require executable replay/parity tests. |
| Consumers | Broad intended callers; no import surfaced | Premature framework | Start with one governed consumer. |
| Sensitive fixtures | Prior docs contemplated package fixtures | Disclosure or distribution leakage | Use repository fixture home; synthetic public-safe values only. |
| Safe output | Redacted/generalized candidate | Candidate mistaken for release | Preserve downstream evidence/policy/review/release gates. |
| CI | Generic repository checks may be green | Green check overread | Require package-specific meaningful execution. |

When code, metadata, contract, schema, policy, profile, tests, validators, receipts, runtime, or docs disagree:

1. stop adoption or release of the affected behavior;
2. identify exact versions and authority owners;
3. preserve the conflict and affected outputs;
4. resolve through appropriate review/ADR/migration/correction;
5. update code, tests, validators, docs, and release notes together;
6. define rollback and downstream correction;
7. do not silently make package behavior canonical.

[Back to top](#top)

---

## Maintenance and change review

### Before change

- [ ] Pin base commit and target blobs.
- [ ] Inspect package, source, namespace, manifest, implementation, tests, consumers, contracts, schemas, policy, profiles, and standards.
- [ ] Search for duplicate APIs and active PRs.
- [ ] Check Directory Rules, ADRs, drift, and verification backlog.
- [ ] Identify rights, sensitivity, security, compatibility, and release impact.
- [ ] Define validation, migration, correction, and rollback.

### During change

- [ ] Keep the smallest reusable mechanic.
- [ ] Use explicit immutable inputs.
- [ ] Preserve vocabulary and authority layers.
- [ ] Avoid hidden fetches, selection, effects, and sensitive diagnostics.
- [ ] Add behavior and negative tests with the implementation.
- [ ] Keep profile/policy rules outside package code.
- [ ] Keep exports intentional and minimal.
- [ ] Update the narrowest authoritative README layer.
- [ ] Preserve unknowns/conflicts rather than guessing.

### Before review

- [ ] Build and inspect artifacts.
- [ ] Install/import/uninstall in clean environments.
- [ ] Run unit, negative, property/fuzz, security, privacy, no-network, replay, schema/fixture, artifact, and integration checks.
- [ ] Scan artifacts/logs/errors/fixtures for sensitive data and secrets.
- [ ] Verify dependency provenance/licenses/vulnerabilities.
- [ ] Read back remote blobs and verify changed paths.
- [ ] Add/update generated-work receipt when required.

### Before merge or package release

- [ ] Confirm owners, reviewers, separation of duties, and meaningful required checks.
- [ ] Resolve or explicitly carry blockers.
- [ ] Confirm versioning, compatibility, migration, deprecation, correction, revocation, and rollback.
- [ ] Confirm consumer and runtime evidence.
- [ ] Do not treat package release, Git merge, or generated receipt as KFM data publication.

[Back to top](#top)

---

## Versioning, deprecation, correction, and revocation

### Package/API versioning

Version changes should reflect externally observable behavior, including:

- accepted input/output types;
- export names and import paths;
- transform semantics;
- profile binding;
- canonicalization/hashing/seed behavior;
- geometry precision/generalization;
- negative-state and exception behavior;
- receipt-candidate metadata;
- side effects or dependency changes;
- security/privacy posture.

### Profile/implementation version separation

Package version, transform implementation version, profile version, canonicalization version, schema version, contract version, and release version are separate identities. Do not collapse them.

### Deprecation

A supported behavior may be deprecated only with:

- reason and replacement;
- affected consumers;
- compatibility/migration plan;
- review and time window;
- security/sensitivity impact;
- tests for old/new behavior;
- rollback target;
- documentation and release notes.

Unsafe behavior may require immediate disablement; record the emergency path and correction duties.

### Correction and revocation

Profile revocation, consent/rights change, sensitivity upgrade, algorithm defect, dependency vulnerability, replay drift, or disclosure incident may invalidate prior derivatives. The owning workflows must identify affected candidates, receipts, proofs, releases, exports, and public artifacts and perform correction, withdrawal, supersession, or rebuild as required.

Rolling back code alone does not retract previously emitted artifacts.

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | Supports | Does not support |
|---|---:|---|---|
| Prior package README | **CONFIRMED v1** | Documentation lineage and prior intent. | Functional implementation. |
| Package path and minimal `pyproject.toml` | **CONFIRMED placeholder** | Distribution name/version and package placement. | Build/install/import. |
| Source README v1.1 | **CONFIRMED** | Source-admission boundary. | Package API or behavior. |
| Namespace README v1.1 | **CONFIRMED** | Namespace design and implementation burden. | Functional exports or runtime. |
| Empty `__init__.py` / comment-only `core.py` | **CONFIRMED** | Greenfield state. | Any transform behavior. |
| Root Python project | **CONFIRMED** | Root Hatchling/Python posture. | Redaction subpackage support. |
| Directory Rules | **CONFIRMED doctrine** | Reusable package placement and authority separation. | Package maturity. |
| Shared RedactionReceipt contract | **CONFIRMED draft / PROPOSED** | Intended cross-domain meaning. | Accepted machine shape or persistence. |
| Redaction receipt schema | **CONFIRMED permissive PROPOSED scaffold** | Schema path exists. | Field-level validation/readiness. |
| Redaction profile registry | **CONFIRMED placeholder / PROPOSED** | Intended catalog path. | Active profiles or activation. |
| Redaction profiles standard | **CONFIRMED draft** | Intended profile lifecycle/burden. | Implemented catalog or algorithms. |
| Redaction determinism standard | **CONFIRMED draft** | Intended replay burden. | Accepted algorithm or vectors. |
| Bounded consumer/test search | **CONFIRMED search performed** | No adoption surfaced in inspected index. | Permanent/global absence. |
| This v1.1 revision | **PROPOSED until merged** | Package-level documentation alignment. | Code, policy, receipt, proof, release, or publication change. |

[Back to top](#top)

---

## Related documentation

- [Shared packages responsibility root](../README.md)
- [Redaction package metadata](pyproject.toml)
- [Redaction source-envelope boundary](src/README.md)
- [`redaction` namespace boundary](src/redaction/README.md)
- [Root Python project](../../pyproject.toml)
- [Directory Rules](../../docs/doctrine/directory-rules.md)
- [Trust membrane doctrine](../../docs/doctrine/trust-membrane.md)
- [Lifecycle law](../../docs/doctrine/lifecycle-law.md)
- [Sensitive-domain fail-closed architecture](../../docs/architecture/sensitive-domain-fail-closed.md)
- [Redaction profiles standard](../../docs/standards/REDACTION_PROFILES.md)
- [Redaction determinism standard](../../docs/standards/REDACTION_DETERMINISM.md)
- [Sensitivity rubric](../../docs/standards/SENSITIVITY_RUBRIC.md)
- [Data classification](../../docs/security/DATA_CLASSIFICATION.md)
- [Shared `RedactionReceipt` contract](../../contracts/shared/redaction_receipt.md)
- [Redaction receipt schema scaffold](../../schemas/contracts/v1/receipts/redaction_receipt.schema.json)
- [Redaction profile registry placeholder](../../policy/redaction/profiles.yaml)
- [Repository drift register](../../docs/registers/DRIFT_REGISTER.md)
- [Generated-work receipt lane](../../data/receipts/generated/README.md)
- [Generated-work receipt schema](../../schemas/contracts/v1/receipts/generated_receipt.schema.json)

[Back to top](#top)

---

## Rollback

### Documentation rollback

Revert the documentation commit or close its unmerged pull request. Preserve history; do not reset or force-rewrite shared history. Re-run documentation, link, receipt, and scope checks.

Documentation rollback does not alter code, policy, profiles, lifecycle data, receipts, proofs, releases, or public artifacts because this revision changes none of those surfaces.

### Future software rollback expectations

A package behavior rollback must identify:

- prior package/API/implementation versions;
- affected consumers and deployments;
- profile/activation/contract/schema/canonicalization/dependency versions;
- affected candidate derivatives, receipts, proofs, releases, exports, and public artifacts;
- safe disable and restoration order;
- data/public correction, withdrawal, and notification duties;
- post-rollback validation and replay;
- supersession and deprecation handling.

If behavior causes authority drift, sensitive disclosure, nondeterminism, invalid receipt metadata, fail-open output, or unsafe public exposure:

1. disable or revert the affected behavior through a reviewed change;
2. preserve evidence and audit history;
3. quarantine affected candidates;
4. identify downstream artifacts and releases;
5. issue correction/withdrawal/supersession as required;
6. restore a reviewed safe version;
7. run replay and regression validation;
8. update the relevant drift/verification/incident records.

Rolling back package code does not automatically roll back policy decisions, receipts, proofs, releases, exports, caches, or public artifacts.

[Back to top](#top)
