<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-nrcs-src-readme
title: connectors/nrcs/src/ — NRCS Connector Source Envelope and Python Layout Boundary
type: readme
version: v0.2
status: draft; repository-grounded; source-envelope; implementation-empty; package-layout-unratified; non-authoritative
owners: OWNER_TBD — Connector steward · Source steward · NRCS steward · Package steward · Soil steward · Agriculture steward · Hydrology steward · Atmosphere/Climate steward · Rights reviewer · Sensitivity reviewer · Tribal/sovereignty reviewer · Security steward · Validation steward · Contract steward · Schema steward · Receipt steward · Migration steward · CI steward · Docs steward
created: 2026-06-20
updated: 2026-07-15
supersedes: v0.1 planning-oriented source-root guide (2026-06-20)
policy_label: "public-doctrine; connector-source-root; nrcs; python-src-layout; implementation-empty; package-discovery-unratified; import-side-effect-free; no-network-by-default; fixture-first; product-isolated; descriptor-gated; raw-quarantine-only; no-authority; no-publication; no-secrets; migration-required; rollback-aware"
current_path: connectors/nrcs/src/README.md
truth_posture: CONFIRMED target v0.1 README, merged child namespace v0.2 contract, empty child initializer, kfm-connector-nrcs 0.0.0 placeholder metadata, NRCS family and test-root READMEs, grounded SDA/SCAN/gSSURGO/gNATSGO product boundaries, SSURGO v0.1 nested boundary, empty PROPOSED source-authority register, TODO-only connector-gate workflow, and bounded absence of selected shared modules, product modules, package tests, dedicated NRCS workflows, build backend, Python range, dependencies, and source-discovery configuration / PROPOSED explicit src-layout contract, single-package rule, package discovery and distribution boundary, shared-versus-product module placement, import/dependency direction, generated-code controls, runner handoff, package-data rules, tests, CI admission, correction, migration, deprecation, and rollback / CONFLICTED documentation-rich package plans versus empty executable source tree, SSURGO and SCAN nested-versus-flat placement, gSSURGO descriptor/source-role/support-type identity, and gNATSGO product identity / UNKNOWN accepted build system, supported runtime, dependencies, public exports, package consumers, source activation, executable adapters, fixtures, substantive CI, schedules, receipts, deployment, and runtime health
base_commit: 49392f54b1e994164000c083366daddf68a6a38a
prior_blob: 3b26759548ddaf52eb5b6de0e25dfa354e1d62ec
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 49392f54b1e994164000c083366daddf68a6a38a
  prior_blob: 3b26759548ddaf52eb5b6de0e25dfa354e1d62ec
  namespace_readme_blob: 00d12e0f07e53cff877e9ea4d396c96b3fb03658
  namespace_merge_commit: 49392f54b1e994164000c083366daddf68a6a38a
  family_readme_blob: 888236f218fc0892c54c947c0c2651b34ca5137b
  tests_readme_blob: 7c65ba6ef85a8369e17c40d5e3fbc388b04a306b
  package_metadata_blob: c6bb1565db7df490bee52a597d04d694e2b9f8a4
  namespace_initializer_blob: e69de29bb2d1d6434b8b29ae775ad8c2e48c5391
  sda_boundary_blob: 6f3ba95d70ae0779d00e26ad360f7b8737dbf77a
  scan_boundary_blob: 76eb5a0683e571d045d01d7e8dc387ef497ba958
  ssurgo_boundary_blob: 601b919cf0627b69b21be317cd5e8086502be0bd
  gssurgo_boundary_blob: 3ad1db6721224232f4e5eb99440a7b031bdb7afa
  gnatsgo_boundary_blob: 83b3816033fc558fd552480edefdde978488ccfd
  source_authority_register_blob: 82c23722520922f5ca0dad7f37ed794d1c2edf81
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  source_admission_adr_blob: 0e8d03786bcc99b19f179680890df9e30a27633a
  connector_gate_workflow_blob: fc36ecced55bb0b4002d551cb28addfff0be918a
  bounded_path_checks:
    - connectors/nrcs/src/README.md existed at version v0.1 before this revision
    - connectors/nrcs/src/nrcs/README.md is merged at version v0.2
    - connectors/nrcs/src/nrcs/__init__.py exists and is empty
    - connectors/nrcs/pyproject.toml contains only project name kfm-connector-nrcs and version 0.0.0
    - selected shared modules config.py, client.py, descriptors.py, envelope.py, and errors.py were not found under the namespace
    - selected product modules products/sda.py, scan.py, ssurgo.py, gssurgo.py, and gnatsgo.py were not found
    - selected tests test_import_safety.py and test_descriptor_gates.py were not found
    - dedicated workflows .github/workflows/nrcs.yml and nrcs-connector.yml were not found
    - .github/workflows/connector-gate.yml contains TODO echo steps
    - control_plane/source_authority_register.yaml is PROPOSED and entries is empty
