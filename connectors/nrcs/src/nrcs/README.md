<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-nrcs-src-nrcs-readme
title: connectors/nrcs/src/nrcs/ — NRCS Connector Python Namespace and Shared Source-Admission Boundary
type: readme
version: v0.2
status: draft; repository-grounded; empty-namespace; api-unratified; source-admission-only; non-authoritative
owners: OWNER_TBD — Connector steward · Source steward · NRCS steward · Package steward · Soil steward · Agriculture steward · Hydrology steward · Atmosphere/Climate steward · Rights reviewer · Sensitivity reviewer · Tribal/sovereignty reviewer · Security steward · Validation steward · Contract steward · Schema steward · Receipt steward · Migration steward · CI steward · Docs steward
created: 2026-06-20
updated: 2026-07-15
supersedes: v0.1 planning-oriented Python package guide (2026-06-20)
policy_label: "public-doctrine; connector-package-boundary; nrcs; python-namespace; implementation-empty; api-unratified; source-inactive; product-isolated; descriptor-gated; no-network-by-default; import-side-effect-free; fixture-first; raw-quarantine-only; rights-aware; sensitivity-aware; sovereignty-aware; provenance-preserving; finite-outcomes; no-publication; rollback-aware; no-secrets"
current_path: connectors/nrcs/src/nrcs/README.md
truth_posture: CONFIRMED target v0.1 README, parent source-root README, NRCS family README, NRCS test-root README, kfm-connector-nrcs 0.0.0 placeholder metadata, empty package initializer, grounded SDA/SCAN/gSSURGO/gNATSGO product boundaries, SSURGO v0.1 nested boundary, empty PROPOSED source-authority register, TODO-only connector-gate workflow, and bounded absence of selected shared modules, product modules, import-safety tests, descriptor-gate tests, and dedicated NRCS workflows / PROPOSED shared package architecture, explicit product-adapter registration, typed configuration and result families, dependency direction, import/network/resource controls, identity/time/digest preservation, finite outcomes, runner handoff, testing, migration, correction, deprecation, and rollback / CONFLICTED rich documentation versus empty executable namespace, shared-helper proposals versus product-specific contracts, SSURGO and SCAN nested-versus-flat placement, gSSURGO descriptor/source-role/support-type identity, and gNATSGO product identity / UNKNOWN accepted build backend, Python range, dependencies, public exports, product-adapter API, source activation, endpoint profiles, schemas, live behavior, fixtures, tests, substantive CI, schedules, receipts, deployment, consumers, and runtime health
base_commit: f55fe7937ee122e47b6c274630192504ecde9f8f
prior_blob: 3e022257cc553e8661b988e9e01c61cccc1fddc8
related:
  - ./__init__.py
  - ../README.md
  - ../../README.md
  - ../../tests/README.md
  - ../../pyproject.toml
  - ../../sda/README.md
  - ../../scan/README.md
  - ../../ssurgo/README.md
  - ../../gssurgo/README.md
  - ../../gnatsgo/README.md
  - ../../../README.md
  - ../../../nrcs-ssurgo/README.md
  - ../../../nrcs-scan/README.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/adr/ADR-0017-source-descriptor-admission-process.md
  - ../../../../control_plane/source_authority_register.yaml
  - ../../../../data/raw/
  - ../../../../data/quarantine/
  - ../../../../data/receipts/
  - ../../../../data/proofs/
  - ../../../../contracts/
  - ../../../../schemas/
  - ../../../../policy/rights/
  - ../../../../policy/sensitivity/
  - ../../../../release/
  - ../../../../.github/workflows/connector-gate.yml
tags: [kfm, connectors, nrcs, python, namespace, package, source-admission, import-safety, no-network, descriptor-gate, product-adapter, sda, scan, ssurgo, gssurgo, gnatsgo, provenance, raw, quarantine, finite-outcomes, correction, migration, rollback]
notes:
  - "This revision changes only connectors/nrcs/src/nrcs/README.md."
  - "Current repository evidence establishes an empty initializer and documentation only; no accepted package API or executable product adapter is claimed."
  - "The package must not flatten product-specific source roles, identities, time models, scale, quality, rights, sensitivity, or lineage."
  - "Live network behavior is explicit, profile-gated, descriptor-gated, bounded, and off by default."
  - "Public clients and generated answers never import or call this package directly."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# NRCS Connector Python Namespace and Shared Source-Admission Boundary

