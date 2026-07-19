<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION/packages-release-readme
title: packages/release/ — Package Boundary and Greenfield Governed Release-Support Scaffold
type: readme
version: v1.1
prior_version: v1
status: draft
owners: OWNER_TBD — Release steward · Promotion steward · Rollback/correction steward · Contracts steward · Schema steward · Policy steward · Evidence steward · Security/signing steward · Validation steward · Package steward · Runtime/API steward · CI steward · Docs steward
created: NEEDS VERIFICATION — target file existed before this evidence-grounded revision
updated: 2026-07-19
policy_label: "public-doctrine; package-boundary; python-package-scaffold; greenfield-placeholder; build-unconfigured; no-supported-api; explicit-inputs; no-hidden-fetches; no-network-by-default; deterministic-candidate-mechanics; fail-closed; release-authority-external; signing-key-external; receipt-proof-external; no-publication-authority; compatibility-unratified; correction-aware; rollback-aware"
current_path: packages/release/README.md
truth_posture: >
  CONFIRMED target README v1, repository-present packages/release package, kfm-release
  distribution metadata version 0.0.0, merged source-envelope README v1.1, merged
  release namespace README v1.1, empty release/__init__.py, comment-only release/core.py
  greenfield placeholder, root Hatchling project that delegates subpackages to their own
  manifests, packages responsibility-root doctrine, authoritative release-governance root,
  draft ReleaseManifest, PromotionDecision, RollbackCard, and CorrectionNotice contracts,
  uneven PROPOSED schema/validator/test maturity, draft signing standard, proposed
  promotion-gate ADR, and explicit release-dry-run holds / PROPOSED a small reusable
  Python package for explicit deterministic release-candidate normalization, injected
  validation, public verification-result handling, replay-safe comparison, and sanitized
  test support / CONFLICTED prior README implications that proposed package layout,
  modules, imports, broad consumers, and custom helper outcomes were usable implementation;
  competing draft A–G gate vocabularies; CorrectionNotice release-vs-correction family
  placement / UNKNOWN accepted import name, public API, build backend, Python support,
  package discovery, dependencies, source-module decomposition, signer integration, first
  consumer, package-local test home, CI enforcement, deployment, operational health, and
  release use / NEEDS VERIFICATION owners, package metadata completion, API approval,
  contract/schema/policy acceptance, validators, fixtures, security review, compatibility
  policy, correction process, and rollback drills
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 2783739bba744f560772388a9969ed3107d08930
  prior_blob: e0f2aad3f3b1e70b15bd1f1b410c60852c9d41dd
  source_readme_blob: 8318fc5aeee6856391487a80c1e623a62e6fd510
  namespace_readme_blob: 1fc83f7549c1258da3f121ba3b364db9877ca333
  package_metadata_blob: b50731922626e9eb12b69f62dd8e71b11f00068b
  root_pyproject_blob: e3bd40e8e6ce14dfcde78ff5c09608095c3eca76
  namespace_init_blob: e69de29bb2d1d6434b8b29ae775ad8c2e48c5391
  namespace_core_blob: 1c98feb4fb83b956decc0f55171a732d4a3233c0
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  release_root_blob: 089c4a394c5cbf3b9e5a2a1963e68e16be485dce
  release_manifest_contract_blob: 9ca1c9d4a5b247196aa84a31a158fe734c8a6720
  release_manifest_schema_blob: 727db0a781900aa3816dcdce723fe355fec2e786
  promotion_decision_contract_blob: 42295bfc83a621cf125d33aa821912b426f70bd2
  promotion_decision_schema_blob: a2d087a46772cf60e4b9dfb394892690e8a88b31
  promotion_decision_validator_blob: ead33d6c5c073f319627ee42d99c5933c0e370d1
  promotion_decision_test_blob: 495c76aa9d3a016b7a60831e47c15d3a21efaa0c
  rollback_card_contract_blob: 72ab9e148491243cc8a374556350ab94c2557ab4
  rollback_card_schema_blob: 779ffcf282201ba4dba9689e622f92723db55b4e
  rollback_validator_placeholder_blob: b80dd40e93733c7fa76f8f9a78e9ec55b6090b4b
  correction_notice_contract_blob: 4716f2bc6e714ad2ab873d95144417d7855f5beb
  correction_notice_schema_blob: 8f260eb5a5adba0b4966adfeffebfbcf6960277d
  promotion_gate_adr_blob: d7604ab92b915abaec8d7d9bac3da5d40d51e7f3
  signing_standard_blob: b719251e5f7d0abb954da4f043f8ea5d95e6283f
  release_dry_run_workflow_blob: c91e794ae68a99edf6b618e9e3992c30ab0e4fe5
  bounded_path_checks:
    - packages/release/README.md existed at version v1 before this revision
    - packages/release/pyproject.toml declares only project name kfm-release and version 0.0.0
    - package metadata declares no build system, Python requirement, package discovery, dependencies, scripts, entry points, license, authors, or test configuration
    - packages/release/src/README.md exists at version v1.1 on main
    - packages/release/src/release/README.md exists at version v1.1 on main
    - packages/release/src/release/__init__.py is empty
    - packages/release/src/release/core.py is a comment-only greenfield placeholder
    - bounded repository search surfaced no functional release namespace consumer import or package-local test reference
    - PromotionDecision has a concrete PROPOSED schema, validator, and repository fixture test
    - ReleaseManifest, RollbackCard, and CorrectionNotice enforcement remains thin, incomplete, or conflicted
    - release-dry-run workflow explicitly emits holds and no release or publication artifact