related:
  - ../README.md
  - ./nrcs/README.md
  - ./nrcs/__init__.py
  - ../pyproject.toml
  - ../tests/README.md
  - ../sda/README.md
  - ../scan/README.md
  - ../ssurgo/README.md
  - ../gssurgo/README.md
  - ../gnatsgo/README.md
  - ../../README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0017-source-descriptor-admission-process.md
  - ../../../control_plane/source_authority_register.yaml
  - ../../../data/raw/
  - ../../../data/quarantine/
  - ../../../data/receipts/
  - ../../../data/proofs/
  - ../../../contracts/
  - ../../../schemas/
  - ../../../policy/rights/
  - ../../../policy/sensitivity/
  - ../../../release/
  - ../../../.github/workflows/connector-gate.yml
tags: [kfm, connectors, nrcs, python, src-layout, source-envelope, package-discovery, import-safety, no-network, product-adapter, sda, scan, ssurgo, gssurgo, gnatsgo, raw, quarantine, provenance, tests, migration, rollback]
notes:
  - "This revision changes only connectors/nrcs/src/README.md."
  - "The merged child namespace contract is authoritative for proposed import behavior; this README governs source placement, discovery, dependency direction, and admission of new modules."
  - "Current repository evidence establishes documentation and an empty initializer only; no buildable package or executable connector is claimed."
  - "Product-specific source roles, identities, time models, quality, scale, rights, sensitivity, and lineage must not be flattened into generic source-root helpers."
  - "Public clients and generated answers never import or call code from this source root directly."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# NRCS Connector Source Envelope and Python Layout Boundary

`connectors/nrcs/src/`

> Repository-present source envelope for the candidate `nrcs` Python package. Current evidence establishes this README, the grounded child namespace README, and an empty package initializer—not a configured, installable, exported, tested, or operational connector implementation.

