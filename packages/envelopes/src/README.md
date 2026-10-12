<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-envelopes-src-readme
title: packages/envelopes/src/ — Governed Envelope Package Source Root
type: readme
version: v0.2
status: draft; repository-grounded; python-src-root; implementation-placeholder; non-authoritative
owners:
  - OWNER_TBD — Envelopes package owner
  - OWNER_TBD — Runtime and governed API steward
  - OWNER_TBD — Contract and schema steward
  - OWNER_TBD — Policy, rights, and sensitivity steward
  - OWNER_TBD — Evidence, citation, release, and correction steward
  - OWNER_TBD — Validator, security, packaging, and docs steward
created: NEEDS VERIFICATION — target file existed before this revision
updated: 2026-07-15
supersedes: v1 planning-oriented source-directory guide (2026-06-14)
policy_label: public; packages; envelopes; python; src-layout; finite-outcomes; no-network-by-default; fail-closed; evidence-ref-aware; non-authoritative
path: packages/envelopes/src/README.md
truth_posture: CONFIRMED target and prior blob, kfm-envelopes 0.0.0 project metadata, Python src layout, envelopes import package, empty initializer, merged child-module v0.2 contract, bounded absence of tested helper modules and package.json, parent package README, runtime/envelopes lane, fielded closed RuntimeResponseEnvelope and DecisionEnvelope schemas, paired draft contracts, validators, fixture roots, common schema harness, Directory Rules v1.4, draft/proposed ADR-0019, and schema-validation workflow / PROPOSED future package discovery, explicit exports, pure candidate builders, generated schema adapters, compatibility adapters, package tests, and typed marker / CONFLICTED architecture-envelope prose versus current paired schema fields, DecisionEnvelope policy-style vocabulary versus schema finite outcomes, package source implementation versus runtime/envelopes ownership, and package-specific versus contract-schema fixture/test placement / UNKNOWN build backend, Python requirement, dependencies, package discovery, license metadata, public exports, import consumers, runtime/API wiring, package-specific CI, registry publication, release integration, and production behavior / NEEDS VERIFICATION accepted owners, canonical envelope profiles, reason-code/state vocabularies, schema/contract acceptance, generation provenance, compatibility policy, correction invalidation, and rollback integration
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 7862e6c8b3c724839be32bbc465dc159e443e424
  prior_blob: c874ad6ec7b4615747e1c32ea8c0b3de316ee1b4
  child_module_blob: 72d2ecdab6b056f6eb7efdd66a39fa5b0b27c8cf
related:
  - ./envelopes/README.md
  - ./envelopes/__init__.py
  - ../README.md
  - ../pyproject.toml
  - ../../README.md
  - ../../../runtime/envelopes/README.md
  - ../../../contracts/runtime/runtime_response_envelope.md
  - ../../../contracts/runtime/decision_envelope.md
  - ../../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
  - ../../../schemas/contracts/v1/runtime/decision_envelope.schema.json
  - ../../../fixtures/contracts/v1/runtime/runtime_response_envelope/README.md
  - ../../../fixtures/contracts/v1/runtime/decision_envelope/README.md
  - ../../../tools/validators/validate_runtime_response_envelope.py
  - ../../../tools/validators/validate_decision_envelope.py
  - ../../../tests/schemas/test_common_contracts.py
  - ../../../docs/architecture/governed-api/ENVELOPES.md
  - ../../../docs/adr/ADR-0019-ai-adapter-contract-and-finite-envelopes.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../.github/workflows/schema-validation.yml
tags: [kfm, packages, envelopes, python, src-layout, source-root, import-boundary, runtime-response-envelope, decision-envelope, finite-outcomes, profiles, generated-code, deterministic, no-network, fail-closed, rollback]
notes:
  - "v0.2 replaces stale planning language with a commit-pinned description of the current kfm-envelopes 0.0.0 Python src-layout scaffold."
  - "The child envelopes module README v0.2 owns detailed candidate-builder semantics; this file owns source-root, package-discovery, import, dependency, generated-code, packaging, test-placement, and compatibility boundaries."
  - "The import package initializer is empty and tested helper-module paths are absent; no supported API, build behavior, consumer, or runtime integration is claimed."
  - "Current architecture prose and paired runtime schemas conflict; the source root requires explicit profile selection and forbids silent compatibility invention."
  - "Only this Markdown file changes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Envelope Package Source Root

`packages/envelopes/src/`