`connectors/nrcs/src/nrcs/`

> Repository-present Python namespace for future shared USDA NRCS connector implementation. Current evidence establishes an empty initializer and documentation—not an installable, exported, tested, source-activated, or CI-enforced connector package.

![status](https://img.shields.io/badge/status-draft-yellow)
![version](https://img.shields.io/badge/version-v0.2-informational)
![maturity](https://img.shields.io/badge/maturity-empty__namespace-lightgrey)
![package](https://img.shields.io/badge/package-kfm--connector--nrcs%200.0.0-blue)
![API](https://img.shields.io/badge/API-unratified-orange)
![network](https://img.shields.io/badge/network-off__by__default-critical)
![lifecycle](https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE-blue)
![publication](https://img.shields.io/badge/publication-DENIED-red)

**Quick links:** [Purpose](#purpose) · [Status](#status-and-evidence) · [Authority](#authority-and-directory-basis) · [Responsibilities](#namespace-responsibilities) · [Products](#product-adapter-boundaries) · [Imports](#import-and-dependency-contract) · [Configuration](#configuration-activation-and-network) · [Preservation](#identity-time-digest-and-parser-preservation) · [Outcomes](#finite-results-and-reason-codes) · [Lifecycle](#raw-quarantine-receipt-and-proof-boundary) · [Public boundary](#pipeline-release-public-interface-and-ai-separation) · [Security](#security-observability-and-resource-bounds) · [Testing](#testing-fixtures-and-ci) · [Tree](#proposed-module-tree) · [Implementation](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Rollback](#rollback-correction-deprecation-and-migration)

> [!IMPORTANT]
> **This README is not an API, source-activation, endpoint, dependency, or release decision.** The `nrcs` namespace exists, but the accepted build system, exports, adapters, contracts, dependencies, source profiles, tests, and runtime behavior remain unresolved.

> [!CAUTION]
> **Import is not activation, parsing is not truth, and connector success is not publication.** This namespace may eventually prepare evidence-bearing admission candidates; it may not establish source authority, domain truth, policy clearance, EvidenceBundle closure, release approval, or public safety.

---

<a id="purpose"></a>

## Purpose

This README governs shared Python implementation placed inside the NRCS connector family. It defines what future code may do, what it must preserve, and what remains outside package authority.

A conforming package may eventually provide:

- immutable configuration and profile-reference value objects;
- explicit, bounded transport adapters called by an owning runner;
- descriptor and activation-reference checks;
- product-adapter registration and dispatch;
- deterministic parsing of supplied payloads or approved fixtures;
- source-native identity, time, quality, scale, and lineage preservation;
- finite connector-local results and stable reason codes;
- RAW or QUARANTINE candidate construction;
- receipt-ready interaction facts returned to orchestration.

It must not:

- define source doctrine, SourceDescriptors, contracts, schemas, policy, or release rules;
- execute network access during import or without explicit profiles and activation context;
- write directly to lifecycle, receipt, proof, catalog, triplet, release, API, UI, or tile stores;
- merge NRCS products into a single source role, cadence, scale, quality model, or public posture;
- expose a public query proxy, generic SQL console, general-purpose download service, or public API;
- let AI-generated text or fluent summaries substitute for evidence, policy, or review state.

[Back to top](#top)

---

<a id="status-and-evidence"></a>

## Status and evidence

### Current repository state

| Surface | Status | Safe conclusion |
|---|---:|---|
| This README | **CONFIRMED v0.1 before revision** | A planning-oriented namespace guide existed. |
| [`__init__.py`](./__init__.py) | **CONFIRMED empty** | No exports, initialization logic, or package behavior are established. |
| [`pyproject.toml`](../../pyproject.toml) | **CONFIRMED minimal** | Only distribution name `kfm-connector-nrcs` and version `0.0.0` are declared. |
| Build backend, Python range, dependencies, package discovery | **NOT ESTABLISHED** | Installability and supported environments are unknown. |
| Shared modules named by v0.1 | **NOT FOUND at bounded paths** | `config.py`, `client.py`, `descriptors.py`, `envelope.py`, and `errors.py` are not implementation facts. |
| Product modules | **NOT FOUND at bounded paths** | `products/sda.py`, `scan.py`, `ssurgo.py`, `gssurgo.py`, and `gnatsgo.py` are not implemented at those paths. |
| Test implementation | **NOT FOUND at selected paths** | `test_import_safety.py` and `test_descriptor_gates.py` are absent. |
| Dedicated NRCS workflow | **NOT FOUND at selected paths** | `.github/workflows/nrcs.yml` and `nrcs-connector.yml` are absent. |
| Generic connector gate | **CONFIRMED TODO-only** | Its green state cannot prove connector behavior. |
| Source authority register | **CONFIRMED empty / PROPOSED** | No NRCS product activation can be inferred. |

### Truth labels

| Label | Meaning here |
|---|---|
| **CONFIRMED** | Directly verified from current repository content or exact path checks. |
| **PROPOSED** | Candidate package design that requires implementation and review. |
| **CONFLICTED** | Current docs or paths express competing identities, roles, or homes. |
| **UNKNOWN** | Runtime or governance state was not established. |
| **NEEDS VERIFICATION** | Checkable before implementation or release, but not yet resolved. |

[Back to top](#top)

---

<a id="authority-and-directory-basis"></a>

## Authority and Directory Rules basis

`connectors/` is the implementation root for source-specific fetch, probe, parse, and admission support. The path is appropriate for an importable implementation namespace because its primary responsibility is source admission—not domain meaning or publication.

Responsibility remains separated:

| Concern | Owning surface |
|---|---|
| Source-family and product explanation | `docs/sources/catalog/` |
| Source identity and activation | `data/registry/sources/` and accepted control-plane records |
| Semantic meaning | `contracts/` |
| Machine shape | `schemas/` |
| Rights and sensitivity decisions | `policy/rights/`, `policy/sensitivity/` |
| Executable downstream normalization | `pipelines/`, `pipeline_specs/` |
| Fixtures and tests | `fixtures/`, `tests/`, or the accepted connector-local test convention |
| Lifecycle data | `data/raw/`, `data/quarantine/`, then governed downstream stages |
| Receipts and proofs | `data/receipts/`, `data/proofs/` |
| Release, correction, and rollback decisions | `release/`, accepted rollback/correction homes |
| Public access | governed API and released artifacts only |

This package consumes references to those authorities. It does not replace them or create parallel authority.

[Back to top](#top)

---

<a id="namespace-responsibilities"></a>

## Namespace responsibilities

### Shared responsibilities

Code belongs in the shared namespace only when the behavior is genuinely common across NRCS products and does not erase product semantics. Candidate shared areas include:

- immutable configuration and explicit endpoint/profile references;
- bounded transport primitives;
- credential-provider interfaces that return secrets without persisting or logging them;
- descriptor/activation reference verification;
- digest and canonicalization delegation to accepted shared libraries;
- common result, issue, and reason-code types;
- product-adapter registration;
- RAW/QUARANTINE candidate value objects;
- sanitized observability helpers.

### Responsibilities that remain product-specific

Keep these inside reviewed product adapters or owning product lanes:

- request/report/query vocabulary;
- source-native identifiers;
- payload and archive formats;
- tables, columns, bands, variables, units, nulls, sentinels, and quality flags;
- CRS, grid, station, geometry, survey, and key lineage;
- time kinds, cadence, freshness, vintage, and corrections;
- product-specific rights, sensitivity, sovereignty, and disclosure posture;
- product-specific anti-collapse rules.

### No generic fallback parser

An unknown product identifier must fail closed. The package must not guess a parser by media type, filename, URL, or “closest” product profile.

[Back to top](#top)

---

<a id="product-adapter-boundaries"></a>

## Product adapter boundaries

| Product | Required preservation | Current posture |
|---|---|---|
| [SDA](../../sda/README.md) | Accepted query profile, typed bounded parameters, request/response/result identity, schema, ordering, keys, cardinality, nulls, digests; deny free-form live SQL. | README-only; source inactive; adapter absent. |
| [SCAN](../../scan/README.md) | Network, station, variable, units, sensor depth, cadence, time, quality, missingness, freshness, correction, Tribal/sovereignty context. | README-only; placement conflicted; adapter absent. |
| [SSURGO](../../ssurgo/README.md) | Survey area, package vintage, package file inventory, spatial/tabular relationships, `MUKEY`/`COKEY`/`CHKEY`, scale caveats, digest. | Nested/flat placement unresolved; adapter absent. |
| [gSSURGO](../../gssurgo/README.md) | Product/package/grid/band identity, CRS, resolution, NoData, `MUKEY` joins, source-survey vintage, rasterization lineage, role/support type. | Descriptor identity and role/support type conflicted; adapter absent. |
| [gNATSGO](../../gnatsgo/README.md) | Accepted product identity, grid/band/attribute identity, CRS, resolution, native joins, fill/generalization lineage, vintage, correction. | Product identity unsettled; adapter absent. |

The package must not convert:

```text
SDA query response -> complete SSURGO package
SCAN station -> county/watershed/raster truth
SSURGO map unit -> parcel or field verification
gSSURGO cell size -> survey precision
gNATSGO filled/generalized value -> direct observation
connector success -> evidence closure or public release
```

[Back to top](#top)

---

<a id="import-and-dependency-contract"></a>

## Import and dependency contract

Importing `nrcs` or any submodule must be side-effect-free:

- no network or DNS calls;
- no credential, token, cookie, private-session, or ambient environment reads;
- no filesystem writes, cache creation, temp-file creation, or data discovery;
- no database connections or lifecycle-store access;
- no thread, process, scheduler, telemetry exporter, or logging-handler startup;
- no source activation checks against live systems;
- no registration that mutates global application state;
- no public claims, release artifacts, or UI/API state.

Allowed dependency direction:

```text
approved runner / orchestration
  -> nrcs shared namespace
      -> explicit product adapter
          -> accepted shared pure libraries
```

Disallowed direction:

```text
nrcs package
  -X-> public apps or UI
  -X-> release decision code
  -X-> canonical lifecycle stores
  -X-> product doctrine or registries as writable state
  -X-> pipeline orchestration
```

Third-party dependencies require pinned versions, license review, offline behavior, import-safety tests, resource limits, and a rollback plan. Optional product dependencies must fail with an explicit typed outcome rather than silently changing behavior.

[Back to top](#top)

---

<a id="configuration-activation-and-network"></a>

## Configuration, activation, and network

Configuration must be explicit and immutable. A live request requires, at minimum:

- product identifier and adapter version;
- active SourceDescriptor/activation reference;
- approved endpoint and operation profile;
- rights and sensitivity review references;
- timeout, retry, redirect, response-size, archive, and decompression limits;
- caller/run identity and receipt context;
- explicit network enablement.

Defaults:

```text
network_enabled = false
source_activation = unresolved
unknown_product = deny
unknown_profile = deny
unknown_rights = quarantine_or_deny
unknown_sensitivity = quarantine_or_deny
unbounded_response = deny
```

Transport must enforce host allowlists, HTTPS requirements where applicable, redirect revalidation, SSRF defenses, bounded retries with jitter, rate limits, response and decompression ceilings, and sanitized errors. Mutation operations are denied unless a separately governed scope explicitly permits them; this package is expected to be read-only.

[Back to top](#top)

---

<a id="identity-time-digest-and-parser-preservation"></a>

## Identity, time, digest, and parser preservation

### Layered identity

Do not collapse these identities:

1. source family;
2. SourceDescriptor and activation decision;
3. product or collection;
4. endpoint/operation profile;
5. request/query/package/station/grid identity;
6. retrieved payload bytes and digest;
7. parsed record/result identity;
8. correction or supersession identity;
9. adapter and schema/profile versions.

### Time kinds

Preserve applicable time kinds separately:

- observation or source-effective time;
- report/query period;
- package/product release time;
- constituent survey or source vintage;
- retrieval time;
- processing/parse time;
- correction/supersession time;
- freshness evaluation time.

### Digests

Use accepted shared canonicalization and hashing contracts. The namespace must not invent a local “almost canonical” profile. Keep distinct, when applicable:

- request/query/template digest;
- parameter digest;
- raw response or package digest;
- manifest/file-set digest;
- parsed-result digest;
- fixture digest.

A matching digest proves declared byte/profile equality only. It does not prove source authority, semantic correctness, rights, policy, evidence closure, or release.

### Parsing

Parsers must preserve unknown fields or explicitly report them, retain source-native order where material, distinguish missing/null/sentinel/invalid, reject silent coercion, report partial/truncated results, and return schema drift as a typed issue. Silent “repair” is prohibited unless an accepted transform contract and receipt make it explicit.

[Back to top](#top)

---

<a id="finite-results-and-reason-codes"></a>

## Finite results and reason codes

A future API should return typed connector-local results rather than booleans or unbounded exceptions.

Proposed outcome family:

```text
ADMIT_RAW_CANDIDATE
ROUTE_QUARANTINE_CANDIDATE
NO_CHANGE
NOT_MODIFIED
DENY
RETRYABLE_FAILURE
PERMANENT_FAILURE
UNSUPPORTED_PRODUCT
UNSUPPORTED_PROFILE
```

Proposed reason-code families:

```text
NRCS.ACTIVATION.*
NRCS.PROFILE.*
NRCS.TRANSPORT.*
NRCS.INTEGRITY.*
NRCS.SCHEMA.*
NRCS.IDENTITY.*
NRCS.TIME.*
NRCS.RIGHTS.*
NRCS.SENSITIVITY.*
NRCS.SOVEREIGNTY.*
NRCS.RESOURCE.*
NRCS.PRODUCT.*
NRCS.INTERNAL.*
```

These names are **PROPOSED**, not an accepted contract. Each result should carry product/profile versions, source and request identity, relevant digests, timestamps, issues, and receipt-ready facts without claiming downstream authority.

[Back to top](#top)

---

<a id="raw-quarantine-receipt-and-proof-boundary"></a>

## RAW, QUARANTINE, receipt, and proof boundary

The library should return immutable candidates to an owning runner. The runner—not the package—owns persistence, idempotency, transaction boundaries, receipt emission, and retry scheduling.

```text
external source or approved fixture
  -> explicit runner
  -> descriptor/profile/policy preflight
  -> nrcs package + product adapter
  -> typed result
      -> RAW candidate
      -> QUARANTINE candidate
      -> no-change / denial / failure receipt facts
  -> owning lifecycle and receipt writers
```

The package must not write directly to:

- `data/raw/` or `data/quarantine/`;
- `data/work/`, `data/processed/`, catalog, triplet, or published stores;
- `data/receipts/` or `data/proofs/`;
- release manifests, correction notices, or rollback cards.

Receipt-ready facts are not a receipt until written under the accepted receipt contract. A receipt is not an EvidenceBundle. An EvidenceBundle is not release approval.

[Back to top](#top)

---

<a id="pipeline-release-public-interface-and-ai-separation"></a>

## Pipeline, release, public interface, and AI separation

The package may parse and preserve source material. It may not:

- normalize source data into canonical Soil, Agriculture, Hydrology, or Atmosphere objects;
- aggregate, interpolate, rasterize, generalize, redact, or model values without accepted downstream transforms;
- create catalog/triplet truth or EvidenceBundle closure;
- approve rights, sensitivity, sovereignty, or geoprivacy decisions;
- create release candidates, manifests, public tiles, API responses, UI state, notifications, or generated answers.

Public clients use governed APIs and released artifacts only. AI may interpret evidence after retrieval and policy checks; it must not call this package as a substitute for evidence resolution, source activation, or release state.

[Back to top](#top)

---

<a id="security-observability-and-resource-bounds"></a>

## Security, observability, and resource bounds

Required controls include:

- no secrets in code, configuration committed to the repository, fixtures, logs, exceptions, or receipts;
- host and operation allowlists;
- bounded URL, header, query, body, response, row, cell, table, file, archive, raster, and decompression sizes;
- archive path traversal, symlink, nested-archive, and compression-bomb defenses;
- XML/entity, CSV/formula, JSON depth, binary-header, raster-dimension, and malformed-encoding defenses as applicable;
- no raw sensitive payloads in logs;
- structured event names, stable reason codes, and redacted identifiers;
- metrics that avoid high-cardinality source-native IDs unless approved;
- deterministic idempotency keys derived from accepted identity inputs;
- no ambient cross-run cache; any cache must be bounded, keyed by profile and digest, and invalidated on correction.

Errors shown to public surfaces must be mapped by governed callers. Internal connector errors must never leak credentials, source-private parameters, filesystem paths, or raw payload excerpts.

[Back to top](#top)

---

<a id="testing-fixtures-and-ci"></a>

## Testing, fixtures, and CI

Default tests must run with network blocked and no credentials or private sessions.

Minimum test families:

- import safety for package and every adapter;
- unknown product/profile denial;
- descriptor/activation gate failure;
- rights, sensitivity, and sovereignty fail-closed behavior;
- timeout, redirect, retry, rate, response-size, and decompression limits;
- malformed payload, schema drift, unknown field, truncation, null/sentinel, encoding, and archive attacks;
- deterministic digests and replay;
- RAW/QUARANTINE result construction without direct writes;
- product anti-collapse cases from each product README;
- sanitized logs and finite reason codes;
- compatibility and correction regression tests.

Fixtures must be synthetic, minimized, redacted, or explicitly approved snapshots with product/profile identity, purpose, source/retrieval or creation date, digest, rights/sensitivity review, expected behavior, and safe-use rationale.

Current CI limitation: `.github/workflows/connector-gate.yml` only echoes TODO commands. A green run proves orchestration only; it does not prove this package contract.

[Back to top](#top)

---

<a id="proposed-module-tree"></a>

## Proposed module tree

The current namespace contains only this README and an empty initializer. The following is **PROPOSED**, not repository fact:

```text
nrcs/
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

Placement rules:

- shared code must be demonstrably cross-product;
- product semantics stay in product adapters;
- contracts, schemas, policy, registries, fixtures, tests, receipts, and data stay in their owning roots;
- no adapter is added before its product identity, activation, profile, fixture, tests, and rollback are reviewable.

[Back to top](#top)

---

<a id="smallest-sound-implementation-sequence"></a>

## Smallest sound implementation sequence

1. **Settle package metadata** — build backend, Python range, discovery, dependencies, license, and import name.
2. **Ratify shared contracts** — configuration, profiles, adapter protocol, result/issue/reason families, candidate handoff.
3. **Add import-safe primitives** — pure value objects only; no network or writes.
4. **Add one fixture-only pilot adapter** — selected by governance, with approved product profile and negative tests.
5. **Add runner integration** — explicit network opt-in, descriptor gating, transport limits, idempotency, and receipt writer.
6. **Add substantive CI** — network-blocked tests and connector-output/receipt assertions.
7. **Expand one product at a time** — never by generic fallback.
8. **Document consumers, compatibility, correction, and rollback** before operational use.

Do not implement all proposed modules in one broad scaffold. Each stage should be independently reviewable and reversible.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

This namespace is not implementation-complete until all applicable items are verified:

- [ ] owners and CODEOWNERS/path protections are accepted;
- [ ] build metadata and install/import behavior are reproducible;
- [ ] public exports and compatibility policy are documented;
- [ ] imports are side-effect-free under tests;
- [ ] accepted shared contracts and schemas exist outside this package;
- [ ] source activation and product profiles are machine-resolvable;
- [ ] product adapters preserve native identity, time, quality, scale, rights, sensitivity, and lineage;
- [ ] network is off by default and transport limits are enforced;
- [ ] finite outcomes and reason codes are accepted;
- [ ] package code performs no direct lifecycle, receipt, proof, release, API, or UI writes;
- [ ] fixtures and negative tests are governed;
- [ ] substantive CI replaces TODO-only connector gates;
- [ ] consumers, schedules, receipts, deployment, observability, correction, and rollback are documented and tested;
- [ ] public clients remain behind governed interfaces and released artifacts.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| ID | Question | Status |
|---|---|---|
| NRCS-PKG-001 | Who owns the package and product adapters? | NEEDS VERIFICATION |
| NRCS-PKG-002 | What build backend, Python range, discovery rule, and dependency set are accepted? | UNKNOWN |
| NRCS-PKG-003 | Is `nrcs` the accepted import namespace and what are its public exports? | NEEDS VERIFICATION |
| NRCS-PKG-004 | What shared configuration/result/issue/reason contracts are accepted? | NEEDS VERIFICATION |
| NRCS-PKG-005 | What adapter registration and unknown-product behavior are accepted? | NEEDS VERIFICATION |
| NRCS-PKG-006 | Which SourceDescriptors and NRCS products are active? | UNKNOWN |
| NRCS-PKG-007 | Which endpoint and operation profiles are approved? | UNKNOWN |
| NRCS-PKG-008 | What transport, response, archive, raster, row, and decompression limits apply? | UNKNOWN |
| NRCS-PKG-009 | What canonicalization and digest profiles are accepted? | NEEDS VERIFICATION |
| NRCS-PKG-010 | What candidate and receipt schemas are accepted? | NEEDS VERIFICATION |
| NRCS-PKG-011 | Where do approved fixtures live and who reviews them? | NEEDS VERIFICATION |
| NRCS-PKG-012 | What runner owns network, lifecycle writes, idempotency, and receipt persistence? | UNKNOWN |
| NRCS-PKG-013 | How are corrections, supersessions, replay, and downstream propagation recorded? | NEEDS VERIFICATION |
| NRCS-PKG-014 | How are SSURGO and SCAN nested-versus-flat paths resolved? | CONFLICTED |
| NRCS-PKG-015 | What descriptor/source-role/support-type model applies to gSSURGO? | CONFLICTED |
| NRCS-PKG-016 | What accepted product identity and fill/generalization lineage applies to gNATSGO? | CONFLICTED |
| NRCS-PKG-017 | What Tribal/sovereignty and exact-location review applies to SCAN? | NEEDS VERIFICATION |
| NRCS-PKG-018 | Where is SDA query-profile authority stored? | NEEDS VERIFICATION |
| NRCS-PKG-019 | What tests and substantive workflow enforce the namespace contract? | UNKNOWN |
| NRCS-PKG-020 | Which consumers, schedules, deployments, and operational health signals exist? | UNKNOWN |

[Back to top](#top)

---

<a id="rollback-correction-deprecation-and-migration"></a>

## Rollback, correction, deprecation, and migration

### Documentation rollback

Before merge, close or abandon the review branch. After merge, restore the prior blob or transparently revert the merge:

```text
3e022257cc553e8661b988e9e01c61cccc1fddc8
```

### Future code rollback

Every implementation change must record:

- prior package/profile/adapter versions;
- affected runners, fixtures, receipts, candidates, and consumers;
- dependency and cache implications;
- correction or replay requirements;
- tested restoration procedure and rollback target.

### Correction and supersession

Do not mutate historical receipts or parsed results. Issue a new adapter/profile version, identify affected interactions, replay only under an approved plan, preserve original and corrected artifacts, propagate correction references, and update docs/tests/fixtures.

### Path migration

Any consolidation of flat and nested NRCS connector lanes requires an ADR or migration note, redirects or compatibility documentation, a single implementation owner, duplicate-schedule prevention, receipt-lineage continuity, and a reversible rollback plan.

---

> **Maintainer summary:** `connectors/nrcs/src/nrcs/` is an empty, non-authoritative Python namespace scaffold for future shared NRCS source-admission implementation. It must preserve product-specific meaning, remain import-safe and network-off by default, return finite RAW/QUARANTINE candidates and receipt-ready facts, and stay outside evidence closure, policy approval, release, public interfaces, and generated truth.

[Back to top](#top)
