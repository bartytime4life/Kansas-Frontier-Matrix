<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-evidence-resolver-src-readme
title: packages/evidence-resolver/src/ — Governed Evidence Resolver Package Source Root
type: readme
version: v0.2
status: draft; repository-grounded; python-src-root; implementation-placeholder; non-authoritative
owners:
  - OWNER_TBD — Evidence resolver package owner
  - OWNER_TBD — Evidence and proof steward
  - OWNER_TBD — Contract and schema steward
  - OWNER_TBD — Policy, rights, and sensitivity steward
  - OWNER_TBD — Runtime and governed API steward
  - OWNER_TBD — Release, correction, validator, security, packaging, and docs steward
created: NEEDS VERIFICATION — target file existed before this revision
updated: 2026-07-15
supersedes: v1 planning-oriented source-directory guide (2026-06-14)
policy_label: public; packages; evidence-resolver; python; src-layout; evidenceref; evidencebundle; closure-validation; no-network-by-default; cite-or-abstain; fail-closed; non-authoritative
path: packages/evidence-resolver/src/README.md
truth_posture: CONFIRMED target and prior blob, kfm-evidence-resolver 0.0.0 project metadata, Python src layout, evidence_resolver import package, empty initializer, merged child-module v0.2 contract, bounded absence of selected resolver modules and package.json, parent package README, sibling packages/evidence boundary, fielded closed EvidenceRef and EvidenceBundle schemas, paired draft contracts, minimal fixture families, generic schema harness, existing EvidenceBundle validator, missing schema-declared EvidenceRef validator, echo-only evidence-resolver workflow, Directory Rules v1.4, and current common SpecHash contract/schema / PROPOSED future package discovery, deliberate exports, pure resolver candidate helpers, generated schema adapters, lookup-snapshot adapters, compatibility adapters, package tests, and typed marker / CONFLICTED architecture EvidenceRef and EvidenceBundle shapes versus current paired schemas, JCS-prefixed architecture hash notation versus current SpecHash shape, resolver-local outcomes versus runtime outcomes and NEEDS_REVIEW, strong structured scope checks versus current free-form claim_scope, evidence-resolver versus packages/evidence responsibility overlap, and package-specific versus contract-schema test/fixture placement / UNKNOWN build backend, Python requirement, dependencies, package discovery, license metadata, public exports, import consumers, resolver input/result contracts, registry adapter, package-specific CI, runtime/API wiring, package publication, release integration, and production behavior / NEEDS VERIFICATION accepted owners, canonical resolver profiles and outcomes, registry and supersession contracts, canonicalization profile, reason-code vocabulary, policy handoff, correction invalidation, and rollback integration
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 3b2cb50acf90c9ee5f0f082aec5d1e04601a3b9b
  prior_blob: f1770cffc315004305f3b300601d8ec2914a35c6
  child_module_blob: 62dd6340557b9ea2076ee8d5b0c579149ab06bc0
related:
  - ./evidence_resolver/README.md
  - ./evidence_resolver/__init__.py
  - ../README.md
  - ../pyproject.toml
  - ../../README.md
  - ../../evidence/README.md
  - ../../../contracts/evidence/evidence_ref.md
  - ../../../contracts/evidence/evidence_bundle.md
  - ../../../contracts/common/spec_hash.md
  - ../../../schemas/contracts/v1/evidence/evidence_ref.schema.json
  - ../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json
  - ../../../schemas/contracts/v1/common/spec_hash.schema.json
  - ../../../fixtures/contracts/v1/evidence/evidence_ref/README.md
  - ../../../fixtures/contracts/v1/evidence/evidence_bundle/README.md
  - ../../../tools/validators/validate_evidence_bundle.py
  - ../../../tests/schemas/test_common_contracts.py
  - ../../../docs/architecture/evidence-identity.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../.github/workflows/evidence-resolver.yml
tags: [kfm, packages, evidence-resolver, python, src-layout, source-root, import-boundary, EvidenceRef, EvidenceBundle, closure, resolver-profile, generated-code, deterministic, no-network, fail-closed, cite-or-abstain, rollback]
notes:
  - "v0.2 replaces stale planning language with a commit-pinned description of the current kfm-evidence-resolver 0.0.0 Python src-layout scaffold."
  - "The merged evidence_resolver/README.md v0.2 owns resolver candidate semantics; this file owns source-root, discovery, import, dependency, generated-code, packaging, test-placement, and compatibility boundaries."
  - "The import package initializer is empty and selected resolver modules are absent; no supported API, build behavior, consumer, registry adapter, or runtime integration is claimed."
  - "Architecture prose, paired schemas, hash notation, scope semantics, and resolver outcome vocabularies conflict; the source root requires explicit profiles and forbids silent normalization."
  - "Only this Markdown file changes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Evidence Resolver Package Source Root

`packages/evidence-resolver/src/`