> Python `src`-layout container for the `kfm-envelopes` shared package. This directory may organize reusable finite-outcome envelope helper implementation, but it must not become envelope semantic authority, schema authority, policy execution, evidence resolution, lifecycle storage, receipt/proof persistence, release authority, runtime orchestration, public API routing, UI/map rendering, or generated truth.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.2-informational)
![distribution](https://img.shields.io/badge/distribution-kfm--envelopes-3776ab)
![layout](https://img.shields.io/badge/layout-Python%20src--layout-3776ab)
![implementation](https://img.shields.io/badge/implementation-placeholder-lightgrey)
![outcomes](https://img.shields.io/badge/outcomes-ANSWER%20%7C%20ABSTAIN%20%7C%20DENY%20%7C%20ERROR-6f42c1)
![network](https://img.shields.io/badge/network-none%20by%20default-455a64)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-0b7285)

**Quick links:** [Purpose](#purpose-and-audience) · [Status](#current-repository-state) · [Context](#source-root-bounded-context) · [Placement](#placement-and-authority) · [Surface](#current-source-tree) · [Root/module split](#source-root-versus-import-module) · [Packaging](#packaging-and-discovery-boundary) · [Imports](#import-and-export-contract) · [Import safety](#import-time-safety) · [Dependencies](#dependency-direction) · [Profiles](#envelope-profile-and-drift-boundary) · [Generated code](#generated-code-and-schema-adapters) · [Inputs](#source-root-input-and-output-boundary) · [Trust](#lifecycle-evidence-policy-release-and-public-safety) · [Tests](#tests-fixtures-validators-and-ci) · [Security](#security-and-observability) · [Evolution](#proposed-source-tree-evolution) · [Compatibility](#compatibility-correction-and-rollback) · [Validation](#validation-commands) · [Done](#definition-of-done) · [Backlog](#open-verification-register) · [Ledger](#evidence-ledger)

> [!IMPORTANT]
> **Repository snapshot:** `main@7862e6c8b3c724839be32bbc465dc159e443e424`<br>
> **Distribution:** `kfm-envelopes`<br>
> **Declared version:** `0.0.0`<br>
> **Verified source root:** `src/`<br>
> **Verified import package:** `src/envelopes/`<br>
> **Verified implementation:** empty `envelopes/__init__.py`; tested helper files were absent<br>
> **Verified child contract:** [`envelopes/README.md`](./envelopes/README.md) v0.2<br>
> **Build backend, Python requirement, dependencies, package discovery, exports, and consumers:** not established<br>
> **Runtime schemas/contracts:** present but `PROPOSED`, with documented architecture/schema drift

> [!CAUTION]
> Source layout does not confer authority. A package can contain a candidate builder without owning the envelope contract. A schema adapter can validate shape without approving policy, resolving evidence, authorizing release, or serving a public response.

---

## Purpose and audience

`packages/envelopes/src/` is the implementation container for the Python project declared by [`../pyproject.toml`](../pyproject.toml).

Its durable responsibilities are structural:

- contain importable source for the `envelopes` package;
- make package discovery and import boundaries explicit;
- provide a stable home for reusable, source-agnostic envelope helper code;
- keep package exports deliberate, small, versioned, and reviewable;
- keep import-time behavior deterministic and side-effect-free;
- preserve explicit envelope profile, source refs, evidence refs, policy posture, freshness, correction state, time, version, and hash lineage;
- keep generated adapters subordinate to accepted contracts and schemas;
- keep implementation separate from runtime orchestration, source connectors, policy engines, lifecycle data, evidence stores, receipt/proof stores, release systems, API routes, UI/map code, and model providers;
- support deterministic, synthetic, no-network tests without storing production payloads in the source root.

This README is for package and runtime maintainers, governed API authors, contract/schema/policy/evidence/release stewards, validator and test maintainers, packaging/security reviewers, and maintainers deciding whether proposed code belongs in this source root.

Detailed candidate-builder and object-family semantics belong in [`envelopes/README.md`](./envelopes/README.md). This source-root README governs the container, discovery, import surface, dependency direction, generated-code boundary, test placement, packaging posture, compatibility, and enforceability placement.

[Back to top](#top)

---

## Current repository state

| Surface | Evidence at snapshot | Status | Consequence |
|---|---|---:|---|
| This README | Existing v1 planning-oriented source guide. | **CONFIRMED** | Revised in place. |
| [`../pyproject.toml`](../pyproject.toml) | Declares `[project]`, name `kfm-envelopes`, and version `0.0.0` only. | **CONFIRMED minimal placeholder** | Distribution identity is known; build and dependency behavior are not. |
| [`envelopes/README.md`](./envelopes/README.md) | Merged repository-grounded source-module contract v0.2. | **CONFIRMED** | Detailed helper semantics and conflict posture live there. |
| `envelopes/__init__.py` | Exists and is empty. | **CONFIRMED** | Import-package marker only; no public exports are established. |
| `package.json` | Absent at `packages/envelopes/package.json`. | **CONFIRMED bounded absence** | Do not claim a JavaScript/TypeScript package. |
| Selected helper files | `outcomes.py`, `runtime_response.py`, `decision.py`, and `validation.py` were absent at exact tested paths. | **CONFIRMED bounded absence** | No executable envelope helper implementation is established. |
| Build backend | No `[build-system]` section was observed. | **NOT OBSERVED** | Build/install behavior remains unknown. |
| Dependencies | No dependency list was observed. | **NOT OBSERVED** | Do not claim `jsonschema`, API, runtime, or generated-model dependencies. |
| Supported Python versions | No `requires-python` field was observed. | **NOT OBSERVED** | Interpreter support is unknown. |
| Package discovery | No explicit package-discovery configuration was observed. | **NOT OBSERVED** | Do not claim editable install or wheel inclusion works. |
| Public exports | Empty initializer. | **NOT ESTABLISHED** | No symbol is part of a supported package API. |
| Consumers | Indexed search did not establish production imports of `envelopes`. | **NOT OBSERVED / search-limited** | Do not claim runtime/API integration. |
| Parent package README | `packages/envelopes/README.md` exists but retains older planning assumptions. | **CONFIRMED README / stale relative to child evidence** | This source root follows current repo evidence and the merged child contract. |
| Runtime helper lane | `runtime/envelopes/README.md` exists. | **CONFIRMED documentation lane** | Implementation ownership must be resolved before parallel code appears. |
| RuntimeResponseEnvelope contract/schema | Paired draft contract and fielded closed schema exist. | **CONFIRMED surfaces / `PROPOSED` status** | Builders must bind to an explicit accepted profile. |
| DecisionEnvelope contract/schema | Paired draft contract and fielded closed schema exist. | **CONFIRMED surfaces / `PROPOSED` status** | Older decision vocabulary cannot be assumed compatible. |
| Dedicated validators | Thin entry points load the paired schemas and fixture roots. | **CONFIRMED files** | Presence does not prove current execution success or package behavior. |
| Runtime fixture families | One documented valid and one invalid fixture exist for each paired schema. | **CONFIRMED minimal coverage** | Coverage is narrow and schema-only. |
| Generic schema harness | `tests/schemas/test_common_contracts.py` discovers runtime fixtures. | **CONFIRMED test code** | Package-level tests are not established. |
| Package test README | `tests/packages/envelopes/README.md` was absent at the exact tested path. | **CONFIRMED bounded absence** | No package-specific test lane is documented there. |
| Package fixture README | `fixtures/packages/envelopes/README.md` was absent at the exact tested path. | **CONFIRMED bounded absence** | No package-specific fixture lane is documented there. |
| Schema workflow | `.github/workflows/schema-validation.yml` installs the root package and runs `make schemas`. | **CONFIRMED workflow definition** | Package-specific enforcement is unknown. |
| Runtime/release evidence | No deployed consumer, runtime log, receipt, release artifact, or public response was inspected. | **UNKNOWN** | This README is not implementation or deployment proof. |

```text
Python distribution identity            = CONFIRMED
Python src-layout container              = CONFIRMED
envelopes import package                 = CONFIRMED
empty initializer                        = CONFIRMED
implemented helper modules               = NOT OBSERVED
supported public exports                 = NOT ESTABLISHED
package consumers                        = NOT OBSERVED
build/install behavior                   = UNKNOWN
package-specific tests/fixtures          = NOT ESTABLISHED
schema contracts/fixtures/validators     = CONFIRMED, PROPOSED/narrow
runtime/API behavior                     = UNKNOWN
release behavior                         = UNKNOWN
```

[Back to top](#top)

---

## Source-root bounded context

The source-root bounded context is:

> The organization and admission boundary for importable, reusable envelope helper implementation.

It includes:

- source-tree structure;
- package discovery;
- import-module placement;
- supported exports;
- dependency direction;
- import-time safety;
- generated-code placement;
- schema-profile adapter placement;
- package tests/fixtures integration;
- packaging, distribution, compatibility, and deprecation posture.

It excludes:

- envelope semantic meaning;
- canonical schema shape;
- policy evaluation;
- source admission;
- evidence resolution or closure;
- lifecycle orchestration;
- receipt/proof persistence;
- release approval;
- correction/withdrawal mutation;
- runtime service orchestration;
- public API serialization;
- UI/map rendering;
- model execution;
- public truth.

| Concept | Current value | Status |
|---|---|---|
| Distribution name | `kfm-envelopes` | **CONFIRMED** |
| Source root | `packages/envelopes/src/` | **CONFIRMED** |
| Import package | `envelopes` | **CONFIRMED path / no exports** |
| Version | `0.0.0` | **CONFIRMED placeholder** |
| Public package API | none established | **NOT OBSERVED** |
| Build backend | none observed | **UNKNOWN** |
| Implementation owner versus `runtime/envelopes/` | unresolved | **NEEDS VERIFICATION / ADR** |

[Back to top](#top)

---

## Placement and authority

Directory Rules classify `packages/` as the shared reusable implementation root.

```text
packages/envelopes/                   = package-level boundary
packages/envelopes/src/               = Python source-layout container
packages/envelopes/src/envelopes/     = import package and helper module boundary

contracts/runtime/                    = envelope semantic meaning
schemas/contracts/v1/runtime/         = machine-checkable envelope shape
policy/runtime/                       = runtime policy and obligations
runtime/envelopes/                    = runtime envelope handoff/note lane
tools/validators/                     = validator entry points
tests/ + fixtures/                    = enforceability and examples
data/                                 = lifecycle, receipts, and proofs
release/                              = release/correction/rollback authority
apps/                                 = governed runtime/API and client applications
```

This path is valid because its responsibility is reusable source code, not because the topic is “envelopes.”

### Authority table

| Question | Answer |
|---|---|
| Can this root define envelope fields? | No. It may implement an accepted contract/schema profile. |
| Can it decide `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`? | No. It may preserve or locally validate an explicit outcome supplied by governed runtime logic. |
| Can it translate policy `hold` or `restrict` into public outcomes? | Not without an accepted policy/runtime mapping. |
| Can it resolve EvidenceRefs or create EvidenceBundles? | No. |
| Can it approve release or promotion? | No. |
| Can public clients import it directly? | No. Public clients consume governed runtime/API envelopes. |
| Can it contain generated schema models? | Only under accepted generation, provenance, version, review, and regeneration rules. |
| Can it own runtime service wiring? | No. Runtime orchestration belongs outside this source root. |

[Back to top](#top)

---

## Current source tree

The verified source surface at the snapshot is:

```text
packages/envelopes/src/
├── README.md
└── envelopes/
    ├── README.md
    └── __init__.py
```

The initializer is empty. The tested helper paths were absent.

Do not infer the existence of:

```text
outcomes.py
runtime_response.py
decision.py
validation.py
profiles.py
issues.py
compatibility.py
py.typed
_generated/
```

Those names remain **PROPOSED** until implementation admission and repository evidence establish them.

[Back to top](#top)

---

## Source root versus import module

The two README levels have different responsibilities.

| File | Owns | Does not own |
|---|---|---|
| `packages/envelopes/src/README.md` | Source layout, discovery, import placement, dependency direction, generated-code boundary, packaging, test placement, compatibility. | Detailed helper API semantics or object-family authority. |
| `packages/envelopes/src/envelopes/README.md` | Candidate-builder semantics, envelope-profile rules, object-family boundaries, local issue/result posture, security and fail-closed behavior. | Package discovery, build backend, runtime orchestration, schemas, policy, evidence, or release. |
| `packages/envelopes/README.md` | Package-level purpose and shared-library boundary. | Source-module implementation details and authority roots. |

Changes that affect only one level should not be copied blindly into all three. Update dependent documentation when behavior or public guarantees materially change.

[Back to top](#top)

---

## Packaging and discovery boundary

The current `pyproject.toml` establishes only:

```toml
[project]
name = "kfm-envelopes"
version = "0.0.0"
```

The following remain unknown:

- build backend;
- package discovery;
- source-layout mapping;
- Python requirement;
- runtime/test/optional dependencies;
- license metadata;
- package data;
- typed-package marker inclusion;
- wheel/sdist behavior;
- editable-install behavior;
- package registry;
- publishing credentials and provenance;
- reproducible build settings.

Before implementation is considered installable, an accepted package configuration must prove that `src/envelopes/` is discovered and included.

A future packaging decision should explicitly answer:

```text
build backend
Python range
dependency groups
src-layout discovery
package data
py.typed posture
license/readme metadata
build reproducibility
artifact signing/provenance
registry and release separation
```

Package distribution is not KFM data publication. Publishing a wheel cannot promote data, approve a claim, or release a map layer.

[Back to top](#top)

---

## Import and export contract

### Current state

`envelopes/__init__.py` is empty. Therefore:

- no supported public symbol is established;
- no import-time setup behavior is established;
- no stable compatibility promise exists;
- no wildcard export is authorized;
- no caller may assume a top-level builder API.

### Future export rules

A supported export must be:

- backed by a real consumer;
- bound to an explicit accepted envelope profile;
- documented in the child module README;
- covered by positive, negative, ambiguity, and no-I/O tests;
- versioned under an accepted compatibility policy;
- safe to import without network, filesystem, credential, model, policy, evidence-store, or release side effects.

Preferred shape after admission:

```python
from envelopes.outcomes import Outcome
from envelopes.runtime_response import build_runtime_response_candidate
from envelopes.decision import build_decision_envelope_candidate
```

Avoid:

```python
from envelopes import *
from envelopes._internal import unsafe_assembler
from runtime.envelopes import build_response  # parallel implementation risk
```

`__init__.py` should remain empty until the first stable export is intentionally reviewed. Re-exporting every internal helper is not a compatibility strategy.

[Back to top](#top)

---

## Import-time safety

Importing `envelopes` must not:

- read environment credentials;
- read or write files;
- fetch schemas or contracts over a network;
- open database or object-store connections;
- inspect RAW, WORK, QUARANTINE, canonical, or release stores;
- call a policy engine;
- call a model provider;
- register public routes;
- mutate global registries;
- create random ids;
- read the wall clock for hidden defaults;
- emit receipts, proofs, metrics containing payload data, or release records;
- configure logging globally;
- select “latest” schemas dynamically.

Allowed import-time behavior should be limited to defining constants, enums, immutable types, and pure functions.

Any registry must be explicit, local, deterministic, versioned, and passed or imported deliberately—not populated by plugin discovery or ambient process state unless an accepted architecture requires it.

[Back to top](#top)

---

## Dependency direction

Preferred dependency flow:

```text
accepted contracts/schemas/policy vocabularies
                 |
                 v
generated or handwritten narrow value adapters
                 |
                 v
packages/envelopes/src/envelopes
                 |
                 v
governed runtime/API caller
                 |
                 v
authoritative validation + evidence/policy/release gates
                 |
                 v
public response
```

Allowed dependencies, after explicit packaging approval:

- Python standard library;
- narrow shared immutable value types;
- pinned schema-validation library;
- generated models with provenance;
- stable local canonicalization/hash helpers.

Prohibited dependencies:

- connectors and source clients;
- lifecycle or canonical-store access;
- policy engines;
- evidence resolvers or proof stores;
- receipt persistence;
- release writers;
- model-provider SDKs;
- API routers and service containers;
- UI/map packages;
- deployment configuration and credentials.

Authority roots must not depend on this package to define their meaning. Contracts, schemas, policy, lifecycle, and release remain independently inspectable.

[Back to top](#top)

---

## Envelope profile and drift boundary

The repository currently exposes conflicting envelope descriptions.

### RuntimeResponseEnvelope

Architecture prose describes a richer wire object with fields such as:

```text
object_type
schema_version
policy_decision
release_ref
citation_validation
payload
reason
trace
```

The paired closed schema instead requires:

```text
id
spec_hash
version
issued_at
outcome
reason_code
evidence_refs
policy_state
freshness
correction_state
```

Because `additionalProperties` is `false`, these are not interchangeable profiles.

### DecisionEnvelope

Older architecture prose uses:

```text
allow · deny · restrict · hold · abstain
```

The paired schema requires:

```text
ANSWER · ABSTAIN · DENY · ERROR
```

and a closed `policy_family` enum.

### Source-root rule

No source file may implement an unqualified “envelope” API while this drift is unresolved.

Every implementation must name:

- object family;
- semantic contract;
- schema path;
- schema/profile version;
- content/spec hash when available;
- compatibility behavior;
- unsupported fields;
- migration and rollback plan.

Mixed-profile objects must fail closed. Silent renaming, omission, coercion, or policy-to-outcome translation is prohibited.

[Back to top](#top)

---

## Generated code and schema adapters

Generated code may be useful, but it must remain subordinate to accepted authority.

### Preconditions

Before adding generated models or adapters:

- the contract/schema profile is accepted or explicitly version-pinned as experimental;
- generation inputs are immutable or hash-pinned;
- generator name/version and command are recorded;
- output path is approved under Directory Rules;
- regeneration is deterministic;
- generated files are clearly marked;
- generated code does not embed policy, evidence resolution, release decisions, or runtime I/O;
- fixtures and compatibility tests cover generation changes;
- review can distinguish generated changes from handwritten adapters.

### Proposed placement

```text
packages/envelopes/src/envelopes/
├── _generated/            # PROPOSED, only after generation policy is accepted
│   ├── README.md
│   └── <profile-specific models>
└── adapters/              # PROPOSED handwritten boundary around generated types
```

Do not put canonical schemas under `src/`. Do not edit generated files manually without a documented emergency repair and regeneration plan.

Generated models are not automatically the supported package API. Stable exports should wrap or alias them deliberately so generator churn does not leak into every consumer.

[Back to top](#top)

---

## Source-root input and output boundary

### Inputs to code in this source tree

Allowed inputs are explicit, caller-supplied, and already available in memory:

- selected envelope profile/version;
- required field values;
- finite outcome;
- stable identifiers and hashes;
- issuance/evaluation times;
- reason codes/reasons;
- EvidenceRef carriers;
- policy family/state/obligations;
- freshness and correction state;
- explicit release/trace refs when an accepted profile supports them.

Disallowed input acquisition:

- live network fetches;
- raw/canonical store reads;
- environment credential reads;
- model calls;
- policy-engine execution;
- hidden global state;
- UI state scraping;
- filesystem schema discovery at runtime;
- “latest” profile lookups.

### Outputs from code in this source tree

Permitted outputs:

- profile-specific candidate mapping/value object;
- deterministic local issues;
- explicit unsupported-profile result;
- explicit compatibility conversion result;
- synthetic fixture candidate.

Prohibited outputs:

- public HTTP response;
- released/published object;
- EvidenceBundle;
- PolicyDecision;
- PromotionDecision;
- authoritative receipt/proof;
- lifecycle mutation;
- model-generated answer;
- UI/map projection that bypasses governed API;
- success boolean that hides issues or profile selection.

[Back to top](#top)

---

## Lifecycle, evidence, policy, release, and public safety

The lifecycle invariant remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

This source root does not store or move lifecycle records.

### Evidence

Helpers may preserve EvidenceRefs but must not resolve, fabricate, upgrade, or declare them sufficient. `ANSWER` remains governed by evidence, policy, freshness, correction, release, and audience conditions outside this package.

### Policy and sensitivity

Helpers may preserve explicit policy fields and obligations. They must not evaluate access, render, capability, consent, sensitivity, rights, or release policy. Unknown or conflicting policy mappings fail closed.

### Release and correction

Helpers may preserve accepted refs/states. They must not create manifests, promote, publish, correct, withdraw, supersede, or roll back releases.

### Public trust membrane

Public clients must not import package internals. A mature flow is:

```text
governed caller
  -> package candidate helper
  -> authoritative schema validation
  -> policy/evidence/release/freshness/correction gates
  -> governed runtime/API serializer
  -> public client
```

A package helper cannot turn a bare payload into trusted public content.

[Back to top](#top)

---

## Tests, fixtures, validators, and CI

### Confirmed shared validation surfaces

- RuntimeResponseEnvelope schema and fixture family;
- DecisionEnvelope schema and fixture family;
- dedicated validator entry points;
- generic contract-schema fixture harness;
- repository schema-validation workflow.

These prove schema infrastructure exists. They do not prove package implementation, import safety, compatibility, policy correctness, evidence sufficiency, release safety, or public integration.

### Package-specific test placement

`tests/packages/envelopes/README.md` and `fixtures/packages/envelopes/README.md` were absent at exact tested paths.

Before creating them:

- verify repository package-test conventions;
- avoid duplicating contract-schema fixtures;
- reuse canonical schema fixtures where appropriate;
- keep package fixtures synthetic/public-safe;
- document whether package tests wrap, extend, or deliberately differ from contract fixtures.

### Proposed package tests

```text
tests/packages/envelopes/
├── test_source_root.py
├── test_import_safety.py
├── test_public_exports.py
├── test_runtime_response_candidate.py
├── test_decision_envelope_candidate.py
├── test_profile_rejection.py
├── test_closed_fields.py
├── test_identity_hash_and_time.py
├── test_no_hidden_io.py
├── test_dependency_boundaries.py
└── test_compatibility.py          # only after mappings exist
```

This tree is **PROPOSED**.

### Required test classes

- import succeeds in a clean no-network environment;
- no import-time side effects;
- deterministic repeatability;
- exact public export surface;
- missing required fields;
- unknown closed-schema fields;
- invalid outcomes, policy families, ids, hashes, and timestamps;
- conflicting aliases;
- mixed profiles;
- unsupported profiles;
- evidence-ref shape preservation;
- stale/correction-affected context preservation;
- safe issues/exceptions;
- dependency graph exclusions;
- generated-model regeneration;
- compatibility and breaking-version behavior;
- oversized input limits.

### CI posture

The schema-validation workflow is repository-level. A future package workflow should not report green by echoing TODOs or by running schema tests alone. It should prove import, unit, boundary, no-I/O, compatibility, security, and packaging behavior.

[Back to top](#top)

---

## Security and observability

Future source code should be secure by default:

- no network;
- no secrets;
- no credentials;
- no raw provider payloads;
- no hidden reasoning;
- no unrestricted source or evidence text;
- no exact protected locations or private data in ids/errors/logs;
- no dynamic code loading;
- no unbounded recursion or payload growth;
- no unsafe deserialization;
- no mutable global registries;
- no environment-dependent behavior;
- no schema downloads at runtime.

Observability may emit:

- safe issue code;
- profile/version;
- operation name;
- duration;
- count summaries;
- caller-provided request/run correlation id;
- success/invalid/unsupported/error status.

Observability must not emit full envelope payloads by default. Logs are not receipts, proofs, policy decisions, or release records.

[Back to top](#top)

---

## Proposed source-tree evolution

The smallest useful evolution after governance resolution is:

```text
packages/envelopes/src/
├── README.md
└── envelopes/
    ├── README.md
    ├── __init__.py
    ├── outcomes.py
    ├── issues.py
    ├── profiles.py
    ├── runtime_response.py
    └── decision.py
```

Add only when justified:

```text
compatibility.py
adapters/
_generated/
py.typed
```

Admission order:

1. resolve package-versus-runtime ownership;
2. resolve or explicitly pin envelope profiles;
3. define packaging/discovery and dependencies;
4. establish package test placement;
5. implement one profile-specific candidate builder;
6. keep exports narrow;
7. run shared schema validators and package tests;
8. wire one governed consumer;
9. record review evidence and rollback target;
10. add compatibility/generated code only from demonstrated need.

Do not create a broad framework before one supported consumer and one accepted profile exist.

[Back to top](#top)

---

## Compatibility, correction, and rollback

### Compatibility

Until a stable API exists:

- all proposed symbols are unstable;
- explicit profile identifiers are required;
- unknown/mixed profiles are rejected;
- architecture-only and schema-only fields are not silently combined;
- policy decision vocabularies are not silently mapped to public outcomes;
- no default “latest” profile is selected.

After a stable release:

- follow an accepted versioning policy;
- document deprecation windows;
- provide migration fixtures and consumer tests;
- record lossy conversions;
- keep profile hashes/versions observable;
- remove compatibility shims deliberately.

### Correction

A schema/contract correction may invalidate generated models, adapters, package candidates, fixtures, and downstream responses. Maintain enough lineage to:

- identify the profile/version/hash used;
- detect superseded profiles;
- regenerate adapters;
- rebuild candidates from original governed inputs;
- invalidate affected caches/artifacts;
- preserve historical receipts rather than rewriting them.

### Rollback triggers

Rollback or disable source changes that:

- introduce parallel schema/contract/policy/evidence/release authority;
- create parallel implementation beside `runtime/envelopes/` without migration authority;
- perform hidden I/O;
- accept mixed profiles;
- fabricate refs, ids, hashes, times, decisions, or release support;
- leak sensitive data;
- bypass authoritative validation or governed API/runtime gates;
- break consumers without migration;
- publish an incomplete or irreproducible package.

### Documentation-only rollback

Restore prior target blob:

```text
c874ad6ec7b4615747e1c32ea8c0b3de316ee1b4
```

No code, schema, contract, policy, runtime, fixture, test, data, receipt, proof, release, deployment, or publication rollback is required for this README-only revision.

[Back to top](#top)

---

## Validation commands

Current confirmed validation paths:

```bash
python tools/validators/validate_runtime_response_envelope.py
python tools/validators/validate_decision_envelope.py
pytest -q tests/schemas/test_common_contracts.py
```

Future package checks, after placement exists:

```bash
python -c "import envelopes"
pytest -q tests/packages/envelopes
python -m build packages/envelopes
python -m pip install --no-deps --force-reinstall <built-wheel>
python -c "import envelopes; print(envelopes.__file__)"
```

Do not claim these future commands pass until package configuration and tests exist and are run at the review commit.

Review should also inspect:

```bash
find packages/envelopes/src -maxdepth 5 -type f | sort
git grep -n "from envelopes\|import envelopes" -- . 2>/dev/null || true
git grep -n "packages.envelopes\|runtime.envelopes" -- . 2>/dev/null || true
```

[Back to top](#top)

---

## Definition of done

### This README revision

- [x] Replaces stale source-layout uncertainty with verified Python `src`-layout evidence.
- [x] Records `kfm-envelopes` version `0.0.0`.
- [x] Records the merged child module v0.2 contract and empty initializer.
- [x] Records bounded absence of tested helper files and package-specific test/fixture READMEs.
- [x] Separates source-root concerns from module semantics and runtime orchestration.
- [x] Preserves contracts, schemas, policy, lifecycle, evidence, release, runtime, tests, and apps as distinct authority roots.
- [x] Surfaces profile and ownership conflicts.
- [x] Defines packaging, import, dependency, generated-code, test, security, compatibility, correction, and rollback boundaries.
- [x] Changes only this Markdown file.

### First supported source package

- [ ] Owners and CODEOWNERS review are accepted.
- [ ] Package-versus-runtime implementation ownership is resolved.
- [ ] Envelope profile conflicts are resolved or version-pinned.
- [ ] Build backend, Python range, discovery, dependencies, license, and package data are defined.
- [ ] Public exports and compatibility policy are accepted.
- [ ] At least one governed consumer exists.
- [ ] Package tests and appropriate fixtures exist.
- [ ] Schema, package, import-safety, dependency-boundary, and packaging checks pass.
- [ ] Generated code, if any, is reproducible and provenance-bound.
- [ ] No trust-membrane or authority-root bypass is proven.
- [ ] Correction, deprecation, migration, and rollback are documented.
- [ ] Package artifact provenance and integrity are verified if distributed.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status |
|---|---|---|
| `PKG-ENV-SRC-001` | Who owns the source root and which CODEOWNERS rule is enforceable? | **UNKNOWN** |
| `PKG-ENV-SRC-002` | Does implementation ownership belong here or under `runtime/envelopes/`? | **NEEDS VERIFICATION / ADR** |
| `PKG-ENV-SRC-003` | Which RuntimeResponseEnvelope profile is canonical? | **CONFLICTED** |
| `PKG-ENV-SRC-004` | Which DecisionEnvelope vocabulary is canonical? | **CONFLICTED** |
| `PKG-ENV-SRC-005` | What is the acceptance status of current runtime contracts and schemas? | **NEEDS VERIFICATION** |
| `PKG-ENV-SRC-006` | Which build backend and package-discovery configuration apply? | **UNKNOWN** |
| `PKG-ENV-SRC-007` | Which Python versions are supported? | **UNKNOWN** |
| `PKG-ENV-SRC-008` | Which runtime, test, and optional dependencies are approved? | **UNKNOWN** |
| `PKG-ENV-SRC-009` | Which symbols form the first supported public API? | **UNKNOWN** |
| `PKG-ENV-SRC-010` | Which governed consumer will be the first adopter? | **UNKNOWN** |
| `PKG-ENV-SRC-011` | Where should package-specific tests and fixtures live? | **NEEDS VERIFICATION** |
| `PKG-ENV-SRC-012` | Which reason-code and state vocabularies bind helpers? | **UNKNOWN** |
| `PKG-ENV-SRC-013` | How are policy `hold`/`restrict` states mapped to public finite outcomes? | **UNKNOWN / policy decision required** |
| `PKG-ENV-SRC-014` | What canonicalization profile produces authoritative `spec_hash` values? | **UNKNOWN** |
| `PKG-ENV-SRC-015` | Is generated code permitted, and where should it live? | **NEEDS VERIFICATION** |
| `PKG-ENV-SRC-016` | Which generator/version/provenance format is accepted? | **UNKNOWN** |
| `PKG-ENV-SRC-017` | Is `py.typed` intended, and how is it packaged/tested? | **UNKNOWN** |
| `PKG-ENV-SRC-018` | Which CI checks block hidden I/O, authority imports, profile drift, and packaging failure? | **UNKNOWN** |
| `PKG-ENV-SRC-019` | How are corrected/superseded profiles regenerated and invalidated? | **UNKNOWN** |
| `PKG-ENV-SRC-020` | Is wheel/sdist publication planned, and how is it separated from KFM data publication? | **UNKNOWN** |

[Back to top](#top)

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Current request | **CONFIRMED task authority** | Update this exact source-root README. | Not implementation proof. |
| Prior target README | **CONFIRMED** | Existing helper-only, no-network, finite-outcome, anti-authority, test, and rollback posture. | Planning-oriented and stale relative to current package evidence. |
| `packages/envelopes/pyproject.toml` | **CONFIRMED** | Distribution name and placeholder version. | No build, dependency, Python, discovery, or publication behavior. |
| `src/envelopes/__init__.py` | **CONFIRMED empty file** | Import package scaffold exists. | No exports or behavior. |
| Merged child module README v0.2 | **CONFIRMED repository document** | Detailed candidate-builder semantics, profile drift, finite failures, evidence/policy/release boundaries. | Does not establish executable code or consumers. |
| Parent package README | **CONFIRMED repository document / stale planning posture** | Package-level helper intent. | Does not prove implementation and contains older assumptions. |
| Exact absent-path checks | **CONFIRMED bounded absence** | `package.json`, selected helper modules, and package-specific test/fixture READMEs were absent at tested paths. | Not exhaustive tree proof. |
| RuntimeResponseEnvelope contract/schema | **CONFIRMED paired draft surfaces** | Current required closed field set and finite outcomes. | Status is `PROPOSED`; conflicts with architecture prose. |
| DecisionEnvelope contract/schema | **CONFIRMED paired draft surfaces** | Current required fields, outcomes, policy families, and compatibility fields. | Status is `PROPOSED`; conflicts with older decision vocabulary. |
| Runtime envelope fixture READMEs | **CONFIRMED minimal fixtures** | One valid and one invalid case for each paired schema. | Narrow schema coverage only. |
| Dedicated validators | **CONFIRMED files** | Validator entry points and exact schema/fixture paths. | Execution and package integration not proven by file presence. |
| Common schema harness | **CONFIRMED test code** | Discovers contract-schema fixture families. | Not package-specific; current run not claimed here. |
| Schema-validation workflow | **CONFIRMED workflow definition** | Repository CI path exists. | Package-specific enforcement remains unknown. |
| `runtime/envelopes/README.md` | **CONFIRMED repository document** | Separate runtime helper-note/handoff lane. | Does not settle implementation ownership. |
| Governed API envelope architecture | **CONFIRMED repository document / draft** | Rich envelope concept, finite outcomes, reason-code posture. | Field surface conflicts with paired schema. |
| ADR-0019 | **CONFIRMED file / PROPOSED ADR** | Provider-neutral, finite-outcome, no-generated-truth direction. | Explicitly not accepted authority. |
| Directory Rules v1.4 | **CONFIRMED placement doctrine** | `packages/` responsibility and authority-root separation. | Some ADR/path decisions remain proposed. |
| Indexed repository search | **CONFIRMED bounded search** | Did not establish production package consumers. | Search is not exhaustive runtime proof. |

[Back to top](#top)

---

## Maintainer checklist

Before changing this source root or adding code:

- [ ] Confirm owner and review burden.
- [ ] Confirm package-versus-runtime implementation ownership.
- [ ] Pin the envelope profile and authority documents.
- [ ] Update packaging/discovery intentionally.
- [ ] Keep imports side-effect-free.
- [ ] Preserve dependency direction.
- [ ] Add tests before exports.
- [ ] Reuse schema fixtures without creating parallel authority.
- [ ] Document generated-code provenance.
- [ ] Run schema, package, security, and packaging checks.
- [ ] Record compatibility, correction, and rollback.
- [ ] Keep public clients behind governed runtime/API envelopes.
- [ ] Update affected package/module/runtime docs when behavior changes.

`packages/envelopes/src/` is a verified source-layout container, not yet a verified envelope library. Its next sound change is a small, profile-pinned, test-first package foundation after governance resolves the current profile and ownership conflicts.

<p align="right"><a href="#top">Back to top</a></p>