related:
  - ../README.md
  - pyproject.toml
  - src/README.md
  - src/release/README.md
  - src/release/__init__.py
  - src/release/core.py
  - ../../pyproject.toml
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/doctrine/trust-membrane.md
  - ../../docs/doctrine/lifecycle-law.md
  - ../../docs/architecture/release-discipline.md
  - ../../docs/architecture/publication/RELEASE_GATES.md
  - ../../docs/adr/ADR-0018-promotion-gate-sequence.md
  - ../../docs/standards/SIGNING.md
  - ../../contracts/release/release_manifest.md
  - ../../contracts/release/promotion_decision.md
  - ../../contracts/release/rollback_card.md
  - ../../contracts/correction/correction_notice.md
  - ../../schemas/contracts/v1/release/release_manifest.schema.json
  - ../../schemas/contracts/v1/release/promotion_decision.schema.json
  - ../../schemas/contracts/v1/release/rollback_card.schema.json
  - ../../schemas/contracts/v1/correction/correction_notice.schema.json
  - ../../tools/validators/release/validate_promotion_decision.py
  - ../../tools/validators/validate_rollback_card.py
  - ../../tests/release/test_promotion_decision_schema.py
  - ../../release/README.md
  - ../../.github/workflows/release-dry-run.yml
  - ../../data/receipts/generated/README.md
  - ../../schemas/contracts/v1/receipts/generated_receipt.schema.json
tags: [kfm, packages, release, python, package, scaffold, release-candidate, promotion-decision, release-manifest, rollback-card, correction-notice, signing, fail-closed, compatibility, correction, rollback]
notes:
  - "v1.1 aligns the package entrypoint with the merged source-envelope and namespace v1.1 boundaries."
  - "This README owns package identity, packaging, adoption, compatibility, and package-level governance; source-file admission belongs to src/README.md and namespace/API detail belongs to src/release/README.md."
  - "This README does not install the package, establish a supported API, accept a release-gate vocabulary, implement release mechanics, hold signing keys, write trust artifacts, mutate release state, authorize publication, or prove operational safety."
  - "The package remains a greenfield placeholder at the recorded evidence snapshot."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Release Package Boundary and Greenfield Governed Release-Support Scaffold

`packages/release/`

> Package-level governance, packaging, adoption, compatibility, and rollback boundary for a future reusable Python release-support library. Current evidence establishes a `0.0.0` metadata stub, two evidence-grounded child READMEs, an empty package initializer, and a comment-only `core.py` placeholder—not an installable distribution, supported API, release runner, signer, rollback executor, correction publisher, receipt writer, release ledger, deployment, or publication authority.

