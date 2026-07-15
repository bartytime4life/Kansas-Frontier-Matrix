<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-nrcs-readme
title: connectors/nrcs/ — NRCS Connector Family and Source-Admission Boundary
type: readme
version: v0.2
status: draft; repository-grounded; connector-family-boundary; implementation-placeholder; source-inactive; non-authoritative
owners: OWNER_TBD — Connector steward · Source steward · NRCS steward · Package steward · Soil steward · Agriculture liaison · Hydrology liaison · Atmosphere/Climate liaison · Tribal/sovereignty reviewer · Rights reviewer · Sensitivity reviewer · Security steward · Validation steward · Contract steward · Schema steward · Receipt steward · Migration steward · CI steward · Docs steward
created: 2026-06-20
updated: 2026-07-15
supersedes: v0.1 planning-oriented NRCS connector-family guide
policy_label: "public-doctrine; connector-family-boundary; nrcs; source-inactive; implementation-placeholder; product-isolated; descriptor-gated; no-network-by-default; fixture-first; rights-aware; sensitivity-aware; sovereignty-aware; raw-quarantine-only; watcher-non-publisher; no-publication; migration-required; rollback-aware"
current_path: connectors/nrcs/README.md
truth_posture: CONFIRMED repository-present NRCS family README, merged source-root/namespace/test v0.2 boundaries, grounded SDA/SCAN/SSURGO/gSSURGO/gNATSGO boundaries, kfm-connector-nrcs 0.0.0 placeholder metadata, empty initializer, empty PROPOSED source-authority register, proposed source-admission ADR, TODO-only connector workflow, SCAN/SSURGO topology conflicts, and bounded absence of shared/product modules, named tests, fixture root, package-local test configuration, and dedicated NRCS workflows / PROPOSED family contract, shared-kernel limits, product-adapter admission, finite outcomes, runner handoff, tests, CI, correction, migration, and rollback / CONFLICTED documentation-rich product contracts versus empty executable package, SCAN and SSURGO placement, source-role versus support-type vocabularies, and root pytest availability versus absent package build/discovery / UNKNOWN accepted owners, canonical topology, active SourceDescriptors, approved source surfaces, dependencies, exports, consumers, fixtures, substantive CI, schedules, receipts, deployment, and runtime health
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 96ae9619f3d38daeb7a2881c0ae691e31314177c
  prior_blob: 888236f218fc0892c54c947c0c2651b34ca5137b
  source_root_blob: 7edac87aec3ff4ed5621dedd5c31ebaa2b04759a
  namespace_blob: 00d12e0f07e53cff877e9ea4d396c96b3fb03658
  tests_blob: 929ca9a819e40f1b95d829e35d573603a2407b94
  package_metadata_blob: c6bb1565db7df490bee52a597d04d694e2b9f8a4
  namespace_initializer_blob: e69de29bb2d1d6434b8b29ae775ad8c2e48c5391
  sda_blob: 6f3ba95d70ae0779d00e26ad360f7b8737dbf77a
  scan_blob: 76eb5a0683e571d045d01d7e8dc387ef497ba958
  ssurgo_blob: 357efa694fb059ed91eed3bc2b78829b673f14c3
  gssurgo_blob: 3ad1db6721224232f4e5eb99440a7b031bdb7afa
  gnatsgo_blob: 83b3816033fc558fd552480edefdde978488ccfd
  flat_scan_blob: e4e5ffe1a64ec533f4ff15503270e7cd570432b6
  flat_ssurgo_blob: a161b2aa80fa3192c0a007a04e000a43c07eba49
  standalone_ssurgo_alias_blob: bc6370b9206e22ce4f2657d9ce8fb28111244f40
  source_authority_register_blob: 82c23722520922f5ca0dad7f37ed794d1c2edf81
  source_admission_adr_blob: 0e8d03786bcc99b19f179680890df9e30a27633a
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  connector_gate_workflow_blob: fc36ecced55bb0b4002d551cb28addfff0be918a
  bounded_path_checks:
    - source-root, namespace, tests, SDA, SCAN, SSURGO, gSSURGO, and gNATSGO READMEs are grounded at v0.2
    - pyproject.toml contains only project name kfm-connector-nrcs and version 0.0.0
    - src/nrcs/__init__.py is empty
    - selected shared modules and all five product modules were not found
    - selected safety/product tests and fixture-root README were not found
    - package-local pytest/tox configuration was not found
    - dedicated NRCS workflows were not found
    - source-authority register is PROPOSED with entries []
    - connector-gate workflow contains TODO echo steps
