<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-connectors-core-src-readme
title: Connectors Core Package Source Root README
type: readme
version: v0.2
status: draft; repository-grounded; python-source-root; implementation-placeholder; PROPOSED source-root contract
owners:
  - OWNER_TBD — Package steward
  - OWNER_TBD — Connector steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Contracts steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Validator steward
  - OWNER_TBD — Security / sensitivity steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Docs steward
created: 2026-06-13
updated: 2026-07-14
policy_label: public
supersedes: v0.1 (2026-06-13)
path: packages/connectors-core/src/README.md
repository_snapshot: main@578d30e76c8eba980c0ff4a8d3cfd1dd11974623
related:
  - ./connectors_core/README.md
  - ../README.md
  - ../pyproject.toml
  - ../../README.md
  - ../../../connectors/README.md
  - ../../../docs/sources/ADMISSION_PROCESS.md
  - ../../../docs/adr/ADR-0017-source-descriptor-admission-process.md
  - ../../../data/registry/sources/README.md
  - ../../../contracts/source/source_descriptor.md
  - ../../../contracts/source/ingest_receipt.md
  - ../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../../schemas/contracts/v1/source/ingest_receipt.schema.json
  - ../../../fixtures/contracts/v1/source/source_descriptor/README.md
  - ../../../tests/schemas/test_common_contracts.py
  - ../../../tools/validators/validate_source_descriptor.py
  - ../../../tools/validators/connector_gate/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../.github/workflows/connector-gate.yml
tags: [kfm, packages, connectors-core, python, src-layout, source-root, import-boundary, connector-primitives, source-descriptor, ingest-receipt, no-network, fail-closed, no-hidden-io, generated-code, compatibility, rollback]
notes:
  - "v0.2 replaces runtime uncertainty with a commit-pinned description of the Python src-layout scaffold."
  - "The package declares kfm-connectors-core 0.0.0; the verified import package is src/connectors_core/."
  - "connectors_core/__init__.py is empty and core.py contains only a greenfield-placeholder comment; no implemented exports or indexed consumers are claimed."
  - "The merged child-module README at src/connectors_core/README.md is the detailed contract for connector primitive semantics and SourceDescriptor/IngestReceipt drift."
  - "No package-specific tests or fixtures were found at the tested README paths, and connector-gate CI remains echo-only."
  - "This source-root README does not resolve SourceDescriptor singular/plural schema authority or validator/fixture path drift."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Connectors Core Package Source Root

`packages/connectors-core/src/`