> Python `src`-layout container for the `kfm-evidence-resolver` shared package. This directory may organize reusable, deterministic evidence-resolution helper implementation, but it must not become evidence meaning, schema authority, registry or proof storage, policy execution, lifecycle access, receipt persistence, release authority, runtime orchestration, public API routing, UI rendering, or generated truth.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.2-informational)
![distribution](https://img.shields.io/badge/distribution-kfm--evidence--resolver-3776ab)
![layout](https://img.shields.io/badge/layout-Python%20src--layout-3776ab)
![implementation](https://img.shields.io/badge/implementation-placeholder-lightgrey)
![boundary](https://img.shields.io/badge/boundary-EvidenceRef%E2%86%92EvidenceBundle-6f42c1)
![network](https://img.shields.io/badge/network-none%20by%20default-455a64)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-0b7285)

**Quick links:** [Purpose](#purpose-and-audience) · [Status](#current-repository-state) · [Context](#source-root-bounded-context) · [Placement](#placement-and-authority) · [Surface](#current-source-tree) · [Root/module split](#source-root-versus-import-module) · [Sibling package](#relationship-to-packagesevidence) · [Packaging](#packaging-and-discovery-boundary) · [Imports](#import-and-export-contract) · [Import safety](#import-time-safety) · [Dependencies](#dependency-direction) · [Profiles](#resolver-profile-and-drift-boundary) · [Generated code](#generated-code-and-schema-adapters) · [Inputs](#source-root-input-and-output-boundary) · [Trust](#lifecycle-evidence-policy-release-and-public-safety) · [Tests](#tests-fixtures-validators-and-ci) · [Security](#security-and-observability) · [Evolution](#proposed-source-tree-evolution) · [Compatibility](#compatibility-correction-and-rollback) · [Validation](#validation-commands) · [Done](#definition-of-done) · [Backlog](#open-verification-register) · [Ledger](#evidence-ledger)

> [!IMPORTANT]
> **Repository snapshot:** `main@3b2cb50acf90c9ee5f0f082aec5d1e04601a3b9b`<br>
> **Distribution:** `kfm-evidence-resolver`<br>
> **Declared version:** `0.0.0`<br>
> **Verified source root:** `src/`<br>
> **Verified import package:** `src/evidence_resolver/`<br>
> **Verified implementation:** empty `evidence_resolver/__init__.py`; selected resolver modules are absent<br>
> **Verified child contract:** [`evidence_resolver/README.md`](./evidence_resolver/README.md) v0.2<br>
> **Build backend, Python requirement, dependencies, package discovery, exports, consumers, and package publication:** not established<br>
> **Evidence schemas/contracts:** present but `PROPOSED`, with documented architecture/schema, hash, scope, and outcome drift<br>
> **Resolver workflow:** present, but both jobs are `echo TODO` scaffolds

> [!CAUTION]
> Source layout does not confer authority. A package can validate an explicit lookup snapshot without owning the registry. A schema adapter can validate shape without proving closure. A `RESOLVED` candidate is not policy clearance, release approval, or a public answer.

---

## Purpose and audience

`packages/evidence-resolver/src/` is the implementation container for the Python project declared by [`../pyproject.toml`](../pyproject.toml).

Its durable responsibilities are structural:

- contain importable source for the `evidence_resolver` package;
- make package discovery and import boundaries explicit;
- provide a stable home for reusable, no-network resolver helper code;
- keep exports deliberate, small, versioned, and reviewable;
- keep import-time behavior deterministic and side-effect-free;
- preserve explicit resolver profiles, evidence refs, bundle refs, hashes, rights, sensitivity, correction, release, and policy context supplied by callers;
- keep generated adapters subordinate to accepted contracts and schemas;
- keep implementation separate from registries, proof stores, source connectors, lifecycle data, policy engines, receipt stores, release systems, API routes, UI surfaces, and model providers;
- support deterministic, synthetic, public-safe tests without storing production evidence in source.

This README is for package maintainers, evidence/proof stewards, contract/schema/policy/release reviewers, runtime and governed API authors, validator and test maintainers, packaging/security reviewers, and maintainers deciding whether proposed code belongs in this source root.

Detailed resolver candidate semantics belong in [`evidence_resolver/README.md`](./evidence_resolver/README.md). This source-root README governs the container, discovery, import surface, dependency direction, generated-code boundary, test placement, packaging posture, compatibility, and enforceability placement.

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
| Base commit | `3b2cb50acf90c9ee5f0f082aec5d1e04601a3b9b` |
| Prior target blob | `f1770cffc315004305f3b300601d8ec2914a35c6` |
| Child module blob | `62dd6340557b9ea2076ee8d5b0c579149ab06bc0` |
| Current revision | documentation-only v0.2 proposal |

### Verified source-root surface

| Surface | Evidence at snapshot | Status | Consequence |
|---|---|---:|---|
| This README | Existing v1 planning-oriented source guide. | **CONFIRMED** | Revised in place. |
| [`../pyproject.toml`](../pyproject.toml) | Declares `[project]`, name `kfm-evidence-resolver`, and version `0.0.0` only. | **CONFIRMED minimal placeholder** | Distribution identity is known; build and dependency behavior are not. |
| [`evidence_resolver/README.md`](./evidence_resolver/README.md) | Merged repository-grounded source-module contract v0.2. | **CONFIRMED** | Detailed resolver semantics and conflict posture live there. |
| `evidence_resolver/__init__.py` | Exists and is empty. | **CONFIRMED** | Import-package marker only; no public exports are established. |
| `package.json` | Absent at `packages/evidence-resolver/package.json` during the bounded package check. | **CONFIRMED bounded absence** | Do not claim a JavaScript/TypeScript package. |
| Selected helper files | `outcomes.py`, `resolver.py`, `closure.py`, and `scope.py` were absent at exact tested paths. | **CONFIRMED bounded absence** | No executable resolver implementation is established. |
| Build backend | No `[build-system]` section was observed. | **NOT OBSERVED** | Build/install behavior remains unknown. |
| Dependencies | No dependency list was observed. | **NOT OBSERVED** | Do not claim `jsonschema`, registry, API, or crypto dependencies. |
| Supported Python versions | No `requires-python` field was observed. | **NOT OBSERVED** | Interpreter support is unknown. |
| Package discovery | No explicit discovery configuration was observed. | **NOT OBSERVED** | Do not claim editable install or wheel inclusion works. |
| Public exports | Empty initializer. | **NOT ESTABLISHED** | No symbol is part of a supported package API. |
| Consumers | Indexed search did not establish production imports of `evidence_resolver`. | **NOT OBSERVED / search-limited** | Do not claim runtime/API integration. |
| Parent package README | `packages/evidence-resolver/README.md` exists. | **CONFIRMED README / planning-oriented** | Package responsibility is described but implementation maturity is not proven. |
| Sibling package | `packages/evidence/README.md` exists. | **CONFIRMED README** | Ref/digest helper and resolver responsibilities must not collapse silently. |
| EvidenceRef contract/schema | Paired draft contract and fielded closed schema exist. | **CONFIRMED surfaces / `PROPOSED` status** | Source code must bind to an explicit profile. |
| EvidenceBundle contract/schema | Paired draft contract and fielded closed schema exist. | **CONFIRMED surfaces / `PROPOSED` status** | Closure checks must use actual schema fields, not architecture-only fields. |
| SpecHash contract/schema | Current object profile uses `{ "value": "sha256:<hex>" }`. | **CONFIRMED surfaces / `PROPOSED` status** | Architecture `jcs:sha256:` notation cannot be assumed equivalent. |
| EvidenceRef validator | Schema declares `tools/validators/validate_evidence_ref.py`; exact file is absent. | **CONFLICTED metadata / file state** | Source code must not claim dedicated validator availability. |
| EvidenceBundle validator | `tools/validators/validate_evidence_bundle.py` exists. | **CONFIRMED file** | Presence does not prove package behavior. |
| Contract fixtures | One valid and one invalid fixture family are documented for each evidence object. | **CONFIRMED minimal coverage** | Coverage is schema-only and narrow. |
| Generic schema harness | `tests/schemas/test_common_contracts.py` includes the evidence family. | **CONFIRMED test code** | Package-level resolver tests are not established. |
| Package test README | `tests/packages/evidence-resolver/README.md` was absent at the exact tested path. | **CONFIRMED bounded absence** | No package-specific test lane is documented there. |
| Package fixture README | `fixtures/packages/evidence-resolver/README.md` was absent at the exact tested path. | **CONFIRMED bounded absence** | No package-specific fixture lane is documented there. |
| Resolver workflow | `.github/workflows/evidence-resolver.yml` has `resolve-bundles` and `denied-bundles-fail-closed`. | **CONFIRMED echo-only scaffold** | Green workflow status does not prove resolution or fail-closed behavior. |
| Resolver input/result contract | No contract/schema was found at exact tested `evidence_resolution` paths. | **NOT FOUND at tested paths** | A stable source API cannot be declared yet. |
| Runtime/release evidence | No deployed consumer, runtime log, resolver receipt, release artifact, or public response was inspected. | **UNKNOWN** | This README is not implementation or deployment proof. |

```text
Python distribution identity              = CONFIRMED
Python src-layout container                = CONFIRMED
evidence_resolver import package           = CONFIRMED
empty initializer                          = CONFIRMED
implemented resolver modules               = NOT OBSERVED
supported public exports                   = NOT ESTABLISHED
package consumers                          = NOT OBSERVED
build/install behavior                     = UNKNOWN
package-specific tests/fixtures            = NOT ESTABLISHED
EvidenceRef/EvidenceBundle schema surfaces = CONFIRMED, PROPOSED
resolver result contract                   = NOT FOUND at tested paths
resolver workflow                          = CONFIRMED, echo-only
runtime/API behavior                       = UNKNOWN
release behavior                           = UNKNOWN
```

[Back to top](#top)

---

## Source-root bounded context

The source-root bounded context is:

> The organization and admission boundary for importable, reusable evidence-resolution helper implementation.

It includes:

- source-tree structure;
- package discovery;
- import-module placement;
- supported exports;
- dependency direction;
- import-time safety;
- generated-code placement;
- EvidenceRef/EvidenceBundle profile adapter placement;
- lookup-snapshot adapter placement;
- package tests/fixtures integration;
- packaging, distribution, compatibility, and deprecation posture.

It excludes:

- EvidenceRef or EvidenceBundle semantic meaning;
- canonical schema shape;
- evidence registry ownership;
- proof storage;
- source admission;
- policy evaluation;
- lifecycle orchestration;
- receipt persistence;
- release approval;
- correction/withdrawal mutation;
- runtime service orchestration;
- public API serialization;
- Evidence Drawer/UI rendering;
- AI generation or truth determination.

[Back to top](#top)

---

## Placement and authority

Directory Rules place reusable implementation under `packages/`. The existing path is therefore appropriate for an importable shared library **if** a stable cross-consumer need is verified.

```text
packages/evidence-resolver/src/
```

| Concern | Authority here |
|---|---|
| Source-tree organization | **Yes.** This README defines structural expectations. |
| Import package and exports | **Supporting authority**, once implemented and tested. |
| EvidenceRef meaning | **No.** `contracts/evidence/evidence_ref.md`. |
| EvidenceBundle meaning | **No.** `contracts/evidence/evidence_bundle.md`. |
| Machine shape | **No.** `schemas/contracts/v1/evidence/`. |
| Registry lookup truth | **No.** Governed registry/proof systems. |
| Evidence closure records | **No.** Governed EvidenceBundle/proof records. |
| Policy, rights, sensitivity | **No.** Policy systems and decisions. |
| Lifecycle state | **No.** `data/` lifecycle roots. |
| Receipts/proofs | **No.** `data/receipts/` and `data/proofs/`. |
| Release/correction/rollback | **No.** `release/` and governed records. |
| Public interface | **No.** Governed runtime/API applications. |
| UI/map rendering | **No.** UI/application roots. |
| Model calls or generated truth | **No.** Governed AI runtime, evidence-subordinate. |

No new root, parallel schema home, parallel contract home, or hidden registry is proposed.

[Back to top](#top)

---

## Current source tree

The bounded verified source tree is:

```text
packages/evidence-resolver/
├── README.md
├── pyproject.toml
└── src/
    ├── README.md                  # this file
    └── evidence_resolver/
        ├── README.md              # v0.2 module contract
        └── __init__.py            # empty
```

Selected proposed helper files were checked and were absent:

```text
outcomes.py
resolver.py
closure.py
scope.py
```

This is a bounded inventory, not proof that every possible unindexed or empty path is absent.

[Back to top](#top)

---

## Source root versus import module

The two README layers have different responsibilities.

| Layer | Owns | Does not own |
|---|---|---|
| `packages/evidence-resolver/src/README.md` | Source container, discovery, imports, exports, dependency direction, generated code, packaging, tests, compatibility. | Resolver semantics or public outcome decisions. |
| `packages/evidence-resolver/src/evidence_resolver/README.md` | Candidate resolver semantics, object boundaries, explicit profiles, local issues/results, fail-closed behavior. | Package distribution, registry authority, policy, release, public serving. |
| `packages/evidence-resolver/README.md` | Package purpose, consumers, package-level responsibility, sibling-package boundary. | Source-module implementation details. |

Rules:

- do not duplicate a different public API in the source-root README;
- do not let package/source/module docs define conflicting resolver outcomes;
- update all three layers when package-level behavior changes materially;
- treat merged child-module v0.2 as the current detailed implementation proposal;
- keep package/source-root/module claims bounded by actual code and tests.

[Back to top](#top)

---

## Relationship to `packages/evidence`

The sibling boundary is currently documentation-defined and remains partly unresolved.

| Package | Intended lane | Source-root guardrail |
|---|---|---|
| `packages/evidence/` | Reusable EvidenceRef/value/digest/citation/fixture helpers. | Must not become resolver authority or proof storage. |
| `packages/evidence-resolver/` | EvidenceRef → EvidenceBundle candidate resolution and closure-check helpers. | Must not become a dumping ground for all evidence helpers. |

Before adding shared types:

1. inspect whether `packages/evidence/` already owns the value/helper;
2. avoid duplicate EvidenceRef, digest, citation, or identity implementations;
3. make import direction one-way and documented;
4. use an ADR/migration note for consolidation, package rename, or responsibility transfer;
5. update consumers, tests, docs, package metadata, and rollback together.

**Status:** package presence is `CONFIRMED`; final responsibility split is `NEEDS VERIFICATION / ADR`.

[Back to top](#top)

---

## Packaging and discovery boundary

The current `pyproject.toml` does not establish a complete build.

### Confirmed metadata

```toml
[project]
name = "kfm-evidence-resolver"
version = "0.0.0"
```

### Not established

- build backend;
- package discovery;
- source-layout mapping;
- supported Python version;
- dependencies;
- optional dependency groups;
- license/readme classifiers;
- package data;
- `py.typed` inclusion;
- wheel/sdist behavior;
- registry publication;
- editable-install behavior;
- reproducible build or artifact provenance.

Before claiming installability, add and test an explicit packaging profile. A successful repository-root editable install in an unrelated workflow does not by itself prove this subpackage is independently discoverable or publishable.

[Back to top](#top)

---

## Import and export contract

The current empty `evidence_resolver/__init__.py` defines no supported public API.

A future import surface may be admitted only after a resolver profile and result contract are accepted. Illustrative imports are **PROPOSED**:

```python
from evidence_resolver.profiles import ResolverProfile
from evidence_resolver.results import ResolutionCandidate
from evidence_resolver.resolve import resolve_candidate
```

Avoid:

```python
from evidence_resolver import *
from evidence_resolver._unsafe import force_resolved
from evidence_resolver.registry import global_registry
```

Export rules:

- export only reviewed, tested symbols;
- use explicit `__all__` only when stable exports exist;
- do not export schema/contract duplicates;
- do not export registry clients by default;
- do not export authority verbs such as `publish`, `approve`, `admit`, `force_resolved`, `ignore_policy`, or `bypass_release`;
- keep generated models and migration adapters private until compatibility obligations are accepted;
- do not imply that import success proves resolution correctness.

[Back to top](#top)

---

## Import-time safety

Importing `evidence_resolver` must be side-effect-free.

Import time must not:

- access a network;
- read registry, proof, lifecycle, receipt, or release stores;
- load secrets or credentials;
- read mutable environment configuration that changes semantic behavior;
- register global clients;
- create files or directories;
- mutate logging globally;
- inspect current time for resolution outcomes;
- call validators over repository fixtures;
- scan plugins;
- call model providers;
- emit public responses.

Recommended test:

```python
def test_import_is_side_effect_free() -> None:
    import evidence_resolver  # noqa: F401
```

The test should run with network/filesystem guards and an empty credential environment once a package test lane exists.

[Back to top](#top)

---

## Dependency direction

Preferred direction:

```text
accepted contracts + schemas + explicit lookup snapshots
                         |
                         v
              governed caller / adapter
                         |
                         v
       packages/evidence-resolver/src/
                         |
                         v
        local candidate checks and issues
                         |
                         v
 authoritative schema + policy + release gates
                         |
                         v
          governed runtime/API envelope
                         |
                         v
                    public client
```

The source root may depend on:

- Python standard library;
- accepted shared value types;
- `packages/evidence/` only through a documented one-way dependency;
- schema libraries after packaging review;
- generated models with provenance and version pinning.

It must not depend directly on:

- connectors or source clients;
- RAW/WORK/QUARANTINE/PROCESSED/CATALOG/PUBLISHED stores;
- evidence/proof registry implementations as hidden globals;
- policy engines;
- receipt/proof writers;
- release writers;
- API routers or application containers;
- UI/MapLibre components;
- model providers;
- deployment secrets.

Adapters that perform I/O belong in a runtime/application boundary unless an ADR explicitly places a narrow adapter package here.

[Back to top](#top)

---

## Resolver profile and drift boundary

The repository currently contains incompatible evidence-resolution descriptions.

### EvidenceRef shape conflict

The current closed schema supports:

```text
ref
kind
bundle_ref?
```

Architecture prose describes richer fields such as:

```text
ref_id
target_spec_hash
expected_bundle_digest
resolution
policy_metadata
```

These are not interchangeable. Architecture-only fields cannot be emitted into the current closed schema.

### EvidenceBundle shape conflict

The current closed schema requires:

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

Architecture prose describes additional or differently grouped families such as inputs, parameters, artifacts, checks, integrity, signatures, and attestations. A source adapter must bind to one explicit accepted profile.

### Hash-profile conflict

Architecture prose uses:

```text
jcs:sha256:<hex>
```

The current common SpecHash schema uses:

```json
{
  "value": "sha256:<64 lowercase hex>"
}
```

The current schema does not encode canonicalization. Source code must not strip/add `jcs:` or infer canonicalization silently.

### Outcome conflict

Observed vocabularies include:

```text
resolver-local: RESOLVED | UNRESOLVED | DENIED | ERROR
architecture:   ANSWER | ABSTAIN | DENY | ERROR | NEEDS_REVIEW
runtime schema: ANSWER | ABSTAIN | DENY | ERROR
```

No accepted resolver-result contract/schema was found at the exact tested paths.

### Scope conflict

The EvidenceBundle schema has free-form `claim_scope`. It does not by itself encode structured field, temporal, spatial, domain, or object scope. Source code must not claim strong scope equivalence unless the caller supplies an accepted structured profile.

### Required source-root posture

1. require explicit resolver profile identifiers;
2. validate EvidenceRef/EvidenceBundle against exact pinned schemas;
3. reject mixed-profile fields;
4. preserve hashes exactly as profile-defined;
5. keep local resolver status distinct from public runtime outcome;
6. return `UNSUPPORTED` when mapping is not accepted;
7. require an ADR/migration note before profile translation;
8. update schemas, contracts, fixtures, validators, package tests, docs, and consumers together.

[Back to top](#top)

---

## Generated code and schema adapters

Generated code may belong under this source root only when all of the following are defined:

- generator identity and version;
- input schema path and digest;
- generation command/configuration;
- output path and namespace;
- deterministic regeneration check;
- review ownership;
- compatibility policy;
- security review;
- update and rollback procedure.

Generated code must not become a second schema authority.

```text
schema = authority for shape
generated model = implementation projection
resolver helper = candidate behavior
validator = executable conformance
policy/release = admissibility and publication authority
```

Do not hand-edit generated files without a documented escape hatch. Do not commit generated EvidenceRef/EvidenceBundle models until package discovery and dependency decisions are accepted.

[Back to top](#top)

---

## Source-root input and output boundary

### Accepted source-level inputs

- accepted schema/profile identifiers;
- explicit EvidenceRef candidates;
- explicit EvidenceBundle candidates or lookup snapshots supplied by governed callers;
- caller-supplied rights, sensitivity, policy, release, correction, and supersession context;
- explicit clocks/timestamps where a profile requires them;
- deterministic synthetic fixtures.

### Permitted source-level outputs

- candidate resolver mappings or immutable values;
- deterministic local issue lists;
- schema-validation results;
- explicit unsupported-profile results;
- compatibility results that name source/target profiles;
- receipt-ready metadata for owning systems to persist.

### Prohibited source-level behavior

- direct registry or proof-store reads hidden inside pure helpers;
- creation or persistence of EvidenceBundles;
- policy decisions;
- release approval;
- lifecycle promotion;
- receipt/proof writing;
- public API serialization;
- UI rendering;
- model calls;
- fabricated refs, hashes, citations, roles, rights, sensitivity, or closure states.

[Back to top](#top)

---

## Lifecycle, evidence, policy, release, and public safety

The lifecycle invariant remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

This source root owns no lifecycle phase.

Allowed flow:

```text
governed caller
  -> explicit EvidenceRef + lookup snapshot/profile
  -> source-root helper candidate
  -> authoritative schema validation
  -> registry/proof verification
  -> policy + rights + sensitivity gates
  -> citation + release + correction gates
  -> governed runtime/API envelope
  -> public client
```

Blocked flow:

```text
source-root helper
  -> read canonical/proof/lifecycle stores directly
  -> invent missing bundle or hash
  -> translate profile drift silently
  -> emit ANSWER/public payload directly
  -> let UI infer closure from bundle_ref presence
```

Public clients must never import this package or read registry/proof stores as the normal path.

[Back to top](#top)

---

## Tests, fixtures, validators, and CI

### Confirmed repository surfaces

| Surface | Current evidence | What it proves | What it does not prove |
|---|---|---|---|
| EvidenceRef schema | Closed fielded `PROPOSED` schema. | Machine shape for current profile. | Resolver correctness or closure. |
| EvidenceBundle schema | Closed fielded `PROPOSED` schema. | Machine shape and required collections. | Registry existence, scope sufficiency, policy, release. |
| EvidenceRef fixtures | One valid and one invalid case. | Minimal schema acceptance/rejection. | Dedicated validator or resolver behavior. |
| EvidenceBundle fixtures | One valid and one invalid case. | Minimal schema acceptance/rejection. | Broad closure semantics. |
| EvidenceBundle validator | Wrapper exists. | Executable schema-validation entry point exists. | It passed in every environment or validates resolver logic. |
| EvidenceRef validator | Schema metadata declares path, exact file absent. | Metadata/file drift exists. | No dedicated wrapper behavior. |
| Generic schema harness | Evidence family is discovered. | Repository test code covers fixture families. | Package-specific resolver behavior. |
| Evidence-resolver workflow | Two jobs complete `echo TODO`. | Workflow trigger/execution scaffold. | Resolution, denial, registry, or fail-closed behavior. |

### Proposed package test lane

```text
tests/packages/evidence-resolver/
├── test_import_safety.py
├── test_public_exports.py
├── test_profile_selection.py
├── test_evidence_ref_validation.py
├── test_evidence_bundle_validation.py
├── test_lookup_snapshot.py
├── test_scope_limits.py
├── test_hash_profile.py
├── test_outcome_mapping.py
├── test_no_hidden_io.py
├── test_no_authority_imports.py
├── test_sensitive_diagnostics.py
└── test_compatibility.py
```

This tree is **PROPOSED**. Confirm repository conventions before creating it.

### Required cases

- current-profile valid and invalid refs/bundles;
- unknown and mixed profiles;
- absent `bundle_ref`;
- missing bundle;
- bundle-id mismatch;
- stale/superseded/corrected lookup context;
- invalid checksum and SpecHash shape;
- architecture hash notation supplied to current profile;
- unsupported structured-scope claims;
- rights/sensitivity/policy denial context;
- ambiguous local-to-runtime outcome mapping;
- oversized inputs;
- deterministic repeatability;
- no network/filesystem/store access;
- no secrets or sensitive evidence in diagnostics;
- no imports from connectors, stores, policy/release writers, API routes, UI, or model providers.

### Workflow truth posture

A green `.github/workflows/evidence-resolver.yml` run currently proves only that checkout and `echo TODO` steps completed. Replace echo steps with executable tests before treating the workflow as behavioral enforcement.

[Back to top](#top)

---

## Security and observability

Future source code must be no-network and no-secret by default.

Required controls:

- no environment credential reads;
- no hidden registry/proof-store clients;
- no source-system or model-provider calls;
- no raw evidence retention;
- no full candidate logging by default;
- no exact sensitive locations, living-person data, restricted records, secrets, or policy internals in issues/exceptions;
- bounded input sizes;
- explicit profile/unknown-field rejection;
- synthetic/public-safe fixtures;
- deterministic safe diagnostic codes;
- dependency review before adding JSON Schema, crypto, serialization, or client libraries;
- caller-controlled trace identifiers without hidden reasoning.

Observability belongs in caller/runtime receipts. This package may return safe receipt-ready metadata but must not persist receipts itself.

[Back to top](#top)

---

## Proposed source-tree evolution

No path below is implemented except the existing README and initializer.

```text
packages/evidence-resolver/src/
├── README.md
└── evidence_resolver/
    ├── README.md
    ├── __init__.py
    ├── profiles.py
    ├── issues.py
    ├── results.py
    ├── evidence_ref.py
    ├── evidence_bundle.py
    ├── lookup_snapshot.py
    ├── resolve.py
    └── compatibility.py       # only after accepted mappings exist
```

Smallest useful first change:

1. resolve package-versus-sibling responsibility;
2. accept one resolver profile;
3. define a resolver input/result contract;
4. repair the EvidenceRef validator metadata/file gap;
5. add package metadata and test discovery;
6. implement one no-I/O candidate function;
7. run authoritative schema validation;
8. wire one governed consumer;
9. replace echo-only CI with executable tests;
10. record correction and rollback behavior.

Do not begin with a registry client, generic framework, or public API route.

[Back to top](#top)

---

## Compatibility, correction, and rollback

### Compatibility

Before a stable API exists:

- treat all symbols as unstable;
- require explicit profile identifiers;
- reject mixed architecture/schema shapes;
- reject unknown outcome mappings;
- preserve hash notation exactly;
- document every adapter with source/target profiles, lossiness, tests, and removal plan.

After a stable release:

- follow an accepted package version policy;
- keep deprecations observable;
- require migration fixtures and consumer tests;
- retain old parsers only when governance/security allow;
- record package and profile versions in receipts.

### Correction and supersession

A corrected EvidenceRef, EvidenceBundle, schema, or canonicalization profile may invalidate prior resolution results. Callers must be able to identify:

- resolver package version;
- resolver profile/version;
- schema ids/digests;
- EvidenceRef and bundle ids;
- lookup snapshot or registry revision;
- correction/supersession state;
- policy/release context;
- original inputs needed for replay.

Source code must not mutate historical proof/release records in place.

### Rollback triggers

Rollback or disable source changes if they:

- become a registry, proof, contract, schema, policy, release, or public API authority;
- fabricate evidence or closure;
- silently translate profile shapes or hash notation;
- return public outcomes without accepted mapping;
- perform hidden network/store/model I/O;
- leak sensitive data;
- bypass governed runtime/API validation;
- duplicate `packages/evidence/` responsibilities without ADR/migration;
- break callers without tested migration.

### Documentation-only rollback

Restore prior blob:

```text
f1770cffc315004305f3b300601d8ec2914a35c6
```

No code, schema, contract, policy, fixture, test, proof, receipt, release, deployment, or registry rollback is required for this README-only change.

[Back to top](#top)

---

## Validation commands

Confirmed repository checks relevant to current schema surfaces:

```bash
python tools/validators/validate_evidence_bundle.py
pytest -q tests/schemas/test_common_contracts.py
```

The following are **PROPOSED** until files exist:

```bash
python tools/validators/validate_evidence_ref.py
pytest -q tests/packages/evidence-resolver
```

Packaging checks to add after metadata is complete:

```bash
python -m build packages/evidence-resolver
python -m pip install --no-deps packages/evidence-resolver
python -c "import evidence_resolver"
```

Do not claim these package commands pass until the build backend and discovery configuration exist.

[Back to top](#top)

---

## Definition of done

### This README revision

- [x] Grounds the Python distribution and source layout.
- [x] Records the empty initializer and absent selected helper modules.
- [x] Aligns with the merged child-module v0.2 contract.
- [x] Separates source-root structure from resolver semantics and package responsibility.
- [x] Records EvidenceRef/EvidenceBundle schemas, fixtures, validator asymmetry, and echo-only workflow.
- [x] Surfaces architecture/schema/hash/scope/outcome conflicts.
- [x] Preserves lifecycle, evidence, policy, release, public-safety, security, and rollback boundaries.
- [x] Changes no code, schema, contract, policy, workflow, fixture, test, data, proof, receipt, release, or deployment artifact.

### First supported source release

- [ ] Owners and CODEOWNERS review are accepted.
- [ ] `packages/evidence/` responsibility overlap is resolved.
- [ ] Canonical EvidenceRef/EvidenceBundle/resolver-result profiles are accepted.
- [ ] Hash/canonicalization and outcome mappings are accepted.
- [ ] Build backend, Python range, dependencies, discovery, license, and package data are defined.
- [ ] Public exports are reviewed.
- [ ] EvidenceRef validator metadata/file drift is repaired.
- [ ] Package tests cover positive, negative, unsupported, conflicting, sensitive, stale, corrected, and no-I/O cases.
- [ ] Echo-only workflow steps are replaced with executable validation.
- [ ] At least one governed consumer exists.
- [ ] Correction, migration, deprecation, and rollback are documented.
- [ ] Package artifacts have provenance/integrity verification if distributed.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status |
|---|---|---|
| `SRC-ER-001` | Who owns this source root and which CODEOWNERS rule applies? | **UNKNOWN** |
| `SRC-ER-002` | Is `packages/evidence-resolver/` permanently separate from `packages/evidence/`? | **NEEDS VERIFICATION / ADR** |
| `SRC-ER-003` | Which EvidenceRef profile is canonical: architecture prose, current schema, or successor? | **CONFLICTED** |
| `SRC-ER-004` | Which EvidenceBundle profile is canonical? | **CONFLICTED** |
| `SRC-ER-005` | What resolver input and result contract/schema should callers use? | **UNKNOWN** |
| `SRC-ER-006` | Which resolver-local outcomes are accepted? | **UNKNOWN** |
| `SRC-ER-007` | How does `NEEDS_REVIEW` map to the four public runtime outcomes? | **UNKNOWN** |
| `SRC-ER-008` | What canonicalization profile binds SpecHash production? | **UNKNOWN** |
| `SRC-ER-009` | Is `jcs:sha256:` a distinct profile or architecture shorthand? | **CONFLICTED** |
| `SRC-ER-010` | How are field, temporal, spatial, domain, and object scope represented? | **UNKNOWN** |
| `SRC-ER-011` | What registry/lookup-snapshot contract carries existence and supersession state? | **UNKNOWN** |
| `SRC-ER-012` | What build backend and package discovery configuration apply? | **UNKNOWN** |
| `SRC-ER-013` | Which Python versions and dependencies are supported? | **UNKNOWN** |
| `SRC-ER-014` | Which symbols form the first supported export surface? | **UNKNOWN** |
| `SRC-ER-015` | Which production consumers import this package? | **NEEDS VERIFICATION** |
| `SRC-ER-016` | Where should package-specific tests and fixtures live? | **NEEDS VERIFICATION** |
| `SRC-ER-017` | Why does the EvidenceRef schema declare a missing validator wrapper? | **CONFLICTED** |
| `SRC-ER-018` | Which reason-code vocabulary is stable for resolver issues? | **UNKNOWN** |
| `SRC-ER-019` | How are rights/sensitivity/policy obligations passed without local policy execution? | **UNKNOWN** |
| `SRC-ER-020` | How do correction and supersession invalidate cached resolution candidates? | **UNKNOWN** |
| `SRC-ER-021` | Which CI checks replace the current echo-only resolver workflow? | **UNKNOWN** |
| `SRC-ER-022` | Can public clients be proven unable to bypass governed resolver/API paths? | **NEEDS VERIFICATION** |
| `SRC-ER-023` | Is package-registry publication planned, and how is it separated from evidence publication? | **UNKNOWN** |
| `SRC-ER-024` | What rollback target and compatibility window apply after the first stable release? | **UNKNOWN** |

[Back to top](#top)

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Current request | **CONFIRMED task authority** | Update this exact source-root README. | Not implementation proof. |
| Prior target README | **CONFIRMED** | Existing no-network, cite-or-abstain, helper-only, anti-authority posture. | Planning-oriented and stale. |
| `packages/evidence-resolver/pyproject.toml` | **CONFIRMED** | Distribution `kfm-evidence-resolver`, version `0.0.0`. | No complete build/discovery/dependency profile. |
| `src/evidence_resolver/__init__.py` | **CONFIRMED empty** | Import namespace scaffold. | No exports or behavior. |
| Child module README v0.2 | **CONFIRMED merged document** | Current detailed resolver candidate and conflict posture. | Documentation, not code/runtime proof. |
| Parent package README | **CONFIRMED repository doc** | Package and sibling-package intent. | Planning-oriented; does not prove implementation. |
| EvidenceRef contract/schema | **CONFIRMED paired draft surfaces** | Current pointer meaning and closed shape. | Status `PROPOSED`; architecture profile differs. |
| EvidenceBundle contract/schema | **CONFIRMED paired draft surfaces** | Current closure meaning and closed shape. | Status `PROPOSED`; registry/policy/release behavior separate. |
| SpecHash contract/schema | **CONFIRMED paired draft surfaces** | Current `{value: sha256:...}` shape. | Canonicalization is not encoded. |
| EvidenceRef fixtures | **CONFIRMED minimal family** | One valid and one invalid schema case. | Dedicated validator missing; narrow coverage. |
| EvidenceBundle fixtures | **CONFIRMED minimal family** | One valid and one invalid schema case. | Narrow coverage. |
| EvidenceBundle validator | **CONFIRMED file** | Schema wrapper exists. | Package behavior not proven. |
| Common schema harness | **CONFIRMED test code** | Discovers evidence schema fixture families. | Resolver tests not established. |
| Evidence-resolver workflow | **CONFIRMED workflow / echo-only** | Pull-request workflow exists and runs. | Does not enforce resolver semantics or fail-closed behavior. |
| Directory Rules v1.4 | **CONFIRMED placement doctrine** | `packages/` is shared implementation; authority/data/test/runtime roots remain separate. | Specific unresolved package split may require ADR. |
| Architecture evidence-identity note | **CONFIRMED document / mixed posture** | Explains resolver/trust-membrane intent and exposes richer proposed profiles. | Several paths/shapes remain proposed and conflict with current schemas. |
| Bounded repository checks | **CONFIRMED limited inspection** | Selected modules, package test/fixture READMEs, and resolver-result paths were absent at exact paths. | Not exhaustive tree or runtime proof. |

[Back to top](#top)

---

## Status summary

`packages/evidence-resolver/src/` is a verified Python source-layout container for distribution `kfm-evidence-resolver` version `0.0.0`. Its child import package exists but contains only an empty initializer and a repository-grounded README; selected resolver modules, supported exports, package tests, consumers, and runtime wiring are not established. EvidenceRef and EvidenceBundle have paired draft schemas/contracts and minimal schema fixtures, but resolver-result, hash, scope, outcome, sibling-package, validator, and CI boundaries remain unresolved. The next useful change is governance reconciliation plus one profile-pinned, no-I/O candidate function and executable tests—not a registry client or broad resolver framework.

<p align="right"><a href="#top">Back to top</a></p>