related:
  - ../README.md
  - ./src/README.md
  - ./src/nrcs/README.md
  - ./tests/README.md
  - ./pyproject.toml
  - ./sda/README.md
  - ./scan/README.md
  - ./ssurgo/README.md
  - ./gssurgo/README.md
  - ./gnatsgo/README.md
  - ../nrcs-scan/README.md
  - ../nrcs-ssurgo/README.md
  - ../ssurgo/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0017-source-descriptor-admission-process.md
  - ../../docs/sources/catalog/nrcs.md
  - ../../docs/sources/catalog/nrcs/README.md
  - ../../control_plane/source_authority_register.yaml
  - ../../data/raw/
  - ../../data/quarantine/
  - ../../data/receipts/
  - ../../data/proofs/
  - ../../contracts/
  - ../../schemas/
  - ../../policy/rights/
  - ../../policy/sensitivity/
  - ../../release/
  - ../../.github/workflows/connector-gate.yml
tags: [kfm, connectors, nrcs, connector-family, source-admission, product-isolation, sda, scan, ssurgo, gssurgo, gnatsgo, soil, agriculture, hydrology, atmosphere, no-network, fixture-first, raw, quarantine, provenance, rights, sensitivity, sovereignty, migration, correction, rollback]
notes:
  - "This revision changes only connectors/nrcs/README.md."
  - "Current evidence establishes grounded documentation and an empty 0.0.0 package scaffold, not an operational connector family."
  - "The family coordinates product boundaries; it does not replace source descriptors, doctrine, schemas, contracts, policy, tests, pipelines, receipts, proofs, release records, or public interfaces."
  - "Connector code may return RAW or QUARANTINE candidates and receipt-ready facts; orchestration owns persistence and receipt emission."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# NRCS Connector Family and Source-Admission Boundary

`connectors/nrcs/`

> Repository-present coordination and implementation boundary for candidate USDA Natural Resources Conservation Service connector work. Current evidence establishes grounded documentation, a minimal `0.0.0` package shell, and an empty namespace—not an active source family, approved acquisition surface, executable adapter suite, collected test suite, substantive connector gate, deployment, or release-ready data path.

