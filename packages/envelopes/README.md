<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-envelopes-readme
title: packages/envelopes/ — Governed Finite-Outcome Envelope Helper Package
type: readme
version: v0.2
status: draft; repository-grounded; python-package-scaffold; non-authoritative
owners:
  - OWNER_TBD — Envelopes package owner
  - OWNER_TBD — Runtime and governed API steward
  - OWNER_TBD — Contract and schema steward
  - OWNER_TBD — Policy, rights, and sensitivity steward
  - OWNER_TBD — Evidence, citation, release, and correction steward
  - OWNER_TBD — Validator, security, packaging, and docs steward
created: NEEDS VERIFICATION — target file existed before this revision
updated: 2026-07-15
supersedes: v1 planning-oriented package guide (2026-06-14)
policy_label: public; packages; envelopes; python; finite-outcomes; no-network-by-default; fail-closed; evidence-ref-aware; non-authoritative
path: packages/envelopes/README.md
truth_posture: CONFIRMED target and prior blob, packages root contract, kfm-envelopes 0.0.0 metadata, Python src layout, merged source-root and child-module v0.2 contracts, empty initializer, bounded absence of tested helper modules and package.json, runtime/envelopes lane, fielded closed RuntimeResponseEnvelope and DecisionEnvelope schemas, paired draft contracts, validator entry points, fixture roots, common schema harness, Directory Rules v1.4, draft/proposed ADR-0019, and schema-validation workflow / PROPOSED future deterministic envelope candidate builders, local invariant guards, generated adapters, compatibility adapters, package tests, explicit exports, registry distribution, and governed consumers / CONFLICTED architecture-envelope prose versus current paired schema fields, DecisionEnvelope policy-style vocabulary versus schema finite outcomes, package implementation versus runtime/envelopes ownership, and package-specific versus contract-schema test/fixture placement / UNKNOWN build backend, Python requirement, dependencies, package discovery, license metadata, public exports, import consumers, runtime/API wiring, package-specific CI, registry publication, release integration, and production behavior / NEEDS VERIFICATION accepted owners, canonical envelope profiles, reason-code/state vocabularies, schema/contract acceptance, generation provenance, compatibility policy, correction invalidation, and rollback integration
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: cbc65b4bd3f7ecd7cb55cbae97da564cad5b5546
  prior_blob: c0eb5e305c17d70aa0acb92d5c711a27f5684161
  source_root_blob: 308fcea29b790064f1911243cde2094ebb3ae347
  source_module_blob: 72d2ecdab6b056f6eb7efdd66a39fa5b0b27c8cf
related:
  - ./pyproject.toml
  - ./src/README.md
  - ./src/envelopes/README.md
  - ./src/envelopes/__init__.py
  - ../README.md
  - ../../runtime/envelopes/README.md
  - ../../contracts/runtime/runtime_response_envelope.md
  - ../../contracts/runtime/decision_envelope.md
  - ../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
  - ../../schemas/contracts/v1/runtime/decision_envelope.schema.json
  - ../../fixtures/contracts/v1/runtime/runtime_response_envelope/README.md
  - ../../fixtures/contracts/v1/runtime/decision_envelope/README.md
  - ../../tools/validators/validate_runtime_response_envelope.py
  - ../../tools/validators/validate_decision_envelope.py
  - ../../tests/schemas/test_common_contracts.py
  - ../../docs/architecture/governed-api/ENVELOPES.md
  - ../../docs/adr/ADR-0019-ai-adapter-contract-and-finite-envelopes.md
  - ../../docs/doctrine/directory-rules.md
  - ../../.github/workflows/schema-validation.yml
tags: [kfm, packages, envelopes, python, package-boundary, runtime-response-envelope, decision-envelope, finite-outcomes, profiles, evidence-ref, policy-state, freshness, correction-state, deterministic, no-network, fail-closed, rollback]
notes:
  - "v0.2 replaces stale planning language with a commit-pinned description of the current kfm-envelopes 0.0.0 Python package scaffold."
  - "The merged src/README.md and src/envelopes/README.md v0.2 documents own source-root and candidate-builder detail; this file owns the package-level responsibility, consumer, packaging, compatibility, and trust-boundary contract."
  - "The import package initializer is empty and tested helper-module paths are absent; no supported API, build behavior, consumer, or runtime integration is claimed."
  - "Current architecture prose and paired runtime schemas conflict; the package requires explicit profile selection and forbids silent compatibility invention."
  - "Only this Markdown file changes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Finite-Outcome Envelope Helper Package

`packages/envelopes/`