![status](https://img.shields.io/badge/status-draft-yellow)
![version](https://img.shields.io/badge/version-v0.2-informational)
![maturity](https://img.shields.io/badge/maturity-source__scaffold-lightgrey)
![namespace](https://img.shields.io/badge/namespace-nrcs-blue)
![discovery](https://img.shields.io/badge/package__discovery-UNRATIFIED-orange)
![network](https://img.shields.io/badge/network-off__by__default-critical)
![lifecycle](https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE-blue)
![publication](https://img.shields.io/badge/publication-DENIED-red)

**Quick links:** [Purpose](#purpose) · [Evidence](#status-and-evidence) · [Authority](#authority-and-directory-rules-basis) · [Responsibility split](#package-source-and-namespace-split) · [Tree](#confirmed-bounded-tree) · [Invariants](#keystone-invariants) · [Layout](#src-layout-and-package-discovery) · [Placement](#module-placement-and-product-isolation) · [Imports](#import-and-dependency-direction) · [Configuration](#configuration-profiles-and-package-data) · [Runner](#network-runner-and-lifecycle-boundary) · [Generated code](#generated-code-vendoring-and-assets) · [Security](#security-supply-chain-and-resource-bounds) · [Testing](#tests-fixtures-and-ci) · [Compatibility](#compatibility-topology-and-migration) · [Proposed tree](#proposed-future-tree) · [Implementation](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Ledger](#evidence-ledger) · [Rollback](#rollback-correction-deprecation-and-migration)

> [!IMPORTANT]
> **This README is not a build-system, package-discovery, dependency, API, source-activation, endpoint, or release decision.** It records the current source envelope and the conditions that must be met before code is added or relied upon.

> [!CAUTION]
> **A file under `src/` is implementation, not authority.** Source code may consume accepted descriptors, contracts, schemas, policy decisions, and profiles. It may not redefine them locally or turn successful parsing into evidence closure, policy approval, or publication.

---

<a id="purpose"></a>

## Purpose

This README governs source placement and implementation admission under `connectors/nrcs/src/`.

It answers five questions:

1. Which importable package may live below this source root?
2. How must package discovery and imports be configured?
3. Which behavior is genuinely shared, and which must remain product-specific?
4. What may source code return to orchestration?
5. What evidence is required before a proposed module becomes repository fact?

This source envelope may eventually contain implementation for the shared NRCS connector package. It must not contain:

- source-family or product doctrine;
- authoritative `SourceDescriptor` or source-authority records;
- semantic contracts or machine schemas copied for convenience;
- rights, sensitivity, sovereignty, geoprivacy, or release policy;
- fixtures, captured source payloads, receipts, proofs, lifecycle data, or published artifacts;
- pipeline orchestration, schedules, public API handlers, UI state, map layers, notifications, or AI answer logic;
- credentials, tokens, cookies, private sessions, or embedded secret references.

[Back to top](#top)

---

<a id="status-and-evidence"></a>

## Status and evidence

### Current repository state

| Surface | Status | Safe conclusion |
|---|---:|---|
| This README | **CONFIRMED v0.1 before revision** | A planning-oriented source-root guide existed. |
| [`nrcs/README.md`](./nrcs/README.md) | **CONFIRMED v0.2 merged** | The child namespace has a repository-grounded package and source-admission contract. |
| [`nrcs/__init__.py`](./nrcs/__init__.py) | **CONFIRMED empty** | No exports, import behavior, or executable package implementation are established. |
| [`pyproject.toml`](../pyproject.toml) | **CONFIRMED minimal** | Only `kfm-connector-nrcs` and version `0.0.0` are declared. |
| Build backend, Python range, dependencies, discovery, wheel contents | **NOT ESTABLISHED** | The distribution is not proven buildable or installable. |
| Shared modules named by v0.1 | **NOT FOUND at bounded paths** | The old proposed tree is not current implementation. |
| Product adapter modules | **NOT FOUND at bounded paths** | SDA, SCAN, SSURGO, gSSURGO, and gNATSGO executable adapters are not established. |
| Package tests | **NOT FOUND at selected paths** | Import-safety and descriptor-gate behavior are not proven. |
| Dedicated NRCS workflow | **NOT FOUND at selected paths** | No package-specific CI enforcement is established. |
| Generic connector gate | **CONFIRMED TODO-only** | A green run proves workflow orchestration only. |
| Source authority register | **CONFIRMED empty / PROPOSED** | No active NRCS source or product can be inferred. |

### Truth labels

| Label | Meaning here |
|---|---|
| **CONFIRMED** | Directly verified from repository content or exact path checks in this work. |
| **PROPOSED** | A design or placement candidate requiring implementation and review. |
| **CONFLICTED** | Current paths, docs, or vocabularies express competing choices. |
| **UNKNOWN** | Runtime or governance state was not established. |
| **NEEDS VERIFICATION** | Checkable before implementation or release, but unresolved. |

[Back to top](#top)

---

<a id="authority-and-directory-rules-basis"></a>

## Authority and Directory Rules basis

Directory Rules place source-specific fetch, probe, parse, and admission implementation under `connectors/`. The existing `connectors/nrcs/src/` path is therefore a sound source envelope for the NRCS connector family.

Placement does not confer broader authority.

| Concern | Owning surface |
|---|---|
| NRCS family and product explanation | `docs/sources/catalog/` |
| Source identity and activation | `data/registry/sources/` and accepted control-plane records |
| Semantic meaning | `contracts/` |
| Machine shape | `schemas/` |
| Rights, sensitivity, sovereignty, and disclosure decisions | `policy/rights/`, `policy/sensitivity/` |
| Executable normalization and downstream transforms | `pipelines/`, `pipeline_specs/` |
| Test data and executable tests | `fixtures/`, `tests/`, or the accepted connector-local test convention |
| RAW and QUARANTINE records | `data/raw/`, `data/quarantine/` |
| Receipts and proofs | `data/receipts/`, `data/proofs/` |
| Release, correction, withdrawal, and rollback decisions | `release/` and accepted correction/rollback homes |
| Public access | governed APIs and released artifacts only |

This source root may import accepted contracts or generated bindings only through governed dependency choices. It must not create a parallel schema, policy, registry, receipt, proof, or release home.

[Back to top](#top)

---

<a id="package-source-and-namespace-split"></a>

## Package, source, and namespace split

| Layer | Responsibility | Must not do |
|---|---|---|
| [`connectors/nrcs/`](../README.md) | Family boundary, package metadata, product-lane index, operational ownership. | Define domain truth or release state. |
| `connectors/nrcs/src/` | Source layout, package discovery, implementation placement, import direction. | Define package API semantics already owned by the namespace. |
| [`connectors/nrcs/src/nrcs/`](./nrcs/README.md) | Proposed import namespace, shared behavior, adapter protocol, finite results. | Own build metadata, fixtures, lifecycle stores, or public interfaces. |
| Product lanes | Product-specific identity, preservation, rights, sensitivity, and anti-collapse rules. | Become executable package code merely because a README exists. |
| [`connectors/nrcs/tests/`](../tests/README.md) | Connector-local test boundary if retained. | Become source authority or fixture authority. |
| Runner or orchestrator | Explicit network calls, persistence, receipt emission, retries, schedules. | Hide activation, profiles, or writes inside importable library code. |

The parent source-root README and child namespace README are complementary. When they conflict:

1. Directory Rules and accepted ADRs govern placement;
2. accepted contracts, schemas, policy, and source records govern meaning and admissibility;
3. the child namespace governs proposed import behavior;
4. this README governs where implementation code may be placed and how it is discovered.

[Back to top](#top)

---

<a id="confirmed-bounded-tree"></a>

## Confirmed bounded tree

The verified source tree is intentionally small:

```text
connectors/nrcs/src/
├── README.md
└── nrcs/
    ├── README.md
    └── __init__.py   # empty
```

This bounded tree does **not** prove that no other files could exist outside the checked paths in future commits. It proves only the current surfaces inspected for this revision.

The v0.1 proposed modules and product adapters are not current repository facts.

[Back to top](#top)

---

<a id="keystone-invariants"></a>

## Keystone invariants

Any future code below this source root must preserve all of the following:

1. **Import is not activation.** Importing `nrcs` or a product adapter performs no live access and proves no source is admitted.
2. **Network is off by default.** Live access requires explicit runner invocation, active descriptor context, accepted profiles, and bounded controls.
3. **Product isolation is mandatory.** SDA, SCAN, SSURGO, gSSURGO, and gNATSGO remain distinct products with distinct identities and caveats.
4. **Unknown means deny or hold.** Unknown product, profile, schema, rights, sensitivity, quality, time, scale, or lineage never falls through to a generic parser.
5. **RAW or QUARANTINE only.** Library output may be a candidate for those admission stages; it is not processed, cataloged, released, or published truth.
6. **Writes belong to orchestration.** Importable source code returns data and interaction facts; a runner owns persistence and receipt emission.
7. **Evidence and policy remain external.** Code may return references and review flags, not EvidenceBundle closure or policy approval.
8. **Public clients stay behind governed interfaces.** No browser, UI, public API, notebook, or generated answer imports this package directly.
9. **Corrections preserve history.** Reprocessing or supersession creates new versioned records and receipts; it does not overwrite historical evidence.
10. **Changes remain reversible.** Module additions, dependency choices, profile versions, and path migrations require explicit rollback targets.

[Back to top](#top)

---

<a id="src-layout-and-package-discovery"></a>

## `src` layout and package discovery

The repository currently uses a candidate `src` layout, but `pyproject.toml` does not establish how the package is discovered or built.

Before executable code is admitted, package metadata must explicitly define:

- build backend and build requirements;
- supported Python versions;
- distribution name and version source;
- package discovery rooted at `src/`;
- inclusion and exclusion rules;
- runtime and optional dependencies;
- package data, typing markers, and generated binding policy;
- license and redistribution metadata;
- reproducible wheel and source-distribution checks.

Required layout rules:

- one accepted top-level import package: `nrcs`;
- no sibling `src/nrcs.py` shadow module;
- no second import package for one product without an ADR or migration decision;
- no implicit namespace-package conversion unless explicitly approved and tested;
- no dynamic path mutation, `sys.path` edits, import hooks, or working-directory assumptions;
- no package discovery based on undocumented tool defaults;
- no executable modules placed directly under `src/` beside the package;
- no editable-install-only behavior accepted as production proof.

The same import path must resolve under source checkout, built wheel, isolated virtual environment, and supported CI environments.

[Back to top](#top)

---

<a id="module-placement-and-product-isolation"></a>

## Module placement and product isolation

Shared code belongs in the namespace only when it is semantically shared across multiple product adapters.

### Appropriate shared responsibilities

- immutable profile references and bounded configuration objects;
- transport interfaces without approved endpoint constants embedded in code;
- digest and integrity helpers that use accepted external profiles;
- finite result and issue containers;
- product-adapter registration with explicit failure for unknown products;
- RAW/QUARANTINE candidate containers;
- receipt-ready interaction facts returned to the runner;
- safe logging and resource-limit utilities.

### Product-specific responsibilities

| Product | Must remain product-specific |
|---|---|
| [SDA](../sda/README.md) | Query-profile identity, read-only template and parameter rules, result-set shape, ordering, columns, keys, joins, cardinality, and free-form SQL denial. |
| [SCAN](../scan/README.md) | Network/station identity, time, cadence, sensor depth, variable, units, quality, missingness, Tribal/sovereignty review, and station-not-area posture. |
| [SSURGO](../ssurgo/README.md) | Survey-area/package identity, map-unit geometry, MUKEY/COKEY/CHKEY lineage, table relationships, scale, vintage, and package completeness. |
| [gSSURGO](../gssurgo/README.md) | Grid, CRS, resolution, band/nodata, rasterization lineage, MUKEY joins, constituent survey vintage, and support-type distinction. |
| [gNATSGO](../gnatsgo/README.md) | Product identity, grid and attribute structure, source vintage, fill/generalization lineage, support type, and national-scale caveats. |

A shared helper must not erase product identity by accepting an untyped dictionary and returning a generic “NRCS record.”

No product adapter may be added until its product lane, source identity, activation, profile, fixtures, tests, correction behavior, and rollback path are reviewable.

[Back to top](#top)

---

<a id="import-and-dependency-direction"></a>

## Import and dependency direction

Allowed direction:

```text
runner / connector command
        ↓
nrcs public namespace
        ↓
explicit shared primitives
        ↓
selected product adapter
        ↓
pure parser / candidate builder
```

Disallowed direction:

```text
product adapter → runner or scheduler
product adapter → lifecycle store
product adapter → receipt/proof writer
product adapter → public API or UI
shared primitive → product-specific semantics
namespace import → network, secrets, filesystem writes, or source activation
```

Additional rules:

- product adapters may depend on shared primitives, not on sibling product adapters;
- shared primitives must not import from product modules;
- circular imports are denied;
- optional dependencies must fail explicitly at call time, never silently downgrade behavior;
- dependencies may not fetch grids, schemas, models, binaries, or reference data during import;
- domain packages and public applications must not depend directly on connector internals as their truth source;
- type-only imports must not trigger runtime side effects.

[Back to top](#top)

---

<a id="configuration-profiles-and-package-data"></a>

## Configuration, profiles, and package data

Configuration is explicit input, not ambient state.

Source code may consume accepted references to:

- source descriptor and activation record;
- product, endpoint, operation, query, report, package, grid, and parser profiles;
- rights, attribution, sensitivity, sovereignty, and disclosure decisions;
- timeout, retry, redirect, pagination, rate, byte, row, cell, table, archive, raster, and decompression limits;
- canonicalization, digest, candidate, and receipt profiles.

It must not:

- infer activation from a file’s presence;
- read repository config by searching upward from the working directory;
- read environment variables during import;
- embed mutable endpoint catalogs or policy decisions in source code;
- use undocumented defaults when a profile is missing;
- accept UI- or model-generated free-form instructions as trusted configuration.

Package data must be minimal. Contracts, schemas, fixtures, captured payloads, source registries, policies, receipts, and lifecycle records remain outside the wheel. Any generated binding included in the package must record its source schema or contract version, generator, deterministic regeneration command, review state, and drift test.

[Back to top](#top)

---

<a id="network-runner-and-lifecycle-boundary"></a>

## Network, runner, and lifecycle boundary

Importable code may expose bounded transport and parsing functions, but an owning runner must control external effects.

### Package responsibility

- validate explicit configuration and profile references;
- construct a bounded request plan;
- parse supplied bytes or approved fixtures deterministically;
- return finite results, issues, candidate payloads, and receipt-ready facts;
- avoid direct writes and hidden retries.

### Runner responsibility

- confirm source activation and current policy decisions;
- resolve credentials through approved external secret handling;
- perform network calls under allowlists and resource limits;
- own retries, rate limiting, idempotency, cancellation, and scheduling;
- persist RAW or QUARANTINE records;
- emit interaction and ingest receipts;
- preserve run identity and correction lineage;
- stop or hold when package results require review.

The package must never write directly to:

```text
data/raw/
data/quarantine/
data/work/
data/processed/
data/catalog/
data/triplets/
data/published/
data/receipts/
data/proofs/
release/
```

Returning a path string is not equivalent to a governed handoff. The runner must validate the target, enforce lifecycle policy, write atomically, and record the receipt.

[Back to top](#top)

---

<a id="generated-code-vendoring-and-assets"></a>

## Generated code, vendoring, and assets

Generated or vendored material is denied by default unless a reviewed need is established.

Before adding generated code:

- identify the authoritative input contract or schema;
- record generator and version;
- make generation deterministic and repeatable;
- add drift detection;
- preserve license and attribution;
- prevent manual edits or document the exception;
- define correction and rollback behavior.

Before vendoring a dependency or data asset:

- document why normal dependency management is insufficient;
- record origin, version, digest, license, vulnerabilities, update cadence, and removal plan;
- prove the asset contains no secrets, private data, or prohibited source material;
- keep large fixtures, reference datasets, grids, archives, and source snapshots out of `src/`.

`src/` must not become a cache, download mirror, fixture store, schema mirror, model store, or package-data dumping ground.

[Back to top](#top)

---

<a id="security-supply-chain-and-resource-bounds"></a>

## Security, supply chain, and resource bounds

Required source-root controls include:

- no credentials, tokens, cookies, private session material, or secret-bearing examples;
- no network, filesystem writes, subprocesses, dynamic code execution, plugin discovery, or environment mutation during import;
- pinned and reviewed direct dependencies with license and vulnerability posture;
- explicit optional dependency groups and fail-closed behavior;
- no untrusted deserialization, `eval`, `exec`, shell interpolation, or unrestricted template execution;
- bounded URL, header, query, body, response, row, cell, table, file, archive, raster, and decompression sizes;
- archive traversal, symlink, nested-archive, and compression-bomb defenses;
- XML/entity, CSV/formula, JSON-depth, encoding, binary-header, and raster-dimension defenses as applicable;
- structured, redacted errors and logs with finite reason codes;
- no high-cardinality source-native IDs in metrics without review;
- deterministic cache keys and no ambient cross-run cache;
- dependency and wheel provenance recorded for operational releases.

Source code must not log raw sensitive payloads, free-form SDA parameters, precise sensitive station locations, private land or producer identifiers, unpublished material, or secret-bearing response headers.

[Back to top](#top)

---

<a id="tests-fixtures-and-ci"></a>

## Tests, fixtures, and CI

Source implementation is not admitted by documentation alone.

Minimum test layers:

1. package build and isolated wheel installation;
2. import safety with network, secret, filesystem, and subprocess traps;
3. package discovery and public-export tests;
4. shared primitive unit tests;
5. product adapter contract and anti-collapse tests;
6. malformed, adversarial, oversized, truncated, and schema-drift tests;
7. deterministic fixture replay and digest checks;
8. RAW/QUARANTINE candidate construction without direct writes;
9. runner integration with temporary stores and receipt assertions;
10. correction, supersession, compatibility, and rollback regression tests.

Fixtures must live in the accepted test or fixture responsibility root, not under `src/`. They must be synthetic, minimized, redacted, or explicitly approved snapshots with identity, purpose, date, digest, rights/sensitivity review, expected behavior, and safe-use rationale.

Default CI must block live network and require no credentials. Live integration checks, if ever approved, must be separately marked, descriptor-gated, rate-limited, non-mutating, and excluded from the default test path.

Current limitation: `.github/workflows/connector-gate.yml` runs TODO echo steps. It does not prove build, discovery, import safety, parser behavior, product isolation, candidate routing, or receipt emission.

[Back to top](#top)

---

<a id="compatibility-topology-and-migration"></a>

## Compatibility, topology, and migration

The source root must not silently resolve repository topology conflicts.

Current conflicts include:

- nested [`connectors/nrcs/scan/`](../scan/README.md) versus flat `connectors/nrcs-scan/`;
- nested [`connectors/nrcs/ssurgo/`](../ssurgo/README.md) versus flat `connectors/nrcs-ssurgo/`;
- gSSURGO descriptor, source-role, support-type, and collection identity;
- gNATSGO product identity and fill/generalization lineage;
- documentation-rich package plans versus an empty executable namespace.

Until accepted migration decisions exist:

- do not create two executable adapters for one product;
- do not duplicate schedules, descriptors, fixtures, caches, or receipt lineages;
- do not use import aliases to hide path conflict;
- do not deprecate a sibling lane by README assertion;
- do not let callers select whichever path happens to import successfully.

A migration requires an ADR or migration note, a single implementation owner, consumer inventory, compatibility period, redirects or explicit denials, duplicate-run prevention, receipt-lineage continuity, correction implications, tested rollback, and documentation updates across all affected roots.

[Back to top](#top)

---

<a id="proposed-future-tree"></a>

## Proposed future tree

The following tree is a **PROPOSED decomposition**, not repository fact:

```text
connectors/nrcs/src/
├── README.md
└── nrcs/
    ├── README.md
    ├── __init__.py
    ├── models.py
    ├── results.py
    ├── reasons.py
    ├── configuration.py
    ├── profiles.py
    ├── activation.py
    ├── transport.py
    ├── integrity.py
    ├── handoff.py
    ├── registry.py
    └── products/
        ├── __init__.py
        ├── sda.py
        ├── scan.py
        ├── ssurgo.py
        ├── gssurgo.py
        └── gnatsgo.py
```

Admission rules:

- add only the smallest module required by an accepted contract and test;
- do not scaffold every proposed file at once;
- keep product semantics in product adapters;
- keep schemas, policies, registries, fixtures, data, receipts, proofs, and release records outside `src/`;
- update package metadata, tests, and docs in the same change when behavior becomes real;
- record rollback targets before operational adoption.

[Back to top](#top)

---

<a id="smallest-sound-implementation-sequence"></a>

## Smallest sound implementation sequence

### Stage 0 — settle packaging

Accept the build backend, Python range, package discovery, dependencies, license, distribution/import naming, wheel contents, and version policy.

### Stage 1 — ratify shared contracts

Accept configuration/profile references, adapter protocol, finite result/issue/reason families, candidate handoff, and runner interaction facts in their owning contract/schema homes.

### Stage 2 — add import-safe primitives

Implement immutable value objects and result containers only. No network, filesystem, lifecycle writes, or source-specific parsing.

### Stage 3 — prove the package boundary

Build and install the wheel in isolation; test imports, discovery, exports, dependency absence, and no side effects.

### Stage 4 — add one fixture-only product adapter

Select one product through governance. Require its accepted identity, product profile, fixtures, parser contract, negative tests, correction behavior, and rollback plan.

### Stage 5 — integrate an owning runner

Add explicit network opt-in, activation checks, transport limits, idempotency, RAW/QUARANTINE persistence, and receipt emission outside the package.

### Stage 6 — replace TODO-only CI

Add substantive package build, import-safety, product-isolation, candidate-routing, and receipt-presence assertions.

### Stage 7 — expand one product at a time

Never add generic fallback behavior. Each product remains independently reviewable, correctable, deprecable, and reversible.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

This source root is not implementation-complete until all applicable items are verified:

- [ ] owners and CODEOWNERS/path protections are accepted;
- [ ] build backend, Python range, dependencies, discovery, license, and wheel contents are explicit;
- [ ] isolated build and install succeed reproducibly;
- [ ] `nrcs` is the accepted import namespace and shadow modules are absent;
- [ ] public exports and compatibility policy are documented;
- [ ] imports are side-effect-free under tests;
- [ ] shared contracts and schemas exist in their owning roots;
- [ ] source activation and product profiles are machine-resolvable;
- [ ] product adapters preserve native identity, time, quality, scale, rights, sensitivity, sovereignty, and lineage;
- [ ] unknown products and profiles fail closed;
- [ ] network is off by default and runner transport limits are enforced;
- [ ] source code performs no direct lifecycle, receipt, proof, release, API, UI, or tile writes;
- [ ] fixtures are governed and remain outside `src/`;
- [ ] package build, import, parser, adversarial, correction, and rollback tests pass;
- [ ] substantive CI replaces TODO-only connector gates;
- [ ] consumers, schedules, deployments, observability, correction, and rollback are documented;
- [ ] public clients remain behind governed interfaces and released artifacts.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| ID | Question | Status |
|---|---|---|
| NRCS-SRC-001 | Who owns the source root, package metadata, shared modules, and product adapters? | NEEDS VERIFICATION |
| NRCS-SRC-002 | What build backend and supported Python range are accepted? | UNKNOWN |
| NRCS-SRC-003 | How is the `src/` package-discovery rule configured and tested? | UNKNOWN |
| NRCS-SRC-004 | Is `nrcs` the accepted import namespace and what exports are public? | NEEDS VERIFICATION |
| NRCS-SRC-005 | What direct, optional, and development dependencies are accepted? | UNKNOWN |
| NRCS-SRC-006 | What package data, typing, generated-binding, and wheel-content policy applies? | NEEDS VERIFICATION |
| NRCS-SRC-007 | Which shared configuration, profile, result, issue, reason, and handoff contracts are accepted? | NEEDS VERIFICATION |
| NRCS-SRC-008 | What runner owns network, idempotency, lifecycle writes, and receipt persistence? | UNKNOWN |
| NRCS-SRC-009 | Which SourceDescriptors and product profiles are active? | UNKNOWN |
| NRCS-SRC-010 | What transport, archive, raster, row, cell, byte, and decompression limits apply? | UNKNOWN |
| NRCS-SRC-011 | What canonicalization and digest profiles are accepted? | NEEDS VERIFICATION |
| NRCS-SRC-012 | Where do approved fixtures live and who reviews them? | NEEDS VERIFICATION |
| NRCS-SRC-013 | What build, import-safety, package-discovery, and adapter tests are required? | NEEDS VERIFICATION |
| NRCS-SRC-014 | What substantive workflow replaces the TODO-only connector gate? | UNKNOWN |
| NRCS-SRC-015 | How are nested and flat SSURGO and SCAN paths resolved? | CONFLICTED |
| NRCS-SRC-016 | What descriptor/source-role/support-type model applies to gSSURGO? | CONFLICTED |
| NRCS-SRC-017 | What accepted product identity and fill/generalization lineage applies to gNATSGO? | CONFLICTED |
| NRCS-SRC-018 | How are corrections, replay, downstream invalidation, and supersession recorded? | NEEDS VERIFICATION |
| NRCS-SRC-019 | Which consumers, schedules, deployments, and operational health signals exist? | UNKNOWN |
| NRCS-SRC-020 | What compatibility period and rollback automation apply to future package or path migrations? | NEEDS VERIFICATION |

[Back to top](#top)

---

<a id="evidence-ledger"></a>

## Evidence ledger

| Evidence | Status | What it supports |
|---|---:|---|
| Prior source-root README blob `3b267595…` | CONFIRMED | Target existed as v0.1 planning guidance. |
| Merged namespace blob `00d12e0f…` | CONFIRMED | Child package/import contract is grounded at v0.2. |
| Empty initializer blob `e69de29b…` | CONFIRMED | No package exports or executable initialization behavior. |
| `pyproject.toml` blob `c6bb1565…` | CONFIRMED | Distribution name/version only; build and discovery are unestablished. |
| Test README blob `7c65ba6e…` | CONFIRMED | Test doctrine exists; executable tests remain unproven. |
| SDA, SCAN, gSSURGO, gNATSGO boundary blobs | CONFIRMED | Product-specific preservation and anti-collapse contracts exist in documentation. |
| SSURGO v0.1 blob `601b919c…` | CONFIRMED | Nested SSURGO lane exists but remains less grounded than updated siblings. |
| Source-authority register blob `82c23722…` | CONFIRMED | Register is PROPOSED with no entries. |
| Connector-gate blob `fc36ecce…` | CONFIRMED | Workflow exists but performs TODO echo steps only. |
| Directory Rules blob `2affb080…` | CONFIRMED | `connectors/` is the source-admission implementation responsibility root. |

Evidence does not establish package buildability, source activation, executable adapters, parser correctness, substantive CI, deployment, or publication readiness.

[Back to top](#top)

---

<a id="rollback-correction-deprecation-and-migration"></a>

## Rollback, correction, deprecation, and migration

### Documentation rollback

Before merge, close or abandon the review branch. After merge, transparently revert the merge or restore the prior target blob:

```text
3b26759548ddaf52eb5b6de0e25dfa354e1d62ec
```

### Future implementation rollback

Every implementation change must record:

- prior build metadata, dependency lock state, package/profile/adapter versions;
- affected runners, fixtures, receipts, candidates, caches, and consumers;
- correction or replay requirements;
- tested restoration command and rollback target;
- conditions that require disabling the adapter rather than restoring it.

### Correction and supersession

Do not overwrite historical source responses, parsed candidates, or receipts. Introduce a new adapter/profile version, identify affected interactions, preserve original and corrected artifacts, replay only under an approved plan, propagate correction references, and update docs/tests/fixtures.

### Deprecation

Deprecation requires a consumer inventory, replacement path, warning period, removal criteria, migration tests, and rollback plan. An undocumented import alias is not a migration strategy.

### Path migration

Any consolidation of flat and nested NRCS lanes requires an ADR or migration note, one implementation owner, duplicate-run prevention, descriptor and receipt-lineage continuity, compatibility documentation, correction analysis, and reversible rollback.

---

> **Maintainer summary:** `connectors/nrcs/src/` is a source-layout and implementation-admission boundary for the empty `nrcs` package scaffold. It governs package discovery, module placement, dependency direction, product isolation, runner handoff, tests, and reversibility. It does not activate sources, define authority, write lifecycle stores, or publish public truth.

[Back to top](#top)
