<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION/packages-envelopes-src-envelopes-readme
title: packages/envelopes/src/envelopes/ — Governed Finite-Outcome Envelope Helper Module
type: readme
version: v0.2
status: draft; repository-grounded; python-source-module; implementation-placeholder; non-authoritative
owners:
  - OWNER_TBD — Envelopes package owner
  - OWNER_TBD — Runtime and governed API steward
  - OWNER_TBD — Contract and schema steward
  - OWNER_TBD — Policy, rights, and sensitivity steward
  - OWNER_TBD — Evidence, citation, and release steward
  - OWNER_TBD — Validator, security, and docs steward
created: NEEDS VERIFICATION — target file existed before this repair but contained only placeholder text
updated: 2026-07-15
policy_label: public; packages; envelopes; python; finite-outcomes; no-network-by-default; evidence-ref-aware; policy-visible; release-aware; fail-closed; non-authoritative
path: packages/envelopes/src/envelopes/README.md
truth_posture: CONFIRMED target and prior blob, package name/version, Python src layout, empty namespace initializer, parent package/source READMEs, runtime envelope lane, fielded closed RuntimeResponseEnvelope and DecisionEnvelope schemas, paired draft semantic contracts, validators, fixture roots, common schema harness, Directory Rules v1.4, draft/proposed ADR-0019, and schema-validation workflow / PROPOSED future deterministic envelope candidate builders, local invariant guards, reference carriers, compatibility adapters, and typed issue/result APIs / CONFLICTED architecture-envelope prose versus current paired schema fields, DecisionEnvelope allow/deny/restrict/hold/abstain prose versus schema finite outcomes, and package namespace versus runtime/envelopes implementation ownership / UNKNOWN build backend, Python requirement, dependencies, public exports, import consumers, package tests, package-specific CI, runtime/API wiring, validator execution results, release integration, and production behavior / NEEDS VERIFICATION accepted owners, canonical reason-code and state vocabularies, schema/contract acceptance status, compatibility policy, evidence-resolution handoff, correction invalidation, and rollback integration
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 63a04206d7cb5c51b6fc45caf684c1c731cc177d
  prior_blob: 71899b1233770534f3f0cadbb61425940684c620
  bounded_module_search: README.md and empty __init__.py confirmed; no supported helper implementation or consumer established
related:
  - ./__init__.py
  - ../README.md
  - ../../README.md
  - ../../pyproject.toml
  - ../../../../runtime/envelopes/README.md
  - ../../../../contracts/runtime/runtime_response_envelope.md
  - ../../../../contracts/runtime/decision_envelope.md
  - ../../../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
  - ../../../../schemas/contracts/v1/runtime/decision_envelope.schema.json
  - ../../../../fixtures/contracts/v1/runtime/runtime_response_envelope/README.md
  - ../../../../fixtures/contracts/v1/runtime/decision_envelope/README.md
  - ../../../../tools/validators/validate_runtime_response_envelope.py
  - ../../../../tools/validators/validate_decision_envelope.py
  - ../../../../tests/schemas/test_common_contracts.py
  - ../../../../docs/architecture/governed-api/ENVELOPES.md
  - ../../../../docs/adr/ADR-0019-ai-adapter-contract-and-finite-envelopes.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../.github/workflows/schema-validation.yml
tags: [kfm, packages, envelopes, python, source-module, runtime-response-envelope, decision-envelope, finite-outcomes, evidence-ref, reason-code, policy-state, freshness, correction-state, deterministic, no-network, fail-closed, rollback]
notes:
  - "v0.2 replaces a planning-oriented namespace guide with a commit-pinned account of the current kfm-envelopes 0.0.0 Python scaffold."
  - "The namespace initializer is empty; no helper modules, supported exports, import consumers, package tests, or runtime bindings are claimed."
  - "RuntimeResponseEnvelope and DecisionEnvelope have fielded, closed, PROPOSED schemas with paired draft contracts, validators, fixtures, and a generic schema harness."
  - "Architecture prose and paired schemas currently disagree on several fields and vocabularies; this README records the conflict and forbids silent compatibility invention."
  - "Only this Markdown file changes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Finite-Outcome Envelope Helper Module

`packages/envelopes/src/envelopes/`