> Shared Python package boundary for reusable, deterministic, side-effect-minimal helpers that may prepare finite-outcome envelope **candidates**. The current repository surface is a **greenfield `0.0.0` scaffold**, not an implemented envelope library: package metadata is minimal, the import initializer is empty, no supported exports or consumers are established, and contract/schema drift must be resolved before a stable API is declared.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.2-informational)
![distribution](https://img.shields.io/badge/distribution-kfm--envelopes-3776ab)
![implementation](https://img.shields.io/badge/implementation-placeholder-lightgrey)
![outcomes](https://img.shields.io/badge/outcomes-ANSWER%20%7C%20ABSTAIN%20%7C%20DENY%20%7C%20ERROR-6f42c1)
![network](https://img.shields.io/badge/network-none%20by%20default-455a64)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-0b7285)

**Quick links:** [Purpose](#purpose-and-audience) · [Status](#current-repository-state) · [Context](#package-bounded-context) · [Placement](#placement-and-authority) · [Package map](#current-package-surface) · [Responsibilities](#owned-responsibilities) · [Exclusions](#explicit-non-ownership) · [Root/module split](#package-source-root-and-module-split) · [Runtime lane](#package-versus-runtime-envelope-lane) · [Profiles](#contract-schema-and-architecture-drift) · [Objects](#envelope-object-family-boundary) · [Inputs](#accepted-inputs) · [Outputs](#permitted-outputs) · [Consumers](#consumer-and-public-interface-boundary) · [Dependencies](#dependency-direction) · [Identity/time](#identity-time-hash-and-version-posture) · [Trust](#lifecycle-evidence-policy-release-and-public-safety) · [Failures](#failure-and-error-semantics) · [Security](#security-privacy-and-data-minimization) · [Packaging](#packaging-distribution-and-versioning) · [Tests](#tests-fixtures-validators-and-ci) · [Evolution](#implementation-admission-sequence) · [Compatibility](#compatibility-correction-and-rollback) · [Done](#definition-of-done) · [Backlog](#open-verification-register) · [Ledger](#evidence-ledger)

> [!IMPORTANT]
> **Repository snapshot:** `main@cbc65b4bd3f7ecd7cb55cbae97da564cad5b5546`<br>
> **Distribution:** `kfm-envelopes`<br>
> **Declared version:** `0.0.0`<br>
> **Verified source root:** `src/`<br>
> **Verified import package:** `src/envelopes/`<br>
> **Verified implementation:** empty `src/envelopes/__init__.py`; tested helper modules were absent<br>
> **Verified child contracts:** [`src/README.md`](./src/README.md) v0.2 and [`src/envelopes/README.md`](./src/envelopes/README.md) v0.2<br>
> **Build backend, Python requirement, dependencies, package discovery, exports, consumers, and package publication:** not established<br>
> **Runtime schemas/contracts:** present but `PROPOSED`, with documented architecture/schema and vocabulary drift

> [!CAUTION]
> A package is not an authority surface. A schema-valid object is not evidence closure. An `ANSWER` value is not disclosure permission. A `DecisionEnvelope` is not policy execution. A reference is not the referenced object. A release reference is not release approval. A package import is not the public trust membrane.

---

## Purpose and audience

`packages/envelopes/` is the package-level boundary for reusable envelope helper implementation.

A mature package may provide deterministic or side-effect-minimal support for:

- finite outcome constants bound to an accepted envelope profile;
- candidate construction for `RuntimeResponseEnvelope`;
- candidate construction for `DecisionEnvelope`;
- local invariant checks that are unambiguously defined by an accepted schema profile;
- explicit profile and version selection;
- preservation of ids, hashes, times, reason codes, evidence refs, policy state, freshness, and correction state;
- compatibility adapters between explicitly accepted versions;
- generated schema adapters with provenance;
- deterministic issue/result carriers;
- synthetic, public-safe, no-network fixtures;
- package-level imports used by more than one governed internal consumer.

This package is for:

- envelope package maintainers;
- governed runtime and API maintainers;
- contract, schema, policy, evidence, citation, release, and correction stewards;
- validators and test maintainers;
- security, privacy, packaging, and dependency reviewers;
- application, pipeline, tool, and domain-package authors considering this package as a dependency;
- reviewers deciding whether proposed behavior belongs in a shared package, runtime lane, validator, policy engine, evidence resolver, release workflow, or application.

It must not fetch sources, evaluate policy, resolve evidence, write lifecycle state, create receipts/proofs, approve release, orchestrate runtime services, expose public routes, render UI/map content, call model providers, or make generated language true.

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
| Base commit | `cbc65b4bd3f7ecd7cb55cbae97da564cad5b5546` |
| Prior target blob | `c0eb5e305c17d70aa0acb92d5c711a27f5684161` |
| Source-root blob | `308fcea29b790064f1911243cde2094ebb3ae347` |
| Source-module blob | `72d2ecdab6b056f6eb7efdd66a39fa5b0b27c8cf` |
| Current revision | documentation-only package v0.2 proposal |

### Verified package surface

| Surface | Evidence at snapshot | Status | Consequence |
|---|---|---:|---|
| This README | Existing v1 planning-oriented package guide. | **CONFIRMED** | Revised in place. |
| [`pyproject.toml`](./pyproject.toml) | Declares `[project]`, name `kfm-envelopes`, and version `0.0.0` only. | **CONFIRMED minimal placeholder** | Distribution identity is known; build and dependency behavior are not. |
| [`src/README.md`](./src/README.md) | Merged repository-grounded source-root contract v0.2. | **CONFIRMED** | Source layout, imports, packaging, generated-code, and test-placement boundaries are grounded. |
| [`src/envelopes/README.md`](./src/envelopes/README.md) | Merged repository-grounded source-module contract v0.2. | **CONFIRMED** | Candidate-builder, object-family, failure, safety, and profile-drift detail lives there. |
| `src/envelopes/__init__.py` | Exists and is empty. | **CONFIRMED** | Import-package marker only; no public exports are established. |
| `package.json` | Absent at `packages/envelopes/package.json` during the source-root review. | **CONFIRMED bounded absence** | Do not claim a JavaScript/TypeScript package. |
| Selected helper modules | `outcomes.py`, `runtime_response.py`, `decision.py`, and `validation.py` were absent at exact tested paths. | **CONFIRMED bounded absence** | No executable envelope helper implementation is established. |
| Build backend | No `[build-system]` section was observed. | **NOT OBSERVED** | Build/install behavior remains unknown. |
| Dependencies | No dependency list was observed. | **NOT OBSERVED** | Do not claim `jsonschema`, API, runtime, or generated-model dependencies. |
| Supported Python versions | No `requires-python` field was observed. | **NOT OBSERVED** | Interpreter support is unknown. |
| Package discovery | No explicit discovery configuration was observed. | **NOT OBSERVED** | Editable install and wheel inclusion are unproven. |
| Public exports | Empty initializer. | **NOT ESTABLISHED** | No symbol is part of a supported package API. |
| Consumers | Indexed searches did not establish production imports of `envelopes`. | **NOT OBSERVED / search-limited** | Do not claim runtime/API integration. |
| `runtime/envelopes/` | README-backed runtime helper-note/handoff lane exists. | **CONFIRMED documentation lane** | Implementation ownership must be resolved before parallel code appears. |
| RuntimeResponseEnvelope contract/schema | Paired draft contract and fielded closed schema exist. | **CONFIRMED surfaces / `PROPOSED` status** | Builders must bind to an explicit accepted profile. |
| DecisionEnvelope contract/schema | Paired draft contract and fielded closed schema exist. | **CONFIRMED surfaces / `PROPOSED` status** | Older decision vocabulary cannot be assumed compatible. |
| Dedicated validators | Thin entry points load the paired schemas and fixture roots. | **CONFIRMED files** | Presence does not prove package behavior. |
| Runtime fixture families | One documented valid and one invalid fixture exist for each paired schema. | **CONFIRMED minimal coverage** | Coverage is narrow and schema-only. |
| Generic schema harness | `tests/schemas/test_common_contracts.py` discovers runtime fixtures. | **CONFIRMED test code** | Package-level tests are not established. |
| Package test README | `tests/packages/envelopes/README.md` was absent at the exact tested path. | **CONFIRMED bounded absence** | No package-specific test lane is documented there. |
| Package fixture README | `fixtures/packages/envelopes/README.md` was absent at the exact tested path. | **CONFIRMED bounded absence** | No package-specific fixture lane is documented there. |
| Schema workflow | `.github/workflows/schema-validation.yml` installs the repository root and runs `make schemas`. | **CONFIRMED workflow definition** | Package-specific enforcement is unknown. |
| Runtime/release evidence | No deployed consumer, runtime log, receipt, release artifact, package registry artifact, or public response was inspected. | **UNKNOWN** | This README is not implementation, deployment, or publication proof. |

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
package registry publication             = UNKNOWN
release behavior                         = UNKNOWN
```

[Back to top](#top)

---

## Package bounded context

The bounded context is:

> The package-level ownership, admission, compatibility, distribution, and consumer boundary for reusable envelope helper implementation.

It includes:

- package identity and metadata;
- source-root organization;
- import package and supported exports;
- package discovery and build configuration;
- dependency direction;
- public-versus-internal API designation;
- schema-profile pinning;
- generated-code provenance;
- package-level tests and fixture integration;
- consumer compatibility;
- deprecation and migration;
- package distribution and integrity;
- correction and rollback posture.

It excludes:

- envelope semantic meaning;
- canonical schema shape;
- policy evaluation;
- source admission;
- evidence resolution and closure;
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
| Import package | `src/envelopes/` Python namespace. | Supported public API. |
| Envelope candidate | Local object prepared for later validation and governed handling. | Public response or release-approved artifact. |
| Envelope profile | Explicit contract/schema/version/hash combination. | “Latest” inferred from ambient repository state. |
| Local invariant | Rule checkable without I/O or authority decisions. | Policy evaluation, evidence sufficiency, or release approval. |
| Compatibility adapter | Explicit, tested conversion between accepted profiles. | Silent field renaming or best-effort coercion. |
| Generated adapter | Derived code tied to a schema version and generation receipt. | New semantic or schema authority. |
| Package release | Distribution of helper code. | Publication of KFM data or claims. |
| Consumer | Internal code that imports the supported package API. | Public client calling package internals. |

[Back to top](#top)

---

## Placement and authority

Directory Rules classify `packages/` as the responsibility root for shared reusable implementation.

```text
packages/envelopes/                    = package-level boundary
packages/envelopes/src/                = Python source-root container
packages/envelopes/src/envelopes/      = import package
runtime/envelopes/                     = runtime note/handoff lane
contracts/runtime/                     = semantic meaning
schemas/contracts/v1/runtime/          = machine shape
policy/runtime/                        = runtime policy
fixtures/contracts/v1/runtime/         = schema fixtures
tools/validators/                      = validator implementations
tests/                                 = enforceability
data/                                  = lifecycle, receipts, proofs
release/                               = release/correction/rollback authority
apps/                                  = deployable and public-serving boundaries
```

| Question | Answer | Status |
|---|---|---|
| Why `packages/envelopes/`? | Envelope helper logic may be reused by multiple governed internal consumers. | **CONFIRMED placement pattern / implementation PROPOSED** |
| Does the package define envelope meaning? | No. Semantic contracts remain under `contracts/runtime/`. | **CONFIRMED boundary** |
| Does the package define schema shape? | No. Schemas remain under `schemas/contracts/v1/runtime/`. | **CONFIRMED boundary** |
| Can it evaluate policy? | No. It may preserve policy outputs supplied by callers. | **CONFIRMED boundary** |
| Can it resolve evidence? | No. It may preserve references only. | **CONFIRMED boundary** |
| Can it approve or perform release? | No. Package and data publication remain separate governed processes. | **CONFIRMED boundary** |
| Can public clients import it? | No. Public clients consume governed runtime/API envelopes. | **CONFIRMED trust-membrane posture** |
| Does `runtime/envelopes/` replace this package? | Not decided. The final implementation boundary requires review/ADR. | **CONFLICTED / NEEDS VERIFICATION** |

[Back to top](#top)

---

## Current package surface

```text
packages/envelopes/
├── README.md
├── pyproject.toml
└── src/
    ├── README.md
    └── envelopes/
        ├── README.md
        └── __init__.py
```

The tree above is the bounded verified surface used by the current child contracts. It is not an exhaustive proof that no unindexed or empty file exists.

### Package control layers

| Layer | File/path | Responsibility |
|---|---|---|
| Package | `README.md` | Package identity, responsibility, consumers, compatibility, distribution, and trust boundary. |
| Project metadata | `pyproject.toml` | Current project name/version placeholder. |
| Source root | `src/README.md` | Discovery, import, dependency, generated-code, packaging, and test-placement boundary. |
| Import module | `src/envelopes/README.md` | Candidate-builder semantics, object-family boundary, local failures, safety, and profile handling. |
| Import marker | `src/envelopes/__init__.py` | Empty namespace marker; no supported exports. |

[Back to top](#top)

---

## Owned responsibilities

A future mature package may own implementation for:

- explicit envelope-profile identifiers;
- finite outcome constants or enums tied to an accepted profile;
- deterministic package-local issue and result types;
- local candidate construction;
- local required-field and value-shape guards;
- explicit closed-field rejection;
- explicit compatibility adapters;
- deterministic identity and hash syntax helpers;
- safe reason-code syntax helpers after vocabulary governance exists;
- preservation of caller-supplied evidence refs, policy state, freshness, correction state, obligations, and timestamps;
- generated models/adapters with pinned schema provenance;
- package-local import and export behavior;
- package-level compatibility and deprecation;
- package distribution metadata and integrity;
- package tests and synthetic/public-safe fixtures.

A good package-placement test:

> Behavior may belong here when multiple governed internal consumers need it, the logic is deterministic and side-effect-minimal, it does not decide truth/admissibility/release, and it can be validated without network, stores, providers, or hidden state.

[Back to top](#top)

---

## Explicit non-ownership

| This package does not own | Correct responsibility |
|---|---|
| Envelope semantic contracts | `contracts/runtime/` |
| Canonical JSON Schemas | `schemas/contracts/v1/runtime/` |
| Policy rules and evaluation | `policy/` and governed policy runtime |
| Reason-code authority registry | Accepted contract/schema/policy or governed API registry |
| EvidenceRef resolution | Evidence resolver/runtime evidence lanes |
| EvidenceBundle construction or storage | Proof/evidence homes |
| Source acquisition, admission, rights review | Connectors, source registry, and review lanes |
| Lifecycle data and promotion | `data/`, pipelines, promotion/release workflows |
| Receipt/proof creation, signing, persistence | Receipt/proof homes |
| ReleaseManifest, correction, withdrawal, rollback mutation | `release/` |
| Runtime service orchestration | `runtime/` and deployable applications |
| Public API routes and final serialization | Governed API application |
| UI, MapLibre, Evidence Drawer, Focus Mode rendering | UI/application roots |
| Model providers, prompts, inference, completions | Governed AI runtime behind evidence and policy |
| Claim truth or public disclosure permission | Evidence, policy, review, release, and governed runtime |

Disallowed authority verbs in the supported package API include:

```text
approve_release
publish
promote
evaluate_policy
decide_sensitivity
resolve_evidence_bundle
create_evidence_bundle
store_proof
sign_receipt
fetch_source
call_model
generate_answer
is_true
canonicalize_fact
```

[Back to top](#top)

---

## Package, source-root, and module split

The three README contracts have distinct scopes:

| Contract | Owns | Defers |
|---|---|---|
| `packages/envelopes/README.md` | Package identity, high-level responsibility, consumers, compatibility, packaging/distribution, public boundary, review and rollback. | Source layout and detailed helper semantics. |
| `packages/envelopes/src/README.md` | Source layout, discovery, imports, dependencies, generated code, test placement, build/install posture. | Detailed object-family helper behavior. |
| `packages/envelopes/src/envelopes/README.md` | Candidate-builder semantics, local invariants, profile drift, object-family handling, failures, data minimization. | Package distribution and authority roots. |

A change that alters supported exports or consumer compatibility normally requires all affected layers to be reviewed together.

[Back to top](#top)

---

## Package versus runtime envelope lane

Two confirmed paths mention envelope helpers:

```text
packages/envelopes/      # reusable package boundary
runtime/envelopes/       # runtime helper-note and handoff lane
```

Until an accepted architecture decision settles implementation ownership:

- package code should remain reusable, pure, and runtime-agnostic;
- runtime orchestration, service context, adapter state, operational configuration, request context, and handoff notes remain outside the package;
- `runtime/envelopes/` must not become a parallel implementation of the same supported API;
- this package must not absorb provider clients, service containers, credentials, deployment configuration, or runtime-global state;
- callers must use one reviewed implementation surface;
- any migration must identify canonical owner, compatibility window, dependent consumers, deletion target, tests, docs, and rollback.

**Status:** both paths are `CONFIRMED`; implementation ownership is `CONFLICTED / NEEDS VERIFICATION`.

[Back to top](#top)

---

## Contract, schema, and architecture drift

The repository currently contains envelope descriptions that do not fully agree. This blocks a stable package API.

### RuntimeResponseEnvelope conflict

The governed API architecture guide sketches fields such as:

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

The current paired closed schema requires:

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

Because the schema sets `additionalProperties: false`, a builder targeting that profile cannot add architecture-only fields without failing validation.

### DecisionEnvelope conflict

Older architecture prose uses:

```text
allow · deny · restrict · hold · abstain
```

The current paired schema requires:

```text
ANSWER · ABSTAIN · DENY · ERROR
```

and a closed `policy_family`:

```text
promotion · access · render · capability · consent · sensitivity
```

The paired contract treats `decision` as an optional compatibility alias for the same finite outcome vocabulary, not as the older policy-state vocabulary.

### Package posture

Until governance resolves the drift:

1. every builder must name one explicit envelope profile;
2. the paired semantic contract for that profile must be used;
3. mixed-profile objects must be rejected;
4. no architecture-only field may be emitted into a closed schema;
5. `allow`, `hold`, or `restrict` must not be silently mapped to a public outcome;
6. evidence, release, freshness, correction, and obligations must not be collapsed into a simple decision token;
7. a resolution must update contracts, schemas, fixtures, validators, docs, package code, tests, and consumers together;
8. compatibility mappings must state lossiness and removal plans.

[Back to top](#top)

---

## Envelope object-family boundary

| Object/family | Permitted package role | Forbidden collapse |
|---|---|---|
| `RuntimeResponseEnvelope` | Construct and locally check a profile-specific candidate. | Public response authority, payload store, or release approval. |
| `DecisionEnvelope` | Preserve finite outcome, policy family, reasons, obligations, evidence refs, and times from governed inputs. | Policy engine, PromotionDecision, ReleaseManifest, or truth decision. |
| `DomainFeatureEnvelope` | No supported package API until accepted contract/schema/ADR exists. | Generic domain payload that flattens source role, sensitivity, ownership, time, evidence, or geometry precision. |
| `EvidenceRef` | Preserve caller-supplied reference shape. | Evidence resolution or EvidenceBundle closure. |
| `EvidenceBundle` | Carry a reference when an accepted profile allows it. | Proof creation or storage. |
| `PolicyDecision` | Preserve a caller-supplied reference/state/obligation. | Policy execution or override. |
| `AIReceipt` / `RunReceipt` | Preserve references where an accepted profile allows. | Receipt creation, signing, persistence, or hidden reasoning. |
| `ReleaseManifest` / `RollbackCard` | Preserve references where an accepted profile allows. | Release, withdrawal, correction, rollback, or publication authority. |
| Reason code | Validate stable syntax/vocabulary when accepted. | Free-text denial, raw exception, secret, PII, policy internals, or chain-of-thought. |
| Trace context | Preserve explicit correlation fields when in profile. | Complete private reasoning or provider payload. |

`DomainFeatureEnvelope` remains `PROPOSED / OPEN ADR`; it must not be exported or implemented based on prose alone.

[Back to top](#top)

---

## Accepted inputs

Inputs must be explicit, governed by their owning systems, and compatible with the selected profile.

| Input family | Accepted posture | Package obligation |
|---|---|---|
| Profile | Explicit contract/schema/version/hash identifier. | Reject unknown or mixed profiles. |
| Identity | Caller-supplied id or accepted deterministic key inputs. | Validate syntax; do not embed secrets or sensitive facts. |
| Outcome | Closed finite value for the selected profile. | Reject null, unknown, lowercase, or provider-specific statuses. |
| Reason | Stable code and safe structured reasons. | Preserve; do not invent policy explanations. |
| Evidence | EvidenceRef values from a governed caller. | Preserve only; do not resolve or fabricate. |
| Policy | Policy family/state/reasons/obligations supplied by policy/runtime systems. | Preserve; do not evaluate, downgrade, or waive. |
| Freshness | Explicit caller-supplied freshness posture. | Do not recompute from hidden source access. |
| Correction | Explicit correction/withdrawal/supersession posture. | Preserve; do not mutate release/correction state. |
| Time | Explicit issuance/evaluation times or injected clock. | Preserve time kind; avoid hidden wall-clock dependence. |
| Hash/version | Explicit profile/version/spec hash. | Validate syntax; do not invent authoritative hashes. |
| Release/receipt refs | Explicit refs when supported by a selected profile. | Preserve only; do not create or approve target objects. |
| Fixture inputs | Synthetic or public-safe values. | Mark fixture scope and prevent production use. |

The package must not fetch missing values from networks, stores, model providers, environment credentials, UI state, mutable globals, or operator memory.

[Back to top](#top)

---

## Permitted outputs

The package may eventually return:

- profile-specific candidate mappings or immutable value objects;
- deterministic local issue lists;
- compatibility results naming source and target profiles;
- schema-ready candidate data after local checks;
- generated models tied to a schema provenance record;
- synthetic/public-safe fixture candidates;
- explicit unsupported/invalid results.

It must not return:

- final public HTTP responses;
- approved policy or release results;
- EvidenceBundles or resolved-evidence assertions;
- durable receipts or proofs;
- lifecycle promotion outcomes;
- model-generated answers;
- UI/map-ready objects that bypass governed API projection;
- ambiguous success booleans that hide profile selection and issues.

### Proposed package-local result

The following is **PROPOSED**, not implemented or canonical:

```python
from dataclasses import dataclass
from typing import Generic, Literal, TypeVar

T = TypeVar("T")

@dataclass(frozen=True)
class EnvelopeIssue:
    code: str
    field: str | None = None
    detail: str | None = None

@dataclass(frozen=True)
class EnvelopeCandidateResult(Generic[T]):
    status: Literal["CANDIDATE", "INVALID", "UNSUPPORTED", "ERROR"]
    profile: str
    value: T | None
    issues: tuple[EnvelopeIssue, ...]
```

Package-local status must remain distinct from public `RuntimeResponseEnvelope.outcome`.

[Back to top](#top)

---

## Consumer and public interface boundary

### Potential internal consumers

Future governed consumers may include:

- governed API assemblers;
- runtime response adapters;
- policy/runtime handoff code;
- evidence-aware response composition;
- validators and contract tests;
- domain packages preparing candidate response objects;
- command-line validation tools;
- synthetic fixture builders.

No consumer is currently established from inspected import evidence.

### Public boundary

Public clients must not import or execute this package directly.

```text
internal governed inputs
  -> package candidate helper
  -> authoritative schema validation
  -> policy/evidence/release/runtime gates
  -> governed API/runtime serializer
  -> public client
```

Blocked:

```text
browser or public client
  -> packages/envelopes internals
  -> canonical/lifecycle/evidence stores
  -> model provider
```

The package may help standardize the trust membrane. It does not replace it.

[Back to top](#top)

---

## Dependency direction

Preferred direction:

```text
contracts + schemas + governed policy/evidence/release outputs
                              |
                              v
                    governed internal caller
                              |
                              v
                     packages/envelopes
                              |
                              v
                 authoritative schema validator
                              |
                              v
                    runtime/API trust membrane
                              |
                              v
                         public client
```

Allowed future dependencies, after review:

- Python standard library;
- accepted shared value types;
- generated schema models with provenance;
- an explicit JSON Schema library if packaging and dependency policy accepts it;
- narrow internal utilities that do not reverse authority.

Forbidden dependencies:

- source connectors;
- lifecycle/canonical stores;
- policy engines;
- evidence/proof stores;
- receipt writers;
- release writers;
- model-provider clients;
- API routers or service containers;
- UI/map components;
- credentials or deployment configuration.

Authority roots must not depend on this package to define their own meaning or validity.

[Back to top](#top)

---

## Identity, time, hash, and version posture

### Identity

Envelope ids must:

- satisfy the selected schema pattern;
- remain stable enough for audit, replay detection, correction, and client reconciliation;
- not encode secrets, raw prompts, private facts, exact protected locations, credentials, or unrestricted source values;
- distinguish response-envelope ids from decision-envelope ids;
- carry identity-profile version when deterministic construction is introduced.

Any deterministic-id recipe remains `PROPOSED` until canonicalization, namespace, collision handling, and versioning are accepted.

### Time

Keep time kinds distinct:

- `issued_at` is envelope issuance time;
- `evaluated_at` is decision evaluation time;
- source observation/valid/publication times belong to source/domain objects;
- freshness is a governed posture, not a timestamp alias;
- correction state is not a timestamp;
- release time belongs to release records.

Do not rewrite times to make stale, corrected, or superseded responses appear current.

### Hashes

The current RuntimeResponseEnvelope schema constrains `spec_hash` syntax. Authoritative computation requires an accepted content boundary and canonical serialization.

Until that exists, the package may:

- preserve caller-supplied hashes;
- validate syntax;
- expose profile/version mismatch issues.

It must not claim to produce authoritative hashes from unspecified content.

### Versioning

Three version dimensions may differ:

```text
package version
envelope schema/profile version
object instance version
```

Do not collapse them. Compatibility tests must name all relevant versions.

[Back to top](#top)

---

## Lifecycle, evidence, policy, release, and public safety

The lifecycle invariant remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

This package is outside lifecycle storage and promotion authority.

### Evidence

The package may preserve EvidenceRef values. It must not:

- resolve evidence from canonical/internal stores;
- create EvidenceBundles;
- claim refs are admissible, current, complete, or sufficient;
- fabricate citations;
- expose restricted evidence in reasons or diagnostics;
- turn unresolved evidence into `ANSWER` by convenience.

### Policy, rights, and sensitivity

The package may preserve policy fields. It must not:

- evaluate audience, access, render, capability, consent, sensitivity, or promotion policy;
- downgrade obligations;
- expose policy internals;
- infer disclosure permission from an outcome token;
- silently convert `hold` or `restrict` to a public outcome.

### Release and correction

The package may preserve supported refs/states. It must not:

- create or approve a ReleaseManifest;
- publish or promote data;
- withdraw, correct, supersede, or roll back a release;
- hide stale or correction-affected state;
- equate package distribution with KFM data publication.

### Public-safe behavior

Fail closed when:

- profile selection is ambiguous;
- schema/contract status is unresolved;
- policy mapping is not accepted;
- evidence is insufficient or unresolved;
- release support is missing;
- freshness or correction posture is unknown;
- rights/sensitivity posture is unavailable;
- compatibility would be lossy and unapproved.

[Back to top](#top)

---

## Failure and error semantics

Failures must be finite, explicit, deterministic where practical, and safe.

### Proposed package issue families

```text
profile/unsupported
profile/mixed-fields
schema/required-field-missing
schema/field-not-allowed
schema/value-pattern-invalid
schema/outcome-invalid
schema/policy-family-invalid
identity/invalid
hash/invalid-syntax
time/invalid
compatibility/no-mapping
compatibility/lossy
reference/invalid-shape
dependency/missing
internal/unexpected
```

Rules:

- package issues do not decide public outcomes;
- no fatal issue may be hidden behind a “successful” candidate;
- raw exceptions may be chained internally but must not leak publicly;
- `ABSTAIN`, `DENY`, and `ERROR` are not interchangeable;
- no helper may catch every exception and fabricate an apparently valid `ERROR` envelope without required governed context;
- diagnostics must exclude secrets, credentials, raw prompts, chain-of-thought, private records, protected locations, and unrestricted evidence.

When ambiguity affects authority, return `UNSUPPORTED` or `INVALID` locally and require the governed caller to select a safe public outcome.

[Back to top](#top)

---

## Security, privacy, and data minimization

Future implementation should be no-network and no-secret by default.

Required controls:

- no environment credential reads;
- no model-provider calls;
- no direct canonical/lifecycle/evidence-store reads;
- no filesystem writes except isolated test fixtures or explicit build output;
- no import-time I/O, registration, logging, or mutable global state;
- no logging full envelope inputs by default;
- no sensitive values in ids, reason codes, issue details, reprs, or exceptions;
- bounded input sizes and collection lengths;
- rejection of unknown fields under closed profiles;
- synthetic/public-safe fixtures;
- dependency and supply-chain review;
- deterministic diagnostic redaction;
- explicit license and provenance for generated code;
- no chain-of-thought or raw provider payload retention.

A governed caller is responsible for supplying authorized inputs. The package must still minimize what it retains and returns.

[Back to top](#top)

---

## Packaging, distribution, and versioning

Current project metadata is only:

```toml
[project]
name = "kfm-envelopes"
version = "0.0.0"
```

Before installation or distribution can be claimed, define and validate:

- `[build-system]`;
- supported Python versions;
- package discovery for `src/envelopes`;
- dependencies and optional extras;
- license and project metadata;
- type-marker policy;
- generated-code inclusion/exclusion;
- package data rules;
- reproducible build process;
- source distribution and wheel contents;
- artifact digest/signing/attestation;
- vulnerability and license scanning;
- release notes and compatibility policy;
- rollback/yank procedure;
- separation between package registry publication and KFM data publication.

### Package release is not data release

```text
Python package release
  = distribution of helper implementation

KFM data release
  = governed publication of claims/artifacts under release authority
```

Neither implies the other.

[Back to top](#top)

---

## Tests, fixtures, validators, and CI

### Confirmed validation surfaces

| Surface | Current evidence | Proves | Does not prove |
|---|---|---|---|
| RuntimeResponseEnvelope schema | Fielded, closed, `PROPOSED`. | Machine shape for that profile. | Semantic sufficiency, policy, evidence, release, package behavior. |
| DecisionEnvelope schema | Fielded, closed, `PROPOSED`. | Required fields and finite enums. | Policy correctness or disclosure permission. |
| Dedicated validators | Thin schema/fixture runner entry points. | Validator paths exist. | Package candidate builders exist or are correct. |
| Runtime fixture families | One valid and one invalid case per paired schema. | Minimal positive/negative schema examples. | Broad outcome, security, compatibility, or consumer coverage. |
| Generic schema harness | Discovers contract fixtures. | Repository test code exists. | Package tests exist. |
| Schema workflow | Runs repository schema checks. | CI wiring exists. | Package-specific import/API/compatibility behavior. |

### Proposed package tests

```text
tests/packages/envelopes/
├── test_package_metadata.py
├── test_install_and_import.py
├── test_public_exports.py
├── test_import_safety.py
├── test_runtime_response_candidate.py
├── test_decision_envelope_candidate.py
├── test_profile_rejection.py
├── test_closed_fields.py
├── test_outcomes.py
├── test_policy_families.py
├── test_identity_hash_time.py
├── test_reference_preservation.py
├── test_no_hidden_io.py
├── test_no_authority_imports.py
├── test_sensitive_diagnostics.py
└── test_compatibility.py
```

This tree is `PROPOSED`; verify repository test conventions before creating it.

### Required cases

- package installation and import in supported environments;
- deliberate and minimal `__init__` exports;
- no import-time side effects;
- each supported profile’s valid and invalid shapes;
- each missing required field;
- unknown fields under closed schemas;
- invalid outcomes, policy families, ids, hashes, and date-times;
- mixed architecture and schema profile fields;
- conflicting outcome aliases;
- ambiguous policy mapping;
- malformed/unresolved/restricted evidence refs;
- stale and correction-affected context;
- oversized inputs;
- deterministic repeatability;
- no-network/no-store/no-provider behavior;
- no sensitive leakage;
- no imports from connectors, policy engines, evidence stores, release writers, API routers, UI, or model providers;
- migration and rollback cases for every compatibility adapter.

### Validation commands after implementation exists

```bash
python tools/validators/validate_runtime_response_envelope.py
python tools/validators/validate_decision_envelope.py
pytest -q tests/schemas/test_common_contracts.py
pytest -q tests/packages/envelopes
python -m build packages/envelopes
```

The first three paths exist. The package-test and build commands remain `PROPOSED` until package/test configuration is established.

[Back to top](#top)

---

## Implementation admission sequence

Use the smallest reversible sequence:

1. **Assign owners:** package, runtime/API, contract/schema, policy, evidence/release, security, packaging, and docs.
2. **Resolve implementation ownership:** package versus `runtime/envelopes/`.
3. **Resolve envelope profiles:** reconcile architecture prose, contracts, and schemas through an accepted ADR/migration.
4. **Pin authority:** identify accepted contract and exact schema version/hash.
5. **Complete package metadata:** build backend, Python range, discovery, dependencies, license, and security posture.
6. **Establish package tests:** follow accepted test/fixture conventions without creating a parallel authority root.
7. **Implement one object family:** start with one current-profile candidate builder.
8. **Keep exports narrow:** add only reviewed symbols to `__init__.py`.
9. **Validate locally and in CI:** schema, package, negative, adversarial, no-I/O, and security cases.
10. **Wire one governed consumer:** runtime/API validates again at the trust boundary.
11. **Record release evidence:** versions, hashes, tests, dependencies, known gaps, correction, rollback.
12. **Expand only from observed need:** add other object families or adapters after consumers and tests justify them.

Do not collapse profile resolution, implementation, self-approval, package release, and data release into one unreviewed change.

[Back to top](#top)

---

## Compatibility, correction, and rollback

### Compatibility

Before a stable API exists:

- treat proposed symbols as unstable;
- require explicit profile identifiers;
- reject mixed and unknown profiles;
- do not silently rename fields or map decision vocabularies;
- document source/target profiles, lossiness, obligations, tests, and removal plan for each adapter.

After a stable API exists:

- follow an accepted semantic-versioning policy;
- keep deprecations observable;
- require migration fixtures and consumer tests;
- retain old parsers only when security/governance permit;
- publish compatibility and removal timelines;
- preserve rollback targets.

### Correction

Contract/schema corrections may invalidate prior candidates or package versions. A mature package should let callers:

- identify profile and package versions;
- identify schema/spec hashes;
- detect unsupported or superseded profiles;
- rebuild from original governed inputs;
- distinguish corrected, superseded, withdrawn, and stale states;
- avoid mutating historical receipts/releases in place.

### Rollback triggers

Rollback, disable, or yank a package change if it:

- creates a parallel contract/schema/policy/evidence/release authority;
- accepts mixed or unknown profiles silently;
- maps policy states to public outcomes without accepted rules;
- permits closed-schema extra fields;
- fabricates evidence, release, policy, identity, time, or hashes;
- performs hidden network/store/model/filesystem I/O;
- leaks sensitive data;
- bypasses governed runtime/API validation;
- creates a second implementation beside `runtime/envelopes/` without migration authority;
- breaks consumers without an accepted migration;
- publishes an artifact whose contents or provenance cannot be reproduced.

### Documentation-only rollback target

For this v0.2 README revision, restore prior target blob:

```text
c0eb5e305c17d70aa0acb92d5c711a27f5684161
```

No code, schema, contract, policy, runtime, fixture, test, data, receipt, proof, release, deployment, or package-registry rollback is required for this documentation-only change.

[Back to top](#top)

---

## Definition of done

### This README revision

- [x] Grounds the package in the verified `kfm-envelopes` `0.0.0` scaffold.
- [x] Reconciles package-level guidance with merged source-root and module contracts.
- [x] Records the empty initializer and absence of supported exports/consumers.
- [x] Separates package, source-root, import-module, and runtime-lane responsibilities.
- [x] Preserves finite-outcome, no-network, helper-only, fail-closed posture.
- [x] Surfaces architecture/schema, vocabulary, ownership, and test-placement conflicts.
- [x] Documents consumers, dependencies, identity/time/hash/version, lifecycle, evidence, policy, release, security, testing, packaging, compatibility, correction, and rollback.
- [x] Changes no code, schema, contract, policy, runtime, fixture, test, data, receipt, proof, release, deployment, or package artifact.

### First supported package release

- [ ] Owners and CODEOWNERS review are accepted.
- [ ] Package/runtime implementation ownership is resolved.
- [ ] Envelope profile drift is resolved through accepted governance.
- [ ] Build backend, Python range, dependencies, discovery, license, and security metadata are defined.
- [ ] Public exports and compatibility policy are accepted.
- [ ] At least one real governed consumer exists.
- [ ] Package tests cover positive, negative, ambiguous, conflicting, stale, correction-affected, restricted, unsupported, and no-I/O cases.
- [ ] Schema validators and fixtures pass for pinned profiles.
- [ ] No authority-root or trust-membrane bypass is proven.
- [ ] Correction, migration, deprecation, and rollback are documented.
- [ ] Reproducible package artifacts and integrity evidence are verified.
- [ ] Package registry publication is separated from KFM data publication.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status |
|---|---|---|
| `PKG-ENV-001` | Who owns the package and which CODEOWNERS rule is enforceable? | **UNKNOWN** |
| `PKG-ENV-002` | Does reusable implementation belong here, in `runtime/envelopes/`, or behind another boundary? | **NEEDS VERIFICATION / ADR** |
| `PKG-ENV-003` | Which RuntimeResponseEnvelope field set is canonical? | **CONFLICTED** |
| `PKG-ENV-004` | Which DecisionEnvelope decision vocabulary is canonical? | **CONFLICTED** |
| `PKG-ENV-005` | What is the acceptance status of current paired runtime contracts/schemas? | **NEEDS VERIFICATION** |
| `PKG-ENV-006` | Which reason-code registry and stability policy bind package helpers? | **UNKNOWN** |
| `PKG-ENV-007` | Which vocabularies govern policy state, freshness, and correction state? | **UNKNOWN** |
| `PKG-ENV-008` | What build backend, Python range, discovery, dependencies, and license metadata apply? | **UNKNOWN** |
| `PKG-ENV-009` | Which symbols form the first supported API? | **UNKNOWN** |
| `PKG-ENV-010` | Which internal consumer is the first committed adopter? | **UNKNOWN** |
| `PKG-ENV-011` | Where should package tests and package-specific fixtures live? | **NEEDS VERIFICATION** |
| `PKG-ENV-012` | Which CI checks block import, compatibility, security, and authority drift? | **UNKNOWN** |
| `PKG-ENV-013` | How are policy `hold`/`restrict` states translated to finite public outcomes? | **UNKNOWN / policy decision required** |
| `PKG-ENV-014` | What conditional evidence/payload rules apply per outcome in successor profiles? | **UNKNOWN** |
| `PKG-ENV-015` | Is DomainFeatureEnvelope accepted and schema-backed? | **PROPOSED / OPEN ADR** |
| `PKG-ENV-016` | What canonical serialization produces authoritative spec hashes? | **UNKNOWN** |
| `PKG-ENV-017` | How are corrected/superseded profiles and package versions invalidated and replayed? | **UNKNOWN** |
| `PKG-ENV-018` | Can public clients be proven unable to import package internals or bypass governed APIs? | **NEEDS VERIFICATION** |
| `PKG-ENV-019` | Is package-registry publication planned, and what provenance/signing policy applies? | **UNKNOWN** |
| `PKG-ENV-020` | How is package release operationally separated from data/release authority? | **NEEDS VERIFICATION** |
| `PKG-ENV-021` | Which generated adapters, if any, are permitted and how is generation provenance recorded? | **UNKNOWN** |
| `PKG-ENV-022` | Which vulnerability, license, SBOM, and artifact-integrity gates are required? | **UNKNOWN** |

[Back to top](#top)

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Current request | **CONFIRMED task authority** | Update this exact package README. | Not implementation proof. |
| Prior target README | **CONFIRMED** | Existing helper-only, finite-outcome, no-network, anti-authority, validation, and rollback posture. | Planning-oriented and stale relative to current package/source evidence. |
| `packages/README.md` | **CONFIRMED root contract** | `packages/` is shared reusable implementation and not a public/internal-store shortcut. | Does not define envelope behavior. |
| `pyproject.toml` | **CONFIRMED** | Distribution `kfm-envelopes`, version `0.0.0`. | No build, dependency, discovery, Python, license, or publication behavior. |
| `src/README.md` v0.2 | **CONFIRMED repository document** | Source layout, imports, package discovery, generated code, tests, compatibility, and current scaffold inventory. | Documentation and bounded path evidence, not runtime proof. |
| `src/envelopes/README.md` v0.2 | **CONFIRMED repository document** | Candidate-builder semantics, object boundaries, profile drift, failure and public-safety rules. | Does not establish code, exports, or consumers. |
| Empty `src/envelopes/__init__.py` | **CONFIRMED file** | Import marker exists and exports nothing. | Does not prove installation/discovery. |
| `runtime/envelopes/README.md` | **CONFIRMED repository document** | Separate runtime helper-note/handoff lane. | Does not settle implementation ownership or prove runtime code. |
| RuntimeResponseEnvelope contract/schema | **CONFIRMED paired draft surfaces** | Current closed field profile and finite outcomes. | Status is `PROPOSED`; architecture conflicts and conditional rules remain. |
| DecisionEnvelope contract/schema | **CONFIRMED paired draft surfaces** | Current required fields, finite outcomes, policy families, compatibility fields. | Status is `PROPOSED`; conflicts with older policy-style vocabulary. |
| Governed API envelope guide | **CONFIRMED repository document / draft** | Richer wire-envelope intent and reason-code posture. | Field surface conflicts with current closed schema. |
| ADR-0019 | **CONFIRMED file / PROPOSED ADR** | Provider-neutral and finite-outcome direction. | Explicitly not accepted authority. |
| Validator entry points | **CONFIRMED files** | Exact schema/fixture paths are wired to common runner. | Package behavior and current pass status are separate questions. |
| Runtime fixture READMEs | **CONFIRMED minimal fixture families** | One valid and one invalid case per paired schema. | Narrow schema-only coverage. |
| Common schema harness | **CONFIRMED test code** | Discovers contract fixture families. | Not package-specific. |
| Schema-validation workflow | **CONFIRMED workflow definition** | Repository schema CI path exists. | Package-specific packaging/import/compatibility coverage is unknown. |
| Directory Rules v1.4 | **CONFIRMED placement doctrine** | Responsibility-root split and anti-drift rules. | Some architecture/ADR decisions remain proposed. |
| Indexed search and exact-path checks | **CONFIRMED bounded evidence** | Did not establish helper modules, package tests, or consumers. | Not exhaustive tree or runtime proof. |

[Back to top](#top)

---

## Status summary

`packages/envelopes/` is a verified Python package path with project identity `kfm-envelopes` version `0.0.0`, a `src` layout, and an empty `envelopes` initializer. It is not yet a verified helper library, stable API, installable distribution, runtime service, policy engine, evidence resolver, lifecycle writer, receipt/proof emitter, release authority, public API, UI/map package, model adapter, or truth source. The next sound step is to resolve ownership and envelope-profile drift, then implement one small, profile-pinned, deterministic, no-I/O candidate builder with a real governed consumer and tests.

<p align="right"><a href="#top">Back to top</a></p>
