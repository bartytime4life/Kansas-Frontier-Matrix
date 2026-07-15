<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-evidence-resolver-readme
title: packages/evidence-resolver/ — Governed Evidence Resolution Helper Package
type: readme
version: v0.2
status: draft; repository-grounded; python-package-scaffold; non-authoritative
owners:
  - OWNER_TBD — Evidence resolver package owner
  - OWNER_TBD — Evidence and proof steward
  - OWNER_TBD — Contract and schema steward
  - OWNER_TBD — Policy, rights, and sensitivity steward
  - OWNER_TBD — Runtime and governed API steward
  - OWNER_TBD — Release, correction, validator, security, packaging, and docs steward
created: NEEDS VERIFICATION — target file existed before this revision
updated: 2026-07-15
supersedes: v1 planning-oriented package guide (2026-06-14)
policy_label: public; packages; evidence-resolver; python; EvidenceRef; EvidenceBundle; closure-validation; no-network-by-default; cite-or-abstain; fail-closed; non-authoritative
path: packages/evidence-resolver/README.md
truth_posture: CONFIRMED target and prior blob, packages responsibility root, kfm-evidence-resolver 0.0.0 metadata, Python src layout, merged source-root and child-module v0.2 contracts, empty initializer, bounded absence of selected resolver modules and package.json, sibling packages/evidence boundary, fielded closed EvidenceRef and EvidenceBundle schemas, paired draft contracts, minimal fixture families, generic schema harness, existing EvidenceBundle validator, missing schema-declared EvidenceRef validator, echo-only evidence-resolver workflow, Directory Rules v1.4, and current common SpecHash contract/schema / PROPOSED future deterministic resolver candidate helpers, explicit profile adapters, lookup-snapshot adapters, generated schema adapters, deliberate exports, package tests, distribution metadata, compatibility adapters, and governed consumers / CONFLICTED architecture EvidenceRef and EvidenceBundle shapes versus current paired schemas, JCS-prefixed architecture hash notation versus current SpecHash shape, resolver-local outcomes versus runtime outcomes and NEEDS_REVIEW, strong structured scope checks versus current free-form claim_scope, evidence-resolver versus packages/evidence responsibility overlap, and package-specific versus contract-schema test/fixture placement / UNKNOWN build backend, Python requirement, dependencies, package discovery, license metadata, public exports, import consumers, registry adapter, package-specific CI, runtime/API wiring, package publication, release integration, and production behavior / NEEDS VERIFICATION accepted owners, canonical resolver profiles and outcomes, registry and supersession contracts, canonicalization profile, reason-code vocabulary, policy handoff, correction invalidation, package publication, and rollback integration
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 8af224617684d8e708c7550510a1f27d314e585a
  prior_blob: 8a6aa41745dcdef75a3b48110b3ff963e10751c7
  source_root_blob: ec71b65875731ca3cbfca6a29839172b52b48418
  source_module_blob: 62dd6340557b9ea2076ee8d5b0c579149ab06bc0
related:
  - ./pyproject.toml
  - ./src/README.md
  - ./src/evidence_resolver/README.md
  - ./src/evidence_resolver/__init__.py
  - ../README.md
  - ../evidence/README.md
  - ../../contracts/evidence/evidence_ref.md
  - ../../contracts/evidence/evidence_bundle.md
  - ../../contracts/common/spec_hash.md
  - ../../schemas/contracts/v1/evidence/evidence_ref.schema.json
  - ../../schemas/contracts/v1/evidence/evidence_bundle.schema.json
  - ../../schemas/contracts/v1/common/spec_hash.schema.json
  - ../../fixtures/contracts/v1/evidence/evidence_ref/README.md
  - ../../fixtures/contracts/v1/evidence/evidence_bundle/README.md
  - ../../tools/validators/validate_evidence_bundle.py
  - ../../tests/schemas/test_common_contracts.py
  - ../../docs/architecture/evidence-identity.md
  - ../../docs/doctrine/directory-rules.md
  - ../../.github/workflows/evidence-resolver.yml
tags: [kfm, packages, evidence-resolver, python, package-boundary, EvidenceRef, EvidenceBundle, closure, resolver-profile, claim-scope, spec-hash, generated-code, deterministic, no-network, fail-closed, cite-or-abstain, rollback]
notes:
  - "v0.2 replaces stale planning language with a commit-pinned description of the current kfm-evidence-resolver 0.0.0 Python package scaffold."
  - "The merged src/README.md and src/evidence_resolver/README.md v0.2 documents own source-root and resolver-candidate detail; this file owns package-level responsibility, consumer, packaging, compatibility, and trust-boundary posture."
  - "The import package initializer is empty and selected resolver module paths are absent; no supported API, build behavior, consumer, registry adapter, or production resolution behavior is claimed."
  - "Architecture prose, paired schemas, hash notation, scope semantics, and resolver outcome vocabularies conflict; the package requires explicit profile selection and forbids silent compatibility invention."
  - "Only this Markdown file changes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Evidence Resolution Helper Package

`packages/evidence-resolver/`