> Python source-module boundary for reusable, deterministic, side-effect-minimal helpers that may assemble **candidate** finite-outcome envelope objects. The current repository surface is a **greenfield `0.0.0` scaffold**, not an implemented envelope library: the namespace initializer is empty, no supported exports or consumers are established, and the current contract/schema surfaces contain unresolved drift that must be settled before a stable API is declared.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.2-informational)
![distribution](https://img.shields.io/badge/distribution-kfm--envelopes-3776ab)
![implementation](https://img.shields.io/badge/helpers-NOT%20IMPLEMENTED-yellow)
![outcomes](https://img.shields.io/badge/outcomes-ANSWER%20%7C%20ABSTAIN%20%7C%20DENY%20%7C%20ERROR-6f42c1)
![network](https://img.shields.io/badge/network-none%20by%20default-455a64)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-0b7285)

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#current-repository-state) · [Vocabulary](#bounded-context-and-ubiquitous-language) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Runtime lane](#package-module-versus-runtime-envelope-lane) · [Drift](#contract-schema-and-architecture-drift) · [RuntimeResponseEnvelope](#runtimeresponseenvelope-helper-boundary) · [DecisionEnvelope](#decisionenvelope-helper-boundary) · [Inputs](#accepted-inputs) · [Outputs](#permitted-outputs) · [Interfaces](#proposed-module-interface) · [Dependencies](#dependency-and-import-direction) · [Determinism](#determinism-identity-time-and-hashing) · [Evidence](#evidence-citation-policy-and-release-boundaries) · [Failures](#failure-and-error-semantics) · [Security](#security-privacy-and-data-minimization) · [Validation](#validation-tests-fixtures-and-ci) · [Admission](#implementation-admission-sequence) · [Compatibility](#compatibility-correction-and-rollback) · [Done](#definition-of-done) · [Backlog](#open-verification-register) · [Ledger](#evidence-ledger)

> [!IMPORTANT]
> **Document status:** draft `v0.2`<br>
> **Repository evidence snapshot:** `main@63a04206d7cb5c51b6fc45caf684c1c731cc177d`<br>
> **Distribution:** `kfm-envelopes` version `0.0.0`<br>
> **Observed module maturity:** empty `envelopes/__init__.py`; no supported public API or executable helper implementation established<br>
> **Machine-shape posture:** current runtime envelope schemas are fielded, closed, and marked `PROPOSED`<br>
> **Public posture:** public clients consume governed API/runtime envelopes; they do not import this module or read canonical, lifecycle, evidence, policy, receipt, proof, or release stores directly

> [!CAUTION]
> A builder is not an authority. A schema-valid object is not evidence closure. An `ANSWER` token is not permission to disclose. A `DecisionEnvelope` is not policy execution. A reference is not the referenced object. A release reference is not release approval. A package import is not the public trust membrane.

---

## Purpose

`packages/envelopes/src/envelopes/` is the internal Python namespace for reusable envelope helper implementation inside the `packages/envelopes/` shared package.

A mature implementation may provide pure or side-effect-minimal helpers for:

- constructing **candidate** `RuntimeResponseEnvelope` objects from explicit caller-supplied values;
- constructing **candidate** `DecisionEnvelope` objects from explicit runtime/policy results;
- enforcing small local invariants that are unambiguous in an accepted schema version;
- preserving finite outcomes without silent nulls, fallthrough, or partial-response leakage;
- preserving stable identifiers, spec hashes, versions, issuance/evaluation times, reason codes, evidence refs, policy state, freshness, and correction state;
- returning deterministic issue lists rather than ambiguous booleans or ad hoc exceptions;
- adapting between explicitly versioned, accepted envelope profiles after compatibility rules exist;
- supporting deterministic, synthetic, no-network tests.

This module must remain subordinate to contract meaning, schema shape, policy, evidence, lifecycle, receipts, release, runtime integration, and governed API serialization.

### Audience

This README is for:

- package and runtime maintainers;
- governed API and AI-runtime maintainers;
- contract, schema, policy, evidence, citation, release, correction, and validator stewards;
- application, pipeline, tool, and test authors considering this package as a dependency;
- security and privacy reviewers;
- reviewers deciding whether proposed behavior belongs here, in `runtime/envelopes/`, in a validator, in policy, or in an application.

[Back to top](#top)

---

## Authority level

**Implementation-bearing package source module, currently scaffolded; non-authoritative for meaning, admissibility, evidence, release, lifecycle, or public serving.**

| Concern | Authority in this module |
|---|---|
| Envelope semantic meaning | **None.** Meaning belongs to `contracts/runtime/` and accepted architecture/ADR decisions. |
| Machine-checkable shape | **None.** Shape belongs to `schemas/contracts/v1/runtime/`. |
| Policy evaluation | **None.** Policy systems decide access, render, capability, consent, sensitivity, and related obligations. |
| Evidence resolution | **None.** Evidence systems resolve `EvidenceRef` to admissible evidence or `EvidenceBundle` support. |
| Source admission | **None.** Connectors, registries, rights review, and admission workflows own source acceptance. |
| Lifecycle promotion | **None.** Promotion is a governed transition outside this package. |
| Receipt/proof creation | **None.** Receipt and proof homes own durable audit objects. |
| Release, correction, withdrawal, rollback | **None.** Release roots and accepted records own those state changes. |
| Public API trust membrane | **None.** Governed runtime/API surfaces validate and serialize public responses. |
| UI/map rendering | **None.** Clients interpret only governed envelopes and obligations. |
| Local helper behavior | **Supporting only.** Code may construct candidates, preserve fields, reject local invalid combinations, and return issues. |

Importing a type, validating JSON, computing a digest, or returning an enum does not transfer authority into this package.

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
| Base commit | `63a04206d7cb5c51b6fc45caf684c1c731cc177d` |
| Prior target blob | `71899b1233770534f3f0cadbb61425940684c620` |
| Current revision | documentation-only v0.2 proposal |

### Verified package/module surface

| Surface | Evidence at snapshot | Status | Consequence |
|---|---|---:|---|
| This README | Existing v1 planning-oriented namespace guide. | **CONFIRMED** | Revised in place; strong boundaries are retained and grounded. |
| Parent package README | `packages/envelopes/README.md` exists. | **CONFIRMED README / stale planning posture** | Parent remains relevant but does not prove implementation. |
| Source-root README | `packages/envelopes/src/README.md` exists. | **CONFIRMED README / stale planning posture** | This file refines the import-module boundary. |
| Python project metadata | `pyproject.toml` declares project `kfm-envelopes`, version `0.0.0`. | **CONFIRMED greenfield placeholder** | Python intent is visible; build and install behavior are not. |
| Build backend | No `[build-system]` block appears in the inspected project file. | **NOT OBSERVED** | Do not claim installability or wheel behavior. |
| Python requirement | No `requires-python` field appears in the inspected project file. | **NOT OBSERVED** | Supported interpreter versions are unknown. |
| Dependencies | No dependency list appears in the inspected project file. | **NOT OBSERVED** | Do not claim `jsonschema`, model, API, or runtime dependencies. |
| Namespace initializer | `src/envelopes/__init__.py` exists and is empty. | **CONFIRMED scaffold** | No public exports or initialization behavior are established. |
| Helper modules | Indexed search established this README and parent source README; no supported helper implementation was identified. | **NOT OBSERVED / search-limited** | Do not claim builders, guards, serializers, or adapters exist. |
| Import consumers | Indexed search did not establish production imports of `envelopes`. | **NOT OBSERVED / search-limited** | Runtime/API integration remains unknown. |
| Package test README | `tests/packages/envelopes/README.md` returned no file at the exact path. | **CONFIRMED absent at tested path** | No package-specific test lane is documented there. |
| Runtime helper lane | `runtime/envelopes/README.md` exists. | **CONFIRMED documentation lane** | Package and runtime responsibilities must not duplicate silently. |
| RuntimeResponseEnvelope schema | Fielded draft schema exists; required fields are closed by `additionalProperties: false`. | **CONFIRMED schema / `PROPOSED` status** | A builder must bind to an explicit schema version. |
| DecisionEnvelope schema | Fielded draft schema exists; finite outcomes and policy families are closed. | **CONFIRMED schema / `PROPOSED` status** | Older decision vocabularies cannot be assumed compatible. |
| RuntimeResponseEnvelope contract | Draft v0.2 contract is paired to the schema. | **CONFIRMED contract document / `PROPOSED`** | Current semantic guidance is more recent than the older package README. |
| DecisionEnvelope contract | Draft v0.2 contract is paired to the schema. | **CONFIRMED contract document / `PROPOSED`** | Current semantic guidance aligns with the paired schema. |
| Dedicated validators | Two thin validator entry points load the paired schemas and fixture roots. | **CONFIRMED files / execution not run** | Validator presence is real; passing behavior is not claimed here. |
| Fixture families | Each paired schema has one documented valid and one invalid case. | **CONFIRMED minimal fixtures** | Coverage is real but narrow. |
| Generic schema harness | `tests/schemas/test_common_contracts.py` discovers runtime schema fixtures. | **CONFIRMED test code / not run** | Package behavior is still untested. |
| Schema-validation workflow | Workflow installs the root package and runs `make schemas`. | **CONFIRMED workflow definition / run result not established here** | CI wiring exists at repository level; package-specific enforcement remains unknown. |
| ADR-0019 | File exists but explicitly remains draft/proposed and not accepted authority. | **CONFIRMED file / PROPOSED decision** | Do not present its paths or API as implemented fact. |
| Runtime/API production behavior | No deployed consumer, runtime log, receipt, release record, or public response was inspected. | **UNKNOWN** | This README is not implementation or deployment proof. |

### Current namespace tree

```text
packages/envelopes/
├── README.md
├── pyproject.toml                 # kfm-envelopes 0.0.0 only
└── src/
    ├── README.md
    └── envelopes/
        ├── README.md              # this file
        └── __init__.py            # empty
```

This tree is a bounded verified surface, not an exhaustive proof that no unindexed or empty file exists.

[Back to top](#top)

---

## Bounded context and ubiquitous language

The bounded context is:

> Deterministic construction and local checking of envelope **candidates** from explicit governed inputs.

Use these terms consistently:

| Term | Meaning here | Not equivalent to |
|---|---|---|
| Envelope candidate | In-memory mapping/object prepared for later schema, policy, evidence, release, and runtime handling. | Governed public response. |
| Finite outcome | One of `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` in the paired runtime schemas. | Policy decision vocabulary, HTTP status, exception class, or truth score. |
| Local invariant | A rule unambiguously derivable from an accepted schema/profile and checkable without I/O or authority decisions. | Policy evaluation or evidence closure. |
| Reference carrier | A value that preserves an identifier/ref supplied by a caller. | Resolver, store, or proof. |
| Reason code | Stable machine-readable classification safe for the intended audience. | Raw exception, free-text policy explanation, PII, secret, or chain-of-thought. |
| Policy state | Caller-supplied summary field in the current RuntimeResponseEnvelope schema. | Full `PolicyDecision` or policy-engine result. |
| Freshness | Caller-supplied response freshness posture. | Recomputed source validity or guaranteed current truth. |
| Correction state | Caller-supplied correction/withdrawal/supersession posture. | A correction workflow or release mutation. |
| Schema profile | Explicit schema path/version/hash that defines a machine shape. | Architecture prose alone. |
| Compatibility adapter | Explicit, tested conversion between accepted profiles. | Silent field renaming or best-effort coercion. |

The word **build** means “prepare a candidate,” not “authorize, validate completely, release, publish, or render.”

[Back to top](#top)

---

## What belongs here

Appropriate future implementation includes:

- closed finite-outcome constants or enums bound to an accepted profile;
- candidate builders for current schema-confirmed fields;
- local required-field and value-shape guards;
- explicit schema-profile identifiers;
- deterministic identifier/spec-hash preservation utilities;
- stable reason-code syntax checks when a canonical vocabulary exists;
- evidence-ref carrier adapters that never resolve or fabricate evidence;
- policy/freshness/correction-state carrier adapters that never decide those states;
- explicit compatibility adapters between accepted versions;
- immutable or plainly serializable candidate/result types;
- synthetic fixture builders for package tests;
- issue objects with stable codes and safe context.

A placement test:

> The code may belong here when it is reusable across multiple governed callers, performs no hidden I/O, does not decide truth/admissibility/release, and can be tested deterministically from explicit inputs.

[Back to top](#top)

---

## What does not belong here

| Do not place here | Owning responsibility |
|---|---|
| Envelope semantic contracts | `contracts/runtime/` |
| Canonical JSON Schemas | `schemas/contracts/v1/runtime/` |
| Policy rules, OPA/Rego, audience decisions, sensitivity decisions | `policy/` and governed policy runtime |
| Reason-code authority registry | Accepted contract/schema/policy or governed API registry home |
| EvidenceRef resolution or EvidenceBundle construction | Evidence resolver/proof lanes |
| Source fetching, source admission, rights review | `connectors/`, source registry, intake/review lanes |
| Lifecycle reads/writes or promotion | `data/`, pipelines, promotion/release workflows |
| Receipt or proof persistence/signing | `data/receipts/`, `data/proofs/`, accepted trust-object homes |
| ReleaseManifest, correction, withdrawal, supersession, rollback mutation | `release/` and governed release workflows |
| Runtime adapter orchestration and service wiring | `runtime/`, applications, or accepted runtime packages |
| Public API route handlers or final serializers | Governed API application |
| UI/MapLibre rendering or Evidence Drawer projection | UI/application roots |
| Model provider calls, prompts, completions, hidden reasoning | Governed AI runtime behind evidence and policy gates |
| Raw exceptions, provider payloads, secrets, credentials, private source records | Nowhere in this package or fixtures |

[Back to top](#top)

---

## Package module versus runtime envelope lane

Two confirmed paths mention envelope helpers:

```text
packages/envelopes/src/envelopes/   # reusable import-module candidate
runtime/envelopes/                  # runtime helper-note and handoff lane
```

Until an accepted ADR or implementation boundary settles ownership:

- reusable pure helpers may be **PROPOSED** here;
- runtime orchestration, adapter handoff, request context, service integration, and operational notes remain outside this module;
- `runtime/envelopes/` must not become a second Python implementation of the same API without a migration/ADR;
- this package must not absorb runtime-specific globals, service containers, credentials, provider clients, or deployment configuration;
- callers must depend on one supported implementation surface, not choose between parallel helpers by convenience.

**Status:** path presence is `CONFIRMED`; final implementation ownership is `NEEDS VERIFICATION / ADR`.

[Back to top](#top)

---

## Contract, schema, and architecture drift

The repository currently contains multiple envelope descriptions that do not fully agree. This is a material implementation blocker, not a formatting issue.

### RuntimeResponseEnvelope drift

The architecture guide sketches fields such as:

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

The current paired schema is closed and instead requires:

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

Because `additionalProperties` is `false`, an implementation targeting the current schema cannot add the architecture-guide fields without failing validation.

### DecisionEnvelope drift

The older architecture guide describes a decision vocabulary:

```text
allow · deny · restrict · hold · abstain
```

The current paired schema instead requires `outcome` from:

```text
ANSWER · ABSTAIN · DENY · ERROR
```

and requires `policy_family` from:

```text
promotion · access · render · capability · consent · sensitivity
```

The paired draft contract follows this schema and documents `decision` only as an optional compatibility alias for the same finite outcome set.

### Required posture

Until governance resolves the drift:

1. bind every candidate builder to one explicit schema/profile;
2. use the paired semantic contract for that schema profile;
3. do not emit architecture-only fields into a closed schema;
4. do not map `hold` or `restrict` to a finite public outcome without an accepted policy/runtime rule;
5. do not silently translate `allow` to `ANSWER` or `deny` to `DENY`—evidence, release, freshness, correction, and obligations still matter;
6. reject mixed-profile objects with a stable incompatibility issue;
7. record the resolution in an ADR/migration note and update schemas, contracts, fixtures, validators, docs, package tests, and callers together.

```text
CONFLICTED design surface
  -> no stable package API
  -> explicit profile selection
  -> governed schema/contract reconciliation
  -> tested compatibility or breaking-version decision
  -> first supported exports
```

[Back to top](#top)

---

## RuntimeResponseEnvelope helper boundary

For the **current paired schema profile**, a candidate builder may accept only explicit values for the schema-confirmed fields:

| Field | Current schema posture | Package-helper rule |
|---|---|---|
| `id` | required, pattern-constrained string | Preserve caller value or construct only under an accepted deterministic identity profile. |
| `spec_hash` | required `sha256:<64 hex>` | Validate syntax; never invent a hash for unknown content. |
| `version` | required string | Require explicit profile/version; no ambient default after stable releases begin. |
| `issued_at` | required date-time | Accept explicit time or caller-provided clock; do not hide nondeterministic current-time calls. |
| `outcome` | required finite enum | Reject unknown, null, lowercase, or provider-specific outcomes. |
| `reason_code` | required string | Preserve stable code; canonical vocabulary is still `NEEDS VERIFICATION`. |
| `evidence_refs` | required array of EvidenceRef objects | Preserve refs; do not resolve, upgrade, or fabricate them. |
| `policy_state` | required string | Preserve caller-supplied state; controlled vocabulary is `NEEDS VERIFICATION`. |
| `freshness` | required string | Preserve caller-supplied posture; do not compute source freshness implicitly. |
| `correction_state` | required string | Preserve caller-supplied posture; do not mutate correction/release state. |

The current schema does **not** include a payload field. Therefore this module must not claim to construct a payload-bearing public response under that profile.

### Local guards allowed before schema validation

A helper may reject:

- absent required fields;
- malformed `id` or `spec_hash` syntax;
- invalid date-time strings when the implementation has an accepted date-time parser;
- outcomes outside the finite set;
- non-array `evidence_refs`;
- mixed schema-profile fields;
- fields that would violate the closed schema.

A helper must not claim full validity until the authoritative schema validator passes.

[Back to top](#top)

---

## DecisionEnvelope helper boundary

For the **current paired schema profile**, required fields are:

| Field | Current schema posture | Package-helper rule |
|---|---|---|
| `decision_id` | required, pattern-constrained string | Preserve or construct under accepted identity rules. |
| `outcome` | required finite enum | Keep distinct from policy-engine internal decision vocabularies. |
| `policy_family` | required closed enum | Reject unknown families; do not infer from free text. |
| `reasons` | required array of strings | Keep safe and structured; do not leak policy internals or sensitive facts. |
| `obligations` | required array of strings | Preserve supplied obligations; do not create or waive them. |
| `evaluated_at` | required date-time | Preserve the actual evaluation time; do not rewrite stale decisions. |

Optional schema-confirmed fields are:

```text
id · decision · reason_code · evidence_refs · spec_hash · version · issued_at
```

Rules:

- when both `outcome` and compatibility alias `decision` are present, they must agree;
- `PolicyDecision`, `PromotionDecision`, `ReleaseManifest`, and `RuntimeResponseEnvelope` remain distinct objects;
- a finite `ANSWER` decision is not sufficient to authorize a public answer;
- obligations remain mandatory downstream unless an accepted policy/release process clears them;
- evidence refs remain references, not proof closure.

[Back to top](#top)

---

## DomainFeatureEnvelope and other envelope families

`DomainFeatureEnvelope` appears in architecture documentation as **PROPOSED** with open ADR status. No accepted package API or current schema binding was verified for it in this task.

Therefore:

- do not export `DomainFeatureEnvelope` from `envelopes.__init__`;
- do not add a builder based only on prose;
- do not use it as a generic container that flattens source role, sensitivity, ownership, evidence, geometry precision, or time;
- require accepted contract meaning, schema shape, fixtures, validator coverage, public-safety rules, and a consumer before implementation;
- keep map/UI projection logic outside this module.

The same admission rule applies to `MapContextEnvelope`, `AIReceipt`, `RunReceipt`, `ReleaseManifest`, `RollbackCard`, and any new “envelope” name: reference or adapter support does not make this package the object’s authority home.

[Back to top](#top)

---

## Accepted inputs

Inputs must be explicit, already available to the caller, and safe for the selected envelope profile.

| Input family | Accepted posture | Rejected behavior |
|---|---|---|
| Schema/profile | Explicit path/version/hash or accepted profile identifier. | Guessing the “latest” schema at runtime. |
| Identity | Caller-provided stable id or accepted deterministic key inputs. | Random hidden ids or ids encoding sensitive content. |
| Outcome | Closed finite outcome. | Provider-specific status, boolean success, null, or free text. |
| Reason | Stable code and safe structured reasons. | Raw exception, prompt, model output, PII, secret, or policy internals. |
| Evidence | EvidenceRef objects or refs supplied by governed caller. | Direct canonical-store read or fabricated bundle/ref. |
| Policy | Policy family/state/obligations supplied by policy/runtime systems. | Local policy evaluation or obligation removal. |
| Time | Explicit issuance/evaluation time and caller-supplied freshness posture. | Hidden wall-clock dependence or freshness recomputation. |
| Correction | Explicit correction state/ref from release/correction systems. | Local correction, withdrawal, or supersession mutation. |
| Release | Reference supplied by release-aware caller when a future profile supports it. | Release approval or manifest creation. |
| Trace | Explicit request/run/spec context when an accepted profile includes it. | Hidden chain-of-thought or provider internals. |

No helper should fetch missing inputs from a network, data store, environment credential, model provider, UI state, or mutable global.

[Back to top](#top)

---

## Permitted outputs

The module may eventually return:

- a schema-profile-specific candidate mapping or immutable value object;
- a deterministic list of local issues;
- a compatibility result that explicitly names source and target profiles;
- a serialization-ready mapping only after local checks pass;
- fixture candidates containing synthetic/public-safe values.

It must not return:

- a public HTTP response;
- a release-approved or policy-approved object;
- an EvidenceBundle or resolved-evidence assertion;
- an authoritative receipt/proof;
- a lifecycle promotion result;
- a model-generated answer;
- a UI/map-ready object that bypasses governed API projection;
- a success boolean that hides issues or profile selection.

### Proposed local result shape

The following is **PROPOSED**, not implemented or canonical:

```python
from dataclasses import dataclass
from typing import Generic, Literal, Mapping, TypeVar

T = TypeVar("T")

@dataclass(frozen=True)
class EnvelopeIssue:
    code: str
    field: str | None = None
    detail: str | None = None  # safe, non-sensitive context only

@dataclass(frozen=True)
class EnvelopeCandidateResult(Generic[T]):
    status: Literal["CANDIDATE", "INVALID", "UNSUPPORTED", "ERROR"]
    profile: str
    value: T | None
    issues: tuple[EnvelopeIssue, ...]
```

This result status is package-local and must not be confused with `RuntimeResponseEnvelope.outcome`.

[Back to top](#top)

---

## Proposed module interface

No module below currently has verified implementation. This is a smallest-useful, reversible proposal after the drift is resolved.

```text
packages/envelopes/src/envelopes/
├── README.md
├── __init__.py                 # deliberate supported exports only
├── outcomes.py                 # finite outcome enum/constants
├── issues.py                   # local issue/result carriers
├── profiles.py                 # accepted schema-profile identifiers
├── runtime_response.py         # current-profile candidate builder/guards
├── decision.py                 # current-profile candidate builder/guards
└── compatibility.py            # add only after explicit migration rules exist
```

### Proposed callable surface

```python
build_runtime_response_candidate(...)
build_decision_envelope_candidate(...)
check_runtime_response_local_invariants(...)
check_decision_envelope_local_invariants(...)
convert_envelope_profile(...)
```

Admission rules:

- no export until a real consumer and tests exist;
- no wildcard exports;
- no import-time registration or I/O;
- no “latest profile” ambient default;
- no generic `build_envelope(**kwargs)` that erases object-family differences;
- no authority verbs such as `approve`, `publish`, `promote`, `decide_policy`, `resolve_truth`, `resolve_evidence`, or `call_model`.

[Back to top](#top)

---

## Import and export posture

The current empty `__init__.py` establishes no supported public API.

A future supported import may look like this only after implementation admission:

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

`__init__.py` should export only stable, reviewed symbols. Internal profile adapters and migration helpers should remain private until their compatibility burden is accepted.

[Back to top](#top)

---

## Dependency and import direction

Preferred direction:

```text
contracts + schemas + policy decisions + evidence/release refs
                         |
                         v
              governed caller/runtime
                         |
                         v
        packages/envelopes helper candidate
                         |
                         v
            authoritative schema validation
                         |
                         v
             governed runtime/API serializer
                         |
                         v
                    public client
```

This module may depend on:

- Python standard library;
- narrowly accepted shared value types;
- generated or pinned schema models after provenance and compatibility are accepted;
- a schema library only after dependency and packaging decisions are explicit.

This module must not import:

- connectors or source clients;
- lifecycle data access or canonical stores;
- policy engines;
- release writers;
- receipt/proof stores;
- model-provider clients;
- API routers or application service containers;
- UI/map components;
- deployment configuration or credentials.

Circular direction is prohibited: contracts/schemas/policy/data/release must not depend on package implementation for their authority.

[Back to top](#top)

---

## Determinism, identity, time, and hashing

### Determinism

Given the same explicit inputs and profile, helpers should return byte-equivalent canonical values or equivalent structured results after any accepted normalization.

Do not depend on:

- current wall-clock time unless injected;
- random ids unless a caller supplies them;
- environment-dependent locale/timezone;
- dictionary iteration assumptions for canonical hashing;
- network lookups;
- mutable global registries;
- provider-specific response order.

### Identity

Identifiers must:

- satisfy the selected schema pattern;
- remain stable enough for audit and correction;
- avoid embedding secrets, private prompts, exact protected locations, personal data, or credentials;
- distinguish RuntimeResponseEnvelope identity from DecisionEnvelope identity;
- preserve source identifiers as separate provenance fields where future profiles allow them.

Any deterministic-id recipe is `PROPOSED` until an accepted identity profile defines canonicalization, namespace, collision handling, and versioning.

### Time

Preserve distinct time meanings:

- `issued_at` is envelope issuance time;
- `evaluated_at` is decision evaluation time;
- source observation/valid/publication times belong to their source/domain objects;
- freshness is a governed posture, not a timestamp alias;
- correction state is not a time field.

Do not rewrite timestamps to make stale or corrected responses appear current.

### Hashing

`spec_hash` syntax is schema-confirmed for RuntimeResponseEnvelope. Computing its value requires an accepted canonical serialization and content boundary. Until that profile exists, helpers may validate syntax and preserve supplied hashes but must not claim to generate authoritative hashes.

[Back to top](#top)

---

## Evidence, citation, policy, and release boundaries

### Evidence and citations

The module may preserve EvidenceRef values. It must not:

- create EvidenceBundles;
- resolve evidence through canonical/internal stores;
- claim that a ref is admissible, current, complete, or sufficient;
- fabricate citations or locator precision;
- turn an empty or unresolved evidence set into an `ANSWER` by convenience;
- disclose restricted evidence through reason strings or issue details.

The current RuntimeResponseEnvelope schema requires `evidence_refs` for every outcome but does not encode conditional minimums. Outcome-specific evidence sufficiency therefore remains a semantic/policy/runtime concern unless a future schema adds explicit constraints.

### Policy, rights, and sensitivity

The module may preserve policy fields supplied by a caller. It must not:

- evaluate audience class, rights, consent, sensitivity, capability, access, render, or promotion policy;
- choose a policy family from free text;
- downgrade obligations;
- translate `hold`/`restrict` into a public outcome without an accepted rule;
- expose private policy internals in errors;
- treat an `ANSWER` outcome as proof that policy evaluation passed.

### Release and correction

The module may preserve release/correction refs only when an accepted profile contains them. It must not:

- create or approve a ReleaseManifest;
- promote data;
- mark content published;
- withdraw, supersede, correct, or roll back releases;
- hide correction or stale-state posture;
- infer release safety from schema validity.

[Back to top](#top)

---

## Lifecycle and trust-membrane posture

The lifecycle invariant remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

This package is outside lifecycle storage and promotion authority.

Allowed flow:

```text
governed caller
  -> explicit policy/evidence/freshness/correction context
  -> envelope candidate helper
  -> authoritative schema validation
  -> runtime policy/evidence/release gates
  -> governed API/runtime serialization
  -> public client
```

Blocked flow:

```text
package helper
  -> read RAW / WORK / QUARANTINE or canonical stores directly
  -> call model provider
  -> invent evidence or release support
  -> emit public response directly
  -> let client infer permission from payload presence
```

The package may help make the trust membrane consistent. It is not the trust membrane.

[Back to top](#top)

---

## Failure and error semantics

Failures must be finite, explicit, deterministic where practical, and safe to expose to maintainers.

### Proposed local issue families

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
reference/invalid-shape
internal/unexpected
```

Rules:

- package issues do not decide the public outcome;
- raw exceptions may be chained internally but must not leak through public payloads;
- `ABSTAIN`, `DENY`, and `ERROR` are not interchangeable;
- no partial candidate should be returned as successful after a fatal issue;
- no helper should catch every exception and return an apparently valid `ERROR` envelope without required governed context;
- issue details must exclude secrets, credentials, raw prompts, chain-of-thought, private records, precise protected locations, and unrestricted evidence text.

### Fail-closed defaults

When profile selection, field meaning, policy mapping, evidence sufficiency, or compatibility is ambiguous, return `UNSUPPORTED`/`INVALID` locally or require the caller to choose a governed `ABSTAIN`, `DENY`, or `ERROR` path. Do not guess.

[Back to top](#top)

---

## Security, privacy, and data minimization

The module should be no-network and no-secret by default.

Required controls for future code:

- no environment credential reads;
- no network clients;
- no filesystem reads/writes except explicitly isolated test fixtures;
- no logging of full envelope inputs by default;
- no raw evidence, source payload, model response, prompt, or hidden reasoning retention;
- no sensitive details in ids, reason codes, issue details, reprs, or exceptions;
- bounded input sizes to reduce denial-of-service risk;
- explicit rejection of unknown fields under closed profiles;
- synthetic/public-safe fixtures only;
- secure dependency review before adding serialization/schema libraries;
- deterministic redaction of any diagnostic context allowed by policy.

A caller remains responsible for supplying already authorized values. The package must still minimize what it retains or returns.

[Back to top](#top)

---

## Validation, tests, fixtures, and CI

### Confirmed repository validation surfaces

| Surface | Current evidence | What it proves | What it does not prove |
|---|---|---|---|
| RuntimeResponseEnvelope schema | Fielded, closed, `PROPOSED`. | Machine shape for that profile. | Semantic sufficiency, runtime behavior, evidence resolution, release safety. |
| DecisionEnvelope schema | Fielded, closed, `PROPOSED`. | Machine shape and finite enums. | Policy correctness or public permission. |
| Dedicated validators | Thin entry points use the common JSON Schema runner. | Validator files and configured paths exist. | They passed in this session or cover package code. |
| RuntimeResponseEnvelope fixtures | One valid, one invalid missing-id case. | Minimal positive/negative schema examples. | Outcome-condition rules or broad adversarial coverage. |
| DecisionEnvelope fixtures | One valid, one invalid missing-decision-id case. | Minimal positive/negative schema examples. | Policy mapping, obligations semantics, or compatibility drift. |
| Generic schema harness | Discovers fixture families under contract schemas. | Repository test code exists. | A current green CI result. |
| Schema-validation workflow | Installs root and runs `make schemas`. | A repository CI path is defined. | Dedicated package tests or production correctness. |

### Required package tests before first export

```text
tests/packages/envelopes/
├── test_import_safety.py
├── test_public_exports.py
├── test_runtime_response_candidate.py
├── test_decision_envelope_candidate.py
├── test_profile_rejection.py
├── test_closed_fields.py
├── test_outcome_enum.py
├── test_policy_family_enum.py
├── test_reason_code_safety.py
├── test_identity_and_hash_syntax.py
├── test_time_injection.py
├── test_no_hidden_io.py
├── test_no_authority_imports.py
└── test_compatibility.py          # only after mappings exist
```

This tree is **PROPOSED**. Do not create it as a parallel test authority without checking repository test conventions.

### Required cases

- valid and invalid examples for every supported profile;
- each missing required field;
- every unknown field under a closed schema;
- invalid enum, id, hash, and date-time values;
- conflicting `outcome`/`decision` aliases;
- mixed architecture-profile and current-schema fields;
- ambiguous policy decision mapping;
- empty, malformed, unresolved, or restricted evidence refs;
- stale and correction-affected caller context;
- oversized inputs;
- deterministic repeatability;
- no-network and no-filesystem behavior;
- no sensitive leakage in issues/exceptions;
- import graph checks against connectors, stores, policy engines, release writers, model clients, API routes, and UI packages.

### Validation commands after implementation exists

```bash
python tools/validators/validate_runtime_response_envelope.py
python tools/validators/validate_decision_envelope.py
pytest -q tests/schemas/test_common_contracts.py
pytest -q tests/packages/envelopes
```

The first three commands target confirmed repository paths. The package-test command is **PROPOSED** until that lane exists.

[Back to top](#top)

---

## Implementation admission sequence

Use the smallest reversible sequence:

1. **Resolve ownership:** decide package module versus `runtime/envelopes/` implementation responsibility.
2. **Resolve profiles:** reconcile architecture prose, paired contracts, and paired schemas through an ADR/migration decision.
3. **Pin authority:** name the accepted semantic contract and exact schema version/hash.
4. **Define package metadata:** build backend, Python range, dependencies, license/security posture, and package discovery.
5. **Add package test lane:** follow current test/fixture conventions; do not create a parallel authority root.
6. **Implement one object family:** prefer the simplest current-profile candidate builder with no compatibility mapping.
7. **Keep `__init__` narrow:** export only reviewed symbols.
8. **Run schema and package tests:** include negative, adversarial, and no-I/O cases.
9. **Wire one governed consumer:** runtime/API caller validates again at the trust boundary.
10. **Emit review evidence:** record versions, hashes, test results, known gaps, correction, and rollback target.
11. **Expand only from observed need:** add DecisionEnvelope or compatibility helpers after real consumers and tests justify them.

Do not collapse profile resolution, implementation, self-approval, and release into one unreviewed change.

[Back to top](#top)

---

## Compatibility, correction, and rollback

### Compatibility policy

Before a stable package API exists:

- treat all proposed symbols as unstable;
- require explicit profile identifiers;
- reject unknown fields and mixed profiles;
- do not silently rename fields or map vocabularies;
- document every compatibility adapter with source/target profiles, lossiness, obligations, tests, and removal plan.

After a stable release:

- follow semantic versioning or an accepted repository version policy;
- keep deprecations observable;
- preserve old parsers only when security and governance allow;
- require migration fixtures and consumer tests for breaking changes;
- retain correction and rollback targets.

### Correction posture

A contract/schema correction may invalidate prior candidate objects. A mature implementation should let callers:

- identify the profile/hash used;
- detect unsupported or superseded profiles;
- rebuild candidates from original governed inputs;
- distinguish corrected, superseded, withdrawn, and stale states;
- avoid mutating historical receipts or released artifacts in place.

### Rollback triggers

Rollback or disable the package change if it:

- becomes a parallel contract/schema/policy/evidence/release authority;
- accepts mixed or unknown profiles silently;
- maps policy decisions to public outcomes without accepted rules;
- allows closed-schema extra fields;
- fabricates evidence, release, policy, identity, time, or hashes;
- performs hidden network/filesystem/model/store I/O;
- leaks sensitive data in logs/errors/reprs;
- bypasses governed runtime/API validation;
- creates a second implementation beside `runtime/envelopes/` without migration authority;
- breaks existing callers without an accepted migration.

### Documentation-only rollback target

For this v0.2 README revision, restore prior target blob:

```text
71899b1233770534f3f0cadbb61425940684c620
```

No data, schema, contract, policy, runtime, release, or deployment rollback is required for this documentation-only change.

[Back to top](#top)

---

## Definition of done

### This README revision

- [x] Preserves the helper-only, finite-outcome, no-network, no-authority posture.
- [x] Records the verified `kfm-envelopes` `0.0.0` Python scaffold.
- [x] Records the empty namespace initializer and absent supported exports.
- [x] Separates package helpers from runtime orchestration and public serving.
- [x] Grounds RuntimeResponseEnvelope and DecisionEnvelope fields in paired schemas/contracts.
- [x] Surfaces architecture/schema and decision-vocabulary conflicts.
- [x] Documents evidence, policy, lifecycle, release, correction, security, validation, and rollback boundaries.
- [x] Changes no code, schema, contract, policy, workflow, fixture, test, data, receipt, proof, release, or deployment artifact.

### First supported module release

- [ ] Owners and CODEOWNERS review are accepted.
- [ ] Package/runtime implementation ownership is resolved.
- [ ] Envelope profile drift is resolved through accepted governance.
- [ ] Build backend, Python range, dependencies, discovery, and security posture are defined.
- [ ] Public exports and compatibility policy are accepted.
- [ ] At least one real governed consumer exists.
- [ ] Package tests cover positive, negative, ambiguous, conflicting, stale, correction-affected, restricted, unsupported, and no-I/O cases.
- [ ] Schema validators and fixture harness pass for the pinned profile.
- [ ] No authority-root or trust-membrane bypass is proven.
- [ ] Correction, migration, deprecation, and rollback are documented.
- [ ] Release provenance and artifact integrity are verified if the package is distributed.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status |
|---|---|---|
| `PKG-ENV-001` | Who owns the package/module and which CODEOWNERS rule is enforceable? | **UNKNOWN** |
| `PKG-ENV-002` | Does implementation belong here, in `runtime/envelopes/`, or behind another accepted package boundary? | **NEEDS VERIFICATION / ADR** |
| `PKG-ENV-003` | Which RuntimeResponseEnvelope field set is canonical: architecture prose, current paired schema, or a successor profile? | **CONFLICTED** |
| `PKG-ENV-004` | Which DecisionEnvelope vocabulary is canonical: policy-style decisions or finite runtime outcomes? | **CONFLICTED** |
| `PKG-ENV-005` | What is the acceptance status of the current paired runtime schemas and contracts? | **NEEDS VERIFICATION** |
| `PKG-ENV-006` | Which reason-code registry and stability policy bind package helpers? | **UNKNOWN** |
| `PKG-ENV-007` | Which controlled vocabularies govern `policy_state`, `freshness`, and `correction_state`? | **UNKNOWN** |
| `PKG-ENV-008` | What build backend, Python range, dependencies, package discovery, and license metadata apply? | **UNKNOWN** |
| `PKG-ENV-009` | Which symbols form the first supported public API? | **UNKNOWN** |
| `PKG-ENV-010` | Which application/runtime consumers import the package today or are committed first adopters? | **NEEDS VERIFICATION** |
| `PKG-ENV-011` | Should package tests live under `tests/packages/envelopes/`, and which fixture lane should they use? | **NEEDS VERIFICATION** |
| `PKG-ENV-012` | Have dedicated validators and common schema fixtures passed at the intended merge commit? | **NEEDS VERIFICATION** |
| `PKG-ENV-013` | How are policy `hold`/`restrict` states translated to finite public outcomes? | **UNKNOWN / policy decision required** |
| `PKG-ENV-014` | What conditional rules govern evidence refs and payload support per outcome in future profiles? | **UNKNOWN** |
| `PKG-ENV-015` | Is `DomainFeatureEnvelope` accepted, schema-backed, and safe for package implementation? | **PROPOSED / OPEN ADR** |
| `PKG-ENV-016` | What canonical serialization and hashing profile produces authoritative `spec_hash` values? | **UNKNOWN** |
| `PKG-ENV-017` | How are corrected or superseded profiles invalidated and replayed? | **UNKNOWN** |
| `PKG-ENV-018` | Which CI checks block unsafe package imports, profile drift, and authority bypass? | **UNKNOWN** |
| `PKG-ENV-019` | Can public clients be proven unable to import package internals or bypass governed API/runtime validation? | **NEEDS VERIFICATION** |
| `PKG-ENV-020` | Is package-registry publication planned, and how is it separated from KFM data publication? | **UNKNOWN** |

[Back to top](#top)

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Current request | **CONFIRMED task authority** | Update this exact README through a scoped documentation change. | Not implementation proof. |
| Prior target README | **CONFIRMED** | Existing helper-only, finite-outcome, no-network, anti-authority, validation, and rollback posture. | Planning-oriented; package state and current schema drift were stale. |
| `packages/envelopes/pyproject.toml` | **CONFIRMED** | Distribution `kfm-envelopes`, version `0.0.0`. | No build backend, dependencies, Python range, discovery, or publishing behavior. |
| `src/envelopes/__init__.py` | **CONFIRMED empty file** | Python namespace scaffold exists. | No exports or runtime behavior. |
| Parent package/source READMEs | **CONFIRMED repository docs** | Shared-package and source-root intent. | Remain planning-oriented and do not prove implementation. |
| `runtime/envelopes/README.md` | **CONFIRMED repository doc** | Separate runtime helper-note/handoff lane exists. | Does not settle implementation ownership or prove runtime code. |
| RuntimeResponseEnvelope contract/schema | **CONFIRMED paired draft surfaces** | Current fielded closed profile, finite outcomes, evidence/policy/freshness/correction posture. | Status is `PROPOSED`; conditional public-response semantics remain incomplete. |
| DecisionEnvelope contract/schema | **CONFIRMED paired draft surfaces** | Current required fields, finite outcomes, policy families, optional compatibility fields. | Status is `PROPOSED`; conflicts with older architecture vocabulary. |
| Architecture envelope guide | **CONFIRMED repository doc / draft** | Richer wire-envelope concept and reason-code posture. | Field surface conflicts with current closed schema. |
| ADR-0019 | **CONFIRMED file / PROPOSED ADR** | Provider-neutral, finite-outcome direction and no-generated-truth posture. | Explicitly not accepted authority; implementation paths remain proposed. |
| Dedicated validator entry points | **CONFIRMED files** | Exact schema and fixture paths are wired into common validator runner. | Execution and CI pass status were not established in this README authoring step. |
| Runtime envelope fixture READMEs | **CONFIRMED minimal fixture families** | One valid and one invalid case for each paired schema. | Narrow coverage; does not prove package behavior, policy, evidence, release, or public safety. |
| Common schema test harness | **CONFIRMED test code** | Discovers contract schema fixture families and checks expected errors. | Not package-specific; not run in this step. |
| Schema-validation workflow | **CONFIRMED workflow definition** | Repository CI path runs schema validation via `make schemas`. | Current run result and package-specific enforcement remain unverified. |
| Directory Rules v1.4 | **CONFIRMED placement doctrine** | `packages/` is shared implementation; contracts, schemas, policy, data, runtime, tests, and release remain distinct roots. | Some path/ADR decisions remain proposed. |
| Indexed repository search | **CONFIRMED bounded search** | Did not establish supported helper modules or production import consumers. | Search is not exhaustive tree/runtime proof. |

[Back to top](#top)

---

## Status summary

`packages/envelopes/src/envelopes/` is a verified Python namespace scaffold inside distribution `kfm-envelopes` version `0.0.0`. Its initializer is empty, and no supported helper API, consumer, package test suite, runtime wiring, receipt, release integration, or production behavior is established. The repository does contain paired draft contracts/schemas, validators, fixtures, and a schema harness for RuntimeResponseEnvelope and DecisionEnvelope, but architecture and schema surfaces currently conflict. The next implementation step is governance reconciliation and one small, profile-pinned, no-I/O candidate builder—not a broad envelope framework.

<p align="right"><a href="#top">Back to top</a></p>