> Python `src`-layout container for the `kfm-connectors-core` shared package. This directory organizes importable package implementation; it does not create source authority, admit sources, perform hidden network access, write lifecycle state, emit authoritative receipts, close evidence, decide policy, approve release, or serve public clients.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.2-1f6feb)
![layout](https://img.shields.io/badge/layout-Python%20src--layout-3776ab)
![implementation](https://img.shields.io/badge/implementation-placeholder-lightgrey)
![network](https://img.shields.io/badge/import%20network-forbidden-critical)
![lifecycle](https://img.shields.io/badge/hidden%20writes-forbidden-critical)

> [!IMPORTANT]
> **Repository snapshot:** `main` at `578d30e76c8eba980c0ff4a8d3cfd1dd11974623`  
> **Current project metadata:** `kfm-connectors-core`, version `0.0.0`  
> **Verified import package:** `src/connectors_core/`  
> **Verified implementation:** empty `connectors_core/__init__.py` and comment-only `connectors_core/core.py`  
> **Verified child contract:** [`connectors_core/README.md`](./connectors_core/README.md) v0.2  
> **Exports and consumers:** not observed in indexed repository search  
> **Package tests and fixtures:** not found at the tested package-specific README paths  
> **Connector-gate workflow:** echo-TODO scaffold, not enforcement proof

> [!CAUTION]
> The existence of a Python source tree does not prove that the project builds, installs, exports symbols, has consumers, passes tests, or safely handles network and lifecycle operations. Those claims require package metadata, implementation, tests, fixtures, workflows, and runtime evidence.

---

## Quick jump

- [1. Purpose and audience](#1-purpose-and-audience)
- [2. Current repository state](#2-current-repository-state)
- [3. Source-root bounded context](#3-source-root-bounded-context)
- [4. Placement and authority](#4-placement-and-authority)
- [5. Current directory surface](#5-current-directory-surface)
- [6. Source root versus import package](#6-source-root-versus-import-package)
- [7. Import and export contract](#7-import-and-export-contract)
- [8. Import-time safety](#8-import-time-safety)
- [9. Dependency direction](#9-dependency-direction)
- [10. Configuration and secrets boundary](#10-configuration-and-secrets-boundary)
- [11. Generated code and schema adapters](#11-generated-code-and-schema-adapters)
- [12. Contract and schema drift boundary](#12-contract-and-schema-drift-boundary)
- [13. Lifecycle and receipt boundary](#13-lifecycle-and-receipt-boundary)
- [14. Public trust boundary](#14-public-trust-boundary)
- [15. Proposed source-tree evolution](#15-proposed-source-tree-evolution)
- [16. Tests and fixtures](#16-tests-and-fixtures)
- [17. Packaging and installation gates](#17-packaging-and-installation-gates)
- [18. Security and observability](#18-security-and-observability)
- [19. Compatibility, correction, and rollback](#19-compatibility-correction-and-rollback)
- [20. Validation commands](#20-validation-commands)
- [21. Definition of done](#21-definition-of-done)
- [22. Open verification register](#22-open-verification-register)
- [23. Evidence ledger](#23-evidence-ledger)
- [24. Maintainer checklist](#24-maintainer-checklist)

---

## 1. Purpose and audience

`packages/connectors-core/src/` is the package implementation container for the Python project declared by [`../pyproject.toml`](../pyproject.toml).

Its durable responsibility is structural:

- contain importable source for the `connectors_core` package;
- make package discovery and import boundaries explicit;
- provide a stable home for source-agnostic connector primitives;
- keep package exports deliberate and reviewable;
- keep generated adapters subordinate to canonical contracts and schemas;
- keep implementation separate from source-specific connectors, lifecycle data, policy, receipts, evidence, and release authority;
- support deterministic, offline-first tests without placing tests or production payloads in the source root.

This README is for:

- package maintainers;
- authors of source-specific connectors and watchers;
- source, rights, sensitivity, evidence, and release stewards;
- contract, schema, validator, and fixture maintainers;
- reviewers checking packaging, import, dependency, or authority drift;
- maintainers planning the first executable connector-core slice.

This README does not define connector primitive semantics in detail. That responsibility belongs to the child module contract at [`connectors_core/README.md`](./connectors_core/README.md).

[Back to top](#top)

---

## 2. Current repository state

| Surface | Evidence at snapshot | Status | Consequence |
|---|---|---|---|
| This README | Existing v0.1 planning document at `packages/connectors-core/src/README.md`. | **CONFIRMED** | Revised in place. |
| [`../pyproject.toml`](../pyproject.toml) | Declares `[project]`, name `kfm-connectors-core`, and version `0.0.0` only. | **CONFIRMED minimal placeholder** | Python project identity is known; build backend, dependencies, package discovery, and supported Python versions are not declared. |
| [`connectors_core/README.md`](./connectors_core/README.md) | Merged v0.2 repository-grounded child-module contract. | **CONFIRMED** | Detailed primitive, drift, retry, integrity, and safety guidance lives there. |
| `connectors_core/__init__.py` | Exists and is empty. | **CONFIRMED** | Import package marker only; no public exports are established. |
| `connectors_core/core.py` | Contains only a greenfield-placeholder comment. | **CONFIRMED placeholder** | No executable connector-core primitive is established. |
| Source-root index search | Surfaced this README and the child package surfaces. | **CONFIRMED search result / incomplete inventory** | Search is not a recursive tree proof. |
| Connector-core imports | Indexed searches for `from connectors_core`, `import connectors_core`, and `connectors_core.core` returned no consumers during the child-module review. | **NOT OBSERVED / search-limited** | Do not claim the package is consumed. |
| Package tests | `tests/packages/connectors-core/README.md` was not found at the tested path. | **CONFIRMED absent at tested path** | No dedicated package test lane is established by current evidence. |
| Package fixtures | `fixtures/packages/connectors-core/README.md` was not found at the tested path. | **CONFIRMED absent at tested path** | No dedicated package fixture lane is established by current evidence. |
| Connector-gate workflow | `.github/workflows/connector-gate.yml` contains echo-TODO jobs. | **CONFIRMED scaffold** | Workflow success cannot prove connector-core behavior. |
| SourceDescriptor schema family | Fielded singular schema and empty plural schema both exist. | **CONFIRMED drift** | Source-root code must not choose authority implicitly. |
| IngestReceipt contract/schema | Fielded contract and closed schema exist. | **CONFIRMED contract/schema** | Package may eventually adapt shapes but must not emit authoritative receipts by itself. |
| Build/install behavior | No build backend, dependency list, package discovery configuration, wheel/sdist artifact, or installation test was inspected. | **UNKNOWN** | Do not claim installability. |
| Runtime behavior | No live network, connector run, receipt, lifecycle write, or deployed consumer was inspected. | **UNKNOWN** | This README is not runtime proof. |

### Truth summary

```text
Python project name/version            = CONFIRMED
src-layout intent                      = CONFIRMED by path and package marker
import package path                    = CONFIRMED
public exports                         = NOT OBSERVED
implemented primitives                 = NOT OBSERVED
consumer imports                       = NOT OBSERVED
package-specific tests/fixtures        = NOT FOUND at tested paths
build/install behavior                 = UNKNOWN
runtime/network behavior               = UNKNOWN
source admission enforcement           = UNKNOWN
lifecycle/receipt integration          = UNKNOWN
```

[Back to top](#top)

---

## 3. Source-root bounded context

The source root owns **package implementation organization**, not source governance.

### Terms

| Term | Meaning here | Must not be confused with |
|---|---|---|
| Source root | `packages/connectors-core/src/`, the container used for importable Python source. | Repository root, source registry, external source, or lifecycle RAW. |
| Import package | `connectors_core/`, the Python package directory under the source root. | The distribution name `kfm-connectors-core`. |
| Distribution name | `kfm-connectors-core`, declared in project metadata. | Python import name `connectors_core`. |
| Public export | Symbol intentionally re-exported from `connectors_core/__init__.py` and supported as package API. | Any internal module or object that merely exists. |
| Internal module | Source file used inside the package but not promised as stable public API. | Canonical contract or schema authority. |
| Source-specific connector | Implementation for one source, agency, product, or endpoint under `connectors/`. | Shared connector primitive. |
| SourceDescriptor | Governed source identity and treatment descriptor. | Connector configuration, fetch result, or source payload. |
| IngestReceipt | Governed record of a capture/ingest event. | Helper dictionary, log entry, retry record, or manifest fragment. |
| Source root fixture helper | Pure factory for synthetic test inputs, if accepted. | Production fixture data or source evidence. |

### Core statement

```text
packages/connectors-core/src/
  = package implementation container

packages/connectors-core/src/connectors_core/
  = Python import package

connectors/
  = source-specific implementations

data/registry/sources/
  = source identity and treatment authority

data/raw/ + data/quarantine/
  = governed lifecycle outputs

contracts/ + schemas/
  = semantic and shape authority

policy/ + release/
  = admissibility and publication authority
```

[Back to top](#top)

---

## 4. Placement and authority

Directory Rules assign files by responsibility. This source root is correct because it is implementation code for a shared package.

| Responsibility | Correct home | Source-root posture |
|---|---|---|
| Shared connector-core implementation | `packages/connectors-core/src/connectors_core/` | Owned here. |
| Python project metadata | `packages/connectors-core/pyproject.toml` | Parent-owned; source root consumes it. |
| Package-level contract | `packages/connectors-core/README.md` | Parent package boundary. |
| Module-level primitive contract | `packages/connectors-core/src/connectors_core/README.md` | Child module boundary. |
| Source-specific connector | `connectors/<source>/` | Must remain outside this package. |
| Source identity and admission records | `data/registry/sources/` | Referenced, never owned here. |
| Source admission doctrine | `docs/sources/ADMISSION_PROCESS.md` and accepted governance surfaces | Constrains implementation. |
| Contract meaning | `contracts/source/` and other accepted contract roots | Consumed, never redefined here. |
| Machine shape | `schemas/contracts/v1/` | Consumed, never redefined here. |
| Validator implementation | `tools/validators/` | Package may expose pure helpers; validator orchestration stays in tools. |
| Tests | `tests/` | Primary test authority outside source. |
| Cross-cutting fixtures | `fixtures/` | Shared synthetic inputs outside source. |
| Lifecycle records | `data/raw/`, `data/work/`, `data/quarantine/`, downstream phases | Never hidden package-owned state. |
| Receipts and proofs | `data/receipts/`, `data/proofs/` | Emitted/stored by governed execution, not source-root import. |
| Policy | `policy/` | Package preserves inputs/results; does not decide. |
| Release and rollback | `release/` | Outside package authority. |
| Public interface | governed apps/runtime | Package is not a public trust membrane. |

> [!WARNING]
> A shared package is an implementation dependency, not a governance shortcut. Callers may not use package availability to bypass SourceDescriptor resolution, rights/sensitivity checks, lifecycle routing, receipt emission, evidence closure, policy, review, or release.

[Back to top](#top)

---

## 5. Current directory surface

Files verified at the inspected snapshot:

```text
packages/connectors-core/
├── README.md
├── pyproject.toml
└── src/
    ├── README.md
    └── connectors_core/
        ├── README.md
        ├── __init__.py
        └── core.py
```

Current semantic status:

| Path | Status | Meaning |
|---|---|---|
| `src/README.md` | v0.2 after this change | Source-root contract. |
| `src/connectors_core/README.md` | v0.2 | Child import-package and primitive contract. |
| `src/connectors_core/__init__.py` | empty | No exports. |
| `src/connectors_core/core.py` | comment-only | Placeholder; no behavior. |

This is a **verified tested-path surface**, not a guarantee that no other unindexed files exist.

### Do not infer

- successful `pip install`;
- editable-install support;
- wheel or sdist generation;
- namespace-package behavior;
- entry points or console scripts;
- dependency resolution;
- semantic version stability;
- consumer compatibility;
- production readiness.

[Back to top](#top)

---

## 6. Source root versus import package

The source root and import package have different responsibilities.

### `src/`

`src/` should contain:

- import-package directories;
- generated package source only when governed;
- package-level source documentation;
- no production data;
- no package-independent scripts;
- no source-specific connector implementation.

### `src/connectors_core/`

`src/connectors_core/` should contain:

- Python modules for source-agnostic connector primitives;
- deliberate package exports;
- internal types and protocols;
- pure adapters to canonical contract/schema objects;
- package-owned exceptions and result categories;
- child documentation.

### Boundary rule

```text
src/ controls package layout
src/connectors_core/ controls Python implementation
pyproject.toml controls project/build metadata
tests/ proves behavior
fixtures/ supplies shared synthetic examples
connectors/ owns source-specific execution
```

Do not put implementation directly under `src/` unless Python packaging evidence establishes a deliberate module layout. The current verified import package is `connectors_core/`.

[Back to top](#top)

---

## 7. Import and export contract

### Import name

The distribution and import names differ:

```text
distribution: kfm-connectors-core
import:       connectors_core
```

Documentation, tests, and consumers must not conflate them.

### Current export state

`connectors_core/__init__.py` is empty. Therefore:

- no stable public symbols are currently confirmed;
- no wildcard-import contract exists;
- no version constant is confirmed;
- no compatibility promise exists for `core.py`;
- the child module should be treated as internal scaffolding.

### Future public exports

A symbol may be exported only when:

1. its responsibility belongs in connectors-core;
2. its contract is documented;
3. its typing and exception behavior are stable;
4. it has positive and negative tests;
5. it does not perform hidden network or lifecycle I/O;
6. it preserves source, rights, sensitivity, time, and integrity context where relevant;
7. its compatibility and deprecation policy are defined;
8. at least one governed consumer justifies the shared API.

Example future posture:

```python
# PROPOSED shape only — not current implementation.
from .results import FetchObservation
from .retry import RetryDecision
from .source_head import SourceHeadObservation

__all__ = [
    "FetchObservation",
    "RetryDecision",
    "SourceHeadObservation",
]
```

The example is not permission to create these names without implementation review.

### Internal modules

Internal modules should be imported through documented package-internal paths and may change before a stable package release. Public consumers must not depend on private or underscored modules without an explicit compatibility decision.

[Back to top](#top)

---

## 8. Import-time safety

Importing `connectors_core` must be safe and deterministic.

### Forbidden during import

- network requests;
- DNS resolution;
- credential lookup;
- environment mutation;
- secret-manager access;
- filesystem writes;
- lifecycle reads or writes;
- source registry mutation;
- schema downloads;
- policy evaluation;
- connector registration with external systems;
- background threads;
- timers or schedulers;
- telemetry emission;
- logging of environment or header values;
- clock-dependent object creation;
- random identifiers;
- source activation or admission checks.

### Allowed during import

- class and function definitions;
- immutable constants that contain no secrets;
- safe enum and type declarations;
- exception definitions;
- pure protocol/type imports;
- explicit package metadata constants when sourced deterministically.

### Import-safety test

A future test should verify:

```text
import connectors_core
  -> no network
  -> no filesystem writes
  -> no environment mutation
  -> no logs containing secrets
  -> no lifecycle access
  -> no policy/release decision
```

An import failure caused by optional runtime dependencies should be avoided through explicit adapters and dependency groups rather than hidden import fallbacks.

[Back to top](#top)

---

## 9. Dependency direction

### Allowed direction

```text
source-specific connectors / validators / pipelines / tests
  -> connectors_core public API
  -> pure result, retry, integrity, metadata, or adapter behavior
  -> caller performs governed execution and lifecycle actions
```

### Disallowed direction

```text
connectors_core
  -> imports a specific connector
  -> activates a source
  -> reads source registry as hidden global state
  -> writes RAW or QUARANTINE
  -> emits authoritative receipt
  -> creates EvidenceBundle
  -> decides policy
  -> releases or publishes
```

### Layering

| Layer | May depend on | Must not depend on |
|---|---|---|
| Pure primitive | Python standard library and approved lightweight types | connectors, lifecycle data, policy engines, web frameworks |
| Contract adapter | canonical generated/typed contract support | alternate local schema definitions |
| Validator adapter | shared validator API supplied by caller | hidden filesystem or network discovery |
| Source-specific connector | connectors-core plus source-owned dependencies | public UI or release authority |
| Governed ingest execution | connector, policy, registry, lifecycle, receipt systems | package-level hidden globals |
| Public application | governed runtime/API surfaces | package internals or raw connector outputs directly |

Circular dependencies between `connectors_core` and source-specific connectors are forbidden.

[Back to top](#top)

---

## 10. Configuration and secrets boundary

Connectors-core may define configuration **types**, validation helpers, or safe redaction utilities. It must not own production configuration or secrets.

### May accept

- caller-provided timeout and retry limits;
- caller-provided transport interfaces;
- caller-provided safe endpoint identifiers;
- caller-provided policy/descriptor references;
- caller-provided redaction profiles;
- caller-provided clocks and random sources for tests;
- opaque credential references that are never resolved or logged by pure helpers.

### Must not contain

- API keys;
- OAuth tokens;
- passwords;
- cookies;
- private certificates;
- secret values in defaults;
- production endpoint credentials;
- personal access tokens;
- unrestricted local file paths;
- real restricted payload examples;
- hard-coded source activation flags.

### Environment variables

Reading environment variables is runtime I/O. It belongs in a caller-owned configuration/bootstrap layer, not in pure package imports or result models.

### Redaction

Any future metadata/logging helper must default-deny:

- `Authorization`;
- `Cookie` and `Set-Cookie`;
- API key headers and query parameters;
- bearer tokens;
- signed URLs;
- credentials embedded in URLs;
- private path components;
- restricted identifiers;
- payload excerpts unless explicitly safe.

[Back to top](#top)

---

## 11. Generated code and schema adapters

Generated source is allowed only when it reduces drift without creating a second authority.

### Required conditions

- source schema path and blob/spec hash recorded;
- generator name and version recorded;
- generation command documented;
- output deterministic;
- generated header identifies provenance;
- generated files are not hand-edited;
- drift test compares generated output to committed output;
- rollback target exists;
- schema authority conflict is resolved before generation.

### Current blocker

The SourceDescriptor family has unresolved authority drift:

```text
schemas/contracts/v1/source/source_descriptor.schema.json
  = fielded and closed
  = declares plural path canonical

schemas/contracts/v1/sources/source_descriptor.schema.json
  = permissive empty scaffold
  = contract_doc null
```

Therefore, generated SourceDescriptor types must not be admitted into this source root until the canonical schema and migration path are resolved.

### Adapter posture

A hand-written adapter may temporarily accept an explicit schema object supplied by a caller, but must not:

- duplicate the schema fields locally as sovereign truth;
- silently choose singular or plural authority;
- accept permissive plural shape as equivalent to the fielded schema;
- hide fixture or validator path drift;
- claim contract maturity from schema existence alone.

[Back to top](#top)

---

## 12. Contract and schema drift boundary

The child module README contains the detailed drift register. The source root must enforce these package-level consequences.

| Drift | Confirmed evidence | Source-root consequence |
|---|---|---|
| Singular versus plural SourceDescriptor schema | Both paths exist; only singular is fielded. | No generated canonical type and no implicit schema selection. |
| Canonical-path metadata mismatch | Singular schema declares plural canonical. | Require steward/ADR/migration resolution. |
| Validator-path mismatch | Schema metadata names `tools/validators/sources/validate_source_descriptor.py`; observed wrapper is `tools/validators/validate_source_descriptor.py`. | Package must not hard-code either path as canonical. |
| Fixture-root mismatch | Schema metadata names `tests/fixtures/sources/source_descriptor/`; observed harness uses `fixtures/contracts/v1/source/source_descriptor/`. | Package test adapters must accept caller-supplied fixture paths until resolved. |
| IngestReceipt validator absent | Schema names `tools/validators/validate_ingest_receipt.py`, not found at tested path. | Do not claim dedicated receipt validation or emit receipts from this package. |
| Proposed admission ADR | ADR-0017 status is proposed. | Do not represent proposed activation workflow as accepted runtime implementation. |

### Admission gate for source-root implementation

Before schema-bound package code is accepted:

- [ ] canonical SourceDescriptor schema chosen;
- [ ] contract and schema metadata agree;
- [ ] validator path agrees with repository reality;
- [ ] fixture root agrees with test harness;
- [ ] migration and rollback recorded;
- [ ] generated or hand-written types tested against valid and invalid fixtures;
- [ ] consumer imports use one supported API.

[Back to top](#top)

---

## 13. Lifecycle and receipt boundary

Connectors-core supports callers near the pre-RAW edge but does not own lifecycle transitions.

```text
External source
  -> source-specific connector
  -> connector-core primitives
  -> admission / policy / steward gate
  -> RAW or QUARANTINE + receipt
  -> downstream lifecycle outside connectors-core
```

### Hidden writes are forbidden

Package code must not select or write:

- `data/raw/`;
- `data/work/`;
- `data/quarantine/`;
- `data/processed/`;
- `data/catalog/`;
- `data/triplets/`;
- `data/published/`;
- `data/receipts/`;
- `data/proofs/`;
- `release/`.

A caller may provide an explicit sink interface, but the governed caller owns:

- path selection;
- authorization;
- atomicity;
- receipts;
- policy and review;
- failure routing;
- correction and rollback.

### IngestReceipt distinction

Connectors-core may eventually help validate or assemble **candidate field values** for an `IngestReceipt`. It must not declare a helper dictionary authoritative.

The confirmed schema requires:

```text
id
source_id
run_id
started_at
finished_at
outcome = SUCCESS | PARTIAL | FAIL
bytes_in
digests
```

Receipt authority begins only when governed execution binds those fields to:

- a real source descriptor;
- a real run;
- captured content;
- trusted time;
- calculated digests;
- lifecycle destination;
- immutable persisted receipt identity.

[Back to top](#top)

---

## 14. Public trust boundary

This source root is not a public interface.

Public clients and normal UI surfaces must not:

- import connectors-core directly;
- receive raw transport results;
- receive secret-bearing headers;
- receive unreleased source metadata;
- query source registry or RAW/QUARANTINE through package shortcuts;
- infer source admissibility from fetch success;
- infer freshness from ETag presence;
- infer evidence closure from a checksum;
- infer publication permission from an IngestReceipt.

Governed applications may use package outputs internally, but public responses must be mediated by:

- source identity and role checks;
- rights and sensitivity policy;
- evidence and citation state;
- lifecycle and release state;
- correction and rollback state;
- finite runtime outcomes;
- public-safe projection.

[Back to top](#top)

---

## 15. Proposed source-tree evolution

The current source tree is a placeholder. Evolve it in small reversible steps.

### Phase 0 — Resolve package discovery

- choose build backend;
- declare supported Python versions;
- configure `src` package discovery;
- define dependencies and optional groups;
- add build/install smoke tests;
- keep version `0.0.0` until compatibility policy is chosen.

### Phase 1 — Establish import safety

- keep `__init__.py` minimal;
- add import-side-effect tests;
- add typing/lint baseline;
- define package-owned exceptions;
- add no-network test guard.

### Phase 2 — Add pure primitives

Candidate internal modules, all **PROPOSED**:

```text
connectors_core/
├── __init__.py
├── results.py
├── retry.py
├── deadlines.py
├── source_head.py
├── integrity.py
├── redaction.py
└── errors.py
```

Requirements:

- no source-specific code;
- no network implementation required;
- caller-supplied clocks/randomness;
- immutable result types where practical;
- bounded inputs and outputs;
- deterministic tests.

### Phase 3 — Add schema-bound adapters

Only after drift resolution:

```text
connectors_core/
├── source_descriptor.py
└── ingest_receipt.py
```

Adapters should validate or map explicit objects; they should not own registry, policy, persistence, or receipt emission.

### Phase 4 — Define public exports

- export only proven shared APIs;
- add `__all__`;
- document compatibility;
- add API tests;
- add consumer migration notes.

### Phase 5 — Pilot with one governed connector

Choose a low-risk source with:

- public-safe fixtures;
- no credential requirement;
- explicit SourceDescriptor;
- no public output;
- RAW/QUARANTINE routing owned by caller;
- receipt and rollback coverage.

No broad connector migration should precede this proof slice.

[Back to top](#top)

---

## 16. Tests and fixtures

No dedicated package test or fixture README was found at the tested paths. The following is **PROPOSED**.

### Test families

```text
tests/packages/connectors-core/
├── test_src_layout.py
├── test_import_safety.py
├── test_public_exports.py
├── test_no_source_specific_imports.py
├── test_no_hidden_network.py
├── test_no_hidden_filesystem_writes.py
├── test_retry_bounds.py
├── test_deadline_and_cancellation.py
├── test_source_head_normalization.py
├── test_digest_streaming.py
├── test_header_redaction.py
├── test_result_categories.py
├── test_source_descriptor_adapter.py
├── test_ingest_receipt_adapter.py
└── test_no_lifecycle_or_release_authority.py
```

### Fixture families

```text
fixtures/packages/connectors-core/
├── transport/
├── retry/
├── source_head/
├── integrity/
├── redaction/
├── source_descriptor/
└── ingest_receipt/
```

Package fixtures must be synthetic and no-network.

### Negative-first cases

- import attempts network access;
- retry count exceeds limit;
- delay exceeds remaining deadline;
- cancellation is ignored;
- response exceeds byte limit;
- redirect exceeds limit or crosses disallowed policy;
- header redactor leaks authorization;
- credential appears in URL;
- ETag is treated as SHA-256;
- digest is computed after bytes change;
- source-specific endpoint appears in shared primitive;
- package chooses singular/plural SourceDescriptor schema silently;
- helper writes RAW or QUARANTINE;
- helper emits authoritative receipt without caller context;
- helper treats `SUCCESS` as source admission;
- package import depends on optional connector dependency;
- generated file lacks provenance;
- public export changes without compatibility test.

### Existing schema harness

`tests/schemas/test_common_contracts.py` validates contract fixture families under `fixtures/contracts/v1/`. That proves schema fixture behavior, not connector-core package behavior.

[Back to top](#top)

---

## 17. Packaging and installation gates

Before claiming this source root is installable:

- [ ] `[build-system]` is declared;
- [ ] package discovery includes `src/connectors_core`;
- [ ] supported Python versions are declared;
- [ ] runtime dependencies are declared;
- [ ] optional/test/dev dependencies are separated;
- [ ] wheel builds;
- [ ] sdist builds;
- [ ] clean virtual-environment install succeeds;
- [ ] editable install succeeds if supported;
- [ ] `import connectors_core` succeeds;
- [ ] package metadata reports expected name/version;
- [ ] no repository-root path injection is required;
- [ ] no undeclared dependency is imported;
- [ ] package contains required generated data or excludes it deliberately;
- [ ] build artifact contains no secrets, fixtures, raw data, or internal receipts;
- [ ] reproducibility or artifact-digest posture is documented.

### Versioning

Version `0.0.0` indicates placeholder status. A first non-placeholder version should require:

- defined public API;
- compatibility policy;
- changelog or release note;
- test coverage;
- at least one governed consumer;
- packaging CI;
- rollback path.

[Back to top](#top)

---

## 18. Security and observability

### Security defaults

- no network on import;
- no implicit credential resolution;
- no secrets in exceptions;
- no raw response body in logs;
- no header dump by default;
- no unrestricted redirect following;
- no unbounded response buffering;
- no retry of non-idempotent operations unless caller explicitly permits;
- no path construction from unsanitized source identifiers;
- no deserialization into executable objects;
- no source role or policy inference from hostname.

### Observability boundary

Pure helpers may return structured, non-sensitive observations to the caller.

Example **PROPOSED** fields:

```text
operation
attempt
elapsed_ms
status_category
retryable
bytes_observed
etag_present
last_modified_present
digest_algorithm
redaction_applied
reason_code
```

They must not include:

- credential values;
- complete signed URLs;
- cookies;
- raw sensitive payload excerpts;
- private file paths;
- secret environment values;
- policy-protected identifiers.

The caller owns log destination, retention, access, receipt binding, and incident handling.

[Back to top](#top)

---

## 19. Compatibility, correction, and rollback

### Compatibility

Until a public API exists, internal modules may evolve, but changes must still preserve:

- child README boundaries;
- import safety;
- no-hidden-I/O;
- source-agnostic responsibility;
- explicit contract/schema choice;
- negative test coverage;
- migration notes when consumers appear.

Once public exports exist:

- deprecate before removal;
- preserve semantic distinctions;
- document exception and result changes;
- avoid silent default changes;
- provide adapters or migration notes;
- test old and new consumers during the compatibility window.

### Correction

When source governance or schema authority changes:

1. update the authoritative contract/schema/ADR first;
2. update generated or adapter source;
3. update fixtures and tests;
4. record supersession or correction;
5. rebuild package artifacts;
6. re-run consumer tests;
7. invalidate stale releases or receipts where required.

### Rollback triggers

Rollback source-root changes when they:

- create hidden network or filesystem effects;
- add source-specific implementation to connectors-core;
- bypass source admission;
- write lifecycle state;
- leak secrets or restricted metadata;
- create duplicate contract/schema authority;
- choose unresolved schema authority silently;
- emit receipts without governed execution;
- break package installation or consumers;
- permit public clients to access package internals.

### Documentation rollback

Revert the documentation commit or close its draft PR without merging. Do not rewrite shared history.

[Back to top](#top)

---

## 20. Validation commands

These commands are inspection guidance. They are not reported as run in this connector-only documentation change.

```bash
# Inspect package source and metadata.
find packages/connectors-core -maxdepth 4 -type f -print | sort
cat packages/connectors-core/pyproject.toml

# Inspect imports and consumers.
git grep -nE '(^|[[:space:]])(from|import)[[:space:]]+connectors_core' -- \
  ':!packages/connectors-core/src/README.md' \
  ':!packages/connectors-core/src/connectors_core/README.md'

# Inspect source-specific leakage.
git grep -nE 'https?://|api[_-]?key|authorization|cookie|password|token' -- \
  packages/connectors-core/src/connectors_core

# Inspect source-contract drift.
git diff --no-index \
  schemas/contracts/v1/source/source_descriptor.schema.json \
  schemas/contracts/v1/sources/source_descriptor.schema.json

# Inspect validator and fixture locations.
find tools/validators fixtures/contracts/v1/source tests/fixtures/sources \
  -maxdepth 5 -type f -print | sort 2>/dev/null
```

Proposed package checks after tooling exists:

```bash
python -m build packages/connectors-core
python -m pytest tests/packages/connectors-core
python -m pytest tests/schemas/test_common_contracts.py
```

No command above is evidence of a current passing build unless a current run log is supplied.

[Back to top](#top)

---

## 21. Definition of done

This README update is complete when:

- [x] the Python source-root role is explicit;
- [x] current package metadata and placeholder implementation are documented;
- [x] `src/` is distinguished from `src/connectors_core/`;
- [x] current exports, consumers, tests, fixtures, build, and runtime maturity are bounded honestly;
- [x] import-time network and lifecycle effects are forbidden;
- [x] package and source-specific connector authority remain separated;
- [x] schema-generated source is blocked until SourceDescriptor drift is resolved;
- [x] IngestReceipt helper and authority boundaries are distinct;
- [x] packaging, security, tests, compatibility, correction, and rollback gates are documented;
- [x] the child module README remains the detailed primitive contract.

The source root becomes implementation-mature only when:

- [ ] build backend and package discovery are configured;
- [ ] supported Python and dependency policy are declared;
- [ ] build/install smoke tests pass;
- [ ] import-safety tests pass;
- [ ] pure primitives are implemented and tested;
- [ ] SourceDescriptor authority/path drift is resolved;
- [ ] validator and fixture paths are reconciled;
- [ ] schema-bound adapters are tested;
- [ ] public exports are deliberate;
- [ ] at least one governed consumer is verified;
- [ ] connector-gate CI runs real checks;
- [ ] no-hidden-I/O and no-authority-bypass tests pass;
- [ ] compatibility and rollback are demonstrated.

[Back to top](#top)

---

## 22. Open verification register

| ID | Question | Status | Evidence required |
|---|---|---|---|
| `PKG-CONN-SRC-001` | Which build backend owns `kfm-connectors-core`? | UNKNOWN | `pyproject.toml` build-system decision and build test. |
| `PKG-CONN-SRC-002` | Is `src` package discovery configured correctly? | UNKNOWN | Build metadata and wheel inspection. |
| `PKG-CONN-SRC-003` | Which Python versions are supported? | UNKNOWN | Project metadata and CI matrix. |
| `PKG-CONN-SRC-004` | Which runtime dependencies are allowed? | UNKNOWN | Dependency policy and metadata. |
| `PKG-CONN-SRC-005` | Which symbols form the first public API? | PROPOSED | Implemented/tested consumer-backed API decision. |
| `PKG-CONN-SRC-006` | Are there unindexed source files or consumers? | NEEDS VERIFICATION | Recursive tree and code-search audit. |
| `PKG-CONN-SRC-007` | Which SourceDescriptor schema path is canonical? | CONFLICTED | Accepted ADR/migration and aligned metadata. |
| `PKG-CONN-SRC-008` | Which SourceDescriptor validator path is canonical? | CONFLICTED | Validator inventory, workflow, and metadata update. |
| `PKG-CONN-SRC-009` | Which SourceDescriptor fixture root is canonical? | CONFLICTED | Harness/metadata alignment. |
| `PKG-CONN-SRC-010` | Does a dedicated IngestReceipt validator exist elsewhere? | NEEDS VERIFICATION | Recursive tool inventory and workflow evidence. |
| `PKG-CONN-SRC-011` | Which connector-gate outcomes and report schema are accepted? | UNKNOWN | Contract/schema/policy/test evidence. |
| `PKG-CONN-SRC-012` | Which connector will be the first governed consumer? | PROPOSED | Pilot selection and acceptance package. |
| `PKG-CONN-SRC-013` | Are generated schema types desired? | NEEDS VERIFICATION | Generator decision, provenance, drift test. |
| `PKG-CONN-SRC-014` | What compatibility policy begins after `0.0.0`? | UNKNOWN | Package/versioning ADR or maintainer decision. |
| `PKG-CONN-SRC-015` | Which CI workflow proves build, import safety, and package tests? | UNKNOWN | Real workflow and successful run. |
| `PKG-CONN-SRC-016` | Does CODEOWNERS need a package-specific steward rule? | NEEDS VERIFICATION | Ownership decision and CODEOWNERS update. |
| `PKG-CONN-SRC-017` | How are package artifacts signed or digest-pinned? | UNKNOWN | Build/release policy and artifact evidence. |
| `PKG-CONN-SRC-018` | What is the rollback target for the first executable package release? | UNKNOWN | Release manifest and rollback drill. |

[Back to top](#top)

---

## 23. Evidence ledger

| Evidence | Blob / ref | Supports | Limitation |
|---|---|---|---|
| Previous `packages/connectors-core/src/README.md` | `5ee3b60574e14de3c7ac158a3a56554705eac487` | Existing source-root planning contract. | Predates current package inspection and child v0.2 update. |
| `packages/connectors-core/pyproject.toml` | `f49ef584549c29f87c5b44b7f89914604a1a8b6a` | Project name and `0.0.0` version. | No build backend, dependencies, or discovery configuration. |
| `connectors_core/__init__.py` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | Empty package marker. | No export or behavior proof. |
| `connectors_core/core.py` | `d30ad39b6b499ca9950d77798b44507b8b20f5c1` | Comment-only placeholder. | No implementation. |
| `connectors_core/README.md` v0.2 | merge commit `578d30e76c8eba980c0ff4a8d3cfd1dd11974623` | Detailed child-module contract and drift findings. | Documentation, not runtime proof. |
| `packages/connectors-core/README.md` | `5f8143304fdfa87b4dabc65d4436632aaf3fe018` | Parent package boundary. | Still v0.1 and planning-heavy. |
| `connectors/README.md` | `bdd50032bed62ac36964c79f16cf5541b21759a6` | Source-specific connector root and raw/quarantine/receipt boundary. | Child connector maturity varies. |
| `contracts/source/source_descriptor.md` | `b57ae5ccc042c1423b75c168438800384c9b6713` | SourceDescriptor semantics and schema drift acknowledgment. | Contract status PROPOSED. |
| Singular SourceDescriptor schema | `582e70b834278c3c6ca9a8b31efbe0989c96f0bc` | Fielded closed schema and metadata. | Declares a different canonical path and mismatched validator/fixture homes. |
| Plural SourceDescriptor schema | `8d5cee60a711454a78cbf4a3c84eebbaed2503e8` | Confirms plural path exists. | Empty permissive scaffold; not equivalent to singular schema. |
| SourceDescriptor fixture README | `4df8a264ef6f8ba48dbfcf313d3d6390b557f5c5` | Observed fixtures and path mismatch. | Tests were not run in that documentation update. |
| Observed SourceDescriptor validator wrapper | `9d0538e727b5eb49c043998a3550972349d2e790` | Wrapper uses singular schema and `fixtures/contracts/v1/source`. | Does not prove CI or runtime use. |
| `contracts/source/ingest_receipt.md` | `4273a9bad9edc7ce7f54c288075f8a49b0f2fe80` | Receipt meaning and finite outcomes. | Runtime integration unverified. |
| IngestReceipt schema | `4e9707bec7da63049c5043562c9470564b77184f` | Required fields, SHA-256 digests, closed shape. | Dedicated validator not found at tested path. |
| Connector-gate workflow | `fc36ecced55bb0b4002d551cb28addfff0be918a` | Workflow exists. | Echo-only scaffold. |
| Directory Rules | `2affb080e6f0043867c64c7f06c1ca52030fbd55` | `packages/` owns reusable implementation; authority roots remain separate. | Does not prove package runtime. |
| Repository snapshot | `578d30e76c8eba980c0ff4a8d3cfd1dd11974623` | Commit-pinned review base containing merged child v0.2. | No local tests or deployed runtime inspected. |

[Back to top](#top)

---

## 24. Maintainer checklist

Before changing this source root:

- [ ] Confirm the change belongs to shared package implementation.
- [ ] Read the parent and child READMEs.
- [ ] Keep source-specific connectors under `connectors/`.
- [ ] Keep import-time behavior free of network and lifecycle I/O.
- [ ] Avoid environment or secret resolution in pure modules.
- [ ] Preserve caller ownership of sinks, receipts, policy, and release.
- [ ] Do not generate schema types while SourceDescriptor authority is conflicted.
- [ ] Add deterministic positive and negative tests.
- [ ] Use synthetic, no-network fixtures.
- [ ] Redact credentials, signed URLs, cookies, and sensitive identifiers.
- [ ] Bound retries, delays, redirects, payload sizes, and deadlines.
- [ ] Keep ETag, Last-Modified, checksum, and SHA-256 semantics distinct.
- [ ] Add public exports only with consumer-backed compatibility review.
- [ ] Update package metadata when build or dependency behavior changes.
- [ ] Update documentation with material behavior changes.
- [ ] Record correction, migration, and rollback targets.
- [ ] Do not claim CI, installation, or runtime success without current evidence.

## Status summary

`packages/connectors-core/src/` is a **confirmed Python source-root scaffold**, not an implemented connector framework.

Its current purpose is to hold the `connectors_core` import package and document the boundaries that future implementation must preserve. The next useful change is not a broad connector abstraction; it is a small, tested packaging baseline plus pure source-agnostic primitives after SourceDescriptor authority and tooling drift are resolved.

<p align="right"><a href="#top">Back to top</a></p>