![status](https://img.shields.io/badge/status-draft-yellow)
![version](https://img.shields.io/badge/version-v0.2-informational)
![maturity](https://img.shields.io/badge/maturity-documentation__scaffold-lightgrey)
![source](https://img.shields.io/badge/source__family-inactive-critical)
![package](https://img.shields.io/badge/package-0.0.0__shell-orange)
![network](https://img.shields.io/badge/network-off__by__default-critical)
![lifecycle](https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE-blue)
![publication](https://img.shields.io/badge/publication-DENIED-red)

**Quick links:** [Purpose](#purpose) · [Evidence](#status-and-evidence) · [Authority](#authority-and-directory-rules-basis) · [Tree](#confirmed-bounded-tree) · [Products](#product-lane-index) · [Invariants](#keystone-invariants) · [Activation](#source-activation-and-admission) · [Shared code](#shared-family-kernel-boundary) · [Isolation](#product-isolation-contract) · [Operations](#configuration-network-and-resource-boundary) · [Semantics](#identity-time-quality-scale-and-lineage) · [Rights](#rights-sensitivity-sovereignty-and-disclosure) · [Lifecycle](#raw-quarantine-runner-and-receipt-handoff) · [Outcomes](#finite-outcomes-and-reason-codes) · [Domains](#domain-and-consumer-boundaries) · [Tests](#tests-fixtures-and-ci) · [Topology](#topology-conflicts-and-migration) · [Implementation](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Ledger](#evidence-ledger) · [Rollback](#rollback-correction-deprecation-and-migration)

> [!IMPORTANT]
> **This README is not a source activation or implementation decision.** Path presence does not establish an admitted `SourceDescriptor`, approved source surface, buildable package, supported API, product adapter, fixtures, tests, schedule, receipt flow, deployment, or publication readiness.

> [!CAUTION]
> **NRCS is a source family, not a single data product or authority role.** SDA results, SCAN observations, SSURGO packages, gSSURGO grids, and gNATSGO grids must retain separate identity, cadence, scale, quality, support type, lineage, and public-use constraints.

> [!WARNING]
> **Connector success is not evidence closure or release.** A connector may preserve source material and return an admission candidate. It may not approve policy, resolve an `EvidenceBundle`, create a released layer, answer a public claim, or bypass the KFM lifecycle.

---

<a id="purpose"></a>

## Purpose

This README governs the NRCS connector-family boundary.

It defines:

1. the family responsibility root;
2. the verified current maturity;
3. the product-lane split;
4. the limits of shared family code;
5. the prerequisites for source activation;
6. the connector-to-runner handoff;
7. topology, test, correction, and rollback expectations.

A future conforming family may support:

- accepted source and product profile resolution;
- bounded read-only retrieval;
- deterministic no-network fixtures;
- source-native parsing;
- product-specific identity, time, quality, scale, rights, sensitivity, and lineage;
- finite connector outcomes;
- RAW or QUARANTINE candidate construction;
- receipt-ready facts;
- correction, supersession, migration, and rollback.

It must not become:

- source or product doctrine;
- a SourceDescriptor or source-authority register;
- a schema, semantic contract, policy, or release home;
- a lifecycle, receipt, proof, catalog, triplet, or published-data store;
- a scheduler or pipeline;
- a public API, UI, map, notification, or AI-answer surface;
- a generic soil connector that erases product distinctions.

[Back to top](#top)

---

<a id="status-and-evidence"></a>

## Status and evidence

| Surface | Status | Safe conclusion |
|---|---:|---|
| Family README | **CONFIRMED v0.1 before revision** | A planning-oriented family guide existed. |
| [`src/README.md`](./src/README.md) | **CONFIRMED v0.2** | Source placement and package-discovery rules are documented. |
| [`src/nrcs/README.md`](./src/nrcs/README.md) | **CONFIRMED v0.2** | Proposed import and package behavior are documented. |
| [`tests/README.md`](./tests/README.md) | **CONFIRMED v0.2** | Test and fixture admission rules are documented. |
| Package metadata | **CONFIRMED minimal** | `kfm-connector-nrcs` is version `0.0.0`. |
| Namespace initializer | **CONFIRMED empty** | No exports or runtime behavior are established. |
| Shared modules | **NOT FOUND at checked paths** | No shared family implementation is established. |
| Product modules | **NOT FOUND at checked paths** | No executable SDA, SCAN, SSURGO, gSSURGO, or gNATSGO adapter is established. |
| Named tests and fixture root | **NOT FOUND at checked paths** | No connector test coverage is established. |
| Dedicated NRCS workflow | **NOT FOUND** | No package-specific CI gate is established. |
| Generic connector workflow | **CONFIRMED TODO-only** | Green status proves orchestration only. |
| Source authority register | **CONFIRMED empty / PROPOSED** | No active NRCS source is established. |

### Truth labels

| Label | Meaning here |
|---|---|
| **CONFIRMED** | Verified from repository content or exact path checks. |
| **PROPOSED** | Candidate design requiring implementation and review. |
| **CONFLICTED** | Current paths or vocabularies express competing choices. |
| **UNKNOWN** | Runtime or governance state was not established. |
| **NEEDS VERIFICATION** | Checkable before implementation or reliance, but unresolved. |

This revision does not establish package buildability, supported Python versions, dependencies, exports, active sources, approved operations, current source formats, fixtures, tests, schedules, receipts, deployments, consumers, runtime health, or release approval.

[Back to top](#top)

---

<a id="authority-and-directory-rules-basis"></a>

## Authority and Directory Rules basis

Directory Rules place source-specific fetch, probe, parse, and admission implementation under `connectors/`. `connectors/nrcs/` is therefore the sound responsibility root for an NRCS family implementation.

Placement does not confer broader authority.

| Concern | Owning surface |
|---|---|
| Family coordination and implementation | `connectors/nrcs/` |
| Source layout | `connectors/nrcs/src/` |
| Python namespace | `connectors/nrcs/src/nrcs/` |
| Product source edge | Product lane and eventual product adapter |
| Connector tests | `connectors/nrcs/tests/` |
| Source doctrine | `docs/sources/catalog/nrcs*` |
| Source activation | SourceDescriptor, authority register, activation decision |
| Semantic contracts | `contracts/` |
| Machine schemas | `schemas/` |
| Rights and sensitivity | `policy/` and review records |
| Lifecycle stores | `data/` responsibility roots |
| Receipts and proofs | `data/receipts/`, `data/proofs/` |
| Transformation | `pipelines/` |
| Release | `release/` |
| Public access | Governed APIs and released artifacts |

A file belongs here only when its primary responsibility is NRCS-family connector coordination, safely shared connector implementation, a ratified product adapter, connector tests, package metadata, or documentation governing those responsibilities.

[Back to top](#top)

---

<a id="confirmed-bounded-tree"></a>

## Confirmed bounded tree

This is a **bounded verified surface**, not a complete-tree claim:

```text
connectors/nrcs/
├── README.md
├── pyproject.toml
├── src/
│   ├── README.md
│   └── nrcs/
│       ├── README.md
│       └── __init__.py
├── tests/
│   └── README.md
├── sda/
│   └── README.md
├── scan/
│   └── README.md
├── ssurgo/
│   └── README.md
├── gssurgo/
│   └── README.md
└── gnatsgo/
    └── README.md
```

The product and package surfaces are documentation-led. Selected implementation modules, tests, fixtures, package-local test configuration, and dedicated workflows were absent at the checked paths.

[Back to top](#top)

---

<a id="product-lane-index"></a>

## Product lane index

| Product | Evidence form | Required preservation | Current posture |
|---|---|---|---|
| [`sda/`](./sda/README.md) | Bounded query request and result set | Query-profile identity, parameters, result shape, ordering, keys, limits, digest, correction | README-only; source inactive; free-form live SQL denied |
| [`scan/`](./scan/README.md) | Station observation | Network, station, variable, time, cadence, units, sensor depth, quality, freshness, Tribal posture | README-only; placement conflicted; source inactive |
| [`ssurgo/`](./ssurgo/README.md) | Static survey-area package | Survey area, package/assets, archive safety, CRS, geometry, tables, relationships, MUKEY/COKEY/CHKEY, scale, vintage | README-only; three-lane topology conflict; source inactive |
| [`gssurgo/`](./gssurgo/README.md) | Gridded derivative | Grid, CRS, transform, resolution, bands, nodata, joins, source-survey vintage, rasterization lineage | README-only; descriptor identity conflicted; source inactive |
| [`gnatsgo/`](./gnatsgo/README.md) | National soil-grid candidate | Accepted product identity, grid, resolution, attributes, modeled/fill/generalization lineage, vintage | README-only; product identity unsettled; source inactive |

Required separation:

```text
SDA query result
  != SSURGO survey package
  != gSSURGO grid
  != gNATSGO national grid
  != SCAN station observation
  != normalized Soil object
  != current field verification
  != parcel or ownership truth
  != regulatory determination
  != released public claim
```

Other NRCS programs or documents do not become connector lanes merely because they exist in source documentation. A new lane requires verified identity, Directory Rules review, source doctrine, descriptor and activation, rights/sensitivity review, fixture-first tests, CI, and migration notes where paths overlap.

[Back to top](#top)

---

<a id="keystone-invariants"></a>

## Keystone invariants

### Lifecycle

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Connector code may support entry into RAW or QUARANTINE. It does not own later promotion.

### Watcher non-publisher

A connector may retrieve approved source material, preserve source-native structure, return a finite result, and provide receipt-ready facts. It may not write published data, approve release, mutate domain truth, or emit public claims.

### Cite or abstain

Generated language is not source truth. Where evidence, identity, rights, sensitivity, sovereignty, time, scale, quality, or release state is unresolved, downstream systems narrow, abstain, restrict, quarantine, or deny.

### Product isolation

Shared code must preserve product-specific identity, time, quality, units, depth, scale, CRS, keys, rights, sensitivity, sovereignty, correction, and lineage.

### Fail-safe defaults

Unclear configuration, activation, product identity, schema, rights, sensitivity, quality, scale, lineage, or correction state must not silently become an outward-facing result.

[Back to top](#top)

---

<a id="source-activation-and-admission"></a>

## Source activation and admission

Before live source access, a product lane requires:

- accepted source and product identity;
- canonical path or explicit compatibility classification;
- active SourceDescriptor;
- non-empty authority-register entry;
- activation decision;
- approved read-only operation profile;
- rights, attribution, retention, sensitivity, and sovereignty posture;
- source-role and support-type mapping;
- request, query, station, package, or grid profile;
- resource limits;
- correction and supersession model;
- safe fixture and negative tests;
- substantive CI;
- rollback target.

Activation permits only the approved internal source-admission path. It is not release approval.

Until activation is established, future executable code should return a finite inactive/configuration outcome without attempting network access.

[Back to top](#top)

---

<a id="shared-family-kernel-boundary"></a>

## Shared family kernel boundary

A shared family kernel is **PROPOSED** and not implemented.

Behavior may be shared only when materially identical across accepted products, such as:

- immutable configuration loading;
- profile-reference resolution;
- no-network default enforcement;
- bounded read-only transport;
- timeout and retry mechanics;
- content digests;
- temporary-storage management;
- safe diagnostics;
- connector result-envelope primitives;
- receipt-ready transport facts.

These semantics must remain product-specific:

- SDA query profiles, parameters, result shape, cardinality, and ordering;
- SCAN station/network identity, units, depth, cadence, quality, and Tribal review;
- SSURGO archive, survey-area, spatial/table inventory, relationships, and source keys;
- gSSURGO grid, resolution, bands, nodata, source-survey vintage, and rasterization lineage;
- gNATSGO product identity, national-scale caveats, modeled/fill lineage, and native joins.

A helper should be shared only when it preserves typed product inputs and outputs, avoids parser guessing, fails closed without a profile, remains testable offline, and does not redefine source, contract, schema, or policy authority.

[Back to top](#top)

---

<a id="product-isolation-contract"></a>

## Product isolation contract

Future dispatch must use an accepted typed product profile. It must not infer a product from URL fragments, filename extensions, response headers, archive contents, generic NRCS labels, model guesses, or parser fallback.

A parser mismatch must produce a finite mismatch or quarantine result. It must not fall through to another product parser merely because parsing succeeds.

Cache, idempotency, retry, and deduplication identities must include product and profile identity. Query responses, station records, survey packages, and grids must never collide because they share an NRCS publisher or a field such as `MUKEY`.

A successful parse does not promote across products. An SDA result does not replace SSURGO, SCAN does not validate a grid, and SSURGO parsing does not authorize a gSSURGO layer.

[Back to top](#top)

---

<a id="configuration-network-and-resource-boundary"></a>

## Configuration, network, and resource boundary

Future runtime configuration should provide explicit references to source, product, operation, rights, sensitivity, resource, correction, and output-candidate profiles.

Imports, constructors, and default tests must not access the network. Live operations require explicit activation and approved read-only profiles.

Each operation profile should define applicable limits for timeouts, redirects, retries, pagination, rows, cells, bytes, archive members, expansion, raster dimensions, bands, temporary storage, memory, and concurrency.

Transport must constrain destinations and revalidate redirects. Package and raster parsers must fail safely on malformed, oversized, unsupported, or ambiguous inputs.

Environment variables may provide deployment values, but they must not silently define source role, support type, activation, rights, sensitivity, schema authority, release permission, or public visibility.

No credential requirement is established. Any future credential mechanism must remain outside repository content and test fixtures.

[Back to top](#top)

---

<a id="identity-time-quality-scale-and-lineage"></a>

## Identity, time, quality, scale, and lineage

A future implementation must distinguish, where applicable:

- publisher, source, product, collection, descriptor, and operation profile;
- query, request, response, station, survey area, package, asset, table, grid, band, record, and correction identities.

Do not collapse:

- source publication, product release, source vintage, survey-area vintage, observation time, report period, request, retrieval, valid, correction, processing, and release times.

Preserve source-native:

- quality flags;
- nulls and sentinels;
- units and sensor depth;
- incomplete joins;
- missing tables or bands;
- coverage gaps;
- stale state;
- source-native identifiers.

SSURGO, gSSURGO, and gNATSGO scale or resolution must not imply parcel precision, point observation, current field condition, ownership, legal boundary, engineering-site verification, or regulatory determination.

`MUKEY`, `COKEY`, `CHKEY`, station IDs, product-native join fields, and source-native record IDs must remain inspectable. Missing keys or relationships must not be silently invented or repaired.

[Back to top](#top)

---

<a id="rights-sensitivity-sovereignty-and-disclosure"></a>

## Rights, sensitivity, sovereignty, and disclosure

Before live retrieval or fixture inclusion, verify terms, attribution, redistribution, retention, derivative permissions, automated-access restrictions, citation, and review dates.

Public availability does not automatically establish unrestricted reuse.

NRCS materials may intersect private land, agriculture, ecology, infrastructure, cultural resources, or precise locations. Connector code preserves review inputs and does not decide public disclosure.

SCAN and related materials may include Tribal program context. Public technical access does not automatically permit broader aggregation, republication, or reinterpretation. Where sovereignty or cultural sensitivity is unresolved, prefer quarantine, narrower scope, staged access, review, or denial.

Diagnostics should use profile IDs, digests, bounded counts, and reason codes rather than full source payloads, exact sensitive locations, private identifiers, or access material.

[Back to top](#top)

---

<a id="raw-quarantine-runner-and-receipt-handoff"></a>

## RAW, QUARANTINE, runner, and receipt handoff

A future adapter may return:

- finite outcome;
- product-qualified candidate;
- source/profile references;
- request and retrieval facts;
- digests and bounded counts;
- review signals;
- reason codes;
- suggested RAW or QUARANTINE disposition;
- receipt-ready facts.

It must not directly write lifecycle stores, authority records, receipts, proofs, catalogs, triplets, release records, or published artifacts.

The owning runner should validate activation, call the connector, select the governed disposition, persist atomically, emit the receipt, schedule allowed downstream work, and preserve retry/idempotency state.

| Condition | Suggested result | Runner posture |
|---|---|---|
| Source inactive or profile missing | Configuration outcome | No network |
| Retrieval and integrity clear | RAW candidate | Persist through runner and emit receipt |
| Rights, identity, schema, quality, scale, lineage, sensitivity, or correction unclear | QUARANTINE candidate | Preserve with reason codes for review |
| Source unchanged | No-change result | Avoid duplicate payload |
| Retryable source failure | Retryable result | Bounded retry outside connector |
| Policy-blocked or permanent failure | Denied/permanent result | No downstream candidate |
| Internal invariant failure | Internal error | Fail closed |

The persistence-and-receipt transaction mechanism remains **NEEDS VERIFICATION**.

[Back to top](#top)

---

<a id="finite-outcomes-and-reason-codes"></a>

## Finite outcomes and reason codes

No accepted NRCS result enum was verified. This **PROPOSED** family is illustrative:

```text
NOT_CONFIGURED
SOURCE_INACTIVE
PROFILE_INVALID
DENIED
NO_CHANGE
RAW_CANDIDATE
QUARANTINE_CANDIDATE
RETRYABLE_SOURCE_ERROR
PERMANENT_SOURCE_ERROR
INTERNAL_ERROR
```

Proposed reason-code namespaces:

```text
NRCS.CONFIG.*
NRCS.ACTIVATION.*
NRCS.RIGHTS.*
NRCS.SENSITIVITY.*
NRCS.SOVEREIGNTY.*
NRCS.PROFILE.*
NRCS.NETWORK.*
NRCS.RESOURCE.*
NRCS.INTEGRITY.*
NRCS.SCHEMA.*
NRCS.IDENTITY.*
NRCS.TIME.*
NRCS.QUALITY.*
NRCS.SCALE.*
NRCS.LINEAGE.*
NRCS.CORRECTION.*
NRCS.SDA.*
NRCS.SCAN.*
NRCS.SSURGO.*
NRCS.GSSURGO.*
NRCS.GNATSGO.*
NRCS.INTERNAL.*
```

Adoption requires a semantic contract, machine schema, registry, product mappings, tests, compatibility rules, and documentation.

[Back to top](#top)

---

<a id="domain-and-consumer-boundaries"></a>

## Domain and consumer boundaries

NRCS products may support several domains, but the connector family does not own their truth.

- **Soil:** does not define map-unit, component, horizon, property, or interpretation meaning.
- **Agriculture:** does not prove current practice, yield, management effectiveness, compliance, or private-land conditions.
- **Hydrology and hazards:** does not establish streamflow, flood determination, water rights, groundwater status, warning, or life-safety guidance.
- **Atmosphere and climate:** does not create normals, forecasts, gridded weather, drought determinations, or advisories.
- **People and land:** survey geometry is not parcel, ownership, access, title, easement, or legal boundary.
- **Engineering and regulation:** ratings and standards do not become design, permit, compliance, or regulatory decisions.

Public clients use governed APIs and released artifacts. They must not import this package, read RAW/QUARANTINE data directly, execute arbitrary queries, expose unreleased payloads, or treat generated summaries as evidence.

[Back to top](#top)

---

<a id="tests-fixtures-and-ci"></a>

## Tests, fixtures, and CI

The merged [`tests/README.md`](./tests/README.md) governs test and fixture admission.

Current evidence:

- no named NRCS tests at checked paths;
- no fixture-root README;
- no `conftest.py`;
- no package-local pytest or tox configuration;
- no dedicated NRCS workflow;
- generic connector workflow is echo-only;
- root pytest availability does not prove collection or installation.

Before implementation claims, a substantive suite should prove:

- clean build and wheel installation;
- side-effect-free imports;
- no-network defaults;
- descriptor and activation gates;
- rights, sensitivity, and sovereignty gates;
- product dispatch isolation;
- finite outcomes;
- temporary-filesystem-only behavior;
- resource limits;
- deterministic digests;
- malformed/adversarial input handling;
- product-specific positive and negative matrices;
- RAW/QUARANTINE boundaries;
- receipt-ready fact completeness;
- correction, migration, and rollback.

Fixtures must be synthetic, minimized, redacted, or explicitly approved, with product/profile identity, version, purpose, origin, date, digest, rights, review posture, expected result, and retirement path.

A future workflow must install from build output, collect a nonzero suite, deny network, run product matrices, validate fixture manifests, emit reports, and fail on zero tests or unexpected skips.

[Back to top](#top)

---

<a id="topology-conflicts-and-migration"></a>

## Topology conflicts and migration

### SCAN

```text
connectors/nrcs/scan/
connectors/nrcs-scan/
```

The nested path is the strongest family-root candidate. No migration or deprecation is ratified here.

### SSURGO

```text
connectors/nrcs/ssurgo/
connectors/nrcs-ssurgo/
connectors/ssurgo/
```

The nested path is the strongest family-root candidate. The other lanes require an ADR or migration note before implementation, redirect, tombstone, deprecation, or removal.

### Topology freeze

Until accepted decisions exist:

- do not create duplicate implementations, descriptors, schedules, fixtures, caches, receipts, or adapter registrations;
- do not silently import across compatibility lanes;
- do not allow one source run to enter multiple canonical paths.

Any migration record must identify old/new paths, ownership, source/product IDs, compatibility, import/configuration/test impact, provenance continuity, deprecation period, rollback, and documentation changes.

[Back to top](#top)

---

<a id="smallest-sound-implementation-sequence"></a>

## Smallest sound implementation sequence

### 0. Governance

- confirm owners;
- resolve path conflicts;
- pin source and product identity;
- accept role/support-type vocabulary;
- record rights, sensitivity, sovereignty, correction, and rollback.

### 1. Package

- choose build backend and supported Python versions;
- define dependencies and package discovery;
- build and install in a clean environment;
- prove side-effect-free imports;
- define public exports or intentionally keep none.

### 2. Tests

- add deterministic test controls;
- deny network by default;
- add fixture manifest and one synthetic fixture;
- require nonzero collection;
- wire substantive CI.

### 3. Minimal shared primitives

Implement only immutable configuration, profile references, finite result envelopes, digests, bounded transport, temporary storage, and safe diagnostics needed by one product.

### 4. First adapter

Choose based on governance readiness. Write negative tests first, implement fixture-only parsing, return RAW/QUARANTINE candidates and receipt-ready facts, and keep live access disabled.

### 5. Live dry run

After activation and fixture tests, allow one approved read-only operation, persist through the runner, emit a receipt, review quarantine behavior, and keep publication denied.

### 6. Additional products

Add each product independently. Generalize shared code only after at least two implemented adapters prove the behavior is truly common.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

This README is documentation-complete when:

- [ ] owners are confirmed or tracked;
- [x] current maturity is recorded;
- [x] product boundaries are explicit;
- [x] lifecycle and publication boundaries are explicit;
- [x] topology conflicts are visible;
- [x] rollback is documented.

The connector family is not implementation-complete until:

- [ ] topology is accepted;
- [ ] package metadata and discovery are complete;
- [ ] clean build/install passes;
- [ ] imports are tested;
- [ ] source/product profiles and active descriptors exist;
- [ ] rights, sensitivity, and sovereignty decisions are current;
- [ ] fixtures are approved;
- [ ] tests collect and pass;
- [ ] no-network and resource controls are enforced;
- [ ] adapters preserve product semantics;
- [ ] outcomes and reason codes are contracted;
- [ ] runner handoff and receipt pairing are tested;
- [ ] CI is substantive;
- [ ] correction, migration, deprecation, and rollback are tested;
- [ ] deployment and runtime health are verified;
- [ ] public consumers use governed interfaces only.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| ID | Question | Status |
|---|---|---|
| NRCS-FAM-001 | Who owns the family? | NEEDS VERIFICATION |
| NRCS-FAM-002 | Is this the accepted canonical family root? | PROPOSED / strong fit |
| NRCS-FAM-003 | What is the canonical SCAN path? | CONFLICTED |
| NRCS-FAM-004 | What is the canonical SSURGO path? | CONFLICTED |
| NRCS-FAM-005 | What compatibility behavior applies to other lanes? | UNKNOWN |
| NRCS-FAM-006 | What are canonical source and product IDs? | UNKNOWN |
| NRCS-FAM-007 | Which products are activated? | UNKNOWN |
| NRCS-FAM-008 | Which operations are approved? | UNKNOWN |
| NRCS-FAM-009 | What rights, sensitivity, and sovereignty rules apply? | NEEDS VERIFICATION |
| NRCS-FAM-010 | How are source role and support type separated? | CONFLICTED |
| NRCS-FAM-011 | Which build backend and Python versions are supported? | UNKNOWN |
| NRCS-FAM-012 | What dependencies and package discovery are accepted? | UNKNOWN |
| NRCS-FAM-013 | What public exports are accepted? | UNKNOWN |
| NRCS-FAM-014 | What is truly shared across products? | PROPOSED |
| NRCS-FAM-015 | What result and reason-code contracts are accepted? | UNKNOWN |
| NRCS-FAM-016 | What network and resource limits apply? | UNKNOWN |
| NRCS-FAM-017 | What cache and idempotency rules apply? | UNKNOWN |
| NRCS-FAM-018 | How are corrections and supersession modeled? | UNKNOWN |
| NRCS-FAM-019 | What fixture home and rights posture are accepted? | UNKNOWN |
| NRCS-FAM-020 | What deterministic test command and marker policy apply? | UNKNOWN |
| NRCS-FAM-021 | What substantive CI matrix applies? | UNKNOWN |
| NRCS-FAM-022 | How are RAW/QUARANTINE writes paired with receipts? | UNKNOWN |
| NRCS-FAM-023 | Which downstream pipelines consume each product? | UNKNOWN |
| NRCS-FAM-024 | What schedules and deployment exist? | UNKNOWN |
| NRCS-FAM-025 | What runtime health evidence exists? | UNKNOWN |
| NRCS-FAM-026 | How are stale or retired sources blocked? | UNKNOWN |
| NRCS-FAM-027 | Is connector CI release-blocking? | UNKNOWN |
| NRCS-FAM-028 | Are schemas enforceable rather than permissive scaffolds? | NEEDS VERIFICATION |
| NRCS-FAM-029 | Do downstream EvidenceRefs resolve to EvidenceBundles? | UNKNOWN |
| NRCS-FAM-030 | Are generated answers evidence-subordinate? | NEEDS VERIFICATION |

[Back to top](#top)

---

<a id="evidence-ledger"></a>

## Evidence ledger

| Evidence | Blob/state | Conclusion |
|---|---|---|
| Family README before revision | `888236f218fc0892c54c947c0c2651b34ca5137b` | Parent boundary required reconciliation. |
| Source root | `7edac87aec3ff4ed5621dedd5c31ebaa2b04759a` | Source layout documented; implementation empty. |
| Namespace | `00d12e0f07e53cff877e9ea4d396c96b3fb03658` | Proposed import/package behavior documented. |
| Tests | `929ca9a819e40f1b95d829e35d573603a2407b94` | Test requirements documented; suite absent. |
| Package metadata | `c6bb1565db7df490bee52a597d04d694e2b9f8a4` | Only name and `0.0.0` declared. |
| Initializer | empty blob | No exports or runtime behavior. |
| SDA | `6f3ba95d70ae0779d00e26ad360f7b8737dbf77a` | Profile-gated query boundary. |
| SCAN | `76eb5a0683e571d045d01d7e8dc387ef497ba958` | Station/depth/cadence/Tribal boundary and path conflict. |
| SSURGO | `357efa694fb059ed91eed3bc2b78829b673f14c3` | Package/key-lineage boundary and three-lane conflict. |
| gSSURGO | `3ad1db6721224232f4e5eb99440a7b031bdb7afa` | Grid/vintage/raster-lineage boundary. |
| gNATSGO | `83b3816033fc558fd552480edefdde978488ccfd` | Product identity and modeled/fill lineage unresolved. |
| Authority register | empty entries | No source activation. |
| Source-admission ADR | proposed | Process guidance, not runtime proof. |
| Connector workflow | TODO echo-only | Does not prove connector or receipt behavior. |
| Directory Rules | verified | `connectors/` owns source-specific implementation. |

This evidence supports the boundary and maturity assessment only. It does not support implementation, activation, testing, deployment, consumer, or release claims.

[Back to top](#top)

---

<a id="rollback-correction-deprecation-and-migration"></a>

## Rollback, correction, deprecation, and migration

### Documentation rollback

Before merge, close or abandon the branch.

After merge, revert the merge or restore prior blob:

```text
888236f218fc0892c54c947c0c2651b34ca5137b
```

No runtime, source, fixture, lifecycle, receipt, proof, pipeline, release, deployment, or public artifact rollback is required for this README-only revision.

### Future implementation rollback

Consider package version, imports, profile versions, source activation, cached material, idempotency, RAW/QUARANTINE records, receipts, schedules, consumers, correction state, compatibility lanes, and deployment manifests.

### Correction

Record what changed, why, affected products and runs, prior/replacement identity, review or receipt references, public impact, and rollback target. Do not silently rewrite released evidence.

### Deprecation and migration

Require a replacement, compatibility posture, warning period, consumer inventory, tests, documentation, removal criteria, provenance continuity, and rollback. No SCAN or SSURGO lane may be moved or deleted solely because another path appears cleaner.

[Back to top](#top)

---

## Status summary

`connectors/nrcs/` is the coordination and implementation boundary for a future governed NRCS connector family. Current evidence establishes grounded documentation and an empty package scaffold only.

The family is **not source-active, build-proven, adapter-complete, test-proven, CI-enforced, deployed, or publication-authoritative**.

> Preserve each NRCS product as its own source-, profile-, identity-, time-, quality-, scale-, rights-, sensitivity-, sovereignty-, lineage-, correction-, and lifecycle-scoped evidence path; return only governed admission candidates; and let downstream evidence, policy, review, release, correction, and rollback machinery decide what may become public.

<p align="right"><a href="#top">Back to top</a></p>