![status](https://img.shields.io/badge/status-draft-yellow)
![version](https://img.shields.io/badge/version-v1.1-informational)
![maturity](https://img.shields.io/badge/maturity-greenfield__placeholder-lightgrey)
![distribution](https://img.shields.io/badge/distribution-kfm--release-blue)
![package-version](https://img.shields.io/badge/package__version-0.0.0-lightgrey)
![build](https://img.shields.io/badge/build-unconfigured-orange)
![exports](https://img.shields.io/badge/exports-none-orange)
![tests](https://img.shields.io/badge/package__tests-not__established-orange)
![authority](https://img.shields.io/badge/publication__authority-none-red)

**Quick links:** [Purpose](#purpose) · [Impact](#impact-and-operating-posture) · [Evidence](#status-and-evidence) · [Placement](#directory-rules-and-authority) · [Inventory](#confirmed-package-inventory) · [Layers](#package-source-and-namespace-layers) · [Packaging](#packaging-build-import-and-api-status) · [Vocabulary](#bounded-context-and-ubiquitous-language) · [Responsibilities](#proposed-package-responsibility-envelope) · [Exclusions](#explicit-non-responsibilities) · [Objects](#release-object-maturity-boundary) · [Inputs](#input-and-semantic-completeness-boundary) · [Outputs](#candidate-output-and-persistence-boundary) · [Outcomes](#outcome-vocabularies-and-fail-closed-behavior) · [Lifecycle](#lifecycle-and-trust-membrane) · [Dependencies](#dependency-direction) · [Effects](#inputs-outputs-and-side-effects) · [Reliability](#determinism-canonicalization-identity-replay-and-freshness) · [Security](#security-signing-key-custody-and-threat-model) · [Supply chain](#dependencies-supply-chain-and-resource-bounds) · [Telemetry](#logging-telemetry-and-error-hygiene) · [Consumers](#consumer-adoption-versioning-and-compatibility-boundary) · [Testing](#testing-fixtures-and-ci) · [Implementation](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Open](#verification-register) · [Drift](#drift-and-conflicts) · [Maintenance](#maintenance-and-change-review) · [Compatibility](#versioning-deprecation-correction-and-revocation) · [Evidence ledger](#evidence-ledger) · [Rollback](#rollback)

> [!IMPORTANT]
> **This README is not implementation evidence for release support.** It does not establish installation, import success, exports, accepted release objects, promotion behavior, signing, rollback, correction publication, receipt/proof persistence, release mutation, consumer adoption, tests, CI enforcement, deployment, or operational health.

> [!CAUTION]
> **Release-support code is not release authority.** A schema-valid candidate, signature, PromotionDecision, workflow result, pull request, merge, copied artifact, or generated summary cannot create evidence, satisfy release closure, or silently change `PUBLISHED` state.

---

## Purpose

This README defines the package-level responsibility, packaging, adoption, compatibility, validation, correction, and rollback boundary for:

```text
packages/release/
```

The package is intended to become a **small reusable library** of explicit-input, deterministic, fail-closed release-candidate mechanics shared by more than one governed pipeline, validator, worker, review tool, release workflow, runtime component, or maintenance utility.

The current repository state is narrower:

- `pyproject.toml` declares only `kfm-release` version `0.0.0`;
- the package manifest does not define a build backend, supported Python version, package discovery, dependencies, scripts, entry points, license, authors, or test configuration;
- `src/README.md` and `src/release/README.md` are evidence-grounded v1.1 boundary documents;
- `src/release/__init__.py` is empty;
- `src/release/core.py` is a comment-only greenfield placeholder;
- no functional package module, supported export, consumer import, package-local test lane, signer binding, release mutation, deployment, or runtime behavior is established;
- the release-object, signing, and promotion-gate surfaces have uneven draft or PROPOSED maturity.

This README therefore has three jobs:

1. record the **CONFIRMED placeholder state** without turning design intent into implementation fact;
2. define a **PROPOSED reusable package boundary** for future release-candidate mechanics; and
3. make packaging, contracts, schemas, policy, evidence, signing, validation, adoption, compatibility, correction, revocation, and rollback burdens explicit before use.

[Back to top](#top)

---

## Impact and operating posture

| Surface | Current status | Package effect | Required posture |
|---|---:|---|---|
| Repository placement | **CONFIRMED** | Package exists under `packages/`. | Preserve shared-library responsibility. |
| Distribution metadata | **CONFIRMED placeholder** | Name and version exist. | Do not claim installability. |
| Source envelope | **CONFIRMED placeholder** | `src/` and one namespace exist. | Keep admission narrow and evidence-backed. |
| Functional behavior | **NOT ESTABLISHED** | No release helper behavior is implemented. | Treat algorithms and modules as proposals only. |
| Public API | **NOT ESTABLISHED** | No exports or compatibility promise exists. | No consumer may rely on README-only imports. |
| Release objects | **UNEVEN maturity** | One concrete shape lane; several thin lanes. | Preserve object-specific evidence. |
| Signing | **DRAFT / unbound** | No production signer, key custody, or trust root is proved. | Integrity support only after review. |
| Consumers | **NOT ESTABLISHED** | Broad callers are design targets only. | Start with one governed internal consumer. |
| Tests and CI | **NOT ESTABLISHED for package behavior** | No package proof exists. | Add negative and replay tests before adoption. |
| Deployment and health | **UNKNOWN** | No runtime integration is proved. | Do not claim operational readiness. |
| Release and publication | **NONE** | Package has no release authority. | Preserve downstream gates and rollback. |

The package should reduce duplicated candidate-normalization and validation risk. It must not become a shortcut around contracts, schemas, policy, evidence, rights, sensitivity, review, signing, receipts, proofs, release records, correction, rollback, or governed public interfaces.

[Back to top](#top)

---

## Status and evidence

| Surface | Status | Safe conclusion |
|---|---:|---|
| Target package README | **CONFIRMED v1 before revision** | The prior guide over-described implementation. |
| Package path | **CONFIRMED present** | `packages/release/` exists. |
| Distribution metadata | **CONFIRMED placeholder** | `kfm-release`, version `0.0.0`. |
| Subpackage build/discovery | **NOT DECLARED** | Build, install, and import are unproved. |
| Source-envelope README | **CONFIRMED v1.1** | Source admission is evidence-grounded. |
| Namespace README | **CONFIRMED v1.1** | Namespace/API boundary is evidence-grounded. |
| `release/__init__.py` | **CONFIRMED empty** | No supported exports. |
| `release/core.py` | **CONFIRMED comment-only** | No release-support behavior. |
| Functional source modules | **NOT ESTABLISHED by bounded inspection** | Prior proposed module names are not facts. |
| Consumer imports | **NOT ESTABLISHED by bounded search** | Adoption is not proved. |
| Package-local tests | **NOT ESTABLISHED by bounded search** | Package behavior is not proved. |
| `ReleaseManifest` | **DRAFT / PROPOSED / thin schema** | Rich semantics exist; closure is not enforced. |
| `PromotionDecision` | **DRAFT / PROPOSED / concrete schema** | Shape validator/test exist; authorization is not proved. |
| `RollbackCard` | **DRAFT / PROPOSED / thin schema** | Declared validator absent; another validator is a placeholder. |
| `CorrectionNotice` | **DRAFT / thin schema** | Validator absent; contract-family placement is conflicted. |
| Signing standard | **DRAFT** | Key custody and production verification remain unproved. |
| Promotion-gate ADR | **PROPOSED** | Competing A–G vocabularies remain unresolved. |
| Release dry run | **EXPLICIT HOLD** | It emits no release or publication artifact. |
| Runtime health | **UNKNOWN** | No operational package is proved. |

### Corrections from v1

| Prior implication | Current evidence | v1.1 correction |
|---|---|---|
| Package metadata or language layout is merely proposed | A `pyproject.toml` and `src/release/` exist | Confirm paths; keep build/install/import unproved. |
| Proposed source modules are a near-term package layout | Those modules do not exist | Remove fictional tree and module commitments. |
| `from release...` imports are plausible examples | Import name and installability are unresolved | Remove imports from package contract. |
| Custom `READY`, `SIGNED`, `ROLLBACK_READY`, and `DRIFT` states are compatibility promises | No package API or result type exists | Require accepted object/runtime mapping before exports. |
| Broad pipelines, APIs, signing workflows, and tools consume the package | No functional consumer import surfaced | Consumer set remains UNKNOWN. |
| Signing helpers can be described without custody review | Signer, keys, trust roots, and revocation are unproved | Make signing integration gated and external. |
| Dry-run success implies release readiness | Workflow explicitly records holds | Keep dry-run evidence bounded. |
| One release-object maturity level applies to all objects | Object enforcement is uneven | Record each object separately. |

Open items must not be upgraded from `UNKNOWN` or `NEEDS VERIFICATION` based on this README alone.

[Back to top](#top)

---

## Directory Rules and authority

`packages/` is the responsibility root for reusable shared implementation libraries. `release/` at repository root is the authority root for release-governance records. Topic similarity does not collapse those responsibilities.

| Path or root | Responsibility | Package relationship |
|---|---|---|
| `packages/release/` | Package identity, packaging, adoption, compatibility | This README's scope. |
| `packages/release/src/` | Production source admission and dependency direction | Delegated to `src/README.md`. |
| `packages/release/src/release/` | Namespace/API boundary | Delegated to `src/release/README.md`. |
| `release/` | Authoritative release records and release state | External authority; package may not write directly. |
| `contracts/` | Semantic meaning | Package consumes accepted contracts. |
| `schemas/contracts/v1/` | Machine shape | Package invokes accepted validation. |
| `policy/` | Admissibility and obligations | Package does not decide policy. |
| Evidence surfaces | EvidenceRef/EvidenceBundle authority | Package preserves refs; does not create evidence. |
| `data/receipts/`, `data/proofs/` | Trust-artifact persistence | Package returns candidates only. |
| `data/<phase>/` | Lifecycle artifacts and state | Package does not own lifecycle state. |
| Security/KMS/signing infrastructure | Private keys, identities, trust roots, revocation | Package may receive public verification context only. |
| Governed APIs/UI/map/AI | Public delivery | Downstream from released state. |

No path is moved or renamed by this revision. No parallel contract, schema, policy, profile, source, registry, receipt, proof, release, catalog, signing, or documentation authority is created.

[Back to top](#top)

---

## Confirmed package inventory

At the recorded snapshot, the package inventory is:

```text
packages/release/
├── README.md
├── pyproject.toml
└── src/
    ├── README.md
    └── release/
        ├── README.md
        ├── __init__.py
        └── core.py
```

| Path | Confirmed state | Safe interpretation |
|---|---|---|
| `README.md` | v1 before this revision | Package-level contract required correction. |
| `pyproject.toml` | Name/version only | Metadata stub, not installable-distribution proof. |
| `src/README.md` | v1.1 | Source-admission boundary. |
| `src/release/README.md` | v1.1 | Namespace/API boundary. |
| `src/release/__init__.py` | Empty | No public exports. |
| `src/release/core.py` | Comment-only | No runtime behavior. |

No module beyond the two Python files above is established. Do not infer future filenames from prior documentation.

[Back to top](#top)

---

## Package, source, and namespace layers

The three README layers are complementary.

| Layer | Owns | Must not duplicate |
|---|---|---|
| Package README | Distribution identity, packaging gates, adoption, compatibility, deprecation, package-wide security and rollback | Source-file admission details or API signatures |
| Source README | What production source may enter `src/`, dependency direction, side-effect constraints, test burden | Package distribution promises or namespace exports |
| Namespace README | Public/internal API boundary, object/result semantics, verifier adapter boundary | Packaging decisions or release authority |

Change-review rule:

- packaging or supported Python changes update the package README and manifest;
- new production source classes update the source README;
- exports, types, or result mappings update the namespace README;
- cross-layer changes update all affected docs, tests, migration notes, and receipts in one reviewable change;
- no README may claim implementation that code, tests, and runtime evidence do not support.

[Back to top](#top)

---

## Packaging, build, import, and API status

### Confirmed metadata

```toml
[project]
name = "kfm-release"
version = "0.0.0"
```

The manifest does not currently declare:

- `[build-system]`;
- supported Python versions;
- package discovery;
- dependencies or optional dependencies;
- scripts or entry points;
- license, authors, classifiers, or project URLs;
- test, lint, type-check, coverage, or build configuration.

The root repository Hatchling configuration applies to the root `kfm` project and explicitly delegates subpackages to their own manifests. It does not prove this package is buildable or installable.

### Package gate

Before claiming an installable distribution:

1. choose and document a build backend;
2. declare supported Python versions;
3. configure `src/` discovery;
4. confirm the accepted import namespace;
5. declare only reviewed dependencies;
6. add build, wheel-inspection, clean-environment install, import, and uninstall tests;
7. verify no unintended packages or sensitive files enter artifacts;
8. define versioning, changelog, compatibility, deprecation, and rollback policy.

### API gate

Before claiming a supported API:

1. ratify object and result types;
2. align contracts, schemas, policy, and finite vocabularies;
3. define deliberate exports;
4. reject unknown fields and unknown outcomes where required;
5. add positive, negative, replay, security, and no-side-effect tests;
6. integrate one governed internal consumer;
7. document compatibility and migration;
8. retain a kill switch and rollback target.

Until both gates pass, `kfm-release` is a repository placeholder, not a supported package.

[Back to top](#top)

---

## Bounded context and ubiquitous language

| Term | Meaning in this package |
|---|---|
| Release candidate | Explicit-input candidate metadata presented to external governance. |
| Release authority | The governed process and records under `release/`; never this package. |
| ReleaseManifest | Release-facing binding object; current schema remains thin. |
| PromotionDecision | Governed transition decision object using `APPROVE | DENY | ABSTAIN`. |
| RollbackCard | Explicit rollback target and restoration/invalidation context. |
| CorrectionNotice | Append-only correction/supersession/withdrawal notice. |
| Candidate | Non-authoritative output requiring external validation and governance. |
| Shape validity | JSON-schema conformance; not release readiness. |
| Governance readiness | Evidence, rights, sensitivity, policy, review, receipts/proofs, integrity, correction, and rollback closure. |
| Signature verification | Integrity/identity result; not truth or publication approval. |
| Replay | Recomputing or comparing pinned candidate inputs and results. |
| Drift | Material mismatch between pinned expectations and observed result. |
| Fail closed | Refuse unsafe continuation when support is missing, stale, conflicted, or unverifiable. |
| Publication | Governed transition to `PUBLISHED`; never a package function result. |

Names that appear in drafts are not compatibility commitments until accepted and implemented.

[Back to top](#top)

---

## Proposed package responsibility envelope

Future package responsibility may include reusable mechanics for:

- explicit release-candidate input models;
- deterministic normalization of release refs and digests;
- injected schema-validator adapters;
- deterministic canonicalization and hash comparison;
- explicit PromotionDecision input assembly without deciding;
- public signature-verification result normalization without key custody;
- rollback affected/target/invalidation metadata normalization without execution;
- correction and supersession reference preservation without publication;
- replay expectation and drift comparison;
- sanitized deterministic test builders.

All such mechanics remain **PROPOSED** until implemented and tested.

The package must remain:

- reusable across more than one governed caller;
- explicit-input;
- deterministic where promised;
- no-network by default;
- candidate-only;
- evidence-subordinate;
- policy-subordinate;
- release-subordinate;
- correction- and rollback-aware.

[Back to top](#top)

---

## Explicit non-responsibilities

This package must not:

- approve, deny, abstain, or hold a promotion as release authority;
- create, mutate, publish, withdraw, supersede, or revoke authoritative release records;
- move files into or out of lifecycle phases;
- set or mutate `current`, `latest`, alias, or routing pointers;
- persist receipts, proofs, evidence bundles, review records, manifests, cards, or notices;
- evaluate policy as authority;
- resolve evidence as truth;
- store or use private signing keys;
- issue certificates, trust roots, or revocation policy;
- retrieve sources, canonical stores, unpublished candidates, or protected data;
- expose public routes, UI components, map layers, or AI answers;
- generate release claims or public summaries as sovereign truth;
- bypass separation of duties;
- turn a warning-only mismatch into release continuation.

One-off release execution belongs under accepted `tools/`, `pipelines/`, workflows, or release-authority surfaces—not this reusable package.

[Back to top](#top)

---

## Release-object maturity boundary

### `ReleaseManifest`

The semantic contract is rich, but its PROPOSED schema requires only `id` and permits additional properties.

Package implication:

- adapters may normalize explicit candidate refs and digests;
- schema validity must not be reported as governance readiness;
- the package must not persist manifests;
- evidence, rights, sensitivity, policy, review, attestation, receipt/proof, correction, rollback, and publication closure remain external.

### `PromotionDecision`

The PROPOSED schema is closed, requires eleven fields, and uses:

```text
APPROVE | DENY | ABSTAIN
```

A repository validator and fixture test exist. They prove bounded shape validation only.

Package implication:

- future code may assemble explicit inputs;
- the package must not choose the decision;
- policy evaluation, reviewer accountability, release-state mutation, and publication remain external;
- unknown outcomes must fail closed.

### `RollbackCard`

The semantic contract exists; the schema is thin. The schema-declared validator is absent, while a different validator raises `NotImplementedError`.

Package implication:

- future code may normalize explicit rollback metadata;
- no rollback-validation maturity may be claimed yet;
- no alias movement, cache invalidation, restoration, or notice publication may execute here.

### `CorrectionNotice`

The semantic contract exists under `contracts/correction/`; the schema is thin and its validator is absent. Release-vs-correction family placement remains conflicted.

Package implication:

- preserve append-only correction and supersession refs;
- do not resolve the family placement in package code;
- do not expose restricted correction details;
- do not publish notices.

### Signing and promotion gates

The signing standard is draft, ADR-0018 is proposed, and competing A–G gate vocabularies remain visible.

Package implication:

- do not hard-code a draft gate vocabulary as public API;
- do not claim production signer integration;
- accept only explicit public verification context after security review;
- keep key custody, trust roots, identities, and revocation external.

[Back to top](#top)

---

## Input and semantic-completeness boundary

Future package functions must receive explicit inputs appropriate to their operation.

| Input family | Examples | Requirement |
|---|---|---|
| Identity | release id, candidate id, run id, object version, spec hash | Stable and validated. |
| Artifacts | artifact refs, digests, media types, sizes, manifest refs | Explicit refs/digests; no hidden reads. |
| Evidence | EvidenceRef, EvidenceBundle ref, resolver status | Preserve refs; unresolved support fails closed. |
| Policy and review | PolicyDecision ref, PromotionDecision input, review/ticket refs, obligations | Consume explicit posture; do not decide. |
| Rights and sensitivity | rights result, audience, sensitivity posture, redaction refs | Unknown or stale posture fails closed. |
| Receipts and proofs | run, validation, redaction, promotion, proof refs | Preserve refs; do not persist. |
| Signing | canonical payload ref/digest, payload type, public verification context, result | No private keys or hidden KMS access. |
| Rollback and correction | affected release, target, invalidation list, correction/supersession refs | Candidate normalization only. |
| Replay | expected refs, digests, versions, prior result, comparison policy | Pinned and deterministic. |
| Time | observed, decided, built, validated, effective, expiry times | Preserve time kinds; enforce freshness externally or by accepted rules. |
| Limits | size, depth, count, timeout budgets | Bound resource use. |

Missing required input is not permission to fetch it. The safe result is a typed validation failure or external abstention/denial path, according to accepted contracts.

[Back to top](#top)

---

## Candidate output and persistence boundary

Package outputs may eventually include:

- normalized candidate values;
- local validation findings;
- deterministic digests;
- public signature-verification findings;
- replay comparison results;
- safe reason codes;
- receipt-ready metadata candidates;
- explicit warnings and obligations.

Package outputs must not be:

- authoritative ReleaseManifest, PromotionDecision, RollbackCard, or CorrectionNotice persistence;
- release approval;
- policy authority;
- evidence authority;
- proof that signing identity is trusted beyond supplied context;
- proof that rollback executed;
- public release state;
- a public API response.

Persistence belongs to owning workflows after schema, policy, evidence, review, signing, release, receipt, proof, correction, and rollback gates.

[Back to top](#top)

---

## Outcome vocabularies and fail-closed behavior

Do not collapse distinct vocabularies.

| Vocabulary | Owner/use |
|---|---|
| `APPROVE | DENY | ABSTAIN` | PromotionDecision |
| `ANSWER | ABSTAIN | DENY | ERROR` | Runtime/policy envelope |
| `PASS | FAIL | SKIPPED` | Validation and workflow reporting |
| Release record states | `release/` governance |
| Local adapter findings | Package-internal, versioned, non-authoritative |

Rules:

- package-local results must map exhaustively into accepted external contracts;
- unknown values fail closed;
- `APPROVE` is not publication;
- signature success is not truth;
- schema validity is not governance readiness;
- workflow success is not release;
- `SKIPPED` must distinguish explicit inapplicability from missing enforcement;
- stale, conflicted, revoked, or unverifiable support blocks continuation.

The previous README's `READY`, `SIGNED`, `ROLLBACK_READY`, and `DRIFT` labels are not accepted package compatibility commitments.

[Back to top](#top)

---

## Lifecycle and trust membrane

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

The package may support candidate computation near governed release transitions. It does not own lifecycle state.

A release still requires:

1. accepted object semantics and machine shape;
2. resolvable evidence;
3. rights and sensitivity posture;
4. policy decision;
5. accountable review and separation of duties where required;
6. receipts and proofs;
7. deterministic integrity support;
8. manifest and rollback/correction lineage;
9. authoritative release records;
10. governed downstream interfaces.

A file move, merge, deployment, signature, workflow success, or package result is not a release.

Public clients must consume released state through governed APIs, manifests, and approved surfaces. They must never import this package to bypass release authority.

[Back to top](#top)

---

## Dependency direction

Allowed dependency direction:

```text
accepted contracts / schemas / pure identity and hashing primitives
                         ↓
                packages/release
                         ↓
 governed internal consumers and release-owned adapters
                         ↓
     authoritative release workflows and records
```

The package should not import:

- connectors or source clients;
- lifecycle stores or release-record writers;
- public API routers or UI components;
- private-key/KMS implementations;
- AI/model providers;
- receipt/proof stores;
- mutable global policy bundles;
- environment-specific release authority.

Adapters for I/O, policy execution, signing, persistence, and public delivery belong outside the pure core and must be injected through reviewed interfaces where needed.

Circular dependencies between `packages/release` and consumer packages are prohibited.

[Back to top](#top)

---

## Inputs, outputs, and side effects

### Default side-effect posture

Core package behavior must be pure and no-network by default.

Forbidden hidden effects include:

- release or lifecycle store reads/writes;
- source retrieval;
- policy-bundle discovery;
- KMS or private-key access;
- environment-variable decisions;
- alias/current-pointer mutation;
- cache, index, tile, or CDN invalidation;
- receipt/proof persistence;
- filesystem writes;
- clock-dependent decisions without explicit time input;
- random behavior without explicit accepted seed/profile.

### Adapter posture

A future adapter may perform constrained external work only when:

- the responsibility cannot remain outside the package;
- an ADR or accepted design authorizes the seam;
- permissions are least-privilege;
- inputs and outputs are explicit;
- timeouts and size limits are enforced;
- secrets remain out of logs and exceptions;
- failure is typed and fail-closed;
- tests prove no authority drift;
- a kill switch and rollback path exist.

No adapter may turn this package into the release ledger or signer authority.

[Back to top](#top)

---

## Determinism, canonicalization, identity, replay, and freshness

Where deterministic behavior is promised, identity must bind at least:

- package/API version;
- accepted contract and schema versions;
- canonicalization profile;
- input refs and digests;
- policy/review refs where relevant;
- public verification context version;
- rollback/correction refs;
- explicit time inputs;
- limit profile.

Replay must distinguish:

- exact match;
- semantically equivalent but byte-different input;
- contract/schema version drift;
- policy/review drift;
- artifact digest drift;
- signature or trust-context drift;
- rollback-target drift;
- stale evidence or expired posture;
- unverifiable prior result;
- execution error.

The package must not hide drift behind a warning-only success.

Freshness must use explicit timestamps and accepted policy. File modification time, branch age, or log recency is not release freshness.

[Back to top](#top)

---

## Security, signing, key custody, and threat model

Private keys, KMS clients, OIDC credentials, certificate issuance, trust-root policy, signer identities, and transparency-log authority do not belong in the package.

A future verifier adapter must:

- accept explicit canonical payload and public verification context;
- bind digest, payload type, identity, issuer, and policy;
- distinguish invalid, unverifiable, stale, revoked, and error states;
- avoid network access in the pure core;
- avoid secret or protected-data leakage;
- fail closed;
- never equate signature validity with truth, rights, sensitivity clearance, or release approval.

| Threat | Required control |
|---|---|
| Package becomes release ledger | No authoritative writes |
| Schema-valid but unsafe candidate | Separate shape from governance readiness |
| Gate vocabulary drift | Versioned mapping; no draft enum hard-code |
| Signature treated as truth | Integrity-only semantics |
| Key or token leakage | No secrets in code, fixtures, logs, exceptions |
| TOCTOU | Digest/version/time binding and authority-boundary reverification |
| Stale evidence/policy/review | Explicit versions and freshness checks |
| Rollback substitution | Digest-bound target and reviewed lineage |
| Warning-only drift | Typed fail-closed result |
| Malicious nested payload | Depth, count, size, and timeout limits |
| Protected correction detail leakage | Public-safe reason/result surfaces |
| Consumer bypasses release authority | Integration and no-write tests |

Security review is required before any signing or verifier integration is treated as supported.

[Back to top](#top)

---

## Dependencies, supply chain, and resource bounds

Before adding a dependency, record:

- why the standard library or existing reviewed package is insufficient;
- exact functionality used;
- license and provenance;
- version pinning and update policy;
- vulnerability response;
- transitive dependency impact;
- offline/no-network behavior;
- artifact size impact;
- rollback strategy.

Dependency classes requiring heightened review include:

- cryptography and signing;
- canonicalization and serialization;
- policy runtimes;
- network clients;
- cloud/KMS SDKs;
- native extensions;
- dynamic plugin loaders.

Every parser, validator, canonicalizer, and verifier must define:

- maximum payload bytes;
- maximum collection count;
- maximum nesting depth;
- maximum string length;
- maximum artifact/ref count;
- timeout or step budget;
- deterministic failure mode.

Unbounded work is not release-safe.

[Back to top](#top)

---

## Logging, telemetry, and error hygiene

Allowed telemetry:

- safe package/API version;
- operation class;
- safe object id or digest prefix where policy permits;
- result class;
- stable safe reason code;
- timing and resource counters;
- contract/schema/canonicalization profile versions.

Forbidden telemetry:

- payload bodies;
- evidence bodies;
- private keys or tokens;
- raw signatures where not required;
- protected locations;
- living-person or genomic data;
- restricted correction details;
- unpublished release content;
- environment secrets;
- stack traces containing sensitive input.

Errors must be typed, bounded, actionable, and safe for the intended audience. Public error surfaces are downstream concerns and must not expose package internals.

[Back to top](#top)

---

## Consumer adoption, versioning, and compatibility boundary

The first consumer must be:

- internal;
- governed;
- reviewable;
- reversible;
- unable to mutate release state through the package;
- able to handle every negative result;
- covered by replay and rollback tests;
- protected by a kill switch.

Consumer obligations:

1. pin package/API version;
2. supply explicit validated inputs;
3. preserve evidence, policy, review, receipt/proof, signing, rollback, and correction refs;
4. treat package output as candidate-only;
5. persist authoritative objects only through release-owned workflows;
6. revalidate at the authority boundary;
7. record compatibility and migration impact;
8. avoid direct public exposure;
9. retain rollback and correction paths.

Public clients must never depend directly on the package or namespace.

[Back to top](#top)

---

## Testing, fixtures, and CI

Minimum package test matrix:

| Area | Required tests |
|---|---|
| Packaging | Build, wheel contents, clean install, import, uninstall |
| Exports | Intentional exports; unknown export failure |
| Manifest candidates | Deterministic normalization; missing/unknown fields |
| PromotionDecision | Valid/invalid shapes; exhaustive outcome mapping |
| Hashing/canonicalization | Stable digests; version drift; malformed input |
| Signing verification | Match, mismatch, stale, revoked, unverifiable, error |
| Rollback | Affected/target/invalidation completeness; substitution |
| Correction | Append-only behavior; restricted-summary safety |
| Replay | Exact match and all drift families |
| Side effects | No network, store, KMS, filesystem, alias mutation |
| Security/privacy | Secrets, keys, personal data, protected locations absent |
| Resource bounds | Oversize, depth, count, timeout |
| Consumer integration | No release mutation; negative-result handling |
| Compatibility | Upgrade, downgrade, deprecation, kill switch, rollback |

Fixture rules:

- synthetic or safely public;
- deterministic;
- minimal;
- no keys, credentials, real personal/genomic data, or protected locations;
- explicit expected result;
- no fixture doubles as an authoritative release record.

Current workflow evidence is bounded:

- `release-dry-run.yml` confirms explicit holds;
- PromotionDecision shape validation exists;
- package-native behavior is absent;
- workflow success does not prove package readiness or publication.

[Back to top](#top)

---

## Smallest sound implementation sequence

### Gate 0 — Governance resolution

- assign owners;
- confirm CODEOWNERS/ruleset expectations;
- resolve accepted import name;
- decide whether the package remains necessary as a shared library;
- resolve gate vocabulary and CorrectionNotice family placement.

### Gate 1 — Packaging

- complete `pyproject.toml`;
- configure build backend and source discovery;
- declare Python support and reviewed dependencies;
- add clean build/install/import tests.

### Gate 2 — Minimal semantic surface

- ratify minimal candidate types;
- define exhaustive result mapping;
- align contracts, schemas, policy, and docs;
- keep exports empty until tests exist.

### Gate 3 — Pure mechanics

- implement deterministic normalization;
- implement canonicalization and hash comparison using accepted profiles;
- enforce limits;
- add negative and replay tests.

### Gate 4 — Object enforcement

- harden ReleaseManifest, RollbackCard, and CorrectionNotice schemas/validators/fixtures;
- preserve PromotionDecision shape boundaries;
- separate shape validity from governance readiness.

### Gate 5 — Signing seam

- complete security review;
- define injected public-key verifier protocol;
- keep key custody external;
- add mismatch, stale, revoked, unverifiable, and error tests.

### Gate 6 — First consumer

- integrate one governed internal consumer;
- prohibit release-store mutation through the package;
- revalidate at the release authority boundary;
- add kill switch and rollback tests.

### Gate 7 — Operational graduation

- prove receipts/proofs and release handoff;
- prove compatibility and correction procedures;
- run rollback drill;
- document health signals without claiming publication authority.

No gate may claim release merely because the previous gate passed.

[Back to top](#top)

---

## Definition of done

The package is not done until all applicable criteria are evidenced:

- owners and review controls are resolved;
- package builds and installs reproducibly;
- import namespace and public API are accepted;
- exports are deliberate and minimal;
- dependencies and Python support are declared;
- contracts, schemas, policy, and result vocabularies align;
- ReleaseManifest, PromotionDecision, RollbackCard, and CorrectionNotice boundaries are enforceable;
- signing verifier is reviewed and key custody remains external;
- deterministic and replay behavior is tested;
- no-network/no-store/no-KMS boundaries are tested;
- resource and telemetry limits are enforced;
- one governed consumer is integrated;
- authoritative release persistence remains outside the package;
- positive, negative, security, privacy, replay, compatibility, correction, and rollback tests pass;
- package docs and generated receipts match behavior;
- rollback drill succeeds;
- no public client bypasses governed release interfaces.

Until then, the correct maturity label remains **greenfield placeholder** or a narrower evidenced stage.

[Back to top](#top)

---

## Verification register

| # | Item | Status |
|---:|---|---|
| 1 | Package owners | NEEDS VERIFICATION |
| 2 | Independent review/ruleset enforcement | NEEDS VERIFICATION |
| 3 | Continued need for shared package | NEEDS VERIFICATION |
| 4 | Accepted import namespace | UNKNOWN |
| 5 | Build backend | UNKNOWN |
| 6 | Supported Python versions | UNKNOWN |
| 7 | Source discovery | UNKNOWN |
| 8 | Dependencies and optional dependencies | UNKNOWN |
| 9 | License/authors/project metadata | NEEDS VERIFICATION |
| 10 | Accepted API and exports | UNKNOWN |
| 11 | First governed consumer | UNKNOWN |
| 12 | Package-local test home | UNKNOWN |
| 13 | Package CI enforcement | UNKNOWN |
| 14 | ReleaseManifest hardening and validator | NEEDS VERIFICATION |
| 15 | PromotionDecision policy/review/runtime wiring | NEEDS VERIFICATION |
| 16 | RollbackCard validator and fixtures | NEEDS VERIFICATION |
| 17 | CorrectionNotice family and validator | CONFLICTED / NEEDS VERIFICATION |
| 18 | Accepted A–G gate vocabulary | CONFLICTED / NEEDS VERIFICATION |
| 19 | Canonicalization profile | NEEDS VERIFICATION |
| 20 | Identity and digest profile | NEEDS VERIFICATION |
| 21 | Verifier protocol | UNKNOWN |
| 22 | Signer identity/trust roots | UNKNOWN |
| 23 | Revocation behavior | UNKNOWN |
| 24 | No-network enforcement | NEEDS VERIFICATION |
| 25 | Side-effect isolation | NEEDS VERIFICATION |
| 26 | Resource limits | NEEDS VERIFICATION |
| 27 | Telemetry redaction | NEEDS VERIFICATION |
| 28 | Receipt/proof candidate handoff | UNKNOWN |
| 29 | Release-authority persistence adapter | UNKNOWN |
| 30 | Separation of duties | NEEDS VERIFICATION |
| 31 | Compatibility/versioning/deprecation policy | NEEDS VERIFICATION |
| 32 | Correction and revocation process | NEEDS VERIFICATION |
| 33 | Kill switch | UNKNOWN |
| 34 | Rollback drill | NEEDS VERIFICATION |
| 35 | Deployment/runtime health | UNKNOWN |
| 36 | Public-interface integration | UNKNOWN |
| 37 | Parent/source/namespace doc reconciliation | CONFIRMED by this revision |
| 38 | Human review of generated receipt | PENDING |

[Back to top](#top)

---

## Drift and conflicts

Current documented conflicts or drift seams:

| Seam | Status | Required handling |
|---|---:|---|
| Prior package module tree vs repository inventory | CONFLICTED | Inventory wins; modules remain proposals. |
| Prior imports vs unconfigured build/import | CONFLICTED | Remove import claims. |
| Prior helper outcomes vs no API | CONFLICTED | No compatibility commitment. |
| A–G gate vocabularies | CONFLICTED | Await accepted ADR. |
| CorrectionNotice family placement | CONFLICTED | Await ADR/migration note. |
| Rich contracts vs thin schemas | CONFIRMED mismatch | Separate semantic target from enforcement. |
| Concrete PromotionDecision shape vs authorization | CONFIRMED boundary | Shape test is not release decision proof. |
| Root Hatchling project vs subpackage metadata | CONFIRMED boundary | Complete subpackage manifest separately. |
| CODEOWNERS routing vs independent approval | NEEDS VERIFICATION | Do not equate routing with governance closure. |

A future change that resolves a conflict must update the owning authority artifact, migration/ADR record where required, tests, package docs, and rollback path.

[Back to top](#top)

---

## Maintenance and change review

Review this README when:

- package metadata changes;
- source or namespace boundaries change;
- the first functional module or export is added;
- a contract, schema, policy, or outcome vocabulary changes;
- signing or verifier integration changes;
- a consumer adopts or removes the package;
- release-dry-run behavior changes;
- a correction, revocation, security issue, or rollback occurs;
- compatibility or deprecation policy changes.

Every material package change should state:

- evidence basis;
- truth labels;
- affected contracts, schemas, policy, consumers, tests, and docs;
- security/signing impact;
- release-authority impact;
- compatibility and migration impact;
- correction and rollback path;
- validation results;
- generated receipt and human-review state.

Documentation must follow behavior and must not substitute for it.

[Back to top](#top)

---

## Versioning, deprecation, correction, and revocation

Before a supported release:

- choose a versioning policy;
- define what is public versus internal;
- define compatibility guarantees;
- publish a changelog;
- define deprecation windows;
- define upgrade and downgrade tests;
- define emergency kill-switch behavior;
- define correction and revocation procedure;
- define package rollback targets.

If package behavior emitted incorrect candidate metadata:

1. disable affected consumers;
2. identify package versions, runs, candidates, releases, and public derivatives;
3. preserve prior records and evidence;
4. issue governed correction, withdrawal, supersession, or rollback where public state was affected;
5. invalidate derivatives through release authority;
6. patch or revert through review;
7. rerun validation, replay, compatibility, and rollback drills;
8. document the correction without exposing restricted details.

Package revocation does not erase history. It stops unsafe use and routes correction through governed release surfaces.

[Back to top](#top)

---

## Evidence ledger

| Evidence | Finding | Limit |
|---|---|---|
| Package inventory | Six files; metadata stub and placeholder source | No behavior or installability |
| Source README | v1.1 source-admission contract | Does not establish package API |
| Namespace README | v1.1 candidate-only API boundary | Does not establish exports or runtime |
| Release root | Owns release-governance records | Lane conventions still contain open questions |
| ReleaseManifest | Rich draft meaning, thin schema | No production closure |
| PromotionDecision | Concrete proposed shape and test | No authorization |
| RollbackCard | Rich meaning, thin schema | Validator incomplete |
| CorrectionNotice | Rich meaning, thin schema | Placement/validator unresolved |
| Signing standard | Draft | No production signer or trust-root proof |
| Promotion-gate ADR | Proposed | Vocabulary not accepted |
| Release dry run | Explicit holds | No release emitted |
| CODEOWNERS | Package path routed for review | Not proof of independent approval |

### Maintainer checklist

- [ ] Verify owners, base, package inventory, and object maturity.
- [ ] Keep release authority outside the package.
- [ ] Keep key custody and signer authority outside the package.
- [ ] Add tests before exports.
- [ ] Protect secrets, personal data, protected locations, and release payloads.
- [ ] Preserve evidence, policy, review, receipt/proof, correction, and rollback refs.
- [ ] Record compatibility, migration, correction, revocation, and rollback impact.
- [ ] Update all affected documentation and generated receipts.
- [ ] Require human review separate from release/publication approval.

[Back to top](#top)

---

## Rollback

### Before merge

- close the pull request;
- abandon the review branch;
- preserve generated review evidence as policy permits;
- do not mutate shared history.

### After merge

- use a revert pull request;
- preserve the original README and generated receipt in Git history;
- update any later documentation that depended on the reverted contract;
- record authority drift if the package had been used to bypass release governance.

### Behavioral rollback

No behavioral rollback is required for this documentation-only revision because it changes no code, package metadata, dependency, contract, schema, policy, validator, fixture, test, workflow, release record, signature, receipt/proof instance, lifecycle artifact, public route, deployment, or publication state.

[Back to top](#top)