> Shared Python package boundary for reusable, deterministic, side-effect-minimal helpers that may prepare evidence-resolution **candidates** from explicit `EvidenceRef` values and caller-supplied governed lookup snapshots. The current repository surface is a **greenfield `0.0.0` scaffold**, not an implemented resolver library: package metadata is minimal, the import initializer is empty, no supported exports or production consumers are established, and material contract/schema/profile conflicts remain unresolved.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.2-informational)
![distribution](https://img.shields.io/badge/distribution-kfm--evidence--resolver-3776ab)
![implementation](https://img.shields.io/badge/implementation-placeholder-lightgrey)
![boundary](https://img.shields.io/badge/boundary-EvidenceRef%E2%86%92EvidenceBundle-6f42c1)
![network](https://img.shields.io/badge/network-none%20by%20default-455a64)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-0b7285)

**Quick links:** [Purpose](#purpose-and-audience) · [Status](#current-repository-state) · [Context](#package-bounded-context) · [Placement](#placement-and-authority) · [Package map](#current-package-surface) · [Responsibilities](#owned-responsibilities) · [Exclusions](#explicit-non-ownership) · [Root/module split](#package-source-root-and-module-split) · [Sibling](#relationship-to-packagesevidence) · [Profiles](#contract-schema-and-architecture-profile-conflicts) · [EvidenceRef](#evidenceref-boundary) · [EvidenceBundle](#evidencebundle-boundary) · [Scope](#claim-scope-and-closure-boundary) · [Outcomes](#resolver-outcome-boundary) · [Inputs](#accepted-inputs) · [Outputs](#permitted-outputs) · [Consumers](#consumer-and-public-interface-boundary) · [Dependencies](#dependency-direction) · [Identity](#identity-hashing-time-and-supersession) · [Trust](#lifecycle-policy-release-and-public-safety) · [Failures](#failure-and-error-semantics) · [Security](#security-privacy-and-data-minimization) · [Packaging](#packaging-distribution-and-versioning) · [Tests](#tests-fixtures-validators-and-ci) · [Evolution](#implementation-admission-sequence) · [Compatibility](#compatibility-correction-and-rollback) · [Done](#definition-of-done) · [Backlog](#open-verification-register) · [Ledger](#evidence-ledger)

> [!IMPORTANT]
> **Repository snapshot:** `main@8af224617684d8e708c7550510a1f27d314e585a`<br>
> **Distribution:** `kfm-evidence-resolver`<br>
> **Declared version:** `0.0.0`<br>
> **Verified source root:** `src/`<br>
> **Verified import package:** `src/evidence_resolver/`<br>
> **Verified implementation:** empty `src/evidence_resolver/__init__.py`; selected resolver modules were absent<br>
> **Verified child contracts:** [`src/README.md`](./src/README.md) v0.2 and [`src/evidence_resolver/README.md`](./src/evidence_resolver/README.md) v0.2<br>
> **Build backend, Python requirement, dependencies, package discovery, exports, consumers, and package publication:** not established<br>
> **Evidence schemas/contracts:** present but `PROPOSED`, with documented architecture/schema, hash, scope, and outcome drift<br>
> **Resolver workflow:** present, but both jobs are `echo TODO` scaffolds

> [!CAUTION]
> Resolution is not truth. Schema validity is not evidence closure. `bundle_ref` is not a verified bundle. A matching digest is not policy clearance. A `RESOLVED` candidate is not release approval or a public answer. A package import is not the governed trust membrane.

---

## Purpose and audience

`packages/evidence-resolver/` is the package-level boundary for reusable evidence-resolution helper implementation.

A mature package may provide deterministic or side-effect-minimal support for:

- explicit resolver-profile selection;
- local validation of current-profile `EvidenceRef` candidates;
- local validation of caller-supplied EvidenceBundle candidates or lookup snapshots;
- comparison of profile-defined ids, refs, hashes, scope fields, and supersession context;
- deterministic issue carriers for malformed, missing, inconsistent, unsupported, stale, superseded, restricted, or blocked resolution context;
- candidate resolver results for downstream policy, citation, release, and runtime-envelope handling;
- generated schema adapters with pinned provenance;
- compatibility adapters between explicitly accepted versions;
- synthetic, public-safe, no-network fixtures;
- package-level imports used by more than one governed internal consumer.

This package is for:

- evidence resolver package maintainers;
- evidence, proof, contract, schema, policy, release, and correction stewards;
- governed runtime and API maintainers;
- validator and test maintainers;
- security, privacy, rights, packaging, and dependency reviewers;
- application, pipeline, tool, and domain-package authors considering this package as a dependency;
- reviewers deciding whether proposed behavior belongs in this package, `packages/evidence/`, a registry/proof service, a validator, policy, release, runtime, or an application.

It must not fetch sources, own the bundle registry, materialize proof records, evaluate policy, write lifecycle state, persist receipts, approve release, orchestrate runtime services, expose public routes, render UI/map content, call model providers, or make generated language true.

[Back to top](#top)

---

## Current repository state

### Evidence snapshot

| Field | Value |
|---|---|
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Repository ID | `1059091169` |
| Visibility | public |
| Base ref | `main` |
| Base commit | `8af224617684d8e708c7550510a1f27d314e585a` |
| Prior target blob | `8a6aa41745dcdef75a3b48110b3ff963e10751c7` |
| Source-root blob | `ec71b65875731ca3cbfca6a29839172b52b48418` |
| Source-module blob | `62dd6340557b9ea2076ee8d5b0c579149ab06bc0` |
| Current revision | documentation-only package v0.2 proposal |

### Verified package surface

| Surface | Evidence at snapshot | Status | Consequence |
|---|---|---:|---|
| This README | Existing v1 planning-oriented package guide. | **CONFIRMED** | Revised in place. |
| [`pyproject.toml`](./pyproject.toml) | Declares `[project]`, name `kfm-evidence-resolver`, and version `0.0.0` only. | **CONFIRMED minimal placeholder** | Distribution identity is known; build and dependency behavior are not. |
| [`src/README.md`](./src/README.md) | Merged repository-grounded source-root contract v0.2. | **CONFIRMED** | Source layout, imports, generated-code, packaging, test-placement, and compatibility boundaries are grounded. |
| [`src/evidence_resolver/README.md`](./src/evidence_resolver/README.md) | Merged repository-grounded source-module contract v0.2. | **CONFIRMED** | Resolver-candidate semantics, profile conflicts, failure handling, and safety detail live there. |
| `src/evidence_resolver/__init__.py` | Exists and is empty. | **CONFIRMED** | Import-package marker only; no supported exports are established. |
| `package.json` | Absent at `packages/evidence-resolver/package.json` during bounded checks. | **CONFIRMED bounded absence** | Do not claim a JavaScript/TypeScript package. |
| Selected helper modules | `outcomes.py`, `resolver.py`, `closure.py`, and `scope.py` were absent at exact tested paths. | **CONFIRMED bounded absence** | No executable resolver implementation is established. |
| Build backend | No `[build-system]` section was observed. | **NOT OBSERVED** | Build/install behavior remains unknown. |
| Dependencies | No dependency list was observed. | **NOT OBSERVED** | Do not claim `jsonschema`, registry, API, crypto, or runtime dependencies. |
| Supported Python versions | No `requires-python` field was observed. | **NOT OBSERVED** | Interpreter support is unknown. |
| Package discovery | No explicit discovery configuration was observed. | **NOT OBSERVED** | Editable install and wheel inclusion are unproven. |
| Public exports | Empty initializer. | **NOT ESTABLISHED** | No symbol is part of a supported package API. |
| Consumers | Indexed checks did not establish production imports of `evidence_resolver`. | **NOT OBSERVED / search-limited** | Do not claim runtime or API integration. |
| Sibling package | `packages/evidence/README.md` exists. | **CONFIRMED README** | Ref/digest helper and resolver responsibilities must not collapse silently. |
| EvidenceRef contract/schema | Paired draft contract and fielded closed schema exist. | **CONFIRMED surfaces / `PROPOSED` status** | Package code must bind to an explicit profile. |
| EvidenceBundle contract/schema | Paired draft contract and fielded closed schema exist. | **CONFIRMED surfaces / `PROPOSED` status** | Closure checks must use actual schema fields, not architecture-only fields. |
| SpecHash contract/schema | Current object profile uses `{ "value": "sha256:<hex>" }`. | **CONFIRMED surfaces / `PROPOSED` status** | Architecture `jcs:sha256:` notation cannot be assumed equivalent. |
| EvidenceRef validator | Schema declares `tools/validators/validate_evidence_ref.py`; exact file is absent. | **CONFLICTED metadata / file state** | Package docs and code must not claim dedicated validator availability. |
| EvidenceBundle validator | `tools/validators/validate_evidence_bundle.py` exists. | **CONFIRMED file** | Presence does not prove package behavior. |
| Contract fixture families | One documented valid and one invalid case exist for each evidence object. | **CONFIRMED minimal coverage** | Coverage is narrow and schema-only. |
| Generic schema harness | `tests/schemas/test_common_contracts.py` includes the evidence family. | **CONFIRMED test code** | Package-level resolver tests are not established. |
| Package test README | `tests/packages/evidence-resolver/README.md` was absent at the exact tested path. | **CONFIRMED bounded absence** | No package-specific test lane is documented there. |
| Package fixture README | `fixtures/packages/evidence-resolver/README.md` was absent at the exact tested path. | **CONFIRMED bounded absence** | No package-specific fixture lane is documented there. |
| Resolver workflow | `.github/workflows/evidence-resolver.yml` defines two jobs. | **CONFIRMED echo-only scaffold** | Green workflow status does not prove resolution or fail-closed behavior. |
| Resolver input/result contract | No contract/schema was found at exact tested `evidence_resolution` paths. | **NOT FOUND at tested paths** | A stable result API cannot be declared yet. |
| Runtime/release evidence | No deployed consumer, runtime log, receipt, proof pack, release artifact, registry publication, or public response was inspected. | **UNKNOWN** | This README is not implementation, deployment, or publication proof. |

```text
Python distribution identity            = CONFIRMED
Python src-layout container              = CONFIRMED
evidence_resolver import package         = CONFIRMED
empty initializer                        = CONFIRMED
implemented resolver modules             = NOT OBSERVED
supported public exports                 = NOT ESTABLISHED
package consumers                        = NOT OBSERVED
build/install behavior                   = UNKNOWN
package-specific tests/fixtures          = NOT ESTABLISHED
contract schemas/fixtures                = CONFIRMED, PROPOSED/narrow
EvidenceRef dedicated validator          = DECLARED BUT ABSENT
resolver workflow                        = CONFIRMED, ECHO-ONLY
runtime/API behavior                     = UNKNOWN
package registry publication             = UNKNOWN
release behavior                         = UNKNOWN
```

[Back to top](#top)

---

## Package bounded context

The bounded context is:

> The package-level ownership, admission, compatibility, distribution, and consumer boundary for reusable evidence-resolution helper implementation.

It includes:

- package identity and metadata;
- source-root organization;
- import package and supported exports;
- package discovery and build configuration;
- dependency direction;
- public-versus-internal API designation;
- resolver-profile pinning;
- generated-code provenance;
- package-level tests and fixture integration;
- consumer compatibility;
- deprecation and migration;
- package distribution and integrity;
- correction and rollback posture.

It excludes:

- EvidenceRef and EvidenceBundle semantic meaning;
- canonical schema shape;
- registry or proof storage;
- source admission;
- evidence admissibility decisions;
- policy and sensitivity evaluation;
- lifecycle state and promotion;
- receipt/proof persistence;
- release approval and release-state mutation;
- runtime orchestration;
- public API serialization;
- UI/map rendering;
- model-provider execution;
- truth determination.

### Ubiquitous language

| Term | Meaning here | Not equivalent to |
|---|---|---|
| Package | Reusable implementation distribution boundary. | Deployable service, authority root, or public API. |
| Source root | `src/` container used to organize importable package code. | Proof that packaging/discovery works. |
| Import package | `src/evidence_resolver/` Python namespace. | Supported public API. |
| EvidenceRef | Current-profile governed pointer candidate. | Evidence closure or publication permission. |
| EvidenceBundle | Current-profile claim-scope closure object candidate. | Policy decision, release approval, or proof-store placement. |
| Lookup snapshot | Explicit, caller-supplied registry/proof response used as resolver input. | Package-owned registry or live-store authority. |
| Resolver candidate | Deterministic local result prepared for downstream governance. | Runtime answer or released claim. |
| Resolver profile | Explicit contract/schema/version/hash combination. | “Latest” inferred from ambient repository state. |
| Compatibility adapter | Explicit, tested conversion between accepted profiles. | Silent field renaming or best-effort coercion. |
| Generated adapter | Derived code tied to a schema version and generation receipt. | New semantic or schema authority. |
| Package release | Distribution of helper code. | Publication of KFM evidence or claims. |
| Consumer | Internal code that imports the supported package API. | Public client calling package internals. |

[Back to top](#top)

---

## Placement and authority

Directory Rules classify `packages/` as the responsibility root for shared reusable implementation.

```text
packages/evidence-resolver/                     = package-level boundary
packages/evidence-resolver/src/                 = Python source-root container
packages/evidence-resolver/src/evidence_resolver/ = import package
packages/evidence/                              = sibling general evidence-helper lane
contracts/evidence/                             = semantic meaning
schemas/contracts/v1/evidence/                  = machine shape
policy/evidence/                                = evidence policy/admissibility
fixtures/contracts/v1/evidence/                 = contract-schema fixtures
tools/validators/                               = validator implementations
data/proofs/                                    = materialized proof/evidence records
data/receipts/                                  = process and validation memory
release/                                        = release, correction, withdrawal, rollback
apps/                                           = governed deployables and public interfaces
```

### Authority matrix

| Concern | Package authority | Governing home |
|---|---:|---|
| EvidenceRef meaning | None | `contracts/evidence/evidence_ref.md` |
| EvidenceRef machine shape | None | `schemas/contracts/v1/evidence/evidence_ref.schema.json` |
| EvidenceBundle meaning | None | `contracts/evidence/evidence_bundle.md` |
| EvidenceBundle machine shape | None | `schemas/contracts/v1/evidence/evidence_bundle.schema.json` |
| SpecHash meaning/shape | None | common contract/schema family |
| Registry lookup truth | None | accepted registry/proof system |
| Materialized evidence closure | None | governed EvidenceBundle/proof records |
| Rights and sensitivity | None | source descriptors, rights review, and policy |
| Policy outcome | None | policy systems and PolicyDecision records |
| Release approval | None | release workflows and records |
| Public runtime outcome | None | governed API/runtime envelopes |
| Local resolver candidate logic | Supporting only | accepted package source and tests |
| Package exports/version | Package-level responsibility | this package plus accepted packaging configuration |

Importing a schema model, comparing hashes, returning a status, or constructing a candidate does not move semantic, policy, registry, proof, release, or public authority into this package.

[Back to top](#top)

---

## Current package surface

```text
packages/evidence-resolver/
├── README.md
├── pyproject.toml
└── src/
    ├── README.md
    └── evidence_resolver/
        ├── README.md
        └── __init__.py
```

### Status of the observed tree

| Path | Status | Role |
|---|---:|---|
| `README.md` | **CONFIRMED** | Package-level boundary and governance contract. |
| `pyproject.toml` | **CONFIRMED minimal placeholder** | Distribution name/version only. |
| `src/README.md` | **CONFIRMED v0.2** | Source-root, discovery, import, generated-code, test-placement, and compatibility contract. |
| `src/evidence_resolver/README.md` | **CONFIRMED v0.2** | Resolver-candidate, profile, object, failure, and safety contract. |
| `src/evidence_resolver/__init__.py` | **CONFIRMED empty** | Namespace marker; no exports established. |
| Resolver implementation modules | **NOT OBSERVED at tested paths** | Do not claim implementation. |
| Package tests | **NOT ESTABLISHED** | Contract-schema tests exist elsewhere. |
| Package fixtures | **NOT ESTABLISHED** | Contract-schema fixtures exist elsewhere. |
| Build/discovery config | **NOT ESTABLISHED** | Do not claim installability. |
| Published package artifact | **UNKNOWN** | No registry artifact inspected. |

> [!WARNING]
> A README tree is not an implementation tree. The package currently documents where code may belong and how it must behave if admitted; it does not prove that resolver code exists or that the distribution can be built or installed.

[Back to top](#top)

---

## Owned responsibilities

The package may own these responsibilities after explicit implementation and validation:

1. **Package identity** — distribution name, package version, supported Python versions, license metadata, build backend, and dependency declaration.
2. **Source admission** — which resolver modules are included in the distribution.
3. **Public import surface** — intentional exports, stability tier, deprecation path, and semantic versioning.
4. **Profile binding** — explicit references to accepted EvidenceRef, EvidenceBundle, SpecHash, resolver-result, and reason-code profiles.
5. **Pure candidate checks** — deterministic checks over explicit values and caller-supplied lookup snapshots.
6. **Generated adapter provenance** — schema source, generator version, command, input digest, output digest, and regeneration rules.
7. **Compatibility adapters** — reviewed conversions between accepted profile versions.
8. **Package tests** — unit/property/negative tests for supported exports and imports.
9. **Distribution integrity** — reproducible package artifacts, checksums, changelog, and rollback instructions.
10. **Consumer contract** — documented supported internal consumers and version compatibility.

These responsibilities remain **PROPOSED** until code, packaging metadata, tests, consumers, and artifacts verify them.

[Back to top](#top)

---

## Explicit non-ownership

This package must not own or silently perform any of the following:

| Non-owned concern | Required owner |
|---|---|
| EvidenceRef or EvidenceBundle semantics | `contracts/evidence/` |
| JSON Schema authority | `schemas/contracts/v1/evidence/` |
| SpecHash canonicalization standard | accepted common contract/standard and tooling |
| Bundle registry or supersession index | accepted registry/proof system |
| Materialized EvidenceBundle storage | `data/proofs/` or accepted proof home |
| Source descriptors and source-role authority | source registry roots |
| Rights, sensitivity, admissibility, or disclosure decisions | policy and review systems |
| RAW/WORK/QUARANTINE/PROCESSED/CATALOG/TRIPLET/PUBLISHED data | lifecycle `data/` roots |
| Receipt persistence | `data/receipts/` |
| Release, correction, withdrawal, supersession, rollback decisions | `release/` |
| Governed API routes or serializers | application/runtime roots |
| UI, Evidence Drawer, MapLibre, Focus Mode rendering | UI/application roots |
| Model calls or generated answers | governed AI runtime |
| Secrets, credentials, tokens, private raw records, chain-of-thought | never package source or fixtures |

### Prohibited authority verbs

Package APIs should not expose authority verbs such as:

```text
publish
approve_release
promote
write_proof
store_bundle
decide_policy
allow_public
deny_public
force_resolved
ignore_policy
bypass_release
read_raw
fetch_source
generate_truth
```

A helper named with an authority verb creates ambiguity even when its implementation is small. Use narrower names that describe local candidate construction or validation.

[Back to top](#top)

---

## Package, source root, and module split

The three README layers have distinct responsibilities.

| Layer | Owns | Does not own |
|---|---|---|
| `packages/evidence-resolver/README.md` | Package identity, responsibility, consumers, packaging, versioning, compatibility, admission, and package rollback. | Detailed module API or source layout internals. |
| `packages/evidence-resolver/src/README.md` | Python source-root, discovery, imports/exports, generated code, dependency direction, test placement, and enforceability placement. | Package-wide distribution policy or resolver semantics. |
| `packages/evidence-resolver/src/evidence_resolver/README.md` | Resolver-candidate semantics, object/profile boundaries, proposed module interface, local failures, and security behavior. | Build backend, package publication, or package consumer compatibility. |

Rules:

- package documentation may summarize child boundaries but should link rather than duplicate every detail;
- child docs may refine but must not contradict package responsibility;
- implementation changes that affect multiple layers must update all affected READMEs;
- a stable public export requires package-level admission, source-root import rules, module semantics, and tests;
- generated files must not become an undocumented fourth authority layer.

[Back to top](#top)

---

## Relationship to `packages/evidence`

The repository currently documents two sibling package lanes.

| Package | Intended responsibility | Current implementation proof | Risk |
|---|---|---:|---|
| `packages/evidence/` | General evidence refs, identities, digest helpers, citation carriers, and fixtures. | README-backed; implementation maturity not established here. | Can absorb resolver behavior and blur closure authority. |
| `packages/evidence-resolver/` | EvidenceRef → EvidenceBundle candidate resolution and closure-check helpers. | `0.0.0` scaffold; no resolver modules observed. | Can duplicate general evidence primitives or become a registry/proof service. |

### Boundary rules

- General value-object parsing or digest helpers belong in the general evidence package when reused outside resolution.
- Resolution-specific orchestration and candidate issue/result types may belong here after contracts are accepted.
- Registry I/O belongs in an adapter/service boundary, not silently inside a pure resolver core.
- EvidenceBundle storage and proof retrieval remain outside both packages.
- Shared types must have one source of truth and one import direction.
- Cross-import cycles between the two packages are prohibited.
- Consolidation, renaming, or responsibility transfer is ADR-class because it changes imports, consumers, schemas, tests, docs, compatibility, and rollback.

### Decision test

Place code here only when all are true:

1. the behavior is specifically about resolving or checking an EvidenceRef against explicit bundle/lookup context;
2. the behavior is reusable across more than one governed internal consumer;
3. the behavior is deterministic or side-effect-minimal;
4. the behavior does not own registry/proof I/O, policy, release, or lifecycle state;
5. an accepted profile defines the fields the behavior examines;
6. package-level tests can prove positive and negative behavior.

[Back to top](#top)

---

## Contract, schema, and architecture profile conflicts

The package must not pretend the current evidence object family is internally reconciled.

### Conflict summary

| Area | Architecture prose | Current paired schema/contract | Package consequence |
|---|---|---|---|
| EvidenceRef shape | Rich profile including reference identity, target hash, expected digest, resolution strategy, and policy metadata. | Closed object with `ref`, `kind`, optional `bundle_ref`. | Architecture-only fields cannot be read from current-profile objects. |
| EvidenceBundle shape | Rich inputs/parameters/artifacts/checks/integrity/signature families. | Closed object with `bundle_id`, `claim_scope`, `evidence_refs`, `source_records`, `citations`, `rights`, `sensitivity`, `transforms`, `checksums`, `spec_hash`. | Builders/checkers must bind to one explicit profile. |
| Hash notation | `jcs:sha256:<hex>` architecture convention. | Current SpecHash object wraps `sha256:<hex>` in `value`; canonicalization is not encoded. | Equality and canonicalization cannot be inferred across profiles. |
| Resolver outcomes | Architecture includes runtime outcomes and `NEEDS_REVIEW`; older package prose uses local statuses. | Current runtime envelope uses a finite public outcome family elsewhere. | Local results need an accepted contract and explicit mapping. |
| Scope checks | Field/time/space/source-role-aware matching. | Current `claim_scope` is a free-form string and EvidenceRef is minimal. | Strong structured scope claims are not implementable from current fields alone. |
| Validator coverage | Schema metadata declares validators. | EvidenceBundle wrapper exists; EvidenceRef wrapper is absent. | Validator capability must be reported object by object. |

### Required profile discipline

Every package function that consumes or emits governed objects must identify:

- contract family;
- schema path or schema identifier;
- schema/profile version;
- schema/spec hash when available;
- compatibility adapter, if any;
- accepted field set;
- outcome/reason-code vocabulary;
- canonicalization profile;
- registry/supersession profile;
- policy and release handoff assumptions.

### Prohibited silent translation

The package must not silently:

- rename architecture fields into schema fields;
- infer `bundle_ref` from unrelated identifiers;
- manufacture expected digests;
- treat `claim_scope` prose as structured field/time/space data;
- strip unknown fields and call the result valid;
- convert `NEEDS_REVIEW` into `ABSTAIN` or another outcome without an accepted mapping;
- assume `jcs:sha256:` and `{ "value": "sha256:..." }` are interchangeable;
- follow supersession to a new bundle without preserving the original request and traversal record;
- treat a missing validator as a successful validation path.

Until an ADR/contract/schema migration resolves these conflicts, compatibility adapters remain **PROPOSED** and must fail closed on ambiguous input.

[Back to top](#top)

---

## EvidenceRef boundary

The current paired EvidenceRef schema confirms this closed shape:

```json
{
  "ref": "obs:1",
  "kind": "measurement",
  "bundle_ref": "optional-bundle-id"
}
```

Current machine-shape facts:

- `ref` is required and is a string;
- `kind` is required;
- `kind` is one of `measurement`, `record`, `dataset`, or `artifact`;
- `bundle_ref` is optional and is a string;
- undeclared top-level fields are rejected;
- schema metadata marks the profile `PROPOSED`.

Package rules:

- preserve `ref`, `kind`, and `bundle_ref` exactly;
- do not reinterpret `ref` by naming convention alone;
- absence of `bundle_ref` is pre-closure by default;
- presence of `bundle_ref` is a claim that still requires governed lookup and validation;
- do not infer rights, sensitivity, source role, time, space, release, or policy from the minimal object;
- do not treat a schema-valid EvidenceRef as proof that the referenced evidence exists;
- do not declare dedicated EvidenceRef validator support while the declared wrapper file is absent.

[Back to top](#top)

---

## EvidenceBundle boundary

The current paired EvidenceBundle schema requires:

```text
bundle_id
claim_scope
evidence_refs
source_records
citations
rights
sensitivity
transforms
checksums
spec_hash
```

Current machine-shape facts:

- `bundle_id` matches the current lowercase identifier pattern;
- `claim_scope` is a string;
- `evidence_refs`, `source_records`, and `citations` require at least one item;
- `rights` requires `license` and is closed;
- `sensitivity` references the policy sensitivity profile;
- `transforms` is required but may be empty under the current schema;
- `checksums` requires at least one `sha256:<64 lowercase hex>` value;
- `spec_hash` references the common SpecHash object;
- undeclared top-level fields are rejected;
- schema metadata marks the profile `PROPOSED`.

Package rules:

- validate the whole current-profile object before local closure checks;
- preserve evidence refs, source records, citations, rights, sensitivity, transforms, checksums, and spec hash;
- do not accept architecture-only fields as current-profile fields;
- do not make registry existence or release claims from schema validity;
- do not treat non-empty arrays as proof of adequacy or authority;
- do not hide mixed source roles, restricted citations, or transform gaps supplied by callers;
- do not mutate a bundle to “repair” missing required fields;
- return explicit issues when profile validation or local consistency checks fail.

[Back to top](#top)

---

## Claim-scope and closure boundary

Current `claim_scope` is free-form. Therefore, the package cannot truthfully claim structured matching for:

- object id;
- field path;
- temporal interval;
- spatial geometry or resolution;
- source-role distribution;
- audience;
- significance tier;
- policy purpose;
- correction lineage.

A structured scope checker requires an accepted structured scope contract or an explicit caller-supplied normalized scope object.

### Allowed current behavior

A package helper may:

- require a non-empty current-profile `claim_scope` string when schema validation does not already ensure non-empty content;
- compare exact strings only when the caller selected that explicit policy;
- preserve a caller-supplied structured scope object in a separate, accepted resolver-input profile;
- return `scope/unverifiable` when required structured context is unavailable;
- avoid public-answer eligibility when claim-scope support cannot be demonstrated.

### Prohibited current behavior

A package helper must not:

- parse arbitrary natural-language scope into authoritative structured meaning without a contract;
- infer temporal or spatial coverage from bundle ids or citations;
- treat exact string equality as universal semantic equivalence;
- widen supported claim scope beyond the bundle’s declared scope;
- report full closure when required scope dimensions are absent.

[Back to top](#top)

---

## Resolver outcome boundary

A package-local resolver result contract is not currently established at the tested canonical paths.

### Candidate local vocabulary

The earlier package prose used:

```text
RESOLVED
UNRESOLVED
DENIED
ERROR
```

This vocabulary is useful as a design discussion, but it is not yet a verified public package API.

### Boundary to public runtime outcomes

A future mapping might follow this shape:

| Local candidate state | Downstream public candidate | Additional gates required |
|---|---|---|
| `RESOLVED` | potentially `ANSWER` | policy, citation, release, correction, freshness, envelope validation |
| `UNRESOLVED` | generally `ABSTAIN` | reason-code and evidence-gap handling |
| `DENIED` | generally `DENY` | accepted policy decision and redaction-safe reason summary |
| `ERROR` | generally `ERROR` | safe error classification and observability |

This table is **PROPOSED**, not a compatibility guarantee.

### `NEEDS_REVIEW` conflict

Architecture prose includes `NEEDS_REVIEW`, but current public finite-outcome surfaces elsewhere use a smaller set. The package must not choose a mapping unilaterally. Acceptable future approaches include:

- keep review state as a separate field/obligation while returning a finite public outcome;
- define an explicit resolver-result contract with `NEEDS_REVIEW` and a reviewed mapping;
- reject the profile as unsupported until a governing decision exists.

### Result contract requirements

Before public exports are admitted, a result profile must define:

- finite state enum;
- reason-code vocabulary;
- issue structure;
- resolved bundle reference behavior;
- original EvidenceRef preservation;
- profile/version/hash fields;
- lookup/supersession trace fields;
- policy/release/correction handoff fields;
- safe serialization rules;
- compatibility rules.

[Back to top](#top)

---

## Accepted inputs

Package functions should accept explicit data, not ambient authority.

| Input family | Accepted candidate content | Required handling |
|---|---|---|
| Resolver profile | object/schema versions, identifiers, hashes, mapping policy | Required for profile-sensitive behavior; reject unknown profiles. |
| EvidenceRef | current-profile object or explicitly versioned alternate profile | Validate and preserve original values. |
| Lookup snapshot | found/not-found state, candidate bundle, registry version, lookup time, source, traversal trace | Caller supplied; never presented as package-owned registry truth. |
| EvidenceBundle | current-profile candidate or explicitly versioned alternate profile | Validate against selected schema before local checks. |
| Claim context | accepted structured object or explicit comparison policy | Do not infer unsupported structure from free-form text. |
| Integrity context | checksums, spec hash, canonicalization profile, expected digests | Compare only under compatible algorithms/profiles. |
| Rights/sensitivity context | explicit labels, refs, obligations, policy decision refs | Preserve; do not evaluate policy. |
| Release/correction context | release ref/state, rollback ref, correction/supersession refs | Preserve; do not approve or mutate release state. |
| Trace context | request id, run id, resolver version, schema ids/hashes, input digest | Return receipt-ready data for callers to persist. |
| Fixture context | synthetic/public-safe objects and expected issues | Keep clearly fixture-only and deterministic. |

### Input rejection rules

Reject or return explicit invalid/unsupported issues when:

- the profile is absent for ambiguous shapes;
- schema/profile version is unknown;
- required fields are missing;
- undeclared fields indicate profile mismatch;
- hash notation or canonicalization is incompatible;
- lookup snapshot provenance is absent where required;
- a supersession traversal is incomplete or cyclic;
- required policy/release/correction context is absent for the requested operation;
- sensitive or private material is supplied to an API not designed to hold it.

[Back to top](#top)

---

## Permitted outputs

A package helper may return candidate values only.

| Output family | Permitted content | Required qualifier |
|---|---|---|
| Validation result | valid/invalid plus deterministic issues | Shape/local check only; not closure or policy. |
| Resolver candidate | local state, reason codes, original ref, candidate bundle ref, issues | Not a public runtime answer. |
| Comparison result | equal/mismatch/unsupported for explicit profile-defined values | Not proof of source authority or freshness. |
| Supersession trace candidate | visited ids/refs, traversal state, cycle/stale issues | Caller-supplied registry snapshot only. |
| Receipt candidate | input/output digests, versions, profile ids, issues, timing metadata | Caller persists in receipt home. |
| Generated adapter metadata | source schema id/hash, generator, command, output digest | Must not redefine semantics. |
| Compatibility result | converted object plus warnings/loss report | Only for accepted source/target profiles. |

### Outputs that are forbidden

The package must not directly return or persist:

- public claim prose;
- authoritative evidence closure declarations detached from governed proof records;
- policy allow/deny decisions;
- release approvals;
- promotion receipts;
- materialized EvidenceBundles in proof storage;
- lifecycle state transitions;
- public API response envelopes unless that responsibility is explicitly accepted elsewhere;
- unredacted restricted evidence;
- fabricated citations or refs;
- hidden fallback content.

[Back to top](#top)

---

## Consumer and public-interface boundary

### Potential internal consumers

Future governed consumers may include:

- governed API assemblers;
- runtime envelope builders;
- citation/evidence validation tools;
- release preflight tools;
- Evidence Drawer projection services;
- Focus Mode evidence support;
- domain packages that need local candidate checks;
- correction and rollback analysis tools;
- test and fixture harnesses.

These are **PROPOSED consumer classes**, not verified imports.

### Consumer obligations

A consumer must:

- select an accepted resolver profile;
- supply governed lookup/proof context;
- preserve original EvidenceRef values;
- honor all local issues and unsupported states;
- perform policy, rights, sensitivity, citation, release, freshness, correction, and runtime-envelope gates outside this package;
- persist receipts/proofs in owning roots;
- avoid exposing package internals to public clients;
- pin package and profile versions in reproducible workflows.

### Public-client rule

```text
Public client
  -> governed API/runtime
  -> policy/release/evidence gates
  -> package helper as internal implementation detail

Public client
  -X-> packages/evidence-resolver
  -X-> bundle registry
  -X-> data/proofs
  -X-> RAW / WORK / QUARANTINE
```

No UI, browser client, external integration, or model-facing prompt should import this package as its truth source.

[Back to top](#top)

---

## Dependency direction

The intended dependency direction is inward toward narrow value/validation helpers and outward through caller-supplied interfaces.

```text
accepted contracts/schemas
          |
          v
packages/evidence or generated schema adapters
          |
          v
packages/evidence-resolver pure candidate core
          ^
          |
caller-supplied lookup snapshots / ports
          |
          v
governed runtime, API, validators, release preflight
```

### Allowed dependency classes

Subject to explicit packaging metadata and review:

- standard-library immutable/value utilities;
- accepted common/evidence value-object helpers;
- generated schema adapters tied to accepted schema profiles;
- narrow validation libraries declared in package metadata;
- typed protocol/port interfaces for caller-supplied lookups;
- deterministic hashing helpers tied to an accepted canonicalization profile.

### Disallowed dependency direction

The pure package core must not import:

- source connectors;
- lifecycle data repositories;
- proof or receipt stores;
- release writers;
- policy engines as hidden globals;
- API routers;
- UI components;
- model providers;
- deployment/infra code;
- secret managers;
- ambient application state.

### Cycle prevention

- `packages/evidence-resolver` may depend on a narrow accepted `packages/evidence` primitive surface.
- `packages/evidence` should not depend back on the resolver package.
- Runtime/app layers may depend on this package; this package must not depend on runtime/app layers.
- Generated adapters may depend on schemas at generation time but should not read arbitrary repository paths at import time.

[Back to top](#top)

---

## Identity, hashing, time, and supersession

### Hash profile

The package must distinguish:

- the current SpecHash object shape;
- checksum strings inside EvidenceBundle;
- architecture-level JCS+SHA-256 notation;
- hashes of schemas, profiles, inputs, outputs, and package artifacts.

A hash comparison is meaningful only when algorithm, encoding, canonicalization, and semantic target are compatible.

### Required hash handling

- preserve algorithm prefixes;
- reject uppercase or malformed values where the selected profile forbids them;
- never strip `jcs:` or other prefixes to force equality;
- never hash developer-formatted JSON and call it canonical without an accepted procedure;
- include profile/canonicalization identity in receipt candidates;
- distinguish bundle checksum mismatch from spec-hash mismatch;
- avoid comparing hashes that name different semantic surfaces.

### Time handling

Future resolver inputs/results should distinguish:

- lookup time;
- evidence observation/source time;
- bundle creation time;
- validation time;
- policy evaluation time;
- release time;
- correction/supersession time;
- package execution time.

The package must not invent freshness from execution time alone.

### Supersession handling

A future supersession adapter should:

- accept an explicit registry snapshot or port;
- preserve the originally requested ref/bundle;
- record every visited bundle id/ref;
- detect loops and depth limits;
- identify the selected head and the rule used;
- preserve correction/rollback markers;
- fail closed on ambiguous branches, missing heads, or incompatible profiles;
- return a trace candidate for callers to receipt.

Following a supersession link does not itself make the selected head released, policy-safe, or claim-scope adequate.

[Back to top](#top)

---

## Lifecycle, policy, release, and public safety

The package sits downstream of governed evidence preparation and upstream of final public response assembly.

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

It must not move data between phases or treat a file path as lifecycle state.

### Evidence boundary

- EvidenceRef is a pointer, not closure.
- EvidenceBundle is claim-scope closure support, not policy/release approval.
- Schema validity is necessary but not sufficient.
- Source records, citations, rights, sensitivity, transforms, checksums, and spec identity must remain visible.
- Generated summaries, maps, tiles, graphs, indexes, and vectors remain derived artifacts, not sovereign truth.

### Policy boundary

The package may preserve policy context supplied by callers, but it must not:

- infer policy allowance from sensitivity labels;
- convert unknown rights into allowed use;
- downgrade deny/restrict/hold obligations;
- expose sensitive policy reasons to public callers;
- fabricate PolicyDecision refs;
- bypass audience or purpose constraints.

### Release boundary

The package may carry release/correction refs, but it must not:

- approve publication;
- mark an object PUBLISHED;
- create ReleaseManifest or RollbackCard authority;
- select a release merely because a bundle validates;
- ignore withdrawal, correction, or supersession state;
- mutate release records.

### Cite-or-abstain posture

When material support cannot be resolved unambiguously, downstream callers should receive an abstain-ready or error-ready candidate, never plausible filler.

[Back to top](#top)

---

## Failure and error semantics

Failures must be finite, typed, and inspectable.

### Candidate issue families

| Family | Examples | Default posture |
|---|---|---|
| `profile/*` | missing profile, unsupported version, incompatible mapping | fail closed |
| `schema/*` | invalid EvidenceRef, invalid EvidenceBundle, undeclared fields | fail closed |
| `evidence/*` | ref not found, bundle missing, bundle_ref mismatch | unresolved/abstain-ready |
| `scope/*` | scope absent, mismatch, unverifiable structured context | unresolved/abstain-ready |
| `integrity/*` | checksum mismatch, spec-hash mismatch, incompatible canonicalization | error or unresolved per accepted contract |
| `registry/*` | snapshot missing, lookup failed, supersession cycle, ambiguous head | error/unresolved |
| `rights/*` | rights absent, unknown, restricted | policy handoff; no public answer |
| `sensitivity/*` | sensitivity absent or exposure blocked | policy handoff; no public answer |
| `release/*` | unreleased, withdrawn, superseded, rollback-affected | no public answer |
| `correction/*` | corrected ref, invalidated bundle, stale dependent result | no public answer |
| `internal/*` | invariant violation, unsupported adapter, unexpected exception | error-ready, sanitized |

### Fail-closed rules

- Unknown profile is not “best effort.”
- Missing lookup result is not an empty bundle.
- Missing EvidenceRef validator is not validator success.
- Unknown rights are not public rights.
- Missing release context is not release approval.
- Unsupported `NEEDS_REVIEW` mapping is not silent `ANSWER`.
- Hash mismatch is not warning-only when integrity is required.
- Supersession ambiguity is not permission to choose the newest timestamp.
- Exceptions must not trigger uncited fallback text.

### Exception boundary

Internal exceptions should be converted into deterministic, sanitized issue/result carriers at the package boundary. Do not leak stack traces, filesystem paths, secrets, raw records, or restricted context to public surfaces.

[Back to top](#top)

---

## Security, privacy, and data minimization

### No-network default

The pure package core should perform no network access. Registry/proof access should be supplied through explicit ports or snapshots owned by callers.

### Import-time safety

Importing the package must not:

- read environment variables for operational decisions;
- open files or databases;
- inspect repositories;
- initialize network clients;
- load credentials;
- contact registries;
- mutate global state;
- emit logs containing evidence;
- register background tasks;
- execute schema generation.

### Data minimization

Package inputs and outputs should carry only what local checks require. Prefer refs, ids, hashes, labels, and bounded issue context over full raw records.

### Sensitive content

The package and its fixtures must not contain:

- secrets or credentials;
- private raw source payloads;
- precise restricted locations;
- living-person sensitive data;
- genomic/DNA records;
- culturally restricted material;
- unrestricted infrastructure exposure;
- hidden chain-of-thought;
- raw model-provider payloads.

### Logging and observability

Future observability should record:

- operation name;
- package/profile version;
- request/run ids;
- object ids/refs where policy-safe;
- issue codes;
- duration and success/failure;
- input/output digests where appropriate.

It should not record full evidence payloads, secret headers, restricted citations, or sensitive policy reasons by default.

[Back to top](#top)

---

## Packaging, distribution, and versioning

Current `pyproject.toml` establishes only:

```toml
[project]
name = "kfm-evidence-resolver"
version = "0.0.0"
```

It does not currently establish:

- build backend;
- Python version range;
- dependencies;
- package discovery;
- license;
- authors/maintainers;
- classifiers;
- entry points;
- optional dependency groups;
- typed-package marker inclusion;
- package data;
- registry publication.

### Admission requirements for buildable distribution

Before claiming installability:

1. select and configure a build backend;
2. set supported Python versions;
3. configure `src`-layout package discovery;
4. declare runtime and optional dependencies;
5. define license and maintainers;
6. decide whether `py.typed` is supported;
7. verify wheel and sdist contents;
8. run clean-environment install/import tests;
9. publish only through an accepted registry/release process;
10. record artifact digests and rollback instructions.

### Versioning posture

- `0.0.0` is a scaffold marker, not a compatibility promise.
- The first supported export requires a deliberate version decision.
- Breaking contract/schema/profile changes require package compatibility review.
- Package version and resolver-profile version are separate axes and should both be recorded.
- Generated adapters must identify source schema/profile versions independently of package version.
- Deprecations require documented replacement, timeline, tests, and rollback.

### Package release is not data release

Publishing a Python wheel does not publish EvidenceBundles, claims, maps, or KFM lifecycle data. Code distribution and knowledge publication remain separate governed transitions.

[Back to top](#top)

---

## Tests, fixtures, validators, and CI

### Confirmed current surfaces

| Surface | Status | Limit |
|---|---:|---|
| EvidenceRef schema fixtures | one valid and one invalid case documented | narrow schema coverage |
| EvidenceBundle schema fixtures | one valid and one invalid case documented | narrow schema coverage |
| Generic schema harness | evidence family included | schema fixtures, not resolver behavior |
| EvidenceBundle validator wrapper | exists | presence does not prove current run or package integration |
| EvidenceRef validator wrapper | declared by schema but absent | metadata/file conflict |
| Package-specific tests | not established | no resolver behavior proof |
| Package-specific fixtures | not established | no adapter/lookup/supersession proof |
| Evidence-resolver workflow | two jobs exist | both execute `echo TODO` only |

### Required package test matrix

A future implementation should test:

- import without side effects;
- empty/minimal initializer policy;
- explicit supported exports;
- unknown profile rejection;
- valid and invalid EvidenceRef objects;
- valid and invalid EvidenceBundle objects;
- missing `bundle_ref` and missing bundle cases;
- bundle_ref/bundle_id mismatch;
- malformed and incompatible hashes;
- canonicalization-profile mismatch;
- empty or unverifiable claim scope;
- structured scope match/mismatch when a contract exists;
- registry lookup not-found/error;
- supersession single-hop/multi-hop/cycle/ambiguous-head cases;
- rights/sensitivity/release context absence;
- correction/rollback invalidation;
- issue determinism and stable ordering;
- serialization safety;
- no-network behavior;
- no secret/sensitive fixture content;
- compatibility adapter loss reporting;
- clean wheel/sdist install and import;
- supported Python versions.

### Workflow truth posture

A green `evidence-resolver` workflow currently means only that these commands ran successfully:

```text
echo TODO resolve-bundles
echo TODO denied-bundles-fail-closed
```

Do not describe that workflow as resolver validation, bundle resolution, fail-closed enforcement, or production readiness until the jobs execute real tests with inspectable fixtures and assertions.

### Test placement question

Package unit/property tests may belong under an accepted package-test lane, while contract-schema fixtures remain under `fixtures/contracts/v1/evidence/`. The canonical split is unresolved and should be decided before parallel fixture homes appear.

[Back to top](#top)

---

## Implementation admission sequence

Use the smallest reversible sequence that proves each new layer before expanding it.

### Stage 0 — governance and profile decision

- assign owners;
- accept or explicitly version EvidenceRef/EvidenceBundle profiles;
- decide SpecHash/canonicalization profile;
- define resolver-result and reason-code contracts;
- decide `NEEDS_REVIEW` mapping;
- decide registry/supersession input contract;
- decide `packages/evidence` dependency direction;
- decide package test/fixture placement.

### Stage 1 — packaging baseline

- configure build backend and `src` discovery;
- set Python requirement and dependencies;
- add clean install/import tests;
- keep initializer minimal;
- publish no registry artifact yet.

### Stage 2 — value/profile adapters

- add explicit profile identifiers;
- add generated or hand-written schema adapters with provenance;
- validate current EvidenceRef and EvidenceBundle shapes;
- add deterministic issue carriers;
- add package tests.

### Stage 3 — pure resolution candidate core

- accept EvidenceRef, lookup snapshot, candidate bundle, and profile;
- check local identity/profile consistency;
- return a typed candidate result;
- add negative-path and property tests;
- preserve no-network behavior.

### Stage 4 — registry/supersession port

- define a typed port outside the pure core;
- implement one caller-owned adapter;
- add traversal receipts and cycle protection;
- do not hide I/O inside imports or global state.

### Stage 5 — governed consumer integration

- integrate one internal consumer;
- pin package/profile versions;
- perform policy/citation/release/envelope gates outside the package;
- produce receipts and rollback instructions;
- verify no public bypass path.

### Stage 6 — package release

- build reproducible artifacts;
- verify contents and hashes;
- publish through accepted release controls;
- document compatibility, correction, and rollback;
- retain previous artifact for rollback.

Each stage should be independently reviewable and reversible. Do not jump from README scaffold to a broad resolver framework.

[Back to top](#top)

---

## Compatibility, correction, and rollback

### Compatibility posture

Compatibility is explicit, not inferred.

A compatibility adapter must identify:

- source profile/version/hash;
- target profile/version/hash;
- field mapping;
- defaults introduced;
- information lost;
- unsupported cases;
- issue/warning behavior;
- tests;
- deprecation timeline;
- rollback target.

Adapters must fail when conversion would invent authority, evidence, policy, release, scope, or integrity context.

### Correction invalidation

When an EvidenceRef, EvidenceBundle, schema, policy, release, or registry head is corrected or withdrawn, affected package results should be treated as cacheable candidates that may require invalidation. The package should not own invalidation authority, but future result carriers should preserve enough identity to let callers find affected outputs.

Useful future fields may include:

- original ref;
- resolved bundle id/ref;
- profile ids/hashes;
- lookup snapshot/version;
- supersession head;
- release/correction refs;
- input/output digests;
- execution time;
- package version.

### Rollback triggers

Rollback package changes if they:

- create parallel semantic/schema/policy authority;
- introduce registry/proof storage into package source;
- read lifecycle stores or connectors directly;
- silently translate incompatible profiles;
- fabricate missing evidence, hashes, scope, policy, or release context;
- expose package internals to public clients;
- add import-time I/O or secrets;
- claim workflow/test coverage not actually present;
- break supported consumers without a migration;
- publish an artifact without reproducible provenance.

### Current documentation rollback

For this README-only change:

- before merge, close or abandon the PR;
- after merge, create a transparent revert restoring the prior blob;
- no code, schema, contract, policy, fixture, test, proof, receipt, release, deployment, or package-registry rollback is required.

[Back to top](#top)

---

## Definition of done

This package README is complete for the current evidence boundary when it:

- accurately records the `kfm-evidence-resolver` `0.0.0` scaffold;
- links the merged source-root and module v0.2 contracts;
- distinguishes package, source-root, and module responsibilities;
- records the empty initializer and absent selected resolver modules;
- records unknown build, dependency, discovery, export, consumer, and publication behavior;
- grounds current EvidenceRef, EvidenceBundle, and SpecHash profiles;
- surfaces architecture/schema, hash, scope, outcome, sibling-package, validator, and test-placement conflicts;
- preserves cite-or-abstain and fail-closed behavior;
- keeps registry, proof, policy, release, lifecycle, receipt, API, UI, and AI authority outside the package;
- defines packaging, security, validation, compatibility, correction, and rollback expectations;
- avoids claiming resolver behavior from echo-only CI;
- provides a reversible implementation admission path;
- includes an evidence ledger and verification register.

### Implementation definition of done

The package itself is not implementation-complete until:

- profiles and owners are accepted;
- build/install metadata is complete;
- supported exports exist;
- unit/property/negative tests pass;
- EvidenceRef validator metadata/file conflict is resolved;
- resolver workflow executes real tests;
- at least one governed consumer is verified;
- no public bypass exists;
- package artifacts are reproducible and receipted;
- correction and rollback are exercised.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status | Required evidence |
|---|---|---|---|
| `ER-PKG-001` | Who owns this package? | NEEDS VERIFICATION | CODEOWNERS/owner assignment |
| `ER-PKG-002` | What build backend is accepted? | NEEDS VERIFICATION | `pyproject.toml` build-system plus build test |
| `ER-PKG-003` | Which Python versions are supported? | NEEDS VERIFICATION | `requires-python` plus CI matrix |
| `ER-PKG-004` | What runtime dependencies are allowed? | NEEDS VERIFICATION | dependency declaration and review |
| `ER-PKG-005` | How is `src` package discovery configured? | NEEDS VERIFICATION | build config and wheel-content test |
| `ER-PKG-006` | Which exports are public and stable? | NEEDS VERIFICATION | implemented modules, initializer, API docs, tests |
| `ER-PKG-007` | Which internal consumers import the package? | NEEDS VERIFICATION | indexed imports and integration tests |
| `ER-PKG-008` | What is the accepted EvidenceRef profile? | NEEDS VERIFICATION | accepted contract/schema/version/hash |
| `ER-PKG-009` | What is the accepted EvidenceBundle profile? | NEEDS VERIFICATION | accepted contract/schema/version/hash |
| `ER-PKG-010` | What is the accepted SpecHash/canonicalization profile? | NEEDS VERIFICATION | contract/standard/tool tests |
| `ER-PKG-011` | What is the resolver-result contract? | NEEDS VERIFICATION | contract, schema, fixtures, validator |
| `ER-PKG-012` | What are the canonical reason codes? | NEEDS VERIFICATION | governed vocabulary and tests |
| `ER-PKG-013` | How is `NEEDS_REVIEW` represented or mapped? | CONFLICTED | accepted ADR/contract mapping |
| `ER-PKG-014` | What structured claim-scope contract supports field/time/space checks? | CONFLICTED | accepted schema and fixtures |
| `ER-PKG-015` | What is the registry lookup/snapshot contract? | NEEDS VERIFICATION | typed port/contract and fixtures |
| `ER-PKG-016` | What are supersession traversal rules? | NEEDS VERIFICATION | registry contract, cycle/depth tests |
| `ER-PKG-017` | How are rights/sensitivity/policy handoffs represented? | NEEDS VERIFICATION | accepted input/result contracts |
| `ER-PKG-018` | How are release/correction/rollback refs represented? | NEEDS VERIFICATION | accepted contracts and integration tests |
| `ER-PKG-019` | Why is the EvidenceRef validator declared but absent? | CONFLICTED | implement wrapper or correct schema metadata |
| `ER-PKG-020` | Where do package unit/property tests live? | NEEDS VERIFICATION | accepted directory/test convention |
| `ER-PKG-021` | Where do package-specific lookup/supersession fixtures live? | NEEDS VERIFICATION | accepted fixture convention |
| `ER-PKG-022` | Should this package depend on `packages/evidence`? | CONFLICTED | ADR/import direction decision |
| `ER-PKG-023` | When will resolver CI run real behavior tests? | NEEDS VERIFICATION | workflow patch and passing assertions |
| `ER-PKG-024` | Is the package published to a registry? | UNKNOWN | package artifact and release record |
| `ER-PKG-025` | How are package artifacts signed/hashed/receipted? | NEEDS VERIFICATION | release workflow and artifact evidence |
| `ER-PKG-026` | Has rollback been exercised with a real consumer? | UNKNOWN | rollback drill and readback |

[Back to top](#top)

---

## Evidence ledger

| Evidence source | Status | Supports | Does not prove |
|---|---|---|---|
| Current target README, prior blob `8a6aa41745dcdef75a3b48110b3ff963e10751c7` | **CONFIRMED** | Prior package intent and anti-authority posture. | Implementation maturity or current layout detail. |
| [`pyproject.toml`](./pyproject.toml) | **CONFIRMED** | Distribution name `kfm-evidence-resolver`, version `0.0.0`. | Build backend, dependencies, installability, publication. |
| [`src/README.md`](./src/README.md), blob `ec71b65875731ca3cbfca6a29839172b52b48418` | **CONFIRMED** | Source-root structure, packaging, import, generated-code, testing, and conflict posture. | Executable resolver behavior. |
| [`src/evidence_resolver/README.md`](./src/evidence_resolver/README.md), blob `62dd6340557b9ea2076ee8d5b0c579149ab06bc0` | **CONFIRMED** | Module semantics, profile conflicts, inputs/outputs, failures, security, implementation sequence. | Implemented modules, exports, consumers, runtime behavior. |
| Empty `src/evidence_resolver/__init__.py` | **CONFIRMED** | Namespace marker exists and exports are not established. | Supported API. |
| Bounded absent module checks | **CONFIRMED bounded absence** | Selected resolver modules were not present at tested paths. | Absence of every possible implementation file. |
| EvidenceRef contract/schema | **CONFIRMED surfaces / `PROPOSED`** | Current closed field shape and pointer boundary. | Registry existence, closure, policy, release, runtime behavior. |
| EvidenceBundle contract/schema | **CONFIRMED surfaces / `PROPOSED`** | Current closed field shape and claim-scope closure boundary. | Adequacy, authority, policy, release, storage, runtime behavior. |
| SpecHash contract/schema | **CONFIRMED surfaces / `PROPOSED`** | Current `{ value: sha256:<hex> }` shape. | Canonicalization equivalence with architecture notation. |
| Evidence fixture READMEs and generic schema harness | **CONFIRMED minimal** | One valid/invalid schema case per object and evidence-family discovery. | Resolver, registry, policy, release, or package behavior. |
| EvidenceBundle validator wrapper | **CONFIRMED file** | Dedicated bundle schema entry point exists. | Current execution or package integration. |
| Missing EvidenceRef validator path | **CONFIRMED conflict** | Schema metadata and file state disagree. | Intended resolution of the conflict. |
| Evidence-resolver workflow | **CONFIRMED echo-only scaffold** | Workflow triggers and job names exist. | Resolution or fail-closed behavior. |
| Directory Rules v1.4 | **CONFIRMED doctrine** | `packages/` owns shared libraries; authority/data/test/runtime roots remain separate. | Package implementation maturity. |
| Current branch preparation and validation | **CONFIRMED in this task** | One-file documentation update, local validation, remote blob readback. | Merge, runtime deployment, package publication, or production behavior. |

### Truth summary

```text
CONFIRMED
- package path and prior README
- kfm-evidence-resolver 0.0.0 metadata
- Python src root and evidence_resolver namespace
- merged source-root and module v0.2 contracts
- empty initializer
- selected resolver modules absent at tested paths
- current EvidenceRef/EvidenceBundle/SpecHash schema surfaces
- minimal contract fixtures and generic schema harness
- EvidenceBundle validator present
- EvidenceRef validator declared but absent
- resolver workflow exists and is echo-only

PROPOSED
- supported resolver package API
- profile adapters and generated adapters
- lookup/supersession ports
- deterministic candidate result types
- package tests and fixtures
- governed consumers
- package registry publication

CONFLICTED
- architecture object shapes versus paired schemas
- JCS-prefixed hash notation versus current SpecHash shape
- resolver-local/public outcome vocabularies and NEEDS_REVIEW
- structured scope ambitions versus free-form claim_scope
- packages/evidence versus evidence-resolver responsibility split
- package-specific versus contract-schema test/fixture placement
- EvidenceRef validator metadata versus file state

UNKNOWN
- build/install behavior
- supported Python versions and dependencies
- public exports and production consumers
- registry/proof adapter implementation
- runtime/API integration
- package publication
- production resolution behavior
- release integration
```

[Back to top](#top)

---

## Maintainer summary

Keep this package small, deterministic, and subordinate to governed evidence, policy, release, and public-interface systems.

The next useful change is not a broad resolver framework. It is a reviewed profile and packaging decision, followed by the smallest pure candidate checker with real negative-path tests. Until then, this package remains a documented `0.0.0` scaffold.
